from services.json_service import JsonService
from utils.validation import Validator


class StudentService:
    # Nghiệp vụ quản lý sinh viên: thêm, tìm kiếm, sắp xếp, thống kê, lưu/đọc.

    def __init__(self, json_service=None):
        # Khởi tạo danh sách rỗng, load_failed = True khi file JSON bị hỏng.
        self.json_service = json_service or JsonService()
        self.students = []
        self.load_failed = False

    def load_data(self):
        # Nạp dữ liệu từ file JSON, file hỏng thì bắt đầu rỗng, trả về danh sách thông báo.
        try:
            self.students, messages = self.json_service.load()
            self.load_failed = False
            return messages
        except (ValueError, OSError) as e:
            self.students = []
            self.load_failed = True
            return [f"Lỗi khi đọc file JSON: {e}"]

    def save_data(self):
        # Lưu toàn bộ danh sách sinh viên xuống file JSON.
        self.json_service.save(self.students)
        self.load_failed = False

    def add_student(self, student):
        # Thêm sinh viên mới, không cho phép trùng MSSV.
        if self.find_by_id(student.student_id) is not None:
            raise ValueError(f"Mã sinh viên '{student.student_id}' đã tồn tại!")
        self.students.append(student)

    def find_by_id(self, student_id):
        # Tìm sinh viên theo MSSV (không phân biệt hoa/thường), không thấy trả về None.
        student_id = student_id.strip().upper()
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_by_name(self, name):
        # Tìm sinh viên có họ tên chứa từ khóa (không phân biệt hoa/thường).
        keyword = name.strip().lower()
        return [s for s in self.students if keyword in s.name.lower()]

    def sort_by_gpa(self, descending=True):
        # Trả về danh sách mới sắp theo GPA, không làm thay đổi danh sách gốc.
        return sorted(self.students, key=lambda s: s.gpa, reverse=descending)

    def statistics(self):
        # Thống kê GPA cao nhất, thấp nhất, trung bình; danh sách rỗng trả về None.
        if not self.students:
            return None

        highest = max(self.students, key=lambda s: s.gpa)
        lowest = min(self.students, key=lambda s: s.gpa)
        average_gpa = Validator.round_half_up(sum(s.gpa for s in self.students) / len(self.students), 2)
        return {"highest": highest, "lowest": lowest, "average_gpa": average_gpa}
