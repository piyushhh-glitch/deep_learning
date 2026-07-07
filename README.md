# deep_learning

🧠

Documenting my journey of learning and building Deep Learning models using PyTorch. Covers ANN, CNN, RNN, GANs, Computer Vision, Transfer Learning.

## ANN

Artificial Neural Networks (ANNs) are the foundation of Deep Learning. They learn patterns from data using interconnected neurons and are commonly used for regression and classification tasks.

## CNN

Convolutional Neural Networks (CNNs) are designed for image data. They automatically extract features using convolution and pooling layers, making them highly effective for computer vision tasks like image classification.

## Project Structure

```text
deep_learning/
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
│   │   │   └── PetImages/
│   │   │       ├── Cat/
│   │   │       └── Dog/
│   │   └── CNN_For_Cats&Dogs.ipynb
│   │
│   ├── CIFAR10/
│   │   ├── data/
│   │   │   └── cifar-10-batches-py/
│   │   └── CNN_For_CIFAR10.ipynb
│
└── README.md
```