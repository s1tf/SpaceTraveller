import text
import pyxel

day = 1
health = 100
money = 100
fuel = 100


class App:
    def __init__(self):
        pyxel.init(320, 240)
        pyxel.mouse(True)
        self.x = 0
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        pyxel.text(x=1, y=1, s='Day:', col=pyxel.COLOR_GRAY)
        pyxel.text(x=20, y=1, s=str(day), col=pyxel.COLOR_RED)
        x_offset = 180
        pyxel.text(x=1+x_offset, y=1, s='Health:', col=pyxel.COLOR_GRAY)
        pyxel.text(x=30+x_offset, y=1, s=str(health), col=pyxel.COLOR_RED)
        pyxel.text(x=55+x_offset, y=1, s='Money:', col=pyxel.COLOR_GRAY)
        pyxel.text(x=80+x_offset, y=1, s=str(money), col=pyxel.COLOR_RED)
        pyxel.text(x=105+x_offset, y=1, s='Fuel:', col=pyxel.COLOR_GRAY)
        pyxel.text(x=126+x_offset, y=1, s=str(fuel), col=pyxel.COLOR_RED)
        pyxel.line(x1=0, y1=8, x2=pyxel.width, y2=8, col=pyxel.COLOR_GRAY)
        # text.draw(text=f'Здоровье: {health}', x=1, y=0, color=pyxel.COLOR_RED)


App()
