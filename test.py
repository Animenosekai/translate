import enum


class Test(enum.Enum):
    TEST = "test"
    BUILD = "build"


print(Test(1))
