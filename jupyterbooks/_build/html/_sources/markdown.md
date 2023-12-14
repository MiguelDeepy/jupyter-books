# Arquivos Markdown

Seja escrevendo o conteúdo do seu livro em Notebooks Jupyter (.ipynb) ou em arquivos markdown comuns (.md), você escreverá no mesmo "tipo" de markdown chamado MyST Markdown.
Este é um arquivo simples para ajudá-lo a começar e mostrar um pouco da sintaxe.

## O que é MyST?

MyST significa "Markedly Structured Text" (Texto Estruturado Marcante). É
uma pequena variação de um tipo de markdown chamado "CommonMark", com
pequenas extensões de sintaxe para permitir que você escreva **regras** e
**diretrizes** no ecossistema Sphinx.

MyST stands for "Markedly Structured Text". It
is a slight variation on a flavor of markdown called "CommonMark" markdown,
with small syntax extensions to allow you to write **roles** and **directives**
in the Sphinx ecosystem.

Para saber mais sobre MyST, consulte [Visão geral do MyST Markdown](https://jupyterbook.org/content/myst.html)

## Regras e Diretrizes de Exemplo

Funções e diretivas são duas das ferramentas mais poderosas do Jupyter Book. Elas
são como funções, mas escritas em uma linguagem de marcação. Ambas
servem a um propósito semelhante, mas **regras são escritas em uma linha**,
enquanto **diretrizes se estendem por várias linhas**. Ambas aceitam diferentes
tipos de entradas, e o que fazem com essas entradas depende da função ou
diretiva específica que está sendo chamada.

Aqui está uma diretiva "nota":

```{note}
Aqui é uma nota.
```

Ela será renderizada em uma caixa especial quando você construir seu livro.

Aqui está uma diretiva inline para referenciar um documento: {doc}`markdown-notebooks`.

## Citations

Você também pode citar referências armazenadas em um arquivo `bibtex`. Por exemplo,
a seguinte sintaxe: ``{cite}`holdgraf_evidence_2014` `` será renderizada como
isso: `{cite}holdgraf_evidence_2014``.

Além disso, você pode inserir uma bibliografia em sua página com esta sintaxe:
A diretiva `{bibliography}` deve ser usada para que todas as regra `{cite}`
sejam renderizadas corretamente.

Por exemplo, se as referências para o seu livro estão armazenadas em `references.bib`, a bibliografia é inserida com:

```{bibliography}
```

## Aprenda Mais

Este é apenas um simples começo para você começar.
Você pode aprender muito mais em [jupyterbook.org](https://jupyterbook.org)
