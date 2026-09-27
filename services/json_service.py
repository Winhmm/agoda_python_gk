# services/json_service.py
import json
import os
from models.student import Student


class JsonService:
    """
    Lớp chịu trách nhiệm đọc/ghi dữ liệu sinh viên vào/ra file JSON.
    Tách riêng phần I/O ra khỏi logic nghiệp vụ (StudentService) để dễ bảo trì,
    dễ thay thế nguồn lưu trữ (ví dụ sau này đổi sang SQLite) mà không ảnh hưởng chỗ khác.
    """

    def __init__(self, file_path="data/students.json"):
        self.file_path = file_path
        # Đảm bảo thư mục chứa file tồn tại (vd: thư mục "data/")
        folder = os.path.dirname(self.file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

    def save(self, students):
        """
        Lưu danh sách object Student (list) xuống file JSON.
        students: list các object Student
        """
        try:
            data = [student.to_dict() for student in students]
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Đã lưu dữ liệu vào '{self.file_path}' thành công.")
        except (IOError, OSError) as e:
            print(f"Lỗi khi ghi file JSON: {e}")
        except TypeError as e:
            print(f"Lỗi dữ liệu không thể chuyển sang JSON: {e}")

    def load(self):
        """
        Đọc dữ liệu từ file JSON và trả về danh sách object Student.
        Nếu file không tồn tại hoặc lỗi định dạng -> trả về list rỗng.
        """
        if not os.path.exists(self.file_path):
            print(f"File '{self.file_path}' chưa tồn tại. Bắt đầu với danh sách rỗng.")
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            students = [Student.from_dict(item) for item in data]
            return students
        except json.JSONDecodeError as e:
            print(f"Lỗi định dạng file JSON: {e}")
            return []
        except (IOError, OSError) as e:
            print(f"Lỗi khi đọc file JSON: {e}")
            return []
        except (KeyError, ValueError) as e:
            print(f"Dữ liệu JSON không hợp lệ để tạo Student: {e}")
            return []