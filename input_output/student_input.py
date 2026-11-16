from models.student import Student
from models.subject import Subject
from utils.validation import Validator
from input_output.student_output import StudentOutput


class StudentInput:
    # Toàn bộ phần nhập từ bàn phím, nhập sai thì báo lỗi và cho nhập lại.

    @staticmethod
    def read_valid(prompt, check):
        # Hỏi lặp lại tới khi hàm check không còn raise ValueError, trả về giá trị đã chuẩn hóa.
        while True:
            try:
                return check(input(prompt))
            except ValueError as e:
                StudentOutput.error(f"Lỗi: {e}")

    @staticmethod
    def read_int(prompt, min_value=1):
        # Nhập một số nguyên >= min_value.
        while True:
            try:
                value = int(input(prompt))
                if value >= min_value:
                    return value
            except ValueError:
                pass
            StudentOutput.error(f"Vui lòng nhập một số nguyên >= {min_value}.")

    @staticmethod
    def read_score(prompt):
        # Nhập điểm trong khoảng 0 - 10, làm tròn 1 chữ số thập phân.
        return StudentInput.read_valid(
            prompt,
            lambda value: Validator.round_half_up(Validator.validate_score(value), 1),
        )

    @staticmethod
    def read_yes_no(prompt):
        # Hỏi y/n, trả về True nếu chọn y.
        while True:
            answer = input(prompt).strip().lower()
            if answer in ("y", "n"):
                return answer == "y"
            StudentOutput.error("Vui lòng chỉ nhập y hoặc n.")

    @staticmethod
    def read_student_id(service):
        # Nhập mã sinh viên đúng định dạng 'SV.X' và chưa tồn tại.

        def check(value):
            student_id = Validator.validate_student_id(value)
            if service.find_by_id(student_id) is not None:
                raise ValueError(f"Mã '{student_id}' đã tồn tại. Vui lòng nhập lại!")
            return student_id

        return StudentInput.read_valid("+ Nhập mã sinh viên (VD: SV.1): ", check)

    @staticmethod
    def read_student(service):
        # Nhập 1 sinh viên kèm các môn học, nhập đủ rồi mới thêm vào danh sách.
        print()
        student_id = StudentInput.read_student_id(service)
        print()
        name = StudentInput.read_valid("+ Nhập họ tên: ", Validator.validate_name)
        student = Student(student_id, name)

        print()
        num_subjects = StudentInput.read_int("+ Nhập số lượng môn học: ")
        print()
        for i in range(num_subjects):
            print(f"----- Môn học thứ {i + 1} -----")
            print()
            subject_name = StudentInput.read_valid(
                "- Nhập tên môn học: ", Validator.validate_subject_name
            )
            print()
            score_40 = StudentInput.read_score("- Nhập điểm thành phần 1 (40%): ")
            print()
            score_60 = StudentInput.read_score("- Nhập điểm thành phần 2 (60%): ")
            print()
            student.add_subject(Subject(subject_name, score_40, score_60))

        service.add_student(student)
        StudentOutput.success("Thêm thành công")
