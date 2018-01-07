import turtle as t


def init_turtle():
    """Initializes turtle facing upwards and drawing fast"""
    t.home()
    t.clear()
    t.speed(0)
    t.tracer(2)
    t.left(90)


def draw_string(string, angle, stepsize):
    """ Draws a string like 'FF+-[FF]--F'

    Parameters
    ----------
    string: str
        With 'F' for forward
        '+' for left
        '-' for right
        and '[', ']' for storing and loading from stack
    angle: float
        Angle in degree
    stepsize: int
        Stepsize of turtle

    """
    stack = []
    for char in string:
        if char == 'F' or char == 'G':
            t.forward(stepsize)
        elif char == '+':
            t.left(angle)
        elif char == '-':
            t.right(angle)
        elif char == '[':
            # Adds Position and Heading to stack
            pos, heading = t.pos(), t.heading()
            stack.append((pos, heading))
        elif char == ']':
            # Loads Position and Heading from stack
            pos, heading = stack.pop()
            t.pu()
            t.setpos(pos)
            t.setheading(heading)
            t.pd()


def apply_rules(start, rules, n):
    """ Applies recursive rules

    Parameters
    ----------
    start: str
        Starting position, e.g. 'F'
    rules: list of str
        Rules to apply notation is 'State>Replacement',
        e.g. 'F>F+F--F+F'
    n: int
        Number of iterations

    Returns
    -------
    str: Final string after `n` iterations

    """
    current = start
    for irun in range(n):
        # first replace with tmp value (Char+Int) to allow
        # "simultaneous" replacment
        for kdx, rule in enumerate(rules):
            state, _ = rule.split('>')
            current = current.replace(state, state + str(kdx))
        # replace tmp value with real replacemnt
        for kdx, rule in enumerate(rules):
            state, replacement = rule.split('>')
            current = current.replace(state + str(kdx), replacement)
    return current


def kochcurve():
    """Plots the Kochkurve"""
    init_turtle()
    n, angle, stepsize = 6, 60, 1
    koch = apply_rules('F', ['F>F+F--F+F'], 5)
    print('Kochcurve:\n' + koch)
    draw_string(koch, angle, stepsize)


def plant_c():
    """Plots plant C from Prusinkiewicz et al. 1990"""
    init_turtle()
    n, angle, stepsize = 4, 22.5, 6
    plant_c = apply_rules('F', ['F>FF-[-F+F+F]+[+F-F-F]'], n)
    print('Pland c: \n' + plant_c)
    draw_string(plant_c, angle, stepsize)


def plant_d():
    """Plots plant D from Prusinkiewicz et al. 1990"""
    init_turtle()
    n, angle, stepsize = 6, 20, 1
    plant_d = apply_rules('X', ['X>F[+X]F[-X]+X', 'F>FF'], n)
    print('Plant d: \n' + plant_d)
    draw_string(plant_d, angle, stepsize)


def sierpinski():
    """Plots the Serpinky triangle"""
    init_turtle()
    n, angle, stepsize= 6, 120, 5
    triangle = apply_rules('F-G-G', ['F>F-G+F+G-F', 'G>GG'], n)
    print('Sierpinsky Triangle: \n' + triangle)
    draw_string(triangle, angle, stepsize)


## Uncomment for drawing
#kochcurve()
#plant_c()
#plant_d()
sierpinski()

# close turtle graphics
t.exitonclick()
