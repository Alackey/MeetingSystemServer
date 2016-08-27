# Meeting System Server

The API for the MeetingSystem GUI program

## API
### /timeblocks
#### GET
Get timeblocks for employees with specific date range

Required (query):
 - employees : Array as String
 - startDate : String
 - endDate : String
 - date : String

Returns (JSON):
 - error : Boolean
 - timeblocks : JSON

#### POST
Add timeblock

Required (body):
- employeeID : String
- type<sup>1</sup> : String
- meetingID : String 
- startTime : String
- endTime : String
- date : String
- id : int

<sub>1\. MEETING or BUSY</sub>
