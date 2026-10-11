# Child-Quine
Pure playful Python nested quine replication project.

## Introduction
This is an **abstract, for-fun distributed quine experiment**.

All child scripts have **no independent control authority**.
Before replicating a new generation, every child must query permission from `main.py`.

The master program holds the global token counter.
The entire nesting chain stops automatically once the tokens run out.

## How It Works
1. `main.py` acts as the only master controller.
2. Every `child` process requests a token before replication.
3. If token > 0: replicate itself and run the new file.
4. If token = 0: stop all nesting immediately.

## File Structure
- `main.py` — Master token control center
- `child_*.py` — Auto-generated self-replicating quine scripts

## Run
```bash
python main.py
