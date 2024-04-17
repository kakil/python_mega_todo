def get_average():
    with open('files/data.txt', 'r') as file:
        temperatures = file.readlines()

        temp_values = []
        for temp_value in temperatures:
            temp_value = temp_value.strip('\n')
            if temp_value.isdigit():
                temp_values.append(int(temp_value))

    total = 0
    for value in temp_values:
        total = total + value

    average = total / len(temp_values)
    print(f"Average is: {average}")



get_average()