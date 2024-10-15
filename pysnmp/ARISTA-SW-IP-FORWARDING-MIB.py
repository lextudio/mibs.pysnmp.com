# SNMP MIB module (ARISTA-SW-IP-FORWARDING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-SW-IP-FORWARDING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:28 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(InetVersion,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetVersion")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

aristaSwIpForwardingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1)
)
aristaSwIpForwardingMIB.setRevisions(
        ("2014-08-15 00:00",
         "2011-03-31 13:00",
         "2010-01-31 00:00",
         "2009-03-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AristaSwFwdIp_ObjectIdentity = ObjectIdentity
aristaSwFwdIp = _AristaSwFwdIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1)
)
_AristaSwFwdIpStatsTable_Object = MibTable
aristaSwFwdIpStatsTable = _AristaSwFwdIpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsTable.setStatus("current")
_AristaSwFwdIpStatsEntry_Object = MibTableRow
aristaSwFwdIpStatsEntry = _AristaSwFwdIpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1)
)
aristaSwFwdIpStatsEntry.setIndexNames(
    (0, "ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsIPVersion"),
)
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsEntry.setStatus("current")
_AristaSwFwdIpStatsIPVersion_Type = InetVersion
_AristaSwFwdIpStatsIPVersion_Object = MibTableColumn
aristaSwFwdIpStatsIPVersion = _AristaSwFwdIpStatsIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 1),
    _AristaSwFwdIpStatsIPVersion_Type()
)
aristaSwFwdIpStatsIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsIPVersion.setStatus("current")
_AristaSwFwdIpStatsInReceives_Type = Counter32
_AristaSwFwdIpStatsInReceives_Object = MibTableColumn
aristaSwFwdIpStatsInReceives = _AristaSwFwdIpStatsInReceives_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 3),
    _AristaSwFwdIpStatsInReceives_Type()
)
aristaSwFwdIpStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInReceives.setStatus("current")
_AristaSwFwdIpStatsHCInReceives_Type = Counter64
_AristaSwFwdIpStatsHCInReceives_Object = MibTableColumn
aristaSwFwdIpStatsHCInReceives = _AristaSwFwdIpStatsHCInReceives_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 4),
    _AristaSwFwdIpStatsHCInReceives_Type()
)
aristaSwFwdIpStatsHCInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCInReceives.setStatus("current")
_AristaSwFwdIpStatsInOctets_Type = Counter32
_AristaSwFwdIpStatsInOctets_Object = MibTableColumn
aristaSwFwdIpStatsInOctets = _AristaSwFwdIpStatsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 5),
    _AristaSwFwdIpStatsInOctets_Type()
)
aristaSwFwdIpStatsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInOctets.setStatus("current")
_AristaSwFwdIpStatsHCInOctets_Type = Counter64
_AristaSwFwdIpStatsHCInOctets_Object = MibTableColumn
aristaSwFwdIpStatsHCInOctets = _AristaSwFwdIpStatsHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 6),
    _AristaSwFwdIpStatsHCInOctets_Type()
)
aristaSwFwdIpStatsHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCInOctets.setStatus("current")
_AristaSwFwdIpStatsInHdrErrors_Type = Counter32
_AristaSwFwdIpStatsInHdrErrors_Object = MibTableColumn
aristaSwFwdIpStatsInHdrErrors = _AristaSwFwdIpStatsInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 7),
    _AristaSwFwdIpStatsInHdrErrors_Type()
)
aristaSwFwdIpStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInHdrErrors.setStatus("current")
_AristaSwFwdIpStatsInNoRoutes_Type = Counter32
_AristaSwFwdIpStatsInNoRoutes_Object = MibTableColumn
aristaSwFwdIpStatsInNoRoutes = _AristaSwFwdIpStatsInNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 8),
    _AristaSwFwdIpStatsInNoRoutes_Type()
)
aristaSwFwdIpStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInNoRoutes.setStatus("current")
_AristaSwFwdIpStatsInAddrErrors_Type = Counter32
_AristaSwFwdIpStatsInAddrErrors_Object = MibTableColumn
aristaSwFwdIpStatsInAddrErrors = _AristaSwFwdIpStatsInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 9),
    _AristaSwFwdIpStatsInAddrErrors_Type()
)
aristaSwFwdIpStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInAddrErrors.setStatus("current")
_AristaSwFwdIpStatsInUnknownProtos_Type = Counter32
_AristaSwFwdIpStatsInUnknownProtos_Object = MibTableColumn
aristaSwFwdIpStatsInUnknownProtos = _AristaSwFwdIpStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 10),
    _AristaSwFwdIpStatsInUnknownProtos_Type()
)
aristaSwFwdIpStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInUnknownProtos.setStatus("current")
_AristaSwFwdIpStatsInTruncatedPkts_Type = Counter32
_AristaSwFwdIpStatsInTruncatedPkts_Object = MibTableColumn
aristaSwFwdIpStatsInTruncatedPkts = _AristaSwFwdIpStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 11),
    _AristaSwFwdIpStatsInTruncatedPkts_Type()
)
aristaSwFwdIpStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInTruncatedPkts.setStatus("current")
_AristaSwFwdIpStatsInForwDatagrams_Type = Counter32
_AristaSwFwdIpStatsInForwDatagrams_Object = MibTableColumn
aristaSwFwdIpStatsInForwDatagrams = _AristaSwFwdIpStatsInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 12),
    _AristaSwFwdIpStatsInForwDatagrams_Type()
)
aristaSwFwdIpStatsInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInForwDatagrams.setStatus("current")
_AristaSwFwdIpStatsHCInForwDatagrams_Type = Counter64
_AristaSwFwdIpStatsHCInForwDatagrams_Object = MibTableColumn
aristaSwFwdIpStatsHCInForwDatagrams = _AristaSwFwdIpStatsHCInForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 13),
    _AristaSwFwdIpStatsHCInForwDatagrams_Type()
)
aristaSwFwdIpStatsHCInForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCInForwDatagrams.setStatus("current")
_AristaSwFwdIpStatsReasmReqds_Type = Counter32
_AristaSwFwdIpStatsReasmReqds_Object = MibTableColumn
aristaSwFwdIpStatsReasmReqds = _AristaSwFwdIpStatsReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 14),
    _AristaSwFwdIpStatsReasmReqds_Type()
)
aristaSwFwdIpStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsReasmReqds.setStatus("current")
_AristaSwFwdIpStatsReasmOKs_Type = Counter32
_AristaSwFwdIpStatsReasmOKs_Object = MibTableColumn
aristaSwFwdIpStatsReasmOKs = _AristaSwFwdIpStatsReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 15),
    _AristaSwFwdIpStatsReasmOKs_Type()
)
aristaSwFwdIpStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsReasmOKs.setStatus("current")
_AristaSwFwdIpStatsReasmFails_Type = Counter32
_AristaSwFwdIpStatsReasmFails_Object = MibTableColumn
aristaSwFwdIpStatsReasmFails = _AristaSwFwdIpStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 16),
    _AristaSwFwdIpStatsReasmFails_Type()
)
aristaSwFwdIpStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsReasmFails.setStatus("current")
_AristaSwFwdIpStatsInDiscards_Type = Counter32
_AristaSwFwdIpStatsInDiscards_Object = MibTableColumn
aristaSwFwdIpStatsInDiscards = _AristaSwFwdIpStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 17),
    _AristaSwFwdIpStatsInDiscards_Type()
)
aristaSwFwdIpStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInDiscards.setStatus("current")
_AristaSwFwdIpStatsInDelivers_Type = Counter32
_AristaSwFwdIpStatsInDelivers_Object = MibTableColumn
aristaSwFwdIpStatsInDelivers = _AristaSwFwdIpStatsInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 18),
    _AristaSwFwdIpStatsInDelivers_Type()
)
aristaSwFwdIpStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInDelivers.setStatus("current")
_AristaSwFwdIpStatsHCInDelivers_Type = Counter64
_AristaSwFwdIpStatsHCInDelivers_Object = MibTableColumn
aristaSwFwdIpStatsHCInDelivers = _AristaSwFwdIpStatsHCInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 19),
    _AristaSwFwdIpStatsHCInDelivers_Type()
)
aristaSwFwdIpStatsHCInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCInDelivers.setStatus("current")
_AristaSwFwdIpStatsOutRequests_Type = Counter32
_AristaSwFwdIpStatsOutRequests_Object = MibTableColumn
aristaSwFwdIpStatsOutRequests = _AristaSwFwdIpStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 20),
    _AristaSwFwdIpStatsOutRequests_Type()
)
aristaSwFwdIpStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutRequests.setStatus("current")
_AristaSwFwdIpStatsHCOutRequests_Type = Counter64
_AristaSwFwdIpStatsHCOutRequests_Object = MibTableColumn
aristaSwFwdIpStatsHCOutRequests = _AristaSwFwdIpStatsHCOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 21),
    _AristaSwFwdIpStatsHCOutRequests_Type()
)
aristaSwFwdIpStatsHCOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCOutRequests.setStatus("current")
_AristaSwFwdIpStatsOutNoRoutes_Type = Counter32
_AristaSwFwdIpStatsOutNoRoutes_Object = MibTableColumn
aristaSwFwdIpStatsOutNoRoutes = _AristaSwFwdIpStatsOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 22),
    _AristaSwFwdIpStatsOutNoRoutes_Type()
)
aristaSwFwdIpStatsOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutNoRoutes.setStatus("current")
_AristaSwFwdIpStatsOutForwDatagrams_Type = Counter32
_AristaSwFwdIpStatsOutForwDatagrams_Object = MibTableColumn
aristaSwFwdIpStatsOutForwDatagrams = _AristaSwFwdIpStatsOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 23),
    _AristaSwFwdIpStatsOutForwDatagrams_Type()
)
aristaSwFwdIpStatsOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutForwDatagrams.setStatus("current")
_AristaSwFwdIpStatsHCOutForwDatagrams_Type = Counter64
_AristaSwFwdIpStatsHCOutForwDatagrams_Object = MibTableColumn
aristaSwFwdIpStatsHCOutForwDatagrams = _AristaSwFwdIpStatsHCOutForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 24),
    _AristaSwFwdIpStatsHCOutForwDatagrams_Type()
)
aristaSwFwdIpStatsHCOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCOutForwDatagrams.setStatus("current")
_AristaSwFwdIpStatsOutDiscards_Type = Counter32
_AristaSwFwdIpStatsOutDiscards_Object = MibTableColumn
aristaSwFwdIpStatsOutDiscards = _AristaSwFwdIpStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 25),
    _AristaSwFwdIpStatsOutDiscards_Type()
)
aristaSwFwdIpStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutDiscards.setStatus("current")
_AristaSwFwdIpStatsOutFragReqds_Type = Counter32
_AristaSwFwdIpStatsOutFragReqds_Object = MibTableColumn
aristaSwFwdIpStatsOutFragReqds = _AristaSwFwdIpStatsOutFragReqds_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 26),
    _AristaSwFwdIpStatsOutFragReqds_Type()
)
aristaSwFwdIpStatsOutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutFragReqds.setStatus("current")
_AristaSwFwdIpStatsOutFragOKs_Type = Counter32
_AristaSwFwdIpStatsOutFragOKs_Object = MibTableColumn
aristaSwFwdIpStatsOutFragOKs = _AristaSwFwdIpStatsOutFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 27),
    _AristaSwFwdIpStatsOutFragOKs_Type()
)
aristaSwFwdIpStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutFragOKs.setStatus("current")
_AristaSwFwdIpStatsOutFragFails_Type = Counter32
_AristaSwFwdIpStatsOutFragFails_Object = MibTableColumn
aristaSwFwdIpStatsOutFragFails = _AristaSwFwdIpStatsOutFragFails_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 28),
    _AristaSwFwdIpStatsOutFragFails_Type()
)
aristaSwFwdIpStatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutFragFails.setStatus("current")
_AristaSwFwdIpStatsOutFragCreates_Type = Counter32
_AristaSwFwdIpStatsOutFragCreates_Object = MibTableColumn
aristaSwFwdIpStatsOutFragCreates = _AristaSwFwdIpStatsOutFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 29),
    _AristaSwFwdIpStatsOutFragCreates_Type()
)
aristaSwFwdIpStatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutFragCreates.setStatus("current")
_AristaSwFwdIpStatsOutTransmits_Type = Counter32
_AristaSwFwdIpStatsOutTransmits_Object = MibTableColumn
aristaSwFwdIpStatsOutTransmits = _AristaSwFwdIpStatsOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 30),
    _AristaSwFwdIpStatsOutTransmits_Type()
)
aristaSwFwdIpStatsOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutTransmits.setStatus("current")
_AristaSwFwdIpStatsHCOutTransmits_Type = Counter64
_AristaSwFwdIpStatsHCOutTransmits_Object = MibTableColumn
aristaSwFwdIpStatsHCOutTransmits = _AristaSwFwdIpStatsHCOutTransmits_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 31),
    _AristaSwFwdIpStatsHCOutTransmits_Type()
)
aristaSwFwdIpStatsHCOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCOutTransmits.setStatus("current")
_AristaSwFwdIpStatsOutOctets_Type = Counter32
_AristaSwFwdIpStatsOutOctets_Object = MibTableColumn
aristaSwFwdIpStatsOutOctets = _AristaSwFwdIpStatsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 32),
    _AristaSwFwdIpStatsOutOctets_Type()
)
aristaSwFwdIpStatsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutOctets.setStatus("current")
_AristaSwFwdIpStatsHCOutOctets_Type = Counter64
_AristaSwFwdIpStatsHCOutOctets_Object = MibTableColumn
aristaSwFwdIpStatsHCOutOctets = _AristaSwFwdIpStatsHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 33),
    _AristaSwFwdIpStatsHCOutOctets_Type()
)
aristaSwFwdIpStatsHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCOutOctets.setStatus("current")
_AristaSwFwdIpStatsInMcastPkts_Type = Counter32
_AristaSwFwdIpStatsInMcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsInMcastPkts = _AristaSwFwdIpStatsInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 34),
    _AristaSwFwdIpStatsInMcastPkts_Type()
)
aristaSwFwdIpStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInMcastPkts.setStatus("current")
_AristaSwFwdIpStatsHCInMcastPkts_Type = Counter64
_AristaSwFwdIpStatsHCInMcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsHCInMcastPkts = _AristaSwFwdIpStatsHCInMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 35),
    _AristaSwFwdIpStatsHCInMcastPkts_Type()
)
aristaSwFwdIpStatsHCInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCInMcastPkts.setStatus("current")
_AristaSwFwdIpStatsInMcastOctets_Type = Counter32
_AristaSwFwdIpStatsInMcastOctets_Object = MibTableColumn
aristaSwFwdIpStatsInMcastOctets = _AristaSwFwdIpStatsInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 36),
    _AristaSwFwdIpStatsInMcastOctets_Type()
)
aristaSwFwdIpStatsInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInMcastOctets.setStatus("current")
_AristaSwFwdIpStatsHCInMcastOctets_Type = Counter64
_AristaSwFwdIpStatsHCInMcastOctets_Object = MibTableColumn
aristaSwFwdIpStatsHCInMcastOctets = _AristaSwFwdIpStatsHCInMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 37),
    _AristaSwFwdIpStatsHCInMcastOctets_Type()
)
aristaSwFwdIpStatsHCInMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCInMcastOctets.setStatus("current")
_AristaSwFwdIpStatsOutMcastPkts_Type = Counter32
_AristaSwFwdIpStatsOutMcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsOutMcastPkts = _AristaSwFwdIpStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 38),
    _AristaSwFwdIpStatsOutMcastPkts_Type()
)
aristaSwFwdIpStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutMcastPkts.setStatus("current")
_AristaSwFwdIpStatsHCOutMcastPkts_Type = Counter64
_AristaSwFwdIpStatsHCOutMcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsHCOutMcastPkts = _AristaSwFwdIpStatsHCOutMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 39),
    _AristaSwFwdIpStatsHCOutMcastPkts_Type()
)
aristaSwFwdIpStatsHCOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCOutMcastPkts.setStatus("current")
_AristaSwFwdIpStatsOutMcastOctets_Type = Counter32
_AristaSwFwdIpStatsOutMcastOctets_Object = MibTableColumn
aristaSwFwdIpStatsOutMcastOctets = _AristaSwFwdIpStatsOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 40),
    _AristaSwFwdIpStatsOutMcastOctets_Type()
)
aristaSwFwdIpStatsOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutMcastOctets.setStatus("current")
_AristaSwFwdIpStatsHCOutMcastOctets_Type = Counter64
_AristaSwFwdIpStatsHCOutMcastOctets_Object = MibTableColumn
aristaSwFwdIpStatsHCOutMcastOctets = _AristaSwFwdIpStatsHCOutMcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 41),
    _AristaSwFwdIpStatsHCOutMcastOctets_Type()
)
aristaSwFwdIpStatsHCOutMcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCOutMcastOctets.setStatus("current")
_AristaSwFwdIpStatsInBcastPkts_Type = Counter32
_AristaSwFwdIpStatsInBcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsInBcastPkts = _AristaSwFwdIpStatsInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 42),
    _AristaSwFwdIpStatsInBcastPkts_Type()
)
aristaSwFwdIpStatsInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsInBcastPkts.setStatus("current")
_AristaSwFwdIpStatsHCInBcastPkts_Type = Counter64
_AristaSwFwdIpStatsHCInBcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsHCInBcastPkts = _AristaSwFwdIpStatsHCInBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 43),
    _AristaSwFwdIpStatsHCInBcastPkts_Type()
)
aristaSwFwdIpStatsHCInBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCInBcastPkts.setStatus("current")
_AristaSwFwdIpStatsOutBcastPkts_Type = Counter32
_AristaSwFwdIpStatsOutBcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsOutBcastPkts = _AristaSwFwdIpStatsOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 44),
    _AristaSwFwdIpStatsOutBcastPkts_Type()
)
aristaSwFwdIpStatsOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsOutBcastPkts.setStatus("current")
_AristaSwFwdIpStatsHCOutBcastPkts_Type = Counter64
_AristaSwFwdIpStatsHCOutBcastPkts_Object = MibTableColumn
aristaSwFwdIpStatsHCOutBcastPkts = _AristaSwFwdIpStatsHCOutBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 45),
    _AristaSwFwdIpStatsHCOutBcastPkts_Type()
)
aristaSwFwdIpStatsHCOutBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsHCOutBcastPkts.setStatus("current")
_AristaSwFwdIpStatsDiscontinuityTime_Type = TimeStamp
_AristaSwFwdIpStatsDiscontinuityTime_Object = MibTableColumn
aristaSwFwdIpStatsDiscontinuityTime = _AristaSwFwdIpStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 46),
    _AristaSwFwdIpStatsDiscontinuityTime_Type()
)
aristaSwFwdIpStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsDiscontinuityTime.setStatus("current")
_AristaSwFwdIpStatsRefreshRate_Type = Unsigned32
_AristaSwFwdIpStatsRefreshRate_Object = MibTableColumn
aristaSwFwdIpStatsRefreshRate = _AristaSwFwdIpStatsRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 1, 1, 1, 47),
    _AristaSwFwdIpStatsRefreshRate_Type()
)
aristaSwFwdIpStatsRefreshRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsRefreshRate.setUnits("milli-seconds")
_AristaSwIpFwdMIBConformance_ObjectIdentity = ObjectIdentity
aristaSwIpFwdMIBConformance = _AristaSwIpFwdMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 2)
)
_AristaSwIpFwdMIBCompliances_ObjectIdentity = ObjectIdentity
aristaSwIpFwdMIBCompliances = _AristaSwIpFwdMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 1)
)
_AristaSwIpFwdMIBGroups_ObjectIdentity = ObjectIdentity
aristaSwIpFwdMIBGroups = _AristaSwIpFwdMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 2)
)

# Managed Objects groups

aristaSwFwdIpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 2, 1)
)
aristaSwFwdIpStatsGroup.setObjects(
      *(("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInReceives"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInReceives"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInHdrErrors"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInNoRoutes"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInAddrErrors"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInUnknownProtos"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInTruncatedPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInForwDatagrams"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInForwDatagrams"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsReasmReqds"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsReasmOKs"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsReasmFails"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInDiscards"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInDelivers"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInDelivers"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutRequests"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutRequests"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutNoRoutes"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutForwDatagrams"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutForwDatagrams"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutDiscards"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragReqds"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragOKs"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragFails"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutFragCreates"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutTransmits"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutTransmits"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInMcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInMcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutMcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutMcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInBcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInBcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutBcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutBcastPkts"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsDiscontinuityTime"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsRefreshRate"))
)
if mibBuilder.loadTexts:
    aristaSwFwdIpStatsGroup.setStatus("current")

aristaSwFwdIpOctetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 2, 2)
)
aristaSwFwdIpOctetGroup.setObjects(
      *(("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInOctets"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInOctets"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutOctets"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutOctets"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsInMcastOctets"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCInMcastOctets"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsOutMcastOctets"),
        ("ARISTA-SW-IP-FORWARDING-MIB", "aristaSwFwdIpStatsHCOutMcastOctets"))
)
if mibBuilder.loadTexts:
    aristaSwFwdIpOctetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaSwIpFwdMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    aristaSwIpFwdMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-SW-IP-FORWARDING-MIB",
    **{"aristaSwIpForwardingMIB": aristaSwIpForwardingMIB,
       "aristaSwFwdIp": aristaSwFwdIp,
       "aristaSwFwdIpStatsTable": aristaSwFwdIpStatsTable,
       "aristaSwFwdIpStatsEntry": aristaSwFwdIpStatsEntry,
       "aristaSwFwdIpStatsIPVersion": aristaSwFwdIpStatsIPVersion,
       "aristaSwFwdIpStatsInReceives": aristaSwFwdIpStatsInReceives,
       "aristaSwFwdIpStatsHCInReceives": aristaSwFwdIpStatsHCInReceives,
       "aristaSwFwdIpStatsInOctets": aristaSwFwdIpStatsInOctets,
       "aristaSwFwdIpStatsHCInOctets": aristaSwFwdIpStatsHCInOctets,
       "aristaSwFwdIpStatsInHdrErrors": aristaSwFwdIpStatsInHdrErrors,
       "aristaSwFwdIpStatsInNoRoutes": aristaSwFwdIpStatsInNoRoutes,
       "aristaSwFwdIpStatsInAddrErrors": aristaSwFwdIpStatsInAddrErrors,
       "aristaSwFwdIpStatsInUnknownProtos": aristaSwFwdIpStatsInUnknownProtos,
       "aristaSwFwdIpStatsInTruncatedPkts": aristaSwFwdIpStatsInTruncatedPkts,
       "aristaSwFwdIpStatsInForwDatagrams": aristaSwFwdIpStatsInForwDatagrams,
       "aristaSwFwdIpStatsHCInForwDatagrams": aristaSwFwdIpStatsHCInForwDatagrams,
       "aristaSwFwdIpStatsReasmReqds": aristaSwFwdIpStatsReasmReqds,
       "aristaSwFwdIpStatsReasmOKs": aristaSwFwdIpStatsReasmOKs,
       "aristaSwFwdIpStatsReasmFails": aristaSwFwdIpStatsReasmFails,
       "aristaSwFwdIpStatsInDiscards": aristaSwFwdIpStatsInDiscards,
       "aristaSwFwdIpStatsInDelivers": aristaSwFwdIpStatsInDelivers,
       "aristaSwFwdIpStatsHCInDelivers": aristaSwFwdIpStatsHCInDelivers,
       "aristaSwFwdIpStatsOutRequests": aristaSwFwdIpStatsOutRequests,
       "aristaSwFwdIpStatsHCOutRequests": aristaSwFwdIpStatsHCOutRequests,
       "aristaSwFwdIpStatsOutNoRoutes": aristaSwFwdIpStatsOutNoRoutes,
       "aristaSwFwdIpStatsOutForwDatagrams": aristaSwFwdIpStatsOutForwDatagrams,
       "aristaSwFwdIpStatsHCOutForwDatagrams": aristaSwFwdIpStatsHCOutForwDatagrams,
       "aristaSwFwdIpStatsOutDiscards": aristaSwFwdIpStatsOutDiscards,
       "aristaSwFwdIpStatsOutFragReqds": aristaSwFwdIpStatsOutFragReqds,
       "aristaSwFwdIpStatsOutFragOKs": aristaSwFwdIpStatsOutFragOKs,
       "aristaSwFwdIpStatsOutFragFails": aristaSwFwdIpStatsOutFragFails,
       "aristaSwFwdIpStatsOutFragCreates": aristaSwFwdIpStatsOutFragCreates,
       "aristaSwFwdIpStatsOutTransmits": aristaSwFwdIpStatsOutTransmits,
       "aristaSwFwdIpStatsHCOutTransmits": aristaSwFwdIpStatsHCOutTransmits,
       "aristaSwFwdIpStatsOutOctets": aristaSwFwdIpStatsOutOctets,
       "aristaSwFwdIpStatsHCOutOctets": aristaSwFwdIpStatsHCOutOctets,
       "aristaSwFwdIpStatsInMcastPkts": aristaSwFwdIpStatsInMcastPkts,
       "aristaSwFwdIpStatsHCInMcastPkts": aristaSwFwdIpStatsHCInMcastPkts,
       "aristaSwFwdIpStatsInMcastOctets": aristaSwFwdIpStatsInMcastOctets,
       "aristaSwFwdIpStatsHCInMcastOctets": aristaSwFwdIpStatsHCInMcastOctets,
       "aristaSwFwdIpStatsOutMcastPkts": aristaSwFwdIpStatsOutMcastPkts,
       "aristaSwFwdIpStatsHCOutMcastPkts": aristaSwFwdIpStatsHCOutMcastPkts,
       "aristaSwFwdIpStatsOutMcastOctets": aristaSwFwdIpStatsOutMcastOctets,
       "aristaSwFwdIpStatsHCOutMcastOctets": aristaSwFwdIpStatsHCOutMcastOctets,
       "aristaSwFwdIpStatsInBcastPkts": aristaSwFwdIpStatsInBcastPkts,
       "aristaSwFwdIpStatsHCInBcastPkts": aristaSwFwdIpStatsHCInBcastPkts,
       "aristaSwFwdIpStatsOutBcastPkts": aristaSwFwdIpStatsOutBcastPkts,
       "aristaSwFwdIpStatsHCOutBcastPkts": aristaSwFwdIpStatsHCOutBcastPkts,
       "aristaSwFwdIpStatsDiscontinuityTime": aristaSwFwdIpStatsDiscontinuityTime,
       "aristaSwFwdIpStatsRefreshRate": aristaSwFwdIpStatsRefreshRate,
       "aristaSwIpFwdMIBConformance": aristaSwIpFwdMIBConformance,
       "aristaSwIpFwdMIBCompliances": aristaSwIpFwdMIBCompliances,
       "aristaSwIpFwdMIBCompliance": aristaSwIpFwdMIBCompliance,
       "aristaSwIpFwdMIBGroups": aristaSwIpFwdMIBGroups,
       "aristaSwFwdIpStatsGroup": aristaSwFwdIpStatsGroup,
       "aristaSwFwdIpOctetGroup": aristaSwFwdIpOctetGroup}
)
