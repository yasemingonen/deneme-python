# Find Harshad Numbers ? Pls search for Internet What is the meaning of Harshad Numbers.

number = input("Pls Write a Number")
toplam = 0
for i in number:
    toplam += int(i)
if int(number) % toplam == 0:
    print(True, f"- Numbers of {number} is Harshad")
else:
    print(False, f"- Numbers of {number} is not Harshad")
       

