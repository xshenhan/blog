# A-D判别法

$若f,g满足下列条件之一，则\int_a^bf(x)g(x)dx收敛(a,b为之一为瑕点或正负无穷)$

> - Abel:$\int_a^bf(x)dx收敛$，g(x)单调有界
> - Dirichlet: $\int_a^x f(t)dt有界(若b为瑕点或正负无穷)$，$\displaystyle\lim_{x\rightarrow b^+} g\left( x \right) =0$且$g(x)$单调

证明
$$
\left( 1 \right) b=+\infty \text{情形：}
\\
Ab\mathrm{e}l:\because g\left( x \right) \text{有界，}\therefore \exists M>0,\left| g\left( x \right) \right|<M
\\
\forall \varepsilon >0,\because \int_a^{+\infty}{f(x)dx}\text{收敛}
\\
\therefore \exists X>a,\forall A''>A\prime>X:
\\
\left| \int_{A\prime}^{A''}{f\left( x \right) \mathrm{d}x} \right|<\frac{\varepsilon}{2M}
\\
\text{由积分第二中值定理}
\\
\int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x}=g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x}
\\
\therefore \left| \int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x} \right|=\left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
\leqslant \left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x} \right|+\left| g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
<M\frac{\varepsilon}{2M}+M\frac{\varepsilon}{2M}=\varepsilon 
\\
Dirichl\mathrm{e}t:\because F\left( A \right) =\int_a^A{f(x)dx}\text{有界，}\therefore \exists M>0,\left| \int_a^A{f(x)dx} \right|<M
\\
\because \lim_{x\rightarrow +\infty} g\left( x \right) =0
\\
\therefore \exists X>a,\forall x>X:
\\
\left| g\left( x \right) \right|<\frac{\varepsilon}{2M}
\\
\text{由积分第二中值定理}
\\
\int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x}=g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x}
\\
\therefore \left| \int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x} \right|=\left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
\leqslant \left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x} \right|+\left| g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
<\frac{\varepsilon}{2M}M+\frac{\varepsilon}{2M}M=\varepsilon 
\\
\left( 2 \right) b\text{为瑕点情形：}
\\
Ab\mathrm{e}l:\because g\left( x \right) \text{有界，}\therefore \exists M>0,\left| g\left( x \right) \right|<M
\\
\forall \varepsilon >0,\because \int_a^b{f(x)dx}\text{收敛}
\\
\therefore \exists \delta >0,\forall b>A''>A\prime>b-\delta :
\\
\left| \int_{A\prime}^{A''}{f\left( x \right) \mathrm{d}x} \right|<\frac{\varepsilon}{2M}
\\
\text{由积分第二中值定理}
\\
\int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x}=g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x}
\\
\therefore \left| \int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x} \right|=\left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
\leqslant \left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x} \right|+\left| g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
<M\frac{\varepsilon}{2M}+M\frac{\varepsilon}{2M}=\varepsilon 
\\
Dirichl\mathrm{e}t:\because F\left( A \right) =\int_a^A{f(x)dx}\text{有界，}\therefore \exists M>0,\left| \int_a^A{f(x)dx} \right|<M
\\
\because \lim_{x\rightarrow b^+} g\left( x \right) =0
\\
\therefore \exists \delta >0,\forall b>x>b-\delta :
\\
\left| g\left( x \right) \right|<\frac{\varepsilon}{2M}
\\
\forall b>A''>A\prime>b-\delta :
\\
\text{由积分第二中值定理}
\\
\int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x}=g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x}
\\
\therefore \left| \int_{A\prime}^{A''}{f(x)g(x)\mathrm{d}x} \right|=\left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x}+g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
\leqslant \left| g\left( A\prime \right) \int_{A\prime}^{\xi}{f(x)\mathrm{d}x} \right|+\left| g\left( A'' \right) \int_{\xi}^{A''}{f(x)\mathrm{d}x} \right|
\\
<\frac{\varepsilon}{2M}M+\frac{\varepsilon}{2M}M=\varepsilon
$$