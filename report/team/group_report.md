# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: KKK
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm dùng 1.624 trace của 1.200 yêu cầu giả lập để tính chi phí mỗi việc thành công, kiểm độ nhạy và thiết kế pilot có đối chứng. Quyết định Gate 2a dựa trên chi phí, lỗi, chỉ số dùng và an toàn; chưa suy diễn tác động từ đợt chạy thử không có đối chứng.

## 3. Giải pháp

Cả nhóm dùng `src/lab13.py` để tính A1–A4 và B1–B4; người kiểm số đối chiếu kết quả với trace, nhóm ghi vào `bang_chi_phi.md`. Hai người gắn nhãn so 20 ca lỗi, thống nhất ba ca khác nhau và cả nhóm chọn năm cách khắc phục trong `bang_loi.md`.

Cả nhóm chọn chia pilot ngẫu nhiên theo nhân viên (20 người mỗi nhóm), ghi rõ đánh đổi MDE 6 điểm và power khoảng 0,64 nếu tác động thật là 5 điểm; kế hoạch ở `pilot_plan.yaml`. Cả nhóm đặc tả chỉ số, event và rủi ro trong `chi_so.md`. Người giữ hồ sơ tổng hợp quyết định chung vào `ho_so_launch_v0.md`.

## 4. Kết quả

Chi phí mỗi việc thành công trên toàn mẫu là 4.472 đ; trong phạm vi `noi_dia` + `hang_nang`, cộng chi phí cố định ở quy mô 45.000 yêu cầu/tháng là 4.599 đ [simulated]. Chi phí cả hệ thống trên toàn mẫu là 5.865 đ/yêu cầu sau khi tính nhân viên làm thay, bằng 0,49× mức tự làm 12.000 đ [simulated]. Nếu xem lại 100%, chi phí trong phạm vi pilot lên 11.743–12.415 đ/việc [simulated].

Hai bộ nhãn trùng 17/20 ca (85%). Trong đợt chạy thử, chỉ số chính là 82,83% (994/1.200), tỉ lệ bỏ qua gợi ý 27,12% (48/177), tỉ lệ mở lại 7 ngày 4,25% (51/1.200). Cả nhóm đề xuất **Go có điều kiện** cho kế hoạch pilot, với điều kiện xử lý lỗi sổ cái và hoàn trùng, chấp nhận đánh đổi cỡ mẫu, bật event và thay phút giả lập bằng thời gian đo thật. Ở bước duyệt chéo, nhóm KKK chấm hồ sơ của nhóm RealCua được 25/30 (đề xuất khớp bằng chứng 5, số giả lập và phạm vi 10, pilot ra được quyết định 10) và kết luận Go có điều kiện: xem lại 100% có thể xoá lợi thế chi phí (11.743–12.415 đ so với 12.000 đ) [simulated], và power chỉ 0,64 nếu tác động thật là 5 điểm.

## 5. Khó khăn và cách xử lý

Khi chia theo 40 nhân viên, cỡ mẫu hiệu dụng tối đa ở mức chênh 5 điểm không đạt 1.251 yêu cầu mỗi nhóm. Nhóm chấp nhận thiết kế đo mức chênh 6 điểm, giữ bước rollout 50% trong 14 ngày và đặt điều kiện tối thiểu 299 yêu cầu mỗi nhân viên. Hai cột phút `_simulated` chưa phải thời gian đo thật; pilot phải thay chúng bằng event thời gian thực.

## 6. Tổng hợp đóng góp

Các quyết định về phạm vi, pilot, luật dừng, chỉ số và đề xuất là công việc chung của nhóm. Người viết code tạo kết quả tính, người kiểm số đối chiếu, hai người gắn nhãn xử lý CP3, người giữ hồ sơ tổng hợp file. Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md` và báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Đợt chạy thử chưa có đối chứng nên không chứng minh trợ lý làm tăng chỉ số chính. Chi phí phụ thuộc mạnh vào số ca làm lại (+51,8% nếu gấp đôi) và thời gian xem lại. Pilot phải đo thời gian nhân viên thật, đối soát sổ cái và theo dõi chênh lệch với nhóm đối chứng trước khi quyết định mở rộng [simulated đối với số chi phí].

## 8. Tài liệu tham khảo

- `README.md`, `RULES.md`, `CHECKPOINTS.md`, `RUBRIC.md`, `SUBMISSION.md` của lab.
- `docs/du_lieu_va_cong_thuc.md` và `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`.
- `src/logix_runs.csv`, `src/logix_requests.csv` (dữ liệu giả lập của lab).
