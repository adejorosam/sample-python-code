h = []
with open('cat.txt', encoding='utf8') as f:
    for line in f:
        line.strip()
        h.append(line)
        # print(line.strip())
print(h[2])

with open("out.txt", "a") as file_object:
    # Append 'hello' at the end of file
    file_object.write("\n" + h[2])
