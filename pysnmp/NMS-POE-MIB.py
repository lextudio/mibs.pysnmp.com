# SNMP MIB module (NMS-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:03 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Poe_ObjectIdentity = ObjectIdentity
poe = _Poe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236)
)
_PowerEtherTable_Object = MibTable
powerEtherTable = _PowerEtherTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1)
)
if mibBuilder.loadTexts:
    powerEtherTable.setStatus("mandatory")
_PowerEtherTableEntry_Object = MibTableRow
powerEtherTableEntry = _PowerEtherTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1)
)
powerEtherTableEntry.setIndexNames(
    (0, "NMS-POE-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    powerEtherTableEntry.setStatus("mandatory")
_IfIndex_Type = Integer32
_IfIndex_Object = MibTableColumn
ifIndex = _IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 1),
    _IfIndex_Type()
)
ifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIndex.setStatus("mandatory")


class _IfDescr_Type(DisplayString):
    """Custom type ifDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfDescr_Type.__name__ = "DisplayString"
_IfDescr_Object = MibTableColumn
ifDescr = _IfDescr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 2),
    _IfDescr_Type()
)
ifDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifDescr.setStatus("mandatory")
_IfPethPortControlAbility_Type = TruthValue
_IfPethPortControlAbility_Object = MibTableColumn
ifPethPortControlAbility = _IfPethPortControlAbility_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 3),
    _IfPethPortControlAbility_Type()
)
ifPethPortControlAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPethPortControlAbility.setStatus("mandatory")


class _IfPethPortMaxPower_Type(Integer32):
    """Custom type ifPethPortMaxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_IfPethPortMaxPower_Type.__name__ = "Integer32"
_IfPethPortMaxPower_Object = MibTableColumn
ifPethPortMaxPower = _IfPethPortMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 4),
    _IfPethPortMaxPower_Type()
)
ifPethPortMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPethPortMaxPower.setStatus("mandatory")
_IfPethPortConsumptionPower_Type = Integer32
_IfPethPortConsumptionPower_Object = MibTableColumn
ifPethPortConsumptionPower = _IfPethPortConsumptionPower_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 236, 1, 1, 5),
    _IfPethPortConsumptionPower_Type()
)
ifPethPortConsumptionPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPethPortConsumptionPower.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-POE-MIB",
    **{"poe": poe,
       "powerEtherTable": powerEtherTable,
       "powerEtherTableEntry": powerEtherTableEntry,
       "ifIndex": ifIndex,
       "ifDescr": ifDescr,
       "ifPethPortControlAbility": ifPethPortControlAbility,
       "ifPethPortMaxPower": ifPethPortMaxPower,
       "ifPethPortConsumptionPower": ifPethPortConsumptionPower}
)
