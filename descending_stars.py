rows = 7

for row in range(rows):
    star_row = ''
    for column in range(stars):
        star_row += '*'
    print(star_row)
    stars -= 1