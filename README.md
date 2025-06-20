# ShapeInheritance на Python

Цей репозиторій містить проект на Python, який реалізує **ієрархію класів для різних геометричних фігур**. Проект демонструє ключові принципи **об'єктно-орієнтованого програмування (ООП)**, такі як **успадкування**, **поліморфізм** та **інкапсуляція**.

-----

## 🏗️ Структура Проекту

Проект побудований на базі абстрактного класу `Shape`, від якого успадковуються конкретні геометричні фігури.

  * **`Shape`**: Базовий клас, що визначає загальні атрибути (`color`) та методи (`get_color`, `set_color`, `describe`). Також реалізує **перевантаження операторів** (`<`, `>`, `==`) для порівняння фігур за їхньою площею.
  * **`Circle`**: Представляє коло. Має властивості `radius`, `space`, `center` та методи для обчислення `area`, `perimeter`, `diameter`, а також `move_center`.
  * **`Rectangle`**: Представляє прямокутник. Має властивості `width`, `height`, `position` та методи для обчислення `area`, `perimeter`, перевірки `is_square` та `move`.
  * **`Triangle`**: Представляє трикутник. Має властивості `side1`, `side2`, `side3`, `triangle_type` та методи для обчислення `area`, `perimeter`, визначення `triangle_type` та `scale`.
  * **`Square`**: Успадковується від `Rectangle`, спеціалізуючись на квадратах. Додає метод `get_sides` та перевизначає `is_square` та `describe`.
  * **`main.py`**: Точка входу в програму, де створюються екземпляри різних фігур, демонструються їхні методи та можливості поліморфізму (функція `TotalArea`).

-----

## 📊 Діаграма Класів

```
Shape
├── Circle
├── Rectangle
│   └── Square
└── Triangle
```

-----

## 🚀 Як Запустити

Щоб запустити демонстрацію проекту, просто виконайте файл `main.py` у вашому терміналі:

```bash
python main.py
```

Ви побачите вивід з деталями та розрахунками для різних екземплярів фігур, включаючи їхні площі, периметри та результати порівняння.

-----

## 💡 Приклад Використання

Ось фрагмент коду з `main.py`, який демонструє створення та взаємодію з об'єктами фігур:

```python
from circle import Circle
from rectangle import Rectangle
from triangle import Triangle
from square import Square

# Створення екземплярів різних фігур
circle = Circle(radius=6, color="Black", center=(2, 3))
rectangle = Rectangle(width=4, height=6, color="Blue", position=(0, 0))
triangle = Triangle(side1=3, side2=4, side3=5, triangle_type="right", color="Green")
square = Square(side1=5, side2=5)

# Демонстрація описів фігур та розрахунків
print(circle.describe())
print(f"Площа кола: {circle.area():.2f}, периметр: {circle.perimeter():.2f}, діаметр: {circle.diameter()}\n")

print(rectangle.describe())
print(f"Площа прямокутника: {rectangle.area()}, периметр: {rectangle.perimeter()}, чи квадрат: {rectangle.is_square()}\n")

# Функція для обчислення загальної площі (демонстрація поліморфізму)
def TotalArea(shapes):
    total = 0
    for shape in shapes:
        total += shape.area()
    return total

shapes = [circle, rectangle, triangle]
print(f"Загальна площа всіх фігур: {TotalArea(shapes):.2f}")

# Демонстрація перевантаження операторів
print(f"Коло > Прямокутник: {circle > rectangle}")
```
