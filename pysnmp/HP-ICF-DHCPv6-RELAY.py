# SNMP MIB module (HP-ICF-DHCPv6-RELAY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DHCPv6-RELAY
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:20 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfDhcpv6Relay = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50)
)
hpicfDhcpv6Relay.setRevisions(
        ("2014-02-12 00:00",
         "2012-04-24 00:00",
         "2008-04-08 06:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _HpicfDhcpv6RelayAdminStatus_Type(Integer32):
    """Custom type hpicfDhcpv6RelayAdminStatus based on Integer32"""
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


_HpicfDhcpv6RelayAdminStatus_Type.__name__ = "Integer32"
_HpicfDhcpv6RelayAdminStatus_Object = MibScalar
hpicfDhcpv6RelayAdminStatus = _HpicfDhcpv6RelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 1),
    _HpicfDhcpv6RelayAdminStatus_Type()
)
hpicfDhcpv6RelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv6RelayAdminStatus.setStatus("current")
_HpicfDhcpRelayHelperAddressTable_Object = MibTable
hpicfDhcpRelayHelperAddressTable = _HpicfDhcpRelayHelperAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2)
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayHelperAddressTable.setStatus("current")
_HpicfDhcpRelayHelperAddressEntry_Object = MibTableRow
hpicfDhcpRelayHelperAddressEntry = _HpicfDhcpRelayHelperAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1)
)
hpicfDhcpRelayHelperAddressEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressType"),
    (0, "HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddress"),
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayHelperAddressEntry.setStatus("current")
_HpicfDhcpRelayHelperAddressType_Type = InetAddressType
_HpicfDhcpRelayHelperAddressType_Object = MibTableColumn
hpicfDhcpRelayHelperAddressType = _HpicfDhcpRelayHelperAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 1),
    _HpicfDhcpRelayHelperAddressType_Type()
)
hpicfDhcpRelayHelperAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpRelayHelperAddressType.setStatus("current")
_HpicfDhcpRelayHelperAddress_Type = InetAddress
_HpicfDhcpRelayHelperAddress_Object = MibTableColumn
hpicfDhcpRelayHelperAddress = _HpicfDhcpRelayHelperAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 2),
    _HpicfDhcpRelayHelperAddress_Type()
)
hpicfDhcpRelayHelperAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDhcpRelayHelperAddress.setStatus("current")


class _HpicfDhcpRelayHelperAddressEgressInterface_Type(InterfaceIndex):
    """Custom type hpicfDhcpRelayHelperAddressEgressInterface based on InterfaceIndex"""
    defaultValue = 0


_HpicfDhcpRelayHelperAddressEgressInterface_Object = MibTableColumn
hpicfDhcpRelayHelperAddressEgressInterface = _HpicfDhcpRelayHelperAddressEgressInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 3),
    _HpicfDhcpRelayHelperAddressEgressInterface_Type()
)
hpicfDhcpRelayHelperAddressEgressInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpRelayHelperAddressEgressInterface.setStatus("current")
_HpicfDhcpRelayHelperAddressStatus_Type = RowStatus
_HpicfDhcpRelayHelperAddressStatus_Object = MibTableColumn
hpicfDhcpRelayHelperAddressStatus = _HpicfDhcpRelayHelperAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 2, 1, 4),
    _HpicfDhcpRelayHelperAddressStatus_Type()
)
hpicfDhcpRelayHelperAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDhcpRelayHelperAddressStatus.setStatus("current")
_HpicfDhcpRelayPerInterfaceStatsTable_Object = MibTable
hpicfDhcpRelayPerInterfaceStatsTable = _HpicfDhcpRelayPerInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3)
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceStatsTable.setStatus("current")
_HpicfDhcpRelayPerInterfaceStatsEntry_Object = MibTableRow
hpicfDhcpRelayPerInterfaceStatsEntry = _HpicfDhcpRelayPerInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1)
)
hpicfDhcpRelayPerInterfaceStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceStatsEntry.setStatus("current")
_HpicfDhcpRelayPerInterfaceClientPktsRecd_Type = Counter32
_HpicfDhcpRelayPerInterfaceClientPktsRecd_Object = MibTableColumn
hpicfDhcpRelayPerInterfaceClientPktsRecd = _HpicfDhcpRelayPerInterfaceClientPktsRecd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 1),
    _HpicfDhcpRelayPerInterfaceClientPktsRecd_Type()
)
hpicfDhcpRelayPerInterfaceClientPktsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceClientPktsRecd.setStatus("current")
_HpicfDhcpRelayPerInterfaceClientPktsDropped_Type = Counter32
_HpicfDhcpRelayPerInterfaceClientPktsDropped_Object = MibTableColumn
hpicfDhcpRelayPerInterfaceClientPktsDropped = _HpicfDhcpRelayPerInterfaceClientPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 2),
    _HpicfDhcpRelayPerInterfaceClientPktsDropped_Type()
)
hpicfDhcpRelayPerInterfaceClientPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceClientPktsDropped.setStatus("current")
_HpicfDhcpRelayPerInterfaceClientPktsXmitFail_Type = Counter32
_HpicfDhcpRelayPerInterfaceClientPktsXmitFail_Object = MibTableColumn
hpicfDhcpRelayPerInterfaceClientPktsXmitFail = _HpicfDhcpRelayPerInterfaceClientPktsXmitFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 3),
    _HpicfDhcpRelayPerInterfaceClientPktsXmitFail_Type()
)
hpicfDhcpRelayPerInterfaceClientPktsXmitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceClientPktsXmitFail.setStatus("current")
_HpicfDhcpRelayPerInterfaceServerPktsRecd_Type = Counter32
_HpicfDhcpRelayPerInterfaceServerPktsRecd_Object = MibTableColumn
hpicfDhcpRelayPerInterfaceServerPktsRecd = _HpicfDhcpRelayPerInterfaceServerPktsRecd_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 4),
    _HpicfDhcpRelayPerInterfaceServerPktsRecd_Type()
)
hpicfDhcpRelayPerInterfaceServerPktsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceServerPktsRecd.setStatus("current")
_HpicfDhcpRelayPerInterfaceServerPktsDropped_Type = Counter32
_HpicfDhcpRelayPerInterfaceServerPktsDropped_Object = MibTableColumn
hpicfDhcpRelayPerInterfaceServerPktsDropped = _HpicfDhcpRelayPerInterfaceServerPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 5),
    _HpicfDhcpRelayPerInterfaceServerPktsDropped_Type()
)
hpicfDhcpRelayPerInterfaceServerPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceServerPktsDropped.setStatus("current")
_HpicfDhcpRelayPerInterfaceServerPktsXmitFail_Type = Counter32
_HpicfDhcpRelayPerInterfaceServerPktsXmitFail_Object = MibTableColumn
hpicfDhcpRelayPerInterfaceServerPktsXmitFail = _HpicfDhcpRelayPerInterfaceServerPktsXmitFail_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 3, 1, 6),
    _HpicfDhcpRelayPerInterfaceServerPktsXmitFail_Type()
)
hpicfDhcpRelayPerInterfaceServerPktsXmitFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayPerInterfaceServerPktsXmitFail.setStatus("current")
_HpicfDhcpRelayConformance_ObjectIdentity = ObjectIdentity
hpicfDhcpRelayConformance = _HpicfDhcpRelayConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4)
)
_HpicfDhcpRelayGroups_ObjectIdentity = ObjectIdentity
hpicfDhcpRelayGroups = _HpicfDhcpRelayGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1)
)
_HpicfDhcpRelayCompliances_ObjectIdentity = ObjectIdentity
hpicfDhcpRelayCompliances = _HpicfDhcpRelayCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2)
)
_HpicfDhcpRelayGlobalStatistics_ObjectIdentity = ObjectIdentity
hpicfDhcpRelayGlobalStatistics = _HpicfDhcpRelayGlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5)
)
_HpicfDhcpRelayPktsDropped_Type = Counter32
_HpicfDhcpRelayPktsDropped_Object = MibScalar
hpicfDhcpRelayPktsDropped = _HpicfDhcpRelayPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 1),
    _HpicfDhcpRelayPktsDropped_Type()
)
hpicfDhcpRelayPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayPktsDropped.setStatus("current")
_HpicfDhcpRelayErrorPktsDropped_Type = Counter32
_HpicfDhcpRelayErrorPktsDropped_Object = MibScalar
hpicfDhcpRelayErrorPktsDropped = _HpicfDhcpRelayErrorPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 2),
    _HpicfDhcpRelayErrorPktsDropped_Type()
)
hpicfDhcpRelayErrorPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayErrorPktsDropped.setStatus("current")
_HpicfDhcpRelayTotalPktsReceived_Type = Counter32
_HpicfDhcpRelayTotalPktsReceived_Object = MibScalar
hpicfDhcpRelayTotalPktsReceived = _HpicfDhcpRelayTotalPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 3),
    _HpicfDhcpRelayTotalPktsReceived_Type()
)
hpicfDhcpRelayTotalPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayTotalPktsReceived.setStatus("current")
_HpicfDhcpRelaySolicitPktsReceived_Type = Counter32
_HpicfDhcpRelaySolicitPktsReceived_Object = MibScalar
hpicfDhcpRelaySolicitPktsReceived = _HpicfDhcpRelaySolicitPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 4),
    _HpicfDhcpRelaySolicitPktsReceived_Type()
)
hpicfDhcpRelaySolicitPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelaySolicitPktsReceived.setStatus("current")
_HpicfDhcpRelayRequestPktsReceived_Type = Counter32
_HpicfDhcpRelayRequestPktsReceived_Object = MibScalar
hpicfDhcpRelayRequestPktsReceived = _HpicfDhcpRelayRequestPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 5),
    _HpicfDhcpRelayRequestPktsReceived_Type()
)
hpicfDhcpRelayRequestPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayRequestPktsReceived.setStatus("current")
_HpicfDhcpRelayConfirmPktsReceived_Type = Counter32
_HpicfDhcpRelayConfirmPktsReceived_Object = MibScalar
hpicfDhcpRelayConfirmPktsReceived = _HpicfDhcpRelayConfirmPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 6),
    _HpicfDhcpRelayConfirmPktsReceived_Type()
)
hpicfDhcpRelayConfirmPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayConfirmPktsReceived.setStatus("current")
_HpicfDhcpRelayRenewPktsReceived_Type = Counter32
_HpicfDhcpRelayRenewPktsReceived_Object = MibScalar
hpicfDhcpRelayRenewPktsReceived = _HpicfDhcpRelayRenewPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 7),
    _HpicfDhcpRelayRenewPktsReceived_Type()
)
hpicfDhcpRelayRenewPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayRenewPktsReceived.setStatus("current")
_HpicfDhcpRelayRebindPktsReceived_Type = Counter32
_HpicfDhcpRelayRebindPktsReceived_Object = MibScalar
hpicfDhcpRelayRebindPktsReceived = _HpicfDhcpRelayRebindPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 8),
    _HpicfDhcpRelayRebindPktsReceived_Type()
)
hpicfDhcpRelayRebindPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayRebindPktsReceived.setStatus("current")
_HpicfDhcpRelayReleasePktsReceived_Type = Counter32
_HpicfDhcpRelayReleasePktsReceived_Object = MibScalar
hpicfDhcpRelayReleasePktsReceived = _HpicfDhcpRelayReleasePktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 9),
    _HpicfDhcpRelayReleasePktsReceived_Type()
)
hpicfDhcpRelayReleasePktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayReleasePktsReceived.setStatus("current")
_HpicfDhcpRelayDeclinePktsReceived_Type = Counter32
_HpicfDhcpRelayDeclinePktsReceived_Object = MibScalar
hpicfDhcpRelayDeclinePktsReceived = _HpicfDhcpRelayDeclinePktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 10),
    _HpicfDhcpRelayDeclinePktsReceived_Type()
)
hpicfDhcpRelayDeclinePktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayDeclinePktsReceived.setStatus("current")
_HpicfDhcpRelayInformationReqPktsReceived_Type = Counter32
_HpicfDhcpRelayInformationReqPktsReceived_Object = MibScalar
hpicfDhcpRelayInformationReqPktsReceived = _HpicfDhcpRelayInformationReqPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 11),
    _HpicfDhcpRelayInformationReqPktsReceived_Type()
)
hpicfDhcpRelayInformationReqPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayInformationReqPktsReceived.setStatus("current")
_HpicfDhcpRelayRelayForwardPktsReceived_Type = Counter32
_HpicfDhcpRelayRelayForwardPktsReceived_Object = MibScalar
hpicfDhcpRelayRelayForwardPktsReceived = _HpicfDhcpRelayRelayForwardPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 12),
    _HpicfDhcpRelayRelayForwardPktsReceived_Type()
)
hpicfDhcpRelayRelayForwardPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayRelayForwardPktsReceived.setStatus("current")
_HpicfDhcpRelayRelayReplyPktsReceived_Type = Counter32
_HpicfDhcpRelayRelayReplyPktsReceived_Object = MibScalar
hpicfDhcpRelayRelayReplyPktsReceived = _HpicfDhcpRelayRelayReplyPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 13),
    _HpicfDhcpRelayRelayReplyPktsReceived_Type()
)
hpicfDhcpRelayRelayReplyPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayRelayReplyPktsReceived.setStatus("current")
_HpicfDhcpRelayTotalPktsSent_Type = Counter32
_HpicfDhcpRelayTotalPktsSent_Object = MibScalar
hpicfDhcpRelayTotalPktsSent = _HpicfDhcpRelayTotalPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 14),
    _HpicfDhcpRelayTotalPktsSent_Type()
)
hpicfDhcpRelayTotalPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayTotalPktsSent.setStatus("current")
_HpicfDhcpRelayAdvertisePktsSent_Type = Counter32
_HpicfDhcpRelayAdvertisePktsSent_Object = MibScalar
hpicfDhcpRelayAdvertisePktsSent = _HpicfDhcpRelayAdvertisePktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 15),
    _HpicfDhcpRelayAdvertisePktsSent_Type()
)
hpicfDhcpRelayAdvertisePktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayAdvertisePktsSent.setStatus("current")
_HpicfDhcpRelayReconfigurePktsSent_Type = Counter32
_HpicfDhcpRelayReconfigurePktsSent_Object = MibScalar
hpicfDhcpRelayReconfigurePktsSent = _HpicfDhcpRelayReconfigurePktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 16),
    _HpicfDhcpRelayReconfigurePktsSent_Type()
)
hpicfDhcpRelayReconfigurePktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayReconfigurePktsSent.setStatus("current")
_HpicfDhcpRelayReplyPktsSent_Type = Counter32
_HpicfDhcpRelayReplyPktsSent_Object = MibScalar
hpicfDhcpRelayReplyPktsSent = _HpicfDhcpRelayReplyPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 17),
    _HpicfDhcpRelayReplyPktsSent_Type()
)
hpicfDhcpRelayReplyPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayReplyPktsSent.setStatus("current")
_HpicfDhcpRelayRelayForwardPktsSent_Type = Counter32
_HpicfDhcpRelayRelayForwardPktsSent_Object = MibScalar
hpicfDhcpRelayRelayForwardPktsSent = _HpicfDhcpRelayRelayForwardPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 18),
    _HpicfDhcpRelayRelayForwardPktsSent_Type()
)
hpicfDhcpRelayRelayForwardPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayRelayForwardPktsSent.setStatus("current")
_HpicfDhcpRelayRelayReplyPktsSent_Type = Counter32
_HpicfDhcpRelayRelayReplyPktsSent_Object = MibScalar
hpicfDhcpRelayRelayReplyPktsSent = _HpicfDhcpRelayRelayReplyPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 5, 19),
    _HpicfDhcpRelayRelayReplyPktsSent_Type()
)
hpicfDhcpRelayRelayReplyPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDhcpRelayRelayReplyPktsSent.setStatus("current")
_HpicfDhcpv6RelayOptions_ObjectIdentity = ObjectIdentity
hpicfDhcpv6RelayOptions = _HpicfDhcpv6RelayOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 6)
)


class _HpicfDhcpv6RelayOption79Status_Type(Integer32):
    """Custom type hpicfDhcpv6RelayOption79Status based on Integer32"""
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


_HpicfDhcpv6RelayOption79Status_Type.__name__ = "Integer32"
_HpicfDhcpv6RelayOption79Status_Object = MibScalar
hpicfDhcpv6RelayOption79Status = _HpicfDhcpv6RelayOption79Status_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 6, 1),
    _HpicfDhcpv6RelayOption79Status_Type()
)
hpicfDhcpv6RelayOption79Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDhcpv6RelayOption79Status.setStatus("current")

# Managed Objects groups

hpicfDhcpRelayConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 1)
)
hpicfDhcpRelayConfigGroup.setObjects(
      *(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpv6RelayAdminStatus"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressEgressInterface"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressStatus"))
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayConfigGroup.setStatus("deprecated")

hpicfDhcpRelayStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 2)
)
hpicfDhcpRelayStatsGroup.setObjects(
      *(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsRecd"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsDropped"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsXmitFail"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsRecd"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsDropped"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsXmitFail"))
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayStatsGroup.setStatus("deprecated")

hpicfDhcpRelayStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 3)
)
hpicfDhcpRelayStatsGroup1.setObjects(
      *(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsRecd"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsDropped"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceClientPktsXmitFail"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsRecd"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsDropped"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPerInterfaceServerPktsXmitFail"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayPktsDropped"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayErrorPktsDropped"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayTotalPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelaySolicitPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRequestPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayConfirmPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRenewPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRebindPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayReleasePktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayDeclinePktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayInformationReqPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayForwardPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayReplyPktsReceived"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayTotalPktsSent"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayAdvertisePktsSent"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayReconfigurePktsSent"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayReplyPktsSent"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayForwardPktsSent"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayRelayReplyPktsSent"))
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayStatsGroup1.setStatus("current")

hpicfDhcpRelayConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 1, 4)
)
hpicfDhcpRelayConfigGroup1.setObjects(
      *(("HP-ICF-DHCPv6-RELAY", "hpicfDhcpv6RelayAdminStatus"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressEgressInterface"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpRelayHelperAddressStatus"),
        ("HP-ICF-DHCPv6-RELAY", "hpicfDhcpv6RelayOption79Status"))
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDhcpRelayCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayCompliance.setStatus(
        "deprecated"
    )

hpicfDhcpRelayCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayCompliance1.setStatus(
        "deprecated"
    )

hpicfDhcpRelayCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 50, 4, 2, 3)
)
if mibBuilder.loadTexts:
    hpicfDhcpRelayCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DHCPv6-RELAY",
    **{"hpicfDhcpv6Relay": hpicfDhcpv6Relay,
       "hpicfDhcpv6RelayAdminStatus": hpicfDhcpv6RelayAdminStatus,
       "hpicfDhcpRelayHelperAddressTable": hpicfDhcpRelayHelperAddressTable,
       "hpicfDhcpRelayHelperAddressEntry": hpicfDhcpRelayHelperAddressEntry,
       "hpicfDhcpRelayHelperAddressType": hpicfDhcpRelayHelperAddressType,
       "hpicfDhcpRelayHelperAddress": hpicfDhcpRelayHelperAddress,
       "hpicfDhcpRelayHelperAddressEgressInterface": hpicfDhcpRelayHelperAddressEgressInterface,
       "hpicfDhcpRelayHelperAddressStatus": hpicfDhcpRelayHelperAddressStatus,
       "hpicfDhcpRelayPerInterfaceStatsTable": hpicfDhcpRelayPerInterfaceStatsTable,
       "hpicfDhcpRelayPerInterfaceStatsEntry": hpicfDhcpRelayPerInterfaceStatsEntry,
       "hpicfDhcpRelayPerInterfaceClientPktsRecd": hpicfDhcpRelayPerInterfaceClientPktsRecd,
       "hpicfDhcpRelayPerInterfaceClientPktsDropped": hpicfDhcpRelayPerInterfaceClientPktsDropped,
       "hpicfDhcpRelayPerInterfaceClientPktsXmitFail": hpicfDhcpRelayPerInterfaceClientPktsXmitFail,
       "hpicfDhcpRelayPerInterfaceServerPktsRecd": hpicfDhcpRelayPerInterfaceServerPktsRecd,
       "hpicfDhcpRelayPerInterfaceServerPktsDropped": hpicfDhcpRelayPerInterfaceServerPktsDropped,
       "hpicfDhcpRelayPerInterfaceServerPktsXmitFail": hpicfDhcpRelayPerInterfaceServerPktsXmitFail,
       "hpicfDhcpRelayConformance": hpicfDhcpRelayConformance,
       "hpicfDhcpRelayGroups": hpicfDhcpRelayGroups,
       "hpicfDhcpRelayConfigGroup": hpicfDhcpRelayConfigGroup,
       "hpicfDhcpRelayStatsGroup": hpicfDhcpRelayStatsGroup,
       "hpicfDhcpRelayStatsGroup1": hpicfDhcpRelayStatsGroup1,
       "hpicfDhcpRelayConfigGroup1": hpicfDhcpRelayConfigGroup1,
       "hpicfDhcpRelayCompliances": hpicfDhcpRelayCompliances,
       "hpicfDhcpRelayCompliance": hpicfDhcpRelayCompliance,
       "hpicfDhcpRelayCompliance1": hpicfDhcpRelayCompliance1,
       "hpicfDhcpRelayCompliance2": hpicfDhcpRelayCompliance2,
       "hpicfDhcpRelayGlobalStatistics": hpicfDhcpRelayGlobalStatistics,
       "hpicfDhcpRelayPktsDropped": hpicfDhcpRelayPktsDropped,
       "hpicfDhcpRelayErrorPktsDropped": hpicfDhcpRelayErrorPktsDropped,
       "hpicfDhcpRelayTotalPktsReceived": hpicfDhcpRelayTotalPktsReceived,
       "hpicfDhcpRelaySolicitPktsReceived": hpicfDhcpRelaySolicitPktsReceived,
       "hpicfDhcpRelayRequestPktsReceived": hpicfDhcpRelayRequestPktsReceived,
       "hpicfDhcpRelayConfirmPktsReceived": hpicfDhcpRelayConfirmPktsReceived,
       "hpicfDhcpRelayRenewPktsReceived": hpicfDhcpRelayRenewPktsReceived,
       "hpicfDhcpRelayRebindPktsReceived": hpicfDhcpRelayRebindPktsReceived,
       "hpicfDhcpRelayReleasePktsReceived": hpicfDhcpRelayReleasePktsReceived,
       "hpicfDhcpRelayDeclinePktsReceived": hpicfDhcpRelayDeclinePktsReceived,
       "hpicfDhcpRelayInformationReqPktsReceived": hpicfDhcpRelayInformationReqPktsReceived,
       "hpicfDhcpRelayRelayForwardPktsReceived": hpicfDhcpRelayRelayForwardPktsReceived,
       "hpicfDhcpRelayRelayReplyPktsReceived": hpicfDhcpRelayRelayReplyPktsReceived,
       "hpicfDhcpRelayTotalPktsSent": hpicfDhcpRelayTotalPktsSent,
       "hpicfDhcpRelayAdvertisePktsSent": hpicfDhcpRelayAdvertisePktsSent,
       "hpicfDhcpRelayReconfigurePktsSent": hpicfDhcpRelayReconfigurePktsSent,
       "hpicfDhcpRelayReplyPktsSent": hpicfDhcpRelayReplyPktsSent,
       "hpicfDhcpRelayRelayForwardPktsSent": hpicfDhcpRelayRelayForwardPktsSent,
       "hpicfDhcpRelayRelayReplyPktsSent": hpicfDhcpRelayRelayReplyPktsSent,
       "hpicfDhcpv6RelayOptions": hpicfDhcpv6RelayOptions,
       "hpicfDhcpv6RelayOption79Status": hpicfDhcpv6RelayOption79Status}
)
