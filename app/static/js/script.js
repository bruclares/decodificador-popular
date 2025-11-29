let termosDict = [];

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const response = await fetch("/api/termos");
    termosDict = await response.json();
    console.log(
      "Dicionário carregado com sucesso:",
      termosDict.length,
      "termos."
    );
  } catch (error) {
    console.error("Erro ao carregar dicionário:", error);
  }
});

function decodificar() {
  const inputElement = document.getElementById("inputTexto");
  const outputElement = document.getElementById("resultado");
  let texto = inputElement.value;

  if (!texto.trim()) {
    outputElement.innerHTML =
      '<p style="color: #666;">Por favor, cole um texto para analisar.</p>';
    return;
  }

  texto = escapeHtml(texto);

  let encontrouAlgo = false;

  termosDict.forEach((item) => {
    const regex = new RegExp(escapeRegExp(item.termo), "gi");

    if (texto.match(regex)) {
      encontrouAlgo = true;
      texto = texto.replace(regex, (match) => {
        return `<span class="alerta" data-traducao="${item.tipo.toUpperCase()}: ${
          item.traducao
        }">${match}</span>`;
      });
    }
  });

  texto = texto.replace(/\n/g, "<br>");

  if (encontrouAlgo) {
    outputElement.innerHTML = texto;
  } else {
    outputElement.innerHTML =
      "<p>Nenhum termo suspeito encontrado neste trecho. (Ou nosso dicionário precisa crescer!)</p>" +
      '<div style="margin-top:20px; color:#666;">' +
      texto +
      "</div>";
  }
}

function limpar() {
  document.getElementById("inputTexto").value = "";
  document.getElementById("resultado").innerHTML =
    '<p class="placeholder-text">O texto decodificado aparecerá aqui...</p>';
}

function escapeHtml(text) {
  const map = {
    "&": "&amp;",
    "<": "&lt;",
    ">": "&gt;",
    '"': "&quot;",
    "'": "&#039;",
  };
  return text.replace(/[&<>"']/g, function (m) {
    return map[m];
  });
}

function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
