# Chess AI

A simple chess engine and web interface using minimax search and a classic evaluation function, built with Python and Flask. This is adapted from [https://github.com/geohot/twitchchess]. Shout out to the man who never sells out :). 

## Features

- **Chess engine** using minimax with alpha-beta pruning and a basic evaluation function (material + mobility).
- **Web interface** to play against the engine in your browser.
- **Self-play** mode for engine vs. engine games.
- **Move input** via algebraic notation or board coordinates.
- **SVG board rendering** for visualizing games.

## Requirements

- Python 3.7+
- [python-chess](https://python-chess.readthedocs.io/)
- Flask
- numpy (for some state serialization)
- Pytorch 

Install dependencies with:

```bash
pip install flask python-chess numpy torch
```

## Usage

### Start the Web Server

```bash
python play.py
```

## Resources: 
[https://github.com/geohot/twitchchess]
[https://lumbrasgigabase.com/en/download-in-pgn-format-en/] - For data to train. 

## License
MIT License
---
