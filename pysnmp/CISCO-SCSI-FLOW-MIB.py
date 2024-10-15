# SNMP MIB module (CISCO-SCSI-FLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SCSI-FLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:58 2024
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

(ScsiLUNOrZero,) = mibBuilder.importSymbols(
    "CISCO-SCSI-MIB",
    "ScsiLUNOrZero")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(FcNameId,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId",
    "VsanIndex")

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

ciscoScsiFlowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447)
)
ciscoScsiFlowMIB.setRevisions(
        ("2005-01-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CSFlowDeviceType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("initiator", 1),
          ("target", 2))
    )



class CSFlowVerifyReasonCode(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("cfsError", 12),
          ("cfsTimeout", 13),
          ("deviceNotFibreChannel", 10),
          ("deviceNotInitiator", 8),
          ("deviceNotOnIlc", 6),
          ("deviceNotScsi", 7),
          ("deviceNotTarget", 9),
          ("generalError", 3),
          ("initNotInNameServer", 17),
          ("initTargetZonedOut", 15),
          ("ipcTimeout", 11),
          ("noLicense", 2),
          ("notInFlogiServer", 5),
          ("notInNameServer", 4),
          ("portsUnprovisioned", 14),
          ("statusNotChecked", 16),
          ("success", 1),
          ("tgtNotInFlogiServer", 19),
          ("tgtNotInNameServer", 18))
    )



class CSFlowCfgReasonCode(Integer32, TextualConvention):
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
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("cfsError", 6),
          ("cfsTimeout", 7),
          ("deviceNotOnIlc", 8),
          ("dppError", 12),
          ("dppFlowExists", 19),
          ("dppNoBuffers", 17),
          ("dppNoMemory", 18),
          ("ilcAsicDrvError", 11),
          ("ipcError", 2),
          ("ipcTimeout", 3),
          ("lcIpcError", 9),
          ("sfcDBError", 14),
          ("sfcFlowExists", 16),
          ("sfcGenericError", 5),
          ("sfcNoSuchFlow", 15),
          ("sfmGenericError", 4),
          ("statusNotChecked", 13),
          ("success", 1),
          ("tcamError", 10))
    )



class CSFlowFeatureCfgReasonCode(Integer32, TextualConvention):
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
        *(("featureCfgFailure", 2),
          ("flowVerifFailure", 3),
          ("success", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoScsiFlowMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoScsiFlowMIBNotifs = _CiscoScsiFlowMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 0)
)
_CiscoScsiFlowMIBObjects_ObjectIdentity = ObjectIdentity
ciscoScsiFlowMIBObjects = _CiscoScsiFlowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1)
)
_CsfConfiguration_ObjectIdentity = ObjectIdentity
csfConfiguration = _CsfConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1)
)


class _CiscoScsiFlowNextIndexAvail_Type(Unsigned32):
    """Custom type ciscoScsiFlowNextIndexAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiscoScsiFlowNextIndexAvail_Type.__name__ = "Unsigned32"
_CiscoScsiFlowNextIndexAvail_Object = MibScalar
ciscoScsiFlowNextIndexAvail = _CiscoScsiFlowNextIndexAvail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 1),
    _CiscoScsiFlowNextIndexAvail_Type()
)
ciscoScsiFlowNextIndexAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowNextIndexAvail.setStatus("current")
_CiscoScsiFlowTable_Object = MibTable
ciscoScsiFlowTable = _CiscoScsiFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoScsiFlowTable.setStatus("current")
_CiscoScsiFlowEntry_Object = MibTableRow
ciscoScsiFlowEntry = _CiscoScsiFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1)
)
ciscoScsiFlowEntry.setIndexNames(
    (0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"),
)
if mibBuilder.loadTexts:
    ciscoScsiFlowEntry.setStatus("current")


class _CiscoScsiFlowId_Type(Unsigned32):
    """Custom type ciscoScsiFlowId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoScsiFlowId_Type.__name__ = "Unsigned32"
_CiscoScsiFlowId_Object = MibTableColumn
ciscoScsiFlowId = _CiscoScsiFlowId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 1),
    _CiscoScsiFlowId_Type()
)
ciscoScsiFlowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiFlowId.setStatus("current")
_CiscoScsiFlowIntrWwn_Type = FcNameId
_CiscoScsiFlowIntrWwn_Object = MibTableColumn
ciscoScsiFlowIntrWwn = _CiscoScsiFlowIntrWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 2),
    _CiscoScsiFlowIntrWwn_Type()
)
ciscoScsiFlowIntrWwn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowIntrWwn.setStatus("current")
_CiscoScsiFlowTargetWwn_Type = FcNameId
_CiscoScsiFlowTargetWwn_Object = MibTableColumn
ciscoScsiFlowTargetWwn = _CiscoScsiFlowTargetWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 3),
    _CiscoScsiFlowTargetWwn_Type()
)
ciscoScsiFlowTargetWwn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowTargetWwn.setStatus("current")


class _CiscoScsiFlowIntrVsan_Type(VsanIndex):
    """Custom type ciscoScsiFlowIntrVsan based on VsanIndex"""
    defaultValue = 1


_CiscoScsiFlowIntrVsan_Object = MibTableColumn
ciscoScsiFlowIntrVsan = _CiscoScsiFlowIntrVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 4),
    _CiscoScsiFlowIntrVsan_Type()
)
ciscoScsiFlowIntrVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowIntrVsan.setStatus("current")


class _CiscoScsiFlowTargetVsan_Type(VsanIndex):
    """Custom type ciscoScsiFlowTargetVsan based on VsanIndex"""
    defaultValue = 1


_CiscoScsiFlowTargetVsan_Object = MibTableColumn
ciscoScsiFlowTargetVsan = _CiscoScsiFlowTargetVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 5),
    _CiscoScsiFlowTargetVsan_Type()
)
ciscoScsiFlowTargetVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowTargetVsan.setStatus("current")


class _CiscoScsiFlowAllLuns_Type(TruthValue):
    """Custom type ciscoScsiFlowAllLuns based on TruthValue"""


_CiscoScsiFlowAllLuns_Object = MibTableColumn
ciscoScsiFlowAllLuns = _CiscoScsiFlowAllLuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 6),
    _CiscoScsiFlowAllLuns_Type()
)
ciscoScsiFlowAllLuns.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowAllLuns.setStatus("current")


class _CiscoScsiFlowWriteAcc_Type(TruthValue):
    """Custom type ciscoScsiFlowWriteAcc based on TruthValue"""


_CiscoScsiFlowWriteAcc_Object = MibTableColumn
ciscoScsiFlowWriteAcc = _CiscoScsiFlowWriteAcc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 7),
    _CiscoScsiFlowWriteAcc_Type()
)
ciscoScsiFlowWriteAcc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowWriteAcc.setStatus("current")


class _CiscoScsiFlowBufCount_Type(Unsigned32):
    """Custom type ciscoScsiFlowBufCount based on Unsigned32"""
    defaultValue = 1024

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoScsiFlowBufCount_Type.__name__ = "Unsigned32"
_CiscoScsiFlowBufCount_Object = MibTableColumn
ciscoScsiFlowBufCount = _CiscoScsiFlowBufCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 8),
    _CiscoScsiFlowBufCount_Type()
)
ciscoScsiFlowBufCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowBufCount.setStatus("current")


class _CiscoScsiFlowStatsEnabled_Type(TruthValue):
    """Custom type ciscoScsiFlowStatsEnabled based on TruthValue"""


_CiscoScsiFlowStatsEnabled_Object = MibTableColumn
ciscoScsiFlowStatsEnabled = _CiscoScsiFlowStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 9),
    _CiscoScsiFlowStatsEnabled_Type()
)
ciscoScsiFlowStatsEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsEnabled.setStatus("current")


class _CiscoScsiFlowClearStats_Type(Integer32):
    """Custom type ciscoScsiFlowClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noop", 2))
    )


_CiscoScsiFlowClearStats_Type.__name__ = "Integer32"
_CiscoScsiFlowClearStats_Object = MibTableColumn
ciscoScsiFlowClearStats = _CiscoScsiFlowClearStats_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 10),
    _CiscoScsiFlowClearStats_Type()
)
ciscoScsiFlowClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowClearStats.setStatus("current")
_CiscoScsiFlowIntrVrfStatus_Type = CSFlowVerifyReasonCode
_CiscoScsiFlowIntrVrfStatus_Object = MibTableColumn
ciscoScsiFlowIntrVrfStatus = _CiscoScsiFlowIntrVrfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 11),
    _CiscoScsiFlowIntrVrfStatus_Type()
)
ciscoScsiFlowIntrVrfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowIntrVrfStatus.setStatus("current")
_CiscoScsiFlowTgtVrfStatus_Type = CSFlowVerifyReasonCode
_CiscoScsiFlowTgtVrfStatus_Object = MibTableColumn
ciscoScsiFlowTgtVrfStatus = _CiscoScsiFlowTgtVrfStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 12),
    _CiscoScsiFlowTgtVrfStatus_Type()
)
ciscoScsiFlowTgtVrfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowTgtVrfStatus.setStatus("current")
_CiscoScsiFlowIntrLCStatus_Type = CSFlowVerifyReasonCode
_CiscoScsiFlowIntrLCStatus_Object = MibTableColumn
ciscoScsiFlowIntrLCStatus = _CiscoScsiFlowIntrLCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 13),
    _CiscoScsiFlowIntrLCStatus_Type()
)
ciscoScsiFlowIntrLCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowIntrLCStatus.setStatus("current")
_CiscoScsiFlowTgtLCStatus_Type = CSFlowVerifyReasonCode
_CiscoScsiFlowTgtLCStatus_Object = MibTableColumn
ciscoScsiFlowTgtLCStatus = _CiscoScsiFlowTgtLCStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 14),
    _CiscoScsiFlowTgtLCStatus_Type()
)
ciscoScsiFlowTgtLCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowTgtLCStatus.setStatus("current")
_CiscoScsiFlowRowStatus_Type = RowStatus
_CiscoScsiFlowRowStatus_Object = MibTableColumn
ciscoScsiFlowRowStatus = _CiscoScsiFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 2, 1, 15),
    _CiscoScsiFlowRowStatus_Type()
)
ciscoScsiFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoScsiFlowRowStatus.setStatus("current")


class _CiscoScsiFlowNum_Type(Unsigned32):
    """Custom type ciscoScsiFlowNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiscoScsiFlowNum_Type.__name__ = "Unsigned32"
_CiscoScsiFlowNum_Object = MibScalar
ciscoScsiFlowNum = _CiscoScsiFlowNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 3),
    _CiscoScsiFlowNum_Type()
)
ciscoScsiFlowNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoScsiFlowNum.setStatus("current")
_CiscoScsiFlowDeviceType_Type = CSFlowDeviceType
_CiscoScsiFlowDeviceType_Object = MibScalar
ciscoScsiFlowDeviceType = _CiscoScsiFlowDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 4),
    _CiscoScsiFlowDeviceType_Type()
)
ciscoScsiFlowDeviceType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoScsiFlowDeviceType.setStatus("current")
_CiscoScsiFlowVerifyReasonCode_Type = CSFlowVerifyReasonCode
_CiscoScsiFlowVerifyReasonCode_Object = MibScalar
ciscoScsiFlowVerifyReasonCode = _CiscoScsiFlowVerifyReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 5),
    _CiscoScsiFlowVerifyReasonCode_Type()
)
ciscoScsiFlowVerifyReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoScsiFlowVerifyReasonCode.setStatus("current")
_CiscoScsiFlowCfgReasonCode_Type = CSFlowCfgReasonCode
_CiscoScsiFlowCfgReasonCode_Object = MibScalar
ciscoScsiFlowCfgReasonCode = _CiscoScsiFlowCfgReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 1, 6),
    _CiscoScsiFlowCfgReasonCode_Type()
)
ciscoScsiFlowCfgReasonCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ciscoScsiFlowCfgReasonCode.setStatus("current")
_CsfStats_ObjectIdentity = ObjectIdentity
csfStats = _CsfStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2)
)
_CiscoScsiFlowStatsTable_Object = MibTable
ciscoScsiFlowStatsTable = _CiscoScsiFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsTable.setStatus("current")
_CiscoScsiFlowStatsEntry_Object = MibTableRow
ciscoScsiFlowStatsEntry = _CiscoScsiFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1)
)
ciscoScsiFlowStatsEntry.setIndexNames(
    (0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"),
    (0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowLunId"),
)
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsEntry.setStatus("current")
_CiscoScsiFlowLunId_Type = ScsiLUNOrZero
_CiscoScsiFlowLunId_Object = MibTableColumn
ciscoScsiFlowLunId = _CiscoScsiFlowLunId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 1),
    _CiscoScsiFlowLunId_Type()
)
ciscoScsiFlowLunId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoScsiFlowLunId.setStatus("current")
_CiscoScsiFlowRdIos_Type = Counter64
_CiscoScsiFlowRdIos_Object = MibTableColumn
ciscoScsiFlowRdIos = _CiscoScsiFlowRdIos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 2),
    _CiscoScsiFlowRdIos_Type()
)
ciscoScsiFlowRdIos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdIos.setStatus("current")
_CiscoScsiFlowRdFailedIos_Type = Counter32
_CiscoScsiFlowRdFailedIos_Object = MibTableColumn
ciscoScsiFlowRdFailedIos = _CiscoScsiFlowRdFailedIos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 3),
    _CiscoScsiFlowRdFailedIos_Type()
)
ciscoScsiFlowRdFailedIos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdFailedIos.setStatus("current")
_CiscoScsiFlowRdTimeouts_Type = Counter32
_CiscoScsiFlowRdTimeouts_Object = MibTableColumn
ciscoScsiFlowRdTimeouts = _CiscoScsiFlowRdTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 4),
    _CiscoScsiFlowRdTimeouts_Type()
)
ciscoScsiFlowRdTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdTimeouts.setStatus("current")
_CiscoScsiFlowRdBlocks_Type = Counter64
_CiscoScsiFlowRdBlocks_Object = MibTableColumn
ciscoScsiFlowRdBlocks = _CiscoScsiFlowRdBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 5),
    _CiscoScsiFlowRdBlocks_Type()
)
ciscoScsiFlowRdBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdBlocks.setStatus("current")
_CiscoScsiFlowRdMaxBlocks_Type = Gauge32
_CiscoScsiFlowRdMaxBlocks_Object = MibTableColumn
ciscoScsiFlowRdMaxBlocks = _CiscoScsiFlowRdMaxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 6),
    _CiscoScsiFlowRdMaxBlocks_Type()
)
ciscoScsiFlowRdMaxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdMaxBlocks.setStatus("current")
_CiscoScsiFlowRdMinTime_Type = Gauge32
_CiscoScsiFlowRdMinTime_Object = MibTableColumn
ciscoScsiFlowRdMinTime = _CiscoScsiFlowRdMinTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 7),
    _CiscoScsiFlowRdMinTime_Type()
)
ciscoScsiFlowRdMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdMinTime.setStatus("current")
_CiscoScsiFlowRdMaxTime_Type = Gauge32
_CiscoScsiFlowRdMaxTime_Object = MibTableColumn
ciscoScsiFlowRdMaxTime = _CiscoScsiFlowRdMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 8),
    _CiscoScsiFlowRdMaxTime_Type()
)
ciscoScsiFlowRdMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdMaxTime.setStatus("current")
_CiscoScsiFlowRdsActive_Type = Gauge32
_CiscoScsiFlowRdsActive_Object = MibTableColumn
ciscoScsiFlowRdsActive = _CiscoScsiFlowRdsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 9),
    _CiscoScsiFlowRdsActive_Type()
)
ciscoScsiFlowRdsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdsActive.setStatus("current")
_CiscoScsiFlowWrIos_Type = Counter64
_CiscoScsiFlowWrIos_Object = MibTableColumn
ciscoScsiFlowWrIos = _CiscoScsiFlowWrIos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 10),
    _CiscoScsiFlowWrIos_Type()
)
ciscoScsiFlowWrIos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrIos.setStatus("current")
_CiscoScsiFlowWrFailedIos_Type = Counter32
_CiscoScsiFlowWrFailedIos_Object = MibTableColumn
ciscoScsiFlowWrFailedIos = _CiscoScsiFlowWrFailedIos_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 11),
    _CiscoScsiFlowWrFailedIos_Type()
)
ciscoScsiFlowWrFailedIos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrFailedIos.setStatus("current")
_CiscoScsiFlowWrTimeouts_Type = Counter32
_CiscoScsiFlowWrTimeouts_Object = MibTableColumn
ciscoScsiFlowWrTimeouts = _CiscoScsiFlowWrTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 12),
    _CiscoScsiFlowWrTimeouts_Type()
)
ciscoScsiFlowWrTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrTimeouts.setStatus("current")
_CiscoScsiFlowWrBlocks_Type = Counter64
_CiscoScsiFlowWrBlocks_Object = MibTableColumn
ciscoScsiFlowWrBlocks = _CiscoScsiFlowWrBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 13),
    _CiscoScsiFlowWrBlocks_Type()
)
ciscoScsiFlowWrBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrBlocks.setStatus("current")
_CiscoScsiFlowWrMaxBlocks_Type = Gauge32
_CiscoScsiFlowWrMaxBlocks_Object = MibTableColumn
ciscoScsiFlowWrMaxBlocks = _CiscoScsiFlowWrMaxBlocks_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 14),
    _CiscoScsiFlowWrMaxBlocks_Type()
)
ciscoScsiFlowWrMaxBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrMaxBlocks.setStatus("current")
_CiscoScsiFlowWrMinTime_Type = Gauge32
_CiscoScsiFlowWrMinTime_Object = MibTableColumn
ciscoScsiFlowWrMinTime = _CiscoScsiFlowWrMinTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 15),
    _CiscoScsiFlowWrMinTime_Type()
)
ciscoScsiFlowWrMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrMinTime.setStatus("current")
_CiscoScsiFlowWrMaxTime_Type = Gauge32
_CiscoScsiFlowWrMaxTime_Object = MibTableColumn
ciscoScsiFlowWrMaxTime = _CiscoScsiFlowWrMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 16),
    _CiscoScsiFlowWrMaxTime_Type()
)
ciscoScsiFlowWrMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrMaxTime.setStatus("current")
_CiscoScsiFlowWrsActive_Type = Gauge32
_CiscoScsiFlowWrsActive_Object = MibTableColumn
ciscoScsiFlowWrsActive = _CiscoScsiFlowWrsActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 17),
    _CiscoScsiFlowWrsActive_Type()
)
ciscoScsiFlowWrsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrsActive.setStatus("current")
_CiscoScsiFlowTestUnitRdys_Type = Counter32
_CiscoScsiFlowTestUnitRdys_Object = MibTableColumn
ciscoScsiFlowTestUnitRdys = _CiscoScsiFlowTestUnitRdys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 18),
    _CiscoScsiFlowTestUnitRdys_Type()
)
ciscoScsiFlowTestUnitRdys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowTestUnitRdys.setStatus("current")
_CiscoScsiFlowRepLuns_Type = Counter32
_CiscoScsiFlowRepLuns_Object = MibTableColumn
ciscoScsiFlowRepLuns = _CiscoScsiFlowRepLuns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 19),
    _CiscoScsiFlowRepLuns_Type()
)
ciscoScsiFlowRepLuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRepLuns.setStatus("current")
_CiscoScsiFlowInquirys_Type = Counter32
_CiscoScsiFlowInquirys_Object = MibTableColumn
ciscoScsiFlowInquirys = _CiscoScsiFlowInquirys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 20),
    _CiscoScsiFlowInquirys_Type()
)
ciscoScsiFlowInquirys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowInquirys.setStatus("current")
_CiscoScsiFlowRdCapacitys_Type = Counter32
_CiscoScsiFlowRdCapacitys_Object = MibTableColumn
ciscoScsiFlowRdCapacitys = _CiscoScsiFlowRdCapacitys_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 21),
    _CiscoScsiFlowRdCapacitys_Type()
)
ciscoScsiFlowRdCapacitys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRdCapacitys.setStatus("current")
_CiscoScsiFlowModeSenses_Type = Counter32
_CiscoScsiFlowModeSenses_Object = MibTableColumn
ciscoScsiFlowModeSenses = _CiscoScsiFlowModeSenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 22),
    _CiscoScsiFlowModeSenses_Type()
)
ciscoScsiFlowModeSenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowModeSenses.setStatus("current")
_CiscoScsiFlowReqSenses_Type = Counter32
_CiscoScsiFlowReqSenses_Object = MibTableColumn
ciscoScsiFlowReqSenses = _CiscoScsiFlowReqSenses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 23),
    _CiscoScsiFlowReqSenses_Type()
)
ciscoScsiFlowReqSenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowReqSenses.setStatus("current")
_CiscoScsiFlowRxFc2Frames_Type = Counter64
_CiscoScsiFlowRxFc2Frames_Object = MibTableColumn
ciscoScsiFlowRxFc2Frames = _CiscoScsiFlowRxFc2Frames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 24),
    _CiscoScsiFlowRxFc2Frames_Type()
)
ciscoScsiFlowRxFc2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRxFc2Frames.setStatus("current")
_CiscoScsiFlowTxFc2Frames_Type = Counter64
_CiscoScsiFlowTxFc2Frames_Object = MibTableColumn
ciscoScsiFlowTxFc2Frames = _CiscoScsiFlowTxFc2Frames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 25),
    _CiscoScsiFlowTxFc2Frames_Type()
)
ciscoScsiFlowTxFc2Frames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowTxFc2Frames.setStatus("current")
_CiscoScsiFlowRxFc2Octets_Type = Counter64
_CiscoScsiFlowRxFc2Octets_Object = MibTableColumn
ciscoScsiFlowRxFc2Octets = _CiscoScsiFlowRxFc2Octets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 26),
    _CiscoScsiFlowRxFc2Octets_Type()
)
ciscoScsiFlowRxFc2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowRxFc2Octets.setStatus("current")
_CiscoScsiFlowTxFc2Octets_Type = Counter64
_CiscoScsiFlowTxFc2Octets_Object = MibTableColumn
ciscoScsiFlowTxFc2Octets = _CiscoScsiFlowTxFc2Octets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 27),
    _CiscoScsiFlowTxFc2Octets_Type()
)
ciscoScsiFlowTxFc2Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowTxFc2Octets.setStatus("current")
_CiscoScsiFlowBusyStatuses_Type = Counter32
_CiscoScsiFlowBusyStatuses_Object = MibTableColumn
ciscoScsiFlowBusyStatuses = _CiscoScsiFlowBusyStatuses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 28),
    _CiscoScsiFlowBusyStatuses_Type()
)
ciscoScsiFlowBusyStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowBusyStatuses.setStatus("current")
_CiscoScsiFlowStatusResvConfs_Type = Counter32
_CiscoScsiFlowStatusResvConfs_Object = MibTableColumn
ciscoScsiFlowStatusResvConfs = _CiscoScsiFlowStatusResvConfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 29),
    _CiscoScsiFlowStatusResvConfs_Type()
)
ciscoScsiFlowStatusResvConfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowStatusResvConfs.setStatus("current")
_CiscoScsiFlowTskSetFulStatuses_Type = Counter32
_CiscoScsiFlowTskSetFulStatuses_Object = MibTableColumn
ciscoScsiFlowTskSetFulStatuses = _CiscoScsiFlowTskSetFulStatuses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 30),
    _CiscoScsiFlowTskSetFulStatuses_Type()
)
ciscoScsiFlowTskSetFulStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowTskSetFulStatuses.setStatus("current")
_CiscoScsiFlowAcaActiveStatuses_Type = Counter32
_CiscoScsiFlowAcaActiveStatuses_Object = MibTableColumn
ciscoScsiFlowAcaActiveStatuses = _CiscoScsiFlowAcaActiveStatuses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 31),
    _CiscoScsiFlowAcaActiveStatuses_Type()
)
ciscoScsiFlowAcaActiveStatuses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowAcaActiveStatuses.setStatus("current")
_CiscoScsiFlowSenseKeyNotRdyErrs_Type = Counter32
_CiscoScsiFlowSenseKeyNotRdyErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyNotRdyErrs = _CiscoScsiFlowSenseKeyNotRdyErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 32),
    _CiscoScsiFlowSenseKeyNotRdyErrs_Type()
)
ciscoScsiFlowSenseKeyNotRdyErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyNotRdyErrs.setStatus("current")
_CiscoScsiFlowSenseKeyMedErrs_Type = Counter32
_CiscoScsiFlowSenseKeyMedErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyMedErrs = _CiscoScsiFlowSenseKeyMedErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 33),
    _CiscoScsiFlowSenseKeyMedErrs_Type()
)
ciscoScsiFlowSenseKeyMedErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyMedErrs.setStatus("current")
_CiscoScsiFlowSenseKeyHwErrs_Type = Counter32
_CiscoScsiFlowSenseKeyHwErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyHwErrs = _CiscoScsiFlowSenseKeyHwErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 34),
    _CiscoScsiFlowSenseKeyHwErrs_Type()
)
ciscoScsiFlowSenseKeyHwErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyHwErrs.setStatus("current")
_CiscoScsiFlowSenseKeyIllReqErrs_Type = Counter32
_CiscoScsiFlowSenseKeyIllReqErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyIllReqErrs = _CiscoScsiFlowSenseKeyIllReqErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 35),
    _CiscoScsiFlowSenseKeyIllReqErrs_Type()
)
ciscoScsiFlowSenseKeyIllReqErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyIllReqErrs.setStatus("current")
_CiscoScsiFlowSenseKeyUnitAttErrs_Type = Counter32
_CiscoScsiFlowSenseKeyUnitAttErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyUnitAttErrs = _CiscoScsiFlowSenseKeyUnitAttErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 36),
    _CiscoScsiFlowSenseKeyUnitAttErrs_Type()
)
ciscoScsiFlowSenseKeyUnitAttErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyUnitAttErrs.setStatus("current")
_CiscoScsiFlowSenseKeyDatProtErrs_Type = Counter32
_CiscoScsiFlowSenseKeyDatProtErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyDatProtErrs = _CiscoScsiFlowSenseKeyDatProtErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 37),
    _CiscoScsiFlowSenseKeyDatProtErrs_Type()
)
ciscoScsiFlowSenseKeyDatProtErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyDatProtErrs.setStatus("current")
_CiscoScsiFlowSenseKeyBlankErrs_Type = Counter32
_CiscoScsiFlowSenseKeyBlankErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyBlankErrs = _CiscoScsiFlowSenseKeyBlankErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 38),
    _CiscoScsiFlowSenseKeyBlankErrs_Type()
)
ciscoScsiFlowSenseKeyBlankErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyBlankErrs.setStatus("current")
_CiscoScsiFlowSenseKeyCpAbrtErrs_Type = Counter32
_CiscoScsiFlowSenseKeyCpAbrtErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyCpAbrtErrs = _CiscoScsiFlowSenseKeyCpAbrtErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 39),
    _CiscoScsiFlowSenseKeyCpAbrtErrs_Type()
)
ciscoScsiFlowSenseKeyCpAbrtErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyCpAbrtErrs.setStatus("current")
_CiscoScsiFlowSenseKeyAbrtCmdErrs_Type = Counter32
_CiscoScsiFlowSenseKeyAbrtCmdErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyAbrtCmdErrs = _CiscoScsiFlowSenseKeyAbrtCmdErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 40),
    _CiscoScsiFlowSenseKeyAbrtCmdErrs_Type()
)
ciscoScsiFlowSenseKeyAbrtCmdErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyAbrtCmdErrs.setStatus("current")
_CiscoScsiFlowSenseKeyVolFlowErrs_Type = Counter32
_CiscoScsiFlowSenseKeyVolFlowErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyVolFlowErrs = _CiscoScsiFlowSenseKeyVolFlowErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 41),
    _CiscoScsiFlowSenseKeyVolFlowErrs_Type()
)
ciscoScsiFlowSenseKeyVolFlowErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyVolFlowErrs.setStatus("current")
_CiscoScsiFlowSenseKeyMiscmpErrs_Type = Counter32
_CiscoScsiFlowSenseKeyMiscmpErrs_Object = MibTableColumn
ciscoScsiFlowSenseKeyMiscmpErrs = _CiscoScsiFlowSenseKeyMiscmpErrs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 42),
    _CiscoScsiFlowSenseKeyMiscmpErrs_Type()
)
ciscoScsiFlowSenseKeyMiscmpErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowSenseKeyMiscmpErrs.setStatus("current")
_CiscoScsiFlowAbts_Type = Counter32
_CiscoScsiFlowAbts_Object = MibTableColumn
ciscoScsiFlowAbts = _CiscoScsiFlowAbts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 2, 1, 1, 43),
    _CiscoScsiFlowAbts_Type()
)
ciscoScsiFlowAbts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowAbts.setStatus("current")
_CsfFeatureStatus_ObjectIdentity = ObjectIdentity
csfFeatureStatus = _CsfFeatureStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3)
)
_CiscoScsiFlowWrAccStatusTable_Object = MibTable
ciscoScsiFlowWrAccStatusTable = _CiscoScsiFlowWrAccStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiFlowWrAccStatusTable.setStatus("current")
_CiscoScsiFlowWrAccStatusEntry_Object = MibTableRow
ciscoScsiFlowWrAccStatusEntry = _CiscoScsiFlowWrAccStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1)
)
ciscoScsiFlowWrAccStatusEntry.setIndexNames(
    (0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"),
)
if mibBuilder.loadTexts:
    ciscoScsiFlowWrAccStatusEntry.setStatus("current")
_CiscoScsiFlowWrAccCfgStatus_Type = CSFlowFeatureCfgReasonCode
_CiscoScsiFlowWrAccCfgStatus_Object = MibTableColumn
ciscoScsiFlowWrAccCfgStatus = _CiscoScsiFlowWrAccCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1, 1),
    _CiscoScsiFlowWrAccCfgStatus_Type()
)
ciscoScsiFlowWrAccCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrAccCfgStatus.setStatus("current")
_CiscoScsiFlowWrAccIntrCfgStatus_Type = CSFlowCfgReasonCode
_CiscoScsiFlowWrAccIntrCfgStatus_Object = MibTableColumn
ciscoScsiFlowWrAccIntrCfgStatus = _CiscoScsiFlowWrAccIntrCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1, 2),
    _CiscoScsiFlowWrAccIntrCfgStatus_Type()
)
ciscoScsiFlowWrAccIntrCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrAccIntrCfgStatus.setStatus("current")
_CiscoScsiFlowWrAccTgtCfgStatus_Type = CSFlowCfgReasonCode
_CiscoScsiFlowWrAccTgtCfgStatus_Object = MibTableColumn
ciscoScsiFlowWrAccTgtCfgStatus = _CiscoScsiFlowWrAccTgtCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 1, 1, 3),
    _CiscoScsiFlowWrAccTgtCfgStatus_Type()
)
ciscoScsiFlowWrAccTgtCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowWrAccTgtCfgStatus.setStatus("current")
_CiscoScsiFlowStatsStatusTable_Object = MibTable
ciscoScsiFlowStatsStatusTable = _CiscoScsiFlowStatsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2)
)
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsStatusTable.setStatus("current")
_CiscoScsiFlowStatsStatusEntry_Object = MibTableRow
ciscoScsiFlowStatsStatusEntry = _CiscoScsiFlowStatsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1)
)
ciscoScsiFlowStatsStatusEntry.setIndexNames(
    (0, "CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowId"),
)
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsStatusEntry.setStatus("current")
_CiscoScsiFlowStatsCfgStatus_Type = CSFlowFeatureCfgReasonCode
_CiscoScsiFlowStatsCfgStatus_Object = MibTableColumn
ciscoScsiFlowStatsCfgStatus = _CiscoScsiFlowStatsCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1, 1),
    _CiscoScsiFlowStatsCfgStatus_Type()
)
ciscoScsiFlowStatsCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsCfgStatus.setStatus("current")
_CiscoScsiFlowStatsIntrCfgStatus_Type = CSFlowCfgReasonCode
_CiscoScsiFlowStatsIntrCfgStatus_Object = MibTableColumn
ciscoScsiFlowStatsIntrCfgStatus = _CiscoScsiFlowStatsIntrCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1, 2),
    _CiscoScsiFlowStatsIntrCfgStatus_Type()
)
ciscoScsiFlowStatsIntrCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsIntrCfgStatus.setStatus("current")
_CiscoScsiFlowStatsTgtCfgStatus_Type = CSFlowCfgReasonCode
_CiscoScsiFlowStatsTgtCfgStatus_Object = MibTableColumn
ciscoScsiFlowStatsTgtCfgStatus = _CiscoScsiFlowStatsTgtCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 1, 3, 2, 1, 3),
    _CiscoScsiFlowStatsTgtCfgStatus_Type()
)
ciscoScsiFlowStatsTgtCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsTgtCfgStatus.setStatus("current")
_CiscoScsiFlowMIBConform_ObjectIdentity = ObjectIdentity
ciscoScsiFlowMIBConform = _CiscoScsiFlowMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2)
)
_CiscoScsiFlowMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoScsiFlowMIBCompliances = _CiscoScsiFlowMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 1)
)
_CiscoScsiFlowMIBGroups_ObjectIdentity = ObjectIdentity
ciscoScsiFlowMIBGroups = _CiscoScsiFlowMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2)
)

# Managed Objects groups

ciscoScsiFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 1)
)
ciscoScsiFlowGroup.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNextIndexAvail"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrWwn"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTargetWwn"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrVsan"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTargetVsan"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowAllLuns"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWriteAcc"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowBufCount"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsEnabled"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRowStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowClearStats"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrVrfStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowIntrLCStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTgtLCStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTgtVrfStatus"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowGroup.setStatus("current")

ciscoScsiFlowStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 2)
)
ciscoScsiFlowStatsGroup.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdIos"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdFailedIos"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdTimeouts"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdBlocks"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdMaxBlocks"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdMinTime"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdMaxTime"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdsActive"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrIos"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrFailedIos"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrTimeouts"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrBlocks"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrMaxBlocks"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrMinTime"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrMaxTime"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrsActive"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTestUnitRdys"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRepLuns"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowInquirys"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRdCapacitys"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowModeSenses"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowReqSenses"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRxFc2Frames"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTxFc2Frames"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowRxFc2Octets"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTxFc2Octets"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowBusyStatuses"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatusResvConfs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowTskSetFulStatuses"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowAcaActiveStatuses"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyNotRdyErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyMedErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyHwErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyIllReqErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyUnitAttErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyDatProtErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyBlankErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyCpAbrtErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyAbrtCmdErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyVolFlowErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowSenseKeyMiscmpErrs"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowAbts"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsGroup.setStatus("current")

ciscoScsiFlowInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 3)
)
ciscoScsiFlowInfoGroup.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowVerifyReasonCode"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowCfgReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowInfoGroup.setStatus("current")

ciscoScsiFlowFeatureStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 5)
)
ciscoScsiFlowFeatureStatusGroup.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccCfgStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccIntrCfgStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccTgtCfgStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsCfgStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsIntrCfgStatus"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsTgtCfgStatus"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowFeatureStatusGroup.setStatus("current")


# Notification objects

ciscoScsiFlowVerifyNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 0, 1)
)
ciscoScsiFlowVerifyNotify.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowVerifyReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowVerifyNotify.setStatus(
        "current"
    )

ciscoScsiFlowWrAccNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 0, 2)
)
ciscoScsiFlowWrAccNotify.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowCfgReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowWrAccNotify.setStatus(
        "current"
    )

ciscoScsiFlowStatsNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 0, 3)
)
ciscoScsiFlowStatsNotify.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowNum"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowDeviceType"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowCfgReasonCode"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowStatsNotify.setStatus(
        "current"
    )


# Notifications groups

ciscoScsiFlowNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 2, 4)
)
ciscoScsiFlowNotifyGroup.setObjects(
      *(("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowVerifyNotify"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowWrAccNotify"),
        ("CISCO-SCSI-FLOW-MIB", "ciscoScsiFlowStatsNotify"))
)
if mibBuilder.loadTexts:
    ciscoScsiFlowNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoScsiFlowMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 447, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoScsiFlowMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SCSI-FLOW-MIB",
    **{"CSFlowDeviceType": CSFlowDeviceType,
       "CSFlowVerifyReasonCode": CSFlowVerifyReasonCode,
       "CSFlowCfgReasonCode": CSFlowCfgReasonCode,
       "CSFlowFeatureCfgReasonCode": CSFlowFeatureCfgReasonCode,
       "ciscoScsiFlowMIB": ciscoScsiFlowMIB,
       "ciscoScsiFlowMIBNotifs": ciscoScsiFlowMIBNotifs,
       "ciscoScsiFlowVerifyNotify": ciscoScsiFlowVerifyNotify,
       "ciscoScsiFlowWrAccNotify": ciscoScsiFlowWrAccNotify,
       "ciscoScsiFlowStatsNotify": ciscoScsiFlowStatsNotify,
       "ciscoScsiFlowMIBObjects": ciscoScsiFlowMIBObjects,
       "csfConfiguration": csfConfiguration,
       "ciscoScsiFlowNextIndexAvail": ciscoScsiFlowNextIndexAvail,
       "ciscoScsiFlowTable": ciscoScsiFlowTable,
       "ciscoScsiFlowEntry": ciscoScsiFlowEntry,
       "ciscoScsiFlowId": ciscoScsiFlowId,
       "ciscoScsiFlowIntrWwn": ciscoScsiFlowIntrWwn,
       "ciscoScsiFlowTargetWwn": ciscoScsiFlowTargetWwn,
       "ciscoScsiFlowIntrVsan": ciscoScsiFlowIntrVsan,
       "ciscoScsiFlowTargetVsan": ciscoScsiFlowTargetVsan,
       "ciscoScsiFlowAllLuns": ciscoScsiFlowAllLuns,
       "ciscoScsiFlowWriteAcc": ciscoScsiFlowWriteAcc,
       "ciscoScsiFlowBufCount": ciscoScsiFlowBufCount,
       "ciscoScsiFlowStatsEnabled": ciscoScsiFlowStatsEnabled,
       "ciscoScsiFlowClearStats": ciscoScsiFlowClearStats,
       "ciscoScsiFlowIntrVrfStatus": ciscoScsiFlowIntrVrfStatus,
       "ciscoScsiFlowTgtVrfStatus": ciscoScsiFlowTgtVrfStatus,
       "ciscoScsiFlowIntrLCStatus": ciscoScsiFlowIntrLCStatus,
       "ciscoScsiFlowTgtLCStatus": ciscoScsiFlowTgtLCStatus,
       "ciscoScsiFlowRowStatus": ciscoScsiFlowRowStatus,
       "ciscoScsiFlowNum": ciscoScsiFlowNum,
       "ciscoScsiFlowDeviceType": ciscoScsiFlowDeviceType,
       "ciscoScsiFlowVerifyReasonCode": ciscoScsiFlowVerifyReasonCode,
       "ciscoScsiFlowCfgReasonCode": ciscoScsiFlowCfgReasonCode,
       "csfStats": csfStats,
       "ciscoScsiFlowStatsTable": ciscoScsiFlowStatsTable,
       "ciscoScsiFlowStatsEntry": ciscoScsiFlowStatsEntry,
       "ciscoScsiFlowLunId": ciscoScsiFlowLunId,
       "ciscoScsiFlowRdIos": ciscoScsiFlowRdIos,
       "ciscoScsiFlowRdFailedIos": ciscoScsiFlowRdFailedIos,
       "ciscoScsiFlowRdTimeouts": ciscoScsiFlowRdTimeouts,
       "ciscoScsiFlowRdBlocks": ciscoScsiFlowRdBlocks,
       "ciscoScsiFlowRdMaxBlocks": ciscoScsiFlowRdMaxBlocks,
       "ciscoScsiFlowRdMinTime": ciscoScsiFlowRdMinTime,
       "ciscoScsiFlowRdMaxTime": ciscoScsiFlowRdMaxTime,
       "ciscoScsiFlowRdsActive": ciscoScsiFlowRdsActive,
       "ciscoScsiFlowWrIos": ciscoScsiFlowWrIos,
       "ciscoScsiFlowWrFailedIos": ciscoScsiFlowWrFailedIos,
       "ciscoScsiFlowWrTimeouts": ciscoScsiFlowWrTimeouts,
       "ciscoScsiFlowWrBlocks": ciscoScsiFlowWrBlocks,
       "ciscoScsiFlowWrMaxBlocks": ciscoScsiFlowWrMaxBlocks,
       "ciscoScsiFlowWrMinTime": ciscoScsiFlowWrMinTime,
       "ciscoScsiFlowWrMaxTime": ciscoScsiFlowWrMaxTime,
       "ciscoScsiFlowWrsActive": ciscoScsiFlowWrsActive,
       "ciscoScsiFlowTestUnitRdys": ciscoScsiFlowTestUnitRdys,
       "ciscoScsiFlowRepLuns": ciscoScsiFlowRepLuns,
       "ciscoScsiFlowInquirys": ciscoScsiFlowInquirys,
       "ciscoScsiFlowRdCapacitys": ciscoScsiFlowRdCapacitys,
       "ciscoScsiFlowModeSenses": ciscoScsiFlowModeSenses,
       "ciscoScsiFlowReqSenses": ciscoScsiFlowReqSenses,
       "ciscoScsiFlowRxFc2Frames": ciscoScsiFlowRxFc2Frames,
       "ciscoScsiFlowTxFc2Frames": ciscoScsiFlowTxFc2Frames,
       "ciscoScsiFlowRxFc2Octets": ciscoScsiFlowRxFc2Octets,
       "ciscoScsiFlowTxFc2Octets": ciscoScsiFlowTxFc2Octets,
       "ciscoScsiFlowBusyStatuses": ciscoScsiFlowBusyStatuses,
       "ciscoScsiFlowStatusResvConfs": ciscoScsiFlowStatusResvConfs,
       "ciscoScsiFlowTskSetFulStatuses": ciscoScsiFlowTskSetFulStatuses,
       "ciscoScsiFlowAcaActiveStatuses": ciscoScsiFlowAcaActiveStatuses,
       "ciscoScsiFlowSenseKeyNotRdyErrs": ciscoScsiFlowSenseKeyNotRdyErrs,
       "ciscoScsiFlowSenseKeyMedErrs": ciscoScsiFlowSenseKeyMedErrs,
       "ciscoScsiFlowSenseKeyHwErrs": ciscoScsiFlowSenseKeyHwErrs,
       "ciscoScsiFlowSenseKeyIllReqErrs": ciscoScsiFlowSenseKeyIllReqErrs,
       "ciscoScsiFlowSenseKeyUnitAttErrs": ciscoScsiFlowSenseKeyUnitAttErrs,
       "ciscoScsiFlowSenseKeyDatProtErrs": ciscoScsiFlowSenseKeyDatProtErrs,
       "ciscoScsiFlowSenseKeyBlankErrs": ciscoScsiFlowSenseKeyBlankErrs,
       "ciscoScsiFlowSenseKeyCpAbrtErrs": ciscoScsiFlowSenseKeyCpAbrtErrs,
       "ciscoScsiFlowSenseKeyAbrtCmdErrs": ciscoScsiFlowSenseKeyAbrtCmdErrs,
       "ciscoScsiFlowSenseKeyVolFlowErrs": ciscoScsiFlowSenseKeyVolFlowErrs,
       "ciscoScsiFlowSenseKeyMiscmpErrs": ciscoScsiFlowSenseKeyMiscmpErrs,
       "ciscoScsiFlowAbts": ciscoScsiFlowAbts,
       "csfFeatureStatus": csfFeatureStatus,
       "ciscoScsiFlowWrAccStatusTable": ciscoScsiFlowWrAccStatusTable,
       "ciscoScsiFlowWrAccStatusEntry": ciscoScsiFlowWrAccStatusEntry,
       "ciscoScsiFlowWrAccCfgStatus": ciscoScsiFlowWrAccCfgStatus,
       "ciscoScsiFlowWrAccIntrCfgStatus": ciscoScsiFlowWrAccIntrCfgStatus,
       "ciscoScsiFlowWrAccTgtCfgStatus": ciscoScsiFlowWrAccTgtCfgStatus,
       "ciscoScsiFlowStatsStatusTable": ciscoScsiFlowStatsStatusTable,
       "ciscoScsiFlowStatsStatusEntry": ciscoScsiFlowStatsStatusEntry,
       "ciscoScsiFlowStatsCfgStatus": ciscoScsiFlowStatsCfgStatus,
       "ciscoScsiFlowStatsIntrCfgStatus": ciscoScsiFlowStatsIntrCfgStatus,
       "ciscoScsiFlowStatsTgtCfgStatus": ciscoScsiFlowStatsTgtCfgStatus,
       "ciscoScsiFlowMIBConform": ciscoScsiFlowMIBConform,
       "ciscoScsiFlowMIBCompliances": ciscoScsiFlowMIBCompliances,
       "ciscoScsiFlowMIBCompliance": ciscoScsiFlowMIBCompliance,
       "ciscoScsiFlowMIBGroups": ciscoScsiFlowMIBGroups,
       "ciscoScsiFlowGroup": ciscoScsiFlowGroup,
       "ciscoScsiFlowStatsGroup": ciscoScsiFlowStatsGroup,
       "ciscoScsiFlowInfoGroup": ciscoScsiFlowInfoGroup,
       "ciscoScsiFlowNotifyGroup": ciscoScsiFlowNotifyGroup,
       "ciscoScsiFlowFeatureStatusGroup": ciscoScsiFlowFeatureStatusGroup}
)
