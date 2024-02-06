'''import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class CGPA_Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.credit_label = QLabel("Enter credit hours:")
        self.grade_label = QLabel("Enter grade points:")

        self.credit_input = QLineEdit()
        self.grade_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate CGPA")
        self.calculate_button.clicked.connect(self.calculate_cgpa)

        self.layout.addWidget(self.credit_label)
        self.layout.addWidget(self.credit_input)
        self.layout.addWidget(self.grade_label)
        self.layout.addWidget(self.grade_input)
        self.layout.addWidget(self.calculate_button)

        self.setWindowTitle("CGPA Calculator")
        self.show()

    def calculate_cgpa(self):
        try:
            credit_hours = float(self.credit_input.text())
            grade_points = float(self.grade_input.text())

            if credit_hours <= 0 or grade_points < 0:
                raise ValueError("Credit hours and grade points must be positive.")

            cgpa = grade_points / credit_hours

            QMessageBox.information(self, "CGPA Calculator", f"Your CGPA is {cgpa:.2f}.")

        except ValueError as e:
            QMessageBox.critical(self, "CGPA Calculator", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    calculator = CGPA_Calculator()

    sys.exit(app.exec_())'''
    
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QMessageBox

def calculate_gpa(course_grades, course_units):
    total_course_points = 0
    total_course_units = sum(course_units)
    grade_to_points = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}
    for grade, units in zip(course_grades, course_units):
        total_course_points += grade_to_points[grade] * units
    if total_course_units == 0:
        return 0.0
    return total_course_points / total_course_units

def calculate_cgpa(semester_gpas, total_course_units):
    total_course_points = 0
    for semester_gpa, course_units in zip(semester_gpas, total_course_units):
        total_course_points += semester_gpa * sum(course_units)
    if total_course_units == 0:
        return 0.0
    return total_course_points / sum(total_course_units)

class GPAcalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('GPA and CGPA Calculator')
        self.setGeometry(300, 300, 400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.num_courses_label = QLabel('Enter the number of courses:')
        layout.addWidget(self.num_courses_label)

        self.num_courses_input = QLineEdit()
        layout.addWidget(self.num_courses_input)

        self.calculate_gpa_button = QPushButton('Calculate Semester GPA')
        self.calculate_gpa_button.clicked.connect(self.calculate_gpa_clicked)
        layout.addWidget(self.calculate_gpa_button)

        self.semester_gpas = []
        self.total_course_units = []

        self.cgpa_label = QLabel('CGPA:')
        layout.addWidget(self.cgpa_label)

        self.cgpa_value = QLabel('0.0')
        layout.addWidget(self.cgpa_value)

        self.calculate_cgpa_button = QPushButton('Calculate CGPA')
        self.calculate_cgpa_button.clicked.connect(self.calculate_cgpa_clicked)
        layout.addWidget(self.calculate_cgpa_button)

    def calculate_gpa_clicked(self):
        num_courses = int(self.num_courses_input.text())
        course_grades = []
        course_units = []
        for i in range(num_courses):
            grade_input = QLineEdit()
            grade_label = QLabel(f'Enter grade for course {i+1}:')
            grade_layout = QHBoxLayout()
            grade_layout.addWidget(grade_label)
            grade_layout.addWidget(grade_input)

            units_input = QLineEdit()
            units_label = QLabel(f'Enter units for course {i+1}:')
            units_layout = QHBoxLayout()
            units_layout.addWidget(units_label)
            units_layout.addWidget(units_input)

            layout = QVBoxLayout()
            layout.addLayout(grade_layout)
            layout.addLayout(units_layout)

            grade_and_units_widget = QWidget()
            grade_and_units_widget.setLayout(layout)

            self.layout().addWidget(grade_and_units_widget)

            course_grades.append(grade_input.text())
            course_units.append(int(units_input.text()))

        semester_gpa = calculate_gpa(course_grades, course_units)
        self.semester_gpas.append(semester_gpa)
        self.total_course_units.append(sum(course_units))

        self.cgpa_value.setText(str(calculate_cgpa(self.semester_gpas, self.total_course_units)))

    def calculate_cgpa_clicked(self):
        num_semesters = int(QInputDialog.getText(self, 'Number of Semesters', 'Enter the number of semesters:'))
        for i in range(num_semesters - len(self.semester_gpas)):
            self.calculate_gpa_clicked()

        self.cgpa_value.setText(str(calculate_cgpa(self.semester_gpas, self.total_course_units)))

app = QApplication(sys.argv)
ex = GPAcalculator()
ex.show()
sys.exit(app.exec_())