# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

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
- Commit: (điền mã commit sau khi push)
