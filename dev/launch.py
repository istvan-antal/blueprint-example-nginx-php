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

print "Instance ready, use the following command to SSH in:"
print instance.get_ssh_command() + "\n"

instance.install_my_key()

#print "To install your public key run:"
#print instance.get_ssh_command() + " \"echo '$(cat ~/.ssh/id_rsa.pub)' >> ~/.ssh/authorized_keys\"" + "\n"

print "For mail sending please run: sudo apt-get install postfix"