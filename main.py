from services.student_service import StudentService
from input_output.student_input import StudentInput
from input_output.student_output import StudentOutput
from utils.validation import validate
from UI.view import user_view
import time


def main():

    service = StudentService()
    student_input = StudentInput()
    service.reload_data()
    while True:
        try:
            user_view.print_menu()
            choice = input("Chọn chức năng: ").strip()

            time.sleep(1)

            match choice:
                case "1":
                    n = validate.read_int("Nhập số lượng sinh viên cần thêm: ", 1)
                    print()
                    for i in range(n):
                        print(f"{f' {f"NHẬP SINH VIÊN THỨ {i + 1}"} ':=^50}")
                        student_input.input_student(service)
                        time.sleep(2)
                case "2":
                    print()
                    StudentOutput.show_list(service.get_all(), "DANH SÁCH SINH VIÊN")
                    time.sleep(2)
                case "3":
                    service.save_data()
                    time.sleep(2)
                case "4":
                    id = input("Nhập ID cần tìm 🔎: ")
                    StudentOutput.print_student(
                        service.find_by_id(id), "KẾT QUẢ TÌM KIẾM"
                    )
                    time.sleep(2)
                case "5":
                    name = input("Nhập họ tên cần tìm 🔎: ")
                    print()
                    StudentOutput.show_list(
                        service.find_by_name(name), "KẾT QUẢ TÌM KIẾM"
                    )
                    time.sleep(2)
                case "6":
                    while True:
                        print()
                        order = (
                            input("Sắp xếp giảm dần? (y = giảm dần / n = tăng dần): ")
                            .strip()
                            .lower()
                        )
                        if order in ("y", "n"):
                            break
                        print()
                        print("\033[91mVui lòng chỉ nhập y hoặc n.\033[0m")

                    descending = order == "y"
                    result = service.sort_by_gpa(descending=descending)
                    print()
                    StudentOutput.show_list(result, "DANH SÁCH SẮP XẾP THEO GPA")
                    time.sleep(2)
                case "7":
                    StudentOutput.show_statistics(service, "THỐNG KÊ")
                    time.sleep(2)
                case "0":
                    while True:
                        save = (
                            input("Lưu dữ liệu trước khi thoát? (y/n): ")
                            .strip()
                            .lower()
                        )

                        if save == "y":
                            service.save_data()
                            break

                        elif save == "n":
                            break

                        else:
                            print("\n\033[91mVui lòng chỉ nhập y hoặc n.\033[0m\n")

                    print("Tạm biệt!\n")
                    break

                case _:
                    print("\033[91mLựa chọn không hợp lệ, vui lòng chọn lại.\033[0m")

        except (KeyboardInterrupt, EOFError):
            print("\nĐã thoát chương trình.")
            break
        except Exception as e:
            # Bắt các lỗi không lường trước để chương trình không bị dừng đột ngột
            print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    main()
