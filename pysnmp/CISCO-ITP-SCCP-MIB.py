# SNMP MIB module (CISCO-ITP-SCCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-SCCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:34 2024
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

(cItpSpCLLICode,
 cItpSpDisplayName) = mibBuilder.importSymbols(
    "CISCO-ITP-SP-MIB",
    "cItpSpCLLICode",
    "cItpSpDisplayName")

(CItpTcDisplayPC,
 CItpTcGtaAddr,
 CItpTcGtaDisplay,
 CItpTcGtaDisplayZB,
 CItpTcNAI,
 CItpTcNumberingPlan,
 CItpTcPointCode,
 CItpTcSubSystemNumber,
 CItpTcTableLoadStatus,
 CItpTcTranslationType,
 CItpTcXuaName) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcDisplayPC",
    "CItpTcGtaAddr",
    "CItpTcGtaDisplay",
    "CItpTcGtaDisplayZB",
    "CItpTcNAI",
    "CItpTcNumberingPlan",
    "CItpTcPointCode",
    "CItpTcSubSystemNumber",
    "CItpTcTableLoadStatus",
    "CItpTcTranslationType",
    "CItpTcXuaName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpSccpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233)
)
ciscoItpSccpMIB.setRevisions(
        ("2003-02-03 00:00",
         "2002-04-02 00:00",
         "2002-02-28 00:00",
         "2001-09-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CItpSccpConPcListName(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class CItpSccpGttSelName(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )



class CItpSccpGttAppName(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class CItpSccpGttPrefName(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class CItpSccpGttDisplaySS(OctetString, TextualConvention):
    status = "deprecated"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 3),
    )



class CItpSccpGttAppCost(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class CItpSccpGttAppType(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("as", 3),
          ("pc", 1),
          ("pcssn", 2))
    )



class CItpSccpGttGtaAddrLen(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )



class CItpSccpGttGtaAddrLenZB(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )



class CItpSccpGttMapType(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("primary", 1))
    )



class CItpSccpGttGtaResType(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("app", 3),
          ("as", 4),
          ("pc", 1),
          ("pcssn", 2))
    )



class CItpSccpGttRoutingInd(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("replTT", 5),
          ("ri2gt", 1),
          ("ri2ssn", 2),
          ("riNotAppl", 6),
          ("riUndef", 7),
          ("ssnRI2gt", 3),
          ("ssnRI2ssn", 4))
    )



class CItpSccpGttMapPcStatus(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("prohibited", 2))
    )



class CItpSccpGttMapSsStatus(Integer32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("prohibited", 2))
    )



class CItpSccpGttMultInd(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("cost", 4),
          ("dominant", 3),
          ("shared", 2),
          ("solitary", 1))
    )



class CItpSccpGttMapCongStatus(Integer32, TextualConvention):
    status = "deprecated"
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
        *(("congLevel1", 2),
          ("congLevel2", 3),
          ("congLevel3", 4),
          ("notCong", 1))
    )



class CItpSccpGttTransType(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpSccpGttQOS(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CItpSccpGttGlobalTitleInd(Unsigned32, TextualConvention):
    status = "deprecated"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_CItpSccpMIBNotifs_ObjectIdentity = ObjectIdentity
cItpSccpMIBNotifs = _CItpSccpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 0)
)
_CItpSccpNotifications_ObjectIdentity = ObjectIdentity
cItpSccpNotifications = _CItpSccpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 0, 0)
)
_CItpSccpMIBObjects_ObjectIdentity = ObjectIdentity
cItpSccpMIBObjects = _CItpSccpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1)
)
_CItpSccpScalars_ObjectIdentity = ObjectIdentity
cItpSccpScalars = _CItpSccpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1)
)
_CItpSccpTotalMsgs_Type = Counter32
_CItpSccpTotalMsgs_Object = MibScalar
cItpSccpTotalMsgs = _CItpSccpTotalMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 1),
    _CItpSccpTotalMsgs_Type()
)
cItpSccpTotalMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpTotalMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpTotalMsgs.setUnits("packets")
_CItpSccpLocalMsgs_Type = Counter32
_CItpSccpLocalMsgs_Object = MibScalar
cItpSccpLocalMsgs = _CItpSccpLocalMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 2),
    _CItpSccpLocalMsgs_Type()
)
cItpSccpLocalMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpLocalMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpLocalMsgs.setUnits("packets")
_CItpSccpTotalGttMsgs_Type = Counter32
_CItpSccpTotalGttMsgs_Object = MibScalar
cItpSccpTotalGttMsgs = _CItpSccpTotalGttMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 3),
    _CItpSccpTotalGttMsgs_Type()
)
cItpSccpTotalGttMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpTotalGttMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpTotalGttMsgs.setUnits("packets")
_CItpSccpUDTMsgsSent_Type = Counter32
_CItpSccpUDTMsgsSent_Object = MibScalar
cItpSccpUDTMsgsSent = _CItpSccpUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 4),
    _CItpSccpUDTMsgsSent_Type()
)
cItpSccpUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpUDTMsgsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpUDTMsgsSent.setUnits("packets")
_CItpSccpUDTSMsgsSent_Type = Counter32
_CItpSccpUDTSMsgsSent_Object = MibScalar
cItpSccpUDTSMsgsSent = _CItpSccpUDTSMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 5),
    _CItpSccpUDTSMsgsSent_Type()
)
cItpSccpUDTSMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpUDTSMsgsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpUDTSMsgsSent.setUnits("packets")
_CItpSccpUDTMsgsRcvd_Type = Counter32
_CItpSccpUDTMsgsRcvd_Object = MibScalar
cItpSccpUDTMsgsRcvd = _CItpSccpUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 6),
    _CItpSccpUDTMsgsRcvd_Type()
)
cItpSccpUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpUDTMsgsRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpUDTMsgsRcvd.setUnits("packets")
_CItpSccpUDTSMsgsRcvd_Type = Counter32
_CItpSccpUDTSMsgsRcvd_Object = MibScalar
cItpSccpUDTSMsgsRcvd = _CItpSccpUDTSMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 7),
    _CItpSccpUDTSMsgsRcvd_Type()
)
cItpSccpUDTSMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpUDTSMsgsRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpUDTSMsgsRcvd.setUnits("packets")
_CItpSccpXUDTMsgsSent_Type = Counter32
_CItpSccpXUDTMsgsSent_Object = MibScalar
cItpSccpXUDTMsgsSent = _CItpSccpXUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 8),
    _CItpSccpXUDTMsgsSent_Type()
)
cItpSccpXUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpXUDTMsgsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpXUDTMsgsSent.setUnits("packets")
_CItpSccpXUDTSMsgsSent_Type = Counter32
_CItpSccpXUDTSMsgsSent_Object = MibScalar
cItpSccpXUDTSMsgsSent = _CItpSccpXUDTSMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 9),
    _CItpSccpXUDTSMsgsSent_Type()
)
cItpSccpXUDTSMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpXUDTSMsgsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpXUDTSMsgsSent.setUnits("packets")
_CItpSccpXUDTMsgsRcvd_Type = Counter32
_CItpSccpXUDTMsgsRcvd_Object = MibScalar
cItpSccpXUDTMsgsRcvd = _CItpSccpXUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 10),
    _CItpSccpXUDTMsgsRcvd_Type()
)
cItpSccpXUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpXUDTMsgsRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpXUDTMsgsRcvd.setUnits("packets")
_CItpSccpXUDTSMsgsRcvd_Type = Counter32
_CItpSccpXUDTSMsgsRcvd_Object = MibScalar
cItpSccpXUDTSMsgsRcvd = _CItpSccpXUDTSMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 11),
    _CItpSccpXUDTSMsgsRcvd_Type()
)
cItpSccpXUDTSMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpXUDTSMsgsRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpXUDTSMsgsRcvd.setUnits("packets")
_CItpSccpLUDTMsgsSent_Type = Counter32
_CItpSccpLUDTMsgsSent_Object = MibScalar
cItpSccpLUDTMsgsSent = _CItpSccpLUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 12),
    _CItpSccpLUDTMsgsSent_Type()
)
cItpSccpLUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpLUDTMsgsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpLUDTMsgsSent.setUnits("packets")
_CItpSccpLUDTSMsgsSent_Type = Counter32
_CItpSccpLUDTSMsgsSent_Object = MibScalar
cItpSccpLUDTSMsgsSent = _CItpSccpLUDTSMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 13),
    _CItpSccpLUDTSMsgsSent_Type()
)
cItpSccpLUDTSMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpLUDTSMsgsSent.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpLUDTSMsgsSent.setUnits("packets")
_CItpSccpLUDTMsgsRcvd_Type = Counter32
_CItpSccpLUDTMsgsRcvd_Object = MibScalar
cItpSccpLUDTMsgsRcvd = _CItpSccpLUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 14),
    _CItpSccpLUDTMsgsRcvd_Type()
)
cItpSccpLUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpLUDTMsgsRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpLUDTMsgsRcvd.setUnits("packets")
_CItpSccpLUDTSMsgsRcvd_Type = Counter32
_CItpSccpLUDTSMsgsRcvd_Object = MibScalar
cItpSccpLUDTSMsgsRcvd = _CItpSccpLUDTSMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 15),
    _CItpSccpLUDTSMsgsRcvd_Type()
)
cItpSccpLUDTSMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpLUDTSMsgsRcvd.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpLUDTSMsgsRcvd.setUnits("packets")
_CItpSccpCrToMtp_Type = Counter32
_CItpSccpCrToMtp_Object = MibScalar
cItpSccpCrToMtp = _CItpSccpCrToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 16),
    _CItpSccpCrToMtp_Type()
)
cItpSccpCrToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpCrToMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpCrToMtp.setUnits("packets")
_CItpSccpCrefToMtp_Type = Counter32
_CItpSccpCrefToMtp_Object = MibScalar
cItpSccpCrefToMtp = _CItpSccpCrefToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 17),
    _CItpSccpCrefToMtp_Type()
)
cItpSccpCrefToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpCrefToMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpCrefToMtp.setUnits("packets")
_CItpSccpCrFromMtp_Type = Counter32
_CItpSccpCrFromMtp_Object = MibScalar
cItpSccpCrFromMtp = _CItpSccpCrFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 18),
    _CItpSccpCrFromMtp_Type()
)
cItpSccpCrFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpCrFromMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpCrFromMtp.setUnits("packets")
_CItpSccpCrefFromMtp_Type = Counter32
_CItpSccpCrefFromMtp_Object = MibScalar
cItpSccpCrefFromMtp = _CItpSccpCrefFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 19),
    _CItpSccpCrefFromMtp_Type()
)
cItpSccpCrefFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpCrefFromMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpCrefFromMtp.setUnits("packets")
_CItpSccpRsrToMtp_Type = Counter32
_CItpSccpRsrToMtp_Object = MibScalar
cItpSccpRsrToMtp = _CItpSccpRsrToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 20),
    _CItpSccpRsrToMtp_Type()
)
cItpSccpRsrToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpRsrToMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpRsrToMtp.setUnits("packets")
_CItpSccpRsrFromMtp_Type = Counter32
_CItpSccpRsrFromMtp_Object = MibScalar
cItpSccpRsrFromMtp = _CItpSccpRsrFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 21),
    _CItpSccpRsrFromMtp_Type()
)
cItpSccpRsrFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpRsrFromMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpRsrFromMtp.setUnits("packets")
_CItpSccpErrToMtp_Type = Counter32
_CItpSccpErrToMtp_Object = MibScalar
cItpSccpErrToMtp = _CItpSccpErrToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 22),
    _CItpSccpErrToMtp_Type()
)
cItpSccpErrToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpErrToMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpErrToMtp.setUnits("packets")
_CItpSccpErrFromMtp_Type = Counter32
_CItpSccpErrFromMtp_Object = MibScalar
cItpSccpErrFromMtp = _CItpSccpErrFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 23),
    _CItpSccpErrFromMtp_Type()
)
cItpSccpErrFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpErrFromMtp.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpErrFromMtp.setUnits("packets")
_CItpSccpCpcConfigLastChanged_Type = TimeStamp
_CItpSccpCpcConfigLastChanged_Object = MibScalar
cItpSccpCpcConfigLastChanged = _CItpSccpCpcConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 24),
    _CItpSccpCpcConfigLastChanged_Type()
)
cItpSccpCpcConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpCpcConfigLastChanged.setStatus("deprecated")
_CItpSccpMapConfigLastChanged_Type = TimeStamp
_CItpSccpMapConfigLastChanged_Object = MibScalar
cItpSccpMapConfigLastChanged = _CItpSccpMapConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 25),
    _CItpSccpMapConfigLastChanged_Type()
)
cItpSccpMapConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpMapConfigLastChanged.setStatus("deprecated")
_CItpSccpSelConfigLastChanged_Type = TimeStamp
_CItpSccpSelConfigLastChanged_Object = MibScalar
cItpSccpSelConfigLastChanged = _CItpSccpSelConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 26),
    _CItpSccpSelConfigLastChanged_Type()
)
cItpSccpSelConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpSelConfigLastChanged.setStatus("deprecated")
_CItpSccpGtaConfigLastChanged_Type = TimeStamp
_CItpSccpGtaConfigLastChanged_Object = MibScalar
cItpSccpGtaConfigLastChanged = _CItpSccpGtaConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 27),
    _CItpSccpGtaConfigLastChanged_Type()
)
cItpSccpGtaConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGtaConfigLastChanged.setStatus("deprecated")
_CItpSccpAppConfigLastChanged_Type = TimeStamp
_CItpSccpAppConfigLastChanged_Object = MibScalar
cItpSccpAppConfigLastChanged = _CItpSccpAppConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 28),
    _CItpSccpAppConfigLastChanged_Type()
)
cItpSccpAppConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpAppConfigLastChanged.setStatus("deprecated")


class _CItpSccpGttMapStateNotifEnabled_Type(TruthValue):
    """Custom type cItpSccpGttMapStateNotifEnabled based on TruthValue"""


_CItpSccpGttMapStateNotifEnabled_Object = MibScalar
cItpSccpGttMapStateNotifEnabled = _CItpSccpGttMapStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 29),
    _CItpSccpGttMapStateNotifEnabled_Type()
)
cItpSccpGttMapStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpSccpGttMapStateNotifEnabled.setStatus("deprecated")
_CItpSccpPrefConfigLastChanged_Type = TimeStamp
_CItpSccpPrefConfigLastChanged_Object = MibScalar
cItpSccpPrefConfigLastChanged = _CItpSccpPrefConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 30),
    _CItpSccpPrefConfigLastChanged_Type()
)
cItpSccpPrefConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpPrefConfigLastChanged.setStatus("deprecated")
_CItpSccpGttConfigLoad_Type = TimeStamp
_CItpSccpGttConfigLoad_Object = MibScalar
cItpSccpGttConfigLoad = _CItpSccpGttConfigLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 31),
    _CItpSccpGttConfigLoad_Type()
)
cItpSccpGttConfigLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttConfigLoad.setStatus("deprecated")
_CItpSccpGttConfigLoadStatus_Type = CItpTcTableLoadStatus
_CItpSccpGttConfigLoadStatus_Object = MibScalar
cItpSccpGttConfigLoadStatus = _CItpSccpGttConfigLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 1, 32),
    _CItpSccpGttConfigLoadStatus_Type()
)
cItpSccpGttConfigLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttConfigLoadStatus.setStatus("deprecated")
_CItpSccpGttConPc_ObjectIdentity = ObjectIdentity
cItpSccpGttConPc = _CItpSccpGttConPc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 2)
)
_CItpSccpGttConPcTable_Object = MibTable
cItpSccpGttConPcTable = _CItpSccpGttConPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cItpSccpGttConPcTable.setStatus("deprecated")
_CItpSccpGttConPcTableEntry_Object = MibTableRow
cItpSccpGttConPcTableEntry = _CItpSccpGttConPcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 2, 1, 1)
)
cItpSccpGttConPcTableEntry.setIndexNames(
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttConPcListName"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttConPointCode"),
)
if mibBuilder.loadTexts:
    cItpSccpGttConPcTableEntry.setStatus("deprecated")
_CItpSccpGttConPcListName_Type = CItpSccpConPcListName
_CItpSccpGttConPcListName_Object = MibTableColumn
cItpSccpGttConPcListName = _CItpSccpGttConPcListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 2, 1, 1, 1),
    _CItpSccpGttConPcListName_Type()
)
cItpSccpGttConPcListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttConPcListName.setStatus("deprecated")
_CItpSccpGttConPointCode_Type = CItpTcPointCode
_CItpSccpGttConPointCode_Object = MibTableColumn
cItpSccpGttConPointCode = _CItpSccpGttConPointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 2, 1, 1, 2),
    _CItpSccpGttConPointCode_Type()
)
cItpSccpGttConPointCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttConPointCode.setStatus("deprecated")


class _CItpSccpGttConPcRefCount_Type(Unsigned32):
    """Custom type cItpSccpGttConPcRefCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CItpSccpGttConPcRefCount_Type.__name__ = "Unsigned32"
_CItpSccpGttConPcRefCount_Object = MibTableColumn
cItpSccpGttConPcRefCount = _CItpSccpGttConPcRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 2, 1, 1, 3),
    _CItpSccpGttConPcRefCount_Type()
)
cItpSccpGttConPcRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttConPcRefCount.setStatus("deprecated")
_CItpSccpGttMap_ObjectIdentity = ObjectIdentity
cItpSccpGttMap = _CItpSccpGttMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3)
)
_CItpSccpGttMapTable_Object = MibTable
cItpSccpGttMapTable = _CItpSccpGttMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cItpSccpGttMapTable.setStatus("deprecated")
_CItpSccpGttMapTableEntry_Object = MibTableRow
cItpSccpGttMapTableEntry = _CItpSccpGttMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1)
)
cItpSccpGttMapTableEntry.setIndexNames(
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttMapPc"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttMapSsn"),
)
if mibBuilder.loadTexts:
    cItpSccpGttMapTableEntry.setStatus("deprecated")
_CItpSccpGttMapPc_Type = CItpTcPointCode
_CItpSccpGttMapPc_Object = MibTableColumn
cItpSccpGttMapPc = _CItpSccpGttMapPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 1),
    _CItpSccpGttMapPc_Type()
)
cItpSccpGttMapPc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttMapPc.setStatus("deprecated")
_CItpSccpGttMapSsn_Type = CItpTcSubSystemNumber
_CItpSccpGttMapSsn_Object = MibTableColumn
cItpSccpGttMapSsn = _CItpSccpGttMapSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 2),
    _CItpSccpGttMapSsn_Type()
)
cItpSccpGttMapSsn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttMapSsn.setStatus("deprecated")
_CItpSccpGttMapDisplayPC_Type = CItpTcDisplayPC
_CItpSccpGttMapDisplayPC_Object = MibTableColumn
cItpSccpGttMapDisplayPC = _CItpSccpGttMapDisplayPC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 3),
    _CItpSccpGttMapDisplayPC_Type()
)
cItpSccpGttMapDisplayPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapDisplayPC.setStatus("deprecated")
_CItpSccpGttMapDisplaySS_Type = CItpSccpGttDisplaySS
_CItpSccpGttMapDisplaySS_Object = MibTableColumn
cItpSccpGttMapDisplaySS = _CItpSccpGttMapDisplaySS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 4),
    _CItpSccpGttMapDisplaySS_Type()
)
cItpSccpGttMapDisplaySS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapDisplaySS.setStatus("deprecated")
_CItpSccpGttMapType_Type = CItpSccpGttMapType
_CItpSccpGttMapType_Object = MibTableColumn
cItpSccpGttMapType = _CItpSccpGttMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 5),
    _CItpSccpGttMapType_Type()
)
cItpSccpGttMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapType.setStatus("deprecated")
_CItpSccpGttMapPcStatus_Type = CItpSccpGttMapPcStatus
_CItpSccpGttMapPcStatus_Object = MibTableColumn
cItpSccpGttMapPcStatus = _CItpSccpGttMapPcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 6),
    _CItpSccpGttMapPcStatus_Type()
)
cItpSccpGttMapPcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapPcStatus.setStatus("deprecated")
_CItpSccpGttMapSsStatus_Type = CItpSccpGttMapSsStatus
_CItpSccpGttMapSsStatus_Object = MibTableColumn
cItpSccpGttMapSsStatus = _CItpSccpGttMapSsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 7),
    _CItpSccpGttMapSsStatus_Type()
)
cItpSccpGttMapSsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapSsStatus.setStatus("deprecated")
_CItpSccpGttMapMultInd_Type = CItpSccpGttMultInd
_CItpSccpGttMapMultInd_Object = MibTableColumn
cItpSccpGttMapMultInd = _CItpSccpGttMapMultInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 8),
    _CItpSccpGttMapMultInd_Type()
)
cItpSccpGttMapMultInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapMultInd.setStatus("deprecated")
_CItpSccpGttMapBackupPc_Type = CItpTcPointCode
_CItpSccpGttMapBackupPc_Object = MibTableColumn
cItpSccpGttMapBackupPc = _CItpSccpGttMapBackupPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 9),
    _CItpSccpGttMapBackupPc_Type()
)
cItpSccpGttMapBackupPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapBackupPc.setStatus("deprecated")
_CItpSccpGttMapBackupSsn_Type = CItpTcSubSystemNumber
_CItpSccpGttMapBackupSsn_Object = MibTableColumn
cItpSccpGttMapBackupSsn = _CItpSccpGttMapBackupSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 10),
    _CItpSccpGttMapBackupSsn_Type()
)
cItpSccpGttMapBackupSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapBackupSsn.setStatus("deprecated")
_CItpSccpGttMapConPcList_Type = CItpSccpConPcListName
_CItpSccpGttMapConPcList_Object = MibTableColumn
cItpSccpGttMapConPcList = _CItpSccpGttMapConPcList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 11),
    _CItpSccpGttMapConPcList_Type()
)
cItpSccpGttMapConPcList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapConPcList.setStatus("deprecated")
_CItpSccpGttMapReRouteOnCong_Type = TruthValue
_CItpSccpGttMapReRouteOnCong_Object = MibTableColumn
cItpSccpGttMapReRouteOnCong = _CItpSccpGttMapReRouteOnCong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 12),
    _CItpSccpGttMapReRouteOnCong_Type()
)
cItpSccpGttMapReRouteOnCong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapReRouteOnCong.setStatus("deprecated")
_CItpSccpGttMapAdjacent_Type = TruthValue
_CItpSccpGttMapAdjacent_Object = MibTableColumn
cItpSccpGttMapAdjacent = _CItpSccpGttMapAdjacent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 13),
    _CItpSccpGttMapAdjacent_Type()
)
cItpSccpGttMapAdjacent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapAdjacent.setStatus("deprecated")
_CItpSccpGttMapLastSsUsed_Type = TruthValue
_CItpSccpGttMapLastSsUsed_Object = MibTableColumn
cItpSccpGttMapLastSsUsed = _CItpSccpGttMapLastSsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 14),
    _CItpSccpGttMapLastSsUsed_Type()
)
cItpSccpGttMapLastSsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapLastSsUsed.setStatus("deprecated")
_CItpSccpGttMapUsed_Type = Counter32
_CItpSccpGttMapUsed_Object = MibTableColumn
cItpSccpGttMapUsed = _CItpSccpGttMapUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 15),
    _CItpSccpGttMapUsed_Type()
)
cItpSccpGttMapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapUsed.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapUsed.setUnits("messages")
_CItpSccpGttMapAltUsed_Type = Counter32
_CItpSccpGttMapAltUsed_Object = MibTableColumn
cItpSccpGttMapAltUsed = _CItpSccpGttMapAltUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 16),
    _CItpSccpGttMapAltUsed_Type()
)
cItpSccpGttMapAltUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapAltUsed.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapAltUsed.setUnits("messages")
_CItpSccpGttMapSccpUnavail_Type = Counter32
_CItpSccpGttMapSccpUnavail_Object = MibTableColumn
cItpSccpGttMapSccpUnavail = _CItpSccpGttMapSccpUnavail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 17),
    _CItpSccpGttMapSccpUnavail_Type()
)
cItpSccpGttMapSccpUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapSccpUnavail.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapSccpUnavail.setUnits("occurrences")
_CItpSccpGttMapPcUnavail_Type = Counter32
_CItpSccpGttMapPcUnavail_Object = MibTableColumn
cItpSccpGttMapPcUnavail = _CItpSccpGttMapPcUnavail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 18),
    _CItpSccpGttMapPcUnavail_Type()
)
cItpSccpGttMapPcUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapPcUnavail.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapPcUnavail.setUnits("occurrences")
_CItpSccpGttMapSsUnavail_Type = Counter32
_CItpSccpGttMapSsUnavail_Object = MibTableColumn
cItpSccpGttMapSsUnavail = _CItpSccpGttMapSsUnavail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 19),
    _CItpSccpGttMapSsUnavail_Type()
)
cItpSccpGttMapSsUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapSsUnavail.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapSsUnavail.setUnits("occurrences")
_CItpSccpGttMapPcCongested_Type = Counter32
_CItpSccpGttMapPcCongested_Object = MibTableColumn
cItpSccpGttMapPcCongested = _CItpSccpGttMapPcCongested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 20),
    _CItpSccpGttMapPcCongested_Type()
)
cItpSccpGttMapPcCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapPcCongested.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapPcCongested.setUnits("occurrences")
_CItpSccpGttMapSsCongested_Type = Counter32
_CItpSccpGttMapSsCongested_Object = MibTableColumn
cItpSccpGttMapSsCongested = _CItpSccpGttMapSsCongested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 21),
    _CItpSccpGttMapSsCongested_Type()
)
cItpSccpGttMapSsCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapSsCongested.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapSsCongested.setUnits("occurrences")
_CItpSccpGttMapMtp3Fail_Type = Counter32
_CItpSccpGttMapMtp3Fail_Object = MibTableColumn
cItpSccpGttMapMtp3Fail = _CItpSccpGttMapMtp3Fail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 22),
    _CItpSccpGttMapMtp3Fail_Type()
)
cItpSccpGttMapMtp3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapMtp3Fail.setStatus("deprecated")
if mibBuilder.loadTexts:
    cItpSccpGttMapMtp3Fail.setUnits("occurrences")


class _CItpSccpGttMapRefCount_Type(Unsigned32):
    """Custom type cItpSccpGttMapRefCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CItpSccpGttMapRefCount_Type.__name__ = "Unsigned32"
_CItpSccpGttMapRefCount_Object = MibTableColumn
cItpSccpGttMapRefCount = _CItpSccpGttMapRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 23),
    _CItpSccpGttMapRefCount_Type()
)
cItpSccpGttMapRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapRefCount.setStatus("deprecated")
_CItpSccpGttMapCongStatus_Type = CItpSccpGttMapCongStatus
_CItpSccpGttMapCongStatus_Object = MibTableColumn
cItpSccpGttMapCongStatus = _CItpSccpGttMapCongStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 3, 1, 1, 24),
    _CItpSccpGttMapCongStatus_Type()
)
cItpSccpGttMapCongStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttMapCongStatus.setStatus("deprecated")
_CItpSccpGttSel_ObjectIdentity = ObjectIdentity
cItpSccpGttSel = _CItpSccpGttSel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4)
)
_CItpSccpGttSelTable_Object = MibTable
cItpSccpGttSelTable = _CItpSccpGttSelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cItpSccpGttSelTable.setStatus("deprecated")
_CItpSccpGttSelTableEntry_Object = MibTableRow
cItpSccpGttSelTableEntry = _CItpSccpGttSelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1)
)
cItpSccpGttSelTableEntry.setIndexNames(
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttSelTT"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttSelNAI"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttSelNP"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttSelGTI"),
)
if mibBuilder.loadTexts:
    cItpSccpGttSelTableEntry.setStatus("deprecated")
_CItpSccpGttSelTT_Type = CItpSccpGttTransType
_CItpSccpGttSelTT_Object = MibTableColumn
cItpSccpGttSelTT = _CItpSccpGttSelTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 1),
    _CItpSccpGttSelTT_Type()
)
cItpSccpGttSelTT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttSelTT.setStatus("deprecated")
_CItpSccpGttSelNAI_Type = CItpTcNAI
_CItpSccpGttSelNAI_Object = MibTableColumn
cItpSccpGttSelNAI = _CItpSccpGttSelNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 2),
    _CItpSccpGttSelNAI_Type()
)
cItpSccpGttSelNAI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttSelNAI.setStatus("deprecated")
_CItpSccpGttSelNP_Type = CItpTcNumberingPlan
_CItpSccpGttSelNP_Object = MibTableColumn
cItpSccpGttSelNP = _CItpSccpGttSelNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 3),
    _CItpSccpGttSelNP_Type()
)
cItpSccpGttSelNP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttSelNP.setStatus("deprecated")
_CItpSccpGttSelGTI_Type = CItpSccpGttGlobalTitleInd
_CItpSccpGttSelGTI_Object = MibTableColumn
cItpSccpGttSelGTI = _CItpSccpGttSelGTI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 4),
    _CItpSccpGttSelGTI_Type()
)
cItpSccpGttSelGTI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttSelGTI.setStatus("deprecated")
_CItpSccpGttSelName_Type = CItpSccpGttSelName
_CItpSccpGttSelName_Object = MibTableColumn
cItpSccpGttSelName = _CItpSccpGttSelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 5),
    _CItpSccpGttSelName_Type()
)
cItpSccpGttSelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttSelName.setStatus("deprecated")
_CItpSccpGttSelNumPerf_Type = Counter32
_CItpSccpGttSelNumPerf_Object = MibTableColumn
cItpSccpGttSelNumPerf = _CItpSccpGttSelNumPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 6),
    _CItpSccpGttSelNumPerf_Type()
)
cItpSccpGttSelNumPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttSelNumPerf.setStatus("deprecated")
_CItpSccpGttSelNotFound_Type = Counter32
_CItpSccpGttSelNotFound_Object = MibTableColumn
cItpSccpGttSelNotFound = _CItpSccpGttSelNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 7),
    _CItpSccpGttSelNotFound_Type()
)
cItpSccpGttSelNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttSelNotFound.setStatus("deprecated")
_CItpSccpGttSelQOS_Type = CItpSccpGttQOS
_CItpSccpGttSelQOS_Object = MibTableColumn
cItpSccpGttSelQOS = _CItpSccpGttSelQOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 8),
    _CItpSccpGttSelQOS_Type()
)
cItpSccpGttSelQOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttSelQOS.setStatus("deprecated")


class _CItpSccpGttSelRefCount_Type(Unsigned32):
    """Custom type cItpSccpGttSelRefCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CItpSccpGttSelRefCount_Type.__name__ = "Unsigned32"
_CItpSccpGttSelRefCount_Object = MibTableColumn
cItpSccpGttSelRefCount = _CItpSccpGttSelRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 9),
    _CItpSccpGttSelRefCount_Type()
)
cItpSccpGttSelRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttSelRefCount.setStatus("deprecated")
_CItpSccpGttPrePrefConv_Type = CItpSccpGttPrefName
_CItpSccpGttPrePrefConv_Object = MibTableColumn
cItpSccpGttPrePrefConv = _CItpSccpGttPrePrefConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 10),
    _CItpSccpGttPrePrefConv_Type()
)
cItpSccpGttPrePrefConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttPrePrefConv.setStatus("deprecated")
_CItpSccpGttPostPrefConv_Type = CItpSccpGttPrefName
_CItpSccpGttPostPrefConv_Object = MibTableColumn
cItpSccpGttPostPrefConv = _CItpSccpGttPostPrefConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 4, 1, 1, 11),
    _CItpSccpGttPostPrefConv_Type()
)
cItpSccpGttPostPrefConv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttPostPrefConv.setStatus("deprecated")
_CItpSccpGttGta_ObjectIdentity = ObjectIdentity
cItpSccpGttGta = _CItpSccpGttGta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5)
)
_CItpSccpGttGtaTable_Object = MibTable
cItpSccpGttGtaTable = _CItpSccpGttGtaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cItpSccpGttGtaTable.setStatus("deprecated")
_CItpSccpGttGtaTableEntry_Object = MibTableRow
cItpSccpGttGtaTableEntry = _CItpSccpGttGtaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1)
)
cItpSccpGttGtaTableEntry.setIndexNames(
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaTT"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaNAI"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaNP"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaGTI"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAddr"),
)
if mibBuilder.loadTexts:
    cItpSccpGttGtaTableEntry.setStatus("deprecated")
_CItpSccpGttGtaTT_Type = CItpSccpGttTransType
_CItpSccpGttGtaTT_Object = MibTableColumn
cItpSccpGttGtaTT = _CItpSccpGttGtaTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 1),
    _CItpSccpGttGtaTT_Type()
)
cItpSccpGttGtaTT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttGtaTT.setStatus("deprecated")
_CItpSccpGttGtaNAI_Type = CItpTcNAI
_CItpSccpGttGtaNAI_Object = MibTableColumn
cItpSccpGttGtaNAI = _CItpSccpGttGtaNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 2),
    _CItpSccpGttGtaNAI_Type()
)
cItpSccpGttGtaNAI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttGtaNAI.setStatus("deprecated")
_CItpSccpGttGtaNP_Type = CItpTcNumberingPlan
_CItpSccpGttGtaNP_Object = MibTableColumn
cItpSccpGttGtaNP = _CItpSccpGttGtaNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 3),
    _CItpSccpGttGtaNP_Type()
)
cItpSccpGttGtaNP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttGtaNP.setStatus("deprecated")
_CItpSccpGttGtaGTI_Type = CItpSccpGttGlobalTitleInd
_CItpSccpGttGtaGTI_Object = MibTableColumn
cItpSccpGttGtaGTI = _CItpSccpGttGtaGTI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 4),
    _CItpSccpGttGtaGTI_Type()
)
cItpSccpGttGtaGTI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttGtaGTI.setStatus("deprecated")
_CItpSccpGttGtaAddr_Type = CItpTcGtaAddr
_CItpSccpGttGtaAddr_Object = MibTableColumn
cItpSccpGttGtaAddr = _CItpSccpGttGtaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 5),
    _CItpSccpGttGtaAddr_Type()
)
cItpSccpGttGtaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttGtaAddr.setStatus("deprecated")
_CItpSccpGttGtaAddrDisp_Type = CItpTcGtaDisplay
_CItpSccpGttGtaAddrDisp_Object = MibTableColumn
cItpSccpGttGtaAddrDisp = _CItpSccpGttGtaAddrDisp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 6),
    _CItpSccpGttGtaAddrDisp_Type()
)
cItpSccpGttGtaAddrDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaAddrDisp.setStatus("deprecated")
_CItpSccpGttGtaAddrLen_Type = CItpSccpGttGtaAddrLen
_CItpSccpGttGtaAddrLen_Object = MibTableColumn
cItpSccpGttGtaAddrLen = _CItpSccpGttGtaAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 7),
    _CItpSccpGttGtaAddrLen_Type()
)
cItpSccpGttGtaAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaAddrLen.setStatus("deprecated")
_CItpSccpGttGtaSelName_Type = CItpSccpGttSelName
_CItpSccpGttGtaSelName_Object = MibTableColumn
cItpSccpGttGtaSelName = _CItpSccpGttGtaSelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 8),
    _CItpSccpGttGtaSelName_Type()
)
cItpSccpGttGtaSelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaSelName.setStatus("deprecated")
_CItpSccpGttGtaResType_Type = CItpSccpGttGtaResType
_CItpSccpGttGtaResType_Object = MibTableColumn
cItpSccpGttGtaResType = _CItpSccpGttGtaResType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 9),
    _CItpSccpGttGtaResType_Type()
)
cItpSccpGttGtaResType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaResType.setStatus("deprecated")
_CItpSccpGttGtaResPc_Type = CItpTcPointCode
_CItpSccpGttGtaResPc_Object = MibTableColumn
cItpSccpGttGtaResPc = _CItpSccpGttGtaResPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 10),
    _CItpSccpGttGtaResPc_Type()
)
cItpSccpGttGtaResPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaResPc.setStatus("deprecated")
_CItpSccpGttGtaResMap_Type = CItpTcPointCode
_CItpSccpGttGtaResMap_Object = MibTableColumn
cItpSccpGttGtaResMap = _CItpSccpGttGtaResMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 11),
    _CItpSccpGttGtaResMap_Type()
)
cItpSccpGttGtaResMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaResMap.setStatus("deprecated")
_CItpSccpGttGtaResAppGroup_Type = CItpSccpGttAppName
_CItpSccpGttGtaResAppGroup_Object = MibTableColumn
cItpSccpGttGtaResAppGroup = _CItpSccpGttGtaResAppGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 12),
    _CItpSccpGttGtaResAppGroup_Type()
)
cItpSccpGttGtaResAppGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaResAppGroup.setStatus("deprecated")
_CItpSccpGttGtaTTorSSN_Type = CItpTcTranslationType
_CItpSccpGttGtaTTorSSN_Object = MibTableColumn
cItpSccpGttGtaTTorSSN = _CItpSccpGttGtaTTorSSN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 13),
    _CItpSccpGttGtaTTorSSN_Type()
)
cItpSccpGttGtaTTorSSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaTTorSSN.setStatus("deprecated")
_CItpSccpGttGtaRoutingInd_Type = CItpSccpGttRoutingInd
_CItpSccpGttGtaRoutingInd_Object = MibTableColumn
cItpSccpGttGtaRoutingInd = _CItpSccpGttGtaRoutingInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 14),
    _CItpSccpGttGtaRoutingInd_Type()
)
cItpSccpGttGtaRoutingInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaRoutingInd.setStatus("deprecated")
_CItpSccpGttGtaQOS_Type = CItpSccpGttQOS
_CItpSccpGttGtaQOS_Object = MibTableColumn
cItpSccpGttGtaQOS = _CItpSccpGttGtaQOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 15),
    _CItpSccpGttGtaQOS_Type()
)
cItpSccpGttGtaQOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaQOS.setStatus("deprecated")
_CItpSccpGttGtaAddrDispZB_Type = CItpTcGtaDisplayZB
_CItpSccpGttGtaAddrDispZB_Object = MibTableColumn
cItpSccpGttGtaAddrDispZB = _CItpSccpGttGtaAddrDispZB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 16),
    _CItpSccpGttGtaAddrDispZB_Type()
)
cItpSccpGttGtaAddrDispZB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaAddrDispZB.setStatus("deprecated")
_CItpSccpGttGtaAddrLenZB_Type = CItpSccpGttGtaAddrLenZB
_CItpSccpGttGtaAddrLenZB_Object = MibTableColumn
cItpSccpGttGtaAddrLenZB = _CItpSccpGttGtaAddrLenZB_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 17),
    _CItpSccpGttGtaAddrLenZB_Type()
)
cItpSccpGttGtaAddrLenZB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaAddrLenZB.setStatus("deprecated")
_CItpSccpGttGtaAsName_Type = CItpTcXuaName
_CItpSccpGttGtaAsName_Object = MibTableColumn
cItpSccpGttGtaAsName = _CItpSccpGttGtaAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 18),
    _CItpSccpGttGtaAsName_Type()
)
cItpSccpGttGtaAsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaAsName.setStatus("deprecated")


class _CItpSccpGttGtaTTorSSNvalue_Type(Unsigned32):
    """Custom type cItpSccpGttGtaTTorSSNvalue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CItpSccpGttGtaTTorSSNvalue_Type.__name__ = "Unsigned32"
_CItpSccpGttGtaTTorSSNvalue_Object = MibTableColumn
cItpSccpGttGtaTTorSSNvalue = _CItpSccpGttGtaTTorSSNvalue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 5, 1, 1, 19),
    _CItpSccpGttGtaTTorSSNvalue_Type()
)
cItpSccpGttGtaTTorSSNvalue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttGtaTTorSSNvalue.setStatus("deprecated")
_CItpSccpGttApp_ObjectIdentity = ObjectIdentity
cItpSccpGttApp = _CItpSccpGttApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6)
)
_CItpSccpGttAppTable_Object = MibTable
cItpSccpGttAppTable = _CItpSccpGttAppTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cItpSccpGttAppTable.setStatus("deprecated")
_CItpSccpGttAppTableEntry_Object = MibTableRow
cItpSccpGttAppTableEntry = _CItpSccpGttAppTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1)
)
cItpSccpGttAppTableEntry.setIndexNames(
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttAppName"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttAppCost"),
)
if mibBuilder.loadTexts:
    cItpSccpGttAppTableEntry.setStatus("deprecated")
_CItpSccpGttAppName_Type = CItpSccpGttAppName
_CItpSccpGttAppName_Object = MibTableColumn
cItpSccpGttAppName = _CItpSccpGttAppName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 1),
    _CItpSccpGttAppName_Type()
)
cItpSccpGttAppName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttAppName.setStatus("deprecated")
_CItpSccpGttAppCost_Type = CItpSccpGttAppCost
_CItpSccpGttAppCost_Object = MibTableColumn
cItpSccpGttAppCost = _CItpSccpGttAppCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 2),
    _CItpSccpGttAppCost_Type()
)
cItpSccpGttAppCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttAppCost.setStatus("deprecated")
_CItpSccpGttAppType_Type = CItpSccpGttAppType
_CItpSccpGttAppType_Object = MibTableColumn
cItpSccpGttAppType = _CItpSccpGttAppType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 3),
    _CItpSccpGttAppType_Type()
)
cItpSccpGttAppType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppType.setStatus("deprecated")
_CItpSccpGttAppPc_Type = CItpTcPointCode
_CItpSccpGttAppPc_Object = MibTableColumn
cItpSccpGttAppPc = _CItpSccpGttAppPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 4),
    _CItpSccpGttAppPc_Type()
)
cItpSccpGttAppPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppPc.setStatus("deprecated")
_CItpSccpGttAppSsn_Type = CItpTcSubSystemNumber
_CItpSccpGttAppSsn_Object = MibTableColumn
cItpSccpGttAppSsn = _CItpSccpGttAppSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 5),
    _CItpSccpGttAppSsn_Type()
)
cItpSccpGttAppSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppSsn.setStatus("deprecated")
_CItpSccpGttAppRi_Type = CItpSccpGttRoutingInd
_CItpSccpGttAppRi_Object = MibTableColumn
cItpSccpGttAppRi = _CItpSccpGttAppRi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 6),
    _CItpSccpGttAppRi_Type()
)
cItpSccpGttAppRi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppRi.setStatus("deprecated")
_CItpSccpGttAppMult_Type = CItpSccpGttMultInd
_CItpSccpGttAppMult_Object = MibTableColumn
cItpSccpGttAppMult = _CItpSccpGttAppMult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 7),
    _CItpSccpGttAppMult_Type()
)
cItpSccpGttAppMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppMult.setStatus("deprecated")


class _CItpSccpGttAppRefCount_Type(Unsigned32):
    """Custom type cItpSccpGttAppRefCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CItpSccpGttAppRefCount_Type.__name__ = "Unsigned32"
_CItpSccpGttAppRefCount_Object = MibTableColumn
cItpSccpGttAppRefCount = _CItpSccpGttAppRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 6, 1, 1, 8),
    _CItpSccpGttAppRefCount_Type()
)
cItpSccpGttAppRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppRefCount.setStatus("deprecated")
_CItpSccpGttAppGr_ObjectIdentity = ObjectIdentity
cItpSccpGttAppGr = _CItpSccpGttAppGr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7)
)
_CItpSccpGttAppGrTable_Object = MibTable
cItpSccpGttAppGrTable = _CItpSccpGttAppGrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cItpSccpGttAppGrTable.setStatus("deprecated")
_CItpSccpGttAppGrTableEntry_Object = MibTableRow
cItpSccpGttAppGrTableEntry = _CItpSccpGttAppGrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1)
)
cItpSccpGttAppGrTableEntry.setIndexNames(
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrName"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrCost"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrEntNum"),
)
if mibBuilder.loadTexts:
    cItpSccpGttAppGrTableEntry.setStatus("deprecated")
_CItpSccpGttAppGrName_Type = CItpSccpGttAppName
_CItpSccpGttAppGrName_Object = MibTableColumn
cItpSccpGttAppGrName = _CItpSccpGttAppGrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 1),
    _CItpSccpGttAppGrName_Type()
)
cItpSccpGttAppGrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrName.setStatus("deprecated")
_CItpSccpGttAppGrCost_Type = CItpSccpGttAppCost
_CItpSccpGttAppGrCost_Object = MibTableColumn
cItpSccpGttAppGrCost = _CItpSccpGttAppGrCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 2),
    _CItpSccpGttAppGrCost_Type()
)
cItpSccpGttAppGrCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrCost.setStatus("deprecated")


class _CItpSccpGttAppGrEntNum_Type(Unsigned32):
    """Custom type cItpSccpGttAppGrEntNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpSccpGttAppGrEntNum_Type.__name__ = "Unsigned32"
_CItpSccpGttAppGrEntNum_Object = MibTableColumn
cItpSccpGttAppGrEntNum = _CItpSccpGttAppGrEntNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 3),
    _CItpSccpGttAppGrEntNum_Type()
)
cItpSccpGttAppGrEntNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrEntNum.setStatus("deprecated")
_CItpSccpGttAppGrType_Type = CItpSccpGttAppType
_CItpSccpGttAppGrType_Object = MibTableColumn
cItpSccpGttAppGrType = _CItpSccpGttAppGrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 4),
    _CItpSccpGttAppGrType_Type()
)
cItpSccpGttAppGrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrType.setStatus("deprecated")
_CItpSccpGttAppGrPc_Type = CItpTcPointCode
_CItpSccpGttAppGrPc_Object = MibTableColumn
cItpSccpGttAppGrPc = _CItpSccpGttAppGrPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 5),
    _CItpSccpGttAppGrPc_Type()
)
cItpSccpGttAppGrPc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrPc.setStatus("deprecated")
_CItpSccpGttAppGrSsn_Type = CItpTcSubSystemNumber
_CItpSccpGttAppGrSsn_Object = MibTableColumn
cItpSccpGttAppGrSsn = _CItpSccpGttAppGrSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 6),
    _CItpSccpGttAppGrSsn_Type()
)
cItpSccpGttAppGrSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrSsn.setStatus("deprecated")
_CItpSccpGttAppGrRi_Type = CItpSccpGttRoutingInd
_CItpSccpGttAppGrRi_Object = MibTableColumn
cItpSccpGttAppGrRi = _CItpSccpGttAppGrRi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 7),
    _CItpSccpGttAppGrRi_Type()
)
cItpSccpGttAppGrRi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrRi.setStatus("deprecated")
_CItpSccpGttAppGrMult_Type = CItpSccpGttMultInd
_CItpSccpGttAppGrMult_Object = MibTableColumn
cItpSccpGttAppGrMult = _CItpSccpGttAppGrMult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 8),
    _CItpSccpGttAppGrMult_Type()
)
cItpSccpGttAppGrMult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrMult.setStatus("deprecated")


class _CItpSccpGttAppGrRefCount_Type(Unsigned32):
    """Custom type cItpSccpGttAppGrRefCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CItpSccpGttAppGrRefCount_Type.__name__ = "Unsigned32"
_CItpSccpGttAppGrRefCount_Object = MibTableColumn
cItpSccpGttAppGrRefCount = _CItpSccpGttAppGrRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 9),
    _CItpSccpGttAppGrRefCount_Type()
)
cItpSccpGttAppGrRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrRefCount.setStatus("deprecated")
_CItpSccpGttAppGrAsName_Type = CItpTcXuaName
_CItpSccpGttAppGrAsName_Object = MibTableColumn
cItpSccpGttAppGrAsName = _CItpSccpGttAppGrAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 10),
    _CItpSccpGttAppGrAsName_Type()
)
cItpSccpGttAppGrAsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrAsName.setStatus("deprecated")
_CItpSccpGttAppGrNewSsn_Type = CItpTcSubSystemNumber
_CItpSccpGttAppGrNewSsn_Object = MibTableColumn
cItpSccpGttAppGrNewSsn = _CItpSccpGttAppGrNewSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 11),
    _CItpSccpGttAppGrNewSsn_Type()
)
cItpSccpGttAppGrNewSsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrNewSsn.setStatus("deprecated")
_CItpSccpGttAppGrNumUsed_Type = Counter32
_CItpSccpGttAppGrNumUsed_Object = MibTableColumn
cItpSccpGttAppGrNumUsed = _CItpSccpGttAppGrNumUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 7, 1, 1, 12),
    _CItpSccpGttAppGrNumUsed_Type()
)
cItpSccpGttAppGrNumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttAppGrNumUsed.setStatus("deprecated")
_CItpSccpGttPref_ObjectIdentity = ObjectIdentity
cItpSccpGttPref = _CItpSccpGttPref_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8)
)
_CItpSccpGttPrefTable_Object = MibTable
cItpSccpGttPrefTable = _CItpSccpGttPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cItpSccpGttPrefTable.setStatus("deprecated")
_CItpSccpGttPrefTableEntry_Object = MibTableRow
cItpSccpGttPrefTableEntry = _CItpSccpGttPrefTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1)
)
cItpSccpGttPrefTableEntry.setIndexNames(
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttPrefName"),
    (0, "CISCO-ITP-SCCP-MIB", "cItpSccpGttPrefInAddr"),
)
if mibBuilder.loadTexts:
    cItpSccpGttPrefTableEntry.setStatus("deprecated")
_CItpSccpGttPrefName_Type = CItpSccpGttPrefName
_CItpSccpGttPrefName_Object = MibTableColumn
cItpSccpGttPrefName = _CItpSccpGttPrefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1, 1),
    _CItpSccpGttPrefName_Type()
)
cItpSccpGttPrefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttPrefName.setStatus("deprecated")
_CItpSccpGttPrefInAddr_Type = CItpTcGtaAddr
_CItpSccpGttPrefInAddr_Object = MibTableColumn
cItpSccpGttPrefInAddr = _CItpSccpGttPrefInAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1, 2),
    _CItpSccpGttPrefInAddr_Type()
)
cItpSccpGttPrefInAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpSccpGttPrefInAddr.setStatus("deprecated")
_CItpSccpGttPrefOutAddr_Type = CItpTcGtaAddr
_CItpSccpGttPrefOutAddr_Object = MibTableColumn
cItpSccpGttPrefOutAddr = _CItpSccpGttPrefOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1, 3),
    _CItpSccpGttPrefOutAddr_Type()
)
cItpSccpGttPrefOutAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttPrefOutAddr.setStatus("deprecated")
_CItpSccpGttPrefTblNAI_Type = CItpTcNAI
_CItpSccpGttPrefTblNAI_Object = MibTableColumn
cItpSccpGttPrefTblNAI = _CItpSccpGttPrefTblNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1, 4),
    _CItpSccpGttPrefTblNAI_Type()
)
cItpSccpGttPrefTblNAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttPrefTblNAI.setStatus("deprecated")
_CItpSccpGttPrefTblNP_Type = CItpTcNumberingPlan
_CItpSccpGttPrefTblNP_Object = MibTableColumn
cItpSccpGttPrefTblNP = _CItpSccpGttPrefTblNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1, 5),
    _CItpSccpGttPrefTblNP_Type()
)
cItpSccpGttPrefTblNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttPrefTblNP.setStatus("deprecated")
_CItpSccpGttPrefItemNAI_Type = CItpTcNAI
_CItpSccpGttPrefItemNAI_Object = MibTableColumn
cItpSccpGttPrefItemNAI = _CItpSccpGttPrefItemNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1, 6),
    _CItpSccpGttPrefItemNAI_Type()
)
cItpSccpGttPrefItemNAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttPrefItemNAI.setStatus("deprecated")
_CItpSccpGttPrefItemNP_Type = CItpTcNumberingPlan
_CItpSccpGttPrefItemNP_Object = MibTableColumn
cItpSccpGttPrefItemNP = _CItpSccpGttPrefItemNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 1, 8, 1, 1, 7),
    _CItpSccpGttPrefItemNP_Type()
)
cItpSccpGttPrefItemNP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpSccpGttPrefItemNP.setStatus("deprecated")
_CItpSccpConformance_ObjectIdentity = ObjectIdentity
cItpSccpConformance = _CItpSccpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2)
)
_CItpSccpMIBCompliances_ObjectIdentity = ObjectIdentity
cItpSccpMIBCompliances = _CItpSccpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 1)
)
_CItpSccpMIBGroups_ObjectIdentity = ObjectIdentity
cItpSccpMIBGroups = _CItpSccpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2)
)

# Managed Objects groups

cItpSccpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 1)
)
cItpSccpScalarsGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpTotalMsgs"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpLocalMsgs"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpTotalGttMsgs"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpUDTMsgsSent"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpUDTSMsgsSent"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpUDTMsgsRcvd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpUDTSMsgsRcvd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpXUDTMsgsSent"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpXUDTSMsgsSent"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpXUDTMsgsRcvd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpXUDTSMsgsRcvd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpLUDTMsgsSent"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpLUDTSMsgsSent"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpLUDTMsgsRcvd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpLUDTSMsgsRcvd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpCrToMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpCrefToMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpCrFromMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpCrefFromMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpRsrToMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpRsrFromMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpErrToMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpErrFromMtp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpCpcConfigLastChanged"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpMapConfigLastChanged"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpSelConfigLastChanged"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGtaConfigLastChanged"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpAppConfigLastChanged"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapStateNotifEnabled"))
)
if mibBuilder.loadTexts:
    cItpSccpScalarsGroup.setStatus("deprecated")

cItpSccpGttConPcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 2)
)
cItpSccpGttConPcGroup.setObjects(
    ("CISCO-ITP-SCCP-MIB", "cItpSccpGttConPcRefCount")
)
if mibBuilder.loadTexts:
    cItpSccpGttConPcGroup.setStatus("deprecated")

cItpSccpGttMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 3)
)
cItpSccpGttMapGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapDisplayPC"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapDisplaySS"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapType"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapPcStatus"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapSsStatus"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapMultInd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapBackupPc"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapBackupSsn"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapConPcList"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapReRouteOnCong"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapAdjacent"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapLastSsUsed"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapUsed"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapAltUsed"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapSccpUnavail"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapPcUnavail"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapSsUnavail"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapPcCongested"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapSsCongested"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapMtp3Fail"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapRefCount"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapCongStatus"))
)
if mibBuilder.loadTexts:
    cItpSccpGttMapGroup.setStatus("deprecated")

cItpSccpGttSelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 4)
)
cItpSccpGttSelGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelNumPerf"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelNotFound"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelQOS"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelRefCount"))
)
if mibBuilder.loadTexts:
    cItpSccpGttSelGroup.setStatus("deprecated")

cItpSccpGttGtaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 5)
)
cItpSccpGttGtaGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAddrDisp"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAddrLen"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaSelName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResType"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResPc"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResMap"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResAppGroup"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaTTorSSN"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaRoutingInd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaQOS"))
)
if mibBuilder.loadTexts:
    cItpSccpGttGtaGroup.setStatus("deprecated")

cItpSccpGttAppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 6)
)
cItpSccpGttAppGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppType"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppPc"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppSsn"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppRi"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppMult"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppRefCount"))
)
if mibBuilder.loadTexts:
    cItpSccpGttAppGroup.setStatus("deprecated")

cItpSccpConfigStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 8)
)
cItpSccpConfigStatusGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpPrefConfigLastChanged"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttConfigLoad"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttConfigLoadStatus"))
)
if mibBuilder.loadTexts:
    cItpSccpConfigStatusGroup.setStatus("deprecated")

cItpSccpGttSelGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 9)
)
cItpSccpGttSelGroupRev1.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelNumPerf"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelNotFound"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelQOS"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttSelRefCount"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttPrePrefConv"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttPostPrefConv"))
)
if mibBuilder.loadTexts:
    cItpSccpGttSelGroupRev1.setStatus("deprecated")

cItpSccpGttGtaGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 10)
)
cItpSccpGttGtaGroupRev1.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaSelName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResType"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResPc"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResMap"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResAppGroup"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaTTorSSN"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaRoutingInd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaQOS"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAddrDispZB"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAddrLenZB"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAsName"))
)
if mibBuilder.loadTexts:
    cItpSccpGttGtaGroupRev1.setStatus("deprecated")

cItpSccpGttAppGrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 11)
)
cItpSccpGttAppGrGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrType"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrPc"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrSsn"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrRi"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrMult"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrRefCount"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrAsName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrNewSsn"))
)
if mibBuilder.loadTexts:
    cItpSccpGttAppGrGroup.setStatus("deprecated")

cItpSccpGttPrefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 12)
)
cItpSccpGttPrefGroup.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttPrefOutAddr"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttPrefTblNAI"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttPrefTblNP"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttPrefItemNAI"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttPrefItemNP"))
)
if mibBuilder.loadTexts:
    cItpSccpGttPrefGroup.setStatus("deprecated")

cItpSccpGttGtaGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 13)
)
cItpSccpGttGtaGroupRev2.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaSelName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResType"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResPc"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResMap"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaResAppGroup"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaTTorSSN"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaRoutingInd"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaQOS"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAddrDispZB"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAddrLenZB"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaAsName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttGtaTTorSSNvalue"))
)
if mibBuilder.loadTexts:
    cItpSccpGttGtaGroupRev2.setStatus("deprecated")

cItpSccpGttAppGrGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 14)
)
cItpSccpGttAppGrGroupRev2.setObjects(
      *(("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrType"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrPc"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrSsn"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrRi"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrMult"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrRefCount"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrAsName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrNewSsn"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttAppGrNumUsed"))
)
if mibBuilder.loadTexts:
    cItpSccpGttAppGrGroupRev2.setStatus("deprecated")


# Notification objects

cItpSccpGttMapStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 0, 0, 1)
)
cItpSccpGttMapStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-SP-MIB", "cItpSpDisplayName"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapDisplayPC"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapDisplaySS"),
        ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapSsStatus"))
)
if mibBuilder.loadTexts:
    cItpSccpGttMapStateChange.setStatus(
        "deprecated"
    )


# Notifications groups

cItpSccpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 2, 7)
)
cItpSccpNotificationsGroup.setObjects(
    ("CISCO-ITP-SCCP-MIB", "cItpSccpGttMapStateChange")
)
if mibBuilder.loadTexts:
    cItpSccpNotificationsGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance

cItpSccpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cItpSccpMIBCompliance.setStatus(
        "deprecated"
    )

cItpSccpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cItpSccpMIBComplianceRev1.setStatus(
        "deprecated"
    )

cItpSccpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 233, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cItpSccpMIBComplianceRev2.setStatus(
        "deprecated"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-SCCP-MIB",
    **{"CItpSccpConPcListName": CItpSccpConPcListName,
       "CItpSccpGttSelName": CItpSccpGttSelName,
       "CItpSccpGttAppName": CItpSccpGttAppName,
       "CItpSccpGttPrefName": CItpSccpGttPrefName,
       "CItpSccpGttDisplaySS": CItpSccpGttDisplaySS,
       "CItpSccpGttAppCost": CItpSccpGttAppCost,
       "CItpSccpGttAppType": CItpSccpGttAppType,
       "CItpSccpGttGtaAddrLen": CItpSccpGttGtaAddrLen,
       "CItpSccpGttGtaAddrLenZB": CItpSccpGttGtaAddrLenZB,
       "CItpSccpGttMapType": CItpSccpGttMapType,
       "CItpSccpGttGtaResType": CItpSccpGttGtaResType,
       "CItpSccpGttRoutingInd": CItpSccpGttRoutingInd,
       "CItpSccpGttMapPcStatus": CItpSccpGttMapPcStatus,
       "CItpSccpGttMapSsStatus": CItpSccpGttMapSsStatus,
       "CItpSccpGttMultInd": CItpSccpGttMultInd,
       "CItpSccpGttMapCongStatus": CItpSccpGttMapCongStatus,
       "CItpSccpGttTransType": CItpSccpGttTransType,
       "CItpSccpGttQOS": CItpSccpGttQOS,
       "CItpSccpGttGlobalTitleInd": CItpSccpGttGlobalTitleInd,
       "ciscoItpSccpMIB": ciscoItpSccpMIB,
       "cItpSccpMIBNotifs": cItpSccpMIBNotifs,
       "cItpSccpNotifications": cItpSccpNotifications,
       "cItpSccpGttMapStateChange": cItpSccpGttMapStateChange,
       "cItpSccpMIBObjects": cItpSccpMIBObjects,
       "cItpSccpScalars": cItpSccpScalars,
       "cItpSccpTotalMsgs": cItpSccpTotalMsgs,
       "cItpSccpLocalMsgs": cItpSccpLocalMsgs,
       "cItpSccpTotalGttMsgs": cItpSccpTotalGttMsgs,
       "cItpSccpUDTMsgsSent": cItpSccpUDTMsgsSent,
       "cItpSccpUDTSMsgsSent": cItpSccpUDTSMsgsSent,
       "cItpSccpUDTMsgsRcvd": cItpSccpUDTMsgsRcvd,
       "cItpSccpUDTSMsgsRcvd": cItpSccpUDTSMsgsRcvd,
       "cItpSccpXUDTMsgsSent": cItpSccpXUDTMsgsSent,
       "cItpSccpXUDTSMsgsSent": cItpSccpXUDTSMsgsSent,
       "cItpSccpXUDTMsgsRcvd": cItpSccpXUDTMsgsRcvd,
       "cItpSccpXUDTSMsgsRcvd": cItpSccpXUDTSMsgsRcvd,
       "cItpSccpLUDTMsgsSent": cItpSccpLUDTMsgsSent,
       "cItpSccpLUDTSMsgsSent": cItpSccpLUDTSMsgsSent,
       "cItpSccpLUDTMsgsRcvd": cItpSccpLUDTMsgsRcvd,
       "cItpSccpLUDTSMsgsRcvd": cItpSccpLUDTSMsgsRcvd,
       "cItpSccpCrToMtp": cItpSccpCrToMtp,
       "cItpSccpCrefToMtp": cItpSccpCrefToMtp,
       "cItpSccpCrFromMtp": cItpSccpCrFromMtp,
       "cItpSccpCrefFromMtp": cItpSccpCrefFromMtp,
       "cItpSccpRsrToMtp": cItpSccpRsrToMtp,
       "cItpSccpRsrFromMtp": cItpSccpRsrFromMtp,
       "cItpSccpErrToMtp": cItpSccpErrToMtp,
       "cItpSccpErrFromMtp": cItpSccpErrFromMtp,
       "cItpSccpCpcConfigLastChanged": cItpSccpCpcConfigLastChanged,
       "cItpSccpMapConfigLastChanged": cItpSccpMapConfigLastChanged,
       "cItpSccpSelConfigLastChanged": cItpSccpSelConfigLastChanged,
       "cItpSccpGtaConfigLastChanged": cItpSccpGtaConfigLastChanged,
       "cItpSccpAppConfigLastChanged": cItpSccpAppConfigLastChanged,
       "cItpSccpGttMapStateNotifEnabled": cItpSccpGttMapStateNotifEnabled,
       "cItpSccpPrefConfigLastChanged": cItpSccpPrefConfigLastChanged,
       "cItpSccpGttConfigLoad": cItpSccpGttConfigLoad,
       "cItpSccpGttConfigLoadStatus": cItpSccpGttConfigLoadStatus,
       "cItpSccpGttConPc": cItpSccpGttConPc,
       "cItpSccpGttConPcTable": cItpSccpGttConPcTable,
       "cItpSccpGttConPcTableEntry": cItpSccpGttConPcTableEntry,
       "cItpSccpGttConPcListName": cItpSccpGttConPcListName,
       "cItpSccpGttConPointCode": cItpSccpGttConPointCode,
       "cItpSccpGttConPcRefCount": cItpSccpGttConPcRefCount,
       "cItpSccpGttMap": cItpSccpGttMap,
       "cItpSccpGttMapTable": cItpSccpGttMapTable,
       "cItpSccpGttMapTableEntry": cItpSccpGttMapTableEntry,
       "cItpSccpGttMapPc": cItpSccpGttMapPc,
       "cItpSccpGttMapSsn": cItpSccpGttMapSsn,
       "cItpSccpGttMapDisplayPC": cItpSccpGttMapDisplayPC,
       "cItpSccpGttMapDisplaySS": cItpSccpGttMapDisplaySS,
       "cItpSccpGttMapType": cItpSccpGttMapType,
       "cItpSccpGttMapPcStatus": cItpSccpGttMapPcStatus,
       "cItpSccpGttMapSsStatus": cItpSccpGttMapSsStatus,
       "cItpSccpGttMapMultInd": cItpSccpGttMapMultInd,
       "cItpSccpGttMapBackupPc": cItpSccpGttMapBackupPc,
       "cItpSccpGttMapBackupSsn": cItpSccpGttMapBackupSsn,
       "cItpSccpGttMapConPcList": cItpSccpGttMapConPcList,
       "cItpSccpGttMapReRouteOnCong": cItpSccpGttMapReRouteOnCong,
       "cItpSccpGttMapAdjacent": cItpSccpGttMapAdjacent,
       "cItpSccpGttMapLastSsUsed": cItpSccpGttMapLastSsUsed,
       "cItpSccpGttMapUsed": cItpSccpGttMapUsed,
       "cItpSccpGttMapAltUsed": cItpSccpGttMapAltUsed,
       "cItpSccpGttMapSccpUnavail": cItpSccpGttMapSccpUnavail,
       "cItpSccpGttMapPcUnavail": cItpSccpGttMapPcUnavail,
       "cItpSccpGttMapSsUnavail": cItpSccpGttMapSsUnavail,
       "cItpSccpGttMapPcCongested": cItpSccpGttMapPcCongested,
       "cItpSccpGttMapSsCongested": cItpSccpGttMapSsCongested,
       "cItpSccpGttMapMtp3Fail": cItpSccpGttMapMtp3Fail,
       "cItpSccpGttMapRefCount": cItpSccpGttMapRefCount,
       "cItpSccpGttMapCongStatus": cItpSccpGttMapCongStatus,
       "cItpSccpGttSel": cItpSccpGttSel,
       "cItpSccpGttSelTable": cItpSccpGttSelTable,
       "cItpSccpGttSelTableEntry": cItpSccpGttSelTableEntry,
       "cItpSccpGttSelTT": cItpSccpGttSelTT,
       "cItpSccpGttSelNAI": cItpSccpGttSelNAI,
       "cItpSccpGttSelNP": cItpSccpGttSelNP,
       "cItpSccpGttSelGTI": cItpSccpGttSelGTI,
       "cItpSccpGttSelName": cItpSccpGttSelName,
       "cItpSccpGttSelNumPerf": cItpSccpGttSelNumPerf,
       "cItpSccpGttSelNotFound": cItpSccpGttSelNotFound,
       "cItpSccpGttSelQOS": cItpSccpGttSelQOS,
       "cItpSccpGttSelRefCount": cItpSccpGttSelRefCount,
       "cItpSccpGttPrePrefConv": cItpSccpGttPrePrefConv,
       "cItpSccpGttPostPrefConv": cItpSccpGttPostPrefConv,
       "cItpSccpGttGta": cItpSccpGttGta,
       "cItpSccpGttGtaTable": cItpSccpGttGtaTable,
       "cItpSccpGttGtaTableEntry": cItpSccpGttGtaTableEntry,
       "cItpSccpGttGtaTT": cItpSccpGttGtaTT,
       "cItpSccpGttGtaNAI": cItpSccpGttGtaNAI,
       "cItpSccpGttGtaNP": cItpSccpGttGtaNP,
       "cItpSccpGttGtaGTI": cItpSccpGttGtaGTI,
       "cItpSccpGttGtaAddr": cItpSccpGttGtaAddr,
       "cItpSccpGttGtaAddrDisp": cItpSccpGttGtaAddrDisp,
       "cItpSccpGttGtaAddrLen": cItpSccpGttGtaAddrLen,
       "cItpSccpGttGtaSelName": cItpSccpGttGtaSelName,
       "cItpSccpGttGtaResType": cItpSccpGttGtaResType,
       "cItpSccpGttGtaResPc": cItpSccpGttGtaResPc,
       "cItpSccpGttGtaResMap": cItpSccpGttGtaResMap,
       "cItpSccpGttGtaResAppGroup": cItpSccpGttGtaResAppGroup,
       "cItpSccpGttGtaTTorSSN": cItpSccpGttGtaTTorSSN,
       "cItpSccpGttGtaRoutingInd": cItpSccpGttGtaRoutingInd,
       "cItpSccpGttGtaQOS": cItpSccpGttGtaQOS,
       "cItpSccpGttGtaAddrDispZB": cItpSccpGttGtaAddrDispZB,
       "cItpSccpGttGtaAddrLenZB": cItpSccpGttGtaAddrLenZB,
       "cItpSccpGttGtaAsName": cItpSccpGttGtaAsName,
       "cItpSccpGttGtaTTorSSNvalue": cItpSccpGttGtaTTorSSNvalue,
       "cItpSccpGttApp": cItpSccpGttApp,
       "cItpSccpGttAppTable": cItpSccpGttAppTable,
       "cItpSccpGttAppTableEntry": cItpSccpGttAppTableEntry,
       "cItpSccpGttAppName": cItpSccpGttAppName,
       "cItpSccpGttAppCost": cItpSccpGttAppCost,
       "cItpSccpGttAppType": cItpSccpGttAppType,
       "cItpSccpGttAppPc": cItpSccpGttAppPc,
       "cItpSccpGttAppSsn": cItpSccpGttAppSsn,
       "cItpSccpGttAppRi": cItpSccpGttAppRi,
       "cItpSccpGttAppMult": cItpSccpGttAppMult,
       "cItpSccpGttAppRefCount": cItpSccpGttAppRefCount,
       "cItpSccpGttAppGr": cItpSccpGttAppGr,
       "cItpSccpGttAppGrTable": cItpSccpGttAppGrTable,
       "cItpSccpGttAppGrTableEntry": cItpSccpGttAppGrTableEntry,
       "cItpSccpGttAppGrName": cItpSccpGttAppGrName,
       "cItpSccpGttAppGrCost": cItpSccpGttAppGrCost,
       "cItpSccpGttAppGrEntNum": cItpSccpGttAppGrEntNum,
       "cItpSccpGttAppGrType": cItpSccpGttAppGrType,
       "cItpSccpGttAppGrPc": cItpSccpGttAppGrPc,
       "cItpSccpGttAppGrSsn": cItpSccpGttAppGrSsn,
       "cItpSccpGttAppGrRi": cItpSccpGttAppGrRi,
       "cItpSccpGttAppGrMult": cItpSccpGttAppGrMult,
       "cItpSccpGttAppGrRefCount": cItpSccpGttAppGrRefCount,
       "cItpSccpGttAppGrAsName": cItpSccpGttAppGrAsName,
       "cItpSccpGttAppGrNewSsn": cItpSccpGttAppGrNewSsn,
       "cItpSccpGttAppGrNumUsed": cItpSccpGttAppGrNumUsed,
       "cItpSccpGttPref": cItpSccpGttPref,
       "cItpSccpGttPrefTable": cItpSccpGttPrefTable,
       "cItpSccpGttPrefTableEntry": cItpSccpGttPrefTableEntry,
       "cItpSccpGttPrefName": cItpSccpGttPrefName,
       "cItpSccpGttPrefInAddr": cItpSccpGttPrefInAddr,
       "cItpSccpGttPrefOutAddr": cItpSccpGttPrefOutAddr,
       "cItpSccpGttPrefTblNAI": cItpSccpGttPrefTblNAI,
       "cItpSccpGttPrefTblNP": cItpSccpGttPrefTblNP,
       "cItpSccpGttPrefItemNAI": cItpSccpGttPrefItemNAI,
       "cItpSccpGttPrefItemNP": cItpSccpGttPrefItemNP,
       "cItpSccpConformance": cItpSccpConformance,
       "cItpSccpMIBCompliances": cItpSccpMIBCompliances,
       "cItpSccpMIBCompliance": cItpSccpMIBCompliance,
       "cItpSccpMIBComplianceRev1": cItpSccpMIBComplianceRev1,
       "cItpSccpMIBComplianceRev2": cItpSccpMIBComplianceRev2,
       "cItpSccpMIBGroups": cItpSccpMIBGroups,
       "cItpSccpScalarsGroup": cItpSccpScalarsGroup,
       "cItpSccpGttConPcGroup": cItpSccpGttConPcGroup,
       "cItpSccpGttMapGroup": cItpSccpGttMapGroup,
       "cItpSccpGttSelGroup": cItpSccpGttSelGroup,
       "cItpSccpGttGtaGroup": cItpSccpGttGtaGroup,
       "cItpSccpGttAppGroup": cItpSccpGttAppGroup,
       "cItpSccpNotificationsGroup": cItpSccpNotificationsGroup,
       "cItpSccpConfigStatusGroup": cItpSccpConfigStatusGroup,
       "cItpSccpGttSelGroupRev1": cItpSccpGttSelGroupRev1,
       "cItpSccpGttGtaGroupRev1": cItpSccpGttGtaGroupRev1,
       "cItpSccpGttAppGrGroup": cItpSccpGttAppGrGroup,
       "cItpSccpGttPrefGroup": cItpSccpGttPrefGroup,
       "cItpSccpGttGtaGroupRev2": cItpSccpGttGtaGroupRev2,
       "cItpSccpGttAppGrGroupRev2": cItpSccpGttAppGrGroupRev2}
)
