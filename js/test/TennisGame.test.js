const TennisGame = require('../src/TennisGame');

let game;

beforeEach(() => {
    game = new TennisGame();
});


test('it returns Love All when no one has scored yet', function () {
    expect(game.displayScore()).toBe('Love All');
});

