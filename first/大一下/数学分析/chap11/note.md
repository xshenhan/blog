# 幂级数

### 1.Cauchy-Hadamard 定理

![image-20230529223440830](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529223440830.png)

- 若$\lim \limits_{n \rightarrow \infty} \frac{\left|a_{n+1}\right|}{\left|a_{n}\right|}$存在广义极限，则$r=\lim \limits_{n \rightarrow \infty} \frac{\left|a_{n}\right|}{\left|a_{n+1}\right|}$

- 收敛域求法 ==先用比值法或者根值法求收敛半径，在考察端点处的敛散性==

  > 缺项幂级数不能用比值法求收敛半径!

- 广义幂级数:

  - 形式 ：$$\sum_{n=0}^{\infty} a_{n}[g(x)]^{n}$$
  - 令 $t=g(x)$, 变为 $\sum_{n=0}^{\infty} a_{n} t^{n}$. 若其收敛区间为 $(-r, r)$, 则 原级数的收敛域包含 $\{x|| g(x) \mid<r\}$

### 2.Abel定理

- **Abel第I定理** 设 $\sum_{n=0}^{\infty} a_{n} x^{n}$ 在 $x_{1}(\neq 0)$ 收敛, 则 $|x|<\left|x_{1}\right|$ 时 绝对收敛; 若 $\sum_{n=0}^{\infty} a_{n} x^{n}$ 在 $x_{2}$ 发散, 则 $|x|>\left|x_{2}\right|$ 时发散.

- **Abel第II定理** 设 $\sum_{n=n}^{\infty} a_{n} x^{n}$ 收敛半径为 $r(>0)$, 则它在 $(-r, r)$ 内闭一致收敛; 若 $x=r$ 时收敛, 则它在 $[0, r]$ 一致收敛, 从而在 $(-r, r]$ 内闭一致收敛.

  >注意： 内壁一致收敛性是幂级数的特性，一般函数项级数未必具有， 考察例子：$\sum_{n=0}^{\infty} \frac{n x}{1+n^{4} x^{4}}$

- **Abel第III定理** 

  
  $$
  设 f(x)=\sum_{n=0}^{\infty} a_{n} x^{n} \quad x \in(-r, r],
  则 f(x) 在 x=r 处左连续, 即:\\\lim \limits_{x \rightarrow r^{-}} \sum_{n=0}^{\infty} a_{n} x^{n}=\sum_{n=0}^{\infty} a_{n} r^{n}
  $$

  > 贴个反例：
  >
  > ![image-20230529230632137](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529230632137.png)

### 3.分析性质

- 定理 幂级数 $\sum_{n=0}^{\infty} a_{n} x^{n}$ 与其导数级数 $\sum_{n=1}^{\infty} n a_{n} x^{n-1}$ 和 积分级数 $\sum_{n=0}^{\infty} \frac{a_{n}}{n+1} x^{n+1}$ 的收敛半径相等. 

  > 注意 三个级数在端点的收敛性未必相同，有 $D' \subset D \subset D_1$ 其中 D 是$\sum_{n=0}^{\infty} a_{n} x^{n}$的收敛域，$D'$ 是$ \sum_{n=1}^{\infty} n a_{n} x^{n-1}$的收敛域，$D_1$是$\sum_{n=0}^{\infty} \frac{a_{n}}{n+1} x^{n+1}$的收敛域

- 
    ![image-20230529230338975](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529230338975.png)

- 几个常用幂级数的和函数：
  - $\sum_{n=1}^{\infty} \frac{x^{n}}{n} = \ln(\frac{1}{1-x}) x\in[-1,1)$ 
  - $\sum_{n=0}^{\infty} \frac{x^{n}}{n \text { ! }} = e^x$;

## 函数的幂级数展开

### 1.Taylor级数


$$
定义 设 f(x) 在 x_{0} 无穷次可导, 则称\\f(x) \sim \sum_{n=0}^{\infty} \frac{f^{(n)}\left(x_{0}\right)}{n !}\left(x-x_{0}\right)^{n}
为 f(x) 在 x_{0}处的 Taylor级数.\\
x_{0}=0 时称为 Maclaurin级数.
$$
**Maclaurin级数和原函数不等的例子**

![image-20230529231654919](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529231654919.png)

---

问题 $f(x)$ 满足何条件时, 其 Taylor级数收敛于 $f(x)$ ?

![image-20230529231851289](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529231851289.png)

![image-20230529231859324](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529231859324.png)

---

![image-20230529231947904](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529231947904.png)

![image-20230529232012506](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529232012506.png)



$$
arctanx = \sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} x^{2n+1}\\
arcsinx = x + \sum_{n=1}^{\infty}\frac{(2n-1)!!}{(2n)!!(2n+1)}x^{2n+1}
$$


### Stirling 公式

![image-20230529232418480](https://raw.githubusercontent.com/hanleo001/img/main/image-20230529232418480.png)

