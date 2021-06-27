ships = {}

def detect_ones(field):
    # '1' and only '0' (or edge) in all 8 positions around
    count = 0
    for y,row in enumerate(field):
        for x,item in enumerate(row):
            if item == 1 and neighbors_are_0_or_edge(field,[(y,x)]):
                count += 1
    return count

def detect_hor_threes(field):
    # '1' accompanied by a '1' to the right and then a '0'
    count = 0
    for y,row in enumerate(field):
        for x,item in enumerate(row[:-2]):
            if item == 1 \
                and field[y][x+1] == 1 and field[y][x+2] ==0 and field[x+3] == 0 \
                and neighbors_are_0_or_edge(field,[(y,x),(y,x+1), (y, x+2)]):
                # print(f"+ {y=}/{x=}")
                count += 1
    return count

def detect_vert_threes(field):
    # '1' accompanied by a '1' below and then a '0'
    count = 0
    for y,row in enumerate(field[:-2]):
        for x,item in enumerate(row):
            if item == 1 \
                and field[y+1][x] == 1 and field[y+2][x] == 0 and field[y+3][x] == 0\
                and neighbors_are_0_or_edge(field,[(y,x),(y+1,x), (y+2,x)]):
                # print(f"+ {y=}/{x=}")
                count += 1
    return count
    
def detect_hor_twos(field):
    # '1' accompanied by a '1' to the right and then a '0'
    count = 0
    for y,row in enumerate(field):
        for x,item in enumerate(row[:-2]):
            if item == 1 \
                and field[y][x+1] == 1 and field[y][x+2] ==0  \
                and neighbors_are_0_or_edge(field,[(y,x),(y,x+1)]):
                # print(f"+ {y=}/{x=}")
                count += 1
    return count

def detect_vert_twos(field):
    # '1' accompanied by a '1' below and then a '0'
    count = 0
    for y,row in enumerate(field[:-2]):
        for x,item in enumerate(row):
            if item == 1 \
                and field[y+1][x] == 1 and field[y+2][x] == 0 \
                and neighbors_are_0_or_edge(field,[(y,x),(y+1,x)]):
                count += 1
    return count
    
def get_orientation(poslist):
    ''' 
    determine the orientation by checking the first two items
    they have either identical x- or y-values
    returns "hor" or "vert"
    '''
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
        # check 3 values on the left, 3 values on the right, above/below for all
        for index,pos in enumerate(poslist):
            if len(poslist) >1:
                print(f"{index=} {pos=}")
            if index == 0:
                for y in range(max(pos[0]-1,0), min(pos[0]+1,len(field)-1)+1):
                    x = max(pos[1]-1,0)
                    print("hor left",y,x)
                    if field[y][x]  != 0:
                        print("XX")
                        return False
            if index == len(poslist)-1:
                for y in range(max(pos[0]-1,0), min(pos[0]+1,len(field)-1)+1):
                    x = min(pos[1]+1,len(field)-1)
                    print("hor right",y,x)
                    if field[y][x]  != 0:
                        print("XX")
                        return False
            x = pos[1]
            for y in (max(pos[0]-1,0),min(pos[0]+1,len(field)-1)):
                print("hor inner",y,x)
                if field[y][x] != 0 and y != pos[0]:
                    print("XX")
                    return False
    else:
        # check 3 values above, 3 values below, right/left for all
        for index,pos in enumerate(poslist):
            # print(f"{index=} {pos=}")
            if index == 0:
                for x in range(max(pos[1]-1,0), min(pos[1]+1,len(field)-1)+1):
                    y = max(pos[0]-1,0)
                    # print("vert above",y,x)
                    if field[y][x]  != 0:
                        return False
            if index == len(poslist)-1:
                for x in range(max(pos[1]-1,0), min(pos[1]+1,len(field)-1)+1):
                    y = min(pos[0]+1,len(field)-1)
                    # print("vert below",y,x)
                    if field[y][x]  != 0:
                        return False
            y = pos[0]
            for x in (max(pos[1]-1,0),min(pos[1]+1,len(field)-1)):
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
    print(f"1-ships: {detect_ones(field)}")
    print(f"horizontal 2-ships: {detect_hor_twos(field)}")
    print(f"vertical 2-ships: {detect_vert_twos(field)}")
    print(f"horizontal 3-ships: {detect_hor_threes(field)}")
    print(f"vertical 3-ships: {detect_vert_threes(field)}")
    return True
