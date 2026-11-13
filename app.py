import streamlit as st
from datetime import datetime
import re

st.set_page_config(
    page_title="Valentina Labs - Enterprise Industrial Core",
    page_icon="💜",
    layout="wide"
)

# CSS CORPORATIVO GLOBAL / SUPREMO E LIMPO
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;900&display=swap');
    
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #030206 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stButton>button, div[data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #00FF66 0%, #00b347 100%) !important;
        color: #030206 !important;
        font-weight: 800 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 14px 20px !important;
        font-size: 16px !important;
        width: 100% !important;
        box-shadow: 0 0 20px rgba(0, 255, 102, 0.3);
        transition: all 0.25s ease-in-out;
    }
    .stButton>button:hover {
        box-shadow: 0 0 30px rgba(0, 255, 102, 0.6);
        transform: translateY(-1px);
    }
    
    .enterprise-banner {
        background: linear-gradient(135deg, #0b0517 0%, #170932 100%);
        border: 2px solid #8A2BE2;
        padding: 24px;
        border-radius: 14px;
        text-align: center;
        margin-bottom: 22px;
        box-shadow: 0 0 35px rgba(138, 43, 226, 0.35);
    }
    .enterprise-title {
        font-size: 34px;
        font-weight: 900;
        letter-spacing: 5px;
        color: #00FF66 !important;
        text-shadow: 0 0 15px rgba(0, 255, 102, 0.6);
        margin: 0;
    }
    
    input, select, textarea, div[data-baseweb="select"] > div {
        background-color: #080512 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
        border-radius: 8px !important;
    }
    
    div[data-baseweb="select"] svg { fill: #00FF66 !important; }
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
        background-color: #080512 !important;
        border: 1.5px solid #00FF66 !important;
    }

    div[data-testid="stFileUploader"] {
        background-color: #080512 !important;
        border: 1.5px solid #00FF66 !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    
    .metric-card {
        background-color: #080512 !important;
        border: 1.5px solid #8A2BE2 !important;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 18px;
        box-shadow: 0 6px 20px rgba(138, 43, 226, 0.2);
    }
    
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #030206 !important;
        padding: 5px 10px;
        border-radius: 6px;
        font-weight: 800;
        font-size: 12px;
        display: inline-block;
        margin-bottom: 10px;
        letter-spacing: 0.5px;
    }
    
    h1, h2, h3, label, .stMarkdown { color: #ffffff !important; }
    </style>
""", unsafe_allow_html=True)

def sanitizar_url(url: str) -> str:
    if not url:
        return "tiktok-shop-verified-item"
    clean = re.sub(r'https?://(www\.)?', '', url).strip('/')
    return clean[:50]

# 1. CABEÇALHO DO SISTEMA
st.markdown("""
    <div class="enterprise-banner">
        <h1 class="enterprise-title">VALENTINA LABS</h1>
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2.5px;">SUPREME INDUSTRIAL CORE • IPHONE 18 PRO OPTICS + CAPCUT OPTIMIZED</p>
    </div>
""", unsafe_allow_html=True)

# 2. PAINEL DE CONFIGURAÇÃO
c1, c2 = st.columns(2)
with c1:
    resolucao = st.selectbox("FORMATO DO VÍDEO", ["9:16 (Vertical TikTok / Reels / Shorts)", "1:1 (Feed Standard)", "16:9 (Cinematic)"])
with c2:
    estilo_fluxo = st.selectbox("ESTRATÉGIA DE RETENÇÃO", [
        "🔥 Padrão CapCut Pro (Cortes Secos + Legendas Magnéticas)",
        "⚡ Unboxing Tátil Orgânico (Foco em Mãos & Textura)",
        "📱 POV Imersivo Real (Câmera de Smartphone Nativa)"
    ])

st.markdown("---")

# 3. ENTRADAS DE DADOS DO PRODUTO
col_in1, col_in2 = st.columns(2)

with col_in1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Preta Salto Bloco Tira Fina")
    produto_link = st.text_input("LINK OFICIAL DO TIKTOK SHOP", placeholder="Ex: https://shop.tiktok.com/view/product/...")

with col_in2:
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>1. FOTO DA MODELO (FACE LOCK 1:1)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-top:10px; margin-bottom:4px;'>2. FOTO DO PRODUTO (PIXEL-PERFECT CLONE)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. BANCO DE GANCHOS E CTAS
hooks = [
    "Meninas, olha o que acabou de chegar exatamente igual ao link, eu tô chocada com a perfeição!",
    "Gente, sério, recebi o produto exato da foto e precisava gravar de perto pra vocês verem o acabamento.",
    "Olha isso aqui na minha mão, veio idêntico ao que tá cadastrado na loja, qualidade absurda.",
    "Vocês me pediram muito o link desse modelo exato e chegou reposição impecável.",
    "Para tudo e repara nos detalhes dessa peça que acabou de sair da caixa.",
    "Eu sou super exigente, mas quando chegou exatamente igual ao anúncio eu precisei mostrar."
]

ctas = [
    "Corre pra garantir o seu na Loja da Valentina, clica no carrinho laranja aqui embaixo.",
    "Tá com preço promocional na Loja da Valentina, clica no carrinho laranja aqui embaixo antes que acabe.",
    "Disponível agora com envio rápido na Loja da Valentina, é só clicar no carrinho laranja aqui embaixo.",
    "Não deixa passar porque esgota rápido, garante o seu na Loja da Valentina clicando no carrinho laranja.",
    "Aproveita a condição especial na Loja da Valentina, clica no carrinho laranja aqui embaixo.",
    "Tudo disponível na Loja da Valentina, clica no carrinho laranja aqui embaixo e garante o seu."
]

# 5. GERADOR SUPREMO OTIMIZADO COM ÓPTICA DO IPHONE 18 PRO
if st.button("⚡ GERAR LOTE INDUSTRIAL DE ALTA CONVERSÃO (6 SLOTS)"):
    if not produto_nome or not produto_link:
        st.warning("⚠️ Insira o nome do produto e o link oficial.")
    elif not foto_peca:
        st.warning("⚠️ Faça o upload da foto do produto para ativar a clonagem neural 1:1.")
    else:
        id_slug = sanitizar_url(produto_link)
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"⚡ Lote processado às {agora} | Referência: `{id_slug}` | Óptica iPhone 18 Pro & CapCut Ativos.")

        ciclos = [
            "09:00 — Abertura de Feed Matinal",
            "12:00 — Pico de Almoço (Alta Retenção)",
            "15:00 — Engajamento da Tarde",
            "18:00 — Tráfego Fim de Tarde",
            "19:00 — Pico Global de Vendas TikTok Shop",
            "23:00 — Fechamento Estratégico Noturno"
        ]

        # Matriz Neural Atualizada com Sensor e Lentes do iPhone 18 Pro Max
        core_matrix = (
            f"Hyper-realistic 8K resolution UGC video ({resolucao.split()[0]}), shot natively on iPhone 18 Pro Max advanced camera system with variable aperture sensor and professional mobile optics. "
            f"Natural window soft daylight, organic handheld micro-tremors, realistic human respiration physics, sub-surface skin scattering. "
            f"SINGLE CONTINUOUS INDOOR ENVIRONMENT: Zero scene cuts, zero door transitions, zero background morphing, absolute spatial continuity. "
            f"STRICT 1:1 NEURAL IDENTITY LOCK: Creator facial structure, skin tone, hair, and micro-features match the uploaded model reference photo precisely. "
            f"Product '{produto_nome}' (ref: {id_slug}) strictly and perfectly replicates the uploaded product image down to every minor stitch, exact color tone, material reflection, and geometry—zero item substitution, zero AI hallucinations."
        )

        for i, slot in enumerate(ciclos):
            h_hook = hooks[i % 6]
            h_cta = ctas[i % 6]

            quadros = [
                (
                    "SLOT 1: Unboxing Tátil de Bancada",
                    f"Medium close-up handheld cinematic smartphone tracking inside a minimalist luxury room. The human creator naturally opens a branded package on a clean table, lifting the exact '{produto_nome}' from the uploaded reference image into frame, rotating it smoothly with realistic finger friction. {core_matrix}",
                    f"{h_hook} Tô abrindo aqui na bancada pra vocês verem de perto a {produto_nome}. {h_cta}"
                ),
                (
                    "SLOT 2: Demonstração de Uso Orgânico",
                    f"Fluid handheld movement in a bright, modern interior space. The exact reference model naturally wears and showcases '{produto_nome}' matching the uploaded image, moving organically with authentic human weight distribution and realistic fabric physics. {core_matrix}",
                    f"{h_hook} Testando no uso real hoje a {produto_nome} e o caimento fica simplesmente impecável. {h_cta}"
                ),
                (
                    "SLOT 3: Close Macro Cirúrgico de Detalhes",
                    f"Macro close-up handheld framing focusing tightly on '{produto_nome}' held steady in the creator's hands under warm ambient light, revealing authentic surface grain, precise material finish, and exact color matching the reference photo. {core_matrix}",
                    f"{h_hook} Olha bem de perto a textura e o acabamento da {produto_nome} na minha mão. {h_cta}"
                ),
                (
                    "SLOT 4: Mirror Check Natural (Espelho)",
                    f"Authentic mirror reflection video in a high-end boutique dressing room. The creator holds her smartphone naturally, adjusting her posture slightly while showcasing '{produto_nome}' matching the uploaded product photo clearly in the reflection. {core_matrix}",
                    f"{h_hook} Não podia deixar de gravar esse close no espelho com a {produto_nome}. {h_cta}"
                )
            ]

            st.markdown(f"### 🕒 {slot}")
            col_esq, col_dir = st.columns(2)

            for idx, (titulo_take, prompt_tecnico, roteiro_fala) in enumerate(quadros):
                coluna_alvo = col_esq if idx % 2 == 0 else col_dir
                with coluna_alvo:
                    st.markdown(f"""
                    <div class="metric-card">
                        <span class="tag-estilo">{titulo_take}</span><br>
                        <b style="color: #00FF66; font-size: 13px;">Prompt Neural (Copiar para o Motor de Vídeo):</b>
                    """, unsafe_allow_html=True)
                    st.code(prompt_tecnico, language="text")
                    st.markdown("""<b style="color: #00FF66; font-size: 13px;">Roteiro Otimizado (Legendas & Cortes CapCut):</b>""", unsafe_allow_html=True)
                    st.code(roteiro_fala, language="text")
                    st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("---")
