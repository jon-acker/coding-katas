namespace lift;


class Lift 
{
    private readonly LiftButton button;
    private readonly Door door;

    public Lift(LiftButton button, Door door)
    {
        this.button = button;
        this.door = door;
    }

    public void PressButton()
    {
        if (door.state == DoorStates.CLOSED) {
            this.button.Press();
        }
    }

    public void OpenDoor()
    {
        this.door.state = DoorStates.OPEN;
        this.button.lightState = LightStates.OFF;
    }

}