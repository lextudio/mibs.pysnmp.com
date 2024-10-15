# SNMP MIB module (A3COM-HUAWEI-DHCPRELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DHCPRELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:30 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

h3cDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58)
)
h3cDhcpRelay.setRevisions(
        ("2005-06-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDHCPRMibObject_ObjectIdentity = ObjectIdentity
h3cDHCPRMibObject = _H3cDHCPRMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1)
)
_H3cDHCPRIfSelectTable_Object = MibTable
h3cDHCPRIfSelectTable = _H3cDHCPRIfSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 1)
)
if mibBuilder.loadTexts:
    h3cDHCPRIfSelectTable.setStatus("current")
_H3cDHCPRIfSelectEntry_Object = MibTableRow
h3cDHCPRIfSelectEntry = _H3cDHCPRIfSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 1, 1)
)
h3cDHCPRIfSelectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDHCPRIfSelectEntry.setStatus("current")


class _H3cDHCPRIfSelectRelayMode_Type(Integer32):
    """Custom type h3cDHCPRIfSelectRelayMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_H3cDHCPRIfSelectRelayMode_Type.__name__ = "Integer32"
_H3cDHCPRIfSelectRelayMode_Object = MibTableColumn
h3cDHCPRIfSelectRelayMode = _H3cDHCPRIfSelectRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 1, 1, 1),
    _H3cDHCPRIfSelectRelayMode_Type()
)
h3cDHCPRIfSelectRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPRIfSelectRelayMode.setStatus("current")
_H3cDHCPRIpToGroupTable_Object = MibTable
h3cDHCPRIpToGroupTable = _H3cDHCPRIpToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 2)
)
if mibBuilder.loadTexts:
    h3cDHCPRIpToGroupTable.setStatus("current")
_H3cDHCPRIpToGroupEntry_Object = MibTableRow
h3cDHCPRIpToGroupEntry = _H3cDHCPRIpToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 2, 1)
)
h3cDHCPRIpToGroupEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPRELAY-MIB", "h3cDHCPRIpToGroupGroupId"),
    (0, "A3COM-HUAWEI-DHCPRELAY-MIB", "h3cDHCPRIpToGroupServerIpType"),
    (0, "A3COM-HUAWEI-DHCPRELAY-MIB", "h3cDHCPRIpToGroupServerIp"),
)
if mibBuilder.loadTexts:
    h3cDHCPRIpToGroupEntry.setStatus("current")


class _H3cDHCPRIpToGroupGroupId_Type(Integer32):
    """Custom type h3cDHCPRIpToGroupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_H3cDHCPRIpToGroupGroupId_Type.__name__ = "Integer32"
_H3cDHCPRIpToGroupGroupId_Object = MibTableColumn
h3cDHCPRIpToGroupGroupId = _H3cDHCPRIpToGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 2, 1, 1),
    _H3cDHCPRIpToGroupGroupId_Type()
)
h3cDHCPRIpToGroupGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDHCPRIpToGroupGroupId.setStatus("current")
_H3cDHCPRIpToGroupServerIpType_Type = InetAddressType
_H3cDHCPRIpToGroupServerIpType_Object = MibTableColumn
h3cDHCPRIpToGroupServerIpType = _H3cDHCPRIpToGroupServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 2, 1, 2),
    _H3cDHCPRIpToGroupServerIpType_Type()
)
h3cDHCPRIpToGroupServerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDHCPRIpToGroupServerIpType.setStatus("current")


class _H3cDHCPRIpToGroupServerIp_Type(InetAddress):
    """Custom type h3cDHCPRIpToGroupServerIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDHCPRIpToGroupServerIp_Type.__name__ = "InetAddress"
_H3cDHCPRIpToGroupServerIp_Object = MibTableColumn
h3cDHCPRIpToGroupServerIp = _H3cDHCPRIpToGroupServerIp_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 2, 1, 3),
    _H3cDHCPRIpToGroupServerIp_Type()
)
h3cDHCPRIpToGroupServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDHCPRIpToGroupServerIp.setStatus("current")
_H3cDHCPRIpToGroupRowStatus_Type = RowStatus
_H3cDHCPRIpToGroupRowStatus_Object = MibTableColumn
h3cDHCPRIpToGroupRowStatus = _H3cDHCPRIpToGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 2, 1, 4),
    _H3cDHCPRIpToGroupRowStatus_Type()
)
h3cDHCPRIpToGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPRIpToGroupRowStatus.setStatus("current")
_H3cDHCPRIfToGroupTable_Object = MibTable
h3cDHCPRIfToGroupTable = _H3cDHCPRIfToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 3)
)
if mibBuilder.loadTexts:
    h3cDHCPRIfToGroupTable.setStatus("current")
_H3cDHCPRIfToGroupEntry_Object = MibTableRow
h3cDHCPRIfToGroupEntry = _H3cDHCPRIfToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 3, 1)
)
h3cDHCPRIfToGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDHCPRIfToGroupEntry.setStatus("current")


class _H3cDHCPRIfToGroupGroupId_Type(Integer32):
    """Custom type h3cDHCPRIfToGroupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_H3cDHCPRIfToGroupGroupId_Type.__name__ = "Integer32"
_H3cDHCPRIfToGroupGroupId_Object = MibTableColumn
h3cDHCPRIfToGroupGroupId = _H3cDHCPRIfToGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 3, 1, 1),
    _H3cDHCPRIfToGroupGroupId_Type()
)
h3cDHCPRIfToGroupGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPRIfToGroupGroupId.setStatus("current")
_H3cDHCPRIfToGroupRowStatus_Type = RowStatus
_H3cDHCPRIfToGroupRowStatus_Object = MibTableColumn
h3cDHCPRIfToGroupRowStatus = _H3cDHCPRIfToGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 3, 1, 2),
    _H3cDHCPRIfToGroupRowStatus_Type()
)
h3cDHCPRIfToGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPRIfToGroupRowStatus.setStatus("current")
_H3cDHCPRAddrCheckTable_Object = MibTable
h3cDHCPRAddrCheckTable = _H3cDHCPRAddrCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 4)
)
if mibBuilder.loadTexts:
    h3cDHCPRAddrCheckTable.setStatus("current")
_H3cDHCPRAddrCheckEntry_Object = MibTableRow
h3cDHCPRAddrCheckEntry = _H3cDHCPRAddrCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 4, 1)
)
h3cDHCPRAddrCheckEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDHCPRAddrCheckEntry.setStatus("current")


class _H3cDHCPRAddrCheckSwitch_Type(Integer32):
    """Custom type h3cDHCPRAddrCheckSwitch based on Integer32"""
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


_H3cDHCPRAddrCheckSwitch_Type.__name__ = "Integer32"
_H3cDHCPRAddrCheckSwitch_Object = MibTableColumn
h3cDHCPRAddrCheckSwitch = _H3cDHCPRAddrCheckSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 4, 1, 1),
    _H3cDHCPRAddrCheckSwitch_Type()
)
h3cDHCPRAddrCheckSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPRAddrCheckSwitch.setStatus("current")
_H3cDHCPRSecurityTable_Object = MibTable
h3cDHCPRSecurityTable = _H3cDHCPRSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 5)
)
if mibBuilder.loadTexts:
    h3cDHCPRSecurityTable.setStatus("current")
_H3cDHCPRSecurityEntry_Object = MibTableRow
h3cDHCPRSecurityEntry = _H3cDHCPRSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 5, 1)
)
h3cDHCPRSecurityEntry.setIndexNames(
    (0, "A3COM-HUAWEI-DHCPRELAY-MIB", "h3cDHCPRSecurityClientIpAddrType"),
    (0, "A3COM-HUAWEI-DHCPRELAY-MIB", "h3cDHCPRSecurityClientIpAddr"),
)
if mibBuilder.loadTexts:
    h3cDHCPRSecurityEntry.setStatus("current")
_H3cDHCPRSecurityClientIpAddrType_Type = InetAddressType
_H3cDHCPRSecurityClientIpAddrType_Object = MibTableColumn
h3cDHCPRSecurityClientIpAddrType = _H3cDHCPRSecurityClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 5, 1, 1),
    _H3cDHCPRSecurityClientIpAddrType_Type()
)
h3cDHCPRSecurityClientIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDHCPRSecurityClientIpAddrType.setStatus("current")


class _H3cDHCPRSecurityClientIpAddr_Type(InetAddress):
    """Custom type h3cDHCPRSecurityClientIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_H3cDHCPRSecurityClientIpAddr_Type.__name__ = "InetAddress"
_H3cDHCPRSecurityClientIpAddr_Object = MibTableColumn
h3cDHCPRSecurityClientIpAddr = _H3cDHCPRSecurityClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 5, 1, 2),
    _H3cDHCPRSecurityClientIpAddr_Type()
)
h3cDHCPRSecurityClientIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDHCPRSecurityClientIpAddr.setStatus("current")
_H3cDHCPRSecurityClientMacAddr_Type = MacAddress
_H3cDHCPRSecurityClientMacAddr_Object = MibTableColumn
h3cDHCPRSecurityClientMacAddr = _H3cDHCPRSecurityClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 5, 1, 3),
    _H3cDHCPRSecurityClientMacAddr_Type()
)
h3cDHCPRSecurityClientMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPRSecurityClientMacAddr.setStatus("current")


class _H3cDHCPRSecurityClientProperty_Type(Integer32):
    """Custom type h3cDHCPRSecurityClientProperty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_H3cDHCPRSecurityClientProperty_Type.__name__ = "Integer32"
_H3cDHCPRSecurityClientProperty_Object = MibTableColumn
h3cDHCPRSecurityClientProperty = _H3cDHCPRSecurityClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 5, 1, 4),
    _H3cDHCPRSecurityClientProperty_Type()
)
h3cDHCPRSecurityClientProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPRSecurityClientProperty.setStatus("current")
_H3cDHCPRSecurityClientRowStatus_Type = RowStatus
_H3cDHCPRSecurityClientRowStatus_Object = MibTableColumn
h3cDHCPRSecurityClientRowStatus = _H3cDHCPRSecurityClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 5, 1, 5),
    _H3cDHCPRSecurityClientRowStatus_Type()
)
h3cDHCPRSecurityClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cDHCPRSecurityClientRowStatus.setStatus("current")
_H3cDHCPRStatisticsGroup_ObjectIdentity = ObjectIdentity
h3cDHCPRStatisticsGroup = _H3cDHCPRStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6)
)
_H3cDHCPRRxClientPktNum_Type = Unsigned32
_H3cDHCPRRxClientPktNum_Object = MibScalar
h3cDHCPRRxClientPktNum = _H3cDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 1),
    _H3cDHCPRRxClientPktNum_Type()
)
h3cDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRRxClientPktNum.setStatus("current")
_H3cDHCPRTxClientPktNum_Type = Unsigned32
_H3cDHCPRTxClientPktNum_Object = MibScalar
h3cDHCPRTxClientPktNum = _H3cDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 2),
    _H3cDHCPRTxClientPktNum_Type()
)
h3cDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRTxClientPktNum.setStatus("current")
_H3cDHCPRRxServerPktNum_Type = Unsigned32
_H3cDHCPRRxServerPktNum_Object = MibScalar
h3cDHCPRRxServerPktNum = _H3cDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 3),
    _H3cDHCPRRxServerPktNum_Type()
)
h3cDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRRxServerPktNum.setStatus("current")
_H3cDHCPRTxServerPktNum_Type = Unsigned32
_H3cDHCPRTxServerPktNum_Object = MibScalar
h3cDHCPRTxServerPktNum = _H3cDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 4),
    _H3cDHCPRTxServerPktNum_Type()
)
h3cDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRTxServerPktNum.setStatus("current")
_H3cDHCPRDiscoverPktNum_Type = Unsigned32
_H3cDHCPRDiscoverPktNum_Object = MibScalar
h3cDHCPRDiscoverPktNum = _H3cDHCPRDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 5),
    _H3cDHCPRDiscoverPktNum_Type()
)
h3cDHCPRDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRDiscoverPktNum.setStatus("current")
_H3cDHCPRRequestPktNum_Type = Unsigned32
_H3cDHCPRRequestPktNum_Object = MibScalar
h3cDHCPRRequestPktNum = _H3cDHCPRRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 6),
    _H3cDHCPRRequestPktNum_Type()
)
h3cDHCPRRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRRequestPktNum.setStatus("current")
_H3cDHCPRDeclinePktNum_Type = Unsigned32
_H3cDHCPRDeclinePktNum_Object = MibScalar
h3cDHCPRDeclinePktNum = _H3cDHCPRDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 7),
    _H3cDHCPRDeclinePktNum_Type()
)
h3cDHCPRDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRDeclinePktNum.setStatus("current")
_H3cDHCPRReleasePktNum_Type = Unsigned32
_H3cDHCPRReleasePktNum_Object = MibScalar
h3cDHCPRReleasePktNum = _H3cDHCPRReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 8),
    _H3cDHCPRReleasePktNum_Type()
)
h3cDHCPRReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRReleasePktNum.setStatus("current")
_H3cDHCPRInformPktNum_Type = Unsigned32
_H3cDHCPRInformPktNum_Object = MibScalar
h3cDHCPRInformPktNum = _H3cDHCPRInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 9),
    _H3cDHCPRInformPktNum_Type()
)
h3cDHCPRInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRInformPktNum.setStatus("current")
_H3cDHCPROfferPktNum_Type = Unsigned32
_H3cDHCPROfferPktNum_Object = MibScalar
h3cDHCPROfferPktNum = _H3cDHCPROfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 10),
    _H3cDHCPROfferPktNum_Type()
)
h3cDHCPROfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPROfferPktNum.setStatus("current")
_H3cDHCPRAckPktNum_Type = Unsigned32
_H3cDHCPRAckPktNum_Object = MibScalar
h3cDHCPRAckPktNum = _H3cDHCPRAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 11),
    _H3cDHCPRAckPktNum_Type()
)
h3cDHCPRAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRAckPktNum.setStatus("current")
_H3cDHCPRNakPktNum_Type = Unsigned32
_H3cDHCPRNakPktNum_Object = MibScalar
h3cDHCPRNakPktNum = _H3cDHCPRNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 12),
    _H3cDHCPRNakPktNum_Type()
)
h3cDHCPRNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDHCPRNakPktNum.setStatus("current")
_H3cDHCPRStatisticsReset_Type = TruthValue
_H3cDHCPRStatisticsReset_Object = MibScalar
h3cDHCPRStatisticsReset = _H3cDHCPRStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 6, 13),
    _H3cDHCPRStatisticsReset_Type()
)
h3cDHCPRStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPRStatisticsReset.setStatus("current")
_H3cDHCPRCycleGroup_ObjectIdentity = ObjectIdentity
h3cDHCPRCycleGroup = _H3cDHCPRCycleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 7)
)


class _H3cDHCPRCycleStatus_Type(Integer32):
    """Custom type h3cDHCPRCycleStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_H3cDHCPRCycleStatus_Type.__name__ = "Integer32"
_H3cDHCPRCycleStatus_Object = MibScalar
h3cDHCPRCycleStatus = _H3cDHCPRCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 7, 1),
    _H3cDHCPRCycleStatus_Type()
)
h3cDHCPRCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPRCycleStatus.setStatus("current")
_H3cDHCPRConfigOption82Group_ObjectIdentity = ObjectIdentity
h3cDHCPRConfigOption82Group = _H3cDHCPRConfigOption82Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8)
)


class _H3cDHCPROption82Switch_Type(Integer32):
    """Custom type h3cDHCPROption82Switch based on Integer32"""
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


_H3cDHCPROption82Switch_Type.__name__ = "Integer32"
_H3cDHCPROption82Switch_Object = MibScalar
h3cDHCPROption82Switch = _H3cDHCPROption82Switch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 1),
    _H3cDHCPROption82Switch_Type()
)
h3cDHCPROption82Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPROption82Switch.setStatus("current")


class _H3cDHCPROption82HandleStrategy_Type(Integer32):
    """Custom type h3cDHCPROption82HandleStrategy based on Integer32"""
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
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_H3cDHCPROption82HandleStrategy_Type.__name__ = "Integer32"
_H3cDHCPROption82HandleStrategy_Object = MibScalar
h3cDHCPROption82HandleStrategy = _H3cDHCPROption82HandleStrategy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 2),
    _H3cDHCPROption82HandleStrategy_Type()
)
h3cDHCPROption82HandleStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPROption82HandleStrategy.setStatus("current")
_H3cDHCPRConfigOption82IfTable_Object = MibTable
h3cDHCPRConfigOption82IfTable = _H3cDHCPRConfigOption82IfTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 3)
)
if mibBuilder.loadTexts:
    h3cDHCPRConfigOption82IfTable.setStatus("current")
_H3cDHCPRConfigOption82IfEntry_Object = MibTableRow
h3cDHCPRConfigOption82IfEntry = _H3cDHCPRConfigOption82IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 3, 1)
)
h3cDHCPRConfigOption82IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDHCPRConfigOption82IfEntry.setStatus("current")


class _H3cDHCPROption82IfSwitch_Type(Integer32):
    """Custom type h3cDHCPROption82IfSwitch based on Integer32"""
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


_H3cDHCPROption82IfSwitch_Type.__name__ = "Integer32"
_H3cDHCPROption82IfSwitch_Object = MibTableColumn
h3cDHCPROption82IfSwitch = _H3cDHCPROption82IfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 3, 1, 1),
    _H3cDHCPROption82IfSwitch_Type()
)
h3cDHCPROption82IfSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPROption82IfSwitch.setStatus("current")


class _H3cDHCPROption82IfStrategy_Type(Integer32):
    """Custom type h3cDHCPROption82IfStrategy based on Integer32"""
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
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_H3cDHCPROption82IfStrategy_Type.__name__ = "Integer32"
_H3cDHCPROption82IfStrategy_Object = MibTableColumn
h3cDHCPROption82IfStrategy = _H3cDHCPROption82IfStrategy_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 3, 1, 2),
    _H3cDHCPROption82IfStrategy_Type()
)
h3cDHCPROption82IfStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPROption82IfStrategy.setStatus("current")


class _H3cDHCPROption82IfFormat_Type(Integer32):
    """Custom type h3cDHCPROption82IfFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("verbose", 2))
    )


_H3cDHCPROption82IfFormat_Type.__name__ = "Integer32"
_H3cDHCPROption82IfFormat_Object = MibTableColumn
h3cDHCPROption82IfFormat = _H3cDHCPROption82IfFormat_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 3, 1, 3),
    _H3cDHCPROption82IfFormat_Type()
)
h3cDHCPROption82IfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPROption82IfFormat.setStatus("current")


class _H3cDHCPROption82IfNodeType_Type(Integer32):
    """Custom type h3cDHCPROption82IfNodeType based on Integer32"""
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
        *(("invalid", 1),
          ("mac", 2),
          ("sysname", 3),
          ("userdefine", 4))
    )


_H3cDHCPROption82IfNodeType_Type.__name__ = "Integer32"
_H3cDHCPROption82IfNodeType_Object = MibTableColumn
h3cDHCPROption82IfNodeType = _H3cDHCPROption82IfNodeType_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 3, 1, 4),
    _H3cDHCPROption82IfNodeType_Type()
)
h3cDHCPROption82IfNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPROption82IfNodeType.setStatus("current")


class _H3cDHCPROption82IfUsrDefString_Type(OctetString):
    """Custom type h3cDHCPROption82IfUsrDefString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_H3cDHCPROption82IfUsrDefString_Type.__name__ = "OctetString"
_H3cDHCPROption82IfUsrDefString_Object = MibTableColumn
h3cDHCPROption82IfUsrDefString = _H3cDHCPROption82IfUsrDefString_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 58, 1, 8, 3, 1, 5),
    _H3cDHCPROption82IfUsrDefString_Type()
)
h3cDHCPROption82IfUsrDefString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDHCPROption82IfUsrDefString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DHCPRELAY-MIB",
    **{"h3cDhcpRelay": h3cDhcpRelay,
       "h3cDHCPRMibObject": h3cDHCPRMibObject,
       "h3cDHCPRIfSelectTable": h3cDHCPRIfSelectTable,
       "h3cDHCPRIfSelectEntry": h3cDHCPRIfSelectEntry,
       "h3cDHCPRIfSelectRelayMode": h3cDHCPRIfSelectRelayMode,
       "h3cDHCPRIpToGroupTable": h3cDHCPRIpToGroupTable,
       "h3cDHCPRIpToGroupEntry": h3cDHCPRIpToGroupEntry,
       "h3cDHCPRIpToGroupGroupId": h3cDHCPRIpToGroupGroupId,
       "h3cDHCPRIpToGroupServerIpType": h3cDHCPRIpToGroupServerIpType,
       "h3cDHCPRIpToGroupServerIp": h3cDHCPRIpToGroupServerIp,
       "h3cDHCPRIpToGroupRowStatus": h3cDHCPRIpToGroupRowStatus,
       "h3cDHCPRIfToGroupTable": h3cDHCPRIfToGroupTable,
       "h3cDHCPRIfToGroupEntry": h3cDHCPRIfToGroupEntry,
       "h3cDHCPRIfToGroupGroupId": h3cDHCPRIfToGroupGroupId,
       "h3cDHCPRIfToGroupRowStatus": h3cDHCPRIfToGroupRowStatus,
       "h3cDHCPRAddrCheckTable": h3cDHCPRAddrCheckTable,
       "h3cDHCPRAddrCheckEntry": h3cDHCPRAddrCheckEntry,
       "h3cDHCPRAddrCheckSwitch": h3cDHCPRAddrCheckSwitch,
       "h3cDHCPRSecurityTable": h3cDHCPRSecurityTable,
       "h3cDHCPRSecurityEntry": h3cDHCPRSecurityEntry,
       "h3cDHCPRSecurityClientIpAddrType": h3cDHCPRSecurityClientIpAddrType,
       "h3cDHCPRSecurityClientIpAddr": h3cDHCPRSecurityClientIpAddr,
       "h3cDHCPRSecurityClientMacAddr": h3cDHCPRSecurityClientMacAddr,
       "h3cDHCPRSecurityClientProperty": h3cDHCPRSecurityClientProperty,
       "h3cDHCPRSecurityClientRowStatus": h3cDHCPRSecurityClientRowStatus,
       "h3cDHCPRStatisticsGroup": h3cDHCPRStatisticsGroup,
       "h3cDHCPRRxClientPktNum": h3cDHCPRRxClientPktNum,
       "h3cDHCPRTxClientPktNum": h3cDHCPRTxClientPktNum,
       "h3cDHCPRRxServerPktNum": h3cDHCPRRxServerPktNum,
       "h3cDHCPRTxServerPktNum": h3cDHCPRTxServerPktNum,
       "h3cDHCPRDiscoverPktNum": h3cDHCPRDiscoverPktNum,
       "h3cDHCPRRequestPktNum": h3cDHCPRRequestPktNum,
       "h3cDHCPRDeclinePktNum": h3cDHCPRDeclinePktNum,
       "h3cDHCPRReleasePktNum": h3cDHCPRReleasePktNum,
       "h3cDHCPRInformPktNum": h3cDHCPRInformPktNum,
       "h3cDHCPROfferPktNum": h3cDHCPROfferPktNum,
       "h3cDHCPRAckPktNum": h3cDHCPRAckPktNum,
       "h3cDHCPRNakPktNum": h3cDHCPRNakPktNum,
       "h3cDHCPRStatisticsReset": h3cDHCPRStatisticsReset,
       "h3cDHCPRCycleGroup": h3cDHCPRCycleGroup,
       "h3cDHCPRCycleStatus": h3cDHCPRCycleStatus,
       "h3cDHCPRConfigOption82Group": h3cDHCPRConfigOption82Group,
       "h3cDHCPROption82Switch": h3cDHCPROption82Switch,
       "h3cDHCPROption82HandleStrategy": h3cDHCPROption82HandleStrategy,
       "h3cDHCPRConfigOption82IfTable": h3cDHCPRConfigOption82IfTable,
       "h3cDHCPRConfigOption82IfEntry": h3cDHCPRConfigOption82IfEntry,
       "h3cDHCPROption82IfSwitch": h3cDHCPROption82IfSwitch,
       "h3cDHCPROption82IfStrategy": h3cDHCPROption82IfStrategy,
       "h3cDHCPROption82IfFormat": h3cDHCPROption82IfFormat,
       "h3cDHCPROption82IfNodeType": h3cDHCPROption82IfNodeType,
       "h3cDHCPROption82IfUsrDefString": h3cDHCPROption82IfUsrDefString}
)
