from enum import Enum
from datetime import date

class StudyField(Enum):
    MECHANICAL_ENGINEERING = 1
    SOFTWARE_ENGINEERING = 2
    FOOD_TECHNOLOGY = 3
    URBANISM_ARCHITECTURE = 4
    VETERINARY_MEDICINE = 5

class Student:
    def __init__(self, first_name, last_name, email, enrollment_date, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.enrollment_date = enrollment_date
        self.date_of_birth = date_of_birth

class Faculty:
    def __init__(self, name, abbreviation, study_field):
        self.name = name
        self.abbreviation = abbreviation
        self.study_field = study_field
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def graduate_student(self, student):
        if student in self.students:
            self.students.remove(student)

class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, name, abbreviation, study_field):
        new_faculty = Faculty(name, abbreviation, study_field)
        self.faculties.append(new_faculty)
        return new_faculty

    def search_faculty_by_student_identifier(self, identifier):
        for faculty in self.faculties:
            for student in faculty.students:
                if student.email == identifier:
                    return faculty
        return None

    def display_all_faculties(self):
        for faculty in self.faculties:
            print(f"{faculty.name} ({faculty.abbreviation}) - {faculty.study_field.name}")

    def display_faculties_by_field(self, study_field):
        matching_faculties = [faculty for faculty in self.faculties if faculty.study_field == study_field]
        for faculty in matching_faculties:
            print(f"{faculty.name} ({faculty.abbreviation}) - {faculty.study_field.name}")

    def display_current_enrolled_students(self):
        for faculty in self.faculties:
            print(f"\n{faculty.name} ({faculty.abbreviation}) - {faculty.study_field.name}")
            for student in faculty.students:
                print(f"{student.first_name} {student.last_name} ({student.email})")

    def display_graduates(self):
        for faculty in self.faculties:
            print(f"\n{faculty.name} ({faculty.abbreviation}) - {faculty.study_field.name}")
            for student in faculty.students:
                print(f"{student.first_name} {student.last_name} ({student.email})")

university = University()

while True:
    print("\n===== TUM Student Management System =====")
    print("Faculty Operations:")
    print("1. Create and assign a student to a faculty.")
    print("2. Graduate a student from a faculty.")
    print("3. Display current enrolled students.")
    print("4. Display graduates.")
    print("5. Check if a student belongs to a faculty.")
    print("\nGeneral Operations:")
    print("6. Create a new faculty.")
    print("7. Search what faculty a student belongs to by email.")
    print("8. Display University faculties.")
    print("9. Display faculties belonging to a field.")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        email = input("Enter student's email: ")
        enrollment_date = date.today()
        date_of_birth = input("Enter student's date of birth (YYYY-MM-DD): ")
        student = Student(first_name, last_name, email, enrollment_date, date_of_birth)

        print("\nAvailable Faculties:")
        university.display_all_faculties()
        faculty_name = input("Enter the name of the faculty to assign the student: ")
        matching_faculties = [faculty for faculty in university.faculties if faculty.name == faculty_name]
        
        if matching_faculties:
            matching_faculties[0].add_student(student)
            print(f"\n{student.first_name} {student.last_name} ({student.email}) assigned to {faculty_name}.")
        else:
            print(f"\nFaculty '{faculty_name}' not found.")

    elif choice == '2':
        email = input("Enter student's email to graduate: ")
        faculty = university.search_faculty_by_student_identifier(email)

        if faculty:
            matching_students = [student for student in faculty.students if student.email == email]
            if matching_students:
                faculty.graduate_student(matching_students[0])
                print(f"\n{matching_students[0].first_name} {matching_students[0].last_name} ({email}) graduated from {faculty.name}.")
            else:
                print(f"\nStudent with email '{email}' not found in {faculty.name}.")
        else:
            print(f"\nStudent with email '{email}' not found in any faculty.")

    elif choice == '3':
        print("\nCurrent Enrolled Students:")
        university.display_current_enrolled_students()

    elif choice == '4':
        print("\nGraduates:")
        university.display_graduates()

    elif choice == '5':
        email = input("Enter student's email to check if they belong to a faculty: ")
        faculty = university.search_faculty_by_student_identifier(email)
        if faculty:
            print(f"\n{email} belongs to {faculty.name} ({faculty.abbreviation}).")
        else:
            print(f"\n{email} does not belong to any faculty.")

    elif choice == '6':
        name = input("Enter new faculty name: ")
        abbreviation = input("Enter new faculty abbreviation: ")
        print("\nAvailable Study Fields:")
        for field in StudyField:
            print(f"{field.name}")
        field_input = input("Enter the study field for the new faculty: ")
        if field_input in StudyField.__members__:
            study_field = StudyField[field_input]
            new_faculty = university.create_faculty(name, abbreviation, study_field)
            print(f"\nNew faculty created: {new_faculty.name} ({new_faculty.abbreviation}) - {new_faculty.study_field.name}.")
        else:
            print("Invalid study field.")

    elif choice == '7':
        email = input("Enter student's email to search for the faculty: ")
        faculty = university.search_faculty_by_student_identifier(email)
        if faculty:
            print(f"\n{email} belongs to {faculty.name} ({faculty.abbreviation}).")
        else:
            print(f"\nStudent with email '{email}' not found in any faculty.")

    elif choice == '8':
        print("\nUniversity Faculties:")
        university.display_all_faculties()

    elif choice == '9':
        print("\nAvailable Study Fields:")
        for field in StudyField:
            print(f"{field.name}")
        field_input = input("Enter the study field to display faculties: ")
        if field_input in StudyField.__members__:
            study_field = StudyField[field_input]
            print(f"\nFaculties belonging to {study_field.name}:")
            university.display_faculties_by_field(study_field)
        else:
            print("Invalid study field.")

    elif choice == '0':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
