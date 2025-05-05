import chess
import numpy as np

class State: 
    def __init__(self, board = None):
      if board is None:
        self.board = chess.Board()
      else:
        self.board = board

    def serialize(self):
      boardState = np.zeros(64, dtype=np.uint64)
      assert(self.board.is_valid())
      for i in range(64):
        piece_at_i = self.board.piece_at(i)
        if piece_at_i is not None:
          boardState[i] = {"P": 1, "N": 2, "B": 3, "R": 4, "Q": 5, "K": 6, \
                     "p": 9, "n":10, "b":11, "r":12, "q":13, "k": 14}[piece_at_i.symbol()]
        if self.board.has_queenside_castling_rights(chess.WHITE):
          boardState[0] = 7
        if self.board.has_kingside_castling_rights(chess.WHITE):
          boardState[56] = 7
        if self.board.has_queenside_castling_rights(chess.BLACK):
          boardState[0] = 8+7
        if self.board.has_kingside_castling_rights(chess.BLACK):
          boardState[56] = 8+7
        
        if self.board.ep_square is not None:
          boardState[self.board.ep_square] = 8

      boardState = boardState.reshape((8, 8))
       
      state = np.zeros((5, 8, 8), dtype = np.uint8)

      state[0] = (boardState>>3)&1
      state[1] = (boardState>>2)&1
      state[2] = (boardState>>1)&1
      state[3] = (boardState>>0)&1

      state[4] = self.board.turn

      return state

# if __name__ == "__main__":
#  board = State()
#  print(board.serialize())
  