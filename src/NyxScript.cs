public class Nyx implements Player {
  
  // Unity movement and sprite generation
  
  private float sight;
  
  private float velocity;
  
  @Overrides void sight();
  
  @Overrides void goalPoint();
  
  public void grab();
  
  public void drop();
  
  public void throw();

  
}
