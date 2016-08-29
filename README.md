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
- recurringDay<sup>2</sup> : int
- recurringDay : boolean

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
- day<sup>2</sup> : int

<sub>1\. MEETING or BUSY</sub>

<sub>2\. 1 - 7 are Sun - Sat respectively</sub>
