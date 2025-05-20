import streamlit as st
from gtts import gTTS
from io import BytesIO

st.title("🌱 Grammar Learning")

# Create tabs
tab1, tab2 = st.tabs(["1. Understanding Past Tense", "2. Pronunciation Practice"])

######### TAB 1

with tab1:
    st.markdown("## 📋 Understanding Past Tense")
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

    irregular_verbs_data = {
        "Base Form": ["Find", "Become", "Be", "Begin", "Break", "Bring", "Buy", "Choose", "Come", "Do", "Drink", "Drive", "Eat", "Fall", "Feel", "Get", "Go", "Have", "Know", "Leave", "Make", "Read", "Run", "Say", "See", "Send", "Sing", "Speak", "Take", "Write"],
        "Past Tense": ["Found", "Became", "Was/Were", "Began", "Broke", "Brought", "Bought", "Chose", "Came", "Did", "Drank", "Drove", "Ate", "Fell", "Felt", "Got", "Went", "Had", "Knew", "Left", "Made", "Read", "Ran", "Said", "Saw", "Sent", "Sang", "Spoke", "Took", "Wrote"],
        "Past Participle": ["Found", "Become", "Been", "Begun", "Broken", "Brought", "Bought", "Chosen", "Come", "Done", "Drunk", "Driven", "Eaten", "Fallen", "Felt", "Gotten", "Gone", "Had", "Known", "Left", "Made", "Read", "Run", "Said", "Seen", "Sent", "Sung", "Spoken", "Taken", "Written"]
    }

    st.table(irregular_verbs_data)

######### TAB 2

with tab2:
    st.title("🔊 Pronunciation Practice")

    # Define the lists of verbs
    regular_verbs = ["discover", "end", "realize", "inspire", "start"]
    irregular_verbs = {
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

    # Regular Verbs Section
    st.header("Regular Verbs Pronunciation")
    selected_regular_verb = st.selectbox("Select a regular verb:", regular_verbs, key="regular")

    if selected_regular_verb:
        st.write(f"Pronunciation for: {selected_regular_verb}")
        tts = gTTS(selected_regular_verb)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0)
        st.audio(audio_fp, format="audio/mp3")

    # Irregular Verbs Section
    st.header("Irregular Verbs Pronunciation")
    selected_irregular_verb = st.selectbox("Select an irregular verb:", list(irregular_verbs.keys()), key="irregular")

    if selected_irregular_verb:
        forms = [selected_irregular_verb] + list(irregular_verbs[selected_irregular_verb])
        for form in forms:
            st.write(f"Pronunciation for: {form}")
            tts = gTTS(form)
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.audio(audio_fp, format="audio/mp3")

