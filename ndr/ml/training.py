import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
import joblib
import os
import glob
import sys

# Define o caminho para a pasta com os datasets e para salvar o modelo
DATASET_DIR = 'MachineLearningCVE'
MODEL_DIR = 'models'
MODEL_PATH = os.path.join(MODEL_DIR, 'decision_tree_model.pkl')
ENCODER_PATH = os.path.join(MODEL_DIR, 'label_encoder.pkl')

def train_model():
    """
    Carrega TODOS os datasets, treina um modelo de Árvore de Decisão e o salva.
    """
    print("[Treinamento] Iniciando o processo de treinamento com todos os datasets...")

    if not os.path.exists(MODEL_DIR):
        os.makedirs(MODEL_DIR)

    # --- Carregamento de Múltiplos Arquivos ---
    try:
        csv_files = glob.glob(os.path.join(DATASET_DIR, '*.csv'))
        if not csv_files:
            print(f"[!] Erro: Nenhum arquivo .csv encontrado no diretório '{DATASET_DIR}'.")
            return
            
        print(f"[Treinamento] Encontrados {len(csv_files)} arquivos CSV para carregar.")
        
        df_list = []
        for i, filename in enumerate(csv_files):
            print(f"[Treinamento] Carregando arquivo {i+1}/{len(csv_files)}: {os.path.basename(filename)}...")
            df_temp = pd.read_csv(filename)
            df_list.append(df_temp)
        
        print("[Treinamento] Combinando todos os datasets em um só...")
        df = pd.concat(df_list, ignore_index=True)
        print(f"[Treinamento] Dataset combinado criado com {len(df)} linhas.")

        df.columns = df.columns.str.strip()

    except Exception as e:
        print(f"[!] Ocorreu um erro inesperado durante o carregamento: {e}")
        return

    # 2. Selecionar features e label (ADAPTADO PARA AS COLUNAS QUE REALMENTE EXISTEM)
    features = ['Destination Port'] # Usando apenas a feature que temos certeza que existe
    label = 'Label'
    
    print(f"[Treinamento] Features selecionadas (Adaptado): {features}")
    print(f"[Treinamento] Label: {label}")

    # 3. Limpeza de dados
    # Verifica se as colunas realmente existem antes de usá-las
    required_cols = features + [label]
    if not all(col in df.columns for col in required_cols):
        print(f"[!] Erro: Nem todas as colunas necessárias {required_cols} foram encontradas no dataset combinado.")
        print(f"    Colunas disponíveis: {df.columns.tolist()}")
        return

    df_clean = df[required_cols].dropna()
    df_clean = df_clean[df_clean[label] != 'Label']

    # 4. Codificar a Label
    le = LabelEncoder()
    df_clean[label] = le.fit_transform(df_clean[label])
    
    print(f"[Treinamento] Classes encontradas e codificadas: {list(le.classes_)}")

    # 5. Dividir dados para treino e teste
    X = df_clean[features]
    y = df_clean[label]
    
    if X.empty or y.empty:
        print("[!] Erro: Não há dados suficientes para treinar.")
        return
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # 6. Treinar o modelo
    print("[Treinamento] Treinando o modelo de Árvore de Decisão (isso pode levar um tempo)...")
    clf = DecisionTreeClassifier(random_state=42, max_depth=10)
    clf.fit(X_train, y_train)

    # 7. Avaliar o modelo
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"[Treinamento] Acurácia do modelo no conjunto de teste: {acc:.4f}")

    # 8. Salvar o modelo e o encoder
    print(f"[Treinamento] Salvando modelo treinado em '{MODEL_PATH}'")
    joblib.dump(clf, MODEL_PATH)
    
    print(f"[Treinamento] Salvando o codificador de labels em '{ENCODER_PATH}'")
    joblib.dump(le, ENCODER_PATH)
    
    print("\n[Treinamento] PROCESSO DE TREINAMENTO COMPLETO!")

if __name__ == '__main__':
    train_model()
