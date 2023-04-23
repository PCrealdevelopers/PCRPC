# PCRPC

Simple lib for rpc discord, Python. 

# Example
 
```python
import PCRPC

c = PCRPC.RPC.Set_ID(app_id=0000)

button = PCRPC.button(
    button_one_label="Example 1",
    button_one_url="https://t.me/pcdevchannel",
    button_two_label="Example 2",
    button_two_url="https://t.me/pcdevchannel"
  )

c.set_activity(
    state="Example\n\nc",
    details="Example PCrpc",
    large_image="image1",
    small_image="image2",
    small_text="Hi, this is example, i love PC!",
    timestamp=c.timestamp(),
    buttons=button
)

c.run()
```
