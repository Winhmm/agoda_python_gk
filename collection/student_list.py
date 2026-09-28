class StudentList:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def remove(self, student):
        self.students.remove(student)

    def get_all(self):
        return self.students

    def size(self):
        return len(self.students)

    def is_empty(self):
        return len(self.students) == 0

    