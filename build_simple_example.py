import csv

with open("four_blocks.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  for i in range(0,500):
    for j in range(0, 500):
        writer.writerow([0, 0, i, j, 0, 4])

  for i in range(500,1000):
    for j in range(0, 500):
        writer.writerow([0, 0, i, j, 1, 5])

  for i in range(0,500):
    for j in range(500, 1000):
        writer.writerow([0, 0, i, j, 2, 6])

  for i in range(500,1000):
    for j in range(500, 1000):
        writer.writerow([0, 0, i, j, 3, 7])
