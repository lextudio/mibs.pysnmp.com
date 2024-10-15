# SNMP MIB module (LEA-SMART-SPLITTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LEA-SMART-SPLITTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:17:39 2024
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

(leaSplitters,) = mibBuilder.importSymbols(
    "LEA-MIB",
    "leaSplitters")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

leaSmartSplitter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1)
)
leaSmartSplitter.setRevisions(
        ("2002-09-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SplitterRelay_ObjectIdentity = ObjectIdentity
splitterRelay = _SplitterRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1)
)


class _RelayActiveDuration_Type(Integer32):
    """Custom type relayActiveDuration based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_RelayActiveDuration_Type.__name__ = "Integer32"
_RelayActiveDuration_Object = MibScalar
relayActiveDuration = _RelayActiveDuration_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 1),
    _RelayActiveDuration_Type()
)
relayActiveDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayActiveDuration.setStatus("current")


class _NumberOfActiveRelays_Type(Integer32):
    """Custom type numberOfActiveRelays based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NumberOfActiveRelays_Type.__name__ = "Integer32"
_NumberOfActiveRelays_Object = MibScalar
numberOfActiveRelays = _NumberOfActiveRelays_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 2),
    _NumberOfActiveRelays_Type()
)
numberOfActiveRelays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfActiveRelays.setStatus("current")


class _HeartBeat_Type(Integer32):
    """Custom type heartBeat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ack", 1)
    )


_HeartBeat_Type.__name__ = "Integer32"
_HeartBeat_Object = MibScalar
heartBeat = _HeartBeat_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 3),
    _HeartBeat_Type()
)
heartBeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    heartBeat.setStatus("current")
_RelayTable_Object = MibTable
relayTable = _RelayTable_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    relayTable.setStatus("current")
_RelayTableEntry_Object = MibTableRow
relayTableEntry = _RelayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 4, 1)
)
relayTableEntry.setIndexNames(
    (0, "LEA-SMART-SPLITTER-MIB", "relayIndex"),
)
if mibBuilder.loadTexts:
    relayTableEntry.setStatus("current")
_RelayIndex_Type = Integer32
_RelayIndex_Object = MibTableColumn
relayIndex = _RelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 4, 1, 1),
    _RelayIndex_Type()
)
relayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    relayIndex.setStatus("current")


class _RelaySlot_Type(Integer32):
    """Custom type relaySlot based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("Slot-1", 1),
          ("Slot-10", 10),
          ("Slot-11", 11),
          ("Slot-12", 12),
          ("Slot-13", 13),
          ("Slot-14", 14),
          ("Slot-15", 15),
          ("Slot-2", 2),
          ("Slot-3", 3),
          ("Slot-4", 4),
          ("Slot-5", 5),
          ("Slot-6", 6),
          ("Slot-7", 7),
          ("Slot-8", 8),
          ("Slot-9", 9))
    )


_RelaySlot_Type.__name__ = "Integer32"
_RelaySlot_Object = MibTableColumn
relaySlot = _RelaySlot_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 4, 1, 2),
    _RelaySlot_Type()
)
relaySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relaySlot.setStatus("current")


class _RelayPort_Type(Integer32):
    """Custom type relayPort based on Integer32"""
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
              24)
        )
    )
    namedValues = NamedValues(
        *(("Port-1", 1),
          ("Port-10", 10),
          ("Port-11", 11),
          ("Port-12", 12),
          ("Port-13", 13),
          ("Port-14", 14),
          ("Port-15", 15),
          ("Port-16", 16),
          ("Port-17", 17),
          ("Port-18", 18),
          ("Port-19", 19),
          ("Port-2", 2),
          ("Port-20", 20),
          ("Port-21", 21),
          ("Port-22", 22),
          ("Port-23", 23),
          ("Port-24", 24),
          ("Port-3", 3),
          ("Port-4", 4),
          ("Port-5", 5),
          ("Port-6", 6),
          ("Port-7", 7),
          ("Port-8", 8),
          ("Port-9", 9))
    )


_RelayPort_Type.__name__ = "Integer32"
_RelayPort_Object = MibTableColumn
relayPort = _RelayPort_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 4, 1, 3),
    _RelayPort_Type()
)
relayPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayPort.setStatus("current")


class _RelayStatus_Type(Integer32):
    """Custom type relayStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("normal", 1))
    )


_RelayStatus_Type.__name__ = "Integer32"
_RelayStatus_Object = MibTableColumn
relayStatus = _RelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 4, 1, 4),
    _RelayStatus_Type()
)
relayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayStatus.setStatus("current")


class _RelayResetAll_Type(Integer32):
    """Custom type relayResetAll based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 2),
          ("unchanged", 1))
    )


_RelayResetAll_Type.__name__ = "Integer32"
_RelayResetAll_Object = MibScalar
relayResetAll = _RelayResetAll_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 5),
    _RelayResetAll_Type()
)
relayResetAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayResetAll.setStatus("current")
_RelayChangeNotification_Type = SnmpAdminString
_RelayChangeNotification_Object = MibScalar
relayChangeNotification = _RelayChangeNotification_Object(
    (1, 3, 6, 1, 4, 1, 14841, 1, 1, 1, 6),
    _RelayChangeNotification_Type()
)
relayChangeNotification.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    relayChangeNotification.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEA-SMART-SPLITTER-MIB",
    **{"leaSmartSplitter": leaSmartSplitter,
       "splitterRelay": splitterRelay,
       "relayActiveDuration": relayActiveDuration,
       "numberOfActiveRelays": numberOfActiveRelays,
       "heartBeat": heartBeat,
       "relayTable": relayTable,
       "relayTableEntry": relayTableEntry,
       "relayIndex": relayIndex,
       "relaySlot": relaySlot,
       "relayPort": relayPort,
       "relayStatus": relayStatus,
       "relayResetAll": relayResetAll,
       "relayChangeNotification": relayChangeNotification}
)
