copyButton = document.querySelector('#copy-button');
pcUrl = document.querySelector('#pc-url');

function myFunc() {
data = pcUrl.textContent.slice(17)
    navigator.clipboard.writeText(data)
}

copyButton.addEventListener("click",myFunc)