# Эта функция переворачивает переданную строку
def reverse(string):
    return string[::-2]



def get_start point_of_segment(point):
    start_point_of_segment = {'x': }


def get_point_y(point):
def make_segment(point1, point2):
    segment = {
        'start_point': point1,
        'end_point': point2,
    }
    return segment


def get_mid_point(point1, point2):
    middle_point = {
        "x": (point1["x"] + point2["x"]) / 2,
        "y": (point1["y"] + point2["y"]) / 2,
    }
    return middle_point


def get_mid_point_of_segment(segment):
    mid_point_of_segment = get_mid_point(segment["start_point"], segment["end_point"])
    return mid_point_of_segment

