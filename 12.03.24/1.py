
class Rectangle:
    def __init__(self, a, b, w, h):
        self.a = a
        self.b = b
        self.w = w
        self.h = h
        print("Создадим объект Rectangle")

    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

    def get_b(self):
        return self.b

    def set_b(self, b):
        self.b = b

    def get_w(self):
        return self.w

    def set_w(self, w):
        self.w = w

    def get_h(self):
        return self.h

    def set_h(self, h):
        self.h = h

    def intersection(self, rect):
        left=max(self.a,rect.a)
        right=min(self.a+self.w,rect.a+rect.w)
        bottom=max(self.b,rect.b)
        top=min(self.b+self.h,rect.b+rect.h)
        width=right-left
        height=top-bottom
        if width==0 or height==0:
            rect3=None
        else:
            rect3=Rectangle(0,0,width,height)

rect1 = Rectangle(0, 0, 10, 10)
rect2 = Rectangle(10, 0, 10, 10)
rect3 = Rectangle(0, 0, 6, 6)
rect4 = Rectangle(4, 4, 6, 6)
rect12 = rect1.intersection(rect2)
rect34 = rect3.intersection(rect4)

if rect12 is None:
    print("No intersection")
else:
    print(rect12.get_a(), rect12.get_b(), rect12.get_w(), rect12.get_h())

if rect34 is None:
    print("No intersection")
else:
    print(rect34.get_a(), rect34.get_b(), rect34.get_w(), rect34.get_h())