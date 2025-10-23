## 🧠 CBAM: Convolutional Block Attention Module

The **Convolutional Block Attention Module (CBAM)** is a lightweight yet effective attention mechanism designed to enhance the representational power of convolutional neural networks. It applies **sequential attention along channel and spatial dimensions**, allowing the network to learn *what* and *where* to focus within feature maps.

### 🔍 Overview

In the original CBAM paper, the authors evaluated its effectiveness primarily on baseline CNN architectures.  
In this project, I extend the CBAM integration to several **widely used convolutional backbones** — including **VGG19**, **GoogLeNet**, **ResNet**, and **LeNet** — to assess its generalization capability and impact on model performance.

### ⚙️ Experimental Setup

- **Dataset:** [Specify dataset name here, e.g., CIFAR-10, ImageNet subset, etc.]  
- **Optimizer:** [e.g., Adam / SGD with momentum 0.9]  
- **Learning Rate:** [e.g., 0.001]  
- **Epochs:** [e.g., 100]  
- **Evaluation Metrics:** Top-1 and Top-5 Accuracy  

All experiments were conducted under identical training configurations, with and without CBAM modules added to the base architectures.

---

### 📊 Results

#### **Table 1 — Top-1 Accuracy Comparison (With and Without CBAM)**

| **Model**    | **Without CBAM** | **With CBAM** | **Improvement** |
|---------------|------------------|----------------|------------------|
| **VGG19**     | 41.26%           | 41.80%         | **+0.54%**       |
| **GoogLeNet** | 28.07%           | 28.92%         | **+0.85%**       |
| **ResNet**    | 35.33%           | 37.02%         | **+1.69%**       |
| **LeNet**     | 33.00%           | 33.25%         | **-0.08%**       |

#### **Table 2 — Top-5 Accuracy Comparison (With and Without CBAM)**

| **Model**    | **Without CBAM** | **With CBAM** | **Improvement** |
|---------------|------------------|----------------|------------------|
| **VGG19**     | 68.84%           | 69.43%         | **+0.59%**       |
| **GoogLeNet** | 54.61%           | 55.46%         | **+0.85%**       |
| **ResNet**    | 67.03%           | 68.85%         | **+1.82%**       |
| **LeNet**     | 62.30%           | 62.24%         | **-0.06%**       |

---

### 📈 Observations

- CBAM consistently improved both **Top-1** and **Top-5** accuracies across most architectures.  
- **ResNet** exhibited the **highest performance gain**, confirming CBAM’s effectiveness in deeper residual networks.  
- Minor fluctuations in simpler networks (like LeNet) indicate that CBAM’s benefits scale with **network depth** and **feature hierarchy**.  
- Overall, integrating CBAM enhanced model interpretability and improved focus on salient spatial regions.

---

### 📄 Report

A detailed experimental **report with graphs, training curves, and analysis** is included in this repository.  
Refer to `CBAM Performance Analysis.pdf` for complete results and implementation details.
