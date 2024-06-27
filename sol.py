import json
import random
from multiprocessing import Pool, cpu_count
from employee import Employee



def load_data(path: str) -> list:
    employee_lst = []
    try:
        with open(path,'r') as f:
            json_data = json.load(f)

        for e in json_data:

            employee_lst.append(Employee(**e))
        return employee_lst
    except FileNotFoundError:
        print(f"File {path} not found")
        exit(1)



def remove_duplicates(employee_lst: list) -> list:
    seen = set() # employees are I see before
    unique_employee_lst = []

    for e in employee_lst:
        if e not in seen:
            seen.add(e)
            unique_employee_lst.append(e)

    return unique_employee_lst


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

    result = create_couples(remove_duplicates(load_data("data.json")))
    # print(len(result))

    print(result)

