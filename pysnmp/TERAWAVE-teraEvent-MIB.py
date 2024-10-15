# SNMP MIB module (TERAWAVE-teraEvent-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERAWAVE-teraEvent-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:16 2024
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Terawave_ObjectIdentity = ObjectIdentity
terawave = _Terawave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513)
)
_Teratraps_ObjectIdentity = ObjectIdentity
teratraps = _Teratraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 1)
)
_TeraAlarms_ObjectIdentity = ObjectIdentity
teraAlarms = _TeraAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1)
)
_TeraLocalEventTable_Object = MibTable
teraLocalEventTable = _TeraLocalEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11)
)
if mibBuilder.loadTexts:
    teraLocalEventTable.setStatus("mandatory")
_TeraLocalEventTableEntry_Object = MibTableRow
teraLocalEventTableEntry = _TeraLocalEventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1)
)
teraLocalEventTableEntry.setIndexNames(
    (0, "TERAWAVE-teraEvent-MIB", "teraLocalEventIndex"),
)
if mibBuilder.loadTexts:
    teraLocalEventTableEntry.setStatus("mandatory")


class _TeraLocalEventIndex_Type(Counter32):
    """Custom type teraLocalEventIndex based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLocalEventIndex_Type.__name__ = "Counter32"
_TeraLocalEventIndex_Object = MibTableColumn
teraLocalEventIndex = _TeraLocalEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 1),
    _TeraLocalEventIndex_Type()
)
teraLocalEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventIndex.setStatus("mandatory")
_TeraLocalEventPort_Type = Integer32
_TeraLocalEventPort_Object = MibTableColumn
teraLocalEventPort = _TeraLocalEventPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 2),
    _TeraLocalEventPort_Type()
)
teraLocalEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventPort.setStatus("mandatory")
_TeraLocalEventPortType_Type = Integer32
_TeraLocalEventPortType_Object = MibTableColumn
teraLocalEventPortType = _TeraLocalEventPortType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 3),
    _TeraLocalEventPortType_Type()
)
teraLocalEventPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventPortType.setStatus("mandatory")
_TeraLocalEventCardType_Type = Integer32
_TeraLocalEventCardType_Object = MibTableColumn
teraLocalEventCardType = _TeraLocalEventCardType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 4),
    _TeraLocalEventCardType_Type()
)
teraLocalEventCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventCardType.setStatus("mandatory")
_TeraLocalEventSlot_Type = Integer32
_TeraLocalEventSlot_Object = MibTableColumn
teraLocalEventSlot = _TeraLocalEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 5),
    _TeraLocalEventSlot_Type()
)
teraLocalEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventSlot.setStatus("mandatory")
_TeraLocalEventPhysPort_Type = Integer32
_TeraLocalEventPhysPort_Object = MibTableColumn
teraLocalEventPhysPort = _TeraLocalEventPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 6),
    _TeraLocalEventPhysPort_Type()
)
teraLocalEventPhysPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventPhysPort.setStatus("mandatory")
_TeraLocalEventType_Type = Integer32
_TeraLocalEventType_Object = MibTableColumn
teraLocalEventType = _TeraLocalEventType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 7),
    _TeraLocalEventType_Type()
)
teraLocalEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventType.setStatus("mandatory")


class _TeraLocalEventSeverity_Type(Integer32):
    """Custom type teraLocalEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("informational", 2),
          ("major", 4),
          ("minor", 3),
          ("nominal", 1))
    )


_TeraLocalEventSeverity_Type.__name__ = "Integer32"
_TeraLocalEventSeverity_Object = MibTableColumn
teraLocalEventSeverity = _TeraLocalEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 8),
    _TeraLocalEventSeverity_Type()
)
teraLocalEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventSeverity.setStatus("mandatory")
_TeraLocalEventTime_Type = OctetString
_TeraLocalEventTime_Object = MibTableColumn
teraLocalEventTime = _TeraLocalEventTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 9),
    _TeraLocalEventTime_Type()
)
teraLocalEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventTime.setStatus("mandatory")
_TeraLocalEventMessage_Type = OctetString
_TeraLocalEventMessage_Object = MibTableColumn
teraLocalEventMessage = _TeraLocalEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 10),
    _TeraLocalEventMessage_Type()
)
teraLocalEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventMessage.setStatus("mandatory")
_TeraLocalEventTimeInSecs_Type = Integer32
_TeraLocalEventTimeInSecs_Object = MibTableColumn
teraLocalEventTimeInSecs = _TeraLocalEventTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 11, 1, 11),
    _TeraLocalEventTimeInSecs_Type()
)
teraLocalEventTimeInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalEventTimeInSecs.setStatus("mandatory")
_TeraLocalRmonEventTable_Object = MibTable
teraLocalRmonEventTable = _TeraLocalRmonEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12)
)
if mibBuilder.loadTexts:
    teraLocalRmonEventTable.setStatus("mandatory")
_TeraLocalRmonEventTableEntry_Object = MibTableRow
teraLocalRmonEventTableEntry = _TeraLocalRmonEventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1)
)
teraLocalRmonEventTableEntry.setIndexNames(
    (0, "TERAWAVE-teraEvent-MIB", "teraLocalRmonEventIndex"),
)
if mibBuilder.loadTexts:
    teraLocalRmonEventTableEntry.setStatus("mandatory")


class _TeraLocalRmonEventIndex_Type(Counter32):
    """Custom type teraLocalRmonEventIndex based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLocalRmonEventIndex_Type.__name__ = "Counter32"
_TeraLocalRmonEventIndex_Object = MibTableColumn
teraLocalRmonEventIndex = _TeraLocalRmonEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1, 1),
    _TeraLocalRmonEventIndex_Type()
)
teraLocalRmonEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalRmonEventIndex.setStatus("mandatory")
_TeraLocalRmonEventAlarmIndex_Type = Counter32
_TeraLocalRmonEventAlarmIndex_Object = MibTableColumn
teraLocalRmonEventAlarmIndex = _TeraLocalRmonEventAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1, 2),
    _TeraLocalRmonEventAlarmIndex_Type()
)
teraLocalRmonEventAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalRmonEventAlarmIndex.setStatus("mandatory")


class _TeraLocalRmonEventTrapType_Type(Integer32):
    """Custom type teraLocalRmonEventTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("falling", 2),
          ("rising", 1))
    )


_TeraLocalRmonEventTrapType_Type.__name__ = "Integer32"
_TeraLocalRmonEventTrapType_Object = MibTableColumn
teraLocalRmonEventTrapType = _TeraLocalRmonEventTrapType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1, 3),
    _TeraLocalRmonEventTrapType_Type()
)
teraLocalRmonEventTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalRmonEventTrapType.setStatus("mandatory")
_TeraLocalRmonEventSampleValue_Type = Integer32
_TeraLocalRmonEventSampleValue_Object = MibTableColumn
teraLocalRmonEventSampleValue = _TeraLocalRmonEventSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1, 4),
    _TeraLocalRmonEventSampleValue_Type()
)
teraLocalRmonEventSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalRmonEventSampleValue.setStatus("mandatory")
_TeraLocalRmonEventSampeThreshold_Type = Integer32
_TeraLocalRmonEventSampeThreshold_Object = MibTableColumn
teraLocalRmonEventSampeThreshold = _TeraLocalRmonEventSampeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1, 5),
    _TeraLocalRmonEventSampeThreshold_Type()
)
teraLocalRmonEventSampeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalRmonEventSampeThreshold.setStatus("mandatory")
_TeraLocalRmonEventTime_Type = OctetString
_TeraLocalRmonEventTime_Object = MibTableColumn
teraLocalRmonEventTime = _TeraLocalRmonEventTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1, 6),
    _TeraLocalRmonEventTime_Type()
)
teraLocalRmonEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalRmonEventTime.setStatus("mandatory")
_TeraLocalRmonEventTimeInSecs_Type = Integer32
_TeraLocalRmonEventTimeInSecs_Object = MibTableColumn
teraLocalRmonEventTimeInSecs = _TeraLocalRmonEventTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 12, 1, 7),
    _TeraLocalRmonEventTimeInSecs_Type()
)
teraLocalRmonEventTimeInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalRmonEventTimeInSecs.setStatus("mandatory")
_TeraLocalTcaEventTable_Object = MibTable
teraLocalTcaEventTable = _TeraLocalTcaEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13)
)
if mibBuilder.loadTexts:
    teraLocalTcaEventTable.setStatus("mandatory")
_TeraLocalTcaEventTableEntry_Object = MibTableRow
teraLocalTcaEventTableEntry = _TeraLocalTcaEventTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1)
)
teraLocalTcaEventTableEntry.setIndexNames(
    (0, "TERAWAVE-teraEvent-MIB", "teraLocalTcaEventIndex"),
)
if mibBuilder.loadTexts:
    teraLocalTcaEventTableEntry.setStatus("mandatory")


class _TeraLocalTcaEventIndex_Type(Counter32):
    """Custom type teraLocalTcaEventIndex based on Counter32"""
    subtypeSpec = Counter32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TeraLocalTcaEventIndex_Type.__name__ = "Counter32"
_TeraLocalTcaEventIndex_Object = MibTableColumn
teraLocalTcaEventIndex = _TeraLocalTcaEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1, 1),
    _TeraLocalTcaEventIndex_Type()
)
teraLocalTcaEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalTcaEventIndex.setStatus("mandatory")
_TeraLocalTcaEventAlarmIndex_Type = Counter32
_TeraLocalTcaEventAlarmIndex_Object = MibTableColumn
teraLocalTcaEventAlarmIndex = _TeraLocalTcaEventAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1, 2),
    _TeraLocalTcaEventAlarmIndex_Type()
)
teraLocalTcaEventAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalTcaEventAlarmIndex.setStatus("mandatory")


class _TeraLocalTcaEventTrapType_Type(Integer32):
    """Custom type teraLocalTcaEventTrapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("falling", 2),
          ("rising", 1))
    )


_TeraLocalTcaEventTrapType_Type.__name__ = "Integer32"
_TeraLocalTcaEventTrapType_Object = MibTableColumn
teraLocalTcaEventTrapType = _TeraLocalTcaEventTrapType_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1, 3),
    _TeraLocalTcaEventTrapType_Type()
)
teraLocalTcaEventTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalTcaEventTrapType.setStatus("mandatory")
_TeraLocalTcaEventSampleValue_Type = Integer32
_TeraLocalTcaEventSampleValue_Object = MibTableColumn
teraLocalTcaEventSampleValue = _TeraLocalTcaEventSampleValue_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1, 4),
    _TeraLocalTcaEventSampleValue_Type()
)
teraLocalTcaEventSampleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalTcaEventSampleValue.setStatus("mandatory")
_TeraLocalTcaEventSampeThreshold_Type = Integer32
_TeraLocalTcaEventSampeThreshold_Object = MibTableColumn
teraLocalTcaEventSampeThreshold = _TeraLocalTcaEventSampeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1, 5),
    _TeraLocalTcaEventSampeThreshold_Type()
)
teraLocalTcaEventSampeThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalTcaEventSampeThreshold.setStatus("mandatory")
_TeraLocalTcaEventTime_Type = OctetString
_TeraLocalTcaEventTime_Object = MibTableColumn
teraLocalTcaEventTime = _TeraLocalTcaEventTime_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1, 6),
    _TeraLocalTcaEventTime_Type()
)
teraLocalTcaEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalTcaEventTime.setStatus("mandatory")
_TeraLocalTcaEventTimeInSecs_Type = Integer32
_TeraLocalTcaEventTimeInSecs_Object = MibTableColumn
teraLocalTcaEventTimeInSecs = _TeraLocalTcaEventTimeInSecs_Object(
    (1, 3, 6, 1, 4, 1, 4513, 1, 1, 13, 1, 7),
    _TeraLocalTcaEventTimeInSecs_Type()
)
teraLocalTcaEventTimeInSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teraLocalTcaEventTimeInSecs.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERAWAVE-teraEvent-MIB",
    **{"terawave": terawave,
       "teratraps": teratraps,
       "teraAlarms": teraAlarms,
       "teraLocalEventTable": teraLocalEventTable,
       "teraLocalEventTableEntry": teraLocalEventTableEntry,
       "teraLocalEventIndex": teraLocalEventIndex,
       "teraLocalEventPort": teraLocalEventPort,
       "teraLocalEventPortType": teraLocalEventPortType,
       "teraLocalEventCardType": teraLocalEventCardType,
       "teraLocalEventSlot": teraLocalEventSlot,
       "teraLocalEventPhysPort": teraLocalEventPhysPort,
       "teraLocalEventType": teraLocalEventType,
       "teraLocalEventSeverity": teraLocalEventSeverity,
       "teraLocalEventTime": teraLocalEventTime,
       "teraLocalEventMessage": teraLocalEventMessage,
       "teraLocalEventTimeInSecs": teraLocalEventTimeInSecs,
       "teraLocalRmonEventTable": teraLocalRmonEventTable,
       "teraLocalRmonEventTableEntry": teraLocalRmonEventTableEntry,
       "teraLocalRmonEventIndex": teraLocalRmonEventIndex,
       "teraLocalRmonEventAlarmIndex": teraLocalRmonEventAlarmIndex,
       "teraLocalRmonEventTrapType": teraLocalRmonEventTrapType,
       "teraLocalRmonEventSampleValue": teraLocalRmonEventSampleValue,
       "teraLocalRmonEventSampeThreshold": teraLocalRmonEventSampeThreshold,
       "teraLocalRmonEventTime": teraLocalRmonEventTime,
       "teraLocalRmonEventTimeInSecs": teraLocalRmonEventTimeInSecs,
       "teraLocalTcaEventTable": teraLocalTcaEventTable,
       "teraLocalTcaEventTableEntry": teraLocalTcaEventTableEntry,
       "teraLocalTcaEventIndex": teraLocalTcaEventIndex,
       "teraLocalTcaEventAlarmIndex": teraLocalTcaEventAlarmIndex,
       "teraLocalTcaEventTrapType": teraLocalTcaEventTrapType,
       "teraLocalTcaEventSampleValue": teraLocalTcaEventSampleValue,
       "teraLocalTcaEventSampeThreshold": teraLocalTcaEventSampeThreshold,
       "teraLocalTcaEventTime": teraLocalTcaEventTime,
       "teraLocalTcaEventTimeInSecs": teraLocalTcaEventTimeInSecs}
)
