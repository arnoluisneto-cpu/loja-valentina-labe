import json
import os
import random
import re
import urllib.request
import time
import streamlit as st

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="centered"
)

# ESTÉTICA DE ALTO LUXO ORIGINAL (MANTIDA IDÊNTICA)
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

# BLINDAGEM CONTRA "KIT/KITS" E "CONJUNTO/CONJUNTOS" (E DEMAIS TERMOS DE RISCO)
SUBSTITUICOES_COMPLIANCE = [
    (r"\bkits?\b", "combinação"),
    (r"\bconjunto\b", "combinação"),
    (r"\bconjuntos\b", "combinações"),
    (r"\bcombo\b", "opção"),
    (r"\bgarantia absoluta\b", "boa experiência"),
    (r"\bresultado garantido\b", "uso prático"),
    (r"\búltima unidade\b", "disponível no carrinho"),
    (r"\bestoque acabando\b", "alta procura"),
    (r"\bwhatsapp\b|\btelegram\b|\bshopee\b|\bmercado livre\b", "carrinho laranja")
]

# UNIVERSALIZAÇÃO AUTOMÁTICA DE QUALQUER PROMPT ENVIADO OU SALVO
SUBSTITUICOES_UNIVERSAIS = [
    (r"\bcanetas?\s+de\s+nail\s+art\b|\bnail\s+art\b|\bcanetas?\b", "o produto de referência"),
    (r"\bunhas?\s+decoradas?\b|\bunhas?\b|\bmesa\s+de\s+manicure\b", "o produto em uso real"),
    (r"\bcamisolas?\s+curtas?\s+de\s+cetim\s+brilhante\s+com\s+decote\s+em\s+renda\s+vermelha\s+e\s+al[çc]as\s+finas\s+sobre\s+mesa\s+de\s+m[áa]rmore\b", "o produto de referência"),
    (r"\bcamisolas?\b|\bcetim\s+brilhante\b|\brenda\s+vermelha\b|\bmesa\s+de\s+m[áa]rmore\b", "o produto selecionado"),
    (r"\btops?\s+de\s+diferentes\s+cores\s+sobre\s+um\s+len[çc]ol\s+branco\b", "o produto de referência sobre uma superfície clara e neutra"),
    (r"\blen[çc]ol\s+branco\b", "superfície clara e neutra"),
    (r"\bsand[áa]lias?\b|\bt[êe]nis\b|\bpantalonas?\b|\brel[óo]gios?\b", "o produto selecionado")
]

# OS 6 GANCHOS DO VÍDEO + VARIAÇÕES DE DOR/AMIGO (SEM REPETIR NA MESMA RODADA)
ESTILOS_FALA_POR_INDICE = {
    1: "gancho_1_promocao_intensa_amigo",
    2: "gancho_2_preco_x_prejuizo_amigo",
    3: "gancho_3_nao_espera_ficar_sem_amigo",
    4: "gancho_4_todo_mundo_comprando_amigo",
    5: "gancho_5_cara_de_luxo_preco_leve_amigo",
    6: "gancho_6_nem_precisava_mas_pegou_amigo",
    7: "fala_visual_sem_audio",
    8: "gancho_3_nao_espera_ficar_sem_amigo"
}

TRAVA_ANTI_TEXTO_FLUTUANTE = (
    "zero floating text, no on-screen text, no captions, no subtitles, no graphics, "
    "no social media icons or UI overlays, no watermarks, no third-party logos, no unrequested objects."
)

def sanitizar_copy_tiktok_shop(texto):
    limpo = texto or ""
    for padrao, substituto in SUBSTITUICOES_COMPLIANCE:
        limpo = re.sub(padrao, substituto, limpo, flags=re.IGNORECASE)
    return " ".join(limpo.split())

def universalizar_prompt(texto):
    limpo = sanitizar_copy_tiktok_shop(texto)
    for padrao, substituto in SUBSTITUICOES_UNIVERSAIS:
        limpo = re.sub(padrao, substituto, limpo, flags=re.IGNORECASE)
    limpo = re.sub(r"\b12s\b", "11s", limpo, flags=re.IGNORECASE)
    limpo = " ".join(limpo.split())
    if "no floating text" not in limpo.lower() and "no on-screen text" not in limpo.lower():
        limpo = f"{limpo} {TRAVA_ANTI_TEXTO_FLUTUANTE}"
    return " ".join(limpo.split())

def _contar_palavras_reais(texto_sem_aspas):
    return len([p for p in texto_sem_aspas.strip().split() if p])

# MOTOR LOCAL COM OS 6 GANCHOS DO VÍDEO EM TOM DE AMIGO BATENDO NA DOR (11s / 22 A 30 PALAVRAS)
def resumir_e_modelar_copy_local(nome_produto, descricao_completa, categoria, estilo_fala, historico_sessao, falas_usadas_lote):
    prod_bruto = sanitizar_copy_tiktok_shop(nome_produto)
    cat_bruta = sanitizar_copy_tiktok_shop(categoria).lower()
    prod_limpo = prod_bruto if prod_bruto else f"esse item de {cat_bruta}"
    prod_curto = " ".join(prod_limpo.split()[:3])

    banco_por_estilo = {
        "gancho_1_promocao_intensa_amigo": [
            f"Amiga, acharam que a promoção virou o fim do mundo! Eu tava sofrendo com {cat_bruta} ruim até ver esse {prod_curto} na Loja da Valentina: clica no carrinho laranja!",
            f"Cara, o pessoal surtou nessa oferta como se fosse o fim do mundo! Eu já errava muito até pegar esse {prod_curto} na Loja da Valentina: clica no carrinho laranja!"
        ],
        "gancho_2_preco_x_prejuizo_amigo": [
            f"Cara, nem sei como compensa esse preço depois de tanto prejuízo com {cat_bruta} fraco! Esse {prod_curto} da Loja da Valentina salvou: abre o carrinho laranja aqui embaixo!",
            f"Amiga, juro que não sei como tá nesse valor após errar tanto com {cat_bruta} ruim! Esse {prod_curto} da Loja da Valentina valeu muito: clica no carrinho laranja!"
        ],
        "gancho_3_nao_espera_ficar_sem_amigo": [
            f"Sério, se esperar viralizar e deixar pra depois, vai ficar sem de novo! Peguei esse {prod_curto} na Loja da Valentina antes que acabasse: clica no carrinho laranja!",
            f"Amiga, quem deixa pra depois sempre sofre ficando sem na hora que precisa! Garanti esse {prod_curto} na Loja da Valentina pra não passar vontade: abre o carrinho laranja!"
        ],
        "gancho_4_todo_mundo_comprando_amigo": [
            f"Amiga, eu via todo mundo pegando e tava cansada de sofrer com {cat_bruta} ruim! Fui testar esse {prod_curto} da Loja da Valentina e entendi: clica no carrinho laranja!",
            f"Cara, vi geral comprando enquanto eu aguentava {cat_bruta} que incomodava! Peguei esse {prod_curto} na Loja da Valentina e mudou tudo: abre o carrinho laranja aqui embaixo!"
        ],
        "gancho_5_cara_de_luxo_preco_leve_amigo": [
            f"Cara, parece item caro de luxo, mas sem o sufoco de estourar o bolso! Esse {prod_curto} da Loja da Valentina surpreendeu demais: clica no carrinho laranja e garante!",
            f"Amiga, tem cara de peça cara de vitrine, mas sem dor de gastar demais! Esse {prod_curto} da Loja da Valentina é um achado: abre o carrinho laranja aqui embaixo!"
        ],
        "gancho_6_nem_precisava_mas_pegou_amigo": [
            f"Amiga, eu nem tava pensando em pegar agora, mas pelo preço leve garanti mais de um! Achado da Loja da Valentina que resolve a dor: clica no carrinho laranja!",
            f"Cara, juro que nem precisava naquele minuto, mas com esse valor peguei logo! Esse {prod_curto} da Loja da Valentina vale o clique: abre o carrinho laranja aqui embaixo!"
        ],
        "fala_visual_sem_audio": [
            f"Sem legenda e sem enrolação: olha esse {prod_curto} resolvendo a dor na prática! Achado da Loja da Valentina direto no ponto: clica no carrinho laranja e garante!"
        ]
    }

    opcoes = list(banco_por_estilo.get(estilo_fala, banco_por_estilo["gancho_1_promocao_intensa_amigo"]))
    random.shuffle(opcoes)

    for raw in opcoes:
        frase = sanitizar_copy_tiktok_shop(raw)
        qtd = _contar_palavras_reais(frase)
        candidata = f'"{frase}"'
        if 21 <= qtd <= 31 and candidata not in historico_sessao and candidata not in falas_usadas_lote:
            historico_sessao.add(candidata)
            falas_usadas_lote.add(candidata)
            return candidata

    for raw in opcoes:
        frase = sanitizar_copy_tiktok_shop(raw)
        candidata = f'"{frase}"'
        if candidata not in historico_sessao and candidata not in falas_usadas_lote:
            historico_sessao.add(candidata)
            falas_usadas_lote.add(candidata)
            return candidata

    fallback = f'"{sanitizar_copy_tiktok_shop(opcoes[0])}"'
    historico_sessao.add(fallback)
    falas_usadas_lote.add(fallback)
    return fallback

def gerar_copy_ia_gemini(api_key, nome_produto, descricao_completa, categoria, estilo_titulo, estilo_fala, variacao_num, historico_sessao, falas_usadas_lote):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key.strip()}"
    bloqueadas = list(historico_sessao)[-6:] + list(falas_usadas_lote)
    evitar_txt = f" NÃO repita nenhuma destas falas: {' | '.join(bloqueadas[-8:])}." if bloqueadas else ""

    instrucao_sistema = (
        "Você escreve falas para TikTok Shop Brasil em tom de AMIGO INDICANDO PARA AMIGO ('Amiga...', 'Cara...', 'Sério...'), "
        "com 11 segundos cravados (24 a 29 palavras). "
        "Use a energia do gancho viral especificado (promoção intensa, dúvida de como compensa o preço, medo de ficar sem "
        "se esperar viralizar, todo mundo pegando e ir ver por que, aparência de luxo com preço leve, ou nem precisava "
        "mas pegou pelo preço), SEMPRE atingindo a dor real do cliente no gancho e no desenvolvimento, "
        "citando 'Loja da Valentina' e chamando para o 'carrinho laranja'. "
        "Nada de linguagem robótica de anúncio genérico ('acabamento firme', 'solução funcional'). "
        f"Gancho/estilo de fala: '{estilo_fala}'. "
        "NUNCA use as palavras 'kit', 'kits', 'conjunto', 'conjuntos', 'combo', promessas absolutas "
        "ou menções a plataformas externas. Retorne APENAS a fala entre aspas duplas."
        f"{evitar_txt}"
    )
    payload = {
        "contents": [{
            "parts": [{
                "text": (
                    f"{instrucao_sistema}\n"
                    f"Produto: {sanitizar_copy_tiktok_shop(nome_produto)} | Categoria: {sanitizar_copy_tiktok_shop(categoria)} | "
                    f"Estilo: {estilo_titulo} | Var #{variacao_num}\n"
                    f"Detalhes: {sanitizar_copy_tiktok_shop(descricao_completa)}"
                )
            }]
        }],
        "generationConfig": {"temperature": 1.0, "maxOutputTokens": 95}
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=12) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        candidates = res_data.get("candidates") or []
        if not candidates:
            raise ValueError("Resposta sem candidatos.")
        partes = ((candidates[0].get("content") or {}).get("parts")) or []
        texto_bruto = ((partes[0].get("text") if partes else "") or "").strip().replace("\n", " ")
        texto_limpo = sanitizar_copy_tiktok_shop(texto_bruto.strip('"'))
        if not texto_limpo:
            raise ValueError("Resposta vazia.")
        return f'"{texto_limpo}"'

# 8 PROMPTS 100% UNIVERSAIS, SEM TEXTO FLUTUANTE, 11s CRAVADOS
def obter_identidade_original(i):
    prompts_universais = {
        1: (
            "Estilo 1: StyleFace GC Revelação",
            f"11s GC StyleFace universal showcase for any product, steady eye-level framing with immediate PT-BR hook at 0.0s, exact 1:1 product lock, grounded physical contact from 0.0s, zero floating, zero warping, zero blur, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        ),
        2: (
            "Estilo 2: UGC POV Plongée & Esticamento Tátil",
            f"11s first-person POV vertical 9:16 video in high-angle plongée and close detail perspective, natural hands handling and gently stretching the referenced product over a clean neutral surface with a quick gathering motion near the end, fluid camera following the action, soft natural lighting highlighting texture and elasticity, lively natural pacing, exact 1:1 product fidelity from 0.0s, grounded contact, zero floating, zero warping, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        ),
        3: (
            "Estilo 3: StyleFace GC Caimento",
            f"11s GC StyleFace universal fitting framing showing natural fit, drape, or placement of any product from 0.0s, PT-BR speech from 0.0s, calm camera, exact reference shape and texture, grounded contact, zero floating, zero stretching, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        ),
        4: (
            "Estilo 4: UGC POV Rotina Prática",
            f"11s UGC POV universal everyday routine shot demonstrating practical use of any product from 0.0s, PT-BR hook at 0.0s, natural movement, exact item dimensions and color, grounded contact, zero floating, zero warping, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        ),
        5: (
            "Estilo 5: StyleFace GC Sem Fala (Trilha Viral)",
            f"11s GC StyleFace universal silent visual rhythm for any product with zero dialogue, clean angle shifts showing true product form from 0.0s, steady motion, strict physical contact, zero floating, zero morphing, zero blur, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        ),
        6: (
            "Estilo 6: UGC POV Corpo Inteiro Urbano",
            f"11s UGC POV universal full-body street walk at an easy pace with any product anchored naturally from 0.0s, PT-BR speech from 0.0s, smooth tracking shot, locked product geometry, zero floating, zero warping, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        ),
        7: (
            "Estilo 7: UGC Criadora Natural Universal",
            f"11s natural vertical 9:16 video of a friendly creator presenting the referenced product spontaneously in bright natural light, transitioning smoothly to practical hands-on demonstration and a clean close-up of the finished product in use, continuous person and product fidelity from first to last frame, zero floating, zero warping, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        ),
        8: (
            "Estilo 8: StyleFace GC Pescoço Para Baixo (Fixo)",
            f"11s GC StyleFace fixed framing strictly from the neck down (no face shown), showcasing any product naturally from 0.0s, PT-BR hook at 0.0s, steady camera, exact 1:1 product lock, grounded physical contact, zero floating, zero warping, zero blur, {TRAVA_ANTI_TEXTO_FLUTUANTE}"
        )
    }
    return prompts_universais.get(i, (f"Estilo {i}", f"11s universal GC showcase {i} for any product, exact 1:1 product lock, grounded contact from 0.0s, zero floating, zero warping, {TRAVA_ANTI_TEXTO_FLUTUANTE}"))

# BANCO E CONFIG
DB_FILE = "moldes_salvos.json"
CONFIG_FILE = "config_ia.json"

def carregar_config():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    return {"api_key": str(data.get("api_key", ""))}
        except Exception:
            pass
    return {"api_key": ""}

def salvar_config(cfg):
    try:
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            json.dump(cfg, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def carregar_db():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                d = json.load(f)
                if isinstance(d, dict) and d:
                    return {int(k) if str(k).isdigit() else k: v for k, v in d.items()}
        except Exception:
            pass
    padrao = {i: dict(zip(["titulo", "prompt"], obter_identidade_original(i))) for i in range(1, 9)}
    salvar_db(padrao)
    return padrao

def salvar_db(db):
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

if "db_estilos" not in st.session_state:
    st.session_state.db_estilos = carregar_db()
if "config_ia" not in st.session_state:
    st.session_state.config_ia = carregar_config()
if "form_version" not in st.session_state:
    st.session_state.form_version = 0
if "acesso_liberado" not in st.session_state:
    st.session_state.acesso_liberado = False
if "historico_copys" not in st.session_state:
    st.session_state.historico_copys = set()
if "contador_takes" not in st.session_state:
    st.session_state.contador_takes = 0

def limpar_formulario():
    st.session_state.form_version += 1
    st.rerun()

v = st.session_state.form_version

# UI TOPO
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">LABORATÓRIOS VALENTINA</h1>
        <p class="hero-subtitle">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION (11s CRAVADOS)</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# PAINEL RÁPIDO
st.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>⚡ PAINEL DE CONTROLE RÁPIDO</p>", unsafe_allow_html=True)
c1, c2, c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.markdown("🎬 **DIRETOR SKIN**")
        skin_sel = st.selectbox("Skin", ["BOY (Elite Director)", "UGC LIFESTYLE"], label_visibility="collapsed", key=f"sel_skin_{v}")
with c2:
    with st.container(border=True):
        st.markdown("📱 **PROPORÇÃO**")
        prop_sel = st.selectbox("Proporção", ["9:16 (TikTok / Reels)", "1:1 (Feed)"], label_visibility="collapsed", key=f"sel_prop_{v}")
with c3:
    with st.container(border=True):
        st.markdown("🧠 **MOTOR DE COPY**")
        copy_mode_sel = st.selectbox("Motor Copy", ["IA Modeladora (Resumo Inteligente)", "Fixo (Do molde salvo)"], label_visibility="collapsed", key=f"sel_copy_mode_{v}")

with st.container(border=True):
    st.markdown("🎬 **SELECIONAR ESTILOS PARA GRADE DIÁRIA (MÁX. 8)**")
    chaves_ord = sorted(list(st.session_state.db_estilos.keys()), key=lambda x: (0, int(x)) if str(x).isdigit() else (1, str(x)))[:8]
    lista_titulos = [st.session_state.db_estilos[k]["titulo"] for k in chaves_ord]
    estilos_selecionados = st.multiselect("Selecione", options=lista_titulos, default=lista_titulos[:1] if lista_titulos else [], max_selections=8, label_visibility="collapsed", key=f"multi_estilos_{v}")

# ÁREA RESTRITA
with st.expander("⚙️ Gerenciar / Editar Prompts & Cérebro IA (Requer Senha)", expanded=False):
    col_s1, col_s2 = st.columns([3, 1])
    with col_s1:
        senha_dig = st.text_input("Senha", placeholder="Senha administrativa...", type="password", label_visibility="collapsed", key=f"pass_{v}")
    with col_s2:
        if st.button("🔓 VALIDAR", key=f"val_{v}"):
            st.session_state.acesso_liberado = (senha_dig == "vidalooka2")
            if st.session_state.acesso_liberado:
                st.success("✅ Liberado!")
            else:
                st.error("❌ Incorreta.")

    if st.session_state.acesso_liberado:
        st.markdown("<p style='color: #00FF66; font-weight: 700;'>🔓 MODO ADMINISTRADOR ATIVO</p>", unsafe_allow_html=True)
        with st.container(border=True):
            st.markdown("🧠 **API GEMINI**")
            k1, k2 = st.columns([3, 1])
            with k1:
                nova_key = st.text_input("Key", value=st.session_state.config_ia.get("api_key", ""), type="password", label_visibility="collapsed", key=f"key_{v}")
            with k2:
                if st.button("💾 SALVAR", key=f"save_k_{v}"):
                    st.session_state.config_ia["api_key"] = nova_key.strip()
                    salvar_config(st.session_state.config_ia)
                    st.success("Salvo!")
                    time.sleep(0.5)
                    st.rerun()

        if chaves_ord:
            slot_edit = st.selectbox("Estilo para Editar", options=chaves_ord, format_func=lambda x: f"Estilo {x} - {st.session_state.db_estilos[x]['titulo']}", key=f"edit_sel_{v}")
            t_edit = st.text_input("Título", value=st.session_state.db_estilos[slot_edit]["titulo"], key=f"t_edit_{slot_edit}_{v}")
            p_edit = st.text_area("Prompt Enxuto (Universal)", value=universalizar_prompt(st.session_state.db_estilos[slot_edit]["prompt"]), height=140, key=f"p_edit_{slot_edit}_{v}")
            if st.button("💾 SALVAR ALTERAÇÃO", key=f"btn_save_st_{slot_edit}_{v}"):
                st.session_state.db_estilos[slot_edit] = {"titulo": t_edit, "prompt": universalizar_prompt(p_edit)}
                salvar_db(st.session_state.db_estilos)
                st.success("Salvo com sucesso (universalizado)!")
                time.sleep(0.5)
                st.rerun()

# DADOS DO PRODUTO
st.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>📦 DADOS DO PRODUTO & DESCRIÇÃO TÉCNICA</p>", unsafe_allow_html=True)
with st.container(border=True):
    p_n1, p_n2 = st.columns(2)
    with p_n1:
        produto_nome = st.text_input("Nome", placeholder="Ex: Sandália, Relógio, Pantalona...", label_visibility="collapsed", key=f"nom_{v}")
    with p_n2:
        tipo_produto = st.selectbox("Categoria", ["Calçado", "Vestuário", "Acessório", "Bolsa", "Outros"], label_visibility="collapsed", key=f"cat_{v}")

    descricao_fornecedor = st.text_area("Descrição", placeholder="Cole a descrição completa do fornecedor aqui...", height=90, label_visibility="collapsed", key=f"desc_{v}")

    f1, f2, f3 = st.columns(3)
    with f1:
        foto_modelo = st.file_uploader("Modelo", type=["jpg", "png"], key=f"m_{v}", label_visibility="collapsed")
    with f2:
        foto_produto_analise = st.file_uploader("Produto", type=["jpg", "png"], key=f"p_{v}", label_visibility="collapsed")
    with f3:
        foto_peca = st.file_uploader("Zoom", type=["jpg", "png"], key=f"z_{v}", label_visibility="collapsed")

st.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)

col_e, btn_g, btn_l, col_d = st.columns([1, 2, 2, 1])
with btn_g:
    gerar_clicado = st.button("🚀 GERAR PROMPTS VIRAIS (11s)", key=f"gen_{v}")
with btn_l:
    st.button("🔄 LIMPAR", on_click=limpar_formulario, key=f"clr_{v}")

GRADE_HORARIOS = ["09:00", "11:00", "13:00", "15:00", "17:00", "19:00", "21:00", "23:00"]
VARIACOES_TOM = [
    "natural handheld angle",
    "soft side light shift",
    "subtle slow push-in",
    "relaxed everyday energy",
    "gentle pan follow",
    "clean front lighting",
    "calm outdoor breeze",
    "steady eye-level framing"
]

if gerar_clicado:
    if not produto_nome and not descricao_fornecedor:
        st.warning("⚠️ Informe o nome ou descrição.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Envie todas as fotos.")
    elif not estilos_selecionados:
        st.warning("⚠️ Selecione ao menos 1 estilo.")
    else:
        api_key = st.session_state.config_ia.get("api_key", "").strip()
        mapa_prompt = {st.session_state.db_estilos[i]["titulo"]: universalizar_prompt(st.session_state.db_estilos[i]["prompt"]) for i in chaves_ord}
        mapa_indice = {st.session_state.db_estilos[i]["titulo"]: i for i in chaves_ord}
        nome_exibicao = sanitizar_copy_tiktok_shop(produto_nome) or "Produto"
        proporcao_alvo = prop_sel.split(" ")[0]
        falas_usadas_lote = set()
        estilos_fala_usados_lote = set()

        with st.spinner("🔥 Disparando Motor Viral (11s cravados)..."):
            st.success(f"✅ Gerados {len(estilos_selecionados)} prompts universais de 11s para '{nome_exibicao}'.")
            for idx, est in enumerate(estilos_selecionados[:8]):
                st.session_state.contador_takes += 1
                take_num = st.session_state.contador_takes
                horario = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
                num_estilo = mapa_indice.get(est, idx + 1)
                estilo_fala_base = ESTILOS_FALA_POR_INDICE.get(num_estilo, "gancho_1_promocao_intensa_amigo")
                if estilo_fala_base in estilos_fala_usados_lote:
                    restantes = [v_f for v_f in ESTILOS_FALA_POR_INDICE.values() if v_f not in estilos_fala_usados_lote]
                    estilo_fala = restantes[0] if restantes else estilo_fala_base
                else:
                    estilo_fala = estilo_fala_base
                estilos_fala_usados_lote.add(estilo_fala)

                p_base = universalizar_prompt(mapa_prompt.get(est, ""))
                if proporcao_alvo != "9:16":
                    p_base = f"{p_base} Aspect: {proporcao_alvo}."

                is_mudo = "Sem Fala" in est or estilo_fala == "fala_visual_sem_audio"
                if not is_mudo:
                    var_tom = VARIACOES_TOM[(take_num - 1) % len(VARIACOES_TOM)]
                    p_base = f"{p_base} Skin: {skin_sel} | Take #{take_num}: {var_tom}."

                if is_mudo or ("Fixo" in copy_mode_sel and '"' in p_base):
                    final_prompt, display_copy = universalizar_prompt(p_base), "Fala fixa mantida."
                else:
                    fala = ""
                    if api_key:
                        try:
                            for _ in range(3):
                                candidata_ia = gerar_copy_ia_gemini(
                                    api_key, produto_nome, descricao_fornecedor, tipo_produto, est, estilo_fala, take_num, st.session_state.historico_copys, falas_usadas_lote
                                )
                                if candidata_ia not in st.session_state.historico_copys and candidata_ia not in falas_usadas_lote:
                                    fala = candidata_ia
                                    st.session_state.historico_copys.add(fala)
                                    falas_usadas_lote.add(fala)
                                    break
                        except Exception as err:
                            st.caption(f"⚠️ Falha na API Gemini ({err}); usando motor local.")
                    if not fala:
                        fala = resumir_e_modelar_copy_local(
                            produto_nome, descricao_fornecedor, tipo_produto, estilo_fala, st.session_state.historico_copys, falas_usadas_lote
                        )
                    fala = f'"{sanitizar_copy_tiktok_shop(fala.strip(chr(34)))}"'
                    st.session_state.historico_copys.add(fala)
                    falas_usadas_lote.add(fala)
                    display_copy = fala
                    final_prompt = f"{p_base}\n\n{fala}"

                st.markdown(f"### 🎬 Prompt {idx+1} • {horario}")
                st.markdown(
                    f'<div class="metric-card"><span class="tag-estilo">{est}</span><br>'
                    f'<span style="color:#00FF66; font-size:11px;">🔥 <b>Copy Viral (11s):</b> {display_copy}</span></div>',
                    unsafe_allow_html=True
                )
                st.code(final_prompt, language="text")
