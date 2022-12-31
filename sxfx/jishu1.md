# 级数-part1

## 基本概念

1. 求解级数值的一些常见方法：

   > - 求出部分和数列
   >   - 错位相减
   >   - 裂项：补几道[习题](https://fir.leoroom.top/sxfx/jishu/liexiang.html)
   >   - 方程式法：建立$S_n$的方程，解出$S_n$ 例：$\displaystyle\sum_{k=1}^nq^kcos\ (ka)$（注：也可以利用复数）
   > - Stolz定理
   > - 利用子列的极限：例题
   > - 先求$S'_n(x)的紧缩形式$

## 正项级数





## 补充习题

【114】 (Carleman Inequality) 设 $f(x)>0$, 则有
$$
\int_0^{\infty} \exp \left[\frac{1}{x} \int_0^x \ln f(t) \mathrm{d} t\right] \mathrm{d} x \leqslant \mathrm{e} \int_0^{\infty} f(x) \mathrm{d} x
$$
离散形式:
$$
\sum_{n=1}^{\infty} \sqrt[n]{a_1 \cdots a_n} \leqslant \mathrm{e} \sum_{n=1}^{\infty} a_n
$$
期中 $\displaystyle\sum_{n=1}^{\infty} a_n$ 是正项级数, 且其中系数 $\mathrm{e}$ 是最佳的.

【129】设 $\left\{a_n\right\}$ 是正项数列, 满足条件 $n a_n \rightarrow 0, n \rightarrow \infty$ 且有 $\frac{a_{n+1}}{a_n}=\frac{n+a}{n+b}, a, b \in \mathbb{R}$.

(1)证明级数 $\sum a_n$ 收敛, 并计算其和;

(2)计算 $\sum \frac{(2 n-1) ! !}{(2 n+2) ! !}$.

【130】设正项级数 $\sum \frac{1}{a_n}$ 收敛. 证明 $\sum \frac{n^2 a_n}{S_n^2}$ 收敛.