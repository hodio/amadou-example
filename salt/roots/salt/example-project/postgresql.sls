include:
  - postgresql

example-postgres-user:
  postgres_user.present:
    - name: example_user
    - createdb: example_db
    - password: example_password
    - runas: postgres
    - require:
      - service: postgresql

example-postgres-db:
  postgres_database.present:
    - name: example_db
    - encoding: UTF8
    - lc_ctype: en_US.UTF8
    - lc_collate: en_US.UTF8
    - template: template0
    - owner: example_user
    - runas: postgres
    - require:
        - postgres_user: example-postgres-user