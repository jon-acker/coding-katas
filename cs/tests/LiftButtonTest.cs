using lift;


class LiftButtonTest
{
    [Test]
    public void TestLightComesOnWhenDoorClosedAndButtonPressed()
    {
        // arrange
        var button = new LiftButton();
        var door = new Door();
        var lift = new Lift(button, door);

        door.state = DoorStates.CLOSED;

        // act
        lift.PressButton();

        // assert
        Assert.IsTrue(button.lightState == LightStates.ON);
    }

    public void TestLightDoesNotComeOnWhenButtonPressedButDoorOpen()
    {
        var button = new LiftButton();
        var door = new Door();
        var lift = new Lift(button, door);

        door.state = DoorStates.OPEN;

        lift.PressButton();

        Assert.IsTrue(button.lightState == LightStates.OFF);
    }

    // when doors open - light goes off
    [Test]
    public void TestLightGoesOffWhenDoorsOpen()
    {
        var button = new LiftButton();
        var door = new Door();

        var lift = new Lift(button, door);

        lift.PressButton();
        lift.OpenDoor();    

        Assert.IsTrue(button.lightState == LightStates.OFF);
    }

    [Test]
    public void TestLightStaysOffWhenPressingButtonButDoorsAreOpen()
    {
        var button = new LiftButton();
        var door = new Door();

        var lift = new Lift(button, door);

        lift.PressButton();
        lift.OpenDoor();  

        lift.PressButton();

        Assert.IsTrue(button.lightState == LightStates.OFF);
    }

}