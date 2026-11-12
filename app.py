import streamlit as st

st.set_page_config(
    page_title="Loja da Valentina - TikTok Shop Viral Lab",
    page_icon="🛍️",
    layout="wide"
)

# --- ESTILIZAÇÃO NEON PRO COM MÁXIMA LEGIDIBILIDADE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&display=swap');

    /* Fundo Principal do App */
    .stApp {
        background: radial-gradient(circle at top, #1a103c 0%, #0c091d 60%, #06040c 100%) !important;
        color: #ffffff !important;
    }

    /* Banner Superior VALENTINA */
    .valentina-banner {
        background: linear-gradient(180deg, rgba(35, 18, 77, 0.95) 0%, rgba(14, 10, 32, 0.98) 100%);
        border: 2px solid #a855f7;
        box-shadow: 0 0 25px rgba(168, 85, 247, 0.5), inset 0 0 15px rgba(56, 189, 248, 0.2);
        border-radius: 14px;
        padding: 25px 15px;
        text-align: center;
        margin-bottom: 20px;
    }
    .valentina-title {
        font-family: 'Montserrat', sans-serif !important;
        font-size: 3.8rem !important;
        font-weight: 900 !important;
        letter-spacing: 4px;
        color: #ffffff !important;
        text-shadow: 
            0 0 10px #c084fc,
            0 0 20px #a855f7,
            0 0 40px #7e22ce,
            0 0 60px #38bdf8;
        margin: 0;
        line-height: 1.1;
    }
    .valentina-subtitle {
        font-family: 'Montserrat', sans-serif !important;
        color: #f1f5f9 !important;
        font-size: 13px !important;
        font-weight: 700 !important;
        letter-spacing: 1.5px;
        margin-top: 10px;
        text-transform: uppercase;
    }

    /* Rótulos (Labels) dos inputs bem claros e visíveis */
    .stTextInput label, .stTextArea label, .stSelectbox label, .stFileUploader label {
        color: #f8fafc !important;
        font-weight: 600 !important;
        font-size: 14px !important;
    }

    /* Inputs, Textareas e Selectboxes com fundo mais claro e texto 100% branco */
    .stTextInput input, .stTextArea textarea, .stSelectbox [data-baseweb="select"] {
        background-color: #17122e !important;
        color: #ffffff !important;
        border: 1.5px solid #a855f7 !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
        font-size: 14px !important;
        box-shadow: 0 0 10px rgba(168, 85, 247, 0.3);
    }

    /* Deixar o texto digitado e o placeholder (exemplo) bem claros e legíveis */
    .stTextInput input::placeholder, .stTextArea textarea::placeholder {
        color: #94a3b8 !important;
        opacity: 1 !important;
    }

    /* Caixa de Uploader */
    [data-testid="stFileUploader"] {
        background-color: #17122e !important;
        border: 1.5px dashed #a855f7 !important;
        border-radius: 8px !important;
        padding: 10px !important;
        color: #ffffff !important;
    }
    [data-testid="stFileUploader"] section {
        background-color: #1f173d !important;
        border-radius: 6px !important;
    }
    [data-testid="stFileUploader"] span, [data-testid="stFileUploader"] small {
        color: #cbd5e1 !important;
    }

    /* Foco nos Campos (Verde Neon) */
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #4ade80 !important;
        box-shadow: 0 0 16px rgba(74, 222, 128, 0.6) !important;
    }

    /* Botão Principal Estilo Neon */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #7c3aed 0%, #2563eb 50%, #10b981 100%) !important;
        color: #ffffff !important;
        border: 1.5px solid #4ade80 !important;
        border-radius: 8px !important;
        font-weight: 800 !important;
        padding: 0.7rem 1.5rem !important;
        font-size: 16px !important;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        box-shadow: 0 0 20px rgba(124, 58, 237, 0.5);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0 0 30px rgba(74, 222, 128, 0.8);
        transform: scale(1.01);
    }

    /* Sidebar Escura */
    [data-testid="stSidebar"] {
        background-color: #0b0817 !important;
        border-right: 1px solid #3b0764;
    }
    [data-testid="stSidebar"] label, [data-testid="stSidebar"] span, [data-testid="stSidebar"] h2 {
        color: #f8fafc !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- BANNER TOPO ---
st.markdown("""
    <div class="valentina-banner">
        <h1 class="valentina-title">VALENTINA</h1>
        <p class="valentina-subtitle">LOJA DA VALENTINA • TIKTOK SHOP VIRAL LAB • PARÂMETROS DE VÍDEO</p>
    </div>
""", unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.header("⚡ Diretor Skin: BOY")
    skin_perfil = st.selectbox("Estilo de Vídeo", ["Pietra (Tendência & Lifestyle)", "Virgínia Routine (Vlog Dinâmico)", "POV Luxury ASMR"])
    formato_video = st.selectbox("Proporção", ["9:16 (TikTok / Reels)"])
    st.markdown("---")
    st.success("✅ Regras Ativas:\n- Falas 100% PT-BR\n- Loja da Valentina\n- CTA Carrinho Laranja")

# --- LINHA 1: 2 BLOCOS DE REFERÊNCIA / PRODUTO ---
col_top1, col_top2 = st.columns(2)
with col_top1:
    produto_nome = st.text_input("Produto / Peça Principal", placeholder="Ex: Sandália Preta Salto Bloco...")
    foto_modelo = st.file_uploader("Foto de Referência da Modelo", type=["png", "jpg", "jpeg"])
with col_top2:
    link_ref = st.text_input("Link ou Código de Referência", placeholder="Ex: REF-092 ou Link do produto...")
    foto_produto = st.file_uploader("Foto da Peça de Roupa / Calçado", type=["png", "jpg", "jpeg"])

# --- LINHA 2: 3 QUADRADINHOS COMPACTOS ---
col_mid1, col_mid2, col_mid3 = st.columns(3)
with col_mid1:
    cor_detalhe = st.text_input("Cor e Material", placeholder="Ex: Preto Fosco / Couro...")
with col_mid2:
    estilo_musical = st.text_input("Vibe / Estilo Musical", placeholder="Ex: Batida viral animada...")
with col_mid3:
    voz_narrador = st.selectbox("Voz / Tom da Fala", ["Feminina Empolgada (Jovem)", "Natural / Conversa de Amiga", "Luxo / Sofisticada"])

# --- LINHA 3: DESCRIÇÃO COMPACTA ---
desc_adicional = st.text_area("Detalhes Extras ou Benefícios do Produto", placeholder="Ex: Não machuca o pé, super confortável para usar o dia todo, combina com tudo...", height=80)

st.markdown("<br>", unsafe_allow_html=True)

# --- BOTÃO GERAR ---
if st.button("🚀 Gerar Roteiro e Prompts (Flow 9:16)"):
    prod = produto_nome if produto_nome else "essa novidade incrível"
    detalhe = desc_adicional if desc_adicional else "tem um acabamento impecável e super confortável"
    
    st.markdown("---")
    st.subheader("🎬 Prompts Prontos para o Flow (Takes de 10s a 12s)")
    
    prompt_take1 = f"""Vertical 9:16 photorealistic UGC video, natural daylight, trendy Brazilian female influencer holding the smartphone in selfie mode, showing {prod} ({cor_detalhe}). Natural hand gestures, authentic facial expressions, high detail skin texture, 4k. Spoken dialogue in português Brasil: "Gente, vocês precisam ver {prod} que acabou de chegar aqui na Loja da Valentina! Olha os detalhes disso aqui." """
    
    prompt_take2 = f"""Vertical 9:16 photorealistic UGC video, dynamic camera movement transitioning smoothly to full body shot showing how {prod} fits perfectly. Authentic influencer energy, natural indoor aesthetic lighting, crisp focus. Spoken dialogue in português Brasil: "Além de lindo, {detalhe}. Sério, não dá vontade de tirar mais! Já clica no carrinho laranja aqui embaixo na Loja da Valentina para garantir o seu antes que acabe!" """

    st.markdown("**Take 1 (Gancho + Apresentação - 10s):**")
    st.code(prompt_take1, language="text")
    
    st.markdown("**Take 2 (Prova + CTA Loja da Valentina e Carrinho Laranja - 12s):**")
    st.code(prompt_take2, language="text")
