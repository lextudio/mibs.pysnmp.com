# SNMP MIB module (HUAWEI-REDUNDANCY-POWER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-REDUNDANCY-POWER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:43 2024
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

(mlsr,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "mlsr")

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

redundancyPower = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RedundancyPowerTable_Object = MibTable
redundancyPowerTable = _RedundancyPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4, 1)
)
if mibBuilder.loadTexts:
    redundancyPowerTable.setStatus("current")
_RedundancyPowerEntry_Object = MibTableRow
redundancyPowerEntry = _RedundancyPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4, 1, 1)
)
redundancyPowerEntry.setIndexNames(
    (0, "HUAWEI-REDUNDANCY-POWER-MIB", "redundancyPowerID"),
)
if mibBuilder.loadTexts:
    redundancyPowerEntry.setStatus("current")
_RedundancyPowerID_Type = Integer32
_RedundancyPowerID_Object = MibTableColumn
redundancyPowerID = _RedundancyPowerID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4, 1, 1, 1),
    _RedundancyPowerID_Type()
)
redundancyPowerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyPowerID.setStatus("current")


class _RedundancyPowerStatus_Type(Integer32):
    """Custom type redundancyPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("normal", 2),
          ("space", 1))
    )


_RedundancyPowerStatus_Type.__name__ = "Integer32"
_RedundancyPowerStatus_Object = MibTableColumn
redundancyPowerStatus = _RedundancyPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4, 1, 1, 2),
    _RedundancyPowerStatus_Type()
)
redundancyPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyPowerStatus.setStatus("current")


class _RedundancyPowerPreviousStatus_Type(Integer32):
    """Custom type redundancyPowerPreviousStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("normal", 2),
          ("space", 1))
    )


_RedundancyPowerPreviousStatus_Type.__name__ = "Integer32"
_RedundancyPowerPreviousStatus_Object = MibTableColumn
redundancyPowerPreviousStatus = _RedundancyPowerPreviousStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4, 1, 1, 3),
    _RedundancyPowerPreviousStatus_Type()
)
redundancyPowerPreviousStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyPowerPreviousStatus.setStatus("current")
_PowerTraps_ObjectIdentity = ObjectIdentity
powerTraps = _PowerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4, 2)
)
_RedundancyFan_ObjectIdentity = ObjectIdentity
redundancyFan = _RedundancyFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5)
)
_RedundancyFanTable_Object = MibTable
redundancyFanTable = _RedundancyFanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5, 1)
)
if mibBuilder.loadTexts:
    redundancyFanTable.setStatus("current")
_RedundancyFanEntry_Object = MibTableRow
redundancyFanEntry = _RedundancyFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5, 1, 1)
)
redundancyFanEntry.setIndexNames(
    (0, "HUAWEI-REDUNDANCY-POWER-MIB", "redundancyFanID"),
)
if mibBuilder.loadTexts:
    redundancyFanEntry.setStatus("current")
_RedundancyFanID_Type = Integer32
_RedundancyFanID_Object = MibTableColumn
redundancyFanID = _RedundancyFanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5, 1, 1, 1),
    _RedundancyFanID_Type()
)
redundancyFanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyFanID.setStatus("current")


class _RedundancyFanStatus_Type(Integer32):
    """Custom type redundancyFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("normal", 1))
    )


_RedundancyFanStatus_Type.__name__ = "Integer32"
_RedundancyFanStatus_Object = MibTableColumn
redundancyFanStatus = _RedundancyFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5, 1, 1, 2),
    _RedundancyFanStatus_Type()
)
redundancyFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    redundancyFanStatus.setStatus("current")
_FanTraps_ObjectIdentity = ObjectIdentity
fanTraps = _FanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5, 2)
)

# Managed Objects groups


# Notification objects

powerStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 4, 2, 1)
)
powerStatusChangedTrap.setObjects(
      *(("HUAWEI-REDUNDANCY-POWER-MIB", "redundancyPowerID"),
        ("HUAWEI-REDUNDANCY-POWER-MIB", "redundancyPowerStatus"),
        ("HUAWEI-REDUNDANCY-POWER-MIB", "redundancyPowerPreviousStatus"))
)
if mibBuilder.loadTexts:
    powerStatusChangedTrap.setStatus(
        "current"
    )

fanStatusChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 2, 33, 5, 2, 1)
)
fanStatusChangedTrap.setObjects(
      *(("HUAWEI-REDUNDANCY-POWER-MIB", "redundancyFanID"),
        ("HUAWEI-REDUNDANCY-POWER-MIB", "redundancyFanStatus"))
)
if mibBuilder.loadTexts:
    fanStatusChangedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-REDUNDANCY-POWER-MIB",
    **{"redundancyPower": redundancyPower,
       "redundancyPowerTable": redundancyPowerTable,
       "redundancyPowerEntry": redundancyPowerEntry,
       "redundancyPowerID": redundancyPowerID,
       "redundancyPowerStatus": redundancyPowerStatus,
       "redundancyPowerPreviousStatus": redundancyPowerPreviousStatus,
       "powerTraps": powerTraps,
       "powerStatusChangedTrap": powerStatusChangedTrap,
       "redundancyFan": redundancyFan,
       "redundancyFanTable": redundancyFanTable,
       "redundancyFanEntry": redundancyFanEntry,
       "redundancyFanID": redundancyFanID,
       "redundancyFanStatus": redundancyFanStatus,
       "fanTraps": fanTraps,
       "fanStatusChangedTrap": fanStatusChangedTrap}
)
