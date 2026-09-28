from services.student_service import StudentService
from input_output.student_input import StudentInput
from input_output.student_output import StudentOutput


def read_int(prompt, min_value=None):
    """Đọc một số nguyên, nhập sai thì yêu cầu nhập lại."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                raise ValueError
            return value
        except ValueError:
            if min_value is not None:
                print(f"Vui lòng nhập một số nguyên >= {min_value}.")
            else:
                print("Vui lòng nhập một số nguyên.")


def input_student(service, student_input):
    """Nhập một sinh viên cùng các môn học và điểm."""
    # Nhập MSSV, họ tên (lặp lại nếu trống hoặc trùng MSSV)
    while True:
        student_id, name = student_input.input_student()
        student = service.add_student(student_id.strip(), name.strip())
        if student is not None:
            break
        print("Vui lòng nhập lại.")

    # Nhập các môn học
    num_subjects = read_int("Nhập số lượng môn học: ", 1)
    for i in range(num_subjects):
        print(f"--- Môn học thứ {i + 1} ---")
        while True:
            subject_name = input("Nhập tên môn học: ").strip()
            if not subject_name:
                print("Tên môn học không được để trống.")
                continue
            score_40 = input("Nhập điểm thành phần 1 (40%): ")
            score_60 = input("Nhập điểm thành phần 2 (60%): ")
            # Trả về None nếu điểm không hợp lệ (ngoài 0-10 hoặc không phải số)
            if service.add_subject_to_student(student.student_id, subject_name, score_40, score_60):
                break
            print("Vui lòng nhập lại môn học này.")


def show_list(students, student_output, title):
    """In một danh sách sinh viên."""
    if not students:
        print("Không có sinh viên nào.")
        return
    print(f"\n========== {title} ==========")
    for student in students:
        print("-" * 40)
        student_output.print_student(student)
    print("-" * 40)


def show_statistics(service, student_output):
    stats = service.statistics()
    if stats is None:
        return
    print("\n========== THỐNG KÊ ==========")
    print("Sinh viên có GPA cao nhất:")
    student_output.print_student(stats["highest"])
    print("\nSinh viên có GPA thấp nhất:")
    student_output.print_student(stats["lowest"])
    print(f"\nGPA trung bình của nhóm: {stats['average_gpa']:.2f}")


def print_menu():
    print("\n=========== QUẢN LÝ KẾT QUẢ HỌC TẬP ===========")
    print("1. Nhập sinh viên mới")
    print("2. Hiển thị danh sách sinh viên")
    print("3. Lưu dữ liệu vào file JSON")
    print("4. Đọc dữ liệu từ file JSON và hiển thị")
    print("5. Tìm kiếm sinh viên theo MSSV")
    print("6. Tìm kiếm sinh viên theo họ tên")
    print("7. Sắp xếp sinh viên theo GPA")
    print("8. Thống kê GPA")
    print("0. Thoát")


def main():
    service = StudentService()
    student_input = StudentInput()
    student_output = StudentOutput()

    while True:
        try:
            print_menu()
            choice = input("Chọn chức năng: ").strip()

            if choice == "1":
                n = read_int("Nhập số lượng sinh viên cần thêm: ", 1)
                for i in range(n):
                    print(f"\n===== NHẬP SINH VIÊN THỨ {i + 1} =====")
                    input_student(service, student_input)

            elif choice == "2":
                show_list(service.get_all(), student_output, "DANH SÁCH SINH VIÊN")

            elif choice == "3":
                service.save_data()

            elif choice == "4":
                service.reload_data()
                show_list(service.get_all(), student_output, "DỮ LIỆU ĐỌC TỪ JSON")

            elif choice == "5":
                student_id = input("Nhập MSSV cần tìm: ").strip()
                student = service.find_by_id(student_id)
                if student is None:
                    print("Không tìm thấy sinh viên.")
                else:
                    show_list([student], student_output, "KẾT QUẢ TÌM KIẾM")

            elif choice == "6":
                name = input("Nhập họ tên cần tìm: ")
                show_list(service.find_by_name(name), student_output, "KẾT QUẢ TÌM KIẾM")

            elif choice == "7":
                order = input("Sắp xếp giảm dần? (y = giảm dần, n = tăng dần): ").strip().lower()
                result = service.sort_by_gpa(descending=(order != "n"))
                show_list(result, student_output, "DANH SÁCH SẮP XẾP THEO GPA")

            elif choice == "8":
                show_statistics(service, student_output)

            elif choice == "0":
                save = input("Lưu dữ liệu trước khi thoát? (y/n): ").strip().lower()
                if save == "y":
                    service.save_data()
                print("Tạm biệt!")
                break

            else:
                print("Lựa chọn không hợp lệ, vui lòng chọn lại.")

        except (KeyboardInterrupt, EOFError):
            print("\nĐã thoát chương trình.")
            break
        except Exception as e:
            # Bắt các lỗi không lường trước để chương trình không bị dừng đột ngột
            print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()