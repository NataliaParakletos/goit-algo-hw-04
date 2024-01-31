from pathlib import Path

with open("D:\Python\salary.txt", "w") as sal:
    sal.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")

with open("D:\Python\salary.txt", "r") as file1:
    lines=file1.readlines()
    total_salary = 0
    for line in lines:
        name, salary_str = line.strip().split(',')
        salary = int(salary_str)
        total_salary += salary
        average_salary = total_salary / len(lines)
    print(f"Загальна сума {total_salary}, Середня зарплата {average_salary}")