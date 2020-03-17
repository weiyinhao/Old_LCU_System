from PyQt5.Qt import *
class HorizontalTabBar(QTableView):

    def __init__(self, *args, **kwargs):

        super(HorizontalTabBar, self).__init__(*args, **kwargs)


    def paintEvent(self, event):

        painter = QStylePainter(self)
        option = QStyleOptionTab()

        painter.begin(self)
        for index in range(self.count()):
            self.initStyleOption(option, index)
            tabRect = self.tabRect(index)
            tabRect.moveLeft(10)
            painter.drawControl(QStyle.CE_TabBarTabShape, option)
            painter.drawText(tabRect, Qt.AlignVCenter | Qt.TextDontClip, self.tabText(index))
        painter.end()
if __name__=='__main__':
    import sys
    app=QApplication(sys.argv)

    window=HorizontalTabBar()
    window.show()

    sys.exit(app.exec_())