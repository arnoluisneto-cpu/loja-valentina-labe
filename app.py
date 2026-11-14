import streamlit as str_app
from datetime import datetime

str_app.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="centered"
)

# ESTÉTICA DE ALTO LUXO ESTÁVEL (Fundo Escuro Puro, Verde Neon e Roxo Valentina)
str_app.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;900&display=swap');
    
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #0b0914 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Botões compactos elegantes */
    .stButton>button, div[data-testid="stFileUploader"] button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border-radius: 6px !important;
        border: none !important;
        padding: 6px 12px !important;
        font-size: 13px !important;
        width: 100% !important;
    }
    .stButton>button:hover, div[data-testid="stFileUploader"] button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
    }
    
    /* Banner do Topo */
    .hero-banner {
        background: linear-gradient(135deg, #161026 0%, #22153b 100%);
        border: 1.5px solid #8A2BE2;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0px 0px 15px rgba(138, 43, 226, 0.25);
    }
    .hero-title {
        font-size: 20px;
        font-weight: 900;
        letter-spacing: 2px;
        color: #00FF66 !important;
        margin: 0;
    }
    
    /* Campos e selects compactos */
    input, select, div[data-baseweb="select"] > div {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        border-radius: 6px !important;
        min-height: 32px !important;
        font-size: 13px !important;
    }
    
    /* Textarea com rolagem interna travada */
    textarea {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        border-radius: 6px !important;
        max-height: 180px !important;
        font-size: 12px !important;
        overflow-y: scroll !important;
    }
    
    .stTextInput input, .stSelectbox select { color: #ffffff !important; font-size: 13px !important; }
    div[data-baseweb="select"] span { color: #ffffff !important; font-size: 13px !important; }
    div[data-baseweb="select"] svg { fill: #00FF66 !important; }
    
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        font-size: 13px !important;
    }
    
    /* Uploaders compactos */
    div[data-testid="stFileUploader"] {
        background-color: #161026 !important;
        border: 1px solid #00FF66 !important;
        border-radius: 6px !important;
        padding: 4px !important;
    }
    div[data-testid="stFileUploader"] section { background-color: #161026 !important; padding: 4px !important; }
    div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] p {
        color: #ffffff !important;
        font-size: 11px !important;
    }
    
    ::placeholder { color: #b0bec5 !important; opacity: 1 !important; }
    
    .metric-card {
        background-color: #161026 !important;
        border: 1px solid #8A2BE2 !important;
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 8px;
    }
    
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #000000 !important;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: bold;
        font-size: 11px;
        display: inline-block;
        margin-bottom: 6px;
    }
    
    h1, h2, h3, label, .stMarkdown {
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 13px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 1. TOPO DA APLICAÇÃO
str_app.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">LABORATÓRIOS VALENTINA</h1>
        <p style="color: #b0bec5; font-size: 9px; margin-top: 2px; margin-bottom: 0; letter-spacing: 1.5px;">LOJA DA VALENTINA • AUTOMATIZAÇÃO DE LOJAS NO TIKTOK</p>
    </div>
""", unsafe_allow_html=True)

# Inicializar os 20 estilos com a estrutura completa
if "db_estilos" not in str_app.session_state:
    str_app.session_state.db_estilos = {}
    for i in range(1, 21):
        if i == 20:
            prompt_texto = (
                "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: 20. Caminhão Preto Gigante do TikTok Parado com Portas Abertas e Valentina. "
                "STRICT ASSERTIVE CATEGORY & ZERO MIC PROTOCOL: Focus exclusively on footwear display, showing shoes clearly on feet, highlighting heel height and comfort. Strictly binding uploaded model reference face/body and isolated exact reference pixels of the product with zero alterations, zero modifications to the product structure, details, or brand. "
                "Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone, completely bare clothing surface with zero attachments. "
                "Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock: identical reference model face and body proportions. "
                "Rigid product lock: exact product matching reference image with zero substitution, preserving original brand aesthetics. "
                "STATIC TRUCK & PERSISTENT BOX CHOREOGRAPHY (0-10s): From exact second 0, the camera is positioned behind the creator (Valentina) from a rear angle. The video opens instantly with Valentina speaking naturally with flawless lip-sync as she walks forward from inside her boutique toward the street. "
                "Directly in front of the store, a massive, giant black delivery truck with clean, bold 'TikTok' lettering written in bright white on its black body is ALREADY PARKED in reverse, completely stationary with its rear cargo doors ALREADY WIDE OPEN, revealing an interior completely packed and stacked wall-to-wall up to the ceiling with storage boxes. "
                "Valentina reaches the glass door, manually pushes it open with her hands, and walks straight up to the truck. She picks up a single storage box. "
                "STRICT PERSISTENCE RULE: Throughout the entire duration of the video, the storage box remains physically present and firmly held in her hands without ever disappearing, vanishing, or morphing. She opens the box steadily while holding it, lifts a matching pair directly out of the box while keeping the box visible in her grip, displays the footwear clearly to the camera, and concludes her sales pitch. "
                "IMMEDIATE FLAWLESS START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks, zero generated text captions. SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 10 seconds with zero abrupt audio cuts and zero dead silence. Fixed realistic background, organic human movement.\n\n"
                "\"Olha, gente... acabou de chegar o estoque aqui na Loja da Valentina. A gente vai trabalhar só com essa sandália, porque ela é recordista de vendas e de muita qualidade! Clica aqui no carrinho laranja embaixo para garantir a sua.\"\n\n"
                "Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, AI morphing transition, soft blending, product switching, changing product model at the end, sudden jump cuts, rapid unrealistic pacing, over 10s, rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, text captions, generated writing, UI graphics, watermarks, distorted brand, altered design, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI, walking backward, truck moving, doors opening, box disappearing, box vanishing, item morphing into hand."
            )
            titulo_texto = "Estilo 20: POV Caminhão Preto Gigante Parado com Portas Abertas e Valentina"
        else:
            prompt_texto = (
                f"Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: {i}. Standard Valentina Showcase. "
                f"STRICT ASSERTIVE CATEGORY & ZERO MIC PROTOCOL: Focus on clear product demonstration, showing details clearly. Strictly binding uploaded model reference face/body and isolated exact reference pixels of the product with zero alterations. "
                f"Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone. "
                f"Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. "
                f"Strict 1:1 pixel lock and rigid product match with zero substitution. "
                f"VIRAL HOOK & FLUID TRY-ON FLOW (0-10s): The video opens dynamically with the creator looking straight into the camera delivering a strong magnetic hook, pacing her speech evenly across the full 10 seconds while interacting directly with the item.\n\n"
                f"\"Olha, gente, meninas, olha aqui o que chegou agora na Loja da Valentina! Chegou todo esse estoque exclusivo. A gente vai trabalhar só com essa marca porque está vendendo muito. Clica no carrinho laranja aqui embaixo e garanta a sua, que esse estoque chegou agora e vai estar de promoção!\"\n\n"
                f"Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI."
            )
            titulo_texto = f"Estilo {i}: Padrão Loja da Valentina #{i}"
            
        str_app.session_state.db_estilos[i] = {
            "titulo": titulo_texto,
            "prompt": prompt_texto
        }

# 2. SEÇÃO 1: PAINEL DE CONTROLE (Com containers nativos seguros do Streamlit)
str_app.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:6px;'>⚡ PAINEL DE CONTROLE RÁPIDO</p>", unsafe_allow_html=True)

c_grid1, c_grid2, c_grid3 = str_app.columns(3)

with c_grid1:
    with str_app.container(border=True):
        str_app.markdown("🎬 **DIRETOR SKIN**")
        str_app.markdown("<span style='color: #b0bec5; font-size: 11px;'>BOY (Elite)</span>", unsafe_allow_html=True)

with c_grid2:
    with str_app.container(border=True):
        str_app.markdown("📱 **PROPORÇÃO**")
        str_app.markdown("<span style='color: #b0bec5; font-size: 11px;'>9:16 Vertical</span>", unsafe_allow_html=True)

with c_grid3:
    with str_app.container(border=True):
        str_app.markdown("⚡ **STATUS ENGINE**")
        str_app.markdown("<span style='color: #00FF66; font-size: 11px;'>Ativo & Sincronizado</span>", unsafe_allow_html=True)

# Selectboxes funcionais logo abaixo dos cards
col_s1, col_s2 = str_app.columns(2)
with col_s1:
    diretor_skin = str_app.selectbox("Skin", ["BOY (Elite Director)", "UGC LIFESTYLE"], label_visibility="collapsed")
with col_s2:
    proporcao = str_app.selectbox("Proporção", ["9:16 (TikTok / Reels)", "1:1 (Feed)"], label_visibility="collapsed")

# Seleção de estilos para a grade diária
lista_titulos_geral = [str_app.session_state.db_estilos[i]["titulo"] for i in str_app.session_state.db_estilos]
estilos_selecionados = str_app.multiselect(
    "🎬 SELECIONAR ESTILOS PARA GRADE DIÁRIA",
    options=lista_titulos_geral,
    default=[str_app.session_state.db_estilos[20]["titulo"]]
)

str_app.markdown("---")

# 3. SEÇÃO 2: EDITOR DE PROMPT COMPACTO
str_app.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:6px;'>✏️ EDITOR DE PROMPT</p>", unsafe_allow_html=True)

c_num, c_txt = str_app.columns([1, 3])
with c_num:
    slot_num_edit = str_app.selectbox("Nº", options=list(str_app.session_state.db_estilos.keys()))
with c_txt:
    str_app.markdown(f"<p style='margin-top: 22px; font-size: 11px; font-weight:600; color: #00FF66;'>{str_app.session_state.db_estilos[slot_num_edit]['titulo']}</p>", unsafe_allow_html=True)

prompt_ativo = str_app.session_state.db_estilos[slot_num_edit]["prompt"]
novo_prompt_digitado = str_app.text_area("Editar Código do Prompt", value=prompt_ativo, height=140, key=f"prompt_full_{slot_num_edit}")

if str_app.button("💾 Salvar Alteração do Estilo"):
    str_app.session_state.db_estilos[slot_num_edit]["prompt"] = novo_prompt_digitado
    str_app.success(f"Estilo #{slot_num_edit} salvo com sucesso!")

str_app.markdown("---")

# 4. SEÇÃO 3: ENTRADAS DO PRODUTO EM CARDS SEGUROS
str_app.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:6px;'>📦 DADOS DO PRODUTO & UPLOADS</p>", unsafe_allow_html=True)

col_input1, col_input2 = str_app.columns(2)

with col_input1:
    produto_nome = str_app.text_input("NOME PRODUTO / SKU", placeholder="Ex: Sandália Gigil...")
    tipo_produto = str_app.selectbox("CATEGORIA", ["Calçado / Tênis / Sandália", "Acessório", "Vestuário", "Bolsa", "Outros"])
    foto_produto_analise = str_app.file_uploader("Foto Produto", type=["jpg", "jpeg", "png"], key="prod_1")
    
with col_input2:
    foto_modelo = str_app.file_uploader("Foto Modelo (1:1)", type=["jpg", "jpeg", "png"], key="m_1")
    foto_peca = str_app.file_uploader("Foto Peça (Pixel Lock)", type=["jpg", "jpeg", "png"], key="p_1")

GRADE_HORARIOS = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"]

str_app.markdown("---")

# 5. BOTÃO DE GERAÇÃO FINAL
if str_app.button("🚀 GERAR PROMPTS DA GRADE DIÁRIA"):
    if not produto_nome:
        str_app.warning("⚠️ Informe o nome do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        str_app.warning("⚠️ Envie todas as fotos.")
    elif not estilos_selecionados:
        str_app.warning("⚠️ Selecione pelo menos 1 estilo.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        str_app.success(f"✅ Gerados {len(estilos_selecionados)} prompts às {agora} para '{produto_nome}'.")
        
        mapa_prompts = {str_app.session_state.db_estilos[i]["titulo"]: str_app.session_state.db_estilos[i]["prompt"] for i in str_app.session_state.db_estilos}
        
        for idx, estilo_titulo in enumerate(estilos_selecionados):
            prompt_numero = idx + 1
            horario_postagem = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
            prompt_ativo_slot = mapa_prompts.get(estilo_titulo, "Prompt não encontrado.")

            str_app.markdown(f"### 🎬 Prompt #{prompt_numero} • {horario_postagem}")
            str_app.markdown(
                '<div class="metric-card">'
                f'<span class="tag-estilo">{estilo_titulo}</span><br>',
                unsafe_allow_html=True
            )
            str_app.code(prompt_ativo_slot, language="text")
            str_app.markdown('</div>', unsafe_allow_html=True)
