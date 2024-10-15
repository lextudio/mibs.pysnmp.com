# SNMP MIB module (CISCO-CDMA-PDSN-CRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-CDMA-PDSN-CRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:10 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoCdmaPdsnCrpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 957)
)
ciscoCdmaPdsnCrpMIB.setRevisions(
        ("2004-07-27 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CcpcMIBObjects_ObjectIdentity = ObjectIdentity
ccpcMIBObjects = _CcpcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1)
)
_CcpcSystemInfo_ObjectIdentity = ObjectIdentity
ccpcSystemInfo = _CcpcSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1)
)
_CcpcEnabled_Type = TruthValue
_CcpcEnabled_Object = MibScalar
ccpcEnabled = _CcpcEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1, 1),
    _CcpcEnabled_Type()
)
ccpcEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcEnabled.setStatus("current")
_CcpcSessionTotal_Type = Gauge32
_CcpcSessionTotal_Object = MibScalar
ccpcSessionTotal = _CcpcSessionTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 1, 2),
    _CcpcSessionTotal_Type()
)
ccpcSessionTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcSessionTotal.setStatus("current")
_CcpcPerfStats_ObjectIdentity = ObjectIdentity
ccpcPerfStats = _CcpcPerfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2)
)
_CcpcPcfPerfStatsTable_Object = MibTable
ccpcPcfPerfStatsTable = _CcpcPcfPerfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ccpcPcfPerfStatsTable.setStatus("current")
_CcpcPcfPerfStatsEntry_Object = MibTableRow
ccpcPcfPerfStatsEntry = _CcpcPcfPerfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1)
)
ccpcPcfPerfStatsEntry.setIndexNames(
    (0, "CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfIpAddressType"),
    (0, "CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfIpAddress"),
)
if mibBuilder.loadTexts:
    ccpcPcfPerfStatsEntry.setStatus("current")
_CcpcPcfIpAddressType_Type = InetAddressType
_CcpcPcfIpAddressType_Object = MibTableColumn
ccpcPcfIpAddressType = _CcpcPcfIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 1),
    _CcpcPcfIpAddressType_Type()
)
ccpcPcfIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccpcPcfIpAddressType.setStatus("current")
_CcpcPcfIpAddress_Type = InetAddress
_CcpcPcfIpAddress_Object = MibTableColumn
ccpcPcfIpAddress = _CcpcPcfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 2),
    _CcpcPcfIpAddress_Type()
)
ccpcPcfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ccpcPcfIpAddress.setStatus("current")
_CcpcPcfRcvdIcrqs_Type = Counter32
_CcpcPcfRcvdIcrqs_Object = MibTableColumn
ccpcPcfRcvdIcrqs = _CcpcPcfRcvdIcrqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 3),
    _CcpcPcfRcvdIcrqs_Type()
)
ccpcPcfRcvdIcrqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfRcvdIcrqs.setStatus("current")
_CcpcPcfAcptdIcrqs_Type = Counter32
_CcpcPcfAcptdIcrqs_Object = MibTableColumn
ccpcPcfAcptdIcrqs = _CcpcPcfAcptdIcrqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 4),
    _CcpcPcfAcptdIcrqs_Type()
)
ccpcPcfAcptdIcrqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfAcptdIcrqs.setStatus("current")
_CcpcPcfDroppedIcrqs_Type = Counter32
_CcpcPcfDroppedIcrqs_Object = MibTableColumn
ccpcPcfDroppedIcrqs = _CcpcPcfDroppedIcrqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 5),
    _CcpcPcfDroppedIcrqs_Type()
)
ccpcPcfDroppedIcrqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfDroppedIcrqs.setStatus("current")
_CcpcPcfSentIcrps_Type = Counter32
_CcpcPcfSentIcrps_Object = MibTableColumn
ccpcPcfSentIcrps = _CcpcPcfSentIcrps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 6),
    _CcpcPcfSentIcrps_Type()
)
ccpcPcfSentIcrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfSentIcrps.setStatus("current")
_CcpcPcfRcvdIccns_Type = Counter32
_CcpcPcfRcvdIccns_Object = MibTableColumn
ccpcPcfRcvdIccns = _CcpcPcfRcvdIccns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 7),
    _CcpcPcfRcvdIccns_Type()
)
ccpcPcfRcvdIccns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfRcvdIccns.setStatus("current")
_CcpcPcfAcptdIccns_Type = Counter32
_CcpcPcfAcptdIccns_Object = MibTableColumn
ccpcPcfAcptdIccns = _CcpcPcfAcptdIccns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 8),
    _CcpcPcfAcptdIccns_Type()
)
ccpcPcfAcptdIccns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfAcptdIccns.setStatus("current")
_CcpcPcfDroppedIccns_Type = Counter32
_CcpcPcfDroppedIccns_Object = MibTableColumn
ccpcPcfDroppedIccns = _CcpcPcfDroppedIccns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 9),
    _CcpcPcfDroppedIccns_Type()
)
ccpcPcfDroppedIccns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfDroppedIccns.setStatus("current")
_CcpcPcfRcvdCdns_Type = Counter32
_CcpcPcfRcvdCdns_Object = MibTableColumn
ccpcPcfRcvdCdns = _CcpcPcfRcvdCdns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 10),
    _CcpcPcfRcvdCdns_Type()
)
ccpcPcfRcvdCdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfRcvdCdns.setStatus("current")
_CcpcPcfSentCdns_Type = Counter32
_CcpcPcfSentCdns_Object = MibTableColumn
ccpcPcfSentCdns = _CcpcPcfSentCdns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 11),
    _CcpcPcfSentCdns_Type()
)
ccpcPcfSentCdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfSentCdns.setStatus("current")
_CcpcPcfDroppedCdns_Type = Counter32
_CcpcPcfDroppedCdns_Object = MibTableColumn
ccpcPcfDroppedCdns = _CcpcPcfDroppedCdns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 12),
    _CcpcPcfDroppedCdns_Type()
)
ccpcPcfDroppedCdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfDroppedCdns.setStatus("current")
_CcpcPcfRcvdZlbs_Type = Counter32
_CcpcPcfRcvdZlbs_Object = MibTableColumn
ccpcPcfRcvdZlbs = _CcpcPcfRcvdZlbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 13),
    _CcpcPcfRcvdZlbs_Type()
)
ccpcPcfRcvdZlbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfRcvdZlbs.setStatus("current")
_CcpcPcfSentZlbs_Type = Counter32
_CcpcPcfSentZlbs_Object = MibTableColumn
ccpcPcfSentZlbs = _CcpcPcfSentZlbs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 1, 2, 1, 1, 14),
    _CcpcPcfSentZlbs_Type()
)
ccpcPcfSentZlbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ccpcPcfSentZlbs.setStatus("current")
_CcpcMIBConformance_ObjectIdentity = ObjectIdentity
ccpcMIBConformance = _CcpcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 2)
)
_CcpcMIBCompliances_ObjectIdentity = ObjectIdentity
ccpcMIBCompliances = _CcpcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 1)
)
_CcpcMIBGroups_ObjectIdentity = ObjectIdentity
ccpcMIBGroups = _CcpcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2)
)

# Managed Objects groups

ccpcSystemGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2, 1)
)
ccpcSystemGrp.setObjects(
      *(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcEnabled"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcSessionTotal"))
)
if mibBuilder.loadTexts:
    ccpcSystemGrp.setStatus("current")

ccpcPerfGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 2, 2)
)
ccpcPerfGrp.setObjects(
      *(("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdIcrqs"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfAcptdIcrqs"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedIcrqs"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentIcrps"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdIccns"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfAcptdIccns"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedIccns"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdCdns"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentCdns"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfDroppedCdns"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfRcvdZlbs"),
        ("CISCO-CDMA-PDSN-CRP-MIB", "ccpcPcfSentZlbs"))
)
if mibBuilder.loadTexts:
    ccpcPerfGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ccpcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 957, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ccpcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-CDMA-PDSN-CRP-MIB",
    **{"ciscoCdmaPdsnCrpMIB": ciscoCdmaPdsnCrpMIB,
       "ccpcMIBObjects": ccpcMIBObjects,
       "ccpcSystemInfo": ccpcSystemInfo,
       "ccpcEnabled": ccpcEnabled,
       "ccpcSessionTotal": ccpcSessionTotal,
       "ccpcPerfStats": ccpcPerfStats,
       "ccpcPcfPerfStatsTable": ccpcPcfPerfStatsTable,
       "ccpcPcfPerfStatsEntry": ccpcPcfPerfStatsEntry,
       "ccpcPcfIpAddressType": ccpcPcfIpAddressType,
       "ccpcPcfIpAddress": ccpcPcfIpAddress,
       "ccpcPcfRcvdIcrqs": ccpcPcfRcvdIcrqs,
       "ccpcPcfAcptdIcrqs": ccpcPcfAcptdIcrqs,
       "ccpcPcfDroppedIcrqs": ccpcPcfDroppedIcrqs,
       "ccpcPcfSentIcrps": ccpcPcfSentIcrps,
       "ccpcPcfRcvdIccns": ccpcPcfRcvdIccns,
       "ccpcPcfAcptdIccns": ccpcPcfAcptdIccns,
       "ccpcPcfDroppedIccns": ccpcPcfDroppedIccns,
       "ccpcPcfRcvdCdns": ccpcPcfRcvdCdns,
       "ccpcPcfSentCdns": ccpcPcfSentCdns,
       "ccpcPcfDroppedCdns": ccpcPcfDroppedCdns,
       "ccpcPcfRcvdZlbs": ccpcPcfRcvdZlbs,
       "ccpcPcfSentZlbs": ccpcPcfSentZlbs,
       "ccpcMIBConformance": ccpcMIBConformance,
       "ccpcMIBCompliances": ccpcMIBCompliances,
       "ccpcMIBCompliance": ccpcMIBCompliance,
       "ccpcMIBGroups": ccpcMIBGroups,
       "ccpcSystemGrp": ccpcSystemGrp,
       "ccpcPerfGrp": ccpcPerfGrp}
)
