import csv
import itertools


"""import csv file"""
file = open("data.csv")
csvreader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC)

MAX_EXPENSE = 500
rows = []
selected_stocks = []
benefits_added = []
best_profit = ["", 0.0, 0.0]

"""append data to rows list"""
for row in csvreader:
    rows.append(row)

for profit in rows:
    profit[2] = profit[1] * profit[2] / 100

"""generating every possible stocks combinations"""
combination_of_stocks = list(
    itertools.chain(*[itertools.combinations(rows, i + 1) for i in range(len(rows))])
)

"""select every combinations that cost less than MAX_EXPENSE"""
for combinations, i in zip(combination_of_stocks, range(len(combination_of_stocks))):
    S = sum(x[1] for x in combinations)
    if S <= MAX_EXPENSE:
        selected_stocks.append(combination_of_stocks[i])

"""get the sum of every benefits of every selected stock combinations"""
for stocks in selected_stocks:
    benefits_added.append(
        (
            [i[0] for i in stocks],
            sum([i[1] for i in stocks]),
            sum([i[2] for i in stocks]),
        )
    )

"""picks the combination that yields the most profit"""
for benefits, i in zip(benefits_added, range(len(benefits_added))):
    if benefits[2] > best_profit[2]:
        best_profit = benefits_added[i]

print("Liste des actions : ", best_profit[0])
print("coût total : ", best_profit[1])
print("Bénéfice : ", best_profit[2])
