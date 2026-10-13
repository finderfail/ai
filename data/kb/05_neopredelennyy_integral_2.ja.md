# 不定積分 — その2

## 基本的な積分の表

| 積分 | 結果 |
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

## 置換積分法

$x = \varphi(t)$ が微分可能な関数なら：
$$\int f(x)\,dx = \int f(\varphi(t))\varphi'(t)\,dt$$

よく使う特別な場合：$\int f(g(x)) g'(x)\,dx = \int f(u)\,du$（$u = g(x)$）。
