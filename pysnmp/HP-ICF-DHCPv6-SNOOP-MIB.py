# SNMP MIB module (HP-ICF-DHCPv6-SNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DHCPv6-SNOOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:21 2024
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

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "VidList")

(hpicfSaviObjectsBindingEntry,
 hpicfSaviObjectsPortEntry) = mibBuilder.importSymbols(
    "HPICF-SAVI-MIB",
    "hpicfSaviObjectsBindingEntry",
    "hpicfSaviObjectsPortEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfDSnoopV6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102)
)
hpicfDSnoopV6.setRevisions(
        ("2017-11-08 00:00",
         "2015-01-28 00:00",
         "2013-10-06 00:00",
         "2013-04-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDSnoopV6Notifications_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6Notifications = _HpicfDSnoopV6Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0)
)
_HpicfDsnoopV6SourceBindingOutOfResourcesObjects_ObjectIdentity = ObjectIdentity
hpicfDsnoopV6SourceBindingOutOfResourcesObjects = _HpicfDsnoopV6SourceBindingOutOfResourcesObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 2)
)
_HpicfDsnoopV6SourceBindingPort_Type = InterfaceIndex
_HpicfDsnoopV6SourceBindingPort_Object = MibScalar
hpicfDsnoopV6SourceBindingPort = _HpicfDsnoopV6SourceBindingPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 2, 1),
    _HpicfDsnoopV6SourceBindingPort_Type()
)
hpicfDsnoopV6SourceBindingPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDsnoopV6SourceBindingPort.setStatus("current")
_HpicfDsnoopV6SourceBindingMacAddress_Type = MacAddress
_HpicfDsnoopV6SourceBindingMacAddress_Object = MibScalar
hpicfDsnoopV6SourceBindingMacAddress = _HpicfDsnoopV6SourceBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 2, 2),
    _HpicfDsnoopV6SourceBindingMacAddress_Type()
)
hpicfDsnoopV6SourceBindingMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDsnoopV6SourceBindingMacAddress.setStatus("current")
_HpicfDsnoopV6SourceBindingIpAddressType_Type = InetAddressType
_HpicfDsnoopV6SourceBindingIpAddressType_Object = MibScalar
hpicfDsnoopV6SourceBindingIpAddressType = _HpicfDsnoopV6SourceBindingIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 2, 3),
    _HpicfDsnoopV6SourceBindingIpAddressType_Type()
)
hpicfDsnoopV6SourceBindingIpAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDsnoopV6SourceBindingIpAddressType.setStatus("current")
_HpicfDsnoopV6SourceBindingIpAddress_Type = InetAddress
_HpicfDsnoopV6SourceBindingIpAddress_Object = MibScalar
hpicfDsnoopV6SourceBindingIpAddress = _HpicfDsnoopV6SourceBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 2, 4),
    _HpicfDsnoopV6SourceBindingIpAddress_Type()
)
hpicfDsnoopV6SourceBindingIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDsnoopV6SourceBindingIpAddress.setStatus("current")
_HpicfDsnoopV6SourceBindingVlan_Type = VlanIndex
_HpicfDsnoopV6SourceBindingVlan_Object = MibScalar
hpicfDsnoopV6SourceBindingVlan = _HpicfDsnoopV6SourceBindingVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 2, 5),
    _HpicfDsnoopV6SourceBindingVlan_Type()
)
hpicfDsnoopV6SourceBindingVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDsnoopV6SourceBindingVlan.setStatus("current")
_HpicfDSnoopV6SourceBindingNotifyObjects_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6SourceBindingNotifyObjects = _HpicfDSnoopV6SourceBindingNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 4)
)
_HpicfDSnoopV6SourceBindingNotifyCount_Type = Counter32
_HpicfDSnoopV6SourceBindingNotifyCount_Object = MibScalar
hpicfDSnoopV6SourceBindingNotifyCount = _HpicfDSnoopV6SourceBindingNotifyCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 4, 1),
    _HpicfDSnoopV6SourceBindingNotifyCount_Type()
)
hpicfDSnoopV6SourceBindingNotifyCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SourceBindingNotifyCount.setStatus("current")
_HpicfDSnoopV6SourceBindingErrantSrcMAC_Type = MacAddress
_HpicfDSnoopV6SourceBindingErrantSrcMAC_Object = MibScalar
hpicfDSnoopV6SourceBindingErrantSrcMAC = _HpicfDSnoopV6SourceBindingErrantSrcMAC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 4, 2),
    _HpicfDSnoopV6SourceBindingErrantSrcMAC_Type()
)
hpicfDSnoopV6SourceBindingErrantSrcMAC.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SourceBindingErrantSrcMAC.setStatus("current")
_HpicfDSnoopV6SourceBindingErrantSrcIPType_Type = InetAddressType
_HpicfDSnoopV6SourceBindingErrantSrcIPType_Object = MibScalar
hpicfDSnoopV6SourceBindingErrantSrcIPType = _HpicfDSnoopV6SourceBindingErrantSrcIPType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 4, 3),
    _HpicfDSnoopV6SourceBindingErrantSrcIPType_Type()
)
hpicfDSnoopV6SourceBindingErrantSrcIPType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SourceBindingErrantSrcIPType.setStatus("current")
_HpicfDSnoopV6SourceBindingErrantSrcIP_Type = InetAddress
_HpicfDSnoopV6SourceBindingErrantSrcIP_Object = MibScalar
hpicfDSnoopV6SourceBindingErrantSrcIP = _HpicfDSnoopV6SourceBindingErrantSrcIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 4, 4),
    _HpicfDSnoopV6SourceBindingErrantSrcIP_Type()
)
hpicfDSnoopV6SourceBindingErrantSrcIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SourceBindingErrantSrcIP.setStatus("current")
_HpicfDSnoopV6Objects_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6Objects = _HpicfDSnoopV6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1)
)
_HpicfDSnoopV6Config_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6Config = _HpicfDSnoopV6Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1)
)
_HpicfDSnoopV6GlobalCfg_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6GlobalCfg = _HpicfDSnoopV6GlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1)
)
_HpicfDSnoopV6Enable_Type = TruthValue
_HpicfDSnoopV6Enable_Object = MibScalar
hpicfDSnoopV6Enable = _HpicfDSnoopV6Enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 1),
    _HpicfDSnoopV6Enable_Type()
)
hpicfDSnoopV6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6Enable.setStatus("current")
_HpicfDSnoopV6VlanEnable_Type = VidList
_HpicfDSnoopV6VlanEnable_Object = MibScalar
hpicfDSnoopV6VlanEnable = _HpicfDSnoopV6VlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 2),
    _HpicfDSnoopV6VlanEnable_Type()
)
hpicfDSnoopV6VlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6VlanEnable.setStatus("current")
_HpicfDSnoopV6DatabaseFile_Type = SnmpAdminString
_HpicfDSnoopV6DatabaseFile_Object = MibScalar
hpicfDSnoopV6DatabaseFile = _HpicfDSnoopV6DatabaseFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 3),
    _HpicfDSnoopV6DatabaseFile_Type()
)
hpicfDSnoopV6DatabaseFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseFile.setStatus("current")


class _HpicfDSnoopV6DatabaseWriteDelay_Type(Unsigned32):
    """Custom type hpicfDSnoopV6DatabaseWriteDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_HpicfDSnoopV6DatabaseWriteDelay_Type.__name__ = "Unsigned32"
_HpicfDSnoopV6DatabaseWriteDelay_Object = MibScalar
hpicfDSnoopV6DatabaseWriteDelay = _HpicfDSnoopV6DatabaseWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 4),
    _HpicfDSnoopV6DatabaseWriteDelay_Type()
)
hpicfDSnoopV6DatabaseWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseWriteDelay.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseWriteDelay.setUnits("seconds")


class _HpicfDSnoopV6DatabaseWriteTimeout_Type(Unsigned32):
    """Custom type hpicfDSnoopV6DatabaseWriteTimeout based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_HpicfDSnoopV6DatabaseWriteTimeout_Type.__name__ = "Unsigned32"
_HpicfDSnoopV6DatabaseWriteTimeout_Object = MibScalar
hpicfDSnoopV6DatabaseWriteTimeout = _HpicfDSnoopV6DatabaseWriteTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 5),
    _HpicfDSnoopV6DatabaseWriteTimeout_Type()
)
hpicfDSnoopV6DatabaseWriteTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseWriteTimeout.setStatus("current")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseWriteTimeout.setUnits("seconds")


class _HpicfDSnoopV6OutOfResourcesTrapCtrl_Type(Integer32):
    """Custom type hpicfDSnoopV6OutOfResourcesTrapCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfDSnoopV6OutOfResourcesTrapCtrl_Type.__name__ = "Integer32"
_HpicfDSnoopV6OutOfResourcesTrapCtrl_Object = MibScalar
hpicfDSnoopV6OutOfResourcesTrapCtrl = _HpicfDSnoopV6OutOfResourcesTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 6),
    _HpicfDSnoopV6OutOfResourcesTrapCtrl_Type()
)
hpicfDSnoopV6OutOfResourcesTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6OutOfResourcesTrapCtrl.setStatus("current")


class _HpicfDSnoopV6ErrantReplyTrapCtrl_Type(Integer32):
    """Custom type hpicfDSnoopV6ErrantReplyTrapCtrl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfDSnoopV6ErrantReplyTrapCtrl_Type.__name__ = "Integer32"
_HpicfDSnoopV6ErrantReplyTrapCtrl_Object = MibScalar
hpicfDSnoopV6ErrantReplyTrapCtrl = _HpicfDSnoopV6ErrantReplyTrapCtrl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 7),
    _HpicfDSnoopV6ErrantReplyTrapCtrl_Type()
)
hpicfDSnoopV6ErrantReplyTrapCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6ErrantReplyTrapCtrl.setStatus("current")


class _HpicfDSnoopV6DatabaseFTPort_Type(Unsigned32):
    """Custom type hpicfDSnoopV6DatabaseFTPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfDSnoopV6DatabaseFTPort_Type.__name__ = "Unsigned32"
_HpicfDSnoopV6DatabaseFTPort_Object = MibScalar
hpicfDSnoopV6DatabaseFTPort = _HpicfDSnoopV6DatabaseFTPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 8),
    _HpicfDSnoopV6DatabaseFTPort_Type()
)
hpicfDSnoopV6DatabaseFTPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseFTPort.setStatus("current")
_HpicfDSnoopV6DatabaseSFTPUsername_Type = SnmpAdminString
_HpicfDSnoopV6DatabaseSFTPUsername_Object = MibScalar
hpicfDSnoopV6DatabaseSFTPUsername = _HpicfDSnoopV6DatabaseSFTPUsername_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 9),
    _HpicfDSnoopV6DatabaseSFTPUsername_Type()
)
hpicfDSnoopV6DatabaseSFTPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseSFTPUsername.setStatus("current")
_HpicfDSnoopV6DatabaseSFTPPassword_Type = SnmpAdminString
_HpicfDSnoopV6DatabaseSFTPPassword_Object = MibScalar
hpicfDSnoopV6DatabaseSFTPPassword = _HpicfDSnoopV6DatabaseSFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 10),
    _HpicfDSnoopV6DatabaseSFTPPassword_Type()
)
hpicfDSnoopV6DatabaseSFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseSFTPPassword.setStatus("current")


class _HpicfDSnoopV6DatabaseValidateSFTPServer_Type(Integer32):
    """Custom type hpicfDSnoopV6DatabaseValidateSFTPServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfDSnoopV6DatabaseValidateSFTPServer_Type.__name__ = "Integer32"
_HpicfDSnoopV6DatabaseValidateSFTPServer_Object = MibScalar
hpicfDSnoopV6DatabaseValidateSFTPServer = _HpicfDSnoopV6DatabaseValidateSFTPServer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 1, 11),
    _HpicfDSnoopV6DatabaseValidateSFTPServer_Type()
)
hpicfDSnoopV6DatabaseValidateSFTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DatabaseValidateSFTPServer.setStatus("current")
_HpicfDSnoopV6AuthorizedServerTable_Object = MibTable
hpicfDSnoopV6AuthorizedServerTable = _HpicfDSnoopV6AuthorizedServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6AuthorizedServerTable.setStatus("current")
_HpicfDSnoopV6AuthorizedServerEntry_Object = MibTableRow
hpicfDSnoopV6AuthorizedServerEntry = _HpicfDSnoopV6AuthorizedServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 2, 1)
)
hpicfDSnoopV6AuthorizedServerEntry.setIndexNames(
    (0, "HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6AuthorizedServerAddrType"),
    (0, "HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6AuthorizedServerAddress"),
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6AuthorizedServerEntry.setStatus("current")
_HpicfDSnoopV6AuthorizedServerAddrType_Type = InetAddressType
_HpicfDSnoopV6AuthorizedServerAddrType_Object = MibTableColumn
hpicfDSnoopV6AuthorizedServerAddrType = _HpicfDSnoopV6AuthorizedServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 2, 1, 1),
    _HpicfDSnoopV6AuthorizedServerAddrType_Type()
)
hpicfDSnoopV6AuthorizedServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDSnoopV6AuthorizedServerAddrType.setStatus("current")


class _HpicfDSnoopV6AuthorizedServerAddress_Type(InetAddress):
    """Custom type hpicfDSnoopV6AuthorizedServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_HpicfDSnoopV6AuthorizedServerAddress_Type.__name__ = "InetAddress"
_HpicfDSnoopV6AuthorizedServerAddress_Object = MibTableColumn
hpicfDSnoopV6AuthorizedServerAddress = _HpicfDSnoopV6AuthorizedServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 2, 1, 2),
    _HpicfDSnoopV6AuthorizedServerAddress_Type()
)
hpicfDSnoopV6AuthorizedServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDSnoopV6AuthorizedServerAddress.setStatus("current")
_HpicfDSnoopV6AuthorizedServerStatus_Type = RowStatus
_HpicfDSnoopV6AuthorizedServerStatus_Object = MibTableColumn
hpicfDSnoopV6AuthorizedServerStatus = _HpicfDSnoopV6AuthorizedServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 2, 1, 3),
    _HpicfDSnoopV6AuthorizedServerStatus_Type()
)
hpicfDSnoopV6AuthorizedServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDSnoopV6AuthorizedServerStatus.setStatus("current")
_HpicfDSnoopV6PortMaxBindingTable_Object = MibTable
hpicfDSnoopV6PortMaxBindingTable = _HpicfDSnoopV6PortMaxBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6PortMaxBindingTable.setStatus("current")
_HpicfDSnoopV6PortMaxBindingEntry_Object = MibTableRow
hpicfDSnoopV6PortMaxBindingEntry = _HpicfDSnoopV6PortMaxBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6PortMaxBindingEntry.setStatus("current")


class _HpicfDSnoopV6PortStaticBinding_Type(Unsigned32):
    """Custom type hpicfDSnoopV6PortStaticBinding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_HpicfDSnoopV6PortStaticBinding_Type.__name__ = "Unsigned32"
_HpicfDSnoopV6PortStaticBinding_Object = MibTableColumn
hpicfDSnoopV6PortStaticBinding = _HpicfDSnoopV6PortStaticBinding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 3, 1, 2),
    _HpicfDSnoopV6PortStaticBinding_Type()
)
hpicfDSnoopV6PortStaticBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6PortStaticBinding.setStatus("current")


class _HpicfDSnoopV6PortDynamicBinding_Type(Unsigned32):
    """Custom type hpicfDSnoopV6PortDynamicBinding based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8192),
    )


_HpicfDSnoopV6PortDynamicBinding_Type.__name__ = "Unsigned32"
_HpicfDSnoopV6PortDynamicBinding_Object = MibTableColumn
hpicfDSnoopV6PortDynamicBinding = _HpicfDSnoopV6PortDynamicBinding_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 3, 1, 3),
    _HpicfDSnoopV6PortDynamicBinding_Type()
)
hpicfDSnoopV6PortDynamicBinding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6PortDynamicBinding.setStatus("current")
_HpicfDSnoopV6StaticBindingTable_Object = MibTable
hpicfDSnoopV6StaticBindingTable = _HpicfDSnoopV6StaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6StaticBindingTable.setStatus("current")
_HpicfDSnoopV6StaticBindingEntry_Object = MibTableRow
hpicfDSnoopV6StaticBindingEntry = _HpicfDSnoopV6StaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6StaticBindingEntry.setStatus("current")


class _HpicfDSnoopV6BindingVlanId_Type(VlanIndex):
    """Custom type hpicfDSnoopV6BindingVlanId based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpicfDSnoopV6BindingVlanId_Type.__name__ = "VlanIndex"
_HpicfDSnoopV6BindingVlanId_Object = MibTableColumn
hpicfDSnoopV6BindingVlanId = _HpicfDSnoopV6BindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 4, 1, 1),
    _HpicfDSnoopV6BindingVlanId_Type()
)
hpicfDSnoopV6BindingVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6BindingVlanId.setStatus("current")


class _HpicfDSnoopV6BindingLLAddress_Type(InetAddress):
    """Custom type hpicfDSnoopV6BindingLLAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_HpicfDSnoopV6BindingLLAddress_Type.__name__ = "InetAddress"
_HpicfDSnoopV6BindingLLAddress_Object = MibTableColumn
hpicfDSnoopV6BindingLLAddress = _HpicfDSnoopV6BindingLLAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 4, 1, 2),
    _HpicfDSnoopV6BindingLLAddress_Type()
)
hpicfDSnoopV6BindingLLAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6BindingLLAddress.setStatus("current")
_HpicfDSnoopV6BindingSecVlan_Type = Unsigned32
_HpicfDSnoopV6BindingSecVlan_Object = MibTableColumn
hpicfDSnoopV6BindingSecVlan = _HpicfDSnoopV6BindingSecVlan_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 1, 4, 1, 3),
    _HpicfDSnoopV6BindingSecVlan_Type()
)
hpicfDSnoopV6BindingSecVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6BindingSecVlan.setStatus("current")
_HpicfDSnoopV6GlobalStats_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6GlobalStats = _HpicfDSnoopV6GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2)
)
_HpicfDSnoopV6CSForwards_Type = Counter32
_HpicfDSnoopV6CSForwards_Object = MibScalar
hpicfDSnoopV6CSForwards = _HpicfDSnoopV6CSForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 1),
    _HpicfDSnoopV6CSForwards_Type()
)
hpicfDSnoopV6CSForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6CSForwards.setStatus("current")
_HpicfDSnoopV6CSMACMismatches_Type = Counter32
_HpicfDSnoopV6CSMACMismatches_Object = MibScalar
hpicfDSnoopV6CSMACMismatches = _HpicfDSnoopV6CSMACMismatches_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 2),
    _HpicfDSnoopV6CSMACMismatches_Type()
)
hpicfDSnoopV6CSMACMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6CSMACMismatches.setStatus("current")
_HpicfDSnoopV6CSBadReleases_Type = Counter32
_HpicfDSnoopV6CSBadReleases_Object = MibScalar
hpicfDSnoopV6CSBadReleases = _HpicfDSnoopV6CSBadReleases_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 3),
    _HpicfDSnoopV6CSBadReleases_Type()
)
hpicfDSnoopV6CSBadReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6CSBadReleases.setStatus("current")
_HpicfDSnoopV6CSUntrustedDestPorts_Type = Counter32
_HpicfDSnoopV6CSUntrustedDestPorts_Object = MibScalar
hpicfDSnoopV6CSUntrustedDestPorts = _HpicfDSnoopV6CSUntrustedDestPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 4),
    _HpicfDSnoopV6CSUntrustedDestPorts_Type()
)
hpicfDSnoopV6CSUntrustedDestPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6CSUntrustedDestPorts.setStatus("current")
_HpicfDSnoopV6SCForwards_Type = Counter32
_HpicfDSnoopV6SCForwards_Object = MibScalar
hpicfDSnoopV6SCForwards = _HpicfDSnoopV6SCForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 5),
    _HpicfDSnoopV6SCForwards_Type()
)
hpicfDSnoopV6SCForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SCForwards.setStatus("current")
_HpicfDSnoopV6SCUntrustedPorts_Type = Counter32
_HpicfDSnoopV6SCUntrustedPorts_Object = MibScalar
hpicfDSnoopV6SCUntrustedPorts = _HpicfDSnoopV6SCUntrustedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 6),
    _HpicfDSnoopV6SCUntrustedPorts_Type()
)
hpicfDSnoopV6SCUntrustedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SCUntrustedPorts.setStatus("current")
_HpicfDSnoopV6SCRelayReplyUntrustedPorts_Type = Counter32
_HpicfDSnoopV6SCRelayReplyUntrustedPorts_Object = MibScalar
hpicfDSnoopV6SCRelayReplyUntrustedPorts = _HpicfDSnoopV6SCRelayReplyUntrustedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 7),
    _HpicfDSnoopV6SCRelayReplyUntrustedPorts_Type()
)
hpicfDSnoopV6SCRelayReplyUntrustedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SCRelayReplyUntrustedPorts.setStatus("current")
_HpicfDSnoopV6SCUnauthorizedServers_Type = Counter32
_HpicfDSnoopV6SCUnauthorizedServers_Object = MibScalar
hpicfDSnoopV6SCUnauthorizedServers = _HpicfDSnoopV6SCUnauthorizedServers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 8),
    _HpicfDSnoopV6SCUnauthorizedServers_Type()
)
hpicfDSnoopV6SCUnauthorizedServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6SCUnauthorizedServers.setStatus("current")
_HpicfDSnoopV6DBFileWriteAttempts_Type = Counter32
_HpicfDSnoopV6DBFileWriteAttempts_Object = MibScalar
hpicfDSnoopV6DBFileWriteAttempts = _HpicfDSnoopV6DBFileWriteAttempts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 9),
    _HpicfDSnoopV6DBFileWriteAttempts_Type()
)
hpicfDSnoopV6DBFileWriteAttempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DBFileWriteAttempts.setStatus("current")
_HpicfDSnoopV6DBFileWriteFailures_Type = Counter32
_HpicfDSnoopV6DBFileWriteFailures_Object = MibScalar
hpicfDSnoopV6DBFileWriteFailures = _HpicfDSnoopV6DBFileWriteFailures_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 10),
    _HpicfDSnoopV6DBFileWriteFailures_Type()
)
hpicfDSnoopV6DBFileWriteFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DBFileWriteFailures.setStatus("current")


class _HpicfDSnoopV6DBFileReadStatus_Type(Integer32):
    """Custom type hpicfDSnoopV6DBFileReadStatus based on Integer32"""
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
        *(("failed", 4),
          ("inProgress", 2),
          ("notConfigured", 1),
          ("succeeded", 3))
    )


_HpicfDSnoopV6DBFileReadStatus_Type.__name__ = "Integer32"
_HpicfDSnoopV6DBFileReadStatus_Object = MibScalar
hpicfDSnoopV6DBFileReadStatus = _HpicfDSnoopV6DBFileReadStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 11),
    _HpicfDSnoopV6DBFileReadStatus_Type()
)
hpicfDSnoopV6DBFileReadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DBFileReadStatus.setStatus("current")


class _HpicfDSnoopV6DBFileWriteStatus_Type(Integer32):
    """Custom type hpicfDSnoopV6DBFileWriteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("delaying", 2),
          ("failed", 5),
          ("inProgress", 3),
          ("notConfigured", 1),
          ("succeeded", 4))
    )


_HpicfDSnoopV6DBFileWriteStatus_Type.__name__ = "Integer32"
_HpicfDSnoopV6DBFileWriteStatus_Object = MibScalar
hpicfDSnoopV6DBFileWriteStatus = _HpicfDSnoopV6DBFileWriteStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 12),
    _HpicfDSnoopV6DBFileWriteStatus_Type()
)
hpicfDSnoopV6DBFileWriteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DBFileWriteStatus.setStatus("current")
_HpicfDSnoopV6DBFileLastWriteTime_Type = DateAndTime
_HpicfDSnoopV6DBFileLastWriteTime_Object = MibScalar
hpicfDSnoopV6DBFileLastWriteTime = _HpicfDSnoopV6DBFileLastWriteTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 13),
    _HpicfDSnoopV6DBFileLastWriteTime_Type()
)
hpicfDSnoopV6DBFileLastWriteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6DBFileLastWriteTime.setStatus("current")
_HpicfDSnoopV6MaxbindPktsDropped_Type = Counter32
_HpicfDSnoopV6MaxbindPktsDropped_Object = MibScalar
hpicfDSnoopV6MaxbindPktsDropped = _HpicfDSnoopV6MaxbindPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 2, 14),
    _HpicfDSnoopV6MaxbindPktsDropped_Type()
)
hpicfDSnoopV6MaxbindPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDSnoopV6MaxbindPktsDropped.setStatus("current")
_HpicfDSnoopV6ClearStatsOptions_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6ClearStatsOptions = _HpicfDSnoopV6ClearStatsOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 3)
)
_HpicfDSnoopV6ClearStats_Type = TruthValue
_HpicfDSnoopV6ClearStats_Object = MibScalar
hpicfDSnoopV6ClearStats = _HpicfDSnoopV6ClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 1, 3, 1),
    _HpicfDSnoopV6ClearStats_Type()
)
hpicfDSnoopV6ClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDSnoopV6ClearStats.setStatus("current")
_HpicfDSnoopV6Conformance_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6Conformance = _HpicfDSnoopV6Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2)
)
_HpicfDSnoopV6Groups_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6Groups = _HpicfDSnoopV6Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1)
)
_HpicfDSnoopV6Compliances_ObjectIdentity = ObjectIdentity
hpicfDSnoopV6Compliances = _HpicfDSnoopV6Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 3)
)
hpicfSaviObjectsPortEntry.registerAugmentions(
    ("HP-ICF-DHCPv6-SNOOP-MIB",
     "hpicfDSnoopV6PortMaxBindingEntry")
)
hpicfDSnoopV6PortMaxBindingEntry.setIndexNames(*hpicfSaviObjectsPortEntry.getIndexNames())
hpicfSaviObjectsBindingEntry.registerAugmentions(
    ("HP-ICF-DHCPv6-SNOOP-MIB",
     "hpicfDSnoopV6StaticBindingEntry")
)
hpicfDSnoopV6StaticBindingEntry.setIndexNames(*hpicfSaviObjectsBindingEntry.getIndexNames())

# Managed Objects groups

hpicfDSnoopV6BaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 1)
)
hpicfDSnoopV6BaseGroup.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6Enable"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6VlanEnable"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6CSForwards"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6CSBadReleases"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6CSUntrustedDestPorts"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6CSMACMismatches"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SCForwards"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SCUnauthorizedServers"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SCUntrustedPorts"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SCRelayReplyUntrustedPorts"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6BaseGroup.setStatus("current")

hpicfDSnoopV6ServersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 2)
)
hpicfDSnoopV6ServersGroup.setObjects(
    ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6AuthorizedServerStatus")
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6ServersGroup.setStatus("current")

hpicfDSnoopV6DbaseFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 3)
)
hpicfDSnoopV6DbaseFileGroup.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseFile"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseWriteDelay"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseWriteTimeout"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileWriteAttempts"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileWriteFailures"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileReadStatus"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileWriteStatus"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileLastWriteTime"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6DbaseFileGroup.setStatus("deprecated")

hpicfDSnoopV6MaxBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 4)
)
hpicfDSnoopV6MaxBindingsGroup.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6MaxbindPktsDropped"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6PortStaticBinding"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6PortDynamicBinding"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6MaxBindingsGroup.setStatus("current")

hpicfDSnoopV6StaticBindingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 5)
)
hpicfDSnoopV6StaticBindingsGroup.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6BindingVlanId"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6BindingLLAddress"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6BindingSecVlan"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6StaticBindingsGroup.setStatus("current")

hpicfDSnoopV6ClearStatsOptionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 6)
)
hpicfDSnoopV6ClearStatsOptionsGroup.setObjects(
    ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6ClearStats")
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6ClearStatsOptionsGroup.setStatus("current")

hpicfDSnoopV6TrapObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 7)
)
hpicfDSnoopV6TrapObjectsGroup.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingNotifyCount"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingErrantSrcMAC"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingErrantSrcIPType"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingErrantSrcIP"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingPort"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingMacAddress"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingIpAddressType"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingIpAddress"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingVlan"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6OutOfResourcesTrapCtrl"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6ErrantReplyTrapCtrl"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6TrapObjectsGroup.setStatus("current")

hpicfDSnoopV6DbaseFileGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 9)
)
hpicfDSnoopV6DbaseFileGroup1.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseFile"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseWriteDelay"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseWriteTimeout"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileWriteAttempts"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileWriteFailures"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileReadStatus"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileWriteStatus"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DBFileLastWriteTime"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseFTPort"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseSFTPUsername"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseSFTPPassword"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6DatabaseValidateSFTPServer"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6DbaseFileGroup1.setStatus("current")


# Notification objects

hpicfDSnoopV6SourceBindingOutOfResources = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 1)
)
hpicfDSnoopV6SourceBindingOutOfResources.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingPort"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingMacAddress"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingIpAddressType"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingIpAddress"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDsnoopV6SourceBindingVlan"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6SourceBindingOutOfResources.setStatus(
        "current"
    )

hpicfDSnoopV6SourceBindingErrantReply = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 0, 3)
)
hpicfDSnoopV6SourceBindingErrantReply.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingNotifyCount"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingErrantSrcMAC"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingErrantSrcIPType"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingErrantSrcIP"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6SourceBindingErrantReply.setStatus(
        "current"
    )


# Notifications groups

hpicfDSnoopV6TrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 1, 8)
)
hpicfDSnoopV6TrapsGroup.setObjects(
      *(("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingOutOfResources"),
        ("HP-ICF-DHCPv6-SNOOP-MIB", "hpicfDSnoopV6SourceBindingErrantReply"))
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6TrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfDSnoopV6Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6Compliance2.setStatus(
        "deprecated"
    )

hpicfDSnoopV6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 102, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hpicfDSnoopV6Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DHCPv6-SNOOP-MIB",
    **{"hpicfDSnoopV6": hpicfDSnoopV6,
       "hpicfDSnoopV6Notifications": hpicfDSnoopV6Notifications,
       "hpicfDSnoopV6SourceBindingOutOfResources": hpicfDSnoopV6SourceBindingOutOfResources,
       "hpicfDsnoopV6SourceBindingOutOfResourcesObjects": hpicfDsnoopV6SourceBindingOutOfResourcesObjects,
       "hpicfDsnoopV6SourceBindingPort": hpicfDsnoopV6SourceBindingPort,
       "hpicfDsnoopV6SourceBindingMacAddress": hpicfDsnoopV6SourceBindingMacAddress,
       "hpicfDsnoopV6SourceBindingIpAddressType": hpicfDsnoopV6SourceBindingIpAddressType,
       "hpicfDsnoopV6SourceBindingIpAddress": hpicfDsnoopV6SourceBindingIpAddress,
       "hpicfDsnoopV6SourceBindingVlan": hpicfDsnoopV6SourceBindingVlan,
       "hpicfDSnoopV6SourceBindingErrantReply": hpicfDSnoopV6SourceBindingErrantReply,
       "hpicfDSnoopV6SourceBindingNotifyObjects": hpicfDSnoopV6SourceBindingNotifyObjects,
       "hpicfDSnoopV6SourceBindingNotifyCount": hpicfDSnoopV6SourceBindingNotifyCount,
       "hpicfDSnoopV6SourceBindingErrantSrcMAC": hpicfDSnoopV6SourceBindingErrantSrcMAC,
       "hpicfDSnoopV6SourceBindingErrantSrcIPType": hpicfDSnoopV6SourceBindingErrantSrcIPType,
       "hpicfDSnoopV6SourceBindingErrantSrcIP": hpicfDSnoopV6SourceBindingErrantSrcIP,
       "hpicfDSnoopV6Objects": hpicfDSnoopV6Objects,
       "hpicfDSnoopV6Config": hpicfDSnoopV6Config,
       "hpicfDSnoopV6GlobalCfg": hpicfDSnoopV6GlobalCfg,
       "hpicfDSnoopV6Enable": hpicfDSnoopV6Enable,
       "hpicfDSnoopV6VlanEnable": hpicfDSnoopV6VlanEnable,
       "hpicfDSnoopV6DatabaseFile": hpicfDSnoopV6DatabaseFile,
       "hpicfDSnoopV6DatabaseWriteDelay": hpicfDSnoopV6DatabaseWriteDelay,
       "hpicfDSnoopV6DatabaseWriteTimeout": hpicfDSnoopV6DatabaseWriteTimeout,
       "hpicfDSnoopV6OutOfResourcesTrapCtrl": hpicfDSnoopV6OutOfResourcesTrapCtrl,
       "hpicfDSnoopV6ErrantReplyTrapCtrl": hpicfDSnoopV6ErrantReplyTrapCtrl,
       "hpicfDSnoopV6DatabaseFTPort": hpicfDSnoopV6DatabaseFTPort,
       "hpicfDSnoopV6DatabaseSFTPUsername": hpicfDSnoopV6DatabaseSFTPUsername,
       "hpicfDSnoopV6DatabaseSFTPPassword": hpicfDSnoopV6DatabaseSFTPPassword,
       "hpicfDSnoopV6DatabaseValidateSFTPServer": hpicfDSnoopV6DatabaseValidateSFTPServer,
       "hpicfDSnoopV6AuthorizedServerTable": hpicfDSnoopV6AuthorizedServerTable,
       "hpicfDSnoopV6AuthorizedServerEntry": hpicfDSnoopV6AuthorizedServerEntry,
       "hpicfDSnoopV6AuthorizedServerAddrType": hpicfDSnoopV6AuthorizedServerAddrType,
       "hpicfDSnoopV6AuthorizedServerAddress": hpicfDSnoopV6AuthorizedServerAddress,
       "hpicfDSnoopV6AuthorizedServerStatus": hpicfDSnoopV6AuthorizedServerStatus,
       "hpicfDSnoopV6PortMaxBindingTable": hpicfDSnoopV6PortMaxBindingTable,
       "hpicfDSnoopV6PortMaxBindingEntry": hpicfDSnoopV6PortMaxBindingEntry,
       "hpicfDSnoopV6PortStaticBinding": hpicfDSnoopV6PortStaticBinding,
       "hpicfDSnoopV6PortDynamicBinding": hpicfDSnoopV6PortDynamicBinding,
       "hpicfDSnoopV6StaticBindingTable": hpicfDSnoopV6StaticBindingTable,
       "hpicfDSnoopV6StaticBindingEntry": hpicfDSnoopV6StaticBindingEntry,
       "hpicfDSnoopV6BindingVlanId": hpicfDSnoopV6BindingVlanId,
       "hpicfDSnoopV6BindingLLAddress": hpicfDSnoopV6BindingLLAddress,
       "hpicfDSnoopV6BindingSecVlan": hpicfDSnoopV6BindingSecVlan,
       "hpicfDSnoopV6GlobalStats": hpicfDSnoopV6GlobalStats,
       "hpicfDSnoopV6CSForwards": hpicfDSnoopV6CSForwards,
       "hpicfDSnoopV6CSMACMismatches": hpicfDSnoopV6CSMACMismatches,
       "hpicfDSnoopV6CSBadReleases": hpicfDSnoopV6CSBadReleases,
       "hpicfDSnoopV6CSUntrustedDestPorts": hpicfDSnoopV6CSUntrustedDestPorts,
       "hpicfDSnoopV6SCForwards": hpicfDSnoopV6SCForwards,
       "hpicfDSnoopV6SCUntrustedPorts": hpicfDSnoopV6SCUntrustedPorts,
       "hpicfDSnoopV6SCRelayReplyUntrustedPorts": hpicfDSnoopV6SCRelayReplyUntrustedPorts,
       "hpicfDSnoopV6SCUnauthorizedServers": hpicfDSnoopV6SCUnauthorizedServers,
       "hpicfDSnoopV6DBFileWriteAttempts": hpicfDSnoopV6DBFileWriteAttempts,
       "hpicfDSnoopV6DBFileWriteFailures": hpicfDSnoopV6DBFileWriteFailures,
       "hpicfDSnoopV6DBFileReadStatus": hpicfDSnoopV6DBFileReadStatus,
       "hpicfDSnoopV6DBFileWriteStatus": hpicfDSnoopV6DBFileWriteStatus,
       "hpicfDSnoopV6DBFileLastWriteTime": hpicfDSnoopV6DBFileLastWriteTime,
       "hpicfDSnoopV6MaxbindPktsDropped": hpicfDSnoopV6MaxbindPktsDropped,
       "hpicfDSnoopV6ClearStatsOptions": hpicfDSnoopV6ClearStatsOptions,
       "hpicfDSnoopV6ClearStats": hpicfDSnoopV6ClearStats,
       "hpicfDSnoopV6Conformance": hpicfDSnoopV6Conformance,
       "hpicfDSnoopV6Groups": hpicfDSnoopV6Groups,
       "hpicfDSnoopV6BaseGroup": hpicfDSnoopV6BaseGroup,
       "hpicfDSnoopV6ServersGroup": hpicfDSnoopV6ServersGroup,
       "hpicfDSnoopV6DbaseFileGroup": hpicfDSnoopV6DbaseFileGroup,
       "hpicfDSnoopV6MaxBindingsGroup": hpicfDSnoopV6MaxBindingsGroup,
       "hpicfDSnoopV6StaticBindingsGroup": hpicfDSnoopV6StaticBindingsGroup,
       "hpicfDSnoopV6ClearStatsOptionsGroup": hpicfDSnoopV6ClearStatsOptionsGroup,
       "hpicfDSnoopV6TrapObjectsGroup": hpicfDSnoopV6TrapObjectsGroup,
       "hpicfDSnoopV6TrapsGroup": hpicfDSnoopV6TrapsGroup,
       "hpicfDSnoopV6DbaseFileGroup1": hpicfDSnoopV6DbaseFileGroup1,
       "hpicfDSnoopV6Compliances": hpicfDSnoopV6Compliances,
       "hpicfDSnoopV6Compliance2": hpicfDSnoopV6Compliance2,
       "hpicfDSnoopV6Compliance": hpicfDSnoopV6Compliance}
)
