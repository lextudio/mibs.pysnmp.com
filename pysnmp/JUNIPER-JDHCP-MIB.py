# SNMP MIB module (JUNIPER-JDHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JDHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:13 2024
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

(jnxJdhcpMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxJdhcpMibRoot")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxJdhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61)
)
jnxJdhcpMIB.setRevisions(
        ("2015-03-03 00:00",
         "2011-07-09 00:00",
         "2011-03-15 00:00",
         "2011-01-25 00:00",
         "2010-04-19 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJdhcpLocalServerObjects_ObjectIdentity = ObjectIdentity
jnxJdhcpLocalServerObjects = _JnxJdhcpLocalServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1)
)
_JnxJdhcpLocalServerStatistics_ObjectIdentity = ObjectIdentity
jnxJdhcpLocalServerStatistics = _JnxJdhcpLocalServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1)
)
_JnxJdhcpLocalServerTotalDropped_Type = Counter32
_JnxJdhcpLocalServerTotalDropped_Object = MibScalar
jnxJdhcpLocalServerTotalDropped = _JnxJdhcpLocalServerTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 1),
    _JnxJdhcpLocalServerTotalDropped_Type()
)
jnxJdhcpLocalServerTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerTotalDropped.setStatus("current")
_JnxJdhcpLocalServerBadHardwareDropped_Type = Counter32
_JnxJdhcpLocalServerBadHardwareDropped_Object = MibScalar
jnxJdhcpLocalServerBadHardwareDropped = _JnxJdhcpLocalServerBadHardwareDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 2),
    _JnxJdhcpLocalServerBadHardwareDropped_Type()
)
jnxJdhcpLocalServerBadHardwareDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBadHardwareDropped.setStatus("current")
_JnxJdhcpLocalServerBadBootpOpcodeDropped_Type = Counter32
_JnxJdhcpLocalServerBadBootpOpcodeDropped_Object = MibScalar
jnxJdhcpLocalServerBadBootpOpcodeDropped = _JnxJdhcpLocalServerBadBootpOpcodeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 3),
    _JnxJdhcpLocalServerBadBootpOpcodeDropped_Type()
)
jnxJdhcpLocalServerBadBootpOpcodeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBadBootpOpcodeDropped.setStatus("current")
_JnxJdhcpLocalServerBadOptionsDropped_Type = Counter32
_JnxJdhcpLocalServerBadOptionsDropped_Object = MibScalar
jnxJdhcpLocalServerBadOptionsDropped = _JnxJdhcpLocalServerBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 4),
    _JnxJdhcpLocalServerBadOptionsDropped_Type()
)
jnxJdhcpLocalServerBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBadOptionsDropped.setStatus("current")
_JnxJdhcpLocalServerBadAddressDropped_Type = Counter32
_JnxJdhcpLocalServerBadAddressDropped_Object = MibScalar
jnxJdhcpLocalServerBadAddressDropped = _JnxJdhcpLocalServerBadAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 5),
    _JnxJdhcpLocalServerBadAddressDropped_Type()
)
jnxJdhcpLocalServerBadAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBadAddressDropped.setStatus("current")
_JnxJdhcpLocalServerNoAddressDropped_Type = Counter32
_JnxJdhcpLocalServerNoAddressDropped_Object = MibScalar
jnxJdhcpLocalServerNoAddressDropped = _JnxJdhcpLocalServerNoAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 6),
    _JnxJdhcpLocalServerNoAddressDropped_Type()
)
jnxJdhcpLocalServerNoAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerNoAddressDropped.setStatus("current")
_JnxJdhcpLocalServerNoInterfaceDropped_Type = Counter32
_JnxJdhcpLocalServerNoInterfaceDropped_Object = MibScalar
jnxJdhcpLocalServerNoInterfaceDropped = _JnxJdhcpLocalServerNoInterfaceDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 7),
    _JnxJdhcpLocalServerNoInterfaceDropped_Type()
)
jnxJdhcpLocalServerNoInterfaceDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerNoInterfaceDropped.setStatus("current")
_JnxJdhcpLocalServerNoRoutingInstanceDropped_Type = Counter32
_JnxJdhcpLocalServerNoRoutingInstanceDropped_Object = MibScalar
jnxJdhcpLocalServerNoRoutingInstanceDropped = _JnxJdhcpLocalServerNoRoutingInstanceDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 8),
    _JnxJdhcpLocalServerNoRoutingInstanceDropped_Type()
)
jnxJdhcpLocalServerNoRoutingInstanceDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerNoRoutingInstanceDropped.setStatus("current")
_JnxJdhcpLocalServerNoLocalAddressDropped_Type = Counter32
_JnxJdhcpLocalServerNoLocalAddressDropped_Object = MibScalar
jnxJdhcpLocalServerNoLocalAddressDropped = _JnxJdhcpLocalServerNoLocalAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 9),
    _JnxJdhcpLocalServerNoLocalAddressDropped_Type()
)
jnxJdhcpLocalServerNoLocalAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerNoLocalAddressDropped.setStatus("current")
_JnxJdhcpLocalServerShortPacketDropped_Type = Counter32
_JnxJdhcpLocalServerShortPacketDropped_Object = MibScalar
jnxJdhcpLocalServerShortPacketDropped = _JnxJdhcpLocalServerShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 10),
    _JnxJdhcpLocalServerShortPacketDropped_Type()
)
jnxJdhcpLocalServerShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerShortPacketDropped.setStatus("current")
_JnxJdhcpLocalServerBadReadDropped_Type = Counter32
_JnxJdhcpLocalServerBadReadDropped_Object = MibScalar
jnxJdhcpLocalServerBadReadDropped = _JnxJdhcpLocalServerBadReadDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 11),
    _JnxJdhcpLocalServerBadReadDropped_Type()
)
jnxJdhcpLocalServerBadReadDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBadReadDropped.setStatus("current")
_JnxJdhcpLocalServerBadSendDropped_Type = Counter32
_JnxJdhcpLocalServerBadSendDropped_Object = MibScalar
jnxJdhcpLocalServerBadSendDropped = _JnxJdhcpLocalServerBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 12),
    _JnxJdhcpLocalServerBadSendDropped_Type()
)
jnxJdhcpLocalServerBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBadSendDropped.setStatus("current")
_JnxJdhcpLocalServerAuthenticationDropped_Type = Counter32
_JnxJdhcpLocalServerAuthenticationDropped_Object = MibScalar
jnxJdhcpLocalServerAuthenticationDropped = _JnxJdhcpLocalServerAuthenticationDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 13),
    _JnxJdhcpLocalServerAuthenticationDropped_Type()
)
jnxJdhcpLocalServerAuthenticationDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerAuthenticationDropped.setStatus("current")
_JnxJdhcpLocalServerDynamicProfileDropped_Type = Counter32
_JnxJdhcpLocalServerDynamicProfileDropped_Object = MibScalar
jnxJdhcpLocalServerDynamicProfileDropped = _JnxJdhcpLocalServerDynamicProfileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 14),
    _JnxJdhcpLocalServerDynamicProfileDropped_Type()
)
jnxJdhcpLocalServerDynamicProfileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDynamicProfileDropped.setStatus("current")
_JnxJdhcpLocalServerLicenseDropped_Type = Counter32
_JnxJdhcpLocalServerLicenseDropped_Object = MibScalar
jnxJdhcpLocalServerLicenseDropped = _JnxJdhcpLocalServerLicenseDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 15),
    _JnxJdhcpLocalServerLicenseDropped_Type()
)
jnxJdhcpLocalServerLicenseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerLicenseDropped.setStatus("current")
_JnxJdhcpLocalServerBootRequestReceived_Type = Counter32
_JnxJdhcpLocalServerBootRequestReceived_Object = MibScalar
jnxJdhcpLocalServerBootRequestReceived = _JnxJdhcpLocalServerBootRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 16),
    _JnxJdhcpLocalServerBootRequestReceived_Type()
)
jnxJdhcpLocalServerBootRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBootRequestReceived.setStatus("current")
_JnxJdhcpLocalServerDhcpDeclineReceived_Type = Counter32
_JnxJdhcpLocalServerDhcpDeclineReceived_Object = MibScalar
jnxJdhcpLocalServerDhcpDeclineReceived = _JnxJdhcpLocalServerDhcpDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 17),
    _JnxJdhcpLocalServerDhcpDeclineReceived_Type()
)
jnxJdhcpLocalServerDhcpDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpDeclineReceived.setStatus("current")
_JnxJdhcpLocalServerDhcpDiscoverReceived_Type = Counter32
_JnxJdhcpLocalServerDhcpDiscoverReceived_Object = MibScalar
jnxJdhcpLocalServerDhcpDiscoverReceived = _JnxJdhcpLocalServerDhcpDiscoverReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 18),
    _JnxJdhcpLocalServerDhcpDiscoverReceived_Type()
)
jnxJdhcpLocalServerDhcpDiscoverReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpDiscoverReceived.setStatus("current")
_JnxJdhcpLocalServerDhcpInformReceived_Type = Counter32
_JnxJdhcpLocalServerDhcpInformReceived_Object = MibScalar
jnxJdhcpLocalServerDhcpInformReceived = _JnxJdhcpLocalServerDhcpInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 19),
    _JnxJdhcpLocalServerDhcpInformReceived_Type()
)
jnxJdhcpLocalServerDhcpInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpInformReceived.setStatus("current")
_JnxJdhcpLocalServerDhcpReleaseReceived_Type = Counter32
_JnxJdhcpLocalServerDhcpReleaseReceived_Object = MibScalar
jnxJdhcpLocalServerDhcpReleaseReceived = _JnxJdhcpLocalServerDhcpReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 20),
    _JnxJdhcpLocalServerDhcpReleaseReceived_Type()
)
jnxJdhcpLocalServerDhcpReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpReleaseReceived.setStatus("current")
_JnxJdhcpLocalServerDhcpRequestReceived_Type = Counter32
_JnxJdhcpLocalServerDhcpRequestReceived_Object = MibScalar
jnxJdhcpLocalServerDhcpRequestReceived = _JnxJdhcpLocalServerDhcpRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 21),
    _JnxJdhcpLocalServerDhcpRequestReceived_Type()
)
jnxJdhcpLocalServerDhcpRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpRequestReceived.setStatus("current")
_JnxJdhcpLocalServerDhcpBootReplySent_Type = Counter32
_JnxJdhcpLocalServerDhcpBootReplySent_Object = MibScalar
jnxJdhcpLocalServerDhcpBootReplySent = _JnxJdhcpLocalServerDhcpBootReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 22),
    _JnxJdhcpLocalServerDhcpBootReplySent_Type()
)
jnxJdhcpLocalServerDhcpBootReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpBootReplySent.setStatus("current")
_JnxJdhcpLocalServerDhcpOfferSent_Type = Counter32
_JnxJdhcpLocalServerDhcpOfferSent_Object = MibScalar
jnxJdhcpLocalServerDhcpOfferSent = _JnxJdhcpLocalServerDhcpOfferSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 23),
    _JnxJdhcpLocalServerDhcpOfferSent_Type()
)
jnxJdhcpLocalServerDhcpOfferSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpOfferSent.setStatus("current")
_JnxJdhcpLocalServerDhcpAckSent_Type = Counter32
_JnxJdhcpLocalServerDhcpAckSent_Object = MibScalar
jnxJdhcpLocalServerDhcpAckSent = _JnxJdhcpLocalServerDhcpAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 24),
    _JnxJdhcpLocalServerDhcpAckSent_Type()
)
jnxJdhcpLocalServerDhcpAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpAckSent.setStatus("current")
_JnxJdhcpLocalServerDhcpNakSent_Type = Counter32
_JnxJdhcpLocalServerDhcpNakSent_Object = MibScalar
jnxJdhcpLocalServerDhcpNakSent = _JnxJdhcpLocalServerDhcpNakSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 25),
    _JnxJdhcpLocalServerDhcpNakSent_Type()
)
jnxJdhcpLocalServerDhcpNakSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDhcpNakSent.setStatus("current")
_JnxJdhcpLocalServerForceRenewSent_Type = Counter32
_JnxJdhcpLocalServerForceRenewSent_Object = MibScalar
jnxJdhcpLocalServerForceRenewSent = _JnxJdhcpLocalServerForceRenewSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 26),
    _JnxJdhcpLocalServerForceRenewSent_Type()
)
jnxJdhcpLocalServerForceRenewSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerForceRenewSent.setStatus("current")
_JnxJdhcpLocalServerTotalLeaseCount_Type = Counter32
_JnxJdhcpLocalServerTotalLeaseCount_Object = MibScalar
jnxJdhcpLocalServerTotalLeaseCount = _JnxJdhcpLocalServerTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 27),
    _JnxJdhcpLocalServerTotalLeaseCount_Type()
)
jnxJdhcpLocalServerTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerTotalLeaseCount.setStatus("current")
_JnxJdhcpLocalServerSwitchDropped_Type = Counter32
_JnxJdhcpLocalServerSwitchDropped_Object = MibScalar
jnxJdhcpLocalServerSwitchDropped = _JnxJdhcpLocalServerSwitchDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 28),
    _JnxJdhcpLocalServerSwitchDropped_Type()
)
jnxJdhcpLocalServerSwitchDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerSwitchDropped.setStatus("current")
_JnxJdhcpLocalServerLeaseQueryReceived_Type = Counter32
_JnxJdhcpLocalServerLeaseQueryReceived_Object = MibScalar
jnxJdhcpLocalServerLeaseQueryReceived = _JnxJdhcpLocalServerLeaseQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 29),
    _JnxJdhcpLocalServerLeaseQueryReceived_Type()
)
jnxJdhcpLocalServerLeaseQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerLeaseQueryReceived.setStatus("current")
_JnxJdhcpLocalServerBulkLeaseQueryReceived_Type = Counter32
_JnxJdhcpLocalServerBulkLeaseQueryReceived_Object = MibScalar
jnxJdhcpLocalServerBulkLeaseQueryReceived = _JnxJdhcpLocalServerBulkLeaseQueryReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 30),
    _JnxJdhcpLocalServerBulkLeaseQueryReceived_Type()
)
jnxJdhcpLocalServerBulkLeaseQueryReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBulkLeaseQueryReceived.setStatus("current")
_JnxJdhcpLocalServerLeaseActiveSent_Type = Counter32
_JnxJdhcpLocalServerLeaseActiveSent_Object = MibScalar
jnxJdhcpLocalServerLeaseActiveSent = _JnxJdhcpLocalServerLeaseActiveSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 31),
    _JnxJdhcpLocalServerLeaseActiveSent_Type()
)
jnxJdhcpLocalServerLeaseActiveSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerLeaseActiveSent.setStatus("current")
_JnxJdhcpLocalServerLeaseUnknownSent_Type = Counter32
_JnxJdhcpLocalServerLeaseUnknownSent_Object = MibScalar
jnxJdhcpLocalServerLeaseUnknownSent = _JnxJdhcpLocalServerLeaseUnknownSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 32),
    _JnxJdhcpLocalServerLeaseUnknownSent_Type()
)
jnxJdhcpLocalServerLeaseUnknownSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerLeaseUnknownSent.setStatus("current")
_JnxJdhcpLocalServerLeaseUnAssignedSent_Type = Counter32
_JnxJdhcpLocalServerLeaseUnAssignedSent_Object = MibScalar
jnxJdhcpLocalServerLeaseUnAssignedSent = _JnxJdhcpLocalServerLeaseUnAssignedSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 33),
    _JnxJdhcpLocalServerLeaseUnAssignedSent_Type()
)
jnxJdhcpLocalServerLeaseUnAssignedSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerLeaseUnAssignedSent.setStatus("current")
_JnxJdhcpLocalServerLeaseQueryDoneSent_Type = Counter32
_JnxJdhcpLocalServerLeaseQueryDoneSent_Object = MibScalar
jnxJdhcpLocalServerLeaseQueryDoneSent = _JnxJdhcpLocalServerLeaseQueryDoneSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 1, 34),
    _JnxJdhcpLocalServerLeaseQueryDoneSent_Type()
)
jnxJdhcpLocalServerLeaseQueryDoneSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerLeaseQueryDoneSent.setStatus("current")
_JnxJdhcpLocalServerBindings_ObjectIdentity = ObjectIdentity
jnxJdhcpLocalServerBindings = _JnxJdhcpLocalServerBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2)
)
_JnxJdhcpLocalServerBindingsTable_Object = MibTable
jnxJdhcpLocalServerBindingsTable = _JnxJdhcpLocalServerBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsTable.setStatus("current")
_JnxJdhcpLocalServerBindingsEntry_Object = MibTableRow
jnxJdhcpLocalServerBindingsEntry = _JnxJdhcpLocalServerBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1)
)
jnxJdhcpLocalServerBindingsEntry.setIndexNames(
    (0, "JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerBindingsIpAddress"),
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsEntry.setStatus("current")
_JnxJdhcpLocalServerBindingsIpAddress_Type = IpAddress
_JnxJdhcpLocalServerBindingsIpAddress_Object = MibTableColumn
jnxJdhcpLocalServerBindingsIpAddress = _JnxJdhcpLocalServerBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 1),
    _JnxJdhcpLocalServerBindingsIpAddress_Type()
)
jnxJdhcpLocalServerBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsIpAddress.setStatus("current")
_JnxJdhcpLocalServerBindingsMacAddress_Type = MacAddress
_JnxJdhcpLocalServerBindingsMacAddress_Object = MibTableColumn
jnxJdhcpLocalServerBindingsMacAddress = _JnxJdhcpLocalServerBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 2),
    _JnxJdhcpLocalServerBindingsMacAddress_Type()
)
jnxJdhcpLocalServerBindingsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsMacAddress.setStatus("current")


class _JnxJdhcpLocalServerBindingsState_Type(Integer32):
    """Custom type jnxJdhcpLocalServerBindingsState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("bound", 5),
          ("init", 1),
          ("none", 0),
          ("rebinding", 7),
          ("release", 4),
          ("renewing", 6),
          ("requesting", 3),
          ("selecting", 2))
    )


_JnxJdhcpLocalServerBindingsState_Type.__name__ = "Integer32"
_JnxJdhcpLocalServerBindingsState_Object = MibTableColumn
jnxJdhcpLocalServerBindingsState = _JnxJdhcpLocalServerBindingsState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 3),
    _JnxJdhcpLocalServerBindingsState_Type()
)
jnxJdhcpLocalServerBindingsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsState.setStatus("current")
_JnxJdhcpLocalServerBindingsLeaseEndTime_Type = DateAndTime
_JnxJdhcpLocalServerBindingsLeaseEndTime_Object = MibTableColumn
jnxJdhcpLocalServerBindingsLeaseEndTime = _JnxJdhcpLocalServerBindingsLeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 4),
    _JnxJdhcpLocalServerBindingsLeaseEndTime_Type()
)
jnxJdhcpLocalServerBindingsLeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsLeaseEndTime.setStatus("current")
_JnxJdhcpLocalServerBindingsLeaseExpireTime_Type = Unsigned32
_JnxJdhcpLocalServerBindingsLeaseExpireTime_Object = MibTableColumn
jnxJdhcpLocalServerBindingsLeaseExpireTime = _JnxJdhcpLocalServerBindingsLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 5),
    _JnxJdhcpLocalServerBindingsLeaseExpireTime_Type()
)
jnxJdhcpLocalServerBindingsLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsLeaseExpireTime.setStatus("current")
_JnxJdhcpLocalServerBindingsLeaseStartTime_Type = DateAndTime
_JnxJdhcpLocalServerBindingsLeaseStartTime_Object = MibTableColumn
jnxJdhcpLocalServerBindingsLeaseStartTime = _JnxJdhcpLocalServerBindingsLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 6),
    _JnxJdhcpLocalServerBindingsLeaseStartTime_Type()
)
jnxJdhcpLocalServerBindingsLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsLeaseStartTime.setStatus("current")
_JnxJdhcpLocalServerBindingsIncomingClientInterface_Type = DisplayString
_JnxJdhcpLocalServerBindingsIncomingClientInterface_Object = MibTableColumn
jnxJdhcpLocalServerBindingsIncomingClientInterface = _JnxJdhcpLocalServerBindingsIncomingClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 7),
    _JnxJdhcpLocalServerBindingsIncomingClientInterface_Type()
)
jnxJdhcpLocalServerBindingsIncomingClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsIncomingClientInterface.setStatus("current")
_JnxJdhcpLocalServerBindingsClientInterfaceVlanId_Type = Unsigned32
_JnxJdhcpLocalServerBindingsClientInterfaceVlanId_Object = MibTableColumn
jnxJdhcpLocalServerBindingsClientInterfaceVlanId = _JnxJdhcpLocalServerBindingsClientInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 8),
    _JnxJdhcpLocalServerBindingsClientInterfaceVlanId_Type()
)
jnxJdhcpLocalServerBindingsClientInterfaceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsClientInterfaceVlanId.setStatus("current")
_JnxJdhcpLocalServerBindingsDemuxInterfaceName_Type = DisplayString
_JnxJdhcpLocalServerBindingsDemuxInterfaceName_Object = MibTableColumn
jnxJdhcpLocalServerBindingsDemuxInterfaceName = _JnxJdhcpLocalServerBindingsDemuxInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 9),
    _JnxJdhcpLocalServerBindingsDemuxInterfaceName_Type()
)
jnxJdhcpLocalServerBindingsDemuxInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsDemuxInterfaceName.setStatus("current")
_JnxJdhcpLocalServerBindingsServerIpAddress_Type = IpAddress
_JnxJdhcpLocalServerBindingsServerIpAddress_Object = MibTableColumn
jnxJdhcpLocalServerBindingsServerIpAddress = _JnxJdhcpLocalServerBindingsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 10),
    _JnxJdhcpLocalServerBindingsServerIpAddress_Type()
)
jnxJdhcpLocalServerBindingsServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsServerIpAddress.setStatus("current")
_JnxJdhcpLocalServerBindingsBootpRelayAddress_Type = IpAddress
_JnxJdhcpLocalServerBindingsBootpRelayAddress_Object = MibTableColumn
jnxJdhcpLocalServerBindingsBootpRelayAddress = _JnxJdhcpLocalServerBindingsBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 11),
    _JnxJdhcpLocalServerBindingsBootpRelayAddress_Type()
)
jnxJdhcpLocalServerBindingsBootpRelayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsBootpRelayAddress.setStatus("current")
_JnxJdhcpLocalServerBindingsPreviousBootpRelayAddress_Type = IpAddress
_JnxJdhcpLocalServerBindingsPreviousBootpRelayAddress_Object = MibTableColumn
jnxJdhcpLocalServerBindingsPreviousBootpRelayAddress = _JnxJdhcpLocalServerBindingsPreviousBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 12),
    _JnxJdhcpLocalServerBindingsPreviousBootpRelayAddress_Type()
)
jnxJdhcpLocalServerBindingsPreviousBootpRelayAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsPreviousBootpRelayAddress.setStatus("current")
_JnxJdhcpLocalServerBindingsClientPoolName_Type = DisplayString
_JnxJdhcpLocalServerBindingsClientPoolName_Object = MibTableColumn
jnxJdhcpLocalServerBindingsClientPoolName = _JnxJdhcpLocalServerBindingsClientPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 13),
    _JnxJdhcpLocalServerBindingsClientPoolName_Type()
)
jnxJdhcpLocalServerBindingsClientPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsClientPoolName.setStatus("current")
_JnxJdhcpLocalServerBindingsClientProfileName_Type = DisplayString
_JnxJdhcpLocalServerBindingsClientProfileName_Object = MibTableColumn
jnxJdhcpLocalServerBindingsClientProfileName = _JnxJdhcpLocalServerBindingsClientProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 2, 1, 1, 14),
    _JnxJdhcpLocalServerBindingsClientProfileName_Type()
)
jnxJdhcpLocalServerBindingsClientProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerBindingsClientProfileName.setStatus("current")
_JnxJdhcpLocalServerTraps_ObjectIdentity = ObjectIdentity
jnxJdhcpLocalServerTraps = _JnxJdhcpLocalServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 3)
)
_JnxJdhcpLocalServerTrapVars_ObjectIdentity = ObjectIdentity
jnxJdhcpLocalServerTrapVars = _JnxJdhcpLocalServerTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4)
)
_JnxJdhcpLocalServerLastDetected_Type = DateAndTime
_JnxJdhcpLocalServerLastDetected_Object = MibScalar
jnxJdhcpLocalServerLastDetected = _JnxJdhcpLocalServerLastDetected_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4, 1),
    _JnxJdhcpLocalServerLastDetected_Type()
)
jnxJdhcpLocalServerLastDetected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerLastDetected.setStatus("current")


class _JnxJdhcpRouterName_Type(DisplayString):
    """Custom type jnxJdhcpRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 257),
    )


_JnxJdhcpRouterName_Type.__name__ = "DisplayString"
_JnxJdhcpRouterName_Object = MibScalar
jnxJdhcpRouterName = _JnxJdhcpRouterName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4, 2),
    _JnxJdhcpRouterName_Type()
)
jnxJdhcpRouterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpRouterName.setStatus("current")
_JnxJdhcpLocalServerMacAddress_Type = MacAddress
_JnxJdhcpLocalServerMacAddress_Object = MibScalar
jnxJdhcpLocalServerMacAddress = _JnxJdhcpLocalServerMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4, 3),
    _JnxJdhcpLocalServerMacAddress_Type()
)
jnxJdhcpLocalServerMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerMacAddress.setStatus("current")
_JnxJdhcpLocalServerInterfaceName_Type = DisplayString
_JnxJdhcpLocalServerInterfaceName_Object = MibScalar
jnxJdhcpLocalServerInterfaceName = _JnxJdhcpLocalServerInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4, 4),
    _JnxJdhcpLocalServerInterfaceName_Type()
)
jnxJdhcpLocalServerInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerInterfaceName.setStatus("current")
_JnxJdhcpLocalServerInterfaceLimit_Type = Unsigned32
_JnxJdhcpLocalServerInterfaceLimit_Object = MibScalar
jnxJdhcpLocalServerInterfaceLimit = _JnxJdhcpLocalServerInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4, 5),
    _JnxJdhcpLocalServerInterfaceLimit_Type()
)
jnxJdhcpLocalServerInterfaceLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerInterfaceLimit.setStatus("current")


class _JnxJdhcpLocalServerEventSeverity_Type(Integer32):
    """Custom type jnxJdhcpLocalServerEventSeverity based on Integer32"""
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


_JnxJdhcpLocalServerEventSeverity_Type.__name__ = "Integer32"
_JnxJdhcpLocalServerEventSeverity_Object = MibScalar
jnxJdhcpLocalServerEventSeverity = _JnxJdhcpLocalServerEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4, 6),
    _JnxJdhcpLocalServerEventSeverity_Type()
)
jnxJdhcpLocalServerEventSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerEventSeverity.setStatus("current")
_JnxJdhcpLocalServerEventString_Type = DisplayString
_JnxJdhcpLocalServerEventString_Object = MibScalar
jnxJdhcpLocalServerEventString = _JnxJdhcpLocalServerEventString_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 4, 7),
    _JnxJdhcpLocalServerEventString_Type()
)
jnxJdhcpLocalServerEventString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerEventString.setStatus("current")
_JnxJdhcpLocalServerIfcStats_ObjectIdentity = ObjectIdentity
jnxJdhcpLocalServerIfcStats = _JnxJdhcpLocalServerIfcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5)
)
_JnxJdhcpLocalServerIfcStatsTable_Object = MibTable
jnxJdhcpLocalServerIfcStatsTable = _JnxJdhcpLocalServerIfcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsTable.setStatus("current")
_JnxJdhcpLocalServerIfcStatsEntry_Object = MibTableRow
jnxJdhcpLocalServerIfcStatsEntry = _JnxJdhcpLocalServerIfcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1)
)
jnxJdhcpLocalServerIfcStatsEntry.setIndexNames(
    (0, "JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerIfcStatsIfIndex"),
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsEntry.setStatus("current")
_JnxJdhcpLocalServerIfcStatsIfIndex_Type = InterfaceIndex
_JnxJdhcpLocalServerIfcStatsIfIndex_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsIfIndex = _JnxJdhcpLocalServerIfcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 1),
    _JnxJdhcpLocalServerIfcStatsIfIndex_Type()
)
jnxJdhcpLocalServerIfcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsIfIndex.setStatus("current")
_JnxJdhcpLocalServerIfcStatsTotalDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsTotalDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsTotalDropped = _JnxJdhcpLocalServerIfcStatsTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 2),
    _JnxJdhcpLocalServerIfcStatsTotalDropped_Type()
)
jnxJdhcpLocalServerIfcStatsTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsTotalDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBadHardwareDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBadHardwareDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBadHardwareDropped = _JnxJdhcpLocalServerIfcStatsBadHardwareDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 3),
    _JnxJdhcpLocalServerIfcStatsBadHardwareDropped_Type()
)
jnxJdhcpLocalServerIfcStatsBadHardwareDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBadHardwareDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped = _JnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 4),
    _JnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped_Type()
)
jnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBadOptionsDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBadOptionsDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBadOptionsDropped = _JnxJdhcpLocalServerIfcStatsBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 5),
    _JnxJdhcpLocalServerIfcStatsBadOptionsDropped_Type()
)
jnxJdhcpLocalServerIfcStatsBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBadOptionsDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBadAddressDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBadAddressDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBadAddressDropped = _JnxJdhcpLocalServerIfcStatsBadAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 6),
    _JnxJdhcpLocalServerIfcStatsBadAddressDropped_Type()
)
jnxJdhcpLocalServerIfcStatsBadAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBadAddressDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsNoAddressDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsNoAddressDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsNoAddressDropped = _JnxJdhcpLocalServerIfcStatsNoAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 7),
    _JnxJdhcpLocalServerIfcStatsNoAddressDropped_Type()
)
jnxJdhcpLocalServerIfcStatsNoAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsNoAddressDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped = _JnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 8),
    _JnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped_Type()
)
jnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsNoLocalAddressDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsNoLocalAddressDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsNoLocalAddressDropped = _JnxJdhcpLocalServerIfcStatsNoLocalAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 9),
    _JnxJdhcpLocalServerIfcStatsNoLocalAddressDropped_Type()
)
jnxJdhcpLocalServerIfcStatsNoLocalAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsNoLocalAddressDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsShortPacketDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsShortPacketDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsShortPacketDropped = _JnxJdhcpLocalServerIfcStatsShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 10),
    _JnxJdhcpLocalServerIfcStatsShortPacketDropped_Type()
)
jnxJdhcpLocalServerIfcStatsShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsShortPacketDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBadSendDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBadSendDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBadSendDropped = _JnxJdhcpLocalServerIfcStatsBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 11),
    _JnxJdhcpLocalServerIfcStatsBadSendDropped_Type()
)
jnxJdhcpLocalServerIfcStatsBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBadSendDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsAuthenticationDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsAuthenticationDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsAuthenticationDropped = _JnxJdhcpLocalServerIfcStatsAuthenticationDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 12),
    _JnxJdhcpLocalServerIfcStatsAuthenticationDropped_Type()
)
jnxJdhcpLocalServerIfcStatsAuthenticationDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsAuthenticationDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDynamicProfileDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDynamicProfileDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDynamicProfileDropped = _JnxJdhcpLocalServerIfcStatsDynamicProfileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 13),
    _JnxJdhcpLocalServerIfcStatsDynamicProfileDropped_Type()
)
jnxJdhcpLocalServerIfcStatsDynamicProfileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDynamicProfileDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsLicenseDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsLicenseDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsLicenseDropped = _JnxJdhcpLocalServerIfcStatsLicenseDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 14),
    _JnxJdhcpLocalServerIfcStatsLicenseDropped_Type()
)
jnxJdhcpLocalServerIfcStatsLicenseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsLicenseDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBootRequestReceived_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBootRequestReceived_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBootRequestReceived = _JnxJdhcpLocalServerIfcStatsBootRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 15),
    _JnxJdhcpLocalServerIfcStatsBootRequestReceived_Type()
)
jnxJdhcpLocalServerIfcStatsBootRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBootRequestReceived.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpDeclineReceived_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpDeclineReceived_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpDeclineReceived = _JnxJdhcpLocalServerIfcStatsDhcpDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 16),
    _JnxJdhcpLocalServerIfcStatsDhcpDeclineReceived_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpDeclineReceived.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived = _JnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 17),
    _JnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpInformReceived_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpInformReceived_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpInformReceived = _JnxJdhcpLocalServerIfcStatsDhcpInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 18),
    _JnxJdhcpLocalServerIfcStatsDhcpInformReceived_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpInformReceived.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpReleaseReceived_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpReleaseReceived_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpReleaseReceived = _JnxJdhcpLocalServerIfcStatsDhcpReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 19),
    _JnxJdhcpLocalServerIfcStatsDhcpReleaseReceived_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpReleaseReceived.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpRequestReceived_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpRequestReceived_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpRequestReceived = _JnxJdhcpLocalServerIfcStatsDhcpRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 20),
    _JnxJdhcpLocalServerIfcStatsDhcpRequestReceived_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpRequestReceived.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpBootReplySent_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpBootReplySent_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpBootReplySent = _JnxJdhcpLocalServerIfcStatsDhcpBootReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 21),
    _JnxJdhcpLocalServerIfcStatsDhcpBootReplySent_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpBootReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpBootReplySent.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpOfferSent_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpOfferSent_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpOfferSent = _JnxJdhcpLocalServerIfcStatsDhcpOfferSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 22),
    _JnxJdhcpLocalServerIfcStatsDhcpOfferSent_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpOfferSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpOfferSent.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpAckSent_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpAckSent_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpAckSent = _JnxJdhcpLocalServerIfcStatsDhcpAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 23),
    _JnxJdhcpLocalServerIfcStatsDhcpAckSent_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpAckSent.setStatus("current")
_JnxJdhcpLocalServerIfcStatsDhcpNakSent_Type = Counter32
_JnxJdhcpLocalServerIfcStatsDhcpNakSent_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsDhcpNakSent = _JnxJdhcpLocalServerIfcStatsDhcpNakSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 24),
    _JnxJdhcpLocalServerIfcStatsDhcpNakSent_Type()
)
jnxJdhcpLocalServerIfcStatsDhcpNakSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsDhcpNakSent.setStatus("current")
_JnxJdhcpLocalServerIfcStatsForceRenewSent_Type = Counter32
_JnxJdhcpLocalServerIfcStatsForceRenewSent_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsForceRenewSent = _JnxJdhcpLocalServerIfcStatsForceRenewSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 25),
    _JnxJdhcpLocalServerIfcStatsForceRenewSent_Type()
)
jnxJdhcpLocalServerIfcStatsForceRenewSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsForceRenewSent.setStatus("current")
_JnxJdhcpLocalServerIfcStatsTotalLeaseCount_Type = Counter32
_JnxJdhcpLocalServerIfcStatsTotalLeaseCount_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsTotalLeaseCount = _JnxJdhcpLocalServerIfcStatsTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 26),
    _JnxJdhcpLocalServerIfcStatsTotalLeaseCount_Type()
)
jnxJdhcpLocalServerIfcStatsTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsTotalLeaseCount.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped = _JnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 27),
    _JnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped_Type()
)
jnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsNoOptionsDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsNoOptionsDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsNoOptionsDropped = _JnxJdhcpLocalServerIfcStatsNoOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 28),
    _JnxJdhcpLocalServerIfcStatsNoOptionsDropped_Type()
)
jnxJdhcpLocalServerIfcStatsNoOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsNoOptionsDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsHopLimitDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsHopLimitDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsHopLimitDropped = _JnxJdhcpLocalServerIfcStatsHopLimitDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 29),
    _JnxJdhcpLocalServerIfcStatsHopLimitDropped_Type()
)
jnxJdhcpLocalServerIfcStatsHopLimitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsHopLimitDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsTtlExpiredDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsTtlExpiredDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsTtlExpiredDropped = _JnxJdhcpLocalServerIfcStatsTtlExpiredDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 30),
    _JnxJdhcpLocalServerIfcStatsTtlExpiredDropped_Type()
)
jnxJdhcpLocalServerIfcStatsTtlExpiredDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsTtlExpiredDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsBadUdpCksumDropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsBadUdpCksumDropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsBadUdpCksumDropped = _JnxJdhcpLocalServerIfcStatsBadUdpCksumDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 31),
    _JnxJdhcpLocalServerIfcStatsBadUdpCksumDropped_Type()
)
jnxJdhcpLocalServerIfcStatsBadUdpCksumDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsBadUdpCksumDropped.setStatus("current")
_JnxJdhcpLocalServerIfcStatsOption60Dropped_Type = Counter32
_JnxJdhcpLocalServerIfcStatsOption60Dropped_Object = MibTableColumn
jnxJdhcpLocalServerIfcStatsOption60Dropped = _JnxJdhcpLocalServerIfcStatsOption60Dropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 5, 1, 1, 32),
    _JnxJdhcpLocalServerIfcStatsOption60Dropped_Type()
)
jnxJdhcpLocalServerIfcStatsOption60Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerIfcStatsOption60Dropped.setStatus("current")
_JnxJdhcpRelayObjects_ObjectIdentity = ObjectIdentity
jnxJdhcpRelayObjects = _JnxJdhcpRelayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2)
)
_JnxJdhcpRelayStatistics_ObjectIdentity = ObjectIdentity
jnxJdhcpRelayStatistics = _JnxJdhcpRelayStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1)
)
_JnxJdhcpRelayTotalDropped_Type = Counter32
_JnxJdhcpRelayTotalDropped_Object = MibScalar
jnxJdhcpRelayTotalDropped = _JnxJdhcpRelayTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 1),
    _JnxJdhcpRelayTotalDropped_Type()
)
jnxJdhcpRelayTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayTotalDropped.setStatus("current")
_JnxJdhcpRelayBadHardwareDropped_Type = Counter32
_JnxJdhcpRelayBadHardwareDropped_Object = MibScalar
jnxJdhcpRelayBadHardwareDropped = _JnxJdhcpRelayBadHardwareDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 2),
    _JnxJdhcpRelayBadHardwareDropped_Type()
)
jnxJdhcpRelayBadHardwareDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBadHardwareDropped.setStatus("current")
_JnxJdhcpRelayBadBootpOpcodeDropped_Type = Counter32
_JnxJdhcpRelayBadBootpOpcodeDropped_Object = MibScalar
jnxJdhcpRelayBadBootpOpcodeDropped = _JnxJdhcpRelayBadBootpOpcodeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 3),
    _JnxJdhcpRelayBadBootpOpcodeDropped_Type()
)
jnxJdhcpRelayBadBootpOpcodeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBadBootpOpcodeDropped.setStatus("current")
_JnxJdhcpRelayBadOptionsDropped_Type = Counter32
_JnxJdhcpRelayBadOptionsDropped_Object = MibScalar
jnxJdhcpRelayBadOptionsDropped = _JnxJdhcpRelayBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 4),
    _JnxJdhcpRelayBadOptionsDropped_Type()
)
jnxJdhcpRelayBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBadOptionsDropped.setStatus("current")
_JnxJdhcpRelayBadAddressDropped_Type = Counter32
_JnxJdhcpRelayBadAddressDropped_Object = MibScalar
jnxJdhcpRelayBadAddressDropped = _JnxJdhcpRelayBadAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 5),
    _JnxJdhcpRelayBadAddressDropped_Type()
)
jnxJdhcpRelayBadAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBadAddressDropped.setStatus("current")
_JnxJdhcpRelayNoAddressDropped_Type = Counter32
_JnxJdhcpRelayNoAddressDropped_Object = MibScalar
jnxJdhcpRelayNoAddressDropped = _JnxJdhcpRelayNoAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 6),
    _JnxJdhcpRelayNoAddressDropped_Type()
)
jnxJdhcpRelayNoAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayNoAddressDropped.setStatus("current")
_JnxJdhcpRelayNoInterfaceDropped_Type = Counter32
_JnxJdhcpRelayNoInterfaceDropped_Object = MibScalar
jnxJdhcpRelayNoInterfaceDropped = _JnxJdhcpRelayNoInterfaceDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 7),
    _JnxJdhcpRelayNoInterfaceDropped_Type()
)
jnxJdhcpRelayNoInterfaceDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayNoInterfaceDropped.setStatus("current")
_JnxJdhcpRelayNoRoutingInstanceDropped_Type = Counter32
_JnxJdhcpRelayNoRoutingInstanceDropped_Object = MibScalar
jnxJdhcpRelayNoRoutingInstanceDropped = _JnxJdhcpRelayNoRoutingInstanceDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 8),
    _JnxJdhcpRelayNoRoutingInstanceDropped_Type()
)
jnxJdhcpRelayNoRoutingInstanceDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayNoRoutingInstanceDropped.setStatus("current")
_JnxJdhcpRelayNoLocalAddressDropped_Type = Counter32
_JnxJdhcpRelayNoLocalAddressDropped_Object = MibScalar
jnxJdhcpRelayNoLocalAddressDropped = _JnxJdhcpRelayNoLocalAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 9),
    _JnxJdhcpRelayNoLocalAddressDropped_Type()
)
jnxJdhcpRelayNoLocalAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayNoLocalAddressDropped.setStatus("current")
_JnxJdhcpRelayShortPacketDropped_Type = Counter32
_JnxJdhcpRelayShortPacketDropped_Object = MibScalar
jnxJdhcpRelayShortPacketDropped = _JnxJdhcpRelayShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 10),
    _JnxJdhcpRelayShortPacketDropped_Type()
)
jnxJdhcpRelayShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayShortPacketDropped.setStatus("current")
_JnxJdhcpRelayBadReadDropped_Type = Counter32
_JnxJdhcpRelayBadReadDropped_Object = MibScalar
jnxJdhcpRelayBadReadDropped = _JnxJdhcpRelayBadReadDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 11),
    _JnxJdhcpRelayBadReadDropped_Type()
)
jnxJdhcpRelayBadReadDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBadReadDropped.setStatus("current")
_JnxJdhcpRelayBadSendDropped_Type = Counter32
_JnxJdhcpRelayBadSendDropped_Object = MibScalar
jnxJdhcpRelayBadSendDropped = _JnxJdhcpRelayBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 12),
    _JnxJdhcpRelayBadSendDropped_Type()
)
jnxJdhcpRelayBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBadSendDropped.setStatus("current")
_JnxJdhcpRelayOption82Dropped_Type = Counter32
_JnxJdhcpRelayOption82Dropped_Object = MibScalar
jnxJdhcpRelayOption82Dropped = _JnxJdhcpRelayOption82Dropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 13),
    _JnxJdhcpRelayOption82Dropped_Type()
)
jnxJdhcpRelayOption82Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayOption82Dropped.setStatus("current")
_JnxJdhcpRelayOption60Dropped_Type = Counter32
_JnxJdhcpRelayOption60Dropped_Object = MibScalar
jnxJdhcpRelayOption60Dropped = _JnxJdhcpRelayOption60Dropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 14),
    _JnxJdhcpRelayOption60Dropped_Type()
)
jnxJdhcpRelayOption60Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayOption60Dropped.setStatus("current")
_JnxJdhcpRelayAuthenticationDropped_Type = Counter32
_JnxJdhcpRelayAuthenticationDropped_Object = MibScalar
jnxJdhcpRelayAuthenticationDropped = _JnxJdhcpRelayAuthenticationDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 15),
    _JnxJdhcpRelayAuthenticationDropped_Type()
)
jnxJdhcpRelayAuthenticationDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayAuthenticationDropped.setStatus("current")
_JnxJdhcpRelayDynamicProfileDropped_Type = Counter32
_JnxJdhcpRelayDynamicProfileDropped_Object = MibScalar
jnxJdhcpRelayDynamicProfileDropped = _JnxJdhcpRelayDynamicProfileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 16),
    _JnxJdhcpRelayDynamicProfileDropped_Type()
)
jnxJdhcpRelayDynamicProfileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDynamicProfileDropped.setStatus("current")
_JnxJdhcpRelayLicenseDropped_Type = Counter32
_JnxJdhcpRelayLicenseDropped_Object = MibScalar
jnxJdhcpRelayLicenseDropped = _JnxJdhcpRelayLicenseDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 17),
    _JnxJdhcpRelayLicenseDropped_Type()
)
jnxJdhcpRelayLicenseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayLicenseDropped.setStatus("current")
_JnxJdhcpRelayBootRequestReceived_Type = Counter32
_JnxJdhcpRelayBootRequestReceived_Object = MibScalar
jnxJdhcpRelayBootRequestReceived = _JnxJdhcpRelayBootRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 18),
    _JnxJdhcpRelayBootRequestReceived_Type()
)
jnxJdhcpRelayBootRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBootRequestReceived.setStatus("current")
_JnxJdhcpRelayDhcpDeclineReceived_Type = Counter32
_JnxJdhcpRelayDhcpDeclineReceived_Object = MibScalar
jnxJdhcpRelayDhcpDeclineReceived = _JnxJdhcpRelayDhcpDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 19),
    _JnxJdhcpRelayDhcpDeclineReceived_Type()
)
jnxJdhcpRelayDhcpDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpDeclineReceived.setStatus("current")
_JnxJdhcpRelayDhcpDiscoverReceived_Type = Counter32
_JnxJdhcpRelayDhcpDiscoverReceived_Object = MibScalar
jnxJdhcpRelayDhcpDiscoverReceived = _JnxJdhcpRelayDhcpDiscoverReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 20),
    _JnxJdhcpRelayDhcpDiscoverReceived_Type()
)
jnxJdhcpRelayDhcpDiscoverReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpDiscoverReceived.setStatus("current")
_JnxJdhcpRelayDhcpInformReceived_Type = Counter32
_JnxJdhcpRelayDhcpInformReceived_Object = MibScalar
jnxJdhcpRelayDhcpInformReceived = _JnxJdhcpRelayDhcpInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 21),
    _JnxJdhcpRelayDhcpInformReceived_Type()
)
jnxJdhcpRelayDhcpInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpInformReceived.setStatus("current")
_JnxJdhcpRelayDhcpReleaseReceived_Type = Counter32
_JnxJdhcpRelayDhcpReleaseReceived_Object = MibScalar
jnxJdhcpRelayDhcpReleaseReceived = _JnxJdhcpRelayDhcpReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 22),
    _JnxJdhcpRelayDhcpReleaseReceived_Type()
)
jnxJdhcpRelayDhcpReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpReleaseReceived.setStatus("current")
_JnxJdhcpRelayDhcpRequestReceived_Type = Counter32
_JnxJdhcpRelayDhcpRequestReceived_Object = MibScalar
jnxJdhcpRelayDhcpRequestReceived = _JnxJdhcpRelayDhcpRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 23),
    _JnxJdhcpRelayDhcpRequestReceived_Type()
)
jnxJdhcpRelayDhcpRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpRequestReceived.setStatus("current")
_JnxJdhcpRelayDhcpBootReplySent_Type = Counter32
_JnxJdhcpRelayDhcpBootReplySent_Object = MibScalar
jnxJdhcpRelayDhcpBootReplySent = _JnxJdhcpRelayDhcpBootReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 24),
    _JnxJdhcpRelayDhcpBootReplySent_Type()
)
jnxJdhcpRelayDhcpBootReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpBootReplySent.setStatus("current")
_JnxJdhcpRelayDhcpOfferSent_Type = Counter32
_JnxJdhcpRelayDhcpOfferSent_Object = MibScalar
jnxJdhcpRelayDhcpOfferSent = _JnxJdhcpRelayDhcpOfferSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 25),
    _JnxJdhcpRelayDhcpOfferSent_Type()
)
jnxJdhcpRelayDhcpOfferSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpOfferSent.setStatus("current")
_JnxJdhcpRelayDhcpAckSent_Type = Counter32
_JnxJdhcpRelayDhcpAckSent_Object = MibScalar
jnxJdhcpRelayDhcpAckSent = _JnxJdhcpRelayDhcpAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 26),
    _JnxJdhcpRelayDhcpAckSent_Type()
)
jnxJdhcpRelayDhcpAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpAckSent.setStatus("current")
_JnxJdhcpRelayDhcpNakSent_Type = Counter32
_JnxJdhcpRelayDhcpNakSent_Object = MibScalar
jnxJdhcpRelayDhcpNakSent = _JnxJdhcpRelayDhcpNakSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 27),
    _JnxJdhcpRelayDhcpNakSent_Type()
)
jnxJdhcpRelayDhcpNakSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayDhcpNakSent.setStatus("current")
_JnxJdhcpRelayForceRenewSent_Type = Counter32
_JnxJdhcpRelayForceRenewSent_Object = MibScalar
jnxJdhcpRelayForceRenewSent = _JnxJdhcpRelayForceRenewSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 28),
    _JnxJdhcpRelayForceRenewSent_Type()
)
jnxJdhcpRelayForceRenewSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayForceRenewSent.setStatus("current")
_JnxJdhcpRelayTotalLeaseCount_Type = Counter32
_JnxJdhcpRelayTotalLeaseCount_Object = MibScalar
jnxJdhcpRelayTotalLeaseCount = _JnxJdhcpRelayTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 29),
    _JnxJdhcpRelayTotalLeaseCount_Type()
)
jnxJdhcpRelayTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayTotalLeaseCount.setStatus("current")
_JnxJdhcpRelaySwitchDropped_Type = Counter32
_JnxJdhcpRelaySwitchDropped_Object = MibScalar
jnxJdhcpRelaySwitchDropped = _JnxJdhcpRelaySwitchDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 30),
    _JnxJdhcpRelaySwitchDropped_Type()
)
jnxJdhcpRelaySwitchDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelaySwitchDropped.setStatus("current")
_JnxJdhcpRelayLeaseQuerySent_Type = Counter32
_JnxJdhcpRelayLeaseQuerySent_Object = MibScalar
jnxJdhcpRelayLeaseQuerySent = _JnxJdhcpRelayLeaseQuerySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 31),
    _JnxJdhcpRelayLeaseQuerySent_Type()
)
jnxJdhcpRelayLeaseQuerySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayLeaseQuerySent.setStatus("current")
_JnxJdhcpRelayBulkLeaseQuerySent_Type = Counter32
_JnxJdhcpRelayBulkLeaseQuerySent_Object = MibScalar
jnxJdhcpRelayBulkLeaseQuerySent = _JnxJdhcpRelayBulkLeaseQuerySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 32),
    _JnxJdhcpRelayBulkLeaseQuerySent_Type()
)
jnxJdhcpRelayBulkLeaseQuerySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBulkLeaseQuerySent.setStatus("current")
_JnxJdhcpRelayLeaseActiveReceived_Type = Counter32
_JnxJdhcpRelayLeaseActiveReceived_Object = MibScalar
jnxJdhcpRelayLeaseActiveReceived = _JnxJdhcpRelayLeaseActiveReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 33),
    _JnxJdhcpRelayLeaseActiveReceived_Type()
)
jnxJdhcpRelayLeaseActiveReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayLeaseActiveReceived.setStatus("current")
_JnxJdhcpRelayLeaseUnknownReceived_Type = Counter32
_JnxJdhcpRelayLeaseUnknownReceived_Object = MibScalar
jnxJdhcpRelayLeaseUnknownReceived = _JnxJdhcpRelayLeaseUnknownReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 34),
    _JnxJdhcpRelayLeaseUnknownReceived_Type()
)
jnxJdhcpRelayLeaseUnknownReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayLeaseUnknownReceived.setStatus("current")
_JnxJdhcpRelayLeaseUnAssignedReceived_Type = Counter32
_JnxJdhcpRelayLeaseUnAssignedReceived_Object = MibScalar
jnxJdhcpRelayLeaseUnAssignedReceived = _JnxJdhcpRelayLeaseUnAssignedReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 35),
    _JnxJdhcpRelayLeaseUnAssignedReceived_Type()
)
jnxJdhcpRelayLeaseUnAssignedReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayLeaseUnAssignedReceived.setStatus("current")
_JnxJdhcpRelayLeaseQueryDoneReceived_Type = Counter32
_JnxJdhcpRelayLeaseQueryDoneReceived_Object = MibScalar
jnxJdhcpRelayLeaseQueryDoneReceived = _JnxJdhcpRelayLeaseQueryDoneReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 1, 36),
    _JnxJdhcpRelayLeaseQueryDoneReceived_Type()
)
jnxJdhcpRelayLeaseQueryDoneReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayLeaseQueryDoneReceived.setStatus("current")
_JnxJdhcpRelayBindings_ObjectIdentity = ObjectIdentity
jnxJdhcpRelayBindings = _JnxJdhcpRelayBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2)
)
_JnxJdhcpRelayBindingsTable_Object = MibTable
jnxJdhcpRelayBindingsTable = _JnxJdhcpRelayBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsTable.setStatus("current")
_JnxJdhcpRelayBindingsEntry_Object = MibTableRow
jnxJdhcpRelayBindingsEntry = _JnxJdhcpRelayBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1)
)
jnxJdhcpRelayBindingsEntry.setIndexNames(
    (0, "JUNIPER-JDHCP-MIB", "jnxJdhcpRelayBindingsIpAddress"),
)
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsEntry.setStatus("current")
_JnxJdhcpRelayBindingsIpAddress_Type = IpAddress
_JnxJdhcpRelayBindingsIpAddress_Object = MibTableColumn
jnxJdhcpRelayBindingsIpAddress = _JnxJdhcpRelayBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 1),
    _JnxJdhcpRelayBindingsIpAddress_Type()
)
jnxJdhcpRelayBindingsIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsIpAddress.setStatus("current")


class _JnxJdhcpRelayBindingsLeaseState_Type(Integer32):
    """Custom type jnxJdhcpRelayBindingsLeaseState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("bound", 5),
          ("init", 1),
          ("none", 0),
          ("rebinding", 7),
          ("release", 4),
          ("renewing", 6),
          ("requesting", 3),
          ("selecting", 2))
    )


_JnxJdhcpRelayBindingsLeaseState_Type.__name__ = "Integer32"
_JnxJdhcpRelayBindingsLeaseState_Object = MibTableColumn
jnxJdhcpRelayBindingsLeaseState = _JnxJdhcpRelayBindingsLeaseState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 2),
    _JnxJdhcpRelayBindingsLeaseState_Type()
)
jnxJdhcpRelayBindingsLeaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsLeaseState.setStatus("current")
_JnxJdhcpRelayBindingsLeaseEndTime_Type = DateAndTime
_JnxJdhcpRelayBindingsLeaseEndTime_Object = MibTableColumn
jnxJdhcpRelayBindingsLeaseEndTime = _JnxJdhcpRelayBindingsLeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 3),
    _JnxJdhcpRelayBindingsLeaseEndTime_Type()
)
jnxJdhcpRelayBindingsLeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsLeaseEndTime.setStatus("current")
_JnxJdhcpRelayBindingsLeaseExpireTime_Type = Unsigned32
_JnxJdhcpRelayBindingsLeaseExpireTime_Object = MibTableColumn
jnxJdhcpRelayBindingsLeaseExpireTime = _JnxJdhcpRelayBindingsLeaseExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 4),
    _JnxJdhcpRelayBindingsLeaseExpireTime_Type()
)
jnxJdhcpRelayBindingsLeaseExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsLeaseExpireTime.setStatus("current")
_JnxJdhcpRelayBindingsLeaseStartTime_Type = DateAndTime
_JnxJdhcpRelayBindingsLeaseStartTime_Object = MibTableColumn
jnxJdhcpRelayBindingsLeaseStartTime = _JnxJdhcpRelayBindingsLeaseStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 5),
    _JnxJdhcpRelayBindingsLeaseStartTime_Type()
)
jnxJdhcpRelayBindingsLeaseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsLeaseStartTime.setStatus("current")
_JnxJdhcpRelayBindingsIncomingClientInterface_Type = DisplayString
_JnxJdhcpRelayBindingsIncomingClientInterface_Object = MibTableColumn
jnxJdhcpRelayBindingsIncomingClientInterface = _JnxJdhcpRelayBindingsIncomingClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 6),
    _JnxJdhcpRelayBindingsIncomingClientInterface_Type()
)
jnxJdhcpRelayBindingsIncomingClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsIncomingClientInterface.setStatus("current")
_JnxJdhcpRelayBindingsClientInterfaceVlanId_Type = Unsigned32
_JnxJdhcpRelayBindingsClientInterfaceVlanId_Object = MibTableColumn
jnxJdhcpRelayBindingsClientInterfaceVlanId = _JnxJdhcpRelayBindingsClientInterfaceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 7),
    _JnxJdhcpRelayBindingsClientInterfaceVlanId_Type()
)
jnxJdhcpRelayBindingsClientInterfaceVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsClientInterfaceVlanId.setStatus("current")
_JnxJdhcpRelayBindingsDemuxInterfaceName_Type = DisplayString
_JnxJdhcpRelayBindingsDemuxInterfaceName_Object = MibTableColumn
jnxJdhcpRelayBindingsDemuxInterfaceName = _JnxJdhcpRelayBindingsDemuxInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 8),
    _JnxJdhcpRelayBindingsDemuxInterfaceName_Type()
)
jnxJdhcpRelayBindingsDemuxInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsDemuxInterfaceName.setStatus("current")
_JnxJdhcpRelayBindingsServerIpAddress_Type = IpAddress
_JnxJdhcpRelayBindingsServerIpAddress_Object = MibTableColumn
jnxJdhcpRelayBindingsServerIpAddress = _JnxJdhcpRelayBindingsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 9),
    _JnxJdhcpRelayBindingsServerIpAddress_Type()
)
jnxJdhcpRelayBindingsServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsServerIpAddress.setStatus("current")
_JnxJdhcpRelayBindingsServerInterface_Type = DisplayString
_JnxJdhcpRelayBindingsServerInterface_Object = MibTableColumn
jnxJdhcpRelayBindingsServerInterface = _JnxJdhcpRelayBindingsServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 10),
    _JnxJdhcpRelayBindingsServerInterface_Type()
)
jnxJdhcpRelayBindingsServerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsServerInterface.setStatus("current")
_JnxJdhcpRelayBindingsBootpRelayAddress_Type = IpAddress
_JnxJdhcpRelayBindingsBootpRelayAddress_Object = MibTableColumn
jnxJdhcpRelayBindingsBootpRelayAddress = _JnxJdhcpRelayBindingsBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 11),
    _JnxJdhcpRelayBindingsBootpRelayAddress_Type()
)
jnxJdhcpRelayBindingsBootpRelayAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsBootpRelayAddress.setStatus("current")
_JnxJdhcpRelayBindingsPreviousBootpRelayAddress_Type = IpAddress
_JnxJdhcpRelayBindingsPreviousBootpRelayAddress_Object = MibTableColumn
jnxJdhcpRelayBindingsPreviousBootpRelayAddress = _JnxJdhcpRelayBindingsPreviousBootpRelayAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 12),
    _JnxJdhcpRelayBindingsPreviousBootpRelayAddress_Type()
)
jnxJdhcpRelayBindingsPreviousBootpRelayAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsPreviousBootpRelayAddress.setStatus("current")
_JnxJdhcpRelayBindingsClientProfileName_Type = DisplayString
_JnxJdhcpRelayBindingsClientProfileName_Object = MibTableColumn
jnxJdhcpRelayBindingsClientProfileName = _JnxJdhcpRelayBindingsClientProfileName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 2, 1, 1, 13),
    _JnxJdhcpRelayBindingsClientProfileName_Type()
)
jnxJdhcpRelayBindingsClientProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayBindingsClientProfileName.setStatus("current")
_JnxJdhcpRelayTraps_ObjectIdentity = ObjectIdentity
jnxJdhcpRelayTraps = _JnxJdhcpRelayTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 3)
)
_JnxJdhcpRelayTrapVars_ObjectIdentity = ObjectIdentity
jnxJdhcpRelayTrapVars = _JnxJdhcpRelayTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 4)
)


class _JnxJdhcpRelayRouterName_Type(DisplayString):
    """Custom type jnxJdhcpRelayRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 257),
    )


_JnxJdhcpRelayRouterName_Type.__name__ = "DisplayString"
_JnxJdhcpRelayRouterName_Object = MibScalar
jnxJdhcpRelayRouterName = _JnxJdhcpRelayRouterName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 4, 1),
    _JnxJdhcpRelayRouterName_Type()
)
jnxJdhcpRelayRouterName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpRelayRouterName.setStatus("current")
_JnxJdhcpRelayInterfaceName_Type = DisplayString
_JnxJdhcpRelayInterfaceName_Object = MibScalar
jnxJdhcpRelayInterfaceName = _JnxJdhcpRelayInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 4, 2),
    _JnxJdhcpRelayInterfaceName_Type()
)
jnxJdhcpRelayInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpRelayInterfaceName.setStatus("current")
_JnxJdhcpRelayInterfaceLimit_Type = Unsigned32
_JnxJdhcpRelayInterfaceLimit_Object = MibScalar
jnxJdhcpRelayInterfaceLimit = _JnxJdhcpRelayInterfaceLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 4, 3),
    _JnxJdhcpRelayInterfaceLimit_Type()
)
jnxJdhcpRelayInterfaceLimit.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJdhcpRelayInterfaceLimit.setStatus("current")
_JnxJdhcpRelayIfcStats_ObjectIdentity = ObjectIdentity
jnxJdhcpRelayIfcStats = _JnxJdhcpRelayIfcStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5)
)
_JnxJdhcpRelayIfcStatsTable_Object = MibTable
jnxJdhcpRelayIfcStatsTable = _JnxJdhcpRelayIfcStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1)
)
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsTable.setStatus("current")
_JnxJdhcpRelayIfcStatsEntry_Object = MibTableRow
jnxJdhcpRelayIfcStatsEntry = _JnxJdhcpRelayIfcStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1)
)
jnxJdhcpRelayIfcStatsEntry.setIndexNames(
    (0, "JUNIPER-JDHCP-MIB", "jnxJdhcpRelayIfcStatsIfIndex"),
)
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsEntry.setStatus("current")
_JnxJdhcpRelayIfcStatsIfIndex_Type = InterfaceIndex
_JnxJdhcpRelayIfcStatsIfIndex_Object = MibTableColumn
jnxJdhcpRelayIfcStatsIfIndex = _JnxJdhcpRelayIfcStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 1),
    _JnxJdhcpRelayIfcStatsIfIndex_Type()
)
jnxJdhcpRelayIfcStatsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsIfIndex.setStatus("current")
_JnxJdhcpRelayIfcStatsTotalDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsTotalDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsTotalDropped = _JnxJdhcpRelayIfcStatsTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 2),
    _JnxJdhcpRelayIfcStatsTotalDropped_Type()
)
jnxJdhcpRelayIfcStatsTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsTotalDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsBadHardwareDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsBadHardwareDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBadHardwareDropped = _JnxJdhcpRelayIfcStatsBadHardwareDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 3),
    _JnxJdhcpRelayIfcStatsBadHardwareDropped_Type()
)
jnxJdhcpRelayIfcStatsBadHardwareDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBadHardwareDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsBadBootpOpcodeDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsBadBootpOpcodeDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBadBootpOpcodeDropped = _JnxJdhcpRelayIfcStatsBadBootpOpcodeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 4),
    _JnxJdhcpRelayIfcStatsBadBootpOpcodeDropped_Type()
)
jnxJdhcpRelayIfcStatsBadBootpOpcodeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBadBootpOpcodeDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsBadOptionsDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsBadOptionsDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBadOptionsDropped = _JnxJdhcpRelayIfcStatsBadOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 5),
    _JnxJdhcpRelayIfcStatsBadOptionsDropped_Type()
)
jnxJdhcpRelayIfcStatsBadOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBadOptionsDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsBadAddressDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsBadAddressDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBadAddressDropped = _JnxJdhcpRelayIfcStatsBadAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 6),
    _JnxJdhcpRelayIfcStatsBadAddressDropped_Type()
)
jnxJdhcpRelayIfcStatsBadAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBadAddressDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsNoAddressDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsNoAddressDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsNoAddressDropped = _JnxJdhcpRelayIfcStatsNoAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 7),
    _JnxJdhcpRelayIfcStatsNoAddressDropped_Type()
)
jnxJdhcpRelayIfcStatsNoAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsNoAddressDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsNoInterfaceCfgDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsNoInterfaceCfgDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsNoInterfaceCfgDropped = _JnxJdhcpRelayIfcStatsNoInterfaceCfgDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 8),
    _JnxJdhcpRelayIfcStatsNoInterfaceCfgDropped_Type()
)
jnxJdhcpRelayIfcStatsNoInterfaceCfgDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsNoInterfaceCfgDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsNoLocalAddressDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsNoLocalAddressDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsNoLocalAddressDropped = _JnxJdhcpRelayIfcStatsNoLocalAddressDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 9),
    _JnxJdhcpRelayIfcStatsNoLocalAddressDropped_Type()
)
jnxJdhcpRelayIfcStatsNoLocalAddressDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsNoLocalAddressDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsShortPacketDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsShortPacketDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsShortPacketDropped = _JnxJdhcpRelayIfcStatsShortPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 10),
    _JnxJdhcpRelayIfcStatsShortPacketDropped_Type()
)
jnxJdhcpRelayIfcStatsShortPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsShortPacketDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsBadSendDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsBadSendDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBadSendDropped = _JnxJdhcpRelayIfcStatsBadSendDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 11),
    _JnxJdhcpRelayIfcStatsBadSendDropped_Type()
)
jnxJdhcpRelayIfcStatsBadSendDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBadSendDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsAuthenticationDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsAuthenticationDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsAuthenticationDropped = _JnxJdhcpRelayIfcStatsAuthenticationDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 12),
    _JnxJdhcpRelayIfcStatsAuthenticationDropped_Type()
)
jnxJdhcpRelayIfcStatsAuthenticationDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsAuthenticationDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsDynamicProfileDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsDynamicProfileDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDynamicProfileDropped = _JnxJdhcpRelayIfcStatsDynamicProfileDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 13),
    _JnxJdhcpRelayIfcStatsDynamicProfileDropped_Type()
)
jnxJdhcpRelayIfcStatsDynamicProfileDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDynamicProfileDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsLicenseDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsLicenseDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsLicenseDropped = _JnxJdhcpRelayIfcStatsLicenseDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 14),
    _JnxJdhcpRelayIfcStatsLicenseDropped_Type()
)
jnxJdhcpRelayIfcStatsLicenseDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsLicenseDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsBootRequestReceived_Type = Counter32
_JnxJdhcpRelayIfcStatsBootRequestReceived_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBootRequestReceived = _JnxJdhcpRelayIfcStatsBootRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 15),
    _JnxJdhcpRelayIfcStatsBootRequestReceived_Type()
)
jnxJdhcpRelayIfcStatsBootRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBootRequestReceived.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpDeclineReceived_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpDeclineReceived_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpDeclineReceived = _JnxJdhcpRelayIfcStatsDhcpDeclineReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 16),
    _JnxJdhcpRelayIfcStatsDhcpDeclineReceived_Type()
)
jnxJdhcpRelayIfcStatsDhcpDeclineReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpDeclineReceived.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpDiscoverReceived_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpDiscoverReceived_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpDiscoverReceived = _JnxJdhcpRelayIfcStatsDhcpDiscoverReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 17),
    _JnxJdhcpRelayIfcStatsDhcpDiscoverReceived_Type()
)
jnxJdhcpRelayIfcStatsDhcpDiscoverReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpDiscoverReceived.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpInformReceived_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpInformReceived_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpInformReceived = _JnxJdhcpRelayIfcStatsDhcpInformReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 18),
    _JnxJdhcpRelayIfcStatsDhcpInformReceived_Type()
)
jnxJdhcpRelayIfcStatsDhcpInformReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpInformReceived.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpReleaseReceived_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpReleaseReceived_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpReleaseReceived = _JnxJdhcpRelayIfcStatsDhcpReleaseReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 19),
    _JnxJdhcpRelayIfcStatsDhcpReleaseReceived_Type()
)
jnxJdhcpRelayIfcStatsDhcpReleaseReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpReleaseReceived.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpRequestReceived_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpRequestReceived_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpRequestReceived = _JnxJdhcpRelayIfcStatsDhcpRequestReceived_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 20),
    _JnxJdhcpRelayIfcStatsDhcpRequestReceived_Type()
)
jnxJdhcpRelayIfcStatsDhcpRequestReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpRequestReceived.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpBootReplySent_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpBootReplySent_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpBootReplySent = _JnxJdhcpRelayIfcStatsDhcpBootReplySent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 21),
    _JnxJdhcpRelayIfcStatsDhcpBootReplySent_Type()
)
jnxJdhcpRelayIfcStatsDhcpBootReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpBootReplySent.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpOfferSent_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpOfferSent_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpOfferSent = _JnxJdhcpRelayIfcStatsDhcpOfferSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 22),
    _JnxJdhcpRelayIfcStatsDhcpOfferSent_Type()
)
jnxJdhcpRelayIfcStatsDhcpOfferSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpOfferSent.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpAckSent_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpAckSent_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpAckSent = _JnxJdhcpRelayIfcStatsDhcpAckSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 23),
    _JnxJdhcpRelayIfcStatsDhcpAckSent_Type()
)
jnxJdhcpRelayIfcStatsDhcpAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpAckSent.setStatus("current")
_JnxJdhcpRelayIfcStatsDhcpNakSent_Type = Counter32
_JnxJdhcpRelayIfcStatsDhcpNakSent_Object = MibTableColumn
jnxJdhcpRelayIfcStatsDhcpNakSent = _JnxJdhcpRelayIfcStatsDhcpNakSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 24),
    _JnxJdhcpRelayIfcStatsDhcpNakSent_Type()
)
jnxJdhcpRelayIfcStatsDhcpNakSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsDhcpNakSent.setStatus("current")
_JnxJdhcpRelayIfcStatsForceRenewSent_Type = Counter32
_JnxJdhcpRelayIfcStatsForceRenewSent_Object = MibTableColumn
jnxJdhcpRelayIfcStatsForceRenewSent = _JnxJdhcpRelayIfcStatsForceRenewSent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 25),
    _JnxJdhcpRelayIfcStatsForceRenewSent_Type()
)
jnxJdhcpRelayIfcStatsForceRenewSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsForceRenewSent.setStatus("current")
_JnxJdhcpRelayIfcStatsTotalLeaseCount_Type = Counter32
_JnxJdhcpRelayIfcStatsTotalLeaseCount_Object = MibTableColumn
jnxJdhcpRelayIfcStatsTotalLeaseCount = _JnxJdhcpRelayIfcStatsTotalLeaseCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 26),
    _JnxJdhcpRelayIfcStatsTotalLeaseCount_Type()
)
jnxJdhcpRelayIfcStatsTotalLeaseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsTotalLeaseCount.setStatus("current")
_JnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped = _JnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 27),
    _JnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped_Type()
)
jnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsNoOptionsDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsNoOptionsDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsNoOptionsDropped = _JnxJdhcpRelayIfcStatsNoOptionsDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 28),
    _JnxJdhcpRelayIfcStatsNoOptionsDropped_Type()
)
jnxJdhcpRelayIfcStatsNoOptionsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsNoOptionsDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsHopLimitDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsHopLimitDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsHopLimitDropped = _JnxJdhcpRelayIfcStatsHopLimitDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 29),
    _JnxJdhcpRelayIfcStatsHopLimitDropped_Type()
)
jnxJdhcpRelayIfcStatsHopLimitDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsHopLimitDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsTtlExpiredDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsTtlExpiredDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsTtlExpiredDropped = _JnxJdhcpRelayIfcStatsTtlExpiredDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 30),
    _JnxJdhcpRelayIfcStatsTtlExpiredDropped_Type()
)
jnxJdhcpRelayIfcStatsTtlExpiredDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsTtlExpiredDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsBadUdpCksumDropped_Type = Counter32
_JnxJdhcpRelayIfcStatsBadUdpCksumDropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsBadUdpCksumDropped = _JnxJdhcpRelayIfcStatsBadUdpCksumDropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 31),
    _JnxJdhcpRelayIfcStatsBadUdpCksumDropped_Type()
)
jnxJdhcpRelayIfcStatsBadUdpCksumDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsBadUdpCksumDropped.setStatus("current")
_JnxJdhcpRelayIfcStatsOption82Dropped_Type = Counter32
_JnxJdhcpRelayIfcStatsOption82Dropped_Object = MibTableColumn
jnxJdhcpRelayIfcStatsOption82Dropped = _JnxJdhcpRelayIfcStatsOption82Dropped_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 5, 1, 1, 32),
    _JnxJdhcpRelayIfcStatsOption82Dropped_Type()
)
jnxJdhcpRelayIfcStatsOption82Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJdhcpRelayIfcStatsOption82Dropped.setStatus("current")

# Managed Objects groups


# Notification objects

jnxJdhcpLocalServerDuplicateClient = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 3, 1)
)
jnxJdhcpLocalServerDuplicateClient.setObjects(
      *(("JUNIPER-JDHCP-MIB", "jnxJdhcpRouterName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerMacAddress"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerInterfaceName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerLastDetected"))
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerDuplicateClient.setStatus(
        "current"
    )

jnxJdhcpLocalServerInterfaceLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 3, 2)
)
jnxJdhcpLocalServerInterfaceLimitExceeded.setObjects(
      *(("JUNIPER-JDHCP-MIB", "jnxJdhcpRouterName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerInterfaceName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerInterfaceLimitExceeded.setStatus(
        "current"
    )

jnxJdhcpLocalServerInterfaceLimitAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 3, 3)
)
jnxJdhcpLocalServerInterfaceLimitAbated.setObjects(
      *(("JUNIPER-JDHCP-MIB", "jnxJdhcpRouterName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerInterfaceName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerInterfaceLimitAbated.setStatus(
        "current"
    )

jnxJdhcpLocalServerHealth = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 1, 3, 4)
)
jnxJdhcpLocalServerHealth.setObjects(
      *(("JUNIPER-JDHCP-MIB", "jnxJdhcpRouterName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerEventSeverity"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpLocalServerEventString"))
)
if mibBuilder.loadTexts:
    jnxJdhcpLocalServerHealth.setStatus(
        "current"
    )

jnxJdhcpRelayInterfaceLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 3, 1)
)
jnxJdhcpRelayInterfaceLimitExceeded.setObjects(
      *(("JUNIPER-JDHCP-MIB", "jnxJdhcpRelayRouterName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpRelayInterfaceName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpRelayInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpRelayInterfaceLimitExceeded.setStatus(
        "current"
    )

jnxJdhcpRelayInterfaceLimitAbated = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 61, 61, 2, 3, 2)
)
jnxJdhcpRelayInterfaceLimitAbated.setObjects(
      *(("JUNIPER-JDHCP-MIB", "jnxJdhcpRelayRouterName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpRelayInterfaceName"),
        ("JUNIPER-JDHCP-MIB", "jnxJdhcpRelayInterfaceLimit"))
)
if mibBuilder.loadTexts:
    jnxJdhcpRelayInterfaceLimitAbated.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JDHCP-MIB",
    **{"jnxJdhcpMIB": jnxJdhcpMIB,
       "jnxJdhcpLocalServerObjects": jnxJdhcpLocalServerObjects,
       "jnxJdhcpLocalServerStatistics": jnxJdhcpLocalServerStatistics,
       "jnxJdhcpLocalServerTotalDropped": jnxJdhcpLocalServerTotalDropped,
       "jnxJdhcpLocalServerBadHardwareDropped": jnxJdhcpLocalServerBadHardwareDropped,
       "jnxJdhcpLocalServerBadBootpOpcodeDropped": jnxJdhcpLocalServerBadBootpOpcodeDropped,
       "jnxJdhcpLocalServerBadOptionsDropped": jnxJdhcpLocalServerBadOptionsDropped,
       "jnxJdhcpLocalServerBadAddressDropped": jnxJdhcpLocalServerBadAddressDropped,
       "jnxJdhcpLocalServerNoAddressDropped": jnxJdhcpLocalServerNoAddressDropped,
       "jnxJdhcpLocalServerNoInterfaceDropped": jnxJdhcpLocalServerNoInterfaceDropped,
       "jnxJdhcpLocalServerNoRoutingInstanceDropped": jnxJdhcpLocalServerNoRoutingInstanceDropped,
       "jnxJdhcpLocalServerNoLocalAddressDropped": jnxJdhcpLocalServerNoLocalAddressDropped,
       "jnxJdhcpLocalServerShortPacketDropped": jnxJdhcpLocalServerShortPacketDropped,
       "jnxJdhcpLocalServerBadReadDropped": jnxJdhcpLocalServerBadReadDropped,
       "jnxJdhcpLocalServerBadSendDropped": jnxJdhcpLocalServerBadSendDropped,
       "jnxJdhcpLocalServerAuthenticationDropped": jnxJdhcpLocalServerAuthenticationDropped,
       "jnxJdhcpLocalServerDynamicProfileDropped": jnxJdhcpLocalServerDynamicProfileDropped,
       "jnxJdhcpLocalServerLicenseDropped": jnxJdhcpLocalServerLicenseDropped,
       "jnxJdhcpLocalServerBootRequestReceived": jnxJdhcpLocalServerBootRequestReceived,
       "jnxJdhcpLocalServerDhcpDeclineReceived": jnxJdhcpLocalServerDhcpDeclineReceived,
       "jnxJdhcpLocalServerDhcpDiscoverReceived": jnxJdhcpLocalServerDhcpDiscoverReceived,
       "jnxJdhcpLocalServerDhcpInformReceived": jnxJdhcpLocalServerDhcpInformReceived,
       "jnxJdhcpLocalServerDhcpReleaseReceived": jnxJdhcpLocalServerDhcpReleaseReceived,
       "jnxJdhcpLocalServerDhcpRequestReceived": jnxJdhcpLocalServerDhcpRequestReceived,
       "jnxJdhcpLocalServerDhcpBootReplySent": jnxJdhcpLocalServerDhcpBootReplySent,
       "jnxJdhcpLocalServerDhcpOfferSent": jnxJdhcpLocalServerDhcpOfferSent,
       "jnxJdhcpLocalServerDhcpAckSent": jnxJdhcpLocalServerDhcpAckSent,
       "jnxJdhcpLocalServerDhcpNakSent": jnxJdhcpLocalServerDhcpNakSent,
       "jnxJdhcpLocalServerForceRenewSent": jnxJdhcpLocalServerForceRenewSent,
       "jnxJdhcpLocalServerTotalLeaseCount": jnxJdhcpLocalServerTotalLeaseCount,
       "jnxJdhcpLocalServerSwitchDropped": jnxJdhcpLocalServerSwitchDropped,
       "jnxJdhcpLocalServerLeaseQueryReceived": jnxJdhcpLocalServerLeaseQueryReceived,
       "jnxJdhcpLocalServerBulkLeaseQueryReceived": jnxJdhcpLocalServerBulkLeaseQueryReceived,
       "jnxJdhcpLocalServerLeaseActiveSent": jnxJdhcpLocalServerLeaseActiveSent,
       "jnxJdhcpLocalServerLeaseUnknownSent": jnxJdhcpLocalServerLeaseUnknownSent,
       "jnxJdhcpLocalServerLeaseUnAssignedSent": jnxJdhcpLocalServerLeaseUnAssignedSent,
       "jnxJdhcpLocalServerLeaseQueryDoneSent": jnxJdhcpLocalServerLeaseQueryDoneSent,
       "jnxJdhcpLocalServerBindings": jnxJdhcpLocalServerBindings,
       "jnxJdhcpLocalServerBindingsTable": jnxJdhcpLocalServerBindingsTable,
       "jnxJdhcpLocalServerBindingsEntry": jnxJdhcpLocalServerBindingsEntry,
       "jnxJdhcpLocalServerBindingsIpAddress": jnxJdhcpLocalServerBindingsIpAddress,
       "jnxJdhcpLocalServerBindingsMacAddress": jnxJdhcpLocalServerBindingsMacAddress,
       "jnxJdhcpLocalServerBindingsState": jnxJdhcpLocalServerBindingsState,
       "jnxJdhcpLocalServerBindingsLeaseEndTime": jnxJdhcpLocalServerBindingsLeaseEndTime,
       "jnxJdhcpLocalServerBindingsLeaseExpireTime": jnxJdhcpLocalServerBindingsLeaseExpireTime,
       "jnxJdhcpLocalServerBindingsLeaseStartTime": jnxJdhcpLocalServerBindingsLeaseStartTime,
       "jnxJdhcpLocalServerBindingsIncomingClientInterface": jnxJdhcpLocalServerBindingsIncomingClientInterface,
       "jnxJdhcpLocalServerBindingsClientInterfaceVlanId": jnxJdhcpLocalServerBindingsClientInterfaceVlanId,
       "jnxJdhcpLocalServerBindingsDemuxInterfaceName": jnxJdhcpLocalServerBindingsDemuxInterfaceName,
       "jnxJdhcpLocalServerBindingsServerIpAddress": jnxJdhcpLocalServerBindingsServerIpAddress,
       "jnxJdhcpLocalServerBindingsBootpRelayAddress": jnxJdhcpLocalServerBindingsBootpRelayAddress,
       "jnxJdhcpLocalServerBindingsPreviousBootpRelayAddress": jnxJdhcpLocalServerBindingsPreviousBootpRelayAddress,
       "jnxJdhcpLocalServerBindingsClientPoolName": jnxJdhcpLocalServerBindingsClientPoolName,
       "jnxJdhcpLocalServerBindingsClientProfileName": jnxJdhcpLocalServerBindingsClientProfileName,
       "jnxJdhcpLocalServerTraps": jnxJdhcpLocalServerTraps,
       "jnxJdhcpLocalServerDuplicateClient": jnxJdhcpLocalServerDuplicateClient,
       "jnxJdhcpLocalServerInterfaceLimitExceeded": jnxJdhcpLocalServerInterfaceLimitExceeded,
       "jnxJdhcpLocalServerInterfaceLimitAbated": jnxJdhcpLocalServerInterfaceLimitAbated,
       "jnxJdhcpLocalServerHealth": jnxJdhcpLocalServerHealth,
       "jnxJdhcpLocalServerTrapVars": jnxJdhcpLocalServerTrapVars,
       "jnxJdhcpLocalServerLastDetected": jnxJdhcpLocalServerLastDetected,
       "jnxJdhcpRouterName": jnxJdhcpRouterName,
       "jnxJdhcpLocalServerMacAddress": jnxJdhcpLocalServerMacAddress,
       "jnxJdhcpLocalServerInterfaceName": jnxJdhcpLocalServerInterfaceName,
       "jnxJdhcpLocalServerInterfaceLimit": jnxJdhcpLocalServerInterfaceLimit,
       "jnxJdhcpLocalServerEventSeverity": jnxJdhcpLocalServerEventSeverity,
       "jnxJdhcpLocalServerEventString": jnxJdhcpLocalServerEventString,
       "jnxJdhcpLocalServerIfcStats": jnxJdhcpLocalServerIfcStats,
       "jnxJdhcpLocalServerIfcStatsTable": jnxJdhcpLocalServerIfcStatsTable,
       "jnxJdhcpLocalServerIfcStatsEntry": jnxJdhcpLocalServerIfcStatsEntry,
       "jnxJdhcpLocalServerIfcStatsIfIndex": jnxJdhcpLocalServerIfcStatsIfIndex,
       "jnxJdhcpLocalServerIfcStatsTotalDropped": jnxJdhcpLocalServerIfcStatsTotalDropped,
       "jnxJdhcpLocalServerIfcStatsBadHardwareDropped": jnxJdhcpLocalServerIfcStatsBadHardwareDropped,
       "jnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped": jnxJdhcpLocalServerIfcStatsBadBootpOpcodeDropped,
       "jnxJdhcpLocalServerIfcStatsBadOptionsDropped": jnxJdhcpLocalServerIfcStatsBadOptionsDropped,
       "jnxJdhcpLocalServerIfcStatsBadAddressDropped": jnxJdhcpLocalServerIfcStatsBadAddressDropped,
       "jnxJdhcpLocalServerIfcStatsNoAddressDropped": jnxJdhcpLocalServerIfcStatsNoAddressDropped,
       "jnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped": jnxJdhcpLocalServerIfcStatsNoInterfaceCfgDropped,
       "jnxJdhcpLocalServerIfcStatsNoLocalAddressDropped": jnxJdhcpLocalServerIfcStatsNoLocalAddressDropped,
       "jnxJdhcpLocalServerIfcStatsShortPacketDropped": jnxJdhcpLocalServerIfcStatsShortPacketDropped,
       "jnxJdhcpLocalServerIfcStatsBadSendDropped": jnxJdhcpLocalServerIfcStatsBadSendDropped,
       "jnxJdhcpLocalServerIfcStatsAuthenticationDropped": jnxJdhcpLocalServerIfcStatsAuthenticationDropped,
       "jnxJdhcpLocalServerIfcStatsDynamicProfileDropped": jnxJdhcpLocalServerIfcStatsDynamicProfileDropped,
       "jnxJdhcpLocalServerIfcStatsLicenseDropped": jnxJdhcpLocalServerIfcStatsLicenseDropped,
       "jnxJdhcpLocalServerIfcStatsBootRequestReceived": jnxJdhcpLocalServerIfcStatsBootRequestReceived,
       "jnxJdhcpLocalServerIfcStatsDhcpDeclineReceived": jnxJdhcpLocalServerIfcStatsDhcpDeclineReceived,
       "jnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived": jnxJdhcpLocalServerIfcStatsDhcpDiscoverReceived,
       "jnxJdhcpLocalServerIfcStatsDhcpInformReceived": jnxJdhcpLocalServerIfcStatsDhcpInformReceived,
       "jnxJdhcpLocalServerIfcStatsDhcpReleaseReceived": jnxJdhcpLocalServerIfcStatsDhcpReleaseReceived,
       "jnxJdhcpLocalServerIfcStatsDhcpRequestReceived": jnxJdhcpLocalServerIfcStatsDhcpRequestReceived,
       "jnxJdhcpLocalServerIfcStatsDhcpBootReplySent": jnxJdhcpLocalServerIfcStatsDhcpBootReplySent,
       "jnxJdhcpLocalServerIfcStatsDhcpOfferSent": jnxJdhcpLocalServerIfcStatsDhcpOfferSent,
       "jnxJdhcpLocalServerIfcStatsDhcpAckSent": jnxJdhcpLocalServerIfcStatsDhcpAckSent,
       "jnxJdhcpLocalServerIfcStatsDhcpNakSent": jnxJdhcpLocalServerIfcStatsDhcpNakSent,
       "jnxJdhcpLocalServerIfcStatsForceRenewSent": jnxJdhcpLocalServerIfcStatsForceRenewSent,
       "jnxJdhcpLocalServerIfcStatsTotalLeaseCount": jnxJdhcpLocalServerIfcStatsTotalLeaseCount,
       "jnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped": jnxJdhcpLocalServerIfcStatsBadDhcpOpcodeDropped,
       "jnxJdhcpLocalServerIfcStatsNoOptionsDropped": jnxJdhcpLocalServerIfcStatsNoOptionsDropped,
       "jnxJdhcpLocalServerIfcStatsHopLimitDropped": jnxJdhcpLocalServerIfcStatsHopLimitDropped,
       "jnxJdhcpLocalServerIfcStatsTtlExpiredDropped": jnxJdhcpLocalServerIfcStatsTtlExpiredDropped,
       "jnxJdhcpLocalServerIfcStatsBadUdpCksumDropped": jnxJdhcpLocalServerIfcStatsBadUdpCksumDropped,
       "jnxJdhcpLocalServerIfcStatsOption60Dropped": jnxJdhcpLocalServerIfcStatsOption60Dropped,
       "jnxJdhcpRelayObjects": jnxJdhcpRelayObjects,
       "jnxJdhcpRelayStatistics": jnxJdhcpRelayStatistics,
       "jnxJdhcpRelayTotalDropped": jnxJdhcpRelayTotalDropped,
       "jnxJdhcpRelayBadHardwareDropped": jnxJdhcpRelayBadHardwareDropped,
       "jnxJdhcpRelayBadBootpOpcodeDropped": jnxJdhcpRelayBadBootpOpcodeDropped,
       "jnxJdhcpRelayBadOptionsDropped": jnxJdhcpRelayBadOptionsDropped,
       "jnxJdhcpRelayBadAddressDropped": jnxJdhcpRelayBadAddressDropped,
       "jnxJdhcpRelayNoAddressDropped": jnxJdhcpRelayNoAddressDropped,
       "jnxJdhcpRelayNoInterfaceDropped": jnxJdhcpRelayNoInterfaceDropped,
       "jnxJdhcpRelayNoRoutingInstanceDropped": jnxJdhcpRelayNoRoutingInstanceDropped,
       "jnxJdhcpRelayNoLocalAddressDropped": jnxJdhcpRelayNoLocalAddressDropped,
       "jnxJdhcpRelayShortPacketDropped": jnxJdhcpRelayShortPacketDropped,
       "jnxJdhcpRelayBadReadDropped": jnxJdhcpRelayBadReadDropped,
       "jnxJdhcpRelayBadSendDropped": jnxJdhcpRelayBadSendDropped,
       "jnxJdhcpRelayOption82Dropped": jnxJdhcpRelayOption82Dropped,
       "jnxJdhcpRelayOption60Dropped": jnxJdhcpRelayOption60Dropped,
       "jnxJdhcpRelayAuthenticationDropped": jnxJdhcpRelayAuthenticationDropped,
       "jnxJdhcpRelayDynamicProfileDropped": jnxJdhcpRelayDynamicProfileDropped,
       "jnxJdhcpRelayLicenseDropped": jnxJdhcpRelayLicenseDropped,
       "jnxJdhcpRelayBootRequestReceived": jnxJdhcpRelayBootRequestReceived,
       "jnxJdhcpRelayDhcpDeclineReceived": jnxJdhcpRelayDhcpDeclineReceived,
       "jnxJdhcpRelayDhcpDiscoverReceived": jnxJdhcpRelayDhcpDiscoverReceived,
       "jnxJdhcpRelayDhcpInformReceived": jnxJdhcpRelayDhcpInformReceived,
       "jnxJdhcpRelayDhcpReleaseReceived": jnxJdhcpRelayDhcpReleaseReceived,
       "jnxJdhcpRelayDhcpRequestReceived": jnxJdhcpRelayDhcpRequestReceived,
       "jnxJdhcpRelayDhcpBootReplySent": jnxJdhcpRelayDhcpBootReplySent,
       "jnxJdhcpRelayDhcpOfferSent": jnxJdhcpRelayDhcpOfferSent,
       "jnxJdhcpRelayDhcpAckSent": jnxJdhcpRelayDhcpAckSent,
       "jnxJdhcpRelayDhcpNakSent": jnxJdhcpRelayDhcpNakSent,
       "jnxJdhcpRelayForceRenewSent": jnxJdhcpRelayForceRenewSent,
       "jnxJdhcpRelayTotalLeaseCount": jnxJdhcpRelayTotalLeaseCount,
       "jnxJdhcpRelaySwitchDropped": jnxJdhcpRelaySwitchDropped,
       "jnxJdhcpRelayLeaseQuerySent": jnxJdhcpRelayLeaseQuerySent,
       "jnxJdhcpRelayBulkLeaseQuerySent": jnxJdhcpRelayBulkLeaseQuerySent,
       "jnxJdhcpRelayLeaseActiveReceived": jnxJdhcpRelayLeaseActiveReceived,
       "jnxJdhcpRelayLeaseUnknownReceived": jnxJdhcpRelayLeaseUnknownReceived,
       "jnxJdhcpRelayLeaseUnAssignedReceived": jnxJdhcpRelayLeaseUnAssignedReceived,
       "jnxJdhcpRelayLeaseQueryDoneReceived": jnxJdhcpRelayLeaseQueryDoneReceived,
       "jnxJdhcpRelayBindings": jnxJdhcpRelayBindings,
       "jnxJdhcpRelayBindingsTable": jnxJdhcpRelayBindingsTable,
       "jnxJdhcpRelayBindingsEntry": jnxJdhcpRelayBindingsEntry,
       "jnxJdhcpRelayBindingsIpAddress": jnxJdhcpRelayBindingsIpAddress,
       "jnxJdhcpRelayBindingsLeaseState": jnxJdhcpRelayBindingsLeaseState,
       "jnxJdhcpRelayBindingsLeaseEndTime": jnxJdhcpRelayBindingsLeaseEndTime,
       "jnxJdhcpRelayBindingsLeaseExpireTime": jnxJdhcpRelayBindingsLeaseExpireTime,
       "jnxJdhcpRelayBindingsLeaseStartTime": jnxJdhcpRelayBindingsLeaseStartTime,
       "jnxJdhcpRelayBindingsIncomingClientInterface": jnxJdhcpRelayBindingsIncomingClientInterface,
       "jnxJdhcpRelayBindingsClientInterfaceVlanId": jnxJdhcpRelayBindingsClientInterfaceVlanId,
       "jnxJdhcpRelayBindingsDemuxInterfaceName": jnxJdhcpRelayBindingsDemuxInterfaceName,
       "jnxJdhcpRelayBindingsServerIpAddress": jnxJdhcpRelayBindingsServerIpAddress,
       "jnxJdhcpRelayBindingsServerInterface": jnxJdhcpRelayBindingsServerInterface,
       "jnxJdhcpRelayBindingsBootpRelayAddress": jnxJdhcpRelayBindingsBootpRelayAddress,
       "jnxJdhcpRelayBindingsPreviousBootpRelayAddress": jnxJdhcpRelayBindingsPreviousBootpRelayAddress,
       "jnxJdhcpRelayBindingsClientProfileName": jnxJdhcpRelayBindingsClientProfileName,
       "jnxJdhcpRelayTraps": jnxJdhcpRelayTraps,
       "jnxJdhcpRelayInterfaceLimitExceeded": jnxJdhcpRelayInterfaceLimitExceeded,
       "jnxJdhcpRelayInterfaceLimitAbated": jnxJdhcpRelayInterfaceLimitAbated,
       "jnxJdhcpRelayTrapVars": jnxJdhcpRelayTrapVars,
       "jnxJdhcpRelayRouterName": jnxJdhcpRelayRouterName,
       "jnxJdhcpRelayInterfaceName": jnxJdhcpRelayInterfaceName,
       "jnxJdhcpRelayInterfaceLimit": jnxJdhcpRelayInterfaceLimit,
       "jnxJdhcpRelayIfcStats": jnxJdhcpRelayIfcStats,
       "jnxJdhcpRelayIfcStatsTable": jnxJdhcpRelayIfcStatsTable,
       "jnxJdhcpRelayIfcStatsEntry": jnxJdhcpRelayIfcStatsEntry,
       "jnxJdhcpRelayIfcStatsIfIndex": jnxJdhcpRelayIfcStatsIfIndex,
       "jnxJdhcpRelayIfcStatsTotalDropped": jnxJdhcpRelayIfcStatsTotalDropped,
       "jnxJdhcpRelayIfcStatsBadHardwareDropped": jnxJdhcpRelayIfcStatsBadHardwareDropped,
       "jnxJdhcpRelayIfcStatsBadBootpOpcodeDropped": jnxJdhcpRelayIfcStatsBadBootpOpcodeDropped,
       "jnxJdhcpRelayIfcStatsBadOptionsDropped": jnxJdhcpRelayIfcStatsBadOptionsDropped,
       "jnxJdhcpRelayIfcStatsBadAddressDropped": jnxJdhcpRelayIfcStatsBadAddressDropped,
       "jnxJdhcpRelayIfcStatsNoAddressDropped": jnxJdhcpRelayIfcStatsNoAddressDropped,
       "jnxJdhcpRelayIfcStatsNoInterfaceCfgDropped": jnxJdhcpRelayIfcStatsNoInterfaceCfgDropped,
       "jnxJdhcpRelayIfcStatsNoLocalAddressDropped": jnxJdhcpRelayIfcStatsNoLocalAddressDropped,
       "jnxJdhcpRelayIfcStatsShortPacketDropped": jnxJdhcpRelayIfcStatsShortPacketDropped,
       "jnxJdhcpRelayIfcStatsBadSendDropped": jnxJdhcpRelayIfcStatsBadSendDropped,
       "jnxJdhcpRelayIfcStatsAuthenticationDropped": jnxJdhcpRelayIfcStatsAuthenticationDropped,
       "jnxJdhcpRelayIfcStatsDynamicProfileDropped": jnxJdhcpRelayIfcStatsDynamicProfileDropped,
       "jnxJdhcpRelayIfcStatsLicenseDropped": jnxJdhcpRelayIfcStatsLicenseDropped,
       "jnxJdhcpRelayIfcStatsBootRequestReceived": jnxJdhcpRelayIfcStatsBootRequestReceived,
       "jnxJdhcpRelayIfcStatsDhcpDeclineReceived": jnxJdhcpRelayIfcStatsDhcpDeclineReceived,
       "jnxJdhcpRelayIfcStatsDhcpDiscoverReceived": jnxJdhcpRelayIfcStatsDhcpDiscoverReceived,
       "jnxJdhcpRelayIfcStatsDhcpInformReceived": jnxJdhcpRelayIfcStatsDhcpInformReceived,
       "jnxJdhcpRelayIfcStatsDhcpReleaseReceived": jnxJdhcpRelayIfcStatsDhcpReleaseReceived,
       "jnxJdhcpRelayIfcStatsDhcpRequestReceived": jnxJdhcpRelayIfcStatsDhcpRequestReceived,
       "jnxJdhcpRelayIfcStatsDhcpBootReplySent": jnxJdhcpRelayIfcStatsDhcpBootReplySent,
       "jnxJdhcpRelayIfcStatsDhcpOfferSent": jnxJdhcpRelayIfcStatsDhcpOfferSent,
       "jnxJdhcpRelayIfcStatsDhcpAckSent": jnxJdhcpRelayIfcStatsDhcpAckSent,
       "jnxJdhcpRelayIfcStatsDhcpNakSent": jnxJdhcpRelayIfcStatsDhcpNakSent,
       "jnxJdhcpRelayIfcStatsForceRenewSent": jnxJdhcpRelayIfcStatsForceRenewSent,
       "jnxJdhcpRelayIfcStatsTotalLeaseCount": jnxJdhcpRelayIfcStatsTotalLeaseCount,
       "jnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped": jnxJdhcpRelayIfcStatsBadDhcpOpcodeDropped,
       "jnxJdhcpRelayIfcStatsNoOptionsDropped": jnxJdhcpRelayIfcStatsNoOptionsDropped,
       "jnxJdhcpRelayIfcStatsHopLimitDropped": jnxJdhcpRelayIfcStatsHopLimitDropped,
       "jnxJdhcpRelayIfcStatsTtlExpiredDropped": jnxJdhcpRelayIfcStatsTtlExpiredDropped,
       "jnxJdhcpRelayIfcStatsBadUdpCksumDropped": jnxJdhcpRelayIfcStatsBadUdpCksumDropped,
       "jnxJdhcpRelayIfcStatsOption82Dropped": jnxJdhcpRelayIfcStatsOption82Dropped}
)
