# SNMP MIB module (DELL-NETWORKING-TRAP-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-TRAP-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:00 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "TextualConvention")


# MODULE-IDENTITY

dellNetTrapEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6)
)
dellNetTrapEventMib.setRevisions(
        ("2012-02-21 00:00",
         "2005-10-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetTrapEventObjects_ObjectIdentity = ObjectIdentity
dellNetTrapEventObjects = _DellNetTrapEventObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1)
)
_DellNetHistoryTrapEvent_ObjectIdentity = ObjectIdentity
dellNetHistoryTrapEvent = _DellNetHistoryTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1)
)
_DellNetChassisBootupTime_Type = DateAndTime
_DellNetChassisBootupTime_Object = MibScalar
dellNetChassisBootupTime = _DellNetChassisBootupTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 1),
    _DellNetChassisBootupTime_Type()
)
dellNetChassisBootupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisBootupTime.setStatus("current")


class _DellNetLastTrapEventSeqId_Type(Integer32):
    """Custom type dellNetLastTrapEventSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DellNetLastTrapEventSeqId_Type.__name__ = "Integer32"
_DellNetLastTrapEventSeqId_Object = MibScalar
dellNetLastTrapEventSeqId = _DellNetLastTrapEventSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 2),
    _DellNetLastTrapEventSeqId_Type()
)
dellNetLastTrapEventSeqId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetLastTrapEventSeqId.setStatus("current")
_DellNetMaxHistoryTableSize_Type = Integer32
_DellNetMaxHistoryTableSize_Object = MibScalar
dellNetMaxHistoryTableSize = _DellNetMaxHistoryTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 3),
    _DellNetMaxHistoryTableSize_Type()
)
dellNetMaxHistoryTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetMaxHistoryTableSize.setStatus("current")
_DellNetHistoryTrapEventTable_Object = MibTable
dellNetHistoryTrapEventTable = _DellNetHistoryTrapEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    dellNetHistoryTrapEventTable.setStatus("current")
_DellNetHistoryTrapEventEntry_Object = MibTableRow
dellNetHistoryTrapEventEntry = _DellNetHistoryTrapEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1)
)
dellNetHistoryTrapEventEntry.setIndexNames(
    (0, "DELL-NETWORKING-TRAP-EVENT-MIB", "historyTrapEventSeqId"),
)
if mibBuilder.loadTexts:
    dellNetHistoryTrapEventEntry.setStatus("current")


class _HistoryTrapEventSeqId_Type(Integer32):
    """Custom type historyTrapEventSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HistoryTrapEventSeqId_Type.__name__ = "Integer32"
_HistoryTrapEventSeqId_Object = MibTableColumn
historyTrapEventSeqId = _HistoryTrapEventSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 1),
    _HistoryTrapEventSeqId_Type()
)
historyTrapEventSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyTrapEventSeqId.setStatus("current")
_HistoryTrapEventSeverity_Type = Integer32
_HistoryTrapEventSeverity_Object = MibTableColumn
historyTrapEventSeverity = _HistoryTrapEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 2),
    _HistoryTrapEventSeverity_Type()
)
historyTrapEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventSeverity.setStatus("current")
_HistoryTrapEventType_Type = Integer32
_HistoryTrapEventType_Object = MibTableColumn
historyTrapEventType = _HistoryTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 3),
    _HistoryTrapEventType_Type()
)
historyTrapEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventType.setStatus("current")
_HistoryTrapEventMsg_Type = DisplayString
_HistoryTrapEventMsg_Object = MibTableColumn
historyTrapEventMsg = _HistoryTrapEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 4),
    _HistoryTrapEventMsg_Type()
)
historyTrapEventMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventMsg.setStatus("current")
_HistoryTrapEventOid_Type = RowPointer
_HistoryTrapEventOid_Object = MibTableColumn
historyTrapEventOid = _HistoryTrapEventOid_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 5),
    _HistoryTrapEventOid_Type()
)
historyTrapEventOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventOid.setStatus("current")
_HistoryTrapEventSlot_Type = Integer32
_HistoryTrapEventSlot_Object = MibTableColumn
historyTrapEventSlot = _HistoryTrapEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 6),
    _HistoryTrapEventSlot_Type()
)
historyTrapEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventSlot.setStatus("current")
_HistoryTrapEventTimeStamp_Type = TimeTicks
_HistoryTrapEventTimeStamp_Object = MibTableColumn
historyTrapEventTimeStamp = _HistoryTrapEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 7),
    _HistoryTrapEventTimeStamp_Type()
)
historyTrapEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventTimeStamp.setStatus("current")
_HistoryTrapEventPort_Type = Integer32
_HistoryTrapEventPort_Object = MibTableColumn
historyTrapEventPort = _HistoryTrapEventPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 1, 4, 1, 8),
    _HistoryTrapEventPort_Type()
)
historyTrapEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    historyTrapEventPort.setStatus("current")
_DellNetActiveTrapEvent_ObjectIdentity = ObjectIdentity
dellNetActiveTrapEvent = _DellNetActiveTrapEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2)
)
_DellNetActiveTrapEventTable_Object = MibTable
dellNetActiveTrapEventTable = _DellNetActiveTrapEventTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dellNetActiveTrapEventTable.setStatus("current")
_DellNetActiveTrapEventEntry_Object = MibTableRow
dellNetActiveTrapEventEntry = _DellNetActiveTrapEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1)
)
dellNetActiveTrapEventEntry.setIndexNames(
    (0, "DELL-NETWORKING-TRAP-EVENT-MIB", "activeTrapEventSeqId"),
)
if mibBuilder.loadTexts:
    dellNetActiveTrapEventEntry.setStatus("current")


class _ActiveTrapEventSeqId_Type(Integer32):
    """Custom type activeTrapEventSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ActiveTrapEventSeqId_Type.__name__ = "Integer32"
_ActiveTrapEventSeqId_Object = MibTableColumn
activeTrapEventSeqId = _ActiveTrapEventSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 1),
    _ActiveTrapEventSeqId_Type()
)
activeTrapEventSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeTrapEventSeqId.setStatus("current")
_ActiveTrapEventSeverity_Type = Integer32
_ActiveTrapEventSeverity_Object = MibTableColumn
activeTrapEventSeverity = _ActiveTrapEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 2),
    _ActiveTrapEventSeverity_Type()
)
activeTrapEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventSeverity.setStatus("current")
_ActiveTrapEventType_Type = Integer32
_ActiveTrapEventType_Object = MibTableColumn
activeTrapEventType = _ActiveTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 3),
    _ActiveTrapEventType_Type()
)
activeTrapEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventType.setStatus("current")
_ActiveTrapEventMsg_Type = DisplayString
_ActiveTrapEventMsg_Object = MibTableColumn
activeTrapEventMsg = _ActiveTrapEventMsg_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 4),
    _ActiveTrapEventMsg_Type()
)
activeTrapEventMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventMsg.setStatus("current")
_ActiveTrapEventOid_Type = RowPointer
_ActiveTrapEventOid_Object = MibTableColumn
activeTrapEventOid = _ActiveTrapEventOid_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 5),
    _ActiveTrapEventOid_Type()
)
activeTrapEventOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventOid.setStatus("current")
_ActiveTrapEventSlot_Type = Integer32
_ActiveTrapEventSlot_Object = MibTableColumn
activeTrapEventSlot = _ActiveTrapEventSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 6),
    _ActiveTrapEventSlot_Type()
)
activeTrapEventSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventSlot.setStatus("current")
_ActiveTrapEventTimeStamp_Type = TimeTicks
_ActiveTrapEventTimeStamp_Object = MibTableColumn
activeTrapEventTimeStamp = _ActiveTrapEventTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 7),
    _ActiveTrapEventTimeStamp_Type()
)
activeTrapEventTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventTimeStamp.setStatus("current")
_ActiveTrapEventPort_Type = Integer32
_ActiveTrapEventPort_Object = MibTableColumn
activeTrapEventPort = _ActiveTrapEventPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 2, 1, 1, 8),
    _ActiveTrapEventPort_Type()
)
activeTrapEventPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeTrapEventPort.setStatus("current")
_DellNetTrapVarbindEvent_ObjectIdentity = ObjectIdentity
dellNetTrapVarbindEvent = _DellNetTrapVarbindEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3)
)
_DellNetTrapEventVarbindTable_Object = MibTable
dellNetTrapEventVarbindTable = _DellNetTrapEventVarbindTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dellNetTrapEventVarbindTable.setStatus("current")
_DellNetTrapEventVarbindEntry_Object = MibTableRow
dellNetTrapEventVarbindEntry = _DellNetTrapEventVarbindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1)
)
dellNetTrapEventVarbindEntry.setIndexNames(
    (0, "DELL-NETWORKING-TRAP-EVENT-MIB", "trapEventVarbindSeqId"),
    (0, "DELL-NETWORKING-TRAP-EVENT-MIB", "trapEventVarbindId"),
)
if mibBuilder.loadTexts:
    dellNetTrapEventVarbindEntry.setStatus("current")


class _TrapEventVarbindSeqId_Type(Integer32):
    """Custom type trapEventVarbindSeqId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TrapEventVarbindSeqId_Type.__name__ = "Integer32"
_TrapEventVarbindSeqId_Object = MibTableColumn
trapEventVarbindSeqId = _TrapEventVarbindSeqId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 1),
    _TrapEventVarbindSeqId_Type()
)
trapEventVarbindSeqId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventVarbindSeqId.setStatus("current")


class _TrapEventVarbindId_Type(Integer32):
    """Custom type trapEventVarbindId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_TrapEventVarbindId_Type.__name__ = "Integer32"
_TrapEventVarbindId_Object = MibTableColumn
trapEventVarbindId = _TrapEventVarbindId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 2),
    _TrapEventVarbindId_Type()
)
trapEventVarbindId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventVarbindId.setStatus("current")
_TrapEventVarbindOid_Type = ObjectIdentifier
_TrapEventVarbindOid_Object = MibTableColumn
trapEventVarbindOid = _TrapEventVarbindOid_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 3),
    _TrapEventVarbindOid_Type()
)
trapEventVarbindOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventVarbindOid.setStatus("current")
_TrapEventVarbindType_Type = Integer32
_TrapEventVarbindType_Object = MibTableColumn
trapEventVarbindType = _TrapEventVarbindType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 4),
    _TrapEventVarbindType_Type()
)
trapEventVarbindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventVarbindType.setStatus("current")
_TrapEventVarbindValue_Type = DisplayString
_TrapEventVarbindValue_Object = MibTableColumn
trapEventVarbindValue = _TrapEventVarbindValue_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 6, 1, 3, 1, 1, 5),
    _TrapEventVarbindValue_Type()
)
trapEventVarbindValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventVarbindValue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-TRAP-EVENT-MIB",
    **{"dellNetTrapEventMib": dellNetTrapEventMib,
       "dellNetTrapEventObjects": dellNetTrapEventObjects,
       "dellNetHistoryTrapEvent": dellNetHistoryTrapEvent,
       "dellNetChassisBootupTime": dellNetChassisBootupTime,
       "dellNetLastTrapEventSeqId": dellNetLastTrapEventSeqId,
       "dellNetMaxHistoryTableSize": dellNetMaxHistoryTableSize,
       "dellNetHistoryTrapEventTable": dellNetHistoryTrapEventTable,
       "dellNetHistoryTrapEventEntry": dellNetHistoryTrapEventEntry,
       "historyTrapEventSeqId": historyTrapEventSeqId,
       "historyTrapEventSeverity": historyTrapEventSeverity,
       "historyTrapEventType": historyTrapEventType,
       "historyTrapEventMsg": historyTrapEventMsg,
       "historyTrapEventOid": historyTrapEventOid,
       "historyTrapEventSlot": historyTrapEventSlot,
       "historyTrapEventTimeStamp": historyTrapEventTimeStamp,
       "historyTrapEventPort": historyTrapEventPort,
       "dellNetActiveTrapEvent": dellNetActiveTrapEvent,
       "dellNetActiveTrapEventTable": dellNetActiveTrapEventTable,
       "dellNetActiveTrapEventEntry": dellNetActiveTrapEventEntry,
       "activeTrapEventSeqId": activeTrapEventSeqId,
       "activeTrapEventSeverity": activeTrapEventSeverity,
       "activeTrapEventType": activeTrapEventType,
       "activeTrapEventMsg": activeTrapEventMsg,
       "activeTrapEventOid": activeTrapEventOid,
       "activeTrapEventSlot": activeTrapEventSlot,
       "activeTrapEventTimeStamp": activeTrapEventTimeStamp,
       "activeTrapEventPort": activeTrapEventPort,
       "dellNetTrapVarbindEvent": dellNetTrapVarbindEvent,
       "dellNetTrapEventVarbindTable": dellNetTrapEventVarbindTable,
       "dellNetTrapEventVarbindEntry": dellNetTrapEventVarbindEntry,
       "trapEventVarbindSeqId": trapEventVarbindSeqId,
       "trapEventVarbindId": trapEventVarbindId,
       "trapEventVarbindOid": trapEventVarbindOid,
       "trapEventVarbindType": trapEventVarbindType,
       "trapEventVarbindValue": trapEventVarbindValue}
)
