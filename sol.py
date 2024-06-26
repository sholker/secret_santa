import json
import random
from multiprocessing import Pool, cpu_count

class Employee():
    '''
	{
		"department": "R&D",
		"name": "Nikolas Porter",
		"age": 46
	},'''

    def __init__(self, department: str, name: str, age: int):
        self.department = department
        self.name = name
        self.age = age

    def get_name(self):
        return self.name


    def __str__(self):
        return f"{self.department}, {self.name},{self.age}"


def load_data(path: str) -> list:
    employee_lst = []
    with open(path,'r') as f:
        json_data = json.load(f)

    for e in json_data:

        employee_lst.append(Employee(**e))
    return employee_lst

result_couple = tuple()


def create_couples(employee_lst: list) -> tuple:

    random.shuffle(employee_lst) # Shuffle the list

    n = len(employee_lst)

    '''[1,2,3]
    [ (1,2),(2,3), (3, 1) ]
    index -> (0,1), (1,2), (2,0)
    i=0 -> i + 1 % n = 1 % 3 = 1
    i=1 -> i + 1 % n = 2 % 3 = 2
    i=2 -> i + 1 % n = 3 % 3 = 0
    '''
    return [(employee_lst[i].get_name(), employee_lst[(i+1)%n].get_name()) for i in range(n)]



if __name__ =="__main__":
    employee_lst = load_data("data.json")
    result = create_couples(employee_lst)

    print(result)

