class ValidationError(Exception):
    # problems that user could fix by changing configuration
    pass


class InternalError(Exception):
    # problems that user _can not_ fix by changing configuration and shouldn't happen
    pass
