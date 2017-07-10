# === Solution Problem 1 Part A

# Enter your code for RectangularRoom (from the previous problem)
#  and Robot in this box
class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.

        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        self.totalTiles = width * height
        self.cleanTileCount = 0
        self.cleanTileList = []


    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.

        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        # add tile to list of clean tiles

        posX = math.floor(pos.x)
        posY = math.floor(pos.y)
        posit = (posX, posY)

        if not self.isTileCleaned(posX,posY):
            self.cleanTileCount = self.cleanTileCount + 1


        if pos.x < 1 and pos.y < 1:
            self.cleanTileList.append((0,0))

            return


        self.cleanTileList.append(posit)


        return

    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        #loop through cleanTileList and check if tile is cleaned
        posX = math.floor(m)
        posY = math.floor(n)
        pos = (posX, posY)

        if pos in self.cleanTileList:
            return True
        else:
            return False


    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        # total numTiles equals width * height..could also return self.TotalTiles
        return self.width * self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        return self.cleanTileCount

    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = (random.random()) * self.width
        y = (random.random()) * self.height
        return Position(x,y)
        #return a tuple of 2 numbers between width and height


    def isPositionInRoom(self, pos):
        """
        Return True if pos is inside the room.

        pos: a Position object.
        returns: True if pos is in the room, False otherwise.
        """
        if pos.x < 0:
            return False
        if pos.y < 0:
            return False
        if float(pos.x) >= self.width:
            return False
        if float(pos.y) >= self.height:
            return False
        return True


# === Solution Problem 1 Part A

class Robot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in the room.
    The robot also has a fixed speed.

    Subclasses of Robot should provide movement strategies by implementing
    updatePositionAndClean(), which simulates a single time-step.
    """
    #any class inheriting from an abstract class  should implement and override the abstract
    #methods
#    import abc
#
#class BasePizza(object):
#    __metaclass__  = abc.ABCMeta
#
#    @abc.abstractmethod
#    def get_radius(self):
#         """Method that should do something."""
#
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified room. The
        robot initially has a random direction and a random position in the
        room. The robot cleans the tile it is on.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.randrange(360)
        self.room.cleanTileAtPosition(self.position)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position

    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction

    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.

        TEST whether the position fits in the room
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees

        change direction when moving out of room
        """
        #increment direction by 90 degrees when hit wall

        self.direction = direction

    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
        raise NotImplementedError # don't change this!


# === Solution Problem 2
class StandardRobot(Robot):
    """
    A StandardRobot is a Robot with the standard movement strategy.

    At each time-step, a StandardRobot attempts to move in its current
    direction; when it would hit a wall, it *instead* chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the raise passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """

        # list of positions along the wall
        wall = []
        width = self.room.width - 1
        height = self.room.height - 1

        for i in range(width):
            bottom = (i, 0)
            top = (0, height - 1)
            wall.append(bottom)
            wall.append(top)

        for p in range(height):
            left = (0,p)
            right = (width - 1, p)
            wall.append(left)
            wall.append(right)

        new = self.getRobotPosition().getNewPosition(self.direction, self.speed)
        # if new position isn't on the wall
        if new not in wall and self.room.isPositionInRoom(new):
            # move in same direction, clean tile
            self.setRobotPosition(new)
            self.room.cleanTileAtPosition(new)
        else:
            #set to position in room
            self.setRobotDirection(random.randrange(360))


# === Solution Problem 3


def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """

    timeList = []

    for i in range(num_trials):
        room = RectangularRoom(width, height)
        robotList = []

        for r in range(num_robots):
#                #need to connect robot with room somehow
            robotList.append(robot_type(room, speed))

        time = 0

        while (1.0*room.getNumCleanedTiles()/room.getNumTiles()) <= min_coverage:
            for robot in robotList:
                robot.updatePositionAndClean()
            time = time + 1
        timeList.append(time)
    return float(sum(timeList)) / len(timeList)
