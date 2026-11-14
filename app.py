import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# ESTÉTICA DE ALTO LUXO (Fundo Escuro Puro, Padrão Verde Neon e Roxo Valentina)
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
        padding: 10px 18px !important;
        font-size: 15px !important;
    }
    .stButton>button:hover, div[data-testid="stFileUploader"] button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #161026 0%, #22153b 100%);
        border: 2px solid #8A2BE2;
        padding: 18px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0px 0px 20px rgba(138, 43, 226, 0.3);
    }
    .hero-title {
        font-size: 30px;
        font-weight: 900;
        letter-spacing: 3px;
        color: #00FF66 !important;
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
        padding: 10px !important;
    }
    div[data-testid="stFileUploader"] section { background-color: #161026 !important; }
    div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] p {
        color: #ffffff !important;
    }
    
    ::placeholder { color: #b0bec5 !important; opacity: 1 !important; }
    
    .metric-card {
        background-color: #161026 !important;
        border: 1.5px solid #8A2BE2 !important;
        padding: 16px;
        border-radius: 10px;
        margin-bottom: 12px;
    }
    
    .tag-estilo {
        background-color: #00FF66 !important;
        color: #000000 !important;
        padding: 3px 8px;
        border-radius: 6px;
        font-weight: bold;
        font-size: 12px;
        display: inline-block;
        margin-bottom: 8px;
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
        <p style="color: #b0bec5; font-size: 11px; margin-top: 4px; margin-bottom: 0; letter-spacing: 2px;">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION</p>
    </div>
""", unsafe_allow_html=True)

# Inicializar os 20 estilos com nomes descritivos reais e limpos
if "db_estilos" not in st.session_state:
    st.session_state.db_estilos = {
        1: {"titulo": "Estilo 1: Caminhão e Van do TikTok Shop Chegando", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        2: {"titulo": "Estilo 2: POV Acordando na Cama (Morning Routine)", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        3: {"titulo": "Estilo 3: POV Arrumando o Closet / Selecionando Peças", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        4: {"titulo": "Estilo 4: POV Imersivo (Olhando para Baixo nos Pés)", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        5: {"titulo": "Estilo 5: Corpo Inteiro na Rua (Caminhando no Calçadão)", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        6: {"titulo": "Estilo 6: Frente ao Espelho (Mirror Selfie)", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        7: {"titulo": "Estilo 7: Giro Dinâmico 360° (Mostrando Caimento)", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        8: {"titulo": "Estilo 8: Close Macro Cirúrgico (Detalhes e Textura)", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        9: {"titulo": "Estilo 9: Unboxing Surpresa em Cima da Mesa", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        10: {"titulo": "Estilo 10: Transição Rápida de Looks", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        11: {"titulo": "Estilo 11: Vlog de Rotina Diária Estilo Lifestyle", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        12: {"titulo": "Estilo 12: Review Sincero Boca a Boca", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        13: {"titulo": "Estilo 13: Provador Rápido de Loja Física", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        14: {"titulo": "Estilo 14: Trend do Sofá / Almofada", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        15: {"titulo": "Estilo 15: POV Dirigindo o Carro", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        16: {"titulo": "Estilo 16: POV Café da Manhã na Mesa Posta", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        17: {"titulo": "Estilo 17: Challenge de Transição: Look Casual para Luxo", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        18: {"titulo": "Estilo 18: Unboxing Rasgando Pacote do TikTok Shop", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        19: {"titulo": "Estilo 19: POV Van de Entregas Chegando na Loja de Vidro", "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video..."},
        20: {
            "titulo": "Estilo 20: POV Caminhão Preto Gigante Parado com Portas Abertas e Valentina",
            "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: 20. Caminhão Preto Gigante do TikTok Parado com Portas Abertas e Valentina. STRICT ASSERTIVE CATEGORY & ZERO MIC PROTOCOL: Focus exclusively on footwear display, showing shoes clearly on feet, highlighting heel height and comfort. Strictly binding uploaded model reference face/body and isolated exact reference pixels of 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' with zero alterations, zero modifications to the product structure, details, or brand. Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone, completely bare clothing surface with zero attachments. Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock: identical reference model face and body proportions. Rigid product lock: exact 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' matching reference image with zero substitution, preserving original brand aesthetics. STATIC TRUCK & PERSISTENT BOX CHOREOGRAPHY (0-10s): From exact second 0, the camera is positioned behind the creator (Valentina) from a rear angle. The video opens instantly with Valentina speaking naturally with flawless lip-sync as she walks forward from inside her boutique toward the street. Directly in front of the store, a massive, giant black delivery truck with clean, bold \"TikTok\" lettering written in bright white on its black body is ALREADY PARKED in reverse, completely stationary with its rear cargo doors ALREADY WIDE OPEN, revealing an interior completely packed and stacked wall-to-wall up to the ceiling with storage boxes of the 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' (Brand Gigi). Valentina reaches the glass door, manually pushes it open with her hands, and walks straight up to the truck. She picks up a single storage box. STRICT PERSISTENCE RULE: Throughout the entire duration of the video, the storage box remains physically present and firmly held in her hands without ever disappearing, vanishing, or morphing. She opens the box steadily while holding it, lifts a matching pair of 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' directly out of the box while keeping the box visible in her grip, displays the footwear clearly to the camera, and concludes her sales pitch. IMMEDIATE FLAWLESS START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks, zero generated text captions. SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 10 seconds with zero abrupt audio cuts and zero dead silence. Fixed realistic background, organic human movement.\n\n\"Olha, gente... acabou de chegar o estoque aqui na Loja da Valentina. A gente vai trabalhar só com essa sandália, porque ela é recordista de vendas e de muita qualidade! Clica aqui no carrinho laranja embaixo para garantir a sua.\"\n\nAbsolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, AI morphing transition, soft blending, product switching, changing product model at the end, sudden jump cuts, rapid unrealistic pacing, over 10s, rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, text captions, generated writing, UI graphics, watermarks, distorted brand, altered design, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI, walking backward, truck moving, doors opening, box disappearing, box vanishing, item morphing into hand."
        }
    }

# 2. SELETORES DO TOPO (Compactos)
c_top1, c_top2 = st.columns(2)
with c_top1:
    diretor_skin = st.selectbox("DIRETOR SKIN", ["BOY (Elite Director)", "UGC LIFESTYLE"])
with c_top2:
    proporcao = st.selectbox("PROPORÇÃO", ["9:16 (TikTok / Reels)", "1:1 (Feed)"])

st.markdown("---")

# 3. SEÇÃO DE GERENCIAMENTO E EDIÇÃO DIRETA DOS ESTILOS
st.markdown("### ✏️ GERENCIAR E EDITAR ESTILOS (1 AO 20)")
st.info("💡 Escolha o número do estilo abaixo para alterar o título ou substituir o prompt diretamente em tempo real.")

# Seleção rápida do slot a ser editado
col_slot_num, col_slot_name = st.columns([1, 3])
with col_slot_num:
    slot_num_edit = st.selectbox("Nº do Estilo", options=list(st.session_state.db_estilos.keys()))
with col_slot_name:
    st.markdown(f"<p style='margin-top: 28px; font-weight:600; color: #00FF66;'>Editando: {st.session_state.db_estilos[slot_num_edit]['titulo']}</p>", unsafe_allow_html=True)

# Caixa limpa de edição do prompt selecionado
with st.container():
    novo_titulo_slot = st.text_input("Título / Nome do Estilo", value=st.session_state.db_estilos[slot_num_edit]["titulo"], key=f"t_{slot_num_edit}")
    novo_prompt_slot = st.text_area("Código do Prompt (Cole, apague ou substitua aqui)", value=st.session_state.db_estilos[slot_num_edit]["prompt"], height=160, key=f"p_{slot_num_edit}")
    
    if st.button("💾 Salvar Alterações deste Estilo"):
        st.session_state.db_estilos[slot_num_edit]["titulo"] = novo_titulo_slot
        st.session_state.db_estilos[slot_num_edit]["prompt"] = novo_prompt_slot
        st.success(f"✅ Estilo #{slot_num_edit} atualizado com sucesso!")

st.markdown("---")

# 4. SELEÇÃO PARA A GRADE DE GERAÇÃO
lista_titulos_geral = [st.session_state.db_estilos[i]["titulo"] for i in st.session_state.db_estilos]
estilos_selecionados = st.multiselect(
    "🎬 SELECIONE OS ESTILOS PARA GERAR NA GRADE DIÁRIA",
    options=lista_titulos_geral,
    default=[st.session_state.db_estilos[20]["titulo"]]
)

st.markdown("---")

# 5. ENTRADAS DO PRODUTO (Limpo e Organizado)
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Gigil Salto Bloco...")
    
    st.markdown("<p style='font-size:12px; font-weight:700; margin-bottom:4px;'>FOTO PRODUTO (ANÁLISE)</p>", unsafe_allow_html=True)
    foto_produto_analise = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="prod_1", label_visibility="collapsed")

    tipo_produto = st.selectbox("CATEGORIA", [
        "Calçado / Tênis / Sandália", 
        "Acessório", 
        "Vestuário",
        "Bolsa",
        "Outros"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:12px; font-weight:700; margin-bottom:4px;'>FOTO MODELO (FACE & CORPO 1:1)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m_1", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:12px; font-weight:700; margin-top:8px; margin-bottom:4px;'>FOTO REFERÊNCIA PEÇA (PIXEL LOCK)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Peça", type=["jpg", "jpeg", "png"], key="p_1", label_visibility="collapsed")

st.markdown("---")

GRADE_HORARIOS = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"]

# 6. BOTÃO DE GERAÇÃO
if st.button("🚀 GERAR PROMPTS DA GRADE DIÁRIA"):
    if not produto_nome:
        st.warning("⚠️ Informe o nome exato do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Faça o upload de todas as fotos necessárias.")
    elif not estilos_selecionados:
        st.warning("⚠️ Selecione pelo menos 1 estilo na grade.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"✅ Gerados {len(estilos_selecionados)} prompts às {agora} para '{produto_nome}'.")
        
        mapa_prompts = {st.session_state.db_estilos[i]["titulo"]: st.session_state.db_estilos[i]["prompt"] for i in st.session_state.db_estilos}
        
        for idx, estilo_titulo in enumerate(estilos_selecionados):
            prompt_numero = idx + 1
            horario_postagem = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
            prompt_ativo_slot = mapa_prompts.get(estilo_titulo, "Prompt não encontrado.")

            st.markdown(f"### 🎬 Prompt Comercial #{prompt_numero} • ⏰ Horário: {horario_postagem}")
            st.markdown(
                '<div class="metric-card">'
                f'<span class="tag-estilo">{estilo_titulo}</span><br>',
                unsafe_allow_html=True
            )
            st.code(prompt_ativo_slot, language="text")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
