import json
import os
import random
import re
import time
import urllib.request
import streamlit as st

st.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="centered"
)

# ESTÉTICA ORIGINAL MANTIDA
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');

    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #0b0914 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }

    .stButton>button, div[data-testid="stDownloadButton"]>button {
        background-color: #00FF66 !important;
        color: #000000 !important;
        font-weight: 700 !important;
        border-radius: 6px !important;
        border: none !important;
        padding: 6px 12px !important;
        font-size: 13px !important;
        width: 100% !important;
    }
    .stButton>button:hover, div[data-testid="stDownloadButton"]>button:hover {
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

REGRAS_LIMPEZA_TEXTO = [
    (r"\bkits?\b", "combinação"),
    (r"\bconjuntos?\b", "combinações"),
    (r"\bconjunto\b", "combinação"),
    (r"\bcombo\b", "opção"),
    (r"\bgarantia absoluta\b", "boa experiência"),
    (r"\bresultado garantido\b", "uso prático"),
    (r"\búltima unidade\b", "disponível no carrinho"),
    (r"\bestoque acabando\b", "alta procura"),
    (r"\bwhatsapp\b|\btelegram\b|\bshopee\b|\bmercado livre\b", "carrinho laranja"),
    (r"\bcara,\s*", "Amiga, "),
    (r"\bcara\b", "amiga"),
    (r"\bgarante o seu\b", "garante a sua"),
    (r"\bgarante!\b", "garante a sua!"),
    (r"\bvalentina\b", "")
]

SUBSTITUICOES_UNIVERSAIS = [
    (r"\bcanetas?\s+de\s+nail\s+art\b|\bnail\s+art\b|\bcanetas?\b", "o produto de referência"),
    (r"\bunhas?\s+decoradas?\b|\bunhas?\b|\bmesa\s+de\s+manicure\b", "o produto em uso real"),
    (r"\bcamisolas?\s+curtas?\s+de\s+cetim\s+brilhante\s+com\s+decote\s+em\s+renda\s+vermelha\s+e\s+al[çc]as\s+finas\s+sobre\s+mesa\s+de\s+m[áa]rmore\b", "o produto de referência"),
    (r"\bcamisolas?\b|\bcetim\s+brilhante\b|\brenda\s+vermelha\b|\bmesa\s+de\s+m[áa]rmore\b", "o produto selecionado"),
    (r"\btops?\s+de\s+diferentes\s+cores\s+sobre\s+um\s+len[çc]ol\s+branco\b", "o produto de referência sobre superfície clara e neutra"),
    (r"\blen[çc]ol\s+branco\b", "superfície clara e neutra"),
    (r"\bsand[áa]lias?\b|\bt[êe]nis\b|\bpantalonas?\b|\brel[óo]gios?\b", "o produto selecionado")
]

ESTILOS_FALA_POR_INDICE = {
    1: "gancho_1_promocao_intensa_amiga",
    2: "gancho_2_custo_beneficio_dor_amiga",
    3: "gancho_3_nao_espera_ficar_sem_amiga",
    4: "gancho_4_todo_mundo_comprando_amiga",
    5: "gancho_5_cara_de_luxo_preco_leve_amiga",
    6: "gancho_6_nem_precisava_mas_pegou_amiga",
    7: "fala_visual_sem_audio",
    8: "gancho_2_custo_beneficio_dor_amiga"
}

BLOCO_MESTRE_UNICO = (
    "strict 1:1 model and product lock (exact face, proportions, skin tone, hair; exact item shape, colorway, "
    "texture, stitching, hardware, strap/buckle count; zero added straps, buckles, logos, morphing, or floating; "
    "grounded contact; realistic hands and feet; natural UGC smartphone motion), zero floating text, no on-screen "
    "text, no captions, no subtitles, no UI overlays, no watermarks, no unrequested objects."
)

def _normalizar_espacos(texto):
    limpo = re.sub(r"\s+([,.!?;:])", r"\1", texto or "")
    return " ".join(limpo.split())

def sanitizar_copy_tiktok_shop(texto):
    limpo = texto or ""
    for padrao, substituto in REGRAS_LIMPEZA_TEXTO:
        limpo = re.sub(padrao, substituto, limpo, flags=re.IGNORECASE)
    return _normalizar_espacos(limpo)

def universalizar_prompt(texto):
    limpo = sanitizar_copy_tiktok_shop(texto)
    for padrao, substituto in SUBSTITUICOES_UNIVERSAIS:
        limpo = re.sub(padrao, substituto, limpo, flags=re.IGNORECASE)
    limpo = re.sub(r"\b(10|11|12)s\b", "11.5s", limpo, flags=re.IGNORECASE)
    if "no floating text" not in limpo.lower():
        limpo = f"{limpo} {BLOCO_MESTRE_UNICO}"
    return _normalizar_espacos(limpo)

def _fala_valida_11s(frase_sem_aspas):
    qtd = len([p for p in frase_sem_aspas.strip().split() if p])
    tem_cta = "carrinho laranja" in frase_sem_aspas.lower()
    tem_proibido = bool(re.search(r"\b(kits?|conjuntos?|combo|cara)\b", frase_sem_aspas, flags=re.IGNORECASE))
    return (21 <= qtd <= 32) and tem_cta and (not tem_proibido)

def _registrar_fala_unica(fala_crua, historico_sessao, falas_usadas_lote, validar_ritmo=True):
    limpa = sanitizar_copy_tiktok_shop(fala_crua.strip().strip('"'))
    if not limpa or (validar_ritmo and not _fala_valida_11s(limpa)):
        return None
    candidata = f'"{limpa}"'
    if candidata in historico_sessao or candidata in falas_usadas_lote:
        return None
    historico_sessao.add(candidata)
    falas_usadas_lote.add(candidata)
    return candidata

def _extrair_resumo_util(descricao_completa, categoria, beneficio_extra="", material_extra=""):
    extras = [sanitizar_copy_tiktok_shop(x).lower() for x in (beneficio_extra, material_extra) if sanitizar_copy_tiktok_shop(x)]
    if extras:
        return " e ".join(extras[:2])
    desc_limpa = sanitizar_copy_tiktok_shop(descricao_completa)
    if desc_limpa:
        trecho = re.split(r"[.!?\n]", desc_limpa)[0].strip()
        if trecho:
            return " ".join(trecho.split()[:6]).lower()
    cat_map = {
        "Calçado": "conforto real ao andar sem apertar",
        "Vestuário": "caimento leve que valoriza o corpo",
        "Acessório": "detalhes bem feitos que elevam o visual",
        "Bolsa": "espaço útil e praticidade no dia a dia",
        "Outros": "praticidade real na rotina diária"
    }
    return cat_map.get(categoria, "praticidade real na rotina diária")

# MOTOR LOCAL DE VENDA DIRETA (11.5s / 21 A 32 PALAVRAS)
def resumir_e_modelar_copy_local(nome_produto, descricao_completa, categoria, estilo_fala, historico_sessao, falas_usadas_lote, beneficio_extra="", material_extra=""):
    prod_bruto = sanitizar_copy_tiktok_shop(nome_produto)
    cat_bruta = sanitizar_copy_tiktok_shop(categoria).lower()
    item_fala = prod_bruto.strip() if prod_bruto else f"essa peça de {cat_bruta}"
    detalhe_real = _extrair_resumo_util(descricao_completa, categoria, beneficio_extra, material_extra)

    banco_por_estilo = {
        "gancho_1_promocao_intensa_amiga": [
            f"Amiga, essa oferta tá chamando atenção porque ninguém aguenta mais {cat_bruta} ruim! {item_fala.capitalize()} entrega {detalhe_real}. Garante a sua no carrinho laranja agora!",
            f"Meninas, essa condição tá disputada porque resolve a dor de errar em {cat_bruta}! {item_fala.capitalize()} traz {detalhe_real}. Corre no carrinho laranja!"
        ],
        "gancho_2_custo_beneficio_dor_amiga": [
            f"Amiga, pelo preço que tá vale aproveitar antes de mudar! Chega de gastar com {cat_bruta} desconfortável: {item_fala} entrega {detalhe_real}. Clica no carrinho laranja!",
            f"Gente, o custo-benefício compensa demais pra quem cansou de {cat_bruta} fraco! {item_fala.capitalize()} tem {detalhe_real}. Pega a sua no carrinho laranja!"
        ],
        "gancho_3_nao_espera_ficar_sem_amiga": [
            f"Amiga, se deixar pra depois, pode ficar sem na hora que mais precisar! {item_fala.capitalize()} resolve o incômodo com {detalhe_real}. Garante no carrinho laranja!",
            f"Meninas, quem deixa pra depois acaba perdendo condição boa! {item_fala.capitalize()} entrega {detalhe_real} no dia a dia. Não deixa passar no carrinho laranja!"
        ],
        "gancho_4_todo_mundo_comprando_amiga": [
            f"Amiga, todo mundo tá pegando porque resolve um problema real! Se você cansou de {cat_bruta} sem graça, {item_fala} entrega {detalhe_real}. Vê no carrinho laranja!",
            f"Gente, tá todo mundo buscando opção que funcione de verdade! {item_fala.capitalize()} traz {detalhe_real} sem complicação. Aproveita agora no carrinho laranja!"
        ],
        "gancho_5_cara_de_luxo_preco_leve_amiga": [
            f"Amiga, tem cara de item caro, mas sem pesar no bolso! Ideal pra fugir de {cat_bruta} mal feito: {item_fala} entrega {detalhe_real}. Clica no carrinho laranja!",
            f"Meninas, o visual chama atenção e o preço cabe na rotina! {item_fala.capitalize()} tem {detalhe_real} de verdade. Garante já no carrinho laranja!"
        ],
        "gancho_6_nem_precisava_mas_pegou_amiga": [
            f"Amiga, eu nem tava pensando em pegar agora, mas quando vi o benefício quis mostrar! {item_fala.capitalize()} entrega {detalhe_real}. Confere no carrinho laranja!",
            f"Gente, às vezes a gente só descobre o achado certo na hora! {item_fala.capitalize()} traz {detalhe_real} pro seu dia. Pega já no carrinho laranja!"
        ],
        "fala_visual_sem_audio": [
            f"Amiga, olha como {item_fala} funciona na prática sem enrolação! Entrega {detalhe_real} no dia a dia. Clica no carrinho laranja e garante a sua!"
        ]
    }

    opcoes = list(banco_por_estilo.get(estilo_fala, banco_por_estilo["gancho_1_promocao_intensa_amiga"]))
    random.shuffle(opcoes)

    for validar in (True, False):
        for raw in opcoes:
            registrada = _registrar_fala_unica(raw, historico_sessao, falas_usadas_lote, validar_ritmo=validar)
            if registrada:
                return registrada

    fallback = f'"{sanitizar_copy_tiktok_shop(opcoes[0])}"'
    historico_sessao.add(fallback)
    falas_usadas_lote.add(fallback)
    return fallback

def gerar_copy_ia_gemini(api_key, nome_produto, descricao_completa, categoria, estilo_titulo, estilo_fala, variacao_num, historico_sessao, falas_usadas_lote, beneficio_extra="", material_extra="", ref_internacional=""):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key.strip()}"
    bloqueadas = list(historico_sessao)[-6:] + list(falas_usadas_lote)
    evitar_txt = f" NÃO repita nenhuma destas falas: {' | '.join(bloqueadas[-8:])}." if bloqueadas else ""

    instrucao_sistema = (
        "Você escreve falas de venda para TikTok Shop Brasil em tom feminino de amiga para amiga "
        "('Amiga...', 'Meninas...', 'Gente...'), aplicando inteligência de tendências, ganchos de retenção "
        "e estrutura de vídeo curto internacional adaptada com naturalidade ao português do Brasil. "
        "Duração: 11.5 segundos cravados (24 a 29 palavras), com começo (dor real), meio (produto e "
        "benefício prático) e fim (CTA direto chamando para o 'carrinho laranja'). "
        "NUNCA use nomes próprios, 'cara' ou concordância masculina. "
        f"Gancho: '{estilo_fala}'. "
        "NUNCA use 'kit', 'kits', 'conjunto', 'conjuntos', 'combo', promessas absolutas "
        "ou plataformas externas. Retorne APENAS a fala entre aspas duplas."
        f"{evitar_txt}"
    )
    info_extra = (
        f"Benefício: {sanitizar_copy_tiktok_shop(beneficio_extra)} | "
        f"Material: {sanitizar_copy_tiktok_shop(material_extra)} | "
        f"Pesquisa/Tendência Internacional: {sanitizar_copy_tiktok_shop(ref_internacional) or 'padrão global de retenção e demonstração visual adaptado ao Brasil'} | "
    )
    payload = {
        "contents": [{
            "parts": [{
                "text": (
                    f"{instrucao_sistema}\n"
                    f"Produto: {sanitizar_copy_tiktok_shop(nome_produto)} | Categoria: {sanitizar_copy_tiktok_shop(categoria)} | "
                    f"{info_extra}Estilo: {estilo_titulo} | Var #{variacao_num}\n"
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
            raise ValueError("Sem retorno da IA.")
        partes = ((candidates[0].get("content") or {}).get("parts")) or []
        texto_bruto = ((partes[0].get("text") if partes else "") or "").strip().replace("\n", " ")
        registrada = _registrar_fala_unica(texto_bruto, historico_sessao, falas_usadas_lote, validar_ritmo=True)
        if not registrada:
            raise ValueError("Fala fora do padrão de tempo ou repetida.")
        return registrada

# 8 PROMPTS ENXUTOS E UNIVERSAIS (11.5s CRAVADOS)
def obter_identidade_original(i):
    prompts_universais = {
        1: ("Estilo 1: StyleFace GC Revelação", f"11.5s GC StyleFace showcase at eye level with immediate female PT-BR hook at 0.0s, {BLOCO_MESTRE_UNICO}"),
        2: ("Estilo 2: UGC POV Plongée & Esticamento Tátil", f"11.5s first-person POV vertical video in high-angle plongée and detail view, female hands gently stretching the item on a neutral surface with a quick gather at the end, natural light highlighting texture and stretch, {BLOCO_MESTRE_UNICO}"),
        3: ("Estilo 3: StyleFace GC Caimento", f"11.5s GC StyleFace fitting framing showing natural fit and drape from 0.0s with female PT-BR speech, calm camera, {BLOCO_MESTRE_UNICO}"),
        4: ("Estilo 4: UGC POV Rotina Prática", f"11.5s UGC POV everyday routine shot showing practical use from 0.0s with female PT-BR hook, natural movement, {BLOCO_MESTRE_UNICO}"),
        5: ("Estilo 5: StyleFace GC Sem Fala (Trilha Viral)", f"11.5s GC StyleFace silent visual rhythm with zero dialogue, clean angle shifts showing true product form from 0.0s, {BLOCO_MESTRE_UNICO}"),
        6: ("Estilo 6: UGC POV Corpo Inteiro Urbano", f"11.5s UGC POV full-body street walk at an easy pace with item anchored naturally from 0.0s and female PT-BR speech, smooth tracking, {BLOCO_MESTRE_UNICO}"),
        7: ("Estilo 7: UGC Criadora Natural Universal", f"11.5s natural vertical video of a friendly female creator presenting the item in daylight, moving into hands-on use and a clean close-up of the result, continuous fidelity from first to last frame, {BLOCO_MESTRE_UNICO}"),
        8: ("Estilo 8: StyleFace GC Pescoço Para Baixo (Fixo)", f"11.5s GC StyleFace fixed framing strictly from neck down (no face shown), showcasing the item naturally from 0.0s with female PT-BR hook, steady camera, {BLOCO_MESTRE_UNICO}")
    }
    return prompts_universais.get(i, (f"Estilo {i}", f"11.5s universal GC showcase {i}, {BLOCO_MESTRE_UNICO}"))

DB_FILE = "moldes_salvos.json"
CONFIG_FILE = "config_ia.json"

def carregar_json(caminho, padrao):
    if os.path.exists(caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data:
                    return data
        except Exception:
            pass
    return padrao

def salvar_json(caminho, dados):
    try:
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

def carregar_config():
    data = carregar_json(CONFIG_FILE, {})
    return {"api_key": str(data.get("api_key", ""))} if isinstance(data, dict) else {"api_key": ""}

def carregar_db():
    d = carregar_json(DB_FILE, {})
    if isinstance(d, dict) and d:
        return {int(k) if str(k).isdigit() else k: v for k, v in d.items()}
    padrao = {i: dict(zip(["titulo", "prompt"], obter_identidade_original(i))) for i in range(1, 9)}
    salvar_json(DB_FILE, padrao)
    return padrao

for chave, padrao in [
    ("db_estilos", None),
    ("config_ia", None),
    ("form_version", 0),
    ("acesso_liberado", False),
    ("historico_copys", set()),
    ("contador_takes", 0),
    ("ultimo_lote_txt", "")
]:
    if chave not in st.session_state:
        if chave == "db_estilos":
            st.session_state[chave] = carregar_db()
        elif chave == "config_ia":
            st.session_state[chave] = carregar_config()
        else:
            st.session_state[chave] = padrao

def limpar_formulario():
    st.session_state.form_version += 1
    st.rerun()

v = st.session_state.form_version

st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">LABORATÓRIOS VALENTINA</h1>
        <p class="hero-subtitle">TIKTOK SHOP AUTOMATION • 11.5s CRAVADOS</p>
    </div>
""", unsafe_allow_html=True)

st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

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
        copy_mode_sel = st.selectbox("Motor Copy", ["IA Modeladora (Resumo Inteligente)", "Fixo (Do molde salvo)", "Sem Fala (Visual Puro)"], label_visibility="collapsed", key=f"sel_copy_mode_{v}")

with st.container(border=True):
    st.markdown("🎬 **SELECIONAR ESTILOS PARA GRADE DIÁRIA (MÁX. 8)**")
    chaves_ord = sorted(list(st.session_state.db_estilos.keys()), key=lambda x: (0, int(x)) if str(x).isdigit() else (1, str(x)))[:8]
    lista_titulos = [st.session_state.db_estilos[k]["titulo"] for k in chaves_ord]
    estilos_selecionados = st.multiselect("Selecione", options=lista_titulos, default=lista_titulos[:1] if lista_titulos else [], max_selections=8, label_visibility="collapsed", key=f"multi_estilos_{v}")

with st.expander("⚙️ Gerenciar / Editar Prompts & Cérebro IA (Requer Senha)", expanded=False):
    col_s1, col_s2 = st.columns([3, 1])
    with col_s1:
        senha_dig = st.text_input("Senha", placeholder="Senha administrativa...", type="password", label_visibility="collapsed", key=f"pass_{v}")
    with col_s2:
        if st.button("🔓 VALIDAR", key=f"val_{v}"):
            st.session_state.acesso_liberado = (senha_dig == "vidalooka2")
            st.success("✅ Liberado!") if st.session_state.acesso_liberado else st.error("❌ Incorreta.")

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
                    salvar_json(CONFIG_FILE, st.session_state.config_ia)
                    st.success("Salvo!")
                    time.sleep(0.5)
                    st.rerun()

        if chaves_ord:
            slot_edit = st.selectbox("Estilo para Editar", options=chaves_ord, format_func=lambda x: f"Estilo {x} - {st.session_state.db_estilos[x]['titulo']}", key=f"edit_sel_{v}")
            t_edit = st.text_input("Título", value=st.session_state.db_estilos[slot_edit]["titulo"], key=f"t_edit_{slot_edit}_{v}")
            p_edit = st.text_area("Prompt Enxuto (Universal)", value=universalizar_prompt(st.session_state.db_estilos[slot_edit]["prompt"]), height=140, key=f"p_edit_{slot_edit}_{v}")
            if st.button("💾 SALVAR ALTERAÇÃO", key=f"btn_save_st_{slot_edit}_{v}"):
                st.session_state.db_estilos[slot_edit] = {"titulo": t_edit, "prompt": universalizar_prompt(p_edit)}
                salvar_json(DB_FILE, st.session_state.db_estilos)
                st.success("Salvo com sucesso!")
                time.sleep(0.5)
                st.rerun()

st.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>📦 DADOS DO PRODUTO & DESCRIÇÃO TÉCNICA</p>", unsafe_allow_html=True)
with st.container(border=True):
    p_n1, p_n2 = st.columns(2)
    with p_n1:
        produto_nome = st.text_input("Nome", placeholder="Ex: Sandália, Relógio, Pantalona...", label_visibility="collapsed", key=f"nom_{v}")
    with p_n2:
        tipo_produto = st.selectbox("Categoria", ["Calçado", "Vestuário", "Acessório", "Bolsa", "Outros"], label_visibility="collapsed", key=f"cat_{v}")

    b_n1, b_n2 = st.columns(2)
    with b_n1:
        beneficio_prod = st.text_input("Benefício", placeholder="Opcional: benefício principal (ex: não aperta)...", label_visibility="collapsed", key=f"ben_{v}")
    with b_n2:
        material_prod = st.text_input("Material", placeholder="Opcional: material/textura (ex: malha macia)...", label_visibility="collapsed", key=f"mat_{v}")

    ref_internacional = st.text_input("Tendência Internacional", placeholder="Opcional: gancho ou pesquisa internacional para adaptar ao Brasil...", label_visibility="collapsed", key=f"ref_intl_{v}")
    descricao_fornecedor = st.text_area("Descrição", placeholder="Cole a descrição completa do fornecedor aqui...", height=85, label_visibility="collapsed", key=f"desc_{v}")

st.markdown("<div style='margin: 8px 0;'></div>", unsafe_allow_html=True)

col_e, btn_g, btn_l, btn_h, col_d = st.columns([0.5, 2, 1.5, 1.5, 0.5])
with btn_g:
    gerar_clicado = st.button("🚀 GERAR PROMPTS VIRAIS (11.5s)", key=f"gen_{v}")
with btn_l:
    st.button("🔄 LIMPAR", on_click=limpar_formulario, key=f"clr_{v}")
with btn_h:
    if st.button("🧹 ZERAR FALAS", key=f"rst_hist_{v}"):
        st.session_state.historico_copys = set()
        st.toast("Histórico de falas limpo!")

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
        st.warning("⚠️ Informe o nome ou descrição do produto.")
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
        blocos_exportacao = []
        todos_ganchos = list(ESTILOS_FALA_POR_INDICE.values())

        with st.spinner("🔥 Disparando Motor Viral (11.5s cravados)..."):
            st.success(f"✅ Gerados {len(estilos_selecionados)} prompts de 11.5s para '{nome_exibicao}'.")
            for idx, est in enumerate(estilos_selecionados[:8]):
                st.session_state.contador_takes += 1
                take_num = st.session_state.contador_takes
                horario = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
                num_estilo = mapa_indice.get(est, idx + 1)

                gancho_alvo = ESTILOS_FALA_POR_INDICE.get(num_estilo, "gancho_1_promocao_intensa_amiga")
                if gancho_alvo in estilos_fala_usados_lote:
                    gancho_alvo = next((g for g in todos_ganchos if g not in estilos_fala_usados_lote), gancho_alvo)
                estilos_fala_usados_lote.add(gancho_alvo)

                p_base = mapa_prompt.get(est, "")
                if proporcao_alvo != "9:16":
                    p_base = f"{p_base} Aspect: {proporcao_alvo}."

                is_mudo = ("Sem Fala" in est) or ("Sem Fala" in copy_mode_sel) or (gancho_alvo == "fala_visual_sem_audio")
                if is_mudo:
                    final_prompt = universalizar_prompt(f"{p_base} Silent visual only, no speech, no voice-over, no music.")
                    display_copy = "Modo visual / fala fixa."
                else:
                    var_tom = VARIACOES_TOM[(take_num - 1) % len(VARIACOES_TOM)]
                    p_base = universalizar_prompt(f"{p_base} Skin: {skin_sel} | Take #{take_num}: {var_tom}.")
                    if "Fixo" in copy_mode_sel and '"' in p_base:
                        final_prompt, display_copy = p_base, "Modo visual / fala fixa."
                    else:
                        fala = ""
                        if api_key:
                            try:
                                for _ in range(3):
                                    fala = gerar_copy_ia_gemini(
                                        api_key, produto_nome, descricao_fornecedor, tipo_produto, est,
                                        gancho_alvo, take_num, st.session_state.historico_copys, falas_usadas_lote,
                                        beneficio_prod, material_prod, ref_internacional
                                    )
                                    if fala:
                                        break
                            except Exception:
                                st.caption("⚠️ Conexão com a IA indisponível no momento; usando motor local automaticamente.")
                        if not fala:
                            fala = resumir_e_modelar_copy_local(
                                produto_nome, descricao_fornecedor, tipo_produto, gancho_alvo,
                                st.session_state.historico_copys, falas_usadas_lote,
                                beneficio_prod, material_prod
                            )
                        display_copy = fala
                        final_prompt = f"{p_base}\n\n{fala}"

                blocos_exportacao.append(f"=== PROMPT {idx+1} • {horario} • {est} ===\nCopy: {display_copy}\n\n{final_prompt}\n")

                st.markdown(f"### 🎬 Prompt {idx+1} • {horario}")
                st.markdown(
                    f'<div class="metric-card"><span class="tag-estilo">{est}</span><br>'
                    f'<span style="color:#00FF66; font-size:11px;">🔥 <b>Copy Viral (11.5s):</b> {display_copy}</span></div>',
                    unsafe_allow_html=True
                )
                st.code(final_prompt, language="text")

        st.session_state.ultimo_lote_txt = "\n".join(blocos_exportacao)

if st.session_state.ultimo_lote_txt:
    st.download_button(
        label="📥 BAIXAR LOTE COMPLETO (.TXT)",
        data=st.session_state.ultimo_lote_txt,
        file_name="prompts_tiktok_shop_11_5s.txt",
        mime="text/plain",
        key=f"dl_{v}"
    )
