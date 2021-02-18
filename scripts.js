function openNav() {
	document.getElementById("mySideBar").style.width = "250px";
	document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
	document.getElementById("mySideBar").style.width = "0";
	document.getElementById("main").style.marginLeft= "0";
}

function openProject(container, content, button, header){
	document.getElementById(container).style.transitionDelay = '0s';
	document.getElementById(content).style.transitionDelay = '0.5s';
	document.getElementById(container).style.marginBottom = '1%';
	document.getElementById(container).style.marginTop = '1%';
	document.getElementById(content).style.width = "70%";
	document.getElementById(container).style.height = '410px';
	document.getElementById(button).innerHTML = "Close"
	document.getElementById(button).onclick = function() {closeProject(container, content, button, header)};
}

function closeProject(container, content, button, header){
	document.getElementById(container).style.transitionDelay = '0.5s';
	document.getElementById(content).style.transitionDelay = '0s';
	document.getElementById(container).style.marginBottom = '0%';
	document.getElementById(container).style.marginTop = '0%';
	document.getElementById(content).style.width = "0";
	document.getElementById(container).style.height = '0';
	document.getElementById(button).innerHTML = header
	document.getElementById(button).onclick = function() {openProject(container, content, button, header)};
}

function copyEmail(){
	var input = document.body.appendChild(document.createElement("input"));
	input.value = 'g.jeanneret10@uniandes.edu.co';
	input.focus();
	input.select();
	input.setSelectionRange(0, 99999);
	document.execCommand('copy');
	input.parentNode.removeChild(input);
	alert('Email copied to clipboard.')
}

function openExperience(button, text, content){
	document.getElementById(button).firstChild.data = "< Close";
	document.getElementById(content).style.height = '300px';
	document.getElementById(button).onclick = function() {closeExperience(button, text, content)}
}

function closeExperience(button, text, content){
	document.getElementById(button).firstChild.data = "> " + text
	document.getElementById(content).style.height = '0';
	document.getElementById(button).onclick = function() {openExperience(button, text, content)}
}
