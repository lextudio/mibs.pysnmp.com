# SNMP MIB module (HPN-ICF-DHCPRELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DHCPRELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:42 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfDhcpRelay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58)
)
hpnicfDhcpRelay.setRevisions(
        ("2005-06-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDHCPRMibObject_ObjectIdentity = ObjectIdentity
hpnicfDHCPRMibObject = _HpnicfDHCPRMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1)
)
_HpnicfDHCPRIfSelectTable_Object = MibTable
hpnicfDHCPRIfSelectTable = _HpnicfDHCPRIfSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIfSelectTable.setStatus("current")
_HpnicfDHCPRIfSelectEntry_Object = MibTableRow
hpnicfDHCPRIfSelectEntry = _HpnicfDHCPRIfSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 1, 1)
)
hpnicfDHCPRIfSelectEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIfSelectEntry.setStatus("current")


class _HpnicfDHCPRIfSelectRelayMode_Type(Integer32):
    """Custom type hpnicfDHCPRIfSelectRelayMode based on Integer32"""
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


_HpnicfDHCPRIfSelectRelayMode_Type.__name__ = "Integer32"
_HpnicfDHCPRIfSelectRelayMode_Object = MibTableColumn
hpnicfDHCPRIfSelectRelayMode = _HpnicfDHCPRIfSelectRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 1, 1, 1),
    _HpnicfDHCPRIfSelectRelayMode_Type()
)
hpnicfDHCPRIfSelectRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRIfSelectRelayMode.setStatus("current")
_HpnicfDHCPRIpToGroupTable_Object = MibTable
hpnicfDHCPRIpToGroupTable = _HpnicfDHCPRIpToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIpToGroupTable.setStatus("current")
_HpnicfDHCPRIpToGroupEntry_Object = MibTableRow
hpnicfDHCPRIpToGroupEntry = _HpnicfDHCPRIpToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 2, 1)
)
hpnicfDHCPRIpToGroupEntry.setIndexNames(
    (0, "HPN-ICF-DHCPRELAY-MIB", "hpnicfDHCPRIpToGroupGroupId"),
    (0, "HPN-ICF-DHCPRELAY-MIB", "hpnicfDHCPRIpToGroupServerIpType"),
    (0, "HPN-ICF-DHCPRELAY-MIB", "hpnicfDHCPRIpToGroupServerIp"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIpToGroupEntry.setStatus("current")


class _HpnicfDHCPRIpToGroupGroupId_Type(Integer32):
    """Custom type hpnicfDHCPRIpToGroupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_HpnicfDHCPRIpToGroupGroupId_Type.__name__ = "Integer32"
_HpnicfDHCPRIpToGroupGroupId_Object = MibTableColumn
hpnicfDHCPRIpToGroupGroupId = _HpnicfDHCPRIpToGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 2, 1, 1),
    _HpnicfDHCPRIpToGroupGroupId_Type()
)
hpnicfDHCPRIpToGroupGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDHCPRIpToGroupGroupId.setStatus("current")
_HpnicfDHCPRIpToGroupServerIpType_Type = InetAddressType
_HpnicfDHCPRIpToGroupServerIpType_Object = MibTableColumn
hpnicfDHCPRIpToGroupServerIpType = _HpnicfDHCPRIpToGroupServerIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 2, 1, 2),
    _HpnicfDHCPRIpToGroupServerIpType_Type()
)
hpnicfDHCPRIpToGroupServerIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDHCPRIpToGroupServerIpType.setStatus("current")


class _HpnicfDHCPRIpToGroupServerIp_Type(InetAddress):
    """Custom type hpnicfDHCPRIpToGroupServerIp based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfDHCPRIpToGroupServerIp_Type.__name__ = "InetAddress"
_HpnicfDHCPRIpToGroupServerIp_Object = MibTableColumn
hpnicfDHCPRIpToGroupServerIp = _HpnicfDHCPRIpToGroupServerIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 2, 1, 3),
    _HpnicfDHCPRIpToGroupServerIp_Type()
)
hpnicfDHCPRIpToGroupServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDHCPRIpToGroupServerIp.setStatus("current")
_HpnicfDHCPRIpToGroupRowStatus_Type = RowStatus
_HpnicfDHCPRIpToGroupRowStatus_Object = MibTableColumn
hpnicfDHCPRIpToGroupRowStatus = _HpnicfDHCPRIpToGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 2, 1, 4),
    _HpnicfDHCPRIpToGroupRowStatus_Type()
)
hpnicfDHCPRIpToGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPRIpToGroupRowStatus.setStatus("current")
_HpnicfDHCPRIfToGroupTable_Object = MibTable
hpnicfDHCPRIfToGroupTable = _HpnicfDHCPRIfToGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIfToGroupTable.setStatus("current")
_HpnicfDHCPRIfToGroupEntry_Object = MibTableRow
hpnicfDHCPRIfToGroupEntry = _HpnicfDHCPRIfToGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 3, 1)
)
hpnicfDHCPRIfToGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRIfToGroupEntry.setStatus("current")


class _HpnicfDHCPRIfToGroupGroupId_Type(Integer32):
    """Custom type hpnicfDHCPRIfToGroupGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_HpnicfDHCPRIfToGroupGroupId_Type.__name__ = "Integer32"
_HpnicfDHCPRIfToGroupGroupId_Object = MibTableColumn
hpnicfDHCPRIfToGroupGroupId = _HpnicfDHCPRIfToGroupGroupId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 3, 1, 1),
    _HpnicfDHCPRIfToGroupGroupId_Type()
)
hpnicfDHCPRIfToGroupGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRIfToGroupGroupId.setStatus("current")
_HpnicfDHCPRIfToGroupRowStatus_Type = RowStatus
_HpnicfDHCPRIfToGroupRowStatus_Object = MibTableColumn
hpnicfDHCPRIfToGroupRowStatus = _HpnicfDHCPRIfToGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 3, 1, 2),
    _HpnicfDHCPRIfToGroupRowStatus_Type()
)
hpnicfDHCPRIfToGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPRIfToGroupRowStatus.setStatus("current")
_HpnicfDHCPRAddrCheckTable_Object = MibTable
hpnicfDHCPRAddrCheckTable = _HpnicfDHCPRAddrCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRAddrCheckTable.setStatus("current")
_HpnicfDHCPRAddrCheckEntry_Object = MibTableRow
hpnicfDHCPRAddrCheckEntry = _HpnicfDHCPRAddrCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 4, 1)
)
hpnicfDHCPRAddrCheckEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRAddrCheckEntry.setStatus("current")


class _HpnicfDHCPRAddrCheckSwitch_Type(Integer32):
    """Custom type hpnicfDHCPRAddrCheckSwitch based on Integer32"""
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


_HpnicfDHCPRAddrCheckSwitch_Type.__name__ = "Integer32"
_HpnicfDHCPRAddrCheckSwitch_Object = MibTableColumn
hpnicfDHCPRAddrCheckSwitch = _HpnicfDHCPRAddrCheckSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 4, 1, 1),
    _HpnicfDHCPRAddrCheckSwitch_Type()
)
hpnicfDHCPRAddrCheckSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRAddrCheckSwitch.setStatus("current")
_HpnicfDHCPRSecurityTable_Object = MibTable
hpnicfDHCPRSecurityTable = _HpnicfDHCPRSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRSecurityTable.setStatus("current")
_HpnicfDHCPRSecurityEntry_Object = MibTableRow
hpnicfDHCPRSecurityEntry = _HpnicfDHCPRSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 5, 1)
)
hpnicfDHCPRSecurityEntry.setIndexNames(
    (0, "HPN-ICF-DHCPRELAY-MIB", "hpnicfDHCPRSecurityClientIpAddrType"),
    (0, "HPN-ICF-DHCPRELAY-MIB", "hpnicfDHCPRSecurityClientIpAddr"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRSecurityEntry.setStatus("current")
_HpnicfDHCPRSecurityClientIpAddrType_Type = InetAddressType
_HpnicfDHCPRSecurityClientIpAddrType_Object = MibTableColumn
hpnicfDHCPRSecurityClientIpAddrType = _HpnicfDHCPRSecurityClientIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 5, 1, 1),
    _HpnicfDHCPRSecurityClientIpAddrType_Type()
)
hpnicfDHCPRSecurityClientIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDHCPRSecurityClientIpAddrType.setStatus("current")


class _HpnicfDHCPRSecurityClientIpAddr_Type(InetAddress):
    """Custom type hpnicfDHCPRSecurityClientIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpnicfDHCPRSecurityClientIpAddr_Type.__name__ = "InetAddress"
_HpnicfDHCPRSecurityClientIpAddr_Object = MibTableColumn
hpnicfDHCPRSecurityClientIpAddr = _HpnicfDHCPRSecurityClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 5, 1, 2),
    _HpnicfDHCPRSecurityClientIpAddr_Type()
)
hpnicfDHCPRSecurityClientIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDHCPRSecurityClientIpAddr.setStatus("current")
_HpnicfDHCPRSecurityClientMacAddr_Type = MacAddress
_HpnicfDHCPRSecurityClientMacAddr_Object = MibTableColumn
hpnicfDHCPRSecurityClientMacAddr = _HpnicfDHCPRSecurityClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 5, 1, 3),
    _HpnicfDHCPRSecurityClientMacAddr_Type()
)
hpnicfDHCPRSecurityClientMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRSecurityClientMacAddr.setStatus("current")


class _HpnicfDHCPRSecurityClientProperty_Type(Integer32):
    """Custom type hpnicfDHCPRSecurityClientProperty based on Integer32"""
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


_HpnicfDHCPRSecurityClientProperty_Type.__name__ = "Integer32"
_HpnicfDHCPRSecurityClientProperty_Object = MibTableColumn
hpnicfDHCPRSecurityClientProperty = _HpnicfDHCPRSecurityClientProperty_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 5, 1, 4),
    _HpnicfDHCPRSecurityClientProperty_Type()
)
hpnicfDHCPRSecurityClientProperty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRSecurityClientProperty.setStatus("current")
_HpnicfDHCPRSecurityClientRowStatus_Type = RowStatus
_HpnicfDHCPRSecurityClientRowStatus_Object = MibTableColumn
hpnicfDHCPRSecurityClientRowStatus = _HpnicfDHCPRSecurityClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 5, 1, 5),
    _HpnicfDHCPRSecurityClientRowStatus_Type()
)
hpnicfDHCPRSecurityClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfDHCPRSecurityClientRowStatus.setStatus("current")
_HpnicfDHCPRStatisticsGroup_ObjectIdentity = ObjectIdentity
hpnicfDHCPRStatisticsGroup = _HpnicfDHCPRStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6)
)
_HpnicfDHCPRRxClientPktNum_Type = Unsigned32
_HpnicfDHCPRRxClientPktNum_Object = MibScalar
hpnicfDHCPRRxClientPktNum = _HpnicfDHCPRRxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 1),
    _HpnicfDHCPRRxClientPktNum_Type()
)
hpnicfDHCPRRxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRRxClientPktNum.setStatus("current")
_HpnicfDHCPRTxClientPktNum_Type = Unsigned32
_HpnicfDHCPRTxClientPktNum_Object = MibScalar
hpnicfDHCPRTxClientPktNum = _HpnicfDHCPRTxClientPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 2),
    _HpnicfDHCPRTxClientPktNum_Type()
)
hpnicfDHCPRTxClientPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRTxClientPktNum.setStatus("current")
_HpnicfDHCPRRxServerPktNum_Type = Unsigned32
_HpnicfDHCPRRxServerPktNum_Object = MibScalar
hpnicfDHCPRRxServerPktNum = _HpnicfDHCPRRxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 3),
    _HpnicfDHCPRRxServerPktNum_Type()
)
hpnicfDHCPRRxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRRxServerPktNum.setStatus("current")
_HpnicfDHCPRTxServerPktNum_Type = Unsigned32
_HpnicfDHCPRTxServerPktNum_Object = MibScalar
hpnicfDHCPRTxServerPktNum = _HpnicfDHCPRTxServerPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 4),
    _HpnicfDHCPRTxServerPktNum_Type()
)
hpnicfDHCPRTxServerPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRTxServerPktNum.setStatus("current")
_HpnicfDHCPRDiscoverPktNum_Type = Unsigned32
_HpnicfDHCPRDiscoverPktNum_Object = MibScalar
hpnicfDHCPRDiscoverPktNum = _HpnicfDHCPRDiscoverPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 5),
    _HpnicfDHCPRDiscoverPktNum_Type()
)
hpnicfDHCPRDiscoverPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRDiscoverPktNum.setStatus("current")
_HpnicfDHCPRRequestPktNum_Type = Unsigned32
_HpnicfDHCPRRequestPktNum_Object = MibScalar
hpnicfDHCPRRequestPktNum = _HpnicfDHCPRRequestPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 6),
    _HpnicfDHCPRRequestPktNum_Type()
)
hpnicfDHCPRRequestPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRRequestPktNum.setStatus("current")
_HpnicfDHCPRDeclinePktNum_Type = Unsigned32
_HpnicfDHCPRDeclinePktNum_Object = MibScalar
hpnicfDHCPRDeclinePktNum = _HpnicfDHCPRDeclinePktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 7),
    _HpnicfDHCPRDeclinePktNum_Type()
)
hpnicfDHCPRDeclinePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRDeclinePktNum.setStatus("current")
_HpnicfDHCPRReleasePktNum_Type = Unsigned32
_HpnicfDHCPRReleasePktNum_Object = MibScalar
hpnicfDHCPRReleasePktNum = _HpnicfDHCPRReleasePktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 8),
    _HpnicfDHCPRReleasePktNum_Type()
)
hpnicfDHCPRReleasePktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRReleasePktNum.setStatus("current")
_HpnicfDHCPRInformPktNum_Type = Unsigned32
_HpnicfDHCPRInformPktNum_Object = MibScalar
hpnicfDHCPRInformPktNum = _HpnicfDHCPRInformPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 9),
    _HpnicfDHCPRInformPktNum_Type()
)
hpnicfDHCPRInformPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRInformPktNum.setStatus("current")
_HpnicfDHCPROfferPktNum_Type = Unsigned32
_HpnicfDHCPROfferPktNum_Object = MibScalar
hpnicfDHCPROfferPktNum = _HpnicfDHCPROfferPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 10),
    _HpnicfDHCPROfferPktNum_Type()
)
hpnicfDHCPROfferPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPROfferPktNum.setStatus("current")
_HpnicfDHCPRAckPktNum_Type = Unsigned32
_HpnicfDHCPRAckPktNum_Object = MibScalar
hpnicfDHCPRAckPktNum = _HpnicfDHCPRAckPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 11),
    _HpnicfDHCPRAckPktNum_Type()
)
hpnicfDHCPRAckPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRAckPktNum.setStatus("current")
_HpnicfDHCPRNakPktNum_Type = Unsigned32
_HpnicfDHCPRNakPktNum_Object = MibScalar
hpnicfDHCPRNakPktNum = _HpnicfDHCPRNakPktNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 12),
    _HpnicfDHCPRNakPktNum_Type()
)
hpnicfDHCPRNakPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDHCPRNakPktNum.setStatus("current")
_HpnicfDHCPRStatisticsReset_Type = TruthValue
_HpnicfDHCPRStatisticsReset_Object = MibScalar
hpnicfDHCPRStatisticsReset = _HpnicfDHCPRStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 6, 13),
    _HpnicfDHCPRStatisticsReset_Type()
)
hpnicfDHCPRStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRStatisticsReset.setStatus("current")
_HpnicfDHCPRCycleGroup_ObjectIdentity = ObjectIdentity
hpnicfDHCPRCycleGroup = _HpnicfDHCPRCycleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 7)
)


class _HpnicfDHCPRCycleStatus_Type(Integer32):
    """Custom type hpnicfDHCPRCycleStatus based on Integer32"""
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


_HpnicfDHCPRCycleStatus_Type.__name__ = "Integer32"
_HpnicfDHCPRCycleStatus_Object = MibScalar
hpnicfDHCPRCycleStatus = _HpnicfDHCPRCycleStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 7, 1),
    _HpnicfDHCPRCycleStatus_Type()
)
hpnicfDHCPRCycleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPRCycleStatus.setStatus("current")
_HpnicfDHCPRConfigOption82Group_ObjectIdentity = ObjectIdentity
hpnicfDHCPRConfigOption82Group = _HpnicfDHCPRConfigOption82Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8)
)


class _HpnicfDHCPROption82Switch_Type(Integer32):
    """Custom type hpnicfDHCPROption82Switch based on Integer32"""
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


_HpnicfDHCPROption82Switch_Type.__name__ = "Integer32"
_HpnicfDHCPROption82Switch_Object = MibScalar
hpnicfDHCPROption82Switch = _HpnicfDHCPROption82Switch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 1),
    _HpnicfDHCPROption82Switch_Type()
)
hpnicfDHCPROption82Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPROption82Switch.setStatus("current")


class _HpnicfDHCPROption82HandleStrategy_Type(Integer32):
    """Custom type hpnicfDHCPROption82HandleStrategy based on Integer32"""
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


_HpnicfDHCPROption82HandleStrategy_Type.__name__ = "Integer32"
_HpnicfDHCPROption82HandleStrategy_Object = MibScalar
hpnicfDHCPROption82HandleStrategy = _HpnicfDHCPROption82HandleStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 2),
    _HpnicfDHCPROption82HandleStrategy_Type()
)
hpnicfDHCPROption82HandleStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPROption82HandleStrategy.setStatus("current")
_HpnicfDHCPRConfigOption82IfTable_Object = MibTable
hpnicfDHCPRConfigOption82IfTable = _HpnicfDHCPRConfigOption82IfTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 3)
)
if mibBuilder.loadTexts:
    hpnicfDHCPRConfigOption82IfTable.setStatus("current")
_HpnicfDHCPRConfigOption82IfEntry_Object = MibTableRow
hpnicfDHCPRConfigOption82IfEntry = _HpnicfDHCPRConfigOption82IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 3, 1)
)
hpnicfDHCPRConfigOption82IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDHCPRConfigOption82IfEntry.setStatus("current")


class _HpnicfDHCPROption82IfSwitch_Type(Integer32):
    """Custom type hpnicfDHCPROption82IfSwitch based on Integer32"""
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


_HpnicfDHCPROption82IfSwitch_Type.__name__ = "Integer32"
_HpnicfDHCPROption82IfSwitch_Object = MibTableColumn
hpnicfDHCPROption82IfSwitch = _HpnicfDHCPROption82IfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 3, 1, 1),
    _HpnicfDHCPROption82IfSwitch_Type()
)
hpnicfDHCPROption82IfSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPROption82IfSwitch.setStatus("current")


class _HpnicfDHCPROption82IfStrategy_Type(Integer32):
    """Custom type hpnicfDHCPROption82IfStrategy based on Integer32"""
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


_HpnicfDHCPROption82IfStrategy_Type.__name__ = "Integer32"
_HpnicfDHCPROption82IfStrategy_Object = MibTableColumn
hpnicfDHCPROption82IfStrategy = _HpnicfDHCPROption82IfStrategy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 3, 1, 2),
    _HpnicfDHCPROption82IfStrategy_Type()
)
hpnicfDHCPROption82IfStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPROption82IfStrategy.setStatus("current")


class _HpnicfDHCPROption82IfFormat_Type(Integer32):
    """Custom type hpnicfDHCPROption82IfFormat based on Integer32"""
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


_HpnicfDHCPROption82IfFormat_Type.__name__ = "Integer32"
_HpnicfDHCPROption82IfFormat_Object = MibTableColumn
hpnicfDHCPROption82IfFormat = _HpnicfDHCPROption82IfFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 3, 1, 3),
    _HpnicfDHCPROption82IfFormat_Type()
)
hpnicfDHCPROption82IfFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPROption82IfFormat.setStatus("current")


class _HpnicfDHCPROption82IfNodeType_Type(Integer32):
    """Custom type hpnicfDHCPROption82IfNodeType based on Integer32"""
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


_HpnicfDHCPROption82IfNodeType_Type.__name__ = "Integer32"
_HpnicfDHCPROption82IfNodeType_Object = MibTableColumn
hpnicfDHCPROption82IfNodeType = _HpnicfDHCPROption82IfNodeType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 3, 1, 4),
    _HpnicfDHCPROption82IfNodeType_Type()
)
hpnicfDHCPROption82IfNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPROption82IfNodeType.setStatus("current")


class _HpnicfDHCPROption82IfUsrDefString_Type(OctetString):
    """Custom type hpnicfDHCPROption82IfUsrDefString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfDHCPROption82IfUsrDefString_Type.__name__ = "OctetString"
_HpnicfDHCPROption82IfUsrDefString_Object = MibTableColumn
hpnicfDHCPROption82IfUsrDefString = _HpnicfDHCPROption82IfUsrDefString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 58, 1, 8, 3, 1, 5),
    _HpnicfDHCPROption82IfUsrDefString_Type()
)
hpnicfDHCPROption82IfUsrDefString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDHCPROption82IfUsrDefString.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DHCPRELAY-MIB",
    **{"hpnicfDhcpRelay": hpnicfDhcpRelay,
       "hpnicfDHCPRMibObject": hpnicfDHCPRMibObject,
       "hpnicfDHCPRIfSelectTable": hpnicfDHCPRIfSelectTable,
       "hpnicfDHCPRIfSelectEntry": hpnicfDHCPRIfSelectEntry,
       "hpnicfDHCPRIfSelectRelayMode": hpnicfDHCPRIfSelectRelayMode,
       "hpnicfDHCPRIpToGroupTable": hpnicfDHCPRIpToGroupTable,
       "hpnicfDHCPRIpToGroupEntry": hpnicfDHCPRIpToGroupEntry,
       "hpnicfDHCPRIpToGroupGroupId": hpnicfDHCPRIpToGroupGroupId,
       "hpnicfDHCPRIpToGroupServerIpType": hpnicfDHCPRIpToGroupServerIpType,
       "hpnicfDHCPRIpToGroupServerIp": hpnicfDHCPRIpToGroupServerIp,
       "hpnicfDHCPRIpToGroupRowStatus": hpnicfDHCPRIpToGroupRowStatus,
       "hpnicfDHCPRIfToGroupTable": hpnicfDHCPRIfToGroupTable,
       "hpnicfDHCPRIfToGroupEntry": hpnicfDHCPRIfToGroupEntry,
       "hpnicfDHCPRIfToGroupGroupId": hpnicfDHCPRIfToGroupGroupId,
       "hpnicfDHCPRIfToGroupRowStatus": hpnicfDHCPRIfToGroupRowStatus,
       "hpnicfDHCPRAddrCheckTable": hpnicfDHCPRAddrCheckTable,
       "hpnicfDHCPRAddrCheckEntry": hpnicfDHCPRAddrCheckEntry,
       "hpnicfDHCPRAddrCheckSwitch": hpnicfDHCPRAddrCheckSwitch,
       "hpnicfDHCPRSecurityTable": hpnicfDHCPRSecurityTable,
       "hpnicfDHCPRSecurityEntry": hpnicfDHCPRSecurityEntry,
       "hpnicfDHCPRSecurityClientIpAddrType": hpnicfDHCPRSecurityClientIpAddrType,
       "hpnicfDHCPRSecurityClientIpAddr": hpnicfDHCPRSecurityClientIpAddr,
       "hpnicfDHCPRSecurityClientMacAddr": hpnicfDHCPRSecurityClientMacAddr,
       "hpnicfDHCPRSecurityClientProperty": hpnicfDHCPRSecurityClientProperty,
       "hpnicfDHCPRSecurityClientRowStatus": hpnicfDHCPRSecurityClientRowStatus,
       "hpnicfDHCPRStatisticsGroup": hpnicfDHCPRStatisticsGroup,
       "hpnicfDHCPRRxClientPktNum": hpnicfDHCPRRxClientPktNum,
       "hpnicfDHCPRTxClientPktNum": hpnicfDHCPRTxClientPktNum,
       "hpnicfDHCPRRxServerPktNum": hpnicfDHCPRRxServerPktNum,
       "hpnicfDHCPRTxServerPktNum": hpnicfDHCPRTxServerPktNum,
       "hpnicfDHCPRDiscoverPktNum": hpnicfDHCPRDiscoverPktNum,
       "hpnicfDHCPRRequestPktNum": hpnicfDHCPRRequestPktNum,
       "hpnicfDHCPRDeclinePktNum": hpnicfDHCPRDeclinePktNum,
       "hpnicfDHCPRReleasePktNum": hpnicfDHCPRReleasePktNum,
       "hpnicfDHCPRInformPktNum": hpnicfDHCPRInformPktNum,
       "hpnicfDHCPROfferPktNum": hpnicfDHCPROfferPktNum,
       "hpnicfDHCPRAckPktNum": hpnicfDHCPRAckPktNum,
       "hpnicfDHCPRNakPktNum": hpnicfDHCPRNakPktNum,
       "hpnicfDHCPRStatisticsReset": hpnicfDHCPRStatisticsReset,
       "hpnicfDHCPRCycleGroup": hpnicfDHCPRCycleGroup,
       "hpnicfDHCPRCycleStatus": hpnicfDHCPRCycleStatus,
       "hpnicfDHCPRConfigOption82Group": hpnicfDHCPRConfigOption82Group,
       "hpnicfDHCPROption82Switch": hpnicfDHCPROption82Switch,
       "hpnicfDHCPROption82HandleStrategy": hpnicfDHCPROption82HandleStrategy,
       "hpnicfDHCPRConfigOption82IfTable": hpnicfDHCPRConfigOption82IfTable,
       "hpnicfDHCPRConfigOption82IfEntry": hpnicfDHCPRConfigOption82IfEntry,
       "hpnicfDHCPROption82IfSwitch": hpnicfDHCPROption82IfSwitch,
       "hpnicfDHCPROption82IfStrategy": hpnicfDHCPROption82IfStrategy,
       "hpnicfDHCPROption82IfFormat": hpnicfDHCPROption82IfFormat,
       "hpnicfDHCPROption82IfNodeType": hpnicfDHCPROption82IfNodeType,
       "hpnicfDHCPROption82IfUsrDefString": hpnicfDHCPROption82IfUsrDefString}
)
