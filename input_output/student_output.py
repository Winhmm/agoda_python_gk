from UI.view import user_view


class StudentOutput:

    @staticmethod
    def print_student(student, title):
        # In một sinh viên.
        print(f"\n{f' {title} ':=^50}")

        # Không tìm thấy
        if student is None:
            print("\n\033[91mKhông tìm thấy sinh viên!\033[0m")
            return

        print("Mã sinh viên:", student.student_id)
        print("Họ tên:", student.name)

        print("Các môn học:")
        user_view.print_subject_table(student.subjects)

        print(f"ĐIỂM TRUNG BÌNH (GPA): {student.gpa:.2f}")

    @staticmethod
    def show_list(students, title):
        # In một danh sách sinh viên.
        print(f"{f' {title} ':=^50}")
        if not students:
            print("\n\033[91mKhông có sinh viên nào.\033[0m")
            return
        user_view.print_table_header()
        for student in students:
            user_view.table_information(student.student_id, student.name, student.gpa)
            user_view.One_line()

    @staticmethod
    def show_statistics(service, title):
        stats = service.statistics()
        if stats is None:
            return
        print()
        print(f"{f' {title} ':=^50}")
        print()
        StudentOutput.print_student(stats["highest"], "SINH VIÊN CÓ GPA CAO NHẤT")
        print()
        StudentOutput.print_student(stats["lowest"], "SINH VIÊN CÓ GPA THẤP NHẤT")
        print(f"\nGPA TRUNG BÌNH CỦA NHÓM SINH VIÊN: {stats['average_gpa']:.2f}")
