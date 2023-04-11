# 第十四章知识点梳理

[TOC]

## 偏导数与全微分

### 14.1.1偏导数

1. 定义：
   $$
   f_x\left(x_0, y_0\right) \stackrel{\text { def }}{=} \lim _{\Delta x \rightarrow 0} \frac{\Delta_x z}{\Delta x}=\lim _{\Delta x \rightarrow 0} \frac{f\left(x_0+\Delta x, y_0\right)-f\left(x_0, y_0\right)}{\Delta x}
   $$

   > - 可偏导未必连续：
   >
   >   考察 $f(x, y)=\left\{\begin{array}{cc}\frac{x y}{x^2+y^2}, & (x, y) \neq(0,0) \\ 0, & (x, y)=(0,0)\end{array}\right.$ 在 $(0,0)$ 的情况.
   >
   >   
   >
   > - 连续未必可偏导
   >
   >   考察$f(x,y) = |x|+|y|$在$(0,0)$的情况
   >
   >   

### 14.1.2全微分

1. 定义: 对函数 $z=f(x, y)$, 若全增量

$$
\begin{aligned}
\Delta z & =f\left(x_0+\Delta x, y_0+\Delta y\right)-f\left(x_0, y_0\right) \\
& =A \cdot \Delta x+B \cdot \Delta y+o(\rho)
\end{aligned}
$$
其中 $A, B$ 是常数, $\rho=\sqrt{(\Delta x)^2+(\Delta y)^2}$, 则称 $f$ 在 $\left(x_0, y_0\right)$ 可微.且$A \cdot \Delta x+B \cdot \Delta y$为f在$(x_0,y_0)$的全微分

若f在区域D内处处可微,则称f是D内的可微函数.

2. 可微与连续，偏导的关系：

   > - 可微必连续
   >
   > - 可微必可偏导, 且若
   >   $$
   >   \begin{gathered}
   >   \left.\mathrm{d} f\right|_{\left(x_0, y_0\right)}=A \cdot \Delta x+B \cdot \Delta y \\
   >   \Rightarrow \quad f_x\left(x_0, y_0\right)=A, f_y\left(x_0, y_0\right)=B
   >   \end{gathered}
   >   $$
   >
   > - 连续不一定可偏导，可偏导不一定连续

3. 可微的判断方法：

   >- 一个充分条件：连续偏导数$\Rightarrow$可微
   >
   >```python
   >if 不可偏导：
   >	return 不可微
   >else:
   >    return 求极限（见下）
   >```
   >
   >判断$\lim_{\rho \rightarrow 0} \frac{f_x\left( x_0,y_0 \right) \varDelta x+f_y\left( x_0,y_0 \right) \varDelta y-\varDelta z}{\rho}$是否等于0

## 14.2复合函数微分法

### 14.2.1复合函数的偏导数

1. 定理 设 $ u=u(x, y), v=v(x, y) $ 在 $ (x, y) $ 可偏导，$ z=f(u, v) $ 在相应的 $ (u, v) $ 处可微，则复合函数 $ z=f(u(x, y), v(x, y)) $ 在 $ (x, y) $ 处可偏导，且

$$
\frac{\partial z}{\partial x}=\frac{\partial f}{\partial u} \cdot \frac{\partial u}{\partial x}+\frac{\partial f}{\partial v} \cdot \frac{\partial v}{\partial x}, \frac{\partial z}{\partial y}=\frac{\partial f}{\partial u} \cdot \frac{\partial u}{\partial y}+\frac{\partial f}{\partial v} \cdot \frac{\partial v}{\partial y}
$$
链法则<img src="https://raw.githubusercontent.com/hanleo001/img/main/image-20230313200414815.png" alt="image-20230313200414815" style="zoom: 80%;" />
矩阵形式 $ \quad\left(\begin{array}{lll}z_{x} & z_{y}\end{array}\right)=\left(\begin{array}{ll}f_{u} & f_{v}\end{array}\right)\left(\begin{array}{ll}u_{x} & u_{y} \\ v_{x} & v_{y}\end{array}\right) $

2. 推广 设向量值函数
   $$
   \boldsymbol{f}(u, v)=\left(\begin{array}{l}
   f_1(u, v) \\
   f_2(u, v)
   \end{array}\right), \quad \boldsymbol{g}(x, y)=\left(\begin{array}{l}
   u(x, y) \\
   v(x, y)
   \end{array}\right)
   $$
   偏导数连续, 则 $\boldsymbol{f} \circ \boldsymbol{g}=\left(\begin{array}{l}z_1(x, y) \\ z_2(x, y)\end{array}\right)$ 的 $\mathbf{J a c o b i}$ 矩阵
   $$
   \boldsymbol{D}_{f^{\circ} g}(x, y)=\left(\begin{array}{ll}
   \frac{\partial z_1}{\partial x} & \frac{\partial z_1}{\partial y} \\
   \frac{\partial z_2}{\partial x} & \frac{\partial z_2}{\partial y}
   \end{array}\right)=\left(\begin{array}{ll}
   \frac{\partial f_1}{\partial u} & \frac{\partial f_1}{\partial v} \\
   \frac{\partial f_2}{\partial u} & \frac{\partial f_2}{\partial v}
   \end{array}\right)\left(\begin{array}{ll}
   \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\
   \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y}
   \end{array}\right)=\boldsymbol{D}_f(u, v) \cdot \boldsymbol{D}_g(x, y)
   $$
   

   想一想 $\boldsymbol{f}$ 为 $m$ 维 $k$ 元, $\boldsymbol{g}$ 为 $k$ 维 $n$ 元向量值函数的情形

   **复合向量值函数的Jacobi矩阵等于外层函数Jacobi矩阵左乘内层函数Jacobi矩阵**：
   $$
   \boldsymbol{D}_{f^{\circ} g}=\boldsymbol{D}_f \cdot \boldsymbol{D}_g
   $$
### 14.2.2一阶全微分具有形式不变性

## 14.3高阶偏导数与全微分

### 14.3.1 高阶偏导数

1. 混合偏导数不是总与求导次序无关：
   $$
   \text { 设 } f(x, y)=\left\{\begin{array}{ll}
   x y, & |x| \geq|y| \\
   -x y, & |x|<|y|
   \end{array} \text {, 求 } f_{x y}(0,0), f_{y x}(0,0)\right. \text {. }
   $$

2. 定理 若 $f(x, y)$ 的两个二阶混合偏导数在 $(x, y)$ 连续, 则
   $$
   f_{x y}(x, y)=f_{y x}(x, y)
   $$

3. n阶全微分:

$$
\begin{aligned}
\mathrm{d}^n z & =\left(\frac{\partial}{\partial x} \mathrm{~d} x+\frac{\partial}{\partial y} \mathrm{~d} y\right)^n z \\
& =\left(\sum_{k=0}^n C_n^k \frac{\partial^n}{\partial x^k \partial y^{n-k}} \mathrm{~d} x^k \mathrm{~d} y^{n-k}\right) z
\end{aligned}
$$
注意 高阶全微分不再具有形式不变性!

## 14.4 Taylor公式与极值问题

0. 凸区域：若区域 $D$ 中任意两点的连线都含于 $D$.
   微分中值定理：设 $f$ 在凸区域 $D$ 中可微, 则 $\exists \theta \in(0,1)$ :
   $$
   \begin{aligned}
   & f\left(x_0+\Delta x, y_0+\Delta y\right)-f\left(x_0, y_0\right) \\
   = & f_x\left(x_0+\theta \Delta x, y_0+\theta \Delta y\right) \Delta x+f_y\left(x_0+\theta \Delta x, y_0+\theta \Delta y\right) \Delta y
   \end{aligned}
   $$
   若 $f(x, y)$ 在区域 $D$ 可微, 且 $f_x(x, y)=0, f_y(x, y)=0$, 则
   $$
   f(x, y) \equiv C
   $$

1. 

1. **定理(Taylor公式)** 设函数 $f(x, y)$ 在 $U\left(P_0\left(x_0, y_0\right)\right)$ 有 $n+1$
   阶连续偏导数, 则 $\exists \theta \in(0,1)$ :
   $$
   f\left(x_0+\Delta x, y_0+\Delta y\right)=\sum_{k=0}^n \frac{1}{k !}\left(\Delta x \frac{\partial}{\partial x}+\Delta y \frac{\partial}{\partial y}\right)^k f\left(x_0, y_0\right)+R_n
   $$
   其中Lagrange型余项
   $$
   R_n=\frac{1}{(n+1) !}\left(\Delta x \frac{\partial}{\partial x}+\Delta y \frac{\partial}{\partial y}\right)^{n+1} f\left(x_0+\theta \Delta x, y_0+\theta \Delta y\right)
   $$

2. **极值的必要条件**

   若 $f(x, y)$ 可偏导, 且在 $P_0\left(x_0, y_0\right)$ 取极值, 则

$$
f_x\left(x_0, y_0\right)=0=f_y\left(x_0, y_0\right)
$$
- 满足上式的点称为驻点(驻点末必是极值点)

- 极值点未必是驻点，可偏导的极值点是驻点

3. **极值的充分条件：**

   定理 设 $f(x, y)$ 在 $U\left(P_0\left(x_0, y_0\right)\right)$ 的二阶偏导数连续, 且
   $$
   f_x\left(x_0, y_0\right)=0, f_y\left(x_0, y_0\right)=0,
   $$
   记Hesse矩阵 $\boldsymbol{H}=\left(\begin{array}{ll}f_{x x} & f_{x y} \\ f_{y x} & f_{y y}\end{array}\right)_{P_0}$
   (1) 若 $\boldsymbol{H}$ 为正定矩阵, 则 $f\left(x_0, y_0\right)$ 为严格极小值; 若 $\boldsymbol{H}$ 为负定矩阵, 则 $f\left(x_0, y_0\right)$ 为严格极大值

   (2) 若 $\boldsymbol{H}$ 为不定矩阵, 则 $f\left(x_0, y_0\right)$ 非极值.

   (3) 若$\boldsymbol{H}$为半正(负)定矩阵，则$f\left(x_0, y_0\right)$无法判断

   ## 14.5隐函数存在定理

1. 

   ![image-20230409152112559](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409152112559.png)

2. ![image-20230409152246045](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409152246045.png)

3. ![image-20230409152324520](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409152324520.png)

- 求隐函数所有偏导数时, 全微分法比较简便





## 14.7 多元微分学的几何应用

| 几何图形 | 方程类型                                                     | 法向量或方向向量                                             |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 曲线     | 空间曲线$\Gamma$参数式$x=x(t), y=y(t), z=z(t)$               | $\Gamma$ 的切向量$\boldsymbol{\tau}=\left(x^{\prime}\left(t_{0}\right), y^{\prime}\left(t_{0}\right), z^{\prime}\left(t_{0}\right)\right)$ |
| 曲线     | 一般式$\Gamma:\left\{\begin{array}{l}F(x,y,z)=0 \\ G(x,y,z)=0\end{array}\right.$ | $(\frac{\part{(F,G)}}{\part(y,z)},\frac{\part{(F,G)}}{\part(z,x)},\frac{\part{(F,G)}}{\part(x,y)})|_{u_0}$ |
| 曲面     | 一般式：$F(x, y, z) = 0$                                     | $\nabla F\left(M_{0}\right)=\left.\left(F_{x}, F_{y}, F_{z}\right)\right.$ |
| 曲面     | 参数式：$\left\{\begin{array}{l}x=x(u, v) \\ y=y(u, v) \\ z=z(u, v)\end{array}\right.$ | $(x_u,y_u,z_u)\times(x_v,y_v,z_v)=\\(\frac{\part(y,z)}{\part(u,v)},\frac{\part(z,x)}{\part(u,v)},\frac{\part(x,y)}{\part(u,v)})$ |

![image-20230409183559184](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409183559184.png)

## 14.8 条件极值--Lagrange乘数法

- 最值问题：

  原则 有界闭区域上的可微函数的最值在内部 驻点或边界点取到. 实际问题中, 若最值必在区域 内部取得又驻点唯一, 则此驻点就是最值点.
