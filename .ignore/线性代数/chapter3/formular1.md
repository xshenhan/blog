定理：设A为n阶方阵，$$ f(\lambda)= \lambda ^{n}+a_{n-1}\lambda ^{n-1}+ \cdots +a_{1}\lambda +a_{0} $$是A的特征多项式，那么$$ f(A)=O $$ 

证明1：
$$
设A的特征值为\lambda_1,\lambda_2,\cdots\lambda_n(重根分别计算)\\则f(A)的特征值为f(\lambda_1),f(\lambda_2),\cdots,f(\lambda_n)\\即f(A)的n个特征值都是0\\
\therefore f(A)相似于0矩阵\\
\therefore \exist 可逆阵P,st:P^{-1}f(A)P=O
\therefore f(A)=O
$$
证明2：
$$
设A的Jordan标准型为J_A 设
J_A=\left( \begin{matrix}
	J_1&		&		\cdots&		\\
	&		J_2&		\cdots&		\\
	\vdots&		\vdots&		&		\vdots\\
	&		&		\cdots&		J_p\\
\end{matrix} \right) 
\\
\therefore \exist 可逆阵P st:P^{-1}AP=J_A\\
\therefore f(A)=O \iff P^{-1}f(A)P=f(P^{-1}AP)=O\iff f(J_A)=O\\
设A的特征多项式为f(x)=(x-\lambda_1)^{s_1}(x-\lambda_2)^{s_2}\cdots (x-\lambda_p)^{s_p}\\
\therefore f(J_A)=(J_A-\lambda_1E)^{s_1}(J_A-\lambda_2E)^{s_2}\cdots (J_A-\lambda_pE)^{s_p}\\
=\left( \begin{matrix}
	\left( J_1-\lambda _1E \right) ^{s_1}&		&		\cdots&		\\
	&		J_{2}^{s_2}&		\cdots&		\\
	\vdots&		\vdots&		&		\vdots\\
	&		&		\cdots&		J_{p}^{s_p}\\
\end{matrix} \right) \left( \begin{matrix}
	{J_1}^{s_1}&		&		\cdots&		\\
	&		\left( J_2-\lambda _2E \right) ^{s_2}&		\cdots&		\\
	\vdots&		\vdots&		&		\vdots\\
	&		&		\cdots&		{J_p}^{s_p}\\
\end{matrix} \right) \cdots \left( \begin{matrix}
	{J_1}^{s_1}&		&		\cdots&		\\
	&		{J_2}^{s_2}&		\cdots&		\\
	\vdots&		\vdots&		&		\vdots\\
	&		&		\cdots&		\left( J_m-\lambda _mE \right) ^{s_p}\\
\end{matrix} \right)\\
=\left( \begin{matrix}
	O&		&		\cdots&		\\
	&		J_{2}^{s_2}&		\cdots&		\\
	\vdots&		\vdots&		&		\vdots\\
	&		&		\cdots&		J_{p}^{s_p}\\
\end{matrix} \right) \left( \begin{matrix}
	{J_1}^{s_1}&		&		\cdots&		\\
	&		O&		\cdots&		\\
	\vdots&		\vdots&		&		\vdots\\
	&		&		\cdots&		{J_p}^{s_p}\\
\end{matrix} \right) \cdots \left( \begin{matrix}
	{J_1}^{s_1}&		&		\cdots&		\\
	&		{J_2}^{s_2}&		\cdots&		\\
	\vdots&		\vdots&		&		\vdots\\
	&		&		\cdots&		O\\
\end{matrix} \right) \\
=O
$$
