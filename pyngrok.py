from pyngrok import ngrok

public_url = ngrok.connect()
response = ngrok.api_request("{}/some-route".format(public_url),
                             method="POST", data={"foo": "bar"})