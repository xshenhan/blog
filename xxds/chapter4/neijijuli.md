1.列向量的内积

>通常意义下的内积

$$
(\alpha,\beta)=\beta^T\alpha
$$

>  另一种内积的定义

$$
(\alpha, \beta)=a_1 b_1+2 a_2 b_2+\cdots+n a_n b_n=\sum_{i=1}^n i a_i b_i
$$

2.$R^{m\times n}$中可定义内积
$$
(A, B)=\sum_{i=1}^m \sum_{j=1}^n a_{i j} b_{i j}，这里A=(a_{ij})_{m\times n}，B=(b_{ij})_{m\times n}
$$
3.C([a,b])中可定义内积：
$$
\text { 对任意 } f(x), g(x) \in C([a, b]),(f(x), g(x))=\int_a^b f(t) g(t) d t
$$
证明：
$$
(1)对称性显然成立\\
(2)线性性：(kf(x),g(x))=\int_a^bkf(x)g(x)dx=k\int_a^bf(t)g(t)dt=k(f(x),g(x))\\
设\theta(x)\in C[a,b],((f+\theta)(x),g(x))=\int_a^b((f+\theta)(x)g(x)dx)\\
=\int_a^bf(x)g(x)dx+\int_a^b\theta(x)g(x)dx=(f(x),g(x))+(\theta(x),g(x))\\
(3)正定性：(f(x),f(x))=\int_a^bf^2(x)dx\ge0\\
切仅当f(x)\equiv0时取等
$$
