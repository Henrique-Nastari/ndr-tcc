# 🛡️ NDR (Network Detection and Response) com Machine Learning

## 📌 Descrição

Sistema de **detecção e resposta a intrusões em rede (NDR)** que captura tráfego em tempo real, extrai features e utiliza **Machine Learning** para **detectar e classificar múltiplos tipos de ataque**, exibindo os resultados em uma interface gráfica com sugestões de mitigação.

---

## 🎯 Objetivos

* Detectar tráfego malicioso em tempo real
* Classificar o tipo de ataque (multiclass)
* Integrar captura de pacotes + pipeline de ML
* Exibir resultados em GUI
* Fornecer recomendações de mitigação

---

## 🧠 Classes de Ataque (exemplo)

* BENIGN (normal)
* DDoS / DoS
* PortScan
* Brute Force (FTP/SSH)
* Web Attacks (SQLi, XSS)

> As classes dependem do dataset (CICIDS2017) e podem ser agrupadas para simplificação.

---

## 🏗️ Arquitetura (Lab Virtual)

```
Kali (Atacante)
        ↓
Rede Interna (VirtualBox: ndr_lab)
        ↓
Lubuntu (NDR: captura + ML + GUI)
        ↓
Ubuntu Server (Vítima)
```

---

## 🧰 Tecnologias

* **Python 3**
* **scapy** (captura de pacotes)
* **pandas / numpy** (dados)
* **scikit-learn** (ML)
* **joblib** (persistência de modelos)
* **Tkinter/PyQt (GUI)**
* **VirtualBox** (ambiente)

---

## 📊 Dataset

* **CICIDS2017 – MachineLearningCSV**

  * +80 features por fluxo
  * Labels multiclasses
  * Padrão acadêmico

---

## ⚙️ Funcionalidades

### ✅ Já implementado

* Captura de pacotes em tempo real com **Scapy**
* Extração de features básicas (IP, portas, protocolo, tamanho)
* Pipeline de leitura de dataset (CICIDS2017)
* Treinamento de modelo de Machine Learning
* Salvamento do modelo (`.pkl`) com **joblib**
* Sistema de predição com modelo carregado

### 🚧 Em desenvolvimento

* Classificação em tempo real integrada à captura
* Interface gráfica para visualização dos ataques
* Sistema de alertas (ex: tráfego suspeito detectado)
* Módulo de recomendação de mitigação por tipo de ataque

### 🔮 Futuro (melhorias)

* Suporte a múltiplos modelos (Random Forest, SVM, etc.)
* Dashboard com gráficos em tempo real
* Detecção de anomalias além de classificação supervisionada
* Logs estruturados para análise forense

---

## 🧩 Estrutura do Projeto (ATUAL)

```
ndr-tcc/
│
├── .venv/
│
├── data/
│   ├── .gitkeep
│   └── MachineLearningCVE/
│       ├── Friday-WorkingHours-Afternoon-DDoS.pcap_ISCX.csv
│       ├── Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv
│       ├── Friday-WorkingHours-Morning.pcap_ISCX.csv
│       ├── Monday-WorkingHours.pcap_ISCX.csv
│       ├── Thursday-WorkingHours-Afternoon-Infiltration.pcap_ISCX.csv
│       ├── Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv
│       ├── Tuesday-WorkingHours.pcap_ISCX.csv
│       └── Wednesday-workingHours.pcap_ISCX.csv
│
├── models/
│   ├── .gitkeep
│   ├── decision_tree_model.pkl
│   └── label_encoder.pkl
│
├── ndr/
│   ├── __init__.py
│   ├── capture.py                # captura de pacotes (scapy)
│   │
│   ├── gui/
│   │   ├── __init__.py
│   │   └── window.py             # interface gráfica
│   │
│   └── ml/
│       ├── __init__.py
│       ├── features.py           # extração/engenharia de features
│       ├── training.py           # treino e salvamento do modelo
│       └── predict.py            # carregamento e predição
│
├── main.py                       # ponto de entrada do sistema
├── README.md
└── .gitignore
```

---

## 🔁 Fluxo do Sistema

1. **capture.py** captura pacotes
2. **features.py** extrai atributos
3. **predict.py** carrega modelo e classifica
4. **GUI** exibe resultado + alerta

---

## 🚀 Como Executar

### 1. Instalar dependências

```bash
sudo apt update
sudo apt install python3-pip -y
pip install scapy pandas scikit-learn joblib
```

### 2. Treinar modelo

```bash
python3 ndr/ml/training.py
```

### 3. Executar sistema

```bash
sudo python3 main.py
```

> ⚠️ Uso de `sudo` necessário para captura de pacotes

---

---

## 🧠 Machine Learning

* Tipo: Classificação supervisionada
* Entrada: features de fluxo
* Saída: classe do tráfego

### Modelos iniciais

* Decision Tree (baseline)
* Random Forest (recomendado)

---

## ⚠️ Limitações

* Dataset offline ≠ rede real
* Simplificação de features em tempo real
* Dependência de VM para testes

---

## 📚 Referências

* CICIDS2017
* Scikit-learn
* Scapy

---

## 👨‍🎓 Autor

Henrique Nastari Corrêa 

---

## 📌 Observação

Projeto acadêmico com foco em:

* Segurança de redes
* Detecção de intrusões
* Machine Learning aplicado

---

🚀 Em desenvolvimento
