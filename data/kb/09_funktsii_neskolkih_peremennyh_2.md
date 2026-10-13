# Функции нескольких переменных — часть 2

## Частные производные второго порядка

$$\frac{\partial^2 z}{\partial x^2},\quad \frac{\partial^2 z}{\partial y^2},\quad \frac{\partial^2 z}{\partial x \partial y},\quad \frac{\partial^2 z}{\partial y \partial x}$$

**Теорема Шварца (Клеро)**: если смешанные частные производные непрерывны, то они не зависят от порядка дифференцирования:
$$\frac{\partial^2 z}{\partial x \partial y} = \frac{\partial^2 z}{\partial y \partial x}$$

## Полный дифференциал

Если функция $z = f(x,y)$ дифференцируема в точке, её полный дифференциал:
$$dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$$

Используется для приближённых вычислений: $\Delta z \approx dz$ при малых приращениях $dx, dy$.
