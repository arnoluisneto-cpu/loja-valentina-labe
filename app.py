import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# ESTÉTICA ORIGINAL CLÁSSICA TRAVADA E BLINDADA (Fundo Escuro, Padrão Verde Neon)
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

# 1. TOPO DA APLICAÇÃO
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">VALENTINA LABS</h1>
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES
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

# 3. ENTRADAS DO PRODUTO (3 UPLOADS EM VERDE NEON)
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Vermelha Salto Bloco")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>DESCRIÇÃO DO PRODUTO - UPLOAD FOTO</p>", unsafe_allow_html=True)
    foto_produto_analise = st.file_uploader("Upload Foto Produto", type=["jpg", "jpeg", "png"], key="prod_upload_original", label_visibility="collapsed")

    tipo_produto = st.selectbox("CATEGORIA", [
        "Calçado / Tênis / Sandália", 
        "Acessório de Pulso ou Rosto (Relógio / Óculos)", 
        "Vestuário / Vestido / Conjunto",
        "Bolsa / Acessório de Mão",
        "Utilidades & Outros"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>1. FOTO MODELO (FACE & CORPO INTEIRO 1:1)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-top:10px; margin-bottom:4px;'>2. FOTO REFERÊNCIA PEÇA (CLONAGEM 1:1)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. BANCO DE ROTEIROS ÚNICOS (FALA 1 E FALA 2)
roteiros_completos = [
    {
        "fala1": "Meninas... olha o que acabou de chegar... exatamente como eu pedi, estou totalmente apaixonada por cada detalhe...",
        "fala2": "e para garantir o seu com segurança, corre lá na Loja da Valentina e clica no carrinho laranja aqui embaixo na tela."
    },
    {
        "fala1": "Gente, sério... recebi o produto exato da foto... precisava gravar bem de calma para vocês verem a qualidade real...",
        "fala2": "está com um preço promocional imperdível na Loja da Valentina, então clica no carrinho laranja aí embaixo e aproveita."
    },
    {
        "fala1": "Olha... veio idêntico ao que está cadastrado... acabamento impecável, perfeito para o dia a dia e super confortável...",
        "fala2": "já está disponível com frete rápido direto na Loja da Valentina, corre e clica no carrinho laranja aí na tela."
    },
    {
        "fala1": "Vocês me pediram muito esse modelo exato... e ele chegou perfeito, superando todas as expectativas de acabamento...",
        "fala2": "não perde tempo porque esgota rápido, garante o seu na Loja da Valentina clicando no carrinho laranja."
    },
    {
        "fala1": "Meninas... reposição oficial do produto que vocês tanto queriam... chegou fresquinho para compor os melhores looks...",
        "fala2": "corre para garantir o seu direto na Loja da Valentina, clica no carrinho laranja aqui embaixo e confere."
    },
    {
        "fala1": "Para tudo... e presta atenção na fidelidade absoluta desse produto... simplesmente maravilhoso e impecável em tudo...",
        "fala2": "tudo disponível na Loja da Valentina, clica no carrinho laranja e aproveita a promoção especial de hoje."
    }
]

# 5. GERADOR INDUSTRIAL COM PENTE FINO (BLINDAGEM ENXUTA E DIRETA)
if st.button("🚀 GERAR PACOTE COMERCIAL LIMPO E BLINDADO (6 HORÁRIOS)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome exato do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Por favor, faça o upload da FOTO DA MODELO, da FOTO DO PRODUTO e da foto na descrição para ativar a precisão máxima.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"✅ Pacote gerado às {agora} | Comandos limpos, sem excessos e Travas 1:1 Ativas.")
        
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        # Trava enxuta e cirúrgica (zero comandos repetidos)
        clean_lock = (
            f"STRICT 1:1 INDUSTRIAL CLONE: "
            f"1. MODEL LOCK: Exact 1:1 match of reference model face, features, skin tone, and body. Zero model swapping. "
            f"2. PRODUCT LOCK: Exact 1:1 physical clone of '{produto_nome}' based on reference images. Zero scaling or alterations. "
            f"3. SCENARIO LOCK: Identical indoor luxury background, lighting, and base clothing. Zero environment shifting."
        )
        
        clean_negative = "Negative Prompt: model swapping, face mutation, outfit change, background shift, wrong product, scaling error, low quality, distortion, watermark."

        for i, h in enumerate(horarios):
            rot = roteiros_completos[i % len(roteiros_completos)]

            takes = [
                (
                    "ESTILO 1: Unboxing na Bancada",
                    f"Hyper-realistic 8K full-body UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {clean_lock}. Medium close-up handheld cinematic tracking. Creator opens package on table, lifting '{produto_nome}' into frame.\n\n\n\n"
                    f"FALA 1: \"{rot['fala1']}\"\n\n\n\n"
                    f"FALA 2: \"{rot['fala2']}\"\n\n\n\n"
                    f"Continuous indoor location. {clean_negative}"
                ),
                (
                    "ESTILO 2: Movimento Interno Dinâmico",
                    f"Hyper-realistic 8K UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {clean_lock}. Fluid handheld movement. Reference model wears and showcases '{produto_nome}' with natural fabric physics.\n\n\n\n"
                    f"FALA 1: \"{rot['fala1']}\"\n\n\n\n"
                    f"FALA 2: \"{rot['fala2']}\"\n\n\n\n"
                    f"Continuous indoor environment. {clean_negative}"
                ),
                (
                    "ESTILO 3: Close Macro de Detalhes",
                    f"Hyper-realistic 8K UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {clean_lock}. Macro close-up framing focusing tightly on '{produto_nome}' held in hands under warm ambient light.\n\n\n\n"
                    f"FALA 1: \"{rot['fala1']}\"\n\n\n\n"
                    f"FALA 2: \"{rot['fala2']}\"\n\n\n\n"
                    f"Zero artifacts, perfect fidelity. {clean_negative}"
                ),
                (
                    "ESTILO 4: Review no Espelho",
                    f"Hyper-realistic 8K UGC video ({proporcao.split()[0]}), shot on iPhone Pro Max. {clean_lock}. Authentic mirror reflection video in boutique dressing room. Creator showcases '{produto_nome}' clearly in reflection.\n\n\n\n"
                    f"FALA 1: \"{rot['fala1']}\"\n\n\n\n"
                    f"FALA 2: \"{rot['fala2']}\"\n\n\n\n"
                    f"Fixed spatial continuity. {clean_negative}"
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
                        <b style="color: #00FF66; font-size: 12px;">Prompt Limpo e Otimizado:</b>
                    """, unsafe_allow_html=True)
                    st.code(t_prompt, language="text")
                    st.markdown("</div>", unsafe_allow_html=True)

            with col2:
                for idx_take in [1, 3]:
                    t_title, t_prompt = takes[idx_take]
                    st.markdown(f"""
                    <div class="metric-card">
                        <span class="tag-estilo">{t_title}</span><br>
                        <b style="color: #00FF66; font-size: 12px;">Prompt Limpo e Otimizado:</b>
                    """, unsafe_allow_html=True)
                    st.code(t_prompt, language="text")
                    st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("---")
