import csv


def get_best_profit(max_expense, cost, profit, names):
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

    result = table[n][max_expense]
    total_cost = []

    print("Bénéfice sur 2 ans : ", result / 100)
    print("liste des actions : ")

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

    print("Coût total : ", sum(total_cost))


if __name__ == "__main__":

    """import csv file"""
    file = open("data.csv")
    csvreader = csv.reader(file)

    """append csv data to lists"""
    rows = []
    stock_name = []
    stock_costs = []
    stock_profits = []
    max_expense = 500

    for data in csvreader:
        rows.append(data)

    for row, i in zip(rows, range(len(rows))):
        if int(float(rows[i][1])) > 0 and int(float(rows[i][2]) > 0):
            stock_name.append(rows[i][0])
            stock_costs.append(int(float(rows[i][1])))
            stock_profits.append(round(float(rows[i][2]) * float(rows[i][1])))

    get_best_profit(max_expense, stock_costs, stock_profits, stock_name)