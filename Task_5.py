revenue = int(input('Enter your current revenue: '))
employees = int(input('Enter number of employees: '))
costs = int(input('Enter your current costs: '))
profit = revenue - costs
profit_per_employee = employees / profit
profitability = profit / revenue
if profit > 0:
    print('Your current profit is {}, your profitability is {}, your profit per employee is {}'.format(profit,
                                                                                                       profitability,
                                                                                                       profit_per_employee))


else:
    print('Your loss is {}'.format(profit))