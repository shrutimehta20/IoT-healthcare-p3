import datetime

class VitalSignsRecord:
    def _init_(self, date, systolic, diastolic, pulse, temperature, oxygen_level):
        self.date = date
        self.systolic = systolic
        self.diastolic = diastolic
        self.pulse = pulse
        self.temperature = temperature
        self.oxygen_level = oxygen_level

class EmergencyContact:
    def _init_(self, name, phone):
        self.name = name
        self.phone = phone

class HealthGoal:
    def _init_(self, name, target_value):
        self.name = name
        self.target_value = target_value

class Symptom:
    def _init_(self, name, description, date):
        self.name = name
        self.description = description
        self.date = date

class JournalEntry:
    def _init_(self, date, entry, emotion):
        self.date = date
        self.entry = entry
        self.emotion = emotion

class VitalSignsMonitor:
    def _init_(self):
        self.records = []
        self.emergency_contacts = []
        self.appointments = []
        self.health_goals = []
        self.symptoms = []  # List to store symptoms
        self.journal_entries = []

    def add_emergency_contact(self, name, phone):
        contact = EmergencyContact(name, phone)
        self.emergency_contacts.append(contact)

    def add_appointment(self, name, month, day, hour, minute):
        appointment = (name, month, day, hour, minute)
        self.appointments.append(appointment)

    def add_health_goal(self, name, target_value):
        goal = HealthGoal(name, target_value)
        self.health_goals.append(goal)

    def add_record(self, date, systolic, diastolic, pulse, temperature, oxygen_level):
        record = VitalSignsRecord(date, systolic, diastolic, pulse, temperature, oxygen_level)
        self.records.append(record)
        if len(self.records) > 10:
            self.records.pop(0)  # Remove the oldest record

    def get_last_10_records(self):
        return self.records

    def check_vital_signs(self):
        try:
            date = input("Enter the date (e.g., 2023-10-13): ")
            systolic = float(input("Enter systolic blood pressure (mmHg): "))
            diastolic = float(input("Enter diastolic blood pressure (mmHg): "))
            pulse = int(input("Enter pulse rate (bpm): "))
            temperature = float(input("Enter body temperature (°C): "))
            oxygen_level = float(input("Enter oxygen level (%): "))
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            return

        # Check and print whether vital signs are low, high, or normal
        self.check_vital_range("Systolic Blood Pressure", systolic, 90, 120, 140)
        self.check_vital_range("Diastolic Blood Pressure", diastolic, 60, 80, 90)
        self.check_vital_range("Pulse Rate", pulse, 60, 100, 120)
        self.check_vital_range("Temperature", temperature, 36, 37, 38)
        self.check_vital_range("Oxygen Level", oxygen_level, 90, 95, 100)

        self.add_record(date, systolic, diastolic, pulse, temperature, oxygen_level)

        print("Last 10 Vital Signs Records:")
        for record in self.get_last_10_records():
            print(f"Date: {record.date}, Systolic: {record.systolic}, Diastolic: {record.diastolic}, Pulse: {record.pulse}, Temperature: {record.temperature}°C, Oxygen Level: {record.oxygen_level}%")

    def check_vital_range(self, name, value, low, normal_low, normal_high):
        if value < low:
            print(f"{name} is low.")
        elif low <= value < normal_low:
            print(f"{name} is below normal.")
        elif normal_low <= value <= normal_high:
            print(f"{name} is within normal range.")
        else:
            print(f"{name} is high.")

    def display_emergency_contacts(self):
        if self.emergency_contacts:
            print("Emergency Contacts:")
            for contact in self.emergency_contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No emergency contacts found.")

    def check_appointments(self):
        if self.appointments:
            current_time = datetime.datetime.now()
            next_appointment = None
            for appointment in self.appointments:
                name, month, day, hour, minute = appointment
                appointment_time = datetime.datetime(current_time.year, month, day, hour, minute)
                if appointment_time >= current_time:
                    if next_appointment is None or appointment_time < next_appointment[1]:
                        next_appointment = (name, appointment_time)

            if next_appointment:
                name, appointment_time = next_appointment
                print(f"Next appointment is scheduled for {appointment_time.strftime('%Y-%m-%d %H:%M')} with {name}!")
            else:
                print("No upcoming appointments.")
        else:
            print("No appointments in the system.")

    def display_health_goals(self):
        if self.health_goals:
            print("Health Goals:")
            for goal in self.health_goals:
                print(f"Goal: {goal.name}, Target Value: {goal.target_value}")
        else:
            print("No health goals set.")

    def add_symptom(self, name, description, date):
        symptom = Symptom(name, description, date)
        self.symptoms.append(symptom)
        print("Symptom added successfully!")

    def display_symptoms(self):
        if self.symptoms:
            print("Symptoms Tracked:")
            for symptom in self.symptoms:
                print(f"Name: {symptom.name}, Description: {symptom.description}, Date: {symptom.date}")
        else:
            print("No symptoms tracked.")

    def add_journal_entry(self, date, entry, emotion):
        journal_entry = JournalEntry(date, entry, emotion)
        self.journal_entries.append(journal_entry)
        print("Journal entry added successfully!")

    def display_journal_entries(self):
        if self.journal_entries:
            print("Journal Entries:")
            for entry in self.journal_entries:
                print(f"Date: {entry.date}, Emotion: {entry.emotion}")
                print(entry.entry)
        else:
            print("No journal entries available.")

def add_predefined_symptoms(monitor, disease_name):
    predefined_symptoms = {
        "Common Cold": ["Runny or stuffy nose", "Sneezing", "Coughing", "Sore throat", "Mild headache"],
        "Influenza (Flu)": ["High fever", "Chills", "Muscle aches", "Fatigue", "Cough"],
        "COVID-19": ["Fever", "Dry cough", "Shortness of breath", "Loss of taste or smell", "Sore throat"],
        "Asthma": ["Shortness of breath", "Wheezing", "Coughing", "Chest tightness", "Difficulty sleeping"],
        "Diabetes": ["Frequent urination", "Excessive thirst", "Fatigue", "Blurred vision", "Slow wound healing"],
        "Hypertension (High Blood Pressure)": ["Headaches", "Dizziness", "Chest pain", "Shortness of breath", "Visual changes"],
        "Migraine": ["Severe headache", "Nausea", "Vomiting", "Sensitivity to light", "Sensitivity to sound"],
        "Allergies": ["Sneezing", "Runny nose", "Itchy or watery eyes", "Skin rashes", "Coughing"],
        "Gastroenteritis (Stomach Flu)": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Fever"],
        "Osteoarthritis": ["Joint pain", "Stiffness", "Swelling", "Reduced range of motion", "Crepitus (joint cracking)"]
        # Add more diseases and their symptoms as needed
    }
    if disease_name in predefined_symptoms:
        symptoms = predefined_symptoms[disease_name]
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        for symptom in symptoms:
            monitor.add_symptom(disease_name, symptom, current_date)
    else:
        print("Disease not found in the predefined list.")

if __name__ == "__main__":
    monitor = VitalSignsMonitor()

    while True:
        print("\nOptions:")
        print("1. Check Vital Signs")
        print("2. Display Emergency Contacts")
        print("3. Check Appointments")
        print("4. Set Emergency Contact")
        print("5. Set Appointment")
        print("6. Display Health Goals")
        print("7. Set Health Goal")
        print("8. Track Symptoms")
        print("9. Add Journal Entry")
        print("10. View Journal Entries")
        print("11. Display Symptoms")
        print("12. Add Predefined Symptoms")
        print("13. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/13): ")

        if choice == "1":
            monitor.check_vital_signs()
        elif choice == "2":
            monitor.display_emergency_contacts()
        elif choice == "3":
            monitor.check_appointments()
        elif choice == "4":
            name = input("Enter the name of the emergency contact: ")
            phone = input("Enter the phone number: ")
            monitor.add_emergency_contact(name, phone)
        elif choice == "5":
            name = input("Enter the name of the appointment: ")
            month = int(input("Enter the month (1-12): "))
            day = int(input("Enter the day (1-31): "))
            hour = int(input("Enter the hour (0-23): "))
            minute = int(input("Enter the minute (0-59): "))
            monitor.add_appointment(name, month, day, hour, minute)
        elif choice == "6":
            monitor.display_health_goals()
        elif choice == "7":
            name = input("Enter the name of the health goal: ")
            target_value = float(input("Enter the target value: "))
            monitor.add_health_goal(name, target_value)
        elif choice == "8":
            monitor.display_symptoms()
        elif choice == "9":
            date = input("Enter the date (e.g., 2023-10-13): ")
            entry = input("Enter your journal entry: ")
            emotion = input("Enter your emotion: ")
            monitor.add_journal_entry(date, entry, emotion)
        elif choice == "10":
            monitor.display_journal_entries()
        elif choice == "11":
            monitor.display_symptoms()
        elif choice == "12":
            disease_name = input("Enter the name of the disease: ")
            add_predefined_symptoms(monitor, disease_name)
        elif choice == "13":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
