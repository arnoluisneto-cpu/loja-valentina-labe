import streamlit as st
from datetime import datetime
import re

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# ESTÉTICA ORIGINAL TRAVADA E BLINDADA (Fundo Escuro Puro, Sem Faixas Brancas, Contraste Perfeito)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #0b0914 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .stButton>button, div[data-testid="stFileUploader"] button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 12px 20px !important;
        font-size: 16px !important;
        width: 100% !important;
    }
    .stButton>button:hover, div[data-testid="stFileUploader"] button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #161026 0%, #22153b 100%);
        border: 2px solid #8A2BE2;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 0px 25px rgba(138, 43, 226, 0.4);
    }
    .hero-title {
        font-size: 34px;
        font-weight: 900;
        letter-spacing: 4px;
        color: #00FF66 !important;
        text-shadow: 0 0 12px rgba(0, 255, 102, 0.5);
        margin: 0;
    }
    
    input, select, textarea, div[data-baseweb="select"] > div {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
        border-radius: 8px !important;
    }
    
    .stTextInput input, .stSelectbox select { color: #ffffff !important; }
    div[data-baseweb="select"] span { color: #ffffff !important; }
    div[data-baseweb="select"] svg { fill: #00FF66 !important; }
    
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
    }
    
    div[data-testid="stFileUploader"] {
        background-color: #161026 !important;
        border: 2px solid #00FF66 !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    div[data-testid="stFileUploader"] section { background-color: #161026 !important; }
    div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] p {
        color: #ffffff !important;
    }
    
    ::placeholder { color: #b0bec5 !important; opacity: 1 !important; }
    
    .metric-card {
        background-color: #161026 !important;
        border: 1.5px solid #8A2BE2 !important;
        padding: 18px;
        border-radius: 12px;
        margin-bottom: 15px;
        box-shadow: 0px 4px 15px rgba(138, 43, 226, 0.2);
        height: 100%;
    }
    
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #000000 !important;
        padding: 4px 10px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 13px;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    h1, h2, h3, label, .stMarkdown {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    </style>
""", unsafe_allow_html=True)

def sanitizar_url(url: str) -> str:
    if not url:
        return "verified-catalog-item"
    return re.sub(r'https?://(www\.)?', '', url).strip('/')[:50]

# 1. TOPO DA APLICAÇÃO
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VALENTINA LABS</h1>
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES ORIGINAIS
c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    diretor_skin = st.selectbox("DIRETOR SKIN", ["BOY (Elite Director)", "UGC LIFESTYLE (Influencer & Conversão)"])
with c_top2:
    proporcao = st.selectbox("PROPORÇÃO", ["9:16 (TikTok / Reels)", "1:1 (Feed)", "16:9 (Wide)"])
with c_top3:
    estilo_persona = st.selectbox("ESTILO DE VÍDEO", [
        "1. Caminhão e Van do TikTok Shop",
        "2. POV Acordando na Cama (Morning Routine)",
        "3. POV Arrumando o Closet / Selecionando Peças",
        "4. POV Imersivo (Olhando para Baixo nos Pés)",
        "5. Corpo Inteiro na Rua (Caminhando no Calçadão)",
        "6. Frente ao Espelho (Mirror Selfie)",
        "7. Giro Dinâmico 360° (Mostrando Caimento)",
        "8. Close Macro Cirúrgico (Detalhes e Textura)",
        "9. Unboxing Surpresa em Cima da Mesa",
        "10. Transição Rápida de Looks",
        "11. Vlog de Rotina Diária Estilo Lifestyle",
        "12. Review Sincero Boca a Boca",
        "13. Provador Rápido de Loja Física",
        "14. Trend do Sofá / Almofada",
        "15. POV Dirigindo o Carro",
        "16. POV Café da Manhã na Mesa Posta",
        "17. Challenge de Transição: Look Casual para Luxo",
        "18. Unboxing Rasgando Pacote do TikTok Shop",
        "19. POV Fitness / Rotação de Estilo Diário",
        "20. POV Encontro Noturno / Night Out Look Reveal"
    ])

st.markdown("---")

# 3. ENTRADAS DO PRODUTO
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Vermelha Salto Bloco")
    produto_link = st.text_input("LINK OU CÓDIGO DE REFERÊNCIA", placeholder="Ex: https://shop.tiktok.com/... ou REF-092")
    tipo_produto = st.selectbox("CATEGORIA", [
        "Calçado / Tênis / Sandália", 
        "Acessório de Pulso ou Rosto (Relógio / Óculos)", 
        "Vestuário / Vestido / Conjunto",
        "Bolsa / Acessório de Mão",
        "Utilidades & Outros"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>1. FOTO MODELO (FACE LOCK 1:1)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-top:10px; margin-bottom:4px;'>2. FOTO PRODUTO (PIXEL-PERFECT CLONE)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. BANCOS DE GANCHOS E CTAS FIXADAS (LOJA DA VALENTINA & CARRINHO LARANJA)
hooks_abertura = [
    "Meninas, olha o que acabou de chegar exatamente como eu pedi no link, estou apaixonada!",
    "Gente, sério, recebi o produto exato do link e da foto, precisava gravar para vocês verem.",
    "Olha, veio idêntico ao que está cadastrado na nossa loja através do link.",
    "Vocês me mandaram o link pedindo esse modelo exato, e ele chegou impecável.",
    "Meninas, reposição oficial do produto que vocês tanto pediram pelo link e foto.",
    "Para tudo e presta atenção na fidelidade absoluta desse produto que chegou para mim."
]

ctas_fechamento = [
    "Corre para garantir o seu na Loja da Valentina, clica no carrinho laranja aqui embaixo.",
    "Está com um preço promocional imperdível na Loja da Valentina, clica no carrinho laranja.",
    "Disponível agora com frete rápido na Loja da Valentina, clica no carrinho laranja aí na tela.",
    "Não perde tempo porque esgota rápido, clica no carrinho laranja na Loja da Valentina.",
    "Garante o seu direto na Loja da Valentina, clica no carrinho laranja aqui embaixo.",
    "Tudo disponível na Loja da Valentina, clica no carrinho laranja e aproveita a promoção."
]

# 5. GERADOR INDUSTRIAL OTIMIZADO
if st.button("🚀 GERAR PACOTE COMERCIAL (6 HORÁRIOS)"):
    if not produto_nome or not produto_link:
        st.warning("⚠️ Por favor, informe o nome do produto e o link oficial.")
    elif not foto_peca:
        st.warning("⚠️ Por favor, faça o upload da foto do produto para garantir a clonagem pixel-perfect.")
    else:
        contexto_url = sanitizar_url(produto_link)
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"✅ Pacote gerado com sucesso às {agora} | Referência travada: `{contexto_url}`")
        
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        strict_link_lock = (
            f"ABSOLUTE LINK & PRODUCT ENFORCEMENT: The item rendered MUST strictly match the exact specifications, color tone, and design from official URL '{produto_link}' and product name '{produto_nome}'. "
            f"Zero color alteration, zero item substitution. If the name or link specifies a color, that exact color must dominate the product without exception."
        )
        
        base_negative = "Negative Prompt: low quality, distorted hands, morphing, wrong product color, item substitution, generic substitute item, blurry background, bad anatomy, deformed fingers, text artifacts, watermark, low resolution."

        for i, h in enumerate(horarios):
            h_hook = hooks_abertura[i % len(hooks_abertura)]
            h_cta = ctas_fechamento[i % len(ctas_fechamento)]

            takes = [
                (
                    "ESTILO 1: Unboxing na Bancada",
                    f"Hyper-realistic 8K UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {strict_link_lock}. Medium close-up handheld cinematic tracking inside a luxury room. The human creator opens a package on a table, lifting '{produto_nome}' into frame. Spoken dialogue in Portuguese Brazil embedded: \"{h_hook} Tô abrindo aqui na bancada pra vocês verem de perto a {produto_nome}. {h_cta}\". Continuous indoor location, 1:1 facial identity lock. {base_negative}"
                ),
                (
                    "ESTILO 2: Movimento Interno Dinâmico",
                    f"Hyper-realistic 8K UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {strict_link_lock}. Fluid handheld movement in a bright modern space. The exact reference model wears and showcases '{produto_nome}' with natural fabric physics. Spoken dialogue in Portuguese Brazil embedded: \"{h_hook} Testando no uso real hoje a {produto_nome} e o caimento fica simplesmente impecável. {h_cta}\". Continuous indoor environment, strict identity match. {base_negative}"
                ),
                (
                    "ESTILO 3: Close Macro de Detalhes",
                    f"Hyper-realistic 8K UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {strict_link_lock}. Macro close-up framing focusing tightly on '{produto_nome}' held steady in hands under warm ambient light, revealing precise surface finish. Spoken dialogue in Portuguese Brazil embedded: \"{h_hook} Olha bem de perto a textura e o acabamento da {produto_nome} na minha mão. {h_cta}\". Zero artifacts, perfect fidelity. {base_negative}"
                ),
                (
                    "ESTILO 4: Review no Espelho",
                    f"Hyper-realistic 8K UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {strict_link_lock}. Authentic mirror reflection video in a boutique dressing room. Creator holds smartphone, showcasing '{produto_nome}' clearly in the reflection. Spoken dialogue in Portuguese Brazil embedded: \"{h_hook} Não podia deixar de gravar esse close no espelho com a {produto_nome}. {h_cta}\". Continuous spatial continuity. {base_negative}"
                )
            ]

            st.markdown(f"### 🕒 Bloco de Postagem: {h}")

            col1, col2 = st.columns(2)
            
            with col1:
                for idx_take in [0, 2]:
                    t_title, t_prompt = takes[idx_take]
                    st.markdown(f"""
                    <div class="metric-card">
                        <span class="tag-estilo">{t_title}</span><br>
                        <b style="color: #00FF66; font-size: 12px;">Prompt Completo (Link + Fala + Negativo):</b>
                    """, unsafe_allow_html=True)
                    st.code(t_prompt, language="text")
                    st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                for idx_take in [1, 3]:
                    t_title, t_prompt = takes[idx_take]
                    st.markdown(f"""
                    <div class="metric-card">
                        <span class="tag-estilo">{t_title}</span><br>
                        <b style="color: #00FF66; font-size: 12px;">Prompt Completo (Link + Fala + Negativo):</b>
                    """, unsafe_allow_html=True)
                    st.code(t_prompt, language="text")
                    st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("---")
