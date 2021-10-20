def floodFill(image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    stack = [(sr, sc)]
    start = image[sr][sc]
    while stack:
        i, j = stack.pop()
        if image[i][j] == start:
            image[i][j] = newColor
            if i + 1 < len(image):
                stack.append((i + 1, j))
            if i - 1 >= 0:
                stack.append((i - 1, j))
            if j + 1 < len(image[0]):
                stack.append((i, j + 1))
            if j - 1 >= 0:
                stack.append((i, j - 1))
    return image



print(floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))