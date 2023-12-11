def calculate_flames(name1, name2):
    name1_list = list(name1.lower())
    name2_list = list(name2.lower())
    for letter in name1_list:
        if letter in name2_list:
            name2_list.remove(letter)
    count = len(name1_list) + len(name2_list)
    flames_list = ['Friendship', 'Love', 'Affection', 'Marriage', 'Enemy', 'Siblings']
    while len(flames_list) > 1:
        split_index = (count % len(flames_list)) - 1
        if split_index >= 0:
            right = flames_list[split_index + 1:]
            left = flames_list[:split_index]
            flames_list = right + left
        else:
            flames_list = flames_list[:len(flames_list) - 1]
    return flames_list[0]

name1 = input("Enter Your  name: ")
name2 = input("Enter second persons name: ")
result = calculate_flames(name1, name2)
print("Result: " + result)
