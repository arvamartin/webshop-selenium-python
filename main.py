import subprocess

if __name__ == "__main__":
    print("Starting all tests...")

    result = subprocess.run(
            ['behave'])


