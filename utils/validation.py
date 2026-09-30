import re

class validate:

    @staticmethod
    def validateScore(score_input):
        try:
            # Điểm phải nằm từ 0.0 đến 10.0
            score = float(score_input)
            if 0.0 <= score <= 10.0:
                return score
            else:
                raise ValueError(f"Điểm {score} không hợp lệ. Điểm phải từ 0 đến 10.")
        except ValueError as e:
            # Bắt cả lỗi ép kiểu (VD: nhập chữ) và lỗi ngoài khoảng 0-10
            raise ValueError(f"Lỗi dữ liệu điểm: {e}")

    @staticmethod
    def read_int(prompt, min_value=None):
        # Đọc một số nguyên, nhập sai thì yêu cầu nhập lại.
        while True:
            try:
                value = int(input(prompt))
                if min_value is not None and value < min_value:
                    raise ValueError
                return value
            except ValueError:
                if min_value is not None:
                    print(f"\n\033[91mVui lòng nhập một số nguyên >= {min_value}.\033[0m\n")
                else:
                    print("\n\033[91mVui lòng nhập một số nguyên.\033[0m\n")   

    @staticmethod
    def input_student_id(service_instance = None , prompt="+ Nhập mã sinh viên (VD: SV.1): "):
        #Yêu cầu nhập mã sinh viên đúng định dạng SV.X.
        #Pattern: Bắt đầu bằng 'SV.', theo sau là 1 hoặc nhiều chữ số
        
        pattern = r"^SV\.\d+$"
        # ^     : Bắt buộc bắt đầu chuỗi
        # SV\.  : Bắt buộc là 2 chữ 'SV' theo sau bởi dấu chấm '.'
        # \d+   : Theo sau là 1 hoặc nhiều chữ số (0-9)
        # $     : Bắt buộc kết thúc chuỗi tại đó (không được thừa ký tự lạ phía sau)
        print()
        while True:
            # strip() bỏ khoảng trắng thừa, upper() tự đổi 'sv.1' thành 'SV.1'
            val = input(prompt).strip().upper()
            
            if not val:
                print("\n\033[91mLỗi: Mã sinh viên không được để trống!\033[0m\n")
                continue

            if not re.match(pattern, val):
                print("\n\033[91mLỗi: Mã sinh viên phải đúng định dạng 'SV.X' (ví dụ: SV.1, SV.2)!\033[0m\n")
                continue

            # Kiểm tra trùng lặp thông qua service_instance
            if service_instance is not None:
                # Kiểm tra xem ID có nằm trong danh sách students của service không
                is_duplicate = any(s.student_id == val for s in service_instance.students)
                if is_duplicate:
                    print(f"\n\033[91mLỗi: Mã '{val}' đã tồn tại. Vui lòng nhập lại!\033[0m\n")
                    continue

            return val

    @staticmethod
    def input_student_name(prompt="+ Nhập họ tên: "):
        # Yêu cầu nhập họ tên: không rỗng, chuẩn hóa khoảng trắng thừa.
        print()
        while True:
            val = input(prompt).strip()
            
            if not val:               
                print("\n\033[91mLỗi: Họ tên không được để trống!\033[0m\n")
                continue

            # Kiểm tra nếu tên chứa chữ số
            if any(char.isdigit() for char in val):
                print("\n\033[91mLỗi: Họ tên không được chứa chữ số!\033[0m\n")
                continue

            # "   nguyễn     văn      an   " -> ['nguyễn', 'văn', 'an']
            words = val.split()

            # ['nguyễn', 'văn', 'an'] -> "nguyễn văn an"
            single_spaced = " ".join(words)

            # "nguyễn văn an" -> "Nguyễn Văn An"
            formatted_name = single_spaced.title()

            return formatted_name

    @staticmethod
    def read_score(prompt):
        while True:
            try:
                score = float(input(prompt))
                
                if score < 0 or score > 10:
                    # Gộp các print() lại và chèn màu đỏ
                    print("\n\033[91mLỗi: Điểm phải nằm trong khoảng từ 0 đến 10.\033[0m\n")
                    continue

                return round(score, 1)

            except ValueError:
                # Gộp các print() lại và chèn màu đỏ
                print("\n\033[91mLỗi: Điểm phải là một số.\033[0m\n")