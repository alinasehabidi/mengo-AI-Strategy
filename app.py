import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="MENGO | AI Strategy & Growth",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Design & Interactive CSS
st.markdown(
    """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0b0f12;
        color: #f3f4f6;
    }

    /* Gradient animations */
    @keyframes slideInUp {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulseGlow {
        0%, 100% { box-shadow: 0 0 15px rgba(45, 212, 191, 0.2); }
        50% { box-shadow: 0 0 30px rgba(45, 212, 191, 0.45); }
    }

    .slide-container {
        animation: slideInUp 0.45s cubic-bezier(0.16, 1, 0.3, 1);
        padding: 1.5rem 1rem 3rem 1rem;
        max-width: 1050px;
        margin: auto;
    }

    .eyebrow {
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #a3e635;
        margin-bottom: 0.5rem;
    }

    .main-title {
        font-size: 2.8rem;
        font-weight: 800;
        line-height: 1.15;
        margin-bottom: 1.5rem;
        color: #ffffff;
    }

    .glass-card {
        background: #141b22;
        border: 1px solid #232f3e;
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1rem;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }
    .glass-card:hover {
        transform: translateY(-3px);
        border-color: #38bdf8;
    }

    .highlight-card {
        border-left: 4px solid #a3e635;
        background: #131d1d;
    }

    .pill {
        display: inline-block;
        padding: 0.35rem 0.85rem;
        border-radius: 9999px;
        font-size: 0.8rem;
        font-weight: 600;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
    }
    .pill-green { background: rgba(34, 197, 94, 0.15); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); }
    .pill-yellow { background: rgba(234, 179, 8, 0.15); color: #facc15; border: 1px solid rgba(234, 179, 8, 0.3); }
    .pill-red { background: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }

    .interactive-box {
        background: #10161d;
        border-radius: 14px;
        padding: 1.2rem;
        border: 1px dashed #334155;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Navigation Definitions
SLIDES = [
    "1. The Founder's Challenge",
    "2. The Real Problem",
    "3. Structure Before Generation",
    "4. Marketing With AI Ecosystem",
    "5. Output Multiplication Engine",
    "6. Governance: Human-in-the-Loop",
    "7. The Leadership Opportunity",
]

if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0

# Top Presentation Controls
col_nav1, col_nav2, col_nav3 = st.columns([2, 5, 2])
with col_nav1:
    if st.button("⬅ Previous", use_container_width=True) and st.session_state.slide_idx > 0:
        st.session_state.slide_idx -= 1
        st.rerun()

with col_nav2:
    selected = st.selectbox(
        "Jump to section",
        range(len(SLIDES)),
        format_func=lambda i: SLIDES[i],
        index=st.session_state.slide_idx,
        label_visibility="collapsed",
    )
    if selected != st.session_state.slide_idx:
        st.session_state.slide_idx = selected
        st.rerun()

with col_nav3:
    if st.button("Next ➡", use_container_width=True) and st.session_state.slide_idx < len(SLIDES) - 1:
        st.session_state.slide_idx += 1
        st.rerun()

st.progress((st.session_state.slide_idx + 1) / len(SLIDES))
current_slide = st.session_state.slide_idx

# ----------------- SLIDE 1 -----------------
if current_slide == 0:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">The Founder\'s Challenge</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Two Bottlenecks Holding Back Growth</div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        st.markdown(
            """
        <div class="glass-card">
            <span class="pill pill-red">PROBLEM 01</span>
            <h3 style="color:#ffffff; margin-top:0.5rem;">Quality Gap</h3>
            <p style="color:#94a3b8;">The content generated does not match what you need. You prompt AI, it creates, but it completely misses your voice, brand, and vision.</p>
            <hr style="border-color:#22303c;">
            <p style="color:#cbd5e1; font-size:0.9rem;"><strong>Result:</strong> Founders end up rewriting, editing, and fixing everything generated manually.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            """
        <div class="glass-card">
            <span class="pill pill-yellow">PROBLEM 02</span>
            <h3 style="color:#ffffff; margin-top:0.5rem;">Quantity Deficit</h3>
            <p style="color:#94a3b8;">You cannot create fast enough. You need 50 pieces of multi-channel content, but your team only has the bandwidth to write 5.</p>
            <hr style="border-color:#22303c;">
            <p style="color:#cbd5e1; font-size:0.9rem;"><strong>Result:</strong> Volume severely exceeds capacity. Campaigns stall across channels.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div class="glass-card highlight-card">
        <h4 style="margin:0; color:#a3e635;">The Core Shift</h4>
        <p style="margin:0.4rem 0 0 0; color:#f1f5f9;">A small AI-enabled team can match or exceed the total output that previously required an entire enterprise department.</p>
    </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ----------------- SLIDE 2 -----------------
elif current_slide == 1:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">The Root Cause</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Random AI Usage Creates Random Output</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <div class="glass-card">
        <p style="font-size:1.15rem; color:#cbd5e1; line-height:1.6;">
            AI can multiply output. But <strong>if the input is confused, it multiplies confusion</strong>.<br>
            When teams skip foundational thinking, marketing turns entirely reactive instead of strategic.
        </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("### Interactive Diagnostic: Test Your Input Clarity")
    diag_col1, diag_col2 = st.columns([1, 1])

    with diag_col1:
        has_pos = st.checkbox("Defined Business Positioning", value=True)
        has_aud = st.checkbox("Clear Target Audience Persona", value=False)
        has_tone = st.checkbox("Documented Tone of Voice & Style Guide", value=False)
        has_obj = st.checkbox("Measurable Campaign Objective", value=True)

    score = sum([has_pos, has_aud, has_tone, has_obj])

    with diag_col2:
        if score <= 1:
            st.markdown(
                """
            <div class="interactive-box" style="border-color:#ef4444;">
                <span class="pill pill-red">High Risk</span>
                <h4 style="color:#f87171;">Random Gen Loop</h4>
                <p style="color:#94a3b8; font-size:0.9rem;">Output will feel generic, misaligned, and will require total rewrites by senior staff.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        elif score <= 3:
            st.markdown(
                """
            <div class="interactive-box" style="border-color:#eab308;">
                <span class="pill pill-yellow">Moderate Alignment</span>
                <h4 style="color:#facc15;">Functional but Inconsistent</h4>
                <p style="color:#94a3b8; font-size:0.9rem;">Output is useful for drafts, but campaigns will lack brand cohesion across multi-channel distribution.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                """
            <div class="interactive-box" style="border-color:#22c55e;">
                <span class="pill pill-green">High Leverage</span>
                <h4 style="color:#4ade80;">Multiplication Ready</h4>
                <p style="color:#94a3b8; font-size:0.9rem;">Clean inputs yield aligned assets at high velocity with near-zero editorial rework.</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- SLIDE 3 -----------------
elif current_slide == 2:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">Framework</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Structure Before Generation</div>', unsafe_allow_html=True)

    st.write("The leadership mandate: Give AI context, boundaries, and clear constraints before execution.")

    cols = st.columns(3)
    pillars = [
        ("01. Identity", ["Business Positioning", "Target Audience", "Industry Profile"]),
        ("02. Strategy", ["Growth Goals", "Offer Clarity", "Value Proposition"]),
        ("03. Execution", ["Tone of Voice", "Content Objective", "Distribution Guardrails"]),
    ]

    for col, (title, items) in zip(cols, pillars):
        with col:
            st.markdown(
                f"""
            <div class="glass-card">
                <h4 style="color:#38bdf8; margin-top:0;">{title}</h4>
                <ul style="color:#94a3b8; padding-left:1.2rem; font-size:0.95rem; line-height:1.7;">
                    {"".join(f"<li>{item}</li>" for item in items)}
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
    <div style="text-align: center; margin-top:1.5rem; font-size:1.15rem; font-weight:700; color:#a3e635;">
        Clear Strategic Input &nbsp; ➔ &nbsp; Aligned Scalable Output
    </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ----------------- SLIDE 4 -----------------
elif current_slide == 3:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">End-to-End Workflow</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">One Continuous Execution Loop</div>', unsafe_allow_html=True)

    stage = st.select_slider(
        "Walk through the workflow stages:",
        options=["Research", "Create", "Campaign", "Convert", "Optimise"],
        value="Create",
    )

    stage_data = {
        "Research": {
            "focus": "Customer signals, competitor gaps, positioning hooks",
            "deliverable": "Synthesized insights, market intelligence summaries, and buyer pain-point matrices.",
        },
        "Create": {
            "focus": "Landing pages, long-form blogs, ad creatives, outbound emails, and scripts",
            "deliverable": "Channel-native copy and visual assets produced with locked brand parameters.",
        },
        "Campaign": {
            "focus": "Editorial calendars, theme matrices, audience variants, and channel orchestration",
            "deliverable": "A coherent 30-day multi-channel roadmap with scheduled variant distribution.",
        },
        "Convert": {
            "focus": "High-intent lead capture, nurturing drips, objection handling, and sales assets",
            "deliverable": "Personalized dynamic lead responses, proposal decks, and case-study alignment.",
        },
        "Optimise": {
            "focus": "Funnel metrics analysis, A/B variant testing, continuous iteration",
            "deliverable": "Weekly performance feedback loops tuning subsequent content generation runs.",
        },
    }

    st.markdown(
        f"""
    <div class="glass-card" style="border-color:#38bdf8; margin-top:1rem;">
        <span class="pill pill-green">Stage: {stage}</span>
        <h3 style="color:#ffffff; margin-top:0.75rem;">Core Focus: {stage_data[stage]['focus']}</h3>
        <p style="color:#94a3b8; font-size:1rem; margin-bottom:0;"><strong>System Output:</strong> {stage_data[stage]['deliverable']}</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
    <p style="color:#64748b; font-size:0.85rem; margin-top:1rem; text-align:center;">
        Al is not one department or tool—it is an operational capability layer running across the entire customer lifecycle.
    </p>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ----------------- SLIDE 5 -----------------
elif current_slide == 4:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">Scale & Leverage</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">Output Multiplication Engine</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <p style="color:#cbd5e1; font-size:1.05rem;">
        AI shifts the economics of creation. One single campaign concept expands into 100 high-converting downstream deliverables.
    </p>
    """,
        unsafe_allow_html=True,
    )

    seed_idea = st.text_input(
        "Enter a core core campaign concept:",
        value="Launch an enterprise AI advisory retainership for mid-market CFOs",
    )

    if st.button("Generate Multiplication Preview ⚡", type="primary"):
        st.markdown("#### Dynamic Channel Multiplication Plan")
        c1, c2, c3 = st.columns(3)

        with c1:
            st.markdown(
                f"""
            <div class="interactive-box">
                <strong style="color:#38bdf8;">Short-Form & Social</strong>
                <ul style="color:#94a3b8; font-size:0.85rem; padding-left:1.1rem; margin-top:0.5rem;">
                    <li>10 Thought-leadership posts on CFO cost control</li>
                    <li>5 Video scripts addressing legacy vendor bloat</li>
                    <li>15 Tactical carousel outline cards</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with c2:
            st.markdown(
                f"""
            <div class="interactive-box">
                <strong style="color:#a3e635;">Funnels & Ads</strong>
                <ul style="color:#94a3b8; font-size:0.85rem; padding-left:1.1rem; margin-top:0.5rem;">
                    <li>4 Tailored landing page variant angles</li>
                    <li>20 Ad variations (Problem-Agitate-Solve)</li>
                    <li>Downloadable executive benchmarking checklist</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

        with c3:
            st.markdown(
                f"""
            <div class="interactive-box">
                <strong style="color:#f43f5e;">Outreach & Sales</strong>
                <ul style="color:#94a3b8; font-size:0.85rem; padding-left:1.1rem; margin-top:0.5rem;">
                    <li>6-Part nurturing email sequence</li>
                    <li>Personalized cold LinkedIn connection templates</li>
                    <li>Sales battlecard & objection FAQ document</li>
                </ul>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("</div>", unsafe_allow_html=True)

# ----------------- SLIDE 6 -----------------
elif current_slide == 5:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">Quality Control</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">AI Generates. Humans Govern.</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <p style="color:#cbd5e1; font-size:1.05rem;">
        More automation requires more deliberate editorial control. Machine output must pass human checkpoints to protect brand equity.
    </p>
    """,
        unsafe_allow_html=True,
    )

    g1, g2, g3 = st.columns(3)
    with g1:
        st.markdown(
            """
        <div class="glass-card" style="border-top: 4px solid #22c55e; text-align:center;">
            <h2 style="color:#22c55e; margin:0.2rem 0;">Approve</h2>
            <p style="color:#94a3b8; font-size:0.95rem;">High-fidelity output aligned with brand, accuracy, and tone moves forward to production.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with g2:
        st.markdown(
            """
        <div class="glass-card" style="border-top: 4px solid #eab308; text-align:center;">
            <h2 style="color:#eab308; margin:0.2rem 0;">Regenerate</h2>
            <p style="color:#94a3b8; font-size:0.95rem;">Good structure but off-tone. Provide tighter prompt feedback and generate alternative angles.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    with g3:
        st.markdown(
            """
        <div class="glass-card" style="border-top: 4px solid #ef4444; text-align:center;">
            <h2 style="color:#ef4444; margin:0.2rem 0;">Reject</h2>
            <p style="color:#94a3b8; font-size:0.95rem;">Hallucinated facts, off-brand messaging, or generic clichés are purged immediately.</p>
        </div>
        """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
    <div class="glass-card highlight-card" style="margin-top:1.5rem;">
        <h4 style="margin:0; color:#a3e635;">The Human Value Equation</h4>
        <p style="margin:0.4rem 0 0 0; color:#f1f5f9;">
            AI handles synthesis, variant expansion, and initial asset drafting. Leaders decide what is true, ethical, empathetic, and ready for customers.
        </p>
    </div>
    </div>
    """,
        unsafe_allow_html=True,
    )

# ----------------- SLIDE 7 -----------------
elif current_slide == 6:
    st.markdown('<div class="slide-container">', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">Conclusion</div>', unsafe_allow_html=True)
    st.markdown('<div class="main-title">The Leadership Opportunity</div>', unsafe_allow_html=True)

    st.markdown(
        """
    <div class="glass-card" style="text-align:center; padding: 3rem 2rem; border-color: #2dd4bf;">
        <p style="color:#94a3b8; font-size:1.1rem; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem;">
            Do not only ask:
        </p>
        <h2 style="color:#f87171; text-decoration: line-through; margin-top:0;">"Will AI replace me?"</h2>
        <div style="height: 1rem;"></div>
        <p style="color:#94a3b8; font-size:1.1rem; text-transform:uppercase; letter-spacing:0.1em; margin-bottom:0.5rem;">
            Ask instead:
        </p>
        <h1 style="color:#a3e635; font-size:2.4rem; margin-top:0;">"What can we accomplish now that AI exists?"</h1>
        <p style="color:#cbd5e1; font-size:1.1rem; margin-top:2rem; max-width:600px; margin-left:auto; margin-right:auto;">
            Now imagine what an entire, aligned organization can accomplish.
        </p>
    </div>
    </div>
    """,
        unsafe_allow_html=True,
    )