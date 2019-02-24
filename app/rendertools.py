import cv2


class RenderTools:

    @staticmethod
    def draw_label(img, text, position, bg_color):
        """
        Draws a label at the specified position.

        :param img: the to be drawn into
        :param text: the text to be displayed
        :param position: the x, y position where the label will be drawn
        :param bg_color: the background color for the label. best choose the color of your bounding box.
        """

        font_face = cv2.FONT_HERSHEY_SIMPLEX
        scale = 0.4
        color = (0, 0, 0)
        thickness = cv2.FILLED
        margin = 2

        txt_size = cv2.getTextSize(text, font_face, scale, thickness)

        end_x = position[0] + txt_size[0][0] + margin
        end_y = position[1] + txt_size[0][1] + margin

        text_pos = (position[0], position[1] + txt_size[0][1])

        cv2.rectangle(img, position, (end_x, end_y), bg_color, thickness)
        cv2.putText(img, text, text_pos, font_face, scale, color, 1, cv2.LINE_AA)
