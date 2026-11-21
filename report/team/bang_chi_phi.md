# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
|---|---|
| Số lần chạy trung bình, tối đa 2 lần | (1 - (1 - 0,8)^2) / 0,8 = 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1 / 0,8 = 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | [(1 - 0,2^3) / 0,8] / (1 - 0,2^3) = 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
|---|---:|---|---|
| Token | 245.585 | logix_runs.csv | đo từ trace |
| Tool | 84.000 | logix_runs.csv | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | phut_xem_lai_simulated | simulated |
| Làm lại | 2.264.000 | phut_lam_lai_simulated | simulated |
| Tổng chi phí | 4.373.585 | cộng bốn khoản chi phí | có phần simulated |
| Số việc thành công | 978 | ket_qua == 'thanh_cong' | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | tổng chi phí / số việc thành công | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (token + tool) / 1.200 | đo từ trace |

- Đối chiếu tính tay: (245.585 + 84.000 + 1.780.000 + 2.264.000) / 978 = 4.472 đ/việc thành công [simulated]. Chi phí này gấp 4.472 / 274,7 = 16,3 lần "hoá đơn chia số yêu cầu".
- Làm lại là khoản lớn nhất: 2.264.000 / 4.373.585 × 100 = 51,8% tổng chi phí [simulated].

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? ...
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? ...

## A3 · Tách theo loại yêu cầu

Tất cả cột chi phí và so sánh có nhãn simulated.

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? `quoc_te` (1,88×, thành công 27,3%) [simulated]. Chạy lại không giúp: tỉ lệ ok theo lần thử là 30,0% → 11,4% → 2,2%, lỗi lặp lại trên cùng yêu cầu nên chỉ tốn thêm tiền. `doi_tac` sát ngưỡng (0,85×) và có điều khoản riêng nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

Chi phí cố định 40 triệu đ/tháng. Chi phí mỗi việc thành công của phạm vi chưa cộng cố định: 3.414 đ (900 việc thành công trong 982 yêu cầu của phạm vi). Mọi số dưới đây là simulated.

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận: cả hai mức đều dưới 0,5× của 12.000 đ [simulated]. Nhưng chi phí cố định mỗi việc tăng gấp đôi (1.185 → 2.370 đ) khi khối lượng giảm một nửa, nên hồ sơ phải ghi rõ con số đã cộng cố định ở khối lượng nào.

## B1 · Đổi từng yếu tố

Chi phí gốc (A2): 4.472 đ. Tất cả số dưới đây là simulated.

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tự kiểm tra: mỗi kịch bản "giảm một nửa" bằng đúng nửa mức tăng của kịch bản "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9).

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: 6.543 đ (+46,3%) [simulated], đúng bằng tổng hai tác động riêng (5,6% + 40,7%) vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%) [simulated]. Giá token chỉ +5,6%.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Tất cả là simulated.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ (rẻ nhất) | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ), không trùng với giới hạn 1 lần cho chi phí mỗi việc thấp nhất (4.111 đ). Tối ưu riêng chi phí mỗi việc thành công sẽ đẩy thêm 85 việc (319 − 234) sang nhân viên [simulated].

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang` (982 yêu cầu): 948 yêu cầu có ít nhất một lần chạy ok, mỗi yêu cầu xem lại 5 phút; 48 ca `lam_lai`; 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: 11.743 đ = 0,98× với 9 phút làm lại (đề bài); 12.415 đ = 1,03× nếu dùng 15,3 phút làm lại trung bình của dữ liệu [simulated]. Hoà vốn khi mỗi lần xem lại ≤ 5,1 phút (9 phút làm lại) hoặc ≤ 4,8 phút (15,3 phút).
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% thì trợ lý gần như không tiết kiệm được gì (tiền xem lại chiếm khoảng 90% chi phí), nên pilot phải học được tỉ lệ xem lại có thể giảm an toàn xuống mức nào và mỗi lần xem lại có ngắn hơn 5 phút được không [simulated].
