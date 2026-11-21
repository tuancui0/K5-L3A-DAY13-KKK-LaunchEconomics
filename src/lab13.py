"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist

import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # đồng/tháng, chi phí cố định của trợ lý
YC_THANG = 45_000            # số yêu cầu hoàn phí mỗi tháng
PHAM_VI = ['noi_dia', 'hang_nang']
ICC = 0.02


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # dùng cho B1, B3
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhóm khi so hai tỉ lệ (D1)."""
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


# ---------- In các bảng ----------
def nhiem_vu_a(runs, reqs):
    kq = mo_hinh(runs, reqs)
    print('\n== A2 · Mô hình chi phí (toàn mẫu) ==')
    for ten, gia_tri in kq.items():
        print(f'{ten:14s} {gia_tri:>14,.1f}')
    print(f"cps / hóa đơn token+tool mỗi yêu cầu = {kq['cps'] / kq['hoa_don_moi_yc']:.1f} lần [simulated]")
    print(f"Tỷ trọng: làm lại {kq['lam_lai'] / kq['tong']:.1%}, xem lại {kq['xem_lai'] / kq['tong']:.1%}, "
          f"giờ nhân viên {(kq['lam_lai'] + kq['xem_lai']) / kq['tong']:.1%} [simulated]")
    he_thong = (kq['tong'] + BASELINE * (len(reqs) - kq['thanh_cong'])) / len(reqs)
    print(f'Chi phí cả hệ thống / yêu cầu: {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}× của {BASELINE:,} đ [simulated]')

    print('\n== A3 · Theo loại yêu cầu [simulated] ==')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        k = mo_hinh(runs, r)
        print(f"{loai:10s} n={len(r):4d}  thành công={k['thanh_cong'] / len(r):6.1%}  "
              f"lần chạy/yc={r['so_lan_chay'].mean():.2f}  cps={k['cps']:8,.0f} đ  "
              f"so với 12.000 đ={k['cps'] / BASELINE:.2f}×")
    print('Tỉ lệ ok theo lần thử (chạy lại có giúp không):')
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m['status'] == 'ok').astype(float)
    print(m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean').round(3).to_string())

    print('\n== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang [simulated] ==')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    kp = mo_hinh(runs, pv)
    viec_thang = YC_THANG * kp['thanh_cong'] / len(reqs)
    for ten, he in [('đầy đủ 45.000 yc/tháng', 1.0), ('một nửa khối lượng', 0.5)]:
        cd = CO_DINH_THANG / (viec_thang * he)
        print(f"{ten}: cố định {cd:,.0f} đ/việc → cps {kp['cps'] + cd:,.0f} đ = {(kp['cps'] + cd) / BASELINE:.2f}× "
              f"(cps phạm vi chưa cố định {kp['cps']:,.0f} đ, {viec_thang:,.0f} việc/tháng)")


def nhiem_vu_b(runs, reqs):
    goc = mo_hinh(runs, reqs)['cps']
    kich_ban = {
        'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi': dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi': dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
        'Lương tăng 25%': dict(luong_phut=2500),
        'Tối đa 2 lần chạy': dict(max_lan_chay=2),
        'Chỉ 1 lần chạy': dict(max_lan_chay=1),
    }
    print('\n== B1 · Độ nhạy [simulated] ==')
    print(f"{'Gốc (A2)':26s} {goc:8,.0f}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:26s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'\nB2 · Token ×2 + xem lại ×2: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%) [simulated]')

    print('\n== B3 · Giới hạn chạy lại, chi phí cả hệ thống [simulated] ==')
    for k in (1, 2, 3):
        kq = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - kq['thanh_cong']
        print(f"tối đa {k} lần: tổng trợ lý {kq['tong']:,.0f} đ  không thành công {khong_tc}  "
              f"cả hệ thống {kq['tong'] + BASELINE * khong_tc:,.0f} đ  cps {kq['cps']:,.0f} đ")

    print('\n== B4 · Xem lại 100% (noi_dia + hang_nang) [simulated] ==')
    r = reqs[reqs.loai.isin(PHAM_VI)]
    rr = runs[runs.request_id.isin(r.request_id)]
    co_ok = rr[rr.status == 'ok'].request_id.nunique()
    lam = r[r.ket_qua == 'lam_lai']
    tt = (rr['tokens_in'] / 1000 * GIA_VAO + rr['tokens_out'] / 1000 * GIA_RA).sum() + rr['tool_calls'].sum() * GIA_TOOL
    tc = int((r.ket_qua == 'thanh_cong').sum())
    phut_tb = reqs[reqs.ket_qua == 'lam_lai'].phut_lam_lai_simulated.mean()  # trung bình trên mọi ca lam_lai
    for ten, phut in [('9 phút làm lại (đề bài)', 9),
                      (f'{phut_tb:.1f} phút làm lại (dữ liệu, mọi ca lam_lai)', phut_tb)]:
        tong = co_ok * 5 * LUONG_PHUT + len(lam) * phut * LUONG_PHUT + tt
        hoa_von = (BASELINE * tc - len(lam) * phut * LUONG_PHUT - tt) / (co_ok * LUONG_PHUT)
        print(f'{ten}: {co_ok} yc xem lại, {len(lam)} ca làm lại, tổng {tong:,.0f} đ / {tc} việc → '
              f'{tong / tc:,.0f} đ = {tong / tc / BASELINE:.2f}× ; hòa vốn nếu xem lại ≤ {hoa_von:.1f} phút')


def nhiem_vu_d(reqs):
    from statsmodels.stats.proportion import proportion_effectsize
    from statsmodels.stats.power import NormalIndPower
    print('\n== D1 · Cỡ mẫu ==')
    n5, n6 = co_mau(0.70, 0.75), co_mau(0.70, 0.76)
    print(f'a) chia theo yêu cầu, chênh 5 điểm: {n5} / nhóm')
    de = 1 + (75 - 1) * ICC
    ng = math.ceil(n5 * de / 75)
    print(f'b) theo nhân viên m=75: DE={de:.2f}, n={math.ceil(n5 * de)} / nhóm → {ng} người/nhóm, tổng {2 * ng} > 40')
    print(f'c) 20 nhân viên/nhóm: tối đa {20 / ICC:.0f} < {n5}')
    print(f'd) 6 depot/nhóm: tối đa {6 / ICC:.0f}')
    m = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    print(f'e) chênh 6 điểm ({n6}/nhóm), 20 người/nhóm: m ≥ {m} yc/người '
          f'(DE={1 + (m - 1) * ICC:.2f}, hiệu dụng={20 * m / (1 + (m - 1) * ICC):.0f})')
    pw = NormalIndPower().power(effect_size=proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05, ratio=1.0)
    print(f'   nếu tác động thật chỉ 5 điểm, n={n6}/nhóm: power={pw:.2f}')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    print(f'\nmo_lai_trong_7_ngay: toàn mẫu {reqs.mo_lai_trong_7_ngay.mean():.2%}, phạm vi noi_dia+hang_nang {pv.mo_lai_trong_7_ngay.mean():.2%}')


def nhiem_vu_e(reqs):
    chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)).mean()
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo']).mean()
    an_toan = (reqs.mo_lai_trong_7_ngay == 1).mean()
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    print('\n== E1 · Chỉ số trong đợt chạy thử ==')
    print(f'Chính: {chinh:.2%} | Dùng (bỏ qua gợi ý): {bo_qua:.2%} ({len(xem)} yc được xem lại) | An toàn (mở lại 7 ngày): {an_toan:.2%}')
    print(f"Tỉ lệ làm lại trong phạm vi: {(pv.ket_qua == 'lam_lai').mean():.1%}")


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    nhiem_vu_a(runs, reqs)
    nhiem_vu_b(runs, reqs)
    nhiem_vu_d(reqs)
    nhiem_vu_e(reqs)
