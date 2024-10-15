# SNMP MIB module (HPN-ICF-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-MPLSOAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:12 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfMplsOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfMplsOAMDefectType(Integer32, TextualConvention):
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("dExcess", 6),
          ("dLOCV", 3),
          ("dLspDown", 9),
          ("dME", 10),
          ("dPeerMe", 2),
          ("dRlsnDown", 8),
          ("dServer", 1),
          ("dTTSIMismatch", 4),
          ("dTTSIMismerge", 5),
          ("dUnknown", 7),
          ("noDefect", 11))
    )



class HpnicfMplsOAMDetectFreq(Integer32, TextualConvention):
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
        *(("cv1000ms", 7),
          ("ffd100ms", 4),
          ("ffd10ms", 1),
          ("ffd200ms", 5),
          ("ffd20ms", 2),
          ("ffd500ms", 6),
          ("ffd50ms", 3))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfMplsOamScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfMplsOamScalarGroup = _HpnicfMplsOamScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 1)
)


class _HpnicfMplsOamCapability_Type(TruthValue):
    """Custom type hpnicfMplsOamCapability based on TruthValue"""


_HpnicfMplsOamCapability_Object = MibScalar
hpnicfMplsOamCapability = _HpnicfMplsOamCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 1, 1),
    _HpnicfMplsOamCapability_Type()
)
hpnicfMplsOamCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsOamCapability.setStatus("current")


class _HpnicfMplsOamTrapOpen_Type(TruthValue):
    """Custom type hpnicfMplsOamTrapOpen based on TruthValue"""


_HpnicfMplsOamTrapOpen_Object = MibScalar
hpnicfMplsOamTrapOpen = _HpnicfMplsOamTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 1, 2),
    _HpnicfMplsOamTrapOpen_Type()
)
hpnicfMplsOamTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMplsOamTrapOpen.setStatus("current")
_HpnicfMplsOamTable_ObjectIdentity = ObjectIdentity
hpnicfMplsOamTable = _HpnicfMplsOamTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2)
)
_HpnicfMplsOamIgrTable_Object = MibTable
hpnicfMplsOamIgrTable = _HpnicfMplsOamIgrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrTable.setStatus("current")
_HpnicfMplsOamIgrEntry_Object = MibTableRow
hpnicfMplsOamIgrEntry = _HpnicfMplsOamIgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1)
)
hpnicfMplsOamIgrEntry.setIndexNames(
    (0, "HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamIgrIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrEntry.setStatus("current")
_HpnicfMplsOamIgrIndex_Type = Unsigned32
_HpnicfMplsOamIgrIndex_Object = MibTableColumn
hpnicfMplsOamIgrIndex = _HpnicfMplsOamIgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 1),
    _HpnicfMplsOamIgrIndex_Type()
)
hpnicfMplsOamIgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrIndex.setStatus("current")
_HpnicfMplsOamIgrLspName_Type = OctetString
_HpnicfMplsOamIgrLspName_Object = MibTableColumn
hpnicfMplsOamIgrLspName = _HpnicfMplsOamIgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 2),
    _HpnicfMplsOamIgrLspName_Type()
)
hpnicfMplsOamIgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrLspName.setStatus("current")


class _HpnicfMplsOamIgrDetectType_Type(Integer32):
    """Custom type hpnicfMplsOamIgrDetectType based on Integer32"""
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


_HpnicfMplsOamIgrDetectType_Type.__name__ = "Integer32"
_HpnicfMplsOamIgrDetectType_Object = MibTableColumn
hpnicfMplsOamIgrDetectType = _HpnicfMplsOamIgrDetectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 3),
    _HpnicfMplsOamIgrDetectType_Type()
)
hpnicfMplsOamIgrDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrDetectType.setStatus("current")
_HpnicfMplsOamIgrDetectFreq_Type = HpnicfMplsOAMDetectFreq
_HpnicfMplsOamIgrDetectFreq_Object = MibTableColumn
hpnicfMplsOamIgrDetectFreq = _HpnicfMplsOamIgrDetectFreq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 4),
    _HpnicfMplsOamIgrDetectFreq_Type()
)
hpnicfMplsOamIgrDetectFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrDetectFreq.setStatus("current")


class _HpnicfMplsOamIgrRevType_Type(Integer32):
    """Custom type hpnicfMplsOamIgrRevType based on Integer32"""
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


_HpnicfMplsOamIgrRevType_Type.__name__ = "Integer32"
_HpnicfMplsOamIgrRevType_Object = MibTableColumn
hpnicfMplsOamIgrRevType = _HpnicfMplsOamIgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 5),
    _HpnicfMplsOamIgrRevType_Type()
)
hpnicfMplsOamIgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrRevType.setStatus("current")
_HpnicfMplsOamIgrRevLspName_Type = OctetString
_HpnicfMplsOamIgrRevLspName_Object = MibTableColumn
hpnicfMplsOamIgrRevLspName = _HpnicfMplsOamIgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 6),
    _HpnicfMplsOamIgrRevLspName_Type()
)
hpnicfMplsOamIgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrRevLspName.setStatus("current")
_HpnicfMplsOamIgrLspId_Type = Integer32
_HpnicfMplsOamIgrLspId_Object = MibTableColumn
hpnicfMplsOamIgrLspId = _HpnicfMplsOamIgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 7),
    _HpnicfMplsOamIgrLspId_Type()
)
hpnicfMplsOamIgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrLspId.setStatus("current")


class _HpnicfMplsOamIgrEnable_Type(TruthValue):
    """Custom type hpnicfMplsOamIgrEnable based on TruthValue"""


_HpnicfMplsOamIgrEnable_Object = MibTableColumn
hpnicfMplsOamIgrEnable = _HpnicfMplsOamIgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 8),
    _HpnicfMplsOamIgrEnable_Type()
)
hpnicfMplsOamIgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrEnable.setStatus("current")
_HpnicfMplsOamIgrDefectType_Type = HpnicfMplsOAMDefectType
_HpnicfMplsOamIgrDefectType_Object = MibTableColumn
hpnicfMplsOamIgrDefectType = _HpnicfMplsOamIgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 9),
    _HpnicfMplsOamIgrDefectType_Type()
)
hpnicfMplsOamIgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrDefectType.setStatus("current")
_HpnicfMplsOamIgrRowStatus_Type = RowStatus
_HpnicfMplsOamIgrRowStatus_Object = MibTableColumn
hpnicfMplsOamIgrRowStatus = _HpnicfMplsOamIgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 1, 1, 10),
    _HpnicfMplsOamIgrRowStatus_Type()
)
hpnicfMplsOamIgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrRowStatus.setStatus("current")
_HpnicfMplsOamEgrTable_Object = MibTable
hpnicfMplsOamEgrTable = _HpnicfMplsOamEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrTable.setStatus("current")
_HpnicfMplsOamEgrEntry_Object = MibTableRow
hpnicfMplsOamEgrEntry = _HpnicfMplsOamEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1)
)
hpnicfMplsOamEgrEntry.setIndexNames(
    (0, "HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamEgrIndex"),
)
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrEntry.setStatus("current")
_HpnicfMplsOamEgrIndex_Type = Unsigned32
_HpnicfMplsOamEgrIndex_Object = MibTableColumn
hpnicfMplsOamEgrIndex = _HpnicfMplsOamEgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 1),
    _HpnicfMplsOamEgrIndex_Type()
)
hpnicfMplsOamEgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrIndex.setStatus("current")
_HpnicfMplsOamEgrLspName_Type = OctetString
_HpnicfMplsOamEgrLspName_Object = MibTableColumn
hpnicfMplsOamEgrLspName = _HpnicfMplsOamEgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 2),
    _HpnicfMplsOamEgrLspName_Type()
)
hpnicfMplsOamEgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrLspName.setStatus("current")


class _HpnicfMplsOamEgrDetectType_Type(Integer32):
    """Custom type hpnicfMplsOamEgrDetectType based on Integer32"""
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


_HpnicfMplsOamEgrDetectType_Type.__name__ = "Integer32"
_HpnicfMplsOamEgrDetectType_Object = MibTableColumn
hpnicfMplsOamEgrDetectType = _HpnicfMplsOamEgrDetectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 3),
    _HpnicfMplsOamEgrDetectType_Type()
)
hpnicfMplsOamEgrDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrDetectType.setStatus("current")
_HpnicfMplsOamEgrDetectFreq_Type = HpnicfMplsOAMDetectFreq
_HpnicfMplsOamEgrDetectFreq_Object = MibTableColumn
hpnicfMplsOamEgrDetectFreq = _HpnicfMplsOamEgrDetectFreq_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 4),
    _HpnicfMplsOamEgrDetectFreq_Type()
)
hpnicfMplsOamEgrDetectFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrDetectFreq.setStatus("current")


class _HpnicfMplsOamEgrRevType_Type(Integer32):
    """Custom type hpnicfMplsOamEgrRevType based on Integer32"""
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


_HpnicfMplsOamEgrRevType_Type.__name__ = "Integer32"
_HpnicfMplsOamEgrRevType_Object = MibTableColumn
hpnicfMplsOamEgrRevType = _HpnicfMplsOamEgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 5),
    _HpnicfMplsOamEgrRevType_Type()
)
hpnicfMplsOamEgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrRevType.setStatus("current")
_HpnicfMplsOamEgrRevLspName_Type = OctetString
_HpnicfMplsOamEgrRevLspName_Object = MibTableColumn
hpnicfMplsOamEgrRevLspName = _HpnicfMplsOamEgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 6),
    _HpnicfMplsOamEgrRevLspName_Type()
)
hpnicfMplsOamEgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrRevLspName.setStatus("current")
_HpnicfMplsOamEgrLsrId_Type = IpAddress
_HpnicfMplsOamEgrLsrId_Object = MibTableColumn
hpnicfMplsOamEgrLsrId = _HpnicfMplsOamEgrLsrId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 7),
    _HpnicfMplsOamEgrLsrId_Type()
)
hpnicfMplsOamEgrLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrLsrId.setStatus("current")
_HpnicfMplsOamEgrLspId_Type = Integer32
_HpnicfMplsOamEgrLspId_Object = MibTableColumn
hpnicfMplsOamEgrLspId = _HpnicfMplsOamEgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 8),
    _HpnicfMplsOamEgrLspId_Type()
)
hpnicfMplsOamEgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrLspId.setStatus("current")


class _HpnicfMplsOamEgrEnable_Type(TruthValue):
    """Custom type hpnicfMplsOamEgrEnable based on TruthValue"""


_HpnicfMplsOamEgrEnable_Object = MibTableColumn
hpnicfMplsOamEgrEnable = _HpnicfMplsOamEgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 9),
    _HpnicfMplsOamEgrEnable_Type()
)
hpnicfMplsOamEgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrEnable.setStatus("current")
_HpnicfMplsOamEgrDefectType_Type = HpnicfMplsOAMDefectType
_HpnicfMplsOamEgrDefectType_Object = MibTableColumn
hpnicfMplsOamEgrDefectType = _HpnicfMplsOamEgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 10),
    _HpnicfMplsOamEgrDefectType_Type()
)
hpnicfMplsOamEgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrDefectType.setStatus("current")
_HpnicfMplsOamEgrRowStatus_Type = RowStatus
_HpnicfMplsOamEgrRowStatus_Object = MibTableColumn
hpnicfMplsOamEgrRowStatus = _HpnicfMplsOamEgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 2, 2, 1, 11),
    _HpnicfMplsOamEgrRowStatus_Type()
)
hpnicfMplsOamEgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrRowStatus.setStatus("current")
_HpnicfMplsOamNotifications_ObjectIdentity = ObjectIdentity
hpnicfMplsOamNotifications = _HpnicfMplsOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 3)
)

# Managed Objects groups


# Notification objects

hpnicfMplsOamIgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 3, 1)
)
hpnicfMplsOamIgrLSPOutDefect.setObjects(
      *(("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamIgrLspName"),
        ("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrLSPOutDefect.setStatus(
        "current"
    )

hpnicfMplsOamIgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 3, 2)
)
hpnicfMplsOamIgrLSPInDefect.setObjects(
      *(("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamIgrLspName"),
        ("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hpnicfMplsOamIgrLSPInDefect.setStatus(
        "current"
    )

hpnicfMplsOamEgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 3, 3)
)
hpnicfMplsOamEgrLSPOutDefect.setObjects(
      *(("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamEgrLspName"),
        ("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrLSPOutDefect.setStatus(
        "current"
    )

hpnicfMplsOamEgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 79, 3, 4)
)
hpnicfMplsOamEgrLSPInDefect.setObjects(
      *(("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamEgrLspName"),
        ("HPN-ICF-MPLSOAM-MIB", "hpnicfMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hpnicfMplsOamEgrLSPInDefect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-MPLSOAM-MIB",
    **{"HpnicfMplsOAMDefectType": HpnicfMplsOAMDefectType,
       "HpnicfMplsOAMDetectFreq": HpnicfMplsOAMDetectFreq,
       "hpnicfMplsOam": hpnicfMplsOam,
       "hpnicfMplsOamScalarGroup": hpnicfMplsOamScalarGroup,
       "hpnicfMplsOamCapability": hpnicfMplsOamCapability,
       "hpnicfMplsOamTrapOpen": hpnicfMplsOamTrapOpen,
       "hpnicfMplsOamTable": hpnicfMplsOamTable,
       "hpnicfMplsOamIgrTable": hpnicfMplsOamIgrTable,
       "hpnicfMplsOamIgrEntry": hpnicfMplsOamIgrEntry,
       "hpnicfMplsOamIgrIndex": hpnicfMplsOamIgrIndex,
       "hpnicfMplsOamIgrLspName": hpnicfMplsOamIgrLspName,
       "hpnicfMplsOamIgrDetectType": hpnicfMplsOamIgrDetectType,
       "hpnicfMplsOamIgrDetectFreq": hpnicfMplsOamIgrDetectFreq,
       "hpnicfMplsOamIgrRevType": hpnicfMplsOamIgrRevType,
       "hpnicfMplsOamIgrRevLspName": hpnicfMplsOamIgrRevLspName,
       "hpnicfMplsOamIgrLspId": hpnicfMplsOamIgrLspId,
       "hpnicfMplsOamIgrEnable": hpnicfMplsOamIgrEnable,
       "hpnicfMplsOamIgrDefectType": hpnicfMplsOamIgrDefectType,
       "hpnicfMplsOamIgrRowStatus": hpnicfMplsOamIgrRowStatus,
       "hpnicfMplsOamEgrTable": hpnicfMplsOamEgrTable,
       "hpnicfMplsOamEgrEntry": hpnicfMplsOamEgrEntry,
       "hpnicfMplsOamEgrIndex": hpnicfMplsOamEgrIndex,
       "hpnicfMplsOamEgrLspName": hpnicfMplsOamEgrLspName,
       "hpnicfMplsOamEgrDetectType": hpnicfMplsOamEgrDetectType,
       "hpnicfMplsOamEgrDetectFreq": hpnicfMplsOamEgrDetectFreq,
       "hpnicfMplsOamEgrRevType": hpnicfMplsOamEgrRevType,
       "hpnicfMplsOamEgrRevLspName": hpnicfMplsOamEgrRevLspName,
       "hpnicfMplsOamEgrLsrId": hpnicfMplsOamEgrLsrId,
       "hpnicfMplsOamEgrLspId": hpnicfMplsOamEgrLspId,
       "hpnicfMplsOamEgrEnable": hpnicfMplsOamEgrEnable,
       "hpnicfMplsOamEgrDefectType": hpnicfMplsOamEgrDefectType,
       "hpnicfMplsOamEgrRowStatus": hpnicfMplsOamEgrRowStatus,
       "hpnicfMplsOamNotifications": hpnicfMplsOamNotifications,
       "hpnicfMplsOamIgrLSPOutDefect": hpnicfMplsOamIgrLSPOutDefect,
       "hpnicfMplsOamIgrLSPInDefect": hpnicfMplsOamIgrLSPInDefect,
       "hpnicfMplsOamEgrLSPOutDefect": hpnicfMplsOamEgrLSPOutDefect,
       "hpnicfMplsOamEgrLSPInDefect": hpnicfMplsOamEgrLSPInDefect}
)
