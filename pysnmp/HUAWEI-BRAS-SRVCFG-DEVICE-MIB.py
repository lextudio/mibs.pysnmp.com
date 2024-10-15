# SNMP MIB module (HUAWEI-BRAS-SRVCFG-DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-SRVCFG-DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:08 2024
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

(hwBRASMib,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwBRASMib")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(mplsVpnVrfName,) = mibBuilder.importSymbols(
    "MPLS-VPN-MIB",
    "mplsVpnVrfName")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwBRASSrvcfgDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSrvcfgDeviceMibObjects_ObjectIdentity = ObjectIdentity
hwSrvcfgDeviceMibObjects = _HwSrvcfgDeviceMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1)
)
_HwDeviceUserTable_Object = MibTable
hwDeviceUserTable = _HwDeviceUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1)
)
if mibBuilder.loadTexts:
    hwDeviceUserTable.setStatus("current")
_HwDeviceUserEntry_Object = MibTableRow
hwDeviceUserEntry = _HwDeviceUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1)
)
hwDeviceUserEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddr"),
)
if mibBuilder.loadTexts:
    hwDeviceUserEntry.setStatus("current")
_HwDeviceUserStartIpAddr_Type = IpAddress
_HwDeviceUserStartIpAddr_Object = MibTableColumn
hwDeviceUserStartIpAddr = _HwDeviceUserStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 1),
    _HwDeviceUserStartIpAddr_Type()
)
hwDeviceUserStartIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceUserStartIpAddr.setStatus("current")
_HwDeviceUserEndIpAddr_Type = IpAddress
_HwDeviceUserEndIpAddr_Object = MibTableColumn
hwDeviceUserEndIpAddr = _HwDeviceUserEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 2),
    _HwDeviceUserEndIpAddr_Type()
)
hwDeviceUserEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserEndIpAddr.setStatus("current")
_HwDeviceUserIfIndex_Type = InterfaceIndex
_HwDeviceUserIfIndex_Object = MibTableColumn
hwDeviceUserIfIndex = _HwDeviceUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 3),
    _HwDeviceUserIfIndex_Type()
)
hwDeviceUserIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserIfIndex.setStatus("current")


class _HwDeviceUserIfName_Type(DisplayString):
    """Custom type hwDeviceUserIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwDeviceUserIfName_Type.__name__ = "DisplayString"
_HwDeviceUserIfName_Object = MibTableColumn
hwDeviceUserIfName = _HwDeviceUserIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 4),
    _HwDeviceUserIfName_Type()
)
hwDeviceUserIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceUserIfName.setStatus("current")


class _HwDeviceUserVlan_Type(Integer32):
    """Custom type hwDeviceUserVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwDeviceUserVlan_Type.__name__ = "Integer32"
_HwDeviceUserVlan_Object = MibTableColumn
hwDeviceUserVlan = _HwDeviceUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 5),
    _HwDeviceUserVlan_Type()
)
hwDeviceUserVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserVlan.setStatus("current")


class _HwDeviceUserVpi_Type(Integer32):
    """Custom type hwDeviceUserVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwDeviceUserVpi_Type.__name__ = "Integer32"
_HwDeviceUserVpi_Object = MibTableColumn
hwDeviceUserVpi = _HwDeviceUserVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 6),
    _HwDeviceUserVpi_Type()
)
hwDeviceUserVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserVpi.setStatus("current")


class _HwDeviceUserVci_Type(Integer32):
    """Custom type hwDeviceUserVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwDeviceUserVci_Type.__name__ = "Integer32"
_HwDeviceUserVci_Object = MibTableColumn
hwDeviceUserVci = _HwDeviceUserVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 7),
    _HwDeviceUserVci_Type()
)
hwDeviceUserVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserVci.setStatus("current")
_HwDeviceUserMac_Type = MacAddress
_HwDeviceUserMac_Object = MibTableColumn
hwDeviceUserMac = _HwDeviceUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 8),
    _HwDeviceUserMac_Type()
)
hwDeviceUserMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserMac.setStatus("current")


class _HwDeviceUserDomain_Type(DisplayString):
    """Custom type hwDeviceUserDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HwDeviceUserDomain_Type.__name__ = "DisplayString"
_HwDeviceUserDomain_Object = MibTableColumn
hwDeviceUserDomain = _HwDeviceUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 9),
    _HwDeviceUserDomain_Type()
)
hwDeviceUserDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserDomain.setStatus("current")


class _HwDeviceUserStatus_Type(Integer32):
    """Custom type hwDeviceUserStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleting", 2),
          ("detecting", 1),
          ("online", 3),
          ("ready", 0))
    )


_HwDeviceUserStatus_Type.__name__ = "Integer32"
_HwDeviceUserStatus_Object = MibTableColumn
hwDeviceUserStatus = _HwDeviceUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 10),
    _HwDeviceUserStatus_Type()
)
hwDeviceUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceUserStatus.setStatus("current")
_HwDeviceUserRowStatus_Type = RowStatus
_HwDeviceUserRowStatus_Object = MibTableColumn
hwDeviceUserRowStatus = _HwDeviceUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 11),
    _HwDeviceUserRowStatus_Type()
)
hwDeviceUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDeviceUserRowStatus.setStatus("current")


class _HwDeviceQinQUserVlan_Type(Integer32):
    """Custom type hwDeviceQinQUserVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwDeviceQinQUserVlan_Type.__name__ = "Integer32"
_HwDeviceQinQUserVlan_Object = MibTableColumn
hwDeviceQinQUserVlan = _HwDeviceQinQUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 1, 1, 12),
    _HwDeviceQinQUserVlan_Type()
)
hwDeviceQinQUserVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceQinQUserVlan.setStatus("current")
_HwDeviceUserTableV2_Object = MibTable
hwDeviceUserTableV2 = _HwDeviceUserTableV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2)
)
if mibBuilder.loadTexts:
    hwDeviceUserTableV2.setStatus("current")
_HwDeviceUserEntryV2_Object = MibTableRow
hwDeviceUserEntryV2 = _HwDeviceUserEntryV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1)
)
hwDeviceUserEntryV2.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVrfNameV2"),
    (0, "HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddrV2"),
)
if mibBuilder.loadTexts:
    hwDeviceUserEntryV2.setStatus("current")
_HwDeviceUserStartIpAddrV2_Type = IpAddress
_HwDeviceUserStartIpAddrV2_Object = MibTableColumn
hwDeviceUserStartIpAddrV2 = _HwDeviceUserStartIpAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 1),
    _HwDeviceUserStartIpAddrV2_Type()
)
hwDeviceUserStartIpAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceUserStartIpAddrV2.setStatus("current")
_HwDeviceUserEndIpAddrV2_Type = IpAddress
_HwDeviceUserEndIpAddrV2_Object = MibTableColumn
hwDeviceUserEndIpAddrV2 = _HwDeviceUserEndIpAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 2),
    _HwDeviceUserEndIpAddrV2_Type()
)
hwDeviceUserEndIpAddrV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserEndIpAddrV2.setStatus("current")
_HwDeviceUserIfIndexV2_Type = InterfaceIndex
_HwDeviceUserIfIndexV2_Object = MibTableColumn
hwDeviceUserIfIndexV2 = _HwDeviceUserIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 3),
    _HwDeviceUserIfIndexV2_Type()
)
hwDeviceUserIfIndexV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserIfIndexV2.setStatus("current")


class _HwDeviceUserIfNameV2_Type(DisplayString):
    """Custom type hwDeviceUserIfNameV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HwDeviceUserIfNameV2_Type.__name__ = "DisplayString"
_HwDeviceUserIfNameV2_Object = MibTableColumn
hwDeviceUserIfNameV2 = _HwDeviceUserIfNameV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 4),
    _HwDeviceUserIfNameV2_Type()
)
hwDeviceUserIfNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceUserIfNameV2.setStatus("current")


class _HwDeviceUserVlanV2_Type(Integer32):
    """Custom type hwDeviceUserVlanV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwDeviceUserVlanV2_Type.__name__ = "Integer32"
_HwDeviceUserVlanV2_Object = MibTableColumn
hwDeviceUserVlanV2 = _HwDeviceUserVlanV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 5),
    _HwDeviceUserVlanV2_Type()
)
hwDeviceUserVlanV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserVlanV2.setStatus("current")


class _HwDeviceUserVpiV2_Type(Integer32):
    """Custom type hwDeviceUserVpiV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwDeviceUserVpiV2_Type.__name__ = "Integer32"
_HwDeviceUserVpiV2_Object = MibTableColumn
hwDeviceUserVpiV2 = _HwDeviceUserVpiV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 6),
    _HwDeviceUserVpiV2_Type()
)
hwDeviceUserVpiV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserVpiV2.setStatus("current")


class _HwDeviceUserVciV2_Type(Integer32):
    """Custom type hwDeviceUserVciV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwDeviceUserVciV2_Type.__name__ = "Integer32"
_HwDeviceUserVciV2_Object = MibTableColumn
hwDeviceUserVciV2 = _HwDeviceUserVciV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 7),
    _HwDeviceUserVciV2_Type()
)
hwDeviceUserVciV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserVciV2.setStatus("current")
_HwDeviceUserMacV2_Type = MacAddress
_HwDeviceUserMacV2_Object = MibTableColumn
hwDeviceUserMacV2 = _HwDeviceUserMacV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 8),
    _HwDeviceUserMacV2_Type()
)
hwDeviceUserMacV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserMacV2.setStatus("current")


class _HwDeviceUserDomainV2_Type(DisplayString):
    """Custom type hwDeviceUserDomainV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwDeviceUserDomainV2_Type.__name__ = "DisplayString"
_HwDeviceUserDomainV2_Object = MibTableColumn
hwDeviceUserDomainV2 = _HwDeviceUserDomainV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 9),
    _HwDeviceUserDomainV2_Type()
)
hwDeviceUserDomainV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceUserDomainV2.setStatus("current")


class _HwDeviceUserStatusV2_Type(Integer32):
    """Custom type hwDeviceUserStatusV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deleting", 2),
          ("detecting", 1),
          ("online", 3),
          ("ready", 0))
    )


_HwDeviceUserStatusV2_Type.__name__ = "Integer32"
_HwDeviceUserStatusV2_Object = MibTableColumn
hwDeviceUserStatusV2 = _HwDeviceUserStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 10),
    _HwDeviceUserStatusV2_Type()
)
hwDeviceUserStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceUserStatusV2.setStatus("current")
_HwDeviceUserRowStatusV2_Type = RowStatus
_HwDeviceUserRowStatusV2_Object = MibTableColumn
hwDeviceUserRowStatusV2 = _HwDeviceUserRowStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 11),
    _HwDeviceUserRowStatusV2_Type()
)
hwDeviceUserRowStatusV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDeviceUserRowStatusV2.setStatus("current")


class _HwDeviceQinQUserVlanV2_Type(Integer32):
    """Custom type hwDeviceQinQUserVlanV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwDeviceQinQUserVlanV2_Type.__name__ = "Integer32"
_HwDeviceQinQUserVlanV2_Object = MibTableColumn
hwDeviceQinQUserVlanV2 = _HwDeviceQinQUserVlanV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 12),
    _HwDeviceQinQUserVlanV2_Type()
)
hwDeviceQinQUserVlanV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwDeviceQinQUserVlanV2.setStatus("current")


class _HwDeviceUserVrfNameV2_Type(DisplayString):
    """Custom type hwDeviceUserVrfNameV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwDeviceUserVrfNameV2_Type.__name__ = "DisplayString"
_HwDeviceUserVrfNameV2_Object = MibTableColumn
hwDeviceUserVrfNameV2 = _HwDeviceUserVrfNameV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 1, 2, 1, 13),
    _HwDeviceUserVrfNameV2_Type()
)
hwDeviceUserVrfNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDeviceUserVrfNameV2.setStatus("current")
_HwSrvcfgDeviceConformance_ObjectIdentity = ObjectIdentity
hwSrvcfgDeviceConformance = _HwSrvcfgDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2)
)
_HwSrvcfgDeviceCompliances_ObjectIdentity = ObjectIdentity
hwSrvcfgDeviceCompliances = _HwSrvcfgDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 1)
)
_HwDeviceUserGroups_ObjectIdentity = ObjectIdentity
hwDeviceUserGroups = _HwDeviceUserGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 2)
)

# Managed Objects groups

hwDeviceUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 2, 1)
)
hwDeviceUserGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddr"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserEndIpAddr"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfIndex"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfName"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVlan"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVpi"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVci"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserMac"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserDomain"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStatus"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserRowStatus"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceQinQUserVlan"))
)
if mibBuilder.loadTexts:
    hwDeviceUserGroup.setStatus("current")

hwDeviceUserV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 2, 2)
)
hwDeviceUserV2Group.setObjects(
      *(("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStartIpAddrV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserEndIpAddrV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfIndexV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserIfNameV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVlanV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVpiV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVciV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserMacV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserDomainV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserStatusV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserRowStatusV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceQinQUserVlanV2"),
        ("HUAWEI-BRAS-SRVCFG-DEVICE-MIB", "hwDeviceUserVrfNameV2"))
)
if mibBuilder.loadTexts:
    hwDeviceUserV2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwSrvcfgDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 6, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwSrvcfgDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-SRVCFG-DEVICE-MIB",
    **{"hwBRASSrvcfgDevice": hwBRASSrvcfgDevice,
       "hwSrvcfgDeviceMibObjects": hwSrvcfgDeviceMibObjects,
       "hwDeviceUserTable": hwDeviceUserTable,
       "hwDeviceUserEntry": hwDeviceUserEntry,
       "hwDeviceUserStartIpAddr": hwDeviceUserStartIpAddr,
       "hwDeviceUserEndIpAddr": hwDeviceUserEndIpAddr,
       "hwDeviceUserIfIndex": hwDeviceUserIfIndex,
       "hwDeviceUserIfName": hwDeviceUserIfName,
       "hwDeviceUserVlan": hwDeviceUserVlan,
       "hwDeviceUserVpi": hwDeviceUserVpi,
       "hwDeviceUserVci": hwDeviceUserVci,
       "hwDeviceUserMac": hwDeviceUserMac,
       "hwDeviceUserDomain": hwDeviceUserDomain,
       "hwDeviceUserStatus": hwDeviceUserStatus,
       "hwDeviceUserRowStatus": hwDeviceUserRowStatus,
       "hwDeviceQinQUserVlan": hwDeviceQinQUserVlan,
       "hwDeviceUserTableV2": hwDeviceUserTableV2,
       "hwDeviceUserEntryV2": hwDeviceUserEntryV2,
       "hwDeviceUserStartIpAddrV2": hwDeviceUserStartIpAddrV2,
       "hwDeviceUserEndIpAddrV2": hwDeviceUserEndIpAddrV2,
       "hwDeviceUserIfIndexV2": hwDeviceUserIfIndexV2,
       "hwDeviceUserIfNameV2": hwDeviceUserIfNameV2,
       "hwDeviceUserVlanV2": hwDeviceUserVlanV2,
       "hwDeviceUserVpiV2": hwDeviceUserVpiV2,
       "hwDeviceUserVciV2": hwDeviceUserVciV2,
       "hwDeviceUserMacV2": hwDeviceUserMacV2,
       "hwDeviceUserDomainV2": hwDeviceUserDomainV2,
       "hwDeviceUserStatusV2": hwDeviceUserStatusV2,
       "hwDeviceUserRowStatusV2": hwDeviceUserRowStatusV2,
       "hwDeviceQinQUserVlanV2": hwDeviceQinQUserVlanV2,
       "hwDeviceUserVrfNameV2": hwDeviceUserVrfNameV2,
       "hwSrvcfgDeviceConformance": hwSrvcfgDeviceConformance,
       "hwSrvcfgDeviceCompliances": hwSrvcfgDeviceCompliances,
       "hwSrvcfgDeviceCompliance": hwSrvcfgDeviceCompliance,
       "hwDeviceUserGroups": hwDeviceUserGroups,
       "hwDeviceUserGroup": hwDeviceUserGroup,
       "hwDeviceUserV2Group": hwDeviceUserV2Group}
)
