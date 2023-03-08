def equal(a,b):
    if a == b :
        print("Two Numbers are Equal")
    else:
        print("They are not equal")
x= int(input("Enter a number"))
y= int(input("Enter a number"))

print(equal(x,y))

def sums(a,b):
    sums= a + b
    if sums > 10:
        print("Greater than 10")
    elif sums < 10 :
        print("Less than 10")
    elif sums == 10:
        print("Equal to 10")

print(sums(x,y))

def five(l):
    if 5 in l:
        return l

lists= [1 ,2 ,3 ,4 ,4 ,5]
print(five(lists))
def leap(z):
    if z%100 == 0 and z%400 == 0:
        return True
    elif z%4 == 0 :
        return True
    else:
        return False


c= int(input("Enter a year"))
print(leap(c))

def check_task_completion(task, items, debuffs):
    task_items = {
        'Climb a mountain': ['rope', 'coat', 'first aid kit'],
        'Cook a meal': ['pan', 'groceries'],
        'Write a book': ['pen', 'paper', 'idea']
    }

    # Check if all required items are in the item list
    if all(item in items for item in task_items[task]):
        # Check if there are any status debuffs
        if not any(debuff in debuffs for debuff in ['slow', 'confusion']):
            print(f"Task '{task}' completed successfully!")
            return True
        else:
            print(f"Cannot complete task '{task}' due to status debuff.")
            return False
    else:
        print(f"Cannot complete task '{task}' due to missing items.")
        return False


items = ['pan', 'paper', 'idea', 'rope', 'groceries']
debuffs = ['slow']

# Check task 1: Climb a mountain
check_task_completion('Climb a mountain', items, debuffs)

# Check task 2: Cook a meal
check_task_completion('Cook a meal', items, debuffs)

# Check task 3: Write a book
check_task_completion('Write a book', items, debuffs)


#Done BY Mohammed Adnan Khan






