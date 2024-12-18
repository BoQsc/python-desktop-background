import subprocess

def shutdown():
    shutdown_methods = ['shutdown', '/s', '/f', '/t', '0']  # /s: shutdown, /f: force apps closed, /t: timeout (0 sec)

    try:
        result = subprocess.run(shutdown_methods, capture_output=True)

        if result.returncode == 0:
            print("Shutdown initiated successfully.")
        else:
            print(f"Shutdown failed with error: {result.stderr.decode().strip()}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    shutdown()
