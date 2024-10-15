# SNMP MIB module (DATASMART-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DATASMART-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:19 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DLCI(Integer32):
    """Custom type DLCI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )





class Counter32(Counter32):
    """Custom type Counter32 based on Counter32"""




class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Datasmart_ObjectIdentity = ObjectIdentity
datasmart = _Datasmart_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2)
)
_DsSs_ObjectIdentity = ObjectIdentity
dsSs = _DsSs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 1)
)


class _DsSsAlarmSource_Type(Integer32):
    """Custom type dsSsAlarmSource based on Integer32"""
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
        *(("ssSourceDp1", 4),
          ("ssSourceDp2", 5),
          ("ssSourceNi", 2),
          ("ssSourceNone", 1),
          ("ssSourceSystem", 6),
          ("ssSourceTi", 3))
    )


_DsSsAlarmSource_Type.__name__ = "Integer32"
_DsSsAlarmSource_Object = MibScalar
dsSsAlarmSource = _DsSsAlarmSource_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 1, 1),
    _DsSsAlarmSource_Type()
)
dsSsAlarmSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSsAlarmSource.setStatus("mandatory")


class _DsSsAlarmState_Type(Integer32):
    """Custom type dsSsAlarmState based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("ssStateAis", 4),
          ("ssStateBer", 6),
          ("ssStateDds", 12),
          ("ssStateEcf", 2),
          ("ssStateEer", 11),
          ("ssStateLos", 3),
          ("ssStateNone", 1),
          ("ssStateOmf", 10),
          ("ssStateOof", 5),
          ("ssStateOos", 13),
          ("ssStateRfa", 8),
          ("ssStateRma", 9),
          ("ssStateYel", 7))
    )


_DsSsAlarmState_Type.__name__ = "Integer32"
_DsSsAlarmState_Object = MibScalar
dsSsAlarmState = _DsSsAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 1, 2),
    _DsSsAlarmState_Type()
)
dsSsAlarmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSsAlarmState.setStatus("mandatory")


class _DsSsLoopback_Type(Integer32):
    """Custom type dsSsLoopback based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("ssLbkCsu", 14),
          ("ssLbkDp1", 10),
          ("ssLbkDp2", 11),
          ("ssLbkDpdt", 16),
          ("ssLbkDsu", 15),
          ("ssLbkDt1", 12),
          ("ssLbkDt2", 13),
          ("ssLbkLlb", 6),
          ("ssLbkLoc", 7),
          ("ssLbkNone", 1),
          ("ssLbkPlb", 8),
          ("ssLbkRemDp1", 4),
          ("ssLbkRemDp2", 5),
          ("ssLbkRemLlb", 2),
          ("ssLbkRemPlb", 3),
          ("ssLbkTlb", 9))
    )


_DsSsLoopback_Type.__name__ = "Integer32"
_DsSsLoopback_Object = MibScalar
dsSsLoopback = _DsSsLoopback_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 1, 3),
    _DsSsLoopback_Type()
)
dsSsLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSsLoopback.setStatus("mandatory")


class _DsSsPowerStatus_Type(Integer32):
    """Custom type dsSsPowerStatus based on Integer32"""
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
        *(("ssAOffBOn", 3),
          ("ssAOnBOff", 2),
          ("ssBothOff", 1),
          ("ssBothOn", 4))
    )


_DsSsPowerStatus_Type.__name__ = "Integer32"
_DsSsPowerStatus_Object = MibScalar
dsSsPowerStatus = _DsSsPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 1, 4),
    _DsSsPowerStatus_Type()
)
dsSsPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsSsPowerStatus.setStatus("mandatory")
_DsRp_ObjectIdentity = ObjectIdentity
dsRp = _DsRp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2)
)
_DsRpUsr_ObjectIdentity = ObjectIdentity
dsRpUsr = _DsRpUsr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1)
)
_DsRpUsrTmCntTable_Object = MibTable
dsRpUsrTmCntTable = _DsRpUsrTmCntTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dsRpUsrTmCntTable.setStatus("mandatory")
_DsRpUsrTmCntEntry_Object = MibTableRow
dsRpUsrTmCntEntry = _DsRpUsrTmCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 1, 1)
)
dsRpUsrTmCntEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpUsrTmCntIndex"),
)
if mibBuilder.loadTexts:
    dsRpUsrTmCntEntry.setStatus("mandatory")


class _DsRpUsrTmCntIndex_Type(Integer32):
    """Custom type dsRpUsrTmCntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DsRpUsrTmCntIndex_Type.__name__ = "Integer32"
_DsRpUsrTmCntIndex_Object = MibTableColumn
dsRpUsrTmCntIndex = _DsRpUsrTmCntIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 1, 1, 1),
    _DsRpUsrTmCntIndex_Type()
)
dsRpUsrTmCntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTmCntIndex.setStatus("mandatory")


class _DsRpUsrTmCntSecs_Type(Integer32):
    """Custom type dsRpUsrTmCntSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_DsRpUsrTmCntSecs_Type.__name__ = "Integer32"
_DsRpUsrTmCntSecs_Object = MibTableColumn
dsRpUsrTmCntSecs = _DsRpUsrTmCntSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 1, 1, 2),
    _DsRpUsrTmCntSecs_Type()
)
dsRpUsrTmCntSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTmCntSecs.setStatus("mandatory")


class _DsRpUsrTmCnt15Mins_Type(Integer32):
    """Custom type dsRpUsrTmCnt15Mins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_DsRpUsrTmCnt15Mins_Type.__name__ = "Integer32"
_DsRpUsrTmCnt15Mins_Object = MibTableColumn
dsRpUsrTmCnt15Mins = _DsRpUsrTmCnt15Mins_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 1, 1, 3),
    _DsRpUsrTmCnt15Mins_Type()
)
dsRpUsrTmCnt15Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTmCnt15Mins.setStatus("mandatory")


class _DsRpUsrTmCntDays_Type(Integer32):
    """Custom type dsRpUsrTmCntDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DsRpUsrTmCntDays_Type.__name__ = "Integer32"
_DsRpUsrTmCntDays_Object = MibTableColumn
dsRpUsrTmCntDays = _DsRpUsrTmCntDays_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 1, 1, 4),
    _DsRpUsrTmCntDays_Type()
)
dsRpUsrTmCntDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTmCntDays.setStatus("mandatory")
_DsRpUsrCurTable_Object = MibTable
dsRpUsrCurTable = _DsRpUsrCurTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    dsRpUsrCurTable.setStatus("mandatory")
_DsRpUsrCurEntry_Object = MibTableRow
dsRpUsrCurEntry = _DsRpUsrCurEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1)
)
dsRpUsrCurEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpUsrCurIndex"),
)
if mibBuilder.loadTexts:
    dsRpUsrCurEntry.setStatus("mandatory")


class _DsRpUsrCurIndex_Type(Integer32):
    """Custom type dsRpUsrCurIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DsRpUsrCurIndex_Type.__name__ = "Integer32"
_DsRpUsrCurIndex_Object = MibTableColumn
dsRpUsrCurIndex = _DsRpUsrCurIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 1),
    _DsRpUsrCurIndex_Type()
)
dsRpUsrCurIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurIndex.setStatus("mandatory")
_DsRpUsrCurEE_Type = Gauge32
_DsRpUsrCurEE_Object = MibTableColumn
dsRpUsrCurEE = _DsRpUsrCurEE_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 2),
    _DsRpUsrCurEE_Type()
)
dsRpUsrCurEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurEE.setStatus("mandatory")
_DsRpUsrCurES_Type = Gauge32
_DsRpUsrCurES_Object = MibTableColumn
dsRpUsrCurES = _DsRpUsrCurES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 3),
    _DsRpUsrCurES_Type()
)
dsRpUsrCurES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurES.setStatus("mandatory")
_DsRpUsrCurBES_Type = Gauge32
_DsRpUsrCurBES_Object = MibTableColumn
dsRpUsrCurBES = _DsRpUsrCurBES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 4),
    _DsRpUsrCurBES_Type()
)
dsRpUsrCurBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurBES.setStatus("mandatory")
_DsRpUsrCurSES_Type = Gauge32
_DsRpUsrCurSES_Object = MibTableColumn
dsRpUsrCurSES = _DsRpUsrCurSES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 5),
    _DsRpUsrCurSES_Type()
)
dsRpUsrCurSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurSES.setStatus("mandatory")
_DsRpUsrCurUAS_Type = Gauge32
_DsRpUsrCurUAS_Object = MibTableColumn
dsRpUsrCurUAS = _DsRpUsrCurUAS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 6),
    _DsRpUsrCurUAS_Type()
)
dsRpUsrCurUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurUAS.setStatus("mandatory")
_DsRpUsrCurCSS_Type = Gauge32
_DsRpUsrCurCSS_Object = MibTableColumn
dsRpUsrCurCSS = _DsRpUsrCurCSS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 7),
    _DsRpUsrCurCSS_Type()
)
dsRpUsrCurCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurCSS.setStatus("mandatory")
_DsRpUsrCurDM_Type = Gauge32
_DsRpUsrCurDM_Object = MibTableColumn
dsRpUsrCurDM = _DsRpUsrCurDM_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 8),
    _DsRpUsrCurDM_Type()
)
dsRpUsrCurDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurDM.setStatus("mandatory")


class _DsRpUsrCurStatus_Type(DisplayString):
    """Custom type dsRpUsrCurStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DsRpUsrCurStatus_Type.__name__ = "DisplayString"
_DsRpUsrCurStatus_Object = MibTableColumn
dsRpUsrCurStatus = _DsRpUsrCurStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 2, 1, 9),
    _DsRpUsrCurStatus_Type()
)
dsRpUsrCurStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrCurStatus.setStatus("mandatory")
_DsRpUsrIntvlTable_Object = MibTable
dsRpUsrIntvlTable = _DsRpUsrIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    dsRpUsrIntvlTable.setStatus("mandatory")
_DsRpUsrIntvlEntry_Object = MibTableRow
dsRpUsrIntvlEntry = _DsRpUsrIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1)
)
dsRpUsrIntvlEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpUsrIntvlIndex"),
    (0, "DATASMART-MIB", "dsRpUsrIntvlNum"),
)
if mibBuilder.loadTexts:
    dsRpUsrIntvlEntry.setStatus("mandatory")
_DsRpUsrIntvlIndex_Type = Integer32
_DsRpUsrIntvlIndex_Object = MibTableColumn
dsRpUsrIntvlIndex = _DsRpUsrIntvlIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 1),
    _DsRpUsrIntvlIndex_Type()
)
dsRpUsrIntvlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlIndex.setStatus("mandatory")


class _DsRpUsrIntvlNum_Type(Integer32):
    """Custom type dsRpUsrIntvlNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DsRpUsrIntvlNum_Type.__name__ = "Integer32"
_DsRpUsrIntvlNum_Object = MibTableColumn
dsRpUsrIntvlNum = _DsRpUsrIntvlNum_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 2),
    _DsRpUsrIntvlNum_Type()
)
dsRpUsrIntvlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlNum.setStatus("mandatory")
_DsRpUsrIntvlEE_Type = Gauge32
_DsRpUsrIntvlEE_Object = MibTableColumn
dsRpUsrIntvlEE = _DsRpUsrIntvlEE_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 3),
    _DsRpUsrIntvlEE_Type()
)
dsRpUsrIntvlEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlEE.setStatus("mandatory")
_DsRpUsrIntvlES_Type = Gauge32
_DsRpUsrIntvlES_Object = MibTableColumn
dsRpUsrIntvlES = _DsRpUsrIntvlES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 4),
    _DsRpUsrIntvlES_Type()
)
dsRpUsrIntvlES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlES.setStatus("mandatory")
_DsRpUsrIntvlBES_Type = Gauge32
_DsRpUsrIntvlBES_Object = MibTableColumn
dsRpUsrIntvlBES = _DsRpUsrIntvlBES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 5),
    _DsRpUsrIntvlBES_Type()
)
dsRpUsrIntvlBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlBES.setStatus("mandatory")
_DsRpUsrIntvlSES_Type = Gauge32
_DsRpUsrIntvlSES_Object = MibTableColumn
dsRpUsrIntvlSES = _DsRpUsrIntvlSES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 6),
    _DsRpUsrIntvlSES_Type()
)
dsRpUsrIntvlSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlSES.setStatus("mandatory")
_DsRpUsrIntvlUAS_Type = Gauge32
_DsRpUsrIntvlUAS_Object = MibTableColumn
dsRpUsrIntvlUAS = _DsRpUsrIntvlUAS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 7),
    _DsRpUsrIntvlUAS_Type()
)
dsRpUsrIntvlUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlUAS.setStatus("mandatory")
_DsRpUsrIntvlCSS_Type = Gauge32
_DsRpUsrIntvlCSS_Object = MibTableColumn
dsRpUsrIntvlCSS = _DsRpUsrIntvlCSS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 8),
    _DsRpUsrIntvlCSS_Type()
)
dsRpUsrIntvlCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlCSS.setStatus("mandatory")
_DsRpUsrIntvlDM_Type = Gauge32
_DsRpUsrIntvlDM_Object = MibTableColumn
dsRpUsrIntvlDM = _DsRpUsrIntvlDM_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 9),
    _DsRpUsrIntvlDM_Type()
)
dsRpUsrIntvlDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlDM.setStatus("mandatory")


class _DsRpUsrIntvlStatus_Type(DisplayString):
    """Custom type dsRpUsrIntvlStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DsRpUsrIntvlStatus_Type.__name__ = "DisplayString"
_DsRpUsrIntvlStatus_Object = MibTableColumn
dsRpUsrIntvlStatus = _DsRpUsrIntvlStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 3, 1, 10),
    _DsRpUsrIntvlStatus_Type()
)
dsRpUsrIntvlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrIntvlStatus.setStatus("mandatory")
_DsRpUsrTotalTable_Object = MibTable
dsRpUsrTotalTable = _DsRpUsrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    dsRpUsrTotalTable.setStatus("mandatory")
_DsRpUsrTotalEntry_Object = MibTableRow
dsRpUsrTotalEntry = _DsRpUsrTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1)
)
dsRpUsrTotalEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpUsrTotalIndex"),
)
if mibBuilder.loadTexts:
    dsRpUsrTotalEntry.setStatus("mandatory")
_DsRpUsrTotalIndex_Type = Integer32
_DsRpUsrTotalIndex_Object = MibTableColumn
dsRpUsrTotalIndex = _DsRpUsrTotalIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 1),
    _DsRpUsrTotalIndex_Type()
)
dsRpUsrTotalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalIndex.setStatus("mandatory")
_DsRpUsrTotalEE_Type = Gauge32
_DsRpUsrTotalEE_Object = MibTableColumn
dsRpUsrTotalEE = _DsRpUsrTotalEE_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 2),
    _DsRpUsrTotalEE_Type()
)
dsRpUsrTotalEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalEE.setStatus("mandatory")
_DsRpUsrTotalES_Type = Gauge32
_DsRpUsrTotalES_Object = MibTableColumn
dsRpUsrTotalES = _DsRpUsrTotalES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 3),
    _DsRpUsrTotalES_Type()
)
dsRpUsrTotalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalES.setStatus("mandatory")
_DsRpUsrTotalBES_Type = Gauge32
_DsRpUsrTotalBES_Object = MibTableColumn
dsRpUsrTotalBES = _DsRpUsrTotalBES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 4),
    _DsRpUsrTotalBES_Type()
)
dsRpUsrTotalBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalBES.setStatus("mandatory")
_DsRpUsrTotalSES_Type = Gauge32
_DsRpUsrTotalSES_Object = MibTableColumn
dsRpUsrTotalSES = _DsRpUsrTotalSES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 5),
    _DsRpUsrTotalSES_Type()
)
dsRpUsrTotalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalSES.setStatus("mandatory")
_DsRpUsrTotalUAS_Type = Gauge32
_DsRpUsrTotalUAS_Object = MibTableColumn
dsRpUsrTotalUAS = _DsRpUsrTotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 6),
    _DsRpUsrTotalUAS_Type()
)
dsRpUsrTotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalUAS.setStatus("mandatory")
_DsRpUsrTotalCSS_Type = Gauge32
_DsRpUsrTotalCSS_Object = MibTableColumn
dsRpUsrTotalCSS = _DsRpUsrTotalCSS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 7),
    _DsRpUsrTotalCSS_Type()
)
dsRpUsrTotalCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalCSS.setStatus("mandatory")
_DsRpUsrTotalDM_Type = Gauge32
_DsRpUsrTotalDM_Object = MibTableColumn
dsRpUsrTotalDM = _DsRpUsrTotalDM_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 8),
    _DsRpUsrTotalDM_Type()
)
dsRpUsrTotalDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalDM.setStatus("mandatory")


class _DsRpUsrTotalStatus_Type(DisplayString):
    """Custom type dsRpUsrTotalStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DsRpUsrTotalStatus_Type.__name__ = "DisplayString"
_DsRpUsrTotalStatus_Object = MibTableColumn
dsRpUsrTotalStatus = _DsRpUsrTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 4, 1, 9),
    _DsRpUsrTotalStatus_Type()
)
dsRpUsrTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrTotalStatus.setStatus("mandatory")
_DsRpUsrDayTable_Object = MibTable
dsRpUsrDayTable = _DsRpUsrDayTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    dsRpUsrDayTable.setStatus("mandatory")
_DsRpUsrDayEntry_Object = MibTableRow
dsRpUsrDayEntry = _DsRpUsrDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1)
)
dsRpUsrDayEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpUsrDayIndex"),
    (0, "DATASMART-MIB", "dsRpUsrDayNum"),
)
if mibBuilder.loadTexts:
    dsRpUsrDayEntry.setStatus("mandatory")
_DsRpUsrDayIndex_Type = Integer32
_DsRpUsrDayIndex_Object = MibTableColumn
dsRpUsrDayIndex = _DsRpUsrDayIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 1),
    _DsRpUsrDayIndex_Type()
)
dsRpUsrDayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayIndex.setStatus("mandatory")


class _DsRpUsrDayNum_Type(Integer32):
    """Custom type dsRpUsrDayNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_DsRpUsrDayNum_Type.__name__ = "Integer32"
_DsRpUsrDayNum_Object = MibTableColumn
dsRpUsrDayNum = _DsRpUsrDayNum_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 2),
    _DsRpUsrDayNum_Type()
)
dsRpUsrDayNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayNum.setStatus("mandatory")
_DsRpUsrDayEE_Type = Gauge32
_DsRpUsrDayEE_Object = MibTableColumn
dsRpUsrDayEE = _DsRpUsrDayEE_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 3),
    _DsRpUsrDayEE_Type()
)
dsRpUsrDayEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayEE.setStatus("mandatory")
_DsRpUsrDayES_Type = Gauge32
_DsRpUsrDayES_Object = MibTableColumn
dsRpUsrDayES = _DsRpUsrDayES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 4),
    _DsRpUsrDayES_Type()
)
dsRpUsrDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayES.setStatus("mandatory")
_DsRpUsrDayBES_Type = Gauge32
_DsRpUsrDayBES_Object = MibTableColumn
dsRpUsrDayBES = _DsRpUsrDayBES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 5),
    _DsRpUsrDayBES_Type()
)
dsRpUsrDayBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayBES.setStatus("mandatory")
_DsRpUsrDaySES_Type = Gauge32
_DsRpUsrDaySES_Object = MibTableColumn
dsRpUsrDaySES = _DsRpUsrDaySES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 6),
    _DsRpUsrDaySES_Type()
)
dsRpUsrDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDaySES.setStatus("mandatory")
_DsRpUsrDayUAS_Type = Gauge32
_DsRpUsrDayUAS_Object = MibTableColumn
dsRpUsrDayUAS = _DsRpUsrDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 7),
    _DsRpUsrDayUAS_Type()
)
dsRpUsrDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayUAS.setStatus("mandatory")
_DsRpUsrDayCSS_Type = Gauge32
_DsRpUsrDayCSS_Object = MibTableColumn
dsRpUsrDayCSS = _DsRpUsrDayCSS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 8),
    _DsRpUsrDayCSS_Type()
)
dsRpUsrDayCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayCSS.setStatus("mandatory")
_DsRpUsrDayDM_Type = Gauge32
_DsRpUsrDayDM_Object = MibTableColumn
dsRpUsrDayDM = _DsRpUsrDayDM_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 9),
    _DsRpUsrDayDM_Type()
)
dsRpUsrDayDM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayDM.setStatus("mandatory")


class _DsRpUsrDayStatus_Type(DisplayString):
    """Custom type dsRpUsrDayStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DsRpUsrDayStatus_Type.__name__ = "DisplayString"
_DsRpUsrDayStatus_Object = MibTableColumn
dsRpUsrDayStatus = _DsRpUsrDayStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 1, 5, 1, 10),
    _DsRpUsrDayStatus_Type()
)
dsRpUsrDayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpUsrDayStatus.setStatus("mandatory")
_DsRpCar_ObjectIdentity = ObjectIdentity
dsRpCar = _DsRpCar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2)
)


class _DsRpCarCntSecs_Type(Integer32):
    """Custom type dsRpCarCntSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_DsRpCarCntSecs_Type.__name__ = "Integer32"
_DsRpCarCntSecs_Object = MibScalar
dsRpCarCntSecs = _DsRpCarCntSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 1),
    _DsRpCarCntSecs_Type()
)
dsRpCarCntSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCntSecs.setStatus("mandatory")


class _DsRpCarCnt15Mins_Type(Integer32):
    """Custom type dsRpCarCnt15Mins based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_DsRpCarCnt15Mins_Type.__name__ = "Integer32"
_DsRpCarCnt15Mins_Object = MibScalar
dsRpCarCnt15Mins = _DsRpCarCnt15Mins_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 2),
    _DsRpCarCnt15Mins_Type()
)
dsRpCarCnt15Mins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCnt15Mins.setStatus("mandatory")
_DsRpCarCur_ObjectIdentity = ObjectIdentity
dsRpCarCur = _DsRpCarCur_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3)
)
_DsRpCarCurEE_Type = Gauge32
_DsRpCarCurEE_Object = MibScalar
dsRpCarCurEE = _DsRpCarCurEE_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3, 1),
    _DsRpCarCurEE_Type()
)
dsRpCarCurEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCurEE.setStatus("mandatory")
_DsRpCarCurES_Type = Gauge32
_DsRpCarCurES_Object = MibScalar
dsRpCarCurES = _DsRpCarCurES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3, 2),
    _DsRpCarCurES_Type()
)
dsRpCarCurES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCurES.setStatus("mandatory")
_DsRpCarCurBES_Type = Gauge32
_DsRpCarCurBES_Object = MibScalar
dsRpCarCurBES = _DsRpCarCurBES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3, 3),
    _DsRpCarCurBES_Type()
)
dsRpCarCurBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCurBES.setStatus("mandatory")
_DsRpCarCurSES_Type = Gauge32
_DsRpCarCurSES_Object = MibScalar
dsRpCarCurSES = _DsRpCarCurSES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3, 4),
    _DsRpCarCurSES_Type()
)
dsRpCarCurSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCurSES.setStatus("mandatory")
_DsRpCarCurUAS_Type = Gauge32
_DsRpCarCurUAS_Object = MibScalar
dsRpCarCurUAS = _DsRpCarCurUAS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3, 5),
    _DsRpCarCurUAS_Type()
)
dsRpCarCurUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCurUAS.setStatus("mandatory")
_DsRpCarCurCSS_Type = Gauge32
_DsRpCarCurCSS_Object = MibScalar
dsRpCarCurCSS = _DsRpCarCurCSS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3, 6),
    _DsRpCarCurCSS_Type()
)
dsRpCarCurCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCurCSS.setStatus("mandatory")
_DsRpCarCurLOFC_Type = Gauge32
_DsRpCarCurLOFC_Object = MibScalar
dsRpCarCurLOFC = _DsRpCarCurLOFC_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 3, 7),
    _DsRpCarCurLOFC_Type()
)
dsRpCarCurLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarCurLOFC.setStatus("mandatory")
_DsRpCarIntvlTable_Object = MibTable
dsRpCarIntvlTable = _DsRpCarIntvlTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4)
)
if mibBuilder.loadTexts:
    dsRpCarIntvlTable.setStatus("mandatory")
_DsRpCarIntvlEntry_Object = MibTableRow
dsRpCarIntvlEntry = _DsRpCarIntvlEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1)
)
dsRpCarIntvlEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpCarIntvlNum"),
)
if mibBuilder.loadTexts:
    dsRpCarIntvlEntry.setStatus("mandatory")


class _DsRpCarIntvlNum_Type(Integer32):
    """Custom type dsRpCarIntvlNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_DsRpCarIntvlNum_Type.__name__ = "Integer32"
_DsRpCarIntvlNum_Object = MibTableColumn
dsRpCarIntvlNum = _DsRpCarIntvlNum_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 1),
    _DsRpCarIntvlNum_Type()
)
dsRpCarIntvlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlNum.setStatus("mandatory")
_DsRpCarIntvlEE_Type = Gauge32
_DsRpCarIntvlEE_Object = MibTableColumn
dsRpCarIntvlEE = _DsRpCarIntvlEE_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 2),
    _DsRpCarIntvlEE_Type()
)
dsRpCarIntvlEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlEE.setStatus("mandatory")
_DsRpCarIntvlES_Type = Gauge32
_DsRpCarIntvlES_Object = MibTableColumn
dsRpCarIntvlES = _DsRpCarIntvlES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 3),
    _DsRpCarIntvlES_Type()
)
dsRpCarIntvlES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlES.setStatus("mandatory")
_DsRpCarIntvlBES_Type = Gauge32
_DsRpCarIntvlBES_Object = MibTableColumn
dsRpCarIntvlBES = _DsRpCarIntvlBES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 4),
    _DsRpCarIntvlBES_Type()
)
dsRpCarIntvlBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlBES.setStatus("mandatory")
_DsRpCarIntvlSES_Type = Gauge32
_DsRpCarIntvlSES_Object = MibTableColumn
dsRpCarIntvlSES = _DsRpCarIntvlSES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 5),
    _DsRpCarIntvlSES_Type()
)
dsRpCarIntvlSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlSES.setStatus("mandatory")
_DsRpCarIntvlUAS_Type = Gauge32
_DsRpCarIntvlUAS_Object = MibTableColumn
dsRpCarIntvlUAS = _DsRpCarIntvlUAS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 6),
    _DsRpCarIntvlUAS_Type()
)
dsRpCarIntvlUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlUAS.setStatus("mandatory")
_DsRpCarIntvlCSS_Type = Gauge32
_DsRpCarIntvlCSS_Object = MibTableColumn
dsRpCarIntvlCSS = _DsRpCarIntvlCSS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 7),
    _DsRpCarIntvlCSS_Type()
)
dsRpCarIntvlCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlCSS.setStatus("mandatory")
_DsRpCarIntvlLOFC_Type = Gauge32
_DsRpCarIntvlLOFC_Object = MibTableColumn
dsRpCarIntvlLOFC = _DsRpCarIntvlLOFC_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 4, 1, 8),
    _DsRpCarIntvlLOFC_Type()
)
dsRpCarIntvlLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarIntvlLOFC.setStatus("mandatory")
_DsRpCarTotal_ObjectIdentity = ObjectIdentity
dsRpCarTotal = _DsRpCarTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5)
)
_DsRpCarTotalEE_Type = Gauge32
_DsRpCarTotalEE_Object = MibScalar
dsRpCarTotalEE = _DsRpCarTotalEE_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5, 1),
    _DsRpCarTotalEE_Type()
)
dsRpCarTotalEE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarTotalEE.setStatus("mandatory")
_DsRpCarTotalES_Type = Gauge32
_DsRpCarTotalES_Object = MibScalar
dsRpCarTotalES = _DsRpCarTotalES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5, 2),
    _DsRpCarTotalES_Type()
)
dsRpCarTotalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarTotalES.setStatus("mandatory")
_DsRpCarTotalBES_Type = Gauge32
_DsRpCarTotalBES_Object = MibScalar
dsRpCarTotalBES = _DsRpCarTotalBES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5, 3),
    _DsRpCarTotalBES_Type()
)
dsRpCarTotalBES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarTotalBES.setStatus("mandatory")
_DsRpCarTotalSES_Type = Gauge32
_DsRpCarTotalSES_Object = MibScalar
dsRpCarTotalSES = _DsRpCarTotalSES_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5, 4),
    _DsRpCarTotalSES_Type()
)
dsRpCarTotalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarTotalSES.setStatus("mandatory")
_DsRpCarTotalUAS_Type = Gauge32
_DsRpCarTotalUAS_Object = MibScalar
dsRpCarTotalUAS = _DsRpCarTotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5, 5),
    _DsRpCarTotalUAS_Type()
)
dsRpCarTotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarTotalUAS.setStatus("mandatory")
_DsRpCarTotalCSS_Type = Gauge32
_DsRpCarTotalCSS_Object = MibScalar
dsRpCarTotalCSS = _DsRpCarTotalCSS_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5, 6),
    _DsRpCarTotalCSS_Type()
)
dsRpCarTotalCSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarTotalCSS.setStatus("mandatory")
_DsRpCarTotalLOFC_Type = Gauge32
_DsRpCarTotalLOFC_Object = MibScalar
dsRpCarTotalLOFC = _DsRpCarTotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 2, 5, 7),
    _DsRpCarTotalLOFC_Type()
)
dsRpCarTotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpCarTotalLOFC.setStatus("mandatory")
_DsRpStat_ObjectIdentity = ObjectIdentity
dsRpStat = _DsRpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3)
)
_DsRpStTable_Object = MibTable
dsRpStTable = _DsRpStTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    dsRpStTable.setStatus("mandatory")
_DsRpStEntry_Object = MibTableRow
dsRpStEntry = _DsRpStEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1)
)
dsRpStEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpStIndex"),
)
if mibBuilder.loadTexts:
    dsRpStEntry.setStatus("mandatory")


class _DsRpStIndex_Type(Integer32):
    """Custom type dsRpStIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DsRpStIndex_Type.__name__ = "Integer32"
_DsRpStIndex_Object = MibTableColumn
dsRpStIndex = _DsRpStIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 1),
    _DsRpStIndex_Type()
)
dsRpStIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStIndex.setStatus("mandatory")
_DsRpStEsfErrors_Type = Counter32
_DsRpStEsfErrors_Object = MibTableColumn
dsRpStEsfErrors = _DsRpStEsfErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 2),
    _DsRpStEsfErrors_Type()
)
dsRpStEsfErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStEsfErrors.setStatus("mandatory")
_DsRpStCrcErrors_Type = Counter32
_DsRpStCrcErrors_Object = MibTableColumn
dsRpStCrcErrors = _DsRpStCrcErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 3),
    _DsRpStCrcErrors_Type()
)
dsRpStCrcErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStCrcErrors.setStatus("mandatory")
_DsRpStOofErrors_Type = Counter32
_DsRpStOofErrors_Object = MibTableColumn
dsRpStOofErrors = _DsRpStOofErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 4),
    _DsRpStOofErrors_Type()
)
dsRpStOofErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStOofErrors.setStatus("mandatory")
_DsRpStFrameBitErrors_Type = Counter32
_DsRpStFrameBitErrors_Object = MibTableColumn
dsRpStFrameBitErrors = _DsRpStFrameBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 5),
    _DsRpStFrameBitErrors_Type()
)
dsRpStFrameBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStFrameBitErrors.setStatus("mandatory")
_DsRpStBPVs_Type = Counter32
_DsRpStBPVs_Object = MibTableColumn
dsRpStBPVs = _DsRpStBPVs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 6),
    _DsRpStBPVs_Type()
)
dsRpStBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStBPVs.setStatus("mandatory")
_DsRpStControlledSlips_Type = Counter32
_DsRpStControlledSlips_Object = MibTableColumn
dsRpStControlledSlips = _DsRpStControlledSlips_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 7),
    _DsRpStControlledSlips_Type()
)
dsRpStControlledSlips.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStControlledSlips.setStatus("mandatory")
_DsRpStYellowEvents_Type = Counter32
_DsRpStYellowEvents_Object = MibTableColumn
dsRpStYellowEvents = _DsRpStYellowEvents_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 8),
    _DsRpStYellowEvents_Type()
)
dsRpStYellowEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStYellowEvents.setStatus("mandatory")
_DsRpStAISEvents_Type = Counter32
_DsRpStAISEvents_Object = MibTableColumn
dsRpStAISEvents = _DsRpStAISEvents_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 9),
    _DsRpStAISEvents_Type()
)
dsRpStAISEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStAISEvents.setStatus("mandatory")
_DsRpStLOFEvents_Type = Counter32
_DsRpStLOFEvents_Object = MibTableColumn
dsRpStLOFEvents = _DsRpStLOFEvents_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 10),
    _DsRpStLOFEvents_Type()
)
dsRpStLOFEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStLOFEvents.setStatus("mandatory")
_DsRpStLOSEvents_Type = Counter32
_DsRpStLOSEvents_Object = MibTableColumn
dsRpStLOSEvents = _DsRpStLOSEvents_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 11),
    _DsRpStLOSEvents_Type()
)
dsRpStLOSEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStLOSEvents.setStatus("mandatory")
_DsRpStFarEndBlkErrors_Type = Counter32
_DsRpStFarEndBlkErrors_Object = MibTableColumn
dsRpStFarEndBlkErrors = _DsRpStFarEndBlkErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 12),
    _DsRpStFarEndBlkErrors_Type()
)
dsRpStFarEndBlkErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStFarEndBlkErrors.setStatus("mandatory")
_DsRpStRemFrameAlmEvts_Type = Counter32
_DsRpStRemFrameAlmEvts_Object = MibTableColumn
dsRpStRemFrameAlmEvts = _DsRpStRemFrameAlmEvts_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 13),
    _DsRpStRemFrameAlmEvts_Type()
)
dsRpStRemFrameAlmEvts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStRemFrameAlmEvts.setStatus("mandatory")
_DsRpStRemMFrameAlmEvts_Type = Counter32
_DsRpStRemMFrameAlmEvts_Object = MibTableColumn
dsRpStRemMFrameAlmEvts = _DsRpStRemMFrameAlmEvts_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 14),
    _DsRpStRemMFrameAlmEvts_Type()
)
dsRpStRemMFrameAlmEvts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStRemMFrameAlmEvts.setStatus("mandatory")
_DsRpStLOTS16MFrameEvts_Type = Counter32
_DsRpStLOTS16MFrameEvts_Object = MibTableColumn
dsRpStLOTS16MFrameEvts = _DsRpStLOTS16MFrameEvts_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 15),
    _DsRpStLOTS16MFrameEvts_Type()
)
dsRpStLOTS16MFrameEvts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpStLOTS16MFrameEvts.setStatus("mandatory")


class _DsRpStZeroCounters_Type(Integer32):
    """Custom type dsRpStZeroCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpStZeroCountersIdle", 1),
          ("rpStZeroCountersStart", 2))
    )


_DsRpStZeroCounters_Type.__name__ = "Integer32"
_DsRpStZeroCounters_Object = MibTableColumn
dsRpStZeroCounters = _DsRpStZeroCounters_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 3, 1, 1, 16),
    _DsRpStZeroCounters_Type()
)
dsRpStZeroCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRpStZeroCounters.setStatus("mandatory")
_DsRpPl_ObjectIdentity = ObjectIdentity
dsRpPl = _DsRpPl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 4)
)


class _DsPlBreak_Type(Integer32):
    """Custom type dsPlBreak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rpPlLineFeed", 1),
          ("rpPlMorePrompt", 2))
    )


_DsPlBreak_Type.__name__ = "Integer32"
_DsPlBreak_Object = MibScalar
dsPlBreak = _DsPlBreak_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 4, 1),
    _DsPlBreak_Type()
)
dsPlBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsPlBreak.setStatus("mandatory")


class _DsPlLen_Type(Integer32):
    """Custom type dsPlLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 70),
    )


_DsPlLen_Type.__name__ = "Integer32"
_DsPlLen_Object = MibScalar
dsPlLen = _DsPlLen_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 4, 2),
    _DsPlLen_Type()
)
dsPlLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsPlLen.setStatus("mandatory")
_DsRpAhrTable_Object = MibTable
dsRpAhrTable = _DsRpAhrTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 5)
)
if mibBuilder.loadTexts:
    dsRpAhrTable.setStatus("mandatory")
_DsRpAhrEntry_Object = MibTableRow
dsRpAhrEntry = _DsRpAhrEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 5, 1)
)
dsRpAhrEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpAhrIndex"),
)
if mibBuilder.loadTexts:
    dsRpAhrEntry.setStatus("mandatory")


class _DsRpAhrIndex_Type(Integer32):
    """Custom type dsRpAhrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_DsRpAhrIndex_Type.__name__ = "Integer32"
_DsRpAhrIndex_Object = MibTableColumn
dsRpAhrIndex = _DsRpAhrIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 5, 1, 1),
    _DsRpAhrIndex_Type()
)
dsRpAhrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpAhrIndex.setStatus("mandatory")


class _DsRpAhrStr_Type(DisplayString):
    """Custom type dsRpAhrStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DsRpAhrStr_Type.__name__ = "DisplayString"
_DsRpAhrStr_Object = MibTableColumn
dsRpAhrStr = _DsRpAhrStr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 5, 1, 2),
    _DsRpAhrStr_Type()
)
dsRpAhrStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpAhrStr.setStatus("mandatory")
_DsRpShrTable_Object = MibTable
dsRpShrTable = _DsRpShrTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 6)
)
if mibBuilder.loadTexts:
    dsRpShrTable.setStatus("mandatory")
_DsRpShrEntry_Object = MibTableRow
dsRpShrEntry = _DsRpShrEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 6, 1)
)
dsRpShrEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpShrIndex"),
)
if mibBuilder.loadTexts:
    dsRpShrEntry.setStatus("mandatory")
_DsRpShrIndex_Type = Integer32
_DsRpShrIndex_Object = MibTableColumn
dsRpShrIndex = _DsRpShrIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 6, 1, 1),
    _DsRpShrIndex_Type()
)
dsRpShrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpShrIndex.setStatus("mandatory")


class _DsRpShrDateTime_Type(DisplayString):
    """Custom type dsRpShrDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DsRpShrDateTime_Type.__name__ = "DisplayString"
_DsRpShrDateTime_Object = MibTableColumn
dsRpShrDateTime = _DsRpShrDateTime_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 6, 1, 2),
    _DsRpShrDateTime_Type()
)
dsRpShrDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpShrDateTime.setStatus("mandatory")


class _DsRpShrEventType_Type(Integer32):
    """Custom type dsRpShrEventType based on Integer32"""
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
        *(("rpShrReadCommString", 3),
          ("rpShrSrcIpAddressScreen", 2),
          ("rpShrTelnetPassword", 1),
          ("rpShrWriteCommString", 4))
    )


_DsRpShrEventType_Type.__name__ = "Integer32"
_DsRpShrEventType_Object = MibTableColumn
dsRpShrEventType = _DsRpShrEventType_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 6, 1, 3),
    _DsRpShrEventType_Type()
)
dsRpShrEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpShrEventType.setStatus("mandatory")


class _DsRpShrComments_Type(DisplayString):
    """Custom type dsRpShrComments based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DsRpShrComments_Type.__name__ = "DisplayString"
_DsRpShrComments_Object = MibTableColumn
dsRpShrComments = _DsRpShrComments_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 6, 1, 4),
    _DsRpShrComments_Type()
)
dsRpShrComments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpShrComments.setStatus("mandatory")


class _DsRpBes_Type(Integer32):
    """Custom type dsRpBes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 63999),
    )


_DsRpBes_Type.__name__ = "Integer32"
_DsRpBes_Object = MibScalar
dsRpBes = _DsRpBes_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 7),
    _DsRpBes_Type()
)
dsRpBes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRpBes.setStatus("mandatory")


class _DsRpSes_Type(Integer32):
    """Custom type dsRpSes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 64000),
    )


_DsRpSes_Type.__name__ = "Integer32"
_DsRpSes_Object = MibScalar
dsRpSes = _DsRpSes_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 8),
    _DsRpSes_Type()
)
dsRpSes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRpSes.setStatus("mandatory")


class _DsRpDm_Type(Integer32):
    """Custom type dsRpDm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64000),
    )


_DsRpDm_Type.__name__ = "Integer32"
_DsRpDm_Object = MibScalar
dsRpDm = _DsRpDm_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 9),
    _DsRpDm_Type()
)
dsRpDm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRpDm.setStatus("mandatory")
_DsRpFr_ObjectIdentity = ObjectIdentity
dsRpFr = _DsRpFr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10)
)
_DsRpFrTmCntTable_Object = MibTable
dsRpFrTmCntTable = _DsRpFrTmCntTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 1)
)
if mibBuilder.loadTexts:
    dsRpFrTmCntTable.setStatus("mandatory")
_DsRpFrTmCntEntry_Object = MibTableRow
dsRpFrTmCntEntry = _DsRpFrTmCntEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 1, 1)
)
dsRpFrTmCntEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrTmCntDir"),
)
if mibBuilder.loadTexts:
    dsRpFrTmCntEntry.setStatus("mandatory")


class _DsRpFrTmCntDir_Type(Integer32):
    """Custom type dsRpFrTmCntDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrTmCntDir_Type.__name__ = "Integer32"
_DsRpFrTmCntDir_Object = MibTableColumn
dsRpFrTmCntDir = _DsRpFrTmCntDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 1, 1, 1),
    _DsRpFrTmCntDir_Type()
)
dsRpFrTmCntDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTmCntDir.setStatus("mandatory")


class _DsRpFrTmCntSecs_Type(Integer32):
    """Custom type dsRpFrTmCntSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7200),
    )


_DsRpFrTmCntSecs_Type.__name__ = "Integer32"
_DsRpFrTmCntSecs_Object = MibTableColumn
dsRpFrTmCntSecs = _DsRpFrTmCntSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 1, 1, 2),
    _DsRpFrTmCntSecs_Type()
)
dsRpFrTmCntSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTmCntSecs.setStatus("mandatory")


class _DsRpFrTmCnt2Hrs_Type(Integer32):
    """Custom type dsRpFrTmCnt2Hrs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_DsRpFrTmCnt2Hrs_Type.__name__ = "Integer32"
_DsRpFrTmCnt2Hrs_Object = MibTableColumn
dsRpFrTmCnt2Hrs = _DsRpFrTmCnt2Hrs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 1, 1, 3),
    _DsRpFrTmCnt2Hrs_Type()
)
dsRpFrTmCnt2Hrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTmCnt2Hrs.setStatus("mandatory")


class _DsRpFrTmCntDays_Type(Integer32):
    """Custom type dsRpFrTmCntDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DsRpFrTmCntDays_Type.__name__ = "Integer32"
_DsRpFrTmCntDays_Object = MibTableColumn
dsRpFrTmCntDays = _DsRpFrTmCntDays_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 1, 1, 4),
    _DsRpFrTmCntDays_Type()
)
dsRpFrTmCntDays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTmCntDays.setStatus("mandatory")
_DsRpFrPre15MTable_Object = MibTable
dsRpFrPre15MTable = _DsRpFrPre15MTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2)
)
if mibBuilder.loadTexts:
    dsRpFrPre15MTable.setStatus("mandatory")
_DsRpFrPre15MEntry_Object = MibTableRow
dsRpFrPre15MEntry = _DsRpFrPre15MEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1)
)
dsRpFrPre15MEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrPre15MDir"),
    (0, "DATASMART-MIB", "dsRpFrPre15MVcIndex"),
)
if mibBuilder.loadTexts:
    dsRpFrPre15MEntry.setStatus("mandatory")


class _DsRpFrPre15MDir_Type(Integer32):
    """Custom type dsRpFrPre15MDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrPre15MDir_Type.__name__ = "Integer32"
_DsRpFrPre15MDir_Object = MibTableColumn
dsRpFrPre15MDir = _DsRpFrPre15MDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 1),
    _DsRpFrPre15MDir_Type()
)
dsRpFrPre15MDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MDir.setStatus("mandatory")


class _DsRpFrPre15MVcIndex_Type(Integer32):
    """Custom type dsRpFrPre15MVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_DsRpFrPre15MVcIndex_Type.__name__ = "Integer32"
_DsRpFrPre15MVcIndex_Object = MibTableColumn
dsRpFrPre15MVcIndex = _DsRpFrPre15MVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 2),
    _DsRpFrPre15MVcIndex_Type()
)
dsRpFrPre15MVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MVcIndex.setStatus("mandatory")


class _DsRpFrPre15MVc_Type(Integer32):
    """Custom type dsRpFrPre15MVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388607),
    )


_DsRpFrPre15MVc_Type.__name__ = "Integer32"
_DsRpFrPre15MVc_Object = MibTableColumn
dsRpFrPre15MVc = _DsRpFrPre15MVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 3),
    _DsRpFrPre15MVc_Type()
)
dsRpFrPre15MVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MVc.setStatus("mandatory")
_DsRpFrPre15MFrames_Type = Counter32
_DsRpFrPre15MFrames_Object = MibTableColumn
dsRpFrPre15MFrames = _DsRpFrPre15MFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 4),
    _DsRpFrPre15MFrames_Type()
)
dsRpFrPre15MFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MFrames.setStatus("mandatory")
_DsRpFrPre15MOctets_Type = Counter32
_DsRpFrPre15MOctets_Object = MibTableColumn
dsRpFrPre15MOctets = _DsRpFrPre15MOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 5),
    _DsRpFrPre15MOctets_Type()
)
dsRpFrPre15MOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MOctets.setStatus("mandatory")
_DsRpFrPre15MKbps_Type = Gauge32
_DsRpFrPre15MKbps_Object = MibTableColumn
dsRpFrPre15MKbps = _DsRpFrPre15MKbps_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 6),
    _DsRpFrPre15MKbps_Type()
)
dsRpFrPre15MKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MKbps.setStatus("mandatory")
_DsRpFrPre15MFpMax_Type = Counter32
_DsRpFrPre15MFpMax_Object = MibTableColumn
dsRpFrPre15MFpMax = _DsRpFrPre15MFpMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 7),
    _DsRpFrPre15MFpMax_Type()
)
dsRpFrPre15MFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MFpMax.setStatus("mandatory")
_DsRpFrPre15MFpAvg_Type = Gauge32
_DsRpFrPre15MFpAvg_Object = MibTableColumn
dsRpFrPre15MFpAvg = _DsRpFrPre15MFpAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 8),
    _DsRpFrPre15MFpAvg_Type()
)
dsRpFrPre15MFpAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MFpAvg.setStatus("mandatory")
_DsRpFrPre15MFpLost_Type = Counter32
_DsRpFrPre15MFpLost_Object = MibTableColumn
dsRpFrPre15MFpLost = _DsRpFrPre15MFpLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 9),
    _DsRpFrPre15MFpLost_Type()
)
dsRpFrPre15MFpLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MFpLost.setStatus("mandatory")
_DsRpFrPre15MFpSent_Type = Counter32
_DsRpFrPre15MFpSent_Object = MibTableColumn
dsRpFrPre15MFpSent = _DsRpFrPre15MFpSent_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 10),
    _DsRpFrPre15MFpSent_Type()
)
dsRpFrPre15MFpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MFpSent.setStatus("mandatory")


class _DsRpFrPre15MStatus_Type(DisplayString):
    """Custom type dsRpFrPre15MStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DsRpFrPre15MStatus_Type.__name__ = "DisplayString"
_DsRpFrPre15MStatus_Object = MibTableColumn
dsRpFrPre15MStatus = _DsRpFrPre15MStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 2, 1, 11),
    _DsRpFrPre15MStatus_Type()
)
dsRpFrPre15MStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrPre15MStatus.setStatus("mandatory")
_DsRpFrCur15MTable_Object = MibTable
dsRpFrCur15MTable = _DsRpFrCur15MTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3)
)
if mibBuilder.loadTexts:
    dsRpFrCur15MTable.setStatus("mandatory")
_DsRpFrCur15MEntry_Object = MibTableRow
dsRpFrCur15MEntry = _DsRpFrCur15MEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1)
)
dsRpFrCur15MEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrCur15MDir"),
    (0, "DATASMART-MIB", "dsRpFrCur15MVcIndex"),
)
if mibBuilder.loadTexts:
    dsRpFrCur15MEntry.setStatus("mandatory")


class _DsRpFrCur15MDir_Type(Integer32):
    """Custom type dsRpFrCur15MDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrCur15MDir_Type.__name__ = "Integer32"
_DsRpFrCur15MDir_Object = MibTableColumn
dsRpFrCur15MDir = _DsRpFrCur15MDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 1),
    _DsRpFrCur15MDir_Type()
)
dsRpFrCur15MDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MDir.setStatus("mandatory")


class _DsRpFrCur15MVcIndex_Type(Integer32):
    """Custom type dsRpFrCur15MVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_DsRpFrCur15MVcIndex_Type.__name__ = "Integer32"
_DsRpFrCur15MVcIndex_Object = MibTableColumn
dsRpFrCur15MVcIndex = _DsRpFrCur15MVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 2),
    _DsRpFrCur15MVcIndex_Type()
)
dsRpFrCur15MVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MVcIndex.setStatus("mandatory")


class _DsRpFrCur15MVc_Type(Integer32):
    """Custom type dsRpFrCur15MVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388607),
    )


_DsRpFrCur15MVc_Type.__name__ = "Integer32"
_DsRpFrCur15MVc_Object = MibTableColumn
dsRpFrCur15MVc = _DsRpFrCur15MVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 3),
    _DsRpFrCur15MVc_Type()
)
dsRpFrCur15MVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MVc.setStatus("mandatory")
_DsRpFrCur15MFrames_Type = Counter32
_DsRpFrCur15MFrames_Object = MibTableColumn
dsRpFrCur15MFrames = _DsRpFrCur15MFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 4),
    _DsRpFrCur15MFrames_Type()
)
dsRpFrCur15MFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MFrames.setStatus("mandatory")
_DsRpFrCur15MOctets_Type = Counter32
_DsRpFrCur15MOctets_Object = MibTableColumn
dsRpFrCur15MOctets = _DsRpFrCur15MOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 5),
    _DsRpFrCur15MOctets_Type()
)
dsRpFrCur15MOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MOctets.setStatus("mandatory")
_DsRpFrCur15MKbps_Type = Gauge32
_DsRpFrCur15MKbps_Object = MibTableColumn
dsRpFrCur15MKbps = _DsRpFrCur15MKbps_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 6),
    _DsRpFrCur15MKbps_Type()
)
dsRpFrCur15MKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MKbps.setStatus("mandatory")
_DsRpFrCur15MFpMax_Type = Counter32
_DsRpFrCur15MFpMax_Object = MibTableColumn
dsRpFrCur15MFpMax = _DsRpFrCur15MFpMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 7),
    _DsRpFrCur15MFpMax_Type()
)
dsRpFrCur15MFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MFpMax.setStatus("mandatory")
_DsRpFrCur15MFpAvg_Type = Gauge32
_DsRpFrCur15MFpAvg_Object = MibTableColumn
dsRpFrCur15MFpAvg = _DsRpFrCur15MFpAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 8),
    _DsRpFrCur15MFpAvg_Type()
)
dsRpFrCur15MFpAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MFpAvg.setStatus("mandatory")
_DsRpFrCur15MFpLost_Type = Counter32
_DsRpFrCur15MFpLost_Object = MibTableColumn
dsRpFrCur15MFpLost = _DsRpFrCur15MFpLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 9),
    _DsRpFrCur15MFpLost_Type()
)
dsRpFrCur15MFpLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MFpLost.setStatus("mandatory")
_DsRpFrCur15MFpSent_Type = Counter32
_DsRpFrCur15MFpSent_Object = MibTableColumn
dsRpFrCur15MFpSent = _DsRpFrCur15MFpSent_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 10),
    _DsRpFrCur15MFpSent_Type()
)
dsRpFrCur15MFpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MFpSent.setStatus("mandatory")
_DsRpFrCur15MFpRmtIp_Type = IpAddress
_DsRpFrCur15MFpRmtIp_Object = MibTableColumn
dsRpFrCur15MFpRmtIp = _DsRpFrCur15MFpRmtIp_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 11),
    _DsRpFrCur15MFpRmtIp_Type()
)
dsRpFrCur15MFpRmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MFpRmtIp.setStatus("mandatory")


class _DsRpFrCur15MFpRmtVc_Type(Integer32):
    """Custom type dsRpFrCur15MFpRmtVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_DsRpFrCur15MFpRmtVc_Type.__name__ = "Integer32"
_DsRpFrCur15MFpRmtVc_Object = MibTableColumn
dsRpFrCur15MFpRmtVc = _DsRpFrCur15MFpRmtVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 12),
    _DsRpFrCur15MFpRmtVc_Type()
)
dsRpFrCur15MFpRmtVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MFpRmtVc.setStatus("mandatory")


class _DsRpFrCur15MStatus_Type(DisplayString):
    """Custom type dsRpFrCur15MStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DsRpFrCur15MStatus_Type.__name__ = "DisplayString"
_DsRpFrCur15MStatus_Object = MibTableColumn
dsRpFrCur15MStatus = _DsRpFrCur15MStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 3, 1, 13),
    _DsRpFrCur15MStatus_Type()
)
dsRpFrCur15MStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur15MStatus.setStatus("mandatory")
_DsRpFrCur2HTable_Object = MibTable
dsRpFrCur2HTable = _DsRpFrCur2HTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4)
)
if mibBuilder.loadTexts:
    dsRpFrCur2HTable.setStatus("mandatory")
_DsRpFrCur2HEntry_Object = MibTableRow
dsRpFrCur2HEntry = _DsRpFrCur2HEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1)
)
dsRpFrCur2HEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrCur2HDir"),
    (0, "DATASMART-MIB", "dsRpFrCur2HVcIndex"),
)
if mibBuilder.loadTexts:
    dsRpFrCur2HEntry.setStatus("mandatory")


class _DsRpFrCur2HDir_Type(Integer32):
    """Custom type dsRpFrCur2HDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrCur2HDir_Type.__name__ = "Integer32"
_DsRpFrCur2HDir_Object = MibTableColumn
dsRpFrCur2HDir = _DsRpFrCur2HDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 1),
    _DsRpFrCur2HDir_Type()
)
dsRpFrCur2HDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HDir.setStatus("mandatory")


class _DsRpFrCur2HVcIndex_Type(Integer32):
    """Custom type dsRpFrCur2HVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_DsRpFrCur2HVcIndex_Type.__name__ = "Integer32"
_DsRpFrCur2HVcIndex_Object = MibTableColumn
dsRpFrCur2HVcIndex = _DsRpFrCur2HVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 2),
    _DsRpFrCur2HVcIndex_Type()
)
dsRpFrCur2HVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HVcIndex.setStatus("mandatory")


class _DsRpFrCur2HVc_Type(Integer32):
    """Custom type dsRpFrCur2HVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388607),
    )


_DsRpFrCur2HVc_Type.__name__ = "Integer32"
_DsRpFrCur2HVc_Object = MibTableColumn
dsRpFrCur2HVc = _DsRpFrCur2HVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 3),
    _DsRpFrCur2HVc_Type()
)
dsRpFrCur2HVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HVc.setStatus("mandatory")
_DsRpFrCur2HFrames_Type = Counter32
_DsRpFrCur2HFrames_Object = MibTableColumn
dsRpFrCur2HFrames = _DsRpFrCur2HFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 4),
    _DsRpFrCur2HFrames_Type()
)
dsRpFrCur2HFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HFrames.setStatus("mandatory")
_DsRpFrCur2HOctets_Type = Counter32
_DsRpFrCur2HOctets_Object = MibTableColumn
dsRpFrCur2HOctets = _DsRpFrCur2HOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 5),
    _DsRpFrCur2HOctets_Type()
)
dsRpFrCur2HOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HOctets.setStatus("mandatory")
_DsRpFrCur2HKbps_Type = Gauge32
_DsRpFrCur2HKbps_Object = MibTableColumn
dsRpFrCur2HKbps = _DsRpFrCur2HKbps_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 6),
    _DsRpFrCur2HKbps_Type()
)
dsRpFrCur2HKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HKbps.setStatus("mandatory")
_DsRpFrCur2HFpMax_Type = Counter32
_DsRpFrCur2HFpMax_Object = MibTableColumn
dsRpFrCur2HFpMax = _DsRpFrCur2HFpMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 7),
    _DsRpFrCur2HFpMax_Type()
)
dsRpFrCur2HFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HFpMax.setStatus("mandatory")
_DsRpFrCur2HFpAvg_Type = Gauge32
_DsRpFrCur2HFpAvg_Object = MibTableColumn
dsRpFrCur2HFpAvg = _DsRpFrCur2HFpAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 8),
    _DsRpFrCur2HFpAvg_Type()
)
dsRpFrCur2HFpAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HFpAvg.setStatus("mandatory")
_DsRpFrCur2HFpLost_Type = Counter32
_DsRpFrCur2HFpLost_Object = MibTableColumn
dsRpFrCur2HFpLost = _DsRpFrCur2HFpLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 9),
    _DsRpFrCur2HFpLost_Type()
)
dsRpFrCur2HFpLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HFpLost.setStatus("mandatory")
_DsRpFrCur2HFpSent_Type = Counter32
_DsRpFrCur2HFpSent_Object = MibTableColumn
dsRpFrCur2HFpSent = _DsRpFrCur2HFpSent_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 10),
    _DsRpFrCur2HFpSent_Type()
)
dsRpFrCur2HFpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HFpSent.setStatus("mandatory")


class _DsRpFrCur2HStatus_Type(DisplayString):
    """Custom type dsRpFrCur2HStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DsRpFrCur2HStatus_Type.__name__ = "DisplayString"
_DsRpFrCur2HStatus_Object = MibTableColumn
dsRpFrCur2HStatus = _DsRpFrCur2HStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 4, 1, 11),
    _DsRpFrCur2HStatus_Type()
)
dsRpFrCur2HStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrCur2HStatus.setStatus("mandatory")
_DsRpFrIntvl2HTable_Object = MibTable
dsRpFrIntvl2HTable = _DsRpFrIntvl2HTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5)
)
if mibBuilder.loadTexts:
    dsRpFrIntvl2HTable.setStatus("mandatory")
_DsRpFrIntvl2HEntry_Object = MibTableRow
dsRpFrIntvl2HEntry = _DsRpFrIntvl2HEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1)
)
dsRpFrIntvl2HEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrIntvl2HDir"),
    (0, "DATASMART-MIB", "dsRpFrIntvl2HVcIndex"),
    (0, "DATASMART-MIB", "dsRpFrIntvl2HNum"),
)
if mibBuilder.loadTexts:
    dsRpFrIntvl2HEntry.setStatus("mandatory")


class _DsRpFrIntvl2HDir_Type(Integer32):
    """Custom type dsRpFrIntvl2HDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrIntvl2HDir_Type.__name__ = "Integer32"
_DsRpFrIntvl2HDir_Object = MibTableColumn
dsRpFrIntvl2HDir = _DsRpFrIntvl2HDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 1),
    _DsRpFrIntvl2HDir_Type()
)
dsRpFrIntvl2HDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HDir.setStatus("mandatory")


class _DsRpFrIntvl2HVcIndex_Type(Integer32):
    """Custom type dsRpFrIntvl2HVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_DsRpFrIntvl2HVcIndex_Type.__name__ = "Integer32"
_DsRpFrIntvl2HVcIndex_Object = MibTableColumn
dsRpFrIntvl2HVcIndex = _DsRpFrIntvl2HVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 2),
    _DsRpFrIntvl2HVcIndex_Type()
)
dsRpFrIntvl2HVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HVcIndex.setStatus("mandatory")


class _DsRpFrIntvl2HNum_Type(Integer32):
    """Custom type dsRpFrIntvl2HNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DsRpFrIntvl2HNum_Type.__name__ = "Integer32"
_DsRpFrIntvl2HNum_Object = MibTableColumn
dsRpFrIntvl2HNum = _DsRpFrIntvl2HNum_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 3),
    _DsRpFrIntvl2HNum_Type()
)
dsRpFrIntvl2HNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HNum.setStatus("mandatory")


class _DsRpFrIntvl2HVc_Type(Integer32):
    """Custom type dsRpFrIntvl2HVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388607),
    )


_DsRpFrIntvl2HVc_Type.__name__ = "Integer32"
_DsRpFrIntvl2HVc_Object = MibTableColumn
dsRpFrIntvl2HVc = _DsRpFrIntvl2HVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 4),
    _DsRpFrIntvl2HVc_Type()
)
dsRpFrIntvl2HVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HVc.setStatus("mandatory")
_DsRpFrIntvl2HFrames_Type = Counter32
_DsRpFrIntvl2HFrames_Object = MibTableColumn
dsRpFrIntvl2HFrames = _DsRpFrIntvl2HFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 5),
    _DsRpFrIntvl2HFrames_Type()
)
dsRpFrIntvl2HFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HFrames.setStatus("mandatory")
_DsRpFrIntvl2HOctets_Type = Counter32
_DsRpFrIntvl2HOctets_Object = MibTableColumn
dsRpFrIntvl2HOctets = _DsRpFrIntvl2HOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 6),
    _DsRpFrIntvl2HOctets_Type()
)
dsRpFrIntvl2HOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HOctets.setStatus("mandatory")
_DsRpFrIntvl2HKbps_Type = Gauge32
_DsRpFrIntvl2HKbps_Object = MibTableColumn
dsRpFrIntvl2HKbps = _DsRpFrIntvl2HKbps_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 7),
    _DsRpFrIntvl2HKbps_Type()
)
dsRpFrIntvl2HKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HKbps.setStatus("mandatory")
_DsRpFrIntvl2HFpMax_Type = Counter32
_DsRpFrIntvl2HFpMax_Object = MibTableColumn
dsRpFrIntvl2HFpMax = _DsRpFrIntvl2HFpMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 8),
    _DsRpFrIntvl2HFpMax_Type()
)
dsRpFrIntvl2HFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HFpMax.setStatus("mandatory")
_DsRpFrIntvl2HFpAvg_Type = Gauge32
_DsRpFrIntvl2HFpAvg_Object = MibTableColumn
dsRpFrIntvl2HFpAvg = _DsRpFrIntvl2HFpAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 9),
    _DsRpFrIntvl2HFpAvg_Type()
)
dsRpFrIntvl2HFpAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HFpAvg.setStatus("mandatory")
_DsRpFrIntvl2HFpLost_Type = Counter32
_DsRpFrIntvl2HFpLost_Object = MibTableColumn
dsRpFrIntvl2HFpLost = _DsRpFrIntvl2HFpLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 10),
    _DsRpFrIntvl2HFpLost_Type()
)
dsRpFrIntvl2HFpLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HFpLost.setStatus("mandatory")
_DsRpFrIntvl2HFpSent_Type = Counter32
_DsRpFrIntvl2HFpSent_Object = MibTableColumn
dsRpFrIntvl2HFpSent = _DsRpFrIntvl2HFpSent_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 11),
    _DsRpFrIntvl2HFpSent_Type()
)
dsRpFrIntvl2HFpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HFpSent.setStatus("mandatory")


class _DsRpFrIntvl2HStatus_Type(DisplayString):
    """Custom type dsRpFrIntvl2HStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DsRpFrIntvl2HStatus_Type.__name__ = "DisplayString"
_DsRpFrIntvl2HStatus_Object = MibTableColumn
dsRpFrIntvl2HStatus = _DsRpFrIntvl2HStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 5, 1, 12),
    _DsRpFrIntvl2HStatus_Type()
)
dsRpFrIntvl2HStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrIntvl2HStatus.setStatus("mandatory")
_DsRpFrTotalTable_Object = MibTable
dsRpFrTotalTable = _DsRpFrTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6)
)
if mibBuilder.loadTexts:
    dsRpFrTotalTable.setStatus("mandatory")
_DsRpFrTotalEntry_Object = MibTableRow
dsRpFrTotalEntry = _DsRpFrTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1)
)
dsRpFrTotalEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrTotalDir"),
    (0, "DATASMART-MIB", "dsRpFrTotalVcIndex"),
)
if mibBuilder.loadTexts:
    dsRpFrTotalEntry.setStatus("mandatory")


class _DsRpFrTotalDir_Type(Integer32):
    """Custom type dsRpFrTotalDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrTotalDir_Type.__name__ = "Integer32"
_DsRpFrTotalDir_Object = MibTableColumn
dsRpFrTotalDir = _DsRpFrTotalDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 1),
    _DsRpFrTotalDir_Type()
)
dsRpFrTotalDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalDir.setStatus("mandatory")


class _DsRpFrTotalVcIndex_Type(Integer32):
    """Custom type dsRpFrTotalVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_DsRpFrTotalVcIndex_Type.__name__ = "Integer32"
_DsRpFrTotalVcIndex_Object = MibTableColumn
dsRpFrTotalVcIndex = _DsRpFrTotalVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 2),
    _DsRpFrTotalVcIndex_Type()
)
dsRpFrTotalVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalVcIndex.setStatus("mandatory")


class _DsRpFrTotalVc_Type(Integer32):
    """Custom type dsRpFrTotalVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388607),
    )


_DsRpFrTotalVc_Type.__name__ = "Integer32"
_DsRpFrTotalVc_Object = MibTableColumn
dsRpFrTotalVc = _DsRpFrTotalVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 3),
    _DsRpFrTotalVc_Type()
)
dsRpFrTotalVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalVc.setStatus("mandatory")
_DsRpFrTotalFrames_Type = Counter32
_DsRpFrTotalFrames_Object = MibTableColumn
dsRpFrTotalFrames = _DsRpFrTotalFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 4),
    _DsRpFrTotalFrames_Type()
)
dsRpFrTotalFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalFrames.setStatus("mandatory")
_DsRpFrTotalOctets_Type = Counter32
_DsRpFrTotalOctets_Object = MibTableColumn
dsRpFrTotalOctets = _DsRpFrTotalOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 5),
    _DsRpFrTotalOctets_Type()
)
dsRpFrTotalOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalOctets.setStatus("mandatory")
_DsRpFrTotalKbps_Type = Gauge32
_DsRpFrTotalKbps_Object = MibTableColumn
dsRpFrTotalKbps = _DsRpFrTotalKbps_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 6),
    _DsRpFrTotalKbps_Type()
)
dsRpFrTotalKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalKbps.setStatus("mandatory")
_DsRpFrTotalFpMax_Type = Counter32
_DsRpFrTotalFpMax_Object = MibTableColumn
dsRpFrTotalFpMax = _DsRpFrTotalFpMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 7),
    _DsRpFrTotalFpMax_Type()
)
dsRpFrTotalFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalFpMax.setStatus("mandatory")
_DsRpFrTotalFpAvg_Type = Gauge32
_DsRpFrTotalFpAvg_Object = MibTableColumn
dsRpFrTotalFpAvg = _DsRpFrTotalFpAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 8),
    _DsRpFrTotalFpAvg_Type()
)
dsRpFrTotalFpAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalFpAvg.setStatus("mandatory")
_DsRpFrTotalFpLost_Type = Counter32
_DsRpFrTotalFpLost_Object = MibTableColumn
dsRpFrTotalFpLost = _DsRpFrTotalFpLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 9),
    _DsRpFrTotalFpLost_Type()
)
dsRpFrTotalFpLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalFpLost.setStatus("mandatory")
_DsRpFrTotalFpSent_Type = Counter32
_DsRpFrTotalFpSent_Object = MibTableColumn
dsRpFrTotalFpSent = _DsRpFrTotalFpSent_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 10),
    _DsRpFrTotalFpSent_Type()
)
dsRpFrTotalFpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalFpSent.setStatus("mandatory")


class _DsRpFrTotalStatus_Type(DisplayString):
    """Custom type dsRpFrTotalStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DsRpFrTotalStatus_Type.__name__ = "DisplayString"
_DsRpFrTotalStatus_Object = MibTableColumn
dsRpFrTotalStatus = _DsRpFrTotalStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 6, 1, 11),
    _DsRpFrTotalStatus_Type()
)
dsRpFrTotalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrTotalStatus.setStatus("mandatory")
_DsRpFrDayTable_Object = MibTable
dsRpFrDayTable = _DsRpFrDayTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7)
)
if mibBuilder.loadTexts:
    dsRpFrDayTable.setStatus("mandatory")
_DsRpFrDayEntry_Object = MibTableRow
dsRpFrDayEntry = _DsRpFrDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1)
)
dsRpFrDayEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrDayDir"),
    (0, "DATASMART-MIB", "dsRpFrDayVcIndex"),
    (0, "DATASMART-MIB", "dsRpFrDayNum"),
)
if mibBuilder.loadTexts:
    dsRpFrDayEntry.setStatus("mandatory")


class _DsRpFrDayDir_Type(Integer32):
    """Custom type dsRpFrDayDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrDayDir_Type.__name__ = "Integer32"
_DsRpFrDayDir_Object = MibTableColumn
dsRpFrDayDir = _DsRpFrDayDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 1),
    _DsRpFrDayDir_Type()
)
dsRpFrDayDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayDir.setStatus("mandatory")


class _DsRpFrDayVcIndex_Type(Integer32):
    """Custom type dsRpFrDayVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_DsRpFrDayVcIndex_Type.__name__ = "Integer32"
_DsRpFrDayVcIndex_Object = MibTableColumn
dsRpFrDayVcIndex = _DsRpFrDayVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 2),
    _DsRpFrDayVcIndex_Type()
)
dsRpFrDayVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayVcIndex.setStatus("mandatory")


class _DsRpFrDayNum_Type(Integer32):
    """Custom type dsRpFrDayNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DsRpFrDayNum_Type.__name__ = "Integer32"
_DsRpFrDayNum_Object = MibTableColumn
dsRpFrDayNum = _DsRpFrDayNum_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 3),
    _DsRpFrDayNum_Type()
)
dsRpFrDayNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayNum.setStatus("mandatory")


class _DsRpFrDayVc_Type(Integer32):
    """Custom type dsRpFrDayVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388607),
    )


_DsRpFrDayVc_Type.__name__ = "Integer32"
_DsRpFrDayVc_Object = MibTableColumn
dsRpFrDayVc = _DsRpFrDayVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 4),
    _DsRpFrDayVc_Type()
)
dsRpFrDayVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayVc.setStatus("mandatory")
_DsRpFrDayFrames_Type = Counter32
_DsRpFrDayFrames_Object = MibTableColumn
dsRpFrDayFrames = _DsRpFrDayFrames_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 5),
    _DsRpFrDayFrames_Type()
)
dsRpFrDayFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayFrames.setStatus("mandatory")
_DsRpFrDayOctets_Type = Counter32
_DsRpFrDayOctets_Object = MibTableColumn
dsRpFrDayOctets = _DsRpFrDayOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 6),
    _DsRpFrDayOctets_Type()
)
dsRpFrDayOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayOctets.setStatus("mandatory")
_DsRpFrDayKbps_Type = Gauge32
_DsRpFrDayKbps_Object = MibTableColumn
dsRpFrDayKbps = _DsRpFrDayKbps_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 7),
    _DsRpFrDayKbps_Type()
)
dsRpFrDayKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayKbps.setStatus("mandatory")
_DsRpFrDayFpMax_Type = Counter32
_DsRpFrDayFpMax_Object = MibTableColumn
dsRpFrDayFpMax = _DsRpFrDayFpMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 8),
    _DsRpFrDayFpMax_Type()
)
dsRpFrDayFpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayFpMax.setStatus("mandatory")
_DsRpFrDayFpAvg_Type = Gauge32
_DsRpFrDayFpAvg_Object = MibTableColumn
dsRpFrDayFpAvg = _DsRpFrDayFpAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 9),
    _DsRpFrDayFpAvg_Type()
)
dsRpFrDayFpAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayFpAvg.setStatus("mandatory")
_DsRpFrDayFpLost_Type = Counter32
_DsRpFrDayFpLost_Object = MibTableColumn
dsRpFrDayFpLost = _DsRpFrDayFpLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 10),
    _DsRpFrDayFpLost_Type()
)
dsRpFrDayFpLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayFpLost.setStatus("mandatory")
_DsRpFrDayFpSent_Type = Counter32
_DsRpFrDayFpSent_Object = MibTableColumn
dsRpFrDayFpSent = _DsRpFrDayFpSent_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 11),
    _DsRpFrDayFpSent_Type()
)
dsRpFrDayFpSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayFpSent.setStatus("mandatory")


class _DsRpFrDayStatus_Type(DisplayString):
    """Custom type dsRpFrDayStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DsRpFrDayStatus_Type.__name__ = "DisplayString"
_DsRpFrDayStatus_Object = MibTableColumn
dsRpFrDayStatus = _DsRpFrDayStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 7, 1, 12),
    _DsRpFrDayStatus_Type()
)
dsRpFrDayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrDayStatus.setStatus("mandatory")
_DsRpFrUrTable_Object = MibTable
dsRpFrUrTable = _DsRpFrUrTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8)
)
if mibBuilder.loadTexts:
    dsRpFrUrTable.setStatus("mandatory")
_DsRpFrUrEntry_Object = MibTableRow
dsRpFrUrEntry = _DsRpFrUrEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1)
)
dsRpFrUrEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpFrUrDir"),
    (0, "DATASMART-MIB", "dsRpFrUrVcIndex"),
)
if mibBuilder.loadTexts:
    dsRpFrUrEntry.setStatus("mandatory")


class _DsRpFrUrDir_Type(Integer32):
    """Custom type dsRpFrUrDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsRpFrUrDir_Type.__name__ = "Integer32"
_DsRpFrUrDir_Object = MibTableColumn
dsRpFrUrDir = _DsRpFrUrDir_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1, 1),
    _DsRpFrUrDir_Type()
)
dsRpFrUrDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrUrDir.setStatus("mandatory")


class _DsRpFrUrVcIndex_Type(Integer32):
    """Custom type dsRpFrUrVcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65),
    )


_DsRpFrUrVcIndex_Type.__name__ = "Integer32"
_DsRpFrUrVcIndex_Object = MibTableColumn
dsRpFrUrVcIndex = _DsRpFrUrVcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1, 2),
    _DsRpFrUrVcIndex_Type()
)
dsRpFrUrVcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrUrVcIndex.setStatus("mandatory")


class _DsRpFrUrVc_Type(Integer32):
    """Custom type dsRpFrUrVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8388607),
    )


_DsRpFrUrVc_Type.__name__ = "Integer32"
_DsRpFrUrVc_Object = MibTableColumn
dsRpFrUrVc = _DsRpFrUrVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1, 3),
    _DsRpFrUrVc_Type()
)
dsRpFrUrVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrUrVc.setStatus("mandatory")
_DsRpFrUrCIRExceeded_Type = Counter32
_DsRpFrUrCIRExceeded_Object = MibTableColumn
dsRpFrUrCIRExceeded = _DsRpFrUrCIRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1, 4),
    _DsRpFrUrCIRExceeded_Type()
)
dsRpFrUrCIRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrUrCIRExceeded.setStatus("mandatory")
_DsRpFrUrCIRExceededOctets_Type = Counter32
_DsRpFrUrCIRExceededOctets_Object = MibTableColumn
dsRpFrUrCIRExceededOctets = _DsRpFrUrCIRExceededOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1, 5),
    _DsRpFrUrCIRExceededOctets_Type()
)
dsRpFrUrCIRExceededOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrUrCIRExceededOctets.setStatus("mandatory")
_DsRpFrUrEIRExceeded_Type = Counter32
_DsRpFrUrEIRExceeded_Object = MibTableColumn
dsRpFrUrEIRExceeded = _DsRpFrUrEIRExceeded_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1, 6),
    _DsRpFrUrEIRExceeded_Type()
)
dsRpFrUrEIRExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrUrEIRExceeded.setStatus("mandatory")
_DsRpFrUrEIRExceededOctets_Type = Counter32
_DsRpFrUrEIRExceededOctets_Object = MibTableColumn
dsRpFrUrEIRExceededOctets = _DsRpFrUrEIRExceededOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 10, 8, 1, 7),
    _DsRpFrUrEIRExceededOctets_Type()
)
dsRpFrUrEIRExceededOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpFrUrEIRExceededOctets.setStatus("mandatory")
_DsRpDdsDuration_Type = TimeTicks
_DsRpDdsDuration_Object = MibScalar
dsRpDdsDuration = _DsRpDdsDuration_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 11),
    _DsRpDdsDuration_Type()
)
dsRpDdsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpDdsDuration.setStatus("mandatory")
_DsRpDdsTable_Object = MibTable
dsRpDdsTable = _DsRpDdsTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 12)
)
if mibBuilder.loadTexts:
    dsRpDdsTable.setStatus("mandatory")
_DsRpDdsEntry_Object = MibTableRow
dsRpDdsEntry = _DsRpDdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 12, 1)
)
dsRpDdsEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsRpDdsIfIndex"),
)
if mibBuilder.loadTexts:
    dsRpDdsEntry.setStatus("mandatory")
_DsRpDdsIfIndex_Type = Integer32
_DsRpDdsIfIndex_Object = MibTableColumn
dsRpDdsIfIndex = _DsRpDdsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 12, 1, 1),
    _DsRpDdsIfIndex_Type()
)
dsRpDdsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpDdsIfIndex.setStatus("mandatory")
_DsRpDdsAvailableSecs_Type = Counter32
_DsRpDdsAvailableSecs_Object = MibTableColumn
dsRpDdsAvailableSecs = _DsRpDdsAvailableSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 12, 1, 2),
    _DsRpDdsAvailableSecs_Type()
)
dsRpDdsAvailableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpDdsAvailableSecs.setStatus("mandatory")
_DsRpDdsTotalSecs_Type = Counter32
_DsRpDdsTotalSecs_Object = MibTableColumn
dsRpDdsTotalSecs = _DsRpDdsTotalSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 12, 1, 3),
    _DsRpDdsTotalSecs_Type()
)
dsRpDdsTotalSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpDdsTotalSecs.setStatus("mandatory")
_DsRpDdsBPVs_Type = Counter32
_DsRpDdsBPVs_Object = MibTableColumn
dsRpDdsBPVs = _DsRpDdsBPVs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 2, 12, 1, 4),
    _DsRpDdsBPVs_Type()
)
dsRpDdsBPVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRpDdsBPVs.setStatus("mandatory")
_DsLm_ObjectIdentity = ObjectIdentity
dsLm = _DsLm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 3)
)


class _DsLmLoopback_Type(Integer32):
    """Custom type dsLmLoopback based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("lmLbkCsu", 10),
          ("lmLbkDp1", 6),
          ("lmLbkDp2", 7),
          ("lmLbkDpdt", 12),
          ("lmLbkDsu", 11),
          ("lmLbkDt1", 8),
          ("lmLbkDt2", 9),
          ("lmLbkLine", 2),
          ("lmLbkLocal", 4),
          ("lmLbkNone", 1),
          ("lmLbkPayload", 3),
          ("lmLbkTiTest", 5))
    )


_DsLmLoopback_Type.__name__ = "Integer32"
_DsLmLoopback_Object = MibScalar
dsLmLoopback = _DsLmLoopback_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 3, 1),
    _DsLmLoopback_Type()
)
dsLmLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsLmLoopback.setStatus("mandatory")


class _DsLmSelfTestState_Type(Integer32):
    """Custom type dsLmSelfTestState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lmSelfTestIdle", 1),
          ("lmSelfTestStart", 2))
    )


_DsLmSelfTestState_Type.__name__ = "Integer32"
_DsLmSelfTestState_Object = MibScalar
dsLmSelfTestState = _DsLmSelfTestState_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 3, 2),
    _DsLmSelfTestState_Type()
)
dsLmSelfTestState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsLmSelfTestState.setStatus("mandatory")


class _DsLmSelfTestResults_Type(DisplayString):
    """Custom type dsLmSelfTestResults based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsLmSelfTestResults_Type.__name__ = "DisplayString"
_DsLmSelfTestResults_Object = MibScalar
dsLmSelfTestResults = _DsLmSelfTestResults_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 3, 3),
    _DsLmSelfTestResults_Type()
)
dsLmSelfTestResults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsLmSelfTestResults.setStatus("mandatory")
_DsRm_ObjectIdentity = ObjectIdentity
dsRm = _DsRm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4)
)


class _DsRmLbkCode_Type(Integer32):
    """Custom type dsRmLbkCode based on Integer32"""
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
        *(("rmRDp1", 5),
          ("rmRDp2", 6),
          ("rmRLine", 3),
          ("rmRNone", 1),
          ("rmRPayload", 4),
          ("rmRst1", 2))
    )


_DsRmLbkCode_Type.__name__ = "Integer32"
_DsRmLbkCode_Object = MibScalar
dsRmLbkCode = _DsRmLbkCode_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 1),
    _DsRmLbkCode_Type()
)
dsRmLbkCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmLbkCode.setStatus("mandatory")


class _DsRmTestCode_Type(Integer32):
    """Custom type dsRmTestCode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("rmTest2047Dp1", 8),
          ("rmTest2047Dp2", 9),
          ("rmTest2toThe15", 11),
          ("rmTest2toThe23", 10),
          ("rmTest324", 3),
          ("rmTest511Dp1", 6),
          ("rmTest511Dp2", 7),
          ("rmTestNone", 1),
          ("rmTestOnes", 4),
          ("rmTestQrs", 2),
          ("rmTestZeros", 5))
    )


_DsRmTestCode_Type.__name__ = "Integer32"
_DsRmTestCode_Object = MibScalar
dsRmTestCode = _DsRmTestCode_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 2),
    _DsRmTestCode_Type()
)
dsRmTestCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmTestCode.setStatus("mandatory")


class _DsRmBertState_Type(Integer32):
    """Custom type dsRmBertState based on Integer32"""
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
        *(("rmBertFound", 4),
          ("rmBertIdle", 1),
          ("rmBertOtherStart", 2),
          ("rmBertSearching", 3))
    )


_DsRmBertState_Type.__name__ = "Integer32"
_DsRmBertState_Object = MibScalar
dsRmBertState = _DsRmBertState_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 3),
    _DsRmBertState_Type()
)
dsRmBertState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmBertState.setStatus("mandatory")


class _DsRmBertCode_Type(Integer32):
    """Custom type dsRmBertCode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("rmBert2047Dp1", 8),
          ("rmBert2047Dp2", 9),
          ("rmBert324", 3),
          ("rmBert511Dp1", 6),
          ("rmBert511Dp2", 7),
          ("rmBertNone", 1),
          ("rmBertOnes", 4),
          ("rmBertQrs", 2),
          ("rmBertZeros", 5),
          ("rmTest2toThe15", 11),
          ("rmTest2toThe23", 10))
    )


_DsRmBertCode_Type.__name__ = "Integer32"
_DsRmBertCode_Object = MibScalar
dsRmBertCode = _DsRmBertCode_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 4),
    _DsRmBertCode_Type()
)
dsRmBertCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmBertCode.setStatus("mandatory")


class _DsRmBertTestSecs_Type(Integer32):
    """Custom type dsRmBertTestSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsRmBertTestSecs_Type.__name__ = "Integer32"
_DsRmBertTestSecs_Object = MibScalar
dsRmBertTestSecs = _DsRmBertTestSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 5),
    _DsRmBertTestSecs_Type()
)
dsRmBertTestSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmBertTestSecs.setStatus("mandatory")


class _DsRmBertBitErrors_Type(Integer32):
    """Custom type dsRmBertBitErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsRmBertBitErrors_Type.__name__ = "Integer32"
_DsRmBertBitErrors_Object = MibScalar
dsRmBertBitErrors = _DsRmBertBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 6),
    _DsRmBertBitErrors_Type()
)
dsRmBertBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmBertBitErrors.setStatus("mandatory")


class _DsRmBertErrdSecs_Type(Integer32):
    """Custom type dsRmBertErrdSecs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsRmBertErrdSecs_Type.__name__ = "Integer32"
_DsRmBertErrdSecs_Object = MibScalar
dsRmBertErrdSecs = _DsRmBertErrdSecs_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 7),
    _DsRmBertErrdSecs_Type()
)
dsRmBertErrdSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmBertErrdSecs.setStatus("mandatory")


class _DsRmBertTotalErrors_Type(Integer32):
    """Custom type dsRmBertTotalErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsRmBertTotalErrors_Type.__name__ = "Integer32"
_DsRmBertTotalErrors_Object = MibScalar
dsRmBertTotalErrors = _DsRmBertTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 8),
    _DsRmBertTotalErrors_Type()
)
dsRmBertTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmBertTotalErrors.setStatus("mandatory")


class _DsRmBertReSync_Type(Integer32):
    """Custom type dsRmBertReSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsRmBertReSync_Type.__name__ = "Integer32"
_DsRmBertReSync_Object = MibScalar
dsRmBertReSync = _DsRmBertReSync_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 9),
    _DsRmBertReSync_Type()
)
dsRmBertReSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmBertReSync.setStatus("mandatory")
_DsRmFping_ObjectIdentity = ObjectIdentity
dsRmFping = _DsRmFping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10)
)


class _DsRmFpingAction_Type(Integer32):
    """Custom type dsRmFpingAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rmFpingStart", 1),
          ("rmFpingStop", 2))
    )


_DsRmFpingAction_Type.__name__ = "Integer32"
_DsRmFpingAction_Object = MibScalar
dsRmFpingAction = _DsRmFpingAction_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 1),
    _DsRmFpingAction_Type()
)
dsRmFpingAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmFpingAction.setStatus("mandatory")


class _DsRmFpingState_Type(Integer32):
    """Custom type dsRmFpingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rmFpingIdle", 1),
          ("rmFpingOtherStart", 2),
          ("rmFpingRunning", 3))
    )


_DsRmFpingState_Type.__name__ = "Integer32"
_DsRmFpingState_Object = MibScalar
dsRmFpingState = _DsRmFpingState_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 2),
    _DsRmFpingState_Type()
)
dsRmFpingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingState.setStatus("mandatory")


class _DsRmFpingVc_Type(Integer32):
    """Custom type dsRmFpingVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_DsRmFpingVc_Type.__name__ = "Integer32"
_DsRmFpingVc_Object = MibScalar
dsRmFpingVc = _DsRmFpingVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 3),
    _DsRmFpingVc_Type()
)
dsRmFpingVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmFpingVc.setStatus("mandatory")


class _DsRmFpingFreq_Type(Integer32):
    """Custom type dsRmFpingFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_DsRmFpingFreq_Type.__name__ = "Integer32"
_DsRmFpingFreq_Object = MibScalar
dsRmFpingFreq = _DsRmFpingFreq_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 4),
    _DsRmFpingFreq_Type()
)
dsRmFpingFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmFpingFreq.setStatus("mandatory")


class _DsRmFpingLen_Type(Integer32):
    """Custom type dsRmFpingLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1400),
    )


_DsRmFpingLen_Type.__name__ = "Integer32"
_DsRmFpingLen_Object = MibScalar
dsRmFpingLen = _DsRmFpingLen_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 5),
    _DsRmFpingLen_Type()
)
dsRmFpingLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmFpingLen.setStatus("mandatory")


class _DsRmFpingCur_Type(Integer32):
    """Custom type dsRmFpingCur based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_DsRmFpingCur_Type.__name__ = "Integer32"
_DsRmFpingCur_Object = MibScalar
dsRmFpingCur = _DsRmFpingCur_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 6),
    _DsRmFpingCur_Type()
)
dsRmFpingCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingCur.setStatus("mandatory")


class _DsRmFpingMin_Type(Integer32):
    """Custom type dsRmFpingMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_DsRmFpingMin_Type.__name__ = "Integer32"
_DsRmFpingMin_Object = MibScalar
dsRmFpingMin = _DsRmFpingMin_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 7),
    _DsRmFpingMin_Type()
)
dsRmFpingMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingMin.setStatus("mandatory")


class _DsRmFpingMax_Type(Integer32):
    """Custom type dsRmFpingMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_DsRmFpingMax_Type.__name__ = "Integer32"
_DsRmFpingMax_Object = MibScalar
dsRmFpingMax = _DsRmFpingMax_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 8),
    _DsRmFpingMax_Type()
)
dsRmFpingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingMax.setStatus("mandatory")


class _DsRmFpingAvg_Type(Integer32):
    """Custom type dsRmFpingAvg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_DsRmFpingAvg_Type.__name__ = "Integer32"
_DsRmFpingAvg_Object = MibScalar
dsRmFpingAvg = _DsRmFpingAvg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 9),
    _DsRmFpingAvg_Type()
)
dsRmFpingAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingAvg.setStatus("mandatory")


class _DsRmFpingLost_Type(Integer32):
    """Custom type dsRmFpingLost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsRmFpingLost_Type.__name__ = "Integer32"
_DsRmFpingLost_Object = MibScalar
dsRmFpingLost = _DsRmFpingLost_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 10),
    _DsRmFpingLost_Type()
)
dsRmFpingLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingLost.setStatus("mandatory")


class _DsRmFpingTotal_Type(Integer32):
    """Custom type dsRmFpingTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DsRmFpingTotal_Type.__name__ = "Integer32"
_DsRmFpingTotal_Object = MibScalar
dsRmFpingTotal = _DsRmFpingTotal_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 11),
    _DsRmFpingTotal_Type()
)
dsRmFpingTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingTotal.setStatus("mandatory")


class _DsRmFpingRmtVc_Type(DisplayString):
    """Custom type dsRmFpingRmtVc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_DsRmFpingRmtVc_Type.__name__ = "DisplayString"
_DsRmFpingRmtVc_Object = MibScalar
dsRmFpingRmtVc = _DsRmFpingRmtVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 12),
    _DsRmFpingRmtVc_Type()
)
dsRmFpingRmtVc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingRmtVc.setStatus("mandatory")
_DsRmFpingRmtIp_Type = IpAddress
_DsRmFpingRmtIp_Object = MibScalar
dsRmFpingRmtIp = _DsRmFpingRmtIp_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 10, 13),
    _DsRmFpingRmtIp_Type()
)
dsRmFpingRmtIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsRmFpingRmtIp.setStatus("mandatory")


class _DsRmInsertBitError_Type(Integer32):
    """Custom type dsRmInsertBitError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insertBitError", 1),
          ("noInsertBitError", 2))
    )


_DsRmInsertBitError_Type.__name__ = "Integer32"
_DsRmInsertBitError_Object = MibScalar
dsRmInsertBitError = _DsRmInsertBitError_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 4, 11),
    _DsRmInsertBitError_Type()
)
dsRmInsertBitError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsRmInsertBitError.setStatus("mandatory")
_DsAc_ObjectIdentity = ObjectIdentity
dsAc = _DsAc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5)
)


class _DsAcAlmMsg_Type(Integer32):
    """Custom type dsAcAlmMsg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acAlmMsgDisable", 2),
          ("acAlmMsgEnable", 1))
    )


_DsAcAlmMsg_Type.__name__ = "Integer32"
_DsAcAlmMsg_Object = MibScalar
dsAcAlmMsg = _DsAcAlmMsg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 1),
    _DsAcAlmMsg_Type()
)
dsAcAlmMsg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcAlmMsg.setStatus("mandatory")


class _DsAcYelAlm_Type(Integer32):
    """Custom type dsAcYelAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acYelAlmDisable", 2),
          ("acYelAlmEnable", 1))
    )


_DsAcYelAlm_Type.__name__ = "Integer32"
_DsAcYelAlm_Object = MibScalar
dsAcYelAlm = _DsAcYelAlm_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 2),
    _DsAcYelAlm_Type()
)
dsAcYelAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcYelAlm.setStatus("mandatory")


class _DsAcDeact_Type(Integer32):
    """Custom type dsAcDeact based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_DsAcDeact_Type.__name__ = "Integer32"
_DsAcDeact_Object = MibScalar
dsAcDeact = _DsAcDeact_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 3),
    _DsAcDeact_Type()
)
dsAcDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcDeact.setStatus("mandatory")


class _DsAcEst_Type(Integer32):
    """Custom type dsAcEst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAcEst_Type.__name__ = "Integer32"
_DsAcEst_Object = MibScalar
dsAcEst = _DsAcEst_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 4),
    _DsAcEst_Type()
)
dsAcEst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcEst.setStatus("mandatory")


class _DsAcUst_Type(Integer32):
    """Custom type dsAcUst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_DsAcUst_Type.__name__ = "Integer32"
_DsAcUst_Object = MibScalar
dsAcUst = _DsAcUst_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 5),
    _DsAcUst_Type()
)
dsAcUst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcUst.setStatus("mandatory")


class _DsAcSt_Type(Integer32):
    """Custom type dsAcSt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acSt15", 1),
          ("acSt60", 2))
    )


_DsAcSt_Type.__name__ = "Integer32"
_DsAcSt_Object = MibScalar
dsAcSt = _DsAcSt_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 6),
    _DsAcSt_Type()
)
dsAcSt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcSt.setStatus("mandatory")


class _DsAcBerAlm_Type(Integer32):
    """Custom type dsAcBerAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acBerAlmDisable", 2),
          ("acBerAlmEnable", 1))
    )


_DsAcBerAlm_Type.__name__ = "Integer32"
_DsAcBerAlm_Object = MibScalar
dsAcBerAlm = _DsAcBerAlm_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 7),
    _DsAcBerAlm_Type()
)
dsAcBerAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcBerAlm.setStatus("mandatory")


class _DsAcRfaAlm_Type(Integer32):
    """Custom type dsAcRfaAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acRfaAlmDisable", 2),
          ("acRfaAlmEnable", 1))
    )


_DsAcRfaAlm_Type.__name__ = "Integer32"
_DsAcRfaAlm_Object = MibScalar
dsAcRfaAlm = _DsAcRfaAlm_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 8),
    _DsAcRfaAlm_Type()
)
dsAcRfaAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcRfaAlm.setStatus("mandatory")


class _DsAcAisAlm_Type(Integer32):
    """Custom type dsAcAisAlm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acAisAlmDisable", 2),
          ("acAisAlmEnable", 1))
    )


_DsAcAisAlm_Type.__name__ = "Integer32"
_DsAcAisAlm_Object = MibScalar
dsAcAisAlm = _DsAcAisAlm_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 5, 9),
    _DsAcAisAlm_Type()
)
dsAcAisAlm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAcAisAlm.setStatus("mandatory")
_DsCc_ObjectIdentity = ObjectIdentity
dsCc = _DsCc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6)
)


class _DsCcEcho_Type(Integer32):
    """Custom type dsCcEcho based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccEchoDisable", 2),
          ("ccEchoEnable", 1))
    )


_DsCcEcho_Type.__name__ = "Integer32"
_DsCcEcho_Object = MibScalar
dsCcEcho = _DsCcEcho_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 1),
    _DsCcEcho_Type()
)
dsCcEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCcEcho.setStatus("mandatory")


class _DsCcControlPort_Type(Integer32):
    """Custom type dsCcControlPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ccDce", 1),
          ("ccDte", 2))
    )


_DsCcControlPort_Type.__name__ = "Integer32"
_DsCcControlPort_Object = MibScalar
dsCcControlPort = _DsCcControlPort_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 2),
    _DsCcControlPort_Type()
)
dsCcControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsCcControlPort.setStatus("mandatory")


class _DsCcBaud_Type(Integer32):
    """Custom type dsCcBaud based on Integer32"""
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
        *(("cc19200", 3),
          ("cc2400", 1),
          ("cc38400", 4),
          ("cc9600", 2))
    )


_DsCcBaud_Type.__name__ = "Integer32"
_DsCcBaud_Object = MibScalar
dsCcBaud = _DsCcBaud_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 3),
    _DsCcBaud_Type()
)
dsCcBaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCcBaud.setStatus("mandatory")


class _DsCcParity_Type(Integer32):
    """Custom type dsCcParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ccEven", 2),
          ("ccNone", 1),
          ("ccOdd", 3))
    )


_DsCcParity_Type.__name__ = "Integer32"
_DsCcParity_Object = MibScalar
dsCcParity = _DsCcParity_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 4),
    _DsCcParity_Type()
)
dsCcParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCcParity.setStatus("mandatory")


class _DsCcDataBits_Type(Integer32):
    """Custom type dsCcDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cc7Bit", 1),
          ("cc8Bit", 2))
    )


_DsCcDataBits_Type.__name__ = "Integer32"
_DsCcDataBits_Object = MibScalar
dsCcDataBits = _DsCcDataBits_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 5),
    _DsCcDataBits_Type()
)
dsCcDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCcDataBits.setStatus("mandatory")


class _DsCcStopBits_Type(Integer32):
    """Custom type dsCcStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cc1Bit", 1),
          ("cc2Bit", 2))
    )


_DsCcStopBits_Type.__name__ = "Integer32"
_DsCcStopBits_Object = MibScalar
dsCcStopBits = _DsCcStopBits_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 6),
    _DsCcStopBits_Type()
)
dsCcStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCcStopBits.setStatus("mandatory")


class _DsCcDceIn_Type(Integer32):
    """Custom type dsCcDceIn based on Integer32"""
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
        *(("ccBothOff", 1),
          ("ccBothOn", 4),
          ("ccRtsOffDtrOn", 3),
          ("ccRtsOnDtrOff", 2))
    )


_DsCcDceIn_Type.__name__ = "Integer32"
_DsCcDceIn_Object = MibScalar
dsCcDceIn = _DsCcDceIn_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 7),
    _DsCcDceIn_Type()
)
dsCcDceIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCcDceIn.setStatus("mandatory")


class _DsCcDteIn_Type(Integer32):
    """Custom type dsCcDteIn based on Integer32"""
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
        *(("ccBothOff", 1),
          ("ccBothOn", 4),
          ("ccCtsOffDcdOn", 3),
          ("ccCtsOnDcdOff", 2))
    )


_DsCcDteIn_Type.__name__ = "Integer32"
_DsCcDteIn_Object = MibScalar
dsCcDteIn = _DsCcDteIn_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 6, 8),
    _DsCcDteIn_Type()
)
dsCcDteIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsCcDteIn.setStatus("mandatory")
_DsDc_ObjectIdentity = ObjectIdentity
dsDc = _DsDc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7)
)
_DsDcTable_Object = MibTable
dsDcTable = _DsDcTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    dsDcTable.setStatus("mandatory")
_DsDcEntry_Object = MibTableRow
dsDcEntry = _DsDcEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1)
)
dsDcEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsDcIndex"),
)
if mibBuilder.loadTexts:
    dsDcEntry.setStatus("mandatory")


class _DsDcIndex_Type(Integer32):
    """Custom type dsDcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DsDcIndex_Type.__name__ = "Integer32"
_DsDcIndex_Object = MibTableColumn
dsDcIndex = _DsDcIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 1),
    _DsDcIndex_Type()
)
dsDcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsDcIndex.setStatus("mandatory")


class _DsDcDataInvert_Type(Integer32):
    """Custom type dsDcDataInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcDataInvertDisable", 2),
          ("dcDataInvertEnable", 1))
    )


_DsDcDataInvert_Type.__name__ = "Integer32"
_DsDcDataInvert_Object = MibTableColumn
dsDcDataInvert = _DsDcDataInvert_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 2),
    _DsDcDataInvert_Type()
)
dsDcDataInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDcDataInvert.setStatus("mandatory")


class _DsDcInterface_Type(Integer32):
    """Custom type dsDcInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dcEia530Interface", 2),
          ("dcV35DSInterface", 3),
          ("dcV35Interface", 1))
    )


_DsDcInterface_Type.__name__ = "Integer32"
_DsDcInterface_Object = MibTableColumn
dsDcInterface = _DsDcInterface_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 3),
    _DsDcInterface_Type()
)
dsDcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDcInterface.setStatus("mandatory")


class _DsDcClockSource_Type(Integer32):
    """Custom type dsDcClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcExternalClock", 2),
          ("dcInternalClock", 1))
    )


_DsDcClockSource_Type.__name__ = "Integer32"
_DsDcClockSource_Object = MibTableColumn
dsDcClockSource = _DsDcClockSource_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 4),
    _DsDcClockSource_Type()
)
dsDcClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDcClockSource.setStatus("mandatory")


class _DsDcXmtClkInvert_Type(Integer32):
    """Custom type dsDcXmtClkInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcXClkInvertDisable", 2),
          ("dcXClkInvertEnable", 1))
    )


_DsDcXmtClkInvert_Type.__name__ = "Integer32"
_DsDcXmtClkInvert_Object = MibTableColumn
dsDcXmtClkInvert = _DsDcXmtClkInvert_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 5),
    _DsDcXmtClkInvert_Type()
)
dsDcXmtClkInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDcXmtClkInvert.setStatus("mandatory")


class _DsDcRcvClkInvert_Type(Integer32):
    """Custom type dsDcRcvClkInvert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcRClkInvertDisable", 2),
          ("dcRClkInvertEnable", 1))
    )


_DsDcRcvClkInvert_Type.__name__ = "Integer32"
_DsDcRcvClkInvert_Object = MibTableColumn
dsDcRcvClkInvert = _DsDcRcvClkInvert_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 6),
    _DsDcRcvClkInvert_Type()
)
dsDcRcvClkInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDcRcvClkInvert.setStatus("mandatory")


class _DsDcIdleChar_Type(Integer32):
    """Custom type dsDcIdleChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dc7eIdleChar", 1),
          ("dc7fIdleChar", 2),
          ("dcffIdleChar", 3))
    )


_DsDcIdleChar_Type.__name__ = "Integer32"
_DsDcIdleChar_Object = MibTableColumn
dsDcIdleChar = _DsDcIdleChar_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 7),
    _DsDcIdleChar_Type()
)
dsDcIdleChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDcIdleChar.setStatus("mandatory")


class _DsDcLOSInput_Type(Integer32):
    """Custom type dsDcLOSInput based on Integer32"""
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
        *(("dcLosBoth", 4),
          ("dcLosDTR", 3),
          ("dcLosNone", 1),
          ("dcLosRTS", 2))
    )


_DsDcLOSInput_Type.__name__ = "Integer32"
_DsDcLOSInput_Object = MibTableColumn
dsDcLOSInput = _DsDcLOSInput_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 7, 1, 1, 8),
    _DsDcLOSInput_Type()
)
dsDcLOSInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsDcLOSInput.setStatus("mandatory")
_DsFc_ObjectIdentity = ObjectIdentity
dsFc = _DsFc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8)
)


class _DsFcLoadXcute_Type(Integer32):
    """Custom type dsFcLoadXcute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fcLoadXcuteIdle", 1),
          ("fcLoadXcuteStartA", 2),
          ("fcLoadXcuteStartB", 3))
    )


_DsFcLoadXcute_Type.__name__ = "Integer32"
_DsFcLoadXcute_Object = MibScalar
dsFcLoadXcute = _DsFcLoadXcute_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8, 1),
    _DsFcLoadXcute_Type()
)
dsFcLoadXcute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFcLoadXcute.setStatus("mandatory")
_DsFcTable_Object = MibTable
dsFcTable = _DsFcTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8, 2)
)
if mibBuilder.loadTexts:
    dsFcTable.setStatus("mandatory")
_DsFcEntry_Object = MibTableRow
dsFcEntry = _DsFcEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8, 2, 1)
)
dsFcEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsFcTableIndex"),
    (0, "DATASMART-MIB", "dsFcChanIndex"),
)
if mibBuilder.loadTexts:
    dsFcEntry.setStatus("mandatory")


class _DsFcTableIndex_Type(Integer32):
    """Custom type dsFcTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_DsFcTableIndex_Type.__name__ = "Integer32"
_DsFcTableIndex_Object = MibTableColumn
dsFcTableIndex = _DsFcTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8, 2, 1, 1),
    _DsFcTableIndex_Type()
)
dsFcTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFcTableIndex.setStatus("mandatory")


class _DsFcChanIndex_Type(Integer32):
    """Custom type dsFcChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DsFcChanIndex_Type.__name__ = "Integer32"
_DsFcChanIndex_Object = MibTableColumn
dsFcChanIndex = _DsFcChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8, 2, 1, 2),
    _DsFcChanIndex_Type()
)
dsFcChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFcChanIndex.setStatus("mandatory")


class _DsFcChanMap_Type(Integer32):
    """Custom type dsFcChanMap based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("fcChan56Dp1", 4),
          ("fcChan56Dp2", 6),
          ("fcChan64Dp1", 5),
          ("fcChan64Dp2", 7),
          ("fcChanDLNK", 8),
          ("fcChanDPDL", 9),
          ("fcChanIdle", 1),
          ("fcChanTiData", 2),
          ("fcChanTiVoice", 3),
          ("fcChanUnav", 10))
    )


_DsFcChanMap_Type.__name__ = "Integer32"
_DsFcChanMap_Object = MibTableColumn
dsFcChanMap = _DsFcChanMap_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8, 2, 1, 3),
    _DsFcChanMap_Type()
)
dsFcChanMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFcChanMap.setStatus("mandatory")


class _DsFcMap16_Type(Integer32):
    """Custom type dsFcMap16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcMap16Unused", 2),
          ("fcMap16Used", 1))
    )


_DsFcMap16_Type.__name__ = "Integer32"
_DsFcMap16_Object = MibScalar
dsFcMap16 = _DsFcMap16_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 8, 3),
    _DsFcMap16_Type()
)
dsFcMap16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFcMap16.setStatus("mandatory")
_DsFmc_ObjectIdentity = ObjectIdentity
dsFmc = _DsFmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9)
)


class _DsFmcFrameType_Type(Integer32):
    """Custom type dsFmcFrameType based on Integer32"""
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
        *(("fmcAtmLlcSnap", 4),
          ("fmcAtmNlpid", 3),
          ("fmcAtmVcMux", 5),
          ("fmcFrEther", 2),
          ("fmcFrNlpid", 1))
    )


_DsFmcFrameType_Type.__name__ = "Integer32"
_DsFmcFrameType_Object = MibScalar
dsFmcFrameType = _DsFmcFrameType_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 1),
    _DsFmcFrameType_Type()
)
dsFmcFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcFrameType.setStatus("mandatory")


class _DsFmcAddrOctets_Type(Integer32):
    """Custom type dsFmcAddrOctets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fmcFourOctets", 2),
          ("fmcTwoOctets", 1))
    )


_DsFmcAddrOctets_Type.__name__ = "Integer32"
_DsFmcAddrOctets_Object = MibScalar
dsFmcAddrOctets = _DsFmcAddrOctets_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 2),
    _DsFmcAddrOctets_Type()
)
dsFmcAddrOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcAddrOctets.setStatus("mandatory")


class _DsFmcFcsBits_Type(Integer32):
    """Custom type dsFmcFcsBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fmc16Bits", 1),
          ("fmc32Bits", 2))
    )


_DsFmcFcsBits_Type.__name__ = "Integer32"
_DsFmcFcsBits_Object = MibScalar
dsFmcFcsBits = _DsFmcFcsBits_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 3),
    _DsFmcFcsBits_Type()
)
dsFmcFcsBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcFcsBits.setStatus("mandatory")


class _DsFmcUpperBW_Type(Integer32):
    """Custom type dsFmcUpperBW based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 95),
    )


_DsFmcUpperBW_Type.__name__ = "Integer32"
_DsFmcUpperBW_Object = MibScalar
dsFmcUpperBW = _DsFmcUpperBW_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 4),
    _DsFmcUpperBW_Type()
)
dsFmcUpperBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcUpperBW.setStatus("mandatory")


class _DsFmcFpingOper_Type(Integer32):
    """Custom type dsFmcFpingOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fmcFpoDisable", 2),
          ("fmcFpoEnable", 1))
    )


_DsFmcFpingOper_Type.__name__ = "Integer32"
_DsFmcFpingOper_Object = MibScalar
dsFmcFpingOper = _DsFmcFpingOper_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 5),
    _DsFmcFpingOper_Type()
)
dsFmcFpingOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcFpingOper.setStatus("mandatory")


class _DsFmcFpingGen_Type(Integer32):
    """Custom type dsFmcFpingGen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DsFmcFpingGen_Type.__name__ = "Integer32"
_DsFmcFpingGen_Object = MibScalar
dsFmcFpingGen = _DsFmcFpingGen_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 6),
    _DsFmcFpingGen_Type()
)
dsFmcFpingGen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcFpingGen.setStatus("mandatory")


class _DsFmcFpingThres_Type(Integer32):
    """Custom type dsFmcFpingThres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_DsFmcFpingThres_Type.__name__ = "Integer32"
_DsFmcFpingThres_Object = MibScalar
dsFmcFpingThres = _DsFmcFpingThres_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 7),
    _DsFmcFpingThres_Type()
)
dsFmcFpingThres.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcFpingThres.setStatus("mandatory")


class _DsFmcFpingRst_Type(Integer32):
    """Custom type dsFmcFpingRst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_DsFmcFpingRst_Type.__name__ = "Integer32"
_DsFmcFpingRst_Object = MibScalar
dsFmcFpingRst = _DsFmcFpingRst_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 8),
    _DsFmcFpingRst_Type()
)
dsFmcFpingRst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcFpingRst.setStatus("mandatory")


class _DsFmcAddVc_Type(Integer32):
    """Custom type dsFmcAddVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_DsFmcAddVc_Type.__name__ = "Integer32"
_DsFmcAddVc_Object = MibScalar
dsFmcAddVc = _DsFmcAddVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 9),
    _DsFmcAddVc_Type()
)
dsFmcAddVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcAddVc.setStatus("mandatory")


class _DsFmcDelVc_Type(Integer32):
    """Custom type dsFmcDelVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_DsFmcDelVc_Type.__name__ = "Integer32"
_DsFmcDelVc_Object = MibScalar
dsFmcDelVc = _DsFmcDelVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 9, 10),
    _DsFmcDelVc_Type()
)
dsFmcDelVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsFmcDelVc.setStatus("mandatory")
_DsMc_ObjectIdentity = ObjectIdentity
dsMc = _DsMc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10)
)


class _DsMcNetif_Type(Integer32):
    """Custom type dsMcNetif based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("mcNetDatalink", 5),
          ("mcNetED", 7),
          ("mcNetES", 6),
          ("mcNetESD", 8),
          ("mcNetEthernet", 2),
          ("mcNetInband", 11),
          ("mcNetNone", 1),
          ("mcNetPSD", 9),
          ("mcNetPppSlip", 3),
          ("mcNetSD", 10),
          ("mcNetSlip", 4))
    )


_DsMcNetif_Type.__name__ = "Integer32"
_DsMcNetif_Object = MibScalar
dsMcNetif = _DsMcNetif_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 1),
    _DsMcNetif_Type()
)
dsMcNetif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcNetif.setStatus("mandatory")


class _DsMcT1DLPath_Type(Integer32):
    """Custom type dsMcT1DLPath based on Integer32"""
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49)
        )
    )
    namedValues = NamedValues(
        *(("mcDLPathFdl", 1),
          ("mcDLPathTS1-56", 26),
          ("mcDLPathTS1-64", 2),
          ("mcDLPathTS10-56", 35),
          ("mcDLPathTS10-64", 11),
          ("mcDLPathTS11-56", 36),
          ("mcDLPathTS11-64", 12),
          ("mcDLPathTS12-56", 37),
          ("mcDLPathTS12-64", 13),
          ("mcDLPathTS13-56", 38),
          ("mcDLPathTS13-64", 14),
          ("mcDLPathTS14-56", 39),
          ("mcDLPathTS14-64", 15),
          ("mcDLPathTS15-56", 40),
          ("mcDLPathTS15-64", 16),
          ("mcDLPathTS16-56", 41),
          ("mcDLPathTS16-64", 17),
          ("mcDLPathTS17-56", 42),
          ("mcDLPathTS17-64", 18),
          ("mcDLPathTS18-56", 43),
          ("mcDLPathTS18-64", 19),
          ("mcDLPathTS19-56", 44),
          ("mcDLPathTS19-64", 20),
          ("mcDLPathTS2-56", 27),
          ("mcDLPathTS2-64", 3),
          ("mcDLPathTS20-56", 45),
          ("mcDLPathTS20-64", 21),
          ("mcDLPathTS21-56", 46),
          ("mcDLPathTS21-64", 22),
          ("mcDLPathTS22-56", 47),
          ("mcDLPathTS22-64", 23),
          ("mcDLPathTS23-56", 48),
          ("mcDLPathTS23-64", 24),
          ("mcDLPathTS24-56", 49),
          ("mcDLPathTS24-64", 25),
          ("mcDLPathTS3-56", 28),
          ("mcDLPathTS3-64", 4),
          ("mcDLPathTS4-56", 29),
          ("mcDLPathTS4-64", 5),
          ("mcDLPathTS5-56", 30),
          ("mcDLPathTS5-64", 6),
          ("mcDLPathTS6-56", 31),
          ("mcDLPathTS6-64", 7),
          ("mcDLPathTS7-56", 32),
          ("mcDLPathTS7-64", 8),
          ("mcDLPathTS8-56", 33),
          ("mcDLPathTS8-64", 9),
          ("mcDLPathTS9-56", 34),
          ("mcDLPathTS9-64", 10))
    )


_DsMcT1DLPath_Type.__name__ = "Integer32"
_DsMcT1DLPath_Object = MibScalar
dsMcT1DLPath = _DsMcT1DLPath_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 2),
    _DsMcT1DLPath_Type()
)
dsMcT1DLPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcT1DLPath.setStatus("mandatory")
_DsMcDefRoute_Type = IpAddress
_DsMcDefRoute_Object = MibScalar
dsMcDefRoute = _DsMcDefRoute_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 3),
    _DsMcDefRoute_Type()
)
dsMcDefRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcDefRoute.setStatus("mandatory")
_DsMcCIpAddr_Type = IpAddress
_DsMcCIpAddr_Object = MibScalar
dsMcCIpAddr = _DsMcCIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 4),
    _DsMcCIpAddr_Type()
)
dsMcCIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcCIpAddr.setStatus("mandatory")
_DsMcDIpAddr_Type = IpAddress
_DsMcDIpAddr_Object = MibScalar
dsMcDIpAddr = _DsMcDIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 5),
    _DsMcDIpAddr_Type()
)
dsMcDIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcDIpAddr.setStatus("mandatory")
_DsMcCDIpMask_Type = IpAddress
_DsMcCDIpMask_Object = MibScalar
dsMcCDIpMask = _DsMcCDIpMask_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 6),
    _DsMcCDIpMask_Type()
)
dsMcCDIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcCDIpMask.setStatus("mandatory")
_DsMcEIpAddr_Type = IpAddress
_DsMcEIpAddr_Object = MibScalar
dsMcEIpAddr = _DsMcEIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 7),
    _DsMcEIpAddr_Type()
)
dsMcEIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcEIpAddr.setStatus("mandatory")
_DsMcEIpMask_Type = IpAddress
_DsMcEIpMask_Object = MibScalar
dsMcEIpMask = _DsMcEIpMask_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 8),
    _DsMcEIpMask_Type()
)
dsMcEIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcEIpMask.setStatus("mandatory")
_DsMcIIpAddr_Type = IpAddress
_DsMcIIpAddr_Object = MibScalar
dsMcIIpAddr = _DsMcIIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 9),
    _DsMcIIpAddr_Type()
)
dsMcIIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcIIpAddr.setStatus("mandatory")
_DsMcIIpMask_Type = IpAddress
_DsMcIIpMask_Object = MibScalar
dsMcIIpMask = _DsMcIIpMask_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 10),
    _DsMcIIpMask_Type()
)
dsMcIIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcIIpMask.setStatus("mandatory")
_DsAmc_ObjectIdentity = ObjectIdentity
dsAmc = _DsAmc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11)
)


class _DsAmcAgent_Type(Integer32):
    """Custom type dsAmcAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("amcDisabled", 2),
          ("amcEnabled", 1))
    )


_DsAmcAgent_Type.__name__ = "Integer32"
_DsAmcAgent_Object = MibScalar
dsAmcAgent = _DsAmcAgent_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 1),
    _DsAmcAgent_Type()
)
dsAmcAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcAgent.setStatus("mandatory")


class _DsAmcSourceScreen_Type(Integer32):
    """Custom type dsAmcSourceScreen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mcIpScreen", 1),
          ("mcNoScreen", 2))
    )


_DsAmcSourceScreen_Type.__name__ = "Integer32"
_DsAmcSourceScreen_Object = MibScalar
dsAmcSourceScreen = _DsAmcSourceScreen_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 2),
    _DsAmcSourceScreen_Type()
)
dsAmcSourceScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcSourceScreen.setStatus("mandatory")
_DsAmcTrapTable_Object = MibTable
dsAmcTrapTable = _DsAmcTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 3)
)
if mibBuilder.loadTexts:
    dsAmcTrapTable.setStatus("mandatory")
_DsAmcTrapEntry_Object = MibTableRow
dsAmcTrapEntry = _DsAmcTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 3, 1)
)
dsAmcTrapEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsAmcTrapType"),
)
if mibBuilder.loadTexts:
    dsAmcTrapEntry.setStatus("mandatory")


class _DsAmcTrapType_Type(Integer32):
    """Custom type dsAmcTrapType based on Integer32"""
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
        *(("mcAuthenTraps", 3),
          ("mcEnterpriseTraps", 4),
          ("mcLinkTraps", 2),
          ("mcStartTraps", 1))
    )


_DsAmcTrapType_Type.__name__ = "Integer32"
_DsAmcTrapType_Object = MibTableColumn
dsAmcTrapType = _DsAmcTrapType_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 3, 1, 1),
    _DsAmcTrapType_Type()
)
dsAmcTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAmcTrapType.setStatus("mandatory")


class _DsAmcTrapStatus_Type(Integer32):
    """Custom type dsAmcTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("amcDisabled", 2),
          ("amcEnabled", 1))
    )


_DsAmcTrapStatus_Type.__name__ = "Integer32"
_DsAmcTrapStatus_Object = MibTableColumn
dsAmcTrapStatus = _DsAmcTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 3, 1, 2),
    _DsAmcTrapStatus_Type()
)
dsAmcTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcTrapStatus.setStatus("mandatory")
_DsAmcScrnTable_Object = MibTable
dsAmcScrnTable = _DsAmcScrnTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 4)
)
if mibBuilder.loadTexts:
    dsAmcScrnTable.setStatus("mandatory")
_DsAmcScrnEntry_Object = MibTableRow
dsAmcScrnEntry = _DsAmcScrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 4, 1)
)
dsAmcScrnEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsAmcScrnIndex"),
)
if mibBuilder.loadTexts:
    dsAmcScrnEntry.setStatus("mandatory")


class _DsAmcScrnIndex_Type(Integer32):
    """Custom type dsAmcScrnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DsAmcScrnIndex_Type.__name__ = "Integer32"
_DsAmcScrnIndex_Object = MibTableColumn
dsAmcScrnIndex = _DsAmcScrnIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 4, 1, 1),
    _DsAmcScrnIndex_Type()
)
dsAmcScrnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAmcScrnIndex.setStatus("mandatory")
_DsAmcScrnIpAddr_Type = IpAddress
_DsAmcScrnIpAddr_Object = MibTableColumn
dsAmcScrnIpAddr = _DsAmcScrnIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 4, 1, 2),
    _DsAmcScrnIpAddr_Type()
)
dsAmcScrnIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcScrnIpAddr.setStatus("mandatory")
_DsAmcScrnIpMask_Type = IpAddress
_DsAmcScrnIpMask_Object = MibTableColumn
dsAmcScrnIpMask = _DsAmcScrnIpMask_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 4, 1, 3),
    _DsAmcScrnIpMask_Type()
)
dsAmcScrnIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcScrnIpMask.setStatus("mandatory")
_DsAmcTrapDestTable_Object = MibTable
dsAmcTrapDestTable = _DsAmcTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 5)
)
if mibBuilder.loadTexts:
    dsAmcTrapDestTable.setStatus("mandatory")
_DsAmcTrapDestEntry_Object = MibTableRow
dsAmcTrapDestEntry = _DsAmcTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 5, 1)
)
dsAmcTrapDestEntry.setIndexNames(
    (0, "DATASMART-MIB", "dsAmcTrapDestIndex"),
)
if mibBuilder.loadTexts:
    dsAmcTrapDestEntry.setStatus("mandatory")


class _DsAmcTrapDestIndex_Type(Integer32):
    """Custom type dsAmcTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_DsAmcTrapDestIndex_Type.__name__ = "Integer32"
_DsAmcTrapDestIndex_Object = MibTableColumn
dsAmcTrapDestIndex = _DsAmcTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 5, 1, 1),
    _DsAmcTrapDestIndex_Type()
)
dsAmcTrapDestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsAmcTrapDestIndex.setStatus("mandatory")
_DsAmcTrapDestIpAddr_Type = IpAddress
_DsAmcTrapDestIpAddr_Object = MibTableColumn
dsAmcTrapDestIpAddr = _DsAmcTrapDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 5, 1, 2),
    _DsAmcTrapDestIpAddr_Type()
)
dsAmcTrapDestIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcTrapDestIpAddr.setStatus("mandatory")


class _DsAmcTrapDestVc_Type(Integer32):
    """Custom type dsAmcTrapDestVc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )


_DsAmcTrapDestVc_Type.__name__ = "Integer32"
_DsAmcTrapDestVc_Object = MibTableColumn
dsAmcTrapDestVc = _DsAmcTrapDestVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 5, 1, 3),
    _DsAmcTrapDestVc_Type()
)
dsAmcTrapDestVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcTrapDestVc.setStatus("mandatory")


class _DsAmcTrapDestPort_Type(Integer32):
    """Custom type dsAmcTrapDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("amcDPPort", 2),
          ("amcNIPort", 1))
    )


_DsAmcTrapDestPort_Type.__name__ = "Integer32"
_DsAmcTrapDestPort_Object = MibTableColumn
dsAmcTrapDestPort = _DsAmcTrapDestPort_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 11, 5, 1, 4),
    _DsAmcTrapDestPort_Type()
)
dsAmcTrapDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsAmcTrapDestPort.setStatus("mandatory")
_DsMcIVc_Type = DLCI
_DsMcIVc_Object = MibScalar
dsMcIVc = _DsMcIVc_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 12),
    _DsMcIVc_Type()
)
dsMcIVc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcIVc.setStatus("mandatory")


class _DsMcIPort_Type(Integer32):
    """Custom type dsMcIPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("amcDPPort", 2),
          ("amcNiPort", 1))
    )


_DsMcIPort_Type.__name__ = "Integer32"
_DsMcIPort_Object = MibScalar
dsMcIPort = _DsMcIPort_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 10, 13),
    _DsMcIPort_Type()
)
dsMcIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsMcIPort.setStatus("mandatory")
_DsNc_ObjectIdentity = ObjectIdentity
dsNc = _DsNc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11)
)


class _DsNcFraming_Type(Integer32):
    """Custom type dsNcFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncESF", 2),
          ("ncEricsson", 3),
          ("ncSF", 1))
    )


_DsNcFraming_Type.__name__ = "Integer32"
_DsNcFraming_Object = MibScalar
dsNcFraming = _DsNcFraming_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 1),
    _DsNcFraming_Type()
)
dsNcFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcFraming.setStatus("mandatory")


class _DsNcCoding_Type(Integer32):
    """Custom type dsNcCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncAmi", 1),
          ("ncB8zs", 2))
    )


_DsNcCoding_Type.__name__ = "Integer32"
_DsNcCoding_Object = MibScalar
dsNcCoding = _DsNcCoding_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 2),
    _DsNcCoding_Type()
)
dsNcCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcCoding.setStatus("mandatory")


class _DsNcT1403_Type(Integer32):
    """Custom type dsNcT1403 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncT1403Disable", 2),
          ("ncT1403Enable", 1))
    )


_DsNcT1403_Type.__name__ = "Integer32"
_DsNcT1403_Object = MibScalar
dsNcT1403 = _DsNcT1403_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 3),
    _DsNcT1403_Type()
)
dsNcT1403.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcT1403.setStatus("mandatory")


class _DsNcYellow_Type(Integer32):
    """Custom type dsNcYellow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncYelDisable", 2),
          ("ncYelEnable", 1))
    )


_DsNcYellow_Type.__name__ = "Integer32"
_DsNcYellow_Object = MibScalar
dsNcYellow = _DsNcYellow_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 4),
    _DsNcYellow_Type()
)
dsNcYellow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcYellow.setStatus("mandatory")


class _DsNcAddr54_Type(Integer32):
    """Custom type dsNcAddr54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncAddrBoth", 3),
          ("ncAddrCsu", 1),
          ("ncAddrDsu", 2))
    )


_DsNcAddr54_Type.__name__ = "Integer32"
_DsNcAddr54_Object = MibScalar
dsNcAddr54 = _DsNcAddr54_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 5),
    _DsNcAddr54_Type()
)
dsNcAddr54.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcAddr54.setStatus("mandatory")


class _DsNc54016_Type(Integer32):
    """Custom type dsNc54016 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nc54016Disable", 2),
          ("nc54016Enable", 1))
    )


_DsNc54016_Type.__name__ = "Integer32"
_DsNc54016_Object = MibScalar
dsNc54016 = _DsNc54016_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 6),
    _DsNc54016_Type()
)
dsNc54016.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNc54016.setStatus("mandatory")


class _DsNcLbo_Type(Integer32):
    """Custom type dsNcLbo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ncLbo0", 1),
          ("ncLbo1", 2),
          ("ncLbo2", 3))
    )


_DsNcLbo_Type.__name__ = "Integer32"
_DsNcLbo_Object = MibScalar
dsNcLbo = _DsNcLbo_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 7),
    _DsNcLbo_Type()
)
dsNcLbo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcLbo.setStatus("mandatory")


class _DsNcMF16_Type(Integer32):
    """Custom type dsNcMF16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncMF16Disable", 2),
          ("ncMF16Enable", 1))
    )


_DsNcMF16_Type.__name__ = "Integer32"
_DsNcMF16_Object = MibScalar
dsNcMF16 = _DsNcMF16_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 8),
    _DsNcMF16_Type()
)
dsNcMF16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcMF16.setStatus("mandatory")


class _DsNcCRC_Type(Integer32):
    """Custom type dsNcCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncCrcDisable", 2),
          ("ncCrcEnable", 1))
    )


_DsNcCRC_Type.__name__ = "Integer32"
_DsNcCRC_Object = MibScalar
dsNcCRC = _DsNcCRC_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 9),
    _DsNcCRC_Type()
)
dsNcCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcCRC.setStatus("mandatory")


class _DsNcFasAlign_Type(Integer32):
    """Custom type dsNcFasAlign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncFasWord", 1),
          ("ncNonFasWord", 2))
    )


_DsNcFasAlign_Type.__name__ = "Integer32"
_DsNcFasAlign_Object = MibScalar
dsNcFasAlign = _DsNcFasAlign_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 10),
    _DsNcFasAlign_Type()
)
dsNcFasAlign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcFasAlign.setStatus("mandatory")


class _DsNcE1DLPath_Type(Integer32):
    """Custom type dsNcE1DLPath based on Integer32"""
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
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37)
        )
    )
    namedValues = NamedValues(
        *(("ncSaBit4", 2),
          ("ncSaBit5", 3),
          ("ncSaBit6", 4),
          ("ncSaBit7", 5),
          ("ncSaBit8", 6),
          ("ncSaNone", 1),
          ("ncTS1", 7),
          ("ncTS10", 16),
          ("ncTS11", 17),
          ("ncTS12", 18),
          ("ncTS13", 19),
          ("ncTS14", 20),
          ("ncTS15", 21),
          ("ncTS16", 22),
          ("ncTS17", 23),
          ("ncTS18", 24),
          ("ncTS19", 25),
          ("ncTS2", 8),
          ("ncTS20", 26),
          ("ncTS21", 27),
          ("ncTS22", 28),
          ("ncTS23", 29),
          ("ncTS24", 30),
          ("ncTS25", 31),
          ("ncTS26", 32),
          ("ncTS27", 33),
          ("ncTS28", 34),
          ("ncTS29", 35),
          ("ncTS3", 9),
          ("ncTS30", 36),
          ("ncTS31", 37),
          ("ncTS4", 10),
          ("ncTS5", 11),
          ("ncTS6", 12),
          ("ncTS7", 13),
          ("ncTS8", 14),
          ("ncTS9", 15))
    )


_DsNcE1DLPath_Type.__name__ = "Integer32"
_DsNcE1DLPath_Object = MibScalar
dsNcE1DLPath = _DsNcE1DLPath_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 11),
    _DsNcE1DLPath_Type()
)
dsNcE1DLPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcE1DLPath.setStatus("mandatory")


class _DsNcKA_Type(Integer32):
    """Custom type dsNcKA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncFramedKeepAlive", 1),
          ("ncUnFramedKeepAlive", 2))
    )


_DsNcKA_Type.__name__ = "Integer32"
_DsNcKA_Object = MibScalar
dsNcKA = _DsNcKA_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 12),
    _DsNcKA_Type()
)
dsNcKA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcKA.setStatus("mandatory")


class _DsNcGenRfa_Type(Integer32):
    """Custom type dsNcGenRfa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncGenRfaDisable", 2),
          ("ncGenRfaEnable", 1))
    )


_DsNcGenRfa_Type.__name__ = "Integer32"
_DsNcGenRfa_Object = MibScalar
dsNcGenRfa = _DsNcGenRfa_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 13),
    _DsNcGenRfa_Type()
)
dsNcGenRfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcGenRfa.setStatus("mandatory")


class _DsNcPassTiRfa_Type(Integer32):
    """Custom type dsNcPassTiRfa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ncPassTiRfaDisable", 2),
          ("ncPassTiRfaEnable", 1))
    )


_DsNcPassTiRfa_Type.__name__ = "Integer32"
_DsNcPassTiRfa_Object = MibScalar
dsNcPassTiRfa = _DsNcPassTiRfa_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 14),
    _DsNcPassTiRfa_Type()
)
dsNcPassTiRfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcPassTiRfa.setStatus("mandatory")


class _DsNcIdle_Type(Integer32):
    """Custom type dsNcIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsNcIdle_Type.__name__ = "Integer32"
_DsNcIdle_Object = MibScalar
dsNcIdle = _DsNcIdle_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 15),
    _DsNcIdle_Type()
)
dsNcIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcIdle.setStatus("mandatory")


class _DsNcDdsType_Type(Integer32):
    """Custom type dsNcDdsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scDds56K", 1),
          ("scDds64K", 2))
    )


_DsNcDdsType_Type.__name__ = "Integer32"
_DsNcDdsType_Object = MibScalar
dsNcDdsType = _DsNcDdsType_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 11, 16),
    _DsNcDdsType_Type()
)
dsNcDdsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsNcDdsType.setStatus("mandatory")
_DsSc_ObjectIdentity = ObjectIdentity
dsSc = _DsSc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12)
)


class _DsScMonth_Type(Integer32):
    """Custom type dsScMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DsScMonth_Type.__name__ = "Integer32"
_DsScMonth_Object = MibScalar
dsScMonth = _DsScMonth_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 1),
    _DsScMonth_Type()
)
dsScMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScMonth.setStatus("mandatory")


class _DsScDay_Type(Integer32):
    """Custom type dsScDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DsScDay_Type.__name__ = "Integer32"
_DsScDay_Object = MibScalar
dsScDay = _DsScDay_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 2),
    _DsScDay_Type()
)
dsScDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScDay.setStatus("mandatory")


class _DsScYear_Type(Integer32):
    """Custom type dsScYear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DsScYear_Type.__name__ = "Integer32"
_DsScYear_Object = MibScalar
dsScYear = _DsScYear_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 3),
    _DsScYear_Type()
)
dsScYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScYear.setStatus("mandatory")


class _DsScHour_Type(Integer32):
    """Custom type dsScHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_DsScHour_Type.__name__ = "Integer32"
_DsScHour_Object = MibScalar
dsScHour = _DsScHour_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 4),
    _DsScHour_Type()
)
dsScHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScHour.setStatus("mandatory")


class _DsScMinutes_Type(Integer32):
    """Custom type dsScMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DsScMinutes_Type.__name__ = "Integer32"
_DsScMinutes_Object = MibScalar
dsScMinutes = _DsScMinutes_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 5),
    _DsScMinutes_Type()
)
dsScMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScMinutes.setStatus("mandatory")


class _DsScName_Type(DisplayString):
    """Custom type dsScName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DsScName_Type.__name__ = "DisplayString"
_DsScName_Object = MibScalar
dsScName = _DsScName_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 6),
    _DsScName_Type()
)
dsScName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScName.setStatus("mandatory")


class _DsScSlotAddr_Type(Integer32):
    """Custom type dsScSlotAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DsScSlotAddr_Type.__name__ = "Integer32"
_DsScSlotAddr_Object = MibScalar
dsScSlotAddr = _DsScSlotAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 7),
    _DsScSlotAddr_Type()
)
dsScSlotAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScSlotAddr.setStatus("mandatory")


class _DsScShelfAddr_Type(Integer32):
    """Custom type dsScShelfAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_DsScShelfAddr_Type.__name__ = "Integer32"
_DsScShelfAddr_Object = MibScalar
dsScShelfAddr = _DsScShelfAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 8),
    _DsScShelfAddr_Type()
)
dsScShelfAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScShelfAddr.setStatus("mandatory")


class _DsScGroupAddr_Type(Integer32):
    """Custom type dsScGroupAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsScGroupAddr_Type.__name__ = "Integer32"
_DsScGroupAddr_Object = MibScalar
dsScGroupAddr = _DsScGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 9),
    _DsScGroupAddr_Type()
)
dsScGroupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScGroupAddr.setStatus("mandatory")


class _DsScFrontPanel_Type(Integer32):
    """Custom type dsScFrontPanel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scFpDisable", 2),
          ("scFpEnable", 1))
    )


_DsScFrontPanel_Type.__name__ = "Integer32"
_DsScFrontPanel_Object = MibScalar
dsScFrontPanel = _DsScFrontPanel_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 10),
    _DsScFrontPanel_Type()
)
dsScFrontPanel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScFrontPanel.setStatus("mandatory")


class _DsScDSCompatible_Type(Integer32):
    """Custom type dsScDSCompatible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scDSDisable", 2),
          ("scDSEnable", 1))
    )


_DsScDSCompatible_Type.__name__ = "Integer32"
_DsScDSCompatible_Object = MibScalar
dsScDSCompatible = _DsScDSCompatible_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 11),
    _DsScDSCompatible_Type()
)
dsScDSCompatible.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScDSCompatible.setStatus("mandatory")


class _DsScClockSource_Type(Integer32):
    """Custom type dsScClockSource based on Integer32"""
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
        *(("scDP1Timing", 5),
          ("scDP2Timing", 6),
          ("scInternalTiming", 3),
          ("scLoopTiming", 4),
          ("scTerminalTiming", 1),
          ("scThroughTiming", 2))
    )


_DsScClockSource_Type.__name__ = "Integer32"
_DsScClockSource_Object = MibScalar
dsScClockSource = _DsScClockSource_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 12),
    _DsScClockSource_Type()
)
dsScClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScClockSource.setStatus("mandatory")


class _DsScAutologout_Type(Integer32):
    """Custom type dsScAutologout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_DsScAutologout_Type.__name__ = "Integer32"
_DsScAutologout_Object = MibScalar
dsScAutologout = _DsScAutologout_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 13),
    _DsScAutologout_Type()
)
dsScAutologout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScAutologout.setStatus("mandatory")


class _DsScZeroPerData_Type(Integer32):
    """Custom type dsScZeroPerData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scZallIdle", 1),
          ("scZallStart", 2))
    )


_DsScZeroPerData_Type.__name__ = "Integer32"
_DsScZeroPerData_Object = MibScalar
dsScZeroPerData = _DsScZeroPerData_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 14),
    _DsScZeroPerData_Type()
)
dsScZeroPerData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScZeroPerData.setStatus("mandatory")


class _DsScWyv_Type(DisplayString):
    """Custom type dsScWyv based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsScWyv_Type.__name__ = "DisplayString"
_DsScWyv_Object = MibScalar
dsScWyv = _DsScWyv_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 15),
    _DsScWyv_Type()
)
dsScWyv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsScWyv.setStatus("mandatory")


class _DsScAutoCfg_Type(Integer32):
    """Custom type dsScAutoCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scAcDisable", 2),
          ("scAcEnable", 1))
    )


_DsScAutoCfg_Type.__name__ = "Integer32"
_DsScAutoCfg_Object = MibScalar
dsScAutoCfg = _DsScAutoCfg_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 16),
    _DsScAutoCfg_Type()
)
dsScAutoCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScAutoCfg.setStatus("mandatory")


class _DsScTftpSwdl_Type(DisplayString):
    """Custom type dsScTftpSwdl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DsScTftpSwdl_Type.__name__ = "DisplayString"
_DsScTftpSwdl_Object = MibScalar
dsScTftpSwdl = _DsScTftpSwdl_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 17),
    _DsScTftpSwdl_Type()
)
dsScTftpSwdl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScTftpSwdl.setStatus("mandatory")


class _DsScBoot_Type(Integer32):
    """Custom type dsScBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("scBootActive", 2),
          ("scBootIdle", 1),
          ("scBootInactive", 3))
    )


_DsScBoot_Type.__name__ = "Integer32"
_DsScBoot_Object = MibScalar
dsScBoot = _DsScBoot_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 18),
    _DsScBoot_Type()
)
dsScBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScBoot.setStatus("mandatory")


class _DsScOperMode_Type(Integer32):
    """Custom type dsScOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("scMonitorMode", 2),
          ("scTransparentMode", 1))
    )


_DsScOperMode_Type.__name__ = "Integer32"
_DsScOperMode_Object = MibScalar
dsScOperMode = _DsScOperMode_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 19),
    _DsScOperMode_Type()
)
dsScOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScOperMode.setStatus("mandatory")


class _DsScYearExtention_Type(Integer32):
    """Custom type dsScYearExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1992, 2091),
    )


_DsScYearExtention_Type.__name__ = "Integer32"
_DsScYearExtention_Object = MibScalar
dsScYearExtention = _DsScYearExtention_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 20),
    _DsScYearExtention_Type()
)
dsScYearExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScYearExtention.setStatus("mandatory")


class _DsScMonthExtention_Type(Integer32):
    """Custom type dsScMonthExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DsScMonthExtention_Type.__name__ = "Integer32"
_DsScMonthExtention_Object = MibScalar
dsScMonthExtention = _DsScMonthExtention_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 21),
    _DsScMonthExtention_Type()
)
dsScMonthExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScMonthExtention.setStatus("mandatory")


class _DsScDayExtention_Type(Integer32):
    """Custom type dsScDayExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DsScDayExtention_Type.__name__ = "Integer32"
_DsScDayExtention_Object = MibScalar
dsScDayExtention = _DsScDayExtention_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 22),
    _DsScDayExtention_Type()
)
dsScDayExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScDayExtention.setStatus("mandatory")


class _DsScHourExtention_Type(Integer32):
    """Custom type dsScHourExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_DsScHourExtention_Type.__name__ = "Integer32"
_DsScHourExtention_Object = MibScalar
dsScHourExtention = _DsScHourExtention_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 23),
    _DsScHourExtention_Type()
)
dsScHourExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScHourExtention.setStatus("mandatory")


class _DsScMinExtention_Type(Integer32):
    """Custom type dsScMinExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DsScMinExtention_Type.__name__ = "Integer32"
_DsScMinExtention_Object = MibScalar
dsScMinExtention = _DsScMinExtention_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 24),
    _DsScMinExtention_Type()
)
dsScMinExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScMinExtention.setStatus("mandatory")


class _DsScSecExtention_Type(Integer32):
    """Custom type dsScSecExtention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_DsScSecExtention_Type.__name__ = "Integer32"
_DsScSecExtention_Object = MibScalar
dsScSecExtention = _DsScSecExtention_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 25),
    _DsScSecExtention_Type()
)
dsScSecExtention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsScSecExtention.setStatus("mandatory")


class _DsScPinK_Type(Integer32):
    """Custom type dsScPinK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pinKDisabled", 2),
          ("pinKEnabled", 1))
    )


_DsScPinK_Type.__name__ = "Integer32"
_DsScPinK_Object = MibScalar
dsScPinK = _DsScPinK_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 12, 26),
    _DsScPinK_Type()
)
dsScPinK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsScPinK.setStatus("mandatory")
_DsTc_ObjectIdentity = ObjectIdentity
dsTc = _DsTc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13)
)


class _DsTcFraming_Type(Integer32):
    """Custom type dsTcFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tcESF", 2),
          ("tcEricsson", 3),
          ("tcSF", 1))
    )


_DsTcFraming_Type.__name__ = "Integer32"
_DsTcFraming_Object = MibScalar
dsTcFraming = _DsTcFraming_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 1),
    _DsTcFraming_Type()
)
dsTcFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcFraming.setStatus("mandatory")


class _DsTcCoding_Type(Integer32):
    """Custom type dsTcCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcAmi", 1),
          ("tcB8zs", 2))
    )


_DsTcCoding_Type.__name__ = "Integer32"
_DsTcCoding_Object = MibScalar
dsTcCoding = _DsTcCoding_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 2),
    _DsTcCoding_Type()
)
dsTcCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcCoding.setStatus("mandatory")


class _DsTcIdle_Type(Integer32):
    """Custom type dsTcIdle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DsTcIdle_Type.__name__ = "Integer32"
_DsTcIdle_Object = MibScalar
dsTcIdle = _DsTcIdle_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 3),
    _DsTcIdle_Type()
)
dsTcIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcIdle.setStatus("mandatory")


class _DsTcEqual_Type(Integer32):
    """Custom type dsTcEqual based on Integer32"""
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
        *(("tcTe0", 1),
          ("tcTe1", 2),
          ("tcTe2", 3),
          ("tcTe3", 4),
          ("tcTe4", 5))
    )


_DsTcEqual_Type.__name__ = "Integer32"
_DsTcEqual_Object = MibScalar
dsTcEqual = _DsTcEqual_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 4),
    _DsTcEqual_Type()
)
dsTcEqual.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcEqual.setStatus("mandatory")


class _DsTcMF16_Type(Integer32):
    """Custom type dsTcMF16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcMF16Disable", 2),
          ("tcMF16Enable", 1))
    )


_DsTcMF16_Type.__name__ = "Integer32"
_DsTcMF16_Object = MibScalar
dsTcMF16 = _DsTcMF16_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 5),
    _DsTcMF16_Type()
)
dsTcMF16.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcMF16.setStatus("mandatory")


class _DsTcCRC_Type(Integer32):
    """Custom type dsTcCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcCrcDisable", 2),
          ("tcCrcEnable", 1))
    )


_DsTcCRC_Type.__name__ = "Integer32"
_DsTcCRC_Object = MibScalar
dsTcCRC = _DsTcCRC_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 6),
    _DsTcCRC_Type()
)
dsTcCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcCRC.setStatus("mandatory")


class _DsTcFasAlign_Type(Integer32):
    """Custom type dsTcFasAlign based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcFasWord", 1),
          ("tcNonFasWord", 2))
    )


_DsTcFasAlign_Type.__name__ = "Integer32"
_DsTcFasAlign_Object = MibScalar
dsTcFasAlign = _DsTcFasAlign_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 7),
    _DsTcFasAlign_Type()
)
dsTcFasAlign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcFasAlign.setStatus("mandatory")


class _DsTcAis_Type(Integer32):
    """Custom type dsTcAis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcAisDisable", 2),
          ("tcAisEnable", 1))
    )


_DsTcAis_Type.__name__ = "Integer32"
_DsTcAis_Object = MibScalar
dsTcAis = _DsTcAis_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 8),
    _DsTcAis_Type()
)
dsTcAis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcAis.setStatus("mandatory")


class _DsTcGenRfa_Type(Integer32):
    """Custom type dsTcGenRfa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcGenRfaDisable", 2),
          ("tcGenRfaEnable", 1))
    )


_DsTcGenRfa_Type.__name__ = "Integer32"
_DsTcGenRfa_Object = MibScalar
dsTcGenRfa = _DsTcGenRfa_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 9),
    _DsTcGenRfa_Type()
)
dsTcGenRfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcGenRfa.setStatus("mandatory")


class _DsTcPassTiRfa_Type(Integer32):
    """Custom type dsTcPassTiRfa based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcPassTiRfaDisable", 2),
          ("tcPassTiRfaEnable", 1))
    )


_DsTcPassTiRfa_Type.__name__ = "Integer32"
_DsTcPassTiRfa_Object = MibScalar
dsTcPassTiRfa = _DsTcPassTiRfa_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 13, 10),
    _DsTcPassTiRfa_Type()
)
dsTcPassTiRfa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsTcPassTiRfa.setStatus("mandatory")
_DsFp_ObjectIdentity = ObjectIdentity
dsFp = _DsFp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14)
)
_DsFpFr56_ObjectIdentity = ObjectIdentity
dsFpFr56 = _DsFpFr56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1)
)


class _DsFpFr56PwrLed_Type(Integer32):
    """Custom type dsFpFr56PwrLed based on Integer32"""
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
        *(("fpLedBlinkGreen", 4),
          ("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnGreen", 3))
    )


_DsFpFr56PwrLed_Type.__name__ = "Integer32"
_DsFpFr56PwrLed_Object = MibScalar
dsFpFr56PwrLed = _DsFpFr56PwrLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 1),
    _DsFpFr56PwrLed_Type()
)
dsFpFr56PwrLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56PwrLed.setStatus("mandatory")


class _DsFpFr56DnldFailLed_Type(Integer32):
    """Custom type dsFpFr56DnldFailLed based on Integer32"""
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
        *(("fpLedBlinkRed", 4),
          ("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnRed", 3))
    )


_DsFpFr56DnldFailLed_Type.__name__ = "Integer32"
_DsFpFr56DnldFailLed_Object = MibScalar
dsFpFr56DnldFailLed = _DsFpFr56DnldFailLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 2),
    _DsFpFr56DnldFailLed_Type()
)
dsFpFr56DnldFailLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56DnldFailLed.setStatus("mandatory")


class _DsFpFr56NiAlarmLed_Type(Integer32):
    """Custom type dsFpFr56NiAlarmLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnRed", 3))
    )


_DsFpFr56NiAlarmLed_Type.__name__ = "Integer32"
_DsFpFr56NiAlarmLed_Object = MibScalar
dsFpFr56NiAlarmLed = _DsFpFr56NiAlarmLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 3),
    _DsFpFr56NiAlarmLed_Type()
)
dsFpFr56NiAlarmLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56NiAlarmLed.setStatus("mandatory")


class _DsFpFr56NiDataLed_Type(Integer32):
    """Custom type dsFpFr56NiDataLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnGreen", 3))
    )


_DsFpFr56NiDataLed_Type.__name__ = "Integer32"
_DsFpFr56NiDataLed_Object = MibScalar
dsFpFr56NiDataLed = _DsFpFr56NiDataLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 4),
    _DsFpFr56NiDataLed_Type()
)
dsFpFr56NiDataLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56NiDataLed.setStatus("mandatory")


class _DsFpFr56TestLed_Type(Integer32):
    """Custom type dsFpFr56TestLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnYellow", 3))
    )


_DsFpFr56TestLed_Type.__name__ = "Integer32"
_DsFpFr56TestLed_Object = MibScalar
dsFpFr56TestLed = _DsFpFr56TestLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 5),
    _DsFpFr56TestLed_Type()
)
dsFpFr56TestLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56TestLed.setStatus("mandatory")


class _DsFpFr56DpCtsTxLed_Type(Integer32):
    """Custom type dsFpFr56DpCtsTxLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnYellow", 3))
    )


_DsFpFr56DpCtsTxLed_Type.__name__ = "Integer32"
_DsFpFr56DpCtsTxLed_Object = MibScalar
dsFpFr56DpCtsTxLed = _DsFpFr56DpCtsTxLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 6),
    _DsFpFr56DpCtsTxLed_Type()
)
dsFpFr56DpCtsTxLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56DpCtsTxLed.setStatus("mandatory")


class _DsFpFr56DpRtsRxLed_Type(Integer32):
    """Custom type dsFpFr56DpRtsRxLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnYellow", 3))
    )


_DsFpFr56DpRtsRxLed_Type.__name__ = "Integer32"
_DsFpFr56DpRtsRxLed_Object = MibScalar
dsFpFr56DpRtsRxLed = _DsFpFr56DpRtsRxLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 7),
    _DsFpFr56DpRtsRxLed_Type()
)
dsFpFr56DpRtsRxLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56DpRtsRxLed.setStatus("mandatory")


class _DsFpFr56FrLinkLed_Type(Integer32):
    """Custom type dsFpFr56FrLinkLed based on Integer32"""
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
        *(("fpLedBlinkGreen", 4),
          ("fpLedIndeterminate", 1),
          ("fpLedOff", 2),
          ("fpLedOnGreen", 3))
    )


_DsFpFr56FrLinkLed_Type.__name__ = "Integer32"
_DsFpFr56FrLinkLed_Object = MibScalar
dsFpFr56FrLinkLed = _DsFpFr56FrLinkLed_Object(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 14, 1, 8),
    _DsFpFr56FrLinkLed_Type()
)
dsFpFr56FrLinkLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsFpFr56FrLinkLed.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dsAcOnPowerTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 5005)
)
dsAcOnPowerTransition.setObjects(
    ("DATASMART-MIB", "dsSsPowerStatus")
)
if mibBuilder.loadTexts:
    dsAcOnPowerTransition.setStatus(
        ""
    )

dsAcOffPowerTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 5006)
)
dsAcOffPowerTransition.setObjects(
    ("DATASMART-MIB", "dsSsPowerStatus")
)
if mibBuilder.loadTexts:
    dsAcOffPowerTransition.setStatus(
        ""
    )

dsFmcSetNiRcvUpperBwThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 9001)
)
dsFmcSetNiRcvUpperBwThresh.setObjects(
    ("DATASMART-MIB", "dsRpFrCur15MVc")
)
if mibBuilder.loadTexts:
    dsFmcSetNiRcvUpperBwThresh.setStatus(
        ""
    )

dsFmcClrNiRcvUpperBwThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 9002)
)
dsFmcClrNiRcvUpperBwThresh.setObjects(
    ("DATASMART-MIB", "dsRpFrCur15MVc")
)
if mibBuilder.loadTexts:
    dsFmcClrNiRcvUpperBwThresh.setStatus(
        ""
    )

dsFmcSetNiXmtUpperBwThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 9003)
)
dsFmcSetNiXmtUpperBwThresh.setObjects(
    ("DATASMART-MIB", "dsRpFrCur15MVc")
)
if mibBuilder.loadTexts:
    dsFmcSetNiXmtUpperBwThresh.setStatus(
        ""
    )

dsFmcClrNiXmtUpperBwThresh = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 9004)
)
dsFmcClrNiXmtUpperBwThresh.setObjects(
    ("DATASMART-MIB", "dsRpFrCur15MVc")
)
if mibBuilder.loadTexts:
    dsFmcClrNiXmtUpperBwThresh.setStatus(
        ""
    )

dsFmcFpingLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 9005)
)
dsFmcFpingLinkDown.setObjects(
    ("DATASMART-MIB", "dsRpFrCur15MVc")
)
if mibBuilder.loadTexts:
    dsFmcFpingLinkDown.setStatus(
        ""
    )

dsFmcFpingLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 181, 2, 2, 0, 9006)
)
dsFmcFpingLinkUp.setObjects(
    ("DATASMART-MIB", "dsRpFrCur15MVc")
)
if mibBuilder.loadTexts:
    dsFmcFpingLinkUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DATASMART-MIB",
    **{"DLCI": DLCI,
       "Counter32": Counter32,
       "DisplayString": DisplayString,
       "datasmart": datasmart,
       "dsAcOnPowerTransition": dsAcOnPowerTransition,
       "dsAcOffPowerTransition": dsAcOffPowerTransition,
       "dsFmcSetNiRcvUpperBwThresh": dsFmcSetNiRcvUpperBwThresh,
       "dsFmcClrNiRcvUpperBwThresh": dsFmcClrNiRcvUpperBwThresh,
       "dsFmcSetNiXmtUpperBwThresh": dsFmcSetNiXmtUpperBwThresh,
       "dsFmcClrNiXmtUpperBwThresh": dsFmcClrNiXmtUpperBwThresh,
       "dsFmcFpingLinkDown": dsFmcFpingLinkDown,
       "dsFmcFpingLinkUp": dsFmcFpingLinkUp,
       "dsSs": dsSs,
       "dsSsAlarmSource": dsSsAlarmSource,
       "dsSsAlarmState": dsSsAlarmState,
       "dsSsLoopback": dsSsLoopback,
       "dsSsPowerStatus": dsSsPowerStatus,
       "dsRp": dsRp,
       "dsRpUsr": dsRpUsr,
       "dsRpUsrTmCntTable": dsRpUsrTmCntTable,
       "dsRpUsrTmCntEntry": dsRpUsrTmCntEntry,
       "dsRpUsrTmCntIndex": dsRpUsrTmCntIndex,
       "dsRpUsrTmCntSecs": dsRpUsrTmCntSecs,
       "dsRpUsrTmCnt15Mins": dsRpUsrTmCnt15Mins,
       "dsRpUsrTmCntDays": dsRpUsrTmCntDays,
       "dsRpUsrCurTable": dsRpUsrCurTable,
       "dsRpUsrCurEntry": dsRpUsrCurEntry,
       "dsRpUsrCurIndex": dsRpUsrCurIndex,
       "dsRpUsrCurEE": dsRpUsrCurEE,
       "dsRpUsrCurES": dsRpUsrCurES,
       "dsRpUsrCurBES": dsRpUsrCurBES,
       "dsRpUsrCurSES": dsRpUsrCurSES,
       "dsRpUsrCurUAS": dsRpUsrCurUAS,
       "dsRpUsrCurCSS": dsRpUsrCurCSS,
       "dsRpUsrCurDM": dsRpUsrCurDM,
       "dsRpUsrCurStatus": dsRpUsrCurStatus,
       "dsRpUsrIntvlTable": dsRpUsrIntvlTable,
       "dsRpUsrIntvlEntry": dsRpUsrIntvlEntry,
       "dsRpUsrIntvlIndex": dsRpUsrIntvlIndex,
       "dsRpUsrIntvlNum": dsRpUsrIntvlNum,
       "dsRpUsrIntvlEE": dsRpUsrIntvlEE,
       "dsRpUsrIntvlES": dsRpUsrIntvlES,
       "dsRpUsrIntvlBES": dsRpUsrIntvlBES,
       "dsRpUsrIntvlSES": dsRpUsrIntvlSES,
       "dsRpUsrIntvlUAS": dsRpUsrIntvlUAS,
       "dsRpUsrIntvlCSS": dsRpUsrIntvlCSS,
       "dsRpUsrIntvlDM": dsRpUsrIntvlDM,
       "dsRpUsrIntvlStatus": dsRpUsrIntvlStatus,
       "dsRpUsrTotalTable": dsRpUsrTotalTable,
       "dsRpUsrTotalEntry": dsRpUsrTotalEntry,
       "dsRpUsrTotalIndex": dsRpUsrTotalIndex,
       "dsRpUsrTotalEE": dsRpUsrTotalEE,
       "dsRpUsrTotalES": dsRpUsrTotalES,
       "dsRpUsrTotalBES": dsRpUsrTotalBES,
       "dsRpUsrTotalSES": dsRpUsrTotalSES,
       "dsRpUsrTotalUAS": dsRpUsrTotalUAS,
       "dsRpUsrTotalCSS": dsRpUsrTotalCSS,
       "dsRpUsrTotalDM": dsRpUsrTotalDM,
       "dsRpUsrTotalStatus": dsRpUsrTotalStatus,
       "dsRpUsrDayTable": dsRpUsrDayTable,
       "dsRpUsrDayEntry": dsRpUsrDayEntry,
       "dsRpUsrDayIndex": dsRpUsrDayIndex,
       "dsRpUsrDayNum": dsRpUsrDayNum,
       "dsRpUsrDayEE": dsRpUsrDayEE,
       "dsRpUsrDayES": dsRpUsrDayES,
       "dsRpUsrDayBES": dsRpUsrDayBES,
       "dsRpUsrDaySES": dsRpUsrDaySES,
       "dsRpUsrDayUAS": dsRpUsrDayUAS,
       "dsRpUsrDayCSS": dsRpUsrDayCSS,
       "dsRpUsrDayDM": dsRpUsrDayDM,
       "dsRpUsrDayStatus": dsRpUsrDayStatus,
       "dsRpCar": dsRpCar,
       "dsRpCarCntSecs": dsRpCarCntSecs,
       "dsRpCarCnt15Mins": dsRpCarCnt15Mins,
       "dsRpCarCur": dsRpCarCur,
       "dsRpCarCurEE": dsRpCarCurEE,
       "dsRpCarCurES": dsRpCarCurES,
       "dsRpCarCurBES": dsRpCarCurBES,
       "dsRpCarCurSES": dsRpCarCurSES,
       "dsRpCarCurUAS": dsRpCarCurUAS,
       "dsRpCarCurCSS": dsRpCarCurCSS,
       "dsRpCarCurLOFC": dsRpCarCurLOFC,
       "dsRpCarIntvlTable": dsRpCarIntvlTable,
       "dsRpCarIntvlEntry": dsRpCarIntvlEntry,
       "dsRpCarIntvlNum": dsRpCarIntvlNum,
       "dsRpCarIntvlEE": dsRpCarIntvlEE,
       "dsRpCarIntvlES": dsRpCarIntvlES,
       "dsRpCarIntvlBES": dsRpCarIntvlBES,
       "dsRpCarIntvlSES": dsRpCarIntvlSES,
       "dsRpCarIntvlUAS": dsRpCarIntvlUAS,
       "dsRpCarIntvlCSS": dsRpCarIntvlCSS,
       "dsRpCarIntvlLOFC": dsRpCarIntvlLOFC,
       "dsRpCarTotal": dsRpCarTotal,
       "dsRpCarTotalEE": dsRpCarTotalEE,
       "dsRpCarTotalES": dsRpCarTotalES,
       "dsRpCarTotalBES": dsRpCarTotalBES,
       "dsRpCarTotalSES": dsRpCarTotalSES,
       "dsRpCarTotalUAS": dsRpCarTotalUAS,
       "dsRpCarTotalCSS": dsRpCarTotalCSS,
       "dsRpCarTotalLOFC": dsRpCarTotalLOFC,
       "dsRpStat": dsRpStat,
       "dsRpStTable": dsRpStTable,
       "dsRpStEntry": dsRpStEntry,
       "dsRpStIndex": dsRpStIndex,
       "dsRpStEsfErrors": dsRpStEsfErrors,
       "dsRpStCrcErrors": dsRpStCrcErrors,
       "dsRpStOofErrors": dsRpStOofErrors,
       "dsRpStFrameBitErrors": dsRpStFrameBitErrors,
       "dsRpStBPVs": dsRpStBPVs,
       "dsRpStControlledSlips": dsRpStControlledSlips,
       "dsRpStYellowEvents": dsRpStYellowEvents,
       "dsRpStAISEvents": dsRpStAISEvents,
       "dsRpStLOFEvents": dsRpStLOFEvents,
       "dsRpStLOSEvents": dsRpStLOSEvents,
       "dsRpStFarEndBlkErrors": dsRpStFarEndBlkErrors,
       "dsRpStRemFrameAlmEvts": dsRpStRemFrameAlmEvts,
       "dsRpStRemMFrameAlmEvts": dsRpStRemMFrameAlmEvts,
       "dsRpStLOTS16MFrameEvts": dsRpStLOTS16MFrameEvts,
       "dsRpStZeroCounters": dsRpStZeroCounters,
       "dsRpPl": dsRpPl,
       "dsPlBreak": dsPlBreak,
       "dsPlLen": dsPlLen,
       "dsRpAhrTable": dsRpAhrTable,
       "dsRpAhrEntry": dsRpAhrEntry,
       "dsRpAhrIndex": dsRpAhrIndex,
       "dsRpAhrStr": dsRpAhrStr,
       "dsRpShrTable": dsRpShrTable,
       "dsRpShrEntry": dsRpShrEntry,
       "dsRpShrIndex": dsRpShrIndex,
       "dsRpShrDateTime": dsRpShrDateTime,
       "dsRpShrEventType": dsRpShrEventType,
       "dsRpShrComments": dsRpShrComments,
       "dsRpBes": dsRpBes,
       "dsRpSes": dsRpSes,
       "dsRpDm": dsRpDm,
       "dsRpFr": dsRpFr,
       "dsRpFrTmCntTable": dsRpFrTmCntTable,
       "dsRpFrTmCntEntry": dsRpFrTmCntEntry,
       "dsRpFrTmCntDir": dsRpFrTmCntDir,
       "dsRpFrTmCntSecs": dsRpFrTmCntSecs,
       "dsRpFrTmCnt2Hrs": dsRpFrTmCnt2Hrs,
       "dsRpFrTmCntDays": dsRpFrTmCntDays,
       "dsRpFrPre15MTable": dsRpFrPre15MTable,
       "dsRpFrPre15MEntry": dsRpFrPre15MEntry,
       "dsRpFrPre15MDir": dsRpFrPre15MDir,
       "dsRpFrPre15MVcIndex": dsRpFrPre15MVcIndex,
       "dsRpFrPre15MVc": dsRpFrPre15MVc,
       "dsRpFrPre15MFrames": dsRpFrPre15MFrames,
       "dsRpFrPre15MOctets": dsRpFrPre15MOctets,
       "dsRpFrPre15MKbps": dsRpFrPre15MKbps,
       "dsRpFrPre15MFpMax": dsRpFrPre15MFpMax,
       "dsRpFrPre15MFpAvg": dsRpFrPre15MFpAvg,
       "dsRpFrPre15MFpLost": dsRpFrPre15MFpLost,
       "dsRpFrPre15MFpSent": dsRpFrPre15MFpSent,
       "dsRpFrPre15MStatus": dsRpFrPre15MStatus,
       "dsRpFrCur15MTable": dsRpFrCur15MTable,
       "dsRpFrCur15MEntry": dsRpFrCur15MEntry,
       "dsRpFrCur15MDir": dsRpFrCur15MDir,
       "dsRpFrCur15MVcIndex": dsRpFrCur15MVcIndex,
       "dsRpFrCur15MVc": dsRpFrCur15MVc,
       "dsRpFrCur15MFrames": dsRpFrCur15MFrames,
       "dsRpFrCur15MOctets": dsRpFrCur15MOctets,
       "dsRpFrCur15MKbps": dsRpFrCur15MKbps,
       "dsRpFrCur15MFpMax": dsRpFrCur15MFpMax,
       "dsRpFrCur15MFpAvg": dsRpFrCur15MFpAvg,
       "dsRpFrCur15MFpLost": dsRpFrCur15MFpLost,
       "dsRpFrCur15MFpSent": dsRpFrCur15MFpSent,
       "dsRpFrCur15MFpRmtIp": dsRpFrCur15MFpRmtIp,
       "dsRpFrCur15MFpRmtVc": dsRpFrCur15MFpRmtVc,
       "dsRpFrCur15MStatus": dsRpFrCur15MStatus,
       "dsRpFrCur2HTable": dsRpFrCur2HTable,
       "dsRpFrCur2HEntry": dsRpFrCur2HEntry,
       "dsRpFrCur2HDir": dsRpFrCur2HDir,
       "dsRpFrCur2HVcIndex": dsRpFrCur2HVcIndex,
       "dsRpFrCur2HVc": dsRpFrCur2HVc,
       "dsRpFrCur2HFrames": dsRpFrCur2HFrames,
       "dsRpFrCur2HOctets": dsRpFrCur2HOctets,
       "dsRpFrCur2HKbps": dsRpFrCur2HKbps,
       "dsRpFrCur2HFpMax": dsRpFrCur2HFpMax,
       "dsRpFrCur2HFpAvg": dsRpFrCur2HFpAvg,
       "dsRpFrCur2HFpLost": dsRpFrCur2HFpLost,
       "dsRpFrCur2HFpSent": dsRpFrCur2HFpSent,
       "dsRpFrCur2HStatus": dsRpFrCur2HStatus,
       "dsRpFrIntvl2HTable": dsRpFrIntvl2HTable,
       "dsRpFrIntvl2HEntry": dsRpFrIntvl2HEntry,
       "dsRpFrIntvl2HDir": dsRpFrIntvl2HDir,
       "dsRpFrIntvl2HVcIndex": dsRpFrIntvl2HVcIndex,
       "dsRpFrIntvl2HNum": dsRpFrIntvl2HNum,
       "dsRpFrIntvl2HVc": dsRpFrIntvl2HVc,
       "dsRpFrIntvl2HFrames": dsRpFrIntvl2HFrames,
       "dsRpFrIntvl2HOctets": dsRpFrIntvl2HOctets,
       "dsRpFrIntvl2HKbps": dsRpFrIntvl2HKbps,
       "dsRpFrIntvl2HFpMax": dsRpFrIntvl2HFpMax,
       "dsRpFrIntvl2HFpAvg": dsRpFrIntvl2HFpAvg,
       "dsRpFrIntvl2HFpLost": dsRpFrIntvl2HFpLost,
       "dsRpFrIntvl2HFpSent": dsRpFrIntvl2HFpSent,
       "dsRpFrIntvl2HStatus": dsRpFrIntvl2HStatus,
       "dsRpFrTotalTable": dsRpFrTotalTable,
       "dsRpFrTotalEntry": dsRpFrTotalEntry,
       "dsRpFrTotalDir": dsRpFrTotalDir,
       "dsRpFrTotalVcIndex": dsRpFrTotalVcIndex,
       "dsRpFrTotalVc": dsRpFrTotalVc,
       "dsRpFrTotalFrames": dsRpFrTotalFrames,
       "dsRpFrTotalOctets": dsRpFrTotalOctets,
       "dsRpFrTotalKbps": dsRpFrTotalKbps,
       "dsRpFrTotalFpMax": dsRpFrTotalFpMax,
       "dsRpFrTotalFpAvg": dsRpFrTotalFpAvg,
       "dsRpFrTotalFpLost": dsRpFrTotalFpLost,
       "dsRpFrTotalFpSent": dsRpFrTotalFpSent,
       "dsRpFrTotalStatus": dsRpFrTotalStatus,
       "dsRpFrDayTable": dsRpFrDayTable,
       "dsRpFrDayEntry": dsRpFrDayEntry,
       "dsRpFrDayDir": dsRpFrDayDir,
       "dsRpFrDayVcIndex": dsRpFrDayVcIndex,
       "dsRpFrDayNum": dsRpFrDayNum,
       "dsRpFrDayVc": dsRpFrDayVc,
       "dsRpFrDayFrames": dsRpFrDayFrames,
       "dsRpFrDayOctets": dsRpFrDayOctets,
       "dsRpFrDayKbps": dsRpFrDayKbps,
       "dsRpFrDayFpMax": dsRpFrDayFpMax,
       "dsRpFrDayFpAvg": dsRpFrDayFpAvg,
       "dsRpFrDayFpLost": dsRpFrDayFpLost,
       "dsRpFrDayFpSent": dsRpFrDayFpSent,
       "dsRpFrDayStatus": dsRpFrDayStatus,
       "dsRpFrUrTable": dsRpFrUrTable,
       "dsRpFrUrEntry": dsRpFrUrEntry,
       "dsRpFrUrDir": dsRpFrUrDir,
       "dsRpFrUrVcIndex": dsRpFrUrVcIndex,
       "dsRpFrUrVc": dsRpFrUrVc,
       "dsRpFrUrCIRExceeded": dsRpFrUrCIRExceeded,
       "dsRpFrUrCIRExceededOctets": dsRpFrUrCIRExceededOctets,
       "dsRpFrUrEIRExceeded": dsRpFrUrEIRExceeded,
       "dsRpFrUrEIRExceededOctets": dsRpFrUrEIRExceededOctets,
       "dsRpDdsDuration": dsRpDdsDuration,
       "dsRpDdsTable": dsRpDdsTable,
       "dsRpDdsEntry": dsRpDdsEntry,
       "dsRpDdsIfIndex": dsRpDdsIfIndex,
       "dsRpDdsAvailableSecs": dsRpDdsAvailableSecs,
       "dsRpDdsTotalSecs": dsRpDdsTotalSecs,
       "dsRpDdsBPVs": dsRpDdsBPVs,
       "dsLm": dsLm,
       "dsLmLoopback": dsLmLoopback,
       "dsLmSelfTestState": dsLmSelfTestState,
       "dsLmSelfTestResults": dsLmSelfTestResults,
       "dsRm": dsRm,
       "dsRmLbkCode": dsRmLbkCode,
       "dsRmTestCode": dsRmTestCode,
       "dsRmBertState": dsRmBertState,
       "dsRmBertCode": dsRmBertCode,
       "dsRmBertTestSecs": dsRmBertTestSecs,
       "dsRmBertBitErrors": dsRmBertBitErrors,
       "dsRmBertErrdSecs": dsRmBertErrdSecs,
       "dsRmBertTotalErrors": dsRmBertTotalErrors,
       "dsRmBertReSync": dsRmBertReSync,
       "dsRmFping": dsRmFping,
       "dsRmFpingAction": dsRmFpingAction,
       "dsRmFpingState": dsRmFpingState,
       "dsRmFpingVc": dsRmFpingVc,
       "dsRmFpingFreq": dsRmFpingFreq,
       "dsRmFpingLen": dsRmFpingLen,
       "dsRmFpingCur": dsRmFpingCur,
       "dsRmFpingMin": dsRmFpingMin,
       "dsRmFpingMax": dsRmFpingMax,
       "dsRmFpingAvg": dsRmFpingAvg,
       "dsRmFpingLost": dsRmFpingLost,
       "dsRmFpingTotal": dsRmFpingTotal,
       "dsRmFpingRmtVc": dsRmFpingRmtVc,
       "dsRmFpingRmtIp": dsRmFpingRmtIp,
       "dsRmInsertBitError": dsRmInsertBitError,
       "dsAc": dsAc,
       "dsAcAlmMsg": dsAcAlmMsg,
       "dsAcYelAlm": dsAcYelAlm,
       "dsAcDeact": dsAcDeact,
       "dsAcEst": dsAcEst,
       "dsAcUst": dsAcUst,
       "dsAcSt": dsAcSt,
       "dsAcBerAlm": dsAcBerAlm,
       "dsAcRfaAlm": dsAcRfaAlm,
       "dsAcAisAlm": dsAcAisAlm,
       "dsCc": dsCc,
       "dsCcEcho": dsCcEcho,
       "dsCcControlPort": dsCcControlPort,
       "dsCcBaud": dsCcBaud,
       "dsCcParity": dsCcParity,
       "dsCcDataBits": dsCcDataBits,
       "dsCcStopBits": dsCcStopBits,
       "dsCcDceIn": dsCcDceIn,
       "dsCcDteIn": dsCcDteIn,
       "dsDc": dsDc,
       "dsDcTable": dsDcTable,
       "dsDcEntry": dsDcEntry,
       "dsDcIndex": dsDcIndex,
       "dsDcDataInvert": dsDcDataInvert,
       "dsDcInterface": dsDcInterface,
       "dsDcClockSource": dsDcClockSource,
       "dsDcXmtClkInvert": dsDcXmtClkInvert,
       "dsDcRcvClkInvert": dsDcRcvClkInvert,
       "dsDcIdleChar": dsDcIdleChar,
       "dsDcLOSInput": dsDcLOSInput,
       "dsFc": dsFc,
       "dsFcLoadXcute": dsFcLoadXcute,
       "dsFcTable": dsFcTable,
       "dsFcEntry": dsFcEntry,
       "dsFcTableIndex": dsFcTableIndex,
       "dsFcChanIndex": dsFcChanIndex,
       "dsFcChanMap": dsFcChanMap,
       "dsFcMap16": dsFcMap16,
       "dsFmc": dsFmc,
       "dsFmcFrameType": dsFmcFrameType,
       "dsFmcAddrOctets": dsFmcAddrOctets,
       "dsFmcFcsBits": dsFmcFcsBits,
       "dsFmcUpperBW": dsFmcUpperBW,
       "dsFmcFpingOper": dsFmcFpingOper,
       "dsFmcFpingGen": dsFmcFpingGen,
       "dsFmcFpingThres": dsFmcFpingThres,
       "dsFmcFpingRst": dsFmcFpingRst,
       "dsFmcAddVc": dsFmcAddVc,
       "dsFmcDelVc": dsFmcDelVc,
       "dsMc": dsMc,
       "dsMcNetif": dsMcNetif,
       "dsMcT1DLPath": dsMcT1DLPath,
       "dsMcDefRoute": dsMcDefRoute,
       "dsMcCIpAddr": dsMcCIpAddr,
       "dsMcDIpAddr": dsMcDIpAddr,
       "dsMcCDIpMask": dsMcCDIpMask,
       "dsMcEIpAddr": dsMcEIpAddr,
       "dsMcEIpMask": dsMcEIpMask,
       "dsMcIIpAddr": dsMcIIpAddr,
       "dsMcIIpMask": dsMcIIpMask,
       "dsAmc": dsAmc,
       "dsAmcAgent": dsAmcAgent,
       "dsAmcSourceScreen": dsAmcSourceScreen,
       "dsAmcTrapTable": dsAmcTrapTable,
       "dsAmcTrapEntry": dsAmcTrapEntry,
       "dsAmcTrapType": dsAmcTrapType,
       "dsAmcTrapStatus": dsAmcTrapStatus,
       "dsAmcScrnTable": dsAmcScrnTable,
       "dsAmcScrnEntry": dsAmcScrnEntry,
       "dsAmcScrnIndex": dsAmcScrnIndex,
       "dsAmcScrnIpAddr": dsAmcScrnIpAddr,
       "dsAmcScrnIpMask": dsAmcScrnIpMask,
       "dsAmcTrapDestTable": dsAmcTrapDestTable,
       "dsAmcTrapDestEntry": dsAmcTrapDestEntry,
       "dsAmcTrapDestIndex": dsAmcTrapDestIndex,
       "dsAmcTrapDestIpAddr": dsAmcTrapDestIpAddr,
       "dsAmcTrapDestVc": dsAmcTrapDestVc,
       "dsAmcTrapDestPort": dsAmcTrapDestPort,
       "dsMcIVc": dsMcIVc,
       "dsMcIPort": dsMcIPort,
       "dsNc": dsNc,
       "dsNcFraming": dsNcFraming,
       "dsNcCoding": dsNcCoding,
       "dsNcT1403": dsNcT1403,
       "dsNcYellow": dsNcYellow,
       "dsNcAddr54": dsNcAddr54,
       "dsNc54016": dsNc54016,
       "dsNcLbo": dsNcLbo,
       "dsNcMF16": dsNcMF16,
       "dsNcCRC": dsNcCRC,
       "dsNcFasAlign": dsNcFasAlign,
       "dsNcE1DLPath": dsNcE1DLPath,
       "dsNcKA": dsNcKA,
       "dsNcGenRfa": dsNcGenRfa,
       "dsNcPassTiRfa": dsNcPassTiRfa,
       "dsNcIdle": dsNcIdle,
       "dsNcDdsType": dsNcDdsType,
       "dsSc": dsSc,
       "dsScMonth": dsScMonth,
       "dsScDay": dsScDay,
       "dsScYear": dsScYear,
       "dsScHour": dsScHour,
       "dsScMinutes": dsScMinutes,
       "dsScName": dsScName,
       "dsScSlotAddr": dsScSlotAddr,
       "dsScShelfAddr": dsScShelfAddr,
       "dsScGroupAddr": dsScGroupAddr,
       "dsScFrontPanel": dsScFrontPanel,
       "dsScDSCompatible": dsScDSCompatible,
       "dsScClockSource": dsScClockSource,
       "dsScAutologout": dsScAutologout,
       "dsScZeroPerData": dsScZeroPerData,
       "dsScWyv": dsScWyv,
       "dsScAutoCfg": dsScAutoCfg,
       "dsScTftpSwdl": dsScTftpSwdl,
       "dsScBoot": dsScBoot,
       "dsScOperMode": dsScOperMode,
       "dsScYearExtention": dsScYearExtention,
       "dsScMonthExtention": dsScMonthExtention,
       "dsScDayExtention": dsScDayExtention,
       "dsScHourExtention": dsScHourExtention,
       "dsScMinExtention": dsScMinExtention,
       "dsScSecExtention": dsScSecExtention,
       "dsScPinK": dsScPinK,
       "dsTc": dsTc,
       "dsTcFraming": dsTcFraming,
       "dsTcCoding": dsTcCoding,
       "dsTcIdle": dsTcIdle,
       "dsTcEqual": dsTcEqual,
       "dsTcMF16": dsTcMF16,
       "dsTcCRC": dsTcCRC,
       "dsTcFasAlign": dsTcFasAlign,
       "dsTcAis": dsTcAis,
       "dsTcGenRfa": dsTcGenRfa,
       "dsTcPassTiRfa": dsTcPassTiRfa,
       "dsFp": dsFp,
       "dsFpFr56": dsFpFr56,
       "dsFpFr56PwrLed": dsFpFr56PwrLed,
       "dsFpFr56DnldFailLed": dsFpFr56DnldFailLed,
       "dsFpFr56NiAlarmLed": dsFpFr56NiAlarmLed,
       "dsFpFr56NiDataLed": dsFpFr56NiDataLed,
       "dsFpFr56TestLed": dsFpFr56TestLed,
       "dsFpFr56DpCtsTxLed": dsFpFr56DpCtsTxLed,
       "dsFpFr56DpRtsRxLed": dsFpFr56DpRtsRxLed,
       "dsFpFr56FrLinkLed": dsFpFr56FrLinkLed}
)
