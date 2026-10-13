# 多変数関数 — その1

## 定義

ある集合 $D$（定義域）に属する数の組 $(x, y)$ のそれぞれに、ただ1つの数 $z$ を対応させる規則 $z = f(x, y)$ を2変数関数といいます。

3変数以上の関数 $u = f(x_1, x_2, \dots, x_n)$ も同様に定義します。

## 偏導関数

関数 $z = f(x, y)$ の $x$ についての**偏導関数**は次の極限です：
$$\frac{\partial z}{\partial x} = f_x'(x,y) = \lim_{\Delta x \to 0} \frac{f(x+\Delta x, y) - f(x,y)}{\Delta x}$$

$\partial z/\partial x$ を計算するときは $y$ を定数とみなし、$\partial z/\partial y$ では $x$ を定数とみなします。
