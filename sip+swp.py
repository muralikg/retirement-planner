returns = 15
inflation = 7
monthly_inflation_rate = (1+(inflation)/100) ** (1/12)
monthly_return_rate = (1+(returns)/100) ** (1/12)

current_age = 37
swp_age = 90
period = (90 - 37 ) * 12
monthly_withdrawal = 100000

sip_monthly = 200000
sip_step_up = 15
lumpsum = 3000000


def can_retire(monthly_expenses, months, corpus):
	for i in range(period):
		corpus -= monthly_expenses
		if corpus < 0:
			return False
		monthly_expenses *= monthly_inflation_rate
		corpus *= monthly_return_rate
	return True

i = 0
amount = lumpsum
while True:
	i += 1
	if i % 12 == 0:
		sip_monthly *= (1+sip_step_up/100)

	if can_retire(monthly_withdrawal, period - 1, amount):
		print(f"Year {int(i/12)} Month {i%12} => Amount {amount}. Monthly SWP {monthly_withdrawal}")
		break
	monthly_withdrawal *= monthly_inflation_rate
	amount = (amount + sip_monthly) * monthly_return_rate
