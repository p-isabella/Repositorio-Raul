# Dicas

## Estão tendo problemas com dependências?

Isso aqui ajuda a rodar em qualquer lugar direto, desde que a **versão do python** seja a mesma.

O pip (gerenciador de pacotes do python) instala pacotes no seu computador para poder usar quando precisar. Só que tem um problema nisso. Ele instala no seu computador para rodar no seu computador, ou seja, você não vai ter os pacotes dele disponíveis em qualquer lugar, ai tem que ficar dando "pip install" infinitamente.

Pra evitar isso, nós usamos um truque chamado "ambiente virtual". Nele você pode forçar o python a não enxergar os pacotes do seu computador.

> Ué, mas por que eu iria querer isso?

Simples, você vai rodar com a certeza de que o seu ambiente está igual (ou pelomenos bem próximo disso) a qualquer outro computador que você queira rodar seu código. Dessa forma o seu código não depende mais de "onde está rodando", mas sim da versão do python.

Bem mais simples né?

Pra iniciar um ambiente virtual é só fazer isso aqui:

```bash
python -m venv nome_do_seu_ambiente
```

> ### O que isso faz?
> Ele usa chama o interpretador do Python (`python`) para executar um módulo (`-m`) chamado venv (`venv`), recebendo o argumento "nome_do_seu_ambiente".
>
> Eu aconselho fortemente que você nomeie seu ambiente como "venv". Não tem nenhum motivo especial, mas é um padrão na comunidade. Seguir esse padrão vai ajudar outros programadores que trabalharem com você a baterem o olho nessa pasta "./venv" e já saber exatamente do que se trata, sem gastar um segundo sequer pensando ou perguntando pra alguém.

Se quiser nomear seu ambiente como "venv" o comando é esse:

```bash
python -m venv venv
```

Feito isso, agora é só entrar no nosso ambiente.

Quando você executar esse comando ele vai criar uma pasta. Essa pasta tem uma outra pasta dentro dela chamada `/Scripts`, lá dentro tem alguns binários que são interessantes pra gente. Especialmente um chamado `activate`, que vai ativar nosso ambiente virtual (vai nos colocar dentro dele).

```
./venv/Scripts/activate
```

> ### E se eu for um penguim?
> Se você estiver usando Linux, a pasta que você quer não é o `/Scripts`, mas sim a pasta `/bin`
>
> ```
> source venv/bin/activate
> ```
>
> Esse "source" é só pra evitar problemas de permissão ;)

Pronto, agora estamos em um ambiente novo em folha, sem nenhum módulo. Agora temos **total controle** dos módulos que nosso código vai usar, tudo que você baixar vai estar aqui, e o que você não baixar **pra esse projeto** não vai estar **no ambiente desse projeto**.

Eu fiz esse caminho todo pra te apresentar um comando novo:

```
pip freeze
```

Esse comando vai te mostrar todas as bibliotecas que você tem baixado pelo pip. Se você rodar isso em qualquer pasta do seu computador fora do ambiente virtual, ele vai te retornar **todas as bibliotecas que você já baixou na vida e não desinstalou**. Mas dá pra deixar ele mais útil do que isso.

Dentro do ambiente virtual, ele só sabe dos pacotes que estão **aqui dentro**. Ou seja, o comando `pip freeze` agora nos mostra todas as dependências do nosso projeto! (se ele já estiver com elas baixadas, claro)

Sabendo disso, podemos usar o seguinte comando para criar um arquivo de texto com essas dependências.

```
pip freeze > requirements.txt
```

Aqui só tem um comando que você provavelmente não conhece: o `>`. Ele basicamente vai pegar a saída do comando anterior `pip freeze` e passar pro próximo. Dessa forma vamos gerar um arquivo `requirements.txt` com todas as dependências do nosso projeto, legal né?

Agora, toda vez que você entrar em um ambiente virtual novo limpinho, e ver um `requirements.txt` de bobeira por ai, você pode fazer o seguinte:

```
pip install -r requirements.txt
```

> ### O que isso faz?
> Ele vai chamar o `pip install` que você já conhece, e vai passar pra ele um "requirements file" (você disse que é um requirements file quando você digitou "`-r`" no comando) no caminho especificado `requirements.txt`.
> 
> RESUMINDO: ele vai instalar tudo que ta escrito no requirements.txt, nas EXATAS VERSÕES que estão descritas lá (isso evita uma dor de cabeça bizarra)

Agora toda vez que você for executar esse programa em qualquer lugar, cria um ambiente virtual, entra, instala as dependencias, e roda. Zero problemas com ficar instalando pacotes manualmente ;)


---


## Arquivo de testes