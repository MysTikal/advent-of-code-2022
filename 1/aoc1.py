with open('input', 'r') as file:
    data = file.read()

data = data[:-1] #avoid EOF
chunks = eval(data.replace("\n\n", ",").replace("\n", "+")) #evil eval use :)
print(chunks)


print(sum(sorted(chunks, reverse=True)[:3]))
