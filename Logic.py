from ClassRectangle import Rectangle

class Logic:
    def calculate_TOTAL_square(rectangles):
        if isinstance(rectangles, (list, tuple)):
            TOTAL = 0
            for rect in rectangles:
               if isinstance(rect, Rectangle):
                   TOTAL+= rect.calculate_square()
            return TOTAL

    def calculate_TOTAL_P(rectangles):
        if isinstance(rectangles, (list, tuple)):
            TOTAL = 0
            for rect in rectangles:
               if isinstance(rect, Rectangle):
                   TOTAL+= rect.calculate_P()
            return TOTAL