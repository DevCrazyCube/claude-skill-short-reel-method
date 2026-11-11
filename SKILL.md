---
name: short-reel-method
description: Find and test the idea for a short comedy reel (8–12 s, Instagram Reels, TikTok, Shorts) before anything is drawn, voiced or animated. Covers the truth, the one-line pitch, an eight-question pitch test, a cold read by a fresh agent, four stills, and the rules for animating the turn and writing the caption. Use before writing any reel pitch, script or storyboard, and when a finished reel was called "random" or "has no punchline".
---

# Short reel method

This method exists because of a failure. A set of storyboards and a finished, voiced animatic passed every
technical check (pacing, loudness, lip-sync, a design review) and were still rejected by the account's owner as
random, with no punchline. Two lessons came out of it:

- Checks and design reviews measure clarity and finish. Nothing measured whether the idea was funny.
- A yes to an idea described in words did not predict the verdict on the pictures. People judge pictures.

So an idea is tested in one line, by someone who did not write it, and judged on four stills before anything is
voiced or animated.

## Words used here

- **Truth:** a moment the audience has lived, or watched a friend live. The raw material.
- **Hook:** the text on screen at 0.0 s that names the situation, five words or fewer, with a character already moving.
- **Turn:** the one moment where what the viewer expects breaks. It is the punchline. One per reel.
- **Reaction:** the held picture after the turn.
- **Game:** the one thing a character does every time.
- **Gag reel:** 8–12 s, one turn. The default.
- **Story reel:** 20–30 s with dialogue, a want, a reversal and a reveal. Only on request.

## The order of work

Each step has a gate. Do not start a step before the one above it has passed.

| Step | What you make | Gate |
|---|---|---|
| 1. Truth | One sentence, ten words or fewer | It is on the project's truths list, in the account's own comments or messages, or the owner has seen it happen. Never from the stay-away list. |
| 2. Pitch | One line: the hook, what we see, the turn | The pitch test, then the cold read. Then the owner picks which pitches get stills. |
| 3. Four stills | Setup, the moment before the turn, the turn, the reaction | The owner's OK on the pictures. This is the real test of the idea. |
| 4. Sound | The voice takes or the audio track, final | Locked before any animation. Foley and room tone follow the picture later. |
| 5. Animatic | Rough frames on the locked sound | Arms counted on every still; then the owner's look. |
| 6. Finish | The reel | A design review by a separate critic, then the technical checks. |

Send the owner three to six pitches that passed, not one. A pick is permission to draw that pitch's four stills
and nothing more.

Keep the truths in a file per project: copy `truths-template.md` and fill it in. Write each pitch in the format
of `pitch-template.md`; `scripts/pitch_check.py` checks the parts of the pitch test that can be counted.

## What a gag reel is

One recognisable truth with one turn you can see. It is not a short story.

- **One unusual thing.** A sketch takes one unusual thing and pushes it further. A second unusual thing starts a
  second joke and weakens the first.
- **Surprising and true.** The viewer does not see the turn coming, and within a second sees why it had to be so.
  A turn nobody can explain is random. A turn everybody saw coming is an illustration of the hook, not a joke.
- **The turn is an event on screen.** A character does something, an object appears or goes, or the frame widens
  to show what the close shot hid. A spoken line is not an event. A phone screen the viewer has to read is a line.
- **Nothing invented after the hook.** The turn is something the viewer has done, has watched someone do, or would
  do; exaggerating it is fine. A turn that needs a new fact the hook never set up is invented.
- **It ends on the reaction.** Hold it 1.0–1.5 s, nearly still, then cut or loop. No line after it that comments on it.
- **It works with the sound off.** Dialogue is optional. When there is dialogue it is full sentences in character.
- **Early, not rushed.** Someone who has never seen the account knows the situation by 2 s, and the turn lands by
  7 s. Short means fewer things, each given its time: at most two beats before the turn, the hook text up for
  0.3 s a word plus 0.5 s, the reaction held. If it only fits by speeding up, cut a beat.
- **Longer than 12 s only when** a clock or countdown is on screen from frame 1 and the viewer can see its end
  coming, or a story reel was asked for.
- **The product is never in the sketch.** At most it is in the caption.
- **One location, two or three characters.**

## The pitch test (you answer)

One no, and the pitch is fixed or dropped.

1. Can you tell it as "we see X, then Y" without quoting a spoken line?
2. Is the hook five words or fewer, and would a newcomer know the situation from it and the picture?
3. Is the turn a visible change, as defined above?
4. Does the turn land by 7 s, or is a clock on screen from frame 1?
5. Is the turn free of any fact the hook did not set up?
6. If the moment is on the worn-out list: can you write, in one sentence, what this version shows that the earlier
   hundred did not? If not, drop it.
7. Count the new events after the hook. Is it one? (The same beat repeated and growing counts as one. "And then"
   something else is a second.)
8. Put another character in the lead. Does the joke break? If it works unchanged with anyone, the cast is
   decoration: rewrite so a character's game causes the turn, or say plainly that it is a one-character reel.

Questions 2, 4 and 7 can be counted, and the script counts them:

```bash
python3 scripts/pitch_check.py pitches/*.md
```

It also checks the reaction's hold, the length for the reel's shape, that the turn is not written as a quoted
line, and that the caption asks for nothing. It cannot tell whether the turn is a surprise. That is the cold read.

## The cold read (someone else answers)

You wrote the pitch, so you cannot judge whether its turn is a surprise. Start a fresh agent that has seen none of
this. Use two messages, so it cannot see the turn early.

1. Give it only the hook and what we see before the turn. Ask: "What is the situation, in one sentence? What
   happens next? Give your three most likely guesses."
2. Then give it the turn. Ask: "Why did that happen, in one sentence? Would someone in the audience send this to
   someone, and to whom?"

It passes when:

- the situation it names is your truth;
- none of its three guesses is your turn (if one is, the picture only repeats the text);
- it gives the reason without help, and it is your reason (if not, the turn is random);
- it says yes to sending and names a kind of person, not "a friend". "Maybe", or "a like, not a send", is not a pass.

**When the turn was guessed, keep the truth and drop the turn.** The three guesses are now the list of what
everyone expects. Write a turn that comes after them, and read it cold again with a new agent, never the one that
has seen it. Do not loosen the rule to save a pitch you like.

Read the guesses for more than pass or fail: a reader sometimes guesses a better turn than the one you wrote.

Put the agent's answers under the pitch when it goes to the owner. An agent is a weak stand-in for the audience:
this catches the predictable and the unexplainable, and nothing more. The owner's eye on the four stills decides.

## Shapes

- **The clock.** Frame 1 shows a question and a running countdown, so the viewer knows the stake and when it ends.
  No words. A new distraction about every 2 s. It ends where it began and loops. Use it when a truth is about
  time: starting on the hour, the last minute before a deadline.
- **The reveal.** A character wants something, reverses, and the reveal contradicts a fact shown earlier. The
  reveal is a picture, not a line.
- **Lip-sync to an audio (7–9 s).** The hook names the moment, a character mouths a known audio, the last word
  lands on a pose change. Use only audio you have the right to use.
- **Two-character contrast (10–12 s).** The hook names the situation, one character's reaction, the other's
  opposite, a look from a third.
- **Fact × situation (10–12 s).** The hook names what is going on inside ("your brain after the lecture"), the
  characters act it out, the fact goes in the caption.

Pick one shape and make several in it before judging the shape. One reel says little.

## The cast: one game each

A joke starts where what a character wants meets what stops it. Give each character one game, in one line, and
keep to it: "more invested in your plans than you are", "builds a disaster out of one small fact", "bargains for
the minimum", "says the uncomfortable truth flatly". Write the games down in the project and get them confirmed
before building a reel around one.

## The four stills (step 3)

Setup, the moment before the turn, the turn, the reaction. The poses at finish quality; the set may be plain.

Before they go to the owner, look at them with the characters filled black and the text removed. The turn should
still read as a change from still 2 to still 3. If stills 2 and 3 look alike, the turn is a line, not an event; go
back to the pitch. Also check: no two characters in the same pose, eyes pointing at what matters, two arms per
character at their own length.

## Animating the turn

- **A take is four poses:** the start, an anticipation the other way (0.17–0.25 s), the accent reached in 0.12 s
  or less, a settle of about 0.3 s. Spend the drawing on the turn's pose. The rest is held poses with breath and
  eye darts.
- **One character moves broadly at a time.** The eyes go first, the body follows.
- **A rhythm per character:** one in quick pops, one slow and soft, one still with only the eyes.
- **Arms:** the rig's own arm only, stretched 0.8–1.15 of its drawn length. To reach further the body leans, hops
  or steps, or cut to an insert. A prop is picked up by swapping the hand drawing on one frame. Never draw a
  second arm for a reach. Limbs never pass through props.
- **Count the arms** on stills of the animatic and of the final (one still a second or less, plus one at every
  grab): two per character, none thin. A third arm shows up in motion, not in storyboards.
- **One idea per shot.** A 10 s reel is three to six shots. A single-shot reel (the clock) is an exception; say so
  instead of adding cuts.
- **Camera moves leave and land at rest.** No fast zoom-ins; at most three punch-ins.
- **Keep words and key action out of the top 12 % and the bottom 20 %** of a vertical frame; the app's own
  interface covers them.
- **Voices:** never pitch-shift or time-stretch a voice. One fresh take per line, never one take repeated.
- **No repeated action loops inside the reel.** A reel that ends where it began and loops as a whole is fine.

## Caption and posting

- **No "tag a friend", "send this to" or "comment if".** Platforms treat these as engagement bait and show the
  reel to fewer people. The reel should make someone want to send it without being asked.
- Post original files, with no watermark from another app.
- **Post a truth in the week it is true.** Write that week next to the pitch.
- **Do not draw another company's screen, logo or colours.** A real app's name may be said as a word.
- **Music:** only audio you have the right to use. Do not download a commercial track to cut to it.
- **After posting, report rates, not counts,** in this order: sends per reach, skip rate, average watch time
  against the length, likes per reach, the share of non-followers.

## What is established and what is a guess

Say this when you report, so nobody takes a guess for a law.

- **Widely taught and sourced** (sketch-writing and animation teaching, the platforms' public statements): one
  unusual thing per sketch, one game per character, the four-pose take, audio locked before animation,
  engagement bait reducing reach, sends and watch time as the main signals.
- **This method's own inference, not measured:** the 2 s / 7 s / 12 s numbers, the hook's reading time, and
  whether an agent's cold read predicts a person's laugh. In its first trial the cold read stopped four of four
  pitches, each time because the turn was among the reader's guesses; all four readers named the situation
  correctly. So recognition was not the problem: a truth with the expected ending is an illustrated observation.
- **Unknown:** the best length for a given account. Change the numbers when the account's own figures say otherwise.
