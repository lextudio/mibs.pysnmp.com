# SNMP MIB module (BAY-STACK-STORM-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAY-STACK-STORM-CONTROL-MIB
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

bayStackStormControlMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 42)
)
bayStackStormControlMib.setRevisions(
        ("2014-03-04 00:00",
         "2012-06-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsStormControlNotifications_ObjectIdentity = ObjectIdentity
bsStormControlNotifications = _BsStormControlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 0)
)
_BsStormControlObjects_ObjectIdentity = ObjectIdentity
bsStormControlObjects = _BsStormControlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1)
)
_BsStormControlScalars_ObjectIdentity = ObjectIdentity
bsStormControlScalars = _BsStormControlScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 1)
)
_BsStormControlPollValue_Type = Unsigned32
_BsStormControlPollValue_Object = MibScalar
bsStormControlPollValue = _BsStormControlPollValue_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 1, 1),
    _BsStormControlPollValue_Type()
)
bsStormControlPollValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bsStormControlPollValue.setStatus("current")
_BsStormControlTable_Object = MibTable
bsStormControlTable = _BsStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2)
)
if mibBuilder.loadTexts:
    bsStormControlTable.setStatus("current")
_BsStormControlEntry_Object = MibTableRow
bsStormControlEntry = _BsStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1)
)
bsStormControlEntry.setIndexNames(
    (0, "BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"),
)
if mibBuilder.loadTexts:
    bsStormControlEntry.setStatus("current")


class _BsStormControlTrafficType_Type(Integer32):
    """Custom type bsStormControlTrafficType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("multicast", 3),
          ("unicast", 1))
    )


_BsStormControlTrafficType_Type.__name__ = "Integer32"
_BsStormControlTrafficType_Object = MibTableColumn
bsStormControlTrafficType = _BsStormControlTrafficType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 1),
    _BsStormControlTrafficType_Type()
)
bsStormControlTrafficType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsStormControlTrafficType.setStatus("current")
_BsStormControlEnabled_Type = TruthValue
_BsStormControlEnabled_Object = MibTableColumn
bsStormControlEnabled = _BsStormControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 2),
    _BsStormControlEnabled_Type()
)
bsStormControlEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlEnabled.setStatus("current")


class _BsStormControlLowWatermark_Type(Unsigned32):
    """Custom type bsStormControlLowWatermark based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000000),
    )


_BsStormControlLowWatermark_Type.__name__ = "Unsigned32"
_BsStormControlLowWatermark_Object = MibTableColumn
bsStormControlLowWatermark = _BsStormControlLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 3),
    _BsStormControlLowWatermark_Type()
)
bsStormControlLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    bsStormControlLowWatermark.setUnits("packets per second")


class _BsStormControlHighWatermark_Type(Unsigned32):
    """Custom type bsStormControlHighWatermark based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000000),
    )


_BsStormControlHighWatermark_Type.__name__ = "Unsigned32"
_BsStormControlHighWatermark_Object = MibTableColumn
bsStormControlHighWatermark = _BsStormControlHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 4),
    _BsStormControlHighWatermark_Type()
)
bsStormControlHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    bsStormControlHighWatermark.setUnits("packets per second")


class _BsStormControlPollInterval_Type(TimeInterval):
    """Custom type bsStormControlPollInterval based on TimeInterval"""
    defaultValue = 3000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 30000),
    )


_BsStormControlPollInterval_Type.__name__ = "TimeInterval"
_BsStormControlPollInterval_Object = MibTableColumn
bsStormControlPollInterval = _BsStormControlPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 5),
    _BsStormControlPollInterval_Type()
)
bsStormControlPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlPollInterval.setStatus("current")


class _BsStormControlTrapInterval_Type(Integer32):
    """Custom type bsStormControlTrapInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BsStormControlTrapInterval_Type.__name__ = "Integer32"
_BsStormControlTrapInterval_Object = MibTableColumn
bsStormControlTrapInterval = _BsStormControlTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 6),
    _BsStormControlTrapInterval_Type()
)
bsStormControlTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlTrapInterval.setStatus("current")


class _BsStormControlActionType_Type(Integer32):
    """Custom type bsStormControlActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("none", 1),
          ("shutdown", 3))
    )


_BsStormControlActionType_Type.__name__ = "Integer32"
_BsStormControlActionType_Object = MibTableColumn
bsStormControlActionType = _BsStormControlActionType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 2, 1, 7),
    _BsStormControlActionType_Type()
)
bsStormControlActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlActionType.setStatus("current")
_BsStormControlIfTable_Object = MibTable
bsStormControlIfTable = _BsStormControlIfTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3)
)
if mibBuilder.loadTexts:
    bsStormControlIfTable.setStatus("current")
_BsStormControlIfEntry_Object = MibTableRow
bsStormControlIfEntry = _BsStormControlIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1)
)
bsStormControlIfEntry.setIndexNames(
    (0, "BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"),
    (0, "BAY-STACK-STORM-CONTROL-MIB", "bsStormControlIfIndex"),
)
if mibBuilder.loadTexts:
    bsStormControlIfEntry.setStatus("current")
_BsStormControlIfIndex_Type = InterfaceIndex
_BsStormControlIfIndex_Object = MibTableColumn
bsStormControlIfIndex = _BsStormControlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 1),
    _BsStormControlIfIndex_Type()
)
bsStormControlIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsStormControlIfIndex.setStatus("current")
_BsStormControlIfEnabled_Type = TruthValue
_BsStormControlIfEnabled_Object = MibTableColumn
bsStormControlIfEnabled = _BsStormControlIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 2),
    _BsStormControlIfEnabled_Type()
)
bsStormControlIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlIfEnabled.setStatus("current")


class _BsStormControlIfLowWatermark_Type(Unsigned32):
    """Custom type bsStormControlIfLowWatermark based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000000),
    )


_BsStormControlIfLowWatermark_Type.__name__ = "Unsigned32"
_BsStormControlIfLowWatermark_Object = MibTableColumn
bsStormControlIfLowWatermark = _BsStormControlIfLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 3),
    _BsStormControlIfLowWatermark_Type()
)
bsStormControlIfLowWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlIfLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    bsStormControlIfLowWatermark.setUnits("packets per second")


class _BsStormControlIfHighWatermark_Type(Unsigned32):
    """Custom type bsStormControlIfHighWatermark based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000000),
    )


_BsStormControlIfHighWatermark_Type.__name__ = "Unsigned32"
_BsStormControlIfHighWatermark_Object = MibTableColumn
bsStormControlIfHighWatermark = _BsStormControlIfHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 4),
    _BsStormControlIfHighWatermark_Type()
)
bsStormControlIfHighWatermark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlIfHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    bsStormControlIfHighWatermark.setUnits("packets per second")


class _BsStormControlIfPollInterval_Type(TimeInterval):
    """Custom type bsStormControlIfPollInterval based on TimeInterval"""
    defaultValue = 3000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 30000),
    )


_BsStormControlIfPollInterval_Type.__name__ = "TimeInterval"
_BsStormControlIfPollInterval_Object = MibTableColumn
bsStormControlIfPollInterval = _BsStormControlIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 5),
    _BsStormControlIfPollInterval_Type()
)
bsStormControlIfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlIfPollInterval.setStatus("current")


class _BsStormControlIfTrapInterval_Type(Integer32):
    """Custom type bsStormControlIfTrapInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_BsStormControlIfTrapInterval_Type.__name__ = "Integer32"
_BsStormControlIfTrapInterval_Object = MibTableColumn
bsStormControlIfTrapInterval = _BsStormControlIfTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 6),
    _BsStormControlIfTrapInterval_Type()
)
bsStormControlIfTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlIfTrapInterval.setStatus("current")


class _BsStormControlIfActionType_Type(Integer32):
    """Custom type bsStormControlIfActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("none", 1),
          ("shutdown", 3))
    )


_BsStormControlIfActionType_Type.__name__ = "Integer32"
_BsStormControlIfActionType_Object = MibTableColumn
bsStormControlIfActionType = _BsStormControlIfActionType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 1, 3, 1, 7),
    _BsStormControlIfActionType_Type()
)
bsStormControlIfActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsStormControlIfActionType.setStatus("current")

# Managed Objects groups


# Notification objects

bsStormControlBelowLowWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 0, 1)
)
bsStormControlBelowLowWatermark.setObjects(
      *(("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"),
        ("IF-MIB", "ifIndex"),
        ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlPollValue"),
        ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlLowWatermark"))
)
if mibBuilder.loadTexts:
    bsStormControlBelowLowWatermark.setStatus(
        "current"
    )

bsStormControlAboveHighWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 42, 0, 2)
)
bsStormControlAboveHighWatermark.setObjects(
      *(("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlTrafficType"),
        ("IF-MIB", "ifIndex"),
        ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlPollValue"),
        ("BAY-STACK-STORM-CONTROL-MIB", "bsStormControlHighWatermark"))
)
if mibBuilder.loadTexts:
    bsStormControlAboveHighWatermark.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-STORM-CONTROL-MIB",
    **{"bayStackStormControlMib": bayStackStormControlMib,
       "bsStormControlNotifications": bsStormControlNotifications,
       "bsStormControlBelowLowWatermark": bsStormControlBelowLowWatermark,
       "bsStormControlAboveHighWatermark": bsStormControlAboveHighWatermark,
       "bsStormControlObjects": bsStormControlObjects,
       "bsStormControlScalars": bsStormControlScalars,
       "bsStormControlPollValue": bsStormControlPollValue,
       "bsStormControlTable": bsStormControlTable,
       "bsStormControlEntry": bsStormControlEntry,
       "bsStormControlTrafficType": bsStormControlTrafficType,
       "bsStormControlEnabled": bsStormControlEnabled,
       "bsStormControlLowWatermark": bsStormControlLowWatermark,
       "bsStormControlHighWatermark": bsStormControlHighWatermark,
       "bsStormControlPollInterval": bsStormControlPollInterval,
       "bsStormControlTrapInterval": bsStormControlTrapInterval,
       "bsStormControlActionType": bsStormControlActionType,
       "bsStormControlIfTable": bsStormControlIfTable,
       "bsStormControlIfEntry": bsStormControlIfEntry,
       "bsStormControlIfIndex": bsStormControlIfIndex,
       "bsStormControlIfEnabled": bsStormControlIfEnabled,
       "bsStormControlIfLowWatermark": bsStormControlIfLowWatermark,
       "bsStormControlIfHighWatermark": bsStormControlIfHighWatermark,
       "bsStormControlIfPollInterval": bsStormControlIfPollInterval,
       "bsStormControlIfTrapInterval": bsStormControlIfTrapInterval,
       "bsStormControlIfActionType": bsStormControlIfActionType}
)
