# SNMP MIB module (CISCO-GGSN-SERVICE-AWARE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GGSN-SERVICE-AWARE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:52 2024
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

(cGgsnNotifPdpImsi,
 cGgsnNotifPdpMsisdn) = mibBuilder.importSymbols(
    "CISCO-GGSN-MIB",
    "cGgsnNotifPdpImsi",
    "cGgsnNotifPdpMsisdn")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cGgsnSAMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497)
)
cGgsnSAMIB.setRevisions(
        ("2010-08-06 00:00",
         "2009-12-16 00:00",
         "2009-09-17 00:00",
         "2008-12-10 00:00",
         "2006-05-04 17:00",
         "2005-10-11 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CGgsnCsgPathState(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CGgsnSAMIBObjects_ObjectIdentity = ObjectIdentity
cGgsnSAMIBObjects = _CGgsnSAMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1)
)
_CGgsnSAStatistics_ObjectIdentity = ObjectIdentity
cGgsnSAStatistics = _CGgsnSAStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1)
)
_CGgsnSACsgStatistics_ObjectIdentity = ObjectIdentity
cGgsnSACsgStatistics = _CGgsnSACsgStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1)
)
_CGgsnSACsgOutboundMsgs_Type = Counter32
_CGgsnSACsgOutboundMsgs_Object = MibScalar
cGgsnSACsgOutboundMsgs = _CGgsnSACsgOutboundMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 1),
    _CGgsnSACsgOutboundMsgs_Type()
)
cGgsnSACsgOutboundMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgOutboundMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnSACsgOutboundMsgs.setUnits("packets")
_CGgsnSACsgOutboundOctets_Type = Counter32
_CGgsnSACsgOutboundOctets_Object = MibScalar
cGgsnSACsgOutboundOctets = _CGgsnSACsgOutboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 2),
    _CGgsnSACsgOutboundOctets_Type()
)
cGgsnSACsgOutboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgOutboundOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnSACsgOutboundOctets.setUnits("octets")
_CGgsnSACsgInboundMsgs_Type = Counter32
_CGgsnSACsgInboundMsgs_Object = MibScalar
cGgsnSACsgInboundMsgs = _CGgsnSACsgInboundMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 3),
    _CGgsnSACsgInboundMsgs_Type()
)
cGgsnSACsgInboundMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgInboundMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnSACsgInboundMsgs.setUnits("packets")
_CGgsnSACsgInboundOctets_Type = Counter32
_CGgsnSACsgInboundOctets_Object = MibScalar
cGgsnSACsgInboundOctets = _CGgsnSACsgInboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 4),
    _CGgsnSACsgInboundOctets_Type()
)
cGgsnSACsgInboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgInboundOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGgsnSACsgInboundOctets.setUnits("octets")
_CGgsnSACsgServiceAuthReqs_Type = Counter32
_CGgsnSACsgServiceAuthReqs_Object = MibScalar
cGgsnSACsgServiceAuthReqs = _CGgsnSACsgServiceAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 5),
    _CGgsnSACsgServiceAuthReqs_Type()
)
cGgsnSACsgServiceAuthReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgServiceAuthReqs.setStatus("deprecated")
_CGgsnSACsgServiceAuthResps_Type = Counter32
_CGgsnSACsgServiceAuthResps_Object = MibScalar
cGgsnSACsgServiceAuthResps = _CGgsnSACsgServiceAuthResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 6),
    _CGgsnSACsgServiceAuthResps_Type()
)
cGgsnSACsgServiceAuthResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgServiceAuthResps.setStatus("deprecated")
_CGgsnSACsgServiceReAuthReqs_Type = Counter32
_CGgsnSACsgServiceReAuthReqs_Object = MibScalar
cGgsnSACsgServiceReAuthReqs = _CGgsnSACsgServiceReAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 7),
    _CGgsnSACsgServiceReAuthReqs_Type()
)
cGgsnSACsgServiceReAuthReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgServiceReAuthReqs.setStatus("deprecated")
_CGgsnSACsgQuotaReturns_Type = Counter32
_CGgsnSACsgQuotaReturns_Object = MibScalar
cGgsnSACsgQuotaReturns = _CGgsnSACsgQuotaReturns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 8),
    _CGgsnSACsgQuotaReturns_Type()
)
cGgsnSACsgQuotaReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgQuotaReturns.setStatus("deprecated")
_CGgsnSACsgQuotaReturnReqs_Type = Counter32
_CGgsnSACsgQuotaReturnReqs_Object = MibScalar
cGgsnSACsgQuotaReturnReqs = _CGgsnSACsgQuotaReturnReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 9),
    _CGgsnSACsgQuotaReturnReqs_Type()
)
cGgsnSACsgQuotaReturnReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgQuotaReturnReqs.setStatus("deprecated")
_CGgsnSACsgQuotaPushResps_Type = Counter32
_CGgsnSACsgQuotaPushResps_Object = MibScalar
cGgsnSACsgQuotaPushResps = _CGgsnSACsgQuotaPushResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 10),
    _CGgsnSACsgQuotaPushResps_Type()
)
cGgsnSACsgQuotaPushResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgQuotaPushResps.setStatus("deprecated")
_CGgsnSACsgServiceStopMsgs_Type = Counter32
_CGgsnSACsgServiceStopMsgs_Object = MibScalar
cGgsnSACsgServiceStopMsgs = _CGgsnSACsgServiceStopMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 11),
    _CGgsnSACsgServiceStopMsgs_Type()
)
cGgsnSACsgServiceStopMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgServiceStopMsgs.setStatus("deprecated")
_CGgsnSACsgServiceStopReqs_Type = Counter32
_CGgsnSACsgServiceStopReqs_Object = MibScalar
cGgsnSACsgServiceStopReqs = _CGgsnSACsgServiceStopReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 12),
    _CGgsnSACsgServiceStopReqs_Type()
)
cGgsnSACsgServiceStopReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgServiceStopReqs.setStatus("deprecated")
_CGgsnSACsgQuotaPushMsgs_Type = Counter32
_CGgsnSACsgQuotaPushMsgs_Object = MibScalar
cGgsnSACsgQuotaPushMsgs = _CGgsnSACsgQuotaPushMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 13),
    _CGgsnSACsgQuotaPushMsgs_Type()
)
cGgsnSACsgQuotaPushMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgQuotaPushMsgs.setStatus("deprecated")
_CGgsnSACsgQuotaPushRsps_Type = Counter32
_CGgsnSACsgQuotaPushRsps_Object = MibScalar
cGgsnSACsgQuotaPushRsps = _CGgsnSACsgQuotaPushRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 14),
    _CGgsnSACsgQuotaPushRsps_Type()
)
cGgsnSACsgQuotaPushRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgQuotaPushRsps.setStatus("deprecated")
_CGgsnSACsgGtpAcks_Type = Counter32
_CGgsnSACsgGtpAcks_Object = MibScalar
cGgsnSACsgGtpAcks = _CGgsnSACsgGtpAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 15),
    _CGgsnSACsgGtpAcks_Type()
)
cGgsnSACsgGtpAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgGtpAcks.setStatus("deprecated")
_CggsnSACsgStatisticsTable_Object = MibTable
cggsnSACsgStatisticsTable = _CggsnSACsgStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cggsnSACsgStatisticsTable.setStatus("current")
_CggsnSACsgStatisticsEntry_Object = MibTableRow
cggsnSACsgStatisticsEntry = _CggsnSACsgStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    cggsnSACsgStatisticsEntry.setStatus("current")
_CGgsnSACsgStatsOutboundMsgs_Type = Counter32
_CGgsnSACsgStatsOutboundMsgs_Object = MibTableColumn
cGgsnSACsgStatsOutboundMsgs = _CGgsnSACsgStatsOutboundMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 1),
    _CGgsnSACsgStatsOutboundMsgs_Type()
)
cGgsnSACsgStatsOutboundMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsOutboundMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsOutboundMsgs.setUnits("packets")
_CGgsnSACsgStatsOutboundOctets_Type = Counter32
_CGgsnSACsgStatsOutboundOctets_Object = MibTableColumn
cGgsnSACsgStatsOutboundOctets = _CGgsnSACsgStatsOutboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 2),
    _CGgsnSACsgStatsOutboundOctets_Type()
)
cGgsnSACsgStatsOutboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsOutboundOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsOutboundOctets.setUnits("octets")
_CGgsnSACsgStatsInboundMsgs_Type = Counter32
_CGgsnSACsgStatsInboundMsgs_Object = MibTableColumn
cGgsnSACsgStatsInboundMsgs = _CGgsnSACsgStatsInboundMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 3),
    _CGgsnSACsgStatsInboundMsgs_Type()
)
cGgsnSACsgStatsInboundMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsInboundMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsInboundMsgs.setUnits("packets")
_CGgsnSACsgStatsInboundOctets_Type = Counter32
_CGgsnSACsgStatsInboundOctets_Object = MibTableColumn
cGgsnSACsgStatsInboundOctets = _CGgsnSACsgStatsInboundOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 4),
    _CGgsnSACsgStatsInboundOctets_Type()
)
cGgsnSACsgStatsInboundOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsInboundOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsInboundOctets.setUnits("octets")
_CGgsnSACsgStatsServiceAuthReqs_Type = Counter32
_CGgsnSACsgStatsServiceAuthReqs_Object = MibTableColumn
cGgsnSACsgStatsServiceAuthReqs = _CGgsnSACsgStatsServiceAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 5),
    _CGgsnSACsgStatsServiceAuthReqs_Type()
)
cGgsnSACsgStatsServiceAuthReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsServiceAuthReqs.setStatus("current")
_CGgsnSACsgStatsServiceAuthResps_Type = Counter32
_CGgsnSACsgStatsServiceAuthResps_Object = MibTableColumn
cGgsnSACsgStatsServiceAuthResps = _CGgsnSACsgStatsServiceAuthResps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 6),
    _CGgsnSACsgStatsServiceAuthResps_Type()
)
cGgsnSACsgStatsServiceAuthResps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsServiceAuthResps.setStatus("current")
_CGgsnSACsgStatsServiceReAuthReqs_Type = Counter32
_CGgsnSACsgStatsServiceReAuthReqs_Object = MibTableColumn
cGgsnSACsgStatsServiceReAuthReqs = _CGgsnSACsgStatsServiceReAuthReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 7),
    _CGgsnSACsgStatsServiceReAuthReqs_Type()
)
cGgsnSACsgStatsServiceReAuthReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsServiceReAuthReqs.setStatus("current")
_CGgsnSACsgStatsQuotaReturns_Type = Counter32
_CGgsnSACsgStatsQuotaReturns_Object = MibTableColumn
cGgsnSACsgStatsQuotaReturns = _CGgsnSACsgStatsQuotaReturns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 8),
    _CGgsnSACsgStatsQuotaReturns_Type()
)
cGgsnSACsgStatsQuotaReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsQuotaReturns.setStatus("current")
_CGgsnSACsgStatsQuotaReturnReqs_Type = Counter32
_CGgsnSACsgStatsQuotaReturnReqs_Object = MibTableColumn
cGgsnSACsgStatsQuotaReturnReqs = _CGgsnSACsgStatsQuotaReturnReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 9),
    _CGgsnSACsgStatsQuotaReturnReqs_Type()
)
cGgsnSACsgStatsQuotaReturnReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsQuotaReturnReqs.setStatus("current")
_CGgsnSACsgStatsQuotaReturnAccept_Type = Counter32
_CGgsnSACsgStatsQuotaReturnAccept_Object = MibTableColumn
cGgsnSACsgStatsQuotaReturnAccept = _CGgsnSACsgStatsQuotaReturnAccept_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 10),
    _CGgsnSACsgStatsQuotaReturnAccept_Type()
)
cGgsnSACsgStatsQuotaReturnAccept.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsQuotaReturnAccept.setStatus("current")
_CGgsnSACsgStatsServiceStopMsgs_Type = Counter32
_CGgsnSACsgStatsServiceStopMsgs_Object = MibTableColumn
cGgsnSACsgStatsServiceStopMsgs = _CGgsnSACsgStatsServiceStopMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 11),
    _CGgsnSACsgStatsServiceStopMsgs_Type()
)
cGgsnSACsgStatsServiceStopMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsServiceStopMsgs.setStatus("current")
_CGgsnSACsgStatsServiceStopReqs_Type = Counter32
_CGgsnSACsgStatsServiceStopReqs_Object = MibTableColumn
cGgsnSACsgStatsServiceStopReqs = _CGgsnSACsgStatsServiceStopReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 12),
    _CGgsnSACsgStatsServiceStopReqs_Type()
)
cGgsnSACsgStatsServiceStopReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsServiceStopReqs.setStatus("current")
_CGgsnSACsgStatsQuotaPushMsgs_Type = Counter32
_CGgsnSACsgStatsQuotaPushMsgs_Object = MibTableColumn
cGgsnSACsgStatsQuotaPushMsgs = _CGgsnSACsgStatsQuotaPushMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 13),
    _CGgsnSACsgStatsQuotaPushMsgs_Type()
)
cGgsnSACsgStatsQuotaPushMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsQuotaPushMsgs.setStatus("current")
_CGgsnSACsgStatsQuotaPushRsps_Type = Counter32
_CGgsnSACsgStatsQuotaPushRsps_Object = MibTableColumn
cGgsnSACsgStatsQuotaPushRsps = _CGgsnSACsgStatsQuotaPushRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 14),
    _CGgsnSACsgStatsQuotaPushRsps_Type()
)
cGgsnSACsgStatsQuotaPushRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsQuotaPushRsps.setStatus("current")
_CGgsnSACsgStatsGtpAcks_Type = Counter32
_CGgsnSACsgStatsGtpAcks_Object = MibTableColumn
cGgsnSACsgStatsGtpAcks = _CGgsnSACsgStatsGtpAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 1, 16, 1, 15),
    _CGgsnSACsgStatsGtpAcks_Type()
)
cGgsnSACsgStatsGtpAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgStatsGtpAcks.setStatus("current")
_CGgsnSAQuotaServerStatistics_ObjectIdentity = ObjectIdentity
cGgsnSAQuotaServerStatistics = _CGgsnSAQuotaServerStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2)
)
_CGgsnSAQsRcvdRequests_Type = Counter32
_CGgsnSAQsRcvdRequests_Object = MibScalar
cGgsnSAQsRcvdRequests = _CGgsnSAQsRcvdRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 1),
    _CGgsnSAQsRcvdRequests_Type()
)
cGgsnSAQsRcvdRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsRcvdRequests.setStatus("current")
_CGgsnSAQsRcvdResponses_Type = Counter32
_CGgsnSAQsRcvdResponses_Object = MibScalar
cGgsnSAQsRcvdResponses = _CGgsnSAQsRcvdResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 2),
    _CGgsnSAQsRcvdResponses_Type()
)
cGgsnSAQsRcvdResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsRcvdResponses.setStatus("current")
_CGgsnSAQsSentRequests_Type = Counter32
_CGgsnSAQsSentRequests_Object = MibScalar
cGgsnSAQsSentRequests = _CGgsnSAQsSentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 3),
    _CGgsnSAQsSentRequests_Type()
)
cGgsnSAQsSentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsSentRequests.setStatus("current")
_CGgsnSAQsSentResponses_Type = Counter32
_CGgsnSAQsSentResponses_Object = MibScalar
cGgsnSAQsSentResponses = _CGgsnSAQsSentResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 4),
    _CGgsnSAQsSentResponses_Type()
)
cGgsnSAQsSentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsSentResponses.setStatus("current")
_CGgsnSAQsRcvdPathRequests_Type = Counter32
_CGgsnSAQsRcvdPathRequests_Object = MibScalar
cGgsnSAQsRcvdPathRequests = _CGgsnSAQsRcvdPathRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 5),
    _CGgsnSAQsRcvdPathRequests_Type()
)
cGgsnSAQsRcvdPathRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsRcvdPathRequests.setStatus("current")
_CGgsnSAQsRcvdPathResponses_Type = Counter32
_CGgsnSAQsRcvdPathResponses_Object = MibScalar
cGgsnSAQsRcvdPathResponses = _CGgsnSAQsRcvdPathResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 6),
    _CGgsnSAQsRcvdPathResponses_Type()
)
cGgsnSAQsRcvdPathResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsRcvdPathResponses.setStatus("current")
_CGgsnSAQsSentPathRequests_Type = Counter32
_CGgsnSAQsSentPathRequests_Object = MibScalar
cGgsnSAQsSentPathRequests = _CGgsnSAQsSentPathRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 7),
    _CGgsnSAQsSentPathRequests_Type()
)
cGgsnSAQsSentPathRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsSentPathRequests.setStatus("current")
_CGgsnSAQsSentPathResponses_Type = Counter32
_CGgsnSAQsSentPathResponses_Object = MibScalar
cGgsnSAQsSentPathResponses = _CGgsnSAQsSentPathResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 8),
    _CGgsnSAQsSentPathResponses_Type()
)
cGgsnSAQsSentPathResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsSentPathResponses.setStatus("current")
_CGgsnSAQsRcvdNegativeResponses_Type = Counter32
_CGgsnSAQsRcvdNegativeResponses_Object = MibScalar
cGgsnSAQsRcvdNegativeResponses = _CGgsnSAQsRcvdNegativeResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 9),
    _CGgsnSAQsRcvdNegativeResponses_Type()
)
cGgsnSAQsRcvdNegativeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsRcvdNegativeResponses.setStatus("current")
_CGgsnSAQsRequestsUnreplied_Type = Counter32
_CGgsnSAQsRequestsUnreplied_Object = MibScalar
cGgsnSAQsRequestsUnreplied = _CGgsnSAQsRequestsUnreplied_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 10),
    _CGgsnSAQsRequestsUnreplied_Type()
)
cGgsnSAQsRequestsUnreplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsRequestsUnreplied.setStatus("current")
_CGgsnSAQsSeqnumFailures_Type = Counter32
_CGgsnSAQsSeqnumFailures_Object = MibScalar
cGgsnSAQsSeqnumFailures = _CGgsnSAQsSeqnumFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 11),
    _CGgsnSAQsSeqnumFailures_Type()
)
cGgsnSAQsSeqnumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsSeqnumFailures.setStatus("current")
_CGgsnSAQsDroppedMsgs_Type = Counter32
_CGgsnSAQsDroppedMsgs_Object = MibScalar
cGgsnSAQsDroppedMsgs = _CGgsnSAQsDroppedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 12),
    _CGgsnSAQsDroppedMsgs_Type()
)
cGgsnSAQsDroppedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsDroppedMsgs.setStatus("current")
_CGgsnSAQsUnknownMsgs_Type = Counter32
_CGgsnSAQsUnknownMsgs_Object = MibScalar
cGgsnSAQsUnknownMsgs = _CGgsnSAQsUnknownMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 13),
    _CGgsnSAQsUnknownMsgs_Type()
)
cGgsnSAQsUnknownMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsUnknownMsgs.setStatus("current")
_CGgsnSAQsUnknownResponses_Type = Counter32
_CGgsnSAQsUnknownResponses_Object = MibScalar
cGgsnSAQsUnknownResponses = _CGgsnSAQsUnknownResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 14),
    _CGgsnSAQsUnknownResponses_Type()
)
cGgsnSAQsUnknownResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsUnknownResponses.setStatus("current")
_CGgsnSAQsIEErrorMsgs_Type = Counter32
_CGgsnSAQsIEErrorMsgs_Object = MibScalar
cGgsnSAQsIEErrorMsgs = _CGgsnSAQsIEErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 15),
    _CGgsnSAQsIEErrorMsgs_Type()
)
cGgsnSAQsIEErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsIEErrorMsgs.setStatus("current")
_CGgsnSAQsBadSrcAddressMsgs_Type = Counter32
_CGgsnSAQsBadSrcAddressMsgs_Object = MibScalar
cGgsnSAQsBadSrcAddressMsgs = _CGgsnSAQsBadSrcAddressMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 16),
    _CGgsnSAQsBadSrcAddressMsgs_Type()
)
cGgsnSAQsBadSrcAddressMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsBadSrcAddressMsgs.setStatus("current")
_CGgsnSAQsVersionUnSupportedMsgs_Type = Counter32
_CGgsnSAQsVersionUnSupportedMsgs_Object = MibScalar
cGgsnSAQsVersionUnSupportedMsgs = _CGgsnSAQsVersionUnSupportedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 17),
    _CGgsnSAQsVersionUnSupportedMsgs_Type()
)
cGgsnSAQsVersionUnSupportedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsVersionUnSupportedMsgs.setStatus("current")
_CGgsnSAQsMandTlvMissingMsgs_Type = Counter32
_CGgsnSAQsMandTlvMissingMsgs_Object = MibScalar
cGgsnSAQsMandTlvMissingMsgs = _CGgsnSAQsMandTlvMissingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 18),
    _CGgsnSAQsMandTlvMissingMsgs_Type()
)
cGgsnSAQsMandTlvMissingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsMandTlvMissingMsgs.setStatus("current")
_CGgsnSAQsMandTlvIncorrectMsgs_Type = Counter32
_CGgsnSAQsMandTlvIncorrectMsgs_Object = MibScalar
cGgsnSAQsMandTlvIncorrectMsgs = _CGgsnSAQsMandTlvIncorrectMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 19),
    _CGgsnSAQsMandTlvIncorrectMsgs_Type()
)
cGgsnSAQsMandTlvIncorrectMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsMandTlvIncorrectMsgs.setStatus("current")
_CGgsnSAQsInvalidMsgFormats_Type = Counter32
_CGgsnSAQsInvalidMsgFormats_Object = MibScalar
cGgsnSAQsInvalidMsgFormats = _CGgsnSAQsInvalidMsgFormats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 20),
    _CGgsnSAQsInvalidMsgFormats_Type()
)
cGgsnSAQsInvalidMsgFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsInvalidMsgFormats.setStatus("current")
_CGgsnSAQsNoResponseToMsgs_Type = Counter32
_CGgsnSAQsNoResponseToMsgs_Object = MibScalar
cGgsnSAQsNoResponseToMsgs = _CGgsnSAQsNoResponseToMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 2, 21),
    _CGgsnSAQsNoResponseToMsgs_Type()
)
cGgsnSAQsNoResponseToMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAQsNoResponseToMsgs.setStatus("current")
_CGgsnSAServiceAwareStatistics_ObjectIdentity = ObjectIdentity
cGgsnSAServiceAwareStatistics = _CGgsnSAServiceAwareStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3)
)
_CGgsnSANumServiceAwareApns_Type = Counter32
_CGgsnSANumServiceAwareApns_Object = MibScalar
cGgsnSANumServiceAwareApns = _CGgsnSANumServiceAwareApns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 1),
    _CGgsnSANumServiceAwareApns_Type()
)
cGgsnSANumServiceAwareApns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSANumServiceAwareApns.setStatus("current")
_CGgsnSATotalGgsnEvents_Type = Counter32
_CGgsnSATotalGgsnEvents_Object = MibScalar
cGgsnSATotalGgsnEvents = _CGgsnSATotalGgsnEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 2),
    _CGgsnSATotalGgsnEvents_Type()
)
cGgsnSATotalGgsnEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalGgsnEvents.setStatus("current")
_CGgsnSATotalCsgEvents_Type = Counter32
_CGgsnSATotalCsgEvents_Object = MibScalar
cGgsnSATotalCsgEvents = _CGgsnSATotalCsgEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 3),
    _CGgsnSATotalCsgEvents_Type()
)
cGgsnSATotalCsgEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalCsgEvents.setStatus("current")
_CGgsnSATotalDccaEvents_Type = Counter32
_CGgsnSATotalDccaEvents_Object = MibScalar
cGgsnSATotalDccaEvents = _CGgsnSATotalDccaEvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 4),
    _CGgsnSATotalDccaEvents_Type()
)
cGgsnSATotalDccaEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalDccaEvents.setStatus("current")
_CGgsnSATotalCreatedCategories_Type = Counter32
_CGgsnSATotalCreatedCategories_Object = MibScalar
cGgsnSATotalCreatedCategories = _CGgsnSATotalCreatedCategories_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 5),
    _CGgsnSATotalCreatedCategories_Type()
)
cGgsnSATotalCreatedCategories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalCreatedCategories.setStatus("current")
_CGgsnSATotalCreatedSyncObjs_Type = Counter32
_CGgsnSATotalCreatedSyncObjs_Object = MibScalar
cGgsnSATotalCreatedSyncObjs = _CGgsnSATotalCreatedSyncObjs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 6),
    _CGgsnSATotalCreatedSyncObjs_Type()
)
cGgsnSATotalCreatedSyncObjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalCreatedSyncObjs.setStatus("current")
_CGgsnSACategoryFsmRtnErrors_Type = Counter32
_CGgsnSACategoryFsmRtnErrors_Object = MibScalar
cGgsnSACategoryFsmRtnErrors = _CGgsnSACategoryFsmRtnErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 7),
    _CGgsnSACategoryFsmRtnErrors_Type()
)
cGgsnSACategoryFsmRtnErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACategoryFsmRtnErrors.setStatus("current")
_CGgsnSATotalServiceAuthMsgs_Type = Counter32
_CGgsnSATotalServiceAuthMsgs_Object = MibScalar
cGgsnSATotalServiceAuthMsgs = _CGgsnSATotalServiceAuthMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 8),
    _CGgsnSATotalServiceAuthMsgs_Type()
)
cGgsnSATotalServiceAuthMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalServiceAuthMsgs.setStatus("current")
_CGgsnSATotalServiceStopMsgs_Type = Counter32
_CGgsnSATotalServiceStopMsgs_Object = MibScalar
cGgsnSATotalServiceStopMsgs = _CGgsnSATotalServiceStopMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 9),
    _CGgsnSATotalServiceStopMsgs_Type()
)
cGgsnSATotalServiceStopMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalServiceStopMsgs.setStatus("current")
_CGgsnSATotalQuotaGranted_Type = Counter32
_CGgsnSATotalQuotaGranted_Object = MibScalar
cGgsnSATotalQuotaGranted = _CGgsnSATotalQuotaGranted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 10),
    _CGgsnSATotalQuotaGranted_Type()
)
cGgsnSATotalQuotaGranted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalQuotaGranted.setStatus("current")
_CGgsnSATotalBlackListCategories_Type = Counter32
_CGgsnSATotalBlackListCategories_Object = MibScalar
cGgsnSATotalBlackListCategories = _CGgsnSATotalBlackListCategories_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 11),
    _CGgsnSATotalBlackListCategories_Type()
)
cGgsnSATotalBlackListCategories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalBlackListCategories.setStatus("current")
_CGgsnSATotalRAREvents_Type = Counter32
_CGgsnSATotalRAREvents_Object = MibScalar
cGgsnSATotalRAREvents = _CGgsnSATotalRAREvents_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 12),
    _CGgsnSATotalRAREvents_Type()
)
cGgsnSATotalRAREvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalRAREvents.setStatus("current")
_CGgsnSATotalDeletePdps_Type = Counter32
_CGgsnSATotalDeletePdps_Object = MibScalar
cGgsnSATotalDeletePdps = _CGgsnSATotalDeletePdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 13),
    _CGgsnSATotalDeletePdps_Type()
)
cGgsnSATotalDeletePdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalDeletePdps.setStatus("current")
_CGgsnSAFinalConvertToPostpaidPdps_Type = Counter32
_CGgsnSAFinalConvertToPostpaidPdps_Object = MibScalar
cGgsnSAFinalConvertToPostpaidPdps = _CGgsnSAFinalConvertToPostpaidPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 14),
    _CGgsnSAFinalConvertToPostpaidPdps_Type()
)
cGgsnSAFinalConvertToPostpaidPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSAFinalConvertToPostpaidPdps.setStatus("current")
_CGgsnSATotalGgsnFailures_Type = Counter32
_CGgsnSATotalGgsnFailures_Object = MibScalar
cGgsnSATotalGgsnFailures = _CGgsnSATotalGgsnFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 15),
    _CGgsnSATotalGgsnFailures_Type()
)
cGgsnSATotalGgsnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalGgsnFailures.setStatus("current")
_CGgsnSATotalCsgFailures_Type = Counter32
_CGgsnSATotalCsgFailures_Object = MibScalar
cGgsnSATotalCsgFailures = _CGgsnSATotalCsgFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 16),
    _CGgsnSATotalCsgFailures_Type()
)
cGgsnSATotalCsgFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalCsgFailures.setStatus("current")
_CGgsnSATotalDccaFailures_Type = Counter32
_CGgsnSATotalDccaFailures_Object = MibScalar
cGgsnSATotalDccaFailures = _CGgsnSATotalDccaFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 17),
    _CGgsnSATotalDccaFailures_Type()
)
cGgsnSATotalDccaFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalDccaFailures.setStatus("current")
_CGgsnSATotalDeletedCategories_Type = Counter32
_CGgsnSATotalDeletedCategories_Object = MibScalar
cGgsnSATotalDeletedCategories = _CGgsnSATotalDeletedCategories_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 18),
    _CGgsnSATotalDeletedCategories_Type()
)
cGgsnSATotalDeletedCategories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalDeletedCategories.setStatus("current")
_CGgsnSATotalDeletedSyncObjects_Type = Counter32
_CGgsnSATotalDeletedSyncObjects_Object = MibScalar
cGgsnSATotalDeletedSyncObjects = _CGgsnSATotalDeletedSyncObjects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 19),
    _CGgsnSATotalDeletedSyncObjects_Type()
)
cGgsnSATotalDeletedSyncObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalDeletedSyncObjects.setStatus("current")
_CGgsnSATotalQuotaPushAcks_Type = Counter32
_CGgsnSATotalQuotaPushAcks_Object = MibScalar
cGgsnSATotalQuotaPushAcks = _CGgsnSATotalQuotaPushAcks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 20),
    _CGgsnSATotalQuotaPushAcks_Type()
)
cGgsnSATotalQuotaPushAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalQuotaPushAcks.setStatus("current")
_CGgsnSATotalServiceReAuthMsgs_Type = Counter32
_CGgsnSATotalServiceReAuthMsgs_Object = MibScalar
cGgsnSATotalServiceReAuthMsgs = _CGgsnSATotalServiceReAuthMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 21),
    _CGgsnSATotalServiceReAuthMsgs_Type()
)
cGgsnSATotalServiceReAuthMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalServiceReAuthMsgs.setStatus("current")
_CGgsnSATotalQuotaReturns_Type = Counter32
_CGgsnSATotalQuotaReturns_Object = MibScalar
cGgsnSATotalQuotaReturns = _CGgsnSATotalQuotaReturns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 22),
    _CGgsnSATotalQuotaReturns_Type()
)
cGgsnSATotalQuotaReturns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalQuotaReturns.setStatus("current")
_CGgsnSATotalTerminateCategories_Type = Counter32
_CGgsnSATotalTerminateCategories_Object = MibScalar
cGgsnSATotalTerminateCategories = _CGgsnSATotalTerminateCategories_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 23),
    _CGgsnSATotalTerminateCategories_Type()
)
cGgsnSATotalTerminateCategories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalTerminateCategories.setStatus("current")
_CGgsnSATotalUnknownCategories_Type = Counter32
_CGgsnSATotalUnknownCategories_Object = MibScalar
cGgsnSATotalUnknownCategories = _CGgsnSATotalUnknownCategories_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 24),
    _CGgsnSATotalUnknownCategories_Type()
)
cGgsnSATotalUnknownCategories.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalUnknownCategories.setStatus("current")
_CGgsnSATotalRatingChanges_Type = Counter32
_CGgsnSATotalRatingChanges_Object = MibScalar
cGgsnSATotalRatingChanges = _CGgsnSATotalRatingChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 25),
    _CGgsnSATotalRatingChanges_Type()
)
cGgsnSATotalRatingChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalRatingChanges.setStatus("current")
_CGgsnSATotalPostpaidConversions_Type = Counter32
_CGgsnSATotalPostpaidConversions_Object = MibScalar
cGgsnSATotalPostpaidConversions = _CGgsnSATotalPostpaidConversions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 26),
    _CGgsnSATotalPostpaidConversions_Type()
)
cGgsnSATotalPostpaidConversions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalPostpaidConversions.setStatus("current")
_CGgsnSATotalDummyQuotas_Type = Counter32
_CGgsnSATotalDummyQuotas_Object = MibScalar
cGgsnSATotalDummyQuotas = _CGgsnSATotalDummyQuotas_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 27),
    _CGgsnSATotalDummyQuotas_Type()
)
cGgsnSATotalDummyQuotas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalDummyQuotas.setStatus("current")
_CGgsnSATotalPrepaidUsers_Type = Counter32
_CGgsnSATotalPrepaidUsers_Object = MibScalar
cGgsnSATotalPrepaidUsers = _CGgsnSATotalPrepaidUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 28),
    _CGgsnSATotalPrepaidUsers_Type()
)
cGgsnSATotalPrepaidUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalPrepaidUsers.setStatus("current")
_CGgsnSATotalPostpaidUsers_Type = Counter32
_CGgsnSATotalPostpaidUsers_Object = MibScalar
cGgsnSATotalPostpaidUsers = _CGgsnSATotalPostpaidUsers_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 29),
    _CGgsnSATotalPostpaidUsers_Type()
)
cGgsnSATotalPostpaidUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSATotalPostpaidUsers.setStatus("current")
_CGgsnSARejDccaFailures_Type = Counter32
_CGgsnSARejDccaFailures_Object = MibScalar
cGgsnSARejDccaFailures = _CGgsnSARejDccaFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 30),
    _CGgsnSARejDccaFailures_Type()
)
cGgsnSARejDccaFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSARejDccaFailures.setStatus("current")
_CGgsnSARejCsgFailures_Type = Counter32
_CGgsnSARejCsgFailures_Object = MibScalar
cGgsnSARejCsgFailures = _CGgsnSARejCsgFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 1, 3, 31),
    _CGgsnSARejCsgFailures_Type()
)
cGgsnSARejCsgFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSARejCsgFailures.setStatus("current")
_CGgsnSANotifMgmt_ObjectIdentity = ObjectIdentity
cGgsnSANotifMgmt = _CGgsnSANotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 2)
)


class _CGgsnSACsgNotifEnabled_Type(TruthValue):
    """Custom type cGgsnSACsgNotifEnabled based on TruthValue"""


_CGgsnSACsgNotifEnabled_Object = MibScalar
cGgsnSACsgNotifEnabled = _CGgsnSACsgNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 2, 1),
    _CGgsnSACsgNotifEnabled_Type()
)
cGgsnSACsgNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSACsgNotifEnabled.setStatus("current")


class _CGgsnSADccaNotifEnabled_Type(TruthValue):
    """Custom type cGgsnSADccaNotifEnabled based on TruthValue"""


_CGgsnSADccaNotifEnabled_Object = MibScalar
cGgsnSADccaNotifEnabled = _CGgsnSADccaNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 2, 2),
    _CGgsnSADccaNotifEnabled_Type()
)
cGgsnSADccaNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSADccaNotifEnabled.setStatus("current")
_CGgsnSAConfigurations_ObjectIdentity = ObjectIdentity
cGgsnSAConfigurations = _CGgsnSAConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3)
)


class _CGgsnSAServiceAware_Type(TruthValue):
    """Custom type cGgsnSAServiceAware based on TruthValue"""


_CGgsnSAServiceAware_Object = MibScalar
cGgsnSAServiceAware = _CGgsnSAServiceAware_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 1),
    _CGgsnSAServiceAware_Type()
)
cGgsnSAServiceAware.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSAServiceAware.setStatus("current")
_CGgsnSADccaProfileTable_Object = MibTable
cGgsnSADccaProfileTable = _CGgsnSADccaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2)
)
if mibBuilder.loadTexts:
    cGgsnSADccaProfileTable.setStatus("current")
_CGgsnSADccaProfileEntry_Object = MibTableRow
cGgsnSADccaProfileEntry = _CGgsnSADccaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1)
)
cGgsnSADccaProfileEntry.setIndexNames(
    (0, "CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaProfileName"),
)
if mibBuilder.loadTexts:
    cGgsnSADccaProfileEntry.setStatus("current")
_CGgsnSADccaProfileName_Type = SnmpAdminString
_CGgsnSADccaProfileName_Object = MibTableColumn
cGgsnSADccaProfileName = _CGgsnSADccaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 1),
    _CGgsnSADccaProfileName_Type()
)
cGgsnSADccaProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnSADccaProfileName.setStatus("current")
_CGgsnSADccaAuthorization_Type = SnmpAdminString
_CGgsnSADccaAuthorization_Object = MibTableColumn
cGgsnSADccaAuthorization = _CGgsnSADccaAuthorization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 2),
    _CGgsnSADccaAuthorization_Type()
)
cGgsnSADccaAuthorization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaAuthorization.setStatus("current")


class _CGgsnSADccaCcfh_Type(Integer32):
    """Custom type cGgsnSADccaCcfh based on Integer32"""
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
        *(("continue", 3),
          ("retryTerminate", 2),
          ("terminate", 1))
    )


_CGgsnSADccaCcfh_Type.__name__ = "Integer32"
_CGgsnSADccaCcfh_Object = MibTableColumn
cGgsnSADccaCcfh = _CGgsnSADccaCcfh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 3),
    _CGgsnSADccaCcfh_Type()
)
cGgsnSADccaCcfh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaCcfh.setStatus("current")
_CGgsnSADccaDestinationRealm_Type = SnmpAdminString
_CGgsnSADccaDestinationRealm_Object = MibTableColumn
cGgsnSADccaDestinationRealm = _CGgsnSADccaDestinationRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 4),
    _CGgsnSADccaDestinationRealm_Type()
)
cGgsnSADccaDestinationRealm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaDestinationRealm.setStatus("current")


class _CGgsnSADccaSessionFailover_Type(TruthValue):
    """Custom type cGgsnSADccaSessionFailover based on TruthValue"""


_CGgsnSADccaSessionFailover_Object = MibTableColumn
cGgsnSADccaSessionFailover = _CGgsnSADccaSessionFailover_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 5),
    _CGgsnSADccaSessionFailover_Type()
)
cGgsnSADccaSessionFailover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaSessionFailover.setStatus("current")


class _CGgsnSADccaTxTimeout_Type(Unsigned32):
    """Custom type cGgsnSADccaTxTimeout based on Unsigned32"""
    defaultValue = 10


_CGgsnSADccaTxTimeout_Object = MibTableColumn
cGgsnSADccaTxTimeout = _CGgsnSADccaTxTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 6),
    _CGgsnSADccaTxTimeout_Type()
)
cGgsnSADccaTxTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaTxTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSADccaTxTimeout.setUnits("seconds")


class _CGgsnSADccaTriggerSgsnChange_Type(TruthValue):
    """Custom type cGgsnSADccaTriggerSgsnChange based on TruthValue"""


_CGgsnSADccaTriggerSgsnChange_Object = MibTableColumn
cGgsnSADccaTriggerSgsnChange = _CGgsnSADccaTriggerSgsnChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 7),
    _CGgsnSADccaTriggerSgsnChange_Type()
)
cGgsnSADccaTriggerSgsnChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaTriggerSgsnChange.setStatus("current")


class _CGgsnSADccaTriggerQosChange_Type(TruthValue):
    """Custom type cGgsnSADccaTriggerQosChange based on TruthValue"""


_CGgsnSADccaTriggerQosChange_Object = MibTableColumn
cGgsnSADccaTriggerQosChange = _CGgsnSADccaTriggerQosChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 8),
    _CGgsnSADccaTriggerQosChange_Type()
)
cGgsnSADccaTriggerQosChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaTriggerQosChange.setStatus("current")
_CGgsnSADccaRowStatus_Type = RowStatus
_CGgsnSADccaRowStatus_Object = MibTableColumn
cGgsnSADccaRowStatus = _CGgsnSADccaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 9),
    _CGgsnSADccaRowStatus_Type()
)
cGgsnSADccaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaRowStatus.setStatus("current")


class _CGgsnSADccaTriggerPlmnChange_Type(TruthValue):
    """Custom type cGgsnSADccaTriggerPlmnChange based on TruthValue"""


_CGgsnSADccaTriggerPlmnChange_Object = MibTableColumn
cGgsnSADccaTriggerPlmnChange = _CGgsnSADccaTriggerPlmnChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 10),
    _CGgsnSADccaTriggerPlmnChange_Type()
)
cGgsnSADccaTriggerPlmnChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaTriggerPlmnChange.setStatus("current")


class _CGgsnSADccaTriggerRatChange_Type(TruthValue):
    """Custom type cGgsnSADccaTriggerRatChange based on TruthValue"""


_CGgsnSADccaTriggerRatChange_Object = MibTableColumn
cGgsnSADccaTriggerRatChange = _CGgsnSADccaTriggerRatChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 11),
    _CGgsnSADccaTriggerRatChange_Type()
)
cGgsnSADccaTriggerRatChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaTriggerRatChange.setStatus("current")


class _CGgsnSADccaTriggerUserLocChange_Type(TruthValue):
    """Custom type cGgsnSADccaTriggerUserLocChange based on TruthValue"""


_CGgsnSADccaTriggerUserLocChange_Object = MibTableColumn
cGgsnSADccaTriggerUserLocChange = _CGgsnSADccaTriggerUserLocChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 2, 1, 12),
    _CGgsnSADccaTriggerUserLocChange_Type()
)
cGgsnSADccaTriggerUserLocChange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSADccaTriggerUserLocChange.setStatus("current")


class _CGgsnSADccaClci_Type(Integer32):
    """Custom type cGgsnSADccaClci based on Integer32"""
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
        *(("a3Gpp", 1),
          ("clci", 2),
          ("none", 0))
    )


_CGgsnSADccaClci_Type.__name__ = "Integer32"
_CGgsnSADccaClci_Object = MibScalar
cGgsnSADccaClci = _CGgsnSADccaClci_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 3),
    _CGgsnSADccaClci_Type()
)
cGgsnSADccaClci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnSADccaClci.setStatus("current")
_CGgsnSACsgTable_Object = MibTable
cGgsnSACsgTable = _CGgsnSACsgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cGgsnSACsgTable.setStatus("current")
_CGgsnSACsgEntry_Object = MibTableRow
cGgsnSACsgEntry = _CGgsnSACsgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1)
)
cGgsnSACsgEntry.setIndexNames(
    (0, "CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgGroupName"),
)
if mibBuilder.loadTexts:
    cGgsnSACsgEntry.setStatus("current")
_CGgsnSACsgGroupName_Type = SnmpAdminString
_CGgsnSACsgGroupName_Object = MibTableColumn
cGgsnSACsgGroupName = _CGgsnSACsgGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 1),
    _CGgsnSACsgGroupName_Type()
)
cGgsnSACsgGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnSACsgGroupName.setStatus("current")


class _CGgsnSACsgRealAddressType_Type(InetAddressType):
    """Custom type cGgsnSACsgRealAddressType based on InetAddressType"""


_CGgsnSACsgRealAddressType_Object = MibTableColumn
cGgsnSACsgRealAddressType = _CGgsnSACsgRealAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 2),
    _CGgsnSACsgRealAddressType_Type()
)
cGgsnSACsgRealAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgRealAddressType.setStatus("current")
_CGgsnSACsgRealAddress1_Type = InetAddress
_CGgsnSACsgRealAddress1_Object = MibTableColumn
cGgsnSACsgRealAddress1 = _CGgsnSACsgRealAddress1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 3),
    _CGgsnSACsgRealAddress1_Type()
)
cGgsnSACsgRealAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgRealAddress1.setStatus("current")
_CGgsnSACsgRealAddress2_Type = InetAddress
_CGgsnSACsgRealAddress2_Object = MibTableColumn
cGgsnSACsgRealAddress2 = _CGgsnSACsgRealAddress2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 4),
    _CGgsnSACsgRealAddress2_Type()
)
cGgsnSACsgRealAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgRealAddress2.setStatus("current")


class _CGgsnSACsgVirtualAddressType_Type(InetAddressType):
    """Custom type cGgsnSACsgVirtualAddressType based on InetAddressType"""


_CGgsnSACsgVirtualAddressType_Object = MibTableColumn
cGgsnSACsgVirtualAddressType = _CGgsnSACsgVirtualAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 5),
    _CGgsnSACsgVirtualAddressType_Type()
)
cGgsnSACsgVirtualAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgVirtualAddressType.setStatus("current")
_CGgsnSACsgVirtualAddress_Type = InetAddress
_CGgsnSACsgVirtualAddress_Object = MibTableColumn
cGgsnSACsgVirtualAddress = _CGgsnSACsgVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 6),
    _CGgsnSACsgVirtualAddress_Type()
)
cGgsnSACsgVirtualAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgVirtualAddress.setStatus("current")


class _CGgsnSACsgPort_Type(InetPortNumber):
    """Custom type cGgsnSACsgPort based on InetPortNumber"""
    defaultValue = 3386


_CGgsnSACsgPort_Object = MibTableColumn
cGgsnSACsgPort = _CGgsnSACsgPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 7),
    _CGgsnSACsgPort_Type()
)
cGgsnSACsgPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgPort.setStatus("current")
_CGgsnSACsgRowStatus_Type = RowStatus
_CGgsnSACsgRowStatus_Object = MibTableColumn
cGgsnSACsgRowStatus = _CGgsnSACsgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 8),
    _CGgsnSACsgRowStatus_Type()
)
cGgsnSACsgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgRowStatus.setStatus("current")
_CGgsnSACsgAaaAcctGroup_Type = SnmpAdminString
_CGgsnSACsgAaaAcctGroup_Object = MibTableColumn
cGgsnSACsgAaaAcctGroup = _CGgsnSACsgAaaAcctGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 9),
    _CGgsnSACsgAaaAcctGroup_Type()
)
cGgsnSACsgAaaAcctGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSACsgAaaAcctGroup.setStatus("current")
_CGgsnSACsgPathState_Type = CGgsnCsgPathState
_CGgsnSACsgPathState_Object = MibTableColumn
cGgsnSACsgPathState = _CGgsnSACsgPathState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 10),
    _CGgsnSACsgPathState_Type()
)
cGgsnSACsgPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgPathState.setStatus("current")
_CGgsnSACsgNumPdps_Type = Unsigned32
_CGgsnSACsgNumPdps_Object = MibTableColumn
cGgsnSACsgNumPdps = _CGgsnSACsgNumPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 4, 1, 11),
    _CGgsnSACsgNumPdps_Type()
)
cGgsnSACsgNumPdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnSACsgNumPdps.setStatus("current")
_CGgsnSAQuotaServerTable_Object = MibTable
cGgsnSAQuotaServerTable = _CGgsnSAQuotaServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerTable.setStatus("current")
_CGgsnSAQuotaServerEntry_Object = MibTableRow
cGgsnSAQuotaServerEntry = _CGgsnSAQuotaServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1)
)
cGgsnSAQuotaServerEntry.setIndexNames(
    (0, "CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerName"),
)
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerEntry.setStatus("current")
_CGgsnSAQuotaServerName_Type = SnmpAdminString
_CGgsnSAQuotaServerName_Object = MibTableColumn
cGgsnSAQuotaServerName = _CGgsnSAQuotaServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 1),
    _CGgsnSAQuotaServerName_Type()
)
cGgsnSAQuotaServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerName.setStatus("current")
_CGgsnSAQuotaServerInterface_Type = SnmpAdminString
_CGgsnSAQuotaServerInterface_Object = MibTableColumn
cGgsnSAQuotaServerInterface = _CGgsnSAQuotaServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 2),
    _CGgsnSAQuotaServerInterface_Type()
)
cGgsnSAQuotaServerInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerInterface.setStatus("current")
_CGgsnSAQuotaServerCsgGroup_Type = SnmpAdminString
_CGgsnSAQuotaServerCsgGroup_Object = MibTableColumn
cGgsnSAQuotaServerCsgGroup = _CGgsnSAQuotaServerCsgGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 3),
    _CGgsnSAQuotaServerCsgGroup_Type()
)
cGgsnSAQuotaServerCsgGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerCsgGroup.setStatus("current")


class _CGgsnSAQuotaServerEchoInterval_Type(Integer32):
    """Custom type cGgsnSAQuotaServerEchoInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 65535),
    )


_CGgsnSAQuotaServerEchoInterval_Type.__name__ = "Integer32"
_CGgsnSAQuotaServerEchoInterval_Object = MibTableColumn
cGgsnSAQuotaServerEchoInterval = _CGgsnSAQuotaServerEchoInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 4),
    _CGgsnSAQuotaServerEchoInterval_Type()
)
cGgsnSAQuotaServerEchoInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerEchoInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerEchoInterval.setUnits("seconds")


class _CGgsnSAQuotaServerN3Requests_Type(Integer32):
    """Custom type cGgsnSAQuotaServerN3Requests based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGgsnSAQuotaServerN3Requests_Type.__name__ = "Integer32"
_CGgsnSAQuotaServerN3Requests_Object = MibTableColumn
cGgsnSAQuotaServerN3Requests = _CGgsnSAQuotaServerN3Requests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 5),
    _CGgsnSAQuotaServerN3Requests_Type()
)
cGgsnSAQuotaServerN3Requests.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerN3Requests.setStatus("current")


class _CGgsnSAQuotaServerT3Response_Type(Integer32):
    """Custom type cGgsnSAQuotaServerT3Response based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGgsnSAQuotaServerT3Response_Type.__name__ = "Integer32"
_CGgsnSAQuotaServerT3Response_Object = MibTableColumn
cGgsnSAQuotaServerT3Response = _CGgsnSAQuotaServerT3Response_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 6),
    _CGgsnSAQuotaServerT3Response_Type()
)
cGgsnSAQuotaServerT3Response.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerT3Response.setStatus("current")
_CGgsnSAQuotaServerRowStatus_Type = RowStatus
_CGgsnSAQuotaServerRowStatus_Object = MibTableColumn
cGgsnSAQuotaServerRowStatus = _CGgsnSAQuotaServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 7),
    _CGgsnSAQuotaServerRowStatus_Type()
)
cGgsnSAQuotaServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerRowStatus.setStatus("current")


class _CGgsnSAQuotaServerSvcMsgEnabled_Type(TruthValue):
    """Custom type cGgsnSAQuotaServerSvcMsgEnabled based on TruthValue"""


_CGgsnSAQuotaServerSvcMsgEnabled_Object = MibTableColumn
cGgsnSAQuotaServerSvcMsgEnabled = _CGgsnSAQuotaServerSvcMsgEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 3, 5, 1, 8),
    _CGgsnSAQuotaServerSvcMsgEnabled_Type()
)
cGgsnSAQuotaServerSvcMsgEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnSAQuotaServerSvcMsgEnabled.setStatus("current")
_CGgsnSANotifInfo_ObjectIdentity = ObjectIdentity
cGgsnSANotifInfo = _CGgsnSANotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 4)
)
_CGgsnSANotifCsgRealAddressType_Type = InetAddressType
_CGgsnSANotifCsgRealAddressType_Object = MibScalar
cGgsnSANotifCsgRealAddressType = _CGgsnSANotifCsgRealAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 4, 1),
    _CGgsnSANotifCsgRealAddressType_Type()
)
cGgsnSANotifCsgRealAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnSANotifCsgRealAddressType.setStatus("current")
_CGgsnSANotifCsgRealAddress_Type = InetAddress
_CGgsnSANotifCsgRealAddress_Object = MibScalar
cGgsnSANotifCsgRealAddress = _CGgsnSANotifCsgRealAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 4, 2),
    _CGgsnSANotifCsgRealAddress_Type()
)
cGgsnSANotifCsgRealAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnSANotifCsgRealAddress.setStatus("current")
_CGgsnSANotifCsgVirtualAddrType_Type = InetAddressType
_CGgsnSANotifCsgVirtualAddrType_Object = MibScalar
cGgsnSANotifCsgVirtualAddrType = _CGgsnSANotifCsgVirtualAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 4, 3),
    _CGgsnSANotifCsgVirtualAddrType_Type()
)
cGgsnSANotifCsgVirtualAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnSANotifCsgVirtualAddrType.setStatus("current")
_CGgsnSANotifCsgVirtualAddress_Type = InetAddress
_CGgsnSANotifCsgVirtualAddress_Object = MibScalar
cGgsnSANotifCsgVirtualAddress = _CGgsnSANotifCsgVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 4, 4),
    _CGgsnSANotifCsgVirtualAddress_Type()
)
cGgsnSANotifCsgVirtualAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnSANotifCsgVirtualAddress.setStatus("current")


class _CGgsnSANotifCsgPort_Type(InetPortNumber):
    """Custom type cGgsnSANotifCsgPort based on InetPortNumber"""
    defaultValue = 3386


_CGgsnSANotifCsgPort_Object = MibScalar
cGgsnSANotifCsgPort = _CGgsnSANotifCsgPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 4, 5),
    _CGgsnSANotifCsgPort_Type()
)
cGgsnSANotifCsgPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnSANotifCsgPort.setStatus("current")
_CGgsnSANotifCsgName_Type = SnmpAdminString
_CGgsnSANotifCsgName_Object = MibScalar
cGgsnSANotifCsgName = _CGgsnSANotifCsgName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 1, 4, 6),
    _CGgsnSANotifCsgName_Type()
)
cGgsnSANotifCsgName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnSANotifCsgName.setStatus("current")
_CGgsnSAMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cGgsnSAMIBNotificationPrefix = _CGgsnSAMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2)
)
_CGgsnSANotifications_ObjectIdentity = ObjectIdentity
cGgsnSANotifications = _CGgsnSANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0)
)
_CGgsnSAMIBConformance_ObjectIdentity = ObjectIdentity
cGgsnSAMIBConformance = _CGgsnSAMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3)
)
_CGgsnSAMIBCompliances_ObjectIdentity = ObjectIdentity
cGgsnSAMIBCompliances = _CGgsnSAMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 1)
)
_CGgsnSAMIBGroups_ObjectIdentity = ObjectIdentity
cGgsnSAMIBGroups = _CGgsnSAMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2)
)
cGgsnSACsgEntry.registerAugmentions(
    ("CISCO-GGSN-SERVICE-AWARE-MIB",
     "cggsnSACsgStatisticsEntry")
)
cggsnSACsgStatisticsEntry.setIndexNames(*cGgsnSACsgEntry.getIndexNames())

# Managed Objects groups

cGgsnSAConfigurationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 1)
)
cGgsnSAConfigurationsGroup.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaRowStatus"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaAuthorization"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaCcfh"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaDestinationRealm"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaSessionFailover"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaTxTimeout"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaTriggerSgsnChange"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaTriggerQosChange"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaClci"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAServiceAware"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgRowStatus"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgRealAddressType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgRealAddress1"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgRealAddress2"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgVirtualAddressType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgVirtualAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgPort"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerRowStatus"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerInterface"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerCsgGroup"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerEchoInterval"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerN3Requests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerT3Response"))
)
if mibBuilder.loadTexts:
    cGgsnSAConfigurationsGroup.setStatus("current")

cGgsnSAStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 2)
)
cGgsnSAStatisticsGroup.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgOutboundMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgOutboundOctets"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgInboundMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgInboundOctets"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgServiceAuthReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgServiceAuthResps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgServiceReAuthReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgQuotaReturns"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgQuotaReturnReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgQuotaPushResps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgServiceStopMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgServiceStopReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgQuotaPushMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgQuotaPushRsps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgGtpAcks"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdPathRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdPathResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentPathRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentPathResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdNegativeResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRequestsUnreplied"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSeqnumFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsDroppedMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsUnknownMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsUnknownResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsIEErrorMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsBadSrcAddressMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsVersionUnSupportedMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsMandTlvMissingMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsMandTlvIncorrectMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsInvalidMsgFormats"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsNoResponseToMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANumServiceAwareApns"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalGgsnEvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCsgEvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDccaEvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCreatedCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCreatedSyncObjs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACategoryFsmRtnErrors"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalServiceAuthMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalServiceStopMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalQuotaGranted"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalBlackListCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalRAREvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDeletePdps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAFinalConvertToPostpaidPdps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalGgsnFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCsgFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDccaFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDeletedCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDeletedSyncObjects"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalQuotaPushAcks"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalServiceReAuthMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalQuotaReturns"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalTerminateCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalUnknownCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalRatingChanges"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalPostpaidConversions"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDummyQuotas"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalPrepaidUsers"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalPostpaidUsers"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSARejDccaFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSARejCsgFailures"))
)
if mibBuilder.loadTexts:
    cGgsnSAStatisticsGroup.setStatus("deprecated")

cGgsnSANotifInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 4)
)
cGgsnSANotifInfoGroup.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddressType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddrType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgPort"))
)
if mibBuilder.loadTexts:
    cGgsnSANotifInfoGroup.setStatus("current")

cGgsnSANotifMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 5)
)
cGgsnSANotifMgmtGroup.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgNotifEnabled"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaNotifEnabled"))
)
if mibBuilder.loadTexts:
    cGgsnSANotifMgmtGroup.setStatus("current")

cGgsnSAExtConfigurationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 6)
)
cGgsnSAExtConfigurationsGroup.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaTriggerPlmnChange"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaTriggerRatChange"))
)
if mibBuilder.loadTexts:
    cGgsnSAExtConfigurationsGroup.setStatus("current")

cGgsnSAExtConfigurationsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 7)
)
cGgsnSAExtConfigurationsGroupSup1.setObjects(
    ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaTriggerUserLocChange")
)
if mibBuilder.loadTexts:
    cGgsnSAExtConfigurationsGroupSup1.setStatus("current")

cGgsnSAConfigurationsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 8)
)
cGgsnSAConfigurationsGroupSup1.setObjects(
    ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQuotaServerSvcMsgEnabled")
)
if mibBuilder.loadTexts:
    cGgsnSAConfigurationsGroupSup1.setStatus("current")

cGgsnSAConfigurationsGroupR100 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 9)
)
cGgsnSAConfigurationsGroupR100.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgAaaAcctGroup"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgPathState"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgNumPdps"))
)
if mibBuilder.loadTexts:
    cGgsnSAConfigurationsGroupR100.setStatus("current")

cGgsnSAStatisticsGroupR100 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 10)
)
cGgsnSAStatisticsGroupR100.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdPathRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdPathResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentPathRequests"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSentPathResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRcvdNegativeResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsRequestsUnreplied"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsSeqnumFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsDroppedMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsUnknownMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsUnknownResponses"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsIEErrorMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsBadSrcAddressMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsVersionUnSupportedMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsMandTlvMissingMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsMandTlvIncorrectMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsInvalidMsgFormats"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAQsNoResponseToMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANumServiceAwareApns"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalGgsnEvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCsgEvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDccaEvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCreatedCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCreatedSyncObjs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACategoryFsmRtnErrors"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalServiceAuthMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalServiceStopMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalQuotaGranted"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalBlackListCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalRAREvents"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDeletePdps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSAFinalConvertToPostpaidPdps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalGgsnFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalCsgFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDccaFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDeletedCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDeletedSyncObjects"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalQuotaPushAcks"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalServiceReAuthMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalQuotaReturns"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalTerminateCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalUnknownCategories"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalRatingChanges"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalPostpaidConversions"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalDummyQuotas"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalPrepaidUsers"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSATotalPostpaidUsers"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSARejDccaFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSARejCsgFailures"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsOutboundMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsOutboundOctets"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsInboundMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsInboundOctets"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsServiceAuthReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsServiceAuthResps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsServiceReAuthReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsQuotaReturns"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsQuotaReturnReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsQuotaReturnAccept"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsServiceStopMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsServiceStopReqs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsQuotaPushMsgs"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsQuotaPushRsps"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStatsGtpAcks"))
)
if mibBuilder.loadTexts:
    cGgsnSAStatisticsGroupR100.setStatus("current")

cGgsnSANotifInfoGroupR100 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 11)
)
cGgsnSANotifInfoGroupR100.setObjects(
    ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgName")
)
if mibBuilder.loadTexts:
    cGgsnSANotifInfoGroupR100.setStatus("current")


# Notification objects

cGgsnSACsgStateUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 1)
)
cGgsnSACsgStateUpNotif.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddressType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddrType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgPort"))
)
if mibBuilder.loadTexts:
    cGgsnSACsgStateUpNotif.setStatus(
        "deprecated"
    )

cGgsnSACsgStateDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 2)
)
cGgsnSACsgStateDownNotif.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddressType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddrType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgPort"))
)
if mibBuilder.loadTexts:
    cGgsnSACsgStateDownNotif.setStatus(
        "deprecated"
    )

cGgsnSADccaEndUsrServDeniedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 3)
)
cGgsnSADccaEndUsrServDeniedNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpMsisdn"))
)
if mibBuilder.loadTexts:
    cGgsnSADccaEndUsrServDeniedNotif.setStatus(
        "current"
    )

cGgsnSADccaCreditLimReachedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 4)
)
cGgsnSADccaCreditLimReachedNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpMsisdn"))
)
if mibBuilder.loadTexts:
    cGgsnSADccaCreditLimReachedNotif.setStatus(
        "current"
    )

cGgsnSADccaUserUnknownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 5)
)
cGgsnSADccaUserUnknownNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpMsisdn"))
)
if mibBuilder.loadTexts:
    cGgsnSADccaUserUnknownNotif.setStatus(
        "current"
    )

cGgsnSADccaRatingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 6)
)
cGgsnSADccaRatingFailed.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpMsisdn"))
)
if mibBuilder.loadTexts:
    cGgsnSADccaRatingFailed.setStatus(
        "current"
    )

cGgsnSADccaAuthRejectedNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 7)
)
cGgsnSADccaAuthRejectedNotif.setObjects(
      *(("CISCO-GGSN-MIB", "cGgsnNotifPdpImsi"),
        ("CISCO-GGSN-MIB", "cGgsnNotifPdpMsisdn"))
)
if mibBuilder.loadTexts:
    cGgsnSADccaAuthRejectedNotif.setStatus(
        "current"
    )

cGgsnSACsgR100StateUpNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 8)
)
cGgsnSACsgR100StateUpNotif.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgName"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddressType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddrType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgPort"))
)
if mibBuilder.loadTexts:
    cGgsnSACsgR100StateUpNotif.setStatus(
        "current"
    )

cGgsnSACsgR100StateDownNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 2, 0, 9)
)
cGgsnSACsgR100StateDownNotif.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgName"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddressType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgRealAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddrType"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgVirtualAddress"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSANotifCsgPort"))
)
if mibBuilder.loadTexts:
    cGgsnSACsgR100StateDownNotif.setStatus(
        "current"
    )


# Notifications groups

cGgsnSANotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 3)
)
cGgsnSANotifGroup.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStateUpNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgStateDownNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaEndUsrServDeniedNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaCreditLimReachedNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaUserUnknownNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaRatingFailed"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaAuthRejectedNotif"))
)
if mibBuilder.loadTexts:
    cGgsnSANotifGroup.setStatus(
        "deprecated"
    )

cGgsnSANotifGroupR100 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 2, 12)
)
cGgsnSANotifGroupR100.setObjects(
      *(("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaEndUsrServDeniedNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaCreditLimReachedNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaUserUnknownNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaRatingFailed"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSADccaAuthRejectedNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgR100StateUpNotif"),
        ("CISCO-GGSN-SERVICE-AWARE-MIB", "cGgsnSACsgR100StateDownNotif"))
)
if mibBuilder.loadTexts:
    cGgsnSANotifGroupR100.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cGgsnSAMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cGgsnSAMIBCompliance.setStatus(
        "deprecated"
    )

cGgsnSAMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cGgsnSAMIBComplianceRev1.setStatus(
        "deprecated"
    )

cGgsnSAMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cGgsnSAMIBComplianceRev2.setStatus(
        "deprecated"
    )

cGgsnSAMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cGgsnSAMIBComplianceRev3.setStatus(
        "deprecated"
    )

cGgsnSAMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 497, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cGgsnSAMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GGSN-SERVICE-AWARE-MIB",
    **{"CGgsnCsgPathState": CGgsnCsgPathState,
       "cGgsnSAMIB": cGgsnSAMIB,
       "cGgsnSAMIBObjects": cGgsnSAMIBObjects,
       "cGgsnSAStatistics": cGgsnSAStatistics,
       "cGgsnSACsgStatistics": cGgsnSACsgStatistics,
       "cGgsnSACsgOutboundMsgs": cGgsnSACsgOutboundMsgs,
       "cGgsnSACsgOutboundOctets": cGgsnSACsgOutboundOctets,
       "cGgsnSACsgInboundMsgs": cGgsnSACsgInboundMsgs,
       "cGgsnSACsgInboundOctets": cGgsnSACsgInboundOctets,
       "cGgsnSACsgServiceAuthReqs": cGgsnSACsgServiceAuthReqs,
       "cGgsnSACsgServiceAuthResps": cGgsnSACsgServiceAuthResps,
       "cGgsnSACsgServiceReAuthReqs": cGgsnSACsgServiceReAuthReqs,
       "cGgsnSACsgQuotaReturns": cGgsnSACsgQuotaReturns,
       "cGgsnSACsgQuotaReturnReqs": cGgsnSACsgQuotaReturnReqs,
       "cGgsnSACsgQuotaPushResps": cGgsnSACsgQuotaPushResps,
       "cGgsnSACsgServiceStopMsgs": cGgsnSACsgServiceStopMsgs,
       "cGgsnSACsgServiceStopReqs": cGgsnSACsgServiceStopReqs,
       "cGgsnSACsgQuotaPushMsgs": cGgsnSACsgQuotaPushMsgs,
       "cGgsnSACsgQuotaPushRsps": cGgsnSACsgQuotaPushRsps,
       "cGgsnSACsgGtpAcks": cGgsnSACsgGtpAcks,
       "cggsnSACsgStatisticsTable": cggsnSACsgStatisticsTable,
       "cggsnSACsgStatisticsEntry": cggsnSACsgStatisticsEntry,
       "cGgsnSACsgStatsOutboundMsgs": cGgsnSACsgStatsOutboundMsgs,
       "cGgsnSACsgStatsOutboundOctets": cGgsnSACsgStatsOutboundOctets,
       "cGgsnSACsgStatsInboundMsgs": cGgsnSACsgStatsInboundMsgs,
       "cGgsnSACsgStatsInboundOctets": cGgsnSACsgStatsInboundOctets,
       "cGgsnSACsgStatsServiceAuthReqs": cGgsnSACsgStatsServiceAuthReqs,
       "cGgsnSACsgStatsServiceAuthResps": cGgsnSACsgStatsServiceAuthResps,
       "cGgsnSACsgStatsServiceReAuthReqs": cGgsnSACsgStatsServiceReAuthReqs,
       "cGgsnSACsgStatsQuotaReturns": cGgsnSACsgStatsQuotaReturns,
       "cGgsnSACsgStatsQuotaReturnReqs": cGgsnSACsgStatsQuotaReturnReqs,
       "cGgsnSACsgStatsQuotaReturnAccept": cGgsnSACsgStatsQuotaReturnAccept,
       "cGgsnSACsgStatsServiceStopMsgs": cGgsnSACsgStatsServiceStopMsgs,
       "cGgsnSACsgStatsServiceStopReqs": cGgsnSACsgStatsServiceStopReqs,
       "cGgsnSACsgStatsQuotaPushMsgs": cGgsnSACsgStatsQuotaPushMsgs,
       "cGgsnSACsgStatsQuotaPushRsps": cGgsnSACsgStatsQuotaPushRsps,
       "cGgsnSACsgStatsGtpAcks": cGgsnSACsgStatsGtpAcks,
       "cGgsnSAQuotaServerStatistics": cGgsnSAQuotaServerStatistics,
       "cGgsnSAQsRcvdRequests": cGgsnSAQsRcvdRequests,
       "cGgsnSAQsRcvdResponses": cGgsnSAQsRcvdResponses,
       "cGgsnSAQsSentRequests": cGgsnSAQsSentRequests,
       "cGgsnSAQsSentResponses": cGgsnSAQsSentResponses,
       "cGgsnSAQsRcvdPathRequests": cGgsnSAQsRcvdPathRequests,
       "cGgsnSAQsRcvdPathResponses": cGgsnSAQsRcvdPathResponses,
       "cGgsnSAQsSentPathRequests": cGgsnSAQsSentPathRequests,
       "cGgsnSAQsSentPathResponses": cGgsnSAQsSentPathResponses,
       "cGgsnSAQsRcvdNegativeResponses": cGgsnSAQsRcvdNegativeResponses,
       "cGgsnSAQsRequestsUnreplied": cGgsnSAQsRequestsUnreplied,
       "cGgsnSAQsSeqnumFailures": cGgsnSAQsSeqnumFailures,
       "cGgsnSAQsDroppedMsgs": cGgsnSAQsDroppedMsgs,
       "cGgsnSAQsUnknownMsgs": cGgsnSAQsUnknownMsgs,
       "cGgsnSAQsUnknownResponses": cGgsnSAQsUnknownResponses,
       "cGgsnSAQsIEErrorMsgs": cGgsnSAQsIEErrorMsgs,
       "cGgsnSAQsBadSrcAddressMsgs": cGgsnSAQsBadSrcAddressMsgs,
       "cGgsnSAQsVersionUnSupportedMsgs": cGgsnSAQsVersionUnSupportedMsgs,
       "cGgsnSAQsMandTlvMissingMsgs": cGgsnSAQsMandTlvMissingMsgs,
       "cGgsnSAQsMandTlvIncorrectMsgs": cGgsnSAQsMandTlvIncorrectMsgs,
       "cGgsnSAQsInvalidMsgFormats": cGgsnSAQsInvalidMsgFormats,
       "cGgsnSAQsNoResponseToMsgs": cGgsnSAQsNoResponseToMsgs,
       "cGgsnSAServiceAwareStatistics": cGgsnSAServiceAwareStatistics,
       "cGgsnSANumServiceAwareApns": cGgsnSANumServiceAwareApns,
       "cGgsnSATotalGgsnEvents": cGgsnSATotalGgsnEvents,
       "cGgsnSATotalCsgEvents": cGgsnSATotalCsgEvents,
       "cGgsnSATotalDccaEvents": cGgsnSATotalDccaEvents,
       "cGgsnSATotalCreatedCategories": cGgsnSATotalCreatedCategories,
       "cGgsnSATotalCreatedSyncObjs": cGgsnSATotalCreatedSyncObjs,
       "cGgsnSACategoryFsmRtnErrors": cGgsnSACategoryFsmRtnErrors,
       "cGgsnSATotalServiceAuthMsgs": cGgsnSATotalServiceAuthMsgs,
       "cGgsnSATotalServiceStopMsgs": cGgsnSATotalServiceStopMsgs,
       "cGgsnSATotalQuotaGranted": cGgsnSATotalQuotaGranted,
       "cGgsnSATotalBlackListCategories": cGgsnSATotalBlackListCategories,
       "cGgsnSATotalRAREvents": cGgsnSATotalRAREvents,
       "cGgsnSATotalDeletePdps": cGgsnSATotalDeletePdps,
       "cGgsnSAFinalConvertToPostpaidPdps": cGgsnSAFinalConvertToPostpaidPdps,
       "cGgsnSATotalGgsnFailures": cGgsnSATotalGgsnFailures,
       "cGgsnSATotalCsgFailures": cGgsnSATotalCsgFailures,
       "cGgsnSATotalDccaFailures": cGgsnSATotalDccaFailures,
       "cGgsnSATotalDeletedCategories": cGgsnSATotalDeletedCategories,
       "cGgsnSATotalDeletedSyncObjects": cGgsnSATotalDeletedSyncObjects,
       "cGgsnSATotalQuotaPushAcks": cGgsnSATotalQuotaPushAcks,
       "cGgsnSATotalServiceReAuthMsgs": cGgsnSATotalServiceReAuthMsgs,
       "cGgsnSATotalQuotaReturns": cGgsnSATotalQuotaReturns,
       "cGgsnSATotalTerminateCategories": cGgsnSATotalTerminateCategories,
       "cGgsnSATotalUnknownCategories": cGgsnSATotalUnknownCategories,
       "cGgsnSATotalRatingChanges": cGgsnSATotalRatingChanges,
       "cGgsnSATotalPostpaidConversions": cGgsnSATotalPostpaidConversions,
       "cGgsnSATotalDummyQuotas": cGgsnSATotalDummyQuotas,
       "cGgsnSATotalPrepaidUsers": cGgsnSATotalPrepaidUsers,
       "cGgsnSATotalPostpaidUsers": cGgsnSATotalPostpaidUsers,
       "cGgsnSARejDccaFailures": cGgsnSARejDccaFailures,
       "cGgsnSARejCsgFailures": cGgsnSARejCsgFailures,
       "cGgsnSANotifMgmt": cGgsnSANotifMgmt,
       "cGgsnSACsgNotifEnabled": cGgsnSACsgNotifEnabled,
       "cGgsnSADccaNotifEnabled": cGgsnSADccaNotifEnabled,
       "cGgsnSAConfigurations": cGgsnSAConfigurations,
       "cGgsnSAServiceAware": cGgsnSAServiceAware,
       "cGgsnSADccaProfileTable": cGgsnSADccaProfileTable,
       "cGgsnSADccaProfileEntry": cGgsnSADccaProfileEntry,
       "cGgsnSADccaProfileName": cGgsnSADccaProfileName,
       "cGgsnSADccaAuthorization": cGgsnSADccaAuthorization,
       "cGgsnSADccaCcfh": cGgsnSADccaCcfh,
       "cGgsnSADccaDestinationRealm": cGgsnSADccaDestinationRealm,
       "cGgsnSADccaSessionFailover": cGgsnSADccaSessionFailover,
       "cGgsnSADccaTxTimeout": cGgsnSADccaTxTimeout,
       "cGgsnSADccaTriggerSgsnChange": cGgsnSADccaTriggerSgsnChange,
       "cGgsnSADccaTriggerQosChange": cGgsnSADccaTriggerQosChange,
       "cGgsnSADccaRowStatus": cGgsnSADccaRowStatus,
       "cGgsnSADccaTriggerPlmnChange": cGgsnSADccaTriggerPlmnChange,
       "cGgsnSADccaTriggerRatChange": cGgsnSADccaTriggerRatChange,
       "cGgsnSADccaTriggerUserLocChange": cGgsnSADccaTriggerUserLocChange,
       "cGgsnSADccaClci": cGgsnSADccaClci,
       "cGgsnSACsgTable": cGgsnSACsgTable,
       "cGgsnSACsgEntry": cGgsnSACsgEntry,
       "cGgsnSACsgGroupName": cGgsnSACsgGroupName,
       "cGgsnSACsgRealAddressType": cGgsnSACsgRealAddressType,
       "cGgsnSACsgRealAddress1": cGgsnSACsgRealAddress1,
       "cGgsnSACsgRealAddress2": cGgsnSACsgRealAddress2,
       "cGgsnSACsgVirtualAddressType": cGgsnSACsgVirtualAddressType,
       "cGgsnSACsgVirtualAddress": cGgsnSACsgVirtualAddress,
       "cGgsnSACsgPort": cGgsnSACsgPort,
       "cGgsnSACsgRowStatus": cGgsnSACsgRowStatus,
       "cGgsnSACsgAaaAcctGroup": cGgsnSACsgAaaAcctGroup,
       "cGgsnSACsgPathState": cGgsnSACsgPathState,
       "cGgsnSACsgNumPdps": cGgsnSACsgNumPdps,
       "cGgsnSAQuotaServerTable": cGgsnSAQuotaServerTable,
       "cGgsnSAQuotaServerEntry": cGgsnSAQuotaServerEntry,
       "cGgsnSAQuotaServerName": cGgsnSAQuotaServerName,
       "cGgsnSAQuotaServerInterface": cGgsnSAQuotaServerInterface,
       "cGgsnSAQuotaServerCsgGroup": cGgsnSAQuotaServerCsgGroup,
       "cGgsnSAQuotaServerEchoInterval": cGgsnSAQuotaServerEchoInterval,
       "cGgsnSAQuotaServerN3Requests": cGgsnSAQuotaServerN3Requests,
       "cGgsnSAQuotaServerT3Response": cGgsnSAQuotaServerT3Response,
       "cGgsnSAQuotaServerRowStatus": cGgsnSAQuotaServerRowStatus,
       "cGgsnSAQuotaServerSvcMsgEnabled": cGgsnSAQuotaServerSvcMsgEnabled,
       "cGgsnSANotifInfo": cGgsnSANotifInfo,
       "cGgsnSANotifCsgRealAddressType": cGgsnSANotifCsgRealAddressType,
       "cGgsnSANotifCsgRealAddress": cGgsnSANotifCsgRealAddress,
       "cGgsnSANotifCsgVirtualAddrType": cGgsnSANotifCsgVirtualAddrType,
       "cGgsnSANotifCsgVirtualAddress": cGgsnSANotifCsgVirtualAddress,
       "cGgsnSANotifCsgPort": cGgsnSANotifCsgPort,
       "cGgsnSANotifCsgName": cGgsnSANotifCsgName,
       "cGgsnSAMIBNotificationPrefix": cGgsnSAMIBNotificationPrefix,
       "cGgsnSANotifications": cGgsnSANotifications,
       "cGgsnSACsgStateUpNotif": cGgsnSACsgStateUpNotif,
       "cGgsnSACsgStateDownNotif": cGgsnSACsgStateDownNotif,
       "cGgsnSADccaEndUsrServDeniedNotif": cGgsnSADccaEndUsrServDeniedNotif,
       "cGgsnSADccaCreditLimReachedNotif": cGgsnSADccaCreditLimReachedNotif,
       "cGgsnSADccaUserUnknownNotif": cGgsnSADccaUserUnknownNotif,
       "cGgsnSADccaRatingFailed": cGgsnSADccaRatingFailed,
       "cGgsnSADccaAuthRejectedNotif": cGgsnSADccaAuthRejectedNotif,
       "cGgsnSACsgR100StateUpNotif": cGgsnSACsgR100StateUpNotif,
       "cGgsnSACsgR100StateDownNotif": cGgsnSACsgR100StateDownNotif,
       "cGgsnSAMIBConformance": cGgsnSAMIBConformance,
       "cGgsnSAMIBCompliances": cGgsnSAMIBCompliances,
       "cGgsnSAMIBCompliance": cGgsnSAMIBCompliance,
       "cGgsnSAMIBComplianceRev1": cGgsnSAMIBComplianceRev1,
       "cGgsnSAMIBComplianceRev2": cGgsnSAMIBComplianceRev2,
       "cGgsnSAMIBComplianceRev3": cGgsnSAMIBComplianceRev3,
       "cGgsnSAMIBComplianceRev4": cGgsnSAMIBComplianceRev4,
       "cGgsnSAMIBGroups": cGgsnSAMIBGroups,
       "cGgsnSAConfigurationsGroup": cGgsnSAConfigurationsGroup,
       "cGgsnSAStatisticsGroup": cGgsnSAStatisticsGroup,
       "cGgsnSANotifGroup": cGgsnSANotifGroup,
       "cGgsnSANotifInfoGroup": cGgsnSANotifInfoGroup,
       "cGgsnSANotifMgmtGroup": cGgsnSANotifMgmtGroup,
       "cGgsnSAExtConfigurationsGroup": cGgsnSAExtConfigurationsGroup,
       "cGgsnSAExtConfigurationsGroupSup1": cGgsnSAExtConfigurationsGroupSup1,
       "cGgsnSAConfigurationsGroupSup1": cGgsnSAConfigurationsGroupSup1,
       "cGgsnSAConfigurationsGroupR100": cGgsnSAConfigurationsGroupR100,
       "cGgsnSAStatisticsGroupR100": cGgsnSAStatisticsGroupR100,
       "cGgsnSANotifInfoGroupR100": cGgsnSANotifInfoGroupR100,
       "cGgsnSANotifGroupR100": cGgsnSANotifGroupR100}
)
