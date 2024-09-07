import pytest
from robot import Robot 

@pytest.fixture
def robot():
    return Robot("Arturito","R2D2")

@pytest.mark.parametrize("minutos_carga, nivel_bateria, velocidad_carga, nivel_bateria_esperado", [
    (1, 0, 1, 1),
    (22, 0, 1, 22),
    (10, 56, 1, 66),
    (15, 65, 2, 95),
    (0, 0, 1, ValueError),
    (-1, 23, 1, ValueError),
    (60, 90, 5, 100),
    (10, 0, 10, 100)
])
def test_metodo_cargar_bateria(robot, minutos_carga, nivel_bateria, velocidad_carga, nivel_bateria_esperado):
    robot.set_bateria(nivel_bateria)
    robot.set_velocidad_carga(velocidad_carga)
    
    if nivel_bateria_esperado == ValueError:
        with pytest.raises(ValueError):
            robot.cargar_bateria(minutos_carga)
    else:
        robot.cargar_bateria(minutos_carga)
        assert robot.get_nivel_bateria() == nivel_bateria_esperado

@pytest.mark.parametrize("nivel_bateria, minutos_trabajo, consumo, minutos_trabajo_esperados", [
    (100, 1, 1, 1),
    (100, 99, 1, 99),
    (100, 100, 1, 100),
    (100, 101, 1, 100),
    (10, 15, 5, 2),
    (100, -1, 1, ValueError)

])

def test_metodo_trabajar(robot, nivel_bateria, minutos_trabajo, consumo, minutos_trabajo_esperados):
    robot.set_bateria(nivel_bateria)
    robot.set_consumo(consumo)

    if minutos_trabajo_esperados == ValueError:
        with pytest.raises(ValueError):
            robot.trabajar(minutos_trabajo)
    else:
        if nivel_bateria < (consumo * minutos_trabajo):
            robot.trabajar(minutos_trabajo)
            assert nivel_bateria / consumo == minutos_trabajo_esperados
        
        else:
            assert minutos_trabajo == minutos_trabajo_esperados


@pytest.mark.parametrize("nivel_bateria, estado, velocidad_prendido_apagado, velocidad_esperada", [
    (100, True, 20, 5),
    (100, True, 100, 1),
    (100, True, 5, 20),
    (0, False, 100, ValueError),

])

def test_velocidad_cambio_apagado_prendido(robot, nivel_bateria, estado, velocidad_prendido_apagado, velocidad_esperada):
    robot.set_bateria(nivel_bateria)
    robot.set_estado(estado)
    robot.set_velocidad_prendido_apagado(velocidad_prendido_apagado)

    if velocidad_esperada == ValueError:
        with pytest.raises(ValueError):
            robot.cambiar_estado()
    else:
        assert robot.cambiar_estado() == velocidad_esperada