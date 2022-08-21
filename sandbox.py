signs = {1: 'Speed Limit (50 km/h)', 2: 'Speed Limit (90 km/H)', 3: 'Stop', 4: 'Pedestrian Crosing',
                   5: 'Minimum Speed Limit (60 km/h)'}

def check_sign(code):
    return signs.get(code)

a = check_sign(2)
print(a)
