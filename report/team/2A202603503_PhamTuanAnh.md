# Báo cáo cá nhân — Phạm Tuấn Anh — 2A202603503

## 1. Thông tin thành viên

- Họ tên: Phạm Tuấn Anh
- MSSV: 2A202603503
- Email: pta070707123@gmail.com
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Ghi bộ nhãn thứ hai cho 20 ca lỗi, tham gia so nhãn và tổng hợp bảng khắc phục của CP3.
- Giữ `ho_so_launch_v0.md`: cập nhật bằng chứng từ CP1 đến CP5, trạng thái và vai trò phụ trách cho từng mục.
- Soạn thảo các phần việc chung trong `pilot_plan.yaml`, `chi_so.md` và `group_report.md` theo quyết định của nhóm; không nhận phần tính code của người viết code hoặc phần đối chiếu số của người kiểm số.

## 3. Đóng góp cụ thể

- CP1–CP2: ghi chi phí 4.472 đ/việc thành công trên toàn mẫu, 4.599 đ/việc trong phạm vi đã cộng cố định, ba yếu tố nhạy nhất và rủi ro xem lại 100% vào hồ sơ [simulated].
- CP3: bảng hiện có 20 nhãn mỗi người, đồng thuận 17/20 ca = 85%; ghi quy tắc phân biệt cho ca 6, 13, 18 và bảng khắc phục 5 ca thuộc đủ 5 loại lỗi. Hai thành viên chịu trách nhiệm xác nhận các bộ nhãn gốc được làm độc lập trước khi so.
- CP4: tổng hợp quyết định chung về chia ngẫu nhiên theo nhân viên, 20 người mỗi nhóm; ghi đánh đổi 859 yêu cầu hiệu dụng/nhóm ở MDE 6 điểm, power khoảng 0,64 nếu tác động thật là 5 điểm, cùng luật dừng và ngày quyết định.
- CP5: tổng hợp ba chỉ số đã được người viết code tính và người kiểm số xác nhận; nối chỉ số với event có `trace_id`, ghi rủi ro kinh tế và hoàn thiện trang hồ sơ Gate 2a cùng nhóm.

## 4. Bằng chứng

- `report/team/bang_loi.md`: hai cột nhãn, mức đồng thuận 85%, ba quy tắc phân biệt và bảng khắc phục 5 ca.
- `report/team/ho_so_launch_v0.md`: bảy mục hồ sơ, trạng thái, vai trò phụ trách và đề xuất cuối.
- `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/group_report.md`: phần việc chung do tôi tổng hợp cho nhóm.

## 5. Công cụ AI đã dùng

- Dùng Codex để đọc yêu cầu, gợi ý nhãn và quy tắc phân biệt, soạn bảng khắc phục, kiểm công thức và hỗ trợ trình bày các file hồ sơ. Nhãn AI gợi ý không thay cho việc hai thành viên xác nhận bộ nhãn độc lập.
- Cách kiểm tra: đếm lại 20 ca và 17 ca trùng; đối chiếu các số chi phí với `bang_chi_phi.md`, ba chỉ số với output `lab13.py` và dữ liệu CSV; kiểm `pilot_plan.yaml` bằng `yaml.safe_load` và so các trường với checklist CP4.

## 6. Tự đánh giá

Tôi đã tổng hợp bằng chứng cho quyết định Gate 2a và ghi rõ các giả định `simulated`. Trước khi nộp, tôi cần cùng nhóm rà lần cuối đề xuất, phiếu chấm chéo và việc xác nhận hai bộ nhãn CP3 được làm độc lập.
