class user_view:

    BLUE = "\033[94m"
    CYAN = "\033[96m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"
    GREEN = "\033[92m"

    @staticmethod
    def print_menu():
        print()
        print("╔" + "═" * 44 + "╗")
        print("║         " + user_view.CYAN + "APP QUẢN LÝ KẾT QUẢ HỌC TẬP" + user_view.RESET + "        ║" + user_view.RESET)
        print("╠" + "═" * 44 + "╣" + user_view.RESET)
        print("║  " + user_view.GREEN + "1." + " Nhập sinh viên mới                     " + user_view.RESET + "║" + user_view.RESET)
        print("║  " + user_view.GREEN + "2." + " Hiển thị danh sách sinh viên           " + user_view.RESET + "║" + user_view.RESET)
        print("║  " + user_view.GREEN + "3." + " Lưu dữ liệu vào file JSON              " + user_view.RESET + "║" + user_view.RESET)
        print("║  " + user_view.GREEN + "4." + " Tìm kiếm sinh viên theo MSSV           " + user_view.RESET + "║" + user_view.RESET)
        print("║  " + user_view.GREEN + "5." + " Tìm kiếm sinh viên theo họ tên         " + user_view.RESET + "║" + user_view.RESET)
        print("║  " + user_view.GREEN + "6." + " Sắp xếp sinh viên theo GPA             " + user_view.RESET + "║" + user_view.RESET)
        print("║  " + user_view.GREEN + "7." + " Thống kê GPA                           " + user_view.RESET + "║" + user_view.RESET)
        print("║  " + user_view.RED   + "0." + " Thoát                                  " + user_view.RESET + "║" + user_view.RESET)
        print("╚" + "═" * 44 + "╝" + user_view.RESET)
        print()

    @staticmethod
    def One_line():
        print("═" * 50 + user_view.RESET)

    @staticmethod
    def print_table_header():
        # In tiêu đề cột của bảng
        print(f"{'Mã SV':<12} | {'Họ Tên':<26} | {'GPA':<6}")
        print("=" * 50)

    @staticmethod
    def table_information(msv, name, gpa):
        # In thông tin 1 dòng dữ liệu sinh viên căn chỉnh theo bảng
        print(f"{msv:<12} | {name:<26} | {gpa:<6.2f}")

    @staticmethod
    def print_subject_table(subjects):
        # In bảng điểm chi tiết các môn học của 1 sinh viên

        # 1. In tiêu đề bảng
        print(f"{'STT':<4} | {'Tên Môn Học':<30} | {'40%':<6} | {'60%':<6} | {'Tổng kết':<8}")
        print("-" * 56)

        # 2. Duyệt từng môn và in từng cột
        for i, sub in enumerate(subjects, start=1):
            print(f"{i:<4} | {sub.name:<30} | {sub.score_40:<6.1f} | {sub.score_60:<6.1f} | {sub.final_score:<8.1f}")