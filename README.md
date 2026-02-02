# DANDI Open Data Tutorial

Development repo for concise tutorial of DANDI for the Open Data Registry.


### Goal

To make as short of a tutorial as possible for someone to get a minimal understanding of DANDI.

### Philosophy

Minimize verbosity and maximize clarity.

Alternate Markdown cells which prompt questions with short code snippets.

Consider how rendered views (via GitHub or DANDIHub) appear on mobile devices or when 'zoomed in' during screen sharing.

Also consider how items appear in both light mode and dark mode.

Think about this as a "quick start" guide for DANDI.

### Design

Limit sentence length as much as possible (except for last two sections - even there, trying to be not too verbose).

Render each sentence on a separate line to decrease instances of soft-wrapping (again, except for last two sections which are meant to be solid text).

Limit code lines as much as possible (note we could use some even better helper methods in PyNWB and DANDI APIs for certain tasks like streaming).

The final version of the notebook will be partially rendered to show what it 'should' look like if cells run successfully. As such, keep all outputs trimmed to be as small as possible, such as only printing the first few items of a list. The one exception to this is the dynamic HTML exploration of NWB files, which is nice to have for anyone running the notebook but looks horrible when expanded in full by GitHub.
