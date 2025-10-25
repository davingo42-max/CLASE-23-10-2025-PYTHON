class Maquina:
    
    def __init__(self):
        self.encendida = False
        self.estado_limpieza = "Pendiente"
        print("Máquina de Lavado Automático inicializada.")

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print("Máquina de lavado encendida.")
        else:
            print("Máquina de lavado ya estaba encendida.")

    def realizar_limpieza(self, carro):
        if self.encendida:
            print(f"Iniciando ciclo de lavado para el carro: {carro.modelo}...")
            if carro.kilometraje < 50000:
                self.estado_limpieza = "Excelente - Lavado estándar completado."
            else:
                self.estado_limpieza = "Bueno - Lavado con cera y pulido completado."
            print("Lavado, enjuague y secado completados.")
        else:
            print("Error: La máquina debe estar encendida para realizar la limpieza.")

    def mostrar_estado(self):
        print(f"\n--- Resultados del Ciclo de Limpieza ---")
        print(f"Estado de la Limpieza: {self.estado_limpieza}")
        print("---------------------------------------")