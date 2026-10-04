# Base exception class for all GAME RELATED Errors.
class MidNightProtocolException(Exception):
    pass

class TimeExpiredError(MidNightProtocolException):
    def __init__(self, message = "⏰ Action failed: The trail has gone cold. You have run out of time."):
        self.message = message
        super().__init__(self.message)


# raised when a player tries to enter a restricted area without the required item.
class LocationLockedError(MidNightProtocolException):
    def __init__(self, location_name, message = None):
        self.location_name = location_name

        if message is None:
            self.message = f"🔒 Access Denied: {location_name} is locked. You need specific access clearance."
        else:
            self.message = message

        super().__init__(self.message)

# Raised when the detective makes too many false accusations and loses the case.
class CredibilityRuinedError(MidNightProtocolException):
    def __init__(self, message =  "💥 Disgraced: Your professional credibility hit 0%. The department pulled you off the case."):
        self.message = message
        super().__init__(self.message)
