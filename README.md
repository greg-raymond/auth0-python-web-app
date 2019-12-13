# Auth0 Python Web App

[![CircleCI](https://circleci.com/gh/auth0-samples/auth0-python-web-app.svg?style=svg)](https://circleci.com/gh/auth0-samples/auth0-python-web-app)

This repository contains the source code for the [Python Web App Quickstart](https://auth0.com/docs/quickstart/webapp/python).

## What is Auth0?

Auth0 helps you to easily:

- implement authentication with multiple identity providers, including social (e.g., Google, Facebook, Microsoft, LinkedIn, GitHub, Twitter, etc), or enterprise (e.g., Windows Azure AD, Google Apps, Active Directory, ADFS, SAML, etc.)
- log in users with username/password databases, passwordless, or multi-factor authentication
- link multiple user accounts together
- generate signed JSON Web Tokens to authorize your API calls and flow the user identity securely
- access demographics and analytics detailing how, when, and where users are logging in
- enrich user profiles from other data sources using customizable JavaScript rules

[Why Auth0?](https://auth0.com/why-auth0)

## Issue Reporting

If you have found a bug or if you have a feature request, please report them at this repository issues section. Please do not report security vulnerabilities on the public GitHub issue tracker. The [Responsible Disclosure Program](https://auth0.com/whitehat) details the procedure for disclosing security issues.

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more info.

## HealthEngine Configuration

This is example program is taken from auth0 and edited to provide a quick start for external vendors. In this case, it will allow you to request an access_token & refresh_token for a specific practice which is to be included in the Authorization header with the prefix Bearer.

How to run:
1. Install python
2. Run pip install -r requirements.txt from the Login-01 folder
3. Configure a .env file with the required fields given from HealthEngine
4. Run python server.py
5. In a web browser visit localhost:3000
6. Complete the login flow and take the access_token from the last page
