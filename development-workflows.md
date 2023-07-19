# Product & Development Workflows

## High Level Overview

From a development-focussed perspective we want to be able to understand user needs and requirements across all of the projects that we work on, plan how we can develop our software and platforms to meet these needs, and keep track of code to be written and bugs to be fixed. This helps with understanding what needs to be done, what the priority is, and how the work can be split based on available capacity in the team.

Development related items may arise from [operational workflows](./operational-workflows.md) or may be raised directly by the team. The below workflows give examples of how different items may be thought through, but are not prescriptive and are intended as guidelines.

## Examples

### Epic Workflow

Groups of related [FEATURE] and [STORY] issues may roll up into an [EPIC] that represents a larger initiative to be accomplished. Alternatively an identified [EPIC] may need to be broken down into [FEATURE] and [STORY] issues.

```mermaid
    flowchart LR

    initiative([New business \n initiative identified])
    epic_breakdown["Breakdown into \n [FEATURE] issues and/or \n identify related [STORY]s"]
    epic_item_workflow[["Complete [FEATURE] & [STORY] items,\n updating progress \n against[EPIC]"]]
    is_epic_complete{"EPIC acceptance \n criteria met?"}
    update_epic["Update [EPIC]"]
    close_epic["Close [EPIC]"]

    done([Done])

    initiative --> epic_issue 

    subgraph Epic Development Workflow
        epic_issue --> epic_breakdown --> epic_item_workflow --> update_epic --> is_epic_complete
        is_epic_complete --Yes--> close_epic
        is_epic_complete --No--> epic_breakdown
    end

    close_epic --> done

    epic_issue[["Create [EPIC] issue"]]

```

### Story Workflow

User needs can be recorded through the creation of a [STORY] issue. If selected for development, they can be broken down into [TASK] items that implement the needed functionality, or if part of a set of related user needs, rolled up into a [FEATURE].

```mermaid
    flowchart LR
    
    user_need([Possible user need identified])
    story_issue[["Create [STORY] issue"]]
    story_breakdown["Breakdown into \n [TASK] issues and/or \n identify related [FEATURE]s"]
    story_item_workflow[["Complete [TASK] items,\n updating progress \n against[STORY]"]]
    is_story_complete{"Story acceptance \n criteria met?"}
    update_story["Update [STORY]"]
    close_story["Close [STORY]"]

    done([Done])

    user_need --> story_issue 

    subgraph Story Development Workflow
        story_issue --> story_breakdown --> story_item_workflow --> update_story --> is_story_complete
        is_story_complete --Yes--> close_story
        is_story_complete --No--> story_breakdown
    end

    close_story --> done
```

### Feature Workflow

Larger pieces of development, defined directly by the MIRSG team, or through the aggregation of user needs can be recorded as a [FEATURE] issue. If selected for development, they can be refined and broken down into [STORY] and [TASK] issues to track their implementation.

```mermaid
    flowchart LR
    
    technical_need([New development identified])
    feature_issue[["Create [FEATURE]"]]
    feature_breakdown["Breakdown into [STORY] \n and [TASK] issues"]
    feature_item_workflow[["Complete [STORY] and \n [TASK] items, updating \n progress against [FEATURE]"]]
    is_feature_complete{"Feature meets \n definition of done?"}
    update_feature["Update [FEATURE]"]
    close_feature["Close [FEATURE]"]

    done([Done])

    technical_need --> feature_issue
    subgraph Feature Development Workflow
        feature_issue --> feature_breakdown --> feature_item_workflow --> update_feature --> is_feature_complete
        is_feature_complete --Yes--> close_feature
        is_feature_complete --No--> feature_breakdown
    end

    close_feature --> done

```

### Task Workflow

[TASK] issues may result from the breakdown of larger work items, or be directly defined. They usually represent a defined piece of work that can be completed in a short timeframe - e.g. a day.

```mermaid
    flowchart LR
    action([New actionable \n work identified])
    
    task_issue[["Create [TASK] issue"]]
    do_devops_work[Do work]
    is_task_complete{Is the \n task done?}
    update_task["Update [TASK]"]
    close_task["Close [TASK]"]
    done([Done])

    action --> task_issue

    subgraph Task Workflow
        task_issue --> do_devops_work --> update_task --> is_task_complete --Yes--> close_task
        is_task_complete --No--> do_devops_work
    end
    close_task --> done
    

```

### Bug Workflow

Through [operational workflows](./operational-workflows.md), other development tasks, or serendipitous discovery, bugs may be identified and tracked in a [BUG] issue.
Simple bugs may be addressed directly in a branch and closed with a PR, whilst more complex ones may require the creation of several [TASK] issues.

```mermaid
    flowchart LR

    bug(["New technical \n issue identified"])
    bug_issue[["Create [BUG] issue"]]
    is_simple_fix{Is the bug \n simple to fix?}
    bug_task_breakdown["Breakdown bug \n resolution into \n [TASK] issues"]
    bug_task_process[[Complete \n Task Workflow \n for each task]]
    do_bug_work[Resolve the bug]
    close_bug["Update and close [[BUG]]"]


    done([Done])
    
    bug --> bug_issue
    
    subgraph Bug Workflow
        bug_issue --> is_simple_fix --Yes--> do_bug_work --> close_bug
        is_simple_fix --No--> bug_task_breakdown --> bug_task_process --> close_bug
    end
    close_bug --> done

```
