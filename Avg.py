from pathlib import Path

with open("D:\Python\salary.txt", "w") as sal:
    sal.write("Alex Korp,3000\nNikita Borisenko,2000\nSitarama Raju,1000")


def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

            total_salary = 0
            for line in lines:
                name, salary_str = line.strip().split(',')
                salary = int(salary_str)
                total_salary += salary

            average_salary = total_salary / len(lines)

            return total_salary, average_salary

    except FileNotFoundError:
        return "Файл не знайдено."


    
total, average = total_salary("D:\Python\salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
