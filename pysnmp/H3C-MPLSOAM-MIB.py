# SNMP MIB module (H3C-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-MPLSOAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:57 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cMplsOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cMplsOAMDefectType(Integer32, TextualConvention):
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



class H3cMplsOAMDetectFreq(Integer32, TextualConvention):
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

_H3cMplsOamScalarGroup_ObjectIdentity = ObjectIdentity
h3cMplsOamScalarGroup = _H3cMplsOamScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 1)
)


class _H3cMplsOamCapability_Type(TruthValue):
    """Custom type h3cMplsOamCapability based on TruthValue"""


_H3cMplsOamCapability_Object = MibScalar
h3cMplsOamCapability = _H3cMplsOamCapability_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 1, 1),
    _H3cMplsOamCapability_Type()
)
h3cMplsOamCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMplsOamCapability.setStatus("current")


class _H3cMplsOamTrapOpen_Type(TruthValue):
    """Custom type h3cMplsOamTrapOpen based on TruthValue"""


_H3cMplsOamTrapOpen_Object = MibScalar
h3cMplsOamTrapOpen = _H3cMplsOamTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 1, 2),
    _H3cMplsOamTrapOpen_Type()
)
h3cMplsOamTrapOpen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cMplsOamTrapOpen.setStatus("current")
_H3cMplsOamTable_ObjectIdentity = ObjectIdentity
h3cMplsOamTable = _H3cMplsOamTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2)
)
_H3cMplsOamIgrTable_Object = MibTable
h3cMplsOamIgrTable = _H3cMplsOamIgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1)
)
if mibBuilder.loadTexts:
    h3cMplsOamIgrTable.setStatus("current")
_H3cMplsOamIgrEntry_Object = MibTableRow
h3cMplsOamIgrEntry = _H3cMplsOamIgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1)
)
h3cMplsOamIgrEntry.setIndexNames(
    (0, "H3C-MPLSOAM-MIB", "h3cMplsOamIgrIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsOamIgrEntry.setStatus("current")
_H3cMplsOamIgrIndex_Type = Unsigned32
_H3cMplsOamIgrIndex_Object = MibTableColumn
h3cMplsOamIgrIndex = _H3cMplsOamIgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 1),
    _H3cMplsOamIgrIndex_Type()
)
h3cMplsOamIgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsOamIgrIndex.setStatus("current")
_H3cMplsOamIgrLspName_Type = OctetString
_H3cMplsOamIgrLspName_Object = MibTableColumn
h3cMplsOamIgrLspName = _H3cMplsOamIgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 2),
    _H3cMplsOamIgrLspName_Type()
)
h3cMplsOamIgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrLspName.setStatus("current")


class _H3cMplsOamIgrDetectType_Type(Integer32):
    """Custom type h3cMplsOamIgrDetectType based on Integer32"""
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


_H3cMplsOamIgrDetectType_Type.__name__ = "Integer32"
_H3cMplsOamIgrDetectType_Object = MibTableColumn
h3cMplsOamIgrDetectType = _H3cMplsOamIgrDetectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 3),
    _H3cMplsOamIgrDetectType_Type()
)
h3cMplsOamIgrDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrDetectType.setStatus("current")
_H3cMplsOamIgrDetectFreq_Type = H3cMplsOAMDetectFreq
_H3cMplsOamIgrDetectFreq_Object = MibTableColumn
h3cMplsOamIgrDetectFreq = _H3cMplsOamIgrDetectFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 4),
    _H3cMplsOamIgrDetectFreq_Type()
)
h3cMplsOamIgrDetectFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrDetectFreq.setStatus("current")


class _H3cMplsOamIgrRevType_Type(Integer32):
    """Custom type h3cMplsOamIgrRevType based on Integer32"""
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


_H3cMplsOamIgrRevType_Type.__name__ = "Integer32"
_H3cMplsOamIgrRevType_Object = MibTableColumn
h3cMplsOamIgrRevType = _H3cMplsOamIgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 5),
    _H3cMplsOamIgrRevType_Type()
)
h3cMplsOamIgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrRevType.setStatus("current")
_H3cMplsOamIgrRevLspName_Type = OctetString
_H3cMplsOamIgrRevLspName_Object = MibTableColumn
h3cMplsOamIgrRevLspName = _H3cMplsOamIgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 6),
    _H3cMplsOamIgrRevLspName_Type()
)
h3cMplsOamIgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrRevLspName.setStatus("current")
_H3cMplsOamIgrLspId_Type = Integer32
_H3cMplsOamIgrLspId_Object = MibTableColumn
h3cMplsOamIgrLspId = _H3cMplsOamIgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 7),
    _H3cMplsOamIgrLspId_Type()
)
h3cMplsOamIgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrLspId.setStatus("current")


class _H3cMplsOamIgrEnable_Type(TruthValue):
    """Custom type h3cMplsOamIgrEnable based on TruthValue"""


_H3cMplsOamIgrEnable_Object = MibTableColumn
h3cMplsOamIgrEnable = _H3cMplsOamIgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 8),
    _H3cMplsOamIgrEnable_Type()
)
h3cMplsOamIgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrEnable.setStatus("current")
_H3cMplsOamIgrDefectType_Type = H3cMplsOAMDefectType
_H3cMplsOamIgrDefectType_Object = MibTableColumn
h3cMplsOamIgrDefectType = _H3cMplsOamIgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 9),
    _H3cMplsOamIgrDefectType_Type()
)
h3cMplsOamIgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsOamIgrDefectType.setStatus("current")
_H3cMplsOamIgrRowStatus_Type = RowStatus
_H3cMplsOamIgrRowStatus_Object = MibTableColumn
h3cMplsOamIgrRowStatus = _H3cMplsOamIgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 1, 1, 10),
    _H3cMplsOamIgrRowStatus_Type()
)
h3cMplsOamIgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamIgrRowStatus.setStatus("current")
_H3cMplsOamEgrTable_Object = MibTable
h3cMplsOamEgrTable = _H3cMplsOamEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2)
)
if mibBuilder.loadTexts:
    h3cMplsOamEgrTable.setStatus("current")
_H3cMplsOamEgrEntry_Object = MibTableRow
h3cMplsOamEgrEntry = _H3cMplsOamEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1)
)
h3cMplsOamEgrEntry.setIndexNames(
    (0, "H3C-MPLSOAM-MIB", "h3cMplsOamEgrIndex"),
)
if mibBuilder.loadTexts:
    h3cMplsOamEgrEntry.setStatus("current")
_H3cMplsOamEgrIndex_Type = Unsigned32
_H3cMplsOamEgrIndex_Object = MibTableColumn
h3cMplsOamEgrIndex = _H3cMplsOamEgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 1),
    _H3cMplsOamEgrIndex_Type()
)
h3cMplsOamEgrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cMplsOamEgrIndex.setStatus("current")
_H3cMplsOamEgrLspName_Type = OctetString
_H3cMplsOamEgrLspName_Object = MibTableColumn
h3cMplsOamEgrLspName = _H3cMplsOamEgrLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 2),
    _H3cMplsOamEgrLspName_Type()
)
h3cMplsOamEgrLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrLspName.setStatus("current")


class _H3cMplsOamEgrDetectType_Type(Integer32):
    """Custom type h3cMplsOamEgrDetectType based on Integer32"""
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


_H3cMplsOamEgrDetectType_Type.__name__ = "Integer32"
_H3cMplsOamEgrDetectType_Object = MibTableColumn
h3cMplsOamEgrDetectType = _H3cMplsOamEgrDetectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 3),
    _H3cMplsOamEgrDetectType_Type()
)
h3cMplsOamEgrDetectType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrDetectType.setStatus("current")
_H3cMplsOamEgrDetectFreq_Type = H3cMplsOAMDetectFreq
_H3cMplsOamEgrDetectFreq_Object = MibTableColumn
h3cMplsOamEgrDetectFreq = _H3cMplsOamEgrDetectFreq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 4),
    _H3cMplsOamEgrDetectFreq_Type()
)
h3cMplsOamEgrDetectFreq.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrDetectFreq.setStatus("current")


class _H3cMplsOamEgrRevType_Type(Integer32):
    """Custom type h3cMplsOamEgrRevType based on Integer32"""
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


_H3cMplsOamEgrRevType_Type.__name__ = "Integer32"
_H3cMplsOamEgrRevType_Object = MibTableColumn
h3cMplsOamEgrRevType = _H3cMplsOamEgrRevType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 5),
    _H3cMplsOamEgrRevType_Type()
)
h3cMplsOamEgrRevType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrRevType.setStatus("current")
_H3cMplsOamEgrRevLspName_Type = OctetString
_H3cMplsOamEgrRevLspName_Object = MibTableColumn
h3cMplsOamEgrRevLspName = _H3cMplsOamEgrRevLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 6),
    _H3cMplsOamEgrRevLspName_Type()
)
h3cMplsOamEgrRevLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrRevLspName.setStatus("current")
_H3cMplsOamEgrLsrId_Type = IpAddress
_H3cMplsOamEgrLsrId_Object = MibTableColumn
h3cMplsOamEgrLsrId = _H3cMplsOamEgrLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 7),
    _H3cMplsOamEgrLsrId_Type()
)
h3cMplsOamEgrLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrLsrId.setStatus("current")
_H3cMplsOamEgrLspId_Type = Integer32
_H3cMplsOamEgrLspId_Object = MibTableColumn
h3cMplsOamEgrLspId = _H3cMplsOamEgrLspId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 8),
    _H3cMplsOamEgrLspId_Type()
)
h3cMplsOamEgrLspId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrLspId.setStatus("current")


class _H3cMplsOamEgrEnable_Type(TruthValue):
    """Custom type h3cMplsOamEgrEnable based on TruthValue"""


_H3cMplsOamEgrEnable_Object = MibTableColumn
h3cMplsOamEgrEnable = _H3cMplsOamEgrEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 9),
    _H3cMplsOamEgrEnable_Type()
)
h3cMplsOamEgrEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrEnable.setStatus("current")
_H3cMplsOamEgrDefectType_Type = H3cMplsOAMDefectType
_H3cMplsOamEgrDefectType_Object = MibTableColumn
h3cMplsOamEgrDefectType = _H3cMplsOamEgrDefectType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 10),
    _H3cMplsOamEgrDefectType_Type()
)
h3cMplsOamEgrDefectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cMplsOamEgrDefectType.setStatus("current")
_H3cMplsOamEgrRowStatus_Type = RowStatus
_H3cMplsOamEgrRowStatus_Object = MibTableColumn
h3cMplsOamEgrRowStatus = _H3cMplsOamEgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 2, 2, 1, 11),
    _H3cMplsOamEgrRowStatus_Type()
)
h3cMplsOamEgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cMplsOamEgrRowStatus.setStatus("current")
_H3cMplsOamNotifications_ObjectIdentity = ObjectIdentity
h3cMplsOamNotifications = _H3cMplsOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3)
)

# Managed Objects groups


# Notification objects

h3cMplsOamIgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 1)
)
h3cMplsOamIgrLSPOutDefect.setObjects(
      *(("H3C-MPLSOAM-MIB", "h3cMplsOamIgrLspName"),
        ("H3C-MPLSOAM-MIB", "h3cMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    h3cMplsOamIgrLSPOutDefect.setStatus(
        "current"
    )

h3cMplsOamIgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 2)
)
h3cMplsOamIgrLSPInDefect.setObjects(
      *(("H3C-MPLSOAM-MIB", "h3cMplsOamIgrLspName"),
        ("H3C-MPLSOAM-MIB", "h3cMplsOamIgrDefectType"))
)
if mibBuilder.loadTexts:
    h3cMplsOamIgrLSPInDefect.setStatus(
        "current"
    )

h3cMplsOamEgrLSPOutDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 3)
)
h3cMplsOamEgrLSPOutDefect.setObjects(
      *(("H3C-MPLSOAM-MIB", "h3cMplsOamEgrLspName"),
        ("H3C-MPLSOAM-MIB", "h3cMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    h3cMplsOamEgrLSPOutDefect.setStatus(
        "current"
    )

h3cMplsOamEgrLSPInDefect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 79, 3, 4)
)
h3cMplsOamEgrLSPInDefect.setObjects(
      *(("H3C-MPLSOAM-MIB", "h3cMplsOamEgrLspName"),
        ("H3C-MPLSOAM-MIB", "h3cMplsOamEgrDefectType"))
)
if mibBuilder.loadTexts:
    h3cMplsOamEgrLSPInDefect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-MPLSOAM-MIB",
    **{"H3cMplsOAMDefectType": H3cMplsOAMDefectType,
       "H3cMplsOAMDetectFreq": H3cMplsOAMDetectFreq,
       "h3cMplsOam": h3cMplsOam,
       "h3cMplsOamScalarGroup": h3cMplsOamScalarGroup,
       "h3cMplsOamCapability": h3cMplsOamCapability,
       "h3cMplsOamTrapOpen": h3cMplsOamTrapOpen,
       "h3cMplsOamTable": h3cMplsOamTable,
       "h3cMplsOamIgrTable": h3cMplsOamIgrTable,
       "h3cMplsOamIgrEntry": h3cMplsOamIgrEntry,
       "h3cMplsOamIgrIndex": h3cMplsOamIgrIndex,
       "h3cMplsOamIgrLspName": h3cMplsOamIgrLspName,
       "h3cMplsOamIgrDetectType": h3cMplsOamIgrDetectType,
       "h3cMplsOamIgrDetectFreq": h3cMplsOamIgrDetectFreq,
       "h3cMplsOamIgrRevType": h3cMplsOamIgrRevType,
       "h3cMplsOamIgrRevLspName": h3cMplsOamIgrRevLspName,
       "h3cMplsOamIgrLspId": h3cMplsOamIgrLspId,
       "h3cMplsOamIgrEnable": h3cMplsOamIgrEnable,
       "h3cMplsOamIgrDefectType": h3cMplsOamIgrDefectType,
       "h3cMplsOamIgrRowStatus": h3cMplsOamIgrRowStatus,
       "h3cMplsOamEgrTable": h3cMplsOamEgrTable,
       "h3cMplsOamEgrEntry": h3cMplsOamEgrEntry,
       "h3cMplsOamEgrIndex": h3cMplsOamEgrIndex,
       "h3cMplsOamEgrLspName": h3cMplsOamEgrLspName,
       "h3cMplsOamEgrDetectType": h3cMplsOamEgrDetectType,
       "h3cMplsOamEgrDetectFreq": h3cMplsOamEgrDetectFreq,
       "h3cMplsOamEgrRevType": h3cMplsOamEgrRevType,
       "h3cMplsOamEgrRevLspName": h3cMplsOamEgrRevLspName,
       "h3cMplsOamEgrLsrId": h3cMplsOamEgrLsrId,
       "h3cMplsOamEgrLspId": h3cMplsOamEgrLspId,
       "h3cMplsOamEgrEnable": h3cMplsOamEgrEnable,
       "h3cMplsOamEgrDefectType": h3cMplsOamEgrDefectType,
       "h3cMplsOamEgrRowStatus": h3cMplsOamEgrRowStatus,
       "h3cMplsOamNotifications": h3cMplsOamNotifications,
       "h3cMplsOamIgrLSPOutDefect": h3cMplsOamIgrLSPOutDefect,
       "h3cMplsOamIgrLSPInDefect": h3cMplsOamIgrLSPInDefect,
       "h3cMplsOamEgrLSPOutDefect": h3cMplsOamEgrLSPOutDefect,
       "h3cMplsOamEgrLSPInDefect": h3cMplsOamEgrLSPInDefect}
)
