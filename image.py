class ImageCrop:
    def __init__(self, x, y, w, h, origin):
        self.X = x
        self.Y = y
        self.W = w
        self.H = h
        self.Origin = origin

class ImageOptions:
    def __init__(self, cfg):
        self.ImagePath = None
        self.ImageCrop = None
        self.Greyscale = 0
        self.ImageTint = (0xff,0xff,0xff,0xff)
        self.ImageAlpha = 0xff
        self.ImageFlip = None
        self.ImageRotate = 0.0
        self.UseExifOrientation = 0
        self.ColorMatrix = [
            [1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0],
            [0, 0, 0, 0, 1]
        ]
