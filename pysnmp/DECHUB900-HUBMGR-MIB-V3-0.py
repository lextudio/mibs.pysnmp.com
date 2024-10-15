# SNMP MIB module (DECHUB900-HUBMGR-MIB-V3-0) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DECHUB900-HUBMGR-MIB-V3-0
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:41 2024
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
 NotificationType,
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
    "NotificationType",
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

_Dec_ObjectIdentity = ObjectIdentity
dec = _Dec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36)
)
_Ema_ObjectIdentity = ObjectIdentity
ema = _Ema_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2)
)
_DecMIBextension_ObjectIdentity = ObjectIdentity
decMIBextension = _DecMIBextension_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18)
)
_DecHub900_ObjectIdentity = ObjectIdentity
decHub900 = _DecHub900_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11)
)
_MgmtAgent_ObjectIdentity = ObjectIdentity
mgmtAgent = _MgmtAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1)
)
_MgmtAgentVersion2_ObjectIdentity = ObjectIdentity
mgmtAgentVersion2 = _MgmtAgentVersion2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2)
)
_MamPrivate_ObjectIdentity = ObjectIdentity
mamPrivate = _MamPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1)
)
_EventLogger_ObjectIdentity = ObjectIdentity
eventLogger = _EventLogger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1)
)
_EventLogTotalEvents_Type = Counter32
_EventLogTotalEvents_Object = MibScalar
eventLogTotalEvents = _EventLogTotalEvents_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1, 1),
    _EventLogTotalEvents_Type()
)
eventLogTotalEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTotalEvents.setStatus("mandatory")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("mandatory")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1, 2, 1)
)
eventLogEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("mandatory")


class _EventLogIndex_Type(Integer32):
    """Custom type eventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_EventLogIndex_Type.__name__ = "Integer32"
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1, 2, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("mandatory")


class _EventLogSlot_Type(Integer32):
    """Custom type eventLogSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventLogSlot_Type.__name__ = "Integer32"
_EventLogSlot_Object = MibTableColumn
eventLogSlot = _EventLogSlot_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1, 2, 1, 2),
    _EventLogSlot_Type()
)
eventLogSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSlot.setStatus("mandatory")
_EventLogTimeStamp_Type = TimeTicks
_EventLogTimeStamp_Object = MibTableColumn
eventLogTimeStamp = _EventLogTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1, 2, 1, 3),
    _EventLogTimeStamp_Type()
)
eventLogTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTimeStamp.setStatus("mandatory")


class _EventLogDescription_Type(OctetString):
    """Custom type eventLogDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_EventLogDescription_Type.__name__ = "OctetString"
_EventLogDescription_Object = MibTableColumn
eventLogDescription = _EventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 1, 2, 1, 4),
    _EventLogDescription_Type()
)
eventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDescription.setStatus("mandatory")
_RmonHub_ObjectIdentity = ObjectIdentity
rmonHub = _RmonHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2)
)
_HubAlarm_ObjectIdentity = ObjectIdentity
hubAlarm = _HubAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1)
)
_HubAlarmTable_Object = MibTable
hubAlarmTable = _HubAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hubAlarmTable.setStatus("mandatory")
_HubAlarmEntry_Object = MibTableRow
hubAlarmEntry = _HubAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1)
)
hubAlarmEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmSlotNumber"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmIndex"),
)
if mibBuilder.loadTexts:
    hubAlarmEntry.setStatus("mandatory")


class _HubAlarmSlotNumber_Type(Integer32):
    """Custom type hubAlarmSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HubAlarmSlotNumber_Type.__name__ = "Integer32"
_HubAlarmSlotNumber_Object = MibTableColumn
hubAlarmSlotNumber = _HubAlarmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 1),
    _HubAlarmSlotNumber_Type()
)
hubAlarmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAlarmSlotNumber.setStatus("mandatory")


class _HubAlarmIndex_Type(Integer32):
    """Custom type hubAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubAlarmIndex_Type.__name__ = "Integer32"
_HubAlarmIndex_Object = MibTableColumn
hubAlarmIndex = _HubAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 2),
    _HubAlarmIndex_Type()
)
hubAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAlarmIndex.setStatus("mandatory")


class _HubAlarmInterval_Type(Integer32):
    """Custom type hubAlarmInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 21474835),
    )


_HubAlarmInterval_Type.__name__ = "Integer32"
_HubAlarmInterval_Object = MibTableColumn
hubAlarmInterval = _HubAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 3),
    _HubAlarmInterval_Type()
)
hubAlarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmInterval.setStatus("mandatory")
_HubAlarmVariable_Type = ObjectIdentifier
_HubAlarmVariable_Object = MibTableColumn
hubAlarmVariable = _HubAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 4),
    _HubAlarmVariable_Type()
)
hubAlarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmVariable.setStatus("mandatory")


class _HubAlarmSampleType_Type(Integer32):
    """Custom type hubAlarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("deltaValue", 2))
    )


_HubAlarmSampleType_Type.__name__ = "Integer32"
_HubAlarmSampleType_Object = MibTableColumn
hubAlarmSampleType = _HubAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 5),
    _HubAlarmSampleType_Type()
)
hubAlarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmSampleType.setStatus("mandatory")


class _HubAlarmValue_Type(Integer32):
    """Custom type hubAlarmValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HubAlarmValue_Type.__name__ = "Integer32"
_HubAlarmValue_Object = MibTableColumn
hubAlarmValue = _HubAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 6),
    _HubAlarmValue_Type()
)
hubAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAlarmValue.setStatus("mandatory")


class _HubAlarmStartupAlarm_Type(Integer32):
    """Custom type hubAlarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_HubAlarmStartupAlarm_Type.__name__ = "Integer32"
_HubAlarmStartupAlarm_Object = MibTableColumn
hubAlarmStartupAlarm = _HubAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 7),
    _HubAlarmStartupAlarm_Type()
)
hubAlarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmStartupAlarm.setStatus("mandatory")


class _HubAlarmRisingThreshold_Type(Integer32):
    """Custom type hubAlarmRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HubAlarmRisingThreshold_Type.__name__ = "Integer32"
_HubAlarmRisingThreshold_Object = MibTableColumn
hubAlarmRisingThreshold = _HubAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 8),
    _HubAlarmRisingThreshold_Type()
)
hubAlarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmRisingThreshold.setStatus("mandatory")


class _HubAlarmFallingThreshold_Type(Integer32):
    """Custom type hubAlarmFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HubAlarmFallingThreshold_Type.__name__ = "Integer32"
_HubAlarmFallingThreshold_Object = MibTableColumn
hubAlarmFallingThreshold = _HubAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 9),
    _HubAlarmFallingThreshold_Type()
)
hubAlarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmFallingThreshold.setStatus("mandatory")


class _HubAlarmRisingEventIndex_Type(Integer32):
    """Custom type hubAlarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HubAlarmRisingEventIndex_Type.__name__ = "Integer32"
_HubAlarmRisingEventIndex_Object = MibTableColumn
hubAlarmRisingEventIndex = _HubAlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 10),
    _HubAlarmRisingEventIndex_Type()
)
hubAlarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmRisingEventIndex.setStatus("mandatory")


class _HubAlarmFallingEventIndex_Type(Integer32):
    """Custom type hubAlarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HubAlarmFallingEventIndex_Type.__name__ = "Integer32"
_HubAlarmFallingEventIndex_Object = MibTableColumn
hubAlarmFallingEventIndex = _HubAlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 11),
    _HubAlarmFallingEventIndex_Type()
)
hubAlarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmFallingEventIndex.setStatus("mandatory")


class _HubAlarmOwner_Type(DisplayString):
    """Custom type hubAlarmOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HubAlarmOwner_Type.__name__ = "DisplayString"
_HubAlarmOwner_Object = MibTableColumn
hubAlarmOwner = _HubAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 12),
    _HubAlarmOwner_Type()
)
hubAlarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmOwner.setStatus("mandatory")


class _HubAlarmState_Type(Integer32):
    """Custom type hubAlarmState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HubAlarmState_Type.__name__ = "Integer32"
_HubAlarmState_Object = MibTableColumn
hubAlarmState = _HubAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 13),
    _HubAlarmState_Type()
)
hubAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubAlarmState.setStatus("mandatory")


class _HubAlarmStatus_Type(Integer32):
    """Custom type hubAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_HubAlarmStatus_Type.__name__ = "Integer32"
_HubAlarmStatus_Object = MibTableColumn
hubAlarmStatus = _HubAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 1, 1, 1, 14),
    _HubAlarmStatus_Type()
)
hubAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubAlarmStatus.setStatus("mandatory")
_HubEvent_ObjectIdentity = ObjectIdentity
hubEvent = _HubEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2)
)
_HubEventTable_Object = MibTable
hubEventTable = _HubEventTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hubEventTable.setStatus("mandatory")
_HubEventEntry_Object = MibTableRow
hubEventEntry = _HubEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1)
)
hubEventEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubEventIndex"),
)
if mibBuilder.loadTexts:
    hubEventEntry.setStatus("mandatory")


class _HubEventIndex_Type(Integer32):
    """Custom type hubEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubEventIndex_Type.__name__ = "Integer32"
_HubEventIndex_Object = MibTableColumn
hubEventIndex = _HubEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1, 1),
    _HubEventIndex_Type()
)
hubEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEventIndex.setStatus("mandatory")


class _HubEventDescription_Type(DisplayString):
    """Custom type hubEventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HubEventDescription_Type.__name__ = "DisplayString"
_HubEventDescription_Object = MibTableColumn
hubEventDescription = _HubEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1, 2),
    _HubEventDescription_Type()
)
hubEventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubEventDescription.setStatus("mandatory")


class _HubEventType_Type(Integer32):
    """Custom type hubEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("log", 2),
          ("log-and-trap", 4),
          ("none", 1),
          ("snmp-trap", 3))
    )


_HubEventType_Type.__name__ = "Integer32"
_HubEventType_Object = MibTableColumn
hubEventType = _HubEventType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1, 3),
    _HubEventType_Type()
)
hubEventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubEventType.setStatus("mandatory")


class _HubEventCommunity_Type(OctetString):
    """Custom type hubEventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HubEventCommunity_Type.__name__ = "OctetString"
_HubEventCommunity_Object = MibTableColumn
hubEventCommunity = _HubEventCommunity_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1, 4),
    _HubEventCommunity_Type()
)
hubEventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubEventCommunity.setStatus("mandatory")
_HubEventLastTimeSent_Type = TimeTicks
_HubEventLastTimeSent_Object = MibTableColumn
hubEventLastTimeSent = _HubEventLastTimeSent_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1, 5),
    _HubEventLastTimeSent_Type()
)
hubEventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEventLastTimeSent.setStatus("mandatory")


class _HubEventOwner_Type(DisplayString):
    """Custom type hubEventOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HubEventOwner_Type.__name__ = "DisplayString"
_HubEventOwner_Object = MibTableColumn
hubEventOwner = _HubEventOwner_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1, 6),
    _HubEventOwner_Type()
)
hubEventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubEventOwner.setStatus("mandatory")


class _HubEventStatus_Type(Integer32):
    """Custom type hubEventStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("createRequest", 2),
          ("invalid", 4),
          ("underCreation", 3),
          ("valid", 1))
    )


_HubEventStatus_Type.__name__ = "Integer32"
_HubEventStatus_Object = MibTableColumn
hubEventStatus = _HubEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 1, 1, 7),
    _HubEventStatus_Type()
)
hubEventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubEventStatus.setStatus("mandatory")
_HubLogTable_Object = MibTable
hubLogTable = _HubLogTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hubLogTable.setStatus("mandatory")
_HubLogEntry_Object = MibTableRow
hubLogEntry = _HubLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 2, 1)
)
hubLogEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubLogSlotNumber"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubLogEventIndex"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubLogIndex"),
)
if mibBuilder.loadTexts:
    hubLogEntry.setStatus("mandatory")


class _HubLogSlotNumber_Type(Integer32):
    """Custom type hubLogSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubLogSlotNumber_Type.__name__ = "Integer32"
_HubLogSlotNumber_Object = MibTableColumn
hubLogSlotNumber = _HubLogSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 2, 1, 1),
    _HubLogSlotNumber_Type()
)
hubLogSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubLogSlotNumber.setStatus("mandatory")


class _HubLogEventIndex_Type(Integer32):
    """Custom type hubLogEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubLogEventIndex_Type.__name__ = "Integer32"
_HubLogEventIndex_Object = MibTableColumn
hubLogEventIndex = _HubLogEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 2, 1, 2),
    _HubLogEventIndex_Type()
)
hubLogEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubLogEventIndex.setStatus("mandatory")


class _HubLogIndex_Type(Integer32):
    """Custom type hubLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HubLogIndex_Type.__name__ = "Integer32"
_HubLogIndex_Object = MibTableColumn
hubLogIndex = _HubLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 2, 1, 3),
    _HubLogIndex_Type()
)
hubLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubLogIndex.setStatus("mandatory")
_HubLogTime_Type = TimeTicks
_HubLogTime_Object = MibTableColumn
hubLogTime = _HubLogTime_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 2, 1, 4),
    _HubLogTime_Type()
)
hubLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubLogTime.setStatus("mandatory")


class _HubLogDescription_Type(DisplayString):
    """Custom type hubLogDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HubLogDescription_Type.__name__ = "DisplayString"
_HubLogDescription_Object = MibTableColumn
hubLogDescription = _HubLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 2, 2, 1, 5),
    _HubLogDescription_Type()
)
hubLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubLogDescription.setStatus("mandatory")
_HubEtherCapabilities_ObjectIdentity = ObjectIdentity
hubEtherCapabilities = _HubEtherCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3)
)
_HubEtherCapabilitiesTable_Object = MibTable
hubEtherCapabilitiesTable = _HubEtherCapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hubEtherCapabilitiesTable.setStatus("mandatory")
_HubEtherCapabilitiesEntry_Object = MibTableRow
hubEtherCapabilitiesEntry = _HubEtherCapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1, 1)
)
hubEtherCapabilitiesEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubEtherCapabilitiesSlotNumber"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubEtherCapabilitiesIndex"),
)
if mibBuilder.loadTexts:
    hubEtherCapabilitiesEntry.setStatus("mandatory")


class _HubEtherCapabilitiesSlotNumber_Type(Integer32):
    """Custom type hubEtherCapabilitiesSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HubEtherCapabilitiesSlotNumber_Type.__name__ = "Integer32"
_HubEtherCapabilitiesSlotNumber_Object = MibTableColumn
hubEtherCapabilitiesSlotNumber = _HubEtherCapabilitiesSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1, 1, 1),
    _HubEtherCapabilitiesSlotNumber_Type()
)
hubEtherCapabilitiesSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherCapabilitiesSlotNumber.setStatus("mandatory")


class _HubEtherCapabilitiesIndex_Type(Integer32):
    """Custom type hubEtherCapabilitiesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubEtherCapabilitiesIndex_Type.__name__ = "Integer32"
_HubEtherCapabilitiesIndex_Object = MibTableColumn
hubEtherCapabilitiesIndex = _HubEtherCapabilitiesIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1, 1, 2),
    _HubEtherCapabilitiesIndex_Type()
)
hubEtherCapabilitiesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherCapabilitiesIndex.setStatus("mandatory")


class _HubEtherCapabilitiesLanType_Type(Integer32):
    """Custom type hubEtherCapabilitiesLanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("port", 3),
          ("portGroup", 2))
    )


_HubEtherCapabilitiesLanType_Type.__name__ = "Integer32"
_HubEtherCapabilitiesLanType_Object = MibTableColumn
hubEtherCapabilitiesLanType = _HubEtherCapabilitiesLanType_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1, 1, 3),
    _HubEtherCapabilitiesLanType_Type()
)
hubEtherCapabilitiesLanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherCapabilitiesLanType.setStatus("mandatory")


class _HubEtherCapabilitiesLanSpeed_Type(Integer32):
    """Custom type hubEtherCapabilitiesLanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HubEtherCapabilitiesLanSpeed_Type.__name__ = "Integer32"
_HubEtherCapabilitiesLanSpeed_Object = MibTableColumn
hubEtherCapabilitiesLanSpeed = _HubEtherCapabilitiesLanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1, 1, 4),
    _HubEtherCapabilitiesLanSpeed_Type()
)
hubEtherCapabilitiesLanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherCapabilitiesLanSpeed.setStatus("mandatory")


class _HubEtherCapabilitiesTrueCollisions_Type(Integer32):
    """Custom type hubEtherCapabilitiesTrueCollisions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HubEtherCapabilitiesTrueCollisions_Type.__name__ = "Integer32"
_HubEtherCapabilitiesTrueCollisions_Object = MibTableColumn
hubEtherCapabilitiesTrueCollisions = _HubEtherCapabilitiesTrueCollisions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1, 1, 5),
    _HubEtherCapabilitiesTrueCollisions_Type()
)
hubEtherCapabilitiesTrueCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherCapabilitiesTrueCollisions.setStatus("mandatory")


class _HubEtherCapabilitiesState_Type(Integer32):
    """Custom type hubEtherCapabilitiesState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HubEtherCapabilitiesState_Type.__name__ = "Integer32"
_HubEtherCapabilitiesState_Object = MibTableColumn
hubEtherCapabilitiesState = _HubEtherCapabilitiesState_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 3, 1, 1, 6),
    _HubEtherCapabilitiesState_Type()
)
hubEtherCapabilitiesState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubEtherCapabilitiesState.setStatus("mandatory")
_HubStatistics_ObjectIdentity = ObjectIdentity
hubStatistics = _HubStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4)
)
_HubEtherStatsTable_Object = MibTable
hubEtherStatsTable = _HubEtherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    hubEtherStatsTable.setStatus("mandatory")
_HubEtherStatsEntry_Object = MibTableRow
hubEtherStatsEntry = _HubEtherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1)
)
hubEtherStatsEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubEtherStatsSlotNumber"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubEtherStatsIndex"),
)
if mibBuilder.loadTexts:
    hubEtherStatsEntry.setStatus("mandatory")


class _HubEtherStatsSlotNumber_Type(Integer32):
    """Custom type hubEtherStatsSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubEtherStatsSlotNumber_Type.__name__ = "Integer32"
_HubEtherStatsSlotNumber_Object = MibTableColumn
hubEtherStatsSlotNumber = _HubEtherStatsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 1),
    _HubEtherStatsSlotNumber_Type()
)
hubEtherStatsSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsSlotNumber.setStatus("mandatory")


class _HubEtherStatsIndex_Type(Integer32):
    """Custom type hubEtherStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HubEtherStatsIndex_Type.__name__ = "Integer32"
_HubEtherStatsIndex_Object = MibTableColumn
hubEtherStatsIndex = _HubEtherStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 2),
    _HubEtherStatsIndex_Type()
)
hubEtherStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsIndex.setStatus("mandatory")
_HubEtherStatsDropEvents_Type = Counter32
_HubEtherStatsDropEvents_Object = MibTableColumn
hubEtherStatsDropEvents = _HubEtherStatsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 3),
    _HubEtherStatsDropEvents_Type()
)
hubEtherStatsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsDropEvents.setStatus("mandatory")
_HubEtherStatsOctets_Type = Counter32
_HubEtherStatsOctets_Object = MibTableColumn
hubEtherStatsOctets = _HubEtherStatsOctets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 4),
    _HubEtherStatsOctets_Type()
)
hubEtherStatsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsOctets.setStatus("mandatory")
_HubEtherStatsPkts_Type = Counter32
_HubEtherStatsPkts_Object = MibTableColumn
hubEtherStatsPkts = _HubEtherStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 5),
    _HubEtherStatsPkts_Type()
)
hubEtherStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsPkts.setStatus("mandatory")
_HubEtherStatsBroadcastPkts_Type = Counter32
_HubEtherStatsBroadcastPkts_Object = MibTableColumn
hubEtherStatsBroadcastPkts = _HubEtherStatsBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 6),
    _HubEtherStatsBroadcastPkts_Type()
)
hubEtherStatsBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsBroadcastPkts.setStatus("mandatory")
_HubEtherStatsMulticastPkts_Type = Counter32
_HubEtherStatsMulticastPkts_Object = MibTableColumn
hubEtherStatsMulticastPkts = _HubEtherStatsMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 7),
    _HubEtherStatsMulticastPkts_Type()
)
hubEtherStatsMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsMulticastPkts.setStatus("mandatory")
_HubEtherStatsCRCAlignErrors_Type = Counter32
_HubEtherStatsCRCAlignErrors_Object = MibTableColumn
hubEtherStatsCRCAlignErrors = _HubEtherStatsCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 8),
    _HubEtherStatsCRCAlignErrors_Type()
)
hubEtherStatsCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsCRCAlignErrors.setStatus("mandatory")
_HubEtherStatsUndersizePkts_Type = Counter32
_HubEtherStatsUndersizePkts_Object = MibTableColumn
hubEtherStatsUndersizePkts = _HubEtherStatsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 9),
    _HubEtherStatsUndersizePkts_Type()
)
hubEtherStatsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsUndersizePkts.setStatus("mandatory")
_HubEtherStatsOversizePkts_Type = Counter32
_HubEtherStatsOversizePkts_Object = MibTableColumn
hubEtherStatsOversizePkts = _HubEtherStatsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 10),
    _HubEtherStatsOversizePkts_Type()
)
hubEtherStatsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsOversizePkts.setStatus("mandatory")
_HubEtherStatsFragments_Type = Counter32
_HubEtherStatsFragments_Object = MibTableColumn
hubEtherStatsFragments = _HubEtherStatsFragments_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 11),
    _HubEtherStatsFragments_Type()
)
hubEtherStatsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsFragments.setStatus("mandatory")
_HubEtherStatsJabbers_Type = Counter32
_HubEtherStatsJabbers_Object = MibTableColumn
hubEtherStatsJabbers = _HubEtherStatsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 12),
    _HubEtherStatsJabbers_Type()
)
hubEtherStatsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsJabbers.setStatus("mandatory")
_HubEtherStatsCollisions_Type = Counter32
_HubEtherStatsCollisions_Object = MibTableColumn
hubEtherStatsCollisions = _HubEtherStatsCollisions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 13),
    _HubEtherStatsCollisions_Type()
)
hubEtherStatsCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsCollisions.setStatus("mandatory")
_HubEtherStatsPkts64Octets_Type = Counter32
_HubEtherStatsPkts64Octets_Object = MibTableColumn
hubEtherStatsPkts64Octets = _HubEtherStatsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 14),
    _HubEtherStatsPkts64Octets_Type()
)
hubEtherStatsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsPkts64Octets.setStatus("mandatory")
_HubEtherStatsPkts65to127Octets_Type = Counter32
_HubEtherStatsPkts65to127Octets_Object = MibTableColumn
hubEtherStatsPkts65to127Octets = _HubEtherStatsPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 15),
    _HubEtherStatsPkts65to127Octets_Type()
)
hubEtherStatsPkts65to127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsPkts65to127Octets.setStatus("mandatory")
_HubEtherStatsPkts128to255Octets_Type = Counter32
_HubEtherStatsPkts128to255Octets_Object = MibTableColumn
hubEtherStatsPkts128to255Octets = _HubEtherStatsPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 16),
    _HubEtherStatsPkts128to255Octets_Type()
)
hubEtherStatsPkts128to255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsPkts128to255Octets.setStatus("mandatory")
_HubEtherStatsPkts256to511Octets_Type = Counter32
_HubEtherStatsPkts256to511Octets_Object = MibTableColumn
hubEtherStatsPkts256to511Octets = _HubEtherStatsPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 17),
    _HubEtherStatsPkts256to511Octets_Type()
)
hubEtherStatsPkts256to511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsPkts256to511Octets.setStatus("mandatory")
_HubEtherStatsPkts512to1023Octets_Type = Counter32
_HubEtherStatsPkts512to1023Octets_Object = MibTableColumn
hubEtherStatsPkts512to1023Octets = _HubEtherStatsPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 18),
    _HubEtherStatsPkts512to1023Octets_Type()
)
hubEtherStatsPkts512to1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsPkts512to1023Octets.setStatus("mandatory")
_HubEtherStatsPkts1024to1518Octets_Type = Counter32
_HubEtherStatsPkts1024to1518Octets_Object = MibTableColumn
hubEtherStatsPkts1024to1518Octets = _HubEtherStatsPkts1024to1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 4, 1, 1, 19),
    _HubEtherStatsPkts1024to1518Octets_Type()
)
hubEtherStatsPkts1024to1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherStatsPkts1024to1518Octets.setStatus("mandatory")
_HubHistory_ObjectIdentity = ObjectIdentity
hubHistory = _HubHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5)
)


class _HubHistoryControlFastPollInterval_Type(Integer32):
    """Custom type hubHistoryControlFastPollInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_HubHistoryControlFastPollInterval_Type.__name__ = "Integer32"
_HubHistoryControlFastPollInterval_Object = MibScalar
hubHistoryControlFastPollInterval = _HubHistoryControlFastPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 1),
    _HubHistoryControlFastPollInterval_Type()
)
hubHistoryControlFastPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubHistoryControlFastPollInterval.setStatus("mandatory")


class _HubHistoryControlSlowPollInterval_Type(Integer32):
    """Custom type hubHistoryControlSlowPollInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_HubHistoryControlSlowPollInterval_Type.__name__ = "Integer32"
_HubHistoryControlSlowPollInterval_Object = MibScalar
hubHistoryControlSlowPollInterval = _HubHistoryControlSlowPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 2),
    _HubHistoryControlSlowPollInterval_Type()
)
hubHistoryControlSlowPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hubHistoryControlSlowPollInterval.setStatus("mandatory")
_HubHistoryControlTable_Object = MibTable
hubHistoryControlTable = _HubHistoryControlTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    hubHistoryControlTable.setStatus("mandatory")
_HubHistoryControlEntry_Object = MibTableRow
hubHistoryControlEntry = _HubHistoryControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 3, 1)
)
hubHistoryControlEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubHistoryControlSlotNumber"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubHistoryControlIndex"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubHistoryControlHistoryIndex"),
)
if mibBuilder.loadTexts:
    hubHistoryControlEntry.setStatus("mandatory")


class _HubHistoryControlSlotNumber_Type(Integer32):
    """Custom type hubHistoryControlSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubHistoryControlSlotNumber_Type.__name__ = "Integer32"
_HubHistoryControlSlotNumber_Object = MibTableColumn
hubHistoryControlSlotNumber = _HubHistoryControlSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 3, 1, 1),
    _HubHistoryControlSlotNumber_Type()
)
hubHistoryControlSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHistoryControlSlotNumber.setStatus("mandatory")


class _HubHistoryControlIndex_Type(Integer32):
    """Custom type hubHistoryControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubHistoryControlIndex_Type.__name__ = "Integer32"
_HubHistoryControlIndex_Object = MibTableColumn
hubHistoryControlIndex = _HubHistoryControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 3, 1, 2),
    _HubHistoryControlIndex_Type()
)
hubHistoryControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHistoryControlIndex.setStatus("mandatory")


class _HubHistoryControlHistoryIndex_Type(Integer32):
    """Custom type hubHistoryControlHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubHistoryControlHistoryIndex_Type.__name__ = "Integer32"
_HubHistoryControlHistoryIndex_Object = MibTableColumn
hubHistoryControlHistoryIndex = _HubHistoryControlHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 3, 1, 3),
    _HubHistoryControlHistoryIndex_Type()
)
hubHistoryControlHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHistoryControlHistoryIndex.setStatus("mandatory")


class _HubHistoryControlBuckets_Type(Integer32):
    """Custom type hubHistoryControlBuckets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubHistoryControlBuckets_Type.__name__ = "Integer32"
_HubHistoryControlBuckets_Object = MibTableColumn
hubHistoryControlBuckets = _HubHistoryControlBuckets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 3, 1, 4),
    _HubHistoryControlBuckets_Type()
)
hubHistoryControlBuckets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHistoryControlBuckets.setStatus("mandatory")


class _HubHistoryControlInterval_Type(Integer32):
    """Custom type hubHistoryControlInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_HubHistoryControlInterval_Type.__name__ = "Integer32"
_HubHistoryControlInterval_Object = MibTableColumn
hubHistoryControlInterval = _HubHistoryControlInterval_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 3, 1, 5),
    _HubHistoryControlInterval_Type()
)
hubHistoryControlInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubHistoryControlInterval.setStatus("mandatory")
_HubEtherHistoryTable_Object = MibTable
hubEtherHistoryTable = _HubEtherHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4)
)
if mibBuilder.loadTexts:
    hubEtherHistoryTable.setStatus("mandatory")
_HubEtherHistoryEntry_Object = MibTableRow
hubEtherHistoryEntry = _HubEtherHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1)
)
hubEtherHistoryEntry.setIndexNames(
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubEtherHistoryIndex"),
    (0, "DECHUB900-HUBMGR-MIB-V3-0", "hubEtherHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    hubEtherHistoryEntry.setStatus("mandatory")


class _HubEtherHistoryIndex_Type(Integer32):
    """Custom type hubEtherHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HubEtherHistoryIndex_Type.__name__ = "Integer32"
_HubEtherHistoryIndex_Object = MibTableColumn
hubEtherHistoryIndex = _HubEtherHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 1),
    _HubEtherHistoryIndex_Type()
)
hubEtherHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryIndex.setStatus("mandatory")


class _HubEtherHistorySampleIndex_Type(Integer32):
    """Custom type hubEtherHistorySampleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HubEtherHistorySampleIndex_Type.__name__ = "Integer32"
_HubEtherHistorySampleIndex_Object = MibTableColumn
hubEtherHistorySampleIndex = _HubEtherHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 2),
    _HubEtherHistorySampleIndex_Type()
)
hubEtherHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistorySampleIndex.setStatus("mandatory")
_HubEtherHistoryIntervalStart_Type = TimeTicks
_HubEtherHistoryIntervalStart_Object = MibTableColumn
hubEtherHistoryIntervalStart = _HubEtherHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 3),
    _HubEtherHistoryIntervalStart_Type()
)
hubEtherHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryIntervalStart.setStatus("mandatory")
_HubEtherHistoryDropEvents_Type = Counter32
_HubEtherHistoryDropEvents_Object = MibTableColumn
hubEtherHistoryDropEvents = _HubEtherHistoryDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 4),
    _HubEtherHistoryDropEvents_Type()
)
hubEtherHistoryDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryDropEvents.setStatus("mandatory")
_HubEtherHistoryOctets_Type = Counter32
_HubEtherHistoryOctets_Object = MibTableColumn
hubEtherHistoryOctets = _HubEtherHistoryOctets_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 5),
    _HubEtherHistoryOctets_Type()
)
hubEtherHistoryOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryOctets.setStatus("mandatory")
_HubEtherHistoryPkts_Type = Counter32
_HubEtherHistoryPkts_Object = MibTableColumn
hubEtherHistoryPkts = _HubEtherHistoryPkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 6),
    _HubEtherHistoryPkts_Type()
)
hubEtherHistoryPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryPkts.setStatus("mandatory")
_HubEtherHistoryBroadcastPkts_Type = Counter32
_HubEtherHistoryBroadcastPkts_Object = MibTableColumn
hubEtherHistoryBroadcastPkts = _HubEtherHistoryBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 7),
    _HubEtherHistoryBroadcastPkts_Type()
)
hubEtherHistoryBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryBroadcastPkts.setStatus("mandatory")
_HubEtherHistoryMulticastPkts_Type = Counter32
_HubEtherHistoryMulticastPkts_Object = MibTableColumn
hubEtherHistoryMulticastPkts = _HubEtherHistoryMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 8),
    _HubEtherHistoryMulticastPkts_Type()
)
hubEtherHistoryMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryMulticastPkts.setStatus("mandatory")
_HubEtherHistoryCRCAlignErrors_Type = Counter32
_HubEtherHistoryCRCAlignErrors_Object = MibTableColumn
hubEtherHistoryCRCAlignErrors = _HubEtherHistoryCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 9),
    _HubEtherHistoryCRCAlignErrors_Type()
)
hubEtherHistoryCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryCRCAlignErrors.setStatus("mandatory")
_HubEtherHistoryUndersizePkts_Type = Counter32
_HubEtherHistoryUndersizePkts_Object = MibTableColumn
hubEtherHistoryUndersizePkts = _HubEtherHistoryUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 10),
    _HubEtherHistoryUndersizePkts_Type()
)
hubEtherHistoryUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryUndersizePkts.setStatus("mandatory")
_HubEtherHistoryOversizePkts_Type = Counter32
_HubEtherHistoryOversizePkts_Object = MibTableColumn
hubEtherHistoryOversizePkts = _HubEtherHistoryOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 11),
    _HubEtherHistoryOversizePkts_Type()
)
hubEtherHistoryOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryOversizePkts.setStatus("mandatory")
_HubEtherHistoryFragments_Type = Counter32
_HubEtherHistoryFragments_Object = MibTableColumn
hubEtherHistoryFragments = _HubEtherHistoryFragments_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 12),
    _HubEtherHistoryFragments_Type()
)
hubEtherHistoryFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryFragments.setStatus("mandatory")
_HubEtherHistoryJabbers_Type = Counter32
_HubEtherHistoryJabbers_Object = MibTableColumn
hubEtherHistoryJabbers = _HubEtherHistoryJabbers_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 13),
    _HubEtherHistoryJabbers_Type()
)
hubEtherHistoryJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryJabbers.setStatus("mandatory")
_HubEtherHistoryCollisions_Type = Counter32
_HubEtherHistoryCollisions_Object = MibTableColumn
hubEtherHistoryCollisions = _HubEtherHistoryCollisions_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 14),
    _HubEtherHistoryCollisions_Type()
)
hubEtherHistoryCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryCollisions.setStatus("mandatory")


class _HubEtherHistoryUtilization_Type(Integer32):
    """Custom type hubEtherHistoryUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HubEtherHistoryUtilization_Type.__name__ = "Integer32"
_HubEtherHistoryUtilization_Object = MibTableColumn
hubEtherHistoryUtilization = _HubEtherHistoryUtilization_Object(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 2, 5, 4, 1, 15),
    _HubEtherHistoryUtilization_Type()
)
hubEtherHistoryUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hubEtherHistoryUtilization.setStatus("mandatory")

# Managed Objects groups


# Notification objects

hubRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 0, 1)
)
hubRisingAlarm.setObjects(
      *(("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmSlotNumber"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmIndex"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmVariable"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmSampleType"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmValue"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    hubRisingAlarm.setStatus(
        ""
    )

hubFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 36, 2, 18, 11, 1, 2, 1, 0, 2)
)
hubFallingAlarm.setObjects(
      *(("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmSlotNumber"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmIndex"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmVariable"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmSampleType"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmValue"),
        ("DECHUB900-HUBMGR-MIB-V3-0", "hubAlarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    hubFallingAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DECHUB900-HUBMGR-MIB-V3-0",
    **{"dec": dec,
       "ema": ema,
       "decMIBextension": decMIBextension,
       "decHub900": decHub900,
       "mgmtAgent": mgmtAgent,
       "mgmtAgentVersion2": mgmtAgentVersion2,
       "mamPrivate": mamPrivate,
       "hubRisingAlarm": hubRisingAlarm,
       "hubFallingAlarm": hubFallingAlarm,
       "eventLogger": eventLogger,
       "eventLogTotalEvents": eventLogTotalEvents,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogSlot": eventLogSlot,
       "eventLogTimeStamp": eventLogTimeStamp,
       "eventLogDescription": eventLogDescription,
       "rmonHub": rmonHub,
       "hubAlarm": hubAlarm,
       "hubAlarmTable": hubAlarmTable,
       "hubAlarmEntry": hubAlarmEntry,
       "hubAlarmSlotNumber": hubAlarmSlotNumber,
       "hubAlarmIndex": hubAlarmIndex,
       "hubAlarmInterval": hubAlarmInterval,
       "hubAlarmVariable": hubAlarmVariable,
       "hubAlarmSampleType": hubAlarmSampleType,
       "hubAlarmValue": hubAlarmValue,
       "hubAlarmStartupAlarm": hubAlarmStartupAlarm,
       "hubAlarmRisingThreshold": hubAlarmRisingThreshold,
       "hubAlarmFallingThreshold": hubAlarmFallingThreshold,
       "hubAlarmRisingEventIndex": hubAlarmRisingEventIndex,
       "hubAlarmFallingEventIndex": hubAlarmFallingEventIndex,
       "hubAlarmOwner": hubAlarmOwner,
       "hubAlarmState": hubAlarmState,
       "hubAlarmStatus": hubAlarmStatus,
       "hubEvent": hubEvent,
       "hubEventTable": hubEventTable,
       "hubEventEntry": hubEventEntry,
       "hubEventIndex": hubEventIndex,
       "hubEventDescription": hubEventDescription,
       "hubEventType": hubEventType,
       "hubEventCommunity": hubEventCommunity,
       "hubEventLastTimeSent": hubEventLastTimeSent,
       "hubEventOwner": hubEventOwner,
       "hubEventStatus": hubEventStatus,
       "hubLogTable": hubLogTable,
       "hubLogEntry": hubLogEntry,
       "hubLogSlotNumber": hubLogSlotNumber,
       "hubLogEventIndex": hubLogEventIndex,
       "hubLogIndex": hubLogIndex,
       "hubLogTime": hubLogTime,
       "hubLogDescription": hubLogDescription,
       "hubEtherCapabilities": hubEtherCapabilities,
       "hubEtherCapabilitiesTable": hubEtherCapabilitiesTable,
       "hubEtherCapabilitiesEntry": hubEtherCapabilitiesEntry,
       "hubEtherCapabilitiesSlotNumber": hubEtherCapabilitiesSlotNumber,
       "hubEtherCapabilitiesIndex": hubEtherCapabilitiesIndex,
       "hubEtherCapabilitiesLanType": hubEtherCapabilitiesLanType,
       "hubEtherCapabilitiesLanSpeed": hubEtherCapabilitiesLanSpeed,
       "hubEtherCapabilitiesTrueCollisions": hubEtherCapabilitiesTrueCollisions,
       "hubEtherCapabilitiesState": hubEtherCapabilitiesState,
       "hubStatistics": hubStatistics,
       "hubEtherStatsTable": hubEtherStatsTable,
       "hubEtherStatsEntry": hubEtherStatsEntry,
       "hubEtherStatsSlotNumber": hubEtherStatsSlotNumber,
       "hubEtherStatsIndex": hubEtherStatsIndex,
       "hubEtherStatsDropEvents": hubEtherStatsDropEvents,
       "hubEtherStatsOctets": hubEtherStatsOctets,
       "hubEtherStatsPkts": hubEtherStatsPkts,
       "hubEtherStatsBroadcastPkts": hubEtherStatsBroadcastPkts,
       "hubEtherStatsMulticastPkts": hubEtherStatsMulticastPkts,
       "hubEtherStatsCRCAlignErrors": hubEtherStatsCRCAlignErrors,
       "hubEtherStatsUndersizePkts": hubEtherStatsUndersizePkts,
       "hubEtherStatsOversizePkts": hubEtherStatsOversizePkts,
       "hubEtherStatsFragments": hubEtherStatsFragments,
       "hubEtherStatsJabbers": hubEtherStatsJabbers,
       "hubEtherStatsCollisions": hubEtherStatsCollisions,
       "hubEtherStatsPkts64Octets": hubEtherStatsPkts64Octets,
       "hubEtherStatsPkts65to127Octets": hubEtherStatsPkts65to127Octets,
       "hubEtherStatsPkts128to255Octets": hubEtherStatsPkts128to255Octets,
       "hubEtherStatsPkts256to511Octets": hubEtherStatsPkts256to511Octets,
       "hubEtherStatsPkts512to1023Octets": hubEtherStatsPkts512to1023Octets,
       "hubEtherStatsPkts1024to1518Octets": hubEtherStatsPkts1024to1518Octets,
       "hubHistory": hubHistory,
       "hubHistoryControlFastPollInterval": hubHistoryControlFastPollInterval,
       "hubHistoryControlSlowPollInterval": hubHistoryControlSlowPollInterval,
       "hubHistoryControlTable": hubHistoryControlTable,
       "hubHistoryControlEntry": hubHistoryControlEntry,
       "hubHistoryControlSlotNumber": hubHistoryControlSlotNumber,
       "hubHistoryControlIndex": hubHistoryControlIndex,
       "hubHistoryControlHistoryIndex": hubHistoryControlHistoryIndex,
       "hubHistoryControlBuckets": hubHistoryControlBuckets,
       "hubHistoryControlInterval": hubHistoryControlInterval,
       "hubEtherHistoryTable": hubEtherHistoryTable,
       "hubEtherHistoryEntry": hubEtherHistoryEntry,
       "hubEtherHistoryIndex": hubEtherHistoryIndex,
       "hubEtherHistorySampleIndex": hubEtherHistorySampleIndex,
       "hubEtherHistoryIntervalStart": hubEtherHistoryIntervalStart,
       "hubEtherHistoryDropEvents": hubEtherHistoryDropEvents,
       "hubEtherHistoryOctets": hubEtherHistoryOctets,
       "hubEtherHistoryPkts": hubEtherHistoryPkts,
       "hubEtherHistoryBroadcastPkts": hubEtherHistoryBroadcastPkts,
       "hubEtherHistoryMulticastPkts": hubEtherHistoryMulticastPkts,
       "hubEtherHistoryCRCAlignErrors": hubEtherHistoryCRCAlignErrors,
       "hubEtherHistoryUndersizePkts": hubEtherHistoryUndersizePkts,
       "hubEtherHistoryOversizePkts": hubEtherHistoryOversizePkts,
       "hubEtherHistoryFragments": hubEtherHistoryFragments,
       "hubEtherHistoryJabbers": hubEtherHistoryJabbers,
       "hubEtherHistoryCollisions": hubEtherHistoryCollisions,
       "hubEtherHistoryUtilization": hubEtherHistoryUtilization}
)
