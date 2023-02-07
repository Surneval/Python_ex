# greedy algorythm - to choose local optimal decision several times so it's gonna be global optimal decision
# you have several stations each covering some states. you have to cover all the states and
# to use the smallest ammount of stations

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations ['ktwo'] = set(['wa', 'id', 'mt'])
stations [ 'kthree'] = set(['or', 'nv', 'ca'])
stations ['kfour'] = set(['nv', 'ut'])
stations ['kfive'] = set(['ca', 'az'])

final_stations  = set()

while states_needed:
    best_station = None
    states_covered = set()
    for station, state in stations.items():
        covered  = states_needed & state
        if len(covered) > len(states_covered):
            states_covered = covered
            best_station = station
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)