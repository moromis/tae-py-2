- Implement player app
- Implement response conditions
- ~~Add adjacencies to rooms~~
- Implement game preview/save/resume in editor
- ~~Fix go back in menus~~
  - ~~Fix exit with ctrl+c from main menu~~

- ~~rooms, adjacencies, and movement~~

- fix player "exit" verb exiting to main menu
- fix not being able to re-enter player after exiting

- ~~return focus to command line after selecting file~~
- ~~properly close tkinter window after selecting file~~

- (game) save files
- ~~UNDO~~
- Editing while playing?
  - Separate state and game... could write new game files, load in, and reapply state/commands? depends on changes

- multiple commands (split_by_and)

- hot reload
  - save commands, loaded game to disk, restart process with external script, reload game, run back commands
  - for editing while playing... watch files?

- default desc: f"A/An {adjective} {name}"

- item inside item
  - item inside closed item, can't be taken till item is opened