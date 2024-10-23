Table 1. DC Motor Power Supply Connection to Relay Module

Relay		Jumper	Chassis		Cable	Power
Module		Wire	DC Jack		DC Plug	Supply
CH-1	NC-1	JW-A2				
	COM-1					
	NO-1	JW-A1	JG-A		PG-A	GND-A
CH-2	NC-2	JW-A1				
	COM-2					
	NO-2	JW-A2				
CH-3	NC-3	JW-A2				
	COM-3	JW-A2				
	NO-3		JP-A		PP-A	VCC-A


Table 2. DC Motor Connection to Relay Module

Relay		Jumper	Chassis		Cable	DC
Module		Wire	DC Jack		DC Plug	Motor
CH-1	NC-1	JW-A2				
	COM-1		JP-3		PP-3	M-F
	NO-1	JW-A1				
CH-2	NC-2	JW-A1				
	COM-2		JG-3		PG-3	M-R
	NO-2	JW-A2				
CH-3	NC-3	JW-A2				
	COM-3	JW-A2				
	NO-3					


Table 3. Solenoid Lock Power Supply Connection to Relay Module

Relay		Jumper	Chassis		Cable	Power
Module		Wire	DC Jack		DC Plug	Supply
CH-4	NC-4	JW-B1	JP-B		PP-B	VCC-B
	COM-4	JW-B1				
	NO-4					
			JG-B		PG-B	GND-B


Table 4. Solenoid Lock Connection to Relay Module

Relay		Jumper	Chassis		Cable	Solenoid
Module		Wire	DC Jack		DC Plug	Lock
CH-4	NC-4	JW-B1	JP-B			
	COM-4	JW-B1				
	NO-4		JP-4		PP-4	SL-VCC
		JW-4	JG-B			
		JW-4	JG-4		PG-4	SL-GND


Table 5. LED Bar (Internal and External) Power Supply Connection to Relay Module

Relay		Jumper	Chassis		Cable	Power
Module		Wire	DC Jack		DC Plug	Supply
CH-5	NC-5	JW-C1	JP-C		PP-C	VCC-C
	COM-5	JW-C1				
	NO-5					
			JG-C		PG-C	GND-C
CH-6	NC-6	JW-C1				
	COM-6	JW-C1				
	NO-6					


Table 6. LED Bar (Internal and External) Connection to Relay Module

Relay		Jumper	Chassis		Cable	LED
Module		Wire	DC Jack		DC Plug	Bar (Int)
CH-5	NC-5	JW-C1	JP-C			
	COM-5	JW-C1				
	NO-5		JP-5		PP-5	LBI-VCC
		JW-5	JG-C			
		JW-5	JG-5		PG-5	LBI-GND
					Cable	LED
					DC Plug	Bar (Ext)
CH-6	NC-6	JW-C1				
	COM-6	JW-C1				
	NO-6		JP-6		PP-6	LBE-VCC
		JW-5	JG-6		PG-6	LBE-GND


Table 7. Legend for Table 1 to Table  6

Legend	Description	
JP	DC Jack Positive Terminal (usually middle pin)	
JG	DC Jack Ground Terminal (usually outer pin)	
PP	DC Plug Positive Terminal	
PG	DC Plug Ground Terminal	


Table 8. Summary List of Jack and Plug Connections

Chassis	Cable	Description		
DC Jack	DC Plug			
JP-A	PP-A	For first 12V DC Supply (VCC).		
JG-A	PG-A	For first 12V DC Supply (GND).		
JP-B	PP-B	For second 12V DC Supply (VCC).		
JG-B	PG-B	For second 12V DC Supply (GND).		
JP-C	PP-C	For third 12V DC Supply (VCC).		
JG-C	PG-C	For third 12V DC Supply (GND).		
JP-1	PP-1	For DC Motor pin (F).		
JG-1	PG-1	For DC Motor pin (R).		
JP-4	PP-4	For Solenoid Lock pin (VCC).		
JG-4	PG-4	For Solenoid Lock pin (GND).		
JP-5	PP-5	For LED Bar (Internal) pin (VCC).		
JG-5	PG-5	For LED Bar (Internal) pin (GND).		
JP-6	PP-6	For LED Bar (External) pin (VCC).		
JG-6	PG-6	For LED Bar (External) pin (GND).		
