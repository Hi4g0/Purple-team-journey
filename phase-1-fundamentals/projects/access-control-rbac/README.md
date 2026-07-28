# Linux Access Control & Least Privilege Enforcement (RBAC Lab) date:27/07

**Date:** July 28, 2026  
**Category:** Identity & Access Management (IAM) / Blue Team  
**Framework Alignment:** ISC2 CC Domain 3 - Access Controls Concepts  

---

## 1. Objective
Implement the Principle of Least Privilege and Role-Based Access Control (RBAC) on a Linux host by creating restricted user roles and verifying authorization boundaries.

---

## 2. Security Concepts Applied
- **Authentication**: User identity creation (`adduser soc_intern`).
- **Authorization**: Privilege restriction using Linux groups and default non-sudoer policies.
- **Principle of Least Privilege**: Ensuring the analyst account possesses only the minimum necessary permissions required for log inspection.

---

## 3. Implementation Steps

### Step 1: User & Group Creation
Created a dedicated low-privilege analyst user and assigned it to a custom monitoring group:
- `sudo adduser soc_intern`
- `sudo groupadd log_analysts`
- `sudo usermod -aG log_analysts soc_intern`

### Step 2: Authorization & Boundary Testing
Switched to the restricted account (`su - soc_intern`) and attempted administrative operations (`sudo apt update`).
- **Result**: Access denied (`soc_intern is not in the sudoers file`).
- **Verification**: Administrative boundaries successfully enforced.

---

## 4. Business Value
Restricting permissions prevents internal misconfigurations, limits the blast radius of compromised credentials, and ensures strict audit compliance across corporate SOC environments.
