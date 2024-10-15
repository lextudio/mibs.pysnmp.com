# SNMP MIB module (HH3C-DHCPRELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-DHCPRELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:42 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58)
)
hh3cDhcpRelay.setRevisions(
        ("2005-06-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cDHCPRMibObject_ObjectIdentity = ObjectIdentity
hh3cDHCPRMibObject = _Hh3cDHCPRMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1)
)
_Hh3cDHCPRIfSelectTable_Object = MibTable
hh3cDHCPRIfSelectTable = _Hh3cDHCPRIfSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cDHCPRIfSelectTable.setStatus("current")
_Hh3cDHCPRIfSelectEntry_Object = MibTableRow
hh3cDHCPRIfSelectEntry = _Hh3cDHCPRIfSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 1, 1)
)
hh3cDHCPRIfSelectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRIfSelectEntry.setStatus("current")


class _Hh3cDHCPRIfSelectRelayMode_Type(Integer32):
    """Custom type hh3cDHCPRIfSelectRelayMode based on Integer32"""
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


_Hh3cDHCPRIfSelectRelayMode_Type.__name__ = "Integer32"
_Hh3cDHCPRIfSelectRelayMode_Object = MibTableColumn
hh3cDHCPRIfSelectRelayMode = _Hh3cDHCPRIfSelectRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 1, 1, 1),
    _Hh3cDHCPRIfSelectRelayMode_Type()
)
hh3cDHCPRIfSelectRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRIfSelectRelayMode.setStatus("current")
_Hh3cDHCPRIpToGroupTable_Object = MibTable
hh3cDHCPRIpToGroupTable = _Hh3cDHCPRIpToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cDHCPRIpToGroupTable.setStatus("current")
_Hh3cDHCPRIpToGroupEntry_Object = MibTableRow
hh3cDHCPRIpToGroupEntry = _Hh3cDHCPRIpToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 2, 1)
)
hh3cDHCPRIpToGroupEntry.setIndexNames(
    (0, "HH3C-DHCPRELAY-MIB", "hh3cDHCPRIpToGroupGroupId"),
    (0, "HH3C-DHCPRELAY-MIB", "hh3cDHCPRIpToGroupServerIpType"),
    (0, "HH3C-DHCPRELAY-MIB", "hh3cDHCPRIpToGroupServerIp"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRIpToGroupEntry.setStatus("current")


class _Hh3cDHCPRIpToGroupGroupId_Type(Integer32):
    """Custom type hh3cDHCPRIpToGroupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_Hh3cDHCPRIpToGroupGroupId_Type.__name__ = "Integer32"
_Hh3cDHCPRIpToGroupGroupId_Object = MibTableColumn
hh3cDHCPRIpToGroupGroupId = _Hh3cDHCPRIpToGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 2, 1, 1),
    _Hh3cDHCPRIpToGroupGroupId_Type()
)
hh3cDHCPRIpToGroupGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDHCPRIpToGroupGroupId.setStatus("current")
_Hh3cDHCPRIpToGroupServerIpType_Type = InetAddressType
_Hh3cDHCPRIpToGroupServerIpType_Object = MibTableColumn
hh3cDHCPRIpToGroupServerIpType = _Hh3cDHCPRIpToGroupServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 2, 1, 2),
    _Hh3cDHCPRIpToGroupServerIpType_Type()
)
hh3cDHCPRIpToGroupServerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDHCPRIpToGroupServerIpType.setStatus("current")


class _Hh3cDHCPRIpToGroupServerIp_Type(InetAddress):
    """Custom type hh3cDHCPRIpToGroupServerIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDHCPRIpToGroupServerIp_Type.__name__ = "InetAddress"
_Hh3cDHCPRIpToGroupServerIp_Object = MibTableColumn
hh3cDHCPRIpToGroupServerIp = _Hh3cDHCPRIpToGroupServerIp_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 2, 1, 3),
    _Hh3cDHCPRIpToGroupServerIp_Type()
)
hh3cDHCPRIpToGroupServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDHCPRIpToGroupServerIp.setStatus("current")
_Hh3cDHCPRIpToGroupRowStatus_Type = RowStatus
_Hh3cDHCPRIpToGroupRowStatus_Object = MibTableColumn
hh3cDHCPRIpToGroupRowStatus = _Hh3cDHCPRIpToGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 2, 1, 4),
    _Hh3cDHCPRIpToGroupRowStatus_Type()
)
hh3cDHCPRIpToGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPRIpToGroupRowStatus.setStatus("current")
_Hh3cDHCPRIfToGroupTable_Object = MibTable
hh3cDHCPRIfToGroupTable = _Hh3cDHCPRIfToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cDHCPRIfToGroupTable.setStatus("current")
_Hh3cDHCPRIfToGroupEntry_Object = MibTableRow
hh3cDHCPRIfToGroupEntry = _Hh3cDHCPRIfToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 3, 1)
)
hh3cDHCPRIfToGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRIfToGroupEntry.setStatus("current")


class _Hh3cDHCPRIfToGroupGroupId_Type(Integer32):
    """Custom type hh3cDHCPRIfToGroupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_Hh3cDHCPRIfToGroupGroupId_Type.__name__ = "Integer32"
_Hh3cDHCPRIfToGroupGroupId_Object = MibTableColumn
hh3cDHCPRIfToGroupGroupId = _Hh3cDHCPRIfToGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 3, 1, 1),
    _Hh3cDHCPRIfToGroupGroupId_Type()
)
hh3cDHCPRIfToGroupGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRIfToGroupGroupId.setStatus("current")
_Hh3cDHCPRIfToGroupRowStatus_Type = RowStatus
_Hh3cDHCPRIfToGroupRowStatus_Object = MibTableColumn
hh3cDHCPRIfToGroupRowStatus = _Hh3cDHCPRIfToGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 3, 1, 2),
    _Hh3cDHCPRIfToGroupRowStatus_Type()
)
hh3cDHCPRIfToGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPRIfToGroupRowStatus.setStatus("current")
_Hh3cDHCPRAddrCheckTable_Object = MibTable
hh3cDHCPRAddrCheckTable = _Hh3cDHCPRAddrCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cDHCPRAddrCheckTable.setStatus("current")
_Hh3cDHCPRAddrCheckEntry_Object = MibTableRow
hh3cDHCPRAddrCheckEntry = _Hh3cDHCPRAddrCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 4, 1)
)
hh3cDHCPRAddrCheckEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRAddrCheckEntry.setStatus("current")


class _Hh3cDHCPRAddrCheckSwitch_Type(Integer32):
    """Custom type hh3cDHCPRAddrCheckSwitch based on Integer32"""
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


_Hh3cDHCPRAddrCheckSwitch_Type.__name__ = "Integer32"
_Hh3cDHCPRAddrCheckSwitch_Object = MibTableColumn
hh3cDHCPRAddrCheckSwitch = _Hh3cDHCPRAddrCheckSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 4, 1, 1),
    _Hh3cDHCPRAddrCheckSwitch_Type()
)
hh3cDHCPRAddrCheckSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRAddrCheckSwitch.setStatus("current")
_Hh3cDHCPRSecurityTable_Object = MibTable
hh3cDHCPRSecurityTable = _Hh3cDHCPRSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 5)
)
if mibBuilder.loadTexts:
    hh3cDHCPRSecurityTable.setStatus("current")
_Hh3cDHCPRSecurityEntry_Object = MibTableRow
hh3cDHCPRSecurityEntry = _Hh3cDHCPRSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 5, 1)
)
hh3cDHCPRSecurityEntry.setIndexNames(
    (0, "HH3C-DHCPRELAY-MIB", "hh3cDHCPRSecurityClientIpAddrType"),
    (0, "HH3C-DHCPRELAY-MIB", "hh3cDHCPRSecurityClientIpAddr"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRSecurityEntry.setStatus("current")
_Hh3cDHCPRSecurityClientIpAddrType_Type = InetAddressType
_Hh3cDHCPRSecurityClientIpAddrType_Object = MibTableColumn
hh3cDHCPRSecurityClientIpAddrType = _Hh3cDHCPRSecurityClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 5, 1, 1),
    _Hh3cDHCPRSecurityClientIpAddrType_Type()
)
hh3cDHCPRSecurityClientIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDHCPRSecurityClientIpAddrType.setStatus("current")


class _Hh3cDHCPRSecurityClientIpAddr_Type(InetAddress):
    """Custom type hh3cDHCPRSecurityClientIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_Hh3cDHCPRSecurityClientIpAddr_Type.__name__ = "InetAddress"
_Hh3cDHCPRSecurityClientIpAddr_Object = MibTableColumn
hh3cDHCPRSecurityClientIpAddr = _Hh3cDHCPRSecurityClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 5, 1, 2),
    _Hh3cDHCPRSecurityClientIpAddr_Type()
)
hh3cDHCPRSecurityClientIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cDHCPRSecurityClientIpAddr.setStatus("current")
_Hh3cDHCPRSecurityClientMacAddr_Type = MacAddress
_Hh3cDHCPRSecurityClientMacAddr_Object = MibTableColumn
hh3cDHCPRSecurityClientMacAddr = _Hh3cDHCPRSecurityClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 5, 1, 3),
    _Hh3cDHCPRSecurityClientMacAddr_Type()
)
hh3cDHCPRSecurityClientMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRSecurityClientMacAddr.setStatus("current")


class _Hh3cDHCPRSecurityClientProperty_Type(Integer32):
    """Custom type hh3cDHCPRSecurityClientProperty based on Integer32"""
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


_Hh3cDHCPRSecurityClientProperty_Type.__name__ = "Integer32"
_Hh3cDHCPRSecurityClientProperty_Object = MibTableColumn
hh3cDHCPRSecurityClientProperty = _Hh3cDHCPRSecurityClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 5, 1, 4),
    _Hh3cDHCPRSecurityClientProperty_Type()
)
hh3cDHCPRSecurityClientProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRSecurityClientProperty.setStatus("current")
_Hh3cDHCPRSecurityClientRowStatus_Type = RowStatus
_Hh3cDHCPRSecurityClientRowStatus_Object = MibTableColumn
hh3cDHCPRSecurityClientRowStatus = _Hh3cDHCPRSecurityClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 5, 1, 5),
    _Hh3cDHCPRSecurityClientRowStatus_Type()
)
hh3cDHCPRSecurityClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cDHCPRSecurityClientRowStatus.setStatus("current")
_Hh3cDHCPRStatisticsGroup_ObjectIdentity = ObjectIdentity
hh3cDHCPRStatisticsGroup = _Hh3cDHCPRStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6)
)
_Hh3cDHCPRRxClientPktNum_Type = Unsigned32
_Hh3cDHCPRRxClientPktNum_Object = MibScalar
hh3cDHCPRRxClientPktNum = _Hh3cDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 1),
    _Hh3cDHCPRRxClientPktNum_Type()
)
hh3cDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRRxClientPktNum.setStatus("current")
_Hh3cDHCPRTxClientPktNum_Type = Unsigned32
_Hh3cDHCPRTxClientPktNum_Object = MibScalar
hh3cDHCPRTxClientPktNum = _Hh3cDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 2),
    _Hh3cDHCPRTxClientPktNum_Type()
)
hh3cDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRTxClientPktNum.setStatus("current")
_Hh3cDHCPRRxServerPktNum_Type = Unsigned32
_Hh3cDHCPRRxServerPktNum_Object = MibScalar
hh3cDHCPRRxServerPktNum = _Hh3cDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 3),
    _Hh3cDHCPRRxServerPktNum_Type()
)
hh3cDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRRxServerPktNum.setStatus("current")
_Hh3cDHCPRTxServerPktNum_Type = Unsigned32
_Hh3cDHCPRTxServerPktNum_Object = MibScalar
hh3cDHCPRTxServerPktNum = _Hh3cDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 4),
    _Hh3cDHCPRTxServerPktNum_Type()
)
hh3cDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRTxServerPktNum.setStatus("current")
_Hh3cDHCPRDiscoverPktNum_Type = Unsigned32
_Hh3cDHCPRDiscoverPktNum_Object = MibScalar
hh3cDHCPRDiscoverPktNum = _Hh3cDHCPRDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 5),
    _Hh3cDHCPRDiscoverPktNum_Type()
)
hh3cDHCPRDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRDiscoverPktNum.setStatus("current")
_Hh3cDHCPRRequestPktNum_Type = Unsigned32
_Hh3cDHCPRRequestPktNum_Object = MibScalar
hh3cDHCPRRequestPktNum = _Hh3cDHCPRRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 6),
    _Hh3cDHCPRRequestPktNum_Type()
)
hh3cDHCPRRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRRequestPktNum.setStatus("current")
_Hh3cDHCPRDeclinePktNum_Type = Unsigned32
_Hh3cDHCPRDeclinePktNum_Object = MibScalar
hh3cDHCPRDeclinePktNum = _Hh3cDHCPRDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 7),
    _Hh3cDHCPRDeclinePktNum_Type()
)
hh3cDHCPRDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRDeclinePktNum.setStatus("current")
_Hh3cDHCPRReleasePktNum_Type = Unsigned32
_Hh3cDHCPRReleasePktNum_Object = MibScalar
hh3cDHCPRReleasePktNum = _Hh3cDHCPRReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 8),
    _Hh3cDHCPRReleasePktNum_Type()
)
hh3cDHCPRReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRReleasePktNum.setStatus("current")
_Hh3cDHCPRInformPktNum_Type = Unsigned32
_Hh3cDHCPRInformPktNum_Object = MibScalar
hh3cDHCPRInformPktNum = _Hh3cDHCPRInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 9),
    _Hh3cDHCPRInformPktNum_Type()
)
hh3cDHCPRInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRInformPktNum.setStatus("current")
_Hh3cDHCPROfferPktNum_Type = Unsigned32
_Hh3cDHCPROfferPktNum_Object = MibScalar
hh3cDHCPROfferPktNum = _Hh3cDHCPROfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 10),
    _Hh3cDHCPROfferPktNum_Type()
)
hh3cDHCPROfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPROfferPktNum.setStatus("current")
_Hh3cDHCPRAckPktNum_Type = Unsigned32
_Hh3cDHCPRAckPktNum_Object = MibScalar
hh3cDHCPRAckPktNum = _Hh3cDHCPRAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 11),
    _Hh3cDHCPRAckPktNum_Type()
)
hh3cDHCPRAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRAckPktNum.setStatus("current")
_Hh3cDHCPRNakPktNum_Type = Unsigned32
_Hh3cDHCPRNakPktNum_Object = MibScalar
hh3cDHCPRNakPktNum = _Hh3cDHCPRNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 12),
    _Hh3cDHCPRNakPktNum_Type()
)
hh3cDHCPRNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cDHCPRNakPktNum.setStatus("current")
_Hh3cDHCPRStatisticsReset_Type = TruthValue
_Hh3cDHCPRStatisticsReset_Object = MibScalar
hh3cDHCPRStatisticsReset = _Hh3cDHCPRStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 6, 13),
    _Hh3cDHCPRStatisticsReset_Type()
)
hh3cDHCPRStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRStatisticsReset.setStatus("current")
_Hh3cDHCPRCycleGroup_ObjectIdentity = ObjectIdentity
hh3cDHCPRCycleGroup = _Hh3cDHCPRCycleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 7)
)


class _Hh3cDHCPRCycleStatus_Type(Integer32):
    """Custom type hh3cDHCPRCycleStatus based on Integer32"""
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


_Hh3cDHCPRCycleStatus_Type.__name__ = "Integer32"
_Hh3cDHCPRCycleStatus_Object = MibScalar
hh3cDHCPRCycleStatus = _Hh3cDHCPRCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 7, 1),
    _Hh3cDHCPRCycleStatus_Type()
)
hh3cDHCPRCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPRCycleStatus.setStatus("current")
_Hh3cDHCPRConfigOption82Group_ObjectIdentity = ObjectIdentity
hh3cDHCPRConfigOption82Group = _Hh3cDHCPRConfigOption82Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8)
)


class _Hh3cDHCPROption82Switch_Type(Integer32):
    """Custom type hh3cDHCPROption82Switch based on Integer32"""
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


_Hh3cDHCPROption82Switch_Type.__name__ = "Integer32"
_Hh3cDHCPROption82Switch_Object = MibScalar
hh3cDHCPROption82Switch = _Hh3cDHCPROption82Switch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 1),
    _Hh3cDHCPROption82Switch_Type()
)
hh3cDHCPROption82Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPROption82Switch.setStatus("current")


class _Hh3cDHCPROption82HandleStrategy_Type(Integer32):
    """Custom type hh3cDHCPROption82HandleStrategy based on Integer32"""
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


_Hh3cDHCPROption82HandleStrategy_Type.__name__ = "Integer32"
_Hh3cDHCPROption82HandleStrategy_Object = MibScalar
hh3cDHCPROption82HandleStrategy = _Hh3cDHCPROption82HandleStrategy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 2),
    _Hh3cDHCPROption82HandleStrategy_Type()
)
hh3cDHCPROption82HandleStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPROption82HandleStrategy.setStatus("current")
_Hh3cDHCPRConfigOption82IfTable_Object = MibTable
hh3cDHCPRConfigOption82IfTable = _Hh3cDHCPRConfigOption82IfTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 3)
)
if mibBuilder.loadTexts:
    hh3cDHCPRConfigOption82IfTable.setStatus("current")
_Hh3cDHCPRConfigOption82IfEntry_Object = MibTableRow
hh3cDHCPRConfigOption82IfEntry = _Hh3cDHCPRConfigOption82IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 3, 1)
)
hh3cDHCPRConfigOption82IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cDHCPRConfigOption82IfEntry.setStatus("current")


class _Hh3cDHCPROption82IfSwitch_Type(Integer32):
    """Custom type hh3cDHCPROption82IfSwitch based on Integer32"""
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


_Hh3cDHCPROption82IfSwitch_Type.__name__ = "Integer32"
_Hh3cDHCPROption82IfSwitch_Object = MibTableColumn
hh3cDHCPROption82IfSwitch = _Hh3cDHCPROption82IfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 3, 1, 1),
    _Hh3cDHCPROption82IfSwitch_Type()
)
hh3cDHCPROption82IfSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPROption82IfSwitch.setStatus("current")


class _Hh3cDHCPROption82IfStrategy_Type(Integer32):
    """Custom type hh3cDHCPROption82IfStrategy based on Integer32"""
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


_Hh3cDHCPROption82IfStrategy_Type.__name__ = "Integer32"
_Hh3cDHCPROption82IfStrategy_Object = MibTableColumn
hh3cDHCPROption82IfStrategy = _Hh3cDHCPROption82IfStrategy_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 3, 1, 2),
    _Hh3cDHCPROption82IfStrategy_Type()
)
hh3cDHCPROption82IfStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPROption82IfStrategy.setStatus("current")


class _Hh3cDHCPROption82IfFormat_Type(Integer32):
    """Custom type hh3cDHCPROption82IfFormat based on Integer32"""
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


_Hh3cDHCPROption82IfFormat_Type.__name__ = "Integer32"
_Hh3cDHCPROption82IfFormat_Object = MibTableColumn
hh3cDHCPROption82IfFormat = _Hh3cDHCPROption82IfFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 3, 1, 3),
    _Hh3cDHCPROption82IfFormat_Type()
)
hh3cDHCPROption82IfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPROption82IfFormat.setStatus("current")


class _Hh3cDHCPROption82IfNodeType_Type(Integer32):
    """Custom type hh3cDHCPROption82IfNodeType based on Integer32"""
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


_Hh3cDHCPROption82IfNodeType_Type.__name__ = "Integer32"
_Hh3cDHCPROption82IfNodeType_Object = MibTableColumn
hh3cDHCPROption82IfNodeType = _Hh3cDHCPROption82IfNodeType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 3, 1, 4),
    _Hh3cDHCPROption82IfNodeType_Type()
)
hh3cDHCPROption82IfNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPROption82IfNodeType.setStatus("current")


class _Hh3cDHCPROption82IfUsrDefString_Type(OctetString):
    """Custom type hh3cDHCPROption82IfUsrDefString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cDHCPROption82IfUsrDefString_Type.__name__ = "OctetString"
_Hh3cDHCPROption82IfUsrDefString_Object = MibTableColumn
hh3cDHCPROption82IfUsrDefString = _Hh3cDHCPROption82IfUsrDefString_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 58, 1, 8, 3, 1, 5),
    _Hh3cDHCPROption82IfUsrDefString_Type()
)
hh3cDHCPROption82IfUsrDefString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cDHCPROption82IfUsrDefString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-DHCPRELAY-MIB",
    **{"hh3cDhcpRelay": hh3cDhcpRelay,
       "hh3cDHCPRMibObject": hh3cDHCPRMibObject,
       "hh3cDHCPRIfSelectTable": hh3cDHCPRIfSelectTable,
       "hh3cDHCPRIfSelectEntry": hh3cDHCPRIfSelectEntry,
       "hh3cDHCPRIfSelectRelayMode": hh3cDHCPRIfSelectRelayMode,
       "hh3cDHCPRIpToGroupTable": hh3cDHCPRIpToGroupTable,
       "hh3cDHCPRIpToGroupEntry": hh3cDHCPRIpToGroupEntry,
       "hh3cDHCPRIpToGroupGroupId": hh3cDHCPRIpToGroupGroupId,
       "hh3cDHCPRIpToGroupServerIpType": hh3cDHCPRIpToGroupServerIpType,
       "hh3cDHCPRIpToGroupServerIp": hh3cDHCPRIpToGroupServerIp,
       "hh3cDHCPRIpToGroupRowStatus": hh3cDHCPRIpToGroupRowStatus,
       "hh3cDHCPRIfToGroupTable": hh3cDHCPRIfToGroupTable,
       "hh3cDHCPRIfToGroupEntry": hh3cDHCPRIfToGroupEntry,
       "hh3cDHCPRIfToGroupGroupId": hh3cDHCPRIfToGroupGroupId,
       "hh3cDHCPRIfToGroupRowStatus": hh3cDHCPRIfToGroupRowStatus,
       "hh3cDHCPRAddrCheckTable": hh3cDHCPRAddrCheckTable,
       "hh3cDHCPRAddrCheckEntry": hh3cDHCPRAddrCheckEntry,
       "hh3cDHCPRAddrCheckSwitch": hh3cDHCPRAddrCheckSwitch,
       "hh3cDHCPRSecurityTable": hh3cDHCPRSecurityTable,
       "hh3cDHCPRSecurityEntry": hh3cDHCPRSecurityEntry,
       "hh3cDHCPRSecurityClientIpAddrType": hh3cDHCPRSecurityClientIpAddrType,
       "hh3cDHCPRSecurityClientIpAddr": hh3cDHCPRSecurityClientIpAddr,
       "hh3cDHCPRSecurityClientMacAddr": hh3cDHCPRSecurityClientMacAddr,
       "hh3cDHCPRSecurityClientProperty": hh3cDHCPRSecurityClientProperty,
       "hh3cDHCPRSecurityClientRowStatus": hh3cDHCPRSecurityClientRowStatus,
       "hh3cDHCPRStatisticsGroup": hh3cDHCPRStatisticsGroup,
       "hh3cDHCPRRxClientPktNum": hh3cDHCPRRxClientPktNum,
       "hh3cDHCPRTxClientPktNum": hh3cDHCPRTxClientPktNum,
       "hh3cDHCPRRxServerPktNum": hh3cDHCPRRxServerPktNum,
       "hh3cDHCPRTxServerPktNum": hh3cDHCPRTxServerPktNum,
       "hh3cDHCPRDiscoverPktNum": hh3cDHCPRDiscoverPktNum,
       "hh3cDHCPRRequestPktNum": hh3cDHCPRRequestPktNum,
       "hh3cDHCPRDeclinePktNum": hh3cDHCPRDeclinePktNum,
       "hh3cDHCPRReleasePktNum": hh3cDHCPRReleasePktNum,
       "hh3cDHCPRInformPktNum": hh3cDHCPRInformPktNum,
       "hh3cDHCPROfferPktNum": hh3cDHCPROfferPktNum,
       "hh3cDHCPRAckPktNum": hh3cDHCPRAckPktNum,
       "hh3cDHCPRNakPktNum": hh3cDHCPRNakPktNum,
       "hh3cDHCPRStatisticsReset": hh3cDHCPRStatisticsReset,
       "hh3cDHCPRCycleGroup": hh3cDHCPRCycleGroup,
       "hh3cDHCPRCycleStatus": hh3cDHCPRCycleStatus,
       "hh3cDHCPRConfigOption82Group": hh3cDHCPRConfigOption82Group,
       "hh3cDHCPROption82Switch": hh3cDHCPROption82Switch,
       "hh3cDHCPROption82HandleStrategy": hh3cDHCPROption82HandleStrategy,
       "hh3cDHCPRConfigOption82IfTable": hh3cDHCPRConfigOption82IfTable,
       "hh3cDHCPRConfigOption82IfEntry": hh3cDHCPRConfigOption82IfEntry,
       "hh3cDHCPROption82IfSwitch": hh3cDHCPROption82IfSwitch,
       "hh3cDHCPROption82IfStrategy": hh3cDHCPROption82IfStrategy,
       "hh3cDHCPROption82IfFormat": hh3cDHCPROption82IfFormat,
       "hh3cDHCPROption82IfNodeType": hh3cDHCPROption82IfNodeType,
       "hh3cDHCPROption82IfUsrDefString": hh3cDHCPROption82IfUsrDefString}
)
