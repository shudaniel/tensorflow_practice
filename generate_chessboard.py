import csv

with open("chess.txt",'w') as file:
  writer = csv.writer(file, delimiter = ",")
  writer.writerow(["ts", "user" ,"x_coordinate" ,"y_coordinate" ,"color", "label"])


  for i in range(0,100,2):
    for j in range(0, 100):
        writer.writerow([0, 0, i, j, 0, 0])
        writer.writerow([0, 0, i+1, j, 1, 1])
