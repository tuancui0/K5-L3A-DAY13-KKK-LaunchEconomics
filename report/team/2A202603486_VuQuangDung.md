# Báo cáo cá nhân — Vũ Quang Dũng — 2A202603486

## 1. Thông tin thành viên

- Họ tên: Vũ Quang Dũng
- MSSV: 2A202603486
- Email: vuquangdung2309@gmail.com
- Vai trong nhóm: Người gắn nhãn 1

## 2. Phần việc phụ trách

- Đọc đề và theo dõi điều kiện "Xong khi" của từng nhiệm vụ.
- Gắn nhãn độc lập 20 ca lỗi ở CP3 (nhiệm vụ C) theo năm loại của Google PAIR.
- Ở CP5: rà tiến độ các file hồ sơ theo `CHECKPOINTS.md`, điền mục 4 và mục 7 của `report/team/ho_so_launch_v0.md`.

## 3. Đóng góp cụ thể

### CP3 · Gắn nhãn 20 ca lỗi

- Gắn nhãn 20 ca làm cột "Nhãn người 1" trong `report/team/bang_loi.md`; Phạm Tuấn Anh ghi hộ vào file.
- So với người gắn nhãn 2: trùng 17/20 ca, tỉ lệ đồng thuận 85% (đạt mức 80%).
- Ba ca không trùng (6, 13, 18) được nhóm thống nhất và ghi quy tắc phân biệt.

### CP5 · Rà tiến độ và hồ sơ launch

- Rà các sản phẩm của nhiệm vụ E theo "Xong khi": `chi_so.md` đủ ba chỉ số tính thử, hai chỉ số đề xuất, 10 event có `trace_id`, ba dòng rủi ro; `grep -rni production report/team` không in gì.
- Chỉ ra các phần còn thiếu trong hồ sơ: mục 4, mục 7, dòng đề xuất, và người phụ trách mục 1–3 nên là vai trò có quyền quyết định.
- Điền mục 4 (chỉ số) và mục 7 (rủi ro kinh tế) của `ho_so_launch_v0.md`, dùng lại số trong `chi_so.md`:
  - Mục 4: chính 82,83% (994/1.200), dùng 27,12% (48/177), an toàn 4,25% (51/1.200); trạng thái Xong, có bằng chứng.
  - Mục 7: làm lại gấp đôi +51,8% (4.472 → 6.787 đ/việc); xem lại 100% 11.743 đ/việc (0,98×) hoặc 12.415 đ (1,03×); khối lượng còn một nửa 1.185 → 2.370 đ/việc [simulated]; trạng thái Giả lập.

## 4. Bằng chứng

- `report/team/bang_loi.md`: cột "Nhãn người 1", tỉ lệ đồng thuận 17/20 = 85%. Commit `35e1907`.
- `report/team/ho_so_launch_v0.md`: mục 4 và mục 7.
- Đối chiếu ba chỉ số E1 bằng cách tính lại trực tiếp từ `src/logix_requests.csv`: 994/1.200, 48/177, 51/1.200, khớp `chi_so.md`.

## 5. Công cụ AI đã dùng

- Claude Code (Claude Opus 5.5):
  - Hướng dẫn cài môi trường Python trên Windows PowerShell và giải thích lỗi `NotImplementedError` của file khởi đầu.
  - Giải thích năm loại lỗi và cách điền `bang_loi.md`. Claude không gắn nhãn hộ; nhãn do tôi tự chọn.
  - Thực hiện các lệnh git (commit, push) cho `bang_loi.md` theo yêu cầu của tôi.
  - Rà tiến độ CP5 theo `CHECKPOINTS.md` và `RUBRIC.md`; soạn nội dung mục 4 và mục 7 từ số đã có trong `chi_so.md`.
- Cách tự kiểm tra:
  - Tính lại ba chỉ số E1 từ CSV, so với `chi_so.md`.
  - Đối chiếu từng con số trong mục 7 với bảng E2 của `chi_so.md` và `bang_chi_phi.md`.
  - Kiểm tra số dựa trên cột `_simulated` đều có nhãn `simulated`; chạy `grep -rni production report/team`.

## 6. Tự đánh giá

- Hoàn thành phần gắn nhãn CP3; tỉ lệ đồng thuận đạt yêu cầu.
- Hoàn thành mục 4 và mục 7 của hồ sơ launch, số liệu đều truy được về file nguồn.
- Cần cải thiện: lẽ ra phải tự ghi nhãn vào file ngay khi gắn xong, thay vì nhờ người khác ghi hộ.
