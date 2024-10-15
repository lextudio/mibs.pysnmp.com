# SNMP MIB module (HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:38 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(hpicfSaviObjectsFilteringEntry,) = mibBuilder.importSymbols(
    "HPICF-SAVI-MIB",
    "hpicfSaviObjectsFilteringEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfIpv6Lockdown = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103)
)
hpicfIpv6Lockdown.setRevisions(
        ("2017-11-08 00:00",
         "2013-10-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDIPLDv6SourceBindingNotifications_ObjectIdentity = ObjectIdentity
hpicfDIPLDv6SourceBindingNotifications = _HpicfDIPLDv6SourceBindingNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0)
)
_HpicfDIPLDv6SourceBindingOutOfResourcesObjects_ObjectIdentity = ObjectIdentity
hpicfDIPLDv6SourceBindingOutOfResourcesObjects = _HpicfDIPLDv6SourceBindingOutOfResourcesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 2)
)
_HpicfDIPLDv6SourceBindingAddrPort_Type = InterfaceIndex
_HpicfDIPLDv6SourceBindingAddrPort_Object = MibScalar
hpicfDIPLDv6SourceBindingAddrPort = _HpicfDIPLDv6SourceBindingAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 2, 1),
    _HpicfDIPLDv6SourceBindingAddrPort_Type()
)
hpicfDIPLDv6SourceBindingAddrPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingAddrPort.setStatus("current")
_HpicfDIPLDv6SourceBindingAddrMacAddress_Type = MacAddress
_HpicfDIPLDv6SourceBindingAddrMacAddress_Object = MibScalar
hpicfDIPLDv6SourceBindingAddrMacAddress = _HpicfDIPLDv6SourceBindingAddrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 2, 2),
    _HpicfDIPLDv6SourceBindingAddrMacAddress_Type()
)
hpicfDIPLDv6SourceBindingAddrMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingAddrMacAddress.setStatus("current")
_HpicfDIPLDv6SourceBindingAddrIpAddressType_Type = InetAddressType
_HpicfDIPLDv6SourceBindingAddrIpAddressType_Object = MibScalar
hpicfDIPLDv6SourceBindingAddrIpAddressType = _HpicfDIPLDv6SourceBindingAddrIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 2, 3),
    _HpicfDIPLDv6SourceBindingAddrIpAddressType_Type()
)
hpicfDIPLDv6SourceBindingAddrIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingAddrIpAddressType.setStatus("current")
_HpicfDIPLDv6SourceBindingAddrIpAddress_Type = InetAddress
_HpicfDIPLDv6SourceBindingAddrIpAddress_Object = MibScalar
hpicfDIPLDv6SourceBindingAddrIpAddress = _HpicfDIPLDv6SourceBindingAddrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 2, 4),
    _HpicfDIPLDv6SourceBindingAddrIpAddress_Type()
)
hpicfDIPLDv6SourceBindingAddrIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingAddrIpAddress.setStatus("current")
_HpicfDIPLDv6SourceBindingAddrVlan_Type = VlanIndex
_HpicfDIPLDv6SourceBindingAddrVlan_Object = MibScalar
hpicfDIPLDv6SourceBindingAddrVlan = _HpicfDIPLDv6SourceBindingAddrVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 2, 5),
    _HpicfDIPLDv6SourceBindingAddrVlan_Type()
)
hpicfDIPLDv6SourceBindingAddrVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingAddrVlan.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsObjects_ObjectIdentity = ObjectIdentity
hpicfDIPLDv6SourceBindingVoilationsObjects = _HpicfDIPLDv6SourceBindingVoilationsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4)
)
_HpicfDIPLDv6SourceBindingVoilationsCount_Type = Counter32
_HpicfDIPLDv6SourceBindingVoilationsCount_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsCount = _HpicfDIPLDv6SourceBindingVoilationsCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 1),
    _HpicfDIPLDv6SourceBindingVoilationsCount_Type()
)
hpicfDIPLDv6SourceBindingVoilationsCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsCount.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsPort_Type = InterfaceIndex
_HpicfDIPLDv6SourceBindingVoilationsPort_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsPort = _HpicfDIPLDv6SourceBindingVoilationsPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 2),
    _HpicfDIPLDv6SourceBindingVoilationsPort_Type()
)
hpicfDIPLDv6SourceBindingVoilationsPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsPort.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Type = InetAddressType
_HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsSrcIpType = _HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 3),
    _HpicfDIPLDv6SourceBindingVoilationsSrcIpType_Type()
)
hpicfDIPLDv6SourceBindingVoilationsSrcIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsSrcIpType.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Type = InetAddress
_HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress = _HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 4),
    _HpicfDIPLDv6SourceBindingVoilationsSrcIpAddress_Type()
)
hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsDstIpType_Type = InetAddressType
_HpicfDIPLDv6SourceBindingVoilationsDstIpType_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsDstIpType = _HpicfDIPLDv6SourceBindingVoilationsDstIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 5),
    _HpicfDIPLDv6SourceBindingVoilationsDstIpType_Type()
)
hpicfDIPLDv6SourceBindingVoilationsDstIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsDstIpType.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Type = InetAddress
_HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsDstIpAddress = _HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 6),
    _HpicfDIPLDv6SourceBindingVoilationsDstIpAddress_Type()
)
hpicfDIPLDv6SourceBindingVoilationsDstIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsDstIpAddress.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsMacAddress_Type = MacAddress
_HpicfDIPLDv6SourceBindingVoilationsMacAddress_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsMacAddress = _HpicfDIPLDv6SourceBindingVoilationsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 7),
    _HpicfDIPLDv6SourceBindingVoilationsMacAddress_Type()
)
hpicfDIPLDv6SourceBindingVoilationsMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsMacAddress.setStatus("current")
_HpicfDIPLDv6SourceBindingVoilationsPktCount_Type = Counter32
_HpicfDIPLDv6SourceBindingVoilationsPktCount_Object = MibScalar
hpicfDIPLDv6SourceBindingVoilationsPktCount = _HpicfDIPLDv6SourceBindingVoilationsPktCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 4, 8),
    _HpicfDIPLDv6SourceBindingVoilationsPktCount_Type()
)
hpicfDIPLDv6SourceBindingVoilationsPktCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilationsPktCount.setStatus("current")
_HpicfDIPLDv6Objects_ObjectIdentity = ObjectIdentity
hpicfDIPLDv6Objects = _HpicfDIPLDv6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1)
)
_HpicfDIPLDv6Config_ObjectIdentity = ObjectIdentity
hpicfDIPLDv6Config = _HpicfDIPLDv6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1)
)
_HpicfDIPLDv6LockEnable_Type = TruthValue
_HpicfDIPLDv6LockEnable_Object = MibScalar
hpicfDIPLDv6LockEnable = _HpicfDIPLDv6LockEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1, 1),
    _HpicfDIPLDv6LockEnable_Type()
)
hpicfDIPLDv6LockEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDIPLDv6LockEnable.setStatus("current")
_HpicfDIPLDv6PortTable_Object = MibTable
hpicfDIPLDv6PortTable = _HpicfDIPLDv6PortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDIPLDv6PortTable.setStatus("current")
_HpicfDIPLDv6PortEntry_Object = MibTableRow
hpicfDIPLDv6PortEntry = _HpicfDIPLDv6PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1, 2, 1)
)
hpicfDIPLDv6PortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfDIPLDv6PortEntry.setStatus("current")
_HpicfDIPLDv6PortEnable_Type = TruthValue
_HpicfDIPLDv6PortEnable_Object = MibTableColumn
hpicfDIPLDv6PortEnable = _HpicfDIPLDv6PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1, 2, 1, 1),
    _HpicfDIPLDv6PortEnable_Type()
)
hpicfDIPLDv6PortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDIPLDv6PortEnable.setStatus("current")


class _HpicfDIPLDv6PortOperStatus_Type(Bits):
    """Custom type hpicfDIPLDv6PortOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("active", 0),
          ("noDsnoopv6", 1),
          ("noSnoopingVlan", 3),
          ("trustedPort", 2))
    )

_HpicfDIPLDv6PortOperStatus_Type.__name__ = "Bits"
_HpicfDIPLDv6PortOperStatus_Object = MibTableColumn
hpicfDIPLDv6PortOperStatus = _HpicfDIPLDv6PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1, 2, 1, 2),
    _HpicfDIPLDv6PortOperStatus_Type()
)
hpicfDIPLDv6PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDIPLDv6PortOperStatus.setStatus("current")


class _HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Type(TruthValue):
    """Custom type hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl based on TruthValue"""


_HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Object = MibScalar
hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl = _HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1, 3),
    _HpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl_Type()
)
hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl.setStatus("current")


class _HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Type(TruthValue):
    """Custom type hpicfDIPLDv6SourceBindingViolationsTrapCtrl based on TruthValue"""


_HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Object = MibScalar
hpicfDIPLDv6SourceBindingViolationsTrapCtrl = _HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 1, 4),
    _HpicfDIPLDv6SourceBindingViolationsTrapCtrl_Type()
)
hpicfDIPLDv6SourceBindingViolationsTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingViolationsTrapCtrl.setStatus("current")
_HpicfDIPLDv6Status_ObjectIdentity = ObjectIdentity
hpicfDIPLDv6Status = _HpicfDIPLDv6Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 2)
)
_HpicfDIPLDv6AddrTable_Object = MibTable
hpicfDIPLDv6AddrTable = _HpicfDIPLDv6AddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDIPLDv6AddrTable.setStatus("current")
_HpicfDIPLDv6AddrEntry_Object = MibTableRow
hpicfDIPLDv6AddrEntry = _HpicfDIPLDv6AddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDIPLDv6AddrEntry.setStatus("current")
_HpicfDIPLDv6AddrVlan_Type = VlanIndex
_HpicfDIPLDv6AddrVlan_Object = MibTableColumn
hpicfDIPLDv6AddrVlan = _HpicfDIPLDv6AddrVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 2, 1, 1, 1),
    _HpicfDIPLDv6AddrVlan_Type()
)
hpicfDIPLDv6AddrVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDIPLDv6AddrVlan.setStatus("current")
_HpicfDIPLDv6ResourceAvailable_Type = TruthValue
_HpicfDIPLDv6ResourceAvailable_Object = MibTableColumn
hpicfDIPLDv6ResourceAvailable = _HpicfDIPLDv6ResourceAvailable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 1, 2, 1, 1, 2),
    _HpicfDIPLDv6ResourceAvailable_Type()
)
hpicfDIPLDv6ResourceAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDIPLDv6ResourceAvailable.setStatus("current")
_HpicfIpv6LockConformance_ObjectIdentity = ObjectIdentity
hpicfIpv6LockConformance = _HpicfIpv6LockConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2)
)
_HpicfIpv6LockGroups_ObjectIdentity = ObjectIdentity
hpicfIpv6LockGroups = _HpicfIpv6LockGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2, 1)
)
_HpicfIpv6LockCompliances_ObjectIdentity = ObjectIdentity
hpicfIpv6LockCompliances = _HpicfIpv6LockCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2, 2)
)
hpicfSaviObjectsFilteringEntry.registerAugmentions(
    ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB",
     "hpicfDIPLDv6AddrEntry")
)
hpicfDIPLDv6AddrEntry.setIndexNames(*hpicfSaviObjectsFilteringEntry.getIndexNames())

# Managed Objects groups

hpicfIpv6LockBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2, 1, 1)
)
hpicfIpv6LockBaseGroup.setObjects(
      *(("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6LockEnable"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6PortEnable"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6PortOperStatus"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6AddrVlan"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6ResourceAvailable"))
)
if mibBuilder.loadTexts:
    hpicfIpv6LockBaseGroup.setStatus("current")

hpicfSourceBindingTrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2, 1, 2)
)
hpicfSourceBindingTrapObjectsGroup.setObjects(
      *(("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrPort"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrMacAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrIpAddressType"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrIpAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrVlan"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsCount"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsPort"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsSrcIpType"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsDstIpType"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsDstIpAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsMacAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsPktCount"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingViolationsTrapCtrl"))
)
if mibBuilder.loadTexts:
    hpicfSourceBindingTrapObjectsGroup.setStatus("current")


# Notification objects

hpicfDIPDv6SourceBindingOutOfResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 1)
)
hpicfDIPDv6SourceBindingOutOfResources.setObjects(
      *(("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrPort"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrMacAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrIpAddressType"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrIpAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingAddrVlan"))
)
if mibBuilder.loadTexts:
    hpicfDIPDv6SourceBindingOutOfResources.setStatus(
        "current"
    )

hpicfDIPLDv6SourceBindingVoilations = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 0, 3)
)
hpicfDIPLDv6SourceBindingVoilations.setObjects(
      *(("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsCount"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsPort"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsSrcIpType"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsDstIpType"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsDstIpAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsMacAddress"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilationsPktCount"))
)
if mibBuilder.loadTexts:
    hpicfDIPLDv6SourceBindingVoilations.setStatus(
        "current"
    )


# Notifications groups

hpicfSourceBindingTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2, 1, 3)
)
hpicfSourceBindingTrapsGroup.setObjects(
      *(("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPDv6SourceBindingOutOfResources"),
        ("HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB", "hpicfDIPLDv6SourceBindingVoilations"))
)
if mibBuilder.loadTexts:
    hpicfSourceBindingTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfDIPLDv6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDIPLDv6Compliance.setStatus(
        "current"
    )

hpicfIpv6SourceBindingTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 103, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfIpv6SourceBindingTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-IPv6-DYNAMIC-LOCKDOWN-MIB",
    **{"hpicfIpv6Lockdown": hpicfIpv6Lockdown,
       "hpicfDIPLDv6SourceBindingNotifications": hpicfDIPLDv6SourceBindingNotifications,
       "hpicfDIPDv6SourceBindingOutOfResources": hpicfDIPDv6SourceBindingOutOfResources,
       "hpicfDIPLDv6SourceBindingOutOfResourcesObjects": hpicfDIPLDv6SourceBindingOutOfResourcesObjects,
       "hpicfDIPLDv6SourceBindingAddrPort": hpicfDIPLDv6SourceBindingAddrPort,
       "hpicfDIPLDv6SourceBindingAddrMacAddress": hpicfDIPLDv6SourceBindingAddrMacAddress,
       "hpicfDIPLDv6SourceBindingAddrIpAddressType": hpicfDIPLDv6SourceBindingAddrIpAddressType,
       "hpicfDIPLDv6SourceBindingAddrIpAddress": hpicfDIPLDv6SourceBindingAddrIpAddress,
       "hpicfDIPLDv6SourceBindingAddrVlan": hpicfDIPLDv6SourceBindingAddrVlan,
       "hpicfDIPLDv6SourceBindingVoilations": hpicfDIPLDv6SourceBindingVoilations,
       "hpicfDIPLDv6SourceBindingVoilationsObjects": hpicfDIPLDv6SourceBindingVoilationsObjects,
       "hpicfDIPLDv6SourceBindingVoilationsCount": hpicfDIPLDv6SourceBindingVoilationsCount,
       "hpicfDIPLDv6SourceBindingVoilationsPort": hpicfDIPLDv6SourceBindingVoilationsPort,
       "hpicfDIPLDv6SourceBindingVoilationsSrcIpType": hpicfDIPLDv6SourceBindingVoilationsSrcIpType,
       "hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress": hpicfDIPLDv6SourceBindingVoilationsSrcIpAddress,
       "hpicfDIPLDv6SourceBindingVoilationsDstIpType": hpicfDIPLDv6SourceBindingVoilationsDstIpType,
       "hpicfDIPLDv6SourceBindingVoilationsDstIpAddress": hpicfDIPLDv6SourceBindingVoilationsDstIpAddress,
       "hpicfDIPLDv6SourceBindingVoilationsMacAddress": hpicfDIPLDv6SourceBindingVoilationsMacAddress,
       "hpicfDIPLDv6SourceBindingVoilationsPktCount": hpicfDIPLDv6SourceBindingVoilationsPktCount,
       "hpicfDIPLDv6Objects": hpicfDIPLDv6Objects,
       "hpicfDIPLDv6Config": hpicfDIPLDv6Config,
       "hpicfDIPLDv6LockEnable": hpicfDIPLDv6LockEnable,
       "hpicfDIPLDv6PortTable": hpicfDIPLDv6PortTable,
       "hpicfDIPLDv6PortEntry": hpicfDIPLDv6PortEntry,
       "hpicfDIPLDv6PortEnable": hpicfDIPLDv6PortEnable,
       "hpicfDIPLDv6PortOperStatus": hpicfDIPLDv6PortOperStatus,
       "hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl": hpicfDIPLDv6SourceBindingOutOfResourcesTrapCtrl,
       "hpicfDIPLDv6SourceBindingViolationsTrapCtrl": hpicfDIPLDv6SourceBindingViolationsTrapCtrl,
       "hpicfDIPLDv6Status": hpicfDIPLDv6Status,
       "hpicfDIPLDv6AddrTable": hpicfDIPLDv6AddrTable,
       "hpicfDIPLDv6AddrEntry": hpicfDIPLDv6AddrEntry,
       "hpicfDIPLDv6AddrVlan": hpicfDIPLDv6AddrVlan,
       "hpicfDIPLDv6ResourceAvailable": hpicfDIPLDv6ResourceAvailable,
       "hpicfIpv6LockConformance": hpicfIpv6LockConformance,
       "hpicfIpv6LockGroups": hpicfIpv6LockGroups,
       "hpicfIpv6LockBaseGroup": hpicfIpv6LockBaseGroup,
       "hpicfSourceBindingTrapObjectsGroup": hpicfSourceBindingTrapObjectsGroup,
       "hpicfSourceBindingTrapsGroup": hpicfSourceBindingTrapsGroup,
       "hpicfIpv6LockCompliances": hpicfIpv6LockCompliances,
       "hpicfDIPLDv6Compliance": hpicfDIPLDv6Compliance,
       "hpicfIpv6SourceBindingTrapCompliance": hpicfIpv6SourceBindingTrapCompliance}
)
