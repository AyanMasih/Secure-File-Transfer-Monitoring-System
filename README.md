# Secure-File-Transfer-Monitoring-System
A Python-based system to monitor file transfers, detect unauthorized movement, and verify file integrity using hashing techniques.
# Secure File Transfer Monitoring System

## Project Overview
This project implements a Secure File Transfer Monitoring System designed to
track file movement, detect unauthorized access, and verify file integrity.
It simulates real-world defensive monitoring used in SOC and Blue Team roles.

The system observes file creation, modification, and deletion events and logs
them with cryptographic hash values for integrity verification.

---

## Key Features
- Real-time file system monitoring
- File transfer and modification logging
- SHA-256 hash-based integrity verification
- Detection of suspicious file activities
- Audit-ready log generation

---

## Technologies Used
- Python 3
- Watchdog (file system monitoring)
- Hashlib (integrity verification)
- Logging module

---

## Project Structure
