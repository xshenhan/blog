# 线性代数知识点总结

目录

[线性代数知识点总结](#_Toc120298685)

[第一章](#_Toc120298686)

[1.多项式和数域](#_Toc120298687)

[2.矩阵的概念和运算](#_Toc120298688)

[3.行列式的定义](#_Toc120298689)

[4.行列式的性质](#_Toc120298690)

[5.行列式按行（列）展开](#_Toc120298691)

[6. Laplace定理](#_Toc120298692)

[7.可逆矩阵](#7可逆矩阵)

[8.克莱姆法则](#8克莱姆法则)

[9.分块矩阵](#9分块矩阵)

[10行列式的计算（例题见超链接）](#10行列式的计算例题见超链接)

[11.几个特殊的矩阵](#11几个特殊的矩阵)

[12.总结](#12总结)

[第二章](#第二章)

[1.矩阵的初等变换](#1矩阵的初等变换)

[2.初等矩阵](#2初等矩阵)

[3.矩阵的秩](#3矩阵的秩)

[4.分块矩阵的初等变换](#4分块矩阵的初等变换)

[5. n维向量空间](#5-n维向量空间)

[6.方程组的解与秩](#6方程组的解与秩)

[7.向量的线性表示](#7向量的线性表示)

[8.向量组的秩](#8向量组的秩)

[9.方程组的解的性质和结构](#9方程组的解的性质和结构)

<!--more-->

# 第一章

## 1.多项式和数域

1.1多项式的带余除法：

$p\left( x \right) =s\left( x \right) q\left( x \right) +r\left( x \right) , d\mathrm{e}g\left( r\left( x \right) \right) <d\mathrm{e}g\left( s\left( x \right) \right) $

1.2多项式的根：对于复数域上的多项式：$p\left( x \right) =a_nx^n+a_{n-1}x^{n-1}+...+a_1x+a_0,a_i\in \mathbb{C} \left( 0\leqslant i\leqslant n,i\in \mathbb{Z} \right) $*p(x)*在复数域上有n个根（重根按重数计算）

1.3多项式根与系数的关系：

$l\mathrm{e}t\,\,th\mathrm{e} roots\,\,of\,\,p\left( x \right) \,\,ar\mathrm{e}:x_1,x_2,...,x_n\\th\mathrm{e}n\,\,p\left( x \right) =a_n\left( x-x_1 \right) \left( x-x_2 \right) ...\left( x-x_n \right) $

然后利用对应系数相等即可得出

1.4常见数域

有理数域：Q

实数域：R

复数域：C

1.5数域的特点：对四则运算封闭

## 2.矩阵的概念和运算

2.1求和号的重要性质：$\displaystyle\sum_{i=1}^n{\sum_{j=1}^n{a_ib_j=\sum_{j=1}^n{\sum_{i=1}^n{a_ib_j}}}}$

2.2矩阵的概念：m$\times $n个数排成的长方形数表，用圆括号或方括号括起来，称为矩阵，如：

$\left( \begin{matrix} a_{11}& a_{12}& ...& a_{1n}\\ a_{21}& a_{22}& ...& a_{2n}\\ ...& ...& ...& ...\\ a_{m1}& a_{m2}& ...& a_{mn}\\\end{matrix} \right) $

2.3特殊矩阵：

零矩阵，行矩阵（行向量），列矩阵（列向量），方阵，单位矩阵（记作*E*或*I*），对角形矩阵，数量矩阵，上（下）三角形矩阵，对称矩阵，反对称矩阵

2.4矩阵运算：

2.4.1矩阵相等：对应元素相等

2.4.2加减法：同型矩阵

性质：交换律，结合律，存在加法单位元，存在加法逆元

2.4.3数乘：若$A=\left( a_{ij} \right) _{m\times n}$，则$kA=\left( ka_{ij} \right) _{m\times n}$

性质：$1\times A=A;k(lA)=(kl)A;(k+l)A=kA+lA;k(A+B)=kA+kB$

2.4.4乘法：若$A=\left( a_{ij} \right) _{n\times p},B=\left( b_{ij} \right) _{p\times m}$，则$AB=\left( c_{ij} \right) _{n\times m}$，其中$c_{ij}=\sum_{k=1}^p{a_{ik}b_{kj}}$

性质：结合律，k(AB)=(kA)B=A(kB),左（右）分配律，AE=EA=A，AO=OA=O

方阵的幂：就是多个乘法

2.4.5矩阵的转置：若$A=\left( a_{ij} \right) _{m\times n}$，则$A^T=\left( a_{ji} \right) _{n\times m}$

性质：$\left( AB \right) ^T=B^TA^T$，$\left( A+B \right) ^T=A^T+B^T$，$k\left( A \right) ^T=\left( kA \right) ^T$

2.5补充注意：

2.5.1矩阵乘法不满足消去律（详细参见：）

2.5.2 AB=O不能推出A=O或B=O（详细参见：）

2.5.3矩阵乘法中完全平方公式和平方差一般不成立

2.5.4一种特殊矩阵的幂：

$$\mathbf{\alpha }=\left( a_1,a_2,...,a_n \right) ,\mathbf{\beta }=\left( b_{1,}b_2,...,b_n \right) ,A=\mathbf{\beta }^T\boldsymbol{\alpha }\\\therefore A^n=\left( \mathbf{\beta \alpha } \right) ^{\boldsymbol{n}}=\mathbf{\beta }^T\left( \boldsymbol{\alpha }\mathbf{\beta }^T \right) ^{n-1}\mathbf{\alpha }=\left| \left( \boldsymbol{\alpha }\mathbf{\beta } \right) \right|^{n-1}\mathbf{\beta }^T\boldsymbol{\alpha }$$

注：A的特点是：行（列）是某个行（列）的倍数

2.5.5命题：

A是实矩阵，若对于任意的$x\in \mathbb{R} ^n$，都有$x^TAx=0,\Leftrightarrow $A是反对称矩阵。证明

2.5.6命题：

设$$A_{k\times k}=\left( \begin{matrix} 0& 1& 0& \cdots& 0& 0\\ 0& 0& 1& \cdots& 0& 0\\ 0& 0& 0& \cdots& 0& 0\\ \vdots& \vdots& \vdots& & \vdots& \vdots\\ 0& 0& 0& \cdots& 0& 1\\ 0& 0& 0& \cdots& 0& 0\\\end{matrix} \right) ,f\left( n \right) =A^n$$，则有：

$$f\left( n \right) =\begin{cases} P_n& 1\leqslant n\leqslant k-1\\ O& n\geqslant k\\\end{cases}\\P_n\text{为}A_n\text{中的}1\text{向右上移动}n-1\text{位所得的矩阵}$$

## 3.行列式的定义

3.1排列和逆序数

3.2行列式的定义

3.3贡献法

3.4行列式的递归定义。见第一章--5

## 4.行列式的性质

4.1 $D=D^T$

4.2互换行列式的两列（行），行列式变号

4.3用行列式的某一行（列）乘以某个数加到另一行（列）

4.4行列式中的某一行（列）乘以一个非零的数，等于用这个数乘以行列式

推论若A为n阶方阵，则$\left| kA \right|=k^n\left| A \right|$

## 5.行列式按行（列）展开

5.1 范德蒙德行列式（Vandermonde）行列式：

$$\left( \begin{matrix} 1& 1& 1& \cdots& 1& 1\\ x_1& x_2& x_3& \cdots& x_{n-1}& x_n\\ x_{1}^{2}& x_{2}^{2}& x_{3}^{2}& \cdots& x_{n-1}^{2}& x_{n}^{2}\\ \vdots& \vdots& \vdots& & \vdots& \vdots\\ x_{1}^{n-2}& x_{2}^{n-2}& x_{3}^{n-2}& \cdots& x_{n-1}^{n-2}& x_{n}^{n-2}\\ x_{1}^{n-1}& x_{2}^{n-1}& x_{3}^{n-1}& \cdots& x_{n-1}^{n-1}& x_{n}^{n-1}\\\end{matrix} \right) =\prod_{1\leqslant i<j\leqslant n}^n{\left( x_j-x_i \right)}$$

## 6. Laplace定理

6.1定理内容：(Laplace定理)设在n阶行列式D中,取定某k行,则D位于这k行的所有k 阶子式 与它们各自对应的代数余子式的乘积之和等于行列式D,即$D=N_1A_1+N_2A_2+\cdots +N_tA_t=\sum_{i=1}^t{N_i}A_i$

6.2命题：

$$\left| \begin{matrix} X& O\\ C& Y\\\end{matrix} \right|=|X||Y|\\$$

6.3行列式的乘积法则：

$$\left| A_nB_n \right|=\left| A_n \right|\left| B_n \right|$$

6.4命题

$$\left| \begin{matrix} a_1& a_n& a_{n-1}& \cdots& a_3& a_2\\ a_2& a_1& a_n& \cdots& a_4& a_3\\ a_3& a_2& a_1& \cdots& a_5& a_4\\ \vdots& \vdots& \vdots& & \vdots& \vdots\\ a_{n-1}& a_{n-2}& a_{n-3}& \cdots& a_1& a_n\\ a_n& a_{n-1}& a_{n-2}& \cdots& a_2& a_1\\\end{matrix} \right|=\prod_{k=0}^{n-1}{f\left( \omega _k \right)}$$

证明

000$$l\mathrm{e}t\,\,f\left( \omega \right) =a_1\omega ^0+a_2\omega ^1+\cdots +a_n\omega ^{n-1}\\f\left( \omega _k \right) =a_1{\omega _k}^0+a_2{\omega _k}^1+\cdots +a_n{\omega _k}^{n-1}\\=\left( {\omega _k}^0,{\omega _k}^1,\cdots ,{\omega _k}^{n-1} \right) \left( \begin{array}{c} a_1\\ a_2\\ \vdots\\ a_n\\\end{array} \right) \\\because a_n{\omega _k}^0+a_1{\omega _k}^1+\cdots +a_{n-1}{\omega _k}^{n-1}=\omega _k\left( a_1{\omega _k}^0+a_2{\omega _k}^1+\cdots +a_n{\omega _k}^{n-1} \right) \\=\omega _k\left( {\omega _k}^0,{\omega _k}^1,\cdots ,{\omega _k}^{n-1} \right) \left( \begin{array}{c} a_1\\ a_2\\ \vdots\\ a_n\\\end{array} \right) \\\left( {\omega _k}^0,{\omega _k}^1,\cdots ,{\omega _k}^{n-1} \right) \left( \begin{matrix} a_1& a_n& a_{n-1}& \cdots& a_3& a_2\\ a_2& a_1& a_n& \cdots& a_4& a_3\\ a_3& a_2& a_1& \cdots& a_5& a_4\\ \vdots& \vdots& \vdots& & \vdots& \vdots\\ a_{n-1}& a_{n-2}& a_{n-3}& \cdots& a_1& a_n\\ a_n& a_{n-1}& a_{n-2}& \cdots& a_2& a_1\\\end{matrix} \right) \\=\left( \begin{matrix} f\left( \omega _k \right)& {\omega _k}^1f\left( \omega _k \right)& \cdots& {\omega _k}^{n-1}f\left( \omega _k \right)\\\end{matrix} \right) \\=\left( {\omega _k}^0,{\omega _k}^1,\cdots ,{\omega _k}^{n-1} \right) f\left( \omega _k \right) \\\therefore \left| \begin{matrix} 1& {\omega _1}^1& \cdots& {\omega _1}^{n-1}\\ 1& {\omega _2}^1& \cdots& \omega _{2}^{n-1}\\ \vdots& \vdots& & \vdots\\ 1& \omega _{n}^{1}& \cdots& {\omega _n}^{n-1}\\\end{matrix} \right|\left| \begin{matrix} a_1& a_n& \cdots& a_2\\ a_2& a_1& \cdots& a_3\\ \vdots& \vdots& & \vdots\\ a_n& a_{n-1}& \cdots& a_1\\\end{matrix} \right|=\left| \begin{matrix} 1& {\omega _1}^1& \cdots& {\omega _1}^{n-1}\\ 1& {\omega _2}^1& \cdots& \omega _{2}^{n-1}\\ \vdots& \vdots& & \vdots\\ 1& \omega _{n}^{1}& \cdots& {\omega _n}^{n-1}\\\end{matrix} \right|\prod_{k=0}^{n-1}{f\left( \omega _k \right)}\\\therefore \left| \begin{matrix} a_1& a_n& \cdots& a_2\\ a_2& a_1& \cdots& a_3\\ \vdots& \vdots& & \vdots\\ a_n& a_{n-1}& \cdots& a_1\\\end{matrix} \right|=\prod_{k=0}^{n-1}{f\left( \omega _k \right)}$$

## 7.可逆矩阵

7.1 定义：A为n阶方阵，若存在n阶方阵B，使得$AB=BA=E$，则称A可逆，称B为A的逆矩阵，记为$A^{-1}$7.2 对角矩阵的逆：

若对角矩阵$\left( \begin{matrix} k_1& 0& 0\\ 0& k_2& 0\\ 0& 0& k_3\\\end{matrix} \right) $可逆，则其逆矩阵为$\left( \begin{matrix} \frac{1}{k_1}& 0& 0\\ 0& \frac{1}{k_2}& 0\\ 0& 0& \frac{1}{k_3}\\\end{matrix} \right) $

7.3 A存在可逆矩阵$\Leftrightarrow $|A|$\ne $0

7.4 唯一性：若A可逆，则A的逆矩阵唯一. [证明](https://sjtueducn-my.sharepoint.com/:w:/g/personal/hxs001_sjtu_edu_cn/EUrbwbRSGExHrXpkYT3lehcBrOuRiPaR05aRLqwbOhaJSA)

7.5 伴随矩阵求逆法：

$\text{若}A\text{可逆，则}A^{-1}=\frac{A^*}{|A|}$

特别的：$\text{若}A\text{为阶矩阵，记}A=\left( \begin{matrix} a& b\\ c& d\\\end{matrix} \right) ,\text{则}A=\left( \begin{matrix} d& -b\\ -c& a\\\end{matrix} \right) $

7.6 典例1：

$$\text{设}n\text{阶方阵}A,B,A+B\text{均可逆，}\\\text{试证}A^{-1}+B^{-1}\text{可逆，并求出}A^{-1}+B^{-1}\text{的逆矩阵}\\\text{证明：}\\\because A\left( A^{-1}+B^{-1} \right) B=B+A\\\therefore \left( A^{-1}+B^{-1} \right) =A^{-1}\left( A+B \right) B^{-1}\\\therefore \left| A^{-1}+B^{-1} \right|=\left| A^{-1} \right|\left| A+B \right|\left| B^{-1} \right|\ne 0\\\therefore A^{-1}+B^{-1}\text{可逆}\\\therefore \left( A^{-1}+B^{-1} \right) ^{-1}=B\left( A+B \right) ^{-1}A=A\left( A+B \right) ^{-1}B$$

7.7 典例2：

$$\text{设}A\text{为}m\times n\text{阶矩阵，}B\text{为}n\times m\text{阶矩阵，且}E_m-AB\text{可逆}\\\text{试证：}E_n-BA\text{可逆，并求其逆矩阵表达式}\\\text{证明：}\left( E_n-BA \right) \left( E_n+B\left( E_m-AB \right) ^{-1}A \right) \\=E_n-BA+B\left( E_m-AB \right) ^{-1}A-BAB\left( E_m-AB \right) ^{-1}A\\=E_n-BA+B\left( E-AB \right) \left( E_m-AB \right) ^{-1}A\\=E_n-BA+BA\\=E_n\\\therefore \left( E_n-BA \right) ^{-1}=\left( E_n+B\left( E_m-AB \right) ^{-1}A \right) $$

7.8结论1：若A，B可逆：

$$\left( \begin{matrix} A& O\\ O& B\\\end{matrix} \right) ^{-1}=\left( \begin{matrix} A^{-1}& O\\ O& B^{-1}\\\end{matrix} \right) \\\left( \begin{matrix} O& A\\ B& O\\\end{matrix} \right) ^{-1}=\left( \begin{matrix} O& B^{-1}\\ A^{-1}& O\\\end{matrix} \right) $$

7.9结论2若A，C可逆：

$$\left( \begin{matrix} A& B\\ O& C\\\end{matrix} \right) =\left( \begin{matrix} A^{-1}& -A^{-1}BC^{-1}\\ O& C^{-1}\\\end{matrix} \right) $$

7.10定理：

$$\text{设}A\text{为方阵，且}f\left( x \right) =a_mx^m+a_{m-1}x^{m-1}+...+a_1x+a_0,\\\text{若}f\left( A \right) =0,\text{对任意满足}f\left( c \right) \ne 0,\text{则}\left( A-cE \right) \text{可逆，且}\\\left( A-cE \right) ^{-1}=-\frac{g\left( A \right)}{f\left( c \right)},\text{其中}g\left( x \right) =\frac{f\left( x \right) -f\left( c \right)}{x-c}$$

证明：

$$\text{由带余除法}:\\f\left( x \right) =\left( x-c \right) g\left( x \right) +f\left( c \right) \\f\left( A \right) =\left( A-cE \right) g\left( A \right) +f\left( c \right) E=0\\\because f\left( c \right) \ne 0\\\therefore \left( A-cE \right) \left( -\frac{g\left( A \right)}{f\left( c \right)} \right) =E\\\therefore \left( A-cE \right) \text{可逆},\text{且}\left( A-cE \right) ^{-1}=-\frac{g\left( x \right)}{f\left( c \right)}$$

## 8.克莱姆法则

8.1.内容：

$$\text{如果线性方程组：}\\\left\{ \begin{array}{c} a_{11}x_1+a_{12}x_2+\cdots +a_{1n}x_n=b_1\\ a_{21}x_1+a_{22}x_2+\cdots +a_{2n}x_n=b_2\\ \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots\\ a_{n1}x_1+a_{n2}x_2+\cdots +a_{nn}x_n=b_n\\\end{array} \right. \\\text{的系数行列式不等于}0\text{，即}\\\left| \begin{matrix} a_{11}& a_{12}& \cdots& a_{1n}\\ a_{21}& a_{22}& \cdots& a_{2n}\\ \vdots& \vdots& & \vdots\\ a_{n1}& a_{n2}& \cdots& a_{nn}\\\end{matrix} \right|\ne 0,\text{则非齐次方程组有解，并且解是唯一的，}\\\text{解可以表述为：}\\x_1=\frac{D_1}{D},x_2=\frac{D_2}{D},\cdots ,x_n=\frac{D_n}{D}\\\text{其中}D_j\text{是是把系数行列式}D\text{中第}j\text{列的元素用方程组右端的常数项代替后所得到的}n\text{阶行列式，即}$$

证明（证法2）：

$$\text{将原方程组写成矩阵方程}AX=B,\text{若系数矩阵}A\text{可逆，则解向量}X\text{为：}\\X=A^{-1}B=\frac{A^*B}{D}$$

8.2.注意：系数矩阵的行列式D$\ne $0$\Leftrightarrow $方程组解不唯一或无解**（两种情况）**

8.3一道典例的有趣解法：

求$$D=\left| \begin{matrix} 1& x_1& \cdots& x_{1}^{n-2}& x_{1}^{n}\\ 1& x_2& \cdots& x_{2}^{n-2}& x_{2}^{n}\\ 1& x_3& \cdots& x_{3}^{n-2}& x_{3}^{n}\\ \vdots& \vdots& & \vdots& \vdots\\ 1& x_n& \cdots& x_{n}^{n-2}& x_{n}^{n}\\\end{matrix} \right|$$

解：

$$\text{考虑关于}a_i\text{的线性方程组}\left\{ \begin{array}{c} a_1+x_1a_2+x_{1}^{2}a_3+\cdots +x_{1}^{n-2}a_{n-1}+x_{1}^{n-1}a_n=x_{1}^{n}\\ a_1+x_2a_2+x_{2}^{2}a_3+\cdots +x_{2}^{n-2}a_{n-1}+x_{2}^{n-1}a_n=x_{2}^{n}\\ \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots \cdots\\ a_1+x_na_2+x_{n}^{2}a_3+\cdots +x_{n}^{n-2}a_{n-1}+x_{n}^{n-1}a_n=x_{n}^{n}\\\end{array} \right. \\\text{则}D=a_n\times V_n\left( n\text{阶范德蒙行列式} \right) \\\text{考虑}n\text{次方程组}x^n-\left( a_nx^{n-1}+a_{n-1}x^{n-2}+...+a_1 \right) =0\left( * \right) \\\text{则}x_i\text{为}\left( * \right) \text{式的}n\text{个根，由根与系数的关系：}\\\sum_{i=1}^n{x_i}=a_n\\\therefore D=\sum_{i=1}^n{x_i}\times \prod_{1\leqslant i<j\leqslant n}^{}{\left( a_j-a_i \right)}$$

## 9.分块矩阵

9.1概念：定义：将矩阵A用若干条纵线和横线分成许多小矩阵，每个小矩阵称为A的一个子块，以这些子块为元素的形式上的矩阵称为分块矩阵。

9.2 基本原则：不管整体，还是局部小块，都必须符合矩阵运算规则

9.3几种常用的分块方式：分为行（列）向量，将矩阵相乘化为一个矩阵乘以一个形式上的向量

9.4分块矩阵的转置：

$$\,\,\text{设} A=\left( A_{ij} \right) _{s\times t}=\left( \begin{matrix} A_{11}& A_{12}& \cdots& A_{1t}\\ A_{21}& A_{22}& \cdots& A_{2t}\\ \cdots& \cdots& \cdots& \cdots\\ A_{s1}& A_{s2}& \cdots& A_{st}\\\end{matrix} \right) _{s\times t}, \\A^T=\left( B_{ij} \right) _{t\times s}=\left( A_{ji}^{T} \right) _{t\times s}=\left( \begin{matrix} A_{11}^{T}& A_{21}^{T}& \cdots& A_{s1}^{T}\\ A_{12}^{T}& A_{22}^{T}& \cdots& A_{s2}^{T}\\ \cdots& \cdots& \cdots& \cdots\\ A_{1t}^{T}& A_{2t}^{T}& \cdots& A_{st}^{T}\\\end{matrix} \right) _{t\times s}$$

9.5标准单位行(列)向量：

列：$$\varepsilon _j$$是$$n\times 1$$的矩阵，它的第j行为1，其余的全为0：

$$\varepsilon _1=\left( \begin{array}{c} 1\\ 0\\ \vdots\\ 0\\\end{array} \right) ,\varepsilon _2=\left( \begin{array}{c} 0\\ 1\\ \vdots\\ 0\\\end{array} \right) ,...,\varepsilon _n=\left( \begin{array}{c} 0\\ 0\\ \vdots\\ 1\\\end{array} \right) $$

特点:  
任何一个n维列向量,可以用这n个列向量(线性)表示出来.  
他们中任何一个列向量,都不能被其他向量(线性)表示出来.

行：$\varepsilon _i$是$1\times n$的矩阵，它的第i列为1，其余的全为0：

$$\begin{aligned} &\varepsilon _1=\left( \begin{matrix}{l} 1& 0& \cdots& 0\\\end{matrix} \right) ,\\ &\varepsilon _2=\left( \begin{matrix}{l} 0& 1& \cdots& 0\\\end{matrix} \right) ,...,\\ &\varepsilon _n=\left( \begin{matrix}{l} 0& 0& \cdots& 1\\\end{matrix} \right) ,\\\end{aligned}$$

特点与上类似

9.5分块对角矩阵及其运算：

$$\text{若}A=\left( \begin{matrix} A_1& O& \cdots& O\\ O& A_2& \cdots& O\\ \cdots& \cdots& \cdots& O\\ O& O& \cdots& A_s\\\end{matrix} \right) ,B=\left( \begin{matrix} B_1& O& \cdots& O\\ O& B_2& \cdots& O\\ \cdots& \cdots& \cdots& O\\ O& O& \cdots& B_s\\\end{matrix} \right) \\\left( 1 \right) \text{若}A_i,B_i\text{为同阶的方阵},\text{则}A+B=\left( \begin{matrix} A_1+B_1& O& \cdots& O\\ O& A_2+B_2& \cdots& O\\ \cdots& \cdots& \cdots& O\\ O& O& \cdots& A_s+B_s\\\end{matrix} \right) \\\left( 2 \right) \text{若}c\text{为一个数，则}cA=\left( \begin{matrix} cA_1& O& \cdots& O\\ O& cA_2& \cdots& O\\ \cdots& \cdots& \cdots& O\\ O& O& \cdots& cA_s\\\end{matrix} \right) \\\left( 3 \right) AB=\left( \begin{matrix} A_1B_1& O& \cdots& O\\ O& A_2B_2& \cdots& O\\ \cdots& \cdots& \cdots& O\\ O& O& \cdots& A_sB_s\\\end{matrix} \right) \\\left( 4 \right) A^T=\left( \begin{matrix} A_{1}^{T}& O& \cdots& O\\ O& A_{2}^{T}& \cdots& O\\ \cdots& \cdots& \cdots& O\\ O& O& \cdots& A_{s}^{T}\\\end{matrix} \right) $$

## 10行列式的计算（例题见超链接）

10.1行列式定义法（贡献法常用）

10.2化三角形法（结合Gauss消元法理解）

10.3按行列展开法（尽量多凑0）

10.4综合法（等于没说）

10.5递推法（$D_n$与$D_{n-1}$有关的时候可以考虑）

10.6消去化零法（结合10.3）

10.7拆元法

10.8加边法（有很多相同元素（或差一个倍数）的时候考虑）

10.9数学归纳法（无需多说）

10.10利用线性方程组的解

10.11利用递推多项式

10.12乘以已知多项式

10.13 Laplace定理

10.14特征值法

## 11.几个特殊的矩阵

11.1幂零矩阵

11.1.1定义：设A为n阶方阵，若存在整数m，使得$A^m=O$，则称A为幂零矩阵，称最小的整数m为幂零指数。

11.1.2[性质](https://sjtueducn-my.sharepoint.com/:w:/g/personal/hxs001_sjtu_edu_cn/Ef4WlmlE0SBOrSOBq-x2EZ4BDSn4qd-MR-dsuACkLvC68A)：(1)存在列向量$\alpha $，使得$A^{m-1}\alpha \ne 0$

(2)方程组$x_1\alpha +x_2A\alpha +\cdots +x_mA^{m-1}\alpha =0$只有零解 证明

(3)设A为n阶幂零矩阵，$A\ne 0$,A的幂零指数为n

则：$AP=P\left( \begin{matrix} 0& 1& \cdots& 0& 0\\ 0& 0& \cdots& 0& 0\\ \vdots& \vdots& & \vdots& \vdots\\ 0& 0& \cdots& 0& 1\\ 0& 0& \cdots& 0& 0\\\end{matrix} \right) $其中$P=\left( A^{n-1}\alpha ,A^{n-2}\alpha ,\cdots ,\alpha \right) $（$\alpha $为(2)中的$\alpha $）

11.2幂等矩阵

11.2.1定义：设A为n阶方阵，若$A^2=A$那么称A为幂等矩阵（也叫投影矩阵）

[性质](https://sjtueducn-my.sharepoint.com/:w:/g/personal/hxs001_sjtu_edu_cn/Ef9Iyh1_Zl1LmmVa9_efQXoBudopZNowwZlqqHw-LOj7mg)：设A为n阶幂等矩阵.令$U=\left\{ Ax|x\in \mathbb{R} ^n \right\} ,V=\left\{ x\in \mathbb{R} |Ax=0 \right\} $

1.  对任何$u\in U$都有$Au=u$
2.  对任何$v\in V$都有$Av=0$
3.  $U\bigcap{V=\left\{ 0 \right\}}$
4.  对任何向量$\alpha \in \mathbb{R} ^n$存在唯一的向量$u\in U,v\in V$使得$\alpha =u+v$

11.3对合矩阵

11.3.1定义：设A为n阶方阵，若$A^2=E$那么称A为对合矩阵（空间中的对称变换）

11.3.2[性质](https://sjtueducn-my.sharepoint.com/:w:/g/personal/hxs001_sjtu_edu_cn/ETfMyTHAhr9NlwkKlB_2BeoBmOMifsMuAZuc-ptF_1ATIA)：设A为n阶对合矩阵，令$U=\left\{ x\in \mathbb{R} ^n|Ax=x\in \mathbb{R} ^n \right\} ,V=\left\{ x\in \mathbb{R} ^n|Ax=-x \right\} $

那么：(1)$U\bigcap{V}=\left\{ 0 \right\} $

(2)对任何向量$\alpha \in \mathbb{R} ^n$，存在唯一的向量$u\in U,v\in V$使得$\alpha =u+v$

11.4周期矩阵：设A为n阶方阵，若存在正整数k，使得$A^k=E$，那么称A为周期矩阵

## 12.总结

12.1 $A^*$相关问题

12.2 f(A)=0 定理或因式分解

12.3 向量相关时 注意常数项 构造f(A)=0

<!--next chapter-->

# 第二章

## 1.矩阵的初等变换

1.1矩阵的初等行（列）变换

1.1.1行阶梯形矩阵

1.1.2简化行阶梯形矩阵—存在且唯一

存在性的证明：

$$
\text{考虑数学归纳法，对于}m\times n\text{的矩阵}A:\\\left( 1 \right) \text{当}n=1\text{时：显然成立}\\\left( 2 \right) \text{假设}n=k\text{时成立：}\\n=k+1\text{时：将}A\text{分块为}\left( M\,\,\alpha \right) \\\text{先通过初等行变换将}M\text{变为行阶梯形}M\prime\\\text{由假设可知}M\prime\text{唯一}\\\text{此时}A\text{变为}\left( M\prime \alpha \prime \right) ,\\\text{假设有}\beta \text{使得}\left( M\prime \beta \right) \text{为}A\text{的标准形}\\\text{下证}\alpha \prime=\beta \\\text{因为}\left( M\,\,\alpha \right) \text{可经初等行变换变为}\left( M\prime \beta \right) \text{和}\left( M\prime \alpha \prime \right) \,\,\\\text{则三个方程组}Mx=\alpha ,M\prime x=\alpha \prime,M\prime x=\beta \text{是同解的}\\\text{若方程组有解，取}\xi \text{为方程组的解，则有}\\\beta =M\prime\xi =M\prime\xi =\alpha \prime\\\text{若方程组无解，则}r\left( M\,\,\alpha \right) =r\left( M \right) +1\\r\left( M\prime \alpha \prime \right) =r\left( M\prime \right) +1=r\left( M \right) +1=r\left( M\,\,\alpha \right) \\r\left( M\prime \beta \right) =r\left( M\prime \right) +1=r\left( M \right) +1=r\left( M\,\,\alpha \right) \\\text{因为}\left( M\prime \alpha \prime \right) \text{是行标准形，则}\alpha \prime\text{只有第}r\left( M \right) +1\text{为}1\text{，其余行全为零}\\\text{因为}\left( M\prime \beta \right) \text{是行标准形，则}\beta \text{只有第}r\left( M \right) +1\text{为}1\text{，其余行全为零}\\\text{证毕}
$$


1.1.3矩阵的相抵标准型

1.2方程组的解法：

对于方程组$AX=b$写出其增广矩阵$\left( A,b \right) $，将其化为简化阶梯形矩阵，便可以看出解。

1.3矩阵的等价：（矩阵属于同一类）若矩阵A可经有限次初等变换变为B则称A，B等价（或相抵）

1.4等价关系：

自反性：自己与自己等价

对称性：A与B等价，B也与A等价

传递性：A可以变换成B，B也可以变成C，则A也可以变成C

## 2.初等矩阵

2.1初等矩阵：单位矩阵经过一次变换得到的矩阵

2.1每一个初等变换都对应一个初等矩阵：

2.1.1交换矩阵的i j 两行：左乘将单位矩阵交换i j两行得到的初等矩阵

2.1.2将矩阵的第i行乘以非0数k：左乘将单位矩阵第i行乘以非0数k得到的初等矩阵

2.1.3将矩阵的第i行乘以k加到第j行：左乘将单位矩阵第i行乘以k加到第j行得到的初等矩阵

推论：初等矩阵都是可逆矩阵，且其逆矩阵是同类型的初等矩阵。

2.2定理：设A为$m\times n$矩阵，则存在一系列初等矩阵$R_1,R_2,\cdots R_s$使得$R_1R_2\cdots R_nA$为（规范的）行阶梯形矩阵。

进一步，存在一系列初等矩阵$C_1,C_2,\cdots ,C_{\xi}$使得$AC_1C_2\cdots C_{\xi}$（规范的）列阶梯形矩阵。

进而，存在$R_1,R_2,\cdots R_s,C_1,C_2,\cdots ,C_t$使得$R_1R_2\cdots R_nAC_1C_2\cdots C_{\xi}$为标准型矩阵

推论：对于$m\times n$阶矩阵A，存在m阶可逆矩阵P和n阶可逆矩阵Q使得$PAQ=\left( \begin{matrix} E_r& O\\ O& O\\\end{matrix} \right) $

推论：任意可逆矩阵可写为一系列初等矩阵的乘积。

2.3初等变换法解矩阵方程：

2.3.1 AX=B

解法：$\left( \begin{matrix} A& B\\\end{matrix} \right) \rightarrow \left( \begin{matrix} E& A^{-1}B\\\end{matrix} \right) $

2.3.2 XA=B

解法：$\left( \begin{array}{c} A\\ B\\\end{array} \right) \rightarrow \left( \begin{array}{c} E\\ BA^{-1}\\\end{array} \right) $

2.3.3 AXB=C

解法：$\left( \begin{matrix} O& B\\ A& X\\\end{matrix} \right) \rightarrow A^{-1}\left( \begin{matrix} O& B\\ A& X\\\end{matrix} \right) \rightarrow \left( \begin{matrix} O& B\\ E& A^{-1}X\\\end{matrix} \right) B^{-1}\rightarrow \left( \begin{matrix} O& E\\ E& A^{-1}XB^{-1}\\\end{matrix} \right) $

2.4 矩阵A与B等价$\Leftrightarrow $存在可逆矩阵P和Q使得$B=PAQ$

$\Leftrightarrow $A与B有相同的标准形

## 3.矩阵的秩

3.1子式：m行n列的矩阵A的k阶子式：

$k\leqslant \min \left\{ m,n \right\} $，从A中取k列k行的交叉点上元素，按照他们在矩阵A中的相对位置组成的k阶行列式

3.2矩阵的秩：矩阵A中存在一个r阶子式不等于0，但是所有的r+1阶子式都等于0

基本事实：若矩阵A的所有k阶子式都等于0，则矩阵A的所有m阶子式$\left( m\geqslant k+1 \right) $都等于0

也就是：若矩阵A存在一个k阶子式不等于0，则矩阵A存在m阶子式$\left( m\leqslant k \right) $不为0

3.3矩阵秩的性质：

3.3.1唯一性

3.3.2矩阵秩的性质:

(1)唯一性;

(2) $r\left( A_{m\times n} \right) \le \min \{m,n\}$;

(3) 若矩阵A有一个r阶子式不为 0 , 则 $r(A)\ge r$;

(4) 若矩阵 $A$ 的所有r阶子式都为 0 , 则 $r(A)<r$;

(5) $r\left( A^T \right) =r(A)$;

(6)行阶梯型矩阵的秩等于其非零行的数目;

(7) n阶可逆矩阵的秩等于n 。

3.4定理：初等变换不改变矩阵的秩。

推论：设矩阵A的秩为r，即r（A）=r，则A的标准型为$\left( \begin{matrix} E_r& O\\ O& O\\\end{matrix} \right) $

推论：矩阵乘以一个可逆阵秩不变。

3.5$m\times n$矩阵$A$是列(行)满秩,

则$A$的标准型矩阵为 $\left( \begin{array}{c} E_n\\ 0\\\end{array} \right) \left( E_m\quad 0 \right) $

3.6行列满秩矩阵可以只经过初等列行变换化为标准型

3.7秩的求法：

3.7.1定义法

3.7.2初等变换法

## 4.分块矩阵的初等变换

4.1分块矩阵的初等变换：

交换分块矩阵的两行, 记为 $R_i\leftrightarrow R_j\left( C_i\leftrightarrow C_j \right) $

用一个可逆矩阵$P(Q)$左(右)乘分块的某行的各子块, 记为 $PR_i\rightarrow R_i\left( C_iQ\rightarrow C_i \right) $

用一个适当阶数的矩阵左(右)乘分块矩阵某行(列)的各子块后加至另一行的对应子块上去, 记为 $R_j+\left( A_i \right) R_i\rightarrow R_j$

4.2分块初等矩阵：

分块的单位矩阵经过一次分块初等变换所得到的矩阵称为分块初等矩阵。

4.3定理：用分块初等矩阵左(右)乘分块矩阵相当于对分块矩阵实施相应的分块初等变换

4.4行列式第一降阶定理：

设$M=\left( \begin{matrix} A& B\\ C& D\\\end{matrix} \right) $，其中A和D分别为m阶和n阶矩阵，且$\left| A \right|\ne 0$，试证: $|M|=|A|\cdot \left| D-CA^{-1}B \right|$

证明：$\because \left( \begin{matrix} A& B\\ C& D\\\end{matrix} \right) \left( \begin{matrix} E_m& -A^{-1}B\\ O& E_n\\\end{matrix} \right) =\left( \begin{matrix} A& 0\\ C& D-CA^{-1}B\\\end{matrix} \right) \\\therefore \left| \left( \begin{matrix} A& B\\ C& D\\\end{matrix} \right) \left( \begin{matrix} E_m& -A^{-1}B\\ O& E_n\\\end{matrix} \right) \right|=\left| \left( \begin{matrix} A& 0\\ C& D-CA^{-1}B\\\end{matrix} \right) \right|\\\therefore \left| M \right|\times 1=\left| A \right|\left| D-CA^{-1}B \right|$

4.5例: 设有分块矩阵 $P=\left( \begin{matrix}{l} A& B\\ O& C\\\end{matrix} \right) $, 其中 $A$ 和 $C$ 分别 是 $m$ 和 $n$ 阶可逆矩阵, 试证: 矩阵 $P$ 可逆, 并求 $P^{-1}$

解：

$$\because \left| P \right|=\left| A \right|\left| C \right|\ne 0\\\therefore P\text{可逆}\\\because \left( \begin{matrix} A& B\\ O& C\\\end{matrix} \right) \left( \begin{matrix} E_m& -A^{-1}B\\ O& E_n\\\end{matrix} \right) =\left( \begin{matrix} A& O\\ O& C\\\end{matrix} \right) \\\therefore \left( \begin{matrix} E_m& -A^{-1}B\\ O& E_n\\\end{matrix} \right) ^{-1}\left( \begin{matrix} A& B\\ O& C\\\end{matrix} \right) ^{-1}=\left( \begin{matrix} A^{-1}& O\\ O& C^{-1}\\\end{matrix} \right) \\\therefore \left( \begin{matrix} A& B\\ O& C\\\end{matrix} \right) ^{-1}=\left( \begin{matrix} E_m& -A^{-1}B\\ O& E_n\\\end{matrix} \right) \left( \begin{matrix} A^{-1}& O\\ O& C^{-1}\\\end{matrix} \right) =\left( \begin{matrix} A^{-1}& -A^{-1}BC^{-1}\\ & C^{-1}\\\end{matrix} \right) $$

4.6例：设 $A,B$ 为 $n$ 阶矩阵, 试证:

$$\left| \begin{matrix}{l} A& B\\ B& A\\\end{matrix} \right|=|A+B|\cdot |A-B|$$

证明

$$\because \left( \begin{matrix} E& -E\\ O& E\\\end{matrix} \right) \left( \begin{matrix} A& B\\ B& A\\\end{matrix} \right) \left( \begin{matrix} E& E\\ O& E\\\end{matrix} \right) \\=\left( \begin{matrix} E& -E\\ O& E\\\end{matrix} \right) \left( \begin{matrix} A& A+B\\ B& A+B\\\end{matrix} \right) \\=\left( \begin{matrix} A-B& O\\ B& A+B\\\end{matrix} \right) \\\therefore \left| \left( \begin{matrix} E& -E\\ O& E\\\end{matrix} \right) \left( \begin{matrix} A& B\\ B& A\\\end{matrix} \right) \left( \begin{matrix} E& E\\ O& E\\\end{matrix} \right) \right|=\left| \left( \begin{matrix} A-B& O\\ B& A+B\\\end{matrix} \right) \right|\\\therefore \left| \begin{matrix} A& B\\ B& A\\\end{matrix} \right|=\left| A+B \right|\cdot \left| A-B \right|$$

4.7结论:

$$\left( 1 \right) r\left( \begin{matrix} A& O\\ O& B\\\end{matrix} \right) =r\left( A \right) +r\left( B \right) \\\left( 2 \right) r\left( \begin{matrix} A& O\\ C& B\\\end{matrix} \right) \geqslant r\left( A \right) +r\left( B \right) $$

4.8例：设A为$m\times n$阵，B为$n\times m$阵($m\geqslant n$)，试证：若$\left| \lambda E_m-AB \right|=\lambda ^{m-n}\left| \lambda En-BA \right|$

## 5. n维向量空间

5.1 n维向量

5.2 运算性质: 交换律，结合律，有单位元，有逆元

5.3 子空间:$S\subseteq F^n$，且S非空。如果S对于加法与数乘封闭，那么说S是$F^n$的子空间。

5.4生成的子空间：定义: $\alpha _1,\alpha _2,\cdots ,\alpha _s$ 是 $F^n$ 中 $s$ 个元素,令

$$L\left( \alpha _1,\alpha _2,\cdots ,\alpha _s \right) =\left\{ k_1\alpha _1+k_2\alpha _2+\cdots +k_s\alpha _s\mid k_i\in P,i=1,2,\cdots s \right\} $$

称 $L\left( \alpha _1,\alpha _2,\cdots ,\alpha _s \right) $ 为由 $\alpha _1,\alpha _2,\cdots ,\alpha _s$ 生成的线性子空间。

## 6.方程组的解与秩

6.1 解的情况:

1.系数矩阵的秩=增广矩阵的秩时，有解

2.系数矩阵的秩=增广矩阵的秩，没有自由未知量n-r(A)=0)的时候，有唯一解

3.系数矩阵的秩=增广矩阵的秩，有 自由未知量-r(A)\>0 的时候，有无穷多解

4.系数矩阵的秩不等于增广矩阵的秩，无解（系数矩阵的秩+1等于增广矩阵的秩）

6.2重要推论：

设齐次线性方程组$AX=O$的系数矩阵为$m\times n$阶矩阵。

(1)当$m<n$(方程个数少于末知数个数)时,方程组$AX=O$必有非0解。

(1)当$m=n$(方程个数等于末知数个数)时,方程组$AX=O$有非0解当且仅当$|A|=0$。

6.3定理：矩阵方程组$AX=B$有解的充要条件是$r\left( A \right) =r\left( A,B \right) $

6.4试证：方程组$A^TAX=0$和$Ax=0$在实数范围内同解。

6.5试证：线性方程组AX=B有解的充分必要条件是$\left( \begin{array}{c} A^T\\ B^T\\\end{array} \right) Y=\left( \begin{array}{c} 0\\ 1\\\end{array} \right) $无解

## 7.向量的线性表示

7.1线性组合

7.2线性表示：若向量$\beta $可以由向量组$\alpha _1,\alpha _2,\cdots ,\alpha _m$线性表示，则存在$k_1,k_2\cdots k_m$使得：$k_1\alpha _1+k_2\alpha _2+\cdots +k_m\alpha _m=\beta $

即存在$K=\left( \begin{array}{c} k_1\\ k_2\\ \vdots\\ k_m\\\end{array} \right) $，使得$\left( \begin{matrix} \alpha _1& \alpha _2& \cdots& \alpha _m\\\end{matrix} \right) K=\beta $

7.3向量组的等价：设有两个向量组$\alpha _1,\alpha _2,\cdots ,\alpha _m$，$\beta _1,\beta _2,\cdots ,\beta _m$，这两个向量组可以互相线表，则称这两个向量组等价（满足：反身性，对称性，传递性）

7.4线性相关与线性无关：对于$\alpha _1,\alpha _2,\cdots ,\alpha _m$，若存在一组不全为零的数$k_1,k_2\cdots k_m$使得$k_1\alpha _1+k_2\alpha _2+\cdots +k_m\alpha _m=0$则称$\alpha _1,\alpha _2,\cdots ,\alpha _m$线性相关，否则称其线性相关。

7.5一些小结论：

1.若m个n维向量是线性无关的，那么保持这m个n维向量的分量的相对位置的任何n+k维向量仍然是线性无关的。

2.若m个n维向量是线性相关的，那么保持这m个n维向量的分量的相对位置的任何k(≤n)维向量是线性相关的。

7.6基本n维向量

$$\varepsilon _1=\left( \begin{array}{c} 1\\ 0\\ \vdots\\ 0\\\end{array} \right) ,\varepsilon _2=\left( \begin{array}{c} 0\\ 1\\ \vdots\\ 0\\\end{array} \right) ,\cdots ,\varepsilon _n=\left( \begin{array}{c} 0\\ 0\\ \vdots\\ 1\\\end{array} \right) $$

n个基本n维向量是线性无关的$\rightarrow $任意n维向量$\alpha =\left( a_1,a_2,\cdots a_n \right) $可以表示为：

$$\alpha =a_1\varepsilon _1+a_2\varepsilon _2+\cdots +a_n\varepsilon _n$$

7.7判断向量组线性相关/无关的方法：设表达式 $x_1\alpha _1+x_2\alpha _2+\cdots +x_m\alpha _m=0$ 将之看成一个以 $x_1,x_2,\cdots ,x_m$ 为未末知数的方程组, 如果能够求出一个非 0 解, 那么 $\alpha _1,\alpha _2,\cdots ,\alpha _m$ 线性相关.

7.8向量 $\alpha _1,\alpha _2,\cdots ,\alpha _m$ 线性无关, 且 $\alpha _1,\alpha _2,\cdots ,\alpha _m,\beta $ 线性相关 $\Leftrightarrow $$\beta $ 可由向量组 $\alpha _1,\alpha _2,\cdots ,\alpha _m$ 线性表出, 且表出系数唯一。

7.9例: 设 $\alpha $ 为 $n$ 维向量, 已知 $A^{n-1}\alpha \ne 0$, 但是 $A^n\alpha =0$, 试证: $\alpha ,A\alpha ,A^2\alpha ,\cdots ,A^{n-1}\alpha $ 线性无关。

## 8.向量组的秩

8.1向量组的极大线性无关组与向量组的秩

8.2定理：若向量组$\alpha_1,\alpha _2,\cdots ,\alpha _s$和向量组$\beta _1,\beta _2,\cdots ,\beta _t$满足：

（1）$\alpha_1,\alpha_2,\cdots,\alpha_s$可由$\beta _1,\beta _2,\cdots ,\beta _t$线性表出

（2）s\>t

则 $\alpha_1,\alpha_2,\cdots,\alpha_s$线性相关

推论：若向量组$\alpha_1,\alpha_2,\cdots,\alpha_s$可由向量组$\beta _1,\beta _2,\cdots ,\beta _t$线性表出，则$r\left( \alpha _1,\alpha _2,\cdots ,\alpha _s \right) \leqslant r\left( \beta _1,\beta _2,\cdots ,\beta _t \right) $

推论：等价的向量组有相同的秩

8.3 $F^n$的一个子空间M的基(dim(W))

8.4矩阵的行秩=矩阵的列秩=矩阵的秩

## 9.方程组的解的性质和结构

9.1齐次线性方程组任意解的线性组合还是方程组的解

9.2基础解系：设$\xi _1,\xi _2,\cdots .\xi _s$都是线性方程组的解，且满足：

（1）$\xi _1,\xi _2,\cdots .\xi _s$线性无关

（2）齐次线性方程组的任意一个解都可以由$\xi _1,\xi _2,\cdots .\xi _s$线性表出，

则称$\xi _1,\xi _2,\cdots .\xi _s$为线性方程组的基础解系

9.3对于方程组$AX=0$，基础解系的秩为n-r(A)

9.4非齐次线性方程组的解的结构：

特解+对应齐次线性方程组的通解

<!--next chapter-->

# 第三章

## 1.特征值的概念和性质

1.1概念

1.2注意：<u>**特征向量不是零向量**</u>

1.3一些理解

| $A\alpha=\lambda_0\alpha$ | $\Leftrightarrow$ | $(\lambda_0E-A)\alpha=0$                                |
| ------------------------- | ----------------- | ------------------------------------------------------- |
|                           | $\Leftrightarrow$ | 特征向量$\alpha$是方程组$(\lambda_0E-A)x=0$的一个非零解 |
|                           | $\Leftrightarrow$ | $r(\lambda_0E-A)<n$                                     |

| $A\alpha\not=\lambda_0\alpha$ | $\Leftrightarrow$ | 方阵$\lambda_0E-A$可逆 |
| ----------------------------- | ----------------- | ---------------------- |
|                               | $\Leftrightarrow$ | $|\lambda_0E-A|\ne0$   |



1.4$\lambda_0$对应的所有线性无关的特征向量<u>**加上0向量**</u>构成一个线性空间，是方程组$(\lambda_0E-A=0)$的解空间

1.5关于$\lambda$的n次方程$|\lambda E-A|=0$的解$\lambda_0$的重数称作$\lambda_0$的代数重数，向量方程$(\lambda_0E-A)x=0$的基础解系的向量个数称为$\lambda_0$的几何重数。

可以[证明](https://fir.leoroom.top/xxds/chapter3/jihe_daishu_chongshu.html) $\lambda_0$ 的几何重数一定小于等于 $\lambda_0$ 的代数重数 

1.6若$\lambda$是A的一个特征值，$\alpha$是对应于$\lambda$的一个特征向量,则：

>$\lambda^{-1}$是矩阵$A^{-1}$的一个特征值，$\alpha$是对应于$\lambda^{-1}$的一个特征向量
>
>$\lambda^{-1} |A|$是矩阵$A^{*}$的一个特征值，$\alpha$是对应于$\lambda^{-1} |A|$的一个特征向量

1.7 若f为多项式，$\lambda$是A的特征值，$\alpha$是对应的特征向量,则$f(\lambda)$是$f(A)$的特征向量，$\alpha$是对应的特征向量

> 若$f(A)=0$则$f(\lambda)=0$

## 2.特征向量的性质

2.1 n阶方阵A的属于不同特征值的特征向量线性无关，[证明](https://fir.leoroom.top/xxds/chapter3/characteristic_victor_1.html)

> 进而：若 $\lambda_1, \lambda_2, \cdots, \lambda_s$ 是 $A$ 的 $s$ 个两两不同的特征值, $\alpha_{i 1}, \alpha_{i 2}, \cdots, \alpha_{i r_i}$ 是对应特征值 $\lambda_i$ 的一组线性无关的特征向量,那么 $\alpha_{11}, \alpha_{12}, \cdots, \alpha_{1r_1},\alpha_{21}, \alpha_{22}, \cdots, \alpha_{2 r_2}, \cdots, \alpha_{s 1}, \alpha_{s 2}, \cdots, \alpha_{sr_1}$ 线性无关。

# 3.相似矩阵与矩阵的相似对角化

3.1 定义

3.2 所有n阶第三类初等矩阵都相似于矩阵:
$$
\left(\begin{array}{lllll}
1 & 1 & 0 & \cdots & 0 \\
0 & 1 & 0 & \cdots & 0 \\
0 & 0 & 1 & \cdots & 0 \\
\cdots & \cdots & \cdots & \cdots & \cdots \\
0 & 0 & 0 & \cdots & 1
\end{array}\right)
$$
3.3性质

>(1) 若矩阵 $A$ 与矩阵 $B$ 相似, 即 $A \sim B$, 那么矩阵 $A$ 与 矩阵 $B$ 有相同的特征多项式.
>
>(2) 若$A\sim B$ 则$A^T \sim B^T$
>
>(3) 若$A\sim B$ 则$A^{-1} \sim B^{-1}$
>
>(4) 若$A\sim B$ $f$为多项式，则$f(A)\sim f(B)$

3.4 两种视角

> $A=PBP^{-1}$
>
> $AP=PB$

3.5对角化的两个充要条件

>A有n个线性无关的特征向量
>
>A的每个特征值的几何重数都等于代数重数

## 4 几个特别的矩阵

### 4.1幂等矩阵

设A为n阶幂等矩阵，$A^2=A$,则有：

>1. 若A非零矩阵，则A的最小多项式是$f(x)=x^2-x$,进而可得A可以相似对角化
>2. 若A非零矩阵，A的特征值为0和1，其中1的代数重数和几何重数为$r(A)$,0的代数重数和几何重数均为$n-r(A)$

### 4.2对合矩阵

设A为n阶对合矩阵，$A^2=E$,则有：

> 1. 联系对称变换

### 4.3秩为1的矩阵

迹非0的情况

> 1. A可以相似对角化

迹为0的情况

> 1. A不可以相似对角化，但可以相似变换为$\left( \begin{matrix}
>    	0&		0&		0&		\cdots&		0&		0\\
>    	1&		0&		0&		\cdots&		0&		0\\
>    	0&		0&		0&		\cdots&		0&		0\\
>    	\vdots&		\vdots&		\vdots&		&		\vdots&		\vdots\\
>    	0&		0&		0&		\cdots&		0&		0\\
>    	0&		0&		0&		\cdots&		0&		0\\
>    \end{matrix} \right) $

















