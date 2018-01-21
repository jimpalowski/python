class Patient:
	def __init__(self, name, allergies, bed_number=None):
		self.name = name
		self.bed_number = bed_number
		self.allergies = allergies
		self.id =id(self)
                   
	def display(self):
		print "Name: " + self.name
		print "Bed number: " + str(self.bed_number)
		print "ID: " + str(self.id)
		for allergy in self.allergies:
			print "Allergy: " + allergy
		return self

class Hospital:
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = []

	def display(self):
		print "Name: " + self.name
		print "Capacity: " + str(self.capacity)
		for patient in self.patients:
			patient.display()
		return self

	def admit(self, name, allergies, bed_number=None):
		if len(self.patients) >= self.capacity:
			return "No room"
		else:
			patient = Patient(name, allergies, bed_number)
			self.patients.append(patient)
			return "Admitted"

	def discharge(self, name):
		return_text = ""
		for patient in self.patients:
			if patient.name == name:
				patient.bed_number = None
				patient_index = self.patients.index(patient)
				self.patients.pop(patient_index)
				return_text = name + " discharged."
			else:
				return_text = name + " was not found."
		return return_text

hospital = Hospital("Bad Samaritan", 3)
print hospital.admit("Bruce", [], "1A")
print hospital.admit("John", ['nuts', 'shellfish'], "2A")
print hospital.admit("Frank", ['penicillin'])
print hospital.admit("Tom", ['penicillin', 'nuts', 'shellfish'], "3A")
hospital.display()
print hospital.discharge("John")
print hospital.admit("Tom", ['penicillin', 'nuts', 'shellfish'], "3A")
hospital.display()