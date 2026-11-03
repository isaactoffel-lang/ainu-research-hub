# AINU Research Hub

A shared workspace for organizing investment research and analyst work.

## The problem

Research becomes difficult to review when assignments, company notes, and supporting files live in separate places. The hub brings that work into a common workflow.

## Implementation

The private source includes a browser interface, valuation tools, database scripts, and checks for application behavior and access boundaries.

| Area | Purpose |
| --- | --- |
| Research library | Organize company material and supporting documents |
| Analyst workflow | Keep assignments and research progress visible |
| Valuation tools | Connect assumptions with a research argument |
| Database layer | Store shared records and define access behavior |
| Review tools | Support consistent handoffs between analysts |

## Design decisions

Separate research content from account configuration. Make assumptions visible to the reviewer. Treat access controls as behavior that needs testing rather than a promise made by the interface.

## Public scope

This repository contains a qualitative description only. Source code, analyst records, sample financial data, account configuration, contact information, attachments, and development history are retained privately.

This writeup does not establish the current security of the deployed database or confirm a working live integration. AI assisted with implementation, testing, and documentation.
