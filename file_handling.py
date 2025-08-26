# file_handling.py

def main():
    print("📂 File Handling Challenge\n")

    # Ask user for input and output files
    input_file = input("Enter the filename to read: ")
    output_file = input("Enter the filename to save modified content: ")

    try:
        # Read the input file
        with open(input_file, 'r') as f:
            content = f.read()
        print("\n✅ File read successfully!\n")

        # Modify content: uppercase and replace 'Python' with 'PYTHON'
        modified_content = content.upper().replace("PYTHON", "PYTHON 🐍")

        # Write to the output file
        with open(output_file, 'w') as f:
            f.write(modified_content)

        print(f"\n🎉 Modified content saved to '{output_file}' successfully!")

    except FileNotFoundError:
        print(f"\n❌ Error: The file '{input_file}' does not exist.")
    except IOError:
        print("\n❌ Error: Cannot read/write to file.")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
