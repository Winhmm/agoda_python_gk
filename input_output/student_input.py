from utils.validation import validate


class StudentInput:

    def input_student(self, service):

        # Nhập một sinh viên cùng các môn học và điểm

        student_id = validate.input_student_id(service)

        name = validate.input_student_name()

        student = service.add_student(student_id, name)

        print()
        # Nhập các môn học
        num_subjects = validate.read_int("+ Nhập số lượng môn học: ", 1)
        print()
        for i in range(num_subjects):

            print(f"----- Môn học thứ {i + 1} -----")
            while True:
                print()
                subject_name = input("- Nhập tên môn học: ").strip()

                if not subject_name:

                    print("\n\033[91mTên môn học không được để trống.\033[0m")
                    continue

                print()
                score_40 = validate.read_score("- Nhập điểm thành phần 1 (40%): ")
                print()
                score_60 = validate.read_score("- Nhập điểm thành phần 2 (60%): ")
                print()

                # Trả về None nếu điểm không hợp lệ (ngoài 0-10 hoặc không phải số)
                if service.add_subject_to_student(
                    student.student_id, subject_name, score_40, score_60
                ):
                    break

        print("\033[92mThêm thành công\033[0m\n")
