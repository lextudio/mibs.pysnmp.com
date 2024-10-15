# SNMP MIB module (CISCO-ITP-GSCCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-GSCCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:15 2024
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

(cgspCLLICode,
 cgspEventSequenceNumber,
 cgspInstNetwork) = mibBuilder.importSymbols(
    "CISCO-ITP-GSP-MIB",
    "cgspCLLICode",
    "cgspEventSequenceNumber",
    "cgspInstNetwork")

(CItpTcDisplayPC,
 CItpTcGtaLongAddr,
 CItpTcGtaLongDisplay,
 CItpTcGtaLongDisplayLen,
 CItpTcNAI,
 CItpTcNetworkName,
 CItpTcNumberingPlan,
 CItpTcPointCode,
 CItpTcSubSystemNumber,
 CItpTcTableLoadStatus,
 CItpTcTranslationType,
 CItpTcURL,
 CItpTcXuaName) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcDisplayPC",
    "CItpTcGtaLongAddr",
    "CItpTcGtaLongDisplay",
    "CItpTcGtaLongDisplayLen",
    "CItpTcNAI",
    "CItpTcNetworkName",
    "CItpTcNumberingPlan",
    "CItpTcPointCode",
    "CItpTcSubSystemNumber",
    "CItpTcTableLoadStatus",
    "CItpTcTranslationType",
    "CItpTcURL",
    "CItpTcXuaName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(EntPhysicalIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "EntPhysicalIndexOrZero")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoGsccpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335)
)
ciscoGsccpMIB.setRevisions(
        ("2009-11-08 00:00",
         "2009-05-25 00:00",
         "2008-11-24 00:00",
         "2005-11-10 00:00",
         "2004-12-22 00:00",
         "2004-11-16 00:00",
         "2004-04-30 00:00",
         "2003-09-30 00:00",
         "2003-08-21 00:00",
         "2003-03-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CgsccpConPcListName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class CgsccpGttSelName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class CgsccpGttAppName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class CgsccpGttPrefName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )



class CgsccpGttDisplaySS(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )



class CgsccpGttAppCost(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class CgsccpGttAppType(Integer32, TextualConvention):
    status = "current"
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



class CgsccpGttMapType(Integer32, TextualConvention):
    status = "current"
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



class CgsccpGttGtaResType(Integer32, TextualConvention):
    status = "current"
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



class CgsccpGttRoutingInd(Integer32, TextualConvention):
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



class CgsccpGttMapPcStatus(Integer32, TextualConvention):
    status = "current"
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



class CgsccpGttMapSsStatus(Integer32, TextualConvention):
    status = "current"
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



class CgsccpGttMultInd(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cgpa", 5),
          ("cost", 4),
          ("dominant", 3),
          ("shared", 2),
          ("solitary", 1),
          ("wrr", 6))
    )



class CgsccpGttMapCongStatus(Integer32, TextualConvention):
    status = "current"
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



class CgsccpGttTransType(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CgsccpGttQOS(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CgsccpGttGlobalTitleInd(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CgsccpClass(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("class0", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoGsccpMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGsccpMIBNotifs = _CiscoGsccpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0)
)
_CiscoGsccpMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGsccpMIBObjects = _CiscoGsccpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1)
)
_CgsccpScalars_ObjectIdentity = ObjectIdentity
cgsccpScalars = _CgsccpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1)
)


class _CgsccpGttTranslateSample_Type(Unsigned32):
    """Custom type cgsccpGttTranslateSample based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CgsccpGttTranslateSample_Type.__name__ = "Unsigned32"
_CgsccpGttTranslateSample_Object = MibScalar
cgsccpGttTranslateSample = _CgsccpGttTranslateSample_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1, 1),
    _CgsccpGttTranslateSample_Type()
)
cgsccpGttTranslateSample.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsccpGttTranslateSample.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttTranslateSample.setUnits("seconds")


class _CgsccpGttTranslatePeriod_Type(Unsigned32):
    """Custom type cgsccpGttTranslatePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_CgsccpGttTranslatePeriod_Type.__name__ = "Unsigned32"
_CgsccpGttTranslatePeriod_Object = MibScalar
cgsccpGttTranslatePeriod = _CgsccpGttTranslatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1, 2),
    _CgsccpGttTranslatePeriod_Type()
)
cgsccpGttTranslatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsccpGttTranslatePeriod.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttTranslatePeriod.setUnits("seconds")


class _CgsccpGttMapStateNotifEnabled_Type(TruthValue):
    """Custom type cgsccpGttMapStateNotifEnabled based on TruthValue"""


_CgsccpGttMapStateNotifEnabled_Object = MibScalar
cgsccpGttMapStateNotifEnabled = _CgsccpGttMapStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1, 3),
    _CgsccpGttMapStateNotifEnabled_Type()
)
cgsccpGttMapStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsccpGttMapStateNotifEnabled.setStatus("current")


class _CgsccpGttLoadTableNotifEnabled_Type(TruthValue):
    """Custom type cgsccpGttLoadTableNotifEnabled based on TruthValue"""


_CgsccpGttLoadTableNotifEnabled_Object = MibScalar
cgsccpGttLoadTableNotifEnabled = _CgsccpGttLoadTableNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1, 4),
    _CgsccpGttLoadTableNotifEnabled_Type()
)
cgsccpGttLoadTableNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsccpGttLoadTableNotifEnabled.setStatus("current")


class _CgsccpGttTransErrorsNotifEnabled_Type(TruthValue):
    """Custom type cgsccpGttTransErrorsNotifEnabled based on TruthValue"""


_CgsccpGttTransErrorsNotifEnabled_Object = MibScalar
cgsccpGttTransErrorsNotifEnabled = _CgsccpGttTransErrorsNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1, 5),
    _CgsccpGttTransErrorsNotifEnabled_Type()
)
cgsccpGttTransErrorsNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsccpGttTransErrorsNotifEnabled.setStatus("current")


class _CgsccpGttErrorPeriod_Type(Unsigned32):
    """Custom type cgsccpGttErrorPeriod based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_CgsccpGttErrorPeriod_Type.__name__ = "Unsigned32"
_CgsccpGttErrorPeriod_Object = MibScalar
cgsccpGttErrorPeriod = _CgsccpGttErrorPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1, 6),
    _CgsccpGttErrorPeriod_Type()
)
cgsccpGttErrorPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsccpGttErrorPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorPeriod.setUnits("seconds")


class _CgsccpGttErrorRecoveryCount_Type(Unsigned32):
    """Custom type cgsccpGttErrorRecoveryCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CgsccpGttErrorRecoveryCount_Type.__name__ = "Unsigned32"
_CgsccpGttErrorRecoveryCount_Object = MibScalar
cgsccpGttErrorRecoveryCount = _CgsccpGttErrorRecoveryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 1, 7),
    _CgsccpGttErrorRecoveryCount_Type()
)
cgsccpGttErrorRecoveryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cgsccpGttErrorRecoveryCount.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorRecoveryCount.setUnits("windows")
_CgsccpInst_ObjectIdentity = ObjectIdentity
cgsccpInst = _CgsccpInst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2)
)
_CgsccpInstTable_Object = MibTable
cgsccpInstTable = _CgsccpInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cgsccpInstTable.setStatus("current")
_CgsccpInstTableEntry_Object = MibTableRow
cgsccpInstTableEntry = _CgsccpInstTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1)
)
cgsccpInstTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgsccpInstTableEntry.setStatus("current")
_CgsccpInstTotalMsgs_Type = Counter32
_CgsccpInstTotalMsgs_Object = MibTableColumn
cgsccpInstTotalMsgs = _CgsccpInstTotalMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 1),
    _CgsccpInstTotalMsgs_Type()
)
cgsccpInstTotalMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstTotalMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstTotalMsgs.setUnits("packets")
_CgsccpInstLocalMsgs_Type = Counter32
_CgsccpInstLocalMsgs_Object = MibTableColumn
cgsccpInstLocalMsgs = _CgsccpInstLocalMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 2),
    _CgsccpInstLocalMsgs_Type()
)
cgsccpInstLocalMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstLocalMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstLocalMsgs.setUnits("packets")
_CgsccpInstTotalGttMsgs_Type = Counter32
_CgsccpInstTotalGttMsgs_Object = MibTableColumn
cgsccpInstTotalGttMsgs = _CgsccpInstTotalGttMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 3),
    _CgsccpInstTotalGttMsgs_Type()
)
cgsccpInstTotalGttMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstTotalGttMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstTotalGttMsgs.setUnits("packets")
_CgsccpInstUDTMsgsSent_Type = Counter32
_CgsccpInstUDTMsgsSent_Object = MibTableColumn
cgsccpInstUDTMsgsSent = _CgsccpInstUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 4),
    _CgsccpInstUDTMsgsSent_Type()
)
cgsccpInstUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstUDTMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstUDTMsgsSent.setUnits("packets")
_CgsccpInstUDTSMsgsSent_Type = Counter32
_CgsccpInstUDTSMsgsSent_Object = MibTableColumn
cgsccpInstUDTSMsgsSent = _CgsccpInstUDTSMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 5),
    _CgsccpInstUDTSMsgsSent_Type()
)
cgsccpInstUDTSMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstUDTSMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstUDTSMsgsSent.setUnits("packets")
_CgsccpInstUDTSMsgsAttempted_Type = Counter32
_CgsccpInstUDTSMsgsAttempted_Object = MibTableColumn
cgsccpInstUDTSMsgsAttempted = _CgsccpInstUDTSMsgsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 6),
    _CgsccpInstUDTSMsgsAttempted_Type()
)
cgsccpInstUDTSMsgsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstUDTSMsgsAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstUDTSMsgsAttempted.setUnits("packets")
_CgsccpInstUDTMsgsRcvd_Type = Counter32
_CgsccpInstUDTMsgsRcvd_Object = MibTableColumn
cgsccpInstUDTMsgsRcvd = _CgsccpInstUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 7),
    _CgsccpInstUDTMsgsRcvd_Type()
)
cgsccpInstUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstUDTMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstUDTMsgsRcvd.setUnits("packets")
_CgsccpInstUDTSMsgsRcvd_Type = Counter32
_CgsccpInstUDTSMsgsRcvd_Object = MibTableColumn
cgsccpInstUDTSMsgsRcvd = _CgsccpInstUDTSMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 8),
    _CgsccpInstUDTSMsgsRcvd_Type()
)
cgsccpInstUDTSMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstUDTSMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstUDTSMsgsRcvd.setUnits("packets")
_CgsccpInstXUDTMsgsSent_Type = Counter32
_CgsccpInstXUDTMsgsSent_Object = MibTableColumn
cgsccpInstXUDTMsgsSent = _CgsccpInstXUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 9),
    _CgsccpInstXUDTMsgsSent_Type()
)
cgsccpInstXUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstXUDTMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstXUDTMsgsSent.setUnits("packets")
_CgsccpInstXUDTSMsgsAttempted_Type = Counter32
_CgsccpInstXUDTSMsgsAttempted_Object = MibTableColumn
cgsccpInstXUDTSMsgsAttempted = _CgsccpInstXUDTSMsgsAttempted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 10),
    _CgsccpInstXUDTSMsgsAttempted_Type()
)
cgsccpInstXUDTSMsgsAttempted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstXUDTSMsgsAttempted.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstXUDTSMsgsAttempted.setUnits("packets")
_CgsccpInstXUDTSMsgsSent_Type = Counter32
_CgsccpInstXUDTSMsgsSent_Object = MibTableColumn
cgsccpInstXUDTSMsgsSent = _CgsccpInstXUDTSMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 11),
    _CgsccpInstXUDTSMsgsSent_Type()
)
cgsccpInstXUDTSMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstXUDTSMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstXUDTSMsgsSent.setUnits("packets")
_CgsccpInstXUDTMsgsRcvd_Type = Counter32
_CgsccpInstXUDTMsgsRcvd_Object = MibTableColumn
cgsccpInstXUDTMsgsRcvd = _CgsccpInstXUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 12),
    _CgsccpInstXUDTMsgsRcvd_Type()
)
cgsccpInstXUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstXUDTMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstXUDTMsgsRcvd.setUnits("packets")
_CgsccpInstXUDTSMsgsRcvd_Type = Counter32
_CgsccpInstXUDTSMsgsRcvd_Object = MibTableColumn
cgsccpInstXUDTSMsgsRcvd = _CgsccpInstXUDTSMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 13),
    _CgsccpInstXUDTSMsgsRcvd_Type()
)
cgsccpInstXUDTSMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstXUDTSMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstXUDTSMsgsRcvd.setUnits("packets")
_CgsccpInstLUDTMsgsSent_Type = Counter32
_CgsccpInstLUDTMsgsSent_Object = MibTableColumn
cgsccpInstLUDTMsgsSent = _CgsccpInstLUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 14),
    _CgsccpInstLUDTMsgsSent_Type()
)
cgsccpInstLUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstLUDTMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstLUDTMsgsSent.setUnits("packets")
_CgsccpInstLUDTSMsgsSent_Type = Counter32
_CgsccpInstLUDTSMsgsSent_Object = MibTableColumn
cgsccpInstLUDTSMsgsSent = _CgsccpInstLUDTSMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 15),
    _CgsccpInstLUDTSMsgsSent_Type()
)
cgsccpInstLUDTSMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstLUDTSMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstLUDTSMsgsSent.setUnits("packets")
_CgsccpInstLUDTMsgsRcvd_Type = Counter32
_CgsccpInstLUDTMsgsRcvd_Object = MibTableColumn
cgsccpInstLUDTMsgsRcvd = _CgsccpInstLUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 16),
    _CgsccpInstLUDTMsgsRcvd_Type()
)
cgsccpInstLUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstLUDTMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstLUDTMsgsRcvd.setUnits("packets")
_CgsccpInstLUDTSMsgsRcvd_Type = Counter32
_CgsccpInstLUDTSMsgsRcvd_Object = MibTableColumn
cgsccpInstLUDTSMsgsRcvd = _CgsccpInstLUDTSMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 17),
    _CgsccpInstLUDTSMsgsRcvd_Type()
)
cgsccpInstLUDTSMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstLUDTSMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstLUDTSMsgsRcvd.setUnits("packets")
_CgsccpInstCrToMtp_Type = Counter32
_CgsccpInstCrToMtp_Object = MibTableColumn
cgsccpInstCrToMtp = _CgsccpInstCrToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 18),
    _CgsccpInstCrToMtp_Type()
)
cgsccpInstCrToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstCrToMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstCrToMtp.setUnits("packets")
_CgsccpInstCrefToMtp_Type = Counter32
_CgsccpInstCrefToMtp_Object = MibTableColumn
cgsccpInstCrefToMtp = _CgsccpInstCrefToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 19),
    _CgsccpInstCrefToMtp_Type()
)
cgsccpInstCrefToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstCrefToMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstCrefToMtp.setUnits("packets")
_CgsccpInstCrFromMtp_Type = Counter32
_CgsccpInstCrFromMtp_Object = MibTableColumn
cgsccpInstCrFromMtp = _CgsccpInstCrFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 20),
    _CgsccpInstCrFromMtp_Type()
)
cgsccpInstCrFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstCrFromMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstCrFromMtp.setUnits("packets")
_CgsccpInstCrefFromMtp_Type = Counter32
_CgsccpInstCrefFromMtp_Object = MibTableColumn
cgsccpInstCrefFromMtp = _CgsccpInstCrefFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 21),
    _CgsccpInstCrefFromMtp_Type()
)
cgsccpInstCrefFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstCrefFromMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstCrefFromMtp.setUnits("packets")
_CgsccpInstRsrToMtp_Type = Counter32
_CgsccpInstRsrToMtp_Object = MibTableColumn
cgsccpInstRsrToMtp = _CgsccpInstRsrToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 22),
    _CgsccpInstRsrToMtp_Type()
)
cgsccpInstRsrToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstRsrToMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstRsrToMtp.setUnits("packets")
_CgsccpInstRsrFromMtp_Type = Counter32
_CgsccpInstRsrFromMtp_Object = MibTableColumn
cgsccpInstRsrFromMtp = _CgsccpInstRsrFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 23),
    _CgsccpInstRsrFromMtp_Type()
)
cgsccpInstRsrFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstRsrFromMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstRsrFromMtp.setUnits("packets")
_CgsccpInstErrToMtp_Type = Counter32
_CgsccpInstErrToMtp_Object = MibTableColumn
cgsccpInstErrToMtp = _CgsccpInstErrToMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 24),
    _CgsccpInstErrToMtp_Type()
)
cgsccpInstErrToMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstErrToMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstErrToMtp.setUnits("packets")
_CgsccpInstErrFromMtp_Type = Counter32
_CgsccpInstErrFromMtp_Object = MibTableColumn
cgsccpInstErrFromMtp = _CgsccpInstErrFromMtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 25),
    _CgsccpInstErrFromMtp_Type()
)
cgsccpInstErrFromMtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstErrFromMtp.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstErrFromMtp.setUnits("packets")
_CgsccpInstQ752T7E1_Type = Counter32
_CgsccpInstQ752T7E1_Object = MibTableColumn
cgsccpInstQ752T7E1 = _CgsccpInstQ752T7E1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 26),
    _CgsccpInstQ752T7E1_Type()
)
cgsccpInstQ752T7E1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstQ752T7E1.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstQ752T7E1.setUnits("packets")
_CgsccpInstInvalidGttFormat_Type = Counter32
_CgsccpInstInvalidGttFormat_Object = MibTableColumn
cgsccpInstInvalidGttFormat = _CgsccpInstInvalidGttFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 27),
    _CgsccpInstInvalidGttFormat_Type()
)
cgsccpInstInvalidGttFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstInvalidGttFormat.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstInvalidGttFormat.setUnits("packets")
_CgsccpInstQ752T7E13_Type = Counter32
_CgsccpInstQ752T7E13_Object = MibTableColumn
cgsccpInstQ752T7E13 = _CgsccpInstQ752T7E13_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 28),
    _CgsccpInstQ752T7E13_Type()
)
cgsccpInstQ752T7E13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstQ752T7E13.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstQ752T7E13.setUnits("packets")
_CgsccpInstMapNotFound_Type = Counter32
_CgsccpInstMapNotFound_Object = MibTableColumn
cgsccpInstMapNotFound = _CgsccpInstMapNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 29),
    _CgsccpInstMapNotFound_Type()
)
cgsccpInstMapNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstMapNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstMapNotFound.setUnits("packets")
_CgsccpInstQ752T7E7_Type = Counter32
_CgsccpInstQ752T7E7_Object = MibTableColumn
cgsccpInstQ752T7E7 = _CgsccpInstQ752T7E7_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 30),
    _CgsccpInstQ752T7E7_Type()
)
cgsccpInstQ752T7E7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstQ752T7E7.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstQ752T7E7.setUnits("packets")
_CgsccpInstGttConfigStatus_Type = CItpTcTableLoadStatus
_CgsccpInstGttConfigStatus_Object = MibTableColumn
cgsccpInstGttConfigStatus = _CgsccpInstGttConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 31),
    _CgsccpInstGttConfigStatus_Type()
)
cgsccpInstGttConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstGttConfigStatus.setStatus("current")
_CgsccpInstConfigTS_Type = TimeStamp
_CgsccpInstConfigTS_Object = MibTableColumn
cgsccpInstConfigTS = _CgsccpInstConfigTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 32),
    _CgsccpInstConfigTS_Type()
)
cgsccpInstConfigTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstConfigTS.setStatus("current")
_CgsccpInstGttConfigTS_Type = TimeStamp
_CgsccpInstGttConfigTS_Object = MibTableColumn
cgsccpInstGttConfigTS = _CgsccpInstGttConfigTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 33),
    _CgsccpInstGttConfigTS_Type()
)
cgsccpInstGttConfigTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstGttConfigTS.setStatus("current")
_CgsccpInstLastURL_Type = CItpTcURL
_CgsccpInstLastURL_Object = MibTableColumn
cgsccpInstLastURL = _CgsccpInstLastURL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 34),
    _CgsccpInstLastURL_Type()
)
cgsccpInstLastURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstLastURL.setStatus("current")
_CgsccpInstConPcTableEntries_Type = Gauge32
_CgsccpInstConPcTableEntries_Object = MibTableColumn
cgsccpInstConPcTableEntries = _CgsccpInstConPcTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 35),
    _CgsccpInstConPcTableEntries_Type()
)
cgsccpInstConPcTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstConPcTableEntries.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstConPcTableEntries.setUnits("entries")
_CgsccpInstMapTableEntries_Type = Gauge32
_CgsccpInstMapTableEntries_Object = MibTableColumn
cgsccpInstMapTableEntries = _CgsccpInstMapTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 36),
    _CgsccpInstMapTableEntries_Type()
)
cgsccpInstMapTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstMapTableEntries.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstMapTableEntries.setUnits("entries")
_CgsccpInstGtaTableEntries_Type = Gauge32
_CgsccpInstGtaTableEntries_Object = MibTableColumn
cgsccpInstGtaTableEntries = _CgsccpInstGtaTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 37),
    _CgsccpInstGtaTableEntries_Type()
)
cgsccpInstGtaTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstGtaTableEntries.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstGtaTableEntries.setUnits("entries")
_CgsccpInstSelTableEntries_Type = Gauge32
_CgsccpInstSelTableEntries_Object = MibTableColumn
cgsccpInstSelTableEntries = _CgsccpInstSelTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 38),
    _CgsccpInstSelTableEntries_Type()
)
cgsccpInstSelTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstSelTableEntries.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstSelTableEntries.setUnits("entries")
_CgsccpInstAppGrTableEntries_Type = Gauge32
_CgsccpInstAppGrTableEntries_Object = MibTableColumn
cgsccpInstAppGrTableEntries = _CgsccpInstAppGrTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 39),
    _CgsccpInstAppGrTableEntries_Type()
)
cgsccpInstAppGrTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstAppGrTableEntries.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstAppGrTableEntries.setUnits("entries")
_CgsccpInstRowStatus_Type = RowStatus
_CgsccpInstRowStatus_Object = MibTableColumn
cgsccpInstRowStatus = _CgsccpInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 40),
    _CgsccpInstRowStatus_Type()
)
cgsccpInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpInstRowStatus.setStatus("current")
_CgsccpInstPrefTableEntries_Type = Gauge32
_CgsccpInstPrefTableEntries_Object = MibTableColumn
cgsccpInstPrefTableEntries = _CgsccpInstPrefTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 41),
    _CgsccpInstPrefTableEntries_Type()
)
cgsccpInstPrefTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstPrefTableEntries.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstPrefTableEntries.setUnits("entries")
_CgsccpInstQ752Unqualified_Type = Counter32
_CgsccpInstQ752Unqualified_Object = MibTableColumn
cgsccpInstQ752Unqualified = _CgsccpInstQ752Unqualified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 42),
    _CgsccpInstQ752Unqualified_Type()
)
cgsccpInstQ752Unqualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstQ752Unqualified.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpInstQ752Unqualified.setUnits("packets")


class _CgsccpInstErrorIndicator_Type(TruthValue):
    """Custom type cgsccpInstErrorIndicator based on TruthValue"""


_CgsccpInstErrorIndicator_Object = MibTableColumn
cgsccpInstErrorIndicator = _CgsccpInstErrorIndicator_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 43),
    _CgsccpInstErrorIndicator_Type()
)
cgsccpInstErrorIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstErrorIndicator.setStatus("current")
_CgsccpInstReassUnsup_Type = Counter32
_CgsccpInstReassUnsup_Object = MibTableColumn
cgsccpInstReassUnsup = _CgsccpInstReassUnsup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 44),
    _CgsccpInstReassUnsup_Type()
)
cgsccpInstReassUnsup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstReassUnsup.setStatus("current")
_CgsccpInstReassFail_Type = Counter32
_CgsccpInstReassFail_Object = MibTableColumn
cgsccpInstReassFail = _CgsccpInstReassFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 45),
    _CgsccpInstReassFail_Type()
)
cgsccpInstReassFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstReassFail.setStatus("current")
_CgsccpInstSegUnsup_Type = Counter32
_CgsccpInstSegUnsup_Object = MibTableColumn
cgsccpInstSegUnsup = _CgsccpInstSegUnsup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 46),
    _CgsccpInstSegUnsup_Type()
)
cgsccpInstSegUnsup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstSegUnsup.setStatus("current")
_CgsccpInstSegFail_Type = Counter32
_CgsccpInstSegFail_Object = MibTableColumn
cgsccpInstSegFail = _CgsccpInstSegFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 2, 1, 1, 47),
    _CgsccpInstSegFail_Type()
)
cgsccpInstSegFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpInstSegFail.setStatus("current")
_CgsccpGttConPc_ObjectIdentity = ObjectIdentity
cgsccpGttConPc = _CgsccpGttConPc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 3)
)
_CgsccpGttConPcTable_Object = MibTable
cgsccpGttConPcTable = _CgsccpGttConPcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttConPcTable.setStatus("current")
_CgsccpGttConPcTableEntry_Object = MibTableRow
cgsccpGttConPcTableEntry = _CgsccpGttConPcTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 3, 1, 1)
)
cgsccpGttConPcTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttConPcListName"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttConPointCode"),
)
if mibBuilder.loadTexts:
    cgsccpGttConPcTableEntry.setStatus("current")
_CgsccpGttConPcListName_Type = CgsccpConPcListName
_CgsccpGttConPcListName_Object = MibTableColumn
cgsccpGttConPcListName = _CgsccpGttConPcListName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 3, 1, 1, 1),
    _CgsccpGttConPcListName_Type()
)
cgsccpGttConPcListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttConPcListName.setStatus("current")
_CgsccpGttConPointCode_Type = CItpTcPointCode
_CgsccpGttConPointCode_Object = MibTableColumn
cgsccpGttConPointCode = _CgsccpGttConPointCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 3, 1, 1, 2),
    _CgsccpGttConPointCode_Type()
)
cgsccpGttConPointCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttConPointCode.setStatus("current")
_CgsccpGttConPcRowStatus_Type = RowStatus
_CgsccpGttConPcRowStatus_Object = MibTableColumn
cgsccpGttConPcRowStatus = _CgsccpGttConPcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 3, 1, 1, 3),
    _CgsccpGttConPcRowStatus_Type()
)
cgsccpGttConPcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttConPcRowStatus.setStatus("current")
_CgsccpGttMap_ObjectIdentity = ObjectIdentity
cgsccpGttMap = _CgsccpGttMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4)
)
_CgsccpGttMapTable_Object = MibTable
cgsccpGttMapTable = _CgsccpGttMapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttMapTable.setStatus("current")
_CgsccpGttMapTableEntry_Object = MibTableRow
cgsccpGttMapTableEntry = _CgsccpGttMapTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1)
)
cgsccpGttMapTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttMapPc"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttMapSsn"),
)
if mibBuilder.loadTexts:
    cgsccpGttMapTableEntry.setStatus("current")
_CgsccpGttMapPc_Type = CItpTcPointCode
_CgsccpGttMapPc_Object = MibTableColumn
cgsccpGttMapPc = _CgsccpGttMapPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 1),
    _CgsccpGttMapPc_Type()
)
cgsccpGttMapPc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttMapPc.setStatus("current")
_CgsccpGttMapSsn_Type = CItpTcSubSystemNumber
_CgsccpGttMapSsn_Object = MibTableColumn
cgsccpGttMapSsn = _CgsccpGttMapSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 2),
    _CgsccpGttMapSsn_Type()
)
cgsccpGttMapSsn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttMapSsn.setStatus("current")
_CgsccpGttMapDisplayPC_Type = CItpTcDisplayPC
_CgsccpGttMapDisplayPC_Object = MibTableColumn
cgsccpGttMapDisplayPC = _CgsccpGttMapDisplayPC_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 3),
    _CgsccpGttMapDisplayPC_Type()
)
cgsccpGttMapDisplayPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapDisplayPC.setStatus("current")
_CgsccpGttMapDisplaySS_Type = CgsccpGttDisplaySS
_CgsccpGttMapDisplaySS_Object = MibTableColumn
cgsccpGttMapDisplaySS = _CgsccpGttMapDisplaySS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 4),
    _CgsccpGttMapDisplaySS_Type()
)
cgsccpGttMapDisplaySS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapDisplaySS.setStatus("current")
_CgsccpGttMapType_Type = CgsccpGttMapType
_CgsccpGttMapType_Object = MibTableColumn
cgsccpGttMapType = _CgsccpGttMapType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 5),
    _CgsccpGttMapType_Type()
)
cgsccpGttMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapType.setStatus("current")
_CgsccpGttMapPcStatus_Type = CgsccpGttMapPcStatus
_CgsccpGttMapPcStatus_Object = MibTableColumn
cgsccpGttMapPcStatus = _CgsccpGttMapPcStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 6),
    _CgsccpGttMapPcStatus_Type()
)
cgsccpGttMapPcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapPcStatus.setStatus("current")
_CgsccpGttMapSsStatus_Type = CgsccpGttMapSsStatus
_CgsccpGttMapSsStatus_Object = MibTableColumn
cgsccpGttMapSsStatus = _CgsccpGttMapSsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 7),
    _CgsccpGttMapSsStatus_Type()
)
cgsccpGttMapSsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapSsStatus.setStatus("current")
_CgsccpGttMapMultInd_Type = CgsccpGttMultInd
_CgsccpGttMapMultInd_Object = MibTableColumn
cgsccpGttMapMultInd = _CgsccpGttMapMultInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 8),
    _CgsccpGttMapMultInd_Type()
)
cgsccpGttMapMultInd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapMultInd.setStatus("current")


class _CgsccpGttMapBackupPc_Type(CItpTcPointCode):
    """Custom type cgsccpGttMapBackupPc based on CItpTcPointCode"""
    defaultValue = 0


_CgsccpGttMapBackupPc_Object = MibTableColumn
cgsccpGttMapBackupPc = _CgsccpGttMapBackupPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 9),
    _CgsccpGttMapBackupPc_Type()
)
cgsccpGttMapBackupPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapBackupPc.setStatus("current")


class _CgsccpGttMapBackupSsn_Type(CItpTcSubSystemNumber):
    """Custom type cgsccpGttMapBackupSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CgsccpGttMapBackupSsn_Object = MibTableColumn
cgsccpGttMapBackupSsn = _CgsccpGttMapBackupSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 10),
    _CgsccpGttMapBackupSsn_Type()
)
cgsccpGttMapBackupSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapBackupSsn.setStatus("current")
_CgsccpGttMapConPcList_Type = CgsccpConPcListName
_CgsccpGttMapConPcList_Object = MibTableColumn
cgsccpGttMapConPcList = _CgsccpGttMapConPcList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 11),
    _CgsccpGttMapConPcList_Type()
)
cgsccpGttMapConPcList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapConPcList.setStatus("current")


class _CgsccpGttMapReRouteOnCong_Type(TruthValue):
    """Custom type cgsccpGttMapReRouteOnCong based on TruthValue"""


_CgsccpGttMapReRouteOnCong_Object = MibTableColumn
cgsccpGttMapReRouteOnCong = _CgsccpGttMapReRouteOnCong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 12),
    _CgsccpGttMapReRouteOnCong_Type()
)
cgsccpGttMapReRouteOnCong.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapReRouteOnCong.setStatus("current")


class _CgsccpGttMapAdjacent_Type(TruthValue):
    """Custom type cgsccpGttMapAdjacent based on TruthValue"""


_CgsccpGttMapAdjacent_Object = MibTableColumn
cgsccpGttMapAdjacent = _CgsccpGttMapAdjacent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 13),
    _CgsccpGttMapAdjacent_Type()
)
cgsccpGttMapAdjacent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapAdjacent.setStatus("current")
_CgsccpGttMapLastSsUsed_Type = TruthValue
_CgsccpGttMapLastSsUsed_Object = MibTableColumn
cgsccpGttMapLastSsUsed = _CgsccpGttMapLastSsUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 14),
    _CgsccpGttMapLastSsUsed_Type()
)
cgsccpGttMapLastSsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapLastSsUsed.setStatus("current")
_CgsccpGttMapUsed_Type = Counter32
_CgsccpGttMapUsed_Object = MibTableColumn
cgsccpGttMapUsed = _CgsccpGttMapUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 15),
    _CgsccpGttMapUsed_Type()
)
cgsccpGttMapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapUsed.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapUsed.setUnits("messages")
_CgsccpGttMapAltUsed_Type = Counter32
_CgsccpGttMapAltUsed_Object = MibTableColumn
cgsccpGttMapAltUsed = _CgsccpGttMapAltUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 16),
    _CgsccpGttMapAltUsed_Type()
)
cgsccpGttMapAltUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapAltUsed.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapAltUsed.setUnits("messages")
_CgsccpGttMapSccpUnavail_Type = Counter32
_CgsccpGttMapSccpUnavail_Object = MibTableColumn
cgsccpGttMapSccpUnavail = _CgsccpGttMapSccpUnavail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 17),
    _CgsccpGttMapSccpUnavail_Type()
)
cgsccpGttMapSccpUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapSccpUnavail.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapSccpUnavail.setUnits("occurrences")
_CgsccpGttMapQ752T7E3Fail_Type = Counter32
_CgsccpGttMapQ752T7E3Fail_Object = MibTableColumn
cgsccpGttMapQ752T7E3Fail = _CgsccpGttMapQ752T7E3Fail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 18),
    _CgsccpGttMapQ752T7E3Fail_Type()
)
cgsccpGttMapQ752T7E3Fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E3Fail.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E3Fail.setUnits("occurrences")
_CgsccpGttMapQ752T7E3Un_Type = Counter32
_CgsccpGttMapQ752T7E3Un_Object = MibTableColumn
cgsccpGttMapQ752T7E3Un = _CgsccpGttMapQ752T7E3Un_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 19),
    _CgsccpGttMapQ752T7E3Un_Type()
)
cgsccpGttMapQ752T7E3Un.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E3Un.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E3Un.setUnits("occurrences")
_CgsccpGttMapQ752T7E4_Type = Counter32
_CgsccpGttMapQ752T7E4_Object = MibTableColumn
cgsccpGttMapQ752T7E4 = _CgsccpGttMapQ752T7E4_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 20),
    _CgsccpGttMapQ752T7E4_Type()
)
cgsccpGttMapQ752T7E4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E4.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E4.setUnits("occurrences")
_CgsccpGttMapQ752T7E5_Type = Counter32
_CgsccpGttMapQ752T7E5_Object = MibTableColumn
cgsccpGttMapQ752T7E5 = _CgsccpGttMapQ752T7E5_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 21),
    _CgsccpGttMapQ752T7E5_Type()
)
cgsccpGttMapQ752T7E5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E5.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E5.setUnits("occurrences")
_CgsccpGttMapQ752T7E6_Type = Counter32
_CgsccpGttMapQ752T7E6_Object = MibTableColumn
cgsccpGttMapQ752T7E6 = _CgsccpGttMapQ752T7E6_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 22),
    _CgsccpGttMapQ752T7E6_Type()
)
cgsccpGttMapQ752T7E6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E6.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttMapQ752T7E6.setUnits("occurrences")


class _CgsccpGttMapRefCount_Type(Gauge32):
    """Custom type cgsccpGttMapRefCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CgsccpGttMapRefCount_Type.__name__ = "Gauge32"
_CgsccpGttMapRefCount_Object = MibTableColumn
cgsccpGttMapRefCount = _CgsccpGttMapRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 23),
    _CgsccpGttMapRefCount_Type()
)
cgsccpGttMapRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapRefCount.setStatus("current")
_CgsccpGttMapCongStatus_Type = CgsccpGttMapCongStatus
_CgsccpGttMapCongStatus_Object = MibTableColumn
cgsccpGttMapCongStatus = _CgsccpGttMapCongStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 24),
    _CgsccpGttMapCongStatus_Type()
)
cgsccpGttMapCongStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapCongStatus.setStatus("current")
_CgsccpGttMapRowStatus_Type = RowStatus
_CgsccpGttMapRowStatus_Object = MibTableColumn
cgsccpGttMapRowStatus = _CgsccpGttMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 25),
    _CgsccpGttMapRowStatus_Type()
)
cgsccpGttMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttMapRowStatus.setStatus("current")
_CgsccpGttMapCongLvl1_Type = Counter32
_CgsccpGttMapCongLvl1_Object = MibTableColumn
cgsccpGttMapCongLvl1 = _CgsccpGttMapCongLvl1_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 26),
    _CgsccpGttMapCongLvl1_Type()
)
cgsccpGttMapCongLvl1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapCongLvl1.setStatus("current")
_CgsccpGttMapCongLvl2_Type = Counter32
_CgsccpGttMapCongLvl2_Object = MibTableColumn
cgsccpGttMapCongLvl2 = _CgsccpGttMapCongLvl2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 27),
    _CgsccpGttMapCongLvl2_Type()
)
cgsccpGttMapCongLvl2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapCongLvl2.setStatus("current")
_CgsccpGttMapCongLvl3_Type = Counter32
_CgsccpGttMapCongLvl3_Object = MibTableColumn
cgsccpGttMapCongLvl3 = _CgsccpGttMapCongLvl3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 28),
    _CgsccpGttMapCongLvl3_Type()
)
cgsccpGttMapCongLvl3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapCongLvl3.setStatus("current")
_CgsccpGttMapSSPRcvd_Type = Counter32
_CgsccpGttMapSSPRcvd_Object = MibTableColumn
cgsccpGttMapSSPRcvd = _CgsccpGttMapSSPRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 29),
    _CgsccpGttMapSSPRcvd_Type()
)
cgsccpGttMapSSPRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapSSPRcvd.setStatus("current")
_CgsccpGttMapSSARcvd_Type = Counter32
_CgsccpGttMapSSARcvd_Object = MibTableColumn
cgsccpGttMapSSARcvd = _CgsccpGttMapSSARcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 4, 1, 1, 30),
    _CgsccpGttMapSSARcvd_Type()
)
cgsccpGttMapSSARcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttMapSSARcvd.setStatus("current")
_CgsccpGttSel_ObjectIdentity = ObjectIdentity
cgsccpGttSel = _CgsccpGttSel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5)
)
_CgsccpGttSelTable_Object = MibTable
cgsccpGttSelTable = _CgsccpGttSelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttSelTable.setStatus("current")
_CgsccpGttSelTableEntry_Object = MibTableRow
cgsccpGttSelTableEntry = _CgsccpGttSelTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1)
)
cgsccpGttSelTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelTT"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelNAI"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelNP"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelGTI"),
)
if mibBuilder.loadTexts:
    cgsccpGttSelTableEntry.setStatus("current")
_CgsccpGttSelTT_Type = CgsccpGttTransType
_CgsccpGttSelTT_Object = MibTableColumn
cgsccpGttSelTT = _CgsccpGttSelTT_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 1),
    _CgsccpGttSelTT_Type()
)
cgsccpGttSelTT.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttSelTT.setStatus("current")
_CgsccpGttSelNAI_Type = CItpTcNAI
_CgsccpGttSelNAI_Object = MibTableColumn
cgsccpGttSelNAI = _CgsccpGttSelNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 2),
    _CgsccpGttSelNAI_Type()
)
cgsccpGttSelNAI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttSelNAI.setStatus("current")
_CgsccpGttSelNP_Type = CItpTcNumberingPlan
_CgsccpGttSelNP_Object = MibTableColumn
cgsccpGttSelNP = _CgsccpGttSelNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 3),
    _CgsccpGttSelNP_Type()
)
cgsccpGttSelNP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttSelNP.setStatus("current")
_CgsccpGttSelGTI_Type = CgsccpGttGlobalTitleInd
_CgsccpGttSelGTI_Object = MibTableColumn
cgsccpGttSelGTI = _CgsccpGttSelGTI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 4),
    _CgsccpGttSelGTI_Type()
)
cgsccpGttSelGTI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttSelGTI.setStatus("current")
_CgsccpGttSelName_Type = CgsccpGttSelName
_CgsccpGttSelName_Object = MibTableColumn
cgsccpGttSelName = _CgsccpGttSelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 5),
    _CgsccpGttSelName_Type()
)
cgsccpGttSelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttSelName.setStatus("current")
_CgsccpGttSelNumPerf_Type = Counter32
_CgsccpGttSelNumPerf_Object = MibTableColumn
cgsccpGttSelNumPerf = _CgsccpGttSelNumPerf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 6),
    _CgsccpGttSelNumPerf_Type()
)
cgsccpGttSelNumPerf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttSelNumPerf.setStatus("current")
_CgsccpGttQ752T7E2_Type = Counter32
_CgsccpGttQ752T7E2_Object = MibTableColumn
cgsccpGttQ752T7E2 = _CgsccpGttQ752T7E2_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 7),
    _CgsccpGttQ752T7E2_Type()
)
cgsccpGttQ752T7E2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttQ752T7E2.setStatus("current")


class _CgsccpGttSelQOS_Type(CgsccpGttQOS):
    """Custom type cgsccpGttSelQOS based on CgsccpGttQOS"""
    defaultValue = 255


_CgsccpGttSelQOS_Object = MibTableColumn
cgsccpGttSelQOS = _CgsccpGttSelQOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 8),
    _CgsccpGttSelQOS_Type()
)
cgsccpGttSelQOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttSelQOS.setStatus("current")


class _CgsccpGttSelRefCount_Type(Gauge32):
    """Custom type cgsccpGttSelRefCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CgsccpGttSelRefCount_Type.__name__ = "Gauge32"
_CgsccpGttSelRefCount_Object = MibTableColumn
cgsccpGttSelRefCount = _CgsccpGttSelRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 9),
    _CgsccpGttSelRefCount_Type()
)
cgsccpGttSelRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttSelRefCount.setStatus("current")
_CgsccpGttSelPrePrefConv_Type = CgsccpGttPrefName
_CgsccpGttSelPrePrefConv_Object = MibTableColumn
cgsccpGttSelPrePrefConv = _CgsccpGttSelPrePrefConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 10),
    _CgsccpGttSelPrePrefConv_Type()
)
cgsccpGttSelPrePrefConv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttSelPrePrefConv.setStatus("current")
_CgsccpGttSelPostPrefConv_Type = CgsccpGttPrefName
_CgsccpGttSelPostPrefConv_Object = MibTableColumn
cgsccpGttSelPostPrefConv = _CgsccpGttSelPostPrefConv_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 11),
    _CgsccpGttSelPostPrefConv_Type()
)
cgsccpGttSelPostPrefConv.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttSelPostPrefConv.setStatus("current")
_CgsccpGttSelRowStatus_Type = RowStatus
_CgsccpGttSelRowStatus_Object = MibTableColumn
cgsccpGttSelRowStatus = _CgsccpGttSelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 12),
    _CgsccpGttSelRowStatus_Type()
)
cgsccpGttSelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttSelRowStatus.setStatus("current")
_CgsccpGttNextSelName_Type = CgsccpGttSelName
_CgsccpGttNextSelName_Object = MibTableColumn
cgsccpGttNextSelName = _CgsccpGttNextSelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 13),
    _CgsccpGttNextSelName_Type()
)
cgsccpGttNextSelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttNextSelName.setStatus("current")
_CgsccpGttNextSelRefed_Type = Gauge32
_CgsccpGttNextSelRefed_Object = MibTableColumn
cgsccpGttNextSelRefed = _CgsccpGttNextSelRefed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 5, 1, 1, 14),
    _CgsccpGttNextSelRefed_Type()
)
cgsccpGttNextSelRefed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttNextSelRefed.setStatus("current")
_CgsccpGttGta_ObjectIdentity = ObjectIdentity
cgsccpGttGta = _CgsccpGttGta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6)
)
_CgsccpGttGtaTable_Object = MibTable
cgsccpGttGtaTable = _CgsccpGttGtaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttGtaTable.setStatus("current")
_CgsccpGttGtaTableEntry_Object = MibTableRow
cgsccpGttGtaTableEntry = _CgsccpGttGtaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1)
)
cgsccpGttGtaTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelTT"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelNAI"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelNP"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttSelGTI"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaAddr"),
)
if mibBuilder.loadTexts:
    cgsccpGttGtaTableEntry.setStatus("current")
_CgsccpGttGtaAddr_Type = CItpTcGtaLongAddr
_CgsccpGttGtaAddr_Object = MibTableColumn
cgsccpGttGtaAddr = _CgsccpGttGtaAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 1),
    _CgsccpGttGtaAddr_Type()
)
cgsccpGttGtaAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttGtaAddr.setStatus("current")
_CgsccpGttGtaSelName_Type = CgsccpGttSelName
_CgsccpGttGtaSelName_Object = MibTableColumn
cgsccpGttGtaSelName = _CgsccpGttGtaSelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 2),
    _CgsccpGttGtaSelName_Type()
)
cgsccpGttGtaSelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaSelName.setStatus("current")
_CgsccpGttGtaResType_Type = CgsccpGttGtaResType
_CgsccpGttGtaResType_Object = MibTableColumn
cgsccpGttGtaResType = _CgsccpGttGtaResType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 3),
    _CgsccpGttGtaResType_Type()
)
cgsccpGttGtaResType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaResType.setStatus("current")


class _CgsccpGttGtaResPc_Type(CItpTcPointCode):
    """Custom type cgsccpGttGtaResPc based on CItpTcPointCode"""
    defaultValue = 0


_CgsccpGttGtaResPc_Object = MibTableColumn
cgsccpGttGtaResPc = _CgsccpGttGtaResPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 4),
    _CgsccpGttGtaResPc_Type()
)
cgsccpGttGtaResPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaResPc.setStatus("current")


class _CgsccpGttGtaResMap_Type(CItpTcPointCode):
    """Custom type cgsccpGttGtaResMap based on CItpTcPointCode"""
    defaultValue = 0


_CgsccpGttGtaResMap_Object = MibTableColumn
cgsccpGttGtaResMap = _CgsccpGttGtaResMap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 5),
    _CgsccpGttGtaResMap_Type()
)
cgsccpGttGtaResMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaResMap.setStatus("current")
_CgsccpGttGtaResAppGroup_Type = CgsccpGttAppName
_CgsccpGttGtaResAppGroup_Object = MibTableColumn
cgsccpGttGtaResAppGroup = _CgsccpGttGtaResAppGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 6),
    _CgsccpGttGtaResAppGroup_Type()
)
cgsccpGttGtaResAppGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaResAppGroup.setStatus("current")
_CgsccpGttGtaTTorSSN_Type = CItpTcTranslationType
_CgsccpGttGtaTTorSSN_Object = MibTableColumn
cgsccpGttGtaTTorSSN = _CgsccpGttGtaTTorSSN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 7),
    _CgsccpGttGtaTTorSSN_Type()
)
cgsccpGttGtaTTorSSN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaTTorSSN.setStatus("current")


class _CgsccpGttGtaTTorSSNvalue_Type(Unsigned32):
    """Custom type cgsccpGttGtaTTorSSNvalue based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CgsccpGttGtaTTorSSNvalue_Type.__name__ = "Unsigned32"
_CgsccpGttGtaTTorSSNvalue_Object = MibTableColumn
cgsccpGttGtaTTorSSNvalue = _CgsccpGttGtaTTorSSNvalue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 8),
    _CgsccpGttGtaTTorSSNvalue_Type()
)
cgsccpGttGtaTTorSSNvalue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaTTorSSNvalue.setStatus("current")
_CgsccpGttGtaRoutingInd_Type = CgsccpGttRoutingInd
_CgsccpGttGtaRoutingInd_Object = MibTableColumn
cgsccpGttGtaRoutingInd = _CgsccpGttGtaRoutingInd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 9),
    _CgsccpGttGtaRoutingInd_Type()
)
cgsccpGttGtaRoutingInd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaRoutingInd.setStatus("current")


class _CgsccpGttGtaQOS_Type(CgsccpGttQOS):
    """Custom type cgsccpGttGtaQOS based on CgsccpGttQOS"""
    defaultValue = 255


_CgsccpGttGtaQOS_Object = MibTableColumn
cgsccpGttGtaQOS = _CgsccpGttGtaQOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 10),
    _CgsccpGttGtaQOS_Type()
)
cgsccpGttGtaQOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaQOS.setStatus("current")
_CgsccpGttGtaAddrDisp_Type = CItpTcGtaLongDisplay
_CgsccpGttGtaAddrDisp_Object = MibTableColumn
cgsccpGttGtaAddrDisp = _CgsccpGttGtaAddrDisp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 11),
    _CgsccpGttGtaAddrDisp_Type()
)
cgsccpGttGtaAddrDisp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttGtaAddrDisp.setStatus("current")
_CgsccpGttGtaAddrLen_Type = CItpTcGtaLongDisplayLen
_CgsccpGttGtaAddrLen_Object = MibTableColumn
cgsccpGttGtaAddrLen = _CgsccpGttGtaAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 12),
    _CgsccpGttGtaAddrLen_Type()
)
cgsccpGttGtaAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttGtaAddrLen.setStatus("current")
_CgsccpGttGtaAsName_Type = CItpTcXuaName
_CgsccpGttGtaAsName_Object = MibTableColumn
cgsccpGttGtaAsName = _CgsccpGttGtaAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 13),
    _CgsccpGttGtaAsName_Type()
)
cgsccpGttGtaAsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaAsName.setStatus("current")
_CgsccpGttGtaRowStatus_Type = RowStatus
_CgsccpGttGtaRowStatus_Object = MibTableColumn
cgsccpGttGtaRowStatus = _CgsccpGttGtaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 14),
    _CgsccpGttGtaRowStatus_Type()
)
cgsccpGttGtaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaRowStatus.setStatus("current")
_CgsccpGttGtaNetwork_Type = CItpTcNetworkName
_CgsccpGttGtaNetwork_Object = MibTableColumn
cgsccpGttGtaNetwork = _CgsccpGttGtaNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 6, 1, 1, 15),
    _CgsccpGttGtaNetwork_Type()
)
cgsccpGttGtaNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttGtaNetwork.setStatus("current")
_CgsccpGttAppGr_ObjectIdentity = ObjectIdentity
cgsccpGttAppGr = _CgsccpGttAppGr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7)
)
_CgsccpGttAppGrTable_Object = MibTable
cgsccpGttAppGrTable = _CgsccpGttAppGrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttAppGrTable.setStatus("deprecated")
_CgsccpGttAppGrTableEntry_Object = MibTableRow
cgsccpGttAppGrTableEntry = _CgsccpGttAppGrTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1)
)
cgsccpGttAppGrTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrName"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrCost"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrEntNum"),
)
if mibBuilder.loadTexts:
    cgsccpGttAppGrTableEntry.setStatus("deprecated")
_CgsccpGttAppGrName_Type = CgsccpGttAppName
_CgsccpGttAppGrName_Object = MibTableColumn
cgsccpGttAppGrName = _CgsccpGttAppGrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 1),
    _CgsccpGttAppGrName_Type()
)
cgsccpGttAppGrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttAppGrName.setStatus("deprecated")
_CgsccpGttAppGrCost_Type = CgsccpGttAppCost
_CgsccpGttAppGrCost_Object = MibTableColumn
cgsccpGttAppGrCost = _CgsccpGttAppGrCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 2),
    _CgsccpGttAppGrCost_Type()
)
cgsccpGttAppGrCost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttAppGrCost.setStatus("deprecated")


class _CgsccpGttAppGrEntNum_Type(Unsigned32):
    """Custom type cgsccpGttAppGrEntNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CgsccpGttAppGrEntNum_Type.__name__ = "Unsigned32"
_CgsccpGttAppGrEntNum_Object = MibTableColumn
cgsccpGttAppGrEntNum = _CgsccpGttAppGrEntNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 3),
    _CgsccpGttAppGrEntNum_Type()
)
cgsccpGttAppGrEntNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttAppGrEntNum.setStatus("deprecated")
_CgsccpGttAppGrType_Type = CgsccpGttAppType
_CgsccpGttAppGrType_Object = MibTableColumn
cgsccpGttAppGrType = _CgsccpGttAppGrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 4),
    _CgsccpGttAppGrType_Type()
)
cgsccpGttAppGrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrType.setStatus("deprecated")


class _CgsccpGttAppGrPc_Type(CItpTcPointCode):
    """Custom type cgsccpGttAppGrPc based on CItpTcPointCode"""
    defaultValue = 0


_CgsccpGttAppGrPc_Object = MibTableColumn
cgsccpGttAppGrPc = _CgsccpGttAppGrPc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 5),
    _CgsccpGttAppGrPc_Type()
)
cgsccpGttAppGrPc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrPc.setStatus("deprecated")


class _CgsccpGttAppGrSsn_Type(CItpTcSubSystemNumber):
    """Custom type cgsccpGttAppGrSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CgsccpGttAppGrSsn_Object = MibTableColumn
cgsccpGttAppGrSsn = _CgsccpGttAppGrSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 6),
    _CgsccpGttAppGrSsn_Type()
)
cgsccpGttAppGrSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrSsn.setStatus("deprecated")
_CgsccpGttAppGrRi_Type = CgsccpGttRoutingInd
_CgsccpGttAppGrRi_Object = MibTableColumn
cgsccpGttAppGrRi = _CgsccpGttAppGrRi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 7),
    _CgsccpGttAppGrRi_Type()
)
cgsccpGttAppGrRi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrRi.setStatus("deprecated")
_CgsccpGttAppGrMult_Type = CgsccpGttMultInd
_CgsccpGttAppGrMult_Object = MibTableColumn
cgsccpGttAppGrMult = _CgsccpGttAppGrMult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 8),
    _CgsccpGttAppGrMult_Type()
)
cgsccpGttAppGrMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrMult.setStatus("deprecated")


class _CgsccpGttAppGrRefCount_Type(Gauge32):
    """Custom type cgsccpGttAppGrRefCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CgsccpGttAppGrRefCount_Type.__name__ = "Gauge32"
_CgsccpGttAppGrRefCount_Object = MibTableColumn
cgsccpGttAppGrRefCount = _CgsccpGttAppGrRefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 9),
    _CgsccpGttAppGrRefCount_Type()
)
cgsccpGttAppGrRefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttAppGrRefCount.setStatus("deprecated")
_CgsccpGttAppGrAsName_Type = CItpTcXuaName
_CgsccpGttAppGrAsName_Object = MibTableColumn
cgsccpGttAppGrAsName = _CgsccpGttAppGrAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 10),
    _CgsccpGttAppGrAsName_Type()
)
cgsccpGttAppGrAsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrAsName.setStatus("deprecated")


class _CgsccpGttAppGrNewSsn_Type(CItpTcSubSystemNumber):
    """Custom type cgsccpGttAppGrNewSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CgsccpGttAppGrNewSsn_Object = MibTableColumn
cgsccpGttAppGrNewSsn = _CgsccpGttAppGrNewSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 11),
    _CgsccpGttAppGrNewSsn_Type()
)
cgsccpGttAppGrNewSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrNewSsn.setStatus("deprecated")
_CgsccpGttAppGrNumUsed_Type = Counter32
_CgsccpGttAppGrNumUsed_Object = MibTableColumn
cgsccpGttAppGrNumUsed = _CgsccpGttAppGrNumUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 12),
    _CgsccpGttAppGrNumUsed_Type()
)
cgsccpGttAppGrNumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttAppGrNumUsed.setStatus("deprecated")
_CgsccpGttAppGrRowStatus_Type = RowStatus
_CgsccpGttAppGrRowStatus_Object = MibTableColumn
cgsccpGttAppGrRowStatus = _CgsccpGttAppGrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 13),
    _CgsccpGttAppGrRowStatus_Type()
)
cgsccpGttAppGrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrRowStatus.setStatus("deprecated")
_CgsccpGttAppGrNetwork_Type = CItpTcNetworkName
_CgsccpGttAppGrNetwork_Object = MibTableColumn
cgsccpGttAppGrNetwork = _CgsccpGttAppGrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 7, 1, 1, 14),
    _CgsccpGttAppGrNetwork_Type()
)
cgsccpGttAppGrNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGrNetwork.setStatus("deprecated")
_CgsccpGttPref_ObjectIdentity = ObjectIdentity
cgsccpGttPref = _CgsccpGttPref_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8)
)
_CgsccpGttPrefTable_Object = MibTable
cgsccpGttPrefTable = _CgsccpGttPrefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttPrefTable.setStatus("deprecated")
_CgsccpGttPrefTableEntry_Object = MibTableRow
cgsccpGttPrefTableEntry = _CgsccpGttPrefTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1)
)
cgsccpGttPrefTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefName"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefInAddr"),
)
if mibBuilder.loadTexts:
    cgsccpGttPrefTableEntry.setStatus("deprecated")
_CgsccpGttPrefName_Type = CgsccpGttPrefName
_CgsccpGttPrefName_Object = MibTableColumn
cgsccpGttPrefName = _CgsccpGttPrefName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 1),
    _CgsccpGttPrefName_Type()
)
cgsccpGttPrefName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttPrefName.setStatus("deprecated")
_CgsccpGttPrefInAddr_Type = CItpTcGtaLongAddr
_CgsccpGttPrefInAddr_Object = MibTableColumn
cgsccpGttPrefInAddr = _CgsccpGttPrefInAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 2),
    _CgsccpGttPrefInAddr_Type()
)
cgsccpGttPrefInAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttPrefInAddr.setStatus("deprecated")
_CgsccpGttPrefOutAddr_Type = CItpTcGtaLongAddr
_CgsccpGttPrefOutAddr_Object = MibTableColumn
cgsccpGttPrefOutAddr = _CgsccpGttPrefOutAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 3),
    _CgsccpGttPrefOutAddr_Type()
)
cgsccpGttPrefOutAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPrefOutAddr.setStatus("deprecated")


class _CgsccpGttPrefTblNAI_Type(CItpTcNAI):
    """Custom type cgsccpGttPrefTblNAI based on CItpTcNAI"""
    defaultValue = 253


_CgsccpGttPrefTblNAI_Object = MibTableColumn
cgsccpGttPrefTblNAI = _CgsccpGttPrefTblNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 4),
    _CgsccpGttPrefTblNAI_Type()
)
cgsccpGttPrefTblNAI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPrefTblNAI.setStatus("deprecated")


class _CgsccpGttPrefTblNP_Type(CItpTcNumberingPlan):
    """Custom type cgsccpGttPrefTblNP based on CItpTcNumberingPlan"""
    defaultValue = 253


_CgsccpGttPrefTblNP_Object = MibTableColumn
cgsccpGttPrefTblNP = _CgsccpGttPrefTblNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 5),
    _CgsccpGttPrefTblNP_Type()
)
cgsccpGttPrefTblNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPrefTblNP.setStatus("deprecated")


class _CgsccpGttPrefItemNAI_Type(CItpTcNAI):
    """Custom type cgsccpGttPrefItemNAI based on CItpTcNAI"""
    defaultValue = 253


_CgsccpGttPrefItemNAI_Object = MibTableColumn
cgsccpGttPrefItemNAI = _CgsccpGttPrefItemNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 6),
    _CgsccpGttPrefItemNAI_Type()
)
cgsccpGttPrefItemNAI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPrefItemNAI.setStatus("deprecated")


class _CgsccpGttPrefItemNP_Type(CItpTcNumberingPlan):
    """Custom type cgsccpGttPrefItemNP based on CItpTcNumberingPlan"""
    defaultValue = 253


_CgsccpGttPrefItemNP_Object = MibTableColumn
cgsccpGttPrefItemNP = _CgsccpGttPrefItemNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 7),
    _CgsccpGttPrefItemNP_Type()
)
cgsccpGttPrefItemNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPrefItemNP.setStatus("deprecated")
_CgsccpGttPrefRowStatus_Type = RowStatus
_CgsccpGttPrefRowStatus_Object = MibTableColumn
cgsccpGttPrefRowStatus = _CgsccpGttPrefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 8, 1, 1, 8),
    _CgsccpGttPrefRowStatus_Type()
)
cgsccpGttPrefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPrefRowStatus.setStatus("deprecated")
_CgsccpGttTranslate_ObjectIdentity = ObjectIdentity
cgsccpGttTranslate = _CgsccpGttTranslate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9)
)
_CgsccpGttTranslateTable_Object = MibTable
cgsccpGttTranslateTable = _CgsccpGttTranslateTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttTranslateTable.setStatus("current")
_CgsccpGttTranslateTableEntry_Object = MibTableRow
cgsccpGttTranslateTableEntry = _CgsccpGttTranslateTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9, 1, 1)
)
cgsccpGttTranslateTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslateSlot"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslateEntry"),
)
if mibBuilder.loadTexts:
    cgsccpGttTranslateTableEntry.setStatus("current")


class _CgsccpGttTranslateSlot_Type(Unsigned32):
    """Custom type cgsccpGttTranslateSlot based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_CgsccpGttTranslateSlot_Type.__name__ = "Unsigned32"
_CgsccpGttTranslateSlot_Object = MibTableColumn
cgsccpGttTranslateSlot = _CgsccpGttTranslateSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9, 1, 1, 1),
    _CgsccpGttTranslateSlot_Type()
)
cgsccpGttTranslateSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttTranslateSlot.setStatus("current")


class _CgsccpGttTranslateEntry_Type(Unsigned32):
    """Custom type cgsccpGttTranslateEntry based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CgsccpGttTranslateEntry_Type.__name__ = "Unsigned32"
_CgsccpGttTranslateEntry_Object = MibTableColumn
cgsccpGttTranslateEntry = _CgsccpGttTranslateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9, 1, 1, 2),
    _CgsccpGttTranslateEntry_Type()
)
cgsccpGttTranslateEntry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttTranslateEntry.setStatus("current")


class _CgsccpGttTranslateRate_Type(Gauge32):
    """Custom type cgsccpGttTranslateRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CgsccpGttTranslateRate_Type.__name__ = "Gauge32"
_CgsccpGttTranslateRate_Object = MibTableColumn
cgsccpGttTranslateRate = _CgsccpGttTranslateRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9, 1, 1, 3),
    _CgsccpGttTranslateRate_Type()
)
cgsccpGttTranslateRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttTranslateRate.setStatus("current")
_CgsccpGttTranslateTS_Type = TimeStamp
_CgsccpGttTranslateTS_Object = MibTableColumn
cgsccpGttTranslateTS = _CgsccpGttTranslateTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9, 1, 1, 4),
    _CgsccpGttTranslateTS_Type()
)
cgsccpGttTranslateTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttTranslateTS.setStatus("current")
_CgsccpGttTranslatePhysicalIndex_Type = EntPhysicalIndexOrZero
_CgsccpGttTranslatePhysicalIndex_Object = MibTableColumn
cgsccpGttTranslatePhysicalIndex = _CgsccpGttTranslatePhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 9, 1, 1, 5),
    _CgsccpGttTranslatePhysicalIndex_Type()
)
cgsccpGttTranslatePhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttTranslatePhysicalIndex.setStatus("current")
_CgsccpGttPref2_ObjectIdentity = ObjectIdentity
cgsccpGttPref2 = _CgsccpGttPref2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10)
)
_CgsccpGttPref2Table_Object = MibTable
cgsccpGttPref2Table = _CgsccpGttPref2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttPref2Table.setStatus("current")
_CgsccpGttPref2TableEntry_Object = MibTableRow
cgsccpGttPref2TableEntry = _CgsccpGttPref2TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1)
)
cgsccpGttPref2TableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2Name"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2InAddr"),
)
if mibBuilder.loadTexts:
    cgsccpGttPref2TableEntry.setStatus("current")
_CgsccpGttPref2Name_Type = CgsccpGttPrefName
_CgsccpGttPref2Name_Object = MibTableColumn
cgsccpGttPref2Name = _CgsccpGttPref2Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 1),
    _CgsccpGttPref2Name_Type()
)
cgsccpGttPref2Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttPref2Name.setStatus("current")
_CgsccpGttPref2InAddr_Type = CItpTcGtaLongAddr
_CgsccpGttPref2InAddr_Object = MibTableColumn
cgsccpGttPref2InAddr = _CgsccpGttPref2InAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 2),
    _CgsccpGttPref2InAddr_Type()
)
cgsccpGttPref2InAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttPref2InAddr.setStatus("current")
_CgsccpGttPref2OutAddr_Type = CItpTcGtaLongAddr
_CgsccpGttPref2OutAddr_Object = MibTableColumn
cgsccpGttPref2OutAddr = _CgsccpGttPref2OutAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 3),
    _CgsccpGttPref2OutAddr_Type()
)
cgsccpGttPref2OutAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPref2OutAddr.setStatus("current")


class _CgsccpGttPref2TblNAI_Type(CItpTcNAI):
    """Custom type cgsccpGttPref2TblNAI based on CItpTcNAI"""
    defaultValue = 253


_CgsccpGttPref2TblNAI_Object = MibTableColumn
cgsccpGttPref2TblNAI = _CgsccpGttPref2TblNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 4),
    _CgsccpGttPref2TblNAI_Type()
)
cgsccpGttPref2TblNAI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPref2TblNAI.setStatus("current")


class _CgsccpGttPref2TblNP_Type(CItpTcNumberingPlan):
    """Custom type cgsccpGttPref2TblNP based on CItpTcNumberingPlan"""
    defaultValue = 253


_CgsccpGttPref2TblNP_Object = MibTableColumn
cgsccpGttPref2TblNP = _CgsccpGttPref2TblNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 5),
    _CgsccpGttPref2TblNP_Type()
)
cgsccpGttPref2TblNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPref2TblNP.setStatus("current")


class _CgsccpGttPref2ItemNAI_Type(CItpTcNAI):
    """Custom type cgsccpGttPref2ItemNAI based on CItpTcNAI"""
    defaultValue = 253


_CgsccpGttPref2ItemNAI_Object = MibTableColumn
cgsccpGttPref2ItemNAI = _CgsccpGttPref2ItemNAI_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 6),
    _CgsccpGttPref2ItemNAI_Type()
)
cgsccpGttPref2ItemNAI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPref2ItemNAI.setStatus("current")


class _CgsccpGttPref2ItemNP_Type(CItpTcNumberingPlan):
    """Custom type cgsccpGttPref2ItemNP based on CItpTcNumberingPlan"""
    defaultValue = 253


_CgsccpGttPref2ItemNP_Object = MibTableColumn
cgsccpGttPref2ItemNP = _CgsccpGttPref2ItemNP_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 7),
    _CgsccpGttPref2ItemNP_Type()
)
cgsccpGttPref2ItemNP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPref2ItemNP.setStatus("current")
_CgsccpGttPref2RowStatus_Type = RowStatus
_CgsccpGttPref2RowStatus_Object = MibTableColumn
cgsccpGttPref2RowStatus = _CgsccpGttPref2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 8),
    _CgsccpGttPref2RowStatus_Type()
)
cgsccpGttPref2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPref2RowStatus.setStatus("current")


class _CgsccpGttPref2EncodingScheme_Type(Integer32):
    """Custom type cgsccpGttPref2EncodingScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bcdEven", 2),
          ("bcdOdd", 1),
          ("national", 3),
          ("unknown", 0))
    )


_CgsccpGttPref2EncodingScheme_Type.__name__ = "Integer32"
_CgsccpGttPref2EncodingScheme_Object = MibTableColumn
cgsccpGttPref2EncodingScheme = _CgsccpGttPref2EncodingScheme_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 10, 1, 1, 9),
    _CgsccpGttPref2EncodingScheme_Type()
)
cgsccpGttPref2EncodingScheme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttPref2EncodingScheme.setStatus("current")
_CgsccpGttAppGr2_ObjectIdentity = ObjectIdentity
cgsccpGttAppGr2 = _CgsccpGttAppGr2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11)
)
_CgsccpGttAppGr2Table_Object = MibTable
cgsccpGttAppGr2Table = _CgsccpGttAppGr2Table_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Table.setStatus("current")
_CgsccpGttAppGr2TableEntry_Object = MibTableRow
cgsccpGttAppGr2TableEntry = _CgsccpGttAppGr2TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1)
)
cgsccpGttAppGr2TableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Name"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2EntNum"),
)
if mibBuilder.loadTexts:
    cgsccpGttAppGr2TableEntry.setStatus("current")
_CgsccpGttAppGr2Name_Type = CgsccpGttAppName
_CgsccpGttAppGr2Name_Object = MibTableColumn
cgsccpGttAppGr2Name = _CgsccpGttAppGr2Name_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 1),
    _CgsccpGttAppGr2Name_Type()
)
cgsccpGttAppGr2Name.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Name.setStatus("current")
_CgsccpGttAppGr2EntNum_Type = Unsigned32
_CgsccpGttAppGr2EntNum_Object = MibTableColumn
cgsccpGttAppGr2EntNum = _CgsccpGttAppGr2EntNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 2),
    _CgsccpGttAppGr2EntNum_Type()
)
cgsccpGttAppGr2EntNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2EntNum.setStatus("current")
_CgsccpGttAppGr2Mult_Type = CgsccpGttMultInd
_CgsccpGttAppGr2Mult_Object = MibTableColumn
cgsccpGttAppGr2Mult = _CgsccpGttAppGr2Mult_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 3),
    _CgsccpGttAppGr2Mult_Type()
)
cgsccpGttAppGr2Mult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Mult.setStatus("current")
_CgsccpGttAppGr2Type_Type = CgsccpGttAppType
_CgsccpGttAppGr2Type_Object = MibTableColumn
cgsccpGttAppGr2Type = _CgsccpGttAppGr2Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 4),
    _CgsccpGttAppGr2Type_Type()
)
cgsccpGttAppGr2Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Type.setStatus("current")
_CgsccpGttAppGr2Cost_Type = CgsccpGttAppCost
_CgsccpGttAppGr2Cost_Object = MibTableColumn
cgsccpGttAppGr2Cost = _CgsccpGttAppGr2Cost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 5),
    _CgsccpGttAppGr2Cost_Type()
)
cgsccpGttAppGr2Cost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Cost.setStatus("current")


class _CgsccpGttAppGr2Weight_Type(Unsigned32):
    """Custom type cgsccpGttAppGr2Weight based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_CgsccpGttAppGr2Weight_Type.__name__ = "Unsigned32"
_CgsccpGttAppGr2Weight_Object = MibTableColumn
cgsccpGttAppGr2Weight = _CgsccpGttAppGr2Weight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 6),
    _CgsccpGttAppGr2Weight_Type()
)
cgsccpGttAppGr2Weight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Weight.setStatus("current")


class _CgsccpGttAppGr2Pc_Type(CItpTcPointCode):
    """Custom type cgsccpGttAppGr2Pc based on CItpTcPointCode"""
    defaultValue = 0


_CgsccpGttAppGr2Pc_Object = MibTableColumn
cgsccpGttAppGr2Pc = _CgsccpGttAppGr2Pc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 7),
    _CgsccpGttAppGr2Pc_Type()
)
cgsccpGttAppGr2Pc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Pc.setStatus("current")


class _CgsccpGttAppGr2Ssn_Type(CItpTcSubSystemNumber):
    """Custom type cgsccpGttAppGr2Ssn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CgsccpGttAppGr2Ssn_Object = MibTableColumn
cgsccpGttAppGr2Ssn = _CgsccpGttAppGr2Ssn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 8),
    _CgsccpGttAppGr2Ssn_Type()
)
cgsccpGttAppGr2Ssn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Ssn.setStatus("current")
_CgsccpGttAppGr2Ri_Type = CgsccpGttRoutingInd
_CgsccpGttAppGr2Ri_Object = MibTableColumn
cgsccpGttAppGr2Ri = _CgsccpGttAppGr2Ri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 9),
    _CgsccpGttAppGr2Ri_Type()
)
cgsccpGttAppGr2Ri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Ri.setStatus("current")


class _CgsccpGttAppGr2RefCount_Type(Gauge32):
    """Custom type cgsccpGttAppGr2RefCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CgsccpGttAppGr2RefCount_Type.__name__ = "Gauge32"
_CgsccpGttAppGr2RefCount_Object = MibTableColumn
cgsccpGttAppGr2RefCount = _CgsccpGttAppGr2RefCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 10),
    _CgsccpGttAppGr2RefCount_Type()
)
cgsccpGttAppGr2RefCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2RefCount.setStatus("current")
_CgsccpGttAppGr2AsName_Type = CItpTcXuaName
_CgsccpGttAppGr2AsName_Object = MibTableColumn
cgsccpGttAppGr2AsName = _CgsccpGttAppGr2AsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 11),
    _CgsccpGttAppGr2AsName_Type()
)
cgsccpGttAppGr2AsName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2AsName.setStatus("current")


class _CgsccpGttAppGr2NewSsn_Type(CItpTcSubSystemNumber):
    """Custom type cgsccpGttAppGr2NewSsn based on CItpTcSubSystemNumber"""
    defaultValue = 0


_CgsccpGttAppGr2NewSsn_Object = MibTableColumn
cgsccpGttAppGr2NewSsn = _CgsccpGttAppGr2NewSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 12),
    _CgsccpGttAppGr2NewSsn_Type()
)
cgsccpGttAppGr2NewSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2NewSsn.setStatus("current")
_CgsccpGttAppGr2NumUsed_Type = Counter32
_CgsccpGttAppGr2NumUsed_Object = MibTableColumn
cgsccpGttAppGr2NumUsed = _CgsccpGttAppGr2NumUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 13),
    _CgsccpGttAppGr2NumUsed_Type()
)
cgsccpGttAppGr2NumUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2NumUsed.setStatus("current")
_CgsccpGttAppGr2Network_Type = CItpTcNetworkName
_CgsccpGttAppGr2Network_Object = MibTableColumn
cgsccpGttAppGr2Network = _CgsccpGttAppGr2Network_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 14),
    _CgsccpGttAppGr2Network_Type()
)
cgsccpGttAppGr2Network.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2Network.setStatus("current")
_CgsccpGttAppGr2RowStatus_Type = RowStatus
_CgsccpGttAppGr2RowStatus_Object = MibTableColumn
cgsccpGttAppGr2RowStatus = _CgsccpGttAppGr2RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 11, 1, 1, 15),
    _CgsccpGttAppGr2RowStatus_Type()
)
cgsccpGttAppGr2RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cgsccpGttAppGr2RowStatus.setStatus("current")
_CgsccpGttErrors_ObjectIdentity = ObjectIdentity
cgsccpGttErrors = _CgsccpGttErrors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12)
)
_CgsccpGttErrorsTable_Object = MibTable
cgsccpGttErrorsTable = _CgsccpGttErrorsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cgsccpGttErrorsTable.setStatus("current")
_CgsccpGttErrorsTableEntry_Object = MibTableRow
cgsccpGttErrorsTableEntry = _CgsccpGttErrorsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1)
)
cgsccpGttErrorsTableEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
)
if mibBuilder.loadTexts:
    cgsccpGttErrorsTableEntry.setStatus("current")
_CgsccpGttErrorsSelectorNotFound_Type = Gauge32
_CgsccpGttErrorsSelectorNotFound_Object = MibTableColumn
cgsccpGttErrorsSelectorNotFound = _CgsccpGttErrorsSelectorNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 1),
    _CgsccpGttErrorsSelectorNotFound_Type()
)
cgsccpGttErrorsSelectorNotFound.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSelectorNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSelectorNotFound.setUnits("packets")
_CgsccpGttErrorsIncorrectFormat_Type = Gauge32
_CgsccpGttErrorsIncorrectFormat_Object = MibTableColumn
cgsccpGttErrorsIncorrectFormat = _CgsccpGttErrorsIncorrectFormat_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 2),
    _CgsccpGttErrorsIncorrectFormat_Type()
)
cgsccpGttErrorsIncorrectFormat.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsIncorrectFormat.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsIncorrectFormat.setUnits("packets")
_CgsccpGttErrorsGtaNotFound_Type = Gauge32
_CgsccpGttErrorsGtaNotFound_Object = MibTableColumn
cgsccpGttErrorsGtaNotFound = _CgsccpGttErrorsGtaNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 3),
    _CgsccpGttErrorsGtaNotFound_Type()
)
cgsccpGttErrorsGtaNotFound.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsGtaNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsGtaNotFound.setUnits("packets")
_CgsccpGttErrorsHopViolation_Type = Gauge32
_CgsccpGttErrorsHopViolation_Object = MibTableColumn
cgsccpGttErrorsHopViolation = _CgsccpGttErrorsHopViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 4),
    _CgsccpGttErrorsHopViolation_Type()
)
cgsccpGttErrorsHopViolation.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsHopViolation.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsHopViolation.setUnits("packets")
_CgsccpGttErrorsMapNotFound_Type = Gauge32
_CgsccpGttErrorsMapNotFound_Object = MibTableColumn
cgsccpGttErrorsMapNotFound = _CgsccpGttErrorsMapNotFound_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 5),
    _CgsccpGttErrorsMapNotFound_Type()
)
cgsccpGttErrorsMapNotFound.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsMapNotFound.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsMapNotFound.setUnits("packets")
_CgsccpGttErrorsUnequipedSS_Type = Gauge32
_CgsccpGttErrorsUnequipedSS_Object = MibTableColumn
cgsccpGttErrorsUnequipedSS = _CgsccpGttErrorsUnequipedSS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 6),
    _CgsccpGttErrorsUnequipedSS_Type()
)
cgsccpGttErrorsUnequipedSS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsUnequipedSS.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsUnequipedSS.setUnits("packets")
_CgsccpGttErrorsSccpUnavailable_Type = Gauge32
_CgsccpGttErrorsSccpUnavailable_Object = MibTableColumn
cgsccpGttErrorsSccpUnavailable = _CgsccpGttErrorsSccpUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 7),
    _CgsccpGttErrorsSccpUnavailable_Type()
)
cgsccpGttErrorsSccpUnavailable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSccpUnavailable.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSccpUnavailable.setUnits("packets")
_CgsccpGttErrorsDpcUnavailable_Type = Gauge32
_CgsccpGttErrorsDpcUnavailable_Object = MibTableColumn
cgsccpGttErrorsDpcUnavailable = _CgsccpGttErrorsDpcUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 8),
    _CgsccpGttErrorsDpcUnavailable_Type()
)
cgsccpGttErrorsDpcUnavailable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsDpcUnavailable.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsDpcUnavailable.setUnits("packets")
_CgsccpGttErrorsSsUnavailable_Type = Gauge32
_CgsccpGttErrorsSsUnavailable_Object = MibTableColumn
cgsccpGttErrorsSsUnavailable = _CgsccpGttErrorsSsUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 9),
    _CgsccpGttErrorsSsUnavailable_Type()
)
cgsccpGttErrorsSsUnavailable.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSsUnavailable.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSsUnavailable.setUnits("packets")
_CgsccpGttErrorsDpcCongested_Type = Gauge32
_CgsccpGttErrorsDpcCongested_Object = MibTableColumn
cgsccpGttErrorsDpcCongested = _CgsccpGttErrorsDpcCongested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 10),
    _CgsccpGttErrorsDpcCongested_Type()
)
cgsccpGttErrorsDpcCongested.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsDpcCongested.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsDpcCongested.setUnits("packets")
_CgsccpGttErrorsSsCongested_Type = Gauge32
_CgsccpGttErrorsSsCongested_Object = MibTableColumn
cgsccpGttErrorsSsCongested = _CgsccpGttErrorsSsCongested_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 11),
    _CgsccpGttErrorsSsCongested_Type()
)
cgsccpGttErrorsSsCongested.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSsCongested.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSsCongested.setUnits("packets")
_CgsccpGttErrorsRouteFailure_Type = Gauge32
_CgsccpGttErrorsRouteFailure_Object = MibTableColumn
cgsccpGttErrorsRouteFailure = _CgsccpGttErrorsRouteFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 12),
    _CgsccpGttErrorsRouteFailure_Type()
)
cgsccpGttErrorsRouteFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsRouteFailure.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsRouteFailure.setUnits("packets")
_CgsccpGttErrorsSccpUnqualified_Type = Gauge32
_CgsccpGttErrorsSccpUnqualified_Object = MibTableColumn
cgsccpGttErrorsSccpUnqualified = _CgsccpGttErrorsSccpUnqualified_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 13),
    _CgsccpGttErrorsSccpUnqualified_Type()
)
cgsccpGttErrorsSccpUnqualified.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSccpUnqualified.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSccpUnqualified.setUnits("packets")
_CgsccpGttErrorsReassUnsupported_Type = Gauge32
_CgsccpGttErrorsReassUnsupported_Object = MibTableColumn
cgsccpGttErrorsReassUnsupported = _CgsccpGttErrorsReassUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 14),
    _CgsccpGttErrorsReassUnsupported_Type()
)
cgsccpGttErrorsReassUnsupported.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsReassUnsupported.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsReassUnsupported.setUnits("packets")
_CgsccpGttErrorsReassFailure_Type = Gauge32
_CgsccpGttErrorsReassFailure_Object = MibTableColumn
cgsccpGttErrorsReassFailure = _CgsccpGttErrorsReassFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 15),
    _CgsccpGttErrorsReassFailure_Type()
)
cgsccpGttErrorsReassFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsReassFailure.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsReassFailure.setUnits("packets")
_CgsccpGttErrorsSegUnsupported_Type = Gauge32
_CgsccpGttErrorsSegUnsupported_Object = MibTableColumn
cgsccpGttErrorsSegUnsupported = _CgsccpGttErrorsSegUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 16),
    _CgsccpGttErrorsSegUnsupported_Type()
)
cgsccpGttErrorsSegUnsupported.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSegUnsupported.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSegUnsupported.setUnits("packets")
_CgsccpGttErrorsSegFailure_Type = Gauge32
_CgsccpGttErrorsSegFailure_Object = MibTableColumn
cgsccpGttErrorsSegFailure = _CgsccpGttErrorsSegFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 12, 1, 1, 17),
    _CgsccpGttErrorsSegFailure_Type()
)
cgsccpGttErrorsSegFailure.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSegFailure.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpGttErrorsSegFailure.setUnits("packets")
_CgsccpSSN_ObjectIdentity = ObjectIdentity
cgsccpSSN = _CgsccpSSN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 13)
)
_CgsccpSSNTable_Object = MibTable
cgsccpSSNTable = _CgsccpSSNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cgsccpSSNTable.setStatus("current")
_CgsccpSSNEntry_Object = MibTableRow
cgsccpSSNEntry = _CgsccpSSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 13, 1, 1)
)
cgsccpSSNEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpSsn"),
)
if mibBuilder.loadTexts:
    cgsccpSSNEntry.setStatus("current")
_CgsccpSsn_Type = CItpTcSubSystemNumber
_CgsccpSsn_Object = MibTableColumn
cgsccpSsn = _CgsccpSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 13, 1, 1, 1),
    _CgsccpSsn_Type()
)
cgsccpSsn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpSsn.setStatus("current")
_CgsccpSSNNumProhibits_Type = Counter32
_CgsccpSSNNumProhibits_Object = MibTableColumn
cgsccpSSNNumProhibits = _CgsccpSSNNumProhibits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 13, 1, 1, 2),
    _CgsccpSSNNumProhibits_Type()
)
cgsccpSSNNumProhibits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNNumProhibits.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNNumProhibits.setUnits("occurrences")
_CgsccpSSNNumAllows_Type = Counter32
_CgsccpSSNNumAllows_Object = MibTableColumn
cgsccpSSNNumAllows = _CgsccpSSNNumAllows_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 13, 1, 1, 3),
    _CgsccpSSNNumAllows_Type()
)
cgsccpSSNNumAllows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNNumAllows.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNNumAllows.setUnits("occurrences")
_CgsccpClassSsn_ObjectIdentity = ObjectIdentity
cgsccpClassSsn = _CgsccpClassSsn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14)
)
_CgsccpSSNClassTable_Object = MibTable
cgsccpSSNClassTable = _CgsccpSSNClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1)
)
if mibBuilder.loadTexts:
    cgsccpSSNClassTable.setStatus("current")
_CgsccpSSNClassEntry_Object = MibTableRow
cgsccpSSNClassEntry = _CgsccpSSNClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1)
)
cgsccpSSNClassEntry.setIndexNames(
    (0, "CISCO-ITP-GSP-MIB", "cgspInstNetwork"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpSsn"),
    (0, "CISCO-ITP-GSCCP-MIB", "cgsccpClassIdx"),
)
if mibBuilder.loadTexts:
    cgsccpSSNClassEntry.setStatus("current")
_CgsccpClassIdx_Type = CgsccpClass
_CgsccpClassIdx_Object = MibTableColumn
cgsccpClassIdx = _CgsccpClassIdx_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1, 1),
    _CgsccpClassIdx_Type()
)
cgsccpClassIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cgsccpClassIdx.setStatus("current")
_CgsccpSSNClassUDTMsgsSent_Type = Counter32
_CgsccpSSNClassUDTMsgsSent_Object = MibTableColumn
cgsccpSSNClassUDTMsgsSent = _CgsccpSSNClassUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1, 2),
    _CgsccpSSNClassUDTMsgsSent_Type()
)
cgsccpSSNClassUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNClassUDTMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNClassUDTMsgsSent.setUnits("packets")
_CgsccpSSNClassUDTMsgsRcvd_Type = Counter32
_CgsccpSSNClassUDTMsgsRcvd_Object = MibTableColumn
cgsccpSSNClassUDTMsgsRcvd = _CgsccpSSNClassUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1, 3),
    _CgsccpSSNClassUDTMsgsRcvd_Type()
)
cgsccpSSNClassUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNClassUDTMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNClassUDTMsgsRcvd.setUnits("packets")
_CgsccpSSNClassXUDTMsgsSent_Type = Counter32
_CgsccpSSNClassXUDTMsgsSent_Object = MibTableColumn
cgsccpSSNClassXUDTMsgsSent = _CgsccpSSNClassXUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1, 4),
    _CgsccpSSNClassXUDTMsgsSent_Type()
)
cgsccpSSNClassXUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNClassXUDTMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNClassXUDTMsgsSent.setUnits("packets")
_CgsccpSSNClassXUDTMsgsRcvd_Type = Counter32
_CgsccpSSNClassXUDTMsgsRcvd_Object = MibTableColumn
cgsccpSSNClassXUDTMsgsRcvd = _CgsccpSSNClassXUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1, 5),
    _CgsccpSSNClassXUDTMsgsRcvd_Type()
)
cgsccpSSNClassXUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNClassXUDTMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNClassXUDTMsgsRcvd.setUnits("packets")
_CgsccpSSNClassLUDTMsgsSent_Type = Counter32
_CgsccpSSNClassLUDTMsgsSent_Object = MibTableColumn
cgsccpSSNClassLUDTMsgsSent = _CgsccpSSNClassLUDTMsgsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1, 6),
    _CgsccpSSNClassLUDTMsgsSent_Type()
)
cgsccpSSNClassLUDTMsgsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNClassLUDTMsgsSent.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNClassLUDTMsgsSent.setUnits("packets")
_CgsccpSSNClassLUDTMsgsRcvd_Type = Counter32
_CgsccpSSNClassLUDTMsgsRcvd_Object = MibTableColumn
cgsccpSSNClassLUDTMsgsRcvd = _CgsccpSSNClassLUDTMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 14, 1, 1, 7),
    _CgsccpSSNClassLUDTMsgsRcvd_Type()
)
cgsccpSSNClassLUDTMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cgsccpSSNClassLUDTMsgsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpSSNClassLUDTMsgsRcvd.setUnits("packets")
_CgsccpNotificationsInfo_ObjectIdentity = ObjectIdentity
cgsccpNotificationsInfo = _CgsccpNotificationsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 15)
)
_CgsccpLocalDisplaySS_Type = Unsigned32
_CgsccpLocalDisplaySS_Object = MibScalar
cgsccpLocalDisplaySS = _CgsccpLocalDisplaySS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 15, 1),
    _CgsccpLocalDisplaySS_Type()
)
cgsccpLocalDisplaySS.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpLocalDisplaySS.setStatus("current")
if mibBuilder.loadTexts:
    cgsccpLocalDisplaySS.setUnits("seconds")
_CgsccpLocalSsStatus_Type = CgsccpGttMapSsStatus
_CgsccpLocalSsStatus_Object = MibScalar
cgsccpLocalSsStatus = _CgsccpLocalSsStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 1, 15, 2),
    _CgsccpLocalSsStatus_Type()
)
cgsccpLocalSsStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cgsccpLocalSsStatus.setStatus("current")
_CiscoGsccpMIBConform_ObjectIdentity = ObjectIdentity
ciscoGsccpMIBConform = _CiscoGsccpMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2)
)
_CiscoGsccpMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoGsccpMIBCompliances = _CiscoGsccpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1)
)
_CiscoGsccpMIBGroups_ObjectIdentity = ObjectIdentity
ciscoGsccpMIBGroups = _CiscoGsccpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2)
)

# Managed Objects groups

ciscoGsccpGlobalEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 1)
)
ciscoGsccpGlobalEntryGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslateSample"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslatePeriod"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslateRate"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapStateNotifEnabled"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttLoadTableNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGlobalEntryGroup.setStatus("deprecated")

ciscoGsccpInstTableEntryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 2)
)
ciscoGsccpInstTableEntryGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpInstTotalMsgs"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLocalMsgs"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstTotalGttMsgs"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTSMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTSMsgsAttempted"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTSMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTSMsgsAttempted"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTSMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTSMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTSMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTSMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrefToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrefFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstRsrToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstRsrFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstErrToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstErrFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstQ752T7E1"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstInvalidGttFormat"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstQ752T7E13"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstMapNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstQ752T7E7"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstGttConfigStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstConfigTS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstGttConfigTS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLastURL"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstConPcTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstMapTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstGtaTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstSelTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstAppGrTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpInstTableEntryGroup.setStatus("deprecated")

ciscoGsccpGttConPcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 3)
)
ciscoGsccpGttConPcGroup.setObjects(
    ("CISCO-ITP-GSCCP-MIB", "cgsccpGttConPcRowStatus")
)
if mibBuilder.loadTexts:
    ciscoGsccpGttConPcGroup.setStatus("current")

ciscoGsccpGttAppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 4)
)
ciscoGsccpGttAppGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrType"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrPc"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrSsn"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrRi"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrMult"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrRefCount"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrAsName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrNewSsn"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrNumUsed"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttAppGroup.setStatus("deprecated")

ciscoGsccpGttMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 5)
)
ciscoGsccpGttMapGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapDisplayPC"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapDisplaySS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapType"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapPcStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapSsStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapMultInd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapBackupPc"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapBackupSsn"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapConPcList"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapReRouteOnCong"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapAdjacent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapLastSsUsed"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapUsed"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapAltUsed"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapSccpUnavail"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapQ752T7E3Fail"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapQ752T7E3Un"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapQ752T7E4"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapQ752T7E5"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapQ752T7E6"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapRefCount"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttMapGroup.setStatus("current")

ciscoGsccpGttSelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 6)
)
ciscoGsccpGttSelGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttSelName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttSelNumPerf"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttQ752T7E2"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttSelQOS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttSelRefCount"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttSelPrePrefConv"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttSelPostPrefConv"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttSelRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttSelGroup.setStatus("current")

ciscoGsccpGttGtaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 7)
)
ciscoGsccpGttGtaGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaSelName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResType"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResPc"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResMap"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResAppGroup"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaTTorSSN"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaTTorSSNvalue"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaRoutingInd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaQOS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaAddrDisp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaAddrLen"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaAsName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttGtaGroup.setStatus("deprecated")

ciscoGsccpGttPrefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 8)
)
ciscoGsccpGttPrefGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefOutAddr"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefTblNAI"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefTblNP"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefItemNAI"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefItemNP"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPrefRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttPrefGroup.setStatus("deprecated")

ciscoGsccpGttPrefGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 10)
)
ciscoGsccpGttPrefGroupRev1.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2OutAddr"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2TblNAI"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2TblNP"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2ItemNAI"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2ItemNP"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2RowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttPrefGroupRev1.setStatus("current")

ciscoGsccpInstTableEntryGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 11)
)
ciscoGsccpInstTableEntryGroupRev1.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpInstTotalMsgs"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLocalMsgs"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstTotalGttMsgs"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTSMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTSMsgsAttempted"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstUDTSMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTSMsgsAttempted"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTSMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstXUDTSMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTSMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLUDTSMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrefToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstCrefFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstRsrToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstRsrFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstErrToMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstErrFromMtp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstQ752T7E1"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstInvalidGttFormat"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstQ752T7E13"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstMapNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstQ752T7E7"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstGttConfigStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstConfigTS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstGttConfigTS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLastURL"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstConPcTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstMapTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstGtaTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstSelTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstAppGrTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstRowStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstPrefTableEntries"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstQ752Unqualified"))
)
if mibBuilder.loadTexts:
    ciscoGsccpInstTableEntryGroupRev1.setStatus("current")

ciscoGsccpGlobalEntryGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 12)
)
ciscoGsccpGlobalEntryGroupRev1.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslateSample"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslatePeriod"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslateRate"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapStateNotifEnabled"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttLoadTableNotifEnabled"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslateTS"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGlobalEntryGroupRev1.setStatus("current")

ciscoGsccpGttAppGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 13)
)
ciscoGsccpGttAppGroupRev2.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrType"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrPc"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrSsn"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrRi"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrMult"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrRefCount"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrAsName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrNewSsn"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrNumUsed"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrRowStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGrNetwork"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttAppGroupRev2.setStatus("deprecated")

ciscoGsccpGttGtaGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 14)
)
ciscoGsccpGttGtaGroupRev2.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaSelName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResType"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResPc"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResMap"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaResAppGroup"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaTTorSSN"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaTTorSSNvalue"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaRoutingInd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaQOS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaAddrDisp"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaAddrLen"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaAsName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaRowStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttGtaNetwork"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttGtaGroupRev2.setStatus("current")

ciscoGsccpGttAppGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 15)
)
ciscoGsccpGttAppGroupRev3.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Mult"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Type"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Cost"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Weight"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Pc"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Ssn"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Ri"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2RefCount"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2AsName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2NewSsn"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2NumUsed"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2Network"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttAppGr2RowStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttAppGroupRev3.setStatus("current")

ciscoGsccpGttErrorsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 17)
)
ciscoGsccpGttErrorsGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorPeriod"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorRecoveryCount"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstErrorIndicator"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttTransErrorsNotifEnabled"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSelectorNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsIncorrectFormat"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsGtaNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsHopViolation"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsMapNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsUnequipedSS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSccpUnavailable"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsDpcUnavailable"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSsUnavailable"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsDpcCongested"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSsCongested"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsRouteFailure"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSccpUnqualified"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttErrorsGroup.setStatus("current")

ciscoGsccpGttPrefGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 18)
)
ciscoGsccpGttPrefGroupSup1.setObjects(
    ("CISCO-ITP-GSCCP-MIB", "cgsccpGttPref2EncodingScheme")
)
if mibBuilder.loadTexts:
    ciscoGsccpGttPrefGroupSup1.setStatus("current")

ciscoGsccpGlobalEntryGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 19)
)
ciscoGsccpGlobalEntryGroupSup1.setObjects(
    ("CISCO-ITP-GSCCP-MIB", "cgsccpGttTranslatePhysicalIndex")
)
if mibBuilder.loadTexts:
    ciscoGsccpGlobalEntryGroupSup1.setStatus("current")

ciscoGsccpInstTableEntryGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 20)
)
ciscoGsccpInstTableEntryGroupSup1.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpInstReassUnsup"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstReassFail"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstSegUnsup"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstSegFail"))
)
if mibBuilder.loadTexts:
    ciscoGsccpInstTableEntryGroupSup1.setStatus("current")

ciscoGsccpGttMapGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 21)
)
ciscoGsccpGttMapGroupSup1.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongLvl1"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongLvl2"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongLvl3"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapSSPRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapSSARcvd"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttMapGroupSup1.setStatus("current")

ciscoGsccpGttErrorsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 22)
)
ciscoGsccpGttErrorsGroupSup1.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsReassUnsupported"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsReassFailure"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSegUnsupported"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSegFailure"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttErrorsGroupSup1.setStatus("current")

ciscoGsccpGttSsnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 23)
)
ciscoGsccpGttSsnGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpSSNNumProhibits"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpSSNNumAllows"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttSsnGroup.setStatus("current")

ciscoGsccpGttSsnClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 24)
)
ciscoGsccpGttSsnClassGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpSSNClassUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpSSNClassUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpSSNClassXUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpSSNClassXUDTMsgsRcvd"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpSSNClassLUDTMsgsSent"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpSSNClassLUDTMsgsRcvd"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttSsnClassGroup.setStatus("current")

ciscoGsccpNotificationsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 25)
)
ciscoGsccpNotificationsInfoGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpLocalDisplaySS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpLocalSsStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpNotificationsInfoGroup.setStatus("current")

ciscoGsccpGttSelGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 27)
)
ciscoGsccpGttSelGroupSup1.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "cgsccpGttNextSelName"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttNextSelRefed"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttSelGroupSup1.setStatus("current")


# Notification objects

ciscoGsccpGttMapStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0, 1)
)
ciscoGsccpGttMapStateChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapDisplayPC"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapDisplaySS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapSsStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttMapStateChange.setStatus(
        "current"
    )

ciscoGsccpGttLoadTable = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0, 2)
)
ciscoGsccpGttLoadTable.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstGttConfigStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstLastURL"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttLoadTable.setStatus(
        "current"
    )

ciscoGsccpGttErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0, 3)
)
ciscoGsccpGttErrors.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstErrorIndicator"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSelectorNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsIncorrectFormat"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsGtaNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsHopViolation"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsMapNotFound"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsUnequipedSS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSccpUnavailable"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsDpcUnavailable"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSsUnavailable"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsDpcCongested"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSsCongested"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsRouteFailure"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSccpUnqualified"))
)
if mibBuilder.loadTexts:
    ciscoGsccpGttErrors.setStatus(
        "current"
    )

ciscoGsccpSegReassUnsup = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0, 4)
)
ciscoGsccpSegReassUnsup.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpInstErrorIndicator"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsReassUnsupported"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsReassFailure"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSegUnsupported"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttErrorsSegFailure"))
)
if mibBuilder.loadTexts:
    ciscoGsccpSegReassUnsup.setStatus(
        "current"
    )

ciscoGsccpSOGReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0, 5)
)
ciscoGsccpSOGReceived.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapDisplayPC"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapDisplaySS"))
)
if mibBuilder.loadTexts:
    ciscoGsccpSOGReceived.setStatus(
        "current"
    )

ciscoGsccpRmtCongestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0, 6)
)
ciscoGsccpRmtCongestion.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapDisplayPC"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongStatus"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongLvl1"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongLvl2"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpGttMapCongLvl3"))
)
if mibBuilder.loadTexts:
    ciscoGsccpRmtCongestion.setStatus(
        "current"
    )

ciscoGsccpLocalSsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 0, 7)
)
ciscoGsccpLocalSsStateChange.setObjects(
      *(("CISCO-ITP-GSP-MIB", "cgspEventSequenceNumber"),
        ("CISCO-ITP-GSP-MIB", "cgspCLLICode"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpLocalDisplaySS"),
        ("CISCO-ITP-GSCCP-MIB", "cgsccpLocalSsStatus"))
)
if mibBuilder.loadTexts:
    ciscoGsccpLocalSsStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoGsccpNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 9)
)
ciscoGsccpNotificationsGroup.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "ciscoGsccpGttMapStateChange"),
        ("CISCO-ITP-GSCCP-MIB", "ciscoGsccpGttLoadTable"))
)
if mibBuilder.loadTexts:
    ciscoGsccpNotificationsGroup.setStatus(
        "current"
    )

ciscoGsccpNotificationsGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 16)
)
ciscoGsccpNotificationsGroupSup1.setObjects(
    ("CISCO-ITP-GSCCP-MIB", "ciscoGsccpGttErrors")
)
if mibBuilder.loadTexts:
    ciscoGsccpNotificationsGroupSup1.setStatus(
        "current"
    )

ciscoGsccpNotificationsGroupSup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 2, 26)
)
ciscoGsccpNotificationsGroupSup2.setObjects(
      *(("CISCO-ITP-GSCCP-MIB", "ciscoGsccpSegReassUnsup"),
        ("CISCO-ITP-GSCCP-MIB", "ciscoGsccpSOGReceived"),
        ("CISCO-ITP-GSCCP-MIB", "ciscoGsccpRmtCongestion"),
        ("CISCO-ITP-GSCCP-MIB", "ciscoGsccpLocalSsStateChange"))
)
if mibBuilder.loadTexts:
    ciscoGsccpNotificationsGroupSup2.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoGsccpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBCompliance.setStatus(
        "deprecated"
    )

ciscoGsccpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoGsccpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoGsccpMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoGsccpMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoGsccpMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoGsccpMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBComplianceRev6.setStatus(
        "deprecated"
    )

ciscoGsccpMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 335, 2, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoGsccpMIBComplianceRev7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-GSCCP-MIB",
    **{"CgsccpConPcListName": CgsccpConPcListName,
       "CgsccpGttSelName": CgsccpGttSelName,
       "CgsccpGttAppName": CgsccpGttAppName,
       "CgsccpGttPrefName": CgsccpGttPrefName,
       "CgsccpGttDisplaySS": CgsccpGttDisplaySS,
       "CgsccpGttAppCost": CgsccpGttAppCost,
       "CgsccpGttAppType": CgsccpGttAppType,
       "CgsccpGttMapType": CgsccpGttMapType,
       "CgsccpGttGtaResType": CgsccpGttGtaResType,
       "CgsccpGttRoutingInd": CgsccpGttRoutingInd,
       "CgsccpGttMapPcStatus": CgsccpGttMapPcStatus,
       "CgsccpGttMapSsStatus": CgsccpGttMapSsStatus,
       "CgsccpGttMultInd": CgsccpGttMultInd,
       "CgsccpGttMapCongStatus": CgsccpGttMapCongStatus,
       "CgsccpGttTransType": CgsccpGttTransType,
       "CgsccpGttQOS": CgsccpGttQOS,
       "CgsccpGttGlobalTitleInd": CgsccpGttGlobalTitleInd,
       "CgsccpClass": CgsccpClass,
       "ciscoGsccpMIB": ciscoGsccpMIB,
       "ciscoGsccpMIBNotifs": ciscoGsccpMIBNotifs,
       "ciscoGsccpGttMapStateChange": ciscoGsccpGttMapStateChange,
       "ciscoGsccpGttLoadTable": ciscoGsccpGttLoadTable,
       "ciscoGsccpGttErrors": ciscoGsccpGttErrors,
       "ciscoGsccpSegReassUnsup": ciscoGsccpSegReassUnsup,
       "ciscoGsccpSOGReceived": ciscoGsccpSOGReceived,
       "ciscoGsccpRmtCongestion": ciscoGsccpRmtCongestion,
       "ciscoGsccpLocalSsStateChange": ciscoGsccpLocalSsStateChange,
       "ciscoGsccpMIBObjects": ciscoGsccpMIBObjects,
       "cgsccpScalars": cgsccpScalars,
       "cgsccpGttTranslateSample": cgsccpGttTranslateSample,
       "cgsccpGttTranslatePeriod": cgsccpGttTranslatePeriod,
       "cgsccpGttMapStateNotifEnabled": cgsccpGttMapStateNotifEnabled,
       "cgsccpGttLoadTableNotifEnabled": cgsccpGttLoadTableNotifEnabled,
       "cgsccpGttTransErrorsNotifEnabled": cgsccpGttTransErrorsNotifEnabled,
       "cgsccpGttErrorPeriod": cgsccpGttErrorPeriod,
       "cgsccpGttErrorRecoveryCount": cgsccpGttErrorRecoveryCount,
       "cgsccpInst": cgsccpInst,
       "cgsccpInstTable": cgsccpInstTable,
       "cgsccpInstTableEntry": cgsccpInstTableEntry,
       "cgsccpInstTotalMsgs": cgsccpInstTotalMsgs,
       "cgsccpInstLocalMsgs": cgsccpInstLocalMsgs,
       "cgsccpInstTotalGttMsgs": cgsccpInstTotalGttMsgs,
       "cgsccpInstUDTMsgsSent": cgsccpInstUDTMsgsSent,
       "cgsccpInstUDTSMsgsSent": cgsccpInstUDTSMsgsSent,
       "cgsccpInstUDTSMsgsAttempted": cgsccpInstUDTSMsgsAttempted,
       "cgsccpInstUDTMsgsRcvd": cgsccpInstUDTMsgsRcvd,
       "cgsccpInstUDTSMsgsRcvd": cgsccpInstUDTSMsgsRcvd,
       "cgsccpInstXUDTMsgsSent": cgsccpInstXUDTMsgsSent,
       "cgsccpInstXUDTSMsgsAttempted": cgsccpInstXUDTSMsgsAttempted,
       "cgsccpInstXUDTSMsgsSent": cgsccpInstXUDTSMsgsSent,
       "cgsccpInstXUDTMsgsRcvd": cgsccpInstXUDTMsgsRcvd,
       "cgsccpInstXUDTSMsgsRcvd": cgsccpInstXUDTSMsgsRcvd,
       "cgsccpInstLUDTMsgsSent": cgsccpInstLUDTMsgsSent,
       "cgsccpInstLUDTSMsgsSent": cgsccpInstLUDTSMsgsSent,
       "cgsccpInstLUDTMsgsRcvd": cgsccpInstLUDTMsgsRcvd,
       "cgsccpInstLUDTSMsgsRcvd": cgsccpInstLUDTSMsgsRcvd,
       "cgsccpInstCrToMtp": cgsccpInstCrToMtp,
       "cgsccpInstCrefToMtp": cgsccpInstCrefToMtp,
       "cgsccpInstCrFromMtp": cgsccpInstCrFromMtp,
       "cgsccpInstCrefFromMtp": cgsccpInstCrefFromMtp,
       "cgsccpInstRsrToMtp": cgsccpInstRsrToMtp,
       "cgsccpInstRsrFromMtp": cgsccpInstRsrFromMtp,
       "cgsccpInstErrToMtp": cgsccpInstErrToMtp,
       "cgsccpInstErrFromMtp": cgsccpInstErrFromMtp,
       "cgsccpInstQ752T7E1": cgsccpInstQ752T7E1,
       "cgsccpInstInvalidGttFormat": cgsccpInstInvalidGttFormat,
       "cgsccpInstQ752T7E13": cgsccpInstQ752T7E13,
       "cgsccpInstMapNotFound": cgsccpInstMapNotFound,
       "cgsccpInstQ752T7E7": cgsccpInstQ752T7E7,
       "cgsccpInstGttConfigStatus": cgsccpInstGttConfigStatus,
       "cgsccpInstConfigTS": cgsccpInstConfigTS,
       "cgsccpInstGttConfigTS": cgsccpInstGttConfigTS,
       "cgsccpInstLastURL": cgsccpInstLastURL,
       "cgsccpInstConPcTableEntries": cgsccpInstConPcTableEntries,
       "cgsccpInstMapTableEntries": cgsccpInstMapTableEntries,
       "cgsccpInstGtaTableEntries": cgsccpInstGtaTableEntries,
       "cgsccpInstSelTableEntries": cgsccpInstSelTableEntries,
       "cgsccpInstAppGrTableEntries": cgsccpInstAppGrTableEntries,
       "cgsccpInstRowStatus": cgsccpInstRowStatus,
       "cgsccpInstPrefTableEntries": cgsccpInstPrefTableEntries,
       "cgsccpInstQ752Unqualified": cgsccpInstQ752Unqualified,
       "cgsccpInstErrorIndicator": cgsccpInstErrorIndicator,
       "cgsccpInstReassUnsup": cgsccpInstReassUnsup,
       "cgsccpInstReassFail": cgsccpInstReassFail,
       "cgsccpInstSegUnsup": cgsccpInstSegUnsup,
       "cgsccpInstSegFail": cgsccpInstSegFail,
       "cgsccpGttConPc": cgsccpGttConPc,
       "cgsccpGttConPcTable": cgsccpGttConPcTable,
       "cgsccpGttConPcTableEntry": cgsccpGttConPcTableEntry,
       "cgsccpGttConPcListName": cgsccpGttConPcListName,
       "cgsccpGttConPointCode": cgsccpGttConPointCode,
       "cgsccpGttConPcRowStatus": cgsccpGttConPcRowStatus,
       "cgsccpGttMap": cgsccpGttMap,
       "cgsccpGttMapTable": cgsccpGttMapTable,
       "cgsccpGttMapTableEntry": cgsccpGttMapTableEntry,
       "cgsccpGttMapPc": cgsccpGttMapPc,
       "cgsccpGttMapSsn": cgsccpGttMapSsn,
       "cgsccpGttMapDisplayPC": cgsccpGttMapDisplayPC,
       "cgsccpGttMapDisplaySS": cgsccpGttMapDisplaySS,
       "cgsccpGttMapType": cgsccpGttMapType,
       "cgsccpGttMapPcStatus": cgsccpGttMapPcStatus,
       "cgsccpGttMapSsStatus": cgsccpGttMapSsStatus,
       "cgsccpGttMapMultInd": cgsccpGttMapMultInd,
       "cgsccpGttMapBackupPc": cgsccpGttMapBackupPc,
       "cgsccpGttMapBackupSsn": cgsccpGttMapBackupSsn,
       "cgsccpGttMapConPcList": cgsccpGttMapConPcList,
       "cgsccpGttMapReRouteOnCong": cgsccpGttMapReRouteOnCong,
       "cgsccpGttMapAdjacent": cgsccpGttMapAdjacent,
       "cgsccpGttMapLastSsUsed": cgsccpGttMapLastSsUsed,
       "cgsccpGttMapUsed": cgsccpGttMapUsed,
       "cgsccpGttMapAltUsed": cgsccpGttMapAltUsed,
       "cgsccpGttMapSccpUnavail": cgsccpGttMapSccpUnavail,
       "cgsccpGttMapQ752T7E3Fail": cgsccpGttMapQ752T7E3Fail,
       "cgsccpGttMapQ752T7E3Un": cgsccpGttMapQ752T7E3Un,
       "cgsccpGttMapQ752T7E4": cgsccpGttMapQ752T7E4,
       "cgsccpGttMapQ752T7E5": cgsccpGttMapQ752T7E5,
       "cgsccpGttMapQ752T7E6": cgsccpGttMapQ752T7E6,
       "cgsccpGttMapRefCount": cgsccpGttMapRefCount,
       "cgsccpGttMapCongStatus": cgsccpGttMapCongStatus,
       "cgsccpGttMapRowStatus": cgsccpGttMapRowStatus,
       "cgsccpGttMapCongLvl1": cgsccpGttMapCongLvl1,
       "cgsccpGttMapCongLvl2": cgsccpGttMapCongLvl2,
       "cgsccpGttMapCongLvl3": cgsccpGttMapCongLvl3,
       "cgsccpGttMapSSPRcvd": cgsccpGttMapSSPRcvd,
       "cgsccpGttMapSSARcvd": cgsccpGttMapSSARcvd,
       "cgsccpGttSel": cgsccpGttSel,
       "cgsccpGttSelTable": cgsccpGttSelTable,
       "cgsccpGttSelTableEntry": cgsccpGttSelTableEntry,
       "cgsccpGttSelTT": cgsccpGttSelTT,
       "cgsccpGttSelNAI": cgsccpGttSelNAI,
       "cgsccpGttSelNP": cgsccpGttSelNP,
       "cgsccpGttSelGTI": cgsccpGttSelGTI,
       "cgsccpGttSelName": cgsccpGttSelName,
       "cgsccpGttSelNumPerf": cgsccpGttSelNumPerf,
       "cgsccpGttQ752T7E2": cgsccpGttQ752T7E2,
       "cgsccpGttSelQOS": cgsccpGttSelQOS,
       "cgsccpGttSelRefCount": cgsccpGttSelRefCount,
       "cgsccpGttSelPrePrefConv": cgsccpGttSelPrePrefConv,
       "cgsccpGttSelPostPrefConv": cgsccpGttSelPostPrefConv,
       "cgsccpGttSelRowStatus": cgsccpGttSelRowStatus,
       "cgsccpGttNextSelName": cgsccpGttNextSelName,
       "cgsccpGttNextSelRefed": cgsccpGttNextSelRefed,
       "cgsccpGttGta": cgsccpGttGta,
       "cgsccpGttGtaTable": cgsccpGttGtaTable,
       "cgsccpGttGtaTableEntry": cgsccpGttGtaTableEntry,
       "cgsccpGttGtaAddr": cgsccpGttGtaAddr,
       "cgsccpGttGtaSelName": cgsccpGttGtaSelName,
       "cgsccpGttGtaResType": cgsccpGttGtaResType,
       "cgsccpGttGtaResPc": cgsccpGttGtaResPc,
       "cgsccpGttGtaResMap": cgsccpGttGtaResMap,
       "cgsccpGttGtaResAppGroup": cgsccpGttGtaResAppGroup,
       "cgsccpGttGtaTTorSSN": cgsccpGttGtaTTorSSN,
       "cgsccpGttGtaTTorSSNvalue": cgsccpGttGtaTTorSSNvalue,
       "cgsccpGttGtaRoutingInd": cgsccpGttGtaRoutingInd,
       "cgsccpGttGtaQOS": cgsccpGttGtaQOS,
       "cgsccpGttGtaAddrDisp": cgsccpGttGtaAddrDisp,
       "cgsccpGttGtaAddrLen": cgsccpGttGtaAddrLen,
       "cgsccpGttGtaAsName": cgsccpGttGtaAsName,
       "cgsccpGttGtaRowStatus": cgsccpGttGtaRowStatus,
       "cgsccpGttGtaNetwork": cgsccpGttGtaNetwork,
       "cgsccpGttAppGr": cgsccpGttAppGr,
       "cgsccpGttAppGrTable": cgsccpGttAppGrTable,
       "cgsccpGttAppGrTableEntry": cgsccpGttAppGrTableEntry,
       "cgsccpGttAppGrName": cgsccpGttAppGrName,
       "cgsccpGttAppGrCost": cgsccpGttAppGrCost,
       "cgsccpGttAppGrEntNum": cgsccpGttAppGrEntNum,
       "cgsccpGttAppGrType": cgsccpGttAppGrType,
       "cgsccpGttAppGrPc": cgsccpGttAppGrPc,
       "cgsccpGttAppGrSsn": cgsccpGttAppGrSsn,
       "cgsccpGttAppGrRi": cgsccpGttAppGrRi,
       "cgsccpGttAppGrMult": cgsccpGttAppGrMult,
       "cgsccpGttAppGrRefCount": cgsccpGttAppGrRefCount,
       "cgsccpGttAppGrAsName": cgsccpGttAppGrAsName,
       "cgsccpGttAppGrNewSsn": cgsccpGttAppGrNewSsn,
       "cgsccpGttAppGrNumUsed": cgsccpGttAppGrNumUsed,
       "cgsccpGttAppGrRowStatus": cgsccpGttAppGrRowStatus,
       "cgsccpGttAppGrNetwork": cgsccpGttAppGrNetwork,
       "cgsccpGttPref": cgsccpGttPref,
       "cgsccpGttPrefTable": cgsccpGttPrefTable,
       "cgsccpGttPrefTableEntry": cgsccpGttPrefTableEntry,
       "cgsccpGttPrefName": cgsccpGttPrefName,
       "cgsccpGttPrefInAddr": cgsccpGttPrefInAddr,
       "cgsccpGttPrefOutAddr": cgsccpGttPrefOutAddr,
       "cgsccpGttPrefTblNAI": cgsccpGttPrefTblNAI,
       "cgsccpGttPrefTblNP": cgsccpGttPrefTblNP,
       "cgsccpGttPrefItemNAI": cgsccpGttPrefItemNAI,
       "cgsccpGttPrefItemNP": cgsccpGttPrefItemNP,
       "cgsccpGttPrefRowStatus": cgsccpGttPrefRowStatus,
       "cgsccpGttTranslate": cgsccpGttTranslate,
       "cgsccpGttTranslateTable": cgsccpGttTranslateTable,
       "cgsccpGttTranslateTableEntry": cgsccpGttTranslateTableEntry,
       "cgsccpGttTranslateSlot": cgsccpGttTranslateSlot,
       "cgsccpGttTranslateEntry": cgsccpGttTranslateEntry,
       "cgsccpGttTranslateRate": cgsccpGttTranslateRate,
       "cgsccpGttTranslateTS": cgsccpGttTranslateTS,
       "cgsccpGttTranslatePhysicalIndex": cgsccpGttTranslatePhysicalIndex,
       "cgsccpGttPref2": cgsccpGttPref2,
       "cgsccpGttPref2Table": cgsccpGttPref2Table,
       "cgsccpGttPref2TableEntry": cgsccpGttPref2TableEntry,
       "cgsccpGttPref2Name": cgsccpGttPref2Name,
       "cgsccpGttPref2InAddr": cgsccpGttPref2InAddr,
       "cgsccpGttPref2OutAddr": cgsccpGttPref2OutAddr,
       "cgsccpGttPref2TblNAI": cgsccpGttPref2TblNAI,
       "cgsccpGttPref2TblNP": cgsccpGttPref2TblNP,
       "cgsccpGttPref2ItemNAI": cgsccpGttPref2ItemNAI,
       "cgsccpGttPref2ItemNP": cgsccpGttPref2ItemNP,
       "cgsccpGttPref2RowStatus": cgsccpGttPref2RowStatus,
       "cgsccpGttPref2EncodingScheme": cgsccpGttPref2EncodingScheme,
       "cgsccpGttAppGr2": cgsccpGttAppGr2,
       "cgsccpGttAppGr2Table": cgsccpGttAppGr2Table,
       "cgsccpGttAppGr2TableEntry": cgsccpGttAppGr2TableEntry,
       "cgsccpGttAppGr2Name": cgsccpGttAppGr2Name,
       "cgsccpGttAppGr2EntNum": cgsccpGttAppGr2EntNum,
       "cgsccpGttAppGr2Mult": cgsccpGttAppGr2Mult,
       "cgsccpGttAppGr2Type": cgsccpGttAppGr2Type,
       "cgsccpGttAppGr2Cost": cgsccpGttAppGr2Cost,
       "cgsccpGttAppGr2Weight": cgsccpGttAppGr2Weight,
       "cgsccpGttAppGr2Pc": cgsccpGttAppGr2Pc,
       "cgsccpGttAppGr2Ssn": cgsccpGttAppGr2Ssn,
       "cgsccpGttAppGr2Ri": cgsccpGttAppGr2Ri,
       "cgsccpGttAppGr2RefCount": cgsccpGttAppGr2RefCount,
       "cgsccpGttAppGr2AsName": cgsccpGttAppGr2AsName,
       "cgsccpGttAppGr2NewSsn": cgsccpGttAppGr2NewSsn,
       "cgsccpGttAppGr2NumUsed": cgsccpGttAppGr2NumUsed,
       "cgsccpGttAppGr2Network": cgsccpGttAppGr2Network,
       "cgsccpGttAppGr2RowStatus": cgsccpGttAppGr2RowStatus,
       "cgsccpGttErrors": cgsccpGttErrors,
       "cgsccpGttErrorsTable": cgsccpGttErrorsTable,
       "cgsccpGttErrorsTableEntry": cgsccpGttErrorsTableEntry,
       "cgsccpGttErrorsSelectorNotFound": cgsccpGttErrorsSelectorNotFound,
       "cgsccpGttErrorsIncorrectFormat": cgsccpGttErrorsIncorrectFormat,
       "cgsccpGttErrorsGtaNotFound": cgsccpGttErrorsGtaNotFound,
       "cgsccpGttErrorsHopViolation": cgsccpGttErrorsHopViolation,
       "cgsccpGttErrorsMapNotFound": cgsccpGttErrorsMapNotFound,
       "cgsccpGttErrorsUnequipedSS": cgsccpGttErrorsUnequipedSS,
       "cgsccpGttErrorsSccpUnavailable": cgsccpGttErrorsSccpUnavailable,
       "cgsccpGttErrorsDpcUnavailable": cgsccpGttErrorsDpcUnavailable,
       "cgsccpGttErrorsSsUnavailable": cgsccpGttErrorsSsUnavailable,
       "cgsccpGttErrorsDpcCongested": cgsccpGttErrorsDpcCongested,
       "cgsccpGttErrorsSsCongested": cgsccpGttErrorsSsCongested,
       "cgsccpGttErrorsRouteFailure": cgsccpGttErrorsRouteFailure,
       "cgsccpGttErrorsSccpUnqualified": cgsccpGttErrorsSccpUnqualified,
       "cgsccpGttErrorsReassUnsupported": cgsccpGttErrorsReassUnsupported,
       "cgsccpGttErrorsReassFailure": cgsccpGttErrorsReassFailure,
       "cgsccpGttErrorsSegUnsupported": cgsccpGttErrorsSegUnsupported,
       "cgsccpGttErrorsSegFailure": cgsccpGttErrorsSegFailure,
       "cgsccpSSN": cgsccpSSN,
       "cgsccpSSNTable": cgsccpSSNTable,
       "cgsccpSSNEntry": cgsccpSSNEntry,
       "cgsccpSsn": cgsccpSsn,
       "cgsccpSSNNumProhibits": cgsccpSSNNumProhibits,
       "cgsccpSSNNumAllows": cgsccpSSNNumAllows,
       "cgsccpClassSsn": cgsccpClassSsn,
       "cgsccpSSNClassTable": cgsccpSSNClassTable,
       "cgsccpSSNClassEntry": cgsccpSSNClassEntry,
       "cgsccpClassIdx": cgsccpClassIdx,
       "cgsccpSSNClassUDTMsgsSent": cgsccpSSNClassUDTMsgsSent,
       "cgsccpSSNClassUDTMsgsRcvd": cgsccpSSNClassUDTMsgsRcvd,
       "cgsccpSSNClassXUDTMsgsSent": cgsccpSSNClassXUDTMsgsSent,
       "cgsccpSSNClassXUDTMsgsRcvd": cgsccpSSNClassXUDTMsgsRcvd,
       "cgsccpSSNClassLUDTMsgsSent": cgsccpSSNClassLUDTMsgsSent,
       "cgsccpSSNClassLUDTMsgsRcvd": cgsccpSSNClassLUDTMsgsRcvd,
       "cgsccpNotificationsInfo": cgsccpNotificationsInfo,
       "cgsccpLocalDisplaySS": cgsccpLocalDisplaySS,
       "cgsccpLocalSsStatus": cgsccpLocalSsStatus,
       "ciscoGsccpMIBConform": ciscoGsccpMIBConform,
       "ciscoGsccpMIBCompliances": ciscoGsccpMIBCompliances,
       "ciscoGsccpMIBCompliance": ciscoGsccpMIBCompliance,
       "ciscoGsccpMIBComplianceRev1": ciscoGsccpMIBComplianceRev1,
       "ciscoGsccpMIBComplianceRev2": ciscoGsccpMIBComplianceRev2,
       "ciscoGsccpMIBComplianceRev3": ciscoGsccpMIBComplianceRev3,
       "ciscoGsccpMIBComplianceRev4": ciscoGsccpMIBComplianceRev4,
       "ciscoGsccpMIBComplianceRev5": ciscoGsccpMIBComplianceRev5,
       "ciscoGsccpMIBComplianceRev6": ciscoGsccpMIBComplianceRev6,
       "ciscoGsccpMIBComplianceRev7": ciscoGsccpMIBComplianceRev7,
       "ciscoGsccpMIBGroups": ciscoGsccpMIBGroups,
       "ciscoGsccpGlobalEntryGroup": ciscoGsccpGlobalEntryGroup,
       "ciscoGsccpInstTableEntryGroup": ciscoGsccpInstTableEntryGroup,
       "ciscoGsccpGttConPcGroup": ciscoGsccpGttConPcGroup,
       "ciscoGsccpGttAppGroup": ciscoGsccpGttAppGroup,
       "ciscoGsccpGttMapGroup": ciscoGsccpGttMapGroup,
       "ciscoGsccpGttSelGroup": ciscoGsccpGttSelGroup,
       "ciscoGsccpGttGtaGroup": ciscoGsccpGttGtaGroup,
       "ciscoGsccpGttPrefGroup": ciscoGsccpGttPrefGroup,
       "ciscoGsccpNotificationsGroup": ciscoGsccpNotificationsGroup,
       "ciscoGsccpGttPrefGroupRev1": ciscoGsccpGttPrefGroupRev1,
       "ciscoGsccpInstTableEntryGroupRev1": ciscoGsccpInstTableEntryGroupRev1,
       "ciscoGsccpGlobalEntryGroupRev1": ciscoGsccpGlobalEntryGroupRev1,
       "ciscoGsccpGttAppGroupRev2": ciscoGsccpGttAppGroupRev2,
       "ciscoGsccpGttGtaGroupRev2": ciscoGsccpGttGtaGroupRev2,
       "ciscoGsccpGttAppGroupRev3": ciscoGsccpGttAppGroupRev3,
       "ciscoGsccpNotificationsGroupSup1": ciscoGsccpNotificationsGroupSup1,
       "ciscoGsccpGttErrorsGroup": ciscoGsccpGttErrorsGroup,
       "ciscoGsccpGttPrefGroupSup1": ciscoGsccpGttPrefGroupSup1,
       "ciscoGsccpGlobalEntryGroupSup1": ciscoGsccpGlobalEntryGroupSup1,
       "ciscoGsccpInstTableEntryGroupSup1": ciscoGsccpInstTableEntryGroupSup1,
       "ciscoGsccpGttMapGroupSup1": ciscoGsccpGttMapGroupSup1,
       "ciscoGsccpGttErrorsGroupSup1": ciscoGsccpGttErrorsGroupSup1,
       "ciscoGsccpGttSsnGroup": ciscoGsccpGttSsnGroup,
       "ciscoGsccpGttSsnClassGroup": ciscoGsccpGttSsnClassGroup,
       "ciscoGsccpNotificationsInfoGroup": ciscoGsccpNotificationsInfoGroup,
       "ciscoGsccpNotificationsGroupSup2": ciscoGsccpNotificationsGroupSup2,
       "ciscoGsccpGttSelGroupSup1": ciscoGsccpGttSelGroupSup1}
)
