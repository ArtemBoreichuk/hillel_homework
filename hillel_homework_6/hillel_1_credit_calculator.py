def credit_calculator(loan_amount, period):
    monthly_payments = []
    remaining_balance = loan_amount
    for month in range(1, period * 12 + 1):
        if month <= 24:
            interest_rate = 0.02
        else:
            interest_rate = 0.04
        interest = remaining_balance * interest_rate
        monthly_payment = (loan_amount / (period * 12)) + interest
        monthly_payments.append((month, monthly_payment, interest))
        remaining_balance -= (monthly_payment - interest)
    return monthly_payments
loan_amount = float(input("Cума кредиту: "))
period = int(input("Введіть період (в роках): "))
payments = credit_calculator(loan_amount, period)
for payment in payments:
    print(f"Номер місяця: {payment[0]}  |  "
          f"Сума виплати за місяць: {payment[1]:.2f}  |  "
          f"Кількість процентів нараховано за місяць : {payment[2]:.2f}")
