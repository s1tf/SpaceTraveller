import text
import pyxel

health = 100


class App:
    def __init__(self):
        pyxel.init(320, 240)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        text.draw(text=f'Здоровье: {health}', x=1, y=0, color=pyxel.COLOR_RED)


App()
