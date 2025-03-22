function checkGrammar() {
    let inputText = document.getElementById("inputText").value;
    let correctedText = inputText.replace(/\bteh\b/g, "the"); // Example correction
    document.getElementById("outputText").value = correctedText;
}