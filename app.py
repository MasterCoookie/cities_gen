from pathlib import Path
from random import randint

def gen_line(cities):
    city_a = cities[randint(0, len(cities) - 1)]
    city_b = cities[randint(0, len(cities) - 1)]

    while city_a == city_b:
        city_b = cities[randint(0, len(cities) - 1)]

    return (city_a + city_b + ' ' + str(randint(1, 9999)) + '\n')[1:]


    

print("Welcome to my generator!\nChoose 1 for limiting by filesize or 2 for limiting by lines count")
choice = input()
file = open("miasta.txt", mode='r', encoding="utf8")
cities = file.read().split('\n')
if choice == '1':
    limit = int(input("Specify file size limit in MB "))
    limit *= 1000000

    file_append = open("miasta_out.txt", mode='a',  encoding="utf8")
    count = 0
    filesize = Path("miasta_out.txt").stat().st_size
    while(filesize < limit):
        line = gen_line(cities)
        file_append.write(line)
        count += 1
        if not count % 10000:
            print(f"{count} lines written. Current file size: {filesize / 1000000} MB")
        filesize = Path("miasta_out.txt").stat().st_size
    print(f"Generated {count} lines")
    

    
if choice == '2':
    limit = int(input("Specify file size limit in lines "))
    file_append = open("miasta_out.txt", mode='a')
    for _ in range(limit):
        line = gen_line(cities)
        file_append.write(line)

    filesize = Path("miasta_out.txt").stat().st_size
    print(f"Generated {count} lines> File size: {filesize / 1000000} MB")