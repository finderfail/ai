# 関数の極限 — その3

## 不定形

極限の計算では、次のような不定形がよく現れます：
$$\frac{0}{0}, \quad \frac{\infty}{\infty}, \quad \infty - \infty, \quad 0 \cdot \infty, \quad 1^\infty, \quad 0^0, \quad \infty^0$$

不定形の解消には、因数分解、共役式を掛ける、重要な極限、ロピタルの定理、テイラー展開などを使います。

## ロピタルの定理

$\lim_{x \to a} f(x) = \lim_{x \to a} g(x) = 0$（または両方が $\infty$）で、$\lim_{x \to a} \frac{f'(x)}{g'(x)}$ が存在するなら：
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$

この定理は $0/0$ と $\infty/\infty$ の不定形にだけ使えます。それ以外の形は代数的な変形でこの2つに帰着させます。

## 例

$\lim_{x \to 0} \frac{\sin 3x}{x}$ を求めます。

3を掛けて3で割ると：
$$\lim_{x \to 0} \frac{\sin 3x}{x} = 3 \cdot \lim_{x \to 0} \frac{\sin 3x}{3x} = 3 \cdot 1 = 3$$
