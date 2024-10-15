# SNMP MIB module (HUAWEI-BRAS-SRVCFG-STATICUSER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BRAS-SRVCFG-STATICUSER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:11 2024
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

hwBRASSrvcfgStaticUser = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5)
)
hwBRASSrvcfgStaticUser.setRevisions(
        ("2013-06-26 16:08",
         "2009-08-09 18:50")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSrvcfgStaticUserMibObjects_ObjectIdentity = ObjectIdentity
hwSrvcfgStaticUserMibObjects = _HwSrvcfgStaticUserMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1)
)
_HwStaticUserTable_Object = MibTable
hwStaticUserTable = _HwStaticUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwStaticUserTable.setStatus("current")
_HwStaticUserEntry_Object = MibTableRow
hwStaticUserEntry = _HwStaticUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1)
)
hwStaticUserEntry.setIndexNames(
    (0, "MPLS-VPN-MIB", "mplsVpnVrfName"),
    (0, "HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddr"),
)
if mibBuilder.loadTexts:
    hwStaticUserEntry.setStatus("current")
_HwStaticUserStartIpAddr_Type = IpAddress
_HwStaticUserStartIpAddr_Object = MibTableColumn
hwStaticUserStartIpAddr = _HwStaticUserStartIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 1),
    _HwStaticUserStartIpAddr_Type()
)
hwStaticUserStartIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticUserStartIpAddr.setStatus("current")
_HwStaticUserEndIpAddr_Type = IpAddress
_HwStaticUserEndIpAddr_Object = MibTableColumn
hwStaticUserEndIpAddr = _HwStaticUserEndIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 2),
    _HwStaticUserEndIpAddr_Type()
)
hwStaticUserEndIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserEndIpAddr.setStatus("current")
_HwStaticUserIfIndex_Type = InterfaceIndex
_HwStaticUserIfIndex_Object = MibTableColumn
hwStaticUserIfIndex = _HwStaticUserIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 3),
    _HwStaticUserIfIndex_Type()
)
hwStaticUserIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserIfIndex.setStatus("current")


class _HwStaticUserVlan_Type(Integer32):
    """Custom type hwStaticUserVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwStaticUserVlan_Type.__name__ = "Integer32"
_HwStaticUserVlan_Object = MibTableColumn
hwStaticUserVlan = _HwStaticUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 4),
    _HwStaticUserVlan_Type()
)
hwStaticUserVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserVlan.setStatus("current")


class _HwStaticUserVpi_Type(Integer32):
    """Custom type hwStaticUserVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwStaticUserVpi_Type.__name__ = "Integer32"
_HwStaticUserVpi_Object = MibTableColumn
hwStaticUserVpi = _HwStaticUserVpi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 5),
    _HwStaticUserVpi_Type()
)
hwStaticUserVpi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserVpi.setStatus("current")


class _HwStaticUserVci_Type(Integer32):
    """Custom type hwStaticUserVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwStaticUserVci_Type.__name__ = "Integer32"
_HwStaticUserVci_Object = MibTableColumn
hwStaticUserVci = _HwStaticUserVci_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 6),
    _HwStaticUserVci_Type()
)
hwStaticUserVci.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserVci.setStatus("current")
_HwStaticUserMac_Type = MacAddress
_HwStaticUserMac_Object = MibTableColumn
hwStaticUserMac = _HwStaticUserMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 7),
    _HwStaticUserMac_Type()
)
hwStaticUserMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserMac.setStatus("current")


class _HwStaticUserDomain_Type(DisplayString):
    """Custom type hwStaticUserDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HwStaticUserDomain_Type.__name__ = "DisplayString"
_HwStaticUserDomain_Object = MibTableColumn
hwStaticUserDomain = _HwStaticUserDomain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 8),
    _HwStaticUserDomain_Type()
)
hwStaticUserDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserDomain.setStatus("current")


class _HwStaticUserDetect_Type(TruthValue):
    """Custom type hwStaticUserDetect based on TruthValue"""


_HwStaticUserDetect_Object = MibTableColumn
hwStaticUserDetect = _HwStaticUserDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 9),
    _HwStaticUserDetect_Type()
)
hwStaticUserDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserDetect.setStatus("current")
_HwStaticUserRowStatus_Type = RowStatus
_HwStaticUserRowStatus_Object = MibTableColumn
hwStaticUserRowStatus = _HwStaticUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 10),
    _HwStaticUserRowStatus_Type()
)
hwStaticUserRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaticUserRowStatus.setStatus("current")


class _HwStaticUserStatus_Type(Integer32):
    """Custom type hwStaticUserStatus based on Integer32"""
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


_HwStaticUserStatus_Type.__name__ = "Integer32"
_HwStaticUserStatus_Object = MibTableColumn
hwStaticUserStatus = _HwStaticUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 11),
    _HwStaticUserStatus_Type()
)
hwStaticUserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticUserStatus.setStatus("current")


class _HwStaticUserQinQVlan_Type(Integer32):
    """Custom type hwStaticUserQinQVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwStaticUserQinQVlan_Type.__name__ = "Integer32"
_HwStaticUserQinQVlan_Object = MibTableColumn
hwStaticUserQinQVlan = _HwStaticUserQinQVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 12),
    _HwStaticUserQinQVlan_Type()
)
hwStaticUserQinQVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserQinQVlan.setStatus("current")


class _HwStaticUserDescription_Type(DisplayString):
    """Custom type hwStaticUserDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwStaticUserDescription_Type.__name__ = "DisplayString"
_HwStaticUserDescription_Object = MibTableColumn
hwStaticUserDescription = _HwStaticUserDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 13),
    _HwStaticUserDescription_Type()
)
hwStaticUserDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserDescription.setStatus("current")
_HwStaticUserGatewayIpAddr_Type = IpAddress
_HwStaticUserGatewayIpAddr_Object = MibTableColumn
hwStaticUserGatewayIpAddr = _HwStaticUserGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 14),
    _HwStaticUserGatewayIpAddr_Type()
)
hwStaticUserGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserGatewayIpAddr.setStatus("current")
_HwStaticUserVrfName_Type = DisplayString
_HwStaticUserVrfName_Object = MibTableColumn
hwStaticUserVrfName = _HwStaticUserVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 1, 1, 15),
    _HwStaticUserVrfName_Type()
)
hwStaticUserVrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserVrfName.setStatus("current")
_HwStaticUserV2Table_Object = MibTable
hwStaticUserV2Table = _HwStaticUserV2Table_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2)
)
if mibBuilder.loadTexts:
    hwStaticUserV2Table.setStatus("current")
_HwStaticUserV2Entry_Object = MibTableRow
hwStaticUserV2Entry = _HwStaticUserV2Entry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1)
)
hwStaticUserV2Entry.setIndexNames(
    (0, "HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVrfNameV2"),
    (0, "HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddrV2"),
)
if mibBuilder.loadTexts:
    hwStaticUserV2Entry.setStatus("current")
_HwStaticUserStartIpAddrV2_Type = IpAddress
_HwStaticUserStartIpAddrV2_Object = MibTableColumn
hwStaticUserStartIpAddrV2 = _HwStaticUserStartIpAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 1),
    _HwStaticUserStartIpAddrV2_Type()
)
hwStaticUserStartIpAddrV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticUserStartIpAddrV2.setStatus("current")
_HwStaticUserEndIpAddrV2_Type = IpAddress
_HwStaticUserEndIpAddrV2_Object = MibTableColumn
hwStaticUserEndIpAddrV2 = _HwStaticUserEndIpAddrV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 2),
    _HwStaticUserEndIpAddrV2_Type()
)
hwStaticUserEndIpAddrV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserEndIpAddrV2.setStatus("current")
_HwStaticUserIfIndexV2_Type = InterfaceIndex
_HwStaticUserIfIndexV2_Object = MibTableColumn
hwStaticUserIfIndexV2 = _HwStaticUserIfIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 3),
    _HwStaticUserIfIndexV2_Type()
)
hwStaticUserIfIndexV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserIfIndexV2.setStatus("current")


class _HwStaticUserVlanV2_Type(Integer32):
    """Custom type hwStaticUserVlanV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwStaticUserVlanV2_Type.__name__ = "Integer32"
_HwStaticUserVlanV2_Object = MibTableColumn
hwStaticUserVlanV2 = _HwStaticUserVlanV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 4),
    _HwStaticUserVlanV2_Type()
)
hwStaticUserVlanV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserVlanV2.setStatus("current")


class _HwStaticUserVpiV2_Type(Integer32):
    """Custom type hwStaticUserVpiV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwStaticUserVpiV2_Type.__name__ = "Integer32"
_HwStaticUserVpiV2_Object = MibTableColumn
hwStaticUserVpiV2 = _HwStaticUserVpiV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 5),
    _HwStaticUserVpiV2_Type()
)
hwStaticUserVpiV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserVpiV2.setStatus("current")


class _HwStaticUserVciV2_Type(Integer32):
    """Custom type hwStaticUserVciV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_HwStaticUserVciV2_Type.__name__ = "Integer32"
_HwStaticUserVciV2_Object = MibTableColumn
hwStaticUserVciV2 = _HwStaticUserVciV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 6),
    _HwStaticUserVciV2_Type()
)
hwStaticUserVciV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserVciV2.setStatus("current")
_HwStaticUserMacV2_Type = MacAddress
_HwStaticUserMacV2_Object = MibTableColumn
hwStaticUserMacV2 = _HwStaticUserMacV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 7),
    _HwStaticUserMacV2_Type()
)
hwStaticUserMacV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserMacV2.setStatus("current")


class _HwStaticUserDomainV2_Type(DisplayString):
    """Custom type hwStaticUserDomainV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwStaticUserDomainV2_Type.__name__ = "DisplayString"
_HwStaticUserDomainV2_Object = MibTableColumn
hwStaticUserDomainV2 = _HwStaticUserDomainV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 8),
    _HwStaticUserDomainV2_Type()
)
hwStaticUserDomainV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserDomainV2.setStatus("current")


class _HwStaticUserDetectV2_Type(TruthValue):
    """Custom type hwStaticUserDetectV2 based on TruthValue"""


_HwStaticUserDetectV2_Object = MibTableColumn
hwStaticUserDetectV2 = _HwStaticUserDetectV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 9),
    _HwStaticUserDetectV2_Type()
)
hwStaticUserDetectV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserDetectV2.setStatus("current")
_HwStaticUserRowStatusV2_Type = RowStatus
_HwStaticUserRowStatusV2_Object = MibTableColumn
hwStaticUserRowStatusV2 = _HwStaticUserRowStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 10),
    _HwStaticUserRowStatusV2_Type()
)
hwStaticUserRowStatusV2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaticUserRowStatusV2.setStatus("current")


class _HwStaticUserStatusV2_Type(Integer32):
    """Custom type hwStaticUserStatusV2 based on Integer32"""
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


_HwStaticUserStatusV2_Type.__name__ = "Integer32"
_HwStaticUserStatusV2_Object = MibTableColumn
hwStaticUserStatusV2 = _HwStaticUserStatusV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 11),
    _HwStaticUserStatusV2_Type()
)
hwStaticUserStatusV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticUserStatusV2.setStatus("current")


class _HwStaticUserQinQVlanV2_Type(Integer32):
    """Custom type hwStaticUserQinQVlanV2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwStaticUserQinQVlanV2_Type.__name__ = "Integer32"
_HwStaticUserQinQVlanV2_Object = MibTableColumn
hwStaticUserQinQVlanV2 = _HwStaticUserQinQVlanV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 12),
    _HwStaticUserQinQVlanV2_Type()
)
hwStaticUserQinQVlanV2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaticUserQinQVlanV2.setStatus("current")


class _HwStaticUserVrfNameV2_Type(DisplayString):
    """Custom type hwStaticUserVrfNameV2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwStaticUserVrfNameV2_Type.__name__ = "DisplayString"
_HwStaticUserVrfNameV2_Object = MibTableColumn
hwStaticUserVrfNameV2 = _HwStaticUserVrfNameV2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 2, 1, 13),
    _HwStaticUserVrfNameV2_Type()
)
hwStaticUserVrfNameV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaticUserVrfNameV2.setStatus("current")


class _HwStaticUserPassowrd_Type(OctetString):
    """Custom type hwStaticUserPassowrd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
        ValueSizeConstraint(32, 32),
    )


_HwStaticUserPassowrd_Type.__name__ = "OctetString"
_HwStaticUserPassowrd_Object = MibScalar
hwStaticUserPassowrd = _HwStaticUserPassowrd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 3),
    _HwStaticUserPassowrd_Type()
)
hwStaticUserPassowrd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaticUserPassowrd.setStatus("current")


class _HwStaticUserUserNameFormatInclude_Type(Integer32):
    """Custom type hwStaticUserUserNameFormatInclude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("ipaddress", 2),
          ("macaddress", 3),
          ("sysname", 4))
    )


_HwStaticUserUserNameFormatInclude_Type.__name__ = "Integer32"
_HwStaticUserUserNameFormatInclude_Object = MibScalar
hwStaticUserUserNameFormatInclude = _HwStaticUserUserNameFormatInclude_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 1, 4),
    _HwStaticUserUserNameFormatInclude_Type()
)
hwStaticUserUserNameFormatInclude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaticUserUserNameFormatInclude.setStatus("current")
_HwStaticUserConformance_ObjectIdentity = ObjectIdentity
hwStaticUserConformance = _HwStaticUserConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2)
)
_HwStaticUserCompliances_ObjectIdentity = ObjectIdentity
hwStaticUserCompliances = _HwStaticUserCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1)
)
_HwStaticUserObjectGroups_ObjectIdentity = ObjectIdentity
hwStaticUserObjectGroups = _HwStaticUserObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 2)
)

# Managed Objects groups

hwStaticUserTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 2, 1)
)
hwStaticUserTableGroup.setObjects(
      *(("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddr"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserEndIpAddr"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserIfIndex"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVlan"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVpi"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVci"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserMac"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDomain"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDetect"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserRowStatus"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStatus"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserQinQVlan"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDescription"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserGatewayIpAddr"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVrfName"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserPassowrd"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserUserNameFormatInclude"))
)
if mibBuilder.loadTexts:
    hwStaticUserTableGroup.setStatus("current")

hwStaticUserTableV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 2, 2)
)
hwStaticUserTableV2Group.setObjects(
      *(("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStartIpAddrV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserEndIpAddrV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserIfIndexV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVlanV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVpiV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVciV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserMacV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDomainV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserDetectV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserRowStatusV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserStatusV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserQinQVlanV2"),
        ("HUAWEI-BRAS-SRVCFG-STATICUSER-MIB", "hwStaticUserVrfNameV2"))
)
if mibBuilder.loadTexts:
    hwStaticUserTableV2Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwStaticUserCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 40, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwStaticUserCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BRAS-SRVCFG-STATICUSER-MIB",
    **{"hwBRASSrvcfgStaticUser": hwBRASSrvcfgStaticUser,
       "hwSrvcfgStaticUserMibObjects": hwSrvcfgStaticUserMibObjects,
       "hwStaticUserTable": hwStaticUserTable,
       "hwStaticUserEntry": hwStaticUserEntry,
       "hwStaticUserStartIpAddr": hwStaticUserStartIpAddr,
       "hwStaticUserEndIpAddr": hwStaticUserEndIpAddr,
       "hwStaticUserIfIndex": hwStaticUserIfIndex,
       "hwStaticUserVlan": hwStaticUserVlan,
       "hwStaticUserVpi": hwStaticUserVpi,
       "hwStaticUserVci": hwStaticUserVci,
       "hwStaticUserMac": hwStaticUserMac,
       "hwStaticUserDomain": hwStaticUserDomain,
       "hwStaticUserDetect": hwStaticUserDetect,
       "hwStaticUserRowStatus": hwStaticUserRowStatus,
       "hwStaticUserStatus": hwStaticUserStatus,
       "hwStaticUserQinQVlan": hwStaticUserQinQVlan,
       "hwStaticUserDescription": hwStaticUserDescription,
       "hwStaticUserGatewayIpAddr": hwStaticUserGatewayIpAddr,
       "hwStaticUserVrfName": hwStaticUserVrfName,
       "hwStaticUserV2Table": hwStaticUserV2Table,
       "hwStaticUserV2Entry": hwStaticUserV2Entry,
       "hwStaticUserStartIpAddrV2": hwStaticUserStartIpAddrV2,
       "hwStaticUserEndIpAddrV2": hwStaticUserEndIpAddrV2,
       "hwStaticUserIfIndexV2": hwStaticUserIfIndexV2,
       "hwStaticUserVlanV2": hwStaticUserVlanV2,
       "hwStaticUserVpiV2": hwStaticUserVpiV2,
       "hwStaticUserVciV2": hwStaticUserVciV2,
       "hwStaticUserMacV2": hwStaticUserMacV2,
       "hwStaticUserDomainV2": hwStaticUserDomainV2,
       "hwStaticUserDetectV2": hwStaticUserDetectV2,
       "hwStaticUserRowStatusV2": hwStaticUserRowStatusV2,
       "hwStaticUserStatusV2": hwStaticUserStatusV2,
       "hwStaticUserQinQVlanV2": hwStaticUserQinQVlanV2,
       "hwStaticUserVrfNameV2": hwStaticUserVrfNameV2,
       "hwStaticUserPassowrd": hwStaticUserPassowrd,
       "hwStaticUserUserNameFormatInclude": hwStaticUserUserNameFormatInclude,
       "hwStaticUserConformance": hwStaticUserConformance,
       "hwStaticUserCompliances": hwStaticUserCompliances,
       "hwStaticUserCompliance": hwStaticUserCompliance,
       "hwStaticUserObjectGroups": hwStaticUserObjectGroups,
       "hwStaticUserTableGroup": hwStaticUserTableGroup,
       "hwStaticUserTableV2Group": hwStaticUserTableV2Group}
)
