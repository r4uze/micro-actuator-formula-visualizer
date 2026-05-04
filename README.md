# Micro-Actuator Formula Visualizer

Built with Python · Streamlit · Plotly · NumPy

---

## English

### Overview

This app helps beginners understand the most fundamental formula in
micro-actuator design: **how much does a cantilever beam bend** when you
push on it?

Change beam dimensions, material, and force with simple sliders — the
deflection updates instantly on an interactive chart. No prior MEMS
knowledge needed. If you understand high-school physics, you're ready.

**The current version (v0.1) covers only cantilever beam tip deflection.**
More modules are planned for future releases.

### Features

- Interactive sliders for 5 physical parameters
- Real-time deflection calculation with SI unit conversion
- Force vs. Deflection Plotly line chart
- Educational schematic diagram (fixed end, free end, applied force)
- LaTeX-rendered formula display
- Symbol reference table with units
- Full bilingual interface — switch between English and Chinese with one click

### Formula

Cantilever beam tip deflection under a point load at the free end:

```
δ = F · L³ / (3 · E · I)
```

The moment of inertia for a rectangular cross-section:

```
I = w · t³ / 12
```

| Symbol | Meaning | Unit |
|---|---|---|
| δ | Tip deflection | μm |
| F | Applied force | μN |
| L | Beam length | μm |
| w | Beam width | μm |
| t | Beam thickness | μm |
| E | Young's modulus | GPa |
| I | Moment of inertia | μm⁴ |

All calculations use SI units internally. Slider inputs in μm, GPa,
and μN are converted automatically.

### How to Run

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/micro-actuator-formula-visualizer.git
cd micro-actuator-formula-visualizer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch the app
streamlit run app.py
```

Then open **http://localhost:8501** in your browser.

**Project structure:**

```
micro-actuator-formula-visualizer/
├── app.py               # Main application
├── requirements.txt     # Python dependencies
├── locales/             # Translations (en.json, zh-CN.json)
├── assets/              # Screenshots and diagrams
│   └── README.md
└── README.md            # You are here
```

Everything is in `app.py` — a single file you can read and modify in
one sitting.

### Screenshot

> Add a screenshot of the running app here.
>
> Recommended size: 1200×700 px.
> Place the image in `assets/` and link it:
>
> ```markdown
> ![App screenshot](assets/screenshot.png)
> ```

### Model Assumptions

- **Rectangular cross-section** — the beam has a uniform rectangular profile.
- **Small deformation** — deflection is small relative to beam length.
- **Linear elastic behavior** — material obeys Hooke's law, no plastic deformation.

### Limitations

This is a simplified educational model. It does **not** account for:

- Nonlinear deformation (large-deflection effects)
- Damping (viscous or structural)
- Dynamic response (vibration, resonance, time-dependent loads)

**This tool is not a replacement for Finite Element Method (FEM) simulation.**

### Roadmap

The current version (v0.1) covers only cantilever beam tip deflection.
Planned modules for future releases:

| Module | Description |
|---|---|
| Beam stiffness | Spring constant k = F / δ |
| Resonant frequency | Natural frequency of micro-beams |
| Piezoelectric actuation | Piezoelectric extension and force |
| Magnetic micro-actuation | Lorentz force and magnetic torque |
| Material presets | Quick-select common MEMS materials |

Contributions and ideas are welcome.

**Author:** Created by **Toufik RADI** as a beginner-friendly open-source project.

---

## 中文说明

### 项目简介

本应用帮助初学者理解微执行器设计中最基础的公式：
**悬臂梁在受力时会产生多大的挠度？**

通过简单的滑块调整梁的尺寸、材料和外力，交互式图表会实时显示挠度
变化。不需要 MEMS 背景知识，只要具备高中物理基础即可轻松上手。

**当前版本（v0.1）仅包含悬臂梁尖端挠度模块。** 更多模块计划在后
续版本中添加。

### 功能特点

- 5 个物理参数的交互式滑块
- 实时挠度计算，内置 SI 单位转换
- 施加力-挠度关系 Plotly 折线图
- 教学示意图（固定端、自由端、施加力）
- LaTeX 渲染公式显示
- 符号含义对照表（含单位）
- 完整中英文双语界面，一键切换语言

### 公式说明

悬臂梁在自由端受到集中力时的尖端挠度：

```
δ = F · L³ / (3 · E · I)
```

矩形截面的截面二次矩：

```
I = w · t³ / 12
```

| 符号 | 含义 | 单位 |
|---|---|---|
| δ | 尖端挠度 | μm |
| F | 施加力 | μN |
| L | 梁长度 | μm |
| w | 梁宽度 | μm |
| t | 梁厚度 | μm |
| E | 杨氏模量 | GPa |
| I | 截面二次矩 | μm⁴ |

所有计算均使用国际单位制（SI），滑块输入的 μm、GPa、μN 会自动转换。

### 如何运行

```bash
# 1. 克隆仓库
git clone https://github.com/YOUR_USERNAME/micro-actuator-formula-visualizer.git
cd micro-actuator-formula-visualizer

# 2. 安装依赖
pip install -r requirements.txt

# 3. 启动应用
streamlit run app.py
```

在浏览器中打开 **http://localhost:8501**。

**项目结构：**

```
micro-actuator-formula-visualizer/
├── app.py               # 主程序
├── requirements.txt     # Python 依赖
├── locales/             # 翻译文件（en.json、zh-CN.json）
├── assets/              # 截图与示意图
│   └── README.md
└── README.md            # 项目说明
```

所有代码集中在 `app.py` 这一个文件中，方便初学者阅读和修改。

### 项目截图

> 在此处添加应用运行截图。
>
> 建议尺寸：1200×700 像素。
> 将图片放入 `assets/` 文件夹中并在此处链接：
>
> ```markdown
> ![应用截图](assets/screenshot.png)
> ```

### 模型假设

- **矩形截面** —— 梁具有均匀矩形轮廓。
- **小变形** —— 挠度相对于梁长度很小。
- **线弹性行为** —— 材料遵循胡克定律，无塑性变形。

### 模型局限

本工具是一个简化教学模型，**不包含**以下内容：

- 非线性变形（大挠度效应）
- 阻尼（粘性阻尼或结构阻尼）
- 动态响应（振动、谐振、随时间变化的载荷）

**本工具不能替代有限元法（FEM）仿真。**

### 后续计划

当前版本（v0.1）仅包含悬臂梁尖端挠度模块。后续版本计划添加：

| 模块 | 说明 |
|---|---|
| 梁刚度 | 弹簧常数 k = F / δ |
| 谐振频率 | 微梁的固有频率 |
| 压电驱动 | 压电伸缩与驱动力 |
| 磁微驱动 | 洛伦兹力与磁力矩 |
| 材料预设 | 快速选择常用 MEMS 材料 |

欢迎贡献代码和提出建议。

**作者：** 本项目由 **Toufik RADI** 创建，旨在帮助初学者入门 MEMS 微执行器。
