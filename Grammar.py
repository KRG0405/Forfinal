import streamlit as st
import random
import pandas as pd

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

    # Introduction
    st.header("What is the Past Tense?")
    st.write("The past tense is used to talk about actions that have already happened.")

    # Regular Verbs Section
    st.header("Regular Verbs")
    st.write("Forming Regular Past Tense:")
    st.write("1. General Rule: Add -ed (e.g., walk → walked)")
    st.write("2. Ending with 'e': Add -d (e.g., love → loved)")
    st.write("3. Single Vowel + Consonant: Double the consonant, add -ed (e.g., stop → stopped)")
    st.write("4. Ending with 'y': Change 'y' to 'i', add -ed (e.g., cry → cried)")

    # Irregular Verbs Section
    st.header("Irregular Verbs")
    st.write("Irregular verbs do not follow standard rules. Here are some examples:")

    # Irregular Verbs Table
    irregular_verbs_data = {
        "Base Form": ["Find", "Become", "Be", "Begin", "Break", "Bring", "Buy", "Choose", "Come", "Do", "Drink", "Drive", "Eat", "Fall", "Feel", "Get", "Go", "Have", "Know", "Leave", "Make", "Read", "Run", "Say", "See", "Send", "Sing", "Speak", "Take", "Write"],
        "Past Tense": ["Found", "Became", "Was/Were", "Began", "Broke", "Brought", "Bought", "Chose", "Came", "Did", "Drank", "Drove", "Ate", "Fell", "Felt", "Got", "Went", "Had", "Knew", "Left", "Made", "Read", "Ran", "Said", "Saw", "Sent", "Sang", "Spoke", "Took", "Wrote"],
        "Past Participle": ["Found", "Become", "Been", "Begun", "Broken", "Brought", "Bought", "Chosen", "Come", "Done", "Drunk", "Driven", "Eaten", "Fallen", "Felt", "Gotten", "Gone", "Had", "Known", "Left", "Made", "Read", "Run", "Said", "Seen", "Sent", "Sung", "Spoken", "Taken", "Written"]
    }

    irregular_verbs_df = pd.DataFrame(irregular_verbs_data)
    st.table(irregular_verbs_df)

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

with tab3:
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

