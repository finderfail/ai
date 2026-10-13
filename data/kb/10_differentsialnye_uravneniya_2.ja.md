# 常微分方程式（入門）— その2

### 例

$y' = xy$ を解きます。

$$\frac{dy}{y} = x\,dx \Rightarrow \ln|y| = \frac{x^2}{2} + C_1 \Rightarrow y = C e^{x^2/2}$$

## 1階線形方程式

$y' + p(x) y = q(x)$ の形の方程式は、積分因子 $\mu(x) = e^{\int p(x)dx}$ を使って解きます：
$$y = \frac{1}{\mu(x)}\left(\int \mu(x) q(x)\,dx + C\right)$$

別の方法として、ベルヌーイの方法（$y = uv$ と置換）があります。

## 定数係数の2階線形同次方程式

$y'' + py' + qy = 0$ の形の方程式。特性方程式をつくります：
$$k^2 + pk + q = 0$$

判別式 $D = p^2 - 4q$ によって：

- $D > 0$：2つの実数解 $k_1, k_2$、一般解 $y = C_1 e^{k_1 x} + C_2 e^{k_2 x}$；
- $D = 0$：重解 $k$、$y = (C_1 + C_2 x)e^{kx}$；
- $D < 0$：複素数解 $k = \alpha \pm i\beta$、$y = e^{\alpha x}(C_1 \cos\beta x + C_2 \sin\beta x)$。
