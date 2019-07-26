// create "close" button for each list item
var myNodeList = document.getElementsByTagName("LI");
var i;
for (i=0; i<myNodeList.length; i++)
{
    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    myNodeList[i].appendChild(span);
}

//click on close button to hide list item
var close = document.getElementsByClassName("close");
var i;
for (i = 0; i < close.length; i++){
    close[i].onclick = function() {
        var div = this.parentElement;
        div.style.display = "none";
    }
}

// add checked symbol when clicking on list item
var list = document.querySelector('UL');
list.addEventListener('click', check , false);

// create new list item on enter
var input = document.getElementById("myInput");
input.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        newElement();
    }
});

function check(ev) {
    if (ev.target.tagName === 'LI') {
        ev.target.classList.toggle('checked');
    }
}

// create new list item when clicking add
function newElement() {
    var li = document.createElement('LI');
    var inputValue = document.getElementById("myInput").value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    if (inputValue === '') {
        alert("You must type something!");
    } else {
        document.getElementById('myUL').appendChild(li);
    }
    document.getElementById('myInput').value = "";

    var span = document.createElement("SPAN");
    var txt = document.createTextNode("\u00D7");
    span.className = "close";
    span.appendChild(txt);
    li.appendChild(span);

    for (i = 0; i< close.length; i++) {
        close[i].onclick = function() {
            var div = this.parentElement;
            div.style.display = "none";
        }
    }
}
