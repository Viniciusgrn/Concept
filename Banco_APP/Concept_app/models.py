from django.db import models

############ NOTAS ############

    #### Fields
        # ForeignKey -> Para utilizarmos ForeingKey é necessario 'chama-la' da seguinte maneira -> models.ForeignKey( nomeDoModelApontadoSemAspas, on_delete=models.CASCADE)
            #Ponto importante!
            # Nas foreings key você provavelmente verá o parametro 'on_delete' ele é responsavel pela forma que o registro no banco se comportará caso seja apagado,
            # como por exemplos caso venha a utilizar o 'on_delete=models.CASCADE' e um registro desta tabela sejá excluido
            # todos os demais registros que dependam deste serão excluidos junto.
            # Temos outras opções de on_delete como a DO_NOTHING, que faz com que o registro possa ser excluido sozinho 
            # e PROTECT que impede a exclusão de um registro caso o mesmo possua dependentes
        #AutoField -> O django por si só ja cria uma coluna de ID para primary key, sendo está numérica e auto increment, 
            # então não precisamos nos preocupar com a PK ao montar nossos models
        
    #### Parametros
        # null=False -> por default o django já deixa todos os parametros booleanos como False, então é necessario apenas modifica-lo se quiser como True
        # verbose_name -> É um parametro opcional, utilizado para que você coloque um "apelido" no campo, sendo este apelido o mostrado em tabelas e formulários no front-end
        # auto_now_add -> Funciona como uma Trigger de banco de dados, no qual ao adicionar um novo objeto a tabela, ela automaticamente adiciona a data e hora no campo indicado
        # auto_now -> Tambem funciona como uma Trigger de banco, entretanto diferente do auto_now_add que modifica o valor do campo apenas quando o objeto é criado, 
            #  este parametro modifica a data e hora sempre que o objeto é atualizado. Portanto é preferivel que sejá utilizado apenas um por DateTimeField ou DateField
        # blank -> Permite que os campos em formulários permaneçam em branco, entretanto ainda não é permitido null no banco
        # null -> Permite que o valor sejá null no banco de dados, entretanto ainda é necessario um input no campo de formulário

    #### Nome de registro
        # id_exemplo -> É preferivel, quando se cria uma foreing key, usar apenas o nome do campo sem a palavra "id", 
        # pois quando o django criar a tabela ele já irá concatenar a palavra "id", às colunas que recebem uma primary key ou foreing key

# Teremos o registro da empresa? Como ele será feito? Durante o cadastro do pedido, antes ou após?
# Eu pensei bastante e acho que seria legar realizar esse cadastro durante o preenchimento do orçamento
class Cliente(models.Model):

    opcoes_tipo =[
        (1, "Mecânico"),
        (2, "Elétrico"),
        (3, "Civil")
    ]
    

    opcoes_urgencias =[
        (1, "Urgente"),
        (2, "Data marcada"),
        (3, " ")
    ]

    servicos = models.IntegerField()
    idcnpj_cliente = models.CharField(primary_key=True, max_length=45)
    nome_empresa = models.CharField(max_length=255)
    endereco = models.CharField(max_length=45)
    tipo_de_executante = models.IntegerField(choices= opcoes_tipo, default=1)
    grau_de_urgencia = models.IntegerField(choices= opcoes_urgencias, default=1)
    nome_do_solicitante = models.CharField(max_length=50)

# Temos que pensar se existe a necessidade de uma tabela no banco de dados que armazenará as informações de uma unica empresa
# tendo em vista que o sistema é feito para a concept, entendemos que tudo que entrar nele já será relacionado a empresa 
# Num geral criamos no banco tabelas que armazenam objetos mutaveis, e que podem vir a aumentar ou diminuir algum dia,
# mesmo as tabelas que tendem a permanescer as mesmas sempre como uma tabela de choices, pode vir a receber novas escolhas ou vir a remover algumas
# R: A ideia da Empresa foimias para criar o login pro usuario, porém como você fise que não precisa. Acho que não vejo mais necessidade de ter esse atributo então.

# class Empresa(models.Models):
#     cnpj_concepet = models.CharField(primary_key=True, blank=False, max_length=45)
#     usuario = models.CharField( max_length=45, null=False)
#     senha = models.IntegerField(max_lenght=45, null=False)
#     email = models.CharField(max_lenght=45, null=False)

# # Pode se tornar uma classe para Usuario(com um campo de escolha da profissao), permitindo que a mesma tenha maior abrangencia de pessoas, facilitando possiveis ajustes.
# # Atualmente com o que temos da tabela Engenheiro, ele não seria capaz de acessar o sistema, visto que apenas na tabela empresa temos login e senha
# # (é apenas uma observação, visto que o django já irá criar a parte de registro de login e senha, então não é nessesario as ter nesta tabela tambem)
# class Engenheiro(models.Models):
#     numero_do_crea = models.CharField(primary_key=True, blank=False, max_length=45, null=False)
#     nome_do_responsavel = models.CharField(max_length=45, null=False)
#     especializacao = models.IntegerField(max_length=5, null=False)
#     cnpj_concept = models.ForeignKey("app.Model", verbose_name=_("Empresa"), on_delete=models.CASCADE) # type: ignore

class ServicosPrestados(models.Model):
    
    opcoes_status_da_obra ={
        (1,"Aguardando aprovação"),
        (2,"Em andamento"),
        (3,"Finalizado")
    }
    opcoes_tipo_de_servico ={
        (1, "Mecânico"),
        (2, "Elétrico"),
        (3, "Civil")
    }
    
    
    # servico_prestados = models.CharField(max_length=100)
    data_de_inicio = models.DateTimeField(auto_now_add=True)
    data_de_termino = models.DateTimeField(auto_now_add=True)
    status_da_obra = models.IntegerField(choices= opcoes_status_da_obra, default=1) #Vini essa parte achei muitp interessante naõ fazia ideia kkk 
    tipo_de_servico = models.IntegerField(choices= opcoes_tipo_de_servico, default=1)
    custo_da_obra = models.DecimalField(max_digits=10, decimal_places=2)
    idcnpj_cliente = models.ForeignKey( Cliente, on_delete=models.CASCADE)
    # atualizacao_da_obra = models.CharField(max_length=255)



    # Função utilizada para que você mande os campos que deseja desta tabela, para chamadas no front-end, de tabelas que a utilizam como foreing key
    def __init__(self):
        return '{}, {}'.format(self.status_da_obra, self.atualizacao_da_obra)

    def __repr__(self):
        return '{}, {}'.format(self.nome, self.sobrenome)

    

    
