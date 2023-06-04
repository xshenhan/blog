$$
S_{n}(f, x)=\frac{a_{0}}{2}+\sum_{k=1}^{n}\left(a_{k} \cos k x+b_{k} \sin k x\right)\\
= \frac{1}{2} \cdot \frac{1}{\pi}\int_{-\pi}^{\pi}f(t) \mathrm{~d}t +\frac{1}{\pi}\sum_{k=1}^{n}\int_{-\pi}^{\pi}f(t)(\cos kt\cos kx+\sin k t \sin kx)\mathrm{~d}t\\
=\frac{1}{2} \cdot \frac{1}{\pi}\int_{-\pi}^{\pi}f(t) \mathrm{~d}t +\frac{1}{\pi} \int_{-\pi}^{\pi}f(t)\sum_{k=1}^{n}(\cos k(t-x))\mathrm{~d}t\\
=\frac{1}{\pi} \int_{-\pi}^{\pi} f(x+u) \frac{\sin \frac{2 n+1}{2} u}{2 \sin \frac{u}{2}} \mathrm{~d} u\ \ (u=t-x)
$$

