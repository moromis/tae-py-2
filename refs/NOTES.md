# Architecture

## Primary components
1. Parser
2. Editor
3. Runner

## Basic ingredients
Objects
  - Rooms
  - Others, i.e. a candelabra, a jewel, a monster's corpse
Commands

## Parsing input
- assume that the first word is a command
- split by spaces
- remove commas?
- assume "I don't know what you're talking about"
- how to handle synonyms?
- how to map efficiently: probably, simple list of basic commands
  - allow for extensions? add commands etc.
  - how does inform handle this? or ZIL?
- format: PRSA, [PRSO] (optional), [PRSI] (optional)
  - action, [object] (optional), [indirect object]
- handle PRSI first
- PRSO next
- verb default as last resort
- take verb (first word or multiple words -- how to tell how many to take?) and rewrite if synonym to base verb. All of this should be enum based.
- handle "and" as multi function, run in series?
- allow for unlimited numbers of verbs in check for PRSO or PRSI (if they should be handled in the same way, of course)

## Interupt system
- queue of tick-based functions
- actions can cause 0, 1, or more ticks
  - examples of each would be a system command like `VERBOSE`, `EAT SANDWICH`, and `WAIT` (which might be 3 ticks or something like that)
- global, allow for adding and removing things from the queue, probably by ID for removal
- after each tick, check top of queue and see if that action wants to run. If so run it. Keep checking till the next peek reveals an action that doesn't need to run yet

## Game endings
- if the game ended poorly, the `JIGS-UP` routine runs and produces a message followed by `*** You have died. ***` and finally options to restore or restart -- unless the player has an item that can revive them -- check for that first.

## Go command
- arbitrary direction designation
  - not just north south east west, but also up, down, sideways, etc.
- example of conditional movement in ZIL room definition: `(WEST TO STRANGE-PASSAGE IF CYCLOPS-FLED ELSE "The wooden door is nailed shut.")` - relies on globals. Thus, must have globals definition. This could be stored in a local file or in a DB. Probably this should be a layer - call it the data layer, and that way we could write to a JSON file, a local DB, or even a cloud DB if we wanted.
- `(DOWN PER TRAP-DOOR-EXIT)` function exit, based on `PER`, 
- non-exit: e.g. `(NW SORRY "The soldier at Uncle Otto's front door informs you that only Emperor Bonaparte is allowed through.")`, can't exit but doesn't do the default. Could just recognize this based off the argument being a string and not a function etc. -- i.e. not a runnable
- door exit: `(SOUTH TO GARAGE IF GARAGE-DOOR IS OPEN ELSE "You ought to use the garage door opener.")`, note the `IS OPEN`

## Verbs
- base dictionary and handlers (must be integrated with parser?)
- matching:
  - [trie](https://en.wikipedia.org/wiki/Trie), match at earliest leaf?
- verbs could/should have idea of handling here vs there? for instance look at vs look toward

## Fun stuff
- handle: ,W?XYZZY ,W?PLUGH ,W?PLOVER ,W?YOHO ,W?ULYSSES ,W?ODYSSEUS>>

## Rooms
- has flags for things such as is land/air/water, is it lit, does something occur in this room on a timer, etc. [here, 2.3](Learning_ZIL_Steven_Eric_Meretzky_1995.pdf)

## Runner
I'd like to be able to present photos for rooms and/or situations (such as `inspect gem`). Would probably need to plan this from the beginning so that those pictures can be displayed at the appropriate time and various triggers can be tied into easily

## Objects (structure/schema)
- articles
- pronouns
- characteristics
- responses to commands (i.e. examine, take)
- different responses after a condition has been met, or the player has an object, etc.
- all objects are global, they just have a LOC flag
  - is this efficient in a very large game? perhaps it would be wise to modernize this and have the objects belong to the given object where they reside -- but maybe this also depends on the language being used. in ZIL it would all be compiled to one file like Assembly so that's why all globals could be read from literally anywhere

## Interpreters
- write to ZIL, read ZIL (?) probably a lot of work, see [Stretch Goals](#stretch)
- would be nice to just easily be able to swap out input/output layers, so those should be abstracted

## Things that are important to me
- all internal code should be tested from the ground up
- users should be able to write tests or at least test routines that run through the game and make sure functionality is correct

## Stretch
- images
- allow for ZIL import?
- allow for Inform import?
- Quick travel
- Automatic game versioning
- Mobile?
- Allow for AI to parse input as an option (y/n to accept suggestion)

## Parchment
- https://iplayif.com/

## Input
Something like [this](https://github.com/CITGuru/PyInquirer/)

## Various
- UNDO command