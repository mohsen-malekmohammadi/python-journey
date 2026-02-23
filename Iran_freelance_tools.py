# تابع محاسبه هوشمند کارمزد برای ایرانی جماعت
def calculate_smart_fee(total_price):
    """
    اگر پروژه بالای ۱۰ میلیون باشد: ۷٪ کارمزد
    اگر پروژه زیر ۱۰ میلیون باشد: ۱۰٪ کارمزد
    """
    if total_price > 10000000:
        fee_percent = 7
    else:
        fee_percent = 10
        
    fee_amount = (total_price * fee_percent) / 100
    profit = total_price - fee_amount
    return profit, fee_percent

# --- تست برنامه با دو عدد متفاوت ---
project_1 = 15000000  # ۱۵ میلیون تومان
project_2 = 5000000   # ۵ میلیون تومان

result1, rate1 = calculate_smart_fee(project_1)
result2, rate2 = calculate_smart_fee(project_2)

print(f"پروژه بزرگ: {project_1} تومان | کارمزد: {rate1}% | سود نهایی: {result1}")
print(f"پروژه کوچک: {project_2} تومان | کارمزد: {rate2}% | سود نهایی: {result2}")
