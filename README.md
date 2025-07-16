# RAG_CRC: Retrieval-Augmented Deep Learning for MHC-Agnostic Prediction of Colorectal Cancer Neoantigen Immunogenicity
Yu-Chen Liu,  Yan-Yun Chang, Cheng-Che Chuang, Yu-Yen Ou
|[ 🎇&nbsp;Abstract](#abstract) |[📃&nbsp;Dataset](#Dataset) | |[ 💾&nbsp;Requirements](#requirement)|[ 📚&nbsp;License](#License)|
|-------------------------------|-----------------------------|---------------------------------------|-----------------------------|

## 🎇Abstract <a name="abstract"></a>
Colorectal cancer (CRC) imposes a significant global health burden. Personalized immunotherapy holds immense promise by targeting tumor-specific neoantigens, which are unique peptide fragments arising from mutations. The successful development of epitope-based cancer vaccines and T-cell therapies hinges on identifying truly immunogenic neoantigens capable of eliciting potent anti-tumor T cell responses. However, traditional methods for predicting neoantigen immunogenicity often lack accuracy, particularly when operating independently of specific MHC allele information (MHC-agnostic). This study presents RAG_CRC, a novel deep learning framework that integrates Retrieval-Augmented Generation (RAG) with a hybrid Multi-window Convolutional Neural Network and Bidirectional Long Short-Term Memory architecture (MC-LSTM) for accurate and MHC-agnostic prediction of neoantigen immunogenicity. RAG_CRC leverages ProstT5, a state-of-the-art structure-aware pretrained protein language model, to generate rich embedding representations of peptide sequences. By incorporating a RAG-based similarity retrieval and embedding augmentation strategy using curated antigen databases, RAG_CRC effectively captures both multi-scale local patterns and long-range sequential dependencies relevant for immunogenicity, significantly improving prediction performance compared to baseline methods relying solely on PLM embeddings or alternative architectures. We demonstrate the performance of RAG_CRC on rigorously curated datasets, achieving an ROC-AUC of 0.8762 on an independent test set and correctly classifying 11 out of 13 clinically relevant neoantigens, highlighting its potential for advancing the selection of high-quality candidates for personalized CRC immunotherapies.
<br>

![workflow]()

## 📃Dataset <a name="Dataset"></a>

| Experiment Dataset | Origin           | Remove similarity <40% |  Train (80%)    | Test (20%)    |
|--------------------|------------------|------------------------|-----------------|---------------|
| Neo antigen        | 754              | 295                    | 2393            | 59            |
| General antigen    | 6226             | 307                    | 598             | 62            |

| RAG Database       | Origin           | Remove similarity <40%|
|--------------------|------------------|-----------------------|
| Neo antigen        | 3032             | 1057                  |
| General antigen    | 120599           | 5652                  |


## 💾&nbsp;Requirements <a name="requirement"></a>
```bash
h5py==3.11.0
tqdm==4.66.4
numpy==1.26.4
scikit-learn==1.4.2
tensorflow==2.10.1
transformers==4.40.1
torch==2.3.0+cu118
```

## 📚&nbsp;License <a name="License"></a>
Licensed under the Academic Free License version 3.0
