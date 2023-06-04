# 第一类线面积分

## 第一类曲线积分

1. 性质

   - 与曲线方向无关
   - 线性性
   - 可加性

2. 第一类曲线积分的计算

   - $$
     \int_{C} f(x, y) \mathrm{d} s=\int_{\alpha}^{\beta} f(x(t), y(t)) \underbrace{\sqrt{x^{\prime 2}(t)+y^{\prime 2}(t)} \mathrm{d} t}_{\mathrm{d} s \text { 弧微分 }}
     $$

     - 特别的，当曲线 $C$ 形式为 $y=y(x), x \in[a, b]$时：
       $$
       \int_{C} f(x, y) \mathrm{d} s=\int_{a}^{b} f(x, y(x)) \sqrt{1+y^{\prime 2}(x)} \mathrm{d} x
       $$

     - 在极坐标$r=r(\theta)$ 时, $\mathrm{d} s=\sqrt{r^{2}+r^{\prime 2}} \mathrm{~d} \theta$
     - 对于空间曲线 $L$ :
       $x=x(t), y=y(t), z=z(t), \quad t \in[\alpha, \beta]$
       第一类曲线积分 $\int f(x, y, z) \mathrm{d} s = \int_\alpha^\beta f(x(t), y(t), z(t)) \sqrt{x^{\prime  2}(t)+y^{\prime  2}(t)+z^{\prime  2}(t) }\mathrm{d} t$ 

## 第一类曲面积分  

- 曲面面积公式

$$
\mathrm{d} S=\sqrt{1+z_{x}^{2}+z_{y}^{2}} \mathrm{~d} x \mathrm{~d} y
$$

- 若 $S$ 为双参数方程 $\left\{\begin{array}{l}x=x(u, v), \\ y=y(u, v),(u, v) \in D \\ z=z(u, v),\end{array}\right.$，则
  $$
  \mathrm{d} S=\sqrt{A^{2}+B^{2}+C^{2}} \mathrm{~d} u \mathrm{~d} v
  $$

- 计算法

  - 曲面S为显式方程
    $$
    z=z(x,y), x,y\in D
    $$
    则有
    $$
    dS = \sqrt{1+z_x^2+z_y^2} \mathrm{d}x\mathrm{d}y
    $$
    从而
    $$
    \iint_{S} f(x, y, z) \mathrm{d} S=\iint_{D} f(x, y, z(x, y)) \sqrt{1+z_{x}^{2}+z_{y}^{2}} \mathrm{~d} x \mathrm{~d} y
    $$

  - 曲面是双参数方程
    $$
    \left\{\begin{array}{l}x=x(u, v), \\ y=y(u, v), \quad(u, v) \in D \\ z=z(u, v),\end{array}\right.
    $$
    则有
    $$
    
    \iint_{S} f(x, y, z) \mathrm{d} S=\iint_{D} f[x(u, v), y(u, v), z(u, v)] \sqrt{A^{2}+B^{2}+C^{2}} \mathrm{~d} u \mathrm{~d} v\\
    $$
    其中
    $$
    \\A=\frac{\partial(y, z)}{\partial(u, v)}, \quad B=\frac{\partial(z, x)}{\partial(u, v)}, \quad C=\frac{\partial(x, y)}{\partial(u, v)}
    $$
    

