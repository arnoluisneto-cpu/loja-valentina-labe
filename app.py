import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="wide"
)

# ESTÉTICA ORIGINAL DE ALTO LUXO (Fundo Escuro Puro, Padrão Verde Neon)
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
        <p style="color: #b0bec5; font-size: 12px; margin-top: 5px; margin-bottom: 0; letter-spacing: 2px;">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION (REAL-TIME EDITABLE ENGINE)</p>
    </div>
""", unsafe_allow_html=True)

# 2. SELETORES DO TOPO
c_top1, c_top2 = st.columns(2)
with c_top1:
    diretor_skin = st.selectbox("DIRETOR SKIN", ["BOY (Elite Director)", "UGC LIFESTYLE (Influencer & Conversão)"])
with c_top2:
    proporcao = st.selectbox("PROPORÇÃO", ["9:16 (TikTok / Reels)", "1:1 (Feed)", "16:9 (Wide)"])

st.markdown("---")

# 3. PAINEL DE EDIÇÃO EM TEMPO REAL DOS 20 SLOTS DE ESTILOS
st.markdown("### ⚙️ EDITOR EM TEMPO REAL DOS ESTILOS (1 AO 20)")
st.info("💡 Selecione qualquer slot abaixo para apagar, reescrever ou substituir o prompt instantaneamente. Clique em 'Salvar' para atualizar o banco de dados do aplicativo.")

if "db_estilos" not in st.session_state:
    st.session_state.db_estilos = {
        i: {
            "titulo": f"{i}. Estilo Padrão Loja da Valentina #{i}",
            "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science..."
        } for i in range(1, 21)
    }
    # Deixar o Slot 20 pré-configurado com o nosso prompt definitivo do caminhão
    st.session_state.db_estilos[20] = {
        "titulo": "20. POV Caminhão Preto Gigante Parado com Portas Abertas e Valentina",
        "prompt": "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: 20. Caminhão Preto Gigante do TikTok Parado com Portas Abertas e Valentina. STRICT ASSERTIVE CATEGORY & ZERO MIC PROTOCOL: Focus exclusively on footwear display, showing shoes clearly on feet, highlighting heel height and comfort. Strictly binding uploaded model reference face/body and isolated exact reference pixels of 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' with zero alterations, zero modifications to the product structure, details, or brand. Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Bare clothes, clean collarbone, completely bare clothing surface with zero attachments. Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock: identical reference model face and body proportions. Rigid product lock: exact 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' matching reference image with zero substitution, preserving original brand aesthetics. STATIC TRUCK & PERSISTENT BOX CHOREOGRAPHY (0-10s): From exact second 0, the camera is positioned behind the creator (Valentina) from a rear angle. The video opens instantly with Valentina speaking naturally with flawless lip-sync as she walks forward from inside her boutique toward the street. Directly in front of the store, a massive, giant black delivery truck with clean, bold \"TikTok\" lettering written in bright white on its black body is ALREADY PARKED in reverse, completely stationary with its rear cargo doors ALREADY WIDE OPEN, revealing an interior completely packed and stacked wall-to-wall up to the ceiling with storage boxes of the 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' (Brand Gigi). Valentina reaches the glass door, manually pushes it open with her hands, and walks straight up to the truck. She picks up a single storage box. STRICT PERSISTENCE RULE: Throughout the entire duration of the video, the storage box remains physically present and firmly held in her hands without ever disappearing, vanishing, or morphing. She opens the box steadily while holding it, lifts a matching pair of 'SANDALIA MARCA GIGIL SALTO BLOCO COR PRETA' directly out of the box while keeping the box visible in her grip, displays the footwear clearly to the camera, and concludes her sales pitch. IMMEDIATE FLAWLESS START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks, zero generated text captions. SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 10 seconds with zero abrupt audio cuts and zero dead silence. Fixed realistic background, organic human movement.\n\n\"Olha, gente... acabou de chegar o estoque aqui na Loja da Valentina. A gente vai trabalhar só com essa sandália, porque ela é recordista de vendas e de muita qualidade! Clica aqui no carrinho laranja embaixo para garantir a sua.\"\n\nAbsolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, AI morphing transition, soft blending, product switching, changing product model at the end, sudden jump cuts, rapid unrealistic pacing, over 10s, rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, text captions, generated writing, UI graphics, watermarks, distorted brand, altered design, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI, walking backward, truck moving, doors opening, box disappearing, box vanishing, item morphing into hand."
    }

slot_ativo = st.selectbox(
    "SELECIONE O SLOT PARA EDITAR EM TEMPO REAL",
    options=list(st.session_state.db_estilos.keys()),
    format_func=lambda x: st.session_state.db_estilos[x]["titulo"]
)

with st.form(key=f"form_slot_{slot_ativo}"):
    titulo_editado = st.text_input("Editar Título do Estilo", value=st.session_state.db_estilos[slot_ativo]["titulo"])
    prompt_editado = st.text_area("Editar Código do Prompt (Cole ou Apague aqui)", value=st.session_state.db_estilos[slot_ativo]["prompt"], height=220)
    
    botao_salvar = st.form_submit_button(label=f"💾 Salvar Modificações do Slot #{slot_ativo}")
    if botao_salvar:
        st.session_state.db_estilos[slot_ativo]["titulo"] = titulo_editado
        st.session_state.db_estilos[slot_ativo]["prompt"] = prompt_editado
        st.success(f"✅ Slot #{slot_ativo} atualizado com sucesso no aplicativo!")

st.markdown("---")

# Seleção dos estilos para gerar a grade de vídeos
lista_titulos = [st.session_state.db_estilos[i]["titulo"] for i in st.session_state.db_estilos]
estilos_selecionados = st.multiselect(
    "🎬 SELECIONE OS ESTILOS PARA A GRADE DE GERAÇÃO DIÁRIA",
    options=lista_titulos,
    default=[st.session_state.db_estilos[20]["titulo"]]
)

st.markdown("---")

# 4. ENTRADAS DO PRODUTO
col_input1, col_input2 = st.columns(2)

with col_input1:
    produto_nome = st.text_input("NOME EXATO DO PRODUTO / SKU", placeholder="Ex: Sandália Gigil Salto Bloco...")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>DESCRIÇÃO DO PRODUTO - UPLOAD FOTO</p>", unsafe_allow_html=True)
    foto_produto_analise = st.file_uploader("Upload Foto Produto", type=["jpg", "jpeg", "png"], key="prod_upload_original", label_visibility="collapsed")

    tipo_produto = st.selectbox("CATEGORIA DO PRODUTO (FOCO ASSERTIVO)", [
        "Calçado / Tênis / Sandália", 
        "Acessório de Pulso ou Rosto (Relógio / Óculos)", 
        "Vestuário / Vestido / Conjunto / Calça",
        "Bolsa / Acessório de Mão",
        "Utilidades & Outros"
    ])
    
with col_input2:
    st.markdown("<p style='font-size:13px; font-weight:700; margin-bottom:4px;'>1. FOTO MODELO (FACE & CORPO 1:1 + TRAVA ABSOLUTA)</p>", unsafe_allow_html=True)
    foto_modelo = st.file_uploader("Upload Modelo", type=["jpg", "jpeg", "png"], key="m", label_visibility="collapsed")
    
    st.markdown("<p style='font-size:13px; font-weight:700; margin-top:10px; margin-bottom:4px;'>2. FOTO REFERÊNCIA PEÇA (ISOLADA + TRAVA RÍGIDA DE PIXEL)</p>", unsafe_allow_html=True)
    foto_peca = st.file_uploader("Upload Produto", type=["jpg", "jpeg", "png"], key="p", label_visibility="collapsed")

st.markdown("---")

GRADE_HORARIOS = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"]

# 5. GERADOR DA GRADE
if st.button("🚀 GERAR PROMPTS DA GRADE DIÁRIA • LIVE EDITABLE ENGINE"):
    if not produto_nome:
        st.warning("⚠️ Por favor, informe o nome exato do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Por favor, faça o upload de todas as fotos necessárias.")
    elif not estilos_selecionados:
        st.warning("⚠️ Por favor, selecione pelo menos 1 estilo/cenário no seletor acima.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        total_gerados = len(estilos_selecionados)
        st.success(f"✅ Gerados {total_gerados} prompts às {agora} | Produto: '{produto_nome}' | Sincronizados com a grade diária.")
        
        mapa_prompts = {st.session_state.db_estilos[i]["titulo"]: st.session_state.db_estilos[i]["prompt"] for i in st.session_state.db_estilos}
        
        for idx, estilo_titulo in enumerate(estilos_selecionados):
            prompt_numero = idx + 1
            horario_postagem = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
            prompt_ativo_slot = mapa_prompts.get(estilo_titulo, "Prompt não encontrado.")

            st.markdown(f"### 🎬 Prompt Comercial #{prompt_numero} • ⏰ Horário: {horario_postagem}")
            st.markdown(
                '<div class="metric-card">'
                f'<span class="tag-estilo">Horário: {horario_postagem} | Cenário: {estilo_titulo} (10s)</span><br>',
                unsafe_allow_html=True
            )
            st.code(prompt_ativo_slot, language="text")
            st.markdown('</div>', unsafe_allow_html=True)
            st.markdown("---")
