function OpenFunc() {
    var i, j;
    var ele = document.getElementsByClassName('a-sty');
    for (i = 0; i < ele.length; i++) {
        ele[i].style.display = "block";
    }
    document.getElementById('Close-Btn').style.display = 'block';
    document.getElementById('Open-Btn').style.display = 'none';
}

function CloseFunc() {
    var i, j;
    var clele = document.getElementsByClassName('a-sty');
    for (i = 0; i < clele.length; i++) {
        if (clele[i].classList.contains('active')) {
            clele[i].style.display = 'block';
        } else {
            clele[i].style.display = 'none';
        }
    }
    document.getElementById('Open-Btn').style.display = 'block';
    document.getElementById('Close-Btn').style.display = 'none';
}

function myFunction(x) {
    var i, j;
    if (x.matches) {
        var clele = document.getElementsByClassName('a-sty');
        for (i = 0; i < clele.length; i++) {
            clele[i].style.display = "block";
        }
        document.getElementById('Open-Btn').style.display = 'none';
        document.getElementById('Close-Btn').style.display = 'none';
    } else {
        var clele = document.getElementsByClassName('a-sty');
        for (i = 0; i < clele.length; i++) {
            if (clele[i].classList.contains('active')) {
                clele[i].style.display = 'block';
            } else {
                clele[i].style.display = 'none';
            }
        }
        document.getElementById('Open-Btn').style.display = 'block';
        document.getElementById('Close-Btn').style.display = 'none';
    }
}
var x = window.matchMedia("(min-width: 768px)")
myFunction(x)
x.addListener(myFunction)