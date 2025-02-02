function showTalkingScreen() {
    document.getElementById("talking_screen").hidden = false;
    document.getElementById("chela_screen").hidden = true;
}

function showChelaScreen() {
    document.getElementById("talking_screen").hidden = true;
    document.getElementById("chela_screen").hidden = false;
}

function setAssistantText(text) {
    document.getElementById("assistant_text").innerHTML = text;
}

eel.expose(showTalkingScreen);
eel.expose(showChelaScreen);
eel.expose(setAssistantText);
