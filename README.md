# 🧠 Deep Learning

This repository documents my journey of learning **Deep Learning with PyTorch** through hands-on implementations, experiments, and projects.

The repository covers fundamental deep learning concepts including **ANNs, CNNs, RNNs, Activation Functions, and Transformers**.

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

### 🔹 Transformer

This section explores Transformer-based architectures and their application to Natural Language Processing.

- Text Summarization
- SAMSum Dataset
- Transformer-based Text Summarization Model

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
│   ├── neuron.ipynb
│   ├── ANN_Regression.ipynb
│   ├── ANN_Classification.ipynb
│   ├── powerplant_data.csv
│   ├── DateFruit_Dataset.csv
│   └── best_model.pt
│
├── CNN/
│   ├── Cats_&_Dogs/
│   │   ├── data/
│   │   └── CNN_For_Cats&Dogs.ipynb
│   │
│   └── CIFAR10/
│       ├── data/
│       └── CNN_For_CIFAR10.ipynb
│
├── RNN/
│   ├── data/
│   ├── IMDB Dataset.csv
│   ├── Sentiment_Analysis.ipynb
│   └── HandwrittenDigitClassification.ipynb
│
├── Transformer/
│   ├── dataset/
│   │   ├── samsum-test.csv
│   │   └── samsum-validation.csv
│   │
│   ├── results/
│   ├── saved_summary_model/
│   └── text_summarizer.ipynb
│
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies

- Python
- PyTorch
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- Transformers
- Hugging Face