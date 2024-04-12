class Doctor:
  def __init__(self, name, especialidad):
      self.name = name
      self.especialidad = especialidad

class Patient:
  def __init__(self, name, sintomas):
      self.name = name
      self.sintomas = sintomas

class AppointmentSystem:
  def __init__(self):
      self.doctores = []
      self.pacientes = []

  def agregar_doctores(self, doctor):
      self.doctores.append(doctor)

  def add_patient(self, paciente):
      self.pacientes.append(paciente)

  def mostrar_doctores(self):
      print("Lista de médicos disponibles:")
      for idx, doctor in enumerate(self.doctores):
          print(f"{idx + 1}. {doctor.name} - {doctor.especialidad}")

  def schedule_appointment(self, doctor_idx, paciente_idx):
      doctor = self.doctores[doctor_idx - 1]
      paciente = self.pacientes[paciente_idx - 1]
      print(f"Cita programada: {paciente.name} con el Dr. {doctor.name}")

  def analizar_sintomas(self, sintomas):
      print("Análisis del paciente:")
      print(f"Síntomas proporcionados: {sintomas}")

appointment_system = AppointmentSystem()

doctor1 = Doctor("Dr. García", "Pediatría")
doctor2 = Doctor("Dr. Martínez" , "Cardiología")
appointment_system.agregar_doctores(doctor1)
appointment_system.agregar_doctores(doctor2)

paciente1 = Patient("Juan", "Fiebre y dolor de garganta")
paaciente2 = Patient("María", "Dolor en el pecho y dificultad para respirar")
appointment_system.add_patient(paciente1)
appointment_system.add_patient(paaciente2)

appointment_system.mostrar_doctores()
doctor_choice = int(input("Seleccione el numero del médico: "))
appointment_system.analizar_sintomas(paciente1.sintomas)
appointment_system.schedule_appointment(doctor_choice, 1)
