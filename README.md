# Till Backend

The Till Backend is implemented as a Camel K integration on OpenShift.

---

## Deployment

1. Use the OpenShift CLI to login to the cluster and make sure you have selected the correct project you want to deploy the integration into.


2. Deploy application.properties as config map to OpenShift.
   ```shell
    oc create configmap till-backend-amqp --from-file=application.properties
    ```

3. Deploy the Camel K integration.
    ```shell
    kamel run TillBackend.java --config configmap:till-backend-amqp
    ```