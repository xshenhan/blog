# 凸函数

1. $f(x)(下)凸:f(\lambda x_1+(1-\lambda )x_2)\le\lambda f(x_1)+(1-\lambda)f(x_2)$
2. 等价表述：

$$
(1)\forall x\in[a,b]:f(x)\le\frac{b-x}{b-a}f(a)+\frac{x-a}{b-a}f(b)\\
(2)\forall x\in[a,b]:\frac{f(x)-f(a)}{x-a}\le \frac{f(b)-f(x)}{b-x}
$$



3. 第一充要条件：$若f\in C[a,b]\bigcap D(a,b)，则f(x)为凸函数等价于f^\prime(x)单调递增$

4. 第二充要条件：$若f\in C[a,b]且在(a,b)上二阶可导，则f(x)为凸函数等价于f'' (x)单调递增$

5. 拐点在二阶导为0点或不可导点中

6. 性质：

   > - 凸函数的斜率函数($k(x)=\frac{f(x)-f(x_0)}{x-x_0}$)递增
   > - 凸函数在区间内部左右可导，且左导不超过右导
   > - 闭区间上的凸函数在开区间连续，且端点处单侧极限存在