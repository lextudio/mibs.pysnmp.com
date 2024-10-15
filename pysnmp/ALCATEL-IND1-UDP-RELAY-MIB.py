# SNMP MIB module (ALCATEL-IND1-UDP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-UDP-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:30 2024
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

(routingIND1UdpRelay,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1UdpRelay")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

alcatelIND1UDPRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1)
)
alcatelIND1UDPRelayMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IphelpereOption82ASCIIFieldType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("interface", 6),
          ("interfaceAlias", 4),
          ("macAddress", 1),
          ("none", 0),
          ("systemName", 2),
          ("userString", 3),
          ("vlan", 5))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1UDPRelayNotificationObjects_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayNotificationObjects = _AlcatelIND1UDPRelayNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayNotificationObjects.setStatus("current")
_AlcatelIND1UDPRelayMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBObjects = _AlcatelIND1UDPRelayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBObjects.setStatus("current")
_IphelperMIB_ObjectIdentity = ObjectIdentity
iphelperMIB = _IphelperMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1)
)
_IphelperTable_Object = MibTable
iphelperTable = _IphelperTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iphelperTable.setStatus("current")
_IphelperEntry_Object = MibTableRow
iphelperEntry = _IphelperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1)
)
iphelperEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperVlan"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperNextHopIpAddress"),
)
if mibBuilder.loadTexts:
    iphelperEntry.setStatus("current")
_IphelperVlan_Type = Unsigned32
_IphelperVlan_Object = MibTableColumn
iphelperVlan = _IphelperVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 1),
    _IphelperVlan_Type()
)
iphelperVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperVlan.setStatus("current")
_IphelperNextHopIpAddress_Type = IpAddress
_IphelperNextHopIpAddress_Object = MibTableColumn
iphelperNextHopIpAddress = _IphelperNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 2),
    _IphelperNextHopIpAddress_Type()
)
iphelperNextHopIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperNextHopIpAddress.setStatus("current")
_IphelperResetSrvStats_Type = Unsigned32
_IphelperResetSrvStats_Object = MibTableColumn
iphelperResetSrvStats = _IphelperResetSrvStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 3),
    _IphelperResetSrvStats_Type()
)
iphelperResetSrvStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperResetSrvStats.setStatus("current")
_IphelperRowStatus_Type = RowStatus
_IphelperRowStatus_Object = MibTableColumn
iphelperRowStatus = _IphelperRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 1, 1, 4),
    _IphelperRowStatus_Type()
)
iphelperRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iphelperRowStatus.setStatus("current")
_IphelperStatTable_Object = MibTable
iphelperStatTable = _IphelperStatTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    iphelperStatTable.setStatus("current")
_IphelperStatEntry_Object = MibTableRow
iphelperStatEntry = _IphelperStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1)
)
iphelperStatEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperStatsVlan"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperStatsNextHopIpAddr"),
)
if mibBuilder.loadTexts:
    iphelperStatEntry.setStatus("current")
_IphelperStatsVlan_Type = Unsigned32
_IphelperStatsVlan_Object = MibTableColumn
iphelperStatsVlan = _IphelperStatsVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 1),
    _IphelperStatsVlan_Type()
)
iphelperStatsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperStatsVlan.setStatus("current")
_IphelperStatsNextHopIpAddr_Type = IpAddress
_IphelperStatsNextHopIpAddr_Object = MibTableColumn
iphelperStatsNextHopIpAddr = _IphelperStatsNextHopIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 2),
    _IphelperStatsNextHopIpAddr_Type()
)
iphelperStatsNextHopIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperStatsNextHopIpAddr.setStatus("current")
_IphelperTxToNextHop_Type = Counter32
_IphelperTxToNextHop_Object = MibTableColumn
iphelperTxToNextHop = _IphelperTxToNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 3),
    _IphelperTxToNextHop_Type()
)
iphelperTxToNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperTxToNextHop.setStatus("current")
_IphelperInvalidAgentInfoOptFrmSrver_Type = Counter32
_IphelperInvalidAgentInfoOptFrmSrver_Object = MibTableColumn
iphelperInvalidAgentInfoOptFrmSrver = _IphelperInvalidAgentInfoOptFrmSrver_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 2, 1, 4),
    _IphelperInvalidAgentInfoOptFrmSrver_Type()
)
iphelperInvalidAgentInfoOptFrmSrver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperInvalidAgentInfoOptFrmSrver.setStatus("current")
_IphelperRxFromClient_Type = Counter32
_IphelperRxFromClient_Object = MibScalar
iphelperRxFromClient = _IphelperRxFromClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 3),
    _IphelperRxFromClient_Type()
)
iphelperRxFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperRxFromClient.setStatus("current")
_IphelperMaxHopsViolation_Type = Counter32
_IphelperMaxHopsViolation_Object = MibScalar
iphelperMaxHopsViolation = _IphelperMaxHopsViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 4),
    _IphelperMaxHopsViolation_Type()
)
iphelperMaxHopsViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperMaxHopsViolation.setStatus("current")
_IphelperForwDelayViolation_Type = Counter32
_IphelperForwDelayViolation_Object = MibScalar
iphelperForwDelayViolation = _IphelperForwDelayViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 5),
    _IphelperForwDelayViolation_Type()
)
iphelperForwDelayViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperForwDelayViolation.setStatus("current")
_IphelperAgentInfoViolation_Type = Counter32
_IphelperAgentInfoViolation_Object = MibScalar
iphelperAgentInfoViolation = _IphelperAgentInfoViolation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 6),
    _IphelperAgentInfoViolation_Type()
)
iphelperAgentInfoViolation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperAgentInfoViolation.setStatus("current")
_IphelperInvalidGatewayIP_Type = Counter32
_IphelperInvalidGatewayIP_Object = MibScalar
iphelperInvalidGatewayIP = _IphelperInvalidGatewayIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 7),
    _IphelperInvalidGatewayIP_Type()
)
iphelperInvalidGatewayIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperInvalidGatewayIP.setStatus("current")


class _IphelperForwDelay_Type(Unsigned32):
    """Custom type iphelperForwDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IphelperForwDelay_Type.__name__ = "Unsigned32"
_IphelperForwDelay_Object = MibScalar
iphelperForwDelay = _IphelperForwDelay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 8),
    _IphelperForwDelay_Type()
)
iphelperForwDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperForwDelay.setStatus("current")


class _IphelperMaxHops_Type(Integer32):
    """Custom type iphelperMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IphelperMaxHops_Type.__name__ = "Integer32"
_IphelperMaxHops_Object = MibScalar
iphelperMaxHops = _IphelperMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 9),
    _IphelperMaxHops_Type()
)
iphelperMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperMaxHops.setStatus("current")


class _IphelperForwardOption_Type(Integer32):
    """Custom type iphelperForwardOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("perVlan", 2),
          ("standard", 1))
    )


_IphelperForwardOption_Type.__name__ = "Integer32"
_IphelperForwardOption_Object = MibScalar
iphelperForwardOption = _IphelperForwardOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 10),
    _IphelperForwardOption_Type()
)
iphelperForwardOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperForwardOption.setStatus("current")


class _IphelperResetAllStats_Type(Integer32):
    """Custom type iphelperResetAllStats based on Integer32"""
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
        *(("noOperation", 0),
          ("resetAllGlbStats", 2),
          ("resetAllSrvStats", 3),
          ("resetAllStats", 1))
    )


_IphelperResetAllStats_Type.__name__ = "Integer32"
_IphelperResetAllStats_Object = MibScalar
iphelperResetAllStats = _IphelperResetAllStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 11),
    _IphelperResetAllStats_Type()
)
iphelperResetAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperResetAllStats.setStatus("current")


class _IphelperBootupOption_Type(Integer32):
    """Custom type iphelperBootupOption based on Integer32"""
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


_IphelperBootupOption_Type.__name__ = "Integer32"
_IphelperBootupOption_Object = MibScalar
iphelperBootupOption = _IphelperBootupOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 12),
    _IphelperBootupOption_Type()
)
iphelperBootupOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperBootupOption.setStatus("current")


class _IphelperBootupPacketOption_Type(Integer32):
    """Custom type iphelperBootupPacketOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 1),
          ("dhcp", 2))
    )


_IphelperBootupPacketOption_Type.__name__ = "Integer32"
_IphelperBootupPacketOption_Object = MibScalar
iphelperBootupPacketOption = _IphelperBootupPacketOption_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 13),
    _IphelperBootupPacketOption_Type()
)
iphelperBootupPacketOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperBootupPacketOption.setStatus("current")


class _IphelperAgentInformation_Type(Integer32):
    """Custom type iphelperAgentInformation based on Integer32"""
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


_IphelperAgentInformation_Type.__name__ = "Integer32"
_IphelperAgentInformation_Object = MibScalar
iphelperAgentInformation = _IphelperAgentInformation_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 14),
    _IphelperAgentInformation_Type()
)
iphelperAgentInformation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperAgentInformation.setStatus("current")


class _IphelperAgentInformationPolicy_Type(Integer32):
    """Custom type iphelperAgentInformationPolicy based on Integer32"""
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
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_IphelperAgentInformationPolicy_Type.__name__ = "Integer32"
_IphelperAgentInformationPolicy_Object = MibScalar
iphelperAgentInformationPolicy = _IphelperAgentInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 15),
    _IphelperAgentInformationPolicy_Type()
)
iphelperAgentInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperAgentInformationPolicy.setStatus("current")


class _IphelperPXESupport_Type(Integer32):
    """Custom type iphelperPXESupport based on Integer32"""
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


_IphelperPXESupport_Type.__name__ = "Integer32"
_IphelperPXESupport_Object = MibScalar
iphelperPXESupport = _IphelperPXESupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 16),
    _IphelperPXESupport_Type()
)
iphelperPXESupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperPXESupport.setStatus("current")


class _IphelperDhcpOption82FormatType_Type(Integer32):
    """Custom type iphelperDhcpOption82FormatType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 6),
          ("autoInterfaceAlias", 5),
          ("interfaceAlias", 4),
          ("macAddress", 1),
          ("systemName", 2),
          ("userString", 3))
    )


_IphelperDhcpOption82FormatType_Type.__name__ = "Integer32"
_IphelperDhcpOption82FormatType_Object = MibScalar
iphelperDhcpOption82FormatType = _IphelperDhcpOption82FormatType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 17),
    _IphelperDhcpOption82FormatType_Type()
)
iphelperDhcpOption82FormatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatType.setStatus("current")


class _IphelperDhcpOption82StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82StringValue_Object = MibScalar
iphelperDhcpOption82StringValue = _IphelperDhcpOption82StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 18),
    _IphelperDhcpOption82StringValue_Type()
)
iphelperDhcpOption82StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField1_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField1 based on IphelpereOption82ASCIIFieldType"""


_IphelperDhcpOption82FormatASCIIField1_Object = MibScalar
iphelperDhcpOption82FormatASCIIField1 = _IphelperDhcpOption82FormatASCIIField1_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 19),
    _IphelperDhcpOption82FormatASCIIField1_Type()
)
iphelperDhcpOption82FormatASCIIField1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField1.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField1StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField1StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField1StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField1StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField1StringValue = _IphelperDhcpOption82FormatASCIIField1StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 20),
    _IphelperDhcpOption82FormatASCIIField1StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField1StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField1StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField2_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField2 based on IphelpereOption82ASCIIFieldType"""


_IphelperDhcpOption82FormatASCIIField2_Object = MibScalar
iphelperDhcpOption82FormatASCIIField2 = _IphelperDhcpOption82FormatASCIIField2_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 21),
    _IphelperDhcpOption82FormatASCIIField2_Type()
)
iphelperDhcpOption82FormatASCIIField2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField2.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField2StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField2StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField2StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField2StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField2StringValue = _IphelperDhcpOption82FormatASCIIField2StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 22),
    _IphelperDhcpOption82FormatASCIIField2StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField2StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField2StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField3_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField3 based on IphelpereOption82ASCIIFieldType"""


_IphelperDhcpOption82FormatASCIIField3_Object = MibScalar
iphelperDhcpOption82FormatASCIIField3 = _IphelperDhcpOption82FormatASCIIField3_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 23),
    _IphelperDhcpOption82FormatASCIIField3_Type()
)
iphelperDhcpOption82FormatASCIIField3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField3.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField3StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField3StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField3StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField3StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField3StringValue = _IphelperDhcpOption82FormatASCIIField3StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 24),
    _IphelperDhcpOption82FormatASCIIField3StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField3StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField3StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField4_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField4 based on IphelpereOption82ASCIIFieldType"""


_IphelperDhcpOption82FormatASCIIField4_Object = MibScalar
iphelperDhcpOption82FormatASCIIField4 = _IphelperDhcpOption82FormatASCIIField4_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 25),
    _IphelperDhcpOption82FormatASCIIField4_Type()
)
iphelperDhcpOption82FormatASCIIField4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField4.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField4StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField4StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField4StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField4StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField4StringValue = _IphelperDhcpOption82FormatASCIIField4StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 26),
    _IphelperDhcpOption82FormatASCIIField4StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField4StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField4StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField5_Type(IphelpereOption82ASCIIFieldType):
    """Custom type iphelperDhcpOption82FormatASCIIField5 based on IphelpereOption82ASCIIFieldType"""


_IphelperDhcpOption82FormatASCIIField5_Object = MibScalar
iphelperDhcpOption82FormatASCIIField5 = _IphelperDhcpOption82FormatASCIIField5_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 27),
    _IphelperDhcpOption82FormatASCIIField5_Type()
)
iphelperDhcpOption82FormatASCIIField5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField5.setStatus("current")


class _IphelperDhcpOption82FormatASCIIField5StringValue_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIField5StringValue based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIField5StringValue_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIField5StringValue_Object = MibScalar
iphelperDhcpOption82FormatASCIIField5StringValue = _IphelperDhcpOption82FormatASCIIField5StringValue_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 28),
    _IphelperDhcpOption82FormatASCIIField5StringValue_Type()
)
iphelperDhcpOption82FormatASCIIField5StringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIField5StringValue.setStatus("current")


class _IphelperDhcpOption82FormatASCIIDelimiter_Type(SnmpAdminString):
    """Custom type iphelperDhcpOption82FormatASCIIDelimiter based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IphelperDhcpOption82FormatASCIIDelimiter_Type.__name__ = "SnmpAdminString"
_IphelperDhcpOption82FormatASCIIDelimiter_Object = MibScalar
iphelperDhcpOption82FormatASCIIDelimiter = _IphelperDhcpOption82FormatASCIIDelimiter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 29),
    _IphelperDhcpOption82FormatASCIIDelimiter_Type()
)
iphelperDhcpOption82FormatASCIIDelimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperDhcpOption82FormatASCIIDelimiter.setStatus("current")


class _IphelperResetAllOpt82ErrStats_Type(Integer32):
    """Custom type iphelperResetAllOpt82ErrStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("resetAllStats", 1))
    )


_IphelperResetAllOpt82ErrStats_Type.__name__ = "Integer32"
_IphelperResetAllOpt82ErrStats_Object = MibScalar
iphelperResetAllOpt82ErrStats = _IphelperResetAllOpt82ErrStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 30),
    _IphelperResetAllOpt82ErrStats_Type()
)
iphelperResetAllOpt82ErrStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperResetAllOpt82ErrStats.setStatus("current")
_IphelperOption82ErrStatsTable_Object = MibTable
iphelperOption82ErrStatsTable = _IphelperOption82ErrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31)
)
if mibBuilder.loadTexts:
    iphelperOption82ErrStatsTable.setStatus("current")
_IphelperOption82ErrStatsEntry_Object = MibTableRow
iphelperOption82ErrStatsEntry = _IphelperOption82ErrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1)
)
iphelperOption82ErrStatsEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperOpt82ifIndex"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "iphelperOpt82vlan"),
)
if mibBuilder.loadTexts:
    iphelperOption82ErrStatsEntry.setStatus("current")
_IphelperOpt82ifIndex_Type = InterfaceIndex
_IphelperOpt82ifIndex_Object = MibTableColumn
iphelperOpt82ifIndex = _IphelperOpt82ifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 1),
    _IphelperOpt82ifIndex_Type()
)
iphelperOpt82ifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperOpt82ifIndex.setStatus("current")
_IphelperOpt82vlan_Type = Unsigned32
_IphelperOpt82vlan_Object = MibTableColumn
iphelperOpt82vlan = _IphelperOpt82vlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 2),
    _IphelperOpt82vlan_Type()
)
iphelperOpt82vlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iphelperOpt82vlan.setStatus("current")
_IphelperOpt82agentInfoViolationCnt_Type = Counter32
_IphelperOpt82agentInfoViolationCnt_Object = MibTableColumn
iphelperOpt82agentInfoViolationCnt = _IphelperOpt82agentInfoViolationCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 3),
    _IphelperOpt82agentInfoViolationCnt_Type()
)
iphelperOpt82agentInfoViolationCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperOpt82agentInfoViolationCnt.setStatus("current")
_IphelperOpt82invalidGatewayIPAddrCnt_Type = Counter32
_IphelperOpt82invalidGatewayIPAddrCnt_Object = MibTableColumn
iphelperOpt82invalidGatewayIPAddrCnt = _IphelperOpt82invalidGatewayIPAddrCnt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 4),
    _IphelperOpt82invalidGatewayIPAddrCnt_Type()
)
iphelperOpt82invalidGatewayIPAddrCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphelperOpt82invalidGatewayIPAddrCnt.setStatus("current")


class _IphelperOpt82resetErrStats_Type(Integer32):
    """Custom type iphelperOpt82resetErrStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("resetErrStats", 1))
    )


_IphelperOpt82resetErrStats_Type.__name__ = "Integer32"
_IphelperOpt82resetErrStats_Object = MibTableColumn
iphelperOpt82resetErrStats = _IphelperOpt82resetErrStats_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 1, 31, 1, 5),
    _IphelperOpt82resetErrStats_Type()
)
iphelperOpt82resetErrStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphelperOpt82resetErrStats.setStatus("current")
_GenericUdpServiceMIB_ObjectIdentity = ObjectIdentity
genericUdpServiceMIB = _GenericUdpServiceMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2)
)
_GenericUdpServiceTable_Object = MibTable
genericUdpServiceTable = _GenericUdpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    genericUdpServiceTable.setStatus("current")
_GenericUdpServiceEntry_Object = MibTableRow
genericUdpServiceEntry = _GenericUdpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1)
)
genericUdpServiceEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceUdpPort"),
)
if mibBuilder.loadTexts:
    genericUdpServiceEntry.setStatus("current")


class _GenericUdpServiceUdpPort_Type(Unsigned32):
    """Custom type genericUdpServiceUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GenericUdpServiceUdpPort_Type.__name__ = "Unsigned32"
_GenericUdpServiceUdpPort_Object = MibTableColumn
genericUdpServiceUdpPort = _GenericUdpServiceUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 1),
    _GenericUdpServiceUdpPort_Type()
)
genericUdpServiceUdpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genericUdpServiceUdpPort.setStatus("current")


class _GenericUdpServiceDescription_Type(SnmpAdminString):
    """Custom type genericUdpServiceDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_GenericUdpServiceDescription_Type.__name__ = "SnmpAdminString"
_GenericUdpServiceDescription_Object = MibTableColumn
genericUdpServiceDescription = _GenericUdpServiceDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 2),
    _GenericUdpServiceDescription_Type()
)
genericUdpServiceDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genericUdpServiceDescription.setStatus("current")
_GenericUdpServiceStatRxFromClient_Type = Counter32
_GenericUdpServiceStatRxFromClient_Object = MibTableColumn
genericUdpServiceStatRxFromClient = _GenericUdpServiceStatRxFromClient_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 3),
    _GenericUdpServiceStatRxFromClient_Type()
)
genericUdpServiceStatRxFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericUdpServiceStatRxFromClient.setStatus("current")
_GenericUdpServiceRowStatus_Type = RowStatus
_GenericUdpServiceRowStatus_Object = MibTableColumn
genericUdpServiceRowStatus = _GenericUdpServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 1, 1, 4),
    _GenericUdpServiceRowStatus_Type()
)
genericUdpServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genericUdpServiceRowStatus.setStatus("current")
_GenericUdpServiceDstTable_Object = MibTable
genericUdpServiceDstTable = _GenericUdpServiceDstTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    genericUdpServiceDstTable.setStatus("current")
_GenericUdpServiceDstEntry_Object = MibTableRow
genericUdpServiceDstEntry = _GenericUdpServiceDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1)
)
genericUdpServiceDstEntry.setIndexNames(
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServicePort"),
    (0, "ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceDstVlan"),
)
if mibBuilder.loadTexts:
    genericUdpServiceDstEntry.setStatus("current")


class _GenericUdpServicePort_Type(Unsigned32):
    """Custom type genericUdpServicePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_GenericUdpServicePort_Type.__name__ = "Unsigned32"
_GenericUdpServicePort_Object = MibTableColumn
genericUdpServicePort = _GenericUdpServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 1),
    _GenericUdpServicePort_Type()
)
genericUdpServicePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genericUdpServicePort.setStatus("current")


class _GenericUdpServiceDstVlan_Type(Unsigned32):
    """Custom type genericUdpServiceDstVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_GenericUdpServiceDstVlan_Type.__name__ = "Unsigned32"
_GenericUdpServiceDstVlan_Object = MibTableColumn
genericUdpServiceDstVlan = _GenericUdpServiceDstVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 2),
    _GenericUdpServiceDstVlan_Type()
)
genericUdpServiceDstVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    genericUdpServiceDstVlan.setStatus("current")
_GenericUdpServiceStatTxToVlan_Type = Counter32
_GenericUdpServiceStatTxToVlan_Object = MibTableColumn
genericUdpServiceStatTxToVlan = _GenericUdpServiceStatTxToVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 3),
    _GenericUdpServiceStatTxToVlan_Type()
)
genericUdpServiceStatTxToVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genericUdpServiceStatTxToVlan.setStatus("current")
_GenericUdpServiceDstTblRowStatus_Type = RowStatus
_GenericUdpServiceDstTblRowStatus_Object = MibTableColumn
genericUdpServiceDstTblRowStatus = _GenericUdpServiceDstTblRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 2, 1, 4),
    _GenericUdpServiceDstTblRowStatus_Type()
)
genericUdpServiceDstTblRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    genericUdpServiceDstTblRowStatus.setStatus("current")


class _GenericUdpServiceStatReset_Type(Integer32):
    """Custom type genericUdpServiceStatReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("resetAllStats", 1))
    )


_GenericUdpServiceStatReset_Type.__name__ = "Integer32"
_GenericUdpServiceStatReset_Object = MibScalar
genericUdpServiceStatReset = _GenericUdpServiceStatReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 2, 3),
    _GenericUdpServiceStatReset_Type()
)
genericUdpServiceStatReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genericUdpServiceStatReset.setStatus("current")
_AlaDhcpClientTrapsObj_ObjectIdentity = ObjectIdentity
alaDhcpClientTrapsObj = _AlaDhcpClientTrapsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 3)
)
_AlaDhcpClientAddress_Type = IpAddress
_AlaDhcpClientAddress_Object = MibScalar
alaDhcpClientAddress = _AlaDhcpClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 3, 1),
    _AlaDhcpClientAddress_Type()
)
alaDhcpClientAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpClientAddress.setStatus("current")
_AlaDhcpClientNewAddress_Type = IpAddress
_AlaDhcpClientNewAddress_Object = MibScalar
alaDhcpClientNewAddress = _AlaDhcpClientNewAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 1, 3, 2),
    _AlaDhcpClientNewAddress_Type()
)
alaDhcpClientNewAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDhcpClientNewAddress.setStatus("current")
_AlcatelIND1UDPRelayMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBConformance = _AlcatelIND1UDPRelayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBConformance.setStatus("current")
_AlcatelIND1UDPRelayMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBGroups = _AlcatelIND1UDPRelayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBGroups.setStatus("current")
_AlcatelIND1UDPRelayMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1UDPRelayMIBCompliances = _AlcatelIND1UDPRelayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBCompliances.setStatus("current")

# Managed Objects groups

iphelperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 1)
)
iphelperGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperResetSrvStats"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperRowStatus"))
)
if mibBuilder.loadTexts:
    iphelperGroup.setStatus("current")

iphelperStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 2)
)
iphelperStatGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperTxToNextHop"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperInvalidAgentInfoOptFrmSrver"))
)
if mibBuilder.loadTexts:
    iphelperStatGroup.setStatus("current")

iphelperMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 3)
)
iphelperMiscGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperRxFromClient"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperMaxHopsViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwDelayViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperAgentInfoViolation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperInvalidGatewayIP"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwDelay"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperMaxHops"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperForwardOption"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperResetAllStats"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperBootupOption"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperBootupPacketOption"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperAgentInformation"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperAgentInformationPolicy"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperPXESupport"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatType"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField1"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField1StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField2"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField2StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField3"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField3StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField4"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField4StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField5"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIField5StringValue"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperDhcpOption82FormatASCIIDelimiter"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperResetAllOpt82ErrStats"))
)
if mibBuilder.loadTexts:
    iphelperMiscGroup.setStatus("current")

genericUdpServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 4)
)
genericUdpServiceGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceDescription"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceStatRxFromClient"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceRowStatus"))
)
if mibBuilder.loadTexts:
    genericUdpServiceGroup.setStatus("current")

genericUdpServiceDstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 5)
)
genericUdpServiceDstGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceStatTxToVlan"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceDstTblRowStatus"))
)
if mibBuilder.loadTexts:
    genericUdpServiceDstGroup.setStatus("current")

genericUdpServiceMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 6)
)
genericUdpServiceMiscGroup.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "genericUdpServiceStatReset")
)
if mibBuilder.loadTexts:
    genericUdpServiceMiscGroup.setStatus("current")

alaDhcpClientTrapsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 8)
)
alaDhcpClientTrapsObjectGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientNewAddress"))
)
if mibBuilder.loadTexts:
    alaDhcpClientTrapsObjectGroup.setStatus("current")

iphelperOpt82ErrorStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 9)
)
iphelperOpt82ErrorStatGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperOpt82agentInfoViolationCnt"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperOpt82invalidGatewayIPAddrCnt"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "iphelperOpt82resetErrStats"))
)
if mibBuilder.loadTexts:
    iphelperOpt82ErrorStatGroup.setStatus("current")


# Notification objects

alaDhcpClientAddressAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0, 1)
)
alaDhcpClientAddressAddTrap.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress")
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressAddTrap.setStatus(
        "current"
    )

alaDhcpClientAddressExpiryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0, 2)
)
alaDhcpClientAddressExpiryTrap.setObjects(
    ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress")
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressExpiryTrap.setStatus(
        "current"
    )

alaDhcpClientAddressModifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 0, 3)
)
alaDhcpClientAddressModifyTrap.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddress"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientNewAddress"))
)
if mibBuilder.loadTexts:
    alaDhcpClientAddressModifyTrap.setStatus(
        "current"
    )


# Notifications groups

alaDhcpClientTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 1, 7)
)
alaDhcpClientTrapsGroup.setObjects(
      *(("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddressAddTrap"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddressExpiryTrap"),
        ("ALCATEL-IND1-UDP-RELAY-MIB", "alaDhcpClientAddressModifyTrap"))
)
if mibBuilder.loadTexts:
    alaDhcpClientTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alcatelIND1UDPRelayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 9, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1UDPRelayMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-UDP-RELAY-MIB",
    **{"IphelpereOption82ASCIIFieldType": IphelpereOption82ASCIIFieldType,
       "alcatelIND1UDPRelayMIB": alcatelIND1UDPRelayMIB,
       "alcatelIND1UDPRelayNotificationObjects": alcatelIND1UDPRelayNotificationObjects,
       "alaDhcpClientAddressAddTrap": alaDhcpClientAddressAddTrap,
       "alaDhcpClientAddressExpiryTrap": alaDhcpClientAddressExpiryTrap,
       "alaDhcpClientAddressModifyTrap": alaDhcpClientAddressModifyTrap,
       "alcatelIND1UDPRelayMIBObjects": alcatelIND1UDPRelayMIBObjects,
       "iphelperMIB": iphelperMIB,
       "iphelperTable": iphelperTable,
       "iphelperEntry": iphelperEntry,
       "iphelperVlan": iphelperVlan,
       "iphelperNextHopIpAddress": iphelperNextHopIpAddress,
       "iphelperResetSrvStats": iphelperResetSrvStats,
       "iphelperRowStatus": iphelperRowStatus,
       "iphelperStatTable": iphelperStatTable,
       "iphelperStatEntry": iphelperStatEntry,
       "iphelperStatsVlan": iphelperStatsVlan,
       "iphelperStatsNextHopIpAddr": iphelperStatsNextHopIpAddr,
       "iphelperTxToNextHop": iphelperTxToNextHop,
       "iphelperInvalidAgentInfoOptFrmSrver": iphelperInvalidAgentInfoOptFrmSrver,
       "iphelperRxFromClient": iphelperRxFromClient,
       "iphelperMaxHopsViolation": iphelperMaxHopsViolation,
       "iphelperForwDelayViolation": iphelperForwDelayViolation,
       "iphelperAgentInfoViolation": iphelperAgentInfoViolation,
       "iphelperInvalidGatewayIP": iphelperInvalidGatewayIP,
       "iphelperForwDelay": iphelperForwDelay,
       "iphelperMaxHops": iphelperMaxHops,
       "iphelperForwardOption": iphelperForwardOption,
       "iphelperResetAllStats": iphelperResetAllStats,
       "iphelperBootupOption": iphelperBootupOption,
       "iphelperBootupPacketOption": iphelperBootupPacketOption,
       "iphelperAgentInformation": iphelperAgentInformation,
       "iphelperAgentInformationPolicy": iphelperAgentInformationPolicy,
       "iphelperPXESupport": iphelperPXESupport,
       "iphelperDhcpOption82FormatType": iphelperDhcpOption82FormatType,
       "iphelperDhcpOption82StringValue": iphelperDhcpOption82StringValue,
       "iphelperDhcpOption82FormatASCIIField1": iphelperDhcpOption82FormatASCIIField1,
       "iphelperDhcpOption82FormatASCIIField1StringValue": iphelperDhcpOption82FormatASCIIField1StringValue,
       "iphelperDhcpOption82FormatASCIIField2": iphelperDhcpOption82FormatASCIIField2,
       "iphelperDhcpOption82FormatASCIIField2StringValue": iphelperDhcpOption82FormatASCIIField2StringValue,
       "iphelperDhcpOption82FormatASCIIField3": iphelperDhcpOption82FormatASCIIField3,
       "iphelperDhcpOption82FormatASCIIField3StringValue": iphelperDhcpOption82FormatASCIIField3StringValue,
       "iphelperDhcpOption82FormatASCIIField4": iphelperDhcpOption82FormatASCIIField4,
       "iphelperDhcpOption82FormatASCIIField4StringValue": iphelperDhcpOption82FormatASCIIField4StringValue,
       "iphelperDhcpOption82FormatASCIIField5": iphelperDhcpOption82FormatASCIIField5,
       "iphelperDhcpOption82FormatASCIIField5StringValue": iphelperDhcpOption82FormatASCIIField5StringValue,
       "iphelperDhcpOption82FormatASCIIDelimiter": iphelperDhcpOption82FormatASCIIDelimiter,
       "iphelperResetAllOpt82ErrStats": iphelperResetAllOpt82ErrStats,
       "iphelperOption82ErrStatsTable": iphelperOption82ErrStatsTable,
       "iphelperOption82ErrStatsEntry": iphelperOption82ErrStatsEntry,
       "iphelperOpt82ifIndex": iphelperOpt82ifIndex,
       "iphelperOpt82vlan": iphelperOpt82vlan,
       "iphelperOpt82agentInfoViolationCnt": iphelperOpt82agentInfoViolationCnt,
       "iphelperOpt82invalidGatewayIPAddrCnt": iphelperOpt82invalidGatewayIPAddrCnt,
       "iphelperOpt82resetErrStats": iphelperOpt82resetErrStats,
       "genericUdpServiceMIB": genericUdpServiceMIB,
       "genericUdpServiceTable": genericUdpServiceTable,
       "genericUdpServiceEntry": genericUdpServiceEntry,
       "genericUdpServiceUdpPort": genericUdpServiceUdpPort,
       "genericUdpServiceDescription": genericUdpServiceDescription,
       "genericUdpServiceStatRxFromClient": genericUdpServiceStatRxFromClient,
       "genericUdpServiceRowStatus": genericUdpServiceRowStatus,
       "genericUdpServiceDstTable": genericUdpServiceDstTable,
       "genericUdpServiceDstEntry": genericUdpServiceDstEntry,
       "genericUdpServicePort": genericUdpServicePort,
       "genericUdpServiceDstVlan": genericUdpServiceDstVlan,
       "genericUdpServiceStatTxToVlan": genericUdpServiceStatTxToVlan,
       "genericUdpServiceDstTblRowStatus": genericUdpServiceDstTblRowStatus,
       "genericUdpServiceStatReset": genericUdpServiceStatReset,
       "alaDhcpClientTrapsObj": alaDhcpClientTrapsObj,
       "alaDhcpClientAddress": alaDhcpClientAddress,
       "alaDhcpClientNewAddress": alaDhcpClientNewAddress,
       "alcatelIND1UDPRelayMIBConformance": alcatelIND1UDPRelayMIBConformance,
       "alcatelIND1UDPRelayMIBGroups": alcatelIND1UDPRelayMIBGroups,
       "iphelperGroup": iphelperGroup,
       "iphelperStatGroup": iphelperStatGroup,
       "iphelperMiscGroup": iphelperMiscGroup,
       "genericUdpServiceGroup": genericUdpServiceGroup,
       "genericUdpServiceDstGroup": genericUdpServiceDstGroup,
       "genericUdpServiceMiscGroup": genericUdpServiceMiscGroup,
       "alaDhcpClientTrapsGroup": alaDhcpClientTrapsGroup,
       "alaDhcpClientTrapsObjectGroup": alaDhcpClientTrapsObjectGroup,
       "iphelperOpt82ErrorStatGroup": iphelperOpt82ErrorStatGroup,
       "alcatelIND1UDPRelayMIBCompliances": alcatelIND1UDPRelayMIBCompliances,
       "alcatelIND1UDPRelayMIBCompliance": alcatelIND1UDPRelayMIBCompliance}
)
