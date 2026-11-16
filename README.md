# Quản lý kết quả học tập sinh viên (JSON)

Bài A1 – Xử lý dữ liệu có cấu trúc với JSON.

## Thành viên

| STT | Họ và tên | MSSV |
|---|---|---|
| 1 | Nguyễn Chí Hào | 50.01.104.043 |
| 2 | Nguyễn Thanh Phong | 50.01.104.118 |
| 3 | Võ Hoàng Quân | 50.01.104.127 |
| 4 | Nguyễn Đức Tính | 50.01.104.163 |
| 5 | Lê Nhật Trí | 50.01.104.167 |

## Đề bài

### Bài A1. Xử lý dữ liệu có cấu trúc với JSON

#### Mô tả

Xây dựng chương trình quản lý kết quả học tập của một nhóm sinh viên.

Mỗi sinh viên gồm:

- Mã số sinh viên.
- Họ tên.
- Danh sách môn học.
- Điểm thành phần từng môn.
- Điểm tổng kết từng môn.
- GPA.

Mỗi môn học có:

- Điểm thành phần 1: 40%.
- Điểm thành phần 2: 60%.

#### Yêu cầu

Chương trình phải:

1. Cho phép nhập thông tin sinh viên và điểm.
2. Kiểm tra điểm hợp lệ trong khoảng 0–10.
3. Tính điểm môn học:

   ```
   Điểm môn = Điểm 40% × 0.4 + Điểm 60% × 0.6
   ```

4. Điểm môn lấy 01 chữ số thập phân.
5. GPA lấy 02 chữ số thập phân.
6. Lưu toàn bộ dữ liệu vào file JSON.
7. Đọc dữ liệu từ JSON và hiển thị lại.
8. Tìm kiếm sinh viên theo MSSV/họ tên.
9. Sắp xếp sinh viên theo GPA.
10. Thống kê sinh viên có GPA cao nhất, thấp nhất và GPA trung bình của nhóm.
11. Sử dụng try...except để xử lý lỗi.

#### Kết quả cần đạt

Có chương trình Python hoàn chỉnh có khả năng:

Nhập dữ liệu → xử lý → lưu JSON → đọc JSON → tìm kiếm → sắp xếp → thống kê.

## Cách chạy

Yêu cầu: **Python 3.8 trở lên** (đã chạy thử trên Python 3.12). Chỉ dùng thư viện có sẵn của Python, không cần cài thêm gì.

```bash
cd agoda_python_gk
python main.py
```

Khi khởi động, chương trình tự đọc dữ liệu từ `data/students.json` (chưa có file thì bắt đầu với danh sách rỗng).

## Chức năng

| Phím | Chức năng |
|---|---|
| 1 | Nhập sinh viên mới (MSSV dạng `SV.X`, họ tên, các môn học và điểm) |
| 2 | Hiển thị danh sách sinh viên |
| 3 | Lưu dữ liệu vào file JSON |
| 4 | Tìm kiếm sinh viên theo MSSV |
| 5 | Tìm kiếm sinh viên theo họ tên (không phân biệt hoa/thường, tìm theo một phần tên) |
| 6 | Sắp xếp sinh viên theo GPA (tăng dần / giảm dần) |
| 7 | Thống kê GPA cao nhất, thấp nhất, trung bình |
| 0 | Thoát (hỏi có lưu dữ liệu trước khi thoát không) |

## Cấu trúc thư mục

```
agoda_python_gk/
├── main.py                     # Menu chính
├── data/
│   └── students.json           # File dữ liệu
├── models/
│   ├── student.py              # Lớp Student (tính GPA)
│   └── subject.py              # Lớp Subject (tính điểm môn)
├── services/
│   ├── student_service.py      # Thêm, tìm kiếm, sắp xếp, thống kê
│   └── json_service.py         # Đọc/ghi file JSON
├── input_output/
│   ├── student_input.py        # Nhập liệu từ bàn phím
│   └── student_output.py       # In menu, bảng, kết quả
└── utils/
    └── validation.py           # Kiểm tra dữ liệu, làm tròn điểm
```

## Định dạng file JSON

```json
[
    {
        "student_id": "SV.2",
        "name": "Võ Hoàng Quân",
        "subjects": [
            { "name": "python", "score_40": 10.0, "score_60": 10.0, "final_score": 10.0 },
            { "name": "Lý thuyết đồ thị", "score_40": 7.0, "score_60": 8.0, "final_score": 7.6 }
        ],
        "gpa": 8.8
    }
]
```

## Xử lý lỗi

- Nhập sai (điểm ngoài 0 – 10, nhập chữ thay số, MSSV sai định dạng hoặc bị trùng, họ tên rỗng hoặc chứa số) → báo lỗi và cho nhập lại.
- File JSON có bản ghi lỗi → bỏ qua bản ghi đó, vẫn đọc các bản ghi hợp lệ.
- File JSON bị hỏng → bắt đầu với danh sách rỗng và hỏi lại trước khi lưu để không ghi đè mất dữ liệu gốc.
- Lỗi ghi file, lỗi không lường trước → báo lỗi, chương trình không bị dừng đột ngột.
- Nhấn `Ctrl + C` → thoát chương trình gọn gàng, không hiện lỗi.
