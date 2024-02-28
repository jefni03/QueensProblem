import tkinter as tk

class ChessBoardGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Queens Problem")

        self.board_size = 8
        self.create_chess_board()
        self.create_button()

    def create_chess_board(self):
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        self.square_size = 50
        self.chessboard = [[0] * self.board_size for _ in range(self.board_size)]

        for row in range(self.board_size):
            for col in range(self.board_size):
                x0 = col * self.square_size
                y0 = row * self.square_size
                x1 = x0 + self.square_size
                y1 = y0 + self.square_size

                color = "white" if (row + col) % 2 == 0 else "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

    def create_button(self):
        button = tk.Button(self.master, text="Start", command=self.button_click, height=3, width=10)
        button.place(x=410, y=100)

    def button_click(self):
        self.solveNQ()
        self.update_chessboard()

    def update_chessboard(self):
        self.canvas.delete("all")  # Clear previous chessboard
        for row in range(self.board_size):
            for col in range(self.board_size):
                x0 = col * self.square_size
                y0 = row * self.square_size
                x1 = x0 + self.square_size
                y1 = y0 + self.square_size

                color = "white" if (row + col) % 2 == 0 else "black"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="black")

                if self.chessboard[row][col] == 1:
                    self.canvas.create_text(x0 + self.square_size / 2, y0 + self.square_size / 2,
                                            text="♛", font=("Helvetica", 16), fill="red")

    def solveNQ(self):
        global N
        N = self.board_size

        def isSafe(row, col):
            for i in range(col):
                if self.chessboard[row][i] == 1:
                    return False

            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if self.chessboard[i][j] == 1:
                    return False

            for i, j in zip(range(row, N, 1), range(col, -1, -1)):
                if self.chessboard[i][j] == 1:
                    return False

            return True

        def solveNQUtil(col):
            if col >= N:
                return True

            for i in range(N):
                if isSafe(i, col):
                    self.chessboard[i][col] = 1

                    if solveNQUtil(col + 1):
                        return True

                    self.chessboard[i][col] = 0

            return False

        solveNQUtil(0)

if __name__ == "__main__":
    root = tk.Tk()
    chess_board = ChessBoardGUI(root)
    root.mainloop()
