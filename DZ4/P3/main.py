
import numpy as np
import math
import struct

def print_progress_bar(cur_val, max_val, section_count=20):
    section_count += 1
    percent = cur_val / max_val
    active_section = int(percent * section_count)
    print_str = "\r[" + "#" * active_section + " " * (section_count - active_section - 1) + "]" + f" {percent * 100:.2f} / 100%"
    print(print_str, end="")


def set_pixel(pic_array, x, y, size, color):
    pic_array[y, x] = color
    size -= 1
    y__left_border = max(y-size, 0)
    y_right_border = min(y+size, len(pic_array)-1)
    x__left_border = max(x-size, 0)
    x_right_border = min(x+size, len(pic_array[0])-1)

    pic_array[y__left_border:y_right_border, x__left_border:x_right_border, :] = color



def generate_rgb_matrix(scale=1, plot_point_size=None, step=0.001, progress=True):
    if (plot_point_size is None):
        plot_point_size = round(scale / 10)
        if (plot_point_size == 0):
            plot_point_size = 1

    matrix_size = int(15 * 2 * scale) + 1
    pic_matrix = np.full((matrix_size, matrix_size, 3), 255, dtype=np.uint8)

    t = 0
    max_value = 4 * math.pi
    while t <= max_value:
        if (progress):
            print_progress_bar(t, max_value)
        x = int((13 * (math.cos(t) - math.cos(6.5 * t) / 6.5) + 15) * scale)
        y = int((13 * (math.sin(t) - math.sin(6.5 * t) / 6.5) + 15) * scale)

        # Цвет пикселя зависит от координат и времени
        set_pixel(pic_matrix, x, y, plot_point_size, (int(x / matrix_size / 2 * 255), int(y / matrix_size * 255),
                                                      int(t / max_value * 255)))

        t += step

        if (progress):
            print("", end="\r")

    return pic_matrix


def write_bmp(pixel, filename, progress=True):
    width = len(pixel)
    height = len(pixel[0])

    bmp_file_size = 14 + 40 + (3 * width * height)
    header = struct.pack("=HIHHI", 0x4D42, bmp_file_size, 0, 0, 54) + \
             struct.pack("=IiiHHIIIIII", 40, width, height, 1, 24, 0, 0, 0, 0, 0, 0)

    data = bytes()
    width_str_struct = "=" + "BBB" * width
    pixel = pixel.reshape(height, 3 * width)
    for y in range(height):
        if (progress):
            print_progress_bar(y, height)

        data += struct.pack(width_str_struct, *pixel[y])
        for i in range(width % 4):
            data += struct.pack("=B", 0)

    with open(filename, "wb") as f:
        f.write(header)
        f.write(data)

    if (progress):
        print("", end="\r")


print("generating rgb matrix")
pic = generate_rgb_matrix(scale=20, plot_point_size=4)
print("writing bmp file")
write_bmp(pic, "test.bmp")
print("Ok")

# import matplotlib.pyplot as plt
# plt.imshow(pic)
# plt.show()



