# 电影感 AI 视频运镜提示词技法卡

> 主题:高手怎么写"有电影感、可控运镜"的 AI 视频提示词。聚焦能直接拿来写分镜的硬技巧——镜头/运镜/VFX/光线/结构/用词/节奏。覆盖 Higgsfield、Runway、Kling、Veo、Sora 五大模型的共性套路与差异。

## 来源
- Higgsfield《Prompt Guide to Cinematic AI Videos》— https://higgsfield.ai/blog/Prompt-Guide-to-Cinematic-AI-Videos
- Higgsfield Camera Controls(50+ 运镜预设官方清单)— https://higgsfield.ai/camera-controls
- Kristopher Dunham《How to Actually Control Next-Gen Video AI: Runway, Kling, Veo, Sora》(Medium)— https://medium.com/@creativeaininja/how-to-actually-control-next-gen-video-ai-runway-kling-veo-and-sora-prompting-strategies-92ef0055658b
- LzyPrompt《AI Video Camera Movement Prompts: The 2026 Director's Cheatsheet》— https://lzyprompt.com/blog/ai-video-camera-movement-prompts/
- InVideo《The Ultimate guide on camera movements & angles for AI videos》— https://invideo.io/blog/camera-movement-guide-for-ai-video/

---

## 一、提示词万能结构(先定骨架再填肉)

高手不是写一段散文,而是按固定**插槽**填空。两套主流骨架,按镜头类型选:

- **镜头优先(运镜主导镜头用)**:`电影摄影法 + 主体 + 动作 + 环境 + 风格氛围`
  例:`slow dolly-in, medium close-up + a girl reading + turns the page + sunlit library + warm 35mm film look`
- **主体优先(表演/叙事镜头用)**:`主体 → 动作 → 运镜 → 镜头/景别 → 风格光线`
  例:`A surfer paddling out → slow tracking shot from the side → low angle → golden hour → cinematic film grain`

**铁律:模型从前往后解析,越靠前的词权重越高。** 把"这条镜头最重要的东西"放句首(运镜重要就镜头先行,表演重要就主体先行)。

Higgsfield 的写法更进一步:**把"画面 / 身份 / 运镜"拆成三段独立指令**,别揉在一句里互相打架——只有三者分开写,人物与运镜才稳定。

---

## 二、镜头与运镜(核心硬技巧)

**1. 「Dolly In / Push In」永远优于「Zoom In」。** "Zoom In" 模型往往只是放大像素 → 画面发"平";"Dolly In / Push In" 会模拟视差(前景比背景动得快)→ 出**纵深和电影感**。同理:拉远用 `Dolly Out / Pull Out`,别用 `Zoom Out`。

**2. 一条镜头只给「一个主导运镜」。** 每个镜头 2–3 个修饰词封顶、**一个主导运镜**;最干净的公式是"一个景别 + 一个运镜 + 一颗镜头",如 `medium close-up, slow dolly in, 35mm lens`。要复杂运镜最多叠 3 个(如 dolly forward + slow tilt up),再多就糊。

**3. 速度词要和运镜规模匹配**(由慢到快的标尺):
`imperceptible → slow → steady → smooth → quick → whip / fast`。小景别配慢推、大场面配快移;速度和幅度不匹配是常见翻车点。

**4. 运镜短语速查(英文直接抄进分镜)**:

| 意图 | 英文提示词写法 |
|---|---|
| 推进(带纵深) | `slow dolly in toward [subject]` / `slow push-in` |
| 拉远揭示环境 | `dolly out, revealing the [environment]` |
| 横移跟拍 | `tracking shot, camera follows [subject] from the side` |
| 360 环绕 | `360 orbit around [subject], smooth circular motion` / `smooth arc shot orbiting clockwise` |
| 摇镜 | `slow pan left across the [scene]` |
| 俯仰 | `tilt up from [foreground] to [background]` |
| 升降臂 | `crane up from low to high, revealing [scene]` |
| 急推/爆点 | `crash zoom in toward [subject's eyes]` |
| 甩镜转场 | `whip pan to [next scene]` |
| 眩晕变焦(希区柯克) | `dolly zoom in, vertigo effect, background compresses` |
| 子弹时间 | `bullet time, frozen moment, camera orbits 180° around [subject]` |
| FPV 穿越 | `FPV drone shot, fast immersive flythrough` |
| 手持纪实 | `handheld, subtle micro-movements` |
| 穿物转场 | `through object in` / `through object out` |
| 固定机位 | `static shot, locked-off, tripod-mounted, no movement` |

> Higgsfield 50+ 官方预设名(选预设 = 锁运镜,再用文字描述主体/场景):Dolly In/Out/Left/Right、Super Dolly、Dolly Zoom、Crash Zoom In/Out、Rapid Zoom、Pan/Tilt、Whip Pan、Crane Up/Down/Over The Head、Jib、**360 Orbit**、3D Rotation、Arc Left/Right、Lazy Susan、**FPV Drone**、Handheld、Snorricam、Dutch Angle、Overhead、Fisheye、Hyperlapse、Low Shutter、**Bullet Time**、Object POV、Car Grip、Car Chasing、Eyes In/Mouth In、Hero Cam、Focus Change…

---

## 三、VFX 与特效

- **把"特效"也当成一个运镜/动作来点名**:Higgsfield 一条镜头 = 主体 + 场景 + 一个明确运镜或 VFX(如 crash zoom / orbit)+ 光线 + 情绪。
- **物理碎片要写实物**:`dust, glass, and metal fragments scatter across the frame`、`sparks, smoke, debris flying`、`subtle motion blur`、`high shutter speed`。
- **光学特效**:`the sun flares in the lens` / `lens flare`、`neon reflections shift across the surface`。
- **变身/换脸类编辑用短命令**:`Make the old man look like a zombie, rotten flesh, white eyes.` / `Change the woman to an old man.`(身份编辑指令越短越准)。
- **一镜到底标签**:动作大场面加 `one continuous take, no cuts` 锁住"不剪辑、连续运动"。

---

## 四、光线与色调(情绪 80% 靠这里)

- **三要素写全:方向 + 色温 + 质感**。`golden hour from camera-left`(方向)、`warm / cool`(色温)、`hard / diffused`(软硬)。如 `overcast diffused light` 和 `golden hour, hard backlight` 情绪完全不同。
- **电影质感词**:`shallow depth of field`、`shot on 35mm / 50mm lens`、`subtle film grain`、`muted yellow-green tones`、`desaturated warm tones`、`filmic tone`。
- **用摄影师/导演名锚定整体调性**:`in the style of Roger Deakins / Denis Villeneuve / Todd Haynes`、`psychological horror realism`、`melancholic, intimate`。
- **要安静就显式写** `no music`,避免模型自动配乐毁氛围。

---

## 五、结构与节奏

- **单镜单动作**:一个 clip 只承载一个主导运镜 + 一个情绪转折,别在 5 秒里塞两段剧情。
- **时间码 beat 脚本(Kling 强项)**:`Beat 0-4s: wide establishing shot… / Beat 4-8s: camera pushes in on the vendor…`;**音画分轨**写,`Audio 0-4s: market ambience, distant synth`;**每句对白 < 5 秒**。
- **多段运镜(仅 Sora 2 / Veo 3.1 支持)**:`static for the first 2 seconds, then slow dolly-in toward the subject` / `wide shot, then crane down to eye level`。
- **情绪推进节奏**:平静铺垫 → 转折 → 爆点推到大特写,如 `the camera pushes in hard to a tight close-up at the peak of the scream`。

---

## 六、用词铁律(高手与新手的分水岭)

- **"描述作用在物体上的力,而不是物体长什么样"**(Runway 力-反应句法):多用 `heavy / dense / weighted` + `impacts / crumples / shatters`。
- **解释"为什么会发生",给因果链**(Sora 物理思维):`the glass tips on its fulcrum, liquid sloshes against the rim before breaching` —— 写出 `fulcrum / impact force / surface tension` 这类物理子模块。
- **精确 > 诗意**:模型靠精确指令出稳定结果;长段抒情会逼它"猜",短命令减少歧义。
- **运镜与主体动作分开写**:`camera dollies in` 和 `she turns her head` 各自独立,才能精确控制。
- **常见翻车**:运镜词太空("camera moves through the scene")、速度与幅度不匹配、主体运动与镜头运动互相打架。

### 各模型差异速查
- **Runway Gen-4.5**:Director Mode 认专业术语;`truck / boom / dolly` 区分横移/升降/推拉;运镜与主体分离;力-反应句法。
- **Kling 3.0**:时间码 beat 脚本;镜头/运镜先行 + 结尾补一句统一风格句保持一致性;对白每句 <5s。
- **Veo 3.1**:吃结构化/JSON 参数,`camera / subject / lighting` 分块写(如 `"key_light": "Softbox 45-degree right"`)防止概念串味;支持多段运镜。
- **Sora 2**:因果链 + 物理模块;支持 multi-stage 运镜。
- **Higgsfield**:选预设锁运镜 + 短指令描述主体场景;单一主导运镜;画面/身份/运镜三分离。

---

## 七、可复用示例提示词(英文原样,直接抄)

**① 公式短镜(B-roll / 通用,主体优先结构)** — 实证自 LzyPrompt
```
A surfer paddling out through the lineup, slow tracking shot from the side, low angle just above the water, golden hour lighting, cinematic film grain.
```

**② 产品环绕(Runway 写法:运镜分区 + 光线随镜头反应)** — 实证自 Medium 文
```
Low angle, wide shot of a futuristic sneaker on wet asphalt. Camera: Smooth arc shot orbiting the shoe clockwise, maintaining the shoe as the central focal point. Lighting: Neon reflections shift across the surface as the camera moves.
```

**③ 情绪推进特写(dolly-in + 50mm + 含对白 + no music)** — 实证自 Higgsfield 指南
```
A cinematic close-up of a middle-aged woman sitting in a softly lit vintage kitchen, looking down with a sorrowful expression. She speaks quietly, her voice trembling as she says, "I miss you so much…" A moment of silence follows, and then her lips curve into a faint, bittersweet smile. The sunlight from the lace-curtained window gently touches her face, reflecting small tears in her eyes. Shot on a 50mm lens with shallow depth of field, warm green-yellow tones, subtle film grain, intimate handheld framing, evoking emotion and loss, no music.
```

**④ 动作 / VFX 一镜到底(套用上述法则组合:crash zoom + bullet time + 物理碎片 + 镜头炫光)** — 模板
```
A lone skateboarder launches off a concrete ledge at dusk. Crash zoom in on his face mid-air, then bullet time — the camera orbits 180° around him while dust and debris hang frozen in the air. Low angle, 24mm wide lens, hard backlight with lens flare, deep teal-and-orange tones, subtle motion blur, cinematic film grain, one continuous high-energy take, no cuts.
```

---

### 一句话记忆
**Dolly 别用 Zoom;一镜一主导运镜;前置最重要的词;光线写方向+色温+软硬;描述"力"和"因果"而非外观;画面/身份/运镜三分离。**
