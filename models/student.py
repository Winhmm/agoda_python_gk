# models/student.py
from models.subject import Subject


class Student:

    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.subjects = []  # Danh sách các môn học của sinh viên

    def add_subject(self, subject):
        """Thêm môn học vào danh sách môn học của sinh viên"""
        # isinstance kiểm tra là object đó có thuộc lớp Subject hay không
        if isinstance(subject, Subject):
            self.subjects.append(subject)
        else:
            raise ValueError("subject phải là một instance của lớp Subject")

    # @property sử dụng để tính toán điểm trung bình của sinh viên dựa trên các môn học đã thêm vào
    @property
    def gpa(self):
        if not self.subjects:
            return 0.0  # Nếu không có môn học, GPA là 0
        # tổng điểm môn học khi duyệt từng môn học trong danh sách subjects
        total_score = sum(subject.final_score for subject in self.subjects)
        return round(
            total_score / len(self.subjects), 2
        )  # tổng điểm / số môn học ,kết quả làm tròn 2 chữ số sau dấu thập phân

    def to_dict(self):
        # Chuyển object Student thành Dictionary để sau này lưu vào JSON
        return {
            "student_id": self.student_id,
            "name": self.name,
            "subjects": [
                subject.to_dict() for subject in self.subjects
            ],  # chuyển từng môn học thành dict
            "gpa": self.gpa,
        }

    # classmethod cho phép gọi phương thức trực tiếp từ class
    # mà không cần tạo object trước.
    # cls đại diện cho class đang sử dụng phương thức.
    @classmethod
    def from_dict(cls, data):
        """Tạo object Student từ Dictionary (khi đọc từ JSON)"""
        student = cls(data["student_id"], data["name"])
        # duyệt dữ liệu môn học trong danh sách môn học nếu không có trả về list rỗng
        for subject_data in data.get("subjects", []):
            subject = Subject.from_dict(
                subject_data
            )  # Tạo object Subject từ Dictionary
            student.add_subject(subject)
        return student

    def __str__(self):
        # Hiển thị thông tin sinh viên và các môn học của họ
        # duyệt từng môn học trong list chứa các object Subject và chuyển chúng thành chuỗi, mỗi môn học trên một dòng mới
        subjects = "\n".join(f"- {s}" for s in self.subjects)
        return f"MSSV: {self.student_id}\nHọ tên: {self.name}\nCác môn học:\n{subjects}\nGPA: {self.gpa:.2f}"
