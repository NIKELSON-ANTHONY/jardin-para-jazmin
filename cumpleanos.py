import os
from nicegui import app, ui

# Permitir que NiceGUI sirva tu archivo de audio 'pensamientos.mp3' desde la carpeta actual
app.add_media_files('/media', '.')

@ui.page('/')
def main_page():
    # Estilos CSS generales y animaciones
    ui.add_head_html('''
    <style>
        body {
            background-color: #0f172a;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }
        @keyframes floatCenter {
            0% { transform: translateY(0px) scale(1); }
            50% { transform: translateY(-8px) scale(1.03); }
            100% { transform: translateY(0px) scale(1); }
        }
        .central-flower-3d {
            animation: floatCenter 4s ease-in-out infinite;
            filter: drop-shadow(0 15px 25px rgba(0, 0, 0, 0.4));
        }
        .petal-btn {
            transition: all 0.25s ease;
            cursor: pointer;
        }
        .petal-btn:active {
            transform: scale(0.97);
        }
    </style>
    ''')

    # Configuración de audio cargando el archivo 'pensamientos.mp3'
    audio_src = "/media/pensamientos.mp3"
    
    ui.add_body_html(f'''
    <audio id="bg-music" loop src="{audio_src}"></audio>
    <script>
        function playMusic() {{
            var audio = document.getElementById('bg-music');
            if (audio) {{
                audio.play().catch(e => console.log('Reproducción iniciada por interacción'));
                var btn = document.getElementById('music-text-label');
                if(btn) btn.innerText = '🎵 Airbag - Pensamientos: On';
            }}
        }}

        function toggleAudio() {{
            var audio = document.getElementById('bg-music');
            var btn = document.getElementById('music-text-label');
            if (audio.paused) {{
                audio.play();
                if(btn) btn.innerText = '🎵 Airbag - Pensamientos: On';
            }} else {{
                audio.pause();
                if(btn) btn.innerText = '🔇 Música: Off';
            }}
        }}
    </script>
    ''')

    # Base de datos del jardín con recuerdos
    jardin = [
        {
            "nombre": "El Girasol",
            "subtitulo": "Espontaneidad, risas y sinceridad",
            "flor": "🌻",
            "color_texto": "text-amber-300",
            "borde_tarjeta": "border-amber-500/40",
            "badge_bg": "bg-amber-500/20 text-amber-300 border border-amber-500/40",
            "color_activo": "#f59e0b",
            "color_texto_activo": "#1f1300",
            "color_inactivo": "rgba(255, 255, 255, 0.08)",
            "tarjeta_recuerdo": "border-amber-400",
            "petalos": [
                {
                    "parte": "🌻 Pétalo 1",
                    "titulo": "Sinceridad y Nervios (Marzo 2025)",
                    "texto": "Aún me emociona recordar la primera vez que me preguntaste, con esa alegría tan tuya, si te había dado un detalle por marzo del 2025. Aunque los nervios me erizaban la piel y por un segundo quise mentirte para hacerte feliz, decidí ser completamente sincero. Ese instante de vulnerabilidad y honestidad marcó el inicio de algo irremplazable."
                },
                {
                    "parte": "🌻 Pétalo 2",
                    "titulo": "Un halago especial",
                    "texto": "Aquel día que decidí ponerme mi gabardina y, al verme, me dijiste entre sonrisas que parecía Jun-pyo o Lee Min-ho. No te lo dije entonces, pero me encantó... porque verte sonreír gracias a mí es una de mis cosas favoritas."
                },
                {
                    "parte": "🌻 Pétalo 3",
                    "titulo": "Susto en el archivo",
                    "texto": "Recordar cuando estaba sumergido en mi música, cantando mientras archivaba, y de pronto apareciste por la espalda a tocarme las costillas. Me sacaste un grito de terror inmenso y luego te perseguí entre risas. Amo la forma en que logras transformar cualquier momento ordinario en una alegría inolvidable."
                }
            ]
        },
        {
            "nombre": "La Rosa",
            "subtitulo": "Miradas, gestos dulces y complicidad",
            "flor": "🌹",
            "color_texto": "text-rose-300",
            "borde_tarjeta": "border-rose-500/40",
            "badge_bg": "bg-rose-500/20 text-rose-300 border border-rose-500/40",
            "color_activo": "#e11d48",
            "color_texto_activo": "#ffffff",
            "color_inactivo": "rgba(255, 255, 255, 0.08)",
            "tarjeta_recuerdo": "border-rose-400",
            "petalos": [
                {
                    "parte": "🌹 Pétalo 1",
                    "titulo": "Miradas en redacción",
                    "texto": "Cada vez que entraba a redacción a llevar las pericias, buscaba tu mirada. Cruzar nuestros ojos se sentía mágico y me llenaba el alma, aunque la verdad es que la emoción me ganaba, me ponía rojo de inmediato y me costaba sostenerte la mirada sin que el corazón se me acelerara."
                },
                {
                    "parte": "🌹 Pétalo 2",
                    "titulo": "Nuestros apodos especiales",
                    "texto": "El día que nacieron nuestros apodos especiales: cuando te llamé «Mujer de Arena del Vecino» y tú me nombraste «Poseidón de Totora». Detrás de esas palabras juguetonas se escondía una complicidad hermosa que hasta hoy guardo con inmenso cariño."
                },
                {
                    "parte": "🌹 Pétalo 3",
                    "titulo": "Pan con chicharrón y manzana",
                    "texto": "El sencillo pero inolvidable momento en que te invité un pan con chicharrón y tú, con esa dulzura que te caracteriza, me trajiste una manzana sabiendo que eran mis favoritas. Esos pequeños e insustituibles gestos se quedaron grabados para siempre en mi corazón."
                }
            ]
        },
        {
            "nombre": "El Tulipán",
            "subtitulo": "Ocurrencias, salidas y momentos compartidos",
            "flor": "🌷",
            "color_texto": "text-pink-300",
            "borde_tarjeta": "border-pink-500/40",
            "badge_bg": "bg-pink-500/20 text-pink-300 border border-pink-500/40",
            "color_activo": "#ec4899",
            "color_texto_activo": "#ffffff",
            "color_inactivo": "rgba(255, 255, 255, 0.08)",
            "tarjeta_recuerdo": "border-pink-400",
            "petalos": [
                {
                    "parte": "🌷 Pétalo 1",
                    "titulo": "«¡Ni más te hablo!»",
                    "texto": "Ese día en que me saludaste y me preguntaste cómo estaba, y yo —pensando erróneamente que era solo por las fechas de los aportes— te dije que seguro me hablabas por eso. Tu respuesta con un «¡ni más te hablo!» y tu risa me demostraron lo equivocado que estaba. Me quedé con una sonrisa hermosa recordando tu espontaneidad."
                },
                {
                    "parte": "🌷 Pétalo 2",
                    "titulo": "Pichari y la fiesta de la UML",
                    "texto": "Cuando llegaste de Pichari para la fiesta de la UML y, de la manera más sutil y linda, me dijiste que me habías extrañado. Te sonrojaste al volvértelo a preguntar, pero lo que no sabías es que por dentro mi cerebro hizo un cortocircuito: me moría por decirte cuánto te había extrañado yo también, pero las palabras no alcanzaban para expresarlo."
                },
                {
                    "parte": "🌷 Pétalo 3",
                    "titulo": "Paseo a Dollarcity",
                    "texto": "Nuestra salida a Dollarcity mientras yo andaba todo cojito. Aunque me mirabas con sospecha preguntándome si me sentía incómodo o aburrido, la única verdad es que a tu lado tocaba el cielo. Escondí el dolor insoportable de mi muela solo para no arruinar nuestro tiempo juntos y poder compartir una comida a tu lado. Valía cada segundo con tal de estar contigo."
                }
            ]
        },
        {
            "nombre": "El Jazmín",
            "subtitulo": "Calidez, paz... y tu nombre",
            "flor": "💮",
            "color_texto": "text-emerald-300",
            "borde_tarjeta": "border-emerald-500/40",
            "badge_bg": "bg-emerald-500/20 text-emerald-300 border border-emerald-500/40",
            "color_activo": "#059669",
            "color_texto_activo": "#ffffff",
            "color_inactivo": "rgba(255, 255, 255, 0.08)",
            "tarjeta_recuerdo": "border-emerald-400",
            "petalos": [
                {
                    "parte": "💮 Pétalo 1",
                    "titulo": "Tu llamada tras mi operación",
                    "texto": "Escuchar tu voz llamándome después de mi operación fue lo más bonito y reconfortante del mundo. Aunque en ese instante la doctora requería mi historial y más tarde estabas ocupadita, saber que pensaste en mí en un momento tan delicado significó absolutamente todo."
                },
                {
                    "parte": "💮 Pétalo 2",
                    "titulo": "Un abrazo eterno en el archivo",
                    "texto": "El momento en que llegaste renegando al archivo por el estrés del trabajo y los pendientes. No dudé en abrazarte fuerte para ahuyentar toda la energía negativa y regalarte paz. Mientras te sostenía entre mis brazos, lo único que le pedía al tiempo era que ese abrazo fuera eterno."
                },
                {
                    "parte": "💮 Pétalo 3",
                    "titulo": "Infinitos tesoros a tu lado",
                    "texto": "Quedan infinitos recuerdos por mencionar, porque a tu lado cada instante se vuelve un tesoro. Sé muy bien que probablemente no sea capaz de decirte todo esto en persona, porque al tenerte en frente me daría el síndrome de Asperger: se me nublaría todo, los nervios me ganarían y no sabría ni por dónde empezar. Pero ten por seguro que, muy dentro de mí, te estaría dedicando cada una de estas palabras de la manera más detallada, ordenada y sentimental. Por esa misma razón elijo escribírtelo. Mi mente colapsa de tantas memorias hermosas a tu lado; si existiera una cámara fotografiando cada segundo juntos, guardaría cada imagen como la prueba de lo maravilloso que es compartir la vida contigo."
                }
            ]
        }
    ]

    # Sección de Planes / Sueños Futuros
    futuro = [
        {
            "icono": "✈️",
            "titulo": "El Viaje en Avión",
            "texto": "Ese momento tan esperado en el que volemos juntos rumbo a Lima, listos para despegar hacia una aventura inolvidable y atesorar recuerdos que se quedarán grabados para siempre en nuestro corazón."
        },
        {
            "icono": "🎸🎤✨",
            "titulo": "El Concierto de Airbag",
            "texto": "Imaginarnos los dos cantando a todo pulmón en el concierto de Airbag, dejándonos llevar por canciones como «Pensamientos», sintiendo que en cada letra tú lees los míos y yo leo los tuyos en una conexión perfecta."
        },
        {
            "icono": "🌊🌙🏨",
            "titulo": "La Vista desde el Airbnb",
            "texto": "Regresar del concierto en la noche, abrir la ventana y disfrutar juntos de la hermosa vista al mar desde nuestro Airbnb, soñando con que la luna nos acompañe en una de esas charlas íntimas que se quedan flotando en el tiempo."
        },
        {
            "icono": "🏖️👣✨",
            "titulo": "Caminar en la Orilla del Mar",
            "texto": "Caminar descalzos por la orilla de la playa, ya sea bajo la luz de la luna al terminar el concierto o esperando juntos las primeras luces del amanecer a la mañana siguiente... con la firme fe de que la emoción no nos dejará dormir."
        }
    ]

    # Estado de la navegación: -1 = Bienvenida, 0..3 = Flores, 4 = Planes Futuros, 5 = Carta Final
    estado = {'flor': -1, 'petalo': 0, 'futuro_idx': 0}

    # Botón Flotante para Controlar la Música (Sin errores de atributos)
    with ui.row().classes('fixed top-3 right-3 z-50'):
        with ui.button(on_click=lambda: ui.run_javascript('toggleAudio()')) \
                .props('flat round size=sm') \
                .classes('bg-slate-800/80 text-emerald-300 border border-emerald-500/40 px-3 py-1 text-xs rounded-full shadow-lg backdrop-blur-md'):
            ui.html('<span id="music-text-label">🎵 Airbag - Pensamientos: On</span>')

    with ui.column().classes('w-full min-h-screen items-center justify-center p-3 bg-slate-950'):
        
        @ui.refreshable
        def render_contenido():
            f_idx = estado['flor']
            p_idx = estado['petalo']
            fut_idx = estado['futuro_idx']

            with ui.column().classes('items-center text-center w-full max-w-sm transition-all duration-300'):
                if f_idx == -1:
                    # --- Pantalla de Bienvenida ---
                    with ui.column().classes('items-center text-center bg-slate-900/95 backdrop-blur-xl p-6 rounded-3xl shadow-2xl border border-emerald-500/30 w-full text-white'):
                        ui.label('🌻 🌹 🌷 💮').classes('text-3xl mb-2 tracking-widest')
                        ui.label('JARDÍN DE RECUERDOS').classes('text-emerald-400 font-semibold tracking-wider text-xs uppercase')
                        ui.label('¡Feliz Cumpleaños, Jasmín!').classes('text-2xl font-bold mt-2 font-serif')
                        ui.label('Un detalle especial preparado con mucho cariño. Entra al jardín para descubrir cada flor, sus recuerdos y nuestros próximos momentos por compartir.').classes('text-gray-300 mt-3 text-xs leading-relaxed')
                        
                        def entrar_y_reproducir():
                            ui.run_javascript('playMusic()')
                            cambiar_flor(0, 0)

                        btn_bienvenida = ui.button('ENTRAR AL JARDÍN 🌿', on_click=entrar_y_reproducir).classes('mt-5 w-full py-3 rounded-2xl shadow-lg')
                        btn_bienvenida.style('background-color: #059669 !important; color: #ffffff !important; font-weight: bold;')

                elif 0 <= f_idx < len(jardin):
                    # --- Pantalla de la Flor y sus Pétalos ---
                    flor_actual = jardin[f_idx]
                    petalo_actual = flor_actual['petalos'][p_idx]

                    with ui.column().classes(f'items-center text-center w-full bg-slate-900/95 backdrop-blur-xl p-4 rounded-3xl shadow-2xl border {flor_actual["borde_tarjeta"]} text-white'):
                        
                        # Cabecera
                        with ui.row().classes('justify-between w-full items-center mb-1 px-1'):
                            ui.label(f'Flor {f_idx + 1} de {len(jardin)}').classes('text-xs font-bold text-gray-400 uppercase')
                            ui.badge(flor_actual['nombre'], color=None).classes(f'text-xs font-bold px-2 py-0.5 rounded {flor_actual["badge_bg"]}')

                        # FLOR CENTRAL GIGANTE FLOTANTE
                        ui.label(flor_actual['flor']).classes('text-8xl my-2 central-flower-3d')

                        ui.label(flor_actual['nombre']).classes(f'text-2xl font-bold font-serif ' + flor_actual['color_texto'])
                        ui.badge(flor_actual['subtitulo'], color=None).classes(flor_actual['badge_bg'] + ' font-medium mt-1 mb-3 text-xs px-3 py-1 rounded-full')

                        # SELECTOR DE PÉTALOS
                        ui.label('👇 Toca un pétalo para ver su recuerdo:').classes('text-xs text-gray-300 mb-2')
                        
                        with ui.column().classes('w-full gap-1.5 mb-3'):
                            for idx, pt in enumerate(flor_actual['petalos']):
                                if idx == p_idx:
                                    estilo_btn = f'background-color: {flor_actual["color_activo"]} !important; color: {flor_actual["color_texto_activo"]} !important; font-weight: bold; box-shadow: 0 4px 12px rgba(0,0,0,0.3);'
                                else:
                                    estilo_btn = f'background-color: {flor_actual["color_inactivo"]} !important; color: #ffffff !important; border: 1px solid {flor_actual["color_activo"]};'
                                
                                def crear_accion(i=idx):
                                    return lambda: seleccionar_petalo(i)

                                b = ui.button(pt['parte'], on_click=crear_accion()).classes('petal-btn w-full py-2.5 rounded-xl text-xs font-medium')
                                b.style(estilo_btn)

                        # TARJETA DEL RECUERDO
                        with ui.card().classes(f'w-full bg-white/95 text-gray-900 border-2 {flor_actual["tarjeta_recuerdo"]} p-3.5 rounded-2xl mb-3 shadow-inner'):
                            with ui.row().classes('justify-between w-full items-center mb-1'):
                                ui.label(petalo_actual['parte']).classes('text-xs font-bold uppercase text-gray-700')
                                ui.label(f'{p_idx + 1} / {len(flor_actual["petalos"])}').classes('text-xs text-gray-400')
                            
                            ui.label(petalo_actual['titulo']).classes('text-sm font-bold text-gray-800 mb-1 font-serif')
                            ui.label(petalo_actual['texto']).classes('text-gray-600 text-xs leading-relaxed text-left')

                        # Botones de navegación inferiores
                        with ui.row().classes('justify-between w-full gap-2 mt-1'):
                            btn_ant = ui.button('⬅️ Anterior', on_click=lambda: cambiar_flor(f_idx - 1, 0) if f_idx > 0 else cambiar_flor(-1, 0)).classes('px-3 py-2 rounded-xl text-xs flex-1')
                            btn_ant.style('background-color: rgba(255,255,255,0.15) !important; color: #ffffff !important;')

                            btn_sig = ui.button('Siguiente flor ➡️', on_click=lambda: avanzar_flor(f_idx)).classes('px-3 py-2 rounded-xl text-xs flex-1 shadow')
                            btn_sig.style(f'background-color: {flor_actual["color_activo"]} !important; color: {flor_actual["color_texto_activo"]} !important; font-weight: bold;')

                elif f_idx == len(jardin):
                    # --- CUADRO DE PLANES Y SUEÑOS FUTUROS ---
                    plan_actual = futuro[fut_idx]

                    with ui.column().classes('items-center text-center w-full bg-slate-900/95 backdrop-blur-xl p-5 rounded-3xl shadow-2xl border border-sky-500/40 text-white'):
                        
                        # Cabecera
                        with ui.row().classes('justify-between w-full items-center mb-1 px-1'):
                            ui.label(f'Sueño {fut_idx + 1} de {len(futuro)}').classes('text-xs font-bold text-sky-400 uppercase tracking-wider')
                            ui.badge('Nuestros Próximos Pasos ✈️', color=None).classes('text-xs font-bold px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-500/40')

                        # LOGO EMOJI 3D VIBRANTE
                        ui.label(plan_actual['icono']).classes('text-7xl my-3 central-flower-3d')

                        ui.label(plan_actual['titulo']).classes('text-2xl font-bold font-serif text-sky-200 mb-3')

                        # BOTONES SELECTORES DE PLANES FUTUROS
                        with ui.row().classes('w-full justify-center gap-1.5 mb-3'):
                            for idx, f_item in enumerate(futuro):
                                if idx == fut_idx:
                                    b_st = 'background-color: #38bdf8 !important; color: #0f172a !important; font-weight: bold;'
                                else:
                                    b_st = 'background-color: rgba(255,255,255,0.1) !important; color: #ffffff !important; border: 1px solid #38bdf8;'
                                
                                def acc_fut(i=idx):
                                    return lambda: seleccionar_futuro(i)

                                b_f = ui.button(f'0{idx+1}', on_click=acc_fut()).classes('px-3 py-1.5 rounded-lg text-xs')
                                b_f.style(b_st)

                        # TARJETA DEL SUEÑO
                        with ui.card().classes('w-full bg-white/95 text-gray-900 border-2 border-sky-400 p-4 rounded-2xl mb-3 shadow-inner'):
                            ui.label(plan_actual['titulo']).classes('text-sm font-bold text-sky-900 mb-1.5 font-serif uppercase tracking-wide')
                            ui.label(plan_actual['texto']).classes('text-gray-700 text-xs sm:text-sm leading-relaxed text-left')

                        # Botones de navegación inferiores
                        with ui.row().classes('justify-between w-full gap-2 mt-1'):
                            btn_ant = ui.button('⬅️ Volver al Jazmín', on_click=lambda: cambiar_flor(3, 2)).classes('px-3 py-2 rounded-xl text-xs flex-1')
                            btn_ant.style('background-color: rgba(255,255,255,0.15) !important; color: #ffffff !important;')

                            btn_sig = ui.button('Ver Carta Final 💌', on_click=lambda: ir_a_carta_final()).classes('px-3 py-2 rounded-xl text-xs flex-1 shadow')
                            btn_sig.style('background-color: #38bdf8 !important; color: #0f172a !important; font-weight: bold;')

                elif f_idx == len(jardin) + 1:
                    # --- Carta de Cumpleaños y Cierre Especial (Canasta con 4 Flores) ---
                    with ui.column().classes('items-center text-center bg-slate-900/95 backdrop-blur-xl p-5 rounded-3xl shadow-2xl border border-emerald-500/40 w-full text-white'):
                        
                        # CANASTA DE LAS 4 FLORES Y ADORNO BRILLANTE
                        ui.label('🧺🌻🌹🌷💮✨').classes('text-4xl mb-2 central-flower-3d')
                        ui.label('Para alguien inolvidable...').classes('text-emerald-400 font-semibold text-xs uppercase tracking-wider')
                        ui.label('Carta de Cumpleaños y Cierre Especial').classes('text-lg font-bold mt-1 font-serif text-emerald-200')
                        
                        ui.separator().classes('my-2 w-24 bg-emerald-500/50')
                        
                        # PÁRRAFOS DE LA CARTA SINCERA Y EMOTIVA
                        with ui.column().classes('text-gray-300 text-xs leading-relaxed gap-2 text-left my-1 max-h-80 overflow-y-auto px-1'):
                            ui.label('Sé que hace poco me pediste que ya no tuviera estos gestos o detalles por todo lo que conversamos, pero en un día tan especial como tu cumpleaños, no podía dejar pasar la oportunidad de entregarte este humilde detalle. Es una manera distinta de mostrarte un poquito de todo lo que guarda mi corazón: el corazón de alguien que tal vez en su momento pareció un poco frío, pero que por dentro está lleno de calidez y de sentimientos genuinos por expresarte.')
                            
                            ui.label('Sé también que me dijiste que estabas conociendo a alguien más y escuché con atención cada una de las palabras que salieron de tus labios; sin embargo, al mirarte a los ojos, sentí que guardaban una historia diferente a lo que decías. Ese día había miles de cosas que quería decirte, pero me quedé helado y solo pude pronunciar una fracción de todo lo que sentía.')
                            
                            ui.label('Tal vez el Anthony del pasado no fue todo lo que esperabas por cómo solía ser, pero guardo la esperanza de que Nikelson pueda mostrarte una versión diferente, una que aún no has terminado de conocer. Y si quizás Jasmin no lo llega a ver del todo, tal vez Isabel sí lo haga con el tiempo. Pero entiendo que todo es cuestión de tiempo; por ahora acepto y respeto nuestra amistad de corazón. Lo que más me importa hoy es que pases un cumpleaños maravilloso junto a tu familia y a las personas que más amas.')
                            
                            ui.label('Espero sinceramente que este pequeño detalle te llegue al alma. Te deseo con todo mi corazón un ¡Muy Feliz Cumpleaños!, porque sé perfectamente lo especial e importante que es este día para ti.').classes('font-medium text-emerald-300')
                        
                        with ui.row().classes('justify-between w-full mt-4 gap-2'):
                            btn_volver = ui.button('VOLVER AL JARDÍN', on_click=lambda: cambiar_flor(3, 2)).classes('px-3 py-2 rounded-xl text-xs flex-1')
                            btn_volver.style('background-color: rgba(255,255,255,0.15) !important; color: #ffffff !important;')

                            btn_reiniciar = ui.button('REINICIAR ✨', on_click=lambda: cambiar_flor(-1, 0)).classes('px-3 py-2 rounded-xl text-xs flex-1 shadow')
                            btn_reiniciar.style('background-color: #059669 !important; color: #ffffff !important; font-weight: bold;')

        def cambiar_flor(f, p):
            estado['flor'] = f
            estado['petalo'] = p
            estado['futuro_idx'] = 0
            render_contenido.refresh()

        def seleccionar_petalo(p_idx):
            estado['petalo'] = p_idx
            render_contenido.refresh()

        def seleccionar_futuro(f_idx):
            estado['futuro_idx'] = f_idx
            render_contenido.refresh()

        def ir_a_carta_final():
            estado['flor'] = len(jardin) + 1
            render_contenido.refresh()

        def avanzar_flor(f_idx):
            if f_idx < len(jardin) - 1:
                cambiar_flor(f_idx + 1, 0)
            else:
                estado['flor'] = len(jardin)
                estado['futuro_idx'] = 0
                render_contenido.refresh()

        render_contenido()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(
        title="Un jardín para Jazmín",
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 8080)),
        reload=False,
        show=False,
    )
