line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

map = [line1, line2, line3]

print("Hiding Treasure! X mark the spot")

position = input()
abc = ['a', 'b','c']

letter_index = position[0].lower()

connect_letter_index = abc.index(letter_index)

number_index = int(position[1])-1

map[connect_letter_index][number_index] = "X"


print(f"{line1} \n {line2} \n {line3}")







