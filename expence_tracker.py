import json
def load_expenses():
    try :
        with open('expenses.json','r') as file:
             return json.load(file)
    except (FileNotFoundError,json.JSONDecodeError):

        print("Error: The file 'expenses.json' was not found.")
        return []
def save_expenses(expenses):
    try :
        with open('expenses.json','w') as json_file:
         json.dump(expenses, json_file, indent=4)
    except IOError as e:
        print(f"Error saving file: {e}")




def menu():
    print("\n\t\t1.Add Expenses")
    print("\t\t2.View Expenses ")
    print("\t\t3.View Total")
    print("\t\t4.Exit")

def get_options(options):
    match options:
        case 1:
            return "\n\n\tAdding expense"
        case 2:
            return "\n\n\tViewing expense"
        case 3:
            return " \n\n\tViewing Total"
        case 4:
            return "\n\n\tExiting Expense Tracker"
        case _:
            return "\n\n\tEnter a valid choice!"

def main():
    print("\n\n\t\tWelcome to Expense Tracker.")
    print("\n\t\tYour one stop budgeting solution.")
    expenses = [] 
    expenses = load_expenses()
    while True :
        try: 
         menu()
         choice= int(input("\n\tChoose an option : "))
         print(get_options(choice))
         if choice ==1:
            amount = float(input("Amount : "))
            category = input("Category : ")
            descriptions = input("Descriptions : ")
            expense = {
                "Amount" : amount,
                "Category" : category,
                "Descriptions" : descriptions
            }
            expenses.append(expense)
            save_expenses(expenses)

         elif choice == 2:
             for expense in expenses:
                 print(f"\n\tAmount : {expense['Amount']}")
                 print(f"\tCategory :{expense['Category']}")    
                 print(f"\tDescriptions :{expense['Descriptions']}")   
                 
                 
         elif choice == 3 :
                total = 0
                for expense in expenses:
                    total+=expense["Amount"]
                print(f"\t\t = {total}")
            
         elif choice ==4:
             break
        except ValueError:
            print("Enter a number . No alphabets allowed.")

if __name__=="__main__":
    main()