#
# PySNMP MIB module H320ENTITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H320ENTITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
mmH320Root, MmTerminalVideoCapability, MmTerminalAudioCapability, MmTerminalLineRateCapability, MmTerminalDataCapability = mibBuilder.importSymbols("MULTI-MEDIA-MIB-TC", "mmH320Root", "MmTerminalVideoCapability", "MmTerminalAudioCapability", "MmTerminalLineRateCapability", "MmTerminalDataCapability")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, Gauge32, ModuleIdentity, iso, Bits, Integer32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, Unsigned32, Counter32, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "ModuleIdentity", "iso", "Bits", "Integer32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter32", "IpAddress", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h320Entity = ModuleIdentity((0, 0, 8, 341, 1, 2, 1))
h320Entity.setRevisions(('1998-12-18 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h320Entity.setRevisionsDescriptions((' The H320 entity mib',))
if mibBuilder.loadTexts: h320Entity.setLastUpdated('9812181400Z')
if mibBuilder.loadTexts: h320Entity.setOrganization('ITU-T')
if mibBuilder.loadTexts: h320Entity.setContactInfo(' ITU-T SG-16 ')
if mibBuilder.loadTexts: h320Entity.setDescription('This MIB module supports the common functions of the ITU-T H.320 terminal, MCU and H.320/H.323 gateway')
h320Capability = MibIdentifier((0, 0, 8, 341, 1, 2, 1, 1))
h320CallStatus = MibIdentifier((0, 0, 8, 341, 1, 2, 1, 2))
h320H221Stats = MibIdentifier((0, 0, 8, 341, 1, 2, 1, 3))
h320CapsTable = MibTable((0, 0, 8, 341, 1, 2, 1, 1, 1), )
if mibBuilder.loadTexts: h320CapsTable.setStatus('current')
if mibBuilder.loadTexts: h320CapsTable.setDescription("A list of capability entries. Objects are grouped as a table so that one can use this table in the H.320 terminal, the H.320 MCU, and the H.320/H.323 gateway. The total number of capability entries is equal to the number of H.320 entities in a system. For instance, there will be one row of capability in the table of the H.320 terminal. The number of rows will be equal to the number of H320 entities in the MCU and the H320/H323 gateway. These entries describe the general capability of a system. Within a particular call, the behavior of the system is further constrained by the characteristics of the call itself. For example, h320CapsEntityMaxVideoRate describes the maximum video rate a system can handle (perhaps due to processing constraints). A particular call's transfer rate may limit video to a lower rate ")
h320CapsEntry = MibTableRow((0, 0, 8, 341, 1, 2, 1, 1, 1, 1), ).setIndexNames((0, "H320ENTITY-MIB", "terminalIndex"))
if mibBuilder.loadTexts: h320CapsEntry.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntry.setDescription('A capability row.')
terminalIndex = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: terminalIndex.setStatus('current')
if mibBuilder.loadTexts: terminalIndex.setDescription('A unique value for each video conference entity. The value ranges between 1 and the number of H.320 entities in a system. For instance, the table in the H.320 terminal has one row and the H.323/H.320 gateway or the H.320 MCU may have multiple rows of the H.320 capability. ')
h320CapsEntityLineRate = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 2), MmTerminalLineRateCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CapsEntityLineRate.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntityLineRate.setDescription('This object represents the line rate capabilities of the H.320 entity. Supported line rates are indicated by an octet string marked with 1s.')
h320CapsEntityVideoFormats = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 3), MmTerminalVideoCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CapsEntityVideoFormats.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntityVideoFormats.setDescription('This object represents the video capabilities of the H.320 entity. This includes the various video algorithms that it supports.')
h320CapsEntityMaxVideoRate = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CapsEntityMaxVideoRate.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntityMaxVideoRate.setDescription('The maximum bit rate in kbit/s that the video channel can do.')
h320CapsEntityAudioTypes = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 5), MmTerminalAudioCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CapsEntityAudioTypes.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntityAudioTypes.setDescription('This object represents the audio capabilities of the H320 entity. This includes the various audio algorithms that it supports.')
h320CapsEntityDataCaps = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 6), MmTerminalDataCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CapsEntityDataCaps.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntityDataCaps.setDescription('This object represents the data capability of the entity. ')
h320CapsEntityEncryp = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CapsEntityEncryp.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntityEncryp.setDescription('This object represents the encryption capability of the entity. Capability Bit # other 0 H.233/H.234 1 Bits are numbered starting with the most significant bit of the first byte being bit 0, the least significant bit of the first byte being bit 7, the most significant bit of the second byte being bit 8, and so on. A one bit encodes that the capability is supported, a zero bit encodes that the capability is not supported.')
h320CapsEntryRDC = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CapsEntryRDC.setStatus('current')
if mibBuilder.loadTexts: h320CapsEntryRDC.setDescription('This object represents the Remote Device Control capability of the entity. Capability Bit # Other 0 H.281 1 -- Far-end Camera Control Bits are numbered starting with the most significant bit of the first byte being bit 0, the least significant bit of the first byte being bit 7, the most significant bit of the second byte being bit 8, and so on. A one bit encodes that the capability is supported, a zero bit encodes that the capability is not supported.')
h320CallStatusTable = MibTable((0, 0, 8, 341, 1, 2, 1, 2, 1), )
if mibBuilder.loadTexts: h320CallStatusTable.setStatus('current')
if mibBuilder.loadTexts: h320CallStatusTable.setDescription('A list of call status entries. Objects are grouped as a table so that one can use this table in the H.320 terminal, the H.320 MCU, and the H.320/H.323 gateway. The total number of call status entries is equal to the number of H.320 entities in a system. For instance, there will be one row of call status in the table of the H.320 terminal. The number of rows will be equal to the number of H320 entities in the MCU and the H320/H323 gateway')
h320CallStatusEntry = MibTableRow((0, 0, 8, 341, 1, 2, 1, 2, 1, 1), )
h320CapsEntry.registerAugmentions(("H320ENTITY-MIB", "h320CallStatusEntry"))
h320CallStatusEntry.setIndexNames(*h320CapsEntry.getIndexNames())
if mibBuilder.loadTexts: h320CallStatusEntry.setStatus('current')
if mibBuilder.loadTexts: h320CallStatusEntry.setDescription('A call status row.')
h320CallCurrentCallStatus = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("idle", 1), ("connecting", 2), ("connected", 3), ("disconnecting", 4), ("disconnected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallCurrentCallStatus.setStatus('current')
if mibBuilder.loadTexts: h320CallCurrentCallStatus.setDescription('The current call status. An idle(1) means there were no calls placed since the system is up. Once calls were established and disconnected, the system remains in the disconnected(5) state. A connected(2) means the call is established and reached its intended mode of operation ')
h320CallSiteName = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallSiteName.setStatus('current')
if mibBuilder.loadTexts: h320CallSiteName.setDescription('The address to which this call is made. ')
h320CallLineRate = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 3), MmTerminalLineRateCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallLineRate.setStatus('current')
if mibBuilder.loadTexts: h320CallLineRate.setDescription('This object represents the line rate being used in the current call in progress.')
h320CallVideoInFormat = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 4), MmTerminalVideoCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallVideoInFormat.setStatus('current')
if mibBuilder.loadTexts: h320CallVideoInFormat.setDescription('This object represents the video decoding format being used in the current call in progress.')
h320CallVideoOutFormat = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 5), MmTerminalVideoCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallVideoOutFormat.setStatus('current')
if mibBuilder.loadTexts: h320CallVideoOutFormat.setDescription('This object represents the video encoding format being used in the current call in progress.')
h320CallAudioInFormat = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 6), MmTerminalAudioCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallAudioInFormat.setStatus('current')
if mibBuilder.loadTexts: h320CallAudioInFormat.setDescription('This object represents the audio decoding format being used in the current call in progress.')
h320CallAudioOutFormat = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 7), MmTerminalAudioCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallAudioOutFormat.setStatus('current')
if mibBuilder.loadTexts: h320CallAudioOutFormat.setDescription('This object represents the audio encoding format being used in the current call in progress.')
h320CallData = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 8), MmTerminalDataCapability()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallData.setStatus('current')
if mibBuilder.loadTexts: h320CallData.setDescription('This object represents the type of data communication protocol used in the call.')
h320CallEncryp = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("h233", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallEncryp.setStatus('current')
if mibBuilder.loadTexts: h320CallEncryp.setDescription('This object indicates the type of encryption protocol used in the call. 1 indicates other type of encryption. 2 indicates the encryption based on H.233.')
h320CallRDC = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("other", 1), ("h281FECC", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h320CallRDC.setStatus('current')
if mibBuilder.loadTexts: h320CallRDC.setDescription('This object indicates the type of remote device control. 1 indicates other type of device is used. 2 indicates the FECC is used. ')
h221CallStatusHangUpDirection = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nearEndUser", 1), ("nearEndSystem", 2), ("farEnd", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221CallStatusHangUpDirection.setStatus('current')
if mibBuilder.loadTexts: h221CallStatusHangUpDirection.setDescription('Identifies who initiated hanging up the last call: the near end user; the near end videoconferencing system (perhaps due to errors such as loss of framing); or the far end/ network. If a call is currently active, this refers to the previous call.')
h221CallStatusQ850Cause = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221CallStatusQ850Cause.setStatus('current')
if mibBuilder.loadTexts: h221CallStatusQ850Cause.setDescription('The Q.850 cause code received from the network when the last call hung-up. If the near end hung up the call, this field should be set to zero. If a call is currently active, this refers to the previous call.')
h221ChannelStatsTable = MibTable((0, 0, 8, 341, 1, 2, 1, 3, 1), )
if mibBuilder.loadTexts: h221ChannelStatsTable.setStatus('current')
if mibBuilder.loadTexts: h221ChannelStatsTable.setDescription('A list of statistics entries. Objects are grouped as a table so that one can use this table in the H.320 terminal, the H.320 MCU, and the H.320/H.323 gateway. The total number of statistics entries is equal to the number of H.320 entities in a system. For instance, there will be one row of statistics in the table of the H.320 terminal. The number of rows will be equal to the number of H320 entities in the MCU and the H320/H323 gateway')
h221ChannelStatsEntry = MibTableRow((0, 0, 8, 341, 1, 2, 1, 3, 1, 1), )
h320CapsEntry.registerAugmentions(("H320ENTITY-MIB", "h221ChannelStatsEntry"))
h221ChannelStatsEntry.setIndexNames(*h320CapsEntry.getIndexNames())
if mibBuilder.loadTexts: h221ChannelStatsEntry.setStatus('current')
if mibBuilder.loadTexts: h221ChannelStatsEntry.setDescription('A h221 statistics row.')
numberofConnections = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: numberofConnections.setStatus('current')
if mibBuilder.loadTexts: numberofConnections.setDescription('The number of connections in each channel in a call. For instance 2x64 has two connections ')
h221StatsInVideoFrames = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsInVideoFrames.setStatus('current')
if mibBuilder.loadTexts: h221StatsInVideoFrames.setDescription('The total number of video BCH frames received')
h221StatsInVideoFramesCorrectableErrs = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsInVideoFramesCorrectableErrs.setStatus('current')
if mibBuilder.loadTexts: h221StatsInVideoFramesCorrectableErrs.setDescription('The number of video BCH frames received with correctable errors')
h221StatsInVideoFramesUncorrectableErrs = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsInVideoFramesUncorrectableErrs.setStatus('current')
if mibBuilder.loadTexts: h221StatsInVideoFramesUncorrectableErrs.setDescription('The number of video BCH frames received with uncorrectable errors')
h221StatsOutVCU = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsOutVCU.setStatus('current')
if mibBuilder.loadTexts: h221StatsOutVCU.setDescription('The number of VCUs transmitted')
h221ConnectionStatsTable = MibTable((0, 0, 8, 341, 1, 2, 1, 3, 2), )
if mibBuilder.loadTexts: h221ConnectionStatsTable.setStatus('current')
if mibBuilder.loadTexts: h221ConnectionStatsTable.setDescription('A list of statistics entries for each port. There are two connections if the call is 2x64. These statistics get re-initialized at the start of each call and are retained after the end of the call. Thus, one can query these items after the end of call and prior to the start of a new call to get the overall statistics of the old call.')
h221ConnectionStatsEntry = MibTableRow((0, 0, 8, 341, 1, 2, 1, 3, 2, 1), ).setIndexNames((0, "H320ENTITY-MIB", "terminalIndex"), (0, "H320ENTITY-MIB", "connectionIndex"))
if mibBuilder.loadTexts: h221ConnectionStatsEntry.setStatus('current')
if mibBuilder.loadTexts: h221ConnectionStatsEntry.setDescription('A h221 statistics row.')
connectionIndex = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: connectionIndex.setStatus('current')
if mibBuilder.loadTexts: connectionIndex.setDescription('A unique value for each entry. The value ranges between 1 and the number of connections indicated in numberofConnections.')
h221StatsInFrames = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsInFrames.setStatus('current')
if mibBuilder.loadTexts: h221StatsInFrames.setDescription('The number of H.221 frames received')
h221StatsOutFrames = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsOutFrames.setStatus('current')
if mibBuilder.loadTexts: h221StatsOutFrames.setDescription('The number of H.221 frames sent')
h221StatsInFrameErrs = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsInFrameErrs.setStatus('current')
if mibBuilder.loadTexts: h221StatsInFrameErrs.setDescription('The number of error frames received')
h221StatsFrameAlignmentErrs = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsFrameAlignmentErrs.setStatus('current')
if mibBuilder.loadTexts: h221StatsFrameAlignmentErrs.setDescription('The number of times frame alignment is lost, i.e. three consecutive frame alignment words were received with an error after the establishment of frame alignment. ')
h221StatsMultiFrameAlignmentErrs = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsMultiFrameAlignmentErrs.setStatus('current')
if mibBuilder.loadTexts: h221StatsMultiFrameAlignmentErrs.setDescription('The number of times multi-frame alignment is lost, i.e. three consecutive multi-frame alignment words were received with an error after the establishment of frame alignment. ')
h221StatsErrorPerformance = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 50))).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsErrorPerformance.setStatus('current')
if mibBuilder.loadTexts: h221StatsErrorPerformance.setDescription('The quality of the 64 kbp/s connection can be monitored by counting the number of CRC blocks in error (E-bit = 1) within a period of one second (50 blocks). The following indicates the mapping between the number of CRC blocks in error and the equivalent line error rate. Percentage of CRC blocks in error Error rate 70% CRC blocks in error 10E-4 12% CRC blocks in error 10E-5 1.2% CRC blocks in error 10E-6 0.12% CRC blocks in error 10E-7 0.012% CRC blocks in error 10E-8')
h221StatsBASErrs = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsBASErrs.setStatus('current')
if mibBuilder.loadTexts: h221StatsBASErrs.setDescription('The number of BAS codes received with ECC errors ')
h221StatsCRC4Err = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsCRC4Err.setStatus('current')
if mibBuilder.loadTexts: h221StatsCRC4Err.setDescription('The number of frames received with CRC4 errors ')
h221StatsInEBit = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsInEBit.setStatus('current')
if mibBuilder.loadTexts: h221StatsInEBit.setDescription('The number of frames received with the E bit set')
h221StatsInopportuneBAS = MibTableColumn((0, 0, 8, 341, 1, 2, 1, 3, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h221StatsInopportuneBAS.setStatus('current')
if mibBuilder.loadTexts: h221StatsInopportuneBAS.setDescription('The number of BAS codes received at inappropriate times (e.g. commands received in the middle of capabilities exchange).')
h320EntityMIBConfs = MibIdentifier((0, 0, 8, 341, 1, 2, 1, 4))
h320EntityMIBGroups = MibIdentifier((0, 0, 8, 341, 1, 2, 1, 4, 1))
h320EntityMIBCompl = MibIdentifier((0, 0, 8, 341, 1, 2, 1, 4, 2))
h320CapsGroups = ObjectGroup((0, 0, 8, 341, 1, 2, 1, 4, 1, 1)).setObjects(("H320ENTITY-MIB", "h320CapsEntityLineRate"), ("H320ENTITY-MIB", "h320CapsEntityVideoFormats"), ("H320ENTITY-MIB", "h320CapsEntityMaxVideoRate"), ("H320ENTITY-MIB", "h320CapsEntityAudioTypes"), ("H320ENTITY-MIB", "h320CapsEntityDataCaps"), ("H320ENTITY-MIB", "h320CapsEntityEncryp"), ("H320ENTITY-MIB", "h320CapsEntryRDC"), ("H320ENTITY-MIB", "h221CallStatusHangUpDirection"), ("H320ENTITY-MIB", "h221CallStatusQ850Cause"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h320CapsGroups = h320CapsGroups.setStatus('current')
if mibBuilder.loadTexts: h320CapsGroups.setDescription('A collection of objects providing capabilities of the entity')
h320CallStatusGroup = ObjectGroup((0, 0, 8, 341, 1, 2, 1, 4, 1, 2)).setObjects(("H320ENTITY-MIB", "h320CallCurrentCallStatus"), ("H320ENTITY-MIB", "h320CallSiteName"), ("H320ENTITY-MIB", "h320CallLineRate"), ("H320ENTITY-MIB", "h320CallVideoInFormat"), ("H320ENTITY-MIB", "h320CallVideoOutFormat"), ("H320ENTITY-MIB", "h320CallAudioInFormat"), ("H320ENTITY-MIB", "h320CallAudioOutFormat"), ("H320ENTITY-MIB", "h320CallData"), ("H320ENTITY-MIB", "h320CallEncryp"), ("H320ENTITY-MIB", "h320CallRDC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h320CallStatusGroup = h320CallStatusGroup.setStatus('current')
if mibBuilder.loadTexts: h320CallStatusGroup.setDescription('A collection of objects providing the ability to invoke terminal functions')
h320H221StatsGroup = ObjectGroup((0, 0, 8, 341, 1, 2, 1, 4, 1, 3)).setObjects(("H320ENTITY-MIB", "numberofConnections"), ("H320ENTITY-MIB", "h221StatsInFrames"), ("H320ENTITY-MIB", "h221StatsOutFrames"), ("H320ENTITY-MIB", "h221StatsInFrameErrs"), ("H320ENTITY-MIB", "h221StatsFrameAlignmentErrs"), ("H320ENTITY-MIB", "h221StatsMultiFrameAlignmentErrs"), ("H320ENTITY-MIB", "h221StatsErrorPerformance"), ("H320ENTITY-MIB", "h221StatsBASErrs"), ("H320ENTITY-MIB", "h221StatsInVideoFrames"), ("H320ENTITY-MIB", "h221StatsInVideoFramesCorrectableErrs"), ("H320ENTITY-MIB", "h221StatsInVideoFramesUncorrectableErrs"), ("H320ENTITY-MIB", "h221StatsOutVCU"), ("H320ENTITY-MIB", "h221StatsCRC4Err"), ("H320ENTITY-MIB", "h221StatsInEBit"), ("H320ENTITY-MIB", "h221StatsInopportuneBAS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h320H221StatsGroup = h320H221StatsGroup.setStatus('current')
if mibBuilder.loadTexts: h320H221StatsGroup.setDescription('A collection of objects providing the ability to invoke terminal functions')
h221StatsCompliance = ModuleCompliance((0, 0, 8, 341, 1, 2, 1, 4, 2, 1)).setObjects(("H320ENTITY-MIB", "h320CapsGroups"), ("H320ENTITY-MIB", "h320CallStatusGroup"), ("H320ENTITY-MIB", "h320H221StatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h221StatsCompliance = h221StatsCompliance.setStatus('current')
if mibBuilder.loadTexts: h221StatsCompliance.setDescription('The set of objects required for compliance')
mibBuilder.exportSymbols("H320ENTITY-MIB", h221CallStatusQ850Cause=h221CallStatusQ850Cause, h320Capability=h320Capability, h320CallLineRate=h320CallLineRate, PYSNMP_MODULE_ID=h320Entity, h320CallCurrentCallStatus=h320CallCurrentCallStatus, h320CallSiteName=h320CallSiteName, h221StatsInVideoFramesCorrectableErrs=h221StatsInVideoFramesCorrectableErrs, h221ConnectionStatsEntry=h221ConnectionStatsEntry, h221StatsErrorPerformance=h221StatsErrorPerformance, h221StatsInopportuneBAS=h221StatsInopportuneBAS, h320EntityMIBCompl=h320EntityMIBCompl, h320CapsGroups=h320CapsGroups, h320CallStatusTable=h320CallStatusTable, h320CallAudioOutFormat=h320CallAudioOutFormat, h320CapsTable=h320CapsTable, h221StatsOutVCU=h221StatsOutVCU, h221ConnectionStatsTable=h221ConnectionStatsTable, h221StatsMultiFrameAlignmentErrs=h221StatsMultiFrameAlignmentErrs, h320CallStatusGroup=h320CallStatusGroup, h320CallStatus=h320CallStatus, h320CallStatusEntry=h320CallStatusEntry, numberofConnections=numberofConnections, h221ChannelStatsTable=h221ChannelStatsTable, h320CapsEntryRDC=h320CapsEntryRDC, h320CapsEntityLineRate=h320CapsEntityLineRate, h320CapsEntry=h320CapsEntry, h320Entity=h320Entity, h221StatsFrameAlignmentErrs=h221StatsFrameAlignmentErrs, h221StatsInVideoFrames=h221StatsInVideoFrames, h221ChannelStatsEntry=h221ChannelStatsEntry, h221StatsBASErrs=h221StatsBASErrs, connectionIndex=connectionIndex, h221StatsInEBit=h221StatsInEBit, h320CallData=h320CallData, h221StatsCompliance=h221StatsCompliance, h320CapsEntityDataCaps=h320CapsEntityDataCaps, h221StatsCRC4Err=h221StatsCRC4Err, h320H221Stats=h320H221Stats, h320EntityMIBGroups=h320EntityMIBGroups, h320H221StatsGroup=h320H221StatsGroup, h221StatsInFrames=h221StatsInFrames, h320CallEncryp=h320CallEncryp, h320CapsEntityMaxVideoRate=h320CapsEntityMaxVideoRate, h320CallRDC=h320CallRDC, h320CallVideoInFormat=h320CallVideoInFormat, h221CallStatusHangUpDirection=h221CallStatusHangUpDirection, h221StatsInVideoFramesUncorrectableErrs=h221StatsInVideoFramesUncorrectableErrs, h320CallAudioInFormat=h320CallAudioInFormat, h221StatsOutFrames=h221StatsOutFrames, terminalIndex=terminalIndex, h320CapsEntityAudioTypes=h320CapsEntityAudioTypes, h320EntityMIBConfs=h320EntityMIBConfs, h221StatsInFrameErrs=h221StatsInFrameErrs, h320CallVideoOutFormat=h320CallVideoOutFormat, h320CapsEntityVideoFormats=h320CapsEntityVideoFormats, h320CapsEntityEncryp=h320CapsEntityEncryp)