# 博士申请全流程 Skill

[English](README_EN.md)

一个面向 Codex 与兼容 Agent 环境的博士申请套磁工作流。它把申请人背景分析、院校与导师筛选、研究匹配、飞书进度管理、Gmail 草稿创建和教授回复分类串成一条可恢复、可审计的流水线。

## 功能

- 从 CV 和申请偏好提取研究方向与匹配关键词
- 跨 ME、CS、ECE/EECS、Robotics、ISyE 等院系寻找导师
- 优先使用学校官网、实验室主页和近期论文验证导师信息
- 使用保守评分体系评估导师匹配度
- 生成简洁、个性化且不夸大的套磁邮件
- 在飞书多维表格中维护状态、下一步动作和风险备注
- 创建附带 CV 的 Gmail 草稿并进行完整性检查
- 对教授回复进行分类并创建回复草稿
- 检测重复导师记录，支持批量任务断点恢复

## 安装

将仓库克隆到 Codex Skill 目录：

```bash
git clone https://github.com/YOUR_USERNAME/phd-application-pipeline.git \
  ~/.codex/skills/phd-application-pipeline
```

也可以复制仓库目录到其他兼容 Agent 的 skills 目录。

## 使用示例

```text
请读取我的 CV，寻找 20 位适合 Fall 2027 的机器人学博士导师，
验证导师官网与近期研究，按匹配度排序，并写入我的飞书多维表格。
```

```text
请读取最近 14 天的教授回复，更新套磁状态，
并为需要回复的邮件创建 Gmail 草稿，不要发送。
```

## 配置

Skill 不包含任何真实个人信息或凭证。使用前请准备：

- 申请人姓名、邮箱、目标入学季和研究方向
- 本地 CV 的绝对路径
- 飞书 Base Token、Table ID 和 View ID
- 已授权的 Gmail Connector
- 可访问学校官网和导师主页的网络环境

详细说明见 [references/setup-guide.md](references/setup-guide.md)。

## 推荐飞书字段

`姓名`、`学校`、`邮件`、`官网链接`、`研究方向主线`、`研究方向摘要`、`匹配度`、`优先级`、`学校池层级`、`导师验证状态`、`邮件内容`、`套磁信版本`、`状态`、`下一步动作`、`风险备注`

## 隐私与安全

- 不要把 CV、邮箱、Token、Table ID 或邮件正文提交到公开仓库。
- Skill 默认只创建邮件草稿，不会自动发送。
- 删除飞书记录前必须确认它是明确的重复项。
- 导师匹配必须基于可验证来源，禁止编造招生、资金或研究信息。

## 项目结构

```text
.
├── SKILL.md
├── README.md
├── README_EN.md
├── LICENSE
├── agents/
│   └── openai.yaml
└── references/
    ├── setup-guide.md
    └── status-taxonomy.md
```

## 贡献

欢迎提交 Issue 和 Pull Request。请确保示例数据已经匿名化，且不包含申请人的私人信息。

## 许可证

[MIT](LICENSE)
