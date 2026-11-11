"""Tests for scripts/pitch_check.py.

    python3 -m unittest discover -s tests -v      (from the repo root)
"""
import os
import subprocess
import sys
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPT = os.path.join(ROOT, 'scripts', 'pitch_check.py')
sys.path.insert(0, os.path.join(ROOT, 'scripts'))

import pitch_check  # noqa: E402

GOOD = """---
hook: The library at 9:00
shape: gag
length: 10
turn_at: 6.0
events_after_hook: 1
---

**Truth:** A coat holds a library seat for an absent owner.
**We see:** A student walks along a row of desks, each chair holding a coat.
**Turn:** The frame widens: the whole hall is coats, and nobody else.
**Reaction:** The student stands still, looking at the camera.
**Why it had to be so:** Everyone reserves, nobody sits.
**Caption:** Fully booked.
"""


def failures(text):
    return [msg for ok, msg in pitch_check.check(text) if ok is False]


def swap(old, new):
    assert old in GOOD, old
    return GOOD.replace(old, new)


class Counting(unittest.TestCase):
    def test_words_ignore_bare_punctuation(self):
        self.assertEqual(len(pitch_check.words('POV: your flatmate — again')), 4)

    def test_hook_time(self):
        self.assertEqual(pitch_check.hook_time(4), 1.7)
        self.assertEqual(pitch_check.hook_time(5), 2.0)


class Parsing(unittest.TestCase):
    def test_front_matter_and_fields(self):
        meta, fields = pitch_check.parse(GOOD)
        self.assertEqual(meta['hook'], 'The library at 9:00')
        self.assertEqual(meta['turn_at'], '6.0')
        self.assertTrue(fields['turn'].startswith('The frame widens'))
        self.assertEqual(fields['caption'], 'Fully booked.')

    def test_comments_after_values_are_dropped(self):
        meta, _ = pitch_check.parse('---\nlength: 10   # seconds\n---\n')
        self.assertEqual(meta['length'], '10')

    def test_a_field_may_run_over_two_lines(self):
        _, fields = pitch_check.parse('**We see:** one\n  two\n**Turn:** three\n')
        self.assertEqual(fields['we see'], 'one two')


class Checks(unittest.TestCase):
    def test_good_pitch_passes(self):
        self.assertEqual(failures(GOOD), [])

    def test_long_hook(self):
        out = failures(swap('hook: The library at 9:00', 'hook: When the library is full at nine'))
        self.assertTrue(any('hook is 7 words' in m for m in out), out)

    def test_long_truth(self):
        out = failures(swap('for an absent owner', 'for an owner who left two hours ago'))
        self.assertTrue(any('truth is' in m for m in out), out)

    def test_late_turn(self):
        out = failures(swap('turn_at: 6.0', 'turn_at: 8'))
        self.assertTrue(any('turn lands at 8 s' in m for m in out), out)

    def test_a_clock_reel_may_turn_late_and_run_long(self):
        text = swap('shape: gag', 'shape: clock').replace('turn_at: 6.0', 'turn_at: 18').replace('length: 10', 'length: 20')
        self.assertEqual(failures(text), [])

    def test_gag_reel_too_long(self):
        out = failures(swap('length: 10', 'length: 15'))
        self.assertTrue(any('length 15 s' in m for m in out), out)

    def test_no_room_for_the_reaction(self):
        out = failures(swap('turn_at: 6.0', 'turn_at: 19.5').replace('length: 10', 'length: 20').replace('gag', 'clock'))
        self.assertEqual(len(out), 1, out)
        self.assertIn('0.5 s left after the turn', out[0])

    def test_hook_still_on_screen_at_the_turn(self):
        out = failures(swap('turn_at: 6.0', 'turn_at: 1.0'))
        self.assertTrue(any('hook needs 1.7 s' in m for m in out), out)

    def test_two_events(self):
        out = failures(swap('events_after_hook: 1', 'events_after_hook: 2'))
        self.assertTrue(any('2 new events' in m for m in out), out)

    def test_spoken_turn(self):
        out = failures(swap('The frame widens: the whole hall is coats, and nobody else.', 'She says "this one is free".'))
        self.assertTrue(any('spoken line' in m for m in out), out)

    def test_bait_caption(self):
        for caption in ('Tag the friend who does this.', 'Send this to your flatmate', 'Comment if this is you'):
            out = failures(swap('Fully booked.', caption))
            self.assertTrue(any('asks for engagement' in m for m in out), caption)

    def test_bait_words_inside_other_words_are_fine(self):
        self.assertEqual(failures(swap('Fully booked.', 'Vintage, the price tags still on.')), [])

    def test_missing_parts_are_named(self):
        out = failures('**Truth:** Short.\n')
        for part in ('"hook"', '"length"', '"turn_at"', '"events_after_hook"', '**We see:**', '**Turn:**', '**Reaction:**'):
            self.assertTrue(any(part in m for m in out), part)

    def test_unknown_shape(self):
        out = failures(swap('shape: gag', 'shape: epic'))
        self.assertTrue(any('shape is "epic"' in m for m in out), out)

    def test_the_surprise_is_never_claimed(self):
        notes = [msg for ok, msg in pitch_check.check(GOOD) if ok is None]
        self.assertTrue(any('cold read' in m for m in notes))


class CommandLine(unittest.TestCase):
    def run_on(self, *names):
        paths = [os.path.join(ROOT, n) for n in names]
        return subprocess.run([sys.executable, SCRIPT, *paths], capture_output=True, text=True)

    def test_examples(self):
        good = self.run_on('examples/coats.pitch.md')
        self.assertEqual(good.returncode, 0, good.stdout)
        self.assertIn('all counted checks pass', good.stdout)
        bad = self.run_on('examples/overloaded.pitch.md')
        self.assertEqual(bad.returncode, 1)
        self.assertEqual(bad.stdout.count('FAIL '), 7, bad.stdout)

    def test_the_template_itself_passes(self):
        self.assertEqual(self.run_on('pitch-template.md').returncode, 0)

    def test_one_bad_file_fails_the_run(self):
        self.assertEqual(self.run_on('examples/coats.pitch.md', 'examples/overloaded.pitch.md').returncode, 1)

    def test_unreadable_file(self):
        out = self.run_on('examples/nope.md')
        self.assertEqual(out.returncode, 2)

    def test_no_arguments(self):
        out = subprocess.run([sys.executable, SCRIPT], capture_output=True, text=True)
        self.assertEqual(out.returncode, 2)
        self.assertIn('pitch_check.py PITCH.md', out.stdout)


if __name__ == '__main__':
    unittest.main()
