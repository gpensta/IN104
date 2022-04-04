import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, RobustScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import plot_confusion_matrix
from sklearn.svm import LinearSVC

# Entraînement du classifieur

PATH = r'./data/features.csv'

dataset = pd.read_csv(PATH,sep=';')
columns = dataset.columns.tolist() # get the columns

batch_audio = pd.DataFrame(dataset).to_numpy()

features = batch_audio[:, 1:]
y = batch_audio[:, 0]

X_train, X_test, y_train, y_test = train_test_split(features, y, test_size=0.20, random_state=0)

model = LinearSVC(C=0.1, max_iter=1e6, tol=1e-4)
model.fit(X_train, y_train)

print("Performances du modèle sur la base de données de test : ", model.score(X_test, y_test))


# Plot Confusion Matrix

# labels = ['blues', 'classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']


# fig, ax = plt.subplots(figsize=(10, 10), dpi=300)
# plot_confusion_matrix(model, X_test, y_test, ax=ax, normalize='true', display_labels=labels)
# plt.savefig('confusion.png',transparent=False, facecolor='white' )