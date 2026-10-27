from image_test import measure_pixel_width


def calculate_focal_length(pixel_width_calibration, known_distance_calibration, real_width_calibration):
    focal_length = pixel_width_calibration * \
        known_distance_calibration / real_width_calibration
    return focal_length


def calculate_distance(focal_length, pixel_width, real_width):
    distance = (real_width * focal_length) / pixel_width
    return distance


def main():

    # Calibration
    pixel_width_calibration = measure_pixel_width(
        "Tank photo calibration 2.jpg")
    if pixel_width_calibration is None or pixel_width_calibration == 0:
        print("Invalid pixel width for calibration")
        return ()
    known_distance_calibration = float(
        input("Please enter known distance for calibration: "))
    if known_distance_calibration <= 0:
        print("Invalid known distance for calibration")
    if known_distance_calibration <= 0:
        print("Invalid known distance for calibration")
        return ()
    real_width_calibration = float(
        input("Please enter real width for calibration: "))
    if real_width_calibration <= 0:
        print("Invalid real width for calibration")
        return ()
    focal_length = calculate_focal_length(
        pixel_width_calibration, known_distance_calibration, real_width_calibration)

    # Distance
    image_path = "None"
    while True:
        print("Tank Image Selection")
        print("1. Tank photo 1")
        print("2. Tank photo 2")
        print("3. Tank photo 3")

        choice = input("Enter the number of your choice: ")

        if choice == "1":
            image_path = "Tank photo 50m.jpg"
        elif choice == "2":
            image_path = "Tank photo 200m.jpg"
        elif choice == "3":
            image_path = "Tank photo 300m.jpg"
        else:
            print("Invalid choice")
            continue
        break

    pixel_width = measure_pixel_width(image_path)
    if pixel_width is None or pixel_width == 0:
        print("Failed to measure pixel width")
        return ()
    real_width = float(input("Please enter real width of object: "))
    if real_width <= 0:
        print("Invalid real width of object")
        return ()
    distance = calculate_distance(focal_length, pixel_width, real_width)
    print("The distance to the object is:", distance)


if __name__ == "__main__":
    main()
