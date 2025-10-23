🧠 CBAM: Convolutional Block Attention Module

The Convolutional Block Attention Module (CBAM) is a lightweight yet powerful attention mechanism widely used in computer vision tasks to enhance model performance by refining feature representations. It sequentially infers channel and spatial attention maps, enabling the network to focus on what and where to emphasize in feature maps.

In the original paper, CBAM was primarily integrated with a baseline CNN architecture to demonstrate its efficacy in improving accuracy and IoU (Intersection over Union).

In this project, I extended CBAM beyond the baseline and integrated it with several state-of-the-art vision backbones — including popular architectures such as ResNet, DenseNet, EfficientNet, and MobileNet. The objective was to evaluate how CBAM generalizes across different model families and its impact on performance metrics.

After conducting extensive experiments across these architectures, CBAM consistently improved both accuracy and IoU, validating its versatility and effectiveness in enhancing spatial and channel-wise feature refinement.

A comprehensive experimental report containing results, visualizations, and comparative analysis is also included in this repository.
