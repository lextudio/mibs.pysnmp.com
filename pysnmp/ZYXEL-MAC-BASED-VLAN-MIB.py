# SNMP MIB module (ZYXEL-MAC-BASED-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MAC-BASED-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:17 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMacBasedVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelMacBasedVlanSetup_ObjectIdentity = ObjectIdentity
zyxelMacBasedVlanSetup = _ZyxelMacBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1)
)
_ZyMacBasedVlanMaxNumberOfVlans_Type = Integer32
_ZyMacBasedVlanMaxNumberOfVlans_Object = MibScalar
zyMacBasedVlanMaxNumberOfVlans = _ZyMacBasedVlanMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 1),
    _ZyMacBasedVlanMaxNumberOfVlans_Type()
)
zyMacBasedVlanMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMacBasedVlanMaxNumberOfVlans.setStatus("current")
_ZyxelMacBasedVlanBindingTable_Object = MibTable
zyxelMacBasedVlanBindingTable = _ZyxelMacBasedVlanBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelMacBasedVlanBindingTable.setStatus("current")
_ZyxelMacBasedVlanBindingEntry_Object = MibTableRow
zyxelMacBasedVlanBindingEntry = _ZyxelMacBasedVlanBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1)
)
zyxelMacBasedVlanBindingEntry.setIndexNames(
    (0, "ZYXEL-MAC-BASED-VLAN-MIB", "zyMacBasedVlanBindingSourceMac"),
)
if mibBuilder.loadTexts:
    zyxelMacBasedVlanBindingEntry.setStatus("current")
_ZyMacBasedVlanBindingSourceMac_Type = MacAddress
_ZyMacBasedVlanBindingSourceMac_Object = MibTableColumn
zyMacBasedVlanBindingSourceMac = _ZyMacBasedVlanBindingSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 1),
    _ZyMacBasedVlanBindingSourceMac_Type()
)
zyMacBasedVlanBindingSourceMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMacBasedVlanBindingSourceMac.setStatus("current")
_ZyMacBasedVlanBindingName_Type = OctetString
_ZyMacBasedVlanBindingName_Object = MibTableColumn
zyMacBasedVlanBindingName = _ZyMacBasedVlanBindingName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 2),
    _ZyMacBasedVlanBindingName_Type()
)
zyMacBasedVlanBindingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacBasedVlanBindingName.setStatus("current")


class _ZyMacBasedVlanBindingVlan_Type(Integer32):
    """Custom type zyMacBasedVlanBindingVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyMacBasedVlanBindingVlan_Type.__name__ = "Integer32"
_ZyMacBasedVlanBindingVlan_Object = MibTableColumn
zyMacBasedVlanBindingVlan = _ZyMacBasedVlanBindingVlan_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 3),
    _ZyMacBasedVlanBindingVlan_Type()
)
zyMacBasedVlanBindingVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacBasedVlanBindingVlan.setStatus("current")


class _ZyMacBasedVlanBindingPriority_Type(Integer32):
    """Custom type zyMacBasedVlanBindingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZyMacBasedVlanBindingPriority_Type.__name__ = "Integer32"
_ZyMacBasedVlanBindingPriority_Object = MibTableColumn
zyMacBasedVlanBindingPriority = _ZyMacBasedVlanBindingPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 4),
    _ZyMacBasedVlanBindingPriority_Type()
)
zyMacBasedVlanBindingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMacBasedVlanBindingPriority.setStatus("current")
_ZyMacBasedVlanBindingRowStatus_Type = RowStatus
_ZyMacBasedVlanBindingRowStatus_Object = MibTableColumn
zyMacBasedVlanBindingRowStatus = _ZyMacBasedVlanBindingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 1, 2, 1, 5),
    _ZyMacBasedVlanBindingRowStatus_Type()
)
zyMacBasedVlanBindingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyMacBasedVlanBindingRowStatus.setStatus("current")
_ZyxelMacBasedVlanStatus_ObjectIdentity = ObjectIdentity
zyxelMacBasedVlanStatus = _ZyxelMacBasedVlanStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 99, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MAC-BASED-VLAN-MIB",
    **{"zyxelMacBasedVlan": zyxelMacBasedVlan,
       "zyxelMacBasedVlanSetup": zyxelMacBasedVlanSetup,
       "zyMacBasedVlanMaxNumberOfVlans": zyMacBasedVlanMaxNumberOfVlans,
       "zyxelMacBasedVlanBindingTable": zyxelMacBasedVlanBindingTable,
       "zyxelMacBasedVlanBindingEntry": zyxelMacBasedVlanBindingEntry,
       "zyMacBasedVlanBindingSourceMac": zyMacBasedVlanBindingSourceMac,
       "zyMacBasedVlanBindingName": zyMacBasedVlanBindingName,
       "zyMacBasedVlanBindingVlan": zyMacBasedVlanBindingVlan,
       "zyMacBasedVlanBindingPriority": zyMacBasedVlanBindingPriority,
       "zyMacBasedVlanBindingRowStatus": zyMacBasedVlanBindingRowStatus,
       "zyxelMacBasedVlanStatus": zyxelMacBasedVlanStatus}
)
