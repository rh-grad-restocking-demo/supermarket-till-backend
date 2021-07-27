// camel-k: language=java
import org.apache.camel.builder.RouteBuilder;

public class TillIntegration extends RouteBuilder {
  @Override
  public void configure() throws Exception {

    restConfiguration()
        .port(8080);

    rest("/").post("/product_purchase")
      .consumes("application/json")
      .to("direct:product_purchase");

    from("direct:product_purchase")
      .to("amqp:queue:productPurchasedAddress");

  }
}
