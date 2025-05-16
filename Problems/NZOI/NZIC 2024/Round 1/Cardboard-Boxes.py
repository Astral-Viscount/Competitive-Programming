# https://train.nzoi.org.nz/problems/1371

n = int(input())
cardboard_boxes = []

for i in range(n):
    box_width = int(input())
    cardboard_boxes.append(box_width)

cardboard_boxes = set(cardboard_boxes)
print(len(cardboard_boxes))
