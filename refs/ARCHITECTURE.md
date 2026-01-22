# TAE Architecture

## Intermediate language
- ZIL? or custom
  - custom. ZIL is bad.
- human-readable
- handle `it`, `the`, etc.

## Compiler

## Parser
- multithreaded verb processing?
- first thing to do with input is to sanitize and transform it
- after that, identify word functions (grammatical, that is)
- run matched functions based on verb and direct/indirect object, giving preference first to indirect object, then direct, and handling with the verb default as the base case
- split by `and`, run sequentially

## Runner

## Editor