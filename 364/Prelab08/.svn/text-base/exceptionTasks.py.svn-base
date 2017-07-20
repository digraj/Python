from pprint import pprint as pp
from prelab08addon import performProcessing

class PointND:
    def __init__(self, *args):
        self.t = args
        self.n = len(self.t)
        for item in self.t:
            if not isinstance(item, float):
                raise ValueError("Cannot instantiate an object with non-float values.")

    def __str__(self):
        my_str = "("
        for item in self.t[:-1]:
            if item < 0.0:
                temp = "{0:.5s}".format(str(item))
            else:
                temp = "{0:.4s}".format(str(item))
            my_str = my_str + temp + ", "
        if self.t[-1] < 0.0:
            temp = "{0:.5s}".format(str(self.t[-1]))
        else:
            temp = "{0:.4s}".format(str(self.t[-1]))
        my_str = my_str + temp + ")"
        return my_str

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self, other):
        total = 0;

        if isinstance(other, PointND):
            my_other = other.t
        else:
            my_other = other

        try:
            if len(my_other) == len(self.t):
                pass
            else:
                raise ValueError("Cannot operate on points with different cardinalities.")
        except ValueError:
            return "ERROR: Cardinality error."

        for i in range(0, self.n):
            distance = (self.t[i] - my_other[i]) ** 2
            total = total + distance
        total = total ** 0.5

        return (total)

    def nearestPoint(self, points):
        if points == []:
            raise ValueError("Input cannot be empty.")
        distance = self.distanceFrom(points[0])
        for point in points[1:]:
            new_dist = self.distanceFrom(point)
            if new_dist < distance:
                answer = point
                distance = new_dist

        return point

    def clone(self):
        return self

    def __add__(self, other):
        answer = []
        if isinstance(other, PointND):
            if (len(self.t) != len(other.t)):
                raise ValueError("Cannot operate on points with different cardinalities.")
            my_other = other.t
            for i in range(0, self.n):
                answer.append(self.t[i] + my_other[i])
            answer = PointND(*answer)
            return answer
        else:
            my_other = other
            for i in range(0, self.n):
                answer.append(self.t[i] + my_other)
            answer = PointND(*answer)
            return answer

    def __sub__(self, other):
        answer = []
        if isinstance(other, PointND):
            if (len(self.t) != len(other.t)):
                raise ValueError("Cannot operate on points with different cardinalities.")
            my_other = other.t
            for i in range(0, self.n):
                answer.append(self.t[i] - my_other[i])
            answer = PointND(*answer)
            return answer
        else:
            my_other = other
            for i in range(0, self.n):
                answer.append(self.t[i] - my_other)
            answer = PointND(*answer)
            return answer

    def __mul__(self, number):
        answer = []
        for i in range(0, self.n):
            answer.append(self.t[i] * number)
        answer = PointND(*answer)
        return answer

    def __truediv__(self, number):
        answer = []
        for i in range(0, self.n):
            answer.append(self.t[i] / number)
        answer = PointND(*answer)
        return answer

    def __neg__(self):
        answer = []
        for i in range(0, self.n):
            answer.append(-self.t[i])
        answer = PointND(*answer)
        return answer

    def __getitem__(self, item):
        answer = self.t[item]
        return answer

    def __eq__(self, other):
        if (len(self.t) != len(other.t)):
            raise ValueError("Cannot operate on points with different cardinalities.")
        for i in range(0, self.n):
            if self.t[i] != other.t[i]:
                return False
        return True

    def __ne__(self, other):
        if (len(self.t) != len(other.t)):
            raise ValueError("Cannot operate on points with different cardinalities.")
        for i in range(0, self.n):
            if self.t[i] == other.t[i]:
                return False
        return True

    def length(self):
        dist = 0;
        for coord in self.t:
            dist = dist + (coord ** 2)
        dist = dist ** 0.5

        return dist

    def __ge__(self, other):
        if (len(self.t) != len(other.t)):
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        self_dist = self.distanceFrom(zeroes)
        other_dist = other.distanceFrom(zeroes)

        if self_dist >= other_dist:
            return True
        return False

    def __le__(self, other):
        if (len(self.t) != len(other.t)):
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        self_dist = self.distanceFrom(zeroes)
        other_dist = other.distanceFrom(zeroes)

        if self_dist <= other_dist:
            return True
        return False

    def __gt__(self, other):
        if (len(self.t) != len(other.t)):
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        self_dist = self.distanceFrom(zeroes)
        other_dist = other.distanceFrom(zeroes)

        if self_dist > other_dist:
            return True
        return False

    def __lt__(self, other):
        if (len(self.t) != len(other.t)):
            raise ValueError("Cannot operate on points with different cardinalities.")
        zeroes = [0.0] * self.n
        self_dist = self.distanceFrom(zeroes)
        other_dist = other.distanceFrom(zeroes)

        if self_dist < other_dist:
            return True
        return False

def createPoint(dataString):
    data = dataString.split(",")
    for i in range(len(data)):
        try:
            data[i] = float(data[i].strip())
        except:
            return "ERROR: String found. All inputs should be floats."
    x = PointND(*data)
    return(x)

def distanceBetween(point1, point2):
    distance = point1.distanceFrom(point2)
    return distance

def checkVicinity(point, pointList, radius):
    greaterThan = 0
    lessThan = 0
    invalid = 0
    for data in pointList:
        distance = point.distanceFrom(data)
        if isinstance(distance, str):
            invalid += 1
        elif distance > radius:
            greaterThan += 1
        elif distance <= radius:
            lessThan += 1

    return (lessThan, greaterThan, invalid)

def checkOperation(*args):
    try:
        performProcessing(*args)
    except ConnectionRefusedError:
        raise ConnectionRefusedError
    except OSError as oserror:
        return "The following Error occurred: {0}".format(type(oserror).__name__)
    except:
        return False
    return True

if __name__ == "__main__":
    print("\n\n-----CHECKING createPoint with invalid data-----")
    answer = createPoint("1.34,3.54,lol")
    print(answer)
    print("\n\n-----CHECKING createPoint with valid data-----")
    answer = createPoint("1.34,3.54,    7.545")
    print(answer)
    print("\n\n-----CHECKING distanceFrom with valid data-----")
    x = answer
    y = PointND(3.14, 5.635, 1.00)
    answer = distanceBetween(x, y)
    print(answer)
    print("\n\n-----CHECKING distanceFrom with invalid data-----")
    y = PointND(3.14, 5.635, 1.00)
    z = PointND(6.26, 8.46, 1.0)
    answer = distanceBetween(x, y)
    print(answer)
    print("\n\n-----CHECKING checkVicinity-----")
    a = PointND(1.573, 4.621, 3.00)
    invalid = PointND(1.573, 4.621, 3.00, 900.0)
    pointList = [x, y, z, invalid, a]
    answer = checkVicinity(a, pointList, 6.3)
    print(answer)
    print("\n\n")
    print("\n\n-----CHECKING checkOperation-----")
    answer = checkOperation(x, y, z)
    print(answer)