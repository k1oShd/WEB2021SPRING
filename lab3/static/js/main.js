var cntAdd = 0;
var cntClk = 0;

function handleAddNote(text){
	var node = document.createElement("div");
	var checkBox = document.createElement("input");
	var par = document.createElement("p");
	var trashCan = document.createElement("div");
	var trashCanImg = document.createElement("img");
	var mainDiv = document.getElementById("notesStorage");
	checkBox.setAttribute("type","checkbox");
	checkBox.setAttribute("id","Chk");
	checkBox.style.width = "10%";
	checkBox.setAttribute("onclick","writeOff(this)");
	trashCanImg.setAttribute("onclick","terminate(this)")
	par.style.width = "80%";
	par.innerHTML = text;
	trashCan.style.width = "10%";
	trashCan.setAttribute("class","trashCanDiv");
	trashCan.style.justifyContent = "center";
	trashCan.style.height = "20px";
	trashCanImg.style.height = "19px";
	trashCanImg.style.width = "19px";
	trashCanImg.setAttribute("src","static/img/delete.png")
	node.setAttribute("class","newNote");
	node.setAttribute("id","Note");
	node.style.display = "flex";
	node.style.justifyContent = "space-around";
	node.style.alignItems = "center";
	mainDiv.style.border = "10px solid #565656";
	mainDiv.style.borderRadius = "5px";
	document.getElementById("notesStorage").appendChild(node);
	document.getElementById("textInput").value = "";
	cntAdd++;
	document.getElementsByClassName("newNote")[cntAdd-1].appendChild(checkBox);
	document.getElementsByClassName("newNote")[cntAdd-1].appendChild(par);
	document.getElementsByClassName("newNote")[cntAdd-1].appendChild(trashCan);
	document.getElementsByClassName("trashCanDiv")[cntAdd-1].appendChild(trashCanImg);
}

function handleHover(){
	var deleteButton = document.createElement("img");
	deleteButton.setAttribute("src","static/img/delete.png");
	deleteButton.setAttribute("class","delButt");
	document.getElementById("notesStorage").appendChild(deleteButton);
}

function deleteNote(){
	var delNote = document.getElementsByClassName("delButt");
}

function writeOff(el) {
	var checkBox = el;
	var note = checkBox.parentElement;
	if (checkBox.checked) {
		note.style.textDecoration = "line-through";	
	}
	else {
		note.style.textDecoration = "none";
	}
}

function terminate(el) {
	el.parentElement.parentElement.style.backgroundColor = "white";
	el.parentElement.parentElement.style.color = "white";
	el.style.opacity = "0";
	el.style.transitionDuration = ".4s";
	el.parentElement.parentElement.style.transitionDuration = ".5s";
	setTimeout(function() {el.parentElement.parentElement.remove();}, 600);
	
}

