

class BusAppError(Exception):
    pass


class BusNotFoundError(BusAppError):
    pass


class InvalidBusNumberError(BusAppError):
    pass


class InvalidCapacityError(BusAppError):
    pass


class InvalidYearError(BusAppError):
    pass


class InvalidBusTypeError(BusAppError):
    pass


class SaveError(BusAppError):
    pass


class LoadError(BusAppError):
    pass