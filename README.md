# DANDI Open Data Tutorial

This was a development repo for a concise tutorial of DANDI for the Open Data Registry.

It resulted in the eventual merge of https://github.com/awslabs/open-data-registry/pull/3072 to the Open Data Registry page for the DANDI Archive, which refers to the final version of the notebook found at:

https://github.com/dandi/example-notebooks/blob/master/tutorials/open_data_quick_start_2026/Get-to-know-a-Dandiset.ipynb


### Goal

To make as short of a tutorial as possible for someone to get a minimal understanding of DANDI.

### Philosophy

Think about this as a "quick start" guide for DANDI.

Minimize verbosity and maximize clarity.

Alternate Markdown cells which prompt questions with short code snippets.

Consider how rendered views (via GitHub or DANDIHub) appear on mobile devices or when 'zoomed in' during screen sharing.

Also consider how items appear in both light mode and dark mode.

Keep distractions (such as side topics or long explanations) to a minimum. Provide links to external resources for further reading instead.

### Design

Limit sentence length as much as possible (except for last two sections - even there, trying to be not too verbose).

Render each sentence on a separate line to decrease instances of soft-wrapping (again, except for last two sections which are meant to be solid text).

Limit code lines as much as possible (note we could use some even better helper methods in PyNWB and DANDI APIs for certain tasks like streaming).

The final version of the notebook will be partially rendered to show what it 'should' look like if cells run successfully. As such, keep all outputs trimmed to be as small as possible, such as only printing the first few items of a list. The one exception to this is the dynamic HTML exploration of NWB files, which is nice to have for anyone running the notebook but looks horrible when expanded in full by GitHub.
