
class Parker(object):
    def __init__(self):
        pass

    def park(self):
        pass

    def unpark(self):
        pass


class PrakingSpace(object):
    def __init__(self, booked, total):
        pass

    def park_car(self):
        raise NotImplementedError

    def unparked_car(self):
        raise NotImplementedError


class ParkingLot(object):
    def __init__(self):
        pass

    def take_place(self):
        pass

    def vacate_pace(self):
        pass