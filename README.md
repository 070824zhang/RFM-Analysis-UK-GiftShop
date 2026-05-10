# RFM-Analysis-UK-GiftShop
A customer segmentation project using Python (Pandas/PyEcharts) on UK retail data.
# 英国零售商客户价值挖掘 (RFM模型)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![PyEcharts](https://img.shields.io/badge/Visual-PyEcharts-orange.svg)](https://pyecharts.org/)

## 📈 项目演示
👉 **[点击此处在线查看交互式可视化图表](https://070824zhang.github.io/RFM-Analysis-UK-GiftShop/index.html)**
功能说明：

双圆环图对比：一眼看清“客户数量占比”与“营收贡献占比”的巨大差距。

横向均值柱状图：横向对比不同层级客户的真实消费能力。

Power BI效果图：
<img width="2216" height="1377" alt="ScreenShot_2026-05-03_151947_105" src="https://github.com/user-attachments/assets/024a0268-4a9b-477e-afe7-f511ed6caf27" />
AB测试结果：
<img width="747" height="378" alt="ScreenShot_2026-05-10_133511_200" src="https://github.com/user-attachments/assets/a5400b89-b9b9-4911-8f09-8f68ed09a5e5" />

## 🎯 项目核心洞察
- **高贡献度**：通过 RFM 模型识别出占总人数 21% 的“重要价值客户”，贡献了超过 63% 的总营收。
- **数据清洗**：独立处理了 4000+ 条脏数据，包括退货订单处理及 CustomerID 缺失值清洗。
- **流失预警体系**：基于数据分布确定了 119 天 的静默流失预警线，建议针对“重点挽留客户”触发自动化召回方案。
- **针对客户流失的策略**：通过AB测试发现优惠券发放策略可有效提升转化率

## 🛠️ 技术栈
- **Pandas**: 指标计算与分箱逻辑
- **PyEcharts**: 动态环形图渲染
- **SQL**:模型重构与工程迭代
- **Power BI**：商业决策看板搭建
- **AB测试**：制定策略
1. 项目亮点 (Project Highlights)
“本项目已从基础的 RFM 模型升级为 多维业务洞察看板 2.0，新增了用户分布与营收贡献的对比分析。”

3. 核心业务发现 (Key Business Insights)：
二八定律分析：核心客户（Champions）占比仅为 21%，但贡献了全店 63.68% 的总营收，说明维持高端客户关系是业务核心。
消费潜力洞察：重要保持客户（Loyal Customers）的人均消费金额达 £6098，是新客的 14 倍。
流失预警指标：根据数据分布，将静默时间超过 119 天的客户定义为高风险流失群体，建议触发自动化召回邮件。

4. 技术栈更新 (Tech Stack)
数据处理：Pandas (多维聚合 agg 函数应用)。
可视化：PyEcharts (利用 Page 容器实现多图表整合布局)。
部署：GitHub Pages 自动化静态网页托管。
模型重构：SQL 将 Python 逻辑重构为 SQL 存储过程，引入 CTE (公用表表达式) 实现模块化计算链路。
利用 窗口函数 NTILE 替代简单均值法进行分箱打分，有效解决了数据分布极化导致的异常退化问题，提升了在数据库端的处理效率。
商业决策看板搭建：Power BI  DAX 建模：利用时间智能函数克服了原始数据在 2010 年与 2012 年的时间截断挑战，实现了精准的 YoY 年度同比 追踪。
UI/UX 设计：采用圆角卡片化布局，配合浅灰色调视觉分层，大幅提升了信息获取效率。
AB测试：针对将要流失客户指定合适的策略来提高用户留存。

🚀 Phase 2: Marketing Strategy Validation (A/B Testing)
策略验证阶段：A/B 测试实战
Context / 背景: After identifying At-Risk customers in Phase 1, I designed a coupon intervention to prevent churn. To ensure the effectiveness of this strategy, a randomized controlled trial (A/B Test) was conducted.
在第一阶段识别出“受损客户（At-Risk）”后，我设计了优惠券干预方案以防止流失。为验证该策略的有效性，我开展了一场随机对照实验（A/B 测试）。
Experimental Design / 实验设计: * Targeting / 目标人群: 918 users identified as 'At-Risk'. (918名受损客户)
Randomization / 随机分流: Users were split 1:1 into Control and Treatment groups using SQL MOD(CustomerID, 2). (利用 SQL 对用户 ID 取模，实现 1:1 均匀分流)
Infrastructure / 工程落地: Built an automated data pipeline using Python (SQLAlchemy) to fetch data directly from the MySQL database, replacing manual exports. (使用 Python SQLAlchemy 构建自动化数据链路，直接从数据库提取数据)
Statistical Analysis / 统计分析: I performed a Proportions Z-Test to compare the re-purchase rates.
我使用了比例 Z 检验来对比两组的复购转化率。
Control Group Conv. Rate (对照组转化率): 5.01%
Treatment Group Conv. Rate (实验组转化率): 8.93%
P-Value (P 值): 0.0197 (At 95% confidence level / 在 95% 置信水平下)
Conclusion / 最终结论: The P < 0.05 indicates that the 78% relative lift in conversion is statistically significant. The coupon strategy is proven effective for churn prevention and is recommended for full-scale rollout.
P < 0.05 表明转化率 78% 的相对提升在统计学上是显著的。证明优惠券策略对防止流失有效，建议全量推广。
