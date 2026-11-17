import json
import os
import random
import urllib.request
import urllib.error
import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="centered"
)

# ESTÉTICA DE ALTO LUXO (BLINDADA E POLIDA)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #0b0914 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    div[data-testid="stFileUploader"] button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        border-radius: 6px !important;
        border: none !important;
        padding: 6px 12px !important;
        font-size: 13px !important;
        width: 100% !important;
    }
    div[data-testid="stFileUploader"] button * {
        color: #000000 !important;
        font-weight: 900 !important;
    }
    div[data-testid="stFileUploader"] button:hover {
        background-color: #00cc52 !important;
        color: #000000 !important;
    }
    
    div[data-testid="stFileUploader"] {
        background-color: #161026 !important;
        border: 1px solid #00FF66 !important;
        border-radius: 8px !important;
        padding: 10px !important;
    }
    div[data-testid="stFileUploader"] section {
        background-color: #161026 !important;
        border: none !important;
    }
    div[data-testid="stFileUploader"] small, div[data-testid="stFileUploader"] span, div[data-testid="stFileUploader"] div {
        color: #cccccc !important;
    }
    
    .stButton>button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border-radius: 6px !important;
        border: none !important;
        padding: 6px 12px !important;
        font-size: 13px !important;
        width: 100% !important;
    }
    .stButton>button:hover {
        background-color: #00cc52 !important;
        color: #ffffff !important;
    }
    
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
    
    input, select, div[data-baseweb="select"] > div {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        border-radius: 6px !important;
        min-height: 32px !important;
        font-size: 13px !important;
    }
    
    div[data-testid="stSelectbox"] { width: 100% !important; }
    div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1.5px solid #00FF66 !important;
        font-size: 13px !important;
        max-height: 300px !important;
        overflow-y: auto !important;
    }
    
    textarea {
        background-color: #161026 !important;
        color: #ffffff !important;
        border: 1px solid #00FF66 !important;
        border-radius: 6px !important;
        max-height: 180px !important;
        font-size: 12px !important;
        overflow-y: scroll !important;
    }
    
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

# MOTOR INTELIGENTE DE RESUMO E MODELAGEM DE COPY (CALIBRADO PARA EXATAMENTE 12.5s)
def resumir_e_modelar_copy_local(descricao_completa, categoria, historico_sessao):
    # Extrai termos-chave da descrição do usuário para injetar com inteligência
    desc_lower = descricao_completa.lower()
    
    # Identifica atributos principais mencionados na descrição
    destaques = []
    if "gel" in desc_lower or "palmilha" in desc_lower:
        destaques.append("com palmilha em gel super confortável")
    if "leve" in desc_lower:
        destaques.append("super leve e macio")
    if "cores" in desc_lower:
        destaques.append("com várias cores lindas")
    if "couro" in desc_lower or "material" in desc_lower:
        destaques.append("com acabamento impecável")
        
    detalhe_str = " ".join(destaques) if destaques else "com uma qualidade e acabamento incríveis"

    ganchos = [
        f"Gente, para tudo e olha os detalhes desse produto que acabou de chegar na Loja da Valentina!",
        f"Meninas, vocês simplesmente não têm noção do conforto real desse modelo quando a gente usa!",
        f"Eu juro que não estava preparada para a qualidade absurda e o padrão desse lançamento!",
        f"Olha de pertinho tudo o que esse produto entrega antes que acabe o nosso lote de hoje!"
    ]
    
    desenvolvimento = [
        f"Ele é {detalhe_str}, veste super bem no dia a dia e traz um visual sofisticado sem esforço.",
        f"Cada detalhe foi pensado para durar muito, unindo resistência {detalhe_str} e muita elegância.",
        f"É aquela peça coringa indispensável, {detalhe_str}, que valoriza qualquer look na hora."
    ]
    
    ctas = [
        "Clica agora no carrinho laranja aqui embaixo e garante o seu na Loja da Valentina!",
        "Toca no carrinho laranja no cantinho e aproveita enquanto ainda tem disponível no estoque!",
        "Já clica no carrinho laranja aqui embaixo para garantir com envio rápido!"
    ]
    
    tentativas = 0
    copy_final = ""
    while tentativas < 30:
        g = random.choice(ganchos)
        d = random.choice(desenvolvimento)
        c = random.choice(ctas)
        candidata = f'"{g} {d} {c}"'
        if candidata not in historico_sessao:
            copy_final = candidata
            break
        tentativas += 1
        
    if not copy_final:
        copy_final = f'"{random.choice(ganchos)} {random.choice(desenvolvimento)} {random.choice(ctas)}"'
        
    historico_sessao.add(copy_final)
    return copy_final

def gerar_copy_ia_gemini(api_key, descricao_completa, categoria, estilo_titulo, variacao_num):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key.strip()}"
    
    instrucao_sistema = (
        "Você é um Copywriter Sênior especialista em vídeos virais de alta conversão para TikTok Shop Brasil (Loja da Valentina). "
        "Sua tarefa é ANALISAR a descrição técnica completa enviada pelo usuário, extrair os atributos mais fortes (marca, conforto, material, diferenciais) "
        "e CRIAR uma fala 100% ORIGINAL, INÉDITA e NATURAL em Português do Brasil modelada para vídeos curtos. "
        "REGRAS OBRIGATÓRIAS: "
        "1. Tom espontâneo de influenciadora brasileira. "
        "2. Duração exata de leitura: 10 a 12.5 segundos (rigorosamente entre 30 e 38 palavras no máximo). "
        "3. Mencione 'Loja da Valentina' e o 'carrinho laranja' no final. "
        "4. Retorne APENAS a fala final entre aspas duplas."
    )
    
    prompt_usuario = (
        f"Analise esta descrição completa do produto e crie a variação criativa #{variacao_num} inédita:\n"
        f"- Descrição do Produto / Fornecedor: {descricao_completa}\n"
        f"- Categoria: {categoria}\n"
        f"- Estilo visual: {estilo_titulo}\n"
        f"Escreva apenas a fala falada pela criadora entre aspas:"
    )
    
    payload = {
        "contents": [{
            "parts": [{"text": f"{instrucao_sistema}\n\n{prompt_usuario}"}]
        }],
        "generationConfig": {
            "temperature": 0.95,
            "maxOutputTokens": 150
        }
    }
    
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    
    with urllib.request.urlopen(req, timeout=12) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        texto = res_data["candidates"][0]["content"]["parts"][0]["text"].strip()
        texto = texto.replace("\n", " ").strip()
        if not texto.startswith('"'):
            texto = f'"{texto}'
        if not texto.endswith('"'):
            texto = f'{texto}"'
        return texto

# FÁBRICA DE IDENTIDADE ORIGINAL (12.5s)
def obter_identidade_original(i):
    identidades_estilos = {
        1: ("Estilo 1: POV Mão & Revelação Tátil do Produto (ASMR)", "Foco tátil universal manuseando a peça com extrema nitidez, texturas refinadas e som imersivo de abertura."),
        2: ("Estilo 2: POV Corpo Inteiro em Movimento Dinâmico Urbano", "Câmera em movimento fluido acompanhando o produto de corpo inteiro (head-to-toe) ao ar livre sob luz natural."),
        3: ("Estilo 3: POV Provador de Luxo (Close Íntimo)", "Enquadramento elegante detalhando o caimento exato, a modelagem e a textura da peça."),
        4: ("Estilo 4: POV Giro 360 Graus em Frente ao Espelho", "Rotação e giros fluidos em frente ao espelho iluminado da boutique, exibindo todos os ângulos do item."),
        5: ("Estilo 5: POV Sem Fala com Trilha Viral & Transição Rápida", "Estilo puramente visual de altíssima retenção, sem diálogos, focado em cortes dinâmicos sincronizados com a batida da música."),
        6: ("Estilo 6: POV Close Macro com Foco nos Detalhes", "Câmera de perto apontada diretamente para o produto enviado, destacando acabamentos, costuras e diferenciais."),
        7: ("Estilo 7: Look do Dia Executivo & Elegância (Estilo Virgínia)", "Estética de alto padrão transmitindo autoridade, sofisticação e caimento impecável."),
        8: ("Estilo 8: Look Verão & Frescor na Praça Externa", "Cenário ensolarado e vibrante, mostrando leveza, versatilidade e praticidade."),
        9: ("Estilo 9: Estilo Clássico Imponente em Estúdio de Cinema", "Iluminação profissional de estúdio de cinema focada na imponência, postura e sofisticação máxima."),
        10: ("Estilo 10: Provador Expresso de Oferta Relâmpago", "Ritmo acelerado, troca dinâmica e foco em conversão imediata de estoque limitado e preço promocional."),
        11: ("Estilo 11: Destaque Dinâmico & Movimento Urbano", "Foco na utilidade e versatilidade do produto em trânsito pela cidade."),
        12: ("Estilo 12: Texturas Aconchegantes & Toque Suave", "Foco em macro-texturas, caimento flexível e toque agradável para o dia a dia."),
        13: ("Estilo 13: Look Noite & Balada com Luz Dramática", "Iluminação noturna sofisticada e moderna, destacando reflexos, brilho e acabamento sob neon."),
        14: ("Estilo 14: Estilo Atitude Streetwear & Modernidade", "Foco em design autêntico, estilo urbano moderno e apelo jovem para o TikTok."),
        15: ("Estilo 15: Peça Delicate (Close de Ocasião & Elegância)", "Detalhes delicados e acabamento refinado para ocasiões especiais."),
        16: ("Estilo 16: Sobreposição & Camadas Versáteis", "Estilo moderno de composição, demonstrando versatilidade e encaixe perfeito."),
        17: ("Estilo 17: Movimento Fluido & Apresentação Dinâmica", "Fluidez, leveza e apresentação natural do produto em uso."),
        18: ("Estilo 18: Peça Premium de Cós / Estrutura Alta & Elegância", "Caimento impecável e acabamento de alfaiataria em plano aberto."),
        19: ("Estilo 19: Praticidade & Funcionalidade Ágil", "Demonstração rápida de agilidade e facilidade de uso para o público."),
        20: ("Estilo 20: POV Caminhão Preto Gigante do TikTok (Estoque Chegando)", "Cenário épico externo com caminhão gigante estacionado e portas abertas repletas de caixas da Loja da Valentina.")
    }
    
    titulo_texto, desc_estilo = identidades_estilos.get(i, (f"Estilo {i}", "Estilo universal personalizado da Loja da Valentina."))
    
    if i == 20:
        prompt_texto = (
            "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 12.5-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: 20. Caminhão Preto Gigante do TikTok Parado com Portas Abertas e Valentina. "
            "STRICT UNIVERSAL PRODUCT LOCK & ZERO MIC PROTOCOL: Focus strictly on the exact product uploaded by the user with zero alterations, zero modifications to its structure, color, details, or brand. "
            "Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Clean collarbone, completely bare surface with zero attachments. "
            "Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock: identical reference model face and body proportions. "
            "CONTINUOUS TIMELINE CHOREOGRAPHY & RIGID OBJECT PERSISTENCE (0-12.5s): From exact second 0, the camera is positioned behind the creator (Valentina) from a rear angle. The video opens instantly with Valentina speaking naturally in Brazilian Portuguese with flawless lip-sync as she walks forward from inside her boutique toward the street in one single fluid, continuous motion with zero jump cuts. "
            "Directly in front of the store, a massive, giant black delivery truck with clean, bold 'TikTok' lettering written in bright white on its black body is ALREADY PARKED in reverse, completely stationary with its rear cargo doors ALREADY WIDE OPEN, revealing an interior completely packed and stacked wall-to-wall up to the ceiling with storage boxes. "
            "Valentina reaches the glass door, manually pushes it open with her hands, and walks straight up to the truck. She picks up a single storage box. "
            "RIGID PIXEL PERSISTENCE RULE: Throughout the entire duration, the storage box and the exact product inside remain physically permanent, 100% rigid, and unalterable. Absolute zero morphing, zero flickering, zero fading, zero transparency, zero ghosting transitions, and zero disappearance during lifting or handling. The hand and product maintain continuous, unbroken physical contact. "
            "IMMEDIATE FLAWLESS START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks, zero generated text captions. SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 12.5 seconds with zero abrupt audio cuts and zero dead silence."
        )
    elif i == 5:
        prompt_texto = (
            f"Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 12.5-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: {i}. {titulo_texto} - {desc_estilo}. "
            f"STRICT UNIVERSAL PRODUCT LOCK & ZERO MIC PROTOCOL: Faithfully match the exact product from the user-uploaded image with zero substitution, preserving original colors, textures, and details. "
            f"Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Clean collarbone. "
            f"Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock. "
            f"SILENT VISUAL SHOWCASE (0-12.5s): Purely visual dynamic showcase without spoken dialogue, synced to upbeat viral rhythm, showing the product from multiple flattering angles with smooth camera glides. "
            f"RIGID PIXEL PERSISTENCE RULE: The product maintains continuous, unbroken physical integrity, remaining 100% rigid, stable, and completely identical to the reference image. Absolute zero morphing, zero flickering, zero ghosting transitions, and zero object disappearance."
        )
    else:
        prompt_texto = (
            f"Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 12.5-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: {i}. {titulo_texto} - {desc_estilo}. "
            f"STRICT UNIVERSAL PRODUCT LOCK & ZERO MIC PROTOCOL: Faithfully match the exact product from the user-uploaded image with zero substitution, preserving original colors, textures, and details. "
            f"Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Clean collarbone. "
            f"Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock. "
            f"CONTINUOUS TIMELINE CHOREOGRAPHY & RIGID OBJECT PERSISTENCE (0-12.5s): The video opens dynamically with the creator moving smoothly (e.g., standing up, turning, or walking in a single continuous fluid motion with zero jump cuts) while speaking naturally in Brazilian Portuguese with flawless lip-sync and interacting directly with the item. "
            f"RIGID PIXEL PERSISTENCE RULE: The product maintains continuous, unbroken physical contact with the model's hand, remaining 100% rigid, stable, and completely identical to the reference image. Absolute zero morphing, zero flickering, zero ghosting transitions, and zero object disappearance. Pacing speech evenly across the full 12.5 seconds."
        )
    return titulo_texto, prompt_texto

# PERSISTÊNCIA PERMANENTE NO DISCO (JSON)
DB_FILE = "moldes_salvos.json"
CONFIG_FILE = "config_ia.json"

def carregar_config_ia():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"api_key": ""}

def salvar_config_ia(cfg):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def carregar_db_disco():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                dados = json.load(f)
                if isinstance(dados, dict):
                    db_convertido = {}
                    for k, v in dados.items():
                        k_final = int(k) if str(k).isdigit() else k
                        if isinstance(v, dict) and "titulo" in v and "prompt" in v:
                            db_convertido[k_final] = v
                    return db_convertido
        except Exception:
            pass
            
    if not os.path.exists(DB_FILE):
        padrao = {}
        for i in range(1, 21):
            t, p = obter_identidade_original(i)
            padrao[i] = {"titulo": t, "prompt": p}
        salvar_db_disco(padrao)
        return padrao
    return {}

def salvar_db_disco(db_dict):
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db_dict, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

# GESTÃO DE ESTADOS
if "db_estilos" not in st.session_state:
    st.session_state.db_estilos = carregar_db_disco()

if "config_ia" not in st.session_state:
    st.session_state.config_ia = carregar_config_ia()

if "form_version" not in st.session_state:
    st.session_state.form_version = 0

if "acesso_liberado" not in st.session_state:
    st.session_state.acesso_liberado = False

if "historico_copys" not in st.session_state:
    st.session_state.historico_copys = set()

def limpar_apenas_formulario():
    st.session_state.form_version += 1
    st.rerun()

v = st.session_state.form_version

# TOPO
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">LABORATÓRIOS VALENTINA</h1>
        <p class="hero-subtitle">LOJA DA VALENTINA • AUTOMATIZAÇÃO DE LOJAS NO TIKTOK</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# PAINEL DE CONTROLE RÁPIDO
st.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>⚡ PAINEL DE CONTROLE RÁPIDO</p>", unsafe_allow_html=True)

c_grid1, c_grid2, c_grid3 = st.columns(3)

with c_grid1:
    with st.container(border=True):
        st.markdown("🎬 **DIRETOR SKIN**")
        diretor_skin = st.selectbox("Skin", ["BOY (Elite Director)", "UGC LIFESTYLE"], label_visibility="collapsed", key=f"sel_skin_{v}")

with c_grid2:
    with st.container(border=True):
        st.markdown("📱 **PROPORÇÃO**")
        proporcao = st.selectbox("Proporção", ["9:16 (TikTok / Reels)", "1:1 (Feed)"], label_visibility="collapsed", key=f"sel_prop_{v}")

with c_grid3:
    with st.container(border=True):
        st.markdown("🧠 **MOTOR DE COPY**")
        modo_copy = st.selectbox("Motor Copy", ["IA Modeladora (Resumo Inteligente)", "Fixo (Do molde salvo)"], label_visibility="collapsed", key=f"sel_copy_mode_{v}")

with st.container(border=True):
    st.markdown("🎬 **SELECIONAR ESTILOS PARA GRADE DIÁRIA**")
    chaves_ordenadas = sorted(list(st.session_state.db_estilos.keys()), key=lambda x: (0, int(x)) if str(x).isdigit() else (1, str(x)))
    lista_titulos_geral = [st.session_state.db_estilos[k]["titulo"] for k in chaves_ordenadas] if chaves_ordenadas else []
    
    estilos_selecionados = st.multiselect(
        "Selecione",
        options=lista_titulos_geral,
        default=lista_titulos_geral[:1] if len(lista_titulos_geral) > 0 else [],
        label_visibility="collapsed",
        key=f"multi_estilos_{v}"
    )

# ÁREA RESTRITA PROTEGIDA POR SENHA ADMINISTRATIVA
SENHA_MESTRE = "vidalooka2"

with st.expander("⚙️ Gerenciar / Editar / Excluir Prompts & Cérebro IA (Área Restrita - Requer Senha)", expanded=False):
    col_s1, col_s2 = st.columns([3, 1])
    
    with col_s1:
        st.markdown("🔐 **SENHA ADMINISTRATIVA**")
        senha_digitada = st.text_input("Senha", placeholder="Digite a senha administrativa...", type="password", label_visibility="collapsed", key=f"input_senha_adm_{v}")
    
    with col_s2:
        st.markdown("🛡️ **AÇÃO**")
        if st.button("🔓 VALIDAR", key=f"btn_validar_{v}"):
            if senha_digitada == SENHA_MESTRE:
                st.session_state.acesso_liberado = True
                st.success("✅ Acesso administrativo liberado!")
            else:
                st.session_state.acesso_liberado = False
                st.error("❌ Senha incorreta.")

    st.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)

    if st.session_state.acesso_liberado:
        st.markdown("<p style='color: #00FF66; font-weight: 700;'>🔓 MODO ADMINISTRADOR ATIVO</p>", unsafe_allow_html=True)
        
        with st.container(border=True):
            st.markdown("🧠 **CONEXÃO CÉREBRO IA (API GEMINI - OPCIONAL)**")
            col_api1, col_api2 = st.columns([3, 1])
            with col_api1:
                nova_api_key = st.text_input(
                    "Chave API Gemini",
                    value=st.session_state.config_ia.get("api_key", ""),
                    type="password",
                    placeholder="Cole sua Gemini API Key aqui (opcional)...",
                    label_visibility="collapsed",
                    key=f"api_key_input_{v}"
                )
            with col_api2:
                if st.button("💾 SALVAR CHAVE", key=f"btn_save_api_{v}"):
                    st.session_state.config_ia["api_key"] = nova_api_key.strip()
                    salvar_config_ia(st.session_state.config_ia)
                    st.success("✅ Chave salva!")
                    time.sleep(0.5)
                    st.rerun()

        col_ger1, col_ger2 = st.columns(2)
        with col_ger1:
            if st.button("🗑️ ZERAR TODOS OS PROMPTS", key=f"btn_apagar_tudo_geral_{v}"):
                with st.spinner("🗑️ Apagando todos os prompts..."):
                    time.sleep(0.4)
                    st.session_state.db_estilos = {}
                    salvar_db_disco(st.session_state.db_estilos)
                st.success("✅ Banco zerado definitivamente!")
                time.sleep(0.8)
                st.rerun()

        with col_ger2:
            estilo_a_restaurar = st.number_input("Nº do Estilo para Restaurar (1 a 20)", min_value=1, max_value=20, value=1, step=1, key=f"num_rest_{v}")
            if st.button("🔄 RESTAURAR ESTE ESTILO ESPECÍFICO", key=f"btn_rest_one_{v}"):
                t_orig, p_orig = obter_identidade_original(estilo_a_restaurar)
                st.session_state.db_estilos[estilo_a_restaurar] = {"titulo": t_orig, "prompt": p_orig}
                salvar_db_disco(st.session_state.db_estilos)
                st.success(f"✅ Estilo {estilo_a_restaurar} restaurado com sucesso!")
                time.sleep(0.8)
                st.rerun()

        st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

        numeric_keys = [k for k in chaves_ordenadas if str(k).isdigit()]
        proximo_id_sugerido = (max([int(k) for k in numeric_keys]) + 1) if numeric_keys else 1

        modo_operacao = st.radio("Modo de Operação", ["✏️ Editar / Excluir Estilo Existente", f"➕ Inserir Novo (Manual / ID {proximo_id_sugerido})"], horizontal=True, label_visibility="collapsed", key=f"modo_op_{v}")

        st.markdown(f"<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>{modo_operacao.upper()}</p>", unsafe_allow_html=True)

        with st.container(border=True):
            if "Editar" in modo_operacao:
                if chaves_ordenadas:
                    slot_num_edit = st.selectbox(
                        "Selecione o Estilo para Editar", 
                        options=chaves_ordenadas, 
                        format_func=lambda x: f"Estilo {x} - {st.session_state.db_estilos[x]['titulo']}",
                        key=f"select_editor_direto_id_{v}"
                    )

                    titulo_atual_estilo = st.session_state.db_estilos[slot_num_edit]["titulo"]
                    prompt_atual_estilo = st.session_state.db_estilos[slot_num_edit]["prompt"]

                    novo_titulo_editado = st.text_input("Tema / Título do Estilo", value=titulo_atual_estilo, key=f"titulo_input_edit_{slot_num_edit}_{v}")
                    texto_editado_usuario = st.text_area("Código do Prompt", value=prompt_atual_estilo, height=160, key=f"prompt_textarea_edit_{slot_num_edit}_{v}")
                    
                    st.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
                    
                    col_b_salvar, col_b_exc = st.columns(2)
                    
                    with col_b_salvar:
                        if st.button("💾 SALVAR ALTERAÇÃO", key=f"btn_salvar_{slot_num_edit}_{v}"):
                            if not novo_titulo_editado or not texto_editado_usuario:
                                st.warning("⚠️ Preencha o Título e o Código antes de salvar.")
                            else:
                                with st.spinner(f"💾 Salvando alterações no disco..."):
                                    time.sleep(0.4)
                                    st.session_state.db_estilos[slot_num_edit]["titulo"] = novo_titulo_editado
                                    st.session_state.db_estilos[slot_num_edit]["prompt"] = texto_editado_usuario
                                    salvar_db_disco(st.session_state.db_estilos)
                                st.success(f"✨ Estilo {slot_num_edit} alterado com sucesso!")
                                time.sleep(0.8)
                                st.rerun()
                                
                    with col_b_exc:
                        if st.button("🗑️ EXCLUIR ESTE ESTILO", key=f"btn_exc_direto_{slot_num_edit}_{v}"):
                            with st.spinner(f"🗑️ Excluindo Estilo {slot_num_edit}..."):
                                time.sleep(0.3)
                                del st.session_state.db_estilos[slot_num_edit]
                                salvar_db_disco(st.session_state.db_estilos)
                            st.success(f"🗑️ Estilo excluído definitivamente do disco!")
                            time.sleep(0.8)
                            st.rerun()
                else:
                    st.info("Nenhum estilo disponível no momento.")
            else:
                novo_id_manual = st.number_input("ID Numérico do Novo Estilo", min_value=1, value=proximo_id_sugerido, step=1, key=f"id_manual_{v}")
                novo_titulo_input = st.text_input("Título / Tema do Novo Prompt", value="", placeholder="Ex: Meu Estilo Personalizado...", key=f"campo_novo_titulo_valencia_fixo_{v}")
                novo_prompt_input = st.text_area("Código do Prompt", placeholder="Cole o código técnico do prompt aqui...", height=160, key=f"campo_novo_prompt_valencia_fixo_{v}")
                
                st.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
                
                if st.button("📥 INSERIR E SALVAR NO SISTEMA", key=f"btn_inserir_novo_{v}"):
                    if not novo_titulo_input or not novo_prompt_input:
                        st.warning("⚠️ Preencha o Título e o Código do novo prompt.")
                    else:
                        with st.spinner(f"📥 Inserindo novo estilo..."):
                            time.sleep(0.4)
                            st.session_state.db_estilos[novo_id_manual] = {
                                "titulo": novo_titulo_input,
                                "prompt": novo_prompt_input
                            }
                            salvar_db_disco(st.session_state.db_estilos)
                        st.success(f"🎉 Estilo {novo_id_manual} inserido e gravado permanentemente!")
                        time.sleep(0.8)
                        st.rerun()
    else:
        st.info("🔒 Insira a senha administrativa correta acima para desbloquear a gestão de prompts.")

st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# DADOS DO PRODUTO & UPLOADS (DESCRIÇÃO COMPLETA PARA RESUMO INTELIGENTE)
st.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>📦 DADOS DO PRODUTO & DESCRIÇÃO TÉCNICA</p>", unsafe_allow_html=True)

with st.container(border=True):
    c_l1_1, c_l1_2 = st.columns(2)
    with c_l1_1:
        st.markdown("🏷️ **NOME / MARCA DO PRODUTO**")
        produto_nome = st.text_input("Nome", placeholder="Ex: Tênis Sapatilha Wayper...", label_visibility="collapsed", key=f"input_nome_produto_{v}")
    with c_l1_2:
        st.markdown("📂 **CATEGORIA**")
        tipo_produto = st.selectbox("Categoria", ["Calçado", "Vestuário", "Acessório", "Bolsa", "Outros"], label_visibility="collapsed", key=f"sel_categoria_{v}")

    st.markdown("📝 **DESCRIÇÃO COMPLETA (Cole tudo aqui: marca, modelo, palmilha em gel, cores, detalhes...)**")
    descricao_fornecedor = st.text_area("Descrição", placeholder="Cole aqui a descrição completa do seu fornecedor. O app vai analisar tudo e resumir os melhores argumentos no roteiro...", height=100, label_visibility="collapsed", key=f"input_desc_completa_{v}")

    st.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)

    c_f1, c_f2, c_f3 = st.columns(3)
    
    with c_f1:
        st.markdown("👩 **FOTO MODELO**")
        foto_modelo = st.file_uploader("Foto Modelo", type=["jpg", "jpeg", "png"], key=f"m_1_{v}", label_visibility="collapsed")
        
    with c_f2:
        st.markdown("📷 **FOTO PRODUTO**")
        foto_produto_analise = st.file_uploader("Foto Produto", type=["jpg", "jpeg", "png"], key=f"prod_1_{v}", label_visibility="collapsed")
        
    with c_f3:
        st.markdown("🔍 **FOTO ZOOM**")
        foto_peca = st.file_uploader("Foto Zoom", type=["jpg", "jpeg", "png"], key=f"p_1_{v}", label_visibility="collapsed")

st.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)

# BOTÕES CENTRALIZADOS
col_esq_vazio, col_btn1, col_btn2, col_dir_vazio = st.columns([1, 2, 2, 1])

with col_btn1:
    gerar_clicado = st.button("🚀 GERAR PROMPTS", key=f"btn_gerar_{v}")

with col_btn2:
    st.button("🔄 LIMPAR TUDO", on_click=limpar_apenas_formulario, key=f"btn_limpar_tudo_{v}")

GRADE_HORARIOS = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"]

if gerar_clicado:
    if not produto_nome and not descricao_fornecedor:
        st.warning("⚠️ Informe o nome ou cole a descrição do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Envie todas as fotos.")
    elif not estilos_selecionados:
        st.warning("⚠️ Selecione pelo menos 1 estilo.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        api_key_salva = st.session_state.config_ia.get("api_key", "").strip()
        texto_base_analise = f"{produto_nome} - {descricao_fornecedor}"
        
        mapa_prompts = {st.session_state.db_estilos[i]["titulo"]: st.session_state.db_estilos[i]["prompt"] for i in st.session_state.db_estilos if i in st.session_state.db_estilos}
        
        with st.spinner("🧠 Analisando descrição e resumindo para 12.5s..."):
            st.success(f"✅ Gerados {len(estilos_selecionados)} prompts às {agora} para '{produto_nome}'.")
            
            for idx, estilo_titulo in enumerate(estilos_selecionados):
                prompt_numero = idx + 1
                horario_postagem = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
                prompt_base = mapa_prompts.get(estilo_titulo, "Prompt não encontrado.")
                
                eh_estilo_mudo = "Sem Fala" in estilo_titulo or "SILENT VISUAL SHOWCASE" in prompt_base
                
                if eh_estilo_mudo or ("Fixo" in modo_copy and '"' in prompt_base):
                    prompt_final_montado = prompt_base
                    copy_gerada_exibicao = "Fala fixa mantida do seu molde salvo."
                else:
                    fala_resumida = ""
                    if api_key_salva:
                        try:
                            fala_resumida = gerar_copy_ia_gemini(
                                api_key=api_key_salva,
                                descricao_completa=texto_base_analise,
                                categoria=tipo_produto,
                                estilo_titulo=estilo_titulo,
                                variacao_num=prompt_numero + random.randint(1, 999)
                            )
                        except Exception:
                            fala_resumida = resumir_e_modelar_copy_local(texto_base_analise, tipo_produto, st.session_state.historico_copys)
                    else:
                        fala_resumida = resumir_e_modelar_copy_local(texto_base_analise, tipo_produto, st.session_state.historico_copys)
                        
                    copy_gerada_exibicao = fala_resumida
                    prompt_final_montado = f"{prompt_base}\n\n{fala_resumida}"

                st.markdown(f"### 🎬 Prompt {prompt_numero} • {horario_postagem}")
                st.markdown(
                    '<div class="metric-card">'
                    f'<span class="tag-estilo">{estilo_titulo}</span><br>'
                    f'<span style="color:#00FF66; font-size:11px;">🗣️ <b>Fala Resumida (12.5s):</b> {copy_gerada_exibicao}</span>',
                    unsafe_allow_html=True
                )
                st.code(prompt_final_montado, language="text")
                st.markdown('</div>', unsafe_allow_html=True)
