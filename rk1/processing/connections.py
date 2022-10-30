def one_to_many(musics, orchectras):
    return [(mus.name, mus.duration, orch.name)
            for mus in musics
            for orch in orchectras
            if mus.orch_id == orch.id]


def many_to_many(musics, orchectras, orchMusic):
    return [(mus.name, mus.duration, orch.name)
            for oc in orchMusic
            for mus in musics
            for orch in orchectras
            if mus.id == oc.id_mus and orch.id == oc.id_orch]
