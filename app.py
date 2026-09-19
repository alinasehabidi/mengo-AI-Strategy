import streamlit as st
import time

# Page Configuration
st.set_page_config(
    page_title="MENGO | Founder Simulation Game",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Custom Gamified CSS & Animations
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=JetBrains+Mono:wght@500;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Plus Jakarta Sans', sans-serif;
        background-color: #0b0f12;
        color: #f3f4f6;
    }

    /* Floating retro-glow badges */
    .game-hud {
        background: rgba(20, 27, 34, 0.95);
        border: 1px solid #334155;
        border-radius: 14px;
        padding: 0.75rem 1.25rem;
        display: flex;
        justify-content: space-around;
        align-items: center;
        margin-bottom: 1.5rem;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.4);
    }

    .hud-metric {
        font-family: 'JetBrains Mono', monospace;
        font-weight: 700;
        font-size: 1.1rem;
    }

    .level-badge {
        font-family: 'JetBrains Mono', monospace;
        font-size: 0.75rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #a3e635;
        background: rgba(163, 230, 53, 0.12);
        padding: 0.25rem 0.6rem;
        border-radius: 6px;
        border: 1px solid rgba(163, 230, 53, 0.3);
    }

    .slide-card {
        background: #141b22;
        border: 1px solid #232f3e;
        border-radius: 18px;
        padding: 2rem;
        margin-top: 1rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
    }

    .choice-card {
        background: #0f172a;
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1.2rem;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
    }
    .choice-card:hover {
        border-color: #38bdf8;
        transform: translateY(-2px);
    }

    .action-btn {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 700;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Game State Initialization
if "stage" not in st.session_state:
    st.session_state.stage = 1
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "chaos" not in st.session_state:
    st.session_state.chaos = 50
if "outputs_unlocked" not in st.session_state:
    st.session_state.outputs_unlocked = 0
if "governance_deck" not in st.session_state:
    st.session_state.governance_deck = [
        {"title": "Generic 5-paragraph blog with zero voice", "expected": "Reject", "reason": "Low quality, unaligned with positioning."},
        {"title": "Sharp LinkedIn hook with clear customer proof", "expected": "Approve", "reason": "Matches brand tone and clear value prop."},
        {"title": "Email variant with great angle but wrong product claim", "expected": "Regenerate", "reason": "Tone is good, but needs factual prompt adjustment."}
    ]
if "gov_index" not in st.session_state:
    st.session_state.gov_index = 0

# --- Top HUD Display ---
c_hud1, c_hud2, c_hud3, c_hud4 = st.columns([2, 1, 1, 1])

with c_hud1:
    st.markdown(f'<span class="level-badge">MISSION {st.session_state.stage} OF 5</span>', unsafe_allow_html=True)
    stages_titles = {
        1: "The Founder's Dilemma (Quality vs Quantity)",
        2: "The Chaos Reducer (Structure Setup)",
        3: "The Full Ecosystem Loop",
        4: "The 100x Multiplier Cannon",
        5: "The Governance Boss Gate"
    }
    st.markdown(f"### {stages_titles[st.session_state.stage]}")

with c_hud2:
    st.metric("Strategy XP", f"{st.session_state.xp} pts")

with c_hud3:
    chaos_color = "🟢" if st.session_state.chaos < 30 else ("🟡" if st.session_state.chaos <= 60 else "🔴")
    st.metric("Team Chaos", f"{st.session_state.chaos}% {chaos_color}")

with c_hud4:
    st.metric("Multiplied Assets", f"{st.session_state.outputs_unlocked}")

st.progress(st.session_state.stage / 5)

# --- LEVEL 1: FOUNDER'S DILEMMA ---
if st.session_state.stage == 1:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("""
    #### ⚠️ An incoming crisis at your startup:
    Your team is drowning under two classic bottlenecks:
    - **Problem 1 (Quality Gap):** AI creates content, but it ignores your voice and vision. You spend all day rewriting[cite: 1].
    - **Problem 2 (Quantity Deficit):** You need 50 assets across 5 channels, but only have the capacity to make 5[cite: 1].
    
    *How do you respond to the board?*
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🅰 Hire 10 more copywriters to fix volume manually", use_container_width=True):
            st.error("❌ Burned your budget! Output remains tethered directly to team size.")
            st.session_state.chaos += 20
    with col2:
        if st.button("🅱 Turn your existing team into an AI-leveraged growth squad", use_container_width=True):
            st.success("🎯 Correct! A smaller AI-enabled team can match the output of a legacy department.")
            st.session_state.xp += 100
            st.session_state.chaos -= 15
            time.sleep(0.8)
            st.session_state.stage = 2
            st.rerun()
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- LEVEL 2: INPUT CALIBRATION ---
elif st.session_state.stage == 2:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("""
    #### 🎯 The Real Problem: Random Input = Random Output
    AI multiplies output. But if the input is confused, it just **multiplies confusion**[cite: 1].
    
    **Objective:** Calibrate your brand's foundational parameters before hitting the generation button[cite: 1].
    """)
    
    c1, c2 = st.columns(2)
    with c1:
        b1 = st.checkbox("Define Business Positioning & Value Prop", value=False)
        b2 = st.checkbox("Set Explicit Target Audience Boundaries", value=False)
        b3 = st.checkbox("Lock Specific Tone of Voice & Rules", value=False)
        b4 = st.checkbox("Define Exact Content Objectives & Metrics", value=False)
    
    inputs_checked = sum([b1, b2, b3, b4])
    
    with c2:
        if inputs_checked == 0:
            st.warning("⚠️ Warning: Completely blind prompting. Output will be generic fluff.")
        elif inputs_checked < 4:
            st.info(f"⚙ Calibrating... {inputs_checked}/4 constraints applied.")
        else:
            st.success("💎 Maximum Clarity! Prompt boundaries locked. Ready to execute.")
            if st.button("Lock Strategy & Advance ➔", type="primary", use_container_width=True):
                st.session_state.xp += 150
                st.session_state.chaos = max(10, st.session_state.chaos - 25)
                st.session_state.stage = 3
                st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- LEVEL 3: THE END-TO-END SYSTEM ---
elif st.session_state.stage == 3:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("""
    #### 🔄 AI Is Not One Prompt — It's A Continuous Loop
    Connect each stage of your execution engine from Research to Optimization[cite: 1].
    """)
    
    tabs = st.tabs(["1. Research", "2. Create", "3. Campaign", "4. Convert", "5. Optimise"])
    
    with tabs[0]:
        st.write("**AI Scope:** Customer pain signals, competitor gaps, positioning benchmarks[cite: 1].")
    with tabs[1]:
        st.write("**AI Scope:** Landing pages, blogs, ad hooks, outbound scripts[cite: 1].")
    with tabs[2]:
        st.write("**AI Scope:** Omnichannel calendar, message variants, distribution mapping[cite: 1].")
    with tabs[3]:
        st.write("**AI Scope:** Lead capture personalization, nurturing emails, sales objection support[cite: 1].")
    with tabs[4]:
        st.write("**AI Scope:** Analytics synthesis, A/B performance auditing, continuous prompt tuning[cite: 1].")
        
    st.markdown("---")
    if st.button("Deploy Marketing System ➔", type="primary"):
        st.session_state.xp += 100
        st.session_state.stage = 4
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- LEVEL 4: THE 100X MULTIPLIER ---
elif st.session_state.stage == 4:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("""
    #### ⚡ The Output Multiplication Engine
    One core business objective can turn into **100 actionable outputs**[cite: 1].
    """)
    
    user_idea = st.text_input("Enter your primary seed campaign idea:", "High-ticket enterprise customer acquisition")
    
    if st.button("🔥 Fire Multiplier Engine", type="primary"):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)
            
        st.session_state.outputs_unlocked = 100
        st.session_state.xp += 200
        st.balloons()
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Short-Form & Ads", "35 assets", "+35")
        c2.metric("Nurture & Outbound", "25 touchpoints", "+25")
        c3.metric("Landing Pages & Funnels", "40 variations", "+40")
        
        st.success("🎉 Asset explosion complete without ballooning headcount!")
        
    if st.session_state.outputs_unlocked >= 100:
        if st.button("Proceed to Human Governance Gate ➔"):
            st.session_state.stage = 5
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# --- LEVEL 5: GOVERNANCE ARENA ---
elif st.session_state.stage == 5:
    st.markdown('<div class="slide-card">', unsafe_allow_html=True)
    st.markdown("""
    #### 🛡️ AI Generates. Humans Govern[cite: 1].
    **Rule:** More automation requires tighter human responsibility[cite: 1]. Make editorial decisions to protect brand equity:
    """)
    
    if st.session_state.gov_index < len(st.session_state.governance_deck):
        card = st.session_state.governance_deck[st.session_state.gov_index]
        
        st.markdown(f"""
        <div style="background:#0f172a; border-radius:12px; padding:1.5rem; border:2px dashed #475569; text-align:center;">
            <p style="color:#94a3b8; font-size:0.8rem; text-transform:uppercase;">Asset Review #{st.session_state.gov_index + 1}</p>
            <h3 style="color:#ffffff;">"{card['title']}"</h3>
        </div>
        """, unsafe_allow_html=True)
        
        b_col1, b_col2, b_col3 = st.columns(3)
        
        action = None
        with b_col1:
            if st.button("✅ Approve", use_container_width=True):
                action = "Approve"
        with b_col2:
            if st.button("🔄 Regenerate", use_container_width=True):
                action = "Regenerate"
        with b_col3:
            if st.button("❌ Reject", use_container_width=True):
                action = "Reject"
                
        if action:
            if action == card["expected"]:
                st.success(f"🎯 Correct Decision! {card['reason']}")
                st.session_state.xp += 50
            else:
                st.warning(f"⚠️ Suboptimal Call. Recommendation was {card['expected']}: {card['reason']}")
                st.session_state.chaos += 10
            
            time.sleep(1.2)
            st.session_state.gov_index += 1
            st.rerun()
            
    else:
        st.markdown("""
        <div style="text-align:center; padding: 2rem 1rem;">
            <h1 style="color:#a3e635; font-size:3rem; margin-bottom:0;">🏆 SIMULATION CONQUERED</h1>
            <h3 style="color:#cbd5e1; margin-top:0.5rem;">"What can we accomplish now that AI exists?"</h3>
            <p style="color:#94a3b8; max-width:600px; margin:auto;">
                You've turned AI from a random content generator into a disciplined, scalable growth engine across your entire organization.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.snow()
        
        if st.button("↺ Restart Simulation", use_container_width=True):
            st.session_state.stage = 1
            st.session_state.xp = 0
            st.session_state.chaos = 50
            st.session_state.outputs_unlocked = 0
            st.session_state.gov_index = 0
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
