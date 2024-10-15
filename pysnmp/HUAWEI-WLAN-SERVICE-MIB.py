# SNMP MIB module (HUAWEI-WLAN-SERVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-WLAN-SERVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:39 2024
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

(hwWlan,) = mibBuilder.importSymbols(
    "HUAWEI-WLAN-MIB",
    "hwWlan")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwWlanServiceManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4)
)
hwWlanServiceManagement.setRevisions(
        ("2015-09-25 09:38",
         "2015-06-18 20:25",
         "2015-01-20 20:25",
         "2014-12-16 15:25",
         "2014-11-29 15:25",
         "2014-08-30 15:25",
         "2014-08-22 15:25",
         "2014-08-08 15:25",
         "2014-07-17 15:25",
         "2014-06-08 15:25",
         "2014-04-21 14:05",
         "2014-03-22 14:05",
         "2013-12-11 14:09",
         "2013-10-23 14:09",
         "2010-06-01 10:00",
         "2010-08-13 10:00",
         "2010-09-02 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwEssManagementTable_Object = MibTable
hwEssManagementTable = _HwEssManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1)
)
if mibBuilder.loadTexts:
    hwEssManagementTable.setStatus("current")
_HwEssManagementEntry_Object = MibTableRow
hwEssManagementEntry = _HwEssManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1)
)
hwEssManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssName"),
)
if mibBuilder.loadTexts:
    hwEssManagementEntry.setStatus("current")


class _HwWlanServiceEssName_Type(OctetString):
    """Custom type hwWlanServiceEssName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceEssName_Type.__name__ = "OctetString"
_HwWlanServiceEssName_Object = MibTableColumn
hwWlanServiceEssName = _HwWlanServiceEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 1),
    _HwWlanServiceEssName_Type()
)
hwWlanServiceEssName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceEssName.setStatus("current")


class _HwWlanServiceEssSsid_Type(OctetString):
    """Custom type hwWlanServiceEssSsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwWlanServiceEssSsid_Type.__name__ = "OctetString"
_HwWlanServiceEssSsid_Object = MibTableColumn
hwWlanServiceEssSsid = _HwWlanServiceEssSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 2),
    _HwWlanServiceEssSsid_Type()
)
hwWlanServiceEssSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssSsid.setStatus("current")


class _HwWlanServiceEssHideSsid_Type(Integer32):
    """Custom type hwWlanServiceEssHideSsid based on Integer32"""
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


_HwWlanServiceEssHideSsid_Type.__name__ = "Integer32"
_HwWlanServiceEssHideSsid_Object = MibTableColumn
hwWlanServiceEssHideSsid = _HwWlanServiceEssHideSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 3),
    _HwWlanServiceEssHideSsid_Type()
)
hwWlanServiceEssHideSsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssHideSsid.setStatus("current")


class _HwWlanServiceEssUserIsolate_Type(Integer32):
    """Custom type hwWlanServiceEssUserIsolate based on Integer32"""
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


_HwWlanServiceEssUserIsolate_Type.__name__ = "Integer32"
_HwWlanServiceEssUserIsolate_Object = MibTableColumn
hwWlanServiceEssUserIsolate = _HwWlanServiceEssUserIsolate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 4),
    _HwWlanServiceEssUserIsolate_Type()
)
hwWlanServiceEssUserIsolate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssUserIsolate.setStatus("current")


class _HwWlanServiceEssType_Type(Integer32):
    """Custom type hwWlanServiceEssType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acManagement", 3),
          ("apManagement", 2),
          ("service", 1))
    )


_HwWlanServiceEssType_Type.__name__ = "Integer32"
_HwWlanServiceEssType_Object = MibTableColumn
hwWlanServiceEssType = _HwWlanServiceEssType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 5),
    _HwWlanServiceEssType_Type()
)
hwWlanServiceEssType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssType.setStatus("current")


class _HwWlanServiceEssTrafficProfileName_Type(OctetString):
    """Custom type hwWlanServiceEssTrafficProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceEssTrafficProfileName_Type.__name__ = "OctetString"
_HwWlanServiceEssTrafficProfileName_Object = MibTableColumn
hwWlanServiceEssTrafficProfileName = _HwWlanServiceEssTrafficProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 6),
    _HwWlanServiceEssTrafficProfileName_Type()
)
hwWlanServiceEssTrafficProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssTrafficProfileName.setStatus("current")


class _HwWlanServiceEssSecurityProfileName_Type(OctetString):
    """Custom type hwWlanServiceEssSecurityProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceEssSecurityProfileName_Type.__name__ = "OctetString"
_HwWlanServiceEssSecurityProfileName_Object = MibTableColumn
hwWlanServiceEssSecurityProfileName = _HwWlanServiceEssSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 7),
    _HwWlanServiceEssSecurityProfileName_Type()
)
hwWlanServiceEssSecurityProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssSecurityProfileName.setStatus("current")
_HwWlanServiceEssMaxUserNumber_Type = Integer32
_HwWlanServiceEssMaxUserNumber_Object = MibTableColumn
hwWlanServiceEssMaxUserNumber = _HwWlanServiceEssMaxUserNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 8),
    _HwWlanServiceEssMaxUserNumber_Type()
)
hwWlanServiceEssMaxUserNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssMaxUserNumber.setStatus("current")
_HwWlanServiceEssAssociationTimeOut_Type = Integer32
_HwWlanServiceEssAssociationTimeOut_Object = MibTableColumn
hwWlanServiceEssAssociationTimeOut = _HwWlanServiceEssAssociationTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 9),
    _HwWlanServiceEssAssociationTimeOut_Type()
)
hwWlanServiceEssAssociationTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssAssociationTimeOut.setStatus("current")


class _HwWlanServiceEssIgmpMode_Type(Integer32):
    """Custom type hwWlanServiceEssIgmpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("proxy", 1),
          ("snooping", 2))
    )


_HwWlanServiceEssIgmpMode_Type.__name__ = "Integer32"
_HwWlanServiceEssIgmpMode_Object = MibTableColumn
hwWlanServiceEssIgmpMode = _HwWlanServiceEssIgmpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 10),
    _HwWlanServiceEssIgmpMode_Type()
)
hwWlanServiceEssIgmpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceEssIgmpMode.setStatus("current")
_HwWlanServiceEssRowStatus_Type = RowStatus
_HwWlanServiceEssRowStatus_Object = MibTableColumn
hwWlanServiceEssRowStatus = _HwWlanServiceEssRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 11),
    _HwWlanServiceEssRowStatus_Type()
)
hwWlanServiceEssRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssRowStatus.setStatus("current")


class _HwWlanServiceEssForwardMode_Type(Integer32):
    """Custom type hwWlanServiceEssForwardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("directForward", 1),
          ("tunnel", 2),
          ("unknown", -1))
    )


_HwWlanServiceEssForwardMode_Type.__name__ = "Integer32"
_HwWlanServiceEssForwardMode_Object = MibTableColumn
hwWlanServiceEssForwardMode = _HwWlanServiceEssForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 12),
    _HwWlanServiceEssForwardMode_Type()
)
hwWlanServiceEssForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssForwardMode.setStatus("current")
_HwWlanServiceEssNum_Type = Integer32
_HwWlanServiceEssNum_Object = MibTableColumn
hwWlanServiceEssNum = _HwWlanServiceEssNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 13),
    _HwWlanServiceEssNum_Type()
)
hwWlanServiceEssNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssNum.setStatus("current")


class _HwWlanServiceVlan_Type(Integer32):
    """Custom type hwWlanServiceVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwWlanServiceVlan_Type.__name__ = "Integer32"
_HwWlanServiceVlan_Object = MibTableColumn
hwWlanServiceVlan = _HwWlanServiceVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 14),
    _HwWlanServiceVlan_Type()
)
hwWlanServiceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceVlan.setStatus("current")


class _HwWlanServiceEssDhcpSnooping_Type(Integer32):
    """Custom type hwWlanServiceEssDhcpSnooping based on Integer32"""
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


_HwWlanServiceEssDhcpSnooping_Type.__name__ = "Integer32"
_HwWlanServiceEssDhcpSnooping_Object = MibTableColumn
hwWlanServiceEssDhcpSnooping = _HwWlanServiceEssDhcpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 15),
    _HwWlanServiceEssDhcpSnooping_Type()
)
hwWlanServiceEssDhcpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssDhcpSnooping.setStatus("current")


class _HwWlanServiceEssServiceVlanEnable_Type(Integer32):
    """Custom type hwWlanServiceEssServiceVlanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssServiceVlanEnable_Type.__name__ = "Integer32"
_HwWlanServiceEssServiceVlanEnable_Object = MibTableColumn
hwWlanServiceEssServiceVlanEnable = _HwWlanServiceEssServiceVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 16),
    _HwWlanServiceEssServiceVlanEnable_Type()
)
hwWlanServiceEssServiceVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssServiceVlanEnable.setStatus("current")


class _HwWlanServiceEssIPSGEnable_Type(Integer32):
    """Custom type hwWlanServiceEssIPSGEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssIPSGEnable_Type.__name__ = "Integer32"
_HwWlanServiceEssIPSGEnable_Object = MibTableColumn
hwWlanServiceEssIPSGEnable = _HwWlanServiceEssIPSGEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 17),
    _HwWlanServiceEssIPSGEnable_Type()
)
hwWlanServiceEssIPSGEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssIPSGEnable.setStatus("current")


class _HwWlanServiceEssDhcpTrustPort_Type(Integer32):
    """Custom type hwWlanServiceEssDhcpTrustPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssDhcpTrustPort_Type.__name__ = "Integer32"
_HwWlanServiceEssDhcpTrustPort_Object = MibTableColumn
hwWlanServiceEssDhcpTrustPort = _HwWlanServiceEssDhcpTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 18),
    _HwWlanServiceEssDhcpTrustPort_Type()
)
hwWlanServiceEssDhcpTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssDhcpTrustPort.setStatus("current")


class _HwWlanServiceEssDaiSwitch_Type(Integer32):
    """Custom type hwWlanServiceEssDaiSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssDaiSwitch_Type.__name__ = "Integer32"
_HwWlanServiceEssDaiSwitch_Object = MibTableColumn
hwWlanServiceEssDaiSwitch = _HwWlanServiceEssDaiSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 19),
    _HwWlanServiceEssDaiSwitch_Type()
)
hwWlanServiceEssDaiSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssDaiSwitch.setStatus("current")


class _HwWlanServiceEssArpThreshold_Type(Integer32):
    """Custom type hwWlanServiceEssArpThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_HwWlanServiceEssArpThreshold_Type.__name__ = "Integer32"
_HwWlanServiceEssArpThreshold_Object = MibTableColumn
hwWlanServiceEssArpThreshold = _HwWlanServiceEssArpThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 20),
    _HwWlanServiceEssArpThreshold_Type()
)
hwWlanServiceEssArpThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssArpThreshold.setStatus("current")
_HwWlanServiceEssTunnelProtocol_Type = Integer32
_HwWlanServiceEssTunnelProtocol_Object = MibTableColumn
hwWlanServiceEssTunnelProtocol = _HwWlanServiceEssTunnelProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 21),
    _HwWlanServiceEssTunnelProtocol_Type()
)
hwWlanServiceEssTunnelProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssTunnelProtocol.setStatus("current")
_HwWlanServiceEssStatus_Type = Integer32
_HwWlanServiceEssStatus_Object = MibTableColumn
hwWlanServiceEssStatus = _HwWlanServiceEssStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 22),
    _HwWlanServiceEssStatus_Type()
)
hwWlanServiceEssStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceEssStatus.setStatus("current")


class _HwWlanServiceEssOfflineManagement_Type(Integer32):
    """Custom type hwWlanServiceEssOfflineManagement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssOfflineManagement_Type.__name__ = "Integer32"
_HwWlanServiceEssOfflineManagement_Object = MibTableColumn
hwWlanServiceEssOfflineManagement = _HwWlanServiceEssOfflineManagement_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 23),
    _HwWlanServiceEssOfflineManagement_Type()
)
hwWlanServiceEssOfflineManagement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssOfflineManagement.setStatus("current")


class _HwWlanServiceEssBlacklistProfileName_Type(OctetString):
    """Custom type hwWlanServiceEssBlacklistProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceEssBlacklistProfileName_Type.__name__ = "OctetString"
_HwWlanServiceEssBlacklistProfileName_Object = MibTableColumn
hwWlanServiceEssBlacklistProfileName = _HwWlanServiceEssBlacklistProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 24),
    _HwWlanServiceEssBlacklistProfileName_Type()
)
hwWlanServiceEssBlacklistProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssBlacklistProfileName.setStatus("current")


class _HwWlanServiceEssWhitelistProfileName_Type(OctetString):
    """Custom type hwWlanServiceEssWhitelistProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceEssWhitelistProfileName_Type.__name__ = "OctetString"
_HwWlanServiceEssWhitelistProfileName_Object = MibTableColumn
hwWlanServiceEssWhitelistProfileName = _HwWlanServiceEssWhitelistProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 25),
    _HwWlanServiceEssWhitelistProfileName_Type()
)
hwWlanServiceEssWhitelistProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssWhitelistProfileName.setStatus("current")


class _HwWlanServiceEssStaAccessMode_Type(Integer32):
    """Custom type hwWlanServiceEssStaAccessMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blacklistProfile", 2),
          ("disable", 1),
          ("unknown", -1),
          ("whitelistProfile", 3))
    )


_HwWlanServiceEssStaAccessMode_Type.__name__ = "Integer32"
_HwWlanServiceEssStaAccessMode_Object = MibTableColumn
hwWlanServiceEssStaAccessMode = _HwWlanServiceEssStaAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 26),
    _HwWlanServiceEssStaAccessMode_Type()
)
hwWlanServiceEssStaAccessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssStaAccessMode.setStatus("current")


class _HwWlanServiceEssDhcpOption82InsertSwitch_Type(Integer32):
    """Custom type hwWlanServiceEssDhcpOption82InsertSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssDhcpOption82InsertSwitch_Type.__name__ = "Integer32"
_HwWlanServiceEssDhcpOption82InsertSwitch_Object = MibTableColumn
hwWlanServiceEssDhcpOption82InsertSwitch = _HwWlanServiceEssDhcpOption82InsertSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 27),
    _HwWlanServiceEssDhcpOption82InsertSwitch_Type()
)
hwWlanServiceEssDhcpOption82InsertSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssDhcpOption82InsertSwitch.setStatus("current")


class _HwWlanServiceEssDhcpOption82RemoteIdFormat_Type(Integer32):
    """Custom type hwWlanServiceEssDhcpOption82RemoteIdFormat based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("apMac", 1),
          ("apMacSsid", 2))
    )


_HwWlanServiceEssDhcpOption82RemoteIdFormat_Type.__name__ = "Integer32"
_HwWlanServiceEssDhcpOption82RemoteIdFormat_Object = MibTableColumn
hwWlanServiceEssDhcpOption82RemoteIdFormat = _HwWlanServiceEssDhcpOption82RemoteIdFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 28),
    _HwWlanServiceEssDhcpOption82RemoteIdFormat_Type()
)
hwWlanServiceEssDhcpOption82RemoteIdFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssDhcpOption82RemoteIdFormat.setStatus("current")


class _HwWlanServiceEssDhcpSnoopingOption_Type(OctetString):
    """Custom type hwWlanServiceEssDhcpSnoopingOption based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwWlanServiceEssDhcpSnoopingOption_Type.__name__ = "OctetString"
_HwWlanServiceEssDhcpSnoopingOption_Object = MibTableColumn
hwWlanServiceEssDhcpSnoopingOption = _HwWlanServiceEssDhcpSnoopingOption_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 29),
    _HwWlanServiceEssDhcpSnoopingOption_Type()
)
hwWlanServiceEssDhcpSnoopingOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssDhcpSnoopingOption.setStatus("current")
_HwWlanServiceEssBroadCastPps_Type = Integer32
_HwWlanServiceEssBroadCastPps_Object = MibTableColumn
hwWlanServiceEssBroadCastPps = _HwWlanServiceEssBroadCastPps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 30),
    _HwWlanServiceEssBroadCastPps_Type()
)
hwWlanServiceEssBroadCastPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssBroadCastPps.setStatus("current")
_HwWlanServiceEssMultiCastPps_Type = Integer32
_HwWlanServiceEssMultiCastPps_Object = MibTableColumn
hwWlanServiceEssMultiCastPps = _HwWlanServiceEssMultiCastPps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 31),
    _HwWlanServiceEssMultiCastPps_Type()
)
hwWlanServiceEssMultiCastPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssMultiCastPps.setStatus("current")
_HwWlanServiceEssUniCastPps_Type = Integer32
_HwWlanServiceEssUniCastPps_Object = MibTableColumn
hwWlanServiceEssUniCastPps = _HwWlanServiceEssUniCastPps_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 32),
    _HwWlanServiceEssUniCastPps_Type()
)
hwWlanServiceEssUniCastPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssUniCastPps.setStatus("current")


class _HwWlanServiceEssBroadCastSwitch_Type(Integer32):
    """Custom type hwWlanServiceEssBroadCastSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssBroadCastSwitch_Type.__name__ = "Integer32"
_HwWlanServiceEssBroadCastSwitch_Object = MibTableColumn
hwWlanServiceEssBroadCastSwitch = _HwWlanServiceEssBroadCastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 33),
    _HwWlanServiceEssBroadCastSwitch_Type()
)
hwWlanServiceEssBroadCastSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssBroadCastSwitch.setStatus("current")


class _HwWlanServiceEssMultiCastSwitch_Type(Integer32):
    """Custom type hwWlanServiceEssMultiCastSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssMultiCastSwitch_Type.__name__ = "Integer32"
_HwWlanServiceEssMultiCastSwitch_Object = MibTableColumn
hwWlanServiceEssMultiCastSwitch = _HwWlanServiceEssMultiCastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 34),
    _HwWlanServiceEssMultiCastSwitch_Type()
)
hwWlanServiceEssMultiCastSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssMultiCastSwitch.setStatus("current")


class _HwWlanServiceEssUniCastSwitch_Type(Integer32):
    """Custom type hwWlanServiceEssUniCastSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssUniCastSwitch_Type.__name__ = "Integer32"
_HwWlanServiceEssUniCastSwitch_Object = MibTableColumn
hwWlanServiceEssUniCastSwitch = _HwWlanServiceEssUniCastSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 35),
    _HwWlanServiceEssUniCastSwitch_Type()
)
hwWlanServiceEssUniCastSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssUniCastSwitch.setStatus("current")


class _HwWlanServiceEssSaclNameInbound_Type(OctetString):
    """Custom type hwWlanServiceEssSaclNameInbound based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_HwWlanServiceEssSaclNameInbound_Type.__name__ = "OctetString"
_HwWlanServiceEssSaclNameInbound_Object = MibTableColumn
hwWlanServiceEssSaclNameInbound = _HwWlanServiceEssSaclNameInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 36),
    _HwWlanServiceEssSaclNameInbound_Type()
)
hwWlanServiceEssSaclNameInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNameInbound.setStatus("current")


class _HwWlanServiceEssSaclNameOutbound_Type(OctetString):
    """Custom type hwWlanServiceEssSaclNameOutbound based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_HwWlanServiceEssSaclNameOutbound_Type.__name__ = "OctetString"
_HwWlanServiceEssSaclNameOutbound_Object = MibTableColumn
hwWlanServiceEssSaclNameOutbound = _HwWlanServiceEssSaclNameOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 37),
    _HwWlanServiceEssSaclNameOutbound_Type()
)
hwWlanServiceEssSaclNameOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNameOutbound.setStatus("current")
_HwWlanServiceEssSaclNumInbound_Type = Integer32
_HwWlanServiceEssSaclNumInbound_Object = MibTableColumn
hwWlanServiceEssSaclNumInbound = _HwWlanServiceEssSaclNumInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 38),
    _HwWlanServiceEssSaclNumInbound_Type()
)
hwWlanServiceEssSaclNumInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNumInbound.setStatus("current")
_HwWlanServiceEssSaclNumOutbound_Type = Integer32
_HwWlanServiceEssSaclNumOutbound_Object = MibTableColumn
hwWlanServiceEssSaclNumOutbound = _HwWlanServiceEssSaclNumOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 39),
    _HwWlanServiceEssSaclNumOutbound_Type()
)
hwWlanServiceEssSaclNumOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNumOutbound.setStatus("current")


class _HwWlanServiceEssSaclSwtichInbound_Type(Integer32):
    """Custom type hwWlanServiceEssSaclSwtichInbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssSaclSwtichInbound_Type.__name__ = "Integer32"
_HwWlanServiceEssSaclSwtichInbound_Object = MibTableColumn
hwWlanServiceEssSaclSwtichInbound = _HwWlanServiceEssSaclSwtichInbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 40),
    _HwWlanServiceEssSaclSwtichInbound_Type()
)
hwWlanServiceEssSaclSwtichInbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclSwtichInbound.setStatus("current")


class _HwWlanServiceEssSaclSwtichOutbound_Type(Integer32):
    """Custom type hwWlanServiceEssSaclSwtichOutbound based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssSaclSwtichOutbound_Type.__name__ = "Integer32"
_HwWlanServiceEssSaclSwtichOutbound_Object = MibTableColumn
hwWlanServiceEssSaclSwtichOutbound = _HwWlanServiceEssSaclSwtichOutbound_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 41),
    _HwWlanServiceEssSaclSwtichOutbound_Type()
)
hwWlanServiceEssSaclSwtichOutbound.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclSwtichOutbound.setStatus("current")


class _HwWlanServiceEssServiceModeSwitch_Type(Integer32):
    """Custom type hwWlanServiceEssServiceModeSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssServiceModeSwitch_Type.__name__ = "Integer32"
_HwWlanServiceEssServiceModeSwitch_Object = MibTableColumn
hwWlanServiceEssServiceModeSwitch = _HwWlanServiceEssServiceModeSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 42),
    _HwWlanServiceEssServiceModeSwitch_Type()
)
hwWlanServiceEssServiceModeSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssServiceModeSwitch.setStatus("current")


class _HwWlanServiceEssAutoOffEssAdminSwitch_Type(Integer32):
    """Custom type hwWlanServiceEssAutoOffEssAdminSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssAutoOffEssAdminSwitch_Type.__name__ = "Integer32"
_HwWlanServiceEssAutoOffEssAdminSwitch_Object = MibTableColumn
hwWlanServiceEssAutoOffEssAdminSwitch = _HwWlanServiceEssAutoOffEssAdminSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 43),
    _HwWlanServiceEssAutoOffEssAdminSwitch_Type()
)
hwWlanServiceEssAutoOffEssAdminSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssAutoOffEssAdminSwitch.setStatus("current")


class _HwWlanServiceEssAutoOffEssStartTime_Type(OctetString):
    """Custom type hwWlanServiceEssAutoOffEssStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_HwWlanServiceEssAutoOffEssStartTime_Type.__name__ = "OctetString"
_HwWlanServiceEssAutoOffEssStartTime_Object = MibTableColumn
hwWlanServiceEssAutoOffEssStartTime = _HwWlanServiceEssAutoOffEssStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 44),
    _HwWlanServiceEssAutoOffEssStartTime_Type()
)
hwWlanServiceEssAutoOffEssStartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssAutoOffEssStartTime.setStatus("current")


class _HwWlanServiceEssAutoOffEssEndTime_Type(OctetString):
    """Custom type hwWlanServiceEssAutoOffEssEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 11),
    )


_HwWlanServiceEssAutoOffEssEndTime_Type.__name__ = "OctetString"
_HwWlanServiceEssAutoOffEssEndTime_Object = MibTableColumn
hwWlanServiceEssAutoOffEssEndTime = _HwWlanServiceEssAutoOffEssEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 45),
    _HwWlanServiceEssAutoOffEssEndTime_Type()
)
hwWlanServiceEssAutoOffEssEndTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssAutoOffEssEndTime.setStatus("current")


class _HwWlanServiceEssNdSnooping_Type(Integer32):
    """Custom type hwWlanServiceEssNdSnooping based on Integer32"""
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


_HwWlanServiceEssNdSnooping_Type.__name__ = "Integer32"
_HwWlanServiceEssNdSnooping_Object = MibTableColumn
hwWlanServiceEssNdSnooping = _HwWlanServiceEssNdSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 46),
    _HwWlanServiceEssNdSnooping_Type()
)
hwWlanServiceEssNdSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssNdSnooping.setStatus("current")


class _HwWlanServiceEssSaclNameInboundIPv6_Type(OctetString):
    """Custom type hwWlanServiceEssSaclNameInboundIPv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_HwWlanServiceEssSaclNameInboundIPv6_Type.__name__ = "OctetString"
_HwWlanServiceEssSaclNameInboundIPv6_Object = MibTableColumn
hwWlanServiceEssSaclNameInboundIPv6 = _HwWlanServiceEssSaclNameInboundIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 47),
    _HwWlanServiceEssSaclNameInboundIPv6_Type()
)
hwWlanServiceEssSaclNameInboundIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNameInboundIPv6.setStatus("current")


class _HwWlanServiceEssSaclNameOutboundIPv6_Type(OctetString):
    """Custom type hwWlanServiceEssSaclNameOutboundIPv6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65),
    )


_HwWlanServiceEssSaclNameOutboundIPv6_Type.__name__ = "OctetString"
_HwWlanServiceEssSaclNameOutboundIPv6_Object = MibTableColumn
hwWlanServiceEssSaclNameOutboundIPv6 = _HwWlanServiceEssSaclNameOutboundIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 48),
    _HwWlanServiceEssSaclNameOutboundIPv6_Type()
)
hwWlanServiceEssSaclNameOutboundIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNameOutboundIPv6.setStatus("current")
_HwWlanServiceEssSaclNumInboundIPv6_Type = Integer32
_HwWlanServiceEssSaclNumInboundIPv6_Object = MibTableColumn
hwWlanServiceEssSaclNumInboundIPv6 = _HwWlanServiceEssSaclNumInboundIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 49),
    _HwWlanServiceEssSaclNumInboundIPv6_Type()
)
hwWlanServiceEssSaclNumInboundIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNumInboundIPv6.setStatus("current")
_HwWlanServiceEssSaclNumOutboundIPv6_Type = Integer32
_HwWlanServiceEssSaclNumOutboundIPv6_Object = MibTableColumn
hwWlanServiceEssSaclNumOutboundIPv6 = _HwWlanServiceEssSaclNumOutboundIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 50),
    _HwWlanServiceEssSaclNumOutboundIPv6_Type()
)
hwWlanServiceEssSaclNumOutboundIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclNumOutboundIPv6.setStatus("current")


class _HwWlanServiceEssSaclSwtichInboundIPv6_Type(Integer32):
    """Custom type hwWlanServiceEssSaclSwtichInboundIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssSaclSwtichInboundIPv6_Type.__name__ = "Integer32"
_HwWlanServiceEssSaclSwtichInboundIPv6_Object = MibTableColumn
hwWlanServiceEssSaclSwtichInboundIPv6 = _HwWlanServiceEssSaclSwtichInboundIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 51),
    _HwWlanServiceEssSaclSwtichInboundIPv6_Type()
)
hwWlanServiceEssSaclSwtichInboundIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclSwtichInboundIPv6.setStatus("current")


class _HwWlanServiceEssSaclSwtichOutboundIPv6_Type(Integer32):
    """Custom type hwWlanServiceEssSaclSwtichOutboundIPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssSaclSwtichOutboundIPv6_Type.__name__ = "Integer32"
_HwWlanServiceEssSaclSwtichOutboundIPv6_Object = MibTableColumn
hwWlanServiceEssSaclSwtichOutboundIPv6 = _HwWlanServiceEssSaclSwtichOutboundIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 52),
    _HwWlanServiceEssSaclSwtichOutboundIPv6_Type()
)
hwWlanServiceEssSaclSwtichOutboundIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssSaclSwtichOutboundIPv6.setStatus("current")


class _HwWlanServiceEssNdTrustPort_Type(Integer32):
    """Custom type hwWlanServiceEssNdTrustPort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssNdTrustPort_Type.__name__ = "Integer32"
_HwWlanServiceEssNdTrustPort_Object = MibTableColumn
hwWlanServiceEssNdTrustPort = _HwWlanServiceEssNdTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 53),
    _HwWlanServiceEssNdTrustPort_Type()
)
hwWlanServiceEssNdTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssNdTrustPort.setStatus("current")


class _HwWlanServiceEssMldSnoopingEable_Type(Integer32):
    """Custom type hwWlanServiceEssMldSnoopingEable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssMldSnoopingEable_Type.__name__ = "Integer32"
_HwWlanServiceEssMldSnoopingEable_Object = MibTableColumn
hwWlanServiceEssMldSnoopingEable = _HwWlanServiceEssMldSnoopingEable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 54),
    _HwWlanServiceEssMldSnoopingEable_Type()
)
hwWlanServiceEssMldSnoopingEable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssMldSnoopingEable.setStatus("current")


class _HwWlanServiceEssIPSGEnableRejectAssoc_Type(Integer32):
    """Custom type hwWlanServiceEssIPSGEnableRejectAssoc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssIPSGEnableRejectAssoc_Type.__name__ = "Integer32"
_HwWlanServiceEssIPSGEnableRejectAssoc_Object = MibTableColumn
hwWlanServiceEssIPSGEnableRejectAssoc = _HwWlanServiceEssIPSGEnableRejectAssoc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 55),
    _HwWlanServiceEssIPSGEnableRejectAssoc_Type()
)
hwWlanServiceEssIPSGEnableRejectAssoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssIPSGEnableRejectAssoc.setStatus("current")


class _HwWlanServiceEssLearnClientIpEnable_Type(Integer32):
    """Custom type hwWlanServiceEssLearnClientIpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwWlanServiceEssLearnClientIpEnable_Type.__name__ = "Integer32"
_HwWlanServiceEssLearnClientIpEnable_Object = MibTableColumn
hwWlanServiceEssLearnClientIpEnable = _HwWlanServiceEssLearnClientIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 56),
    _HwWlanServiceEssLearnClientIpEnable_Type()
)
hwWlanServiceEssLearnClientIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssLearnClientIpEnable.setStatus("current")


class _HwWlanServiceEssHomeAgent_Type(Integer32):
    """Custom type hwWlanServiceEssHomeAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("ap", 1))
    )


_HwWlanServiceEssHomeAgent_Type.__name__ = "Integer32"
_HwWlanServiceEssHomeAgent_Object = MibTableColumn
hwWlanServiceEssHomeAgent = _HwWlanServiceEssHomeAgent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 57),
    _HwWlanServiceEssHomeAgent_Type()
)
hwWlanServiceEssHomeAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssHomeAgent.setStatus("current")


class _HwWlanServiceEssVlanMobilityGroup_Type(Integer32):
    """Custom type hwWlanServiceEssVlanMobilityGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwWlanServiceEssVlanMobilityGroup_Type.__name__ = "Integer32"
_HwWlanServiceEssVlanMobilityGroup_Object = MibTableColumn
hwWlanServiceEssVlanMobilityGroup = _HwWlanServiceEssVlanMobilityGroup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 1, 1, 58),
    _HwWlanServiceEssVlanMobilityGroup_Type()
)
hwWlanServiceEssVlanMobilityGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceEssVlanMobilityGroup.setStatus("current")
_HwVapManagementTable_Object = MibTable
hwVapManagementTable = _HwVapManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2)
)
if mibBuilder.loadTexts:
    hwVapManagementTable.setStatus("current")
_HwVapManagementEntry_Object = MibTableRow
hwVapManagementEntry = _HwVapManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1)
)
hwVapManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapApIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapEssName"),
)
if mibBuilder.loadTexts:
    hwVapManagementEntry.setStatus("current")
_HwWlanServiceVapApIndex_Type = Integer32
_HwWlanServiceVapApIndex_Object = MibTableColumn
hwWlanServiceVapApIndex = _HwWlanServiceVapApIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 1),
    _HwWlanServiceVapApIndex_Type()
)
hwWlanServiceVapApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceVapApIndex.setStatus("current")
_HwWlanServiceVapRadioIndex_Type = Integer32
_HwWlanServiceVapRadioIndex_Object = MibTableColumn
hwWlanServiceVapRadioIndex = _HwWlanServiceVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 2),
    _HwWlanServiceVapRadioIndex_Type()
)
hwWlanServiceVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceVapRadioIndex.setStatus("current")


class _HwWlanServiceVapEssName_Type(OctetString):
    """Custom type hwWlanServiceVapEssName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceVapEssName_Type.__name__ = "OctetString"
_HwWlanServiceVapEssName_Object = MibTableColumn
hwWlanServiceVapEssName = _HwWlanServiceVapEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 3),
    _HwWlanServiceVapEssName_Type()
)
hwWlanServiceVapEssName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceVapEssName.setStatus("current")
_HwWlanServiceVapWlanIndex_Type = Integer32
_HwWlanServiceVapWlanIndex_Object = MibTableColumn
hwWlanServiceVapWlanIndex = _HwWlanServiceVapWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 4),
    _HwWlanServiceVapWlanIndex_Type()
)
hwWlanServiceVapWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapWlanIndex.setStatus("current")
_HwWlanServiceVapRowStatus_Type = RowStatus
_HwWlanServiceVapRowStatus_Object = MibTableColumn
hwWlanServiceVapRowStatus = _HwWlanServiceVapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 5),
    _HwWlanServiceVapRowStatus_Type()
)
hwWlanServiceVapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceVapRowStatus.setStatus("current")
_HwWlanServiceVapBssid_Type = MacAddress
_HwWlanServiceVapBssid_Object = MibTableColumn
hwWlanServiceVapBssid = _HwWlanServiceVapBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 6),
    _HwWlanServiceVapBssid_Type()
)
hwWlanServiceVapBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapBssid.setStatus("current")
_HwWlanServiceVapSSID_Type = OctetString
_HwWlanServiceVapSSID_Object = MibTableColumn
hwWlanServiceVapSSID = _HwWlanServiceVapSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 7),
    _HwWlanServiceVapSSID_Type()
)
hwWlanServiceVapSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapSSID.setStatus("current")
_HwWlanServiceVapVlan_Type = Integer32
_HwWlanServiceVapVlan_Object = MibTableColumn
hwWlanServiceVapVlan = _HwWlanServiceVapVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 8),
    _HwWlanServiceVapVlan_Type()
)
hwWlanServiceVapVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapVlan.setStatus("current")
_HwWlanServiceVapFrequency_Type = OctetString
_HwWlanServiceVapFrequency_Object = MibTableColumn
hwWlanServiceVapFrequency = _HwWlanServiceVapFrequency_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 2, 1, 9),
    _HwWlanServiceVapFrequency_Type()
)
hwWlanServiceVapFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapFrequency.setStatus("current")
_HwServiceBatchTable_Object = MibTable
hwServiceBatchTable = _HwServiceBatchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3)
)
if mibBuilder.loadTexts:
    hwServiceBatchTable.setStatus("current")
_HwServiceBatchEntry_Object = MibTableRow
hwServiceBatchEntry = _HwServiceBatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3, 1)
)
hwServiceBatchEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchApType"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchRadioIndex"),
)
if mibBuilder.loadTexts:
    hwServiceBatchEntry.setStatus("current")


class _HwWlanServiceBatchApType_Type(OctetString):
    """Custom type hwWlanServiceBatchApType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceBatchApType_Type.__name__ = "OctetString"
_HwWlanServiceBatchApType_Object = MibTableColumn
hwWlanServiceBatchApType = _HwWlanServiceBatchApType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3, 1, 1),
    _HwWlanServiceBatchApType_Type()
)
hwWlanServiceBatchApType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceBatchApType.setStatus("current")
_HwWlanServiceBatchRadioIndex_Type = Integer32
_HwWlanServiceBatchRadioIndex_Object = MibTableColumn
hwWlanServiceBatchRadioIndex = _HwWlanServiceBatchRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3, 1, 2),
    _HwWlanServiceBatchRadioIndex_Type()
)
hwWlanServiceBatchRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceBatchRadioIndex.setStatus("current")


class _HwWlanServiceBatchRadioProfileName_Type(OctetString):
    """Custom type hwWlanServiceBatchRadioProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwWlanServiceBatchRadioProfileName_Type.__name__ = "OctetString"
_HwWlanServiceBatchRadioProfileName_Object = MibTableColumn
hwWlanServiceBatchRadioProfileName = _HwWlanServiceBatchRadioProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3, 1, 3),
    _HwWlanServiceBatchRadioProfileName_Type()
)
hwWlanServiceBatchRadioProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceBatchRadioProfileName.setStatus("current")
_HwWlanServiceBatchEssNameNumber_Type = Integer32
_HwWlanServiceBatchEssNameNumber_Object = MibTableColumn
hwWlanServiceBatchEssNameNumber = _HwWlanServiceBatchEssNameNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3, 1, 4),
    _HwWlanServiceBatchEssNameNumber_Type()
)
hwWlanServiceBatchEssNameNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceBatchEssNameNumber.setStatus("current")
_HwWlanServiceBatchEssNameList_Type = OctetString
_HwWlanServiceBatchEssNameList_Object = MibTableColumn
hwWlanServiceBatchEssNameList = _HwWlanServiceBatchEssNameList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3, 1, 5),
    _HwWlanServiceBatchEssNameList_Type()
)
hwWlanServiceBatchEssNameList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwWlanServiceBatchEssNameList.setStatus("current")
_HwWlanServiceBatchRowStatus_Type = RowStatus
_HwWlanServiceBatchRowStatus_Object = MibTableColumn
hwWlanServiceBatchRowStatus = _HwWlanServiceBatchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 3, 1, 6),
    _HwWlanServiceBatchRowStatus_Type()
)
hwWlanServiceBatchRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceBatchRowStatus.setStatus("current")
_HwCapwapConfigManagementTable_Object = MibTable
hwCapwapConfigManagementTable = _HwCapwapConfigManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 4)
)
if mibBuilder.loadTexts:
    hwCapwapConfigManagementTable.setStatus("current")
_HwCapwapConfigManagementEntry_Object = MibTableRow
hwCapwapConfigManagementEntry = _HwCapwapConfigManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 4, 1)
)
hwCapwapConfigManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceCapwapConfigApIndex"),
)
if mibBuilder.loadTexts:
    hwCapwapConfigManagementEntry.setStatus("current")
_HwWlanServiceCapwapConfigApIndex_Type = Integer32
_HwWlanServiceCapwapConfigApIndex_Object = MibTableColumn
hwWlanServiceCapwapConfigApIndex = _HwWlanServiceCapwapConfigApIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 4, 1, 1),
    _HwWlanServiceCapwapConfigApIndex_Type()
)
hwWlanServiceCapwapConfigApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceCapwapConfigApIndex.setStatus("current")
_HwWlanServiceCapwapConfigCommit_Type = Integer32
_HwWlanServiceCapwapConfigCommit_Object = MibTableColumn
hwWlanServiceCapwapConfigCommit = _HwWlanServiceCapwapConfigCommit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 4, 1, 2),
    _HwWlanServiceCapwapConfigCommit_Type()
)
hwWlanServiceCapwapConfigCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceCapwapConfigCommit.setStatus("current")
_HwStationTable_Object = MibTable
hwStationTable = _HwStationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5)
)
if mibBuilder.loadTexts:
    hwStationTable.setStatus("current")
_HwStationEntry_Object = MibTableRow
hwStationEntry = _HwStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1)
)
hwStationEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaMac"),
)
if mibBuilder.loadTexts:
    hwStationEntry.setStatus("current")
_HwWlanServiceStaMac_Type = MacAddress
_HwWlanServiceStaMac_Object = MibTableColumn
hwWlanServiceStaMac = _HwWlanServiceStaMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 1),
    _HwWlanServiceStaMac_Type()
)
hwWlanServiceStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwWlanServiceStaMac.setStatus("current")
_HwWlanServiceStaApId_Type = Integer32
_HwWlanServiceStaApId_Object = MibTableColumn
hwWlanServiceStaApId = _HwWlanServiceStaApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 2),
    _HwWlanServiceStaApId_Type()
)
hwWlanServiceStaApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceStaApId.setStatus("current")
_HwWlanServiceStaRadioId_Type = Integer32
_HwWlanServiceStaRadioId_Object = MibTableColumn
hwWlanServiceStaRadioId = _HwWlanServiceStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 3),
    _HwWlanServiceStaRadioId_Type()
)
hwWlanServiceStaRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceStaRadioId.setStatus("current")
_HwWlanServiceStaEssName_Type = OctetString
_HwWlanServiceStaEssName_Object = MibTableColumn
hwWlanServiceStaEssName = _HwWlanServiceStaEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 4),
    _HwWlanServiceStaEssName_Type()
)
hwWlanServiceStaEssName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceStaEssName.setStatus("current")
_HwWlanServiceStaSsid_Type = OctetString
_HwWlanServiceStaSsid_Object = MibTableColumn
hwWlanServiceStaSsid = _HwWlanServiceStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 5),
    _HwWlanServiceStaSsid_Type()
)
hwWlanServiceStaSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceStaSsid.setStatus("current")
_HwWlanServiceStaOnlineTime_Type = Integer32
_HwWlanServiceStaOnlineTime_Object = MibTableColumn
hwWlanServiceStaOnlineTime = _HwWlanServiceStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 6),
    _HwWlanServiceStaOnlineTime_Type()
)
hwWlanServiceStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceStaOnlineTime.setStatus("current")
if mibBuilder.loadTexts:
    hwWlanServiceStaOnlineTime.setUnits("seconds")
_HwWlanServiceStaSnrUs_Type = Integer32
_HwWlanServiceStaSnrUs_Object = MibTableColumn
hwWlanServiceStaSnrUs = _HwWlanServiceStaSnrUs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 7),
    _HwWlanServiceStaSnrUs_Type()
)
hwWlanServiceStaSnrUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceStaSnrUs.setStatus("current")
if mibBuilder.loadTexts:
    hwWlanServiceStaSnrUs.setUnits("0.01 dB")
_HwWlanServiceStaRxPowerUs_Type = Integer32
_HwWlanServiceStaRxPowerUs_Object = MibTableColumn
hwWlanServiceStaRxPowerUs = _HwWlanServiceStaRxPowerUs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 8),
    _HwWlanServiceStaRxPowerUs_Type()
)
hwWlanServiceStaRxPowerUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceStaRxPowerUs.setStatus("current")
if mibBuilder.loadTexts:
    hwWlanServiceStaRxPowerUs.setUnits("0.01 dB")
_HwStaWirelessStatTxPkts_Type = Integer32
_HwStaWirelessStatTxPkts_Object = MibTableColumn
hwStaWirelessStatTxPkts = _HwStaWirelessStatTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 9),
    _HwStaWirelessStatTxPkts_Type()
)
hwStaWirelessStatTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatTxPkts.setStatus("current")
_HwStaWirelessStatRxPkts_Type = Integer32
_HwStaWirelessStatRxPkts_Object = MibTableColumn
hwStaWirelessStatRxPkts = _HwStaWirelessStatRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 10),
    _HwStaWirelessStatRxPkts_Type()
)
hwStaWirelessStatRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatRxPkts.setStatus("current")
_HwStaWirelessStatTxBytes_Type = Integer32
_HwStaWirelessStatTxBytes_Object = MibTableColumn
hwStaWirelessStatTxBytes = _HwStaWirelessStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 11),
    _HwStaWirelessStatTxBytes_Type()
)
hwStaWirelessStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatTxBytes.setStatus("current")
_HwStaWirelessStatRxBytes_Type = Integer32
_HwStaWirelessStatRxBytes_Object = MibTableColumn
hwStaWirelessStatRxBytes = _HwStaWirelessStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 12),
    _HwStaWirelessStatRxBytes_Type()
)
hwStaWirelessStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatRxBytes.setStatus("current")
_HwStaWirelessStatTxRate_Type = Integer32
_HwStaWirelessStatTxRate_Object = MibTableColumn
hwStaWirelessStatTxRate = _HwStaWirelessStatTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 13),
    _HwStaWirelessStatTxRate_Type()
)
hwStaWirelessStatTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatTxRate.setStatus("current")
if mibBuilder.loadTexts:
    hwStaWirelessStatTxRate.setUnits("bits/second")
_HwStaWirelessStatRxRate_Type = Integer32
_HwStaWirelessStatRxRate_Object = MibTableColumn
hwStaWirelessStatRxRate = _HwStaWirelessStatRxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 14),
    _HwStaWirelessStatRxRate_Type()
)
hwStaWirelessStatRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatRxRate.setStatus("current")
if mibBuilder.loadTexts:
    hwStaWirelessStatRxRate.setUnits("bits/second")
_HwStaAccessChannel_Type = Integer32
_HwStaAccessChannel_Object = MibTableColumn
hwStaAccessChannel = _HwStaAccessChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 15),
    _HwStaAccessChannel_Type()
)
hwStaAccessChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAccessChannel.setStatus("current")
_HwStaIp_Type = IpAddress
_HwStaIp_Object = MibTableColumn
hwStaIp = _HwStaIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 16),
    _HwStaIp_Type()
)
hwStaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaIp.setStatus("current")
_HwStaRssi_Type = Integer32
_HwStaRssi_Object = MibTableColumn
hwStaRssi = _HwStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 17),
    _HwStaRssi_Type()
)
hwStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaRssi.setStatus("current")
if mibBuilder.loadTexts:
    hwStaRssi.setUnits("dB")
_HwStaNoise_Type = Integer32
_HwStaNoise_Object = MibTableColumn
hwStaNoise = _HwStaNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 18),
    _HwStaNoise_Type()
)
hwStaNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaNoise.setStatus("current")
_HwStaVlan_Type = Unsigned32
_HwStaVlan_Object = MibTableColumn
hwStaVlan = _HwStaVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 19),
    _HwStaVlan_Type()
)
hwStaVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaVlan.setStatus("current")
_HwStaRecvDropFrames_Type = Counter64
_HwStaRecvDropFrames_Object = MibTableColumn
hwStaRecvDropFrames = _HwStaRecvDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 20),
    _HwStaRecvDropFrames_Type()
)
hwStaRecvDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaRecvDropFrames.setStatus("current")
_HwStaSendDropFrames_Type = Counter64
_HwStaSendDropFrames_Object = MibTableColumn
hwStaSendDropFrames = _HwStaSendDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 21),
    _HwStaSendDropFrames_Type()
)
hwStaSendDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaSendDropFrames.setStatus("current")
_HwStaRecvErrorFrames_Type = Counter64
_HwStaRecvErrorFrames_Object = MibTableColumn
hwStaRecvErrorFrames = _HwStaRecvErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 22),
    _HwStaRecvErrorFrames_Type()
)
hwStaRecvErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaRecvErrorFrames.setStatus("current")
_HwStaSendErrorFrames_Type = Counter64
_HwStaSendErrorFrames_Object = MibTableColumn
hwStaSendErrorFrames = _HwStaSendErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 23),
    _HwStaSendErrorFrames_Type()
)
hwStaSendErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaSendErrorFrames.setStatus("current")
_HwStaReSendFrames_Type = Counter64
_HwStaReSendFrames_Object = MibTableColumn
hwStaReSendFrames = _HwStaReSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 24),
    _HwStaReSendFrames_Type()
)
hwStaReSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaReSendFrames.setStatus("current")
_HwStaReSendBytes_Type = Counter64
_HwStaReSendBytes_Object = MibTableColumn
hwStaReSendBytes = _HwStaReSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 25),
    _HwStaReSendBytes_Type()
)
hwStaReSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaReSendBytes.setStatus("current")
_HwStaUsername_Type = OctetString
_HwStaUsername_Object = MibTableColumn
hwStaUsername = _HwStaUsername_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 26),
    _HwStaUsername_Type()
)
hwStaUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaUsername.setStatus("current")
_HwStaStatus_Type = Integer32
_HwStaStatus_Object = MibTableColumn
hwStaStatus = _HwStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 27),
    _HwStaStatus_Type()
)
hwStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaStatus.setStatus("current")
_HwStaWirelessStatRxBytes64Bits_Type = Counter64
_HwStaWirelessStatRxBytes64Bits_Object = MibTableColumn
hwStaWirelessStatRxBytes64Bits = _HwStaWirelessStatRxBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 28),
    _HwStaWirelessStatRxBytes64Bits_Type()
)
hwStaWirelessStatRxBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatRxBytes64Bits.setStatus("current")
_HwStaWirelessStatTxBytes64Bits_Type = Counter64
_HwStaWirelessStatTxBytes64Bits_Object = MibTableColumn
hwStaWirelessStatTxBytes64Bits = _HwStaWirelessStatTxBytes64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 29),
    _HwStaWirelessStatTxBytes64Bits_Type()
)
hwStaWirelessStatTxBytes64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatTxBytes64Bits.setStatus("current")
_HwStaGateway_Type = IpAddress
_HwStaGateway_Object = MibTableColumn
hwStaGateway = _HwStaGateway_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 30),
    _HwStaGateway_Type()
)
hwStaGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaGateway.setStatus("current")
_HwStaAuthenMethod_Type = Integer32
_HwStaAuthenMethod_Object = MibTableColumn
hwStaAuthenMethod = _HwStaAuthenMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 31),
    _HwStaAuthenMethod_Type()
)
hwStaAuthenMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthenMethod.setStatus("current")
_HwStaEncryptMethod_Type = Integer32
_HwStaEncryptMethod_Object = MibTableColumn
hwStaEncryptMethod = _HwStaEncryptMethod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 32),
    _HwStaEncryptMethod_Type()
)
hwStaEncryptMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaEncryptMethod.setStatus("current")
_HwStaBSSID_Type = MacAddress
_HwStaBSSID_Object = MibTableColumn
hwStaBSSID = _HwStaBSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 33),
    _HwStaBSSID_Type()
)
hwStaBSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaBSSID.setStatus("current")


class _HwStaQosMode_Type(Integer32):
    """Custom type hwStaQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 2),
          ("wmm", 1))
    )


_HwStaQosMode_Type.__name__ = "Integer32"
_HwStaQosMode_Object = MibTableColumn
hwStaQosMode = _HwStaQosMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 34),
    _HwStaQosMode_Type()
)
hwStaQosMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaQosMode.setStatus("current")


class _HwStaHtMode_Type(Integer32):
    """Custom type hwStaHtMode based on Integer32"""
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
        *(("ht20", 2),
          ("ht40", 1),
          ("invalid", 0),
          ("vht80", 3))
    )


_HwStaHtMode_Type.__name__ = "Integer32"
_HwStaHtMode_Object = MibTableColumn
hwStaHtMode = _HwStaHtMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 35),
    _HwStaHtMode_Type()
)
hwStaHtMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaHtMode.setStatus("current")
_HwStaMcsVal_Type = Integer32
_HwStaMcsVal_Object = MibTableColumn
hwStaMcsVal = _HwStaMcsVal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 36),
    _HwStaMcsVal_Type()
)
hwStaMcsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaMcsVal.setStatus("current")


class _HwStaShortGIStatus_Type(Integer32):
    """Custom type hwStaShortGIStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonsupport", 1),
          ("support", 2))
    )


_HwStaShortGIStatus_Type.__name__ = "Integer32"
_HwStaShortGIStatus_Object = MibTableColumn
hwStaShortGIStatus = _HwStaShortGIStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 37),
    _HwStaShortGIStatus_Type()
)
hwStaShortGIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaShortGIStatus.setStatus("current")


class _HwStaRoamStatus_Type(Integer32):
    """Custom type hwStaRoamStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_HwStaRoamStatus_Type.__name__ = "Integer32"
_HwStaRoamStatus_Object = MibTableColumn
hwStaRoamStatus = _HwStaRoamStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 38),
    _HwStaRoamStatus_Type()
)
hwStaRoamStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaRoamStatus.setStatus("current")


class _HwStaStatOperMode_Type(Integer32):
    """Custom type hwStaStatOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearstatistic", 2),
          ("invalid", 1))
    )


_HwStaStatOperMode_Type.__name__ = "Integer32"
_HwStaStatOperMode_Object = MibTableColumn
hwStaStatOperMode = _HwStaStatOperMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 39),
    _HwStaStatOperMode_Type()
)
hwStaStatOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaStatOperMode.setStatus("current")
_HwStaWirelessStatTxPkts64Bits_Type = Counter64
_HwStaWirelessStatTxPkts64Bits_Object = MibTableColumn
hwStaWirelessStatTxPkts64Bits = _HwStaWirelessStatTxPkts64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 40),
    _HwStaWirelessStatTxPkts64Bits_Type()
)
hwStaWirelessStatTxPkts64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatTxPkts64Bits.setStatus("current")
_HwStaWirelessStatRxPkts64Bits_Type = Counter64
_HwStaWirelessStatRxPkts64Bits_Object = MibTableColumn
hwStaWirelessStatRxPkts64Bits = _HwStaWirelessStatRxPkts64Bits_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 41),
    _HwStaWirelessStatRxPkts64Bits_Type()
)
hwStaWirelessStatRxPkts64Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWirelessStatRxPkts64Bits.setStatus("current")
_HwStaRfMode_Type = Integer32
_HwStaRfMode_Object = MibTableColumn
hwStaRfMode = _HwStaRfMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 42),
    _HwStaRfMode_Type()
)
hwStaRfMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaRfMode.setStatus("current")
_HwStaIpV6_Type = OctetString
_HwStaIpV6_Object = MibTableColumn
hwStaIpV6 = _HwStaIpV6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 43),
    _HwStaIpV6_Type()
)
hwStaIpV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaIpV6.setStatus("current")
_HwStaAssociateTime_Type = Integer32
_HwStaAssociateTime_Object = MibTableColumn
hwStaAssociateTime = _HwStaAssociateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 44),
    _HwStaAssociateTime_Type()
)
hwStaAssociateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAssociateTime.setStatus("current")
if mibBuilder.loadTexts:
    hwStaAssociateTime.setUnits("seconds")
_HwStaAccessTime_Type = Integer32
_HwStaAccessTime_Object = MibTableColumn
hwStaAccessTime = _HwStaAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 45),
    _HwStaAccessTime_Type()
)
hwStaAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAccessTime.setStatus("current")
if mibBuilder.loadTexts:
    hwStaAccessTime.setUnits("seconds")
_HwStaAccessOnlineTime_Type = Integer32
_HwStaAccessOnlineTime_Object = MibTableColumn
hwStaAccessOnlineTime = _HwStaAccessOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 46),
    _HwStaAccessOnlineTime_Type()
)
hwStaAccessOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAccessOnlineTime.setStatus("current")
if mibBuilder.loadTexts:
    hwStaAccessOnlineTime.setUnits("seconds")
_HwStaLinkRxRate_Type = Integer32
_HwStaLinkRxRate_Object = MibTableColumn
hwStaLinkRxRate = _HwStaLinkRxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 47),
    _HwStaLinkRxRate_Type()
)
hwStaLinkRxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaLinkRxRate.setStatus("current")
if mibBuilder.loadTexts:
    hwStaLinkRxRate.setUnits("Mbps")
_HwStaLinkTxRate_Type = Integer32
_HwStaLinkTxRate_Object = MibTableColumn
hwStaLinkTxRate = _HwStaLinkTxRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 48),
    _HwStaLinkTxRate_Type()
)
hwStaLinkTxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaLinkTxRate.setStatus("current")
if mibBuilder.loadTexts:
    hwStaLinkTxRate.setUnits("Mbps")
_HwStaActualBandwidth_Type = Unsigned32
_HwStaActualBandwidth_Object = MibTableColumn
hwStaActualBandwidth = _HwStaActualBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 49),
    _HwStaActualBandwidth_Type()
)
hwStaActualBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaActualBandwidth.setStatus("current")
_HwStaPackets_Type = Counter64
_HwStaPackets_Object = MibTableColumn
hwStaPackets = _HwStaPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 50),
    _HwStaPackets_Type()
)
hwStaPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaPackets.setStatus("current")
_HwStaChannelUtilRate_Type = Unsigned32
_HwStaChannelUtilRate_Object = MibTableColumn
hwStaChannelUtilRate = _HwStaChannelUtilRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 51),
    _HwStaChannelUtilRate_Type()
)
hwStaChannelUtilRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaChannelUtilRate.setStatus("current")
_HwStaChannelBusyRate_Type = Unsigned32
_HwStaChannelBusyRate_Object = MibTableColumn
hwStaChannelBusyRate = _HwStaChannelBusyRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 52),
    _HwStaChannelBusyRate_Type()
)
hwStaChannelBusyRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaChannelBusyRate.setStatus("current")
_HwStaChannelFreeRate_Type = Unsigned32
_HwStaChannelFreeRate_Object = MibTableColumn
hwStaChannelFreeRate = _HwStaChannelFreeRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 53),
    _HwStaChannelFreeRate_Type()
)
hwStaChannelFreeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaChannelFreeRate.setStatus("current")
_HwStaChannelInterfRate_Type = Unsigned32
_HwStaChannelInterfRate_Object = MibTableColumn
hwStaChannelInterfRate = _HwStaChannelInterfRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 5, 1, 54),
    _HwStaChannelInterfRate_Type()
)
hwStaChannelInterfRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaChannelInterfRate.setStatus("current")
_HwVapStationListTable_Object = MibTable
hwVapStationListTable = _HwVapStationListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6)
)
if mibBuilder.loadTexts:
    hwVapStationListTable.setStatus("current")
_HwVapStationListEntry_Object = MibTableRow
hwVapStationListEntry = _HwVapStationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1)
)
hwVapStationListEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapStaApId"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapStaRadioId"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapStaEssName"),
)
if mibBuilder.loadTexts:
    hwVapStationListEntry.setStatus("current")
_HwWlanServiceVapStaApId_Type = Integer32
_HwWlanServiceVapStaApId_Object = MibTableColumn
hwWlanServiceVapStaApId = _HwWlanServiceVapStaApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 1),
    _HwWlanServiceVapStaApId_Type()
)
hwWlanServiceVapStaApId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceVapStaApId.setStatus("current")
_HwWlanServiceVapStaRadioId_Type = Integer32
_HwWlanServiceVapStaRadioId_Object = MibTableColumn
hwWlanServiceVapStaRadioId = _HwWlanServiceVapStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 2),
    _HwWlanServiceVapStaRadioId_Type()
)
hwWlanServiceVapStaRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceVapStaRadioId.setStatus("current")
_HwWlanServiceVapStaEssName_Type = OctetString
_HwWlanServiceVapStaEssName_Object = MibTableColumn
hwWlanServiceVapStaEssName = _HwWlanServiceVapStaEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 3),
    _HwWlanServiceVapStaEssName_Type()
)
hwWlanServiceVapStaEssName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWlanServiceVapStaEssName.setStatus("current")
_HwWlanServiceVapStaNum_Type = Integer32
_HwWlanServiceVapStaNum_Object = MibTableColumn
hwWlanServiceVapStaNum = _HwWlanServiceVapStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 4),
    _HwWlanServiceVapStaNum_Type()
)
hwWlanServiceVapStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapStaNum.setStatus("current")
_HwWlanServiceVapStaMacList_Type = OctetString
_HwWlanServiceVapStaMacList_Object = MibTableColumn
hwWlanServiceVapStaMacList = _HwWlanServiceVapStaMacList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 5),
    _HwWlanServiceVapStaMacList_Type()
)
hwWlanServiceVapStaMacList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapStaMacList.setStatus("current")
_HwWlanServiceVapAssociatedStationCount_Type = Integer32
_HwWlanServiceVapAssociatedStationCount_Object = MibTableColumn
hwWlanServiceVapAssociatedStationCount = _HwWlanServiceVapAssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 6),
    _HwWlanServiceVapAssociatedStationCount_Type()
)
hwWlanServiceVapAssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapAssociatedStationCount.setStatus("current")
_HwWlanServiceVapCurOnlineStaCount_Type = Integer32
_HwWlanServiceVapCurOnlineStaCount_Object = MibTableColumn
hwWlanServiceVapCurOnlineStaCount = _HwWlanServiceVapCurOnlineStaCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 7),
    _HwWlanServiceVapCurOnlineStaCount_Type()
)
hwWlanServiceVapCurOnlineStaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapCurOnlineStaCount.setStatus("current")
_HwWlanServiceVapStaAssocAndReAssocReqCount_Type = Integer32
_HwWlanServiceVapStaAssocAndReAssocReqCount_Object = MibTableColumn
hwWlanServiceVapStaAssocAndReAssocReqCount = _HwWlanServiceVapStaAssocAndReAssocReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 8),
    _HwWlanServiceVapStaAssocAndReAssocReqCount_Type()
)
hwWlanServiceVapStaAssocAndReAssocReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapStaAssocAndReAssocReqCount.setStatus("current")
_HwWlanServiceVapStaOnlineTime_Type = Integer32
_HwWlanServiceVapStaOnlineTime_Object = MibTableColumn
hwWlanServiceVapStaOnlineTime = _HwWlanServiceVapStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 6, 1, 9),
    _HwWlanServiceVapStaOnlineTime_Type()
)
hwWlanServiceVapStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceVapStaOnlineTime.setStatus("current")
_HwWlanServiceBatchEssInfo_ObjectIdentity = ObjectIdentity
hwWlanServiceBatchEssInfo = _HwWlanServiceBatchEssInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 7)
)
_HwWlanServiceBatchEssStartNumber_Type = Integer32
_HwWlanServiceBatchEssStartNumber_Object = MibScalar
hwWlanServiceBatchEssStartNumber = _HwWlanServiceBatchEssStartNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 7, 1),
    _HwWlanServiceBatchEssStartNumber_Type()
)
hwWlanServiceBatchEssStartNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceBatchEssStartNumber.setStatus("current")
_HwWlanServiceBatchEssNumber_Type = Integer32
_HwWlanServiceBatchEssNumber_Object = MibScalar
hwWlanServiceBatchEssNumber = _HwWlanServiceBatchEssNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 7, 2),
    _HwWlanServiceBatchEssNumber_Type()
)
hwWlanServiceBatchEssNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwWlanServiceBatchEssNumber.setStatus("current")
_HwWlanServiceBatchReturnEssNumber_Type = Integer32
_HwWlanServiceBatchReturnEssNumber_Object = MibScalar
hwWlanServiceBatchReturnEssNumber = _HwWlanServiceBatchReturnEssNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 7, 3),
    _HwWlanServiceBatchReturnEssNumber_Type()
)
hwWlanServiceBatchReturnEssNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceBatchReturnEssNumber.setStatus("current")
_HwWlanServiceBatchEssName_Type = OctetString
_HwWlanServiceBatchEssName_Object = MibScalar
hwWlanServiceBatchEssName = _HwWlanServiceBatchEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 7, 4),
    _HwWlanServiceBatchEssName_Type()
)
hwWlanServiceBatchEssName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceBatchEssName.setStatus("current")
_HwWlanServiceBatchEssSsid_Type = OctetString
_HwWlanServiceBatchEssSsid_Object = MibScalar
hwWlanServiceBatchEssSsid = _HwWlanServiceBatchEssSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 7, 5),
    _HwWlanServiceBatchEssSsid_Type()
)
hwWlanServiceBatchEssSsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWlanServiceBatchEssSsid.setStatus("current")
_HwCapwapConfigCommitAll_Type = Integer32
_HwCapwapConfigCommitAll_Object = MibScalar
hwCapwapConfigCommitAll = _HwCapwapConfigCommitAll_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 8),
    _HwCapwapConfigCommitAll_Type()
)
hwCapwapConfigCommitAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCapwapConfigCommitAll.setStatus("current")
_HwApAssocStatTable_Object = MibTable
hwApAssocStatTable = _HwApAssocStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9)
)
if mibBuilder.loadTexts:
    hwApAssocStatTable.setStatus("current")
_HwApAssocStatEntry_Object = MibTableRow
hwApAssocStatEntry = _HwApAssocStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1)
)
hwApAssocStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwApAssocStatApId"),
)
if mibBuilder.loadTexts:
    hwApAssocStatEntry.setStatus("current")
_HwApAssocStatApId_Type = Integer32
_HwApAssocStatApId_Object = MibTableColumn
hwApAssocStatApId = _HwApAssocStatApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 1),
    _HwApAssocStatApId_Type()
)
hwApAssocStatApId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApAssocStatApId.setStatus("current")
_HwTotalOnlineTime_Type = Integer32
_HwTotalOnlineTime_Object = MibTableColumn
hwTotalOnlineTime = _HwTotalOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 2),
    _HwTotalOnlineTime_Type()
)
hwTotalOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalOnlineTime.setStatus("current")
if mibBuilder.loadTexts:
    hwTotalOnlineTime.setUnits("seconds")
_HwTotalAssociatedStationCount_Type = Integer32
_HwTotalAssociatedStationCount_Object = MibTableColumn
hwTotalAssociatedStationCount = _HwTotalAssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 3),
    _HwTotalAssociatedStationCount_Type()
)
hwTotalAssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTotalAssociatedStationCount.setStatus("current")
_HwCurrAssociatedStationCount_Type = Integer32
_HwCurrAssociatedStationCount_Object = MibTableColumn
hwCurrAssociatedStationCount = _HwCurrAssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 4),
    _HwCurrAssociatedStationCount_Type()
)
hwCurrAssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCurrAssociatedStationCount.setStatus("current")
_HwAssociationRequestCount_Type = Integer32
_HwAssociationRequestCount_Object = MibTableColumn
hwAssociationRequestCount = _HwAssociationRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 5),
    _HwAssociationRequestCount_Type()
)
hwAssociationRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociationRequestCount.setStatus("current")
_HwAssociationRejectCount_Type = Integer32
_HwAssociationRejectCount_Object = MibTableColumn
hwAssociationRejectCount = _HwAssociationRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 6),
    _HwAssociationRejectCount_Type()
)
hwAssociationRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociationRejectCount.setStatus("current")
_HwAssociationFailedCount_Type = Integer32
_HwAssociationFailedCount_Object = MibTableColumn
hwAssociationFailedCount = _HwAssociationFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 7),
    _HwAssociationFailedCount_Type()
)
hwAssociationFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssociationFailedCount.setStatus("current")
_HwReAssociationRequestCount_Type = Integer32
_HwReAssociationRequestCount_Object = MibTableColumn
hwReAssociationRequestCount = _HwReAssociationRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 8),
    _HwReAssociationRequestCount_Type()
)
hwReAssociationRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwReAssociationRequestCount.setStatus("current")
_HwReAssociationRejectCount_Type = Integer32
_HwReAssociationRejectCount_Object = MibTableColumn
hwReAssociationRejectCount = _HwReAssociationRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 9),
    _HwReAssociationRejectCount_Type()
)
hwReAssociationRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwReAssociationRejectCount.setStatus("current")
_HwReAssociationFailedCount_Type = Integer32
_HwReAssociationFailedCount_Object = MibTableColumn
hwReAssociationFailedCount = _HwReAssociationFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 10),
    _HwReAssociationFailedCount_Type()
)
hwReAssociationFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwReAssociationFailedCount.setStatus("current")
_HwDisAssocOfUserNotifiedCount_Type = Integer32
_HwDisAssocOfUserNotifiedCount_Object = MibTableColumn
hwDisAssocOfUserNotifiedCount = _HwDisAssocOfUserNotifiedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 11),
    _HwDisAssocOfUserNotifiedCount_Type()
)
hwDisAssocOfUserNotifiedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisAssocOfUserNotifiedCount.setStatus("current")
_HwDisAssocOfStaRoamCount_Type = Integer32
_HwDisAssocOfStaRoamCount_Object = MibTableColumn
hwDisAssocOfStaRoamCount = _HwDisAssocOfStaRoamCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 12),
    _HwDisAssocOfStaRoamCount_Type()
)
hwDisAssocOfStaRoamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisAssocOfStaRoamCount.setStatus("current")
_HwDisAssocOfStaAgeCount_Type = Integer32
_HwDisAssocOfStaAgeCount_Object = MibTableColumn
hwDisAssocOfStaAgeCount = _HwDisAssocOfStaAgeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 13),
    _HwDisAssocOfStaAgeCount_Type()
)
hwDisAssocOfStaAgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisAssocOfStaAgeCount.setStatus("current")
_HwDisAssocOfApUnableHandleCount_Type = Integer32
_HwDisAssocOfApUnableHandleCount_Object = MibTableColumn
hwDisAssocOfApUnableHandleCount = _HwDisAssocOfApUnableHandleCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 14),
    _HwDisAssocOfApUnableHandleCount_Type()
)
hwDisAssocOfApUnableHandleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisAssocOfApUnableHandleCount.setStatus("current")
_HwDisAssocOfOtherReasonsCount_Type = Integer32
_HwDisAssocOfOtherReasonsCount_Object = MibTableColumn
hwDisAssocOfOtherReasonsCount = _HwDisAssocOfOtherReasonsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 15),
    _HwDisAssocOfOtherReasonsCount_Type()
)
hwDisAssocOfOtherReasonsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDisAssocOfOtherReasonsCount.setStatus("current")
_HwAssocRequestCntByResource_Type = Integer32
_HwAssocRequestCntByResource_Object = MibTableColumn
hwAssocRequestCntByResource = _HwAssocRequestCntByResource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 16),
    _HwAssocRequestCntByResource_Type()
)
hwAssocRequestCntByResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAssocRequestCntByResource.setStatus("current")
_HwStaExceptionalOfflineCnt_Type = Integer32
_HwStaExceptionalOfflineCnt_Object = MibTableColumn
hwStaExceptionalOfflineCnt = _HwStaExceptionalOfflineCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 17),
    _HwStaExceptionalOfflineCnt_Type()
)
hwStaExceptionalOfflineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaExceptionalOfflineCnt.setStatus("current")
_HwReAssociationSuccessCount_Type = Integer32
_HwReAssociationSuccessCount_Object = MibTableColumn
hwReAssociationSuccessCount = _HwReAssociationSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 18),
    _HwReAssociationSuccessCount_Type()
)
hwReAssociationSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwReAssociationSuccessCount.setStatus("current")
_HwBSSNotSupportAssocFailCount_Type = Unsigned32
_HwBSSNotSupportAssocFailCount_Object = MibTableColumn
hwBSSNotSupportAssocFailCount = _HwBSSNotSupportAssocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 19),
    _HwBSSNotSupportAssocFailCount_Type()
)
hwBSSNotSupportAssocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBSSNotSupportAssocFailCount.setStatus("current")
_HwStaAccessRequestCount_Type = Unsigned32
_HwStaAccessRequestCount_Object = MibTableColumn
hwStaAccessRequestCount = _HwStaAccessRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 20),
    _HwStaAccessRequestCount_Type()
)
hwStaAccessRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAccessRequestCount.setStatus("current")
_HwStaAccessRequestFailedCount_Type = Unsigned32
_HwStaAccessRequestFailedCount_Object = MibTableColumn
hwStaAccessRequestFailedCount = _HwStaAccessRequestFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 21),
    _HwStaAccessRequestFailedCount_Type()
)
hwStaAccessRequestFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAccessRequestFailedCount.setStatus("current")
_HwStaAuthenRequestCount_Type = Unsigned32
_HwStaAuthenRequestCount_Object = MibTableColumn
hwStaAuthenRequestCount = _HwStaAuthenRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 22),
    _HwStaAuthenRequestCount_Type()
)
hwStaAuthenRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthenRequestCount.setStatus("current")
_HwStaAuthenRequestFailedCount_Type = Unsigned32
_HwStaAuthenRequestFailedCount_Object = MibTableColumn
hwStaAuthenRequestFailedCount = _HwStaAuthenRequestFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 23),
    _HwStaAuthenRequestFailedCount_Type()
)
hwStaAuthenRequestFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthenRequestFailedCount.setStatus("current")
_HwRefusedStaNumByResource_Type = Unsigned32
_HwRefusedStaNumByResource_Object = MibTableColumn
hwRefusedStaNumByResource = _HwRefusedStaNumByResource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 24),
    _HwRefusedStaNumByResource_Type()
)
hwRefusedStaNumByResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRefusedStaNumByResource.setStatus("current")
_HwStaAssocAndReAssocRequestCount_Type = Integer32
_HwStaAssocAndReAssocRequestCount_Object = MibTableColumn
hwStaAssocAndReAssocRequestCount = _HwStaAssocAndReAssocRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 25),
    _HwStaAssocAndReAssocRequestCount_Type()
)
hwStaAssocAndReAssocRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAssocAndReAssocRequestCount.setStatus("current")
_HwStaAuthenRequestSuccessCount_Type = Integer32
_HwStaAuthenRequestSuccessCount_Object = MibTableColumn
hwStaAuthenRequestSuccessCount = _HwStaAuthenRequestSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 26),
    _HwStaAuthenRequestSuccessCount_Type()
)
hwStaAuthenRequestSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaAuthenRequestSuccessCount.setStatus("current")
_HwL3RoamInStationCount_Type = Unsigned32
_HwL3RoamInStationCount_Object = MibTableColumn
hwL3RoamInStationCount = _HwL3RoamInStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 27),
    _HwL3RoamInStationCount_Type()
)
hwL3RoamInStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3RoamInStationCount.setStatus("current")
_HwL3RoamOutStationCount_Type = Unsigned32
_HwL3RoamOutStationCount_Object = MibTableColumn
hwL3RoamOutStationCount = _HwL3RoamOutStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 9, 1, 28),
    _HwL3RoamOutStationCount_Type()
)
hwL3RoamOutStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwL3RoamOutStationCount.setStatus("current")
_HwVlanMappingTable_Object = MibTable
hwVlanMappingTable = _HwVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10)
)
if mibBuilder.loadTexts:
    hwVlanMappingTable.setStatus("current")
_HwVlanMappingEntry_Object = MibTableRow
hwVlanMappingEntry = _HwVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1)
)
hwVlanMappingEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingEssName"),
)
if mibBuilder.loadTexts:
    hwVlanMappingEntry.setStatus("current")


class _HwVlanMappingEssName_Type(OctetString):
    """Custom type hwVlanMappingEssName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwVlanMappingEssName_Type.__name__ = "OctetString"
_HwVlanMappingEssName_Object = MibTableColumn
hwVlanMappingEssName = _HwVlanMappingEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 1),
    _HwVlanMappingEssName_Type()
)
hwVlanMappingEssName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwVlanMappingEssName.setStatus("current")


class _HwVlanMappingEssVlanMode_Type(Integer32):
    """Custom type hwVlanMappingEssVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apMode", 3),
          ("essMode", 1),
          ("regionMode", 2))
    )


_HwVlanMappingEssVlanMode_Type.__name__ = "Integer32"
_HwVlanMappingEssVlanMode_Object = MibTableColumn
hwVlanMappingEssVlanMode = _HwVlanMappingEssVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 2),
    _HwVlanMappingEssVlanMode_Type()
)
hwVlanMappingEssVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingEssVlanMode.setStatus("current")


class _HwVlanMappingEssVlanId_Type(Integer32):
    """Custom type hwVlanMappingEssVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
        ValueRangeConstraint(65535, 65535),
    )


_HwVlanMappingEssVlanId_Type.__name__ = "Integer32"
_HwVlanMappingEssVlanId_Object = MibTableColumn
hwVlanMappingEssVlanId = _HwVlanMappingEssVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 3),
    _HwVlanMappingEssVlanId_Type()
)
hwVlanMappingEssVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingEssVlanId.setStatus("current")


class _HwVlanMappingVlanList0_Type(OctetString):
    """Custom type hwVlanMappingVlanList0 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList0_Type.__name__ = "OctetString"
_HwVlanMappingVlanList0_Object = MibTableColumn
hwVlanMappingVlanList0 = _HwVlanMappingVlanList0_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 4),
    _HwVlanMappingVlanList0_Type()
)
hwVlanMappingVlanList0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList0.setStatus("current")


class _HwVlanMappingVlanList1_Type(OctetString):
    """Custom type hwVlanMappingVlanList1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList1_Type.__name__ = "OctetString"
_HwVlanMappingVlanList1_Object = MibTableColumn
hwVlanMappingVlanList1 = _HwVlanMappingVlanList1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 5),
    _HwVlanMappingVlanList1_Type()
)
hwVlanMappingVlanList1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList1.setStatus("current")


class _HwVlanMappingVlanList2_Type(OctetString):
    """Custom type hwVlanMappingVlanList2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList2_Type.__name__ = "OctetString"
_HwVlanMappingVlanList2_Object = MibTableColumn
hwVlanMappingVlanList2 = _HwVlanMappingVlanList2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 6),
    _HwVlanMappingVlanList2_Type()
)
hwVlanMappingVlanList2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList2.setStatus("current")


class _HwVlanMappingVlanList3_Type(OctetString):
    """Custom type hwVlanMappingVlanList3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList3_Type.__name__ = "OctetString"
_HwVlanMappingVlanList3_Object = MibTableColumn
hwVlanMappingVlanList3 = _HwVlanMappingVlanList3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 7),
    _HwVlanMappingVlanList3_Type()
)
hwVlanMappingVlanList3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList3.setStatus("current")


class _HwVlanMappingVlanList4_Type(OctetString):
    """Custom type hwVlanMappingVlanList4 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList4_Type.__name__ = "OctetString"
_HwVlanMappingVlanList4_Object = MibTableColumn
hwVlanMappingVlanList4 = _HwVlanMappingVlanList4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 8),
    _HwVlanMappingVlanList4_Type()
)
hwVlanMappingVlanList4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList4.setStatus("current")


class _HwVlanMappingVlanList5_Type(OctetString):
    """Custom type hwVlanMappingVlanList5 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList5_Type.__name__ = "OctetString"
_HwVlanMappingVlanList5_Object = MibTableColumn
hwVlanMappingVlanList5 = _HwVlanMappingVlanList5_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 9),
    _HwVlanMappingVlanList5_Type()
)
hwVlanMappingVlanList5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList5.setStatus("current")


class _HwVlanMappingVlanList6_Type(OctetString):
    """Custom type hwVlanMappingVlanList6 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList6_Type.__name__ = "OctetString"
_HwVlanMappingVlanList6_Object = MibTableColumn
hwVlanMappingVlanList6 = _HwVlanMappingVlanList6_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 10),
    _HwVlanMappingVlanList6_Type()
)
hwVlanMappingVlanList6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList6.setStatus("current")


class _HwVlanMappingVlanList7_Type(OctetString):
    """Custom type hwVlanMappingVlanList7 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 1024),
    )


_HwVlanMappingVlanList7_Type.__name__ = "OctetString"
_HwVlanMappingVlanList7_Object = MibTableColumn
hwVlanMappingVlanList7 = _HwVlanMappingVlanList7_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 10, 1, 11),
    _HwVlanMappingVlanList7_Type()
)
hwVlanMappingVlanList7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVlanMappingVlanList7.setStatus("current")
_HwGlobalStaMacWhiteListTable_Object = MibTable
hwGlobalStaMacWhiteListTable = _HwGlobalStaMacWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 11)
)
if mibBuilder.loadTexts:
    hwGlobalStaMacWhiteListTable.setStatus("current")
_HwGlobalStaMacWhiteListEntry_Object = MibTableRow
hwGlobalStaMacWhiteListEntry = _HwGlobalStaMacWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 11, 1)
)
hwGlobalStaMacWhiteListEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwStaMacWhiteListMacAddr"),
)
if mibBuilder.loadTexts:
    hwGlobalStaMacWhiteListEntry.setStatus("current")
_HwStaMacWhiteListMacAddr_Type = MacAddress
_HwStaMacWhiteListMacAddr_Object = MibTableColumn
hwStaMacWhiteListMacAddr = _HwStaMacWhiteListMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 11, 1, 1),
    _HwStaMacWhiteListMacAddr_Type()
)
hwStaMacWhiteListMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaMacWhiteListMacAddr.setStatus("current")
_HwGlobalStaMacWhiteListRowStatus_Type = RowStatus
_HwGlobalStaMacWhiteListRowStatus_Object = MibTableColumn
hwGlobalStaMacWhiteListRowStatus = _HwGlobalStaMacWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 11, 1, 2),
    _HwGlobalStaMacWhiteListRowStatus_Type()
)
hwGlobalStaMacWhiteListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwGlobalStaMacWhiteListRowStatus.setStatus("current")
_HwStaMacBlackListTable_Object = MibTable
hwStaMacBlackListTable = _HwStaMacBlackListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 12)
)
if mibBuilder.loadTexts:
    hwStaMacBlackListTable.setStatus("current")
_HwStaMacBlackListEntry_Object = MibTableRow
hwStaMacBlackListEntry = _HwStaMacBlackListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 12, 1)
)
hwStaMacBlackListEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwStaMacBlackListMacAddr"),
)
if mibBuilder.loadTexts:
    hwStaMacBlackListEntry.setStatus("current")
_HwStaMacBlackListMacAddr_Type = MacAddress
_HwStaMacBlackListMacAddr_Object = MibTableColumn
hwStaMacBlackListMacAddr = _HwStaMacBlackListMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 12, 1, 1),
    _HwStaMacBlackListMacAddr_Type()
)
hwStaMacBlackListMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaMacBlackListMacAddr.setStatus("current")
_HwStaMacBlackListRowStatus_Type = RowStatus
_HwStaMacBlackListRowStatus_Object = MibTableColumn
hwStaMacBlackListRowStatus = _HwStaMacBlackListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 12, 1, 2),
    _HwStaMacBlackListRowStatus_Type()
)
hwStaMacBlackListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaMacBlackListRowStatus.setStatus("current")
_HwApStaAccessControlTable_Object = MibTable
hwApStaAccessControlTable = _HwApStaAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 13)
)
if mibBuilder.loadTexts:
    hwApStaAccessControlTable.setStatus("current")
_HwApStaAccessControlEntry_Object = MibTableRow
hwApStaAccessControlEntry = _HwApStaAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 13, 1)
)
hwApStaAccessControlEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwApStaAccessControlApId"),
)
if mibBuilder.loadTexts:
    hwApStaAccessControlEntry.setStatus("current")
_HwApStaAccessControlApId_Type = Integer32
_HwApStaAccessControlApId_Object = MibTableColumn
hwApStaAccessControlApId = _HwApStaAccessControlApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 13, 1, 1),
    _HwApStaAccessControlApId_Type()
)
hwApStaAccessControlApId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwApStaAccessControlApId.setStatus("current")
_HwApStaAccessControlMode_Type = Integer32
_HwApStaAccessControlMode_Object = MibTableColumn
hwApStaAccessControlMode = _HwApStaAccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 13, 1, 2),
    _HwApStaAccessControlMode_Type()
)
hwApStaAccessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApStaAccessControlMode.setStatus("current")
_HwApStaAccessControlRowStatus_Type = Integer32
_HwApStaAccessControlRowStatus_Object = MibTableColumn
hwApStaAccessControlRowStatus = _HwApStaAccessControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 13, 1, 3),
    _HwApStaAccessControlRowStatus_Type()
)
hwApStaAccessControlRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaAccessControlRowStatus.setStatus("current")
_HwAcStatistics_ObjectIdentity = ObjectIdentity
hwAcStatistics = _HwAcStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14)
)
_HwAcReassocSuccessTimes_Type = Integer32
_HwAcReassocSuccessTimes_Object = MibScalar
hwAcReassocSuccessTimes = _HwAcReassocSuccessTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 1),
    _HwAcReassocSuccessTimes_Type()
)
hwAcReassocSuccessTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcReassocSuccessTimes.setStatus("current")
_HwApPerformanceStatTimerLen_Type = Integer32
_HwApPerformanceStatTimerLen_Object = MibScalar
hwApPerformanceStatTimerLen = _HwApPerformanceStatTimerLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 2),
    _HwApPerformanceStatTimerLen_Type()
)
hwApPerformanceStatTimerLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApPerformanceStatTimerLen.setStatus("current")
_HwRtCollectOnoff_Type = Integer32
_HwRtCollectOnoff_Object = MibScalar
hwRtCollectOnoff = _HwRtCollectOnoff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 3),
    _HwRtCollectOnoff_Type()
)
hwRtCollectOnoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwRtCollectOnoff.setStatus("current")
_HwApNormalCollectCycle_Type = Integer32
_HwApNormalCollectCycle_Object = MibScalar
hwApNormalCollectCycle = _HwApNormalCollectCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 4),
    _HwApNormalCollectCycle_Type()
)
hwApNormalCollectCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApNormalCollectCycle.setStatus("current")
_HwApRtCollectCycle_Type = Integer32
_HwApRtCollectCycle_Object = MibScalar
hwApRtCollectCycle = _HwApRtCollectCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 5),
    _HwApRtCollectCycle_Type()
)
hwApRtCollectCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwApRtCollectCycle.setStatus("current")
_HwAcCurAssocStaNum_Type = Integer32
_HwAcCurAssocStaNum_Object = MibScalar
hwAcCurAssocStaNum = _HwAcCurAssocStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 6),
    _HwAcCurAssocStaNum_Type()
)
hwAcCurAssocStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcCurAssocStaNum.setStatus("current")
_HwAcCurAuthSuccessStaNum_Type = Integer32
_HwAcCurAuthSuccessStaNum_Object = MibScalar
hwAcCurAuthSuccessStaNum = _HwAcCurAuthSuccessStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 7),
    _HwAcCurAuthSuccessStaNum_Type()
)
hwAcCurAuthSuccessStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcCurAuthSuccessStaNum.setStatus("current")
_HwAcCurJointApNum_Type = Integer32
_HwAcCurJointApNum_Object = MibScalar
hwAcCurJointApNum = _HwAcCurJointApNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 8),
    _HwAcCurJointApNum_Type()
)
hwAcCurJointApNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAcCurJointApNum.setStatus("current")
_HwAcCurAssoc24gStaNum_Type = Integer32
_HwAcCurAssoc24gStaNum_Object = MibScalar
hwAcCurAssoc24gStaNum = _HwAcCurAssoc24gStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 9),
    _HwAcCurAssoc24gStaNum_Type()
)
hwAcCurAssoc24gStaNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAcCurAssoc24gStaNum.setStatus("current")
_HwAcCurAssoc5gStaNum_Type = Integer32
_HwAcCurAssoc5gStaNum_Object = MibScalar
hwAcCurAssoc5gStaNum = _HwAcCurAssoc5gStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 14, 10),
    _HwAcCurAssoc5gStaNum_Type()
)
hwAcCurAssoc5gStaNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwAcCurAssoc5gStaNum.setStatus("current")
_HwMacVapManagementTable_Object = MibTable
hwMacVapManagementTable = _HwMacVapManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15)
)
if mibBuilder.loadTexts:
    hwMacVapManagementTable.setStatus("current")
_HwMacVapManagementEntry_Object = MibTableRow
hwMacVapManagementEntry = _HwMacVapManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1)
)
hwMacVapManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapEssName"),
)
if mibBuilder.loadTexts:
    hwMacVapManagementEntry.setStatus("current")
_HwMacWlanServiceVapApMac_Type = MacAddress
_HwMacWlanServiceVapApMac_Object = MibTableColumn
hwMacWlanServiceVapApMac = _HwMacWlanServiceVapApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 1),
    _HwMacWlanServiceVapApMac_Type()
)
hwMacWlanServiceVapApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapApMac.setStatus("current")
_HwMacWlanServiceVapRadioIndex_Type = Integer32
_HwMacWlanServiceVapRadioIndex_Object = MibTableColumn
hwMacWlanServiceVapRadioIndex = _HwMacWlanServiceVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 2),
    _HwMacWlanServiceVapRadioIndex_Type()
)
hwMacWlanServiceVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapRadioIndex.setStatus("current")


class _HwMacWlanServiceVapEssName_Type(OctetString):
    """Custom type hwMacWlanServiceVapEssName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacWlanServiceVapEssName_Type.__name__ = "OctetString"
_HwMacWlanServiceVapEssName_Object = MibTableColumn
hwMacWlanServiceVapEssName = _HwMacWlanServiceVapEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 3),
    _HwMacWlanServiceVapEssName_Type()
)
hwMacWlanServiceVapEssName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapEssName.setStatus("current")
_HwMacWlanServiceVapWlanIndex_Type = Integer32
_HwMacWlanServiceVapWlanIndex_Object = MibTableColumn
hwMacWlanServiceVapWlanIndex = _HwMacWlanServiceVapWlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 4),
    _HwMacWlanServiceVapWlanIndex_Type()
)
hwMacWlanServiceVapWlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapWlanIndex.setStatus("current")
_HwMacWlanServiceVapBssid_Type = MacAddress
_HwMacWlanServiceVapBssid_Object = MibTableColumn
hwMacWlanServiceVapBssid = _HwMacWlanServiceVapBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 5),
    _HwMacWlanServiceVapBssid_Type()
)
hwMacWlanServiceVapBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapBssid.setStatus("current")
_HwMacWlanServiceVapRowStatus_Type = RowStatus
_HwMacWlanServiceVapRowStatus_Object = MibTableColumn
hwMacWlanServiceVapRowStatus = _HwMacWlanServiceVapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 6),
    _HwMacWlanServiceVapRowStatus_Type()
)
hwMacWlanServiceVapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapRowStatus.setStatus("current")
_HwMacWlanServiceVapSSID_Type = OctetString
_HwMacWlanServiceVapSSID_Object = MibTableColumn
hwMacWlanServiceVapSSID = _HwMacWlanServiceVapSSID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 7),
    _HwMacWlanServiceVapSSID_Type()
)
hwMacWlanServiceVapSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapSSID.setStatus("current")
_HwMacWlanServiceVapVlan_Type = Integer32
_HwMacWlanServiceVapVlan_Object = MibTableColumn
hwMacWlanServiceVapVlan = _HwMacWlanServiceVapVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 15, 1, 8),
    _HwMacWlanServiceVapVlan_Type()
)
hwMacWlanServiceVapVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapVlan.setStatus("current")
_HwMacCapwapConfigManagementTable_Object = MibTable
hwMacCapwapConfigManagementTable = _HwMacCapwapConfigManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 16)
)
if mibBuilder.loadTexts:
    hwMacCapwapConfigManagementTable.setStatus("current")
_HwMacCapwapConfigManagementEntry_Object = MibTableRow
hwMacCapwapConfigManagementEntry = _HwMacCapwapConfigManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 16, 1)
)
hwMacCapwapConfigManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceCapwapConfigApMac"),
)
if mibBuilder.loadTexts:
    hwMacCapwapConfigManagementEntry.setStatus("current")
_HwMacWlanServiceCapwapConfigApMac_Type = MacAddress
_HwMacWlanServiceCapwapConfigApMac_Object = MibTableColumn
hwMacWlanServiceCapwapConfigApMac = _HwMacWlanServiceCapwapConfigApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 16, 1, 1),
    _HwMacWlanServiceCapwapConfigApMac_Type()
)
hwMacWlanServiceCapwapConfigApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacWlanServiceCapwapConfigApMac.setStatus("current")
_HwMacWlanServiceCapwapConfigCommit_Type = Integer32
_HwMacWlanServiceCapwapConfigCommit_Object = MibTableColumn
hwMacWlanServiceCapwapConfigCommit = _HwMacWlanServiceCapwapConfigCommit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 16, 1, 2),
    _HwMacWlanServiceCapwapConfigCommit_Type()
)
hwMacWlanServiceCapwapConfigCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacWlanServiceCapwapConfigCommit.setStatus("current")
_HwMacVapStationListTable_Object = MibTable
hwMacVapStationListTable = _HwMacVapStationListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17)
)
if mibBuilder.loadTexts:
    hwMacVapStationListTable.setStatus("current")
_HwMacVapStationListEntry_Object = MibTableRow
hwMacVapStationListEntry = _HwMacVapStationListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1)
)
hwMacVapStationListEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaRadioId"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaEssName"),
)
if mibBuilder.loadTexts:
    hwMacVapStationListEntry.setStatus("current")
_HwMacWlanServiceVapStaApMac_Type = MacAddress
_HwMacWlanServiceVapStaApMac_Object = MibTableColumn
hwMacWlanServiceVapStaApMac = _HwMacWlanServiceVapStaApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 1),
    _HwMacWlanServiceVapStaApMac_Type()
)
hwMacWlanServiceVapStaApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapStaApMac.setStatus("current")
_HwMacWlanServiceVapStaRadioId_Type = Integer32
_HwMacWlanServiceVapStaRadioId_Object = MibTableColumn
hwMacWlanServiceVapStaRadioId = _HwMacWlanServiceVapStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 2),
    _HwMacWlanServiceVapStaRadioId_Type()
)
hwMacWlanServiceVapStaRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapStaRadioId.setStatus("current")
_HwMacWlanServiceVapStaEssName_Type = OctetString
_HwMacWlanServiceVapStaEssName_Object = MibTableColumn
hwMacWlanServiceVapStaEssName = _HwMacWlanServiceVapStaEssName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 3),
    _HwMacWlanServiceVapStaEssName_Type()
)
hwMacWlanServiceVapStaEssName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapStaEssName.setStatus("current")
_HwMacWlanServiceVapStaNum_Type = Integer32
_HwMacWlanServiceVapStaNum_Object = MibTableColumn
hwMacWlanServiceVapStaNum = _HwMacWlanServiceVapStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 4),
    _HwMacWlanServiceVapStaNum_Type()
)
hwMacWlanServiceVapStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapStaNum.setStatus("current")
_HwMacWlanServiceVapStaMacList_Type = OctetString
_HwMacWlanServiceVapStaMacList_Object = MibTableColumn
hwMacWlanServiceVapStaMacList = _HwMacWlanServiceVapStaMacList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 5),
    _HwMacWlanServiceVapStaMacList_Type()
)
hwMacWlanServiceVapStaMacList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapStaMacList.setStatus("current")
_HwMacWlanServiceVapAssociatedStationCount_Type = Integer32
_HwMacWlanServiceVapAssociatedStationCount_Object = MibTableColumn
hwMacWlanServiceVapAssociatedStationCount = _HwMacWlanServiceVapAssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 6),
    _HwMacWlanServiceVapAssociatedStationCount_Type()
)
hwMacWlanServiceVapAssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapAssociatedStationCount.setStatus("current")
_HwMacWlanServiceVapCurOnlineStaCount_Type = Integer32
_HwMacWlanServiceVapCurOnlineStaCount_Object = MibTableColumn
hwMacWlanServiceVapCurOnlineStaCount = _HwMacWlanServiceVapCurOnlineStaCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 7),
    _HwMacWlanServiceVapCurOnlineStaCount_Type()
)
hwMacWlanServiceVapCurOnlineStaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapCurOnlineStaCount.setStatus("current")
_HwMacWlanServiceVapStaAssocAndReAssocReqCount_Type = Integer32
_HwMacWlanServiceVapStaAssocAndReAssocReqCount_Object = MibTableColumn
hwMacWlanServiceVapStaAssocAndReAssocReqCount = _HwMacWlanServiceVapStaAssocAndReAssocReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 8),
    _HwMacWlanServiceVapStaAssocAndReAssocReqCount_Type()
)
hwMacWlanServiceVapStaAssocAndReAssocReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapStaAssocAndReAssocReqCount.setStatus("current")
_HwMacWlanServiceVapStaOnlineTime_Type = Integer32
_HwMacWlanServiceVapStaOnlineTime_Object = MibTableColumn
hwMacWlanServiceVapStaOnlineTime = _HwMacWlanServiceVapStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 17, 1, 9),
    _HwMacWlanServiceVapStaOnlineTime_Type()
)
hwMacWlanServiceVapStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacWlanServiceVapStaOnlineTime.setStatus("current")
_HwMacApAssocStatTable_Object = MibTable
hwMacApAssocStatTable = _HwMacApAssocStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18)
)
if mibBuilder.loadTexts:
    hwMacApAssocStatTable.setStatus("current")
_HwMacApAssocStatEntry_Object = MibTableRow
hwMacApAssocStatEntry = _HwMacApAssocStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1)
)
hwMacApAssocStatEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacApAssocStatApMac"),
)
if mibBuilder.loadTexts:
    hwMacApAssocStatEntry.setStatus("current")
_HwMacApAssocStatApMac_Type = MacAddress
_HwMacApAssocStatApMac_Object = MibTableColumn
hwMacApAssocStatApMac = _HwMacApAssocStatApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 1),
    _HwMacApAssocStatApMac_Type()
)
hwMacApAssocStatApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApAssocStatApMac.setStatus("current")
_HwMacTotalOnlineTime_Type = Unsigned32
_HwMacTotalOnlineTime_Object = MibTableColumn
hwMacTotalOnlineTime = _HwMacTotalOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 2),
    _HwMacTotalOnlineTime_Type()
)
hwMacTotalOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacTotalOnlineTime.setStatus("current")
_HwMacTotalAssociatedStationCount_Type = Unsigned32
_HwMacTotalAssociatedStationCount_Object = MibTableColumn
hwMacTotalAssociatedStationCount = _HwMacTotalAssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 3),
    _HwMacTotalAssociatedStationCount_Type()
)
hwMacTotalAssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacTotalAssociatedStationCount.setStatus("current")
_HwMacCurrAssociatedStationCount_Type = Unsigned32
_HwMacCurrAssociatedStationCount_Object = MibTableColumn
hwMacCurrAssociatedStationCount = _HwMacCurrAssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 4),
    _HwMacCurrAssociatedStationCount_Type()
)
hwMacCurrAssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacCurrAssociatedStationCount.setStatus("current")
_HwMacAssociationRequestCount_Type = Unsigned32
_HwMacAssociationRequestCount_Object = MibTableColumn
hwMacAssociationRequestCount = _HwMacAssociationRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 5),
    _HwMacAssociationRequestCount_Type()
)
hwMacAssociationRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAssociationRequestCount.setStatus("current")
_HwMacAssociationRejectCount_Type = Unsigned32
_HwMacAssociationRejectCount_Object = MibTableColumn
hwMacAssociationRejectCount = _HwMacAssociationRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 6),
    _HwMacAssociationRejectCount_Type()
)
hwMacAssociationRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAssociationRejectCount.setStatus("current")
_HwMacAssociationFailedCount_Type = Unsigned32
_HwMacAssociationFailedCount_Object = MibTableColumn
hwMacAssociationFailedCount = _HwMacAssociationFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 7),
    _HwMacAssociationFailedCount_Type()
)
hwMacAssociationFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAssociationFailedCount.setStatus("current")
_HwMacReAssociationRequestCount_Type = Unsigned32
_HwMacReAssociationRequestCount_Object = MibTableColumn
hwMacReAssociationRequestCount = _HwMacReAssociationRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 8),
    _HwMacReAssociationRequestCount_Type()
)
hwMacReAssociationRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacReAssociationRequestCount.setStatus("current")
_HwMacReAssociationRejectCount_Type = Unsigned32
_HwMacReAssociationRejectCount_Object = MibTableColumn
hwMacReAssociationRejectCount = _HwMacReAssociationRejectCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 9),
    _HwMacReAssociationRejectCount_Type()
)
hwMacReAssociationRejectCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacReAssociationRejectCount.setStatus("current")
_HwMacReAssociationFailedCount_Type = Unsigned32
_HwMacReAssociationFailedCount_Object = MibTableColumn
hwMacReAssociationFailedCount = _HwMacReAssociationFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 10),
    _HwMacReAssociationFailedCount_Type()
)
hwMacReAssociationFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacReAssociationFailedCount.setStatus("current")
_HwMacDisAssocOfUserNotifiedCount_Type = Unsigned32
_HwMacDisAssocOfUserNotifiedCount_Object = MibTableColumn
hwMacDisAssocOfUserNotifiedCount = _HwMacDisAssocOfUserNotifiedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 11),
    _HwMacDisAssocOfUserNotifiedCount_Type()
)
hwMacDisAssocOfUserNotifiedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacDisAssocOfUserNotifiedCount.setStatus("current")
_HwMacDisAssocOfStaRoamCount_Type = Unsigned32
_HwMacDisAssocOfStaRoamCount_Object = MibTableColumn
hwMacDisAssocOfStaRoamCount = _HwMacDisAssocOfStaRoamCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 12),
    _HwMacDisAssocOfStaRoamCount_Type()
)
hwMacDisAssocOfStaRoamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacDisAssocOfStaRoamCount.setStatus("current")
_HwMacDisAssocOfStaAgeCount_Type = Unsigned32
_HwMacDisAssocOfStaAgeCount_Object = MibTableColumn
hwMacDisAssocOfStaAgeCount = _HwMacDisAssocOfStaAgeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 13),
    _HwMacDisAssocOfStaAgeCount_Type()
)
hwMacDisAssocOfStaAgeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacDisAssocOfStaAgeCount.setStatus("current")
_HwMacDisAssocOfApUnableHandleCount_Type = Unsigned32
_HwMacDisAssocOfApUnableHandleCount_Object = MibTableColumn
hwMacDisAssocOfApUnableHandleCount = _HwMacDisAssocOfApUnableHandleCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 14),
    _HwMacDisAssocOfApUnableHandleCount_Type()
)
hwMacDisAssocOfApUnableHandleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacDisAssocOfApUnableHandleCount.setStatus("current")
_HwMacDisAssocOfOtherReasonsCount_Type = Unsigned32
_HwMacDisAssocOfOtherReasonsCount_Object = MibTableColumn
hwMacDisAssocOfOtherReasonsCount = _HwMacDisAssocOfOtherReasonsCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 15),
    _HwMacDisAssocOfOtherReasonsCount_Type()
)
hwMacDisAssocOfOtherReasonsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacDisAssocOfOtherReasonsCount.setStatus("current")
_HwMacAssocRequestCntByResource_Type = Unsigned32
_HwMacAssocRequestCntByResource_Object = MibTableColumn
hwMacAssocRequestCntByResource = _HwMacAssocRequestCntByResource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 16),
    _HwMacAssocRequestCntByResource_Type()
)
hwMacAssocRequestCntByResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAssocRequestCntByResource.setStatus("current")
_HwMacStaExceptionalOfflineCnt_Type = Unsigned32
_HwMacStaExceptionalOfflineCnt_Object = MibTableColumn
hwMacStaExceptionalOfflineCnt = _HwMacStaExceptionalOfflineCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 17),
    _HwMacStaExceptionalOfflineCnt_Type()
)
hwMacStaExceptionalOfflineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaExceptionalOfflineCnt.setStatus("current")
_HwMacReAssociationSuccessCount_Type = Unsigned32
_HwMacReAssociationSuccessCount_Object = MibTableColumn
hwMacReAssociationSuccessCount = _HwMacReAssociationSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 18),
    _HwMacReAssociationSuccessCount_Type()
)
hwMacReAssociationSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacReAssociationSuccessCount.setStatus("current")
_HwMacBSSNotSupportAssocFailCount_Type = Unsigned32
_HwMacBSSNotSupportAssocFailCount_Object = MibTableColumn
hwMacBSSNotSupportAssocFailCount = _HwMacBSSNotSupportAssocFailCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 19),
    _HwMacBSSNotSupportAssocFailCount_Type()
)
hwMacBSSNotSupportAssocFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBSSNotSupportAssocFailCount.setStatus("current")
_HwMacStaAccessRequestCount_Type = Unsigned32
_HwMacStaAccessRequestCount_Object = MibTableColumn
hwMacStaAccessRequestCount = _HwMacStaAccessRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 20),
    _HwMacStaAccessRequestCount_Type()
)
hwMacStaAccessRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaAccessRequestCount.setStatus("current")
_HwMacStaAccessRequestFailedCount_Type = Unsigned32
_HwMacStaAccessRequestFailedCount_Object = MibTableColumn
hwMacStaAccessRequestFailedCount = _HwMacStaAccessRequestFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 21),
    _HwMacStaAccessRequestFailedCount_Type()
)
hwMacStaAccessRequestFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaAccessRequestFailedCount.setStatus("current")
_HwMacStaAuthenRequestCount_Type = Unsigned32
_HwMacStaAuthenRequestCount_Object = MibTableColumn
hwMacStaAuthenRequestCount = _HwMacStaAuthenRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 22),
    _HwMacStaAuthenRequestCount_Type()
)
hwMacStaAuthenRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaAuthenRequestCount.setStatus("current")
_HwMacStaAuthenRequestFailedCount_Type = Unsigned32
_HwMacStaAuthenRequestFailedCount_Object = MibTableColumn
hwMacStaAuthenRequestFailedCount = _HwMacStaAuthenRequestFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 23),
    _HwMacStaAuthenRequestFailedCount_Type()
)
hwMacStaAuthenRequestFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaAuthenRequestFailedCount.setStatus("current")
_HwMacRefusedStaNumByResource_Type = Unsigned32
_HwMacRefusedStaNumByResource_Object = MibTableColumn
hwMacRefusedStaNumByResource = _HwMacRefusedStaNumByResource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 24),
    _HwMacRefusedStaNumByResource_Type()
)
hwMacRefusedStaNumByResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRefusedStaNumByResource.setStatus("current")
_HwMacStaAssocAndReAssocRequestCount_Type = Integer32
_HwMacStaAssocAndReAssocRequestCount_Object = MibTableColumn
hwMacStaAssocAndReAssocRequestCount = _HwMacStaAssocAndReAssocRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 25),
    _HwMacStaAssocAndReAssocRequestCount_Type()
)
hwMacStaAssocAndReAssocRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaAssocAndReAssocRequestCount.setStatus("current")
_HwMacStaAuthenRequestSuccessCount_Type = Integer32
_HwMacStaAuthenRequestSuccessCount_Object = MibTableColumn
hwMacStaAuthenRequestSuccessCount = _HwMacStaAuthenRequestSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 26),
    _HwMacStaAuthenRequestSuccessCount_Type()
)
hwMacStaAuthenRequestSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaAuthenRequestSuccessCount.setStatus("current")
_HwMacL3RoamInStationCount_Type = Unsigned32
_HwMacL3RoamInStationCount_Object = MibTableColumn
hwMacL3RoamInStationCount = _HwMacL3RoamInStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 27),
    _HwMacL3RoamInStationCount_Type()
)
hwMacL3RoamInStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacL3RoamInStationCount.setStatus("current")
_HwMacL3RoamOutStationCount_Type = Unsigned32
_HwMacL3RoamOutStationCount_Object = MibTableColumn
hwMacL3RoamOutStationCount = _HwMacL3RoamOutStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 18, 1, 28),
    _HwMacL3RoamOutStationCount_Type()
)
hwMacL3RoamOutStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacL3RoamOutStationCount.setStatus("current")
_HwVapConfigTable_Object = MibTable
hwVapConfigTable = _HwVapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 19)
)
if mibBuilder.loadTexts:
    hwVapConfigTable.setStatus("current")
_HwVapConfigEntry_Object = MibTableRow
hwVapConfigEntry = _HwVapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 19, 1)
)
hwVapConfigEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaRadioId"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaEssName"),
)
if mibBuilder.loadTexts:
    hwVapConfigEntry.setStatus("current")


class _HwVapOptValue_Type(Integer32):
    """Custom type hwVapOptValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwVapOptValue_Type.__name__ = "Integer32"
_HwVapOptValue_Object = MibTableColumn
hwVapOptValue = _HwVapOptValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 19, 1, 1),
    _HwVapOptValue_Type()
)
hwVapOptValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVapOptValue.setStatus("current")
_HwSsidStatisticTable_Object = MibTable
hwSsidStatisticTable = _HwSsidStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20)
)
if mibBuilder.loadTexts:
    hwSsidStatisticTable.setStatus("current")
_HwSsidStatisticEntry_Object = MibTableRow
hwSsidStatisticEntry = _HwSsidStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1)
)
hwSsidStatisticEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwSsidStatisticApIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwSsidStatisticRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwSsidStatisticEssSsid"),
)
if mibBuilder.loadTexts:
    hwSsidStatisticEntry.setStatus("current")
_HwSsidStatisticApIndex_Type = Integer32
_HwSsidStatisticApIndex_Object = MibTableColumn
hwSsidStatisticApIndex = _HwSsidStatisticApIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 1),
    _HwSsidStatisticApIndex_Type()
)
hwSsidStatisticApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSsidStatisticApIndex.setStatus("current")
_HwSsidStatisticRadioIndex_Type = Integer32
_HwSsidStatisticRadioIndex_Object = MibTableColumn
hwSsidStatisticRadioIndex = _HwSsidStatisticRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 2),
    _HwSsidStatisticRadioIndex_Type()
)
hwSsidStatisticRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSsidStatisticRadioIndex.setStatus("current")
_HwSsidStatisticEssSsid_Type = OctetString
_HwSsidStatisticEssSsid_Object = MibTableColumn
hwSsidStatisticEssSsid = _HwSsidStatisticEssSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 3),
    _HwSsidStatisticEssSsid_Type()
)
hwSsidStatisticEssSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSsidStatisticEssSsid.setStatus("current")
_HwSsidAirportRecvBytes_Type = Counter64
_HwSsidAirportRecvBytes_Object = MibTableColumn
hwSsidAirportRecvBytes = _HwSsidAirportRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 4),
    _HwSsidAirportRecvBytes_Type()
)
hwSsidAirportRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportRecvBytes.setStatus("current")
_HwSsidAirportRecvErrorFrames_Type = Counter64
_HwSsidAirportRecvErrorFrames_Object = MibTableColumn
hwSsidAirportRecvErrorFrames = _HwSsidAirportRecvErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 5),
    _HwSsidAirportRecvErrorFrames_Type()
)
hwSsidAirportRecvErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportRecvErrorFrames.setStatus("current")
_HwSsidAirportRecvFrames_Type = Counter64
_HwSsidAirportRecvFrames_Object = MibTableColumn
hwSsidAirportRecvFrames = _HwSsidAirportRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 6),
    _HwSsidAirportRecvFrames_Type()
)
hwSsidAirportRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportRecvFrames.setStatus("current")
_HwSsidAirportRecvUnicastFrames_Type = Counter64
_HwSsidAirportRecvUnicastFrames_Object = MibTableColumn
hwSsidAirportRecvUnicastFrames = _HwSsidAirportRecvUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 7),
    _HwSsidAirportRecvUnicastFrames_Type()
)
hwSsidAirportRecvUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportRecvUnicastFrames.setStatus("current")
_HwSsidAirportRecvDropFrames_Type = Counter64
_HwSsidAirportRecvDropFrames_Object = MibTableColumn
hwSsidAirportRecvDropFrames = _HwSsidAirportRecvDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 8),
    _HwSsidAirportRecvDropFrames_Type()
)
hwSsidAirportRecvDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportRecvDropFrames.setStatus("current")
_HwSsidAirportTransmitBytes_Type = Counter64
_HwSsidAirportTransmitBytes_Object = MibTableColumn
hwSsidAirportTransmitBytes = _HwSsidAirportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 9),
    _HwSsidAirportTransmitBytes_Type()
)
hwSsidAirportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportTransmitBytes.setStatus("current")
_HwSsidAirportTransmitErrorFrames_Type = Counter64
_HwSsidAirportTransmitErrorFrames_Object = MibTableColumn
hwSsidAirportTransmitErrorFrames = _HwSsidAirportTransmitErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 10),
    _HwSsidAirportTransmitErrorFrames_Type()
)
hwSsidAirportTransmitErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportTransmitErrorFrames.setStatus("current")
_HwSsidAirportTransmitFrames_Type = Counter64
_HwSsidAirportTransmitFrames_Object = MibTableColumn
hwSsidAirportTransmitFrames = _HwSsidAirportTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 11),
    _HwSsidAirportTransmitFrames_Type()
)
hwSsidAirportTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportTransmitFrames.setStatus("current")
_HwSsidAirportTransmitUnicastFrames_Type = Counter64
_HwSsidAirportTransmitUnicastFrames_Object = MibTableColumn
hwSsidAirportTransmitUnicastFrames = _HwSsidAirportTransmitUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 12),
    _HwSsidAirportTransmitUnicastFrames_Type()
)
hwSsidAirportTransmitUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportTransmitUnicastFrames.setStatus("current")
_HwSsidAirportTransmitDropFrames_Type = Counter64
_HwSsidAirportTransmitDropFrames_Object = MibTableColumn
hwSsidAirportTransmitDropFrames = _HwSsidAirportTransmitDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 13),
    _HwSsidAirportTransmitDropFrames_Type()
)
hwSsidAirportTransmitDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportTransmitDropFrames.setStatus("current")
_HwSsidAirportDownReTransmitFrames_Type = Counter64
_HwSsidAirportDownReTransmitFrames_Object = MibTableColumn
hwSsidAirportDownReTransmitFrames = _HwSsidAirportDownReTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 14),
    _HwSsidAirportDownReTransmitFrames_Type()
)
hwSsidAirportDownReTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportDownReTransmitFrames.setStatus("current")
_HwSsidCurrentStaNum_Type = Unsigned32
_HwSsidCurrentStaNum_Object = MibTableColumn
hwSsidCurrentStaNum = _HwSsidCurrentStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 15),
    _HwSsidCurrentStaNum_Type()
)
hwSsidCurrentStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidCurrentStaNum.setStatus("current")
_HwSsidAirportNoise_Type = Integer32
_HwSsidAirportNoise_Object = MibTableColumn
hwSsidAirportNoise = _HwSsidAirportNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 16),
    _HwSsidAirportNoise_Type()
)
hwSsidAirportNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportNoise.setStatus("current")
_HwSsidAirportSNR_Type = Integer32
_HwSsidAirportSNR_Object = MibTableColumn
hwSsidAirportSNR = _HwSsidAirportSNR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 20, 1, 17),
    _HwSsidAirportSNR_Type()
)
hwSsidAirportSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSsidAirportSNR.setStatus("current")
_HwMacSsidStatisticTable_Object = MibTable
hwMacSsidStatisticTable = _HwMacSsidStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21)
)
if mibBuilder.loadTexts:
    hwMacSsidStatisticTable.setStatus("current")
_HwMacSsidStatisticEntry_Object = MibTableRow
hwMacSsidStatisticEntry = _HwMacSsidStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1)
)
hwMacSsidStatisticEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidStatisticApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidStatisticRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidStatisticEssSsid"),
)
if mibBuilder.loadTexts:
    hwMacSsidStatisticEntry.setStatus("current")
_HwMacSsidStatisticApMac_Type = MacAddress
_HwMacSsidStatisticApMac_Object = MibTableColumn
hwMacSsidStatisticApMac = _HwMacSsidStatisticApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 1),
    _HwMacSsidStatisticApMac_Type()
)
hwMacSsidStatisticApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacSsidStatisticApMac.setStatus("current")
_HwMacSsidStatisticRadioIndex_Type = Integer32
_HwMacSsidStatisticRadioIndex_Object = MibTableColumn
hwMacSsidStatisticRadioIndex = _HwMacSsidStatisticRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 2),
    _HwMacSsidStatisticRadioIndex_Type()
)
hwMacSsidStatisticRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacSsidStatisticRadioIndex.setStatus("current")
_HwMacSsidStatisticEssSsid_Type = OctetString
_HwMacSsidStatisticEssSsid_Object = MibTableColumn
hwMacSsidStatisticEssSsid = _HwMacSsidStatisticEssSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 3),
    _HwMacSsidStatisticEssSsid_Type()
)
hwMacSsidStatisticEssSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacSsidStatisticEssSsid.setStatus("current")
_HwMacSsidAirportRecvBytes_Type = Counter64
_HwMacSsidAirportRecvBytes_Object = MibTableColumn
hwMacSsidAirportRecvBytes = _HwMacSsidAirportRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 4),
    _HwMacSsidAirportRecvBytes_Type()
)
hwMacSsidAirportRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportRecvBytes.setStatus("current")
_HwMacSsidAirportRecvErrorFrames_Type = Counter64
_HwMacSsidAirportRecvErrorFrames_Object = MibTableColumn
hwMacSsidAirportRecvErrorFrames = _HwMacSsidAirportRecvErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 5),
    _HwMacSsidAirportRecvErrorFrames_Type()
)
hwMacSsidAirportRecvErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportRecvErrorFrames.setStatus("current")
_HwMacSsidAirportRecvFrames_Type = Counter64
_HwMacSsidAirportRecvFrames_Object = MibTableColumn
hwMacSsidAirportRecvFrames = _HwMacSsidAirportRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 6),
    _HwMacSsidAirportRecvFrames_Type()
)
hwMacSsidAirportRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportRecvFrames.setStatus("current")
_HwMacSsidAirportRecvUnicastFrames_Type = Counter64
_HwMacSsidAirportRecvUnicastFrames_Object = MibTableColumn
hwMacSsidAirportRecvUnicastFrames = _HwMacSsidAirportRecvUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 7),
    _HwMacSsidAirportRecvUnicastFrames_Type()
)
hwMacSsidAirportRecvUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportRecvUnicastFrames.setStatus("current")
_HwMacSsidAirportRecvDropFrames_Type = Counter64
_HwMacSsidAirportRecvDropFrames_Object = MibTableColumn
hwMacSsidAirportRecvDropFrames = _HwMacSsidAirportRecvDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 8),
    _HwMacSsidAirportRecvDropFrames_Type()
)
hwMacSsidAirportRecvDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportRecvDropFrames.setStatus("current")
_HwMacSsidAirportTransmitBytes_Type = Counter64
_HwMacSsidAirportTransmitBytes_Object = MibTableColumn
hwMacSsidAirportTransmitBytes = _HwMacSsidAirportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 9),
    _HwMacSsidAirportTransmitBytes_Type()
)
hwMacSsidAirportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportTransmitBytes.setStatus("current")
_HwMacSsidAirportTransmitErrorFrames_Type = Counter64
_HwMacSsidAirportTransmitErrorFrames_Object = MibTableColumn
hwMacSsidAirportTransmitErrorFrames = _HwMacSsidAirportTransmitErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 10),
    _HwMacSsidAirportTransmitErrorFrames_Type()
)
hwMacSsidAirportTransmitErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportTransmitErrorFrames.setStatus("current")
_HwMacSsidAirportTransmitFrames_Type = Counter64
_HwMacSsidAirportTransmitFrames_Object = MibTableColumn
hwMacSsidAirportTransmitFrames = _HwMacSsidAirportTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 11),
    _HwMacSsidAirportTransmitFrames_Type()
)
hwMacSsidAirportTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportTransmitFrames.setStatus("current")
_HwMacSsidAirportTransmitUnicastFrames_Type = Counter64
_HwMacSsidAirportTransmitUnicastFrames_Object = MibTableColumn
hwMacSsidAirportTransmitUnicastFrames = _HwMacSsidAirportTransmitUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 12),
    _HwMacSsidAirportTransmitUnicastFrames_Type()
)
hwMacSsidAirportTransmitUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportTransmitUnicastFrames.setStatus("current")
_HwMacSsidAirportTransmitDropFrames_Type = Counter64
_HwMacSsidAirportTransmitDropFrames_Object = MibTableColumn
hwMacSsidAirportTransmitDropFrames = _HwMacSsidAirportTransmitDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 13),
    _HwMacSsidAirportTransmitDropFrames_Type()
)
hwMacSsidAirportTransmitDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportTransmitDropFrames.setStatus("current")
_HwMacSsidAirportDownReTransmitFrames_Type = Counter64
_HwMacSsidAirportDownReTransmitFrames_Object = MibTableColumn
hwMacSsidAirportDownReTransmitFrames = _HwMacSsidAirportDownReTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 14),
    _HwMacSsidAirportDownReTransmitFrames_Type()
)
hwMacSsidAirportDownReTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportDownReTransmitFrames.setStatus("current")
_HwMacSsidCurrentStaNum_Type = Unsigned32
_HwMacSsidCurrentStaNum_Object = MibTableColumn
hwMacSsidCurrentStaNum = _HwMacSsidCurrentStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 15),
    _HwMacSsidCurrentStaNum_Type()
)
hwMacSsidCurrentStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidCurrentStaNum.setStatus("current")
_HwMacSsidAirportNoise_Type = Integer32
_HwMacSsidAirportNoise_Object = MibTableColumn
hwMacSsidAirportNoise = _HwMacSsidAirportNoise_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 16),
    _HwMacSsidAirportNoise_Type()
)
hwMacSsidAirportNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportNoise.setStatus("current")
_HwMacSsidAirportSNR_Type = Integer32
_HwMacSsidAirportSNR_Object = MibTableColumn
hwMacSsidAirportSNR = _HwMacSsidAirportSNR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 21, 1, 17),
    _HwMacSsidAirportSNR_Type()
)
hwMacSsidAirportSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacSsidAirportSNR.setStatus("current")
_HwMacApStaAccessControlTable_Object = MibTable
hwMacApStaAccessControlTable = _HwMacApStaAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 22)
)
if mibBuilder.loadTexts:
    hwMacApStaAccessControlTable.setStatus("current")
_HwMacApStaAccessControlEntry_Object = MibTableRow
hwMacApStaAccessControlEntry = _HwMacApStaAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 22, 1)
)
hwMacApStaAccessControlEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaAccessControlApMac"),
)
if mibBuilder.loadTexts:
    hwMacApStaAccessControlEntry.setStatus("current")
_HwMacApStaAccessControlApMac_Type = MacAddress
_HwMacApStaAccessControlApMac_Object = MibTableColumn
hwMacApStaAccessControlApMac = _HwMacApStaAccessControlApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 22, 1, 1),
    _HwMacApStaAccessControlApMac_Type()
)
hwMacApStaAccessControlApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacApStaAccessControlApMac.setStatus("current")
_HwMacApStaAccessControlMode_Type = Integer32
_HwMacApStaAccessControlMode_Object = MibTableColumn
hwMacApStaAccessControlMode = _HwMacApStaAccessControlMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 22, 1, 2),
    _HwMacApStaAccessControlMode_Type()
)
hwMacApStaAccessControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacApStaAccessControlMode.setStatus("current")
_HwMacApStaAccessControlRowStatus_Type = Integer32
_HwMacApStaAccessControlRowStatus_Object = MibTableColumn
hwMacApStaAccessControlRowStatus = _HwMacApStaAccessControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 22, 1, 3),
    _HwMacApStaAccessControlRowStatus_Type()
)
hwMacApStaAccessControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMacApStaAccessControlRowStatus.setStatus("current")
_HwApStaInfoTable_Object = MibTable
hwApStaInfoTable = _HwApStaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23)
)
if mibBuilder.loadTexts:
    hwApStaInfoTable.setStatus("current")
_HwApStaInfoEntry_Object = MibTableRow
hwApStaInfoEntry = _HwApStaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1)
)
hwApStaInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaApId"),
)
if mibBuilder.loadTexts:
    hwApStaInfoEntry.setStatus("current")
_HwStaMAC_Type = OctetString
_HwStaMAC_Object = MibTableColumn
hwStaMAC = _HwStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 1),
    _HwStaMAC_Type()
)
hwStaMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaMAC.setStatus("current")
_HwStaIPAddress_Type = OctetString
_HwStaIPAddress_Object = MibTableColumn
hwStaIPAddress = _HwStaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 2),
    _HwStaIPAddress_Type()
)
hwStaIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaIPAddress.setStatus("current")
_HwStaWMMAttr_Type = OctetString
_HwStaWMMAttr_Object = MibTableColumn
hwStaWMMAttr = _HwStaWMMAttr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 3),
    _HwStaWMMAttr_Type()
)
hwStaWMMAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWMMAttr.setStatus("current")
_HwStaRadioMode_Type = OctetString
_HwStaRadioMode_Object = MibTableColumn
hwStaRadioMode = _HwStaRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 4),
    _HwStaRadioMode_Type()
)
hwStaRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaRadioMode.setStatus("current")
_HwStaRadioChannel_Type = OctetString
_HwStaRadioChannel_Object = MibTableColumn
hwStaRadioChannel = _HwStaRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 5),
    _HwStaRadioChannel_Type()
)
hwStaRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaRadioChannel.setStatus("current")
_HwAPTxRates_Type = OctetString
_HwAPTxRates_Object = MibTableColumn
hwAPTxRates = _HwAPTxRates_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 6),
    _HwAPTxRates_Type()
)
hwAPTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAPTxRates.setStatus("current")
_HwStaPowerSaveMode_Type = OctetString
_HwStaPowerSaveMode_Object = MibTableColumn
hwStaPowerSaveMode = _HwStaPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 7),
    _HwStaPowerSaveMode_Type()
)
hwStaPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaPowerSaveMode.setStatus("current")
_HwStaVlanId_Type = OctetString
_HwStaVlanId_Object = MibTableColumn
hwStaVlanId = _HwStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 8),
    _HwStaVlanId_Type()
)
hwStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaVlanId.setStatus("current")
_HwStaSSIDName_Type = OctetString
_HwStaSSIDName_Object = MibTableColumn
hwStaSSIDName = _HwStaSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 9),
    _HwStaSSIDName_Type()
)
hwStaSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaSSIDName.setStatus("current")
_HwApStaTxPacket_Type = OctetString
_HwApStaTxPacket_Object = MibTableColumn
hwApStaTxPacket = _HwApStaTxPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 10),
    _HwApStaTxPacket_Type()
)
hwApStaTxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaTxPacket.setStatus("current")
_HwApStaRxPacket_Type = OctetString
_HwApStaRxPacket_Object = MibTableColumn
hwApStaRxPacket = _HwApStaRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 11),
    _HwApStaRxPacket_Type()
)
hwApStaRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaRxPacket.setStatus("current")
_HwApStaStatus_Type = OctetString
_HwApStaStatus_Object = MibTableColumn
hwApStaStatus = _HwApStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 12),
    _HwApStaStatus_Type()
)
hwApStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaStatus.setStatus("current")
_HwApStaBssid_Type = OctetString
_HwApStaBssid_Object = MibTableColumn
hwApStaBssid = _HwApStaBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 13),
    _HwApStaBssid_Type()
)
hwApStaBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaBssid.setStatus("current")
_HwApStaRssi_Type = OctetString
_HwApStaRssi_Object = MibTableColumn
hwApStaRssi = _HwApStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 14),
    _HwApStaRssi_Type()
)
hwApStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaRssi.setStatus("current")
_HwApStaSnr_Type = OctetString
_HwApStaSnr_Object = MibTableColumn
hwApStaSnr = _HwApStaSnr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 23, 1, 15),
    _HwApStaSnr_Type()
)
hwApStaSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwApStaSnr.setStatus("current")
_HwMacApStaInfoTable_Object = MibTable
hwMacApStaInfoTable = _HwMacApStaInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24)
)
if mibBuilder.loadTexts:
    hwMacApStaInfoTable.setStatus("current")
_HwMacApStaInfoEntry_Object = MibTableRow
hwMacApStaInfoEntry = _HwMacApStaInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1)
)
hwMacApStaInfoEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaApMac"),
)
if mibBuilder.loadTexts:
    hwMacApStaInfoEntry.setStatus("current")
_HwMacStaMAC_Type = OctetString
_HwMacStaMAC_Object = MibTableColumn
hwMacStaMAC = _HwMacStaMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 1),
    _HwMacStaMAC_Type()
)
hwMacStaMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaMAC.setStatus("current")
_HwMacStaIPAddress_Type = OctetString
_HwMacStaIPAddress_Object = MibTableColumn
hwMacStaIPAddress = _HwMacStaIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 2),
    _HwMacStaIPAddress_Type()
)
hwMacStaIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaIPAddress.setStatus("current")
_HwMacStaWMMAttr_Type = OctetString
_HwMacStaWMMAttr_Object = MibTableColumn
hwMacStaWMMAttr = _HwMacStaWMMAttr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 3),
    _HwMacStaWMMAttr_Type()
)
hwMacStaWMMAttr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaWMMAttr.setStatus("current")
_HwMacStaRadioMode_Type = OctetString
_HwMacStaRadioMode_Object = MibTableColumn
hwMacStaRadioMode = _HwMacStaRadioMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 4),
    _HwMacStaRadioMode_Type()
)
hwMacStaRadioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaRadioMode.setStatus("current")
_HwMacStaRadioChannel_Type = OctetString
_HwMacStaRadioChannel_Object = MibTableColumn
hwMacStaRadioChannel = _HwMacStaRadioChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 5),
    _HwMacStaRadioChannel_Type()
)
hwMacStaRadioChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaRadioChannel.setStatus("current")
_HwMacAPTxRates_Type = OctetString
_HwMacAPTxRates_Object = MibTableColumn
hwMacAPTxRates = _HwMacAPTxRates_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 6),
    _HwMacAPTxRates_Type()
)
hwMacAPTxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacAPTxRates.setStatus("current")
_HwMacStaPowerSaveMode_Type = OctetString
_HwMacStaPowerSaveMode_Object = MibTableColumn
hwMacStaPowerSaveMode = _HwMacStaPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 7),
    _HwMacStaPowerSaveMode_Type()
)
hwMacStaPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaPowerSaveMode.setStatus("current")
_HwMacStaVlanId_Type = OctetString
_HwMacStaVlanId_Object = MibTableColumn
hwMacStaVlanId = _HwMacStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 8),
    _HwMacStaVlanId_Type()
)
hwMacStaVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaVlanId.setStatus("current")
_HwMacStaSSIDName_Type = OctetString
_HwMacStaSSIDName_Object = MibTableColumn
hwMacStaSSIDName = _HwMacStaSSIDName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 9),
    _HwMacStaSSIDName_Type()
)
hwMacStaSSIDName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacStaSSIDName.setStatus("current")
_HwMacApStaTxPacket_Type = OctetString
_HwMacApStaTxPacket_Object = MibTableColumn
hwMacApStaTxPacket = _HwMacApStaTxPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 10),
    _HwMacApStaTxPacket_Type()
)
hwMacApStaTxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApStaTxPacket.setStatus("current")
_HwMacApStaRxPacket_Type = OctetString
_HwMacApStaRxPacket_Object = MibTableColumn
hwMacApStaRxPacket = _HwMacApStaRxPacket_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 11),
    _HwMacApStaRxPacket_Type()
)
hwMacApStaRxPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApStaRxPacket.setStatus("current")
_HwMacApStaStatus_Type = OctetString
_HwMacApStaStatus_Object = MibTableColumn
hwMacApStaStatus = _HwMacApStaStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 12),
    _HwMacApStaStatus_Type()
)
hwMacApStaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApStaStatus.setStatus("current")
_HwMacApStaBssid_Type = OctetString
_HwMacApStaBssid_Object = MibTableColumn
hwMacApStaBssid = _HwMacApStaBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 13),
    _HwMacApStaBssid_Type()
)
hwMacApStaBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApStaBssid.setStatus("current")
_HwMacApStaRssi_Type = OctetString
_HwMacApStaRssi_Object = MibTableColumn
hwMacApStaRssi = _HwMacApStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 14),
    _HwMacApStaRssi_Type()
)
hwMacApStaRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApStaRssi.setStatus("current")
_HwMacApStaSnr_Type = OctetString
_HwMacApStaSnr_Object = MibTableColumn
hwMacApStaSnr = _HwMacApStaSnr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 24, 1, 15),
    _HwMacApStaSnr_Type()
)
hwMacApStaSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacApStaSnr.setStatus("current")
_HwInterACRoamingInfo_ObjectIdentity = ObjectIdentity
hwInterACRoamingInfo = _HwInterACRoamingInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 25)
)
_HwInterACRoamingInSuccCnt_Type = Integer32
_HwInterACRoamingInSuccCnt_Object = MibScalar
hwInterACRoamingInSuccCnt = _HwInterACRoamingInSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 25, 1),
    _HwInterACRoamingInSuccCnt_Type()
)
hwInterACRoamingInSuccCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwInterACRoamingInSuccCnt.setStatus("current")
_HwInterACRoamingOutSuccCnt_Type = Integer32
_HwInterACRoamingOutSuccCnt_Object = MibScalar
hwInterACRoamingOutSuccCnt = _HwInterACRoamingOutSuccCnt_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 25, 2),
    _HwInterACRoamingOutSuccCnt_Type()
)
hwInterACRoamingOutSuccCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwInterACRoamingOutSuccCnt.setStatus("current")
_HwRadioStaListTable_Object = MibTable
hwRadioStaListTable = _HwRadioStaListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26)
)
if mibBuilder.loadTexts:
    hwRadioStaListTable.setStatus("current")
_HwRadioStaListEntry_Object = MibTableRow
hwRadioStaListEntry = _HwRadioStaListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26, 1)
)
hwRadioStaListEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwRadioStaApId"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwRadioStaRadioId"),
)
if mibBuilder.loadTexts:
    hwRadioStaListEntry.setStatus("current")
_HwRadioStaApId_Type = Unsigned32
_HwRadioStaApId_Object = MibTableColumn
hwRadioStaApId = _HwRadioStaApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26, 1, 1),
    _HwRadioStaApId_Type()
)
hwRadioStaApId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRadioStaApId.setStatus("current")
_HwRadioStaRadioId_Type = Unsigned32
_HwRadioStaRadioId_Object = MibTableColumn
hwRadioStaRadioId = _HwRadioStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26, 1, 2),
    _HwRadioStaRadioId_Type()
)
hwRadioStaRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRadioStaRadioId.setStatus("current")
_HwRadioStaNumber_Type = Unsigned32
_HwRadioStaNumber_Object = MibTableColumn
hwRadioStaNumber = _HwRadioStaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26, 1, 3),
    _HwRadioStaNumber_Type()
)
hwRadioStaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaNumber.setStatus("current")
_HwRadioStaMacList_Type = OctetString
_HwRadioStaMacList_Object = MibTableColumn
hwRadioStaMacList = _HwRadioStaMacList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26, 1, 4),
    _HwRadioStaMacList_Type()
)
hwRadioStaMacList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaMacList.setStatus("current")
_HwRadioStaTotalAssociatedCount_Type = Integer32
_HwRadioStaTotalAssociatedCount_Object = MibTableColumn
hwRadioStaTotalAssociatedCount = _HwRadioStaTotalAssociatedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26, 1, 5),
    _HwRadioStaTotalAssociatedCount_Type()
)
hwRadioStaTotalAssociatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaTotalAssociatedCount.setStatus("current")
_HwRadioStaAccessReqCount_Type = Integer32
_HwRadioStaAccessReqCount_Object = MibTableColumn
hwRadioStaAccessReqCount = _HwRadioStaAccessReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 26, 1, 6),
    _HwRadioStaAccessReqCount_Type()
)
hwRadioStaAccessReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRadioStaAccessReqCount.setStatus("current")
_HwMacRadioStaListTable_Object = MibTable
hwMacRadioStaListTable = _HwMacRadioStaListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27)
)
if mibBuilder.loadTexts:
    hwMacRadioStaListTable.setStatus("current")
_HwMacRadioStaListEntry_Object = MibTableRow
hwMacRadioStaListEntry = _HwMacRadioStaListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27, 1)
)
hwMacRadioStaListEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacRadioStaApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacRadioStaRadioId"),
)
if mibBuilder.loadTexts:
    hwMacRadioStaListEntry.setStatus("current")
_HwMacRadioStaApMac_Type = MacAddress
_HwMacRadioStaApMac_Object = MibTableColumn
hwMacRadioStaApMac = _HwMacRadioStaApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27, 1, 1),
    _HwMacRadioStaApMac_Type()
)
hwMacRadioStaApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacRadioStaApMac.setStatus("current")
_HwMacRadioStaRadioId_Type = Unsigned32
_HwMacRadioStaRadioId_Object = MibTableColumn
hwMacRadioStaRadioId = _HwMacRadioStaRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27, 1, 2),
    _HwMacRadioStaRadioId_Type()
)
hwMacRadioStaRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacRadioStaRadioId.setStatus("current")
_HwMacRadioStaNumber_Type = Unsigned32
_HwMacRadioStaNumber_Object = MibTableColumn
hwMacRadioStaNumber = _HwMacRadioStaNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27, 1, 3),
    _HwMacRadioStaNumber_Type()
)
hwMacRadioStaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioStaNumber.setStatus("current")
_HwMacRadioStaMacList_Type = OctetString
_HwMacRadioStaMacList_Object = MibTableColumn
hwMacRadioStaMacList = _HwMacRadioStaMacList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27, 1, 4),
    _HwMacRadioStaMacList_Type()
)
hwMacRadioStaMacList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioStaMacList.setStatus("current")
_HwMacRadioStaTotalAssociatedCount_Type = Integer32
_HwMacRadioStaTotalAssociatedCount_Object = MibTableColumn
hwMacRadioStaTotalAssociatedCount = _HwMacRadioStaTotalAssociatedCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27, 1, 5),
    _HwMacRadioStaTotalAssociatedCount_Type()
)
hwMacRadioStaTotalAssociatedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioStaTotalAssociatedCount.setStatus("current")
_HwMacRadioStaAccessReqCount_Type = Integer32
_HwMacRadioStaAccessReqCount_Object = MibTableColumn
hwMacRadioStaAccessReqCount = _HwMacRadioStaAccessReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 27, 1, 6),
    _HwMacRadioStaAccessReqCount_Type()
)
hwMacRadioStaAccessReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacRadioStaAccessReqCount.setStatus("current")
_HwBridgeProfileTable_Object = MibTable
hwBridgeProfileTable = _HwBridgeProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28)
)
if mibBuilder.loadTexts:
    hwBridgeProfileTable.setStatus("current")
_HwBridgeProfileEntry_Object = MibTableRow
hwBridgeProfileEntry = _HwBridgeProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1)
)
hwBridgeProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeProfileName"),
)
if mibBuilder.loadTexts:
    hwBridgeProfileEntry.setStatus("current")


class _HwBridgeProfileName_Type(OctetString):
    """Custom type hwBridgeProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBridgeProfileName_Type.__name__ = "OctetString"
_HwBridgeProfileName_Object = MibTableColumn
hwBridgeProfileName = _HwBridgeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1, 1),
    _HwBridgeProfileName_Type()
)
hwBridgeProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBridgeProfileName.setStatus("current")


class _HwBridgeProfileBridgeName_Type(OctetString):
    """Custom type hwBridgeProfileBridgeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwBridgeProfileBridgeName_Type.__name__ = "OctetString"
_HwBridgeProfileBridgeName_Object = MibTableColumn
hwBridgeProfileBridgeName = _HwBridgeProfileBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1, 2),
    _HwBridgeProfileBridgeName_Type()
)
hwBridgeProfileBridgeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBridgeProfileBridgeName.setStatus("current")


class _HwBridgeProfileSecurityProfileName_Type(OctetString):
    """Custom type hwBridgeProfileSecurityProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBridgeProfileSecurityProfileName_Type.__name__ = "OctetString"
_HwBridgeProfileSecurityProfileName_Object = MibTableColumn
hwBridgeProfileSecurityProfileName = _HwBridgeProfileSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1, 3),
    _HwBridgeProfileSecurityProfileName_Type()
)
hwBridgeProfileSecurityProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBridgeProfileSecurityProfileName.setStatus("current")


class _HwBridgeProfileVlanTagged_Type(OctetString):
    """Custom type hwBridgeProfileVlanTagged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4094),
    )


_HwBridgeProfileVlanTagged_Type.__name__ = "OctetString"
_HwBridgeProfileVlanTagged_Object = MibTableColumn
hwBridgeProfileVlanTagged = _HwBridgeProfileVlanTagged_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1, 4),
    _HwBridgeProfileVlanTagged_Type()
)
hwBridgeProfileVlanTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBridgeProfileVlanTagged.setStatus("current")
_HwBridgeProfileRowStatus_Type = RowStatus
_HwBridgeProfileRowStatus_Object = MibTableColumn
hwBridgeProfileRowStatus = _HwBridgeProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1, 5),
    _HwBridgeProfileRowStatus_Type()
)
hwBridgeProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBridgeProfileRowStatus.setStatus("current")


class _HwBridgeProfileDhcpTrustPort_Type(Integer32):
    """Custom type hwBridgeProfileDhcpTrustPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwBridgeProfileDhcpTrustPort_Type.__name__ = "Integer32"
_HwBridgeProfileDhcpTrustPort_Object = MibTableColumn
hwBridgeProfileDhcpTrustPort = _HwBridgeProfileDhcpTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1, 6),
    _HwBridgeProfileDhcpTrustPort_Type()
)
hwBridgeProfileDhcpTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBridgeProfileDhcpTrustPort.setStatus("current")


class _HwBridgeProfileNdTrustPort_Type(Integer32):
    """Custom type hwBridgeProfileNdTrustPort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwBridgeProfileNdTrustPort_Type.__name__ = "Integer32"
_HwBridgeProfileNdTrustPort_Object = MibTableColumn
hwBridgeProfileNdTrustPort = _HwBridgeProfileNdTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 28, 1, 7),
    _HwBridgeProfileNdTrustPort_Type()
)
hwBridgeProfileNdTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBridgeProfileNdTrustPort.setStatus("current")
_HwBridgeVapManagementTable_Object = MibTable
hwBridgeVapManagementTable = _HwBridgeVapManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 29)
)
if mibBuilder.loadTexts:
    hwBridgeVapManagementTable.setStatus("current")
_HwBridgeVapManagementEntry_Object = MibTableRow
hwBridgeVapManagementEntry = _HwBridgeVapManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 29, 1)
)
hwBridgeVapManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeVapApIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeVapBridgeProfileName"),
)
if mibBuilder.loadTexts:
    hwBridgeVapManagementEntry.setStatus("current")
_HwBridgeVapApIndex_Type = Integer32
_HwBridgeVapApIndex_Object = MibTableColumn
hwBridgeVapApIndex = _HwBridgeVapApIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 29, 1, 1),
    _HwBridgeVapApIndex_Type()
)
hwBridgeVapApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBridgeVapApIndex.setStatus("current")
_HwBridgeVapRadioIndex_Type = Integer32
_HwBridgeVapRadioIndex_Object = MibTableColumn
hwBridgeVapRadioIndex = _HwBridgeVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 29, 1, 2),
    _HwBridgeVapRadioIndex_Type()
)
hwBridgeVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBridgeVapRadioIndex.setStatus("current")


class _HwBridgeVapBridgeProfileName_Type(OctetString):
    """Custom type hwBridgeVapBridgeProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBridgeVapBridgeProfileName_Type.__name__ = "OctetString"
_HwBridgeVapBridgeProfileName_Object = MibTableColumn
hwBridgeVapBridgeProfileName = _HwBridgeVapBridgeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 29, 1, 3),
    _HwBridgeVapBridgeProfileName_Type()
)
hwBridgeVapBridgeProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBridgeVapBridgeProfileName.setStatus("current")
_HwBridgeVapRowStatus_Type = RowStatus
_HwBridgeVapRowStatus_Object = MibTableColumn
hwBridgeVapRowStatus = _HwBridgeVapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 29, 1, 4),
    _HwBridgeVapRowStatus_Type()
)
hwBridgeVapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBridgeVapRowStatus.setStatus("current")
_HwBridgeVapBssid_Type = OctetString
_HwBridgeVapBssid_Object = MibTableColumn
hwBridgeVapBssid = _HwBridgeVapBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 29, 1, 5),
    _HwBridgeVapBssid_Type()
)
hwBridgeVapBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeVapBssid.setStatus("current")
_HwMacBridgeVapManagementTable_Object = MibTable
hwMacBridgeVapManagementTable = _HwMacBridgeVapManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 30)
)
if mibBuilder.loadTexts:
    hwMacBridgeVapManagementTable.setStatus("current")
_HwMacBridgeVapManagementEntry_Object = MibTableRow
hwMacBridgeVapManagementEntry = _HwMacBridgeVapManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 30, 1)
)
hwMacBridgeVapManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeVapApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeVapBridgeProfileName"),
)
if mibBuilder.loadTexts:
    hwMacBridgeVapManagementEntry.setStatus("current")
_HwMacBridgeVapApMac_Type = MacAddress
_HwMacBridgeVapApMac_Object = MibTableColumn
hwMacBridgeVapApMac = _HwMacBridgeVapApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 30, 1, 1),
    _HwMacBridgeVapApMac_Type()
)
hwMacBridgeVapApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacBridgeVapApMac.setStatus("current")
_HwMacBridgeVapRadioIndex_Type = Integer32
_HwMacBridgeVapRadioIndex_Object = MibTableColumn
hwMacBridgeVapRadioIndex = _HwMacBridgeVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 30, 1, 2),
    _HwMacBridgeVapRadioIndex_Type()
)
hwMacBridgeVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacBridgeVapRadioIndex.setStatus("current")


class _HwMacBridgeVapBridgeProfileName_Type(OctetString):
    """Custom type hwMacBridgeVapBridgeProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacBridgeVapBridgeProfileName_Type.__name__ = "OctetString"
_HwMacBridgeVapBridgeProfileName_Object = MibTableColumn
hwMacBridgeVapBridgeProfileName = _HwMacBridgeVapBridgeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 30, 1, 3),
    _HwMacBridgeVapBridgeProfileName_Type()
)
hwMacBridgeVapBridgeProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacBridgeVapBridgeProfileName.setStatus("current")
_HwMacBridgeVapRowStatus_Type = RowStatus
_HwMacBridgeVapRowStatus_Object = MibTableColumn
hwMacBridgeVapRowStatus = _HwMacBridgeVapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 30, 1, 4),
    _HwMacBridgeVapRowStatus_Type()
)
hwMacBridgeVapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacBridgeVapRowStatus.setStatus("current")
_HwMacBridgeVapBssid_Type = OctetString
_HwMacBridgeVapBssid_Object = MibTableColumn
hwMacBridgeVapBssid = _HwMacBridgeVapBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 30, 1, 5),
    _HwMacBridgeVapBssid_Type()
)
hwMacBridgeVapBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeVapBssid.setStatus("current")
_HwBridgeLinkTable_Object = MibTable
hwBridgeLinkTable = _HwBridgeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31)
)
if mibBuilder.loadTexts:
    hwBridgeLinkTable.setStatus("current")
_HwBridgeLinkEntry_Object = MibTableRow
hwBridgeLinkEntry = _HwBridgeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1)
)
hwBridgeLinkEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeVapApIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkIndex"),
)
if mibBuilder.loadTexts:
    hwBridgeLinkEntry.setStatus("current")
_HwBridgeLinkIndex_Type = Integer32
_HwBridgeLinkIndex_Object = MibTableColumn
hwBridgeLinkIndex = _HwBridgeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 1),
    _HwBridgeLinkIndex_Type()
)
hwBridgeLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBridgeLinkIndex.setStatus("current")
_HwBridgeLinkWlanID_Type = Integer32
_HwBridgeLinkWlanID_Object = MibTableColumn
hwBridgeLinkWlanID = _HwBridgeLinkWlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 2),
    _HwBridgeLinkWlanID_Type()
)
hwBridgeLinkWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkWlanID.setStatus("current")
_HwBridgeLinkBridgeType_Type = Integer32
_HwBridgeLinkBridgeType_Object = MibTableColumn
hwBridgeLinkBridgeType = _HwBridgeLinkBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 3),
    _HwBridgeLinkBridgeType_Type()
)
hwBridgeLinkBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkBridgeType.setStatus("current")
_HwBridgeLinkBridgeSubType_Type = Integer32
_HwBridgeLinkBridgeSubType_Object = MibTableColumn
hwBridgeLinkBridgeSubType = _HwBridgeLinkBridgeSubType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 4),
    _HwBridgeLinkBridgeSubType_Type()
)
hwBridgeLinkBridgeSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkBridgeSubType.setStatus("current")
_HwBridgeLinkPeerMac_Type = MacAddress
_HwBridgeLinkPeerMac_Object = MibTableColumn
hwBridgeLinkPeerMac = _HwBridgeLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 5),
    _HwBridgeLinkPeerMac_Type()
)
hwBridgeLinkPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkPeerMac.setStatus("current")


class _HwBridgeLinkBridgeProfileName_Type(OctetString):
    """Custom type hwBridgeLinkBridgeProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwBridgeLinkBridgeProfileName_Type.__name__ = "OctetString"
_HwBridgeLinkBridgeProfileName_Object = MibTableColumn
hwBridgeLinkBridgeProfileName = _HwBridgeLinkBridgeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 6),
    _HwBridgeLinkBridgeProfileName_Type()
)
hwBridgeLinkBridgeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkBridgeProfileName.setStatus("current")
_HwBridgeLinkStpMode_Type = Integer32
_HwBridgeLinkStpMode_Object = MibTableColumn
hwBridgeLinkStpMode = _HwBridgeLinkStpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 7),
    _HwBridgeLinkStpMode_Type()
)
hwBridgeLinkStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkStpMode.setStatus("current")
_HwBridgeLinkInstanceIdList_Type = OctetString
_HwBridgeLinkInstanceIdList_Object = MibTableColumn
hwBridgeLinkInstanceIdList = _HwBridgeLinkInstanceIdList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 8),
    _HwBridgeLinkInstanceIdList_Type()
)
hwBridgeLinkInstanceIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkInstanceIdList.setStatus("current")
_HwBridgeLinkInstanceStateList_Type = OctetString
_HwBridgeLinkInstanceStateList_Object = MibTableColumn
hwBridgeLinkInstanceStateList = _HwBridgeLinkInstanceStateList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 9),
    _HwBridgeLinkInstanceStateList_Type()
)
hwBridgeLinkInstanceStateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkInstanceStateList.setStatus("current")
_HwBridgeLinkApMac_Type = MacAddress
_HwBridgeLinkApMac_Object = MibTableColumn
hwBridgeLinkApMac = _HwBridgeLinkApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 10),
    _HwBridgeLinkApMac_Type()
)
hwBridgeLinkApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkApMac.setStatus("current")


class _HwBridgeLinkBridgeMode_Type(Integer32):
    """Custom type hwBridgeLinkBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 3),
          ("middle", 1),
          ("root", 2))
    )


_HwBridgeLinkBridgeMode_Type.__name__ = "Integer32"
_HwBridgeLinkBridgeMode_Object = MibTableColumn
hwBridgeLinkBridgeMode = _HwBridgeLinkBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 11),
    _HwBridgeLinkBridgeMode_Type()
)
hwBridgeLinkBridgeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkBridgeMode.setStatus("current")
_HwBridgeLinkCoverageDistance_Type = Integer32
_HwBridgeLinkCoverageDistance_Object = MibTableColumn
hwBridgeLinkCoverageDistance = _HwBridgeLinkCoverageDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 12),
    _HwBridgeLinkCoverageDistance_Type()
)
hwBridgeLinkCoverageDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkCoverageDistance.setStatus("current")
_HwBridgeLinkPeerAPID_Type = Integer32
_HwBridgeLinkPeerAPID_Object = MibTableColumn
hwBridgeLinkPeerAPID = _HwBridgeLinkPeerAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 13),
    _HwBridgeLinkPeerAPID_Type()
)
hwBridgeLinkPeerAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkPeerAPID.setStatus("current")


class _HwBridgeLinkPeerAPStatus_Type(Integer32):
    """Custom type hwBridgeLinkPeerAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("autoFind", 2),
          ("commitFailed", 7),
          ("committing", 11),
          ("config", 6),
          ("configFailed", 12),
          ("download", 8),
          ("fault", 5),
          ("idle", 1),
          ("invalid", 13),
          ("normal", 10),
          ("standby", 9),
          ("typeNotMatch", 3),
          ("verMismatch", 4))
    )


_HwBridgeLinkPeerAPStatus_Type.__name__ = "Integer32"
_HwBridgeLinkPeerAPStatus_Object = MibTableColumn
hwBridgeLinkPeerAPStatus = _HwBridgeLinkPeerAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 14),
    _HwBridgeLinkPeerAPStatus_Type()
)
hwBridgeLinkPeerAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkPeerAPStatus.setStatus("current")
_HwBridgeLinkMaxRssi_Type = Integer32
_HwBridgeLinkMaxRssi_Object = MibTableColumn
hwBridgeLinkMaxRssi = _HwBridgeLinkMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 15),
    _HwBridgeLinkMaxRssi_Type()
)
hwBridgeLinkMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkMaxRssi.setStatus("current")
_HwBridgeLinkRssi_Type = Integer32
_HwBridgeLinkRssi_Object = MibTableColumn
hwBridgeLinkRssi = _HwBridgeLinkRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 16),
    _HwBridgeLinkRssi_Type()
)
hwBridgeLinkRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkRssi.setStatus("current")
_HwBridgeLinkPeerApMac_Type = MacAddress
_HwBridgeLinkPeerApMac_Object = MibTableColumn
hwBridgeLinkPeerApMac = _HwBridgeLinkPeerApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 17),
    _HwBridgeLinkPeerApMac_Type()
)
hwBridgeLinkPeerApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkPeerApMac.setStatus("current")
_HwBridgeLinkChannelID_Type = Integer32
_HwBridgeLinkChannelID_Object = MibTableColumn
hwBridgeLinkChannelID = _HwBridgeLinkChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 31, 1, 18),
    _HwBridgeLinkChannelID_Type()
)
hwBridgeLinkChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBridgeLinkChannelID.setStatus("current")
_HwMacBridgeLinkTable_Object = MibTable
hwMacBridgeLinkTable = _HwMacBridgeLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32)
)
if mibBuilder.loadTexts:
    hwMacBridgeLinkTable.setStatus("current")
_HwMacBridgeLinkEntry_Object = MibTableRow
hwMacBridgeLinkEntry = _HwMacBridgeLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1)
)
hwMacBridgeLinkEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeVapApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkIndex"),
)
if mibBuilder.loadTexts:
    hwMacBridgeLinkEntry.setStatus("current")
_HwMacBridgeLinkIndex_Type = Integer32
_HwMacBridgeLinkIndex_Object = MibTableColumn
hwMacBridgeLinkIndex = _HwMacBridgeLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 1),
    _HwMacBridgeLinkIndex_Type()
)
hwMacBridgeLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacBridgeLinkIndex.setStatus("current")
_HwMacBridgeLinkWlanID_Type = Integer32
_HwMacBridgeLinkWlanID_Object = MibTableColumn
hwMacBridgeLinkWlanID = _HwMacBridgeLinkWlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 2),
    _HwMacBridgeLinkWlanID_Type()
)
hwMacBridgeLinkWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkWlanID.setStatus("current")
_HwMacBridgeLinkBridgeType_Type = Integer32
_HwMacBridgeLinkBridgeType_Object = MibTableColumn
hwMacBridgeLinkBridgeType = _HwMacBridgeLinkBridgeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 3),
    _HwMacBridgeLinkBridgeType_Type()
)
hwMacBridgeLinkBridgeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkBridgeType.setStatus("current")
_HwMacBridgeLinkBridgeSubType_Type = Integer32
_HwMacBridgeLinkBridgeSubType_Object = MibTableColumn
hwMacBridgeLinkBridgeSubType = _HwMacBridgeLinkBridgeSubType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 4),
    _HwMacBridgeLinkBridgeSubType_Type()
)
hwMacBridgeLinkBridgeSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkBridgeSubType.setStatus("current")
_HwMacBridgeLinkPeerMac_Type = MacAddress
_HwMacBridgeLinkPeerMac_Object = MibTableColumn
hwMacBridgeLinkPeerMac = _HwMacBridgeLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 5),
    _HwMacBridgeLinkPeerMac_Type()
)
hwMacBridgeLinkPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkPeerMac.setStatus("current")


class _HwMacBridgeLinkBridgeProfileName_Type(OctetString):
    """Custom type hwMacBridgeLinkBridgeProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwMacBridgeLinkBridgeProfileName_Type.__name__ = "OctetString"
_HwMacBridgeLinkBridgeProfileName_Object = MibTableColumn
hwMacBridgeLinkBridgeProfileName = _HwMacBridgeLinkBridgeProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 6),
    _HwMacBridgeLinkBridgeProfileName_Type()
)
hwMacBridgeLinkBridgeProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkBridgeProfileName.setStatus("current")
_HwMacBridgeLinkStpMode_Type = Integer32
_HwMacBridgeLinkStpMode_Object = MibTableColumn
hwMacBridgeLinkStpMode = _HwMacBridgeLinkStpMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 7),
    _HwMacBridgeLinkStpMode_Type()
)
hwMacBridgeLinkStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkStpMode.setStatus("current")
_HwMacBridgeLinkInstanceIdList_Type = OctetString
_HwMacBridgeLinkInstanceIdList_Object = MibTableColumn
hwMacBridgeLinkInstanceIdList = _HwMacBridgeLinkInstanceIdList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 8),
    _HwMacBridgeLinkInstanceIdList_Type()
)
hwMacBridgeLinkInstanceIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkInstanceIdList.setStatus("current")
_HwMacBridgeLinkInstanceStateList_Type = OctetString
_HwMacBridgeLinkInstanceStateList_Object = MibTableColumn
hwMacBridgeLinkInstanceStateList = _HwMacBridgeLinkInstanceStateList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 9),
    _HwMacBridgeLinkInstanceStateList_Type()
)
hwMacBridgeLinkInstanceStateList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkInstanceStateList.setStatus("current")
_HwMacBridgeLinkApID_Type = Integer32
_HwMacBridgeLinkApID_Object = MibTableColumn
hwMacBridgeLinkApID = _HwMacBridgeLinkApID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 10),
    _HwMacBridgeLinkApID_Type()
)
hwMacBridgeLinkApID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkApID.setStatus("current")


class _HwMacBridgeLinkBridgeMode_Type(Integer32):
    """Custom type hwMacBridgeLinkBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 3),
          ("middle", 1),
          ("root", 2))
    )


_HwMacBridgeLinkBridgeMode_Type.__name__ = "Integer32"
_HwMacBridgeLinkBridgeMode_Object = MibTableColumn
hwMacBridgeLinkBridgeMode = _HwMacBridgeLinkBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 11),
    _HwMacBridgeLinkBridgeMode_Type()
)
hwMacBridgeLinkBridgeMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkBridgeMode.setStatus("current")
_HwMacBridgeLinkCoverageDistance_Type = Integer32
_HwMacBridgeLinkCoverageDistance_Object = MibTableColumn
hwMacBridgeLinkCoverageDistance = _HwMacBridgeLinkCoverageDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 12),
    _HwMacBridgeLinkCoverageDistance_Type()
)
hwMacBridgeLinkCoverageDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkCoverageDistance.setStatus("current")
_HwMacBridgeLinkPeerAPID_Type = Integer32
_HwMacBridgeLinkPeerAPID_Object = MibTableColumn
hwMacBridgeLinkPeerAPID = _HwMacBridgeLinkPeerAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 13),
    _HwMacBridgeLinkPeerAPID_Type()
)
hwMacBridgeLinkPeerAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkPeerAPID.setStatus("current")


class _HwMacBridgeLinkPeerAPStatus_Type(Integer32):
    """Custom type hwMacBridgeLinkPeerAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("autoFind", 2),
          ("commitFailed", 7),
          ("committing", 11),
          ("config", 6),
          ("configFailed", 12),
          ("download", 8),
          ("fault", 5),
          ("idle", 1),
          ("invalid", 13),
          ("normal", 10),
          ("standby", 9),
          ("typeNotMatch", 3),
          ("verMismatch", 4))
    )


_HwMacBridgeLinkPeerAPStatus_Type.__name__ = "Integer32"
_HwMacBridgeLinkPeerAPStatus_Object = MibTableColumn
hwMacBridgeLinkPeerAPStatus = _HwMacBridgeLinkPeerAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 14),
    _HwMacBridgeLinkPeerAPStatus_Type()
)
hwMacBridgeLinkPeerAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkPeerAPStatus.setStatus("current")
_HwMacBridgeLinkMaxRssi_Type = Integer32
_HwMacBridgeLinkMaxRssi_Object = MibTableColumn
hwMacBridgeLinkMaxRssi = _HwMacBridgeLinkMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 15),
    _HwMacBridgeLinkMaxRssi_Type()
)
hwMacBridgeLinkMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkMaxRssi.setStatus("current")
_HwMacBridgeLinkRssi_Type = Integer32
_HwMacBridgeLinkRssi_Object = MibTableColumn
hwMacBridgeLinkRssi = _HwMacBridgeLinkRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 16),
    _HwMacBridgeLinkRssi_Type()
)
hwMacBridgeLinkRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkRssi.setStatus("current")
_HwMacBridgeLinkPeerApMac_Type = MacAddress
_HwMacBridgeLinkPeerApMac_Object = MibTableColumn
hwMacBridgeLinkPeerApMac = _HwMacBridgeLinkPeerApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 17),
    _HwMacBridgeLinkPeerApMac_Type()
)
hwMacBridgeLinkPeerApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeLinkPeerApMac.setStatus("current")
_HwMacBridgeChannelID_Type = Integer32
_HwMacBridgeChannelID_Object = MibTableColumn
hwMacBridgeChannelID = _HwMacBridgeChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 32, 1, 18),
    _HwMacBridgeChannelID_Type()
)
hwMacBridgeChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacBridgeChannelID.setStatus("current")
_HwBridgeWhitelistTable_Object = MibTable
hwBridgeWhitelistTable = _HwBridgeWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 33)
)
if mibBuilder.loadTexts:
    hwBridgeWhitelistTable.setStatus("current")
_HwBridgeWhitelistEntry_Object = MibTableRow
hwBridgeWhitelistEntry = _HwBridgeWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 33, 1)
)
hwBridgeWhitelistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwBridgeWhitelistName"),
)
if mibBuilder.loadTexts:
    hwBridgeWhitelistEntry.setStatus("current")


class _HwBridgeWhitelistName_Type(OctetString):
    """Custom type hwBridgeWhitelistName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwBridgeWhitelistName_Type.__name__ = "OctetString"
_HwBridgeWhitelistName_Object = MibTableColumn
hwBridgeWhitelistName = _HwBridgeWhitelistName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 33, 1, 1),
    _HwBridgeWhitelistName_Type()
)
hwBridgeWhitelistName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBridgeWhitelistName.setStatus("current")


class _HwBridgeWhitelistPeerList_Type(OctetString):
    """Custom type hwBridgeWhitelistPeerList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 89),
    )


_HwBridgeWhitelistPeerList_Type.__name__ = "OctetString"
_HwBridgeWhitelistPeerList_Object = MibTableColumn
hwBridgeWhitelistPeerList = _HwBridgeWhitelistPeerList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 33, 1, 2),
    _HwBridgeWhitelistPeerList_Type()
)
hwBridgeWhitelistPeerList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBridgeWhitelistPeerList.setStatus("current")
_HwBridgeWhitelistRowStatus_Type = RowStatus
_HwBridgeWhitelistRowStatus_Object = MibTableColumn
hwBridgeWhitelistRowStatus = _HwBridgeWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 33, 1, 3),
    _HwBridgeWhitelistRowStatus_Type()
)
hwBridgeWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwBridgeWhitelistRowStatus.setStatus("current")
_HwWirelessSsidStatisticTable_Object = MibTable
hwWirelessSsidStatisticTable = _HwWirelessSsidStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34)
)
if mibBuilder.loadTexts:
    hwWirelessSsidStatisticTable.setStatus("current")
_HwWirelessSsidStatisticEntry_Object = MibTableRow
hwWirelessSsidStatisticEntry = _HwWirelessSsidStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1)
)
hwWirelessSsidStatisticEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidStatisticEssSsid"),
)
if mibBuilder.loadTexts:
    hwWirelessSsidStatisticEntry.setStatus("current")
_HwWirelessSsidStatisticEssSsid_Type = OctetString
_HwWirelessSsidStatisticEssSsid_Object = MibTableColumn
hwWirelessSsidStatisticEssSsid = _HwWirelessSsidStatisticEssSsid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 1),
    _HwWirelessSsidStatisticEssSsid_Type()
)
hwWirelessSsidStatisticEssSsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwWirelessSsidStatisticEssSsid.setStatus("current")
_HwWirelessSsidAirportTransmitUnicastFrames_Type = Counter64
_HwWirelessSsidAirportTransmitUnicastFrames_Object = MibTableColumn
hwWirelessSsidAirportTransmitUnicastFrames = _HwWirelessSsidAirportTransmitUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 2),
    _HwWirelessSsidAirportTransmitUnicastFrames_Type()
)
hwWirelessSsidAirportTransmitUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportTransmitUnicastFrames.setStatus("current")
_HwWirelessSsidAirportTransmitFrames_Type = Counter64
_HwWirelessSsidAirportTransmitFrames_Object = MibTableColumn
hwWirelessSsidAirportTransmitFrames = _HwWirelessSsidAirportTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 3),
    _HwWirelessSsidAirportTransmitFrames_Type()
)
hwWirelessSsidAirportTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportTransmitFrames.setStatus("current")
_HwWirelessSsidAirportTransmitErrorFrames_Type = Counter64
_HwWirelessSsidAirportTransmitErrorFrames_Object = MibTableColumn
hwWirelessSsidAirportTransmitErrorFrames = _HwWirelessSsidAirportTransmitErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 4),
    _HwWirelessSsidAirportTransmitErrorFrames_Type()
)
hwWirelessSsidAirportTransmitErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportTransmitErrorFrames.setStatus("current")
_HwWirelessSsidAirportDownReTransmitFrames_Type = Counter64
_HwWirelessSsidAirportDownReTransmitFrames_Object = MibTableColumn
hwWirelessSsidAirportDownReTransmitFrames = _HwWirelessSsidAirportDownReTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 5),
    _HwWirelessSsidAirportDownReTransmitFrames_Type()
)
hwWirelessSsidAirportDownReTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportDownReTransmitFrames.setStatus("current")
_HwWirelessSsidAirportTransmitDropFrames_Type = Counter64
_HwWirelessSsidAirportTransmitDropFrames_Object = MibTableColumn
hwWirelessSsidAirportTransmitDropFrames = _HwWirelessSsidAirportTransmitDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 6),
    _HwWirelessSsidAirportTransmitDropFrames_Type()
)
hwWirelessSsidAirportTransmitDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportTransmitDropFrames.setStatus("current")
_HwWirelessSsidAirportTransmitBytes_Type = Counter64
_HwWirelessSsidAirportTransmitBytes_Object = MibTableColumn
hwWirelessSsidAirportTransmitBytes = _HwWirelessSsidAirportTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 7),
    _HwWirelessSsidAirportTransmitBytes_Type()
)
hwWirelessSsidAirportTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportTransmitBytes.setStatus("current")
_HwWirelessSsidAirportRecvUnicastFrames_Type = Counter64
_HwWirelessSsidAirportRecvUnicastFrames_Object = MibTableColumn
hwWirelessSsidAirportRecvUnicastFrames = _HwWirelessSsidAirportRecvUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 8),
    _HwWirelessSsidAirportRecvUnicastFrames_Type()
)
hwWirelessSsidAirportRecvUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportRecvUnicastFrames.setStatus("current")
_HwWirelessSsidAirportRecvFrames_Type = Counter64
_HwWirelessSsidAirportRecvFrames_Object = MibTableColumn
hwWirelessSsidAirportRecvFrames = _HwWirelessSsidAirportRecvFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 9),
    _HwWirelessSsidAirportRecvFrames_Type()
)
hwWirelessSsidAirportRecvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportRecvFrames.setStatus("current")
_HwWirelessSsidAirportRecvErrorFrames_Type = Counter64
_HwWirelessSsidAirportRecvErrorFrames_Object = MibTableColumn
hwWirelessSsidAirportRecvErrorFrames = _HwWirelessSsidAirportRecvErrorFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 10),
    _HwWirelessSsidAirportRecvErrorFrames_Type()
)
hwWirelessSsidAirportRecvErrorFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportRecvErrorFrames.setStatus("current")
_HwWirelessSsidAirportRecvDropFrames_Type = Counter64
_HwWirelessSsidAirportRecvDropFrames_Object = MibTableColumn
hwWirelessSsidAirportRecvDropFrames = _HwWirelessSsidAirportRecvDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 11),
    _HwWirelessSsidAirportRecvDropFrames_Type()
)
hwWirelessSsidAirportRecvDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportRecvDropFrames.setStatus("current")
_HwWirelessSsidAirportRecvBytes_Type = Counter64
_HwWirelessSsidAirportRecvBytes_Object = MibTableColumn
hwWirelessSsidAirportRecvBytes = _HwWirelessSsidAirportRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 12),
    _HwWirelessSsidAirportRecvBytes_Type()
)
hwWirelessSsidAirportRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidAirportRecvBytes.setStatus("current")
_HwWirelessSsidTotalAssociatedSuccessStationCount_Type = Integer32
_HwWirelessSsidTotalAssociatedSuccessStationCount_Object = MibTableColumn
hwWirelessSsidTotalAssociatedSuccessStationCount = _HwWirelessSsidTotalAssociatedSuccessStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 13),
    _HwWirelessSsidTotalAssociatedSuccessStationCount_Type()
)
hwWirelessSsidTotalAssociatedSuccessStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidTotalAssociatedSuccessStationCount.setStatus("current")
_HwWirelessSsidCurAssocStationCount_Type = Integer32
_HwWirelessSsidCurAssocStationCount_Object = MibTableColumn
hwWirelessSsidCurAssocStationCount = _HwWirelessSsidCurAssocStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 14),
    _HwWirelessSsidCurAssocStationCount_Type()
)
hwWirelessSsidCurAssocStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidCurAssocStationCount.setStatus("current")
_HwWirelessSsidTotalAssociatedFailedStationCount_Type = Integer32
_HwWirelessSsidTotalAssociatedFailedStationCount_Object = MibTableColumn
hwWirelessSsidTotalAssociatedFailedStationCount = _HwWirelessSsidTotalAssociatedFailedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 34, 1, 15),
    _HwWirelessSsidTotalAssociatedFailedStationCount_Type()
)
hwWirelessSsidTotalAssociatedFailedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwWirelessSsidTotalAssociatedFailedStationCount.setStatus("current")
_HwStaBlacklistProfileTable_Object = MibTable
hwStaBlacklistProfileTable = _HwStaBlacklistProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35)
)
if mibBuilder.loadTexts:
    hwStaBlacklistProfileTable.setStatus("current")
_HwStaBlacklistProfileEntry_Object = MibTableRow
hwStaBlacklistProfileEntry = _HwStaBlacklistProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35, 1)
)
hwStaBlacklistProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwStaBlacklistProfileName"),
)
if mibBuilder.loadTexts:
    hwStaBlacklistProfileEntry.setStatus("current")


class _HwStaBlacklistProfileName_Type(OctetString):
    """Custom type hwStaBlacklistProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwStaBlacklistProfileName_Type.__name__ = "OctetString"
_HwStaBlacklistProfileName_Object = MibTableColumn
hwStaBlacklistProfileName = _HwStaBlacklistProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35, 1, 1),
    _HwStaBlacklistProfileName_Type()
)
hwStaBlacklistProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaBlacklistProfileName.setStatus("current")
_HwStaBlacklistProfileStaMac_Type = MacAddress
_HwStaBlacklistProfileStaMac_Object = MibTableColumn
hwStaBlacklistProfileStaMac = _HwStaBlacklistProfileStaMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35, 1, 2),
    _HwStaBlacklistProfileStaMac_Type()
)
hwStaBlacklistProfileStaMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaBlacklistProfileStaMac.setStatus("current")
_HwStaBlacklistProfileOper_Type = Integer32
_HwStaBlacklistProfileOper_Object = MibTableColumn
hwStaBlacklistProfileOper = _HwStaBlacklistProfileOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35, 1, 3),
    _HwStaBlacklistProfileOper_Type()
)
hwStaBlacklistProfileOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaBlacklistProfileOper.setStatus("current")
_HwStaBlacklistProfileStaNum_Type = Integer32
_HwStaBlacklistProfileStaNum_Object = MibTableColumn
hwStaBlacklistProfileStaNum = _HwStaBlacklistProfileStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35, 1, 4),
    _HwStaBlacklistProfileStaNum_Type()
)
hwStaBlacklistProfileStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaBlacklistProfileStaNum.setStatus("current")
_HwStaBlacklistProfileStaList_Type = OctetString
_HwStaBlacklistProfileStaList_Object = MibTableColumn
hwStaBlacklistProfileStaList = _HwStaBlacklistProfileStaList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35, 1, 5),
    _HwStaBlacklistProfileStaList_Type()
)
hwStaBlacklistProfileStaList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaBlacklistProfileStaList.setStatus("current")
_HwStaBlacklistProfileRowStatus_Type = RowStatus
_HwStaBlacklistProfileRowStatus_Object = MibTableColumn
hwStaBlacklistProfileRowStatus = _HwStaBlacklistProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 35, 1, 6),
    _HwStaBlacklistProfileRowStatus_Type()
)
hwStaBlacklistProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaBlacklistProfileRowStatus.setStatus("current")
_HwStaWhitelistProfileTable_Object = MibTable
hwStaWhitelistProfileTable = _HwStaWhitelistProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36)
)
if mibBuilder.loadTexts:
    hwStaWhitelistProfileTable.setStatus("current")
_HwStaWhitelistProfileEntry_Object = MibTableRow
hwStaWhitelistProfileEntry = _HwStaWhitelistProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36, 1)
)
hwStaWhitelistProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwStaWhitelistProfileName"),
)
if mibBuilder.loadTexts:
    hwStaWhitelistProfileEntry.setStatus("current")


class _HwStaWhitelistProfileName_Type(OctetString):
    """Custom type hwStaWhitelistProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwStaWhitelistProfileName_Type.__name__ = "OctetString"
_HwStaWhitelistProfileName_Object = MibTableColumn
hwStaWhitelistProfileName = _HwStaWhitelistProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36, 1, 1),
    _HwStaWhitelistProfileName_Type()
)
hwStaWhitelistProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaWhitelistProfileName.setStatus("current")
_HwStaWhitelistProfileStaMac_Type = MacAddress
_HwStaWhitelistProfileStaMac_Object = MibTableColumn
hwStaWhitelistProfileStaMac = _HwStaWhitelistProfileStaMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36, 1, 2),
    _HwStaWhitelistProfileStaMac_Type()
)
hwStaWhitelistProfileStaMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaWhitelistProfileStaMac.setStatus("current")
_HwStaWhitelistProfileOper_Type = Integer32
_HwStaWhitelistProfileOper_Object = MibTableColumn
hwStaWhitelistProfileOper = _HwStaWhitelistProfileOper_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36, 1, 3),
    _HwStaWhitelistProfileOper_Type()
)
hwStaWhitelistProfileOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaWhitelistProfileOper.setStatus("current")
_HwStaWhitelistProfileStaNum_Type = Integer32
_HwStaWhitelistProfileStaNum_Object = MibTableColumn
hwStaWhitelistProfileStaNum = _HwStaWhitelistProfileStaNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36, 1, 4),
    _HwStaWhitelistProfileStaNum_Type()
)
hwStaWhitelistProfileStaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWhitelistProfileStaNum.setStatus("current")
_HwStaWhitelistProfileStaList_Type = OctetString
_HwStaWhitelistProfileStaList_Object = MibTableColumn
hwStaWhitelistProfileStaList = _HwStaWhitelistProfileStaList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36, 1, 5),
    _HwStaWhitelistProfileStaList_Type()
)
hwStaWhitelistProfileStaList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaWhitelistProfileStaList.setStatus("current")
_HwStaWhitelistProfileRowStatus_Type = RowStatus
_HwStaWhitelistProfileRowStatus_Object = MibTableColumn
hwStaWhitelistProfileRowStatus = _HwStaWhitelistProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 36, 1, 6),
    _HwStaWhitelistProfileRowStatus_Type()
)
hwStaWhitelistProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwStaWhitelistProfileRowStatus.setStatus("current")
_HwMeshProfileTable_Object = MibTable
hwMeshProfileTable = _HwMeshProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37)
)
if mibBuilder.loadTexts:
    hwMeshProfileTable.setStatus("current")
_HwMeshProfileEntry_Object = MibTableRow
hwMeshProfileEntry = _HwMeshProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1)
)
hwMeshProfileEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileName"),
)
if mibBuilder.loadTexts:
    hwMeshProfileEntry.setStatus("current")


class _HwMeshProfileName_Type(OctetString):
    """Custom type hwMeshProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMeshProfileName_Type.__name__ = "OctetString"
_HwMeshProfileName_Object = MibTableColumn
hwMeshProfileName = _HwMeshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 1),
    _HwMeshProfileName_Type()
)
hwMeshProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMeshProfileName.setStatus("current")


class _HwMeshProfileSecurityProfileName_Type(OctetString):
    """Custom type hwMeshProfileSecurityProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMeshProfileSecurityProfileName_Type.__name__ = "OctetString"
_HwMeshProfileSecurityProfileName_Object = MibTableColumn
hwMeshProfileSecurityProfileName = _HwMeshProfileSecurityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 2),
    _HwMeshProfileSecurityProfileName_Type()
)
hwMeshProfileSecurityProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMeshProfileSecurityProfileName.setStatus("current")


class _HwMeshProfileMeshID_Type(OctetString):
    """Custom type hwMeshProfileMeshID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMeshProfileMeshID_Type.__name__ = "OctetString"
_HwMeshProfileMeshID_Object = MibTableColumn
hwMeshProfileMeshID = _HwMeshProfileMeshID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 3),
    _HwMeshProfileMeshID_Type()
)
hwMeshProfileMeshID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMeshProfileMeshID.setStatus("current")


class _HwMeshProfileMaxLinkNum_Type(Integer32):
    """Custom type hwMeshProfileMaxLinkNum based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwMeshProfileMaxLinkNum_Type.__name__ = "Integer32"
_HwMeshProfileMaxLinkNum_Object = MibTableColumn
hwMeshProfileMaxLinkNum = _HwMeshProfileMaxLinkNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 4),
    _HwMeshProfileMaxLinkNum_Type()
)
hwMeshProfileMaxLinkNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileMaxLinkNum.setStatus("current")


class _HwMeshProfileRssiThreshold_Type(Integer32):
    """Custom type hwMeshProfileRssiThreshold based on Integer32"""
    defaultValue = -75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -20),
    )


_HwMeshProfileRssiThreshold_Type.__name__ = "Integer32"
_HwMeshProfileRssiThreshold_Object = MibTableColumn
hwMeshProfileRssiThreshold = _HwMeshProfileRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 5),
    _HwMeshProfileRssiThreshold_Type()
)
hwMeshProfileRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileRssiThreshold.setUnits("dBm")


class _HwMeshProfileReportInterval_Type(Integer32):
    """Custom type hwMeshProfileReportInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_HwMeshProfileReportInterval_Type.__name__ = "Integer32"
_HwMeshProfileReportInterval_Object = MibTableColumn
hwMeshProfileReportInterval = _HwMeshProfileReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 6),
    _HwMeshProfileReportInterval_Type()
)
hwMeshProfileReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileReportInterval.setUnits("s")
_HwMeshProfileRowStatus_Type = RowStatus
_HwMeshProfileRowStatus_Object = MibTableColumn
hwMeshProfileRowStatus = _HwMeshProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 7),
    _HwMeshProfileRowStatus_Type()
)
hwMeshProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileRowStatus.setStatus("current")


class _HwMeshProfileDhcpTrustPort_Type(Integer32):
    """Custom type hwMeshProfileDhcpTrustPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMeshProfileDhcpTrustPort_Type.__name__ = "Integer32"
_HwMeshProfileDhcpTrustPort_Object = MibTableColumn
hwMeshProfileDhcpTrustPort = _HwMeshProfileDhcpTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 8),
    _HwMeshProfileDhcpTrustPort_Type()
)
hwMeshProfileDhcpTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileDhcpTrustPort.setStatus("current")


class _HwMeshProfileNdTrustPort_Type(Integer32):
    """Custom type hwMeshProfileNdTrustPort based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMeshProfileNdTrustPort_Type.__name__ = "Integer32"
_HwMeshProfileNdTrustPort_Object = MibTableColumn
hwMeshProfileNdTrustPort = _HwMeshProfileNdTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 9),
    _HwMeshProfileNdTrustPort_Type()
)
hwMeshProfileNdTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileNdTrustPort.setStatus("current")


class _HwMeshProfileQuickHoSwitch_Type(Integer32):
    """Custom type hwMeshProfileQuickHoSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMeshProfileQuickHoSwitch_Type.__name__ = "Integer32"
_HwMeshProfileQuickHoSwitch_Object = MibTableColumn
hwMeshProfileQuickHoSwitch = _HwMeshProfileQuickHoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 10),
    _HwMeshProfileQuickHoSwitch_Type()
)
hwMeshProfileQuickHoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileQuickHoSwitch.setStatus("current")


class _HwMeshProfileLinkHoThreshold_Type(Integer32):
    """Custom type hwMeshProfileLinkHoThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 70),
    )


_HwMeshProfileLinkHoThreshold_Type.__name__ = "Integer32"
_HwMeshProfileLinkHoThreshold_Object = MibTableColumn
hwMeshProfileLinkHoThreshold = _HwMeshProfileLinkHoThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 11),
    _HwMeshProfileLinkHoThreshold_Type()
)
hwMeshProfileLinkHoThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileLinkHoThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileLinkHoThreshold.setUnits("dB")


class _HwMeshProfileLinkHoldPeriod_Type(Integer32):
    """Custom type hwMeshProfileLinkHoldPeriod based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 60000),
    )


_HwMeshProfileLinkHoldPeriod_Type.__name__ = "Integer32"
_HwMeshProfileLinkHoldPeriod_Object = MibTableColumn
hwMeshProfileLinkHoldPeriod = _HwMeshProfileLinkHoldPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 12),
    _HwMeshProfileLinkHoldPeriod_Type()
)
hwMeshProfileLinkHoldPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileLinkHoldPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileLinkHoldPeriod.setUnits("ms")


class _HwMeshProfileLinkLinkSaturationThreshold_Type(Integer32):
    """Custom type hwMeshProfileLinkLinkSaturationThreshold based on Integer32"""
    defaultValue = -20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, 0),
    )


_HwMeshProfileLinkLinkSaturationThreshold_Type.__name__ = "Integer32"
_HwMeshProfileLinkLinkSaturationThreshold_Object = MibTableColumn
hwMeshProfileLinkLinkSaturationThreshold = _HwMeshProfileLinkLinkSaturationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 13),
    _HwMeshProfileLinkLinkSaturationThreshold_Type()
)
hwMeshProfileLinkLinkSaturationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileLinkLinkSaturationThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileLinkLinkSaturationThreshold.setUnits("dBm")


class _HwMeshProfileLinkProbePeriod_Type(Integer32):
    """Custom type hwMeshProfileLinkProbePeriod based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 6000),
    )


_HwMeshProfileLinkProbePeriod_Type.__name__ = "Integer32"
_HwMeshProfileLinkProbePeriod_Object = MibTableColumn
hwMeshProfileLinkProbePeriod = _HwMeshProfileLinkProbePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 14),
    _HwMeshProfileLinkProbePeriod_Type()
)
hwMeshProfileLinkProbePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileLinkProbePeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileLinkProbePeriod.setUnits("ms")


class _HwMeshProfileFwaMode_Type(Integer32):
    """Custom type hwMeshProfileFwaMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMeshProfileFwaMode_Type.__name__ = "Integer32"
_HwMeshProfileFwaMode_Object = MibTableColumn
hwMeshProfileFwaMode = _HwMeshProfileFwaMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 15),
    _HwMeshProfileFwaMode_Type()
)
hwMeshProfileFwaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileFwaMode.setStatus("current")


class _HwMeshProfileFwaEdcaMode_Type(Integer32):
    """Custom type hwMeshProfileFwaEdcaMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_HwMeshProfileFwaEdcaMode_Type.__name__ = "Integer32"
_HwMeshProfileFwaEdcaMode_Object = MibTableColumn
hwMeshProfileFwaEdcaMode = _HwMeshProfileFwaEdcaMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 16),
    _HwMeshProfileFwaEdcaMode_Type()
)
hwMeshProfileFwaEdcaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileFwaEdcaMode.setStatus("current")


class _HwMeshProfileQuickHandoverMinRssiThreshold_Type(Integer32):
    """Custom type hwMeshProfileQuickHandoverMinRssiThreshold based on Integer32"""
    defaultValue = -60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -20),
    )


_HwMeshProfileQuickHandoverMinRssiThreshold_Type.__name__ = "Integer32"
_HwMeshProfileQuickHandoverMinRssiThreshold_Object = MibTableColumn
hwMeshProfileQuickHandoverMinRssiThreshold = _HwMeshProfileQuickHandoverMinRssiThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 17),
    _HwMeshProfileQuickHandoverMinRssiThreshold_Type()
)
hwMeshProfileQuickHandoverMinRssiThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileQuickHandoverMinRssiThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileQuickHandoverMinRssiThreshold.setUnits("dBm")


class _HwMeshProfileLocationBasedHandoverAlgorithmSwitch_Type(Integer32):
    """Custom type hwMeshProfileLocationBasedHandoverAlgorithmSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HwMeshProfileLocationBasedHandoverAlgorithmSwitch_Type.__name__ = "Integer32"
_HwMeshProfileLocationBasedHandoverAlgorithmSwitch_Object = MibTableColumn
hwMeshProfileLocationBasedHandoverAlgorithmSwitch = _HwMeshProfileLocationBasedHandoverAlgorithmSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 18),
    _HwMeshProfileLocationBasedHandoverAlgorithmSwitch_Type()
)
hwMeshProfileLocationBasedHandoverAlgorithmSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileLocationBasedHandoverAlgorithmSwitch.setStatus("current")


class _HwMeshProfileMovingDirection_Type(Integer32):
    """Custom type hwMeshProfileMovingDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backward", 2),
          ("forward", 1),
          ("undetermined", 3))
    )


_HwMeshProfileMovingDirection_Type.__name__ = "Integer32"
_HwMeshProfileMovingDirection_Object = MibTableColumn
hwMeshProfileMovingDirection = _HwMeshProfileMovingDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 19),
    _HwMeshProfileMovingDirection_Type()
)
hwMeshProfileMovingDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileMovingDirection.setStatus("current")


class _HwMeshProfileHandoverAlgorithmPNCriteriaObserveTime_Type(Integer32):
    """Custom type hwMeshProfileHandoverAlgorithmPNCriteriaObserveTime based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMeshProfileHandoverAlgorithmPNCriteriaObserveTime_Type.__name__ = "Integer32"
_HwMeshProfileHandoverAlgorithmPNCriteriaObserveTime_Object = MibTableColumn
hwMeshProfileHandoverAlgorithmPNCriteriaObserveTime = _HwMeshProfileHandoverAlgorithmPNCriteriaObserveTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 20),
    _HwMeshProfileHandoverAlgorithmPNCriteriaObserveTime_Type()
)
hwMeshProfileHandoverAlgorithmPNCriteriaObserveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileHandoverAlgorithmPNCriteriaObserveTime.setStatus("current")


class _HwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime_Type(Integer32):
    """Custom type hwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime_Type.__name__ = "Integer32"
_HwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime_Object = MibTableColumn
hwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime = _HwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 21),
    _HwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime_Type()
)
hwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime.setStatus("current")


class _HwMeshProfileUrgentHandoverLowRateThreshold_Type(Integer32):
    """Custom type hwMeshProfileUrgentHandoverLowRateThreshold based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1300),
    )


_HwMeshProfileUrgentHandoverLowRateThreshold_Type.__name__ = "Integer32"
_HwMeshProfileUrgentHandoverLowRateThreshold_Object = MibTableColumn
hwMeshProfileUrgentHandoverLowRateThreshold = _HwMeshProfileUrgentHandoverLowRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 22),
    _HwMeshProfileUrgentHandoverLowRateThreshold_Type()
)
hwMeshProfileUrgentHandoverLowRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverLowRateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverLowRateThreshold.setUnits("Mbps")


class _HwMeshProfileUrgentHandoverLowRatePeriod_Type(Integer32):
    """Custom type hwMeshProfileUrgentHandoverLowRatePeriod based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwMeshProfileUrgentHandoverLowRatePeriod_Type.__name__ = "Integer32"
_HwMeshProfileUrgentHandoverLowRatePeriod_Object = MibTableColumn
hwMeshProfileUrgentHandoverLowRatePeriod = _HwMeshProfileUrgentHandoverLowRatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 23),
    _HwMeshProfileUrgentHandoverLowRatePeriod_Type()
)
hwMeshProfileUrgentHandoverLowRatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverLowRatePeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverLowRatePeriod.setUnits("ms")


class _HwMeshProfileUrgentHandoverPunishmentPeriod_Type(Integer32):
    """Custom type hwMeshProfileUrgentHandoverPunishmentPeriod based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_HwMeshProfileUrgentHandoverPunishmentPeriod_Type.__name__ = "Integer32"
_HwMeshProfileUrgentHandoverPunishmentPeriod_Object = MibTableColumn
hwMeshProfileUrgentHandoverPunishmentPeriod = _HwMeshProfileUrgentHandoverPunishmentPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 24),
    _HwMeshProfileUrgentHandoverPunishmentPeriod_Type()
)
hwMeshProfileUrgentHandoverPunishmentPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverPunishmentPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverPunishmentPeriod.setUnits("ms")


class _HwMeshProfileUrgentHandoverPunishmentRssi_Type(Integer32):
    """Custom type hwMeshProfileUrgentHandoverPunishmentRssi based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_HwMeshProfileUrgentHandoverPunishmentRssi_Type.__name__ = "Integer32"
_HwMeshProfileUrgentHandoverPunishmentRssi_Object = MibTableColumn
hwMeshProfileUrgentHandoverPunishmentRssi = _HwMeshProfileUrgentHandoverPunishmentRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 37, 1, 25),
    _HwMeshProfileUrgentHandoverPunishmentRssi_Type()
)
hwMeshProfileUrgentHandoverPunishmentRssi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverPunishmentRssi.setStatus("current")
if mibBuilder.loadTexts:
    hwMeshProfileUrgentHandoverPunishmentRssi.setUnits("dB")
_HwMeshVapManagementTable_Object = MibTable
hwMeshVapManagementTable = _HwMeshVapManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 38)
)
if mibBuilder.loadTexts:
    hwMeshVapManagementTable.setStatus("current")
_HwMeshVapManagementEntry_Object = MibTableRow
hwMeshVapManagementEntry = _HwMeshVapManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 38, 1)
)
hwMeshVapManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshVapApIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshVapMeshProfileName"),
)
if mibBuilder.loadTexts:
    hwMeshVapManagementEntry.setStatus("current")
_HwMeshVapApIndex_Type = Integer32
_HwMeshVapApIndex_Object = MibTableColumn
hwMeshVapApIndex = _HwMeshVapApIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 38, 1, 1),
    _HwMeshVapApIndex_Type()
)
hwMeshVapApIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMeshVapApIndex.setStatus("current")
_HwMeshVapRadioIndex_Type = Integer32
_HwMeshVapRadioIndex_Object = MibTableColumn
hwMeshVapRadioIndex = _HwMeshVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 38, 1, 2),
    _HwMeshVapRadioIndex_Type()
)
hwMeshVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMeshVapRadioIndex.setStatus("current")


class _HwMeshVapMeshProfileName_Type(OctetString):
    """Custom type hwMeshVapMeshProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMeshVapMeshProfileName_Type.__name__ = "OctetString"
_HwMeshVapMeshProfileName_Object = MibTableColumn
hwMeshVapMeshProfileName = _HwMeshVapMeshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 38, 1, 3),
    _HwMeshVapMeshProfileName_Type()
)
hwMeshVapMeshProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMeshVapMeshProfileName.setStatus("current")
_HwMeshVapRowStatus_Type = RowStatus
_HwMeshVapRowStatus_Object = MibTableColumn
hwMeshVapRowStatus = _HwMeshVapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 38, 1, 4),
    _HwMeshVapRowStatus_Type()
)
hwMeshVapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMeshVapRowStatus.setStatus("current")
_HwMeshVapBssid_Type = OctetString
_HwMeshVapBssid_Object = MibTableColumn
hwMeshVapBssid = _HwMeshVapBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 38, 1, 5),
    _HwMeshVapBssid_Type()
)
hwMeshVapBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshVapBssid.setStatus("current")
_HwMacMeshVapManagementTable_Object = MibTable
hwMacMeshVapManagementTable = _HwMacMeshVapManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 39)
)
if mibBuilder.loadTexts:
    hwMacMeshVapManagementTable.setStatus("current")
_HwMacMeshVapManagementEntry_Object = MibTableRow
hwMacMeshVapManagementEntry = _HwMacMeshVapManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 39, 1)
)
hwMacMeshVapManagementEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshVapApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshVapMeshProfileName"),
)
if mibBuilder.loadTexts:
    hwMacMeshVapManagementEntry.setStatus("current")
_HwMacMeshVapApMac_Type = MacAddress
_HwMacMeshVapApMac_Object = MibTableColumn
hwMacMeshVapApMac = _HwMacMeshVapApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 39, 1, 1),
    _HwMacMeshVapApMac_Type()
)
hwMacMeshVapApMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacMeshVapApMac.setStatus("current")
_HwMacMeshVapRadioIndex_Type = Integer32
_HwMacMeshVapRadioIndex_Object = MibTableColumn
hwMacMeshVapRadioIndex = _HwMacMeshVapRadioIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 39, 1, 2),
    _HwMacMeshVapRadioIndex_Type()
)
hwMacMeshVapRadioIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacMeshVapRadioIndex.setStatus("current")


class _HwMacMeshVapMeshProfileName_Type(OctetString):
    """Custom type hwMacMeshVapMeshProfileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMacMeshVapMeshProfileName_Type.__name__ = "OctetString"
_HwMacMeshVapMeshProfileName_Object = MibTableColumn
hwMacMeshVapMeshProfileName = _HwMacMeshVapMeshProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 39, 1, 3),
    _HwMacMeshVapMeshProfileName_Type()
)
hwMacMeshVapMeshProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacMeshVapMeshProfileName.setStatus("current")
_HwMacMeshVapRowStatus_Type = RowStatus
_HwMacMeshVapRowStatus_Object = MibTableColumn
hwMacMeshVapRowStatus = _HwMacMeshVapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 39, 1, 4),
    _HwMacMeshVapRowStatus_Type()
)
hwMacMeshVapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMacMeshVapRowStatus.setStatus("current")
_HwMacMeshVapBssid_Type = OctetString
_HwMacMeshVapBssid_Object = MibTableColumn
hwMacMeshVapBssid = _HwMacMeshVapBssid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 39, 1, 5),
    _HwMacMeshVapBssid_Type()
)
hwMacMeshVapBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshVapBssid.setStatus("current")
_HwMeshLinkTable_Object = MibTable
hwMeshLinkTable = _HwMeshLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40)
)
if mibBuilder.loadTexts:
    hwMeshLinkTable.setStatus("current")
_HwMeshLinkEntry_Object = MibTableRow
hwMeshLinkEntry = _HwMeshLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1)
)
hwMeshLinkEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshVapApIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkIndex"),
)
if mibBuilder.loadTexts:
    hwMeshLinkEntry.setStatus("current")
_HwMeshLinkIndex_Type = Integer32
_HwMeshLinkIndex_Object = MibTableColumn
hwMeshLinkIndex = _HwMeshLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 1),
    _HwMeshLinkIndex_Type()
)
hwMeshLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMeshLinkIndex.setStatus("current")
_HwMeshLinkWlanID_Type = Integer32
_HwMeshLinkWlanID_Object = MibTableColumn
hwMeshLinkWlanID = _HwMeshLinkWlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 2),
    _HwMeshLinkWlanID_Type()
)
hwMeshLinkWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkWlanID.setStatus("current")
_HwMeshLinkPeerMac_Type = MacAddress
_HwMeshLinkPeerMac_Object = MibTableColumn
hwMeshLinkPeerMac = _HwMeshLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 3),
    _HwMeshLinkPeerMac_Type()
)
hwMeshLinkPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkPeerMac.setStatus("current")
_HwMeshLinkChannelID_Type = Integer32
_HwMeshLinkChannelID_Object = MibTableColumn
hwMeshLinkChannelID = _HwMeshLinkChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 4),
    _HwMeshLinkChannelID_Type()
)
hwMeshLinkChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkChannelID.setStatus("current")
_HwMeshLinkRssiValue_Type = Integer32
_HwMeshLinkRssiValue_Object = MibTableColumn
hwMeshLinkRssiValue = _HwMeshLinkRssiValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 5),
    _HwMeshLinkRssiValue_Type()
)
hwMeshLinkRssiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkRssiValue.setStatus("current")
_HwMeshLinkApMac_Type = MacAddress
_HwMeshLinkApMac_Object = MibTableColumn
hwMeshLinkApMac = _HwMeshLinkApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 6),
    _HwMeshLinkApMac_Type()
)
hwMeshLinkApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkApMac.setStatus("current")


class _HwMeshLinkMeshRole_Type(Integer32):
    """Custom type hwMeshLinkMeshRole based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meshNode", 1),
          ("meshPortal", 2))
    )


_HwMeshLinkMeshRole_Type.__name__ = "Integer32"
_HwMeshLinkMeshRole_Object = MibTableColumn
hwMeshLinkMeshRole = _HwMeshLinkMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 7),
    _HwMeshLinkMeshRole_Type()
)
hwMeshLinkMeshRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkMeshRole.setStatus("current")
_HwMeshLinkCoverageDistance_Type = Integer32
_HwMeshLinkCoverageDistance_Object = MibTableColumn
hwMeshLinkCoverageDistance = _HwMeshLinkCoverageDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 8),
    _HwMeshLinkCoverageDistance_Type()
)
hwMeshLinkCoverageDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkCoverageDistance.setStatus("current")
_HwMeshLinkPeerAPID_Type = Integer32
_HwMeshLinkPeerAPID_Object = MibTableColumn
hwMeshLinkPeerAPID = _HwMeshLinkPeerAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 9),
    _HwMeshLinkPeerAPID_Type()
)
hwMeshLinkPeerAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkPeerAPID.setStatus("current")


class _HwMeshLinkPeerAPStatus_Type(Integer32):
    """Custom type hwMeshLinkPeerAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("autoFind", 2),
          ("commitFailed", 7),
          ("committing", 11),
          ("config", 6),
          ("configFailed", 12),
          ("download", 8),
          ("fault", 5),
          ("idle", 1),
          ("invalid", 13),
          ("normal", 10),
          ("standby", 9),
          ("typeNotMatch", 3),
          ("verMismatch", 4))
    )


_HwMeshLinkPeerAPStatus_Type.__name__ = "Integer32"
_HwMeshLinkPeerAPStatus_Object = MibTableColumn
hwMeshLinkPeerAPStatus = _HwMeshLinkPeerAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 10),
    _HwMeshLinkPeerAPStatus_Type()
)
hwMeshLinkPeerAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkPeerAPStatus.setStatus("current")
_HwMeshLinkMaxRssi_Type = Integer32
_HwMeshLinkMaxRssi_Object = MibTableColumn
hwMeshLinkMaxRssi = _HwMeshLinkMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 11),
    _HwMeshLinkMaxRssi_Type()
)
hwMeshLinkMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkMaxRssi.setStatus("current")
_HwMeshLinkPeerApMac_Type = MacAddress
_HwMeshLinkPeerApMac_Object = MibTableColumn
hwMeshLinkPeerApMac = _HwMeshLinkPeerApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 40, 1, 12),
    _HwMeshLinkPeerApMac_Type()
)
hwMeshLinkPeerApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMeshLinkPeerApMac.setStatus("current")
_HwMacMeshLinkTable_Object = MibTable
hwMacMeshLinkTable = _HwMacMeshLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41)
)
if mibBuilder.loadTexts:
    hwMacMeshLinkTable.setStatus("current")
_HwMacMeshLinkEntry_Object = MibTableRow
hwMacMeshLinkEntry = _HwMacMeshLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1)
)
hwMacMeshLinkEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshVapApMac"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshVapRadioIndex"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkIndex"),
)
if mibBuilder.loadTexts:
    hwMacMeshLinkEntry.setStatus("current")
_HwMacMeshLinkIndex_Type = Integer32
_HwMacMeshLinkIndex_Object = MibTableColumn
hwMacMeshLinkIndex = _HwMacMeshLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 1),
    _HwMacMeshLinkIndex_Type()
)
hwMacMeshLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMacMeshLinkIndex.setStatus("current")
_HwMacMeshLinkWlanID_Type = Integer32
_HwMacMeshLinkWlanID_Object = MibTableColumn
hwMacMeshLinkWlanID = _HwMacMeshLinkWlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 2),
    _HwMacMeshLinkWlanID_Type()
)
hwMacMeshLinkWlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkWlanID.setStatus("current")
_HwMacMeshLinkPeerMac_Type = MacAddress
_HwMacMeshLinkPeerMac_Object = MibTableColumn
hwMacMeshLinkPeerMac = _HwMacMeshLinkPeerMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 3),
    _HwMacMeshLinkPeerMac_Type()
)
hwMacMeshLinkPeerMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkPeerMac.setStatus("current")
_HwMacMeshLinkChannelID_Type = Integer32
_HwMacMeshLinkChannelID_Object = MibTableColumn
hwMacMeshLinkChannelID = _HwMacMeshLinkChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 4),
    _HwMacMeshLinkChannelID_Type()
)
hwMacMeshLinkChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkChannelID.setStatus("current")
_HwMacMeshLinkRssiValue_Type = Integer32
_HwMacMeshLinkRssiValue_Object = MibTableColumn
hwMacMeshLinkRssiValue = _HwMacMeshLinkRssiValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 5),
    _HwMacMeshLinkRssiValue_Type()
)
hwMacMeshLinkRssiValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkRssiValue.setStatus("current")
_HwMacMeshLinkApID_Type = Integer32
_HwMacMeshLinkApID_Object = MibTableColumn
hwMacMeshLinkApID = _HwMacMeshLinkApID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 6),
    _HwMacMeshLinkApID_Type()
)
hwMacMeshLinkApID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkApID.setStatus("current")


class _HwMacMeshLinkMeshRole_Type(Integer32):
    """Custom type hwMacMeshLinkMeshRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("meshNode", 1),
          ("meshPortal", 2))
    )


_HwMacMeshLinkMeshRole_Type.__name__ = "Integer32"
_HwMacMeshLinkMeshRole_Object = MibTableColumn
hwMacMeshLinkMeshRole = _HwMacMeshLinkMeshRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 7),
    _HwMacMeshLinkMeshRole_Type()
)
hwMacMeshLinkMeshRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkMeshRole.setStatus("current")
_HwMacMeshLinkCoverageDistance_Type = Integer32
_HwMacMeshLinkCoverageDistance_Object = MibTableColumn
hwMacMeshLinkCoverageDistance = _HwMacMeshLinkCoverageDistance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 8),
    _HwMacMeshLinkCoverageDistance_Type()
)
hwMacMeshLinkCoverageDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkCoverageDistance.setStatus("current")
_HwMacMeshLinkPeerAPID_Type = Integer32
_HwMacMeshLinkPeerAPID_Object = MibTableColumn
hwMacMeshLinkPeerAPID = _HwMacMeshLinkPeerAPID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 9),
    _HwMacMeshLinkPeerAPID_Type()
)
hwMacMeshLinkPeerAPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkPeerAPID.setStatus("current")


class _HwMacMeshLinkPeerAPStatus_Type(Integer32):
    """Custom type hwMacMeshLinkPeerAPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("autoFind", 2),
          ("commitFailed", 7),
          ("committing", 11),
          ("config", 6),
          ("configFailed", 12),
          ("download", 8),
          ("fault", 5),
          ("idle", 1),
          ("invalid", 13),
          ("normal", 10),
          ("standby", 9),
          ("typeNotMatch", 3),
          ("verMismatch", 4))
    )


_HwMacMeshLinkPeerAPStatus_Type.__name__ = "Integer32"
_HwMacMeshLinkPeerAPStatus_Object = MibTableColumn
hwMacMeshLinkPeerAPStatus = _HwMacMeshLinkPeerAPStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 10),
    _HwMacMeshLinkPeerAPStatus_Type()
)
hwMacMeshLinkPeerAPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkPeerAPStatus.setStatus("current")
_HwMacMeshLinkMaxRssi_Type = Integer32
_HwMacMeshLinkMaxRssi_Object = MibTableColumn
hwMacMeshLinkMaxRssi = _HwMacMeshLinkMaxRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 11),
    _HwMacMeshLinkMaxRssi_Type()
)
hwMacMeshLinkMaxRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkMaxRssi.setStatus("current")
_HwMacMeshLinkPeerApMac_Type = MacAddress
_HwMacMeshLinkPeerApMac_Object = MibTableColumn
hwMacMeshLinkPeerApMac = _HwMacMeshLinkPeerApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 41, 1, 12),
    _HwMacMeshLinkPeerApMac_Type()
)
hwMacMeshLinkPeerApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMacMeshLinkPeerApMac.setStatus("current")
_HwMeshWhitelistTable_Object = MibTable
hwMeshWhitelistTable = _HwMeshWhitelistTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 42)
)
if mibBuilder.loadTexts:
    hwMeshWhitelistTable.setStatus("current")
_HwMeshWhitelistEntry_Object = MibTableRow
hwMeshWhitelistEntry = _HwMeshWhitelistEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 42, 1)
)
hwMeshWhitelistEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwMeshWhitelistName"),
)
if mibBuilder.loadTexts:
    hwMeshWhitelistEntry.setStatus("current")


class _HwMeshWhitelistName_Type(OctetString):
    """Custom type hwMeshWhitelistName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwMeshWhitelistName_Type.__name__ = "OctetString"
_HwMeshWhitelistName_Object = MibTableColumn
hwMeshWhitelistName = _HwMeshWhitelistName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 42, 1, 1),
    _HwMeshWhitelistName_Type()
)
hwMeshWhitelistName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMeshWhitelistName.setStatus("current")


class _HwMeshWhitelistPeerList_Type(OctetString):
    """Custom type hwMeshWhitelistPeerList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8193),
    )


_HwMeshWhitelistPeerList_Type.__name__ = "OctetString"
_HwMeshWhitelistPeerList_Object = MibTableColumn
hwMeshWhitelistPeerList = _HwMeshWhitelistPeerList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 42, 1, 2),
    _HwMeshWhitelistPeerList_Type()
)
hwMeshWhitelistPeerList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMeshWhitelistPeerList.setStatus("current")
_HwMeshWhitelistRowStatus_Type = RowStatus
_HwMeshWhitelistRowStatus_Object = MibTableColumn
hwMeshWhitelistRowStatus = _HwMeshWhitelistRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 42, 1, 3),
    _HwMeshWhitelistRowStatus_Type()
)
hwMeshWhitelistRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMeshWhitelistRowStatus.setStatus("current")
_HwWlanServiceManagementObject_ObjectIdentity = ObjectIdentity
hwWlanServiceManagementObject = _HwWlanServiceManagementObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43)
)
_HwLbsTagDevTable_Object = MibTable
hwLbsTagDevTable = _HwLbsTagDevTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 1)
)
if mibBuilder.loadTexts:
    hwLbsTagDevTable.setStatus("current")
_HwLbsTagDevEntry_Object = MibTableRow
hwLbsTagDevEntry = _HwLbsTagDevEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 1, 1)
)
hwLbsTagDevEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwLbsTagDevApID"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwLbsTagDevMac"),
)
if mibBuilder.loadTexts:
    hwLbsTagDevEntry.setStatus("current")
_HwLbsTagDevApID_Type = Integer32
_HwLbsTagDevApID_Object = MibTableColumn
hwLbsTagDevApID = _HwLbsTagDevApID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 1, 1, 1),
    _HwLbsTagDevApID_Type()
)
hwLbsTagDevApID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLbsTagDevApID.setStatus("current")
_HwLbsTagDevMac_Type = MacAddress
_HwLbsTagDevMac_Object = MibTableColumn
hwLbsTagDevMac = _HwLbsTagDevMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 1, 1, 2),
    _HwLbsTagDevMac_Type()
)
hwLbsTagDevMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLbsTagDevMac.setStatus("current")
_HwLbsTagDevType_Type = Integer32
_HwLbsTagDevType_Object = MibTableColumn
hwLbsTagDevType = _HwLbsTagDevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 1, 1, 3),
    _HwLbsTagDevType_Type()
)
hwLbsTagDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLbsTagDevType.setStatus("current")
_HwLbsTagDevChannel_Type = Integer32
_HwLbsTagDevChannel_Object = MibTableColumn
hwLbsTagDevChannel = _HwLbsTagDevChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 1, 1, 4),
    _HwLbsTagDevChannel_Type()
)
hwLbsTagDevChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLbsTagDevChannel.setStatus("current")
_HwLbsTagDevRssi_Type = Integer32
_HwLbsTagDevRssi_Object = MibTableColumn
hwLbsTagDevRssi = _HwLbsTagDevRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 1, 1, 5),
    _HwLbsTagDevRssi_Type()
)
hwLbsTagDevRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLbsTagDevRssi.setStatus("current")
_HwProxyTrackSideEquipTable_Object = MibTable
hwProxyTrackSideEquipTable = _HwProxyTrackSideEquipTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 2)
)
if mibBuilder.loadTexts:
    hwProxyTrackSideEquipTable.setStatus("current")
_HwProxyTrackSideEquipEntry_Object = MibTableRow
hwProxyTrackSideEquipEntry = _HwProxyTrackSideEquipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 2, 1)
)
hwProxyTrackSideEquipEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwProxyTrackSideEquipIndex"),
)
if mibBuilder.loadTexts:
    hwProxyTrackSideEquipEntry.setStatus("current")
_HwProxyTrackSideEquipIndex_Type = Integer32
_HwProxyTrackSideEquipIndex_Object = MibTableColumn
hwProxyTrackSideEquipIndex = _HwProxyTrackSideEquipIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 2, 1, 1),
    _HwProxyTrackSideEquipIndex_Type()
)
hwProxyTrackSideEquipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwProxyTrackSideEquipIndex.setStatus("current")
_HwProxyTrackSideEquipMac_Type = MacAddress
_HwProxyTrackSideEquipMac_Object = MibTableColumn
hwProxyTrackSideEquipMac = _HwProxyTrackSideEquipMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 2, 1, 2),
    _HwProxyTrackSideEquipMac_Type()
)
hwProxyTrackSideEquipMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwProxyTrackSideEquipMac.setStatus("current")


class _HwProxyTrackSideEquipVlanID_Type(Integer32):
    """Custom type hwProxyTrackSideEquipVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwProxyTrackSideEquipVlanID_Type.__name__ = "Integer32"
_HwProxyTrackSideEquipVlanID_Object = MibTableColumn
hwProxyTrackSideEquipVlanID = _HwProxyTrackSideEquipVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 2, 1, 3),
    _HwProxyTrackSideEquipVlanID_Type()
)
hwProxyTrackSideEquipVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwProxyTrackSideEquipVlanID.setStatus("current")
_HwProxyTrackSideEquipRowStatus_Type = RowStatus
_HwProxyTrackSideEquipRowStatus_Object = MibTableColumn
hwProxyTrackSideEquipRowStatus = _HwProxyTrackSideEquipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 2, 1, 4),
    _HwProxyTrackSideEquipRowStatus_Type()
)
hwProxyTrackSideEquipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwProxyTrackSideEquipRowStatus.setStatus("current")
_HwProxyOnBoardEquipTable_Object = MibTable
hwProxyOnBoardEquipTable = _HwProxyOnBoardEquipTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 3)
)
if mibBuilder.loadTexts:
    hwProxyOnBoardEquipTable.setStatus("current")
_HwProxyOnBoardEquipEntry_Object = MibTableRow
hwProxyOnBoardEquipEntry = _HwProxyOnBoardEquipEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 3, 1)
)
hwProxyOnBoardEquipEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwProxyOnBoardEquipIndex"),
)
if mibBuilder.loadTexts:
    hwProxyOnBoardEquipEntry.setStatus("current")
_HwProxyOnBoardEquipIndex_Type = Integer32
_HwProxyOnBoardEquipIndex_Object = MibTableColumn
hwProxyOnBoardEquipIndex = _HwProxyOnBoardEquipIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 3, 1, 1),
    _HwProxyOnBoardEquipIndex_Type()
)
hwProxyOnBoardEquipIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwProxyOnBoardEquipIndex.setStatus("current")
_HwProxyOnBoardEquipMac_Type = MacAddress
_HwProxyOnBoardEquipMac_Object = MibTableColumn
hwProxyOnBoardEquipMac = _HwProxyOnBoardEquipMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 3, 1, 2),
    _HwProxyOnBoardEquipMac_Type()
)
hwProxyOnBoardEquipMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwProxyOnBoardEquipMac.setStatus("current")


class _HwProxyOnBoardEquipVlanID_Type(Integer32):
    """Custom type hwProxyOnBoardEquipVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwProxyOnBoardEquipVlanID_Type.__name__ = "Integer32"
_HwProxyOnBoardEquipVlanID_Object = MibTableColumn
hwProxyOnBoardEquipVlanID = _HwProxyOnBoardEquipVlanID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 3, 1, 3),
    _HwProxyOnBoardEquipVlanID_Type()
)
hwProxyOnBoardEquipVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwProxyOnBoardEquipVlanID.setStatus("current")
_HwProxyOnBoardEquipRowStatus_Type = RowStatus
_HwProxyOnBoardEquipRowStatus_Object = MibTableColumn
hwProxyOnBoardEquipRowStatus = _HwProxyOnBoardEquipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 3, 1, 4),
    _HwProxyOnBoardEquipRowStatus_Type()
)
hwProxyOnBoardEquipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwProxyOnBoardEquipRowStatus.setStatus("current")
_HwHandoverTraceTable_Object = MibTable
hwHandoverTraceTable = _HwHandoverTraceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4)
)
if mibBuilder.loadTexts:
    hwHandoverTraceTable.setStatus("current")
_HwHandoverTraceEntry_Object = MibTableRow
hwHandoverTraceEntry = _HwHandoverTraceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1)
)
hwHandoverTraceEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwHandoverTraceIndex"),
)
if mibBuilder.loadTexts:
    hwHandoverTraceEntry.setStatus("current")
_HwHandoverTraceIndex_Type = Integer32
_HwHandoverTraceIndex_Object = MibTableColumn
hwHandoverTraceIndex = _HwHandoverTraceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 1),
    _HwHandoverTraceIndex_Type()
)
hwHandoverTraceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwHandoverTraceIndex.setStatus("current")


class _HwHandoverTimeStamp_Type(OctetString):
    """Custom type hwHandoverTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwHandoverTimeStamp_Type.__name__ = "OctetString"
_HwHandoverTimeStamp_Object = MibTableColumn
hwHandoverTimeStamp = _HwHandoverTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 2),
    _HwHandoverTimeStamp_Type()
)
hwHandoverTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHandoverTimeStamp.setStatus("current")
_HwHandoverFromApMac_Type = MacAddress
_HwHandoverFromApMac_Object = MibTableColumn
hwHandoverFromApMac = _HwHandoverFromApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 3),
    _HwHandoverFromApMac_Type()
)
hwHandoverFromApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHandoverFromApMac.setStatus("current")
_HwHandoverFromApRssi_Type = Integer32
_HwHandoverFromApRssi_Object = MibTableColumn
hwHandoverFromApRssi = _HwHandoverFromApRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 4),
    _HwHandoverFromApRssi_Type()
)
hwHandoverFromApRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHandoverFromApRssi.setStatus("current")
_HwHandoverToApMac_Type = MacAddress
_HwHandoverToApMac_Object = MibTableColumn
hwHandoverToApMac = _HwHandoverToApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 5),
    _HwHandoverToApMac_Type()
)
hwHandoverToApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHandoverToApMac.setStatus("current")
_HwHandoverToApRssi_Type = Integer32
_HwHandoverToApRssi_Object = MibTableColumn
hwHandoverToApRssi = _HwHandoverToApRssi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 6),
    _HwHandoverToApRssi_Type()
)
hwHandoverToApRssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHandoverToApRssi.setStatus("current")


class _HwHandoverFromApLocationID_Type(Unsigned32):
    """Custom type hwHandoverFromApLocationID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwHandoverFromApLocationID_Type.__name__ = "Unsigned32"
_HwHandoverFromApLocationID_Object = MibTableColumn
hwHandoverFromApLocationID = _HwHandoverFromApLocationID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 7),
    _HwHandoverFromApLocationID_Type()
)
hwHandoverFromApLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHandoverFromApLocationID.setStatus("current")


class _HwHandoverToApLocationID_Type(Unsigned32):
    """Custom type hwHandoverToApLocationID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwHandoverToApLocationID_Type.__name__ = "Unsigned32"
_HwHandoverToApLocationID_Object = MibTableColumn
hwHandoverToApLocationID = _HwHandoverToApLocationID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 4, 1, 8),
    _HwHandoverToApLocationID_Type()
)
hwHandoverToApLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwHandoverToApLocationID.setStatus("current")
_HwNeighborApTable_Object = MibTable
hwNeighborApTable = _HwNeighborApTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5)
)
if mibBuilder.loadTexts:
    hwNeighborApTable.setStatus("current")
_HwNeighborApEntry_Object = MibTableRow
hwNeighborApEntry = _HwNeighborApEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1)
)
hwNeighborApEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApLocalApId"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApLocalRadioId"),
)
if mibBuilder.loadTexts:
    hwNeighborApEntry.setStatus("current")
_HwNeighborApLocalApId_Type = Integer32
_HwNeighborApLocalApId_Object = MibTableColumn
hwNeighborApLocalApId = _HwNeighborApLocalApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 1),
    _HwNeighborApLocalApId_Type()
)
hwNeighborApLocalApId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNeighborApLocalApId.setStatus("current")
_HwNeighborApLocalRadioId_Type = Integer32
_HwNeighborApLocalRadioId_Object = MibTableColumn
hwNeighborApLocalRadioId = _HwNeighborApLocalRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 2),
    _HwNeighborApLocalRadioId_Type()
)
hwNeighborApLocalRadioId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNeighborApLocalRadioId.setStatus("current")
_HwNeighborApLocalApMac_Type = MacAddress
_HwNeighborApLocalApMac_Object = MibTableColumn
hwNeighborApLocalApMac = _HwNeighborApLocalApMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 3),
    _HwNeighborApLocalApMac_Type()
)
hwNeighborApLocalApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNeighborApLocalApMac.setStatus("current")


class _HwNeighborApIdList_Type(OctetString):
    """Custom type hwNeighborApIdList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1280),
    )


_HwNeighborApIdList_Type.__name__ = "OctetString"
_HwNeighborApIdList_Object = MibTableColumn
hwNeighborApIdList = _HwNeighborApIdList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 4),
    _HwNeighborApIdList_Type()
)
hwNeighborApIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNeighborApIdList.setStatus("current")


class _HwNeighborApMacList_Type(OctetString):
    """Custom type hwNeighborApMacList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3840),
    )


_HwNeighborApMacList_Type.__name__ = "OctetString"
_HwNeighborApMacList_Object = MibTableColumn
hwNeighborApMacList = _HwNeighborApMacList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 5),
    _HwNeighborApMacList_Type()
)
hwNeighborApMacList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNeighborApMacList.setStatus("current")


class _HwNeighborApRssiList_Type(OctetString):
    """Custom type hwNeighborApRssiList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1280),
    )


_HwNeighborApRssiList_Type.__name__ = "OctetString"
_HwNeighborApRssiList_Object = MibTableColumn
hwNeighborApRssiList = _HwNeighborApRssiList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 6),
    _HwNeighborApRssiList_Type()
)
hwNeighborApRssiList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNeighborApRssiList.setStatus("current")


class _HwNeighborApUpdateTime_Type(OctetString):
    """Custom type hwNeighborApUpdateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5120),
    )


_HwNeighborApUpdateTime_Type.__name__ = "OctetString"
_HwNeighborApUpdateTime_Object = MibTableColumn
hwNeighborApUpdateTime = _HwNeighborApUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 7),
    _HwNeighborApUpdateTime_Type()
)
hwNeighborApUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNeighborApUpdateTime.setStatus("current")


class _HwNeighborApLocalLocationID_Type(Unsigned32):
    """Custom type hwNeighborApLocalLocationID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_HwNeighborApLocalLocationID_Type.__name__ = "Unsigned32"
_HwNeighborApLocalLocationID_Object = MibTableColumn
hwNeighborApLocalLocationID = _HwNeighborApLocalLocationID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 8),
    _HwNeighborApLocalLocationID_Type()
)
hwNeighborApLocalLocationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNeighborApLocalLocationID.setStatus("current")


class _HwNeighborApLocationIDList_Type(OctetString):
    """Custom type hwNeighborApLocationIDList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1550),
    )


_HwNeighborApLocationIDList_Type.__name__ = "OctetString"
_HwNeighborApLocationIDList_Object = MibTableColumn
hwNeighborApLocationIDList = _HwNeighborApLocationIDList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 5, 1, 9),
    _HwNeighborApLocationIDList_Type()
)
hwNeighborApLocationIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNeighborApLocationIDList.setStatus("current")
_HwStaOnlineFailTable_Object = MibTable
hwStaOnlineFailTable = _HwStaOnlineFailTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6)
)
if mibBuilder.loadTexts:
    hwStaOnlineFailTable.setStatus("current")
_HwStaOnlineFailEntry_Object = MibTableRow
hwStaOnlineFailEntry = _HwStaOnlineFailEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1)
)
hwStaOnlineFailEntry.setIndexNames(
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwStaOnlineFailMacAddress"),
    (0, "HUAWEI-WLAN-SERVICE-MIB", "hwStaOnlineFailReasonIndex"),
)
if mibBuilder.loadTexts:
    hwStaOnlineFailEntry.setStatus("current")
_HwStaOnlineFailMacAddress_Type = MacAddress
_HwStaOnlineFailMacAddress_Object = MibTableColumn
hwStaOnlineFailMacAddress = _HwStaOnlineFailMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 1),
    _HwStaOnlineFailMacAddress_Type()
)
hwStaOnlineFailMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaOnlineFailMacAddress.setStatus("current")


class _HwStaOnlineFailReasonIndex_Type(Integer32):
    """Custom type hwStaOnlineFailReasonIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwStaOnlineFailReasonIndex_Type.__name__ = "Integer32"
_HwStaOnlineFailReasonIndex_Object = MibTableColumn
hwStaOnlineFailReasonIndex = _HwStaOnlineFailReasonIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 2),
    _HwStaOnlineFailReasonIndex_Type()
)
hwStaOnlineFailReasonIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwStaOnlineFailReasonIndex.setStatus("current")
_HwStaOnlineFailApId_Type = Integer32
_HwStaOnlineFailApId_Object = MibTableColumn
hwStaOnlineFailApId = _HwStaOnlineFailApId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 3),
    _HwStaOnlineFailApId_Type()
)
hwStaOnlineFailApId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaOnlineFailApId.setStatus("current")
_HwStaOnlineFailRadioId_Type = Integer32
_HwStaOnlineFailRadioId_Object = MibTableColumn
hwStaOnlineFailRadioId = _HwStaOnlineFailRadioId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 4),
    _HwStaOnlineFailRadioId_Type()
)
hwStaOnlineFailRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaOnlineFailRadioId.setStatus("current")
_HwStaOnlineFailWlanId_Type = Integer32
_HwStaOnlineFailWlanId_Object = MibTableColumn
hwStaOnlineFailWlanId = _HwStaOnlineFailWlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 5),
    _HwStaOnlineFailWlanId_Type()
)
hwStaOnlineFailWlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaOnlineFailWlanId.setStatus("current")
_HwStaOnlineFailLastFailTime_Type = OctetString
_HwStaOnlineFailLastFailTime_Object = MibTableColumn
hwStaOnlineFailLastFailTime = _HwStaOnlineFailLastFailTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 6),
    _HwStaOnlineFailLastFailTime_Type()
)
hwStaOnlineFailLastFailTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaOnlineFailLastFailTime.setStatus("current")
_HwStaOnlineFailReason_Type = OctetString
_HwStaOnlineFailReason_Object = MibTableColumn
hwStaOnlineFailReason = _HwStaOnlineFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 7),
    _HwStaOnlineFailReason_Type()
)
hwStaOnlineFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwStaOnlineFailReason.setStatus("current")
_HwStaOnlineFailRowStatus_Type = RowStatus
_HwStaOnlineFailRowStatus_Object = MibTableColumn
hwStaOnlineFailRowStatus = _HwStaOnlineFailRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 6, 1, 8),
    _HwStaOnlineFailRowStatus_Type()
)
hwStaOnlineFailRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaOnlineFailRowStatus.setStatus("current")
_HwStaOnlineFailTableInfo_ObjectIdentity = ObjectIdentity
hwStaOnlineFailTableInfo = _HwStaOnlineFailTableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 7)
)


class _HwStaResetAllOnlineFailTableReason_Type(Integer32):
    """Custom type hwStaResetAllOnlineFailTableReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HwStaResetAllOnlineFailTableReason_Type.__name__ = "Integer32"
_HwStaResetAllOnlineFailTableReason_Object = MibScalar
hwStaResetAllOnlineFailTableReason = _HwStaResetAllOnlineFailTableReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 43, 7, 1),
    _HwStaResetAllOnlineFailTableReason_Type()
)
hwStaResetAllOnlineFailTableReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwStaResetAllOnlineFailTableReason.setStatus("current")
_HwWlanServiceManagementConformance_ObjectIdentity = ObjectIdentity
hwWlanServiceManagementConformance = _HwWlanServiceManagementConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44)
)
_HwWlanServiceManagementCompliances_ObjectIdentity = ObjectIdentity
hwWlanServiceManagementCompliances = _HwWlanServiceManagementCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 1)
)
_HwWlanServiceManagementObjectGroups_ObjectIdentity = ObjectIdentity
hwWlanServiceManagementObjectGroups = _HwWlanServiceManagementObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2)
)

# Managed Objects groups

hwEssManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 1)
)
hwEssManagementGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssHideSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssUserIsolate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssType"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssTrafficProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSecurityProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssMaxUserNumber"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssAssociationTimeOut"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssIgmpMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssRowStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssForwardMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVlan"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssDhcpSnooping"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssServiceVlanEnable"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssIPSGEnable"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssDhcpTrustPort"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssDaiSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssArpThreshold"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssTunnelProtocol"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssOfflineManagement"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssBlacklistProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssWhitelistProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssStaAccessMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssDhcpOption82InsertSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssDhcpOption82RemoteIdFormat"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssDhcpSnoopingOption"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssBroadCastPps"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssMultiCastPps"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssUniCastPps"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssBroadCastSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssMultiCastSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssUniCastSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNameInbound"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNameOutbound"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNumInbound"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNumOutbound"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclSwtichInbound"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclSwtichOutbound"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssServiceModeSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssAutoOffEssAdminSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssAutoOffEssStartTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssAutoOffEssEndTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssNdSnooping"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNameInboundIPv6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNameOutboundIPv6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNumInboundIPv6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclNumOutboundIPv6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclSwtichInboundIPv6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssSaclSwtichOutboundIPv6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssNdTrustPort"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssMldSnoopingEable"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssIPSGEnableRejectAssoc"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssLearnClientIpEnable"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssHomeAgent"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceEssVlanMobilityGroup"))
)
if mibBuilder.loadTexts:
    hwEssManagementGroup.setStatus("current")

hwVapManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 2)
)
hwVapManagementGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapWlanIndex"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapRowStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapSSID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapVlan"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapFrequency"))
)
if mibBuilder.loadTexts:
    hwVapManagementGroup.setStatus("current")

hwServiceBatchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 3)
)
hwServiceBatchGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchRadioProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchEssNameNumber"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchEssNameList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchRowStatus"))
)
if mibBuilder.loadTexts:
    hwServiceBatchGroup.setStatus("current")

hwCapwapConfigManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 4)
)
hwCapwapConfigManagementGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceCapwapConfigCommit")
)
if mibBuilder.loadTexts:
    hwCapwapConfigManagementGroup.setStatus("current")

hwStationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 5)
)
hwStationGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaApId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaRadioId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaEssName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaSsid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaOnlineTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaSnrUs"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceStaRxPowerUs"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatTxPkts"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatRxPkts"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatTxBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatRxBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatTxRate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatRxRate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAccessChannel"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaIp"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaNoise"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaVlan"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRecvDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaSendDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRecvErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaSendErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaReSendFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaReSendBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaUsername"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatRxBytes64Bits"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatTxBytes64Bits"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaGateway"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAuthenMethod"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaEncryptMethod"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaBSSID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaQosMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaHtMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaMcsVal"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaShortGIStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRoamStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaStatOperMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatTxPkts64Bits"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWirelessStatRxPkts64Bits"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRfMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaIpV6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAssociateTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAccessTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAccessOnlineTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaLinkRxRate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaLinkTxRate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaActualBandwidth"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaPackets"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaChannelUtilRate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaChannelBusyRate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaChannelFreeRate"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaChannelInterfRate"))
)
if mibBuilder.loadTexts:
    hwStationGroup.setStatus("current")

hwVapStationListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 6)
)
hwVapStationListGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapStaMacList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapAssociatedStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapCurOnlineStaCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapStaAssocAndReAssocReqCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceVapStaOnlineTime"))
)
if mibBuilder.loadTexts:
    hwVapStationListGroup.setStatus("current")

hwWlanServiceBatchEssInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 7)
)
hwWlanServiceBatchEssInfoGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchEssStartNumber"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchEssNumber"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchReturnEssNumber"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchEssName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWlanServiceBatchEssSsid"))
)
if mibBuilder.loadTexts:
    hwWlanServiceBatchEssInfoGroup.setStatus("current")

hwApAssocStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 8)
)
hwApAssocStatGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwTotalOnlineTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwTotalAssociatedStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwCurrAssociatedStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAssociationRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAssociationRejectCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAssociationFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwReAssociationRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwReAssociationRejectCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwReAssociationFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwDisAssocOfUserNotifiedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwDisAssocOfStaRoamCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwDisAssocOfStaAgeCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwDisAssocOfApUnableHandleCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwDisAssocOfOtherReasonsCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAssocRequestCntByResource"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaExceptionalOfflineCnt"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwReAssociationSuccessCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBSSNotSupportAssocFailCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAccessRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAccessRequestFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAuthenRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAuthenRequestFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwRefusedStaNumByResource"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAssocAndReAssocRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaAuthenRequestSuccessCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwL3RoamInStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwL3RoamOutStationCount"))
)
if mibBuilder.loadTexts:
    hwApAssocStatGroup.setStatus("current")

hwVlanMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 9)
)
hwVlanMappingGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingEssVlanMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingEssVlanId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList0"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList1"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList2"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList3"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList4"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList5"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList6"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwVlanMappingVlanList7"))
)
if mibBuilder.loadTexts:
    hwVlanMappingGroup.setStatus("current")

hwGlobalStaMacWhiteListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 10)
)
hwGlobalStaMacWhiteListGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwGlobalStaMacWhiteListRowStatus")
)
if mibBuilder.loadTexts:
    hwGlobalStaMacWhiteListGroup.setStatus("current")

hwStaMacBlackListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 11)
)
hwStaMacBlackListGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwStaMacBlackListRowStatus")
)
if mibBuilder.loadTexts:
    hwStaMacBlackListGroup.setStatus("current")

hwApStaAccessControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 12)
)
hwApStaAccessControlGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwApStaAccessControlMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApStaAccessControlRowStatus"))
)
if mibBuilder.loadTexts:
    hwApStaAccessControlGroup.setStatus("current")

hwAcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 13)
)
hwAcStatisticsGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwAcReassocSuccessTimes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApPerformanceStatTimerLen"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwRtCollectOnoff"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApNormalCollectCycle"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApRtCollectCycle"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAcCurAssocStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAcCurAuthSuccessStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAcCurJointApNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAcCurAssoc24gStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAcCurAssoc5gStaNum"))
)
if mibBuilder.loadTexts:
    hwAcStatisticsGroup.setStatus("current")

hwMacVapManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 14)
)
hwMacVapManagementGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapWlanIndex"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapRowStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapSSID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapVlan"))
)
if mibBuilder.loadTexts:
    hwMacVapManagementGroup.setStatus("current")

hwMacCapwapConfigManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 15)
)
hwMacCapwapConfigManagementGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceCapwapConfigCommit")
)
if mibBuilder.loadTexts:
    hwMacCapwapConfigManagementGroup.setStatus("current")

hwMacVapStationListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 16)
)
hwMacVapStationListGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaMacList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapAssociatedStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapCurOnlineStaCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaAssocAndReAssocReqCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacWlanServiceVapStaOnlineTime"))
)
if mibBuilder.loadTexts:
    hwMacVapStationListGroup.setStatus("current")

hwMacApAssocStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 17)
)
hwMacApAssocStatGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacTotalOnlineTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacTotalAssociatedStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacCurrAssociatedStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacAssociationRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacAssociationRejectCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacAssociationFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacReAssociationRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacReAssociationRejectCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacReAssociationFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacDisAssocOfUserNotifiedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacDisAssocOfStaRoamCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacDisAssocOfStaAgeCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacDisAssocOfApUnableHandleCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacDisAssocOfOtherReasonsCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacAssocRequestCntByResource"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaExceptionalOfflineCnt"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacReAssociationSuccessCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBSSNotSupportAssocFailCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaAccessRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaAccessRequestFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaAuthenRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaAuthenRequestFailedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacRefusedStaNumByResource"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaAssocAndReAssocRequestCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaAuthenRequestSuccessCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwL3RoamInStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwL3RoamOutStationCount"))
)
if mibBuilder.loadTexts:
    hwMacApAssocStatGroup.setStatus("current")

hwVapConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 18)
)
hwVapConfigGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwVapOptValue")
)
if mibBuilder.loadTexts:
    hwVapConfigGroup.setStatus("current")

hwSsidStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 19)
)
hwSsidStatisticGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportRecvBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportRecvErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportRecvFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportRecvUnicastFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportRecvDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportTransmitBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportTransmitErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportTransmitFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportTransmitUnicastFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportTransmitDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportDownReTransmitFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidCurrentStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportNoise"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwSsidAirportSNR"))
)
if mibBuilder.loadTexts:
    hwSsidStatisticGroup.setStatus("current")

hwMacSsidStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 20)
)
hwMacSsidStatisticGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportRecvBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportRecvErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportRecvFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportRecvUnicastFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportRecvDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportTransmitBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportTransmitErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportTransmitFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportTransmitUnicastFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportTransmitDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportDownReTransmitFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidCurrentStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportNoise"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacSsidAirportSNR"))
)
if mibBuilder.loadTexts:
    hwMacSsidStatisticGroup.setStatus("current")

hwMacApStaAccessControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 21)
)
hwMacApStaAccessControlGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaAccessControlMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaAccessControlRowStatus"))
)
if mibBuilder.loadTexts:
    hwMacApStaAccessControlGroup.setStatus("current")

hwApStaInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 22)
)
hwApStaInfoGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwStaMAC"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaIPAddress"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWMMAttr"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRadioMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaRadioChannel"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwAPTxRates"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaPowerSaveMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaVlanId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaSSIDName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApStaTxPacket"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApStaRxPacket"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApStaStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApStaBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApStaRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwApStaSnr"))
)
if mibBuilder.loadTexts:
    hwApStaInfoGroup.setStatus("current")

hwMacApStaInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 23)
)
hwMacApStaInfoGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaMAC"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaIPAddress"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaWMMAttr"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaRadioMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaRadioChannel"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacAPTxRates"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaPowerSaveMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaVlanId"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacStaSSIDName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaTxPacket"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaRxPacket"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaBssid"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacApStaSnr"))
)
if mibBuilder.loadTexts:
    hwMacApStaInfoGroup.setStatus("current")

hwInterACRoamingInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 24)
)
hwInterACRoamingInfoGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwInterACRoamingInSuccCnt"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwInterACRoamingOutSuccCnt"))
)
if mibBuilder.loadTexts:
    hwInterACRoamingInfoGroup.setStatus("current")

hwRadioStaListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 25)
)
hwRadioStaListGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwRadioStaNumber"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwRadioStaMacList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwRadioStaTotalAssociatedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwRadioStaAccessReqCount"))
)
if mibBuilder.loadTexts:
    hwRadioStaListGroup.setStatus("current")

hwMacRadioStaListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 26)
)
hwMacRadioStaListGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacRadioStaNumber"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacRadioStaMacList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacRadioStaTotalAssociatedCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacRadioStaAccessReqCount"))
)
if mibBuilder.loadTexts:
    hwMacRadioStaListGroup.setStatus("current")

hwBridgeProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 27)
)
hwBridgeProfileGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeProfileBridgeName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeProfileSecurityProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeProfileVlanTagged"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeProfileRowStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeProfileDhcpTrustPort"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeProfileNdTrustPort"))
)
if mibBuilder.loadTexts:
    hwBridgeProfileGroup.setStatus("current")

hwBridgeVapManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 28)
)
hwBridgeVapManagementGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeVapRowStatus")
)
if mibBuilder.loadTexts:
    hwBridgeVapManagementGroup.setStatus("current")

hwMacBridgeVapManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 29)
)
hwMacBridgeVapManagementGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeVapRowStatus")
)
if mibBuilder.loadTexts:
    hwMacBridgeVapManagementGroup.setStatus("current")

hwBridgeLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 30)
)
hwBridgeLinkGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkWlanID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkBridgeType"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkBridgeSubType"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkPeerMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkBridgeProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkStpMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkInstanceIdList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkInstanceStateList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkBridgeMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkCoverageDistance"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkPeerAPID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkPeerAPStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkMaxRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkPeerApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeLinkChannelID"))
)
if mibBuilder.loadTexts:
    hwBridgeLinkGroup.setStatus("current")

hwMacBridgeLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 31)
)
hwMacBridgeLinkGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkWlanID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkBridgeType"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkBridgeSubType"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkPeerMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkBridgeProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkStpMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkInstanceIdList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkInstanceStateList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkApID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkBridgeMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkCoverageDistance"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkPeerAPID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkPeerAPStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkMaxRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeLinkPeerApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacBridgeChannelID"))
)
if mibBuilder.loadTexts:
    hwMacBridgeLinkGroup.setStatus("current")

hwBridgeWhitelistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 32)
)
hwBridgeWhitelistGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeWhitelistPeerList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwBridgeWhitelistRowStatus"))
)
if mibBuilder.loadTexts:
    hwBridgeWhitelistGroup.setStatus("current")

hwWirelessSsidStatisticGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 33)
)
hwWirelessSsidStatisticGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportTransmitUnicastFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportTransmitFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportTransmitErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportDownReTransmitFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportTransmitDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportTransmitBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportRecvUnicastFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportRecvFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportRecvErrorFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportRecvDropFrames"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidAirportRecvBytes"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidTotalAssociatedSuccessStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidCurAssocStationCount"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwWirelessSsidTotalAssociatedFailedStationCount"))
)
if mibBuilder.loadTexts:
    hwWirelessSsidStatisticGroup.setStatus("current")

hwStaBlacklistProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 34)
)
hwStaBlacklistProfileGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwStaBlacklistProfileStaMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaBlacklistProfileOper"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaBlacklistProfileStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaBlacklistProfileStaList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaBlacklistProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwStaBlacklistProfileGroup.setStatus("current")

hwStaWhitelistProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 35)
)
hwStaWhitelistProfileGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwStaWhitelistProfileStaMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWhitelistProfileOper"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWhitelistProfileStaNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWhitelistProfileStaList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwStaWhitelistProfileRowStatus"))
)
if mibBuilder.loadTexts:
    hwStaWhitelistProfileGroup.setStatus("current")

hwMeshProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 36)
)
hwMeshProfileGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileSecurityProfileName"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileMeshID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileMaxLinkNum"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileRssiThreshold"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileReportInterval"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileRowStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileDhcpTrustPort"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileNdTrustPort"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileQuickHoSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileLinkHoThreshold"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileLinkHoldPeriod"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileLinkLinkSaturationThreshold"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileLinkProbePeriod"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileFwaMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileFwaEdcaMode"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileQuickHandoverMinRssiThreshold"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileLocationBasedHandoverAlgorithmSwitch"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileMovingDirection"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileHandoverAlgorithmPNCriteriaObserveTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileUrgentHandoverLowRateThreshold"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileUrgentHandoverLowRatePeriod"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileUrgentHandoverPunishmentPeriod"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshProfileUrgentHandoverPunishmentRssi"))
)
if mibBuilder.loadTexts:
    hwMeshProfileGroup.setStatus("current")

hwMeshVapManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 37)
)
hwMeshVapManagementGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshVapRowStatus")
)
if mibBuilder.loadTexts:
    hwMeshVapManagementGroup.setStatus("current")

hwMacMeshVapManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 38)
)
hwMacMeshVapManagementGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshVapRowStatus")
)
if mibBuilder.loadTexts:
    hwMacMeshVapManagementGroup.setStatus("current")

hwMeshLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 39)
)
hwMeshLinkGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkWlanID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkPeerMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkChannelID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkRssiValue"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkMeshRole"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkCoverageDistance"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkPeerAPStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkMaxRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshLinkPeerApMac"))
)
if mibBuilder.loadTexts:
    hwMeshLinkGroup.setStatus("current")

hwMacMeshLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 40)
)
hwMacMeshLinkGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkWlanID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkPeerMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkChannelID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkRssiValue"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkApID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkMeshRole"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkCoverageDistance"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkPeerAPID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkPeerAPStatus"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkMaxRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMacMeshLinkPeerApMac"))
)
if mibBuilder.loadTexts:
    hwMacMeshLinkGroup.setStatus("current")

hwMeshWhitelistGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 41)
)
hwMeshWhitelistGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwMeshWhitelistPeerList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwMeshWhitelistRowStatus"))
)
if mibBuilder.loadTexts:
    hwMeshWhitelistGroup.setStatus("current")

hwWlanServiceManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 42)
)
hwWlanServiceManagementGroup.setObjects(
    ("HUAWEI-WLAN-SERVICE-MIB", "hwCapwapConfigCommitAll")
)
if mibBuilder.loadTexts:
    hwWlanServiceManagementGroup.setStatus("current")

hwLbsTagDevGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 43)
)
hwLbsTagDevGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwLbsTagDevType"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwLbsTagDevChannel"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwLbsTagDevRssi"))
)
if mibBuilder.loadTexts:
    hwLbsTagDevGroup.setStatus("current")

hwProxyTrackSideEquipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 44)
)
hwProxyTrackSideEquipGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwProxyTrackSideEquipMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwProxyTrackSideEquipVlanID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwProxyTrackSideEquipRowStatus"))
)
if mibBuilder.loadTexts:
    hwProxyTrackSideEquipGroup.setStatus("current")

hwProxyOnBoardEquipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 45)
)
hwProxyOnBoardEquipGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwProxyOnBoardEquipMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwProxyOnBoardEquipVlanID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwProxyOnBoardEquipRowStatus"))
)
if mibBuilder.loadTexts:
    hwProxyOnBoardEquipGroup.setStatus("current")

hwHandoverTraceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 46)
)
hwHandoverTraceGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwHandoverTimeStamp"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwHandoverFromApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwHandoverFromApRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwHandoverToApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwHandoverToApRssi"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwHandoverFromApLocationID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwHandoverToApLocationID"))
)
if mibBuilder.loadTexts:
    hwHandoverTraceGroup.setStatus("current")

hwNeighborApGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 2, 47)
)
hwNeighborApGroup.setObjects(
      *(("HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApLocalApMac"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApIdList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApMacList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApRssiList"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApUpdateTime"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApLocalLocationID"),
        ("HUAWEI-WLAN-SERVICE-MIB", "hwNeighborApLocationIDList"))
)
if mibBuilder.loadTexts:
    hwNeighborApGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwWlanServiceManagementCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 139, 4, 44, 1, 1)
)
if mibBuilder.loadTexts:
    hwWlanServiceManagementCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-WLAN-SERVICE-MIB",
    **{"hwWlanServiceManagement": hwWlanServiceManagement,
       "hwEssManagementTable": hwEssManagementTable,
       "hwEssManagementEntry": hwEssManagementEntry,
       "hwWlanServiceEssName": hwWlanServiceEssName,
       "hwWlanServiceEssSsid": hwWlanServiceEssSsid,
       "hwWlanServiceEssHideSsid": hwWlanServiceEssHideSsid,
       "hwWlanServiceEssUserIsolate": hwWlanServiceEssUserIsolate,
       "hwWlanServiceEssType": hwWlanServiceEssType,
       "hwWlanServiceEssTrafficProfileName": hwWlanServiceEssTrafficProfileName,
       "hwWlanServiceEssSecurityProfileName": hwWlanServiceEssSecurityProfileName,
       "hwWlanServiceEssMaxUserNumber": hwWlanServiceEssMaxUserNumber,
       "hwWlanServiceEssAssociationTimeOut": hwWlanServiceEssAssociationTimeOut,
       "hwWlanServiceEssIgmpMode": hwWlanServiceEssIgmpMode,
       "hwWlanServiceEssRowStatus": hwWlanServiceEssRowStatus,
       "hwWlanServiceEssForwardMode": hwWlanServiceEssForwardMode,
       "hwWlanServiceEssNum": hwWlanServiceEssNum,
       "hwWlanServiceVlan": hwWlanServiceVlan,
       "hwWlanServiceEssDhcpSnooping": hwWlanServiceEssDhcpSnooping,
       "hwWlanServiceEssServiceVlanEnable": hwWlanServiceEssServiceVlanEnable,
       "hwWlanServiceEssIPSGEnable": hwWlanServiceEssIPSGEnable,
       "hwWlanServiceEssDhcpTrustPort": hwWlanServiceEssDhcpTrustPort,
       "hwWlanServiceEssDaiSwitch": hwWlanServiceEssDaiSwitch,
       "hwWlanServiceEssArpThreshold": hwWlanServiceEssArpThreshold,
       "hwWlanServiceEssTunnelProtocol": hwWlanServiceEssTunnelProtocol,
       "hwWlanServiceEssStatus": hwWlanServiceEssStatus,
       "hwWlanServiceEssOfflineManagement": hwWlanServiceEssOfflineManagement,
       "hwWlanServiceEssBlacklistProfileName": hwWlanServiceEssBlacklistProfileName,
       "hwWlanServiceEssWhitelistProfileName": hwWlanServiceEssWhitelistProfileName,
       "hwWlanServiceEssStaAccessMode": hwWlanServiceEssStaAccessMode,
       "hwWlanServiceEssDhcpOption82InsertSwitch": hwWlanServiceEssDhcpOption82InsertSwitch,
       "hwWlanServiceEssDhcpOption82RemoteIdFormat": hwWlanServiceEssDhcpOption82RemoteIdFormat,
       "hwWlanServiceEssDhcpSnoopingOption": hwWlanServiceEssDhcpSnoopingOption,
       "hwWlanServiceEssBroadCastPps": hwWlanServiceEssBroadCastPps,
       "hwWlanServiceEssMultiCastPps": hwWlanServiceEssMultiCastPps,
       "hwWlanServiceEssUniCastPps": hwWlanServiceEssUniCastPps,
       "hwWlanServiceEssBroadCastSwitch": hwWlanServiceEssBroadCastSwitch,
       "hwWlanServiceEssMultiCastSwitch": hwWlanServiceEssMultiCastSwitch,
       "hwWlanServiceEssUniCastSwitch": hwWlanServiceEssUniCastSwitch,
       "hwWlanServiceEssSaclNameInbound": hwWlanServiceEssSaclNameInbound,
       "hwWlanServiceEssSaclNameOutbound": hwWlanServiceEssSaclNameOutbound,
       "hwWlanServiceEssSaclNumInbound": hwWlanServiceEssSaclNumInbound,
       "hwWlanServiceEssSaclNumOutbound": hwWlanServiceEssSaclNumOutbound,
       "hwWlanServiceEssSaclSwtichInbound": hwWlanServiceEssSaclSwtichInbound,
       "hwWlanServiceEssSaclSwtichOutbound": hwWlanServiceEssSaclSwtichOutbound,
       "hwWlanServiceEssServiceModeSwitch": hwWlanServiceEssServiceModeSwitch,
       "hwWlanServiceEssAutoOffEssAdminSwitch": hwWlanServiceEssAutoOffEssAdminSwitch,
       "hwWlanServiceEssAutoOffEssStartTime": hwWlanServiceEssAutoOffEssStartTime,
       "hwWlanServiceEssAutoOffEssEndTime": hwWlanServiceEssAutoOffEssEndTime,
       "hwWlanServiceEssNdSnooping": hwWlanServiceEssNdSnooping,
       "hwWlanServiceEssSaclNameInboundIPv6": hwWlanServiceEssSaclNameInboundIPv6,
       "hwWlanServiceEssSaclNameOutboundIPv6": hwWlanServiceEssSaclNameOutboundIPv6,
       "hwWlanServiceEssSaclNumInboundIPv6": hwWlanServiceEssSaclNumInboundIPv6,
       "hwWlanServiceEssSaclNumOutboundIPv6": hwWlanServiceEssSaclNumOutboundIPv6,
       "hwWlanServiceEssSaclSwtichInboundIPv6": hwWlanServiceEssSaclSwtichInboundIPv6,
       "hwWlanServiceEssSaclSwtichOutboundIPv6": hwWlanServiceEssSaclSwtichOutboundIPv6,
       "hwWlanServiceEssNdTrustPort": hwWlanServiceEssNdTrustPort,
       "hwWlanServiceEssMldSnoopingEable": hwWlanServiceEssMldSnoopingEable,
       "hwWlanServiceEssIPSGEnableRejectAssoc": hwWlanServiceEssIPSGEnableRejectAssoc,
       "hwWlanServiceEssLearnClientIpEnable": hwWlanServiceEssLearnClientIpEnable,
       "hwWlanServiceEssHomeAgent": hwWlanServiceEssHomeAgent,
       "hwWlanServiceEssVlanMobilityGroup": hwWlanServiceEssVlanMobilityGroup,
       "hwVapManagementTable": hwVapManagementTable,
       "hwVapManagementEntry": hwVapManagementEntry,
       "hwWlanServiceVapApIndex": hwWlanServiceVapApIndex,
       "hwWlanServiceVapRadioIndex": hwWlanServiceVapRadioIndex,
       "hwWlanServiceVapEssName": hwWlanServiceVapEssName,
       "hwWlanServiceVapWlanIndex": hwWlanServiceVapWlanIndex,
       "hwWlanServiceVapRowStatus": hwWlanServiceVapRowStatus,
       "hwWlanServiceVapBssid": hwWlanServiceVapBssid,
       "hwWlanServiceVapSSID": hwWlanServiceVapSSID,
       "hwWlanServiceVapVlan": hwWlanServiceVapVlan,
       "hwWlanServiceVapFrequency": hwWlanServiceVapFrequency,
       "hwServiceBatchTable": hwServiceBatchTable,
       "hwServiceBatchEntry": hwServiceBatchEntry,
       "hwWlanServiceBatchApType": hwWlanServiceBatchApType,
       "hwWlanServiceBatchRadioIndex": hwWlanServiceBatchRadioIndex,
       "hwWlanServiceBatchRadioProfileName": hwWlanServiceBatchRadioProfileName,
       "hwWlanServiceBatchEssNameNumber": hwWlanServiceBatchEssNameNumber,
       "hwWlanServiceBatchEssNameList": hwWlanServiceBatchEssNameList,
       "hwWlanServiceBatchRowStatus": hwWlanServiceBatchRowStatus,
       "hwCapwapConfigManagementTable": hwCapwapConfigManagementTable,
       "hwCapwapConfigManagementEntry": hwCapwapConfigManagementEntry,
       "hwWlanServiceCapwapConfigApIndex": hwWlanServiceCapwapConfigApIndex,
       "hwWlanServiceCapwapConfigCommit": hwWlanServiceCapwapConfigCommit,
       "hwStationTable": hwStationTable,
       "hwStationEntry": hwStationEntry,
       "hwWlanServiceStaMac": hwWlanServiceStaMac,
       "hwWlanServiceStaApId": hwWlanServiceStaApId,
       "hwWlanServiceStaRadioId": hwWlanServiceStaRadioId,
       "hwWlanServiceStaEssName": hwWlanServiceStaEssName,
       "hwWlanServiceStaSsid": hwWlanServiceStaSsid,
       "hwWlanServiceStaOnlineTime": hwWlanServiceStaOnlineTime,
       "hwWlanServiceStaSnrUs": hwWlanServiceStaSnrUs,
       "hwWlanServiceStaRxPowerUs": hwWlanServiceStaRxPowerUs,
       "hwStaWirelessStatTxPkts": hwStaWirelessStatTxPkts,
       "hwStaWirelessStatRxPkts": hwStaWirelessStatRxPkts,
       "hwStaWirelessStatTxBytes": hwStaWirelessStatTxBytes,
       "hwStaWirelessStatRxBytes": hwStaWirelessStatRxBytes,
       "hwStaWirelessStatTxRate": hwStaWirelessStatTxRate,
       "hwStaWirelessStatRxRate": hwStaWirelessStatRxRate,
       "hwStaAccessChannel": hwStaAccessChannel,
       "hwStaIp": hwStaIp,
       "hwStaRssi": hwStaRssi,
       "hwStaNoise": hwStaNoise,
       "hwStaVlan": hwStaVlan,
       "hwStaRecvDropFrames": hwStaRecvDropFrames,
       "hwStaSendDropFrames": hwStaSendDropFrames,
       "hwStaRecvErrorFrames": hwStaRecvErrorFrames,
       "hwStaSendErrorFrames": hwStaSendErrorFrames,
       "hwStaReSendFrames": hwStaReSendFrames,
       "hwStaReSendBytes": hwStaReSendBytes,
       "hwStaUsername": hwStaUsername,
       "hwStaStatus": hwStaStatus,
       "hwStaWirelessStatRxBytes64Bits": hwStaWirelessStatRxBytes64Bits,
       "hwStaWirelessStatTxBytes64Bits": hwStaWirelessStatTxBytes64Bits,
       "hwStaGateway": hwStaGateway,
       "hwStaAuthenMethod": hwStaAuthenMethod,
       "hwStaEncryptMethod": hwStaEncryptMethod,
       "hwStaBSSID": hwStaBSSID,
       "hwStaQosMode": hwStaQosMode,
       "hwStaHtMode": hwStaHtMode,
       "hwStaMcsVal": hwStaMcsVal,
       "hwStaShortGIStatus": hwStaShortGIStatus,
       "hwStaRoamStatus": hwStaRoamStatus,
       "hwStaStatOperMode": hwStaStatOperMode,
       "hwStaWirelessStatTxPkts64Bits": hwStaWirelessStatTxPkts64Bits,
       "hwStaWirelessStatRxPkts64Bits": hwStaWirelessStatRxPkts64Bits,
       "hwStaRfMode": hwStaRfMode,
       "hwStaIpV6": hwStaIpV6,
       "hwStaAssociateTime": hwStaAssociateTime,
       "hwStaAccessTime": hwStaAccessTime,
       "hwStaAccessOnlineTime": hwStaAccessOnlineTime,
       "hwStaLinkRxRate": hwStaLinkRxRate,
       "hwStaLinkTxRate": hwStaLinkTxRate,
       "hwStaActualBandwidth": hwStaActualBandwidth,
       "hwStaPackets": hwStaPackets,
       "hwStaChannelUtilRate": hwStaChannelUtilRate,
       "hwStaChannelBusyRate": hwStaChannelBusyRate,
       "hwStaChannelFreeRate": hwStaChannelFreeRate,
       "hwStaChannelInterfRate": hwStaChannelInterfRate,
       "hwVapStationListTable": hwVapStationListTable,
       "hwVapStationListEntry": hwVapStationListEntry,
       "hwWlanServiceVapStaApId": hwWlanServiceVapStaApId,
       "hwWlanServiceVapStaRadioId": hwWlanServiceVapStaRadioId,
       "hwWlanServiceVapStaEssName": hwWlanServiceVapStaEssName,
       "hwWlanServiceVapStaNum": hwWlanServiceVapStaNum,
       "hwWlanServiceVapStaMacList": hwWlanServiceVapStaMacList,
       "hwWlanServiceVapAssociatedStationCount": hwWlanServiceVapAssociatedStationCount,
       "hwWlanServiceVapCurOnlineStaCount": hwWlanServiceVapCurOnlineStaCount,
       "hwWlanServiceVapStaAssocAndReAssocReqCount": hwWlanServiceVapStaAssocAndReAssocReqCount,
       "hwWlanServiceVapStaOnlineTime": hwWlanServiceVapStaOnlineTime,
       "hwWlanServiceBatchEssInfo": hwWlanServiceBatchEssInfo,
       "hwWlanServiceBatchEssStartNumber": hwWlanServiceBatchEssStartNumber,
       "hwWlanServiceBatchEssNumber": hwWlanServiceBatchEssNumber,
       "hwWlanServiceBatchReturnEssNumber": hwWlanServiceBatchReturnEssNumber,
       "hwWlanServiceBatchEssName": hwWlanServiceBatchEssName,
       "hwWlanServiceBatchEssSsid": hwWlanServiceBatchEssSsid,
       "hwCapwapConfigCommitAll": hwCapwapConfigCommitAll,
       "hwApAssocStatTable": hwApAssocStatTable,
       "hwApAssocStatEntry": hwApAssocStatEntry,
       "hwApAssocStatApId": hwApAssocStatApId,
       "hwTotalOnlineTime": hwTotalOnlineTime,
       "hwTotalAssociatedStationCount": hwTotalAssociatedStationCount,
       "hwCurrAssociatedStationCount": hwCurrAssociatedStationCount,
       "hwAssociationRequestCount": hwAssociationRequestCount,
       "hwAssociationRejectCount": hwAssociationRejectCount,
       "hwAssociationFailedCount": hwAssociationFailedCount,
       "hwReAssociationRequestCount": hwReAssociationRequestCount,
       "hwReAssociationRejectCount": hwReAssociationRejectCount,
       "hwReAssociationFailedCount": hwReAssociationFailedCount,
       "hwDisAssocOfUserNotifiedCount": hwDisAssocOfUserNotifiedCount,
       "hwDisAssocOfStaRoamCount": hwDisAssocOfStaRoamCount,
       "hwDisAssocOfStaAgeCount": hwDisAssocOfStaAgeCount,
       "hwDisAssocOfApUnableHandleCount": hwDisAssocOfApUnableHandleCount,
       "hwDisAssocOfOtherReasonsCount": hwDisAssocOfOtherReasonsCount,
       "hwAssocRequestCntByResource": hwAssocRequestCntByResource,
       "hwStaExceptionalOfflineCnt": hwStaExceptionalOfflineCnt,
       "hwReAssociationSuccessCount": hwReAssociationSuccessCount,
       "hwBSSNotSupportAssocFailCount": hwBSSNotSupportAssocFailCount,
       "hwStaAccessRequestCount": hwStaAccessRequestCount,
       "hwStaAccessRequestFailedCount": hwStaAccessRequestFailedCount,
       "hwStaAuthenRequestCount": hwStaAuthenRequestCount,
       "hwStaAuthenRequestFailedCount": hwStaAuthenRequestFailedCount,
       "hwRefusedStaNumByResource": hwRefusedStaNumByResource,
       "hwStaAssocAndReAssocRequestCount": hwStaAssocAndReAssocRequestCount,
       "hwStaAuthenRequestSuccessCount": hwStaAuthenRequestSuccessCount,
       "hwL3RoamInStationCount": hwL3RoamInStationCount,
       "hwL3RoamOutStationCount": hwL3RoamOutStationCount,
       "hwVlanMappingTable": hwVlanMappingTable,
       "hwVlanMappingEntry": hwVlanMappingEntry,
       "hwVlanMappingEssName": hwVlanMappingEssName,
       "hwVlanMappingEssVlanMode": hwVlanMappingEssVlanMode,
       "hwVlanMappingEssVlanId": hwVlanMappingEssVlanId,
       "hwVlanMappingVlanList0": hwVlanMappingVlanList0,
       "hwVlanMappingVlanList1": hwVlanMappingVlanList1,
       "hwVlanMappingVlanList2": hwVlanMappingVlanList2,
       "hwVlanMappingVlanList3": hwVlanMappingVlanList3,
       "hwVlanMappingVlanList4": hwVlanMappingVlanList4,
       "hwVlanMappingVlanList5": hwVlanMappingVlanList5,
       "hwVlanMappingVlanList6": hwVlanMappingVlanList6,
       "hwVlanMappingVlanList7": hwVlanMappingVlanList7,
       "hwGlobalStaMacWhiteListTable": hwGlobalStaMacWhiteListTable,
       "hwGlobalStaMacWhiteListEntry": hwGlobalStaMacWhiteListEntry,
       "hwStaMacWhiteListMacAddr": hwStaMacWhiteListMacAddr,
       "hwGlobalStaMacWhiteListRowStatus": hwGlobalStaMacWhiteListRowStatus,
       "hwStaMacBlackListTable": hwStaMacBlackListTable,
       "hwStaMacBlackListEntry": hwStaMacBlackListEntry,
       "hwStaMacBlackListMacAddr": hwStaMacBlackListMacAddr,
       "hwStaMacBlackListRowStatus": hwStaMacBlackListRowStatus,
       "hwApStaAccessControlTable": hwApStaAccessControlTable,
       "hwApStaAccessControlEntry": hwApStaAccessControlEntry,
       "hwApStaAccessControlApId": hwApStaAccessControlApId,
       "hwApStaAccessControlMode": hwApStaAccessControlMode,
       "hwApStaAccessControlRowStatus": hwApStaAccessControlRowStatus,
       "hwAcStatistics": hwAcStatistics,
       "hwAcReassocSuccessTimes": hwAcReassocSuccessTimes,
       "hwApPerformanceStatTimerLen": hwApPerformanceStatTimerLen,
       "hwRtCollectOnoff": hwRtCollectOnoff,
       "hwApNormalCollectCycle": hwApNormalCollectCycle,
       "hwApRtCollectCycle": hwApRtCollectCycle,
       "hwAcCurAssocStaNum": hwAcCurAssocStaNum,
       "hwAcCurAuthSuccessStaNum": hwAcCurAuthSuccessStaNum,
       "hwAcCurJointApNum": hwAcCurJointApNum,
       "hwAcCurAssoc24gStaNum": hwAcCurAssoc24gStaNum,
       "hwAcCurAssoc5gStaNum": hwAcCurAssoc5gStaNum,
       "hwMacVapManagementTable": hwMacVapManagementTable,
       "hwMacVapManagementEntry": hwMacVapManagementEntry,
       "hwMacWlanServiceVapApMac": hwMacWlanServiceVapApMac,
       "hwMacWlanServiceVapRadioIndex": hwMacWlanServiceVapRadioIndex,
       "hwMacWlanServiceVapEssName": hwMacWlanServiceVapEssName,
       "hwMacWlanServiceVapWlanIndex": hwMacWlanServiceVapWlanIndex,
       "hwMacWlanServiceVapBssid": hwMacWlanServiceVapBssid,
       "hwMacWlanServiceVapRowStatus": hwMacWlanServiceVapRowStatus,
       "hwMacWlanServiceVapSSID": hwMacWlanServiceVapSSID,
       "hwMacWlanServiceVapVlan": hwMacWlanServiceVapVlan,
       "hwMacCapwapConfigManagementTable": hwMacCapwapConfigManagementTable,
       "hwMacCapwapConfigManagementEntry": hwMacCapwapConfigManagementEntry,
       "hwMacWlanServiceCapwapConfigApMac": hwMacWlanServiceCapwapConfigApMac,
       "hwMacWlanServiceCapwapConfigCommit": hwMacWlanServiceCapwapConfigCommit,
       "hwMacVapStationListTable": hwMacVapStationListTable,
       "hwMacVapStationListEntry": hwMacVapStationListEntry,
       "hwMacWlanServiceVapStaApMac": hwMacWlanServiceVapStaApMac,
       "hwMacWlanServiceVapStaRadioId": hwMacWlanServiceVapStaRadioId,
       "hwMacWlanServiceVapStaEssName": hwMacWlanServiceVapStaEssName,
       "hwMacWlanServiceVapStaNum": hwMacWlanServiceVapStaNum,
       "hwMacWlanServiceVapStaMacList": hwMacWlanServiceVapStaMacList,
       "hwMacWlanServiceVapAssociatedStationCount": hwMacWlanServiceVapAssociatedStationCount,
       "hwMacWlanServiceVapCurOnlineStaCount": hwMacWlanServiceVapCurOnlineStaCount,
       "hwMacWlanServiceVapStaAssocAndReAssocReqCount": hwMacWlanServiceVapStaAssocAndReAssocReqCount,
       "hwMacWlanServiceVapStaOnlineTime": hwMacWlanServiceVapStaOnlineTime,
       "hwMacApAssocStatTable": hwMacApAssocStatTable,
       "hwMacApAssocStatEntry": hwMacApAssocStatEntry,
       "hwMacApAssocStatApMac": hwMacApAssocStatApMac,
       "hwMacTotalOnlineTime": hwMacTotalOnlineTime,
       "hwMacTotalAssociatedStationCount": hwMacTotalAssociatedStationCount,
       "hwMacCurrAssociatedStationCount": hwMacCurrAssociatedStationCount,
       "hwMacAssociationRequestCount": hwMacAssociationRequestCount,
       "hwMacAssociationRejectCount": hwMacAssociationRejectCount,
       "hwMacAssociationFailedCount": hwMacAssociationFailedCount,
       "hwMacReAssociationRequestCount": hwMacReAssociationRequestCount,
       "hwMacReAssociationRejectCount": hwMacReAssociationRejectCount,
       "hwMacReAssociationFailedCount": hwMacReAssociationFailedCount,
       "hwMacDisAssocOfUserNotifiedCount": hwMacDisAssocOfUserNotifiedCount,
       "hwMacDisAssocOfStaRoamCount": hwMacDisAssocOfStaRoamCount,
       "hwMacDisAssocOfStaAgeCount": hwMacDisAssocOfStaAgeCount,
       "hwMacDisAssocOfApUnableHandleCount": hwMacDisAssocOfApUnableHandleCount,
       "hwMacDisAssocOfOtherReasonsCount": hwMacDisAssocOfOtherReasonsCount,
       "hwMacAssocRequestCntByResource": hwMacAssocRequestCntByResource,
       "hwMacStaExceptionalOfflineCnt": hwMacStaExceptionalOfflineCnt,
       "hwMacReAssociationSuccessCount": hwMacReAssociationSuccessCount,
       "hwMacBSSNotSupportAssocFailCount": hwMacBSSNotSupportAssocFailCount,
       "hwMacStaAccessRequestCount": hwMacStaAccessRequestCount,
       "hwMacStaAccessRequestFailedCount": hwMacStaAccessRequestFailedCount,
       "hwMacStaAuthenRequestCount": hwMacStaAuthenRequestCount,
       "hwMacStaAuthenRequestFailedCount": hwMacStaAuthenRequestFailedCount,
       "hwMacRefusedStaNumByResource": hwMacRefusedStaNumByResource,
       "hwMacStaAssocAndReAssocRequestCount": hwMacStaAssocAndReAssocRequestCount,
       "hwMacStaAuthenRequestSuccessCount": hwMacStaAuthenRequestSuccessCount,
       "hwMacL3RoamInStationCount": hwMacL3RoamInStationCount,
       "hwMacL3RoamOutStationCount": hwMacL3RoamOutStationCount,
       "hwVapConfigTable": hwVapConfigTable,
       "hwVapConfigEntry": hwVapConfigEntry,
       "hwVapOptValue": hwVapOptValue,
       "hwSsidStatisticTable": hwSsidStatisticTable,
       "hwSsidStatisticEntry": hwSsidStatisticEntry,
       "hwSsidStatisticApIndex": hwSsidStatisticApIndex,
       "hwSsidStatisticRadioIndex": hwSsidStatisticRadioIndex,
       "hwSsidStatisticEssSsid": hwSsidStatisticEssSsid,
       "hwSsidAirportRecvBytes": hwSsidAirportRecvBytes,
       "hwSsidAirportRecvErrorFrames": hwSsidAirportRecvErrorFrames,
       "hwSsidAirportRecvFrames": hwSsidAirportRecvFrames,
       "hwSsidAirportRecvUnicastFrames": hwSsidAirportRecvUnicastFrames,
       "hwSsidAirportRecvDropFrames": hwSsidAirportRecvDropFrames,
       "hwSsidAirportTransmitBytes": hwSsidAirportTransmitBytes,
       "hwSsidAirportTransmitErrorFrames": hwSsidAirportTransmitErrorFrames,
       "hwSsidAirportTransmitFrames": hwSsidAirportTransmitFrames,
       "hwSsidAirportTransmitUnicastFrames": hwSsidAirportTransmitUnicastFrames,
       "hwSsidAirportTransmitDropFrames": hwSsidAirportTransmitDropFrames,
       "hwSsidAirportDownReTransmitFrames": hwSsidAirportDownReTransmitFrames,
       "hwSsidCurrentStaNum": hwSsidCurrentStaNum,
       "hwSsidAirportNoise": hwSsidAirportNoise,
       "hwSsidAirportSNR": hwSsidAirportSNR,
       "hwMacSsidStatisticTable": hwMacSsidStatisticTable,
       "hwMacSsidStatisticEntry": hwMacSsidStatisticEntry,
       "hwMacSsidStatisticApMac": hwMacSsidStatisticApMac,
       "hwMacSsidStatisticRadioIndex": hwMacSsidStatisticRadioIndex,
       "hwMacSsidStatisticEssSsid": hwMacSsidStatisticEssSsid,
       "hwMacSsidAirportRecvBytes": hwMacSsidAirportRecvBytes,
       "hwMacSsidAirportRecvErrorFrames": hwMacSsidAirportRecvErrorFrames,
       "hwMacSsidAirportRecvFrames": hwMacSsidAirportRecvFrames,
       "hwMacSsidAirportRecvUnicastFrames": hwMacSsidAirportRecvUnicastFrames,
       "hwMacSsidAirportRecvDropFrames": hwMacSsidAirportRecvDropFrames,
       "hwMacSsidAirportTransmitBytes": hwMacSsidAirportTransmitBytes,
       "hwMacSsidAirportTransmitErrorFrames": hwMacSsidAirportTransmitErrorFrames,
       "hwMacSsidAirportTransmitFrames": hwMacSsidAirportTransmitFrames,
       "hwMacSsidAirportTransmitUnicastFrames": hwMacSsidAirportTransmitUnicastFrames,
       "hwMacSsidAirportTransmitDropFrames": hwMacSsidAirportTransmitDropFrames,
       "hwMacSsidAirportDownReTransmitFrames": hwMacSsidAirportDownReTransmitFrames,
       "hwMacSsidCurrentStaNum": hwMacSsidCurrentStaNum,
       "hwMacSsidAirportNoise": hwMacSsidAirportNoise,
       "hwMacSsidAirportSNR": hwMacSsidAirportSNR,
       "hwMacApStaAccessControlTable": hwMacApStaAccessControlTable,
       "hwMacApStaAccessControlEntry": hwMacApStaAccessControlEntry,
       "hwMacApStaAccessControlApMac": hwMacApStaAccessControlApMac,
       "hwMacApStaAccessControlMode": hwMacApStaAccessControlMode,
       "hwMacApStaAccessControlRowStatus": hwMacApStaAccessControlRowStatus,
       "hwApStaInfoTable": hwApStaInfoTable,
       "hwApStaInfoEntry": hwApStaInfoEntry,
       "hwStaMAC": hwStaMAC,
       "hwStaIPAddress": hwStaIPAddress,
       "hwStaWMMAttr": hwStaWMMAttr,
       "hwStaRadioMode": hwStaRadioMode,
       "hwStaRadioChannel": hwStaRadioChannel,
       "hwAPTxRates": hwAPTxRates,
       "hwStaPowerSaveMode": hwStaPowerSaveMode,
       "hwStaVlanId": hwStaVlanId,
       "hwStaSSIDName": hwStaSSIDName,
       "hwApStaTxPacket": hwApStaTxPacket,
       "hwApStaRxPacket": hwApStaRxPacket,
       "hwApStaStatus": hwApStaStatus,
       "hwApStaBssid": hwApStaBssid,
       "hwApStaRssi": hwApStaRssi,
       "hwApStaSnr": hwApStaSnr,
       "hwMacApStaInfoTable": hwMacApStaInfoTable,
       "hwMacApStaInfoEntry": hwMacApStaInfoEntry,
       "hwMacStaMAC": hwMacStaMAC,
       "hwMacStaIPAddress": hwMacStaIPAddress,
       "hwMacStaWMMAttr": hwMacStaWMMAttr,
       "hwMacStaRadioMode": hwMacStaRadioMode,
       "hwMacStaRadioChannel": hwMacStaRadioChannel,
       "hwMacAPTxRates": hwMacAPTxRates,
       "hwMacStaPowerSaveMode": hwMacStaPowerSaveMode,
       "hwMacStaVlanId": hwMacStaVlanId,
       "hwMacStaSSIDName": hwMacStaSSIDName,
       "hwMacApStaTxPacket": hwMacApStaTxPacket,
       "hwMacApStaRxPacket": hwMacApStaRxPacket,
       "hwMacApStaStatus": hwMacApStaStatus,
       "hwMacApStaBssid": hwMacApStaBssid,
       "hwMacApStaRssi": hwMacApStaRssi,
       "hwMacApStaSnr": hwMacApStaSnr,
       "hwInterACRoamingInfo": hwInterACRoamingInfo,
       "hwInterACRoamingInSuccCnt": hwInterACRoamingInSuccCnt,
       "hwInterACRoamingOutSuccCnt": hwInterACRoamingOutSuccCnt,
       "hwRadioStaListTable": hwRadioStaListTable,
       "hwRadioStaListEntry": hwRadioStaListEntry,
       "hwRadioStaApId": hwRadioStaApId,
       "hwRadioStaRadioId": hwRadioStaRadioId,
       "hwRadioStaNumber": hwRadioStaNumber,
       "hwRadioStaMacList": hwRadioStaMacList,
       "hwRadioStaTotalAssociatedCount": hwRadioStaTotalAssociatedCount,
       "hwRadioStaAccessReqCount": hwRadioStaAccessReqCount,
       "hwMacRadioStaListTable": hwMacRadioStaListTable,
       "hwMacRadioStaListEntry": hwMacRadioStaListEntry,
       "hwMacRadioStaApMac": hwMacRadioStaApMac,
       "hwMacRadioStaRadioId": hwMacRadioStaRadioId,
       "hwMacRadioStaNumber": hwMacRadioStaNumber,
       "hwMacRadioStaMacList": hwMacRadioStaMacList,
       "hwMacRadioStaTotalAssociatedCount": hwMacRadioStaTotalAssociatedCount,
       "hwMacRadioStaAccessReqCount": hwMacRadioStaAccessReqCount,
       "hwBridgeProfileTable": hwBridgeProfileTable,
       "hwBridgeProfileEntry": hwBridgeProfileEntry,
       "hwBridgeProfileName": hwBridgeProfileName,
       "hwBridgeProfileBridgeName": hwBridgeProfileBridgeName,
       "hwBridgeProfileSecurityProfileName": hwBridgeProfileSecurityProfileName,
       "hwBridgeProfileVlanTagged": hwBridgeProfileVlanTagged,
       "hwBridgeProfileRowStatus": hwBridgeProfileRowStatus,
       "hwBridgeProfileDhcpTrustPort": hwBridgeProfileDhcpTrustPort,
       "hwBridgeProfileNdTrustPort": hwBridgeProfileNdTrustPort,
       "hwBridgeVapManagementTable": hwBridgeVapManagementTable,
       "hwBridgeVapManagementEntry": hwBridgeVapManagementEntry,
       "hwBridgeVapApIndex": hwBridgeVapApIndex,
       "hwBridgeVapRadioIndex": hwBridgeVapRadioIndex,
       "hwBridgeVapBridgeProfileName": hwBridgeVapBridgeProfileName,
       "hwBridgeVapRowStatus": hwBridgeVapRowStatus,
       "hwBridgeVapBssid": hwBridgeVapBssid,
       "hwMacBridgeVapManagementTable": hwMacBridgeVapManagementTable,
       "hwMacBridgeVapManagementEntry": hwMacBridgeVapManagementEntry,
       "hwMacBridgeVapApMac": hwMacBridgeVapApMac,
       "hwMacBridgeVapRadioIndex": hwMacBridgeVapRadioIndex,
       "hwMacBridgeVapBridgeProfileName": hwMacBridgeVapBridgeProfileName,
       "hwMacBridgeVapRowStatus": hwMacBridgeVapRowStatus,
       "hwMacBridgeVapBssid": hwMacBridgeVapBssid,
       "hwBridgeLinkTable": hwBridgeLinkTable,
       "hwBridgeLinkEntry": hwBridgeLinkEntry,
       "hwBridgeLinkIndex": hwBridgeLinkIndex,
       "hwBridgeLinkWlanID": hwBridgeLinkWlanID,
       "hwBridgeLinkBridgeType": hwBridgeLinkBridgeType,
       "hwBridgeLinkBridgeSubType": hwBridgeLinkBridgeSubType,
       "hwBridgeLinkPeerMac": hwBridgeLinkPeerMac,
       "hwBridgeLinkBridgeProfileName": hwBridgeLinkBridgeProfileName,
       "hwBridgeLinkStpMode": hwBridgeLinkStpMode,
       "hwBridgeLinkInstanceIdList": hwBridgeLinkInstanceIdList,
       "hwBridgeLinkInstanceStateList": hwBridgeLinkInstanceStateList,
       "hwBridgeLinkApMac": hwBridgeLinkApMac,
       "hwBridgeLinkBridgeMode": hwBridgeLinkBridgeMode,
       "hwBridgeLinkCoverageDistance": hwBridgeLinkCoverageDistance,
       "hwBridgeLinkPeerAPID": hwBridgeLinkPeerAPID,
       "hwBridgeLinkPeerAPStatus": hwBridgeLinkPeerAPStatus,
       "hwBridgeLinkMaxRssi": hwBridgeLinkMaxRssi,
       "hwBridgeLinkRssi": hwBridgeLinkRssi,
       "hwBridgeLinkPeerApMac": hwBridgeLinkPeerApMac,
       "hwBridgeLinkChannelID": hwBridgeLinkChannelID,
       "hwMacBridgeLinkTable": hwMacBridgeLinkTable,
       "hwMacBridgeLinkEntry": hwMacBridgeLinkEntry,
       "hwMacBridgeLinkIndex": hwMacBridgeLinkIndex,
       "hwMacBridgeLinkWlanID": hwMacBridgeLinkWlanID,
       "hwMacBridgeLinkBridgeType": hwMacBridgeLinkBridgeType,
       "hwMacBridgeLinkBridgeSubType": hwMacBridgeLinkBridgeSubType,
       "hwMacBridgeLinkPeerMac": hwMacBridgeLinkPeerMac,
       "hwMacBridgeLinkBridgeProfileName": hwMacBridgeLinkBridgeProfileName,
       "hwMacBridgeLinkStpMode": hwMacBridgeLinkStpMode,
       "hwMacBridgeLinkInstanceIdList": hwMacBridgeLinkInstanceIdList,
       "hwMacBridgeLinkInstanceStateList": hwMacBridgeLinkInstanceStateList,
       "hwMacBridgeLinkApID": hwMacBridgeLinkApID,
       "hwMacBridgeLinkBridgeMode": hwMacBridgeLinkBridgeMode,
       "hwMacBridgeLinkCoverageDistance": hwMacBridgeLinkCoverageDistance,
       "hwMacBridgeLinkPeerAPID": hwMacBridgeLinkPeerAPID,
       "hwMacBridgeLinkPeerAPStatus": hwMacBridgeLinkPeerAPStatus,
       "hwMacBridgeLinkMaxRssi": hwMacBridgeLinkMaxRssi,
       "hwMacBridgeLinkRssi": hwMacBridgeLinkRssi,
       "hwMacBridgeLinkPeerApMac": hwMacBridgeLinkPeerApMac,
       "hwMacBridgeChannelID": hwMacBridgeChannelID,
       "hwBridgeWhitelistTable": hwBridgeWhitelistTable,
       "hwBridgeWhitelistEntry": hwBridgeWhitelistEntry,
       "hwBridgeWhitelistName": hwBridgeWhitelistName,
       "hwBridgeWhitelistPeerList": hwBridgeWhitelistPeerList,
       "hwBridgeWhitelistRowStatus": hwBridgeWhitelistRowStatus,
       "hwWirelessSsidStatisticTable": hwWirelessSsidStatisticTable,
       "hwWirelessSsidStatisticEntry": hwWirelessSsidStatisticEntry,
       "hwWirelessSsidStatisticEssSsid": hwWirelessSsidStatisticEssSsid,
       "hwWirelessSsidAirportTransmitUnicastFrames": hwWirelessSsidAirportTransmitUnicastFrames,
       "hwWirelessSsidAirportTransmitFrames": hwWirelessSsidAirportTransmitFrames,
       "hwWirelessSsidAirportTransmitErrorFrames": hwWirelessSsidAirportTransmitErrorFrames,
       "hwWirelessSsidAirportDownReTransmitFrames": hwWirelessSsidAirportDownReTransmitFrames,
       "hwWirelessSsidAirportTransmitDropFrames": hwWirelessSsidAirportTransmitDropFrames,
       "hwWirelessSsidAirportTransmitBytes": hwWirelessSsidAirportTransmitBytes,
       "hwWirelessSsidAirportRecvUnicastFrames": hwWirelessSsidAirportRecvUnicastFrames,
       "hwWirelessSsidAirportRecvFrames": hwWirelessSsidAirportRecvFrames,
       "hwWirelessSsidAirportRecvErrorFrames": hwWirelessSsidAirportRecvErrorFrames,
       "hwWirelessSsidAirportRecvDropFrames": hwWirelessSsidAirportRecvDropFrames,
       "hwWirelessSsidAirportRecvBytes": hwWirelessSsidAirportRecvBytes,
       "hwWirelessSsidTotalAssociatedSuccessStationCount": hwWirelessSsidTotalAssociatedSuccessStationCount,
       "hwWirelessSsidCurAssocStationCount": hwWirelessSsidCurAssocStationCount,
       "hwWirelessSsidTotalAssociatedFailedStationCount": hwWirelessSsidTotalAssociatedFailedStationCount,
       "hwStaBlacklistProfileTable": hwStaBlacklistProfileTable,
       "hwStaBlacklistProfileEntry": hwStaBlacklistProfileEntry,
       "hwStaBlacklistProfileName": hwStaBlacklistProfileName,
       "hwStaBlacklistProfileStaMac": hwStaBlacklistProfileStaMac,
       "hwStaBlacklistProfileOper": hwStaBlacklistProfileOper,
       "hwStaBlacklistProfileStaNum": hwStaBlacklistProfileStaNum,
       "hwStaBlacklistProfileStaList": hwStaBlacklistProfileStaList,
       "hwStaBlacklistProfileRowStatus": hwStaBlacklistProfileRowStatus,
       "hwStaWhitelistProfileTable": hwStaWhitelistProfileTable,
       "hwStaWhitelistProfileEntry": hwStaWhitelistProfileEntry,
       "hwStaWhitelistProfileName": hwStaWhitelistProfileName,
       "hwStaWhitelistProfileStaMac": hwStaWhitelistProfileStaMac,
       "hwStaWhitelistProfileOper": hwStaWhitelistProfileOper,
       "hwStaWhitelistProfileStaNum": hwStaWhitelistProfileStaNum,
       "hwStaWhitelistProfileStaList": hwStaWhitelistProfileStaList,
       "hwStaWhitelistProfileRowStatus": hwStaWhitelistProfileRowStatus,
       "hwMeshProfileTable": hwMeshProfileTable,
       "hwMeshProfileEntry": hwMeshProfileEntry,
       "hwMeshProfileName": hwMeshProfileName,
       "hwMeshProfileSecurityProfileName": hwMeshProfileSecurityProfileName,
       "hwMeshProfileMeshID": hwMeshProfileMeshID,
       "hwMeshProfileMaxLinkNum": hwMeshProfileMaxLinkNum,
       "hwMeshProfileRssiThreshold": hwMeshProfileRssiThreshold,
       "hwMeshProfileReportInterval": hwMeshProfileReportInterval,
       "hwMeshProfileRowStatus": hwMeshProfileRowStatus,
       "hwMeshProfileDhcpTrustPort": hwMeshProfileDhcpTrustPort,
       "hwMeshProfileNdTrustPort": hwMeshProfileNdTrustPort,
       "hwMeshProfileQuickHoSwitch": hwMeshProfileQuickHoSwitch,
       "hwMeshProfileLinkHoThreshold": hwMeshProfileLinkHoThreshold,
       "hwMeshProfileLinkHoldPeriod": hwMeshProfileLinkHoldPeriod,
       "hwMeshProfileLinkLinkSaturationThreshold": hwMeshProfileLinkLinkSaturationThreshold,
       "hwMeshProfileLinkProbePeriod": hwMeshProfileLinkProbePeriod,
       "hwMeshProfileFwaMode": hwMeshProfileFwaMode,
       "hwMeshProfileFwaEdcaMode": hwMeshProfileFwaEdcaMode,
       "hwMeshProfileQuickHandoverMinRssiThreshold": hwMeshProfileQuickHandoverMinRssiThreshold,
       "hwMeshProfileLocationBasedHandoverAlgorithmSwitch": hwMeshProfileLocationBasedHandoverAlgorithmSwitch,
       "hwMeshProfileMovingDirection": hwMeshProfileMovingDirection,
       "hwMeshProfileHandoverAlgorithmPNCriteriaObserveTime": hwMeshProfileHandoverAlgorithmPNCriteriaObserveTime,
       "hwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime": hwMeshProfileHandoverAlgorithmPNCriteriaQualifyTime,
       "hwMeshProfileUrgentHandoverLowRateThreshold": hwMeshProfileUrgentHandoverLowRateThreshold,
       "hwMeshProfileUrgentHandoverLowRatePeriod": hwMeshProfileUrgentHandoverLowRatePeriod,
       "hwMeshProfileUrgentHandoverPunishmentPeriod": hwMeshProfileUrgentHandoverPunishmentPeriod,
       "hwMeshProfileUrgentHandoverPunishmentRssi": hwMeshProfileUrgentHandoverPunishmentRssi,
       "hwMeshVapManagementTable": hwMeshVapManagementTable,
       "hwMeshVapManagementEntry": hwMeshVapManagementEntry,
       "hwMeshVapApIndex": hwMeshVapApIndex,
       "hwMeshVapRadioIndex": hwMeshVapRadioIndex,
       "hwMeshVapMeshProfileName": hwMeshVapMeshProfileName,
       "hwMeshVapRowStatus": hwMeshVapRowStatus,
       "hwMeshVapBssid": hwMeshVapBssid,
       "hwMacMeshVapManagementTable": hwMacMeshVapManagementTable,
       "hwMacMeshVapManagementEntry": hwMacMeshVapManagementEntry,
       "hwMacMeshVapApMac": hwMacMeshVapApMac,
       "hwMacMeshVapRadioIndex": hwMacMeshVapRadioIndex,
       "hwMacMeshVapMeshProfileName": hwMacMeshVapMeshProfileName,
       "hwMacMeshVapRowStatus": hwMacMeshVapRowStatus,
       "hwMacMeshVapBssid": hwMacMeshVapBssid,
       "hwMeshLinkTable": hwMeshLinkTable,
       "hwMeshLinkEntry": hwMeshLinkEntry,
       "hwMeshLinkIndex": hwMeshLinkIndex,
       "hwMeshLinkWlanID": hwMeshLinkWlanID,
       "hwMeshLinkPeerMac": hwMeshLinkPeerMac,
       "hwMeshLinkChannelID": hwMeshLinkChannelID,
       "hwMeshLinkRssiValue": hwMeshLinkRssiValue,
       "hwMeshLinkApMac": hwMeshLinkApMac,
       "hwMeshLinkMeshRole": hwMeshLinkMeshRole,
       "hwMeshLinkCoverageDistance": hwMeshLinkCoverageDistance,
       "hwMeshLinkPeerAPID": hwMeshLinkPeerAPID,
       "hwMeshLinkPeerAPStatus": hwMeshLinkPeerAPStatus,
       "hwMeshLinkMaxRssi": hwMeshLinkMaxRssi,
       "hwMeshLinkPeerApMac": hwMeshLinkPeerApMac,
       "hwMacMeshLinkTable": hwMacMeshLinkTable,
       "hwMacMeshLinkEntry": hwMacMeshLinkEntry,
       "hwMacMeshLinkIndex": hwMacMeshLinkIndex,
       "hwMacMeshLinkWlanID": hwMacMeshLinkWlanID,
       "hwMacMeshLinkPeerMac": hwMacMeshLinkPeerMac,
       "hwMacMeshLinkChannelID": hwMacMeshLinkChannelID,
       "hwMacMeshLinkRssiValue": hwMacMeshLinkRssiValue,
       "hwMacMeshLinkApID": hwMacMeshLinkApID,
       "hwMacMeshLinkMeshRole": hwMacMeshLinkMeshRole,
       "hwMacMeshLinkCoverageDistance": hwMacMeshLinkCoverageDistance,
       "hwMacMeshLinkPeerAPID": hwMacMeshLinkPeerAPID,
       "hwMacMeshLinkPeerAPStatus": hwMacMeshLinkPeerAPStatus,
       "hwMacMeshLinkMaxRssi": hwMacMeshLinkMaxRssi,
       "hwMacMeshLinkPeerApMac": hwMacMeshLinkPeerApMac,
       "hwMeshWhitelistTable": hwMeshWhitelistTable,
       "hwMeshWhitelistEntry": hwMeshWhitelistEntry,
       "hwMeshWhitelistName": hwMeshWhitelistName,
       "hwMeshWhitelistPeerList": hwMeshWhitelistPeerList,
       "hwMeshWhitelistRowStatus": hwMeshWhitelistRowStatus,
       "hwWlanServiceManagementObject": hwWlanServiceManagementObject,
       "hwLbsTagDevTable": hwLbsTagDevTable,
       "hwLbsTagDevEntry": hwLbsTagDevEntry,
       "hwLbsTagDevApID": hwLbsTagDevApID,
       "hwLbsTagDevMac": hwLbsTagDevMac,
       "hwLbsTagDevType": hwLbsTagDevType,
       "hwLbsTagDevChannel": hwLbsTagDevChannel,
       "hwLbsTagDevRssi": hwLbsTagDevRssi,
       "hwProxyTrackSideEquipTable": hwProxyTrackSideEquipTable,
       "hwProxyTrackSideEquipEntry": hwProxyTrackSideEquipEntry,
       "hwProxyTrackSideEquipIndex": hwProxyTrackSideEquipIndex,
       "hwProxyTrackSideEquipMac": hwProxyTrackSideEquipMac,
       "hwProxyTrackSideEquipVlanID": hwProxyTrackSideEquipVlanID,
       "hwProxyTrackSideEquipRowStatus": hwProxyTrackSideEquipRowStatus,
       "hwProxyOnBoardEquipTable": hwProxyOnBoardEquipTable,
       "hwProxyOnBoardEquipEntry": hwProxyOnBoardEquipEntry,
       "hwProxyOnBoardEquipIndex": hwProxyOnBoardEquipIndex,
       "hwProxyOnBoardEquipMac": hwProxyOnBoardEquipMac,
       "hwProxyOnBoardEquipVlanID": hwProxyOnBoardEquipVlanID,
       "hwProxyOnBoardEquipRowStatus": hwProxyOnBoardEquipRowStatus,
       "hwHandoverTraceTable": hwHandoverTraceTable,
       "hwHandoverTraceEntry": hwHandoverTraceEntry,
       "hwHandoverTraceIndex": hwHandoverTraceIndex,
       "hwHandoverTimeStamp": hwHandoverTimeStamp,
       "hwHandoverFromApMac": hwHandoverFromApMac,
       "hwHandoverFromApRssi": hwHandoverFromApRssi,
       "hwHandoverToApMac": hwHandoverToApMac,
       "hwHandoverToApRssi": hwHandoverToApRssi,
       "hwHandoverFromApLocationID": hwHandoverFromApLocationID,
       "hwHandoverToApLocationID": hwHandoverToApLocationID,
       "hwNeighborApTable": hwNeighborApTable,
       "hwNeighborApEntry": hwNeighborApEntry,
       "hwNeighborApLocalApId": hwNeighborApLocalApId,
       "hwNeighborApLocalRadioId": hwNeighborApLocalRadioId,
       "hwNeighborApLocalApMac": hwNeighborApLocalApMac,
       "hwNeighborApIdList": hwNeighborApIdList,
       "hwNeighborApMacList": hwNeighborApMacList,
       "hwNeighborApRssiList": hwNeighborApRssiList,
       "hwNeighborApUpdateTime": hwNeighborApUpdateTime,
       "hwNeighborApLocalLocationID": hwNeighborApLocalLocationID,
       "hwNeighborApLocationIDList": hwNeighborApLocationIDList,
       "hwStaOnlineFailTable": hwStaOnlineFailTable,
       "hwStaOnlineFailEntry": hwStaOnlineFailEntry,
       "hwStaOnlineFailMacAddress": hwStaOnlineFailMacAddress,
       "hwStaOnlineFailReasonIndex": hwStaOnlineFailReasonIndex,
       "hwStaOnlineFailApId": hwStaOnlineFailApId,
       "hwStaOnlineFailRadioId": hwStaOnlineFailRadioId,
       "hwStaOnlineFailWlanId": hwStaOnlineFailWlanId,
       "hwStaOnlineFailLastFailTime": hwStaOnlineFailLastFailTime,
       "hwStaOnlineFailReason": hwStaOnlineFailReason,
       "hwStaOnlineFailRowStatus": hwStaOnlineFailRowStatus,
       "hwStaOnlineFailTableInfo": hwStaOnlineFailTableInfo,
       "hwStaResetAllOnlineFailTableReason": hwStaResetAllOnlineFailTableReason,
       "hwWlanServiceManagementConformance": hwWlanServiceManagementConformance,
       "hwWlanServiceManagementCompliances": hwWlanServiceManagementCompliances,
       "hwWlanServiceManagementCompliance": hwWlanServiceManagementCompliance,
       "hwWlanServiceManagementObjectGroups": hwWlanServiceManagementObjectGroups,
       "hwEssManagementGroup": hwEssManagementGroup,
       "hwVapManagementGroup": hwVapManagementGroup,
       "hwServiceBatchGroup": hwServiceBatchGroup,
       "hwCapwapConfigManagementGroup": hwCapwapConfigManagementGroup,
       "hwStationGroup": hwStationGroup,
       "hwVapStationListGroup": hwVapStationListGroup,
       "hwWlanServiceBatchEssInfoGroup": hwWlanServiceBatchEssInfoGroup,
       "hwApAssocStatGroup": hwApAssocStatGroup,
       "hwVlanMappingGroup": hwVlanMappingGroup,
       "hwGlobalStaMacWhiteListGroup": hwGlobalStaMacWhiteListGroup,
       "hwStaMacBlackListGroup": hwStaMacBlackListGroup,
       "hwApStaAccessControlGroup": hwApStaAccessControlGroup,
       "hwAcStatisticsGroup": hwAcStatisticsGroup,
       "hwMacVapManagementGroup": hwMacVapManagementGroup,
       "hwMacCapwapConfigManagementGroup": hwMacCapwapConfigManagementGroup,
       "hwMacVapStationListGroup": hwMacVapStationListGroup,
       "hwMacApAssocStatGroup": hwMacApAssocStatGroup,
       "hwVapConfigGroup": hwVapConfigGroup,
       "hwSsidStatisticGroup": hwSsidStatisticGroup,
       "hwMacSsidStatisticGroup": hwMacSsidStatisticGroup,
       "hwMacApStaAccessControlGroup": hwMacApStaAccessControlGroup,
       "hwApStaInfoGroup": hwApStaInfoGroup,
       "hwMacApStaInfoGroup": hwMacApStaInfoGroup,
       "hwInterACRoamingInfoGroup": hwInterACRoamingInfoGroup,
       "hwRadioStaListGroup": hwRadioStaListGroup,
       "hwMacRadioStaListGroup": hwMacRadioStaListGroup,
       "hwBridgeProfileGroup": hwBridgeProfileGroup,
       "hwBridgeVapManagementGroup": hwBridgeVapManagementGroup,
       "hwMacBridgeVapManagementGroup": hwMacBridgeVapManagementGroup,
       "hwBridgeLinkGroup": hwBridgeLinkGroup,
       "hwMacBridgeLinkGroup": hwMacBridgeLinkGroup,
       "hwBridgeWhitelistGroup": hwBridgeWhitelistGroup,
       "hwWirelessSsidStatisticGroup": hwWirelessSsidStatisticGroup,
       "hwStaBlacklistProfileGroup": hwStaBlacklistProfileGroup,
       "hwStaWhitelistProfileGroup": hwStaWhitelistProfileGroup,
       "hwMeshProfileGroup": hwMeshProfileGroup,
       "hwMeshVapManagementGroup": hwMeshVapManagementGroup,
       "hwMacMeshVapManagementGroup": hwMacMeshVapManagementGroup,
       "hwMeshLinkGroup": hwMeshLinkGroup,
       "hwMacMeshLinkGroup": hwMacMeshLinkGroup,
       "hwMeshWhitelistGroup": hwMeshWhitelistGroup,
       "hwWlanServiceManagementGroup": hwWlanServiceManagementGroup,
       "hwLbsTagDevGroup": hwLbsTagDevGroup,
       "hwProxyTrackSideEquipGroup": hwProxyTrackSideEquipGroup,
       "hwProxyOnBoardEquipGroup": hwProxyOnBoardEquipGroup,
       "hwHandoverTraceGroup": hwHandoverTraceGroup,
       "hwNeighborApGroup": hwNeighborApGroup}
)
