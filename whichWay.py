import sys
from PyQt5.QtGui import QIcon, QPalette, QColor, QRegExpValidator, QFont
from PyQt5.QtCore import QTimer, Qt, QSize, QRegExp
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QWidget, QPushButton, QLineEdit

class TimerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(355, 200)
        
        timerFont = QFont("Impact")
        timerFont.setPointSize(17)
        
        buttonFont = QFont("Impact")
        buttonFont.setPointSize(10)
        
        palette = self.palette()
        palette.setColor(QPalette.Background, QColor("#000000"))
        self.setPalette(palette)
        self.setStyleSheet("background-color: #000000;") 
        self.setWindowFlag(Qt.WindowStaysOnTopHint, True)
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)
        self.setWindowFlag(Qt.FramelessWindowHint) 
        
        # Welcome message
        self.welcome_label = QLabel("You can edit timers!", self)
        self.welcome_label.setStyleSheet("QLabel {font-size: 9pt; color: white }")
        self.welcome_label.setFont(buttonFont)
        self.welcome_label.show()
        self.welcome_label.setGeometry(69, -55, 200, 200)
        QTimer.singleShot(3000, self.welcome_label.hide)

        # Pin Button
        self.pin_button = QPushButton('Pin', self)
        self.pin_button.clicked.connect(self.pin_window)
        self.pin_button.setFixedSize(QSize(45, 45))
        self.pin_button.setText('🖈')
        self.pin_button.setFlat(True)
        self.pin_button.setAutoFillBackground(True)
        self.pin_button.setStyleSheet("background-color: white; color: white;font-family: Bauhaus 93; font-size: 20pt;color: white")
        
        # Close Button
        close_button = QPushButton('🞮', self)
        close_button.clicked.connect(self.close)
        close_button.setFixedSize(QSize(40, 40))
        close_button.setFlat(True)
        close_button.setStyleSheet("background-color: transparent; font-size: 15pt;color: white")
        close_button.setGeometry(70, -55, 200, 200)
        close_button.show()
        
        self.move_button = QPushButton('Move', self)
        self.move_button.clicked.connect(self.enable_move)
        self.move_button.setHidden(True)
        
        # Timer labels
        self.time_label_1 = QLineEdit("00:00", self)
        self.time_label_1.setFixedSize(80, 40)
        self.time_label_1.setMinimumWidth(50)
        self.time_label_1.setAlignment(Qt.AlignCenter)
        self.time_label_1.setFrame(False)
        self.time_label_1.setFont(timerFont)
        self.time_label_1.setStyleSheet("QLineEdit { background-color: transparent; color: #B0E2FF}")
        self.time_label_1.setReadOnly(False)
        
        self.time_label_2 = QLineEdit("00:00", self)
        self.time_label_2.setFixedSize(80, 40)
        
        self.time_label_2.setMinimumWidth(50)
        self.time_label_2.setAlignment(Qt.AlignCenter)
        self.time_label_2.setFrame(False)
        self.time_label_2.setFont(timerFont)
        self.time_label_2.setStyleSheet("QLineEdit { background-color: transparent; color: red}")
        self.time_label_2.setReadOnly(False)
    
        # Way Labels
        self.way_label = QLabel("On your way!", self)
        self.way_label.setStyleSheet("QLabel { font-size: 10pt; color: #B0E2FF}")
        self.way_label.setFont(buttonFont)
        self.way_label.setGeometry(100, 20, 300, 50)
        self.way_label.hide()
        
        self.way_label2 = QLabel("Getting away!", self)
        self.way_label2.setStyleSheet("QLabel { font-size: 10pt; color: red}")
        self.way_label2.setFont(buttonFont)
        self.way_label2.setGeometry(100, 20, 300, 50)
        self.way_label2.hide()

        # Start/Stop buttons
        self.start_stop_button_1 = QPushButton('RIGHT WAY', self)
        self.start_stop_button_1.clicked.connect(self.start_stop_timer_1)
        self.start_stop_button_1.setFlat(True)
        self.start_stop_button_1.setAutoFillBackground(True)
        self.start_stop_button_1.setStyleSheet("background-color: #B0E2FF; color: #B0E2FF")
        self.start_stop_button_1.setFont(buttonFont)
        self.start_stop_button_1.setFixedWidth(100)
        
        self.start_stop_button_2 = QPushButton('WRONG WAY', self)
        self.start_stop_button_2.clicked.connect(self.start_stop_timer_2)
        self.start_stop_button_2.setFlat(True)
        self.start_stop_button_2.setAutoFillBackground(True)
        self.start_stop_button_2.setStyleSheet("background-color: red; color: red")
        self.start_stop_button_2.setFont(buttonFont)
        self.start_stop_button_2.setFixedWidth(100)
        
        # Timers
        self.timer_1 = QTimer(self)
        self.timer_1.setInterval(1000)
        self.timer_1.timeout.connect(self.update_time_1)
    
        self.timer_2 = QTimer(self)
        self.timer_2.setInterval(1000)
        self.timer_2.timeout.connect(self.update_time_2)
        
        row_layout = QHBoxLayout()
        row_layout.addWidget(self.time_label_1)
        row_layout.addWidget(self.start_stop_button_1)
        
        row_layout2 = QHBoxLayout()
        row_layout2.addWidget(self.time_label_2)
        row_layout2.addWidget(self.start_stop_button_2)
        
        row_layout3 = QHBoxLayout()
        row_layout3.addWidget(self.pin_button)
        row_layout3.addStretch(3)
        row_layout3.addWidget(close_button)
        
        layout = QVBoxLayout(self)
        layout.addLayout(row_layout3)
        layout.addWidget(self.move_button)
        layout.addLayout(row_layout)
        layout.addLayout(row_layout2)
        
        self.setWindowTitle("Which Way?")
        self.moving = False 
        self.show()

    # Düzeltilmiş Metod Girintileri
    def enable_move(self):
        self.setCursor(Qt.OpenHandCursor)
        self.move_button.setText('Release')
        self.move_button.clicked.disconnect()
        self.move_button.clicked.connect(self.disable_move)
        self.moving = False
            
    def disable_move(self):
        self.setCursor(Qt.ArrowCursor)
        self.move_button.setText('Move')
        self.move_button.clicked.disconnect()
        self.move_button.clicked.connect(self.enable_move)
        self.moving = False
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moving = True
            self.offset = event.pos()
            
    def mouseMoveEvent(self, event):
        if self.moving:
            self.move(event.globalPos() - self.offset)
            
    def mouseReleaseEvent(self, event):
        self.moving = False
        
    def pin_window(self):
        if self.windowFlags() & Qt.WindowStaysOnTopHint:
            self.setWindowFlags(self.windowFlags() ^ Qt.WindowStaysOnTopHint)
            self.pin_button.setStyleSheet("background-color: red; color: red;font-family: Bauhaus 93; font-size: 20pt;color:red")
        else:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.pin_button.setText('🖈')
            self.pin_button.setStyleSheet("background-color: white; color: white;font-family: Bauhaus 93; font-size: 20pt;color:white")
        self.show()
        
    def update_time_1(self):
        current_time = self.time_label_1.text()
        minutes, seconds = current_time.split(':')
        minutes, seconds = int(minutes), int(seconds)
        seconds += 1
        if seconds >= 60:
            minutes += 1
            seconds = 0
        self.time_label_1.setText('{:02d}:{:02d}'.format(minutes, seconds))
        
    def update_time_2(self):
        current_time = self.time_label_2.text()
        minutes, seconds = current_time.split(':')
        minutes, seconds = int(minutes), int(seconds)
        seconds += 1
        if seconds >= 60:
            minutes += 1
            seconds = 0
        self.time_label_2.setText('{:02d}:{:02d}'.format(minutes, seconds))
        
    def start_stop_timer_1(self):
        if self.timer_1.isActive():
            self.timer_1.stop()
            self.start_stop_button_1.setText('RIGHT WAY')
            self.way_label.hide()   
        else:
            self.timer_1.start()
            self.start_stop_button_1.setText('STOP')
            self.timer_2.stop()
            self.start_stop_button_2.setText('WRONG WAY')
            self.way_label.show() 
            self.way_label2.hide()
    
    def start_stop_timer_2(self):
        if self.timer_2.isActive():
            self.timer_2.stop()
            self.way_label2.hide()
            self.start_stop_button_2.setText('WRONG WAY')
        else:
            self.timer_2.start()
            self.way_label.hide()
            self.way_label2.show()
            self.start_stop_button_2.setText('STOP')
            self.timer_1.stop()  
            self.start_stop_button_1.setText('RIGHT WAY')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer_app = TimerApp()
    timer_app.show()
    sys.exit(app.exec_())