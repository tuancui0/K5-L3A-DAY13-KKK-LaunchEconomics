# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: KKK · Lớp: L3A

| Mục | Nguồn bằng chứng cần lấy | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | `bang_chi_phi.md` · A2–A4 | Toàn mẫu 4.472 đ/việc; `noi_dia` + `hang_nang` 4.599 đ/việc gồm cố định ở 45.000 yêu cầu/tháng. Loại `quoc_te` (1,88×) và `doi_tac` (0,85×, điều khoản riêng) [simulated] | Giả lập | Người viết code |
| 2 · Ba yếu tố nhạy nhất | `bang_chi_phi.md` · B1–B2 | Làm lại gấp đôi: +51,8%; xem lại gấp đôi: +40,7%; lương tăng 25%: +23,1% [simulated] | Giả lập | Người kiểm số |
| 3 · So với nhân viên tự làm | `bang_chi_phi.md` · A2, B3–B4 | Cả hệ thống 5.865 đ/yêu cầu gồm 222 ca làm thay = 0,49× mức 12.000 đ, chưa cộng cố định. Giới hạn 2 lần rẻ nhất: 6.901.220 đ/1.200 yêu cầu. Xem lại 100%: 11.743–12.415 đ/việc [simulated] | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | `chi_so.md` · E1 | Đợt chạy thử: 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại 7 ngày 4,25% (51/1.200). Có 10 event với `trace_id` | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | `bang_loi.md` · C | Trùng 17/20 nhãn (85%); 3 ca bất đồng đã phân biệt; 5/5 loại có phát hiện, khắc phục và vai trò phụ trách | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | `pilot_plan.yaml` · D1–D3 | 20 nhân viên/nhóm, ít nhất 299 yêu cầu/người → 859 hiệu dụng/nhóm ở MDE 6 điểm; power chỉ 0,64 nếu tác động là 5 điểm. Bốn luật dừng; quyết định 28/12/2026 | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | `chi_so.md` · E2 | Làm lại gấp đôi: 6.787 đ/việc; xem lại 100%: 11.743–12.415 đ/việc; khối lượng giảm nửa: cố định 2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot `noi_dia` + `hang_nang`; chưa mở pilot nếu các điều kiện trước ngày bắt đầu chưa đạt.

- **22/11 — Kỹ sư trưởng agent:** kiểm khóa chống hoàn trùng (ca 20) và đối soát sổ cái (ca 7); ngưỡng 0 ca lỗi.
- **22/11 — Giám đốc vận hành:** ký chấp nhận MDE 6 điểm và power 0,64 nếu tác động thật là 5 điểm.
- **30/11 — PM trợ lý hoàn phí:** bật đủ 10 event có `trace_id`, thay phút `simulated` bằng phút đo thật sau tuần đầu.
- **07/12 — Trưởng nhóm CSKH:** chốt lộ trình giảm xem lại theo bậc với kiểm soát an toàn; xem lại 100% có thể tốn 12.415 đ/việc [simulated].
