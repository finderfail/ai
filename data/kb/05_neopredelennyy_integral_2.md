# Неопределённый интеграл — часть 2

## Таблица основных интегралов

| Интеграл | Результат |
|---|---|
| $\int x^n\,dx$ | $\dfrac{x^{n+1}}{n+1} + C,\; n \neq -1$ |
| $\int \dfrac{dx}{x}$ | $\ln\lvert x \rvert + C$ |
| $\int e^x\,dx$ | $e^x + C$ |
| $\int a^x\,dx$ | $\dfrac{a^x}{\ln a} + C$ |
| $\int \sin x\,dx$ | $-\cos x + C$ |
| $\int \cos x\,dx$ | $\sin x + C$ |
| $\int \dfrac{dx}{\cos^2 x}$ | $\tan x + C$ |
| $\int \dfrac{dx}{\sin^2 x}$ | $-\cot x + C$ |
| $\int \dfrac{dx}{1+x^2}$ | $\arctan x + C$ |
| $\int \dfrac{dx}{\sqrt{1-x^2}}$ | $\arcsin x + C$ |

## Метод замены переменной (подстановки)

Если $x = \varphi(t)$ — дифференцируемая функция, то:
$$\int f(x)\,dx = \int f(\varphi(t))\varphi'(t)\,dt$$

Часто используемый частный случай: $\int f(g(x)) g'(x)\,dx = \int f(u)\,du$, где $u = g(x)$.
