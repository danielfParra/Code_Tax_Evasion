setTimeout(redirect, 1000);

function redirect() {
    window.location.replace($('#prolific').attr('href'));
}
