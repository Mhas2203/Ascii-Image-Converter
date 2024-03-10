# Import the Python Imaging Library (PIL)
import PIL.Image

# ASCII characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# Resize the image according to a new width


def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image

# Convert each pixel to grayscale


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image

# Convert pixels to a string of ASCII characters


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters

# Main function


def main(new_width=100):
    # Attempt to open image from user input
    path = input("Enter a valid pathname to an image:\n")

    try:
        image = PIL.Image.open(path)
    except Exception as e:
        print(f"Error: {e}")
        print(f"{path} is not a valid pathname to an image.")
        return

    # Convert image to ASCII
    new_image_data = pixels_to_ascii(grayify(resize_image(image)))

    # Format
    pixel_count = len(new_image_data)
    ascii_image = "\n".join([new_image_data[index:(index + new_width)]
                            for index in range(0, pixel_count, new_width)])

    # Print result
    print(ascii_image)

    try:
        # Save result to "ascii_image.txt"
        with open("ascii_image.txt", "w") as f:
            f.write(ascii_image)
        print("ASCII art saved to ascii_image.txt")
    except Exception as e:
        print(f"Error saving file: {e}")


# Run program
main()
