===========
Aws Helpers
===========

AWS Helpers - to accelerate hard jobs with AWS Route53

Setup
=====

- Execute: ``python awshelpers/main.py``
- Install: ``python setup.py install``
- Environment with:
- - aws_access_key_id
- - aws_secret_access_key


usage: ``awshelpers [option]``
======

Route53 functions:
==================

- List hosted zones
- Get zone id from a domain name
- Remove zone
- Add subdomain A to a specific domain
- Remove subdomain A from a specific domain
- Add subdomain A to all domains
- Remove subdomain A from all domains
- Create zone with the given domain-name and the values specified in settings file under the domain-type block
- - An option to check the settings file. See the provided ``settings_sample.yml`` file


