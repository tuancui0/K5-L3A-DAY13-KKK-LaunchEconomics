# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: KKK · Lớp: L3A

| Mục | Nguồn bằng chứng cần lấy | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | `bang_chi_phi.md` · A2–A4 | Toàn mẫu: 4.472 đ/việc (978 việc, chưa cộng cố định). Phạm vi `noi_dia` + `hang_nang`: 4.599 đ/việc, đã cộng 40 triệu đ/tháng ở mức 45.000 yêu cầu/tháng; loại `quoc_te` (1,88×) và `doi_tac` (0,85×, có điều khoản riêng) [simulated] | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | `bang_chi_phi.md` · B1, B2 | Số ca làm lại gấp đôi: +51,8%; tỉ lệ xem lại gấp đôi: +40,7%; lương nhân viên tăng 25%: +23,1% chi phí mỗi việc thành công [simulated] | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | `bang_chi_phi.md` · A2, A4, B3, B4 | Toàn mẫu: 5.865 đ/yêu cầu khi cộng 222 ca nhân viên làm thay, bằng 0,49× mức 12.000 đ tự làm; chưa cộng cố định. Giới hạn 2 lần chạy cho chi phí cả hệ thống thấp nhất: 6.901.220 đ/1.200 yêu cầu. Nếu xem lại 100% trong phạm vi pilot: 11.743 đ/việc (0,98×), hoặc 12.415 đ/việc (1,03×) khi làm lại trung bình 15,3 phút [simulated] | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | `chi_so.md` · E1 | ... | Chưa | ... |
| 5 · Bảng lỗi và cách khắc phục | `bang_loi.md` · C | Hai cột nhãn trùng 17/20 ca (85%); 3 ca khác nhãn đã có quy tắc phân biệt; 5/5 loại lỗi có cách phát hiện đo được, cách khắc phục và một vai trò phụ trách | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | `pilot_plan.yaml` · D1–D3 | Chia ngẫu nhiên 20 nhân viên/nhóm; giữ mức 50% trong 14 ngày để đạt ít nhất 299 yêu cầu/người và 859 yêu cầu hiệu dụng/nhóm ở MDE 6 điểm. Nếu tác động thật chỉ 5 điểm, power còn 0,64. Có 4 luật dừng về an toàn, chi phí, mức độ sử dụng; quyết định ngày 28/12/2026 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | `chi_so.md` · E2; `bang_chi_phi.md` · B1, B4 | ... | Chưa | ... |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
