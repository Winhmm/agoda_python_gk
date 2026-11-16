RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

MENU_ITEMS = [
    "Nhập sinh viên mới",
    "Hiển thị danh sách sinh viên",
    "Lưu dữ liệu vào file JSON",
    "Tìm kiếm sinh viên theo MSSV",
    "Tìm kiếm sinh viên theo họ tên",
    "Sắp xếp sinh viên theo GPA",
    "Thống kê GPA",
]


class StudentOutput:
    # Toàn bộ phần in ra màn hình: menu, bảng, kết quả, thông báo.

    @staticmethod
    def error(message):
        # In thông báo lỗi màu đỏ.
        print(f"\n{RED}{message}{RESET}\n")

    @staticmethod
    def success(message):
        # In thông báo thành công màu xanh lá.
        print(f"{GREEN}{message}{RESET}\n")

    @staticmethod
    def print_title(title):
        # In tiêu đề căn giữa giữa các dấu '=' (rộng 50 ký tự).
        title = f" {title} "
        print(f"{title:=^50}")

    @staticmethod
    def print_menu():
        # In menu chính dạng khung.
        print()
        print("╔" + "═" * 44 + "╗")
        print(f"║         {CYAN}APP QUẢN LÝ KẾT QUẢ HỌC TẬP{RESET}        ║")
        print("╠" + "═" * 44 + "╣")
        for i, item in enumerate(MENU_ITEMS, start=1):
            print(f"║  {GREEN}{i}. {item:<39}{RESET}║")
        print(f"║  {RED}0. {'Thoát':<39}{RESET}║")
        print("╚" + "═" * 44 + "╝")
        print()

    @staticmethod
    def print_student_table(students):
        # In bảng danh sách sinh viên: MSSV | Họ tên | GPA.
        print(f"{'Mã SV':<12} | {'Họ Tên':<26} | {'GPA':<6}")
        print("=" * 50)
        for student in students:
            print(f"{student.student_id:<12} | {student.name:<26} | {student.gpa:<6.2f}")
            print("═" * 50)

    @staticmethod
    def print_subject_table(subjects):
        # In bảng điểm chi tiết các môn học của 1 sinh viên.
        print(f"{'STT':<4} | {'Tên Môn Học':<30} | {'40%':<6} | {'60%':<6} | {'Tổng kết':<8}")
        print("-" * 56)
        for i, subject in enumerate(subjects, start=1):
            print(
                f"{i:<4} | {subject.name:<30} | {subject.score_40:<6.1f} | "
                f"{subject.score_60:<6.1f} | {subject.final_score:<8.1f}"
            )

    @staticmethod
    def print_student(student, title):
        # In chi tiết 1 sinh viên: thông tin, bảng điểm, GPA.
        print()
        StudentOutput.print_title(title)

        if student is None:
            print(f"\n{RED}Không tìm thấy sinh viên!{RESET}")
            return

        print("Mã sinh viên:", student.student_id)
        print("Họ tên:", student.name)
        print("Các môn học:")
        StudentOutput.print_subject_table(student.subjects)
        print(f"ĐIỂM TRUNG BÌNH (GPA): {student.gpa:.2f}")

    @staticmethod
    def show_list(students, title):
        # In danh sách sinh viên dạng bảng kèm tiêu đề.
        StudentOutput.print_title(title)
        if not students:
            print(f"\n{RED}Không có sinh viên nào.{RESET}")
            return
        StudentOutput.print_student_table(students)

    @staticmethod
    def show_statistics(stats, title):
        # In kết quả thống kê lấy từ StudentService.statistics().
        if stats is None:
            print("Danh sách sinh viên rỗng, không thể thống kê.")
            return
        print()
        StudentOutput.print_title(title)
        print()
        StudentOutput.print_student(stats["highest"], "SINH VIÊN CÓ GPA CAO NHẤT")
        print()
        StudentOutput.print_student(stats["lowest"], "SINH VIÊN CÓ GPA THẤP NHẤT")
        print(f"\nGPA TRUNG BÌNH CỦA NHÓM SINH VIÊN: {stats['average_gpa']:.2f}")
