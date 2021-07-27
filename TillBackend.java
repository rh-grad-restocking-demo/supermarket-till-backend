// camel-k: language=java

import org.apache.camel.builder.RouteBuilder;

public class TillBackend extends RouteBuilder {
  @Override
  public void configure() throws Exception {


      rest("/")
        .post("/product_purchase").consumes("application/json").to("direct:product_purchase");

        


      rest("/")
          .verb("OPTIONS", "/").route()
          .setHeader("Access-Control-Allow-Origin", constant("*"))
          .setHeader("Access-Control-Allow-Methods", constant("GET, HEAD, POST,PUT, DELETE, TRACE, OPTIONS, CONNECT, PATCH"))
          .setHeader("Access-Control-Allow-Headers", constant("Origin, Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers, Authorization"))
          .setHeader("Allow", constant("GET, OPTIONS, POST, PATCH"));

      from("direct:product_purchase")
        .to("amqp:queue:productPurchasedAddress");




  }
}
