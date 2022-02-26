def is_at_origin(moves):
    """
    Time Complexity = O(N)
    Space Complexity = O(1)
    :param moves:
    :return:
    """
    x = 0
    y = 0
    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        else:
            x -= 1
    return x == 0 and y == 0

moves = 'UDL'

print("Is back at origin", is_at_origin(moves))