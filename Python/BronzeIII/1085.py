x, y, w, h = map(int, input().split())
# up down left right
direction = [h-y, y, x, w-x]
print(min(direction))
