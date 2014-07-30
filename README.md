files setup
=====

We have to manage source and data. Data is shared (for example bittorent sync). Source is managed on github of course.

1. clone this source
2. get (shared) data (using bittorent sync for example)
3. set [data_store](/data_store) in project to this  data. probably best to just make it a subfolder as is so in the source. if you are using bittorent sync, keep the syncignore in the source.
4. set data_dir in [resources.py](resources.py) to the data
