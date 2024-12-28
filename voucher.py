vouchers = {
    "DISCOUNT10": {"discount": 10, "min_order": 100}, 
    "FREESHIP20": {"discount": 20, "min_order": 200},
}

def apply_voucher(voucher_code, order_total):
 
    if voucher_code in vouchers:
        voucher = vouchers[voucher_code]
        if order_total >= voucher["min_order"]:
            discount = voucher["discount"]
            if discount < 1:  
                discount_amount = order_total * discount
            else: 
                discount_amount = discount
            order_total -= discount_amount
            print(f"Áp dụng thành công! Giảm giá: {discount_amount:.2f}")
        else:
            print(f"Đơn hàng không đủ điều kiện. Tối thiểu {voucher['min_order']}.")
    else:
        print("Mã voucher không hợp lệ.")
    return order_total

order_total = 250
voucher_code = input("Nhập mã voucher: ").strip().upper()
final_total = apply_voucher(voucher_code, order_total)
print(f"Tổng tiền sau khi áp dụng voucher: {final_total:.2f}")