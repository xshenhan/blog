# Fourier级数

## Fourier级数

### 1.三角函数系

$$
\{1, \cos x, \sin x, \cdots, \cos n x, \sin n x, \cdots\}
$$

- 三角函数系的特点：正交性！

### 2.Fourier级数

---

设在 $[-\pi, \pi]$ 上函数 $f(x)$ 可展开为三角级数, 即
$$
f(x)=\frac{a_{0}}{2}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$
其中, $a_n,b_n$可由正交性得到：
$$
\left\{\begin{array}{cc}a_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \cos n x \mathrm{~d} x, \quad n=0,1,2, \cdots, \\ b_{n}=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x) \sin n x \mathrm{~d} x, \quad n=1,2, \cdots .\end{array}\right.
$$

---

- 可积与绝对可积: 函数f满足下列两条件之一
  - $f\in R[-\pi,\pi]$
  - 瑕积分$\int_{-\pi}^{\pi}f(x)dx$绝对收敛

- F氏级数

​	<img src="https://raw.githubusercontent.com/hanleo001/img/main/image-20230530090401345.png" alt="image-20230530090401345" style="zoom:50%;" />

- 正弦和余弦级数

<img src="https://raw.githubusercontent.com/hanleo001/img/main/image-20230530090548894.png" alt="image-20230530090548894" style="zoom:50%;" />

## Fourier级数的收敛性

### 1. Dirichlet积分

设 $f$ 以 $2 \pi$ 为周期, 在 $[-\pi, \pi]$ 上可积与绝对可积, 且
$$
f(x) \sim \frac{a_{0}}{2}+\sum_{n=1}^{\infty}\left(a_{n} \cos n x+b_{n} \sin n x\right)
$$
其部分和函数
$$
S_{n}(f, x)=\frac{a_{0}}{2}+\sum_{k=1}^{n}\left(a_{k} \cos k x+b_{k} \sin k x\right)
$$
称为 $f$ 的 $n$ 阶Fourier多项式.

- 结论

$$
S_{n}(f, x)=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x+u) \frac{\sin \frac{2 n+1}{2} u}{2 \sin \frac{u}{2}} \mathrm{~d} u\\
=\frac{1}{\pi} \int_{0}^{\pi} (f(x+u)+f(x-u)) \frac{\sin \frac{2 n+1}{2} u}{2 \sin \frac{u}{2}} \mathrm{~d} u\\且称 \frac{\sin \frac{2 n+1}{2} u}{2 \sin \frac{u}{2}}\text{为Dirichlet积分核}
$$

​	

<details>
    <summary>证明</summary>
    <pre><code>
	<img src="https://raw.githubusercontent.com/hanleo001/img/main/image-20230530133854338.png" alt="image-20230530133854338" />
    </code></pre>
</details>
- 由此可以得到一个简单事实：

$$
\frac{2}{\pi} \int_{0}^{\pi} D_{n}(u) \mathrm{d} u=\frac{2}{\pi} \int_{0}^{\pi}\left(\frac{1}{2}+\sum_{k=1}^{n} \cos k u\right) \mathrm{d} u=1
$$

![image-20230530134658511](https://raw.githubusercontent.com/hanleo001/img/main/image-20230530134658511.png)

​    

### 2. 局部性定理

- Riemann引理: 

  <img src="https://raw.githubusercontent.com/hanleo001/img/main/image-20230530135001475.png" alt="image-20230530135001475" style="zoom: 50%;" />

- 局部性定理：

  <img src="https://raw.githubusercontent.com/hanleo001/img/main/image-20230530141212994.png" alt="image-20230530141212994" style="zoom:50%;" />

- 两个推论: 

  ![image-20230530141249399](https://raw.githubusercontent.com/hanleo001/img/main/image-20230530141249399.png)

- Dini定理

定理(Dini) 设 $f$ 满足局部性定理条件, 且 $\exists \delta \in(0, \pi)$ 使 $\frac{f(x+u)+f(x-u)-2 S(x)}{u}$ 在 $[0, \delta]$ 上可积与绝对可积, 则 $\lim \limits_{n \rightarrow \infty} S_{n}(f, x)=S(x)$

### 3.F氏级数收敛性判别法

- Dirichlet引理

![image-20230530141814575](https://raw.githubusercontent.com/hanleo001/img/main/image-20230530141814575.png)

- 定理：

  ![image-20230530141846698](https://raw.githubusercontent.com/hanleo001/img/main/image-20230530141846698.png)

