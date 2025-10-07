import pandas as pd
from pandas import DataFrame

class LoanSimulations:
    def __init__(self, maturity, interest_rate, spread, notional):
        self.maturity = maturity
        self.interest_rate = interest_rate
        self.spread = spread
        self.notional = notional

    def calc_monthly_payment(self):
        ''' Calculate the monthly payment using the amortization formula '''

        monthly_rate = (self.interest_rate + self.spread) / 12 / 100
        num_payments = self.maturity * 12
        if monthly_rate == 0:
            return self.notional / num_payments
        payment = (self.notional * monthly_rate) / (1 - (1 + monthly_rate) ** -num_payments)
        return payment
    
    def generate_payment_schedule(self):
        ''' Generate the payment schedule without early repayments '''

        monthly_payment = self.calc_monthly_payment()
        balance = self.notional
        schedule = []

        for month in range(1, self.maturity * 12 + 1):
            interest = balance * (self.interest_rate + self.spread) / 12 / 100
            principal = monthly_payment - interest
            balance -= principal
            schedule.append({
                'Month': month,
                'Payment': monthly_payment,
                'Principal': principal,
                'Interest': interest,
                'Balance': max(balance, 0)
            })
        
        return pd.DataFrame(schedule)
    
    def generate_monthly_early_repayment(self, monthly_early_repayment_amount):
        ''' Generate the payment schedule with early repayments '''

        monthly_payment = self.calc_monthly_payment()
        balance = self.notional
        early_schedule = []
        net_early_repayment_amount = monthly_early_repayment_amount * (1 - 0.05)

        for month in range(1, self.maturity * 12 + 1):
            interest = balance * (self.interest_rate + self.spread) / 12 / 100
            principal = monthly_payment - interest
            balance -= principal
            
            # Apply early repayment
            if net_early_repayment_amount > 0:
                early_repayment = min(net_early_repayment_amount, balance)
                balance -= early_repayment
                principal += early_repayment
            
            early_schedule.append({
                'Month': month,
                'Payment': monthly_payment + (early_repayment if net_early_repayment_amount > 0 else 0),
                'Principal': principal,
                'Interest': interest,
                'Balance': max(balance, 0)
            })
            
            if balance <= 0:
                break
        
        return pd.DataFrame(early_schedule)
    
    def get_time_decrease_by_early_repayment(self, schedule: DataFrame, early_schedule: DataFrame):
        ''' Calculate the time decrease in months due to early repayments '''
        
        decrease = len(schedule) - len(early_schedule)

        return decrease


# Example usage:
if __name__ == "__main__":
    loan = LoanSimulations(maturity=27, interest_rate=2.0, spread=0.75, notional=162000)
    print("Monthly Payment:", loan.calc_monthly_payment())
    schedule = loan.generate_payment_schedule()
    print("Payment Schedule:\n", schedule)
    repayment = 200
    early_schedule = loan.generate_monthly_early_repayment(repayment)
    print("Early Repayment Schedule:\n", early_schedule)
    decrease = loan.get_time_decrease_by_early_repayment(schedule, early_schedule)
    print(f'Months decrease by paying {repayment}€ monthly: {decrease} (equivelent to {round(decrease/12,2)} years)')