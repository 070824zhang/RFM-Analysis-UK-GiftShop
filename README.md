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
<img width="2216" height="1377" alt="ScreenShot_2026-05-03_151947_105" src="https://github.com/user-attachments/assets/024a0268-4a9b-477e-afe7-f511ed6caf27" />

## 🎯 项目核心洞察
- **高贡献度**：通过 RFM 模型识别出占总人数 21% 的“重要价值客户”，贡献了超过 63% 的总营收。
- **数据清洗**：独立处理了 4000+ 条脏数据，包括退货订单处理及 CustomerID 缺失值清洗。
- **流失预警体系**：基于数据分布确定了 119 天 的静默流失预警线，建议针对“重点挽留客户”触发自动化召回方案。

## 🛠️ 技术栈
- **Pandas**: 指标计算与分箱逻辑
- **PyEcharts**: 动态环形图渲染
- **SQL**:模型重构与工程迭代
- **Power BI** 商业决策看板搭建
1. 项目亮点 (Project Highlights)
“本项目已从基础的 RFM 模型升级为 多维业务洞察看板 2.0，新增了用户分布与营收贡献的对比分析。”
2. 核心业务发现 (Key Business Insights)：
二八定律分析：核心客户（Champions）占比仅为 21%，但贡献了全店 63.68% 的总营收，说明维持高端客户关系是业务核心。
消费潜力洞察：重要保持客户（Loyal Customers）的人均消费金额达 £6098，是新客的 14 倍。
流失预警指标：根据数据分布，将静默时间超过 119 天的客户定义为高风险流失群体，建议触发自动化召回邮件。
3. 技术栈更新 (Tech Stack)
数据处理：Pandas (多维聚合 agg 函数应用)。
可视化：PyEcharts (利用 Page 容器实现多图表整合布局)。
部署：GitHub Pages 自动化静态网页托管。
模型重构：SQL 将 Python 逻辑重构为 SQL 存储过程，引入 CTE (公用表表达式) 实现模块化计算链路。
利用 窗口函数 NTILE 替代简单均值法进行分箱打分，有效解决了数据分布极化导致的异常退化问题，提升了在数据库端的处理效率。
商业决策看板搭建：Power BI  DAX 建模：利用时间智能函数克服了原始数据在 2010 年与 2012 年的时间截断挑战，实现了精准的 YoY 年度同比 追踪。
UI/UX 设计：采用圆角卡片化布局，配合浅灰色调视觉分层，大幅提升了信息获取效率。

