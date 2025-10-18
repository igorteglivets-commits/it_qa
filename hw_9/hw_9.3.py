class Romb:

    def __init__(self, side_length: float, angle_alpha: float):
        self.side_length = side_length
        self.angle_alpha = angle_alpha

    def __setattr__(self, name, value):
        if name == "side_length":
            if value <= 0:
                raise ValueError(" Side length must be greater than 0!")
            object.__setattr__(self, "_Romb__side_length", value)

        elif name == "angle_alpha":
            if not (0 < value < 180):
                raise ValueError(" Angle α must be between 0 and 180 degrees!")
            object.__setattr__(self, "_Romb__angle_alpha", value)
            object.__setattr__(self, "_Romb__angle_beta", 180 - value)

        else:
            object.__setattr__(self, name, value)

    def get_data(self):

        return {
            "side_length": self.__side_length,
            "angle_alpha": self.__angle_alpha,
            "angle_beta": self.__angle_beta
        }



def main():
    print(" Create a rhomb")
    try:
        side = float(input("Enter the side length of the rhomb: "))
        alpha = float(input("Enter angle α (in degrees): "))

        rhomb = Romb(side, alpha)
        return rhomb.get_data()

    except ValueError as e:
        return str(e)



if __name__ == "__main__":
    result = main()
    print("\nResult:")
    print(result)
