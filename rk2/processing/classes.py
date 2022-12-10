class music:
    """музыкальное произведение"""

    def __init__(self, id, name, duration, orch_id):
        self.id = id
        self.name = name
        self.duration = duration
        self.orch_id = orch_id

class orchestra:
    """оркестр"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class orchMusic:
    def __init__(self, id_mus, id_orch):
        self.id_mus = id_mus
        self.id_orch = id_orch
