# Blameless postmortem (lite)

Short form of the full template. The full pack adds the RFC, the CAB checklist, the rollback plan, worked examples, and docx copies.

## Summary

One paragraph: what broke, the UTC start and end, and whether data was lost.

## Impact

Severity, user-visible symptom, and whether customer data was exposed.

## Timeline

| Time (UTC) | Event |
| --- | --- |
| YYYY-MM-DD HH:MM | One observed fact. |

## Detection

Name the alarm and the minutes between impact and the page.

## Root cause

The mechanism, not a person's mistake. Separate the trigger from the defect.

## Action items

| ID | Action | Owner | Due |
| --- | --- | --- | --- |
| AI-1 | A change to code, config, or an alarm. | Name | YYYY-MM-DD |

## Blameless statement

This review looks at the system and the decisions available at the time. It does not assign personal blame.
