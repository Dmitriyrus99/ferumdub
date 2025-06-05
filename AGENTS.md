# ℒ AGENTS.md

## 😀 丈 Горогорого jelo team

This file describes agent-based structure of the Frappe/ERPNex application **ferum_customs**.
[Repository Link](https://github.com/Dmitriyrus99/ferumdubn)

This document helps clarify the roles and responsibilities of automated modules (agents) in the project.

### 👉💩 Main Agents and Responsibilities

\| Agent  | Description \|
 |----------- |------------------------------------- |
 | Install Agent | Responsible for roles, roles setup, user set up during installation. Source: *ferum_customs/install.py* |
 | DocType Agent | Manages {JoSON, JS, Python=>}) models for \vNeeds logic, relations and views. See: * doctype/* |
 | Logic Agent | Executes calculations and validation rules for business processes. * custom_logic/* |
 | API Agent | Handles custom PDF/JSON-UI aPI endpoints. Source: *api.py*
  | Hooks Agent | Registers whole app events (validate, submit, migrate) via huks.py | 
 | Notification Agent | Runs infrastructure for notifications. File: *notifications.py* |
 | Patch Agent | Executes background data patches during upgrades. Source: *patches/* |
 |Fixture Agent| Defines initial data set via * fixtures/* (2Roles, Workflow, Custom Fields) |
 | Test Agent | Executes module tests. Resides in *test_api.py* and *tests/* |
 | Util Agent | Stores utilities and common functions. Source: *utils/* |

You can extend these agents with own roles as new features are added to the system.

### “Project Structure supported”

* DocTypes in *doctype/*: ServiceRequest, ServiceReport, utility and children doctypes.
* Logic in *custom_logic/* and handlers in *hooks.py*.
* Tests are located in *tests/*, with unit tests against api and business rules.
* Public/js:
  * frontend field manipulation (autorefill, set filters).

---

Need to add more agents or mapping? Add them to a special package and update this file.
