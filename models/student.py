from models.subject import Subject
from utils.validation import Validator


class Student:
    # Sinh viên gồm mã số, họ tên và danh sách môn học.

    def __init__(self, student_id, name):
        # Tạo sinh viên với danh sách môn học rỗng.
        self.student_id = student_id
        self.name = name
        self.subjects = []

    def add_subject(self, subject):
        # Thêm một môn học cho sinh viên.
        self.subjects.append(subject)

    @property
    def gpa(self):
        # GPA = trung bình điểm các môn, lấy 2 chữ số thập phân (chưa có môn thì 0).
        if not self.subjects:
            return 0.0
        total_score = sum(subject.final_score for subject in self.subjects)
        return Validator.round_half_up(total_score / len(self.subjects), 2)

    def to_dict(self):
        # Chuyển Student thành dictionary để lưu JSON.
        return {
            "student_id": self.student_id,
            "name": self.name,
            "subjects": [subject.to_dict() for subject in self.subjects],
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data):
        # Tạo Student (kèm các môn học) từ dictionary đọc từ JSON.
        student = cls(data["student_id"], data["name"])
        for subject_data in data.get("subjects", []):
            student.add_subject(Subject.from_dict(subject_data))
        return student
