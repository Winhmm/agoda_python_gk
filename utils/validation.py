import re
from decimal import Decimal, ROUND_HALF_UP


class Validator:
    # Kiểm tra và chuẩn hóa dữ liệu, sai thì raise ValueError.

    @staticmethod
    def round_half_up(value, digits):
        # Làm tròn kiểu 5 thì lên (7.225 -> 7.23).
        step = Decimal(10) ** -digits
        result = Decimal(str(value)).quantize(step, rounding=ROUND_HALF_UP)
        return float(result)

    @staticmethod
    def validate_score(value):
        # Chuyển điểm sang số thực và kiểm tra nằm trong khoảng 0 - 10.
        try:
            score = float(value)
        except (TypeError, ValueError):
            raise ValueError(f"Điểm '{value}' không phải là số.")

        if not 0 <= score <= 10:
            raise ValueError(f"Điểm {score} không hợp lệ. Điểm phải từ 0 đến 10.")
        return score

    @staticmethod
    def validate_student_id(value):
        # Kiểm tra mã sinh viên dạng 'SV.X' (VD: sv.1 -> SV.1), trả về mã đã chuẩn hóa.
        student_id = value.strip().upper()

        if not student_id:
            raise ValueError("Mã sinh viên không được để trống!")

        if not re.fullmatch(r"SV\.\d+", student_id):
            raise ValueError("Mã sinh viên phải đúng định dạng 'SV.X' (ví dụ: SV.1, SV.2)!")
        return student_id

    @staticmethod
    def validate_name(value):
        # Kiểm tra họ tên không rỗng, không chứa số và chuẩn hóa (VD: '  nguyễn  an' -> 'Nguyễn An').
        if not value.strip():
            raise ValueError("Họ tên không được để trống!")

        if any(char.isdigit() for char in value):
            raise ValueError("Họ tên không được chứa chữ số!")

        return " ".join(value.split()).title()

    @staticmethod
    def validate_subject_name(value):
        # Kiểm tra tên môn học không được để trống.
        subject_name = value.strip()
        if not subject_name:
            raise ValueError("Tên môn học không được để trống.")
        return subject_name
