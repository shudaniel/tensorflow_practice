import csv

with open("test_blocks.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])


  # Test 1: 80% color 1 on left, 20% color 0 on right
  for i in range(0,80):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 1, 1])

  for i in range(80,100):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 0, 0])



  # Test 2: 35% color 0 on top half, 65% color 1 on bottom half
  for i in range(0,100):
    for j in range(0, 35):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(0,100):
    for j in range(35, 100):
        writer.writerow([0, 0, i, j, 1, 1])

  # LEFT AND RIGHT

  # for i in range(0,100):
  #   for j in range(0, 50):
  #       writer.writerow([0, 0, i, j, 0, 0])

  # for i in range(0,100):
  #   for j in range(50, 100):
  #       writer.writerow([0, 0, i, j, 1, 1])



  # for i in range(0,100):
  #   for j in range(0, 50):
  #       writer.writerow([0, 0, i, j, 0, 0])

  # for i in range(0, 33):
  #   for j in range(50, 100):
  #       writer.writerow([0, 0, i, j, 1, 1])

  # for i in range(33,66):
  #   for j in range(50, 100):
  #       writer.writerow([0, 0, i, j, 2, 2])

  # for i in range(66,100):
  #   for j in range(50, 100):
  #       writer.writerow([0, 0, i, j, 3, 3])