# n阶方阵A的属于不同特征值的特征向量线性无关的证明

$$
设\lambda_1,\lambda_2,\cdots,\lambda_s为方阵A的s个两两不同的特征值，
\newline
\alpha_1,\alpha_2,\cdots,\alpha_s为对应的特征向量
考虑方程组 x_1\alpha_1+x_2\alpha_2+\cdots+x_s\alpha_s=0
\newline
\therefore\left\{ \begin{array}{c}
	\alpha _1x_1+\alpha _2x_2+\cdots +\alpha _sx_s=0\\
	A\alpha _1x_1+A\alpha _2x_2+\cdots +A\alpha _sx_s=0\\
	\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots\\
	A^{s-1}\alpha _1x_1+A^{s-1}\alpha _2x_2+\cdots +A^{s-1}\alpha _sx_s=0\\
\end{array} \right. 
\newline
\therefore\left\{ \begin{array}{c}
	\alpha _1x_1+\alpha _2x_2+\cdots +\alpha _sx_s=0\\
	\lambda \alpha _1x_1+\lambda \alpha _2x_2+\cdots +\lambda \alpha _sx_s=0\\
	\cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots\\
	\lambda ^{s-1}\alpha _1x_1+\lambda ^{s-1}\alpha _2x_2+\cdots +\lambda ^{s-1}\alpha _sx_s=0\\
\end{array} \right.
\newline将其看作是关于\alpha_1 x_1,\alpha_2 x_2,\cdots,\alpha_s x_s的方程组，考虑其系数行列式:\newline
\left| \begin{matrix}
	1&		1&		\cdots&		1\\
	\lambda _1&		\lambda _2&		\cdots&		\lambda _s\\
	\vdots&		\vdots&		&		\vdots\\
	\lambda _{1}^{s-1}&		\lambda _{2}^{s-1}&		\cdots&		\lambda _{s}^{s-1}\\
\end{matrix} \right|\ne 0
\newline
\therefore\left\{\begin{array}{c}
\alpha_1 x_1=0\\
\alpha_2 x_2=0\\
\cdots\\
\alpha_s x_s=0\\
\end{array}\right.\\
\because \left\{\begin{array}{c}
\alpha_1\ne 0\\
\alpha_2\ne 0\\
\cdots\\
\alpha_s\ne 0\\
\end{array}\right.\\
\therefore x_1=x_2=\cdots=x_S=0
\therefore \alpha_1,\alpha_2,\cdots,\alpha_s 线性无关
$$

