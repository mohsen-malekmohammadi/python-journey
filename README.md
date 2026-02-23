# Function to calculate net income after tax for UAE projects (5% VAT)
def calculate_net_income(gross_amount, tax_rate=5):
    """
    This function calculates the net income after deducting tax.
    Default tax rate is 5% (UAE standard).
    """
    tax_amount = (gross_amount * tax_rate) / 100
    net_income = gross_amount - tax_amount
    return net_income

# --- Testing the function ---
project_price = 5000  # Price in AED
final_receive = calculate_net_income(project_price)

print(f"Project Gross: {project_price} AED")
print(f"Net Income after 5% Tax: {final_receive} AED")
