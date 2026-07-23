# 分镜工坊（开源版）· Prompt Studio

**中文一句话 → 电影级分镜 / 生图提示词。** 打开网页就能用，无需安装。

> 🌐 **在线直接用**：https://heqi50875087-source.github.io/prompt-studio/
> 源自一线公共文化机构"零专项经费、单人执行"的 AI 视频生产实践——一支约 8 分钟开幕式宣传片、数千张生成图像与数十个视频镜头的试错沉淀。

## 能做什么

- **一句话出分镜**：输入中文场景描述 → 生成结构化分镜表 + 逐镜提示词（中文 / 英文 / 双语）
- **平台方言**：通用 / 即梦 / 小云雀——按目标平台的脾性输出提示词
- **171 条精选提示词库**：运镜、VFX、视频模板（含 Higgsfield 官方预设精选）、生图模板（中文通用），点条目即复制
- **12 张技法卡**：分镜导演、角色一致性、电影化提示词、即梦生图技法等，可一键开关"融入生成"

## 两种用法

| 场景 | 做法 |
|---|---|
| 最省事 | 打开在线版网址 → 「设置」里填一个 OpenAI 兼容 API（DeepSeek / SiliconFlow / OpenRouter…）→ 开用 |
| 本地运行 | `git clone` 本仓库 → `python3 serve.py` → 打开 http://127.0.0.1:8799（浏览器安全策略限制直接双击 index.html，需经本地服务打开；serve.py 纯标准库零依赖，且自带 CORS 代理兜底） |

**密钥安全**：API Key 只存你自己浏览器的 localStorage，不上传、不进仓库。

**接本地模型**：Ollama / LM Studio 暴露的就是 OpenAI 兼容接口——「设置」里填 `http://localhost:11434/v1` 与模型名即可，全程离线。

## 目录

```
index.html      应用本体（单文件前端）
bundle.json     系统提示词 + 平台方言块 + 技法卡全文
library.json    精选提示词库（171 条）
knowledge/      技法卡 Markdown（供直接阅读）
serve.py        可选本地服务（纯标准库，零依赖）
```

## 相关仓库

- [storyboard-prompt-kit](https://github.com/heqi50875087-source/storyboard-prompt-kit)：本工具方法层的模板库（角色参考图 / 分镜生图 / 视频硬约束 / 场景方案），适合想读方法而非用界面的同行。

## 许可

MIT。欢迎在此基础上改进完善或提出建议（issue / PR）。
