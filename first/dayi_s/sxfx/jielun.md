## 级数

1. 若级数$\displaystyle\sum_{n=1}^{+\infty}a_n$**绝对**收敛，则$\displaystyle\sum_{n=1}^{+\infty}a_n^2$收敛

2. 若级数$\displaystyle\sum_{n=1}^{+\infty}a_n$和级数$\displaystyle\sum_{n=1}^{+\infty}b_n$收敛，则级数$\displaystyle\sum_{n=1}^{+\infty}\min\{a_n,b_n\}$和级数$\displaystyle\sum_{n=1}^{+\infty}\max\{a_n,b_n\}$收敛

   若级数$\displaystyle\sum_{n=1}^{+\infty}a_n$和级数$\displaystyle\sum_{n=1}^{+\infty}b_n$发散，则级数$\displaystyle\sum_{n=1}^{+\infty}\max\{a_n,b_n\}$发散，但级数$\displaystyle\sum_{n=1}^{+\infty}\min\{a_n,b_n\}$未必

3. 任给一个发散的正项级数$\displaystyle\sum_{n=1}^{+\infty}a_n$，总存在一个趋向于0的数列$b_n$，使得级数$\displaystyle\sum_{n=1}^{+\infty}a_nb_n$仍然发散

   > 设$s_n$为部分和数列，考虑$\frac{s_n - s_{n-1}}{s_n}$，可以证明(Cauchy发散准则)，正项级数$\displaystyle\sum_{n=1}^{+\infty}\frac{s_{n+1} - s_{n}}{s_{n+1}}$发散，
   >
   > 注意到$s_{n+1}-s_{n}=a_{n+1}$，取$b_n=s_n$，则$\displaystyle\sum_{n=1}^{+\infty}\frac{a_{n+1}}{b_{n+1}}$发散

 4. 任给一个收敛的正项级数$\displaystyle\sum_{n=1}^{+\infty}a_n$，总存在一个趋向于0的数列$b_n$，使得级数$\displaystyle\sum_{n=1}^{+\infty}\frac{a_n}{b_n}$仍然收敛

    > 设$r_n=\displaystyle\sum_{k=n+1}^{+\infty}a_k$，取$b_n=\sqrt{r_n}+\sqrt{r_{n-1}}$

5. 