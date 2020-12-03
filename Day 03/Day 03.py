
treemap = []
for slope in open("input.txt"):
    treemap.append([*slope.strip()])

def countTrees(xMove, yMove):
    treecount = 0
    x = y = 0
    while y < (len(treemap)-1):
        x,y = x+xMove,y+yMove
        x = x%len(treemap[y])
        y = y%len(treemap)
        if treemap[y][x] == "#":
            treecount += 1
    return treecount


print("sol 1: ", countTrees(3, 1))
print("sol 2: ", countTrees(1, 1) * countTrees(3, 1) * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))