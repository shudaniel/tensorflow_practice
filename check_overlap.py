import pandas

col_names = ['ts','user','x_coordinate','y_coordinate','color', 'label']
data = pandas.read_csv("block_in_middle.txt", names = col_names, header=None, skiprows=1)

dim = data.ts.values.shape[0]

count = 0
# print(data.x_coordinate.values)

for i in range(dim):
  for j in range(i + 1, dim):
    x_1 = data.x_coordinate.values[i]
    y_1 = data.y_coordinate.values[i]
    x_2 = data.x_coordinate.values[j]
    y_2 = data.y_coordinate.values[j]

    if (x_1, y_1) == (x_2, y_2):
      count += 1

print(count)