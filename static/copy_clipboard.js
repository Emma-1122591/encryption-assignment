function copyToClipboard(encrypted_text) {
    navigator.clipboard.writeText(encrypted_text);
    alert("Tekst gekopieerd!");
}