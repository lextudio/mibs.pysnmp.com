# SNMP MIB module (BAY-STACK-UNICAST-STORM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-UNICAST-STORM-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:23 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackUnicastStormControlMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 22)
)
bayStackUnicastStormControlMib.setRevisions(
        ("2007-06-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsUnicastStormControlNotifications_ObjectIdentity = ObjectIdentity
bsUnicastStormControlNotifications = _BsUnicastStormControlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 0)
)
_BsUnicastStormControlObjects_ObjectIdentity = ObjectIdentity
bsUnicastStormControlObjects = _BsUnicastStormControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1)
)
_BsUnicastStormControlScalars_ObjectIdentity = ObjectIdentity
bsUnicastStormControlScalars = _BsUnicastStormControlScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 1)
)
_BsUnicastStormControlEnabled_Type = TruthValue
_BsUnicastStormControlEnabled_Object = MibScalar
bsUnicastStormControlEnabled = _BsUnicastStormControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 1, 1),
    _BsUnicastStormControlEnabled_Type()
)
bsUnicastStormControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsUnicastStormControlEnabled.setStatus("current")


class _BsUnicastStormControlLowWatermark_Type(Unsigned32):
    """Custom type bsUnicastStormControlLowWatermark based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000000),
    )


_BsUnicastStormControlLowWatermark_Type.__name__ = "Unsigned32"
_BsUnicastStormControlLowWatermark_Object = MibScalar
bsUnicastStormControlLowWatermark = _BsUnicastStormControlLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 1, 2),
    _BsUnicastStormControlLowWatermark_Type()
)
bsUnicastStormControlLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsUnicastStormControlLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    bsUnicastStormControlLowWatermark.setUnits("packets per second")


class _BsUnicastStormControlHighWatermark_Type(Unsigned32):
    """Custom type bsUnicastStormControlHighWatermark based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000000),
    )


_BsUnicastStormControlHighWatermark_Type.__name__ = "Unsigned32"
_BsUnicastStormControlHighWatermark_Object = MibScalar
bsUnicastStormControlHighWatermark = _BsUnicastStormControlHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 1, 3),
    _BsUnicastStormControlHighWatermark_Type()
)
bsUnicastStormControlHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsUnicastStormControlHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    bsUnicastStormControlHighWatermark.setUnits("packets per second")


class _BsUnicastStormControlPollInterval_Type(TimeInterval):
    """Custom type bsUnicastStormControlPollInterval based on TimeInterval"""
    defaultValue = 3000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 30000),
    )


_BsUnicastStormControlPollInterval_Type.__name__ = "TimeInterval"
_BsUnicastStormControlPollInterval_Object = MibScalar
bsUnicastStormControlPollInterval = _BsUnicastStormControlPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 1, 4),
    _BsUnicastStormControlPollInterval_Type()
)
bsUnicastStormControlPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsUnicastStormControlPollInterval.setStatus("current")


class _BsUnicastStormControlTrapInterval_Type(Integer32):
    """Custom type bsUnicastStormControlTrapInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BsUnicastStormControlTrapInterval_Type.__name__ = "Integer32"
_BsUnicastStormControlTrapInterval_Object = MibScalar
bsUnicastStormControlTrapInterval = _BsUnicastStormControlTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 1, 5),
    _BsUnicastStormControlTrapInterval_Type()
)
bsUnicastStormControlTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsUnicastStormControlTrapInterval.setStatus("current")
_BsUnicastStormControlPollValue_Type = Unsigned32
_BsUnicastStormControlPollValue_Object = MibScalar
bsUnicastStormControlPollValue = _BsUnicastStormControlPollValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 1, 6),
    _BsUnicastStormControlPollValue_Type()
)
bsUnicastStormControlPollValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsUnicastStormControlPollValue.setStatus("current")
_BsUnicastStormControlIfTable_Object = MibTable
bsUnicastStormControlIfTable = _BsUnicastStormControlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 2)
)
if mibBuilder.loadTexts:
    bsUnicastStormControlIfTable.setStatus("current")
_BsUnicastStormControlIfEntry_Object = MibTableRow
bsUnicastStormControlIfEntry = _BsUnicastStormControlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 2, 1)
)
bsUnicastStormControlIfEntry.setIndexNames(
    (0, "BAY-STACK-UNICAST-STORM-CONTROL-MIB", "bsUnicastStormControlIfIndex"),
)
if mibBuilder.loadTexts:
    bsUnicastStormControlIfEntry.setStatus("current")
_BsUnicastStormControlIfIndex_Type = InterfaceIndex
_BsUnicastStormControlIfIndex_Object = MibTableColumn
bsUnicastStormControlIfIndex = _BsUnicastStormControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 2, 1, 1),
    _BsUnicastStormControlIfIndex_Type()
)
bsUnicastStormControlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsUnicastStormControlIfIndex.setStatus("current")
_BsUnicastStormControlIfEnabled_Type = TruthValue
_BsUnicastStormControlIfEnabled_Object = MibTableColumn
bsUnicastStormControlIfEnabled = _BsUnicastStormControlIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 1, 2, 1, 2),
    _BsUnicastStormControlIfEnabled_Type()
)
bsUnicastStormControlIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsUnicastStormControlIfEnabled.setStatus("current")

# Managed Objects groups


# Notification objects

bsUnicastStormControlBelowLowWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 0, 1)
)
bsUnicastStormControlBelowLowWatermark.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAY-STACK-UNICAST-STORM-CONTROL-MIB", "bsUnicastStormControlPollValue"),
        ("BAY-STACK-UNICAST-STORM-CONTROL-MIB", "bsUnicastStormControlLowWatermark"))
)
if mibBuilder.loadTexts:
    bsUnicastStormControlBelowLowWatermark.setStatus(
        "current"
    )

bsUnicastStormControlAboveHighWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 22, 0, 2)
)
bsUnicastStormControlAboveHighWatermark.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("BAY-STACK-UNICAST-STORM-CONTROL-MIB", "bsUnicastStormControlPollValue"),
        ("BAY-STACK-UNICAST-STORM-CONTROL-MIB", "bsUnicastStormControlHighWatermark"))
)
if mibBuilder.loadTexts:
    bsUnicastStormControlAboveHighWatermark.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-UNICAST-STORM-CONTROL-MIB",
    **{"bayStackUnicastStormControlMib": bayStackUnicastStormControlMib,
       "bsUnicastStormControlNotifications": bsUnicastStormControlNotifications,
       "bsUnicastStormControlBelowLowWatermark": bsUnicastStormControlBelowLowWatermark,
       "bsUnicastStormControlAboveHighWatermark": bsUnicastStormControlAboveHighWatermark,
       "bsUnicastStormControlObjects": bsUnicastStormControlObjects,
       "bsUnicastStormControlScalars": bsUnicastStormControlScalars,
       "bsUnicastStormControlEnabled": bsUnicastStormControlEnabled,
       "bsUnicastStormControlLowWatermark": bsUnicastStormControlLowWatermark,
       "bsUnicastStormControlHighWatermark": bsUnicastStormControlHighWatermark,
       "bsUnicastStormControlPollInterval": bsUnicastStormControlPollInterval,
       "bsUnicastStormControlTrapInterval": bsUnicastStormControlTrapInterval,
       "bsUnicastStormControlPollValue": bsUnicastStormControlPollValue,
       "bsUnicastStormControlIfTable": bsUnicastStormControlIfTable,
       "bsUnicastStormControlIfEntry": bsUnicastStormControlIfEntry,
       "bsUnicastStormControlIfIndex": bsUnicastStormControlIfIndex,
       "bsUnicastStormControlIfEnabled": bsUnicastStormControlIfEnabled}
)
