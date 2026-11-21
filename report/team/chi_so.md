# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h == 1` và `mo_lai_trong_7_ngay == 0`, chia tổng số yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | Số quyết định `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ lỗi lọt đến khách | Số yêu cầu có `mo_lai_trong_7_ngay == 1`, chia tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng | % yêu cầu nhóm can thiệp thực sự mở trợ lý | Số `request_id` duy nhất có event `agent_suggestion_shown`, chia số yêu cầu được phân vào nhóm can thiệp | Không cần tính |
| An toàn | % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số mẫu có `so_tien_da_hoan != so_tien_dung`, chia tổng số event `audit_sample_checked` | Không cần tính |

Chỉ số chính trong đợt chạy thử là **82,83% (994/1.200)**. Không kết luận trợ lý đã nâng chỉ số vì đợt chạy thử chưa có nhóm đối chứng đồng thời.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng khách hàng | `request_id`, `loai`, `so_tien`, `arm`, `created_at`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `request_id`, `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mọi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý xuất hiện |
| `staff_review_decision` | Nhân viên CSKH | `request_id`, `staff_id`, `quyet_dinh`, `phut_xem_lai`, `trace_id` | Khi nhân viên giữ, sửa hoặc bỏ gợi ý |
| `staff_rework_completed` | Nhân viên CSKH | `request_id`, `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại hoàn tất |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi giao dịch hoàn phí |
| `handoff_to_staff` | Agent | `request_id`, `reason`, `tom_tat`, `trace_id` | Khi chuyển yêu cầu cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi yêu cầu được mở lại |
| `audit_sample_checked` | Kế toán | `request_id`, `so_tien_da_hoan`, `so_tien_dung`, `checked_at`, `trace_id` | Khi kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính dùng `refund_request_created`, `ticket_closed` và `ticket_reopened` để tính thời gian đóng và theo dõi mở lại trong 7 ngày.
- Tỉ lệ bỏ qua gợi ý dùng `agent_suggestion_shown` và `staff_review_decision` với quyết định `sua` hoặc `bo`.
- Tỉ lệ lỗi lọt đến khách dùng `refund_request_created` và `ticket_reopened`.
- % yêu cầu thực sự mở trợ lý dùng `refund_request_created` (`arm = intervention`) và `agent_suggestion_shown`.
- % đơn hoàn sai tiền dùng `refund_ledger_write` và `audit_sample_checked`; tất cả event nối với nhau bằng `trace_id`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **51,8%**, từ 4.472 đ lên **6.787 đ** [simulated] | Tỉ lệ làm lại theo tuần vượt 7%; mức tham chiếu trong phạm vi `noi_dia` + `hang_nang` là 48/982 = 4,9% | Thu hẹp về `noi_dia`, giới hạn tối đa 2 lần chạy và rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Chi phí đạt **11.743 đ = 0,98×** mức nhân viên tự làm; nếu làm lại mất 15,3 phút thì **12.415 đ = 1,03×** [simulated] | Tỉ lệ yêu cầu được xem lại còn trên 50% vào cuối bước rollout 0,25 hoặc thời gian xem lại trung bình trên 5 phút | Chưa mở rộng rollout; phân tích quyết định `sua`/`bo` và chỉ giảm xem lại theo bậc khi chỉ số an toàn không xấu hơn đối chứng | Trưởng nhóm CSKH |
| Khối lượng thấp hơn kế hoạch | Chi phí cố định là **1.185 đ/việc** ở 45.000 yêu cầu/tháng và tăng thành **2.370 đ/việc** khi khối lượng còn một nửa [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch trong hai tuần liên tiếp | Giữ nguyên quy mô pilot, chưa ký cam kết chi phí cao hơn và rà lại phương án chi phí cố định | PM trợ lý hoàn phí |
