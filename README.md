
# 人脸检测


---
## 实验目的
1. 理解和掌握基于神经网络的人脸检测方法的理论基础知识。
2. 理解[MTCNN](https://kpzhang93.github.io/MTCNN_face_detection_alignment/paper/spl.pdf)人脸检测的基本流程，并加以实践。



## 实验环境
[anaconda3](https://www.anaconda.com/download/)
[pytorch 0.4.1](https://pytorch.org/)
[torchvision](https://pytorch.org/)
[opencv-python](https://pypi.org/project/opencv-python/)等。



## 实验步骤
**一、获取代码**

实验完整代码[mtcnn_pytorch](https://github.com/xiezheng-cs/mtcnn_pytorch)，可直接下载或是通过git clone命令下载。
```bash
git clone https://github.com/xiezheng-cs/mtcnn_pytorch.git
```

**二、实验环境安装**
1. 确保本机或是服务器已安装好[anaconda3](https://www.anaconda.com/download/)环境；
2. pip或conda安装[pytorch 0.4.1 和 torchvision](https://pytorch.org/)环境；
3. pip或conda安装[opencv-python](https://pypi.org/project/opencv-python/)环境；

```bash
pip install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-win_amd64.whl     # Windows
pip install http://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-linux_x86_64.whl  # Linux
pip install torchvision
pip install opencv-python
```

**三、简单测试给定模型**

直接使用我们[训练好的网络模型](https://github.com/xiezheng-cs/mtcnn_pytorch/releases)在给定的测试数据集(位于mtcnn_pytorch/data/test_images/目录下,共64张测试图片)，运行以下命令，即可在mtcnn_pytorch/data/you_result/目录下查看检测结果。
```bash
cd mtcnn_pytorch/
python test_image.py
```

**四、训练步骤**
1. 准备好训练数据，包括 wider face 和 TCDCN两个数据集，前者用来训练人脸框，后者用来训练关键点。
2. 依次训练pnet, rnet, onet.
先运行preprocessing目录下的gen_pnet_data.py，它会生成许多12x12大小的训练样本图像。
3. 运行assemble_pnet_imglist.py，它会生成训练图像列表和标签。
4. 运行training/pnet目录下train.py，开始训练，默认训练50个epoch
5. 与2-4步相同，完成rnet和onet的训练。
6. 用自己的模型测试吧。

有几个需要修改的地方：
代码根目录下config.py，ROOT_DIR 修改为你自己的代码根目录的绝对路径。
training目录下 pnet,rnet,onet三个目录下分别有train.py，把里面的os.chdir那一行的路径改为你的代码根目录。

-----
