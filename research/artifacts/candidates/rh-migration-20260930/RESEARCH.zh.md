# Imported exploratory draft; admission pending

This packages prior local work for review, not a newly admitted research execution. No novelty, formal proof, verifier receipt, or root closure is asserted.

## 2. RH 根命题、否定和六个子问题

R0：ζ 为 Re(s)>1 上 Dirichlet 级数的亚纯延拓。对每个 ρ∈C，若 ζ(ρ)=0 且 0<Reρ<1，则 Reρ=1/2。否定是存在这样的 ρ 且 Reρ≠1/2；必须认证是实际 ζ 零点。仅标准复分析、解析数论等已知基础，不预设 RH、GRH 或全体零点列表。[R1]

将 ξ(s)=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/2。Li 系数 λ_n=1/(n−1)!·(d^n/ds^n)[s^(n−1)log ξ(s)]_{s=1}。零点和应使用标准对称极限，不能随意重排。以下是一个可选 Li 路线，不宣称所有路线只能这样拆。[R2]

1. R1-def：固定 ξ、log 在 1 邻域的支路和 λ_n 的导数/零点和相容性。已知理论；本包没有重新证明无穷求和交换。
2. R2-criterion：证明或准确复用 RH ⇔ ∀n≥1, λ_n≥0 的 Li 判据。已知定理；引用 Li 与 Bombieri–Lagarias，不冒充新发现。
3. R3-finite：对指定 N 认证 λ_1,…,λ_N 的区间正下界。对每个有限 N 是有界验证任务，本包未计算真实 ζ 的这些系数；下一步可选 N=10，并且必须给可审查截断/舍入界，浮点正值不算通过。
4. R4-uniform：获得对全部 n>N 有效、无 RH 假设的 λ_n 非负下界。开放核心；不能以已检查有限前缀或“主项最终支配”代替一致余项证明。
5. R5-attack：建立有限前缀验收器的人工反例测试，防止 R3 被误升格成 R4。已执行，见 §3。是路线健全性诊断，不是 R0 的充分数学前提。
6. R6-tail-audit：审计任何拟议公式 λ_n=A_n+E_n 中 E_n 的 n 一致界、求和顺序及常数。项目级下一叶子：对提案逐项标出是否使用 RH 才能得到的余项；目前尚无候选全局余项证明，故保持 open，而不是伪造一个“可计算尾项”。

依赖 DAG 的箭头 A→B 表示 B 使用 A；AND 门特别标明：R1-def→R2-criterion；R1-def→R3-finite；R1-def→R6-tail-audit→R4-uniform；{R2-criterion,R3-finite,R4-uniform}→R0 是充分路线。R5-attack→R6-tail-audit 仅是验证约束，不是推出 RH 的逻辑边。该 DAG 无环，有限支路不可绕过 uniform 门。

## 3. RH 已执行：有限 Li 前缀的对抗性精确实验

令 ρ=3/5+14i，Q={ρ,conjρ,1−ρ,1−conjρ}，定义 Λ_n(Q)=Σ_{z∈Q}[1−(1−1/z)^n]。所有 z 都在临界带，均不在临界线，Q 满足复共轭和 z↦1−z 对称。这里 Q 是人工构造，不是 ζ 零点集。

置 w=1−1/ρ，则 1−1/(1−ρ)=w^(−1)，故

Λ_n(Q)=4−2 Re(w^n+w^(−n))。

w 的实部和虚部为有理数；复数乘法可完全在 Q² 上进行。execute.py 无浮点判符号：逐项做 Fraction 乘法，检查 n=1,…,87 的分子均正，n=88 的分子负。results.json 保存第88项的完整分数；十进制约 −0.004021226817281 仅用于显示。临界线对照 β=1/2 的同长测试全部非负。

逻辑含义：一个只检查该对称结构和前87项正性的“证明验收器”，会错误接受这个临界线外点集。这足以否定这种验收规则，但不能否定 ζ 专属的更强定理；例如 Euler 乘积、实际零点计数等均未纳入这个人工模型。

进一步的解析诊断：固定 β∈(0,1)\{1/2} 及有限 K，令 ρ=β+it。当 t→∞，对固定 n，有 Λ_n=2n²/t²+O_n(t^−4)。由 w=1+i/t−β/t²+O(t^−3) 及逆元二项展开得到；奇次虚部在实部中消去。对有限的 n≤K 可取共同足够大的 t，使全部前缀为正。因此不存在仅基于此对称类的某个普遍有限前缀门槛。该观察仍不涉及实际 ζ 零点。

失败标准：任何精确符号不符合预期、公式恒等式错误、误把人工点称 ζ 零点、或将有限前缀输出映射为 solved，均判失败。已测：87项正、88项负、临界线对照通过、刻意不安全的前缀分类器确实产生假阳性。

项目推进：本次没有重复仓库已 exhausted 的大范围浮点扫描，而产出可用于后续 candidate 审核的精确负向回归样本。尚待真正攻克的是 R4；R5 不能充当突破。


## Sources and reproduction

Official source: https://www.claymath.org/wp-content/uploads/2022/05/riemann.pdf

RH Li criterion is an external dependency: Bombieri–Lagarias, JNT 77 (1999), 274–287; no full-paper verification asserted. BSD group/valuation arguments are in the draft. Run `python execute.py` in this directory (standard library; timeout 30 seconds). Finite output is only a regression check; the general BSD claim depends on the written argument.
