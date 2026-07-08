# Seedance 2.0 / 即梦（ByteDance）导演级 AI 视频提示词技法卡

> 字节跳动 Seedance 2.0 是多模态视频模型（即梦 Dreamina / BytePlus ModelArk 同源）。核心心法只有一句：**像导演写分镜表那样写提示词，不要像游客写朋友圈那样描述画面**。模型听得懂摄影师在片场说的"行话"（slow dolly in），听不懂"镜头大概靠近一点"这种话。

## 来源

- BytePlus 官方·Dreamina Seedance 2.0 prompt guide：https://docs.byteplus.com/en/docs/ModelArk/2222480
- Higgsfield 完整提示词指南（运镜/VFX/分镜库）：https://higgsfield.ai/blog/seedance-prompting-guide
- Apiyi·官方 6 步公式 + 8 种运镜 + 避坑清单：https://help.apiyi.com/en/seedance-2-0-prompt-guide-video-generation-camera-style-tips-en.html
- MindStudio·时间轴分镜提示法：https://www.mindstudio.ai/blog/timeline-prompting-seedance-2-cinematic-ai-video
- Medium / Cliprise·"像导演而非游客"：https://medium.com/@cliprise/writing-seedance-2-0-prompts-like-a-director-not-a-tourist-db70af20e7b8
- Pixo·导演思维框架：https://pixo.video/blog/seedance-2-0-director-prompts
- GitHub·issastash 完整指南合集：https://github.com/issastash/AI_Complete_Prompting_Guides/blob/main/Seedance_2.0_Complete_Prompting_Guide.md

---

## 核心技法

### 1. 骨架：官方 6 步公式（60–100 词，最佳区间）
固定顺序填空，**少于此则空洞、多于 100 词则稀释指令**：
> `[Subject 主体特征] → [Action 一个具体动作] → [Environment 环境+光] → [Camera 一个运镜] → [Style 风格锚点] → [Constraints 负向约束]`
- 主体要给可视细节（发色/服装/年龄），动作用**强动词**（slams / lunges / erupts / shatters），别写情绪形容词。
- 结尾补 `Duration + 画幅 + Final beat（最后一个定格动作）`，给镜头一个明确落点。

### 2. 运镜铁律：一镜只给一个运动（最省积分、最防抖）
- **Stacking（叠运镜）是抖动/"云台坏掉"画面的头号成因**——"pans while zooming and tracking" 几乎必崩。
- 用**节奏词**（slow / smooth / gentle）而不是技术参数（fps、光圈、焦距）。
- 官方 8 种运镜词汇：`Push-in/Dolly in`（推近，情绪聚焦）· `Pull-out/Dolly out`（拉远，交代环境）· `Pan`（横摇）· `Tracking`（跟拍移动主体）· `Orbit/Arc`（环绕 360°）· `Aerial/Drone`（航拍/俯瞰）· `Handheld`（手持轻晃，纪实感）· `Fixed/Locked-off`（完全锁死）。
- POV/第一人称要**显式写出"镜头不做什么"**来锁视角：`no cuts, no zoom, natural head movement`、`her hands always visible in frame`。

### 3. 光线是"最高杠杆"——加一句光顶得上一百个形容词
- 官方原话：**若只能为提示词加一个元素来提质，就加光线描述。**
- 三段式写光：**光源 + 质感 + 行为**——`Warm afternoon light through a west-facing window`（源）/ `soft shadows`（质）/ `golden highlights on skin`（行为）。
- 高质感常用锚点：`golden hour / rim light / backlit / neon halos on wet asphalt / overcast diffused light / halation on highlights`。

### 4. 节奏：`Fast` 是最容易毁片的词
- **快运镜 + 快剪 + 复杂场景 = 必抖+伪影**。要快，**只让一个元素快**。
- 速度梯度词：`imperceptible/barely`（几乎不动）→ `slow/gentle/gradual` → `smooth/controlled` → `dynamic/swift`（慎用）。
- 慢动作打点：`RAMPS TO SLOW MOTION as [precise moment], then SNAPS BACK`，把冲击力压在精确的动作节拍上。

### 5. 结构：8–15 秒用"时间轴分镜"写（直接当分镜表）
用时间戳把一条提示词切成多个镜头，每个镜头独立给"景别 + 动作 + 运镜 + 光"：
> `[0s] Wide shot: 建场 + 主体入场 + 锁定机位 …`
> `[3s] Slow dolly forward begins, shallow DOF …`
> `[6s] now at medium shot, 主体微动作 …`
> `[8s] Rack focus + 风格锚点收束（film grain / cold blue / anamorphic flare）`
- 进阶 **3×3 分镜法**：3 个叙事阶段（建立张力 → 升级情绪/动作 → 释放收束）× 各 3 个镜头，每段 50–80 词。

### 6. VFX：用方括号内联标注，不打断叙事
- 写法：`[VFX: branching electric circuits pulsing with white-blue current, sparks jumping between fingers]`。
- 点名仿真类型而非泛泛"特效"：`volumetric dust storm / realistic sand physics / absorbed energy glow on character / motion blur on fast actions`。

### 7. 用词：把"情绪"翻译成"物理可见"
- 模型读不懂 "sad"，但读得懂 `disheveled hair / pale fingertips / shattered reflections / a single tear traces down a pale cheek`。
- 给风格锚点：导演/胶片/镜头名 → `ARRI Alexa aesthetic / anamorphic 35mm / Denis Villeneuve IMAX 70mm / shot on Sony A7S3, warm editorial grade`。
- **主体动作与镜头运动分开写**，别揉在一句里。

### 8. 负向约束：每条角色提示词都该带的"标配护栏"
- `avoid jitter and bent limbs`（角色片必带）· `avoid temporal flicker`（长序列防闪烁）· 防 `identity drift`（角色一致性）。

### 9. 多模态引用要"贴标签"说明用途
- `@image1 as the protagonist, preserve face and outfit exactly`
- `@video1 for camera movement and pacing`
- `@audio1 as the soundtrack, match energy to the beat`
- 文件上限：≤9 图 / ≤3 视频 / ≤3 音频 / 合计 ≤12；且**别让图与词冲突**（图是白天、词写 dark night 会打架）。

### 10. 避坑红线
- 角色 ≤2 个（3 人以上易乱）；提示词无结构地堆到 100 词以上会稀释指令。
- 别用空形容词（epic / amazing / beautiful / cool video）——一律换成可视细节。

---

## 可复用示例提示词（英文原样）

**示例 1 · 6 步公式压成一行（官方 Good 范例 / 动作）**
```
A skateboarder lands a clean trick in an empty dawn parking lot, camera low tracking shot then subtle rise, modern cinematic contrast, 6 seconds, 16:9, avoid jitter and bent limbs.
```

**示例 2 · 单镜电影感（完整 6 步 + 收尾定格 / 人物情绪）**
```
A man in his 50s, weathered face, gray stubble, wool cap, looks out across a cold grey sea from a wooden pier. He lifts a mug of coffee, takes a slow sip, lowers it. Windswept North Atlantic coast, faded wooden railing, small fishing boats in the distance. Medium close-up, slow dolly in. Overcast morning light, cool blue tones, salt spray haze. Shot on ARRI Alexa, shallow depth of field, muted color grade, gentle film grain. 10 seconds, 16:9. Final beat: he lowers the mug and stares further out to sea.
```

**示例 3 · 时间轴三段式广告（多镜剪辑结构 / 产品叙事）**
```
A modern professional woman, early 30s, product: a ceramic travel coffee cup, mood: morning rush turned calm.
0-5s: Medium close-up, handheld. She rushes to grab the cup from a cluttered counter, expression stressed. Warm kitchen light.
5-10s: Cut to her sitting in a moving train car, cup in hand, looking out the window. Medium shot, locked off, natural window light from the left.
10-15s: Close-up on the cup in her hands, steam rising. She takes a slow sip, eyes close briefly, the camera holds still. Soft morning sun.
Global style: shot on Sony A7S3, warm editorial grade, consistent across cuts. 15 seconds, 9:16. Final beat: she opens her eyes and looks out the window.
```

**示例 4 · 时间轴单镜·氛围反转（建场→推近→侧脸→变焦收束）**
```
[0s] Wide shot: A figure in a long coat stands at the end of an empty rain-slicked city street at night. Camera is static, framed from behind the figure. Neon signs reflect in puddles. High-contrast, low-key lighting. [3s] Slow dolly forward begins, camera closing in on the figure from behind. Rain falls in foreground, shallow depth of field with bokeh streetlights. [6s] Camera continues push in, now at medium shot. The figure turns their head slightly — profile barely visible. Tension holds. [8s] Rack focus: background city blur sharpens briefly, then returns to subject. Cinematic, 35mm film grain, desaturated with cold blue tones, anamorphic lens flare from streetlights.
```
