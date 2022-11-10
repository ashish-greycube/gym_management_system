frappe.pages['my-gym-profile'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'My Gym Profile',
		single_column: true
	});
	// frappe.require('/assets/gym_management_system/js/gym_bundle.js',()=>{console.log('loaded')})
	$(frappe.render_template("my_gym_profile")).appendTo(page.body.addClass("no-border"));
}