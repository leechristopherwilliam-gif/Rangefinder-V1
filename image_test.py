import cv2

coordinates = []
pixel_width = 0


def handle_mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(coordinates) < 2:
            coordinates.append(x)
            print(coordinates)


def measure_pixel_width(image_path):
    coordinates.clear()  # resets for each use

    image = cv2.imread(image_path)

    if image is None:
        print("Could not load image")
        return None

    cv2.imshow("My photo", image)
    cv2.setMouseCallback("My photo", handle_mouse_event)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if len(coordinates) == 2:
        pixel_width = abs(coordinates[1] - coordinates[0])
        return pixel_width
    return None
