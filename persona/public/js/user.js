frappe.ui.form.on('User', {
    refresh: function(frm, cdt, cdn) {

  
	function canImpersonate(user, target) {
        	if((frappe.session.user === 'Administrator' || frappe.user.has_role("System Manager"))  && frappe.session.user !== frm.doc.name) {
			return true;
		}

		return false;
	}

        if (canImpersonate(frappe.session.user, frm.doc.name)) {
            frm.add_custom_button(__("Impersonate"), function () {

                frappe.call({
                    method: 'persona.api.user.impersonate',
                    args: {
                        user: frm.doc.name,

                    },
                    callback: function (r) {
			if (r.message.status === 'Success') {
                        	frappe.show_alert({message: r.message.message, indicator: 'green'});
				 location.reload(true);
			} else {
			    frappe.throw(r.message.message);
			}
                    }
                })
            });
        }

    },

});
