import streamlit as st
import random

st.write("🌱 Grammar learning")

tab1, tab2, tab3 = st.tabs([
    "❄️ 1. Lesson: Understanding Past Tense",
    "❄️ 2. Activity: Practice Making Regular Tense",
    "❄️ 3. Test: Irregular Tense"
])

######### TAB 1

with tab1:
    st.markdown("### 📋 Understanding Past Tense")
    st.write("Let's Learn About the Past Tense!")

    # List of image URLs from your GitHub repository
    image_urls = [
        "images/슬라이드1.PNG",
        "images/슬라이드2.PNG",
        "images/슬라이드3.PNG",
        "images/슬라이드4.PNG",
        "images/슬라이드5.PNG"
    ]

    # Display each image using a loop
    for url in image_urls:
        st.image(url, caption=f"Slide {image_urls.index(url) + 1}", width=600)  # width in pixels

######### TAB 2

with tab2:
    st.title("Regular Verb Past Tense Practice")

    # List of regular verbs and their past tense forms with rules
    regular_verbs = {
        "discover": ("discovered", "General Rule: Add -ed (e.g., walk → walked)"),
        "end": ("ended", "General Rule: Add -ed (e.g., walk → walked)"),
        "realize": ("realized", "Ending with e: Add -d (e.g., love → loved)"),
        "inspire": ("inspired", "Ending with e: Add -d (e.g., love → loved)"),
        "start": ("started", "Single Vowel + Consonant: Double the consonant, add -ed (e.g., stop → stopped)")
    }

    # Initialize session state variables
    if "current_regular_verb" not in st.session_state:
        st.session_state.current_regular_verb = None
    if "regular_user_input" not in st.session_state:
        st.session_state.regular_user_input = ""
    if "regular_check_clicked" not in st.session_state:
        st.session_state.regular_check_clicked = False

    # Button to select a new random regular verb
    if st.button("🎲 Get a new regular verb", key="regular_button"):
        st.session_state.current_regular_verb = random.choice(list(regular_verbs.keys()))
        st.session_state.regular_user_input = ""
        st.session_state.regular_check_clicked = False

    # Display the current regular verb
    if st.session_state.current_regular_verb:
        st.write(f"Base form: **{st.session_state.current_regular_verb}**")

        # Text input for user's answer
        st.session_state.regular_user_input = st.text_input("Enter the past tense form:", value=st.session_state.regular_user_input, key="regular_input")

        # Button to check the answer
        if st.button("✅ Check the answer", key="regular_check_button"):
            st.session_state.regular_check_clicked = True

        # Feedback
        if st.session_state.regular_check_clicked:
            correct_answer, explanation = regular_verbs[st.session_state.current_regular_verb]
            if st.session_state.regular_user_input.strip().lower() == correct_answer:
                st.success(f"✅ Correct! {explanation}")
            else:
                st.error(f"❌ Incorrect. The correct past tense is: **{correct_answer}**")

######### TAB 3

import streamlit as st
import random

with st.container():
    st.title("Irregular Verb Past Tense Practice")

    # List of verbs and their past and past participle forms
    verbs = {
        "be": ("was/were", "been"),
        "become": ("became", "become"),
        "begin": ("began", "begun"),
        "break": ("broke", "broken"),
        "bring": ("brought", "brought"),
        "build": ("built", "built"),
        "buy": ("bought", "bought"),
        "catch": ("caught", "caught"),
        "choose": ("chose", "chosen"),
        "come": ("came", "come"),
        "do": ("did", "done"),
        "drink": ("drank", "drunk"),
        "drive": ("drove", "driven"),
        "eat": ("ate", "eaten"),
        "fall": ("fell", "fallen"),
        "feel": ("felt", "felt"),
        "get": ("got", "gotten"),
        "go": ("went", "gone"),
        "have": ("had", "had"),
        "know": ("knew", "known"),
        "leave": ("left", "left"),
        "make": ("made", "made"),
        "read": ("read", "read"),
        "run": ("ran", "run"),
        "say": ("said", "said"),
        "see": ("saw", "seen"),
        "send": ("sent", "sent"),
        "sing": ("sang", "sung"),
        "speak": ("spoke", "spoken"),
        "take": ("took", "taken"),
        "write": ("wrote", "written")
    }

    # Initialize session state variables
    if "current_verb" not in st.session_state:
        st.session_state.current_verb = None
    if "user_input_past" not in st.session_state:
        st.session_state.user_input_past = ""
    if "user_input_participle" not in st.session_state:
        st.session_state.user_input_participle = ""
    if "check_clicked" not in st.session_state:
        st.session_state.check_clicked = False

    # Button to select a new random verb
    if st.button("🎲 Get a new verb", key="irregular_button"):
        st.session_state.current_verb = random.choice(list(verbs.keys()))
        st.session_state.user_input_past = ""
        st.session_state.user_input_participle = ""
        st.session_state.check_clicked = False

    # Display the current verb
    if st.session_state.current_verb:
        st.write(f"Base form: **{st.session_state.current_verb}**")

        # Text input for user's answers
        st.session_state.user_input_past = st.text_input("Enter the past tense form:", value=st.session_state.user_input_past, key="past_input")
        st.session_state.user_input_participle = st.text_input("Enter the past participle form:", value=st.session_state.user_input_participle, key="participle_input")

        # Button to check the answer
        if st.button("✅ Check the answers", key="irregular_check_button"):
            st.session_state.check_clicked = True

        # Feedback
        if st.session_state.check_clicked:
            correct_past, correct_participle = verbs[st.session_state.current_verb]
            past_correct = st.session_state.user_input_past.strip().lower() == correct_past
            participle_correct = st.session_state.user_input_participle.strip().lower() == correct_participle

            if past_correct and participle_correct:
                st.success("✅ Both answers are correct!")
            else:
                st.error("❌ Incorrect. You need to get both forms right.")
                if not past_correct:
                    st.info(f"The correct past tense is: **{correct_past}**")
                if not participle_correct:
                    st.info(f"The correct past participle is: **{correct_participle}**")

