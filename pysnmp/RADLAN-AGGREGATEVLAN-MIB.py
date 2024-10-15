# SNMP MIB module (RADLAN-AGGREGATEVLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-AGGREGATEVLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:41:35 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(rnd,) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rnd")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlAggregateVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 89, 73)
)
rlAggregateVlan.setRevisions(
        ("2007-01-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlAggregateVlanMibVersion_Type = Integer32
_RlAggregateVlanMibVersion_Object = MibScalar
rlAggregateVlanMibVersion = _RlAggregateVlanMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 1),
    _RlAggregateVlanMibVersion_Type()
)
rlAggregateVlanMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAggregateVlanMibVersion.setStatus("current")
_RlAggregateVlanTable_Object = MibTable
rlAggregateVlanTable = _RlAggregateVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2)
)
if mibBuilder.loadTexts:
    rlAggregateVlanTable.setStatus("current")
_RlAggregateVlanEntry_Object = MibTableRow
rlAggregateVlanEntry = _RlAggregateVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1)
)
rlAggregateVlanEntry.setIndexNames(
    (0, "RADLAN-AGGREGATEVLAN-MIB", "rlAggregateVlanIndex"),
)
if mibBuilder.loadTexts:
    rlAggregateVlanEntry.setStatus("current")
_RlAggregateVlanIndex_Type = InterfaceIndex
_RlAggregateVlanIndex_Object = MibTableColumn
rlAggregateVlanIndex = _RlAggregateVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 1),
    _RlAggregateVlanIndex_Type()
)
rlAggregateVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlAggregateVlanIndex.setStatus("current")


class _RlAggregateVlanName_Type(DisplayString):
    """Custom type rlAggregateVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlAggregateVlanName_Type.__name__ = "DisplayString"
_RlAggregateVlanName_Object = MibTableColumn
rlAggregateVlanName = _RlAggregateVlanName_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 2),
    _RlAggregateVlanName_Type()
)
rlAggregateVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlAggregateVlanName.setStatus("current")


class _RlAggregateVlanPhysAddressType_Type(Integer32):
    """Custom type rlAggregateVlanPhysAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reserve", 2))
    )


_RlAggregateVlanPhysAddressType_Type.__name__ = "Integer32"
_RlAggregateVlanPhysAddressType_Object = MibTableColumn
rlAggregateVlanPhysAddressType = _RlAggregateVlanPhysAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 3),
    _RlAggregateVlanPhysAddressType_Type()
)
rlAggregateVlanPhysAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlAggregateVlanPhysAddressType.setStatus("current")
_RlAggregateVlanStatus_Type = RowStatus
_RlAggregateVlanStatus_Object = MibTableColumn
rlAggregateVlanStatus = _RlAggregateVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 2, 1, 4),
    _RlAggregateVlanStatus_Type()
)
rlAggregateVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlAggregateVlanStatus.setStatus("current")
_RlAggregateSubVlanTable_Object = MibTable
rlAggregateSubVlanTable = _RlAggregateSubVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3)
)
if mibBuilder.loadTexts:
    rlAggregateSubVlanTable.setStatus("current")
_RlAggregateSubVlanEntry_Object = MibTableRow
rlAggregateSubVlanEntry = _RlAggregateSubVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3, 1)
)
rlAggregateSubVlanEntry.setIndexNames(
    (0, "RADLAN-AGGREGATEVLAN-MIB", "rlAggregateVlanIndex"),
    (0, "RADLAN-AGGREGATEVLAN-MIB", "rlAggregateSubVlanIfIndex"),
)
if mibBuilder.loadTexts:
    rlAggregateSubVlanEntry.setStatus("current")
_RlAggregateSubVlanIfIndex_Type = InterfaceIndex
_RlAggregateSubVlanIfIndex_Object = MibTableColumn
rlAggregateSubVlanIfIndex = _RlAggregateSubVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3, 1, 1),
    _RlAggregateSubVlanIfIndex_Type()
)
rlAggregateSubVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlAggregateSubVlanIfIndex.setStatus("current")
_RlAggregateSubVlanStatus_Type = RowStatus
_RlAggregateSubVlanStatus_Object = MibTableColumn
rlAggregateSubVlanStatus = _RlAggregateSubVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 3, 1, 2),
    _RlAggregateSubVlanStatus_Type()
)
rlAggregateSubVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlAggregateSubVlanStatus.setStatus("current")


class _RlAggregateVlanArpProxy_Type(Integer32):
    """Custom type rlAggregateVlanArpProxy based on Integer32"""
    defaultValue = 2

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


_RlAggregateVlanArpProxy_Type.__name__ = "Integer32"
_RlAggregateVlanArpProxy_Object = MibScalar
rlAggregateVlanArpProxy = _RlAggregateVlanArpProxy_Object(
    (1, 3, 6, 1, 4, 1, 89, 73, 4),
    _RlAggregateVlanArpProxy_Type()
)
rlAggregateVlanArpProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlAggregateVlanArpProxy.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-AGGREGATEVLAN-MIB",
    **{"rlAggregateVlan": rlAggregateVlan,
       "rlAggregateVlanMibVersion": rlAggregateVlanMibVersion,
       "rlAggregateVlanTable": rlAggregateVlanTable,
       "rlAggregateVlanEntry": rlAggregateVlanEntry,
       "rlAggregateVlanIndex": rlAggregateVlanIndex,
       "rlAggregateVlanName": rlAggregateVlanName,
       "rlAggregateVlanPhysAddressType": rlAggregateVlanPhysAddressType,
       "rlAggregateVlanStatus": rlAggregateVlanStatus,
       "rlAggregateSubVlanTable": rlAggregateSubVlanTable,
       "rlAggregateSubVlanEntry": rlAggregateSubVlanEntry,
       "rlAggregateSubVlanIfIndex": rlAggregateSubVlanIfIndex,
       "rlAggregateSubVlanStatus": rlAggregateSubVlanStatus,
       "rlAggregateVlanArpProxy": rlAggregateVlanArpProxy}
)
