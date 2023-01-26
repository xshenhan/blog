# 关于几何重数一定小于代数重数的证明

证明 设 $\lambda_0$是n阶方阵$\mathcal{A}$的特征向量，$\operatorname{dim} V_{\lambda_0}=q$. 取 $V_{\lambda_0}$ 的基 $\alpha_1, \ldots, \alpha_q$, 扩充为 $V$ 的基 $\alpha_1, \ldots, \alpha_q, \ldots, \alpha_n$. 注意到
$$
\mathcal{A} \alpha_i=\lambda_0 \alpha_i, \quad i=1, \ldots, q,
$$
设$P=\left( \begin{matrix}
	\alpha _1&		\alpha _2&		\cdots&		\alpha _n\\
\end{matrix} \right) 
$

于是有
$$
AP=P\left(\begin{array}{cccccc}
\lambda_0 & \cdots & 0 & * & \cdots & * \\
\vdots & \ddots & \vdots & \vdots & & \vdots \\
0 & \cdots & \lambda_0 & * & \cdots & * \\
0 & \cdots & 0 & * & \cdots & * \\
\vdots & & \vdots & \vdots & & \vdots \\
0 & \cdots & 0 & * & \cdots & *
\end{array}\right)=P\left(\begin{array}{cc}
\lambda_0 E_q & A_{12} \\
O & A_{22}
\end{array}\right) .
$$
$\therefore A相似于\left(\begin{array}{cc}
\lambda_0 E_q & A_{12} \\
O & A_{22}
\end{array}\right) .$

由此计算即得 $\mathcal{A}$ 的特征多项式
$$
|\lambda E-A|=\left|\begin{array}{cc}
\left(\lambda-\lambda_0\right) E_q & -A_{12} \\
O & \lambda E_{n-q}-A_{22}
\end{array}\right|=\left(\lambda-\lambda_0\right)^q\left|\lambda E_{n-q}-A_{22}\right|,
$$
即得 $\lambda_0$ 的代数重数 $\geqslant q$.