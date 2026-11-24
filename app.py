import json
import os
import random
import urllib.request
import urllib.error
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

def _contar_palavras_reais(texto_sem_aspas):
    return len([p for p in texto_sem_aspas.strip().split() if p])

# MOTOR LOCAL COM OS 10 GANCHOS EM TOM ESPONTÂNEO (11s / 22 A 28 PALAVRAS)
def resumir_e_modelar_copy_local(nome_produto, descricao_completa, categoria, historico_sessao):
    prod_limpo = nome_produto.strip() if nome_produto and nome_produto.strip() else f"esse {categoria.lower()}"
    prod_curto = " ".join(prod_limpo.split()[:3])
    cat = categoria.lower()

    ganchos_espontaneos = [
        f"Olha como esse {prod_curto} resolve já no primeiro segundo!",
        "Espera eu virar a câmera pra você ver como isso assenta!",
        f"Se você pega {cat} na correria, dá uma olhada nisso aqui!",
        f"Achei que precisava gastar bem mais, mas esse {prod_curto} surpreendeu!",
        f"Antes de pegar qualquer {prod_curto}, repare nesse detalhe de perto!",
        f"Depois de testar 7 opções, esse {prod_curto} foi o único que ficou!",
        f"A diferença na rotina de usar {prod_curto} é bem nítida!",
        f"POV: finalmente achei um {prod_curto} prático de verdade no dia a dia!",
        f"Queria ter visto isso antes de gastar dinheiro com {cat}!",
        "Peguei na promoção agora e já vi que vai sair rápido!"
    ]

    corpo_necessidade = [
        "Conforto real da Loja da Valentina sem pesar no bolso.",
        "Acabamento firme da Loja da Valentina que funciona na prática.",
        "Achado da Loja da Valentina que facilita o uso diário."
    ]

    fechamentos_cta = [
        "Clica aqui embaixo no carrinho laranja e garante o seu!",
        "Dá uma olhada no carrinho laranja aqui embaixo antes que acabe!",
        "Abre o carrinho laranja aqui embaixo e pega o seu!"
    ]

    for _ in range(180):
        g = random.choice(ganchos_espontaneos)
        d = random.choice(corpo_necessidade)
        c = random.choice(fechamentos_cta)
        frase = " ".join(f"{g} {d} {c}".split())
        qtd = _contar_palavras_reais(frase)
        candidata = f'"{frase}"'
        if 22 <= qtd <= 28 and candidata not in historico_sessao:
            historico_sessao.add(candidata)
            return candidata

    gancho_reserva = random.choice(ganchos_espontaneos)
    cta_reserva = random.choice(fechamentos_cta)
    fallback_frase = " ".join(f"{gancho_reserva} Loja da Valentina: {cta_reserva}".split())
    fallback = f'"{fallback_frase}"'
    historico_sessao.add(fallback)
    return fallback

def gerar_copy_ia_gemini(api_key, nome_produto, descricao_completa, categoria, estilo_titulo, variacao_num):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key.strip()}"
    instrucao_sistema = (
        "Você é o Diretor de Crescimento e Copywriter Sênior do TikTok Shop Brasil. "
        "Crie um roteiro 100% autoral de 11 segundos cravados (24 a 28 palavras). "
        "Escreva com tom espontâneo, natural e direto de quem acabou de testar ou descobrir o produto na prática, "
        "evitando clichês artificiais de propaganda. "
        "Abra com um dos 10 ganchos de retenção nos primeiros segundos: "
        "vitrine de resultado no 1º segundo, revelação/caimento ao virar a câmera, chamada de quem usa a categoria na rotina, "
        "surpresa por entregar mais gastando menos, detalhe prático antes de comprar, teste de 7 opções, "
        "diferença antes/depois na rotina, 'POV: finalmente achei...', descoberta prévia da categoria ou oferta do momento. "
        "Cite obrigatoriamente a 'Loja da Valentina' e encerre chamando para o 'carrinho laranja'. "
        "Retorne APENAS a fala final em português do Brasil entre aspas duplas."
    )
    payload = {
        "contents": [{
            "parts": [{
                "text": (
                    f"{instrucao_sistema}\n\n"
                    f"Nome do Produto: {nome_produto}\n"
                    f"Descrição: {descricao_completa}\n"
                    f"Categoria: {categoria}\n"
                    f"Estilo: {estilo_titulo}\n"
                    f"Variação #{variacao_num}:"
                )
            }]
        }],
        "generationConfig": {"temperature": 1.0, "maxOutputTokens": 90}
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
            raise ValueError("Resposta da API sem candidatos válidos.")
        partes = ((candidates[0].get("content") or {}).get("parts")) or []
        texto_bruto = (partes[0].get("text") if partes else "") or ""
        texto = texto_bruto.strip().replace("\n", " ")
        if not texto:
            raise ValueError("Resposta vazia da API.")
        if not texto.startswith('"'):
            texto = f'"{texto}'
        if not texto.endswith('"'):
            texto = f'{texto}"'
        return texto

# FÁBRICA DE IDENTIDADE ORIGINAL (11s CRAVADOS - COMPLIANCE TIKTOK SHOP)
def obter_identidade_original(i):
    estilos = {
        1: ("Estilo 1: POV Mão & Revelação Tátil", "Foco tátil manuseando o produto com extrema nitidez e som imersivo."),
        2: ("Estilo 2: POV Corpo Inteiro Urbano", "Câmera fluida acompanhando o produto de corpo inteiro ao ar livre."),
        3: ("Estilo 3: POV Provador de Luxo", "Enquadramento elegante detalhando caimento e textura."),
        4: ("Estilo 4: POV Giro 360 no Espelho", "Rotação fluida em frente ao espelho da boutique."),
        5: ("Estilo 5: POV Visual Sem Fala (Trilha Viral)", "Vídeo puramente visual dinâmico sem diálogos."),
        6: ("Estilo 6: POV Close Macro de Detalhes", "Câmera de perto destacando costuras, acabamento e marca."),
        7: ("Estilo 7: Look do Dia Executivo", "Estética de alto padrão e sofisticação."),
        8: ("Estilo 8: Look Verão & Frescor", "Cenário ensolarado mostrando leveza e versatilidade."),
        9: ("Estilo 9: Estudo Clássico em Estúdio", "Iluminação de cinema focada em imponência."),
        10: ("Estilo 10: Provador Relâmpago", "Ritmo ágil focado em conversão de estoque limitado."),
        11: ("Estilo 11: Destaque Dinâmico Urbano", "Utilidade e versatilidade em trânsito."),
        12: ("Estilo 12: Texturas Aconchegantes", "Foco em toque suave e flexível."),
        13: ("Estilo 13: Look Noite com Neon", "Iluminação noturna moderna e sofisticada."),
        14: ("Estilo 14: Streetwear Autêntico", "Estilo urbano jovem e moderno."),
        15: ("Estilo 15: Peça Delicate", "Detalhes refinados para ocasiões especiais."),
        16: ("Estilo 16: Sobreposição Versátil", "Composição moderna e encaixe perfeito."),
        17: ("Estilo 17: Movimento Fluido", "Apresentação natural do produto em uso."),
        18: ("Estilo 18: Peça Premium de Alfaiataria", "Caimento impecável em plano aberto."),
        19: ("Estilo 19: Praticidade Ágil", "Demonstração rápida de facilidade de uso."),
        20: ("Estilo 20: Caminhão Preto TikTok (Saída da Loja)", "Cenário épico externo com caminhão e caixas da Loja da Valentina.")
    }
    titulo, desc = estilos.get(i, (f"Estilo {i}", "Estilo personalizado Valentina."))

    regras_base = (
        "Masterpiece 8K UHD UGC video, EXACT 11.0-SECOND DURATION, 9:16 vertical, RAW optical sensor. "
        "STRICT PRODUCT LOCK: 1:1 fidelity on product, exact textures with zero blur, unique lighting and camera angle. "
        "Zero mics, zero text overlays, zero watermarks, zero third-party logos. "
        "PHYSICS & REALISM LOCK: Product/box physically stable and present from second 0.0 with natural movement and zero sudden pop-ins. "
    )
    if i == 20:
        foco_fluxo = (
            f"{regras_base}"
            "CHRONO-LOCK (0-11s): [0-2s] Speaks at 0.0s pushing boutique door open. [2-8s] Fluid walk. [8-11s] Reaches truck, clean finish at 11.0s."
        )
    elif i == 5:
        foco_fluxo = (
            f"{regras_base}"
            "SILENT VISUAL SHOWCASE (11s): Upbeat dynamic visual rhythm with zero dialogue and pixel stability."
        )
    else:
        foco_fluxo = (
            f"{regras_base}"
            "TIMELINE LOCK (0-11s): Immediate speech start at second 0.0 with Brazilian Portuguese lip-sync, max 28 words delivery, smooth finish at 11.0s."
        )
    return titulo, f"{foco_fluxo} ACTIVE STYLE: {i}. {titulo} - {desc}"

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
    padrao = {i: dict(zip(["titulo", "prompt"], obter_identidade_original(i))) for i in range(1, 21)}
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
    st.markdown("🎬 **SELECIONAR ESTILOS PARA GRADE DIÁRIA**")
    chaves_ord = sorted(list(st.session_state.db_estilos.keys()), key=lambda x: (0, int(x)) if str(x).isdigit() else (1, str(x)))
    lista_titulos = [st.session_state.db_estilos[k]["titulo"] for k in chaves_ord]
    estilos_selecionados = st.multiselect("Selecione", options=lista_titulos, default=lista_titulos[:1] if lista_titulos else [], label_visibility="collapsed", key=f"multi_estilos_{v}")

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
            p_edit = st.text_area("Prompt Enxuto", value=st.session_state.db_estilos[slot_edit]["prompt"], height=140, key=f"p_edit_{slot_edit}_{v}")
            if st.button("💾 SALVAR ALTERAÇÃO", key=f"btn_save_st_{slot_edit}_{v}"):
                st.session_state.db_estilos[slot_edit] = {"titulo": t_edit, "prompt": p_edit}
                salvar_db(st.session_state.db_estilos)
                st.success("Salvo com sucesso!")
                time.sleep(0.5)
                st.rerun()

# DADOS DO PRODUTO
st.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>📦 DADOS DO PRODUTO & DESCRIÇÃO TÉCNICA</p>", unsafe_allow_html=True)
with st.container(border=True):
    p_n1, p_n2 = st.columns(2)
    with p_n1:
        produto_nome = st.text_input("Nome", placeholder="Ex: Tênis Wayper...", label_visibility="collapsed", key=f"nom_{v}")
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

if gerar_clicado:
    if not produto_nome and not descricao_fornecedor:
        st.warning("⚠️ Informe o nome ou descrição.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Envie todas as fotos.")
    elif not estilos_selecionados:
        st.warning("⚠️ Selecione ao menos 1 estilo.")
    else:
        api_key = st.session_state.config_ia.get("api_key", "").strip()
        mapa = {st.session_state.db_estilos[i]["titulo"]: st.session_state.db_estilos[i]["prompt"] for i in st.session_state.db_estilos}
        nome_exibicao = produto_nome.strip() if produto_nome and produto_nome.strip() else "Produto"
        proporcao_alvo = prop_sel.split(" ")[0]

        with st.spinner("🔥 Disparando Motor Viral (11s cravados)..."):
            st.success(f"✅ Gerados {len(estilos_selecionados)} prompts para '{nome_exibicao}'.")
            for idx, est in enumerate(estilos_selecionados):
                horario = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
                p_base = mapa.get(est, "").replace("9:16 vertical", f"{proporcao_alvo} framing")
                is_mudo = "Sem Fala" in est or "SILENT" in p_base
                if not is_mudo:
                    p_base = f"{p_base} DIRECTOR MODE: {skin_sel}."

                if is_mudo or ("Fixo" in copy_mode_sel and '"' in p_base):
                    final_prompt, display_copy = p_base, "Fala fixa mantida."
                else:
                    fala = ""
                    if api_key:
                        try:
                            fala = gerar_copy_ia_gemini(api_key, produto_nome, descricao_fornecedor, tipo_produto, est, idx + 400)
                        except Exception as err:
                            st.caption(f"⚠️ Falha na API Gemini ({err}); usando motor local.")
                    if not fala:
                        fala = resumir_e_modelar_copy_local(produto_nome, descricao_fornecedor, tipo_produto, st.session_state.historico_copys)
                    display_copy = fala
                    final_prompt = f"{p_base}\n\n{fala}"

                st.markdown(f"### 🎬 Prompt {idx+1} • {horario}")
                st.markdown(
                    f'<div class="metric-card"><span class="tag-estilo">{est}</span><br>'
                    f'<span style="color:#00FF66; font-size:11px;">🔥 <b>Copy Viral (11s):</b> {display_copy}</span></div>',
                    unsafe_allow_html=True
                )
                st.code(final_prompt, language="text")
