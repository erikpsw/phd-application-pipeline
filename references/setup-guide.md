# 配置指南 / Setup Guide

## 1. 本地工作区

建议结构：

```text
PhD/
├── data/
├── output/
├── resume/
└── scripts/
```

把 CV 放在稳定的本地路径中，但不要提交到 Git：

```text
/absolute/path/to/resume/applicant_cv.pdf
```

## 2. 飞书 / Lark CLI

安装：

```bash
npm install -g @larksuite/cli
lark-cli --version
```

配置并授权：

```bash
lark-cli config init
lark-cli auth login --domain base
lark-cli auth status
```

推荐使用用户身份：

```bash
lark-cli base +record-list \
  --as user \
  --base-token BASE_TOKEN \
  --table-id TABLE_ID \
  --view-id VIEW_ID \
  --limit 200
```

所有 Token 和 ID 都应从用户配置或环境变量读取，不要写入 Skill。

## 3. 飞书表结构

推荐字段：

```text
姓名
学校
邮件
官网链接
研究方向主线
研究方向摘要
匹配度
优先级
学校池层级
导师验证状态
邮件内容
套磁信版本
状态
下一步动作
风险备注
```

## 4. Gmail Connector

在 Codex 中安装并授权 Gmail Connector。

操作原则：

- 默认只创建草稿。
- 使用绝对路径附加 CV。
- 创建后检查收件人、主题和 `has_attachment`。
- 遇到 `token_expired` 时重新授权。

草稿结构：

```json
{
  "to": "professor@example.edu",
  "subject": "PhD Inquiry: Research Topic (Target Intake)",
  "body": "Dear Professor ...",
  "attachment_files": ["/absolute/path/applicant_cv.pdf"]
}
```

## 5. 端到端流程

1. 读取 CV 并提取研究证据。
2. 建立院校和院系池。
3. 从官方页面寻找导师。
4. 验证导师职位、邮箱、研究和实验室活跃度。
5. 写入飞书并计算匹配度。
6. 生成套磁邮件内容。
7. 审核事实、收件人、附件和重复记录。
8. 创建 Gmail 草稿。
9. 用户发送后更新为 `已发送`。
10. 定期搜索教授回复并更新状态。

## 6. 质量标准

- 教授姓名、邮箱和职位必须经过验证。
- 每封邮件必须包含至少一个具体研究连接。
- 不夸大申请人经历。
- 不声称导师会招生或有资金，除非来源明确。
- 不自动发送邮件。
