# DDoS Attack Detection Using Random Forest Classifier

## Project Overview

This project aims to detect Distributed Denial of Service (DDoS) attacks by analyzing network traffic data using a machine learning approach. Specifically, it employs a Random Forest Classifier to differentiate between normal and malicious traffic patterns. The data for training and testing the classifier is generated and processed through a series of steps involving packet capture, conversion, and feature extraction.

## System Requirements

- **Operating Systems:** Windows 11 (Core OS), Kali Linux (Virtualized Attacker OS), Ubuntu (Virtualized Victim OS)
- **Tools:** Wireshark, CICFlowMeter
- **Programming Language:** Python
- **Dependencies:** Anaconda Spyder (IDE), NumPy, Pandas, scikit-learn, Joblib, Pillow (PIL), CustomTkinter, sqlite3.

## Project Setup

### Step 1: Packet Capture

- **Normal Traffic:** Send normal ICMP packets from Kali Linux to Ubuntu Linux and capture them using Wireshark.
- **Malicious Traffic:** Simulate DDoS attacks by sending malicious packets using the Hping command from Kali Linux to Ubuntu Linux.

### Step 2: Verify Incoming Packets

Use system monitoring tools to verify the incoming packets for both normal and attack scenarios.

### Step 3: Convert Packet Data

Convert the captured packets from `.pcap` format to `.csv` using CICFlowMeter for both the normal and malicious traffic.

### Step 4: Data Analysis

Upload the generated CSV files into the system to analyze the traffic. The Random Forest Classifier will be used to:
- Detect the absence of DDoS attacks in normal traffic.
- Detect the presence of DDoS attacks in malicious traffic.

## **Demonstration**

![Demo](Demo.gif)


