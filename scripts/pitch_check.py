#!/usr/bin/env python3
"""Check the countable parts of a short-reel pitch.

    python3 pitch_check.py PITCH.md [PITCH.md ...]

A pitch is a Markdown file in the format of pitch-template.md: front matter (hook, shape, length, turn_at,
events_after_hook) and the lines **Truth:**, **We see:**, **Turn:**, **Reaction:**, **Caption:**.

This checks what can be counted: the hook's length and reading time, when the turn lands, how long the reaction
is held, the reel's length for its shape, the number of events, whether the turn is written as a spoken line,
and whether the caption asks for engagement. It cannot tell whether the turn is a surprise or whether the reel
is funny: that is what the cold read and the four stills are for.

Exit code 0 when every pitch passes, 1 when a check fails, 2 when a file cannot be read. Standard library only.
"""
import re
import sys

HOOK_MAX_WORDS = 5
TRUTH_MAX_WORDS = 10
TURN_BY = 7.0                      # seconds; unless a clock is on screen from frame 1, or a story reel
REACTION_MIN = 1.0                 # seconds the reaction is held
LENGTH = {'gag': (8, 12), 'story': (20, 30), 'clock': (6, 30)}
BAIT = [r'\btag\b', r'\bsend (this|it) to\b', r'\bcomment (if|below|your)\b', r'\bshare (this|it) with\b',
        r'\bfollow for\b', r'\blike if\b', r'\bdouble[- ]tap\b', r'\blink in bio\b']
SPEECH = [r'["“”]', r'\b(says|said|asks|asked|replies|replied|answers|shouts|whispers|tells)\b']


def words(text):
    return [w for w in re.split(r'\s+', text.strip()) if re.search(r'\w', w)]


def hook_time(n_words):
    """Seconds the hook text has to be on screen to be read."""
    return round(0.3 * n_words + 0.5, 2)


def parse(text):
    m = re.match(r'^---\r?\n(.*?)\r?\n---\r?\n?(.*)$', text, re.S)
    meta, body = {}, text
    if m:
        body = m.group(2)
        for line in m.group(1).splitlines():
            kv = re.match(r'^([\w-]+):\s*(.*?)\s*(?:#.*)?$', line)
            if kv:
                meta[kv.group(1)] = kv.group(2)
    fields = {}
    for name, value in re.findall(r'\*\*([^*:]+):\*\*[ \t]*(.*?)(?=\n\*\*|\n#|\Z)', body, re.S):
        fields[name.strip().lower()] = ' '.join(value.split())
    return meta, fields


def number(meta, key):
    try:
        return float(meta[key])
    except (KeyError, ValueError):
        return None


def check(text):
    """Return a list of (ok, message). ok is True, False, or None for a note."""
    meta, fields = parse(text)
    out = []

    def add(ok, msg):
        out.append((ok, msg))

    for key in ('hook', 'length', 'turn_at', 'events_after_hook'):
        if not meta.get(key):
            add(False, f'front matter has no "{key}"')
    for key in ('truth', 'we see', 'turn', 'reaction'):
        if not fields.get(key):
            add(False, f'no **{key.capitalize()}:** line')

    shape = (meta.get('shape') or 'gag').lower()
    if shape not in LENGTH:
        add(False, f'shape is "{shape}"; expected gag, clock or story')
        shape = 'gag'

    hook = meta.get('hook', '')
    n = len(words(hook))
    if hook:
        add(n <= HOOK_MAX_WORDS, f'hook is {n} word{"s" if n != 1 else ""} (at most {HOOK_MAX_WORDS}): "{hook}"')

    truth = fields.get('truth', '')
    if truth:
        t = len(words(truth))
        add(t <= TRUTH_MAX_WORDS, f'truth is {t} words (at most {TRUTH_MAX_WORDS})')

    length, turn_at = number(meta, 'length'), number(meta, 'turn_at')
    if length is not None:
        lo, hi = LENGTH[shape]
        add(lo <= length <= hi, f'length {length:g} s for a {shape} reel ({lo}–{hi} s)')
    if turn_at is not None:
        if shape == 'gag':
            add(turn_at <= TURN_BY, f'turn lands at {turn_at:g} s (by {TURN_BY:g} s)')
        else:
            add(None, f'turn lands at {turn_at:g} s; a {shape} reel is not held to {TURN_BY:g} s')
        if hook:
            need = hook_time(n)
            add(need <= turn_at, f'hook needs {need:g} s on screen, before the turn at {turn_at:g} s')
    if length is not None and turn_at is not None:
        hold = round(length - turn_at, 2)
        add(hold >= REACTION_MIN, f'{hold:g} s left after the turn for the reaction (at least {REACTION_MIN:g} s)')

    events = number(meta, 'events_after_hook')
    if events is not None:
        add(events == 1, f'{events:g} new event{"s" if events != 1 else ""} after the hook (exactly 1)')

    turn = fields.get('turn', '')
    if turn:
        spoken = [p for p in SPEECH if re.search(p, turn, re.I)]
        add(not spoken, 'the turn is written as a visible event, not a spoken line'
            if not spoken else 'the turn reads as a spoken line (a quote or "says"); a line is not an event')

    caption = fields.get('caption', '')
    if caption:
        hits = [m.group(0) for p in BAIT for m in [re.search(p, caption, re.I)] if m]
        add(not hits, 'the caption asks for nothing' if not hits
            else f'the caption asks for engagement ("{hits[0]}"); platforms show such reels to fewer people')

    if not fields.get('why it had to be so'):
        add(None, 'no "Why it had to be so" line: if you cannot write it, the turn is random')
    add(None, 'not checked here: whether the turn is a surprise (run the cold read)')
    return out


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    failed = False
    for path in argv:
        try:
            with open(path, encoding='utf-8') as f:
                results = check(f.read())
        except OSError as err:
            print(f'{path}: {err}', file=sys.stderr)
            return 2
        print(path)
        for ok, msg in results:
            print(f'  {"ok  " if ok else "note" if ok is None else "FAIL"} {msg}')
            failed = failed or ok is False
    print('one or more checks FAIL' if failed else 'all counted checks pass')
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
