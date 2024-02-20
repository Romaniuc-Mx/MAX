import datetime

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.faculty = []
        self.log = []

    def log_operation(self, operation, details):
        timestamp = datetime.datetime.now()
        log_entry = f"{timestamp}: {operation} - {details}"
        self.log.append(log_entry)

    def create_student(self, student_name, student_email):
        self.students.append({'name': student_name, 'email': student_email})
        self.log_operation("Create Student", f"Student: {student_name}, Email: {student_email}")

    def graduate_student(self, student_email):
        if any(student['email'] == student_email for student in self.students):
            self.students = [student for student in self.students if student['email'] != student_email]
            self.log_operation("Graduate Student", f"Student with Email: {student_email}")
        else:
            self.log_operation("Error", f"Can't graduate student: {student_email} (student not present)")

    def create_faculty(self, faculty_name):
        self.faculty.append({'name': faculty_name})
        self.log_operation("Create Faculty", f"Faculty: {faculty_name}")

    def batch_enrollment(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                student_name, student_email = map(str.strip, line.split(','))
                self.create_student(student_name, student_email)

    def batch_graduation(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                student_email = line.strip()
                self.graduate_student(student_email)

# Example usage
sms = StudentManagementSystem()
sms.create_student("John Doe", "john.doe@example.com")
sms.create_faculty("Math Department")
sms.batch_enrollment("enrollment_list.txt")
sms.batch_graduation("graduation_list.txt")

for entry in sms.log:
    print(entry)