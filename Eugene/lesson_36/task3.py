import asyncio


async def connect(reads, writes):

    address = writes.get_extra_info('peername')
    print(f"Connect from: {address}")

    try:
        while True:
            data = await reads.read(1024)
            if not data:
                break
            writes.write(data)
            await writes.drain()
            print(f"Echo: {data.decode('utf-8', errors='ignore').strip()}")
    except Exception as e:
        print(f"Error from {address}: {e}")
    finally:
        writes.close()
        await writes.wait_closed()
        print(f"{address} disconnected.")


async def main():

    HOST = '127.0.0.1'
    PORT = 8888

    server = await asyncio.start_server(connect, HOST, PORT)
    print(f"Server run on {HOST}:{PORT}. Wait for connection.")

    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
