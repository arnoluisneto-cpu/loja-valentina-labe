import json
import os
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

# DICIONÁRIO MESTRE UNIVERSAL (ADAPTÁVEL A QUALQUER PRODUTO ENVIADO)
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
            "Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: 20. Caminhão Preto Gigante do TikTok Parado com Portas Abertas e Valentina. "
            "STRICT UNIVERSAL PRODUCT LOCK: Focus strictly on the exact product uploaded by the user with zero alterations, zero modifications to its structure, color, details, or brand. "
            "Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Clean collarbone, completely bare surface with zero attachments. "
            "Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. Strict 1:1 pixel lock: identical reference model face and body proportions. "
            "STATIC TRUCK & PERSISTENT BOX CHOREOGRAPHY (0-10s): From exact second 0, the camera is positioned behind the creator (Valentina) from a rear angle. The video opens instantly with Valentina speaking naturally with flawless lip-sync as she walks forward from inside her boutique toward the street. "
            "Directly in front of the store, a massive, giant black delivery truck with clean, bold 'TikTok' lettering written in bright white on its black body is ALREADY PARKED in reverse, completely stationary with its rear cargo doors ALREADY WIDE OPEN, revealing an interior completely packed and stacked wall-to-wall up to the ceiling with storage boxes. "
            "Valentina reaches the glass door, manually pushes it open with her hands, and walks straight up to the truck. She picks up a single storage box. "
            "STRICT PERSISTENCE RULE: Throughout the entire duration of the video, the storage box remains physically present and firmly held in her hands without ever disappearing, vanishing, or morphing. She opens the box steadily while holding it, lifts the exact uploaded product directly out of the box while keeping the box visible in her grip, displays the item clearly to the camera, and concludes her sales pitch. "
            "IMMEDIATE FLAWLESS START & CLEAN SCREEN: Absolute zero static frames, zero ghosting, zero overlay transparency, zero floating text, zero subtitles, zero UI overlays, zero watermarks, zero generated text captions. SMOOTH TAIL BUFFER: Action and speech naturally conclude right at 10 seconds with zero abrupt audio cuts and zero dead silence. Fixed realistic background, organic human movement.\n\n"
            "\"Olha, gente... acabou de chegar o estoque aqui na Loja da Valentina. A gente vai trabalhar só com esse produto, porque ele é recordista de vendas e de muita qualidade! Clica aqui no carrinho laranja embaixo para garantir o seu.\"\n\n"
            "Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, AI morphing transition, soft blending, product switching, changing product model at the end, sudden jump cuts, rapid unrealistic pacing, over 10s, rushed speech, fast jerky movement, static starting frame, ghosting effect, transparent overlay, floating text, subtitles, text captions, generated writing, UI graphics, watermarks, distorted brand, altered design, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI, walking backward, truck moving, doors opening, box disappearing, box vanishing, item morphing into hand."
        )
    else:
        prompt_texto = (
            f"Masterpiece 8K UHD hyper-realistic TikTok Shop UGC video powered by Arri Alexa cinema color science, 10-second precise duration, 9:16 vertical format, RAW optical sensor, photorealistic human physics. ACTIVE STYLE: {i}. {titulo_texto} - {desc_estilo}. "
            f"STRICT UNIVERSAL PRODUCT LOCK: Faithfully match the exact product from the user-uploaded image with zero substitution, preserving original colors, textures, and details. "
            f"Absolute zero microphones, NO lapel mics, NO clip-on mics, NO wireless mics on clothing, NO earphones, NO floating gadgets, NO text overlays, NO subtitles, NO watermarks, NO UI graphics, NO branding. Clean collarbone. "
            f"Cinematic Visual Engineering: hyper-detailed micro-textures, razor-sharp natural focus, rich dynamic contrast with zero washed-out shadows, professional 3-point studio lighting, lifelike human skin pores, and glossy vibrant color grading. "
            f"Strict 1:1 pixel lock and rigid product match with zero substitution. "
            f"VIRAL HOOK & FLUID TRY-ON FLOW (0-10s): The video opens dynamically with the creator looking straight into the camera delivering a strong magnetic hook, pacing her speech evenly across the full 10 seconds while interacting directly with the item.\n\n"
            f"\"Olha, gente, meninas, olha aqui o que chegou agora na Loja da Valentina! Chegou todo esse estoque exclusivo. A gente vai trabalhar só com essa marca porque está vendendo muito. Clica no carrinho laranja aqui embaixo e garanta a sua, que esse estoque chegou agora e vai estar de promoção!\"\n\n"
            f"Absolute Negative Prompt / Anti-Mic & Anti-Artifact Engine: microphone, lapel mic, clip-on microphone, wireless mic, badge, pin, earphones, clipped accessories, floating gadgets, washed-out colors, dull lighting, blurry details, soft focus, digital noise, flat lighting, early speech ending, dead silence at the end, abrupt appearance, pop-up object, harsh audio cut, model swapping, face morphing, background shift, CGI."
        )
    return titulo_texto, prompt_texto

# PERSISTÊNCIA PERMANENTE NO DISCO (JSON)
DB_FILE = "moldes_salvos.json"

def carregar_db_disco():
    if os.path.exists(DB_FILE):
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                dados = json.load(f)
                if isinstance(dados, dict):
                    return {int(k) if str(k).isdigit() else k: v for k, v in dados.items()}
        except Exception:
            pass
    padrao = {}
    for i in range(1, 21):
        t, p = obter_identidade_original(i)
        padrao[i] = {"titulo": t, "prompt": p}
    return padrao

def salvar_db_disco(db_dict):
    try:
        with open(DB_FILE, "w", encoding="utf-8") as f:
            json.dump(db_dict, f, ensure_ascii=False, indent=4)
    except Exception:
        pass

# GESTÃO DE ESTADOS & FILA DE EXCLUSÕES ORDENADA
if "db_estilos" not in st.session_state:
    st.session_state.db_estilos = carregar_db_disco()

if "fila_exclusoes" not in st.session_state:
    st.session_state.fila_exclusoes = []

if "form_version" not in st.session_state:
    st.session_state.form_version = 0

if "estilo_ativo_idx" not in st.session_state:
    st.session_state.estilo_ativo_idx = 1

if "acesso_liberado" not in st.session_state:
    st.session_state.acesso_liberado = False

def limpar_apenas_formulario():
    st.session_state.form_version += 1
    st.session_state.acesso_liberado = False
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
        st.markdown("⚡ **STATUS ENGINE**")
        st.markdown("<span style='color: #00FF66; font-size: 11px; font-weight:700;'>Ativo & Sincronizado</span>", unsafe_allow_html=True)

with st.container(border=True):
    st.markdown("🎬 **SELECIONAR ESTILOS PARA GRADE DIÁRIA**")
    lista_titulos_geral = [st.session_state.db_estilos[i]["titulo"] for i in sorted(st.session_state.db_estilos.keys())] if st.session_state.db_estilos else []
    estilos_selecionados = st.multiselect(
        "Selecione",
        options=lista_titulos_geral,
        default=[st.session_state.db_estilos[len(st.session_state.db_estilos)]["titulo"]] if len(st.session_state.db_estilos) > 0 else [],
        label_visibility="collapsed",
        key=f"multi_estilos_{v}"
    )

# GERENCIADOR COM VALIDAÇÃO LIMPA
SENHA_MESTRE = "vidalooka2"

with st.expander("⚙️ Gerenciar / Restaurar / Excluir Estilos (Área Restrita)", expanded=True):
    col_s1, col_s2 = st.columns([3, 1])
    
    with col_s1:
        st.markdown("🔐 **SENHA ADMINISTRATIVA**")
        senha_digitada = st.text_input("Senha", placeholder="Digite a senha...", type="password", label_visibility="collapsed", key=f"input_senha_adm_{v}")
    
    with col_s2:
        st.markdown("🛡️ **AÇÃO**")
        if st.button("🔓 VALIDAR", key=f"btn_validar_{v}"):
            if senha_digitada == SENHA_MESTRE:
                st.session_state.acesso_liberado = True
            else:
                st.session_state.acesso_liberado = False

    st.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)

    if st.session_state.acesso_liberado:
        col_ger1, col_ger2 = st.columns(2)
        
        with col_ger1:
            texto_botao_restaurar = "🔄 RESTAURAR PRÓXIMO APAGADO"
            if st.session_state.fila_exclusoes:
                proximo_a_voltar = st.session_state.fila_exclusoes[0]
                texto_botao_restaurar = f"🔄 RESTAURAR ESTILO {proximo_a_voltar}"

            if st.button(texto_botao_restaurar, key=f"btn_rest_prox_{v}"):
                if st.session_state.fila_exclusoes:
                    id_para_restaurar = st.session_state.fila_exclusoes.pop(0)
                    
                    with st.spinner(f"🔄 Restaurando Estilo {id_para_restaurar}..."):
                        time.sleep(0.4)
                        t_orig, p_orig = obter_identidade_original(id_para_restaurar)
                        st.session_state.db_estilos[id_para_restaurar] = {"titulo": t_orig, "prompt": p_orig}
                        salvar_db_disco(st.session_state.db_estilos)
                    
                    st.success(f"✅ Estilo {id_para_restaurar} retornado com sucesso!")
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.info("ℹ️ Não há nenhum estilo na fila de restauração.")

        with col_ger2:
            if st.button("🔄 RESTAURAR TODOS OS 20", key=f"btn_rest_all_{v}"):
                with st.spinner("🔄 Restaurando grade completa de 1 a 20..."):
                    time.sleep(0.4)
                    st.session_state.db_estilos = {}
                    for i in range(1, 21):
                        t, p = obter_identidade_original(i)
                        st.session_state.db_estilos[i] = {"titulo": t, "prompt": p}
                    st.session_state.fila_exclusoes = []
                    salvar_db_disco(st.session_state.db_estilos)
                st.success("✅ Grade completa de 1 a 20 restaurada perfeitamente!")
                time.sleep(0.8)
                st.rerun()

        st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

        if not st.session_state.db_estilos:
            st.write("Nenhum estilo na memória.")
        else:
            ids_disp = sorted(list(st.session_state.db_estilos.keys()))
            
            estilo_escolhido = st.selectbox(
                "Selecione o Estilo para Excluir",
                options=ids_disp,
                format_func=lambda x: f"Estilo {x} - {st.session_state.db_estilos[x]['titulo']}",
                key=f"selectbox_gerenciador_topo_{v}"
            )
            
            st.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
            
            if st.button("🗑️ EXCLUIR ESTILO SELECIONADO", key=f"btn_exc_estilo_{v}"):
                with st.spinner(f"🗑️ Excluindo Estilo {estilo_escolhido}..."):
                    time.sleep(0.3)
                    if estilo_escolhido not in st.session_state.fila_exclusoes:
                        st.session_state.fila_exclusoes.append(estilo_escolhido)
                    
                    del st.session_state.db_estilos[estilo_escolhido]
                    salvar_db_disco(st.session_state.db_estilos)
                
                st.success(f"🗑️ Estilo {estilo_escolhido} excluído definitivamente do disco!")
                time.sleep(0.8)
                st.rerun()

st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# MODO DE OPERAÇÃO UNIFICADO (EDITAR OU INSERIR NO FINAL)
todos_ids_existentes = list(st.session_state.db_estilos.keys())
proximo_id_sugerido = (max(todos_ids_existentes) + 1) if todos_ids_existentes else 1

modo_operacao = st.radio("Modo de Operação", ["✏️ Editar Estilo Existente", f"➕ Inserir Novo (Estilo {proximo_id_sugerido})"], horizontal=True, label_visibility="collapsed", key=f"modo_op_{v}")

st.markdown(f"<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>{modo_operacao.upper()}</p>", unsafe_allow_html=True)

with st.container(border=True):
    opcoes_editor = sorted(todos_ids_existentes)
    
    if "Editar" in modo_operacao:
        if opcoes_editor:
            if st.session_state.estilo_ativo_idx not in opcoes_editor:
                st.session_state.estilo_ativo_idx = opcoes_editor[0]
                
            slot_num_edit = st.selectbox(
                "Selecione o Estilo para Editar", 
                options=opcoes_editor, 
                index=opcoes_editor.index(st.session_state.estilo_ativo_idx) if st.session_state.estilo_ativo_idx in opcoes_editor else 0,
                format_func=lambda x: f"Estilo {x} - {st.session_state.db_estilos[x]['titulo']}",
                key=f"select_editor_direto_id_{v}"
            )
            
            if slot_num_edit != st.session_state.estilo_ativo_idx:
                st.session_state.estilo_ativo_idx = slot_num_edit

            titulo_atual_estilo = st.session_state.db_estilos[slot_num_edit]["titulo"]
            prompt_atual_estilo = st.session_state.db_estilos[slot_num_edit]["prompt"]

            novo_titulo_editado = st.text_input("Tema / Título do Estilo", value=titulo_atual_estilo, key=f"titulo_input_{slot_num_edit}_{v}")
            texto_editado_usuario = st.text_area("Código do Prompt", value=prompt_atual_estilo, height=160, key=f"prompt_textarea_{slot_num_edit}_{v}")
            
            st.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
            
            if st.button("💾 SALVAR ALTERAÇÃO", key=f"btn_salvar_{slot_num_edit}_{v}"):
                if not novo_titulo_editado or not texto_editado_usuario:
                    st.warning("⚠️ Preencha o Título e o Código do prompt antes de salvar.")
                else:
                    with st.spinner(f"💾 Salvando alterações do Estilo {slot_num_edit} no disco..."):
                        time.sleep(0.4)
                        st.session_state.db_estilos[slot_num_edit]["titulo"] = novo_titulo_editado
                        st.session_state.db_estilos[slot_num_edit]["prompt"] = texto_editado_usuario
                        salvar_db_disco(st.session_state.db_estilos)
                    st.success(f"✨ Estilo {slot_num_edit} alterado e gravado com sucesso!")
                    time.sleep(0.8)
                    st.rerun()
        else:
            st.write("Nenhum estilo disponível.")
    else:
        novo_titulo_input = st.text_input("Título / Tema do Novo Prompt", value="", placeholder="Ex: Novo Estilo Personalizado...", key=f"campo_novo_titulo_valencia_fixo_{v}")
        novo_prompt_input = st.text_area("Código do Novo Prompt", placeholder="Cole o código do prompt aqui...", height=160, key=f"campo_novo_prompt_valencia_fixo_{v}")
        
        st.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
        
        if st.button("📥 INSERIR E SALVAR NO FINAL", key=f"btn_inserir_novo_{v}"):
            if not novo_titulo_input or not novo_prompt_input:
                st.warning("⚠️ Preencha o Título e o Código do novo prompt.")
            else:
                with st.spinner(f"📥 Inserindo Estilo {proximo_id_sugerido}..."):
                    time.sleep(0.4)
                    st.session_state.db_estilos[proximo_id_sugerido] = {
                        "titulo": novo_titulo_input,
                        "prompt": novo_prompt_input
                    }
                    st.session_state.estilo_ativo_idx = proximo_id_sugerido
                    salvar_db_disco(st.session_state.db_estilos)
                st.success(f"🎉 Novo Estilo {proximo_id_sugerido} inserido e gravado permanentemente!")
                time.sleep(0.8)
                st.rerun()

st.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# DADOS DO PRODUTO & UPLOADS
st.markdown("<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>📦 DADOS DO PRODUTO & UPLOADS</p>", unsafe_allow_html=True)

with st.container(border=True):
    c_l1_1, c_l1_2 = st.columns(2)
    with c_l1_1:
        st.markdown("🏷️ **NOME PRODUTO / SKU**")
        produto_nome = st.text_input("Nome", placeholder="Ex: Vestido Midi, Bolsa de Couro...", label_visibility="collapsed", key=f"input_nome_produto_{v}")
    with c_l1_2:
        st.markdown("📂 **CATEGORIA**")
        tipo_produto = st.selectbox("Categoria", ["Geral / Universal", "Calçado", "Vestuário", "Acessório", "Bolsa", "Outros"], label_visibility="collapsed", key=f"sel_categoria_{v}")

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
    if not produto_nome:
        st.warning("⚠️ Informe o nome do produto.")
    elif not foto_peca or not foto_modelo or not foto_produto_analise:
        st.warning("⚠️ Envie todas as fotos.")
    elif not estilos_selecionados:
        st.warning("⚠️ Selecione pelo menos 1 estilo.")
    else:
        agora = datetime.now().strftime("%H:%M:%S")
        st.success(f"✅ Gerados {len(estilos_selecionados)} prompts às {agora} para '{produto_nome}'.")
        
        mapa_prompts = {st.session_state.db_estilos[i]["titulo"]: st.session_state.db_estilos[i]["prompt"] for i in st.session_state.db_estilos if i in st.session_state.db_estilos}
        
        for idx, estilo_titulo in enumerate(estilos_selecionados):
            prompt_numero = idx + 1
            horario_postagem = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
            prompt_ativo_slot = mapa_prompts.get(estilo_titulo, "Prompt não encontrado.")

            st.markdown(f"### 🎬 Prompt {prompt_numero} • {horario_postagem}")
            st.markdown(
                '<div class="metric-card">'
                f'<span class="tag-estilo">{estilo_titulo}</span><br>',
                unsafe_allow_html=True
            )
            # Exibe o prompt dentro da caixinha curta e compacta com rolagem e botão de cópia
            st.code(prompt_ativo_slot, language="text")
            st.markdown('</div>', unsafe_allow_html=True)
