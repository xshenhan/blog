
【1】$判断\int_0^{+\infty}{\sqrt[3]{\sin x}\mathrm{d}x}\text{敛散性}$
$$
\text{解：取}\varepsilon _0=\left| \int_0^{\pi}{\sqrt[3]{\sin x}\mathrm{d}x} \right|,\forall X>0,\text{取}A''=2\pi \left[ X \right] +3\pi ,A\prime=2\pi \left[ X \right] +2\pi :
\\
\left| \int_{A\prime}^{A''}{\sqrt[3]{\sin x}\mathrm{d}x} \right|=\left| \int_0^{\pi}{\sqrt[3]{\sin x}\mathrm{d}x} \right|=\varepsilon _0,\therefore \text{发散}
\\
$$
【2】$证明\int_1^{+\infty}{\frac{\sin x}{x}\mathrm{d}x}\text{收敛}$
$$
\text{证明：}\forall \varepsilon >0,\text{取}X=\max \left\{ \frac{2}{\varepsilon},2 \right\} >1,\forall A''>A\prime>X:
\\
\left| \int_{A\prime}^{A''}{\frac{\sin x}{x}\mathrm{d}x} \right|=\left| \int_{A\prime}^{A''}{\frac{1}{x}\mathrm{d}\cos x} \right|\\=\left| \frac{\cos A''}{A''}-\frac{\cos A\prime}{A\prime}+\int_{A\prime}^{A''}{\frac{\cos x}{x^2}\mathrm{d}x} \right|<\left| \frac{1}{A''} \right|+\left| \frac{1}{A\prime} \right|+\left| \int_{A\prime}^{A''}{\frac{\cos x}{x^2}\mathrm{d}x} \right|
\\
<\frac{1}{A''}+\frac{1}{A\prime}+\int_{A\prime}^{A''}{\frac{1}{x^2}\mathrm{d}x=}\frac{1}{A''}+\frac{1}{A\prime}+\frac{1}{A\prime}-\frac{1}{A''}=\frac{2}{A\prime}<\varepsilon 
\\
$$


【3】$判断\int_2^{+\infty}{\frac{1}{\sqrt[3]{x^4+x^2}}\mathrm{d}x}\text{的敛散性（易）}
\\$
$$
\text{解：}\because \lim_{x\rightarrow +\infty} \frac{x^{\frac{4}{3}}}{\sqrt[3]{x^4+x^2}}=1 \text{由}p-\text{判别法：}
\\
\int_2^{+\infty}{\frac{1}{\sqrt[3]{x^4+x^2}}\mathrm{d}x}\text{收敛}
\\
$$
【4】$讨论\int_{\mathrm{e}}^{+\infty}{\frac{\mathrm{d}x}{x^{\lambda}\ln x}}\text{敛散性}
\\$
$$
\text{当}\lambda =1\text{时：}\int_{\mathrm{e}}^{+\infty}{\frac{\mathrm{d}x}{x\ln x}}=\lim_{x\rightarrow +\infty} \ln\ln \left( x \right) =+\infty 
\\
\text{当}\lambda >1\text{时：}\lim_{x\rightarrow +\infty} x^{\frac{\lambda +1}{2}}\frac{1}{x\ln x}=\lim_{x\rightarrow +\infty} \frac{x^{\frac{\lambda -1}{2}}}{\ln x}=+\infty ,\text{由}p-\text{判别法：}
\\
\int_{\mathrm{e}}^{+\infty}{\frac{\mathrm{d}x}{x^{\lambda}\ln x}}\text{收敛}
\\
\text{当}\lambda <1\text{时：}\lim_{x\rightarrow +\infty} x^{\frac{\lambda +1}{2}}\frac{1}{x\ln x}=\lim_{x\rightarrow +\infty} \frac{1}{x^{\frac{1-\lambda}{2}}\ln x}=0,,\text{由}p-\text{判别法：}
\\
\int_{\mathrm{e}}^{+\infty}{\frac{\mathrm{d}x}{x^{\lambda}\ln x}}\text{发散}
$$
