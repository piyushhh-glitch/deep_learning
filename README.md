# 🧠 Deep Learning

This repository documents my journey of learning **Deep Learning with PyTorch** through hands-on implementations, experiments, and projects.

The repository covers fundamental deep learning concepts including **ANNs, CNNs, RNNs, GANs, Activation Functions, and Transformers**.

---

## 📚 Topics Covered

### 🔹 Activation Functions

This section contains implementations and experiments with commonly used activation functions:

- ReLU
- Sigmoid
- Softmax
- Tanh

---

### 🔹 ANN

Artificial Neural Networks are used for regression and classification tasks. This section contains implementations to understand the fundamentals of neural networks.

- Neural Network from Scratch
- ANN for Regression
- ANN for Classification

---

### 🔹 CNN

Convolutional Neural Networks are designed for image-based tasks. The projects focus on image classification using custom CNN architectures.

- CNN for Cats vs Dogs Classification
- CNN for CIFAR-10 Image Classification

---

### 🔹 RNN

Recurrent Neural Networks are designed for sequential data. This section contains implementations for:

- IMDB Sentiment Analysis
- Handwritten Digit Classification

---

### 🔹 GAN

Generative Adversarial Networks are used for generating new data samples. This section contains implementations of:

- Vanilla GAN
- DCGAN
- CelebA Dataset

---

### 🔹 Transformer

This section explores Transformer-based architectures and their application to Natural Language Processing.

- Text Summarization
- SAMSum Dataset
- Transformer-based Text Summarization Model

---

### 🔹 APIs

This section contains experiments with APIs and their integration with Python applications.

- Gemini API

---

## 📁 Project Structure

```text
deep_learning/
│
├── Activation_Functions/
│   ├── ReLU.ipynb
│   ├── Sigmoid.ipynb
│   ├── softmax.ipynb
│   └── tanh.ipynb
│
├── ANN/
│   ├── ANN_Classification.ipynb
│   ├── ANN_Regression.ipynb
│   ├── DateFruit_Dataset.csv
│   ├── neuron.ipynb
│   ├── powerplant_data.csv
│   └── best_model.pt
│
├── Api's/
│   ├── .env
│   ├── Gemini.ipynb
│   └── image.png
│
├── CNN/
│   ├── Cats_&_Dogs/
│   └── CIFAR10/
│
├── GAN/
│   ├── img_align_celeba/
│   ├── DCGAN.ipynb
│   └── vanilla_gan.ipynb
│
├── RNN/
│   ├── data/
│   ├── IMDB Dataset.csv
│   ├── Sentiment_Analysis.ipynb
│   └── HandwrittenDigitClassification.ipynb
│
├── Transformer/
│   ├── dataset/
│   ├── results/
│   ├── saved_summary_model/
│   └── text_summarizer.ipynb
│
├── .gitignore
└── README.md