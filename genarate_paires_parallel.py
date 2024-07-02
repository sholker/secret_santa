import random
import json
from multiprocessing import Pool, cpu_count, Manager, Queue
from employee import Employee


def run_parallel(func, lst: list) -> list:
    num_processes = cpu_count()
    with Pool(processes=num_processes) as pool:
        results = pool.map(func, lst)
    return results


def create_employee(data: dict) -> Employee:
    return Employee(**data)


def load_data(path: str) -> list:
    try:
        with open(path, 'r') as f:
            json_data = json.load(f)
        results = run_parallel(create_employee, json_data)
        return results
    except FileNotFoundError:
        print(f"File {path} not found")
        exit(1)


def check_duplicates(args) -> None:
    employee, lock, unique_employees = args
    with lock:
        if employee not in unique_employees:
            unique_employees.append(employee)  # Add unique employee to the list


def remove_duplicates(employee_lst: list) -> list:
    with Manager() as manager:
        lock = manager.Lock()  # avoid race conditions
        unique_employees = manager.list()
        run_parallel(check_duplicates, [(e, lock, unique_employees) for e in employee_lst])

        return list(unique_employees)


def create_couple(args: tuple) -> tuple:
    employee_lst, indices = args
    index1, index2 = indices
    return (employee_lst[index1].get_name(), employee_lst[index2].get_name())


def create_couples(employee_lst: list) -> list:
    random.shuffle(employee_lst)  # Shuffle the list

    with Manager() as manager:
        employee_shard_lst = manager.list(employee_lst)
        # create a list of tuples with the index of the employees to be paired
        index_couple_lst = [(i, (i + 1) % len(employee_shard_lst)) for i in range(len(employee_shard_lst))]

        results = run_parallel(create_couple,
                               [(employee_shard_lst, indexes_couple) for indexes_couple in index_couple_lst])
    return results


if __name__ == '__main__':
    couples = create_couples(remove_duplicates(load_data('data.json')))
    # print(len(couples))
    print(couples)
