import tkinter as tk

class MatrixEditor:
    def __init__(self, root, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)]

        self.root = root
        self.root.title("Matrix Editor")

        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.canvas = tk.Canvas(root, width=cols*30, height=rows*30)
        self.canvas.pack()

        self.create_buttons()
        self.create_grid()

        self.canvas.bind("<Button-1>", self.on_click)
        self.current_value = 0

    def create_buttons(self):
        tk.Button(self.buttons_frame, text="0", command=lambda: self.set_value(0)).pack(side=tk.LEFT)
        tk.Button(self.buttons_frame, text="1", command=lambda: self.set_value(1)).pack(side=tk.LEFT)
        tk.Button(self.buttons_frame, text="2", command=lambda: self.set_value(2)).pack(side=tk.LEFT)
        tk.Button(self.buttons_frame, text="Afficher Matrice", command=self.display_matrix).pack(side=tk.LEFT)

    def create_grid(self):
        for i in range(0, self.rows * 30, 30):
            self.canvas.create_line(0, i, self.cols * 30, i, fill="gray", dash=(2, 2))

        for j in range(0, self.cols * 30, 30):
            self.canvas.create_line(j, 0, j, self.rows * 30, fill="gray", dash=(2, 2))

    def set_value(self, value):
        self.current_value = value

    def on_click(self, event):
        col = event.x // 30
        row = event.y // 30
        self.matrix[row][col] = self.current_value
        self.draw_matrix()

    def draw_matrix(self):
        self.canvas.delete("all")
        self.create_grid()

        for i in range(self.rows):
            for j in range(self.cols):
                value = self.matrix[i][j]
                color = ["#F0F0F2", "#e0cda9", "#000000"][value]
                self.canvas.create_rectangle(j * 30, i * 30, (j + 1) * 30, (i + 1) * 30, fill=color)

    def display_matrix(self):
        print("Matrice:")
        for row in self.matrix:
            print(row)

if __name__ == "__main__":
    root = tk.Tk()
    editor = MatrixEditor(root, rows=5, cols=5)
    root.mainloop()