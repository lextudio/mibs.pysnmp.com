# SNMP MIB module (HP-SWITCH-BASIC-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SWITCH-BASIC-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:01 2024
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

(hpSwitchConfig,
 hpSwitchFilterConfig,
 hpSwitchIgmpConfig) = mibBuilder.importSymbols(
    "CONFIG-MIB",
    "hpSwitchConfig",
    "hpSwitchFilterConfig",
    "hpSwitchIgmpConfig")

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(portCopyEntry,) = mibBuilder.importSymbols(
    "SMON-MIB",
    "portCopyEntry")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpSwitchBasicConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29)
)
hpSwitchBasicConfigMIB.setRevisions(
        ("2015-10-11 00:00",
         "2015-04-20 00:00",
         "2014-12-11 00:00",
         "2014-03-25 00:00",
         "2013-07-22 00:00",
         "2013-05-22 00:00",
         "2013-02-16 00:00",
         "2012-02-03 00:00",
         "2011-09-08 00:00",
         "2011-06-15 21:07",
         "2010-08-05 00:00",
         "2010-06-28 00:00",
         "2010-04-14 00:00",
         "2010-02-17 00:00",
         "2009-09-10 00:00",
         "2009-08-18 00:00",
         "2009-07-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfBridgeFilterConfigTable_Object = MibTable
hpicfBridgeFilterConfigTable = _HpicfBridgeFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 2)
)
if mibBuilder.loadTexts:
    hpicfBridgeFilterConfigTable.setStatus("current")
_HpicfBridgeFilterConfigEntry_Object = MibTableRow
hpicfBridgeFilterConfigEntry = _HpicfBridgeFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 2, 1)
)
hpicfBridgeFilterConfigEntry.setIndexNames(
    (0, "HP-SWITCH-BASIC-CONFIG-MIB", "hpicfBridgeFilterName"),
)
if mibBuilder.loadTexts:
    hpicfBridgeFilterConfigEntry.setStatus("current")


class _HpicfBridgeFilterName_Type(DisplayString):
    """Custom type hpicfBridgeFilterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HpicfBridgeFilterName_Type.__name__ = "DisplayString"
_HpicfBridgeFilterName_Object = MibTableColumn
hpicfBridgeFilterName = _HpicfBridgeFilterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 2, 1, 1),
    _HpicfBridgeFilterName_Type()
)
hpicfBridgeFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfBridgeFilterName.setStatus("current")
_HpicfBridgeFilterDropPortMask_Type = PortList
_HpicfBridgeFilterDropPortMask_Object = MibTableColumn
hpicfBridgeFilterDropPortMask = _HpicfBridgeFilterDropPortMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 2, 1, 2),
    _HpicfBridgeFilterDropPortMask_Type()
)
hpicfBridgeFilterDropPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBridgeFilterDropPortMask.setStatus("current")
_HpicfBridgeFilterEntryStatus_Type = RowStatus
_HpicfBridgeFilterEntryStatus_Object = MibTableColumn
hpicfBridgeFilterEntryStatus = _HpicfBridgeFilterEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 8, 2, 1, 3),
    _HpicfBridgeFilterEntryStatus_Type()
)
hpicfBridgeFilterEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBridgeFilterEntryStatus.setStatus("current")
_HpSwitchIgmpProxyDomainConfigTable_Object = MibTable
hpSwitchIgmpProxyDomainConfigTable = _HpSwitchIgmpProxyDomainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5)
)
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainConfigTable.setStatus("current")
_HpSwitchIgmpProxyDomainConfigEntry_Object = MibTableRow
hpSwitchIgmpProxyDomainConfigEntry = _HpSwitchIgmpProxyDomainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5, 1)
)
hpSwitchIgmpProxyDomainConfigEntry.setIndexNames(
    (0, "HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchIgmpProxyDomainId"),
)
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainConfigEntry.setStatus("current")


class _HpSwitchIgmpProxyDomainId_Type(Integer32):
    """Custom type hpSwitchIgmpProxyDomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchIgmpProxyDomainId_Type.__name__ = "Integer32"
_HpSwitchIgmpProxyDomainId_Object = MibTableColumn
hpSwitchIgmpProxyDomainId = _HpSwitchIgmpProxyDomainId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5, 1, 1),
    _HpSwitchIgmpProxyDomainId_Type()
)
hpSwitchIgmpProxyDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainId.setStatus("current")
_HpSwitchIgmpProxyDomainStatus_Type = RowStatus
_HpSwitchIgmpProxyDomainStatus_Object = MibTableColumn
hpSwitchIgmpProxyDomainStatus = _HpSwitchIgmpProxyDomainStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5, 1, 2),
    _HpSwitchIgmpProxyDomainStatus_Type()
)
hpSwitchIgmpProxyDomainStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainStatus.setStatus("current")
_HpSwitchIgmpProxyDomainName_Type = DisplayString
_HpSwitchIgmpProxyDomainName_Object = MibTableColumn
hpSwitchIgmpProxyDomainName = _HpSwitchIgmpProxyDomainName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5, 1, 3),
    _HpSwitchIgmpProxyDomainName_Type()
)
hpSwitchIgmpProxyDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainName.setStatus("current")
_HpSwitchIgmpProxyDomainIp_Type = IpAddress
_HpSwitchIgmpProxyDomainIp_Object = MibTableColumn
hpSwitchIgmpProxyDomainIp = _HpSwitchIgmpProxyDomainIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5, 1, 4),
    _HpSwitchIgmpProxyDomainIp_Type()
)
hpSwitchIgmpProxyDomainIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainIp.setStatus("current")
_HpSwitchIgmpProxyMcastLowerIp_Type = IpAddress
_HpSwitchIgmpProxyMcastLowerIp_Object = MibTableColumn
hpSwitchIgmpProxyMcastLowerIp = _HpSwitchIgmpProxyMcastLowerIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5, 1, 5),
    _HpSwitchIgmpProxyMcastLowerIp_Type()
)
hpSwitchIgmpProxyMcastLowerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyMcastLowerIp.setStatus("current")
_HpSwitchIgmpProxyMcastUpperIp_Type = IpAddress
_HpSwitchIgmpProxyMcastUpperIp_Object = MibTableColumn
hpSwitchIgmpProxyMcastUpperIp = _HpSwitchIgmpProxyMcastUpperIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 15, 5, 1, 6),
    _HpSwitchIgmpProxyMcastUpperIp_Type()
)
hpSwitchIgmpProxyMcastUpperIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyMcastUpperIp.setStatus("current")
_HpSwitchBasicConfigObjects_ObjectIdentity = ObjectIdentity
hpSwitchBasicConfigObjects = _HpSwitchBasicConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1)
)
_HpSwitchNotificationObjects_ObjectIdentity = ObjectIdentity
hpSwitchNotificationObjects = _HpSwitchNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0)
)


class _HpSwitchStartupConfigSource_Type(Integer32):
    """Custom type hpSwitchStartupConfigSource based on Integer32"""
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
        *(("unknown", 0),
          ("viaCli", 1),
          ("viaSnmp", 2),
          ("viaWebUI", 3))
    )


_HpSwitchStartupConfigSource_Type.__name__ = "Integer32"
_HpSwitchStartupConfigSource_Object = MibScalar
hpSwitchStartupConfigSource = _HpSwitchStartupConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0, 1),
    _HpSwitchStartupConfigSource_Type()
)
hpSwitchStartupConfigSource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpSwitchStartupConfigSource.setStatus("current")
_HpSwitchStartupConfigSourceIPAddrType_Type = InetAddressType
_HpSwitchStartupConfigSourceIPAddrType_Object = MibScalar
hpSwitchStartupConfigSourceIPAddrType = _HpSwitchStartupConfigSourceIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0, 2),
    _HpSwitchStartupConfigSourceIPAddrType_Type()
)
hpSwitchStartupConfigSourceIPAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpSwitchStartupConfigSourceIPAddrType.setStatus("current")
_HpSwitchStartupConfigSourceIPAddr_Type = InetAddress
_HpSwitchStartupConfigSourceIPAddr_Object = MibScalar
hpSwitchStartupConfigSourceIPAddr = _HpSwitchStartupConfigSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0, 3),
    _HpSwitchStartupConfigSourceIPAddr_Type()
)
hpSwitchStartupConfigSourceIPAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpSwitchStartupConfigSourceIPAddr.setStatus("current")


class _HpSwitchStartupConfigSourceUsername_Type(DisplayString):
    """Custom type hpSwitchStartupConfigSourceUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchStartupConfigSourceUsername_Type.__name__ = "DisplayString"
_HpSwitchStartupConfigSourceUsername_Object = MibScalar
hpSwitchStartupConfigSourceUsername = _HpSwitchStartupConfigSourceUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0, 4),
    _HpSwitchStartupConfigSourceUsername_Type()
)
hpSwitchStartupConfigSourceUsername.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpSwitchStartupConfigSourceUsername.setStatus("current")


class _HpSwitchStartupConfigThrottled_Type(TruthValue):
    """Custom type hpSwitchStartupConfigThrottled based on TruthValue"""


_HpSwitchStartupConfigThrottled_Object = MibScalar
hpSwitchStartupConfigThrottled = _HpSwitchStartupConfigThrottled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0, 5),
    _HpSwitchStartupConfigThrottled_Type()
)
hpSwitchStartupConfigThrottled.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpSwitchStartupConfigThrottled.setStatus("current")


class _HpSwitchSaveConfig_Type(Integer32):
    """Custom type hpSwitchSaveConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noConfigSave", 1),
          ("saveConfig", 2))
    )


_HpSwitchSaveConfig_Type.__name__ = "Integer32"
_HpSwitchSaveConfig_Object = MibScalar
hpSwitchSaveConfig = _HpSwitchSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 1),
    _HpSwitchSaveConfig_Type()
)
hpSwitchSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSaveConfig.setStatus("current")
_HpSwitchAliasTable_Object = MibTable
hpSwitchAliasTable = _HpSwitchAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 2)
)
if mibBuilder.loadTexts:
    hpSwitchAliasTable.setStatus("current")
_HpSwitchAliasEntry_Object = MibTableRow
hpSwitchAliasEntry = _HpSwitchAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 2, 1)
)
hpSwitchAliasEntry.setIndexNames(
    (0, "HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchAliasName"),
)
if mibBuilder.loadTexts:
    hpSwitchAliasEntry.setStatus("current")


class _HpSwitchAliasName_Type(DisplayString):
    """Custom type hpSwitchAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_HpSwitchAliasName_Type.__name__ = "DisplayString"
_HpSwitchAliasName_Object = MibTableColumn
hpSwitchAliasName = _HpSwitchAliasName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 2, 1, 1),
    _HpSwitchAliasName_Type()
)
hpSwitchAliasName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchAliasName.setStatus("current")


class _HpSwitchAliasCommand_Type(OctetString):
    """Custom type hpSwitchAliasCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchAliasCommand_Type.__name__ = "OctetString"
_HpSwitchAliasCommand_Object = MibTableColumn
hpSwitchAliasCommand = _HpSwitchAliasCommand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 2, 1, 2),
    _HpSwitchAliasCommand_Type()
)
hpSwitchAliasCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAliasCommand.setStatus("current")
_HpSwitchAliasConfigRowStatus_Type = RowStatus
_HpSwitchAliasConfigRowStatus_Object = MibTableColumn
hpSwitchAliasConfigRowStatus = _HpSwitchAliasConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 2, 1, 3),
    _HpSwitchAliasConfigRowStatus_Type()
)
hpSwitchAliasConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchAliasConfigRowStatus.setStatus("current")
_HpSwitchACLConfig_ObjectIdentity = ObjectIdentity
hpSwitchACLConfig = _HpSwitchACLConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 3)
)


class _HpSwitchAclLogtimeoutConfig_Type(Integer32):
    """Custom type hpSwitchAclLogtimeoutConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchAclLogtimeoutConfig_Type.__name__ = "Integer32"
_HpSwitchAclLogtimeoutConfig_Object = MibScalar
hpSwitchAclLogtimeoutConfig = _HpSwitchAclLogtimeoutConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 3, 1),
    _HpSwitchAclLogtimeoutConfig_Type()
)
hpSwitchAclLogtimeoutConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAclLogtimeoutConfig.setStatus("current")


class _HpSwitchAclIpv4DenyFragmentedTcpHeader_Type(Integer32):
    """Custom type hpSwitchAclIpv4DenyFragmentedTcpHeader based on Integer32"""
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


_HpSwitchAclIpv4DenyFragmentedTcpHeader_Type.__name__ = "Integer32"
_HpSwitchAclIpv4DenyFragmentedTcpHeader_Object = MibScalar
hpSwitchAclIpv4DenyFragmentedTcpHeader = _HpSwitchAclIpv4DenyFragmentedTcpHeader_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 3, 2),
    _HpSwitchAclIpv4DenyFragmentedTcpHeader_Type()
)
hpSwitchAclIpv4DenyFragmentedTcpHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAclIpv4DenyFragmentedTcpHeader.setStatus("current")


class _HpSwitchAclIpv6DenyNonClassifiableL4Header_Type(Integer32):
    """Custom type hpSwitchAclIpv6DenyNonClassifiableL4Header based on Integer32"""
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


_HpSwitchAclIpv6DenyNonClassifiableL4Header_Type.__name__ = "Integer32"
_HpSwitchAclIpv6DenyNonClassifiableL4Header_Object = MibScalar
hpSwitchAclIpv6DenyNonClassifiableL4Header = _HpSwitchAclIpv6DenyNonClassifiableL4Header_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 3, 3),
    _HpSwitchAclIpv6DenyNonClassifiableL4Header_Type()
)
hpSwitchAclIpv6DenyNonClassifiableL4Header.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAclIpv6DenyNonClassifiableL4Header.setStatus("current")


class _HpSwitchAclGroupingEnable_Type(TruthValue):
    """Custom type hpSwitchAclGroupingEnable based on TruthValue"""


_HpSwitchAclGroupingEnable_Object = MibScalar
hpSwitchAclGroupingEnable = _HpSwitchAclGroupingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 3, 4),
    _HpSwitchAclGroupingEnable_Type()
)
hpSwitchAclGroupingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchAclGroupingEnable.setStatus("current")
_HpicfPortCopyNameTable_Object = MibTable
hpicfPortCopyNameTable = _HpicfPortCopyNameTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfPortCopyNameTable.setStatus("current")
_HpicfPortCopyNameEntry_Object = MibTableRow
hpicfPortCopyNameEntry = _HpicfPortCopyNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfPortCopyNameEntry.setStatus("current")
_HpicfPortCopyName_Type = DisplayString
_HpicfPortCopyName_Object = MibTableColumn
hpicfPortCopyName = _HpicfPortCopyName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 4, 1, 1),
    _HpicfPortCopyName_Type()
)
hpicfPortCopyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfPortCopyName.setStatus("current")


class _HpSwitchDefaultLogon_Type(Integer32):
    """Custom type hpSwitchDefaultLogon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cli", 0),
          ("menu", 1))
    )


_HpSwitchDefaultLogon_Type.__name__ = "Integer32"
_HpSwitchDefaultLogon_Object = MibScalar
hpSwitchDefaultLogon = _HpSwitchDefaultLogon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 5),
    _HpSwitchDefaultLogon_Type()
)
hpSwitchDefaultLogon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchDefaultLogon.setStatus("current")
_HpSwitchChassisLocateTable_Object = MibTable
hpSwitchChassisLocateTable = _HpSwitchChassisLocateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 6)
)
if mibBuilder.loadTexts:
    hpSwitchChassisLocateTable.setStatus("current")
_HpSwitchChassisLocateEntry_Object = MibTableRow
hpSwitchChassisLocateEntry = _HpSwitchChassisLocateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 6, 1)
)
hpSwitchChassisLocateEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchChassisLocateEntry.setStatus("current")


class _HpSwitchChassisLocateState_Type(Integer32):
    """Custom type hpSwitchChassisLocateState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blink", 3),
          ("off", 1),
          ("on", 2))
    )


_HpSwitchChassisLocateState_Type.__name__ = "Integer32"
_HpSwitchChassisLocateState_Object = MibTableColumn
hpSwitchChassisLocateState = _HpSwitchChassisLocateState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 6, 1, 1),
    _HpSwitchChassisLocateState_Type()
)
hpSwitchChassisLocateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchChassisLocateState.setStatus("current")


class _HpSwitchChassisLocateDuration_Type(Integer32):
    """Custom type hpSwitchChassisLocateDuration based on Integer32"""
    defaultValue = 1800


_HpSwitchChassisLocateDuration_Object = MibTableColumn
hpSwitchChassisLocateDuration = _HpSwitchChassisLocateDuration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 6, 1, 2),
    _HpSwitchChassisLocateDuration_Type()
)
hpSwitchChassisLocateDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchChassisLocateDuration.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchChassisLocateDuration.setUnits("seconds")


class _HpSwitchChassisLocateWhen_Type(Integer32):
    """Custom type hpSwitchChassisLocateWhen based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("now", 1),
          ("startup", 2))
    )


_HpSwitchChassisLocateWhen_Type.__name__ = "Integer32"
_HpSwitchChassisLocateWhen_Object = MibTableColumn
hpSwitchChassisLocateWhen = _HpSwitchChassisLocateWhen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 6, 1, 3),
    _HpSwitchChassisLocateWhen_Type()
)
hpSwitchChassisLocateWhen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchChassisLocateWhen.setStatus("current")
_HpSwitchModules_ObjectIdentity = ObjectIdentity
hpSwitchModules = _HpSwitchModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7)
)
_HpSwitchModuleInfoTable_Object = MibTable
hpSwitchModuleInfoTable = _HpSwitchModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hpSwitchModuleInfoTable.setStatus("current")
_HpSwitchModuleInfoEntry_Object = MibTableRow
hpSwitchModuleInfoEntry = _HpSwitchModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 1, 1)
)
hpSwitchModuleInfoEntry.setIndexNames(
    (0, "HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchModuleInfoModId"),
)
if mibBuilder.loadTexts:
    hpSwitchModuleInfoEntry.setStatus("current")


class _HpSwitchModuleInfoModId_Type(Integer32):
    """Custom type hpSwitchModuleInfoModId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpSwitchModuleInfoModId_Type.__name__ = "Integer32"
_HpSwitchModuleInfoModId_Object = MibTableColumn
hpSwitchModuleInfoModId = _HpSwitchModuleInfoModId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 1, 1, 1),
    _HpSwitchModuleInfoModId_Type()
)
hpSwitchModuleInfoModId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchModuleInfoModId.setStatus("current")


class _HpSwitchModuleInfoModType_Type(DisplayString):
    """Custom type hpSwitchModuleInfoModType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HpSwitchModuleInfoModType_Type.__name__ = "DisplayString"
_HpSwitchModuleInfoModType_Object = MibTableColumn
hpSwitchModuleInfoModType = _HpSwitchModuleInfoModType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 1, 1, 2),
    _HpSwitchModuleInfoModType_Type()
)
hpSwitchModuleInfoModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchModuleInfoModType.setStatus("current")
_HpSwitchModuleConfigTable_Object = MibTable
hpSwitchModuleConfigTable = _HpSwitchModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 2)
)
if mibBuilder.loadTexts:
    hpSwitchModuleConfigTable.setStatus("current")
_HpSwitchModuleConfigEntry_Object = MibTableRow
hpSwitchModuleConfigEntry = _HpSwitchModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 2, 1)
)
hpSwitchModuleConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchModuleConfigEntry.setStatus("current")


class _HpSwitchModuleConfigModType_Type(DisplayString):
    """Custom type hpSwitchModuleConfigModType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchModuleConfigModType_Type.__name__ = "DisplayString"
_HpSwitchModuleConfigModType_Object = MibTableColumn
hpSwitchModuleConfigModType = _HpSwitchModuleConfigModType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 2, 1, 1),
    _HpSwitchModuleConfigModType_Type()
)
hpSwitchModuleConfigModType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchModuleConfigModType.setStatus("current")


class _HpSwitchModuleConfigModName_Type(DisplayString):
    """Custom type hpSwitchModuleConfigModName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchModuleConfigModName_Type.__name__ = "DisplayString"
_HpSwitchModuleConfigModName_Object = MibTableColumn
hpSwitchModuleConfigModName = _HpSwitchModuleConfigModName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 2, 1, 2),
    _HpSwitchModuleConfigModName_Type()
)
hpSwitchModuleConfigModName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchModuleConfigModName.setStatus("current")
_HpSwitchModuleConfigModRemove_Type = TruthValue
_HpSwitchModuleConfigModRemove_Object = MibTableColumn
hpSwitchModuleConfigModRemove = _HpSwitchModuleConfigModRemove_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 7, 2, 1, 3),
    _HpSwitchModuleConfigModRemove_Type()
)
hpSwitchModuleConfigModRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchModuleConfigModRemove.setStatus("current")


class _HpSwitchWebSupportUrl_Type(DisplayString):
    """Custom type hpSwitchWebSupportUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchWebSupportUrl_Type.__name__ = "DisplayString"
_HpSwitchWebSupportUrl_Object = MibScalar
hpSwitchWebSupportUrl = _HpSwitchWebSupportUrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 8),
    _HpSwitchWebSupportUrl_Type()
)
hpSwitchWebSupportUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchWebSupportUrl.setStatus("current")


class _HpSwitchStartupConfigSeqNum_Type(Unsigned32):
    """Custom type hpSwitchStartupConfigSeqNum based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpSwitchStartupConfigSeqNum_Type.__name__ = "Unsigned32"
_HpSwitchStartupConfigSeqNum_Object = MibScalar
hpSwitchStartupConfigSeqNum = _HpSwitchStartupConfigSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 9),
    _HpSwitchStartupConfigSeqNum_Type()
)
hpSwitchStartupConfigSeqNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStartupConfigSeqNum.setStatus("current")


class _HpSwitchStartupConfigNotifyEnable_Type(Integer32):
    """Custom type hpSwitchStartupConfigNotifyEnable based on Integer32"""
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


_HpSwitchStartupConfigNotifyEnable_Type.__name__ = "Integer32"
_HpSwitchStartupConfigNotifyEnable_Object = MibScalar
hpSwitchStartupConfigNotifyEnable = _HpSwitchStartupConfigNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 10),
    _HpSwitchStartupConfigNotifyEnable_Type()
)
hpSwitchStartupConfigNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchStartupConfigNotifyEnable.setStatus("current")


class _HpSwitchImplicitConfigSave_Type(Integer32):
    """Custom type hpSwitchImplicitConfigSave based on Integer32"""
    defaultValue = 1

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


_HpSwitchImplicitConfigSave_Type.__name__ = "Integer32"
_HpSwitchImplicitConfigSave_Object = MibScalar
hpSwitchImplicitConfigSave = _HpSwitchImplicitConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 11),
    _HpSwitchImplicitConfigSave_Type()
)
hpSwitchImplicitConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchImplicitConfigSave.setStatus("current")
_HpSwitchRunningCfgChgObjects_ObjectIdentity = ObjectIdentity
hpSwitchRunningCfgChgObjects = _HpSwitchRunningCfgChgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12)
)


class _HpSwitchRunningCfgChgNotifyEnable_Type(Integer32):
    """Custom type hpSwitchRunningCfgChgNotifyEnable based on Integer32"""
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


_HpSwitchRunningCfgChgNotifyEnable_Type.__name__ = "Integer32"
_HpSwitchRunningCfgChgNotifyEnable_Object = MibScalar
hpSwitchRunningCfgChgNotifyEnable = _HpSwitchRunningCfgChgNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 1),
    _HpSwitchRunningCfgChgNotifyEnable_Type()
)
hpSwitchRunningCfgChgNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgNotifyEnable.setStatus("current")


class _HpSwitchRunningCfgChgTransmitInterval_Type(Unsigned32):
    """Custom type hpSwitchRunningCfgChgTransmitInterval based on Unsigned32"""
    defaultValue = 0


_HpSwitchRunningCfgChgTransmitInterval_Object = MibScalar
hpSwitchRunningCfgChgTransmitInterval = _HpSwitchRunningCfgChgTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 2),
    _HpSwitchRunningCfgChgTransmitInterval_Type()
)
hpSwitchRunningCfgChgTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgTransmitInterval.setStatus("current")
_HpSwitchRunningCfgChgLatestDateAndTime_Type = DateAndTime
_HpSwitchRunningCfgChgLatestDateAndTime_Object = MibScalar
hpSwitchRunningCfgChgLatestDateAndTime = _HpSwitchRunningCfgChgLatestDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 3),
    _HpSwitchRunningCfgChgLatestDateAndTime_Type()
)
hpSwitchRunningCfgChgLatestDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgLatestDateAndTime.setStatus("current")
_HpSwitchRunningCfgChgCount_Type = Counter32
_HpSwitchRunningCfgChgCount_Object = MibScalar
hpSwitchRunningCfgChgCount = _HpSwitchRunningCfgChgCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 4),
    _HpSwitchRunningCfgChgCount_Type()
)
hpSwitchRunningCfgChgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgCount.setStatus("current")
_HpSwitchRunningCfgChgEntriesBumped_Type = Counter32
_HpSwitchRunningCfgChgEntriesBumped_Object = MibScalar
hpSwitchRunningCfgChgEntriesBumped = _HpSwitchRunningCfgChgEntriesBumped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 5),
    _HpSwitchRunningCfgChgEntriesBumped_Type()
)
hpSwitchRunningCfgChgEntriesBumped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEntriesBumped.setStatus("current")
_HpSwitchRunningCfgChgEventTable_Object = MibTable
hpSwitchRunningCfgChgEventTable = _HpSwitchRunningCfgChgEventTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6)
)
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventTable.setStatus("current")
_HpSwitchRunningCfgChgEventEntry_Object = MibTableRow
hpSwitchRunningCfgChgEventEntry = _HpSwitchRunningCfgChgEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1)
)
hpSwitchRunningCfgChgEventEntry.setIndexNames(
    (0, "HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventTableIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventEntry.setStatus("current")


class _HpSwitchRunningCfgChgEventTableIndex_Type(Integer32):
    """Custom type hpSwitchRunningCfgChgEventTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpSwitchRunningCfgChgEventTableIndex_Type.__name__ = "Integer32"
_HpSwitchRunningCfgChgEventTableIndex_Object = MibTableColumn
hpSwitchRunningCfgChgEventTableIndex = _HpSwitchRunningCfgChgEventTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1, 1),
    _HpSwitchRunningCfgChgEventTableIndex_Type()
)
hpSwitchRunningCfgChgEventTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventTableIndex.setStatus("current")


class _HpSwitchRunningCfgChgEventId_Type(Unsigned32):
    """Custom type hpSwitchRunningCfgChgEventId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HpSwitchRunningCfgChgEventId_Type.__name__ = "Unsigned32"
_HpSwitchRunningCfgChgEventId_Object = MibTableColumn
hpSwitchRunningCfgChgEventId = _HpSwitchRunningCfgChgEventId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1, 2),
    _HpSwitchRunningCfgChgEventId_Type()
)
hpSwitchRunningCfgChgEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventId.setStatus("current")


class _HpSwitchRunningCfgChgEventMethod_Type(Integer32):
    """Custom type hpSwitchRunningCfgChgEventMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("internalEvent", 5),
          ("menu", 2),
          ("snmp", 3),
          ("unknown", 0),
          ("webUI", 4))
    )


_HpSwitchRunningCfgChgEventMethod_Type.__name__ = "Integer32"
_HpSwitchRunningCfgChgEventMethod_Object = MibTableColumn
hpSwitchRunningCfgChgEventMethod = _HpSwitchRunningCfgChgEventMethod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1, 3),
    _HpSwitchRunningCfgChgEventMethod_Type()
)
hpSwitchRunningCfgChgEventMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventMethod.setStatus("current")
_HpSwitchRunningCfgChgEventSourceIPAddrType_Type = InetAddressType
_HpSwitchRunningCfgChgEventSourceIPAddrType_Object = MibTableColumn
hpSwitchRunningCfgChgEventSourceIPAddrType = _HpSwitchRunningCfgChgEventSourceIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1, 4),
    _HpSwitchRunningCfgChgEventSourceIPAddrType_Type()
)
hpSwitchRunningCfgChgEventSourceIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventSourceIPAddrType.setStatus("current")
_HpSwitchRunningCfgChgEventSourceIPAddr_Type = InetAddress
_HpSwitchRunningCfgChgEventSourceIPAddr_Object = MibTableColumn
hpSwitchRunningCfgChgEventSourceIPAddr = _HpSwitchRunningCfgChgEventSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1, 5),
    _HpSwitchRunningCfgChgEventSourceIPAddr_Type()
)
hpSwitchRunningCfgChgEventSourceIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventSourceIPAddr.setStatus("current")


class _HpSwitchRunningCfgChgEventUsername_Type(DisplayString):
    """Custom type hpSwitchRunningCfgChgEventUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchRunningCfgChgEventUsername_Type.__name__ = "DisplayString"
_HpSwitchRunningCfgChgEventUsername_Object = MibTableColumn
hpSwitchRunningCfgChgEventUsername = _HpSwitchRunningCfgChgEventUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1, 6),
    _HpSwitchRunningCfgChgEventUsername_Type()
)
hpSwitchRunningCfgChgEventUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventUsername.setStatus("current")
_HpSwitchRunningCfgChgEventDateAndTime_Type = DateAndTime
_HpSwitchRunningCfgChgEventDateAndTime_Object = MibTableColumn
hpSwitchRunningCfgChgEventDateAndTime = _HpSwitchRunningCfgChgEventDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 12, 6, 1, 7),
    _HpSwitchRunningCfgChgEventDateAndTime_Type()
)
hpSwitchRunningCfgChgEventDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgEventDateAndTime.setStatus("current")


class _HpSwitchSecureModeLevel_Type(Integer32):
    """Custom type hpSwitchSecureModeLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              16)
        )
    )
    namedValues = NamedValues(
        *(("enhanced", 16),
          ("error", 0),
          ("standard", 1))
    )


_HpSwitchSecureModeLevel_Type.__name__ = "Integer32"
_HpSwitchSecureModeLevel_Object = MibScalar
hpSwitchSecureModeLevel = _HpSwitchSecureModeLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 13),
    _HpSwitchSecureModeLevel_Type()
)
hpSwitchSecureModeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSecureModeLevel.setStatus("current")


class _HpSwitchCdpRunMode_Type(Integer32):
    """Custom type hpSwitchCdpRunMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("passthru", 2),
          ("preStdVoice", 3),
          ("rxonly", 1))
    )


_HpSwitchCdpRunMode_Type.__name__ = "Integer32"
_HpSwitchCdpRunMode_Object = MibScalar
hpSwitchCdpRunMode = _HpSwitchCdpRunMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 14),
    _HpSwitchCdpRunMode_Type()
)
hpSwitchCdpRunMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCdpRunMode.setStatus("current")
_HpSwitchCdpObjects_ObjectIdentity = ObjectIdentity
hpSwitchCdpObjects = _HpSwitchCdpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 15)
)
_HpSwitchCdpPreStdVoiceTable_Object = MibTable
hpSwitchCdpPreStdVoiceTable = _HpSwitchCdpPreStdVoiceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 15, 1)
)
if mibBuilder.loadTexts:
    hpSwitchCdpPreStdVoiceTable.setStatus("current")
_HpSwitchCdpPreStdVoiceEntry_Object = MibTableRow
hpSwitchCdpPreStdVoiceEntry = _HpSwitchCdpPreStdVoiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 15, 1, 1)
)
hpSwitchCdpPreStdVoiceEntry.setIndexNames(
    (0, "HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchCdpPreStdVoiceIfIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchCdpPreStdVoiceEntry.setStatus("current")
_HpSwitchCdpPreStdVoiceIfIndex_Type = InterfaceIndex
_HpSwitchCdpPreStdVoiceIfIndex_Object = MibTableColumn
hpSwitchCdpPreStdVoiceIfIndex = _HpSwitchCdpPreStdVoiceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 15, 1, 1, 1),
    _HpSwitchCdpPreStdVoiceIfIndex_Type()
)
hpSwitchCdpPreStdVoiceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchCdpPreStdVoiceIfIndex.setStatus("current")


class _HpSwitchCdpPreStdVoiceStatus_Type(Integer32):
    """Custom type hpSwitchCdpPreStdVoiceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rxOnly", 2),
          ("txAndRx", 1))
    )


_HpSwitchCdpPreStdVoiceStatus_Type.__name__ = "Integer32"
_HpSwitchCdpPreStdVoiceStatus_Object = MibTableColumn
hpSwitchCdpPreStdVoiceStatus = _HpSwitchCdpPreStdVoiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 15, 1, 1, 2),
    _HpSwitchCdpPreStdVoiceStatus_Type()
)
hpSwitchCdpPreStdVoiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchCdpPreStdVoiceStatus.setStatus("current")
_HpSwitchIgnoreUntagMacPortList_Type = PortList
_HpSwitchIgnoreUntagMacPortList_Object = MibScalar
hpSwitchIgnoreUntagMacPortList = _HpSwitchIgnoreUntagMacPortList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 16),
    _HpSwitchIgnoreUntagMacPortList_Type()
)
hpSwitchIgnoreUntagMacPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchIgnoreUntagMacPortList.setStatus("current")


class _HpSwitchControlPlaneProtectionAdminStatus_Type(Integer32):
    """Custom type hpSwitchControlPlaneProtectionAdminStatus based on Integer32"""
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


_HpSwitchControlPlaneProtectionAdminStatus_Type.__name__ = "Integer32"
_HpSwitchControlPlaneProtectionAdminStatus_Object = MibScalar
hpSwitchControlPlaneProtectionAdminStatus = _HpSwitchControlPlaneProtectionAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 17),
    _HpSwitchControlPlaneProtectionAdminStatus_Type()
)
hpSwitchControlPlaneProtectionAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchControlPlaneProtectionAdminStatus.setStatus("current")
_HpSwitchFPModules_ObjectIdentity = ObjectIdentity
hpSwitchFPModules = _HpSwitchFPModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 19)
)
_HpSwitchFPModuleConfigTable_Object = MibTable
hpSwitchFPModuleConfigTable = _HpSwitchFPModuleConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 19, 1)
)
if mibBuilder.loadTexts:
    hpSwitchFPModuleConfigTable.setStatus("current")
_HpSwitchFPModuleConfigEntry_Object = MibTableRow
hpSwitchFPModuleConfigEntry = _HpSwitchFPModuleConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 19, 1, 1)
)
hpSwitchFPModuleConfigEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hpSwitchFPModuleConfigEntry.setStatus("current")


class _HpSwitchFPModuleConfigType_Type(Integer32):
    """Custom type hpSwitchFPModuleConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("jl078a", 1),
          ("jl079a", 2),
          ("jl081a", 3),
          ("jl083a", 4),
          ("none", 0))
    )


_HpSwitchFPModuleConfigType_Type.__name__ = "Integer32"
_HpSwitchFPModuleConfigType_Object = MibTableColumn
hpSwitchFPModuleConfigType = _HpSwitchFPModuleConfigType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 19, 1, 1, 1),
    _HpSwitchFPModuleConfigType_Type()
)
hpSwitchFPModuleConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFPModuleConfigType.setStatus("current")


class _HpSwitchFPModuleConfigName_Type(DisplayString):
    """Custom type hpSwitchFPModuleConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchFPModuleConfigName_Type.__name__ = "DisplayString"
_HpSwitchFPModuleConfigName_Object = MibTableColumn
hpSwitchFPModuleConfigName = _HpSwitchFPModuleConfigName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 19, 1, 1, 2),
    _HpSwitchFPModuleConfigName_Type()
)
hpSwitchFPModuleConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchFPModuleConfigName.setStatus("current")


class _HpSwitchRESTInterfaceStatus_Type(Integer32):
    """Custom type hpSwitchRESTInterfaceStatus based on Integer32"""
    defaultValue = 1

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


_HpSwitchRESTInterfaceStatus_Type.__name__ = "Integer32"
_HpSwitchRESTInterfaceStatus_Object = MibScalar
hpSwitchRESTInterfaceStatus = _HpSwitchRESTInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 20),
    _HpSwitchRESTInterfaceStatus_Type()
)
hpSwitchRESTInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRESTInterfaceStatus.setStatus("current")


class _HpSwitchRESTSessionIdleTimeout_Type(Integer32):
    """Custom type hpSwitchRESTSessionIdleTimeout based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_HpSwitchRESTSessionIdleTimeout_Type.__name__ = "Integer32"
_HpSwitchRESTSessionIdleTimeout_Object = MibScalar
hpSwitchRESTSessionIdleTimeout = _HpSwitchRESTSessionIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 21),
    _HpSwitchRESTSessionIdleTimeout_Type()
)
hpSwitchRESTSessionIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchRESTSessionIdleTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpSwitchRESTSessionIdleTimeout.setUnits("seconds")
_HpSwitchBasicConfigConformance_ObjectIdentity = ObjectIdentity
hpSwitchBasicConfigConformance = _HpSwitchBasicConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2)
)
_HpSwitchBasicConfigCompliances_ObjectIdentity = ObjectIdentity
hpSwitchBasicConfigCompliances = _HpSwitchBasicConfigCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1)
)
_HpSwitchBasicConfigGroups_ObjectIdentity = ObjectIdentity
hpSwitchBasicConfigGroups = _HpSwitchBasicConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2)
)
_HpSwitchBasicNotificationGroups_ObjectIdentity = ObjectIdentity
hpSwitchBasicNotificationGroups = _HpSwitchBasicNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 3)
)
portCopyEntry.registerAugmentions(
    ("HP-SWITCH-BASIC-CONFIG-MIB",
     "hpicfPortCopyNameEntry")
)
hpicfPortCopyNameEntry.setIndexNames(*portCopyEntry.getIndexNames())

# Managed Objects groups

hpSwitchBasicConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 1)
)
hpSwitchBasicConfigGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchSaveConfig"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchDefaultLogon"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchWebSupportUrl"))
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigGroup.setStatus("current")

hpSwitchAliasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 2)
)
hpSwitchAliasGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchAliasCommand"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchAliasConfigRowStatus"))
)
if mibBuilder.loadTexts:
    hpSwitchAliasGroup.setStatus("current")

hpicfBridgeFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 3)
)
hpicfBridgeFilterConfigGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpicfBridgeFilterDropPortMask"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpicfBridgeFilterEntryStatus"))
)
if mibBuilder.loadTexts:
    hpicfBridgeFilterConfigGroup.setStatus("current")

hpicfPortCopyNameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 4)
)
hpicfPortCopyNameGroup.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpicfPortCopyName")
)
if mibBuilder.loadTexts:
    hpicfPortCopyNameGroup.setStatus("current")

hpSwitchAclLogtimeoutGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 5)
)
hpSwitchAclLogtimeoutGroup.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchAclLogtimeoutConfig")
)
if mibBuilder.loadTexts:
    hpSwitchAclLogtimeoutGroup.setStatus("current")

hpSwitchIgmpProxyDomainConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 6)
)
hpSwitchIgmpProxyDomainConfigGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchIgmpProxyDomainName"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchIgmpProxyDomainStatus"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchIgmpProxyDomainIp"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchIgmpProxyMcastLowerIp"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchIgmpProxyMcastUpperIp"))
)
if mibBuilder.loadTexts:
    hpSwitchIgmpProxyDomainConfigGroup.setStatus("current")

hpSwitchChassisLocateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 7)
)
hpSwitchChassisLocateGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchChassisLocateState"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchChassisLocateDuration"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchChassisLocateWhen"))
)
if mibBuilder.loadTexts:
    hpSwitchChassisLocateGroup.setStatus("current")

hpSwitchModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 8)
)
hpSwitchModuleGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchModuleInfoModType"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchModuleConfigModType"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchModuleConfigModName"))
)
if mibBuilder.loadTexts:
    hpSwitchModuleGroup.setStatus("current")

hpSwitchStartupConfigChangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 9)
)
hpSwitchStartupConfigChangeGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSeqNum"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigNotifyEnable"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSource"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSourceIPAddrType"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSourceIPAddr"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSourceUsername"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigThrottled"))
)
if mibBuilder.loadTexts:
    hpSwitchStartupConfigChangeGroup.setStatus("current")

hpSwitchBasicConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 10)
)
hpSwitchBasicConfigGroup2.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchImplicitConfigSave")
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigGroup2.setStatus("current")

hpSwitchRunningCfgChgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 11)
)
hpSwitchRunningCfgChgGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgNotifyEnable"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgTransmitInterval"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgLatestDateAndTime"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgCount"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEntriesBumped"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventId"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventMethod"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventSourceIPAddrType"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventSourceIPAddr"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventUsername"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventDateAndTime"))
)
if mibBuilder.loadTexts:
    hpSwitchRunningCfgChgGroup.setStatus("current")

hpSwitchBasicConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 12)
)
hpSwitchBasicConfigGroup3.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchSecureModeLevel")
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigGroup3.setStatus("current")

hpSwitchCdpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 13)
)
hpSwitchCdpConfigGroup.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchCdpRunMode")
)
if mibBuilder.loadTexts:
    hpSwitchCdpConfigGroup.setStatus("current")

hpSwitchCdpPreStdVoiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 14)
)
hpSwitchCdpPreStdVoiceGroup.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchCdpPreStdVoiceStatus")
)
if mibBuilder.loadTexts:
    hpSwitchCdpPreStdVoiceGroup.setStatus("current")

hpSwitchIgnoreUntagMacConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 15)
)
hpSwitchIgnoreUntagMacConfigGroup.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchIgnoreUntagMacPortList")
)
if mibBuilder.loadTexts:
    hpSwitchIgnoreUntagMacConfigGroup.setStatus("current")

hpSwitchModuleConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 16)
)
hpSwitchModuleConfigGroup.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchModuleConfigModRemove")
)
if mibBuilder.loadTexts:
    hpSwitchModuleConfigGroup.setStatus("current")

hpSwitchBasicConfigGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 17)
)
hpSwitchBasicConfigGroup4.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchControlPlaneProtectionAdminStatus")
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigGroup4.setStatus("current")

hpSwitchAclGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 20)
)
hpSwitchAclGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchAclIpv4DenyFragmentedTcpHeader"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchAclIpv6DenyNonClassifiableL4Header"))
)
if mibBuilder.loadTexts:
    hpSwitchAclGroup.setStatus("current")

hpSwitchFPModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 21)
)
hpSwitchFPModuleGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchFPModuleConfigType"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchFPModuleConfigName"))
)
if mibBuilder.loadTexts:
    hpSwitchFPModuleGroup.setStatus("current")

hpSwitchRESTInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 22)
)
hpSwitchRESTInterfaceGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRESTInterfaceStatus"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRESTSessionIdleTimeout"))
)
if mibBuilder.loadTexts:
    hpSwitchRESTInterfaceGroup.setStatus("current")

hpSwitchAclGroupingEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 2, 23)
)
hpSwitchAclGroupingEnableGroup.setObjects(
    ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchAclGroupingEnable")
)
if mibBuilder.loadTexts:
    hpSwitchAclGroupingEnableGroup.setStatus("current")


# Notification objects

hpSwitchStartupConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0, 6)
)
hpSwitchStartupConfigChange.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSeqNum"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSource"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSourceIPAddrType"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSourceIPAddr"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigSourceUsername"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigThrottled"))
)
if mibBuilder.loadTexts:
    hpSwitchStartupConfigChange.setStatus(
        "current"
    )

hpSwitchRunningConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 1, 0, 7)
)
hpSwitchRunningConfigChange.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventId"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventMethod"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventSourceIPAddrType"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventSourceIPAddr"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventUsername"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningCfgChgEventDateAndTime"))
)
if mibBuilder.loadTexts:
    hpSwitchRunningConfigChange.setStatus(
        "current"
    )


# Notifications groups

hpSwitchBasicNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 3, 1)
)
hpSwitchBasicNotificationGroup.setObjects(
      *(("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchRunningConfigChange"),
        ("HP-SWITCH-BASIC-CONFIG-MIB", "hpSwitchStartupConfigChange"))
)
if mibBuilder.loadTexts:
    hpSwitchBasicNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpSwitchBasicConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance2.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance3.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance4.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance5.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance6.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance7.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance8.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance10.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance11.setStatus(
        "current"
    )

hpSwitchBasicConfigCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 7, 1, 29, 2, 1, 12)
)
if mibBuilder.loadTexts:
    hpSwitchBasicConfigCompliance12.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SWITCH-BASIC-CONFIG-MIB",
    **{"hpicfBridgeFilterConfigTable": hpicfBridgeFilterConfigTable,
       "hpicfBridgeFilterConfigEntry": hpicfBridgeFilterConfigEntry,
       "hpicfBridgeFilterName": hpicfBridgeFilterName,
       "hpicfBridgeFilterDropPortMask": hpicfBridgeFilterDropPortMask,
       "hpicfBridgeFilterEntryStatus": hpicfBridgeFilterEntryStatus,
       "hpSwitchIgmpProxyDomainConfigTable": hpSwitchIgmpProxyDomainConfigTable,
       "hpSwitchIgmpProxyDomainConfigEntry": hpSwitchIgmpProxyDomainConfigEntry,
       "hpSwitchIgmpProxyDomainId": hpSwitchIgmpProxyDomainId,
       "hpSwitchIgmpProxyDomainStatus": hpSwitchIgmpProxyDomainStatus,
       "hpSwitchIgmpProxyDomainName": hpSwitchIgmpProxyDomainName,
       "hpSwitchIgmpProxyDomainIp": hpSwitchIgmpProxyDomainIp,
       "hpSwitchIgmpProxyMcastLowerIp": hpSwitchIgmpProxyMcastLowerIp,
       "hpSwitchIgmpProxyMcastUpperIp": hpSwitchIgmpProxyMcastUpperIp,
       "hpSwitchBasicConfigMIB": hpSwitchBasicConfigMIB,
       "hpSwitchBasicConfigObjects": hpSwitchBasicConfigObjects,
       "hpSwitchNotificationObjects": hpSwitchNotificationObjects,
       "hpSwitchStartupConfigSource": hpSwitchStartupConfigSource,
       "hpSwitchStartupConfigSourceIPAddrType": hpSwitchStartupConfigSourceIPAddrType,
       "hpSwitchStartupConfigSourceIPAddr": hpSwitchStartupConfigSourceIPAddr,
       "hpSwitchStartupConfigSourceUsername": hpSwitchStartupConfigSourceUsername,
       "hpSwitchStartupConfigThrottled": hpSwitchStartupConfigThrottled,
       "hpSwitchStartupConfigChange": hpSwitchStartupConfigChange,
       "hpSwitchRunningConfigChange": hpSwitchRunningConfigChange,
       "hpSwitchSaveConfig": hpSwitchSaveConfig,
       "hpSwitchAliasTable": hpSwitchAliasTable,
       "hpSwitchAliasEntry": hpSwitchAliasEntry,
       "hpSwitchAliasName": hpSwitchAliasName,
       "hpSwitchAliasCommand": hpSwitchAliasCommand,
       "hpSwitchAliasConfigRowStatus": hpSwitchAliasConfigRowStatus,
       "hpSwitchACLConfig": hpSwitchACLConfig,
       "hpSwitchAclLogtimeoutConfig": hpSwitchAclLogtimeoutConfig,
       "hpSwitchAclIpv4DenyFragmentedTcpHeader": hpSwitchAclIpv4DenyFragmentedTcpHeader,
       "hpSwitchAclIpv6DenyNonClassifiableL4Header": hpSwitchAclIpv6DenyNonClassifiableL4Header,
       "hpSwitchAclGroupingEnable": hpSwitchAclGroupingEnable,
       "hpicfPortCopyNameTable": hpicfPortCopyNameTable,
       "hpicfPortCopyNameEntry": hpicfPortCopyNameEntry,
       "hpicfPortCopyName": hpicfPortCopyName,
       "hpSwitchDefaultLogon": hpSwitchDefaultLogon,
       "hpSwitchChassisLocateTable": hpSwitchChassisLocateTable,
       "hpSwitchChassisLocateEntry": hpSwitchChassisLocateEntry,
       "hpSwitchChassisLocateState": hpSwitchChassisLocateState,
       "hpSwitchChassisLocateDuration": hpSwitchChassisLocateDuration,
       "hpSwitchChassisLocateWhen": hpSwitchChassisLocateWhen,
       "hpSwitchModules": hpSwitchModules,
       "hpSwitchModuleInfoTable": hpSwitchModuleInfoTable,
       "hpSwitchModuleInfoEntry": hpSwitchModuleInfoEntry,
       "hpSwitchModuleInfoModId": hpSwitchModuleInfoModId,
       "hpSwitchModuleInfoModType": hpSwitchModuleInfoModType,
       "hpSwitchModuleConfigTable": hpSwitchModuleConfigTable,
       "hpSwitchModuleConfigEntry": hpSwitchModuleConfigEntry,
       "hpSwitchModuleConfigModType": hpSwitchModuleConfigModType,
       "hpSwitchModuleConfigModName": hpSwitchModuleConfigModName,
       "hpSwitchModuleConfigModRemove": hpSwitchModuleConfigModRemove,
       "hpSwitchWebSupportUrl": hpSwitchWebSupportUrl,
       "hpSwitchStartupConfigSeqNum": hpSwitchStartupConfigSeqNum,
       "hpSwitchStartupConfigNotifyEnable": hpSwitchStartupConfigNotifyEnable,
       "hpSwitchImplicitConfigSave": hpSwitchImplicitConfigSave,
       "hpSwitchRunningCfgChgObjects": hpSwitchRunningCfgChgObjects,
       "hpSwitchRunningCfgChgNotifyEnable": hpSwitchRunningCfgChgNotifyEnable,
       "hpSwitchRunningCfgChgTransmitInterval": hpSwitchRunningCfgChgTransmitInterval,
       "hpSwitchRunningCfgChgLatestDateAndTime": hpSwitchRunningCfgChgLatestDateAndTime,
       "hpSwitchRunningCfgChgCount": hpSwitchRunningCfgChgCount,
       "hpSwitchRunningCfgChgEntriesBumped": hpSwitchRunningCfgChgEntriesBumped,
       "hpSwitchRunningCfgChgEventTable": hpSwitchRunningCfgChgEventTable,
       "hpSwitchRunningCfgChgEventEntry": hpSwitchRunningCfgChgEventEntry,
       "hpSwitchRunningCfgChgEventTableIndex": hpSwitchRunningCfgChgEventTableIndex,
       "hpSwitchRunningCfgChgEventId": hpSwitchRunningCfgChgEventId,
       "hpSwitchRunningCfgChgEventMethod": hpSwitchRunningCfgChgEventMethod,
       "hpSwitchRunningCfgChgEventSourceIPAddrType": hpSwitchRunningCfgChgEventSourceIPAddrType,
       "hpSwitchRunningCfgChgEventSourceIPAddr": hpSwitchRunningCfgChgEventSourceIPAddr,
       "hpSwitchRunningCfgChgEventUsername": hpSwitchRunningCfgChgEventUsername,
       "hpSwitchRunningCfgChgEventDateAndTime": hpSwitchRunningCfgChgEventDateAndTime,
       "hpSwitchSecureModeLevel": hpSwitchSecureModeLevel,
       "hpSwitchCdpRunMode": hpSwitchCdpRunMode,
       "hpSwitchCdpObjects": hpSwitchCdpObjects,
       "hpSwitchCdpPreStdVoiceTable": hpSwitchCdpPreStdVoiceTable,
       "hpSwitchCdpPreStdVoiceEntry": hpSwitchCdpPreStdVoiceEntry,
       "hpSwitchCdpPreStdVoiceIfIndex": hpSwitchCdpPreStdVoiceIfIndex,
       "hpSwitchCdpPreStdVoiceStatus": hpSwitchCdpPreStdVoiceStatus,
       "hpSwitchIgnoreUntagMacPortList": hpSwitchIgnoreUntagMacPortList,
       "hpSwitchControlPlaneProtectionAdminStatus": hpSwitchControlPlaneProtectionAdminStatus,
       "hpSwitchFPModules": hpSwitchFPModules,
       "hpSwitchFPModuleConfigTable": hpSwitchFPModuleConfigTable,
       "hpSwitchFPModuleConfigEntry": hpSwitchFPModuleConfigEntry,
       "hpSwitchFPModuleConfigType": hpSwitchFPModuleConfigType,
       "hpSwitchFPModuleConfigName": hpSwitchFPModuleConfigName,
       "hpSwitchRESTInterfaceStatus": hpSwitchRESTInterfaceStatus,
       "hpSwitchRESTSessionIdleTimeout": hpSwitchRESTSessionIdleTimeout,
       "hpSwitchBasicConfigConformance": hpSwitchBasicConfigConformance,
       "hpSwitchBasicConfigCompliances": hpSwitchBasicConfigCompliances,
       "hpSwitchBasicConfigCompliance": hpSwitchBasicConfigCompliance,
       "hpSwitchBasicConfigCompliance2": hpSwitchBasicConfigCompliance2,
       "hpSwitchBasicConfigCompliance3": hpSwitchBasicConfigCompliance3,
       "hpSwitchBasicConfigCompliance4": hpSwitchBasicConfigCompliance4,
       "hpSwitchBasicConfigCompliance5": hpSwitchBasicConfigCompliance5,
       "hpSwitchBasicConfigCompliance6": hpSwitchBasicConfigCompliance6,
       "hpSwitchBasicConfigCompliance7": hpSwitchBasicConfigCompliance7,
       "hpSwitchBasicConfigCompliance8": hpSwitchBasicConfigCompliance8,
       "hpSwitchBasicConfigCompliance10": hpSwitchBasicConfigCompliance10,
       "hpSwitchBasicConfigCompliance11": hpSwitchBasicConfigCompliance11,
       "hpSwitchBasicConfigCompliance12": hpSwitchBasicConfigCompliance12,
       "hpSwitchBasicConfigGroups": hpSwitchBasicConfigGroups,
       "hpSwitchBasicConfigGroup": hpSwitchBasicConfigGroup,
       "hpSwitchAliasGroup": hpSwitchAliasGroup,
       "hpicfBridgeFilterConfigGroup": hpicfBridgeFilterConfigGroup,
       "hpicfPortCopyNameGroup": hpicfPortCopyNameGroup,
       "hpSwitchAclLogtimeoutGroup": hpSwitchAclLogtimeoutGroup,
       "hpSwitchIgmpProxyDomainConfigGroup": hpSwitchIgmpProxyDomainConfigGroup,
       "hpSwitchChassisLocateGroup": hpSwitchChassisLocateGroup,
       "hpSwitchModuleGroup": hpSwitchModuleGroup,
       "hpSwitchStartupConfigChangeGroup": hpSwitchStartupConfigChangeGroup,
       "hpSwitchBasicConfigGroup2": hpSwitchBasicConfigGroup2,
       "hpSwitchRunningCfgChgGroup": hpSwitchRunningCfgChgGroup,
       "hpSwitchBasicConfigGroup3": hpSwitchBasicConfigGroup3,
       "hpSwitchCdpConfigGroup": hpSwitchCdpConfigGroup,
       "hpSwitchCdpPreStdVoiceGroup": hpSwitchCdpPreStdVoiceGroup,
       "hpSwitchIgnoreUntagMacConfigGroup": hpSwitchIgnoreUntagMacConfigGroup,
       "hpSwitchModuleConfigGroup": hpSwitchModuleConfigGroup,
       "hpSwitchBasicConfigGroup4": hpSwitchBasicConfigGroup4,
       "hpSwitchAclGroup": hpSwitchAclGroup,
       "hpSwitchFPModuleGroup": hpSwitchFPModuleGroup,
       "hpSwitchRESTInterfaceGroup": hpSwitchRESTInterfaceGroup,
       "hpSwitchAclGroupingEnableGroup": hpSwitchAclGroupingEnableGroup,
       "hpSwitchBasicNotificationGroups": hpSwitchBasicNotificationGroups,
       "hpSwitchBasicNotificationGroup": hpSwitchBasicNotificationGroup}
)
