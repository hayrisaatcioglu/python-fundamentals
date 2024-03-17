import json
import websocket
import pandas as pd

assets = ['BTCUSDT','ETHUSDT','BNBUSDT']
assets = [coin.lower() + '@kline_1m' for coin in assets]
assets = '/'.join(assets)

def on_message(ws,message):
    global source
    message = json.loads(message)
    source = message
    print(message)

socket = "wss://stream.binance.com:9443/stream?streams="+assets
def manipulation(source):
    rel_data = source['data']['k']['c']
    evt_time = pd.to_datetime(source['data']['E'], unit='ms')
    df = pd.DataFrame(rel_data, columns=[source['data']['s']], index=[evt_time])
    df.index.name = 'timestamp'
    df = df.astype(float)
    df = df.reset_index()
    print(df)
    return df


ws = websocket.WebSocketApp(socket, on_message=on_message)
ws.run_forever()
print(manipulation(source))