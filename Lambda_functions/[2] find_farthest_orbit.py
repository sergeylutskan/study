import math

def find_farthest_orbit(list_of_orbits):
    orbits = [math.pi*orbit[0]*orbit[1] for orbit in list_of_orbits if orbit[0] != orbit[1]]
    big_orbit = [(orbit[0],orbit[1]) for orbit in list_of_orbits if math.pi*orbit[0]*orbit[1] == max(orbits)]
    return big_orbit[0]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))

