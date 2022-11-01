from ClassRectangle import Rectangle



class View:
    def convert(rectangles):
        if isinstance(rectangles, (list, tuple)):
            result = ""
            for rect in rectangles:
                if isinstance(rect, Rectangle):
                    result += str(rect) + "\n"

            return result
