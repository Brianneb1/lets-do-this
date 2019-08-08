function loadElements(){
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
            var delTask = new String(div.innerHTML.slice(0,div.innerHTML.indexOf("<")));
             $.ajax({
                        url: '/delete_task',
                        type: 'DELETE',
                        data: { task: delTask },
                        success: function(response){
                          console.log(response.message);
                          console.log(response.keys);
                          console.log(response.data);
                          },
                          error: function(error) {
                              console.log(error);
                          }
                    });
        }
    }

    // add checked symbol when clicking on list item
    var list = document.getElementById('myUL');
    if (list){
        list.addEventListener('click', check , false);
    }

}

// create new list item on enter
var input = document.getElementById("myInput");
if (input){
input.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        newElement();
    }
 }
)};

function check(ev) {
    if (ev.target.tagName === 'LI') {
        ev.target.classList.toggle('checked');
    }
    var checkTask = new String(ev.target.innerHTML.slice(0,ev.target.innerHTML.indexOf("<")));
    $.ajax({
            url: '/update_task',
            type: 'POST',
            data: { task: checkTask },
            success: function(response){
              console.log(response.message);
              console.log(response.keys);
              console.log(response.data);
              },
              error: function(error) {
                  console.log(error);
              }
        });
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

