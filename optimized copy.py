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

    result = table[-1][-1]
    total_cost = []

    print("Bénéfice sur 2 ans : ", result)
    print("liste des actions : ")

    for i in range(n, 0, -1):
        if result <= 0:
            break

        if result == table[i - 1][max_expense]:
            continue

        else:
            total_cost.append(cost[i - 1])

            result = result - profit[i - 1]
            max_expense = max_expense - cost[i - 1]

    print("Coût total : ", sum(total_cost))


if __name__ == "__main__":

    """import csv file"""
    file = open("dataset1_Python+P7.csv")
    csvreader = csv.reader(file)

    """append csv data to lists"""
    rows = []
    stock_name = []
    stock_costs = [2, 3, 5, 7, 6]
    stock_profits = [5, 10, 16, 20, 17]
    max_expense = 10

    for i in range(len(stock_profits) + 1):
        print(stock_costs[i - 1])

    get_best_profit(max_expense, stock_costs, stock_profits, stock_name)
