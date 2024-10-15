# SNMP MIB module (IPV6-ICMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV6-ICMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:25 2024
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

(ipv6IfEntry,) = mibBuilder.importSymbols(
    "IPV6-MIB",
    "ipv6IfEntry")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ipv6IcmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipv6IcmpMIBObjects_ObjectIdentity = ObjectIdentity
ipv6IcmpMIBObjects = _Ipv6IcmpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 56, 1)
)
_Ipv6IfIcmpTable_Object = MibTable
ipv6IfIcmpTable = _Ipv6IfIcmpTable_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6IfIcmpTable.setStatus("current")
_Ipv6IfIcmpEntry_Object = MibTableRow
ipv6IfIcmpEntry = _Ipv6IfIcmpEntry_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6IfIcmpEntry.setStatus("current")
_Ipv6IfIcmpInMsgs_Type = Counter32
_Ipv6IfIcmpInMsgs_Object = MibTableColumn
ipv6IfIcmpInMsgs = _Ipv6IfIcmpInMsgs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 1),
    _Ipv6IfIcmpInMsgs_Type()
)
ipv6IfIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInMsgs.setStatus("current")
_Ipv6IfIcmpInErrors_Type = Counter32
_Ipv6IfIcmpInErrors_Object = MibTableColumn
ipv6IfIcmpInErrors = _Ipv6IfIcmpInErrors_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 2),
    _Ipv6IfIcmpInErrors_Type()
)
ipv6IfIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInErrors.setStatus("current")
_Ipv6IfIcmpInDestUnreachs_Type = Counter32
_Ipv6IfIcmpInDestUnreachs_Object = MibTableColumn
ipv6IfIcmpInDestUnreachs = _Ipv6IfIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 3),
    _Ipv6IfIcmpInDestUnreachs_Type()
)
ipv6IfIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInDestUnreachs.setStatus("current")
_Ipv6IfIcmpInAdminProhibs_Type = Counter32
_Ipv6IfIcmpInAdminProhibs_Object = MibTableColumn
ipv6IfIcmpInAdminProhibs = _Ipv6IfIcmpInAdminProhibs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 4),
    _Ipv6IfIcmpInAdminProhibs_Type()
)
ipv6IfIcmpInAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInAdminProhibs.setStatus("current")
_Ipv6IfIcmpInTimeExcds_Type = Counter32
_Ipv6IfIcmpInTimeExcds_Object = MibTableColumn
ipv6IfIcmpInTimeExcds = _Ipv6IfIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 5),
    _Ipv6IfIcmpInTimeExcds_Type()
)
ipv6IfIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInTimeExcds.setStatus("current")
_Ipv6IfIcmpInParmProblems_Type = Counter32
_Ipv6IfIcmpInParmProblems_Object = MibTableColumn
ipv6IfIcmpInParmProblems = _Ipv6IfIcmpInParmProblems_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 6),
    _Ipv6IfIcmpInParmProblems_Type()
)
ipv6IfIcmpInParmProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInParmProblems.setStatus("current")
_Ipv6IfIcmpInPktTooBigs_Type = Counter32
_Ipv6IfIcmpInPktTooBigs_Object = MibTableColumn
ipv6IfIcmpInPktTooBigs = _Ipv6IfIcmpInPktTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 7),
    _Ipv6IfIcmpInPktTooBigs_Type()
)
ipv6IfIcmpInPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInPktTooBigs.setStatus("current")
_Ipv6IfIcmpInEchos_Type = Counter32
_Ipv6IfIcmpInEchos_Object = MibTableColumn
ipv6IfIcmpInEchos = _Ipv6IfIcmpInEchos_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 8),
    _Ipv6IfIcmpInEchos_Type()
)
ipv6IfIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInEchos.setStatus("current")
_Ipv6IfIcmpInEchoReplies_Type = Counter32
_Ipv6IfIcmpInEchoReplies_Object = MibTableColumn
ipv6IfIcmpInEchoReplies = _Ipv6IfIcmpInEchoReplies_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 9),
    _Ipv6IfIcmpInEchoReplies_Type()
)
ipv6IfIcmpInEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInEchoReplies.setStatus("current")
_Ipv6IfIcmpInRouterSolicits_Type = Counter32
_Ipv6IfIcmpInRouterSolicits_Object = MibTableColumn
ipv6IfIcmpInRouterSolicits = _Ipv6IfIcmpInRouterSolicits_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 10),
    _Ipv6IfIcmpInRouterSolicits_Type()
)
ipv6IfIcmpInRouterSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInRouterSolicits.setStatus("current")
_Ipv6IfIcmpInRouterAdvertisements_Type = Counter32
_Ipv6IfIcmpInRouterAdvertisements_Object = MibTableColumn
ipv6IfIcmpInRouterAdvertisements = _Ipv6IfIcmpInRouterAdvertisements_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 11),
    _Ipv6IfIcmpInRouterAdvertisements_Type()
)
ipv6IfIcmpInRouterAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInRouterAdvertisements.setStatus("current")
_Ipv6IfIcmpInNeighborSolicits_Type = Counter32
_Ipv6IfIcmpInNeighborSolicits_Object = MibTableColumn
ipv6IfIcmpInNeighborSolicits = _Ipv6IfIcmpInNeighborSolicits_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 12),
    _Ipv6IfIcmpInNeighborSolicits_Type()
)
ipv6IfIcmpInNeighborSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInNeighborSolicits.setStatus("current")
_Ipv6IfIcmpInNeighborAdvertisements_Type = Counter32
_Ipv6IfIcmpInNeighborAdvertisements_Object = MibTableColumn
ipv6IfIcmpInNeighborAdvertisements = _Ipv6IfIcmpInNeighborAdvertisements_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 13),
    _Ipv6IfIcmpInNeighborAdvertisements_Type()
)
ipv6IfIcmpInNeighborAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInNeighborAdvertisements.setStatus("current")
_Ipv6IfIcmpInRedirects_Type = Counter32
_Ipv6IfIcmpInRedirects_Object = MibTableColumn
ipv6IfIcmpInRedirects = _Ipv6IfIcmpInRedirects_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 14),
    _Ipv6IfIcmpInRedirects_Type()
)
ipv6IfIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInRedirects.setStatus("current")
_Ipv6IfIcmpInGroupMembQueries_Type = Counter32
_Ipv6IfIcmpInGroupMembQueries_Object = MibTableColumn
ipv6IfIcmpInGroupMembQueries = _Ipv6IfIcmpInGroupMembQueries_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 15),
    _Ipv6IfIcmpInGroupMembQueries_Type()
)
ipv6IfIcmpInGroupMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInGroupMembQueries.setStatus("current")
_Ipv6IfIcmpInGroupMembResponses_Type = Counter32
_Ipv6IfIcmpInGroupMembResponses_Object = MibTableColumn
ipv6IfIcmpInGroupMembResponses = _Ipv6IfIcmpInGroupMembResponses_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 16),
    _Ipv6IfIcmpInGroupMembResponses_Type()
)
ipv6IfIcmpInGroupMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInGroupMembResponses.setStatus("current")
_Ipv6IfIcmpInGroupMembReductions_Type = Counter32
_Ipv6IfIcmpInGroupMembReductions_Object = MibTableColumn
ipv6IfIcmpInGroupMembReductions = _Ipv6IfIcmpInGroupMembReductions_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 17),
    _Ipv6IfIcmpInGroupMembReductions_Type()
)
ipv6IfIcmpInGroupMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpInGroupMembReductions.setStatus("current")
_Ipv6IfIcmpOutMsgs_Type = Counter32
_Ipv6IfIcmpOutMsgs_Object = MibTableColumn
ipv6IfIcmpOutMsgs = _Ipv6IfIcmpOutMsgs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 18),
    _Ipv6IfIcmpOutMsgs_Type()
)
ipv6IfIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutMsgs.setStatus("current")
_Ipv6IfIcmpOutErrors_Type = Counter32
_Ipv6IfIcmpOutErrors_Object = MibTableColumn
ipv6IfIcmpOutErrors = _Ipv6IfIcmpOutErrors_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 19),
    _Ipv6IfIcmpOutErrors_Type()
)
ipv6IfIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutErrors.setStatus("current")
_Ipv6IfIcmpOutDestUnreachs_Type = Counter32
_Ipv6IfIcmpOutDestUnreachs_Object = MibTableColumn
ipv6IfIcmpOutDestUnreachs = _Ipv6IfIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 20),
    _Ipv6IfIcmpOutDestUnreachs_Type()
)
ipv6IfIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutDestUnreachs.setStatus("current")
_Ipv6IfIcmpOutAdminProhibs_Type = Counter32
_Ipv6IfIcmpOutAdminProhibs_Object = MibTableColumn
ipv6IfIcmpOutAdminProhibs = _Ipv6IfIcmpOutAdminProhibs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 21),
    _Ipv6IfIcmpOutAdminProhibs_Type()
)
ipv6IfIcmpOutAdminProhibs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutAdminProhibs.setStatus("current")
_Ipv6IfIcmpOutTimeExcds_Type = Counter32
_Ipv6IfIcmpOutTimeExcds_Object = MibTableColumn
ipv6IfIcmpOutTimeExcds = _Ipv6IfIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 22),
    _Ipv6IfIcmpOutTimeExcds_Type()
)
ipv6IfIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutTimeExcds.setStatus("current")
_Ipv6IfIcmpOutParmProblems_Type = Counter32
_Ipv6IfIcmpOutParmProblems_Object = MibTableColumn
ipv6IfIcmpOutParmProblems = _Ipv6IfIcmpOutParmProblems_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 23),
    _Ipv6IfIcmpOutParmProblems_Type()
)
ipv6IfIcmpOutParmProblems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutParmProblems.setStatus("current")
_Ipv6IfIcmpOutPktTooBigs_Type = Counter32
_Ipv6IfIcmpOutPktTooBigs_Object = MibTableColumn
ipv6IfIcmpOutPktTooBigs = _Ipv6IfIcmpOutPktTooBigs_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 24),
    _Ipv6IfIcmpOutPktTooBigs_Type()
)
ipv6IfIcmpOutPktTooBigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutPktTooBigs.setStatus("current")
_Ipv6IfIcmpOutEchos_Type = Counter32
_Ipv6IfIcmpOutEchos_Object = MibTableColumn
ipv6IfIcmpOutEchos = _Ipv6IfIcmpOutEchos_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 25),
    _Ipv6IfIcmpOutEchos_Type()
)
ipv6IfIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutEchos.setStatus("current")
_Ipv6IfIcmpOutEchoReplies_Type = Counter32
_Ipv6IfIcmpOutEchoReplies_Object = MibTableColumn
ipv6IfIcmpOutEchoReplies = _Ipv6IfIcmpOutEchoReplies_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 26),
    _Ipv6IfIcmpOutEchoReplies_Type()
)
ipv6IfIcmpOutEchoReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutEchoReplies.setStatus("current")
_Ipv6IfIcmpOutRouterSolicits_Type = Counter32
_Ipv6IfIcmpOutRouterSolicits_Object = MibTableColumn
ipv6IfIcmpOutRouterSolicits = _Ipv6IfIcmpOutRouterSolicits_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 27),
    _Ipv6IfIcmpOutRouterSolicits_Type()
)
ipv6IfIcmpOutRouterSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutRouterSolicits.setStatus("current")
_Ipv6IfIcmpOutRouterAdvertisements_Type = Counter32
_Ipv6IfIcmpOutRouterAdvertisements_Object = MibTableColumn
ipv6IfIcmpOutRouterAdvertisements = _Ipv6IfIcmpOutRouterAdvertisements_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 28),
    _Ipv6IfIcmpOutRouterAdvertisements_Type()
)
ipv6IfIcmpOutRouterAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutRouterAdvertisements.setStatus("current")
_Ipv6IfIcmpOutNeighborSolicits_Type = Counter32
_Ipv6IfIcmpOutNeighborSolicits_Object = MibTableColumn
ipv6IfIcmpOutNeighborSolicits = _Ipv6IfIcmpOutNeighborSolicits_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 29),
    _Ipv6IfIcmpOutNeighborSolicits_Type()
)
ipv6IfIcmpOutNeighborSolicits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutNeighborSolicits.setStatus("current")
_Ipv6IfIcmpOutNeighborAdvertisements_Type = Counter32
_Ipv6IfIcmpOutNeighborAdvertisements_Object = MibTableColumn
ipv6IfIcmpOutNeighborAdvertisements = _Ipv6IfIcmpOutNeighborAdvertisements_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 30),
    _Ipv6IfIcmpOutNeighborAdvertisements_Type()
)
ipv6IfIcmpOutNeighborAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutNeighborAdvertisements.setStatus("current")
_Ipv6IfIcmpOutRedirects_Type = Counter32
_Ipv6IfIcmpOutRedirects_Object = MibTableColumn
ipv6IfIcmpOutRedirects = _Ipv6IfIcmpOutRedirects_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 31),
    _Ipv6IfIcmpOutRedirects_Type()
)
ipv6IfIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutRedirects.setStatus("current")
_Ipv6IfIcmpOutGroupMembQueries_Type = Counter32
_Ipv6IfIcmpOutGroupMembQueries_Object = MibTableColumn
ipv6IfIcmpOutGroupMembQueries = _Ipv6IfIcmpOutGroupMembQueries_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 32),
    _Ipv6IfIcmpOutGroupMembQueries_Type()
)
ipv6IfIcmpOutGroupMembQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutGroupMembQueries.setStatus("current")
_Ipv6IfIcmpOutGroupMembResponses_Type = Counter32
_Ipv6IfIcmpOutGroupMembResponses_Object = MibTableColumn
ipv6IfIcmpOutGroupMembResponses = _Ipv6IfIcmpOutGroupMembResponses_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 33),
    _Ipv6IfIcmpOutGroupMembResponses_Type()
)
ipv6IfIcmpOutGroupMembResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutGroupMembResponses.setStatus("current")
_Ipv6IfIcmpOutGroupMembReductions_Type = Counter32
_Ipv6IfIcmpOutGroupMembReductions_Object = MibTableColumn
ipv6IfIcmpOutGroupMembReductions = _Ipv6IfIcmpOutGroupMembReductions_Object(
    (1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 34),
    _Ipv6IfIcmpOutGroupMembReductions_Type()
)
ipv6IfIcmpOutGroupMembReductions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfIcmpOutGroupMembReductions.setStatus("current")
_Ipv6IcmpConformance_ObjectIdentity = ObjectIdentity
ipv6IcmpConformance = _Ipv6IcmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 56, 2)
)
_Ipv6IcmpCompliances_ObjectIdentity = ObjectIdentity
ipv6IcmpCompliances = _Ipv6IcmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 56, 2, 1)
)
_Ipv6IcmpGroups_ObjectIdentity = ObjectIdentity
ipv6IcmpGroups = _Ipv6IcmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 56, 2, 2)
)
ipv6IfEntry.registerAugmentions(
    ("IPV6-ICMP-MIB",
     "ipv6IfIcmpEntry")
)
ipv6IfIcmpEntry.setIndexNames(*ipv6IfEntry.getIndexNames())

# Managed Objects groups

ipv6IcmpGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 56, 2, 2, 1)
)
ipv6IcmpGroup.setObjects(
      *(("IPV6-ICMP-MIB", "ipv6IfIcmpInMsgs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInErrors"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInDestUnreachs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInAdminProhibs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInTimeExcds"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInParmProblems"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInPktTooBigs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchos"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchoReplies"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterSolicits"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterAdvertisements"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborSolicits"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborAdvertisements"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInRedirects"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembQueries"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembResponses"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembReductions"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutMsgs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutErrors"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutDestUnreachs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutAdminProhibs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutTimeExcds"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutParmProblems"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutPktTooBigs"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchos"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchoReplies"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterSolicits"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterAdvertisements"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborSolicits"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborAdvertisements"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRedirects"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembQueries"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembResponses"),
        ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembReductions"))
)
if mibBuilder.loadTexts:
    ipv6IcmpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipv6IcmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 56, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6IcmpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV6-ICMP-MIB",
    **{"ipv6IcmpMIB": ipv6IcmpMIB,
       "ipv6IcmpMIBObjects": ipv6IcmpMIBObjects,
       "ipv6IfIcmpTable": ipv6IfIcmpTable,
       "ipv6IfIcmpEntry": ipv6IfIcmpEntry,
       "ipv6IfIcmpInMsgs": ipv6IfIcmpInMsgs,
       "ipv6IfIcmpInErrors": ipv6IfIcmpInErrors,
       "ipv6IfIcmpInDestUnreachs": ipv6IfIcmpInDestUnreachs,
       "ipv6IfIcmpInAdminProhibs": ipv6IfIcmpInAdminProhibs,
       "ipv6IfIcmpInTimeExcds": ipv6IfIcmpInTimeExcds,
       "ipv6IfIcmpInParmProblems": ipv6IfIcmpInParmProblems,
       "ipv6IfIcmpInPktTooBigs": ipv6IfIcmpInPktTooBigs,
       "ipv6IfIcmpInEchos": ipv6IfIcmpInEchos,
       "ipv6IfIcmpInEchoReplies": ipv6IfIcmpInEchoReplies,
       "ipv6IfIcmpInRouterSolicits": ipv6IfIcmpInRouterSolicits,
       "ipv6IfIcmpInRouterAdvertisements": ipv6IfIcmpInRouterAdvertisements,
       "ipv6IfIcmpInNeighborSolicits": ipv6IfIcmpInNeighborSolicits,
       "ipv6IfIcmpInNeighborAdvertisements": ipv6IfIcmpInNeighborAdvertisements,
       "ipv6IfIcmpInRedirects": ipv6IfIcmpInRedirects,
       "ipv6IfIcmpInGroupMembQueries": ipv6IfIcmpInGroupMembQueries,
       "ipv6IfIcmpInGroupMembResponses": ipv6IfIcmpInGroupMembResponses,
       "ipv6IfIcmpInGroupMembReductions": ipv6IfIcmpInGroupMembReductions,
       "ipv6IfIcmpOutMsgs": ipv6IfIcmpOutMsgs,
       "ipv6IfIcmpOutErrors": ipv6IfIcmpOutErrors,
       "ipv6IfIcmpOutDestUnreachs": ipv6IfIcmpOutDestUnreachs,
       "ipv6IfIcmpOutAdminProhibs": ipv6IfIcmpOutAdminProhibs,
       "ipv6IfIcmpOutTimeExcds": ipv6IfIcmpOutTimeExcds,
       "ipv6IfIcmpOutParmProblems": ipv6IfIcmpOutParmProblems,
       "ipv6IfIcmpOutPktTooBigs": ipv6IfIcmpOutPktTooBigs,
       "ipv6IfIcmpOutEchos": ipv6IfIcmpOutEchos,
       "ipv6IfIcmpOutEchoReplies": ipv6IfIcmpOutEchoReplies,
       "ipv6IfIcmpOutRouterSolicits": ipv6IfIcmpOutRouterSolicits,
       "ipv6IfIcmpOutRouterAdvertisements": ipv6IfIcmpOutRouterAdvertisements,
       "ipv6IfIcmpOutNeighborSolicits": ipv6IfIcmpOutNeighborSolicits,
       "ipv6IfIcmpOutNeighborAdvertisements": ipv6IfIcmpOutNeighborAdvertisements,
       "ipv6IfIcmpOutRedirects": ipv6IfIcmpOutRedirects,
       "ipv6IfIcmpOutGroupMembQueries": ipv6IfIcmpOutGroupMembQueries,
       "ipv6IfIcmpOutGroupMembResponses": ipv6IfIcmpOutGroupMembResponses,
       "ipv6IfIcmpOutGroupMembReductions": ipv6IfIcmpOutGroupMembReductions,
       "ipv6IcmpConformance": ipv6IcmpConformance,
       "ipv6IcmpCompliances": ipv6IcmpCompliances,
       "ipv6IcmpCompliance": ipv6IcmpCompliance,
       "ipv6IcmpGroups": ipv6IcmpGroups,
       "ipv6IcmpGroup": ipv6IcmpGroup}
)
