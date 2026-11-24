"""Калькулятор энергопотребления серверной стойки."""


def rack_power(servers: int, watts_per_server: float) -> float:
    """Суммарная мощность стойки, кВт."""
    if servers < 0 or watts_per_server < 0:
        raise ValueError("значения должны быть неотрицательными")
    return servers * watts_per_server / 1000


if __name__ == "__main__":
    print(f"Стойка 42U, 20 серверов по 450 Вт: {rack_power(20, 450):.1f} кВт")


def rack_heat_btu(power_kw: float) -> float:
    """Тепловыделение стойки, BTU/ч (1 кВт = 3412 BTU/ч)."""
    return power_kw * 3412
