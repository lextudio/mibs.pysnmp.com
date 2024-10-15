# SNMP MIB module (NETI-EVT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-EVT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:34 2024
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
 enterprises,
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
    "enterprises",
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

nevtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1)
)
nevtMIB.setRevisions(
        ("2015-03-03 16:00",
         "2013-06-03 11:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NevtEventType(Integer32, TextualConvention):
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



class NevtAlarmType(Integer32, TextualConvention):
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



class NevtAlarmSeverity(Integer32, TextualConvention):
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



class NevtAlarmCause(Integer32, TextualConvention):
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

_Netinsight_ObjectIdentity = ObjectIdentity
netinsight = _Netinsight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928)
)
_NetiGeneric_ObjectIdentity = ObjectIdentity
netiGeneric = _NetiGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2)
)
_NevtObjects_ObjectIdentity = ObjectIdentity
nevtObjects = _NevtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1)
)
_NevtSequenceCounter_Type = Unsigned32
_NevtSequenceCounter_Object = MibScalar
nevtSequenceCounter = _NevtSequenceCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 1),
    _NevtSequenceCounter_Type()
)
nevtSequenceCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtSequenceCounter.setStatus("current")
_NevtLastChangedTime_Type = DateAndTime
_NevtLastChangedTime_Object = MibScalar
nevtLastChangedTime = _NevtLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 2),
    _NevtLastChangedTime_Type()
)
nevtLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtLastChangedTime.setStatus("current")
_NevtEventTable_Object = MibTable
nevtEventTable = _NevtEventTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    nevtEventTable.setStatus("current")
_NevtEventEntry_Object = MibTableRow
nevtEventEntry = _NevtEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1)
)
nevtEventEntry.setIndexNames(
    (0, "NETI-EVT-MIB", "nevtEventIndex"),
)
if mibBuilder.loadTexts:
    nevtEventEntry.setStatus("current")
_NevtEventIndex_Type = Unsigned32
_NevtEventIndex_Object = MibTableColumn
nevtEventIndex = _NevtEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 1),
    _NevtEventIndex_Type()
)
nevtEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventIndex.setStatus("current")
_NevtEventObject_Type = RowPointer
_NevtEventObject_Object = MibTableColumn
nevtEventObject = _NevtEventObject_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 2),
    _NevtEventObject_Type()
)
nevtEventObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventObject.setStatus("current")
_NevtEventObjectName_Type = DisplayString
_NevtEventObjectName_Object = MibTableColumn
nevtEventObjectName = _NevtEventObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 3),
    _NevtEventObjectName_Type()
)
nevtEventObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventObjectName.setStatus("current")
_NevtEventAlarmType_Type = NevtAlarmType
_NevtEventAlarmType_Object = MibTableColumn
nevtEventAlarmType = _NevtEventAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 4),
    _NevtEventAlarmType_Type()
)
nevtEventAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventAlarmType.setStatus("current")
_NevtEventType_Type = NevtEventType
_NevtEventType_Object = MibTableColumn
nevtEventType = _NevtEventType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 5),
    _NevtEventType_Type()
)
nevtEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventType.setStatus("current")
_NevtEventCause_Type = NevtAlarmCause
_NevtEventCause_Object = MibTableColumn
nevtEventCause = _NevtEventCause_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 6),
    _NevtEventCause_Type()
)
nevtEventCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventCause.setStatus("current")
_NevtEventSeverity_Type = NevtAlarmSeverity
_NevtEventSeverity_Object = MibTableColumn
nevtEventSeverity = _NevtEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 7),
    _NevtEventSeverity_Type()
)
nevtEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventSeverity.setStatus("current")
_NevtEventText_Type = DisplayString
_NevtEventText_Object = MibTableColumn
nevtEventText = _NevtEventText_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 8),
    _NevtEventText_Type()
)
nevtEventText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventText.setStatus("current")
_NevtEventCreatedTime_Type = DateAndTime
_NevtEventCreatedTime_Object = MibTableColumn
nevtEventCreatedTime = _NevtEventCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 9),
    _NevtEventCreatedTime_Type()
)
nevtEventCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventCreatedTime.setStatus("current")
_NevtEventPurpose_Type = SnmpAdminString
_NevtEventPurpose_Object = MibTableColumn
nevtEventPurpose = _NevtEventPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 3, 1, 10),
    _NevtEventPurpose_Type()
)
nevtEventPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtEventPurpose.setStatus("current")
_NevtAlarmTable_Object = MibTable
nevtAlarmTable = _NevtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    nevtAlarmTable.setStatus("current")
_NevtAlarmEntry_Object = MibTableRow
nevtAlarmEntry = _NevtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1)
)
nevtAlarmEntry.setIndexNames(
    (0, "NETI-EVT-MIB", "nevtAlarmIndex"),
)
if mibBuilder.loadTexts:
    nevtAlarmEntry.setStatus("current")
_NevtAlarmIndex_Type = Unsigned32
_NevtAlarmIndex_Object = MibTableColumn
nevtAlarmIndex = _NevtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 1),
    _NevtAlarmIndex_Type()
)
nevtAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmIndex.setStatus("current")
_NevtAlarmObject_Type = RowPointer
_NevtAlarmObject_Object = MibTableColumn
nevtAlarmObject = _NevtAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 2),
    _NevtAlarmObject_Type()
)
nevtAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmObject.setStatus("current")
_NevtAlarmObjectName_Type = DisplayString
_NevtAlarmObjectName_Object = MibTableColumn
nevtAlarmObjectName = _NevtAlarmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 3),
    _NevtAlarmObjectName_Type()
)
nevtAlarmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmObjectName.setStatus("current")
_NevtAlarmAlarmType_Type = NevtAlarmType
_NevtAlarmAlarmType_Object = MibTableColumn
nevtAlarmAlarmType = _NevtAlarmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 4),
    _NevtAlarmAlarmType_Type()
)
nevtAlarmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmAlarmType.setStatus("current")
_NevtAlarmCause_Type = NevtAlarmCause
_NevtAlarmCause_Object = MibTableColumn
nevtAlarmCause = _NevtAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 5),
    _NevtAlarmCause_Type()
)
nevtAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmCause.setStatus("current")
_NevtAlarmSeverity_Type = NevtAlarmSeverity
_NevtAlarmSeverity_Object = MibTableColumn
nevtAlarmSeverity = _NevtAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 6),
    _NevtAlarmSeverity_Type()
)
nevtAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmSeverity.setStatus("current")
_NevtAlarmText_Type = DisplayString
_NevtAlarmText_Object = MibTableColumn
nevtAlarmText = _NevtAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 7),
    _NevtAlarmText_Type()
)
nevtAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmText.setStatus("current")
_NevtAlarmLastChangedTime_Type = DateAndTime
_NevtAlarmLastChangedTime_Object = MibTableColumn
nevtAlarmLastChangedTime = _NevtAlarmLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 8),
    _NevtAlarmLastChangedTime_Type()
)
nevtAlarmLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmLastChangedTime.setStatus("current")
_NevtAlarmAcknowledged_Type = TruthValue
_NevtAlarmAcknowledged_Object = MibTableColumn
nevtAlarmAcknowledged = _NevtAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 9),
    _NevtAlarmAcknowledged_Type()
)
nevtAlarmAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nevtAlarmAcknowledged.setStatus("current")
_NevtAlarmCreatedTime_Type = DateAndTime
_NevtAlarmCreatedTime_Object = MibTableColumn
nevtAlarmCreatedTime = _NevtAlarmCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 10),
    _NevtAlarmCreatedTime_Type()
)
nevtAlarmCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmCreatedTime.setStatus("current")
_NevtAlarmPurpose_Type = SnmpAdminString
_NevtAlarmPurpose_Object = MibTableColumn
nevtAlarmPurpose = _NevtAlarmPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 4, 1, 11),
    _NevtAlarmPurpose_Type()
)
nevtAlarmPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtAlarmPurpose.setStatus("current")
_NevtAlarmCountersGroup_ObjectIdentity = ObjectIdentity
nevtAlarmCountersGroup = _NevtAlarmCountersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5)
)
_NevtCriticalCounter_Type = Unsigned32
_NevtCriticalCounter_Object = MibScalar
nevtCriticalCounter = _NevtCriticalCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 1),
    _NevtCriticalCounter_Type()
)
nevtCriticalCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtCriticalCounter.setStatus("current")
_NevtMajorCounter_Type = Unsigned32
_NevtMajorCounter_Object = MibScalar
nevtMajorCounter = _NevtMajorCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 2),
    _NevtMajorCounter_Type()
)
nevtMajorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtMajorCounter.setStatus("current")
_NevtMinorCounter_Type = Unsigned32
_NevtMinorCounter_Object = MibScalar
nevtMinorCounter = _NevtMinorCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 3),
    _NevtMinorCounter_Type()
)
nevtMinorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtMinorCounter.setStatus("current")
_NevtWarningCounter_Type = Unsigned32
_NevtWarningCounter_Object = MibScalar
nevtWarningCounter = _NevtWarningCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 4),
    _NevtWarningCounter_Type()
)
nevtWarningCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtWarningCounter.setStatus("current")
_NevtIndeterminateCounter_Type = Unsigned32
_NevtIndeterminateCounter_Object = MibScalar
nevtIndeterminateCounter = _NevtIndeterminateCounter_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 5, 5),
    _NevtIndeterminateCounter_Type()
)
nevtIndeterminateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtIndeterminateCounter.setStatus("current")
_NevtActiveAlarmTable_Object = MibTable
nevtActiveAlarmTable = _NevtActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    nevtActiveAlarmTable.setStatus("current")
_NevtActiveAlarmEntry_Object = MibTableRow
nevtActiveAlarmEntry = _NevtActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1)
)
nevtActiveAlarmEntry.setIndexNames(
    (0, "NETI-EVT-MIB", "nevtActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    nevtActiveAlarmEntry.setStatus("current")
_NevtActiveAlarmIndex_Type = Unsigned32
_NevtActiveAlarmIndex_Object = MibTableColumn
nevtActiveAlarmIndex = _NevtActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 1),
    _NevtActiveAlarmIndex_Type()
)
nevtActiveAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmIndex.setStatus("current")
_NevtActiveAlarmObject_Type = RowPointer
_NevtActiveAlarmObject_Object = MibTableColumn
nevtActiveAlarmObject = _NevtActiveAlarmObject_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 2),
    _NevtActiveAlarmObject_Type()
)
nevtActiveAlarmObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmObject.setStatus("current")
_NevtActiveAlarmObjectName_Type = DisplayString
_NevtActiveAlarmObjectName_Object = MibTableColumn
nevtActiveAlarmObjectName = _NevtActiveAlarmObjectName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 3),
    _NevtActiveAlarmObjectName_Type()
)
nevtActiveAlarmObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmObjectName.setStatus("current")
_NevtActiveAlarmAlarmType_Type = NevtAlarmType
_NevtActiveAlarmAlarmType_Object = MibTableColumn
nevtActiveAlarmAlarmType = _NevtActiveAlarmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 4),
    _NevtActiveAlarmAlarmType_Type()
)
nevtActiveAlarmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmAlarmType.setStatus("current")
_NevtActiveAlarmCause_Type = NevtAlarmCause
_NevtActiveAlarmCause_Object = MibTableColumn
nevtActiveAlarmCause = _NevtActiveAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 5),
    _NevtActiveAlarmCause_Type()
)
nevtActiveAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmCause.setStatus("current")
_NevtActiveAlarmSeverity_Type = NevtAlarmSeverity
_NevtActiveAlarmSeverity_Object = MibTableColumn
nevtActiveAlarmSeverity = _NevtActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 6),
    _NevtActiveAlarmSeverity_Type()
)
nevtActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmSeverity.setStatus("current")
_NevtActiveAlarmText_Type = DisplayString
_NevtActiveAlarmText_Object = MibTableColumn
nevtActiveAlarmText = _NevtActiveAlarmText_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 7),
    _NevtActiveAlarmText_Type()
)
nevtActiveAlarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmText.setStatus("current")
_NevtActiveAlarmLastChangedTime_Type = DateAndTime
_NevtActiveAlarmLastChangedTime_Object = MibTableColumn
nevtActiveAlarmLastChangedTime = _NevtActiveAlarmLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 8),
    _NevtActiveAlarmLastChangedTime_Type()
)
nevtActiveAlarmLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmLastChangedTime.setStatus("current")
_NevtActiveAlarmAcknowledged_Type = TruthValue
_NevtActiveAlarmAcknowledged_Object = MibTableColumn
nevtActiveAlarmAcknowledged = _NevtActiveAlarmAcknowledged_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 9),
    _NevtActiveAlarmAcknowledged_Type()
)
nevtActiveAlarmAcknowledged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nevtActiveAlarmAcknowledged.setStatus("current")
_NevtActiveAlarmCreatedTime_Type = DateAndTime
_NevtActiveAlarmCreatedTime_Object = MibTableColumn
nevtActiveAlarmCreatedTime = _NevtActiveAlarmCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 10),
    _NevtActiveAlarmCreatedTime_Type()
)
nevtActiveAlarmCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmCreatedTime.setStatus("current")
_NevtActiveAlarmPurpose_Type = SnmpAdminString
_NevtActiveAlarmPurpose_Object = MibTableColumn
nevtActiveAlarmPurpose = _NevtActiveAlarmPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 6, 1, 11),
    _NevtActiveAlarmPurpose_Type()
)
nevtActiveAlarmPurpose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nevtActiveAlarmPurpose.setStatus("current")
_NevtNotificationObjectsGroup_ObjectIdentity = ObjectIdentity
nevtNotificationObjectsGroup = _NevtNotificationObjectsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 7)
)
_NevtTrapPurpose_Type = SnmpAdminString
_NevtTrapPurpose_Object = MibScalar
nevtTrapPurpose = _NevtTrapPurpose_Object(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 1, 7, 1),
    _NevtTrapPurpose_Type()
)
nevtTrapPurpose.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nevtTrapPurpose.setStatus("obsolete")
_NevtNotifications_ObjectIdentity = ObjectIdentity
nevtNotifications = _NevtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2)
)
_NevtConformanceGroups_ObjectIdentity = ObjectIdentity
nevtConformanceGroups = _NevtConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 3)
)

# Managed Objects groups


# Notification objects

nevtAlarmCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 1)
)
nevtAlarmCritical.setObjects(
      *(("NETI-EVT-MIB", "nevtEventIndex"),
        ("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventAlarmType"),
        ("NETI-EVT-MIB", "nevtEventCause"),
        ("NETI-EVT-MIB", "nevtEventSeverity"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtAlarmCritical.setStatus(
        "current"
    )

nevtAlarmMajor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 2)
)
nevtAlarmMajor.setObjects(
      *(("NETI-EVT-MIB", "nevtEventIndex"),
        ("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventAlarmType"),
        ("NETI-EVT-MIB", "nevtEventCause"),
        ("NETI-EVT-MIB", "nevtEventSeverity"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtAlarmMajor.setStatus(
        "current"
    )

nevtAlarmMinor = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 3)
)
nevtAlarmMinor.setObjects(
      *(("NETI-EVT-MIB", "nevtEventIndex"),
        ("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventAlarmType"),
        ("NETI-EVT-MIB", "nevtEventCause"),
        ("NETI-EVT-MIB", "nevtEventSeverity"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtAlarmMinor.setStatus(
        "current"
    )

nevtAlarmWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 4)
)
nevtAlarmWarning.setObjects(
      *(("NETI-EVT-MIB", "nevtEventIndex"),
        ("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventAlarmType"),
        ("NETI-EVT-MIB", "nevtEventCause"),
        ("NETI-EVT-MIB", "nevtEventSeverity"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtAlarmWarning.setStatus(
        "current"
    )

nevtAlarmIndeterminate = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 5)
)
nevtAlarmIndeterminate.setObjects(
      *(("NETI-EVT-MIB", "nevtEventIndex"),
        ("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventAlarmType"),
        ("NETI-EVT-MIB", "nevtEventCause"),
        ("NETI-EVT-MIB", "nevtEventSeverity"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtAlarmIndeterminate.setStatus(
        "current"
    )

nevtAlarmUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 6)
)
nevtAlarmUnknown.setObjects(
      *(("NETI-EVT-MIB", "nevtEventIndex"),
        ("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventAlarmType"),
        ("NETI-EVT-MIB", "nevtEventCause"),
        ("NETI-EVT-MIB", "nevtEventSeverity"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtAlarmUnknown.setStatus(
        "current"
    )

nevtAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 7)
)
nevtAlarmClear.setObjects(
      *(("NETI-EVT-MIB", "nevtEventIndex"),
        ("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventAlarmType"),
        ("NETI-EVT-MIB", "nevtEventCause"),
        ("NETI-EVT-MIB", "nevtEventSeverity"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtAlarmClear.setStatus(
        "current"
    )

nevtGenericEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2928, 2, 1, 2, 8)
)
nevtGenericEvent.setObjects(
      *(("NETI-EVT-MIB", "nevtEventObject"),
        ("NETI-EVT-MIB", "nevtEventObjectName"),
        ("NETI-EVT-MIB", "nevtEventType"),
        ("NETI-EVT-MIB", "nevtEventText"),
        ("NETI-EVT-MIB", "nevtEventCreatedTime"),
        ("NETI-EVT-MIB", "nevtSequenceCounter"),
        ("NETI-EVT-MIB", "nevtEventPurpose"))
)
if mibBuilder.loadTexts:
    nevtGenericEvent.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-EVT-MIB",
    **{"NevtEventType": NevtEventType,
       "NevtAlarmType": NevtAlarmType,
       "NevtAlarmSeverity": NevtAlarmSeverity,
       "NevtAlarmCause": NevtAlarmCause,
       "netinsight": netinsight,
       "netiGeneric": netiGeneric,
       "nevtMIB": nevtMIB,
       "nevtObjects": nevtObjects,
       "nevtSequenceCounter": nevtSequenceCounter,
       "nevtLastChangedTime": nevtLastChangedTime,
       "nevtEventTable": nevtEventTable,
       "nevtEventEntry": nevtEventEntry,
       "nevtEventIndex": nevtEventIndex,
       "nevtEventObject": nevtEventObject,
       "nevtEventObjectName": nevtEventObjectName,
       "nevtEventAlarmType": nevtEventAlarmType,
       "nevtEventType": nevtEventType,
       "nevtEventCause": nevtEventCause,
       "nevtEventSeverity": nevtEventSeverity,
       "nevtEventText": nevtEventText,
       "nevtEventCreatedTime": nevtEventCreatedTime,
       "nevtEventPurpose": nevtEventPurpose,
       "nevtAlarmTable": nevtAlarmTable,
       "nevtAlarmEntry": nevtAlarmEntry,
       "nevtAlarmIndex": nevtAlarmIndex,
       "nevtAlarmObject": nevtAlarmObject,
       "nevtAlarmObjectName": nevtAlarmObjectName,
       "nevtAlarmAlarmType": nevtAlarmAlarmType,
       "nevtAlarmCause": nevtAlarmCause,
       "nevtAlarmSeverity": nevtAlarmSeverity,
       "nevtAlarmText": nevtAlarmText,
       "nevtAlarmLastChangedTime": nevtAlarmLastChangedTime,
       "nevtAlarmAcknowledged": nevtAlarmAcknowledged,
       "nevtAlarmCreatedTime": nevtAlarmCreatedTime,
       "nevtAlarmPurpose": nevtAlarmPurpose,
       "nevtAlarmCountersGroup": nevtAlarmCountersGroup,
       "nevtCriticalCounter": nevtCriticalCounter,
       "nevtMajorCounter": nevtMajorCounter,
       "nevtMinorCounter": nevtMinorCounter,
       "nevtWarningCounter": nevtWarningCounter,
       "nevtIndeterminateCounter": nevtIndeterminateCounter,
       "nevtActiveAlarmTable": nevtActiveAlarmTable,
       "nevtActiveAlarmEntry": nevtActiveAlarmEntry,
       "nevtActiveAlarmIndex": nevtActiveAlarmIndex,
       "nevtActiveAlarmObject": nevtActiveAlarmObject,
       "nevtActiveAlarmObjectName": nevtActiveAlarmObjectName,
       "nevtActiveAlarmAlarmType": nevtActiveAlarmAlarmType,
       "nevtActiveAlarmCause": nevtActiveAlarmCause,
       "nevtActiveAlarmSeverity": nevtActiveAlarmSeverity,
       "nevtActiveAlarmText": nevtActiveAlarmText,
       "nevtActiveAlarmLastChangedTime": nevtActiveAlarmLastChangedTime,
       "nevtActiveAlarmAcknowledged": nevtActiveAlarmAcknowledged,
       "nevtActiveAlarmCreatedTime": nevtActiveAlarmCreatedTime,
       "nevtActiveAlarmPurpose": nevtActiveAlarmPurpose,
       "nevtNotificationObjectsGroup": nevtNotificationObjectsGroup,
       "nevtTrapPurpose": nevtTrapPurpose,
       "nevtNotifications": nevtNotifications,
       "nevtAlarmCritical": nevtAlarmCritical,
       "nevtAlarmMajor": nevtAlarmMajor,
       "nevtAlarmMinor": nevtAlarmMinor,
       "nevtAlarmWarning": nevtAlarmWarning,
       "nevtAlarmIndeterminate": nevtAlarmIndeterminate,
       "nevtAlarmUnknown": nevtAlarmUnknown,
       "nevtAlarmClear": nevtAlarmClear,
       "nevtGenericEvent": nevtGenericEvent,
       "nevtConformanceGroups": nevtConformanceGroups}
)
