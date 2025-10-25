class Mecanico:
    
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Mecánico {self.nombre} listo para comenzar el lavado.")

    def iniciar_limpieza(self, maquina):
        print(f"\n{self.nombre} está preparando la máquina de lavado...")
        maquina.encender()
        print(f"{self.nombre} ha configurado la máquina para el carro.")
        
    def finalizar_proceso(self, maquina):
        print(f"\n{self.nombre} está revisando el resultado de la limpieza...")
        maquina.mostrar_estado()
        print(f"Proceso de limpieza finalizado por {self.nombre}.")