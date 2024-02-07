# 
# Todo App
# 
# Masivi https://mape.gov.lv/catalog/materials/6501426F-B6EC-44B3-8B93-DC553DAE8886/view?preview=7A90D16F-0A8A-4840-A2E3-5EA4F6D4E194
# Lists https://www.w3schools.com/python/python_lists.asp


def add(list):
  additem = input("What do you want to add to list?(one item)")
  list.append(additem)
pass


def remove(list):
  int(list = [ ])
  index = int(input("What you want to remove?(write the number of item)\n"))
  index = index + 1
  int(index)
  list.pop(index)
pass


def clear(list):
  list.clear()
pass


def print_list(list):
  print(list)
pass


def show(list):
  int(list = [ ])
  print(list)
pass





list = [ ]
print("List is empty now, what you want to do?")
while True:
  choice = int(input("1. Add\n2. Remove\n3. Clear\n4. Print list\n5. Show item by index"))
  if choice == 1:
    add(list)
    print(list)
  # https://www.w3schools.com/python/python_lists_add.asp


  elif choice == 2:
    remove(list)
    print_list(list)
  # https://www.w3schools.com/python/python_lists_remove.asp


  elif choice == 3:
    clear(list)
    print_list(list)
  # https://www.w3schools.com/python/python_lists_remove.asp
    

  elif choice == 4:
    print_list(list)
  # https://www.w3schools.com/python/python_lists_loop.asp

  elif choice == 5:
    show(list)


  else:
    print("Invalid input")
