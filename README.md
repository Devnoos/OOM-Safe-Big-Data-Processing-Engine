# OOM-Safe Big Data Processing Engine

A pure Python project I built to learn how to process massive datasets (gigabytes in size) without crashing my computer's RAM (Out-Of-Memory errors). Instead of loading an entire file into memory at once, this engine uses Python Generators to read and process data in small, efficient chunks.

##  What I Learned / Why I Built This

* **Memory Management:** Learned how to prevent RAM from overflowing when dealing with Big Data.
* **Python Generators:** Got hands-on experience using the `yield` keyword to create lazy iterators.
* **Mock Data Creation:** Instead of downloading huge datasets from the internet, I wrote a script to generate my own custom test data.
* **Modular Code:** Separated the project into different files (Generator, Reader, Analyzer) so the logic stays clean and easy to debug.

## How It Works (The 3-Part System)

The project is broken down into three main scripts:

1. **`data_generator.py`:** Generates a massive dummy dataset (e.g., millions of rows) so I can test the engine locally. 
2. **`chunk_reader.py`:** The heart of the project. It opens the massive file and uses a Python generator (`yield`) to read the data chunk-by-chunk, keeping the memory footprint close to zero.
3. **`analyzer.py`:** Connects to the chunk reader. It takes those small chunks one by one and performs data processing/calculations on the fly.

## 💻 How to Run

1. Clone this repository to your local machine.
2. First, run the data generator to create your test file (Warning: It will create a large file locally!).
   ```bash
   python data_generator.py 
   ```
3. Then, run the analyzer to see the chunk-processing in action:
    ```bash
   python analyzer.py
