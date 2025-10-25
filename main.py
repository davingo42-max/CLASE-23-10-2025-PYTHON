from mecanico import Mecanico
from maquina import Maquina
from carro import Carro

def obtener_datos_carro():
    print("\n--- INGRESO DE DATOS DEL VEHÍCULO ---")
    modelo = input("Ingrese el modelo del carro (Ej: BMW X5): ")
    placa = input("Ingrese el número de placa (Ej: XYZ-789): ")
    
    while True:
        try:
            kilometraje_str = input("Ingrese el kilometraje actual (en km): ")
            kilometraje = int(kilometraje_str)
            break
        except ValueError:
            print("Error: El kilometraje debe ser un número entero. Intente de nuevo.")
            
    return modelo, placa, kilometraje

def main():
    print("--- INICIO DE LA SIMULACIÓN DE LAVADO DE CARRO ---")

    modelo, placa, kilometraje = obtener_datos_carro()

    print("\n--- PREPARANDO EL PROCESO DE LAVADO ---")
    mecanico_principal = Mecanico("Juan Perez")
    maquina_lavado = Maquina()
    
    carro_cliente = Carro(modelo, placa, kilometraje)

    carro_cliente.estacionar()

    mecanico_principal.iniciar_limpieza(maquina_lavado)

    maquina_lavado.realizar_limpieza(carro_cliente)

    mecanico_principal.finalizar_proceso(maquina_lavado)
    
    carro_cliente.salir_del_taller()

    print("\n--- FIN DE LA SIMULACIÓN ---")

if __name__ == "__main__":
    main()