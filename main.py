import arcade
import random as r

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# liste des couleurs
COLORS = [arcade.color.BLUE, arcade.color.FANDANGO_PINK,
          arcade.color.FRENCH_ROSE, arcade.color.GOLDEN_POPPY,
          arcade.color.GREEN, arcade.color.LIGHT_BLUE,
          arcade.color.LIGHT_PINK, arcade.color.LIGHT_YELLOW,
          arcade.color.MEDIUM_BLUE, arcade.color.MEDIUM_RED_VIOLET]


class Balle:
    # definition des variables
    def __init__(self, x, y, change_x, change_y, color, rayon):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.rayon = rayon
        self.color = color

    def update(self):
        # permet de faire rebondir la balle
        self.x += self.change_x
        self.y += self.change_y
        if self.x + self.rayon > SCREEN_WIDTH or self.x - self.rayon < 0:
            self.change_x *= -1
        if self.y + self.rayon > SCREEN_HEIGHT or self.y - self.rayon < 0:
            self.change_y *= -1

    def draw(self):
        # permet de dessiner la balle
        arcade.draw_circle_filled(self.x, self.y, self.rayon, self.color)


class Rectangle:
    # definition des variables
    def __init__(self, x, y, change_x, change_y, width, height, color, angle):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
        self.width = width
        self.height = height
        self.color = color
        self.angle = angle

    def update(self):
        # permet de faire rebondir le rectangle
        self.x += self.change_x
        self.y += self.change_y
        if self.x + self.width / 2 > SCREEN_WIDTH or self.x - self.width / 2 < 0:
            self.change_x *= -1
        if self.y + self.height / 2 > SCREEN_HEIGHT or self.y - self.height / 2 < 0:
            self.change_y *= -1

    def draw(self):
        # permet de dessiner le rectangle
        arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, self.color, self.angle)


class MyGame(arcade.Window):
    
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, 'tp4')
        self.balle_liste = []
        self.rectangle_liste = []

    def on_mouse_press(self, x, y, button, modifiers):
        # permet de créer une balle quand on clique sur la souris gauche
        if button == arcade.MOUSE_BUTTON_LEFT:
            rayon = r.randint(10, 30)
            center_x = x
            center_y = y
            change_x = r.randint(-5, 5)
            change_y = r.randint(-5, 5)
            color = r.choice(COLORS)
            self.balle_liste.append(Balle(center_x, center_y, change_x, change_y, color, rayon))
        # permet de créer un rectangle quand on clique sur la souris droite
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            width = r.randint(10, 50)
            height = r.randint(10, 50)
            center_x = x
            center_y = y
            change_x = r.randint(-5, 5)
            change_y = r.randint(-5, 5)
            color = r.choice(COLORS)
            angle = r.randint(0, 360)
            self.rectangle_liste.append(Rectangle(center_x, center_y, change_x, change_y, width, height, color, angle))

    def on_update(self, delta_time):
        # permet de faire bouger les balles en appelant la fonction update
        for cercle in self.balle_liste:
            cercle.update()
        # permet de faire bouger les rectangles en appelant la fonction update
        for rectangle in self.rectangle_liste:
            rectangle.update()

    def on_draw(self):
        # permet de dessiner les balles et les rectangles en appelant la fonction draw
        arcade.start_render()

        for cercle in self.balle_liste:
            cercle.draw()
        for rectangle in self.rectangle_liste:
            rectangle.draw()


# permet de lancer le jeu
def main():
    MyGame()
    arcade.run()


main()
