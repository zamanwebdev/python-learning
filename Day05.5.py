# 👉 1️⃣ 1 থেকে 10 পর্যন্ত print করো
for i in range(1,11):
    print(i)
# 👉 2️⃣ 1 থেকে 20 এর মধ্যে শুধু Even number print করো
for i in range(1, 11):
    if i % 2 == 0:
        print(i, "Even")
    else:
       pass
# 👉 3️⃣ User থেকে number নিয়ে তার multiplication table print করো
# User থেকে number নেওয়া
num = int(input("Enter a number: "))

print(f"\nMultiplication Table of {num}:\n")

# 1 থেকে 10 পর্যন্ত table
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
