import random
import http


class demineurRessource:
    def __init__(self):
        pass

    @staticmethod
    def create_grid(size_x, size_y):
        grid = [[0 for x in range(size_x)] for x in range(size_y)]
        return grid

    @staticmethod
    def check_params(size_x, size_y, nb_bombs):
        if not size_x.isdigit() or not size_y.isdigit() or not nb_bombs.isdigit():
            raise ValueError('Arguments must be integer')
        if not int(size_x) > 0 or not int(size_y) > 0 or not int(nb_bombs) > 0:
            raise ValueError('Arguments must be superior than 0')
        if int(nb_bombs) > (int(size_x) * int(size_y)):
            raise ValueError('The number of bombs must be inferior of total grid cases')

    def put_bombs_on_grid(self, grid, nb_bombs):
        if nb_bombs == 0:
            return grid
        rand_x = random.randint(0, len(grid) - 1)
        rand_y = random.randint(0, len(grid[0]) - 1)
        if grid[rand_x][rand_y] == 0:
            grid[rand_x][rand_y] = 1
            return self.put_bombs_on_grid(grid, nb_bombs - 1)
        else:
            return self.put_bombs_on_grid(grid, nb_bombs)

    def get_game(self, size_x, size_y, nb_bombs):
        try:
            self.check_params(size_x, size_y, nb_bombs)
            grid = self.create_grid(int(size_x), int(size_y))
            grid = self.put_bombs_on_grid(grid, int(nb_bombs))
            return {"grid": grid}, http.HTTPStatus.OK
        except ValueError as e:
            return {"error": str(e)}, http.HTTPStatus.BAD_REQUEST
