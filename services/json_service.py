import json
from pathlib import Path

from models.student import Student


class JsonService:
    # Đọc/ghi danh sách sinh viên với file JSON.

    def __init__(self, file_path=None):
        # Mặc định dùng file data/students.json trong project, tự tạo thư mục nếu chưa có.
        if file_path is None:
            project_root = Path(__file__).resolve().parent.parent
            self.file_path = project_root / "data" / "students.json"
        else:
            self.file_path = Path(file_path)

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _sort_key(student):
        # Khóa sắp xếp: tách lấy số sau 'SV.' để SV.2 đứng trước SV.10, mã sai định dạng xếp cuối.
        try:
            return (0, int(student.student_id.split(".")[1]))
        except (IndexError, ValueError):
            return (1, 0)

    def save(self, students):
        # Ghi danh sách sinh viên (sắp theo MSSV) xuống file JSON.
        sorted_students = sorted(students, key=self._sort_key)
        data = [student.to_dict() for student in sorted_students]

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load(self):
        # Đọc file JSON, trả về (danh sách Student, thông báo), bỏ qua bản ghi lỗi.
        if not self.file_path.exists():
            message = f"File '{self.file_path}' chưa tồn tại. Bắt đầu với danh sách rỗng."
            return [], [message]

        with open(self.file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Nội dung file JSON phải là một danh sách.")

        students, messages = [], []
        for i, item in enumerate(data, start=1):
            try:
                students.append(Student.from_dict(item))
            except KeyError as e:
                messages.append(f"Bỏ qua bản ghi thứ {i} do thiếu trường {e}.")
            except (ValueError, TypeError) as e:
                messages.append(f"Bỏ qua bản ghi thứ {i} do dữ liệu không hợp lệ: {e}")
        return students, messages
