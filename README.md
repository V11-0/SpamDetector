# SpamDetector
Simple project used to detect if a given email is a SPAM or not, made for AI subject of Systems Development and Analysis course.

The predction model was trained with this dataset:
https://archive.ics.uci.edu/ml/datasets/spambase

Projeto simples para detectar se um Email é SPAM ou não, feito para a disciplina de IA do curso de ADS.

O Modelo foi treinado usando este dataset:
https://archive.ics.uci.edu/ml/datasets/spambase


## Get Started
O programa define um end point em /checkEmail.  
Envie um POST para o end point passando um JSON como body contendo o atributo "message"

    POST /checkEmail

Corpo:

    {
        "message": "Corpo do email a ser verificado"
    }

O retorno da solicitação será um json com o atributo "class".  
'class' será 'true' caso o email seja detectado como spam e 'false' caso não seja spam

    {
        "class": true
    }

## Acknowledgements

Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science. 

Thanks.