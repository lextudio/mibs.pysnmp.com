# SNMP MIB module (HUAWEI-VPN-DIAGNOSTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VPN-DIAGNOSTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:37 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(HWL2VpnVcEncapsType,) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWL2VpnVcEncapsType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

vpndiagnostics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172)
)
vpndiagnostics.setRevisions(
        ("2014-01-18 17:22",
         "2013-12-16 09:58",
         "2013-07-16 16:00",
         "2008-06-06 16:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MacOpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("populate", 1),
          ("purge", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Macoper_ObjectIdentity = ObjectIdentity
macoper = _Macoper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1)
)
_PopulateBase_ObjectIdentity = ObjectIdentity
populateBase = _PopulateBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 1)
)
_HwOamMacPopulateCount_Type = Integer32
_HwOamMacPopulateCount_Object = MibScalar
hwOamMacPopulateCount = _HwOamMacPopulateCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 1, 1),
    _HwOamMacPopulateCount_Type()
)
hwOamMacPopulateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacPopulateCount.setStatus("current")
_HwOamMacPurgeCount_Type = Integer32
_HwOamMacPurgeCount_Object = MibScalar
hwOamMacPurgeCount = _HwOamMacPurgeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 1, 2),
    _HwOamMacPurgeCount_Type()
)
hwOamMacPurgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacPurgeCount.setStatus("current")
_HwOamMacPurgeRegCount_Type = Integer32
_HwOamMacPurgeRegCount_Object = MibScalar
hwOamMacPurgeRegCount = _HwOamMacPurgeRegCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 1, 3),
    _HwOamMacPurgeRegCount_Type()
)
hwOamMacPurgeRegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacPurgeRegCount.setStatus("current")


class _HwOamMacCountReset_Type(Integer32):
    """Custom type hwOamMacCountReset based on Integer32"""
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
        *(("allreset", 4),
          ("populatereset", 1),
          ("purgeregreset", 3),
          ("purgereset", 2))
    )


_HwOamMacCountReset_Type.__name__ = "Integer32"
_HwOamMacCountReset_Object = MibScalar
hwOamMacCountReset = _HwOamMacCountReset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 1, 4),
    _HwOamMacCountReset_Type()
)
hwOamMacCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOamMacCountReset.setStatus("current")


class _HwOamMacSwitch_Type(Integer32):
    """Custom type hwOamMacSwitch based on Integer32"""
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


_HwOamMacSwitch_Type.__name__ = "Integer32"
_HwOamMacSwitch_Object = MibScalar
hwOamMacSwitch = _HwOamMacSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 1, 5),
    _HwOamMacSwitch_Type()
)
hwOamMacSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOamMacSwitch.setStatus("current")
_HwOamMacEntryNum_Type = Integer32
_HwOamMacEntryNum_Object = MibScalar
hwOamMacEntryNum = _HwOamMacEntryNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 1, 6),
    _HwOamMacEntryNum_Type()
)
hwOamMacEntryNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacEntryNum.setStatus("current")
_HwOamMacOperTable_Object = MibTable
hwOamMacOperTable = _HwOamMacOperTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2)
)
if mibBuilder.loadTexts:
    hwOamMacOperTable.setStatus("current")
_HwOamMacOperEntry_Object = MibTableRow
hwOamMacOperEntry = _HwOamMacOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1)
)
hwOamMacOperEntry.setIndexNames(
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperIndex"),
)
if mibBuilder.loadTexts:
    hwOamMacOperEntry.setStatus("current")


class _HwOamMacOperIndex_Type(Integer32):
    """Custom type hwOamMacOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwOamMacOperIndex_Type.__name__ = "Integer32"
_HwOamMacOperIndex_Object = MibTableColumn
hwOamMacOperIndex = _HwOamMacOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 1),
    _HwOamMacOperIndex_Type()
)
hwOamMacOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOamMacOperIndex.setStatus("current")
_HwOamMacOperAddress_Type = MacAddress
_HwOamMacOperAddress_Object = MibTableColumn
hwOamMacOperAddress = _HwOamMacOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 2),
    _HwOamMacOperAddress_Type()
)
hwOamMacOperAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOamMacOperAddress.setStatus("current")


class _HwOamMacOperVsiName_Type(OctetString):
    """Custom type hwOamMacOperVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwOamMacOperVsiName_Type.__name__ = "OctetString"
_HwOamMacOperVsiName_Object = MibTableColumn
hwOamMacOperVsiName = _HwOamMacOperVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 3),
    _HwOamMacOperVsiName_Type()
)
hwOamMacOperVsiName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOamMacOperVsiName.setStatus("current")
_HwOamMacOperType_Type = MacOpType
_HwOamMacOperType_Object = MibTableColumn
hwOamMacOperType = _HwOamMacOperType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 4),
    _HwOamMacOperType_Type()
)
hwOamMacOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOamMacOperType.setStatus("current")


class _HwOamMacOperRegister_Type(EnabledStatus):
    """Custom type hwOamMacOperRegister based on EnabledStatus"""


_HwOamMacOperRegister_Object = MibTableColumn
hwOamMacOperRegister = _HwOamMacOperRegister_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 5),
    _HwOamMacOperRegister_Type()
)
hwOamMacOperRegister.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOamMacOperRegister.setStatus("current")


class _HwOamMacOperFlood_Type(EnabledStatus):
    """Custom type hwOamMacOperFlood based on EnabledStatus"""


_HwOamMacOperFlood_Object = MibTableColumn
hwOamMacOperFlood = _HwOamMacOperFlood_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 6),
    _HwOamMacOperFlood_Type()
)
hwOamMacOperFlood.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOamMacOperFlood.setStatus("current")


class _HwOamMacOperNum_Type(Integer32):
    """Custom type hwOamMacOperNum based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwOamMacOperNum_Type.__name__ = "Integer32"
_HwOamMacOperNum_Object = MibTableColumn
hwOamMacOperNum = _HwOamMacOperNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 7),
    _HwOamMacOperNum_Type()
)
hwOamMacOperNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOamMacOperNum.setStatus("current")
_HwOamMacOperRowStatus_Type = RowStatus
_HwOamMacOperRowStatus_Object = MibTableColumn
hwOamMacOperRowStatus = _HwOamMacOperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 2, 1, 8),
    _HwOamMacOperRowStatus_Type()
)
hwOamMacOperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwOamMacOperRowStatus.setStatus("current")
_HwOamMacListTable_Object = MibTable
hwOamMacListTable = _HwOamMacListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 3)
)
if mibBuilder.loadTexts:
    hwOamMacListTable.setStatus("current")
_HwOamMacListEntry_Object = MibTableRow
hwOamMacListEntry = _HwOamMacListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 3, 1)
)
hwOamMacListEntry.setIndexNames(
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacListIndex"),
)
if mibBuilder.loadTexts:
    hwOamMacListEntry.setStatus("current")


class _HwOamMacListIndex_Type(Integer32):
    """Custom type hwOamMacListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwOamMacListIndex_Type.__name__ = "Integer32"
_HwOamMacListIndex_Object = MibTableColumn
hwOamMacListIndex = _HwOamMacListIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 3, 1, 1),
    _HwOamMacListIndex_Type()
)
hwOamMacListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOamMacListIndex.setStatus("current")
_HwOamMacListAddress_Type = MacAddress
_HwOamMacListAddress_Object = MibTableColumn
hwOamMacListAddress = _HwOamMacListAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 3, 1, 2),
    _HwOamMacListAddress_Type()
)
hwOamMacListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacListAddress.setStatus("current")
_HwOamMacDisplayTable_Object = MibTable
hwOamMacDisplayTable = _HwOamMacDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4)
)
if mibBuilder.loadTexts:
    hwOamMacDisplayTable.setStatus("current")
_HwOamMacDisplayEntry_Object = MibTableRow
hwOamMacDisplayEntry = _HwOamMacDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4, 1)
)
hwOamMacDisplayEntry.setIndexNames(
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacDisplayIndex"),
)
if mibBuilder.loadTexts:
    hwOamMacDisplayEntry.setStatus("current")


class _HwOamMacDisplayIndex_Type(Integer32):
    """Custom type hwOamMacDisplayIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwOamMacDisplayIndex_Type.__name__ = "Integer32"
_HwOamMacDisplayIndex_Object = MibTableColumn
hwOamMacDisplayIndex = _HwOamMacDisplayIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4, 1, 1),
    _HwOamMacDisplayIndex_Type()
)
hwOamMacDisplayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOamMacDisplayIndex.setStatus("current")
_HwOamMacDisplayAddress_Type = MacAddress
_HwOamMacDisplayAddress_Object = MibTableColumn
hwOamMacDisplayAddress = _HwOamMacDisplayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4, 1, 2),
    _HwOamMacDisplayAddress_Type()
)
hwOamMacDisplayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacDisplayAddress.setStatus("current")
_HwOamMacDisplayType_Type = MacOpType
_HwOamMacDisplayType_Object = MibTableColumn
hwOamMacDisplayType = _HwOamMacDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4, 1, 3),
    _HwOamMacDisplayType_Type()
)
hwOamMacDisplayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacDisplayType.setStatus("current")


class _HwOamMacDisplayVsiName_Type(OctetString):
    """Custom type hwOamMacDisplayVsiName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwOamMacDisplayVsiName_Type.__name__ = "OctetString"
_HwOamMacDisplayVsiName_Object = MibTableColumn
hwOamMacDisplayVsiName = _HwOamMacDisplayVsiName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4, 1, 4),
    _HwOamMacDisplayVsiName_Type()
)
hwOamMacDisplayVsiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacDisplayVsiName.setStatus("current")
_HwOamMacDisplayAgeTime_Type = Integer32
_HwOamMacDisplayAgeTime_Object = MibTableColumn
hwOamMacDisplayAgeTime = _HwOamMacDisplayAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4, 1, 5),
    _HwOamMacDisplayAgeTime_Type()
)
hwOamMacDisplayAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacDisplayAgeTime.setStatus("current")
_HwOamMacDisplayLsrId_Type = IpAddress
_HwOamMacDisplayLsrId_Object = MibTableColumn
hwOamMacDisplayLsrId = _HwOamMacDisplayLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 4, 1, 6),
    _HwOamMacDisplayLsrId_Type()
)
hwOamMacDisplayLsrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOamMacDisplayLsrId.setStatus("current")
_MacoperConformance_ObjectIdentity = ObjectIdentity
macoperConformance = _MacoperConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5)
)
_HwOamMacGroup_ObjectIdentity = ObjectIdentity
hwOamMacGroup = _HwOamMacGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5, 1)
)
_MacoperCompliances_ObjectIdentity = ObjectIdentity
macoperCompliances = _MacoperCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5, 2)
)
_HwVpnCfgPing_ObjectIdentity = ObjectIdentity
hwVpnCfgPing = _HwVpnCfgPing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2)
)
_HwVpnCfgPingTable_Object = MibTable
hwVpnCfgPingTable = _HwVpnCfgPingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1)
)
if mibBuilder.loadTexts:
    hwVpnCfgPingTable.setStatus("current")
_HwVpnCfgPingEntry_Object = MibTableRow
hwVpnCfgPingEntry = _HwVpnCfgPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1)
)
hwVpnCfgPingEntry.setIndexNames(
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingIndex"),
)
if mibBuilder.loadTexts:
    hwVpnCfgPingEntry.setStatus("current")


class _HwVpnCfgPingIndex_Type(Integer32):
    """Custom type hwVpnCfgPingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwVpnCfgPingIndex_Type.__name__ = "Integer32"
_HwVpnCfgPingIndex_Object = MibTableColumn
hwVpnCfgPingIndex = _HwVpnCfgPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 1),
    _HwVpnCfgPingIndex_Type()
)
hwVpnCfgPingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVpnCfgPingIndex.setStatus("current")
_HwVpnCfgPingPeerIpType_Type = InetAddressType
_HwVpnCfgPingPeerIpType_Object = MibTableColumn
hwVpnCfgPingPeerIpType = _HwVpnCfgPingPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 2),
    _HwVpnCfgPingPeerIpType_Type()
)
hwVpnCfgPingPeerIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingPeerIpType.setStatus("current")
_HwVpnCfgPingPeerIp_Type = InetAddress
_HwVpnCfgPingPeerIp_Object = MibTableColumn
hwVpnCfgPingPeerIp = _HwVpnCfgPingPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 3),
    _HwVpnCfgPingPeerIp_Type()
)
hwVpnCfgPingPeerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingPeerIp.setStatus("current")


class _HwVpnCfgPingVpnIdType_Type(Integer32):
    """Custom type hwVpnCfgPingVpnIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bgpadVPLS", 6),
          ("kompellaVPLS", 2),
          ("l3vpn", 3),
          ("martiniVLL", 5),
          ("martiniVPLS", 1),
          ("pwe3", 4),
          ("unknown", 255))
    )


_HwVpnCfgPingVpnIdType_Type.__name__ = "Integer32"
_HwVpnCfgPingVpnIdType_Object = MibTableColumn
hwVpnCfgPingVpnIdType = _HwVpnCfgPingVpnIdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 4),
    _HwVpnCfgPingVpnIdType_Type()
)
hwVpnCfgPingVpnIdType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingVpnIdType.setStatus("current")
_HwVpnCfgPingVpnId_Type = OctetString
_HwVpnCfgPingVpnId_Object = MibTableColumn
hwVpnCfgPingVpnId = _HwVpnCfgPingVpnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 5),
    _HwVpnCfgPingVpnId_Type()
)
hwVpnCfgPingVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingVpnId.setStatus("current")
_HwVpnCfgPingPwId_Type = Integer32
_HwVpnCfgPingPwId_Object = MibTableColumn
hwVpnCfgPingPwId = _HwVpnCfgPingPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 6),
    _HwVpnCfgPingPwId_Type()
)
hwVpnCfgPingPwId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingPwId.setStatus("current")


class _HwVpnCfgPingTunnelUsed_Type(Integer32):
    """Custom type hwVpnCfgPingTunnelUsed based on Integer32"""
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
        *(("localAndRemote", 4),
          ("localOnly", 2),
          ("normal", 1),
          ("remoteOnly", 3))
    )


_HwVpnCfgPingTunnelUsed_Type.__name__ = "Integer32"
_HwVpnCfgPingTunnelUsed_Object = MibTableColumn
hwVpnCfgPingTunnelUsed = _HwVpnCfgPingTunnelUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 7),
    _HwVpnCfgPingTunnelUsed_Type()
)
hwVpnCfgPingTunnelUsed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingTunnelUsed.setStatus("current")
_HwVpnCfgPingOperation_Type = EnabledStatus
_HwVpnCfgPingOperation_Object = MibTableColumn
hwVpnCfgPingOperation = _HwVpnCfgPingOperation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 8),
    _HwVpnCfgPingOperation_Type()
)
hwVpnCfgPingOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingOperation.setStatus("current")


class _HwVpnCfgPingResultDetail_Type(Integer32):
    """Custom type hwVpnCfgPingResultDetail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noResult", 255),
          ("requestFailedReplyFailed", 3),
          ("requestSentReplyRecieved", 1),
          ("requestSentReplyTimeout", 2))
    )


_HwVpnCfgPingResultDetail_Type.__name__ = "Integer32"
_HwVpnCfgPingResultDetail_Object = MibTableColumn
hwVpnCfgPingResultDetail = _HwVpnCfgPingResultDetail_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 9),
    _HwVpnCfgPingResultDetail_Type()
)
hwVpnCfgPingResultDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultDetail.setStatus("current")
_HwVpnCfgPingRowStatus_Type = RowStatus
_HwVpnCfgPingRowStatus_Object = MibTableColumn
hwVpnCfgPingRowStatus = _HwVpnCfgPingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 10),
    _HwVpnCfgPingRowStatus_Type()
)
hwVpnCfgPingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingRowStatus.setStatus("current")


class _HwVpnCfgPingSecondary_Type(Integer32):
    """Custom type hwVpnCfgPingSecondary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1),
          ("unknown", 255))
    )


_HwVpnCfgPingSecondary_Type.__name__ = "Integer32"
_HwVpnCfgPingSecondary_Object = MibTableColumn
hwVpnCfgPingSecondary = _HwVpnCfgPingSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 11),
    _HwVpnCfgPingSecondary_Type()
)
hwVpnCfgPingSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingSecondary.setStatus("current")
_HwVpnCfgPingIfName_Type = DisplayString
_HwVpnCfgPingIfName_Object = MibTableColumn
hwVpnCfgPingIfName = _HwVpnCfgPingIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 12),
    _HwVpnCfgPingIfName_Type()
)
hwVpnCfgPingIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingIfName.setStatus("current")
_HwVpnCfgPingPwIdNew_Type = Unsigned32
_HwVpnCfgPingPwIdNew_Object = MibTableColumn
hwVpnCfgPingPwIdNew = _HwVpnCfgPingPwIdNew_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 1, 1, 13),
    _HwVpnCfgPingPwIdNew_Type()
)
hwVpnCfgPingPwIdNew.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwVpnCfgPingPwIdNew.setStatus("current")
_HwVpnCfgPingResultTable_Object = MibTable
hwVpnCfgPingResultTable = _HwVpnCfgPingResultTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2)
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultTable.setStatus("current")
_HwVpnCfgPingResultEntry_Object = MibTableRow
hwVpnCfgPingResultEntry = _HwVpnCfgPingResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1)
)
hwVpnCfgPingResultEntry.setIndexNames(
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingIndex"),
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultLocation"),
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultEntry.setStatus("current")


class _HwVpnCfgPingResultLocation_Type(Integer32):
    """Custom type hwVpnCfgPingResultLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_HwVpnCfgPingResultLocation_Type.__name__ = "Integer32"
_HwVpnCfgPingResultLocation_Object = MibTableColumn
hwVpnCfgPingResultLocation = _HwVpnCfgPingResultLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 1),
    _HwVpnCfgPingResultLocation_Type()
)
hwVpnCfgPingResultLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultLocation.setStatus("current")


class _HwVpnCfgPingResultVpnIdType_Type(Integer32):
    """Custom type hwVpnCfgPingResultVpnIdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bgpadVPLS", 6),
          ("kompellaVPLS", 2),
          ("l3vpn", 3),
          ("martiniVLL", 5),
          ("martiniVPLS", 1),
          ("pwe3", 4),
          ("unknown", 255))
    )


_HwVpnCfgPingResultVpnIdType_Type.__name__ = "Integer32"
_HwVpnCfgPingResultVpnIdType_Object = MibTableColumn
hwVpnCfgPingResultVpnIdType = _HwVpnCfgPingResultVpnIdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 2),
    _HwVpnCfgPingResultVpnIdType_Type()
)
hwVpnCfgPingResultVpnIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultVpnIdType.setStatus("current")
_HwVpnCfgPingResultVpnId_Type = DisplayString
_HwVpnCfgPingResultVpnId_Object = MibTableColumn
hwVpnCfgPingResultVpnId = _HwVpnCfgPingResultVpnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 3),
    _HwVpnCfgPingResultVpnId_Type()
)
hwVpnCfgPingResultVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultVpnId.setStatus("current")
_HwVpnCfgPingResultDesc_Type = DisplayString
_HwVpnCfgPingResultDesc_Object = MibTableColumn
hwVpnCfgPingResultDesc = _HwVpnCfgPingResultDesc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 4),
    _HwVpnCfgPingResultDesc_Type()
)
hwVpnCfgPingResultDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultDesc.setStatus("current")


class _HwVpnCfgPingResultVpnAdminStatus_Type(Integer32):
    """Custom type hwVpnCfgPingResultVpnAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 255),
          ("up", 1))
    )


_HwVpnCfgPingResultVpnAdminStatus_Type.__name__ = "Integer32"
_HwVpnCfgPingResultVpnAdminStatus_Object = MibTableColumn
hwVpnCfgPingResultVpnAdminStatus = _HwVpnCfgPingResultVpnAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 5),
    _HwVpnCfgPingResultVpnAdminStatus_Type()
)
hwVpnCfgPingResultVpnAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultVpnAdminStatus.setStatus("current")


class _HwVpnCfgPingResultOperStatus_Type(Integer32):
    """Custom type hwVpnCfgPingResultOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 255),
          ("up", 1))
    )


_HwVpnCfgPingResultOperStatus_Type.__name__ = "Integer32"
_HwVpnCfgPingResultOperStatus_Object = MibTableColumn
hwVpnCfgPingResultOperStatus = _HwVpnCfgPingResultOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 6),
    _HwVpnCfgPingResultOperStatus_Type()
)
hwVpnCfgPingResultOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultOperStatus.setStatus("current")
_HwVpnCfgPingResultMtu_Type = Integer32
_HwVpnCfgPingResultMtu_Object = MibTableColumn
hwVpnCfgPingResultMtu = _HwVpnCfgPingResultMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 7),
    _HwVpnCfgPingResultMtu_Type()
)
hwVpnCfgPingResultMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultMtu.setStatus("current")
_HwVpnCfgPingResultCeCount_Type = Integer32
_HwVpnCfgPingResultCeCount_Object = MibTableColumn
hwVpnCfgPingResultCeCount = _HwVpnCfgPingResultCeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 8),
    _HwVpnCfgPingResultCeCount_Type()
)
hwVpnCfgPingResultCeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultCeCount.setStatus("current")
_HwVpnCfgPingResultActualIpType_Type = InetAddressType
_HwVpnCfgPingResultActualIpType_Object = MibTableColumn
hwVpnCfgPingResultActualIpType = _HwVpnCfgPingResultActualIpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 9),
    _HwVpnCfgPingResultActualIpType_Type()
)
hwVpnCfgPingResultActualIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultActualIpType.setStatus("current")
_HwVpnCfgPingResultActualIp_Type = InetAddress
_HwVpnCfgPingResultActualIp_Object = MibTableColumn
hwVpnCfgPingResultActualIp = _HwVpnCfgPingResultActualIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 10),
    _HwVpnCfgPingResultActualIp_Type()
)
hwVpnCfgPingResultActualIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultActualIp.setStatus("current")
_HwVpnCfgPingResultPeerIpType_Type = InetAddressType
_HwVpnCfgPingResultPeerIpType_Object = MibTableColumn
hwVpnCfgPingResultPeerIpType = _HwVpnCfgPingResultPeerIpType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 11),
    _HwVpnCfgPingResultPeerIpType_Type()
)
hwVpnCfgPingResultPeerIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultPeerIpType.setStatus("current")
_HwVpnCfgPingResultPeerIp_Type = InetAddress
_HwVpnCfgPingResultPeerIp_Object = MibTableColumn
hwVpnCfgPingResultPeerIp = _HwVpnCfgPingResultPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 12),
    _HwVpnCfgPingResultPeerIp_Type()
)
hwVpnCfgPingResultPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultPeerIp.setStatus("current")
_HwVpnCfgPingResultPwId_Type = Integer32
_HwVpnCfgPingResultPwId_Object = MibTableColumn
hwVpnCfgPingResultPwId = _HwVpnCfgPingResultPwId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 13),
    _HwVpnCfgPingResultPwId_Type()
)
hwVpnCfgPingResultPwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultPwId.setStatus("current")


class _HwVpnCfgPingResultPeType_Type(Integer32):
    """Custom type hwVpnCfgPingResultPeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("spe", 2),
          ("unknown", 255),
          ("upe", 1))
    )


_HwVpnCfgPingResultPeType_Type.__name__ = "Integer32"
_HwVpnCfgPingResultPeType_Object = MibTableColumn
hwVpnCfgPingResultPeType = _HwVpnCfgPingResultPeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 14),
    _HwVpnCfgPingResultPeType_Type()
)
hwVpnCfgPingResultPeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultPeType.setStatus("current")
_HwVpnCfgPingResultVcType_Type = HWL2VpnVcEncapsType
_HwVpnCfgPingResultVcType_Object = MibTableColumn
hwVpnCfgPingResultVcType = _HwVpnCfgPingResultVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 15),
    _HwVpnCfgPingResultVcType_Type()
)
hwVpnCfgPingResultVcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultVcType.setStatus("current")
_HwVpnCfgPingResultLabelIn_Type = Integer32
_HwVpnCfgPingResultLabelIn_Object = MibTableColumn
hwVpnCfgPingResultLabelIn = _HwVpnCfgPingResultLabelIn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 16),
    _HwVpnCfgPingResultLabelIn_Type()
)
hwVpnCfgPingResultLabelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultLabelIn.setStatus("current")
_HwVpnCfgPingResultLableOut_Type = Integer32
_HwVpnCfgPingResultLableOut_Object = MibTableColumn
hwVpnCfgPingResultLableOut = _HwVpnCfgPingResultLableOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 17),
    _HwVpnCfgPingResultLableOut_Type()
)
hwVpnCfgPingResultLableOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultLableOut.setStatus("current")


class _HwVpnCfgPingResultControlWord_Type(Integer32):
    """Custom type hwVpnCfgPingResultControlWord based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("unknown", 255))
    )


_HwVpnCfgPingResultControlWord_Type.__name__ = "Integer32"
_HwVpnCfgPingResultControlWord_Object = MibTableColumn
hwVpnCfgPingResultControlWord = _HwVpnCfgPingResultControlWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 18),
    _HwVpnCfgPingResultControlWord_Type()
)
hwVpnCfgPingResultControlWord.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultControlWord.setStatus("current")


class _HwVpnCfgPingResultPriOrSec_Type(Integer32):
    """Custom type hwVpnCfgPingResultPriOrSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("primary", 0),
          ("secondary", 1),
          ("unknown", 255))
    )


_HwVpnCfgPingResultPriOrSec_Type.__name__ = "Integer32"
_HwVpnCfgPingResultPriOrSec_Object = MibTableColumn
hwVpnCfgPingResultPriOrSec = _HwVpnCfgPingResultPriOrSec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 19),
    _HwVpnCfgPingResultPriOrSec_Type()
)
hwVpnCfgPingResultPriOrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultPriOrSec.setStatus("current")
_HwVpnCfgPingResultVplsID_Type = OctetString
_HwVpnCfgPingResultVplsID_Object = MibTableColumn
hwVpnCfgPingResultVplsID = _HwVpnCfgPingResultVplsID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 20),
    _HwVpnCfgPingResultVplsID_Type()
)
hwVpnCfgPingResultVplsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultVplsID.setStatus("current")
_HwVpnCfgPingResultRD_Type = OctetString
_HwVpnCfgPingResultRD_Object = MibTableColumn
hwVpnCfgPingResultRD = _HwVpnCfgPingResultRD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 21),
    _HwVpnCfgPingResultRD_Type()
)
hwVpnCfgPingResultRD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultRD.setStatus("current")
_HwVpnCfgPingResultPwIdNew_Type = Unsigned32
_HwVpnCfgPingResultPwIdNew_Object = MibTableColumn
hwVpnCfgPingResultPwIdNew = _HwVpnCfgPingResultPwIdNew_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 2, 1, 22),
    _HwVpnCfgPingResultPwIdNew_Type()
)
hwVpnCfgPingResultPwIdNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultPwIdNew.setStatus("current")
_HwVpnCfgPingConformance_ObjectIdentity = ObjectIdentity
hwVpnCfgPingConformance = _HwVpnCfgPingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3)
)
_HwVpnCfgPingGroups_ObjectIdentity = ObjectIdentity
hwVpnCfgPingGroups = _HwVpnCfgPingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3, 1)
)
_HwVpnCfgPingCompliances_ObjectIdentity = ObjectIdentity
hwVpnCfgPingCompliances = _HwVpnCfgPingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3, 2)
)
_HwVpnCfgPingResultIRtTable_Object = MibTable
hwVpnCfgPingResultIRtTable = _HwVpnCfgPingResultIRtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 4)
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultIRtTable.setStatus("current")
_HwVpnCfgPingResultIRtEntry_Object = MibTableRow
hwVpnCfgPingResultIRtEntry = _HwVpnCfgPingResultIRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 4, 1)
)
hwVpnCfgPingResultIRtEntry.setIndexNames(
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingIndex"),
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultLocation"),
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultIRtIndex"),
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultIRtEntry.setStatus("current")
_HwVpnCfgPingResultIRtIndex_Type = Integer32
_HwVpnCfgPingResultIRtIndex_Object = MibTableColumn
hwVpnCfgPingResultIRtIndex = _HwVpnCfgPingResultIRtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 4, 1, 1),
    _HwVpnCfgPingResultIRtIndex_Type()
)
hwVpnCfgPingResultIRtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultIRtIndex.setStatus("current")
_HwVpnCfgPingResultIRt_Type = OctetString
_HwVpnCfgPingResultIRt_Object = MibTableColumn
hwVpnCfgPingResultIRt = _HwVpnCfgPingResultIRt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 4, 1, 2),
    _HwVpnCfgPingResultIRt_Type()
)
hwVpnCfgPingResultIRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultIRt.setStatus("current")
_HwVpnCfgPingResultERtTable_Object = MibTable
hwVpnCfgPingResultERtTable = _HwVpnCfgPingResultERtTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 5)
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultERtTable.setStatus("current")
_HwVpnCfgPingResultERtEntry_Object = MibTableRow
hwVpnCfgPingResultERtEntry = _HwVpnCfgPingResultERtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 5, 1)
)
hwVpnCfgPingResultERtEntry.setIndexNames(
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingIndex"),
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultLocation"),
    (0, "HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultERtIndex"),
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultERtEntry.setStatus("current")
_HwVpnCfgPingResultERtIndex_Type = Integer32
_HwVpnCfgPingResultERtIndex_Object = MibTableColumn
hwVpnCfgPingResultERtIndex = _HwVpnCfgPingResultERtIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 5, 1, 1),
    _HwVpnCfgPingResultERtIndex_Type()
)
hwVpnCfgPingResultERtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultERtIndex.setStatus("current")
_HwVpnCfgPingResultERt_Type = OctetString
_HwVpnCfgPingResultERt_Object = MibTableColumn
hwVpnCfgPingResultERt = _HwVpnCfgPingResultERt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 5, 1, 2),
    _HwVpnCfgPingResultERt_Type()
)
hwVpnCfgPingResultERt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVpnCfgPingResultERt.setStatus("current")

# Managed Objects groups

hwPopuBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5, 1, 1)
)
hwPopuBaseGroup.setObjects(
      *(("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacPopulateCount"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacPurgeCount"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacPurgeRegCount"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacCountReset"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacSwitch"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacEntryNum"))
)
if mibBuilder.loadTexts:
    hwPopuBaseGroup.setStatus("current")

hwOamMacOperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5, 1, 2)
)
hwOamMacOperGroup.setObjects(
      *(("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperAddress"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperVsiName"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperRegister"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperFlood"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperNum"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacOperRowStatus"))
)
if mibBuilder.loadTexts:
    hwOamMacOperGroup.setStatus("current")

hwOamMacListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5, 1, 3)
)
hwOamMacListGroup.setObjects(
    ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacListAddress")
)
if mibBuilder.loadTexts:
    hwOamMacListGroup.setStatus("current")

hwOamMacDisplayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5, 1, 4)
)
hwOamMacDisplayGroup.setObjects(
      *(("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacDisplayAddress"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacDisplayType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacDisplayVsiName"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacDisplayAgeTime"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwOamMacDisplayLsrId"))
)
if mibBuilder.loadTexts:
    hwOamMacDisplayGroup.setStatus("current")

hwVpnCfgPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3, 1, 1)
)
hwVpnCfgPingGroup.setObjects(
      *(("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingPeerIpType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingPeerIp"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingVpnIdType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingVpnId"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingPwId"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingTunnelUsed"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingOperation"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultDetail"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingRowStatus"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingIfName"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingSecondary"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingPwIdNew"))
)
if mibBuilder.loadTexts:
    hwVpnCfgPingGroup.setStatus("current")

hwVpnCfgPingResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3, 1, 2)
)
hwVpnCfgPingResultGroup.setObjects(
      *(("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultVpnIdType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultVpnId"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultDesc"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultVpnAdminStatus"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultOperStatus"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultMtu"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultCeCount"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultActualIpType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultActualIp"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultPeerIpType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultPeerIp"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultPwId"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultPeType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultVcType"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultLabelIn"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultLableOut"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultControlWord"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultPriOrSec"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultVplsID"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultRD"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultPwIdNew"))
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultGroup.setStatus("current")

hwVpnCfgPingResultIRtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3, 1, 3)
)
hwVpnCfgPingResultIRtGroup.setObjects(
      *(("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultIRtIndex"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultIRt"))
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultIRtGroup.setStatus("current")

hwVpnCfgPingResultERtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3, 1, 4)
)
hwVpnCfgPingResultERtGroup.setObjects(
      *(("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultERtIndex"),
        ("HUAWEI-VPN-DIAGNOSTICS-MIB", "hwVpnCfgPingResultERt"))
)
if mibBuilder.loadTexts:
    hwVpnCfgPingResultERtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

macoperCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    macoperCompliance.setStatus(
        "current"
    )

hwVpnCfgPingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 172, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwVpnCfgPingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VPN-DIAGNOSTICS-MIB",
    **{"MacOpType": MacOpType,
       "vpndiagnostics": vpndiagnostics,
       "macoper": macoper,
       "populateBase": populateBase,
       "hwOamMacPopulateCount": hwOamMacPopulateCount,
       "hwOamMacPurgeCount": hwOamMacPurgeCount,
       "hwOamMacPurgeRegCount": hwOamMacPurgeRegCount,
       "hwOamMacCountReset": hwOamMacCountReset,
       "hwOamMacSwitch": hwOamMacSwitch,
       "hwOamMacEntryNum": hwOamMacEntryNum,
       "hwOamMacOperTable": hwOamMacOperTable,
       "hwOamMacOperEntry": hwOamMacOperEntry,
       "hwOamMacOperIndex": hwOamMacOperIndex,
       "hwOamMacOperAddress": hwOamMacOperAddress,
       "hwOamMacOperVsiName": hwOamMacOperVsiName,
       "hwOamMacOperType": hwOamMacOperType,
       "hwOamMacOperRegister": hwOamMacOperRegister,
       "hwOamMacOperFlood": hwOamMacOperFlood,
       "hwOamMacOperNum": hwOamMacOperNum,
       "hwOamMacOperRowStatus": hwOamMacOperRowStatus,
       "hwOamMacListTable": hwOamMacListTable,
       "hwOamMacListEntry": hwOamMacListEntry,
       "hwOamMacListIndex": hwOamMacListIndex,
       "hwOamMacListAddress": hwOamMacListAddress,
       "hwOamMacDisplayTable": hwOamMacDisplayTable,
       "hwOamMacDisplayEntry": hwOamMacDisplayEntry,
       "hwOamMacDisplayIndex": hwOamMacDisplayIndex,
       "hwOamMacDisplayAddress": hwOamMacDisplayAddress,
       "hwOamMacDisplayType": hwOamMacDisplayType,
       "hwOamMacDisplayVsiName": hwOamMacDisplayVsiName,
       "hwOamMacDisplayAgeTime": hwOamMacDisplayAgeTime,
       "hwOamMacDisplayLsrId": hwOamMacDisplayLsrId,
       "macoperConformance": macoperConformance,
       "hwOamMacGroup": hwOamMacGroup,
       "hwPopuBaseGroup": hwPopuBaseGroup,
       "hwOamMacOperGroup": hwOamMacOperGroup,
       "hwOamMacListGroup": hwOamMacListGroup,
       "hwOamMacDisplayGroup": hwOamMacDisplayGroup,
       "macoperCompliances": macoperCompliances,
       "macoperCompliance": macoperCompliance,
       "hwVpnCfgPing": hwVpnCfgPing,
       "hwVpnCfgPingTable": hwVpnCfgPingTable,
       "hwVpnCfgPingEntry": hwVpnCfgPingEntry,
       "hwVpnCfgPingIndex": hwVpnCfgPingIndex,
       "hwVpnCfgPingPeerIpType": hwVpnCfgPingPeerIpType,
       "hwVpnCfgPingPeerIp": hwVpnCfgPingPeerIp,
       "hwVpnCfgPingVpnIdType": hwVpnCfgPingVpnIdType,
       "hwVpnCfgPingVpnId": hwVpnCfgPingVpnId,
       "hwVpnCfgPingPwId": hwVpnCfgPingPwId,
       "hwVpnCfgPingTunnelUsed": hwVpnCfgPingTunnelUsed,
       "hwVpnCfgPingOperation": hwVpnCfgPingOperation,
       "hwVpnCfgPingResultDetail": hwVpnCfgPingResultDetail,
       "hwVpnCfgPingRowStatus": hwVpnCfgPingRowStatus,
       "hwVpnCfgPingSecondary": hwVpnCfgPingSecondary,
       "hwVpnCfgPingIfName": hwVpnCfgPingIfName,
       "hwVpnCfgPingPwIdNew": hwVpnCfgPingPwIdNew,
       "hwVpnCfgPingResultTable": hwVpnCfgPingResultTable,
       "hwVpnCfgPingResultEntry": hwVpnCfgPingResultEntry,
       "hwVpnCfgPingResultLocation": hwVpnCfgPingResultLocation,
       "hwVpnCfgPingResultVpnIdType": hwVpnCfgPingResultVpnIdType,
       "hwVpnCfgPingResultVpnId": hwVpnCfgPingResultVpnId,
       "hwVpnCfgPingResultDesc": hwVpnCfgPingResultDesc,
       "hwVpnCfgPingResultVpnAdminStatus": hwVpnCfgPingResultVpnAdminStatus,
       "hwVpnCfgPingResultOperStatus": hwVpnCfgPingResultOperStatus,
       "hwVpnCfgPingResultMtu": hwVpnCfgPingResultMtu,
       "hwVpnCfgPingResultCeCount": hwVpnCfgPingResultCeCount,
       "hwVpnCfgPingResultActualIpType": hwVpnCfgPingResultActualIpType,
       "hwVpnCfgPingResultActualIp": hwVpnCfgPingResultActualIp,
       "hwVpnCfgPingResultPeerIpType": hwVpnCfgPingResultPeerIpType,
       "hwVpnCfgPingResultPeerIp": hwVpnCfgPingResultPeerIp,
       "hwVpnCfgPingResultPwId": hwVpnCfgPingResultPwId,
       "hwVpnCfgPingResultPeType": hwVpnCfgPingResultPeType,
       "hwVpnCfgPingResultVcType": hwVpnCfgPingResultVcType,
       "hwVpnCfgPingResultLabelIn": hwVpnCfgPingResultLabelIn,
       "hwVpnCfgPingResultLableOut": hwVpnCfgPingResultLableOut,
       "hwVpnCfgPingResultControlWord": hwVpnCfgPingResultControlWord,
       "hwVpnCfgPingResultPriOrSec": hwVpnCfgPingResultPriOrSec,
       "hwVpnCfgPingResultVplsID": hwVpnCfgPingResultVplsID,
       "hwVpnCfgPingResultRD": hwVpnCfgPingResultRD,
       "hwVpnCfgPingResultPwIdNew": hwVpnCfgPingResultPwIdNew,
       "hwVpnCfgPingConformance": hwVpnCfgPingConformance,
       "hwVpnCfgPingGroups": hwVpnCfgPingGroups,
       "hwVpnCfgPingGroup": hwVpnCfgPingGroup,
       "hwVpnCfgPingResultGroup": hwVpnCfgPingResultGroup,
       "hwVpnCfgPingResultIRtGroup": hwVpnCfgPingResultIRtGroup,
       "hwVpnCfgPingResultERtGroup": hwVpnCfgPingResultERtGroup,
       "hwVpnCfgPingCompliances": hwVpnCfgPingCompliances,
       "hwVpnCfgPingCompliance": hwVpnCfgPingCompliance,
       "hwVpnCfgPingResultIRtTable": hwVpnCfgPingResultIRtTable,
       "hwVpnCfgPingResultIRtEntry": hwVpnCfgPingResultIRtEntry,
       "hwVpnCfgPingResultIRtIndex": hwVpnCfgPingResultIRtIndex,
       "hwVpnCfgPingResultIRt": hwVpnCfgPingResultIRt,
       "hwVpnCfgPingResultERtTable": hwVpnCfgPingResultERtTable,
       "hwVpnCfgPingResultERtEntry": hwVpnCfgPingResultERtEntry,
       "hwVpnCfgPingResultERtIndex": hwVpnCfgPingResultERtIndex,
       "hwVpnCfgPingResultERt": hwVpnCfgPingResultERt}
)
