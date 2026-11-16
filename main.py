import time

from services.student_service import StudentService
from input_output.student_input import StudentInput
from input_output.student_output import StudentOutput


def add_students(service):
    # 1. Nhập sinh viên mới.
    num_students = StudentInput.read_int("Nhập số lượng sinh viên cần thêm: ")
    print()
    for i in range(num_students):
        StudentOutput.print_title(f"NHẬP SINH VIÊN THỨ {i + 1}")
        StudentInput.read_student(service)


def show_all(service):
    # 2. Hiển thị danh sách sinh viên.
    print()
    StudentOutput.show_list(service.students, "DANH SÁCH SINH VIÊN")


def save(service):
    # 3. Lưu dữ liệu vào file JSON (hỏi lại nếu file gốc bị hỏng để tránh ghi đè).
    if service.load_failed and not StudentInput.read_yes_no("File JSON gốc bị lỗi, lưu sẽ ghi đè file cũ. Tiếp tục? (y/n): "):
        print("\nĐã hủy lưu, file JSON gốc được giữ nguyên.")
        return

    try:
        service.save_data()
        print(f"\nĐã lưu dữ liệu vào '{service.json_service.file_path}' thành công.")
    except (OSError, TypeError) as e:
        StudentOutput.error(f"Lỗi khi ghi file JSON: {e}")


def search_by_id(service):
    # 4. Tìm kiếm sinh viên theo MSSV.
    student_id = input("Nhập ID cần tìm 🔎: ")
    StudentOutput.print_student(service.find_by_id(student_id), "KẾT QUẢ TÌM KIẾM")


def search_by_name(service):
    # 5. Tìm kiếm sinh viên theo họ tên.
    name = input("Nhập họ tên cần tìm 🔎: ")
    print()
    StudentOutput.show_list(service.find_by_name(name), "KẾT QUẢ TÌM KIẾM")


def sort_by_gpa(service):
    # 6. Sắp xếp sinh viên theo GPA.
    print()
    descending = StudentInput.read_yes_no("Sắp xếp giảm dần? (y = giảm dần / n = tăng dần): ")
    print()
    StudentOutput.show_list(service.sort_by_gpa(descending), "DANH SÁCH SẮP XẾP THEO GPA")


def show_statistics(service):
    # 7. Thống kê GPA.
    StudentOutput.show_statistics(service.statistics(), "THỐNG KÊ")


MENU_ACTIONS = {
    "1": add_students,      "2": show_all,
    "3": save,              "4": search_by_id,
    "5": search_by_name,    "6": sort_by_gpa,
    "7": show_statistics,
}

def main():
    # Đọc dữ liệu JSON rồi chạy vòng lặp menu tới khi chọn 0.
    service = StudentService()
    for message in service.load_data():
        print(message)

    while True:
        try:
            StudentOutput.print_menu()
            choice = input("Chọn chức năng: ").strip()
            time.sleep(1)

            if choice == "0":
                if StudentInput.read_yes_no("Lưu dữ liệu trước khi thoát? (y/n): "):
                    save(service)
                print("Tạm biệt!\n")
                break

            action = MENU_ACTIONS.get(choice)
            if action is None:
                StudentOutput.error("Lựa chọn không hợp lệ, vui lòng chọn lại.")
                continue

            action(service)
            time.sleep(2)

        except (KeyboardInterrupt, EOFError):
            print("\nĐã thoát chương trình.")
            break
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()
