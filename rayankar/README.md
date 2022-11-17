# DevOps Test

## Must do:

1. [GitOps Principles](https://en.wikipedia.org/wiki/DevOps#GitOps)
2. Boostrap script or Ansible Code
3. Document your solution

## Steps

1. Please clone this repository into a new private github repository and add below repository as a git submodule,
https://github.com/Star2Billing/a2billing


2. Follow the INSTALL.rst, this guid is design to run the software in a single VM,
you need to separate the services into 5 Kuberenetes services in two helm charts as below (Deployments).

Of course you you can also skip the part for "Callback Service"

Create a helm chart called a2billing with below deployments

1. `web-customer`: Docker image: php-apache (ingress: http://cluster/customer)
2. `web-admin`: Docker image: php-apache (ingress: http://cluster/admin)
3. `sip-server`: Dockerize asterisk asterisk (ingress:  sip://cluster TCP/UDP 5060)

Create a second helm chart with deployments
1. `db-server`: mysql 
2. `phpmyadmin`: phpMyAdmin (ingress: http://cluster/phpmyadmin)

Note for the Asterisk: you can use CHAN_SIP which is the legacy asterisk module for SIP Server and can configure with `sip.conf` 
and it is recommended to use asterisk 11 to 13 for above (It's OLD!)

Note for PHP: requested php version is 5, but it should also work php 7.x 

3. Test customer portal : try to register when navigating to customer 

4. Test admin portal : you must be able to login and see the customer you just registered

5. (Nice to do) Add CI/CD  Pipeline (You can choose Azure or Gitlab) for automatic testing and automatic deployment

6. (Nice do do) Once your cluster is up and running, you must be able to use the client you have registered
register with a SIP client softphone to your asterisk on port 5060.

- For Windows you can use MicroSIP from https://www.microsip.org/
- For linux/mac you can use [Jitsi](https://jitsi.org/downloads/)

7. We expect to see a single bash script or ansible to bootstrap the build/deployment process for locally execution of the assignment in
minimkube or kind environment.

if it works, dialing 77 should announce your credit. provided you have modified extensions.conf to below:

```

[a2billing]
include => a2billing_callingcard
include => a2billing_monitoring
include => a2billing_voucher

```

Share the result with user: `mason-chase` on GitHub in private mode.

