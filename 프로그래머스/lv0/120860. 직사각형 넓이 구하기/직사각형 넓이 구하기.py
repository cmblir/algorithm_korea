def solution(dots):
    x_coords = [i[0] for i in dots]
    y_coords = [i[1] for i in dots]
    width = max(x_coords) - min(x_coords)
    height = max(y_coords) - min(y_coords)
    area = width * height
    return area