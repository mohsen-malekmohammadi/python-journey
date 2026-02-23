# تابع محاسبه کارمزد (همان منطق قبلی)
def calculate_profit(amount):
    if amount > 10000000:
        rate = 7
    else:
        rate = 10
    
    fee = (amount * rate) / 100
    profit = amount - fee
    return profit, rate

# --- بخش تعاملی برنامه ---
print("سلام محسن! به ماشین‌حساب فریلنسری خوش آمدی.")

# گرفتن مبلغ از کاربر (تبدیل متن به عدد اعشاری با float)
user_amount = float(input("لطفاً مبلغ پروژه را به تومان وارد کن: "))

# صدا زدن تابع و گرفتن خروجی‌ها
final_profit, final_rate = calculate_profit(user_amount)

print("-" * 30)
print(f"درصد کارمزد برای شما: {final_rate}%")
print(f"سود خالص شما: {final_profit} تومان")
