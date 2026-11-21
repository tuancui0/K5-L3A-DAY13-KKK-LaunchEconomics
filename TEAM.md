# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 |        |      |       |        |         |
|   2 |        |      |       |        |         |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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
