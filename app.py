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
    (r"\bsand[áa]lias?\b|\bt[êe]nis\b|\bpantalonas?\b|\bcamisolas?\b|\brel[óo]gios?\b", "o produto selecionado")
]

ESTILOS_FALA_POR_INDICE = {
    1: "fala_styleface_revelacao",
    2: "fala_ugc_pov_mao",
    3: "fala_styleface_caimento",
    4: "fala_ugc_pov_rotina",
    5: "fala_styleface_sem_fala",
    6: "fala_ugc_pov_rua",
    7: "fala_ugc_3cenas_universal",
    8: "fala_styleface_pescoco_baixo_fixo"
}

def sanitizar_copy_tiktok_shop(texto):
    limpo = texto or ""
    for padrao, substituto in SUBSTITUICOES_COMPLIANCE:
        limpo = re.sub(padrao, substituto, limpo, flags=re.IGNORECASE)
    return " ".join(limpo.split())

def universalizar_prompt(texto):
    limpo = sanitizar_copy_tiktok_shop(texto)
    for padrao, substituto in SUBSTITUICOES_UNIVERSAIS:
        limpo = re.sub(padrao, substituto, limpo, flags=re.IGNORECASE)
    return " ".join(limpo.split())

def _contar_palavras_reais(texto_sem_aspas):
    return len([p for p in texto_sem_aspas.strip().split() if p])

# MOTOR LOCAL UNIVERSAL COM ESTILO DE FALA DISTINTO POR ESTILO (12s CRAVADOS / 24 A 34 PALAVRAS)
def resumir_e_modelar_copy_local(nome_produto, descricao_completa, categoria, estilo_fala, historico_sessao, falas_usadas_lote):
    prod_bruto = sanitizar_copy_tiktok_shop(nome_produto)
    cat_bruta = sanitizar_copy_tiktok_shop(categoria).lower()
    prod_limpo = prod_bruto if prod_bruto else f"esse item de {cat_bruta}"
    prod_curto = " ".join(prod_limpo.split()[:3])

    banco_por_estilo = {
        "fala_styleface_revelacao": [
            f"Olha como esse {prod_curto} resolve já no primeiro segundo do vídeo! Entrega da Loja da Valentina com conforto real no dia a dia: clica aqui embaixo no carrinho laranja e garante o seu!",
            f"Logo no primeiro segundo dá pra ver o diferencial desse {prod_curto}! Peça da Loja da Valentina com ótimo encaixe: clica aqui embaixo no carrinho laranja e garante o seu!"
        ],
        "fala_ugc_pov_mao": [
            f"POV: pegando esse {prod_curto} na mão agora e já vendo a firmeza! Achado da Loja da Valentina feito pro dia a dia: dá uma olhada no carrinho laranja aqui embaixo!",
            f"POV: testando esse {prod_curto} de perto na rotina de hoje! Qualidade da Loja da Valentina sem complicação: abre o carrinho laranja aqui embaixo e pega o seu!"
        ],
        "fala_styleface_caimento": [
            f"Repara no caimento real desse {prod_curto} quando o corpo se movimenta! Estilo da Loja da Valentina super confortável: clica aqui embaixo no carrinho laranja e garante o seu!",
            f"Veja como esse {prod_curto} assenta bem sem repuxar na rotina! Peça da Loja da Valentina com acabamento firme: dá uma olhada no carrinho laranja aqui embaixo!"
        ],
        "fala_ugc_pov_rotina": [
            f"POV: finalmente achei um {prod_curto} prático de verdade pra minha rotina diária! Facilidade da Loja da Valentina que ajuda todo dia: abre o carrinho laranja aqui embaixo e pega o seu!",
            f"POV: encaixando esse {prod_curto} na correria do dia sem perder tempo! Solução da Loja da Valentina simples e funcional: clica aqui embaixo no carrinho laranja e garante o seu!"
        ],
        "fala_styleface_sem_fala": [
            f"Sem falar muito, esse {prod_curto} já mostra tudo no visual do take! Linha da Loja da Valentina pensada pro dia a dia: dá uma olhada no carrinho laranja aqui embaixo!"
        ],
        "fala_ugc_pov_rua": [
            f"POV: andando na rua com {prod_curto} e sentindo a leveza no passo! Qualidade da Loja da Valentina feita pra acompanhar o dia: abre o carrinho laranja aqui embaixo e pega o seu!",
            f"POV: saindo pro dia a dia com {prod_curto} bem firme e confortável! Achado da Loja da Valentina super prático: clica aqui embaixo no carrinho laranja e garante o seu!"
        ],
        "fala_ugc_3cenas_universal": [
            f"Olha como esse {prod_curto} funciona na prática e entrega resultado limpo! Achado da Loja da Valentina com acabamento caprichado: clica aqui embaixo no carrinho laranja e garante o seu!",
            f"Do primeiro olhar ao uso real, esse {prod_curto} surpreende no detalhe! Qualidade da Loja da Valentina pro dia a dia: abre o carrinho laranja aqui embaixo e pega o seu!"
        ],
        "fala_styleface_pescoco_baixo_fixo": [
            f"Olha como esse {prod_curto} fica no corpo do pescoço pra baixo com caimento limpo! Loja da Valentina na prática: clica aqui embaixo no carrinho laranja e garante o seu!",
            f"Veja o encaixe real desse {prod_curto} do pescoço pra baixo sem perder a forma! Achado da Loja da Valentina: dá uma olhada no carrinho laranja aqui embaixo!"
        ]
    }

    opcoes = list(banco_por_estilo.get(estilo_fala, banco_por_estilo["fala_styleface_revelacao"]))
    random.shuffle(opcoes)

    for raw in opcoes:
        frase = sanitizar_copy_tiktok_shop(raw)
        qtd = _contar_palavras_reais(frase)
        candidata = f'"{frase}"'
        if 24 <= qtd <= 34 and candidata not in historico_sessao and candidata not in falas_usadas_lote:
            historico_sessao.add(candidata)
            falas_usadas_lote.add(candidata)
            return candidata

    for raw in opcoes:
        frase = sanitizar_copy_tiktok_shop(f"{raw} ({cat_bruta})")
        candidata = f'"{frase}"'
        if candidata not in historico_sessao and candidata not in falas_usadas_lote:
            historico_sessao.add(candidata)
            falas_usadas_lote.add(candidata)
            return candidata

    base_fallback = sanitizar_copy_tiktok_shop(opcoes[0])
    fallback = f'"{base_fallback}"'
    historico_sessao.add(fallback)
    falas_usadas_lote.add(fallback)
    return fallback

def gerar_copy_ia_gemini(api_key, nome_produto, descricao_completa, categoria, estilo_titulo, estilo_fala, variacao_num, historico_sessao, falas_usadas_lote):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key.strip()}"
    bloqueadas = list(historico_sessao)[-6:] + list(falas_usadas_lote)
    evitar_txt = f" NÃO repita nenhuma destas falas: {' | '.join(bloqueadas[-8:])}." if bloqueadas else ""

    instrucao_sistema = (
        f"Diretor de criação TikTok Shop Brasil. Escreva uma fala espontânea de 12 segundos cravados (26 a 32 palavras) "
        f"adaptada de forma universal ao produto informado, com o estilo de fala exclusivo '{estilo_fala}'. "
        "NUNCA use as palavras 'kit', 'kits', 'conjunto', 'conjuntos', 'combo', promessas absolutas "
        "ou menções a plataformas externas. "
        "Inclua 'Loja da Valentina' e chame para o 'carrinho laranja'. Retorne APENAS a fala entre aspas duplas."
        f"{evitar_txt}"
    )
    payload = {
        "contents": [{
            "parts": [{
                "text": (
                    f"{instrucao_sistema}\n"
                    f"Produto: {sanitizar_copy_tiktok_shop(nome_produto)} | Categoria: {sanitizar_copy_tiktok_shop(categoria)} | "
                    f"Estilo: {estilo_titulo} | Estilo de Fala: {estilo_fala} | Var #{variacao_num}\n"
                    f"Detalhes: {sanitizar_copy_tiktok_shop(descricao_completa)}"
                )
            }]
        }],
        "generationConfig": {"temperature": 1.0, "maxOutputTokens": 105}
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

# 8 PROMPTS 100% UNIVERSAIS (QUALQUER PRODUTO, ALTERNANDO STYLEFACE E UGC POV; ESTILO 8 FIXO DO PESCOÇO PARA BAIXO; 12s CRAVADOS)
def obter_identidade_original(i):
    prompts_universais = {
        1: (
            "Estilo 1: StyleFace GC Revelação",
            "12s GC StyleFace universal showcase for any product, steady eye-level framing with immediate PT-BR hook at 0.0s, exact 1:1 product lock, grounded physical contact from 0.0s, zero floating, zero warping, zero blur, no text overlays, no watermarks, no third-party logos, no mics."
        ),
        2: (
            "Estilo 2: UGC POV Mão & Revelação",
            "12s UGC POV universal hands holding and presenting any product firmly from 0.0s, immediate PT-BR hook at 0.0s, natural handheld motion, faithful proportions, grounded contact, zero floating, zero distortion, no text overlays, no watermarks, no logos, no mics."
        ),
        3: (
            "Estilo 3: StyleFace GC Caimento",
            "12s GC StyleFace universal fitting framing showing natural fit, drape, or placement of any product from 0.0s, PT-BR speech from 0.0s, calm camera, exact reference shape and texture, grounded contact, zero floating, zero stretching, no text overlays, no watermarks, no mics."
        ),
        4: (
            "Estilo 4: UGC POV Rotina Prática",
            "12s UGC POV universal everyday routine shot demonstrating practical use of any product from 0.0s, PT-BR hook at 0.0s, natural movement, exact item dimensions and color, grounded contact, zero floating, zero warping, no text overlays, no watermarks, no mics."
        ),
        5: (
            "Estilo 5: StyleFace GC Sem Fala (Trilha Viral)",
            "12s GC StyleFace universal silent visual rhythm for any product with zero dialogue, clean angle shifts showing true product form from 0.0s, steady motion, strict physical contact, zero floating, zero morphing, zero blur, no text overlays, no watermarks, no mics."
        ),
        6: (
            "Estilo 6: UGC POV Corpo Inteiro Urbano",
            "12s UGC POV universal full-body street walk at an easy pace with any product anchored naturally from 0.0s, PT-BR speech from 0.0s, smooth tracking shot, locked product geometry, zero floating, zero warping, no text overlays, no watermarks, no mics."
        ),
        7: (
            "Estilo 7: UGC 3 Cenas Universal",
            "Estilo comercial UGC universal de criadora de conteúdo para qualquer produto, formato vertical 9:16, duração de 12s, iluminação natural e acabamento limpo. CENA 1 – ABERTURA E GANCHO: Criadora simpática apresenta o produto de referência de forma espontânea olhando para a câmera com gancho imediato em português brasileiro. CENA 2 – DEMONSTRAÇÃO NA PRÁTICA: Transição suave mostrando o produto em uso real e prático no dia a dia, preservando forma e detalhes. CENA 3 – RESULTADO: Close limpo e realista do produto e do resultado final. Sem legendas ou textos na tela."
        ),
        8: (
            "Estilo 8: StyleFace GC Pescoço Para Baixo (Fixo)",
            "12s GC StyleFace fixed framing strictly from the neck down (no face shown), showcasing any product naturally from 0.0s, PT-BR hook at 0.0s, steady camera, exact 1:1 product lock, grounded physical contact, zero floating, zero warping, zero blur, no text overlays, no watermarks, no third-party logos, no mics."
        )
    }
    return prompts_universais.get(i, (f"Estilo {i}", f"12s universal GC showcase {i} for any product, exact 1:1 product lock, grounded contact from 0.0s, zero floating, zero warping, no text overlays, no watermarks, no mics."))

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
        <p class="hero-subtitle">LOJA DA VALENTINA • TIKTOK SHOP AUTOMATION (12s CRAVADOS)</p>
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
    gerar_clicado = st.button("🚀 GERAR PROMPTS VIRAIS (12s)", key=f"gen_{v}")
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

        with st.spinner("🔥 Disparando Motor Viral (12s cravados)..."):
            st.success(f"✅ Gerados {len(estilos_selecionados)} prompts universais para '{nome_exibicao}'.")
            for idx, est in enumerate(estilos_selecionados[:8]):
                st.session_state.contador_takes += 1
                take_num = st.session_state.contador_takes
                horario = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
                num_estilo = mapa_indice.get(est, idx + 1)
                estilo_fala_base = ESTILOS_FALA_POR_INDICE.get(num_estilo, "fala_styleface_revelacao")
                if estilo_fala_base in estilos_fala_usados_lote:
                    restantes = [v_f for v_f in ESTILOS_FALA_POR_INDICE.values() if v_f not in estilos_fala_usados_lote]
                    estilo_fala = restantes[0] if restantes else estilo_fala_base
                else:
                    estilo_fala = estilo_fala_base
                estilos_fala_usados_lote.add(estilo_fala)

                p_base = universalizar_prompt(mapa_prompt.get(est, ""))
                if proporcao_alvo != "9:16":
                    p_base = f"{p_base} Aspect: {proporcao_alvo}."

                is_mudo = "Sem Fala" in est or estilo_fala == "fala_styleface_sem_fala"
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
                    f'<span style="color:#00FF66; font-size:11px;">🔥 <b>Copy Viral (12s):</b> {display_copy}</span></div>',
                    unsafe_allow_html=True
                )
                st.code(final_prompt, language="text")
