import Container
from src.wiget.ImageView import ImageView


class Painter:
    def __init__(self):
        self._buttonViewList = {}
        self._imageViewList = {}
        self._textViewList = {}

    def paint(self):
        self.__paintButtons()
        self.__paintTexts()
        self.__paintImages()
        Container.display.update()

    def __paintButtons(self):
        for button in self._buttonViewList.values():
            self.__paintButtonView(button)

    def __paintImages(self):
        for image in self._imageViewList:
            self.__paintImageView(image)

    def __paintTexts(self):
        for text in self._textViewList:
            self.__paintTextView(text)

    def __paintButtonView(self, button):
        imageView = ImageView()
        imageView.setPos(button.getPos())
        imageView.setImageByObject(button.getImage())
        self.__paintImageView(imageView)
        self.__paintTextView(button.getTextView())

    def __paintImageView(self, imageView):
        Container.screen.blit(imageView.getImage(), imageView.getPos())

    def __paintTextView(self, textView):
        Container.screen.blit(textView.getTextView(), textView.getPos())
