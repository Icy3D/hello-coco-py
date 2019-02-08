import random


class Tools:

    @staticmethod
    def create_colors(num_colors):
        result = []
        r = int(random.random() * 256)
        g = int(random.random() * 256)
        b = int(random.random() * 256)
        step = 256 / num_colors
        for i in range(num_colors):
            r += step
            g += step
            b += step
            r = int(r) % 256
            g = int(g) % 256
            b = int(b) % 256
            result.append((r, g, b))
        return result
