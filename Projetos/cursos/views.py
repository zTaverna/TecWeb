from django.shortcuts import render

def cursos(request):
    context = {
        "titulo":"Lista de Cursos",
        "cursos":[
            { "nome": "Análise e Desenvolvimento de Sistemas", "sigla": "ADS", "descricao": "Descrição de ADS" },
            { "nome": "Sistemas da Informação", "sigla": "SI", "descricao": "Descrição de SI" },
            { "nome": "Banco de Dados", "sigla": "BD", "descricao": "Descrição de BD" },
            { "nome": "Gestão em Tecnologia da Informação", "sigla": "GTI", "descricao": "Descrição de GTI" }
        ]
    }
    return render(request, "cursos.html", context)
    
def curso(request, sigla):
    dados ={
        "SI":{
            "nome": "Sistemas da Informação", "sigla": "SI", "sobre": "Descrição de SI", "periodo":["Matutino", "Noturno"]
        }
    }
    context = {
        "curso":dados[sigla]
    }
    return render(request, "curso.html", context)