# SNMP MIB module (ORACLE-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ORACLE-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:35 2024
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



class DateAndTime(OctetString):
    """Custom type DateAndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 11),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oracle_ObjectIdentity = ObjectIdentity
oracle = _Oracle_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111)
)
_OraAgent_ObjectIdentity = ObjectIdentity
oraAgent = _OraAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 12)
)
_OraAgentObjects_ObjectIdentity = ObjectIdentity
oraAgentObjects = _OraAgentObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 12, 1)
)
_OraAgentEventTable_Object = MibTable
oraAgentEventTable = _OraAgentEventTable_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1)
)
if mibBuilder.loadTexts:
    oraAgentEventTable.setStatus("mandatory")
_OraAgentEventEntry_Object = MibTableRow
oraAgentEventEntry = _OraAgentEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1)
)
oraAgentEventEntry.setIndexNames(
    (0, "ORACLE-AGENT-MIB", "oraAgentEventIndex"),
)
if mibBuilder.loadTexts:
    oraAgentEventEntry.setStatus("mandatory")
_OraAgentEventIndex_Type = Integer32
_OraAgentEventIndex_Object = MibTableColumn
oraAgentEventIndex = _OraAgentEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 1),
    _OraAgentEventIndex_Type()
)
oraAgentEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventIndex.setStatus("mandatory")
_OraAgentEventName_Type = DisplayString
_OraAgentEventName_Object = MibTableColumn
oraAgentEventName = _OraAgentEventName_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 2),
    _OraAgentEventName_Type()
)
oraAgentEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventName.setStatus("mandatory")
_OraAgentEventID_Type = Integer32
_OraAgentEventID_Object = MibTableColumn
oraAgentEventID = _OraAgentEventID_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 3),
    _OraAgentEventID_Type()
)
oraAgentEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventID.setStatus("mandatory")
_OraAgentEventService_Type = DisplayString
_OraAgentEventService_Object = MibTableColumn
oraAgentEventService = _OraAgentEventService_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 4),
    _OraAgentEventService_Type()
)
oraAgentEventService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventService.setStatus("mandatory")
_OraAgentEventTime_Type = DateAndTime
_OraAgentEventTime_Object = MibTableColumn
oraAgentEventTime = _OraAgentEventTime_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 5),
    _OraAgentEventTime_Type()
)
oraAgentEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventTime.setStatus("mandatory")


class _OraAgentEventSeverity_Type(Integer32):
    """Custom type oraAgentEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alert", 2),
          ("clear", -1),
          ("warning", 1))
    )


_OraAgentEventSeverity_Type.__name__ = "Integer32"
_OraAgentEventSeverity_Object = MibTableColumn
oraAgentEventSeverity = _OraAgentEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 6),
    _OraAgentEventSeverity_Type()
)
oraAgentEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventSeverity.setStatus("mandatory")
_OraAgentEventUser_Type = DisplayString
_OraAgentEventUser_Object = MibTableColumn
oraAgentEventUser = _OraAgentEventUser_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 7),
    _OraAgentEventUser_Type()
)
oraAgentEventUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventUser.setStatus("mandatory")
_OraAgentEventAppID_Type = Integer32
_OraAgentEventAppID_Object = MibTableColumn
oraAgentEventAppID = _OraAgentEventAppID_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 8),
    _OraAgentEventAppID_Type()
)
oraAgentEventAppID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventAppID.setStatus("mandatory")
_OraAgentEventMessage_Type = DisplayString
_OraAgentEventMessage_Object = MibTableColumn
oraAgentEventMessage = _OraAgentEventMessage_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 9),
    _OraAgentEventMessage_Type()
)
oraAgentEventMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventMessage.setStatus("mandatory")
_OraAgentEventArguments_Type = DisplayString
_OraAgentEventArguments_Object = MibTableColumn
oraAgentEventArguments = _OraAgentEventArguments_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 10),
    _OraAgentEventArguments_Type()
)
oraAgentEventArguments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventArguments.setStatus("mandatory")
_OraAgentEventResults_Type = DisplayString
_OraAgentEventResults_Object = MibTableColumn
oraAgentEventResults = _OraAgentEventResults_Object(
    (1, 3, 6, 1, 4, 1, 111, 12, 1, 1, 1, 11),
    _OraAgentEventResults_Type()
)
oraAgentEventResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oraAgentEventResults.setStatus("mandatory")
_OraAgentTraps_ObjectIdentity = ObjectIdentity
oraAgentTraps = _OraAgentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 111, 12, 2)
)

# Managed Objects groups


# Notification objects

oraAgentEventOcc = NotificationType(
    (1, 3, 6, 1, 4, 1, 111, 12, 2, 0, 2)
)
oraAgentEventOcc.setObjects(
      *(("ORACLE-AGENT-MIB", "oraAgentEventName"),
        ("ORACLE-AGENT-MIB", "oraAgentEventID"),
        ("ORACLE-AGENT-MIB", "oraAgentEventService"),
        ("ORACLE-AGENT-MIB", "oraAgentEventTime"),
        ("ORACLE-AGENT-MIB", "oraAgentEventSeverity"),
        ("ORACLE-AGENT-MIB", "oraAgentEventUser"),
        ("ORACLE-AGENT-MIB", "oraAgentEventAppID"),
        ("ORACLE-AGENT-MIB", "oraAgentEventMessage"),
        ("ORACLE-AGENT-MIB", "oraAgentEventArguments"),
        ("ORACLE-AGENT-MIB", "oraAgentEventResults"))
)
if mibBuilder.loadTexts:
    oraAgentEventOcc.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ORACLE-AGENT-MIB",
    **{"DateAndTime": DateAndTime,
       "oracle": oracle,
       "oraAgent": oraAgent,
       "oraAgentObjects": oraAgentObjects,
       "oraAgentEventTable": oraAgentEventTable,
       "oraAgentEventEntry": oraAgentEventEntry,
       "oraAgentEventIndex": oraAgentEventIndex,
       "oraAgentEventName": oraAgentEventName,
       "oraAgentEventID": oraAgentEventID,
       "oraAgentEventService": oraAgentEventService,
       "oraAgentEventTime": oraAgentEventTime,
       "oraAgentEventSeverity": oraAgentEventSeverity,
       "oraAgentEventUser": oraAgentEventUser,
       "oraAgentEventAppID": oraAgentEventAppID,
       "oraAgentEventMessage": oraAgentEventMessage,
       "oraAgentEventArguments": oraAgentEventArguments,
       "oraAgentEventResults": oraAgentEventResults,
       "oraAgentTraps": oraAgentTraps,
       "oraAgentEventOcc": oraAgentEventOcc}
)
