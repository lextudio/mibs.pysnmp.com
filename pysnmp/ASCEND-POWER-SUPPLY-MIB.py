# SNMP MIB module (ASCEND-POWER-SUPPLY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASCEND-POWER-SUPPLY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:39 2024
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

(powerSupply,) = mibBuilder.importSymbols(
    "ASCEND-MIB",
    "powerSupply")

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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PowerSupplyCount_Type = Integer32
_PowerSupplyCount_Object = MibScalar
powerSupplyCount = _PowerSupplyCount_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 1),
    _PowerSupplyCount_Type()
)
powerSupplyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyCount.setStatus("mandatory")
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 2)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("mandatory")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 2, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "ASCEND-POWER-SUPPLY-MIB", "powerSupplyIndex"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("mandatory")
_PowerSupplyIndex_Type = Integer32
_PowerSupplyIndex_Object = MibTableColumn
powerSupplyIndex = _PowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 1),
    _PowerSupplyIndex_Type()
)
powerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyIndex.setStatus("mandatory")


class _PowerSupplyState_Type(Integer32):
    """Custom type powerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("other", 1),
          ("present", 2))
    )


_PowerSupplyState_Type.__name__ = "Integer32"
_PowerSupplyState_Object = MibTableColumn
powerSupplyState = _PowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 2),
    _PowerSupplyState_Type()
)
powerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyState.setStatus("mandatory")


class _PowerSupplyOperationalState_Type(Integer32):
    """Custom type powerSupplyOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 3),
          ("noFailure", 2),
          ("other", 1))
    )


_PowerSupplyOperationalState_Type.__name__ = "Integer32"
_PowerSupplyOperationalState_Object = MibTableColumn
powerSupplyOperationalState = _PowerSupplyOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 3),
    _PowerSupplyOperationalState_Type()
)
powerSupplyOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyOperationalState.setStatus("mandatory")
_PowerSupplySerialNumber_Type = Integer32
_PowerSupplySerialNumber_Object = MibTableColumn
powerSupplySerialNumber = _PowerSupplySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 2, 1, 4),
    _PowerSupplySerialNumber_Type()
)
powerSupplySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplySerialNumber.setStatus("mandatory")


class _PowerSupplyStateTrapState_Type(Integer32):
    """Custom type powerSupplyStateTrapState based on Integer32"""
    defaultValue = 1

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


_PowerSupplyStateTrapState_Type.__name__ = "Integer32"
_PowerSupplyStateTrapState_Object = MibScalar
powerSupplyStateTrapState = _PowerSupplyStateTrapState_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 3),
    _PowerSupplyStateTrapState_Type()
)
powerSupplyStateTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSupplyStateTrapState.setStatus("mandatory")


class _PowerSupplyOperationalStateTrapState_Type(Integer32):
    """Custom type powerSupplyOperationalStateTrapState based on Integer32"""
    defaultValue = 1

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


_PowerSupplyOperationalStateTrapState_Type.__name__ = "Integer32"
_PowerSupplyOperationalStateTrapState_Object = MibScalar
powerSupplyOperationalStateTrapState = _PowerSupplyOperationalStateTrapState_Object(
    (1, 3, 6, 1, 4, 1, 529, 18, 4),
    _PowerSupplyOperationalStateTrapState_Type()
)
powerSupplyOperationalStateTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerSupplyOperationalStateTrapState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASCEND-POWER-SUPPLY-MIB",
    **{"powerSupplyCount": powerSupplyCount,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyIndex": powerSupplyIndex,
       "powerSupplyState": powerSupplyState,
       "powerSupplyOperationalState": powerSupplyOperationalState,
       "powerSupplySerialNumber": powerSupplySerialNumber,
       "powerSupplyStateTrapState": powerSupplyStateTrapState,
       "powerSupplyOperationalStateTrapState": powerSupplyOperationalStateTrapState}
)
