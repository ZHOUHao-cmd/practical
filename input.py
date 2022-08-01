design_load = []#design_load为一维列表
for i in range(first_dimension):
    design_load.append([])
    for y in range(second_dimension):
        design_load[i].append(input())

for i in range(first_dimension):
    for j in range(second_dimension):
        print(design_load[i][j])