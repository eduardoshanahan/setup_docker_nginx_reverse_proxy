def task_build_monkeysign():
    '''Build and tag a docker image - usage: build_monkeysign -t:0.0.1 (default: "latest")'''
    return {
        'actions': [
            'docker build --rm --tag monkeysign:%(tag)s ./monkeysign/.',
            'docker build --rm --tag monkeysign:latest ./monkeysign/.',
        ],
        'params': [
            {
                'name': 'tag',
                'short': 't',
                'default': 'latest'
            },
        ],
        'verbosity': 2
    }

def task_run_monkeysign():
    '''Run the container of a monkey sign, available at localhost:8081 - usage: run_monkey_sign -t:0.0.1 (default: "latest")'''
    return {
        'actions': [
            'docker run --rm -it -p 8081:80 --name monkeysign monkeysign:%(tag)s',
        ],
        'params': [
            {
                'name': 'tag',
                'short': 't',
                'default': 'latest'
            },
        ],
        'verbosity': 2
    }

def task_run_two_monkeys():
    '''Run the two monkeys, available at localhost:8081 and 8082 - usage: run_two_monkeys -t 0.0.1 (default: "latest")'''
    return {
        'actions': [
            'TAG=%(tag)s docker compose -f ./monkeysign/docker-compose.yml up',
        ],
        'params': [
            {
                'name': 'tag',
                'short': 't',
                'default': 'latest'
            },
        ],
        'verbosity': 2
    }
    
def task_list_certificates():
    '''List the SSL certificates available'''
    return {
        'actions': [
            'docker compose -f ./certbot-dnscloudflare/docker-compose.list.yml up'
        ],
        'verbosity': 2
    }

def task_issue_certificate():    
    '''Issue a certificate for a given domain - usage: issue_certificate -d domain.com (required)'''
    return {
        'actions': [
            'DOMAIN=%(domain)s docker compose -f ./certbot-dnscloudflare/docker-compose.issue.yml up'
        ],
        'params': [
            {
                'name': 'domain',
                'short': 'd',
                'default': 'no domain provided'
            },
        ],
        'verbosity': 2
    }

def task_revoke_certificate():    
    '''Revoke the certificate for a given domain - usage: revoke_certificate -d domain.com (required)'''
    return {
        'actions': [
            'DOMAIN=%(domain)s docker compose -f ./certbot-dnscloudflare/docker-compose.revoke.yml up'
        ],
        'params': [
            {
                'name': 'domain',
                'short': 'd',
                'default': 'no domain provided'
            },
        ],
        'verbosity': 2
    }