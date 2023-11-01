class Tetromino:
    def __init__(self, figura: str):
        self.figura: str = figura
        self.figura_rotada: list[list[str]] = []
        self.figuras: dict[str, list[list[str]]] = {"I": [[".", ".", "@", "."],
                                                          [".", ".", "@", "."],
                                                          [".", ".", "@", "."],
                                                          [".", ".", "@", "."]],
                                                    "O": [[".", ".", ".", "."],
                                                          [".", "@", "@", "."],
                                                          [".", "@", "@", "."],
                                                          [".", ".", ".", "."]],
                                                    "T": [[".", ".", ".", "."],
                                                          [".", "@", "@", "@"],
                                                          [".", ".", "@", "."],
                                                          [".", ".", ".", "."]],
                                                    "S": [[".", ".", ".", "."],
                                                          [".", ".", "@", "@"],
                                                          [".", "@", "@", "."],
                                                          [".", ".", ".", "."]],
                                                    "Z": [[".", ".", ".", "."],
                                                          [".", "@", "@", "."],
                                                          [".", ".", "@", "@"],
                                                          [".", ".", ".", "."]],
                                                    "J": [[".", ".", "@", "."],
                                                          [".", ".", "@", "."],
                                                          [".", "@", "@", "."],
                                                          [".", ".", ".", "."]],
                                                    "L": [[".", "@", ".", "."],
                                                          [".", "@", ".", "."],
                                                          [".", "@", "@", "."],
                                                          [".", ".", ".", "."]]
                                                    }

    def rotar_figura(self):
        figura = self.figuras[self.figura]
        for columna in range(len(figura)):
            self.figura_rotada.append([])
            for fila in range(len(figura)):
                self.figura_rotada[columna].append(figura[len(figura) - 1 - fila][columna])
        print(self.figura_rotada)


tetromino_1 = Tetromino("I")
tetromino_1.rotar_figura()
lista = []
print(lista is [])
