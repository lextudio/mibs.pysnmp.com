# SNMP MIB module (ZHNLANDEVICE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNLANDEVICE
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:58 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(VlanTypeValues,) = mibBuilder.importSymbols(
    "ZHNLAYER2BRIDGING",
    "VlanTypeValues")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhnLANDevice = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41)
)
zhnLANDevice.setRevisions(
        ("2012-06-13 12:00",
         "2012-05-10 12:00",
         "2012-04-11 02:11",
         "2012-01-27 12:00",
         "2011-01-11 00:00",
         "2010-07-21 00:00",
         "2010-04-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LANEthernetStatusValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class LANEthernetMaxBitRateValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class LANEthernetDuplexModeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class LANEthernetPauseModeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class IPInterfaceAddressingTypeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class IGMPSnoopingModeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class DNSTypeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class IpPppoeConnectionTypeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class PPPUserConnectionRequestValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class PPPAuthenticationProtocolValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class PPPEncryptionProtocolValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class PPPCompressionProtocolValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class WANPppConnectionStatusValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class WANPppLastConnectionErrorValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class LANRateLimitBurstSizeValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class LANRateLimitDirectionValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class LANEthernetAclValues(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class LANEthernetIpProtocolValues(Integer32, TextualConvention):
    status = "current"
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
        *(("any", 5),
          ("icmp", 3),
          ("igmp", 4),
          ("tcp", 1),
          ("udp", 2))
    )



# MIB Managed Objects in the order of their OIDs

_ZhnLANDeviceObjects_ObjectIdentity = ObjectIdentity
zhnLANDeviceObjects = _ZhnLANDeviceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1)
)
_LanDeviceTable_Object = MibTable
lanDeviceTable = _LanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 1)
)
if mibBuilder.loadTexts:
    lanDeviceTable.setStatus("current")
_LanDeviceEntry_Object = MibTableRow
lanDeviceEntry = _LanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 1, 1)
)
lanDeviceEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
)
if mibBuilder.loadTexts:
    lanDeviceEntry.setStatus("current")
_LanDeviceIndex_Type = Unsigned32
_LanDeviceIndex_Object = MibTableColumn
lanDeviceIndex = _LanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 1, 1, 1),
    _LanDeviceIndex_Type()
)
lanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lanDeviceIndex.setStatus("current")
_LanEthernetInterfaceNumberOfEntries_Type = Unsigned32
_LanEthernetInterfaceNumberOfEntries_Object = MibTableColumn
lanEthernetInterfaceNumberOfEntries = _LanEthernetInterfaceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 1, 1, 2),
    _LanEthernetInterfaceNumberOfEntries_Type()
)
lanEthernetInterfaceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEthernetInterfaceNumberOfEntries.setStatus("current")
_LanUSBInterfaceNumberOfEntries_Type = Unsigned32
_LanUSBInterfaceNumberOfEntries_Object = MibTableColumn
lanUSBInterfaceNumberOfEntries = _LanUSBInterfaceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 1, 1, 3),
    _LanUSBInterfaceNumberOfEntries_Type()
)
lanUSBInterfaceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanUSBInterfaceNumberOfEntries.setStatus("current")
_LanWLANConfigurationNumberOfEntries_Type = Unsigned32
_LanWLANConfigurationNumberOfEntries_Object = MibTableColumn
lanWLANConfigurationNumberOfEntries = _LanWLANConfigurationNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 1, 1, 4),
    _LanWLANConfigurationNumberOfEntries_Type()
)
lanWLANConfigurationNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanWLANConfigurationNumberOfEntries.setStatus("current")
_LanMocaInterfaceNumberOfEntries_Type = Unsigned32
_LanMocaInterfaceNumberOfEntries_Object = MibTableColumn
lanMocaInterfaceNumberOfEntries = _LanMocaInterfaceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 1, 1, 5),
    _LanMocaInterfaceNumberOfEntries_Type()
)
lanMocaInterfaceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanMocaInterfaceNumberOfEntries.setStatus("current")
_IgmpSnoopingCfgTable_Object = MibTable
igmpSnoopingCfgTable = _IgmpSnoopingCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 2)
)
if mibBuilder.loadTexts:
    igmpSnoopingCfgTable.setStatus("current")
_IgmpSnoopingCfgEntry_Object = MibTableRow
igmpSnoopingCfgEntry = _IgmpSnoopingCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 2, 1)
)
igmpSnoopingCfgEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopingCfgEntry.setStatus("current")
_IgmpEnable_Type = TruthValue
_IgmpEnable_Object = MibTableColumn
igmpEnable = _IgmpEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 2, 1, 1),
    _IgmpEnable_Type()
)
igmpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnable.setStatus("current")
_IgmpMode_Type = IGMPSnoopingModeValues
_IgmpMode_Object = MibTableColumn
igmpMode = _IgmpMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 2, 1, 2),
    _IgmpMode_Type()
)
igmpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpMode.setStatus("current")
_IgmpIfName_Type = OctetString
_IgmpIfName_Object = MibTableColumn
igmpIfName = _IgmpIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 2, 1, 3),
    _IgmpIfName_Type()
)
igmpIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpIfName.setStatus("current")
_LanHostConfigManagementObjects_ObjectIdentity = ObjectIdentity
lanHostConfigManagementObjects = _LanHostConfigManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3)
)
_LanHostConfigManagementTable_Object = MibTable
lanHostConfigManagementTable = _LanHostConfigManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1)
)
if mibBuilder.loadTexts:
    lanHostConfigManagementTable.setStatus("current")
_LanHostConfigManagementEntry_Object = MibTableRow
lanHostConfigManagementEntry = _LanHostConfigManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1)
)
lanHostConfigManagementEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
)
if mibBuilder.loadTexts:
    lanHostConfigManagementEntry.setStatus("current")
_DhcpServerConfigurable_Type = TruthValue
_DhcpServerConfigurable_Object = MibTableColumn
dhcpServerConfigurable = _DhcpServerConfigurable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 1),
    _DhcpServerConfigurable_Type()
)
dhcpServerConfigurable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServerConfigurable.setStatus("current")
_ZhnDhcpServerEnable_Type = TruthValue
_ZhnDhcpServerEnable_Object = MibTableColumn
zhnDhcpServerEnable = _ZhnDhcpServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 2),
    _ZhnDhcpServerEnable_Type()
)
zhnDhcpServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnDhcpServerEnable.setStatus("current")
_DhcpRelay_Type = TruthValue
_DhcpRelay_Object = MibTableColumn
dhcpRelay = _DhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 3),
    _DhcpRelay_Type()
)
dhcpRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpRelay.setStatus("current")
_DhcpRelayServer_Type = IpAddress
_DhcpRelayServer_Object = MibTableColumn
dhcpRelayServer = _DhcpRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 4),
    _DhcpRelayServer_Type()
)
dhcpRelayServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRelayServer.setStatus("current")
_MinAddress_Type = IpAddress
_MinAddress_Object = MibTableColumn
minAddress = _MinAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 5),
    _MinAddress_Type()
)
minAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minAddress.setStatus("current")
_MaxAddress_Type = IpAddress
_MaxAddress_Object = MibTableColumn
maxAddress = _MaxAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 6),
    _MaxAddress_Type()
)
maxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxAddress.setStatus("current")
_ReservedAddresses_Type = OctetString
_ReservedAddresses_Object = MibTableColumn
reservedAddresses = _ReservedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 7),
    _ReservedAddresses_Type()
)
reservedAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    reservedAddresses.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibTableColumn
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 8),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_DnsServers_Type = OctetString
_DnsServers_Object = MibTableColumn
dnsServers = _DnsServers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 9),
    _DnsServers_Type()
)
dnsServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServers.setStatus("current")
_DomainName_Type = OctetString
_DomainName_Object = MibTableColumn
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 10),
    _DomainName_Type()
)
domainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainName.setStatus("current")
_IpRouters_Type = OctetString
_IpRouters_Object = MibTableColumn
ipRouters = _IpRouters_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 11),
    _IpRouters_Type()
)
ipRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRouters.setStatus("current")


class _DhcpLeaseTime_Type(Integer32):
    """Custom type dhcpLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpLeaseTime_Type.__name__ = "Integer32"
_DhcpLeaseTime_Object = MibTableColumn
dhcpLeaseTime = _DhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 12),
    _DhcpLeaseTime_Type()
)
dhcpLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpLeaseTime.setStatus("current")
_IpInterfaceNumberOfEntries_Type = Unsigned32
_IpInterfaceNumberOfEntries_Object = MibTableColumn
ipInterfaceNumberOfEntries = _IpInterfaceNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 1, 1, 13),
    _IpInterfaceNumberOfEntries_Type()
)
ipInterfaceNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceNumberOfEntries.setStatus("current")
_IpInterfaceObjects_ObjectIdentity = ObjectIdentity
ipInterfaceObjects = _IpInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2)
)
_ZhnIpInterfaceTable_Object = MibTable
zhnIpInterfaceTable = _ZhnIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    zhnIpInterfaceTable.setStatus("current")
_ZhnIpInterfaceEntry_Object = MibTableRow
zhnIpInterfaceEntry = _ZhnIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1)
)
zhnIpInterfaceEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "ipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    zhnIpInterfaceEntry.setStatus("current")
_IpInterfaceIndex_Type = Unsigned32
_IpInterfaceIndex_Object = MibTableColumn
ipInterfaceIndex = _IpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 1),
    _IpInterfaceIndex_Type()
)
ipInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipInterfaceIndex.setStatus("current")
_IpInterfaceEnable_Type = TruthValue
_IpInterfaceEnable_Object = MibTableColumn
ipInterfaceEnable = _IpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 2),
    _IpInterfaceEnable_Type()
)
ipInterfaceEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceEnable.setStatus("current")
_IpInterfaceIPAddress_Type = IpAddress
_IpInterfaceIPAddress_Object = MibTableColumn
ipInterfaceIPAddress = _IpInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 3),
    _IpInterfaceIPAddress_Type()
)
ipInterfaceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceIPAddress.setStatus("current")
_IpInterfaceSubnetMask_Type = IpAddress
_IpInterfaceSubnetMask_Object = MibTableColumn
ipInterfaceSubnetMask = _IpInterfaceSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 4),
    _IpInterfaceSubnetMask_Type()
)
ipInterfaceSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceSubnetMask.setStatus("current")
_IpInterfaceAddressingType_Type = IPInterfaceAddressingTypeValues
_IpInterfaceAddressingType_Object = MibTableColumn
ipInterfaceAddressingType = _IpInterfaceAddressingType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 5),
    _IpInterfaceAddressingType_Type()
)
ipInterfaceAddressingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceAddressingType.setStatus("current")
_IpInterfaceifName_Type = OctetString
_IpInterfaceifName_Object = MibTableColumn
ipInterfaceifName = _IpInterfaceifName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 6),
    _IpInterfaceifName_Type()
)
ipInterfaceifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceifName.setStatus("current")
_FirewallEnabled_Type = TruthValue
_FirewallEnabled_Object = MibTableColumn
firewallEnabled = _FirewallEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 7),
    _FirewallEnabled_Type()
)
firewallEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firewallEnabled.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibTableColumn
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 8),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")
_NatEnabled_Type = TruthValue
_NatEnabled_Object = MibTableColumn
natEnabled = _NatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 9),
    _NatEnabled_Type()
)
natEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    natEnabled.setStatus("current")
_DhcpcPid_Type = Unsigned32
_DhcpcPid_Object = MibTableColumn
dhcpcPid = _DhcpcPid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 10),
    _DhcpcPid_Type()
)
dhcpcPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpcPid.setStatus("current")
_DnsType_Type = DNSTypeValues
_DnsType_Object = MibTableColumn
dnsType = _DnsType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 11),
    _DnsType_Type()
)
dnsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsType.setStatus("current")
_PrimaryDnsIPAddress_Type = IpAddress
_PrimaryDnsIPAddress_Object = MibTableColumn
primaryDnsIPAddress = _PrimaryDnsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 12),
    _PrimaryDnsIPAddress_Type()
)
primaryDnsIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    primaryDnsIPAddress.setStatus("current")
_SecondaryDnsIPAddress_Type = IpAddress
_SecondaryDnsIPAddress_Object = MibTableColumn
secondaryDnsIPAddress = _SecondaryDnsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 13),
    _SecondaryDnsIPAddress_Type()
)
secondaryDnsIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secondaryDnsIPAddress.setStatus("current")
_ZhnVlanType_Type = VlanTypeValues
_ZhnVlanType_Object = MibTableColumn
zhnVlanType = _ZhnVlanType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 14),
    _ZhnVlanType_Type()
)
zhnVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhnVlanType.setStatus("current")
_ConnectionType_Type = IpPppoeConnectionTypeValues
_ConnectionType_Object = MibTableColumn
connectionType = _ConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 15),
    _ConnectionType_Type()
)
connectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionType.setStatus("current")


class _MaxMTUSize_Type(Unsigned32):
    """Custom type maxMTUSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1540),
    )


_MaxMTUSize_Type.__name__ = "Unsigned32"
_MaxMTUSize_Object = MibTableColumn
maxMTUSize = _MaxMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 16),
    _MaxMTUSize_Type()
)
maxMTUSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxMTUSize.setStatus("current")
_AlternateWanIfName_Type = OctetString
_AlternateWanIfName_Object = MibTableColumn
alternateWanIfName = _AlternateWanIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 17),
    _AlternateWanIfName_Type()
)
alternateWanIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alternateWanIfName.setStatus("current")
_NaptEnabled_Type = TruthValue
_NaptEnabled_Object = MibTableColumn
naptEnabled = _NaptEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 1, 1, 18),
    _NaptEnabled_Type()
)
naptEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    naptEnabled.setStatus("current")
_PppoeConfigObjects_ObjectIdentity = ObjectIdentity
pppoeConfigObjects = _PppoeConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2)
)
_PppoeConfigTable_Object = MibTable
pppoeConfigTable = _PppoeConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pppoeConfigTable.setStatus("current")
_PppoeConfigEntry_Object = MibTableRow
pppoeConfigEntry = _PppoeConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1)
)
pppoeConfigEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "ipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    pppoeConfigEntry.setStatus("current")
_PppoeIfName_Type = OctetString
_PppoeIfName_Object = MibTableColumn
pppoeIfName = _PppoeIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 1),
    _PppoeIfName_Type()
)
pppoeIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pppoeIfName.setStatus("current")
_Pid_Type = Unsigned32
_Pid_Object = MibTableColumn
pid = _Pid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 2),
    _Pid_Type()
)
pid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pid.setStatus("current")
_ConnectionRequest_Type = PPPUserConnectionRequestValues
_ConnectionRequest_Object = MibTableColumn
connectionRequest = _ConnectionRequest_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 3),
    _ConnectionRequest_Type()
)
connectionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    connectionRequest.setStatus("current")
_Username_Type = OctetString
_Username_Object = MibTableColumn
username = _Username_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 4),
    _Username_Type()
)
username.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    username.setStatus("current")
_Password_Type = OctetString
_Password_Object = MibTableColumn
password = _Password_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 5),
    _Password_Type()
)
password.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    password.setStatus("current")
_Authentication_Type = PPPAuthenticationProtocolValues
_Authentication_Object = MibTableColumn
authentication = _Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 6),
    _Authentication_Type()
)
authentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authentication.setStatus("current")
_ServiceName_Type = OctetString
_ServiceName_Object = MibTableColumn
serviceName = _ServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 7),
    _ServiceName_Type()
)
serviceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serviceName.setStatus("current")
_EncryptionProtocol_Type = PPPEncryptionProtocolValues
_EncryptionProtocol_Object = MibTableColumn
encryptionProtocol = _EncryptionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 8),
    _EncryptionProtocol_Type()
)
encryptionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encryptionProtocol.setStatus("current")
_CompressionProtocol_Type = PPPCompressionProtocolValues
_CompressionProtocol_Object = MibTableColumn
compressionProtocol = _CompressionProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 9),
    _CompressionProtocol_Type()
)
compressionProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    compressionProtocol.setStatus("current")
_IdleDisconnectTime_Type = Unsigned32
_IdleDisconnectTime_Object = MibTableColumn
idleDisconnectTime = _IdleDisconnectTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 10),
    _IdleDisconnectTime_Type()
)
idleDisconnectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleDisconnectTime.setStatus("current")
_HoldOffTime_Type = Unsigned32
_HoldOffTime_Object = MibTableColumn
holdOffTime = _HoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 11),
    _HoldOffTime_Type()
)
holdOffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    holdOffTime.setStatus("current")
_UseStaticIpAddress_Type = TruthValue
_UseStaticIpAddress_Object = MibTableColumn
useStaticIpAddress = _UseStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 12),
    _UseStaticIpAddress_Type()
)
useStaticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    useStaticIpAddress.setStatus("current")
_StaticIpAddress_Type = IpAddress
_StaticIpAddress_Object = MibTableColumn
staticIpAddress = _StaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 13),
    _StaticIpAddress_Type()
)
staticIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticIpAddress.setStatus("current")
_EnableDebug_Type = TruthValue
_EnableDebug_Object = MibTableColumn
enableDebug = _EnableDebug_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 2, 1, 1, 14),
    _EnableDebug_Type()
)
enableDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDebug.setStatus("current")
_PppoeStatusObjects_ObjectIdentity = ObjectIdentity
pppoeStatusObjects = _PppoeStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3)
)
_PppoeStatusTable_Object = MibTable
pppoeStatusTable = _PppoeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pppoeStatusTable.setStatus("current")
_PppoeStatusEntry_Object = MibTableRow
pppoeStatusEntry = _PppoeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3, 1, 1)
)
pppoeStatusEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "ipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    pppoeStatusEntry.setStatus("current")
_ConnectionStatus_Type = WANPppConnectionStatusValues
_ConnectionStatus_Object = MibTableColumn
connectionStatus = _ConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3, 1, 1, 1),
    _ConnectionStatus_Type()
)
connectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionStatus.setStatus("current")
_LastConnectionError_Type = WANPppLastConnectionErrorValues
_LastConnectionError_Object = MibTableColumn
lastConnectionError = _LastConnectionError_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3, 1, 1, 2),
    _LastConnectionError_Type()
)
lastConnectionError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionError.setStatus("current")
_ConnectionEstablishedTime_Type = Unsigned32
_ConnectionEstablishedTime_Object = MibTableColumn
connectionEstablishedTime = _ConnectionEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3, 1, 1, 3),
    _ConnectionEstablishedTime_Type()
)
connectionEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionEstablishedTime.setStatus("current")
_CurrentMTUSize_Type = Unsigned32
_CurrentMTUSize_Object = MibTableColumn
currentMTUSize = _CurrentMTUSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3, 1, 1, 4),
    _CurrentMTUSize_Type()
)
currentMTUSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMTUSize.setStatus("current")
_Uptime_Type = Unsigned32
_Uptime_Object = MibTableColumn
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 2, 3, 1, 1, 5),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("current")
_ZhnDhcpConditionalServingPoolObjects_ObjectIdentity = ObjectIdentity
zhnDhcpConditionalServingPoolObjects = _ZhnDhcpConditionalServingPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3)
)
_ZhnDhcpConditionalServingPoolTable_Object = MibTable
zhnDhcpConditionalServingPoolTable = _ZhnDhcpConditionalServingPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    zhnDhcpConditionalServingPoolTable.setStatus("current")
_ZhnDhcpConditionalServingPoolEntry_Object = MibTableRow
zhnDhcpConditionalServingPoolEntry = _ZhnDhcpConditionalServingPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1)
)
zhnDhcpConditionalServingPoolEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "dhcpPoolIndex"),
)
if mibBuilder.loadTexts:
    zhnDhcpConditionalServingPoolEntry.setStatus("current")
_DhcpPoolIndex_Type = Unsigned32
_DhcpPoolIndex_Object = MibTableColumn
dhcpPoolIndex = _DhcpPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 1),
    _DhcpPoolIndex_Type()
)
dhcpPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpPoolIndex.setStatus("current")
_DhcpPoolEnable_Type = TruthValue
_DhcpPoolEnable_Object = MibTableColumn
dhcpPoolEnable = _DhcpPoolEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 2),
    _DhcpPoolEnable_Type()
)
dhcpPoolEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPoolEnable.setStatus("current")
_DhcpPoolChaddr_Type = MacAddress
_DhcpPoolChaddr_Object = MibTableColumn
dhcpPoolChaddr = _DhcpPoolChaddr_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 3),
    _DhcpPoolChaddr_Type()
)
dhcpPoolChaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolChaddr.setStatus("current")
_DhcpPoolChaddrMask_Type = MacAddress
_DhcpPoolChaddrMask_Object = MibTableColumn
dhcpPoolChaddrMask = _DhcpPoolChaddrMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 4),
    _DhcpPoolChaddrMask_Type()
)
dhcpPoolChaddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolChaddrMask.setStatus("current")
_DhcpPoolMinAddress_Type = IpAddress
_DhcpPoolMinAddress_Object = MibTableColumn
dhcpPoolMinAddress = _DhcpPoolMinAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 5),
    _DhcpPoolMinAddress_Type()
)
dhcpPoolMinAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolMinAddress.setStatus("current")
_DhcpPoolMaxAddress_Type = IpAddress
_DhcpPoolMaxAddress_Object = MibTableColumn
dhcpPoolMaxAddress = _DhcpPoolMaxAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 6),
    _DhcpPoolMaxAddress_Type()
)
dhcpPoolMaxAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolMaxAddress.setStatus("current")
_DhcpPoolReservedAddresses_Type = OctetString
_DhcpPoolReservedAddresses_Object = MibTableColumn
dhcpPoolReservedAddresses = _DhcpPoolReservedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 7),
    _DhcpPoolReservedAddresses_Type()
)
dhcpPoolReservedAddresses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolReservedAddresses.setStatus("current")
_DhcpPoolSubnetMask_Type = IpAddress
_DhcpPoolSubnetMask_Object = MibTableColumn
dhcpPoolSubnetMask = _DhcpPoolSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 8),
    _DhcpPoolSubnetMask_Type()
)
dhcpPoolSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolSubnetMask.setStatus("current")
_DhcpPoolDnsServers_Type = OctetString
_DhcpPoolDnsServers_Object = MibTableColumn
dhcpPoolDnsServers = _DhcpPoolDnsServers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 9),
    _DhcpPoolDnsServers_Type()
)
dhcpPoolDnsServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolDnsServers.setStatus("current")
_DhcpPoolDomainName_Type = OctetString
_DhcpPoolDomainName_Object = MibTableColumn
dhcpPoolDomainName = _DhcpPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 10),
    _DhcpPoolDomainName_Type()
)
dhcpPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolDomainName.setStatus("current")
_DhcpPoolIPRouters_Type = OctetString
_DhcpPoolIPRouters_Object = MibTableColumn
dhcpPoolIPRouters = _DhcpPoolIPRouters_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 11),
    _DhcpPoolIPRouters_Type()
)
dhcpPoolIPRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolIPRouters.setStatus("current")


class _DhcpPoolLeaseTime_Type(Integer32):
    """Custom type dhcpPoolLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_DhcpPoolLeaseTime_Type.__name__ = "Integer32"
_DhcpPoolLeaseTime_Object = MibTableColumn
dhcpPoolLeaseTime = _DhcpPoolLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 12),
    _DhcpPoolLeaseTime_Type()
)
dhcpPoolLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolLeaseTime.setStatus("current")


class _DhcpPoolUseWanVlan_Type(Unsigned32):
    """Custom type dhcpPoolUseWanVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_DhcpPoolUseWanVlan_Type.__name__ = "Unsigned32"
_DhcpPoolUseWanVlan_Object = MibTableColumn
dhcpPoolUseWanVlan = _DhcpPoolUseWanVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 13),
    _DhcpPoolUseWanVlan_Type()
)
dhcpPoolUseWanVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolUseWanVlan.setStatus("current")
_DhcpPoolEnableStaticLease_Type = TruthValue
_DhcpPoolEnableStaticLease_Object = MibTableColumn
dhcpPoolEnableStaticLease = _DhcpPoolEnableStaticLease_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 14),
    _DhcpPoolEnableStaticLease_Type()
)
dhcpPoolEnableStaticLease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolEnableStaticLease.setStatus("current")
_DhcpPoolRowStatus_Type = ZhoneRowStatus
_DhcpPoolRowStatus_Object = MibTableColumn
dhcpPoolRowStatus = _DhcpPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 3, 3, 1, 1, 15),
    _DhcpPoolRowStatus_Type()
)
dhcpPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpPoolRowStatus.setStatus("current")
_ZhnLANEthernetInterfaceObjects_ObjectIdentity = ObjectIdentity
zhnLANEthernetInterfaceObjects = _ZhnLANEthernetInterfaceObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4)
)
_LanEthernetInterfaceConfigTable_Object = MibTable
lanEthernetInterfaceConfigTable = _LanEthernetInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lanEthernetInterfaceConfigTable.setStatus("current")
_LanEthernetInterfaceConfigEntry_Object = MibTableRow
lanEthernetInterfaceConfigEntry = _LanEthernetInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1)
)
lanEthernetInterfaceConfigEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "lanEthernetIndex"),
)
if mibBuilder.loadTexts:
    lanEthernetInterfaceConfigEntry.setStatus("current")
_LanEthernetIndex_Type = Unsigned32
_LanEthernetIndex_Object = MibTableColumn
lanEthernetIndex = _LanEthernetIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 1),
    _LanEthernetIndex_Type()
)
lanEthernetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lanEthernetIndex.setStatus("current")
_LanEthernetEnable_Type = TruthValue
_LanEthernetEnable_Object = MibTableColumn
lanEthernetEnable = _LanEthernetEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 2),
    _LanEthernetEnable_Type()
)
lanEthernetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanEthernetEnable.setStatus("current")
_LanEthernetStatus_Type = LANEthernetStatusValues
_LanEthernetStatus_Object = MibTableColumn
lanEthernetStatus = _LanEthernetStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 3),
    _LanEthernetStatus_Type()
)
lanEthernetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEthernetStatus.setStatus("current")
_MacAddress_Type = OctetString
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 4),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")
_MacAddressControlEnabled_Type = TruthValue
_MacAddressControlEnabled_Object = MibTableColumn
macAddressControlEnabled = _MacAddressControlEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 5),
    _MacAddressControlEnabled_Type()
)
macAddressControlEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddressControlEnabled.setStatus("current")
_MaxBitRate_Type = LANEthernetMaxBitRateValues
_MaxBitRate_Object = MibTableColumn
maxBitRate = _MaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 6),
    _MaxBitRate_Type()
)
maxBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maxBitRate.setStatus("current")
_DuplexMode_Type = LANEthernetDuplexModeValues
_DuplexMode_Object = MibTableColumn
duplexMode = _DuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 7),
    _DuplexMode_Type()
)
duplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    duplexMode.setStatus("current")
_ZhnIfName_Type = OctetString
_ZhnIfName_Object = MibTableColumn
zhnIfName = _ZhnIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 8),
    _ZhnIfName_Type()
)
zhnIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnIfName.setStatus("current")
_ZhnEthernetPriorityMark_Type = Unsigned32
_ZhnEthernetPriorityMark_Object = MibTableColumn
zhnEthernetPriorityMark = _ZhnEthernetPriorityMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 9),
    _ZhnEthernetPriorityMark_Type()
)
zhnEthernetPriorityMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhnEthernetPriorityMark.setStatus("current")
_Dot1qPvid_Type = Unsigned32
_Dot1qPvid_Object = MibTableColumn
dot1qPvid = _Dot1qPvid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 10),
    _Dot1qPvid_Type()
)
dot1qPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPvid.setStatus("current")
_LanEthernetAlias_Type = OctetString
_LanEthernetAlias_Object = MibTableColumn
lanEthernetAlias = _LanEthernetAlias_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 11),
    _LanEthernetAlias_Type()
)
lanEthernetAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEthernetAlias.setStatus("current")
_PauseMode_Type = LANEthernetPauseModeValues
_PauseMode_Object = MibTableColumn
pauseMode = _PauseMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 12),
    _PauseMode_Type()
)
pauseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pauseMode.setStatus("current")
_LanEthernetAcl_Type = LANEthernetAclValues
_LanEthernetAcl_Object = MibTableColumn
lanEthernetAcl = _LanEthernetAcl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 13),
    _LanEthernetAcl_Type()
)
lanEthernetAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanEthernetAcl.setStatus("current")
_LanEthernetAclRulesNumberofEntries_Type = Unsigned32
_LanEthernetAclRulesNumberofEntries_Object = MibTableColumn
lanEthernetAclRulesNumberofEntries = _LanEthernetAclRulesNumberofEntries_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 14),
    _LanEthernetAclRulesNumberofEntries_Type()
)
lanEthernetAclRulesNumberofEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanEthernetAclRulesNumberofEntries.setStatus("current")
_LanEthernetLanFollowsWan_Type = TruthValue
_LanEthernetLanFollowsWan_Object = MibTableColumn
lanEthernetLanFollowsWan = _LanEthernetLanFollowsWan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 15),
    _LanEthernetLanFollowsWan_Type()
)
lanEthernetLanFollowsWan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanEthernetLanFollowsWan.setStatus("current")
_LanEthernetIgmpPriorityMark_Type = Unsigned32
_LanEthernetIgmpPriorityMark_Object = MibTableColumn
lanEthernetIgmpPriorityMark = _LanEthernetIgmpPriorityMark_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 16),
    _LanEthernetIgmpPriorityMark_Type()
)
lanEthernetIgmpPriorityMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanEthernetIgmpPriorityMark.setStatus("current")
_LanEthernetIgmpPvid_Type = Unsigned32
_LanEthernetIgmpPvid_Object = MibTableColumn
lanEthernetIgmpPvid = _LanEthernetIgmpPvid_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 1, 1, 17),
    _LanEthernetIgmpPvid_Type()
)
lanEthernetIgmpPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanEthernetIgmpPvid.setStatus("current")
_LanEthIntfStatisticsTable_Object = MibTable
lanEthIntfStatisticsTable = _LanEthIntfStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2)
)
if mibBuilder.loadTexts:
    lanEthIntfStatisticsTable.setStatus("current")
_LanEthIntfStatisticsEntry_Object = MibTableRow
lanEthIntfStatisticsEntry = _LanEthIntfStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1)
)
lanEthIntfStatisticsEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "lanEthernetIndex"),
)
if mibBuilder.loadTexts:
    lanEthIntfStatisticsEntry.setStatus("current")
_BytesSent_Type = Gauge32
_BytesSent_Object = MibTableColumn
bytesSent = _BytesSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 1),
    _BytesSent_Type()
)
bytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesSent.setStatus("current")
_BytesReceived_Type = Gauge32
_BytesReceived_Object = MibTableColumn
bytesReceived = _BytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 2),
    _BytesReceived_Type()
)
bytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bytesReceived.setStatus("current")
_PacketsSent_Type = Gauge32
_PacketsSent_Object = MibTableColumn
packetsSent = _PacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 3),
    _PacketsSent_Type()
)
packetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsSent.setStatus("current")
_PacketsReceived_Type = Gauge32
_PacketsReceived_Object = MibTableColumn
packetsReceived = _PacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 4),
    _PacketsReceived_Type()
)
packetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    packetsReceived.setStatus("current")
_TxErrors_Type = Gauge32
_TxErrors_Object = MibTableColumn
txErrors = _TxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 5),
    _TxErrors_Type()
)
txErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txErrors.setStatus("current")
_RxErrors_Type = Gauge32
_RxErrors_Object = MibTableColumn
rxErrors = _RxErrors_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 6),
    _RxErrors_Type()
)
rxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxErrors.setStatus("current")
_TxDrops_Type = Gauge32
_TxDrops_Object = MibTableColumn
txDrops = _TxDrops_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 7),
    _TxDrops_Type()
)
txDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txDrops.setStatus("current")
_RxDrops_Type = Gauge32
_RxDrops_Object = MibTableColumn
rxDrops = _RxDrops_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 2, 1, 8),
    _RxDrops_Type()
)
rxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxDrops.setStatus("current")
_LanEthIntfStatusTable_Object = MibTable
lanEthIntfStatusTable = _LanEthIntfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 3)
)
if mibBuilder.loadTexts:
    lanEthIntfStatusTable.setStatus("current")
_LanEthIntfStatusEntry_Object = MibTableRow
lanEthIntfStatusEntry = _LanEthIntfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 3, 1)
)
lanEthIntfStatusEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "lanEthernetIndex"),
)
if mibBuilder.loadTexts:
    lanEthIntfStatusEntry.setStatus("current")
_LinkStatus_Type = LANEthernetStatusValues
_LinkStatus_Object = MibTableColumn
linkStatus = _LinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 3, 1, 1),
    _LinkStatus_Type()
)
linkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linkStatus.setStatus("current")
_RateStatus_Type = LANEthernetMaxBitRateValues
_RateStatus_Object = MibTableColumn
rateStatus = _RateStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 3, 1, 2),
    _RateStatus_Type()
)
rateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rateStatus.setStatus("current")
_DuplexStatus_Type = LANEthernetDuplexModeValues
_DuplexStatus_Object = MibTableColumn
duplexStatus = _DuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 3, 1, 3),
    _DuplexStatus_Type()
)
duplexStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    duplexStatus.setStatus("current")
_PauseStatus_Type = LANEthernetPauseModeValues
_PauseStatus_Object = MibTableColumn
pauseStatus = _PauseStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 3, 1, 4),
    _PauseStatus_Type()
)
pauseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pauseStatus.setStatus("current")
_LanEthIntfRateLimitTable_Object = MibTable
lanEthIntfRateLimitTable = _LanEthIntfRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lanEthIntfRateLimitTable.setStatus("current")
_LanEthIntfRateLimitEntry_Object = MibTableRow
lanEthIntfRateLimitEntry = _LanEthIntfRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 4, 1)
)
lanEthIntfRateLimitEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "lanEthernetIndex"),
)
if mibBuilder.loadTexts:
    lanEthIntfRateLimitEntry.setStatus("current")
_RateLimitEnable_Type = TruthValue
_RateLimitEnable_Object = MibTableColumn
rateLimitEnable = _RateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 4, 1, 1),
    _RateLimitEnable_Type()
)
rateLimitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitEnable.setStatus("current")
_PeakRate_Type = Unsigned32
_PeakRate_Object = MibTableColumn
peakRate = _PeakRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 4, 1, 2),
    _PeakRate_Type()
)
peakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    peakRate.setStatus("current")
_BurstSize_Type = LANRateLimitBurstSizeValues
_BurstSize_Object = MibTableColumn
burstSize = _BurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 4, 1, 3),
    _BurstSize_Type()
)
burstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    burstSize.setStatus("current")
_RateDirection_Type = LANRateLimitDirectionValues
_RateDirection_Object = MibTableColumn
rateDirection = _RateDirection_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 4, 1, 4),
    _RateDirection_Type()
)
rateDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateDirection.setStatus("current")
_InboundPeakRate_Type = Unsigned32
_InboundPeakRate_Object = MibTableColumn
inboundPeakRate = _InboundPeakRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 4, 4, 1, 5),
    _InboundPeakRate_Type()
)
inboundPeakRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inboundPeakRate.setStatus("current")
_IgmpGroupsTable_Object = MibTable
igmpGroupsTable = _IgmpGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5)
)
if mibBuilder.loadTexts:
    igmpGroupsTable.setStatus("current")
_IgmpGroupsEntry_Object = MibTableRow
igmpGroupsEntry = _IgmpGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1)
)
igmpGroupsEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "igmpGroupIndex"),
)
if mibBuilder.loadTexts:
    igmpGroupsEntry.setStatus("current")
_IgmpGroupIndex_Type = Unsigned32
_IgmpGroupIndex_Object = MibTableColumn
igmpGroupIndex = _IgmpGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 1),
    _IgmpGroupIndex_Type()
)
igmpGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpGroupIndex.setStatus("current")
_IgmpGroupAddress_Type = IpAddress
_IgmpGroupAddress_Object = MibTableColumn
igmpGroupAddress = _IgmpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 2),
    _IgmpGroupAddress_Type()
)
igmpGroupAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupAddress.setStatus("current")
_IgmpGroupReporterIP_Type = IpAddress
_IgmpGroupReporterIP_Object = MibTableColumn
igmpGroupReporterIP = _IgmpGroupReporterIP_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 3),
    _IgmpGroupReporterIP_Type()
)
igmpGroupReporterIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupReporterIP.setStatus("current")
_IgmpGroupReporterMAC_Type = OctetString
_IgmpGroupReporterMAC_Object = MibTableColumn
igmpGroupReporterMAC = _IgmpGroupReporterMAC_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 4),
    _IgmpGroupReporterMAC_Type()
)
igmpGroupReporterMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupReporterMAC.setStatus("current")
_IgmpGroupInterface_Type = OctetString
_IgmpGroupInterface_Object = MibTableColumn
igmpGroupInterface = _IgmpGroupInterface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 5),
    _IgmpGroupInterface_Type()
)
igmpGroupInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupInterface.setStatus("current")
_IgmpGroupVlan_Type = OctetString
_IgmpGroupVlan_Object = MibTableColumn
igmpGroupVlan = _IgmpGroupVlan_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 6),
    _IgmpGroupVlan_Type()
)
igmpGroupVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupVlan.setStatus("current")
_IgmpGroupExpiration_Type = Unsigned32
_IgmpGroupExpiration_Object = MibTableColumn
igmpGroupExpiration = _IgmpGroupExpiration_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 7),
    _IgmpGroupExpiration_Type()
)
igmpGroupExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupExpiration.setStatus("current")
_IgmpGroupQuerier_Type = IpAddress
_IgmpGroupQuerier_Object = MibTableColumn
igmpGroupQuerier = _IgmpGroupQuerier_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 5, 1, 8),
    _IgmpGroupQuerier_Type()
)
igmpGroupQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGroupQuerier.setStatus("current")
_ZhnLANDeviceSystemObjects_ObjectIdentity = ObjectIdentity
zhnLANDeviceSystemObjects = _ZhnLANDeviceSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 6)
)
_LanDefaultIfName_Type = OctetString
_LanDefaultIfName_Object = MibScalar
lanDefaultIfName = _LanDefaultIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 6, 1),
    _LanDefaultIfName_Type()
)
lanDefaultIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanDefaultIfName.setStatus("current")
_LanDefaultIfIpAddress_Type = IpAddress
_LanDefaultIfIpAddress_Object = MibScalar
lanDefaultIfIpAddress = _LanDefaultIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 6, 2),
    _LanDefaultIfIpAddress_Type()
)
lanDefaultIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanDefaultIfIpAddress.setStatus("current")
_LanEthAclRulesTable_Object = MibTable
lanEthAclRulesTable = _LanEthAclRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7)
)
if mibBuilder.loadTexts:
    lanEthAclRulesTable.setStatus("current")
_LanEthAclRulesEntry_Object = MibTableRow
lanEthAclRulesEntry = _LanEthAclRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1)
)
lanEthAclRulesEntry.setIndexNames(
    (0, "ZHNLANDEVICE", "lanDeviceIndex"),
    (0, "ZHNLANDEVICE", "lanEthernetIndex"),
    (0, "ZHNLANDEVICE", "lanAclRuleKey"),
)
if mibBuilder.loadTexts:
    lanEthAclRulesEntry.setStatus("current")
_LanAclRuleKey_Type = Unsigned32
_LanAclRuleKey_Object = MibTableColumn
lanAclRuleKey = _LanAclRuleKey_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 1),
    _LanAclRuleKey_Type()
)
lanAclRuleKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lanAclRuleKey.setStatus("current")
_LanAclRuleIfName_Type = OctetString
_LanAclRuleIfName_Object = MibTableColumn
lanAclRuleIfName = _LanAclRuleIfName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 2),
    _LanAclRuleIfName_Type()
)
lanAclRuleIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanAclRuleIfName.setStatus("current")
_LanAclRuleName_Type = OctetString
_LanAclRuleName_Object = MibTableColumn
lanAclRuleName = _LanAclRuleName_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 3),
    _LanAclRuleName_Type()
)
lanAclRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanAclRuleName.setStatus("current")
_LanAclRuleSourceIPAddress_Type = OctetString
_LanAclRuleSourceIPAddress_Object = MibTableColumn
lanAclRuleSourceIPAddress = _LanAclRuleSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 4),
    _LanAclRuleSourceIPAddress_Type()
)
lanAclRuleSourceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanAclRuleSourceIPAddress.setStatus("current")
_LanAclRuleIPProtocol_Type = LANEthernetIpProtocolValues
_LanAclRuleIPProtocol_Object = MibTableColumn
lanAclRuleIPProtocol = _LanAclRuleIPProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 5),
    _LanAclRuleIPProtocol_Type()
)
lanAclRuleIPProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanAclRuleIPProtocol.setStatus("current")
_LanAclRuleSourceMACAddress_Type = OctetString
_LanAclRuleSourceMACAddress_Object = MibTableColumn
lanAclRuleSourceMACAddress = _LanAclRuleSourceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 6),
    _LanAclRuleSourceMACAddress_Type()
)
lanAclRuleSourceMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanAclRuleSourceMACAddress.setStatus("current")
_LanAclRuleSourceMACMask_Type = OctetString
_LanAclRuleSourceMACMask_Object = MibTableColumn
lanAclRuleSourceMACMask = _LanAclRuleSourceMACMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 7),
    _LanAclRuleSourceMACMask_Type()
)
lanAclRuleSourceMACMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanAclRuleSourceMACMask.setStatus("current")
_LanAclRuleRowStatus_Type = ZhoneRowStatus
_LanAclRuleRowStatus_Object = MibTableColumn
lanAclRuleRowStatus = _LanAclRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 1, 7, 1, 8),
    _LanAclRuleRowStatus_Type()
)
lanAclRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lanAclRuleRowStatus.setStatus("current")
_ZhnLANDeviceConformance_ObjectIdentity = ObjectIdentity
zhnLANDeviceConformance = _ZhnLANDeviceConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2)
)
_ZhnLANDeviceGroups_ObjectIdentity = ObjectIdentity
zhnLANDeviceGroups = _ZhnLANDeviceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1)
)
_ZhnLANDeviceCompliances_ObjectIdentity = ObjectIdentity
zhnLANDeviceCompliances = _ZhnLANDeviceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 2)
)

# Managed Objects groups

zhnLANDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 1)
)
zhnLANDeviceGroup.setObjects(
      *(("ZHNLANDEVICE", "lanEthernetInterfaceNumberOfEntries"),
        ("ZHNLANDEVICE", "lanUSBInterfaceNumberOfEntries"),
        ("ZHNLANDEVICE", "lanWLANConfigurationNumberOfEntries"),
        ("ZHNLANDEVICE", "lanMocaInterfaceNumberOfEntries"))
)
if mibBuilder.loadTexts:
    zhnLANDeviceGroup.setStatus("current")

zhnLANIgmpSnoopingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 2)
)
zhnLANIgmpSnoopingGroup.setObjects(
      *(("ZHNLANDEVICE", "igmpEnable"),
        ("ZHNLANDEVICE", "igmpMode"),
        ("ZHNLANDEVICE", "igmpIfName"))
)
if mibBuilder.loadTexts:
    zhnLANIgmpSnoopingGroup.setStatus("current")

zhnLANHostConfigManagementGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 3)
)
zhnLANHostConfigManagementGroup.setObjects(
      *(("ZHNLANDEVICE", "dhcpServerConfigurable"),
        ("ZHNLANDEVICE", "zhnDhcpServerEnable"),
        ("ZHNLANDEVICE", "dhcpRelay"),
        ("ZHNLANDEVICE", "dhcpRelayServer"),
        ("ZHNLANDEVICE", "minAddress"),
        ("ZHNLANDEVICE", "maxAddress"),
        ("ZHNLANDEVICE", "reservedAddresses"),
        ("ZHNLANDEVICE", "subnetMask"),
        ("ZHNLANDEVICE", "dnsServers"),
        ("ZHNLANDEVICE", "domainName"),
        ("ZHNLANDEVICE", "ipRouters"),
        ("ZHNLANDEVICE", "dhcpLeaseTime"),
        ("ZHNLANDEVICE", "ipInterfaceNumberOfEntries"))
)
if mibBuilder.loadTexts:
    zhnLANHostConfigManagementGroup.setStatus("current")

zhnIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 4)
)
zhnIpInterfaceGroup.setObjects(
      *(("ZHNLANDEVICE", "ipInterfaceEnable"),
        ("ZHNLANDEVICE", "ipInterfaceIPAddress"),
        ("ZHNLANDEVICE", "ipInterfaceSubnetMask"),
        ("ZHNLANDEVICE", "ipInterfaceAddressingType"),
        ("ZHNLANDEVICE", "ipInterfaceifName"),
        ("ZHNLANDEVICE", "firewallEnabled"),
        ("ZHNLANDEVICE", "defaultGateway"),
        ("ZHNLANDEVICE", "natEnabled"),
        ("ZHNLANDEVICE", "dhcpcPid"),
        ("ZHNLANDEVICE", "dnsType"),
        ("ZHNLANDEVICE", "primaryDnsIPAddress"),
        ("ZHNLANDEVICE", "secondaryDnsIPAddress"),
        ("ZHNLANDEVICE", "zhnVlanType"),
        ("ZHNLANDEVICE", "connectionType"),
        ("ZHNLANDEVICE", "maxMTUSize"),
        ("ZHNLANDEVICE", "alternateWanIfName"),
        ("ZHNLANDEVICE", "natEnabled"))
)
if mibBuilder.loadTexts:
    zhnIpInterfaceGroup.setStatus("current")

zhnPPPoEConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 5)
)
zhnPPPoEConfigGroup.setObjects(
      *(("ZHNLANDEVICE", "pppoeIfName"),
        ("ZHNLANDEVICE", "pid"),
        ("ZHNLANDEVICE", "connectionRequest"),
        ("ZHNLANDEVICE", "username"),
        ("ZHNLANDEVICE", "password"),
        ("ZHNLANDEVICE", "authentication"),
        ("ZHNLANDEVICE", "serviceName"),
        ("ZHNLANDEVICE", "encryptionProtocol"),
        ("ZHNLANDEVICE", "compressionProtocol"),
        ("ZHNLANDEVICE", "idleDisconnectTime"),
        ("ZHNLANDEVICE", "holdOffTime"),
        ("ZHNLANDEVICE", "useStaticIpAddress"),
        ("ZHNLANDEVICE", "staticIpAddress"),
        ("ZHNLANDEVICE", "enableDebug"))
)
if mibBuilder.loadTexts:
    zhnPPPoEConfigGroup.setStatus("current")

zhnPPPoEStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 6)
)
zhnPPPoEStatusGroup.setObjects(
      *(("ZHNLANDEVICE", "connectionStatus"),
        ("ZHNLANDEVICE", "lastConnectionError"),
        ("ZHNLANDEVICE", "connectionEstablishedTime"),
        ("ZHNLANDEVICE", "currentMTUSize"),
        ("ZHNLANDEVICE", "uptime"))
)
if mibBuilder.loadTexts:
    zhnPPPoEStatusGroup.setStatus("current")

zhnLANEthernetInterfaceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 7)
)
zhnLANEthernetInterfaceConfigGroup.setObjects(
      *(("ZHNLANDEVICE", "lanEthernetEnable"),
        ("ZHNLANDEVICE", "lanEthernetStatus"),
        ("ZHNLANDEVICE", "macAddress"),
        ("ZHNLANDEVICE", "macAddressControlEnabled"),
        ("ZHNLANDEVICE", "maxBitRate"),
        ("ZHNLANDEVICE", "duplexMode"),
        ("ZHNLANDEVICE", "zhnIfName"),
        ("ZHNLANDEVICE", "zhnEthernetPriorityMark"),
        ("ZHNLANDEVICE", "dot1qPvid"),
        ("ZHNLANDEVICE", "lanEthernetAlias"),
        ("ZHNLANDEVICE", "pauseMode"),
        ("ZHNLANDEVICE", "lanEthernetAcl"),
        ("ZHNLANDEVICE", "lanEthernetAclRulesNumberofEntries"),
        ("ZHNLANDEVICE", "lanEthernetLanFollowsWan"),
        ("ZHNLANDEVICE", "lanEthernetIgmpPriorityMark"),
        ("ZHNLANDEVICE", "lanEthernetIgmpPvid"))
)
if mibBuilder.loadTexts:
    zhnLANEthernetInterfaceConfigGroup.setStatus("current")

zhnLANEthIntfStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 8)
)
zhnLANEthIntfStatisticsGroup.setObjects(
      *(("ZHNLANDEVICE", "bytesSent"),
        ("ZHNLANDEVICE", "bytesReceived"),
        ("ZHNLANDEVICE", "packetsSent"),
        ("ZHNLANDEVICE", "packetsReceived"),
        ("ZHNLANDEVICE", "txErrors"),
        ("ZHNLANDEVICE", "rxErrors"),
        ("ZHNLANDEVICE", "txDrops"),
        ("ZHNLANDEVICE", "rxDrops"))
)
if mibBuilder.loadTexts:
    zhnLANEthIntfStatisticsGroup.setStatus("current")

zhnLANEthIntfStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 9)
)
zhnLANEthIntfStatusGroup.setObjects(
      *(("ZHNLANDEVICE", "linkStatus"),
        ("ZHNLANDEVICE", "rateStatus"),
        ("ZHNLANDEVICE", "duplexStatus"),
        ("ZHNLANDEVICE", "pauseStatus"))
)
if mibBuilder.loadTexts:
    zhnLANEthIntfStatusGroup.setStatus("current")

zhnLANEthIntfRateLimitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 10)
)
zhnLANEthIntfRateLimitGroup.setObjects(
      *(("ZHNLANDEVICE", "rateLimitEnable"),
        ("ZHNLANDEVICE", "peakRate"),
        ("ZHNLANDEVICE", "burstSize"),
        ("ZHNLANDEVICE", "rateDirection"),
        ("ZHNLANDEVICE", "inboundPeakRate"))
)
if mibBuilder.loadTexts:
    zhnLANEthIntfRateLimitGroup.setStatus("current")

zhnLANIGMPMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 11)
)
zhnLANIGMPMulticastGroup.setObjects(
      *(("ZHNLANDEVICE", "igmpGroupAddress"),
        ("ZHNLANDEVICE", "igmpGroupReporterIP"),
        ("ZHNLANDEVICE", "igmpGroupReporterMAC"),
        ("ZHNLANDEVICE", "igmpGroupInterface"),
        ("ZHNLANDEVICE", "igmpGroupVlan"),
        ("ZHNLANDEVICE", "igmpGroupExpiration"),
        ("ZHNLANDEVICE", "igmpGroupQuerier"))
)
if mibBuilder.loadTexts:
    zhnLANIGMPMulticastGroup.setStatus("current")

zhnLANSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 12)
)
zhnLANSystemGroup.setObjects(
      *(("ZHNLANDEVICE", "lanDefaultIfName"),
        ("ZHNLANDEVICE", "lanDefaultIfIpAddress"))
)
if mibBuilder.loadTexts:
    zhnLANSystemGroup.setStatus("current")

zhnLANAclRulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 13)
)
zhnLANAclRulesGroup.setObjects(
      *(("ZHNLANDEVICE", "lanAclRuleIfName"),
        ("ZHNLANDEVICE", "lanAclRuleName"),
        ("ZHNLANDEVICE", "lanAclRuleSourceIPAddress"),
        ("ZHNLANDEVICE", "lanAclRuleIPProtocol"),
        ("ZHNLANDEVICE", "lanAclRuleSourceMACAddress"),
        ("ZHNLANDEVICE", "lanAclRuleSourceMACMask"),
        ("ZHNLANDEVICE", "lanAclRuleRowStatus"))
)
if mibBuilder.loadTexts:
    zhnLANAclRulesGroup.setStatus("current")

zhnDhcpConditionalServingPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 1, 14)
)
zhnDhcpConditionalServingPoolGroup.setObjects(
      *(("ZHNLANDEVICE", "dhcpPoolIndex"),
        ("ZHNLANDEVICE", "dhcpPoolEnable"),
        ("ZHNLANDEVICE", "dhcpPoolChaddr"),
        ("ZHNLANDEVICE", "dhcpPoolChaddrMask"),
        ("ZHNLANDEVICE", "dhcpPoolMinAddress"),
        ("ZHNLANDEVICE", "dhcpPoolMaxAddress"),
        ("ZHNLANDEVICE", "dhcpPoolReservedAddresses"),
        ("ZHNLANDEVICE", "dhcpPoolSubnetMask"),
        ("ZHNLANDEVICE", "dhcpPoolDnsServers"),
        ("ZHNLANDEVICE", "dhcpPoolDomainName"),
        ("ZHNLANDEVICE", "dhcpPoolIPRouters"),
        ("ZHNLANDEVICE", "dhcpPoolLeaseTime"),
        ("ZHNLANDEVICE", "dhcpPoolUseWanVlan"),
        ("ZHNLANDEVICE", "dhcpPoolEnableStaticLease"))
)
if mibBuilder.loadTexts:
    zhnDhcpConditionalServingPoolGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnLANDeviceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 41, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnLANDeviceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNLANDEVICE",
    **{"LANEthernetStatusValues": LANEthernetStatusValues,
       "LANEthernetMaxBitRateValues": LANEthernetMaxBitRateValues,
       "LANEthernetDuplexModeValues": LANEthernetDuplexModeValues,
       "LANEthernetPauseModeValues": LANEthernetPauseModeValues,
       "IPInterfaceAddressingTypeValues": IPInterfaceAddressingTypeValues,
       "IGMPSnoopingModeValues": IGMPSnoopingModeValues,
       "DNSTypeValues": DNSTypeValues,
       "IpPppoeConnectionTypeValues": IpPppoeConnectionTypeValues,
       "PPPUserConnectionRequestValues": PPPUserConnectionRequestValues,
       "PPPAuthenticationProtocolValues": PPPAuthenticationProtocolValues,
       "PPPEncryptionProtocolValues": PPPEncryptionProtocolValues,
       "PPPCompressionProtocolValues": PPPCompressionProtocolValues,
       "WANPppConnectionStatusValues": WANPppConnectionStatusValues,
       "WANPppLastConnectionErrorValues": WANPppLastConnectionErrorValues,
       "LANRateLimitBurstSizeValues": LANRateLimitBurstSizeValues,
       "LANRateLimitDirectionValues": LANRateLimitDirectionValues,
       "LANEthernetAclValues": LANEthernetAclValues,
       "LANEthernetIpProtocolValues": LANEthernetIpProtocolValues,
       "zhnLANDevice": zhnLANDevice,
       "zhnLANDeviceObjects": zhnLANDeviceObjects,
       "lanDeviceTable": lanDeviceTable,
       "lanDeviceEntry": lanDeviceEntry,
       "lanDeviceIndex": lanDeviceIndex,
       "lanEthernetInterfaceNumberOfEntries": lanEthernetInterfaceNumberOfEntries,
       "lanUSBInterfaceNumberOfEntries": lanUSBInterfaceNumberOfEntries,
       "lanWLANConfigurationNumberOfEntries": lanWLANConfigurationNumberOfEntries,
       "lanMocaInterfaceNumberOfEntries": lanMocaInterfaceNumberOfEntries,
       "igmpSnoopingCfgTable": igmpSnoopingCfgTable,
       "igmpSnoopingCfgEntry": igmpSnoopingCfgEntry,
       "igmpEnable": igmpEnable,
       "igmpMode": igmpMode,
       "igmpIfName": igmpIfName,
       "lanHostConfigManagementObjects": lanHostConfigManagementObjects,
       "lanHostConfigManagementTable": lanHostConfigManagementTable,
       "lanHostConfigManagementEntry": lanHostConfigManagementEntry,
       "dhcpServerConfigurable": dhcpServerConfigurable,
       "zhnDhcpServerEnable": zhnDhcpServerEnable,
       "dhcpRelay": dhcpRelay,
       "dhcpRelayServer": dhcpRelayServer,
       "minAddress": minAddress,
       "maxAddress": maxAddress,
       "reservedAddresses": reservedAddresses,
       "subnetMask": subnetMask,
       "dnsServers": dnsServers,
       "domainName": domainName,
       "ipRouters": ipRouters,
       "dhcpLeaseTime": dhcpLeaseTime,
       "ipInterfaceNumberOfEntries": ipInterfaceNumberOfEntries,
       "ipInterfaceObjects": ipInterfaceObjects,
       "zhnIpInterfaceTable": zhnIpInterfaceTable,
       "zhnIpInterfaceEntry": zhnIpInterfaceEntry,
       "ipInterfaceIndex": ipInterfaceIndex,
       "ipInterfaceEnable": ipInterfaceEnable,
       "ipInterfaceIPAddress": ipInterfaceIPAddress,
       "ipInterfaceSubnetMask": ipInterfaceSubnetMask,
       "ipInterfaceAddressingType": ipInterfaceAddressingType,
       "ipInterfaceifName": ipInterfaceifName,
       "firewallEnabled": firewallEnabled,
       "defaultGateway": defaultGateway,
       "natEnabled": natEnabled,
       "dhcpcPid": dhcpcPid,
       "dnsType": dnsType,
       "primaryDnsIPAddress": primaryDnsIPAddress,
       "secondaryDnsIPAddress": secondaryDnsIPAddress,
       "zhnVlanType": zhnVlanType,
       "connectionType": connectionType,
       "maxMTUSize": maxMTUSize,
       "alternateWanIfName": alternateWanIfName,
       "naptEnabled": naptEnabled,
       "pppoeConfigObjects": pppoeConfigObjects,
       "pppoeConfigTable": pppoeConfigTable,
       "pppoeConfigEntry": pppoeConfigEntry,
       "pppoeIfName": pppoeIfName,
       "pid": pid,
       "connectionRequest": connectionRequest,
       "username": username,
       "password": password,
       "authentication": authentication,
       "serviceName": serviceName,
       "encryptionProtocol": encryptionProtocol,
       "compressionProtocol": compressionProtocol,
       "idleDisconnectTime": idleDisconnectTime,
       "holdOffTime": holdOffTime,
       "useStaticIpAddress": useStaticIpAddress,
       "staticIpAddress": staticIpAddress,
       "enableDebug": enableDebug,
       "pppoeStatusObjects": pppoeStatusObjects,
       "pppoeStatusTable": pppoeStatusTable,
       "pppoeStatusEntry": pppoeStatusEntry,
       "connectionStatus": connectionStatus,
       "lastConnectionError": lastConnectionError,
       "connectionEstablishedTime": connectionEstablishedTime,
       "currentMTUSize": currentMTUSize,
       "uptime": uptime,
       "zhnDhcpConditionalServingPoolObjects": zhnDhcpConditionalServingPoolObjects,
       "zhnDhcpConditionalServingPoolTable": zhnDhcpConditionalServingPoolTable,
       "zhnDhcpConditionalServingPoolEntry": zhnDhcpConditionalServingPoolEntry,
       "dhcpPoolIndex": dhcpPoolIndex,
       "dhcpPoolEnable": dhcpPoolEnable,
       "dhcpPoolChaddr": dhcpPoolChaddr,
       "dhcpPoolChaddrMask": dhcpPoolChaddrMask,
       "dhcpPoolMinAddress": dhcpPoolMinAddress,
       "dhcpPoolMaxAddress": dhcpPoolMaxAddress,
       "dhcpPoolReservedAddresses": dhcpPoolReservedAddresses,
       "dhcpPoolSubnetMask": dhcpPoolSubnetMask,
       "dhcpPoolDnsServers": dhcpPoolDnsServers,
       "dhcpPoolDomainName": dhcpPoolDomainName,
       "dhcpPoolIPRouters": dhcpPoolIPRouters,
       "dhcpPoolLeaseTime": dhcpPoolLeaseTime,
       "dhcpPoolUseWanVlan": dhcpPoolUseWanVlan,
       "dhcpPoolEnableStaticLease": dhcpPoolEnableStaticLease,
       "dhcpPoolRowStatus": dhcpPoolRowStatus,
       "zhnLANEthernetInterfaceObjects": zhnLANEthernetInterfaceObjects,
       "lanEthernetInterfaceConfigTable": lanEthernetInterfaceConfigTable,
       "lanEthernetInterfaceConfigEntry": lanEthernetInterfaceConfigEntry,
       "lanEthernetIndex": lanEthernetIndex,
       "lanEthernetEnable": lanEthernetEnable,
       "lanEthernetStatus": lanEthernetStatus,
       "macAddress": macAddress,
       "macAddressControlEnabled": macAddressControlEnabled,
       "maxBitRate": maxBitRate,
       "duplexMode": duplexMode,
       "zhnIfName": zhnIfName,
       "zhnEthernetPriorityMark": zhnEthernetPriorityMark,
       "dot1qPvid": dot1qPvid,
       "lanEthernetAlias": lanEthernetAlias,
       "pauseMode": pauseMode,
       "lanEthernetAcl": lanEthernetAcl,
       "lanEthernetAclRulesNumberofEntries": lanEthernetAclRulesNumberofEntries,
       "lanEthernetLanFollowsWan": lanEthernetLanFollowsWan,
       "lanEthernetIgmpPriorityMark": lanEthernetIgmpPriorityMark,
       "lanEthernetIgmpPvid": lanEthernetIgmpPvid,
       "lanEthIntfStatisticsTable": lanEthIntfStatisticsTable,
       "lanEthIntfStatisticsEntry": lanEthIntfStatisticsEntry,
       "bytesSent": bytesSent,
       "bytesReceived": bytesReceived,
       "packetsSent": packetsSent,
       "packetsReceived": packetsReceived,
       "txErrors": txErrors,
       "rxErrors": rxErrors,
       "txDrops": txDrops,
       "rxDrops": rxDrops,
       "lanEthIntfStatusTable": lanEthIntfStatusTable,
       "lanEthIntfStatusEntry": lanEthIntfStatusEntry,
       "linkStatus": linkStatus,
       "rateStatus": rateStatus,
       "duplexStatus": duplexStatus,
       "pauseStatus": pauseStatus,
       "lanEthIntfRateLimitTable": lanEthIntfRateLimitTable,
       "lanEthIntfRateLimitEntry": lanEthIntfRateLimitEntry,
       "rateLimitEnable": rateLimitEnable,
       "peakRate": peakRate,
       "burstSize": burstSize,
       "rateDirection": rateDirection,
       "inboundPeakRate": inboundPeakRate,
       "igmpGroupsTable": igmpGroupsTable,
       "igmpGroupsEntry": igmpGroupsEntry,
       "igmpGroupIndex": igmpGroupIndex,
       "igmpGroupAddress": igmpGroupAddress,
       "igmpGroupReporterIP": igmpGroupReporterIP,
       "igmpGroupReporterMAC": igmpGroupReporterMAC,
       "igmpGroupInterface": igmpGroupInterface,
       "igmpGroupVlan": igmpGroupVlan,
       "igmpGroupExpiration": igmpGroupExpiration,
       "igmpGroupQuerier": igmpGroupQuerier,
       "zhnLANDeviceSystemObjects": zhnLANDeviceSystemObjects,
       "lanDefaultIfName": lanDefaultIfName,
       "lanDefaultIfIpAddress": lanDefaultIfIpAddress,
       "lanEthAclRulesTable": lanEthAclRulesTable,
       "lanEthAclRulesEntry": lanEthAclRulesEntry,
       "lanAclRuleKey": lanAclRuleKey,
       "lanAclRuleIfName": lanAclRuleIfName,
       "lanAclRuleName": lanAclRuleName,
       "lanAclRuleSourceIPAddress": lanAclRuleSourceIPAddress,
       "lanAclRuleIPProtocol": lanAclRuleIPProtocol,
       "lanAclRuleSourceMACAddress": lanAclRuleSourceMACAddress,
       "lanAclRuleSourceMACMask": lanAclRuleSourceMACMask,
       "lanAclRuleRowStatus": lanAclRuleRowStatus,
       "zhnLANDeviceConformance": zhnLANDeviceConformance,
       "zhnLANDeviceGroups": zhnLANDeviceGroups,
       "zhnLANDeviceGroup": zhnLANDeviceGroup,
       "zhnLANIgmpSnoopingGroup": zhnLANIgmpSnoopingGroup,
       "zhnLANHostConfigManagementGroup": zhnLANHostConfigManagementGroup,
       "zhnIpInterfaceGroup": zhnIpInterfaceGroup,
       "zhnPPPoEConfigGroup": zhnPPPoEConfigGroup,
       "zhnPPPoEStatusGroup": zhnPPPoEStatusGroup,
       "zhnLANEthernetInterfaceConfigGroup": zhnLANEthernetInterfaceConfigGroup,
       "zhnLANEthIntfStatisticsGroup": zhnLANEthIntfStatisticsGroup,
       "zhnLANEthIntfStatusGroup": zhnLANEthIntfStatusGroup,
       "zhnLANEthIntfRateLimitGroup": zhnLANEthIntfRateLimitGroup,
       "zhnLANIGMPMulticastGroup": zhnLANIGMPMulticastGroup,
       "zhnLANSystemGroup": zhnLANSystemGroup,
       "zhnLANAclRulesGroup": zhnLANAclRulesGroup,
       "zhnDhcpConditionalServingPoolGroup": zhnDhcpConditionalServingPoolGroup,
       "zhnLANDeviceCompliances": zhnLANDeviceCompliances,
       "zhnLANDeviceCompliance": zhnLANDeviceCompliance}
)
