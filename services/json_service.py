# services/json_service.py
import json
import os
from models.student import Student
from pathlib import Path


class JsonService:
    # Lớp chịu trách nhiệm đọc/ghi dữ liệu sinh viên vào/ra file JSON.
    # Tách riêng phần I/O ra khỏi logic nghiệp vụ (StudentService) để dễ bảo trì,
    # dễ thay thế nguồn lưu trữ (ví dụ sau này đổi sang SQLite) mà không ảnh hưởng chỗ khác.

    def __init__(self, file_path=None):
        if file_path is None:

            PROJECT_ROOT = Path(__file__).resolve().parent.parent
            self.file_path = PROJECT_ROOT / "data" / "students.json"

        else:
            self.file_path = Path(file_path)

        # Tự động tạo thư mục 'data/' nếu chưa có
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    def save(self, students):
        # Lưu danh sách object Student (list) xuống file JSON.
        # students: list các object Student

        try:

            sorted_students = sorted(
                students, key=lambda student: int(student.student_id.split(".")[1])
            )

            # Lưu danh sách đã được sắp xếp
            data = [student.to_dict() for student in sorted_students]

            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                print(f"\nĐã lưu dữ liệu vào '{self.file_path}' thành công.")
        except (IOError, OSError) as e:
            print(f"\nLỗi khi ghi file JSON: {e}\n")
        except TypeError as e:
            print(f"\nLỗi dữ liệu không thể chuyển sang JSON: {e}\n")

    def load(self):
        # Đọc dữ liệu từ file JSON và trả về danh sách object Student.
        # Nếu file không tồn tại hoặc lỗi định dạng -> trả về list rỗng.

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
