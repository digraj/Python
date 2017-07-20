
class Duration:

    def __init__(self, weeks, days, hours):
        if not isinstance(weeks, int) or not isinstance(days, int) or not isinstance(hours, int):
            raise TypeError("This class only accepts integers.")
        if weeks < 0 or days < 0 or hours < 0:
            raise ValueError("Values cannot be negative.")

        if hours > 24:
            hours_left = hours // 24
            days = days + hours_left
            hours = hours % 24

        if days > 7:
            days_left = days // 7
            weeks = weeks + days_left
            days = days % 7

        self.weeks = weeks
        self.days = days
        self.hours = hours

    def __str__(self):
        my_str = "{:02d}W {:01d}D {:02d}H".format(self.weeks, self.days, self.hours)
        return my_str

    def getTotalHours(self):
        total = self.weeks * (7 * 24) + self.days * 24 + self.hours
        return total

    def __add__(self, other):
        if not isinstance(self, Duration) or not isinstance(other, Duration):
            raise TypeError("Duration is expected")
        hours = self.hours + other.hours
        days = self.days + other.days
        weeks = self.weeks + other.weeks
        newDuration = Duration(weeks, days, hours)
        return newDuration

    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Integer is expected")
        if other < 0:
            raise ValueError("Scaling factor must be greater than 0")

        hours = self.hours * other
        days = self.days * other
        weeks = self.weeks * other

        newDuration = Duration(weeks, days, hours)
        return newDuration

    def __rmul__(self, other):
        if not isinstance(other, int):
            raise TypeError("Integer is expected")
        if other < 0:
            raise ValueError("Scaling factor must be greater than 0")

        hours = self.hours * other
        days = self.days * other
        weeks = self.weeks * other

        newDuration = Duration(weeks, days, hours)
        return newDuration

if __name__ == "__main__":
    x = Duration(weeks=2, days=15, hours=49)
    y = Duration(weeks=5, days=11, hours=56)
    print(x)
    print(x.getTotalHours())
    print(x+y)
    print(x*5)
    print(5*x)
