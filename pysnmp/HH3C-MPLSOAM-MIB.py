# SNMP MIB module (HH3C-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-MPLSOAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:13 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cMplsOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cMplsOAMDefectType(Integer32, TextualConvention):
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



class Hh3cMplsOAMDetectFreq(Integer32, TextualConvention):
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

_Hh3cMplsOamScalarGroup_ObjectIdentity = ObjectIdentity
hh3cMplsOamScalarGroup = _Hh3cMplsOamScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 1)
)


class _Hh3cMplsOamCapability_Type(TruthValue):
    """Custom type hh3cMplsOamCapability based on TruthValue"""


_Hh3cMplsOamCapability_Object = MibScalar
hh3cMplsOamCapability = _Hh3cMplsOamCapability_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 1, 1),
    _Hh3cMplsOamCapability_Type()
)
hh3cMplsOamCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsOamCapability.setStatus("current")


class _Hh3cMplsOamTrapOpen_Type(TruthValue):
    """Custom type hh3cMplsOamTrapOpen based on TruthValue"""


_Hh3cMplsOamTrapOpen_Object = MibScalar
hh3cMplsOamTrapOpen = _Hh3cMplsOamTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 1, 2),
    _Hh3cMplsOamTrapOpen_Type()
)
hh3cMplsOamTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMplsOamTrapOpen.setStatus("current")
_Hh3cMplsOamTable_ObjectIdentity = ObjectIdentity
hh3cMplsOamTable = _Hh3cMplsOamTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2)
)
_Hh3cMplsOamIgrTable_Object = MibTable
hh3cMplsOamIgrTable = _Hh3cMplsOamIgrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cMplsOamIgrTable.setStatus("current")
_Hh3cMplsOamIgrEntry_Object = MibTableRow
hh3cMplsOamIgrEntry = _Hh3cMplsOamIgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1)
)
hh3cMplsOamIgrEntry.setIndexNames(
    (0, "HH3C-MPLSOAM-MIB", "hh3cMplsOamIgrIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsOamIgrEntry.setStatus("current")
_Hh3cMplsOamIgrIndex_Type = Unsigned32
_Hh3cMplsOamIgrIndex_Object = MibTableColumn
hh3cMplsOamIgrIndex = _Hh3cMplsOamIgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 1),
    _Hh3cMplsOamIgrIndex_Type()
)
hh3cMplsOamIgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrIndex.setStatus("current")
_Hh3cMplsOamIgrLspName_Type = OctetString
_Hh3cMplsOamIgrLspName_Object = MibTableColumn
hh3cMplsOamIgrLspName = _Hh3cMplsOamIgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 2),
    _Hh3cMplsOamIgrLspName_Type()
)
hh3cMplsOamIgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrLspName.setStatus("current")


class _Hh3cMplsOamIgrDetectType_Type(Integer32):
    """Custom type hh3cMplsOamIgrDetectType based on Integer32"""
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


_Hh3cMplsOamIgrDetectType_Type.__name__ = "Integer32"
_Hh3cMplsOamIgrDetectType_Object = MibTableColumn
hh3cMplsOamIgrDetectType = _Hh3cMplsOamIgrDetectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 3),
    _Hh3cMplsOamIgrDetectType_Type()
)
hh3cMplsOamIgrDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrDetectType.setStatus("current")
_Hh3cMplsOamIgrDetectFreq_Type = Hh3cMplsOAMDetectFreq
_Hh3cMplsOamIgrDetectFreq_Object = MibTableColumn
hh3cMplsOamIgrDetectFreq = _Hh3cMplsOamIgrDetectFreq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 4),
    _Hh3cMplsOamIgrDetectFreq_Type()
)
hh3cMplsOamIgrDetectFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrDetectFreq.setStatus("current")


class _Hh3cMplsOamIgrRevType_Type(Integer32):
    """Custom type hh3cMplsOamIgrRevType based on Integer32"""
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


_Hh3cMplsOamIgrRevType_Type.__name__ = "Integer32"
_Hh3cMplsOamIgrRevType_Object = MibTableColumn
hh3cMplsOamIgrRevType = _Hh3cMplsOamIgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 5),
    _Hh3cMplsOamIgrRevType_Type()
)
hh3cMplsOamIgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrRevType.setStatus("current")
_Hh3cMplsOamIgrRevLspName_Type = OctetString
_Hh3cMplsOamIgrRevLspName_Object = MibTableColumn
hh3cMplsOamIgrRevLspName = _Hh3cMplsOamIgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 6),
    _Hh3cMplsOamIgrRevLspName_Type()
)
hh3cMplsOamIgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrRevLspName.setStatus("current")
_Hh3cMplsOamIgrLspId_Type = Integer32
_Hh3cMplsOamIgrLspId_Object = MibTableColumn
hh3cMplsOamIgrLspId = _Hh3cMplsOamIgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 7),
    _Hh3cMplsOamIgrLspId_Type()
)
hh3cMplsOamIgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrLspId.setStatus("current")


class _Hh3cMplsOamIgrEnable_Type(TruthValue):
    """Custom type hh3cMplsOamIgrEnable based on TruthValue"""


_Hh3cMplsOamIgrEnable_Object = MibTableColumn
hh3cMplsOamIgrEnable = _Hh3cMplsOamIgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 8),
    _Hh3cMplsOamIgrEnable_Type()
)
hh3cMplsOamIgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrEnable.setStatus("current")
_Hh3cMplsOamIgrDefectType_Type = Hh3cMplsOAMDefectType
_Hh3cMplsOamIgrDefectType_Object = MibTableColumn
hh3cMplsOamIgrDefectType = _Hh3cMplsOamIgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 9),
    _Hh3cMplsOamIgrDefectType_Type()
)
hh3cMplsOamIgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrDefectType.setStatus("current")
_Hh3cMplsOamIgrRowStatus_Type = RowStatus
_Hh3cMplsOamIgrRowStatus_Object = MibTableColumn
hh3cMplsOamIgrRowStatus = _Hh3cMplsOamIgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 1, 1, 10),
    _Hh3cMplsOamIgrRowStatus_Type()
)
hh3cMplsOamIgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamIgrRowStatus.setStatus("current")
_Hh3cMplsOamEgrTable_Object = MibTable
hh3cMplsOamEgrTable = _Hh3cMplsOamEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cMplsOamEgrTable.setStatus("current")
_Hh3cMplsOamEgrEntry_Object = MibTableRow
hh3cMplsOamEgrEntry = _Hh3cMplsOamEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1)
)
hh3cMplsOamEgrEntry.setIndexNames(
    (0, "HH3C-MPLSOAM-MIB", "hh3cMplsOamEgrIndex"),
)
if mibBuilder.loadTexts:
    hh3cMplsOamEgrEntry.setStatus("current")
_Hh3cMplsOamEgrIndex_Type = Unsigned32
_Hh3cMplsOamEgrIndex_Object = MibTableColumn
hh3cMplsOamEgrIndex = _Hh3cMplsOamEgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 1),
    _Hh3cMplsOamEgrIndex_Type()
)
hh3cMplsOamEgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrIndex.setStatus("current")
_Hh3cMplsOamEgrLspName_Type = OctetString
_Hh3cMplsOamEgrLspName_Object = MibTableColumn
hh3cMplsOamEgrLspName = _Hh3cMplsOamEgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 2),
    _Hh3cMplsOamEgrLspName_Type()
)
hh3cMplsOamEgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrLspName.setStatus("current")


class _Hh3cMplsOamEgrDetectType_Type(Integer32):
    """Custom type hh3cMplsOamEgrDetectType based on Integer32"""
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


_Hh3cMplsOamEgrDetectType_Type.__name__ = "Integer32"
_Hh3cMplsOamEgrDetectType_Object = MibTableColumn
hh3cMplsOamEgrDetectType = _Hh3cMplsOamEgrDetectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 3),
    _Hh3cMplsOamEgrDetectType_Type()
)
hh3cMplsOamEgrDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrDetectType.setStatus("current")
_Hh3cMplsOamEgrDetectFreq_Type = Hh3cMplsOAMDetectFreq
_Hh3cMplsOamEgrDetectFreq_Object = MibTableColumn
hh3cMplsOamEgrDetectFreq = _Hh3cMplsOamEgrDetectFreq_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 4),
    _Hh3cMplsOamEgrDetectFreq_Type()
)
hh3cMplsOamEgrDetectFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrDetectFreq.setStatus("current")


class _Hh3cMplsOamEgrRevType_Type(Integer32):
    """Custom type hh3cMplsOamEgrRevType based on Integer32"""
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


_Hh3cMplsOamEgrRevType_Type.__name__ = "Integer32"
_Hh3cMplsOamEgrRevType_Object = MibTableColumn
hh3cMplsOamEgrRevType = _Hh3cMplsOamEgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 5),
    _Hh3cMplsOamEgrRevType_Type()
)
hh3cMplsOamEgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrRevType.setStatus("current")
_Hh3cMplsOamEgrRevLspName_Type = OctetString
_Hh3cMplsOamEgrRevLspName_Object = MibTableColumn
hh3cMplsOamEgrRevLspName = _Hh3cMplsOamEgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 6),
    _Hh3cMplsOamEgrRevLspName_Type()
)
hh3cMplsOamEgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrRevLspName.setStatus("current")
_Hh3cMplsOamEgrLsrId_Type = IpAddress
_Hh3cMplsOamEgrLsrId_Object = MibTableColumn
hh3cMplsOamEgrLsrId = _Hh3cMplsOamEgrLsrId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 7),
    _Hh3cMplsOamEgrLsrId_Type()
)
hh3cMplsOamEgrLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrLsrId.setStatus("current")
_Hh3cMplsOamEgrLspId_Type = Integer32
_Hh3cMplsOamEgrLspId_Object = MibTableColumn
hh3cMplsOamEgrLspId = _Hh3cMplsOamEgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 8),
    _Hh3cMplsOamEgrLspId_Type()
)
hh3cMplsOamEgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrLspId.setStatus("current")


class _Hh3cMplsOamEgrEnable_Type(TruthValue):
    """Custom type hh3cMplsOamEgrEnable based on TruthValue"""


_Hh3cMplsOamEgrEnable_Object = MibTableColumn
hh3cMplsOamEgrEnable = _Hh3cMplsOamEgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 9),
    _Hh3cMplsOamEgrEnable_Type()
)
hh3cMplsOamEgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrEnable.setStatus("current")
_Hh3cMplsOamEgrDefectType_Type = Hh3cMplsOAMDefectType
_Hh3cMplsOamEgrDefectType_Object = MibTableColumn
hh3cMplsOamEgrDefectType = _Hh3cMplsOamEgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 10),
    _Hh3cMplsOamEgrDefectType_Type()
)
hh3cMplsOamEgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrDefectType.setStatus("current")
_Hh3cMplsOamEgrRowStatus_Type = RowStatus
_Hh3cMplsOamEgrRowStatus_Object = MibTableColumn
hh3cMplsOamEgrRowStatus = _Hh3cMplsOamEgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 2, 2, 1, 11),
    _Hh3cMplsOamEgrRowStatus_Type()
)
hh3cMplsOamEgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cMplsOamEgrRowStatus.setStatus("current")
_Hh3cMplsOamNotifications_ObjectIdentity = ObjectIdentity
hh3cMplsOamNotifications = _Hh3cMplsOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 3)
)

# Managed Objects groups


# Notification objects

hh3cMplsOamIgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 3, 1)
)
hh3cMplsOamIgrLSPOutDefect.setObjects(
      *(("HH3C-MPLSOAM-MIB", "hh3cMplsOamIgrLspName"),
        ("HH3C-MPLSOAM-MIB", "hh3cMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hh3cMplsOamIgrLSPOutDefect.setStatus(
        "current"
    )

hh3cMplsOamIgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 3, 2)
)
hh3cMplsOamIgrLSPInDefect.setObjects(
      *(("HH3C-MPLSOAM-MIB", "hh3cMplsOamIgrLspName"),
        ("HH3C-MPLSOAM-MIB", "hh3cMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    hh3cMplsOamIgrLSPInDefect.setStatus(
        "current"
    )

hh3cMplsOamEgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 3, 3)
)
hh3cMplsOamEgrLSPOutDefect.setObjects(
      *(("HH3C-MPLSOAM-MIB", "hh3cMplsOamEgrLspName"),
        ("HH3C-MPLSOAM-MIB", "hh3cMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hh3cMplsOamEgrLSPOutDefect.setStatus(
        "current"
    )

hh3cMplsOamEgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 2, 79, 3, 4)
)
hh3cMplsOamEgrLSPInDefect.setObjects(
      *(("HH3C-MPLSOAM-MIB", "hh3cMplsOamEgrLspName"),
        ("HH3C-MPLSOAM-MIB", "hh3cMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    hh3cMplsOamEgrLSPInDefect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-MPLSOAM-MIB",
    **{"Hh3cMplsOAMDefectType": Hh3cMplsOAMDefectType,
       "Hh3cMplsOAMDetectFreq": Hh3cMplsOAMDetectFreq,
       "hh3cMplsOam": hh3cMplsOam,
       "hh3cMplsOamScalarGroup": hh3cMplsOamScalarGroup,
       "hh3cMplsOamCapability": hh3cMplsOamCapability,
       "hh3cMplsOamTrapOpen": hh3cMplsOamTrapOpen,
       "hh3cMplsOamTable": hh3cMplsOamTable,
       "hh3cMplsOamIgrTable": hh3cMplsOamIgrTable,
       "hh3cMplsOamIgrEntry": hh3cMplsOamIgrEntry,
       "hh3cMplsOamIgrIndex": hh3cMplsOamIgrIndex,
       "hh3cMplsOamIgrLspName": hh3cMplsOamIgrLspName,
       "hh3cMplsOamIgrDetectType": hh3cMplsOamIgrDetectType,
       "hh3cMplsOamIgrDetectFreq": hh3cMplsOamIgrDetectFreq,
       "hh3cMplsOamIgrRevType": hh3cMplsOamIgrRevType,
       "hh3cMplsOamIgrRevLspName": hh3cMplsOamIgrRevLspName,
       "hh3cMplsOamIgrLspId": hh3cMplsOamIgrLspId,
       "hh3cMplsOamIgrEnable": hh3cMplsOamIgrEnable,
       "hh3cMplsOamIgrDefectType": hh3cMplsOamIgrDefectType,
       "hh3cMplsOamIgrRowStatus": hh3cMplsOamIgrRowStatus,
       "hh3cMplsOamEgrTable": hh3cMplsOamEgrTable,
       "hh3cMplsOamEgrEntry": hh3cMplsOamEgrEntry,
       "hh3cMplsOamEgrIndex": hh3cMplsOamEgrIndex,
       "hh3cMplsOamEgrLspName": hh3cMplsOamEgrLspName,
       "hh3cMplsOamEgrDetectType": hh3cMplsOamEgrDetectType,
       "hh3cMplsOamEgrDetectFreq": hh3cMplsOamEgrDetectFreq,
       "hh3cMplsOamEgrRevType": hh3cMplsOamEgrRevType,
       "hh3cMplsOamEgrRevLspName": hh3cMplsOamEgrRevLspName,
       "hh3cMplsOamEgrLsrId": hh3cMplsOamEgrLsrId,
       "hh3cMplsOamEgrLspId": hh3cMplsOamEgrLspId,
       "hh3cMplsOamEgrEnable": hh3cMplsOamEgrEnable,
       "hh3cMplsOamEgrDefectType": hh3cMplsOamEgrDefectType,
       "hh3cMplsOamEgrRowStatus": hh3cMplsOamEgrRowStatus,
       "hh3cMplsOamNotifications": hh3cMplsOamNotifications,
       "hh3cMplsOamIgrLSPOutDefect": hh3cMplsOamIgrLSPOutDefect,
       "hh3cMplsOamIgrLSPInDefect": hh3cMplsOamIgrLSPInDefect,
       "hh3cMplsOamEgrLSPOutDefect": hh3cMplsOamEgrLSPOutDefect,
       "hh3cMplsOamEgrLSPInDefect": hh3cMplsOamEgrLSPInDefect}
)
