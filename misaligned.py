
major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
manualReference = {}
def print_color_map():
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
            manualReference[str({major} | {minor})] = i * 5 + j
    return len(major_colors) * len(minor_colors)
result = print_color_map()
assert(result == 25)
assert(manualReference[str({"White"} | {"Blue"})] == 1)
assert(manualReference[str({"Black"} | {"Green"})] == 12)
print("All is well (maybe!)\n")
