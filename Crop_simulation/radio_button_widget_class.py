from PyQt4.QtGui import *

class RadioButtonWidget(QWidget):
    """this class creates a group of radio butons from a given list of labels"""

    #constructor
    def __init__(self, label, instruction, button_list):
        super().__init__() # call super class constructor

        #create widgets
        self.title_label = QLabel(label)
        self.radio_group_box = QGroupBox(instruction)
        self.radio_button_group = QButtonGroup()
        #create the radio buttons
        self.radio_button_list = []
        for each in button_list:
            self.radio_button_list.append(QRadioButton(each))

        #set defult checked item
        self.radio_button_list[0].setChecked(True)

        #create layout
        self.radio_button_layout = QVBoxLayout()

        #add buttons to layout
        counter = 1
        for each in self.radio_button_list:
            self.radio_button_layout.addWidget(each)
            self.radio_button_group.addButton(each)
            self.radio_button_group.setId(each, counter)
            counter += 1
        
        #add radio buttos to the goup box
        self.radio_group_box.setLayout(self.radio_button_layout)

        #create whole widget layout
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.title_label)
        self.main_layout.addWidget(self.radio_group_box)

        #set the laout for this widget
        self.setLayout(self.main_layout)

    #method  to find ou the selected button
    def selected_button(self):
        return self.radio_button_group.checkedId()
