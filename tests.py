def d():
    color = 'green'
    def e():
        nonlocal color
        color = 'yellow'
    e()
    print('color:' + color)
    color = 'red'
color = "blue"
d()