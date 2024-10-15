# SNMP MIB module (CISCO-SESS-BORDER-CTRLR-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SESS-BORDER-CTRLR-STATS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:13 2024
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

(CiscoSbcPeriodicStatsInterval,
 csbCallStatsInstanceIndex,
 csbCallStatsServiceIndex) = mibBuilder.importSymbols(
    "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB",
    "CiscoSbcPeriodicStatsInterval",
    "csbCallStatsInstanceIndex",
    "csbCallStatsServiceIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoSbcStatsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 757)
)
ciscoSbcStatsMIB.setRevisions(
        ("2010-09-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoSbcSIPMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("ack", 2),
          ("bye", 3),
          ("cancel", 4),
          ("info", 5),
          ("invite", 6),
          ("message", 7),
          ("notify", 8),
          ("options", 9),
          ("prack", 10),
          ("refer", 11),
          ("register", 12),
          ("subscribe", 13),
          ("unknown", 1),
          ("update", 14))
    )



class CiscoSbcRadiusClientType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accounting", 2),
          ("authentication", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSbcStatsMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSbcStatsMIBNotifs = _CiscoSbcStatsMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 0)
)
_CiscoSbcStatsMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSbcStatsMIBObjects = _CiscoSbcStatsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1)
)
_CsbRadiusStatsTable_Object = MibTable
csbRadiusStatsTable = _CsbRadiusStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1)
)
if mibBuilder.loadTexts:
    csbRadiusStatsTable.setStatus("current")
_CsbRadiusStatsEntry_Object = MibTableRow
csbRadiusStatsEntry = _CsbRadiusStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1)
)
csbRadiusStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsEntIndex"),
)
if mibBuilder.loadTexts:
    csbRadiusStatsEntry.setStatus("current")
_CsbRadiusStatsEntIndex_Type = Unsigned32
_CsbRadiusStatsEntIndex_Object = MibTableColumn
csbRadiusStatsEntIndex = _CsbRadiusStatsEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 1),
    _CsbRadiusStatsEntIndex_Type()
)
csbRadiusStatsEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbRadiusStatsEntIndex.setStatus("current")
_CsbRadiusStatsClientName_Type = SnmpAdminString
_CsbRadiusStatsClientName_Object = MibTableColumn
csbRadiusStatsClientName = _CsbRadiusStatsClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 2),
    _CsbRadiusStatsClientName_Type()
)
csbRadiusStatsClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsClientName.setStatus("current")
_CsbRadiusStatsClientType_Type = CiscoSbcRadiusClientType
_CsbRadiusStatsClientType_Object = MibTableColumn
csbRadiusStatsClientType = _CsbRadiusStatsClientType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 3),
    _CsbRadiusStatsClientType_Type()
)
csbRadiusStatsClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsClientType.setStatus("current")
_CsbRadiusStatsSrvrName_Type = SnmpAdminString
_CsbRadiusStatsSrvrName_Object = MibTableColumn
csbRadiusStatsSrvrName = _CsbRadiusStatsSrvrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 4),
    _CsbRadiusStatsSrvrName_Type()
)
csbRadiusStatsSrvrName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsSrvrName.setStatus("current")
_CsbRadiusStatsAcsReqs_Type = Counter64
_CsbRadiusStatsAcsReqs_Object = MibTableColumn
csbRadiusStatsAcsReqs = _CsbRadiusStatsAcsReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 5),
    _CsbRadiusStatsAcsReqs_Type()
)
csbRadiusStatsAcsReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsReqs.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsReqs.setUnits("packets")
_CsbRadiusStatsAcsRtrns_Type = Counter64
_CsbRadiusStatsAcsRtrns_Object = MibTableColumn
csbRadiusStatsAcsRtrns = _CsbRadiusStatsAcsRtrns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 6),
    _CsbRadiusStatsAcsRtrns_Type()
)
csbRadiusStatsAcsRtrns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsRtrns.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsRtrns.setUnits("packets")
_CsbRadiusStatsAcsAccpts_Type = Counter64
_CsbRadiusStatsAcsAccpts_Object = MibTableColumn
csbRadiusStatsAcsAccpts = _CsbRadiusStatsAcsAccpts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 7),
    _CsbRadiusStatsAcsAccpts_Type()
)
csbRadiusStatsAcsAccpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsAccpts.setStatus("current")
_CsbRadiusStatsAcsRejects_Type = Counter64
_CsbRadiusStatsAcsRejects_Object = MibTableColumn
csbRadiusStatsAcsRejects = _CsbRadiusStatsAcsRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 8),
    _CsbRadiusStatsAcsRejects_Type()
)
csbRadiusStatsAcsRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsRejects.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsRejects.setUnits("packets")
_CsbRadiusStatsAcsChalls_Type = Counter64
_CsbRadiusStatsAcsChalls_Object = MibTableColumn
csbRadiusStatsAcsChalls = _CsbRadiusStatsAcsChalls_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 9),
    _CsbRadiusStatsAcsChalls_Type()
)
csbRadiusStatsAcsChalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsChalls.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsAcsChalls.setUnits("packets")
_CsbRadiusStatsActReqs_Type = Counter64
_CsbRadiusStatsActReqs_Object = MibTableColumn
csbRadiusStatsActReqs = _CsbRadiusStatsActReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 10),
    _CsbRadiusStatsActReqs_Type()
)
csbRadiusStatsActReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsActReqs.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsActReqs.setUnits("packets")
_CsbRadiusStatsActRetrans_Type = Counter64
_CsbRadiusStatsActRetrans_Object = MibTableColumn
csbRadiusStatsActRetrans = _CsbRadiusStatsActRetrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 11),
    _CsbRadiusStatsActRetrans_Type()
)
csbRadiusStatsActRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsActRetrans.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsActRetrans.setUnits("packets")
_CsbRadiusStatsActRsps_Type = Counter64
_CsbRadiusStatsActRsps_Object = MibTableColumn
csbRadiusStatsActRsps = _CsbRadiusStatsActRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 12),
    _CsbRadiusStatsActRsps_Type()
)
csbRadiusStatsActRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsActRsps.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsActRsps.setUnits("packets")
_CsbRadiusStatsMalformedRsps_Type = Counter64
_CsbRadiusStatsMalformedRsps_Object = MibTableColumn
csbRadiusStatsMalformedRsps = _CsbRadiusStatsMalformedRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 13),
    _CsbRadiusStatsMalformedRsps_Type()
)
csbRadiusStatsMalformedRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsMalformedRsps.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsMalformedRsps.setUnits("packets")
_CsbRadiusStatsBadAuths_Type = Counter64
_CsbRadiusStatsBadAuths_Object = MibTableColumn
csbRadiusStatsBadAuths = _CsbRadiusStatsBadAuths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 14),
    _CsbRadiusStatsBadAuths_Type()
)
csbRadiusStatsBadAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsBadAuths.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsBadAuths.setUnits("packets")
_CsbRadiusStatsPending_Type = Gauge32
_CsbRadiusStatsPending_Object = MibTableColumn
csbRadiusStatsPending = _CsbRadiusStatsPending_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 15),
    _CsbRadiusStatsPending_Type()
)
csbRadiusStatsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsPending.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsPending.setUnits("packets")
_CsbRadiusStatsTimeouts_Type = Counter64
_CsbRadiusStatsTimeouts_Object = MibTableColumn
csbRadiusStatsTimeouts = _CsbRadiusStatsTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 16),
    _CsbRadiusStatsTimeouts_Type()
)
csbRadiusStatsTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsTimeouts.setUnits("packets")
_CsbRadiusStatsUnknownType_Type = Counter64
_CsbRadiusStatsUnknownType_Object = MibTableColumn
csbRadiusStatsUnknownType = _CsbRadiusStatsUnknownType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 17),
    _CsbRadiusStatsUnknownType_Type()
)
csbRadiusStatsUnknownType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsUnknownType.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsUnknownType.setUnits("packets")
_CsbRadiusStatsDropped_Type = Counter64
_CsbRadiusStatsDropped_Object = MibTableColumn
csbRadiusStatsDropped = _CsbRadiusStatsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 1, 1, 18),
    _CsbRadiusStatsDropped_Type()
)
csbRadiusStatsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRadiusStatsDropped.setStatus("current")
if mibBuilder.loadTexts:
    csbRadiusStatsDropped.setUnits("packets")
_CsbRfBillRealmStatsTable_Object = MibTable
csbRfBillRealmStatsTable = _CsbRfBillRealmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2)
)
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTable.setStatus("current")
_CsbRfBillRealmStatsEntry_Object = MibTableRow
csbRfBillRealmStatsEntry = _CsbRfBillRealmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1)
)
csbRfBillRealmStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsRealmName"),
)
if mibBuilder.loadTexts:
    csbRfBillRealmStatsEntry.setStatus("current")


class _CsbRfBillRealmStatsIndex_Type(Unsigned32):
    """Custom type csbRfBillRealmStatsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_CsbRfBillRealmStatsIndex_Type.__name__ = "Unsigned32"
_CsbRfBillRealmStatsIndex_Object = MibTableColumn
csbRfBillRealmStatsIndex = _CsbRfBillRealmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 1),
    _CsbRfBillRealmStatsIndex_Type()
)
csbRfBillRealmStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsIndex.setStatus("current")
_CsbRfBillRealmStatsRealmName_Type = SnmpAdminString
_CsbRfBillRealmStatsRealmName_Object = MibTableColumn
csbRfBillRealmStatsRealmName = _CsbRfBillRealmStatsRealmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 2),
    _CsbRfBillRealmStatsRealmName_Type()
)
csbRfBillRealmStatsRealmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsRealmName.setStatus("current")
_CsbRfBillRealmStatsTotalStartAcrs_Type = Unsigned32
_CsbRfBillRealmStatsTotalStartAcrs_Object = MibTableColumn
csbRfBillRealmStatsTotalStartAcrs = _CsbRfBillRealmStatsTotalStartAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 3),
    _CsbRfBillRealmStatsTotalStartAcrs_Type()
)
csbRfBillRealmStatsTotalStartAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalStartAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalStartAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsTotalInterimAcrs_Type = Unsigned32
_CsbRfBillRealmStatsTotalInterimAcrs_Object = MibTableColumn
csbRfBillRealmStatsTotalInterimAcrs = _CsbRfBillRealmStatsTotalInterimAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 4),
    _CsbRfBillRealmStatsTotalInterimAcrs_Type()
)
csbRfBillRealmStatsTotalInterimAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalInterimAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalInterimAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsTotalStopAcrs_Type = Unsigned32
_CsbRfBillRealmStatsTotalStopAcrs_Object = MibTableColumn
csbRfBillRealmStatsTotalStopAcrs = _CsbRfBillRealmStatsTotalStopAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 5),
    _CsbRfBillRealmStatsTotalStopAcrs_Type()
)
csbRfBillRealmStatsTotalStopAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalStopAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalStopAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsTotalEventAcrs_Type = Unsigned32
_CsbRfBillRealmStatsTotalEventAcrs_Object = MibTableColumn
csbRfBillRealmStatsTotalEventAcrs = _CsbRfBillRealmStatsTotalEventAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 6),
    _CsbRfBillRealmStatsTotalEventAcrs_Type()
)
csbRfBillRealmStatsTotalEventAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalEventAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsTotalEventAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsSuccStartAcrs_Type = Unsigned32
_CsbRfBillRealmStatsSuccStartAcrs_Object = MibTableColumn
csbRfBillRealmStatsSuccStartAcrs = _CsbRfBillRealmStatsSuccStartAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 7),
    _CsbRfBillRealmStatsSuccStartAcrs_Type()
)
csbRfBillRealmStatsSuccStartAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccStartAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccStartAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsSuccInterimAcrs_Type = Unsigned32
_CsbRfBillRealmStatsSuccInterimAcrs_Object = MibTableColumn
csbRfBillRealmStatsSuccInterimAcrs = _CsbRfBillRealmStatsSuccInterimAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 8),
    _CsbRfBillRealmStatsSuccInterimAcrs_Type()
)
csbRfBillRealmStatsSuccInterimAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccInterimAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccInterimAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsSuccStopAcrs_Type = Unsigned32
_CsbRfBillRealmStatsSuccStopAcrs_Object = MibTableColumn
csbRfBillRealmStatsSuccStopAcrs = _CsbRfBillRealmStatsSuccStopAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 9),
    _CsbRfBillRealmStatsSuccStopAcrs_Type()
)
csbRfBillRealmStatsSuccStopAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccStopAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccStopAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsSuccEventAcrs_Type = Unsigned32
_CsbRfBillRealmStatsSuccEventAcrs_Object = MibTableColumn
csbRfBillRealmStatsSuccEventAcrs = _CsbRfBillRealmStatsSuccEventAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 10),
    _CsbRfBillRealmStatsSuccEventAcrs_Type()
)
csbRfBillRealmStatsSuccEventAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccEventAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsSuccEventAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsFailStartAcrs_Type = Unsigned32
_CsbRfBillRealmStatsFailStartAcrs_Object = MibTableColumn
csbRfBillRealmStatsFailStartAcrs = _CsbRfBillRealmStatsFailStartAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 11),
    _CsbRfBillRealmStatsFailStartAcrs_Type()
)
csbRfBillRealmStatsFailStartAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailStartAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailStartAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsFailInterimAcrs_Type = Unsigned32
_CsbRfBillRealmStatsFailInterimAcrs_Object = MibTableColumn
csbRfBillRealmStatsFailInterimAcrs = _CsbRfBillRealmStatsFailInterimAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 12),
    _CsbRfBillRealmStatsFailInterimAcrs_Type()
)
csbRfBillRealmStatsFailInterimAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailInterimAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailInterimAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsFailStopAcrs_Type = Unsigned32
_CsbRfBillRealmStatsFailStopAcrs_Object = MibTableColumn
csbRfBillRealmStatsFailStopAcrs = _CsbRfBillRealmStatsFailStopAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 13),
    _CsbRfBillRealmStatsFailStopAcrs_Type()
)
csbRfBillRealmStatsFailStopAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailStopAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailStopAcrs.setUnits("ACRs")
_CsbRfBillRealmStatsFailEventAcrs_Type = Unsigned32
_CsbRfBillRealmStatsFailEventAcrs_Object = MibTableColumn
csbRfBillRealmStatsFailEventAcrs = _CsbRfBillRealmStatsFailEventAcrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 2, 1, 14),
    _CsbRfBillRealmStatsFailEventAcrs_Type()
)
csbRfBillRealmStatsFailEventAcrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailEventAcrs.setStatus("current")
if mibBuilder.loadTexts:
    csbRfBillRealmStatsFailEventAcrs.setUnits("ACRs")
_CsbSIPMthdCurrentStatsTable_Object = MibTable
csbSIPMthdCurrentStatsTable = _CsbSIPMthdCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3)
)
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsTable.setStatus("current")
_CsbSIPMthdCurrentStatsEntry_Object = MibTableRow
csbSIPMthdCurrentStatsEntry = _CsbSIPMthdCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1)
)
csbSIPMthdCurrentStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsAdjName"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsMethod"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsInterval"),
)
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsEntry.setStatus("current")
_CsbSIPMthdCurrentStatsAdjName_Type = SnmpAdminString
_CsbSIPMthdCurrentStatsAdjName_Object = MibTableColumn
csbSIPMthdCurrentStatsAdjName = _CsbSIPMthdCurrentStatsAdjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 1),
    _CsbSIPMthdCurrentStatsAdjName_Type()
)
csbSIPMthdCurrentStatsAdjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsAdjName.setStatus("current")
_CsbSIPMthdCurrentStatsMethod_Type = CiscoSbcSIPMethod
_CsbSIPMthdCurrentStatsMethod_Object = MibTableColumn
csbSIPMthdCurrentStatsMethod = _CsbSIPMthdCurrentStatsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 2),
    _CsbSIPMthdCurrentStatsMethod_Type()
)
csbSIPMthdCurrentStatsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsMethod.setStatus("current")
_CsbSIPMthdCurrentStatsInterval_Type = CiscoSbcPeriodicStatsInterval
_CsbSIPMthdCurrentStatsInterval_Object = MibTableColumn
csbSIPMthdCurrentStatsInterval = _CsbSIPMthdCurrentStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 3),
    _CsbSIPMthdCurrentStatsInterval_Type()
)
csbSIPMthdCurrentStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsInterval.setStatus("current")
_CsbSIPMthdCurrentStatsMethodName_Type = SnmpAdminString
_CsbSIPMthdCurrentStatsMethodName_Object = MibTableColumn
csbSIPMthdCurrentStatsMethodName = _CsbSIPMthdCurrentStatsMethodName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 4),
    _CsbSIPMthdCurrentStatsMethodName_Type()
)
csbSIPMthdCurrentStatsMethodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsMethodName.setStatus("current")
_CsbSIPMthdCurrentStatsReqIn_Type = Gauge32
_CsbSIPMthdCurrentStatsReqIn_Object = MibTableColumn
csbSIPMthdCurrentStatsReqIn = _CsbSIPMthdCurrentStatsReqIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 5),
    _CsbSIPMthdCurrentStatsReqIn_Type()
)
csbSIPMthdCurrentStatsReqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsReqIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsReqIn.setUnits("requests")
_CsbSIPMthdCurrentStatsReqOut_Type = Gauge32
_CsbSIPMthdCurrentStatsReqOut_Object = MibTableColumn
csbSIPMthdCurrentStatsReqOut = _CsbSIPMthdCurrentStatsReqOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 6),
    _CsbSIPMthdCurrentStatsReqOut_Type()
)
csbSIPMthdCurrentStatsReqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsReqOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsReqOut.setUnits("requests")
_CsbSIPMthdCurrentStatsResp1xxIn_Type = Gauge32
_CsbSIPMthdCurrentStatsResp1xxIn_Object = MibTableColumn
csbSIPMthdCurrentStatsResp1xxIn = _CsbSIPMthdCurrentStatsResp1xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 7),
    _CsbSIPMthdCurrentStatsResp1xxIn_Type()
)
csbSIPMthdCurrentStatsResp1xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp1xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp1xxIn.setUnits("responses")
_CsbSIPMthdCurrentStatsResp1xxOut_Type = Gauge32
_CsbSIPMthdCurrentStatsResp1xxOut_Object = MibTableColumn
csbSIPMthdCurrentStatsResp1xxOut = _CsbSIPMthdCurrentStatsResp1xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 8),
    _CsbSIPMthdCurrentStatsResp1xxOut_Type()
)
csbSIPMthdCurrentStatsResp1xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp1xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp1xxOut.setUnits("responses")
_CsbSIPMthdCurrentStatsResp2xxIn_Type = Gauge32
_CsbSIPMthdCurrentStatsResp2xxIn_Object = MibTableColumn
csbSIPMthdCurrentStatsResp2xxIn = _CsbSIPMthdCurrentStatsResp2xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 9),
    _CsbSIPMthdCurrentStatsResp2xxIn_Type()
)
csbSIPMthdCurrentStatsResp2xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp2xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp2xxIn.setUnits("responses")
_CsbSIPMthdCurrentStatsResp2xxOut_Type = Gauge32
_CsbSIPMthdCurrentStatsResp2xxOut_Object = MibTableColumn
csbSIPMthdCurrentStatsResp2xxOut = _CsbSIPMthdCurrentStatsResp2xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 10),
    _CsbSIPMthdCurrentStatsResp2xxOut_Type()
)
csbSIPMthdCurrentStatsResp2xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp2xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp2xxOut.setUnits("responses")
_CsbSIPMthdCurrentStatsResp3xxIn_Type = Gauge32
_CsbSIPMthdCurrentStatsResp3xxIn_Object = MibTableColumn
csbSIPMthdCurrentStatsResp3xxIn = _CsbSIPMthdCurrentStatsResp3xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 11),
    _CsbSIPMthdCurrentStatsResp3xxIn_Type()
)
csbSIPMthdCurrentStatsResp3xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp3xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp3xxIn.setUnits("responses")
_CsbSIPMthdCurrentStatsResp3xxOut_Type = Gauge32
_CsbSIPMthdCurrentStatsResp3xxOut_Object = MibTableColumn
csbSIPMthdCurrentStatsResp3xxOut = _CsbSIPMthdCurrentStatsResp3xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 12),
    _CsbSIPMthdCurrentStatsResp3xxOut_Type()
)
csbSIPMthdCurrentStatsResp3xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp3xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp3xxOut.setUnits("responses")
_CsbSIPMthdCurrentStatsResp4xxIn_Type = Gauge32
_CsbSIPMthdCurrentStatsResp4xxIn_Object = MibTableColumn
csbSIPMthdCurrentStatsResp4xxIn = _CsbSIPMthdCurrentStatsResp4xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 13),
    _CsbSIPMthdCurrentStatsResp4xxIn_Type()
)
csbSIPMthdCurrentStatsResp4xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp4xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp4xxIn.setUnits("responses")
_CsbSIPMthdCurrentStatsResp4xxOut_Type = Gauge32
_CsbSIPMthdCurrentStatsResp4xxOut_Object = MibTableColumn
csbSIPMthdCurrentStatsResp4xxOut = _CsbSIPMthdCurrentStatsResp4xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 14),
    _CsbSIPMthdCurrentStatsResp4xxOut_Type()
)
csbSIPMthdCurrentStatsResp4xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp4xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp4xxOut.setUnits("responses")
_CsbSIPMthdCurrentStatsResp5xxIn_Type = Gauge32
_CsbSIPMthdCurrentStatsResp5xxIn_Object = MibTableColumn
csbSIPMthdCurrentStatsResp5xxIn = _CsbSIPMthdCurrentStatsResp5xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 15),
    _CsbSIPMthdCurrentStatsResp5xxIn_Type()
)
csbSIPMthdCurrentStatsResp5xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp5xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp5xxIn.setUnits("responses")
_CsbSIPMthdCurrentStatsResp5xxOut_Type = Gauge32
_CsbSIPMthdCurrentStatsResp5xxOut_Object = MibTableColumn
csbSIPMthdCurrentStatsResp5xxOut = _CsbSIPMthdCurrentStatsResp5xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 16),
    _CsbSIPMthdCurrentStatsResp5xxOut_Type()
)
csbSIPMthdCurrentStatsResp5xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp5xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp5xxOut.setUnits("responses")
_CsbSIPMthdCurrentStatsResp6xxIn_Type = Gauge32
_CsbSIPMthdCurrentStatsResp6xxIn_Object = MibTableColumn
csbSIPMthdCurrentStatsResp6xxIn = _CsbSIPMthdCurrentStatsResp6xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 17),
    _CsbSIPMthdCurrentStatsResp6xxIn_Type()
)
csbSIPMthdCurrentStatsResp6xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp6xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp6xxIn.setUnits("responses")
_CsbSIPMthdCurrentStatsResp6xxOut_Type = Gauge32
_CsbSIPMthdCurrentStatsResp6xxOut_Object = MibTableColumn
csbSIPMthdCurrentStatsResp6xxOut = _CsbSIPMthdCurrentStatsResp6xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 3, 1, 18),
    _CsbSIPMthdCurrentStatsResp6xxOut_Type()
)
csbSIPMthdCurrentStatsResp6xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp6xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsResp6xxOut.setUnits("responses")
_CsbSIPMthdHistoryStatsTable_Object = MibTable
csbSIPMthdHistoryStatsTable = _CsbSIPMthdHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4)
)
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsTable.setStatus("current")
_CsbSIPMthdHistoryStatsEntry_Object = MibTableRow
csbSIPMthdHistoryStatsEntry = _CsbSIPMthdHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1)
)
csbSIPMthdHistoryStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsAdjName"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsMethod"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsInterval"),
)
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsEntry.setStatus("current")
_CsbSIPMthdHistoryStatsAdjName_Type = SnmpAdminString
_CsbSIPMthdHistoryStatsAdjName_Object = MibTableColumn
csbSIPMthdHistoryStatsAdjName = _CsbSIPMthdHistoryStatsAdjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 1),
    _CsbSIPMthdHistoryStatsAdjName_Type()
)
csbSIPMthdHistoryStatsAdjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsAdjName.setStatus("current")
_CsbSIPMthdHistoryStatsMethod_Type = CiscoSbcSIPMethod
_CsbSIPMthdHistoryStatsMethod_Object = MibTableColumn
csbSIPMthdHistoryStatsMethod = _CsbSIPMthdHistoryStatsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 2),
    _CsbSIPMthdHistoryStatsMethod_Type()
)
csbSIPMthdHistoryStatsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsMethod.setStatus("current")
_CsbSIPMthdHistoryStatsInterval_Type = CiscoSbcPeriodicStatsInterval
_CsbSIPMthdHistoryStatsInterval_Object = MibTableColumn
csbSIPMthdHistoryStatsInterval = _CsbSIPMthdHistoryStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 3),
    _CsbSIPMthdHistoryStatsInterval_Type()
)
csbSIPMthdHistoryStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsInterval.setStatus("current")
_CsbSIPMthdHistoryStatsMethodName_Type = SnmpAdminString
_CsbSIPMthdHistoryStatsMethodName_Object = MibTableColumn
csbSIPMthdHistoryStatsMethodName = _CsbSIPMthdHistoryStatsMethodName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 4),
    _CsbSIPMthdHistoryStatsMethodName_Type()
)
csbSIPMthdHistoryStatsMethodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsMethodName.setStatus("current")
_CsbSIPMthdHistoryStatsReqIn_Type = Gauge32
_CsbSIPMthdHistoryStatsReqIn_Object = MibTableColumn
csbSIPMthdHistoryStatsReqIn = _CsbSIPMthdHistoryStatsReqIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 5),
    _CsbSIPMthdHistoryStatsReqIn_Type()
)
csbSIPMthdHistoryStatsReqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsReqIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsReqIn.setUnits("requests")
_CsbSIPMthdHistoryStatsReqOut_Type = Gauge32
_CsbSIPMthdHistoryStatsReqOut_Object = MibTableColumn
csbSIPMthdHistoryStatsReqOut = _CsbSIPMthdHistoryStatsReqOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 6),
    _CsbSIPMthdHistoryStatsReqOut_Type()
)
csbSIPMthdHistoryStatsReqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsReqOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsReqOut.setUnits("requests")
_CsbSIPMthdHistoryStatsResp1xxIn_Type = Gauge32
_CsbSIPMthdHistoryStatsResp1xxIn_Object = MibTableColumn
csbSIPMthdHistoryStatsResp1xxIn = _CsbSIPMthdHistoryStatsResp1xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 7),
    _CsbSIPMthdHistoryStatsResp1xxIn_Type()
)
csbSIPMthdHistoryStatsResp1xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp1xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp1xxIn.setUnits("responses")
_CsbSIPMthdHistoryStatsResp1xxOut_Type = Gauge32
_CsbSIPMthdHistoryStatsResp1xxOut_Object = MibTableColumn
csbSIPMthdHistoryStatsResp1xxOut = _CsbSIPMthdHistoryStatsResp1xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 8),
    _CsbSIPMthdHistoryStatsResp1xxOut_Type()
)
csbSIPMthdHistoryStatsResp1xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp1xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp1xxOut.setUnits("responses")
_CsbSIPMthdHistoryStatsResp2xxIn_Type = Gauge32
_CsbSIPMthdHistoryStatsResp2xxIn_Object = MibTableColumn
csbSIPMthdHistoryStatsResp2xxIn = _CsbSIPMthdHistoryStatsResp2xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 9),
    _CsbSIPMthdHistoryStatsResp2xxIn_Type()
)
csbSIPMthdHistoryStatsResp2xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp2xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp2xxIn.setUnits("responses")
_CsbSIPMthdHistoryStatsResp2xxOut_Type = Gauge32
_CsbSIPMthdHistoryStatsResp2xxOut_Object = MibTableColumn
csbSIPMthdHistoryStatsResp2xxOut = _CsbSIPMthdHistoryStatsResp2xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 10),
    _CsbSIPMthdHistoryStatsResp2xxOut_Type()
)
csbSIPMthdHistoryStatsResp2xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp2xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp2xxOut.setUnits("responses")
_CsbSIPMthdHistoryStatsResp3xxIn_Type = Gauge32
_CsbSIPMthdHistoryStatsResp3xxIn_Object = MibTableColumn
csbSIPMthdHistoryStatsResp3xxIn = _CsbSIPMthdHistoryStatsResp3xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 11),
    _CsbSIPMthdHistoryStatsResp3xxIn_Type()
)
csbSIPMthdHistoryStatsResp3xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp3xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp3xxIn.setUnits("responses")
_CsbSIPMthdHistoryStatsResp3xxOut_Type = Gauge32
_CsbSIPMthdHistoryStatsResp3xxOut_Object = MibTableColumn
csbSIPMthdHistoryStatsResp3xxOut = _CsbSIPMthdHistoryStatsResp3xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 12),
    _CsbSIPMthdHistoryStatsResp3xxOut_Type()
)
csbSIPMthdHistoryStatsResp3xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp3xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp3xxOut.setUnits("responses")
_CsbSIPMthdHistoryStatsResp4xxIn_Type = Gauge32
_CsbSIPMthdHistoryStatsResp4xxIn_Object = MibTableColumn
csbSIPMthdHistoryStatsResp4xxIn = _CsbSIPMthdHistoryStatsResp4xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 13),
    _CsbSIPMthdHistoryStatsResp4xxIn_Type()
)
csbSIPMthdHistoryStatsResp4xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp4xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp4xxIn.setUnits("responses")
_CsbSIPMthdHistoryStatsResp4xxOut_Type = Gauge32
_CsbSIPMthdHistoryStatsResp4xxOut_Object = MibTableColumn
csbSIPMthdHistoryStatsResp4xxOut = _CsbSIPMthdHistoryStatsResp4xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 14),
    _CsbSIPMthdHistoryStatsResp4xxOut_Type()
)
csbSIPMthdHistoryStatsResp4xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp4xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp4xxOut.setUnits("responses")
_CsbSIPMthdHistoryStatsResp5xxIn_Type = Gauge32
_CsbSIPMthdHistoryStatsResp5xxIn_Object = MibTableColumn
csbSIPMthdHistoryStatsResp5xxIn = _CsbSIPMthdHistoryStatsResp5xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 15),
    _CsbSIPMthdHistoryStatsResp5xxIn_Type()
)
csbSIPMthdHistoryStatsResp5xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp5xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp5xxIn.setUnits("responses")
_CsbSIPMthdHistoryStatsResp5xxOut_Type = Gauge32
_CsbSIPMthdHistoryStatsResp5xxOut_Object = MibTableColumn
csbSIPMthdHistoryStatsResp5xxOut = _CsbSIPMthdHistoryStatsResp5xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 16),
    _CsbSIPMthdHistoryStatsResp5xxOut_Type()
)
csbSIPMthdHistoryStatsResp5xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp5xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp5xxOut.setUnits("responses")
_CsbSIPMthdHistoryStatsResp6xxIn_Type = Gauge32
_CsbSIPMthdHistoryStatsResp6xxIn_Object = MibTableColumn
csbSIPMthdHistoryStatsResp6xxIn = _CsbSIPMthdHistoryStatsResp6xxIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 17),
    _CsbSIPMthdHistoryStatsResp6xxIn_Type()
)
csbSIPMthdHistoryStatsResp6xxIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp6xxIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp6xxIn.setUnits("responses")
_CsbSIPMthdHistoryStatsResp6xxOut_Type = Gauge32
_CsbSIPMthdHistoryStatsResp6xxOut_Object = MibTableColumn
csbSIPMthdHistoryStatsResp6xxOut = _CsbSIPMthdHistoryStatsResp6xxOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 4, 1, 18),
    _CsbSIPMthdHistoryStatsResp6xxOut_Type()
)
csbSIPMthdHistoryStatsResp6xxOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp6xxOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsResp6xxOut.setUnits("responses")
_CsbSIPMthdRCCurrentStatsTable_Object = MibTable
csbSIPMthdRCCurrentStatsTable = _CsbSIPMthdRCCurrentStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5)
)
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsTable.setStatus("current")
_CsbSIPMthdRCCurrentStatsEntry_Object = MibTableRow
csbSIPMthdRCCurrentStatsEntry = _CsbSIPMthdRCCurrentStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1)
)
csbSIPMthdRCCurrentStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsAdjName"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsMethod"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsRespCode"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsInterval"),
)
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsEntry.setStatus("current")
_CsbSIPMthdRCCurrentStatsAdjName_Type = SnmpAdminString
_CsbSIPMthdRCCurrentStatsAdjName_Object = MibTableColumn
csbSIPMthdRCCurrentStatsAdjName = _CsbSIPMthdRCCurrentStatsAdjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1, 1),
    _CsbSIPMthdRCCurrentStatsAdjName_Type()
)
csbSIPMthdRCCurrentStatsAdjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsAdjName.setStatus("current")
_CsbSIPMthdRCCurrentStatsMethod_Type = CiscoSbcSIPMethod
_CsbSIPMthdRCCurrentStatsMethod_Object = MibTableColumn
csbSIPMthdRCCurrentStatsMethod = _CsbSIPMthdRCCurrentStatsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1, 2),
    _CsbSIPMthdRCCurrentStatsMethod_Type()
)
csbSIPMthdRCCurrentStatsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsMethod.setStatus("current")
_CsbSIPMthdRCCurrentStatsRespCode_Type = Unsigned32
_CsbSIPMthdRCCurrentStatsRespCode_Object = MibTableColumn
csbSIPMthdRCCurrentStatsRespCode = _CsbSIPMthdRCCurrentStatsRespCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1, 3),
    _CsbSIPMthdRCCurrentStatsRespCode_Type()
)
csbSIPMthdRCCurrentStatsRespCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsRespCode.setStatus("current")
_CsbSIPMthdRCCurrentStatsInterval_Type = CiscoSbcPeriodicStatsInterval
_CsbSIPMthdRCCurrentStatsInterval_Object = MibTableColumn
csbSIPMthdRCCurrentStatsInterval = _CsbSIPMthdRCCurrentStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1, 4),
    _CsbSIPMthdRCCurrentStatsInterval_Type()
)
csbSIPMthdRCCurrentStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsInterval.setStatus("current")
_CsbSIPMthdRCCurrentStatsMethodName_Type = SnmpAdminString
_CsbSIPMthdRCCurrentStatsMethodName_Object = MibTableColumn
csbSIPMthdRCCurrentStatsMethodName = _CsbSIPMthdRCCurrentStatsMethodName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1, 5),
    _CsbSIPMthdRCCurrentStatsMethodName_Type()
)
csbSIPMthdRCCurrentStatsMethodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsMethodName.setStatus("current")
_CsbSIPMthdRCCurrentStatsRespIn_Type = Gauge32
_CsbSIPMthdRCCurrentStatsRespIn_Object = MibTableColumn
csbSIPMthdRCCurrentStatsRespIn = _CsbSIPMthdRCCurrentStatsRespIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1, 6),
    _CsbSIPMthdRCCurrentStatsRespIn_Type()
)
csbSIPMthdRCCurrentStatsRespIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsRespIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsRespIn.setUnits("responses")
_CsbSIPMthdRCCurrentStatsRespOut_Type = Gauge32
_CsbSIPMthdRCCurrentStatsRespOut_Object = MibTableColumn
csbSIPMthdRCCurrentStatsRespOut = _CsbSIPMthdRCCurrentStatsRespOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 5, 1, 7),
    _CsbSIPMthdRCCurrentStatsRespOut_Type()
)
csbSIPMthdRCCurrentStatsRespOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsRespOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsRespOut.setUnits("responses")
_CsbSIPMthdRCHistoryStatsTable_Object = MibTable
csbSIPMthdRCHistoryStatsTable = _CsbSIPMthdRCHistoryStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6)
)
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsTable.setStatus("current")
_CsbSIPMthdRCHistoryStatsEntry_Object = MibTableRow
csbSIPMthdRCHistoryStatsEntry = _CsbSIPMthdRCHistoryStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1)
)
csbSIPMthdRCHistoryStatsEntry.setIndexNames(
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsInstanceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-CALL-STATS-MIB", "csbCallStatsServiceIndex"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsAdjName"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsMethod"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsRespCode"),
    (0, "CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsInterval"),
)
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsEntry.setStatus("current")
_CsbSIPMthdRCHistoryStatsAdjName_Type = SnmpAdminString
_CsbSIPMthdRCHistoryStatsAdjName_Object = MibTableColumn
csbSIPMthdRCHistoryStatsAdjName = _CsbSIPMthdRCHistoryStatsAdjName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1, 1),
    _CsbSIPMthdRCHistoryStatsAdjName_Type()
)
csbSIPMthdRCHistoryStatsAdjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsAdjName.setStatus("current")
_CsbSIPMthdRCHistoryStatsMethod_Type = CiscoSbcSIPMethod
_CsbSIPMthdRCHistoryStatsMethod_Object = MibTableColumn
csbSIPMthdRCHistoryStatsMethod = _CsbSIPMthdRCHistoryStatsMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1, 2),
    _CsbSIPMthdRCHistoryStatsMethod_Type()
)
csbSIPMthdRCHistoryStatsMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsMethod.setStatus("current")
_CsbSIPMthdRCHistoryStatsMethodName_Type = SnmpAdminString
_CsbSIPMthdRCHistoryStatsMethodName_Object = MibTableColumn
csbSIPMthdRCHistoryStatsMethodName = _CsbSIPMthdRCHistoryStatsMethodName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1, 3),
    _CsbSIPMthdRCHistoryStatsMethodName_Type()
)
csbSIPMthdRCHistoryStatsMethodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsMethodName.setStatus("current")
_CsbSIPMthdRCHistoryStatsRespCode_Type = Unsigned32
_CsbSIPMthdRCHistoryStatsRespCode_Object = MibTableColumn
csbSIPMthdRCHistoryStatsRespCode = _CsbSIPMthdRCHistoryStatsRespCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1, 4),
    _CsbSIPMthdRCHistoryStatsRespCode_Type()
)
csbSIPMthdRCHistoryStatsRespCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsRespCode.setStatus("current")
_CsbSIPMthdRCHistoryStatsInterval_Type = CiscoSbcPeriodicStatsInterval
_CsbSIPMthdRCHistoryStatsInterval_Object = MibTableColumn
csbSIPMthdRCHistoryStatsInterval = _CsbSIPMthdRCHistoryStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1, 5),
    _CsbSIPMthdRCHistoryStatsInterval_Type()
)
csbSIPMthdRCHistoryStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsInterval.setStatus("current")
_CsbSIPMthdRCHistoryStatsRespIn_Type = Gauge32
_CsbSIPMthdRCHistoryStatsRespIn_Object = MibTableColumn
csbSIPMthdRCHistoryStatsRespIn = _CsbSIPMthdRCHistoryStatsRespIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1, 6),
    _CsbSIPMthdRCHistoryStatsRespIn_Type()
)
csbSIPMthdRCHistoryStatsRespIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsRespIn.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsRespIn.setUnits("responses")
_CsbSIPMthdRCHistoryStatsRespOut_Type = Gauge32
_CsbSIPMthdRCHistoryStatsRespOut_Object = MibTableColumn
csbSIPMthdRCHistoryStatsRespOut = _CsbSIPMthdRCHistoryStatsRespOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 1, 6, 1, 7),
    _CsbSIPMthdRCHistoryStatsRespOut_Type()
)
csbSIPMthdRCHistoryStatsRespOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsRespOut.setStatus("current")
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsRespOut.setUnits("responses")
_CiscoSbcStatsMIBConform_ObjectIdentity = ObjectIdentity
ciscoSbcStatsMIBConform = _CiscoSbcStatsMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2)
)
_CsbStatsMIBCompliances_ObjectIdentity = ObjectIdentity
csbStatsMIBCompliances = _CsbStatsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 1)
)
_CsbStatsMIBGroups_ObjectIdentity = ObjectIdentity
csbStatsMIBGroups = _CsbStatsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 2)
)

# Managed Objects groups

csbRadiusStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 2, 1)
)
csbRadiusStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsClientName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsClientType"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsSrvrName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsAcsReqs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsAcsRtrns"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsAcsAccpts"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsAcsRejects"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsAcsChalls"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsActReqs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsActRetrans"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsActRsps"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsMalformedRsps"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsBadAuths"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsPending"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsTimeouts"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsUnknownType"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRadiusStatsDropped"))
)
if mibBuilder.loadTexts:
    csbRadiusStatsGroup.setStatus("current")

csbRfBillRealmStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 2, 2)
)
csbRfBillRealmStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsRealmName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsTotalStartAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsTotalInterimAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsTotalStopAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsTotalEventAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsSuccStartAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsSuccInterimAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsSuccStopAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsSuccEventAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsFailStartAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsFailInterimAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsFailStopAcrs"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbRfBillRealmStatsFailEventAcrs"))
)
if mibBuilder.loadTexts:
    csbRfBillRealmStatsGroup.setStatus("current")

csbSIPMthdCurrentStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 2, 3)
)
csbSIPMthdCurrentStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsAdjName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsMethodName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsReqIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsReqOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp1xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp1xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp2xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp2xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp3xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp3xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp4xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp4xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp5xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp5xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp6xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdCurrentStatsResp6xxOut"))
)
if mibBuilder.loadTexts:
    csbSIPMthdCurrentStatsGroup.setStatus("current")

csbSIPMthdHistoryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 2, 4)
)
csbSIPMthdHistoryStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsAdjName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsMethodName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsReqIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsReqOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp1xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp1xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp2xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp2xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp3xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp3xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp4xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp4xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp5xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp5xxOut"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp6xxIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdHistoryStatsResp6xxOut"))
)
if mibBuilder.loadTexts:
    csbSIPMthdHistoryStatsGroup.setStatus("current")

csbSIPMthdRCCurrentStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 2, 5)
)
csbSIPMthdRCCurrentStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsAdjName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsMethodName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsRespIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCCurrentStatsRespOut"))
)
if mibBuilder.loadTexts:
    csbSIPMthdRCCurrentStatsGroup.setStatus("current")

csbSIPMthdRCHistoryStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 2, 6)
)
csbSIPMthdRCHistoryStatsGroup.setObjects(
      *(("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsAdjName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsMethodName"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsRespIn"),
        ("CISCO-SESS-BORDER-CTRLR-STATS-MIB", "csbSIPMthdRCHistoryStatsRespOut"))
)
if mibBuilder.loadTexts:
    csbSIPMthdRCHistoryStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csbStatsMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 757, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csbStatsMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SESS-BORDER-CTRLR-STATS-MIB",
    **{"CiscoSbcSIPMethod": CiscoSbcSIPMethod,
       "CiscoSbcRadiusClientType": CiscoSbcRadiusClientType,
       "ciscoSbcStatsMIB": ciscoSbcStatsMIB,
       "ciscoSbcStatsMIBNotifs": ciscoSbcStatsMIBNotifs,
       "ciscoSbcStatsMIBObjects": ciscoSbcStatsMIBObjects,
       "csbRadiusStatsTable": csbRadiusStatsTable,
       "csbRadiusStatsEntry": csbRadiusStatsEntry,
       "csbRadiusStatsEntIndex": csbRadiusStatsEntIndex,
       "csbRadiusStatsClientName": csbRadiusStatsClientName,
       "csbRadiusStatsClientType": csbRadiusStatsClientType,
       "csbRadiusStatsSrvrName": csbRadiusStatsSrvrName,
       "csbRadiusStatsAcsReqs": csbRadiusStatsAcsReqs,
       "csbRadiusStatsAcsRtrns": csbRadiusStatsAcsRtrns,
       "csbRadiusStatsAcsAccpts": csbRadiusStatsAcsAccpts,
       "csbRadiusStatsAcsRejects": csbRadiusStatsAcsRejects,
       "csbRadiusStatsAcsChalls": csbRadiusStatsAcsChalls,
       "csbRadiusStatsActReqs": csbRadiusStatsActReqs,
       "csbRadiusStatsActRetrans": csbRadiusStatsActRetrans,
       "csbRadiusStatsActRsps": csbRadiusStatsActRsps,
       "csbRadiusStatsMalformedRsps": csbRadiusStatsMalformedRsps,
       "csbRadiusStatsBadAuths": csbRadiusStatsBadAuths,
       "csbRadiusStatsPending": csbRadiusStatsPending,
       "csbRadiusStatsTimeouts": csbRadiusStatsTimeouts,
       "csbRadiusStatsUnknownType": csbRadiusStatsUnknownType,
       "csbRadiusStatsDropped": csbRadiusStatsDropped,
       "csbRfBillRealmStatsTable": csbRfBillRealmStatsTable,
       "csbRfBillRealmStatsEntry": csbRfBillRealmStatsEntry,
       "csbRfBillRealmStatsIndex": csbRfBillRealmStatsIndex,
       "csbRfBillRealmStatsRealmName": csbRfBillRealmStatsRealmName,
       "csbRfBillRealmStatsTotalStartAcrs": csbRfBillRealmStatsTotalStartAcrs,
       "csbRfBillRealmStatsTotalInterimAcrs": csbRfBillRealmStatsTotalInterimAcrs,
       "csbRfBillRealmStatsTotalStopAcrs": csbRfBillRealmStatsTotalStopAcrs,
       "csbRfBillRealmStatsTotalEventAcrs": csbRfBillRealmStatsTotalEventAcrs,
       "csbRfBillRealmStatsSuccStartAcrs": csbRfBillRealmStatsSuccStartAcrs,
       "csbRfBillRealmStatsSuccInterimAcrs": csbRfBillRealmStatsSuccInterimAcrs,
       "csbRfBillRealmStatsSuccStopAcrs": csbRfBillRealmStatsSuccStopAcrs,
       "csbRfBillRealmStatsSuccEventAcrs": csbRfBillRealmStatsSuccEventAcrs,
       "csbRfBillRealmStatsFailStartAcrs": csbRfBillRealmStatsFailStartAcrs,
       "csbRfBillRealmStatsFailInterimAcrs": csbRfBillRealmStatsFailInterimAcrs,
       "csbRfBillRealmStatsFailStopAcrs": csbRfBillRealmStatsFailStopAcrs,
       "csbRfBillRealmStatsFailEventAcrs": csbRfBillRealmStatsFailEventAcrs,
       "csbSIPMthdCurrentStatsTable": csbSIPMthdCurrentStatsTable,
       "csbSIPMthdCurrentStatsEntry": csbSIPMthdCurrentStatsEntry,
       "csbSIPMthdCurrentStatsAdjName": csbSIPMthdCurrentStatsAdjName,
       "csbSIPMthdCurrentStatsMethod": csbSIPMthdCurrentStatsMethod,
       "csbSIPMthdCurrentStatsInterval": csbSIPMthdCurrentStatsInterval,
       "csbSIPMthdCurrentStatsMethodName": csbSIPMthdCurrentStatsMethodName,
       "csbSIPMthdCurrentStatsReqIn": csbSIPMthdCurrentStatsReqIn,
       "csbSIPMthdCurrentStatsReqOut": csbSIPMthdCurrentStatsReqOut,
       "csbSIPMthdCurrentStatsResp1xxIn": csbSIPMthdCurrentStatsResp1xxIn,
       "csbSIPMthdCurrentStatsResp1xxOut": csbSIPMthdCurrentStatsResp1xxOut,
       "csbSIPMthdCurrentStatsResp2xxIn": csbSIPMthdCurrentStatsResp2xxIn,
       "csbSIPMthdCurrentStatsResp2xxOut": csbSIPMthdCurrentStatsResp2xxOut,
       "csbSIPMthdCurrentStatsResp3xxIn": csbSIPMthdCurrentStatsResp3xxIn,
       "csbSIPMthdCurrentStatsResp3xxOut": csbSIPMthdCurrentStatsResp3xxOut,
       "csbSIPMthdCurrentStatsResp4xxIn": csbSIPMthdCurrentStatsResp4xxIn,
       "csbSIPMthdCurrentStatsResp4xxOut": csbSIPMthdCurrentStatsResp4xxOut,
       "csbSIPMthdCurrentStatsResp5xxIn": csbSIPMthdCurrentStatsResp5xxIn,
       "csbSIPMthdCurrentStatsResp5xxOut": csbSIPMthdCurrentStatsResp5xxOut,
       "csbSIPMthdCurrentStatsResp6xxIn": csbSIPMthdCurrentStatsResp6xxIn,
       "csbSIPMthdCurrentStatsResp6xxOut": csbSIPMthdCurrentStatsResp6xxOut,
       "csbSIPMthdHistoryStatsTable": csbSIPMthdHistoryStatsTable,
       "csbSIPMthdHistoryStatsEntry": csbSIPMthdHistoryStatsEntry,
       "csbSIPMthdHistoryStatsAdjName": csbSIPMthdHistoryStatsAdjName,
       "csbSIPMthdHistoryStatsMethod": csbSIPMthdHistoryStatsMethod,
       "csbSIPMthdHistoryStatsInterval": csbSIPMthdHistoryStatsInterval,
       "csbSIPMthdHistoryStatsMethodName": csbSIPMthdHistoryStatsMethodName,
       "csbSIPMthdHistoryStatsReqIn": csbSIPMthdHistoryStatsReqIn,
       "csbSIPMthdHistoryStatsReqOut": csbSIPMthdHistoryStatsReqOut,
       "csbSIPMthdHistoryStatsResp1xxIn": csbSIPMthdHistoryStatsResp1xxIn,
       "csbSIPMthdHistoryStatsResp1xxOut": csbSIPMthdHistoryStatsResp1xxOut,
       "csbSIPMthdHistoryStatsResp2xxIn": csbSIPMthdHistoryStatsResp2xxIn,
       "csbSIPMthdHistoryStatsResp2xxOut": csbSIPMthdHistoryStatsResp2xxOut,
       "csbSIPMthdHistoryStatsResp3xxIn": csbSIPMthdHistoryStatsResp3xxIn,
       "csbSIPMthdHistoryStatsResp3xxOut": csbSIPMthdHistoryStatsResp3xxOut,
       "csbSIPMthdHistoryStatsResp4xxIn": csbSIPMthdHistoryStatsResp4xxIn,
       "csbSIPMthdHistoryStatsResp4xxOut": csbSIPMthdHistoryStatsResp4xxOut,
       "csbSIPMthdHistoryStatsResp5xxIn": csbSIPMthdHistoryStatsResp5xxIn,
       "csbSIPMthdHistoryStatsResp5xxOut": csbSIPMthdHistoryStatsResp5xxOut,
       "csbSIPMthdHistoryStatsResp6xxIn": csbSIPMthdHistoryStatsResp6xxIn,
       "csbSIPMthdHistoryStatsResp6xxOut": csbSIPMthdHistoryStatsResp6xxOut,
       "csbSIPMthdRCCurrentStatsTable": csbSIPMthdRCCurrentStatsTable,
       "csbSIPMthdRCCurrentStatsEntry": csbSIPMthdRCCurrentStatsEntry,
       "csbSIPMthdRCCurrentStatsAdjName": csbSIPMthdRCCurrentStatsAdjName,
       "csbSIPMthdRCCurrentStatsMethod": csbSIPMthdRCCurrentStatsMethod,
       "csbSIPMthdRCCurrentStatsRespCode": csbSIPMthdRCCurrentStatsRespCode,
       "csbSIPMthdRCCurrentStatsInterval": csbSIPMthdRCCurrentStatsInterval,
       "csbSIPMthdRCCurrentStatsMethodName": csbSIPMthdRCCurrentStatsMethodName,
       "csbSIPMthdRCCurrentStatsRespIn": csbSIPMthdRCCurrentStatsRespIn,
       "csbSIPMthdRCCurrentStatsRespOut": csbSIPMthdRCCurrentStatsRespOut,
       "csbSIPMthdRCHistoryStatsTable": csbSIPMthdRCHistoryStatsTable,
       "csbSIPMthdRCHistoryStatsEntry": csbSIPMthdRCHistoryStatsEntry,
       "csbSIPMthdRCHistoryStatsAdjName": csbSIPMthdRCHistoryStatsAdjName,
       "csbSIPMthdRCHistoryStatsMethod": csbSIPMthdRCHistoryStatsMethod,
       "csbSIPMthdRCHistoryStatsMethodName": csbSIPMthdRCHistoryStatsMethodName,
       "csbSIPMthdRCHistoryStatsRespCode": csbSIPMthdRCHistoryStatsRespCode,
       "csbSIPMthdRCHistoryStatsInterval": csbSIPMthdRCHistoryStatsInterval,
       "csbSIPMthdRCHistoryStatsRespIn": csbSIPMthdRCHistoryStatsRespIn,
       "csbSIPMthdRCHistoryStatsRespOut": csbSIPMthdRCHistoryStatsRespOut,
       "ciscoSbcStatsMIBConform": ciscoSbcStatsMIBConform,
       "csbStatsMIBCompliances": csbStatsMIBCompliances,
       "csbStatsMIBCompliance": csbStatsMIBCompliance,
       "csbStatsMIBGroups": csbStatsMIBGroups,
       "csbRadiusStatsGroup": csbRadiusStatsGroup,
       "csbRfBillRealmStatsGroup": csbRfBillRealmStatsGroup,
       "csbSIPMthdCurrentStatsGroup": csbSIPMthdCurrentStatsGroup,
       "csbSIPMthdHistoryStatsGroup": csbSIPMthdHistoryStatsGroup,
       "csbSIPMthdRCCurrentStatsGroup": csbSIPMthdRCCurrentStatsGroup,
       "csbSIPMthdRCHistoryStatsGroup": csbSIPMthdRCHistoryStatsGroup}
)
