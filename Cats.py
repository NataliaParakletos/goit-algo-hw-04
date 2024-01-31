from pathlib import Path

with open("D:\Python\cats_file.txt", "w") as cats:
    cats.write("60b90c1c13067a15887e1ae1,Tayson,3\n\
               60b90c2413067a15887e1ae2,Vika,1\n\
               60b90c2e13067a15887e1ae3,Barsik,2\n\
               60b90c3b13067a15887e1ae4,Simon,12\n\
               60b90c4613067a15887e1ae5,Tessi,5")


def get_cats_info(path):
    cats_list = []  

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat = line.strip().split(',')
                cat_info = {"id": cat[0], "name": cat[1], "age": int(cat[2])}
                cats_list.append(cat_info)
    
    except FileNotFoundError:
        print("File not found.")
    
    return cats_list


    
cats_info = get_cats_info("D:\Python\cats_file.txt")
print(cats_info)