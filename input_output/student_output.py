class StudentOutput:
 
    def print_student(self, student):
        print("Mã sinh viên:", student.student_id)
        print("Họ tên:", student.name)
 
        if not student.subjects:
            print("Các môn học: (chưa có môn học nào)")
        else:
            print("Các môn học:")
            # Mỗi môn hiển thị theo Subject.__str__: tên, điểm 40%, điểm 60%, tổng
            for i, subject in enumerate(student.subjects, start=1):
                print(f"  {i}. {subject}")
 
        print(f"GPA: {student.gpa:.2f}") 