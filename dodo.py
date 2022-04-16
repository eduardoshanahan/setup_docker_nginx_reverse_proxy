def task_build_monkeysign():
    """Build and tag a docker image"""
    return {
        'actions': [
            'docker build --rm --tag monkeysign ./monkeysign/.',
        ]
    }

def task_run_monkeysign():
    """Run the container of a monkey sign, available at localhost:8081"""
    return {
        'actions': [
            'docker run --rm -it -p 8081:80 --name monkeysign monkeysign',
        ],
        'verbosity': 2
    }

def task_run_two_monkeys():
    """Run the two monkeys, available at localhost:8081 and 8082"""
    return {
        'actions': [
            'docker compose -f ./monkeysign/docker-compose.yml up',
        ],
        'verbosity': 2
    }
    