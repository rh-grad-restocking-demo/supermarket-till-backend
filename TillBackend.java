// camel-k: language=java

import org.apache.camel.builder.RouteBuilder;

public class TillBackend extends RouteBuilder {
  @Override
  public void configure() throws Exception {

      rest("/")
        .post("/items_purchase").consumes("application/json").to("direct:items_purchase");

      from("direct:items_purchase")
        .to("amqp:queue:itemsPurchasedAddress");

  }
}
