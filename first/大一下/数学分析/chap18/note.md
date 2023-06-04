# 第二类曲线和曲面积分  

## 第二类曲线积分  

1. 连通区域及其边界定向  

   - 

     ![](https://raw.githubusercontent.com/hanleo001/img/main/image-20230603113410967.png)

2. 两类曲线积分关系  

   - $$
     \begin{aligned} \int_{L} \boldsymbol{F} \cdot \boldsymbol{e}_{\tau} \mathrm{d} s & =\int_{L}(P \cos \alpha+Q \cos \beta) \mathrm{d} s \\ & =\int_{L} P \mathrm{~d} x+Q \mathrm{~d} y\end{aligned}
     $$

     

     

3. 具有方向性

   >  其它性质同第一类曲线积分, 如线性性和可加性.  

4. 对于空间定向曲线 $L$ :
   $$
   \boldsymbol{r}=\boldsymbol{r}(t)=x(t) \boldsymbol{i}+y(t) \boldsymbol{j}+z(t) \boldsymbol{k}, t: \alpha \rightarrow \beta
   $$
   向量场 $\boldsymbol{F}=(P, Q, R)$ 在 $L$ 上的第二类曲线积分
   $$
   \int_{L} P \mathrm{~d} x+Q \mathrm{~d} y+R \mathrm{~d} z
   $$
   的计算公式为
   $$
   \int_{\alpha}^\beta (P x^{\prime}(t) +Q y^{\prime}(t)+R z^{\prime}(t))\mathrm{~d} t
   $$
   

## Green公式及其应用  

1. 定理 设 $\boldsymbol{v}=(P, Q)$ 为平面有界闭域 $D$ 上的光滑向量场, $D$ 的边界分段光滑, 则有

$$
\oint_{\partial D^{+}} P \mathrm{~d} x+Q \mathrm{~d} y=\iint_{D}\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) \mathrm{d} x \mathrm{~d} y
$$

> 推论 设平面有界闭域 $D$ 的边界分段光滑, 则其面积
> $$
> S=\frac{1}{2} \oint_{\partial D^{+}} x \mathrm{~d} y-y \mathrm{~d} x
> $$

2. Green公式的向量形式  

设 $\boldsymbol{v}=(Q,-P), \boldsymbol{e}_{\tau}=(\cos \alpha, \cos \beta)$ 为 $\partial D^{+}$的单位切向量, 设 $\boldsymbol{n}^{\circ}$ 为 $\partial D$ 的单位外法向量, 则 $\boldsymbol{n}^{\circ}=(\cos \beta,-\cos \alpha)$, 故有
$$
\oint_{\partial D} \boldsymbol{v} \cdot \boldsymbol{n}^{\circ} \mathrm{d} s=\iint_{D} \nabla \cdot \boldsymbol{v} \mathrm{d} \sigma
$$

3. 平面曲线积分与路径无关的条件  

   - 定义 设 $D$ 为平面单连通区域. 若对任意 $A, B \in D$, 以及 任意分段光滑曲线 $L_{A B} \subset D$, 曲线积分

   $$
   \int_{L_{A B}} P \mathrm{~d} x+Q \mathrm{~d} y
   $$

   

   的值仅与 $A, B$ 有关, 而与 $L$ 无关, 则称**在 $D$ 内曲线积分与路径无关**, 此时积分可记为
   $$
   \int_{A}^{B} P \mathrm{~d} x+Q \mathrm{~d} y
   $$

   - 定理(Green) 设 $\boldsymbol{v}=(P(x, y), Q(x, y))$ 是单连通区域 $D$ 内 的光滑向量场, 则下面四条等价:
     (1) 在 $D$ 内的任一条分段光滑闭曲线 $L$ 上
     $$
     \oint_{L} P \mathrm{~d} x+Q \mathrm{~d} y=0
     $$
     (2) 在 $D$ 内曲线积分 $\int_{L} P \mathrm{~d} x+Q \mathrm{~d} y$ 与路径无关
     (3) $P \mathrm{~d} x+Q \mathrm{~d} y$ 是某函数 $\varphi(x, y)$ 的全微分, 即 $\exists \varphi$ 使得 $\mathrm{d} \varphi=P \mathrm{~d} x+Q \mathrm{~d} y$, 此时称 $\varphi$ 是 $P \mathrm{~d} x+Q \mathrm{~d} y$ 的原函数
     (4) 在 $D$ 内恒成立 
     $$
     \quad \frac{\partial Q}{\partial x} \equiv \frac{\partial P}{\partial y}
     $$

## 第二类曲面积分  

1. 双侧曲面及其定侧

   - Möbius带 非双侧曲面(单侧曲面)

   - 定侧曲面 双侧曲面 $S$ 的侧向由其法向量组确定. 选定 $S$ 的一侧为正侧, 记为 $S^{+}$, 则另一侧为负侧, 记为 $S^{-}$
     约定若曲面 $S$ 的方程为: $z=z(x, y), \quad(x, y) \in D$ 则其单位法向量
     $$
     \boldsymbol{n}^{\circ}= \pm \frac{\left(-z_{x},-z_{y}, 1\right)}{\sqrt{1+z_{x}^{2}+z_{y}^{2}}}
     $$
     选 “+”号时, 则 $\boldsymbol{n}^{\circ}=(\cos \alpha, \cos \beta, \cos \gamma)$, 其中
     $$
     \cos \gamma=\frac{1}{\sqrt{1+z_{x}^{2}+z_{y}^{2}}}>0
     $$
     故 $\boldsymbol{n}^{\circ}$ 与 $z$ 轴正向夹角 $\gamma<90^{\circ}$, 指向上侧, 规定为 $S$ 的正侧, 

     当曲面方程为$x = x (y,z), (y,z)\in D$或 $y = y(x,z) (x,z) \in D$时，类似

     注 封闭曲面规定其外侧为正侧 

2. 两类曲面积分的关系
   $$
   \begin{aligned} \iint_{S} \boldsymbol{v} \cdot \mathrm{d} \boldsymbol{S} & =\iint_{S}(P \cos \alpha+Q \cos \beta+R \cos \gamma) \mathrm{d} S \\ & =\iint_{S} P \mathrm{~d} y \mathrm{~d} z+Q \mathrm{~d} z \mathrm{~d} x+R \mathrm{~d} x \mathrm{~d} y\end{aligned}
   $$
   

3. 侧向性 第二类曲面积分与曲面的侧向有关, 且  
   $$
   \iint_{S^{-}} P \mathrm{~d} y \mathrm{~d} z+Q \mathrm{~d} z \mathrm{~d} x+R \mathrm{~d} x \mathrm{~d} y=-\iint_{S^{+}} P \mathrm{~d} y \mathrm{~d} z+Q \mathrm{~d} z \mathrm{~d} x+R \mathrm{~d} x \mathrm{~d} y
   $$
   其它性质同第一类曲面积分, 如线性性和可加性.

4. 第二类曲面积分的计算 

   定理 若定侧光滑曲面 $S$ 为
   $$
   x=x(u, v), y=y(u, v), z=z(u, v), \quad(u, v) \in D
   $$
   则
   $$
   \iint_{S} P \mathrm{~d} y \mathrm{~d} z+Q \mathrm{~d} z \mathrm{~d} x+R \mathrm{~d} x \mathrm{~d} y= \pm \iint_{D}(P A+Q B+R C) \mathrm{d} u \mathrm{~d} v
   $$
   注 其中 $\pm$ 号选择由 S 指定侧的法向量确定  



## Gauss公式

1. 定理 设 $\boldsymbol{v}=(P, Q, R)$ 为空间有界闭域 $\Omega$ 上的光滑 向量场, $\partial \Omega$ 是分片光滑闭曲面，则有

$$
\oiint_{\partial \Omega^{+}} P \mathrm{~d} y \mathrm{~d} z+Q \mathrm{~d} z \mathrm{~d} x+R \mathrm{~d} x \mathrm{~d} y=\iiint_{\Omega}\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right) \mathrm{d} V
$$

2. 散度  

定义 向量场 $\boldsymbol{v}=(P, Q, R)$ 的散度定义为
$$
\operatorname{div} \boldsymbol{v} \stackrel{\text { def }}{=} \nabla \cdot \boldsymbol{v}=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}
$$

3. Gauss公式的向量形式  

$$
\oiint_{\partial \Omega^{+}} \boldsymbol{v} \cdot \mathrm{d} \boldsymbol{S}=\iiint_{\Omega} \nabla \cdot \boldsymbol{v} \mathrm{d} V=\iiint_{\Omega} \operatorname{div} \boldsymbol{v} \mathrm{d} V
$$

## Stokes公式

1. 定理 设 $\boldsymbol{v}=(P, Q, R)$ 为空间光滑曲面 $S$ 上的光滑 向量场, $\partial S$ 是分段光滑闭曲线，则有
   $$
   \begin{aligned}
   & \oint_{\partial S} P \mathrm{~d} x+Q \mathrm{~d} y+R \mathrm{~d} z \\
   = & \iint_{S}\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}\right) \mathrm{d} y \mathrm{~d} z+\left(\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}\right) \mathrm{d} z \mathrm{~d} x+\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right) \mathrm{d} x \mathrm{~d} y
   \end{aligned}
   $$
   

   其中 $\partial S$ 的方向与 $S$ 的侧向按右手法则联系.

   借助行列式, Stokes公式可记为
   $$
   \begin{aligned}
   \oint_{\partial S} P \mathrm{~d} x+Q \mathrm{~d} y+R \mathrm{~d} z & =\iint_{S}\left|\begin{array}{ccc}
   \mathrm{d} y \mathrm{~d} z & \mathrm{~d} z \mathrm{~d} x & \mathrm{~d} x \mathrm{~d} y \\
   \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
   P & Q & R
   \end{array}\right| \\
   & =\iint_{S}\left|\begin{array}{ccc}
   \cos \alpha & \cos \beta & \cos \gamma \\
   \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
   P & Q & R
   \end{array}\right| \mathrm{d} S
   \end{aligned}
   $$
   其中 $\partial S$ 定向与 $(\cos \alpha, \cos \beta, \cos \gamma)$ 按右手法则联系

2. 旋度
   定义 向量场 $\boldsymbol{v}=(P, Q, R)$ 的旋度定义为
   $$
    \begin{aligned}
      \operatorname{rot} \boldsymbol{v} & =\left|\begin{array}{ccc}
      \boldsymbol{i} & \boldsymbol{j} & \boldsymbol{k} \\
      \frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
      P & Q & R
      \end{array}\right| \\
      & =\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z}-\frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)
      \end{aligned}
   $$

3. Stokes公式的向量形式
   记 $\boldsymbol{r}=(x, y, z)$, 则 $\mathrm{d} \boldsymbol{r}=(\mathrm{d} x, \mathrm{~d} y, \mathrm{~d} z)$, Stokes公式可写成
   $$
   \begin{aligned}
   \oint_{\partial S} \boldsymbol{v} \cdot \mathrm{d} \boldsymbol{r} & =\iint_{S} \operatorname{rot} \boldsymbol{v} \cdot \mathrm{d} S \\
   & =\iint_{S} \operatorname{rot} \boldsymbol{v} \cdot \boldsymbol{n}^{\circ} \mathrm{d} S
   \end{aligned}
   $$
   其中 $\partial S$ 的定向与 $S$ 的定侧 $\left(\boldsymbol{n}^{\circ}\right)$ 满足右手法则
   旋度物理意义
   $$
   \left.\operatorname{rot} \boldsymbol{v} \cdot \boldsymbol{n}^{\circ}\right|_{M}=\lim \limits_{S \rightarrow M} \frac{1}{\operatorname{Area}(S)} \oint_{\partial S} \boldsymbol{v} \cdot \mathrm{d} \boldsymbol{r}
   $$
   



