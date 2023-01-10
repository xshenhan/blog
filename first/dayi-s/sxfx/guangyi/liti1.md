
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