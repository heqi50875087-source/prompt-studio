# 剧本/主题 → 分镜 → 镜头提示词:AI 影像导演流水线技法卡

> 一句话:**核心不是"提示词工程",而是"导演"**。先把主题拆成"视觉主题层 + 镜头表 + 角色锚点",再让每个镜头提示词去**引用**这三样东西,而不是每条各画各的。下面是可直接套用的公式与流程。

## 来源链接(真实仓库/平台)

- 多智能体导演流水线:[HKUDS/ViMax](https://github.com/HKUDS/ViMax)(Director / Screenwriter / Producer / Video Generator 一体)
- Claude/Cursor 用「简报→多镜头分镜」技能:[aicontentskills/ai-video-storyboard-skill](https://github.com/aicontentskills/ai-video-storyboard-skill)
- Higgsfield 提示词技能(MCSLA 公式 / Soul ID / DISCIPLINE):[OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill)
- 电影化提示词资料库(Veo/Sora/Runway/Pika/Kling):[geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)
- Seedance 2.0 提示词大全(2000+,含角色一致性):[YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)
- 通用文生视频提示词集:[khanof89/awesome-video-prompts](https://github.com/khanof89/awesome-video-prompts)
- Sora 电影感提示词完整指南(ruvnet):[gist.github.com/ruvnet](https://gist.github.com/ruvnet/e20537eb50866b2d837d4d13b066bd88)
- GitHub 话题总入口:[github.com/topics/ai-filmmaking](https://github.com/topics/ai-filmmaking)
- Seedance 角色一致性实操:[vmake.ai 教程](https://vmake.ai/blog/seedance-2-0-character-consistency)
- "导演而非提示词"理念出处:[invideo 官方 FAQ](https://invideo.io/faq/how-do-you-generate-a-storyboard-from-a-script-using-ai/)

---

## 一、导演流水线:主题 → 成片的固定 7 步(套路)

源自 `ai-video-storyboard-skill` 的命名步骤 + `ViMax` 的多智能体分工。把每一步当成一道关卡,过了再往下:

1. **简报输入 Brief** — 先定 4 件事:平台、时长、调性 vibe、行动召唤 CTA。
2. **视觉主题层 Visual Theme(关键!只定一次,全片复用)** — 色板 / 灯光风格与色温 / 镜头性格(焦段·景深)/ 胶片质感(颗粒·调色)。**这一层是"一致性"的根**,后面每条提示词都引用它,不再逐条乱改美学。
3. **镜头表 Shot List** — 生成 6–18 个镜头,每镜写清:叙事功能(为什么有这镜)/ 构图 / 运镜 / 灯光方向 / 主体与动作。
4. **提示词合成 Prompt Synthesis** — 把"视觉主题层"嵌进每条镜头提示词,每条 **40–80 词**,标注时长与画幅。
5. **声音方向 Audio** — 逐镜指定同步音效/环境声。
6. **后期规格 Post** — LUT/调色、转场样式与时长、BGM 节奏与曲风、导出分辨率与帧率。
7. **叙事逻辑复盘 Narrative Rationale** — 写一句"为什么是这个镜头顺序",当作自检验收。

> ViMax 把这套拆成可自动跑的 5 个 Agent:**剧本理解(抽角色/环境/分场)→ 分镜规划(排镜头与视觉节拍)→ 资产规划(选参考图)→ 一致性校验(VLM 视觉模型查连贯)→ 视觉合成(出图并拼帧)**。个人手工做时,照这 5 个职能自检即可。

---

## 二、单条镜头提示词公式

### 公式 A:MCSLA(Higgsfield,运镜叙事最顺手)
按顺序堆叠,前者决定后者:

| 字母 | 层 | 例 |
|---|---|---|
| **M** Model | 选模型(先选,锁死下游) | Kling 3.0 |
| **C** Camera | 运镜/机位 | FPV drone weaving through the alley |
| **S** Subject | 主体 | A woman in a tactical jacket |
| **L** Look | 视觉处理(=引用视觉主题层) | Cinematic, cold blue shadows, 16:9 |
| **A** Action | 动作驱动 | She sprints, slides under a gate |

### 公式 B:Sora/通用分镜五段式(ruvnet)
**Shot Type → Camera Movement → Subject/Action → Contextual Details(灯光·色调·背景)→ Emotional/Narrative Purpose**。
骨架模板:`Begin with a [SHOT TYPE] of [SUBJECT]. [CAMERA MOVEMENT] to [ACTION]. Use [LIGHTING] to create a [MOOD].`

---

## 三、角色 & 风格一致性:具体写法(最容易翻车的部分)

把"身份"和"运动/风格"**分轨管理**(Higgsfield Soul ID 硬规则:Identity vs. Motion Separation)。落地手段:

- **先出角色定妆表(Character Sheet),再动画化**:一张多角度参考图 = 正面 front + 侧面 profile + 四分之三 three-quarter + 全身/背面,中性灯光、突出高对比识别特征。先定图,再 image-to-video。
- **@角色标签(Seedance 2.0)**:把参考图命名为 `@Character1`,等于在模型潜空间里建了"全局指针";**之后每一镜都必须显式写出这个标签**才能保住记忆链。
- **9 个参考槽的分配(Seedance 2.0,记死)**:槽 **1–3 = 脸/身份**,槽 **4–5 = 服装/造型**(写 `@Ref4`),槽 **6–7 = 灯光/风格**。身份与风格分开喂。
- **种子锁 Seed Lock**:先生成一段 4 秒身份校验片,把 Seed 写进元数据锁住,保证跨镜噪声几何一致。
- **关键帧注入 Keyframe Injection / 帧链 Frame Chaining**:每进新场景,把角色参考图重新塞进该镜的 **Start Frame**(对抗"注意力疲劳");或抓上一段成片的**最后一帧**当下一镜的参考图,长片更顺滑。
- **图生图补镜套话**:`Same person as reference, three-quarter view facing left, same clothing and accessories, consistent lighting`。
- **Kling 3.0 Character ID**:目前最稳的身份锁,自动抽取身份 embedding(脸型/体型/特征)施加到每次生成,适合不想手动管槽位时用。

---

## 四、可复用示例提示词(英文原样)

**① 短视频竖屏单镜(嵌入视觉主题层,40–80 词):**
```
Extreme close-up overhead shot of hot water pouring over fresh coffee grounds,
warm golden backlight, slow rising steam, shallow depth of field,
35mm full-frame look, subtle 16mm film grain, cinematic 1080p,
5 seconds, 9:16 vertical
```

**② 角色一致性·多镜序列(@标签 + 帧链,Seedance 风格):**
```
Shot 1: @Character1 walking through a neon-drenched Tokyo alley, low-angle tracking shot, rain reflections, cinematic teal-and-orange.
Shot 2: Extreme close-up of @Character1's eyes reflecting the neon lights, sweating, 4k cinematic, same outfit and lighting as Shot 1.
```

**③ Sora/通用五段骨架(套主题即可):**
```
Begin with a wide establishing shot of a lone hiker on a misty ridge.
Slow crane up and dolly forward to reveal a vast valley below.
Use soft golden-hour lighting and a monochromatic blue palette to create a mood of awe and solitude.
```

---

## 五、跟谁学(人/仓库/平台点名)

- **多智能体导演框架**:[HKUDS/ViMax](https://github.com/HKUDS/ViMax)(港大数据智能实验室,开源,理解整套"编剧→导演→制片"分工首选)。
- **可直接装进 Claude Code / Cursor 的分镜技能**:[aicontentskills/ai-video-storyboard-skill](https://github.com/aicontentskills/ai-video-storyboard-skill)。
- **公式党最爱**:[OSideMedia/higgsfield-ai-prompt-skill](https://github.com/OSideMedia/higgsfield-ai-prompt-skill)(MCSLA 公式、Soul ID 角色一致性、DISCIPLINE 3-3-3 框架、17 套类型模板:动作追逐/产品 UGC/恐怖/时尚/科幻/人物介绍等)。
- **提示词速查 + 工具分册**:[geekjourneyx/awesome-ai-video-prompts](https://github.com/geekjourneyx/awesome-ai-video-prompts)、[khanof89/awesome-video-prompts](https://github.com/khanof89/awesome-video-prompts)。
- **Seedance 2.0 专精**:[YouMind-OpenLab/awesome-seedance-2-prompts](https://github.com/YouMind-OpenLab/awesome-seedance-2-prompts)(2000+ 含角色一致性技巧)。
- **Sora 电影感写法**:作者 **ruvnet** 的 [Crafting Cinematic Sora Video Prompts 指南](https://gist.github.com/ruvnet/e20537eb50866b2d837d4d13b066bd88)。
- **平台层身份锁工具**:**Kling 3.0**(Character ID 身份 embedding)、**Seedance 2.0**(9 槽多参考 + @标签)、**Luma Ray3**(keyframes 首尾帧 + 角色参考)、**Runway**(image-to-video)。
- **理念金句**(invideo 创意总监):*"The real unlock isn't the tech... the skill that makes this work isn't prompting — it's directing."* —— 把自己当导演,先定主题层和分镜,再写提示词。

---

### 一页流程小抄(贴墙用)
> 定**主题层**(色/光/镜/质感)→ 排**镜头表**(6–18 镜,每镜含叙事功能)→ 出**角色定妆表**+`@标签`+锁 Seed → 每镜按 **MCSLA / 五段式** 写 40–80 词并**引用主题层** → **帧链/关键帧注入**保连贯 → 自检"镜头顺序为何如此" → 后期 LUT/转场/BGM 收口。
