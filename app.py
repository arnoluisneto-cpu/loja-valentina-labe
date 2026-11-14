import streamlit as str_app
from datetime import datetime

str_app.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="centered"
)

# ESTÉTICA DE ALTO LUXO COM BOTÕES CENTRALIZADOS E RESET INFALÍVEL
str_app.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
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
    
    /* Banner do Topo: Título Gigante, Pesado, com Sombra Forte e Subtítulo Menor */
    .hero-banner {
        background: linear-gradient(135deg, #130d22 0%, #20133f 100%);
        border: 2.5px solid #00FF66;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0px 0px 30px rgba(0, 255, 102, 0.45);
    }
    .hero-title {
        font-size: 34px !important;
        font-weight: 900 !important;
        letter-spacing: 4px;
        color: #ffffff !important;
        text-shadow: 0 0 18px rgba(0, 255, 102, 0.9), 0 0 35px rgba(138, 43, 226, 0.7);
        margin: 0 !important;
        line-height: 1.2;
    }
    .hero-subtitle {
        color: #00FF66 !important;
        font-size: 9px !important;
        font-weight: 700 !important;
        margin-top: 8px !important;
        margin-bottom: 0 !important;
        letter-spacing: 2px;
        text-transform: uppercase;
        opacity: 0.9;
    }
    
    /* Campos gerais e selects */
    input, select, div[data-baseweb="select"] > div {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        border-radius: 6px !important;
        min-height: 32px !important;
        font-size: 13px !important;
    }
    
    /* CORREÇÃO DO DROPDOWN DO DIRETOR SKIN */
    div[data-testid="stSelectbox"] {
        width: 100% !important;
    }
    div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
        padding-right: 15px !important;
    }
    div[data-testid="stSelectbox"] span {
        white-space: nowrap !important;
        overflow: visible !important;
        text-overflow: clip !important;
    }

    /* CORREÇÃO DO MENU DE ESTILOS (Rolagem garantida para mostrar até o Estilo 20) */
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
        font-size: 13px !important;
        max-height: 300px !important;
        overflow-y: auto !important;
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
    
    /* ELIMINAÇÃO TOTAL DOS AVISOS DE TAMANHO (200MB / FORMATOS) */
    div[data-testid="stFileUploader"] small,
    div[data-testid="stFileUploader"] span:nth-of-type(2),
    div[data-testid="stFileUploader"] div:has(> small),
    section[aria-label="File uploader"] small {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    
    div[data-testid="stFileUploader"] {
        background-color: #161026 !important;
        border: 1px solid #00FF66 !important;
        border-radius: 6px !important;
        padding: 6px !important;
        margin-bottom: 2px !important;
    }
    div[data-testid="stFileUploader"] section { background-color: #161026 !important; padding: 4px !important; }
    div[data-testid="stFileUploader"] span {
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

# CONTROLE DE VERSÃO DE ESTADO PARA FORÇAR O RESET DOS INPUTS
if "form_version" not in str_app.session_state:
    str_app.session_state.form_version = 0

def acionar_limpeza():
    str_app.session_state.form_version += 1
    # Limpa explicitamente todas as chaves dinâmicas da sessão
    for k in ["input_nome_produto", "sel_categoria", "sel_skin", "sel_prop", "multi_estilos"]:
        if k in str_app.session_state:
            del str_app.session_state[k]

v = str_app.session_state.form_version

# 1. TOPO DA APLICAÇÃO (Banner Impactante)
str_app.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">LABORATÓRIOS VALENTINA</h1>
        <p class="hero-subtitle">LOJA DA VALENTINA • AUTOMATIZAÇÃO DE LOJAS NO TIKTOK</p>
    </div>
""", unsafe_allow_html=True)

str_app.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# Inicializar os 20 estilos universais completos (do 1 ao 20 garantidos)
if "db_estilos" not in str_app.session_state:
    str_app.session_state.db_estilos = {}
    
    identidades_estilos = {
        1: ("Estilo 1: POV Mão & Rasgando o Plástico de Proteção (ASMR)", "Foco tátil universal abrindo a embalagem e rasgando o plástico de proteção da peça com extrema nitidez e som imersivo."),
        2: ("Estilo 2: POV Corpo Inteiro Caminhando na Calçada Urbana", "Câmera em movimento fluido acompanhando o produto de corpo inteiro (head-to-toe) ao ar livre sob luz natural."),
        3: ("Estilo 3: POV Sentada no Provador de Luxo (Close Íntimo)", "Enquadramento elegante com a modelo sentada em provador sofisticado, detalhando o caimento e o tecido."),
        4: ("Estilo 4: POV Giro 360 Graus em Frente ao Espelho", "Rotação e giros fluidos em frente ao espelho iluminado da boutique, exibindo todos os ângulos da peça."),
        5: ("Estilo 5: POV Sem Fala com Trilha Viral & Transição Rápida", "Estilo puramente visual de altíssima retenção, sem diálogos, focado em cortes dinâmicos sincronizados com a batida da música."),
        6: ("Estilo 6: POV Close Macro com Foco nos Detalhes", "Câmera de perto apontada diretamente para o produto, destacando texturas, acabamentos e diferenciais."),
        7: ("Estilo 7: Look do Dia Executivo com Blazer (Estilo Virgínia)", "Estética corporativa de alto padrão transmitindo autoridade, poder e elegância profissional."),
        8: ("Estilo 8: Look Verão & Frescor na Praça Externa", "Cenário ensolarado e vibrante, mostrando leveza e praticidade para dias quentes."),
        9: ("Estilo 9: Estilo Clássico Imponente em Estúdio de Cinema", "Iluminação profissional de estúdio de cinema focada na imponência, postura e sofisticação máxima."),
        10: ("Estilo 10: Provador Expresso de Oferta Relâmpago", "Ritmo acelerado, troca dinâmica e foco em conversão imediata de estoque limitado e preço promocional."),
        11: ("Estilo 11: Acessório & Movimento Urbano", "Destaque dinâmico para a utilidade e acabamento do item em trânsito pela cidade."),
        12: ("Estilo 12: Conjunto Tricô Aconchegante (Macro Texturas)", "Foco em macro-texturas de tramas fechadas e toque suave para dias amenos."),
        13: ("Estilo 13: Look Noite & Balada com Luz Dramática", "Iluminação noturna sofisticada e moderna, destacando peças acetinadas e brilhantes sob reflexos de neon."),
        14: ("Estilo 14: Estilo Chunky Platform & Atitude Streetwear", "Foco em design robusto, estilo urbano moderno e atitude jovem para o público do TikTok."),
        15: ("Estilo 15: Peça Delicate (Close de Festa & Elegância)", "Detalhes delicados e acabamento refinado para eventos sociais e ocasiões especiais."),
        16: ("Estilo 16: Colete Alfaiataria & Camadas Elegantes", "Estilo moderno de sobreposições, demonstrando sofisticação para compor looks versáteis."),
        17: ("Estilo 17: Short Saia / Envelope em Movimento Fluido", "Fluidez, leveza e segurança com passos ritmados e naturais."),
        18: ("Estilo 18: Pantalona Jeans Premium (Cós Alto & Elegância)", "Caimento impecável e resistência de alfaiataria em plano aberto."),
        19: ("Estilo 19: Slip On Prático (Calce Fácil Ágil)", "Demonstração rápida de agilidade, ideal para o público que busca praticidade sem perder a elegância."),
        20: ("Estilo 20: POV Caminhão Preto Gigante do TikTok (Estoque Chegando)", "Cenário épico externo com caminhão gigante estacionado e portas abertas repletas de caixas da Loja da Valentina.")
    }

    for i in range(1, 21):
        titulo_texto, desc_estilo = identidades_estilos[i]
        
        if i == 20:
            prompt_texto = (
                "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: 20. Caminhão Preto Gigante do TikTok Parado com Portas Abertas e Valentina. "
                "STRICT ASSERTIVE CATEGORY & ZERO MIC PROTOCOL: Focus exclusively on product display, showing items clearly on model, highlighting quality and comfort. Strictly binding uploaded model reference face/body and isolated exact reference pixels of the product with zero alterations, zero modifications to the product structure, details, or brand. "
                "Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone, completely bare clothing surface with zero attachments. "
                "Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock: identical reference model face and body proportions. "
                "Rigid product lock: exact product matching reference image with zero substitution, preserving original brand aesthetics. "
                "STATIC TRUCK & PERSISTENT BOX CHOREOGRAPHY (0-10s): From exact second 0, the camera is positioned behind the creator (Valentina) from a rear angle. The video opens instantly with Valentina speaking naturally with flawless lip-sync as she walks forward from inside her boutique toward the street. "
                "Directly in front of the store, a massive, giant black delivery truck with clean, bold 'TikTok' lettering written in bright white on its black body is ALREADY PARKED in reverse, completely stationary with its rear cargo doors ALREADY WIDE OPEN, revealing an interior completely packed and stacked wall-to-wall up to the ceiling with storage boxes. "
                "Valentina reaches the glass door, manually pushes it open with her hands, and walks straight up to the truck. She picks up a single storage box. "
                "STRICT PERSISTENCE RULE: Throughout the entire duration of the video, the storage box remains physically present and firmly held in her hands without ever disappearing, vanishing, or morphing. She opens the box steadily while holding it, lifts a matching item directly out of the box while keeping the box visible in her grip, displays the product clearly to the camera, and concludes her sales pitch. "
                "IMMEDIATE FLAWLESS START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks, zero generated text captions. SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 10 seconds with zero abrupt audio cuts and zero dead silence. Fixed realistic background, organic human movement.\n\n"
                "\"Olha, gente... acabou de chegar o estoque aqui na Loja da Valentina. A gente vai trabalhar só com esse produto, porque ele é recordista de vendas e de muita qualidade! Clica aqui no carrinho laranja embaixo para garantir o seu.\"\n\n"
                "Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, AI morphing transition, soft blending, product switching, changing product model at the end, sudden jump cuts, rapid unrealistic pacing, over 10s, rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, text captions, generated writing, UI graphics, watermarks, distorted brand, altered design, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI, walking backward, truck moving, doors opening, box disappearing, box vanishing, item morphing into hand."
            )
        else:
            prompt_texto = (
                f"Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: {i}. {titulo_texto} - {desc_estilo}. "
                f"STRICT ASSERTIVE CATEGORY & ZERO MIC PROTOCOL: Focus on clear product demonstration, showing details clearly. Strictly binding uploaded model reference face/body and isolated exact reference pixels of the product with zero alterations. "
                f"Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone. "
                f"Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. "
                f"Strict 1:1 pixel lock and rigid product match with zero substitution. "
                f"VIRAL HOOK & FLUID TRY-ON FLOW (0-10s): The video opens dynamically with the creator looking straight into the camera delivering a strong magnetic hook, pacing her speech evenly across the full 10 seconds while interacting directly with the item.\n\n"
                f"\"Olha, gente, meninas, olha aqui o que chegou agora na Loja da Valentina! Chegou todo esse estoque exclusivo. A gente vai trabalhar só com essa marca porque está vendendo muito. Clica no carrinho laranja aqui embaixo e garanta a sua, que esse estoque chegou agora e vai estar de promoção!\"\n\n"
                f"Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI."
            )
            
        str_app.session_state.db_estilos[i] = {
            "titulo": titulo_texto,
            "prompt": prompt_texto
        }

# 2. SEÇÃO 1: PAINEL DE CONTROLE RÁPIDO
str_app.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>⚡ PAINEL DE CONTROLE RÁPIDO</p>", unsafe_allow_html=True)

c_grid1, c_grid2, c_grid3 = str_app.columns(3)

with c_grid1:
    with str_app.container(border=True):
        str_app.markdown("🎬 **DIRETOR SKIN**")
        diretor_skin = str_app.selectbox("Skin", ["BOY (Elite Director)", "UGC LIFESTYLE"], label_visibility="collapsed", key=f"sel_skin_{v}")

with c_grid2:
    with str_app.container(border=True):
        str_app.markdown("📱 **PROPORÇÃO**")
        proporcao = str_app.selectbox("Proporção", ["9:16 (TikTok / Reels)", "1:1 (Feed)"], label_visibility="collapsed", key=f"sel_prop_{v}")

with c_grid3:
    with str_app.container(border=True):
        str_app.markdown("⚡ **STATUS ENGINE**")
        str_app.markdown("<span style='color: #00FF66; font-size: 11px; font-weight:700;'>Ativo & Sincronizado</span>", unsafe_allow_html=True)

with str_app.container(border=True):
    str_app.markdown("🎬 **SELECIONAR ESTILOS PARA GRADE DIÁRIA**")
    lista_titulos_geral = [str_app.session_state.db_estilos[i]["titulo"] for i in str_app.session_state.db_estilos]
    estilos_selecionados = str_app.multiselect(
        "Selecione",
        options=lista_titulos_geral,
        default=[str_app.session_state.db_estilos[20]["titulo"]],
        label_visibility="collapsed",
        key=f"multi_estilos_{v}"
    )

str_app.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# 3. SEÇÃO 2: EDITOR DE PROMPT (Caixinha limpa e alinhada ao botão Salvar)
str_app.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>✏️ EDITOR DE PROMPT</p>", unsafe_allow_html=True)

with str_app.container(border=True):
    col_esq, col_dir = str_app.columns([1, 2])

    with col_esq:
        str_app.markdown("🔢 **ESTILO**")
        
        # Container com largura idêntica ao botão de salvar
        str_app.markdown('<div style="max-width: 200px;">', unsafe_allow_html=True)
        slot_num_edit = str_app.selectbox("Estilo", options=list(str_app.session_state.db_estilos.keys()), label_visibility="collapsed", key=f"sel_estilo_edit_{v}")
        str_app.markdown('</div>', unsafe_allow_html=True)
        
        str_app.markdown("<div style='height: 10px;'></div>", unsafe_allow_html=True)
        
        if str_app.button("💾 Salvar Alteração"):
            current_val = str_app.session_state.get(f"prompt_full_{slot_num_edit}", str_app.session_state.db_estilos[slot_num_edit]["prompt"])
            str_app.session_state.db_estilos[slot_num_edit]["prompt"] = current_val
            str_app.success(f"Estilo #{slot_num_edit} salvo!")

    with col_dir:
        str_app.markdown("📝 **CÓDIGO DO PROMPT**")
        prompt_ativo = str_app.session_state.db_estilos[slot_num_edit]["prompt"]
        novo_prompt_digitado = str_app.text_area("Editar Código do Prompt", value=prompt_ativo, height=140, key=f"prompt_full_{slot_num_edit}", label_visibility="collapsed")

str_app.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# 4. SEÇÃO 3: DADOS DO PRODUTO & UPLOADS
str_app.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>📦 DADOS DO PRODUTO & UPLOADS</p>", unsafe_allow_html=True)

with str_app.container(border=True):
    c_l1_1, c_l1_2 = str_app.columns(2)
    with c_l1_1:
        str_app.markdown("🏷️ **NOME PRODUTO / SKU**")
        produto_nome = str_app.text_input("Nome", placeholder="Ex: Sandália Gigil...", label_visibility="collapsed", key=f"input_nome_produto_{v}")
    with c_l1_2:
        str_app.markdown("📂 **CATEGORIA**")
        tipo_produto = str_app.selectbox("Categoria", ["Calçado / Tênis / Sandália", "Acessório", "Vestuário", "Bolsa", "Outros"], label_visibility="collapsed", key=f"sel_categoria_{v}")

    str_app.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)

    c_f1, c_f2, c_f3 = str_app.columns(3)
    
    with c_f1:
        str_app.markdown("👩 **FOTO MODELO**")
        foto_modelo = str_app.file_uploader("Foto Modelo", type=["jpg", "jpeg", "png"], key=f"m_1_{v}", label_visibility="collapsed")
        
    with c_f2:
        str_app.markdown("📷 **FOTO PRODUTO**")
        foto_produto_analise = str_app.file_uploader("Foto Produto", type=["jpg", "jpeg", "png"], key=f"prod_1_{v}", label_visibility="collapsed")
        
    with c_f3:
        str_app.markdown("🔍 **FOTO ZOOM**")
        foto_peca = str_app.file_uploader("Foto Zoom", type=["jpg", "jpeg", "png"], key=f"p_1_{v}", label_visibility="collapsed")

str_app.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)

# 5. BOTÕES CENTRALIZADOS EXATAMENTE NO MEIO (Lado a lado, colados com espaçamento milimétrico)
col_esq_vazio, col_btn1, col_btn2, col_dir_vazio = str_app.columns([1, 2, 2, 1])

with col_btn1:
    gerar_clicado = str_app.button("🚀 GERAR PROMPTS")

with col_btn2:
    str_app.button("🔄 LIMPAR TUDO", on_click=acionar_limpeza)

GRADE_HORARIOS = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"]

if gerar_clicado:
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
