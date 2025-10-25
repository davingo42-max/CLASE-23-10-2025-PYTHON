class Carro:
    
    def __init__(self, modelo, placa, kilometraje):
        self.modelo = modelo
        self.placa = placa
        self.kilometraje = kilometraje
        print(f"Carro {self.modelo} (Placa: {self.placa}, KM: {self.kilometraje}) ingresando a la zona de lavado.")

    def estacionar(self):
        print(f"El carro {self.modelo} está posicionado y listo para el lavado.")
        
    def salir_del_taller(self):
        print(f"El carro {self.modelo} está saliendo de la zona de lavado. ¡Carro limpio!")
    
    def __init__(self, modelo, placa, kilometraje):
        self.modelo = modelo
        self.placa = placa
        self.kilometraje = kilometraje
        print(f"Carro {self.modelo} (Placa: {self.placa}, KM: {self.kilometraje}) ingresando al taller.")

    def estacionar(self):
        print(f"El carro {self.modelo} está estacionado y listo para el diagnóstico.")
        
    def salir_del_taller(self):
        print(f"El carro {self.modelo} está saliendo del taller. ¡Hasta pronto!")