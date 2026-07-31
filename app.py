import datetime
import pandas as pd
import streamlit as st

# --- 1. НАСТРОЙКИ СТРАНИЦЫ И ULTRA-MODERN UI/UX ---
st.set_page_config(
    page_title="SHKILKA | Next-Gen Education",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
    /* Полное сокрытие лишних элементов */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}

    /* 🔒 ЖЕСТКАЯ БЛОКИРОВКА И ФИКСАЦИЯ САЙДБАРА (запрет на сворачивание и скрытие) */
    section[data-testid="stSidebar"] {
        width: 300px !important;
        min-width: 300px !important;
        max-width: 300px !important;
        background: #ffffff !important;
        border-right: 1px solid rgba(226, 232, 240, 0.8);
        box-shadow: 10px 0 30px rgba(0, 0, 0, 0.02);
        transform: none !important;
        visibility: visible !important;
    }

    /* Уменьшение вертикальных отступов между элементами в сайдбаре (сближение кнопок) */
    section[data-testid="stSidebar"] div[data-testid="stVerticalBlock"] {
        gap: 0.35rem !important;
    }

    /* Убираем все возможные триггеры сворачивания и стандартные шевроны/кнопки управления сайдбаром */
    button[kind="header"], 
    button[data-testid="baseButton-header"],
    [data-testid="collapsedControl"],
    [data-testid="stSidebarCollapseButton"],
    [data-testid="stSidebarCollapsedControl"],
    [data-testid="stSidebarContent"] button[kind="headerNoPadding"],
    button[aria-label="Collapse sidebar"],
    button[aria-label="Open sidebar"],
    button[title="Collapse sidebar"],
    button[title="Open sidebar"],
    .stSidebarNavItems {
        display: none !important;
    }

    /* Фикс для главного контейнера, чтобы контент не смещался из-за зафиксированного сайдбара */
    .main .block-container {
        max-width: 100% !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }

    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    .stApp {
        background: #f8fafc;
        color: #0f172a;
        font-family: 'Plus Jakarta Sans', sans-serif;
    }

    /* Стеклянные премиальные карточки (Glassmorphism / Neumorphism soft) */
    div[data-testid="stVerticalBlock"] > div > div > div[data-testid="stVerticalBlock"], 
    div[data-testid="stForm"],
    div[data-testid="stExpander"] {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(20px);
        border-radius: 24px !important;
        border: 1px solid rgba(255, 255, 255, 1) !important;
        box-shadow: 0 20px 40px -15px rgba(15, 23, 42, 0.05), 0 0 1px 1px rgba(226, 232, 240, 0.6);
        padding: 32px;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    div[data-testid="stVerticalBlock"] > div > div > div[data-testid="stVerticalBlock"]:hover {
        box-shadow: 0 30px 60px -20px rgba(79, 70, 229, 0.08), 0 0 1px 1px rgba(99, 102, 241, 0.2);
    }

    /* Футуристичные кнопки с неоновым градиентом */
    div.stButton > button:first-child {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        color: white;
        border: none;
        border-radius: 16px;
        padding: 14px 28px;
        font-weight: 700;
        font-size: 0.95rem;
        letter-spacing: -0.01em;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 20px 35px -5px rgba(168, 85, 247, 0.5);
    }

    /* Кнопка-ссылка "Подключиться" — единый стиль с обычными кнопками */
    div.stLinkButton > a {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 16px !important;
        padding: 14px 28px !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        letter-spacing: -0.01em;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4);
        justify-content: center;
    }
    div.stLinkButton > a:hover {
        transform: translateY(-3px) scale(1.01);
        box-shadow: 0 20px 35px -5px rgba(168, 85, 247, 0.5);
        color: white !important;
    }

    /* Навигация в сайдбаре */
    .menu-active div.stButton > button:first-child {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%) !important;
        color: white !important;
        box-shadow: 0 10px 25px -5px rgba(99, 102, 241, 0.4);
        width: 100%;
        text-align: left;
        border-radius: 16px;
        font-weight: 700;
    }
    .menu-inactive div.stButton > button:first-child {
        background: transparent !important;
        color: #64748b !important;
        box-shadow: none !important;
        width: 100%;
        text-align: left;
        font-weight: 600;
        border-radius: 16px;
    }
    .menu-inactive div.stButton > button:first-child:hover {
        background: #f1f5f9 !important;
        color: #6366f1 !important;
        transform: translateX(4px) !important;
    }

    /* Второстепенная кнопка */
    .btn-secondary div.stButton > button:first-child {
        background: #f1f5f9;
        color: #475569;
        box-shadow: none;
    }
    .btn-secondary div.stButton > button:first-child:hover {
        background: #e2e8f0;
        color: #0f172a;
        transform: none;
    }

    /* Карточка-рамка для занятия в расписании ученика */
    .lesson-card {
        border: 1px solid #e2e8f0 !important;
        border-radius: 20px !important;
        background: rgba(255, 255, 255, 0.9) !important;
    }

    /* Эстетичные инпуты */
    .stTextInput > div > div > input, .stDateInput > div > div > input, .stTimeInput > div > div > input, .stTextArea textarea {
        background-color: #f8fafc;
        color: #0f172a;
        border: 1px solid #e2e8f0;
        border-radius: 16px;
        padding: 14px 18px;
        font-weight: 500;
    }
    .stTextInput > div > div > input:focus, .stTextArea textarea:focus {
        border-color: #6366f1;
        box-shadow: 0 0 0 4px rgba(99, 102, 241, 0.12);
        background-color: #ffffff;
    }

    h1, h2, h3 {
        letter-spacing: -0.03em;
        font-weight: 800;
    }
</style>
""",
    unsafe_allow_html=True,
)

# --- 2. ИНИЦИАЛИЗАЦИЯ БАЗЫ ДАННЫХ И СОСТОЯНИЯ ---
if "users" not in st.session_state:
    st.session_state.users = {
        "admin": {
            "pass": "admin",
            "role": "admin",
            "name": "Преподаватель Элитный",
        },
        "student1": {
            "pass": "123",
            "role": "student",
            "name": "Алексей Учеников",
            "status": "Цель: Сдать на 90+ баллов 🚀",
            "avatar": "👨‍💻",
        },
        "student2": {
            "pass": "321",
            "role": "student",
            "name": "Дарья Отличница",
            "status": "Изучаю высшую математику ✨",
            "avatar": "👩‍🎓",
        },
    }

if "courses" not in st.session_state:
    st.session_state.courses = {
        1: {
            "title": "ИЗИ БУСТ подготовка к ЕГЭ по физике",
            "desc": "ДЗ на курсе",
        },
        2: {
            "title": "ИЗИ БУСТ подготовка к ЕГЭ по математике",
            "desc": "ДЗ на курсе",
        },
        3: {
            "title": "Курс подготовки к ЕГЭ по математике (2025-2026)",
            "desc": "ДЗ на курсе",
        },
    }

if "course_assignments" not in st.session_state:
    st.session_state.course_assignments = {
        "student1": [1, 2, 3],
        "student2": [1, 2],
    }

if "variants" not in st.session_state:
    st.session_state.variants = {}
if "student_progress" not in st.session_state:
    st.session_state.student_progress = {}
if "assignments" not in st.session_state:
    st.session_state.assignments = {}
if "schedule" not in st.session_state:
    st.session_state.schedule = {}
if "messages" not in st.session_state:
    st.session_state.messages = {}
if "manual_checks" not in st.session_state:
    st.session_state.manual_checks = {}

# Система пробных экзаменов
if "mock_templates" not in st.session_state:
    st.session_state.mock_templates = {}

if "mock_exams" not in st.session_state:
    st.session_state.mock_exams = {}

if "solving_mock_id" not in st.session_state:
    st.session_state.solving_mock_id = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.current_user = None

if "solving_v_id" not in st.session_state:
    st.session_state.solving_v_id = None

if "solving_course_id" not in st.session_state:
    st.session_state.solving_course_id = None

if "current_menu" not in st.session_state:
    st.session_state.current_menu = None


def get_student_xp_and_stats(student_id):
    xp, solved, failed = 0, 0, 0
    prog = st.session_state.student_progress.get(student_id, {})
    for v_id, v_data in prog.items():
        for t_state in v_data.get("task_states", {}).values():
            if t_state.get("status") == "solved":
                solved += 1
                att = t_state.get("attempts_left", 3)
                if att == 3:
                    xp += 100  # С первого раза
                elif att == 2:
                    xp += 75  # Со второго раза
                else:
                    xp += 50  # С третьего раза
            elif t_state.get("status") == "failed":
                failed += 1
                xp += 25  # Неверно решено
    return xp, solved, failed


def get_rank(xp):
    if xp < 200:
        return "Новичок 🌱"
    elif xp < 500:
        return "Продвинутый ⚡"
    elif xp < 1000:
        return "Мастер 🔮"
    else:
        return "Легенда SHKILKA 👑"


# --- 3. АВТОРИЗАЦИЯ ---
def login(username, password):
    if (
            username in st.session_state.users
            and st.session_state.users[username]["pass"] == password
    ):
        st.session_state.logged_in = True
        st.session_state.current_user = username
        st.session_state.solving_v_id = None
        st.session_state.solving_course_id = None
        st.session_state.solving_mock_id = None
        st.session_state.current_menu = (
            "Профиль и достижения 👤"
            if st.session_state.users[username]["role"] == "student"
            else "Лидерборд"
        )
        st.rerun()
    else:
        st.error("Неверный логин или пароль")


if not st.session_state.logged_in:
    st.markdown(
        '<div style="margin-top: 8vh;"></div>', unsafe_allow_html=True
    )
    st.markdown(
        '<h1 style="text-align: center; font-weight: 900; background:'
        " linear-gradient(135deg, #6366f1, #a855f7, #ec4899);"
        " -webkit-background-clip: text; -webkit-text-fill-color: transparent;"
        ' font-size: 4rem;">SHKILKA</h1>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<p style="text-align: center; color: #64748b; font-size: 1.2rem;'
        ' margin-top: -10px; margin-bottom: 40px; font-weight: 600;">Интерактивная'
        " образовательная экосистема нового поколения</p>",
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1.5, 2, 1.5])
    with col2:
        with st.container():
            st.markdown(
                "<h3 style='text-align: center; margin-bottom: 24px;'>Вход в"
                " систему</h3>",
                unsafe_allow_html=True,
            )
            u_in = st.text_input("Логин", placeholder="admin или student1")
            p_in = st.text_input("Пароль", type="password", placeholder="••••••••")
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Войти в экосистему", use_container_width=True):
                login(u_in, p_in)
    st.stop()

user_info = st.session_state.users[st.session_state.current_user]
role = user_info["role"]
name = user_info["name"]

if st.session_state.current_menu is None:
    st.session_state.current_menu = (
        "Профиль и достижения 👤" if role == "student" else "Лидерборд"
    )

# --- 4. САЙДБАР ---
with st.sidebar:
    st.markdown(
        '<h1 style="text-align: center; font-weight: 950; background:'
        " linear-gradient(135deg, #6366f1, #ec4899);"
        " -webkit-background-clip: text; -webkit-text-fill-color: transparent;"
        ' margin-bottom: 16px; font-size: 2.8rem;">SHKILKA</h1>',
        unsafe_allow_html=True,
    )

    if role == "student":
        avatar_icon = user_info.get("avatar", "🚀")
        is_profile_selected = (
                st.session_state.current_menu == "Профиль и достижения 👤"
        )
        profile_css = "menu-active" if is_profile_selected else "menu-inactive"
        st.markdown(f'<div class="{profile_css}">', unsafe_allow_html=True)
        if st.button(
                f"{avatar_icon}  {name}", key="nav_profile_btn", use_container_width=True
        ):
            st.session_state.current_menu = "Профиль и достижения 👤"
            st.session_state.solving_v_id = None
            st.session_state.solving_course_id = None
            st.session_state.solving_mock_id = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #f8fafc, #f1f5f9); padding: 16px; border-radius: 20px; margin-bottom: 15px; border: 1px solid #e2e8f0; box-shadow: inset 0 2px 4px rgba(0,0,0,0.01);">
                <div style="display: flex; align-items: center;">
                    <div style="background: linear-gradient(135deg, #6366f1, #a855f7); color: white; width: 48px; height: 48px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: 1.3rem; margin-right: 14px; box-shadow: 0 10px 20px -5px rgba(99, 102, 241, 0.4);">👑</div>
                    <div style="overflow: hidden;">
                        <div style="font-weight: 700; font-size: 0.95rem; color: #0f172a; white-space: nowrap; text-overflow: ellipsis;">{name}</div>
                        <div style="font-size: 0.78rem; color: #6366f1; font-weight: 600;">Преподаватель</div>
                    </div>
                </div>
            </div>
        """,
            unsafe_allow_html=True,
        )

    nav_items = (
        ["Мои задания", "Расписание", "Пробные экзамены", "Сообщения ✉️"]
        if role == "student"
        else [
            "Лидерборд",
            "Управление курсами 📚",
            "Конструктор вариантов ✨",
            "Отправка заданий",
            "Пробные экзамены 📝",
            "Проверка заданий 📝",
            "Сообщения ✉️",
            "Расписание",
            "Ученики",
        ]
    )

    for item in nav_items:
        is_selected = st.session_state.current_menu == item
        css_class = "menu-active" if is_selected else "menu-inactive"
        st.markdown(f'<div class="{css_class}">', unsafe_allow_html=True)
        if st.button(item, key=f"nav_{item}", use_container_width=True):
            st.session_state.current_menu = item
            st.session_state.solving_v_id = None
            st.session_state.solving_course_id = None
            st.session_state.solving_mock_id = None
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        """
          <div style="background: linear-gradient(135deg, #eef2ff 0%, #fae8ff 100%); padding: 14px; border-radius: 20px; margin-bottom: 10px; border: 1px solid #e0e7ff;">
              <div style="font-weight: 700; font-size: 0.85rem; color: #6366f1; margin-bottom: 4px;">⚡ PRO Ecosystem</div>
              <div style="font-size: 0.75rem; color: #64748b; line-height: 1.4;">Интерфейс надежно зафиксирован.</div>
          </div>
      """,
        unsafe_allow_html=True,
    )

    st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
    if st.button("Выйти из системы", use_container_width=True):
        st.session_state.logged_in = False
        st.session_state.current_user = None
        st.session_state.current_menu = None
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

menu = st.session_state.current_menu

# --- 5. ЛОГИКА ОТОБРАЖЕНИЯ ---

if role == "admin":
    if menu == "Лидерборд":
        st.title("Лидерборд учеников 🏆")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Глобальный рейтинг успеваемости и опыта учащихся</p>",
            unsafe_allow_html=True,
        )

        students = {
            uid: uinfo
            for uid, uinfo in st.session_state.users.items()
            if uinfo["role"] == "student"
        }
        if not students:
            st.info("Нет зарегистрированных учеников.")
        else:
            lb_data = []
            for s_id, s_info in students.items():
                xp, solved, failed = get_student_xp_and_stats(s_id)
                lb_data.append({
                    "Ученик": s_info["name"],
                    "XP": xp,
                    "Ранг": get_rank(xp),
                    "Решено": solved,
                    "Ошибок": failed,
                })
            df_lb = (
                pd.DataFrame(lb_data)
                .sort_values(by="XP", ascending=False)
                .reset_index(drop=True)
            )
            df_lb.index += 1
            if df_lb["XP"].sum() == 0:
                st.info("Ученики еще не заработали опыт.")
            else:
                st.dataframe(df_lb, use_container_width=True)
                st.bar_chart(df_lb.set_index("Ученик")["XP"], color="#6366f1")

    elif menu == "Управление курсами 📚":
        st.title("Управление курсами 📚")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Создавайте курсы и управляйте доступом учеников к ним</p>",
            unsafe_allow_html=True,
        )

        with st.form("create_course_form", clear_on_submit=True):
            c_title = st.text_input(
                "Название курса",
                placeholder="Например: ИЗИ БУСТ подготовка к ЕГЭ по информатике",
            )
            c_desc = st.text_input("Описание / подзаголовок", placeholder="ДЗ на курсе")
            submitted = st.form_submit_button("Создать новый курс")
            if submitted and c_title:
                new_cid = (
                    max(st.session_state.courses.keys()) + 1
                    if st.session_state.courses
                    else 1
                )
                st.session_state.courses[new_cid] = {"title": c_title, "desc": c_desc}
                st.toast("Курс успешно создан!")
                st.rerun()

        st.markdown("---")
        st.markdown("### Существующие курсы")
        if not st.session_state.courses:
            st.info("Нет созданных курсов.")
        else:
            students_dict = {
                uid: uinfo
                for uid, uinfo in st.session_state.users.items()
                if uinfo["role"] == "student"
            }
            for cid, cdata in list(st.session_state.courses.items()):
                with st.container():
                    col_c1, col_c2 = st.columns([4, 1])
                    col_c1.markdown(f"#### {cdata['title']}")
                    col_c1.write(f"Описание: {cdata['desc']}")

                    current_enrolled = [
                        s_id
                        for s_id, c_list in st.session_state.course_assignments.items()
                        if cid in c_list
                    ]
                    selected_enrolled = col_c1.multiselect(
                        "Ученики, имеющие доступ к курсу",
                        options=list(students_dict.keys()),
                        default=current_enrolled,
                        format_func=lambda x: students_dict[x]["name"],
                        key=f"course_students_{cid}",
                    )

                    for s_id in students_dict.keys():
                        if s_id not in st.session_state.course_assignments:
                            st.session_state.course_assignments[s_id] = []
                        if s_id in selected_enrolled:
                            if cid not in st.session_state.course_assignments[s_id]:
                                st.session_state.course_assignments[s_id].append(cid)
                        else:
                            if cid in st.session_state.course_assignments[s_id]:
                                st.session_state.course_assignments[s_id].remove(cid)

                    if col_c2.button("🗑️ Удалить курс", key=f"del_course_{cid}"):
                        del st.session_state.courses[cid]
                        st.rerun()
                    st.markdown(
                        '<hr style="margin: 20px 0; border: none; border-top: 1px solid'
                        ' #cbd5e1;">',
                        unsafe_allow_html=True,
                    )

    elif menu == "Конструктор вариантов ✨":
        st.title("Конструктор вариантов 🛠️")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Создавайте тесты с фото к заданиям и пояснениям</p>",
            unsafe_allow_html=True,
        )

        if "builder_tasks" not in st.session_state:
            st.session_state.builder_tasks = []
        if "builder_title" not in st.session_state:
            st.session_state.builder_title = ""

        st.session_state.builder_title = st.text_input(
            "Название домашнего задания / варианта",
            value=st.session_state.builder_title,
            placeholder="Например: ДЗ №1 по кинематике",
        )

        if st.session_state.courses:
            course_options = list(st.session_state.courses.keys())
            selected_course_for_variant = st.selectbox(
                "Привязать к курсу",
                options=course_options,
                format_func=lambda cid: st.session_state.courses[cid]["title"],
            )
        else:
            selected_course_for_variant = None
            st.warning(
                "Сначала создайте хотя бы один курс в разделе 'Управление курсами'."
            )

        st.markdown("---")
        st.markdown("### Список заданий в варианте")

        if not st.session_state.builder_tasks:
            st.info("Вариант пока пустой. Добавьте первое задание ниже 👇")
        else:
            for idx, task in enumerate(st.session_state.builder_tasks):
                with st.container():
                    col_h1, col_h2 = st.columns([5, 1])
                    col_h1.markdown(
                        f"#### Задание #{idx + 1}"
                        f" ({'Ручная проверка' if task.get('is_manual') else 'Автопроверка'})"
                    )
                    if col_h2.button("🗑️ Удалить", key=f"del_bt_{idx}"):
                        st.session_state.builder_tasks.pop(idx)
                        st.rerun()

                    task["question_text"] = st.text_input(
                        "Текст вопроса / условие",
                        value=task.get("question_text", ""),
                        key=f"q_txt_{idx}",
                    )

                    if task.get("task_img"):
                        st.image(
                            task["task_img"], caption="Текущее фото к заданию", width=250
                        )
                        if st.button("🗑️ Удалить фото задания", key=f"del_t_img_{idx}"):
                            task["task_img"] = None
                            st.rerun()

                    new_t_img = st.file_uploader(
                        f"📸 Заменить или добавить фото к заданию #{idx + 1}",
                        type=["png", "jpg", "jpeg"],
                        key=f"task_img_file_{idx}",
                    )
                    if new_t_img:
                        task["task_img"] = new_t_img.getvalue()

                    task["answer"] = st.text_input(
                        "Правильный ответ (для автопроверки)",
                        value=task.get("answer", ""),
                        key=f"q_ans_{idx}",
                    )
                    task["is_manual"] = st.checkbox(
                        "Требуется проверка преподавателем (развернутый ответ / эссе)",
                        value=task.get("is_manual", False),
                        key=f"q_man_{idx}",
                    )
                    task["expl_text"] = st.text_area(
                        "Разбор решения",
                        value=task.get("expl_text", ""),
                        key=f"q_exp_{idx}",
                    )

                    if task.get("expl_img"):
                        st.image(
                            task["expl_img"], caption="Текущее фото к разбору", width=250
                        )
                        if st.button("🗑️ Удалить фото разбора", key=f"del_e_img_{idx}"):
                            task["expl_img"] = None
                            st.rerun()

                    new_e_img = st.file_uploader(
                        f"📸 Заменить или добавить фото к разбору #{idx + 1}",
                        type=["png", "jpg", "jpeg"],
                        key=f"expl_img_file_{idx}",
                    )
                    if new_e_img:
                        task["expl_img"] = new_e_img.getvalue()

                    st.markdown("---")

        with st.container():
            st.markdown("#### ➕ Добавить новое задание")
            new_q_text = st.text_input(
                "Текст нового вопроса",
                placeholder="Введите условие задачи...",
                key="new_q_text_input",
            )
            new_img = st.file_uploader(
                "📸 Изображение к заданию (опционально)",
                type=["png", "jpg", "jpeg"],
                key="new_img_uploader",
            )
            new_ans = st.text_input(
                "Правильный ответ (оставьте пустым для ручной проверки)",
                placeholder="Точный ответ...",
                key="new_ans_input",
            )
            new_is_manual = st.checkbox(
                "Проверяется вручную преподавателем", key="new_man_check"
            )
            new_expl = st.text_area(
                "Разбор решения", placeholder="Объяснение...", key="new_expl_textarea"
            )
            new_expl_img = st.file_uploader(
                "📸 Изображение к пояснению (опционально)",
                type=["png", "jpg", "jpeg"],
                key="new_expl_img_uploader",
            )

            if st.button("➕ Добавить задание в вариант", use_container_width=True):
                if new_q_text:
                    st.session_state.builder_tasks.append({
                        "question_text": new_q_text,
                        "task_img": new_img.getvalue() if new_img else None,
                        "answer": new_ans.strip().lower(),
                        "is_manual": new_is_manual,
                        "expl_text": new_expl,
                        "expl_img": new_expl_img.getvalue() if new_expl_img else None,
                    })
                    st.toast("Задание успешно добавлено в конструктор!")
                    st.rerun()
                else:
                    st.error("Заполните текст вопроса.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Сохранить весь вариант в курс", use_container_width=True):
            if (
                    st.session_state.builder_title
                    and st.session_state.builder_tasks
                    and selected_course_for_variant is not None
            ):
                v_id = (
                    max(st.session_state.variants.keys()) + 1
                    if st.session_state.variants
                    else 1
                )
                st.session_state.variants[v_id] = {
                    "title": st.session_state.builder_title,
                    "tasks": st.session_state.builder_tasks,
                    "course_id": selected_course_for_variant,
                }
                st.session_state.builder_tasks = []
                st.session_state.builder_title = ""
                st.toast("Вариант успешно сохранен в выбранный курс! 🎉")
                st.rerun()
            else:
                st.error(
                    "Укажите название варианта, добавьте хотя бы одно задание и выберите"
                    " курс."
                )

    elif menu == "Отправка заданий":
        st.title("Распределение тестов 🚀")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Дополнительное назначение тестов и дедлайнов</p>",
            unsafe_allow_html=True,
        )

        if not st.session_state.variants:
            st.info("Пока нет готовых вариантов. Создайте их в конструкторе.")
        else:
            students_dict = {
                uid: uinfo
                for uid, uinfo in st.session_state.users.items()
                if uinfo["role"] == "student"
            }
            for v_id, v_data in st.session_state.variants.items():
                with st.container():
                    c_title = (
                        st.session_state.courses.get(v_data.get("course_id"), {})
                        .get("title", "Без курса")
                    )
                    st.markdown(
                        f"### {v_data['title']} <span style='font-size: 0.8rem; color:"
                        f" #6366f1;'>({c_title})</span>",
                        unsafe_allow_html=True,
                    )
                    st.write(f"Заданий в варианте: **{len(v_data['tasks'])}**")

                    cd1, cd2 = st.columns(2)
                    d_date = cd1.date_input(
                        "Дедлайн (дата)",
                        datetime.date.today() + datetime.timedelta(days=3),
                        key=f"d_{v_id}",
                    )
                    d_time = cd2.time_input(
                        "Дедлайн (время)", datetime.time(23, 59), key=f"t_{v_id}"
                    )
                    deadline_str = (
                        f"{d_date.strftime('%Y-%m-%d')} {d_time.strftime('%H:%M')}"
                    )

                    selected_st = st.multiselect(
                        "Выберите учеников",
                        options=list(students_dict.keys()),
                        format_func=lambda x: students_dict[x]["name"],
                        key=f"ms_{v_id}",
                    )

                    if st.button("📤 Отправить выбранным ученикам", key=f"snd_{v_id}"):
                        for s_id in selected_st:
                            if s_id not in st.session_state.assignments or not isinstance(
                                    st.session_state.assignments[s_id], dict
                            ):
                                st.session_state.assignments[s_id] = {}
                            st.session_state.assignments[s_id][v_id] = deadline_str
                        st.toast(f"Вариант успешно отправлен!")

                    st.markdown(
                        '<div class="btn-secondary" style="margin-top: 10px;">',
                        unsafe_allow_html=True,
                    )
                    if st.button("Удалить вариант навсегда", key=f"del_v_{v_id}"):
                        del st.session_state.variants[v_id]
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)

    elif menu == "Пробные экзамены 📝":
        st.title("Конструктор и отправка пробных экзаменов 📝")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Создавайте пробники с таймером и картинками, настраивайте"
            " отправку</p>",
            unsafe_allow_html=True,
        )

        if "builder_mock_tasks" not in st.session_state:
            st.session_state.builder_mock_tasks = []

        b_num = st.number_input(
            "Номер пробного экзамена", min_value=0, value=0, step=1
        )
        b_title = st.text_input(
            "Название / Подзаголовок варианта",
            placeholder=(
                "Пробный вариант ЕГЭ №0 | РЕЗЕРВ ЕГЭ-2026 | Пробник для оценки"
                " начального уровня знаний"
            ),
        )
        b_desc = st.text_area(
            "Описание карточки пробника",
            placeholder=(
                "Это первый пробник курса. В него входят задания, которые были на"
                " резерве ЕГЭ-2026..."
            ),
        )
        b_timer = st.number_input(
            "Таймер на выполнение (в минутах)", min_value=1, value=180, step=5
        )

        st.markdown("---")
        st.markdown("### Задания в пробном экзамене")

        if not st.session_state.builder_mock_tasks:
            st.info("Список заданий пуст. Добавьте задания ниже.")
        else:
            for idx, m_task in enumerate(st.session_state.builder_mock_tasks):
                with st.container():
                    col_m1, col_m2 = st.columns([5, 1])
                    col_m1.markdown(f"#### Задание №{idx + 1}")
                    col_m1.write(f"Текст: {m_task['question_text']}")
                    if m_task.get("task_img"):
                        col_m1.image(m_task["task_img"], width=250)
                    col_m1.write(
                        "Эталонный ответ (для проверки преподом):"
                        f" {m_task['reference_answer']}"
                    )

                    if col_m2.button("🗑️ Удалить", key=f"del_bm_{idx}"):
                        st.session_state.builder_mock_tasks.pop(idx)
                        st.rerun()
                    st.markdown("---")

        with st.container():
            st.markdown("#### ➕ Добавить задание в пробник")
            t_q_text = st.text_input(
                "Текст вопроса", placeholder="Условие задачи...", key="bm_q_text"
            )
            t_img = st.file_uploader(
                "📸 Картинка к заданию (опционально)",
                type=["png", "jpg", "jpeg"],
                key="bm_img_uploader",
            )
            t_ref_ans = st.text_input(
                "Эталонный ответ (для учителя)",
                placeholder="Правильный ответ...",
                key="bm_ref_ans",
            )

            if st.button("➕ Добавить задание в шаблон", use_container_width=True):
                if t_q_text:
                    st.session_state.builder_mock_tasks.append({
                        "question_text": t_q_text,
                        "task_img": t_img.getvalue() if t_img else None,
                        "reference_answer": t_ref_ans,
                    })
                    st.toast("Задание добавлено в пробник!")
                    st.rerun()
                else:
                    st.error("Заполните текст вопроса.")

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("💾 Сохранить шаблон пробного экзамена", use_container_width=True):
            if st.session_state.builder_mock_tasks:
                m_id = (
                    max(st.session_state.mock_templates.keys()) + 1
                    if st.session_state.mock_templates
                    else 1
                )
                st.session_state.mock_templates[m_id] = {
                    "number": int(b_num),
                    "title": b_title if b_title else f"Пробный вариант ЕГЭ №{b_num}",
                    "description": (
                        b_desc
                        if b_desc
                        else "Постарайтесь прорешать тест за отведенное время."
                    ),
                    "duration_minutes": int(b_timer),
                    "tasks": st.session_state.builder_mock_tasks,
                }
                st.session_state.builder_mock_tasks = []
                st.toast("Шаблон пробного экзамена успешно сохранен! 🎉")
                st.rerun()
            else:
                st.error("Добавьте хотя бы одно задание в пробный экзамен.")

        st.markdown("---")
        st.markdown("### 📤 Отправка пробных экзаменов ученикам")
        if not st.session_state.mock_templates:
            st.info("Нет сохраненных шаблонов пробных экзаменов.")
        else:
            students_dict = {
                uid: uinfo
                for uid, uinfo in st.session_state.users.items()
                if uinfo["role"] == "student"
            }
            for m_id, m_data in list(st.session_state.mock_templates.items()):
                with st.container():
                    col_t1, col_t2 = st.columns([3, 1])

                    default_mock_title = f"Пробный вариант ЕГЭ №{m_data['number']}"
                    current_mock_title = m_data.get("title", default_mock_title)
                    col_t1.markdown(
                        f"#### {current_mock_title} (Время: {m_data['duration_minutes']}"
                        " мин.)"
                    )

                    col_t1.write(f"Заданий: {len(m_data['tasks'])}")

                    selected_st_mock = col_t1.multiselect(
                        "Выберите учеников для отправки",
                        options=list(students_dict.keys()),
                        format_func=lambda x: students_dict[x]["name"],
                        key=f"mock_send_{m_id}",
                    )

                    if col_t1.button(
                            "🚀 Отправить выбранным ученикам", key=f"btn_send_mock_{m_id}"
                    ):
                        for s_id in selected_st_mock:
                            if s_id not in st.session_state.mock_exams:
                                st.session_state.mock_exams[s_id] = []

                            exam_instance = {
                                "template_id": m_id,
                                "number": m_data["number"],
                                "title": m_data.get(
                                    "title", f"Пробный вариант ЕГЭ №{m_data['number']}"
                                ),
                                "description": m_data.get("description", ""),
                                "duration_minutes": m_data["duration_minutes"],
                                "tasks": m_data["tasks"],
                                "student_answers": {},
                                "status": "not_started",
                                "start_time": None,
                                "grade": "",
                                "primary_score": 0,
                                "max_score": len(m_data["tasks"]),
                            }

                            existing_idx = next(
                                (
                                    i
                                    for i, ex in enumerate(st.session_state.mock_exams[s_id])
                                    if ex["number"] == m_data["number"]
                                ),
                                None,
                            )
                            if existing_idx is not None:
                                st.session_state.mock_exams[s_id][existing_idx] = exam_instance
                            else:
                                st.session_state.mock_exams[s_id].append(exam_instance)

                        st.toast(
                            "Пробный экзамен успешно отправлен выбранным ученикам! ⚡"
                        )
                        st.rerun()

                    if col_t2.button("🗑️ Удалить шаблон", key=f"del_mock_tmpl_{m_id}"):
                        del st.session_state.mock_templates[m_id]
                        st.rerun()
                    st.markdown("---")

    elif menu == "Проверка заданий 📝":
        st.title("Проверка заданий и пробных экзаменов 📝")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Проверяйте развернутые ответы, а также выставляйте оценку и"
            " баллы за пробные экзамены</p>",
            unsafe_allow_html=True,
        )

        students_dict = {
            uid: uinfo
            for uid, uinfo in st.session_state.users.items()
            if uinfo["role"] == "student"
        }

        st.markdown("### 📋 Пробные экзамены, ожидающие проверки")
        mock_pending_found = False
        for s_id, s_exams in st.session_state.mock_exams.items():
            s_name = students_dict.get(s_id, {"name": s_id})["name"]
            for ex_idx, ex in enumerate(s_exams):
                if ex.get("status") == "pending_review":
                    mock_pending_found = True
                    with st.container():
                        ex_title = ex.get("title", f"Пробник №{ex['number']}")
                        st.markdown(f"#### Ученик: {s_name} | {ex_title}")
                        st.write("Ответы ученика:")
                        for t_i, t_item in enumerate(ex["tasks"]):
                            ans_val = ex["student_answers"].get(t_i, "Нет ответа")
                            st.write(
                                f"- Задание №{t_i + 1} ({t_item['question_text']}):"
                                f" **{ans_val}** *(Эталон: {t_item['reference_answer']})*"
                            )

                        col_sc1, col_sc2, col_sc3 = st.columns(3)
                        grade_val = col_sc1.text_input(
                            "Оценка за экзамен (например, 5, 4)",
                            value=str(ex.get("grade", "")),
                            key=f"grade_{s_id}_{ex['number']}",
                        )
                        p_score = col_sc2.number_input(
                            "Набрано баллов",
                            min_value=0,
                            max_value=100,
                            value=ex.get("primary_score", 0),
                            key=f"p_score_{s_id}_{ex['number']}",
                        )
                        max_score_val = col_sc3.number_input(
                            "Максимум баллов",
                            min_value=1,
                            max_value=100,
                            value=ex.get("max_score", len(ex["tasks"])),
                            key=f"max_score_{s_id}_{ex['number']}",
                        )

                        if st.button(
                                "📤 Отправить результат ученику",
                                key=f"send_mock_result_{s_id}_{ex['number']}",
                        ):
                            ex["grade"] = grade_val
                            ex["primary_score"] = p_score
                            ex["max_score"] = max_score_val
                            ex["status"] = "graded"
                            st.toast(f"Результаты отправлены ученику!")
                            st.rerun()
                        st.markdown("---")
        if not mock_pending_found:
            st.info("Нет пробных экзаменов, ожидающих проверки.")

        st.markdown("---")
        st.markdown("### 📝 Обычные домашние задания (ручная проверка)")
        pending_found = False
        for s_id, s_prog in st.session_state.student_progress.items():
            s_name = students_dict.get(s_id, {"name": s_id})["name"]
            for v_id, v_data in s_prog.items():
                if v_id in st.session_state.variants:
                    v_title = st.session_state.variants[v_id]["title"]
                    v_tasks = st.session_state.variants[v_id]["tasks"]
                    for t_idx, t_state in v_data.get("task_states", {}).items():
                        if t_state.get("status") == "pending_review":
                            pending_found = True
                            with st.container():
                                st.markdown(f"#### Ученик: {s_name} | Вариант: {v_title}")
                                st.markdown(
                                    f"**Задание #{t_idx + 1}:**"
                                    f" {v_tasks[t_idx].get('question_text', 'Без вопроса')} "
                                )
                                st.info(
                                    f"Ответ ученика: **{t_state.get('user_answer', '')}**"
                                )

                                c_chk1, c_chk2 = st.columns(2)
                                if c_chk1.button(
                                        "✅ Засчитать верно (+100 XP)",
                                        key=f"pass_{s_id}_{v_id}_{t_idx}",
                                ):
                                    t_state["status"] = "solved"
                                    t_state["feedback"] = "right"
                                    st.toast("Ответ одобрен!")
                                    st.rerun()
                                if c_chk2.button(
                                        "❌ Отклонить", key=f"fail_{s_id}_{v_id}_{t_idx}"
                                ):
                                    t_state["status"] = "failed"
                                    t_state["feedback"] = "wrong"
                                    st.toast("Ответ отклонен.")
                                    st.rerun()
        if not pending_found:
            st.info("Нет обычных заданий, ожидающих ручной проверки.")

    elif menu == "Сообщения ✉️":
        st.title("Сообщения от учеников ✉️")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Диалоги и вопросы от учащихся</p>",
            unsafe_allow_html=True,
        )

        students_dict = {
            uid: uinfo
            for uid, uinfo in st.session_state.users.items()
            if uinfo["role"] == "student"
        }
        if not students_dict:
            st.info("Нет зарегистрированных учеников.")
        else:
            target_st = st.selectbox(
                "Выберите ученика для просмотра чата",
                options=list(students_dict.keys()),
                format_func=lambda x: students_dict[x]["name"],
            )

            st.markdown("---")
            user_msgs = st.session_state.messages.get(target_st, [])
            if not user_msgs:
                st.info("История сообщений с этим учеником пуста.")
            else:
                for m in user_msgs:
                    sender_label = (
                        f"👨‍💻 {students_dict[target_st]['name']}"
                        if m["sender"] == "student"
                        else "👨‍🏫 Преподаватель"
                    )
                    st.write(f"**{sender_label}:** {m['text']}")

            st.markdown("---")
            admin_msg = st.text_input(
                "Написать ответ ученику:", key="admin_reply_input"
            )
            if st.button("Отправить ответ ученику"):
                if admin_msg:
                    if target_st not in st.session_state.messages:
                        st.session_state.messages[target_st] = []
                    st.session_state.messages[target_st].append(
                        {"sender": "admin", "text": admin_msg}
                    )
                    st.toast("Ответ успешно отправлен!")
                    st.rerun()

    elif menu == "Расписание":
        st.title("Календарь и расписание преподавателя 📅")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Сводное расписание всех занятий с учениками и управление"
            " графиком</p>",
            unsafe_allow_html=True,
        )

        students_dict = {
            uid: uinfo
            for uid, uinfo in st.session_state.users.items()
            if uinfo["role"] == "student"
        }

        with st.container():
            st.markdown("### ➕ Назначить новое занятие")
            target_student = st.selectbox(
                "Ученик",
                options=list(students_dict.keys()),
                format_func=lambda x: students_dict[x]["name"],
            )
            lesson_title = st.text_input(
                "Тема вебинара / урока", placeholder="Разбор сложных задач..."
            )
            c1, c2 = st.columns(2)
            l_date = c1.date_input("Дата", datetime.date.today())
            l_time = c2.time_input("Время", datetime.time(15, 0))
            l_link = st.text_input(
                "Ссылка на трансляцию / Zoom", placeholder="https://zoom.us/..."
            )

            if st.button("Назначить занятие", use_container_width=True):
                if target_student and lesson_title:
                    if target_student not in st.session_state.schedule:
                        st.session_state.schedule[target_student] = []
                    st.session_state.schedule[target_student].append({
                        "title": lesson_title,
                        "datetime": (
                            f"{l_date.strftime('%Y-%m-%d')} {l_time.strftime('%H:%M')}"
                        ),
                        "link": l_link,
                    })
                    st.toast("Урок успешно добавлен в расписание ученика!")
                    st.rerun()

        st.markdown("---")
        st.markdown("### 📋 Все запланированные занятия преподавателя")

        all_lessons = []
        for s_id, lessons in st.session_state.schedule.items():
            s_name = students_dict.get(s_id, {"name": s_id})["name"]
            for idx, l in enumerate(lessons):
                all_lessons.append({
                    "student_id": s_id,
                    "student_name": s_name,
                    "title": l["title"],
                    "datetime": l["datetime"],
                    "link": l["link"],
                    "index": idx,
                })

        if not all_lessons:
            st.info(
                "В вашем расписании пока нет запланированных занятий с учениками."
            )
        else:
            all_lessons = sorted(all_lessons, key=lambda x: x["datetime"])
            for item in all_lessons:
                with st.container():
                    col_sch1, col_sch2 = st.columns([4, 1])
                    col_sch1.markdown(
                        f"#### 👤 Ученик: {item['student_name']} | 📚 Тема:"
                        f" {item['title']}"
                    )
                    col_sch1.markdown(
                        "📅 Дата и время:"
                        " **<span style='font-size: 1.1rem; font-weight:"
                        f" 800;'>{item['datetime']} (МСК)</span>**",
                        unsafe_allow_html=True,
                    )
                    if item["link"]:
                        col_sch1.markdown(
                            f"🔗 Ссылка на урок: [Подключиться]({item['link']})"
                        )
                    else:
                        col_sch1.write("🔗 Ссылка не указана")

                    st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
                    if col_sch2.button(
                            "🗑️ Отменить урок",
                            key=f"del_lesson_{item['student_id']}_{item['index']}",
                    ):
                        st.session_state.schedule[item["student_id"]].pop(item["index"])
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)

    elif menu == "Ученики":
        st.title("База учеников 👥")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Управление учетными записями учащихся</p>",
            unsafe_allow_html=True,
        )

        with st.form("add_st_form", clear_on_submit=True):
            c1, c2, c3 = st.columns(3)
            new_id = c1.text_input("Логин (ID)")
            new_name = c2.text_input("Имя и Фамилия")
            new_pass = c3.text_input("Пароль", type="password")
            if st.form_submit_button("Зарегистрировать ученика"):
                if new_id and new_name and new_pass:
                    st.session_state.users[new_id] = {
                        "pass": new_pass,
                        "role": "student",
                        "name": new_name,
                        "status": "Ученик SHKILKA",
                        "avatar": "🎓",
                    }
                    st.toast("Ученик успешно добавлен!")
                    st.rerun()

        st.markdown("---")
        for s_id, s_info in st.session_state.users.items():
            if s_info["role"] == "student":
                with st.container():
                    col1, col2 = st.columns([3, 1])
                    col1.markdown(f"**{s_info['name']}** (ID: `{s_id}`)")
                    st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
                    if col2.button("Удалить", key=f"del_st_{s_id}"):
                        del st.session_state.users[s_id]
                        st.rerun()
                    st.markdown("</div>", unsafe_allow_html=True)

elif role == "student":
    curr_user = st.session_state.current_user

    if menu == "Профиль и достижения 👤":
        st.title("Профиль, статистика и достижения 👤")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Ваша личная информация, аналитика успеваемости и коллекция"
            " наград</p>",
            unsafe_allow_html=True,
        )

        # Блок 1: Настройки профиля
        st.markdown("### ⚙️ Настройки профиля")
        with st.container():
            new_name = st.text_input("Имя и Фамилия", value=user_info["name"])
            new_status = st.text_input(
                "Ваш статус / цель", value=user_info.get("status", "")
            )
            if st.button("Сохранить изменения профиля"):
                user_info["name"] = new_name
                user_info["status"] = new_status
                st.toast("Профиль успешно обновлен!")
                st.rerun()

        st.markdown("<br>", unsafe_allow_html=True)

        # Блок 2: Статистика и аналитика
        st.markdown("### 📊 Аналитика успеваемости и статистика")
        xp, solved, failed = get_student_xp_and_stats(curr_user)
        c1, c2, c3 = st.columns(3)
        c1.metric("Опыт (XP)", f"{xp} ⚡")
        c2.metric("Решено", f"{solved} ✅")
        c3.metric("Ошибок", f"{failed} ❌")

        st.markdown("<br>", unsafe_allow_html=True)

        # Блок 3: Рейтинг учеников (текущее место + 2 спереди и 2 сзади)
        st.markdown("### 🏆 Позиция в рейтинге")
        all_students = {
            uid: uinfo
            for uid, uinfo in st.session_state.users.items()
            if uinfo["role"] == "student"
        }
        lb_data = []
        for s_id, s_info in all_students.items():
            s_xp, s_sol, s_fai = get_student_xp_and_stats(s_id)
            lb_data.append({
                "id": s_id,
                "Ученик": s_info["name"],
                "XP": s_xp,
                "Ранг": get_rank(s_xp),
            })

        # Сортируем по XP по убыванию
        lb_data = sorted(lb_data, key=lambda x: x["XP"], reverse=True)

        # Находим индекс текущего ученика
        curr_idx = next((i for i, item in enumerate(lb_data) if item["id"] == curr_user), None)

        if curr_idx is not None:
            # Выделяем диапазон: 2 спереди, текущий, 2 сзади
            start_idx = max(0, curr_idx - 2)
            end_idx = min(len(lb_data), curr_idx + 3)
            window_data = lb_data[start_idx:end_idx]

            display_window = []
            for idx, item in enumerate(window_data, start=start_idx + 1):
                is_me = " ⭐ (Вы)" if item["id"] == curr_user else ""
                display_window.append({
                    "Место": f"#{idx}",
                    "Ученик": item["Ученик"] + is_me,
                    "XP": item["XP"],
                    "Ранг": item["Ранг"]
                })
            df_window = pd.DataFrame(display_window)
            st.dataframe(df_window, use_container_width=True)
        else:
            st.info("Информация о рейтинге недоступна.")

        st.markdown("<br>", unsafe_allow_html=True)

        # Блок 4: Достижения и ранги
        st.markdown("### 🏅 Достижения и ранги")
        with st.container():
            st.write(f"Ваш текущий ранг: **{get_rank(xp)}**")
            st.progress(
                min(xp / 1000, 1.0),
                text=f"Прогресс до ранга Легенда: {xp}/1000 XP",
            )

    elif menu == "Мои задания":
        if st.session_state.solving_v_id is not None:
            v_id = st.session_state.solving_v_id
            variant = st.session_state.variants[v_id]
            tasks = variant["tasks"]

            st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
            if st.button("← К списку ДЗ курса"):
                st.session_state.solving_v_id = None
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

            st.title(f"{variant['title']}")

            if curr_user not in st.session_state.student_progress:
                st.session_state.student_progress[curr_user] = {}

            if v_id not in st.session_state.student_progress[curr_user]:
                st.session_state.student_progress[curr_user][v_id] = {
                    "curr_idx": 0,
                    "task_states": {
                        i: {
                            "attempts_left": 3,
                            "status": "in_progress",
                            "feedback": "",
                            "user_answer": "",
                        }
                        for i in range(len(tasks))
                    },
                    "finished": False,
                }

            p_data = st.session_state.student_progress[curr_user][v_id]

            solved_count = sum(
                1 for ts in p_data["task_states"].values() if ts["status"] == "solved"
            )
            total_tasks = len(tasks)
            is_all_done = all(
                ts["status"] in ["solved", "failed", "pending_review"]
                for ts in p_data["task_states"].values()
            )
            if is_all_done:
                p_data["finished"] = True

            if p_data["finished"]:
                pct = (
                    int((solved_count / total_tasks) * 100) if total_tasks > 0 else 0
                )
                st.success(
                    f"🎉 Вариант успешно пройден! Верных ответов: {solved_count} из"
                    f" {total_tasks} ({pct}%)"
                )

            st.markdown("##### 📌 Навигация по заданиям варианта:")
            cols_nav = st.columns(min(len(tasks), 8))
            for idx in range(len(tasks)):
                t_st = p_data["task_states"][idx]
                status_icon = "⚪"
                if t_st["status"] == "solved":
                    status_icon = "✅"
                elif t_st["status"] == "failed":
                    status_icon = "❌"
                elif t_st["status"] == "pending_review":
                    status_icon = "⏳"
                elif (
                        t_st["status"] == "in_progress"
                        and t_st.get("feedback") == "wrong"
                ):
                    status_icon = "⚠️"

                col_idx = idx % 8
                with cols_nav[col_idx]:
                    if st.button(
                            f"#{idx + 1} {status_icon}",
                            key=f"nav_task_{v_id}_{idx}",
                            use_container_width=True,
                    ):
                        p_data["curr_idx"] = idx
                        st.rerun()

            st.markdown("---")

            curr_idx = p_data["curr_idx"]
            task = tasks[curr_idx]
            t_state = p_data["task_states"][curr_idx]

            st.markdown(f"### Задание #{curr_idx + 1}")
            with st.container():
                st.markdown(f"**Условие:** {task.get('question_text', '')}")
                if task.get("task_img"):
                    st.image(task["task_img"], use_container_width=True)

                if t_state["status"] == "in_progress":
                    if t_state.get("feedback") == "wrong":
                        st.error(
                            f"❌ Неверный ответ! Осталось попыток:"
                            f" {t_state['attempts_left']}"
                        )

                    user_ans = st.text_input(
                        "Ваш ответ:",
                        value=t_state.get("user_answer", ""),
                        key=f"ans_{v_id}_{curr_idx}",
                    )
                    if st.button(
                            "Отправить ответ",
                            use_container_width=True,
                            key=f"send_ans_{v_id}_{curr_idx}",
                    ):
                        if user_ans:
                            t_state["user_answer"] = user_ans
                            if task.get("is_manual", False):
                                t_state["status"] = "pending_review"
                                st.toast("Отправлено на проверку преподавателю")
                            else:
                                if user_ans.strip().lower() == task["answer"].strip().lower():
                                    t_state["status"] = "solved"
                                    t_state["feedback"] = "right"
                                else:
                                    t_state["attempts_left"] -= 1
                                    t_state["feedback"] = "wrong"
                                    if t_state["attempts_left"] <= 0:
                                        t_state["status"] = "failed"
                            st.rerun()

                elif t_state["status"] == "pending_review":
                    st.info("Отправлено на проверку преподавателю")

                elif t_state["status"] in ["solved", "failed"]:
                    if t_state["status"] == "solved":
                        st.success(
                            f"✨ Верный ответ! (Ваш ответ: {t_state.get('user_answer', '')})"
                        )
                    else:
                        st.error(
                            "❌ Неверный ответ. Попытки исчерпаны. (Ваш ответ:"
                            f" {t_state.get('user_answer', '')})"
                        )

                    if task.get("expl_text") or task.get("expl_img"):
                        with st.expander("📖 Пояснение к решению", expanded=True):
                            if task.get("expl_text"):
                                st.write(task["expl_text"])
                            if task.get("expl_img"):
                                st.image(task["expl_img"], use_container_width=True)

                st.markdown("<br>", unsafe_allow_html=True)
                col_prev, col_next = st.columns(2)
                if curr_idx > 0:
                    if col_prev.button("← Предыдущее задание", use_container_width=True):
                        p_data["curr_idx"] -= 1
                        st.rerun()
                if curr_idx < len(tasks) - 1:
                    if col_next.button("Следующее задание →", use_container_width=True):
                        p_data["curr_idx"] += 1
                        st.rerun()

        elif st.session_state.solving_course_id is not None:
            c_id = st.session_state.solving_course_id
            course = st.session_state.courses.get(c_id, {})

            st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
            if st.button("← К списку курсов"):
                st.session_state.solving_course_id = None
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

            st.title(f"{course.get('title', 'Курс')}")
            st.markdown(
                "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
                " 25px;'>Доступные домашние задания по курсу</p>",
                unsafe_allow_html=True,
            )

            course_variants = {
                v_id: v_data
                for v_id, v_data in st.session_state.variants.items()
                if v_data.get("course_id") == c_id
            }

            if not course_variants:
                st.info("Пока нет ДЗ для этого курса. Преподаватель скоро их добавит!")
            else:
                for v_id, variant in course_variants.items():
                    with st.container():
                        c1, c2 = st.columns([3, 1])
                        c1.markdown(f"#### {variant['title']}")
                        c1.write(f"Заданий: **{len(variant['tasks'])}**")

                        prog = (
                            st.session_state.student_progress.get(curr_user, {})
                            .get(v_id, {})
                        )
                        finished = prog.get("finished", False)
                        if finished:
                            c1.success(
                                "✅ ДЗ выполнено (нажмите «Приступить», чтобы просмотреть"
                                " решения)"
                            )
                        else:
                            c1.info("⚡ Доступно для выполнения")

                        if c2.button(
                                "Приступить", key=f"start_v_{v_id}", use_container_width=True
                        ):
                            st.session_state.solving_v_id = v_id
                            st.rerun()

        else:
            st.title("Список курсов 📚")
            st.markdown(
                "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
                " 25px;'>Выберите курс, чтобы перейти к списку домашних заданий</p>",
                unsafe_allow_html=True,
            )

            my_course_ids = st.session_state.course_assignments.get(
                curr_user, list(st.session_state.courses.keys())
            )
            available_courses = {
                cid: cdata
                for cid, cdata in st.session_state.courses.items()
                if cid in my_course_ids
            }

            if not available_courses:
                st.info("У вас пока нет назначенных курсов.")
            else:
                # Отображаем курсы с тонкими четкими линиями разделения
                course_keys = list(available_courses.keys())
                for idx_c, (cid, cdata) in enumerate(available_courses.items()):
                    with st.container():
                        col_c1, col_c2 = st.columns([4, 1])
                        col_c1.markdown(f"### {cdata['title']}")
                        col_c1.write(cdata["desc"])

                        c_vars = [
                            v_id
                            for v_id, v_data in st.session_state.variants.items()
                            if v_data.get("course_id") == cid
                        ]
                        if c_vars:
                            total_tasks = sum(
                                len(st.session_state.variants[v_id]["tasks"])
                                for v_id in c_vars
                            )
                            solved_tasks = 0
                            for v_id in c_vars:
                                p_prog = (
                                    st.session_state.student_progress.get(curr_user, {})
                                    .get(v_id, {})
                                )
                                for t_st in p_prog.get("task_states", {}).values():
                                    if t_st.get("status") == "solved":
                                        solved_tasks += 1
                            pct = (
                                int((solved_tasks / total_tasks) * 100)
                                if total_tasks > 0
                                else 0
                            )

                            col_c1.markdown(
                                "📊 **Прогресс по курсу:** Решено задач:"
                                f" **{solved_tasks} из {total_tasks}** ({pct}%)"
                            )
                            col_c1.progress(pct / 100)
                        else:
                            col_c1.text("Пока нет ДЗ на курсе")

                        if col_c2.button(
                                "Выбрать курс",
                                key=f"pick_course_{cid}",
                                use_container_width=True,
                        ):
                            st.session_state.solving_course_id = cid
                            st.rerun()

                    # Добавляем тонкую линию разделения между курсами (кроме последнего)
                    if idx_c < len(course_keys) - 1:
                        st.markdown(
                            '<hr style="margin: 20px 0; border: none; border-top: 1px solid'
                            ' #cbd5e1;">',
                            unsafe_allow_html=True,
                        )

    elif menu == "Расписание":
        st.title("Расписание занятий 📅")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Ваши персональные веб-уроки и вебинары</p>",
            unsafe_allow_html=True,
        )
        my_lessons = st.session_state.schedule.get(curr_user, [])
        if not my_lessons:
            st.info("В вашем расписании пока нет запланированных занятий.")
        else:
            for idx, l in enumerate(my_lessons):
                st.markdown('<div class="lesson-card">', unsafe_allow_html=True)
                with st.container(border=True):
                    st.markdown(f"#### 📚 Тема: {l['title']}")
                    st.markdown(
                        "📅 Дата и время:"
                        " **<span style='font-size: 1.2rem; font-weight:"
                        f" 800;'>{l['datetime']} (МСК)</span>**",
                        unsafe_allow_html=True,
                    )
                    if l["link"]:
                        st.link_button("🔗 Подключиться", l["link"], use_container_width=True)
                    else:
                        st.button(
                            "🔗 Ссылка появится позже",
                            disabled=True,
                            use_container_width=True,
                            key=f"nolink_{curr_user}_{idx}",
                        )
                st.markdown("</div>", unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)

    elif menu == "Пробные экзамены":
        if st.session_state.solving_mock_id is not None:
            exams_list = st.session_state.mock_exams.get(curr_user, [])
            current_exam = next(
                (
                    ex
                    for ex in exams_list
                    if ex["number"] == st.session_state.solving_mock_id
                ),
                None,
            )

            if not current_exam:
                st.session_state.solving_mock_id = None
                st.rerun()

            if current_exam["start_time"] is None:
                current_exam["start_time"] = datetime.datetime.now()
                current_exam["status"] = "in_progress"

            elapsed_seconds = (
                    datetime.datetime.now() - current_exam["start_time"]
            ).total_seconds()
            total_allowed_seconds = current_exam["duration_minutes"] * 60
            remaining_seconds = total_allowed_seconds - elapsed_seconds

            if remaining_seconds <= 0:
                current_exam["status"] = "pending_review"
                st.session_state.solving_mock_id = None
                st.warning(
                    "⏱️ Время вышло! Пробный экзамен автоматически отправлен"
                    " преподавателю на проверку."
                )
                st.rerun()

            rem_min = int(remaining_seconds // 60)
            rem_sec = int(remaining_seconds % 60)

            st.markdown('<div class="btn-secondary">', unsafe_allow_html=True)
            if st.button("← К списку пробников"):
                st.session_state.solving_mock_id = None
                st.rerun()
            st.markdown("</div>", unsafe_allow_html=True)

            st.title(
                current_exam.get(
                    "title", f"Пробный экзамен №{current_exam['number']}"
                )
            )
            st.markdown(
                f"""
                <div style="background: linear-gradient(135deg, #eef2ff, #fae8ff); padding: 16px; border-radius: 16px; margin-bottom: 20px; border: 1px solid #e0e7ff; display: flex; justify-content: space-between; align-items: center;">
                    <div style="font-weight: 700; color: #4338ca; font-size: 1.1rem;">⏳ Осталось времени: {rem_min:02d}:{rem_sec:02d}</div>
                    <div style="font-size: 0.9rem; color: #64748b;">Картинки и ответы принимаются без мгновенной проверки</div>
                </div>
            """,
                unsafe_allow_html=True,
            )

            if "mock_task_idx" not in st.session_state:
                st.session_state.mock_task_idx = 0

            tasks = current_exam["tasks"]
            if st.session_state.mock_task_idx >= len(tasks):
                st.session_state.mock_task_idx = len(tasks) - 1

            m_idx = st.session_state.mock_task_idx
            cur_task = tasks[m_idx]

            cols_m_nav = st.columns(min(len(tasks), 8))
            for i in range(len(tasks)):
                col_i = i % 8
                with cols_m_nav[col_i]:
                    has_ans = (
                        "✏️" if current_exam["student_answers"].get(i) else "⚪"
                    )
                    if st.button(
                            f"#{i + 1} {has_ans}",
                            key=f"mock_nav_{i}",
                            use_container_width=True,
                    ):
                        st.session_state.mock_task_idx = i
                        st.rerun()

            st.markdown("---")
            st.markdown(f"### Задание №{m_idx + 1}")
            st.markdown(f"**Условие:** {cur_task['question_text']}")
            if cur_task.get("task_img"):
                st.image(cur_task["task_img"], use_container_width=True)

            ans_key = f"mock_ans_{current_exam['number']}_{m_idx}"
            current_val = current_exam["student_answers"].get(m_idx, "")
            user_ans_input = st.text_input(
                "Ваш ответ (или загрузите фото/опишите решение ниже):",
                value=current_val,
                key=ans_key,
            )
            current_exam["student_answers"][m_idx] = user_ans_input

            st.markdown("<br>", unsafe_allow_html=True)
            col_mp, col_mn = st.columns(2)
            if m_idx > 0:
                if col_mp.button("← Предыдущее задание", use_container_width=True):
                    st.session_state.mock_task_idx -= 1
                    st.rerun()
            if m_idx < len(tasks) - 1:
                if col_mn.button("Следующее задание →", use_container_width=True):
                    st.session_state.mock_task_idx += 1
                    st.rerun()

            st.markdown("<br><br>", unsafe_allow_html=True)
            if st.button(
                    "📤 Завершить экзамен и отправить преподавателю",
                    use_container_width=True,
            ):
                current_exam["status"] = "pending_review"
                st.session_state.solving_mock_id = None
                st.toast("Пробный экзамен успешно отправлен преподавателю!")
                st.rerun()

        else:
            st.title("Система пробных экзаменов 📝")
            st.markdown(
                "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
                " 25px;'>Ваши пробные варианты с таймером и результатами</p>",
                unsafe_allow_html=True,
            )

            exams = st.session_state.mock_exams.get(curr_user, [])

            if not exams:
                st.info("У вас пока нет отправленных пробных экзаменов.")
            else:
                for ex in exams:
                    status = ex.get("status", "not_started")

                    if status == "graded":
                        badge_bg = "#64748b"
                        badge_text = "Проверено"
                        max_s = ex.get("max_score", len(ex["tasks"]))
                        p_s = ex.get("primary_score", 0)
                        score_display = f"{p_s}/{max_s}"
                        grade_display = ex.get("grade", "—")
                    elif status == "pending_review":
                        badge_bg = "#10b981"
                        badge_text = "Отправлено"
                        score_display = "—"
                        grade_display = "—"
                    elif status == "in_progress":
                        badge_bg = "#f59e0b"
                        badge_text = "В процессе"
                        score_display = "—"
                        grade_display = "—"
                    else:
                        badge_bg = "#3b82f6"
                        badge_text = "Не начат"
                        score_display = "—"
                        grade_display = "—"

                    st.markdown(
                        f"""
                        <div style="background: linear-gradient(135deg, #0ea5e9 0%, #2563eb 100%); border-radius: 24px; padding: 28px; color: white; margin-bottom: 20px; box-shadow: 0 15px 35px rgba(37, 99, 235, 0.25);">
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">
                                <span style="background: {badge_bg}; padding: 6px 14px; border-radius: 20px; font-size: 0.8rem; font-weight: 700;">{badge_text}</span>
                                <span style="font-size: 0.85rem; font-weight: 600; opacity: 0.9;">Пробник</span>
                            </div>
                            <h3 style="color: white; font-size: 1.25rem; font-weight: 800; margin-bottom: 12px; line-height: 1.4;">{ex.get('title', f'Пробный вариант ЕГЭ №{ex["number"]}')}</h3>
                            <p style="color: rgba(255, 255, 255, 0.9); font-size: 0.95rem; line-height: 1.5; margin-bottom: 24px;">{ex.get('description', 'Постарайтесь прорешать тест за отведенное время.')}</p>
                            <div style="display: flex; justify-content: space-between; align-items: flex-end;">
                                <div>
                                    <div style="font-size: 0.85rem; font-weight: 600; opacity: 0.8; margin-bottom: 4px;">Оценка за экзамен</div>
                                    <div style="font-size: 1.5rem; font-weight: 900;">{grade_display}</div>
                                </div>
                                <div style="text-align: right;">
                                    <div style="font-size: 0.85rem; font-weight: 600; opacity: 0.8; margin-bottom: 4px;">Баллы</div>
                                    <div style="font-size: 2.2rem; font-weight: 900; line-height: 1;">{score_display}</div>
                                </div>
                            </div>
                        </div>
                    """,
                        unsafe_allow_html=True,
                    )

                    col_b1, col_b2 = st.columns([1, 1])
                    if status == "not_started":
                        if st.button(
                                f"🚀 Начать пробный экзамен №{ex['number']}",
                                key=f"start_mock_{ex['number']}",
                                use_container_width=True,
                        ):
                            st.session_state.solving_mock_id = ex["number"]
                            st.session_state.mock_task_idx = 0
                            st.rerun()
                    elif status == "in_progress":
                        if st.button(
                                f"▶️ Продолжить экзамен №{ex['number']}",
                                key=f"resume_mock_{ex['number']}",
                                use_container_width=True,
                        ):
                            st.session_state.solving_mock_id = ex["number"]
                            st.rerun()
                    elif status == "pending_review":
                        st.info(
                            "⏳ Экзамен отправлен преподавателю. Ожидается проверка и"
                            " выставление баллов."
                        )
                    elif status == "graded":
                        with st.expander("📖 Посмотреть ваши ответы и детали"):
                            for idx_t, t_item in enumerate(ex["tasks"]):
                                st.write(
                                    f"**Задание №{idx_t + 1}:** {t_item['question_text']}"
                                )
                                st.write(
                                    "Ваш ответ:"
                                    f" <b>{ex['student_answers'].get(idx_t, 'Нет ответа')}</b>",
                                    unsafe_allow_html=True,
                                )
                                st.markdown("---")
                    st.markdown("<br>", unsafe_allow_html=True)

    elif menu == "Сообщения ✉️":
        st.title("Сообщения с преподавателем ✉️")
        st.markdown(
            "<p style='color: #64748b; margin-top: -10px; margin-bottom:"
            " 25px;'>Задавайте вопросы и получайте обратную связь</p>",
            unsafe_allow_html=True,
        )

        msg_input = st.text_input("Написать преподавателю вопрос:")
        if st.button("Отправить сообщение"):
            if msg_input:
                if curr_user not in st.session_state.messages:
                    st.session_state.messages[curr_user] = []
                st.session_state.messages[curr_user].append(
                    {"sender": "student", "text": msg_input}
                )
                st.toast("Сообщение отправлено преподавателю!")
                st.rerun()

        st.markdown("---")
        user_msgs = st.session_state.messages.get(curr_user, [])
        if not user_msgs:
            st.info("История сообщений пуста.")
        else:
            for m in user_msgs:
                st.write(
                    f"{'👨‍💻 Вы' if m['sender'] == 'student' else '👨‍🏫 Преподаватель'}:"
                    f" {m['text']}"
                )
