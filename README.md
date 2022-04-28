# Image to LaTeX

An application that maps an image of a LaTeX math equation to LaTeX code.

## Introduction

The problem of image-to-markup generation was attempted by [Deng et al. (2016)](https://arxiv.org/pdf/1609.04938v1.pdf). They extracted about 100K formulas by parsing LaTeX sources of papers from the arXiv. They rendered the formulas using pdflatex and converted the rendered PDF files to PNG format. The raw and preprocessed versions of their dataset are available [online](http://lstm.seas.harvard.edu/latex/data/). In their model, a CNN is first used to extract image features. The rows of the features are then encoded using a RNN. Finally, the encoded features are used by an RNN decoder with an attention mechanism. The model has 9.48 million parameters in total. Recently, Transformer has overtaken RNN for many language tasks, so I thought I might give it try in this problem.

## Methods

Using their dataset, I trained a model that uses ResNet-18 as encoder with 2D positional encoding and a Transformer as decoder with cross-entropy loss. (Similar to the one described in [Singh et al. (2021)](https://arxiv.org/pdf/2103.06450.pdf), except that I used ResNet only up to block 3 to reduce computational costs, and I excluded the line number encoding as it doesn't apply to this problem.) The model has about 3 million parameters.
