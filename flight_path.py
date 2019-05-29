"""Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller."""


def flight_path(l, s):
    out_list = [s]
    while len(l) > 0:
        next_dest = False
        #print("outlist: ", out_list)
        #print("l: ", l)
        pot_next = []
        for i in l:
            if i[0] == s:
                next_dest = True
                pot_next.append(i)
        if next_dest:
            #print(pot_next)
            to_rmv = find_min(pot_next)
            #print("to_rmv: ", to_rmv)
            l.remove(to_rmv)
            out_list.append(to_rmv[1])
            s = to_rmv[1]
        if not next_dest:
            return None
    return out_list


def find_min(l):
    min_dest = 'ZZZZZZZZ'
    min_value = None
    for i in l:
        if i[1] < min_dest:
            min_dest = i[1]
            min_value = i
    return min_value


if __name__ == "__main__":
    print("Test 1: ",  flight_path([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], 'YUL'))
    print("Test 2: ",  flight_path([('SFO', 'COM'), ('COM', 'YYZ')], 'COM'))
    print("Test 3: ", flight_path([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], 'A'))