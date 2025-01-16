import os.path
import sys
from encodings import search_function

from PyQt6.QtWidgets import QDialog, QApplication

from layout import Ui_Dialog


class MyForm(QDialog):
    def __init__(self):
        self.ui = Ui_Dialog()
        super().__init__()
        self.ui.setupUi(self)
        self.ui.students.itemClicked.connect(self.students_fail)
        self.ui.failedStudents.itemClicked.connect(self.good_students)
        self.ui.wyrokButton.clicked.connect(self.student_save)
        self.ui.dodajForm.clicked.connect(self.formularz)
        self.ui.usunButton.clicked.connect(self.delete_student_comboBox)
        self.read_students()
        self.add_students_to_combobox()
        self.show()



    def add_students_to_combobox(self):
        students = []

        for i in range(self.ui.students.count()):
            students.append(self.ui.students.item(i).text())
        self.ui.usunUczniaCOMBOBOX.addItems(students)

        for i in range(self.ui.failedStudents.count()):
            students.append(self.ui.failedStudents.item(i).text())
        self.ui.usunUczniaCOMBOBOX.addItems(students)


    def delete_student_comboBox(self):
        student = self.ui.usunUczniaCOMBOBOX.currentText()

        for i in range(self.ui.students.count()):
            if student == self.ui.students.item(i).text():
                self.ui.students.takeItem(i)
                break

        for i in range(self.ui.failedStudents.count()):
            if student == self.ui.failedStudents.item(i).text():
                self.ui.failedStudents.takeItem(i)
                break
        self.ui.usunUczniaCOMBOBOX.removeItem(self.ui.usunUczniaCOMBOBOX.currentIndex())






    def formularz(self):
        imie = self.ui.imieForm.text()
        nazwisko = self.ui.nazwiskoForm.text()

        self.ui.students.addItem(imie + " " + nazwisko)

    def read_students(self):
        if os.path.exists('zdani.txt') and os.path.exists('sierpien.txt'):
            self.ui.students.clear()
            self.ui.failedStudents.clear()
            with open('zdani.txt','r') as file:
                students = file.read().splitlines()
                for student in students:
                    self.ui.students.addItem(student)

            with open('sierpien.txt','r') as file:
                students = file.read().splitlines()
                for student in students:
                    self.ui.failedStudents.addItem(student)



    def students_fail(self):
        items = self.ui.students.selectedItems()
        self.ui.students.takeItem(self.ui.students.currentRow())
        for item in items:
            self.ui.failedStudents.addItem(item.text())


    def good_students(self):
        items = self.ui.failedStudents.selectedItems()
        self.ui.failedStudents.takeItem(self.ui.failedStudents.currentRow())
        for item in items:
            self.ui.students.addItem(item.text())



    def student_save(self):
        with open('sierpien.txt','w') as file:
            for i in range(self.ui.failedStudents.count()):
                file.write(self.ui.failedStudents.item(i).text())
                file.write('\n')


        with open('zdani.txt','w') as file2:
            for i in range(self.ui.students.count()):
                file2.write(self.ui.students.item(i).text())
                file2.write('\n')



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyForm()
    sys.exit(app.exec())