# SNMP MIB module (ALCATEL-IND1-TIMETRA-VRTR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-TIMETRA-VRTR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:13 2024
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

(TmnxSlotNum,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-CHASSIS-MIB",
    "TmnxSlotNum")

(TFilterID,
 TIPFilterID) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-FILTER-MIB",
    "TFilterID",
    "TIPFilterID")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(tmnxPortNotifyPortId,
 tmnxPortType) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-PORT-MIB",
    "tmnxPortNotifyPortId",
    "tmnxPortType")

(TNetworkPolicyID,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-QOS-MIB",
    "TNetworkPolicyID")

(sapEncapValue,
 sapPortId) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-SAP-MIB",
    "sapEncapValue",
    "sapPortId")

(svcDhcpClientLease,
 svcDhcpLseStateNewChAddr,
 svcDhcpLseStateNewCiAddr) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-SERV-MIB",
    "svcDhcpClientLease",
    "svcDhcpLseStateNewChAddr",
    "svcDhcpLseStateNewCiAddr")

(Dot1PPriority,
 IpAddressPrefixLength,
 TCpmProtPolicyID,
 TDSCPValue,
 TDSCPValueOrNone,
 TFCType,
 TItemDescription,
 TItemLongDescription,
 TNamedItem,
 TNamedItemOrEmpty,
 TPolicyStatementNameOrEmpty,
 TmnxAdminState,
 TmnxBgpAutonomousSystem,
 TmnxCustId,
 TmnxDHCP6MsgType,
 TmnxEncapVal,
 TmnxOperState,
 TmnxPortID,
 TmnxServId,
 TmnxStatus,
 TmnxTunnelID,
 TmnxTunnelType,
 TmnxVPNRouteDistinguisher,
 TmnxVRtrID,
 TmnxVRtrIDOrZero) = mibBuilder.importSymbols(
    "ALCATEL-IND1-TIMETRA-TC-MIB",
    "Dot1PPriority",
    "IpAddressPrefixLength",
    "TCpmProtPolicyID",
    "TDSCPValue",
    "TDSCPValueOrNone",
    "TFCType",
    "TItemDescription",
    "TItemLongDescription",
    "TNamedItem",
    "TNamedItemOrEmpty",
    "TPolicyStatementNameOrEmpty",
    "TmnxAdminState",
    "TmnxBgpAutonomousSystem",
    "TmnxCustId",
    "TmnxDHCP6MsgType",
    "TmnxEncapVal",
    "TmnxOperState",
    "TmnxPortID",
    "TmnxServId",
    "TmnxStatus",
    "TmnxTunnelID",
    "TmnxTunnelType",
    "TmnxVPNRouteDistinguisher",
    "TmnxVRtrID",
    "TmnxVRtrIDOrZero")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressIPv6,
 InetAddressIPv6z,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressIPv6z",
    "InetAddressPrefixLength",
    "InetAddressType")

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

(ipNetToMediaEntry,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaEntry")

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
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

timetraVRtrMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 3)
)
timetraVRtrMIBModule.setRevisions(
        ("1908-01-01 00:00",
         "1907-01-01 00:00",
         "1906-02-28 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1900-08-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxVPNId(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )



class TmnxInetAddrState(Integer32, TextualConvention):
    status = "current"
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
        *(("deprecated", 4),
          ("duplicated", 2),
          ("inaccessible", 3),
          ("preferred", 5),
          ("tentative", 1),
          ("unknown", 0))
    )



class TDSCPAppId(Integer32, TextualConvention):
    status = "current"
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 1),
          ("cflowd", 2),
          ("dhcp", 3),
          ("dns", 4),
          ("ftp", 5),
          ("icmp", 6),
          ("igmp", 7),
          ("ldp", 8),
          ("mld", 9),
          ("msdp", 10),
          ("ndis", 11),
          ("ntp", 12),
          ("ospf", 13),
          ("pim", 14),
          ("radius", 15),
          ("rip", 16),
          ("rsvp", 17),
          ("snmp", 18),
          ("snmp-notification", 19),
          ("srrp", 20),
          ("ssh", 21),
          ("syslog", 22),
          ("tacplus", 23),
          ("telnet", 24),
          ("tftp", 25),
          ("traceroute", 26),
          ("vrrp", 27))
    )



class TDot1pAppId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("isis", 2),
          ("pppoe", 3))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxVRtrConformance_ObjectIdentity = ObjectIdentity
tmnxVRtrConformance = _TmnxVRtrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3)
)
_TmnxVRtrCompliances_ObjectIdentity = ObjectIdentity
tmnxVRtrCompliances = _TmnxVRtrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 1)
)
_TmnxVRtrGroups_ObjectIdentity = ObjectIdentity
tmnxVRtrGroups = _TmnxVRtrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2)
)
_TmnxVRtrObjs_ObjectIdentity = ObjectIdentity
tmnxVRtrObjs = _TmnxVRtrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3)
)
_VRtrConfTable_Object = MibTable
vRtrConfTable = _VRtrConfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    vRtrConfTable.setStatus("current")
_VRtrConfEntry_Object = MibTableRow
vRtrConfEntry = _VRtrConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1)
)
vRtrConfEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrConfEntry.setStatus("current")
_VRtrID_Type = TmnxVRtrID
_VRtrID_Object = MibTableColumn
vRtrID = _VRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 1),
    _VRtrID_Type()
)
vRtrID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrID.setStatus("current")
_VRtrRowStatus_Type = RowStatus
_VRtrRowStatus_Object = MibTableColumn
vRtrRowStatus = _VRtrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 2),
    _VRtrRowStatus_Type()
)
vRtrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRowStatus.setStatus("current")


class _VRtrAdminState_Type(TmnxAdminState):
    """Custom type vRtrAdminState based on TmnxAdminState"""


_VRtrAdminState_Object = MibTableColumn
vRtrAdminState = _VRtrAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 3),
    _VRtrAdminState_Type()
)
vRtrAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAdminState.setStatus("current")
_VRtrName_Type = TNamedItemOrEmpty
_VRtrName_Object = MibTableColumn
vRtrName = _VRtrName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 4),
    _VRtrName_Type()
)
vRtrName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrName.setStatus("current")


class _VRtrMaxNumRoutes_Type(Integer32):
    """Custom type vRtrMaxNumRoutes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VRtrMaxNumRoutes_Type.__name__ = "Integer32"
_VRtrMaxNumRoutes_Object = MibTableColumn
vRtrMaxNumRoutes = _VRtrMaxNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 5),
    _VRtrMaxNumRoutes_Type()
)
vRtrMaxNumRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxNumRoutes.setStatus("current")


class _VRtrBgpStatus_Type(TmnxStatus):
    """Custom type vRtrBgpStatus based on TmnxStatus"""


_VRtrBgpStatus_Object = MibTableColumn
vRtrBgpStatus = _VRtrBgpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 6),
    _VRtrBgpStatus_Type()
)
vRtrBgpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBgpStatus.setStatus("current")


class _VRtrMplsStatus_Type(TmnxStatus):
    """Custom type vRtrMplsStatus based on TmnxStatus"""


_VRtrMplsStatus_Object = MibTableColumn
vRtrMplsStatus = _VRtrMplsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 7),
    _VRtrMplsStatus_Type()
)
vRtrMplsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMplsStatus.setStatus("current")


class _VRtrOspfStatus_Type(TmnxStatus):
    """Custom type vRtrOspfStatus based on TmnxStatus"""


_VRtrOspfStatus_Object = MibTableColumn
vRtrOspfStatus = _VRtrOspfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 8),
    _VRtrOspfStatus_Type()
)
vRtrOspfStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfStatus.setStatus("obsolete")


class _VRtrRipStatus_Type(TmnxStatus):
    """Custom type vRtrRipStatus based on TmnxStatus"""


_VRtrRipStatus_Object = MibTableColumn
vRtrRipStatus = _VRtrRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 9),
    _VRtrRipStatus_Type()
)
vRtrRipStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRipStatus.setStatus("current")


class _VRtrRsvpStatus_Type(TmnxStatus):
    """Custom type vRtrRsvpStatus based on TmnxStatus"""


_VRtrRsvpStatus_Object = MibTableColumn
vRtrRsvpStatus = _VRtrRsvpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 10),
    _VRtrRsvpStatus_Type()
)
vRtrRsvpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRsvpStatus.setStatus("current")


class _VRtrEcmpMaxRoutes_Type(Unsigned32):
    """Custom type vRtrEcmpMaxRoutes based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_VRtrEcmpMaxRoutes_Type.__name__ = "Unsigned32"
_VRtrEcmpMaxRoutes_Object = MibTableColumn
vRtrEcmpMaxRoutes = _VRtrEcmpMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 11),
    _VRtrEcmpMaxRoutes_Type()
)
vRtrEcmpMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrEcmpMaxRoutes.setStatus("current")


class _VRtrAS_Type(TmnxBgpAutonomousSystem):
    """Custom type vRtrAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_VRtrAS_Object = MibTableColumn
vRtrAS = _VRtrAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 12),
    _VRtrAS_Type()
)
vRtrAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAS.setStatus("current")
_VRtrNewIfIndex_Type = TestAndIncr
_VRtrNewIfIndex_Object = MibTableColumn
vRtrNewIfIndex = _VRtrNewIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 13),
    _VRtrNewIfIndex_Type()
)
vRtrNewIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrNewIfIndex.setStatus("current")


class _VRtrLdpStatus_Type(TmnxStatus):
    """Custom type vRtrLdpStatus based on TmnxStatus"""


_VRtrLdpStatus_Object = MibTableColumn
vRtrLdpStatus = _VRtrLdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 14),
    _VRtrLdpStatus_Type()
)
vRtrLdpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrLdpStatus.setStatus("current")


class _VRtrIsIsStatus_Type(TmnxStatus):
    """Custom type vRtrIsIsStatus based on TmnxStatus"""


_VRtrIsIsStatus_Object = MibTableColumn
vRtrIsIsStatus = _VRtrIsIsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 15),
    _VRtrIsIsStatus_Type()
)
vRtrIsIsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsIsStatus.setStatus("current")
_VRtrRouterId_Type = IpAddress
_VRtrRouterId_Object = MibTableColumn
vRtrRouterId = _VRtrRouterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 16),
    _VRtrRouterId_Type()
)
vRtrRouterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRouterId.setStatus("current")


class _VRtrTriggeredPolicy_Type(TruthValue):
    """Custom type vRtrTriggeredPolicy based on TruthValue"""


_VRtrTriggeredPolicy_Object = MibTableColumn
vRtrTriggeredPolicy = _VRtrTriggeredPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 17),
    _VRtrTriggeredPolicy_Type()
)
vRtrTriggeredPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrTriggeredPolicy.setStatus("current")


class _VRtrConfederationAS_Type(TmnxBgpAutonomousSystem):
    """Custom type vRtrConfederationAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_VRtrConfederationAS_Object = MibTableColumn
vRtrConfederationAS = _VRtrConfederationAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 18),
    _VRtrConfederationAS_Type()
)
vRtrConfederationAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrConfederationAS.setStatus("current")


class _VRtrRouteDistinguisher_Type(TmnxVPNRouteDistinguisher):
    """Custom type vRtrRouteDistinguisher based on TmnxVPNRouteDistinguisher"""
    defaultHexValue = "0000000000000000"


_VRtrRouteDistinguisher_Object = MibTableColumn
vRtrRouteDistinguisher = _VRtrRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 19),
    _VRtrRouteDistinguisher_Type()
)
vRtrRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrRouteDistinguisher.setStatus("current")


class _VRtrMidRouteThreshold_Type(Unsigned32):
    """Custom type vRtrMidRouteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMidRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrMidRouteThreshold_Object = MibTableColumn
vRtrMidRouteThreshold = _VRtrMidRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 20),
    _VRtrMidRouteThreshold_Type()
)
vRtrMidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMidRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMidRouteThreshold.setUnits("percent")


class _VRtrHighRouteThreshold_Type(Unsigned32):
    """Custom type vRtrHighRouteThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrHighRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrHighRouteThreshold_Object = MibTableColumn
vRtrHighRouteThreshold = _VRtrHighRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 21),
    _VRtrHighRouteThreshold_Type()
)
vRtrHighRouteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrHighRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrHighRouteThreshold.setUnits("percent")


class _VRtrIllegalLabelThreshold_Type(Unsigned32):
    """Custom type vRtrIllegalLabelThreshold based on Unsigned32"""
    defaultValue = 0


_VRtrIllegalLabelThreshold_Object = MibTableColumn
vRtrIllegalLabelThreshold = _VRtrIllegalLabelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 22),
    _VRtrIllegalLabelThreshold_Type()
)
vRtrIllegalLabelThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIllegalLabelThreshold.setStatus("current")


class _VRtrVpnId_Type(TmnxVPNId):
    """Custom type vRtrVpnId based on TmnxVPNId"""
    defaultHexValue = ""


_VRtrVpnId_Object = MibTableColumn
vRtrVpnId = _VRtrVpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 23),
    _VRtrVpnId_Type()
)
vRtrVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVpnId.setStatus("current")


class _VRtrDescription_Type(TItemDescription):
    """Custom type vRtrDescription based on TItemDescription"""
    defaultHexValue = ""


_VRtrDescription_Object = MibTableColumn
vRtrDescription = _VRtrDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 25),
    _VRtrDescription_Type()
)
vRtrDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrDescription.setStatus("current")


class _VRtrGracefulRestart_Type(TruthValue):
    """Custom type vRtrGracefulRestart based on TruthValue"""


_VRtrGracefulRestart_Object = MibTableColumn
vRtrGracefulRestart = _VRtrGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 26),
    _VRtrGracefulRestart_Type()
)
vRtrGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGracefulRestart.setStatus("current")


class _VRtrGracefulRestartType_Type(Integer32):
    """Custom type vRtrGracefulRestartType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 2),
          ("manual", 1),
          ("never", 0))
    )


_VRtrGracefulRestartType_Type.__name__ = "Integer32"
_VRtrGracefulRestartType_Object = MibTableColumn
vRtrGracefulRestartType = _VRtrGracefulRestartType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 27),
    _VRtrGracefulRestartType_Type()
)
vRtrGracefulRestartType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrGracefulRestartType.setStatus("current")


class _VRtrType_Type(Integer32):
    """Custom type vRtrType based on Integer32"""
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
        *(("baseRouter", 1),
          ("unknown", 0),
          ("vprn", 2),
          ("vr", 3))
    )


_VRtrType_Type.__name__ = "Integer32"
_VRtrType_Object = MibTableColumn
vRtrType = _VRtrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 28),
    _VRtrType_Type()
)
vRtrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrType.setStatus("current")
_VRtrServiceId_Type = TmnxServId
_VRtrServiceId_Object = MibTableColumn
vRtrServiceId = _VRtrServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 29),
    _VRtrServiceId_Type()
)
vRtrServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrServiceId.setStatus("current")
_VRtrCustId_Type = TmnxCustId
_VRtrCustId_Object = MibTableColumn
vRtrCustId = _VRtrCustId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 30),
    _VRtrCustId_Type()
)
vRtrCustId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrCustId.setStatus("current")


class _VRtrIgmpStatus_Type(TmnxStatus):
    """Custom type vRtrIgmpStatus based on TmnxStatus"""


_VRtrIgmpStatus_Object = MibTableColumn
vRtrIgmpStatus = _VRtrIgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 31),
    _VRtrIgmpStatus_Type()
)
vRtrIgmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgmpStatus.setStatus("current")


class _VRtrMaxNumRoutesLogOnly_Type(TruthValue):
    """Custom type vRtrMaxNumRoutesLogOnly based on TruthValue"""


_VRtrMaxNumRoutesLogOnly_Object = MibTableColumn
vRtrMaxNumRoutesLogOnly = _VRtrMaxNumRoutesLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 32),
    _VRtrMaxNumRoutesLogOnly_Type()
)
vRtrMaxNumRoutesLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxNumRoutesLogOnly.setStatus("current")
_VRtrVrfTarget_Type = TNamedItemOrEmpty
_VRtrVrfTarget_Object = MibTableColumn
vRtrVrfTarget = _VRtrVrfTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 33),
    _VRtrVrfTarget_Type()
)
vRtrVrfTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVrfTarget.setStatus("current")
_VRtrVrfExportTarget_Type = TNamedItemOrEmpty
_VRtrVrfExportTarget_Object = MibTableColumn
vRtrVrfExportTarget = _VRtrVrfExportTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 34),
    _VRtrVrfExportTarget_Type()
)
vRtrVrfExportTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVrfExportTarget.setStatus("current")
_VRtrVrfImportTarget_Type = TNamedItemOrEmpty
_VRtrVrfImportTarget_Object = MibTableColumn
vRtrVrfImportTarget = _VRtrVrfImportTarget_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 35),
    _VRtrVrfImportTarget_Type()
)
vRtrVrfImportTarget.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVrfImportTarget.setStatus("current")


class _VRtrPimStatus_Type(TmnxStatus):
    """Custom type vRtrPimStatus based on TmnxStatus"""


_VRtrPimStatus_Object = MibTableColumn
vRtrPimStatus = _VRtrPimStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 36),
    _VRtrPimStatus_Type()
)
vRtrPimStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrPimStatus.setStatus("current")


class _VRtrMaxMcastNumRoutes_Type(Integer32):
    """Custom type vRtrMaxMcastNumRoutes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VRtrMaxMcastNumRoutes_Type.__name__ = "Integer32"
_VRtrMaxMcastNumRoutes_Object = MibTableColumn
vRtrMaxMcastNumRoutes = _VRtrMaxMcastNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 37),
    _VRtrMaxMcastNumRoutes_Type()
)
vRtrMaxMcastNumRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxMcastNumRoutes.setStatus("current")


class _VRtrMaxMcastNumRoutesLogOnly_Type(TruthValue):
    """Custom type vRtrMaxMcastNumRoutesLogOnly based on TruthValue"""


_VRtrMaxMcastNumRoutesLogOnly_Object = MibTableColumn
vRtrMaxMcastNumRoutesLogOnly = _VRtrMaxMcastNumRoutesLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 38),
    _VRtrMaxMcastNumRoutesLogOnly_Type()
)
vRtrMaxMcastNumRoutesLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMaxMcastNumRoutesLogOnly.setStatus("current")


class _VRtrMcastMidRouteThreshold_Type(Unsigned32):
    """Custom type vRtrMcastMidRouteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrMcastMidRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrMcastMidRouteThreshold_Object = MibTableColumn
vRtrMcastMidRouteThreshold = _VRtrMcastMidRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 39),
    _VRtrMcastMidRouteThreshold_Type()
)
vRtrMcastMidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMcastMidRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrMcastMidRouteThreshold.setUnits("percent")


class _VRtrIgnoreIcmpRedirect_Type(TruthValue):
    """Custom type vRtrIgnoreIcmpRedirect based on TruthValue"""


_VRtrIgnoreIcmpRedirect_Object = MibTableColumn
vRtrIgnoreIcmpRedirect = _VRtrIgnoreIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 40),
    _VRtrIgnoreIcmpRedirect_Type()
)
vRtrIgnoreIcmpRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIgnoreIcmpRedirect.setStatus("current")


class _VRtrOspfv3Status_Type(TmnxStatus):
    """Custom type vRtrOspfv3Status based on TmnxStatus"""


_VRtrOspfv3Status_Object = MibTableColumn
vRtrOspfv3Status = _VRtrOspfv3Status_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 41),
    _VRtrOspfv3Status_Type()
)
vRtrOspfv3Status.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrOspfv3Status.setStatus("obsolete")


class _VRtrMsdpStatus_Type(TmnxStatus):
    """Custom type vRtrMsdpStatus based on TmnxStatus"""


_VRtrMsdpStatus_Object = MibTableColumn
vRtrMsdpStatus = _VRtrMsdpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 42),
    _VRtrMsdpStatus_Type()
)
vRtrMsdpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMsdpStatus.setStatus("current")


class _VRtrVprnType_Type(Integer32):
    """Custom type vRtrVprnType based on Integer32"""
    defaultValue = 1

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
        *(("hub", 2),
          ("regular", 1),
          ("spoke", 3),
          ("subscriberSplitHorizon", 4))
    )


_VRtrVprnType_Type.__name__ = "Integer32"
_VRtrVprnType_Object = MibTableColumn
vRtrVprnType = _VRtrVprnType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 43),
    _VRtrVprnType_Type()
)
vRtrVprnType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrVprnType.setStatus("current")
_VRtrSecondaryVrfId_Type = TmnxVRtrIDOrZero
_VRtrSecondaryVrfId_Object = MibTableColumn
vRtrSecondaryVrfId = _VRtrSecondaryVrfId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 44),
    _VRtrSecondaryVrfId_Type()
)
vRtrSecondaryVrfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSecondaryVrfId.setStatus("current")


class _VRtrMldStatus_Type(TmnxStatus):
    """Custom type vRtrMldStatus based on TmnxStatus"""


_VRtrMldStatus_Object = MibTableColumn
vRtrMldStatus = _VRtrMldStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 45),
    _VRtrMldStatus_Type()
)
vRtrMldStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMldStatus.setStatus("current")


class _VRtrIPv6MaxNumRoutes_Type(Integer32):
    """Custom type vRtrIPv6MaxNumRoutes based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_VRtrIPv6MaxNumRoutes_Type.__name__ = "Integer32"
_VRtrIPv6MaxNumRoutes_Object = MibTableColumn
vRtrIPv6MaxNumRoutes = _VRtrIPv6MaxNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 46),
    _VRtrIPv6MaxNumRoutes_Type()
)
vRtrIPv6MaxNumRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6MaxNumRoutes.setStatus("current")


class _VRtrIPv6MidRouteThreshold_Type(Unsigned32):
    """Custom type vRtrIPv6MidRouteThreshold based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrIPv6MidRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrIPv6MidRouteThreshold_Object = MibTableColumn
vRtrIPv6MidRouteThreshold = _VRtrIPv6MidRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 47),
    _VRtrIPv6MidRouteThreshold_Type()
)
vRtrIPv6MidRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6MidRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIPv6MidRouteThreshold.setUnits("percent")


class _VRtrIPv6HighRouteThreshold_Type(Unsigned32):
    """Custom type vRtrIPv6HighRouteThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrIPv6HighRouteThreshold_Type.__name__ = "Unsigned32"
_VRtrIPv6HighRouteThreshold_Object = MibTableColumn
vRtrIPv6HighRouteThreshold = _VRtrIPv6HighRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 48),
    _VRtrIPv6HighRouteThreshold_Type()
)
vRtrIPv6HighRouteThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIPv6HighRouteThreshold.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIPv6HighRouteThreshold.setUnits("percent")


class _VRtrIPv6MaxNumRoutesLogOnly_Type(TruthValue):
    """Custom type vRtrIPv6MaxNumRoutesLogOnly based on TruthValue"""


_VRtrIPv6MaxNumRoutesLogOnly_Object = MibTableColumn
vRtrIPv6MaxNumRoutesLogOnly = _VRtrIPv6MaxNumRoutesLogOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 49),
    _VRtrIPv6MaxNumRoutesLogOnly_Type()
)
vRtrIPv6MaxNumRoutesLogOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6MaxNumRoutesLogOnly.setStatus("current")


class _VRtrIPv6IgnoreIcmpRedirect_Type(TruthValue):
    """Custom type vRtrIPv6IgnoreIcmpRedirect based on TruthValue"""


_VRtrIPv6IgnoreIcmpRedirect_Object = MibTableColumn
vRtrIPv6IgnoreIcmpRedirect = _VRtrIPv6IgnoreIcmpRedirect_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 50),
    _VRtrIPv6IgnoreIcmpRedirect_Type()
)
vRtrIPv6IgnoreIcmpRedirect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIPv6IgnoreIcmpRedirect.setStatus("current")


class _VRtrMcPathMgmtPlcyName_Type(TNamedItem):
    """Custom type vRtrMcPathMgmtPlcyName based on TNamedItem"""
    defaultValue = OctetString("default")


_VRtrMcPathMgmtPlcyName_Object = MibTableColumn
vRtrMcPathMgmtPlcyName = _VRtrMcPathMgmtPlcyName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 1, 1, 51),
    _VRtrMcPathMgmtPlcyName_Type()
)
vRtrMcPathMgmtPlcyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrMcPathMgmtPlcyName.setStatus("current")
_VRtrStatTable_Object = MibTable
vRtrStatTable = _VRtrStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    vRtrStatTable.setStatus("current")
_VRtrStatEntry_Object = MibTableRow
vRtrStatEntry = _VRtrStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrStatEntry.setStatus("current")
_VRtrOperState_Type = TmnxOperState
_VRtrOperState_Object = MibTableColumn
vRtrOperState = _VRtrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 1),
    _VRtrOperState_Type()
)
vRtrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOperState.setStatus("current")
_VRtrDirectRoutes_Type = Gauge32
_VRtrDirectRoutes_Object = MibTableColumn
vRtrDirectRoutes = _VRtrDirectRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 2),
    _VRtrDirectRoutes_Type()
)
vRtrDirectRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDirectRoutes.setStatus("current")
_VRtrDirectActiveRoutes_Type = Gauge32
_VRtrDirectActiveRoutes_Object = MibTableColumn
vRtrDirectActiveRoutes = _VRtrDirectActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 3),
    _VRtrDirectActiveRoutes_Type()
)
vRtrDirectActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDirectActiveRoutes.setStatus("current")
_VRtrStaticRoutes_Type = Gauge32
_VRtrStaticRoutes_Object = MibTableColumn
vRtrStaticRoutes = _VRtrStaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 4),
    _VRtrStaticRoutes_Type()
)
vRtrStaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRoutes.setStatus("current")
_VRtrStaticActiveRoutes_Type = Gauge32
_VRtrStaticActiveRoutes_Object = MibTableColumn
vRtrStaticActiveRoutes = _VRtrStaticActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 5),
    _VRtrStaticActiveRoutes_Type()
)
vRtrStaticActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticActiveRoutes.setStatus("current")
_VRtrOSPFRoutes_Type = Gauge32
_VRtrOSPFRoutes_Object = MibTableColumn
vRtrOSPFRoutes = _VRtrOSPFRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 6),
    _VRtrOSPFRoutes_Type()
)
vRtrOSPFRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOSPFRoutes.setStatus("current")
_VRtrOSPFActiveRoutes_Type = Gauge32
_VRtrOSPFActiveRoutes_Object = MibTableColumn
vRtrOSPFActiveRoutes = _VRtrOSPFActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 7),
    _VRtrOSPFActiveRoutes_Type()
)
vRtrOSPFActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrOSPFActiveRoutes.setStatus("current")
_VRtrBGPRoutes_Type = Gauge32
_VRtrBGPRoutes_Object = MibTableColumn
vRtrBGPRoutes = _VRtrBGPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 8),
    _VRtrBGPRoutes_Type()
)
vRtrBGPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBGPRoutes.setStatus("current")
_VRtrBGPActiveRoutes_Type = Gauge32
_VRtrBGPActiveRoutes_Object = MibTableColumn
vRtrBGPActiveRoutes = _VRtrBGPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 9),
    _VRtrBGPActiveRoutes_Type()
)
vRtrBGPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBGPActiveRoutes.setStatus("current")
_VRtrISISRoutes_Type = Gauge32
_VRtrISISRoutes_Object = MibTableColumn
vRtrISISRoutes = _VRtrISISRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 10),
    _VRtrISISRoutes_Type()
)
vRtrISISRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrISISRoutes.setStatus("current")
_VRtrISISActiveRoutes_Type = Gauge32
_VRtrISISActiveRoutes_Object = MibTableColumn
vRtrISISActiveRoutes = _VRtrISISActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 11),
    _VRtrISISActiveRoutes_Type()
)
vRtrISISActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrISISActiveRoutes.setStatus("current")
_VRtrRIPRoutes_Type = Gauge32
_VRtrRIPRoutes_Object = MibTableColumn
vRtrRIPRoutes = _VRtrRIPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 12),
    _VRtrRIPRoutes_Type()
)
vRtrRIPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRIPRoutes.setStatus("current")
_VRtrRIPActiveRoutes_Type = Gauge32
_VRtrRIPActiveRoutes_Object = MibTableColumn
vRtrRIPActiveRoutes = _VRtrRIPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 13),
    _VRtrRIPActiveRoutes_Type()
)
vRtrRIPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrRIPActiveRoutes.setStatus("current")
_VRtrAggregateRoutes_Type = Gauge32
_VRtrAggregateRoutes_Object = MibTableColumn
vRtrAggregateRoutes = _VRtrAggregateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 14),
    _VRtrAggregateRoutes_Type()
)
vRtrAggregateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrAggregateRoutes.setStatus("current")
_VRtrAggregateActiveRoutes_Type = Gauge32
_VRtrAggregateActiveRoutes_Object = MibTableColumn
vRtrAggregateActiveRoutes = _VRtrAggregateActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 15),
    _VRtrAggregateActiveRoutes_Type()
)
vRtrAggregateActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrAggregateActiveRoutes.setStatus("current")
_VRtrStatConfiguredIfs_Type = Gauge32
_VRtrStatConfiguredIfs_Object = MibTableColumn
vRtrStatConfiguredIfs = _VRtrStatConfiguredIfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 16),
    _VRtrStatConfiguredIfs_Type()
)
vRtrStatConfiguredIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatConfiguredIfs.setStatus("current")
_VRtrStatActiveIfs_Type = Gauge32
_VRtrStatActiveIfs_Object = MibTableColumn
vRtrStatActiveIfs = _VRtrStatActiveIfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 17),
    _VRtrStatActiveIfs_Type()
)
vRtrStatActiveIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveIfs.setStatus("current")
_VRtrStatIllegalLabels_Type = Counter32
_VRtrStatIllegalLabels_Object = MibTableColumn
vRtrStatIllegalLabels = _VRtrStatIllegalLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 18),
    _VRtrStatIllegalLabels_Type()
)
vRtrStatIllegalLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatIllegalLabels.setStatus("current")
_VRtrStatCurrNumRoutes_Type = Gauge32
_VRtrStatCurrNumRoutes_Object = MibTableColumn
vRtrStatCurrNumRoutes = _VRtrStatCurrNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 19),
    _VRtrStatCurrNumRoutes_Type()
)
vRtrStatCurrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatCurrNumRoutes.setStatus("current")
_VRtrStatBGPVpnRoutes_Type = Gauge32
_VRtrStatBGPVpnRoutes_Object = MibTableColumn
vRtrStatBGPVpnRoutes = _VRtrStatBGPVpnRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 20),
    _VRtrStatBGPVpnRoutes_Type()
)
vRtrStatBGPVpnRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatBGPVpnRoutes.setStatus("current")
_VRtrStatBGPVpnActiveRoutes_Type = Gauge32
_VRtrStatBGPVpnActiveRoutes_Object = MibTableColumn
vRtrStatBGPVpnActiveRoutes = _VRtrStatBGPVpnActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 21),
    _VRtrStatBGPVpnActiveRoutes_Type()
)
vRtrStatBGPVpnActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatBGPVpnActiveRoutes.setStatus("current")
_VRtrStatTotalLdpTunnels_Type = Gauge32
_VRtrStatTotalLdpTunnels_Object = MibTableColumn
vRtrStatTotalLdpTunnels = _VRtrStatTotalLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 22),
    _VRtrStatTotalLdpTunnels_Type()
)
vRtrStatTotalLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalLdpTunnels.setStatus("current")
_VRtrStatTotalSdpTunnels_Type = Gauge32
_VRtrStatTotalSdpTunnels_Object = MibTableColumn
vRtrStatTotalSdpTunnels = _VRtrStatTotalSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 23),
    _VRtrStatTotalSdpTunnels_Type()
)
vRtrStatTotalSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalSdpTunnels.setStatus("current")
_VRtrStatActiveLdpTunnels_Type = Gauge32
_VRtrStatActiveLdpTunnels_Object = MibTableColumn
vRtrStatActiveLdpTunnels = _VRtrStatActiveLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 24),
    _VRtrStatActiveLdpTunnels_Type()
)
vRtrStatActiveLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveLdpTunnels.setStatus("current")
_VRtrStatActiveSdpTunnels_Type = Gauge32
_VRtrStatActiveSdpTunnels_Object = MibTableColumn
vRtrStatActiveSdpTunnels = _VRtrStatActiveSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 25),
    _VRtrStatActiveSdpTunnels_Type()
)
vRtrStatActiveSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveSdpTunnels.setStatus("current")
_VRtrMulticastRoutes_Type = Gauge32
_VRtrMulticastRoutes_Object = MibTableColumn
vRtrMulticastRoutes = _VRtrMulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 26),
    _VRtrMulticastRoutes_Type()
)
vRtrMulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMulticastRoutes.setStatus("current")
_VRtrStatActiveARPEntries_Type = Gauge32
_VRtrStatActiveARPEntries_Object = MibTableColumn
vRtrStatActiveARPEntries = _VRtrStatActiveARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 27),
    _VRtrStatActiveARPEntries_Type()
)
vRtrStatActiveARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveARPEntries.setStatus("current")
_VRtrStatTotalARPEntries_Type = Gauge32
_VRtrStatTotalARPEntries_Object = MibTableColumn
vRtrStatTotalARPEntries = _VRtrStatTotalARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 28),
    _VRtrStatTotalARPEntries_Type()
)
vRtrStatTotalARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalARPEntries.setStatus("current")
_VRtrV6DirectRoutes_Type = Gauge32
_VRtrV6DirectRoutes_Object = MibTableColumn
vRtrV6DirectRoutes = _VRtrV6DirectRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 29),
    _VRtrV6DirectRoutes_Type()
)
vRtrV6DirectRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6DirectRoutes.setStatus("current")
_VRtrV6DirectActiveRoutes_Type = Gauge32
_VRtrV6DirectActiveRoutes_Object = MibTableColumn
vRtrV6DirectActiveRoutes = _VRtrV6DirectActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 30),
    _VRtrV6DirectActiveRoutes_Type()
)
vRtrV6DirectActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6DirectActiveRoutes.setStatus("current")
_VRtrV6StaticRoutes_Type = Gauge32
_VRtrV6StaticRoutes_Object = MibTableColumn
vRtrV6StaticRoutes = _VRtrV6StaticRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 31),
    _VRtrV6StaticRoutes_Type()
)
vRtrV6StaticRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StaticRoutes.setStatus("current")
_VRtrV6StaticActiveRoutes_Type = Gauge32
_VRtrV6StaticActiveRoutes_Object = MibTableColumn
vRtrV6StaticActiveRoutes = _VRtrV6StaticActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 32),
    _VRtrV6StaticActiveRoutes_Type()
)
vRtrV6StaticActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StaticActiveRoutes.setStatus("current")
_VRtrV6OSPFRoutes_Type = Gauge32
_VRtrV6OSPFRoutes_Object = MibTableColumn
vRtrV6OSPFRoutes = _VRtrV6OSPFRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 33),
    _VRtrV6OSPFRoutes_Type()
)
vRtrV6OSPFRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6OSPFRoutes.setStatus("current")
_VRtrV6OSPFActiveRoutes_Type = Gauge32
_VRtrV6OSPFActiveRoutes_Object = MibTableColumn
vRtrV6OSPFActiveRoutes = _VRtrV6OSPFActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 34),
    _VRtrV6OSPFActiveRoutes_Type()
)
vRtrV6OSPFActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6OSPFActiveRoutes.setStatus("current")
_VRtrV6BGPRoutes_Type = Gauge32
_VRtrV6BGPRoutes_Object = MibTableColumn
vRtrV6BGPRoutes = _VRtrV6BGPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 35),
    _VRtrV6BGPRoutes_Type()
)
vRtrV6BGPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6BGPRoutes.setStatus("current")
_VRtrV6BGPActiveRoutes_Type = Gauge32
_VRtrV6BGPActiveRoutes_Object = MibTableColumn
vRtrV6BGPActiveRoutes = _VRtrV6BGPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 36),
    _VRtrV6BGPActiveRoutes_Type()
)
vRtrV6BGPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6BGPActiveRoutes.setStatus("current")
_VRtrV6ISISRoutes_Type = Gauge32
_VRtrV6ISISRoutes_Object = MibTableColumn
vRtrV6ISISRoutes = _VRtrV6ISISRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 37),
    _VRtrV6ISISRoutes_Type()
)
vRtrV6ISISRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6ISISRoutes.setStatus("current")
_VRtrV6ISISActiveRoutes_Type = Gauge32
_VRtrV6ISISActiveRoutes_Object = MibTableColumn
vRtrV6ISISActiveRoutes = _VRtrV6ISISActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 38),
    _VRtrV6ISISActiveRoutes_Type()
)
vRtrV6ISISActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6ISISActiveRoutes.setStatus("current")
_VRtrV6RIPRoutes_Type = Gauge32
_VRtrV6RIPRoutes_Object = MibTableColumn
vRtrV6RIPRoutes = _VRtrV6RIPRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 39),
    _VRtrV6RIPRoutes_Type()
)
vRtrV6RIPRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6RIPRoutes.setStatus("current")
_VRtrV6RIPActiveRoutes_Type = Gauge32
_VRtrV6RIPActiveRoutes_Object = MibTableColumn
vRtrV6RIPActiveRoutes = _VRtrV6RIPActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 40),
    _VRtrV6RIPActiveRoutes_Type()
)
vRtrV6RIPActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6RIPActiveRoutes.setStatus("current")
_VRtrV6AggregateRoutes_Type = Gauge32
_VRtrV6AggregateRoutes_Object = MibTableColumn
vRtrV6AggregateRoutes = _VRtrV6AggregateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 41),
    _VRtrV6AggregateRoutes_Type()
)
vRtrV6AggregateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6AggregateRoutes.setStatus("current")
_VRtrV6AggregateActiveRoutes_Type = Gauge32
_VRtrV6AggregateActiveRoutes_Object = MibTableColumn
vRtrV6AggregateActiveRoutes = _VRtrV6AggregateActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 42),
    _VRtrV6AggregateActiveRoutes_Type()
)
vRtrV6AggregateActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6AggregateActiveRoutes.setStatus("current")
_VRtrV6StatConfiguredIfs_Type = Gauge32
_VRtrV6StatConfiguredIfs_Object = MibTableColumn
vRtrV6StatConfiguredIfs = _VRtrV6StatConfiguredIfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 43),
    _VRtrV6StatConfiguredIfs_Type()
)
vRtrV6StatConfiguredIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatConfiguredIfs.setStatus("current")
_VRtrV6StatActiveIfs_Type = Gauge32
_VRtrV6StatActiveIfs_Object = MibTableColumn
vRtrV6StatActiveIfs = _VRtrV6StatActiveIfs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 44),
    _VRtrV6StatActiveIfs_Type()
)
vRtrV6StatActiveIfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveIfs.setStatus("current")
_VRtrV6StatIllegalLabels_Type = Counter32
_VRtrV6StatIllegalLabels_Object = MibTableColumn
vRtrV6StatIllegalLabels = _VRtrV6StatIllegalLabels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 45),
    _VRtrV6StatIllegalLabels_Type()
)
vRtrV6StatIllegalLabels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatIllegalLabels.setStatus("current")
_VRtrV6StatCurrNumRoutes_Type = Gauge32
_VRtrV6StatCurrNumRoutes_Object = MibTableColumn
vRtrV6StatCurrNumRoutes = _VRtrV6StatCurrNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 46),
    _VRtrV6StatCurrNumRoutes_Type()
)
vRtrV6StatCurrNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatCurrNumRoutes.setStatus("current")
_VRtrV6StatBGPVpnRoutes_Type = Gauge32
_VRtrV6StatBGPVpnRoutes_Object = MibTableColumn
vRtrV6StatBGPVpnRoutes = _VRtrV6StatBGPVpnRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 47),
    _VRtrV6StatBGPVpnRoutes_Type()
)
vRtrV6StatBGPVpnRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatBGPVpnRoutes.setStatus("current")
_VRtrV6StatBGPVpnActiveRoutes_Type = Gauge32
_VRtrV6StatBGPVpnActiveRoutes_Object = MibTableColumn
vRtrV6StatBGPVpnActiveRoutes = _VRtrV6StatBGPVpnActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 48),
    _VRtrV6StatBGPVpnActiveRoutes_Type()
)
vRtrV6StatBGPVpnActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatBGPVpnActiveRoutes.setStatus("current")
_VRtrV6StatTotalLdpTunnels_Type = Gauge32
_VRtrV6StatTotalLdpTunnels_Object = MibTableColumn
vRtrV6StatTotalLdpTunnels = _VRtrV6StatTotalLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 49),
    _VRtrV6StatTotalLdpTunnels_Type()
)
vRtrV6StatTotalLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalLdpTunnels.setStatus("current")
_VRtrV6StatTotalSdpTunnels_Type = Gauge32
_VRtrV6StatTotalSdpTunnels_Object = MibTableColumn
vRtrV6StatTotalSdpTunnels = _VRtrV6StatTotalSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 50),
    _VRtrV6StatTotalSdpTunnels_Type()
)
vRtrV6StatTotalSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalSdpTunnels.setStatus("current")
_VRtrV6StatActiveLdpTunnels_Type = Gauge32
_VRtrV6StatActiveLdpTunnels_Object = MibTableColumn
vRtrV6StatActiveLdpTunnels = _VRtrV6StatActiveLdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 51),
    _VRtrV6StatActiveLdpTunnels_Type()
)
vRtrV6StatActiveLdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveLdpTunnels.setStatus("current")
_VRtrV6StatActiveSdpTunnels_Type = Gauge32
_VRtrV6StatActiveSdpTunnels_Object = MibTableColumn
vRtrV6StatActiveSdpTunnels = _VRtrV6StatActiveSdpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 52),
    _VRtrV6StatActiveSdpTunnels_Type()
)
vRtrV6StatActiveSdpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveSdpTunnels.setStatus("current")
_VRtrV6MulticastRoutes_Type = Gauge32
_VRtrV6MulticastRoutes_Object = MibTableColumn
vRtrV6MulticastRoutes = _VRtrV6MulticastRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 53),
    _VRtrV6MulticastRoutes_Type()
)
vRtrV6MulticastRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6MulticastRoutes.setStatus("current")
_VRtrV6StatActiveNbrEntries_Type = Gauge32
_VRtrV6StatActiveNbrEntries_Object = MibTableColumn
vRtrV6StatActiveNbrEntries = _VRtrV6StatActiveNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 54),
    _VRtrV6StatActiveNbrEntries_Type()
)
vRtrV6StatActiveNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveNbrEntries.setStatus("current")
_VRtrV6StatTotalNbrEntries_Type = Gauge32
_VRtrV6StatTotalNbrEntries_Object = MibTableColumn
vRtrV6StatTotalNbrEntries = _VRtrV6StatTotalNbrEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 55),
    _VRtrV6StatTotalNbrEntries_Type()
)
vRtrV6StatTotalNbrEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalNbrEntries.setStatus("current")
_VRtrSubMgmtRoutes_Type = Gauge32
_VRtrSubMgmtRoutes_Object = MibTableColumn
vRtrSubMgmtRoutes = _VRtrSubMgmtRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 56),
    _VRtrSubMgmtRoutes_Type()
)
vRtrSubMgmtRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSubMgmtRoutes.setStatus("current")
_VRtrSubMgmtActiveRoutes_Type = Gauge32
_VRtrSubMgmtActiveRoutes_Object = MibTableColumn
vRtrSubMgmtActiveRoutes = _VRtrSubMgmtActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 57),
    _VRtrSubMgmtActiveRoutes_Type()
)
vRtrSubMgmtActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrSubMgmtActiveRoutes.setStatus("current")
_VRtrStatTotalRsvpTunnels_Type = Gauge32
_VRtrStatTotalRsvpTunnels_Object = MibTableColumn
vRtrStatTotalRsvpTunnels = _VRtrStatTotalRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 58),
    _VRtrStatTotalRsvpTunnels_Type()
)
vRtrStatTotalRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatTotalRsvpTunnels.setStatus("current")
_VRtrStatActiveRsvpTunnels_Type = Gauge32
_VRtrStatActiveRsvpTunnels_Object = MibTableColumn
vRtrStatActiveRsvpTunnels = _VRtrStatActiveRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 59),
    _VRtrStatActiveRsvpTunnels_Type()
)
vRtrStatActiveRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatActiveRsvpTunnels.setStatus("current")
_VRtrV6StatTotalRsvpTunnels_Type = Gauge32
_VRtrV6StatTotalRsvpTunnels_Object = MibTableColumn
vRtrV6StatTotalRsvpTunnels = _VRtrV6StatTotalRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 60),
    _VRtrV6StatTotalRsvpTunnels_Type()
)
vRtrV6StatTotalRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatTotalRsvpTunnels.setStatus("current")
_VRtrV6StatActiveRsvpTunnels_Type = Gauge32
_VRtrV6StatActiveRsvpTunnels_Object = MibTableColumn
vRtrV6StatActiveRsvpTunnels = _VRtrV6StatActiveRsvpTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 61),
    _VRtrV6StatActiveRsvpTunnels_Type()
)
vRtrV6StatActiveRsvpTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6StatActiveRsvpTunnels.setStatus("current")
_VRtrHostRoutes_Type = Gauge32
_VRtrHostRoutes_Object = MibTableColumn
vRtrHostRoutes = _VRtrHostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 62),
    _VRtrHostRoutes_Type()
)
vRtrHostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrHostRoutes.setStatus("current")
_VRtrHostActiveRoutes_Type = Gauge32
_VRtrHostActiveRoutes_Object = MibTableColumn
vRtrHostActiveRoutes = _VRtrHostActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 63),
    _VRtrHostActiveRoutes_Type()
)
vRtrHostActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrHostActiveRoutes.setStatus("current")
_VRtrV6HostRoutes_Type = Gauge32
_VRtrV6HostRoutes_Object = MibTableColumn
vRtrV6HostRoutes = _VRtrV6HostRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 64),
    _VRtrV6HostRoutes_Type()
)
vRtrV6HostRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6HostRoutes.setStatus("current")
_VRtrV6HostActiveRoutes_Type = Gauge32
_VRtrV6HostActiveRoutes_Object = MibTableColumn
vRtrV6HostActiveRoutes = _VRtrV6HostActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 65),
    _VRtrV6HostActiveRoutes_Type()
)
vRtrV6HostActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrV6HostActiveRoutes.setStatus("current")
_VRtrStatLocalARPEntries_Type = Gauge32
_VRtrStatLocalARPEntries_Object = MibTableColumn
vRtrStatLocalARPEntries = _VRtrStatLocalARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 66),
    _VRtrStatLocalARPEntries_Type()
)
vRtrStatLocalARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatLocalARPEntries.setStatus("current")
_VRtrStatStaticARPEntries_Type = Gauge32
_VRtrStatStaticARPEntries_Object = MibTableColumn
vRtrStatStaticARPEntries = _VRtrStatStaticARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 67),
    _VRtrStatStaticARPEntries_Type()
)
vRtrStatStaticARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatStaticARPEntries.setStatus("current")
_VRtrStatDynamicARPEntries_Type = Gauge32
_VRtrStatDynamicARPEntries_Object = MibTableColumn
vRtrStatDynamicARPEntries = _VRtrStatDynamicARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 68),
    _VRtrStatDynamicARPEntries_Type()
)
vRtrStatDynamicARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatDynamicARPEntries.setStatus("current")
_VRtrStatManagedARPEntries_Type = Gauge32
_VRtrStatManagedARPEntries_Object = MibTableColumn
vRtrStatManagedARPEntries = _VRtrStatManagedARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 69),
    _VRtrStatManagedARPEntries_Type()
)
vRtrStatManagedARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatManagedARPEntries.setStatus("current")
_VRtrStatInternalARPEntries_Type = Gauge32
_VRtrStatInternalARPEntries_Object = MibTableColumn
vRtrStatInternalARPEntries = _VRtrStatInternalARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 70),
    _VRtrStatInternalARPEntries_Type()
)
vRtrStatInternalARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStatInternalARPEntries.setStatus("current")
_VRtrManagedRoutes_Type = Gauge32
_VRtrManagedRoutes_Object = MibTableColumn
vRtrManagedRoutes = _VRtrManagedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 71),
    _VRtrManagedRoutes_Type()
)
vRtrManagedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrManagedRoutes.setStatus("current")
_VRtrManagedActiveRoutes_Type = Gauge32
_VRtrManagedActiveRoutes_Object = MibTableColumn
vRtrManagedActiveRoutes = _VRtrManagedActiveRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 2, 1, 72),
    _VRtrManagedActiveRoutes_Type()
)
vRtrManagedActiveRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrManagedActiveRoutes.setStatus("current")


class _VRtrIfTotalNumber_Type(Integer32):
    """Custom type vRtrIfTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIfTotalNumber_Type.__name__ = "Integer32"
_VRtrIfTotalNumber_Object = MibScalar
vRtrIfTotalNumber = _VRtrIfTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 3),
    _VRtrIfTotalNumber_Type()
)
vRtrIfTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfTotalNumber.setStatus("current")
_VRtrIfTable_Object = MibTable
vRtrIfTable = _VRtrIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    vRtrIfTable.setStatus("current")
_VRtrIfEntry_Object = MibTableRow
vRtrIfEntry = _VRtrIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1)
)
vRtrIfEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIfEntry.setStatus("current")
_VRtrIfIndex_Type = InterfaceIndex
_VRtrIfIndex_Object = MibTableColumn
vRtrIfIndex = _VRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 1),
    _VRtrIfIndex_Type()
)
vRtrIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIfIndex.setStatus("current")
_VRtrIfRowStatus_Type = RowStatus
_VRtrIfRowStatus_Object = MibTableColumn
vRtrIfRowStatus = _VRtrIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 2),
    _VRtrIfRowStatus_Type()
)
vRtrIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfRowStatus.setStatus("current")


class _VRtrIfType_Type(Integer32):
    """Custom type vRtrIfType based on Integer32"""
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
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("service", 2),
          ("serviceIes", 3),
          ("serviceIesCem", 13),
          ("serviceIesGroup", 7),
          ("serviceIesRedundant", 10),
          ("serviceIesSubscriber", 6),
          ("serviceRtdVpls", 4),
          ("serviceVpls", 12),
          ("serviceVprn", 5),
          ("serviceVprnCem", 14),
          ("serviceVprnGroup", 9),
          ("serviceVprnIPMirror", 16),
          ("serviceVprnIPsec", 15),
          ("serviceVprnRedundant", 11),
          ("serviceVprnSubscriber", 8))
    )


_VRtrIfType_Type.__name__ = "Integer32"
_VRtrIfType_Object = MibTableColumn
vRtrIfType = _VRtrIfType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 3),
    _VRtrIfType_Type()
)
vRtrIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfType.setStatus("current")
_VRtrIfName_Type = TNamedItem
_VRtrIfName_Object = MibTableColumn
vRtrIfName = _VRtrIfName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 4),
    _VRtrIfName_Type()
)
vRtrIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfName.setStatus("current")


class _VRtrIfPortID_Type(TmnxPortID):
    """Custom type vRtrIfPortID based on TmnxPortID"""
    defaultValue = 0


_VRtrIfPortID_Object = MibTableColumn
vRtrIfPortID = _VRtrIfPortID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 5),
    _VRtrIfPortID_Type()
)
vRtrIfPortID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfPortID.setStatus("current")


class _VRtrIfChannelID_Type(Unsigned32):
    """Custom type vRtrIfChannelID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_VRtrIfChannelID_Type.__name__ = "Unsigned32"
_VRtrIfChannelID_Object = MibTableColumn
vRtrIfChannelID = _VRtrIfChannelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 6),
    _VRtrIfChannelID_Type()
)
vRtrIfChannelID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfChannelID.setStatus("obsolete")
_VRtrIfEncapValue_Type = TmnxEncapVal
_VRtrIfEncapValue_Object = MibTableColumn
vRtrIfEncapValue = _VRtrIfEncapValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 7),
    _VRtrIfEncapValue_Type()
)
vRtrIfEncapValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfEncapValue.setStatus("current")


class _VRtrIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIfAdminState based on TmnxAdminState"""


_VRtrIfAdminState_Object = MibTableColumn
vRtrIfAdminState = _VRtrIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 8),
    _VRtrIfAdminState_Type()
)
vRtrIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfAdminState.setStatus("current")
_VRtrIfOperState_Type = TmnxOperState
_VRtrIfOperState_Object = MibTableColumn
vRtrIfOperState = _VRtrIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 9),
    _VRtrIfOperState_Type()
)
vRtrIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfOperState.setStatus("current")


class _VRtrIfAlias_Type(DisplayString):
    """Custom type vRtrIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrIfAlias_Type.__name__ = "DisplayString"
_VRtrIfAlias_Object = MibTableColumn
vRtrIfAlias = _VRtrIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 10),
    _VRtrIfAlias_Type()
)
vRtrIfAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfAlias.setStatus("current")
_VRtrIfPhysicalAddress_Type = MacAddress
_VRtrIfPhysicalAddress_Object = MibTableColumn
vRtrIfPhysicalAddress = _VRtrIfPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 11),
    _VRtrIfPhysicalAddress_Type()
)
vRtrIfPhysicalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfPhysicalAddress.setStatus("current")


class _VRtrIfArpTimeout_Type(Unsigned32):
    """Custom type vRtrIfArpTimeout based on Unsigned32"""
    defaultValue = 14400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIfArpTimeout_Type.__name__ = "Unsigned32"
_VRtrIfArpTimeout_Object = MibTableColumn
vRtrIfArpTimeout = _VRtrIfArpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 12),
    _VRtrIfArpTimeout_Type()
)
vRtrIfArpTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfArpTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfArpTimeout.setUnits("seconds")


class _VRtrIfIcmpMaskReply_Type(TruthValue):
    """Custom type vRtrIfIcmpMaskReply based on TruthValue"""


_VRtrIfIcmpMaskReply_Object = MibTableColumn
vRtrIfIcmpMaskReply = _VRtrIfIcmpMaskReply_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 13),
    _VRtrIfIcmpMaskReply_Type()
)
vRtrIfIcmpMaskReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpMaskReply.setStatus("current")


class _VRtrIfIcmpRedirects_Type(TruthValue):
    """Custom type vRtrIfIcmpRedirects based on TruthValue"""


_VRtrIfIcmpRedirects_Object = MibTableColumn
vRtrIfIcmpRedirects = _VRtrIfIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 14),
    _VRtrIfIcmpRedirects_Type()
)
vRtrIfIcmpRedirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpRedirects.setStatus("current")


class _VRtrIfIcmpNumRedirects_Type(Unsigned32):
    """Custom type vRtrIfIcmpNumRedirects based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpNumRedirects_Type.__name__ = "Unsigned32"
_VRtrIfIcmpNumRedirects_Object = MibTableColumn
vRtrIfIcmpNumRedirects = _VRtrIfIcmpNumRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 15),
    _VRtrIfIcmpNumRedirects_Type()
)
vRtrIfIcmpNumRedirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpNumRedirects.setStatus("current")


class _VRtrIfIcmpRedirectsTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpRedirectsTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpRedirectsTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpRedirectsTime_Object = MibTableColumn
vRtrIfIcmpRedirectsTime = _VRtrIfIcmpRedirectsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 16),
    _VRtrIfIcmpRedirectsTime_Type()
)
vRtrIfIcmpRedirectsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpRedirectsTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpRedirectsTime.setUnits("seconds")


class _VRtrIfIcmpUnreachables_Type(TruthValue):
    """Custom type vRtrIfIcmpUnreachables based on TruthValue"""


_VRtrIfIcmpUnreachables_Object = MibTableColumn
vRtrIfIcmpUnreachables = _VRtrIfIcmpUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 17),
    _VRtrIfIcmpUnreachables_Type()
)
vRtrIfIcmpUnreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpUnreachables.setStatus("current")


class _VRtrIfIcmpNumUnreachables_Type(Unsigned32):
    """Custom type vRtrIfIcmpNumUnreachables based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpNumUnreachables_Type.__name__ = "Unsigned32"
_VRtrIfIcmpNumUnreachables_Object = MibTableColumn
vRtrIfIcmpNumUnreachables = _VRtrIfIcmpNumUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 18),
    _VRtrIfIcmpNumUnreachables_Type()
)
vRtrIfIcmpNumUnreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpNumUnreachables.setStatus("current")


class _VRtrIfIcmpUnreachablesTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpUnreachablesTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpUnreachablesTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpUnreachablesTime_Object = MibTableColumn
vRtrIfIcmpUnreachablesTime = _VRtrIfIcmpUnreachablesTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 19),
    _VRtrIfIcmpUnreachablesTime_Type()
)
vRtrIfIcmpUnreachablesTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpUnreachablesTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpUnreachablesTime.setUnits("seconds")


class _VRtrIfIcmpTtlExpired_Type(TruthValue):
    """Custom type vRtrIfIcmpTtlExpired based on TruthValue"""


_VRtrIfIcmpTtlExpired_Object = MibTableColumn
vRtrIfIcmpTtlExpired = _VRtrIfIcmpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 20),
    _VRtrIfIcmpTtlExpired_Type()
)
vRtrIfIcmpTtlExpired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpTtlExpired.setStatus("current")


class _VRtrIfIcmpNumTtlExpired_Type(Unsigned32):
    """Custom type vRtrIfIcmpNumTtlExpired based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpNumTtlExpired_Type.__name__ = "Unsigned32"
_VRtrIfIcmpNumTtlExpired_Object = MibTableColumn
vRtrIfIcmpNumTtlExpired = _VRtrIfIcmpNumTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 21),
    _VRtrIfIcmpNumTtlExpired_Type()
)
vRtrIfIcmpNumTtlExpired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpNumTtlExpired.setStatus("current")


class _VRtrIfIcmpTtlExpiredTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpTtlExpiredTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpTtlExpiredTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpTtlExpiredTime_Object = MibTableColumn
vRtrIfIcmpTtlExpiredTime = _VRtrIfIcmpTtlExpiredTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 22),
    _VRtrIfIcmpTtlExpiredTime_Type()
)
vRtrIfIcmpTtlExpiredTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpTtlExpiredTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpTtlExpiredTime.setUnits("seconds")


class _VRtrIfNtpBroadcast_Type(TruthValue):
    """Custom type vRtrIfNtpBroadcast based on TruthValue"""


_VRtrIfNtpBroadcast_Object = MibTableColumn
vRtrIfNtpBroadcast = _VRtrIfNtpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 23),
    _VRtrIfNtpBroadcast_Type()
)
vRtrIfNtpBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfNtpBroadcast.setStatus("current")


class _VRtrIfUnnumbered_Type(IpAddress):
    """Custom type vRtrIfUnnumbered based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfUnnumbered_Object = MibTableColumn
vRtrIfUnnumbered = _VRtrIfUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 24),
    _VRtrIfUnnumbered_Type()
)
vRtrIfUnnumbered.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfUnnumbered.setStatus("current")


class _VRtrIfMtu_Type(Unsigned32):
    """Custom type vRtrIfMtu based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 9000),
    )


_VRtrIfMtu_Type.__name__ = "Unsigned32"
_VRtrIfMtu_Object = MibTableColumn
vRtrIfMtu = _VRtrIfMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 25),
    _VRtrIfMtu_Type()
)
vRtrIfMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfMtu.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfMtu.setUnits("bytes")


class _VRtrIfQosPolicyId_Type(TNetworkPolicyID):
    """Custom type vRtrIfQosPolicyId based on TNetworkPolicyID"""
    defaultValue = 1


_VRtrIfQosPolicyId_Object = MibTableColumn
vRtrIfQosPolicyId = _VRtrIfQosPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 26),
    _VRtrIfQosPolicyId_Type()
)
vRtrIfQosPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfQosPolicyId.setStatus("current")


class _VRtrIfIngressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfIngressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfIngressFilterId_Object = MibTableColumn
vRtrIfIngressFilterId = _VRtrIfIngressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 27),
    _VRtrIfIngressFilterId_Type()
)
vRtrIfIngressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIngressFilterId.setStatus("current")


class _VRtrIfEgressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfEgressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfEgressFilterId_Object = MibTableColumn
vRtrIfEgressFilterId = _VRtrIfEgressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 28),
    _VRtrIfEgressFilterId_Type()
)
vRtrIfEgressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfEgressFilterId.setStatus("current")


class _VRtrIfDirectedBroadcast_Type(TruthValue):
    """Custom type vRtrIfDirectedBroadcast based on TruthValue"""


_VRtrIfDirectedBroadcast_Object = MibTableColumn
vRtrIfDirectedBroadcast = _VRtrIfDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 29),
    _VRtrIfDirectedBroadcast_Type()
)
vRtrIfDirectedBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDirectedBroadcast.setStatus("current")


class _VRtrIfMplsStatus_Type(TmnxStatus):
    """Custom type vRtrIfMplsStatus based on TmnxStatus"""


_VRtrIfMplsStatus_Object = MibTableColumn
vRtrIfMplsStatus = _VRtrIfMplsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 30),
    _VRtrIfMplsStatus_Type()
)
vRtrIfMplsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfMplsStatus.setStatus("current")


class _VRtrIfUnnumberedIf_Type(DisplayString):
    """Custom type vRtrIfUnnumberedIf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrIfUnnumberedIf_Type.__name__ = "DisplayString"
_VRtrIfUnnumberedIf_Object = MibTableColumn
vRtrIfUnnumberedIf = _VRtrIfUnnumberedIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 31),
    _VRtrIfUnnumberedIf_Type()
)
vRtrIfUnnumberedIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfUnnumberedIf.setStatus("current")


class _VRtrIfCflowd_Type(Integer32):
    """Custom type vRtrIfCflowd based on Integer32"""
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
        *(("acl", 2),
          ("interface", 3),
          ("none", 1))
    )


_VRtrIfCflowd_Type.__name__ = "Integer32"
_VRtrIfCflowd_Object = MibTableColumn
vRtrIfCflowd = _VRtrIfCflowd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 32),
    _VRtrIfCflowd_Type()
)
vRtrIfCflowd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfCflowd.setStatus("current")


class _VRtrIfVPNClass_Type(Integer32):
    """Custom type vRtrIfVPNClass based on Integer32"""
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
        *(("carrierOfCarrier", 1),
          ("enterprise", 2),
          ("interProvider", 3),
          ("unknown", 0))
    )


_VRtrIfVPNClass_Type.__name__ = "Integer32"
_VRtrIfVPNClass_Object = MibTableColumn
vRtrIfVPNClass = _VRtrIfVPNClass_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 33),
    _VRtrIfVPNClass_Type()
)
vRtrIfVPNClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfVPNClass.setStatus("current")


class _VRtrIfDescription_Type(TItemLongDescription):
    """Custom type vRtrIfDescription based on TItemLongDescription"""
    defaultHexValue = ""


_VRtrIfDescription_Object = MibTableColumn
vRtrIfDescription = _VRtrIfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 34),
    _VRtrIfDescription_Type()
)
vRtrIfDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDescription.setStatus("current")


class _VRtrIfProtocol_Type(Bits):
    """Custom type vRtrIfProtocol based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 3),
          ("igmp", 7),
          ("isis", 2),
          ("ldp", 6),
          ("mld", 10),
          ("mpls", 4),
          ("ospf3", 9),
          ("ospfv2", 0),
          ("pim", 8),
          ("rip", 1),
          ("rsvp", 5))
    )

_VRtrIfProtocol_Type.__name__ = "Bits"
_VRtrIfProtocol_Object = MibTableColumn
vRtrIfProtocol = _VRtrIfProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 35),
    _VRtrIfProtocol_Type()
)
vRtrIfProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfProtocol.setStatus("current")


class _VRtrIfTosMarkingTrusted_Type(TruthValue):
    """Custom type vRtrIfTosMarkingTrusted based on TruthValue"""


_VRtrIfTosMarkingTrusted_Object = MibTableColumn
vRtrIfTosMarkingTrusted = _VRtrIfTosMarkingTrusted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 36),
    _VRtrIfTosMarkingTrusted_Type()
)
vRtrIfTosMarkingTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfTosMarkingTrusted.setStatus("current")


class _VRtrIfServiceId_Type(TmnxServId):
    """Custom type vRtrIfServiceId based on TmnxServId"""
    defaultValue = 0


_VRtrIfServiceId_Object = MibTableColumn
vRtrIfServiceId = _VRtrIfServiceId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 37),
    _VRtrIfServiceId_Type()
)
vRtrIfServiceId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfServiceId.setStatus("current")


class _VRtrIfArpPopulate_Type(Integer32):
    """Custom type vRtrIfArpPopulate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VRtrIfArpPopulate_Type.__name__ = "Integer32"
_VRtrIfArpPopulate_Object = MibTableColumn
vRtrIfArpPopulate = _VRtrIfArpPopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 38),
    _VRtrIfArpPopulate_Type()
)
vRtrIfArpPopulate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfArpPopulate.setStatus("current")


class _VRtrIfIPv6ConfigAllowed_Type(TruthValue):
    """Custom type vRtrIfIPv6ConfigAllowed based on TruthValue"""


_VRtrIfIPv6ConfigAllowed_Object = MibTableColumn
vRtrIfIPv6ConfigAllowed = _VRtrIfIPv6ConfigAllowed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 39),
    _VRtrIfIPv6ConfigAllowed_Type()
)
vRtrIfIPv6ConfigAllowed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIPv6ConfigAllowed.setStatus("current")
_VRtrIfIPv6OperState_Type = TmnxOperState
_VRtrIfIPv6OperState_Object = MibTableColumn
vRtrIfIPv6OperState = _VRtrIfIPv6OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 40),
    _VRtrIfIPv6OperState_Type()
)
vRtrIfIPv6OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIPv6OperState.setStatus("current")


class _VRtrIfIPv6IngressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfIPv6IngressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfIPv6IngressFilterId_Object = MibTableColumn
vRtrIfIPv6IngressFilterId = _VRtrIfIPv6IngressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 41),
    _VRtrIfIPv6IngressFilterId_Type()
)
vRtrIfIPv6IngressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIPv6IngressFilterId.setStatus("current")


class _VRtrIfIPv6EgressFilterId_Type(TIPFilterID):
    """Custom type vRtrIfIPv6EgressFilterId based on TIPFilterID"""
    defaultValue = 0


_VRtrIfIPv6EgressFilterId_Object = MibTableColumn
vRtrIfIPv6EgressFilterId = _VRtrIfIPv6EgressFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 42),
    _VRtrIfIPv6EgressFilterId_Type()
)
vRtrIfIPv6EgressFilterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIPv6EgressFilterId.setStatus("current")


class _VRtrIfIcmpV6Redirects_Type(TruthValue):
    """Custom type vRtrIfIcmpV6Redirects based on TruthValue"""


_VRtrIfIcmpV6Redirects_Object = MibTableColumn
vRtrIfIcmpV6Redirects = _VRtrIfIcmpV6Redirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 43),
    _VRtrIfIcmpV6Redirects_Type()
)
vRtrIfIcmpV6Redirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6Redirects.setStatus("current")


class _VRtrIfIcmpV6NumRedirects_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumRedirects based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumRedirects_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumRedirects_Object = MibTableColumn
vRtrIfIcmpV6NumRedirects = _VRtrIfIcmpV6NumRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 44),
    _VRtrIfIcmpV6NumRedirects_Type()
)
vRtrIfIcmpV6NumRedirects.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumRedirects.setStatus("current")


class _VRtrIfIcmpV6RedirectsTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6RedirectsTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6RedirectsTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6RedirectsTime_Object = MibTableColumn
vRtrIfIcmpV6RedirectsTime = _VRtrIfIcmpV6RedirectsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 45),
    _VRtrIfIcmpV6RedirectsTime_Type()
)
vRtrIfIcmpV6RedirectsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6RedirectsTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6RedirectsTime.setUnits("seconds")


class _VRtrIfIcmpV6Unreachables_Type(TruthValue):
    """Custom type vRtrIfIcmpV6Unreachables based on TruthValue"""


_VRtrIfIcmpV6Unreachables_Object = MibTableColumn
vRtrIfIcmpV6Unreachables = _VRtrIfIcmpV6Unreachables_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 46),
    _VRtrIfIcmpV6Unreachables_Type()
)
vRtrIfIcmpV6Unreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6Unreachables.setStatus("current")


class _VRtrIfIcmpV6NumUnreachables_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumUnreachables based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumUnreachables_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumUnreachables_Object = MibTableColumn
vRtrIfIcmpV6NumUnreachables = _VRtrIfIcmpV6NumUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 47),
    _VRtrIfIcmpV6NumUnreachables_Type()
)
vRtrIfIcmpV6NumUnreachables.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumUnreachables.setStatus("current")


class _VRtrIfIcmpV6UnreachablesTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6UnreachablesTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6UnreachablesTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6UnreachablesTime_Object = MibTableColumn
vRtrIfIcmpV6UnreachablesTime = _VRtrIfIcmpV6UnreachablesTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 48),
    _VRtrIfIcmpV6UnreachablesTime_Type()
)
vRtrIfIcmpV6UnreachablesTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6UnreachablesTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6UnreachablesTime.setUnits("seconds")


class _VRtrIfIcmpV6TimeExceeded_Type(TruthValue):
    """Custom type vRtrIfIcmpV6TimeExceeded based on TruthValue"""


_VRtrIfIcmpV6TimeExceeded_Object = MibTableColumn
vRtrIfIcmpV6TimeExceeded = _VRtrIfIcmpV6TimeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 49),
    _VRtrIfIcmpV6TimeExceeded_Type()
)
vRtrIfIcmpV6TimeExceeded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6TimeExceeded.setStatus("current")


class _VRtrIfIcmpV6NumTimeExceeded_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumTimeExceeded based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumTimeExceeded_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumTimeExceeded_Object = MibTableColumn
vRtrIfIcmpV6NumTimeExceeded = _VRtrIfIcmpV6NumTimeExceeded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 50),
    _VRtrIfIcmpV6NumTimeExceeded_Type()
)
vRtrIfIcmpV6NumTimeExceeded.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumTimeExceeded.setStatus("current")


class _VRtrIfIcmpV6TimeExceededTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6TimeExceededTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6TimeExceededTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6TimeExceededTime_Object = MibTableColumn
vRtrIfIcmpV6TimeExceededTime = _VRtrIfIcmpV6TimeExceededTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 51),
    _VRtrIfIcmpV6TimeExceededTime_Type()
)
vRtrIfIcmpV6TimeExceededTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6TimeExceededTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6TimeExceededTime.setUnits("seconds")


class _VRtrIfIcmpV6PktTooBig_Type(TruthValue):
    """Custom type vRtrIfIcmpV6PktTooBig based on TruthValue"""


_VRtrIfIcmpV6PktTooBig_Object = MibTableColumn
vRtrIfIcmpV6PktTooBig = _VRtrIfIcmpV6PktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 52),
    _VRtrIfIcmpV6PktTooBig_Type()
)
vRtrIfIcmpV6PktTooBig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6PktTooBig.setStatus("current")


class _VRtrIfIcmpV6NumPktTooBig_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumPktTooBig based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumPktTooBig_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumPktTooBig_Object = MibTableColumn
vRtrIfIcmpV6NumPktTooBig = _VRtrIfIcmpV6NumPktTooBig_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 53),
    _VRtrIfIcmpV6NumPktTooBig_Type()
)
vRtrIfIcmpV6NumPktTooBig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumPktTooBig.setStatus("current")


class _VRtrIfIcmpV6PktTooBigTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6PktTooBigTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6PktTooBigTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6PktTooBigTime_Object = MibTableColumn
vRtrIfIcmpV6PktTooBigTime = _VRtrIfIcmpV6PktTooBigTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 54),
    _VRtrIfIcmpV6PktTooBigTime_Type()
)
vRtrIfIcmpV6PktTooBigTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6PktTooBigTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6PktTooBigTime.setUnits("seconds")


class _VRtrIfIcmpV6ParamProblem_Type(TruthValue):
    """Custom type vRtrIfIcmpV6ParamProblem based on TruthValue"""


_VRtrIfIcmpV6ParamProblem_Object = MibTableColumn
vRtrIfIcmpV6ParamProblem = _VRtrIfIcmpV6ParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 55),
    _VRtrIfIcmpV6ParamProblem_Type()
)
vRtrIfIcmpV6ParamProblem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6ParamProblem.setStatus("current")


class _VRtrIfIcmpV6NumParamProblem_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6NumParamProblem based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_VRtrIfIcmpV6NumParamProblem_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6NumParamProblem_Object = MibTableColumn
vRtrIfIcmpV6NumParamProblem = _VRtrIfIcmpV6NumParamProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 56),
    _VRtrIfIcmpV6NumParamProblem_Type()
)
vRtrIfIcmpV6NumParamProblem.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6NumParamProblem.setStatus("current")


class _VRtrIfIcmpV6ParamProblemTime_Type(Unsigned32):
    """Custom type vRtrIfIcmpV6ParamProblemTime based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_VRtrIfIcmpV6ParamProblemTime_Type.__name__ = "Unsigned32"
_VRtrIfIcmpV6ParamProblemTime_Object = MibTableColumn
vRtrIfIcmpV6ParamProblemTime = _VRtrIfIcmpV6ParamProblemTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 57),
    _VRtrIfIcmpV6ParamProblemTime_Type()
)
vRtrIfIcmpV6ParamProblemTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6ParamProblemTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfIcmpV6ParamProblemTime.setUnits("seconds")
_VRtrIfLinkLocalAddressType_Type = InetAddressType
_VRtrIfLinkLocalAddressType_Object = MibTableColumn
vRtrIfLinkLocalAddressType = _VRtrIfLinkLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 58),
    _VRtrIfLinkLocalAddressType_Type()
)
vRtrIfLinkLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLinkLocalAddressType.setStatus("current")


class _VRtrIfLinkLocalAddress_Type(InetAddress):
    """Custom type vRtrIfLinkLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_VRtrIfLinkLocalAddress_Type.__name__ = "InetAddress"
_VRtrIfLinkLocalAddress_Object = MibTableColumn
vRtrIfLinkLocalAddress = _VRtrIfLinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 59),
    _VRtrIfLinkLocalAddress_Type()
)
vRtrIfLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLinkLocalAddress.setStatus("current")
_VRtrIfLinkLocalAddressState_Type = TmnxInetAddrState
_VRtrIfLinkLocalAddressState_Object = MibTableColumn
vRtrIfLinkLocalAddressState = _VRtrIfLinkLocalAddressState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 60),
    _VRtrIfLinkLocalAddressState_Type()
)
vRtrIfLinkLocalAddressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLinkLocalAddressState.setStatus("current")
_VRtrIfLastOperStateChange_Type = TimeStamp
_VRtrIfLastOperStateChange_Object = MibTableColumn
vRtrIfLastOperStateChange = _VRtrIfLastOperStateChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 61),
    _VRtrIfLastOperStateChange_Type()
)
vRtrIfLastOperStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfLastOperStateChange.setStatus("current")
_VRtrIfOperMtu_Type = Unsigned32
_VRtrIfOperMtu_Object = MibTableColumn
vRtrIfOperMtu = _VRtrIfOperMtu_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 62),
    _VRtrIfOperMtu_Type()
)
vRtrIfOperMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfOperMtu.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfOperMtu.setUnits("bytes")


class _VRtrIfGlobalIndex_Type(Unsigned32):
    """Custom type vRtrIfGlobalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIfGlobalIndex_Type.__name__ = "Unsigned32"
_VRtrIfGlobalIndex_Object = MibTableColumn
vRtrIfGlobalIndex = _VRtrIfGlobalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 63),
    _VRtrIfGlobalIndex_Type()
)
vRtrIfGlobalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfGlobalIndex.setStatus("current")


class _VRtrIfDelaySeconds_Type(Unsigned32):
    """Custom type vRtrIfDelaySeconds based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1200),
    )


_VRtrIfDelaySeconds_Type.__name__ = "Unsigned32"
_VRtrIfDelaySeconds_Object = MibTableColumn
vRtrIfDelaySeconds = _VRtrIfDelaySeconds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 64),
    _VRtrIfDelaySeconds_Type()
)
vRtrIfDelaySeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDelaySeconds.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfDelaySeconds.setUnits("seconds")
_VRtrIfDelayUpTimer_Type = Integer32
_VRtrIfDelayUpTimer_Object = MibTableColumn
vRtrIfDelayUpTimer = _VRtrIfDelayUpTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 65),
    _VRtrIfDelayUpTimer_Type()
)
vRtrIfDelayUpTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDelayUpTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfDelayUpTimer.setUnits("seconds")


class _VRtrIfLocalDhcpServerName_Type(TNamedItemOrEmpty):
    """Custom type vRtrIfLocalDhcpServerName based on TNamedItemOrEmpty"""
    defaultHexValue = ""


_VRtrIfLocalDhcpServerName_Object = MibTableColumn
vRtrIfLocalDhcpServerName = _VRtrIfLocalDhcpServerName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 66),
    _VRtrIfLocalDhcpServerName_Type()
)
vRtrIfLocalDhcpServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfLocalDhcpServerName.setStatus("current")


class _VRtrIfInitDelayEnable_Type(TruthValue):
    """Custom type vRtrIfInitDelayEnable based on TruthValue"""


_VRtrIfInitDelayEnable_Object = MibTableColumn
vRtrIfInitDelayEnable = _VRtrIfInitDelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 67),
    _VRtrIfInitDelayEnable_Type()
)
vRtrIfInitDelayEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfInitDelayEnable.setStatus("current")
_VRtrIfCpmProtPolicyId_Type = TCpmProtPolicyID
_VRtrIfCpmProtPolicyId_Object = MibTableColumn
vRtrIfCpmProtPolicyId = _VRtrIfCpmProtPolicyId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 68),
    _VRtrIfCpmProtPolicyId_Type()
)
vRtrIfCpmProtPolicyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfCpmProtPolicyId.setStatus("current")
_VRtrIfCpmProtUncfgdProtoDropCnt_Type = Gauge32
_VRtrIfCpmProtUncfgdProtoDropCnt_Object = MibTableColumn
vRtrIfCpmProtUncfgdProtoDropCnt = _VRtrIfCpmProtUncfgdProtoDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 69),
    _VRtrIfCpmProtUncfgdProtoDropCnt_Type()
)
vRtrIfCpmProtUncfgdProtoDropCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfCpmProtUncfgdProtoDropCnt.setStatus("current")


class _VRtrIfLdpSyncTimer_Type(Unsigned32):
    """Custom type vRtrIfLdpSyncTimer based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1800),
    )


_VRtrIfLdpSyncTimer_Type.__name__ = "Unsigned32"
_VRtrIfLdpSyncTimer_Object = MibTableColumn
vRtrIfLdpSyncTimer = _VRtrIfLdpSyncTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 4, 1, 70),
    _VRtrIfLdpSyncTimer_Type()
)
vRtrIfLdpSyncTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfLdpSyncTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfLdpSyncTimer.setUnits("seconds")
_VRtrIfNameTable_Object = MibTable
vRtrIfNameTable = _VRtrIfNameTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 5)
)
if mibBuilder.loadTexts:
    vRtrIfNameTable.setStatus("current")
_VRtrIfNameEntry_Object = MibTableRow
vRtrIfNameEntry = _VRtrIfNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 5, 1)
)
vRtrIfNameEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (1, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfName"),
)
if mibBuilder.loadTexts:
    vRtrIfNameEntry.setStatus("current")
_VRtrIfNameIndex_Type = InterfaceIndex
_VRtrIfNameIndex_Object = MibTableColumn
vRtrIfNameIndex = _VRtrIfNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 5, 1, 1),
    _VRtrIfNameIndex_Type()
)
vRtrIfNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfNameIndex.setStatus("current")
_VRtrIpAddrTable_Object = MibTable
vRtrIpAddrTable = _VRtrIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6)
)
if mibBuilder.loadTexts:
    vRtrIpAddrTable.setStatus("current")
_VRtrIpAddrEntry_Object = MibTableRow
vRtrIpAddrEntry = _VRtrIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1)
)
vRtrIpAddrEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaIndex"),
)
if mibBuilder.loadTexts:
    vRtrIpAddrEntry.setStatus("current")


class _VRiaIndex_Type(Integer32):
    """Custom type vRiaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VRiaIndex_Type.__name__ = "Integer32"
_VRiaIndex_Object = MibTableColumn
vRiaIndex = _VRiaIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 1),
    _VRiaIndex_Type()
)
vRiaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRiaIndex.setStatus("current")
_VRiaRowStatus_Type = RowStatus
_VRiaRowStatus_Object = MibTableColumn
vRiaRowStatus = _VRiaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 2),
    _VRiaRowStatus_Type()
)
vRiaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaRowStatus.setStatus("current")
_VRiaIpAddress_Type = IpAddress
_VRiaIpAddress_Object = MibTableColumn
vRiaIpAddress = _VRiaIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 3),
    _VRiaIpAddress_Type()
)
vRiaIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaIpAddress.setStatus("current")


class _VRiaNetMask_Type(IpAddress):
    """Custom type vRiaNetMask based on IpAddress"""
    defaultHexValue = "FFFFFF00"


_VRiaNetMask_Object = MibTableColumn
vRiaNetMask = _VRiaNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 4),
    _VRiaNetMask_Type()
)
vRiaNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaNetMask.setStatus("current")


class _VRiaBcastAddrFormat_Type(Integer32):
    """Custom type vRiaBcastAddrFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 1),
          ("hostOnes", 2))
    )


_VRiaBcastAddrFormat_Type.__name__ = "Integer32"
_VRiaBcastAddrFormat_Object = MibTableColumn
vRiaBcastAddrFormat = _VRiaBcastAddrFormat_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 5),
    _VRiaBcastAddrFormat_Type()
)
vRiaBcastAddrFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaBcastAddrFormat.setStatus("current")


class _VRiaReasmMaxSize_Type(Integer32):
    """Custom type vRiaReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRiaReasmMaxSize_Type.__name__ = "Integer32"
_VRiaReasmMaxSize_Object = MibTableColumn
vRiaReasmMaxSize = _VRiaReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 6),
    _VRiaReasmMaxSize_Type()
)
vRiaReasmMaxSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaReasmMaxSize.setStatus("current")
_VRiaIgpInhibit_Type = TruthValue
_VRiaIgpInhibit_Object = MibTableColumn
vRiaIgpInhibit = _VRiaIgpInhibit_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 7),
    _VRiaIgpInhibit_Type()
)
vRiaIgpInhibit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaIgpInhibit.setStatus("current")
_VRiaInetAddressType_Type = InetAddressType
_VRiaInetAddressType_Object = MibTableColumn
vRiaInetAddressType = _VRiaInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 8),
    _VRiaInetAddressType_Type()
)
vRiaInetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetAddressType.setStatus("current")


class _VRiaInetAddress_Type(InetAddress):
    """Custom type vRiaInetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRiaInetAddress_Type.__name__ = "InetAddress"
_VRiaInetAddress_Object = MibTableColumn
vRiaInetAddress = _VRiaInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 9),
    _VRiaInetAddress_Type()
)
vRiaInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetAddress.setStatus("current")
_VRiaInetPrefixLen_Type = InetAddressPrefixLength
_VRiaInetPrefixLen_Object = MibTableColumn
vRiaInetPrefixLen = _VRiaInetPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 10),
    _VRiaInetPrefixLen_Type()
)
vRiaInetPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetPrefixLen.setStatus("current")
_VRiaInetAddrState_Type = TmnxInetAddrState
_VRiaInetAddrState_Object = MibTableColumn
vRiaInetAddrState = _VRiaInetAddrState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 11),
    _VRiaInetAddrState_Type()
)
vRiaInetAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRiaInetAddrState.setStatus("current")


class _VRiaInetEui64_Type(TruthValue):
    """Custom type vRiaInetEui64 based on TruthValue"""


_VRiaInetEui64_Object = MibTableColumn
vRiaInetEui64 = _VRiaInetEui64_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 12),
    _VRiaInetEui64_Type()
)
vRiaInetEui64.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetEui64.setStatus("current")
_VRiaInetOperAddress_Type = InetAddress
_VRiaInetOperAddress_Object = MibTableColumn
vRiaInetOperAddress = _VRiaInetOperAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 13),
    _VRiaInetOperAddress_Type()
)
vRiaInetOperAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRiaInetOperAddress.setStatus("current")


class _VRiaInetGwAddressType_Type(InetAddressType):
    """Custom type vRiaInetGwAddressType based on InetAddressType"""


_VRiaInetGwAddressType_Object = MibTableColumn
vRiaInetGwAddressType = _VRiaInetGwAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 14),
    _VRiaInetGwAddressType_Type()
)
vRiaInetGwAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetGwAddressType.setStatus("current")


class _VRiaInetGwAddress_Type(InetAddress):
    """Custom type vRiaInetGwAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRiaInetGwAddress_Type.__name__ = "InetAddress"
_VRiaInetGwAddress_Object = MibTableColumn
vRiaInetGwAddress = _VRiaInetGwAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 15),
    _VRiaInetGwAddress_Type()
)
vRiaInetGwAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetGwAddress.setStatus("current")


class _VRiaInetRemoteIpType_Type(InetAddressType):
    """Custom type vRiaInetRemoteIpType based on InetAddressType"""


_VRiaInetRemoteIpType_Object = MibTableColumn
vRiaInetRemoteIpType = _VRiaInetRemoteIpType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 16),
    _VRiaInetRemoteIpType_Type()
)
vRiaInetRemoteIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetRemoteIpType.setStatus("current")


class _VRiaInetRemoteIp_Type(InetAddress):
    """Custom type vRiaInetRemoteIp based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRiaInetRemoteIp_Type.__name__ = "InetAddress"
_VRiaInetRemoteIp_Object = MibTableColumn
vRiaInetRemoteIp = _VRiaInetRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 6, 1, 17),
    _VRiaInetRemoteIp_Type()
)
vRiaInetRemoteIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRiaInetRemoteIp.setStatus("current")
_VRtrIpCidrRouteTable_Object = MibTable
vRtrIpCidrRouteTable = _VRtrIpCidrRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 7)
)
if mibBuilder.loadTexts:
    vRtrIpCidrRouteTable.setStatus("current")
_VRtrIpCidrRouteEntry_Object = MibTableRow
vRtrIpCidrRouteEntry = _VRtrIpCidrRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    vRtrIpCidrRouteEntry.setStatus("current")
_VRtrIpCidrRouteLastEnabledTime_Type = TimeStamp
_VRtrIpCidrRouteLastEnabledTime_Object = MibTableColumn
vRtrIpCidrRouteLastEnabledTime = _VRtrIpCidrRouteLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 7, 1, 1),
    _VRtrIpCidrRouteLastEnabledTime_Type()
)
vRtrIpCidrRouteLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIpCidrRouteLastEnabledTime.setStatus("current")


class _VRtrIpCidrRoutePreference_Type(Unsigned32):
    """Custom type vRtrIpCidrRoutePreference based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrIpCidrRoutePreference_Type.__name__ = "Unsigned32"
_VRtrIpCidrRoutePreference_Object = MibTableColumn
vRtrIpCidrRoutePreference = _VRtrIpCidrRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 7, 1, 2),
    _VRtrIpCidrRoutePreference_Type()
)
vRtrIpCidrRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIpCidrRoutePreference.setStatus("current")
_VRtrIpCidrRouteMetric_Type = Unsigned32
_VRtrIpCidrRouteMetric_Object = MibTableColumn
vRtrIpCidrRouteMetric = _VRtrIpCidrRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 7, 1, 3),
    _VRtrIpCidrRouteMetric_Type()
)
vRtrIpCidrRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIpCidrRouteMetric.setStatus("current")
_VRtrStaticRouteNumber_Type = Unsigned32
_VRtrStaticRouteNumber_Object = MibScalar
vRtrStaticRouteNumber = _VRtrStaticRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 8),
    _VRtrStaticRouteNumber_Type()
)
vRtrStaticRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteNumber.setStatus("current")
_VRtrStaticRouteTable_Object = MibTable
vRtrStaticRouteTable = _VRtrStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    vRtrStaticRouteTable.setStatus("current")
_VRtrStaticRouteEntry_Object = MibTableRow
vRtrStaticRouteEntry = _VRtrStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1)
)
vRtrStaticRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteDest"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteMask"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    vRtrStaticRouteEntry.setStatus("current")
_VRtrStaticRouteDest_Type = IpAddress
_VRtrStaticRouteDest_Object = MibTableColumn
vRtrStaticRouteDest = _VRtrStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 1),
    _VRtrStaticRouteDest_Type()
)
vRtrStaticRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteDest.setStatus("current")
_VRtrStaticRouteMask_Type = IpAddress
_VRtrStaticRouteMask_Object = MibTableColumn
vRtrStaticRouteMask = _VRtrStaticRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 2),
    _VRtrStaticRouteMask_Type()
)
vRtrStaticRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteMask.setStatus("current")


class _VRtrStaticRouteIndex_Type(Integer32):
    """Custom type vRtrStaticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrStaticRouteIndex_Type.__name__ = "Integer32"
_VRtrStaticRouteIndex_Object = MibTableColumn
vRtrStaticRouteIndex = _VRtrStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 3),
    _VRtrStaticRouteIndex_Type()
)
vRtrStaticRouteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteIndex.setStatus("current")
_VRtrStaticRouteRowStatus_Type = RowStatus
_VRtrStaticRouteRowStatus_Object = MibTableColumn
vRtrStaticRouteRowStatus = _VRtrStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 4),
    _VRtrStaticRouteRowStatus_Type()
)
vRtrStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteRowStatus.setStatus("current")
_VRtrStaticRouteLastEnabledTime_Type = TimeStamp
_VRtrStaticRouteLastEnabledTime_Object = MibTableColumn
vRtrStaticRouteLastEnabledTime = _VRtrStaticRouteLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 5),
    _VRtrStaticRouteLastEnabledTime_Type()
)
vRtrStaticRouteLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteLastEnabledTime.setStatus("current")


class _VRtrStaticRouteStatus_Type(Integer32):
    """Custom type vRtrStaticRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_VRtrStaticRouteStatus_Type.__name__ = "Integer32"
_VRtrStaticRouteStatus_Object = MibTableColumn
vRtrStaticRouteStatus = _VRtrStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 6),
    _VRtrStaticRouteStatus_Type()
)
vRtrStaticRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteStatus.setStatus("current")


class _VRtrStaticRouteStaticType_Type(Integer32):
    """Custom type vRtrStaticRouteStaticType based on Integer32"""
    defaultValue = 0

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
        *(("blackHole", 3),
          ("indirect", 2),
          ("nextHop", 1),
          ("unknown", 0))
    )


_VRtrStaticRouteStaticType_Type.__name__ = "Integer32"
_VRtrStaticRouteStaticType_Object = MibTableColumn
vRtrStaticRouteStaticType = _VRtrStaticRouteStaticType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 7),
    _VRtrStaticRouteStaticType_Type()
)
vRtrStaticRouteStaticType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteStaticType.setStatus("current")


class _VRtrStaticRoutePreference_Type(Unsigned32):
    """Custom type vRtrStaticRoutePreference based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_VRtrStaticRoutePreference_Type.__name__ = "Unsigned32"
_VRtrStaticRoutePreference_Object = MibTableColumn
vRtrStaticRoutePreference = _VRtrStaticRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 8),
    _VRtrStaticRoutePreference_Type()
)
vRtrStaticRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRoutePreference.setStatus("current")


class _VRtrStaticRouteMetric_Type(Unsigned32):
    """Custom type vRtrStaticRouteMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrStaticRouteMetric_Type.__name__ = "Unsigned32"
_VRtrStaticRouteMetric_Object = MibTableColumn
vRtrStaticRouteMetric = _VRtrStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 9),
    _VRtrStaticRouteMetric_Type()
)
vRtrStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteMetric.setStatus("current")
_VRtrStaticRouteEgressIfIndex_Type = InterfaceIndexOrZero
_VRtrStaticRouteEgressIfIndex_Object = MibTableColumn
vRtrStaticRouteEgressIfIndex = _VRtrStaticRouteEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 11),
    _VRtrStaticRouteEgressIfIndex_Type()
)
vRtrStaticRouteEgressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteEgressIfIndex.setStatus("current")
_VRtrStaticRouteNextHop_Type = IpAddress
_VRtrStaticRouteNextHop_Object = MibTableColumn
vRtrStaticRouteNextHop = _VRtrStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 12),
    _VRtrStaticRouteNextHop_Type()
)
vRtrStaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteNextHop.setStatus("current")


class _VRtrStaticRouteNextHopUnnumberedIf_Type(DisplayString):
    """Custom type vRtrStaticRouteNextHopUnnumberedIf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrStaticRouteNextHopUnnumberedIf_Type.__name__ = "DisplayString"
_VRtrStaticRouteNextHopUnnumberedIf_Object = MibTableColumn
vRtrStaticRouteNextHopUnnumberedIf = _VRtrStaticRouteNextHopUnnumberedIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 13),
    _VRtrStaticRouteNextHopUnnumberedIf_Type()
)
vRtrStaticRouteNextHopUnnumberedIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteNextHopUnnumberedIf.setStatus("current")


class _VRtrStaticRouteAdminState_Type(TmnxAdminState):
    """Custom type vRtrStaticRouteAdminState based on TmnxAdminState"""


_VRtrStaticRouteAdminState_Object = MibTableColumn
vRtrStaticRouteAdminState = _VRtrStaticRouteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 14),
    _VRtrStaticRouteAdminState_Type()
)
vRtrStaticRouteAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteAdminState.setStatus("current")


class _VRtrStaticRouteIgpShortcut_Type(Bits):
    """Custom type vRtrStaticRouteIgpShortcut based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ip", 2),
          ("ldp", 1),
          ("te", 0))
    )

_VRtrStaticRouteIgpShortcut_Type.__name__ = "Bits"
_VRtrStaticRouteIgpShortcut_Object = MibTableColumn
vRtrStaticRouteIgpShortcut = _VRtrStaticRouteIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 15),
    _VRtrStaticRouteIgpShortcut_Type()
)
vRtrStaticRouteIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteIgpShortcut.setStatus("current")


class _VRtrStaticRouteDisallowIgp_Type(TruthValue):
    """Custom type vRtrStaticRouteDisallowIgp based on TruthValue"""


_VRtrStaticRouteDisallowIgp_Object = MibTableColumn
vRtrStaticRouteDisallowIgp = _VRtrStaticRouteDisallowIgp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 16),
    _VRtrStaticRouteDisallowIgp_Type()
)
vRtrStaticRouteDisallowIgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteDisallowIgp.setStatus("current")


class _VRtrStaticRouteTag_Type(Unsigned32):
    """Custom type vRtrStaticRouteTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrStaticRouteTag_Type.__name__ = "Unsigned32"
_VRtrStaticRouteTag_Object = MibTableColumn
vRtrStaticRouteTag = _VRtrStaticRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 9, 1, 17),
    _VRtrStaticRouteTag_Type()
)
vRtrStaticRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrStaticRouteTag.setStatus("current")
_VRtrSvcIpRangeTable_Object = MibTable
vRtrSvcIpRangeTable = _VRtrSvcIpRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 10)
)
if mibBuilder.loadTexts:
    vRtrSvcIpRangeTable.setStatus("current")
_VRtrSvcIpRangeEntry_Object = MibTableRow
vRtrSvcIpRangeEntry = _VRtrSvcIpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 10, 1)
)
vRtrSvcIpRangeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeAddress"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeMask"),
)
if mibBuilder.loadTexts:
    vRtrSvcIpRangeEntry.setStatus("current")
_VRtrSvcIpRangeAddress_Type = IpAddress
_VRtrSvcIpRangeAddress_Object = MibTableColumn
vRtrSvcIpRangeAddress = _VRtrSvcIpRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 10, 1, 1),
    _VRtrSvcIpRangeAddress_Type()
)
vRtrSvcIpRangeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSvcIpRangeAddress.setStatus("current")


class _VRtrSvcIpRangeMask_Type(Unsigned32):
    """Custom type vRtrSvcIpRangeMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VRtrSvcIpRangeMask_Type.__name__ = "Unsigned32"
_VRtrSvcIpRangeMask_Object = MibTableColumn
vRtrSvcIpRangeMask = _VRtrSvcIpRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 10, 1, 2),
    _VRtrSvcIpRangeMask_Type()
)
vRtrSvcIpRangeMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrSvcIpRangeMask.setStatus("current")
_VRtrSvcIpRangeRowStatus_Type = RowStatus
_VRtrSvcIpRangeRowStatus_Object = MibTableColumn
vRtrSvcIpRangeRowStatus = _VRtrSvcIpRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 10, 1, 3),
    _VRtrSvcIpRangeRowStatus_Type()
)
vRtrSvcIpRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSvcIpRangeRowStatus.setStatus("current")


class _VRtrSvcIpRangeExclusive_Type(TruthValue):
    """Custom type vRtrSvcIpRangeExclusive based on TruthValue"""


_VRtrSvcIpRangeExclusive_Object = MibTableColumn
vRtrSvcIpRangeExclusive = _VRtrSvcIpRangeExclusive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 10, 1, 4),
    _VRtrSvcIpRangeExclusive_Type()
)
vRtrSvcIpRangeExclusive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrSvcIpRangeExclusive.setStatus("current")
_VRtrIpNetToMediaTable_Object = MibTable
vRtrIpNetToMediaTable = _VRtrIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 11)
)
if mibBuilder.loadTexts:
    vRtrIpNetToMediaTable.setStatus("current")
_VRtrIpNetToMediaEntry_Object = MibTableRow
vRtrIpNetToMediaEntry = _VRtrIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 11, 1)
)
if mibBuilder.loadTexts:
    vRtrIpNetToMediaEntry.setStatus("current")


class _VRtrIpNetToMediaTimer_Type(Unsigned32):
    """Custom type vRtrIpNetToMediaTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIpNetToMediaTimer_Type.__name__ = "Unsigned32"
_VRtrIpNetToMediaTimer_Object = MibTableColumn
vRtrIpNetToMediaTimer = _VRtrIpNetToMediaTimer_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 11, 1, 1),
    _VRtrIpNetToMediaTimer_Type()
)
vRtrIpNetToMediaTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIpNetToMediaTimer.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIpNetToMediaTimer.setUnits("seconds")
_VRtrIpNetToMediaOperState_Type = TmnxOperState
_VRtrIpNetToMediaOperState_Object = MibTableColumn
vRtrIpNetToMediaOperState = _VRtrIpNetToMediaOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 11, 1, 2),
    _VRtrIpNetToMediaOperState_Type()
)
vRtrIpNetToMediaOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIpNetToMediaOperState.setStatus("current")
_VRtrInstanceAggregationTableLastChanged_Type = TimeStamp
_VRtrInstanceAggregationTableLastChanged_Object = MibScalar
vRtrInstanceAggregationTableLastChanged = _VRtrInstanceAggregationTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 12),
    _VRtrInstanceAggregationTableLastChanged_Type()
)
vRtrInstanceAggregationTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInstanceAggregationTableLastChanged.setStatus("current")
_VRtrInstanceAggregationTable_Object = MibTable
vRtrInstanceAggregationTable = _VRtrInstanceAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13)
)
if mibBuilder.loadTexts:
    vRtrInstanceAggregationTable.setStatus("current")
_VRtrInstanceAggregationEntry_Object = MibTableRow
vRtrInstanceAggregationEntry = _VRtrInstanceAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1)
)
vRtrInstanceAggregationEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationIpPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationIpPrefixMask"),
)
if mibBuilder.loadTexts:
    vRtrInstanceAggregationEntry.setStatus("current")
_VRtrAggregationIpPrefix_Type = IpAddress
_VRtrAggregationIpPrefix_Object = MibTableColumn
vRtrAggregationIpPrefix = _VRtrAggregationIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 1),
    _VRtrAggregationIpPrefix_Type()
)
vRtrAggregationIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrAggregationIpPrefix.setStatus("current")
_VRtrAggregationIpPrefixMask_Type = IpAddressPrefixLength
_VRtrAggregationIpPrefixMask_Object = MibTableColumn
vRtrAggregationIpPrefixMask = _VRtrAggregationIpPrefixMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 2),
    _VRtrAggregationIpPrefixMask_Type()
)
vRtrAggregationIpPrefixMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrAggregationIpPrefixMask.setStatus("current")
_VRtrAggregationRowStatus_Type = RowStatus
_VRtrAggregationRowStatus_Object = MibTableColumn
vRtrAggregationRowStatus = _VRtrAggregationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 3),
    _VRtrAggregationRowStatus_Type()
)
vRtrAggregationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAggregationRowStatus.setStatus("current")
_VRtrAggregationLastChanged_Type = TimeStamp
_VRtrAggregationLastChanged_Object = MibTableColumn
vRtrAggregationLastChanged = _VRtrAggregationLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 4),
    _VRtrAggregationLastChanged_Type()
)
vRtrAggregationLastChanged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAggregationLastChanged.setStatus("current")


class _VRtrAggregationSummaryOnly_Type(TruthValue):
    """Custom type vRtrAggregationSummaryOnly based on TruthValue"""


_VRtrAggregationSummaryOnly_Object = MibTableColumn
vRtrAggregationSummaryOnly = _VRtrAggregationSummaryOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 5),
    _VRtrAggregationSummaryOnly_Type()
)
vRtrAggregationSummaryOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAggregationSummaryOnly.setStatus("current")


class _VRtrAggregationASSet_Type(TruthValue):
    """Custom type vRtrAggregationASSet based on TruthValue"""


_VRtrAggregationASSet_Object = MibTableColumn
vRtrAggregationASSet = _VRtrAggregationASSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 6),
    _VRtrAggregationASSet_Type()
)
vRtrAggregationASSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAggregationASSet.setStatus("current")


class _VRtrAggregationAggregatorAS_Type(TmnxBgpAutonomousSystem):
    """Custom type vRtrAggregationAggregatorAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_VRtrAggregationAggregatorAS_Object = MibTableColumn
vRtrAggregationAggregatorAS = _VRtrAggregationAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 7),
    _VRtrAggregationAggregatorAS_Type()
)
vRtrAggregationAggregatorAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAggregationAggregatorAS.setStatus("current")


class _VRtrAggregationAggregatorIPAddr_Type(IpAddress):
    """Custom type vRtrAggregationAggregatorIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrAggregationAggregatorIPAddr_Object = MibTableColumn
vRtrAggregationAggregatorIPAddr = _VRtrAggregationAggregatorIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 8),
    _VRtrAggregationAggregatorIPAddr_Type()
)
vRtrAggregationAggregatorIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAggregationAggregatorIPAddr.setStatus("current")
_VRtrAggregationOperState_Type = TmnxOperState
_VRtrAggregationOperState_Object = MibTableColumn
vRtrAggregationOperState = _VRtrAggregationOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 13, 1, 9),
    _VRtrAggregationOperState_Type()
)
vRtrAggregationOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrAggregationOperState.setStatus("current")
_VRtrStaticRouteIndexTable_Object = MibTable
vRtrStaticRouteIndexTable = _VRtrStaticRouteIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 14)
)
if mibBuilder.loadTexts:
    vRtrStaticRouteIndexTable.setStatus("current")
_VRtrStaticRouteIndexEntry_Object = MibTableRow
vRtrStaticRouteIndexEntry = _VRtrStaticRouteIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 14, 1)
)
vRtrStaticRouteIndexEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndexDest"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndexMask"),
)
if mibBuilder.loadTexts:
    vRtrStaticRouteIndexEntry.setStatus("current")
_VRtrStaticRouteIndexDest_Type = IpAddress
_VRtrStaticRouteIndexDest_Object = MibTableColumn
vRtrStaticRouteIndexDest = _VRtrStaticRouteIndexDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 14, 1, 1),
    _VRtrStaticRouteIndexDest_Type()
)
vRtrStaticRouteIndexDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteIndexDest.setStatus("current")
_VRtrStaticRouteIndexMask_Type = IpAddress
_VRtrStaticRouteIndexMask_Object = MibTableColumn
vRtrStaticRouteIndexMask = _VRtrStaticRouteIndexMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 14, 1, 2),
    _VRtrStaticRouteIndexMask_Type()
)
vRtrStaticRouteIndexMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteIndexMask.setStatus("current")


class _VRtrStaticRouteAvailableIndex_Type(TestAndIncr):
    """Custom type vRtrStaticRouteAvailableIndex based on TestAndIncr"""
    subtypeSpec = TestAndIncr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrStaticRouteAvailableIndex_Type.__name__ = "TestAndIncr"
_VRtrStaticRouteAvailableIndex_Object = MibTableColumn
vRtrStaticRouteAvailableIndex = _VRtrStaticRouteAvailableIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 14, 1, 3),
    _VRtrStaticRouteAvailableIndex_Type()
)
vRtrStaticRouteAvailableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrStaticRouteAvailableIndex.setStatus("current")
_TmnxVRtrGlobalObjs_ObjectIdentity = ObjectIdentity
tmnxVRtrGlobalObjs = _TmnxVRtrGlobalObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 15)
)
_VRtrNextVRtrID_Type = TestAndIncr
_VRtrNextVRtrID_Object = MibScalar
vRtrNextVRtrID = _VRtrNextVRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 15, 1),
    _VRtrNextVRtrID_Type()
)
vRtrNextVRtrID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrNextVRtrID.setStatus("current")
_VRtrConfiguredVRtrs_Type = Gauge32
_VRtrConfiguredVRtrs_Object = MibScalar
vRtrConfiguredVRtrs = _VRtrConfiguredVRtrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 15, 2),
    _VRtrConfiguredVRtrs_Type()
)
vRtrConfiguredVRtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrConfiguredVRtrs.setStatus("current")
_VRtrActiveVRtrs_Type = Gauge32
_VRtrActiveVRtrs_Object = MibScalar
vRtrActiveVRtrs = _VRtrActiveVRtrs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 15, 3),
    _VRtrActiveVRtrs_Type()
)
vRtrActiveVRtrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrActiveVRtrs.setStatus("current")


class _VRtrRouteThresholdSoakTime_Type(Unsigned32):
    """Custom type vRtrRouteThresholdSoakTime based on Unsigned32"""
    defaultValue = 600


_VRtrRouteThresholdSoakTime_Object = MibScalar
vRtrRouteThresholdSoakTime = _VRtrRouteThresholdSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 15, 4),
    _VRtrRouteThresholdSoakTime_Type()
)
vRtrRouteThresholdSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrRouteThresholdSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrRouteThresholdSoakTime.setUnits("seconds")
_VRtrMaxARPEntries_Type = Unsigned32
_VRtrMaxARPEntries_Object = MibScalar
vRtrMaxARPEntries = _VRtrMaxARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 15, 5),
    _VRtrMaxARPEntries_Type()
)
vRtrMaxARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrMaxARPEntries.setStatus("current")


class _VRtrIPv6RouteThresholdSoakTime_Type(Unsigned32):
    """Custom type vRtrIPv6RouteThresholdSoakTime based on Unsigned32"""
    defaultValue = 600


_VRtrIPv6RouteThresholdSoakTime_Object = MibScalar
vRtrIPv6RouteThresholdSoakTime = _VRtrIPv6RouteThresholdSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 15, 6),
    _VRtrIPv6RouteThresholdSoakTime_Type()
)
vRtrIPv6RouteThresholdSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIPv6RouteThresholdSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIPv6RouteThresholdSoakTime.setUnits("seconds")
_VRtrPolicyTable_Object = MibTable
vRtrPolicyTable = _VRtrPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16)
)
if mibBuilder.loadTexts:
    vRtrPolicyTable.setStatus("current")
_VRtrPolicyEntry_Object = MibTableRow
vRtrPolicyEntry = _VRtrPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1)
)
if mibBuilder.loadTexts:
    vRtrPolicyEntry.setStatus("current")


class _VRtrImportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrImportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrImportPolicy1_Object = MibTableColumn
vRtrImportPolicy1 = _VRtrImportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 1),
    _VRtrImportPolicy1_Type()
)
vRtrImportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrImportPolicy1.setStatus("current")


class _VRtrImportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrImportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrImportPolicy2_Object = MibTableColumn
vRtrImportPolicy2 = _VRtrImportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 2),
    _VRtrImportPolicy2_Type()
)
vRtrImportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrImportPolicy2.setStatus("current")


class _VRtrImportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrImportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrImportPolicy3_Object = MibTableColumn
vRtrImportPolicy3 = _VRtrImportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 3),
    _VRtrImportPolicy3_Type()
)
vRtrImportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrImportPolicy3.setStatus("current")


class _VRtrImportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrImportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrImportPolicy4_Object = MibTableColumn
vRtrImportPolicy4 = _VRtrImportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 4),
    _VRtrImportPolicy4_Type()
)
vRtrImportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrImportPolicy4.setStatus("current")


class _VRtrImportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrImportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrImportPolicy5_Object = MibTableColumn
vRtrImportPolicy5 = _VRtrImportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 5),
    _VRtrImportPolicy5_Type()
)
vRtrImportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrImportPolicy5.setStatus("current")


class _VRtrExportPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrExportPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrExportPolicy1_Object = MibTableColumn
vRtrExportPolicy1 = _VRtrExportPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 6),
    _VRtrExportPolicy1_Type()
)
vRtrExportPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrExportPolicy1.setStatus("current")


class _VRtrExportPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrExportPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrExportPolicy2_Object = MibTableColumn
vRtrExportPolicy2 = _VRtrExportPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 7),
    _VRtrExportPolicy2_Type()
)
vRtrExportPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrExportPolicy2.setStatus("current")


class _VRtrExportPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrExportPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrExportPolicy3_Object = MibTableColumn
vRtrExportPolicy3 = _VRtrExportPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 8),
    _VRtrExportPolicy3_Type()
)
vRtrExportPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrExportPolicy3.setStatus("current")


class _VRtrExportPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrExportPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrExportPolicy4_Object = MibTableColumn
vRtrExportPolicy4 = _VRtrExportPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 9),
    _VRtrExportPolicy4_Type()
)
vRtrExportPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrExportPolicy4.setStatus("current")


class _VRtrExportPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrExportPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrExportPolicy5_Object = MibTableColumn
vRtrExportPolicy5 = _VRtrExportPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 16, 1, 10),
    _VRtrExportPolicy5_Type()
)
vRtrExportPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrExportPolicy5.setStatus("current")
_VRtrTunnelTable_Object = MibTable
vRtrTunnelTable = _VRtrTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17)
)
if mibBuilder.loadTexts:
    vRtrTunnelTable.setStatus("current")
_VRtrTunnelEntry_Object = MibTableRow
vRtrTunnelEntry = _VRtrTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1)
)
vRtrTunnelEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelDest"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelMask"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelPreference"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelNexthop"),
)
if mibBuilder.loadTexts:
    vRtrTunnelEntry.setStatus("current")
_VRtrTunnelDest_Type = IpAddress
_VRtrTunnelDest_Object = MibTableColumn
vRtrTunnelDest = _VRtrTunnelDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 1),
    _VRtrTunnelDest_Type()
)
vRtrTunnelDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTunnelDest.setStatus("current")
_VRtrTunnelMask_Type = IpAddress
_VRtrTunnelMask_Object = MibTableColumn
vRtrTunnelMask = _VRtrTunnelMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 2),
    _VRtrTunnelMask_Type()
)
vRtrTunnelMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTunnelMask.setStatus("current")


class _VRtrTunnelPreference_Type(Unsigned32):
    """Custom type vRtrTunnelPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrTunnelPreference_Type.__name__ = "Unsigned32"
_VRtrTunnelPreference_Object = MibTableColumn
vRtrTunnelPreference = _VRtrTunnelPreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 3),
    _VRtrTunnelPreference_Type()
)
vRtrTunnelPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTunnelPreference.setStatus("current")
_VRtrTunnelType_Type = TmnxTunnelType
_VRtrTunnelType_Object = MibTableColumn
vRtrTunnelType = _VRtrTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 4),
    _VRtrTunnelType_Type()
)
vRtrTunnelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTunnelType.setStatus("current")
_VRtrTunnelID_Type = TmnxTunnelID
_VRtrTunnelID_Object = MibTableColumn
vRtrTunnelID = _VRtrTunnelID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 5),
    _VRtrTunnelID_Type()
)
vRtrTunnelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTunnelID.setStatus("current")
_VRtrTunnelNexthop_Type = IpAddress
_VRtrTunnelNexthop_Object = MibTableColumn
vRtrTunnelNexthop = _VRtrTunnelNexthop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 6),
    _VRtrTunnelNexthop_Type()
)
vRtrTunnelNexthop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrTunnelNexthop.setStatus("current")
_VRtrTunnelMetric_Type = Unsigned32
_VRtrTunnelMetric_Object = MibTableColumn
vRtrTunnelMetric = _VRtrTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 7),
    _VRtrTunnelMetric_Type()
)
vRtrTunnelMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTunnelMetric.setStatus("current")
_VRtrTunnelAge_Type = Integer32
_VRtrTunnelAge_Object = MibTableColumn
vRtrTunnelAge = _VRtrTunnelAge_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 17, 1, 8),
    _VRtrTunnelAge_Type()
)
vRtrTunnelAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrTunnelAge.setStatus("current")
_VRtrIfProxyArpTable_Object = MibTable
vRtrIfProxyArpTable = _VRtrIfProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18)
)
if mibBuilder.loadTexts:
    vRtrIfProxyArpTable.setStatus("current")
_VRtrIfProxyArpEntry_Object = MibTableRow
vRtrIfProxyArpEntry = _VRtrIfProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1)
)
if mibBuilder.loadTexts:
    vRtrIfProxyArpEntry.setStatus("current")


class _VRtrIfProxyArp_Type(TruthValue):
    """Custom type vRtrIfProxyArp based on TruthValue"""


_VRtrIfProxyArp_Object = MibTableColumn
vRtrIfProxyArp = _VRtrIfProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1, 1),
    _VRtrIfProxyArp_Type()
)
vRtrIfProxyArp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyArp.setStatus("current")


class _VRtrIfProxyArpLocal_Type(TruthValue):
    """Custom type vRtrIfProxyArpLocal based on TruthValue"""


_VRtrIfProxyArpLocal_Object = MibTableColumn
vRtrIfProxyArpLocal = _VRtrIfProxyArpLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1, 2),
    _VRtrIfProxyArpLocal_Type()
)
vRtrIfProxyArpLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyArpLocal.setStatus("current")


class _VRtrIfProxyArpPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyArpPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyArpPolicy1_Object = MibTableColumn
vRtrIfProxyArpPolicy1 = _VRtrIfProxyArpPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1, 3),
    _VRtrIfProxyArpPolicy1_Type()
)
vRtrIfProxyArpPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyArpPolicy1.setStatus("current")


class _VRtrIfProxyArpPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyArpPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyArpPolicy2_Object = MibTableColumn
vRtrIfProxyArpPolicy2 = _VRtrIfProxyArpPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1, 4),
    _VRtrIfProxyArpPolicy2_Type()
)
vRtrIfProxyArpPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyArpPolicy2.setStatus("current")


class _VRtrIfProxyArpPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyArpPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyArpPolicy3_Object = MibTableColumn
vRtrIfProxyArpPolicy3 = _VRtrIfProxyArpPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1, 5),
    _VRtrIfProxyArpPolicy3_Type()
)
vRtrIfProxyArpPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyArpPolicy3.setStatus("current")


class _VRtrIfProxyArpPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyArpPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyArpPolicy4_Object = MibTableColumn
vRtrIfProxyArpPolicy4 = _VRtrIfProxyArpPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1, 6),
    _VRtrIfProxyArpPolicy4_Type()
)
vRtrIfProxyArpPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyArpPolicy4.setStatus("current")


class _VRtrIfProxyArpPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyArpPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyArpPolicy5_Object = MibTableColumn
vRtrIfProxyArpPolicy5 = _VRtrIfProxyArpPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 18, 1, 7),
    _VRtrIfProxyArpPolicy5_Type()
)
vRtrIfProxyArpPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyArpPolicy5.setStatus("current")
_VRtrIfDHCPTable_Object = MibTable
vRtrIfDHCPTable = _VRtrIfDHCPTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19)
)
if mibBuilder.loadTexts:
    vRtrIfDHCPTable.setStatus("current")
_VRtrIfDHCPEntry_Object = MibTableRow
vRtrIfDHCPEntry = _VRtrIfDHCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1)
)
if mibBuilder.loadTexts:
    vRtrIfDHCPEntry.setStatus("current")


class _VRtrIfDHCPRelayInfoOption_Type(TruthValue):
    """Custom type vRtrIfDHCPRelayInfoOption based on TruthValue"""


_VRtrIfDHCPRelayInfoOption_Object = MibTableColumn
vRtrIfDHCPRelayInfoOption = _VRtrIfDHCPRelayInfoOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 1),
    _VRtrIfDHCPRelayInfoOption_Type()
)
vRtrIfDHCPRelayInfoOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayInfoOption.setStatus("obsolete")


class _VRtrIfDHCPRelayInfoAction_Type(Integer32):
    """Custom type vRtrIfDHCPRelayInfoAction based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )


_VRtrIfDHCPRelayInfoAction_Type.__name__ = "Integer32"
_VRtrIfDHCPRelayInfoAction_Object = MibTableColumn
vRtrIfDHCPRelayInfoAction = _VRtrIfDHCPRelayInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 2),
    _VRtrIfDHCPRelayInfoAction_Type()
)
vRtrIfDHCPRelayInfoAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayInfoAction.setStatus("current")


class _VRtrIfDHCPRelayCircuitId_Type(Integer32):
    """Custom type vRtrIfDHCPRelayCircuitId based on Integer32"""
    defaultValue = 2

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
        *(("asciiTuple", 2),
          ("ifIndex", 1),
          ("none", 0),
          ("sapId", 3),
          ("vlanAsciiTuple", 4))
    )


_VRtrIfDHCPRelayCircuitId_Type.__name__ = "Integer32"
_VRtrIfDHCPRelayCircuitId_Object = MibTableColumn
vRtrIfDHCPRelayCircuitId = _VRtrIfDHCPRelayCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 3),
    _VRtrIfDHCPRelayCircuitId_Type()
)
vRtrIfDHCPRelayCircuitId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayCircuitId.setStatus("current")


class _VRtrIfDHCPRelayRemoteId_Type(Integer32):
    """Custom type vRtrIfDHCPRelayRemoteId based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("none", 2),
          ("remote-id", 3))
    )


_VRtrIfDHCPRelayRemoteId_Type.__name__ = "Integer32"
_VRtrIfDHCPRelayRemoteId_Object = MibTableColumn
vRtrIfDHCPRelayRemoteId = _VRtrIfDHCPRelayRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 4),
    _VRtrIfDHCPRelayRemoteId_Type()
)
vRtrIfDHCPRelayRemoteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayRemoteId.setStatus("current")


class _VRtrIfDHCPAutoFilter_Type(Unsigned32):
    """Custom type vRtrIfDHCPAutoFilter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_VRtrIfDHCPAutoFilter_Type.__name__ = "Unsigned32"
_VRtrIfDHCPAutoFilter_Object = MibTableColumn
vRtrIfDHCPAutoFilter = _VRtrIfDHCPAutoFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 5),
    _VRtrIfDHCPAutoFilter_Type()
)
vRtrIfDHCPAutoFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPAutoFilter.setStatus("obsolete")


class _VRtrIfDHCPRelayServer1_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer1 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer1_Object = MibTableColumn
vRtrIfDHCPRelayServer1 = _VRtrIfDHCPRelayServer1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 6),
    _VRtrIfDHCPRelayServer1_Type()
)
vRtrIfDHCPRelayServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer1.setStatus("current")


class _VRtrIfDHCPRelayServer2_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer2 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer2_Object = MibTableColumn
vRtrIfDHCPRelayServer2 = _VRtrIfDHCPRelayServer2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 7),
    _VRtrIfDHCPRelayServer2_Type()
)
vRtrIfDHCPRelayServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer2.setStatus("current")


class _VRtrIfDHCPRelayServer3_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer3 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer3_Object = MibTableColumn
vRtrIfDHCPRelayServer3 = _VRtrIfDHCPRelayServer3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 8),
    _VRtrIfDHCPRelayServer3_Type()
)
vRtrIfDHCPRelayServer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer3.setStatus("current")


class _VRtrIfDHCPRelayServer4_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer4 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer4_Object = MibTableColumn
vRtrIfDHCPRelayServer4 = _VRtrIfDHCPRelayServer4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 9),
    _VRtrIfDHCPRelayServer4_Type()
)
vRtrIfDHCPRelayServer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer4.setStatus("current")


class _VRtrIfDHCPRelayServer5_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer5 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer5_Object = MibTableColumn
vRtrIfDHCPRelayServer5 = _VRtrIfDHCPRelayServer5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 10),
    _VRtrIfDHCPRelayServer5_Type()
)
vRtrIfDHCPRelayServer5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer5.setStatus("current")


class _VRtrIfDHCPRelayServer6_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer6 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer6_Object = MibTableColumn
vRtrIfDHCPRelayServer6 = _VRtrIfDHCPRelayServer6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 11),
    _VRtrIfDHCPRelayServer6_Type()
)
vRtrIfDHCPRelayServer6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer6.setStatus("current")


class _VRtrIfDHCPRelayServer7_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer7 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer7_Object = MibTableColumn
vRtrIfDHCPRelayServer7 = _VRtrIfDHCPRelayServer7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 12),
    _VRtrIfDHCPRelayServer7_Type()
)
vRtrIfDHCPRelayServer7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer7.setStatus("current")


class _VRtrIfDHCPRelayServer8_Type(IpAddress):
    """Custom type vRtrIfDHCPRelayServer8 based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPRelayServer8_Object = MibTableColumn
vRtrIfDHCPRelayServer8 = _VRtrIfDHCPRelayServer8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 13),
    _VRtrIfDHCPRelayServer8_Type()
)
vRtrIfDHCPRelayServer8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServer8.setStatus("current")


class _VRtrIfDHCPRelayTrusted_Type(TruthValue):
    """Custom type vRtrIfDHCPRelayTrusted based on TruthValue"""


_VRtrIfDHCPRelayTrusted_Object = MibTableColumn
vRtrIfDHCPRelayTrusted = _VRtrIfDHCPRelayTrusted_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 14),
    _VRtrIfDHCPRelayTrusted_Type()
)
vRtrIfDHCPRelayTrusted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayTrusted.setStatus("current")


class _VRtrIfDHCPAdminState_Type(TmnxAdminState):
    """Custom type vRtrIfDHCPAdminState based on TmnxAdminState"""


_VRtrIfDHCPAdminState_Object = MibTableColumn
vRtrIfDHCPAdminState = _VRtrIfDHCPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 15),
    _VRtrIfDHCPAdminState_Type()
)
vRtrIfDHCPAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPAdminState.setStatus("current")


class _VRtrIfDHCPSnooping_Type(Integer32):
    """Custom type vRtrIfDHCPSnooping based on Integer32"""
    defaultValue = 2

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


_VRtrIfDHCPSnooping_Type.__name__ = "Integer32"
_VRtrIfDHCPSnooping_Object = MibTableColumn
vRtrIfDHCPSnooping = _VRtrIfDHCPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 16),
    _VRtrIfDHCPSnooping_Type()
)
vRtrIfDHCPSnooping.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPSnooping.setStatus("obsolete")


class _VRtrIfDHCPDescription_Type(TItemDescription):
    """Custom type vRtrIfDHCPDescription based on TItemDescription"""
    defaultHexValue = ""


_VRtrIfDHCPDescription_Object = MibTableColumn
vRtrIfDHCPDescription = _VRtrIfDHCPDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 17),
    _VRtrIfDHCPDescription_Type()
)
vRtrIfDHCPDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPDescription.setStatus("current")
_VRtrIfDHCPAutoFilterId_Type = TFilterID
_VRtrIfDHCPAutoFilterId_Object = MibTableColumn
vRtrIfDHCPAutoFilterId = _VRtrIfDHCPAutoFilterId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 18),
    _VRtrIfDHCPAutoFilterId_Type()
)
vRtrIfDHCPAutoFilterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPAutoFilterId.setStatus("obsolete")


class _VRtrIfDHCPOperAutoFilter_Type(Unsigned32):
    """Custom type vRtrIfDHCPOperAutoFilter based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_VRtrIfDHCPOperAutoFilter_Type.__name__ = "Unsigned32"
_VRtrIfDHCPOperAutoFilter_Object = MibTableColumn
vRtrIfDHCPOperAutoFilter = _VRtrIfDHCPOperAutoFilter_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 19),
    _VRtrIfDHCPOperAutoFilter_Type()
)
vRtrIfDHCPOperAutoFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPOperAutoFilter.setStatus("obsolete")


class _VRtrIfDHCPAuthPolicy_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfDHCPAuthPolicy based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfDHCPAuthPolicy_Object = MibTableColumn
vRtrIfDHCPAuthPolicy = _VRtrIfDHCPAuthPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 20),
    _VRtrIfDHCPAuthPolicy_Type()
)
vRtrIfDHCPAuthPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPAuthPolicy.setStatus("current")


class _VRtrIfDHCPLeasePopulate_Type(Unsigned32):
    """Custom type vRtrIfDHCPLeasePopulate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VRtrIfDHCPLeasePopulate_Type.__name__ = "Unsigned32"
_VRtrIfDHCPLeasePopulate_Object = MibTableColumn
vRtrIfDHCPLeasePopulate = _VRtrIfDHCPLeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 21),
    _VRtrIfDHCPLeasePopulate_Type()
)
vRtrIfDHCPLeasePopulate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPLeasePopulate.setStatus("current")


class _VRtrIfDHCPOperLeasePopulate_Type(Unsigned32):
    """Custom type vRtrIfDHCPOperLeasePopulate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VRtrIfDHCPOperLeasePopulate_Type.__name__ = "Unsigned32"
_VRtrIfDHCPOperLeasePopulate_Object = MibTableColumn
vRtrIfDHCPOperLeasePopulate = _VRtrIfDHCPOperLeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 22),
    _VRtrIfDHCPOperLeasePopulate_Type()
)
vRtrIfDHCPOperLeasePopulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPOperLeasePopulate.setStatus("current")


class _VRtrIfDHCPGiAddressType_Type(InetAddressType):
    """Custom type vRtrIfDHCPGiAddressType based on InetAddressType"""


_VRtrIfDHCPGiAddressType_Object = MibTableColumn
vRtrIfDHCPGiAddressType = _VRtrIfDHCPGiAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 23),
    _VRtrIfDHCPGiAddressType_Type()
)
vRtrIfDHCPGiAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPGiAddressType.setStatus("current")


class _VRtrIfDHCPGiAddress_Type(InetAddress):
    """Custom type vRtrIfDHCPGiAddress based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrIfDHCPGiAddress_Type.__name__ = "InetAddress"
_VRtrIfDHCPGiAddress_Object = MibTableColumn
vRtrIfDHCPGiAddress = _VRtrIfDHCPGiAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 24),
    _VRtrIfDHCPGiAddress_Type()
)
vRtrIfDHCPGiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPGiAddress.setStatus("current")


class _VRtrIfDHCPGiAddressAsSrc_Type(TruthValue):
    """Custom type vRtrIfDHCPGiAddressAsSrc based on TruthValue"""


_VRtrIfDHCPGiAddressAsSrc_Object = MibTableColumn
vRtrIfDHCPGiAddressAsSrc = _VRtrIfDHCPGiAddressAsSrc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 25),
    _VRtrIfDHCPGiAddressAsSrc_Type()
)
vRtrIfDHCPGiAddressAsSrc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPGiAddressAsSrc.setStatus("current")


class _VRtrIfDHCPMatchOption82_Type(TruthValue):
    """Custom type vRtrIfDHCPMatchOption82 based on TruthValue"""


_VRtrIfDHCPMatchOption82_Object = MibTableColumn
vRtrIfDHCPMatchOption82 = _VRtrIfDHCPMatchOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 26),
    _VRtrIfDHCPMatchOption82_Type()
)
vRtrIfDHCPMatchOption82.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPMatchOption82.setStatus("current")


class _VRtrIfDHCPRelayRemoteIdStr_Type(DisplayString):
    """Custom type vRtrIfDHCPRelayRemoteIdStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrIfDHCPRelayRemoteIdStr_Type.__name__ = "DisplayString"
_VRtrIfDHCPRelayRemoteIdStr_Object = MibTableColumn
vRtrIfDHCPRelayRemoteIdStr = _VRtrIfDHCPRelayRemoteIdStr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 27),
    _VRtrIfDHCPRelayRemoteIdStr_Type()
)
vRtrIfDHCPRelayRemoteIdStr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayRemoteIdStr.setStatus("current")


class _VRtrIfDHCPProxyAdminState_Type(TmnxAdminState):
    """Custom type vRtrIfDHCPProxyAdminState based on TmnxAdminState"""


_VRtrIfDHCPProxyAdminState_Object = MibTableColumn
vRtrIfDHCPProxyAdminState = _VRtrIfDHCPProxyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 28),
    _VRtrIfDHCPProxyAdminState_Type()
)
vRtrIfDHCPProxyAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPProxyAdminState.setStatus("current")


class _VRtrIfDHCPProxyServerAddr_Type(IpAddress):
    """Custom type vRtrIfDHCPProxyServerAddr based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrIfDHCPProxyServerAddr_Object = MibTableColumn
vRtrIfDHCPProxyServerAddr = _VRtrIfDHCPProxyServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 29),
    _VRtrIfDHCPProxyServerAddr_Type()
)
vRtrIfDHCPProxyServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPProxyServerAddr.setStatus("current")


class _VRtrIfDHCPProxyLeaseTime_Type(Unsigned32):
    """Custom type vRtrIfDHCPProxyLeaseTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(300, 315446399),
    )


_VRtrIfDHCPProxyLeaseTime_Type.__name__ = "Unsigned32"
_VRtrIfDHCPProxyLeaseTime_Object = MibTableColumn
vRtrIfDHCPProxyLeaseTime = _VRtrIfDHCPProxyLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 30),
    _VRtrIfDHCPProxyLeaseTime_Type()
)
vRtrIfDHCPProxyLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPProxyLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfDHCPProxyLeaseTime.setUnits("seconds")


class _VRtrIfDHCPProxyLTRadiusOverride_Type(TruthValue):
    """Custom type vRtrIfDHCPProxyLTRadiusOverride based on TruthValue"""


_VRtrIfDHCPProxyLTRadiusOverride_Object = MibTableColumn
vRtrIfDHCPProxyLTRadiusOverride = _VRtrIfDHCPProxyLTRadiusOverride_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 31),
    _VRtrIfDHCPProxyLTRadiusOverride_Type()
)
vRtrIfDHCPProxyLTRadiusOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPProxyLTRadiusOverride.setStatus("current")


class _VRtrIfDHCPVendorIncludeOptions_Type(Bits):
    """Custom type vRtrIfDHCPVendorIncludeOptions based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("clientMac", 1),
          ("sapId", 3),
          ("serviceId", 2),
          ("systemId", 0))
    )

_VRtrIfDHCPVendorIncludeOptions_Type.__name__ = "Bits"
_VRtrIfDHCPVendorIncludeOptions_Object = MibTableColumn
vRtrIfDHCPVendorIncludeOptions = _VRtrIfDHCPVendorIncludeOptions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 32),
    _VRtrIfDHCPVendorIncludeOptions_Type()
)
vRtrIfDHCPVendorIncludeOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPVendorIncludeOptions.setStatus("current")


class _VRtrIfDHCPVendorOptionString_Type(DisplayString):
    """Custom type vRtrIfDHCPVendorOptionString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrIfDHCPVendorOptionString_Type.__name__ = "DisplayString"
_VRtrIfDHCPVendorOptionString_Object = MibTableColumn
vRtrIfDHCPVendorOptionString = _VRtrIfDHCPVendorOptionString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 33),
    _VRtrIfDHCPVendorOptionString_Type()
)
vRtrIfDHCPVendorOptionString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPVendorOptionString.setStatus("current")


class _VRtrIfDHCPLayer2Header_Type(TruthValue):
    """Custom type vRtrIfDHCPLayer2Header based on TruthValue"""


_VRtrIfDHCPLayer2Header_Object = MibTableColumn
vRtrIfDHCPLayer2Header = _VRtrIfDHCPLayer2Header_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 34),
    _VRtrIfDHCPLayer2Header_Type()
)
vRtrIfDHCPLayer2Header.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPLayer2Header.setStatus("current")


class _VRtrIfDHCPAntiSpoofMacAddr_Type(MacAddress):
    """Custom type vRtrIfDHCPAntiSpoofMacAddr based on MacAddress"""
    defaultHexValue = "000000000000"


_VRtrIfDHCPAntiSpoofMacAddr_Object = MibTableColumn
vRtrIfDHCPAntiSpoofMacAddr = _VRtrIfDHCPAntiSpoofMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 35),
    _VRtrIfDHCPAntiSpoofMacAddr_Type()
)
vRtrIfDHCPAntiSpoofMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPAntiSpoofMacAddr.setStatus("current")


class _VRtrIfDHCPClientApplications_Type(Bits):
    """Custom type vRtrIfDHCPClientApplications based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("dhcp", 0),
          ("pppoe", 1))
    )

_VRtrIfDHCPClientApplications_Type.__name__ = "Bits"
_VRtrIfDHCPClientApplications_Object = MibTableColumn
vRtrIfDHCPClientApplications = _VRtrIfDHCPClientApplications_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 19, 1, 36),
    _VRtrIfDHCPClientApplications_Type()
)
vRtrIfDHCPClientApplications.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCPClientApplications.setStatus("current")
_VRtrIfDHCPRelayStatsTable_Object = MibTable
vRtrIfDHCPRelayStatsTable = _VRtrIfDHCPRelayStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20)
)
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayStatsTable.setStatus("current")
_VRtrIfDHCPRelayStatsEntry_Object = MibTableRow
vRtrIfDHCPRelayStatsEntry = _VRtrIfDHCPRelayStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1)
)
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayStatsEntry.setStatus("current")
_VRtrIfDHCPRelayRxPkts_Type = Counter32
_VRtrIfDHCPRelayRxPkts_Object = MibTableColumn
vRtrIfDHCPRelayRxPkts = _VRtrIfDHCPRelayRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 1),
    _VRtrIfDHCPRelayRxPkts_Type()
)
vRtrIfDHCPRelayRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayRxPkts.setStatus("current")
_VRtrIfDHCPRelayTxPkts_Type = Counter32
_VRtrIfDHCPRelayTxPkts_Object = MibTableColumn
vRtrIfDHCPRelayTxPkts = _VRtrIfDHCPRelayTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 2),
    _VRtrIfDHCPRelayTxPkts_Type()
)
vRtrIfDHCPRelayTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayTxPkts.setStatus("current")
_VRtrIfDHCPRelayRxMalformedPkts_Type = Counter32
_VRtrIfDHCPRelayRxMalformedPkts_Object = MibTableColumn
vRtrIfDHCPRelayRxMalformedPkts = _VRtrIfDHCPRelayRxMalformedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 3),
    _VRtrIfDHCPRelayRxMalformedPkts_Type()
)
vRtrIfDHCPRelayRxMalformedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayRxMalformedPkts.setStatus("current")
_VRtrIfDHCPRelayRxUntrustedPkts_Type = Counter32
_VRtrIfDHCPRelayRxUntrustedPkts_Object = MibTableColumn
vRtrIfDHCPRelayRxUntrustedPkts = _VRtrIfDHCPRelayRxUntrustedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 4),
    _VRtrIfDHCPRelayRxUntrustedPkts_Type()
)
vRtrIfDHCPRelayRxUntrustedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayRxUntrustedPkts.setStatus("current")
_VRtrIfDHCPRelayClientPktsDiscarded_Type = Counter32
_VRtrIfDHCPRelayClientPktsDiscarded_Object = MibTableColumn
vRtrIfDHCPRelayClientPktsDiscarded = _VRtrIfDHCPRelayClientPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 5),
    _VRtrIfDHCPRelayClientPktsDiscarded_Type()
)
vRtrIfDHCPRelayClientPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayClientPktsDiscarded.setStatus("current")
_VRtrIfDHCPRelayClientPktsRelayed_Type = Counter32
_VRtrIfDHCPRelayClientPktsRelayed_Object = MibTableColumn
vRtrIfDHCPRelayClientPktsRelayed = _VRtrIfDHCPRelayClientPktsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 6),
    _VRtrIfDHCPRelayClientPktsRelayed_Type()
)
vRtrIfDHCPRelayClientPktsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayClientPktsRelayed.setStatus("current")
_VRtrIfDHCPRelayServerPktsDiscarded_Type = Counter32
_VRtrIfDHCPRelayServerPktsDiscarded_Object = MibTableColumn
vRtrIfDHCPRelayServerPktsDiscarded = _VRtrIfDHCPRelayServerPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 7),
    _VRtrIfDHCPRelayServerPktsDiscarded_Type()
)
vRtrIfDHCPRelayServerPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServerPktsDiscarded.setStatus("current")
_VRtrIfDHCPRelayServerPktsRelayed_Type = Counter32
_VRtrIfDHCPRelayServerPktsRelayed_Object = MibTableColumn
vRtrIfDHCPRelayServerPktsRelayed = _VRtrIfDHCPRelayServerPktsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 8),
    _VRtrIfDHCPRelayServerPktsRelayed_Type()
)
vRtrIfDHCPRelayServerPktsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServerPktsRelayed.setStatus("current")
_VRtrIfDHCPRelayAuthPktsDiscarded_Type = Counter32
_VRtrIfDHCPRelayAuthPktsDiscarded_Object = MibTableColumn
vRtrIfDHCPRelayAuthPktsDiscarded = _VRtrIfDHCPRelayAuthPktsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 9),
    _VRtrIfDHCPRelayAuthPktsDiscarded_Type()
)
vRtrIfDHCPRelayAuthPktsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayAuthPktsDiscarded.setStatus("current")
_VRtrIfDHCPRelayAuthPktsSuccess_Type = Counter32
_VRtrIfDHCPRelayAuthPktsSuccess_Object = MibTableColumn
vRtrIfDHCPRelayAuthPktsSuccess = _VRtrIfDHCPRelayAuthPktsSuccess_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 10),
    _VRtrIfDHCPRelayAuthPktsSuccess_Type()
)
vRtrIfDHCPRelayAuthPktsSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayAuthPktsSuccess.setStatus("current")
_VRtrIfDHCPRelayClientPktsSnooped_Type = Counter32
_VRtrIfDHCPRelayClientPktsSnooped_Object = MibTableColumn
vRtrIfDHCPRelayClientPktsSnooped = _VRtrIfDHCPRelayClientPktsSnooped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 11),
    _VRtrIfDHCPRelayClientPktsSnooped_Type()
)
vRtrIfDHCPRelayClientPktsSnooped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayClientPktsSnooped.setStatus("current")
_VRtrIfDHCPRelayServerPktsSnooped_Type = Counter32
_VRtrIfDHCPRelayServerPktsSnooped_Object = MibTableColumn
vRtrIfDHCPRelayServerPktsSnooped = _VRtrIfDHCPRelayServerPktsSnooped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 12),
    _VRtrIfDHCPRelayServerPktsSnooped_Type()
)
vRtrIfDHCPRelayServerPktsSnooped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayServerPktsSnooped.setStatus("current")
_VRtrIfDHCPRelayClientPktsProxRad_Type = Counter32
_VRtrIfDHCPRelayClientPktsProxRad_Object = MibTableColumn
vRtrIfDHCPRelayClientPktsProxRad = _VRtrIfDHCPRelayClientPktsProxRad_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 13),
    _VRtrIfDHCPRelayClientPktsProxRad_Type()
)
vRtrIfDHCPRelayClientPktsProxRad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayClientPktsProxRad.setStatus("current")
_VRtrIfDHCPRelayClientPktsProxLS_Type = Counter32
_VRtrIfDHCPRelayClientPktsProxLS_Object = MibTableColumn
vRtrIfDHCPRelayClientPktsProxLS = _VRtrIfDHCPRelayClientPktsProxLS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 14),
    _VRtrIfDHCPRelayClientPktsProxLS_Type()
)
vRtrIfDHCPRelayClientPktsProxLS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayClientPktsProxLS.setStatus("current")
_VRtrIfDHCPRelayPktsGenRelease_Type = Counter32
_VRtrIfDHCPRelayPktsGenRelease_Object = MibTableColumn
vRtrIfDHCPRelayPktsGenRelease = _VRtrIfDHCPRelayPktsGenRelease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 15),
    _VRtrIfDHCPRelayPktsGenRelease_Type()
)
vRtrIfDHCPRelayPktsGenRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayPktsGenRelease.setStatus("current")
_VRtrIfDHCPRelayPktsGenForceRenew_Type = Counter32
_VRtrIfDHCPRelayPktsGenForceRenew_Object = MibTableColumn
vRtrIfDHCPRelayPktsGenForceRenew = _VRtrIfDHCPRelayPktsGenForceRenew_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 20, 1, 16),
    _VRtrIfDHCPRelayPktsGenForceRenew_Type()
)
vRtrIfDHCPRelayPktsGenForceRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPRelayPktsGenForceRenew.setStatus("current")
_TmnxVRtrNotificationObjects_ObjectIdentity = ObjectIdentity
tmnxVRtrNotificationObjects = _TmnxVRtrNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21)
)
_VRtrAutoFilterDHCPClientAddress_Type = IpAddress
_VRtrAutoFilterDHCPClientAddress_Object = MibScalar
vRtrAutoFilterDHCPClientAddress = _VRtrAutoFilterDHCPClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 1),
    _VRtrAutoFilterDHCPClientAddress_Type()
)
vRtrAutoFilterDHCPClientAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrAutoFilterDHCPClientAddress.setStatus("obsolete")
_VRtrAutoFilterDHCPClientLease_Type = Unsigned32
_VRtrAutoFilterDHCPClientLease_Object = MibScalar
vRtrAutoFilterDHCPClientLease = _VRtrAutoFilterDHCPClientLease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 2),
    _VRtrAutoFilterDHCPClientLease_Type()
)
vRtrAutoFilterDHCPClientLease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrAutoFilterDHCPClientLease.setStatus("obsolete")
_VRtrDHCPClientLease_Type = Integer32
_VRtrDHCPClientLease_Object = MibScalar
vRtrDHCPClientLease = _VRtrDHCPClientLease_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 3),
    _VRtrDHCPClientLease_Type()
)
vRtrDHCPClientLease.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCPClientLease.setStatus("obsolete")
_VRtrDhcpLseStateOldCiAddr_Type = IpAddress
_VRtrDhcpLseStateOldCiAddr_Object = MibScalar
vRtrDhcpLseStateOldCiAddr = _VRtrDhcpLseStateOldCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 4),
    _VRtrDhcpLseStateOldCiAddr_Type()
)
vRtrDhcpLseStateOldCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpLseStateOldCiAddr.setStatus("obsolete")
_VRtrDhcpLseStateOldChAddr_Type = MacAddress
_VRtrDhcpLseStateOldChAddr_Object = MibScalar
vRtrDhcpLseStateOldChAddr = _VRtrDhcpLseStateOldChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 5),
    _VRtrDhcpLseStateOldChAddr_Type()
)
vRtrDhcpLseStateOldChAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpLseStateOldChAddr.setStatus("obsolete")
_VRtrDhcpLseStateNewCiAddr_Type = IpAddress
_VRtrDhcpLseStateNewCiAddr_Object = MibScalar
vRtrDhcpLseStateNewCiAddr = _VRtrDhcpLseStateNewCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 6),
    _VRtrDhcpLseStateNewCiAddr_Type()
)
vRtrDhcpLseStateNewCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpLseStateNewCiAddr.setStatus("obsolete")
_VRtrDhcpLseStateNewChAddr_Type = MacAddress
_VRtrDhcpLseStateNewChAddr_Object = MibScalar
vRtrDhcpLseStateNewChAddr = _VRtrDhcpLseStateNewChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 7),
    _VRtrDhcpLseStateNewChAddr_Type()
)
vRtrDhcpLseStateNewChAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpLseStateNewChAddr.setStatus("obsolete")
_VRtrDhcpRestoreLseStateCiAddr_Type = IpAddress
_VRtrDhcpRestoreLseStateCiAddr_Object = MibScalar
vRtrDhcpRestoreLseStateCiAddr = _VRtrDhcpRestoreLseStateCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 8),
    _VRtrDhcpRestoreLseStateCiAddr_Type()
)
vRtrDhcpRestoreLseStateCiAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpRestoreLseStateCiAddr.setStatus("obsolete")
_VRtrDhcpRestoreLseStateVRtrId_Type = TmnxVRtrID
_VRtrDhcpRestoreLseStateVRtrId_Object = MibScalar
vRtrDhcpRestoreLseStateVRtrId = _VRtrDhcpRestoreLseStateVRtrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 9),
    _VRtrDhcpRestoreLseStateVRtrId_Type()
)
vRtrDhcpRestoreLseStateVRtrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpRestoreLseStateVRtrId.setStatus("obsolete")
_VRtrDhcpRestoreLseStateIfIndex_Type = InterfaceIndex
_VRtrDhcpRestoreLseStateIfIndex_Object = MibScalar
vRtrDhcpRestoreLseStateIfIndex = _VRtrDhcpRestoreLseStateIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 10),
    _VRtrDhcpRestoreLseStateIfIndex_Type()
)
vRtrDhcpRestoreLseStateIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpRestoreLseStateIfIndex.setStatus("obsolete")
_VRtrDhcpRestoreLseStateProblem_Type = DisplayString
_VRtrDhcpRestoreLseStateProblem_Object = MibScalar
vRtrDhcpRestoreLseStateProblem = _VRtrDhcpRestoreLseStateProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 11),
    _VRtrDhcpRestoreLseStateProblem_Type()
)
vRtrDhcpRestoreLseStateProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpRestoreLseStateProblem.setStatus("obsolete")
_VRtrDhcpPacketProblem_Type = DisplayString
_VRtrDhcpPacketProblem_Object = MibScalar
vRtrDhcpPacketProblem = _VRtrDhcpPacketProblem_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 12),
    _VRtrDhcpPacketProblem_Type()
)
vRtrDhcpPacketProblem.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpPacketProblem.setStatus("current")
_VRtrDhcpLseStatePopulateError_Type = DisplayString
_VRtrDhcpLseStatePopulateError_Object = MibScalar
vRtrDhcpLseStatePopulateError = _VRtrDhcpLseStatePopulateError_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 13),
    _VRtrDhcpLseStatePopulateError_Type()
)
vRtrDhcpLseStatePopulateError.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDhcpLseStatePopulateError.setStatus("obsolete")
_VRtrBfdSlotNumber_Type = TmnxSlotNum
_VRtrBfdSlotNumber_Object = MibScalar
vRtrBfdSlotNumber = _VRtrBfdSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 14),
    _VRtrBfdSlotNumber_Type()
)
vRtrBfdSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBfdSlotNumber.setStatus("current")
_VRtrNumberOfBfdSessionsOnSlot_Type = Unsigned32
_VRtrNumberOfBfdSessionsOnSlot_Object = MibScalar
vRtrNumberOfBfdSessionsOnSlot = _VRtrNumberOfBfdSessionsOnSlot_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 15),
    _VRtrNumberOfBfdSessionsOnSlot_Type()
)
vRtrNumberOfBfdSessionsOnSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrNumberOfBfdSessionsOnSlot.setStatus("current")


class _VRtrBfdMaxSessionReason_Type(Bits):
    """Custom type vRtrBfdMaxSessionReason based on Bits"""
    namedValues = NamedValues(
        *(("maxRxPacketRate", 2),
          ("maxSessionsPerSlot", 0),
          ("maxTxPacketRate", 1))
    )

_VRtrBfdMaxSessionReason_Type.__name__ = "Bits"
_VRtrBfdMaxSessionReason_Object = MibScalar
vRtrBfdMaxSessionReason = _VRtrBfdMaxSessionReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 16),
    _VRtrBfdMaxSessionReason_Type()
)
vRtrBfdMaxSessionReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBfdMaxSessionReason.setStatus("current")
_VRtrDHCP6ServerNetAddrType_Type = InetAddressType
_VRtrDHCP6ServerNetAddrType_Object = MibScalar
vRtrDHCP6ServerNetAddrType = _VRtrDHCP6ServerNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 17),
    _VRtrDHCP6ServerNetAddrType_Type()
)
vRtrDHCP6ServerNetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6ServerNetAddrType.setStatus("current")
_VRtrDHCP6ServerNetAddr_Type = InetAddress
_VRtrDHCP6ServerNetAddr_Object = MibScalar
vRtrDHCP6ServerNetAddr = _VRtrDHCP6ServerNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 18),
    _VRtrDHCP6ServerNetAddr_Type()
)
vRtrDHCP6ServerNetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6ServerNetAddr.setStatus("current")
_VRtrDHCP6ClientNetAddrType_Type = InetAddressType
_VRtrDHCP6ClientNetAddrType_Object = MibScalar
vRtrDHCP6ClientNetAddrType = _VRtrDHCP6ClientNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 19),
    _VRtrDHCP6ClientNetAddrType_Type()
)
vRtrDHCP6ClientNetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6ClientNetAddrType.setStatus("current")
_VRtrDHCP6ClientNetAddr_Type = InetAddress
_VRtrDHCP6ClientNetAddr_Object = MibScalar
vRtrDHCP6ClientNetAddr = _VRtrDHCP6ClientNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 20),
    _VRtrDHCP6ClientNetAddr_Type()
)
vRtrDHCP6ClientNetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6ClientNetAddr.setStatus("current")
_VRtrDHCP6AssignedNetAddrType_Type = InetAddressType
_VRtrDHCP6AssignedNetAddrType_Object = MibScalar
vRtrDHCP6AssignedNetAddrType = _VRtrDHCP6AssignedNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 21),
    _VRtrDHCP6AssignedNetAddrType_Type()
)
vRtrDHCP6AssignedNetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6AssignedNetAddrType.setStatus("current")
_VRtrDHCP6AssignedNetAddr_Type = InetAddress
_VRtrDHCP6AssignedNetAddr_Object = MibScalar
vRtrDHCP6AssignedNetAddr = _VRtrDHCP6AssignedNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 22),
    _VRtrDHCP6AssignedNetAddr_Type()
)
vRtrDHCP6AssignedNetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6AssignedNetAddr.setStatus("current")
_VRtrDHCP6AssignedPrefixLen_Type = InetAddressPrefixLength
_VRtrDHCP6AssignedPrefixLen_Object = MibScalar
vRtrDHCP6AssignedPrefixLen = _VRtrDHCP6AssignedPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 23),
    _VRtrDHCP6AssignedPrefixLen_Type()
)
vRtrDHCP6AssignedPrefixLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6AssignedPrefixLen.setStatus("current")
_VRtrDHCP6OldAssignedNetAddrType_Type = InetAddressType
_VRtrDHCP6OldAssignedNetAddrType_Object = MibScalar
vRtrDHCP6OldAssignedNetAddrType = _VRtrDHCP6OldAssignedNetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 24),
    _VRtrDHCP6OldAssignedNetAddrType_Type()
)
vRtrDHCP6OldAssignedNetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6OldAssignedNetAddrType.setStatus("current")
_VRtrDHCP6OldAssignedNetAddr_Type = InetAddress
_VRtrDHCP6OldAssignedNetAddr_Object = MibScalar
vRtrDHCP6OldAssignedNetAddr = _VRtrDHCP6OldAssignedNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 25),
    _VRtrDHCP6OldAssignedNetAddr_Type()
)
vRtrDHCP6OldAssignedNetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6OldAssignedNetAddr.setStatus("current")
_VRtrDHCP6OldAssignedPrefixLen_Type = InetAddressPrefixLength
_VRtrDHCP6OldAssignedPrefixLen_Object = MibScalar
vRtrDHCP6OldAssignedPrefixLen = _VRtrDHCP6OldAssignedPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 26),
    _VRtrDHCP6OldAssignedPrefixLen_Type()
)
vRtrDHCP6OldAssignedPrefixLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6OldAssignedPrefixLen.setStatus("current")


class _VRtrDHCP6NewClientId_Type(OctetString):
    """Custom type vRtrDHCP6NewClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VRtrDHCP6NewClientId_Type.__name__ = "OctetString"
_VRtrDHCP6NewClientId_Object = MibScalar
vRtrDHCP6NewClientId = _VRtrDHCP6NewClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 27),
    _VRtrDHCP6NewClientId_Type()
)
vRtrDHCP6NewClientId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6NewClientId.setStatus("current")


class _VRtrDHCP6OldClientId_Type(OctetString):
    """Custom type vRtrDHCP6OldClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VRtrDHCP6OldClientId_Type.__name__ = "OctetString"
_VRtrDHCP6OldClientId_Object = MibScalar
vRtrDHCP6OldClientId = _VRtrDHCP6OldClientId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 28),
    _VRtrDHCP6OldClientId_Type()
)
vRtrDHCP6OldClientId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6OldClientId.setStatus("current")
_VRtrDHCP6LeaseOverrideResult_Type = DisplayString
_VRtrDHCP6LeaseOverrideResult_Object = MibScalar
vRtrDHCP6LeaseOverrideResult = _VRtrDHCP6LeaseOverrideResult_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 29),
    _VRtrDHCP6LeaseOverrideResult_Type()
)
vRtrDHCP6LeaseOverrideResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrDHCP6LeaseOverrideResult.setStatus("current")
_VRtrInetStatRteCpeNotifyAddrType_Type = InetAddressType
_VRtrInetStatRteCpeNotifyAddrType_Object = MibScalar
vRtrInetStatRteCpeNotifyAddrType = _VRtrInetStatRteCpeNotifyAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 30),
    _VRtrInetStatRteCpeNotifyAddrType_Type()
)
vRtrInetStatRteCpeNotifyAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeNotifyAddrType.setStatus("current")
_VRtrInetStatRteCpeNotifyAddr_Type = InetAddress
_VRtrInetStatRteCpeNotifyAddr_Object = MibScalar
vRtrInetStatRteCpeNotifyAddr = _VRtrInetStatRteCpeNotifyAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 31),
    _VRtrInetStatRteCpeNotifyAddr_Type()
)
vRtrInetStatRteCpeNotifyAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeNotifyAddr.setStatus("current")


class _VRtrInetStaticRouteCpeStatus_Type(Integer32):
    """Custom type vRtrInetStaticRouteCpeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 0),
          ("unreachable", 1))
    )


_VRtrInetStaticRouteCpeStatus_Type.__name__ = "Integer32"
_VRtrInetStaticRouteCpeStatus_Object = MibScalar
vRtrInetStaticRouteCpeStatus = _VRtrInetStaticRouteCpeStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 32),
    _VRtrInetStaticRouteCpeStatus_Type()
)
vRtrInetStaticRouteCpeStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteCpeStatus.setStatus("current")
_VRtrManagedRouteInetAddrType_Type = InetAddressType
_VRtrManagedRouteInetAddrType_Object = MibScalar
vRtrManagedRouteInetAddrType = _VRtrManagedRouteInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 33),
    _VRtrManagedRouteInetAddrType_Type()
)
vRtrManagedRouteInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrManagedRouteInetAddrType.setStatus("current")


class _VRtrManagedRouteInetAddr_Type(InetAddress):
    """Custom type vRtrManagedRouteInetAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrManagedRouteInetAddr_Type.__name__ = "InetAddress"
_VRtrManagedRouteInetAddr_Object = MibScalar
vRtrManagedRouteInetAddr = _VRtrManagedRouteInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 34),
    _VRtrManagedRouteInetAddr_Type()
)
vRtrManagedRouteInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrManagedRouteInetAddr.setStatus("current")
_VRtrManagedRoutePrefixLen_Type = InetAddressPrefixLength
_VRtrManagedRoutePrefixLen_Object = MibScalar
vRtrManagedRoutePrefixLen = _VRtrManagedRoutePrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 35),
    _VRtrManagedRoutePrefixLen_Type()
)
vRtrManagedRoutePrefixLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrManagedRoutePrefixLen.setStatus("current")
_VRtrFailureDescription_Type = DisplayString
_VRtrFailureDescription_Object = MibScalar
vRtrFailureDescription = _VRtrFailureDescription_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 21, 36),
    _VRtrFailureDescription_Type()
)
vRtrFailureDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrFailureDescription.setStatus("current")
_VRtrIfDHCPLeaseStateTable_Object = MibTable
vRtrIfDHCPLeaseStateTable = _VRtrIfDHCPLeaseStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 22)
)
if mibBuilder.loadTexts:
    vRtrIfDHCPLeaseStateTable.setStatus("obsolete")
_VRtrIfDHCPLeaseStateEntry_Object = MibTableRow
vRtrIfDHCPLeaseStateEntry = _VRtrIfDHCPLeaseStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 22, 1)
)
vRtrIfDHCPLeaseStateEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLseStateCiAddr"),
)
if mibBuilder.loadTexts:
    vRtrIfDHCPLeaseStateEntry.setStatus("obsolete")
_VRtrIfDHCPLseStateCiAddr_Type = IpAddress
_VRtrIfDHCPLseStateCiAddr_Object = MibTableColumn
vRtrIfDHCPLseStateCiAddr = _VRtrIfDHCPLseStateCiAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 22, 1, 1),
    _VRtrIfDHCPLseStateCiAddr_Type()
)
vRtrIfDHCPLseStateCiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfDHCPLseStateCiAddr.setStatus("obsolete")
_VRtrIfDHCPLseStateChAddr_Type = MacAddress
_VRtrIfDHCPLseStateChAddr_Object = MibTableColumn
vRtrIfDHCPLseStateChAddr = _VRtrIfDHCPLseStateChAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 22, 1, 2),
    _VRtrIfDHCPLseStateChAddr_Type()
)
vRtrIfDHCPLseStateChAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPLseStateChAddr.setStatus("obsolete")
_VRtrIfDHCPLseStateRemainLseTime_Type = Unsigned32
_VRtrIfDHCPLseStateRemainLseTime_Object = MibTableColumn
vRtrIfDHCPLseStateRemainLseTime = _VRtrIfDHCPLseStateRemainLseTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 22, 1, 3),
    _VRtrIfDHCPLseStateRemainLseTime_Type()
)
vRtrIfDHCPLseStateRemainLseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPLseStateRemainLseTime.setStatus("obsolete")
_VRtrIfDHCPLseStateOption82_Type = OctetString
_VRtrIfDHCPLseStateOption82_Object = MibTableColumn
vRtrIfDHCPLseStateOption82 = _VRtrIfDHCPLseStateOption82_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 22, 1, 4),
    _VRtrIfDHCPLseStateOption82_Type()
)
vRtrIfDHCPLseStateOption82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPLseStateOption82.setStatus("obsolete")
_VRtrIfDHCPLseStatePersistKey_Type = Unsigned32
_VRtrIfDHCPLseStatePersistKey_Object = MibTableColumn
vRtrIfDHCPLseStatePersistKey = _VRtrIfDHCPLseStatePersistKey_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 22, 1, 5),
    _VRtrIfDHCPLseStatePersistKey_Type()
)
vRtrIfDHCPLseStatePersistKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCPLseStatePersistKey.setStatus("obsolete")
_VRtrAdvPrefixTable_Object = MibTable
vRtrAdvPrefixTable = _VRtrAdvPrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23)
)
if mibBuilder.loadTexts:
    vRtrAdvPrefixTable.setStatus("current")
_VRtrAdvPrefixEntry_Object = MibTableRow
vRtrAdvPrefixEntry = _VRtrAdvPrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1)
)
vRtrAdvPrefixEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixLength"),
)
if mibBuilder.loadTexts:
    vRtrAdvPrefixEntry.setStatus("current")
_VRtrAdvPrefixIfIndex_Type = InterfaceIndex
_VRtrAdvPrefixIfIndex_Object = MibTableColumn
vRtrAdvPrefixIfIndex = _VRtrAdvPrefixIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 1),
    _VRtrAdvPrefixIfIndex_Type()
)
vRtrAdvPrefixIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrAdvPrefixIfIndex.setStatus("current")


class _VRtrAdvPrefixPrefix_Type(InetAddress):
    """Custom type vRtrAdvPrefixPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_VRtrAdvPrefixPrefix_Type.__name__ = "InetAddress"
_VRtrAdvPrefixPrefix_Object = MibTableColumn
vRtrAdvPrefixPrefix = _VRtrAdvPrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 2),
    _VRtrAdvPrefixPrefix_Type()
)
vRtrAdvPrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrAdvPrefixPrefix.setStatus("current")


class _VRtrAdvPrefixLength_Type(InetAddressPrefixLength):
    """Custom type vRtrAdvPrefixLength based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 127),
    )


_VRtrAdvPrefixLength_Type.__name__ = "InetAddressPrefixLength"
_VRtrAdvPrefixLength_Object = MibTableColumn
vRtrAdvPrefixLength = _VRtrAdvPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 3),
    _VRtrAdvPrefixLength_Type()
)
vRtrAdvPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrAdvPrefixLength.setStatus("current")
_VRtrAdvPrefixRowStatus_Type = RowStatus
_VRtrAdvPrefixRowStatus_Object = MibTableColumn
vRtrAdvPrefixRowStatus = _VRtrAdvPrefixRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 4),
    _VRtrAdvPrefixRowStatus_Type()
)
vRtrAdvPrefixRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAdvPrefixRowStatus.setStatus("current")


class _VRtrAdvPrefixOnLinkFlag_Type(TruthValue):
    """Custom type vRtrAdvPrefixOnLinkFlag based on TruthValue"""


_VRtrAdvPrefixOnLinkFlag_Object = MibTableColumn
vRtrAdvPrefixOnLinkFlag = _VRtrAdvPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 5),
    _VRtrAdvPrefixOnLinkFlag_Type()
)
vRtrAdvPrefixOnLinkFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAdvPrefixOnLinkFlag.setStatus("current")


class _VRtrAdvPrefixAutonomousFlag_Type(TruthValue):
    """Custom type vRtrAdvPrefixAutonomousFlag based on TruthValue"""


_VRtrAdvPrefixAutonomousFlag_Object = MibTableColumn
vRtrAdvPrefixAutonomousFlag = _VRtrAdvPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 6),
    _VRtrAdvPrefixAutonomousFlag_Type()
)
vRtrAdvPrefixAutonomousFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAdvPrefixAutonomousFlag.setStatus("current")


class _VRtrAdvPrefixPreferredLifetime_Type(Unsigned32):
    """Custom type vRtrAdvPrefixPreferredLifetime based on Unsigned32"""
    defaultValue = 604800


_VRtrAdvPrefixPreferredLifetime_Object = MibTableColumn
vRtrAdvPrefixPreferredLifetime = _VRtrAdvPrefixPreferredLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 7),
    _VRtrAdvPrefixPreferredLifetime_Type()
)
vRtrAdvPrefixPreferredLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAdvPrefixPreferredLifetime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrAdvPrefixPreferredLifetime.setUnits("seconds")


class _VRtrAdvPrefixValidLifetime_Type(Unsigned32):
    """Custom type vRtrAdvPrefixValidLifetime based on Unsigned32"""
    defaultValue = 2592000


_VRtrAdvPrefixValidLifetime_Object = MibTableColumn
vRtrAdvPrefixValidLifetime = _VRtrAdvPrefixValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 23, 1, 8),
    _VRtrAdvPrefixValidLifetime_Type()
)
vRtrAdvPrefixValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrAdvPrefixValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrAdvPrefixValidLifetime.setUnits("seconds")
_VRtrInetStaticRouteTable_Object = MibTable
vRtrInetStaticRouteTable = _VRtrInetStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24)
)
if mibBuilder.loadTexts:
    vRtrInetStaticRouteTable.setStatus("current")
_VRtrInetStaticRouteEntry_Object = MibTableRow
vRtrInetStaticRouteEntry = _VRtrInetStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1)
)
vRtrInetStaticRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDestType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDest"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDestPfxLen"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    vRtrInetStaticRouteEntry.setStatus("current")
_VRtrInetStaticRouteDestType_Type = InetAddressType
_VRtrInetStaticRouteDestType_Object = MibTableColumn
vRtrInetStaticRouteDestType = _VRtrInetStaticRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 1),
    _VRtrInetStaticRouteDestType_Type()
)
vRtrInetStaticRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteDestType.setStatus("current")
_VRtrInetStaticRouteDest_Type = InetAddress
_VRtrInetStaticRouteDest_Object = MibTableColumn
vRtrInetStaticRouteDest = _VRtrInetStaticRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 2),
    _VRtrInetStaticRouteDest_Type()
)
vRtrInetStaticRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteDest.setStatus("current")
_VRtrInetStaticRouteDestPfxLen_Type = InetAddressPrefixLength
_VRtrInetStaticRouteDestPfxLen_Object = MibTableColumn
vRtrInetStaticRouteDestPfxLen = _VRtrInetStaticRouteDestPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 3),
    _VRtrInetStaticRouteDestPfxLen_Type()
)
vRtrInetStaticRouteDestPfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteDestPfxLen.setStatus("current")


class _VRtrInetStaticRouteIndex_Type(Integer32):
    """Custom type vRtrInetStaticRouteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrInetStaticRouteIndex_Type.__name__ = "Integer32"
_VRtrInetStaticRouteIndex_Object = MibTableColumn
vRtrInetStaticRouteIndex = _VRtrInetStaticRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 4),
    _VRtrInetStaticRouteIndex_Type()
)
vRtrInetStaticRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteIndex.setStatus("current")
_VRtrInetStaticRouteRowStatus_Type = RowStatus
_VRtrInetStaticRouteRowStatus_Object = MibTableColumn
vRtrInetStaticRouteRowStatus = _VRtrInetStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 5),
    _VRtrInetStaticRouteRowStatus_Type()
)
vRtrInetStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteRowStatus.setStatus("current")
_VRtrInetStaticRouteLastEnabledTime_Type = TimeStamp
_VRtrInetStaticRouteLastEnabledTime_Object = MibTableColumn
vRtrInetStaticRouteLastEnabledTime = _VRtrInetStaticRouteLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 6),
    _VRtrInetStaticRouteLastEnabledTime_Type()
)
vRtrInetStaticRouteLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteLastEnabledTime.setStatus("current")


class _VRtrInetStaticRouteStatus_Type(Integer32):
    """Custom type vRtrInetStaticRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_VRtrInetStaticRouteStatus_Type.__name__ = "Integer32"
_VRtrInetStaticRouteStatus_Object = MibTableColumn
vRtrInetStaticRouteStatus = _VRtrInetStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 7),
    _VRtrInetStaticRouteStatus_Type()
)
vRtrInetStaticRouteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteStatus.setStatus("current")


class _VRtrInetStaticRouteStaticType_Type(Integer32):
    """Custom type vRtrInetStaticRouteStaticType based on Integer32"""
    defaultValue = 0

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
        *(("blackHole", 3),
          ("indirect", 2),
          ("nextHop", 1),
          ("unknown", 0))
    )


_VRtrInetStaticRouteStaticType_Type.__name__ = "Integer32"
_VRtrInetStaticRouteStaticType_Object = MibTableColumn
vRtrInetStaticRouteStaticType = _VRtrInetStaticRouteStaticType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 8),
    _VRtrInetStaticRouteStaticType_Type()
)
vRtrInetStaticRouteStaticType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteStaticType.setStatus("current")


class _VRtrInetStaticRoutePreference_Type(Unsigned32):
    """Custom type vRtrInetStaticRoutePreference based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_VRtrInetStaticRoutePreference_Type.__name__ = "Unsigned32"
_VRtrInetStaticRoutePreference_Object = MibTableColumn
vRtrInetStaticRoutePreference = _VRtrInetStaticRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 9),
    _VRtrInetStaticRoutePreference_Type()
)
vRtrInetStaticRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRoutePreference.setStatus("current")


class _VRtrInetStaticRouteMetric_Type(Unsigned32):
    """Custom type vRtrInetStaticRouteMetric based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrInetStaticRouteMetric_Type.__name__ = "Unsigned32"
_VRtrInetStaticRouteMetric_Object = MibTableColumn
vRtrInetStaticRouteMetric = _VRtrInetStaticRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 10),
    _VRtrInetStaticRouteMetric_Type()
)
vRtrInetStaticRouteMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteMetric.setStatus("current")
_VRtrInetStaticRouteEgressIfIndex_Type = InterfaceIndexOrZero
_VRtrInetStaticRouteEgressIfIndex_Object = MibTableColumn
vRtrInetStaticRouteEgressIfIndex = _VRtrInetStaticRouteEgressIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 11),
    _VRtrInetStaticRouteEgressIfIndex_Type()
)
vRtrInetStaticRouteEgressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteEgressIfIndex.setStatus("current")


class _VRtrInetStaticRouteNextHopType_Type(InetAddressType):
    """Custom type vRtrInetStaticRouteNextHopType based on InetAddressType"""


_VRtrInetStaticRouteNextHopType_Object = MibTableColumn
vRtrInetStaticRouteNextHopType = _VRtrInetStaticRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 12),
    _VRtrInetStaticRouteNextHopType_Type()
)
vRtrInetStaticRouteNextHopType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteNextHopType.setStatus("current")


class _VRtrInetStaticRouteNextHop_Type(InetAddress):
    """Custom type vRtrInetStaticRouteNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_VRtrInetStaticRouteNextHop_Type.__name__ = "InetAddress"
_VRtrInetStaticRouteNextHop_Object = MibTableColumn
vRtrInetStaticRouteNextHop = _VRtrInetStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 13),
    _VRtrInetStaticRouteNextHop_Type()
)
vRtrInetStaticRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteNextHop.setStatus("current")


class _VRtrInetStaticRouteNextHopIf_Type(DisplayString):
    """Custom type vRtrInetStaticRouteNextHopIf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VRtrInetStaticRouteNextHopIf_Type.__name__ = "DisplayString"
_VRtrInetStaticRouteNextHopIf_Object = MibTableColumn
vRtrInetStaticRouteNextHopIf = _VRtrInetStaticRouteNextHopIf_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 14),
    _VRtrInetStaticRouteNextHopIf_Type()
)
vRtrInetStaticRouteNextHopIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteNextHopIf.setStatus("current")


class _VRtrInetStaticRouteAdminState_Type(TmnxAdminState):
    """Custom type vRtrInetStaticRouteAdminState based on TmnxAdminState"""


_VRtrInetStaticRouteAdminState_Object = MibTableColumn
vRtrInetStaticRouteAdminState = _VRtrInetStaticRouteAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 15),
    _VRtrInetStaticRouteAdminState_Type()
)
vRtrInetStaticRouteAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteAdminState.setStatus("current")


class _VRtrInetStaticRouteIgpShortcut_Type(Bits):
    """Custom type vRtrInetStaticRouteIgpShortcut based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ip", 2),
          ("ldp", 1),
          ("te", 0))
    )

_VRtrInetStaticRouteIgpShortcut_Type.__name__ = "Bits"
_VRtrInetStaticRouteIgpShortcut_Object = MibTableColumn
vRtrInetStaticRouteIgpShortcut = _VRtrInetStaticRouteIgpShortcut_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 16),
    _VRtrInetStaticRouteIgpShortcut_Type()
)
vRtrInetStaticRouteIgpShortcut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteIgpShortcut.setStatus("current")


class _VRtrInetStaticRouteDisallowIgp_Type(TruthValue):
    """Custom type vRtrInetStaticRouteDisallowIgp based on TruthValue"""


_VRtrInetStaticRouteDisallowIgp_Object = MibTableColumn
vRtrInetStaticRouteDisallowIgp = _VRtrInetStaticRouteDisallowIgp_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 17),
    _VRtrInetStaticRouteDisallowIgp_Type()
)
vRtrInetStaticRouteDisallowIgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteDisallowIgp.setStatus("current")


class _VRtrInetStaticRouteTag_Type(Unsigned32):
    """Custom type vRtrInetStaticRouteTag based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrInetStaticRouteTag_Type.__name__ = "Unsigned32"
_VRtrInetStaticRouteTag_Object = MibTableColumn
vRtrInetStaticRouteTag = _VRtrInetStaticRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 18),
    _VRtrInetStaticRouteTag_Type()
)
vRtrInetStaticRouteTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteTag.setStatus("current")


class _VRtrInetStaticRouteEnableBfd_Type(TruthValue):
    """Custom type vRtrInetStaticRouteEnableBfd based on TruthValue"""


_VRtrInetStaticRouteEnableBfd_Object = MibTableColumn
vRtrInetStaticRouteEnableBfd = _VRtrInetStaticRouteEnableBfd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 19),
    _VRtrInetStaticRouteEnableBfd_Type()
)
vRtrInetStaticRouteEnableBfd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteEnableBfd.setStatus("current")


class _VRtrInetStaticRouteCpeAddrType_Type(InetAddressType):
    """Custom type vRtrInetStaticRouteCpeAddrType based on InetAddressType"""


_VRtrInetStaticRouteCpeAddrType_Object = MibTableColumn
vRtrInetStaticRouteCpeAddrType = _VRtrInetStaticRouteCpeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 20),
    _VRtrInetStaticRouteCpeAddrType_Type()
)
vRtrInetStaticRouteCpeAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteCpeAddrType.setStatus("current")


class _VRtrInetStaticRouteCpeAddr_Type(InetAddress):
    """Custom type vRtrInetStaticRouteCpeAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrInetStaticRouteCpeAddr_Type.__name__ = "InetAddress"
_VRtrInetStaticRouteCpeAddr_Object = MibTableColumn
vRtrInetStaticRouteCpeAddr = _VRtrInetStaticRouteCpeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 21),
    _VRtrInetStaticRouteCpeAddr_Type()
)
vRtrInetStaticRouteCpeAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteCpeAddr.setStatus("current")


class _VRtrInetStaticRouteCpeInterval_Type(Unsigned32):
    """Custom type vRtrInetStaticRouteCpeInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrInetStaticRouteCpeInterval_Type.__name__ = "Unsigned32"
_VRtrInetStaticRouteCpeInterval_Object = MibTableColumn
vRtrInetStaticRouteCpeInterval = _VRtrInetStaticRouteCpeInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 22),
    _VRtrInetStaticRouteCpeInterval_Type()
)
vRtrInetStaticRouteCpeInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteCpeInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteCpeInterval.setUnits("seconds")


class _VRtrInetStaticRouteCpeDropCnt_Type(Unsigned32):
    """Custom type vRtrInetStaticRouteCpeDropCnt based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VRtrInetStaticRouteCpeDropCnt_Type.__name__ = "Unsigned32"
_VRtrInetStaticRouteCpeDropCnt_Object = MibTableColumn
vRtrInetStaticRouteCpeDropCnt = _VRtrInetStaticRouteCpeDropCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 23),
    _VRtrInetStaticRouteCpeDropCnt_Type()
)
vRtrInetStaticRouteCpeDropCnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteCpeDropCnt.setStatus("current")


class _VRtrInetStaticRouteCpeEnableLog_Type(TruthValue):
    """Custom type vRtrInetStaticRouteCpeEnableLog based on TruthValue"""


_VRtrInetStaticRouteCpeEnableLog_Object = MibTableColumn
vRtrInetStaticRouteCpeEnableLog = _VRtrInetStaticRouteCpeEnableLog_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 24, 1, 24),
    _VRtrInetStaticRouteCpeEnableLog_Type()
)
vRtrInetStaticRouteCpeEnableLog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteCpeEnableLog.setStatus("current")
_VRtrInetStaticRouteIndexTable_Object = MibTable
vRtrInetStaticRouteIndexTable = _VRtrInetStaticRouteIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 25)
)
if mibBuilder.loadTexts:
    vRtrInetStaticRouteIndexTable.setStatus("current")
_VRtrInetStaticRouteIndexEntry_Object = MibTableRow
vRtrInetStaticRouteIndexEntry = _VRtrInetStaticRouteIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 25, 1)
)
vRtrInetStaticRouteIndexEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDestType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDest"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDestPfxLen"),
)
if mibBuilder.loadTexts:
    vRtrInetStaticRouteIndexEntry.setStatus("current")


class _VRtrInetStaticRouteAvailIndex_Type(TestAndIncr):
    """Custom type vRtrInetStaticRouteAvailIndex based on TestAndIncr"""
    subtypeSpec = TestAndIncr.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VRtrInetStaticRouteAvailIndex_Type.__name__ = "TestAndIncr"
_VRtrInetStaticRouteAvailIndex_Object = MibTableColumn
vRtrInetStaticRouteAvailIndex = _VRtrInetStaticRouteAvailIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 25, 1, 1),
    _VRtrInetStaticRouteAvailIndex_Type()
)
vRtrInetStaticRouteAvailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStaticRouteAvailIndex.setStatus("current")
_VRtrInetInstAggrTblLastChged_Type = TimeStamp
_VRtrInetInstAggrTblLastChged_Object = MibScalar
vRtrInetInstAggrTblLastChged = _VRtrInetInstAggrTblLastChged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 26),
    _VRtrInetInstAggrTblLastChged_Type()
)
vRtrInetInstAggrTblLastChged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetInstAggrTblLastChged.setStatus("current")
_VRtrInetInstAggrTable_Object = MibTable
vRtrInetInstAggrTable = _VRtrInetInstAggrTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27)
)
if mibBuilder.loadTexts:
    vRtrInetInstAggrTable.setStatus("current")
_VRtrInetInstAggrEntry_Object = MibTableRow
vRtrInetInstAggrEntry = _VRtrInetInstAggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1)
)
vRtrInetInstAggrEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrIpPrefixType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrIpPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrIpPrefixLen"),
)
if mibBuilder.loadTexts:
    vRtrInetInstAggrEntry.setStatus("current")
_VRtrInetAggrIpPrefixType_Type = InetAddressType
_VRtrInetAggrIpPrefixType_Object = MibTableColumn
vRtrInetAggrIpPrefixType = _VRtrInetAggrIpPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 1),
    _VRtrInetAggrIpPrefixType_Type()
)
vRtrInetAggrIpPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetAggrIpPrefixType.setStatus("current")
_VRtrInetAggrIpPrefix_Type = InetAddress
_VRtrInetAggrIpPrefix_Object = MibTableColumn
vRtrInetAggrIpPrefix = _VRtrInetAggrIpPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 2),
    _VRtrInetAggrIpPrefix_Type()
)
vRtrInetAggrIpPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetAggrIpPrefix.setStatus("current")
_VRtrInetAggrIpPrefixLen_Type = InetAddressPrefixLength
_VRtrInetAggrIpPrefixLen_Object = MibTableColumn
vRtrInetAggrIpPrefixLen = _VRtrInetAggrIpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 3),
    _VRtrInetAggrIpPrefixLen_Type()
)
vRtrInetAggrIpPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetAggrIpPrefixLen.setStatus("current")
_VRtrInetAggrRowStatus_Type = RowStatus
_VRtrInetAggrRowStatus_Object = MibTableColumn
vRtrInetAggrRowStatus = _VRtrInetAggrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 4),
    _VRtrInetAggrRowStatus_Type()
)
vRtrInetAggrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetAggrRowStatus.setStatus("current")
_VRtrInetAggrLastChanged_Type = TimeStamp
_VRtrInetAggrLastChanged_Object = MibTableColumn
vRtrInetAggrLastChanged = _VRtrInetAggrLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 5),
    _VRtrInetAggrLastChanged_Type()
)
vRtrInetAggrLastChanged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetAggrLastChanged.setStatus("current")


class _VRtrInetAggrSummaryOnly_Type(TruthValue):
    """Custom type vRtrInetAggrSummaryOnly based on TruthValue"""


_VRtrInetAggrSummaryOnly_Object = MibTableColumn
vRtrInetAggrSummaryOnly = _VRtrInetAggrSummaryOnly_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 6),
    _VRtrInetAggrSummaryOnly_Type()
)
vRtrInetAggrSummaryOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetAggrSummaryOnly.setStatus("current")


class _VRtrInetAggrASSet_Type(TruthValue):
    """Custom type vRtrInetAggrASSet based on TruthValue"""


_VRtrInetAggrASSet_Object = MibTableColumn
vRtrInetAggrASSet = _VRtrInetAggrASSet_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 7),
    _VRtrInetAggrASSet_Type()
)
vRtrInetAggrASSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetAggrASSet.setStatus("current")


class _VRtrInetAggrAggregatorAS_Type(TmnxBgpAutonomousSystem):
    """Custom type vRtrInetAggrAggregatorAS based on TmnxBgpAutonomousSystem"""
    defaultValue = 0


_VRtrInetAggrAggregatorAS_Object = MibTableColumn
vRtrInetAggrAggregatorAS = _VRtrInetAggrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 8),
    _VRtrInetAggrAggregatorAS_Type()
)
vRtrInetAggrAggregatorAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetAggrAggregatorAS.setStatus("current")


class _VRtrInetAggrAggregatorIPAddr_Type(IpAddress):
    """Custom type vRtrInetAggrAggregatorIPAddr based on IpAddress"""
    defaultHexValue = "00000000"


_VRtrInetAggrAggregatorIPAddr_Object = MibTableColumn
vRtrInetAggrAggregatorIPAddr = _VRtrInetAggrAggregatorIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 9),
    _VRtrInetAggrAggregatorIPAddr_Type()
)
vRtrInetAggrAggregatorIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetAggrAggregatorIPAddr.setStatus("current")
_VRtrInetAggrOperState_Type = TmnxOperState
_VRtrInetAggrOperState_Object = MibTableColumn
vRtrInetAggrOperState = _VRtrInetAggrOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 27, 1, 10),
    _VRtrInetAggrOperState_Type()
)
vRtrInetAggrOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetAggrOperState.setStatus("current")
_VRtrInetSvcIpRangeTable_Object = MibTable
vRtrInetSvcIpRangeTable = _VRtrInetSvcIpRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 28)
)
if mibBuilder.loadTexts:
    vRtrInetSvcIpRangeTable.setStatus("current")
_VRtrInetSvcIpRangeEntry_Object = MibTableRow
vRtrInetSvcIpRangeEntry = _VRtrInetSvcIpRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 28, 1)
)
vRtrInetSvcIpRangeEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetSvcIpRangeAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetSvcIpRangeAddr"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetSvcIpRangePfxLen"),
)
if mibBuilder.loadTexts:
    vRtrInetSvcIpRangeEntry.setStatus("current")
_VRtrInetSvcIpRangeAddrType_Type = InetAddressType
_VRtrInetSvcIpRangeAddrType_Object = MibTableColumn
vRtrInetSvcIpRangeAddrType = _VRtrInetSvcIpRangeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 28, 1, 1),
    _VRtrInetSvcIpRangeAddrType_Type()
)
vRtrInetSvcIpRangeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetSvcIpRangeAddrType.setStatus("current")
_VRtrInetSvcIpRangeAddr_Type = InetAddress
_VRtrInetSvcIpRangeAddr_Object = MibTableColumn
vRtrInetSvcIpRangeAddr = _VRtrInetSvcIpRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 28, 1, 2),
    _VRtrInetSvcIpRangeAddr_Type()
)
vRtrInetSvcIpRangeAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetSvcIpRangeAddr.setStatus("current")
_VRtrInetSvcIpRangePfxLen_Type = InetAddressPrefixLength
_VRtrInetSvcIpRangePfxLen_Object = MibTableColumn
vRtrInetSvcIpRangePfxLen = _VRtrInetSvcIpRangePfxLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 28, 1, 3),
    _VRtrInetSvcIpRangePfxLen_Type()
)
vRtrInetSvcIpRangePfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrInetSvcIpRangePfxLen.setStatus("current")
_VRtrInetSvcIpRangeRowStatus_Type = RowStatus
_VRtrInetSvcIpRangeRowStatus_Object = MibTableColumn
vRtrInetSvcIpRangeRowStatus = _VRtrInetSvcIpRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 28, 1, 4),
    _VRtrInetSvcIpRangeRowStatus_Type()
)
vRtrInetSvcIpRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetSvcIpRangeRowStatus.setStatus("current")


class _VRtrInetSvcIpRangeExclusive_Type(TruthValue):
    """Custom type vRtrInetSvcIpRangeExclusive based on TruthValue"""


_VRtrInetSvcIpRangeExclusive_Object = MibTableColumn
vRtrInetSvcIpRangeExclusive = _VRtrInetSvcIpRangeExclusive_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 28, 1, 5),
    _VRtrInetSvcIpRangeExclusive_Type()
)
vRtrInetSvcIpRangeExclusive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrInetSvcIpRangeExclusive.setStatus("current")
_VRtrIcmp6Table_Object = MibTable
vRtrIcmp6Table = _VRtrIcmp6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31)
)
if mibBuilder.loadTexts:
    vRtrIcmp6Table.setStatus("current")
_VRtrIcmp6Entry_Object = MibTableRow
vRtrIcmp6Entry = _VRtrIcmp6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1)
)
if mibBuilder.loadTexts:
    vRtrIcmp6Entry.setStatus("current")
_VRtrIcmp6InMsgs_Type = Counter32
_VRtrIcmp6InMsgs_Object = MibTableColumn
vRtrIcmp6InMsgs = _VRtrIcmp6InMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 1),
    _VRtrIcmp6InMsgs_Type()
)
vRtrIcmp6InMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InMsgs.setStatus("current")
_VRtrIcmp6InErrors_Type = Counter32
_VRtrIcmp6InErrors_Object = MibTableColumn
vRtrIcmp6InErrors = _VRtrIcmp6InErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 2),
    _VRtrIcmp6InErrors_Type()
)
vRtrIcmp6InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InErrors.setStatus("current")
_VRtrIcmp6InDestUnreachs_Type = Counter32
_VRtrIcmp6InDestUnreachs_Object = MibTableColumn
vRtrIcmp6InDestUnreachs = _VRtrIcmp6InDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 3),
    _VRtrIcmp6InDestUnreachs_Type()
)
vRtrIcmp6InDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InDestUnreachs.setStatus("current")
_VRtrIcmp6InAdminProhibs_Type = Counter32
_VRtrIcmp6InAdminProhibs_Object = MibTableColumn
vRtrIcmp6InAdminProhibs = _VRtrIcmp6InAdminProhibs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 4),
    _VRtrIcmp6InAdminProhibs_Type()
)
vRtrIcmp6InAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InAdminProhibs.setStatus("current")
_VRtrIcmp6InTimeExcds_Type = Counter32
_VRtrIcmp6InTimeExcds_Object = MibTableColumn
vRtrIcmp6InTimeExcds = _VRtrIcmp6InTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 5),
    _VRtrIcmp6InTimeExcds_Type()
)
vRtrIcmp6InTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InTimeExcds.setStatus("current")
_VRtrIcmp6InParmProblems_Type = Counter32
_VRtrIcmp6InParmProblems_Object = MibTableColumn
vRtrIcmp6InParmProblems = _VRtrIcmp6InParmProblems_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 6),
    _VRtrIcmp6InParmProblems_Type()
)
vRtrIcmp6InParmProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InParmProblems.setStatus("current")
_VRtrIcmp6InPktTooBigs_Type = Counter32
_VRtrIcmp6InPktTooBigs_Object = MibTableColumn
vRtrIcmp6InPktTooBigs = _VRtrIcmp6InPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 7),
    _VRtrIcmp6InPktTooBigs_Type()
)
vRtrIcmp6InPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InPktTooBigs.setStatus("current")
_VRtrIcmp6InEchos_Type = Counter32
_VRtrIcmp6InEchos_Object = MibTableColumn
vRtrIcmp6InEchos = _VRtrIcmp6InEchos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 8),
    _VRtrIcmp6InEchos_Type()
)
vRtrIcmp6InEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InEchos.setStatus("current")
_VRtrIcmp6InEchoReplies_Type = Counter32
_VRtrIcmp6InEchoReplies_Object = MibTableColumn
vRtrIcmp6InEchoReplies = _VRtrIcmp6InEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 9),
    _VRtrIcmp6InEchoReplies_Type()
)
vRtrIcmp6InEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InEchoReplies.setStatus("current")
_VRtrIcmp6InRtrSolicits_Type = Counter32
_VRtrIcmp6InRtrSolicits_Object = MibTableColumn
vRtrIcmp6InRtrSolicits = _VRtrIcmp6InRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 10),
    _VRtrIcmp6InRtrSolicits_Type()
)
vRtrIcmp6InRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InRtrSolicits.setStatus("current")
_VRtrIcmp6InRtrAdvertisements_Type = Counter32
_VRtrIcmp6InRtrAdvertisements_Object = MibTableColumn
vRtrIcmp6InRtrAdvertisements = _VRtrIcmp6InRtrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 11),
    _VRtrIcmp6InRtrAdvertisements_Type()
)
vRtrIcmp6InRtrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InRtrAdvertisements.setStatus("current")
_VRtrIcmp6InNbrSolicits_Type = Counter32
_VRtrIcmp6InNbrSolicits_Object = MibTableColumn
vRtrIcmp6InNbrSolicits = _VRtrIcmp6InNbrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 12),
    _VRtrIcmp6InNbrSolicits_Type()
)
vRtrIcmp6InNbrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InNbrSolicits.setStatus("current")
_VRtrIcmp6InNbrAdvertisements_Type = Counter32
_VRtrIcmp6InNbrAdvertisements_Object = MibTableColumn
vRtrIcmp6InNbrAdvertisements = _VRtrIcmp6InNbrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 13),
    _VRtrIcmp6InNbrAdvertisements_Type()
)
vRtrIcmp6InNbrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InNbrAdvertisements.setStatus("current")
_VRtrIcmp6InRedirects_Type = Counter32
_VRtrIcmp6InRedirects_Object = MibTableColumn
vRtrIcmp6InRedirects = _VRtrIcmp6InRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 14),
    _VRtrIcmp6InRedirects_Type()
)
vRtrIcmp6InRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InRedirects.setStatus("current")
_VRtrIcmp6InGrpMembQueries_Type = Counter32
_VRtrIcmp6InGrpMembQueries_Object = MibTableColumn
vRtrIcmp6InGrpMembQueries = _VRtrIcmp6InGrpMembQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 15),
    _VRtrIcmp6InGrpMembQueries_Type()
)
vRtrIcmp6InGrpMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InGrpMembQueries.setStatus("current")
_VRtrIcmp6InGrpMembResponses_Type = Counter32
_VRtrIcmp6InGrpMembResponses_Object = MibTableColumn
vRtrIcmp6InGrpMembResponses = _VRtrIcmp6InGrpMembResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 16),
    _VRtrIcmp6InGrpMembResponses_Type()
)
vRtrIcmp6InGrpMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InGrpMembResponses.setStatus("current")
_VRtrIcmp6InGrpMembReductions_Type = Counter32
_VRtrIcmp6InGrpMembReductions_Object = MibTableColumn
vRtrIcmp6InGrpMembReductions = _VRtrIcmp6InGrpMembReductions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 17),
    _VRtrIcmp6InGrpMembReductions_Type()
)
vRtrIcmp6InGrpMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6InGrpMembReductions.setStatus("current")
_VRtrIcmp6OutMsgs_Type = Counter32
_VRtrIcmp6OutMsgs_Object = MibTableColumn
vRtrIcmp6OutMsgs = _VRtrIcmp6OutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 18),
    _VRtrIcmp6OutMsgs_Type()
)
vRtrIcmp6OutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutMsgs.setStatus("current")
_VRtrIcmp6OutErrors_Type = Counter32
_VRtrIcmp6OutErrors_Object = MibTableColumn
vRtrIcmp6OutErrors = _VRtrIcmp6OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 19),
    _VRtrIcmp6OutErrors_Type()
)
vRtrIcmp6OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutErrors.setStatus("current")
_VRtrIcmp6OutDestUnreachs_Type = Counter32
_VRtrIcmp6OutDestUnreachs_Object = MibTableColumn
vRtrIcmp6OutDestUnreachs = _VRtrIcmp6OutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 20),
    _VRtrIcmp6OutDestUnreachs_Type()
)
vRtrIcmp6OutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutDestUnreachs.setStatus("current")
_VRtrIcmp6OutAdminProhibs_Type = Counter32
_VRtrIcmp6OutAdminProhibs_Object = MibTableColumn
vRtrIcmp6OutAdminProhibs = _VRtrIcmp6OutAdminProhibs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 21),
    _VRtrIcmp6OutAdminProhibs_Type()
)
vRtrIcmp6OutAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutAdminProhibs.setStatus("current")
_VRtrIcmp6OutTimeExcds_Type = Counter32
_VRtrIcmp6OutTimeExcds_Object = MibTableColumn
vRtrIcmp6OutTimeExcds = _VRtrIcmp6OutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 22),
    _VRtrIcmp6OutTimeExcds_Type()
)
vRtrIcmp6OutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutTimeExcds.setStatus("current")
_VRtrIcmp6OutParmProblems_Type = Counter32
_VRtrIcmp6OutParmProblems_Object = MibTableColumn
vRtrIcmp6OutParmProblems = _VRtrIcmp6OutParmProblems_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 23),
    _VRtrIcmp6OutParmProblems_Type()
)
vRtrIcmp6OutParmProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutParmProblems.setStatus("current")
_VRtrIcmp6OutPktTooBigs_Type = Counter32
_VRtrIcmp6OutPktTooBigs_Object = MibTableColumn
vRtrIcmp6OutPktTooBigs = _VRtrIcmp6OutPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 24),
    _VRtrIcmp6OutPktTooBigs_Type()
)
vRtrIcmp6OutPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutPktTooBigs.setStatus("current")
_VRtrIcmp6OutEchos_Type = Counter32
_VRtrIcmp6OutEchos_Object = MibTableColumn
vRtrIcmp6OutEchos = _VRtrIcmp6OutEchos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 25),
    _VRtrIcmp6OutEchos_Type()
)
vRtrIcmp6OutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutEchos.setStatus("current")
_VRtrIcmp6OutEchoReplies_Type = Counter32
_VRtrIcmp6OutEchoReplies_Object = MibTableColumn
vRtrIcmp6OutEchoReplies = _VRtrIcmp6OutEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 26),
    _VRtrIcmp6OutEchoReplies_Type()
)
vRtrIcmp6OutEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutEchoReplies.setStatus("current")
_VRtrIcmp6OutRtrSolicits_Type = Counter32
_VRtrIcmp6OutRtrSolicits_Object = MibTableColumn
vRtrIcmp6OutRtrSolicits = _VRtrIcmp6OutRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 27),
    _VRtrIcmp6OutRtrSolicits_Type()
)
vRtrIcmp6OutRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutRtrSolicits.setStatus("current")
_VRtrIcmp6OutRtrAdvertisements_Type = Counter32
_VRtrIcmp6OutRtrAdvertisements_Object = MibTableColumn
vRtrIcmp6OutRtrAdvertisements = _VRtrIcmp6OutRtrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 28),
    _VRtrIcmp6OutRtrAdvertisements_Type()
)
vRtrIcmp6OutRtrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutRtrAdvertisements.setStatus("current")
_VRtrIcmp6OutNbrSolicits_Type = Counter32
_VRtrIcmp6OutNbrSolicits_Object = MibTableColumn
vRtrIcmp6OutNbrSolicits = _VRtrIcmp6OutNbrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 29),
    _VRtrIcmp6OutNbrSolicits_Type()
)
vRtrIcmp6OutNbrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutNbrSolicits.setStatus("current")
_VRtrIcmp6OutNbrAdvertisements_Type = Counter32
_VRtrIcmp6OutNbrAdvertisements_Object = MibTableColumn
vRtrIcmp6OutNbrAdvertisements = _VRtrIcmp6OutNbrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 30),
    _VRtrIcmp6OutNbrAdvertisements_Type()
)
vRtrIcmp6OutNbrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutNbrAdvertisements.setStatus("current")
_VRtrIcmp6OutRedirects_Type = Counter32
_VRtrIcmp6OutRedirects_Object = MibTableColumn
vRtrIcmp6OutRedirects = _VRtrIcmp6OutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 31),
    _VRtrIcmp6OutRedirects_Type()
)
vRtrIcmp6OutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutRedirects.setStatus("current")
_VRtrIcmp6OutGrpMembQueries_Type = Counter32
_VRtrIcmp6OutGrpMembQueries_Object = MibTableColumn
vRtrIcmp6OutGrpMembQueries = _VRtrIcmp6OutGrpMembQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 32),
    _VRtrIcmp6OutGrpMembQueries_Type()
)
vRtrIcmp6OutGrpMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutGrpMembQueries.setStatus("current")
_VRtrIcmp6OutGrpMembResponses_Type = Counter32
_VRtrIcmp6OutGrpMembResponses_Object = MibTableColumn
vRtrIcmp6OutGrpMembResponses = _VRtrIcmp6OutGrpMembResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 33),
    _VRtrIcmp6OutGrpMembResponses_Type()
)
vRtrIcmp6OutGrpMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutGrpMembResponses.setStatus("current")
_VRtrIcmp6OutGrpMembReductions_Type = Counter32
_VRtrIcmp6OutGrpMembReductions_Object = MibTableColumn
vRtrIcmp6OutGrpMembReductions = _VRtrIcmp6OutGrpMembReductions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 31, 1, 34),
    _VRtrIcmp6OutGrpMembReductions_Type()
)
vRtrIcmp6OutGrpMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIcmp6OutGrpMembReductions.setStatus("current")
_VRtrIfIcmp6Table_Object = MibTable
vRtrIfIcmp6Table = _VRtrIfIcmp6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32)
)
if mibBuilder.loadTexts:
    vRtrIfIcmp6Table.setStatus("current")
_VRtrIfIcmp6Entry_Object = MibTableRow
vRtrIfIcmp6Entry = _VRtrIfIcmp6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1)
)
if mibBuilder.loadTexts:
    vRtrIfIcmp6Entry.setStatus("current")
_VRtrIfIcmp6InMsgs_Type = Counter32
_VRtrIfIcmp6InMsgs_Object = MibTableColumn
vRtrIfIcmp6InMsgs = _VRtrIfIcmp6InMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 1),
    _VRtrIfIcmp6InMsgs_Type()
)
vRtrIfIcmp6InMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InMsgs.setStatus("current")
_VRtrIfIcmp6InErrors_Type = Counter32
_VRtrIfIcmp6InErrors_Object = MibTableColumn
vRtrIfIcmp6InErrors = _VRtrIfIcmp6InErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 2),
    _VRtrIfIcmp6InErrors_Type()
)
vRtrIfIcmp6InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InErrors.setStatus("current")
_VRtrIfIcmp6InDestUnreachs_Type = Counter32
_VRtrIfIcmp6InDestUnreachs_Object = MibTableColumn
vRtrIfIcmp6InDestUnreachs = _VRtrIfIcmp6InDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 3),
    _VRtrIfIcmp6InDestUnreachs_Type()
)
vRtrIfIcmp6InDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InDestUnreachs.setStatus("current")
_VRtrIfIcmp6InAdminProhibs_Type = Counter32
_VRtrIfIcmp6InAdminProhibs_Object = MibTableColumn
vRtrIfIcmp6InAdminProhibs = _VRtrIfIcmp6InAdminProhibs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 4),
    _VRtrIfIcmp6InAdminProhibs_Type()
)
vRtrIfIcmp6InAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InAdminProhibs.setStatus("current")
_VRtrIfIcmp6InTimeExcds_Type = Counter32
_VRtrIfIcmp6InTimeExcds_Object = MibTableColumn
vRtrIfIcmp6InTimeExcds = _VRtrIfIcmp6InTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 5),
    _VRtrIfIcmp6InTimeExcds_Type()
)
vRtrIfIcmp6InTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InTimeExcds.setStatus("current")
_VRtrIfIcmp6InParmProblems_Type = Counter32
_VRtrIfIcmp6InParmProblems_Object = MibTableColumn
vRtrIfIcmp6InParmProblems = _VRtrIfIcmp6InParmProblems_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 6),
    _VRtrIfIcmp6InParmProblems_Type()
)
vRtrIfIcmp6InParmProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InParmProblems.setStatus("current")
_VRtrIfIcmp6InPktTooBigs_Type = Counter32
_VRtrIfIcmp6InPktTooBigs_Object = MibTableColumn
vRtrIfIcmp6InPktTooBigs = _VRtrIfIcmp6InPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 7),
    _VRtrIfIcmp6InPktTooBigs_Type()
)
vRtrIfIcmp6InPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InPktTooBigs.setStatus("current")
_VRtrIfIcmp6InEchos_Type = Counter32
_VRtrIfIcmp6InEchos_Object = MibTableColumn
vRtrIfIcmp6InEchos = _VRtrIfIcmp6InEchos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 8),
    _VRtrIfIcmp6InEchos_Type()
)
vRtrIfIcmp6InEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InEchos.setStatus("current")
_VRtrIfIcmp6InEchoReplies_Type = Counter32
_VRtrIfIcmp6InEchoReplies_Object = MibTableColumn
vRtrIfIcmp6InEchoReplies = _VRtrIfIcmp6InEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 9),
    _VRtrIfIcmp6InEchoReplies_Type()
)
vRtrIfIcmp6InEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InEchoReplies.setStatus("current")
_VRtrIfIcmp6InRtrSolicits_Type = Counter32
_VRtrIfIcmp6InRtrSolicits_Object = MibTableColumn
vRtrIfIcmp6InRtrSolicits = _VRtrIfIcmp6InRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 10),
    _VRtrIfIcmp6InRtrSolicits_Type()
)
vRtrIfIcmp6InRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InRtrSolicits.setStatus("current")
_VRtrIfIcmp6InRtrAdvertisements_Type = Counter32
_VRtrIfIcmp6InRtrAdvertisements_Object = MibTableColumn
vRtrIfIcmp6InRtrAdvertisements = _VRtrIfIcmp6InRtrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 11),
    _VRtrIfIcmp6InRtrAdvertisements_Type()
)
vRtrIfIcmp6InRtrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InRtrAdvertisements.setStatus("current")
_VRtrIfIcmp6InNbrSolicits_Type = Counter32
_VRtrIfIcmp6InNbrSolicits_Object = MibTableColumn
vRtrIfIcmp6InNbrSolicits = _VRtrIfIcmp6InNbrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 12),
    _VRtrIfIcmp6InNbrSolicits_Type()
)
vRtrIfIcmp6InNbrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InNbrSolicits.setStatus("current")
_VRtrIfIcmp6InNbrAdvertisements_Type = Counter32
_VRtrIfIcmp6InNbrAdvertisements_Object = MibTableColumn
vRtrIfIcmp6InNbrAdvertisements = _VRtrIfIcmp6InNbrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 13),
    _VRtrIfIcmp6InNbrAdvertisements_Type()
)
vRtrIfIcmp6InNbrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InNbrAdvertisements.setStatus("current")
_VRtrIfIcmp6InRedirects_Type = Counter32
_VRtrIfIcmp6InRedirects_Object = MibTableColumn
vRtrIfIcmp6InRedirects = _VRtrIfIcmp6InRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 14),
    _VRtrIfIcmp6InRedirects_Type()
)
vRtrIfIcmp6InRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InRedirects.setStatus("current")
_VRtrIfIcmp6InGrpMembQueries_Type = Counter32
_VRtrIfIcmp6InGrpMembQueries_Object = MibTableColumn
vRtrIfIcmp6InGrpMembQueries = _VRtrIfIcmp6InGrpMembQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 15),
    _VRtrIfIcmp6InGrpMembQueries_Type()
)
vRtrIfIcmp6InGrpMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InGrpMembQueries.setStatus("current")
_VRtrIfIcmp6InGrpMembResponses_Type = Counter32
_VRtrIfIcmp6InGrpMembResponses_Object = MibTableColumn
vRtrIfIcmp6InGrpMembResponses = _VRtrIfIcmp6InGrpMembResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 16),
    _VRtrIfIcmp6InGrpMembResponses_Type()
)
vRtrIfIcmp6InGrpMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InGrpMembResponses.setStatus("current")
_VRtrIfIcmp6InGrpMembReductions_Type = Counter32
_VRtrIfIcmp6InGrpMembReductions_Object = MibTableColumn
vRtrIfIcmp6InGrpMembReductions = _VRtrIfIcmp6InGrpMembReductions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 17),
    _VRtrIfIcmp6InGrpMembReductions_Type()
)
vRtrIfIcmp6InGrpMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6InGrpMembReductions.setStatus("current")
_VRtrIfIcmp6OutMsgs_Type = Counter32
_VRtrIfIcmp6OutMsgs_Object = MibTableColumn
vRtrIfIcmp6OutMsgs = _VRtrIfIcmp6OutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 18),
    _VRtrIfIcmp6OutMsgs_Type()
)
vRtrIfIcmp6OutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutMsgs.setStatus("current")
_VRtrIfIcmp6OutErrors_Type = Counter32
_VRtrIfIcmp6OutErrors_Object = MibTableColumn
vRtrIfIcmp6OutErrors = _VRtrIfIcmp6OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 19),
    _VRtrIfIcmp6OutErrors_Type()
)
vRtrIfIcmp6OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutErrors.setStatus("current")
_VRtrIfIcmp6OutDestUnreachs_Type = Counter32
_VRtrIfIcmp6OutDestUnreachs_Object = MibTableColumn
vRtrIfIcmp6OutDestUnreachs = _VRtrIfIcmp6OutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 20),
    _VRtrIfIcmp6OutDestUnreachs_Type()
)
vRtrIfIcmp6OutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutDestUnreachs.setStatus("current")
_VRtrIfIcmp6OutAdminProhibs_Type = Counter32
_VRtrIfIcmp6OutAdminProhibs_Object = MibTableColumn
vRtrIfIcmp6OutAdminProhibs = _VRtrIfIcmp6OutAdminProhibs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 21),
    _VRtrIfIcmp6OutAdminProhibs_Type()
)
vRtrIfIcmp6OutAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutAdminProhibs.setStatus("current")
_VRtrIfIcmp6OutTimeExcds_Type = Counter32
_VRtrIfIcmp6OutTimeExcds_Object = MibTableColumn
vRtrIfIcmp6OutTimeExcds = _VRtrIfIcmp6OutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 22),
    _VRtrIfIcmp6OutTimeExcds_Type()
)
vRtrIfIcmp6OutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutTimeExcds.setStatus("current")
_VRtrIfIcmp6OutParmProblems_Type = Counter32
_VRtrIfIcmp6OutParmProblems_Object = MibTableColumn
vRtrIfIcmp6OutParmProblems = _VRtrIfIcmp6OutParmProblems_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 23),
    _VRtrIfIcmp6OutParmProblems_Type()
)
vRtrIfIcmp6OutParmProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutParmProblems.setStatus("current")
_VRtrIfIcmp6OutPktTooBigs_Type = Counter32
_VRtrIfIcmp6OutPktTooBigs_Object = MibTableColumn
vRtrIfIcmp6OutPktTooBigs = _VRtrIfIcmp6OutPktTooBigs_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 24),
    _VRtrIfIcmp6OutPktTooBigs_Type()
)
vRtrIfIcmp6OutPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutPktTooBigs.setStatus("current")
_VRtrIfIcmp6OutEchos_Type = Counter32
_VRtrIfIcmp6OutEchos_Object = MibTableColumn
vRtrIfIcmp6OutEchos = _VRtrIfIcmp6OutEchos_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 25),
    _VRtrIfIcmp6OutEchos_Type()
)
vRtrIfIcmp6OutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutEchos.setStatus("current")
_VRtrIfIcmp6OutEchoReplies_Type = Counter32
_VRtrIfIcmp6OutEchoReplies_Object = MibTableColumn
vRtrIfIcmp6OutEchoReplies = _VRtrIfIcmp6OutEchoReplies_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 26),
    _VRtrIfIcmp6OutEchoReplies_Type()
)
vRtrIfIcmp6OutEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutEchoReplies.setStatus("current")
_VRtrIfIcmp6OutRtrSolicits_Type = Counter32
_VRtrIfIcmp6OutRtrSolicits_Object = MibTableColumn
vRtrIfIcmp6OutRtrSolicits = _VRtrIfIcmp6OutRtrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 27),
    _VRtrIfIcmp6OutRtrSolicits_Type()
)
vRtrIfIcmp6OutRtrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutRtrSolicits.setStatus("current")
_VRtrIfIcmp6OutRtrSolicitsTime_Type = TimeStamp
_VRtrIfIcmp6OutRtrSolicitsTime_Object = MibTableColumn
vRtrIfIcmp6OutRtrSolicitsTime = _VRtrIfIcmp6OutRtrSolicitsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 28),
    _VRtrIfIcmp6OutRtrSolicitsTime_Type()
)
vRtrIfIcmp6OutRtrSolicitsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutRtrSolicitsTime.setStatus("current")
_VRtrIfIcmp6OutRtrAdvertisements_Type = Counter32
_VRtrIfIcmp6OutRtrAdvertisements_Object = MibTableColumn
vRtrIfIcmp6OutRtrAdvertisements = _VRtrIfIcmp6OutRtrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 29),
    _VRtrIfIcmp6OutRtrAdvertisements_Type()
)
vRtrIfIcmp6OutRtrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutRtrAdvertisements.setStatus("current")
_VRtrIfIcmp6OutRtrAdvTime_Type = TimeStamp
_VRtrIfIcmp6OutRtrAdvTime_Object = MibTableColumn
vRtrIfIcmp6OutRtrAdvTime = _VRtrIfIcmp6OutRtrAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 30),
    _VRtrIfIcmp6OutRtrAdvTime_Type()
)
vRtrIfIcmp6OutRtrAdvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutRtrAdvTime.setStatus("current")
_VRtrIfIcmp6OutNbrSolicits_Type = Counter32
_VRtrIfIcmp6OutNbrSolicits_Object = MibTableColumn
vRtrIfIcmp6OutNbrSolicits = _VRtrIfIcmp6OutNbrSolicits_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 31),
    _VRtrIfIcmp6OutNbrSolicits_Type()
)
vRtrIfIcmp6OutNbrSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutNbrSolicits.setStatus("current")
_VRtrIfIcmp6OutNbrSolicitsTime_Type = TimeStamp
_VRtrIfIcmp6OutNbrSolicitsTime_Object = MibTableColumn
vRtrIfIcmp6OutNbrSolicitsTime = _VRtrIfIcmp6OutNbrSolicitsTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 32),
    _VRtrIfIcmp6OutNbrSolicitsTime_Type()
)
vRtrIfIcmp6OutNbrSolicitsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutNbrSolicitsTime.setStatus("current")
_VRtrIfIcmp6OutNbrAdvertisements_Type = Counter32
_VRtrIfIcmp6OutNbrAdvertisements_Object = MibTableColumn
vRtrIfIcmp6OutNbrAdvertisements = _VRtrIfIcmp6OutNbrAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 33),
    _VRtrIfIcmp6OutNbrAdvertisements_Type()
)
vRtrIfIcmp6OutNbrAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutNbrAdvertisements.setStatus("current")
_VRtrIfIcmp6OutNbrAdvTime_Type = TimeStamp
_VRtrIfIcmp6OutNbrAdvTime_Object = MibTableColumn
vRtrIfIcmp6OutNbrAdvTime = _VRtrIfIcmp6OutNbrAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 34),
    _VRtrIfIcmp6OutNbrAdvTime_Type()
)
vRtrIfIcmp6OutNbrAdvTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutNbrAdvTime.setStatus("current")
_VRtrIfIcmp6OutRedirects_Type = Counter32
_VRtrIfIcmp6OutRedirects_Object = MibTableColumn
vRtrIfIcmp6OutRedirects = _VRtrIfIcmp6OutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 35),
    _VRtrIfIcmp6OutRedirects_Type()
)
vRtrIfIcmp6OutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutRedirects.setStatus("current")
_VRtrIfIcmp6OutGrpMembQueries_Type = Counter32
_VRtrIfIcmp6OutGrpMembQueries_Object = MibTableColumn
vRtrIfIcmp6OutGrpMembQueries = _VRtrIfIcmp6OutGrpMembQueries_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 36),
    _VRtrIfIcmp6OutGrpMembQueries_Type()
)
vRtrIfIcmp6OutGrpMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutGrpMembQueries.setStatus("current")
_VRtrIfIcmp6OutGrpMembResponses_Type = Counter32
_VRtrIfIcmp6OutGrpMembResponses_Object = MibTableColumn
vRtrIfIcmp6OutGrpMembResponses = _VRtrIfIcmp6OutGrpMembResponses_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 37),
    _VRtrIfIcmp6OutGrpMembResponses_Type()
)
vRtrIfIcmp6OutGrpMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutGrpMembResponses.setStatus("current")
_VRtrIfIcmp6OutGrpMembReductions_Type = Counter32
_VRtrIfIcmp6OutGrpMembReductions_Object = MibTableColumn
vRtrIfIcmp6OutGrpMembReductions = _VRtrIfIcmp6OutGrpMembReductions_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 32, 1, 38),
    _VRtrIfIcmp6OutGrpMembReductions_Type()
)
vRtrIfIcmp6OutGrpMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfIcmp6OutGrpMembReductions.setStatus("current")
_VRtrIfBfdTable_Object = MibTable
vRtrIfBfdTable = _VRtrIfBfdTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 33)
)
if mibBuilder.loadTexts:
    vRtrIfBfdTable.setStatus("current")
_VRtrIfBfdEntry_Object = MibTableRow
vRtrIfBfdEntry = _VRtrIfBfdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 33, 1)
)
if mibBuilder.loadTexts:
    vRtrIfBfdEntry.setStatus("current")
_VRtrIfBfdAdminState_Type = TmnxAdminState
_VRtrIfBfdAdminState_Object = MibTableColumn
vRtrIfBfdAdminState = _VRtrIfBfdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 33, 1, 1),
    _VRtrIfBfdAdminState_Type()
)
vRtrIfBfdAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdAdminState.setStatus("current")


class _VRtrIfBfdTransmitInterval_Type(Unsigned32):
    """Custom type vRtrIfBfdTransmitInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_VRtrIfBfdTransmitInterval_Type.__name__ = "Unsigned32"
_VRtrIfBfdTransmitInterval_Object = MibTableColumn
vRtrIfBfdTransmitInterval = _VRtrIfBfdTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 33, 1, 2),
    _VRtrIfBfdTransmitInterval_Type()
)
vRtrIfBfdTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdTransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdTransmitInterval.setUnits("milliseconds")


class _VRtrIfBfdReceiveInterval_Type(Unsigned32):
    """Custom type vRtrIfBfdReceiveInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 100000),
    )


_VRtrIfBfdReceiveInterval_Type.__name__ = "Unsigned32"
_VRtrIfBfdReceiveInterval_Object = MibTableColumn
vRtrIfBfdReceiveInterval = _VRtrIfBfdReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 33, 1, 3),
    _VRtrIfBfdReceiveInterval_Type()
)
vRtrIfBfdReceiveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdReceiveInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdReceiveInterval.setUnits("milliseconds")


class _VRtrIfBfdMultiplier_Type(Unsigned32):
    """Custom type vRtrIfBfdMultiplier based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_VRtrIfBfdMultiplier_Type.__name__ = "Unsigned32"
_VRtrIfBfdMultiplier_Object = MibTableColumn
vRtrIfBfdMultiplier = _VRtrIfBfdMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 33, 1, 4),
    _VRtrIfBfdMultiplier_Type()
)
vRtrIfBfdMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdMultiplier.setStatus("current")


class _VRtrIfBfdEchoInterval_Type(Unsigned32):
    """Custom type vRtrIfBfdEchoInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(100, 100000),
    )


_VRtrIfBfdEchoInterval_Type.__name__ = "Unsigned32"
_VRtrIfBfdEchoInterval_Object = MibTableColumn
vRtrIfBfdEchoInterval = _VRtrIfBfdEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 33, 1, 5),
    _VRtrIfBfdEchoInterval_Type()
)
vRtrIfBfdEchoInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIfBfdEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdEchoInterval.setUnits("milliseconds")
_VRtrIfBfdSessionTable_Object = MibTable
vRtrIfBfdSessionTable = _VRtrIfBfdSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34)
)
if mibBuilder.loadTexts:
    vRtrIfBfdSessionTable.setStatus("current")
_VRtrIfBfdSessionEntry_Object = MibTableRow
vRtrIfBfdSessionEntry = _VRtrIfBfdSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1)
)
vRtrIfBfdSessionEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclAddr"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionRemAddrType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionRemAddr"),
)
if mibBuilder.loadTexts:
    vRtrIfBfdSessionEntry.setStatus("current")
_VRtrIfBfdSessionLclAddrType_Type = InetAddressType
_VRtrIfBfdSessionLclAddrType_Object = MibTableColumn
vRtrIfBfdSessionLclAddrType = _VRtrIfBfdSessionLclAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 1),
    _VRtrIfBfdSessionLclAddrType_Type()
)
vRtrIfBfdSessionLclAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionLclAddrType.setStatus("current")


class _VRtrIfBfdSessionLclAddr_Type(InetAddress):
    """Custom type vRtrIfBfdSessionLclAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrIfBfdSessionLclAddr_Type.__name__ = "InetAddress"
_VRtrIfBfdSessionLclAddr_Object = MibTableColumn
vRtrIfBfdSessionLclAddr = _VRtrIfBfdSessionLclAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 2),
    _VRtrIfBfdSessionLclAddr_Type()
)
vRtrIfBfdSessionLclAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionLclAddr.setStatus("current")
_VRtrIfBfdSessionRemAddrType_Type = InetAddressType
_VRtrIfBfdSessionRemAddrType_Object = MibTableColumn
vRtrIfBfdSessionRemAddrType = _VRtrIfBfdSessionRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 3),
    _VRtrIfBfdSessionRemAddrType_Type()
)
vRtrIfBfdSessionRemAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionRemAddrType.setStatus("current")


class _VRtrIfBfdSessionRemAddr_Type(InetAddress):
    """Custom type vRtrIfBfdSessionRemAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
    )


_VRtrIfBfdSessionRemAddr_Type.__name__ = "InetAddress"
_VRtrIfBfdSessionRemAddr_Object = MibTableColumn
vRtrIfBfdSessionRemAddr = _VRtrIfBfdSessionRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 4),
    _VRtrIfBfdSessionRemAddr_Type()
)
vRtrIfBfdSessionRemAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionRemAddr.setStatus("current")
_VRtrIfBfdSessionOperState_Type = TmnxOperState
_VRtrIfBfdSessionOperState_Object = MibTableColumn
vRtrIfBfdSessionOperState = _VRtrIfBfdSessionOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 5),
    _VRtrIfBfdSessionOperState_Type()
)
vRtrIfBfdSessionOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionOperState.setStatus("current")


class _VRtrIfBfdSessionState_Type(Integer32):
    """Custom type vRtrIfBfdSessionState based on Integer32"""
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
        *(("adminDown", 0),
          ("down", 1),
          ("init", 2),
          ("up", 3))
    )


_VRtrIfBfdSessionState_Type.__name__ = "Integer32"
_VRtrIfBfdSessionState_Object = MibTableColumn
vRtrIfBfdSessionState = _VRtrIfBfdSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 6),
    _VRtrIfBfdSessionState_Type()
)
vRtrIfBfdSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionState.setStatus("current")


class _VRtrIfBfdSessionOperFlags_Type(Bits):
    """Custom type vRtrIfBfdSessionOperFlags based on Bits"""
    namedValues = NamedValues(
        *(("adminClear", 7),
          ("echoFailed", 2),
          ("fwdPlaneReset", 4),
          ("nbrAdminDown", 6),
          ("nbrSignalDown", 3),
          ("noHeartBeat", 1),
          ("noProtocols", 0),
          ("pathDown", 5))
    )

_VRtrIfBfdSessionOperFlags_Type.__name__ = "Bits"
_VRtrIfBfdSessionOperFlags_Object = MibTableColumn
vRtrIfBfdSessionOperFlags = _VRtrIfBfdSessionOperFlags_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 7),
    _VRtrIfBfdSessionOperFlags_Type()
)
vRtrIfBfdSessionOperFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionOperFlags.setStatus("current")
_VRtrIfBfdSessionMesgRecv_Type = Counter32
_VRtrIfBfdSessionMesgRecv_Object = MibTableColumn
vRtrIfBfdSessionMesgRecv = _VRtrIfBfdSessionMesgRecv_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 8),
    _VRtrIfBfdSessionMesgRecv_Type()
)
vRtrIfBfdSessionMesgRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionMesgRecv.setStatus("current")
_VRtrIfBfdSessionMesgSent_Type = Counter32
_VRtrIfBfdSessionMesgSent_Object = MibTableColumn
vRtrIfBfdSessionMesgSent = _VRtrIfBfdSessionMesgSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 9),
    _VRtrIfBfdSessionMesgSent_Type()
)
vRtrIfBfdSessionMesgSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionMesgSent.setStatus("current")
_VRtrIfBfdSessionLastDownTime_Type = TimeStamp
_VRtrIfBfdSessionLastDownTime_Object = MibTableColumn
vRtrIfBfdSessionLastDownTime = _VRtrIfBfdSessionLastDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 10),
    _VRtrIfBfdSessionLastDownTime_Type()
)
vRtrIfBfdSessionLastDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionLastDownTime.setStatus("current")
_VRtrIfBfdSessionLastUpTime_Type = TimeStamp
_VRtrIfBfdSessionLastUpTime_Object = MibTableColumn
vRtrIfBfdSessionLastUpTime = _VRtrIfBfdSessionLastUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 11),
    _VRtrIfBfdSessionLastUpTime_Type()
)
vRtrIfBfdSessionLastUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionLastUpTime.setStatus("current")
_VRtrIfBfdSessionUpCount_Type = Counter32
_VRtrIfBfdSessionUpCount_Object = MibTableColumn
vRtrIfBfdSessionUpCount = _VRtrIfBfdSessionUpCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 12),
    _VRtrIfBfdSessionUpCount_Type()
)
vRtrIfBfdSessionUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionUpCount.setStatus("current")
_VRtrIfBfdSessionDownCount_Type = Counter32
_VRtrIfBfdSessionDownCount_Object = MibTableColumn
vRtrIfBfdSessionDownCount = _VRtrIfBfdSessionDownCount_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 13),
    _VRtrIfBfdSessionDownCount_Type()
)
vRtrIfBfdSessionDownCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionDownCount.setStatus("current")
_VRtrIfBfdSessionLclDisc_Type = Unsigned32
_VRtrIfBfdSessionLclDisc_Object = MibTableColumn
vRtrIfBfdSessionLclDisc = _VRtrIfBfdSessionLclDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 14),
    _VRtrIfBfdSessionLclDisc_Type()
)
vRtrIfBfdSessionLclDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionLclDisc.setStatus("current")
_VRtrIfBfdSessionRemDisc_Type = Unsigned32
_VRtrIfBfdSessionRemDisc_Object = MibTableColumn
vRtrIfBfdSessionRemDisc = _VRtrIfBfdSessionRemDisc_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 15),
    _VRtrIfBfdSessionRemDisc_Type()
)
vRtrIfBfdSessionRemDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionRemDisc.setStatus("current")


class _VRtrIfBfdSessionProtocols_Type(Bits):
    """Custom type vRtrIfBfdSessionProtocols based on Bits"""
    namedValues = NamedValues(
        *(("bgp", 6),
          ("isis", 2),
          ("mcRing", 4),
          ("ospfv2", 0),
          ("pim", 1),
          ("rsvp", 5),
          ("staticRoute", 3))
    )

_VRtrIfBfdSessionProtocols_Type.__name__ = "Bits"
_VRtrIfBfdSessionProtocols_Object = MibTableColumn
vRtrIfBfdSessionProtocols = _VRtrIfBfdSessionProtocols_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 16),
    _VRtrIfBfdSessionProtocols_Type()
)
vRtrIfBfdSessionProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionProtocols.setStatus("current")
_VRtrIfBfdSessionTxInterval_Type = Unsigned32
_VRtrIfBfdSessionTxInterval_Object = MibTableColumn
vRtrIfBfdSessionTxInterval = _VRtrIfBfdSessionTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 17),
    _VRtrIfBfdSessionTxInterval_Type()
)
vRtrIfBfdSessionTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionTxInterval.setUnits("milliseconds")
_VRtrIfBfdSessionRxInterval_Type = Unsigned32
_VRtrIfBfdSessionRxInterval_Object = MibTableColumn
vRtrIfBfdSessionRxInterval = _VRtrIfBfdSessionRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 18),
    _VRtrIfBfdSessionRxInterval_Type()
)
vRtrIfBfdSessionRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionRxInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionRxInterval.setUnits("milliseconds")


class _VRtrIfBfdSessionType_Type(Integer32):
    """Custom type vRtrIfBfdSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpm", 2),
          ("iom", 1))
    )


_VRtrIfBfdSessionType_Type.__name__ = "Integer32"
_VRtrIfBfdSessionType_Object = MibTableColumn
vRtrIfBfdSessionType = _VRtrIfBfdSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 34, 1, 19),
    _VRtrIfBfdSessionType_Type()
)
vRtrIfBfdSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfBfdSessionType.setStatus("current")
_VRtrIfDHCP6TableLastChanged_Type = TimeStamp
_VRtrIfDHCP6TableLastChanged_Object = MibScalar
vRtrIfDHCP6TableLastChanged = _VRtrIfDHCP6TableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 35),
    _VRtrIfDHCP6TableLastChanged_Type()
)
vRtrIfDHCP6TableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCP6TableLastChanged.setStatus("current")
_VRtrIfDHCP6Table_Object = MibTable
vRtrIfDHCP6Table = _VRtrIfDHCP6Table_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36)
)
if mibBuilder.loadTexts:
    vRtrIfDHCP6Table.setStatus("current")
_VRtrIfDHCP6Entry_Object = MibTableRow
vRtrIfDHCP6Entry = _VRtrIfDHCP6Entry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1)
)
if mibBuilder.loadTexts:
    vRtrIfDHCP6Entry.setStatus("current")
_VRtrIfDHCP6LastChanged_Type = TimeStamp
_VRtrIfDHCP6LastChanged_Object = MibTableColumn
vRtrIfDHCP6LastChanged = _VRtrIfDHCP6LastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 1),
    _VRtrIfDHCP6LastChanged_Type()
)
vRtrIfDHCP6LastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCP6LastChanged.setStatus("current")


class _VRtrIfDHCP6AdminState_Type(TmnxAdminState):
    """Custom type vRtrIfDHCP6AdminState based on TmnxAdminState"""


_VRtrIfDHCP6AdminState_Object = MibTableColumn
vRtrIfDHCP6AdminState = _VRtrIfDHCP6AdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 2),
    _VRtrIfDHCP6AdminState_Type()
)
vRtrIfDHCP6AdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6AdminState.setStatus("current")


class _VRtrIfDHCP6OperState_Type(Integer32):
    """Custom type vRtrIfDHCP6OperState based on Integer32"""
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
        *(("down", 2),
          ("noIPv6Pfx", 3),
          ("noServerConfigured", 4),
          ("noValidSourceAddr", 5),
          ("up", 1))
    )


_VRtrIfDHCP6OperState_Type.__name__ = "Integer32"
_VRtrIfDHCP6OperState_Object = MibTableColumn
vRtrIfDHCP6OperState = _VRtrIfDHCP6OperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 3),
    _VRtrIfDHCP6OperState_Type()
)
vRtrIfDHCP6OperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCP6OperState.setStatus("current")


class _VRtrIfDHCP6Description_Type(TItemDescription):
    """Custom type vRtrIfDHCP6Description based on TItemDescription"""
    defaultHexValue = ""


_VRtrIfDHCP6Description_Object = MibTableColumn
vRtrIfDHCP6Description = _VRtrIfDHCP6Description_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 4),
    _VRtrIfDHCP6Description_Type()
)
vRtrIfDHCP6Description.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6Description.setStatus("current")


class _VRtrIfDHCP6RelayServer1_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer1 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer1_Object = MibTableColumn
vRtrIfDHCP6RelayServer1 = _VRtrIfDHCP6RelayServer1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 5),
    _VRtrIfDHCP6RelayServer1_Type()
)
vRtrIfDHCP6RelayServer1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer1.setStatus("current")


class _VRtrIfDHCP6RelayServer2_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer2 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer2_Object = MibTableColumn
vRtrIfDHCP6RelayServer2 = _VRtrIfDHCP6RelayServer2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 6),
    _VRtrIfDHCP6RelayServer2_Type()
)
vRtrIfDHCP6RelayServer2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer2.setStatus("current")


class _VRtrIfDHCP6RelayServer3_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer3 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer3_Object = MibTableColumn
vRtrIfDHCP6RelayServer3 = _VRtrIfDHCP6RelayServer3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 7),
    _VRtrIfDHCP6RelayServer3_Type()
)
vRtrIfDHCP6RelayServer3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer3.setStatus("current")


class _VRtrIfDHCP6RelayServer4_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer4 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer4_Object = MibTableColumn
vRtrIfDHCP6RelayServer4 = _VRtrIfDHCP6RelayServer4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 8),
    _VRtrIfDHCP6RelayServer4_Type()
)
vRtrIfDHCP6RelayServer4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer4.setStatus("current")


class _VRtrIfDHCP6RelayServer5_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer5 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer5_Object = MibTableColumn
vRtrIfDHCP6RelayServer5 = _VRtrIfDHCP6RelayServer5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 9),
    _VRtrIfDHCP6RelayServer5_Type()
)
vRtrIfDHCP6RelayServer5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer5.setStatus("current")


class _VRtrIfDHCP6RelayServer6_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer6 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer6_Object = MibTableColumn
vRtrIfDHCP6RelayServer6 = _VRtrIfDHCP6RelayServer6_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 10),
    _VRtrIfDHCP6RelayServer6_Type()
)
vRtrIfDHCP6RelayServer6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer6.setStatus("current")


class _VRtrIfDHCP6RelayServer7_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer7 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer7_Object = MibTableColumn
vRtrIfDHCP6RelayServer7 = _VRtrIfDHCP6RelayServer7_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 11),
    _VRtrIfDHCP6RelayServer7_Type()
)
vRtrIfDHCP6RelayServer7.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer7.setStatus("current")


class _VRtrIfDHCP6RelayServer8_Type(InetAddressIPv6z):
    """Custom type vRtrIfDHCP6RelayServer8 based on InetAddressIPv6z"""
    defaultHexValue = "0000000000000000000000000000000000000000"


_VRtrIfDHCP6RelayServer8_Object = MibTableColumn
vRtrIfDHCP6RelayServer8 = _VRtrIfDHCP6RelayServer8_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 12),
    _VRtrIfDHCP6RelayServer8_Type()
)
vRtrIfDHCP6RelayServer8.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayServer8.setStatus("current")


class _VRtrIfDHCP6RelayItfIdOption_Type(Integer32):
    """Custom type vRtrIfDHCP6RelayItfIdOption based on Integer32"""
    defaultValue = 0

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
        *(("asciiTuple", 2),
          ("ifIndex", 1),
          ("none", 0),
          ("sapId", 3),
          ("string", 4))
    )


_VRtrIfDHCP6RelayItfIdOption_Type.__name__ = "Integer32"
_VRtrIfDHCP6RelayItfIdOption_Object = MibTableColumn
vRtrIfDHCP6RelayItfIdOption = _VRtrIfDHCP6RelayItfIdOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 13),
    _VRtrIfDHCP6RelayItfIdOption_Type()
)
vRtrIfDHCP6RelayItfIdOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RelayItfIdOption.setStatus("current")


class _VRtrIfDHCP6LeasePopulate_Type(Unsigned32):
    """Custom type vRtrIfDHCP6LeasePopulate based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VRtrIfDHCP6LeasePopulate_Type.__name__ = "Unsigned32"
_VRtrIfDHCP6LeasePopulate_Object = MibTableColumn
vRtrIfDHCP6LeasePopulate = _VRtrIfDHCP6LeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 14),
    _VRtrIfDHCP6LeasePopulate_Type()
)
vRtrIfDHCP6LeasePopulate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6LeasePopulate.setStatus("current")


class _VRtrIfDHCP6CurrLeasePopulate_Type(Unsigned32):
    """Custom type vRtrIfDHCP6CurrLeasePopulate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VRtrIfDHCP6CurrLeasePopulate_Type.__name__ = "Unsigned32"
_VRtrIfDHCP6CurrLeasePopulate_Object = MibTableColumn
vRtrIfDHCP6CurrLeasePopulate = _VRtrIfDHCP6CurrLeasePopulate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 15),
    _VRtrIfDHCP6CurrLeasePopulate_Type()
)
vRtrIfDHCP6CurrLeasePopulate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCP6CurrLeasePopulate.setStatus("current")


class _VRtrIfDHCP6SourceAddress_Type(InetAddressIPv6):
    """Custom type vRtrIfDHCP6SourceAddress based on InetAddressIPv6"""
    defaultHexValue = "00000000000000000000000000000000"


_VRtrIfDHCP6SourceAddress_Object = MibTableColumn
vRtrIfDHCP6SourceAddress = _VRtrIfDHCP6SourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 16),
    _VRtrIfDHCP6SourceAddress_Type()
)
vRtrIfDHCP6SourceAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6SourceAddress.setStatus("current")


class _VRtrIfDHCP6EnableNgbrResolution_Type(TruthValue):
    """Custom type vRtrIfDHCP6EnableNgbrResolution based on TruthValue"""


_VRtrIfDHCP6EnableNgbrResolution_Object = MibTableColumn
vRtrIfDHCP6EnableNgbrResolution = _VRtrIfDHCP6EnableNgbrResolution_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 17),
    _VRtrIfDHCP6EnableNgbrResolution_Type()
)
vRtrIfDHCP6EnableNgbrResolution.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6EnableNgbrResolution.setStatus("current")


class _VRtrIfDHCP6RemoteIdOption_Type(TruthValue):
    """Custom type vRtrIfDHCP6RemoteIdOption based on TruthValue"""


_VRtrIfDHCP6RemoteIdOption_Object = MibTableColumn
vRtrIfDHCP6RemoteIdOption = _VRtrIfDHCP6RemoteIdOption_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 18),
    _VRtrIfDHCP6RemoteIdOption_Type()
)
vRtrIfDHCP6RemoteIdOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6RemoteIdOption.setStatus("current")


class _VRtrIfDHCP6PfxdAdminState_Type(Integer32):
    """Custom type vRtrIfDHCP6PfxdAdminState based on Integer32"""
    defaultValue = 2

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


_VRtrIfDHCP6PfxdAdminState_Type.__name__ = "Integer32"
_VRtrIfDHCP6PfxdAdminState_Object = MibTableColumn
vRtrIfDHCP6PfxdAdminState = _VRtrIfDHCP6PfxdAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 19),
    _VRtrIfDHCP6PfxdAdminState_Type()
)
vRtrIfDHCP6PfxdAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdAdminState.setStatus("current")


class _VRtrIfDHCP6ServerMaxLeaseStates_Type(Unsigned32):
    """Custom type vRtrIfDHCP6ServerMaxLeaseStates based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VRtrIfDHCP6ServerMaxLeaseStates_Type.__name__ = "Unsigned32"
_VRtrIfDHCP6ServerMaxLeaseStates_Object = MibTableColumn
vRtrIfDHCP6ServerMaxLeaseStates = _VRtrIfDHCP6ServerMaxLeaseStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 20),
    _VRtrIfDHCP6ServerMaxLeaseStates_Type()
)
vRtrIfDHCP6ServerMaxLeaseStates.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6ServerMaxLeaseStates.setStatus("current")


class _VRtrIfDHCP6CurrServerLeaseStates_Type(Unsigned32):
    """Custom type vRtrIfDHCP6CurrServerLeaseStates based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8000),
    )


_VRtrIfDHCP6CurrServerLeaseStates_Type.__name__ = "Unsigned32"
_VRtrIfDHCP6CurrServerLeaseStates_Object = MibTableColumn
vRtrIfDHCP6CurrServerLeaseStates = _VRtrIfDHCP6CurrServerLeaseStates_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 21),
    _VRtrIfDHCP6CurrServerLeaseStates_Type()
)
vRtrIfDHCP6CurrServerLeaseStates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCP6CurrServerLeaseStates.setStatus("current")


class _VRtrIfDHCP6ItfIdString_Type(DisplayString):
    """Custom type vRtrIfDHCP6ItfIdString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_VRtrIfDHCP6ItfIdString_Type.__name__ = "DisplayString"
_VRtrIfDHCP6ItfIdString_Object = MibTableColumn
vRtrIfDHCP6ItfIdString = _VRtrIfDHCP6ItfIdString_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 36, 1, 22),
    _VRtrIfDHCP6ItfIdString_Type()
)
vRtrIfDHCP6ItfIdString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6ItfIdString.setStatus("current")
_VRtrIfGlobalIndexTable_Object = MibTable
vRtrIfGlobalIndexTable = _VRtrIfGlobalIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 37)
)
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexTable.setStatus("current")
_VRtrIfGlobalIndexEntry_Object = MibTableRow
vRtrIfGlobalIndexEntry = _VRtrIfGlobalIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 37, 1)
)
vRtrIfGlobalIndexEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfGlobalIndex"),
)
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexEntry.setStatus("current")
_VRtrIfGlobalIndexvRtrID_Type = TmnxVRtrID
_VRtrIfGlobalIndexvRtrID_Object = MibTableColumn
vRtrIfGlobalIndexvRtrID = _VRtrIfGlobalIndexvRtrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 37, 1, 1),
    _VRtrIfGlobalIndexvRtrID_Type()
)
vRtrIfGlobalIndexvRtrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexvRtrID.setStatus("current")
_VRtrIfGlobalIndexvRtrIfIndex_Type = InterfaceIndex
_VRtrIfGlobalIndexvRtrIfIndex_Object = MibTableColumn
vRtrIfGlobalIndexvRtrIfIndex = _VRtrIfGlobalIndexvRtrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 37, 1, 2),
    _VRtrIfGlobalIndexvRtrIfIndex_Type()
)
vRtrIfGlobalIndexvRtrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfGlobalIndexvRtrIfIndex.setStatus("current")
_VRtrIfProxyNDTable_Object = MibTable
vRtrIfProxyNDTable = _VRtrIfProxyNDTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38)
)
if mibBuilder.loadTexts:
    vRtrIfProxyNDTable.setStatus("current")
_VRtrIfProxyNDEntry_Object = MibTableRow
vRtrIfProxyNDEntry = _VRtrIfProxyNDEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38, 1)
)
if mibBuilder.loadTexts:
    vRtrIfProxyNDEntry.setStatus("current")


class _VRtrIfProxyNDLocal_Type(TruthValue):
    """Custom type vRtrIfProxyNDLocal based on TruthValue"""


_VRtrIfProxyNDLocal_Object = MibTableColumn
vRtrIfProxyNDLocal = _VRtrIfProxyNDLocal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38, 1, 1),
    _VRtrIfProxyNDLocal_Type()
)
vRtrIfProxyNDLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyNDLocal.setStatus("current")


class _VRtrIfProxyNDPolicy1_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyNDPolicy1 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyNDPolicy1_Object = MibTableColumn
vRtrIfProxyNDPolicy1 = _VRtrIfProxyNDPolicy1_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38, 1, 2),
    _VRtrIfProxyNDPolicy1_Type()
)
vRtrIfProxyNDPolicy1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyNDPolicy1.setStatus("current")


class _VRtrIfProxyNDPolicy2_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyNDPolicy2 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyNDPolicy2_Object = MibTableColumn
vRtrIfProxyNDPolicy2 = _VRtrIfProxyNDPolicy2_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38, 1, 3),
    _VRtrIfProxyNDPolicy2_Type()
)
vRtrIfProxyNDPolicy2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyNDPolicy2.setStatus("current")


class _VRtrIfProxyNDPolicy3_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyNDPolicy3 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyNDPolicy3_Object = MibTableColumn
vRtrIfProxyNDPolicy3 = _VRtrIfProxyNDPolicy3_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38, 1, 4),
    _VRtrIfProxyNDPolicy3_Type()
)
vRtrIfProxyNDPolicy3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyNDPolicy3.setStatus("current")


class _VRtrIfProxyNDPolicy4_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyNDPolicy4 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyNDPolicy4_Object = MibTableColumn
vRtrIfProxyNDPolicy4 = _VRtrIfProxyNDPolicy4_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38, 1, 5),
    _VRtrIfProxyNDPolicy4_Type()
)
vRtrIfProxyNDPolicy4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyNDPolicy4.setStatus("current")


class _VRtrIfProxyNDPolicy5_Type(TPolicyStatementNameOrEmpty):
    """Custom type vRtrIfProxyNDPolicy5 based on TPolicyStatementNameOrEmpty"""
    defaultHexValue = ""


_VRtrIfProxyNDPolicy5_Object = MibTableColumn
vRtrIfProxyNDPolicy5 = _VRtrIfProxyNDPolicy5_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 38, 1, 6),
    _VRtrIfProxyNDPolicy5_Type()
)
vRtrIfProxyNDPolicy5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfProxyNDPolicy5.setStatus("current")
_VRtrIfDHCP6PfxDelegationLstChgd_Type = TimeStamp
_VRtrIfDHCP6PfxDelegationLstChgd_Object = MibScalar
vRtrIfDHCP6PfxDelegationLstChgd = _VRtrIfDHCP6PfxDelegationLstChgd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 39),
    _VRtrIfDHCP6PfxDelegationLstChgd_Type()
)
vRtrIfDHCP6PfxDelegationLstChgd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxDelegationLstChgd.setStatus("current")
_VRtrIfDHCP6PfxDelegationTable_Object = MibTable
vRtrIfDHCP6PfxDelegationTable = _VRtrIfDHCP6PfxDelegationTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40)
)
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxDelegationTable.setStatus("current")
_VRtrIfDHCP6PfxDelegationEntry_Object = MibTableRow
vRtrIfDHCP6PfxDelegationEntry = _VRtrIfDHCP6PfxDelegationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1)
)
vRtrIfDHCP6PfxDelegationEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdPrefix"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdPrefixLen"),
)
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxDelegationEntry.setStatus("current")
_VRtrIfDHCP6PfxdPrefix_Type = InetAddressIPv6
_VRtrIfDHCP6PfxdPrefix_Object = MibTableColumn
vRtrIfDHCP6PfxdPrefix = _VRtrIfDHCP6PfxdPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 1),
    _VRtrIfDHCP6PfxdPrefix_Type()
)
vRtrIfDHCP6PfxdPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdPrefix.setStatus("current")
_VRtrIfDHCP6PfxdPrefixLen_Type = InetAddressPrefixLength
_VRtrIfDHCP6PfxdPrefixLen_Object = MibTableColumn
vRtrIfDHCP6PfxdPrefixLen = _VRtrIfDHCP6PfxdPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 2),
    _VRtrIfDHCP6PfxdPrefixLen_Type()
)
vRtrIfDHCP6PfxdPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdPrefixLen.setStatus("current")
_VRtrIfDHCP6PfxdRowStatus_Type = RowStatus
_VRtrIfDHCP6PfxdRowStatus_Object = MibTableColumn
vRtrIfDHCP6PfxdRowStatus = _VRtrIfDHCP6PfxdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 3),
    _VRtrIfDHCP6PfxdRowStatus_Type()
)
vRtrIfDHCP6PfxdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdRowStatus.setStatus("current")
_VRtrIfDHCP6PfxdLastChanged_Type = TimeStamp
_VRtrIfDHCP6PfxdLastChanged_Object = MibTableColumn
vRtrIfDHCP6PfxdLastChanged = _VRtrIfDHCP6PfxdLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 4),
    _VRtrIfDHCP6PfxdLastChanged_Type()
)
vRtrIfDHCP6PfxdLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdLastChanged.setStatus("current")


class _VRtrIfDHCP6PfxdDUID_Type(OctetString):
    """Custom type vRtrIfDHCP6PfxdDUID based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VRtrIfDHCP6PfxdDUID_Type.__name__ = "OctetString"
_VRtrIfDHCP6PfxdDUID_Object = MibTableColumn
vRtrIfDHCP6PfxdDUID = _VRtrIfDHCP6PfxdDUID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 6),
    _VRtrIfDHCP6PfxdDUID_Type()
)
vRtrIfDHCP6PfxdDUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdDUID.setStatus("current")


class _VRtrIfDHCP6PfxdIAID_Type(Unsigned32):
    """Custom type vRtrIfDHCP6PfxdIAID based on Unsigned32"""
    defaultValue = 0


_VRtrIfDHCP6PfxdIAID_Object = MibTableColumn
vRtrIfDHCP6PfxdIAID = _VRtrIfDHCP6PfxdIAID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 7),
    _VRtrIfDHCP6PfxdIAID_Type()
)
vRtrIfDHCP6PfxdIAID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdIAID.setStatus("current")


class _VRtrIfDHCP6PfxdPrefLifetime_Type(Unsigned32):
    """Custom type vRtrIfDHCP6PfxdPrefLifetime based on Unsigned32"""
    defaultValue = 604800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrIfDHCP6PfxdPrefLifetime_Type.__name__ = "Unsigned32"
_VRtrIfDHCP6PfxdPrefLifetime_Object = MibTableColumn
vRtrIfDHCP6PfxdPrefLifetime = _VRtrIfDHCP6PfxdPrefLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 8),
    _VRtrIfDHCP6PfxdPrefLifetime_Type()
)
vRtrIfDHCP6PfxdPrefLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdPrefLifetime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdPrefLifetime.setUnits("seconds")


class _VRtrIfDHCP6PfxdValidLifetime_Type(Unsigned32):
    """Custom type vRtrIfDHCP6PfxdValidLifetime based on Unsigned32"""
    defaultValue = 2592000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VRtrIfDHCP6PfxdValidLifetime_Type.__name__ = "Unsigned32"
_VRtrIfDHCP6PfxdValidLifetime_Object = MibTableColumn
vRtrIfDHCP6PfxdValidLifetime = _VRtrIfDHCP6PfxdValidLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 40, 1, 9),
    _VRtrIfDHCP6PfxdValidLifetime_Type()
)
vRtrIfDHCP6PfxdValidLifetime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdValidLifetime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIfDHCP6PfxdValidLifetime.setUnits("seconds")
_VRtrDHCP6DropStatTable_Object = MibTable
vRtrDHCP6DropStatTable = _VRtrDHCP6DropStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 41)
)
if mibBuilder.loadTexts:
    vRtrDHCP6DropStatTable.setStatus("current")
_VRtrDHCP6DropStatEntry_Object = MibTableRow
vRtrDHCP6DropStatEntry = _VRtrDHCP6DropStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 41, 1)
)
vRtrDHCP6DropStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6DropStatReason"),
)
if mibBuilder.loadTexts:
    vRtrDHCP6DropStatEntry.setStatus("current")


class _VRtrDHCP6DropStatReason_Type(Integer32):
    """Custom type vRtrDHCP6DropStatReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25)
        )
    )
    namedValues = NamedValues(
        *(("badRelayedMsg", 5),
          ("clientItfNotFound", 6),
          ("clientMacNotResolved", 23),
          ("dstOperDown", 2),
          ("hopCount", 4),
          ("illegalAssignedAddr", 24),
          ("illegalSrcIp", 20),
          ("illegalUnicast", 19),
          ("msgEncodingError", 25),
          ("msgNotForServer", 14),
          ("msgTooSmall", 13),
          ("nbrAddrsExceeded", 22),
          ("noClientId", 16),
          ("noGlobalPfx", 8),
          ("noMemory", 7),
          ("noRteToServer", 10),
          ("noServerId", 15),
          ("noSrcIp", 9),
          ("none", 0),
          ("pdMsgNotSupported", 21),
          ("relayForw", 12),
          ("rlyReplyOnClientItf", 3),
          ("serverIdInClientMsg", 17),
          ("srcOperDown", 1),
          ("subMgmtUpdFail", 11),
          ("wrongServerId", 18))
    )


_VRtrDHCP6DropStatReason_Type.__name__ = "Integer32"
_VRtrDHCP6DropStatReason_Object = MibTableColumn
vRtrDHCP6DropStatReason = _VRtrDHCP6DropStatReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 41, 1, 1),
    _VRtrDHCP6DropStatReason_Type()
)
vRtrDHCP6DropStatReason.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrDHCP6DropStatReason.setStatus("current")
_VRtrDHCP6DropStatLastCleared_Type = TimeStamp
_VRtrDHCP6DropStatLastCleared_Object = MibTableColumn
vRtrDHCP6DropStatLastCleared = _VRtrDHCP6DropStatLastCleared_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 41, 1, 2),
    _VRtrDHCP6DropStatLastCleared_Type()
)
vRtrDHCP6DropStatLastCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDHCP6DropStatLastCleared.setStatus("current")
_VRtrDHCP6DropStatPktsDropped_Type = Gauge32
_VRtrDHCP6DropStatPktsDropped_Object = MibTableColumn
vRtrDHCP6DropStatPktsDropped = _VRtrDHCP6DropStatPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 41, 1, 3),
    _VRtrDHCP6DropStatPktsDropped_Type()
)
vRtrDHCP6DropStatPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDHCP6DropStatPktsDropped.setStatus("current")
_VRtrDHCP6MsgStatTable_Object = MibTable
vRtrDHCP6MsgStatTable = _VRtrDHCP6MsgStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 42)
)
if mibBuilder.loadTexts:
    vRtrDHCP6MsgStatTable.setStatus("current")
_VRtrDHCP6MsgStatEntry_Object = MibTableRow
vRtrDHCP6MsgStatEntry = _VRtrDHCP6MsgStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 42, 1)
)
vRtrDHCP6MsgStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsMsgType"),
)
if mibBuilder.loadTexts:
    vRtrDHCP6MsgStatEntry.setStatus("current")
_VRtrDHCP6MsgStatsMsgType_Type = TmnxDHCP6MsgType
_VRtrDHCP6MsgStatsMsgType_Object = MibTableColumn
vRtrDHCP6MsgStatsMsgType = _VRtrDHCP6MsgStatsMsgType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 42, 1, 1),
    _VRtrDHCP6MsgStatsMsgType_Type()
)
vRtrDHCP6MsgStatsMsgType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrDHCP6MsgStatsMsgType.setStatus("current")
_VRtrDHCP6MsgStatsLstClrd_Type = TimeStamp
_VRtrDHCP6MsgStatsLstClrd_Object = MibTableColumn
vRtrDHCP6MsgStatsLstClrd = _VRtrDHCP6MsgStatsLstClrd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 42, 1, 2),
    _VRtrDHCP6MsgStatsLstClrd_Type()
)
vRtrDHCP6MsgStatsLstClrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDHCP6MsgStatsLstClrd.setStatus("current")
_VRtrDHCP6MsgStatsRcvd_Type = Gauge32
_VRtrDHCP6MsgStatsRcvd_Object = MibTableColumn
vRtrDHCP6MsgStatsRcvd = _VRtrDHCP6MsgStatsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 42, 1, 3),
    _VRtrDHCP6MsgStatsRcvd_Type()
)
vRtrDHCP6MsgStatsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDHCP6MsgStatsRcvd.setStatus("current")
_VRtrDHCP6MsgStatsSent_Type = Gauge32
_VRtrDHCP6MsgStatsSent_Object = MibTableColumn
vRtrDHCP6MsgStatsSent = _VRtrDHCP6MsgStatsSent_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 42, 1, 4),
    _VRtrDHCP6MsgStatsSent_Type()
)
vRtrDHCP6MsgStatsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDHCP6MsgStatsSent.setStatus("current")
_VRtrDHCP6MsgStatsDropped_Type = Gauge32
_VRtrDHCP6MsgStatsDropped_Object = MibTableColumn
vRtrDHCP6MsgStatsDropped = _VRtrDHCP6MsgStatsDropped_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 42, 1, 5),
    _VRtrDHCP6MsgStatsDropped_Type()
)
vRtrDHCP6MsgStatsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrDHCP6MsgStatsDropped.setStatus("current")
_VRtrIfIpcpTable_Object = MibTable
vRtrIfIpcpTable = _VRtrIfIpcpTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43)
)
if mibBuilder.loadTexts:
    vRtrIfIpcpTable.setStatus("current")
_VRtrIfIpcpEntry_Object = MibTableRow
vRtrIfIpcpEntry = _VRtrIfIpcpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43, 1)
)
if mibBuilder.loadTexts:
    vRtrIfIpcpEntry.setStatus("current")


class _VRtrIfIpcpPeerAddrType_Type(InetAddressType):
    """Custom type vRtrIfIpcpPeerAddrType based on InetAddressType"""


_VRtrIfIpcpPeerAddrType_Object = MibTableColumn
vRtrIfIpcpPeerAddrType = _VRtrIfIpcpPeerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43, 1, 1),
    _VRtrIfIpcpPeerAddrType_Type()
)
vRtrIfIpcpPeerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpcpPeerAddrType.setStatus("current")


class _VRtrIfIpcpPeerAddr_Type(InetAddress):
    """Custom type vRtrIfIpcpPeerAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrIfIpcpPeerAddr_Type.__name__ = "InetAddress"
_VRtrIfIpcpPeerAddr_Object = MibTableColumn
vRtrIfIpcpPeerAddr = _VRtrIfIpcpPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43, 1, 2),
    _VRtrIfIpcpPeerAddr_Type()
)
vRtrIfIpcpPeerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpcpPeerAddr.setStatus("current")


class _VRtrIfIpcpPriDnsAddrType_Type(InetAddressType):
    """Custom type vRtrIfIpcpPriDnsAddrType based on InetAddressType"""


_VRtrIfIpcpPriDnsAddrType_Object = MibTableColumn
vRtrIfIpcpPriDnsAddrType = _VRtrIfIpcpPriDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43, 1, 3),
    _VRtrIfIpcpPriDnsAddrType_Type()
)
vRtrIfIpcpPriDnsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpcpPriDnsAddrType.setStatus("current")


class _VRtrIfIpcpPriDnsAddr_Type(InetAddress):
    """Custom type vRtrIfIpcpPriDnsAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrIfIpcpPriDnsAddr_Type.__name__ = "InetAddress"
_VRtrIfIpcpPriDnsAddr_Object = MibTableColumn
vRtrIfIpcpPriDnsAddr = _VRtrIfIpcpPriDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43, 1, 4),
    _VRtrIfIpcpPriDnsAddr_Type()
)
vRtrIfIpcpPriDnsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpcpPriDnsAddr.setStatus("current")


class _VRtrIfIpcpSecDnsAddrType_Type(InetAddressType):
    """Custom type vRtrIfIpcpSecDnsAddrType based on InetAddressType"""


_VRtrIfIpcpSecDnsAddrType_Object = MibTableColumn
vRtrIfIpcpSecDnsAddrType = _VRtrIfIpcpSecDnsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43, 1, 5),
    _VRtrIfIpcpSecDnsAddrType_Type()
)
vRtrIfIpcpSecDnsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpcpSecDnsAddrType.setStatus("current")


class _VRtrIfIpcpSecDnsAddr_Type(InetAddress):
    """Custom type vRtrIfIpcpSecDnsAddr based on InetAddress"""
    defaultHexValue = ""

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrIfIpcpSecDnsAddr_Type.__name__ = "InetAddress"
_VRtrIfIpcpSecDnsAddr_Object = MibTableColumn
vRtrIfIpcpSecDnsAddr = _VRtrIfIpcpSecDnsAddr_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 43, 1, 6),
    _VRtrIfIpcpSecDnsAddr_Type()
)
vRtrIfIpcpSecDnsAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIfIpcpSecDnsAddr.setStatus("current")
_VRtrInetStatRteCpeChkStatsTable_Object = MibTable
vRtrInetStatRteCpeChkStatsTable = _VRtrInetStatRteCpeChkStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44)
)
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkStatsTable.setStatus("current")
_VRtrInetStatRteCpeChkStatsEntry_Object = MibTableRow
vRtrInetStatRteCpeChkStatsEntry = _VRtrInetStatRteCpeChkStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44, 1)
)
vRtrInetStatRteCpeChkStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDestType"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDest"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDestPfxLen"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteIndex"),
)
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkStatsEntry.setStatus("current")
_VRtrInetStatRteCpeChkUpTime_Type = TimeTicks
_VRtrInetStatRteCpeChkUpTime_Object = MibTableColumn
vRtrInetStatRteCpeChkUpTime = _VRtrInetStatRteCpeChkUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44, 1, 1),
    _VRtrInetStatRteCpeChkUpTime_Type()
)
vRtrInetStatRteCpeChkUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkUpTime.setStatus("current")
_VRtrInetStatRteCpeChkInPktCnt_Type = Counter32
_VRtrInetStatRteCpeChkInPktCnt_Object = MibTableColumn
vRtrInetStatRteCpeChkInPktCnt = _VRtrInetStatRteCpeChkInPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44, 1, 2),
    _VRtrInetStatRteCpeChkInPktCnt_Type()
)
vRtrInetStatRteCpeChkInPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkInPktCnt.setStatus("current")
_VRtrInetStatRteCpeChkOutPktCnt_Type = Counter32
_VRtrInetStatRteCpeChkOutPktCnt_Object = MibTableColumn
vRtrInetStatRteCpeChkOutPktCnt = _VRtrInetStatRteCpeChkOutPktCnt_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44, 1, 3),
    _VRtrInetStatRteCpeChkOutPktCnt_Type()
)
vRtrInetStatRteCpeChkOutPktCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkOutPktCnt.setStatus("current")
_VRtrInetStatRteCpeChkDownTrans_Type = Gauge32
_VRtrInetStatRteCpeChkDownTrans_Object = MibTableColumn
vRtrInetStatRteCpeChkDownTrans = _VRtrInetStatRteCpeChkDownTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44, 1, 4),
    _VRtrInetStatRteCpeChkDownTrans_Type()
)
vRtrInetStatRteCpeChkDownTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkDownTrans.setStatus("current")
_VRtrInetStatRteCpeChkUpTrans_Type = Gauge32
_VRtrInetStatRteCpeChkUpTrans_Object = MibTableColumn
vRtrInetStatRteCpeChkUpTrans = _VRtrInetStatRteCpeChkUpTrans_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44, 1, 5),
    _VRtrInetStatRteCpeChkUpTrans_Type()
)
vRtrInetStatRteCpeChkUpTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkUpTrans.setStatus("current")
_VRtrInetStatRteCpeChkTTL_Type = Unsigned32
_VRtrInetStatRteCpeChkTTL_Object = MibTableColumn
vRtrInetStatRteCpeChkTTL = _VRtrInetStatRteCpeChkTTL_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 44, 1, 6),
    _VRtrInetStatRteCpeChkTTL_Type()
)
vRtrInetStatRteCpeChkTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkTTL.setStatus("current")
if mibBuilder.loadTexts:
    vRtrInetStatRteCpeChkTTL.setUnits("seconds")
_TmnxDscpAppTableLastChanged_Type = TimeStamp
_TmnxDscpAppTableLastChanged_Object = MibScalar
tmnxDscpAppTableLastChanged = _TmnxDscpAppTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 45),
    _TmnxDscpAppTableLastChanged_Type()
)
tmnxDscpAppTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDscpAppTableLastChanged.setStatus("current")
_TmnxDscpAppTable_Object = MibTable
tmnxDscpAppTable = _TmnxDscpAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 46)
)
if mibBuilder.loadTexts:
    tmnxDscpAppTable.setStatus("current")
_TmnxDscpAppEntry_Object = MibTableRow
tmnxDscpAppEntry = _TmnxDscpAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 46, 1)
)
tmnxDscpAppEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpAppId"),
)
if mibBuilder.loadTexts:
    tmnxDscpAppEntry.setStatus("current")
_TmnxDscpAppId_Type = TDSCPAppId
_TmnxDscpAppId_Object = MibTableColumn
tmnxDscpAppId = _TmnxDscpAppId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 46, 1, 1),
    _TmnxDscpAppId_Type()
)
tmnxDscpAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDscpAppId.setStatus("current")
_TmnxDscpAppLastChanged_Type = TimeStamp
_TmnxDscpAppLastChanged_Object = MibTableColumn
tmnxDscpAppLastChanged = _TmnxDscpAppLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 46, 1, 2),
    _TmnxDscpAppLastChanged_Type()
)
tmnxDscpAppLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDscpAppLastChanged.setStatus("current")
_TmnxDscpAppDscpValue_Type = TDSCPValueOrNone
_TmnxDscpAppDscpValue_Object = MibTableColumn
tmnxDscpAppDscpValue = _TmnxDscpAppDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 46, 1, 3),
    _TmnxDscpAppDscpValue_Type()
)
tmnxDscpAppDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDscpAppDscpValue.setStatus("current")
_TmnxDscpFCTableLastChanged_Type = TimeStamp
_TmnxDscpFCTableLastChanged_Object = MibScalar
tmnxDscpFCTableLastChanged = _TmnxDscpFCTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 47),
    _TmnxDscpFCTableLastChanged_Type()
)
tmnxDscpFCTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDscpFCTableLastChanged.setStatus("current")
_TmnxDscpFCTable_Object = MibTable
tmnxDscpFCTable = _TmnxDscpFCTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 48)
)
if mibBuilder.loadTexts:
    tmnxDscpFCTable.setStatus("current")
_TmnxDscpFCEntry_Object = MibTableRow
tmnxDscpFCEntry = _TmnxDscpFCEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 48, 1)
)
tmnxDscpFCEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpFCDscpValue"),
)
if mibBuilder.loadTexts:
    tmnxDscpFCEntry.setStatus("current")
_TmnxDscpFCDscpValue_Type = TDSCPValue
_TmnxDscpFCDscpValue_Object = MibTableColumn
tmnxDscpFCDscpValue = _TmnxDscpFCDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 48, 1, 1),
    _TmnxDscpFCDscpValue_Type()
)
tmnxDscpFCDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDscpFCDscpValue.setStatus("current")
_TmnxDscpFCLastChanged_Type = TimeStamp
_TmnxDscpFCLastChanged_Object = MibTableColumn
tmnxDscpFCLastChanged = _TmnxDscpFCLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 48, 1, 3),
    _TmnxDscpFCLastChanged_Type()
)
tmnxDscpFCLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDscpFCLastChanged.setStatus("current")


class _TmnxDscpFCValue_Type(TFCType):
    """Custom type tmnxDscpFCValue based on TFCType"""


_TmnxDscpFCValue_Object = MibTableColumn
tmnxDscpFCValue = _TmnxDscpFCValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 48, 1, 4),
    _TmnxDscpFCValue_Type()
)
tmnxDscpFCValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDscpFCValue.setStatus("current")
_TmnxDot1pAppTableLastChanged_Type = TimeStamp
_TmnxDot1pAppTableLastChanged_Object = MibScalar
tmnxDot1pAppTableLastChanged = _TmnxDot1pAppTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 49),
    _TmnxDot1pAppTableLastChanged_Type()
)
tmnxDot1pAppTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1pAppTableLastChanged.setStatus("current")
_TmnxDot1pAppTable_Object = MibTable
tmnxDot1pAppTable = _TmnxDot1pAppTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 50)
)
if mibBuilder.loadTexts:
    tmnxDot1pAppTable.setStatus("current")
_TmnxDot1pAppEntry_Object = MibTableRow
tmnxDot1pAppEntry = _TmnxDot1pAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 50, 1)
)
tmnxDot1pAppEntry.setIndexNames(
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDot1pAppId"),
)
if mibBuilder.loadTexts:
    tmnxDot1pAppEntry.setStatus("current")
_TmnxDot1pAppId_Type = TDot1pAppId
_TmnxDot1pAppId_Object = MibTableColumn
tmnxDot1pAppId = _TmnxDot1pAppId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 50, 1, 1),
    _TmnxDot1pAppId_Type()
)
tmnxDot1pAppId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmnxDot1pAppId.setStatus("current")
_TmnxDot1pAppLastChanged_Type = TimeStamp
_TmnxDot1pAppLastChanged_Object = MibTableColumn
tmnxDot1pAppLastChanged = _TmnxDot1pAppLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 50, 1, 2),
    _TmnxDot1pAppLastChanged_Type()
)
tmnxDot1pAppLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmnxDot1pAppLastChanged.setStatus("current")
_TmnxDot1pAppValue_Type = Dot1PPriority
_TmnxDot1pAppValue_Object = MibTableColumn
tmnxDot1pAppValue = _TmnxDot1pAppValue_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 3, 50, 1, 3),
    _TmnxDot1pAppValue_Type()
)
tmnxDot1pAppValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmnxDot1pAppValue.setStatus("current")
_TmnxVRtrNotifyPrefix_ObjectIdentity = ObjectIdentity
tmnxVRtrNotifyPrefix = _TmnxVRtrNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3)
)
_TmnxVRtrNotifications_ObjectIdentity = ObjectIdentity
tmnxVRtrNotifications = _TmnxVRtrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0)
)
vRtrConfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrStatEntry")
)
vRtrStatEntry.setIndexNames(*vRtrConfEntry.getIndexNames())
ipCidrRouteEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIpCidrRouteEntry")
)
vRtrIpCidrRouteEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())
ipNetToMediaEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIpNetToMediaEntry")
)
vRtrIpNetToMediaEntry.setIndexNames(*ipNetToMediaEntry.getIndexNames())
vRtrConfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrPolicyEntry")
)
vRtrPolicyEntry.setIndexNames(*vRtrConfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfProxyArpEntry")
)
vRtrIfProxyArpEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfDHCPEntry")
)
vRtrIfDHCPEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfDHCPRelayStatsEntry")
)
vRtrIfDHCPRelayStatsEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrConfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIcmp6Entry")
)
vRtrIcmp6Entry.setIndexNames(*vRtrConfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfIcmp6Entry")
)
vRtrIfIcmp6Entry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfBfdEntry")
)
vRtrIfBfdEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfDHCP6Entry")
)
vRtrIfDHCP6Entry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfProxyNDEntry")
)
vRtrIfProxyNDEntry.setIndexNames(*vRtrIfEntry.getIndexNames())
vRtrIfEntry.registerAugmentions(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB",
     "vRtrIfIpcpEntry")
)
vRtrIfIpcpEntry.setIndexNames(*vRtrIfEntry.getIndexNames())

# Managed Objects groups

tmnxVRtrGlobalR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 10)
)
tmnxVRtrGlobalR2r1Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNextVRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrConfiguredVRtrs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrActiveVRtrs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouteThresholdSoakTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxARPEntries"))
)
if mibBuilder.loadTexts:
    tmnxVRtrGlobalR2r1Group.setStatus("obsolete")

tmnxVRtrIfSubscrAuthV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 11)
)
tmnxVRtrIfSubscrAuthV3v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPAuthPolicy"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayAuthPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayAuthPktsSuccess"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIfSubscrAuthV3v0Group.setStatus("current")

tmnxVRtrV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 14)
)
tmnxVRtrV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrName"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBgpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMplsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOspfStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRipStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRsvpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrEcmpMaxRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNewIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrLdpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIsIsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTriggeredPolicy"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrConfederationAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouteDistinguisher"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMidRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrHighRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIllegalLabelThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVpnId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrGracefulRestart"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrGracefulRestartType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrCustId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIgmpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxNumRoutesLogOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfExportTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfImportTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrPimStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutesLogOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMcastMidRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIgnoreIcmpRedirect"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOspfv3Status"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDirectRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDirectActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOSPFRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOSPFActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBGPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBGPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrISISRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrISISActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRIPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRIPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregateRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregateActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatConfiguredIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatIllegalLabels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatBGPVpnRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatBGPVpnActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMulticastRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSubMgmtRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSubMgmtActiveRoutes"))
)
if mibBuilder.loadTexts:
    tmnxVRtrV4v0Group.setStatus("obsolete")

tmnxVRtrIfV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 15)
)
tmnxVRtrIfV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfTotalNumber"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfName"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfPortID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfChannelID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfEncapValue"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfAlias"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfPhysicalAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfArpTimeout"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpMaskReply"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpNumRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpRedirectsTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpUnreachables"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpNumUnreachables"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpUnreachablesTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpTtlExpired"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpNumTtlExpired"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpTtlExpiredTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfNtpBroadcast"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfUnnumbered"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfMtu"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIngressFilterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfEgressFilterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDirectedBroadcast"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfMplsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfUnnumberedIf"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfCflowd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfVPNClass"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProtocol"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfTosMarkingTrusted"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfArpPopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpLocal"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfNameIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayInfoAction"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayCircuitId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRemoteId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer6"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer7"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer8"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayTrusted"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayTxPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxMalformedPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxUntrustedPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsRelayed"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsRelayed"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsSnooped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsSnooped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPOperLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddressType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddressAsSrc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPMatchOption82"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIfV4v0Group.setStatus("obsolete")

tmnxVRtrIpV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 16)
)
tmnxVRtrIpV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaIpAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaNetMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaBcastAddrFormat"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaReasmMaxSize"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaIgpInhibit"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetAddressType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetAddrState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetEui64"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetOperAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpCidrRouteLastEnabledTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpCidrRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpCidrRouteMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteDest"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteNumber"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteLastEnabledTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteStaticType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteEgressIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteNextHop"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteNextHopUnnumberedIf"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIgpShortcut"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteDisallowIgp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteTag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndexDest"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndexMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteAvailableIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteLastEnabledTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteStaticType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteEgressIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteNextHopType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteNextHop"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteNextHopIf"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteIgpShortcut"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDisallowIgp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteTag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteEnableBfd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteAvailIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeExclusive"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpNetToMediaTimer"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpNetToMediaOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInstanceAggregationTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationSummaryOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationASSet"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationAggregatorAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationAggregatorIPAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelAge"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixOnLinkFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixAutonomousFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixPreferredLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixValidLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetInstAggrTblLastChged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrSummaryOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrASSet"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrAggregatorAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrAggregatorIPAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetSvcIpRangeRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetSvcIpRangeExclusive"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIpV4v0Group.setStatus("obsolete")

tmnxVRtrObsoletedObjectsV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 17)
)
tmnxVRtrObsoletedObjectsV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLseStateChAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLseStateRemainLseTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLseStateOption82"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLseStatePersistKey"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCPClientLease"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateOldCiAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateOldChAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateCiAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateVRtrId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateProblem"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStatePopulateError"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayInfoOption"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPAutoFilter"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPSnooping"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPAutoFilterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPOperAutoFilter"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAutoFilterDHCPClientAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAutoFilterDHCPClientLease"))
)
if mibBuilder.loadTexts:
    tmnxVRtrObsoletedObjectsV4v0Group.setStatus("current")

tmnxVRtrBfdV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 18)
)
tmnxVRtrBfdV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdTransmitInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdReceiveInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdMultiplier"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionOperFlags"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionMesgRecv"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionMesgSent"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLastDownTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLastUpTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionUpCount"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionDownCount"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclDisc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionRemDisc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionProtocols"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionTxInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionRxInterval"))
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdV4v0Group.setStatus("obsolete")

tmnxVRtrIPv6IfV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 20)
)
tmnxVRtrIPv6IfV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIPv6ConfigAllowed"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIPv6OperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIPv6IngressFilterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIPv6EgressFilterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6Redirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6NumRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6RedirectsTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6Unreachables"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6NumUnreachables"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6UnreachablesTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6TimeExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6NumTimeExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6TimeExceededTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6PktTooBig"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6NumPktTooBig"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6PktTooBigTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6ParamProblem"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6NumParamProblem"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpV6ParamProblemTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfLinkLocalAddressType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfLinkLocalAddressState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfLinkLocalAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InMsgs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InErrors"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InDestUnreachs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InAdminProhibs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InTimeExcds"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InParmProblems"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InPktTooBigs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InEchos"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InEchoReplies"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InRtrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InRtrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InNbrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InNbrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InGrpMembQueries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InGrpMembResponses"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6InGrpMembReductions"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutMsgs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutErrors"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutDestUnreachs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutAdminProhibs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutTimeExcds"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutParmProblems"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutPktTooBigs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutEchos"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutEchoReplies"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutRtrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutRtrSolicitsTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutRtrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutRtrAdvTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutNbrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutNbrSolicitsTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutNbrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutNbrAdvTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutGrpMembQueries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutGrpMembResponses"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmp6OutGrpMembReductions"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InMsgs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InErrors"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InDestUnreachs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InAdminProhibs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InTimeExcds"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InParmProblems"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InPktTooBigs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InEchos"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InEchoReplies"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InRtrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InRtrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InNbrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InNbrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InGrpMembQueries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InGrpMembResponses"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6InGrpMembReductions"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutMsgs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutErrors"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutDestUnreachs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutAdminProhibs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutTimeExcds"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutParmProblems"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutPktTooBigs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutEchos"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutEchoReplies"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutRtrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutRtrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutNbrSolicits"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutNbrAdvertisements"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutGrpMembQueries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutGrpMembResponses"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIcmp6OutGrpMembReductions"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIPv6IfV4v0Group.setStatus("current")

tmnxVRtrIPv6V4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 21)
)
tmnxVRtrIPv6V4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6DirectRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6DirectActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StaticRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StaticActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6OSPFRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6OSPFActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6BGPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6BGPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6ISISRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6ISISActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6RIPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6RIPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6AggregateRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6AggregateActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatConfiguredIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatActiveIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatIllegalLabels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatBGPVpnRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatBGPVpnActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatTotalLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatTotalSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatActiveLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatActiveSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6MulticastRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatActiveNbrEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatTotalNbrEntries"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIPv6V4v0Group.setStatus("current")

tmnxVRtrIPv6IpV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 22)
)
tmnxVRtrIPv6IpV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixOnLinkFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixAutonomousFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixPreferredLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixValidLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixRowStatus"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIPv6IpV4v0Group.setStatus("obsolete")

tmnxVRtrIPv6IpV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 24)
)
tmnxVRtrIPv6IpV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixOnLinkFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixAutonomousFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixPreferredLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixValidLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6TableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6LastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6AdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6OperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6Description"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer6"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer7"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayServer8"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RelayItfIdOption"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6LeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6CurrLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6SourceAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6EnableNgbrResolution"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6RemoteIdOption"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6ServerMaxLeaseStates"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6CurrServerLeaseStates"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6ItfIdString"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyNDLocal"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyNDPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyNDPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyNDPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyNDPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyNDPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdDUID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdIAID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdPrefLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxdValidLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6PfxDelegationLstChgd"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIPv6IpV5v0Group.setStatus("current")

tmnxVRtrIfV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 25)
)
tmnxVRtrIfV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfTotalNumber"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfName"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfPortID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfEncapValue"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfAlias"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfPhysicalAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfArpTimeout"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpMaskReply"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpNumRedirects"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpRedirectsTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpUnreachables"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpNumUnreachables"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpUnreachablesTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpTtlExpired"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpNumTtlExpired"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIcmpTtlExpiredTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfNtpBroadcast"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfUnnumbered"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfMtu"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfQosPolicyId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIngressFilterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfEgressFilterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDirectedBroadcast"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfMplsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfUnnumberedIf"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfCflowd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfVPNClass"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProtocol"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfTosMarkingTrusted"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfArpPopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfLastOperStateChange"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfOperMtu"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfGlobalIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpLocal"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfProxyArpPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfNameIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayInfoAction"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayCircuitId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRemoteId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer6"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer7"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer8"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayTrusted"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayTxPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxMalformedPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxUntrustedPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsRelayed"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsRelayed"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsSnooped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsSnooped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsProxRad"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsProxLS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayPktsGenRelease"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayPktsGenForceRenew"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPOperLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddressType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddressAsSrc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPMatchOption82"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRemoteIdStr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyServerAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyLeaseTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyLTRadiusOverride"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPVendorIncludeOptions"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPVendorOptionString"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfGlobalIndexvRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfGlobalIndexvRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDelaySeconds"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDelayUpTimer"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfInitDelayEnable"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIfV5v0Group.setStatus("current")

tmnxVRtrIpV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 26)
)
tmnxVRtrIpV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaIpAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaNetMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaBcastAddrFormat"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaReasmMaxSize"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaIgpInhibit"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetAddressType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetAddrState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetEui64"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetOperAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetGwAddressType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetGwAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetRemoteIpType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRiaInetRemoteIp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpCidrRouteLastEnabledTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpCidrRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpCidrRouteMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteDest"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteNumber"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteLastEnabledTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteStaticType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteEgressIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteNextHop"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteNextHopUnnumberedIf"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIgpShortcut"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteDisallowIgp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteTag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndexDest"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteIndexMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRouteAvailableIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteLastEnabledTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteStaticType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRoutePreference"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteEgressIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteNextHopType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteNextHop"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteNextHopIf"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteIgpShortcut"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteDisallowIgp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteTag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteEnableBfd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteAvailIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeMask"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSvcIpRangeExclusive"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpNetToMediaTimer"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIpNetToMediaOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInstanceAggregationTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationSummaryOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationASSet"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationAggregatorAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationAggregatorIPAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregationOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelMetric"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTunnelAge"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixOnLinkFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixAutonomousFlag"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixPreferredLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixValidLifetime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdvPrefixRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetInstAggrTblLastChged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrSummaryOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrASSet"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrAggregatorAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrAggregatorIPAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetAggrOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetSvcIpRangeRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetSvcIpRangeExclusive"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIpV5v0Group.setStatus("current")

tmnxVRtrV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 27)
)
tmnxVRtrV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrName"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBgpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMplsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRipStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRsvpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrEcmpMaxRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNewIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrLdpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIsIsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTriggeredPolicy"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrConfederationAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouteDistinguisher"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMidRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrHighRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIllegalLabelThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVpnId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrGracefulRestart"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrGracefulRestartType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrCustId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIgmpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxNumRoutesLogOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfExportTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfImportTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrPimStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutesLogOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMcastMidRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIgnoreIcmpRedirect"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMsdpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVprnType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSecondaryVrfId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMldStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDirectRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDirectActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOSPFRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOSPFActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBGPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBGPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrISISRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrISISActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRIPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRIPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregateRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregateActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatConfiguredIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatIllegalLabels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatBGPVpnRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatBGPVpnActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMulticastRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSubMgmtRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSubMgmtActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatTotalRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatActiveRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6DropStatLastCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6DropStatPktsDropped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsLstClrd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsRcvd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsSent"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsDropped"))
)
if mibBuilder.loadTexts:
    tmnxVRtrV5v0Group.setStatus("obsolete")

tmnxVRtrObsoleteV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 29)
)
tmnxVRtrObsoleteV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOspfStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOspfv3Status"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfChannelID"))
)
if mibBuilder.loadTexts:
    tmnxVRtrObsoleteV5v0Group.setStatus("current")

tmnxVRtrNotificationObjV5v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 30)
)
tmnxVRtrNotificationObjV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpPacketProblem"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBfdSlotNumber"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNumberOfBfdSessionsOnSlot"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBfdMaxSessionReason"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ServerNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ServerNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6NewClientId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldClientId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6LeaseOverrideResult"))
)
if mibBuilder.loadTexts:
    tmnxVRtrNotificationObjV5v0Group.setStatus("obsolete")

tmnxVRtrIfDhcpServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 31)
)
tmnxVRtrIfDhcpServerGroup.setObjects(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfLocalDhcpServerName")
)
if mibBuilder.loadTexts:
    tmnxVRtrIfDhcpServerGroup.setStatus("current")

tmnxVRtrV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 32)
)
tmnxVRtrV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRowStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrName"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBgpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMplsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRipStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRsvpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrEcmpMaxRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNewIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrLdpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIsIsStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouterId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrTriggeredPolicy"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrConfederationAS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouteDistinguisher"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMidRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrHighRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIllegalLabelThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVpnId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrGracefulRestart"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrGracefulRestartType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrCustId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIgmpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxNumRoutesLogOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfExportTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVrfImportTarget"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrPimStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutesLogOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMcastMidRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIgnoreIcmpRedirect"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMsdpStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrVprnType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSecondaryVrfId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMldStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6MaxNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6MidRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6HighRouteThreshold"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6MaxNumRoutesLogOnly"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6IgnoreIcmpRedirect"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMcPathMgmtPlcyName"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrImportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrExportPolicy5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDirectRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDirectActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStaticActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOSPFRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrOSPFActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBGPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBGPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrISISRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrISISActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRIPRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRIPActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregateRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAggregateActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatConfiguredIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveIfs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatIllegalLabels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatBGPVpnRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatBGPVpnActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveLdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveSdpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMulticastRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSubMgmtRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrSubMgmtActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatTotalRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatActiveRsvpTunnels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrHostRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrHostActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6HostRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6HostActiveRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatLocalARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatStaticARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatDynamicARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatManagedARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatInternalARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6DropStatLastCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6DropStatPktsDropped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsLstClrd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsRcvd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsSent"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6MsgStatsDropped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedActiveRoutes"))
)
if mibBuilder.loadTexts:
    tmnxVRtrV6v0Group.setStatus("current")

tmnxVRtrStaticRteCPEChkV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 33)
)
tmnxVRtrStaticRteCPEChkV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteCpeAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteCpeAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteCpeInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteCpeDropCnt"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteCpeEnableLog"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeChkUpTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeChkInPktCnt"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeChkOutPktCnt"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeChkUpTrans"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeChkDownTrans"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeChkTTL"))
)
if mibBuilder.loadTexts:
    tmnxVRtrStaticRteCPEChkV6v0Group.setStatus("current")

tmnxVRtrIfIpcpV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 34)
)
tmnxVRtrIfIpcpV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIpcpPeerAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIpcpPeerAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIpcpPriDnsAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIpcpPriDnsAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIpcpSecDnsAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIpcpSecDnsAddr"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIfIpcpV6v0Group.setStatus("current")

tmnxVRtrIfCpmProtectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 35)
)
tmnxVRtrIfCpmProtectGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfCpmProtPolicyId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfCpmProtUncfgdProtoDropCnt"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIfCpmProtectGroup.setStatus("current")

tmnxDscpAppV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 36)
)
tmnxDscpAppV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpAppLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpAppDscpValue"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpFCLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpFCValue"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpAppTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDscpFCTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDot1pAppTableLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDot1pAppLastChanged"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxDot1pAppValue"))
)
if mibBuilder.loadTexts:
    tmnxDscpAppV6v0Group.setStatus("current")

tmnxVRtrIfDHCPRelayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 37)
)
tmnxVRtrIfDHCPRelayGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayInfoAction"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayCircuitId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRemoteId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer1"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer2"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer3"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer4"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer5"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer6"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer7"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServer8"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayTrusted"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPDescription"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayTxPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxMalformedPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRxUntrustedPkts"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsRelayed"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsDiscarded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsRelayed"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsSnooped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayServerPktsSnooped"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsProxRad"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayClientPktsProxLS"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayPktsGenRelease"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayPktsGenForceRenew"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPOperLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddressType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPGiAddressAsSrc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPMatchOption82"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPRelayRemoteIdStr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyServerAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyLeaseTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPProxyLTRadiusOverride"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPVendorIncludeOptions"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPVendorOptionString"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLayer2Header"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPAntiSpoofMacAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPClientApplications"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfLdpSyncTimer"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIfDHCPRelayGroup.setStatus("current")

tmnxVRtrGlobalV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 38)
)
tmnxVRtrGlobalV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNextVRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrConfiguredVRtrs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrActiveVRtrs"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrRouteThresholdSoakTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6RouteThresholdSoakTime"))
)
if mibBuilder.loadTexts:
    tmnxVRtrGlobalV6v0Group.setStatus("current")

tmnxVRtrNotificationObjV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 39)
)
tmnxVRtrNotificationObjV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpPacketProblem"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBfdSlotNumber"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNumberOfBfdSessionsOnSlot"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBfdMaxSessionReason"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ServerNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ServerNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6NewClientId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldClientId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6LeaseOverrideResult"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeNotifyAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeNotifyAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteCpeStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedRouteInetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedRouteInetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedRoutePrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrFailureDescription"))
)
if mibBuilder.loadTexts:
    tmnxVRtrNotificationObjV6v0Group.setStatus("current")

tmnxVRtrBfdV6v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 41)
)
tmnxVRtrBfdV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdAdminState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdTransmitInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdReceiveInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdMultiplier"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionOperState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionState"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionOperFlags"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionMesgRecv"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionMesgSent"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLastDownTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLastUpTime"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionUpCount"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionDownCount"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclDisc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionRemDisc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionProtocols"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionTxInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionRxInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdEchoInterval"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionType"))
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdV6v0Group.setStatus("current")


# Notification objects

tmnxVRtrMidRouteTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 1)
)
tmnxVRtrMidRouteTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMidRouteThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMidRouteTCA.setStatus(
        "current"
    )

tmnxVRtrHighRouteTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 2)
)
tmnxVRtrHighRouteTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrHighRouteThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrHighRouteTCA.setStatus(
        "current"
    )

tmnxVRtrHighRouteCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 3)
)
tmnxVRtrHighRouteCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrHighRouteThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrHighRouteCleared.setStatus(
        "current"
    )

tmnxVRtrIllegalLabelTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 4)
)
tmnxVRtrIllegalLabelTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatIllegalLabels"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIllegalLabelThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIllegalLabelTCA.setStatus(
        "current"
    )

tmnxVRtrMcastMidRouteTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 5)
)
tmnxVRtrMcastMidRouteTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMulticastRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMcastMidRouteThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMcastMidRouteTCA.setStatus(
        "current"
    )

tmnxVRtrMcastMaxRoutesTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 6)
)
tmnxVRtrMcastMaxRoutesTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMulticastRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutes"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMcastMaxRoutesTCA.setStatus(
        "current"
    )

tmnxVRtrMcastMaxRoutesCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 7)
)
tmnxVRtrMcastMaxRoutesCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMulticastRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxMcastNumRoutes"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMcastMaxRoutesCleared.setStatus(
        "current"
    )

tmnxVRtrMaxArpEntriesTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 8)
)
tmnxVRtrMaxArpEntriesTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxARPEntries"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMaxArpEntriesTCA.setStatus(
        "current"
    )

tmnxVRtrMaxArpEntriesCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 9)
)
tmnxVRtrMaxArpEntriesCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatActiveARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatTotalARPEntries"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxARPEntries"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMaxArpEntriesCleared.setStatus(
        "current"
    )

tmnxVRtrDHCPAFEntriesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 10)
)
tmnxVRtrDHCPAFEntriesExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPOperAutoFilter"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAutoFilterDHCPClientAddress"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrAutoFilterDHCPClientLease"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCPAFEntriesExceeded.setStatus(
        "obsolete"
    )

tmnxVRtrMaxRoutes = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 11)
)
tmnxVRtrMaxRoutes.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrStatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrMaxNumRoutes"))
)
if mibBuilder.loadTexts:
    tmnxVRtrMaxRoutes.setStatus(
        "current"
    )

tmnxVRtrDHCPLseStsExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 12)
)
tmnxVRtrDHCPLseStsExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCPClientLease"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCPLseStsExceeded.setStatus(
        "obsolete"
    )

tmnxVRtrDHCPLeaseStateOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 13)
)
tmnxVRtrDHCPLeaseStateOverride.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateOldCiAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateOldChAddr"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCPLeaseStateOverride.setStatus(
        "obsolete"
    )

tmnxVRtrDHCPSuspiciousPcktRcvd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 14)
)
tmnxVRtrDHCPSuspiciousPcktRcvd.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpPacketProblem"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCPSuspiciousPcktRcvd.setStatus(
        "current"
    )

tmnxVRtrDHCPLseStRestoreProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 15)
)
tmnxVRtrDHCPLseStRestoreProblem.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateVRtrId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateCiAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpRestoreLseStateProblem"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCPLseStRestoreProblem.setStatus(
        "obsolete"
    )

tmnxVRtrDHCPLseStatePopulateErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 16)
)
tmnxVRtrDHCPLseStatePopulateErr.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStatePopulateError"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCPLseStatePopulateErr.setStatus(
        "obsolete"
    )

tmnxVRtrBfdSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 17)
)
tmnxVRtrBfdSessionDown.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclDisc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdSessionDown.setStatus(
        "current"
    )

tmnxVRtrBfdMaxSessionOnSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 18)
)
tmnxVRtrBfdMaxSessionOnSlot.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBfdSlotNumber"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrNumberOfBfdSessionsOnSlot"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrBfdMaxSessionReason"))
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdMaxSessionOnSlot.setStatus(
        "current"
    )

tmnxVRtrBfdPortTypeNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 19)
)
tmnxVRtrBfdPortTypeNotSupported.setObjects(
      *(("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortNotifyPortId"),
        ("ALCATEL-IND1-TIMETRA-PORT-MIB", "tmnxPortType"))
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdPortTypeNotSupported.setStatus(
        "current"
    )

tmnxVRtrDHCPIfLseStatesExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 20)
)
tmnxVRtrDHCPIfLseStatesExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapPortId"),
        ("ALCATEL-IND1-TIMETRA-SAP-MIB", "sapEncapValue"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCPLeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewCiAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpClientLease"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCPIfLseStatesExceeded.setStatus(
        "current"
    )

tmnxVRtrDHCP6RelayLseStExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 21)
)
tmnxVRtrDHCP6RelayLseStExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6LeasePopulate"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6NewClientId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpClientLease"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCP6RelayLseStExceeded.setStatus(
        "current"
    )

tmnxVRtrDHCP6ServerLseStExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 22)
)
tmnxVRtrDHCP6ServerLseStExceeded.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfDHCP6ServerMaxLeaseStates"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6NewClientId"),
        ("ALCATEL-IND1-TIMETRA-SERV-MIB", "svcDhcpClientLease"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCP6ServerLseStExceeded.setStatus(
        "current"
    )

tmnxVRtrDHCP6LseStateOverride = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 23)
)
tmnxVRtrDHCP6LseStateOverride.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldAssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateOldChAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6OldClientId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedPrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDhcpLseStateNewChAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6NewClientId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6LeaseOverrideResult"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCP6LseStateOverride.setStatus(
        "current"
    )

tmnxVRtrDHCP6RelayReplyStripUni = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 24)
)
tmnxVRtrDHCP6RelayReplyStripUni.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ServerNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ServerNetAddr"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCP6RelayReplyStripUni.setStatus(
        "current"
    )

tmnxVRtrDHCP6IllegalClientAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 25)
)
tmnxVRtrDHCP6IllegalClientAddr.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddr"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCP6IllegalClientAddr.setStatus(
        "current"
    )

tmnxVRtrDHCP6AssignedIllegSubnet = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 26)
)
tmnxVRtrDHCP6AssignedIllegSubnet.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedNetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6AssignedPrefixLen"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCP6AssignedIllegSubnet.setStatus(
        "current"
    )

tmnxVRtrDHCP6ClientMacUnresolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 27)
)
tmnxVRtrDHCP6ClientMacUnresolved.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrServiceId"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfIndex"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrDHCP6ClientNetAddr"))
)
if mibBuilder.loadTexts:
    tmnxVRtrDHCP6ClientMacUnresolved.setStatus(
        "current"
    )

tmnxVRtrBfdSessionUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 28)
)
tmnxVRtrBfdSessionUp.setObjects(
    ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclDisc")
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdSessionUp.setStatus(
        "current"
    )

tmnxVRtrIPv6MidRouteTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 29)
)
tmnxVRtrIPv6MidRouteTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6MidRouteThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIPv6MidRouteTCA.setStatus(
        "current"
    )

tmnxVRtrIPv6HighRouteTCA = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 30)
)
tmnxVRtrIPv6HighRouteTCA.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6HighRouteThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIPv6HighRouteTCA.setStatus(
        "current"
    )

tmnxVRtrIPv6HighRouteCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 31)
)
tmnxVRtrIPv6HighRouteCleared.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrV6StatCurrNumRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIPv6HighRouteThreshold"))
)
if mibBuilder.loadTexts:
    tmnxVRtrIPv6HighRouteCleared.setStatus(
        "current"
    )

tmnxVRtrStaticRouteCPEStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 32)
)
tmnxVRtrStaticRouteCPEStatus.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeNotifyAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStatRteCpeNotifyAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrInetStaticRouteCpeStatus"))
)
if mibBuilder.loadTexts:
    tmnxVRtrStaticRouteCPEStatus.setStatus(
        "current"
    )

tmnxVRtrBfdSessionDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 33)
)
tmnxVRtrBfdSessionDeleted.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclDisc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionOperFlags"))
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdSessionDeleted.setStatus(
        "current"
    )

tmnxVRtrBfdSessionProtChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 34)
)
tmnxVRtrBfdSessionProtChange.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionLclDisc"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrIfBfdSessionProtocols"))
)
if mibBuilder.loadTexts:
    tmnxVRtrBfdSessionProtChange.setStatus(
        "current"
    )

tmnxVRtrManagedRouteAddFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 3, 0, 35)
)
tmnxVRtrManagedRouteAddFailed.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrID"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedRouteInetAddrType"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedRouteInetAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrManagedRoutePrefixLen"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "vRtrFailureDescription"))
)
if mibBuilder.loadTexts:
    tmnxVRtrManagedRouteAddFailed.setStatus(
        "current"
    )


# Notifications groups

tmnxVRtrNotificationV4v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 19)
)
tmnxVRtrNotificationV4v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMidRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrHighRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrHighRouteCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrIllegalLabelTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMidRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMaxRoutesTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMaxRoutesCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxArpEntriesTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxArpEntriesCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPSuspiciousPcktRcvd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdSessionDown"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdMaxSessionOnSlot"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdPortTypeNotSupported"))
)
if mibBuilder.loadTexts:
    tmnxVRtrNotificationV4v0Group.setStatus(
        "obsolete"
    )

tmnxVRtrObsoleteNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 23)
)
tmnxVRtrObsoleteNotificationGroup.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPAFEntriesExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPLseStsExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPLeaseStateOverride"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPLseStRestoreProblem"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPLseStatePopulateErr"))
)
if mibBuilder.loadTexts:
    tmnxVRtrObsoleteNotificationGroup.setStatus(
        "current"
    )

tmnxVRtrNotificationV5v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 28)
)
tmnxVRtrNotificationV5v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMidRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrHighRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrHighRouteCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrIllegalLabelTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMidRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMaxRoutesTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMaxRoutesCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxArpEntriesTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxArpEntriesCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPSuspiciousPcktRcvd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdSessionDown"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdMaxSessionOnSlot"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdPortTypeNotSupported"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPIfLseStatesExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6RelayLseStExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6ServerLseStExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6LseStateOverride"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6RelayReplyStripUni"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6IllegalClientAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6AssignedIllegSubnet"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6ClientMacUnresolved"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdSessionUp"))
)
if mibBuilder.loadTexts:
    tmnxVRtrNotificationV5v0Group.setStatus(
        "obsolete"
    )

tmnxVRtrNotificationV6v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 2, 40)
)
tmnxVRtrNotificationV6v0Group.setObjects(
      *(("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMidRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrHighRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrHighRouteCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrIllegalLabelTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMidRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMaxRoutesTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMcastMaxRoutesCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxArpEntriesTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxArpEntriesCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrMaxRoutes"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPSuspiciousPcktRcvd"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdSessionDown"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdMaxSessionOnSlot"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdPortTypeNotSupported"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCPIfLseStatesExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6RelayLseStExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6ServerLseStExceeded"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6LseStateOverride"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6RelayReplyStripUni"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6IllegalClientAddr"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6AssignedIllegSubnet"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrDHCP6ClientMacUnresolved"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdSessionUp"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrIPv6MidRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrIPv6HighRouteTCA"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrIPv6HighRouteCleared"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrStaticRouteCPEStatus"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdSessionDeleted"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrBfdSessionProtChange"),
        ("ALCATEL-IND1-TIMETRA-VRTR-MIB", "tmnxVRtrManagedRouteAddFailed"))
)
if mibBuilder.loadTexts:
    tmnxVRtrNotificationV6v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxVRtr7450V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    tmnxVRtr7450V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxVRtr7750V4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 1, 5)
)
if mibBuilder.loadTexts:
    tmnxVRtr7750V4v0Compliance.setStatus(
        "obsolete"
    )

tmnxVRtr7450V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    tmnxVRtr7450V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxVRtr7750V5v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    tmnxVRtr7750V5v0Compliance.setStatus(
        "obsolete"
    )

tmnxVRtr7450V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    tmnxVRtr7450V6v0Compliance.setStatus(
        "current"
    )

tmnxVRtr77x0V6v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 3, 1, 9)
)
if mibBuilder.loadTexts:
    tmnxVRtr77x0V6v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-TIMETRA-VRTR-MIB",
    **{"TmnxVPNId": TmnxVPNId,
       "TmnxInetAddrState": TmnxInetAddrState,
       "TDSCPAppId": TDSCPAppId,
       "TDot1pAppId": TDot1pAppId,
       "timetraVRtrMIBModule": timetraVRtrMIBModule,
       "tmnxVRtrConformance": tmnxVRtrConformance,
       "tmnxVRtrCompliances": tmnxVRtrCompliances,
       "tmnxVRtr7450V4v0Compliance": tmnxVRtr7450V4v0Compliance,
       "tmnxVRtr7750V4v0Compliance": tmnxVRtr7750V4v0Compliance,
       "tmnxVRtr7450V5v0Compliance": tmnxVRtr7450V5v0Compliance,
       "tmnxVRtr7750V5v0Compliance": tmnxVRtr7750V5v0Compliance,
       "tmnxVRtr7450V6v0Compliance": tmnxVRtr7450V6v0Compliance,
       "tmnxVRtr77x0V6v0Compliance": tmnxVRtr77x0V6v0Compliance,
       "tmnxVRtrGroups": tmnxVRtrGroups,
       "tmnxVRtrGlobalR2r1Group": tmnxVRtrGlobalR2r1Group,
       "tmnxVRtrIfSubscrAuthV3v0Group": tmnxVRtrIfSubscrAuthV3v0Group,
       "tmnxVRtrV4v0Group": tmnxVRtrV4v0Group,
       "tmnxVRtrIfV4v0Group": tmnxVRtrIfV4v0Group,
       "tmnxVRtrIpV4v0Group": tmnxVRtrIpV4v0Group,
       "tmnxVRtrObsoletedObjectsV4v0Group": tmnxVRtrObsoletedObjectsV4v0Group,
       "tmnxVRtrBfdV4v0Group": tmnxVRtrBfdV4v0Group,
       "tmnxVRtrNotificationV4v0Group": tmnxVRtrNotificationV4v0Group,
       "tmnxVRtrIPv6IfV4v0Group": tmnxVRtrIPv6IfV4v0Group,
       "tmnxVRtrIPv6V4v0Group": tmnxVRtrIPv6V4v0Group,
       "tmnxVRtrIPv6IpV4v0Group": tmnxVRtrIPv6IpV4v0Group,
       "tmnxVRtrObsoleteNotificationGroup": tmnxVRtrObsoleteNotificationGroup,
       "tmnxVRtrIPv6IpV5v0Group": tmnxVRtrIPv6IpV5v0Group,
       "tmnxVRtrIfV5v0Group": tmnxVRtrIfV5v0Group,
       "tmnxVRtrIpV5v0Group": tmnxVRtrIpV5v0Group,
       "tmnxVRtrV5v0Group": tmnxVRtrV5v0Group,
       "tmnxVRtrNotificationV5v0Group": tmnxVRtrNotificationV5v0Group,
       "tmnxVRtrObsoleteV5v0Group": tmnxVRtrObsoleteV5v0Group,
       "tmnxVRtrNotificationObjV5v0Group": tmnxVRtrNotificationObjV5v0Group,
       "tmnxVRtrIfDhcpServerGroup": tmnxVRtrIfDhcpServerGroup,
       "tmnxVRtrV6v0Group": tmnxVRtrV6v0Group,
       "tmnxVRtrStaticRteCPEChkV6v0Group": tmnxVRtrStaticRteCPEChkV6v0Group,
       "tmnxVRtrIfIpcpV6v0Group": tmnxVRtrIfIpcpV6v0Group,
       "tmnxVRtrIfCpmProtectGroup": tmnxVRtrIfCpmProtectGroup,
       "tmnxDscpAppV6v0Group": tmnxDscpAppV6v0Group,
       "tmnxVRtrIfDHCPRelayGroup": tmnxVRtrIfDHCPRelayGroup,
       "tmnxVRtrGlobalV6v0Group": tmnxVRtrGlobalV6v0Group,
       "tmnxVRtrNotificationObjV6v0Group": tmnxVRtrNotificationObjV6v0Group,
       "tmnxVRtrNotificationV6v0Group": tmnxVRtrNotificationV6v0Group,
       "tmnxVRtrBfdV6v0Group": tmnxVRtrBfdV6v0Group,
       "tmnxVRtrObjs": tmnxVRtrObjs,
       "vRtrConfTable": vRtrConfTable,
       "vRtrConfEntry": vRtrConfEntry,
       "vRtrID": vRtrID,
       "vRtrRowStatus": vRtrRowStatus,
       "vRtrAdminState": vRtrAdminState,
       "vRtrName": vRtrName,
       "vRtrMaxNumRoutes": vRtrMaxNumRoutes,
       "vRtrBgpStatus": vRtrBgpStatus,
       "vRtrMplsStatus": vRtrMplsStatus,
       "vRtrOspfStatus": vRtrOspfStatus,
       "vRtrRipStatus": vRtrRipStatus,
       "vRtrRsvpStatus": vRtrRsvpStatus,
       "vRtrEcmpMaxRoutes": vRtrEcmpMaxRoutes,
       "vRtrAS": vRtrAS,
       "vRtrNewIfIndex": vRtrNewIfIndex,
       "vRtrLdpStatus": vRtrLdpStatus,
       "vRtrIsIsStatus": vRtrIsIsStatus,
       "vRtrRouterId": vRtrRouterId,
       "vRtrTriggeredPolicy": vRtrTriggeredPolicy,
       "vRtrConfederationAS": vRtrConfederationAS,
       "vRtrRouteDistinguisher": vRtrRouteDistinguisher,
       "vRtrMidRouteThreshold": vRtrMidRouteThreshold,
       "vRtrHighRouteThreshold": vRtrHighRouteThreshold,
       "vRtrIllegalLabelThreshold": vRtrIllegalLabelThreshold,
       "vRtrVpnId": vRtrVpnId,
       "vRtrDescription": vRtrDescription,
       "vRtrGracefulRestart": vRtrGracefulRestart,
       "vRtrGracefulRestartType": vRtrGracefulRestartType,
       "vRtrType": vRtrType,
       "vRtrServiceId": vRtrServiceId,
       "vRtrCustId": vRtrCustId,
       "vRtrIgmpStatus": vRtrIgmpStatus,
       "vRtrMaxNumRoutesLogOnly": vRtrMaxNumRoutesLogOnly,
       "vRtrVrfTarget": vRtrVrfTarget,
       "vRtrVrfExportTarget": vRtrVrfExportTarget,
       "vRtrVrfImportTarget": vRtrVrfImportTarget,
       "vRtrPimStatus": vRtrPimStatus,
       "vRtrMaxMcastNumRoutes": vRtrMaxMcastNumRoutes,
       "vRtrMaxMcastNumRoutesLogOnly": vRtrMaxMcastNumRoutesLogOnly,
       "vRtrMcastMidRouteThreshold": vRtrMcastMidRouteThreshold,
       "vRtrIgnoreIcmpRedirect": vRtrIgnoreIcmpRedirect,
       "vRtrOspfv3Status": vRtrOspfv3Status,
       "vRtrMsdpStatus": vRtrMsdpStatus,
       "vRtrVprnType": vRtrVprnType,
       "vRtrSecondaryVrfId": vRtrSecondaryVrfId,
       "vRtrMldStatus": vRtrMldStatus,
       "vRtrIPv6MaxNumRoutes": vRtrIPv6MaxNumRoutes,
       "vRtrIPv6MidRouteThreshold": vRtrIPv6MidRouteThreshold,
       "vRtrIPv6HighRouteThreshold": vRtrIPv6HighRouteThreshold,
       "vRtrIPv6MaxNumRoutesLogOnly": vRtrIPv6MaxNumRoutesLogOnly,
       "vRtrIPv6IgnoreIcmpRedirect": vRtrIPv6IgnoreIcmpRedirect,
       "vRtrMcPathMgmtPlcyName": vRtrMcPathMgmtPlcyName,
       "vRtrStatTable": vRtrStatTable,
       "vRtrStatEntry": vRtrStatEntry,
       "vRtrOperState": vRtrOperState,
       "vRtrDirectRoutes": vRtrDirectRoutes,
       "vRtrDirectActiveRoutes": vRtrDirectActiveRoutes,
       "vRtrStaticRoutes": vRtrStaticRoutes,
       "vRtrStaticActiveRoutes": vRtrStaticActiveRoutes,
       "vRtrOSPFRoutes": vRtrOSPFRoutes,
       "vRtrOSPFActiveRoutes": vRtrOSPFActiveRoutes,
       "vRtrBGPRoutes": vRtrBGPRoutes,
       "vRtrBGPActiveRoutes": vRtrBGPActiveRoutes,
       "vRtrISISRoutes": vRtrISISRoutes,
       "vRtrISISActiveRoutes": vRtrISISActiveRoutes,
       "vRtrRIPRoutes": vRtrRIPRoutes,
       "vRtrRIPActiveRoutes": vRtrRIPActiveRoutes,
       "vRtrAggregateRoutes": vRtrAggregateRoutes,
       "vRtrAggregateActiveRoutes": vRtrAggregateActiveRoutes,
       "vRtrStatConfiguredIfs": vRtrStatConfiguredIfs,
       "vRtrStatActiveIfs": vRtrStatActiveIfs,
       "vRtrStatIllegalLabels": vRtrStatIllegalLabels,
       "vRtrStatCurrNumRoutes": vRtrStatCurrNumRoutes,
       "vRtrStatBGPVpnRoutes": vRtrStatBGPVpnRoutes,
       "vRtrStatBGPVpnActiveRoutes": vRtrStatBGPVpnActiveRoutes,
       "vRtrStatTotalLdpTunnels": vRtrStatTotalLdpTunnels,
       "vRtrStatTotalSdpTunnels": vRtrStatTotalSdpTunnels,
       "vRtrStatActiveLdpTunnels": vRtrStatActiveLdpTunnels,
       "vRtrStatActiveSdpTunnels": vRtrStatActiveSdpTunnels,
       "vRtrMulticastRoutes": vRtrMulticastRoutes,
       "vRtrStatActiveARPEntries": vRtrStatActiveARPEntries,
       "vRtrStatTotalARPEntries": vRtrStatTotalARPEntries,
       "vRtrV6DirectRoutes": vRtrV6DirectRoutes,
       "vRtrV6DirectActiveRoutes": vRtrV6DirectActiveRoutes,
       "vRtrV6StaticRoutes": vRtrV6StaticRoutes,
       "vRtrV6StaticActiveRoutes": vRtrV6StaticActiveRoutes,
       "vRtrV6OSPFRoutes": vRtrV6OSPFRoutes,
       "vRtrV6OSPFActiveRoutes": vRtrV6OSPFActiveRoutes,
       "vRtrV6BGPRoutes": vRtrV6BGPRoutes,
       "vRtrV6BGPActiveRoutes": vRtrV6BGPActiveRoutes,
       "vRtrV6ISISRoutes": vRtrV6ISISRoutes,
       "vRtrV6ISISActiveRoutes": vRtrV6ISISActiveRoutes,
       "vRtrV6RIPRoutes": vRtrV6RIPRoutes,
       "vRtrV6RIPActiveRoutes": vRtrV6RIPActiveRoutes,
       "vRtrV6AggregateRoutes": vRtrV6AggregateRoutes,
       "vRtrV6AggregateActiveRoutes": vRtrV6AggregateActiveRoutes,
       "vRtrV6StatConfiguredIfs": vRtrV6StatConfiguredIfs,
       "vRtrV6StatActiveIfs": vRtrV6StatActiveIfs,
       "vRtrV6StatIllegalLabels": vRtrV6StatIllegalLabels,
       "vRtrV6StatCurrNumRoutes": vRtrV6StatCurrNumRoutes,
       "vRtrV6StatBGPVpnRoutes": vRtrV6StatBGPVpnRoutes,
       "vRtrV6StatBGPVpnActiveRoutes": vRtrV6StatBGPVpnActiveRoutes,
       "vRtrV6StatTotalLdpTunnels": vRtrV6StatTotalLdpTunnels,
       "vRtrV6StatTotalSdpTunnels": vRtrV6StatTotalSdpTunnels,
       "vRtrV6StatActiveLdpTunnels": vRtrV6StatActiveLdpTunnels,
       "vRtrV6StatActiveSdpTunnels": vRtrV6StatActiveSdpTunnels,
       "vRtrV6MulticastRoutes": vRtrV6MulticastRoutes,
       "vRtrV6StatActiveNbrEntries": vRtrV6StatActiveNbrEntries,
       "vRtrV6StatTotalNbrEntries": vRtrV6StatTotalNbrEntries,
       "vRtrSubMgmtRoutes": vRtrSubMgmtRoutes,
       "vRtrSubMgmtActiveRoutes": vRtrSubMgmtActiveRoutes,
       "vRtrStatTotalRsvpTunnels": vRtrStatTotalRsvpTunnels,
       "vRtrStatActiveRsvpTunnels": vRtrStatActiveRsvpTunnels,
       "vRtrV6StatTotalRsvpTunnels": vRtrV6StatTotalRsvpTunnels,
       "vRtrV6StatActiveRsvpTunnels": vRtrV6StatActiveRsvpTunnels,
       "vRtrHostRoutes": vRtrHostRoutes,
       "vRtrHostActiveRoutes": vRtrHostActiveRoutes,
       "vRtrV6HostRoutes": vRtrV6HostRoutes,
       "vRtrV6HostActiveRoutes": vRtrV6HostActiveRoutes,
       "vRtrStatLocalARPEntries": vRtrStatLocalARPEntries,
       "vRtrStatStaticARPEntries": vRtrStatStaticARPEntries,
       "vRtrStatDynamicARPEntries": vRtrStatDynamicARPEntries,
       "vRtrStatManagedARPEntries": vRtrStatManagedARPEntries,
       "vRtrStatInternalARPEntries": vRtrStatInternalARPEntries,
       "vRtrManagedRoutes": vRtrManagedRoutes,
       "vRtrManagedActiveRoutes": vRtrManagedActiveRoutes,
       "vRtrIfTotalNumber": vRtrIfTotalNumber,
       "vRtrIfTable": vRtrIfTable,
       "vRtrIfEntry": vRtrIfEntry,
       "vRtrIfIndex": vRtrIfIndex,
       "vRtrIfRowStatus": vRtrIfRowStatus,
       "vRtrIfType": vRtrIfType,
       "vRtrIfName": vRtrIfName,
       "vRtrIfPortID": vRtrIfPortID,
       "vRtrIfChannelID": vRtrIfChannelID,
       "vRtrIfEncapValue": vRtrIfEncapValue,
       "vRtrIfAdminState": vRtrIfAdminState,
       "vRtrIfOperState": vRtrIfOperState,
       "vRtrIfAlias": vRtrIfAlias,
       "vRtrIfPhysicalAddress": vRtrIfPhysicalAddress,
       "vRtrIfArpTimeout": vRtrIfArpTimeout,
       "vRtrIfIcmpMaskReply": vRtrIfIcmpMaskReply,
       "vRtrIfIcmpRedirects": vRtrIfIcmpRedirects,
       "vRtrIfIcmpNumRedirects": vRtrIfIcmpNumRedirects,
       "vRtrIfIcmpRedirectsTime": vRtrIfIcmpRedirectsTime,
       "vRtrIfIcmpUnreachables": vRtrIfIcmpUnreachables,
       "vRtrIfIcmpNumUnreachables": vRtrIfIcmpNumUnreachables,
       "vRtrIfIcmpUnreachablesTime": vRtrIfIcmpUnreachablesTime,
       "vRtrIfIcmpTtlExpired": vRtrIfIcmpTtlExpired,
       "vRtrIfIcmpNumTtlExpired": vRtrIfIcmpNumTtlExpired,
       "vRtrIfIcmpTtlExpiredTime": vRtrIfIcmpTtlExpiredTime,
       "vRtrIfNtpBroadcast": vRtrIfNtpBroadcast,
       "vRtrIfUnnumbered": vRtrIfUnnumbered,
       "vRtrIfMtu": vRtrIfMtu,
       "vRtrIfQosPolicyId": vRtrIfQosPolicyId,
       "vRtrIfIngressFilterId": vRtrIfIngressFilterId,
       "vRtrIfEgressFilterId": vRtrIfEgressFilterId,
       "vRtrIfDirectedBroadcast": vRtrIfDirectedBroadcast,
       "vRtrIfMplsStatus": vRtrIfMplsStatus,
       "vRtrIfUnnumberedIf": vRtrIfUnnumberedIf,
       "vRtrIfCflowd": vRtrIfCflowd,
       "vRtrIfVPNClass": vRtrIfVPNClass,
       "vRtrIfDescription": vRtrIfDescription,
       "vRtrIfProtocol": vRtrIfProtocol,
       "vRtrIfTosMarkingTrusted": vRtrIfTosMarkingTrusted,
       "vRtrIfServiceId": vRtrIfServiceId,
       "vRtrIfArpPopulate": vRtrIfArpPopulate,
       "vRtrIfIPv6ConfigAllowed": vRtrIfIPv6ConfigAllowed,
       "vRtrIfIPv6OperState": vRtrIfIPv6OperState,
       "vRtrIfIPv6IngressFilterId": vRtrIfIPv6IngressFilterId,
       "vRtrIfIPv6EgressFilterId": vRtrIfIPv6EgressFilterId,
       "vRtrIfIcmpV6Redirects": vRtrIfIcmpV6Redirects,
       "vRtrIfIcmpV6NumRedirects": vRtrIfIcmpV6NumRedirects,
       "vRtrIfIcmpV6RedirectsTime": vRtrIfIcmpV6RedirectsTime,
       "vRtrIfIcmpV6Unreachables": vRtrIfIcmpV6Unreachables,
       "vRtrIfIcmpV6NumUnreachables": vRtrIfIcmpV6NumUnreachables,
       "vRtrIfIcmpV6UnreachablesTime": vRtrIfIcmpV6UnreachablesTime,
       "vRtrIfIcmpV6TimeExceeded": vRtrIfIcmpV6TimeExceeded,
       "vRtrIfIcmpV6NumTimeExceeded": vRtrIfIcmpV6NumTimeExceeded,
       "vRtrIfIcmpV6TimeExceededTime": vRtrIfIcmpV6TimeExceededTime,
       "vRtrIfIcmpV6PktTooBig": vRtrIfIcmpV6PktTooBig,
       "vRtrIfIcmpV6NumPktTooBig": vRtrIfIcmpV6NumPktTooBig,
       "vRtrIfIcmpV6PktTooBigTime": vRtrIfIcmpV6PktTooBigTime,
       "vRtrIfIcmpV6ParamProblem": vRtrIfIcmpV6ParamProblem,
       "vRtrIfIcmpV6NumParamProblem": vRtrIfIcmpV6NumParamProblem,
       "vRtrIfIcmpV6ParamProblemTime": vRtrIfIcmpV6ParamProblemTime,
       "vRtrIfLinkLocalAddressType": vRtrIfLinkLocalAddressType,
       "vRtrIfLinkLocalAddress": vRtrIfLinkLocalAddress,
       "vRtrIfLinkLocalAddressState": vRtrIfLinkLocalAddressState,
       "vRtrIfLastOperStateChange": vRtrIfLastOperStateChange,
       "vRtrIfOperMtu": vRtrIfOperMtu,
       "vRtrIfGlobalIndex": vRtrIfGlobalIndex,
       "vRtrIfDelaySeconds": vRtrIfDelaySeconds,
       "vRtrIfDelayUpTimer": vRtrIfDelayUpTimer,
       "vRtrIfLocalDhcpServerName": vRtrIfLocalDhcpServerName,
       "vRtrIfInitDelayEnable": vRtrIfInitDelayEnable,
       "vRtrIfCpmProtPolicyId": vRtrIfCpmProtPolicyId,
       "vRtrIfCpmProtUncfgdProtoDropCnt": vRtrIfCpmProtUncfgdProtoDropCnt,
       "vRtrIfLdpSyncTimer": vRtrIfLdpSyncTimer,
       "vRtrIfNameTable": vRtrIfNameTable,
       "vRtrIfNameEntry": vRtrIfNameEntry,
       "vRtrIfNameIndex": vRtrIfNameIndex,
       "vRtrIpAddrTable": vRtrIpAddrTable,
       "vRtrIpAddrEntry": vRtrIpAddrEntry,
       "vRiaIndex": vRiaIndex,
       "vRiaRowStatus": vRiaRowStatus,
       "vRiaIpAddress": vRiaIpAddress,
       "vRiaNetMask": vRiaNetMask,
       "vRiaBcastAddrFormat": vRiaBcastAddrFormat,
       "vRiaReasmMaxSize": vRiaReasmMaxSize,
       "vRiaIgpInhibit": vRiaIgpInhibit,
       "vRiaInetAddressType": vRiaInetAddressType,
       "vRiaInetAddress": vRiaInetAddress,
       "vRiaInetPrefixLen": vRiaInetPrefixLen,
       "vRiaInetAddrState": vRiaInetAddrState,
       "vRiaInetEui64": vRiaInetEui64,
       "vRiaInetOperAddress": vRiaInetOperAddress,
       "vRiaInetGwAddressType": vRiaInetGwAddressType,
       "vRiaInetGwAddress": vRiaInetGwAddress,
       "vRiaInetRemoteIpType": vRiaInetRemoteIpType,
       "vRiaInetRemoteIp": vRiaInetRemoteIp,
       "vRtrIpCidrRouteTable": vRtrIpCidrRouteTable,
       "vRtrIpCidrRouteEntry": vRtrIpCidrRouteEntry,
       "vRtrIpCidrRouteLastEnabledTime": vRtrIpCidrRouteLastEnabledTime,
       "vRtrIpCidrRoutePreference": vRtrIpCidrRoutePreference,
       "vRtrIpCidrRouteMetric": vRtrIpCidrRouteMetric,
       "vRtrStaticRouteNumber": vRtrStaticRouteNumber,
       "vRtrStaticRouteTable": vRtrStaticRouteTable,
       "vRtrStaticRouteEntry": vRtrStaticRouteEntry,
       "vRtrStaticRouteDest": vRtrStaticRouteDest,
       "vRtrStaticRouteMask": vRtrStaticRouteMask,
       "vRtrStaticRouteIndex": vRtrStaticRouteIndex,
       "vRtrStaticRouteRowStatus": vRtrStaticRouteRowStatus,
       "vRtrStaticRouteLastEnabledTime": vRtrStaticRouteLastEnabledTime,
       "vRtrStaticRouteStatus": vRtrStaticRouteStatus,
       "vRtrStaticRouteStaticType": vRtrStaticRouteStaticType,
       "vRtrStaticRoutePreference": vRtrStaticRoutePreference,
       "vRtrStaticRouteMetric": vRtrStaticRouteMetric,
       "vRtrStaticRouteEgressIfIndex": vRtrStaticRouteEgressIfIndex,
       "vRtrStaticRouteNextHop": vRtrStaticRouteNextHop,
       "vRtrStaticRouteNextHopUnnumberedIf": vRtrStaticRouteNextHopUnnumberedIf,
       "vRtrStaticRouteAdminState": vRtrStaticRouteAdminState,
       "vRtrStaticRouteIgpShortcut": vRtrStaticRouteIgpShortcut,
       "vRtrStaticRouteDisallowIgp": vRtrStaticRouteDisallowIgp,
       "vRtrStaticRouteTag": vRtrStaticRouteTag,
       "vRtrSvcIpRangeTable": vRtrSvcIpRangeTable,
       "vRtrSvcIpRangeEntry": vRtrSvcIpRangeEntry,
       "vRtrSvcIpRangeAddress": vRtrSvcIpRangeAddress,
       "vRtrSvcIpRangeMask": vRtrSvcIpRangeMask,
       "vRtrSvcIpRangeRowStatus": vRtrSvcIpRangeRowStatus,
       "vRtrSvcIpRangeExclusive": vRtrSvcIpRangeExclusive,
       "vRtrIpNetToMediaTable": vRtrIpNetToMediaTable,
       "vRtrIpNetToMediaEntry": vRtrIpNetToMediaEntry,
       "vRtrIpNetToMediaTimer": vRtrIpNetToMediaTimer,
       "vRtrIpNetToMediaOperState": vRtrIpNetToMediaOperState,
       "vRtrInstanceAggregationTableLastChanged": vRtrInstanceAggregationTableLastChanged,
       "vRtrInstanceAggregationTable": vRtrInstanceAggregationTable,
       "vRtrInstanceAggregationEntry": vRtrInstanceAggregationEntry,
       "vRtrAggregationIpPrefix": vRtrAggregationIpPrefix,
       "vRtrAggregationIpPrefixMask": vRtrAggregationIpPrefixMask,
       "vRtrAggregationRowStatus": vRtrAggregationRowStatus,
       "vRtrAggregationLastChanged": vRtrAggregationLastChanged,
       "vRtrAggregationSummaryOnly": vRtrAggregationSummaryOnly,
       "vRtrAggregationASSet": vRtrAggregationASSet,
       "vRtrAggregationAggregatorAS": vRtrAggregationAggregatorAS,
       "vRtrAggregationAggregatorIPAddr": vRtrAggregationAggregatorIPAddr,
       "vRtrAggregationOperState": vRtrAggregationOperState,
       "vRtrStaticRouteIndexTable": vRtrStaticRouteIndexTable,
       "vRtrStaticRouteIndexEntry": vRtrStaticRouteIndexEntry,
       "vRtrStaticRouteIndexDest": vRtrStaticRouteIndexDest,
       "vRtrStaticRouteIndexMask": vRtrStaticRouteIndexMask,
       "vRtrStaticRouteAvailableIndex": vRtrStaticRouteAvailableIndex,
       "tmnxVRtrGlobalObjs": tmnxVRtrGlobalObjs,
       "vRtrNextVRtrID": vRtrNextVRtrID,
       "vRtrConfiguredVRtrs": vRtrConfiguredVRtrs,
       "vRtrActiveVRtrs": vRtrActiveVRtrs,
       "vRtrRouteThresholdSoakTime": vRtrRouteThresholdSoakTime,
       "vRtrMaxARPEntries": vRtrMaxARPEntries,
       "vRtrIPv6RouteThresholdSoakTime": vRtrIPv6RouteThresholdSoakTime,
       "vRtrPolicyTable": vRtrPolicyTable,
       "vRtrPolicyEntry": vRtrPolicyEntry,
       "vRtrImportPolicy1": vRtrImportPolicy1,
       "vRtrImportPolicy2": vRtrImportPolicy2,
       "vRtrImportPolicy3": vRtrImportPolicy3,
       "vRtrImportPolicy4": vRtrImportPolicy4,
       "vRtrImportPolicy5": vRtrImportPolicy5,
       "vRtrExportPolicy1": vRtrExportPolicy1,
       "vRtrExportPolicy2": vRtrExportPolicy2,
       "vRtrExportPolicy3": vRtrExportPolicy3,
       "vRtrExportPolicy4": vRtrExportPolicy4,
       "vRtrExportPolicy5": vRtrExportPolicy5,
       "vRtrTunnelTable": vRtrTunnelTable,
       "vRtrTunnelEntry": vRtrTunnelEntry,
       "vRtrTunnelDest": vRtrTunnelDest,
       "vRtrTunnelMask": vRtrTunnelMask,
       "vRtrTunnelPreference": vRtrTunnelPreference,
       "vRtrTunnelType": vRtrTunnelType,
       "vRtrTunnelID": vRtrTunnelID,
       "vRtrTunnelNexthop": vRtrTunnelNexthop,
       "vRtrTunnelMetric": vRtrTunnelMetric,
       "vRtrTunnelAge": vRtrTunnelAge,
       "vRtrIfProxyArpTable": vRtrIfProxyArpTable,
       "vRtrIfProxyArpEntry": vRtrIfProxyArpEntry,
       "vRtrIfProxyArp": vRtrIfProxyArp,
       "vRtrIfProxyArpLocal": vRtrIfProxyArpLocal,
       "vRtrIfProxyArpPolicy1": vRtrIfProxyArpPolicy1,
       "vRtrIfProxyArpPolicy2": vRtrIfProxyArpPolicy2,
       "vRtrIfProxyArpPolicy3": vRtrIfProxyArpPolicy3,
       "vRtrIfProxyArpPolicy4": vRtrIfProxyArpPolicy4,
       "vRtrIfProxyArpPolicy5": vRtrIfProxyArpPolicy5,
       "vRtrIfDHCPTable": vRtrIfDHCPTable,
       "vRtrIfDHCPEntry": vRtrIfDHCPEntry,
       "vRtrIfDHCPRelayInfoOption": vRtrIfDHCPRelayInfoOption,
       "vRtrIfDHCPRelayInfoAction": vRtrIfDHCPRelayInfoAction,
       "vRtrIfDHCPRelayCircuitId": vRtrIfDHCPRelayCircuitId,
       "vRtrIfDHCPRelayRemoteId": vRtrIfDHCPRelayRemoteId,
       "vRtrIfDHCPAutoFilter": vRtrIfDHCPAutoFilter,
       "vRtrIfDHCPRelayServer1": vRtrIfDHCPRelayServer1,
       "vRtrIfDHCPRelayServer2": vRtrIfDHCPRelayServer2,
       "vRtrIfDHCPRelayServer3": vRtrIfDHCPRelayServer3,
       "vRtrIfDHCPRelayServer4": vRtrIfDHCPRelayServer4,
       "vRtrIfDHCPRelayServer5": vRtrIfDHCPRelayServer5,
       "vRtrIfDHCPRelayServer6": vRtrIfDHCPRelayServer6,
       "vRtrIfDHCPRelayServer7": vRtrIfDHCPRelayServer7,
       "vRtrIfDHCPRelayServer8": vRtrIfDHCPRelayServer8,
       "vRtrIfDHCPRelayTrusted": vRtrIfDHCPRelayTrusted,
       "vRtrIfDHCPAdminState": vRtrIfDHCPAdminState,
       "vRtrIfDHCPSnooping": vRtrIfDHCPSnooping,
       "vRtrIfDHCPDescription": vRtrIfDHCPDescription,
       "vRtrIfDHCPAutoFilterId": vRtrIfDHCPAutoFilterId,
       "vRtrIfDHCPOperAutoFilter": vRtrIfDHCPOperAutoFilter,
       "vRtrIfDHCPAuthPolicy": vRtrIfDHCPAuthPolicy,
       "vRtrIfDHCPLeasePopulate": vRtrIfDHCPLeasePopulate,
       "vRtrIfDHCPOperLeasePopulate": vRtrIfDHCPOperLeasePopulate,
       "vRtrIfDHCPGiAddressType": vRtrIfDHCPGiAddressType,
       "vRtrIfDHCPGiAddress": vRtrIfDHCPGiAddress,
       "vRtrIfDHCPGiAddressAsSrc": vRtrIfDHCPGiAddressAsSrc,
       "vRtrIfDHCPMatchOption82": vRtrIfDHCPMatchOption82,
       "vRtrIfDHCPRelayRemoteIdStr": vRtrIfDHCPRelayRemoteIdStr,
       "vRtrIfDHCPProxyAdminState": vRtrIfDHCPProxyAdminState,
       "vRtrIfDHCPProxyServerAddr": vRtrIfDHCPProxyServerAddr,
       "vRtrIfDHCPProxyLeaseTime": vRtrIfDHCPProxyLeaseTime,
       "vRtrIfDHCPProxyLTRadiusOverride": vRtrIfDHCPProxyLTRadiusOverride,
       "vRtrIfDHCPVendorIncludeOptions": vRtrIfDHCPVendorIncludeOptions,
       "vRtrIfDHCPVendorOptionString": vRtrIfDHCPVendorOptionString,
       "vRtrIfDHCPLayer2Header": vRtrIfDHCPLayer2Header,
       "vRtrIfDHCPAntiSpoofMacAddr": vRtrIfDHCPAntiSpoofMacAddr,
       "vRtrIfDHCPClientApplications": vRtrIfDHCPClientApplications,
       "vRtrIfDHCPRelayStatsTable": vRtrIfDHCPRelayStatsTable,
       "vRtrIfDHCPRelayStatsEntry": vRtrIfDHCPRelayStatsEntry,
       "vRtrIfDHCPRelayRxPkts": vRtrIfDHCPRelayRxPkts,
       "vRtrIfDHCPRelayTxPkts": vRtrIfDHCPRelayTxPkts,
       "vRtrIfDHCPRelayRxMalformedPkts": vRtrIfDHCPRelayRxMalformedPkts,
       "vRtrIfDHCPRelayRxUntrustedPkts": vRtrIfDHCPRelayRxUntrustedPkts,
       "vRtrIfDHCPRelayClientPktsDiscarded": vRtrIfDHCPRelayClientPktsDiscarded,
       "vRtrIfDHCPRelayClientPktsRelayed": vRtrIfDHCPRelayClientPktsRelayed,
       "vRtrIfDHCPRelayServerPktsDiscarded": vRtrIfDHCPRelayServerPktsDiscarded,
       "vRtrIfDHCPRelayServerPktsRelayed": vRtrIfDHCPRelayServerPktsRelayed,
       "vRtrIfDHCPRelayAuthPktsDiscarded": vRtrIfDHCPRelayAuthPktsDiscarded,
       "vRtrIfDHCPRelayAuthPktsSuccess": vRtrIfDHCPRelayAuthPktsSuccess,
       "vRtrIfDHCPRelayClientPktsSnooped": vRtrIfDHCPRelayClientPktsSnooped,
       "vRtrIfDHCPRelayServerPktsSnooped": vRtrIfDHCPRelayServerPktsSnooped,
       "vRtrIfDHCPRelayClientPktsProxRad": vRtrIfDHCPRelayClientPktsProxRad,
       "vRtrIfDHCPRelayClientPktsProxLS": vRtrIfDHCPRelayClientPktsProxLS,
       "vRtrIfDHCPRelayPktsGenRelease": vRtrIfDHCPRelayPktsGenRelease,
       "vRtrIfDHCPRelayPktsGenForceRenew": vRtrIfDHCPRelayPktsGenForceRenew,
       "tmnxVRtrNotificationObjects": tmnxVRtrNotificationObjects,
       "vRtrAutoFilterDHCPClientAddress": vRtrAutoFilterDHCPClientAddress,
       "vRtrAutoFilterDHCPClientLease": vRtrAutoFilterDHCPClientLease,
       "vRtrDHCPClientLease": vRtrDHCPClientLease,
       "vRtrDhcpLseStateOldCiAddr": vRtrDhcpLseStateOldCiAddr,
       "vRtrDhcpLseStateOldChAddr": vRtrDhcpLseStateOldChAddr,
       "vRtrDhcpLseStateNewCiAddr": vRtrDhcpLseStateNewCiAddr,
       "vRtrDhcpLseStateNewChAddr": vRtrDhcpLseStateNewChAddr,
       "vRtrDhcpRestoreLseStateCiAddr": vRtrDhcpRestoreLseStateCiAddr,
       "vRtrDhcpRestoreLseStateVRtrId": vRtrDhcpRestoreLseStateVRtrId,
       "vRtrDhcpRestoreLseStateIfIndex": vRtrDhcpRestoreLseStateIfIndex,
       "vRtrDhcpRestoreLseStateProblem": vRtrDhcpRestoreLseStateProblem,
       "vRtrDhcpPacketProblem": vRtrDhcpPacketProblem,
       "vRtrDhcpLseStatePopulateError": vRtrDhcpLseStatePopulateError,
       "vRtrBfdSlotNumber": vRtrBfdSlotNumber,
       "vRtrNumberOfBfdSessionsOnSlot": vRtrNumberOfBfdSessionsOnSlot,
       "vRtrBfdMaxSessionReason": vRtrBfdMaxSessionReason,
       "vRtrDHCP6ServerNetAddrType": vRtrDHCP6ServerNetAddrType,
       "vRtrDHCP6ServerNetAddr": vRtrDHCP6ServerNetAddr,
       "vRtrDHCP6ClientNetAddrType": vRtrDHCP6ClientNetAddrType,
       "vRtrDHCP6ClientNetAddr": vRtrDHCP6ClientNetAddr,
       "vRtrDHCP6AssignedNetAddrType": vRtrDHCP6AssignedNetAddrType,
       "vRtrDHCP6AssignedNetAddr": vRtrDHCP6AssignedNetAddr,
       "vRtrDHCP6AssignedPrefixLen": vRtrDHCP6AssignedPrefixLen,
       "vRtrDHCP6OldAssignedNetAddrType": vRtrDHCP6OldAssignedNetAddrType,
       "vRtrDHCP6OldAssignedNetAddr": vRtrDHCP6OldAssignedNetAddr,
       "vRtrDHCP6OldAssignedPrefixLen": vRtrDHCP6OldAssignedPrefixLen,
       "vRtrDHCP6NewClientId": vRtrDHCP6NewClientId,
       "vRtrDHCP6OldClientId": vRtrDHCP6OldClientId,
       "vRtrDHCP6LeaseOverrideResult": vRtrDHCP6LeaseOverrideResult,
       "vRtrInetStatRteCpeNotifyAddrType": vRtrInetStatRteCpeNotifyAddrType,
       "vRtrInetStatRteCpeNotifyAddr": vRtrInetStatRteCpeNotifyAddr,
       "vRtrInetStaticRouteCpeStatus": vRtrInetStaticRouteCpeStatus,
       "vRtrManagedRouteInetAddrType": vRtrManagedRouteInetAddrType,
       "vRtrManagedRouteInetAddr": vRtrManagedRouteInetAddr,
       "vRtrManagedRoutePrefixLen": vRtrManagedRoutePrefixLen,
       "vRtrFailureDescription": vRtrFailureDescription,
       "vRtrIfDHCPLeaseStateTable": vRtrIfDHCPLeaseStateTable,
       "vRtrIfDHCPLeaseStateEntry": vRtrIfDHCPLeaseStateEntry,
       "vRtrIfDHCPLseStateCiAddr": vRtrIfDHCPLseStateCiAddr,
       "vRtrIfDHCPLseStateChAddr": vRtrIfDHCPLseStateChAddr,
       "vRtrIfDHCPLseStateRemainLseTime": vRtrIfDHCPLseStateRemainLseTime,
       "vRtrIfDHCPLseStateOption82": vRtrIfDHCPLseStateOption82,
       "vRtrIfDHCPLseStatePersistKey": vRtrIfDHCPLseStatePersistKey,
       "vRtrAdvPrefixTable": vRtrAdvPrefixTable,
       "vRtrAdvPrefixEntry": vRtrAdvPrefixEntry,
       "vRtrAdvPrefixIfIndex": vRtrAdvPrefixIfIndex,
       "vRtrAdvPrefixPrefix": vRtrAdvPrefixPrefix,
       "vRtrAdvPrefixLength": vRtrAdvPrefixLength,
       "vRtrAdvPrefixRowStatus": vRtrAdvPrefixRowStatus,
       "vRtrAdvPrefixOnLinkFlag": vRtrAdvPrefixOnLinkFlag,
       "vRtrAdvPrefixAutonomousFlag": vRtrAdvPrefixAutonomousFlag,
       "vRtrAdvPrefixPreferredLifetime": vRtrAdvPrefixPreferredLifetime,
       "vRtrAdvPrefixValidLifetime": vRtrAdvPrefixValidLifetime,
       "vRtrInetStaticRouteTable": vRtrInetStaticRouteTable,
       "vRtrInetStaticRouteEntry": vRtrInetStaticRouteEntry,
       "vRtrInetStaticRouteDestType": vRtrInetStaticRouteDestType,
       "vRtrInetStaticRouteDest": vRtrInetStaticRouteDest,
       "vRtrInetStaticRouteDestPfxLen": vRtrInetStaticRouteDestPfxLen,
       "vRtrInetStaticRouteIndex": vRtrInetStaticRouteIndex,
       "vRtrInetStaticRouteRowStatus": vRtrInetStaticRouteRowStatus,
       "vRtrInetStaticRouteLastEnabledTime": vRtrInetStaticRouteLastEnabledTime,
       "vRtrInetStaticRouteStatus": vRtrInetStaticRouteStatus,
       "vRtrInetStaticRouteStaticType": vRtrInetStaticRouteStaticType,
       "vRtrInetStaticRoutePreference": vRtrInetStaticRoutePreference,
       "vRtrInetStaticRouteMetric": vRtrInetStaticRouteMetric,
       "vRtrInetStaticRouteEgressIfIndex": vRtrInetStaticRouteEgressIfIndex,
       "vRtrInetStaticRouteNextHopType": vRtrInetStaticRouteNextHopType,
       "vRtrInetStaticRouteNextHop": vRtrInetStaticRouteNextHop,
       "vRtrInetStaticRouteNextHopIf": vRtrInetStaticRouteNextHopIf,
       "vRtrInetStaticRouteAdminState": vRtrInetStaticRouteAdminState,
       "vRtrInetStaticRouteIgpShortcut": vRtrInetStaticRouteIgpShortcut,
       "vRtrInetStaticRouteDisallowIgp": vRtrInetStaticRouteDisallowIgp,
       "vRtrInetStaticRouteTag": vRtrInetStaticRouteTag,
       "vRtrInetStaticRouteEnableBfd": vRtrInetStaticRouteEnableBfd,
       "vRtrInetStaticRouteCpeAddrType": vRtrInetStaticRouteCpeAddrType,
       "vRtrInetStaticRouteCpeAddr": vRtrInetStaticRouteCpeAddr,
       "vRtrInetStaticRouteCpeInterval": vRtrInetStaticRouteCpeInterval,
       "vRtrInetStaticRouteCpeDropCnt": vRtrInetStaticRouteCpeDropCnt,
       "vRtrInetStaticRouteCpeEnableLog": vRtrInetStaticRouteCpeEnableLog,
       "vRtrInetStaticRouteIndexTable": vRtrInetStaticRouteIndexTable,
       "vRtrInetStaticRouteIndexEntry": vRtrInetStaticRouteIndexEntry,
       "vRtrInetStaticRouteAvailIndex": vRtrInetStaticRouteAvailIndex,
       "vRtrInetInstAggrTblLastChged": vRtrInetInstAggrTblLastChged,
       "vRtrInetInstAggrTable": vRtrInetInstAggrTable,
       "vRtrInetInstAggrEntry": vRtrInetInstAggrEntry,
       "vRtrInetAggrIpPrefixType": vRtrInetAggrIpPrefixType,
       "vRtrInetAggrIpPrefix": vRtrInetAggrIpPrefix,
       "vRtrInetAggrIpPrefixLen": vRtrInetAggrIpPrefixLen,
       "vRtrInetAggrRowStatus": vRtrInetAggrRowStatus,
       "vRtrInetAggrLastChanged": vRtrInetAggrLastChanged,
       "vRtrInetAggrSummaryOnly": vRtrInetAggrSummaryOnly,
       "vRtrInetAggrASSet": vRtrInetAggrASSet,
       "vRtrInetAggrAggregatorAS": vRtrInetAggrAggregatorAS,
       "vRtrInetAggrAggregatorIPAddr": vRtrInetAggrAggregatorIPAddr,
       "vRtrInetAggrOperState": vRtrInetAggrOperState,
       "vRtrInetSvcIpRangeTable": vRtrInetSvcIpRangeTable,
       "vRtrInetSvcIpRangeEntry": vRtrInetSvcIpRangeEntry,
       "vRtrInetSvcIpRangeAddrType": vRtrInetSvcIpRangeAddrType,
       "vRtrInetSvcIpRangeAddr": vRtrInetSvcIpRangeAddr,
       "vRtrInetSvcIpRangePfxLen": vRtrInetSvcIpRangePfxLen,
       "vRtrInetSvcIpRangeRowStatus": vRtrInetSvcIpRangeRowStatus,
       "vRtrInetSvcIpRangeExclusive": vRtrInetSvcIpRangeExclusive,
       "vRtrIcmp6Table": vRtrIcmp6Table,
       "vRtrIcmp6Entry": vRtrIcmp6Entry,
       "vRtrIcmp6InMsgs": vRtrIcmp6InMsgs,
       "vRtrIcmp6InErrors": vRtrIcmp6InErrors,
       "vRtrIcmp6InDestUnreachs": vRtrIcmp6InDestUnreachs,
       "vRtrIcmp6InAdminProhibs": vRtrIcmp6InAdminProhibs,
       "vRtrIcmp6InTimeExcds": vRtrIcmp6InTimeExcds,
       "vRtrIcmp6InParmProblems": vRtrIcmp6InParmProblems,
       "vRtrIcmp6InPktTooBigs": vRtrIcmp6InPktTooBigs,
       "vRtrIcmp6InEchos": vRtrIcmp6InEchos,
       "vRtrIcmp6InEchoReplies": vRtrIcmp6InEchoReplies,
       "vRtrIcmp6InRtrSolicits": vRtrIcmp6InRtrSolicits,
       "vRtrIcmp6InRtrAdvertisements": vRtrIcmp6InRtrAdvertisements,
       "vRtrIcmp6InNbrSolicits": vRtrIcmp6InNbrSolicits,
       "vRtrIcmp6InNbrAdvertisements": vRtrIcmp6InNbrAdvertisements,
       "vRtrIcmp6InRedirects": vRtrIcmp6InRedirects,
       "vRtrIcmp6InGrpMembQueries": vRtrIcmp6InGrpMembQueries,
       "vRtrIcmp6InGrpMembResponses": vRtrIcmp6InGrpMembResponses,
       "vRtrIcmp6InGrpMembReductions": vRtrIcmp6InGrpMembReductions,
       "vRtrIcmp6OutMsgs": vRtrIcmp6OutMsgs,
       "vRtrIcmp6OutErrors": vRtrIcmp6OutErrors,
       "vRtrIcmp6OutDestUnreachs": vRtrIcmp6OutDestUnreachs,
       "vRtrIcmp6OutAdminProhibs": vRtrIcmp6OutAdminProhibs,
       "vRtrIcmp6OutTimeExcds": vRtrIcmp6OutTimeExcds,
       "vRtrIcmp6OutParmProblems": vRtrIcmp6OutParmProblems,
       "vRtrIcmp6OutPktTooBigs": vRtrIcmp6OutPktTooBigs,
       "vRtrIcmp6OutEchos": vRtrIcmp6OutEchos,
       "vRtrIcmp6OutEchoReplies": vRtrIcmp6OutEchoReplies,
       "vRtrIcmp6OutRtrSolicits": vRtrIcmp6OutRtrSolicits,
       "vRtrIcmp6OutRtrAdvertisements": vRtrIcmp6OutRtrAdvertisements,
       "vRtrIcmp6OutNbrSolicits": vRtrIcmp6OutNbrSolicits,
       "vRtrIcmp6OutNbrAdvertisements": vRtrIcmp6OutNbrAdvertisements,
       "vRtrIcmp6OutRedirects": vRtrIcmp6OutRedirects,
       "vRtrIcmp6OutGrpMembQueries": vRtrIcmp6OutGrpMembQueries,
       "vRtrIcmp6OutGrpMembResponses": vRtrIcmp6OutGrpMembResponses,
       "vRtrIcmp6OutGrpMembReductions": vRtrIcmp6OutGrpMembReductions,
       "vRtrIfIcmp6Table": vRtrIfIcmp6Table,
       "vRtrIfIcmp6Entry": vRtrIfIcmp6Entry,
       "vRtrIfIcmp6InMsgs": vRtrIfIcmp6InMsgs,
       "vRtrIfIcmp6InErrors": vRtrIfIcmp6InErrors,
       "vRtrIfIcmp6InDestUnreachs": vRtrIfIcmp6InDestUnreachs,
       "vRtrIfIcmp6InAdminProhibs": vRtrIfIcmp6InAdminProhibs,
       "vRtrIfIcmp6InTimeExcds": vRtrIfIcmp6InTimeExcds,
       "vRtrIfIcmp6InParmProblems": vRtrIfIcmp6InParmProblems,
       "vRtrIfIcmp6InPktTooBigs": vRtrIfIcmp6InPktTooBigs,
       "vRtrIfIcmp6InEchos": vRtrIfIcmp6InEchos,
       "vRtrIfIcmp6InEchoReplies": vRtrIfIcmp6InEchoReplies,
       "vRtrIfIcmp6InRtrSolicits": vRtrIfIcmp6InRtrSolicits,
       "vRtrIfIcmp6InRtrAdvertisements": vRtrIfIcmp6InRtrAdvertisements,
       "vRtrIfIcmp6InNbrSolicits": vRtrIfIcmp6InNbrSolicits,
       "vRtrIfIcmp6InNbrAdvertisements": vRtrIfIcmp6InNbrAdvertisements,
       "vRtrIfIcmp6InRedirects": vRtrIfIcmp6InRedirects,
       "vRtrIfIcmp6InGrpMembQueries": vRtrIfIcmp6InGrpMembQueries,
       "vRtrIfIcmp6InGrpMembResponses": vRtrIfIcmp6InGrpMembResponses,
       "vRtrIfIcmp6InGrpMembReductions": vRtrIfIcmp6InGrpMembReductions,
       "vRtrIfIcmp6OutMsgs": vRtrIfIcmp6OutMsgs,
       "vRtrIfIcmp6OutErrors": vRtrIfIcmp6OutErrors,
       "vRtrIfIcmp6OutDestUnreachs": vRtrIfIcmp6OutDestUnreachs,
       "vRtrIfIcmp6OutAdminProhibs": vRtrIfIcmp6OutAdminProhibs,
       "vRtrIfIcmp6OutTimeExcds": vRtrIfIcmp6OutTimeExcds,
       "vRtrIfIcmp6OutParmProblems": vRtrIfIcmp6OutParmProblems,
       "vRtrIfIcmp6OutPktTooBigs": vRtrIfIcmp6OutPktTooBigs,
       "vRtrIfIcmp6OutEchos": vRtrIfIcmp6OutEchos,
       "vRtrIfIcmp6OutEchoReplies": vRtrIfIcmp6OutEchoReplies,
       "vRtrIfIcmp6OutRtrSolicits": vRtrIfIcmp6OutRtrSolicits,
       "vRtrIfIcmp6OutRtrSolicitsTime": vRtrIfIcmp6OutRtrSolicitsTime,
       "vRtrIfIcmp6OutRtrAdvertisements": vRtrIfIcmp6OutRtrAdvertisements,
       "vRtrIfIcmp6OutRtrAdvTime": vRtrIfIcmp6OutRtrAdvTime,
       "vRtrIfIcmp6OutNbrSolicits": vRtrIfIcmp6OutNbrSolicits,
       "vRtrIfIcmp6OutNbrSolicitsTime": vRtrIfIcmp6OutNbrSolicitsTime,
       "vRtrIfIcmp6OutNbrAdvertisements": vRtrIfIcmp6OutNbrAdvertisements,
       "vRtrIfIcmp6OutNbrAdvTime": vRtrIfIcmp6OutNbrAdvTime,
       "vRtrIfIcmp6OutRedirects": vRtrIfIcmp6OutRedirects,
       "vRtrIfIcmp6OutGrpMembQueries": vRtrIfIcmp6OutGrpMembQueries,
       "vRtrIfIcmp6OutGrpMembResponses": vRtrIfIcmp6OutGrpMembResponses,
       "vRtrIfIcmp6OutGrpMembReductions": vRtrIfIcmp6OutGrpMembReductions,
       "vRtrIfBfdTable": vRtrIfBfdTable,
       "vRtrIfBfdEntry": vRtrIfBfdEntry,
       "vRtrIfBfdAdminState": vRtrIfBfdAdminState,
       "vRtrIfBfdTransmitInterval": vRtrIfBfdTransmitInterval,
       "vRtrIfBfdReceiveInterval": vRtrIfBfdReceiveInterval,
       "vRtrIfBfdMultiplier": vRtrIfBfdMultiplier,
       "vRtrIfBfdEchoInterval": vRtrIfBfdEchoInterval,
       "vRtrIfBfdSessionTable": vRtrIfBfdSessionTable,
       "vRtrIfBfdSessionEntry": vRtrIfBfdSessionEntry,
       "vRtrIfBfdSessionLclAddrType": vRtrIfBfdSessionLclAddrType,
       "vRtrIfBfdSessionLclAddr": vRtrIfBfdSessionLclAddr,
       "vRtrIfBfdSessionRemAddrType": vRtrIfBfdSessionRemAddrType,
       "vRtrIfBfdSessionRemAddr": vRtrIfBfdSessionRemAddr,
       "vRtrIfBfdSessionOperState": vRtrIfBfdSessionOperState,
       "vRtrIfBfdSessionState": vRtrIfBfdSessionState,
       "vRtrIfBfdSessionOperFlags": vRtrIfBfdSessionOperFlags,
       "vRtrIfBfdSessionMesgRecv": vRtrIfBfdSessionMesgRecv,
       "vRtrIfBfdSessionMesgSent": vRtrIfBfdSessionMesgSent,
       "vRtrIfBfdSessionLastDownTime": vRtrIfBfdSessionLastDownTime,
       "vRtrIfBfdSessionLastUpTime": vRtrIfBfdSessionLastUpTime,
       "vRtrIfBfdSessionUpCount": vRtrIfBfdSessionUpCount,
       "vRtrIfBfdSessionDownCount": vRtrIfBfdSessionDownCount,
       "vRtrIfBfdSessionLclDisc": vRtrIfBfdSessionLclDisc,
       "vRtrIfBfdSessionRemDisc": vRtrIfBfdSessionRemDisc,
       "vRtrIfBfdSessionProtocols": vRtrIfBfdSessionProtocols,
       "vRtrIfBfdSessionTxInterval": vRtrIfBfdSessionTxInterval,
       "vRtrIfBfdSessionRxInterval": vRtrIfBfdSessionRxInterval,
       "vRtrIfBfdSessionType": vRtrIfBfdSessionType,
       "vRtrIfDHCP6TableLastChanged": vRtrIfDHCP6TableLastChanged,
       "vRtrIfDHCP6Table": vRtrIfDHCP6Table,
       "vRtrIfDHCP6Entry": vRtrIfDHCP6Entry,
       "vRtrIfDHCP6LastChanged": vRtrIfDHCP6LastChanged,
       "vRtrIfDHCP6AdminState": vRtrIfDHCP6AdminState,
       "vRtrIfDHCP6OperState": vRtrIfDHCP6OperState,
       "vRtrIfDHCP6Description": vRtrIfDHCP6Description,
       "vRtrIfDHCP6RelayServer1": vRtrIfDHCP6RelayServer1,
       "vRtrIfDHCP6RelayServer2": vRtrIfDHCP6RelayServer2,
       "vRtrIfDHCP6RelayServer3": vRtrIfDHCP6RelayServer3,
       "vRtrIfDHCP6RelayServer4": vRtrIfDHCP6RelayServer4,
       "vRtrIfDHCP6RelayServer5": vRtrIfDHCP6RelayServer5,
       "vRtrIfDHCP6RelayServer6": vRtrIfDHCP6RelayServer6,
       "vRtrIfDHCP6RelayServer7": vRtrIfDHCP6RelayServer7,
       "vRtrIfDHCP6RelayServer8": vRtrIfDHCP6RelayServer8,
       "vRtrIfDHCP6RelayItfIdOption": vRtrIfDHCP6RelayItfIdOption,
       "vRtrIfDHCP6LeasePopulate": vRtrIfDHCP6LeasePopulate,
       "vRtrIfDHCP6CurrLeasePopulate": vRtrIfDHCP6CurrLeasePopulate,
       "vRtrIfDHCP6SourceAddress": vRtrIfDHCP6SourceAddress,
       "vRtrIfDHCP6EnableNgbrResolution": vRtrIfDHCP6EnableNgbrResolution,
       "vRtrIfDHCP6RemoteIdOption": vRtrIfDHCP6RemoteIdOption,
       "vRtrIfDHCP6PfxdAdminState": vRtrIfDHCP6PfxdAdminState,
       "vRtrIfDHCP6ServerMaxLeaseStates": vRtrIfDHCP6ServerMaxLeaseStates,
       "vRtrIfDHCP6CurrServerLeaseStates": vRtrIfDHCP6CurrServerLeaseStates,
       "vRtrIfDHCP6ItfIdString": vRtrIfDHCP6ItfIdString,
       "vRtrIfGlobalIndexTable": vRtrIfGlobalIndexTable,
       "vRtrIfGlobalIndexEntry": vRtrIfGlobalIndexEntry,
       "vRtrIfGlobalIndexvRtrID": vRtrIfGlobalIndexvRtrID,
       "vRtrIfGlobalIndexvRtrIfIndex": vRtrIfGlobalIndexvRtrIfIndex,
       "vRtrIfProxyNDTable": vRtrIfProxyNDTable,
       "vRtrIfProxyNDEntry": vRtrIfProxyNDEntry,
       "vRtrIfProxyNDLocal": vRtrIfProxyNDLocal,
       "vRtrIfProxyNDPolicy1": vRtrIfProxyNDPolicy1,
       "vRtrIfProxyNDPolicy2": vRtrIfProxyNDPolicy2,
       "vRtrIfProxyNDPolicy3": vRtrIfProxyNDPolicy3,
       "vRtrIfProxyNDPolicy4": vRtrIfProxyNDPolicy4,
       "vRtrIfProxyNDPolicy5": vRtrIfProxyNDPolicy5,
       "vRtrIfDHCP6PfxDelegationLstChgd": vRtrIfDHCP6PfxDelegationLstChgd,
       "vRtrIfDHCP6PfxDelegationTable": vRtrIfDHCP6PfxDelegationTable,
       "vRtrIfDHCP6PfxDelegationEntry": vRtrIfDHCP6PfxDelegationEntry,
       "vRtrIfDHCP6PfxdPrefix": vRtrIfDHCP6PfxdPrefix,
       "vRtrIfDHCP6PfxdPrefixLen": vRtrIfDHCP6PfxdPrefixLen,
       "vRtrIfDHCP6PfxdRowStatus": vRtrIfDHCP6PfxdRowStatus,
       "vRtrIfDHCP6PfxdLastChanged": vRtrIfDHCP6PfxdLastChanged,
       "vRtrIfDHCP6PfxdDUID": vRtrIfDHCP6PfxdDUID,
       "vRtrIfDHCP6PfxdIAID": vRtrIfDHCP6PfxdIAID,
       "vRtrIfDHCP6PfxdPrefLifetime": vRtrIfDHCP6PfxdPrefLifetime,
       "vRtrIfDHCP6PfxdValidLifetime": vRtrIfDHCP6PfxdValidLifetime,
       "vRtrDHCP6DropStatTable": vRtrDHCP6DropStatTable,
       "vRtrDHCP6DropStatEntry": vRtrDHCP6DropStatEntry,
       "vRtrDHCP6DropStatReason": vRtrDHCP6DropStatReason,
       "vRtrDHCP6DropStatLastCleared": vRtrDHCP6DropStatLastCleared,
       "vRtrDHCP6DropStatPktsDropped": vRtrDHCP6DropStatPktsDropped,
       "vRtrDHCP6MsgStatTable": vRtrDHCP6MsgStatTable,
       "vRtrDHCP6MsgStatEntry": vRtrDHCP6MsgStatEntry,
       "vRtrDHCP6MsgStatsMsgType": vRtrDHCP6MsgStatsMsgType,
       "vRtrDHCP6MsgStatsLstClrd": vRtrDHCP6MsgStatsLstClrd,
       "vRtrDHCP6MsgStatsRcvd": vRtrDHCP6MsgStatsRcvd,
       "vRtrDHCP6MsgStatsSent": vRtrDHCP6MsgStatsSent,
       "vRtrDHCP6MsgStatsDropped": vRtrDHCP6MsgStatsDropped,
       "vRtrIfIpcpTable": vRtrIfIpcpTable,
       "vRtrIfIpcpEntry": vRtrIfIpcpEntry,
       "vRtrIfIpcpPeerAddrType": vRtrIfIpcpPeerAddrType,
       "vRtrIfIpcpPeerAddr": vRtrIfIpcpPeerAddr,
       "vRtrIfIpcpPriDnsAddrType": vRtrIfIpcpPriDnsAddrType,
       "vRtrIfIpcpPriDnsAddr": vRtrIfIpcpPriDnsAddr,
       "vRtrIfIpcpSecDnsAddrType": vRtrIfIpcpSecDnsAddrType,
       "vRtrIfIpcpSecDnsAddr": vRtrIfIpcpSecDnsAddr,
       "vRtrInetStatRteCpeChkStatsTable": vRtrInetStatRteCpeChkStatsTable,
       "vRtrInetStatRteCpeChkStatsEntry": vRtrInetStatRteCpeChkStatsEntry,
       "vRtrInetStatRteCpeChkUpTime": vRtrInetStatRteCpeChkUpTime,
       "vRtrInetStatRteCpeChkInPktCnt": vRtrInetStatRteCpeChkInPktCnt,
       "vRtrInetStatRteCpeChkOutPktCnt": vRtrInetStatRteCpeChkOutPktCnt,
       "vRtrInetStatRteCpeChkDownTrans": vRtrInetStatRteCpeChkDownTrans,
       "vRtrInetStatRteCpeChkUpTrans": vRtrInetStatRteCpeChkUpTrans,
       "vRtrInetStatRteCpeChkTTL": vRtrInetStatRteCpeChkTTL,
       "tmnxDscpAppTableLastChanged": tmnxDscpAppTableLastChanged,
       "tmnxDscpAppTable": tmnxDscpAppTable,
       "tmnxDscpAppEntry": tmnxDscpAppEntry,
       "tmnxDscpAppId": tmnxDscpAppId,
       "tmnxDscpAppLastChanged": tmnxDscpAppLastChanged,
       "tmnxDscpAppDscpValue": tmnxDscpAppDscpValue,
       "tmnxDscpFCTableLastChanged": tmnxDscpFCTableLastChanged,
       "tmnxDscpFCTable": tmnxDscpFCTable,
       "tmnxDscpFCEntry": tmnxDscpFCEntry,
       "tmnxDscpFCDscpValue": tmnxDscpFCDscpValue,
       "tmnxDscpFCLastChanged": tmnxDscpFCLastChanged,
       "tmnxDscpFCValue": tmnxDscpFCValue,
       "tmnxDot1pAppTableLastChanged": tmnxDot1pAppTableLastChanged,
       "tmnxDot1pAppTable": tmnxDot1pAppTable,
       "tmnxDot1pAppEntry": tmnxDot1pAppEntry,
       "tmnxDot1pAppId": tmnxDot1pAppId,
       "tmnxDot1pAppLastChanged": tmnxDot1pAppLastChanged,
       "tmnxDot1pAppValue": tmnxDot1pAppValue,
       "tmnxVRtrNotifyPrefix": tmnxVRtrNotifyPrefix,
       "tmnxVRtrNotifications": tmnxVRtrNotifications,
       "tmnxVRtrMidRouteTCA": tmnxVRtrMidRouteTCA,
       "tmnxVRtrHighRouteTCA": tmnxVRtrHighRouteTCA,
       "tmnxVRtrHighRouteCleared": tmnxVRtrHighRouteCleared,
       "tmnxVRtrIllegalLabelTCA": tmnxVRtrIllegalLabelTCA,
       "tmnxVRtrMcastMidRouteTCA": tmnxVRtrMcastMidRouteTCA,
       "tmnxVRtrMcastMaxRoutesTCA": tmnxVRtrMcastMaxRoutesTCA,
       "tmnxVRtrMcastMaxRoutesCleared": tmnxVRtrMcastMaxRoutesCleared,
       "tmnxVRtrMaxArpEntriesTCA": tmnxVRtrMaxArpEntriesTCA,
       "tmnxVRtrMaxArpEntriesCleared": tmnxVRtrMaxArpEntriesCleared,
       "tmnxVRtrDHCPAFEntriesExceeded": tmnxVRtrDHCPAFEntriesExceeded,
       "tmnxVRtrMaxRoutes": tmnxVRtrMaxRoutes,
       "tmnxVRtrDHCPLseStsExceeded": tmnxVRtrDHCPLseStsExceeded,
       "tmnxVRtrDHCPLeaseStateOverride": tmnxVRtrDHCPLeaseStateOverride,
       "tmnxVRtrDHCPSuspiciousPcktRcvd": tmnxVRtrDHCPSuspiciousPcktRcvd,
       "tmnxVRtrDHCPLseStRestoreProblem": tmnxVRtrDHCPLseStRestoreProblem,
       "tmnxVRtrDHCPLseStatePopulateErr": tmnxVRtrDHCPLseStatePopulateErr,
       "tmnxVRtrBfdSessionDown": tmnxVRtrBfdSessionDown,
       "tmnxVRtrBfdMaxSessionOnSlot": tmnxVRtrBfdMaxSessionOnSlot,
       "tmnxVRtrBfdPortTypeNotSupported": tmnxVRtrBfdPortTypeNotSupported,
       "tmnxVRtrDHCPIfLseStatesExceeded": tmnxVRtrDHCPIfLseStatesExceeded,
       "tmnxVRtrDHCP6RelayLseStExceeded": tmnxVRtrDHCP6RelayLseStExceeded,
       "tmnxVRtrDHCP6ServerLseStExceeded": tmnxVRtrDHCP6ServerLseStExceeded,
       "tmnxVRtrDHCP6LseStateOverride": tmnxVRtrDHCP6LseStateOverride,
       "tmnxVRtrDHCP6RelayReplyStripUni": tmnxVRtrDHCP6RelayReplyStripUni,
       "tmnxVRtrDHCP6IllegalClientAddr": tmnxVRtrDHCP6IllegalClientAddr,
       "tmnxVRtrDHCP6AssignedIllegSubnet": tmnxVRtrDHCP6AssignedIllegSubnet,
       "tmnxVRtrDHCP6ClientMacUnresolved": tmnxVRtrDHCP6ClientMacUnresolved,
       "tmnxVRtrBfdSessionUp": tmnxVRtrBfdSessionUp,
       "tmnxVRtrIPv6MidRouteTCA": tmnxVRtrIPv6MidRouteTCA,
       "tmnxVRtrIPv6HighRouteTCA": tmnxVRtrIPv6HighRouteTCA,
       "tmnxVRtrIPv6HighRouteCleared": tmnxVRtrIPv6HighRouteCleared,
       "tmnxVRtrStaticRouteCPEStatus": tmnxVRtrStaticRouteCPEStatus,
       "tmnxVRtrBfdSessionDeleted": tmnxVRtrBfdSessionDeleted,
       "tmnxVRtrBfdSessionProtChange": tmnxVRtrBfdSessionProtChange,
       "tmnxVRtrManagedRouteAddFailed": tmnxVRtrManagedRouteAddFailed}
)
