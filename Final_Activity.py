def create_tuple(*values):
    return tuple(values)

def create_dict(*pairs):
    return dict(pairs)

def create_list(*values):
    return list(values)

t = ("apple", "banana", "cherry", "mansanas", "saging", "cher", "fruits")
l = ["loyd", "mark", "rick","sheesh", "Broo"]
d = {"brand": "Ford", "model": "Mustang", "year": 1964}

print("______________________________________________________________________\n")
print("                |         HELLO WELCOME           |                   ")
print("______________________________________________________________________\n")
print("""               1. Len 
               2. Max 
               3. Min 
               4. Tuple 
               5. List 
               6. Del
               7. Dict.clear 
               8. Copy
               9. Fromkeys 
               10. Get 
               11. Items 
               12.Pop 
               13. Popitem 
               14. Setdefault 
               15. Update
               16.  Values""")
print("______________________________________________________________________\n")
option = int(input("Enter an option number: "))
print("______________________________________________________________________\n")
option2 = input("Choose what list or tuple or dictionary will you choose? (t/l/d): ")
print("______________________________________________________________________\n")

if option2 == "t":
    obj = t
elif option2 == "l":
    obj = l
elif option2 == "d":
    obj = d
else:
    print("Invalid option")

if option == 1:
    print(len(obj))
elif option == 2:
    print(max(obj))
elif option == 3:
    print(min(obj))
elif option == 4:
    if option2 != "l":
        print(obj)
    else:
        print(obj)
elif option == 5:
    if option2 != "l":
        print(obj)
    else:
        print(obj)
elif option == 6:
    if option2 == "t":
        t = ("apple", "banana", "cherry", "mansanas", "saging", "cher", "fruits")
        indexs = int(input("Enter the index of the tuple to delete: "))
        print()
        if indexs >= len(t) or indexs < 0:
            print("Invalid index")
        else:
            t = t[:indexs] + t[indexs+1:]
            print("                |        RESULT           |                   \n")
            print(" Deleted element at index", indexs)
            print(  t)
    elif option2 == "l":
        l = ["loyd", "mark", "rick","sheesh", "Broo"]
        indexs = int(input("Enter the index of the list to delete: "))
        print()
        if indexs >= len(l) or indexs < 0:
            print("Invalid index")
        else:
            del l[indexs]
            print("                |        RESULT           |                   \n")
            print("Deleted element at index", indexs)
            print(l)
    elif option2 == "d":
        d = {"brand": "Ford", "model": "Mustang", "year": 1964}
        key = input("Enter the key of the dictionary to delete: ")# the keyy is the brand, model, and the year
        print()
        if key not in d:
            print("Invalid key")
        else:
            del d[key]
            print("                |        RESULT           |                   \n")
            print("Deleted key", key)
            print(d)

      #fix      

elif option == 7:
    d = {"brand": "Ford", "model": "Mustang", "year": 1964}
    if option2 == "d":
        choo = input("Do you want to clear? y/n: ")
        if choo == 'y':
            d.clear()
            print(d)
        elif choo == 'n':
            print(d)
        else:
            print("Invalid input")
elif option == 8:
    if option2 == "d":
        d = {"brand": "Ford", "model": "Mustang", "year": 1964}
        n = int(input("How many copies do you want? "))
        copies = []
        for i in range(n):
            copy_d = d.copy()
            copies.append(copy_d)
        print(copies)
#fix
    
elif option == 9:
    keys = input("Enter the keys separated by commas: ").split(",")
    values = input("Enter the values separated by commas: ").split(",")
    new_dict = dict.fromkeys(keys, values)
    print(new_dict)
    
    #fix
elif option == 10:
    print("                |        RESULT           |                   \n")
    print("     The keys brand, Ford, model, Mustang, year, 1964")
    key = input("Enter the key: ")
    print(obj.get(key))
    
    #fix
elif option == 11:
    print(obj.items())
    
    #fix
elif option == 12:
    if option2 == 'd':
        d = {"brand": "Ford", "model": "Mustang", "year": 1964}
        index = int(input("Enter the index of the element to remove: "))
        removed_element = list(d.keys())[index]
        del d[removed_element]
        print(f"Removed element: {removed_element}\n{d}")

#fix
    
    
elif option == 13:
    removed_item = obj.popitem()
    print(f"Removed item: {removed_item}\n{obj}")
    #fix
    
elif option == 14:
    key = input("Enter the key: ")
    value = input("Enter the value: ")
    obj.setdefault(key, value)
    print(obj)
    
    
elif option == 15:
    if option2 == "d":
        d = {"brand": "Ford", "model": "Mustang", "year": 1964}
        update_dict = input("Enter the dictionary to update (in the format key1:value1,key2:value2,...): ")
        update_dict = create_dict(*[pair.split(":") for pair in update_dict.split(",")])
        d.update(update_dict)
        print(d)


elif option == 16:
    print(list(obj.values()))
else:
    print("Invalid option")






