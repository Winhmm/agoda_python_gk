# services/student_service.py
from models.student import Student
from models.subject import Subject
from services.json_service import JsonService


class StudentService:
    """
    Lớp xử lý logic nghiệp vụ (business logic) liên quan đến sinh viên:
    thêm, tìm kiếm, sắp xếp, thống kê, lưu/đọc dữ liệu.
    StudentService sử dụng JsonService để thao tác với file, tách biệt
    rõ ràng giữa "logic nghiệp vụ" và "lưu trữ dữ liệu".
    """

    def __init__(self, json_service: JsonService = None):
        self.json_service = json_service if json_service else JsonService()
        self.students = self.json_service.load()  # Tải dữ liệu sẵn có (nếu có) khi khởi tạo

    # ---------------------- THÊM SINH VIÊN / MÔN HỌC ----------------------

    def add_student(self, student_id, name):
        """Thêm sinh viên mới. Không cho phép trùng MSSV."""
        try:
            if not student_id or not name:
                raise ValueError("Mã số sinh viên và họ tên không được để trống.")

            if self.find_by_id(student_id) is not None:
                raise ValueError(f"MSSV '{student_id}' đã tồn tại.")

            student = Student(student_id, name)
            self.students.append(student)
            print(f"Đã thêm sinh viên '{name}' (MSSV: {student_id}) thành công.")
            return student
        except ValueError as e:
            print(f"Lỗi khi thêm sinh viên: {e}")
            return None

    def add_subject_to_student(self, student_id, subject_name, score_40, score_60):
        """Thêm môn học (kèm điểm) vào sinh viên theo MSSV."""
        try:
            student = self.find_by_id(student_id)
            if student is None:
                raise ValueError(f"Không tìm thấy sinh viên có MSSV '{student_id}'.")

            subject = Subject(subject_name, score_40, score_60)
            student.add_subject(subject)
            print(f"Đã thêm môn học '{subject_name}' cho sinh viên '{student.name}'.")
            return subject
        except ValueError as e:
            print(f"Lỗi khi thêm môn học: {e}")
            return None

    # ---------------------- TÌM KIẾM ----------------------

    def find_by_id(self, student_id):
        """Tìm sinh viên theo MSSV (trùng khớp chính xác). Trả về None nếu không thấy."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_by_name(self, name):
        """
        Tìm sinh viên theo họ tên (không phân biệt hoa/thường, cho phép chứa 1 phần tên).
        Trả về danh sách các sinh viên khớp (có thể rỗng).
        """
        keyword = name.strip().lower()
        result = [s for s in self.students if keyword in s.name.lower()]
        return result

    # ---------------------- SẮP XẾP ----------------------

    def sort_by_gpa(self, descending=True):
        """Sắp xếp danh sách sinh viên theo GPA. Trả về danh sách mới (không thay đổi self.students)."""
        return sorted(self.students, key=lambda s: s.gpa, reverse=descending)

    # ---------------------- THỐNG KÊ ----------------------

    def statistics(self):
        """
        Thống kê GPA của nhóm sinh viên:
        - Sinh viên có GPA cao nhất
        - Sinh viên có GPA thấp nhất
        - GPA trung bình của cả nhóm
        Trả về dict, hoặc None nếu danh sách rỗng.
        """
        if not self.students:
            print("Danh sách sinh viên rỗng, không thể thống kê.")
            return None

        highest = max(self.students, key=lambda s: s.gpa)
        lowest = min(self.students, key=lambda s: s.gpa)
        avg_gpa = round(sum(s.gpa for s in self.students) / len(self.students), 2)

        return {
            "highest": highest,
            "lowest": lowest,
            "average_gpa": avg_gpa
        }

    # ---------------------- LƯU / TẢI DỮ LIỆU ----------------------

    def save_data(self):
        """Lưu toàn bộ danh sách sinh viên hiện tại xuống file JSON."""
        self.json_service.save(self.students)

    def reload_data(self):
        """Tải lại dữ liệu từ file JSON (ghi đè danh sách hiện tại trong bộ nhớ)."""
        self.students = self.json_service.load()

    # ---------------------- TIỆN ÍCH HIỂN THỊ ----------------------

    def get_all(self):
        """Trả về toàn bộ danh sách sinh viên."""
        return self.students

    def display_all(self):
        """In toàn bộ danh sách sinh viên ra màn hình."""
        if not self.students:
            print("Danh sách sinh viên rỗng.")
            return
        for student in self.students:
            print("-" * 40)
            print(student)
        print("-" * 40)