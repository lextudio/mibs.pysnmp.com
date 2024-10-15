# SNMP MIB module (ZYXEL-SUBNET-BASED-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-SUBNET-BASED-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:52 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelSubnetBasedVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelSubnetBasedVlanSetup_ObjectIdentity = ObjectIdentity
zyxelSubnetBasedVlanSetup = _ZyxelSubnetBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1)
)
_ZySubnetBasedVlanState_Type = EnabledStatus
_ZySubnetBasedVlanState_Object = MibScalar
zySubnetBasedVlanState = _ZySubnetBasedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 1),
    _ZySubnetBasedVlanState_Type()
)
zySubnetBasedVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySubnetBasedVlanState.setStatus("current")
_ZySubnetBasedVlanDhcpVlanOverrideState_Type = EnabledStatus
_ZySubnetBasedVlanDhcpVlanOverrideState_Object = MibScalar
zySubnetBasedVlanDhcpVlanOverrideState = _ZySubnetBasedVlanDhcpVlanOverrideState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 2),
    _ZySubnetBasedVlanDhcpVlanOverrideState_Type()
)
zySubnetBasedVlanDhcpVlanOverrideState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySubnetBasedVlanDhcpVlanOverrideState.setStatus("current")
_ZySubnetBasedVlanMaxNumberOfVlans_Type = Integer32
_ZySubnetBasedVlanMaxNumberOfVlans_Object = MibScalar
zySubnetBasedVlanMaxNumberOfVlans = _ZySubnetBasedVlanMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 3),
    _ZySubnetBasedVlanMaxNumberOfVlans_Type()
)
zySubnetBasedVlanMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySubnetBasedVlanMaxNumberOfVlans.setStatus("current")
_ZyxelSubnetBasedVlanTable_Object = MibTable
zyxelSubnetBasedVlanTable = _ZyxelSubnetBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelSubnetBasedVlanTable.setStatus("current")
_ZyxelSubnetBasedVlanEntry_Object = MibTableRow
zyxelSubnetBasedVlanEntry = _ZyxelSubnetBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4, 1)
)
zyxelSubnetBasedVlanEntry.setIndexNames(
    (0, "ZYXEL-SUBNET-BASED-VLAN-MIB", "zySubnetBasedVlanSourceIpAddress"),
    (0, "ZYXEL-SUBNET-BASED-VLAN-MIB", "zySubnetBasedVlanSourceMaskBits"),
)
if mibBuilder.loadTexts:
    zyxelSubnetBasedVlanEntry.setStatus("current")
_ZySubnetBasedVlanSourceIpAddress_Type = IpAddress
_ZySubnetBasedVlanSourceIpAddress_Object = MibTableColumn
zySubnetBasedVlanSourceIpAddress = _ZySubnetBasedVlanSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4, 1, 1),
    _ZySubnetBasedVlanSourceIpAddress_Type()
)
zySubnetBasedVlanSourceIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySubnetBasedVlanSourceIpAddress.setStatus("current")


class _ZySubnetBasedVlanSourceMaskBits_Type(Integer32):
    """Custom type zySubnetBasedVlanSourceMaskBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZySubnetBasedVlanSourceMaskBits_Type.__name__ = "Integer32"
_ZySubnetBasedVlanSourceMaskBits_Object = MibTableColumn
zySubnetBasedVlanSourceMaskBits = _ZySubnetBasedVlanSourceMaskBits_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4, 1, 2),
    _ZySubnetBasedVlanSourceMaskBits_Type()
)
zySubnetBasedVlanSourceMaskBits.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zySubnetBasedVlanSourceMaskBits.setStatus("current")


class _ZySubnetBasedVlanName_Type(DisplayString):
    """Custom type zySubnetBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZySubnetBasedVlanName_Type.__name__ = "DisplayString"
_ZySubnetBasedVlanName_Object = MibTableColumn
zySubnetBasedVlanName = _ZySubnetBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4, 1, 3),
    _ZySubnetBasedVlanName_Type()
)
zySubnetBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySubnetBasedVlanName.setStatus("current")


class _ZySubnetBasedVlanVid_Type(Integer32):
    """Custom type zySubnetBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZySubnetBasedVlanVid_Type.__name__ = "Integer32"
_ZySubnetBasedVlanVid_Object = MibTableColumn
zySubnetBasedVlanVid = _ZySubnetBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4, 1, 4),
    _ZySubnetBasedVlanVid_Type()
)
zySubnetBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySubnetBasedVlanVid.setStatus("current")


class _ZySubnetBasedVlanPriority_Type(Integer32):
    """Custom type zySubnetBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZySubnetBasedVlanPriority_Type.__name__ = "Integer32"
_ZySubnetBasedVlanPriority_Object = MibTableColumn
zySubnetBasedVlanPriority = _ZySubnetBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4, 1, 5),
    _ZySubnetBasedVlanPriority_Type()
)
zySubnetBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySubnetBasedVlanPriority.setStatus("current")
_ZySubnetBasedVlanRowStatus_Type = RowStatus
_ZySubnetBasedVlanRowStatus_Object = MibTableColumn
zySubnetBasedVlanRowStatus = _ZySubnetBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 80, 1, 4, 1, 6),
    _ZySubnetBasedVlanRowStatus_Type()
)
zySubnetBasedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zySubnetBasedVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SUBNET-BASED-VLAN-MIB",
    **{"zyxelSubnetBasedVlan": zyxelSubnetBasedVlan,
       "zyxelSubnetBasedVlanSetup": zyxelSubnetBasedVlanSetup,
       "zySubnetBasedVlanState": zySubnetBasedVlanState,
       "zySubnetBasedVlanDhcpVlanOverrideState": zySubnetBasedVlanDhcpVlanOverrideState,
       "zySubnetBasedVlanMaxNumberOfVlans": zySubnetBasedVlanMaxNumberOfVlans,
       "zyxelSubnetBasedVlanTable": zyxelSubnetBasedVlanTable,
       "zyxelSubnetBasedVlanEntry": zyxelSubnetBasedVlanEntry,
       "zySubnetBasedVlanSourceIpAddress": zySubnetBasedVlanSourceIpAddress,
       "zySubnetBasedVlanSourceMaskBits": zySubnetBasedVlanSourceMaskBits,
       "zySubnetBasedVlanName": zySubnetBasedVlanName,
       "zySubnetBasedVlanVid": zySubnetBasedVlanVid,
       "zySubnetBasedVlanPriority": zySubnetBasedVlanPriority,
       "zySubnetBasedVlanRowStatus": zySubnetBasedVlanRowStatus}
)
