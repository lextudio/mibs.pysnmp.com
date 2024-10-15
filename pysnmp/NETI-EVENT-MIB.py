# SNMP MIB module (NETI-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:33 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(netiGeneric,) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "netiGeneric")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 RowPointer,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

netiEventMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1)
)
netiEventMIB.setRevisions(
        ("2011-05-03 10:00",
         "2009-07-09 16:00",
         "2007-03-06 00:00",
         "2004-09-10 00:00",
         "2003-11-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EventType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 3),
          ("modified", 2),
          ("none", 0))
    )



class AlarmType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("communication", 1),
          ("environmental", 5),
          ("equipment", 4),
          ("processingError", 3),
          ("qualityOfService", 2),
          ("unknown", 0))
    )



class AlarmSeverity(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 6),
          ("critical", 2),
          ("indeterminate", 1),
          ("major", 3),
          ("minor", 4),
          ("unknown", 0),
          ("warning", 5))
    )



class AlarmCause(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69)
        )
    )
    namedValues = NamedValues(
        *(("adapterError", 1),
          ("alarmIndicationSignal", 66),
          ("applicationSubsystemFailure", 2),
          ("bandwidthReduced", 3),
          ("callEstablishmentError", 4),
          ("communicationsProtocolError", 5),
          ("communicationsSubsystemFailure", 6),
          ("configurationOrCustomizationError", 7),
          ("congestion", 8),
          ("corruptData", 9),
          ("cpuCyclesLimitExceeded", 10),
          ("dTEDCEInterfaceError", 13),
          ("datasetOrModemError", 11),
          ("degradedSignal", 12),
          ("enclosureDoorOpen", 14),
          ("equipmentMalfunction", 15),
          ("excessiveVibration", 16),
          ("fileError", 17),
          ("fireDetected", 18),
          ("floodDetected", 19),
          ("framingError", 20),
          ("heatingOrVentilationOrCoolingSystemProblem", 21),
          ("humidityUnacceptable", 22),
          ("inputDeviceError", 24),
          ("inputOutputDeviceError", 23),
          ("lANError", 25),
          ("leakDetected", 26),
          ("localNodeTransmissionError", 27),
          ("lossOfFrame", 28),
          ("lossOfSignal", 29),
          ("materialSupplyExhausted", 30),
          ("multiplexerProblem", 31),
          ("outOfMemory", 32),
          ("outputDeviceError", 33),
          ("performanceDegraded", 34),
          ("phyAlarmIndicationSignal", 60),
          ("phyLossOfFrame", 59),
          ("phyLossOfSignal", 58),
          ("phyRemoteDefectIndication", 61),
          ("phySignalDegraded", 63),
          ("phySignalFailure", 62),
          ("powerProblem", 35),
          ("pressureUnacceptable", 36),
          ("processorProblem", 37),
          ("pumpFailure", 38),
          ("queueSizeExceeded", 39),
          ("receiveFailure", 40),
          ("receiverFailure", 41),
          ("remoteDefectIndication", 67),
          ("remoteNodeTransmissionError", 42),
          ("replaceableUnitMissing", 68),
          ("replaceableUnitProblem", 69),
          ("resourceAtOrNearingCapacity", 43),
          ("responseTimeExcessive", 44),
          ("retransmissionRateExcessive", 45),
          ("serviceUnavailable", 65),
          ("softwareError", 46),
          ("softwareProgramAbnormallyTerminated", 47),
          ("softwareProgramError", 48),
          ("storageCapacityProblem", 49),
          ("temperatureUnacceptable", 50),
          ("testmodeEntered", 64),
          ("thresholdCrossed", 51),
          ("timingProblem", 52),
          ("toxicLeakDetected", 53),
          ("transmitFailure", 54),
          ("transmitterFailure", 55),
          ("underlyingResourceUnavailable", 56),
          ("unknown", 0),
          ("versionMismatch", 57))
    )



# MIB Managed Objects in the order of their OIDs

_EventObjects_ObjectIdentity = ObjectIdentity
eventObjects = _EventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1)
)
_EventSequenceCounter_Type = Unsigned32
_EventSequenceCounter_Object = MibScalar
eventSequenceCounter = _EventSequenceCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 1),
    _EventSequenceCounter_Type()
)
eventSequenceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSequenceCounter.setStatus("current")
_EventLogLastChangedTime_Type = DateAndTime
_EventLogLastChangedTime_Object = MibScalar
eventLogLastChangedTime = _EventLogLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 2),
    _EventLogLastChangedTime_Type()
)
eventLogLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogLastChangedTime.setStatus("current")
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("current")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1)
)
eventEntry.setIndexNames(
    (0, "NETI-EVENT-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("current")
_EventIndex_Type = Unsigned32
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("current")
_EventObject_Type = RowPointer
_EventObject_Object = MibTableColumn
eventObject = _EventObject_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 2),
    _EventObject_Type()
)
eventObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventObject.setStatus("current")
_EventObjectName_Type = DisplayString
_EventObjectName_Object = MibTableColumn
eventObjectName = _EventObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 3),
    _EventObjectName_Type()
)
eventObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventObjectName.setStatus("current")
_EventAlarmType_Type = AlarmType
_EventAlarmType_Object = MibTableColumn
eventAlarmType = _EventAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 4),
    _EventAlarmType_Type()
)
eventAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmType.setStatus("current")
_EventType_Type = EventType
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 5),
    _EventType_Type()
)
eventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventType.setStatus("current")
_EventCause_Type = AlarmCause
_EventCause_Object = MibTableColumn
eventCause = _EventCause_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 6),
    _EventCause_Type()
)
eventCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCause.setStatus("current")
_EventSeverity_Type = AlarmSeverity
_EventSeverity_Object = MibTableColumn
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 7),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("current")
_EventText_Type = DisplayString
_EventText_Object = MibTableColumn
eventText = _EventText_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 8),
    _EventText_Type()
)
eventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventText.setStatus("current")
_EventCreatedTime_Type = DateAndTime
_EventCreatedTime_Object = MibTableColumn
eventCreatedTime = _EventCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 9),
    _EventCreatedTime_Type()
)
eventCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCreatedTime.setStatus("current")
_EventAlarmTable_Object = MibTable
eventAlarmTable = _EventAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    eventAlarmTable.setStatus("current")
_EventAlarmEntry_Object = MibTableRow
eventAlarmEntry = _EventAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1)
)
eventAlarmEntry.setIndexNames(
    (0, "NETI-EVENT-MIB", "eventAlarmIndex"),
)
if mibBuilder.loadTexts:
    eventAlarmEntry.setStatus("current")
_EventAlarmIndex_Type = Unsigned32
_EventAlarmIndex_Object = MibTableColumn
eventAlarmIndex = _EventAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 1),
    _EventAlarmIndex_Type()
)
eventAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmIndex.setStatus("current")
_EventAlarmObject_Type = RowPointer
_EventAlarmObject_Object = MibTableColumn
eventAlarmObject = _EventAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 2),
    _EventAlarmObject_Type()
)
eventAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmObject.setStatus("current")
_EventAlarmObjectName_Type = DisplayString
_EventAlarmObjectName_Object = MibTableColumn
eventAlarmObjectName = _EventAlarmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 3),
    _EventAlarmObjectName_Type()
)
eventAlarmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmObjectName.setStatus("current")
_EventAlarmAlarmType_Type = AlarmType
_EventAlarmAlarmType_Object = MibTableColumn
eventAlarmAlarmType = _EventAlarmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 4),
    _EventAlarmAlarmType_Type()
)
eventAlarmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmAlarmType.setStatus("current")
_EventAlarmCause_Type = AlarmCause
_EventAlarmCause_Object = MibTableColumn
eventAlarmCause = _EventAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 5),
    _EventAlarmCause_Type()
)
eventAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmCause.setStatus("current")
_EventAlarmSeverity_Type = AlarmSeverity
_EventAlarmSeverity_Object = MibTableColumn
eventAlarmSeverity = _EventAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 6),
    _EventAlarmSeverity_Type()
)
eventAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmSeverity.setStatus("current")
_EventAlarmText_Type = DisplayString
_EventAlarmText_Object = MibTableColumn
eventAlarmText = _EventAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 7),
    _EventAlarmText_Type()
)
eventAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmText.setStatus("current")
_EventAlarmLastChangedTime_Type = DateAndTime
_EventAlarmLastChangedTime_Object = MibTableColumn
eventAlarmLastChangedTime = _EventAlarmLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 8),
    _EventAlarmLastChangedTime_Type()
)
eventAlarmLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmLastChangedTime.setStatus("current")
_EventAlarmAcknowledged_Type = TruthValue
_EventAlarmAcknowledged_Object = MibTableColumn
eventAlarmAcknowledged = _EventAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 9),
    _EventAlarmAcknowledged_Type()
)
eventAlarmAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventAlarmAcknowledged.setStatus("current")
_EventAlarmCreatedTime_Type = DateAndTime
_EventAlarmCreatedTime_Object = MibTableColumn
eventAlarmCreatedTime = _EventAlarmCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 10),
    _EventAlarmCreatedTime_Type()
)
eventAlarmCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventAlarmCreatedTime.setStatus("current")
_EventAlarmCountersGroup_ObjectIdentity = ObjectIdentity
eventAlarmCountersGroup = _EventAlarmCountersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5)
)
_EventCriticalCounter_Type = Unsigned32
_EventCriticalCounter_Object = MibScalar
eventCriticalCounter = _EventCriticalCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 1),
    _EventCriticalCounter_Type()
)
eventCriticalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventCriticalCounter.setStatus("current")
_EventMajorCounter_Type = Unsigned32
_EventMajorCounter_Object = MibScalar
eventMajorCounter = _EventMajorCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 2),
    _EventMajorCounter_Type()
)
eventMajorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventMajorCounter.setStatus("current")
_EventMinorCounter_Type = Unsigned32
_EventMinorCounter_Object = MibScalar
eventMinorCounter = _EventMinorCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 3),
    _EventMinorCounter_Type()
)
eventMinorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventMinorCounter.setStatus("current")
_EventWarningCounter_Type = Unsigned32
_EventWarningCounter_Object = MibScalar
eventWarningCounter = _EventWarningCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 4),
    _EventWarningCounter_Type()
)
eventWarningCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventWarningCounter.setStatus("current")
_EventIndeterminateCounter_Type = Unsigned32
_EventIndeterminateCounter_Object = MibScalar
eventIndeterminateCounter = _EventIndeterminateCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 5),
    _EventIndeterminateCounter_Type()
)
eventIndeterminateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndeterminateCounter.setStatus("current")
_EventActiveAlarmTable_Object = MibTable
eventActiveAlarmTable = _EventActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    eventActiveAlarmTable.setStatus("current")
_EventActiveAlarmEntry_Object = MibTableRow
eventActiveAlarmEntry = _EventActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1)
)
eventActiveAlarmEntry.setIndexNames(
    (0, "NETI-EVENT-MIB", "eventActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    eventActiveAlarmEntry.setStatus("current")
_EventActiveAlarmIndex_Type = Unsigned32
_EventActiveAlarmIndex_Object = MibTableColumn
eventActiveAlarmIndex = _EventActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 1),
    _EventActiveAlarmIndex_Type()
)
eventActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmIndex.setStatus("current")
_EventActiveAlarmObject_Type = RowPointer
_EventActiveAlarmObject_Object = MibTableColumn
eventActiveAlarmObject = _EventActiveAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 2),
    _EventActiveAlarmObject_Type()
)
eventActiveAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmObject.setStatus("current")
_EventActiveAlarmObjectName_Type = DisplayString
_EventActiveAlarmObjectName_Object = MibTableColumn
eventActiveAlarmObjectName = _EventActiveAlarmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 3),
    _EventActiveAlarmObjectName_Type()
)
eventActiveAlarmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmObjectName.setStatus("current")
_EventActiveAlarmAlarmType_Type = AlarmType
_EventActiveAlarmAlarmType_Object = MibTableColumn
eventActiveAlarmAlarmType = _EventActiveAlarmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 4),
    _EventActiveAlarmAlarmType_Type()
)
eventActiveAlarmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmAlarmType.setStatus("current")
_EventActiveAlarmCause_Type = AlarmCause
_EventActiveAlarmCause_Object = MibTableColumn
eventActiveAlarmCause = _EventActiveAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 5),
    _EventActiveAlarmCause_Type()
)
eventActiveAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmCause.setStatus("current")
_EventActiveAlarmSeverity_Type = AlarmSeverity
_EventActiveAlarmSeverity_Object = MibTableColumn
eventActiveAlarmSeverity = _EventActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 6),
    _EventActiveAlarmSeverity_Type()
)
eventActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmSeverity.setStatus("current")
_EventActiveAlarmText_Type = DisplayString
_EventActiveAlarmText_Object = MibTableColumn
eventActiveAlarmText = _EventActiveAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 7),
    _EventActiveAlarmText_Type()
)
eventActiveAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmText.setStatus("current")
_EventActiveAlarmLastChangedTime_Type = DateAndTime
_EventActiveAlarmLastChangedTime_Object = MibTableColumn
eventActiveAlarmLastChangedTime = _EventActiveAlarmLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 8),
    _EventActiveAlarmLastChangedTime_Type()
)
eventActiveAlarmLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmLastChangedTime.setStatus("current")
_EventActiveAlarmAcknowledged_Type = TruthValue
_EventActiveAlarmAcknowledged_Object = MibTableColumn
eventActiveAlarmAcknowledged = _EventActiveAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 9),
    _EventActiveAlarmAcknowledged_Type()
)
eventActiveAlarmAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventActiveAlarmAcknowledged.setStatus("current")
_EventActiveAlarmCreatedTime_Type = DateAndTime
_EventActiveAlarmCreatedTime_Object = MibTableColumn
eventActiveAlarmCreatedTime = _EventActiveAlarmCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 10),
    _EventActiveAlarmCreatedTime_Type()
)
eventActiveAlarmCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventActiveAlarmCreatedTime.setStatus("current")
_EventNotificationObjectsGroup_ObjectIdentity = ObjectIdentity
eventNotificationObjectsGroup = _EventNotificationObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 7)
)
_EventTrapPurpose_Type = SnmpAdminString
_EventTrapPurpose_Object = MibScalar
eventTrapPurpose = _EventTrapPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 7, 1),
    _EventTrapPurpose_Type()
)
eventTrapPurpose.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    eventTrapPurpose.setStatus("current")
_EventNotifications_ObjectIdentity = ObjectIdentity
eventNotifications = _EventNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2)
)
_EventConformanceGroups_ObjectIdentity = ObjectIdentity
eventConformanceGroups = _EventConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 3)
)

# Managed Objects groups

eventConformanceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 3, 1)
)
eventConformanceGroup.setObjects(
      *(("NETI-EVENT-MIB", "eventSequenceCounter"),
        ("NETI-EVENT-MIB", "eventLogLastChangedTime"),
        ("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventAlarmIndex"),
        ("NETI-EVENT-MIB", "eventAlarmObject"),
        ("NETI-EVENT-MIB", "eventAlarmObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmAlarmType"),
        ("NETI-EVENT-MIB", "eventAlarmCause"),
        ("NETI-EVENT-MIB", "eventAlarmSeverity"),
        ("NETI-EVENT-MIB", "eventAlarmText"),
        ("NETI-EVENT-MIB", "eventAlarmLastChangedTime"),
        ("NETI-EVENT-MIB", "eventAlarmAcknowledged"),
        ("NETI-EVENT-MIB", "eventAlarmCreatedTime"),
        ("NETI-EVENT-MIB", "eventActiveAlarmIndex"),
        ("NETI-EVENT-MIB", "eventActiveAlarmObject"),
        ("NETI-EVENT-MIB", "eventActiveAlarmObjectName"),
        ("NETI-EVENT-MIB", "eventActiveAlarmAlarmType"),
        ("NETI-EVENT-MIB", "eventActiveAlarmCause"),
        ("NETI-EVENT-MIB", "eventActiveAlarmSeverity"),
        ("NETI-EVENT-MIB", "eventActiveAlarmText"),
        ("NETI-EVENT-MIB", "eventActiveAlarmLastChangedTime"),
        ("NETI-EVENT-MIB", "eventActiveAlarmAcknowledged"),
        ("NETI-EVENT-MIB", "eventActiveAlarmCreatedTime"),
        ("NETI-EVENT-MIB", "eventCriticalCounter"),
        ("NETI-EVENT-MIB", "eventMajorCounter"),
        ("NETI-EVENT-MIB", "eventMinorCounter"),
        ("NETI-EVENT-MIB", "eventWarningCounter"),
        ("NETI-EVENT-MIB", "eventIndeterminateCounter"))
)
if mibBuilder.loadTexts:
    eventConformanceGroup.setStatus("current")


# Notification objects

eventAlarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 1)
)
eventAlarmCritical.setObjects(
      *(("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    eventAlarmCritical.setStatus(
        "current"
    )

eventAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 2)
)
eventAlarmMajor.setObjects(
      *(("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    eventAlarmMajor.setStatus(
        "current"
    )

eventAlarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 3)
)
eventAlarmMinor.setObjects(
      *(("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    eventAlarmMinor.setStatus(
        "current"
    )

eventAlarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 4)
)
eventAlarmWarning.setObjects(
      *(("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    eventAlarmWarning.setStatus(
        "current"
    )

eventAlarmIndeterminate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 5)
)
eventAlarmIndeterminate.setObjects(
      *(("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    eventAlarmIndeterminate.setStatus(
        "current"
    )

eventAlarmUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 6)
)
eventAlarmUnknown.setObjects(
      *(("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    eventAlarmUnknown.setStatus(
        "current"
    )

eventAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 7)
)
eventAlarmClear.setObjects(
      *(("NETI-EVENT-MIB", "eventIndex"),
        ("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventAlarmType"),
        ("NETI-EVENT-MIB", "eventCause"),
        ("NETI-EVENT-MIB", "eventSeverity"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    eventAlarmClear.setStatus(
        "current"
    )

netiGenericEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 8)
)
netiGenericEvent.setObjects(
      *(("NETI-EVENT-MIB", "eventObject"),
        ("NETI-EVENT-MIB", "eventObjectName"),
        ("NETI-EVENT-MIB", "eventType"),
        ("NETI-EVENT-MIB", "eventText"),
        ("NETI-EVENT-MIB", "eventCreatedTime"),
        ("NETI-EVENT-MIB", "eventSequenceCounter"))
)
if mibBuilder.loadTexts:
    netiGenericEvent.setStatus(
        "current"
    )


# Notifications groups

eventNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 3, 2)
)
eventNotificationsGroup.setObjects(
      *(("NETI-EVENT-MIB", "eventAlarmCritical"),
        ("NETI-EVENT-MIB", "eventAlarmMajor"),
        ("NETI-EVENT-MIB", "eventAlarmMinor"),
        ("NETI-EVENT-MIB", "eventAlarmWarning"),
        ("NETI-EVENT-MIB", "eventAlarmIndeterminate"),
        ("NETI-EVENT-MIB", "eventAlarmUnknown"),
        ("NETI-EVENT-MIB", "eventAlarmClear"),
        ("NETI-EVENT-MIB", "netiGenericEvent"))
)
if mibBuilder.loadTexts:
    eventNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-EVENT-MIB",
    **{"EventType": EventType,
       "AlarmType": AlarmType,
       "AlarmSeverity": AlarmSeverity,
       "AlarmCause": AlarmCause,
       "netiEventMIB": netiEventMIB,
       "eventObjects": eventObjects,
       "eventSequenceCounter": eventSequenceCounter,
       "eventLogLastChangedTime": eventLogLastChangedTime,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventObject": eventObject,
       "eventObjectName": eventObjectName,
       "eventAlarmType": eventAlarmType,
       "eventType": eventType,
       "eventCause": eventCause,
       "eventSeverity": eventSeverity,
       "eventText": eventText,
       "eventCreatedTime": eventCreatedTime,
       "eventAlarmTable": eventAlarmTable,
       "eventAlarmEntry": eventAlarmEntry,
       "eventAlarmIndex": eventAlarmIndex,
       "eventAlarmObject": eventAlarmObject,
       "eventAlarmObjectName": eventAlarmObjectName,
       "eventAlarmAlarmType": eventAlarmAlarmType,
       "eventAlarmCause": eventAlarmCause,
       "eventAlarmSeverity": eventAlarmSeverity,
       "eventAlarmText": eventAlarmText,
       "eventAlarmLastChangedTime": eventAlarmLastChangedTime,
       "eventAlarmAcknowledged": eventAlarmAcknowledged,
       "eventAlarmCreatedTime": eventAlarmCreatedTime,
       "eventAlarmCountersGroup": eventAlarmCountersGroup,
       "eventCriticalCounter": eventCriticalCounter,
       "eventMajorCounter": eventMajorCounter,
       "eventMinorCounter": eventMinorCounter,
       "eventWarningCounter": eventWarningCounter,
       "eventIndeterminateCounter": eventIndeterminateCounter,
       "eventActiveAlarmTable": eventActiveAlarmTable,
       "eventActiveAlarmEntry": eventActiveAlarmEntry,
       "eventActiveAlarmIndex": eventActiveAlarmIndex,
       "eventActiveAlarmObject": eventActiveAlarmObject,
       "eventActiveAlarmObjectName": eventActiveAlarmObjectName,
       "eventActiveAlarmAlarmType": eventActiveAlarmAlarmType,
       "eventActiveAlarmCause": eventActiveAlarmCause,
       "eventActiveAlarmSeverity": eventActiveAlarmSeverity,
       "eventActiveAlarmText": eventActiveAlarmText,
       "eventActiveAlarmLastChangedTime": eventActiveAlarmLastChangedTime,
       "eventActiveAlarmAcknowledged": eventActiveAlarmAcknowledged,
       "eventActiveAlarmCreatedTime": eventActiveAlarmCreatedTime,
       "eventNotificationObjectsGroup": eventNotificationObjectsGroup,
       "eventTrapPurpose": eventTrapPurpose,
       "eventNotifications": eventNotifications,
       "eventAlarmCritical": eventAlarmCritical,
       "eventAlarmMajor": eventAlarmMajor,
       "eventAlarmMinor": eventAlarmMinor,
       "eventAlarmWarning": eventAlarmWarning,
       "eventAlarmIndeterminate": eventAlarmIndeterminate,
       "eventAlarmUnknown": eventAlarmUnknown,
       "eventAlarmClear": eventAlarmClear,
       "netiGenericEvent": netiGenericEvent,
       "eventConformanceGroups": eventConformanceGroups,
       "eventConformanceGroup": eventConformanceGroup,
       "eventNotificationsGroup": eventNotificationsGroup}
)
