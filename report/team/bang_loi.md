# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: qdung2003 · Người gắn nhãn 2: phamtuananhhatay

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Hệ thống | Do người dùng | Không | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Hệ thống | Giới hạn hệ thống | Không | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận theo hai cột nhãn:** 17 / 20 = 85%. Hai thành viên chịu trách nhiệm xác nhận việc gắn nhãn độc lập trước khi so.

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 6: Khách chọn sai mục từ đầu nên nguyên nhân gốc là **Do người dùng**; việc trợ lý không nhận ra nội dung lệch mục là chỗ cần cải thiện.
- Ca 13: Yêu cầu hoàn phí bảo hiểm nằm ngoài phạm vi trợ lý nên là **Giới hạn hệ thống**, dù lời trả lời chung chung cần được sửa.
- Ca 18: Số tiền hoàn đúng chính sách nhưng thiếu cách tính khiến khách hiểu sai, nên là **Ngữ cảnh**, không phải lỗi tính toán của hệ thống.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Đếm `input_validation_failed` với `reason=ma_don_sai` mỗi ngày; cảnh báo nếu vượt 2% yêu cầu | Nhận diện mã đơn sàn thương mại điện tử, tra sang mã vận đơn; nếu không tra được thì hướng dẫn khách nhập đúng mã | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ giữa thông báo `hoan_thanh_cong` và bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng 0 ca lệch | Chỉ báo hoàn thành sau khi sổ cái xác nhận; lỗi 503 sau 3 lần thì báo đang xử lý và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Đếm yêu cầu mở lại vì `khong_hieu_so_tien` trong các ca tính đúng, theo tuần; cảnh báo nếu vượt 1% | Tin nhắn ghi rõ phép tính hoàn tiền, ví dụ 30.000 đ × 50% = 15.000 đ | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Đếm `handoff_to_staff` với `reason=thieu_du_lieu` theo loại yêu cầu mỗi ngày; cảnh báo nếu vượt 5% | Giữ cách chuyển kèm tóm tắt; không đưa yêu cầu `quoc_te` vào phạm vi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn mỗi tuần với bảng giá hiện hành; cảnh báo nếu trên 1% đơn lệch | Xóa bộ nhớ đệm khi bảng giá đổi; ghi phiên bản bảng giá trong event có `trace_id` | Kế toán trưởng |
