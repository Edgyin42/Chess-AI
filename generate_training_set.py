import os
import chess.pgn
import numpy as np
from state import State

def get_dataset(num_samples=None):
  X,Y = [], []
  gn = 0
  values = {'1/2-1/2':0, '0-1':-1, '1-0':1}
  # pgn files in the data folder
  for fn in os.listdir("data"):
    if not fn.endswith(".pgn"):
      continue
    with open(os.path.join("data", fn), encoding="utf-8", errors="ignore") as pgn:
      while 1:
        game = chess.pgn.read_game(pgn)
        if game is None:
          break
        res = game.headers['Result']
        if res not in values:
          continue
        value = values[res]
        board = game.board()
        for i, move in enumerate(game.mainline_moves()):
          board.push(move)
          ser = State(board).serialize()
          X.append(ser)
          Y.append(value)
        print("parsing game %d, got %d examples" % (gn, len(X)))
        if num_samples is not None and len(X) > num_samples:
          return X,Y
        gn += 1
  X = np.array(X)
  Y = np.array(Y)
  return X,Y

def save_dataset(X, Y, filepath):
    """Ensure directory exists and save the dataset."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    np.savez(filepath, X, Y)

if __name__ == "__main__":
    X, Y = get_dataset(1000000)
    output_path = "processed/dataset_1M.npz"
    save_dataset(X, Y, output_path)

