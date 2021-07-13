ships = {}


def count_ones(field):
    # '1' and only '0' (or edge) in all 8 positions around
    count = 0
    for y, row in enumerate(field):
        for x, item in enumerate(row):
            if item == 1 and neighbors_are_0_or_edge(field, [(y, x)]):
                count += 1
    return count


def count_hor_ships(field, size):
    """ size > 1 (for one-ships we still will use count_ones()) """
    # '1' followed by size-1 '1' to the right and then a '0'
    count: int = 0
    for y, row in enumerate(field):
        for x, item in enumerate(row[:-size]):
            if item == 1:
                # breakpoint()
                check_positions = [(y, xx) for xx in range(x, x + size)]
                check_values = [field[y][xx] for xx in range(x, x + size)]
                if 0 not in check_values \
                        and field[y][x + size] == 0 \
                        and neighbors_are_0_or_edge(field, check_positions):
                    count += 1
    return count


def count_vert_ships(field, size):
    """ size > 1 (for one-ships we still will use count_ones()) """
    # '1' followed by size-1 '1' below and then a '0'
    count: int = 0
    for y, row in enumerate(field[:-size]):
        for x, item in enumerate(row):
            if item == 1:
                check_positions = [(yy, x) for yy in range(y, y + size)]
                check_values = [field[yy][x] for yy in range(y, y + size)]
                if 0 not in check_values \
                        and field[y + size][x] == 0 \
                        and neighbors_are_0_or_edge(field, check_positions):
                    count += 1
    return count


def get_orientation(poslist):
    """
    determine the orientation by checking the first two items
    they have either identical x- or y-values
    returns "hor" or "vert"
    """
    if len(poslist) < 2:
        return 'hor'  # in this case it doesn't matter 
    if poslist[0][0] != poslist[1][0]:
        return 'vert'
    else:
        return 'hor'


def neighbors_are_0_or_edge(field, poslist):
    orientation = get_orientation(poslist)
    # print(f"{poslist =};{orientation =}")
    if orientation == 'hor':
        # breakpoint()
        # check 3 values on the left, 3 values on the right, above/below for all
        for index, pos in enumerate(poslist):
            # if len(poslist) >1:
            # print(f"{index=} {pos=}")
            if index == 0 and pos[1] > 0:  # we only need to check on the left side if we are not at the edge anyway
                for y in range(max(pos[0] - 1, 0), min(pos[0] + 1, len(field) - 1) + 1):
                    x = pos[1] - 1
                    print("hor left", y, x)
                    if field[y][x] != 0:
                        # print("XX")
                        return False
            if index == len(poslist) - 1 and pos[1] < len(field) - 1:
                for y in range(max(pos[0] - 1, 0), min(pos[0] + 1, len(field) - 1) + 1):
                    x = pos[1] + 1
                    print("hor right", y, x)
                    if field[y][x] != 0:
                        # print("XX")
                        return False
            x = pos[1]
            for y in (max(pos[0] - 1, 0), min(pos[0] + 1, len(field) - 1)):
                print("hor inner", y, x)
                if field[y][x] != 0 and y != pos[0]:
                    # print("XX")
                    return False
    else:
        # check 3 values above, 3 values below, right/left for all
        for index, pos in enumerate(poslist):
            # print(f"{index=} {pos=}")
            if index == 0 and pos[0] > 0:  # we only need to check on the top if we are not at the top edge anyway
                for x in range(max(pos[1] - 1, 0), min(pos[1] + 1, len(field) - 1) + 1):
                    y = max(pos[0] - 1, 0)
                    # print("vert above",y,x)
                    if field[y][x] != 0:
                        return False
            if index == len(poslist) - 1 and pos[0] < len(field) - 1:
                for x in range(max(pos[1] - 1, 0), min(pos[1] + 1, len(field) - 1) + 1):
                    y = min(pos[0] + 1, len(field) - 1)
                    # print("vert below",y,x)
                    if field[y][x] != 0:
                        return False
            y = pos[0]
            for x in (max(pos[1] - 1, 0), min(pos[1] + 1, len(field) - 1)):
                # print("vert inner",y,x)
                if field[y][x] != 0 and x != pos[1]:
                    return False
    return True


def validate_battlefield(field):
    # 1 * 4, 2 * 3, 3 * 2, 4 * 1
    # Field: 10x10
    # Rules
    # - ships must be straight (no corners)
    # - they may not touch/overlap
    return count_ones(field) == 4 \
        and count_hor_ships(field,2) + count_vert_ships(field,2) == 3 \
        and count_hor_ships(field,3) + count_vert_ships(field,3) == 2 \
        and count_hor_ships(field,4) + count_vert_ships(field,4) == 1 \
