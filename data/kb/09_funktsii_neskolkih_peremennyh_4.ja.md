# 多変数関数 — その4

## 2変数関数の極値

**必要条件**：微分可能な関数の極値点では、1階偏導関数がどちらも0になります：
$$\frac{\partial z}{\partial x} = 0, \quad \frac{\partial z}{\partial y} = 0$$

このような点を**停留点**といいます。

**十分条件**（2階導関数による）。停留点 $(x_0, y_0)$ で：
$$A = \frac{\partial^2 z}{\partial x^2}, \quad B = \frac{\partial^2 z}{\partial x \partial y}, \quad C = \frac{\partial^2 z}{\partial y^2}, \quad D = AC - B^2$$

- $D > 0$ かつ $A > 0$ なら極小点；
- $D > 0$ かつ $A < 0$ なら極大点；
- $D < 0$ なら極値ではない（鞍点）；
- $D = 0$ なら追加の調査が必要。
