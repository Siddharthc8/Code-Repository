import pandas as pd

# Define the test plan data
test_plan = [
    ["A1", "Single Byte Write", "Master writes one byte to a slave.", "Slave acknowledges and stores the byte."],
    ["A2", "Single Byte Read", "Master reads one byte from slave.", "Slave sends correct byte, master sends NACK after read."],
    ["A3", "Multi-Byte Write", "Master writes multiple bytes in one session.", "All bytes received with ACKs; slave stores correctly."],
    ["A4", "Multi-Byte Read", "Master reads multiple bytes from slave.", "All bytes received; final byte followed by NACK."],
    ["A5", "Repeated START", "Master sends repeated START between write and read.", "No STOP; repeated START occurs; data transferred correctly."],
    ["A6", "Combined Format", "Master writes address, then reads data (write+read).", "Correct read after write; address retained."],
    ["B1", "7-bit Addressing", "Communicate using 7-bit address.", "Only addressed slave responds with ACK."],
    ["B2", "10-bit Addressing", "Use 10-bit address format.", "Correct response from 10-bit addressed slave."],
    ["B3", "Invalid Address", "Use address with no attached slave.", "No ACK; master handles NACK appropriately."],
    ["B4", "Address Conflict", "Two slaves have same address.", "Both try to respond; check for conflict detection."],
    ["C1", "Slave NACK", "Slave sends NACK after address/data.", "Master detects NACK and aborts/recovers."],
    ["C2", "Missing ACK", "Simulate corrupted or missing ACK.", "Master times out or retries."],
    ["C3", "Bus Stuck Low", "Hold SDA or SCL low permanently.", "Master detects fault; issues STOP or resets bus."],
    ["C4", "Early STOP", "Send STOP before ACK.", "Slave ignores data; bus releases properly."],
    ["C5", "Glitch on SDA/SCL", "Generate sub-spec pulses (noise).", "Controller ignores glitch; no false START/STOP detected."],
    ["D1", "Clock Stretching", "Slave holds SCL low.", "Master waits until SCL is released before continuing."],
    ["D2", "Setup/Hold Violation", "Change data too early or too late around SCL edge.", "Assertion fails or protocol error is raised."],
    ["D3", "Speed Mode Tests", "Run at 100kHz, 400kHz, 1MHz, etc.", "Controller adjusts timing per mode and functions correctly."],
    ["E1", "Arbitration Win", "Two masters initiate transfers simultaneously.", "One wins; loser releases SDA when mismatch detected."],
    ["E2", "Arbitration Loss", "Intentionally lose arbitration.", "Master detects mismatch and stops; arbitration lost signal set."],
    ["E3", "Bus Handover", "One master finishes, another starts communication.", "No collisions; second master succeeds after first finishes."],
    ["F1", "Power-On Reset", "Reset controller at power-up.", "Controller initializes to IDLE; registers defaulted."],
    ["F2", "Mid-Transaction Reset", "Assert reset during ongoing transfer.", "Controller aborts; recovers cleanly; bus released."],
    ["F3", "Glitch Reset Line", "Briefly pulse reset low.", "Reset not triggered unless held low > threshold."],
    ["G1", "Long Burst Transfers", "Transfer large data blocks (e.g., 256 bytes).", "All bytes transmitted accurately with correct ACK/NACKs."],
    ["G2", "Randomized Stress Test", "Multiple masters/slaves with random addresses, delays.", "No deadlocks; data integrity maintained; bus fully utilized."],
    ["G3", "Timeout Handling", "Slave or master doesn’t respond in time.", "Timeout triggers, and controller exits gracefully."],
]

# Create DataFrame
df = pd.DataFrame(test_plan, columns=["ID", "Test Name", "Description", "Expected Result"])

# Save to Excel
file_path = "/mnt/data/I2C_Test_Plan.xlsx"
df.to_excel(file_path, index=False)

file_path
