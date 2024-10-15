# SNMP MIB module (JUNIPER-JDHCPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JDHCPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:14 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

(jnxJdhcpv6MibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJdhcpv6MibRoot")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jnxJdhcpv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62)
)
jnxJdhcpv6MIB.setRevisions(
        ("2011-03-15 00:00",
         "2011-01-25 00:00",
         "2010-02-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJdhcpv6Objects_ObjectIdentity = ObjectIdentity
jnxJdhcpv6Objects = _JnxJdhcpv6Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 1)
)
_JnxJdhcpv6LocalServerObjects_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerObjects = _JnxJdhcpv6LocalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2)
)
_JnxJdhcpv6LocalServerStatistics_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerStatistics = _JnxJdhcpv6LocalServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1)
)
_JnxJdhcpv6LocalServerTotalDropped_Type = Counter32
_JnxJdhcpv6LocalServerTotalDropped_Object = MibScalar
jnxJdhcpv6LocalServerTotalDropped = _JnxJdhcpv6LocalServerTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 1),
    _JnxJdhcpv6LocalServerTotalDropped_Type()
)
jnxJdhcpv6LocalServerTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerTotalDropped.setStatus("current")
_JnxJdhcpv6LocalServerNoSafdDropped_Type = Counter32
_JnxJdhcpv6LocalServerNoSafdDropped_Object = MibScalar
jnxJdhcpv6LocalServerNoSafdDropped = _JnxJdhcpv6LocalServerNoSafdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 2),
    _JnxJdhcpv6LocalServerNoSafdDropped_Type()
)
jnxJdhcpv6LocalServerNoSafdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerNoSafdDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadSendDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadSendDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadSendDropped = _JnxJdhcpv6LocalServerBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 3),
    _JnxJdhcpv6LocalServerBadSendDropped_Type()
)
jnxJdhcpv6LocalServerBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadSendDropped.setStatus("current")
_JnxJdhcpv6LocalServerShortPacketDropped_Type = Counter32
_JnxJdhcpv6LocalServerShortPacketDropped_Object = MibScalar
jnxJdhcpv6LocalServerShortPacketDropped = _JnxJdhcpv6LocalServerShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 4),
    _JnxJdhcpv6LocalServerShortPacketDropped_Type()
)
jnxJdhcpv6LocalServerShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerShortPacketDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadMsgtypeDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadMsgtypeDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadMsgtypeDropped = _JnxJdhcpv6LocalServerBadMsgtypeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 5),
    _JnxJdhcpv6LocalServerBadMsgtypeDropped_Type()
)
jnxJdhcpv6LocalServerBadMsgtypeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadMsgtypeDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadOptionsDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadOptionsDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadOptionsDropped = _JnxJdhcpv6LocalServerBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 6),
    _JnxJdhcpv6LocalServerBadOptionsDropped_Type()
)
jnxJdhcpv6LocalServerBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadOptionsDropped.setStatus("current")
_JnxJdhcpv6LocalServerBadSrcAddressDropped_Type = Counter32
_JnxJdhcpv6LocalServerBadSrcAddressDropped_Object = MibScalar
jnxJdhcpv6LocalServerBadSrcAddressDropped = _JnxJdhcpv6LocalServerBadSrcAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 7),
    _JnxJdhcpv6LocalServerBadSrcAddressDropped_Type()
)
jnxJdhcpv6LocalServerBadSrcAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBadSrcAddressDropped.setStatus("current")
_JnxJdhcpv6LocalServerRelayHopCountDropped_Type = Counter32
_JnxJdhcpv6LocalServerRelayHopCountDropped_Object = MibScalar
jnxJdhcpv6LocalServerRelayHopCountDropped = _JnxJdhcpv6LocalServerRelayHopCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 8),
    _JnxJdhcpv6LocalServerRelayHopCountDropped_Type()
)
jnxJdhcpv6LocalServerRelayHopCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRelayHopCountDropped.setStatus("current")
_JnxJdhcpv6LocalServerNoClientIdDropped_Type = Counter32
_JnxJdhcpv6LocalServerNoClientIdDropped_Object = MibScalar
jnxJdhcpv6LocalServerNoClientIdDropped = _JnxJdhcpv6LocalServerNoClientIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 9),
    _JnxJdhcpv6LocalServerNoClientIdDropped_Type()
)
jnxJdhcpv6LocalServerNoClientIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerNoClientIdDropped.setStatus("current")
_JnxJdhcpv6LocalServerDeclineReceived_Type = Counter32
_JnxJdhcpv6LocalServerDeclineReceived_Object = MibScalar
jnxJdhcpv6LocalServerDeclineReceived = _JnxJdhcpv6LocalServerDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 10),
    _JnxJdhcpv6LocalServerDeclineReceived_Type()
)
jnxJdhcpv6LocalServerDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerDeclineReceived.setStatus("current")
_JnxJdhcpv6LocalServerSolicitReceived_Type = Counter32
_JnxJdhcpv6LocalServerSolicitReceived_Object = MibScalar
jnxJdhcpv6LocalServerSolicitReceived = _JnxJdhcpv6LocalServerSolicitReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 11),
    _JnxJdhcpv6LocalServerSolicitReceived_Type()
)
jnxJdhcpv6LocalServerSolicitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerSolicitReceived.setStatus("current")
_JnxJdhcpv6LocalServerInformationRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerInformationRequestReceived_Object = MibScalar
jnxJdhcpv6LocalServerInformationRequestReceived = _JnxJdhcpv6LocalServerInformationRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 12),
    _JnxJdhcpv6LocalServerInformationRequestReceived_Type()
)
jnxJdhcpv6LocalServerInformationRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInformationRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerReleaseReceived_Type = Counter32
_JnxJdhcpv6LocalServerReleaseReceived_Object = MibScalar
jnxJdhcpv6LocalServerReleaseReceived = _JnxJdhcpv6LocalServerReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 13),
    _JnxJdhcpv6LocalServerReleaseReceived_Type()
)
jnxJdhcpv6LocalServerReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerReleaseReceived.setStatus("current")
_JnxJdhcpv6LocalServerRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerRequestReceived_Object = MibScalar
jnxJdhcpv6LocalServerRequestReceived = _JnxJdhcpv6LocalServerRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 14),
    _JnxJdhcpv6LocalServerRequestReceived_Type()
)
jnxJdhcpv6LocalServerRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerConfirmReceived_Type = Counter32
_JnxJdhcpv6LocalServerConfirmReceived_Object = MibScalar
jnxJdhcpv6LocalServerConfirmReceived = _JnxJdhcpv6LocalServerConfirmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 15),
    _JnxJdhcpv6LocalServerConfirmReceived_Type()
)
jnxJdhcpv6LocalServerConfirmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerConfirmReceived.setStatus("current")
_JnxJdhcpv6LocalServerRenewReceived_Type = Counter32
_JnxJdhcpv6LocalServerRenewReceived_Object = MibScalar
jnxJdhcpv6LocalServerRenewReceived = _JnxJdhcpv6LocalServerRenewReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 16),
    _JnxJdhcpv6LocalServerRenewReceived_Type()
)
jnxJdhcpv6LocalServerRenewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRenewReceived.setStatus("current")
_JnxJdhcpv6LocalServerRebindReceived_Type = Counter32
_JnxJdhcpv6LocalServerRebindReceived_Object = MibScalar
jnxJdhcpv6LocalServerRebindReceived = _JnxJdhcpv6LocalServerRebindReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 17),
    _JnxJdhcpv6LocalServerRebindReceived_Type()
)
jnxJdhcpv6LocalServerRebindReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRebindReceived.setStatus("current")
_JnxJdhcpv6LocalServerRelayForwReceived_Type = Counter32
_JnxJdhcpv6LocalServerRelayForwReceived_Object = MibScalar
jnxJdhcpv6LocalServerRelayForwReceived = _JnxJdhcpv6LocalServerRelayForwReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 18),
    _JnxJdhcpv6LocalServerRelayForwReceived_Type()
)
jnxJdhcpv6LocalServerRelayForwReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRelayForwReceived.setStatus("current")
_JnxJdhcpv6LocalServerRelayReplReceived_Type = Counter32
_JnxJdhcpv6LocalServerRelayReplReceived_Object = MibScalar
jnxJdhcpv6LocalServerRelayReplReceived = _JnxJdhcpv6LocalServerRelayReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 19),
    _JnxJdhcpv6LocalServerRelayReplReceived_Type()
)
jnxJdhcpv6LocalServerRelayReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerRelayReplReceived.setStatus("current")
_JnxJdhcpv6LocalServerAdvertiseSent_Type = Counter32
_JnxJdhcpv6LocalServerAdvertiseSent_Object = MibScalar
jnxJdhcpv6LocalServerAdvertiseSent = _JnxJdhcpv6LocalServerAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 20),
    _JnxJdhcpv6LocalServerAdvertiseSent_Type()
)
jnxJdhcpv6LocalServerAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerAdvertiseSent.setStatus("current")
_JnxJdhcpv6LocalServerReplySent_Type = Counter32
_JnxJdhcpv6LocalServerReplySent_Object = MibScalar
jnxJdhcpv6LocalServerReplySent = _JnxJdhcpv6LocalServerReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 21),
    _JnxJdhcpv6LocalServerReplySent_Type()
)
jnxJdhcpv6LocalServerReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerReplySent.setStatus("current")
_JnxJdhcpv6LocalServerReconfigureSent_Type = Counter32
_JnxJdhcpv6LocalServerReconfigureSent_Object = MibScalar
jnxJdhcpv6LocalServerReconfigureSent = _JnxJdhcpv6LocalServerReconfigureSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 22),
    _JnxJdhcpv6LocalServerReconfigureSent_Type()
)
jnxJdhcpv6LocalServerReconfigureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerReconfigureSent.setStatus("current")
_JnxJdhcpv6LocalServerTotalLeaseCount_Type = Counter32
_JnxJdhcpv6LocalServerTotalLeaseCount_Object = MibScalar
jnxJdhcpv6LocalServerTotalLeaseCount = _JnxJdhcpv6LocalServerTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 1, 23),
    _JnxJdhcpv6LocalServerTotalLeaseCount_Type()
)
jnxJdhcpv6LocalServerTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerTotalLeaseCount.setStatus("current")
_JnxJdhcpv6LocalServerBindings_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerBindings = _JnxJdhcpv6LocalServerBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2)
)
_JnxJdhcpv6LocalServerBindingsTable_Object = MibTable
jnxJdhcpv6LocalServerBindingsTable = _JnxJdhcpv6LocalServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsTable.setStatus("current")
_JnxJdhcpv6LocalServerBindingsEntry_Object = MibTableRow
jnxJdhcpv6LocalServerBindingsEntry = _JnxJdhcpv6LocalServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1)
)
jnxJdhcpv6LocalServerBindingsEntry.setIndexNames(
    (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerBindingsPrefix"),
    (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerBindingsLength"),
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsEntry.setStatus("current")
_JnxJdhcpv6LocalServerBindingsPrefix_Type = Ipv6AddressPrefix
_JnxJdhcpv6LocalServerBindingsPrefix_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsPrefix = _JnxJdhcpv6LocalServerBindingsPrefix_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 1),
    _JnxJdhcpv6LocalServerBindingsPrefix_Type()
)
jnxJdhcpv6LocalServerBindingsPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsPrefix.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLength_Type = Unsigned32
_JnxJdhcpv6LocalServerBindingsLength_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLength = _JnxJdhcpv6LocalServerBindingsLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 2),
    _JnxJdhcpv6LocalServerBindingsLength_Type()
)
jnxJdhcpv6LocalServerBindingsLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLength.setStatus("current")
_JnxJdhcpv6LocalServerBindingsState_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsState_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsState = _JnxJdhcpv6LocalServerBindingsState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 3),
    _JnxJdhcpv6LocalServerBindingsState_Type()
)
jnxJdhcpv6LocalServerBindingsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsState.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLeaseEndTime_Type = DateAndTime
_JnxJdhcpv6LocalServerBindingsLeaseEndTime_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLeaseEndTime = _JnxJdhcpv6LocalServerBindingsLeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 4),
    _JnxJdhcpv6LocalServerBindingsLeaseEndTime_Type()
)
jnxJdhcpv6LocalServerBindingsLeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLeaseEndTime.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Type = Unsigned32
_JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLeaseExpireTime = _JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 5),
    _JnxJdhcpv6LocalServerBindingsLeaseExpireTime_Type()
)
jnxJdhcpv6LocalServerBindingsLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLeaseExpireTime.setStatus("current")
_JnxJdhcpv6LocalServerBindingsLeaseStartTime_Type = DateAndTime
_JnxJdhcpv6LocalServerBindingsLeaseStartTime_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsLeaseStartTime = _JnxJdhcpv6LocalServerBindingsLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 6),
    _JnxJdhcpv6LocalServerBindingsLeaseStartTime_Type()
)
jnxJdhcpv6LocalServerBindingsLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsLeaseStartTime.setStatus("current")
_JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsIncomingClientInterface = _JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 7),
    _JnxJdhcpv6LocalServerBindingsIncomingClientInterface_Type()
)
jnxJdhcpv6LocalServerBindingsIncomingClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsIncomingClientInterface.setStatus("current")
_JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Type = Unsigned32
_JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId = _JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 8),
    _JnxJdhcpv6LocalServerBindingsClientInterfaceVlanId_Type()
)
jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId.setStatus("current")
_JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsDemuxInterfaceName = _JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 9),
    _JnxJdhcpv6LocalServerBindingsDemuxInterfaceName_Type()
)
jnxJdhcpv6LocalServerBindingsDemuxInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsDemuxInterfaceName.setStatus("current")
_JnxJdhcpv6LocalServerBindingsServerIpAddress_Type = IpAddress
_JnxJdhcpv6LocalServerBindingsServerIpAddress_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsServerIpAddress = _JnxJdhcpv6LocalServerBindingsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 10),
    _JnxJdhcpv6LocalServerBindingsServerIpAddress_Type()
)
jnxJdhcpv6LocalServerBindingsServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsServerIpAddress.setStatus("current")
_JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Type = IpAddress
_JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsBootpRelayAddress = _JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 11),
    _JnxJdhcpv6LocalServerBindingsBootpRelayAddress_Type()
)
jnxJdhcpv6LocalServerBindingsBootpRelayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsBootpRelayAddress.setStatus("current")
_JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Type = IpAddress
_JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress = _JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 12),
    _JnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress_Type()
)
jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress.setStatus("current")
_JnxJdhcpv6LocalServerBindingsClientPoolName_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsClientPoolName_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsClientPoolName = _JnxJdhcpv6LocalServerBindingsClientPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 13),
    _JnxJdhcpv6LocalServerBindingsClientPoolName_Type()
)
jnxJdhcpv6LocalServerBindingsClientPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsClientPoolName.setStatus("current")
_JnxJdhcpv6LocalServerBindingsClientProfileName_Type = DisplayString
_JnxJdhcpv6LocalServerBindingsClientProfileName_Object = MibTableColumn
jnxJdhcpv6LocalServerBindingsClientProfileName = _JnxJdhcpv6LocalServerBindingsClientProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 2, 1, 1, 14),
    _JnxJdhcpv6LocalServerBindingsClientProfileName_Type()
)
jnxJdhcpv6LocalServerBindingsClientProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerBindingsClientProfileName.setStatus("current")
_JnxJdhcpv6LocalServerTraps_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerTraps = _JnxJdhcpv6LocalServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3)
)
_JnxJdhcpv6LocalServerTrapVars_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerTrapVars = _JnxJdhcpv6LocalServerTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4)
)
_JnxJdhcpv6RouterName_Type = DisplayString
_JnxJdhcpv6RouterName_Object = MibScalar
jnxJdhcpv6RouterName = _JnxJdhcpv6RouterName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 1),
    _JnxJdhcpv6RouterName_Type()
)
jnxJdhcpv6RouterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6RouterName.setStatus("current")
_JnxJdhcpv6LocalServerInterfaceName_Type = DisplayString
_JnxJdhcpv6LocalServerInterfaceName_Object = MibScalar
jnxJdhcpv6LocalServerInterfaceName = _JnxJdhcpv6LocalServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 2),
    _JnxJdhcpv6LocalServerInterfaceName_Type()
)
jnxJdhcpv6LocalServerInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceName.setStatus("current")
_JnxJdhcpv6LocalServerInterfaceLimit_Type = Unsigned32
_JnxJdhcpv6LocalServerInterfaceLimit_Object = MibScalar
jnxJdhcpv6LocalServerInterfaceLimit = _JnxJdhcpv6LocalServerInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 3),
    _JnxJdhcpv6LocalServerInterfaceLimit_Type()
)
jnxJdhcpv6LocalServerInterfaceLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceLimit.setStatus("current")


class _JnxJdhcpv6LocalServerEventSeverity_Type(Integer32):
    """Custom type jnxJdhcpv6LocalServerEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("debug", 0),
          ("warning", 1))
    )


_JnxJdhcpv6LocalServerEventSeverity_Type.__name__ = "Integer32"
_JnxJdhcpv6LocalServerEventSeverity_Object = MibScalar
jnxJdhcpv6LocalServerEventSeverity = _JnxJdhcpv6LocalServerEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 4),
    _JnxJdhcpv6LocalServerEventSeverity_Type()
)
jnxJdhcpv6LocalServerEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerEventSeverity.setStatus("current")
_JnxJdhcpv6LocalServerEventString_Type = DisplayString
_JnxJdhcpv6LocalServerEventString_Object = MibScalar
jnxJdhcpv6LocalServerEventString = _JnxJdhcpv6LocalServerEventString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 4, 5),
    _JnxJdhcpv6LocalServerEventString_Type()
)
jnxJdhcpv6LocalServerEventString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerEventString.setStatus("current")
_JnxJdhcpv6LocalServerIfcStats_ObjectIdentity = ObjectIdentity
jnxJdhcpv6LocalServerIfcStats = _JnxJdhcpv6LocalServerIfcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5)
)
_JnxJdhcpv6LocalServerIfcStatsTable_Object = MibTable
jnxJdhcpv6LocalServerIfcStatsTable = _JnxJdhcpv6LocalServerIfcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsTable.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsEntry_Object = MibTableRow
jnxJdhcpv6LocalServerIfcStatsEntry = _JnxJdhcpv6LocalServerIfcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1)
)
jnxJdhcpv6LocalServerIfcStatsEntry.setIndexNames(
    (0, "JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerIfcStatsIfIndex"),
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsEntry.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsIfIndex_Type = InterfaceIndex
_JnxJdhcpv6LocalServerIfcStatsIfIndex_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsIfIndex = _JnxJdhcpv6LocalServerIfcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 1),
    _JnxJdhcpv6LocalServerIfcStatsIfIndex_Type()
)
jnxJdhcpv6LocalServerIfcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsIfIndex.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsTotalDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsTotalDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsTotalDropped = _JnxJdhcpv6LocalServerIfcStatsTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 2),
    _JnxJdhcpv6LocalServerIfcStatsTotalDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsTotalDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsNoSafdDropped = _JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 3),
    _JnxJdhcpv6LocalServerIfcStatsNoSafdDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsNoSafdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsNoSafdDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadSendDropped = _JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 4),
    _JnxJdhcpv6LocalServerIfcStatsBadSendDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadSendDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsShortPacketDropped = _JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 5),
    _JnxJdhcpv6LocalServerIfcStatsShortPacketDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsShortPacketDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped = _JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 6),
    _JnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped = _JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 7),
    _JnxJdhcpv6LocalServerIfcStatsBadOptionsDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped = _JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 8),
    _JnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRelayCountDropped = _JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 9),
    _JnxJdhcpv6LocalServerIfcStatsRelayCountDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsRelayCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRelayCountDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped = _JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 10),
    _JnxJdhcpv6LocalServerIfcStatsNoClientIdDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsDeclineReceived = _JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 11),
    _JnxJdhcpv6LocalServerIfcStatsDeclineReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsDeclineReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsSolicitReceived = _JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 12),
    _JnxJdhcpv6LocalServerIfcStatsSolicitReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsSolicitReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsSolicitReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived = _JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 13),
    _JnxJdhcpv6LocalServerIfcStatsInformationRequestReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsReleaseReceived = _JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 14),
    _JnxJdhcpv6LocalServerIfcStatsReleaseReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsReleaseReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRequestReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRequestReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRequestReceived = _JnxJdhcpv6LocalServerIfcStatsRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 15),
    _JnxJdhcpv6LocalServerIfcStatsRequestReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRequestReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsConfirmReceived = _JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 16),
    _JnxJdhcpv6LocalServerIfcStatsConfirmReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsConfirmReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsConfirmReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRenewReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRenewReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRenewReceived = _JnxJdhcpv6LocalServerIfcStatsRenewReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 17),
    _JnxJdhcpv6LocalServerIfcStatsRenewReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRenewReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRenewReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRebindReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRebindReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRebindReceived = _JnxJdhcpv6LocalServerIfcStatsRebindReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 18),
    _JnxJdhcpv6LocalServerIfcStatsRebindReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRebindReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRebindReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRelayForwReceived = _JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 19),
    _JnxJdhcpv6LocalServerIfcStatsRelayForwReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRelayForwReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRelayForwReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsRelayReplReceived = _JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 20),
    _JnxJdhcpv6LocalServerIfcStatsRelayReplReceived_Type()
)
jnxJdhcpv6LocalServerIfcStatsRelayReplReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsRelayReplReceived.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsAdvertiseSent = _JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 21),
    _JnxJdhcpv6LocalServerIfcStatsAdvertiseSent_Type()
)
jnxJdhcpv6LocalServerIfcStatsAdvertiseSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsAdvertiseSent.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsReplySent_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsReplySent_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsReplySent = _JnxJdhcpv6LocalServerIfcStatsReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 22),
    _JnxJdhcpv6LocalServerIfcStatsReplySent_Type()
)
jnxJdhcpv6LocalServerIfcStatsReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsReplySent.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsReconfigureSent = _JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 23),
    _JnxJdhcpv6LocalServerIfcStatsReconfigureSent_Type()
)
jnxJdhcpv6LocalServerIfcStatsReconfigureSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsReconfigureSent.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount = _JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 24),
    _JnxJdhcpv6LocalServerIfcStatsTotalLeaseCount_Type()
)
jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped = _JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 25),
    _JnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped = _JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 26),
    _JnxJdhcpv6LocalServerIfcStatsAuthenticationDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped = _JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 27),
    _JnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped.setStatus("current")
_JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Type = Counter32
_JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Object = MibTableColumn
jnxJdhcpv6LocalServerIfcStatsLicenseDropped = _JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 5, 1, 1, 28),
    _JnxJdhcpv6LocalServerIfcStatsLicenseDropped_Type()
)
jnxJdhcpv6LocalServerIfcStatsLicenseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerIfcStatsLicenseDropped.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJdhcpv6LocalServerInterfaceLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 1)
)
jnxJdhcpv6LocalServerInterfaceLimitExceeded.setObjects(
      *(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceLimitExceeded.setStatus(
        "current"
    )

jnxJdhcpv6LocalServerInterfaceLimitAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 2)
)
jnxJdhcpv6LocalServerInterfaceLimitAbated.setObjects(
      *(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerInterfaceLimitAbated.setStatus(
        "current"
    )

jnxJdhcpv6LocalServerHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 62, 62, 2, 3, 4)
)
jnxJdhcpv6LocalServerHealth.setObjects(
      *(("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6RouterName"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerEventSeverity"),
        ("JUNIPER-JDHCPV6-MIB", "jnxJdhcpv6LocalServerEventString"))
)
if mibBuilder.loadTexts:
    jnxJdhcpv6LocalServerHealth.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JDHCPV6-MIB",
    **{"jnxJdhcpv6MIB": jnxJdhcpv6MIB,
       "jnxJdhcpv6Objects": jnxJdhcpv6Objects,
       "jnxJdhcpv6LocalServerObjects": jnxJdhcpv6LocalServerObjects,
       "jnxJdhcpv6LocalServerStatistics": jnxJdhcpv6LocalServerStatistics,
       "jnxJdhcpv6LocalServerTotalDropped": jnxJdhcpv6LocalServerTotalDropped,
       "jnxJdhcpv6LocalServerNoSafdDropped": jnxJdhcpv6LocalServerNoSafdDropped,
       "jnxJdhcpv6LocalServerBadSendDropped": jnxJdhcpv6LocalServerBadSendDropped,
       "jnxJdhcpv6LocalServerShortPacketDropped": jnxJdhcpv6LocalServerShortPacketDropped,
       "jnxJdhcpv6LocalServerBadMsgtypeDropped": jnxJdhcpv6LocalServerBadMsgtypeDropped,
       "jnxJdhcpv6LocalServerBadOptionsDropped": jnxJdhcpv6LocalServerBadOptionsDropped,
       "jnxJdhcpv6LocalServerBadSrcAddressDropped": jnxJdhcpv6LocalServerBadSrcAddressDropped,
       "jnxJdhcpv6LocalServerRelayHopCountDropped": jnxJdhcpv6LocalServerRelayHopCountDropped,
       "jnxJdhcpv6LocalServerNoClientIdDropped": jnxJdhcpv6LocalServerNoClientIdDropped,
       "jnxJdhcpv6LocalServerDeclineReceived": jnxJdhcpv6LocalServerDeclineReceived,
       "jnxJdhcpv6LocalServerSolicitReceived": jnxJdhcpv6LocalServerSolicitReceived,
       "jnxJdhcpv6LocalServerInformationRequestReceived": jnxJdhcpv6LocalServerInformationRequestReceived,
       "jnxJdhcpv6LocalServerReleaseReceived": jnxJdhcpv6LocalServerReleaseReceived,
       "jnxJdhcpv6LocalServerRequestReceived": jnxJdhcpv6LocalServerRequestReceived,
       "jnxJdhcpv6LocalServerConfirmReceived": jnxJdhcpv6LocalServerConfirmReceived,
       "jnxJdhcpv6LocalServerRenewReceived": jnxJdhcpv6LocalServerRenewReceived,
       "jnxJdhcpv6LocalServerRebindReceived": jnxJdhcpv6LocalServerRebindReceived,
       "jnxJdhcpv6LocalServerRelayForwReceived": jnxJdhcpv6LocalServerRelayForwReceived,
       "jnxJdhcpv6LocalServerRelayReplReceived": jnxJdhcpv6LocalServerRelayReplReceived,
       "jnxJdhcpv6LocalServerAdvertiseSent": jnxJdhcpv6LocalServerAdvertiseSent,
       "jnxJdhcpv6LocalServerReplySent": jnxJdhcpv6LocalServerReplySent,
       "jnxJdhcpv6LocalServerReconfigureSent": jnxJdhcpv6LocalServerReconfigureSent,
       "jnxJdhcpv6LocalServerTotalLeaseCount": jnxJdhcpv6LocalServerTotalLeaseCount,
       "jnxJdhcpv6LocalServerBindings": jnxJdhcpv6LocalServerBindings,
       "jnxJdhcpv6LocalServerBindingsTable": jnxJdhcpv6LocalServerBindingsTable,
       "jnxJdhcpv6LocalServerBindingsEntry": jnxJdhcpv6LocalServerBindingsEntry,
       "jnxJdhcpv6LocalServerBindingsPrefix": jnxJdhcpv6LocalServerBindingsPrefix,
       "jnxJdhcpv6LocalServerBindingsLength": jnxJdhcpv6LocalServerBindingsLength,
       "jnxJdhcpv6LocalServerBindingsState": jnxJdhcpv6LocalServerBindingsState,
       "jnxJdhcpv6LocalServerBindingsLeaseEndTime": jnxJdhcpv6LocalServerBindingsLeaseEndTime,
       "jnxJdhcpv6LocalServerBindingsLeaseExpireTime": jnxJdhcpv6LocalServerBindingsLeaseExpireTime,
       "jnxJdhcpv6LocalServerBindingsLeaseStartTime": jnxJdhcpv6LocalServerBindingsLeaseStartTime,
       "jnxJdhcpv6LocalServerBindingsIncomingClientInterface": jnxJdhcpv6LocalServerBindingsIncomingClientInterface,
       "jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId": jnxJdhcpv6LocalServerBindingsClientInterfaceVlanId,
       "jnxJdhcpv6LocalServerBindingsDemuxInterfaceName": jnxJdhcpv6LocalServerBindingsDemuxInterfaceName,
       "jnxJdhcpv6LocalServerBindingsServerIpAddress": jnxJdhcpv6LocalServerBindingsServerIpAddress,
       "jnxJdhcpv6LocalServerBindingsBootpRelayAddress": jnxJdhcpv6LocalServerBindingsBootpRelayAddress,
       "jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress": jnxJdhcpv6LocalServerBindingsPreviousBootpRelayAddress,
       "jnxJdhcpv6LocalServerBindingsClientPoolName": jnxJdhcpv6LocalServerBindingsClientPoolName,
       "jnxJdhcpv6LocalServerBindingsClientProfileName": jnxJdhcpv6LocalServerBindingsClientProfileName,
       "jnxJdhcpv6LocalServerTraps": jnxJdhcpv6LocalServerTraps,
       "jnxJdhcpv6LocalServerInterfaceLimitExceeded": jnxJdhcpv6LocalServerInterfaceLimitExceeded,
       "jnxJdhcpv6LocalServerInterfaceLimitAbated": jnxJdhcpv6LocalServerInterfaceLimitAbated,
       "jnxJdhcpv6LocalServerHealth": jnxJdhcpv6LocalServerHealth,
       "jnxJdhcpv6LocalServerTrapVars": jnxJdhcpv6LocalServerTrapVars,
       "jnxJdhcpv6RouterName": jnxJdhcpv6RouterName,
       "jnxJdhcpv6LocalServerInterfaceName": jnxJdhcpv6LocalServerInterfaceName,
       "jnxJdhcpv6LocalServerInterfaceLimit": jnxJdhcpv6LocalServerInterfaceLimit,
       "jnxJdhcpv6LocalServerEventSeverity": jnxJdhcpv6LocalServerEventSeverity,
       "jnxJdhcpv6LocalServerEventString": jnxJdhcpv6LocalServerEventString,
       "jnxJdhcpv6LocalServerIfcStats": jnxJdhcpv6LocalServerIfcStats,
       "jnxJdhcpv6LocalServerIfcStatsTable": jnxJdhcpv6LocalServerIfcStatsTable,
       "jnxJdhcpv6LocalServerIfcStatsEntry": jnxJdhcpv6LocalServerIfcStatsEntry,
       "jnxJdhcpv6LocalServerIfcStatsIfIndex": jnxJdhcpv6LocalServerIfcStatsIfIndex,
       "jnxJdhcpv6LocalServerIfcStatsTotalDropped": jnxJdhcpv6LocalServerIfcStatsTotalDropped,
       "jnxJdhcpv6LocalServerIfcStatsNoSafdDropped": jnxJdhcpv6LocalServerIfcStatsNoSafdDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadSendDropped": jnxJdhcpv6LocalServerIfcStatsBadSendDropped,
       "jnxJdhcpv6LocalServerIfcStatsShortPacketDropped": jnxJdhcpv6LocalServerIfcStatsShortPacketDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped": jnxJdhcpv6LocalServerIfcStatsBadMsgtypeDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped": jnxJdhcpv6LocalServerIfcStatsBadOptionsDropped,
       "jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped": jnxJdhcpv6LocalServerIfcStatsBadSrcAddressDropped,
       "jnxJdhcpv6LocalServerIfcStatsRelayCountDropped": jnxJdhcpv6LocalServerIfcStatsRelayCountDropped,
       "jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped": jnxJdhcpv6LocalServerIfcStatsNoClientIdDropped,
       "jnxJdhcpv6LocalServerIfcStatsDeclineReceived": jnxJdhcpv6LocalServerIfcStatsDeclineReceived,
       "jnxJdhcpv6LocalServerIfcStatsSolicitReceived": jnxJdhcpv6LocalServerIfcStatsSolicitReceived,
       "jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived": jnxJdhcpv6LocalServerIfcStatsInformationRequestReceived,
       "jnxJdhcpv6LocalServerIfcStatsReleaseReceived": jnxJdhcpv6LocalServerIfcStatsReleaseReceived,
       "jnxJdhcpv6LocalServerIfcStatsRequestReceived": jnxJdhcpv6LocalServerIfcStatsRequestReceived,
       "jnxJdhcpv6LocalServerIfcStatsConfirmReceived": jnxJdhcpv6LocalServerIfcStatsConfirmReceived,
       "jnxJdhcpv6LocalServerIfcStatsRenewReceived": jnxJdhcpv6LocalServerIfcStatsRenewReceived,
       "jnxJdhcpv6LocalServerIfcStatsRebindReceived": jnxJdhcpv6LocalServerIfcStatsRebindReceived,
       "jnxJdhcpv6LocalServerIfcStatsRelayForwReceived": jnxJdhcpv6LocalServerIfcStatsRelayForwReceived,
       "jnxJdhcpv6LocalServerIfcStatsRelayReplReceived": jnxJdhcpv6LocalServerIfcStatsRelayReplReceived,
       "jnxJdhcpv6LocalServerIfcStatsAdvertiseSent": jnxJdhcpv6LocalServerIfcStatsAdvertiseSent,
       "jnxJdhcpv6LocalServerIfcStatsReplySent": jnxJdhcpv6LocalServerIfcStatsReplySent,
       "jnxJdhcpv6LocalServerIfcStatsReconfigureSent": jnxJdhcpv6LocalServerIfcStatsReconfigureSent,
       "jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount": jnxJdhcpv6LocalServerIfcStatsTotalLeaseCount,
       "jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped": jnxJdhcpv6LocalServerIfcStatsStrictReconfigDropped,
       "jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped": jnxJdhcpv6LocalServerIfcStatsAuthenticationDropped,
       "jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped": jnxJdhcpv6LocalServerIfcStatsDynamicProfileDropped,
       "jnxJdhcpv6LocalServerIfcStatsLicenseDropped": jnxJdhcpv6LocalServerIfcStatsLicenseDropped}
)
