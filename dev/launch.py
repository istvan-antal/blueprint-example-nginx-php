#!/usr/bin/env python
from blueprint import Infrastructure
import argparse

parser = argparse.ArgumentParser(description='Launch the application.')
parser.add_argument('--env', metavar='env', type=str, help='Environment to launch in.', default='cni-dev')
parser.add_argument('--name', metavar='name', type=str, help='Application name.', default='php-nginx')
args = parser.parse_args()

blueprint = Infrastructure(environment=args.env)
instance = blueprint.create_instance(id=args.name)

instance.provision()
instance.setup_generic_php()

instance.clone_project('git@github.com:istvan-antal/blueprint-example-nginx-php.git')

instance.use_nginx_config('nginx.conf')

instance.install_my_key()