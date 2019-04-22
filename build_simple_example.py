import csv

with open("four_blocks.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  # Set 1: Color 0 on left, color 1 on right
  for i in range(0,50):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(50,100):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 1, 1])


  # Set 2: Color 1 on right, color 0 on left
  for i in range(0,50):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 1, 1])

  for i in range(50,100):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 0, 0])

  # Set 3: color 0 on upper right triangle, color 1 on lower left triangle
  for i in range(0,100):
    for j in range(i, 100):
        writer.writerow([0, 0, i, j, 0, 0])

  for j in range(0,100):
    for i in range(0, j):
        writer.writerow([0, 0, i, j, 1, 1])


  # Set 4: color 1 on upper right triangle, color 0 on lower left triangle
  for i in range(0,100):
    for j in range(i, 100):
        writer.writerow([0, 0, i, j, 1, 1])

  for j in range(0,100):
    for i in range(0, j):
        writer.writerow([0, 0, i, j, 0, 0])


  # Set 5: color 0 on top half, color 1 on bottom half
  for i in range(0,100):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(0,100):
    for j in range(50, 100):
        writer.writerow([0, 0, i, j, 1, 1])



  # Set 6: color 1 on top half, color 0 on bottom half
  for i in range(0,100):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 1, 1])

  for i in range(0,100):
    for j in range(50, 100):
        writer.writerow([0, 0, i, j, 0, 0])



  