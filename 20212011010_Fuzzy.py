def speed(car):
    degree = {}
    if car < 0 or car > 30:
        degree["high"] = 0
        degree["low"] = 0
    elif car <= 10:
        degree["low"] = 1
        degree["high"] = 0
    elif 10 < car < 20:
        degree["low"] = (20 - car) / (20 - 10)
        degree["high"] = (car - 10) / (20 - 10)
    elif 20 <= car <= 30:
        degree["low"] = 0
        degree["high"] = 1
    return degree

def relative_speed(car):
    degree = {}
    if car < 0 or car > 100:
        degree["low"] = 0
        degree["high"] = 0
    elif car <= 40:
        degree["low"] = 1
        degree["high"] = 0
    elif 40 < car < 60:
        degree["low"] = (60 - car) / (60 - 40)
        degree["high"] = (car - 40) / (60 - 40)
    elif 60 <= car <= 100:
        degree["low"] = 0
        degree["high"] = 1
    return degree

# Input values
relative_speed_input, speed_input = 75, 15

# Fuzzy degree calculations
r1 = relative_speed(relative_speed_input)
s1 = speed(speed_input)

print("Relative Speed Degrees:", r1)
print("Speed Degrees:", s1)

# Fuzzy rule evaluations
rule1 = max(r1['low'], s1['high'])
rule2 = r1['high']
rule3 = min(r1['low'], s1['high'])
rule4 = min(r1['low'], s1['low'])

# Defuzzification process
i = 10
COG = 0
down = 0
while i <= 100:
    if i <= 40:
        COG += i * rule1
        down += rule1
    elif 40 < i <= 60:
        COG += i * rule3
        down += rule3
    elif i > 60:
        COG += i * rule2
        down += rule2
    i += 10

# Final defuzzified output
if down != 0:
    print("Defuzzified Output:", COG / down)
else:
    print("No valid defuzzification due to zero denominator.")