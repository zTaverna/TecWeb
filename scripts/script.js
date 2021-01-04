var nome = "Comunistão";
var idade = 40;
var cursos = ["Manifesto", "Filósofo","Visionário"]
var notas = [
	[7, 6, 5],
	[3.5, 4, 6],
	[8, 9, 10]
];

console.log("Olá, "+nome+"!");
console.log("Idade "+idade+" anos.");

for(var i=0; i < cursos.length; i++){
	console.log("Cursos: "+cursos[i]);
	var media = 0;
	for(var j=0; j < notas.length; j++){
		media = media + notas[i][j];
	}
	media = media/3;
	if ( media >= 6 ){
		console.log("Aprovado!");
	} else {
		console.log("Reprovado!");
	
	}
}


