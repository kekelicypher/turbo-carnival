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


@app.command()
def add(item: str):
    Item = {}
    Item["Item"] = input("Item: ")
    Item["Amount"] = input("Amount: ")

    with open("list.csv", "a") as file:
        fieldnames = ["Item", "Amount"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writerow(Item)
    print("Item added succefully")
    print(tabulate(Item, tablefmt="grid"))

# def table():
#     tab = []
#     with open(list) as file:
#         reader = csv.DictReader(file)


app.command()


def view():
    ...


if __name__ == "__main__":
    app()
