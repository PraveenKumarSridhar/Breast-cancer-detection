# Breast-cancer-detection

To build a deep neural network to accurately classify a histology image of breast samples as malignant or benign (i.e) containing IDC or not.

You can also find the link to the notebook [here](https://github.com/PraveenKumarSridhar/Breast-cancer-detection/blob/main/src/Training_V1.ipynb).

## 1.0 What is IDC?
Invasive ductal carcinoma (IDC), sometimes called infiltrating ductal carcinoma, is the most common type of breast cancer. About 80% of all breast cancers are invasive ductal carcinomas.

<img align="center" alt="IDC" src="https://raw.githubusercontent.com/PraveenKumarSridhar/Breast-cancer-detection/main/assets/IDC.jpg" width="500" height="300" />

Invasive means that the cancer has “invaded” or spread to the surrounding breast tissues. Ductal means that the cancer began in the milk ducts, which are the “pipes” that carry milk from the milk-producing lobules to the nipple. Carcinoma refers to any cancer that begins in the skin or other tissues that cover internal organs — such as breast tissue. All together, “invasive ductal carcinoma” refers to cancer that has broken through the wall of the milk duct and begun to invade the tissues of the breast. Over time, invasive ductal carcinoma can spread to the lymph nodes and possibly to other areas of the body.

According to the American Cancer Society, more than 180,000 women in the United States find out they have invasive breast cancer each year. Most of them are diagnosed with invasive ductal carcinoma.


## 2.0 Sample Data:

You can download the dataset from [here](https://www.kaggle.com/paultimothymooney/breast-histopathology-images/).
A sample data would look like this:

<p float = "left">
    <img  alt="Benign" src="https://raw.githubusercontent.com/PraveenKumarSridhar/Breast-cancer-detection/main/assets/Benign.png" width="300" height="300" />
    <img  alt="Malignant" src="https://raw.githubusercontent.com/PraveenKumarSridhar/Breast-cancer-detection/main/assets/Malignant.png" width="300" height="300" />
</p>

## 3.0 Environment and tools Used:
    1. Jupyter Notebook
    2. Numpy
    3. Matplotlib
    4. Tensorflow
    5. Keras
    6. sklearn
    7. imutils
    8. plotly

## 5.0 Architeture used:
Here we have used ResNet-50, this arch has 50 layer hence the name. It is defined as follows:

<img  alt="ResNet-50 Arch" src="https://raw.githubusercontent.com/PraveenKumarSridhar/Breast-cancer-detection/main/assets/resNet-50.png" width="300" height="300" />



## 4.0 Results:

<img  alt="results-confusion-matrix" src="https://raw.githubusercontent.com/PraveenKumarSridhar/Breast-cancer-detection/main/assets/confusion-matrix.png" width="300" height="300" />

## 5.0 Sources:
    1. https://www.kaggle.com/paultimothymooney/breast-histopathology-images/
    2. https://www.breastcancer.org/symptoms/types/idc
    3. Coursera
