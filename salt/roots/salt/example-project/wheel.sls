/home/vagrant/wheel:
  file.directory:
    - user: vagrant

# Manage the tar file containing all the requirements
/home/vagrant/wheel/wheel-requirements.tar.gz:
  file.managed:
    - source: https://s3.amazonaws.com/gibbon-deployment/wheel-requirements.tar.gz
    - source_hash: md5=932669db31cc05684786e4a8bf771a3c
    - user: vagrant
    - require:
      - file: /home/vagrant/wheel

# Extract the archive when it changes
extract-wheel:
  cmd.wait:
    - user: vagrant
    - cwd: /home/vagrant/wheel
    - name: tar -zxf /home/vagrant/wheel/wheel-requirements.tar.gz
    - watch:
      - file: /home/vagrant/wheel/wheel-requirements.tar.gz
    - require:
      - file: /home/vagrant/wheel

# Install all the requirements
example-wheel:
  cmd.wait:
    - name: /home/vagrant/env/bin/pip install --use-wheel --no-index --find-links=/home/vagrant/wheel/example -r /vagrant/project/requirements.txt
    - require:
      - cmd: pip-wheel
      - virtualenv: /home/vagrant/env
    - watch:
      - file: /home/vagrant/wheel/wheel-requirements.tar.gz
    - require:
        - cmd: pip-dev
        - cmd: pip-distribute
        - cmd: extract-wheel
        - virtualenv: /home/vagrant/env
