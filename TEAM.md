# Team

## Thông tin nhóm

- Tên nhóm: KKK
- Lớp: L3A
- Repo nhóm: [`K5-L3A-DAY13-KKK-LaunchEconomics`](https://github.com/tuancui0/K5-L3A-DAY13-KKK-LaunchEconomics) (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/tuancui0/K5-L3A-DAY13-KKK-LaunchEconomics · nhánh `main` · commit chốt: (điền sau khi push bản cuối lúc 17:45)

## Thành viên

|              STT | Họ tên           | MSSV        | Email                       | GitHub           | Vai trò                          |
| ---------------: | ---------------- | ----------- | --------------------------- | ---------------- | -------------------------------- |
|                1 | Đỗ Tuấn Anh      | 2A202603465 | dotuananh30122004@gmail.com | tuancui0         | Người viết code                  |
|                2 | Nguyễn Tiến Khoa | 2A202603460 | nkhoa151004@gmail.com       | llkhoa           | Người kiểm số                    |
|                3 | Vũ Quang Dũng    | 2A202603486 | vuquangdung2309@gmail.com   | qdung2003 | Người gắn nhãn 1 |
|                4 | Phạm Tuấn Anh    | 2A202603503 | pta070707123@gmail.com      | phamtuananhhatay | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## Nguyễn Tiến Khoa — 2A202603460

### Phần việc phụ trách

- Người kiểm số: tính tay một kết quả để đối chiếu với dữ liệu trace và kết quả chương trình.
- Kiểm tra, điền phần A1 và A2 trong `report/team/bang_chi_phi.md`.
- Kiểm tra các số liệu lấy từ cột `_simulated` có nhãn `simulated`.

### Đóng góp cụ thể

- Đối chiếu ba kết quả A1: `1,20`, `1,25` và `1,25`.
- Tính tổng chi phí: `245.585 + 84.000 + 1.780.000 + 2.264.000 = 4.373.585 đ`.
- Tính chi phí mỗi việc thành công: `4.373.585 / 978 = 4.472 đ/việc` [simulated].
- Kiểm tra chi phí này gấp `16,3 lần` hóa đơn token và tool chia số yêu cầu; làm lại chiếm `51,8%` tổng chi phí [simulated].

### Bằng chứng

- `report/team/bang_chi_phi.md`, phần A1 và A2.
- `report/team/2A202603460_NguyenTienKhoa.md`.
- Dữ liệu đối chiếu: `src/logix_runs.csv` và `src/logix_requests.csv`.

## Đỗ Tuấn Anh-2A202603465

### Phần việc phụ trách

- Người viết code: viết và chạy `src/lab13.py` (CP1 nhiệm vụ A, CP2 nhiệm vụ B, phần tính số của D1 và E1).
- Điền `report/team/bang_chi_phi.md` từ output của `lab13.py`.

### Đóng góp cụ thể

- Viết ba hàm A1 (`so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`), ba phép thử đáp án biết trước đều ĐẠT.
- Viết `mo_hinh` (A2) có đủ tham số giá, hệ số và `max_lan_chay`; dùng lại cho A3, A4 và 9 kịch bản độ nhạy B1, cặp B2, giới hạn chạy lại B3, xem lại 100% B4.
- Viết `co_mau` và tính năm câu D1 (1.251 · 3.103 · 1.000 · 300 · m ≥ 299), power 0,64; tính ba chỉ số E1 (82,83% · 27,12% · 4,25%).
- Điền bảng A1–A4, B1–B4 trong `bang_chi_phi.md`; chi phí mỗi việc thành công 4.472 đ, gấp 16,3 lần hoá đơn token [simulated].

### Bằng chứng

- `src/lab13.py`: `python lab13.py` in "Ba phép thử đáp án biết trước: ĐẠT" và các bảng A2–B4, D1, E1.
- `report/team/bang_chi_phi.md`: số khớp bảng đối chiếu trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md`.
- Commit: `ec17c7e` (nguoi_viet_code)

## Vũ Quang Dũng — 2A202603486

### Phần việc phụ trách

- Người gắn nhãn 1: gắn nhãn 20 ca lỗi ở CP3; rà tiến độ CP5.

### Đóng góp cụ thể

- Gắn nhãn cột "Nhãn người 1" trong `bang_loi.md`, đồng thuận 17/20 = 85%.
- Soạn mục 4, mục 7 của `ho_so_launch_v0.md`.

### Bằng chứng

- `report/team/bang_loi.md` (commit `35e1907`), `report/team/2A202603486_VuQuangDung.md`.
