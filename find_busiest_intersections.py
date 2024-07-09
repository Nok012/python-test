def find_busiest_intersections(data):
       
    if len(data) == 0:
        return []

    highest_number_of_vehicles = []
    results = []

    for v in data.items():
        highest_number_of_vehicles.append(v[1])

    max_value = max(highest_number_of_vehicles)


    for v in data.items():
        if v[1] == max_value:
            results.append(v[0])

    return results