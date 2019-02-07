const cucumber = require('cucumber');
const Player = require('../../../js/src/Player');

const Given = cucumber.Given;
const When = cucumber.When;
const Then = cucumber.Then;

cucumber.defineParameterType({
    regexp: /"(.*)"/,
    transformer: name => new Player(name),
    name: 'player'
});

Given('neither player have scored a point', function () {

});

Given('the game is started', function () {
    // Write code here that turns the phrase above into concrete actions
    return 'pending';
});

When('{player} scores a point', function (player) {
    // Write code here that turns the phrase above into concrete actions
});

Then('the scoreboard should display {string}', function (string) {
    // Write code here that turns the phrase above into concrete actions
    return 'pending';
});
