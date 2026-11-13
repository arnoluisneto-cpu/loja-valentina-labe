import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# ESTÉTICA DE ALTO LUXO (Fundo Escuro Puro, Padrão Verde Neon)
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
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION (NATURAL & SMOOTH)</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES (20 Estilos Oficiais)
c_top1, c_top2, c_top3 = st.columns(3)
with c_top1:
    diretor_skin = st.selectbox("DIRETOR SKIN", ["BOY (Elite Director)", "UGC LIFESTYLE (Influencer & Conversão)"])
with c_top2:
    proporcao = st.selectbox("PROPORÇÃO", ["9:16 (TikTok / Reels)", "1:1 (Feed)", "16:9 (Wide)"])
with c_top3:
    estilo_persona = st.selectbox("ESTILO DE VÍDEO (CONTEXTO)", [
        "1. Caminhão e Van do TikTok Shop Chegando",
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
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Salto Bloco GIGIL")
    
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

# 4. BANCO DE ROTEIROS ÚNICOS (13.5 SEGUNDOS COM CTA COMPLETA E RESPIRO FINAL)
roteiros_unicos = [
    "Meninas, olha o que acabou de chegar... exatamente como eu pedi, estou totalmente apaixonada... corre lá na Loja da Valentina... e clica no carrinho laranja aqui embaixo.",
    "Gente, sério... recebi o produto exato da foto, precisava gravar com calma para vocês verem... está imperdível na Loja da Valentina... clica no carrinho laranja aí embaixo.",
    "Olha, veio idêntico ao cadastrado, acabamento impecável, perfeito para o dia a dia... já está disponível na Loja da Valentina... corre e clica no carrinho laranja.",
    "Vocês me pediram muito esse modelo exato, e ele chegou perfeito, superando expectativas... garante o seu na Loja da Valentina... clicando no carrinho laranja.",
    "Meninas, reposição oficial do produto que vocês tanto queriam, chegou fresquinho... corre para garantir o seu direto na Loja da Valentina... clica no carrinho laranja.",
    "Para tudo e presta atenção na fidelidade absoluta desse produto, simplesmente maravilhoso... tudo disponível na Loja da Valentina... clica no carrinho laranja."
]

# 5. GERADOR COM MOVIMENTO SUAVE, SUPERFÍCIE DE APOIO E FIM FLUIDO
if st.button("🚀 GERAR PACOTE COMERCIAL (NATURAL & SMOOTH)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome exato do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Por favor, faça o upload da FOTO DA MODELO, da FOTO DO PRODUTO e da foto na descrição para ativar a precisão máxima.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"✅ Pacote gerado às {agora} | Estilo Ativo: [{estilo_persona}] | Movimento Suave Ativo.")
        
        horarios = [
            "09:00 - Manhã (Abertura de Feed)",
            "12:00 - Almoço (Pico de Engajamento)",
            "15:00 - Tarde (Pausa Comercial)",
            "18:00 - Fim de Tarde (Deslocamento)",
            "19:00 - Noite (Pico Principal de Compra)",
            "23:00 - Fechamento (Último Tiro do Dia)"
        ]
        
        # PROMPT OTIMIZADO CONTRA MOVIMENTO BRUSCO E CORTE SECO
        for i, h in enumerate(horarios):
            roteiro_completo = roteiros_unicos[i % len(roteiros_unicos)]

            prompt_final = (
                f"Photorealistic 4K UGC video (13.5s duration, {proporcao.split()[0]}), mobile sensor. ACTIVE STYLE: {estilo_persona}. "
                f"Strict 1:1 pixel lock: identical reference model face and body proportions. "
                f"Rigid product lock: exact '{produto_nome}' matching reference image with zero substitution. "
                f"NATURAL KINEMATICS & SMOOTH START: The product begins resting naturally on a soft luxury bed surface. The model's hands enter the frame slowly and smoothly, picking up the box with realistic physical weight and gentle inertia (zero abrupt pop-up). "
                f"SMOOTH TAIL BUFFER: The action and speech gently slow down towards the final seconds, allowing a natural, unhurried conclusion with zero abrupt audio cuts. "
                f"Fixed static background, organic human movement.\n\n"
                f"LOCUÇÃO (Com pausas naturais para respiro): \"{roteiro_completo}\"\n\n"
                f"Negative Prompt: abrupt appearance, pop-up object, fast jerky movement, harsh audio cut, model swapping, face morphing, background shift, CGI."
            )

            st.markdown(f"### 🕒 Bloco de Postagem: {h}")
            
            st.markdown(
                '<div class="metric-card">'
                '<span class="tag-estilo">Take Único (13.5s) - Suave & Natural</span><br>',
                unsafe_allow_html=True
            )
            
            st.code(prompt_final, language="text")
                
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
