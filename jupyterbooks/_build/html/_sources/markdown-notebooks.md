---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Notebooks com MyST Markdown

O Jupyter Book também permite que você escreva notebooks baseados em texto usando MyST Markdown.
Consulte [A documentação Notebooks com MyST Markdown](https://jupyterbook.org/file-types/myst-notebooks.html) para instruções detalhadas.
Esta página apresenta um notebook escrito em MyST Markdown.

## Uma célula de exemplo

Com MyST Markdown, você pode definir células de código com uma diretiva como esta:

```{code-cell}
print(2 + 2)
```

Ao construir seu livro, o conteúdo de qualquer bloco `{code-cell}` será executado com seu kernel Jupyter padrão e seus resultados serão exibidos junto com o restante do seu conteúdo.

```{seealso}
O Jupyter Book usa [Jupytext](https://jupytext.readthedocs.io/en/latest/) para converter arquivos de texto em notebooks e também suporta [diversos outros formatos de arquivos de texto para notebooks](https://jupyterbook.org/file-types/jupytext.html).
```

## Criando um notebook com MyST Markdown

Os notebooks MyST Markdown são definidos por duas coisas:

Metadados YAML: necessários para entender se/como converter os arquivos de texto em notebooks (incluindo informações sobre o kernel necessário). Veja o YAML no topo desta página como exemplo.
Presença de diretivas `{code-cell}` que serão executadas com seu livro.

É tudo o que você precisa para começar!

## Adicionar rapidamente metadados YAML para notebooks MyST

Se você tem um arquivo markdown e deseja adicionar rapidamente metadados YAML a ele, para que o Jupyter Book o trate como um Notebook MyST Markdown, execute o seguinte comando:

``` bash
jupyter-book myst init path/to/markdownfile.md
```
