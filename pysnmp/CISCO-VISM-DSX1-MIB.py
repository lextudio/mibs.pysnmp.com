# SNMP MIB module (CISCO-VISM-DSX1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VISM-DSX1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:51 2024
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

(dsx1,) = mibBuilder.importSymbols(
    "BASIS-MIB",
    "dsx1")

(dsx1AlmGrp,) = mibBuilder.importSymbols(
    "CISCO-MGX82XX-DSX1-MIB",
    "dsx1AlmGrp")

(ciscoWan,) = mibBuilder.importSymbols(
    "CISCOWAN-SMI",
    "ciscoWan")

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

ciscoVismDsx1MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 79)
)
ciscoVismDsx1MIB.setRevisions(
        ("2005-09-30 00:00",
         "2005-01-20 00:00",
         "2004-04-16 00:00",
         "2004-03-09 00:00",
         "2004-02-17 00:00",
         "2004-02-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Dsx1AlmHistoryTable_Object = MibTable
dsx1AlmHistoryTable = _Dsx1AlmHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dsx1AlmHistoryTable.setStatus("current")
_Dsx1AlmHistoryEntry_Object = MibTableRow
dsx1AlmHistoryEntry = _Dsx1AlmHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1)
)
dsx1AlmHistoryEntry.setIndexNames(
    (0, "CISCO-VISM-DSX1-MIB", "almlineNumber"),
    (0, "CISCO-VISM-DSX1-MIB", "almIntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx1AlmHistoryEntry.setStatus("current")


class _AlmlineNumber_Type(Integer32):
    """Custom type almlineNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AlmlineNumber_Type.__name__ = "Integer32"
_AlmlineNumber_Object = MibTableColumn
almlineNumber = _AlmlineNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 1),
    _AlmlineNumber_Type()
)
almlineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almlineNumber.setStatus("current")


class _AlmIntervalNumber_Type(Integer32):
    """Custom type almIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_AlmIntervalNumber_Type.__name__ = "Integer32"
_AlmIntervalNumber_Object = MibTableColumn
almIntervalNumber = _AlmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 2),
    _AlmIntervalNumber_Type()
)
almIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    almIntervalNumber.setStatus("current")
_LCV_Type = Counter32
_LCV_Object = MibTableColumn
lCV = _LCV_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 3),
    _LCV_Type()
)
lCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lCV.setStatus("current")
_LES_Type = Counter32
_LES_Object = MibTableColumn
lES = _LES_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 4),
    _LES_Type()
)
lES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lES.setStatus("current")
_LSES_Type = Counter32
_LSES_Object = MibTableColumn
lSES = _LSES_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 5),
    _LSES_Type()
)
lSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lSES.setStatus("current")
_CRC_Type = Counter32
_CRC_Object = MibTableColumn
cRC = _CRC_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 6),
    _CRC_Type()
)
cRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRC.setStatus("current")
_CRCES_Type = Counter32
_CRCES_Object = MibTableColumn
cRCES = _CRCES_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 7),
    _CRCES_Type()
)
cRCES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCES.setStatus("current")
_CRCSES_Type = Counter32
_CRCSES_Object = MibTableColumn
cRCSES = _CRCSES_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 8),
    _CRCSES_Type()
)
cRCSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRCSES.setStatus("current")
_SEFS_Type = Counter32
_SEFS_Object = MibTableColumn
sEFS = _SEFS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 9),
    _SEFS_Type()
)
sEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sEFS.setStatus("current")
_AISS_Type = Counter32
_AISS_Object = MibTableColumn
aISS = _AISS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 10),
    _AISS_Type()
)
aISS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aISS.setStatus("current")
_UAS_Type = Counter32
_UAS_Object = MibTableColumn
uAS = _UAS_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 11),
    _UAS_Type()
)
uAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uAS.setStatus("current")


class _PercentErrorFreeSecs_Type(Integer32):
    """Custom type percentErrorFreeSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PercentErrorFreeSecs_Type.__name__ = "Integer32"
_PercentErrorFreeSecs_Object = MibTableColumn
percentErrorFreeSecs = _PercentErrorFreeSecs_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 12),
    _PercentErrorFreeSecs_Type()
)
percentErrorFreeSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    percentErrorFreeSecs.setStatus("current")
_RcvLOSCnt_Type = Counter32
_RcvLOSCnt_Object = MibTableColumn
rcvLOSCnt = _RcvLOSCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 13),
    _RcvLOSCnt_Type()
)
rcvLOSCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvLOSCnt.setStatus("current")
_RcvOOFCnt_Type = Counter32
_RcvOOFCnt_Object = MibTableColumn
rcvOOFCnt = _RcvOOFCnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 14),
    _RcvOOFCnt_Type()
)
rcvOOFCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvOOFCnt.setStatus("current")
_RcvRAICnt_Type = Counter32
_RcvRAICnt_Object = MibTableColumn
rcvRAICnt = _RcvRAICnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 15),
    _RcvRAICnt_Type()
)
rcvRAICnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvRAICnt.setStatus("current")
_RcvFECnt_Type = Counter32
_RcvFECnt_Object = MibTableColumn
rcvFECnt = _RcvFECnt_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 16),
    _RcvFECnt_Type()
)
rcvFECnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcvFECnt.setStatus("current")


class _Dsx1AlmClrButton_Type(Integer32):
    """Custom type dsx1AlmClrButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("noaction", 1))
    )


_Dsx1AlmClrButton_Type.__name__ = "Integer32"
_Dsx1AlmClrButton_Object = MibTableColumn
dsx1AlmClrButton = _Dsx1AlmClrButton_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 17),
    _Dsx1AlmClrButton_Type()
)
dsx1AlmClrButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1AlmClrButton.setStatus("current")
_Dsx1TxUncontrolledSlips_Type = Counter32
_Dsx1TxUncontrolledSlips_Object = MibTableColumn
dsx1TxUncontrolledSlips = _Dsx1TxUncontrolledSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 18),
    _Dsx1TxUncontrolledSlips_Type()
)
dsx1TxUncontrolledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TxUncontrolledSlips.setStatus("current")
_Dsx1RxUncontrolledSlips_Type = Counter32
_Dsx1RxUncontrolledSlips_Object = MibTableColumn
dsx1RxUncontrolledSlips = _Dsx1RxUncontrolledSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 19),
    _Dsx1RxUncontrolledSlips_Type()
)
dsx1RxUncontrolledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1RxUncontrolledSlips.setStatus("current")
_Dsx1TxFrameSlips_Type = Counter32
_Dsx1TxFrameSlips_Object = MibTableColumn
dsx1TxFrameSlips = _Dsx1TxFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 20),
    _Dsx1TxFrameSlips_Type()
)
dsx1TxFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TxFrameSlips.setStatus("current")
_Dsx1RxFrameSlips_Type = Counter32
_Dsx1RxFrameSlips_Object = MibTableColumn
dsx1RxFrameSlips = _Dsx1RxFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 1, 3, 2, 1, 21),
    _Dsx1RxFrameSlips_Type()
)
dsx1RxFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1RxFrameSlips.setStatus("current")
_Dsx1Vism_ObjectIdentity = ObjectIdentity
dsx1Vism = _Dsx1Vism_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5)
)
_Dsx1VismCnfGrp_ObjectIdentity = ObjectIdentity
dsx1VismCnfGrp = _Dsx1VismCnfGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1)
)
_Dsx1VismCnfGrpTable_Object = MibTable
dsx1VismCnfGrpTable = _Dsx1VismCnfGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    dsx1VismCnfGrpTable.setStatus("current")
_Dsx1VismCnfGrpEntry_Object = MibTableRow
dsx1VismCnfGrpEntry = _Dsx1VismCnfGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1)
)
dsx1VismCnfGrpEntry.setIndexNames(
    (0, "CISCO-VISM-DSX1-MIB", "vismLineNum"),
)
if mibBuilder.loadTexts:
    dsx1VismCnfGrpEntry.setStatus("current")


class _VismLineNum_Type(Integer32):
    """Custom type vismLineNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_VismLineNum_Type.__name__ = "Integer32"
_VismLineNum_Object = MibTableColumn
vismLineNum = _VismLineNum_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 1),
    _VismLineNum_Type()
)
vismLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismLineNum.setStatus("current")


class _VismEcanEnabled_Type(Integer32):
    """Custom type vismEcanEnabled based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VismEcanEnabled_Type.__name__ = "Integer32"
_VismEcanEnabled_Object = MibTableColumn
vismEcanEnabled = _VismEcanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 2),
    _VismEcanEnabled_Type()
)
vismEcanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismEcanEnabled.setStatus("current")


class _VismEcanToneDisable_Type(Integer32):
    """Custom type vismEcanToneDisable based on Integer32"""
    defaultValue = 4

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
        *(("g-164", 2),
          ("g-165", 4),
          ("ignore", 1),
          ("reserve", 3))
    )


_VismEcanToneDisable_Type.__name__ = "Integer32"
_VismEcanToneDisable_Object = MibTableColumn
vismEcanToneDisable = _VismEcanToneDisable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 3),
    _VismEcanToneDisable_Type()
)
vismEcanToneDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismEcanToneDisable.setStatus("deprecated")


class _VismEcanCnfNRN_Type(Integer32):
    """Custom type vismEcanCnfNRN based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reenableOnCallEnd", 2),
          ("reenableOnModemData", 1))
    )


_VismEcanCnfNRN_Type.__name__ = "Integer32"
_VismEcanCnfNRN_Object = MibTableColumn
vismEcanCnfNRN = _VismEcanCnfNRN_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 4),
    _VismEcanCnfNRN_Type()
)
vismEcanCnfNRN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismEcanCnfNRN.setStatus("deprecated")


class _VismEcanTail_Type(Integer32):
    """Custom type vismEcanTail based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 128),
    )


_VismEcanTail_Type.__name__ = "Integer32"
_VismEcanTail_Object = MibTableColumn
vismEcanTail = _VismEcanTail_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 5),
    _VismEcanTail_Type()
)
vismEcanTail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismEcanTail.setStatus("current")
if mibBuilder.loadTexts:
    vismEcanTail.setUnits("milliseconds")


class _VismEcanREC_Type(Integer32):
    """Custom type vismEcanREC based on Integer32"""
    defaultValue = 2

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
        *(("cancelOnly", 1),
          ("comfortNoise", 4),
          ("reserved", 3),
          ("suppressResidual", 2))
    )


_VismEcanREC_Type.__name__ = "Integer32"
_VismEcanREC_Object = MibTableColumn
vismEcanREC = _VismEcanREC_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 6),
    _VismEcanREC_Type()
)
vismEcanREC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismEcanREC.setStatus("current")


class _VismCompCnfVAD_Type(Integer32):
    """Custom type vismCompCnfVAD based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_VismCompCnfVAD_Type.__name__ = "Integer32"
_VismCompCnfVAD_Object = MibTableColumn
vismCompCnfVAD = _VismCompCnfVAD_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 7),
    _VismCompCnfVAD_Type()
)
vismCompCnfVAD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCompCnfVAD.setStatus("current")


class _VismSignalingType_Type(Integer32):
    """Custom type vismSignalingType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cas", 1),
          ("ccs", 2),
          ("none", 3))
    )


_VismSignalingType_Type.__name__ = "Integer32"
_VismSignalingType_Object = MibTableColumn
vismSignalingType = _VismSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 8),
    _VismSignalingType_Type()
)
vismSignalingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismSignalingType.setStatus("current")


class _VismCcsChannels_Type(Integer32):
    """Custom type vismCcsChannels based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismCcsChannels_Type.__name__ = "Integer32"
_VismCcsChannels_Object = MibTableColumn
vismCcsChannels = _VismCcsChannels_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 9),
    _VismCcsChannels_Type()
)
vismCcsChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismCcsChannels.setStatus("current")


class _VismCadenceTime_Type(Integer32):
    """Custom type vismCadenceTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_VismCadenceTime_Type.__name__ = "Integer32"
_VismCadenceTime_Object = MibTableColumn
vismCadenceTime = _VismCadenceTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 10),
    _VismCadenceTime_Type()
)
vismCadenceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismCadenceTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    vismCadenceTime.setUnits("milliseconds")


class _VismTrunkConditionEnable_Type(TruthValue):
    """Custom type vismTrunkConditionEnable based on TruthValue"""


_VismTrunkConditionEnable_Object = MibTableColumn
vismTrunkConditionEnable = _VismTrunkConditionEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 11),
    _VismTrunkConditionEnable_Type()
)
vismTrunkConditionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismTrunkConditionEnable.setStatus("current")
_VismDsx1CircuitIdentifier_Type = DisplayString
_VismDsx1CircuitIdentifier_Object = MibTableColumn
vismDsx1CircuitIdentifier = _VismDsx1CircuitIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 12),
    _VismDsx1CircuitIdentifier_Type()
)
vismDsx1CircuitIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1CircuitIdentifier.setStatus("current")


class _VismDsx1TxDigitOrder_Type(Integer32):
    """Custom type vismDsx1TxDigitOrder based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aniThenDnis", 1),
          ("dnisThenAni", 2))
    )


_VismDsx1TxDigitOrder_Type.__name__ = "Integer32"
_VismDsx1TxDigitOrder_Object = MibTableColumn
vismDsx1TxDigitOrder = _VismDsx1TxDigitOrder_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 13),
    _VismDsx1TxDigitOrder_Type()
)
vismDsx1TxDigitOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1TxDigitOrder.setStatus("current")


class _VismDsx1TonePlanRegion_Type(DisplayString):
    """Custom type vismDsx1TonePlanRegion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_VismDsx1TonePlanRegion_Type.__name__ = "DisplayString"
_VismDsx1TonePlanRegion_Object = MibTableColumn
vismDsx1TonePlanRegion = _VismDsx1TonePlanRegion_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 14),
    _VismDsx1TonePlanRegion_Type()
)
vismDsx1TonePlanRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1TonePlanRegion.setStatus("current")


class _VismDsx1TonePlanVersion_Type(Integer32):
    """Custom type vismDsx1TonePlanVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismDsx1TonePlanVersion_Type.__name__ = "Integer32"
_VismDsx1TonePlanVersion_Object = MibTableColumn
vismDsx1TonePlanVersion = _VismDsx1TonePlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 15),
    _VismDsx1TonePlanVersion_Type()
)
vismDsx1TonePlanVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1TonePlanVersion.setStatus("current")


class _VismDsx1RingingTO_Type(Integer32):
    """Custom type vismDsx1RingingTO based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VismDsx1RingingTO_Type.__name__ = "Integer32"
_VismDsx1RingingTO_Object = MibTableColumn
vismDsx1RingingTO = _VismDsx1RingingTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 16),
    _VismDsx1RingingTO_Type()
)
vismDsx1RingingTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1RingingTO.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1RingingTO.setUnits("seconds")


class _VismDsx1RingBackTO_Type(Integer32):
    """Custom type vismDsx1RingBackTO based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VismDsx1RingBackTO_Type.__name__ = "Integer32"
_VismDsx1RingBackTO_Object = MibTableColumn
vismDsx1RingBackTO = _VismDsx1RingBackTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 17),
    _VismDsx1RingBackTO_Type()
)
vismDsx1RingBackTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1RingBackTO.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1RingBackTO.setUnits("seconds")


class _VismDsx1BusyTO_Type(Integer32):
    """Custom type vismDsx1BusyTO based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VismDsx1BusyTO_Type.__name__ = "Integer32"
_VismDsx1BusyTO_Object = MibTableColumn
vismDsx1BusyTO = _VismDsx1BusyTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 18),
    _VismDsx1BusyTO_Type()
)
vismDsx1BusyTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1BusyTO.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1BusyTO.setUnits("seconds")


class _VismDsx1ReorderTO_Type(Integer32):
    """Custom type vismDsx1ReorderTO based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VismDsx1ReorderTO_Type.__name__ = "Integer32"
_VismDsx1ReorderTO_Object = MibTableColumn
vismDsx1ReorderTO = _VismDsx1ReorderTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 19),
    _VismDsx1ReorderTO_Type()
)
vismDsx1ReorderTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1ReorderTO.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1ReorderTO.setUnits("seconds")


class _VismDsx1DialTO_Type(Integer32):
    """Custom type vismDsx1DialTO based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VismDsx1DialTO_Type.__name__ = "Integer32"
_VismDsx1DialTO_Object = MibTableColumn
vismDsx1DialTO = _VismDsx1DialTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 20),
    _VismDsx1DialTO_Type()
)
vismDsx1DialTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1DialTO.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1DialTO.setUnits("seconds")


class _VismDsx1StutterDialTO_Type(Integer32):
    """Custom type vismDsx1StutterDialTO based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VismDsx1StutterDialTO_Type.__name__ = "Integer32"
_VismDsx1StutterDialTO_Object = MibTableColumn
vismDsx1StutterDialTO = _VismDsx1StutterDialTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 21),
    _VismDsx1StutterDialTO_Type()
)
vismDsx1StutterDialTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1StutterDialTO.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1StutterDialTO.setUnits("seconds")


class _VismDsx1OffHookAlertTO_Type(Integer32):
    """Custom type vismDsx1OffHookAlertTO based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_VismDsx1OffHookAlertTO_Type.__name__ = "Integer32"
_VismDsx1OffHookAlertTO_Object = MibTableColumn
vismDsx1OffHookAlertTO = _VismDsx1OffHookAlertTO_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 22),
    _VismDsx1OffHookAlertTO_Type()
)
vismDsx1OffHookAlertTO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1OffHookAlertTO.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1OffHookAlertTO.setUnits("seconds")


class _VismDsx1RemoteRingback_Type(Integer32):
    """Custom type vismDsx1RemoteRingback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inband", 2),
          ("proxy", 1))
    )


_VismDsx1RemoteRingback_Type.__name__ = "Integer32"
_VismDsx1RemoteRingback_Object = MibTableColumn
vismDsx1RemoteRingback = _VismDsx1RemoteRingback_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 23),
    _VismDsx1RemoteRingback_Type()
)
vismDsx1RemoteRingback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1RemoteRingback.setStatus("current")


class _VismDsx1MidcallTpart_Type(Integer32):
    """Custom type vismDsx1MidcallTpart based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 10000),
    )


_VismDsx1MidcallTpart_Type.__name__ = "Integer32"
_VismDsx1MidcallTpart_Object = MibTableColumn
vismDsx1MidcallTpart = _VismDsx1MidcallTpart_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 24),
    _VismDsx1MidcallTpart_Type()
)
vismDsx1MidcallTpart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1MidcallTpart.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1MidcallTpart.setUnits("seconds")


class _VismDsx1MidcallTcrit_Type(Integer32):
    """Custom type vismDsx1MidcallTcrit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VismDsx1MidcallTcrit_Type.__name__ = "Integer32"
_VismDsx1MidcallTcrit_Object = MibTableColumn
vismDsx1MidcallTcrit = _VismDsx1MidcallTcrit_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 25),
    _VismDsx1MidcallTcrit_Type()
)
vismDsx1MidcallTcrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1MidcallTcrit.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1MidcallTcrit.setUnits("seconds")


class _VismDsx1Sa4Byte_Type(Integer32):
    """Custom type vismDsx1Sa4Byte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismDsx1Sa4Byte_Type.__name__ = "Integer32"
_VismDsx1Sa4Byte_Object = MibTableColumn
vismDsx1Sa4Byte = _VismDsx1Sa4Byte_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 26),
    _VismDsx1Sa4Byte_Type()
)
vismDsx1Sa4Byte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1Sa4Byte.setStatus("current")


class _VismDsx1Sa5Byte_Type(Integer32):
    """Custom type vismDsx1Sa5Byte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismDsx1Sa5Byte_Type.__name__ = "Integer32"
_VismDsx1Sa5Byte_Object = MibTableColumn
vismDsx1Sa5Byte = _VismDsx1Sa5Byte_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 27),
    _VismDsx1Sa5Byte_Type()
)
vismDsx1Sa5Byte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1Sa5Byte.setStatus("current")


class _VismDsx1Sa6Byte_Type(Integer32):
    """Custom type vismDsx1Sa6Byte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismDsx1Sa6Byte_Type.__name__ = "Integer32"
_VismDsx1Sa6Byte_Object = MibTableColumn
vismDsx1Sa6Byte = _VismDsx1Sa6Byte_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 28),
    _VismDsx1Sa6Byte_Type()
)
vismDsx1Sa6Byte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1Sa6Byte.setStatus("current")


class _VismDsx1Sa7Byte_Type(Integer32):
    """Custom type vismDsx1Sa7Byte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismDsx1Sa7Byte_Type.__name__ = "Integer32"
_VismDsx1Sa7Byte_Object = MibTableColumn
vismDsx1Sa7Byte = _VismDsx1Sa7Byte_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 29),
    _VismDsx1Sa7Byte_Type()
)
vismDsx1Sa7Byte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1Sa7Byte.setStatus("current")


class _VismDsx1Sa8Byte_Type(Integer32):
    """Custom type vismDsx1Sa8Byte based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismDsx1Sa8Byte_Type.__name__ = "Integer32"
_VismDsx1Sa8Byte_Object = MibTableColumn
vismDsx1Sa8Byte = _VismDsx1Sa8Byte_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 30),
    _VismDsx1Sa8Byte_Type()
)
vismDsx1Sa8Byte.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1Sa8Byte.setStatus("current")


class _VismDsx1State_Type(Integer32):
    """Custom type vismDsx1State based on Integer32"""
    defaultValue = 6

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
        *(("coos", 5),
          ("inactive", 6),
          ("invalid", 1),
          ("is", 2),
          ("oos", 3),
          ("poos", 4))
    )


_VismDsx1State_Type.__name__ = "Integer32"
_VismDsx1State_Object = MibTableColumn
vismDsx1State = _VismDsx1State_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 31),
    _VismDsx1State_Type()
)
vismDsx1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDsx1State.setStatus("current")


class _VismDsx1AdminStateControl_Type(Integer32):
    """Custom type vismDsx1AdminStateControl based on Integer32"""
    defaultValue = 4

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
        *(("forcefulOutOfService", 2),
          ("gracefulOutOfService", 3),
          ("inService", 1),
          ("inactive", 4))
    )


_VismDsx1AdminStateControl_Type.__name__ = "Integer32"
_VismDsx1AdminStateControl_Object = MibTableColumn
vismDsx1AdminStateControl = _VismDsx1AdminStateControl_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 32),
    _VismDsx1AdminStateControl_Type()
)
vismDsx1AdminStateControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1AdminStateControl.setStatus("current")


class _VismBearerBusyCode_Type(Integer32):
    """Custom type vismBearerBusyCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VismBearerBusyCode_Type.__name__ = "Integer32"
_VismBearerBusyCode_Object = MibTableColumn
vismBearerBusyCode = _VismBearerBusyCode_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 33),
    _VismBearerBusyCode_Type()
)
vismBearerBusyCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismBearerBusyCode.setStatus("current")


class _VismDsx1V110Enable_Type(TruthValue):
    """Custom type vismDsx1V110Enable based on TruthValue"""


_VismDsx1V110Enable_Object = MibTableColumn
vismDsx1V110Enable = _VismDsx1V110Enable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 34),
    _VismDsx1V110Enable_Type()
)
vismDsx1V110Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1V110Enable.setStatus("current")


class _VismDsx1AlarmLogEnable_Type(TruthValue):
    """Custom type vismDsx1AlarmLogEnable based on TruthValue"""


_VismDsx1AlarmLogEnable_Object = MibTableColumn
vismDsx1AlarmLogEnable = _VismDsx1AlarmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 35),
    _VismDsx1AlarmLogEnable_Type()
)
vismDsx1AlarmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1AlarmLogEnable.setStatus("current")


class _VismDsx1AlarmLogAdminTimer_Type(Unsigned32):
    """Custom type vismDsx1AlarmLogAdminTimer based on Unsigned32"""
    defaultValue = 7200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismDsx1AlarmLogAdminTimer_Type.__name__ = "Unsigned32"
_VismDsx1AlarmLogAdminTimer_Object = MibTableColumn
vismDsx1AlarmLogAdminTimer = _VismDsx1AlarmLogAdminTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 36),
    _VismDsx1AlarmLogAdminTimer_Type()
)
vismDsx1AlarmLogAdminTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1AlarmLogAdminTimer.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1AlarmLogAdminTimer.setUnits("minutes")


class _VismDsx1AlarmLogOperTimer_Type(Unsigned32):
    """Custom type vismDsx1AlarmLogOperTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VismDsx1AlarmLogOperTimer_Type.__name__ = "Unsigned32"
_VismDsx1AlarmLogOperTimer_Object = MibTableColumn
vismDsx1AlarmLogOperTimer = _VismDsx1AlarmLogOperTimer_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 37),
    _VismDsx1AlarmLogOperTimer_Type()
)
vismDsx1AlarmLogOperTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDsx1AlarmLogOperTimer.setStatus("current")
if mibBuilder.loadTexts:
    vismDsx1AlarmLogOperTimer.setUnits("minutes")


class _VismDsx1ElectricalSignalEnable_Type(TruthValue):
    """Custom type vismDsx1ElectricalSignalEnable based on TruthValue"""


_VismDsx1ElectricalSignalEnable_Object = MibTableColumn
vismDsx1ElectricalSignalEnable = _VismDsx1ElectricalSignalEnable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 1, 1, 1, 38),
    _VismDsx1ElectricalSignalEnable_Type()
)
vismDsx1ElectricalSignalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vismDsx1ElectricalSignalEnable.setStatus("current")
_Dsx1VismStatsGrp_ObjectIdentity = ObjectIdentity
dsx1VismStatsGrp = _Dsx1VismStatsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2)
)
_Dsx1VismStatsGrpTable_Object = MibTable
dsx1VismStatsGrpTable = _Dsx1VismStatsGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    dsx1VismStatsGrpTable.setStatus("current")
_Dsx1VismStatsGrpEntry_Object = MibTableRow
dsx1VismStatsGrpEntry = _Dsx1VismStatsGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsx1VismStatsGrpEntry.setStatus("current")
_VismDsx1TotalTxUncontrolledSlips_Type = Counter32
_VismDsx1TotalTxUncontrolledSlips_Object = MibTableColumn
vismDsx1TotalTxUncontrolledSlips = _VismDsx1TotalTxUncontrolledSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2, 1, 1, 1),
    _VismDsx1TotalTxUncontrolledSlips_Type()
)
vismDsx1TotalTxUncontrolledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDsx1TotalTxUncontrolledSlips.setStatus("current")
_VismDsx1TotalTxFrameSlips_Type = Counter32
_VismDsx1TotalTxFrameSlips_Object = MibTableColumn
vismDsx1TotalTxFrameSlips = _VismDsx1TotalTxFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2, 1, 1, 2),
    _VismDsx1TotalTxFrameSlips_Type()
)
vismDsx1TotalTxFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDsx1TotalTxFrameSlips.setStatus("current")
_VismDsx1TotalRxUncontrolledSlips_Type = Counter32
_VismDsx1TotalRxUncontrolledSlips_Object = MibTableColumn
vismDsx1TotalRxUncontrolledSlips = _VismDsx1TotalRxUncontrolledSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2, 1, 1, 3),
    _VismDsx1TotalRxUncontrolledSlips_Type()
)
vismDsx1TotalRxUncontrolledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDsx1TotalRxUncontrolledSlips.setStatus("current")
_VismDsx1TotalRxFrameSlips_Type = Counter32
_VismDsx1TotalRxFrameSlips_Object = MibTableColumn
vismDsx1TotalRxFrameSlips = _VismDsx1TotalRxFrameSlips_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2, 1, 1, 4),
    _VismDsx1TotalRxFrameSlips_Type()
)
vismDsx1TotalRxFrameSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismDsx1TotalRxFrameSlips.setStatus("current")


class _VismSlipCntDiscontinuityTime_Type(TimeStamp):
    """Custom type vismSlipCntDiscontinuityTime based on TimeStamp"""
    defaultValue = 0


_VismSlipCntDiscontinuityTime_Object = MibTableColumn
vismSlipCntDiscontinuityTime = _VismSlipCntDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 351, 110, 4, 3, 5, 2, 1, 1, 5),
    _VismSlipCntDiscontinuityTime_Type()
)
vismSlipCntDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vismSlipCntDiscontinuityTime.setStatus("current")
_CvDsx1MIBConformance_ObjectIdentity = ObjectIdentity
cvDsx1MIBConformance = _CvDsx1MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2)
)
_CvDsx1MIBGroups_ObjectIdentity = ObjectIdentity
cvDsx1MIBGroups = _CvDsx1MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1)
)
_CvDsx1MIBCompliances_ObjectIdentity = ObjectIdentity
cvDsx1MIBCompliances = _CvDsx1MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 2)
)
dsx1VismCnfGrpEntry.registerAugmentions(
    ("CISCO-VISM-DSX1-MIB",
     "dsx1VismStatsGrpEntry")
)
dsx1VismStatsGrpEntry.setIndexNames(*dsx1VismCnfGrpEntry.getIndexNames())

# Managed Objects groups

cvDsx1ConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 1)
)
cvDsx1ConfGroup.setObjects(
      *(("CISCO-VISM-DSX1-MIB", "vismLineNum"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanEnabled"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanToneDisable"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanCnfNRN"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanTail"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanREC"),
        ("CISCO-VISM-DSX1-MIB", "vismCompCnfVAD"),
        ("CISCO-VISM-DSX1-MIB", "vismSignalingType"),
        ("CISCO-VISM-DSX1-MIB", "vismCcsChannels"),
        ("CISCO-VISM-DSX1-MIB", "vismCadenceTime"),
        ("CISCO-VISM-DSX1-MIB", "vismTrunkConditionEnable"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1CircuitIdentifier"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TxDigitOrder"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TonePlanRegion"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TonePlanVersion"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RingingTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RingBackTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1BusyTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1ReorderTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1DialTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1StutterDialTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1OffHookAlertTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RemoteRingback"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1MidcallTpart"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1MidcallTcrit"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa4Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa5Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa6Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa7Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa8Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1State"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1AdminStateControl"))
)
if mibBuilder.loadTexts:
    cvDsx1ConfGroup.setStatus("deprecated")

cvDsx1AlmHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 2)
)
cvDsx1AlmHistoryGroup.setObjects(
      *(("CISCO-VISM-DSX1-MIB", "almlineNumber"),
        ("CISCO-VISM-DSX1-MIB", "almIntervalNumber"),
        ("CISCO-VISM-DSX1-MIB", "lCV"),
        ("CISCO-VISM-DSX1-MIB", "lES"),
        ("CISCO-VISM-DSX1-MIB", "lSES"),
        ("CISCO-VISM-DSX1-MIB", "cRC"),
        ("CISCO-VISM-DSX1-MIB", "cRCES"),
        ("CISCO-VISM-DSX1-MIB", "cRCSES"),
        ("CISCO-VISM-DSX1-MIB", "sEFS"),
        ("CISCO-VISM-DSX1-MIB", "aISS"),
        ("CISCO-VISM-DSX1-MIB", "uAS"),
        ("CISCO-VISM-DSX1-MIB", "percentErrorFreeSecs"),
        ("CISCO-VISM-DSX1-MIB", "rcvLOSCnt"),
        ("CISCO-VISM-DSX1-MIB", "rcvOOFCnt"),
        ("CISCO-VISM-DSX1-MIB", "rcvRAICnt"),
        ("CISCO-VISM-DSX1-MIB", "rcvFECnt"),
        ("CISCO-VISM-DSX1-MIB", "dsx1AlmClrButton"))
)
if mibBuilder.loadTexts:
    cvDsx1AlmHistoryGroup.setStatus("deprecated")

cvDsx1ConfGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 3)
)
cvDsx1ConfGroupRev1.setObjects(
      *(("CISCO-VISM-DSX1-MIB", "vismLineNum"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanEnabled"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanTail"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanREC"),
        ("CISCO-VISM-DSX1-MIB", "vismCompCnfVAD"),
        ("CISCO-VISM-DSX1-MIB", "vismSignalingType"),
        ("CISCO-VISM-DSX1-MIB", "vismCcsChannels"),
        ("CISCO-VISM-DSX1-MIB", "vismTrunkConditionEnable"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1CircuitIdentifier"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TxDigitOrder"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TonePlanRegion"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TonePlanVersion"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RingingTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RingBackTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1BusyTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1ReorderTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1DialTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1StutterDialTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1OffHookAlertTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RemoteRingback"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1MidcallTpart"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1MidcallTcrit"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa4Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa5Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa6Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa7Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa8Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1State"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1AdminStateControl"))
)
if mibBuilder.loadTexts:
    cvDsx1ConfGroupRev1.setStatus("deprecated")

cvDsx1ConfGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 4)
)
cvDsx1ConfGroupRev2.setObjects(
      *(("CISCO-VISM-DSX1-MIB", "vismLineNum"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanEnabled"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanTail"),
        ("CISCO-VISM-DSX1-MIB", "vismEcanREC"),
        ("CISCO-VISM-DSX1-MIB", "vismCompCnfVAD"),
        ("CISCO-VISM-DSX1-MIB", "vismSignalingType"),
        ("CISCO-VISM-DSX1-MIB", "vismCcsChannels"),
        ("CISCO-VISM-DSX1-MIB", "vismTrunkConditionEnable"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1CircuitIdentifier"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TxDigitOrder"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TonePlanRegion"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TonePlanVersion"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RingingTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RingBackTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1BusyTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1ReorderTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1DialTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1StutterDialTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1OffHookAlertTO"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1RemoteRingback"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1MidcallTpart"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1MidcallTcrit"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa4Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa5Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa6Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa7Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1Sa8Byte"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1State"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1AdminStateControl"),
        ("CISCO-VISM-DSX1-MIB", "vismBearerBusyCode"))
)
if mibBuilder.loadTexts:
    cvDsx1ConfGroupRev2.setStatus("current")

cvDsx1AlmHistoryGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 5)
)
cvDsx1AlmHistoryGroupRev1.setObjects(
      *(("CISCO-VISM-DSX1-MIB", "almlineNumber"),
        ("CISCO-VISM-DSX1-MIB", "almIntervalNumber"),
        ("CISCO-VISM-DSX1-MIB", "lCV"),
        ("CISCO-VISM-DSX1-MIB", "lES"),
        ("CISCO-VISM-DSX1-MIB", "lSES"),
        ("CISCO-VISM-DSX1-MIB", "cRC"),
        ("CISCO-VISM-DSX1-MIB", "cRCES"),
        ("CISCO-VISM-DSX1-MIB", "cRCSES"),
        ("CISCO-VISM-DSX1-MIB", "sEFS"),
        ("CISCO-VISM-DSX1-MIB", "aISS"),
        ("CISCO-VISM-DSX1-MIB", "uAS"),
        ("CISCO-VISM-DSX1-MIB", "percentErrorFreeSecs"),
        ("CISCO-VISM-DSX1-MIB", "rcvLOSCnt"),
        ("CISCO-VISM-DSX1-MIB", "rcvOOFCnt"),
        ("CISCO-VISM-DSX1-MIB", "rcvRAICnt"),
        ("CISCO-VISM-DSX1-MIB", "rcvFECnt"),
        ("CISCO-VISM-DSX1-MIB", "dsx1AlmClrButton"),
        ("CISCO-VISM-DSX1-MIB", "dsx1TxUncontrolledSlips"),
        ("CISCO-VISM-DSX1-MIB", "dsx1TxFrameSlips"),
        ("CISCO-VISM-DSX1-MIB", "dsx1RxUncontrolledSlips"),
        ("CISCO-VISM-DSX1-MIB", "dsx1RxFrameSlips"))
)
if mibBuilder.loadTexts:
    cvDsx1AlmHistoryGroupRev1.setStatus("current")

cvDsx1StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 6)
)
cvDsx1StatsGroup.setObjects(
      *(("CISCO-VISM-DSX1-MIB", "vismDsx1TotalTxUncontrolledSlips"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TotalTxFrameSlips"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TotalRxUncontrolledSlips"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1TotalRxFrameSlips"),
        ("CISCO-VISM-DSX1-MIB", "vismSlipCntDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    cvDsx1StatsGroup.setStatus("current")

cvDsx1ConfGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 7)
)
cvDsx1ConfGroupSup1.setObjects(
    ("CISCO-VISM-DSX1-MIB", "vismDsx1V110Enable")
)
if mibBuilder.loadTexts:
    cvDsx1ConfGroupSup1.setStatus("current")

cvDsx1AlarmLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 8)
)
cvDsx1AlarmLogGroup.setObjects(
      *(("CISCO-VISM-DSX1-MIB", "vismDsx1AlarmLogEnable"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1AlarmLogAdminTimer"),
        ("CISCO-VISM-DSX1-MIB", "vismDsx1AlarmLogOperTimer"))
)
if mibBuilder.loadTexts:
    cvDsx1AlarmLogGroup.setStatus("current")

cvDsx1ElecSigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 1, 9)
)
cvDsx1ElecSigGroup.setObjects(
    ("CISCO-VISM-DSX1-MIB", "vismDsx1ElectricalSignalEnable")
)
if mibBuilder.loadTexts:
    cvDsx1ElecSigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvDsx1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cvDsx1Compliance.setStatus(
        "deprecated"
    )

cvDsx1ComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 2, 2)
)
if mibBuilder.loadTexts:
    cvDsx1ComplianceRev1.setStatus(
        "deprecated"
    )

cvDsx1ComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 2, 3)
)
if mibBuilder.loadTexts:
    cvDsx1ComplianceRev2.setStatus(
        "deprecated"
    )

cvDsx1ComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 2, 4)
)
if mibBuilder.loadTexts:
    cvDsx1ComplianceRev3.setStatus(
        "deprecated"
    )

cvDsx1ComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 2, 5)
)
if mibBuilder.loadTexts:
    cvDsx1ComplianceRev4.setStatus(
        "deprecated"
    )

cvDsx1ComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 351, 150, 79, 2, 2, 6)
)
if mibBuilder.loadTexts:
    cvDsx1ComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VISM-DSX1-MIB",
    **{"dsx1AlmHistoryTable": dsx1AlmHistoryTable,
       "dsx1AlmHistoryEntry": dsx1AlmHistoryEntry,
       "almlineNumber": almlineNumber,
       "almIntervalNumber": almIntervalNumber,
       "lCV": lCV,
       "lES": lES,
       "lSES": lSES,
       "cRC": cRC,
       "cRCES": cRCES,
       "cRCSES": cRCSES,
       "sEFS": sEFS,
       "aISS": aISS,
       "uAS": uAS,
       "percentErrorFreeSecs": percentErrorFreeSecs,
       "rcvLOSCnt": rcvLOSCnt,
       "rcvOOFCnt": rcvOOFCnt,
       "rcvRAICnt": rcvRAICnt,
       "rcvFECnt": rcvFECnt,
       "dsx1AlmClrButton": dsx1AlmClrButton,
       "dsx1TxUncontrolledSlips": dsx1TxUncontrolledSlips,
       "dsx1RxUncontrolledSlips": dsx1RxUncontrolledSlips,
       "dsx1TxFrameSlips": dsx1TxFrameSlips,
       "dsx1RxFrameSlips": dsx1RxFrameSlips,
       "dsx1Vism": dsx1Vism,
       "dsx1VismCnfGrp": dsx1VismCnfGrp,
       "dsx1VismCnfGrpTable": dsx1VismCnfGrpTable,
       "dsx1VismCnfGrpEntry": dsx1VismCnfGrpEntry,
       "vismLineNum": vismLineNum,
       "vismEcanEnabled": vismEcanEnabled,
       "vismEcanToneDisable": vismEcanToneDisable,
       "vismEcanCnfNRN": vismEcanCnfNRN,
       "vismEcanTail": vismEcanTail,
       "vismEcanREC": vismEcanREC,
       "vismCompCnfVAD": vismCompCnfVAD,
       "vismSignalingType": vismSignalingType,
       "vismCcsChannels": vismCcsChannels,
       "vismCadenceTime": vismCadenceTime,
       "vismTrunkConditionEnable": vismTrunkConditionEnable,
       "vismDsx1CircuitIdentifier": vismDsx1CircuitIdentifier,
       "vismDsx1TxDigitOrder": vismDsx1TxDigitOrder,
       "vismDsx1TonePlanRegion": vismDsx1TonePlanRegion,
       "vismDsx1TonePlanVersion": vismDsx1TonePlanVersion,
       "vismDsx1RingingTO": vismDsx1RingingTO,
       "vismDsx1RingBackTO": vismDsx1RingBackTO,
       "vismDsx1BusyTO": vismDsx1BusyTO,
       "vismDsx1ReorderTO": vismDsx1ReorderTO,
       "vismDsx1DialTO": vismDsx1DialTO,
       "vismDsx1StutterDialTO": vismDsx1StutterDialTO,
       "vismDsx1OffHookAlertTO": vismDsx1OffHookAlertTO,
       "vismDsx1RemoteRingback": vismDsx1RemoteRingback,
       "vismDsx1MidcallTpart": vismDsx1MidcallTpart,
       "vismDsx1MidcallTcrit": vismDsx1MidcallTcrit,
       "vismDsx1Sa4Byte": vismDsx1Sa4Byte,
       "vismDsx1Sa5Byte": vismDsx1Sa5Byte,
       "vismDsx1Sa6Byte": vismDsx1Sa6Byte,
       "vismDsx1Sa7Byte": vismDsx1Sa7Byte,
       "vismDsx1Sa8Byte": vismDsx1Sa8Byte,
       "vismDsx1State": vismDsx1State,
       "vismDsx1AdminStateControl": vismDsx1AdminStateControl,
       "vismBearerBusyCode": vismBearerBusyCode,
       "vismDsx1V110Enable": vismDsx1V110Enable,
       "vismDsx1AlarmLogEnable": vismDsx1AlarmLogEnable,
       "vismDsx1AlarmLogAdminTimer": vismDsx1AlarmLogAdminTimer,
       "vismDsx1AlarmLogOperTimer": vismDsx1AlarmLogOperTimer,
       "vismDsx1ElectricalSignalEnable": vismDsx1ElectricalSignalEnable,
       "dsx1VismStatsGrp": dsx1VismStatsGrp,
       "dsx1VismStatsGrpTable": dsx1VismStatsGrpTable,
       "dsx1VismStatsGrpEntry": dsx1VismStatsGrpEntry,
       "vismDsx1TotalTxUncontrolledSlips": vismDsx1TotalTxUncontrolledSlips,
       "vismDsx1TotalTxFrameSlips": vismDsx1TotalTxFrameSlips,
       "vismDsx1TotalRxUncontrolledSlips": vismDsx1TotalRxUncontrolledSlips,
       "vismDsx1TotalRxFrameSlips": vismDsx1TotalRxFrameSlips,
       "vismSlipCntDiscontinuityTime": vismSlipCntDiscontinuityTime,
       "ciscoVismDsx1MIB": ciscoVismDsx1MIB,
       "cvDsx1MIBConformance": cvDsx1MIBConformance,
       "cvDsx1MIBGroups": cvDsx1MIBGroups,
       "cvDsx1ConfGroup": cvDsx1ConfGroup,
       "cvDsx1AlmHistoryGroup": cvDsx1AlmHistoryGroup,
       "cvDsx1ConfGroupRev1": cvDsx1ConfGroupRev1,
       "cvDsx1ConfGroupRev2": cvDsx1ConfGroupRev2,
       "cvDsx1AlmHistoryGroupRev1": cvDsx1AlmHistoryGroupRev1,
       "cvDsx1StatsGroup": cvDsx1StatsGroup,
       "cvDsx1ConfGroupSup1": cvDsx1ConfGroupSup1,
       "cvDsx1AlarmLogGroup": cvDsx1AlarmLogGroup,
       "cvDsx1ElecSigGroup": cvDsx1ElecSigGroup,
       "cvDsx1MIBCompliances": cvDsx1MIBCompliances,
       "cvDsx1Compliance": cvDsx1Compliance,
       "cvDsx1ComplianceRev1": cvDsx1ComplianceRev1,
       "cvDsx1ComplianceRev2": cvDsx1ComplianceRev2,
       "cvDsx1ComplianceRev3": cvDsx1ComplianceRev3,
       "cvDsx1ComplianceRev4": cvDsx1ComplianceRev4,
       "cvDsx1ComplianceRev5": cvDsx1ComplianceRev5}
)
