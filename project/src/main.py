try:
    from .simulation import run_simulation
except ImportError:
    from simulation import run_simulation


def main() -> None:
    try:
        steps_input = input("Введите количество шагов симуляции (по умолчанию 20): ").strip()
        if steps_input:
            steps = int(steps_input)
            if steps <= 0:
                print("Количество шагов должно быть положительным числом")
                return
        else:
            steps = 20
        
        seed_input = input("Введите seed для генератора случайных чисел (опционально, Enter для пропуска): ").strip()
        seed = int(seed_input) if seed_input else None
    except ValueError:
        print("Ошибка: введите целое число")
        return
    
    run_simulation(steps=steps, seed=seed)


if __name__ == "__main__":
    main()
