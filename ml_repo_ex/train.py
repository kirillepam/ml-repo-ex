from dataclasses import asdict

import click
import mlflow
from mlflow.models import infer_signature
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

from ml_repo_ex.config import Config


def train(params: Config):
    print('In train')
    # Load the Iris dataset
    X, y = datasets.load_iris(return_X_y=True)

    # Split the data into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    lr = LogisticRegression(**asdict(params))
    lr.fit(X_train, y_train)

    # Predict on the test set
    y_pred = lr.predict(X_test)

    # Calculate metrics
    accuracy = accuracy_score(y_test, y_pred)

    return accuracy, X_train, lr


@click.command()
@click.option('--path', default='configs/conf.yaml')
def run(path: str):
    print('In run')
    config = Config.load_config(path)
    accuracy, X_train, lr = train(config)
    print('out of train')
    # Set our tracking server uri for logging
    # mlflow.set_tracking_uri(uri="http://127.0.0.1:8080")
    # Create a new MLflow Experiment
    mlflow.set_experiment('MLflow Quickstart')
    # Start an MLflow run
    with mlflow.start_run():
        # Log the hyperparameters
        mlflow.log_params(asdict(config))
        # Log the loss metric
        mlflow.log_metric('accuracy', accuracy)
        # Set a tag that we can use to remind ourselves what this run was for
        mlflow.set_tag('Training Info', 'Basic LR model for iris data')
        # Infer the model signature
        signature = infer_signature(X_train, lr.predict(X_train))
        # Log the model
        mlflow.sklearn.log_model(
            sk_model=lr,
            artifact_path='iris_model',
            signature=signature,
            input_example=X_train,
            registered_model_name='tracking-quickstart',
        )


if __name__ == '__main__':
    run()  # pylint: disable=no-value-for-parameter
