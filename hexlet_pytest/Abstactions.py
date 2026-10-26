def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)

    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4

    return None

def make_rectangle(point, width, height):
    return {
        "start_point": point,
        "width": width,
        "height": height
        }


def get_start_point(rectangle):
    return rectangle["start_point"]


def get_width(rectangle):
    return rectangle["width"]


def get_height(rectangle):
    return rectangle["height"]


def contains_origin(rectangle):
    point1 = get_start_point(rectangle)
    width = get_width(rectangle)
    height = get_height(rectangle)

    x = get_x(point1) + width
    y = get_y(point1) - height
    point2 = make_decart_point(x, y)

    return get_quadrant(point1) == 2 and get_quadrant(point2) == 4

p = make_decart_point(-4, 3)
print(p)
print(get_quadrant(p))


rectangle = make_rectangle(p, 5, 4)
print(contains_origin(rectangle))