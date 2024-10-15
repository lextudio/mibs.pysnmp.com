# SNMP MIB module (LBHUB-FMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LBHUB-FMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:26 2024
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

(rpMauMediaAvailable,
 rptrPortAutoPartitionState) = mibBuilder.importSymbols(
    "MAU-MIB",
    "rpMauMediaAvailable",
    "rptrPortAutoPartitionState")

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
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "iso",
    "mgmt")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Mib_2_ObjectIdentity = ObjectIdentity
mib_2 = _Mib_2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 1)
)
_Interfaces_ObjectIdentity = ObjectIdentity
interfaces = _Interfaces_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 2)
)
_At_ObjectIdentity = ObjectIdentity
at = _At_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 3)
)
_Ip_ObjectIdentity = ObjectIdentity
ip = _Ip_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 4)
)
_Icmp_ObjectIdentity = ObjectIdentity
icmp = _Icmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 5)
)
_Tcp_ObjectIdentity = ObjectIdentity
tcp = _Tcp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 6)
)
_Udp_ObjectIdentity = ObjectIdentity
udp = _Udp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 7)
)
_Egp_ObjectIdentity = ObjectIdentity
egp = _Egp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 8)
)
_Transmission_ObjectIdentity = ObjectIdentity
transmission = _Transmission_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10)
)
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 11)
)
_Rmon_ObjectIdentity = ObjectIdentity
rmon = _Rmon_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16)
)
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 1)
)
_History_ObjectIdentity = ObjectIdentity
history = _History_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 2)
)
_Alarm_ObjectIdentity = ObjectIdentity
alarm = _Alarm_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 3)
)
_AlarmTable_Object = MibTable
alarmTable = _AlarmTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    alarmTable.setStatus("mandatory")
_AlarmEntry_Object = MibTableRow
alarmEntry = _AlarmEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1)
)
alarmEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "alarmIndex"),
)
if mibBuilder.loadTexts:
    alarmEntry.setStatus("mandatory")


class _AlarmIndex_Type(Integer32):
    """Custom type alarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlarmIndex_Type.__name__ = "Integer32"
_AlarmIndex_Object = MibTableColumn
alarmIndex = _AlarmIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 1),
    _AlarmIndex_Type()
)
alarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmIndex.setStatus("mandatory")
_AlarmInterval_Type = Integer32
_AlarmInterval_Object = MibTableColumn
alarmInterval = _AlarmInterval_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 2),
    _AlarmInterval_Type()
)
alarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmInterval.setStatus("mandatory")
_AlarmVariable_Type = ObjectIdentifier
_AlarmVariable_Object = MibTableColumn
alarmVariable = _AlarmVariable_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 3),
    _AlarmVariable_Type()
)
alarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmVariable.setStatus("mandatory")


class _AlarmSampleType_Type(Integer32):
    """Custom type alarmSampleType based on Integer32"""
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


_AlarmSampleType_Type.__name__ = "Integer32"
_AlarmSampleType_Object = MibTableColumn
alarmSampleType = _AlarmSampleType_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 4),
    _AlarmSampleType_Type()
)
alarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmSampleType.setStatus("mandatory")
_AlarmValue_Type = Integer32
_AlarmValue_Object = MibTableColumn
alarmValue = _AlarmValue_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 5),
    _AlarmValue_Type()
)
alarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmValue.setStatus("mandatory")


class _AlarmStartupAlarm_Type(Integer32):
    """Custom type alarmStartupAlarm based on Integer32"""
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


_AlarmStartupAlarm_Type.__name__ = "Integer32"
_AlarmStartupAlarm_Object = MibTableColumn
alarmStartupAlarm = _AlarmStartupAlarm_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 6),
    _AlarmStartupAlarm_Type()
)
alarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStartupAlarm.setStatus("mandatory")
_AlarmRisingThreshold_Type = Integer32
_AlarmRisingThreshold_Object = MibTableColumn
alarmRisingThreshold = _AlarmRisingThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 7),
    _AlarmRisingThreshold_Type()
)
alarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRisingThreshold.setStatus("mandatory")
_AlarmFallingThreshold_Type = Integer32
_AlarmFallingThreshold_Object = MibTableColumn
alarmFallingThreshold = _AlarmFallingThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 8),
    _AlarmFallingThreshold_Type()
)
alarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFallingThreshold.setStatus("mandatory")


class _AlarmRisingEventIndex_Type(Integer32):
    """Custom type alarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmRisingEventIndex_Type.__name__ = "Integer32"
_AlarmRisingEventIndex_Object = MibTableColumn
alarmRisingEventIndex = _AlarmRisingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 9),
    _AlarmRisingEventIndex_Type()
)
alarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmRisingEventIndex.setStatus("mandatory")


class _AlarmFallingEventIndex_Type(Integer32):
    """Custom type alarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AlarmFallingEventIndex_Type.__name__ = "Integer32"
_AlarmFallingEventIndex_Object = MibTableColumn
alarmFallingEventIndex = _AlarmFallingEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 10),
    _AlarmFallingEventIndex_Type()
)
alarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmFallingEventIndex.setStatus("mandatory")
_AlarmOwner_Type = DisplayString
_AlarmOwner_Object = MibTableColumn
alarmOwner = _AlarmOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 11),
    _AlarmOwner_Type()
)
alarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmOwner.setStatus("mandatory")


class _AlarmStatus_Type(Integer32):
    """Custom type alarmStatus based on Integer32"""
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


_AlarmStatus_Type.__name__ = "Integer32"
_AlarmStatus_Object = MibTableColumn
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 3, 1, 1, 12),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")
_Hosts_ObjectIdentity = ObjectIdentity
hosts = _Hosts_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 4)
)
_HostTopN_ObjectIdentity = ObjectIdentity
hostTopN = _HostTopN_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 5)
)
_Matrix_ObjectIdentity = ObjectIdentity
matrix = _Matrix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 6)
)
_Filter_ObjectIdentity = ObjectIdentity
filter = _Filter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 7)
)
_Capture_ObjectIdentity = ObjectIdentity
capture = _Capture_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 8)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 9)
)
_EventTable_Object = MibTable
eventTable = _EventTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1)
)
if mibBuilder.loadTexts:
    eventTable.setStatus("mandatory")
_EventEntry_Object = MibTableRow
eventEntry = _EventEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1)
)
eventEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "eventIndex"),
)
if mibBuilder.loadTexts:
    eventEntry.setStatus("mandatory")


class _EventIndex_Type(Integer32):
    """Custom type eventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EventIndex_Type.__name__ = "Integer32"
_EventIndex_Object = MibTableColumn
eventIndex = _EventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 1),
    _EventIndex_Type()
)
eventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventIndex.setStatus("mandatory")


class _EventDescription_Type(DisplayString):
    """Custom type eventDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventDescription_Type.__name__ = "DisplayString"
_EventDescription_Object = MibTableColumn
eventDescription = _EventDescription_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 2),
    _EventDescription_Type()
)
eventDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDescription.setStatus("mandatory")


class _EventType_Type(Integer32):
    """Custom type eventType based on Integer32"""
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


_EventType_Type.__name__ = "Integer32"
_EventType_Object = MibTableColumn
eventType = _EventType_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 3),
    _EventType_Type()
)
eventType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventType.setStatus("mandatory")


class _EventCommunity_Type(OctetString):
    """Custom type eventCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_EventCommunity_Type.__name__ = "OctetString"
_EventCommunity_Object = MibTableColumn
eventCommunity = _EventCommunity_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 4),
    _EventCommunity_Type()
)
eventCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventCommunity.setStatus("mandatory")
_EventLastTimeSent_Type = TimeTicks
_EventLastTimeSent_Object = MibTableColumn
eventLastTimeSent = _EventLastTimeSent_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 5),
    _EventLastTimeSent_Type()
)
eventLastTimeSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLastTimeSent.setStatus("mandatory")
_EventOwner_Type = DisplayString
_EventOwner_Object = MibTableColumn
eventOwner = _EventOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 6),
    _EventOwner_Type()
)
eventOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventOwner.setStatus("mandatory")


class _EventStatus_Type(Integer32):
    """Custom type eventStatus based on Integer32"""
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


_EventStatus_Type.__name__ = "Integer32"
_EventStatus_Object = MibTableColumn
eventStatus = _EventStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 1, 1, 7),
    _EventStatus_Type()
)
eventStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventStatus.setStatus("mandatory")
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2)
)
if mibBuilder.loadTexts:
    logTable.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1)
)
logEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "logEventIndex"),
    (0, "LBHUB-FMS-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")


class _LogEventIndex_Type(Integer32):
    """Custom type logEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_LogEventIndex_Type.__name__ = "Integer32"
_LogEventIndex_Object = MibTableColumn
logEventIndex = _LogEventIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 1),
    _LogEventIndex_Type()
)
logEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logEventIndex.setStatus("mandatory")
_LogIndex_Type = Integer32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 2),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")
_LogTime_Type = TimeTicks
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 3),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("mandatory")


class _LogDescription_Type(DisplayString):
    """Custom type logDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LogDescription_Type.__name__ = "DisplayString"
_LogDescription_Object = MibTableColumn
logDescription = _LogDescription_Object(
    (1, 3, 6, 1, 2, 1, 16, 9, 2, 1, 4),
    _LogDescription_Type()
)
logDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDescription.setStatus("mandatory")
_Dot1dBridge_ObjectIdentity = ObjectIdentity
dot1dBridge = _Dot1dBridge_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17)
)
_Novell_ObjectIdentity = ObjectIdentity
novell = _Novell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23)
)
_MibDoc_ObjectIdentity = ObjectIdentity
mibDoc = _MibDoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2)
)
_Ipx_ObjectIdentity = ObjectIdentity
ipx = _Ipx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5)
)
_IpxSystem_ObjectIdentity = ObjectIdentity
ipxSystem = _IpxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1)
)
_IpxBasicSysTable_Object = MibTable
ipxBasicSysTable = _IpxBasicSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1)
)
if mibBuilder.loadTexts:
    ipxBasicSysTable.setStatus("mandatory")
_IpxBasicSysEntry_Object = MibTableRow
ipxBasicSysEntry = _IpxBasicSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1)
)
ipxBasicSysEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "ipxBasicSysInstance"),
)
if mibBuilder.loadTexts:
    ipxBasicSysEntry.setStatus("mandatory")
_IpxBasicSysInstance_Type = Integer32
_IpxBasicSysInstance_Object = MibTableColumn
ipxBasicSysInstance = _IpxBasicSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 1),
    _IpxBasicSysInstance_Type()
)
ipxBasicSysInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInstance.setStatus("mandatory")


class _IpxBasicSysExistState_Type(Integer32):
    """Custom type ipxBasicSysExistState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_IpxBasicSysExistState_Type.__name__ = "Integer32"
_IpxBasicSysExistState_Object = MibTableColumn
ipxBasicSysExistState = _IpxBasicSysExistState_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 2),
    _IpxBasicSysExistState_Type()
)
ipxBasicSysExistState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysExistState.setStatus("mandatory")


class _IpxBasicSysNetNumber_Type(OctetString):
    """Custom type ipxBasicSysNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_IpxBasicSysNetNumber_Type.__name__ = "OctetString"
_IpxBasicSysNetNumber_Object = MibTableColumn
ipxBasicSysNetNumber = _IpxBasicSysNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 3),
    _IpxBasicSysNetNumber_Type()
)
ipxBasicSysNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysNetNumber.setStatus("mandatory")


class _IpxBasicSysNode_Type(OctetString):
    """Custom type ipxBasicSysNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IpxBasicSysNode_Type.__name__ = "OctetString"
_IpxBasicSysNode_Object = MibTableColumn
ipxBasicSysNode = _IpxBasicSysNode_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 4),
    _IpxBasicSysNode_Type()
)
ipxBasicSysNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysNode.setStatus("mandatory")


class _IpxBasicSysName_Type(OctetString):
    """Custom type ipxBasicSysName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_IpxBasicSysName_Type.__name__ = "OctetString"
_IpxBasicSysName_Object = MibTableColumn
ipxBasicSysName = _IpxBasicSysName_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 5),
    _IpxBasicSysName_Type()
)
ipxBasicSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxBasicSysName.setStatus("mandatory")
_IpxBasicSysInReceives_Type = Counter32
_IpxBasicSysInReceives_Object = MibTableColumn
ipxBasicSysInReceives = _IpxBasicSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 6),
    _IpxBasicSysInReceives_Type()
)
ipxBasicSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInReceives.setStatus("mandatory")
_IpxBasicSysInHdrErrors_Type = Counter32
_IpxBasicSysInHdrErrors_Object = MibTableColumn
ipxBasicSysInHdrErrors = _IpxBasicSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 7),
    _IpxBasicSysInHdrErrors_Type()
)
ipxBasicSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInHdrErrors.setStatus("mandatory")
_IpxBasicSysInUnknownSockets_Type = Counter32
_IpxBasicSysInUnknownSockets_Object = MibTableColumn
ipxBasicSysInUnknownSockets = _IpxBasicSysInUnknownSockets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 8),
    _IpxBasicSysInUnknownSockets_Type()
)
ipxBasicSysInUnknownSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInUnknownSockets.setStatus("mandatory")
_IpxBasicSysInDiscards_Type = Counter32
_IpxBasicSysInDiscards_Object = MibTableColumn
ipxBasicSysInDiscards = _IpxBasicSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 9),
    _IpxBasicSysInDiscards_Type()
)
ipxBasicSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDiscards.setStatus("mandatory")
_IpxBasicSysInBadChecksums_Type = Counter32
_IpxBasicSysInBadChecksums_Object = MibTableColumn
ipxBasicSysInBadChecksums = _IpxBasicSysInBadChecksums_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 10),
    _IpxBasicSysInBadChecksums_Type()
)
ipxBasicSysInBadChecksums.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInBadChecksums.setStatus("mandatory")
_IpxBasicSysInDelivers_Type = Counter32
_IpxBasicSysInDelivers_Object = MibTableColumn
ipxBasicSysInDelivers = _IpxBasicSysInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 11),
    _IpxBasicSysInDelivers_Type()
)
ipxBasicSysInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysInDelivers.setStatus("mandatory")
_IpxBasicSysNoRoutes_Type = Counter32
_IpxBasicSysNoRoutes_Object = MibTableColumn
ipxBasicSysNoRoutes = _IpxBasicSysNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 12),
    _IpxBasicSysNoRoutes_Type()
)
ipxBasicSysNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysNoRoutes.setStatus("mandatory")
_IpxBasicSysOutRequests_Type = Counter32
_IpxBasicSysOutRequests_Object = MibTableColumn
ipxBasicSysOutRequests = _IpxBasicSysOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 13),
    _IpxBasicSysOutRequests_Type()
)
ipxBasicSysOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutRequests.setStatus("mandatory")
_IpxBasicSysOutMalformedRequests_Type = Counter32
_IpxBasicSysOutMalformedRequests_Object = MibTableColumn
ipxBasicSysOutMalformedRequests = _IpxBasicSysOutMalformedRequests_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 14),
    _IpxBasicSysOutMalformedRequests_Type()
)
ipxBasicSysOutMalformedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutMalformedRequests.setStatus("mandatory")
_IpxBasicSysOutDiscards_Type = Counter32
_IpxBasicSysOutDiscards_Object = MibTableColumn
ipxBasicSysOutDiscards = _IpxBasicSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 15),
    _IpxBasicSysOutDiscards_Type()
)
ipxBasicSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutDiscards.setStatus("mandatory")
_IpxBasicSysOutPackets_Type = Counter32
_IpxBasicSysOutPackets_Object = MibTableColumn
ipxBasicSysOutPackets = _IpxBasicSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 16),
    _IpxBasicSysOutPackets_Type()
)
ipxBasicSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOutPackets.setStatus("mandatory")
_IpxBasicSysConfigSockets_Type = Integer32
_IpxBasicSysConfigSockets_Object = MibTableColumn
ipxBasicSysConfigSockets = _IpxBasicSysConfigSockets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 17),
    _IpxBasicSysConfigSockets_Type()
)
ipxBasicSysConfigSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysConfigSockets.setStatus("mandatory")
_IpxBasicSysOpenSocketFails_Type = Counter32
_IpxBasicSysOpenSocketFails_Object = MibTableColumn
ipxBasicSysOpenSocketFails = _IpxBasicSysOpenSocketFails_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 1, 1, 18),
    _IpxBasicSysOpenSocketFails_Type()
)
ipxBasicSysOpenSocketFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxBasicSysOpenSocketFails.setStatus("mandatory")
_IpxAdvSysTable_Object = MibTable
ipxAdvSysTable = _IpxAdvSysTable_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ipxAdvSysTable.setStatus("mandatory")
_IpxAdvSysEntry_Object = MibTableRow
ipxAdvSysEntry = _IpxAdvSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1)
)
ipxAdvSysEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "ipxAdvSysInstance"),
)
if mibBuilder.loadTexts:
    ipxAdvSysEntry.setStatus("mandatory")
_IpxAdvSysInstance_Type = Integer32
_IpxAdvSysInstance_Object = MibTableColumn
ipxAdvSysInstance = _IpxAdvSysInstance_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 1),
    _IpxAdvSysInstance_Type()
)
ipxAdvSysInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysInstance.setStatus("mandatory")


class _IpxAdvSysMaxPathSplits_Type(Integer32):
    """Custom type ipxAdvSysMaxPathSplits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_IpxAdvSysMaxPathSplits_Type.__name__ = "Integer32"
_IpxAdvSysMaxPathSplits_Object = MibTableColumn
ipxAdvSysMaxPathSplits = _IpxAdvSysMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 2),
    _IpxAdvSysMaxPathSplits_Type()
)
ipxAdvSysMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysMaxPathSplits.setStatus("mandatory")


class _IpxAdvSysMaxHops_Type(Integer32):
    """Custom type ipxAdvSysMaxHops based on Integer32"""
    defaultValue = 64


_IpxAdvSysMaxHops_Object = MibTableColumn
ipxAdvSysMaxHops = _IpxAdvSysMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 3),
    _IpxAdvSysMaxHops_Type()
)
ipxAdvSysMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAdvSysMaxHops.setStatus("mandatory")
_IpxAdvSysTooManyHops_Type = Counter32
_IpxAdvSysTooManyHops_Object = MibTableColumn
ipxAdvSysTooManyHops = _IpxAdvSysTooManyHops_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 4),
    _IpxAdvSysTooManyHops_Type()
)
ipxAdvSysTooManyHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysTooManyHops.setStatus("mandatory")
_IpxAdvSysInFiltered_Type = Counter32
_IpxAdvSysInFiltered_Object = MibTableColumn
ipxAdvSysInFiltered = _IpxAdvSysInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 5),
    _IpxAdvSysInFiltered_Type()
)
ipxAdvSysInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysInFiltered.setStatus("mandatory")
_IpxAdvSysCompressDiscards_Type = Counter32
_IpxAdvSysCompressDiscards_Object = MibTableColumn
ipxAdvSysCompressDiscards = _IpxAdvSysCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 6),
    _IpxAdvSysCompressDiscards_Type()
)
ipxAdvSysCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysCompressDiscards.setStatus("mandatory")
_IpxAdvSysNETBIOSPackets_Type = Counter32
_IpxAdvSysNETBIOSPackets_Object = MibTableColumn
ipxAdvSysNETBIOSPackets = _IpxAdvSysNETBIOSPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 7),
    _IpxAdvSysNETBIOSPackets_Type()
)
ipxAdvSysNETBIOSPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysNETBIOSPackets.setStatus("mandatory")
_IpxAdvSysForwPackets_Type = Counter32
_IpxAdvSysForwPackets_Object = MibTableColumn
ipxAdvSysForwPackets = _IpxAdvSysForwPackets_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 8),
    _IpxAdvSysForwPackets_Type()
)
ipxAdvSysForwPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysForwPackets.setStatus("mandatory")
_IpxAdvSysOutFiltered_Type = Counter32
_IpxAdvSysOutFiltered_Object = MibTableColumn
ipxAdvSysOutFiltered = _IpxAdvSysOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 9),
    _IpxAdvSysOutFiltered_Type()
)
ipxAdvSysOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysOutFiltered.setStatus("mandatory")
_IpxAdvSysOutCompressDiscards_Type = Counter32
_IpxAdvSysOutCompressDiscards_Object = MibTableColumn
ipxAdvSysOutCompressDiscards = _IpxAdvSysOutCompressDiscards_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 10),
    _IpxAdvSysOutCompressDiscards_Type()
)
ipxAdvSysOutCompressDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysOutCompressDiscards.setStatus("mandatory")
_IpxAdvSysCircCount_Type = Counter32
_IpxAdvSysCircCount_Object = MibTableColumn
ipxAdvSysCircCount = _IpxAdvSysCircCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 11),
    _IpxAdvSysCircCount_Type()
)
ipxAdvSysCircCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysCircCount.setStatus("mandatory")
_IpxAdvSysDestCount_Type = Counter32
_IpxAdvSysDestCount_Object = MibTableColumn
ipxAdvSysDestCount = _IpxAdvSysDestCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 12),
    _IpxAdvSysDestCount_Type()
)
ipxAdvSysDestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysDestCount.setStatus("mandatory")
_IpxAdvSysServCount_Type = Counter32
_IpxAdvSysServCount_Object = MibTableColumn
ipxAdvSysServCount = _IpxAdvSysServCount_Object(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 1, 2, 1, 13),
    _IpxAdvSysServCount_Type()
)
ipxAdvSysServCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAdvSysServCount.setStatus("mandatory")
_IpxCircuit_ObjectIdentity = ObjectIdentity
ipxCircuit = _IpxCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 2)
)
_IpxForwarding_ObjectIdentity = ObjectIdentity
ipxForwarding = _IpxForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 3)
)
_IpxServices_ObjectIdentity = ObjectIdentity
ipxServices = _IpxServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 4)
)
_IpxTraps_ObjectIdentity = ObjectIdentity
ipxTraps = _IpxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 23, 2, 5, 5)
)
_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_TerminalServer_ObjectIdentity = ObjectIdentity
terminalServer = _TerminalServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 1)
)
_DedicatedBridgeServer_ObjectIdentity = ObjectIdentity
dedicatedBridgeServer = _DedicatedBridgeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 2)
)
_DedicatedRouteServer_ObjectIdentity = ObjectIdentity
dedicatedRouteServer = _DedicatedRouteServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 3)
)
_Brouter_ObjectIdentity = ObjectIdentity
brouter = _Brouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 4)
)
_GenericMSWorkstation_ObjectIdentity = ObjectIdentity
genericMSWorkstation = _GenericMSWorkstation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 5)
)
_GenericMSServer_ObjectIdentity = ObjectIdentity
genericMSServer = _GenericMSServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 6)
)
_GenericUnixServer_ObjectIdentity = ObjectIdentity
genericUnixServer = _GenericUnixServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 7)
)
_Hub_ObjectIdentity = ObjectIdentity
hub = _Hub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8)
)
_LinkBuilder3GH_ObjectIdentity = ObjectIdentity
linkBuilder3GH = _LinkBuilder3GH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 1)
)
_LinkBuilder10BTi_ObjectIdentity = ObjectIdentity
linkBuilder10BTi = _LinkBuilder10BTi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 2)
)
_LinkBuilderECS_ObjectIdentity = ObjectIdentity
linkBuilderECS = _LinkBuilderECS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 3)
)
_LinkBuilderMSH_ObjectIdentity = ObjectIdentity
linkBuilderMSH = _LinkBuilderMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 4)
)
_LinkBuilderFMS_ObjectIdentity = ObjectIdentity
linkBuilderFMS = _LinkBuilderFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 5)
)
_LinkBuilderFDDIwg_ObjectIdentity = ObjectIdentity
linkBuilderFDDIwg = _LinkBuilderFDDIwg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 6)
)
_LinkBuilderFMSII_ObjectIdentity = ObjectIdentity
linkBuilderFMSII = _LinkBuilderFMSII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 7)
)
_LinkSwitchFMS_ObjectIdentity = ObjectIdentity
linkSwitchFMS = _LinkSwitchFMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 8)
)
_LinkSwitchMSH_ObjectIdentity = ObjectIdentity
linkSwitchMSH = _LinkSwitchMSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 9)
)
_LinkBuilderFMSLBridge_ObjectIdentity = ObjectIdentity
linkBuilderFMSLBridge = _LinkBuilderFMSLBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 8, 10)
)
_Cards_ObjectIdentity = ObjectIdentity
cards = _Cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9)
)
_LinkBuilder3GH_cards_ObjectIdentity = ObjectIdentity
linkBuilder3GH_cards = _LinkBuilder3GH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 1)
)
_LinkBuilder10BTi_cards_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards = _LinkBuilder10BTi_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2)
)
_LinkBuilder10BTi_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_cards_utp = _LinkBuilder10BTi_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 1)
)
_LinkBuilder10BT_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilder10BT_cards_utp = _LinkBuilder10BT_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 2, 2)
)
_LinkBuilderECS_cards_ObjectIdentity = ObjectIdentity
linkBuilderECS_cards = _LinkBuilderECS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 3)
)
_LinkBuilderMSH_cards_ObjectIdentity = ObjectIdentity
linkBuilderMSH_cards = _LinkBuilderMSH_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 4)
)
_LinkBuilderFMS_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards = _LinkBuilderFMS_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5)
)
_LinkBuilderFMS_cards_utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_utp = _LinkBuilderFMS_cards_utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 1)
)
_LinkBuilderFMS_cards_coax_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_coax = _LinkBuilderFMS_cards_coax_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 2)
)
_LinkBuilderFMS_cards_fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_fiber = _LinkBuilderFMS_cards_fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 3)
)
_LinkBuilderFMS_cards_12fiber_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_12fiber = _LinkBuilderFMS_cards_12fiber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 4)
)
_LinkBuilderFMS_cards_24utp_ObjectIdentity = ObjectIdentity
linkBuilderFMS_cards_24utp = _LinkBuilderFMS_cards_24utp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 5, 5)
)
_LinkBuilderFMSII_cards_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards = _LinkBuilderFMSII_cards_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6)
)
_LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12tp_rj45 = _LinkBuilderFMSII_cards_12tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 1)
)
_LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_10coax_bnc = _LinkBuilderFMSII_cards_10coax_bnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 2)
)
_LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_6fiber_st = _LinkBuilderFMSII_cards_6fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 3)
)
_LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_12fiber_st = _LinkBuilderFMSII_cards_12fiber_st_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 4)
)
_LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_rj45 = _LinkBuilderFMSII_cards_24tp_rj45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 5)
)
_LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity = ObjectIdentity
linkBuilderFMSII_cards_24tp_telco = _LinkBuilderFMSII_cards_24tp_telco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 9, 6, 6)
)
_Chipsets_ObjectIdentity = ObjectIdentity
chipsets = _Chipsets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 10)
)
_Amp_mib_ObjectIdentity = ObjectIdentity
amp_mib = _Amp_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 3)
)
_GenericTrap_ObjectIdentity = ObjectIdentity
genericTrap = _GenericTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 4)
)
_ViewBuilderApps_ObjectIdentity = ObjectIdentity
viewBuilderApps = _ViewBuilderApps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 5)
)
_SpecificTrap_ObjectIdentity = ObjectIdentity
specificTrap = _SpecificTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 6)
)
_LinkBuilder3GH_mib_ObjectIdentity = ObjectIdentity
linkBuilder3GH_mib = _LinkBuilder3GH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 7)
)
_LinkBuilder10BTi_mib_ObjectIdentity = ObjectIdentity
linkBuilder10BTi_mib = _LinkBuilder10BTi_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8)
)
_LinkbuilderMonitorPackage_ObjectIdentity = ObjectIdentity
linkbuilderMonitorPackage = _LinkbuilderMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 1)
)


class _VmMonBatteryStatus_Type(Integer32):
    """Custom type vmMonBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1))
    )


_VmMonBatteryStatus_Type.__name__ = "Integer32"
_VmMonBatteryStatus_Object = MibScalar
vmMonBatteryStatus = _VmMonBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 1),
    _VmMonBatteryStatus_Type()
)
vmMonBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonBatteryStatus.setStatus("mandatory")
_VmMonPOSTResults_Type = Integer32
_VmMonPOSTResults_Object = MibScalar
vmMonPOSTResults = _VmMonPOSTResults_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 2),
    _VmMonPOSTResults_Type()
)
vmMonPOSTResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonPOSTResults.setStatus("mandatory")
_VmMonFault_ObjectIdentity = ObjectIdentity
vmMonFault = _VmMonFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3)
)


class _VmMonFaultModifiedFlag_Type(Integer32):
    """Custom type vmMonFaultModifiedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean-read", 1),
          ("modified", 2))
    )


_VmMonFaultModifiedFlag_Type.__name__ = "Integer32"
_VmMonFaultModifiedFlag_Object = MibScalar
vmMonFaultModifiedFlag = _VmMonFaultModifiedFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3, 1),
    _VmMonFaultModifiedFlag_Type()
)
vmMonFaultModifiedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmMonFaultModifiedFlag.setStatus("deprecated")
_VmMonFaultTable_Object = MibTable
vmMonFaultTable = _VmMonFaultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    vmMonFaultTable.setStatus("deprecated")
_VmMonFaultEntry_Object = MibTableRow
vmMonFaultEntry = _VmMonFaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3, 2, 1)
)
vmMonFaultEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "vmMonFaultIndex"),
)
if mibBuilder.loadTexts:
    vmMonFaultEntry.setStatus("deprecated")
_VmMonFaultIndex_Type = Integer32
_VmMonFaultIndex_Object = MibTableColumn
vmMonFaultIndex = _VmMonFaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3, 2, 1, 1),
    _VmMonFaultIndex_Type()
)
vmMonFaultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonFaultIndex.setStatus("deprecated")
_VmMonFaultErrorNumber_Type = Integer32
_VmMonFaultErrorNumber_Object = MibTableColumn
vmMonFaultErrorNumber = _VmMonFaultErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3, 2, 1, 2),
    _VmMonFaultErrorNumber_Type()
)
vmMonFaultErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonFaultErrorNumber.setStatus("deprecated")
_VmMonFaultTimeStamp_Type = TimeTicks
_VmMonFaultTimeStamp_Object = MibTableColumn
vmMonFaultTimeStamp = _VmMonFaultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3, 2, 1, 3),
    _VmMonFaultTimeStamp_Type()
)
vmMonFaultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonFaultTimeStamp.setStatus("deprecated")
_VmMonFaultRestartCount_Type = Integer32
_VmMonFaultRestartCount_Object = MibTableColumn
vmMonFaultRestartCount = _VmMonFaultRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 3, 2, 1, 4),
    _VmMonFaultRestartCount_Type()
)
vmMonFaultRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonFaultRestartCount.setStatus("deprecated")


class _VmMonDvtEcho_Type(Integer32):
    """Custom type vmMonDvtEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VmMonDvtEcho_Type.__name__ = "Integer32"
_VmMonDvtEcho_Object = MibScalar
vmMonDvtEcho = _VmMonDvtEcho_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 4),
    _VmMonDvtEcho_Type()
)
vmMonDvtEcho.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    vmMonDvtEcho.setStatus("deprecated")
_VmMonMgmtBusOverrunError_Type = Counter32
_VmMonMgmtBusOverrunError_Object = MibScalar
vmMonMgmtBusOverrunError = _VmMonMgmtBusOverrunError_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 5),
    _VmMonMgmtBusOverrunError_Type()
)
vmMonMgmtBusOverrunError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonMgmtBusOverrunError.setStatus("deprecated")
_VmMonMgmtBusFramingError_Type = Counter32
_VmMonMgmtBusFramingError_Object = MibScalar
vmMonMgmtBusFramingError = _VmMonMgmtBusFramingError_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 6),
    _VmMonMgmtBusFramingError_Type()
)
vmMonMgmtBusFramingError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonMgmtBusFramingError.setStatus("deprecated")
_VmMonMgmtBusOverflowError_Type = Counter32
_VmMonMgmtBusOverflowError_Object = MibScalar
vmMonMgmtBusOverflowError = _VmMonMgmtBusOverflowError_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 7),
    _VmMonMgmtBusOverflowError_Type()
)
vmMonMgmtBusOverflowError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonMgmtBusOverflowError.setStatus("deprecated")
_VmMonMgmtBusFiFoFullCounter_Type = Counter32
_VmMonMgmtBusFiFoFullCounter_Object = MibScalar
vmMonMgmtBusFiFoFullCounter = _VmMonMgmtBusFiFoFullCounter_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 1, 8),
    _VmMonMgmtBusFiFoFullCounter_Type()
)
vmMonMgmtBusFiFoFullCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMonMgmtBusFiFoFullCounter.setStatus("deprecated")
_LinkbuilderConfigPackage_ObjectIdentity = ObjectIdentity
linkbuilderConfigPackage = _LinkbuilderConfigPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 2)
)
_VmConfigGroupTable_Object = MibTable
vmConfigGroupTable = _VmConfigGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 2)
)
if mibBuilder.loadTexts:
    vmConfigGroupTable.setStatus("deprecated")
_VmConfigGroupEntry_Object = MibTableRow
vmConfigGroupEntry = _VmConfigGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 2, 1)
)
vmConfigGroupEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "vmConGroupIndex"),
)
if mibBuilder.loadTexts:
    vmConfigGroupEntry.setStatus("deprecated")


class _VmConGroupIndex_Type(Integer32):
    """Custom type vmConGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VmConGroupIndex_Type.__name__ = "Integer32"
_VmConGroupIndex_Object = MibTableColumn
vmConGroupIndex = _VmConGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 2, 1, 1),
    _VmConGroupIndex_Type()
)
vmConGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConGroupIndex.setStatus("deprecated")
_VmConGroupPortMask_Type = Integer32
_VmConGroupPortMask_Object = MibTableColumn
vmConGroupPortMask = _VmConGroupPortMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 2, 1, 2),
    _VmConGroupPortMask_Type()
)
vmConGroupPortMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConGroupPortMask.setStatus("deprecated")
_VmConfigPortTable_Object = MibTable
vmConfigPortTable = _VmConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3)
)
if mibBuilder.loadTexts:
    vmConfigPortTable.setStatus("deprecated")
_VmConfigPortEntry_Object = MibTableRow
vmConfigPortEntry = _VmConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3, 1)
)
vmConfigPortEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "vmConPortGroupIndex"),
    (0, "LBHUB-FMS-MIB", "vmConPortIndex"),
)
if mibBuilder.loadTexts:
    vmConfigPortEntry.setStatus("deprecated")


class _VmConPortGroupIndex_Type(Integer32):
    """Custom type vmConPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VmConPortGroupIndex_Type.__name__ = "Integer32"
_VmConPortGroupIndex_Object = MibTableColumn
vmConPortGroupIndex = _VmConPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3, 1, 1),
    _VmConPortGroupIndex_Type()
)
vmConPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConPortGroupIndex.setStatus("deprecated")


class _VmConPortIndex_Type(Integer32):
    """Custom type vmConPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VmConPortIndex_Type.__name__ = "Integer32"
_VmConPortIndex_Object = MibTableColumn
vmConPortIndex = _VmConPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3, 1, 2),
    _VmConPortIndex_Type()
)
vmConPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConPortIndex.setStatus("deprecated")


class _VmConPortSquelch_Type(Integer32):
    """Custom type vmConPortSquelch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1),
          ("notApplicable", 3))
    )


_VmConPortSquelch_Type.__name__ = "Integer32"
_VmConPortSquelch_Object = MibTableColumn
vmConPortSquelch = _VmConPortSquelch_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3, 1, 3),
    _VmConPortSquelch_Type()
)
vmConPortSquelch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmConPortSquelch.setStatus("deprecated")


class _VmConPortLinkPulse_Type(Integer32):
    """Custom type vmConPortLinkPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_VmConPortLinkPulse_Type.__name__ = "Integer32"
_VmConPortLinkPulse_Object = MibTableColumn
vmConPortLinkPulse = _VmConPortLinkPulse_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3, 1, 4),
    _VmConPortLinkPulse_Type()
)
vmConPortLinkPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmConPortLinkPulse.setStatus("deprecated")


class _VmConPortXoverSwitchState_Type(Integer32):
    """Custom type vmConPortXoverSwitchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("crossed", 3),
          ("normal", 2),
          ("notApplicable", 1))
    )


_VmConPortXoverSwitchState_Type.__name__ = "Integer32"
_VmConPortXoverSwitchState_Object = MibTableColumn
vmConPortXoverSwitchState = _VmConPortXoverSwitchState_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3, 1, 5),
    _VmConPortXoverSwitchState_Type()
)
vmConPortXoverSwitchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConPortXoverSwitchState.setStatus("deprecated")


class _VmConPortType_Type(Integer32):
    """Custom type vmConPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              32,
              40,
              41,
              50,
              60)
        )
    )
    namedValues = NamedValues(
        *(("bti-AUI", 50),
          ("bti-FixedUTP", 32),
          ("bti-ModularCoax", 41),
          ("bti-ModularFibreFL", 40),
          ("fms-AUI", 15),
          ("fms-FixedCoax", 2),
          ("fms-FixedFibreFL", 3),
          ("fms-FixedTP", 1),
          ("fms-ModularBridge", 4),
          ("fms-ModularCoax", 10),
          ("fms-ModularFMaleAUI", 9),
          ("fms-ModularFibreFB", 14),
          ("fms-ModularFibreFL", 11),
          ("fms-ModularMaleAUI", 8),
          ("fms-ModularSTP", 13),
          ("fms-ModularUTP", 12),
          ("unknown", 60))
    )


_VmConPortType_Type.__name__ = "Integer32"
_VmConPortType_Object = MibTableColumn
vmConPortType = _VmConPortType_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 3, 1, 6),
    _VmConPortType_Type()
)
vmConPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConPortType.setStatus("deprecated")
_VmConfigMediaTable_Object = MibTable
vmConfigMediaTable = _VmConfigMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 4)
)
if mibBuilder.loadTexts:
    vmConfigMediaTable.setStatus("deprecated")
_VmConfigMediaEntry_Object = MibTableRow
vmConfigMediaEntry = _VmConfigMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 4, 1)
)
vmConfigMediaEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "vmConMediaIndex"),
)
if mibBuilder.loadTexts:
    vmConfigMediaEntry.setStatus("deprecated")


class _VmConMediaIndex_Type(Integer32):
    """Custom type vmConMediaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VmConMediaIndex_Type.__name__ = "Integer32"
_VmConMediaIndex_Object = MibTableColumn
vmConMediaIndex = _VmConMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 4, 1, 1),
    _VmConMediaIndex_Type()
)
vmConMediaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConMediaIndex.setStatus("deprecated")


class _VmConMediaModuleRevNo_Type(Integer32):
    """Custom type vmConMediaModuleRevNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_VmConMediaModuleRevNo_Type.__name__ = "Integer32"
_VmConMediaModuleRevNo_Object = MibTableColumn
vmConMediaModuleRevNo = _VmConMediaModuleRevNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 4, 1, 2),
    _VmConMediaModuleRevNo_Type()
)
vmConMediaModuleRevNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConMediaModuleRevNo.setStatus("deprecated")


class _VmConMediaModuleCardType_Type(Integer32):
    """Custom type vmConMediaModuleCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              14,
              15,
              30,
              31,
              65,
              66,
              67,
              68,
              69,
              70,
              71)
        )
    )
    namedValues = NamedValues(
        *(("bt-12Port-UTP-Rev1", 15),
          ("bt-12Port-UTP-Rev2", 14),
          ("bti-12Port-UTP-Rev1", 31),
          ("bti-12Port-UTP-Rev2", 30),
          ("fms-10Port-Coax", 2),
          ("fms-12Port-Fibre", 3),
          ("fms-12Port-UTP", 1),
          ("fms-24PortUTP", 5),
          ("fms-6Port-Fibre", 4),
          ("fmsII-10Port-Coax", 66),
          ("fmsII-12Port-Fibre", 67),
          ("fmsII-12Port-TP-RJ45", 65),
          ("fmsII-24Port-TP-RJ45", 69),
          ("fmsII-24Port-TP-Telco", 70),
          ("fmsII-6Port-Fibre", 68),
          ("fmsII-RMON-Box", 71))
    )


_VmConMediaModuleCardType_Type.__name__ = "Integer32"
_VmConMediaModuleCardType_Object = MibTableColumn
vmConMediaModuleCardType = _VmConMediaModuleCardType_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 2, 4, 1, 3),
    _VmConMediaModuleCardType_Type()
)
vmConMediaModuleCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmConMediaModuleCardType.setStatus("deprecated")
_LinkbuilderStatusPackage_ObjectIdentity = ObjectIdentity
linkbuilderStatusPackage = _LinkbuilderStatusPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 3)
)
_DeprSnmpDot3RptrMgt_ObjectIdentity = ObjectIdentity
deprSnmpDot3RptrMgt = _DeprSnmpDot3RptrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4)
)
_DeprRptrBasicPackage_ObjectIdentity = ObjectIdentity
deprRptrBasicPackage = _DeprRptrBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1)
)
_DeprRptrRptrInfo_ObjectIdentity = ObjectIdentity
deprRptrRptrInfo = _DeprRptrRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 1)
)


class _DeprRptrGroupCapacity_Type(Integer32):
    """Custom type deprRptrGroupCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DeprRptrGroupCapacity_Type.__name__ = "Integer32"
_DeprRptrGroupCapacity_Object = MibScalar
deprRptrGroupCapacity = _DeprRptrGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 1, 1),
    _DeprRptrGroupCapacity_Type()
)
deprRptrGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrGroupCapacity.setStatus("deprecated")


class _DeprRptrOperStatus_Type(Integer32):
    """Custom type deprRptrOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("generalFailure", 6),
          ("groupFailure", 4),
          ("ok", 2),
          ("other", 1),
          ("portFailure", 5),
          ("rptrFailure", 3))
    )


_DeprRptrOperStatus_Type.__name__ = "Integer32"
_DeprRptrOperStatus_Object = MibScalar
deprRptrOperStatus = _DeprRptrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 1, 2),
    _DeprRptrOperStatus_Type()
)
deprRptrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrOperStatus.setStatus("deprecated")


class _DeprRptrHealthText_Type(DisplayString):
    """Custom type deprRptrHealthText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeprRptrHealthText_Type.__name__ = "DisplayString"
_DeprRptrHealthText_Object = MibScalar
deprRptrHealthText = _DeprRptrHealthText_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 1, 3),
    _DeprRptrHealthText_Type()
)
deprRptrHealthText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrHealthText.setStatus("deprecated")


class _DeprRptrReset_Type(Integer32):
    """Custom type deprRptrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 1),
          ("reset", 2))
    )


_DeprRptrReset_Type.__name__ = "Integer32"
_DeprRptrReset_Object = MibScalar
deprRptrReset = _DeprRptrReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 1, 4),
    _DeprRptrReset_Type()
)
deprRptrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deprRptrReset.setStatus("deprecated")


class _DeprRptrNonDisruptTest_Type(Integer32):
    """Custom type deprRptrNonDisruptTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSelfTest", 1),
          ("selfTest", 2))
    )


_DeprRptrNonDisruptTest_Type.__name__ = "Integer32"
_DeprRptrNonDisruptTest_Object = MibScalar
deprRptrNonDisruptTest = _DeprRptrNonDisruptTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 1, 5),
    _DeprRptrNonDisruptTest_Type()
)
deprRptrNonDisruptTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deprRptrNonDisruptTest.setStatus("deprecated")
_DeprRptrTotalPartitionedPorts_Type = Gauge32
_DeprRptrTotalPartitionedPorts_Object = MibScalar
deprRptrTotalPartitionedPorts = _DeprRptrTotalPartitionedPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 1, 6),
    _DeprRptrTotalPartitionedPorts_Type()
)
deprRptrTotalPartitionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrTotalPartitionedPorts.setStatus("deprecated")
_DeprRptrGroupInfo_ObjectIdentity = ObjectIdentity
deprRptrGroupInfo = _DeprRptrGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2)
)
_DeprRptrGroupTable_Object = MibTable
deprRptrGroupTable = _DeprRptrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deprRptrGroupTable.setStatus("deprecated")
_DeprRptrGroupEntry_Object = MibTableRow
deprRptrGroupEntry = _DeprRptrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1, 1)
)
deprRptrGroupEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "deprRptrGroupIndex"),
)
if mibBuilder.loadTexts:
    deprRptrGroupEntry.setStatus("deprecated")


class _DeprRptrGroupIndex_Type(Integer32):
    """Custom type deprRptrGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRptrGroupIndex_Type.__name__ = "Integer32"
_DeprRptrGroupIndex_Object = MibTableColumn
deprRptrGroupIndex = _DeprRptrGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1, 1, 1),
    _DeprRptrGroupIndex_Type()
)
deprRptrGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrGroupIndex.setStatus("deprecated")


class _DeprRptrGroupDescr_Type(DisplayString):
    """Custom type deprRptrGroupDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DeprRptrGroupDescr_Type.__name__ = "DisplayString"
_DeprRptrGroupDescr_Object = MibTableColumn
deprRptrGroupDescr = _DeprRptrGroupDescr_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1, 1, 2),
    _DeprRptrGroupDescr_Type()
)
deprRptrGroupDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrGroupDescr.setStatus("deprecated")
_DeprRptrGroupObjectID_Type = ObjectIdentifier
_DeprRptrGroupObjectID_Object = MibTableColumn
deprRptrGroupObjectID = _DeprRptrGroupObjectID_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1, 1, 3),
    _DeprRptrGroupObjectID_Type()
)
deprRptrGroupObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrGroupObjectID.setStatus("deprecated")


class _DeprRptrGroupOperStatus_Type(Integer32):
    """Custom type deprRptrGroupOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("malFunctioning", 3),
          ("notPresent", 4),
          ("operational", 2),
          ("other", 1),
          ("resetInProgress", 6),
          ("undertest", 5))
    )


_DeprRptrGroupOperStatus_Type.__name__ = "Integer32"
_DeprRptrGroupOperStatus_Object = MibTableColumn
deprRptrGroupOperStatus = _DeprRptrGroupOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1, 1, 4),
    _DeprRptrGroupOperStatus_Type()
)
deprRptrGroupOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrGroupOperStatus.setStatus("deprecated")
_DeprRptrGroupLastOperStatusChange_Type = TimeTicks
_DeprRptrGroupLastOperStatusChange_Object = MibTableColumn
deprRptrGroupLastOperStatusChange = _DeprRptrGroupLastOperStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1, 1, 5),
    _DeprRptrGroupLastOperStatusChange_Type()
)
deprRptrGroupLastOperStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrGroupLastOperStatusChange.setStatus("deprecated")


class _DeprRptrGroupPortCapacity_Type(Integer32):
    """Custom type deprRptrGroupPortCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRptrGroupPortCapacity_Type.__name__ = "Integer32"
_DeprRptrGroupPortCapacity_Object = MibTableColumn
deprRptrGroupPortCapacity = _DeprRptrGroupPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 2, 1, 1, 6),
    _DeprRptrGroupPortCapacity_Type()
)
deprRptrGroupPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrGroupPortCapacity.setStatus("deprecated")
_DeprRptrPortInfo_ObjectIdentity = ObjectIdentity
deprRptrPortInfo = _DeprRptrPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3)
)
_DeprRptrPortTable_Object = MibTable
deprRptrPortTable = _DeprRptrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3, 1)
)
if mibBuilder.loadTexts:
    deprRptrPortTable.setStatus("deprecated")
_DeprRptrPortEntry_Object = MibTableRow
deprRptrPortEntry = _DeprRptrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3, 1, 1)
)
deprRptrPortEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "deprRptrPortGroupIndex"),
    (0, "LBHUB-FMS-MIB", "deprRptrPortIndex"),
)
if mibBuilder.loadTexts:
    deprRptrPortEntry.setStatus("deprecated")


class _DeprRptrPortGroupIndex_Type(Integer32):
    """Custom type deprRptrPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRptrPortGroupIndex_Type.__name__ = "Integer32"
_DeprRptrPortGroupIndex_Object = MibTableColumn
deprRptrPortGroupIndex = _DeprRptrPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3, 1, 1, 1),
    _DeprRptrPortGroupIndex_Type()
)
deprRptrPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrPortGroupIndex.setStatus("deprecated")


class _DeprRptrPortIndex_Type(Integer32):
    """Custom type deprRptrPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRptrPortIndex_Type.__name__ = "Integer32"
_DeprRptrPortIndex_Object = MibTableColumn
deprRptrPortIndex = _DeprRptrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3, 1, 1, 2),
    _DeprRptrPortIndex_Type()
)
deprRptrPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrPortIndex.setStatus("deprecated")


class _DeprRptrPortAdminStatus_Type(Integer32):
    """Custom type deprRptrPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DeprRptrPortAdminStatus_Type.__name__ = "Integer32"
_DeprRptrPortAdminStatus_Object = MibTableColumn
deprRptrPortAdminStatus = _DeprRptrPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3, 1, 1, 3),
    _DeprRptrPortAdminStatus_Type()
)
deprRptrPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deprRptrPortAdminStatus.setStatus("deprecated")


class _DeprRptrPortAutoPartitionState_Type(Integer32):
    """Custom type deprRptrPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoPartitioned", 1),
          ("notAutoPartitioned", 2))
    )


_DeprRptrPortAutoPartitionState_Type.__name__ = "Integer32"
_DeprRptrPortAutoPartitionState_Object = MibTableColumn
deprRptrPortAutoPartitionState = _DeprRptrPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3, 1, 1, 4),
    _DeprRptrPortAutoPartitionState_Type()
)
deprRptrPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrPortAutoPartitionState.setStatus("deprecated")


class _DeprRptrPortOperStatus_Type(Integer32):
    """Custom type deprRptrPortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_DeprRptrPortOperStatus_Type.__name__ = "Integer32"
_DeprRptrPortOperStatus_Object = MibTableColumn
deprRptrPortOperStatus = _DeprRptrPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 1, 3, 1, 1, 5),
    _DeprRptrPortOperStatus_Type()
)
deprRptrPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrPortOperStatus.setStatus("deprecated")
_DeprRptrMonitorPackage_ObjectIdentity = ObjectIdentity
deprRptrMonitorPackage = _DeprRptrMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2)
)
_DeprRptrMonitorRptrInfo_ObjectIdentity = ObjectIdentity
deprRptrMonitorRptrInfo = _DeprRptrMonitorRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 1)
)
_DeprRptrMonitorTransmitCollisions_Type = Counter32
_DeprRptrMonitorTransmitCollisions_Object = MibScalar
deprRptrMonitorTransmitCollisions = _DeprRptrMonitorTransmitCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 1, 1),
    _DeprRptrMonitorTransmitCollisions_Type()
)
deprRptrMonitorTransmitCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorTransmitCollisions.setStatus("deprecated")
_DeprRptrMonitorGroupInfo_ObjectIdentity = ObjectIdentity
deprRptrMonitorGroupInfo = _DeprRptrMonitorGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 2)
)
_DeprRptrMonitorGroupTable_Object = MibTable
deprRptrMonitorGroupTable = _DeprRptrMonitorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    deprRptrMonitorGroupTable.setStatus("deprecated")
_DeprRptrMonitorGroupEntry_Object = MibTableRow
deprRptrMonitorGroupEntry = _DeprRptrMonitorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 2, 1, 1)
)
deprRptrMonitorGroupEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "deprRptrMonitorGroupIndex"),
)
if mibBuilder.loadTexts:
    deprRptrMonitorGroupEntry.setStatus("deprecated")


class _DeprRptrMonitorGroupIndex_Type(Integer32):
    """Custom type deprRptrMonitorGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRptrMonitorGroupIndex_Type.__name__ = "Integer32"
_DeprRptrMonitorGroupIndex_Object = MibTableColumn
deprRptrMonitorGroupIndex = _DeprRptrMonitorGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 2, 1, 1, 1),
    _DeprRptrMonitorGroupIndex_Type()
)
deprRptrMonitorGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorGroupIndex.setStatus("deprecated")
_DeprRptrMonitorGroupTotalFrames_Type = Counter32
_DeprRptrMonitorGroupTotalFrames_Object = MibTableColumn
deprRptrMonitorGroupTotalFrames = _DeprRptrMonitorGroupTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 2, 1, 1, 2),
    _DeprRptrMonitorGroupTotalFrames_Type()
)
deprRptrMonitorGroupTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorGroupTotalFrames.setStatus("deprecated")
_DeprRptrMonitorGroupTotalOctets_Type = Counter32
_DeprRptrMonitorGroupTotalOctets_Object = MibTableColumn
deprRptrMonitorGroupTotalOctets = _DeprRptrMonitorGroupTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 2, 1, 1, 3),
    _DeprRptrMonitorGroupTotalOctets_Type()
)
deprRptrMonitorGroupTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorGroupTotalOctets.setStatus("deprecated")
_DeprRptrMonitorGroupTotalErrors_Type = Counter32
_DeprRptrMonitorGroupTotalErrors_Object = MibTableColumn
deprRptrMonitorGroupTotalErrors = _DeprRptrMonitorGroupTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 2, 1, 1, 4),
    _DeprRptrMonitorGroupTotalErrors_Type()
)
deprRptrMonitorGroupTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorGroupTotalErrors.setStatus("deprecated")
_DeprRptrMonitorPortInfo_ObjectIdentity = ObjectIdentity
deprRptrMonitorPortInfo = _DeprRptrMonitorPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3)
)
_DeprRptrMonitorPortTable_Object = MibTable
deprRptrMonitorPortTable = _DeprRptrMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1)
)
if mibBuilder.loadTexts:
    deprRptrMonitorPortTable.setStatus("deprecated")
_DeprRptrMonitorPortEntry_Object = MibTableRow
deprRptrMonitorPortEntry = _DeprRptrMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1)
)
deprRptrMonitorPortEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "deprRptrMonitorPortGroupIndex"),
    (0, "LBHUB-FMS-MIB", "deprRptrMonitorPortIndex"),
)
if mibBuilder.loadTexts:
    deprRptrMonitorPortEntry.setStatus("deprecated")


class _DeprRptrMonitorPortGroupIndex_Type(Integer32):
    """Custom type deprRptrMonitorPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DeprRptrMonitorPortGroupIndex_Type.__name__ = "Integer32"
_DeprRptrMonitorPortGroupIndex_Object = MibTableColumn
deprRptrMonitorPortGroupIndex = _DeprRptrMonitorPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 1),
    _DeprRptrMonitorPortGroupIndex_Type()
)
deprRptrMonitorPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortGroupIndex.setStatus("deprecated")


class _DeprRptrMonitorPortIndex_Type(Integer32):
    """Custom type deprRptrMonitorPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRptrMonitorPortIndex_Type.__name__ = "Integer32"
_DeprRptrMonitorPortIndex_Object = MibTableColumn
deprRptrMonitorPortIndex = _DeprRptrMonitorPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 2),
    _DeprRptrMonitorPortIndex_Type()
)
deprRptrMonitorPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortIndex.setStatus("deprecated")
_DeprRptrMonitorPortReadableFrames_Type = Counter32
_DeprRptrMonitorPortReadableFrames_Object = MibTableColumn
deprRptrMonitorPortReadableFrames = _DeprRptrMonitorPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 3),
    _DeprRptrMonitorPortReadableFrames_Type()
)
deprRptrMonitorPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortReadableFrames.setStatus("deprecated")
_DeprRptrMonitorPortReadableOctets_Type = Counter32
_DeprRptrMonitorPortReadableOctets_Object = MibTableColumn
deprRptrMonitorPortReadableOctets = _DeprRptrMonitorPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 4),
    _DeprRptrMonitorPortReadableOctets_Type()
)
deprRptrMonitorPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortReadableOctets.setStatus("deprecated")
_DeprRptrMonitorPortFCSErrors_Type = Counter32
_DeprRptrMonitorPortFCSErrors_Object = MibTableColumn
deprRptrMonitorPortFCSErrors = _DeprRptrMonitorPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 5),
    _DeprRptrMonitorPortFCSErrors_Type()
)
deprRptrMonitorPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortFCSErrors.setStatus("deprecated")
_DeprRptrMonitorPortAlignmentErrors_Type = Counter32
_DeprRptrMonitorPortAlignmentErrors_Object = MibTableColumn
deprRptrMonitorPortAlignmentErrors = _DeprRptrMonitorPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 6),
    _DeprRptrMonitorPortAlignmentErrors_Type()
)
deprRptrMonitorPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortAlignmentErrors.setStatus("deprecated")
_DeprRptrMonitorPortFrameTooLongs_Type = Counter32
_DeprRptrMonitorPortFrameTooLongs_Object = MibTableColumn
deprRptrMonitorPortFrameTooLongs = _DeprRptrMonitorPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 7),
    _DeprRptrMonitorPortFrameTooLongs_Type()
)
deprRptrMonitorPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortFrameTooLongs.setStatus("deprecated")
_DeprRptrMonitorPortShortEvents_Type = Counter32
_DeprRptrMonitorPortShortEvents_Object = MibTableColumn
deprRptrMonitorPortShortEvents = _DeprRptrMonitorPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 8),
    _DeprRptrMonitorPortShortEvents_Type()
)
deprRptrMonitorPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortShortEvents.setStatus("deprecated")
_DeprRptrMonitorPortRunts_Type = Counter32
_DeprRptrMonitorPortRunts_Object = MibTableColumn
deprRptrMonitorPortRunts = _DeprRptrMonitorPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 9),
    _DeprRptrMonitorPortRunts_Type()
)
deprRptrMonitorPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortRunts.setStatus("deprecated")
_DeprRptrMonitorPortCollisions_Type = Counter32
_DeprRptrMonitorPortCollisions_Object = MibTableColumn
deprRptrMonitorPortCollisions = _DeprRptrMonitorPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 10),
    _DeprRptrMonitorPortCollisions_Type()
)
deprRptrMonitorPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortCollisions.setStatus("deprecated")
_DeprRptrMonitorPortLateEvents_Type = Counter32
_DeprRptrMonitorPortLateEvents_Object = MibTableColumn
deprRptrMonitorPortLateEvents = _DeprRptrMonitorPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 11),
    _DeprRptrMonitorPortLateEvents_Type()
)
deprRptrMonitorPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortLateEvents.setStatus("deprecated")
_DeprRptrMonitorPortVeryLongEvents_Type = Counter32
_DeprRptrMonitorPortVeryLongEvents_Object = MibTableColumn
deprRptrMonitorPortVeryLongEvents = _DeprRptrMonitorPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 12),
    _DeprRptrMonitorPortVeryLongEvents_Type()
)
deprRptrMonitorPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortVeryLongEvents.setStatus("deprecated")
_DeprRptrMonitorPortDataRateMismatches_Type = Counter32
_DeprRptrMonitorPortDataRateMismatches_Object = MibTableColumn
deprRptrMonitorPortDataRateMismatches = _DeprRptrMonitorPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 13),
    _DeprRptrMonitorPortDataRateMismatches_Type()
)
deprRptrMonitorPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortDataRateMismatches.setStatus("deprecated")
_DeprRptrMonitorPortAutoPartitions_Type = Counter32
_DeprRptrMonitorPortAutoPartitions_Object = MibTableColumn
deprRptrMonitorPortAutoPartitions = _DeprRptrMonitorPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 14),
    _DeprRptrMonitorPortAutoPartitions_Type()
)
deprRptrMonitorPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortAutoPartitions.setStatus("deprecated")
_DeprRptrMonitorPortTotalErrors_Type = Counter32
_DeprRptrMonitorPortTotalErrors_Object = MibTableColumn
deprRptrMonitorPortTotalErrors = _DeprRptrMonitorPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 2, 3, 1, 1, 15),
    _DeprRptrMonitorPortTotalErrors_Type()
)
deprRptrMonitorPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrMonitorPortTotalErrors.setStatus("deprecated")
_DeprRptrAddrTrackPackage_ObjectIdentity = ObjectIdentity
deprRptrAddrTrackPackage = _DeprRptrAddrTrackPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3)
)
_DeprRptrAddrTrackRptrInfo_ObjectIdentity = ObjectIdentity
deprRptrAddrTrackRptrInfo = _DeprRptrAddrTrackRptrInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 1)
)
_DeprRptrAddrTrackGroupInfo_ObjectIdentity = ObjectIdentity
deprRptrAddrTrackGroupInfo = _DeprRptrAddrTrackGroupInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 2)
)
_DeprRptrAddrTrackPortInfo_ObjectIdentity = ObjectIdentity
deprRptrAddrTrackPortInfo = _DeprRptrAddrTrackPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 3)
)
_DeprRptrAddrTrackTable_Object = MibTable
deprRptrAddrTrackTable = _DeprRptrAddrTrackTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 3, 1)
)
if mibBuilder.loadTexts:
    deprRptrAddrTrackTable.setStatus("deprecated")
_DeprRptrAddrTrackEntry_Object = MibTableRow
deprRptrAddrTrackEntry = _DeprRptrAddrTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 3, 1, 1)
)
deprRptrAddrTrackEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "deprRptrAddrTrackGroupIndex"),
    (0, "LBHUB-FMS-MIB", "deprRptrAddrTrackPortIndex"),
)
if mibBuilder.loadTexts:
    deprRptrAddrTrackEntry.setStatus("deprecated")


class _DeprRptrAddrTrackGroupIndex_Type(Integer32):
    """Custom type deprRptrAddrTrackGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_DeprRptrAddrTrackGroupIndex_Type.__name__ = "Integer32"
_DeprRptrAddrTrackGroupIndex_Object = MibTableColumn
deprRptrAddrTrackGroupIndex = _DeprRptrAddrTrackGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 3, 1, 1, 1),
    _DeprRptrAddrTrackGroupIndex_Type()
)
deprRptrAddrTrackGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrAddrTrackGroupIndex.setStatus("deprecated")


class _DeprRptrAddrTrackPortIndex_Type(Integer32):
    """Custom type deprRptrAddrTrackPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRptrAddrTrackPortIndex_Type.__name__ = "Integer32"
_DeprRptrAddrTrackPortIndex_Object = MibTableColumn
deprRptrAddrTrackPortIndex = _DeprRptrAddrTrackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 3, 1, 1, 2),
    _DeprRptrAddrTrackPortIndex_Type()
)
deprRptrAddrTrackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrAddrTrackPortIndex.setStatus("deprecated")
_DeprRptrAddrTrackLastSourceAddress_Type = PhysAddress
_DeprRptrAddrTrackLastSourceAddress_Object = MibTableColumn
deprRptrAddrTrackLastSourceAddress = _DeprRptrAddrTrackLastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 3, 1, 1, 3),
    _DeprRptrAddrTrackLastSourceAddress_Type()
)
deprRptrAddrTrackLastSourceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrAddrTrackLastSourceAddress.setStatus("deprecated")
_DeprRptrAddrTrackSourceAddrChanges_Type = Counter32
_DeprRptrAddrTrackSourceAddrChanges_Object = MibTableColumn
deprRptrAddrTrackSourceAddrChanges = _DeprRptrAddrTrackSourceAddrChanges_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 4, 3, 3, 1, 1, 4),
    _DeprRptrAddrTrackSourceAddrChanges_Type()
)
deprRptrAddrTrackSourceAddrChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRptrAddrTrackSourceAddrChanges.setStatus("deprecated")
_DeprSnmpDot3RpMauMgt_ObjectIdentity = ObjectIdentity
deprSnmpDot3RpMauMgt = _DeprSnmpDot3RpMauMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 5)
)
_DeprRpMauBasicGroup_ObjectIdentity = ObjectIdentity
deprRpMauBasicGroup = _DeprRpMauBasicGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1)
)
_DeprRpMauTable_Object = MibTable
deprRpMauTable = _DeprRpMauTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1)
)
if mibBuilder.loadTexts:
    deprRpMauTable.setStatus("deprecated")
_DeprRpMauEntry_Object = MibTableRow
deprRpMauEntry = _DeprRpMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1)
)
deprRpMauEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "deprRpMauGroupIndex"),
    (0, "LBHUB-FMS-MIB", "deprRpMauPortIndex"),
    (0, "LBHUB-FMS-MIB", "deprRpMauIndex"),
)
if mibBuilder.loadTexts:
    deprRpMauEntry.setStatus("deprecated")


class _DeprRpMauGroupIndex_Type(Integer32):
    """Custom type deprRpMauGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRpMauGroupIndex_Type.__name__ = "Integer32"
_DeprRpMauGroupIndex_Object = MibTableColumn
deprRpMauGroupIndex = _DeprRpMauGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 1),
    _DeprRpMauGroupIndex_Type()
)
deprRpMauGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauGroupIndex.setStatus("deprecated")


class _DeprRpMauPortIndex_Type(Integer32):
    """Custom type deprRpMauPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRpMauPortIndex_Type.__name__ = "Integer32"
_DeprRpMauPortIndex_Object = MibTableColumn
deprRpMauPortIndex = _DeprRpMauPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 2),
    _DeprRpMauPortIndex_Type()
)
deprRpMauPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauPortIndex.setStatus("deprecated")


class _DeprRpMauIndex_Type(Integer32):
    """Custom type deprRpMauIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DeprRpMauIndex_Type.__name__ = "Integer32"
_DeprRpMauIndex_Object = MibTableColumn
deprRpMauIndex = _DeprRpMauIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 3),
    _DeprRpMauIndex_Type()
)
deprRpMauIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauIndex.setStatus("deprecated")


class _DeprRpMauType_Type(Integer32):
    """Custom type deprRpMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              7,
              8,
              9,
              10,
              14,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("aui", 7),
          ("foirl", 9),
          ("other", 1),
          ("tenbase2", 10),
          ("tenbase5", 8),
          ("tenbaseFB", 17),
          ("tenbaseFL", 18),
          ("tenbaseFP", 16),
          ("tenbaseT", 14),
          ("unknown", 2))
    )


_DeprRpMauType_Type.__name__ = "Integer32"
_DeprRpMauType_Object = MibTableColumn
deprRpMauType = _DeprRpMauType_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 4),
    _DeprRpMauType_Type()
)
deprRpMauType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauType.setStatus("deprecated")


class _DeprRpMauAdminState_Type(Integer32):
    """Custom type deprRpMauAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("operational", 3),
          ("other", 1),
          ("reset", 6),
          ("shutdown", 5),
          ("standby", 4),
          ("unknown", 2))
    )


_DeprRpMauAdminState_Type.__name__ = "Integer32"
_DeprRpMauAdminState_Object = MibTableColumn
deprRpMauAdminState = _DeprRpMauAdminState_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 5),
    _DeprRpMauAdminState_Type()
)
deprRpMauAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deprRpMauAdminState.setStatus("deprecated")


class _DeprRpMauMediaAvailable_Type(Integer32):
    """Custom type deprRpMauMediaAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("invalidSignal", 6),
          ("notPresent", 4),
          ("other", 1),
          ("present", 3),
          ("remoteFault", 5),
          ("unknown", 2))
    )


_DeprRpMauMediaAvailable_Type.__name__ = "Integer32"
_DeprRpMauMediaAvailable_Object = MibTableColumn
deprRpMauMediaAvailable = _DeprRpMauMediaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 6),
    _DeprRpMauMediaAvailable_Type()
)
deprRpMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauMediaAvailable.setStatus("deprecated")
_DeprRpMauLostMedias_Type = Counter32
_DeprRpMauLostMedias_Object = MibTableColumn
deprRpMauLostMedias = _DeprRpMauLostMedias_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 7),
    _DeprRpMauLostMedias_Type()
)
deprRpMauLostMedias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauLostMedias.setStatus("deprecated")


class _DeprRpMauJabberState_Type(Integer32):
    """Custom type deprRpMauJabberState based on Integer32"""
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
        *(("jabbering", 4),
          ("noJabber", 3),
          ("other", 1),
          ("unknown", 2))
    )


_DeprRpMauJabberState_Type.__name__ = "Integer32"
_DeprRpMauJabberState_Object = MibTableColumn
deprRpMauJabberState = _DeprRpMauJabberState_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 8),
    _DeprRpMauJabberState_Type()
)
deprRpMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauJabberState.setStatus("deprecated")
_DeprRpMauJabbers_Type = Counter32
_DeprRpMauJabbers_Object = MibTableColumn
deprRpMauJabbers = _DeprRpMauJabbers_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 5, 1, 1, 1, 9),
    _DeprRpMauJabbers_Type()
)
deprRpMauJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deprRpMauJabbers.setStatus("deprecated")
_LinkbuilderMonitorMacPackage_ObjectIdentity = ObjectIdentity
linkbuilderMonitorMacPackage = _LinkbuilderMonitorMacPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 8, 6)
)
_VmMacMonitorTable_Object = MibTable
vmMacMonitorTable = _VmMacMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1)
)
if mibBuilder.loadTexts:
    vmMacMonitorTable.setStatus("deprecated")
_VmMacMonitorEntry_Object = MibTableRow
vmMacMonitorEntry = _VmMacMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1)
)
vmMacMonitorEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "vmMacMonitorIndex"),
)
if mibBuilder.loadTexts:
    vmMacMonitorEntry.setStatus("deprecated")


class _VmMacMonitorIndex_Type(Integer32):
    """Custom type vmMacMonitorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VmMacMonitorIndex_Type.__name__ = "Integer32"
_VmMacMonitorIndex_Object = MibTableColumn
vmMacMonitorIndex = _VmMacMonitorIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 1),
    _VmMacMonitorIndex_Type()
)
vmMacMonitorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorIndex.setStatus("deprecated")
_VmMacMonitorMissErrors_Type = Counter32
_VmMacMonitorMissErrors_Object = MibTableColumn
vmMacMonitorMissErrors = _VmMacMonitorMissErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 2),
    _VmMacMonitorMissErrors_Type()
)
vmMacMonitorMissErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorMissErrors.setStatus("deprecated")
_VmMacMonitorBabbleErrors_Type = Counter32
_VmMacMonitorBabbleErrors_Object = MibTableColumn
vmMacMonitorBabbleErrors = _VmMacMonitorBabbleErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 3),
    _VmMacMonitorBabbleErrors_Type()
)
vmMacMonitorBabbleErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorBabbleErrors.setStatus("deprecated")
_VmMacMonitorMemoryErrors_Type = Counter32
_VmMacMonitorMemoryErrors_Object = MibTableColumn
vmMacMonitorMemoryErrors = _VmMacMonitorMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 4),
    _VmMacMonitorMemoryErrors_Type()
)
vmMacMonitorMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorMemoryErrors.setStatus("deprecated")
_VmMacMonitorFCSErrors_Type = Counter32
_VmMacMonitorFCSErrors_Object = MibTableColumn
vmMacMonitorFCSErrors = _VmMacMonitorFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 5),
    _VmMacMonitorFCSErrors_Type()
)
vmMacMonitorFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorFCSErrors.setStatus("deprecated")
_VmMacMonitorOverflowErrors_Type = Counter32
_VmMacMonitorOverflowErrors_Object = MibTableColumn
vmMacMonitorOverflowErrors = _VmMacMonitorOverflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 6),
    _VmMacMonitorOverflowErrors_Type()
)
vmMacMonitorOverflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorOverflowErrors.setStatus("deprecated")
_VmMacMonitorFramingErrors_Type = Counter32
_VmMacMonitorFramingErrors_Object = MibTableColumn
vmMacMonitorFramingErrors = _VmMacMonitorFramingErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 7),
    _VmMacMonitorFramingErrors_Type()
)
vmMacMonitorFramingErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorFramingErrors.setStatus("deprecated")
_VmMacMonitorRetryErrors_Type = Counter32
_VmMacMonitorRetryErrors_Object = MibTableColumn
vmMacMonitorRetryErrors = _VmMacMonitorRetryErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 8),
    _VmMacMonitorRetryErrors_Type()
)
vmMacMonitorRetryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorRetryErrors.setStatus("deprecated")
_VmMacMonitorLateEvents_Type = Counter32
_VmMacMonitorLateEvents_Object = MibTableColumn
vmMacMonitorLateEvents = _VmMacMonitorLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 9),
    _VmMacMonitorLateEvents_Type()
)
vmMacMonitorLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorLateEvents.setStatus("deprecated")
_VmMacMonitorLCarErrors_Type = Counter32
_VmMacMonitorLCarErrors_Object = MibTableColumn
vmMacMonitorLCarErrors = _VmMacMonitorLCarErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 10),
    _VmMacMonitorLCarErrors_Type()
)
vmMacMonitorLCarErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorLCarErrors.setStatus("deprecated")
_VmMacMonitorUnderflowErrors_Type = Counter32
_VmMacMonitorUnderflowErrors_Object = MibTableColumn
vmMacMonitorUnderflowErrors = _VmMacMonitorUnderflowErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 8, 6, 1, 1, 11),
    _VmMacMonitorUnderflowErrors_Type()
)
vmMacMonitorUnderflowErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMacMonitorUnderflowErrors.setStatus("deprecated")
_LinkBuilderECS_mib_ObjectIdentity = ObjectIdentity
linkBuilderECS_mib = _LinkBuilderECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 9)
)
_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10)
)
_GenExperimental_ObjectIdentity = ObjectIdentity
genExperimental = _GenExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1)
)
_TestData_ObjectIdentity = ObjectIdentity
testData = _TestData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 1)
)
_IfExtensions_ObjectIdentity = ObjectIdentity
ifExtensions = _IfExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 2)
)
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2)
)
_SetupGeneral_ObjectIdentity = ObjectIdentity
setupGeneral = _SetupGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 1)
)


class _HeartbeatInterval_Type(Integer32):
    """Custom type heartbeatInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HeartbeatInterval_Type.__name__ = "Integer32"
_HeartbeatInterval_Object = MibScalar
heartbeatInterval = _HeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 1, 1),
    _HeartbeatInterval_Type()
)
heartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    heartbeatInterval.setStatus("mandatory")
_SetupIp_ObjectIdentity = ObjectIdentity
setupIp = _SetupIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2)
)
_SetIpIfTable_Object = MibTable
setIpIfTable = _SetIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1)
)
if mibBuilder.loadTexts:
    setIpIfTable.setStatus("mandatory")
_SetIpIfEntry_Object = MibTableRow
setIpIfEntry = _SetIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1)
)
setIpIfEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "setIpIfIndex"),
)
if mibBuilder.loadTexts:
    setIpIfEntry.setStatus("mandatory")
_SetIpIfIndex_Type = Integer32
_SetIpIfIndex_Object = MibTableColumn
setIpIfIndex = _SetIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1, 1),
    _SetIpIfIndex_Type()
)
setIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setIpIfIndex.setStatus("mandatory")
_SetIpIfAddr_Type = IpAddress
_SetIpIfAddr_Object = MibTableColumn
setIpIfAddr = _SetIpIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1, 2),
    _SetIpIfAddr_Type()
)
setIpIfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpIfAddr.setStatus("mandatory")
_SetIpIfMask_Type = IpAddress
_SetIpIfMask_Object = MibTableColumn
setIpIfMask = _SetIpIfMask_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 1, 1, 3),
    _SetIpIfMask_Type()
)
setIpIfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpIfMask.setStatus("mandatory")
_SetIpIfRouter_Type = IpAddress
_SetIpIfRouter_Object = MibScalar
setIpIfRouter = _SetIpIfRouter_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 2, 2),
    _SetIpIfRouter_Type()
)
setIpIfRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setIpIfRouter.setStatus("mandatory")
_SetupStart_ObjectIdentity = ObjectIdentity
setupStart = _SetupStart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3)
)


class _StartPROMSwVerNo_Type(DisplayString):
    """Custom type startPROMSwVerNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_StartPROMSwVerNo_Type.__name__ = "DisplayString"
_StartPROMSwVerNo_Object = MibScalar
startPROMSwVerNo = _StartPROMSwVerNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 1),
    _StartPROMSwVerNo_Type()
)
startPROMSwVerNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startPROMSwVerNo.setStatus("mandatory")
_StartRestartCount_Type = Counter32
_StartRestartCount_Object = MibScalar
startRestartCount = _StartRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 2),
    _StartRestartCount_Type()
)
startRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startRestartCount.setStatus("mandatory")


class _StartLastRestartType_Type(Integer32):
    """Custom type startLastRestartType based on Integer32"""
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
        *(("command", 2),
          ("other", 1),
          ("power-reset", 4),
          ("system-error", 5),
          ("watchdog", 3))
    )


_StartLastRestartType_Type.__name__ = "Integer32"
_StartLastRestartType_Object = MibScalar
startLastRestartType = _StartLastRestartType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 3),
    _StartLastRestartType_Type()
)
startLastRestartType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startLastRestartType.setStatus("mandatory")


class _StartResetAction_Type(Integer32):
    """Custom type startResetAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manDefaultReset", 2),
          ("nochange", 1))
    )


_StartResetAction_Type.__name__ = "Integer32"
_StartResetAction_Object = MibScalar
startResetAction = _StartResetAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 4),
    _StartResetAction_Type()
)
startResetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startResetAction.setStatus("mandatory")
_StartLastSystemError_Type = Integer32
_StartLastSystemError_Object = MibScalar
startLastSystemError = _StartLastSystemError_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 5),
    _StartLastSystemError_Type()
)
startLastSystemError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    startLastSystemError.setStatus("mandatory")


class _StartRestartAction_Type(Integer32):
    """Custom type startRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nochange", 1),
          ("restart", 2))
    )


_StartRestartAction_Type.__name__ = "Integer32"
_StartRestartAction_Object = MibScalar
startRestartAction = _StartRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 2, 3, 6),
    _StartRestartAction_Type()
)
startRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startRestartAction.setStatus("mandatory")
_SysLoader_ObjectIdentity = ObjectIdentity
sysLoader = _SysLoader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 3)
)
_LoadableDeviceTable_Object = MibTable
loadableDeviceTable = _LoadableDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1)
)
if mibBuilder.loadTexts:
    loadableDeviceTable.setStatus("mandatory")
_LoadableDeviceEntry_Object = MibTableRow
loadableDeviceEntry = _LoadableDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1)
)
loadableDeviceEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "slDeviceType"),
    (0, "LBHUB-FMS-MIB", "slDeviceInstance"),
)
if mibBuilder.loadTexts:
    loadableDeviceEntry.setStatus("mandatory")


class _SlDeviceType_Type(Integer32):
    """Custom type slDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("component", 2),
          ("system", 1))
    )


_SlDeviceType_Type.__name__ = "Integer32"
_SlDeviceType_Object = MibTableColumn
slDeviceType = _SlDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 1),
    _SlDeviceType_Type()
)
slDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDeviceType.setStatus("mandatory")
_SlDeviceInstance_Type = Integer32
_SlDeviceInstance_Object = MibTableColumn
slDeviceInstance = _SlDeviceInstance_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 2),
    _SlDeviceInstance_Type()
)
slDeviceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slDeviceInstance.setStatus("mandatory")


class _SlLoadStatus_Type(Integer32):
    """Custom type slLoadStatus based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
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
              200,
              201,
              202,
              203,
              204,
              205,
              255)
        )
    )
    namedValues = NamedValues(
        *(("accessViolation", 2),
          ("byteCountError", 16),
          ("checksumError", 12),
          ("eraseFailed", 18),
          ("fileNotFound", 1),
          ("illegalOperation", 4),
          ("invalidProgAddress", 17),
          ("invalidRecType", 11),
          ("loadActive", 21),
          ("loadPending", 20),
          ("modBusy", 203),
          ("modChecksumError", 201),
          ("modFailure", 255),
          ("modInvalidAdress", 200),
          ("modNoResource", 205),
          ("modRemoved", 204),
          ("modTimeout", 202),
          ("noFileHeader", 15),
          ("noResource", 9),
          ("noResponse", 8),
          ("noSuchUser", 7),
          ("paused", 23),
          ("progFailed", 19),
          ("recLenMismatch", 10),
          ("success", 22),
          ("unknownTransferID", 5),
          ("wrongDevice", 13),
          ("wrongHardwareVersion", 14))
    )


_SlLoadStatus_Type.__name__ = "Integer32"
_SlLoadStatus_Object = MibTableColumn
slLoadStatus = _SlLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 3),
    _SlLoadStatus_Type()
)
slLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slLoadStatus.setStatus("mandatory")


class _SlSoftwareVersion_Type(DisplayString):
    """Custom type slSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SlSoftwareVersion_Type.__name__ = "DisplayString"
_SlSoftwareVersion_Object = MibTableColumn
slSoftwareVersion = _SlSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 4),
    _SlSoftwareVersion_Type()
)
slSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slSoftwareVersion.setStatus("mandatory")
_SlHardwareVersion_Type = Integer32
_SlHardwareVersion_Object = MibTableColumn
slHardwareVersion = _SlHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 5),
    _SlHardwareVersion_Type()
)
slHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slHardwareVersion.setStatus("mandatory")


class _SlFilename_Type(DisplayString):
    """Custom type slFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_SlFilename_Type.__name__ = "DisplayString"
_SlFilename_Object = MibTableColumn
slFilename = _SlFilename_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 6),
    _SlFilename_Type()
)
slFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slFilename.setStatus("mandatory")


class _SlServerIpAddress_Type(IpAddress):
    """Custom type slServerIpAddress based on IpAddress"""
    defaultValue = 0


_SlServerIpAddress_Object = MibTableColumn
slServerIpAddress = _SlServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 7),
    _SlServerIpAddress_Type()
)
slServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slServerIpAddress.setStatus("deprecated")


class _SlLoad_Type(Integer32):
    """Custom type slLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("startDownload", 2))
    )


_SlLoad_Type.__name__ = "Integer32"
_SlLoad_Object = MibTableColumn
slLoad = _SlLoad_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 8),
    _SlLoad_Type()
)
slLoad.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    slLoad.setStatus("mandatory")


class _SlServerAddress_Type(DisplayString):
    """Custom type slServerAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SlServerAddress_Type.__name__ = "DisplayString"
_SlServerAddress_Object = MibTableColumn
slServerAddress = _SlServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 9),
    _SlServerAddress_Type()
)
slServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slServerAddress.setStatus("mandatory")


class _SlServerProtocol_Type(Integer32):
    """Custom type slServerProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp-ip", 2),
          ("tftp-ipx", 3),
          ("unknown", 1))
    )


_SlServerProtocol_Type.__name__ = "Integer32"
_SlServerProtocol_Object = MibTableColumn
slServerProtocol = _SlServerProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 3, 1, 1, 10),
    _SlServerProtocol_Type()
)
slServerProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slServerProtocol.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 4)
)
_SecurityEnableTable_Object = MibTable
securityEnableTable = _SecurityEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1)
)
if mibBuilder.loadTexts:
    securityEnableTable.setStatus("mandatory")
_SecurityEnableTableEntry_Object = MibTableRow
securityEnableTableEntry = _SecurityEnableTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1)
)
securityEnableTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "securityLevel"),
)
if mibBuilder.loadTexts:
    securityEnableTableEntry.setStatus("mandatory")


class _SecurityLevel_Type(Integer32):
    """Custom type securityLevel based on Integer32"""
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
        *(("manager", 3),
          ("monitor", 1),
          ("secureMonitor", 2),
          ("security", 5),
          ("specialist", 4))
    )


_SecurityLevel_Type.__name__ = "Integer32"
_SecurityLevel_Object = MibTableColumn
securityLevel = _SecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 1),
    _SecurityLevel_Type()
)
securityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityLevel.setStatus("mandatory")


class _SecurityCommunityEnable_Type(Integer32):
    """Custom type securityCommunityEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityCommunityEnable_Type.__name__ = "Integer32"
_SecurityCommunityEnable_Object = MibTableColumn
securityCommunityEnable = _SecurityCommunityEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 2),
    _SecurityCommunityEnable_Type()
)
securityCommunityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityCommunityEnable.setStatus("mandatory")


class _SecuritySecureEnable_Type(Integer32):
    """Custom type securitySecureEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecuritySecureEnable_Type.__name__ = "Integer32"
_SecuritySecureEnable_Object = MibTableColumn
securitySecureEnable = _SecuritySecureEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 3),
    _SecuritySecureEnable_Type()
)
securitySecureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securitySecureEnable.setStatus("mandatory")


class _SecurityTermEnable_Type(Integer32):
    """Custom type securityTermEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityTermEnable_Type.__name__ = "Integer32"
_SecurityTermEnable_Object = MibTableColumn
securityTermEnable = _SecurityTermEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 4),
    _SecurityTermEnable_Type()
)
securityTermEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityTermEnable.setStatus("mandatory")


class _SecurityTelnetEnable_Type(Integer32):
    """Custom type securityTelnetEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityTelnetEnable_Type.__name__ = "Integer32"
_SecurityTelnetEnable_Object = MibTableColumn
securityTelnetEnable = _SecurityTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 5),
    _SecurityTelnetEnable_Type()
)
securityTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityTelnetEnable.setStatus("mandatory")


class _SecurityFrontPanelEnable_Type(Integer32):
    """Custom type securityFrontPanelEnable based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("permanentlyDisabled", 4),
          ("permanentlyEnabled", 3))
    )


_SecurityFrontPanelEnable_Type.__name__ = "Integer32"
_SecurityFrontPanelEnable_Object = MibTableColumn
securityFrontPanelEnable = _SecurityFrontPanelEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 1, 1, 6),
    _SecurityFrontPanelEnable_Type()
)
securityFrontPanelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityFrontPanelEnable.setStatus("mandatory")
_SecurityUserTable_Object = MibTable
securityUserTable = _SecurityUserTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2)
)
if mibBuilder.loadTexts:
    securityUserTable.setStatus("mandatory")
_SecurityUserTableEntry_Object = MibTableRow
securityUserTableEntry = _SecurityUserTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1)
)
securityUserTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "securityUserName"),
)
if mibBuilder.loadTexts:
    securityUserTableEntry.setStatus("mandatory")


class _SecurityUserStatus_Type(Integer32):
    """Custom type securityUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SecurityUserStatus_Type.__name__ = "Integer32"
_SecurityUserStatus_Object = MibTableColumn
securityUserStatus = _SecurityUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 1),
    _SecurityUserStatus_Type()
)
securityUserStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserStatus.setStatus("mandatory")


class _SecurityUserName_Type(DisplayString):
    """Custom type securityUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_SecurityUserName_Type.__name__ = "DisplayString"
_SecurityUserName_Object = MibTableColumn
securityUserName = _SecurityUserName_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 2),
    _SecurityUserName_Type()
)
securityUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityUserName.setStatus("mandatory")


class _SecurityUserLevel_Type(Integer32):
    """Custom type securityUserLevel based on Integer32"""
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
        *(("manager", 3),
          ("monitor", 1),
          ("secureMonitor", 2),
          ("security", 5),
          ("specialist", 4))
    )


_SecurityUserLevel_Type.__name__ = "Integer32"
_SecurityUserLevel_Object = MibTableColumn
securityUserLevel = _SecurityUserLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 3),
    _SecurityUserLevel_Type()
)
securityUserLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserLevel.setStatus("mandatory")


class _SecurityUserPassword_Type(DisplayString):
    """Custom type securityUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SecurityUserPassword_Type.__name__ = "DisplayString"
_SecurityUserPassword_Object = MibTableColumn
securityUserPassword = _SecurityUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 4),
    _SecurityUserPassword_Type()
)
securityUserPassword.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    securityUserPassword.setStatus("mandatory")


class _SecurityUserCommunity_Type(DisplayString):
    """Custom type securityUserCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SecurityUserCommunity_Type.__name__ = "DisplayString"
_SecurityUserCommunity_Object = MibTableColumn
securityUserCommunity = _SecurityUserCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 5),
    _SecurityUserCommunity_Type()
)
securityUserCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserCommunity.setStatus("mandatory")
_SecurityUserLocParty_Type = ObjectIdentifier
_SecurityUserLocParty_Object = MibTableColumn
securityUserLocParty = _SecurityUserLocParty_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 6),
    _SecurityUserLocParty_Type()
)
securityUserLocParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserLocParty.setStatus("mandatory")
_SecurityUserMgrParty_Type = ObjectIdentifier
_SecurityUserMgrParty_Object = MibTableColumn
securityUserMgrParty = _SecurityUserMgrParty_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 2, 1, 7),
    _SecurityUserMgrParty_Type()
)
securityUserMgrParty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityUserMgrParty.setStatus("mandatory")
_SecurityAuditLogTable_Object = MibTable
securityAuditLogTable = _SecurityAuditLogTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3)
)
if mibBuilder.loadTexts:
    securityAuditLogTable.setStatus("mandatory")
_SecurityAuditLogEntry_Object = MibTableRow
securityAuditLogEntry = _SecurityAuditLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1)
)
securityAuditLogEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "securityAuditIndex"),
)
if mibBuilder.loadTexts:
    securityAuditLogEntry.setStatus("mandatory")


class _SecurityAuditIndex_Type(Integer32):
    """Custom type securityAuditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SecurityAuditIndex_Type.__name__ = "Integer32"
_SecurityAuditIndex_Object = MibTableColumn
securityAuditIndex = _SecurityAuditIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 1),
    _SecurityAuditIndex_Type()
)
securityAuditIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditIndex.setStatus("mandatory")
_SecurityAuditTime_Type = TimeTicks
_SecurityAuditTime_Object = MibTableColumn
securityAuditTime = _SecurityAuditTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 2),
    _SecurityAuditTime_Type()
)
securityAuditTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditTime.setStatus("mandatory")


class _SecurityAuditUser_Type(DisplayString):
    """Custom type securityAuditUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SecurityAuditUser_Type.__name__ = "DisplayString"
_SecurityAuditUser_Object = MibTableColumn
securityAuditUser = _SecurityAuditUser_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 3),
    _SecurityAuditUser_Type()
)
securityAuditUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditUser.setStatus("mandatory")
_SecurityAuditObject_Type = ObjectIdentifier
_SecurityAuditObject_Object = MibTableColumn
securityAuditObject = _SecurityAuditObject_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 4),
    _SecurityAuditObject_Type()
)
securityAuditObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditObject.setStatus("mandatory")


class _SecurityAuditValue_Type(OctetString):
    """Custom type securityAuditValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_SecurityAuditValue_Type.__name__ = "OctetString"
_SecurityAuditValue_Object = MibTableColumn
securityAuditValue = _SecurityAuditValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 5),
    _SecurityAuditValue_Type()
)
securityAuditValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditValue.setStatus("mandatory")


class _SecurityAuditResult_Type(Integer32):
    """Custom type securityAuditResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              255)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("locked", 4),
          ("no-such-function", 6),
          ("no-such-item", 7),
          ("pending", 1),
          ("security-violation", 5),
          ("success", 255),
          ("too-big", 2))
    )


_SecurityAuditResult_Type.__name__ = "Integer32"
_SecurityAuditResult_Object = MibTableColumn
securityAuditResult = _SecurityAuditResult_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 4, 3, 1, 6),
    _SecurityAuditResult_Type()
)
securityAuditResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityAuditResult.setStatus("mandatory")
_Gauges_ObjectIdentity = ObjectIdentity
gauges = _Gauges_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 5)
)
_GaugeTable_Object = MibTable
gaugeTable = _GaugeTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1)
)
if mibBuilder.loadTexts:
    gaugeTable.setStatus("mandatory")
_GaugeTableEntry_Object = MibTableRow
gaugeTableEntry = _GaugeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1)
)
gaugeTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "gaugeIndex"),
)
if mibBuilder.loadTexts:
    gaugeTableEntry.setStatus("mandatory")
_GaugeIndex_Type = Integer32
_GaugeIndex_Object = MibTableColumn
gaugeIndex = _GaugeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 1),
    _GaugeIndex_Type()
)
gaugeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gaugeIndex.setStatus("mandatory")
_GaugeItemId_Type = ObjectIdentifier
_GaugeItemId_Object = MibTableColumn
gaugeItemId = _GaugeItemId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 2),
    _GaugeItemId_Type()
)
gaugeItemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeItemId.setStatus("mandatory")


class _GaugeItemType_Type(Integer32):
    """Custom type gaugeItemType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("counter", 1),
          ("signedMeter", 2),
          ("unsignedMeter", 3))
    )


_GaugeItemType_Type.__name__ = "Integer32"
_GaugeItemType_Object = MibTableColumn
gaugeItemType = _GaugeItemType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 3),
    _GaugeItemType_Type()
)
gaugeItemType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeItemType.setStatus("mandatory")


class _GaugeSamplesPerAverage_Type(Integer32):
    """Custom type gaugeSamplesPerAverage based on Integer32"""
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
        *(("maxSamples", 4),
          ("nonAveraging", 1),
          ("threeSamples", 3),
          ("twoSamples", 2))
    )


_GaugeSamplesPerAverage_Type.__name__ = "Integer32"
_GaugeSamplesPerAverage_Object = MibTableColumn
gaugeSamplesPerAverage = _GaugeSamplesPerAverage_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 4),
    _GaugeSamplesPerAverage_Type()
)
gaugeSamplesPerAverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeSamplesPerAverage.setStatus("mandatory")


class _GaugeSamplePeriod_Type(Integer32):
    """Custom type gaugeSamplePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GaugeSamplePeriod_Type.__name__ = "Integer32"
_GaugeSamplePeriod_Object = MibTableColumn
gaugeSamplePeriod = _GaugeSamplePeriod_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 5),
    _GaugeSamplePeriod_Type()
)
gaugeSamplePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeSamplePeriod.setStatus("mandatory")


class _GaugeValue_Type(Integer32):
    """Custom type gaugeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GaugeValue_Type.__name__ = "Integer32"
_GaugeValue_Object = MibTableColumn
gaugeValue = _GaugeValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 6),
    _GaugeValue_Type()
)
gaugeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeValue.setStatus("mandatory")


class _GaugePeakValue_Type(Integer32):
    """Custom type gaugePeakValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GaugePeakValue_Type.__name__ = "Integer32"
_GaugePeakValue_Object = MibTableColumn
gaugePeakValue = _GaugePeakValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 7),
    _GaugePeakValue_Type()
)
gaugePeakValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugePeakValue.setStatus("mandatory")


class _GaugeThresholdLevel_Type(Integer32):
    """Custom type gaugeThresholdLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_GaugeThresholdLevel_Type.__name__ = "Integer32"
_GaugeThresholdLevel_Object = MibTableColumn
gaugeThresholdLevel = _GaugeThresholdLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 8),
    _GaugeThresholdLevel_Type()
)
gaugeThresholdLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeThresholdLevel.setStatus("mandatory")
_GaugeRecoveryLevel_Type = Integer32
_GaugeRecoveryLevel_Object = MibTableColumn
gaugeRecoveryLevel = _GaugeRecoveryLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 9),
    _GaugeRecoveryLevel_Type()
)
gaugeRecoveryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeRecoveryLevel.setStatus("mandatory")


class _GaugeThresholdAction_Type(Integer32):
    """Custom type gaugeThresholdAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              8,
              9,
              12,
              13,
              14,
              15,
              18,
              19,
              20,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("blipCardOff", 13),
          ("blipPortOff", 12),
          ("disable", 3),
          ("disableCard", 15),
          ("disablePort", 14),
          ("enable", 4),
          ("noAction", 1),
          ("notifyAndBlipCardOff", 6),
          ("notifyAndBlipPortOff", 5),
          ("notifyAndDisableCard", 9),
          ("notifyAndDisablePort", 8),
          ("notifyAndResilientSwitch", 18),
          ("notifyBandwidthExceeded", 19),
          ("notifyErrorsExceeded", 20),
          ("notifyFilterBridgePort", 23),
          ("notifyPollFailed", 22),
          ("sendTrap", 2))
    )


_GaugeThresholdAction_Type.__name__ = "Integer32"
_GaugeThresholdAction_Object = MibTableColumn
gaugeThresholdAction = _GaugeThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 10),
    _GaugeThresholdAction_Type()
)
gaugeThresholdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeThresholdAction.setStatus("mandatory")


class _GaugeRecoveryAction_Type(Integer32):
    """Custom type gaugeRecoveryAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              10,
              11,
              16,
              17,
              21,
              24)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 4),
          ("enableCard", 17),
          ("enablePort", 16),
          ("noAction", 1),
          ("notifyAndEnableCard", 11),
          ("notifyAndEnablePort", 10),
          ("notifyPollSuccess", 21),
          ("notifyUnfilterBridgePort", 24),
          ("sendTrap", 2))
    )


_GaugeRecoveryAction_Type.__name__ = "Integer32"
_GaugeRecoveryAction_Object = MibTableColumn
gaugeRecoveryAction = _GaugeRecoveryAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 11),
    _GaugeRecoveryAction_Type()
)
gaugeRecoveryAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeRecoveryAction.setStatus("mandatory")


class _GaugeState_Type(Integer32):
    """Custom type gaugeState based on Integer32"""
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
        *(("autoCalibrate", 5),
          ("deleted", 4),
          ("off", 3),
          ("onTriggersDisabled", 2),
          ("onTriggersEnabled", 1))
    )


_GaugeState_Type.__name__ = "Integer32"
_GaugeState_Object = MibTableColumn
gaugeState = _GaugeState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 12),
    _GaugeState_Type()
)
gaugeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeState.setStatus("mandatory")
_GaugeOwner_Type = DisplayString
_GaugeOwner_Object = MibTableColumn
gaugeOwner = _GaugeOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 1, 1, 13),
    _GaugeOwner_Type()
)
gaugeOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeOwner.setStatus("mandatory")


class _GaugeTableSize_Type(Integer32):
    """Custom type gaugeTableSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GaugeTableSize_Type.__name__ = "Integer32"
_GaugeTableSize_Object = MibScalar
gaugeTableSize = _GaugeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 2),
    _GaugeTableSize_Type()
)
gaugeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gaugeTableSize.setStatus("mandatory")


class _GaugeThresholdLevelScaler_Type(Integer32):
    """Custom type gaugeThresholdLevelScaler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GaugeThresholdLevelScaler_Type.__name__ = "Integer32"
_GaugeThresholdLevelScaler_Object = MibScalar
gaugeThresholdLevelScaler = _GaugeThresholdLevelScaler_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 3),
    _GaugeThresholdLevelScaler_Type()
)
gaugeThresholdLevelScaler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeThresholdLevelScaler.setStatus("mandatory")


class _GaugeRecoveryLevelScaler_Type(Integer32):
    """Custom type gaugeRecoveryLevelScaler based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_GaugeRecoveryLevelScaler_Type.__name__ = "Integer32"
_GaugeRecoveryLevelScaler_Object = MibScalar
gaugeRecoveryLevelScaler = _GaugeRecoveryLevelScaler_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 4),
    _GaugeRecoveryLevelScaler_Type()
)
gaugeRecoveryLevelScaler.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gaugeRecoveryLevelScaler.setStatus("mandatory")


class _GaugeTableUpdate_Type(Integer32):
    """Custom type gaugeTableUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteAll", 1)
    )


_GaugeTableUpdate_Type.__name__ = "Integer32"
_GaugeTableUpdate_Object = MibScalar
gaugeTableUpdate = _GaugeTableUpdate_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 5),
    _GaugeTableUpdate_Type()
)
gaugeTableUpdate.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeTableUpdate.setStatus("mandatory")
_GaugeConfigureObjId_Type = ObjectIdentifier
_GaugeConfigureObjId_Object = MibScalar
gaugeConfigureObjId = _GaugeConfigureObjId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 6),
    _GaugeConfigureObjId_Type()
)
gaugeConfigureObjId.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeConfigureObjId.setStatus("mandatory")


class _GaugeConfigureColumn_Type(Integer32):
    """Custom type gaugeConfigureColumn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("gaugeState", 8),
          ("itemType", 1),
          ("recoveryAction", 7),
          ("recoveryLevel", 5),
          ("samplePeriod", 3),
          ("samplesPerAverage", 2),
          ("thresholdAction", 6),
          ("thresholdLevel", 4))
    )


_GaugeConfigureColumn_Type.__name__ = "Integer32"
_GaugeConfigureColumn_Object = MibScalar
gaugeConfigureColumn = _GaugeConfigureColumn_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 7),
    _GaugeConfigureColumn_Type()
)
gaugeConfigureColumn.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeConfigureColumn.setStatus("mandatory")


class _GaugeConfigureValue_Type(Integer32):
    """Custom type gaugeConfigureValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_GaugeConfigureValue_Type.__name__ = "Integer32"
_GaugeConfigureValue_Object = MibScalar
gaugeConfigureValue = _GaugeConfigureValue_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 8),
    _GaugeConfigureValue_Type()
)
gaugeConfigureValue.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    gaugeConfigureValue.setStatus("mandatory")
_GaugeNextFreeIndex_Type = Integer32
_GaugeNextFreeIndex_Object = MibScalar
gaugeNextFreeIndex = _GaugeNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 5, 9),
    _GaugeNextFreeIndex_Type()
)
gaugeNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gaugeNextFreeIndex.setStatus("mandatory")
_AsciiAgent_ObjectIdentity = ObjectIdentity
asciiAgent = _AsciiAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 6)
)
_AscTimeAttemptedLogin_Type = TimeTicks
_AscTimeAttemptedLogin_Object = MibScalar
ascTimeAttemptedLogin = _AscTimeAttemptedLogin_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 1),
    _AscTimeAttemptedLogin_Type()
)
ascTimeAttemptedLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascTimeAttemptedLogin.setStatus("mandatory")


class _AscUserNameForLastAttemptedLogin_Type(DisplayString):
    """Custom type ascUserNameForLastAttemptedLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AscUserNameForLastAttemptedLogin_Type.__name__ = "DisplayString"
_AscUserNameForLastAttemptedLogin_Object = MibScalar
ascUserNameForLastAttemptedLogin = _AscUserNameForLastAttemptedLogin_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 2),
    _AscUserNameForLastAttemptedLogin_Type()
)
ascUserNameForLastAttemptedLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascUserNameForLastAttemptedLogin.setStatus("mandatory")


class _AscLoginStatus_Type(Integer32):
    """Custom type ascLoginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("deniedAccessFromSerialPort", 4),
          ("deniedAccessFromTelnet", 3),
          ("incorrectPasswordFromSerialPort", 8),
          ("incorrectPasswordFromTelnet", 7),
          ("loginOKFromSerialPort", 2),
          ("loginOKFromTelnet", 1),
          ("nologin", 11),
          ("securityViolationFromSerialPort", 10),
          ("securityViolationFromTelnet", 9),
          ("unknownUserFromSerialPort", 6),
          ("unknownUserFromTelnet", 5))
    )


_AscLoginStatus_Type.__name__ = "Integer32"
_AscLoginStatus_Object = MibScalar
ascLoginStatus = _AscLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 3),
    _AscLoginStatus_Type()
)
ascLoginStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascLoginStatus.setStatus("mandatory")


class _AscLocalManagementBanner_Type(DisplayString):
    """Custom type ascLocalManagementBanner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 490),
    )


_AscLocalManagementBanner_Type.__name__ = "DisplayString"
_AscLocalManagementBanner_Object = MibScalar
ascLocalManagementBanner = _AscLocalManagementBanner_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 6, 4),
    _AscLocalManagementBanner_Type()
)
ascLocalManagementBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ascLocalManagementBanner.setStatus("mandatory")
_SerialIf_ObjectIdentity = ObjectIdentity
serialIf = _SerialIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 7)
)
_SiSlipPort_Type = Integer32
_SiSlipPort_Object = MibScalar
siSlipPort = _SiSlipPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 1),
    _SiSlipPort_Type()
)
siSlipPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siSlipPort.setStatus("mandatory")
_ConfigV24Table_Object = MibTable
configV24Table = _ConfigV24Table_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2)
)
if mibBuilder.loadTexts:
    configV24Table.setStatus("mandatory")
_ConfigV24Entry_Object = MibTableRow
configV24Entry = _ConfigV24Entry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1)
)
configV24Entry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "configV24PortID"),
)
if mibBuilder.loadTexts:
    configV24Entry.setStatus("mandatory")


class _ConfigV24PortID_Type(Integer32):
    """Custom type configV24PortID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ConfigV24PortID_Type.__name__ = "Integer32"
_ConfigV24PortID_Object = MibTableColumn
configV24PortID = _ConfigV24PortID_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 1),
    _ConfigV24PortID_Type()
)
configV24PortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configV24PortID.setStatus("mandatory")


class _ConfigV24ConnType_Type(Integer32):
    """Custom type configV24ConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_ConfigV24ConnType_Type.__name__ = "Integer32"
_ConfigV24ConnType_Object = MibTableColumn
configV24ConnType = _ConfigV24ConnType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 2),
    _ConfigV24ConnType_Type()
)
configV24ConnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24ConnType.setStatus("mandatory")


class _ConfigV24AutoConfig_Type(Integer32):
    """Custom type configV24AutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ConfigV24AutoConfig_Type.__name__ = "Integer32"
_ConfigV24AutoConfig_Object = MibTableColumn
configV24AutoConfig = _ConfigV24AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 3),
    _ConfigV24AutoConfig_Type()
)
configV24AutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24AutoConfig.setStatus("mandatory")


class _ConfigV24Speed_Type(Integer32):
    """Custom type configV24Speed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("speed1200", 4),
          ("speed19200", 8),
          ("speed2400", 5),
          ("speed38400", 9),
          ("speed4800", 6),
          ("speed9600", 7))
    )


_ConfigV24Speed_Type.__name__ = "Integer32"
_ConfigV24Speed_Object = MibTableColumn
configV24Speed = _ConfigV24Speed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 4),
    _ConfigV24Speed_Type()
)
configV24Speed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24Speed.setStatus("mandatory")


class _ConfigV24CharSize_Type(Integer32):
    """Custom type configV24CharSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("size7", 3),
          ("size8", 4))
    )


_ConfigV24CharSize_Type.__name__ = "Integer32"
_ConfigV24CharSize_Object = MibTableColumn
configV24CharSize = _ConfigV24CharSize_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 5),
    _ConfigV24CharSize_Type()
)
configV24CharSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24CharSize.setStatus("mandatory")


class _ConfigV24StopBits_Type(Integer32):
    """Custom type configV24StopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stopOne", 1),
          ("stopOneDotFive", 2),
          ("stopTwo", 3))
    )


_ConfigV24StopBits_Type.__name__ = "Integer32"
_ConfigV24StopBits_Object = MibTableColumn
configV24StopBits = _ConfigV24StopBits_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 6),
    _ConfigV24StopBits_Type()
)
configV24StopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24StopBits.setStatus("mandatory")


class _ConfigV24Parity_Type(Integer32):
    """Custom type configV24Parity based on Integer32"""
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
        *(("evenParity", 5),
          ("markParity", 3),
          ("noParity", 1),
          ("oddParity", 4),
          ("spaceParity", 2))
    )


_ConfigV24Parity_Type.__name__ = "Integer32"
_ConfigV24Parity_Object = MibTableColumn
configV24Parity = _ConfigV24Parity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 7),
    _ConfigV24Parity_Type()
)
configV24Parity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24Parity.setStatus("mandatory")


class _ConfigV24DSRControl_Type(Integer32):
    """Custom type configV24DSRControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ConfigV24DSRControl_Type.__name__ = "Integer32"
_ConfigV24DSRControl_Object = MibTableColumn
configV24DSRControl = _ConfigV24DSRControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 8),
    _ConfigV24DSRControl_Type()
)
configV24DSRControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24DSRControl.setStatus("mandatory")


class _ConfigV24DCDControl_Type(Integer32):
    """Custom type configV24DCDControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ConfigV24DCDControl_Type.__name__ = "Integer32"
_ConfigV24DCDControl_Object = MibTableColumn
configV24DCDControl = _ConfigV24DCDControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 9),
    _ConfigV24DCDControl_Type()
)
configV24DCDControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24DCDControl.setStatus("mandatory")


class _ConfigV24FlowControl_Type(Integer32):
    """Custom type configV24FlowControl based on Integer32"""
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
        *(("noFlowControl", 1),
          ("rtsCtsFullDplx", 3),
          ("rtsCtsHalfDplx", 4),
          ("xonXoff", 2))
    )


_ConfigV24FlowControl_Type.__name__ = "Integer32"
_ConfigV24FlowControl_Object = MibTableColumn
configV24FlowControl = _ConfigV24FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 10),
    _ConfigV24FlowControl_Type()
)
configV24FlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24FlowControl.setStatus("mandatory")


class _ConfigV24Update_Type(Integer32):
    """Custom type configV24Update based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nochange", 1),
          ("update", 2))
    )


_ConfigV24Update_Type.__name__ = "Integer32"
_ConfigV24Update_Object = MibTableColumn
configV24Update = _ConfigV24Update_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 7, 2, 1, 11),
    _ConfigV24Update_Type()
)
configV24Update.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configV24Update.setStatus("mandatory")
_RepeaterMgmt_ObjectIdentity = ObjectIdentity
repeaterMgmt = _RepeaterMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8)
)
_PddrmBasicPackage_ObjectIdentity = ObjectIdentity
pddrmBasicPackage = _PddrmBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 1)
)
_PddrmBasRepeaterPackage_ObjectIdentity = ObjectIdentity
pddrmBasRepeaterPackage = _PddrmBasRepeaterPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 1, 1)
)
_PddrmBasGroupPackage_ObjectIdentity = ObjectIdentity
pddrmBasGroupPackage = _PddrmBasGroupPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 1, 2)
)
_PddrmBasPortPackage_ObjectIdentity = ObjectIdentity
pddrmBasPortPackage = _PddrmBasPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 1, 3)
)
_PddrmMonitorPackage_ObjectIdentity = ObjectIdentity
pddrmMonitorPackage = _PddrmMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2)
)
_PddrmMonRepeaterPackage_ObjectIdentity = ObjectIdentity
pddrmMonRepeaterPackage = _PddrmMonRepeaterPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1)
)
_PddrmMonRepeaterReadableFrames_Type = Counter32
_PddrmMonRepeaterReadableFrames_Object = MibScalar
pddrmMonRepeaterReadableFrames = _PddrmMonRepeaterReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 1),
    _PddrmMonRepeaterReadableFrames_Type()
)
pddrmMonRepeaterReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterReadableFrames.setStatus("deprecated")
_PddrmMonRepeaterReadableOctets_Type = Counter32
_PddrmMonRepeaterReadableOctets_Object = MibScalar
pddrmMonRepeaterReadableOctets = _PddrmMonRepeaterReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 2),
    _PddrmMonRepeaterReadableOctets_Type()
)
pddrmMonRepeaterReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterReadableOctets.setStatus("deprecated")
_PddrmMonRepeaterFCSErrors_Type = Counter32
_PddrmMonRepeaterFCSErrors_Object = MibScalar
pddrmMonRepeaterFCSErrors = _PddrmMonRepeaterFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 3),
    _PddrmMonRepeaterFCSErrors_Type()
)
pddrmMonRepeaterFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterFCSErrors.setStatus("deprecated")
_PddrmMonRepeaterAlignmentErrors_Type = Counter32
_PddrmMonRepeaterAlignmentErrors_Object = MibScalar
pddrmMonRepeaterAlignmentErrors = _PddrmMonRepeaterAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 4),
    _PddrmMonRepeaterAlignmentErrors_Type()
)
pddrmMonRepeaterAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterAlignmentErrors.setStatus("deprecated")
_PddrmMonRepeaterFrameTooLongs_Type = Counter32
_PddrmMonRepeaterFrameTooLongs_Object = MibScalar
pddrmMonRepeaterFrameTooLongs = _PddrmMonRepeaterFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 5),
    _PddrmMonRepeaterFrameTooLongs_Type()
)
pddrmMonRepeaterFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterFrameTooLongs.setStatus("deprecated")
_PddrmMonRepeaterShortEvents_Type = Counter32
_PddrmMonRepeaterShortEvents_Object = MibScalar
pddrmMonRepeaterShortEvents = _PddrmMonRepeaterShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 6),
    _PddrmMonRepeaterShortEvents_Type()
)
pddrmMonRepeaterShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterShortEvents.setStatus("deprecated")
_PddrmMonRepeaterRunts_Type = Counter32
_PddrmMonRepeaterRunts_Object = MibScalar
pddrmMonRepeaterRunts = _PddrmMonRepeaterRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 7),
    _PddrmMonRepeaterRunts_Type()
)
pddrmMonRepeaterRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterRunts.setStatus("deprecated")
_PddrmMonRepeaterCollisions_Type = Counter32
_PddrmMonRepeaterCollisions_Object = MibScalar
pddrmMonRepeaterCollisions = _PddrmMonRepeaterCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 8),
    _PddrmMonRepeaterCollisions_Type()
)
pddrmMonRepeaterCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterCollisions.setStatus("deprecated")
_PddrmMonRepeaterLateEvents_Type = Counter32
_PddrmMonRepeaterLateEvents_Object = MibScalar
pddrmMonRepeaterLateEvents = _PddrmMonRepeaterLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 9),
    _PddrmMonRepeaterLateEvents_Type()
)
pddrmMonRepeaterLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterLateEvents.setStatus("deprecated")
_PddrmMonRepeaterVeryLongEvents_Type = Counter32
_PddrmMonRepeaterVeryLongEvents_Object = MibScalar
pddrmMonRepeaterVeryLongEvents = _PddrmMonRepeaterVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 10),
    _PddrmMonRepeaterVeryLongEvents_Type()
)
pddrmMonRepeaterVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterVeryLongEvents.setStatus("deprecated")
_PddrmMonRepeaterDataRateMismatches_Type = Counter32
_PddrmMonRepeaterDataRateMismatches_Object = MibScalar
pddrmMonRepeaterDataRateMismatches = _PddrmMonRepeaterDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 11),
    _PddrmMonRepeaterDataRateMismatches_Type()
)
pddrmMonRepeaterDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterDataRateMismatches.setStatus("deprecated")
_PddrmMonRepeaterAutoPartitions_Type = Counter32
_PddrmMonRepeaterAutoPartitions_Object = MibScalar
pddrmMonRepeaterAutoPartitions = _PddrmMonRepeaterAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 12),
    _PddrmMonRepeaterAutoPartitions_Type()
)
pddrmMonRepeaterAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterAutoPartitions.setStatus("deprecated")
_PddrmMonRepeaterUniCastFrames_Type = Counter32
_PddrmMonRepeaterUniCastFrames_Object = MibScalar
pddrmMonRepeaterUniCastFrames = _PddrmMonRepeaterUniCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 13),
    _PddrmMonRepeaterUniCastFrames_Type()
)
pddrmMonRepeaterUniCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterUniCastFrames.setStatus("deprecated")
_PddrmMonRepeaterMultiCastFrames_Type = Counter32
_PddrmMonRepeaterMultiCastFrames_Object = MibScalar
pddrmMonRepeaterMultiCastFrames = _PddrmMonRepeaterMultiCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 14),
    _PddrmMonRepeaterMultiCastFrames_Type()
)
pddrmMonRepeaterMultiCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterMultiCastFrames.setStatus("deprecated")
_PddrmMonRepeaterBroadCastFrames_Type = Counter32
_PddrmMonRepeaterBroadCastFrames_Object = MibScalar
pddrmMonRepeaterBroadCastFrames = _PddrmMonRepeaterBroadCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 15),
    _PddrmMonRepeaterBroadCastFrames_Type()
)
pddrmMonRepeaterBroadCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterBroadCastFrames.setStatus("deprecated")


class _PddrmMonRepeaterClearCounters_Type(Integer32):
    """Custom type pddrmMonRepeaterClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 2),
          ("noChangeCounters", 1))
    )


_PddrmMonRepeaterClearCounters_Type.__name__ = "Integer32"
_PddrmMonRepeaterClearCounters_Object = MibScalar
pddrmMonRepeaterClearCounters = _PddrmMonRepeaterClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 16),
    _PddrmMonRepeaterClearCounters_Type()
)
pddrmMonRepeaterClearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterClearCounters.setStatus("deprecated")


class _PddrmMonRepeaterMediaAvailableTraps_Type(Integer32):
    """Custom type pddrmMonRepeaterMediaAvailableTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableMediaTraps", 2),
          ("enableMediaTraps", 1))
    )


_PddrmMonRepeaterMediaAvailableTraps_Type.__name__ = "Integer32"
_PddrmMonRepeaterMediaAvailableTraps_Object = MibScalar
pddrmMonRepeaterMediaAvailableTraps = _PddrmMonRepeaterMediaAvailableTraps_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 17),
    _PddrmMonRepeaterMediaAvailableTraps_Type()
)
pddrmMonRepeaterMediaAvailableTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pddrmMonRepeaterMediaAvailableTraps.setStatus("deprecated")


class _PddrmMonRepeaterAutoPartitionTraps_Type(Integer32):
    """Custom type pddrmMonRepeaterAutoPartitionTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablePartitionTraps", 2),
          ("enablePartitionTraps", 1))
    )


_PddrmMonRepeaterAutoPartitionTraps_Type.__name__ = "Integer32"
_PddrmMonRepeaterAutoPartitionTraps_Object = MibScalar
pddrmMonRepeaterAutoPartitionTraps = _PddrmMonRepeaterAutoPartitionTraps_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 18),
    _PddrmMonRepeaterAutoPartitionTraps_Type()
)
pddrmMonRepeaterAutoPartitionTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pddrmMonRepeaterAutoPartitionTraps.setStatus("deprecated")
_PddrmMonRepeaterTotalErrors_Type = Counter32
_PddrmMonRepeaterTotalErrors_Object = MibScalar
pddrmMonRepeaterTotalErrors = _PddrmMonRepeaterTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 1, 19),
    _PddrmMonRepeaterTotalErrors_Type()
)
pddrmMonRepeaterTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonRepeaterTotalErrors.setStatus("deprecated")
_PddrmMonGroupPackage_ObjectIdentity = ObjectIdentity
pddrmMonGroupPackage = _PddrmMonGroupPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2)
)
_PddrmMonitorGroupTable_Object = MibTable
pddrmMonitorGroupTable = _PddrmMonitorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pddrmMonitorGroupTable.setStatus("deprecated")
_PddrmMonitorGroupEntry_Object = MibTableRow
pddrmMonitorGroupEntry = _PddrmMonitorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1)
)
pddrmMonitorGroupEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "pddrmMonGroupIndex"),
)
if mibBuilder.loadTexts:
    pddrmMonitorGroupEntry.setStatus("deprecated")


class _PddrmMonGroupIndex_Type(Integer32):
    """Custom type pddrmMonGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PddrmMonGroupIndex_Type.__name__ = "Integer32"
_PddrmMonGroupIndex_Object = MibTableColumn
pddrmMonGroupIndex = _PddrmMonGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 1),
    _PddrmMonGroupIndex_Type()
)
pddrmMonGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupIndex.setStatus("deprecated")
_PddrmMonGroupFCSErrors_Type = Counter32
_PddrmMonGroupFCSErrors_Object = MibTableColumn
pddrmMonGroupFCSErrors = _PddrmMonGroupFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 4),
    _PddrmMonGroupFCSErrors_Type()
)
pddrmMonGroupFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupFCSErrors.setStatus("deprecated")
_PddrmMonGroupAlignmentErrors_Type = Counter32
_PddrmMonGroupAlignmentErrors_Object = MibTableColumn
pddrmMonGroupAlignmentErrors = _PddrmMonGroupAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 5),
    _PddrmMonGroupAlignmentErrors_Type()
)
pddrmMonGroupAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupAlignmentErrors.setStatus("deprecated")
_PddrmMonGroupFrameTooLongs_Type = Counter32
_PddrmMonGroupFrameTooLongs_Object = MibTableColumn
pddrmMonGroupFrameTooLongs = _PddrmMonGroupFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 6),
    _PddrmMonGroupFrameTooLongs_Type()
)
pddrmMonGroupFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupFrameTooLongs.setStatus("deprecated")
_PddrmMonGroupShortEvents_Type = Counter32
_PddrmMonGroupShortEvents_Object = MibTableColumn
pddrmMonGroupShortEvents = _PddrmMonGroupShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 7),
    _PddrmMonGroupShortEvents_Type()
)
pddrmMonGroupShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupShortEvents.setStatus("deprecated")
_PddrmMonGroupRunts_Type = Counter32
_PddrmMonGroupRunts_Object = MibTableColumn
pddrmMonGroupRunts = _PddrmMonGroupRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 8),
    _PddrmMonGroupRunts_Type()
)
pddrmMonGroupRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupRunts.setStatus("deprecated")
_PddrmMonGroupCollisions_Type = Counter32
_PddrmMonGroupCollisions_Object = MibTableColumn
pddrmMonGroupCollisions = _PddrmMonGroupCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 9),
    _PddrmMonGroupCollisions_Type()
)
pddrmMonGroupCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupCollisions.setStatus("deprecated")
_PddrmMonGroupLateEvents_Type = Counter32
_PddrmMonGroupLateEvents_Object = MibTableColumn
pddrmMonGroupLateEvents = _PddrmMonGroupLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 10),
    _PddrmMonGroupLateEvents_Type()
)
pddrmMonGroupLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupLateEvents.setStatus("deprecated")
_PddrmMonGroupVeryLongEvents_Type = Counter32
_PddrmMonGroupVeryLongEvents_Object = MibTableColumn
pddrmMonGroupVeryLongEvents = _PddrmMonGroupVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 11),
    _PddrmMonGroupVeryLongEvents_Type()
)
pddrmMonGroupVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupVeryLongEvents.setStatus("deprecated")
_PddrmMonGroupDataRateMismatches_Type = Counter32
_PddrmMonGroupDataRateMismatches_Object = MibTableColumn
pddrmMonGroupDataRateMismatches = _PddrmMonGroupDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 12),
    _PddrmMonGroupDataRateMismatches_Type()
)
pddrmMonGroupDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupDataRateMismatches.setStatus("deprecated")
_PddrmMonGroupAutoPartitions_Type = Counter32
_PddrmMonGroupAutoPartitions_Object = MibTableColumn
pddrmMonGroupAutoPartitions = _PddrmMonGroupAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 13),
    _PddrmMonGroupAutoPartitions_Type()
)
pddrmMonGroupAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupAutoPartitions.setStatus("deprecated")
_PddrmMonGroupUniCastFrames_Type = Counter32
_PddrmMonGroupUniCastFrames_Object = MibTableColumn
pddrmMonGroupUniCastFrames = _PddrmMonGroupUniCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 14),
    _PddrmMonGroupUniCastFrames_Type()
)
pddrmMonGroupUniCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupUniCastFrames.setStatus("deprecated")
_PddrmMonGroupMultiCastFrames_Type = Counter32
_PddrmMonGroupMultiCastFrames_Object = MibTableColumn
pddrmMonGroupMultiCastFrames = _PddrmMonGroupMultiCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 15),
    _PddrmMonGroupMultiCastFrames_Type()
)
pddrmMonGroupMultiCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupMultiCastFrames.setStatus("deprecated")
_PddrmMonGroupBroadCastFrames_Type = Counter32
_PddrmMonGroupBroadCastFrames_Object = MibTableColumn
pddrmMonGroupBroadCastFrames = _PddrmMonGroupBroadCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 16),
    _PddrmMonGroupBroadCastFrames_Type()
)
pddrmMonGroupBroadCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonGroupBroadCastFrames.setStatus("deprecated")


class _PddrmMonGroupClearCounters_Type(Integer32):
    """Custom type pddrmMonGroupClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 2),
          ("noChangeCounters", 1))
    )


_PddrmMonGroupClearCounters_Type.__name__ = "Integer32"
_PddrmMonGroupClearCounters_Object = MibTableColumn
pddrmMonGroupClearCounters = _PddrmMonGroupClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 2, 1, 1, 17),
    _PddrmMonGroupClearCounters_Type()
)
pddrmMonGroupClearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pddrmMonGroupClearCounters.setStatus("deprecated")
_PddrmMonPortPackage_ObjectIdentity = ObjectIdentity
pddrmMonPortPackage = _PddrmMonPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3)
)
_PddrmMonitorPortTable_Object = MibTable
pddrmMonitorPortTable = _PddrmMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pddrmMonitorPortTable.setStatus("deprecated")
_PddrmMonitorPortEntry_Object = MibTableRow
pddrmMonitorPortEntry = _PddrmMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1)
)
pddrmMonitorPortEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "pddrmMonPortGroupIndex"),
    (0, "LBHUB-FMS-MIB", "pddrmMonPortIndex"),
)
if mibBuilder.loadTexts:
    pddrmMonitorPortEntry.setStatus("deprecated")


class _PddrmMonPortGroupIndex_Type(Integer32):
    """Custom type pddrmMonPortGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PddrmMonPortGroupIndex_Type.__name__ = "Integer32"
_PddrmMonPortGroupIndex_Object = MibTableColumn
pddrmMonPortGroupIndex = _PddrmMonPortGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 1),
    _PddrmMonPortGroupIndex_Type()
)
pddrmMonPortGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonPortGroupIndex.setStatus("deprecated")


class _PddrmMonPortIndex_Type(Integer32):
    """Custom type pddrmMonPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_PddrmMonPortIndex_Type.__name__ = "Integer32"
_PddrmMonPortIndex_Object = MibTableColumn
pddrmMonPortIndex = _PddrmMonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 2),
    _PddrmMonPortIndex_Type()
)
pddrmMonPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonPortIndex.setStatus("deprecated")
_PddrmMonPortUniCastFrames_Type = Counter32
_PddrmMonPortUniCastFrames_Object = MibTableColumn
pddrmMonPortUniCastFrames = _PddrmMonPortUniCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 3),
    _PddrmMonPortUniCastFrames_Type()
)
pddrmMonPortUniCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonPortUniCastFrames.setStatus("deprecated")
_PddrmMonPortMultiCastFrames_Type = Counter32
_PddrmMonPortMultiCastFrames_Object = MibTableColumn
pddrmMonPortMultiCastFrames = _PddrmMonPortMultiCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 4),
    _PddrmMonPortMultiCastFrames_Type()
)
pddrmMonPortMultiCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonPortMultiCastFrames.setStatus("deprecated")
_PddrmMonPortBroadCastFrames_Type = Counter32
_PddrmMonPortBroadCastFrames_Object = MibTableColumn
pddrmMonPortBroadCastFrames = _PddrmMonPortBroadCastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 5),
    _PddrmMonPortBroadCastFrames_Type()
)
pddrmMonPortBroadCastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pddrmMonPortBroadCastFrames.setStatus("deprecated")


class _PddrmMonPortClearCounters_Type(Integer32):
    """Custom type pddrmMonPortClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 2),
          ("noChangeCounters", 1))
    )


_PddrmMonPortClearCounters_Type.__name__ = "Integer32"
_PddrmMonPortClearCounters_Object = MibTableColumn
pddrmMonPortClearCounters = _PddrmMonPortClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 6),
    _PddrmMonPortClearCounters_Type()
)
pddrmMonPortClearCounters.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    pddrmMonPortClearCounters.setStatus("deprecated")


class _PddrmMonPortESTFilter_Type(Integer32):
    """Custom type pddrmMonPortESTFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("pass", 2))
    )


_PddrmMonPortESTFilter_Type.__name__ = "Integer32"
_PddrmMonPortESTFilter_Object = MibTableColumn
pddrmMonPortESTFilter = _PddrmMonPortESTFilter_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 7),
    _PddrmMonPortESTFilter_Type()
)
pddrmMonPortESTFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pddrmMonPortESTFilter.setStatus("deprecated")


class _PddrmMonPortMediaAvailableTraps_Type(Integer32):
    """Custom type pddrmMonPortMediaAvailableTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disableMediaTraps", 2),
          ("enableMediaTraps", 1))
    )


_PddrmMonPortMediaAvailableTraps_Type.__name__ = "Integer32"
_PddrmMonPortMediaAvailableTraps_Object = MibTableColumn
pddrmMonPortMediaAvailableTraps = _PddrmMonPortMediaAvailableTraps_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 8),
    _PddrmMonPortMediaAvailableTraps_Type()
)
pddrmMonPortMediaAvailableTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pddrmMonPortMediaAvailableTraps.setStatus("deprecated")


class _PddrmMonPortAutoPartitionTraps_Type(Integer32):
    """Custom type pddrmMonPortAutoPartitionTraps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disablePartitionTraps", 2),
          ("enablePartitionTraps", 1))
    )


_PddrmMonPortAutoPartitionTraps_Type.__name__ = "Integer32"
_PddrmMonPortAutoPartitionTraps_Object = MibTableColumn
pddrmMonPortAutoPartitionTraps = _PddrmMonPortAutoPartitionTraps_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 3, 1, 1, 9),
    _PddrmMonPortAutoPartitionTraps_Type()
)
pddrmMonPortAutoPartitionTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pddrmMonPortAutoPartitionTraps.setStatus("deprecated")
_PddrmMonRepeaterDummyPackage_ObjectIdentity = ObjectIdentity
pddrmMonRepeaterDummyPackage = _PddrmMonRepeaterDummyPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 4)
)
_PddrmMonGroupDummyPackage_ObjectIdentity = ObjectIdentity
pddrmMonGroupDummyPackage = _PddrmMonGroupDummyPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 5)
)
_PddrmMonPortDummyPackage_ObjectIdentity = ObjectIdentity
pddrmMonPortDummyPackage = _PddrmMonPortDummyPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 8, 2, 6)
)
_EndStation_ObjectIdentity = ObjectIdentity
endStation = _EndStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 9)
)


class _EsDatabaseState_Type(Integer32):
    """Custom type esDatabaseState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modified", 2),
          ("noChange", 1))
    )


_EsDatabaseState_Type.__name__ = "Integer32"
_EsDatabaseState_Object = MibScalar
esDatabaseState = _EsDatabaseState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 1),
    _EsDatabaseState_Type()
)
esDatabaseState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esDatabaseState.setStatus("mandatory")


class _EsDatabaseFlush_Type(Integer32):
    """Custom type esDatabaseFlush based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("flush", 1)
    )


_EsDatabaseFlush_Type.__name__ = "Integer32"
_EsDatabaseFlush_Object = MibScalar
esDatabaseFlush = _EsDatabaseFlush_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 2),
    _EsDatabaseFlush_Type()
)
esDatabaseFlush.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    esDatabaseFlush.setStatus("mandatory")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3)
)
if mibBuilder.loadTexts:
    esTable.setStatus("mandatory")
_EsTableEntry_Object = MibTableRow
esTableEntry = _EsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1)
)
esTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "esAddrType"),
    (0, "LBHUB-FMS-MIB", "esAddress"),
)
if mibBuilder.loadTexts:
    esTableEntry.setStatus("mandatory")


class _EsAddrType_Type(Integer32):
    """Custom type esAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021", 1),
          ("internet", 2),
          ("ipx", 3))
    )


_EsAddrType_Type.__name__ = "Integer32"
_EsAddrType_Object = MibTableColumn
esAddrType = _EsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 1),
    _EsAddrType_Type()
)
esAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAddrType.setStatus("mandatory")


class _EsAddress_Type(OctetString):
    """Custom type esAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EsAddress_Type.__name__ = "OctetString"
_EsAddress_Object = MibTableColumn
esAddress = _EsAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 2),
    _EsAddress_Type()
)
esAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAddress.setStatus("mandatory")
_EsSlotNumber_Type = Integer32
_EsSlotNumber_Object = MibTableColumn
esSlotNumber = _EsSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 3),
    _EsSlotNumber_Type()
)
esSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esSlotNumber.setStatus("mandatory")
_EsPortNumber_Type = Integer32
_EsPortNumber_Object = MibTableColumn
esPortNumber = _EsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 3, 1, 4),
    _EsPortNumber_Type()
)
esPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPortNumber.setStatus("mandatory")
_EsModTable_Object = MibTable
esModTable = _EsModTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4)
)
if mibBuilder.loadTexts:
    esModTable.setStatus("mandatory")
_EsModTableEntry_Object = MibTableRow
esModTableEntry = _EsModTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1)
)
esModTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "esModAddrType"),
    (0, "LBHUB-FMS-MIB", "esModAddress"),
)
if mibBuilder.loadTexts:
    esModTableEntry.setStatus("mandatory")


class _EsModAddrType_Type(Integer32):
    """Custom type esModAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021", 1),
          ("internet", 2),
          ("ipx", 3))
    )


_EsModAddrType_Type.__name__ = "Integer32"
_EsModAddrType_Object = MibTableColumn
esModAddrType = _EsModAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 1),
    _EsModAddrType_Type()
)
esModAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModAddrType.setStatus("mandatory")


class _EsModAddress_Type(OctetString):
    """Custom type esModAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EsModAddress_Type.__name__ = "OctetString"
_EsModAddress_Object = MibTableColumn
esModAddress = _EsModAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 2),
    _EsModAddress_Type()
)
esModAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModAddress.setStatus("mandatory")
_EsModSlotNumber_Type = Integer32
_EsModSlotNumber_Object = MibTableColumn
esModSlotNumber = _EsModSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 3),
    _EsModSlotNumber_Type()
)
esModSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModSlotNumber.setStatus("mandatory")
_EsModPortNumber_Type = Integer32
_EsModPortNumber_Object = MibTableColumn
esModPortNumber = _EsModPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 4, 1, 4),
    _EsModPortNumber_Type()
)
esModPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esModPortNumber.setStatus("mandatory")
_EsPortAccessTable_Object = MibTable
esPortAccessTable = _EsPortAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5)
)
if mibBuilder.loadTexts:
    esPortAccessTable.setStatus("mandatory")
_EsPortAccessEntry_Object = MibTableRow
esPortAccessEntry = _EsPortAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1)
)
esPortAccessEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "ecPortCardNo"),
    (0, "LBHUB-FMS-MIB", "ecPortPortNo"),
    (0, "LBHUB-FMS-MIB", "ecPortIndex"),
)
if mibBuilder.loadTexts:
    esPortAccessEntry.setStatus("mandatory")
_EcPortCardNo_Type = Integer32
_EcPortCardNo_Object = MibTableColumn
ecPortCardNo = _EcPortCardNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 2),
    _EcPortCardNo_Type()
)
ecPortCardNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortCardNo.setStatus("mandatory")
_EcPortPortNo_Type = Integer32
_EcPortPortNo_Object = MibTableColumn
ecPortPortNo = _EcPortPortNo_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 3),
    _EcPortPortNo_Type()
)
ecPortPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortPortNo.setStatus("mandatory")
_EcPortIndex_Type = Integer32
_EcPortIndex_Object = MibTableColumn
ecPortIndex = _EcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 4),
    _EcPortIndex_Type()
)
ecPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortIndex.setStatus("mandatory")


class _EcPortAddrType_Type(Integer32):
    """Custom type ecPortAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021", 1),
          ("internet", 2),
          ("ipx", 3))
    )


_EcPortAddrType_Type.__name__ = "Integer32"
_EcPortAddrType_Object = MibTableColumn
ecPortAddrType = _EcPortAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 5),
    _EcPortAddrType_Type()
)
ecPortAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortAddrType.setStatus("mandatory")


class _EcPortAddress_Type(OctetString):
    """Custom type ecPortAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_EcPortAddress_Type.__name__ = "OctetString"
_EcPortAddress_Object = MibTableColumn
ecPortAddress = _EcPortAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 9, 5, 1, 6),
    _EcPortAddress_Type()
)
ecPortAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ecPortAddress.setStatus("mandatory")
_LocalSnmp_ObjectIdentity = ObjectIdentity
localSnmp = _LocalSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 10)
)
_TrapTable_Object = MibTable
trapTable = _TrapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1)
)
if mibBuilder.loadTexts:
    trapTable.setStatus("deprecated")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1)
)
trapEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "trapDestination"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("deprecated")


class _TrapStatus_Type(Integer32):
    """Custom type trapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TrapStatus_Type.__name__ = "Integer32"
_TrapStatus_Object = MibTableColumn
trapStatus = _TrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 1),
    _TrapStatus_Type()
)
trapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapStatus.setStatus("deprecated")
_TrapDestination_Type = IpAddress
_TrapDestination_Object = MibTableColumn
trapDestination = _TrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 2),
    _TrapDestination_Type()
)
trapDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapDestination.setStatus("deprecated")


class _TrapCommunity_Type(DisplayString):
    """Custom type trapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapCommunity_Type.__name__ = "DisplayString"
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 3),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("deprecated")
_TrapSubject_Type = ObjectIdentifier
_TrapSubject_Object = MibTableColumn
trapSubject = _TrapSubject_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 4),
    _TrapSubject_Type()
)
trapSubject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSubject.setStatus("deprecated")
_TrapCategory_Type = Integer32
_TrapCategory_Object = MibTableColumn
trapCategory = _TrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 5),
    _TrapCategory_Type()
)
trapCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCategory.setStatus("deprecated")
_TrapThrottle_Type = Integer32
_TrapThrottle_Object = MibTableColumn
trapThrottle = _TrapThrottle_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 1, 1, 6),
    _TrapThrottle_Type()
)
trapThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapThrottle.setStatus("deprecated")
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("mandatory")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "snmpTrapIndex"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("mandatory")


class _SnmpTrapIndex_Type(Integer32):
    """Custom type snmpTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnmpTrapIndex_Type.__name__ = "Integer32"
_SnmpTrapIndex_Object = MibTableColumn
snmpTrapIndex = _SnmpTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 1),
    _SnmpTrapIndex_Type()
)
snmpTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapIndex.setStatus("mandatory")


class _SnmpTrapDestination_Type(DisplayString):
    """Custom type snmpTrapDestination based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SnmpTrapDestination_Type.__name__ = "DisplayString"
_SnmpTrapDestination_Object = MibTableColumn
snmpTrapDestination = _SnmpTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 2),
    _SnmpTrapDestination_Type()
)
snmpTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapDestination.setStatus("mandatory")


class _SnmpTrapProtocol_Type(Integer32):
    """Custom type snmpTrapProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("ipx", 3),
          ("unknown", 1))
    )


_SnmpTrapProtocol_Type.__name__ = "Integer32"
_SnmpTrapProtocol_Object = MibTableColumn
snmpTrapProtocol = _SnmpTrapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 3),
    _SnmpTrapProtocol_Type()
)
snmpTrapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapProtocol.setStatus("mandatory")


class _SnmpTrapCommunity_Type(DisplayString):
    """Custom type snmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnmpTrapCommunity_Type.__name__ = "DisplayString"
_SnmpTrapCommunity_Object = MibTableColumn
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 4),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("mandatory")


class _SnmpTrapCategory_Type(OctetString):
    """Custom type snmpTrapCategory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_SnmpTrapCategory_Type.__name__ = "OctetString"
_SnmpTrapCategory_Object = MibTableColumn
snmpTrapCategory = _SnmpTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 5),
    _SnmpTrapCategory_Type()
)
snmpTrapCategory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCategory.setStatus("mandatory")


class _SnmpTrapThrottle_Type(Integer32):
    """Custom type snmpTrapThrottle based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_SnmpTrapThrottle_Type.__name__ = "Integer32"
_SnmpTrapThrottle_Object = MibTableColumn
snmpTrapThrottle = _SnmpTrapThrottle_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 6),
    _SnmpTrapThrottle_Type()
)
snmpTrapThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapThrottle.setStatus("mandatory")


class _SnmpTrapRowStatus_Type(Integer32):
    """Custom type snmpTrapRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_SnmpTrapRowStatus_Type.__name__ = "Integer32"
_SnmpTrapRowStatus_Object = MibTableColumn
snmpTrapRowStatus = _SnmpTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 2, 1, 7),
    _SnmpTrapRowStatus_Type()
)
snmpTrapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRowStatus.setStatus("mandatory")


class _SnmpTrapNextFreeIndex_Type(Integer32):
    """Custom type snmpTrapNextFreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnmpTrapNextFreeIndex_Type.__name__ = "Integer32"
_SnmpTrapNextFreeIndex_Object = MibScalar
snmpTrapNextFreeIndex = _SnmpTrapNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 10, 3),
    _SnmpTrapNextFreeIndex_Type()
)
snmpTrapNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapNextFreeIndex.setStatus("mandatory")
_Manager_ObjectIdentity = ObjectIdentity
manager = _Manager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 11)
)
_UnusedGeneric12_ObjectIdentity = ObjectIdentity
unusedGeneric12 = _UnusedGeneric12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 12)
)
_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 14)
)
_MrmResilience_ObjectIdentity = ObjectIdentity
mrmResilience = _MrmResilience_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 15)
)
_ResTable_Object = MibTable
resTable = _ResTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1)
)
if mibBuilder.loadTexts:
    resTable.setStatus("mandatory")
_ResTableEntry_Object = MibTableRow
resTableEntry = _ResTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1)
)
resTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "resRepeater"),
    (0, "LBHUB-FMS-MIB", "resMainSlot"),
    (0, "LBHUB-FMS-MIB", "resMainPort"),
)
if mibBuilder.loadTexts:
    resTableEntry.setStatus("mandatory")
_ResRepeater_Type = Integer32
_ResRepeater_Object = MibTableColumn
resRepeater = _ResRepeater_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 1),
    _ResRepeater_Type()
)
resRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resRepeater.setStatus("mandatory")
_ResMainSlot_Type = Integer32
_ResMainSlot_Object = MibTableColumn
resMainSlot = _ResMainSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 2),
    _ResMainSlot_Type()
)
resMainSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainSlot.setStatus("mandatory")
_ResMainPort_Type = Integer32
_ResMainPort_Object = MibTableColumn
resMainPort = _ResMainPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 3),
    _ResMainPort_Type()
)
resMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainPort.setStatus("mandatory")


class _ResMainState_Type(Integer32):
    """Custom type resMainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2),
          ("ok-and-active", 3))
    )


_ResMainState_Type.__name__ = "Integer32"
_ResMainState_Object = MibTableColumn
resMainState = _ResMainState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 4),
    _ResMainState_Type()
)
resMainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resMainState.setStatus("mandatory")
_ResStandbySlot_Type = Integer32
_ResStandbySlot_Object = MibTableColumn
resStandbySlot = _ResStandbySlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 5),
    _ResStandbySlot_Type()
)
resStandbySlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resStandbySlot.setStatus("mandatory")
_ResStandbyPort_Type = Integer32
_ResStandbyPort_Object = MibTableColumn
resStandbyPort = _ResStandbyPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 6),
    _ResStandbyPort_Type()
)
resStandbyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resStandbyPort.setStatus("mandatory")


class _ResStandbyState_Type(Integer32):
    """Custom type resStandbyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("ok", 2),
          ("ok-and-active", 3))
    )


_ResStandbyState_Type.__name__ = "Integer32"
_ResStandbyState_Object = MibTableColumn
resStandbyState = _ResStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 7),
    _ResStandbyState_Type()
)
resStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resStandbyState.setStatus("mandatory")


class _ResPairState_Type(Integer32):
    """Custom type resPairState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("operational", 2))
    )


_ResPairState_Type.__name__ = "Integer32"
_ResPairState_Object = MibTableColumn
resPairState = _ResPairState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 8),
    _ResPairState_Type()
)
resPairState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resPairState.setStatus("mandatory")


class _ResPairModificationStatus_Type(Integer32):
    """Custom type resPairModificationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stable", 2),
          ("under-modification", 1))
    )


_ResPairModificationStatus_Type.__name__ = "Integer32"
_ResPairModificationStatus_Object = MibTableColumn
resPairModificationStatus = _ResPairModificationStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 9),
    _ResPairModificationStatus_Type()
)
resPairModificationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairModificationStatus.setStatus("mandatory")


class _ResPairAction_Type(Integer32):
    """Custom type resPairAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2),
          ("togglePort", 3))
    )


_ResPairAction_Type.__name__ = "Integer32"
_ResPairAction_Object = MibTableColumn
resPairAction = _ResPairAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 10),
    _ResPairAction_Type()
)
resPairAction.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    resPairAction.setStatus("mandatory")


class _ResPairEnable_Type(Integer32):
    """Custom type resPairEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ResPairEnable_Type.__name__ = "Integer32"
_ResPairEnable_Object = MibTableColumn
resPairEnable = _ResPairEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 1, 1, 11),
    _ResPairEnable_Type()
)
resPairEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resPairEnable.setStatus("mandatory")
_ResStandbyMapTable_Object = MibTable
resStandbyMapTable = _ResStandbyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2)
)
if mibBuilder.loadTexts:
    resStandbyMapTable.setStatus("mandatory")
_ResStandbyMapTableEntry_Object = MibTableRow
resStandbyMapTableEntry = _ResStandbyMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1)
)
resStandbyMapTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "resSbRepeater"),
    (0, "LBHUB-FMS-MIB", "resSbSlot"),
    (0, "LBHUB-FMS-MIB", "resSbPort"),
)
if mibBuilder.loadTexts:
    resStandbyMapTableEntry.setStatus("mandatory")
_ResSbRepeater_Type = Integer32
_ResSbRepeater_Object = MibTableColumn
resSbRepeater = _ResSbRepeater_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 1),
    _ResSbRepeater_Type()
)
resSbRepeater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbRepeater.setStatus("mandatory")
_ResSbSlot_Type = Integer32
_ResSbSlot_Object = MibTableColumn
resSbSlot = _ResSbSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 2),
    _ResSbSlot_Type()
)
resSbSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbSlot.setStatus("mandatory")
_ResSbPort_Type = Integer32
_ResSbPort_Object = MibTableColumn
resSbPort = _ResSbPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 3),
    _ResSbPort_Type()
)
resSbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbPort.setStatus("mandatory")


class _ResSbType_Type(Integer32):
    """Custom type resSbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("standby", 2))
    )


_ResSbType_Type.__name__ = "Integer32"
_ResSbType_Object = MibTableColumn
resSbType = _ResSbType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 4),
    _ResSbType_Type()
)
resSbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbType.setStatus("mandatory")
_ResSbMainSlot_Type = Integer32
_ResSbMainSlot_Object = MibTableColumn
resSbMainSlot = _ResSbMainSlot_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 5),
    _ResSbMainSlot_Type()
)
resSbMainSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbMainSlot.setStatus("mandatory")
_ResSbMainPort_Type = Integer32
_ResSbMainPort_Object = MibTableColumn
resSbMainPort = _ResSbMainPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 2, 1, 6),
    _ResSbMainPort_Type()
)
resSbMainPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    resSbMainPort.setStatus("mandatory")
_ResFlushTable_Type = Integer32
_ResFlushTable_Object = MibScalar
resFlushTable = _ResFlushTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 15, 3),
    _ResFlushTable_Type()
)
resFlushTable.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    resFlushTable.setStatus("mandatory")
_TokenRing_ObjectIdentity = ObjectIdentity
tokenRing = _TokenRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 16)
)
_MultiRepeater_ObjectIdentity = ObjectIdentity
multiRepeater = _MultiRepeater_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17)
)
_MrmBasicPackage_ObjectIdentity = ObjectIdentity
mrmBasicPackage = _MrmBasicPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1)
)
_MrmBasCardPackage_ObjectIdentity = ObjectIdentity
mrmBasCardPackage = _MrmBasCardPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1)
)
_MrmCardTable_Object = MibTable
mrmCardTable = _MrmCardTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mrmCardTable.setStatus("mandatory")
_MrmCardEntry_Object = MibTableRow
mrmCardEntry = _MrmCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1)
)
mrmCardEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "mrmCardServiceId"),
    (0, "LBHUB-FMS-MIB", "mrmCardIndex"),
)
if mibBuilder.loadTexts:
    mrmCardEntry.setStatus("mandatory")
_MrmCardServiceId_Type = Integer32
_MrmCardServiceId_Object = MibTableColumn
mrmCardServiceId = _MrmCardServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 1),
    _MrmCardServiceId_Type()
)
mrmCardServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardServiceId.setStatus("mandatory")
_MrmCardIndex_Type = Integer32
_MrmCardIndex_Object = MibTableColumn
mrmCardIndex = _MrmCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 2),
    _MrmCardIndex_Type()
)
mrmCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardIndex.setStatus("mandatory")
_MrmCardPortCapacity_Type = Integer32
_MrmCardPortCapacity_Object = MibTableColumn
mrmCardPortCapacity = _MrmCardPortCapacity_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 3),
    _MrmCardPortCapacity_Type()
)
mrmCardPortCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardPortCapacity.setStatus("mandatory")


class _MrmCardTest_Type(Integer32):
    """Custom type mrmCardTest based on Integer32"""
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
        *(("failed", 5),
          ("noTest", 1),
          ("passed", 4),
          ("test", 2),
          ("testing", 3))
    )


_MrmCardTest_Type.__name__ = "Integer32"
_MrmCardTest_Object = MibTableColumn
mrmCardTest = _MrmCardTest_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 4),
    _MrmCardTest_Type()
)
mrmCardTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmCardTest.setStatus("mandatory")
_MrmCardDOBPorts_Type = Integer32
_MrmCardDOBPorts_Object = MibTableColumn
mrmCardDOBPorts = _MrmCardDOBPorts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 5),
    _MrmCardDOBPorts_Type()
)
mrmCardDOBPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardDOBPorts.setStatus("mandatory")


class _MrmCardMDIenable_Type(Integer32):
    """Custom type mrmCardMDIenable based on Integer32"""
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
        *(("mdiDisabled", 2),
          ("mdiEnabled", 3),
          ("notApplicable", 4),
          ("unknown", 1))
    )


_MrmCardMDIenable_Type.__name__ = "Integer32"
_MrmCardMDIenable_Object = MibTableColumn
mrmCardMDIenable = _MrmCardMDIenable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 1, 1, 1, 6),
    _MrmCardMDIenable_Type()
)
mrmCardMDIenable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmCardMDIenable.setStatus("mandatory")
_MrmBasPortPackage_ObjectIdentity = ObjectIdentity
mrmBasPortPackage = _MrmBasPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2)
)
_MrmPortTable_Object = MibTable
mrmPortTable = _MrmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mrmPortTable.setStatus("mandatory")
_MrmPortEntry_Object = MibTableRow
mrmPortEntry = _MrmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1)
)
mrmPortEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "mrmPortServiceId"),
    (0, "LBHUB-FMS-MIB", "mrmPortCardIndex"),
    (0, "LBHUB-FMS-MIB", "mrmPortIndex"),
)
if mibBuilder.loadTexts:
    mrmPortEntry.setStatus("mandatory")
_MrmPortServiceId_Type = Integer32
_MrmPortServiceId_Object = MibTableColumn
mrmPortServiceId = _MrmPortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 1),
    _MrmPortServiceId_Type()
)
mrmPortServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortServiceId.setStatus("mandatory")
_MrmPortCardIndex_Type = Integer32
_MrmPortCardIndex_Object = MibTableColumn
mrmPortCardIndex = _MrmPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 2),
    _MrmPortCardIndex_Type()
)
mrmPortCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortCardIndex.setStatus("mandatory")
_MrmPortIndex_Type = Integer32
_MrmPortIndex_Object = MibTableColumn
mrmPortIndex = _MrmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 3),
    _MrmPortIndex_Type()
)
mrmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortIndex.setStatus("mandatory")


class _MrmPortInterfaceType_Type(Integer32):
    """Custom type mrmPortInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("femaleAUI", 3),
          ("fiber", 7),
          ("maleAUI", 2),
          ("thinCoax", 4),
          ("twistedPair", 5),
          ("unknown", 1),
          ("unshieldedTP", 6))
    )


_MrmPortInterfaceType_Type.__name__ = "Integer32"
_MrmPortInterfaceType_Object = MibTableColumn
mrmPortInterfaceType = _MrmPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 4),
    _MrmPortInterfaceType_Type()
)
mrmPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortInterfaceType.setStatus("mandatory")


class _MrmPortConnectorType_Type(Integer32):
    """Custom type mrmPortConnectorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("bnc", 7),
          ("dtype-15", 6),
          ("rj45", 2),
          ("sma", 5),
          ("st", 4),
          ("telco", 3),
          ("unknown", 1))
    )


_MrmPortConnectorType_Type.__name__ = "Integer32"
_MrmPortConnectorType_Object = MibTableColumn
mrmPortConnectorType = _MrmPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 5),
    _MrmPortConnectorType_Type()
)
mrmPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortConnectorType.setStatus("mandatory")


class _MrmPortAdminStatus_Type(Integer32):
    """Custom type mrmPortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MrmPortAdminStatus_Type.__name__ = "Integer32"
_MrmPortAdminStatus_Object = MibTableColumn
mrmPortAdminStatus = _MrmPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 6),
    _MrmPortAdminStatus_Type()
)
mrmPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortAdminStatus.setStatus("mandatory")


class _MrmPortAutoPartitionState_Type(Integer32):
    """Custom type mrmPortAutoPartitionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("partitioned", 1),
          ("unpartitioned", 2))
    )


_MrmPortAutoPartitionState_Type.__name__ = "Integer32"
_MrmPortAutoPartitionState_Object = MibTableColumn
mrmPortAutoPartitionState = _MrmPortAutoPartitionState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 7),
    _MrmPortAutoPartitionState_Type()
)
mrmPortAutoPartitionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortAutoPartitionState.setStatus("mandatory")


class _MrmPortLinkState_Type(Integer32):
    """Custom type mrmPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("present", 1))
    )


_MrmPortLinkState_Type.__name__ = "Integer32"
_MrmPortLinkState_Object = MibTableColumn
mrmPortLinkState = _MrmPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 8),
    _MrmPortLinkState_Type()
)
mrmPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortLinkState.setStatus("mandatory")


class _MrmPortBootState_Type(Integer32):
    """Custom type mrmPortBootState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_MrmPortBootState_Type.__name__ = "Integer32"
_MrmPortBootState_Object = MibTableColumn
mrmPortBootState = _MrmPortBootState_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 9),
    _MrmPortBootState_Type()
)
mrmPortBootState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortBootState.setStatus("mandatory")


class _MrmPortESTFilter_Type(Integer32):
    """Custom type mrmPortESTFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              127,
              128)
        )
    )
    namedValues = NamedValues(
        *(("forwardAll", 127),
          ("forwardIP", 2),
          ("forwardMAC", 1),
          ("forwardNone", 128))
    )


_MrmPortESTFilter_Type.__name__ = "Integer32"
_MrmPortESTFilter_Object = MibTableColumn
mrmPortESTFilter = _MrmPortESTFilter_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 10),
    _MrmPortESTFilter_Type()
)
mrmPortESTFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortESTFilter.setStatus("mandatory")


class _MrmPortPartitionEvent_Type(Integer32):
    """Custom type mrmPortPartitionEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MrmPortPartitionEvent_Type.__name__ = "Integer32"
_MrmPortPartitionEvent_Object = MibTableColumn
mrmPortPartitionEvent = _MrmPortPartitionEvent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 11),
    _MrmPortPartitionEvent_Type()
)
mrmPortPartitionEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortPartitionEvent.setStatus("mandatory")


class _MrmPortLinkStateEvent_Type(Integer32):
    """Custom type mrmPortLinkStateEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MrmPortLinkStateEvent_Type.__name__ = "Integer32"
_MrmPortLinkStateEvent_Object = MibTableColumn
mrmPortLinkStateEvent = _MrmPortLinkStateEvent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 12),
    _MrmPortLinkStateEvent_Type()
)
mrmPortLinkStateEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortLinkStateEvent.setStatus("mandatory")


class _MrmPortSecurityAvailable_Type(Integer32):
    """Custom type mrmPortSecurityAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 1),
          ("notAvailable", 2))
    )


_MrmPortSecurityAvailable_Type.__name__ = "Integer32"
_MrmPortSecurityAvailable_Object = MibTableColumn
mrmPortSecurityAvailable = _MrmPortSecurityAvailable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 13),
    _MrmPortSecurityAvailable_Type()
)
mrmPortSecurityAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortSecurityAvailable.setStatus("mandatory")


class _MrmPortLinkPulse_Type(Integer32):
    """Custom type mrmPortLinkPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("notApplicable", 3))
    )


_MrmPortLinkPulse_Type.__name__ = "Integer32"
_MrmPortLinkPulse_Object = MibTableColumn
mrmPortLinkPulse = _MrmPortLinkPulse_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 14),
    _MrmPortLinkPulse_Type()
)
mrmPortLinkPulse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortLinkPulse.setStatus("mandatory")


class _MrmPortModule_Type(Integer32):
    """Custom type mrmPortModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("modularPort", 2),
          ("notModularPort", 3),
          ("unknown", 1))
    )


_MrmPortModule_Type.__name__ = "Integer32"
_MrmPortModule_Object = MibTableColumn
mrmPortModule = _MrmPortModule_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 15),
    _MrmPortModule_Type()
)
mrmPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortModule.setStatus("mandatory")


class _MrmPortDUDAction_Type(Integer32):
    """Custom type mrmPortDUDAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disconnect", 3),
          ("noAction", 1),
          ("notify", 2))
    )


_MrmPortDUDAction_Type.__name__ = "Integer32"
_MrmPortDUDAction_Object = MibTableColumn
mrmPortDUDAction = _MrmPortDUDAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 16),
    _MrmPortDUDAction_Type()
)
mrmPortDUDAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmPortDUDAction.setStatus("mandatory")


class _MrmPortFunction_Type(Integer32):
    """Custom type mrmPortFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 3),
          ("repeater", 2),
          ("unknown", 1))
    )


_MrmPortFunction_Type.__name__ = "Integer32"
_MrmPortFunction_Object = MibTableColumn
mrmPortFunction = _MrmPortFunction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 1, 2, 1, 1, 17),
    _MrmPortFunction_Type()
)
mrmPortFunction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmPortFunction.setStatus("mandatory")
_MrmMonitorPackage_ObjectIdentity = ObjectIdentity
mrmMonitorPackage = _MrmMonitorPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2)
)
_MrmMonRepeaterPackage_ObjectIdentity = ObjectIdentity
mrmMonRepeaterPackage = _MrmMonRepeaterPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1)
)
_MrmMonitorRepTable_Object = MibTable
mrmMonitorRepTable = _MrmMonitorRepTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1)
)
if mibBuilder.loadTexts:
    mrmMonitorRepTable.setStatus("mandatory")
_MrmMonitorRepEntry_Object = MibTableRow
mrmMonitorRepEntry = _MrmMonitorRepEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1)
)
mrmMonitorRepEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "mrmMonRepServiceId"),
)
if mibBuilder.loadTexts:
    mrmMonitorRepEntry.setStatus("mandatory")
_MrmMonRepServiceId_Type = Integer32
_MrmMonRepServiceId_Object = MibTableColumn
mrmMonRepServiceId = _MrmMonRepServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 1),
    _MrmMonRepServiceId_Type()
)
mrmMonRepServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepServiceId.setStatus("mandatory")
_MrmMonRepReadableFrames_Type = Counter32
_MrmMonRepReadableFrames_Object = MibTableColumn
mrmMonRepReadableFrames = _MrmMonRepReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 2),
    _MrmMonRepReadableFrames_Type()
)
mrmMonRepReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepReadableFrames.setStatus("mandatory")
_MrmMonRepUnicastFrames_Type = Counter32
_MrmMonRepUnicastFrames_Object = MibTableColumn
mrmMonRepUnicastFrames = _MrmMonRepUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 3),
    _MrmMonRepUnicastFrames_Type()
)
mrmMonRepUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepUnicastFrames.setStatus("mandatory")
_MrmMonRepMulticastFrames_Type = Counter32
_MrmMonRepMulticastFrames_Object = MibTableColumn
mrmMonRepMulticastFrames = _MrmMonRepMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 4),
    _MrmMonRepMulticastFrames_Type()
)
mrmMonRepMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepMulticastFrames.setStatus("mandatory")
_MrmMonRepBroadcastFrames_Type = Counter32
_MrmMonRepBroadcastFrames_Object = MibTableColumn
mrmMonRepBroadcastFrames = _MrmMonRepBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 5),
    _MrmMonRepBroadcastFrames_Type()
)
mrmMonRepBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBroadcastFrames.setStatus("mandatory")
_MrmMonRepReadableOctets_Type = Counter32
_MrmMonRepReadableOctets_Object = MibTableColumn
mrmMonRepReadableOctets = _MrmMonRepReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 6),
    _MrmMonRepReadableOctets_Type()
)
mrmMonRepReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepReadableOctets.setStatus("mandatory")
_MrmMonRepUnicastOctets_Type = Counter32
_MrmMonRepUnicastOctets_Object = MibTableColumn
mrmMonRepUnicastOctets = _MrmMonRepUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 7),
    _MrmMonRepUnicastOctets_Type()
)
mrmMonRepUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepUnicastOctets.setStatus("mandatory")
_MrmMonRepMulticastOctets_Type = Counter32
_MrmMonRepMulticastOctets_Object = MibTableColumn
mrmMonRepMulticastOctets = _MrmMonRepMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 8),
    _MrmMonRepMulticastOctets_Type()
)
mrmMonRepMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepMulticastOctets.setStatus("mandatory")
_MrmMonRepBroadcastOctets_Type = Counter32
_MrmMonRepBroadcastOctets_Object = MibTableColumn
mrmMonRepBroadcastOctets = _MrmMonRepBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 9),
    _MrmMonRepBroadcastOctets_Type()
)
mrmMonRepBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBroadcastOctets.setStatus("mandatory")
_MrmMonRepFCSErrors_Type = Counter32
_MrmMonRepFCSErrors_Object = MibTableColumn
mrmMonRepFCSErrors = _MrmMonRepFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 10),
    _MrmMonRepFCSErrors_Type()
)
mrmMonRepFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepFCSErrors.setStatus("mandatory")
_MrmMonRepAlignmentErrors_Type = Counter32
_MrmMonRepAlignmentErrors_Object = MibTableColumn
mrmMonRepAlignmentErrors = _MrmMonRepAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 11),
    _MrmMonRepAlignmentErrors_Type()
)
mrmMonRepAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepAlignmentErrors.setStatus("mandatory")
_MrmMonRepFrameTooLongs_Type = Counter32
_MrmMonRepFrameTooLongs_Object = MibTableColumn
mrmMonRepFrameTooLongs = _MrmMonRepFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 12),
    _MrmMonRepFrameTooLongs_Type()
)
mrmMonRepFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepFrameTooLongs.setStatus("mandatory")
_MrmMonRepShortEvents_Type = Counter32
_MrmMonRepShortEvents_Object = MibTableColumn
mrmMonRepShortEvents = _MrmMonRepShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 13),
    _MrmMonRepShortEvents_Type()
)
mrmMonRepShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepShortEvents.setStatus("mandatory")
_MrmMonRepRunts_Type = Counter32
_MrmMonRepRunts_Object = MibTableColumn
mrmMonRepRunts = _MrmMonRepRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 14),
    _MrmMonRepRunts_Type()
)
mrmMonRepRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepRunts.setStatus("mandatory")
_MrmMonRepTxCollisions_Type = Counter32
_MrmMonRepTxCollisions_Object = MibTableColumn
mrmMonRepTxCollisions = _MrmMonRepTxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 15),
    _MrmMonRepTxCollisions_Type()
)
mrmMonRepTxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepTxCollisions.setStatus("mandatory")
_MrmMonRepLateEvents_Type = Counter32
_MrmMonRepLateEvents_Object = MibTableColumn
mrmMonRepLateEvents = _MrmMonRepLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 16),
    _MrmMonRepLateEvents_Type()
)
mrmMonRepLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepLateEvents.setStatus("mandatory")
_MrmMonRepVeryLongEvents_Type = Counter32
_MrmMonRepVeryLongEvents_Object = MibTableColumn
mrmMonRepVeryLongEvents = _MrmMonRepVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 17),
    _MrmMonRepVeryLongEvents_Type()
)
mrmMonRepVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepVeryLongEvents.setStatus("mandatory")
_MrmMonRepDataRateMismatches_Type = Counter32
_MrmMonRepDataRateMismatches_Object = MibTableColumn
mrmMonRepDataRateMismatches = _MrmMonRepDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 18),
    _MrmMonRepDataRateMismatches_Type()
)
mrmMonRepDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepDataRateMismatches.setStatus("mandatory")
_MrmMonRepAutoPartitions_Type = Counter32
_MrmMonRepAutoPartitions_Object = MibTableColumn
mrmMonRepAutoPartitions = _MrmMonRepAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 19),
    _MrmMonRepAutoPartitions_Type()
)
mrmMonRepAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepAutoPartitions.setStatus("mandatory")
_MrmMonRepTotalErrors_Type = Counter32
_MrmMonRepTotalErrors_Object = MibTableColumn
mrmMonRepTotalErrors = _MrmMonRepTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 20),
    _MrmMonRepTotalErrors_Type()
)
mrmMonRepTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepTotalErrors.setStatus("mandatory")
_MrmMonRepBound0_Type = Counter32
_MrmMonRepBound0_Object = MibTableColumn
mrmMonRepBound0 = _MrmMonRepBound0_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 21),
    _MrmMonRepBound0_Type()
)
mrmMonRepBound0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound0.setStatus("mandatory")
_MrmMonRepBound1_Type = Counter32
_MrmMonRepBound1_Object = MibTableColumn
mrmMonRepBound1 = _MrmMonRepBound1_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 22),
    _MrmMonRepBound1_Type()
)
mrmMonRepBound1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound1.setStatus("mandatory")
_MrmMonRepBound2_Type = Counter32
_MrmMonRepBound2_Object = MibTableColumn
mrmMonRepBound2 = _MrmMonRepBound2_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 23),
    _MrmMonRepBound2_Type()
)
mrmMonRepBound2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound2.setStatus("mandatory")
_MrmMonRepBound3_Type = Counter32
_MrmMonRepBound3_Object = MibTableColumn
mrmMonRepBound3 = _MrmMonRepBound3_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 24),
    _MrmMonRepBound3_Type()
)
mrmMonRepBound3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound3.setStatus("mandatory")
_MrmMonRepBound4_Type = Counter32
_MrmMonRepBound4_Object = MibTableColumn
mrmMonRepBound4 = _MrmMonRepBound4_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 25),
    _MrmMonRepBound4_Type()
)
mrmMonRepBound4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound4.setStatus("mandatory")
_MrmMonRepBound5_Type = Counter32
_MrmMonRepBound5_Object = MibTableColumn
mrmMonRepBound5 = _MrmMonRepBound5_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 26),
    _MrmMonRepBound5_Type()
)
mrmMonRepBound5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBound5.setStatus("mandatory")


class _MrmMonRepAction_Type(Integer32):
    """Custom type mrmMonRepAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              128)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 1),
          ("noAction", 128))
    )


_MrmMonRepAction_Type.__name__ = "Integer32"
_MrmMonRepAction_Object = MibTableColumn
mrmMonRepAction = _MrmMonRepAction_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 27),
    _MrmMonRepAction_Type()
)
mrmMonRepAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmMonRepAction.setStatus("mandatory")
_MrmMonRepBandwidthUsed_Type = Counter32
_MrmMonRepBandwidthUsed_Object = MibTableColumn
mrmMonRepBandwidthUsed = _MrmMonRepBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 28),
    _MrmMonRepBandwidthUsed_Type()
)
mrmMonRepBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepBandwidthUsed.setStatus("mandatory")
_MrmMonRepErrorsPer10000Packets_Type = Counter32
_MrmMonRepErrorsPer10000Packets_Object = MibTableColumn
mrmMonRepErrorsPer10000Packets = _MrmMonRepErrorsPer10000Packets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 1, 1, 1, 29),
    _MrmMonRepErrorsPer10000Packets_Type()
)
mrmMonRepErrorsPer10000Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepErrorsPer10000Packets.setStatus("mandatory")
_MrmMonCardPackage_ObjectIdentity = ObjectIdentity
mrmMonCardPackage = _MrmMonCardPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2)
)
_MrmMonitorCardTable_Object = MibTable
mrmMonitorCardTable = _MrmMonitorCardTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mrmMonitorCardTable.setStatus("mandatory")
_MrmMonitorCardEntry_Object = MibTableRow
mrmMonitorCardEntry = _MrmMonitorCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1)
)
mrmMonitorCardEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "mrmMonCardServiceId"),
    (0, "LBHUB-FMS-MIB", "mrmMonCardIndex"),
)
if mibBuilder.loadTexts:
    mrmMonitorCardEntry.setStatus("mandatory")
_MrmMonCardServiceId_Type = Integer32
_MrmMonCardServiceId_Object = MibTableColumn
mrmMonCardServiceId = _MrmMonCardServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 1),
    _MrmMonCardServiceId_Type()
)
mrmMonCardServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardServiceId.setStatus("mandatory")
_MrmMonCardIndex_Type = Integer32
_MrmMonCardIndex_Object = MibTableColumn
mrmMonCardIndex = _MrmMonCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 2),
    _MrmMonCardIndex_Type()
)
mrmMonCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardIndex.setStatus("mandatory")
_MrmMonCardReadableFrames_Type = Counter32
_MrmMonCardReadableFrames_Object = MibTableColumn
mrmMonCardReadableFrames = _MrmMonCardReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 3),
    _MrmMonCardReadableFrames_Type()
)
mrmMonCardReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardReadableFrames.setStatus("mandatory")
_MrmMonCardUnicastFrames_Type = Counter32
_MrmMonCardUnicastFrames_Object = MibTableColumn
mrmMonCardUnicastFrames = _MrmMonCardUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 4),
    _MrmMonCardUnicastFrames_Type()
)
mrmMonCardUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardUnicastFrames.setStatus("mandatory")
_MrmMonCardMulticastFrames_Type = Counter32
_MrmMonCardMulticastFrames_Object = MibTableColumn
mrmMonCardMulticastFrames = _MrmMonCardMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 5),
    _MrmMonCardMulticastFrames_Type()
)
mrmMonCardMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardMulticastFrames.setStatus("mandatory")
_MrmMonCardBroadcastFrames_Type = Counter32
_MrmMonCardBroadcastFrames_Object = MibTableColumn
mrmMonCardBroadcastFrames = _MrmMonCardBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 6),
    _MrmMonCardBroadcastFrames_Type()
)
mrmMonCardBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBroadcastFrames.setStatus("mandatory")
_MrmMonCardReadableOctets_Type = Counter32
_MrmMonCardReadableOctets_Object = MibTableColumn
mrmMonCardReadableOctets = _MrmMonCardReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 7),
    _MrmMonCardReadableOctets_Type()
)
mrmMonCardReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardReadableOctets.setStatus("mandatory")
_MrmMonCardUnicastOctets_Type = Counter32
_MrmMonCardUnicastOctets_Object = MibTableColumn
mrmMonCardUnicastOctets = _MrmMonCardUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 8),
    _MrmMonCardUnicastOctets_Type()
)
mrmMonCardUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardUnicastOctets.setStatus("mandatory")
_MrmMonCardMulticastOctets_Type = Counter32
_MrmMonCardMulticastOctets_Object = MibTableColumn
mrmMonCardMulticastOctets = _MrmMonCardMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 9),
    _MrmMonCardMulticastOctets_Type()
)
mrmMonCardMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardMulticastOctets.setStatus("mandatory")
_MrmMonCardBroadcastOctets_Type = Counter32
_MrmMonCardBroadcastOctets_Object = MibTableColumn
mrmMonCardBroadcastOctets = _MrmMonCardBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 10),
    _MrmMonCardBroadcastOctets_Type()
)
mrmMonCardBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBroadcastOctets.setStatus("mandatory")
_MrmMonCardFCSErrors_Type = Counter32
_MrmMonCardFCSErrors_Object = MibTableColumn
mrmMonCardFCSErrors = _MrmMonCardFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 11),
    _MrmMonCardFCSErrors_Type()
)
mrmMonCardFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardFCSErrors.setStatus("mandatory")
_MrmMonCardAlignmentErrors_Type = Counter32
_MrmMonCardAlignmentErrors_Object = MibTableColumn
mrmMonCardAlignmentErrors = _MrmMonCardAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 12),
    _MrmMonCardAlignmentErrors_Type()
)
mrmMonCardAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardAlignmentErrors.setStatus("mandatory")
_MrmMonCardFrameTooLongs_Type = Counter32
_MrmMonCardFrameTooLongs_Object = MibTableColumn
mrmMonCardFrameTooLongs = _MrmMonCardFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 13),
    _MrmMonCardFrameTooLongs_Type()
)
mrmMonCardFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardFrameTooLongs.setStatus("mandatory")
_MrmMonCardShortEvents_Type = Counter32
_MrmMonCardShortEvents_Object = MibTableColumn
mrmMonCardShortEvents = _MrmMonCardShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 14),
    _MrmMonCardShortEvents_Type()
)
mrmMonCardShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardShortEvents.setStatus("mandatory")
_MrmMonCardRunts_Type = Counter32
_MrmMonCardRunts_Object = MibTableColumn
mrmMonCardRunts = _MrmMonCardRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 15),
    _MrmMonCardRunts_Type()
)
mrmMonCardRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardRunts.setStatus("mandatory")
_MrmMonCardLateEvents_Type = Counter32
_MrmMonCardLateEvents_Object = MibTableColumn
mrmMonCardLateEvents = _MrmMonCardLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 16),
    _MrmMonCardLateEvents_Type()
)
mrmMonCardLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardLateEvents.setStatus("mandatory")
_MrmMonCardVeryLongEvents_Type = Counter32
_MrmMonCardVeryLongEvents_Object = MibTableColumn
mrmMonCardVeryLongEvents = _MrmMonCardVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 17),
    _MrmMonCardVeryLongEvents_Type()
)
mrmMonCardVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardVeryLongEvents.setStatus("mandatory")
_MrmMonCardDataRateMismatches_Type = Counter32
_MrmMonCardDataRateMismatches_Object = MibTableColumn
mrmMonCardDataRateMismatches = _MrmMonCardDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 18),
    _MrmMonCardDataRateMismatches_Type()
)
mrmMonCardDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardDataRateMismatches.setStatus("mandatory")
_MrmMonCardAutoPartitions_Type = Counter32
_MrmMonCardAutoPartitions_Object = MibTableColumn
mrmMonCardAutoPartitions = _MrmMonCardAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 19),
    _MrmMonCardAutoPartitions_Type()
)
mrmMonCardAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardAutoPartitions.setStatus("mandatory")
_MrmMonCardTotalErrors_Type = Counter32
_MrmMonCardTotalErrors_Object = MibTableColumn
mrmMonCardTotalErrors = _MrmMonCardTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 20),
    _MrmMonCardTotalErrors_Type()
)
mrmMonCardTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardTotalErrors.setStatus("mandatory")
_MrmMonCardBound0_Type = Counter32
_MrmMonCardBound0_Object = MibTableColumn
mrmMonCardBound0 = _MrmMonCardBound0_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 21),
    _MrmMonCardBound0_Type()
)
mrmMonCardBound0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound0.setStatus("mandatory")
_MrmMonCardBound1_Type = Counter32
_MrmMonCardBound1_Object = MibTableColumn
mrmMonCardBound1 = _MrmMonCardBound1_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 22),
    _MrmMonCardBound1_Type()
)
mrmMonCardBound1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound1.setStatus("mandatory")
_MrmMonCardBound2_Type = Counter32
_MrmMonCardBound2_Object = MibTableColumn
mrmMonCardBound2 = _MrmMonCardBound2_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 23),
    _MrmMonCardBound2_Type()
)
mrmMonCardBound2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound2.setStatus("mandatory")
_MrmMonCardBound3_Type = Counter32
_MrmMonCardBound3_Object = MibTableColumn
mrmMonCardBound3 = _MrmMonCardBound3_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 24),
    _MrmMonCardBound3_Type()
)
mrmMonCardBound3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound3.setStatus("mandatory")
_MrmMonCardBound4_Type = Counter32
_MrmMonCardBound4_Object = MibTableColumn
mrmMonCardBound4 = _MrmMonCardBound4_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 25),
    _MrmMonCardBound4_Type()
)
mrmMonCardBound4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound4.setStatus("mandatory")
_MrmMonCardBound5_Type = Counter32
_MrmMonCardBound5_Object = MibTableColumn
mrmMonCardBound5 = _MrmMonCardBound5_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 26),
    _MrmMonCardBound5_Type()
)
mrmMonCardBound5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBound5.setStatus("mandatory")


class _MrmMonCardClearCounters_Type(Integer32):
    """Custom type mrmMonCardClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 2),
          ("noChangeCounters", 1))
    )


_MrmMonCardClearCounters_Type.__name__ = "Integer32"
_MrmMonCardClearCounters_Object = MibTableColumn
mrmMonCardClearCounters = _MrmMonCardClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 27),
    _MrmMonCardClearCounters_Type()
)
mrmMonCardClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmMonCardClearCounters.setStatus("mandatory")
_MrmMonCardBandwidthUsed_Type = Counter32
_MrmMonCardBandwidthUsed_Object = MibTableColumn
mrmMonCardBandwidthUsed = _MrmMonCardBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 28),
    _MrmMonCardBandwidthUsed_Type()
)
mrmMonCardBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardBandwidthUsed.setStatus("mandatory")
_MrmMonCardErrorsPer10000Packets_Type = Counter32
_MrmMonCardErrorsPer10000Packets_Object = MibTableColumn
mrmMonCardErrorsPer10000Packets = _MrmMonCardErrorsPer10000Packets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 2, 1, 1, 29),
    _MrmMonCardErrorsPer10000Packets_Type()
)
mrmMonCardErrorsPer10000Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardErrorsPer10000Packets.setStatus("mandatory")
_MrmMonPortPackage_ObjectIdentity = ObjectIdentity
mrmMonPortPackage = _MrmMonPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3)
)
_MrmMonitorPortTable_Object = MibTable
mrmMonitorPortTable = _MrmMonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1)
)
if mibBuilder.loadTexts:
    mrmMonitorPortTable.setStatus("mandatory")
_MrmMonitorPortEntry_Object = MibTableRow
mrmMonitorPortEntry = _MrmMonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1)
)
mrmMonitorPortEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "mrmMonPortServiceId"),
    (0, "LBHUB-FMS-MIB", "mrmMonPortCardIndex"),
    (0, "LBHUB-FMS-MIB", "mrmMonPortIndex"),
)
if mibBuilder.loadTexts:
    mrmMonitorPortEntry.setStatus("mandatory")


class _MrmMonPortServiceId_Type(Integer32):
    """Custom type mrmMonPortServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_MrmMonPortServiceId_Type.__name__ = "Integer32"
_MrmMonPortServiceId_Object = MibTableColumn
mrmMonPortServiceId = _MrmMonPortServiceId_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 1),
    _MrmMonPortServiceId_Type()
)
mrmMonPortServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortServiceId.setStatus("mandatory")
_MrmMonPortCardIndex_Type = Integer32
_MrmMonPortCardIndex_Object = MibTableColumn
mrmMonPortCardIndex = _MrmMonPortCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 2),
    _MrmMonPortCardIndex_Type()
)
mrmMonPortCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortCardIndex.setStatus("mandatory")
_MrmMonPortIndex_Type = Integer32
_MrmMonPortIndex_Object = MibTableColumn
mrmMonPortIndex = _MrmMonPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 3),
    _MrmMonPortIndex_Type()
)
mrmMonPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortIndex.setStatus("mandatory")
_MrmMonPortReadableFrames_Type = Counter32
_MrmMonPortReadableFrames_Object = MibTableColumn
mrmMonPortReadableFrames = _MrmMonPortReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 4),
    _MrmMonPortReadableFrames_Type()
)
mrmMonPortReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortReadableFrames.setStatus("mandatory")
_MrmMonPortUnicastFrames_Type = Counter32
_MrmMonPortUnicastFrames_Object = MibTableColumn
mrmMonPortUnicastFrames = _MrmMonPortUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 5),
    _MrmMonPortUnicastFrames_Type()
)
mrmMonPortUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortUnicastFrames.setStatus("mandatory")
_MrmMonPortMulticastFrames_Type = Counter32
_MrmMonPortMulticastFrames_Object = MibTableColumn
mrmMonPortMulticastFrames = _MrmMonPortMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 6),
    _MrmMonPortMulticastFrames_Type()
)
mrmMonPortMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortMulticastFrames.setStatus("mandatory")
_MrmMonPortBroadcastFrames_Type = Counter32
_MrmMonPortBroadcastFrames_Object = MibTableColumn
mrmMonPortBroadcastFrames = _MrmMonPortBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 7),
    _MrmMonPortBroadcastFrames_Type()
)
mrmMonPortBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBroadcastFrames.setStatus("mandatory")
_MrmMonPortReadableOctets_Type = Counter32
_MrmMonPortReadableOctets_Object = MibTableColumn
mrmMonPortReadableOctets = _MrmMonPortReadableOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 8),
    _MrmMonPortReadableOctets_Type()
)
mrmMonPortReadableOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortReadableOctets.setStatus("mandatory")
_MrmMonPortUnicastOctets_Type = Counter32
_MrmMonPortUnicastOctets_Object = MibTableColumn
mrmMonPortUnicastOctets = _MrmMonPortUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 9),
    _MrmMonPortUnicastOctets_Type()
)
mrmMonPortUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortUnicastOctets.setStatus("mandatory")
_MrmMonPortMulticastOctets_Type = Counter32
_MrmMonPortMulticastOctets_Object = MibTableColumn
mrmMonPortMulticastOctets = _MrmMonPortMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 10),
    _MrmMonPortMulticastOctets_Type()
)
mrmMonPortMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortMulticastOctets.setStatus("mandatory")
_MrmMonPortBroadcastOctets_Type = Counter32
_MrmMonPortBroadcastOctets_Object = MibTableColumn
mrmMonPortBroadcastOctets = _MrmMonPortBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 11),
    _MrmMonPortBroadcastOctets_Type()
)
mrmMonPortBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBroadcastOctets.setStatus("mandatory")
_MrmMonPortFCSErrors_Type = Counter32
_MrmMonPortFCSErrors_Object = MibTableColumn
mrmMonPortFCSErrors = _MrmMonPortFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 12),
    _MrmMonPortFCSErrors_Type()
)
mrmMonPortFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortFCSErrors.setStatus("mandatory")
_MrmMonPortAlignmentErrors_Type = Counter32
_MrmMonPortAlignmentErrors_Object = MibTableColumn
mrmMonPortAlignmentErrors = _MrmMonPortAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 13),
    _MrmMonPortAlignmentErrors_Type()
)
mrmMonPortAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortAlignmentErrors.setStatus("mandatory")
_MrmMonPortFrameTooLongs_Type = Counter32
_MrmMonPortFrameTooLongs_Object = MibTableColumn
mrmMonPortFrameTooLongs = _MrmMonPortFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 14),
    _MrmMonPortFrameTooLongs_Type()
)
mrmMonPortFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortFrameTooLongs.setStatus("mandatory")
_MrmMonPortShortEvents_Type = Counter32
_MrmMonPortShortEvents_Object = MibTableColumn
mrmMonPortShortEvents = _MrmMonPortShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 15),
    _MrmMonPortShortEvents_Type()
)
mrmMonPortShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortShortEvents.setStatus("mandatory")
_MrmMonPortRunts_Type = Counter32
_MrmMonPortRunts_Object = MibTableColumn
mrmMonPortRunts = _MrmMonPortRunts_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 16),
    _MrmMonPortRunts_Type()
)
mrmMonPortRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortRunts.setStatus("mandatory")
_MrmMonPortCollisions_Type = Counter32
_MrmMonPortCollisions_Object = MibTableColumn
mrmMonPortCollisions = _MrmMonPortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 17),
    _MrmMonPortCollisions_Type()
)
mrmMonPortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortCollisions.setStatus("mandatory")
_MrmMonPortLateEvents_Type = Counter32
_MrmMonPortLateEvents_Object = MibTableColumn
mrmMonPortLateEvents = _MrmMonPortLateEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 18),
    _MrmMonPortLateEvents_Type()
)
mrmMonPortLateEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortLateEvents.setStatus("mandatory")
_MrmMonPortVeryLongEvents_Type = Counter32
_MrmMonPortVeryLongEvents_Object = MibTableColumn
mrmMonPortVeryLongEvents = _MrmMonPortVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 19),
    _MrmMonPortVeryLongEvents_Type()
)
mrmMonPortVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortVeryLongEvents.setStatus("mandatory")
_MrmMonPortDataRateMismatches_Type = Counter32
_MrmMonPortDataRateMismatches_Object = MibTableColumn
mrmMonPortDataRateMismatches = _MrmMonPortDataRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 20),
    _MrmMonPortDataRateMismatches_Type()
)
mrmMonPortDataRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortDataRateMismatches.setStatus("mandatory")
_MrmMonPortAutoPartitions_Type = Counter32
_MrmMonPortAutoPartitions_Object = MibTableColumn
mrmMonPortAutoPartitions = _MrmMonPortAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 21),
    _MrmMonPortAutoPartitions_Type()
)
mrmMonPortAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortAutoPartitions.setStatus("mandatory")
_MrmMonPortTotalErrors_Type = Counter32
_MrmMonPortTotalErrors_Object = MibTableColumn
mrmMonPortTotalErrors = _MrmMonPortTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 22),
    _MrmMonPortTotalErrors_Type()
)
mrmMonPortTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortTotalErrors.setStatus("mandatory")
_MrmMonPortBound0_Type = Counter32
_MrmMonPortBound0_Object = MibTableColumn
mrmMonPortBound0 = _MrmMonPortBound0_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 23),
    _MrmMonPortBound0_Type()
)
mrmMonPortBound0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound0.setStatus("mandatory")
_MrmMonPortBound1_Type = Counter32
_MrmMonPortBound1_Object = MibTableColumn
mrmMonPortBound1 = _MrmMonPortBound1_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 24),
    _MrmMonPortBound1_Type()
)
mrmMonPortBound1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound1.setStatus("mandatory")
_MrmMonPortBound2_Type = Counter32
_MrmMonPortBound2_Object = MibTableColumn
mrmMonPortBound2 = _MrmMonPortBound2_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 25),
    _MrmMonPortBound2_Type()
)
mrmMonPortBound2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound2.setStatus("mandatory")
_MrmMonPortBound3_Type = Counter32
_MrmMonPortBound3_Object = MibTableColumn
mrmMonPortBound3 = _MrmMonPortBound3_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 26),
    _MrmMonPortBound3_Type()
)
mrmMonPortBound3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound3.setStatus("mandatory")
_MrmMonPortBound4_Type = Counter32
_MrmMonPortBound4_Object = MibTableColumn
mrmMonPortBound4 = _MrmMonPortBound4_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 27),
    _MrmMonPortBound4_Type()
)
mrmMonPortBound4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound4.setStatus("mandatory")
_MrmMonPortBound5_Type = Counter32
_MrmMonPortBound5_Object = MibTableColumn
mrmMonPortBound5 = _MrmMonPortBound5_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 28),
    _MrmMonPortBound5_Type()
)
mrmMonPortBound5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBound5.setStatus("mandatory")
_MrmMonPortBandwidthUsed_Type = Counter32
_MrmMonPortBandwidthUsed_Object = MibTableColumn
mrmMonPortBandwidthUsed = _MrmMonPortBandwidthUsed_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 29),
    _MrmMonPortBandwidthUsed_Type()
)
mrmMonPortBandwidthUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortBandwidthUsed.setStatus("mandatory")
_MrmMonPortErrorsPer10000Packets_Type = Counter32
_MrmMonPortErrorsPer10000Packets_Object = MibTableColumn
mrmMonPortErrorsPer10000Packets = _MrmMonPortErrorsPer10000Packets_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 30),
    _MrmMonPortErrorsPer10000Packets_Type()
)
mrmMonPortErrorsPer10000Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortErrorsPer10000Packets.setStatus("mandatory")


class _MrmMonPortClearCounters_Type(Integer32):
    """Custom type mrmMonPortClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 2),
          ("noChangeCounters", 1))
    )


_MrmMonPortClearCounters_Type.__name__ = "Integer32"
_MrmMonPortClearCounters_Object = MibTableColumn
mrmMonPortClearCounters = _MrmMonPortClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 31),
    _MrmMonPortClearCounters_Type()
)
mrmMonPortClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mrmMonPortClearCounters.setStatus("mandatory")
_MrmMonPortLastAddress_Type = OctetString
_MrmMonPortLastAddress_Object = MibTableColumn
mrmMonPortLastAddress = _MrmMonPortLastAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 32),
    _MrmMonPortLastAddress_Type()
)
mrmMonPortLastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortLastAddress.setStatus("mandatory")
_MrmMonPortAddressChanges_Type = Counter32
_MrmMonPortAddressChanges_Object = MibTableColumn
mrmMonPortAddressChanges = _MrmMonPortAddressChanges_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 3, 1, 1, 33),
    _MrmMonPortAddressChanges_Type()
)
mrmMonPortAddressChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortAddressChanges.setStatus("mandatory")
_MrmMonDummyPackage_ObjectIdentity = ObjectIdentity
mrmMonDummyPackage = _MrmMonDummyPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 4)
)
_TrafficLevel_Type = Counter32
_TrafficLevel_Object = MibScalar
trafficLevel = _TrafficLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 4, 1),
    _TrafficLevel_Type()
)
trafficLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trafficLevel.setStatus("deprecated")
_ErrorFrames_Type = Counter32
_ErrorFrames_Object = MibScalar
errorFrames = _ErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 4, 2),
    _ErrorFrames_Type()
)
errorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorFrames.setStatus("deprecated")
_MrmMonRepeaterSmartPackage_ObjectIdentity = ObjectIdentity
mrmMonRepeaterSmartPackage = _MrmMonRepeaterSmartPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 5)
)
_MrmMonRepeaterTrafficLevel_Type = Counter32
_MrmMonRepeaterTrafficLevel_Object = MibScalar
mrmMonRepeaterTrafficLevel = _MrmMonRepeaterTrafficLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 5, 1),
    _MrmMonRepeaterTrafficLevel_Type()
)
mrmMonRepeaterTrafficLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepeaterTrafficLevel.setStatus("mandatory")
_MrmMonRepeaterErrorFrames_Type = Counter32
_MrmMonRepeaterErrorFrames_Object = MibScalar
mrmMonRepeaterErrorFrames = _MrmMonRepeaterErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 5, 2),
    _MrmMonRepeaterErrorFrames_Type()
)
mrmMonRepeaterErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonRepeaterErrorFrames.setStatus("mandatory")
_MrmMonCardSmartPackage_ObjectIdentity = ObjectIdentity
mrmMonCardSmartPackage = _MrmMonCardSmartPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 6)
)
_MrmMonCardTrafficLevel_Type = Counter32
_MrmMonCardTrafficLevel_Object = MibScalar
mrmMonCardTrafficLevel = _MrmMonCardTrafficLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 6, 1),
    _MrmMonCardTrafficLevel_Type()
)
mrmMonCardTrafficLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardTrafficLevel.setStatus("mandatory")
_MrmMonCardErrorFrames_Type = Counter32
_MrmMonCardErrorFrames_Object = MibScalar
mrmMonCardErrorFrames = _MrmMonCardErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 6, 2),
    _MrmMonCardErrorFrames_Type()
)
mrmMonCardErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonCardErrorFrames.setStatus("mandatory")
_MrmMonPortSmartPackage_ObjectIdentity = ObjectIdentity
mrmMonPortSmartPackage = _MrmMonPortSmartPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 7)
)
_MrmMonPortTrafficLevel_Type = Counter32
_MrmMonPortTrafficLevel_Object = MibScalar
mrmMonPortTrafficLevel = _MrmMonPortTrafficLevel_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 7, 1),
    _MrmMonPortTrafficLevel_Type()
)
mrmMonPortTrafficLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortTrafficLevel.setStatus("mandatory")
_MrmMonPortErrorFrames_Type = Counter32
_MrmMonPortErrorFrames_Object = MibScalar
mrmMonPortErrorFrames = _MrmMonPortErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 17, 2, 7, 2),
    _MrmMonPortErrorFrames_Type()
)
mrmMonPortErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mrmMonPortErrorFrames.setStatus("mandatory")
_BridgeMgmt_ObjectIdentity = ObjectIdentity
bridgeMgmt = _BridgeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 18)
)
_Fault_ObjectIdentity = ObjectIdentity
fault = _Fault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 19)
)


class _FaultModifiedFlag_Type(Integer32):
    """Custom type faultModifiedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clean-read", 1),
          ("modified", 2))
    )


_FaultModifiedFlag_Type.__name__ = "Integer32"
_FaultModifiedFlag_Object = MibScalar
faultModifiedFlag = _FaultModifiedFlag_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 1),
    _FaultModifiedFlag_Type()
)
faultModifiedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faultModifiedFlag.setStatus("mandatory")
_FaultTable_Object = MibTable
faultTable = _FaultTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2)
)
if mibBuilder.loadTexts:
    faultTable.setStatus("mandatory")
_FaultEntry_Object = MibTableRow
faultEntry = _FaultEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1)
)
faultEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "faultIndex"),
)
if mibBuilder.loadTexts:
    faultEntry.setStatus("mandatory")
_FaultIndex_Type = Integer32
_FaultIndex_Object = MibTableColumn
faultIndex = _FaultIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 1),
    _FaultIndex_Type()
)
faultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultIndex.setStatus("mandatory")
_FaultErrorNumber_Type = Integer32
_FaultErrorNumber_Object = MibTableColumn
faultErrorNumber = _FaultErrorNumber_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 2),
    _FaultErrorNumber_Type()
)
faultErrorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultErrorNumber.setStatus("mandatory")
_FaultTimeStamp_Type = TimeTicks
_FaultTimeStamp_Object = MibTableColumn
faultTimeStamp = _FaultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 3),
    _FaultTimeStamp_Type()
)
faultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultTimeStamp.setStatus("mandatory")
_FaultRestartCount_Type = Integer32
_FaultRestartCount_Object = MibTableColumn
faultRestartCount = _FaultRestartCount_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 19, 2, 1, 4),
    _FaultRestartCount_Type()
)
faultRestartCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    faultRestartCount.setStatus("mandatory")
_Poll_ObjectIdentity = ObjectIdentity
poll = _Poll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 20)
)
_PollTable_Object = MibTable
pollTable = _PollTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1)
)
if mibBuilder.loadTexts:
    pollTable.setStatus("mandatory")
_PollTableEntry_Object = MibTableRow
pollTableEntry = _PollTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1)
)
pollTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "pollIndex"),
)
if mibBuilder.loadTexts:
    pollTableEntry.setStatus("mandatory")


class _PollIndex_Type(Integer32):
    """Custom type pollIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PollIndex_Type.__name__ = "Integer32"
_PollIndex_Object = MibTableColumn
pollIndex = _PollIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 1),
    _PollIndex_Type()
)
pollIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollIndex.setStatus("mandatory")


class _PollAddress_Type(DisplayString):
    """Custom type pollAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_PollAddress_Type.__name__ = "DisplayString"
_PollAddress_Object = MibTableColumn
pollAddress = _PollAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 2),
    _PollAddress_Type()
)
pollAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollAddress.setStatus("mandatory")


class _PollProtocol_Type(Integer32):
    """Custom type pollProtocol based on Integer32"""
    defaultValue = 1

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
        *(("ip", 2),
          ("ipx", 3),
          ("learn", 4),
          ("llc", 5),
          ("unknown", 1))
    )


_PollProtocol_Type.__name__ = "Integer32"
_PollProtocol_Object = MibTableColumn
pollProtocol = _PollProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 3),
    _PollProtocol_Type()
)
pollProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollProtocol.setStatus("mandatory")


class _PollRate_Type(Integer32):
    """Custom type pollRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("every-30-minutes", 5),
          ("every-30-seconds", 2),
          ("every-5-minutes", 4),
          ("every-hour", 6),
          ("every-minute", 3),
          ("once-only", 1))
    )


_PollRate_Type.__name__ = "Integer32"
_PollRate_Object = MibTableColumn
pollRate = _PollRate_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 4),
    _PollRate_Type()
)
pollRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollRate.setStatus("mandatory")


class _PollTargetType_Type(Integer32):
    """Custom type pollTargetType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("file-server", 2),
          ("other", 1))
    )


_PollTargetType_Type.__name__ = "Integer32"
_PollTargetType_Object = MibTableColumn
pollTargetType = _PollTargetType_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 5),
    _PollTargetType_Type()
)
pollTargetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollTargetType.setStatus("mandatory")


class _PollLastPollSent_Type(TimeTicks):
    """Custom type pollLastPollSent based on TimeTicks"""
    defaultValue = 0


_PollLastPollSent_Object = MibTableColumn
pollLastPollSent = _PollLastPollSent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 6),
    _PollLastPollSent_Type()
)
pollLastPollSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollLastPollSent.setStatus("mandatory")


class _PollRoundTripTime_Type(Integer32):
    """Custom type pollRoundTripTime based on Integer32"""
    defaultValue = 0


_PollRoundTripTime_Object = MibTableColumn
pollRoundTripTime = _PollRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 7),
    _PollRoundTripTime_Type()
)
pollRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollRoundTripTime.setStatus("mandatory")


class _PollInformation_Type(DisplayString):
    """Custom type pollInformation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_PollInformation_Type.__name__ = "DisplayString"
_PollInformation_Object = MibTableColumn
pollInformation = _PollInformation_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 8),
    _PollInformation_Type()
)
pollInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollInformation.setStatus("mandatory")


class _PollAlarmIndex_Type(Integer32):
    """Custom type pollAlarmIndex based on Integer32"""
    defaultValue = 0


_PollAlarmIndex_Object = MibTableColumn
pollAlarmIndex = _PollAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 9),
    _PollAlarmIndex_Type()
)
pollAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollAlarmIndex.setStatus("mandatory")
_PollOwner_Type = DisplayString
_PollOwner_Object = MibTableColumn
pollOwner = _PollOwner_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 10),
    _PollOwner_Type()
)
pollOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollOwner.setStatus("mandatory")


class _PollRowStatus_Type(Integer32):
    """Custom type pollRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_PollRowStatus_Type.__name__ = "Integer32"
_PollRowStatus_Object = MibTableColumn
pollRowStatus = _PollRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 1, 1, 11),
    _PollRowStatus_Type()
)
pollRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pollRowStatus.setStatus("mandatory")


class _PollNextFreeIndex_Type(Integer32):
    """Custom type pollNextFreeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PollNextFreeIndex_Type.__name__ = "Integer32"
_PollNextFreeIndex_Object = MibScalar
pollNextFreeIndex = _PollNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 20, 2),
    _PollNextFreeIndex_Type()
)
pollNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pollNextFreeIndex.setStatus("mandatory")
_PowerSupply_ObjectIdentity = ObjectIdentity
powerSupply = _PowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 21)
)
_PowerStackPackage_ObjectIdentity = ObjectIdentity
powerStackPackage = _PowerStackPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1)
)


class _PowerStackBackupPresent_Type(Integer32):
    """Custom type powerStackBackupPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("present", 2))
    )


_PowerStackBackupPresent_Type.__name__ = "Integer32"
_PowerStackBackupPresent_Object = MibScalar
powerStackBackupPresent = _PowerStackBackupPresent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1, 1),
    _PowerStackBackupPresent_Type()
)
powerStackBackupPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStackBackupPresent.setStatus("mandatory")


class _PowerStackBackupData_Type(OctetString):
    """Custom type powerStackBackupData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_PowerStackBackupData_Type.__name__ = "OctetString"
_PowerStackBackupData_Object = MibScalar
powerStackBackupData = _PowerStackBackupData_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1, 2),
    _PowerStackBackupData_Type()
)
powerStackBackupData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStackBackupData.setStatus("mandatory")
_PowerStackTable_Object = MibTable
powerStackTable = _PowerStackTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1, 3)
)
if mibBuilder.loadTexts:
    powerStackTable.setStatus("mandatory")
_PowerStackTableEntry_Object = MibTableRow
powerStackTableEntry = _PowerStackTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1, 3, 1)
)
powerStackTableEntry.setIndexNames(
    (0, "LBHUB-FMS-MIB", "powerStackTableIndex"),
)
if mibBuilder.loadTexts:
    powerStackTableEntry.setStatus("mandatory")
_PowerStackTableIndex_Type = Integer32
_PowerStackTableIndex_Object = MibTableColumn
powerStackTableIndex = _PowerStackTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1, 3, 1, 1),
    _PowerStackTableIndex_Type()
)
powerStackTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStackTableIndex.setStatus("mandatory")


class _PowerStackRBSPresent_Type(Integer32):
    """Custom type powerStackRBSPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rbsNotApplicable", 1),
          ("rbsNotPresent", 3),
          ("rbsPresent", 2))
    )


_PowerStackRBSPresent_Type.__name__ = "Integer32"
_PowerStackRBSPresent_Object = MibTableColumn
powerStackRBSPresent = _PowerStackRBSPresent_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1, 3, 1, 2),
    _PowerStackRBSPresent_Type()
)
powerStackRBSPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStackRBSPresent.setStatus("mandatory")


class _PowerStackRBSStatus_Type(Integer32):
    """Custom type powerStackRBSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rbsFault", 3),
          ("rbsNotApplicable", 1),
          ("rbsOK", 2))
    )


_PowerStackRBSStatus_Type.__name__ = "Integer32"
_PowerStackRBSStatus_Object = MibTableColumn
powerStackRBSStatus = _PowerStackRBSStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 21, 1, 3, 1, 3),
    _PowerStackRBSStatus_Type()
)
powerStackRBSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerStackRBSStatus.setStatus("mandatory")
_NetBuilder_mib_ObjectIdentity = ObjectIdentity
netBuilder_mib = _NetBuilder_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 11)
)
_LBridgeECS_mib_ObjectIdentity = ObjectIdentity
lBridgeECS_mib = _LBridgeECS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 12)
)
_DeskMan_mib_ObjectIdentity = ObjectIdentity
deskMan_mib = _DeskMan_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 13)
)
_LinkBuilderMSH_mib_ObjectIdentity = ObjectIdentity
linkBuilderMSH_mib = _LinkBuilderMSH_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 14)
)
_LinkBuilderFMS_mib_ObjectIdentity = ObjectIdentity
linkBuilderFMS_mib = _LinkBuilderFMS_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 15)
)
_LinkBuilderFDDI_wghub_mib_ObjectIdentity = ObjectIdentity
linkBuilderFDDI_wghub_mib = _LinkBuilderFDDI_wghub_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 16)
)
_LinkSwitch_mib_ObjectIdentity = ObjectIdentity
linkSwitch_mib = _LinkSwitch_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 17)
)

# Managed Objects groups


# Notification objects

risingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 1)
)
risingAlarm.setObjects(
      *(("LBHUB-FMS-MIB", "alarmIndex"),
        ("LBHUB-FMS-MIB", "alarmVariable"),
        ("LBHUB-FMS-MIB", "alarmSampleType"),
        ("LBHUB-FMS-MIB", "alarmValue"),
        ("LBHUB-FMS-MIB", "alarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    risingAlarm.setStatus(
        ""
    )

fallingAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 0, 2)
)
fallingAlarm.setObjects(
      *(("LBHUB-FMS-MIB", "alarmIndex"),
        ("LBHUB-FMS-MIB", "alarmVariable"),
        ("LBHUB-FMS-MIB", "alarmSampleType"),
        ("LBHUB-FMS-MIB", "alarmValue"),
        ("LBHUB-FMS-MIB", "alarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    fallingAlarm.setStatus(
        ""
    )

deprRptrHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 1)
)
deprRptrHealth.setObjects(
    ("LBHUB-FMS-MIB", "deprRptrOperStatus")
)
if mibBuilder.loadTexts:
    deprRptrHealth.setStatus(
        ""
    )

deprRptrGroupChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 2)
)
deprRptrGroupChange.setObjects(
    ("LBHUB-FMS-MIB", "deprRptrGroupIndex")
)
if mibBuilder.loadTexts:
    deprRptrGroupChange.setStatus(
        ""
    )

deprRptrResetEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 3)
)
deprRptrResetEvent.setObjects(
    ("LBHUB-FMS-MIB", "deprRptrOperStatus")
)
if mibBuilder.loadTexts:
    deprRptrResetEvent.setStatus(
        ""
    )

heartbeatEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 13)
)
if mibBuilder.loadTexts:
    heartbeatEvent.setStatus(
        ""
    )

localManagementUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 14)
)
if mibBuilder.loadTexts:
    localManagementUpdate.setStatus(
        ""
    )

securityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 15)
)
securityViolation.setObjects(
      *(("LBHUB-FMS-MIB", "ascUserNameForLastAttemptedLogin"),
        ("LBHUB-FMS-MIB", "ascLoginStatus"))
)
if mibBuilder.loadTexts:
    securityViolation.setStatus(
        ""
    )

gaugesThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 16)
)
gaugesThresholdTrap.setObjects(
      *(("LBHUB-FMS-MIB", "gaugeItemId"),
        ("LBHUB-FMS-MIB", "gaugeThresholdLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    gaugesThresholdTrap.setStatus(
        ""
    )

gaugesRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 17)
)
gaugesRecoveryTrap.setObjects(
      *(("LBHUB-FMS-MIB", "gaugeItemId"),
        ("LBHUB-FMS-MIB", "gaugeRecoveryLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    gaugesRecoveryTrap.setStatus(
        ""
    )

slFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 18)
)
slFailed.setObjects(
    ("LBHUB-FMS-MIB", "slLoadStatus")
)
if mibBuilder.loadTexts:
    slFailed.setStatus(
        ""
    )

estStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 19)
)
if mibBuilder.loadTexts:
    estStateChange.setStatus(
        ""
    )

estTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 20)
)
if mibBuilder.loadTexts:
    estTableFull.setStatus(
        ""
    )

deprRpMauJabberTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 24)
)
deprRpMauJabberTrap.setObjects(
    ("LBHUB-FMS-MIB", "deprRptrOperStatus")
)
if mibBuilder.loadTexts:
    deprRpMauJabberTrap.setStatus(
        ""
    )

vmMauMediaAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 25)
)
vmMauMediaAvailable.setObjects(
    ("MAU-MIB", "rpMauMediaAvailable")
)
if mibBuilder.loadTexts:
    vmMauMediaAvailable.setStatus(
        ""
    )

vmAutoPartitionState = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 26)
)
vmAutoPartitionState.setObjects(
    ("MAU-MIB", "rptrPortAutoPartitionState")
)
if mibBuilder.loadTexts:
    vmAutoPartitionState.setStatus(
        ""
    )

repPartitionStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 38)
)
repPartitionStateChange.setObjects(
    ("LBHUB-FMS-MIB", "mrmPortAutoPartitionState")
)
if mibBuilder.loadTexts:
    repPartitionStateChange.setStatus(
        ""
    )

repLinkStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 39)
)
repLinkStateChange.setObjects(
    ("LBHUB-FMS-MIB", "mrmPortLinkState")
)
if mibBuilder.loadTexts:
    repLinkStateChange.setStatus(
        ""
    )

repAdminStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 40)
)
repAdminStateChange.setObjects(
    ("LBHUB-FMS-MIB", "mrmPortAdminStatus")
)
if mibBuilder.loadTexts:
    repAdminStateChange.setStatus(
        ""
    )

repPortTopUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 41)
)
repPortTopUsage.setObjects(
      *(("LBHUB-FMS-MIB", "mrmMonPortBandwidthUsed"),
        ("LBHUB-FMS-MIB", "gaugeThresholdLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repPortTopUsage.setStatus(
        ""
    )

repPortErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 42)
)
repPortErrors.setObjects(
      *(("LBHUB-FMS-MIB", "mrmMonPortErrorsPer10000Packets"),
        ("LBHUB-FMS-MIB", "gaugeThresholdLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repPortErrors.setStatus(
        ""
    )

resResilienceSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 43)
)
resResilienceSwitch.setObjects(
      *(("LBHUB-FMS-MIB", "resMainState"),
        ("LBHUB-FMS-MIB", "resStandbyState"))
)
if mibBuilder.loadTexts:
    resResilienceSwitch.setStatus(
        ""
    )

resStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 44)
)
resStateChange.setObjects(
      *(("LBHUB-FMS-MIB", "resMainState"),
        ("LBHUB-FMS-MIB", "resStandbyState"))
)
if mibBuilder.loadTexts:
    resStateChange.setStatus(
        ""
    )

pollTableSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 61)
)
pollTableSuccessTrap.setObjects(
      *(("LBHUB-FMS-MIB", "pollAddress"),
        ("LBHUB-FMS-MIB", "pollProtocol"),
        ("LBHUB-FMS-MIB", "pollTargetType"))
)
if mibBuilder.loadTexts:
    pollTableSuccessTrap.setStatus(
        ""
    )

pollTableFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 62)
)
pollTableFailedTrap.setObjects(
      *(("LBHUB-FMS-MIB", "pollAddress"),
        ("LBHUB-FMS-MIB", "pollProtocol"),
        ("LBHUB-FMS-MIB", "pollTargetType"))
)
if mibBuilder.loadTexts:
    pollTableFailedTrap.setStatus(
        ""
    )

powerStackBackupFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 63)
)
if mibBuilder.loadTexts:
    powerStackBackupFault.setStatus(
        ""
    )

powerStackBackupRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 64)
)
if mibBuilder.loadTexts:
    powerStackBackupRecovered.setStatus(
        ""
    )

dudUnauthorisedDevice = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 66)
)
dudUnauthorisedDevice.setObjects(
    ("LBHUB-FMS-MIB", "mrmPortDUDAction")
)
if mibBuilder.loadTexts:
    dudUnauthorisedDevice.setStatus(
        ""
    )

repRepTopUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 67)
)
repRepTopUsage.setObjects(
      *(("LBHUB-FMS-MIB", "mrmMonRepBandwidthUsed"),
        ("LBHUB-FMS-MIB", "gaugeThresholdLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repRepTopUsage.setStatus(
        ""
    )

repRepErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 68)
)
repRepErrors.setObjects(
      *(("LBHUB-FMS-MIB", "mrmMonRepErrorsPer10000Packets"),
        ("LBHUB-FMS-MIB", "gaugeThresholdLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repRepErrors.setStatus(
        ""
    )

repCardTopUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 69)
)
repCardTopUsage.setObjects(
      *(("LBHUB-FMS-MIB", "mrmMonCardBandwidthUsed"),
        ("LBHUB-FMS-MIB", "gaugeThresholdLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repCardTopUsage.setStatus(
        ""
    )

repCardErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 0, 70)
)
repCardErrors.setObjects(
      *(("LBHUB-FMS-MIB", "mrmMonCardErrorsPer10000Packets"),
        ("LBHUB-FMS-MIB", "gaugeThresholdLevel"),
        ("LBHUB-FMS-MIB", "gaugeSamplePeriod"),
        ("LBHUB-FMS-MIB", "gaugeSamplesPerAverage"))
)
if mibBuilder.loadTexts:
    repCardErrors.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LBHUB-FMS-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "mib-2": mib_2,
       "system": system,
       "interfaces": interfaces,
       "at": at,
       "ip": ip,
       "icmp": icmp,
       "tcp": tcp,
       "udp": udp,
       "egp": egp,
       "transmission": transmission,
       "snmp": snmp,
       "rmon": rmon,
       "risingAlarm": risingAlarm,
       "fallingAlarm": fallingAlarm,
       "statistics": statistics,
       "history": history,
       "alarm": alarm,
       "alarmTable": alarmTable,
       "alarmEntry": alarmEntry,
       "alarmIndex": alarmIndex,
       "alarmInterval": alarmInterval,
       "alarmVariable": alarmVariable,
       "alarmSampleType": alarmSampleType,
       "alarmValue": alarmValue,
       "alarmStartupAlarm": alarmStartupAlarm,
       "alarmRisingThreshold": alarmRisingThreshold,
       "alarmFallingThreshold": alarmFallingThreshold,
       "alarmRisingEventIndex": alarmRisingEventIndex,
       "alarmFallingEventIndex": alarmFallingEventIndex,
       "alarmOwner": alarmOwner,
       "alarmStatus": alarmStatus,
       "hosts": hosts,
       "hostTopN": hostTopN,
       "matrix": matrix,
       "filter": filter,
       "capture": capture,
       "event": event,
       "eventTable": eventTable,
       "eventEntry": eventEntry,
       "eventIndex": eventIndex,
       "eventDescription": eventDescription,
       "eventType": eventType,
       "eventCommunity": eventCommunity,
       "eventLastTimeSent": eventLastTimeSent,
       "eventOwner": eventOwner,
       "eventStatus": eventStatus,
       "logTable": logTable,
       "logEntry": logEntry,
       "logEventIndex": logEventIndex,
       "logIndex": logIndex,
       "logTime": logTime,
       "logDescription": logDescription,
       "dot1dBridge": dot1dBridge,
       "novell": novell,
       "mibDoc": mibDoc,
       "ipx": ipx,
       "ipxSystem": ipxSystem,
       "ipxBasicSysTable": ipxBasicSysTable,
       "ipxBasicSysEntry": ipxBasicSysEntry,
       "ipxBasicSysInstance": ipxBasicSysInstance,
       "ipxBasicSysExistState": ipxBasicSysExistState,
       "ipxBasicSysNetNumber": ipxBasicSysNetNumber,
       "ipxBasicSysNode": ipxBasicSysNode,
       "ipxBasicSysName": ipxBasicSysName,
       "ipxBasicSysInReceives": ipxBasicSysInReceives,
       "ipxBasicSysInHdrErrors": ipxBasicSysInHdrErrors,
       "ipxBasicSysInUnknownSockets": ipxBasicSysInUnknownSockets,
       "ipxBasicSysInDiscards": ipxBasicSysInDiscards,
       "ipxBasicSysInBadChecksums": ipxBasicSysInBadChecksums,
       "ipxBasicSysInDelivers": ipxBasicSysInDelivers,
       "ipxBasicSysNoRoutes": ipxBasicSysNoRoutes,
       "ipxBasicSysOutRequests": ipxBasicSysOutRequests,
       "ipxBasicSysOutMalformedRequests": ipxBasicSysOutMalformedRequests,
       "ipxBasicSysOutDiscards": ipxBasicSysOutDiscards,
       "ipxBasicSysOutPackets": ipxBasicSysOutPackets,
       "ipxBasicSysConfigSockets": ipxBasicSysConfigSockets,
       "ipxBasicSysOpenSocketFails": ipxBasicSysOpenSocketFails,
       "ipxAdvSysTable": ipxAdvSysTable,
       "ipxAdvSysEntry": ipxAdvSysEntry,
       "ipxAdvSysInstance": ipxAdvSysInstance,
       "ipxAdvSysMaxPathSplits": ipxAdvSysMaxPathSplits,
       "ipxAdvSysMaxHops": ipxAdvSysMaxHops,
       "ipxAdvSysTooManyHops": ipxAdvSysTooManyHops,
       "ipxAdvSysInFiltered": ipxAdvSysInFiltered,
       "ipxAdvSysCompressDiscards": ipxAdvSysCompressDiscards,
       "ipxAdvSysNETBIOSPackets": ipxAdvSysNETBIOSPackets,
       "ipxAdvSysForwPackets": ipxAdvSysForwPackets,
       "ipxAdvSysOutFiltered": ipxAdvSysOutFiltered,
       "ipxAdvSysOutCompressDiscards": ipxAdvSysOutCompressDiscards,
       "ipxAdvSysCircCount": ipxAdvSysCircCount,
       "ipxAdvSysDestCount": ipxAdvSysDestCount,
       "ipxAdvSysServCount": ipxAdvSysServCount,
       "ipxCircuit": ipxCircuit,
       "ipxForwarding": ipxForwarding,
       "ipxServices": ipxServices,
       "ipxTraps": ipxTraps,
       "a3Com": a3Com,
       "deprRptrHealth": deprRptrHealth,
       "deprRptrGroupChange": deprRptrGroupChange,
       "deprRptrResetEvent": deprRptrResetEvent,
       "heartbeatEvent": heartbeatEvent,
       "localManagementUpdate": localManagementUpdate,
       "securityViolation": securityViolation,
       "gaugesThresholdTrap": gaugesThresholdTrap,
       "gaugesRecoveryTrap": gaugesRecoveryTrap,
       "slFailed": slFailed,
       "estStateChange": estStateChange,
       "estTableFull": estTableFull,
       "deprRpMauJabberTrap": deprRpMauJabberTrap,
       "vmMauMediaAvailable": vmMauMediaAvailable,
       "vmAutoPartitionState": vmAutoPartitionState,
       "repPartitionStateChange": repPartitionStateChange,
       "repLinkStateChange": repLinkStateChange,
       "repAdminStateChange": repAdminStateChange,
       "repPortTopUsage": repPortTopUsage,
       "repPortErrors": repPortErrors,
       "resResilienceSwitch": resResilienceSwitch,
       "resStateChange": resStateChange,
       "pollTableSuccessTrap": pollTableSuccessTrap,
       "pollTableFailedTrap": pollTableFailedTrap,
       "powerStackBackupFault": powerStackBackupFault,
       "powerStackBackupRecovered": powerStackBackupRecovered,
       "dudUnauthorisedDevice": dudUnauthorisedDevice,
       "repRepTopUsage": repRepTopUsage,
       "repRepErrors": repRepErrors,
       "repCardTopUsage": repCardTopUsage,
       "repCardErrors": repCardErrors,
       "products": products,
       "terminalServer": terminalServer,
       "dedicatedBridgeServer": dedicatedBridgeServer,
       "dedicatedRouteServer": dedicatedRouteServer,
       "brouter": brouter,
       "genericMSWorkstation": genericMSWorkstation,
       "genericMSServer": genericMSServer,
       "genericUnixServer": genericUnixServer,
       "hub": hub,
       "linkBuilder3GH": linkBuilder3GH,
       "linkBuilder10BTi": linkBuilder10BTi,
       "linkBuilderECS": linkBuilderECS,
       "linkBuilderMSH": linkBuilderMSH,
       "linkBuilderFMS": linkBuilderFMS,
       "linkBuilderFDDIwg": linkBuilderFDDIwg,
       "linkBuilderFMSII": linkBuilderFMSII,
       "linkSwitchFMS": linkSwitchFMS,
       "linkSwitchMSH": linkSwitchMSH,
       "linkBuilderFMSLBridge": linkBuilderFMSLBridge,
       "cards": cards,
       "linkBuilder3GH-cards": linkBuilder3GH_cards,
       "linkBuilder10BTi-cards": linkBuilder10BTi_cards,
       "linkBuilder10BTi-cards-utp": linkBuilder10BTi_cards_utp,
       "linkBuilder10BT-cards-utp": linkBuilder10BT_cards_utp,
       "linkBuilderECS-cards": linkBuilderECS_cards,
       "linkBuilderMSH-cards": linkBuilderMSH_cards,
       "linkBuilderFMS-cards": linkBuilderFMS_cards,
       "linkBuilderFMS-cards-utp": linkBuilderFMS_cards_utp,
       "linkBuilderFMS-cards-coax": linkBuilderFMS_cards_coax,
       "linkBuilderFMS-cards-fiber": linkBuilderFMS_cards_fiber,
       "linkBuilderFMS-cards-12fiber": linkBuilderFMS_cards_12fiber,
       "linkBuilderFMS-cards-24utp": linkBuilderFMS_cards_24utp,
       "linkBuilderFMSII-cards": linkBuilderFMSII_cards,
       "linkBuilderFMSII-cards-12tp-rj45": linkBuilderFMSII_cards_12tp_rj45,
       "linkBuilderFMSII-cards-10coax-bnc": linkBuilderFMSII_cards_10coax_bnc,
       "linkBuilderFMSII-cards-6fiber-st": linkBuilderFMSII_cards_6fiber_st,
       "linkBuilderFMSII-cards-12fiber-st": linkBuilderFMSII_cards_12fiber_st,
       "linkBuilderFMSII-cards-24tp-rj45": linkBuilderFMSII_cards_24tp_rj45,
       "linkBuilderFMSII-cards-24tp-telco": linkBuilderFMSII_cards_24tp_telco,
       "chipsets": chipsets,
       "amp-mib": amp_mib,
       "genericTrap": genericTrap,
       "viewBuilderApps": viewBuilderApps,
       "specificTrap": specificTrap,
       "linkBuilder3GH-mib": linkBuilder3GH_mib,
       "linkBuilder10BTi-mib": linkBuilder10BTi_mib,
       "linkbuilderMonitorPackage": linkbuilderMonitorPackage,
       "vmMonBatteryStatus": vmMonBatteryStatus,
       "vmMonPOSTResults": vmMonPOSTResults,
       "vmMonFault": vmMonFault,
       "vmMonFaultModifiedFlag": vmMonFaultModifiedFlag,
       "vmMonFaultTable": vmMonFaultTable,
       "vmMonFaultEntry": vmMonFaultEntry,
       "vmMonFaultIndex": vmMonFaultIndex,
       "vmMonFaultErrorNumber": vmMonFaultErrorNumber,
       "vmMonFaultTimeStamp": vmMonFaultTimeStamp,
       "vmMonFaultRestartCount": vmMonFaultRestartCount,
       "vmMonDvtEcho": vmMonDvtEcho,
       "vmMonMgmtBusOverrunError": vmMonMgmtBusOverrunError,
       "vmMonMgmtBusFramingError": vmMonMgmtBusFramingError,
       "vmMonMgmtBusOverflowError": vmMonMgmtBusOverflowError,
       "vmMonMgmtBusFiFoFullCounter": vmMonMgmtBusFiFoFullCounter,
       "linkbuilderConfigPackage": linkbuilderConfigPackage,
       "vmConfigGroupTable": vmConfigGroupTable,
       "vmConfigGroupEntry": vmConfigGroupEntry,
       "vmConGroupIndex": vmConGroupIndex,
       "vmConGroupPortMask": vmConGroupPortMask,
       "vmConfigPortTable": vmConfigPortTable,
       "vmConfigPortEntry": vmConfigPortEntry,
       "vmConPortGroupIndex": vmConPortGroupIndex,
       "vmConPortIndex": vmConPortIndex,
       "vmConPortSquelch": vmConPortSquelch,
       "vmConPortLinkPulse": vmConPortLinkPulse,
       "vmConPortXoverSwitchState": vmConPortXoverSwitchState,
       "vmConPortType": vmConPortType,
       "vmConfigMediaTable": vmConfigMediaTable,
       "vmConfigMediaEntry": vmConfigMediaEntry,
       "vmConMediaIndex": vmConMediaIndex,
       "vmConMediaModuleRevNo": vmConMediaModuleRevNo,
       "vmConMediaModuleCardType": vmConMediaModuleCardType,
       "linkbuilderStatusPackage": linkbuilderStatusPackage,
       "deprSnmpDot3RptrMgt": deprSnmpDot3RptrMgt,
       "deprRptrBasicPackage": deprRptrBasicPackage,
       "deprRptrRptrInfo": deprRptrRptrInfo,
       "deprRptrGroupCapacity": deprRptrGroupCapacity,
       "deprRptrOperStatus": deprRptrOperStatus,
       "deprRptrHealthText": deprRptrHealthText,
       "deprRptrReset": deprRptrReset,
       "deprRptrNonDisruptTest": deprRptrNonDisruptTest,
       "deprRptrTotalPartitionedPorts": deprRptrTotalPartitionedPorts,
       "deprRptrGroupInfo": deprRptrGroupInfo,
       "deprRptrGroupTable": deprRptrGroupTable,
       "deprRptrGroupEntry": deprRptrGroupEntry,
       "deprRptrGroupIndex": deprRptrGroupIndex,
       "deprRptrGroupDescr": deprRptrGroupDescr,
       "deprRptrGroupObjectID": deprRptrGroupObjectID,
       "deprRptrGroupOperStatus": deprRptrGroupOperStatus,
       "deprRptrGroupLastOperStatusChange": deprRptrGroupLastOperStatusChange,
       "deprRptrGroupPortCapacity": deprRptrGroupPortCapacity,
       "deprRptrPortInfo": deprRptrPortInfo,
       "deprRptrPortTable": deprRptrPortTable,
       "deprRptrPortEntry": deprRptrPortEntry,
       "deprRptrPortGroupIndex": deprRptrPortGroupIndex,
       "deprRptrPortIndex": deprRptrPortIndex,
       "deprRptrPortAdminStatus": deprRptrPortAdminStatus,
       "deprRptrPortAutoPartitionState": deprRptrPortAutoPartitionState,
       "deprRptrPortOperStatus": deprRptrPortOperStatus,
       "deprRptrMonitorPackage": deprRptrMonitorPackage,
       "deprRptrMonitorRptrInfo": deprRptrMonitorRptrInfo,
       "deprRptrMonitorTransmitCollisions": deprRptrMonitorTransmitCollisions,
       "deprRptrMonitorGroupInfo": deprRptrMonitorGroupInfo,
       "deprRptrMonitorGroupTable": deprRptrMonitorGroupTable,
       "deprRptrMonitorGroupEntry": deprRptrMonitorGroupEntry,
       "deprRptrMonitorGroupIndex": deprRptrMonitorGroupIndex,
       "deprRptrMonitorGroupTotalFrames": deprRptrMonitorGroupTotalFrames,
       "deprRptrMonitorGroupTotalOctets": deprRptrMonitorGroupTotalOctets,
       "deprRptrMonitorGroupTotalErrors": deprRptrMonitorGroupTotalErrors,
       "deprRptrMonitorPortInfo": deprRptrMonitorPortInfo,
       "deprRptrMonitorPortTable": deprRptrMonitorPortTable,
       "deprRptrMonitorPortEntry": deprRptrMonitorPortEntry,
       "deprRptrMonitorPortGroupIndex": deprRptrMonitorPortGroupIndex,
       "deprRptrMonitorPortIndex": deprRptrMonitorPortIndex,
       "deprRptrMonitorPortReadableFrames": deprRptrMonitorPortReadableFrames,
       "deprRptrMonitorPortReadableOctets": deprRptrMonitorPortReadableOctets,
       "deprRptrMonitorPortFCSErrors": deprRptrMonitorPortFCSErrors,
       "deprRptrMonitorPortAlignmentErrors": deprRptrMonitorPortAlignmentErrors,
       "deprRptrMonitorPortFrameTooLongs": deprRptrMonitorPortFrameTooLongs,
       "deprRptrMonitorPortShortEvents": deprRptrMonitorPortShortEvents,
       "deprRptrMonitorPortRunts": deprRptrMonitorPortRunts,
       "deprRptrMonitorPortCollisions": deprRptrMonitorPortCollisions,
       "deprRptrMonitorPortLateEvents": deprRptrMonitorPortLateEvents,
       "deprRptrMonitorPortVeryLongEvents": deprRptrMonitorPortVeryLongEvents,
       "deprRptrMonitorPortDataRateMismatches": deprRptrMonitorPortDataRateMismatches,
       "deprRptrMonitorPortAutoPartitions": deprRptrMonitorPortAutoPartitions,
       "deprRptrMonitorPortTotalErrors": deprRptrMonitorPortTotalErrors,
       "deprRptrAddrTrackPackage": deprRptrAddrTrackPackage,
       "deprRptrAddrTrackRptrInfo": deprRptrAddrTrackRptrInfo,
       "deprRptrAddrTrackGroupInfo": deprRptrAddrTrackGroupInfo,
       "deprRptrAddrTrackPortInfo": deprRptrAddrTrackPortInfo,
       "deprRptrAddrTrackTable": deprRptrAddrTrackTable,
       "deprRptrAddrTrackEntry": deprRptrAddrTrackEntry,
       "deprRptrAddrTrackGroupIndex": deprRptrAddrTrackGroupIndex,
       "deprRptrAddrTrackPortIndex": deprRptrAddrTrackPortIndex,
       "deprRptrAddrTrackLastSourceAddress": deprRptrAddrTrackLastSourceAddress,
       "deprRptrAddrTrackSourceAddrChanges": deprRptrAddrTrackSourceAddrChanges,
       "deprSnmpDot3RpMauMgt": deprSnmpDot3RpMauMgt,
       "deprRpMauBasicGroup": deprRpMauBasicGroup,
       "deprRpMauTable": deprRpMauTable,
       "deprRpMauEntry": deprRpMauEntry,
       "deprRpMauGroupIndex": deprRpMauGroupIndex,
       "deprRpMauPortIndex": deprRpMauPortIndex,
       "deprRpMauIndex": deprRpMauIndex,
       "deprRpMauType": deprRpMauType,
       "deprRpMauAdminState": deprRpMauAdminState,
       "deprRpMauMediaAvailable": deprRpMauMediaAvailable,
       "deprRpMauLostMedias": deprRpMauLostMedias,
       "deprRpMauJabberState": deprRpMauJabberState,
       "deprRpMauJabbers": deprRpMauJabbers,
       "linkbuilderMonitorMacPackage": linkbuilderMonitorMacPackage,
       "vmMacMonitorTable": vmMacMonitorTable,
       "vmMacMonitorEntry": vmMacMonitorEntry,
       "vmMacMonitorIndex": vmMacMonitorIndex,
       "vmMacMonitorMissErrors": vmMacMonitorMissErrors,
       "vmMacMonitorBabbleErrors": vmMacMonitorBabbleErrors,
       "vmMacMonitorMemoryErrors": vmMacMonitorMemoryErrors,
       "vmMacMonitorFCSErrors": vmMacMonitorFCSErrors,
       "vmMacMonitorOverflowErrors": vmMacMonitorOverflowErrors,
       "vmMacMonitorFramingErrors": vmMacMonitorFramingErrors,
       "vmMacMonitorRetryErrors": vmMacMonitorRetryErrors,
       "vmMacMonitorLateEvents": vmMacMonitorLateEvents,
       "vmMacMonitorLCarErrors": vmMacMonitorLCarErrors,
       "vmMacMonitorUnderflowErrors": vmMacMonitorUnderflowErrors,
       "linkBuilderECS-mib": linkBuilderECS_mib,
       "generic": generic,
       "genExperimental": genExperimental,
       "testData": testData,
       "ifExtensions": ifExtensions,
       "setup": setup,
       "setupGeneral": setupGeneral,
       "heartbeatInterval": heartbeatInterval,
       "setupIp": setupIp,
       "setIpIfTable": setIpIfTable,
       "setIpIfEntry": setIpIfEntry,
       "setIpIfIndex": setIpIfIndex,
       "setIpIfAddr": setIpIfAddr,
       "setIpIfMask": setIpIfMask,
       "setIpIfRouter": setIpIfRouter,
       "setupStart": setupStart,
       "startPROMSwVerNo": startPROMSwVerNo,
       "startRestartCount": startRestartCount,
       "startLastRestartType": startLastRestartType,
       "startResetAction": startResetAction,
       "startLastSystemError": startLastSystemError,
       "startRestartAction": startRestartAction,
       "sysLoader": sysLoader,
       "loadableDeviceTable": loadableDeviceTable,
       "loadableDeviceEntry": loadableDeviceEntry,
       "slDeviceType": slDeviceType,
       "slDeviceInstance": slDeviceInstance,
       "slLoadStatus": slLoadStatus,
       "slSoftwareVersion": slSoftwareVersion,
       "slHardwareVersion": slHardwareVersion,
       "slFilename": slFilename,
       "slServerIpAddress": slServerIpAddress,
       "slLoad": slLoad,
       "slServerAddress": slServerAddress,
       "slServerProtocol": slServerProtocol,
       "security": security,
       "securityEnableTable": securityEnableTable,
       "securityEnableTableEntry": securityEnableTableEntry,
       "securityLevel": securityLevel,
       "securityCommunityEnable": securityCommunityEnable,
       "securitySecureEnable": securitySecureEnable,
       "securityTermEnable": securityTermEnable,
       "securityTelnetEnable": securityTelnetEnable,
       "securityFrontPanelEnable": securityFrontPanelEnable,
       "securityUserTable": securityUserTable,
       "securityUserTableEntry": securityUserTableEntry,
       "securityUserStatus": securityUserStatus,
       "securityUserName": securityUserName,
       "securityUserLevel": securityUserLevel,
       "securityUserPassword": securityUserPassword,
       "securityUserCommunity": securityUserCommunity,
       "securityUserLocParty": securityUserLocParty,
       "securityUserMgrParty": securityUserMgrParty,
       "securityAuditLogTable": securityAuditLogTable,
       "securityAuditLogEntry": securityAuditLogEntry,
       "securityAuditIndex": securityAuditIndex,
       "securityAuditTime": securityAuditTime,
       "securityAuditUser": securityAuditUser,
       "securityAuditObject": securityAuditObject,
       "securityAuditValue": securityAuditValue,
       "securityAuditResult": securityAuditResult,
       "gauges": gauges,
       "gaugeTable": gaugeTable,
       "gaugeTableEntry": gaugeTableEntry,
       "gaugeIndex": gaugeIndex,
       "gaugeItemId": gaugeItemId,
       "gaugeItemType": gaugeItemType,
       "gaugeSamplesPerAverage": gaugeSamplesPerAverage,
       "gaugeSamplePeriod": gaugeSamplePeriod,
       "gaugeValue": gaugeValue,
       "gaugePeakValue": gaugePeakValue,
       "gaugeThresholdLevel": gaugeThresholdLevel,
       "gaugeRecoveryLevel": gaugeRecoveryLevel,
       "gaugeThresholdAction": gaugeThresholdAction,
       "gaugeRecoveryAction": gaugeRecoveryAction,
       "gaugeState": gaugeState,
       "gaugeOwner": gaugeOwner,
       "gaugeTableSize": gaugeTableSize,
       "gaugeThresholdLevelScaler": gaugeThresholdLevelScaler,
       "gaugeRecoveryLevelScaler": gaugeRecoveryLevelScaler,
       "gaugeTableUpdate": gaugeTableUpdate,
       "gaugeConfigureObjId": gaugeConfigureObjId,
       "gaugeConfigureColumn": gaugeConfigureColumn,
       "gaugeConfigureValue": gaugeConfigureValue,
       "gaugeNextFreeIndex": gaugeNextFreeIndex,
       "asciiAgent": asciiAgent,
       "ascTimeAttemptedLogin": ascTimeAttemptedLogin,
       "ascUserNameForLastAttemptedLogin": ascUserNameForLastAttemptedLogin,
       "ascLoginStatus": ascLoginStatus,
       "ascLocalManagementBanner": ascLocalManagementBanner,
       "serialIf": serialIf,
       "siSlipPort": siSlipPort,
       "configV24Table": configV24Table,
       "configV24Entry": configV24Entry,
       "configV24PortID": configV24PortID,
       "configV24ConnType": configV24ConnType,
       "configV24AutoConfig": configV24AutoConfig,
       "configV24Speed": configV24Speed,
       "configV24CharSize": configV24CharSize,
       "configV24StopBits": configV24StopBits,
       "configV24Parity": configV24Parity,
       "configV24DSRControl": configV24DSRControl,
       "configV24DCDControl": configV24DCDControl,
       "configV24FlowControl": configV24FlowControl,
       "configV24Update": configV24Update,
       "repeaterMgmt": repeaterMgmt,
       "pddrmBasicPackage": pddrmBasicPackage,
       "pddrmBasRepeaterPackage": pddrmBasRepeaterPackage,
       "pddrmBasGroupPackage": pddrmBasGroupPackage,
       "pddrmBasPortPackage": pddrmBasPortPackage,
       "pddrmMonitorPackage": pddrmMonitorPackage,
       "pddrmMonRepeaterPackage": pddrmMonRepeaterPackage,
       "pddrmMonRepeaterReadableFrames": pddrmMonRepeaterReadableFrames,
       "pddrmMonRepeaterReadableOctets": pddrmMonRepeaterReadableOctets,
       "pddrmMonRepeaterFCSErrors": pddrmMonRepeaterFCSErrors,
       "pddrmMonRepeaterAlignmentErrors": pddrmMonRepeaterAlignmentErrors,
       "pddrmMonRepeaterFrameTooLongs": pddrmMonRepeaterFrameTooLongs,
       "pddrmMonRepeaterShortEvents": pddrmMonRepeaterShortEvents,
       "pddrmMonRepeaterRunts": pddrmMonRepeaterRunts,
       "pddrmMonRepeaterCollisions": pddrmMonRepeaterCollisions,
       "pddrmMonRepeaterLateEvents": pddrmMonRepeaterLateEvents,
       "pddrmMonRepeaterVeryLongEvents": pddrmMonRepeaterVeryLongEvents,
       "pddrmMonRepeaterDataRateMismatches": pddrmMonRepeaterDataRateMismatches,
       "pddrmMonRepeaterAutoPartitions": pddrmMonRepeaterAutoPartitions,
       "pddrmMonRepeaterUniCastFrames": pddrmMonRepeaterUniCastFrames,
       "pddrmMonRepeaterMultiCastFrames": pddrmMonRepeaterMultiCastFrames,
       "pddrmMonRepeaterBroadCastFrames": pddrmMonRepeaterBroadCastFrames,
       "pddrmMonRepeaterClearCounters": pddrmMonRepeaterClearCounters,
       "pddrmMonRepeaterMediaAvailableTraps": pddrmMonRepeaterMediaAvailableTraps,
       "pddrmMonRepeaterAutoPartitionTraps": pddrmMonRepeaterAutoPartitionTraps,
       "pddrmMonRepeaterTotalErrors": pddrmMonRepeaterTotalErrors,
       "pddrmMonGroupPackage": pddrmMonGroupPackage,
       "pddrmMonitorGroupTable": pddrmMonitorGroupTable,
       "pddrmMonitorGroupEntry": pddrmMonitorGroupEntry,
       "pddrmMonGroupIndex": pddrmMonGroupIndex,
       "pddrmMonGroupFCSErrors": pddrmMonGroupFCSErrors,
       "pddrmMonGroupAlignmentErrors": pddrmMonGroupAlignmentErrors,
       "pddrmMonGroupFrameTooLongs": pddrmMonGroupFrameTooLongs,
       "pddrmMonGroupShortEvents": pddrmMonGroupShortEvents,
       "pddrmMonGroupRunts": pddrmMonGroupRunts,
       "pddrmMonGroupCollisions": pddrmMonGroupCollisions,
       "pddrmMonGroupLateEvents": pddrmMonGroupLateEvents,
       "pddrmMonGroupVeryLongEvents": pddrmMonGroupVeryLongEvents,
       "pddrmMonGroupDataRateMismatches": pddrmMonGroupDataRateMismatches,
       "pddrmMonGroupAutoPartitions": pddrmMonGroupAutoPartitions,
       "pddrmMonGroupUniCastFrames": pddrmMonGroupUniCastFrames,
       "pddrmMonGroupMultiCastFrames": pddrmMonGroupMultiCastFrames,
       "pddrmMonGroupBroadCastFrames": pddrmMonGroupBroadCastFrames,
       "pddrmMonGroupClearCounters": pddrmMonGroupClearCounters,
       "pddrmMonPortPackage": pddrmMonPortPackage,
       "pddrmMonitorPortTable": pddrmMonitorPortTable,
       "pddrmMonitorPortEntry": pddrmMonitorPortEntry,
       "pddrmMonPortGroupIndex": pddrmMonPortGroupIndex,
       "pddrmMonPortIndex": pddrmMonPortIndex,
       "pddrmMonPortUniCastFrames": pddrmMonPortUniCastFrames,
       "pddrmMonPortMultiCastFrames": pddrmMonPortMultiCastFrames,
       "pddrmMonPortBroadCastFrames": pddrmMonPortBroadCastFrames,
       "pddrmMonPortClearCounters": pddrmMonPortClearCounters,
       "pddrmMonPortESTFilter": pddrmMonPortESTFilter,
       "pddrmMonPortMediaAvailableTraps": pddrmMonPortMediaAvailableTraps,
       "pddrmMonPortAutoPartitionTraps": pddrmMonPortAutoPartitionTraps,
       "pddrmMonRepeaterDummyPackage": pddrmMonRepeaterDummyPackage,
       "pddrmMonGroupDummyPackage": pddrmMonGroupDummyPackage,
       "pddrmMonPortDummyPackage": pddrmMonPortDummyPackage,
       "endStation": endStation,
       "esDatabaseState": esDatabaseState,
       "esDatabaseFlush": esDatabaseFlush,
       "esTable": esTable,
       "esTableEntry": esTableEntry,
       "esAddrType": esAddrType,
       "esAddress": esAddress,
       "esSlotNumber": esSlotNumber,
       "esPortNumber": esPortNumber,
       "esModTable": esModTable,
       "esModTableEntry": esModTableEntry,
       "esModAddrType": esModAddrType,
       "esModAddress": esModAddress,
       "esModSlotNumber": esModSlotNumber,
       "esModPortNumber": esModPortNumber,
       "esPortAccessTable": esPortAccessTable,
       "esPortAccessEntry": esPortAccessEntry,
       "ecPortCardNo": ecPortCardNo,
       "ecPortPortNo": ecPortPortNo,
       "ecPortIndex": ecPortIndex,
       "ecPortAddrType": ecPortAddrType,
       "ecPortAddress": ecPortAddress,
       "localSnmp": localSnmp,
       "trapTable": trapTable,
       "trapEntry": trapEntry,
       "trapStatus": trapStatus,
       "trapDestination": trapDestination,
       "trapCommunity": trapCommunity,
       "trapSubject": trapSubject,
       "trapCategory": trapCategory,
       "trapThrottle": trapThrottle,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapIndex": snmpTrapIndex,
       "snmpTrapDestination": snmpTrapDestination,
       "snmpTrapProtocol": snmpTrapProtocol,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapCategory": snmpTrapCategory,
       "snmpTrapThrottle": snmpTrapThrottle,
       "snmpTrapRowStatus": snmpTrapRowStatus,
       "snmpTrapNextFreeIndex": snmpTrapNextFreeIndex,
       "manager": manager,
       "unusedGeneric12": unusedGeneric12,
       "chassis": chassis,
       "mrmResilience": mrmResilience,
       "resTable": resTable,
       "resTableEntry": resTableEntry,
       "resRepeater": resRepeater,
       "resMainSlot": resMainSlot,
       "resMainPort": resMainPort,
       "resMainState": resMainState,
       "resStandbySlot": resStandbySlot,
       "resStandbyPort": resStandbyPort,
       "resStandbyState": resStandbyState,
       "resPairState": resPairState,
       "resPairModificationStatus": resPairModificationStatus,
       "resPairAction": resPairAction,
       "resPairEnable": resPairEnable,
       "resStandbyMapTable": resStandbyMapTable,
       "resStandbyMapTableEntry": resStandbyMapTableEntry,
       "resSbRepeater": resSbRepeater,
       "resSbSlot": resSbSlot,
       "resSbPort": resSbPort,
       "resSbType": resSbType,
       "resSbMainSlot": resSbMainSlot,
       "resSbMainPort": resSbMainPort,
       "resFlushTable": resFlushTable,
       "tokenRing": tokenRing,
       "multiRepeater": multiRepeater,
       "mrmBasicPackage": mrmBasicPackage,
       "mrmBasCardPackage": mrmBasCardPackage,
       "mrmCardTable": mrmCardTable,
       "mrmCardEntry": mrmCardEntry,
       "mrmCardServiceId": mrmCardServiceId,
       "mrmCardIndex": mrmCardIndex,
       "mrmCardPortCapacity": mrmCardPortCapacity,
       "mrmCardTest": mrmCardTest,
       "mrmCardDOBPorts": mrmCardDOBPorts,
       "mrmCardMDIenable": mrmCardMDIenable,
       "mrmBasPortPackage": mrmBasPortPackage,
       "mrmPortTable": mrmPortTable,
       "mrmPortEntry": mrmPortEntry,
       "mrmPortServiceId": mrmPortServiceId,
       "mrmPortCardIndex": mrmPortCardIndex,
       "mrmPortIndex": mrmPortIndex,
       "mrmPortInterfaceType": mrmPortInterfaceType,
       "mrmPortConnectorType": mrmPortConnectorType,
       "mrmPortAdminStatus": mrmPortAdminStatus,
       "mrmPortAutoPartitionState": mrmPortAutoPartitionState,
       "mrmPortLinkState": mrmPortLinkState,
       "mrmPortBootState": mrmPortBootState,
       "mrmPortESTFilter": mrmPortESTFilter,
       "mrmPortPartitionEvent": mrmPortPartitionEvent,
       "mrmPortLinkStateEvent": mrmPortLinkStateEvent,
       "mrmPortSecurityAvailable": mrmPortSecurityAvailable,
       "mrmPortLinkPulse": mrmPortLinkPulse,
       "mrmPortModule": mrmPortModule,
       "mrmPortDUDAction": mrmPortDUDAction,
       "mrmPortFunction": mrmPortFunction,
       "mrmMonitorPackage": mrmMonitorPackage,
       "mrmMonRepeaterPackage": mrmMonRepeaterPackage,
       "mrmMonitorRepTable": mrmMonitorRepTable,
       "mrmMonitorRepEntry": mrmMonitorRepEntry,
       "mrmMonRepServiceId": mrmMonRepServiceId,
       "mrmMonRepReadableFrames": mrmMonRepReadableFrames,
       "mrmMonRepUnicastFrames": mrmMonRepUnicastFrames,
       "mrmMonRepMulticastFrames": mrmMonRepMulticastFrames,
       "mrmMonRepBroadcastFrames": mrmMonRepBroadcastFrames,
       "mrmMonRepReadableOctets": mrmMonRepReadableOctets,
       "mrmMonRepUnicastOctets": mrmMonRepUnicastOctets,
       "mrmMonRepMulticastOctets": mrmMonRepMulticastOctets,
       "mrmMonRepBroadcastOctets": mrmMonRepBroadcastOctets,
       "mrmMonRepFCSErrors": mrmMonRepFCSErrors,
       "mrmMonRepAlignmentErrors": mrmMonRepAlignmentErrors,
       "mrmMonRepFrameTooLongs": mrmMonRepFrameTooLongs,
       "mrmMonRepShortEvents": mrmMonRepShortEvents,
       "mrmMonRepRunts": mrmMonRepRunts,
       "mrmMonRepTxCollisions": mrmMonRepTxCollisions,
       "mrmMonRepLateEvents": mrmMonRepLateEvents,
       "mrmMonRepVeryLongEvents": mrmMonRepVeryLongEvents,
       "mrmMonRepDataRateMismatches": mrmMonRepDataRateMismatches,
       "mrmMonRepAutoPartitions": mrmMonRepAutoPartitions,
       "mrmMonRepTotalErrors": mrmMonRepTotalErrors,
       "mrmMonRepBound0": mrmMonRepBound0,
       "mrmMonRepBound1": mrmMonRepBound1,
       "mrmMonRepBound2": mrmMonRepBound2,
       "mrmMonRepBound3": mrmMonRepBound3,
       "mrmMonRepBound4": mrmMonRepBound4,
       "mrmMonRepBound5": mrmMonRepBound5,
       "mrmMonRepAction": mrmMonRepAction,
       "mrmMonRepBandwidthUsed": mrmMonRepBandwidthUsed,
       "mrmMonRepErrorsPer10000Packets": mrmMonRepErrorsPer10000Packets,
       "mrmMonCardPackage": mrmMonCardPackage,
       "mrmMonitorCardTable": mrmMonitorCardTable,
       "mrmMonitorCardEntry": mrmMonitorCardEntry,
       "mrmMonCardServiceId": mrmMonCardServiceId,
       "mrmMonCardIndex": mrmMonCardIndex,
       "mrmMonCardReadableFrames": mrmMonCardReadableFrames,
       "mrmMonCardUnicastFrames": mrmMonCardUnicastFrames,
       "mrmMonCardMulticastFrames": mrmMonCardMulticastFrames,
       "mrmMonCardBroadcastFrames": mrmMonCardBroadcastFrames,
       "mrmMonCardReadableOctets": mrmMonCardReadableOctets,
       "mrmMonCardUnicastOctets": mrmMonCardUnicastOctets,
       "mrmMonCardMulticastOctets": mrmMonCardMulticastOctets,
       "mrmMonCardBroadcastOctets": mrmMonCardBroadcastOctets,
       "mrmMonCardFCSErrors": mrmMonCardFCSErrors,
       "mrmMonCardAlignmentErrors": mrmMonCardAlignmentErrors,
       "mrmMonCardFrameTooLongs": mrmMonCardFrameTooLongs,
       "mrmMonCardShortEvents": mrmMonCardShortEvents,
       "mrmMonCardRunts": mrmMonCardRunts,
       "mrmMonCardLateEvents": mrmMonCardLateEvents,
       "mrmMonCardVeryLongEvents": mrmMonCardVeryLongEvents,
       "mrmMonCardDataRateMismatches": mrmMonCardDataRateMismatches,
       "mrmMonCardAutoPartitions": mrmMonCardAutoPartitions,
       "mrmMonCardTotalErrors": mrmMonCardTotalErrors,
       "mrmMonCardBound0": mrmMonCardBound0,
       "mrmMonCardBound1": mrmMonCardBound1,
       "mrmMonCardBound2": mrmMonCardBound2,
       "mrmMonCardBound3": mrmMonCardBound3,
       "mrmMonCardBound4": mrmMonCardBound4,
       "mrmMonCardBound5": mrmMonCardBound5,
       "mrmMonCardClearCounters": mrmMonCardClearCounters,
       "mrmMonCardBandwidthUsed": mrmMonCardBandwidthUsed,
       "mrmMonCardErrorsPer10000Packets": mrmMonCardErrorsPer10000Packets,
       "mrmMonPortPackage": mrmMonPortPackage,
       "mrmMonitorPortTable": mrmMonitorPortTable,
       "mrmMonitorPortEntry": mrmMonitorPortEntry,
       "mrmMonPortServiceId": mrmMonPortServiceId,
       "mrmMonPortCardIndex": mrmMonPortCardIndex,
       "mrmMonPortIndex": mrmMonPortIndex,
       "mrmMonPortReadableFrames": mrmMonPortReadableFrames,
       "mrmMonPortUnicastFrames": mrmMonPortUnicastFrames,
       "mrmMonPortMulticastFrames": mrmMonPortMulticastFrames,
       "mrmMonPortBroadcastFrames": mrmMonPortBroadcastFrames,
       "mrmMonPortReadableOctets": mrmMonPortReadableOctets,
       "mrmMonPortUnicastOctets": mrmMonPortUnicastOctets,
       "mrmMonPortMulticastOctets": mrmMonPortMulticastOctets,
       "mrmMonPortBroadcastOctets": mrmMonPortBroadcastOctets,
       "mrmMonPortFCSErrors": mrmMonPortFCSErrors,
       "mrmMonPortAlignmentErrors": mrmMonPortAlignmentErrors,
       "mrmMonPortFrameTooLongs": mrmMonPortFrameTooLongs,
       "mrmMonPortShortEvents": mrmMonPortShortEvents,
       "mrmMonPortRunts": mrmMonPortRunts,
       "mrmMonPortCollisions": mrmMonPortCollisions,
       "mrmMonPortLateEvents": mrmMonPortLateEvents,
       "mrmMonPortVeryLongEvents": mrmMonPortVeryLongEvents,
       "mrmMonPortDataRateMismatches": mrmMonPortDataRateMismatches,
       "mrmMonPortAutoPartitions": mrmMonPortAutoPartitions,
       "mrmMonPortTotalErrors": mrmMonPortTotalErrors,
       "mrmMonPortBound0": mrmMonPortBound0,
       "mrmMonPortBound1": mrmMonPortBound1,
       "mrmMonPortBound2": mrmMonPortBound2,
       "mrmMonPortBound3": mrmMonPortBound3,
       "mrmMonPortBound4": mrmMonPortBound4,
       "mrmMonPortBound5": mrmMonPortBound5,
       "mrmMonPortBandwidthUsed": mrmMonPortBandwidthUsed,
       "mrmMonPortErrorsPer10000Packets": mrmMonPortErrorsPer10000Packets,
       "mrmMonPortClearCounters": mrmMonPortClearCounters,
       "mrmMonPortLastAddress": mrmMonPortLastAddress,
       "mrmMonPortAddressChanges": mrmMonPortAddressChanges,
       "mrmMonDummyPackage": mrmMonDummyPackage,
       "trafficLevel": trafficLevel,
       "errorFrames": errorFrames,
       "mrmMonRepeaterSmartPackage": mrmMonRepeaterSmartPackage,
       "mrmMonRepeaterTrafficLevel": mrmMonRepeaterTrafficLevel,
       "mrmMonRepeaterErrorFrames": mrmMonRepeaterErrorFrames,
       "mrmMonCardSmartPackage": mrmMonCardSmartPackage,
       "mrmMonCardTrafficLevel": mrmMonCardTrafficLevel,
       "mrmMonCardErrorFrames": mrmMonCardErrorFrames,
       "mrmMonPortSmartPackage": mrmMonPortSmartPackage,
       "mrmMonPortTrafficLevel": mrmMonPortTrafficLevel,
       "mrmMonPortErrorFrames": mrmMonPortErrorFrames,
       "bridgeMgmt": bridgeMgmt,
       "fault": fault,
       "faultModifiedFlag": faultModifiedFlag,
       "faultTable": faultTable,
       "faultEntry": faultEntry,
       "faultIndex": faultIndex,
       "faultErrorNumber": faultErrorNumber,
       "faultTimeStamp": faultTimeStamp,
       "faultRestartCount": faultRestartCount,
       "poll": poll,
       "pollTable": pollTable,
       "pollTableEntry": pollTableEntry,
       "pollIndex": pollIndex,
       "pollAddress": pollAddress,
       "pollProtocol": pollProtocol,
       "pollRate": pollRate,
       "pollTargetType": pollTargetType,
       "pollLastPollSent": pollLastPollSent,
       "pollRoundTripTime": pollRoundTripTime,
       "pollInformation": pollInformation,
       "pollAlarmIndex": pollAlarmIndex,
       "pollOwner": pollOwner,
       "pollRowStatus": pollRowStatus,
       "pollNextFreeIndex": pollNextFreeIndex,
       "powerSupply": powerSupply,
       "powerStackPackage": powerStackPackage,
       "powerStackBackupPresent": powerStackBackupPresent,
       "powerStackBackupData": powerStackBackupData,
       "powerStackTable": powerStackTable,
       "powerStackTableEntry": powerStackTableEntry,
       "powerStackTableIndex": powerStackTableIndex,
       "powerStackRBSPresent": powerStackRBSPresent,
       "powerStackRBSStatus": powerStackRBSStatus,
       "netBuilder-mib": netBuilder_mib,
       "lBridgeECS-mib": lBridgeECS_mib,
       "deskMan-mib": deskMan_mib,
       "linkBuilderMSH-mib": linkBuilderMSH_mib,
       "linkBuilderFMS-mib": linkBuilderFMS_mib,
       "linkBuilderFDDI-wghub-mib": linkBuilderFDDI_wghub_mib,
       "linkSwitch-mib": linkSwitch_mib}
)
