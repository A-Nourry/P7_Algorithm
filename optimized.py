import csv


PRECISION_VALUE = 10  # adjust the precision of the result


def get_best_profit(max_expense=int, cost=int, profit=int, names=str):
    """dynamic solution to get the best combination of stocks

    Args:
        max_expense (int): maximum expense
        cost (int): cost of stock
        profit (int): profit of stock
        names (str): name of stock
    """
    n = len(profit)
    table = [[0 for x in range(max_expense + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(max_expense + 1):

            if i == 0 or j == 0:
                table[i][j] = 0

            elif cost[i - 1] <= j:
                table[i][j] = max(
                    profit[i - 1] + table[i - 1][j - cost[i - 1]], table[i - 1][j]
                )
            else:
                table[i][j] = table[i - 1][j]

    result = table[-1][-1]

    print("Bénéfice sur 2 ans : ", result / 100)
    print("liste des actions : ")

    # Print all stock names
    total_cost = []
    for i in range(n, 0, -1):
        if result <= 0:
            break

        if result == table[i - 1][max_expense]:
            continue

        else:
            print(names[i - 1])
            total_cost.append(cost[i - 1])

            result = result - profit[i - 1]
            max_expense = max_expense - cost[i - 1]

    print("Coût total : ", sum(total_cost) / PRECISION_VALUE)


if __name__ == "__main__":

    """import csv file"""
    file = open("data.csv")
    csvreader = csv.reader(file)
    next(csvreader, None)

    """append csv data to lists"""
    rows = []
    stock_name = []
    stock_costs = []
    stock_profits = []
    max_expense = 500 * PRECISION_VALUE  # maximal cost * 100

    for data in csvreader:
        rows.append(data)

    for row, i in zip(rows, range(len(rows))):
        if int(float(rows[i][1])) > 0 and int(float(rows[i][2]) > 0):
            stock_name.append(rows[i][0])
            stock_costs.append(float(rows[i][1]))
            stock_profits.append(
                round(float(rows[i][2]) * float(rows[i][1])) / PRECISION_VALUE
            )

    for cost, i in zip(stock_costs, range(len(stock_costs))):
        stock_costs[i] = stock_costs[i] * PRECISION_VALUE
        stock_costs[i] = int(stock_costs[i])

    for profit, i in zip(stock_profits, range(len(stock_profits))):
        stock_profits[i] = stock_profits[i] * PRECISION_VALUE
        stock_profits[i] = int(stock_profits[i])

    get_best_profit(max_expense, stock_costs, stock_profits, stock_name)
