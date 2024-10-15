# SNMP MIB module (HUAWEI-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLSOAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:12 2024
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

(hwMpls,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwMpls")

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

hwMplsOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMplsOamPs_ObjectIdentity = ObjectIdentity
hwMplsOamPs = _HwMplsOamPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1)
)
_HwMplsOamObjects_ObjectIdentity = ObjectIdentity
hwMplsOamObjects = _HwMplsOamObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1)
)


class _HwMplsOamCapability_Type(Unsigned32):
    """Custom type hwMplsOamCapability based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_HwMplsOamCapability_Type.__name__ = "Unsigned32"
_HwMplsOamCapability_Object = MibScalar
hwMplsOamCapability = _HwMplsOamCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 1),
    _HwMplsOamCapability_Type()
)
hwMplsOamCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsOamCapability.setStatus("current")
_HwMplsOamIgrTable_Object = MibTable
hwMplsOamIgrTable = _HwMplsOamIgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwMplsOamIgrTable.setStatus("current")
_HwMplsOamIgrEntry_Object = MibTableRow
hwMplsOamIgrEntry = _HwMplsOamIgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1)
)
hwMplsOamIgrEntry.setIndexNames(
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrIndex"),
)
if mibBuilder.loadTexts:
    hwMplsOamIgrEntry.setStatus("current")
_HwMplsOamIgrIndex_Type = Unsigned32
_HwMplsOamIgrIndex_Object = MibTableColumn
hwMplsOamIgrIndex = _HwMplsOamIgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 1),
    _HwMplsOamIgrIndex_Type()
)
hwMplsOamIgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamIgrIndex.setStatus("current")
_HwMplsOamIgrTunnName_Type = OctetString
_HwMplsOamIgrTunnName_Object = MibTableColumn
hwMplsOamIgrTunnName = _HwMplsOamIgrTunnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 2),
    _HwMplsOamIgrTunnName_Type()
)
hwMplsOamIgrTunnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrTunnName.setStatus("current")


class _HwMplsOamIgrDetType_Type(Integer32):
    """Custom type hwMplsOamIgrDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2))
    )


_HwMplsOamIgrDetType_Type.__name__ = "Integer32"
_HwMplsOamIgrDetType_Object = MibTableColumn
hwMplsOamIgrDetType = _HwMplsOamIgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 3),
    _HwMplsOamIgrDetType_Type()
)
hwMplsOamIgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrDetType.setStatus("current")


class _HwMplsOamIgrDetFreq_Type(Integer32):
    """Custom type hwMplsOamIgrDetFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cv1000ms", 0),
          ("ffd100ms5", 4),
          ("ffd10ms2", 1),
          ("ffd200ms6", 5),
          ("ffd20ms3", 2),
          ("ffd3ms8", 7),
          ("ffd500ms7", 6),
          ("ffd50ms4", 3))
    )


_HwMplsOamIgrDetFreq_Type.__name__ = "Integer32"
_HwMplsOamIgrDetFreq_Object = MibTableColumn
hwMplsOamIgrDetFreq = _HwMplsOamIgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 4),
    _HwMplsOamIgrDetFreq_Type()
)
hwMplsOamIgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrDetFreq.setStatus("current")


class _HwMplsOamIgrRevType_Type(Integer32):
    """Custom type hwMplsOamIgrRevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("private", 1),
          ("share", 2))
    )


_HwMplsOamIgrRevType_Type.__name__ = "Integer32"
_HwMplsOamIgrRevType_Object = MibTableColumn
hwMplsOamIgrRevType = _HwMplsOamIgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 5),
    _HwMplsOamIgrRevType_Type()
)
hwMplsOamIgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrRevType.setStatus("current")
_HwMplsOamIgrRevLspName_Type = OctetString
_HwMplsOamIgrRevLspName_Object = MibTableColumn
hwMplsOamIgrRevLspName = _HwMplsOamIgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 6),
    _HwMplsOamIgrRevLspName_Type()
)
hwMplsOamIgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrRevLspName.setStatus("current")
_HwMplsOamIgrRevLsrId_Type = IpAddress
_HwMplsOamIgrRevLsrId_Object = MibTableColumn
hwMplsOamIgrRevLsrId = _HwMplsOamIgrRevLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 7),
    _HwMplsOamIgrRevLsrId_Type()
)
hwMplsOamIgrRevLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrRevLsrId.setStatus("current")


class _HwMplsOamIgrRevSessTunnId_Type(Integer32):
    """Custom type hwMplsOamIgrRevSessTunnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMplsOamIgrRevSessTunnId_Type.__name__ = "Integer32"
_HwMplsOamIgrRevSessTunnId_Object = MibTableColumn
hwMplsOamIgrRevSessTunnId = _HwMplsOamIgrRevSessTunnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 8),
    _HwMplsOamIgrRevSessTunnId_Type()
)
hwMplsOamIgrRevSessTunnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrRevSessTunnId.setStatus("current")


class _HwMplsOamIgrEnable_Type(Integer32):
    """Custom type hwMplsOamIgrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamIgrEnable_Type.__name__ = "Integer32"
_HwMplsOamIgrEnable_Object = MibTableColumn
hwMplsOamIgrEnable = _HwMplsOamIgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 9),
    _HwMplsOamIgrEnable_Type()
)
hwMplsOamIgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrEnable.setStatus("current")


class _HwMplsOamIgrValid_Type(Integer32):
    """Custom type hwMplsOamIgrValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 0))
    )


_HwMplsOamIgrValid_Type.__name__ = "Integer32"
_HwMplsOamIgrValid_Object = MibTableColumn
hwMplsOamIgrValid = _HwMplsOamIgrValid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 10),
    _HwMplsOamIgrValid_Type()
)
hwMplsOamIgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamIgrValid.setStatus("current")


class _HwMplsOamIgrAvaState_Type(Integer32):
    """Custom type hwMplsOamIgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1))
    )


_HwMplsOamIgrAvaState_Type.__name__ = "Integer32"
_HwMplsOamIgrAvaState_Object = MibTableColumn
hwMplsOamIgrAvaState = _HwMplsOamIgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 11),
    _HwMplsOamIgrAvaState_Type()
)
hwMplsOamIgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamIgrAvaState.setStatus("current")


class _HwMplsOamIgrDefectType_Type(Integer32):
    """Custom type hwMplsOamIgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dExcess", 6),
          ("dIngressDown", 9),
          ("dLOCV", 3),
          ("dOamFail", 8),
          ("dPeerMe", 2),
          ("dServer", 1),
          ("dTTSI-Mismatch", 4),
          ("dTTSI-Mismerge", 5),
          ("dUnknown", 7),
          ("nondefect", 0))
    )


_HwMplsOamIgrDefectType_Type.__name__ = "Integer32"
_HwMplsOamIgrDefectType_Object = MibTableColumn
hwMplsOamIgrDefectType = _HwMplsOamIgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 12),
    _HwMplsOamIgrDefectType_Type()
)
hwMplsOamIgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamIgrDefectType.setStatus("current")
_HwMplsOamIgrRowStatus_Type = RowStatus
_HwMplsOamIgrRowStatus_Object = MibTableColumn
hwMplsOamIgrRowStatus = _HwMplsOamIgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 13),
    _HwMplsOamIgrRowStatus_Type()
)
hwMplsOamIgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrRowStatus.setStatus("current")


class _HwMplsOamIgrCompatibilityMode_Type(Integer32):
    """Custom type hwMplsOamIgrCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptnMode", 1),
          ("routerMode", 2))
    )


_HwMplsOamIgrCompatibilityMode_Type.__name__ = "Integer32"
_HwMplsOamIgrCompatibilityMode_Object = MibTableColumn
hwMplsOamIgrCompatibilityMode = _HwMplsOamIgrCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 14),
    _HwMplsOamIgrCompatibilityMode_Type()
)
hwMplsOamIgrCompatibilityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrCompatibilityMode.setStatus("current")


class _HwMplsOamIgrBDIFreq_Type(Integer32):
    """Custom type hwMplsOamIgrBDIFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detectFrequency", 2),
          ("perSecond", 1))
    )


_HwMplsOamIgrBDIFreq_Type.__name__ = "Integer32"
_HwMplsOamIgrBDIFreq_Object = MibTableColumn
hwMplsOamIgrBDIFreq = _HwMplsOamIgrBDIFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 2, 1, 15),
    _HwMplsOamIgrBDIFreq_Type()
)
hwMplsOamIgrBDIFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamIgrBDIFreq.setStatus("current")
_HwMplsOamEgrTable_Object = MibTable
hwMplsOamEgrTable = _HwMplsOamEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwMplsOamEgrTable.setStatus("current")
_HwMplsOamEgrEntry_Object = MibTableRow
hwMplsOamEgrEntry = _HwMplsOamEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1)
)
hwMplsOamEgrEntry.setIndexNames(
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLspName"),
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLsrId"),
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrSessTunnId"),
)
if mibBuilder.loadTexts:
    hwMplsOamEgrEntry.setStatus("current")
_HwMplsOamEgrLspName_Type = OctetString
_HwMplsOamEgrLspName_Object = MibTableColumn
hwMplsOamEgrLspName = _HwMplsOamEgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 1),
    _HwMplsOamEgrLspName_Type()
)
hwMplsOamEgrLspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamEgrLspName.setStatus("current")
_HwMplsOamEgrLsrId_Type = IpAddress
_HwMplsOamEgrLsrId_Object = MibTableColumn
hwMplsOamEgrLsrId = _HwMplsOamEgrLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 2),
    _HwMplsOamEgrLsrId_Type()
)
hwMplsOamEgrLsrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamEgrLsrId.setStatus("current")


class _HwMplsOamEgrSessTunnId_Type(Integer32):
    """Custom type hwMplsOamEgrSessTunnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMplsOamEgrSessTunnId_Type.__name__ = "Integer32"
_HwMplsOamEgrSessTunnId_Object = MibTableColumn
hwMplsOamEgrSessTunnId = _HwMplsOamEgrSessTunnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 3),
    _HwMplsOamEgrSessTunnId_Type()
)
hwMplsOamEgrSessTunnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamEgrSessTunnId.setStatus("current")


class _HwMplsOamEgrDetType_Type(Integer32):
    """Custom type hwMplsOamEgrDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2),
          ("invalid", 0))
    )


_HwMplsOamEgrDetType_Type.__name__ = "Integer32"
_HwMplsOamEgrDetType_Object = MibTableColumn
hwMplsOamEgrDetType = _HwMplsOamEgrDetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 4),
    _HwMplsOamEgrDetType_Type()
)
hwMplsOamEgrDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrDetType.setStatus("current")


class _HwMplsOamEgrDetFreq_Type(Integer32):
    """Custom type hwMplsOamEgrDetFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cv1000ms", 0),
          ("ffd100ms5", 4),
          ("ffd10ms2", 1),
          ("ffd200ms6", 5),
          ("ffd20ms3", 2),
          ("ffd3ms9", 8),
          ("ffd500ms7", 6),
          ("ffd50ms4", 3),
          ("invalid8", 7))
    )


_HwMplsOamEgrDetFreq_Type.__name__ = "Integer32"
_HwMplsOamEgrDetFreq_Object = MibTableColumn
hwMplsOamEgrDetFreq = _HwMplsOamEgrDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 5),
    _HwMplsOamEgrDetFreq_Type()
)
hwMplsOamEgrDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrDetFreq.setStatus("current")


class _HwMplsOamEgrRevType_Type(Integer32):
    """Custom type hwMplsOamEgrRevType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("private", 1),
          ("share", 2))
    )


_HwMplsOamEgrRevType_Type.__name__ = "Integer32"
_HwMplsOamEgrRevType_Object = MibTableColumn
hwMplsOamEgrRevType = _HwMplsOamEgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 6),
    _HwMplsOamEgrRevType_Type()
)
hwMplsOamEgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrRevType.setStatus("current")
_HwMplsOamEgrRevTunnName_Type = OctetString
_HwMplsOamEgrRevTunnName_Object = MibTableColumn
hwMplsOamEgrRevTunnName = _HwMplsOamEgrRevTunnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 7),
    _HwMplsOamEgrRevTunnName_Type()
)
hwMplsOamEgrRevTunnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrRevTunnName.setStatus("current")


class _HwMplsOamEgrAutoEn_Type(Integer32):
    """Custom type hwMplsOamEgrAutoEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamEgrAutoEn_Type.__name__ = "Integer32"
_HwMplsOamEgrAutoEn_Object = MibTableColumn
hwMplsOamEgrAutoEn = _HwMplsOamEgrAutoEn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 8),
    _HwMplsOamEgrAutoEn_Type()
)
hwMplsOamEgrAutoEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrAutoEn.setStatus("current")


class _HwMplsOamEgrAutoOvertime_Type(Integer32):
    """Custom type hwMplsOamEgrAutoOvertime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMplsOamEgrAutoOvertime_Type.__name__ = "Integer32"
_HwMplsOamEgrAutoOvertime_Object = MibTableColumn
hwMplsOamEgrAutoOvertime = _HwMplsOamEgrAutoOvertime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 9),
    _HwMplsOamEgrAutoOvertime_Type()
)
hwMplsOamEgrAutoOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrAutoOvertime.setStatus("current")


class _HwMplsOamEgrBDIFreq_Type(Integer32):
    """Custom type hwMplsOamEgrBDIFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("detectFrequency", 1),
          ("perSecond", 0))
    )


_HwMplsOamEgrBDIFreq_Type.__name__ = "Integer32"
_HwMplsOamEgrBDIFreq_Object = MibTableColumn
hwMplsOamEgrBDIFreq = _HwMplsOamEgrBDIFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 10),
    _HwMplsOamEgrBDIFreq_Type()
)
hwMplsOamEgrBDIFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrBDIFreq.setStatus("current")


class _HwMplsOamEgrEnable_Type(Integer32):
    """Custom type hwMplsOamEgrEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamEgrEnable_Type.__name__ = "Integer32"
_HwMplsOamEgrEnable_Object = MibTableColumn
hwMplsOamEgrEnable = _HwMplsOamEgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 11),
    _HwMplsOamEgrEnable_Type()
)
hwMplsOamEgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrEnable.setStatus("current")


class _HwMplsOamEgrValid_Type(Integer32):
    """Custom type hwMplsOamEgrValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )


_HwMplsOamEgrValid_Type.__name__ = "Integer32"
_HwMplsOamEgrValid_Object = MibTableColumn
hwMplsOamEgrValid = _HwMplsOamEgrValid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 12),
    _HwMplsOamEgrValid_Type()
)
hwMplsOamEgrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamEgrValid.setStatus("current")


class _HwMplsOamEgrAvaState_Type(Integer32):
    """Custom type hwMplsOamEgrAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1))
    )


_HwMplsOamEgrAvaState_Type.__name__ = "Integer32"
_HwMplsOamEgrAvaState_Object = MibTableColumn
hwMplsOamEgrAvaState = _HwMplsOamEgrAvaState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 13),
    _HwMplsOamEgrAvaState_Type()
)
hwMplsOamEgrAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamEgrAvaState.setStatus("current")


class _HwMplsOamEgrDefectType_Type(Integer32):
    """Custom type hwMplsOamEgrDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dEgressDown", 9),
          ("dExcess", 6),
          ("dLOCV", 3),
          ("dOamFail", 8),
          ("dPeerMe", 2),
          ("dServer", 1),
          ("dTTSI-Mismatch", 4),
          ("dTTSI-Mismerge", 5),
          ("dUnknown", 7),
          ("nondefect", 0))
    )


_HwMplsOamEgrDefectType_Type.__name__ = "Integer32"
_HwMplsOamEgrDefectType_Object = MibTableColumn
hwMplsOamEgrDefectType = _HwMplsOamEgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 14),
    _HwMplsOamEgrDefectType_Type()
)
hwMplsOamEgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamEgrDefectType.setStatus("current")
_HwMplsOamEgrRowStatus_Type = RowStatus
_HwMplsOamEgrRowStatus_Object = MibTableColumn
hwMplsOamEgrRowStatus = _HwMplsOamEgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 3, 1, 15),
    _HwMplsOamEgrRowStatus_Type()
)
hwMplsOamEgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamEgrRowStatus.setStatus("current")
_HwMplsOamRlsnTable_Object = MibTable
hwMplsOamRlsnTable = _HwMplsOamRlsnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwMplsOamRlsnTable.setStatus("current")
_HwMplsOamRlsnEntry_Object = MibTableRow
hwMplsOamRlsnEntry = _HwMplsOamRlsnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1)
)
hwMplsOamRlsnEntry.setIndexNames(
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnLspName"),
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnLsrId"),
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnSessTunnId"),
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnIfIndex"),
)
if mibBuilder.loadTexts:
    hwMplsOamRlsnEntry.setStatus("current")
_HwMplsOamRlsnLspName_Type = OctetString
_HwMplsOamRlsnLspName_Object = MibTableColumn
hwMplsOamRlsnLspName = _HwMplsOamRlsnLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1, 1),
    _HwMplsOamRlsnLspName_Type()
)
hwMplsOamRlsnLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamRlsnLspName.setStatus("current")
_HwMplsOamRlsnLsrId_Type = IpAddress
_HwMplsOamRlsnLsrId_Object = MibTableColumn
hwMplsOamRlsnLsrId = _HwMplsOamRlsnLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1, 2),
    _HwMplsOamRlsnLsrId_Type()
)
hwMplsOamRlsnLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamRlsnLsrId.setStatus("current")


class _HwMplsOamRlsnSessTunnId_Type(Integer32):
    """Custom type hwMplsOamRlsnSessTunnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsOamRlsnSessTunnId_Type.__name__ = "Integer32"
_HwMplsOamRlsnSessTunnId_Object = MibTableColumn
hwMplsOamRlsnSessTunnId = _HwMplsOamRlsnSessTunnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1, 3),
    _HwMplsOamRlsnSessTunnId_Type()
)
hwMplsOamRlsnSessTunnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamRlsnSessTunnId.setStatus("current")
_HwMplsOamRlsnIfIndex_Type = Integer32
_HwMplsOamRlsnIfIndex_Object = MibTableColumn
hwMplsOamRlsnIfIndex = _HwMplsOamRlsnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1, 4),
    _HwMplsOamRlsnIfIndex_Type()
)
hwMplsOamRlsnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamRlsnIfIndex.setStatus("current")
_HwMplsOamRlsnIfName_Type = OctetString
_HwMplsOamRlsnIfName_Object = MibTableColumn
hwMplsOamRlsnIfName = _HwMplsOamRlsnIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1, 5),
    _HwMplsOamRlsnIfName_Type()
)
hwMplsOamRlsnIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamRlsnIfName.setStatus("current")


class _HwMplsOamRlsnIsDown_Type(Integer32):
    """Custom type hwMplsOamRlsnIsDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_HwMplsOamRlsnIsDown_Type.__name__ = "Integer32"
_HwMplsOamRlsnIsDown_Object = MibTableColumn
hwMplsOamRlsnIsDown = _HwMplsOamRlsnIsDown_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1, 6),
    _HwMplsOamRlsnIsDown_Type()
)
hwMplsOamRlsnIsDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamRlsnIsDown.setStatus("current")
_HwMplsOamRlsnRowStatus_Type = RowStatus
_HwMplsOamRlsnRowStatus_Object = MibTableColumn
hwMplsOamRlsnRowStatus = _HwMplsOamRlsnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 4, 1, 7),
    _HwMplsOamRlsnRowStatus_Type()
)
hwMplsOamRlsnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamRlsnRowStatus.setStatus("current")


class _HwMplsOamView_Type(Integer32):
    """Custom type hwMplsOamView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mpls-oam", 1),
          ("null", 0))
    )


_HwMplsOamView_Type.__name__ = "Integer32"
_HwMplsOamView_Object = MibScalar
hwMplsOamView = _HwMplsOamView_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 5),
    _HwMplsOamView_Type()
)
hwMplsOamView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamView.setStatus("current")
_HwMplsOamL2vcTable_Object = MibTable
hwMplsOamL2vcTable = _HwMplsOamL2vcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwMplsOamL2vcTable.setStatus("current")
_HwMplsOamL2vcEntry_Object = MibTableRow
hwMplsOamL2vcEntry = _HwMplsOamL2vcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1)
)
hwMplsOamL2vcEntry.setIndexNames(
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcPeerIp"),
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcType"),
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcId"),
)
if mibBuilder.loadTexts:
    hwMplsOamL2vcEntry.setStatus("current")
_HwMplsOamL2vcPeerIp_Type = IpAddress
_HwMplsOamL2vcPeerIp_Object = MibTableColumn
hwMplsOamL2vcPeerIp = _HwMplsOamL2vcPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 1),
    _HwMplsOamL2vcPeerIp_Type()
)
hwMplsOamL2vcPeerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamL2vcPeerIp.setStatus("current")


class _HwMplsOamL2vcVcType_Type(Integer32):
    """Custom type hwMplsOamL2vcVcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              9,
              10,
              11,
              12,
              13,
              14,
              17,
              18,
              21,
              64)
        )
    )
    namedValues = NamedValues(
        *(("atm-1to1-vcc", 12),
          ("atm-1to1-vpc", 13),
          ("atm-aal5-pdu", 14),
          ("atm-aal5-sdu", 2),
          ("atm-nto1-vcc", 9),
          ("atm-nto1-vpc", 10),
          ("atm-trans-cell", 3),
          ("cesopsn-basic", 21),
          ("ethernet", 5),
          ("fr", 1),
          ("hdlc", 6),
          ("ip-interworking", 64),
          ("ip-layer2", 11),
          ("ppp", 7),
          ("satop-e1", 17),
          ("satop-t1", 18),
          ("unknown", 0),
          ("vlan", 4))
    )


_HwMplsOamL2vcVcType_Type.__name__ = "Integer32"
_HwMplsOamL2vcVcType_Object = MibTableColumn
hwMplsOamL2vcVcType = _HwMplsOamL2vcVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 2),
    _HwMplsOamL2vcVcType_Type()
)
hwMplsOamL2vcVcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamL2vcVcType.setStatus("current")
_HwMplsOamL2vcVcId_Type = Unsigned32
_HwMplsOamL2vcVcId_Object = MibTableColumn
hwMplsOamL2vcVcId = _HwMplsOamL2vcVcId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 3),
    _HwMplsOamL2vcVcId_Type()
)
hwMplsOamL2vcVcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamL2vcVcId.setStatus("current")


class _HwMplsOamL2vcDetType_Type(Integer32):
    """Custom type hwMplsOamL2vcDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2))
    )


_HwMplsOamL2vcDetType_Type.__name__ = "Integer32"
_HwMplsOamL2vcDetType_Object = MibTableColumn
hwMplsOamL2vcDetType = _HwMplsOamL2vcDetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 7),
    _HwMplsOamL2vcDetType_Type()
)
hwMplsOamL2vcDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcDetType.setStatus("current")


class _HwMplsOamL2vcDetFreq_Type(Integer32):
    """Custom type hwMplsOamL2vcDetFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cv1000ms", 0),
          ("ffd100ms5", 4),
          ("ffd10ms2", 1),
          ("ffd200ms6", 5),
          ("ffd20ms3", 2),
          ("ffd3ms8", 7),
          ("ffd500ms7", 6),
          ("ffd50ms4", 3))
    )


_HwMplsOamL2vcDetFreq_Type.__name__ = "Integer32"
_HwMplsOamL2vcDetFreq_Object = MibTableColumn
hwMplsOamL2vcDetFreq = _HwMplsOamL2vcDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 8),
    _HwMplsOamL2vcDetFreq_Type()
)
hwMplsOamL2vcDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcDetFreq.setStatus("current")


class _HwMplsOamL2vcRevDetType_Type(Integer32):
    """Custom type hwMplsOamL2vcRevDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2),
          ("invalid", 0))
    )


_HwMplsOamL2vcRevDetType_Type.__name__ = "Integer32"
_HwMplsOamL2vcRevDetType_Object = MibTableColumn
hwMplsOamL2vcRevDetType = _HwMplsOamL2vcRevDetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 9),
    _HwMplsOamL2vcRevDetType_Type()
)
hwMplsOamL2vcRevDetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamL2vcRevDetType.setStatus("current")


class _HwMplsOamL2vcRevDetFreq_Type(Integer32):
    """Custom type hwMplsOamL2vcRevDetFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cv1000ms", 0),
          ("ffd100ms5", 4),
          ("ffd10ms2", 1),
          ("ffd200ms6", 5),
          ("ffd20ms3", 2),
          ("ffd3ms9", 8),
          ("ffd500ms7", 6),
          ("ffd50ms4", 3),
          ("invalid8", 7))
    )


_HwMplsOamL2vcRevDetFreq_Type.__name__ = "Integer32"
_HwMplsOamL2vcRevDetFreq_Object = MibTableColumn
hwMplsOamL2vcRevDetFreq = _HwMplsOamL2vcRevDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 10),
    _HwMplsOamL2vcRevDetFreq_Type()
)
hwMplsOamL2vcRevDetFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamL2vcRevDetFreq.setStatus("current")


class _HwMplsOamL2vcSendEnable_Type(Integer32):
    """Custom type hwMplsOamL2vcSendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamL2vcSendEnable_Type.__name__ = "Integer32"
_HwMplsOamL2vcSendEnable_Object = MibTableColumn
hwMplsOamL2vcSendEnable = _HwMplsOamL2vcSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 11),
    _HwMplsOamL2vcSendEnable_Type()
)
hwMplsOamL2vcSendEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcSendEnable.setStatus("current")


class _HwMplsOamL2vcReceiveEnable_Type(Integer32):
    """Custom type hwMplsOamL2vcReceiveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamL2vcReceiveEnable_Type.__name__ = "Integer32"
_HwMplsOamL2vcReceiveEnable_Object = MibTableColumn
hwMplsOamL2vcReceiveEnable = _HwMplsOamL2vcReceiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 12),
    _HwMplsOamL2vcReceiveEnable_Type()
)
hwMplsOamL2vcReceiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcReceiveEnable.setStatus("current")


class _HwMplsOamL2vcAutoProlEn_Type(Integer32):
    """Custom type hwMplsOamL2vcAutoProlEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamL2vcAutoProlEn_Type.__name__ = "Integer32"
_HwMplsOamL2vcAutoProlEn_Object = MibTableColumn
hwMplsOamL2vcAutoProlEn = _HwMplsOamL2vcAutoProlEn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 13),
    _HwMplsOamL2vcAutoProlEn_Type()
)
hwMplsOamL2vcAutoProlEn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcAutoProlEn.setStatus("current")


class _HwMplsOamL2vcAutoOvertime_Type(Integer32):
    """Custom type hwMplsOamL2vcAutoOvertime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMplsOamL2vcAutoOvertime_Type.__name__ = "Integer32"
_HwMplsOamL2vcAutoOvertime_Object = MibTableColumn
hwMplsOamL2vcAutoOvertime = _HwMplsOamL2vcAutoOvertime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 14),
    _HwMplsOamL2vcAutoOvertime_Type()
)
hwMplsOamL2vcAutoOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcAutoOvertime.setStatus("current")


class _HwMplsOamL2vcValid_Type(Integer32):
    """Custom type hwMplsOamL2vcValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 3),
          ("start", 2),
          ("stop", 1))
    )


_HwMplsOamL2vcValid_Type.__name__ = "Integer32"
_HwMplsOamL2vcValid_Object = MibTableColumn
hwMplsOamL2vcValid = _HwMplsOamL2vcValid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 15),
    _HwMplsOamL2vcValid_Type()
)
hwMplsOamL2vcValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamL2vcValid.setStatus("current")


class _HwMplsOamL2vcAvaState_Type(Integer32):
    """Custom type hwMplsOamL2vcAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1))
    )


_HwMplsOamL2vcAvaState_Type.__name__ = "Integer32"
_HwMplsOamL2vcAvaState_Object = MibTableColumn
hwMplsOamL2vcAvaState = _HwMplsOamL2vcAvaState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 16),
    _HwMplsOamL2vcAvaState_Type()
)
hwMplsOamL2vcAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamL2vcAvaState.setStatus("current")


class _HwMplsOamL2vcDefectType_Type(Integer32):
    """Custom type hwMplsOamL2vcDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("dExcess", 6),
          ("dLOCV", 3),
          ("dOamFail", 8),
          ("dPeerMe", 2),
          ("dServer", 1),
          ("dTTSI-Mismatch", 4),
          ("dTTSI-Mismerge", 5),
          ("dUnknown", 7),
          ("nondefect", 0),
          ("pw-down", 9))
    )


_HwMplsOamL2vcDefectType_Type.__name__ = "Integer32"
_HwMplsOamL2vcDefectType_Object = MibTableColumn
hwMplsOamL2vcDefectType = _HwMplsOamL2vcDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 17),
    _HwMplsOamL2vcDefectType_Type()
)
hwMplsOamL2vcDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamL2vcDefectType.setStatus("current")


class _HwMplsOamL2vcBdiDefectType_Type(Integer32):
    """Custom type hwMplsOamL2vcBdiDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dExcess", 6),
          ("dLOCV", 3),
          ("dOamFail", 8),
          ("dPeerMe", 2),
          ("dServer", 1),
          ("dTTSI-Mismatch", 4),
          ("dTTSI-Mismerge", 5),
          ("dUnknown", 7),
          ("nondefect", 0))
    )


_HwMplsOamL2vcBdiDefectType_Type.__name__ = "Integer32"
_HwMplsOamL2vcBdiDefectType_Object = MibTableColumn
hwMplsOamL2vcBdiDefectType = _HwMplsOamL2vcBdiDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 18),
    _HwMplsOamL2vcBdiDefectType_Type()
)
hwMplsOamL2vcBdiDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamL2vcBdiDefectType.setStatus("current")
_HwMplsOamL2vcRowStatus_Type = RowStatus
_HwMplsOamL2vcRowStatus_Object = MibTableColumn
hwMplsOamL2vcRowStatus = _HwMplsOamL2vcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 30),
    _HwMplsOamL2vcRowStatus_Type()
)
hwMplsOamL2vcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcRowStatus.setStatus("current")


class _HwMplsOamL2vcCompatibilityMode_Type(Integer32):
    """Custom type hwMplsOamL2vcCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptnMode", 1),
          ("routerMode", 2))
    )


_HwMplsOamL2vcCompatibilityMode_Type.__name__ = "Integer32"
_HwMplsOamL2vcCompatibilityMode_Object = MibTableColumn
hwMplsOamL2vcCompatibilityMode = _HwMplsOamL2vcCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 31),
    _HwMplsOamL2vcCompatibilityMode_Type()
)
hwMplsOamL2vcCompatibilityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcCompatibilityMode.setStatus("current")


class _HwMplsOamL2vcBDIFreq_Type(Integer32):
    """Custom type hwMplsOamL2vcBDIFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detectFrequency", 2),
          ("perSecond", 1))
    )


_HwMplsOamL2vcBDIFreq_Type.__name__ = "Integer32"
_HwMplsOamL2vcBDIFreq_Object = MibTableColumn
hwMplsOamL2vcBDIFreq = _HwMplsOamL2vcBDIFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 6, 1, 32),
    _HwMplsOamL2vcBDIFreq_Type()
)
hwMplsOamL2vcBDIFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamL2vcBDIFreq.setStatus("current")
_HwMplsOamBidirectionalTunnelTable_Object = MibTable
hwMplsOamBidirectionalTunnelTable = _HwMplsOamBidirectionalTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelTable.setStatus("current")
_HwMplsOamBidirectionalTunnelEntry_Object = MibTableRow
hwMplsOamBidirectionalTunnelEntry = _HwMplsOamBidirectionalTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1)
)
hwMplsOamBidirectionalTunnelEntry.setIndexNames(
    (0, "HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelIndex"),
)
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelEntry.setStatus("current")
_HwMplsOamBidirectionalTunnelIndex_Type = Unsigned32
_HwMplsOamBidirectionalTunnelIndex_Object = MibTableColumn
hwMplsOamBidirectionalTunnelIndex = _HwMplsOamBidirectionalTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 1),
    _HwMplsOamBidirectionalTunnelIndex_Type()
)
hwMplsOamBidirectionalTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelIndex.setStatus("current")
_HwMplsOamBidirectionalTunnelTunnName_Type = OctetString
_HwMplsOamBidirectionalTunnelTunnName_Object = MibTableColumn
hwMplsOamBidirectionalTunnelTunnName = _HwMplsOamBidirectionalTunnelTunnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 2),
    _HwMplsOamBidirectionalTunnelTunnName_Type()
)
hwMplsOamBidirectionalTunnelTunnName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelTunnName.setStatus("current")


class _HwMplsOamBidirectionalTunnelDetType_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2))
    )


_HwMplsOamBidirectionalTunnelDetType_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelDetType_Object = MibTableColumn
hwMplsOamBidirectionalTunnelDetType = _HwMplsOamBidirectionalTunnelDetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 3),
    _HwMplsOamBidirectionalTunnelDetType_Type()
)
hwMplsOamBidirectionalTunnelDetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelDetType.setStatus("current")


class _HwMplsOamBidirectionalTunnelDetFreq_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelDetFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cv1000ms", 0),
          ("ffd100ms5", 4),
          ("ffd10ms2", 1),
          ("ffd200ms6", 5),
          ("ffd20ms3", 2),
          ("ffd3ms8", 7),
          ("ffd500ms7", 6),
          ("ffd50ms4", 3))
    )


_HwMplsOamBidirectionalTunnelDetFreq_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelDetFreq_Object = MibTableColumn
hwMplsOamBidirectionalTunnelDetFreq = _HwMplsOamBidirectionalTunnelDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 4),
    _HwMplsOamBidirectionalTunnelDetFreq_Type()
)
hwMplsOamBidirectionalTunnelDetFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelDetFreq.setStatus("current")


class _HwMplsOamBidirectionalTunnelRevDetType_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelRevDetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cv", 1),
          ("ffd", 2),
          ("invalid", 0))
    )


_HwMplsOamBidirectionalTunnelRevDetType_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelRevDetType_Object = MibTableColumn
hwMplsOamBidirectionalTunnelRevDetType = _HwMplsOamBidirectionalTunnelRevDetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 5),
    _HwMplsOamBidirectionalTunnelRevDetType_Type()
)
hwMplsOamBidirectionalTunnelRevDetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelRevDetType.setStatus("current")


class _HwMplsOamBidirectionalTunnelRevDetFreq_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelRevDetFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("cv1000ms", 0),
          ("ffd100ms5", 4),
          ("ffd10ms2", 1),
          ("ffd200ms6", 5),
          ("ffd20ms3", 2),
          ("ffd3ms9", 8),
          ("ffd500ms7", 6),
          ("ffd50ms4", 3),
          ("invalid8", 7))
    )


_HwMplsOamBidirectionalTunnelRevDetFreq_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelRevDetFreq_Object = MibTableColumn
hwMplsOamBidirectionalTunnelRevDetFreq = _HwMplsOamBidirectionalTunnelRevDetFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 6),
    _HwMplsOamBidirectionalTunnelRevDetFreq_Type()
)
hwMplsOamBidirectionalTunnelRevDetFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelRevDetFreq.setStatus("current")


class _HwMplsOamBidirectionalTunnelSendEnable_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelSendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamBidirectionalTunnelSendEnable_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelSendEnable_Object = MibTableColumn
hwMplsOamBidirectionalTunnelSendEnable = _HwMplsOamBidirectionalTunnelSendEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 7),
    _HwMplsOamBidirectionalTunnelSendEnable_Type()
)
hwMplsOamBidirectionalTunnelSendEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelSendEnable.setStatus("current")


class _HwMplsOamBidirectionalTunnelReceiveEnable_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelReceiveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamBidirectionalTunnelReceiveEnable_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelReceiveEnable_Object = MibTableColumn
hwMplsOamBidirectionalTunnelReceiveEnable = _HwMplsOamBidirectionalTunnelReceiveEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 8),
    _HwMplsOamBidirectionalTunnelReceiveEnable_Type()
)
hwMplsOamBidirectionalTunnelReceiveEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelReceiveEnable.setStatus("current")


class _HwMplsOamBidirectionalTunnelAutoProtocolEnable_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelAutoProtocolEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwMplsOamBidirectionalTunnelAutoProtocolEnable_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelAutoProtocolEnable_Object = MibTableColumn
hwMplsOamBidirectionalTunnelAutoProtocolEnable = _HwMplsOamBidirectionalTunnelAutoProtocolEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 9),
    _HwMplsOamBidirectionalTunnelAutoProtocolEnable_Type()
)
hwMplsOamBidirectionalTunnelAutoProtocolEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelAutoProtocolEnable.setStatus("current")


class _HwMplsOamBidirectionalTunnelAutoOvertime_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelAutoOvertime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMplsOamBidirectionalTunnelAutoOvertime_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelAutoOvertime_Object = MibTableColumn
hwMplsOamBidirectionalTunnelAutoOvertime = _HwMplsOamBidirectionalTunnelAutoOvertime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 10),
    _HwMplsOamBidirectionalTunnelAutoOvertime_Type()
)
hwMplsOamBidirectionalTunnelAutoOvertime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelAutoOvertime.setStatus("current")


class _HwMplsOamBidirectionalTunnelValid_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ready", 3),
          ("start", 2),
          ("stop", 1))
    )


_HwMplsOamBidirectionalTunnelValid_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelValid_Object = MibTableColumn
hwMplsOamBidirectionalTunnelValid = _HwMplsOamBidirectionalTunnelValid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 11),
    _HwMplsOamBidirectionalTunnelValid_Type()
)
hwMplsOamBidirectionalTunnelValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelValid.setStatus("current")


class _HwMplsOamBidirectionalTunnelAvaState_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelAvaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("available", 0),
          ("unavailable", 1))
    )


_HwMplsOamBidirectionalTunnelAvaState_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelAvaState_Object = MibTableColumn
hwMplsOamBidirectionalTunnelAvaState = _HwMplsOamBidirectionalTunnelAvaState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 12),
    _HwMplsOamBidirectionalTunnelAvaState_Type()
)
hwMplsOamBidirectionalTunnelAvaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelAvaState.setStatus("current")


class _HwMplsOamBidirectionalTunnelDefectType_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("corouteDown", 9),
          ("dExcess", 6),
          ("dLOCV", 3),
          ("dOamFail", 8),
          ("dPeerMe", 2),
          ("dServer", 1),
          ("dTTSI-Mismatch", 4),
          ("dTTSI-Mismerge", 5),
          ("dUnknown", 7),
          ("nondefect", 0))
    )


_HwMplsOamBidirectionalTunnelDefectType_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelDefectType_Object = MibTableColumn
hwMplsOamBidirectionalTunnelDefectType = _HwMplsOamBidirectionalTunnelDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 13),
    _HwMplsOamBidirectionalTunnelDefectType_Type()
)
hwMplsOamBidirectionalTunnelDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelDefectType.setStatus("current")


class _HwMplsOamBidirectionalTunnelBdiDefectType_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelBdiDefectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dExcess", 6),
          ("dLOCV", 3),
          ("dOamFail", 8),
          ("dPeerMe", 2),
          ("dServer", 1),
          ("dTTSI-Mismatch", 4),
          ("dTTSI-Mismerge", 5),
          ("dUnknown", 7),
          ("nondefect", 0))
    )


_HwMplsOamBidirectionalTunnelBdiDefectType_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelBdiDefectType_Object = MibTableColumn
hwMplsOamBidirectionalTunnelBdiDefectType = _HwMplsOamBidirectionalTunnelBdiDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 14),
    _HwMplsOamBidirectionalTunnelBdiDefectType_Type()
)
hwMplsOamBidirectionalTunnelBdiDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelBdiDefectType.setStatus("current")
_HwMplsOamBidirectionalTunnelRowStatus_Type = RowStatus
_HwMplsOamBidirectionalTunnelRowStatus_Object = MibTableColumn
hwMplsOamBidirectionalTunnelRowStatus = _HwMplsOamBidirectionalTunnelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 15),
    _HwMplsOamBidirectionalTunnelRowStatus_Type()
)
hwMplsOamBidirectionalTunnelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelRowStatus.setStatus("current")


class _HwMplsOamBidirectionalTunnelCompatibilityMode_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ptnMode", 1),
          ("routerMode", 2))
    )


_HwMplsOamBidirectionalTunnelCompatibilityMode_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelCompatibilityMode_Object = MibTableColumn
hwMplsOamBidirectionalTunnelCompatibilityMode = _HwMplsOamBidirectionalTunnelCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 16),
    _HwMplsOamBidirectionalTunnelCompatibilityMode_Type()
)
hwMplsOamBidirectionalTunnelCompatibilityMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelCompatibilityMode.setStatus("current")


class _HwMplsOamBidirectionalTunnelBDIFreq_Type(Integer32):
    """Custom type hwMplsOamBidirectionalTunnelBDIFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detectFrequency", 2),
          ("perSecond", 1))
    )


_HwMplsOamBidirectionalTunnelBDIFreq_Type.__name__ = "Integer32"
_HwMplsOamBidirectionalTunnelBDIFreq_Object = MibTableColumn
hwMplsOamBidirectionalTunnelBDIFreq = _HwMplsOamBidirectionalTunnelBDIFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 7, 1, 17),
    _HwMplsOamBidirectionalTunnelBDIFreq_Type()
)
hwMplsOamBidirectionalTunnelBDIFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelBDIFreq.setStatus("current")


class _HwMplsOamTrapOpen_Type(Unsigned32):
    """Custom type hwMplsOamTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwMplsOamTrapOpen_Type.__name__ = "Unsigned32"
_HwMplsOamTrapOpen_Object = MibScalar
hwMplsOamTrapOpen = _HwMplsOamTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 1, 8),
    _HwMplsOamTrapOpen_Type()
)
hwMplsOamTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMplsOamTrapOpen.setStatus("current")
_HwMplsOamNotifications_ObjectIdentity = ObjectIdentity
hwMplsOamNotifications = _HwMplsOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2)
)

# Managed Objects groups


# Notification objects

hwMplsOamIgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 1)
)
hwMplsOamIgrLSPOutDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrTunnName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamIgrLSPOutDefect.setStatus(
        "current"
    )

hwMplsOamIgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 2)
)
hwMplsOamIgrLSPInDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrTunnName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamIgrLSPInDefect.setStatus(
        "current"
    )

hwMplsOamIgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 3)
)
hwMplsOamIgrLSPAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrTunnName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamIgrLSPAva.setStatus(
        "current"
    )

hwMplsOamIgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 4)
)
hwMplsOamIgrLSPUnAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrTunnName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamIgrLSPUnAva.setStatus(
        "current"
    )

hwMplsOamEgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 5)
)
hwMplsOamEgrLSPOutDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLspName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLsrId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrSessTunnId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamEgrLSPOutDefect.setStatus(
        "current"
    )

hwMplsOamEgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 6)
)
hwMplsOamEgrLSPInDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLspName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLsrId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrSessTunnId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamEgrLSPInDefect.setStatus(
        "current"
    )

hwMplsOamEgrLSPAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 7)
)
hwMplsOamEgrLSPAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLspName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLsrId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrSessTunnId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamEgrLSPAva.setStatus(
        "current"
    )

hwMplsOamEgrLSPUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 8)
)
hwMplsOamEgrLSPUnAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLspName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLsrId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrSessTunnId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamEgrLSPUnAva.setStatus(
        "current"
    )

hwMplsOamEgrFirstPkt = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 9)
)
hwMplsOamEgrFirstPkt.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLspName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLsrId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrSessTunnId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrDetType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrDetFreq"))
)
if mibBuilder.loadTexts:
    hwMplsOamEgrFirstPkt.setStatus(
        "current"
    )

hwMplsOamEgrAutoProFDI = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 10)
)
hwMplsOamEgrAutoProFDI.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLspName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrLsrId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrSessTunnId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamEgrEnable"))
)
if mibBuilder.loadTexts:
    hwMplsOamEgrAutoProFDI.setStatus(
        "current"
    )

hwMplsOamEgrRlsnDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 11)
)
hwMplsOamEgrRlsnDown.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnLspName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnLsrId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnIsDown"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnIfName"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamRlsnSessTunnId"))
)
if mibBuilder.loadTexts:
    hwMplsOamEgrRlsnDown.setStatus(
        "current"
    )

hwMplsOamL2vcOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 12)
)
hwMplsOamL2vcOutDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcPeerIp"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamL2vcOutDefect.setStatus(
        "current"
    )

hwMplsOamL2vcInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 13)
)
hwMplsOamL2vcInDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcPeerIp"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamL2vcInDefect.setStatus(
        "current"
    )

hwMplsOamL2vcAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 14)
)
hwMplsOamL2vcAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcPeerIp"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamL2vcAva.setStatus(
        "current"
    )

hwMplsOamL2vcUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 15)
)
hwMplsOamL2vcUnAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcPeerIp"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcVcId"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamL2vcBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamL2vcUnAva.setStatus(
        "current"
    )

hwMplsOamBidirectionalTunnelOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 16)
)
hwMplsOamBidirectionalTunnelOutDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelOutDefect.setStatus(
        "current"
    )

hwMplsOamBidirectionalTunnelInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 17)
)
hwMplsOamBidirectionalTunnelInDefect.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelInDefect.setStatus(
        "current"
    )

hwMplsOamBidirectionalTunnelAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 18)
)
hwMplsOamBidirectionalTunnelAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelAva.setStatus(
        "current"
    )

hwMplsOamBidirectionalTunnelUnAva = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 2, 19)
)
hwMplsOamBidirectionalTunnelUnAva.setObjects(
      *(("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelIndex"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelAvaState"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelDefectType"),
        ("HUAWEI-MPLSOAM-MIB", "hwMplsOamBidirectionalTunnelBdiDefectType"))
)
if mibBuilder.loadTexts:
    hwMplsOamBidirectionalTunnelUnAva.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLSOAM-MIB",
    **{"hwMplsOam": hwMplsOam,
       "hwMplsOamPs": hwMplsOamPs,
       "hwMplsOamObjects": hwMplsOamObjects,
       "hwMplsOamCapability": hwMplsOamCapability,
       "hwMplsOamIgrTable": hwMplsOamIgrTable,
       "hwMplsOamIgrEntry": hwMplsOamIgrEntry,
       "hwMplsOamIgrIndex": hwMplsOamIgrIndex,
       "hwMplsOamIgrTunnName": hwMplsOamIgrTunnName,
       "hwMplsOamIgrDetType": hwMplsOamIgrDetType,
       "hwMplsOamIgrDetFreq": hwMplsOamIgrDetFreq,
       "hwMplsOamIgrRevType": hwMplsOamIgrRevType,
       "hwMplsOamIgrRevLspName": hwMplsOamIgrRevLspName,
       "hwMplsOamIgrRevLsrId": hwMplsOamIgrRevLsrId,
       "hwMplsOamIgrRevSessTunnId": hwMplsOamIgrRevSessTunnId,
       "hwMplsOamIgrEnable": hwMplsOamIgrEnable,
       "hwMplsOamIgrValid": hwMplsOamIgrValid,
       "hwMplsOamIgrAvaState": hwMplsOamIgrAvaState,
       "hwMplsOamIgrDefectType": hwMplsOamIgrDefectType,
       "hwMplsOamIgrRowStatus": hwMplsOamIgrRowStatus,
       "hwMplsOamIgrCompatibilityMode": hwMplsOamIgrCompatibilityMode,
       "hwMplsOamIgrBDIFreq": hwMplsOamIgrBDIFreq,
       "hwMplsOamEgrTable": hwMplsOamEgrTable,
       "hwMplsOamEgrEntry": hwMplsOamEgrEntry,
       "hwMplsOamEgrLspName": hwMplsOamEgrLspName,
       "hwMplsOamEgrLsrId": hwMplsOamEgrLsrId,
       "hwMplsOamEgrSessTunnId": hwMplsOamEgrSessTunnId,
       "hwMplsOamEgrDetType": hwMplsOamEgrDetType,
       "hwMplsOamEgrDetFreq": hwMplsOamEgrDetFreq,
       "hwMplsOamEgrRevType": hwMplsOamEgrRevType,
       "hwMplsOamEgrRevTunnName": hwMplsOamEgrRevTunnName,
       "hwMplsOamEgrAutoEn": hwMplsOamEgrAutoEn,
       "hwMplsOamEgrAutoOvertime": hwMplsOamEgrAutoOvertime,
       "hwMplsOamEgrBDIFreq": hwMplsOamEgrBDIFreq,
       "hwMplsOamEgrEnable": hwMplsOamEgrEnable,
       "hwMplsOamEgrValid": hwMplsOamEgrValid,
       "hwMplsOamEgrAvaState": hwMplsOamEgrAvaState,
       "hwMplsOamEgrDefectType": hwMplsOamEgrDefectType,
       "hwMplsOamEgrRowStatus": hwMplsOamEgrRowStatus,
       "hwMplsOamRlsnTable": hwMplsOamRlsnTable,
       "hwMplsOamRlsnEntry": hwMplsOamRlsnEntry,
       "hwMplsOamRlsnLspName": hwMplsOamRlsnLspName,
       "hwMplsOamRlsnLsrId": hwMplsOamRlsnLsrId,
       "hwMplsOamRlsnSessTunnId": hwMplsOamRlsnSessTunnId,
       "hwMplsOamRlsnIfIndex": hwMplsOamRlsnIfIndex,
       "hwMplsOamRlsnIfName": hwMplsOamRlsnIfName,
       "hwMplsOamRlsnIsDown": hwMplsOamRlsnIsDown,
       "hwMplsOamRlsnRowStatus": hwMplsOamRlsnRowStatus,
       "hwMplsOamView": hwMplsOamView,
       "hwMplsOamL2vcTable": hwMplsOamL2vcTable,
       "hwMplsOamL2vcEntry": hwMplsOamL2vcEntry,
       "hwMplsOamL2vcPeerIp": hwMplsOamL2vcPeerIp,
       "hwMplsOamL2vcVcType": hwMplsOamL2vcVcType,
       "hwMplsOamL2vcVcId": hwMplsOamL2vcVcId,
       "hwMplsOamL2vcDetType": hwMplsOamL2vcDetType,
       "hwMplsOamL2vcDetFreq": hwMplsOamL2vcDetFreq,
       "hwMplsOamL2vcRevDetType": hwMplsOamL2vcRevDetType,
       "hwMplsOamL2vcRevDetFreq": hwMplsOamL2vcRevDetFreq,
       "hwMplsOamL2vcSendEnable": hwMplsOamL2vcSendEnable,
       "hwMplsOamL2vcReceiveEnable": hwMplsOamL2vcReceiveEnable,
       "hwMplsOamL2vcAutoProlEn": hwMplsOamL2vcAutoProlEn,
       "hwMplsOamL2vcAutoOvertime": hwMplsOamL2vcAutoOvertime,
       "hwMplsOamL2vcValid": hwMplsOamL2vcValid,
       "hwMplsOamL2vcAvaState": hwMplsOamL2vcAvaState,
       "hwMplsOamL2vcDefectType": hwMplsOamL2vcDefectType,
       "hwMplsOamL2vcBdiDefectType": hwMplsOamL2vcBdiDefectType,
       "hwMplsOamL2vcRowStatus": hwMplsOamL2vcRowStatus,
       "hwMplsOamL2vcCompatibilityMode": hwMplsOamL2vcCompatibilityMode,
       "hwMplsOamL2vcBDIFreq": hwMplsOamL2vcBDIFreq,
       "hwMplsOamBidirectionalTunnelTable": hwMplsOamBidirectionalTunnelTable,
       "hwMplsOamBidirectionalTunnelEntry": hwMplsOamBidirectionalTunnelEntry,
       "hwMplsOamBidirectionalTunnelIndex": hwMplsOamBidirectionalTunnelIndex,
       "hwMplsOamBidirectionalTunnelTunnName": hwMplsOamBidirectionalTunnelTunnName,
       "hwMplsOamBidirectionalTunnelDetType": hwMplsOamBidirectionalTunnelDetType,
       "hwMplsOamBidirectionalTunnelDetFreq": hwMplsOamBidirectionalTunnelDetFreq,
       "hwMplsOamBidirectionalTunnelRevDetType": hwMplsOamBidirectionalTunnelRevDetType,
       "hwMplsOamBidirectionalTunnelRevDetFreq": hwMplsOamBidirectionalTunnelRevDetFreq,
       "hwMplsOamBidirectionalTunnelSendEnable": hwMplsOamBidirectionalTunnelSendEnable,
       "hwMplsOamBidirectionalTunnelReceiveEnable": hwMplsOamBidirectionalTunnelReceiveEnable,
       "hwMplsOamBidirectionalTunnelAutoProtocolEnable": hwMplsOamBidirectionalTunnelAutoProtocolEnable,
       "hwMplsOamBidirectionalTunnelAutoOvertime": hwMplsOamBidirectionalTunnelAutoOvertime,
       "hwMplsOamBidirectionalTunnelValid": hwMplsOamBidirectionalTunnelValid,
       "hwMplsOamBidirectionalTunnelAvaState": hwMplsOamBidirectionalTunnelAvaState,
       "hwMplsOamBidirectionalTunnelDefectType": hwMplsOamBidirectionalTunnelDefectType,
       "hwMplsOamBidirectionalTunnelBdiDefectType": hwMplsOamBidirectionalTunnelBdiDefectType,
       "hwMplsOamBidirectionalTunnelRowStatus": hwMplsOamBidirectionalTunnelRowStatus,
       "hwMplsOamBidirectionalTunnelCompatibilityMode": hwMplsOamBidirectionalTunnelCompatibilityMode,
       "hwMplsOamBidirectionalTunnelBDIFreq": hwMplsOamBidirectionalTunnelBDIFreq,
       "hwMplsOamTrapOpen": hwMplsOamTrapOpen,
       "hwMplsOamNotifications": hwMplsOamNotifications,
       "hwMplsOamIgrLSPOutDefect": hwMplsOamIgrLSPOutDefect,
       "hwMplsOamIgrLSPInDefect": hwMplsOamIgrLSPInDefect,
       "hwMplsOamIgrLSPAva": hwMplsOamIgrLSPAva,
       "hwMplsOamIgrLSPUnAva": hwMplsOamIgrLSPUnAva,
       "hwMplsOamEgrLSPOutDefect": hwMplsOamEgrLSPOutDefect,
       "hwMplsOamEgrLSPInDefect": hwMplsOamEgrLSPInDefect,
       "hwMplsOamEgrLSPAva": hwMplsOamEgrLSPAva,
       "hwMplsOamEgrLSPUnAva": hwMplsOamEgrLSPUnAva,
       "hwMplsOamEgrFirstPkt": hwMplsOamEgrFirstPkt,
       "hwMplsOamEgrAutoProFDI": hwMplsOamEgrAutoProFDI,
       "hwMplsOamEgrRlsnDown": hwMplsOamEgrRlsnDown,
       "hwMplsOamL2vcOutDefect": hwMplsOamL2vcOutDefect,
       "hwMplsOamL2vcInDefect": hwMplsOamL2vcInDefect,
       "hwMplsOamL2vcAva": hwMplsOamL2vcAva,
       "hwMplsOamL2vcUnAva": hwMplsOamL2vcUnAva,
       "hwMplsOamBidirectionalTunnelOutDefect": hwMplsOamBidirectionalTunnelOutDefect,
       "hwMplsOamBidirectionalTunnelInDefect": hwMplsOamBidirectionalTunnelInDefect,
       "hwMplsOamBidirectionalTunnelAva": hwMplsOamBidirectionalTunnelAva,
       "hwMplsOamBidirectionalTunnelUnAva": hwMplsOamBidirectionalTunnelUnAva}
)
