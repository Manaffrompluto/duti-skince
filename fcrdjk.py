s = "Chips"
p = 1
q = 15
a = True

print(f"Snack: {s}")
print(f"Price: ${p}")
print(f"Quantity left: {q}")
print(f"Availability: {a}")

print(type(s))
print(type(p))
print(type(q))
print(type(a))

t = p * q
print(f"Total value: ${t}")
print(f"Sale price: ${p - 00.25}")
print(f"Double stock: {q * 2}")

print(f"Is the price under $2? {p < 2}")
print(f"Is there more than 7 left in stock? {q > 7}")
print("Is the price exactly $1?", p == 1)

sh = "Chips" + " " + "Shop"
print(f"Shop name: {sh}")
print(f"Number of letters in shop name: {len(sh) - 1}")
print(f"First letter: {sh[0]}")

p1 = 1
p2 = 2
print(f"Due to oil prices rising (yes I guess its related to a snacks shop), we have increased our price from ${p1} to ${p2}.")

t = p1
p1 = p2
p2 = t
print(f"after {p1} is {p2}")