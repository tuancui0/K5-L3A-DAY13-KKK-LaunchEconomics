# Báo cáo cá nhân — Nguyễn Tiến Khoa — 2A202603460

## 1. Thông tin thành viên

- Họ tên: Nguyễn Tiến Khoa
- MSSV: 2A202603460
- Email: nkhoa151004@gmail.com
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

- Tính tay một kết quả chi phí để đối chiếu với dữ liệu trace và kết quả chương trình.
- Kiểm tra, điền các phép thử A1 và bảng mô hình chi phí A2 trong `report/team/bang_chi_phi.md`.
- Kiểm tra các khoản lấy từ cột `_simulated` được ghi đúng nhãn `simulated`.
- Kiểm tra yêu cầu CP5 và hoàn thiện đặc tả chỉ số, danh sách event, kiểm tra chéo event và rủi ro kinh tế trong `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

### Đối chiếu A1

- Số lần chạy trung bình khi `p = 0,8`, tối đa 2 lần: `(1 - (1 - 0,8)^2) / 0,8 = 1,20`.
- Số lần chạy trung bình khi chạy đến lúc đúng: `1 / 0,8 = 1,25`.
- Hệ số chi phí mỗi việc thành công, tối đa 3 lần: `1,25`.

### Đối chiếu A2

- Chi phí token: `245.585 đ`.
- Chi phí tool: `84.000 đ`.
- Chi phí xem lại: `1.780.000 đ` [simulated].
- Chi phí làm lại: `2.264.000 đ` [simulated].
- Tổng chi phí: `245.585 + 84.000 + 1.780.000 + 2.264.000 = 4.373.585 đ`.
- Chi phí mỗi việc thành công: `4.373.585 / 978 = 4.472 đ/việc` [simulated].
- Chi phí này gấp `4.472 / 274,7 = 16,3 lần` hóa đơn token và tool chia số yêu cầu.
- Làm lại là khoản lớn nhất: `2.264.000 / 4.373.585 × 100 = 51,8%` tổng chi phí [simulated].

### Kiểm tra và hoàn thiện CP5

- Tính thử chỉ số chính: `994 / 1.200 = 82,83%` yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày.
- Tính tỉ lệ bỏ qua gợi ý: `48 / 177 = 27,12%` yêu cầu được xem lại có quyết định `sua` hoặc `bo`.
- Tính chỉ số an toàn: `51 / 1.200 = 4,25%` yêu cầu mở lại trong 7 ngày.
- Đề xuất thêm một chỉ số dùng và một chỉ số an toàn có công thức đo rõ ràng.
- Đặc tả 10 event có `trace_id` và kiểm tra mỗi chỉ số đều có event nguồn để tính.
- Bổ sung ba rủi ro kinh tế từ bảng độ nhạy, gồm làm lại tăng gấp đôi, xem lại 100% và khối lượng thấp; các số phụ thuộc dữ liệu `_simulated` đều có nhãn `simulated`.

## 4. Bằng chứng

- `report/team/bang_chi_phi.md`: phần A1 và A2 có công thức, kết quả tính tay và nhãn dữ liệu.
- `report/team/chi_so.md`: ba chỉ số tính thử, hai chỉ số đề xuất, 10 event có `trace_id`, kiểm tra chéo event và ba rủi ro kinh tế.
- Dữ liệu đối chiếu: `src/logix_runs.csv` và `src/logix_requests.csv`.
- Kết quả kiểm tra: chi phí mỗi việc thành công `4.472 đ`, khớp số đối chiếu của bài.
- Kết quả CP5 đối chiếu từ CSV: `82,83%`, `27,12%` và `4,25%`.

## 5. Công cụ AI đã dùng

- Dùng Codex để đọc yêu cầu bài, tổng hợp số liệu trace và trình bày phép tính theo đúng biểu mẫu.
- Dùng Codex để rà checklist CP5, cấu trúc event và tính nhất quán giữa chỉ số với nguồn event.
- Tự kiểm tra lại công thức, phép chia, cách làm tròn và nhãn `simulated` bằng dữ liệu CSV của bài.

## 6. Tự đánh giá

- Hoàn thành phần tính tay và đối chiếu số liệu được giao.
- Hoàn thành phần `chi_so.md` của CP5 và kiểm tra các chỉ số đều đo được từ danh sách event.
- Các phép tính có công thức, nguồn dữ liệu và kết quả làm tròn rõ ràng.
- Không thay đổi code, hồ sơ launch, phiếu chấm hoặc các phần thuộc vai trò khác.
