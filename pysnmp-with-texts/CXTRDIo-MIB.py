#
# PySNMP MIB module CXTRDIo-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CXTRDIo-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:33:31 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
Alias, cxTrdIo = mibBuilder.importSymbols("CXProduct-SMI", "Alias", "cxTrdIo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, IpAddress, NotificationType, Counter32, Gauge32, ModuleIdentity, Bits, iso, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "NotificationType", "Counter32", "Gauge32", "ModuleIdentity", "Bits", "iso", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trdSapOprTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1), )
if mibBuilder.loadTexts: trdSapOprTable.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprTable.setDescription('Provides configuration information for each Token Ring service access point and its associated hardware port. Each row of the table (entry) contains information that corresponds to a particular service access point.')
trdSapOprEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1), ).setIndexNames((0, "CXTRDIo-MIB", "trdSapOprNumber"))
if mibBuilder.loadTexts: trdSapOprEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprEntry.setDescription('Provides the configuration of a particular Token Ring service access point and its associated hardware port.')
trdSapOprNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trdSapOprNumber.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprNumber.setDescription('Identifies the service access point by a numerical value. Each service access point is assigned a unique number. The number is assigned by the system.')
trdSapOprAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 2), Alias()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trdSapOprAlias.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprAlias.setDescription('Identifies the textual name (Alias) of this service access point. Each service access point must have a unique name. Range of Values: 0-16 alphanumeric characters. (Note that the first character must be a letter and spaces are not allowed). Default Value: None')
trdSapOprPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("speed-4-mbps", 1), ("speed-16-mbps", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trdSapOprPortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprPortSpeed.setDescription('Defines the input and output speed, in bits per second, for the associated hardware port. Default Value: speed-16-mbps (2) Range of Values: speed-4-mbps (1) speed-16-mbps (2)')
trdSapOprTxBufferQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 240))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trdSapOprTxBufferQueue.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprTxBufferQueue.setDescription('Defines the transmit queue length, in number of buffers, for the associated hardware port. The number of buffers is usually equal to the number of frames (i.e. one frame per buffer). After the queue has reached this length, up to eight additional frames are stored before data is discarded. Default Value: 64')
trdSapOprRxBufferQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 240))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trdSapOprRxBufferQueue.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprRxBufferQueue.setDescription('Defines the receive queue length, in number of buffers, for the associated hardware port. The number of buffers is usually equal to the number of frames (i.e. one frame per buffer). After the queue has reached this length, data is discarded. Default Value: 64')
trdSapOprDataGenerator = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("enabled-verify", 3), ("retrigger", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapOprDataGenerator.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprDataGenerator.setDescription('Determines whether the Data Generator is enabled. The Data Generator is used for testing purposes. Options: disabled (1): The Data Generator is disabled. enabled (2): The Data Generator is enabled. enabled-verify (3): The Data Generator is enabled, and checks data it receives against data it has sent. The result of the test is displayed in trdStatOprRxGenErrors. retrigger (4): The Data Generator repeats the transmission, as specified in trdSapOprGenFrames and trdSapOprGen. Default Value: disabled Configuration Changed: operative The change cannot be saved.')
trdSapOprGenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapOprGenFrames.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprGenFrames.setDescription('Determines the number of times a frame will be generated (for testing purposes). Frames are generated every 50 msec. If the value is set to zero, then frames will be generated continuously (every 50 msec). If the Data Generator is disabled (using trdSapOprDataGenerator), then the value is ignored. Range of Values: 0 - 255 Default Value: 1 Configuration Changed: operative The change cannot be saved.')
trdSapOprGenFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapOprGenFrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapOprGenFrameSize.setDescription('Determines the size of the frames (in bytes) to be generated for testing purposes. If the Data Generator is disabled, then this value is ignored. Range of Values: 18-2100 bytes Default Value: 512 bytes Configuration Changed: operative The change cannot be saved.')
trdOprControlStats = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("clearSapStats", 1)))).setMaxAccess("writeonly")
if mibBuilder.loadTexts: trdOprControlStats.setStatus('mandatory')
if mibBuilder.loadTexts: trdOprControlStats.setDescription('Determines whether statistics for the hardware port will be cleared. When the clearSapStats option is selected, all counters for this port are cleared, including counters kept in the Interfaces Group MIB, (RFC 1213) and in the dot5 Table (RFC 1231). Options: clearSapStats (1): clears all statistics for the hardware port. Configuration Changed: operative')
trdStatOprRxGenErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trdStatOprRxGenErrors.setStatus('mandatory')
if mibBuilder.loadTexts: trdStatOprRxGenErrors.setDescription("Identifies the total number of frames received that contain errors for a port that is set to enable-verify in 'trdSapOprDataGenerator'. Range of Values: 0 to 4,294,967,295 Default Value: None")
trdSapAdmTable = MibTable((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2), )
if mibBuilder.loadTexts: trdSapAdmTable.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmTable.setDescription('Provides configuration information for each Token Ring service access point and its associated hardware port. Each row (entry) of the table corresponds to a particular service access point.')
trdSapAdmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1), ).setIndexNames((0, "CXTRDIo-MIB", "trdSapAdmNumber"))
if mibBuilder.loadTexts: trdSapAdmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmEntry.setDescription('Provides configuration information for a particular Token Ring service access point and its associated hardware port.')
trdSapAdmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trdSapAdmNumber.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmNumber.setDescription('Identifies the service access point by a number. The system assigns each service access point a unique number.')
trdSapAdmAlias = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 2), Alias()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapAdmAlias.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmAlias.setDescription('Determines the textual name (alias) of this service access point. Each service access point is assigned a unique name. Range of Values: 0-16 alphanumeric characters.The first character must be a letter, and spaces are not allowed.')
trdSapAdmPortSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("speed-4-mbps", 1), ("speed-16-mbps", 2))).clone('speed-16-mbps')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapAdmPortSpeed.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmPortSpeed.setDescription('Defines the input and output speed, in bits per second, for the associated hardware port. Options: speed-4-mbps (1): 4 mbps ring speed speed-16-mbps (2): 16 mbps ring speed Default Value: speed-16-mbps (2)')
trdSapAdmTxBufferQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 240)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapAdmTxBufferQueue.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmTxBufferQueue.setDescription('Defines the transmit queue length, in number of buffers, for the associated hardware port. The number of buffers is usually equal to the number of frames (i.e. one frame per buffer). After the queue has reached this length, up to eight additional frames are stored before data is discarded. Range of Values: 32-240 Default Value: 64')
trdSapAdmRxBufferQueue = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32, 240)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapAdmRxBufferQueue.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmRxBufferQueue.setDescription('Defines the receive queue length, in number of buffers, for the associated hardware port. The number of buffers is usually equal to the number of frames (i.e. one frame per buffer). After the queue has reached this length, data is discarded. Range of Values: 32-240 Default Value: 64')
trdSapAdmDataGenerator = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("enabled-verify", 3))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapAdmDataGenerator.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmDataGenerator.setDescription('Determines whether the Data Generator is enabled. The Data Generator is used for testing purposes. Options: disabled (1) enabled (2) enabled-verify (3): The Data Generator is enabled, and checks data it receives against data it has sent. The result of the test is displayed in trdStatOprRxGenErrors. Default Value: disabled (1) Configuration Changed: administrative Further Action: to activate changed value, click on Action in EMS menu bar, then click on Reset with Save.')
trdSapAdmGenFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapAdmGenFrames.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmGenFrames.setDescription('Determines the number of times a frame will be generated for testing purposes. Frames are generated every 50 msec. If the value is set to zero, then frames will be generated continuously (every 50 msec). If the Data Generator is disabled (using trdSapAdmDataGenerator), then the value is ignored. Range of Values: 0 - 255 Default Value: 1 Configuration Changed: administrative Further action: to activate changed value, click on Action in EMS menu bar, then click on Reset with Save.')
trdSapAdmGenFrameSize = MibTableColumn((1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 51, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(18, 2100)).clone(512)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trdSapAdmGenFrameSize.setStatus('mandatory')
if mibBuilder.loadTexts: trdSapAdmGenFrameSize.setDescription('Determines the size of the frames (in bytes) to be generated for testing purposes. If the Data Generator is disabled, then this value is ignored. Range of Values: 18 - 2100 bytes Default Value: 512 bytes Configuration Changed: administrative Further action: to activate changed value, click on Action in EMS menu bar, then click on Reset with Save.')
mibBuilder.exportSymbols("CXTRDIo-MIB", trdSapOprEntry=trdSapOprEntry, trdStatOprRxGenErrors=trdStatOprRxGenErrors, trdSapOprAlias=trdSapOprAlias, trdSapAdmGenFrames=trdSapAdmGenFrames, trdSapAdmEntry=trdSapAdmEntry, trdSapAdmDataGenerator=trdSapAdmDataGenerator, trdSapOprGenFrames=trdSapOprGenFrames, trdSapAdmAlias=trdSapAdmAlias, trdSapOprDataGenerator=trdSapOprDataGenerator, trdSapAdmRxBufferQueue=trdSapAdmRxBufferQueue, trdSapAdmGenFrameSize=trdSapAdmGenFrameSize, trdSapOprNumber=trdSapOprNumber, trdSapAdmNumber=trdSapAdmNumber, trdSapOprRxBufferQueue=trdSapOprRxBufferQueue, trdSapOprTable=trdSapOprTable, trdSapAdmTable=trdSapAdmTable, trdSapAdmTxBufferQueue=trdSapAdmTxBufferQueue, trdSapOprTxBufferQueue=trdSapOprTxBufferQueue, trdSapAdmPortSpeed=trdSapAdmPortSpeed, trdSapOprPortSpeed=trdSapOprPortSpeed, trdOprControlStats=trdOprControlStats, trdSapOprGenFrameSize=trdSapOprGenFrameSize)