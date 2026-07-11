chracthers = int(input("how many chracthers to previeww?"))
file = open("classnote.txt", "r")


print(file.read(chracthers))
file.closed
print()


file = open("classnote.txt","r")
lines = file.readlines()
file.close()
print("total lines:", len(lines))



for i in range(len(lines)):
    print(i + 1 , "->", lines [i].strip())
    print()


word = input("skip lines starting with: ")
file = open("classnote.txt" , "r")