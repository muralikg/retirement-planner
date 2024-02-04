returns = 15
inflation = 8


target = 12500000
initial = 6000000
sip_monthly = 350000

# percentages %
sip_step_up = 15


monthly_rate = (1+(returns - inflation)/100) ** (1/12)

amount = initial
i = 0
while True:
	i += 1
	if i % 12 == 0:
		sip_monthly *= (1+sip_step_up/100)
		target *= (1+inflation/100)
	amount = (amount + sip_monthly) * monthly_rate
	print(f"Year {int(i/12)} Month {i%12} => Amount {amount}")
	if amount >= target:
		break

print(amount)
