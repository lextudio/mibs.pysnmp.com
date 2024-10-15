# SNMP MIB module (ITOUCH-EVENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ITOUCH-EVENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:11 2024
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

(DateTime,
 iTouch) = mibBuilder.importSymbols(
    "ITOUCH-MIB",
    "DateTime",
    "iTouch")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class EventGroup(Integer32):
    """Custom type EventGroup based on Integer32"""
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
              58)
        )
    )
    namedValues = NamedValues(
        *(("appleTalk", 1),
          ("appleTalkArps", 2),
          ("appleTalkNbp", 5),
          ("appleTalkRtmp", 3),
          ("appleTalkTraffic", 6),
          ("appleTalkZip", 4),
          ("atm", 7),
          ("backup", 8),
          ("chassis", 10),
          ("circuit", 11),
          ("clns", 12),
          ("decNet", 13),
          ("decNetTraffic", 14),
          ("egp", 15),
          ("esis", 16),
          ("fddi", 17),
          ("fddiTraffic", 18),
          ("frame", 19),
          ("frameRelay", 20),
          ("hubManagement", 21),
          ("interface", 22),
          ("ip", 23),
          ("ipRip", 24),
          ("ipRoutes", 25),
          ("ipTraffic", 26),
          ("ipx", 27),
          ("ipxRip", 28),
          ("ipxSap", 29),
          ("isdn", 30),
          ("isdnQ931", 31),
          ("isdnTrace", 32),
          ("isis", 33),
          ("isisHello", 34),
          ("isisLsp", 35),
          ("link", 36),
          ("lmb", 37),
          ("lqm", 38),
          ("ospf", 39),
          ("ospfHello", 40),
          ("ospfLsaPacket", 41),
          ("ospfSpf", 42),
          ("param", 43),
          ("pcmcia", 9),
          ("ppp", 44),
          ("session", 45),
          ("snmp", 47),
          ("spanningTree", 46),
          ("switchForwarding", 48),
          ("switchLoopDetect", 49),
          ("switchManagement", 50),
          ("system", 51),
          ("tcp", 52),
          ("time", 53),
          ("tokenRingManagement", 54),
          ("udp", 55),
          ("ui", 56),
          ("vlmp", 57),
          ("x25", 58))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XEvent_ObjectIdentity = ObjectIdentity
xEvent = _XEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 33)
)


class _EventTableSize_Type(Integer32):
    """Custom type eventTableSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 800),
    )


_EventTableSize_Type.__name__ = "Integer32"
_EventTableSize_Object = MibScalar
eventTableSize = _EventTableSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 1),
    _EventTableSize_Type()
)
eventTableSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTableSize.setStatus("mandatory")


class _EventSeverity_Type(Integer32):
    """Custom type eventSeverity based on Integer32"""
    defaultValue = 2

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
        *(("discard", 1),
          ("high", 4),
          ("low", 2),
          ("medium", 3))
    )


_EventSeverity_Type.__name__ = "Integer32"
_EventSeverity_Object = MibScalar
eventSeverity = _EventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 2),
    _EventSeverity_Type()
)
eventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventSeverity.setStatus("mandatory")


class _EventTimestamp_Type(Integer32):
    """Custom type eventTimestamp based on Integer32"""
    defaultValue = 4

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
        *(("date", 2),
          ("datetime", 4),
          ("none", 1),
          ("time", 3))
    )


_EventTimestamp_Type.__name__ = "Integer32"
_EventTimestamp_Object = MibScalar
eventTimestamp = _EventTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 3),
    _EventTimestamp_Type()
)
eventTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventTimestamp.setStatus("mandatory")


class _EventLanguage_Type(Integer32):
    """Custom type eventLanguage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("english", 1)
    )


_EventLanguage_Type.__name__ = "Integer32"
_EventLanguage_Object = MibScalar
eventLanguage = _EventLanguage_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 4),
    _EventLanguage_Type()
)
eventLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLanguage.setStatus("mandatory")


class _EventClearLog_Type(Integer32):
    """Custom type eventClearLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_EventClearLog_Type.__name__ = "Integer32"
_EventClearLog_Object = MibScalar
eventClearLog = _EventClearLog_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 5),
    _EventClearLog_Type()
)
eventClearLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventClearLog.setStatus("mandatory")


class _EventEnableAll_Type(Integer32):
    """Custom type eventEnableAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_EventEnableAll_Type.__name__ = "Integer32"
_EventEnableAll_Object = MibScalar
eventEnableAll = _EventEnableAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 6),
    _EventEnableAll_Type()
)
eventEnableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventEnableAll.setStatus("mandatory")


class _EventDisableAll_Type(Integer32):
    """Custom type eventDisableAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_EventDisableAll_Type.__name__ = "Integer32"
_EventDisableAll_Object = MibScalar
eventDisableAll = _EventDisableAll_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 7),
    _EventDisableAll_Type()
)
eventDisableAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventDisableAll.setStatus("mandatory")
_EventGroupTable_Object = MibTable
eventGroupTable = _EventGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 8)
)
if mibBuilder.loadTexts:
    eventGroupTable.setStatus("mandatory")
_EventGroupEntry_Object = MibTableRow
eventGroupEntry = _EventGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 8, 1)
)
eventGroupEntry.setIndexNames(
    (0, "ITOUCH-EVENT-MIB", "eventGroupIndex"),
)
if mibBuilder.loadTexts:
    eventGroupEntry.setStatus("mandatory")
_EventGroupIndex_Type = EventGroup
_EventGroupIndex_Object = MibTableColumn
eventGroupIndex = _EventGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 8, 1, 1),
    _EventGroupIndex_Type()
)
eventGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventGroupIndex.setStatus("mandatory")


class _EventGroupState_Type(Integer32):
    """Custom type eventGroupState based on Integer32"""
    defaultValue = 1

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


_EventGroupState_Type.__name__ = "Integer32"
_EventGroupState_Object = MibTableColumn
eventGroupState = _EventGroupState_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 8, 1, 2),
    _EventGroupState_Type()
)
eventGroupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventGroupState.setStatus("mandatory")
_EventTextTable_Object = MibTable
eventTextTable = _EventTextTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 9)
)
if mibBuilder.loadTexts:
    eventTextTable.setStatus("mandatory")
_EventTextEntry_Object = MibTableRow
eventTextEntry = _EventTextEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 9, 1)
)
eventTextEntry.setIndexNames(
    (0, "ITOUCH-EVENT-MIB", "eventTextGroupIndex"),
    (0, "ITOUCH-EVENT-MIB", "eventTextEventIndex"),
)
if mibBuilder.loadTexts:
    eventTextEntry.setStatus("mandatory")
_EventTextGroupIndex_Type = EventGroup
_EventTextGroupIndex_Object = MibTableColumn
eventTextGroupIndex = _EventTextGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 1),
    _EventTextGroupIndex_Type()
)
eventTextGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTextGroupIndex.setStatus("mandatory")
_EventTextEventIndex_Type = Integer32
_EventTextEventIndex_Object = MibTableColumn
eventTextEventIndex = _EventTextEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 2),
    _EventTextEventIndex_Type()
)
eventTextEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTextEventIndex.setStatus("mandatory")


class _EventTextText_Type(DisplayString):
    """Custom type eventTextText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_EventTextText_Type.__name__ = "DisplayString"
_EventTextText_Object = MibTableColumn
eventTextText = _EventTextText_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 3),
    _EventTextText_Type()
)
eventTextText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTextText.setStatus("mandatory")
_EventTextDateTime_Type = DateTime
_EventTextDateTime_Object = MibTableColumn
eventTextDateTime = _EventTextDateTime_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 4),
    _EventTextDateTime_Type()
)
eventTextDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTextDateTime.setStatus("mandatory")


class _EventTextSeverity_Type(Integer32):
    """Custom type eventTextSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("high", 4),
          ("low", 2),
          ("medium", 3))
    )


_EventTextSeverity_Type.__name__ = "Integer32"
_EventTextSeverity_Object = MibTableColumn
eventTextSeverity = _EventTextSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 33, 9, 1, 5),
    _EventTextSeverity_Type()
)
eventTextSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventTextSeverity.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ITOUCH-EVENT-MIB",
    **{"EventGroup": EventGroup,
       "xEvent": xEvent,
       "eventTableSize": eventTableSize,
       "eventSeverity": eventSeverity,
       "eventTimestamp": eventTimestamp,
       "eventLanguage": eventLanguage,
       "eventClearLog": eventClearLog,
       "eventEnableAll": eventEnableAll,
       "eventDisableAll": eventDisableAll,
       "eventGroupTable": eventGroupTable,
       "eventGroupEntry": eventGroupEntry,
       "eventGroupIndex": eventGroupIndex,
       "eventGroupState": eventGroupState,
       "eventTextTable": eventTextTable,
       "eventTextEntry": eventTextEntry,
       "eventTextGroupIndex": eventTextGroupIndex,
       "eventTextEventIndex": eventTextEventIndex,
       "eventTextText": eventTextText,
       "eventTextDateTime": eventTextDateTime,
       "eventTextSeverity": eventTextSeverity}
)
