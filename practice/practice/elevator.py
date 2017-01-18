UP_DIR = "UP"
DOWN_DIR = "DOWN"
HALT_DIR = "HALT"


class RequestQueue(object):
    def __init__(self, pick_up_floor_id, dest_floor_id):
        self._pick_up_floor_id = pick_up_floor_id
        self._dest_floor_id = dest_floor_id


class ElevatorButton(object):
    def __init__(self, start_floor_id, end_floor_id):
        self._start_floor_id = start_floor_id
        self._dest_floor_id = end_floor_id

class FloorButton(object):
    def __init__(self):
        pass


class Elevator(object):
    def __init__(self, direction, start_floor_id, end_floor_id, request_queue):
        self._dir = direction
        self._start_floor_id = start_floor_id
        self._end_floor_id = end_floor_id
        self._request_queue = request_queue


class ElevatorSystem(object):
    def __init__(self):
        pass