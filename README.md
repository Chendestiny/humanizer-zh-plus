# humanizer-zh-plus: 中文深度改写器

一句话：**humanizer-zh 的 24 类模式基座 + 中文原生套路扩展 + 场景档改写纪律**——中文文本的去AI味主改刀。

## 安装

**方式一 · skills 生态**（[skills.sh](https://skills.sh) / 市场用户）：

```bash
npx skills add Chendestiny/humanizer-zh-plus
```

**方式二 · de-ai 流水线组件**：

装 [de-ai-skills](https://github.com/Chendestiny/de-ai-skills) 后，中文主改写自动路由到本技能（缺则降级 humanizer-zh）。注意中文侧是 `humanizer-zh`（24 类基座）+ 本技能（25-33 与场景纪律）两份同载——本技能刻意不重复收录基座规则。

## 它比 humanizer-zh 多了什么

| 增强项 | 说明 |
|---|---|
| 中文原生模式表 | 25-33 九条：四字格堆砌、文言虚词滥用、机械三连排比、套路开头/结尾、伪深度、工作汇报腔、虚假跨度、段落节奏均匀 |
| 场景档 | article / novel（对话豁免）/ ecommerce（合规替换）——同一技能，改网文不清对话、改带货过广告法 |
| 广告法极限词替换对照表 | 改写期内替换，不做事后补丁：合规不是换温和形容词，是写具体事实 |
| 与 slop-gauge 的读数纪律 | 改写里"是什么 AI 印记"，量表答"密度数字"，双道门禁不串位 |

基座 24 类模式全量照常生效（夸大象征、模糊归因、破折号、三段式、否定排比、系动词回避……），本技能不重复收录，见 [humanizer-zh 上游](https://github.com/op7418/Humanizer-zh)。

## 血统与致谢

MIT 基座与概念：

- [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) — 24 类模式基座（源自 blader/humanizer 的中文版）
- [blader/humanizer](https://github.com/blader/humanizer) — 模式哲学源头
- [RobinZorro86/humanizer-zh-plus](https://github.com/RobinZorro86/humanizer-zh-plus) — Pattern 34-38（四字格/文言虚词/机械排比/结尾模板）概念吸收

原 LICENSE 与编号见各上游仓库；本仓库 LICENSE 见 [LICENSE](LICENSE)。

## 许可证

MIT，见 [LICENSE](LICENSE)。
