# 不定積分 — その3

## 部分積分法

$$\int u\,dv = uv - \int v\,du$$

被積分関数が性質の異なる関数の積（多項式×指数関数、多項式×対数関数、多項式×三角関数など）のときに使います。$u$ の選び方の目安は LIATE：対数関数、逆三角関数、代数関数（多項式）、三角関数、指数関数の順に $u$ として優先します。

## 例：置換積分

$\int 2x \cdot e^{x^2}\,dx$ を求めます。

$u = x^2$ とおくと $du = 2x\,dx$：
$$\int 2x \cdot e^{x^2}\,dx = \int e^u\,du = e^u + C = e^{x^2} + C$$

## 例：部分積分

$\int x \cos x\,dx$ を求めます。

$u = x$、$dv = \cos x\,dx$ とおくと $du = dx$、$v = \sin x$：
$$\int x\cos x\,dx = x\sin x - \int \sin x\,dx = x\sin x + \cos x + C$$
