import math

#1
r = 5
volume = (4/3) * math.pi * r**3
print(f"1. Volume of sphere: {volume:.2f}")

#2
cover_price = 24.95
discount = 0.40
wholesale_price = cover_price * (1 - discount)
shipping = 3.00 + (59 * 0.75)  
total_cost = (60 * wholesale_price) + shipping
print(f"2. Total wholesale cost for 60 copies: ${total_cost:.2f}")

#3
start_hours = 6
start_minutes = 52


easy_pace = 8 + 15/60      
tempo_pace = 7 + 12/60     

total_minutes = (1 * easy_pace) + (3 * tempo_pace) + (1 * easy_pace)

end_minutes = start_minutes + total_minutes
end_hours = start_hours + int(end_minutes // 60)
end_minutes = int(end_minutes % 60)

print(f"3. Home by: {end_hours}:{end_minutes:02d} am")