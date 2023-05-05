namespace lift;

public enum LightStates {
    OFF,
    ON
}

public class LiftButton
{
    public LightStates lightState = LightStates.OFF;


    public void Press()
    {
        this.lightState = LightStates.ON;
    }
}