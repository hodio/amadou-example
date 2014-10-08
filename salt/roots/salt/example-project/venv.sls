include:
  - nginx

# Create the Python Virtual environment
/home/vagrant/env:
  virtualenv.managed:
    - no_site_packages: True
    - distribute: True
    - runas: vagrant
    - requirements: /vagrant/project/requirements.txt  
    - require:
      - pkg: python-virtualenv
      - pkg: python-dev
      - pkg: postgresql-server-dev-9.1
      - pkg: libxml2-dev
      - pkg: libxslt1-dev
      - pkg: libjpeg62-dev