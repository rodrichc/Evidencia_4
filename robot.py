class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre
        self.modelo = modelo
        self.__consumo = 2 #porcentaje de consumo por minuto
        self.__nivel_bateria = 0.0 #%
        self.__velocidad_carga = 1 # % por minuto
        self.__estado = False #encendido o apagado
        self.__velocidad_prendido_apagado = 20 #% por segundo

#MÉTODO ESPECIAL
    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Modelo: {self.modelo}\n"
                f"Estado: {"Encendido" if self.__estado else "Apagado"}\n"
                f"Nivel de Batería: {self.__nivel_bateria}%\n"
                f"Velocidad de Carga: {self.__velocidad_carga}% por minuto\n"
                f"Consumo: {self.__consumo}% por minuto\n"
                f"Velocidad prendido/apagado: {self.__velocidad_prendido_apagado}% por segundo"
                )

#METODOS
    
    def cargar_bateria(self, minutos_carga):
        if minutos_carga > 0:
            self.__nivel_bateria +=  (minutos_carga * self.__velocidad_carga)
            if self.__nivel_bateria >= 100:
                self.__nivel_bateria = 100
            return f"{self.nombre} ha cargado a un {self.__nivel_bateria}%"
        else:
            raise ValueError("Solo números mayores a 0")

    
    def trabajar(self, minutos):
        if minutos >= 0:
            consumo_total = self.__consumo * minutos
            if self.__nivel_bateria < consumo_total:
                minutos_trabajados = self.__nivel_bateria / self.__consumo
                self.__nivel_bateria = 0
                return f"{self.nombre} trabajo solamente por {round(minutos_trabajados)} minutos por falta de batería."
            else:
                self.__nivel_bateria -= consumo_total
                return f"{self.nombre} ha trabajado por {minutos} minutos."
        else:
            raise ValueError("Los minutos a trabajar deben ser un numero positivo.")
        
    def cambiar_estado(self):
        tiempo_cambiando_estado = 100 / self.__velocidad_prendido_apagado
        if self.__estado == True:
            self.__estado = False
            return tiempo_cambiando_estado
        elif self.__estado == False and self.__nivel_bateria > 0:
            self.__estado = True
            return tiempo_cambiando_estado
        else:
            raise ValueError("Batería insuficiente")
        
        
#GETTERS
    def get_nombre(self):
        return self.nombre

    def get_modelo(self):
        return self.modelo

    def get_consumo(self):
        return self.__consumo
    
    def get_nivel_bateria(self):
        return self.__nivel_bateria
    
    def get_velocidad_carga(self):
        return self.__velocidad_carga
    
    def get_estado(self):
        return self.__estado

    def get_velocidad_prendido_apagado(self):
        return self.__velocidad_prendido_apagado    
    
#SETTERS
    def set_nombre(self, nombre):
        self.nombre = nombre
        return f"Se ha cambiado el nombre a {self.nombre}"

    def set_modelo(self, modelo):
        self.modelo = modelo
        return f"Se ha cambiado el modelo a {self.modelo}"
    
    def set_consumo(self, consumo):
        if 1 <= consumo <= 5:
            self.__consumo = consumo
            return f"Se ha restablecido el consumo a: {self.__consumo}% por minuto."
        else:
            raise ValueError("El consumo a establecer debe ser de 1 a 5")

    def set_velocidad_carga(self, velocidad_carga):
        if 1 <= velocidad_carga <= 10:
            self.__velocidad_carga = velocidad_carga
            return f"Se ha restablecido la velocidad de carga a: {self.__velocidad_carga}% por minuto."
        else:
            raise ValueError("La velocidad de carga a establecer debe ser de 2 a 10")

    def set_bateria(self, bateria):
        if 0 <= bateria <= 100:
            self.__nivel_bateria = bateria    
        else:
            raise ValueError("El nivel de batería debe de 0 a 100.")
        
    def set_estado(self, estado):
        if isinstance(estado, bool):
            self.__estado = estado
        else:
            raise ValueError("El estado debe ser Booleano")
        
    def set_velocidad_prendido_apagado(self, velocidad):
        if 1 <= velocidad <= 120:
            self.__velocidad_prendido_apagado = velocidad
        else:
            raise ValueError("La velocidad debe ser un numero de 1 a 120")
        
