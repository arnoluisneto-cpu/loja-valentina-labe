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
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION (LOCKED REFERENCE ENGINE)</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES
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

# 3. ENTRADAS DO PRODUTO (DESCRIÇÃO UNIVERSAL + TRAVAS FIXAS NAS FOTOS DE REFERÊNCIA)
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU (UNIVERSAL)", placeholder="Ex: Tênis Nike / Relógio / Vestido...")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>DESCRIÇÃO DO PRODUTO - UPLOAD FOTO (UNIVERSAL)</p>", unsafe_allow_html=True)
    foto_produto_analise = st.file_uploader("Upload Foto Produto", type=["jpg", "jpeg", "png"], key="prod_upload_original", label_visibility="collapsed")

    tipo_produto = st.selectbox("CATEGORIA", [
        "Calçado / Tênis / Sandália", 
        "Acessório de Pulso ou Rosto (Relógio / Óculos)", 
        "Vestuário / Vestido / Conjunto / Peça",
        "Bolsa / Acessório de Mão",
        "Utilidades & Outros"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>1. FOTO MODELO (FACE & CORPO 1:1 + TRAVA ABSOLUTA)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-top:10px; margin-bottom:4px;'>2. FOTO REFERÊNCIA PEÇA (ISOLADA + TRAVA RÍGIDA DE PIXEL)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

# 4. GERAÇÃO DINÂMICA DE ROTEIROS BASEADA NO PRODUTO INFORMADO
def get_roteiros_dinamicos(prod):
    return [
        f"Amiga, para tudo e olha esse(a) {prod} da Loja da Valentina! Qualidade nobre, acabamento perfeito no corpo. Olha que luxo! Clica no carrinho laranja aqui embaixo e já garante o(a) seu(sua) agora.",
        f"Gente, sério, precisava mostrar a qualidade absurda desse(a) {prod}... material impecável que surpreende. Já estou usando, olha esse detalhe! Corre na Loja da Valentina e clica no carrinho laranja.",
        f"Olha esse achado na Loja da Valentina! Esse(a) {prod} é perfeito(a), acabamento impecável. É um espetáculo de elegância! Clica no carrinho laranja aí embaixo e já garante o(a) seu(sua).",
        f"Meninas, vocês queriam {prod} de altíssima qualidade? Achei! Esse(a) aqui é único(a). Corre na Loja da Valentina, clica no carrinho laranja e aproveita o frete.",
        f"Olha a sofisticação desse(a) {prod} que acabou de chegar... padrão premium impecável. Modelagem e acabamento perfeito! Garante o(a) seu(sua) direto na Loja da Valentina clicando no carrinho laranja.",
        f"Para tudo e presta atenção na qualidade desse(a) {prod}... material maravilhoso e super confortável. Fica deslumbrante! Disponível na Loja da Valentina, clica no carrinho laranja.",
        f"Amiga, elegância e conforto total com esse(a) {prod} da Loja da Valentina. Qualidade de shopping por preço de fábrica! Olha os detalhes. Clica no carrinho laranja aqui embaixo.",
        f"Gente, eu testei e apaixonei... esse(a) {prod} tem uma qualidade surreal. É perfeito(a)! Disponível na Loja da Valentina, clica no carrinho laranja.",
        f"Olha esse design impecável... esse(a) {prod} veste tããão bem! Peça indispensável no closet. Corre lá na Loja da Valentina e clica no carrinho laranja aqui embaixo para garantir.",
        f"Meninas, qualidade de primeira linha que fala, né? Esse(a) {prod} é perfeito demais. Olha como valoriza o visual! Garante o(a) seu(sua) na Loja da Valentina, clica no carrinho laranja.",
        f"Amiga, sério, esse(a) {prod} superou todas as expectativas de acabamento. É um luxo só! Tudo na Loja da Valentina, clica no carrinho laranja e já pede o(a) seu(sua).",
        f"Olha a beleza e a elegância desse(a) {prod}... última tendência! É só elogios. Corre pra Loja da Valentina e clica no carrinho laranja para garantir agora.",
        f"Gente, achado perfeito para qualquer ocasião! Esse(a) {prod} tem uma qualidade surreal. Olha isso! Clica no carrinho laranja na Loja da Valentina e aproveite.",
        f"Meninas, reposição do(a) {prod} mais desejado(a)! Material nobre e acabamento impecável. Corre na Loja da Valentina e clica no carrinho laranja.",
        f"Olha a perfeição desse(a) {prod}... toque macio e chique. Garante na Loja da Valentina clicando no carrinho laranja aqui embaixo.",
        f"Amiga, quer estilo sem esforço? É esse(a) {prod} aqui. Qualidade impecável! Clica no carrinho laranja na Loja da Valentina e não fique sem o(a) seu(sua).",
        f"Gente, sério, esse(a) {prod} é de outro planeta de tão bom. Fica divino(a)! Corre lá na Loja da Valentina e clica no carrinho laranja para garantir.",
        f"Olha esse design, olha essa qualidade... {prod} perfeito(a)! É um arraso total. Disponível na Loja da Valentina, clica no carrinho laranja e aproveita.",
        f"Meninas, não fiquem sem o(a) seu(sua) {prod} da Loja da Valentina! Qualidade premium legítima. Olha como valoriza o look! Clica no carrinho laranja aqui embaixo.",
        f"Amiga, achado de milhões! Esse(a) {prod} tem um acabamento único. Garante o(a) seu(sua) na Loja da Valentina, clica no carrinho laranja.",
        f"Para fechar com chave de ouro, olha esse(a) {prod} maravilhoso(a). Qualidade impecável! Corre na Loja da Valentina e clica no carrinho laranja agora."
    ]

# 5. GERADOR COM TRAVAS FIXAS NAS REFERÊNCIAS VISUAIS E MOTOR UNIVERSAL
if st.button("🚀 GERAR PACOTE COMPLETO (21 PROMPTS • LOCKED REFERENCE & UNIVERSAL)"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome exato do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Por favor, faça o upload da FOTO DA MODELO, da FOTO DO PRODUTO e da foto na descrição para ativar a precisão máxima.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"✅ Pacote de 21 Prompts gerado às {agora} | Produto: '{produto_nome}' | Duração: 10s | Cinema 8K RAW & Travas Ativas.")
        
        roteiros_21 = get_roteiros_dinamicos(produto_nome)
        
        for idx in range(21):
            roteiro_atual = roteiros_21[idx % len(roteiros_21)]
            prompt_numero = idx + 1

            prompt_final = (
                f"Masterpiece 8K UHD viral TikTok Shop UGC video powered by Arri Alexa cinema color science (10-second precise duration, {proporcao.split()[0]}), RAW optical sensor. ACTIVE STYLE: {estilo_persona}. "
                f"STRICT LOCKED REFERENCE ENGINE & ZERO MIC PROTOCOL: Strictly binding uploaded model reference face/body and isolated product reference pixels of '{produto_nome}' with zero alterations. Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone, completely bare clothing surface with zero attachments. "
                f"Cinematic Visual Engineering: hyper-detailed micro-textures on material weave, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. "
                f"Strict 1:1 pixel lock: identical reference model face and body proportions. "
                f"Rigid product lock: exact '{produto_nome}' matching reference image with zero substitution. "
                f"VIRAL HOOK & FLUID TRY-ON FLOW (0-10s): The video opens dynamically with the creator looking straight into the camera holding '{produto_nome}' for the first 2 seconds delivering a strong magnetic hook, then seamlessly transitions at second 2 already WEARING OR SHOWING '{produto_nome}' on her body in a chic mirror/dressing room setting, pacing her speech evenly across the full 10 seconds while interacting with the product. "
                f"IMMEDIATE FLUID START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks. "
                f"SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 10 seconds with zero abrupt audio cuts and zero dead silence. "
                f"Fixed static background, organic human movement.\n\n"
                f"LOCUÇÃO RÍTMICA (10s com distribuição equilibrada de fala e conversão): \"{roteiro_atual}\"\n\n"
                f"Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, staying only holding the item without wearing it, no try-on, over 10s, rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, UI graphics, watermarks, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI."
            )

            st.markdown(f"### 🎬 Prompt Comercial #{prompt_numero} de 21")
            
            st.markdown(
                '<div class="metric-card">'
                f'<span class="tag-estilo">Take Único #{prompt_numero} (10s) - Produto: {produto_nome}</span><br>',
                unsafe_allow_html=True
            )
            
            st.code(prompt_final, language="text")
                
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
