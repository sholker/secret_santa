import random
import json
from multiprocessing import Pool, cpu_count, Manager
from employee import Employee

def create_couple(args: tuple) -> tuple:
    employee_lst, indices = args
    index1, index2 = indices
    return (employee_lst[index1].get_name(), employee_lst[index2].get_name())


def run_parallel(func, lst: list) -> list:
    num_processes = cpu_count()
    with Pool(processes=num_processes) as pool:
        results = pool.map(func, lst)
    return results


def create_couples(employee_lst: list) -> list:
    random.shuffle(employee_lst)  # Shuffle the list
    index_couple_lst = [(i, (i + 1) % len(employee_lst)) for i in range(len(employee_lst))]

    with Manager() as manager:
        employee_shard_lst = manager.list(employee_lst)
        results = run_parallel(create_couple,
                               [(employee_shard_lst, indexes_couple) for indexes_couple in index_couple_lst])
    return results


def create_employee(data: dict) -> Employee:
    return Employee(**data)


def load_data(path: str) -> list:
    with open(path, 'r') as f:
        json_data = json.load(f)
    results = run_parallel(create_employee, json_data)
    return results


if __name__ == '__main__':
    employees = load_data('data.json')
    couples = create_couples(employees)
    print(couples)
