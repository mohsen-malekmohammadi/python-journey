# تابع تبدیل درآمد دلاری/درهمی به تومان با نرخ روز
def convert_to_toman(amount, exchange_rate):
    """
    این تابع مبلغ ارزی را می‌گیرد و به تومان تبدیل می‌کند.
    """
    result = amount * exchange_rate
    return result

# تابع محاسبه سهم فریلنسر بعد از کسر کارمزد سایت (مثلاً پونیشا یا فریلنسر)
def calculate_pure_profit(total_project_price, fee_percent=10):
    fee_amount = (total_project_price * fee_percent) / 100
    profit = total_project_price - fee_amount
    return profit

# --- تست برای یک پروژه داخلی ---
project_toman = 10000000  # ۱۰ میلیون تومان
final_money = calculate_pure_profit(project_toman, 15) # با کسر ۱۵٪ کارمزد

print(f"مبلغ پروژه: {project_toman} تومان")
print(f"سودی که به دستت می‌رسه: {final_money} تومان")
