from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from models import *

class DaddyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        #set window title and size
        self.setWindowTitle("null")
        self.resize(700,700)

        #define font sizes
        self.fonts = {}

        title_font = QFont()
        title_font.setPointSize(35)
        self.fonts["title"] = title_font

        subtitle_font = QFont()
        subtitle_font.setPointSize(25)
        self.fonts["subtitle"] = subtitle_font

        body_font = QFont()
        body_font.setPointSize(15)
        self.fonts["body"] = body_font

        baby_font = QFont()
        baby_font.setPointSize(5)
        self.fonts["baby"] = baby_font
        
    def create_label(self, label_text: str, font_name: str, x: int, y: int):
        label = QLabel(label_text, parent = self)
        label.move(x, y)
        label.setStyleSheet("color: white;")
        label.setFont(self.fonts[font_name])
        label.adjustSize()
        return label

    
    def create_picture(self, image_path, x, y, size_x, size_y):
        picture_label = QLabel(parent = self)
        picture_label.move(x,y)
        pixmap = QPixmap(image_path)
        pixmap = pixmap.scaled(size_x, size_y)
        picture_label.setPixmap(pixmap)
        picture_label.resize(pixmap.width(), pixmap.height())

    def create_button(self, text, x, y, size_x, size_y):
        button = QPushButton(parent = self, text = text)
        button.setStyleSheet("color: black;")
        button.move(x,y)
        button.resize(size_x, size_y)
        return button
    
    def create_textbox(self, x, y, size_x, size_y):
        textbox = QLineEdit(parent = self)
        textbox.move(x,y)
        textbox.resize(size_x, size_y)
        return textbox


class HomePageWindow(DaddyWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home Page")
        
        # Create title label
        self.title_label = self.create_label( "Welcome to my Financial Math Calculator", "title", 5, 20)

        #create image
        self.create_picture("images/crawdadShark.jpeg", 150, 250, 300, 250)

        #create buttons 
        self.npv_button = self.create_button("NPV", 50,100,80,40)
        self.npv_button.clicked.connect(self.button_clicked_NPV)

        #display window
        self.show()

    def button_clicked_NPV(self):
        #want to launch NPV Page
        self.npv_window = NpvWindow()


class NpvWindow(DaddyWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NPV Calculator")

        #create cash_flow model
        self.cash_flows = CashFlows()

        #add title
        self.title = self.create_label("NPV Calculator", "title", 20, 20)

        #create place to add cashflow
        self.cashflow_label = self.create_label("Cashflow:", "body", 20, 80)
        self.cashflow_textbox = QLineEdit(parent=self)
        self.cashflow_textbox.move(20,100)
        self.cashflow_textbox.resize(200,30)

        #create place for interest rate
        self.interest_rate_label = self.create_label("Interest Rate: ", "body", 360, 80)
        self.interest_rate_textbox = QLineEdit(parent = self)
        self.interest_rate_textbox.move(400,100)
        self.interest_rate_textbox.resize(50,30)

        #create radio button for interest rate type
        self.button_i = QRadioButton("i", self)
        self.button_i.move(500,60)

        self.button_d = QRadioButton("d", self)
        self.button_d.move(500, 80)

        self.button_delta = QRadioButton("delta", self)
        self.button_delta.move(500, 100)

        self.button_v = QRadioButton("v", self)
        self.button_v.move(500, 120)

        #create place for time
        self.time_label = self.create_label("Time: ", "body", 280, 80)
        self.time_textbox = QLineEdit(parent = self)
        self.time_textbox.move(270, 100)
        self.time_textbox.resize(50,30)

        #create place to submit cf
        self.submit_button = self.create_button("submit cashflow", 15, 150, 550, 40)
        self.submit_button.clicked.connect(self.button_clicked_submit_cf)

        #display cash flows
        self.cashflow_display = self.create_label("", "body", 30, 200)

        #displays window
        self.show()

    def button_clicked_submit_cf(self):
        #need to verify text in text boxes is valid
        int_rate = self.interest_rate_textbox.text().replace(".", "")
        int_rate = int_rate.replace("-","")

        cash_flow = self.cashflow_textbox.text().replace(".", "")
        cash_flow = cash_flow.replace("-", "")

        if(not(str.isnumeric(int_rate))):
            box = QMessageBox.information(self, "Invalid", "Please enter a valid interest rate")
        elif(not(str.isdigit(self.time_textbox.text()))):
            box = QMessageBox.information(self, "Invalid", "Please enter a valid time")
        elif(not(str.isdigit(cash_flow))):
            box = QMessageBox.information(self, "Invalid", "Please enter a cashflow")
        else:
            #add cf to table/model
            self.cash_flows.add_cashflow(int(self.time_textbox.text()), float(self.cashflow_textbox.text()), float(self.interest_rate_textbox.text()))
            
            #reset time and cashflow textbox
            self.time_textbox.setText("")
            self.cashflow_textbox.setText("")

            #present cash flows
            self.present_cash_flows()
            self.show()

    def present_cash_flows(self):
        # new_label = self.create_label(self.cash_flows.__repr__(), "body", 100, 300)
        self.cashflow_display.setText(self.cash_flows.__repr__())
        self.cashflow_display.adjustSize()
    
    
