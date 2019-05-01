import csv

with open("two_blocks_lr.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  # Set 1: Color 0 on left, color 1 on right
  for i in range(0,50):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(50,100):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 1, 1])


with open("two_blocks_diag.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  # Set 3: color 0 on upper right triangle, color 1 on lower left triangle
  for i in range(0,100):
    for j in range(i, 100):
        writer.writerow([0, 0, i, j, 0, 0])

  for j in range(0,100):
    for i in range(j, 100):
        writer.writerow([0, 0, i, j, 1, 1])


with open("two_blocks_tb.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  # Set 5: color 0 on top half, color 1 on bottom half
  for i in range(0,100):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(0,100):
    for j in range(50, 100):
        writer.writerow([0, 0, i, j, 1, 1])


with open("corner_color.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  # Set 5: color 0 on top half, color 1 on bottom half
  for i in range(0,65):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 0, 0])
  for i in range(0,100):
    for j in range(50, 100):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(65,100):
    for j in range(0, 50):
        writer.writerow([0, 0, i, j, 1, 1])

with open("checkerboard_big.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  # Set 5: color 0 on top half, color 1 on bottom half

  for col in range(0,4,2):
    for row in range(0,4,2):

      for i in range(row*10,(row+1)*10):
        for j in range(col*10, (col+1)* 10):
            writer.writerow([0, 0, i, j, 0, 0])

      for i in range((row+1)*10,(row+2)*10):
        for j in range(col* 10, (col+1)* 10):
            writer.writerow([0, 0, i, j, 1, 1])

      for i in range(row*10,(row+1)*10):
        for j in range((col+1)*10, (col+2)* 10):
            writer.writerow([0, 0, i, j, 1, 1])

      for i in range((row+1)*10,(row+2)*10):
        for j in range((col+1)*10, (col+2)* 10):
            writer.writerow([0, 0, i, j, 0, 0])


with open("checkerboard_weird.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  # Set 5: color 0 on top half, color 1 on bottom half

  for col in range(0,4,2):
    for row in range(0,4,2):

      for i in range(row*10,(row+1)*10):
        for j in range(col*10, (col+1)* 10):
            writer.writerow([0, 0, i, j, 0, 0])

      for i in range((row+1)*10,(row+2)*10):
        for j in range((col+1)* 10, (col+2)* 10):
            writer.writerow([0, 0, i, j, 1, 1])
  

with open("block_in_middle.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

  for i in range(25,75):
    for j in range(25, 75):
        writer.writerow([0, 0, i, j, 1, 1])

  for i in range(0,100):
    for j in range(0, 25):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(0,25):
    for j in range(25, 75):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(75,100):
    for j in range(25, 75):
        writer.writerow([0, 0, i, j, 0, 0])

  for i in range(0,100):
    for j in range(75, 100):
        writer.writerow([0, 0, i, j, 0, 0])


  with open("block_in_middle_nocolor.txt",'w') as file:
    writer = csv.writer(file, delimiter = ",")
    writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

    for i in range(25,75):
      for j in range(25, 75):
          writer.writerow([0, 0, i, j, 0, 1])

    for i in range(0,100):
      for j in range(0, 25):
          writer.writerow([0, 0, i, j, 0, 0])

    for i in range(0,25):
      for j in range(25, 75):
          writer.writerow([0, 0, i, j, 0, 0])

    for i in range(75,100):
      for j in range(25, 75):
          writer.writerow([0, 0, i, j, 0, 0])

    for i in range(0,100):
      for j in range(75, 100):
          writer.writerow([0, 0, i, j, 0, 0])


  with open("block_in_middle_noxy.txt",'w') as file:
    writer = csv.writer(file, delimiter = ",")
    writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

    for i in range(25,75):
      for j in range(25, 75):
          writer.writerow([0, 0, 0, 0, 1, 1])

    for i in range(0,100):
      for j in range(0, 25):
          writer.writerow([0, 0, 0, 0, 0, 0])

    for i in range(0,25):
      for j in range(25, 75):
          writer.writerow([0, 0, 0, 0, 0, 0])

    for i in range(75,100):
      for j in range(25, 75):
          writer.writerow([0, 0, 0, 0, 0, 0])

    for i in range(0,100):
      for j in range(75, 100):
          writer.writerow([0, 0, 0, 0, 0, 0])

  with open("block_in_middle_simple.txt",'w') as file:
    writer = csv.writer(file, delimiter = ",")
    writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])

    for i in range(33,66):
      for j in range(0, 50):
          writer.writerow([0, 0, i, j, 1, 1])

    for i in range(0,100):
      for j in range(50, 100):
          writer.writerow([0, 0, i, j, 0, 0])

    for i in range(0,33):
      for j in range(0, 50):
          writer.writerow([0, 0, i, j, 0, 0])

    for i in range(66,100):
      for j in range(0, 50):
          writer.writerow([0, 0, i, j, 0, 0])


