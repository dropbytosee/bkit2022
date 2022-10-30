def task1(one_to_many):
    return [el for el in one_to_many if el[0].endswith('ов')]


def task2(one_to_many):
    orch = []
    duration = []
    for el in one_to_many:
        if el[2] not in orch:
            orch.append(el[2])
            duration.append((el[1], 1))
        else:
            idx = orch.index(el[2])
            duration[idx] = ((duration[idx][0] + el[1]) / (duration[idx][1] + 1), duration[idx][1] + 1)
    salary = [i[0] for i in duration]
    return sorted(list(zip(orch, duration)), key=lambda p: p[1], reverse=True)


def task3(many_to_many):
    orch_R = []
    mus_orch_R = []
    for el in many_to_many:
        if el[2].startswith('Р'):
            if el[2] not in orch_R:
                orch_R.append(el[2])
                mus_orch_R.append((el[0],))
            else:
                mus_orch_R[orch_R.index(el[2])] += (el[0],)
    return list(zip(orch_R, mus_orch_R))
