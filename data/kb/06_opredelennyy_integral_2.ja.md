# 定積分 — その2

## ニュートン＝ライプニッツの公式

$F(x)$ が $[a, b]$ における $f(x)$ の原始関数なら：
$$\int_a^b f(x)\,dx = F(b) - F(a) = F(x)\Big|_a^b$$

定積分と不定積分を結びつける基本公式です。

## 定積分の性質

1. $\int_a^a f(x)\,dx = 0$
2. $\int_a^b f(x)\,dx = -\int_b^a f(x)\,dx$
3. $\int_a^b (f(x) \pm g(x))\,dx = \int_a^b f(x)\,dx \pm \int_a^b g(x)\,dx$
4. $\int_a^b c\cdot f(x)\,dx = c\int_a^b f(x)\,dx$
5. $\int_a^b f(x)\,dx = \int_a^c f(x)\,dx + \int_c^b f(x)\,dx$（区間についての加法性）
6. $[a,b]$ で $f(x) \geq 0$ なら $\int_a^b f(x)\,dx \geq 0$

## 定積分の置換積分

$$\int_a^b f(x)\,dx = \int_\alpha^\beta f(\varphi(t))\varphi'(t)\,dt$$

ここで $x = \varphi(t)$、$\varphi(\alpha) = a$、$\varphi(\beta) = b$。不定積分と違い、積分区間も変わるので、元の変数に戻す必要はありません。
