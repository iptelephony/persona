## Persona - ERPNext custom app

###Announcement 13 August 2024
This app will not be maintained anymore, since ERPNext v15 already has a similar feature. Thanks supporting this project.


Persona is a custom ERPNext app that Allows administrator or a system manager to impersonate another user. Inspired by [Administrator should be able to impersonate any user #17615](https://github.com/frappe/erpnext/issues/17615).

1. Only "Administrator" or "System Manager" roles can impersonate another user.
2. Adds a button "Impersonate" to User form.
3. Will generate 2 entries in activity log.
	1. One will show that the Administrator/System Manager who is impersonating a user.
	2. A second entry shows that the impersonated user logging in.
4. As a safeguard, we don't allow a system manager to impersonate another system manager.


### Installation 

```
bench get-app https://github.com/iptelephony/persona
bench --site sitename install-app persona 
bench migrate
bench restart
bench clear-cache
```

#### License

MIT
