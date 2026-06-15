from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


def MarvellousCalculateAccuracyDecisionTree():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data,target,test_size=0.5,random_state=45)

    model = tree.DecisionTreeClassifier()

    model.fit(X_train, Y_train)

    predictions = model.predict(X_test)

    Accuracy = accuracy_score(predictions,Y_test)
    return Accuracy

def MarvellousCalculateAccuracyKNN():
    iris = load_iris()

    data = iris.data
    target = iris.target

    X_train, X_test, Y_train, Y_test = train_test_split(data,target,test_size=0.5,random_state=45)

    model = KNeighborsClassifier()

    model.fit(X_train, Y_train)

    predictions = model.predict(X_test)

    Accuracy = accuracy_score(predictions,Y_test)
    return Accuracy

def main():
    Result1 = MarvellousCalculateAccuracyDecisionTree()
    Result2 = MarvellousCalculateAccuracyKNN()


    print("Accuracy of decision tree is:",Result1)
    print("Accuracy of KNN classifier is:",Result2)

if __name__=="__main__":
    main()