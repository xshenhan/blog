# 广义积分

[TOC]

## 无穷积分

1. 无穷积分$\int_{a}^{+\infty}{f(x)dx}$只是个形式积分，只是收敛时把收敛到的*极限值* 定义成了这个形式积分的值。

2. $V.P.\int_{-\infty}^{{+\infty}}f(x)dx$是依主值收敛

3. 性质：

   > - 可加性：$\int_a^{+\infty}f(x)dx$与$\int_c^{+\infty}f(x)dx$$(c>a)$同敛散
   > - 线性性

4. 计算

   >  - 无穷积分的N-L公式要求f连续(思想：假设极限存在)
   >  - 无穷积分的分部积分要求$u,v$的导函数连续
   > - 换元积分法要求f连续，且$x=\varphi(t)\in C^{(1)}[\alpha,\beta)$

5. 敛散性判别：

   > - Cauchy准则 [例题](https://blog.leoh.top/first/dayi-s/sxfx/guangyi/liti1.html)
   > - 收敛原理（像单调有界）
   > - 比较判别法及其极限形式，p-判别法都要求$f(x)\ge0$ [例题](https://blog.leoh.top/first/dayi-s/sxfx/guangyi/liti2.html)

6. 绝对收敛$\Rightarrow$收敛

7. A-D判别法：[证明](https://blog.leoh.top/first/dayi-s/sxfx/guangyi/AD.html)

   > $若f,g满足下列条件之一，则\int_a^bf(x)g(x)dx收敛(a,b为之一为瑕点或正负无穷)$
   >
   > - Abel:$\int_a^bf(x)dx收敛$，g(x)单调有界
   > - Dirichlet: $\int_a^x f(t)dt有界(若b为瑕点或正负无穷)$，$\displaystyle\lim_{x\rightarrow b^+} g\left( x \right) =0$且$g(x)$单调

## 瑕积分

1. 瑕积分$\int_{a}^{+\infty}{f(x)dx}$只是个形式积分，只是收敛时把收敛到的*极限值* 定义成了这个形式积分的值。
2. 瑕积分的分部积分要求$u,v$的导函数连续
3. 换元积分法要求f连续，且$x=\varphi(t)\in C^{(1)}[\alpha,\beta)$

## 渐进性态

定理 设 $\int_a^{+\infty} f(x) \mathrm{d} x$ 收敛, 且 $f$ 满足下列四条件之一: 则
$$
\lim _{x \rightarrow+\infty} f(x)=0
$$
(1) $f$ 在 $[a,+\infty)$ 上单调;
(2) $\displaystyle\lim _{x \rightarrow+\infty} f(x)$ 存在
(3) $f \in$ U.C $[a,+\infty)$;
(4) $f^{\prime}$ 在 $[a,+\infty)$ 上有界

证明
