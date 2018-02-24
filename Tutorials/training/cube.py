cube_a = 2 ** 3
cube_b = 2 ** 3
cube_c = lambda x: x ** 3
cube_d = lambda x: x ** 3
cube_e = lambda x: cube_d
cube_f = lambda cube_d: cube_d
def cube_g(cube_a):
    def cube_h(cube_a):
        return cube_a ** 3
    return cube_h
