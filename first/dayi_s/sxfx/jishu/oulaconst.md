求：$1-\frac12-\frac{1}{4}+\cdots+\frac{1}{2n-1}-\frac{1}{4n-2}-\frac{1}{4n}+\cdots$之和

$\lim_{n\rightarrow \infty} S_n=\lim_{n\rightarrow \infty} S_{3n}=\sum_{n=1}^{\infty}{\left( \frac{1}{2n-1}-\frac{1}{4n-2}-\frac{1}{4n} \right)}
\\
=\sum_{n=1}^{\infty}{\left( \frac{1}{4n-2}-\frac{1}{4n} \right)}
\\
=\frac{1}{2}\lim_{n\rightarrow \infty} \left( \sum_{k=1}^n{\frac{1}{2k-1}+\frac{1}{2k}-\frac{1}{k}} \right) 
\\
=\frac{1}{2}\lim_{n\rightarrow \infty} \left( \sum_{k=1}^{2n}{\frac{1}{k}-\sum_{k=1}^n{\frac{1}{k}}} \right) 
\\
=\frac{1}{2}\left( \ln \left( 2n \right) +C+o\left( 1 \right) \right) -\frac{1}{2}\left( \ln \left( n \right) +C+o\left( 1 \right) \right) 
\\
=\frac{\ln \left( 2 \right)}{2}$

