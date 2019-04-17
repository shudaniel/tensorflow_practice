import csv

with open("four_blocks.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  for i in range(0,50):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(50,100):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 1, 1])
'''
  for i in range(0,5):
    for j in range(5, 10):
        writer.writerow([0, 0, i, j, 2, 2])

  for i in range(5,10):
    for j in range(5, 10):
        writer.writerow([0, 0, i, j, 3, 3])
'''