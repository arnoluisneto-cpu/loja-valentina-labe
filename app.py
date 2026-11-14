import streamlit as str_app
from datetime import datetime
import time

str_app.set_page_config(
    page_title="Valentina Labs - TikTok Shop Automation",
    page_icon="💜",
    layout="centered"
)

# ESTÉTICA DE ALTO LUXO (BLINDADA E POLIDA)
str_app.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    .stApp, .main, div[data-testid="stVerticalBlock"] {
        background-color: #0b0914 !important;
        color: #ffffff !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    /* Botão de Upload verde com texto e ícone PRETO E EM NEGRITO */
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
    
    /* Fundo da caixa de upload roxo escuro */
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

# DICIONÁRIO MESTRE DE FÁBRICA (ORIGINAL DOS 20 ESTILOS)
def obter_identidade_original(i):
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
    
    titulo_texto, desc_estilo = identidades_estilos.get(i, (f"Estilo {i}", "Estilo personalizado da Loja da Valentina."))
    
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
    return titulo_texto, prompt_texto

# GESTÃO DE ESTADOS & FILA DE EXCLUSÕES ORDENADA
if "db_estilos" not in str_app.session_state:
    str_app.session_state.db_estilos = {}
    for i in range(1, 21):
        t, p = obter_identidade_original(i)
        str_app.session_state.db_estilos[i] = {"titulo": t, "prompt": p}

if "fila_exclusoes" not in str_app.session_state:
    str_app.session_state.fila_exclusoes = []

if "form_version" not in str_app.session_state:
    str_app.session_state.form_version = 0

if "estilo_ativo_idx" not in str_app.session_state:
    str_app.session_state.estilo_ativo_idx = 1

if "acesso_liberado" not in str_app.session_state:
    str_app.session_state.acesso_liberado = False

def limpar_apenas_formulario():
    str_app.session_state.form_version += 1
    for k in ["input_nome_produto", "sel_categoria", "sel_skin", "sel_prop", "multi_estilos", "m_1", "prod_1", "p_1"]:
        if k in str_app.session_state:
            del str_app.session_state[k]

v = str_app.session_state.form_version

# TOPO
str_app.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">LABORATÓRIOS VALENTINA</h1>
        <p class="hero-subtitle">LOJA DA VALENTINA • AUTOMATIZAÇÃO DE LOJAS NO TIKTOK</p>
    </div>
""", unsafe_allow_html=True)

str_app.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# PAINEL DE CONTROLE RÁPIDO
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
    lista_titulos_geral = [str_app.session_state.db_estilos[i]["titulo"] for i in sorted(str_app.session_state.db_estilos.keys())] if str_app.session_state.db_estilos else []
    estilos_selecionados = str_app.multiselect(
        "Selecione",
        options=lista_titulos_geral,
        default=[str_app.session_state.db_estilos[len(str_app.session_state.db_estilos)]["titulo"]] if len(str_app.session_state.db_estilos) > 0 else [],
        label_visibility="collapsed",
        key=f"multi_estilos_{v}"
    )

# GERENCIADOR COM VALIDAÇÃO LIMPA (SEM MENSAGENS PERMANENTES)
SENHA_MESTRE = "vidalooka2"

with str_app.expander("⚙️ Gerenciar / Restaurar / Excluir Estilos (Área Restrita)", expanded=True):
    col_s1, col_s2 = str_app.columns([3, 1])
    
    with col_s1:
        str_app.markdown("🔐 **SENHA ADMINISTRATIVA**")
        senha_digitada = str_app.text_input("Senha", placeholder="Digite a senha...", type="password", label_visibility="collapsed", key="input_senha_adm")
    
    with col_s2:
        str_app.markdown("🛡️ **AÇÃO**")
        if str_app.button("🔓 VALIDAR"):
            if senha_digitada == SENHA_MESTRE:
                str_app.session_state.acesso_liberado = True
            else:
                str_app.session_state.acesso_liberado = False

    str_app.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)

    if str_app.session_state.acesso_liberado:
        col_ger1, col_ger2 = str_app.columns(2)
        
        with col_ger1:
            texto_botao_restaurar = "🔄 RESTAURAR PRÓXIMO APAGADO"
            if str_app.session_state.fila_exclusoes:
                proximo_a_voltar = str_app.session_state.fila_exclusoes[0]
                texto_botao_restaurar = f"🔄 RESTAURAR ESTILO {proximo_a_voltar}"

            if str_app.button(texto_botao_restaurar):
                if str_app.session_state.fila_exclusoes:
                    id_para_restaurar = str_app.session_state.fila_exclusoes.pop(0)
                    
                    with str_app.spinner(f"🔄 Restaurando Estilo {id_para_restaurar} em sua numeração original..."):
                        time.sleep(0.4)
                        t_orig, p_orig = obter_identidade_original(id_para_restaurar)
                        str_app.session_state.db_estilos[id_para_restaurar] = {"titulo": t_orig, "prompt": p_orig}
                    
                    str_app.success(f"✅ Estilo {id_para_restaurar} retornado com sucesso para a numeração {id_para_restaurar}!")
                    time.sleep(0.8)
                    str_app.rerun()
                else:
                    str_app.info("ℹ️ Não há nenhum estilo na fila de restauração (nenhum apagado recentemente).")

        with col_ger2:
            if str_app.button("🔄 RESTAURAR TODOS OS 20"):
                with str_app.spinner("🔄 Restaurando grade completa de 1 a 20..."):
                    time.sleep(0.4)
                    str_app.session_state.db_estilos = {}
                    for i in range(1, 21):
                        t, p = obter_identidade_original(i)
                        str_app.session_state.db_estilos[i] = {"titulo": t, "prompt": p}
                    str_app.session_state.fila_exclusoes = []
                str_app.success("✅ Grade completa de 1 a 20 restaurada perfeitamente!")
                time.sleep(0.8)
                str_app.rerun()

        str_app.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

        if not str_app.session_state.db_estilos:
            str_app.write("Nenhum estilo na memória.")
        else:
            ids_disp = sorted(list(str_app.session_state.db_estilos.keys()))
            
            estilo_escolhido = str_app.selectbox(
                "Selecione o Estilo para Excluir",
                options=ids_disp,
                format_func=lambda x: f"Estilo {x} - {str_app.session_state.db_estilos[x]['titulo']}",
                key="selectbox_gerenciador_topo"
            )
            
            str_app.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
            
            if str_app.button("🗑️ EXCLUIR ESTILO SELECIONADO"):
                with str_app.spinner(f"🗑️ Excluindo Estilo {estilo_escolhido}..."):
                    time.sleep(0.3)
                    if estilo_escolhido not in str_app.session_state.fila_exclusoes:
                        str_app.session_state.fila_exclusoes.append(estilo_escolhido)
                    
                    del str_app.session_state.db_estilos[estilo_escolhido]
                
                str_app.success(f"🗑️ Estilo {estilo_escolhido} excluído e guardado na fila para restauração exata!")
                time.sleep(0.8)
                str_app.rerun()

str_app.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# MODO DE OPERAÇÃO UNIFICADO (EDITAR OU INSERIR NO FINAL)
todos_ids_existentes = list(str_app.session_state.db_estilos.keys())
proximo_id_sugerido = (max(todos_ids_existentes) + 1) if todos_ids_existentes else 1

modo_operacao = str_app.radio("Modo de Operação", ["✏️ Editar Estilo Existente", f"➕ Inserir Novo (Estilo {proximo_id_sugerido})"], horizontal=True, label_visibility="collapsed")

str_app.markdown(f"<p style='font-weight:700; color:#00FF66; margin-bottom:4px; font-size:11px;'>{modo_operacao.upper()}</p>", unsafe_allow_html=True)

with str_app.container(border=True):
    opcoes_editor = sorted(todos_ids_existentes)
    
    if "Editar" in modo_operacao:
        if opcoes_editor:
            if str_app.session_state.estilo_ativo_idx not in opcoes_editor:
                str_app.session_state.estilo_ativo_idx = opcoes_editor[0]
                
            slot_num_edit = str_app.selectbox(
                "Selecione o Estilo para Editar", 
                options=opcoes_editor, 
                index=opcoes_editor.index(str_app.session_state.estilo_ativo_idx) if str_app.session_state.estilo_ativo_idx in opcoes_editor else 0,
                format_func=lambda x: f"Estilo {x} - {str_app.session_state.db_estilos[x]['titulo']}",
                key="select_editor_direto_id"
            )
            
            if slot_num_edit != str_app.session_state.estilo_ativo_idx:
                str_app.session_state.estilo_ativo_idx = slot_num_edit

            titulo_atual_estilo = str_app.session_state.db_estilos[slot_num_edit]["titulo"]
            prompt_atual_estilo = str_app.session_state.db_estilos[slot_num_edit]["prompt"]

            novo_titulo_editado = str_app.text_input("Tema / Título do Estilo", value=titulo_atual_estilo, key=f"titulo_input_{slot_num_edit}")
            texto_editado_usuario = str_app.text_area("Código do Prompt", value=prompt_atual_estilo, height=160, key=f"prompt_textarea_{slot_num_edit}")
            
            str_app.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
            
            if str_app.button("💾 SALVAR ALTERAÇÃO"):
                with str_app.spinner(f"💾 Salvando alterações do Estilo {slot_num_edit}..."):
                    time.sleep(0.4)
                    str_app.session_state.db_estilos[slot_num_edit]["titulo"] = novo_titulo_editado
                    str_app.session_state.db_estilos[slot_num_edit]["prompt"] = texto_editado_usuario
                str_app.success(f"✨ Estilo {slot_num_edit} alterado e salvo com sucesso!")
                time.sleep(0.8)
                str_app.rerun()
        else:
            str_app.write("Nenhum estilo disponível.")
    else:
        novo_titulo_input = str_app.text_input("Título / Tema do Novo Prompt", value=f"Estilo {proximo_id_sugerido}: Novo Estilo Personalizado Valentina", key="campo_novo_titulo_valencia_fixo")
        novo_prompt_input = str_app.text_area("Código do Novo Prompt", placeholder="Cole o código do prompt aqui...", height=160, key="campo_novo_prompt_valencia_fixo")
        
        str_app.markdown("<div style='margin: 4px 0;'></div>", unsafe_allow_html=True)
        
        if str_app.button("📥 INSERIR E SALVAR NO FINAL"):
            if not novo_titulo_input or not novo_prompt_input:
                str_app.warning("⚠️ Preencha o Título e o Código do novo prompt.")
            else:
                with str_app.spinner(f"📥 Inserindo Estilo {proximo_id_sugerido}..."):
                    time.sleep(0.4)
                    str_app.session_state.db_estilos[proximo_id_sugerido] = {
                        "titulo": novo_titulo_input,
                        "prompt": novo_prompt_input
                    }
                    str_app.session_state.estilo_ativo_idx = proximo_id_sugerido
                str_app.success(f"🎉 Novo Estilo {proximo_id_sugerido} inserido com sucesso!")
                time.sleep(0.8)
                str_app.rerun()

str_app.markdown("<div style='margin: 6px 0;'></div>", unsafe_allow_html=True)

# DADOS DO PRODUTO & UPLOADS
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

# BOTÕES CENTRALIZADOS
col_esq_vazio, col_btn1, col_btn2, col_dir_vazio = str_app.columns([1, 2, 2, 1])

with col_btn1:
    gerar_clicado = str_app.button("🚀 GERAR PROMPTS")

with col_btn2:
    str_app.button("🔄 LIMPAR TUDO", on_click=limpar_apenas_formulario)

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
        
        mapa_prompts = {str_app.session_state.db_estilos[i]["titulo"]: str_app.session_state.db_estilos[i]["prompt"] for i in str_app.session_state.db_estilos if i in str_app.session_state.db_estilos}
        
        for idx, estilo_titulo in enumerate(estilos_selecionados):
            prompt_numero = idx + 1
            horario_postagem = GRADE_HORARIOS[idx % len(GRADE_HORARIOS)]
            prompt_ativo_slot = mapa_prompts.get(estilo_titulo, "Prompt não encontrado.")

            str_app.markdown(f"### 🎬 Prompt {prompt_numero} • {horario_postagem}")
            str_app.markdown(
                '<div class="metric-card">'
                f'<span class="tag-estilo">{estilo_titulo}</span><br>',
                unsafe_allow_html=True
            )
            str_app.code(prompt_ativo_slot, language="text")
            str_app.markdown('</div>', unsafe_allow_html=True)
