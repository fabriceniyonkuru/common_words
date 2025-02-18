{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOmzmRw6+XmSI5ttCJ2nVqf",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/fabriceniyonkuru/common_words/blob/main/common_words.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vVxXHpfe7JW6",
        "outputId": "5ac98e03-0613-4d46-8e7e-75bd0d7ad2b0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "similality 0.64\n",
            "common words {'past', 'the', 'is', 'of', 'systematic', 'study', 'History'}\n"
          ]
        }
      ],
      "source": [
        "file1 = \"History is the systematic study of the past\"\n",
        "file2 = \"History is the systematic study of the past this is just for practice\"\n",
        "def jaccard_simularity(text1,text2):\n",
        "  set1 = set(text1.split())\n",
        "  set2 = set(text2.split())\n",
        "\n",
        "  intersection = set1.intersection(set2)\n",
        "  union = set1.union(set2)\n",
        "  similarity = len(intersection) / len (union)\n",
        "  return similarity, intersection\n",
        "\n",
        "similarity,common_words=jaccard_simularity(file1,file2)\n",
        "print(f\"similality {similarity:.2f}\")\n",
        "print(\"common words\",common_words)"
      ]
    }
  ]
}