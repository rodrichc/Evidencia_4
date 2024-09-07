-- CREACION DE LA BASE DE DATOS
CREATE DATABASE IF NOT EXISTS Robot;
USE Robot;

-- CREACIÓN DE LAS TABLAS
CREATE TABLE IF NOT EXISTS Robots (
    id_robot INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(15) NOT NULL,
    modelo VARCHAR(10) NOT NULL,
    consumo FLOAT(4,2) DEFAULT 0.7, -- Porcentaje de consumo por minuto
    bateria FLOAT(6,2) DEFAULT 0.0, -- Nivel de batería en porcentaje
    velocidad_carga FLOAT(5,2) DEFAULT 1.0, -- Porcentaje de carga por minuto
    velocidad_prendido_apagado FLOAT(6,2) DEFAULT 20.0, -- Porcentaje de prendido/apagado por segundo
    estado BOOLEAN DEFAULT FALSE -- 0: Apagado, 1: Encendido
);

CREATE TABLE IF NOT EXISTS HistorialCarga (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_robot INT,
    minutos_carga INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_robot) REFERENCES Robots(id_robot)
);

CREATE TABLE IF NOT EXISTS HistorialTrabajo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_robot INT,
    minutos_trabajo INT NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_robot) REFERENCES Robots(id_robot)
    );
   
   
   
-- INSERTS
	-- INSERT DE TODOS LOS ATRIBUTOS DE ROBOT:
INSERT INTO Robots (nombre, modelo, consumo, bateria, velocidad_carga, velocidad_prendido_apagado, estado) 
VALUES 
('Arturito', 'R2D2', 0.7, 100.0, 2.2, 25.1, TRUE),
('Optimus', 'Peterbilt', 0.5, 80.0, 1.0, 15.0, FALSE),
('Wall-E', 'RK2', 0.9, 60.0, 4.0, 40.3, TRUE);
	 
     -- INSERT DE LOS ATRIBUTOS DE LOS DATOS QUE NO TIENEN UN VALOR POR DEFECTO:
INSERT INTO Robots (nombre, modelo) 
VALUES 
('Nexus', 'A23Ñ'),
('Trip', '8A9'),
('Ropx', 'C2T1');


	-- INSERT EN HistorialCarga:
INSERT INTO HistorialCarga (id_robot, minutos_carga)
VALUES
(1, 30),
(2, 45),
(2, 55);

	
    -- INSERT EN HistorialTrabajo:
INSERT INTO HistorialTrabajo (id_robot, minutos_trabajo)
VALUES
(3, 10),
(2, 20),
(1, 45);

-- SELECT
	-- SELECT DE LAS TABLAS COMPLETAS:
SELECT * FROM Robots;
SELECT * FROM HistorialCarga;
SELECT * FROM HistorialTrabajo;

	-- SELECT DE COLUMNAS ESPECÍFICAS:
SELECT * FROM Robots;
SELECT nombre, modelo, bateria FROM Robots;
SELECT id_robot, minutos_trabajo, fecha FROM HistorialTrabajo;
SELECT id_robot, minutos_carga, fecha FROM HistorialCarga;
