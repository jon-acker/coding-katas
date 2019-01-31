const chai = require('chai');
const expect = chai.expect;
const should = chai.should();

const TennisGame = require('../src/TennisGame');

describe('Tennis Game', function() {

    let game;

    beforeEach(function() {
        game = new TennisGame();
    });

    it('returns Love All when no one has scored yet', function () {
        expect(game.displayScore()).to.equal('Love All');
    });

});