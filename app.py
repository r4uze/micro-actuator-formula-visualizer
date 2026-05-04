"""
Micro-Actuator Formula Visualizer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A beginner-friendly Streamlit app for visualizing
MEMS micro-actuator formulas.

Created by Toufik RADI.
"""

import json
import streamlit as st
import numpy as np
import plotly.graph_objects as go


# ---------- i18n helpers ----------

def load_translations(lang_code):
    """Load the JSON translation file for the given language code."""
    path = f"locales/{lang_code}.json"
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def t(key):
    """Return the translated string for the given dot-notation key."""
    tr = st.session_state.get("translations", {})
    for part in key.split("."):
        tr = tr.get(part, key)
    return tr


# ---------- Session state init ----------

if "language" not in st.session_state:
    st.session_state["language"] = "en"

# Load translations on every rerun so language changes take effect
st.session_state["translations"] = load_translations(st.session_state["language"])

# Initialize parameter defaults (only on first load)
defaults = {
    "param_L": 200,
    "param_w": 20,
    "param_t": 5,
    "param_E": 170,
    "param_F": 10.0,
}
for key, val in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ---------- Page config ----------
st.set_page_config(
    page_title=t("app.title"),
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------- Custom CSS ----------
st.markdown("""
<style>
    /* --- Page background --- */
    .stApp {
        background-color: #f8fafc;
    }

    /* --- Main content padding --- */
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 2rem !important;
    }

    /* --- Title --- */
    .stApp h1 {
        font-size: 1.75rem !important;
        font-weight: 700 !important;
        color: #1e293b !important;
        margin-bottom: 0.25rem !important;
    }

    /* --- Subheaders --- */
    .stApp h3 {
        font-weight: 600 !important;
        color: #334155 !important;
        border-left: 3px solid #2563eb;
        padding-left: 0.75rem !important;
        margin-top: 1.75rem !important;
        margin-bottom: 0.75rem !important;
    }

    /* --- Metric cards --- */
    [data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 0.75rem 1rem;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }
    [data-testid="stMetricLabel"] {
        font-size: 0.8rem !important;
        color: #64748b !important;
    }
    [data-testid="stMetricValue"] {
        font-size: 1.35rem !important;
        font-weight: 600 !important;
        color: #1e293b !important;
    }

    /* --- Language switch button --- */
    div[data-testid="column"] button[kind="secondary"] {
        border: 1px solid #cbd5e1;
        border-radius: 6px;
        background: #ffffff;
        color: #475569;
        font-size: 0.875rem;
        padding: 0.35rem 0.9rem;
        transition: all 0.15s ease;
    }
    div[data-testid="column"] button[kind="secondary"]:hover {
        border-color: #2563eb;
        color: #2563eb;
        background: #eff6ff;
    }

    /* --- Dividers --- */
    hr {
        border-color: #e2e8f0 !important;
        margin: 1.25rem 0 !important;
    }

    /* --- Info boxes --- */
    .stAlert {
        border-radius: 8px !important;
        background-color: #eff6ff !important;
        border-left: 3px solid #2563eb !important;
        color: #1e40af !important;
    }

    /* --- Caption text --- */
    .stCaption {
        color: #94a3b8 !important;
        font-size: 0.8rem !important;
    }
    .stCaption p {
        font-size: 0.8rem !important;
    }

    /* --- Dataframe table --- */
    .stDataFrame {
        border-radius: 8px !important;
        overflow: hidden !important;
        border: 1px solid #e2e8f0 !important;
    }

    /* --- LaTeX centering --- */
    .stLatex {
        text-align: center !important;
        padding: 0.25rem 0 !important;
    }

    /* --- Sidebar --- */
    [data-testid="stSidebar"] {
        background-color: #f1f5f9;
    }
    [data-testid="stSidebar"] .block-container {
        padding-top: 2rem !important;
    }

    /* --- Slider labels --- */
    [data-testid="stSidebar"] .stSlider label {
        font-size: 0.85rem !important;
        color: #334155 !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Title row + language switch ----------
col_title, col_lang = st.columns([6, 1])
with col_title:
    st.title(t("app.title"))
    st.caption(t("app.caption"))
with col_lang:
    # Button shows the language you can switch TO
    if st.session_state["language"] == "en":
        btn_label = "🌐 中文"
    else:
        btn_label = "🌐 English"

    if st.button(btn_label, key="lang_switch"):
        new_lang = "zh-CN" if st.session_state["language"] == "en" else "en"
        st.session_state["language"] = new_lang
        st.rerun()

# ---------- Introduction ----------
st.markdown(t("intro"))
st.divider()

# ---------- Educational schematic ----------
st.subheader(t("schematic.title"))

# Build a simple diagram using Plotly shapes + annotations
fig_model = go.Figure()

# --- Fixed wall (left side) ---
fig_model.add_shape(type="rect", x0=0.3, y0=1.5, x1=1.0, y1=3.5,
    fillcolor="dimgray", line=dict(width=0))
# Hatch lines on the wall to suggest "fixed" support
for i in range(3):
    hx = 0.45 + i * 0.2
    fig_model.add_shape(type="line", x0=hx, y0=1.5, x1=hx, y1=3.5,
        line=dict(color="lightgray", width=1.5))

# --- Beam (horizontal bar) ---
fig_model.add_shape(type="rect", x0=1.0, y0=2.3, x1=7.5, y1=2.7,
    fillcolor="royalblue", opacity=0.7, line=dict(width=0))

# --- Downward force arrow at the free end ---
fig_model.add_annotation(
    x=7.5, y=0.5,
    ax=7.5, ay=2.3,
    xref="x", yref="y", axref="x", ayref="y",
    showarrow=True, arrowhead=3, arrowsize=1.5, arrowwidth=3,
    arrowcolor="crimson", text="",
)

# --- Labels (translated) ---
fig_model.add_annotation(x=0.65, y=3.9, text=t("schematic.fixed_end"),
    showarrow=False, font=dict(size=12, color="dimgray"))
fig_model.add_annotation(x=7.5, y=3.9, text=t("schematic.free_end"),
    showarrow=False, font=dict(size=12, color="dimgray"))
fig_model.add_annotation(x=8.0, y=1.4, text=t("schematic.force_label"),
    showarrow=False, font=dict(size=12, color="crimson"))
fig_model.add_annotation(x=4.25, y=1.7, text=t("schematic.length_label"),
    showarrow=False, font=dict(size=11, color="gray"))

# --- Dimension line under the beam ---
fig_model.add_shape(type="line", x0=1.0, y0=1.9, x1=7.5, y1=1.9,
    line=dict(color="gray", width=1, dash="dot"))
fig_model.add_shape(type="line", x0=1.0, y0=1.85, x1=1.0, y1=1.95,
    line=dict(color="gray", width=1))
fig_model.add_shape(type="line", x0=7.5, y0=1.85, x1=7.5, y1=1.95,
    line=dict(color="gray", width=1))

# --- Layout ---
fig_model.update_xaxes(visible=False, range=[0, 9.5])
fig_model.update_yaxes(visible=False, range=[0, 5])
fig_model.update_layout(
    plot_bgcolor="white",
    margin=dict(l=20, r=20, t=30, b=20),
    height=220,
)

# Constrain schematic width for a cleaner look
_, col_diagram, _ = st.columns([1, 4, 1])
with col_diagram:
    st.plotly_chart(fig_model, use_container_width=True)

st.markdown(t("schematic.caption"))
st.divider()

# ---------- Sidebar: input controls ----------
with st.sidebar:
    st.header(t("sidebar.title"))

    st.number_input(
        t("sidebar.slider_L"),
        step=1,
        key="param_L",
    )

    st.number_input(
        t("sidebar.slider_w"),
        step=1,
        key="param_w",
    )

    st.number_input(
        t("sidebar.slider_t"),
        step=1,
        key="param_t",
    )

    st.number_input(
        t("sidebar.slider_E"),
        step=1,
        key="param_E",
    )

    st.number_input(
        t("sidebar.slider_F"),
        step=0.10,
        format="%.2f",
        key="param_F",
    )

# Read current values from session state
L = st.session_state["param_L"]
w = st.session_state["param_w"]
t_val = st.session_state["param_t"]
E = st.session_state["param_E"]
F = st.session_state["param_F"]

# ---------- Manual range validation ----------
# Browser-native HTML5 validation messages are in the browser's locale
# (e.g. French). We check ranges manually so we can show translated errors.
errors = []

if L < 50 or L > 1000:
    errors.append(t("validation.range_L"))
if w < 5 or w > 200:
    errors.append(t("validation.range_w"))
if t_val < 1 or t_val > 50:
    errors.append(t("validation.range_t"))
if E < 1 or E > 250:
    errors.append(t("validation.range_E"))
if F < 0.10 or F > 100.00:
    errors.append(t("validation.range_F"))

if errors:
    for msg in errors:
        st.error(msg)
    st.stop()

# ---------- Unit conversions ----------
# The formula uses SI units (meters, Pascals, Newtons).
# Our sliders use μm, GPa, μN — so we convert here.

L_m = L * 1e-6          # μm → m
w_m = w * 1e-6          # μm → m
t_m = t_val * 1e-6       # μm → m
E_Pa = E * 1e9          # GPa → Pa
F_N = F * 1e-6          # μN → N

# ---------- Deflection calculation ----------
# Moment of inertia for a rectangular cross-section:
#   I = w * t^3 / 12
I_m4 = (w_m * t_m**3) / 12

# I in μm⁴ for display (computed from slider values in μm)
I_um4 = (w * t_val**3) / 12

# Cantilever beam tip deflection:
#   delta = F * L^3 / (3 * E * I)
delta_m = (F_N * L_m**3) / (3 * E_Pa * I_m4)

# Convert result from meters to micrometers for display
delta_um = delta_m * 1e6    # m → μm

# ---------- Results: 2x2 metric cards ----------
st.subheader(t("results.title"))

col_a, col_b = st.columns(2)

with col_a:
    st.metric(label=t("results.applied_force"), value=f"{F} μN")
    st.metric(label=t("results.beam_length"), value=f"{L} μm")

with col_b:
    st.metric(
        label=t("results.tip_deflection"),
        value=f"{delta_um:.3f} μm",
    )
    st.metric(
        label=t("results.moment_of_inertia"),
        value=f"{I_m4:.3e} m⁴",
    )
    st.caption(f"≈ {I_um4:.1f} μm⁴")

# ---------- SI units note ----------
st.caption(t("si_note"))
st.divider()

# ---------- Formula explanation ----------
st.subheader(t("formula.title"))

# LaTeX formulas are language-independent (math notation)
st.latex(r"\delta = \frac{F L^3}{3 E I}")
st.latex(r"I = \frac{w t^3}{12}")

# Build the symbol table from translation keys
# Using a list of dicts (no pandas needed) with column_config for translated headers
symbol_data = [
    {"s": "δ", "m": t("formula.symbol_delta"), "u": "μm"},
    {"s": "F", "m": t("formula.symbol_F"),     "u": "μN"},
    {"s": "L", "m": t("formula.symbol_L"),     "u": "μm"},
    {"s": "w", "m": t("formula.symbol_w"),     "u": "μm"},
    {"s": "t", "m": t("formula.symbol_t"),     "u": "μm"},
    {"s": "E", "m": t("formula.symbol_E"),     "u": "GPa"},
    {"s": "I", "m": t("formula.symbol_I"),     "u": "μm⁴"},
]

st.dataframe(
    symbol_data,
    hide_index=True,
    use_container_width=True,
    column_config={
        "s": t("formula.symbol_header"),
        "m": t("formula.meaning_header"),
        "u": t("formula.unit_header"),
    },
)

# ---------- Model assumptions ----------
st.subheader(t("assumptions.title"))

st.markdown(f"""
- {t("assumptions.rectangular")}
- {t("assumptions.small_deformation")}
- {t("assumptions.linear_elastic")}
""")

# ---------- Interactive chart ----------
st.subheader(t("chart.title"))

# Generate a range of force values (μN → N → calculate δ → μm)
F_range_uN = np.linspace(0.1, 100.0, 200)
F_range_N = F_range_uN * 1e-6

# Reuse I_m4 from the single-point calculation above (beam geometry is constant)
delta_range_m = (F_range_N * L_m**3) / (3 * E_Pa * I_m4)
delta_range_um = delta_range_m * 1e6

# Build the Plotly line chart
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=F_range_uN,
    y=delta_range_um,
    mode="lines",
    line=dict(color="royalblue", width=2),
    name="δ vs F",
))

fig.update_layout(
    xaxis_title=t("chart.x_axis"),
    yaxis_title=t("chart.y_axis"),
    margin=dict(l=40, r=20, t=40, b=40),
    height=400,
    showlegend=False,
)

st.plotly_chart(fig, use_container_width=True)
st.caption(t("chart.caption"))

# ---------- Limitations ----------
st.subheader(t("limitations.title"))

st.markdown(f"""
- {t("limitations.no_nonlinear")}
- {t("limitations.no_damping")}
- {t("limitations.no_dynamic")}
""")

st.info(t("fem_disclaimer"))
