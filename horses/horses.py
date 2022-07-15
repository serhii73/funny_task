from itertools import islice


def get_top3(horses):
    def chunks(data, SIZE=5):
        it = iter(data)
        for i in range(0, len(data), SIZE):
            yield {k: data[k] for k in islice(it, SIZE)}

    def first_5_horses(horses):
        top_5 = []
        for i in chunks(horses):
            sorted_i = dict(sorted(i.items(), key=lambda item: item[1]))
            top_5.append(list(sorted_i)[-1])
        return top_5

    top_3 = []

    a, b, c, d, e = chunks(horses)
    top_5 = {i: horses.get(i) for i in first_5_horses(horses)}
    top_5 = dict(sorted(top_5.items(), key=lambda item: item[1]))

    best_name = max(top_5, key=top_5.get)
    top_3.append(best_name)

    last_ride = list(top_5)[2:4]

    for i in [a, b, c, d, e]:
        if best_name in i:
            sorted_i = dict(sorted(i.items(), key=lambda item: item[1]))
            last_ride.extend(list(sorted_i)[2:4])
        if list(top_5)[-2] in i:
            sorted_i = dict(sorted(i.items(), key=lambda item: item[1]))
            last_ride.append(list(sorted_i)[-2])

    last_ride = {i: horses.get(i) for i in last_ride}
    sorted_i = dict(sorted(last_ride.items(), key=lambda item: item[1]))
    top_3.extend(list(sorted_i)[3:][::-1])

    return top_3
