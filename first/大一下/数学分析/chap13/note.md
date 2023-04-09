# 第十三章知识点梳理

# 多元函数的极限与连续

## $R^2$中的点集

- 定义: 设 $\left\{\boldsymbol{x}_{k}\right\} \subset \mathbf{R}^{2}$, 其中 $\boldsymbol{x}_{k}=\left(x_{k}, y_{k}\right), k \in \mathbb{N}$, 又 $\boldsymbol{x}_{0}=\left(x_{0}, y_{0}\right)$. 若 $\forall \varepsilon>0, \exists K \in \mathbf{N}, \forall k>K$ :
  $$
  d\left(\boldsymbol{x}_{k}, \boldsymbol{x}_{0}\right)<\varepsilon
  $$
  结论 $1^{\circ}$ 若 $\left\{x_{k}\right\}$ 收敛, 则其极限点必唯一.

  ​		$2^{\circ} \lim \limits_{k \rightarrow \infty} \boldsymbol{x}_{k}=\boldsymbol{x}_{0} \Leftrightarrow \lim \limits_{k \rightarrow \infty} x_{k}=x_{0} \text { 且 } \lim \limits_{k \rightarrow \infty} y_{k}=y_{0} \text {. }$

- 内点, 外点, 边界点和聚点

  - ![image-20230409110705785](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409110705785.png)

  - 定义 设 $P_{0} \in \mathbf{R}^{2}, E \subset \mathbf{R}^{2}$, 若 $\forall \delta>0, \dot{U}\left(P_{0}, \delta\right) \cap E \neq \varnothing$, 则称 $P_{0}$ 是 $E$ 的聚点. 聚点的集合称为导集, 记为 $E^{\prime}$.

  - >内点一定是聚点，外点一定不是聚点，边界可能是也可能不是
    >
    >孤立点是边界点

  - 命题 $P_{0}$ 是 $E$ 的聚点 $\Leftrightarrow \exists\left\{P_{n}\right\} \subset E, P_{n} \neq P_{0}: \lim \limits_{n \rightarrow \infty} P_{n}=P_{0}$ 

  - 定义 设 $P_{0} \in \mathbf{R}^{2}, E \subset \mathbf{R}^{2}$, 若 $\exists \delta>0, U\left(P_{0}, \delta\right) \cap E=\left\{P_{0}\right\}$, 则称 $P_{0}$ 是 $E$ 的孤立点.

  - 定义 设 $E \subset \mathbf{R}^{2}$, 若 $E$ 中的点都是 $E$ 的内点, 即 $E=E^{\circ}$, 则称 $E$ 为开集.

  - 定义 设 $E \subset \mathbf{R}^{2}$, 若 $E$ 包含 $E$ 的所有聚点, 即 $E^{\prime} \subset E$, 则称 $E$ 为闭集. $E$ 与其导集 $E^{\prime}$ 的并集称 $E$ 的闭包, 记为 $\bar{E}$

  - ![image-20230409111258559](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409111258559.png)

  - 内部是包含于E的最大开集，闭包是包含E的最小闭集

- Cauchy准则
  - 设 $\left\{P_{n}\right\} \subset \mathbf{R}^{2}$, 则 $\left\{P_{n}\right\}$ 收玫
    $\Leftrightarrow\left\{P_{n}\right\}$ 为 Cauchy列, 即$\forall \varepsilon>0, \exists N \in \mathbb{N}, \forall n>N, \forall p \in \mathbb{N}: d\left(P_{n+p}, P_{n}\right)<\varepsilon$

- 闭集套

  - 设非空闭集列, 满足
    $$
    \begin{array}{l}
    1^{\circ} E_{n+1} \subset E_{n}(\forall n \in \mathbb{N}) ; \\
    2^{\circ} \lim \limits_{n \rightarrow \infty} \operatorname{diam}\left(E_{n}\right)=0
    \end{array}
    $$
    .则存在唯一的 $P \in E_{n}(\forall n \in \mathbf{N})$. 这里
    $$
    \operatorname{diam}(E)=\sup _{P^{\prime}, P^{\prime \prime} \in E}\left\{d\left(P^{\prime}, P^{\prime \prime}\right)\right\}
    $$
    称为 $E$ 的直径.

- 定理(Bolzana-Weierstrass) $\mathbf{R}^{2}$ 中的有界点列 $\left\{\boldsymbol{P}_{n}\right\}$ 必有收敛子列.
  定理(聚点) $\mathbf{R}^{2}$ 中的有界无限点集至少有一个聚点.

- 定义 设 $E \subset \mathbf{R}^{n}$. 若存在开集族 $\left\{G_{\lambda} \mid \lambda \in \Lambda\right\}$, 使得
  $$
  E \subset \bigcup_{\lambda \in \Lambda} G_{\lambda}
  $$
  则称 $\left\{G_{\lambda} \mid \lambda \in \Lambda\right\}$ 为 $E$ 的一个开覆盖.

- 定义 若 $E$ 的任意开覆盖 $\left\{G_{\lambda} \mid \lambda \in \Lambda\right\}$ 均存在有限子覆盖, 即存在有限个开集 $G_{\lambda_{i}}(i=1,2, \cdots, p)$ 使得 $E \subset \bigcup_{i=1}^{p} G_{\lambda_{i}}$ 则称 $E$ 为紧集.

- 有限覆盖定理(Borel) 闭区间 $[a, b]$ 为紧集.

- 紧性定理(Heine-Borel) $\mathbf{R}^{n}$ 中的点集 $E$ 为紧集
  $\Leftrightarrow E$ 为有界闭集.

## 多元函数的极限

### 二重极限

- 定义 设 $D \subset \mathbf{R}^{2}, f$ 在 $D$ 上有定义, $P_{0}$ 为 $D$ 的聚点. 若 $\exists A \in \mathbf{R}$ 使得 $\forall \varepsilon>0, \exists \delta>0, \forall P \in \stackrel{\circ}{U}\left(P_{0}, \delta\right) \cap D$ :
  \[|f(P)-A|<\varepsilon\]
  则称在 $D$ 上 $P \rightarrow P_{0}$ 时 $f(P)$ 的二重极限为 $A$, 记为
  $$
  \lim \limits_{\substack{P \rightarrow P_{0} \\ P \in D}} f(P)=A
  $$
  $P \in D$ 可以省略

- 坐标形式
  $$
  \lim \limits_{(x, y) \rightarrow\left(x_{0}, y_{0}\right)} f(x, y)=A 或 \quad \lim \limits_{\substack{x \rightarrow x_{0} \\ y \rightarrow y_{0}}} f(x, y)=A
  $$
  

![image-20230409113933309](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409113933309.png)

计算二重极限方法：

- 夹逼法
- 换元

### 累次极限

- 累次极限和二次极限没有关系
- 定理 设 $\lim \limits_{(x, y) \rightarrow\left(x_{0}, y_{0}\right)} f(x, y)=A$, 且存在首次极限 $\varphi(x)=\lim \limits_{y \rightarrow y_{0}} f(x, y)$, 则 $\lim \limits_{x \rightarrow x_{0}} \lim \limits_{y \rightarrow y_{0}} f(x, y)=A$
  推论 1 若两累次极限和二重极限均存在, 则三者相等. 一推论2 若累次极限存在但不相等, 则二重极限不存在.

### 多元函数的连续

- 定义 设 $D \subset \mathbf{R}^{2}, P_{0} \in D, f: D \rightarrow \mathbf{R}$. 若
  $$
  \forall \varepsilon>0, \exists \delta>0, \forall P \in U\left(P_{0}, \delta\right) \cap D:\left|f(P)-f\left(P_{0}\right)\right|<\varepsilon
  $$
  则称 $f(P)$ 在 $P_{0}$ 连续.

  - $D$ 上的连续函数类 $C(D)$ 

  - $D$ 的孤立点必为函数的连续点 !

  - 若 $P_{0}$ 为 $D$ 的聚点,则
    $$
    f(P) \text { 在 } P_{0} \text { 连续 } \Leftrightarrow \lim \limits_{\substack{P \rightarrow P_{0} \\ P \in D}} f(P)=f\left(P_{0}\right)
    $$

- ![image-20230409120707490](https://raw.githubusercontent.com/hanleo001/img/main/image-20230409120707490.png)

- 有界性和最值性无需连通

- 二元函数的一致连续性

- 定义 设 $D \subset \mathbf{R}^{2}, f: D \rightarrow \mathbf{R}$. 若
  $$
  \begin{array}{c}
  \forall \varepsilon>0, \exists \delta>0, \forall P^{\prime}, P^{\prime \prime} \in D, d\left(P^{\prime}, P^{\prime \prime}\right)<\delta: \\
  \left|f\left(P^{\prime}\right)-f\left(P^{\prime \prime}\right)\right|<\varepsilon
  \end{array}
  $$
  

  则称 $f$ 在 $D$ 上一致连续, 记为 $f \in U . C .(D)$

- 结论 $f$ 在 $D$ 上不一致连续的肯定叙述:
  $$
  \begin{array}{c}
  \exists \varepsilon_{0}>0, \exists P_{n}^{\prime}, P_{n}^{\prime \prime} \in D: \lim \limits_{n \rightarrow \infty} d\left(P_{n}^{\prime}, P_{n}^{\prime \prime}\right)=0 \\
  \left|f\left(P_{n}^{\prime}\right)-f\left(P_{n}^{\prime \prime}\right)\right| \geq \varepsilon_{0}
  \end{array}
  $$

- 

- 定理 (一致连续性) 设 $D \subset \mathbf{R}^{2}$ 为有界闭集, 且 $f \in C(D)$, 则 $f \in U . C .(D)$

