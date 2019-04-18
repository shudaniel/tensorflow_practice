import csv

with open("test_blocks.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  for i in range(0,100):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(0, 33):
    for j in range(50, 100):
        writer.writerow([0, 0, i, j, 1, 1])

  for i in range(33,66):
    for j in range(50, 100):
        writer.writerow([0, 0, i, j, 2, 2])

  for i in range(66,100):
    for j in range(50, 100):
        writer.writerow([0, 0, i, j, 3, 3])