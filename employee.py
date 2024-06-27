class Employee:
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

    def get_name(self) -> str:
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.department == other.department and self.age == other.age
    def __hash__(self):
        return hash((self.department, self.name, self.age))
    def __str__(self) -> str:
        return f"{self.department}, {self.name}, {self.age}"

