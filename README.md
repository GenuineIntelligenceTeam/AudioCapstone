# AudioCapstone
Capstone project for Week 1 of CogWorks 2018.

To install, simply run ```python setup.py install```.

## Train on song database

```python
from songmatch.trainer import train_all_songs

train_all_songs()
```

## Test recording against database

For example, to record for 10 seconds:

```python
from songmatch.matchsong import match_recording

match_recording(10)
```

Change the parameter to match_recording to change duration.

## Edit song database

Want to add more songs to your database?

```python
from songmatch.songbase import songbase

songbase.append("Pink Floyd - Time.mp3")
```

Append the song mp3 file names to the database and then rerun the ```train_all_songs()``` function.

**IMPORTANT NOTE:** when contributing, avoid pushing database.pickle to any branch as the file size is too large for github to handle.
