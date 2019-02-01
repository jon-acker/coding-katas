const TennisGame = require('../src/TennisGame');

let game;

beforeAll(() => {
    game = new TennisGame();
});


test('it returns Love All when no one has scored yet', function () {
    expect(game.displayScore()).toBe('Love All');
});

