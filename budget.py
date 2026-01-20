import typer
import csv
from tabulate import tabulate

app = typer.Typer()


''' 
add - to add an item to the budget, should have amount
    should assign a unique value to each item
view - to view budget in a table, with 
done - to check off an item from the list
mod - to modify a budget amount using id



'''
fieldnames = ["Item", "Amount"]
filename = "list.csv"


@app.command()
def add(item: str):
    Item = {}
    Item["Item"] = item
    Item["Amount"] = input("Amount: ")

    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(Item)
    print("Item added succefully")
    table()


def table():
    tab = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for line in reader:
            tab.append(line)
        print(tabulate(tab, tablefmt="grid"))


@app.command()
def view():
    table()


@app.command()
def done():
    with open("list.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()


if __name__ == "__main__":
    app()
