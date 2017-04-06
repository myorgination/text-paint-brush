import math

_NUM_VARIATIONS_PER_LETTER = 10

## Map of ASCII values to counters for each value
_COUNTERS = {}

## Map of ASCII values to color lists
_COLORS = {}


class Rgb_Color(object):
    def __init__(self):
        self.r_code = None
        self.g_code = None
        self.b_code = None

    def __str__(self):
        return "rgb({0},{1},{2})".format( self.r_code, self.g_code, self.b_code )

    def set_color_codes(self, x, y):
        self.r_code = x * y * 13 % 255
        self.g_code = x * y * 77 % 255
        self.b_code = x * y * 51 % 255


    def set_color_codes_rgb(self, r, g, b):
        self.r_code = r
        self.g_code = g
        self.b_code = b


def setup_colors():
    for x in range(0, 128):
        for y in range(0, _NUM_VARIATIONS_PER_LETTER):
            if y == 0:
                _COLORS[x] = []

            rgb_color_instance = Rgb_Color()
            rgb_color_instance.set_color_codes(x, y)
            _COLORS[x].append(rgb_color_instance)


def get_colors_from_text(text):
    _COUNTERS = {}

    return_cols = []

    for x in text:
        ascii_code = ord(x)
        if ascii_code not in _COUNTERS:
            _COUNTERS[ascii_code] = 0

        if ascii_code in _COLORS and ascii_code in _COUNTERS:
            return_cols.append(_COLORS[ascii_code][_COUNTERS[ascii_code] % _NUM_VARIATIONS_PER_LETTER])
            _COUNTERS[ascii_code] += 1

    return return_cols


def get_color_averages_from_text(text):
    _COUNTERS = {}

    return_cols = []

    for word in text.split(" "):
        word_colors = get_colors_from_text(word)
        r_sum = 0
        g_sum = 0
        b_sum = 0

        for word_color in (word_colors):
            r_sum += word_color.r_code
            g_sum += word_color.g_code
            b_sum += word_color.b_code

        r_avg = r_sum / len(word_colors)
        g_avg = g_sum / len(word_colors)
        b_avg = b_sum / len(word_colors)

        rgb_color_instance = Rgb_Color()
        rgb_color_instance.set_color_codes_rgb(math.floor(r_avg), math.floor(g_avg), math.floor(b_avg))
        return_cols.append(rgb_color_instance)

    return return_cols


if __name__ == "__main__":
    setup_colors()
    print(get_colors_from_text("hello world"))
