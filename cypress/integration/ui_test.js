context('Gym Management System', () => {
	before(() => {
		cy.visit('/login');
		cy.login();
		cy.visit('/app/website');
	});
})