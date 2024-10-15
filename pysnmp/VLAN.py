# SNMP MIB module (VLAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VLAN
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:44 2024
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

(interface,) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "interface")

(VlanGroupT,
 VlanStatusT) = mibBuilder.importSymbols(
    "ExaltComm",
    "VlanGroupT",
    "VlanStatusT")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3)
)
if mibBuilder.loadTexts:
    vlan.setStatus("current")
_VlanStatus_Type = VlanStatusT
_VlanStatus_Object = MibScalar
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("current")


class _VlanDefaultMgmtId_Type(Integer32):
    """Custom type vlanDefaultMgmtId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanDefaultMgmtId_Type.__name__ = "Integer32"
_VlanDefaultMgmtId_Object = MibScalar
vlanDefaultMgmtId = _VlanDefaultMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 5),
    _VlanDefaultMgmtId_Type()
)
vlanDefaultMgmtId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultMgmtId.setStatus("current")
_VlanInterfaces_Object = MibTable
vlanInterfaces = _VlanInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6)
)
if mibBuilder.loadTexts:
    vlanInterfaces.setStatus("current")
_VlanInterfacesEntry_Object = MibTableRow
vlanInterfacesEntry = _VlanInterfacesEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1)
)
vlanInterfacesEntry.setIndexNames(
    (0, "VLAN", "vlanDefaultId"),
)
if mibBuilder.loadTexts:
    vlanInterfacesEntry.setStatus("current")


class _VlanDefaultId_Type(Integer32):
    """Custom type vlanDefaultId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_VlanDefaultId_Type.__name__ = "Integer32"
_VlanDefaultId_Object = MibTableColumn
vlanDefaultId = _VlanDefaultId_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 1),
    _VlanDefaultId_Type()
)
vlanDefaultId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDefaultId.setStatus("current")


class _VlanID_Type(DisplayString):
    """Custom type vlanID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_VlanID_Type.__name__ = "DisplayString"
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 6, 1, 2),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanID.setStatus("current")


class _CommitVlanSettings_Type(DisplayString):
    """Custom type commitVlanSettings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 200),
    )


_CommitVlanSettings_Type.__name__ = "DisplayString"
_CommitVlanSettings_Object = MibScalar
commitVlanSettings = _CommitVlanSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 3, 1000),
    _CommitVlanSettings_Type()
)
commitVlanSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitVlanSettings.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VLAN",
    **{"vlan": vlan,
       "vlanStatus": vlanStatus,
       "vlanDefaultMgmtId": vlanDefaultMgmtId,
       "vlanInterfaces": vlanInterfaces,
       "vlanInterfacesEntry": vlanInterfacesEntry,
       "vlanDefaultId": vlanDefaultId,
       "vlanID": vlanID,
       "commitVlanSettings": commitVlanSettings}
)
