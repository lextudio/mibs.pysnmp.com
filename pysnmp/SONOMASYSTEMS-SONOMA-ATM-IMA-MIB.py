# SNMP MIB module (SONOMASYSTEMS-SONOMA-ATM-IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONOMASYSTEMS-SONOMA-ATM-IMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:42 2024
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

(sonomaATM,) = mibBuilder.importSymbols(
    "SONOMASYSTEMS-SONOMA-MIB",
    "sonomaATM")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonomaImaATMAdapterGroup_ObjectIdentity = ObjectIdentity
sonomaImaATMAdapterGroup = _SonomaImaATMAdapterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7)
)
_AtmImaGroupObjects_ObjectIdentity = ObjectIdentity
atmImaGroupObjects = _AtmImaGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1)
)
_ImaGroupNumber_Type = Integer32
_ImaGroupNumber_Object = MibScalar
imaGroupNumber = _ImaGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 1),
    _ImaGroupNumber_Type()
)
imaGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumber.setStatus("mandatory")
_ImaGroupTable_Object = MibTable
imaGroupTable = _ImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2)
)
if mibBuilder.loadTexts:
    imaGroupTable.setStatus("mandatory")
_ImaGroupEntry_Object = MibTableRow
imaGroupEntry = _ImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1)
)
imaGroupEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaGroupEntry.setStatus("mandatory")
_ImaGroupIndex_Type = Integer32
_ImaGroupIndex_Object = MibTableColumn
imaGroupIndex = _ImaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 1),
    _ImaGroupIndex_Type()
)
imaGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIndex.setStatus("mandatory")


class _ImaGroupRowStatus_Type(Integer32):
    """Custom type imaGroupRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ImaGroupRowStatus_Type.__name__ = "Integer32"
_ImaGroupRowStatus_Object = MibTableColumn
imaGroupRowStatus = _ImaGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 2),
    _ImaGroupRowStatus_Type()
)
imaGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupRowStatus.setStatus("mandatory")
_ImaGroupIfIndex_Type = Integer32
_ImaGroupIfIndex_Object = MibTableColumn
imaGroupIfIndex = _ImaGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 3),
    _ImaGroupIfIndex_Type()
)
imaGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIfIndex.setStatus("mandatory")


class _ImaGroupNeState_Type(Integer32):
    """Custom type imaGroupNeState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 8),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("configAbortUnsupportedM", 4),
          ("insufficientLinks", 7),
          ("notConfigured", 1),
          ("operational", 9),
          ("startUp", 2),
          ("startUpAck", 3))
    )


_ImaGroupNeState_Type.__name__ = "Integer32"
_ImaGroupNeState_Object = MibTableColumn
imaGroupNeState = _ImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 4),
    _ImaGroupNeState_Type()
)
imaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNeState.setStatus("mandatory")


class _ImaGroupFeState_Type(Integer32):
    """Custom type imaGroupFeState based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 8),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("configAbortUnsupportedM", 4),
          ("insufficientLinks", 7),
          ("notConfigured", 1),
          ("operational", 9),
          ("startUp", 2),
          ("startUpAck", 3))
    )


_ImaGroupFeState_Type.__name__ = "Integer32"
_ImaGroupFeState_Object = MibTableColumn
imaGroupFeState = _ImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 5),
    _ImaGroupFeState_Type()
)
imaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeState.setStatus("mandatory")


class _ImaGroupFailureStatus_Type(Integer32):
    """Custom type imaGroupFailureStatus based on Integer32"""
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
        *(("blockedFe", 11),
          ("blockedNe", 10),
          ("failedAssymetricFe", 7),
          ("failedAssymetricNe", 6),
          ("insufficientLinksFe", 9),
          ("insufficientLinksNe", 8),
          ("invalidMValueFe", 5),
          ("invalidMValueNe", 4),
          ("noFailure", 1),
          ("otherFailure", 12),
          ("startUpFe", 3),
          ("startUpNe", 2))
    )


_ImaGroupFailureStatus_Type.__name__ = "Integer32"
_ImaGroupFailureStatus_Object = MibTableColumn
imaGroupFailureStatus = _ImaGroupFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 6),
    _ImaGroupFailureStatus_Type()
)
imaGroupFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFailureStatus.setStatus("mandatory")


class _ImaGroupSymmetry_Type(Integer32):
    """Custom type imaGroupSymmetry based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("asymmetricConfiguration", 3),
          ("asymmetricOperation", 2),
          ("symmetricOperation", 1))
    )


_ImaGroupSymmetry_Type.__name__ = "Integer32"
_ImaGroupSymmetry_Object = MibTableColumn
imaGroupSymmetry = _ImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 7),
    _ImaGroupSymmetry_Type()
)
imaGroupSymmetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupSymmetry.setStatus("mandatory")


class _ImaGroupMinNumTxLinks_Type(Integer32):
    """Custom type imaGroupMinNumTxLinks based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ImaGroupMinNumTxLinks_Type.__name__ = "Integer32"
_ImaGroupMinNumTxLinks_Object = MibTableColumn
imaGroupMinNumTxLinks = _ImaGroupMinNumTxLinks_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 8),
    _ImaGroupMinNumTxLinks_Type()
)
imaGroupMinNumTxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupMinNumTxLinks.setStatus("mandatory")


class _ImaGroupMinNumRxLinks_Type(Integer32):
    """Custom type imaGroupMinNumRxLinks based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ImaGroupMinNumRxLinks_Type.__name__ = "Integer32"
_ImaGroupMinNumRxLinks_Object = MibTableColumn
imaGroupMinNumRxLinks = _ImaGroupMinNumRxLinks_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 9),
    _ImaGroupMinNumRxLinks_Type()
)
imaGroupMinNumRxLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupMinNumRxLinks.setStatus("mandatory")


class _ImaGroupNeTxClkMode_Type(Integer32):
    """Custom type imaGroupNeTxClkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )


_ImaGroupNeTxClkMode_Type.__name__ = "Integer32"
_ImaGroupNeTxClkMode_Object = MibTableColumn
imaGroupNeTxClkMode = _ImaGroupNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 10),
    _ImaGroupNeTxClkMode_Type()
)
imaGroupNeTxClkMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupNeTxClkMode.setStatus("mandatory")


class _ImaGroupFeTxClkMode_Type(Integer32):
    """Custom type imaGroupFeTxClkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ctc", 1),
          ("itc", 2))
    )


_ImaGroupFeTxClkMode_Type.__name__ = "Integer32"
_ImaGroupFeTxClkMode_Object = MibTableColumn
imaGroupFeTxClkMode = _ImaGroupFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 11),
    _ImaGroupFeTxClkMode_Type()
)
imaGroupFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeTxClkMode.setStatus("mandatory")


class _ImaGroupTxTimingRefLink_Type(Integer32):
    """Custom type imaGroupTxTimingRefLink based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ImaGroupTxTimingRefLink_Type.__name__ = "Integer32"
_ImaGroupTxTimingRefLink_Object = MibTableColumn
imaGroupTxTimingRefLink = _ImaGroupTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 12),
    _ImaGroupTxTimingRefLink_Type()
)
imaGroupTxTimingRefLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupTxTimingRefLink.setStatus("mandatory")


class _ImaGroupRxTimingRefLink_Type(Integer32):
    """Custom type imaGroupRxTimingRefLink based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ImaGroupRxTimingRefLink_Type.__name__ = "Integer32"
_ImaGroupRxTimingRefLink_Object = MibTableColumn
imaGroupRxTimingRefLink = _ImaGroupRxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 13),
    _ImaGroupRxTimingRefLink_Type()
)
imaGroupRxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxTimingRefLink.setStatus("mandatory")
_ImaGroupLastChange_Type = Integer32
_ImaGroupLastChange_Object = MibTableColumn
imaGroupLastChange = _ImaGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 14),
    _ImaGroupLastChange_Type()
)
imaGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupLastChange.setStatus("mandatory")


class _ImaGroupTxImaId_Type(Integer32):
    """Custom type imaGroupTxImaId based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupTxImaId_Type.__name__ = "Integer32"
_ImaGroupTxImaId_Object = MibTableColumn
imaGroupTxImaId = _ImaGroupTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 15),
    _ImaGroupTxImaId_Type()
)
imaGroupTxImaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupTxImaId.setStatus("mandatory")


class _ImaGroupRxImaId_Type(Integer32):
    """Custom type imaGroupRxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupRxImaId_Type.__name__ = "Integer32"
_ImaGroupRxImaId_Object = MibTableColumn
imaGroupRxImaId = _ImaGroupRxImaId_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 16),
    _ImaGroupRxImaId_Type()
)
imaGroupRxImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxImaId.setStatus("mandatory")


class _ImaGroupTxFrameLength_Type(Integer32):
    """Custom type imaGroupTxFrameLength based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("m128", 128),
          ("m256", 256),
          ("m32", 32),
          ("m64", 64))
    )


_ImaGroupTxFrameLength_Type.__name__ = "Integer32"
_ImaGroupTxFrameLength_Object = MibTableColumn
imaGroupTxFrameLength = _ImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 17),
    _ImaGroupTxFrameLength_Type()
)
imaGroupTxFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupTxFrameLength.setStatus("mandatory")


class _ImaGroupRxFrameLength_Type(Integer32):
    """Custom type imaGroupRxFrameLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              64,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("m128", 128),
          ("m256", 256),
          ("m32", 32),
          ("m64", 64))
    )


_ImaGroupRxFrameLength_Type.__name__ = "Integer32"
_ImaGroupRxFrameLength_Object = MibTableColumn
imaGroupRxFrameLength = _ImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 18),
    _ImaGroupRxFrameLength_Type()
)
imaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxFrameLength.setStatus("mandatory")


class _ImaGroupDiffDelayMax_Type(Integer32):
    """Custom type imaGroupDiffDelayMax based on Integer32"""
    defaultValue = 25


_ImaGroupDiffDelayMax_Object = MibTableColumn
imaGroupDiffDelayMax = _ImaGroupDiffDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 19),
    _ImaGroupDiffDelayMax_Type()
)
imaGroupDiffDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupDiffDelayMax.setStatus("mandatory")
_ImaGroupLeastDelayLink_Type = Integer32
_ImaGroupLeastDelayLink_Object = MibTableColumn
imaGroupLeastDelayLink = _ImaGroupLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 20),
    _ImaGroupLeastDelayLink_Type()
)
imaGroupLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupLeastDelayLink.setStatus("mandatory")
_ImaGroupDiffDelayMaxObs_Type = Integer32
_ImaGroupDiffDelayMaxObs_Object = MibTableColumn
imaGroupDiffDelayMaxObs = _ImaGroupDiffDelayMaxObs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 21),
    _ImaGroupDiffDelayMaxObs_Type()
)
imaGroupDiffDelayMaxObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupDiffDelayMaxObs.setStatus("mandatory")


class _ImaGroupAlphaValue_Type(Integer32):
    """Custom type imaGroupAlphaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ImaGroupAlphaValue_Type.__name__ = "Integer32"
_ImaGroupAlphaValue_Object = MibTableColumn
imaGroupAlphaValue = _ImaGroupAlphaValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 22),
    _ImaGroupAlphaValue_Type()
)
imaGroupAlphaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupAlphaValue.setStatus("mandatory")


class _ImaGroupBetaValue_Type(Integer32):
    """Custom type imaGroupBetaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ImaGroupBetaValue_Type.__name__ = "Integer32"
_ImaGroupBetaValue_Object = MibTableColumn
imaGroupBetaValue = _ImaGroupBetaValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 23),
    _ImaGroupBetaValue_Type()
)
imaGroupBetaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupBetaValue.setStatus("mandatory")


class _ImaGroupGammaValue_Type(Integer32):
    """Custom type imaGroupGammaValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ImaGroupGammaValue_Type.__name__ = "Integer32"
_ImaGroupGammaValue_Object = MibTableColumn
imaGroupGammaValue = _ImaGroupGammaValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 24),
    _ImaGroupGammaValue_Type()
)
imaGroupGammaValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupGammaValue.setStatus("mandatory")
_ImaGroupRunningSecs_Type = Integer32
_ImaGroupRunningSecs_Object = MibTableColumn
imaGroupRunningSecs = _ImaGroupRunningSecs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 25),
    _ImaGroupRunningSecs_Type()
)
imaGroupRunningSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRunningSecs.setStatus("mandatory")
_ImaGroupUnavailSecs_Type = Integer32
_ImaGroupUnavailSecs_Object = MibTableColumn
imaGroupUnavailSecs = _ImaGroupUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 26),
    _ImaGroupUnavailSecs_Type()
)
imaGroupUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupUnavailSecs.setStatus("mandatory")
_ImaGroupNeNumFailures_Type = Integer32
_ImaGroupNeNumFailures_Object = MibTableColumn
imaGroupNeNumFailures = _ImaGroupNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 27),
    _ImaGroupNeNumFailures_Type()
)
imaGroupNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNeNumFailures.setStatus("mandatory")
_ImaGroupFeNumFailures_Type = Integer32
_ImaGroupFeNumFailures_Object = MibTableColumn
imaGroupFeNumFailures = _ImaGroupFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 28),
    _ImaGroupFeNumFailures_Type()
)
imaGroupFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeNumFailures.setStatus("mandatory")
_ImaGroupTxAvailCellRate_Type = Integer32
_ImaGroupTxAvailCellRate_Object = MibTableColumn
imaGroupTxAvailCellRate = _ImaGroupTxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 29),
    _ImaGroupTxAvailCellRate_Type()
)
imaGroupTxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTxAvailCellRate.setStatus("mandatory")
_ImaGroupRxAvailCellRate_Type = Integer32
_ImaGroupRxAvailCellRate_Object = MibTableColumn
imaGroupRxAvailCellRate = _ImaGroupRxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 30),
    _ImaGroupRxAvailCellRate_Type()
)
imaGroupRxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxAvailCellRate.setStatus("mandatory")
_ImaGroupNumTxCfgLnks_Type = Integer32
_ImaGroupNumTxCfgLnks_Object = MibTableColumn
imaGroupNumTxCfgLnks = _ImaGroupNumTxCfgLnks_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 31),
    _ImaGroupNumTxCfgLnks_Type()
)
imaGroupNumTxCfgLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumTxCfgLnks.setStatus("mandatory")
_ImaGroupNumRxCfgLnks_Type = Integer32
_ImaGroupNumRxCfgLnks_Object = MibTableColumn
imaGroupNumRxCfgLnks = _ImaGroupNumRxCfgLnks_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 32),
    _ImaGroupNumRxCfgLnks_Type()
)
imaGroupNumRxCfgLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumRxCfgLnks.setStatus("mandatory")
_ImaGroupNumTxActLnks_Type = Integer32
_ImaGroupNumTxActLnks_Object = MibTableColumn
imaGroupNumTxActLnks = _ImaGroupNumTxActLnks_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 33),
    _ImaGroupNumTxActLnks_Type()
)
imaGroupNumTxActLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumTxActLnks.setStatus("mandatory")
_ImaGroupNumRxActLnks_Type = Integer32
_ImaGroupNumRxActLnks_Object = MibTableColumn
imaGroupNumRxActLnks = _ImaGroupNumRxActLnks_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 34),
    _ImaGroupNumRxActLnks_Type()
)
imaGroupNumRxActLnks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumRxActLnks.setStatus("mandatory")


class _ImaGroupTestLinkIfIndex_Type(Integer32):
    """Custom type imaGroupTestLinkIfIndex based on Integer32"""
    defaultValue = -1


_ImaGroupTestLinkIfIndex_Object = MibTableColumn
imaGroupTestLinkIfIndex = _ImaGroupTestLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 35),
    _ImaGroupTestLinkIfIndex_Type()
)
imaGroupTestLinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupTestLinkIfIndex.setStatus("mandatory")


class _ImaGroupTestPattern_Type(Integer32):
    """Custom type imaGroupTestPattern based on Integer32"""
    defaultValue = -1


_ImaGroupTestPattern_Object = MibTableColumn
imaGroupTestPattern = _ImaGroupTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 36),
    _ImaGroupTestPattern_Type()
)
imaGroupTestPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupTestPattern.setStatus("mandatory")


class _ImaGroupTestProcStatus_Type(Integer32):
    """Custom type imaGroupTestProcStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("linkFail", 3),
          ("operating", 2))
    )


_ImaGroupTestProcStatus_Type.__name__ = "Integer32"
_ImaGroupTestProcStatus_Object = MibTableColumn
imaGroupTestProcStatus = _ImaGroupTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 1, 2, 1, 37),
    _ImaGroupTestProcStatus_Type()
)
imaGroupTestProcStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaGroupTestProcStatus.setStatus("mandatory")
_AtmImaLinkObjects_ObjectIdentity = ObjectIdentity
atmImaLinkObjects = _AtmImaLinkObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2)
)
_ImaLinkTable_Object = MibTable
imaLinkTable = _ImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1)
)
if mibBuilder.loadTexts:
    imaLinkTable.setStatus("mandatory")
_ImaLinkEntry_Object = MibTableRow
imaLinkEntry = _ImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1)
)
imaLinkEntry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB", "imaLinkGroupIndex"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB", "imaLinkIfIndex"),
)
if mibBuilder.loadTexts:
    imaLinkEntry.setStatus("mandatory")
_ImaLinkIfIndex_Type = Integer32
_ImaLinkIfIndex_Object = MibTableColumn
imaLinkIfIndex = _ImaLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 1),
    _ImaLinkIfIndex_Type()
)
imaLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIfIndex.setStatus("mandatory")


class _ImaLinkRowStatus_Type(Integer32):
    """Custom type imaLinkRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ImaLinkRowStatus_Type.__name__ = "Integer32"
_ImaLinkRowStatus_Object = MibTableColumn
imaLinkRowStatus = _ImaLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 2),
    _ImaLinkRowStatus_Type()
)
imaLinkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaLinkRowStatus.setStatus("mandatory")


class _ImaLinkGroupIndex_Type(Integer32):
    """Custom type imaLinkGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("imaGroup-1", 1),
          ("none", 2))
    )


_ImaLinkGroupIndex_Type.__name__ = "Integer32"
_ImaLinkGroupIndex_Object = MibTableColumn
imaLinkGroupIndex = _ImaLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 3),
    _ImaLinkGroupIndex_Type()
)
imaLinkGroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaLinkGroupIndex.setStatus("mandatory")


class _ImaLinkNeTxState_Type(Integer32):
    """Custom type imaLinkNeTxState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableBlocked", 5),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )


_ImaLinkNeTxState_Type.__name__ = "Integer32"
_ImaLinkNeTxState_Object = MibTableColumn
imaLinkNeTxState = _ImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 4),
    _ImaLinkNeTxState_Type()
)
imaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxState.setStatus("mandatory")


class _ImaLinkNeRxState_Type(Integer32):
    """Custom type imaLinkNeRxState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableBlocked", 5),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )


_ImaLinkNeRxState_Type.__name__ = "Integer32"
_ImaLinkNeRxState_Object = MibTableColumn
imaLinkNeRxState = _ImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 5),
    _ImaLinkNeRxState_Type()
)
imaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxState.setStatus("mandatory")


class _ImaLinkFeTxState_Type(Integer32):
    """Custom type imaLinkFeTxState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableBlocked", 5),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )


_ImaLinkFeTxState_Type.__name__ = "Integer32"
_ImaLinkFeTxState_Object = MibTableColumn
imaLinkFeTxState = _ImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 6),
    _ImaLinkFeTxState_Type()
)
imaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxState.setStatus("mandatory")


class _ImaLinkFeRxState_Type(Integer32):
    """Custom type imaLinkFeRxState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableBlocked", 5),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )


_ImaLinkFeRxState_Type.__name__ = "Integer32"
_ImaLinkFeRxState_Object = MibTableColumn
imaLinkFeRxState = _ImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 7),
    _ImaLinkFeRxState_Type()
)
imaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxState.setStatus("mandatory")


class _ImaLinkNeRxFailureStatus_Type(Integer32):
    """Custom type imaLinkNeRxFailureStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 6),
          ("farEndRxLinkUnusable", 9),
          ("farEndTxLinkUnusable", 8),
          ("fault", 7),
          ("imaLinkFailure", 2),
          ("lifFailure", 3),
          ("lodsFailure", 4),
          ("misConnected", 5),
          ("noFailure", 1))
    )


_ImaLinkNeRxFailureStatus_Type.__name__ = "Integer32"
_ImaLinkNeRxFailureStatus_Object = MibTableColumn
imaLinkNeRxFailureStatus = _ImaLinkNeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 8),
    _ImaLinkNeRxFailureStatus_Type()
)
imaLinkNeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxFailureStatus.setStatus("mandatory")


class _ImaLinkFeRxFailureStatus_Type(Integer32):
    """Custom type imaLinkFeRxFailureStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 6),
          ("farEndRxLinkUnusable", 9),
          ("farEndTxLinkUnusable", 8),
          ("fault", 7),
          ("imaLinkFailure", 2),
          ("lifFailure", 3),
          ("lodsFailure", 4),
          ("misConnected", 5),
          ("noFailure", 1))
    )


_ImaLinkFeRxFailureStatus_Type.__name__ = "Integer32"
_ImaLinkFeRxFailureStatus_Object = MibTableColumn
imaLinkFeRxFailureStatus = _ImaLinkFeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 9),
    _ImaLinkFeRxFailureStatus_Type()
)
imaLinkFeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxFailureStatus.setStatus("mandatory")


class _ImaLinkTxLid_Type(Integer32):
    """Custom type imaLinkTxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ImaLinkTxLid_Type.__name__ = "Integer32"
_ImaLinkTxLid_Object = MibTableColumn
imaLinkTxLid = _ImaLinkTxLid_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 10),
    _ImaLinkTxLid_Type()
)
imaLinkTxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTxLid.setStatus("mandatory")


class _ImaLinkRxLid_Type(Integer32):
    """Custom type imaLinkRxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ImaLinkRxLid_Type.__name__ = "Integer32"
_ImaLinkRxLid_Object = MibTableColumn
imaLinkRxLid = _ImaLinkRxLid_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 11),
    _ImaLinkRxLid_Type()
)
imaLinkRxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxLid.setStatus("mandatory")
_ImaLinkRelDelay_Type = Integer32
_ImaLinkRelDelay_Object = MibTableColumn
imaLinkRelDelay = _ImaLinkRelDelay_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 12),
    _ImaLinkRelDelay_Type()
)
imaLinkRelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRelDelay.setStatus("mandatory")
_ImaLinkImaViolations_Type = Integer32
_ImaLinkImaViolations_Object = MibTableColumn
imaLinkImaViolations = _ImaLinkImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 13),
    _ImaLinkImaViolations_Type()
)
imaLinkImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkImaViolations.setStatus("mandatory")
_ImaLinkOifAnomalies_Type = Integer32
_ImaLinkOifAnomalies_Object = MibTableColumn
imaLinkOifAnomalies = _ImaLinkOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 14),
    _ImaLinkOifAnomalies_Type()
)
imaLinkOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkOifAnomalies.setStatus("mandatory")
_ImaLinkNeSevErroredSec_Type = Integer32
_ImaLinkNeSevErroredSec_Object = MibTableColumn
imaLinkNeSevErroredSec = _ImaLinkNeSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 15),
    _ImaLinkNeSevErroredSec_Type()
)
imaLinkNeSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeSevErroredSec.setStatus("mandatory")
_ImaLinkFeSevErroredSec_Type = Integer32
_ImaLinkFeSevErroredSec_Object = MibTableColumn
imaLinkFeSevErroredSec = _ImaLinkFeSevErroredSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 16),
    _ImaLinkFeSevErroredSec_Type()
)
imaLinkFeSevErroredSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeSevErroredSec.setStatus("mandatory")
_ImaLinkNeUnavailSec_Type = Integer32
_ImaLinkNeUnavailSec_Object = MibTableColumn
imaLinkNeUnavailSec = _ImaLinkNeUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 17),
    _ImaLinkNeUnavailSec_Type()
)
imaLinkNeUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeUnavailSec.setStatus("mandatory")
_ImaLinkFeUnavailSec_Type = Integer32
_ImaLinkFeUnavailSec_Object = MibTableColumn
imaLinkFeUnavailSec = _ImaLinkFeUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 18),
    _ImaLinkFeUnavailSec_Type()
)
imaLinkFeUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeUnavailSec.setStatus("mandatory")
_ImaLinkNeTxUnusableSec_Type = Integer32
_ImaLinkNeTxUnusableSec_Object = MibTableColumn
imaLinkNeTxUnusableSec = _ImaLinkNeTxUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 19),
    _ImaLinkNeTxUnusableSec_Type()
)
imaLinkNeTxUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxUnusableSec.setStatus("mandatory")
_ImaLinkNeRxUnusableSec_Type = Integer32
_ImaLinkNeRxUnusableSec_Object = MibTableColumn
imaLinkNeRxUnusableSec = _ImaLinkNeRxUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 20),
    _ImaLinkNeRxUnusableSec_Type()
)
imaLinkNeRxUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxUnusableSec.setStatus("mandatory")
_ImaLinkFeTxUnusableSec_Type = Integer32
_ImaLinkFeTxUnusableSec_Object = MibTableColumn
imaLinkFeTxUnusableSec = _ImaLinkFeTxUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 21),
    _ImaLinkFeTxUnusableSec_Type()
)
imaLinkFeTxUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxUnusableSec.setStatus("mandatory")
_ImaLinkFeRxUnusableSec_Type = Integer32
_ImaLinkFeRxUnusableSec_Object = MibTableColumn
imaLinkFeRxUnusableSec = _ImaLinkFeRxUnusableSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 22),
    _ImaLinkFeRxUnusableSec_Type()
)
imaLinkFeRxUnusableSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxUnusableSec.setStatus("mandatory")
_ImaLinkNeTxNumFailures_Type = Integer32
_ImaLinkNeTxNumFailures_Object = MibTableColumn
imaLinkNeTxNumFailures = _ImaLinkNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 23),
    _ImaLinkNeTxNumFailures_Type()
)
imaLinkNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxNumFailures.setStatus("mandatory")
_ImaLinkNeRxNumFailures_Type = Integer32
_ImaLinkNeRxNumFailures_Object = MibTableColumn
imaLinkNeRxNumFailures = _ImaLinkNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 24),
    _ImaLinkNeRxNumFailures_Type()
)
imaLinkNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxNumFailures.setStatus("mandatory")
_ImaLinkFeTxNumFailures_Type = Integer32
_ImaLinkFeTxNumFailures_Object = MibTableColumn
imaLinkFeTxNumFailures = _ImaLinkFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 25),
    _ImaLinkFeTxNumFailures_Type()
)
imaLinkFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxNumFailures.setStatus("mandatory")
_ImaLinkFeRxNumFailures_Type = Integer32
_ImaLinkFeRxNumFailures_Object = MibTableColumn
imaLinkFeRxNumFailures = _ImaLinkFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 26),
    _ImaLinkFeRxNumFailures_Type()
)
imaLinkFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxNumFailures.setStatus("mandatory")
_ImaLinkTxStuffs_Type = Integer32
_ImaLinkTxStuffs_Object = MibTableColumn
imaLinkTxStuffs = _ImaLinkTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 27),
    _ImaLinkTxStuffs_Type()
)
imaLinkTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTxStuffs.setStatus("mandatory")
_ImaLinkRxStuffs_Type = Integer32
_ImaLinkRxStuffs_Object = MibTableColumn
imaLinkRxStuffs = _ImaLinkRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 28),
    _ImaLinkRxStuffs_Type()
)
imaLinkRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxStuffs.setStatus("mandatory")


class _ImaLinkRxTestPattern_Type(Integer32):
    """Custom type imaLinkRxTestPattern based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaLinkRxTestPattern_Type.__name__ = "Integer32"
_ImaLinkRxTestPattern_Object = MibTableColumn
imaLinkRxTestPattern = _ImaLinkRxTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 29),
    _ImaLinkRxTestPattern_Type()
)
imaLinkRxTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxTestPattern.setStatus("mandatory")


class _ImaLinkTestProcStatus_Type(Integer32):
    """Custom type imaLinkTestProcStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("linkFail", 3),
          ("operating", 2))
    )


_ImaLinkTestProcStatus_Type.__name__ = "Integer32"
_ImaLinkTestProcStatus_Object = MibTableColumn
imaLinkTestProcStatus = _ImaLinkTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 30),
    _ImaLinkTestProcStatus_Type()
)
imaLinkTestProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTestProcStatus.setStatus("mandatory")
_ImaLinkNumber_Type = Integer32
_ImaLinkNumber_Object = MibTableColumn
imaLinkNumber = _ImaLinkNumber_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 2, 1, 1, 31),
    _ImaLinkNumber_Type()
)
imaLinkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNumber.setStatus("mandatory")
_AtmImaDs1Objects_ObjectIdentity = ObjectIdentity
atmImaDs1Objects = _AtmImaDs1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3)
)
_ImaDs1Table_Object = MibTable
imaDs1Table = _ImaDs1Table_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1)
)
if mibBuilder.loadTexts:
    imaDs1Table.setStatus("mandatory")
_ImaDs1Entry_Object = MibTableRow
imaDs1Entry = _ImaDs1Entry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1)
)
imaDs1Entry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB", "imaDs1GroupIndex"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB", "imaDs1Index"),
)
if mibBuilder.loadTexts:
    imaDs1Entry.setStatus("mandatory")
_ImaDs1Index_Type = Integer32
_ImaDs1Index_Object = MibTableColumn
imaDs1Index = _ImaDs1Index_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 1),
    _ImaDs1Index_Type()
)
imaDs1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1Index.setStatus("mandatory")
_ImaDs1GroupIndex_Type = Integer32
_ImaDs1GroupIndex_Object = MibTableColumn
imaDs1GroupIndex = _ImaDs1GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 2),
    _ImaDs1GroupIndex_Type()
)
imaDs1GroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1GroupIndex.setStatus("mandatory")


class _ImaDs1ConfLoopback_Type(Integer32):
    """Custom type imaDs1ConfLoopback based on Integer32"""
    defaultValue = 1

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
        *(("line", 3),
          ("local", 4),
          ("none", 1),
          ("payload", 2))
    )


_ImaDs1ConfLoopback_Type.__name__ = "Integer32"
_ImaDs1ConfLoopback_Object = MibTableColumn
imaDs1ConfLoopback = _ImaDs1ConfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 3),
    _ImaDs1ConfLoopback_Type()
)
imaDs1ConfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1ConfLoopback.setStatus("mandatory")


class _ImaDs1ConfTxClockSelect_Type(Integer32):
    """Custom type imaDs1ConfTxClockSelect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("recovered", 2))
    )


_ImaDs1ConfTxClockSelect_Type.__name__ = "Integer32"
_ImaDs1ConfTxClockSelect_Object = MibTableColumn
imaDs1ConfTxClockSelect = _ImaDs1ConfTxClockSelect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 4),
    _ImaDs1ConfTxClockSelect_Type()
)
imaDs1ConfTxClockSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1ConfTxClockSelect.setStatus("mandatory")


class _ImaDs1ConfLineCode_Type(Integer32):
    """Custom type imaDs1ConfLineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("b8zs", 1))
    )


_ImaDs1ConfLineCode_Type.__name__ = "Integer32"
_ImaDs1ConfLineCode_Object = MibTableColumn
imaDs1ConfLineCode = _ImaDs1ConfLineCode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 5),
    _ImaDs1ConfLineCode_Type()
)
imaDs1ConfLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1ConfLineCode.setStatus("mandatory")


class _ImaDs1ConfFrameFormat_Type(Integer32):
    """Custom type imaDs1ConfFrameFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("esf", 2),
          ("sf", 1))
    )


_ImaDs1ConfFrameFormat_Type.__name__ = "Integer32"
_ImaDs1ConfFrameFormat_Object = MibTableColumn
imaDs1ConfFrameFormat = _ImaDs1ConfFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 6),
    _ImaDs1ConfFrameFormat_Type()
)
imaDs1ConfFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1ConfFrameFormat.setStatus("mandatory")


class _ImaDs1ConfCableLength_Type(Integer32):
    """Custom type imaDs1ConfCableLength based on Integer32"""
    defaultValue = 1

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("long-haul-0-0-dB", 6),
          ("long-haul-15-0-dB", 8),
          ("long-haul-22-5-dB", 9),
          ("long-haul-7-5-dB", 7),
          ("short-haul-0-133-FT", 1),
          ("short-haul-133-266-FT", 2),
          ("short-haul-266-399-FT", 3),
          ("short-haul-399-533-FT", 4),
          ("short-haul-533-655-FT", 5))
    )


_ImaDs1ConfCableLength_Type.__name__ = "Integer32"
_ImaDs1ConfCableLength_Object = MibTableColumn
imaDs1ConfCableLength = _ImaDs1ConfCableLength_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 7),
    _ImaDs1ConfCableLength_Type()
)
imaDs1ConfCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1ConfCableLength.setStatus("mandatory")
_ImaDs1ConfTxTimingRefLink_Type = Integer32
_ImaDs1ConfTxTimingRefLink_Object = MibTableColumn
imaDs1ConfTxTimingRefLink = _ImaDs1ConfTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 8),
    _ImaDs1ConfTxTimingRefLink_Type()
)
imaDs1ConfTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1ConfTxTimingRefLink.setStatus("mandatory")


class _ImaDs1ConfScramble_Type(Integer32):
    """Custom type imaDs1ConfScramble based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ImaDs1ConfScramble_Type.__name__ = "Integer32"
_ImaDs1ConfScramble_Object = MibTableColumn
imaDs1ConfScramble = _ImaDs1ConfScramble_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 9),
    _ImaDs1ConfScramble_Type()
)
imaDs1ConfScramble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1ConfScramble.setStatus("mandatory")
_ImaDs1StatsNoSignals_Type = Counter32
_ImaDs1StatsNoSignals_Object = MibTableColumn
imaDs1StatsNoSignals = _ImaDs1StatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 10),
    _ImaDs1StatsNoSignals_Type()
)
imaDs1StatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsNoSignals.setStatus("mandatory")
_ImaDs1StatsAISDetects_Type = Counter32
_ImaDs1StatsAISDetects_Object = MibTableColumn
imaDs1StatsAISDetects = _ImaDs1StatsAISDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 11),
    _ImaDs1StatsAISDetects_Type()
)
imaDs1StatsAISDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsAISDetects.setStatus("mandatory")
_ImaDs1StatsYelAlarmCount_Type = Counter32
_ImaDs1StatsYelAlarmCount_Object = MibTableColumn
imaDs1StatsYelAlarmCount = _ImaDs1StatsYelAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 12),
    _ImaDs1StatsYelAlarmCount_Type()
)
imaDs1StatsYelAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsYelAlarmCount.setStatus("mandatory")
_ImaDs1StatsLCVErrors_Type = Counter32
_ImaDs1StatsLCVErrors_Object = MibTableColumn
imaDs1StatsLCVErrors = _ImaDs1StatsLCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 13),
    _ImaDs1StatsLCVErrors_Type()
)
imaDs1StatsLCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsLCVErrors.setStatus("mandatory")
_ImaDs1StatsPCVErrors_Type = Counter32
_ImaDs1StatsPCVErrors_Object = MibTableColumn
imaDs1StatsPCVErrors = _ImaDs1StatsPCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 14),
    _ImaDs1StatsPCVErrors_Type()
)
imaDs1StatsPCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsPCVErrors.setStatus("mandatory")
_ImaDs1StatsMOSErrors_Type = Counter32
_ImaDs1StatsMOSErrors_Object = MibTableColumn
imaDs1StatsMOSErrors = _ImaDs1StatsMOSErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 15),
    _ImaDs1StatsMOSErrors_Type()
)
imaDs1StatsMOSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsMOSErrors.setStatus("mandatory")
_ImaDs1StatsSyncLossCount_Type = Counter32
_ImaDs1StatsSyncLossCount_Object = MibTableColumn
imaDs1StatsSyncLossCount = _ImaDs1StatsSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 16),
    _ImaDs1StatsSyncLossCount_Type()
)
imaDs1StatsSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsSyncLossCount.setStatus("mandatory")
_ImaDs1StatsHECErrors_Type = Counter32
_ImaDs1StatsHECErrors_Object = MibTableColumn
imaDs1StatsHECErrors = _ImaDs1StatsHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 17),
    _ImaDs1StatsHECErrors_Type()
)
imaDs1StatsHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsHECErrors.setStatus("mandatory")


class _ImaDs1StatsSignalLoss_Type(Integer32):
    """Custom type imaDs1StatsSignalLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaDs1StatsSignalLoss_Type.__name__ = "Integer32"
_ImaDs1StatsSignalLoss_Object = MibTableColumn
imaDs1StatsSignalLoss = _ImaDs1StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 18),
    _ImaDs1StatsSignalLoss_Type()
)
imaDs1StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsSignalLoss.setStatus("mandatory")


class _ImaDs1StatsAISDetect_Type(Integer32):
    """Custom type imaDs1StatsAISDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaDs1StatsAISDetect_Type.__name__ = "Integer32"
_ImaDs1StatsAISDetect_Object = MibTableColumn
imaDs1StatsAISDetect = _ImaDs1StatsAISDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 19),
    _ImaDs1StatsAISDetect_Type()
)
imaDs1StatsAISDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsAISDetect.setStatus("mandatory")


class _ImaDs1StatsYellowAlarm_Type(Integer32):
    """Custom type imaDs1StatsYellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaDs1StatsYellowAlarm_Type.__name__ = "Integer32"
_ImaDs1StatsYellowAlarm_Object = MibTableColumn
imaDs1StatsYellowAlarm = _ImaDs1StatsYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 20),
    _ImaDs1StatsYellowAlarm_Type()
)
imaDs1StatsYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsYellowAlarm.setStatus("mandatory")


class _ImaDs1StatsSyncLoss_Type(Integer32):
    """Custom type imaDs1StatsSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaDs1StatsSyncLoss_Type.__name__ = "Integer32"
_ImaDs1StatsSyncLoss_Object = MibTableColumn
imaDs1StatsSyncLoss = _ImaDs1StatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 21),
    _ImaDs1StatsSyncLoss_Type()
)
imaDs1StatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsSyncLoss.setStatus("mandatory")


class _ImaDs1StatsTxClockLoss_Type(Integer32):
    """Custom type imaDs1StatsTxClockLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaDs1StatsTxClockLoss_Type.__name__ = "Integer32"
_ImaDs1StatsTxClockLoss_Object = MibTableColumn
imaDs1StatsTxClockLoss = _ImaDs1StatsTxClockLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 22),
    _ImaDs1StatsTxClockLoss_Type()
)
imaDs1StatsTxClockLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsTxClockLoss.setStatus("mandatory")
_ImaDs1StatsErrSec_Type = Counter32
_ImaDs1StatsErrSec_Object = MibTableColumn
imaDs1StatsErrSec = _ImaDs1StatsErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 23),
    _ImaDs1StatsErrSec_Type()
)
imaDs1StatsErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsErrSec.setStatus("mandatory")
_ImaDs1StatsLineErrSec_Type = Counter32
_ImaDs1StatsLineErrSec_Object = MibTableColumn
imaDs1StatsLineErrSec = _ImaDs1StatsLineErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 24),
    _ImaDs1StatsLineErrSec_Type()
)
imaDs1StatsLineErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsLineErrSec.setStatus("mandatory")
_ImaDs1StatsErrFreeSec_Type = Counter32
_ImaDs1StatsErrFreeSec_Object = MibTableColumn
imaDs1StatsErrFreeSec = _ImaDs1StatsErrFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 25),
    _ImaDs1StatsErrFreeSec_Type()
)
imaDs1StatsErrFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsErrFreeSec.setStatus("mandatory")
_ImaDs1StatsBurstErrSec_Type = Counter32
_ImaDs1StatsBurstErrSec_Object = MibTableColumn
imaDs1StatsBurstErrSec = _ImaDs1StatsBurstErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 26),
    _ImaDs1StatsBurstErrSec_Type()
)
imaDs1StatsBurstErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsBurstErrSec.setStatus("mandatory")
_ImaDs1StatsSevErrSec_Type = Counter32
_ImaDs1StatsSevErrSec_Object = MibTableColumn
imaDs1StatsSevErrSec = _ImaDs1StatsSevErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 27),
    _ImaDs1StatsSevErrSec_Type()
)
imaDs1StatsSevErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsSevErrSec.setStatus("mandatory")
_ImaDs1StatsConSevErrSec_Type = Counter32
_ImaDs1StatsConSevErrSec_Object = MibTableColumn
imaDs1StatsConSevErrSec = _ImaDs1StatsConSevErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 28),
    _ImaDs1StatsConSevErrSec_Type()
)
imaDs1StatsConSevErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsConSevErrSec.setStatus("mandatory")
_ImaDs1StatsFailedSignal_Type = Counter32
_ImaDs1StatsFailedSignal_Object = MibTableColumn
imaDs1StatsFailedSignal = _ImaDs1StatsFailedSignal_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 29),
    _ImaDs1StatsFailedSignal_Type()
)
imaDs1StatsFailedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsFailedSignal.setStatus("mandatory")
_ImaDs1StatsUnavailSec_Type = Counter32
_ImaDs1StatsUnavailSec_Object = MibTableColumn
imaDs1StatsUnavailSec = _ImaDs1StatsUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 30),
    _ImaDs1StatsUnavailSec_Type()
)
imaDs1StatsUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsUnavailSec.setStatus("mandatory")
_ImaDs1StatsSevErrFramSec_Type = Counter32
_ImaDs1StatsSevErrFramSec_Object = MibTableColumn
imaDs1StatsSevErrFramSec = _ImaDs1StatsSevErrFramSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 31),
    _ImaDs1StatsSevErrFramSec_Type()
)
imaDs1StatsSevErrFramSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1StatsSevErrFramSec.setStatus("mandatory")


class _ImaDs1StatsClearCounters_Type(Integer32):
    """Custom type imaDs1StatsClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaDs1StatsClearCounters_Type.__name__ = "Integer32"
_ImaDs1StatsClearCounters_Object = MibTableColumn
imaDs1StatsClearCounters = _ImaDs1StatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 32),
    _ImaDs1StatsClearCounters_Type()
)
imaDs1StatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1StatsClearCounters.setStatus("mandatory")


class _ImaDs1DebugAddr_Type(Integer32):
    """Custom type imaDs1DebugAddr based on Integer32"""
    defaultValue = 0


_ImaDs1DebugAddr_Object = MibTableColumn
imaDs1DebugAddr = _ImaDs1DebugAddr_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 33),
    _ImaDs1DebugAddr_Type()
)
imaDs1DebugAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1DebugAddr.setStatus("mandatory")


class _ImaDs1DebugReadValue_Type(Integer32):
    """Custom type imaDs1DebugReadValue based on Integer32"""
    defaultValue = 0


_ImaDs1DebugReadValue_Object = MibTableColumn
imaDs1DebugReadValue = _ImaDs1DebugReadValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 34),
    _ImaDs1DebugReadValue_Type()
)
imaDs1DebugReadValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1DebugReadValue.setStatus("mandatory")


class _ImaDs1DebugWriteValue_Type(Integer32):
    """Custom type imaDs1DebugWriteValue based on Integer32"""
    defaultValue = 0


_ImaDs1DebugWriteValue_Object = MibTableColumn
imaDs1DebugWriteValue = _ImaDs1DebugWriteValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 35),
    _ImaDs1DebugWriteValue_Type()
)
imaDs1DebugWriteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1DebugWriteValue.setStatus("mandatory")


class _ImaDs1DebugRead_Type(Integer32):
    """Custom type imaDs1DebugRead based on Integer32"""
    defaultValue = 1


_ImaDs1DebugRead_Object = MibTableColumn
imaDs1DebugRead = _ImaDs1DebugRead_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 36),
    _ImaDs1DebugRead_Type()
)
imaDs1DebugRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaDs1DebugRead.setStatus("mandatory")
_ImaDs1PortNumber_Type = Integer32
_ImaDs1PortNumber_Object = MibTableColumn
imaDs1PortNumber = _ImaDs1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 3, 1, 1, 37),
    _ImaDs1PortNumber_Type()
)
imaDs1PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaDs1PortNumber.setStatus("mandatory")
_AtmImaE1Objects_ObjectIdentity = ObjectIdentity
atmImaE1Objects = _AtmImaE1Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4)
)
_ImaE1Table_Object = MibTable
imaE1Table = _ImaE1Table_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1)
)
if mibBuilder.loadTexts:
    imaE1Table.setStatus("mandatory")
_ImaE1Entry_Object = MibTableRow
imaE1Entry = _ImaE1Entry_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1)
)
imaE1Entry.setIndexNames(
    (0, "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB", "imaE1GroupIndex"),
    (0, "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB", "imaE1Index"),
)
if mibBuilder.loadTexts:
    imaE1Entry.setStatus("mandatory")
_ImaE1Index_Type = Integer32
_ImaE1Index_Object = MibTableColumn
imaE1Index = _ImaE1Index_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 1),
    _ImaE1Index_Type()
)
imaE1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1Index.setStatus("mandatory")
_ImaE1GroupIndex_Type = Integer32
_ImaE1GroupIndex_Object = MibTableColumn
imaE1GroupIndex = _ImaE1GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 2),
    _ImaE1GroupIndex_Type()
)
imaE1GroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1GroupIndex.setStatus("mandatory")


class _ImaE1ConfLoopback_Type(Integer32):
    """Custom type imaE1ConfLoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("external", 3),
          ("internal", 2))
    )


_ImaE1ConfLoopback_Type.__name__ = "Integer32"
_ImaE1ConfLoopback_Object = MibTableColumn
imaE1ConfLoopback = _ImaE1ConfLoopback_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 3),
    _ImaE1ConfLoopback_Type()
)
imaE1ConfLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1ConfLoopback.setStatus("mandatory")


class _ImaE1ConfTxClockSelect_Type(Integer32):
    """Custom type imaE1ConfTxClockSelect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("recovered", 2))
    )


_ImaE1ConfTxClockSelect_Type.__name__ = "Integer32"
_ImaE1ConfTxClockSelect_Object = MibTableColumn
imaE1ConfTxClockSelect = _ImaE1ConfTxClockSelect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 4),
    _ImaE1ConfTxClockSelect_Type()
)
imaE1ConfTxClockSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1ConfTxClockSelect.setStatus("mandatory")


class _ImaE1ConfLineCode_Type(Integer32):
    """Custom type imaE1ConfLineCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ami", 2),
          ("hdb3", 1))
    )


_ImaE1ConfLineCode_Type.__name__ = "Integer32"
_ImaE1ConfLineCode_Object = MibTableColumn
imaE1ConfLineCode = _ImaE1ConfLineCode_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 5),
    _ImaE1ConfLineCode_Type()
)
imaE1ConfLineCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1ConfLineCode.setStatus("mandatory")


class _ImaE1ConfFrameFormat_Type(Integer32):
    """Custom type imaE1ConfFrameFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc4-disabled", 2),
          ("crc4-enabled", 1))
    )


_ImaE1ConfFrameFormat_Type.__name__ = "Integer32"
_ImaE1ConfFrameFormat_Object = MibTableColumn
imaE1ConfFrameFormat = _ImaE1ConfFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 6),
    _ImaE1ConfFrameFormat_Type()
)
imaE1ConfFrameFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1ConfFrameFormat.setStatus("mandatory")


class _ImaE1ConfCableLength_Type(Integer32):
    """Custom type imaE1ConfCableLength based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("long-haul", 2),
          ("long-haul-75", 3),
          ("short-haul", 1))
    )


_ImaE1ConfCableLength_Type.__name__ = "Integer32"
_ImaE1ConfCableLength_Object = MibTableColumn
imaE1ConfCableLength = _ImaE1ConfCableLength_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 7),
    _ImaE1ConfCableLength_Type()
)
imaE1ConfCableLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1ConfCableLength.setStatus("mandatory")
_ImaE1ConfTxTimingRefLink_Type = Integer32
_ImaE1ConfTxTimingRefLink_Object = MibTableColumn
imaE1ConfTxTimingRefLink = _ImaE1ConfTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 8),
    _ImaE1ConfTxTimingRefLink_Type()
)
imaE1ConfTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1ConfTxTimingRefLink.setStatus("mandatory")


class _ImaE1ConfScramble_Type(Integer32):
    """Custom type imaE1ConfScramble based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ImaE1ConfScramble_Type.__name__ = "Integer32"
_ImaE1ConfScramble_Object = MibTableColumn
imaE1ConfScramble = _ImaE1ConfScramble_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 9),
    _ImaE1ConfScramble_Type()
)
imaE1ConfScramble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1ConfScramble.setStatus("mandatory")
_ImaE1StatsNoSignals_Type = Counter32
_ImaE1StatsNoSignals_Object = MibTableColumn
imaE1StatsNoSignals = _ImaE1StatsNoSignals_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 10),
    _ImaE1StatsNoSignals_Type()
)
imaE1StatsNoSignals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsNoSignals.setStatus("mandatory")
_ImaE1StatsRAIDetects_Type = Counter32
_ImaE1StatsRAIDetects_Object = MibTableColumn
imaE1StatsRAIDetects = _ImaE1StatsRAIDetects_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 11),
    _ImaE1StatsRAIDetects_Type()
)
imaE1StatsRAIDetects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsRAIDetects.setStatus("mandatory")
_ImaE1StatsFASErrors_Type = Counter32
_ImaE1StatsFASErrors_Object = MibTableColumn
imaE1StatsFASErrors = _ImaE1StatsFASErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 12),
    _ImaE1StatsFASErrors_Type()
)
imaE1StatsFASErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsFASErrors.setStatus("mandatory")
_ImaE1StatsCVErrors_Type = Counter32
_ImaE1StatsCVErrors_Object = MibTableColumn
imaE1StatsCVErrors = _ImaE1StatsCVErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 13),
    _ImaE1StatsCVErrors_Type()
)
imaE1StatsCVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsCVErrors.setStatus("mandatory")
_ImaE1StatsCRCErrors_Type = Counter32
_ImaE1StatsCRCErrors_Object = MibTableColumn
imaE1StatsCRCErrors = _ImaE1StatsCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 14),
    _ImaE1StatsCRCErrors_Type()
)
imaE1StatsCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsCRCErrors.setStatus("mandatory")
_ImaE1StatsEBitErrors_Type = Counter32
_ImaE1StatsEBitErrors_Object = MibTableColumn
imaE1StatsEBitErrors = _ImaE1StatsEBitErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 15),
    _ImaE1StatsEBitErrors_Type()
)
imaE1StatsEBitErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsEBitErrors.setStatus("mandatory")
_ImaE1StatsSyncLossCount_Type = Counter32
_ImaE1StatsSyncLossCount_Object = MibTableColumn
imaE1StatsSyncLossCount = _ImaE1StatsSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 16),
    _ImaE1StatsSyncLossCount_Type()
)
imaE1StatsSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsSyncLossCount.setStatus("mandatory")
_ImaE1StatsHECErrors_Type = Counter32
_ImaE1StatsHECErrors_Object = MibTableColumn
imaE1StatsHECErrors = _ImaE1StatsHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 17),
    _ImaE1StatsHECErrors_Type()
)
imaE1StatsHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsHECErrors.setStatus("mandatory")


class _ImaE1StatsSignalLoss_Type(Integer32):
    """Custom type imaE1StatsSignalLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaE1StatsSignalLoss_Type.__name__ = "Integer32"
_ImaE1StatsSignalLoss_Object = MibTableColumn
imaE1StatsSignalLoss = _ImaE1StatsSignalLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 18),
    _ImaE1StatsSignalLoss_Type()
)
imaE1StatsSignalLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsSignalLoss.setStatus("mandatory")


class _ImaE1StatsRAIDetect_Type(Integer32):
    """Custom type imaE1StatsRAIDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaE1StatsRAIDetect_Type.__name__ = "Integer32"
_ImaE1StatsRAIDetect_Object = MibTableColumn
imaE1StatsRAIDetect = _ImaE1StatsRAIDetect_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 19),
    _ImaE1StatsRAIDetect_Type()
)
imaE1StatsRAIDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsRAIDetect.setStatus("mandatory")


class _ImaE1StatsSyncLoss_Type(Integer32):
    """Custom type imaE1StatsSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaE1StatsSyncLoss_Type.__name__ = "Integer32"
_ImaE1StatsSyncLoss_Object = MibTableColumn
imaE1StatsSyncLoss = _ImaE1StatsSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 20),
    _ImaE1StatsSyncLoss_Type()
)
imaE1StatsSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsSyncLoss.setStatus("mandatory")


class _ImaE1StatsTxClockLoss_Type(Integer32):
    """Custom type imaE1StatsTxClockLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaE1StatsTxClockLoss_Type.__name__ = "Integer32"
_ImaE1StatsTxClockLoss_Object = MibTableColumn
imaE1StatsTxClockLoss = _ImaE1StatsTxClockLoss_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 21),
    _ImaE1StatsTxClockLoss_Type()
)
imaE1StatsTxClockLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsTxClockLoss.setStatus("mandatory")
_ImaE1StatsErrSec_Type = Counter32
_ImaE1StatsErrSec_Object = MibTableColumn
imaE1StatsErrSec = _ImaE1StatsErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 22),
    _ImaE1StatsErrSec_Type()
)
imaE1StatsErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsErrSec.setStatus("mandatory")
_ImaE1StatsLineErrSec_Type = Counter32
_ImaE1StatsLineErrSec_Object = MibTableColumn
imaE1StatsLineErrSec = _ImaE1StatsLineErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 23),
    _ImaE1StatsLineErrSec_Type()
)
imaE1StatsLineErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsLineErrSec.setStatus("mandatory")
_ImaE1StatsErrFreeSec_Type = Counter32
_ImaE1StatsErrFreeSec_Object = MibTableColumn
imaE1StatsErrFreeSec = _ImaE1StatsErrFreeSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 24),
    _ImaE1StatsErrFreeSec_Type()
)
imaE1StatsErrFreeSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsErrFreeSec.setStatus("mandatory")
_ImaE1StatsBurstErrSec_Type = Counter32
_ImaE1StatsBurstErrSec_Object = MibTableColumn
imaE1StatsBurstErrSec = _ImaE1StatsBurstErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 25),
    _ImaE1StatsBurstErrSec_Type()
)
imaE1StatsBurstErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsBurstErrSec.setStatus("mandatory")
_ImaE1StatsSevErrSec_Type = Counter32
_ImaE1StatsSevErrSec_Object = MibTableColumn
imaE1StatsSevErrSec = _ImaE1StatsSevErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 26),
    _ImaE1StatsSevErrSec_Type()
)
imaE1StatsSevErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsSevErrSec.setStatus("mandatory")
_ImaE1StatsConSevErrSec_Type = Counter32
_ImaE1StatsConSevErrSec_Object = MibTableColumn
imaE1StatsConSevErrSec = _ImaE1StatsConSevErrSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 27),
    _ImaE1StatsConSevErrSec_Type()
)
imaE1StatsConSevErrSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsConSevErrSec.setStatus("mandatory")
_ImaE1StatsFailedSignal_Type = Counter32
_ImaE1StatsFailedSignal_Object = MibTableColumn
imaE1StatsFailedSignal = _ImaE1StatsFailedSignal_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 28),
    _ImaE1StatsFailedSignal_Type()
)
imaE1StatsFailedSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsFailedSignal.setStatus("mandatory")
_ImaE1StatsUnavailSec_Type = Counter32
_ImaE1StatsUnavailSec_Object = MibTableColumn
imaE1StatsUnavailSec = _ImaE1StatsUnavailSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 29),
    _ImaE1StatsUnavailSec_Type()
)
imaE1StatsUnavailSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsUnavailSec.setStatus("mandatory")
_ImaE1StatsSevErrFramSec_Type = Counter32
_ImaE1StatsSevErrFramSec_Object = MibTableColumn
imaE1StatsSevErrFramSec = _ImaE1StatsSevErrFramSec_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 30),
    _ImaE1StatsSevErrFramSec_Type()
)
imaE1StatsSevErrFramSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1StatsSevErrFramSec.setStatus("mandatory")


class _ImaE1StatsClearCounters_Type(Integer32):
    """Custom type imaE1StatsClearCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ImaE1StatsClearCounters_Type.__name__ = "Integer32"
_ImaE1StatsClearCounters_Object = MibTableColumn
imaE1StatsClearCounters = _ImaE1StatsClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 31),
    _ImaE1StatsClearCounters_Type()
)
imaE1StatsClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1StatsClearCounters.setStatus("mandatory")


class _ImaE1DebugAddr_Type(Integer32):
    """Custom type imaE1DebugAddr based on Integer32"""
    defaultValue = 0


_ImaE1DebugAddr_Object = MibTableColumn
imaE1DebugAddr = _ImaE1DebugAddr_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 32),
    _ImaE1DebugAddr_Type()
)
imaE1DebugAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1DebugAddr.setStatus("mandatory")


class _ImaE1DebugReadValue_Type(Integer32):
    """Custom type imaE1DebugReadValue based on Integer32"""
    defaultValue = 0


_ImaE1DebugReadValue_Object = MibTableColumn
imaE1DebugReadValue = _ImaE1DebugReadValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 33),
    _ImaE1DebugReadValue_Type()
)
imaE1DebugReadValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1DebugReadValue.setStatus("mandatory")


class _ImaE1DebugWriteValue_Type(Integer32):
    """Custom type imaE1DebugWriteValue based on Integer32"""
    defaultValue = 0


_ImaE1DebugWriteValue_Object = MibTableColumn
imaE1DebugWriteValue = _ImaE1DebugWriteValue_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 34),
    _ImaE1DebugWriteValue_Type()
)
imaE1DebugWriteValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1DebugWriteValue.setStatus("mandatory")


class _ImaE1DebugRead_Type(Integer32):
    """Custom type imaE1DebugRead based on Integer32"""
    defaultValue = 1


_ImaE1DebugRead_Object = MibTableColumn
imaE1DebugRead = _ImaE1DebugRead_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 35),
    _ImaE1DebugRead_Type()
)
imaE1DebugRead.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    imaE1DebugRead.setStatus("mandatory")
_ImaE1PortNumber_Type = Integer32
_ImaE1PortNumber_Object = MibTableColumn
imaE1PortNumber = _ImaE1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2926, 25, 7, 7, 4, 1, 1, 36),
    _ImaE1PortNumber_Type()
)
imaE1PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaE1PortNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONOMASYSTEMS-SONOMA-ATM-IMA-MIB",
    **{"sonomaImaATMAdapterGroup": sonomaImaATMAdapterGroup,
       "atmImaGroupObjects": atmImaGroupObjects,
       "imaGroupNumber": imaGroupNumber,
       "imaGroupTable": imaGroupTable,
       "imaGroupEntry": imaGroupEntry,
       "imaGroupIndex": imaGroupIndex,
       "imaGroupRowStatus": imaGroupRowStatus,
       "imaGroupIfIndex": imaGroupIfIndex,
       "imaGroupNeState": imaGroupNeState,
       "imaGroupFeState": imaGroupFeState,
       "imaGroupFailureStatus": imaGroupFailureStatus,
       "imaGroupSymmetry": imaGroupSymmetry,
       "imaGroupMinNumTxLinks": imaGroupMinNumTxLinks,
       "imaGroupMinNumRxLinks": imaGroupMinNumRxLinks,
       "imaGroupNeTxClkMode": imaGroupNeTxClkMode,
       "imaGroupFeTxClkMode": imaGroupFeTxClkMode,
       "imaGroupTxTimingRefLink": imaGroupTxTimingRefLink,
       "imaGroupRxTimingRefLink": imaGroupRxTimingRefLink,
       "imaGroupLastChange": imaGroupLastChange,
       "imaGroupTxImaId": imaGroupTxImaId,
       "imaGroupRxImaId": imaGroupRxImaId,
       "imaGroupTxFrameLength": imaGroupTxFrameLength,
       "imaGroupRxFrameLength": imaGroupRxFrameLength,
       "imaGroupDiffDelayMax": imaGroupDiffDelayMax,
       "imaGroupLeastDelayLink": imaGroupLeastDelayLink,
       "imaGroupDiffDelayMaxObs": imaGroupDiffDelayMaxObs,
       "imaGroupAlphaValue": imaGroupAlphaValue,
       "imaGroupBetaValue": imaGroupBetaValue,
       "imaGroupGammaValue": imaGroupGammaValue,
       "imaGroupRunningSecs": imaGroupRunningSecs,
       "imaGroupUnavailSecs": imaGroupUnavailSecs,
       "imaGroupNeNumFailures": imaGroupNeNumFailures,
       "imaGroupFeNumFailures": imaGroupFeNumFailures,
       "imaGroupTxAvailCellRate": imaGroupTxAvailCellRate,
       "imaGroupRxAvailCellRate": imaGroupRxAvailCellRate,
       "imaGroupNumTxCfgLnks": imaGroupNumTxCfgLnks,
       "imaGroupNumRxCfgLnks": imaGroupNumRxCfgLnks,
       "imaGroupNumTxActLnks": imaGroupNumTxActLnks,
       "imaGroupNumRxActLnks": imaGroupNumRxActLnks,
       "imaGroupTestLinkIfIndex": imaGroupTestLinkIfIndex,
       "imaGroupTestPattern": imaGroupTestPattern,
       "imaGroupTestProcStatus": imaGroupTestProcStatus,
       "atmImaLinkObjects": atmImaLinkObjects,
       "imaLinkTable": imaLinkTable,
       "imaLinkEntry": imaLinkEntry,
       "imaLinkIfIndex": imaLinkIfIndex,
       "imaLinkRowStatus": imaLinkRowStatus,
       "imaLinkGroupIndex": imaLinkGroupIndex,
       "imaLinkNeTxState": imaLinkNeTxState,
       "imaLinkNeRxState": imaLinkNeRxState,
       "imaLinkFeTxState": imaLinkFeTxState,
       "imaLinkFeRxState": imaLinkFeRxState,
       "imaLinkNeRxFailureStatus": imaLinkNeRxFailureStatus,
       "imaLinkFeRxFailureStatus": imaLinkFeRxFailureStatus,
       "imaLinkTxLid": imaLinkTxLid,
       "imaLinkRxLid": imaLinkRxLid,
       "imaLinkRelDelay": imaLinkRelDelay,
       "imaLinkImaViolations": imaLinkImaViolations,
       "imaLinkOifAnomalies": imaLinkOifAnomalies,
       "imaLinkNeSevErroredSec": imaLinkNeSevErroredSec,
       "imaLinkFeSevErroredSec": imaLinkFeSevErroredSec,
       "imaLinkNeUnavailSec": imaLinkNeUnavailSec,
       "imaLinkFeUnavailSec": imaLinkFeUnavailSec,
       "imaLinkNeTxUnusableSec": imaLinkNeTxUnusableSec,
       "imaLinkNeRxUnusableSec": imaLinkNeRxUnusableSec,
       "imaLinkFeTxUnusableSec": imaLinkFeTxUnusableSec,
       "imaLinkFeRxUnusableSec": imaLinkFeRxUnusableSec,
       "imaLinkNeTxNumFailures": imaLinkNeTxNumFailures,
       "imaLinkNeRxNumFailures": imaLinkNeRxNumFailures,
       "imaLinkFeTxNumFailures": imaLinkFeTxNumFailures,
       "imaLinkFeRxNumFailures": imaLinkFeRxNumFailures,
       "imaLinkTxStuffs": imaLinkTxStuffs,
       "imaLinkRxStuffs": imaLinkRxStuffs,
       "imaLinkRxTestPattern": imaLinkRxTestPattern,
       "imaLinkTestProcStatus": imaLinkTestProcStatus,
       "imaLinkNumber": imaLinkNumber,
       "atmImaDs1Objects": atmImaDs1Objects,
       "imaDs1Table": imaDs1Table,
       "imaDs1Entry": imaDs1Entry,
       "imaDs1Index": imaDs1Index,
       "imaDs1GroupIndex": imaDs1GroupIndex,
       "imaDs1ConfLoopback": imaDs1ConfLoopback,
       "imaDs1ConfTxClockSelect": imaDs1ConfTxClockSelect,
       "imaDs1ConfLineCode": imaDs1ConfLineCode,
       "imaDs1ConfFrameFormat": imaDs1ConfFrameFormat,
       "imaDs1ConfCableLength": imaDs1ConfCableLength,
       "imaDs1ConfTxTimingRefLink": imaDs1ConfTxTimingRefLink,
       "imaDs1ConfScramble": imaDs1ConfScramble,
       "imaDs1StatsNoSignals": imaDs1StatsNoSignals,
       "imaDs1StatsAISDetects": imaDs1StatsAISDetects,
       "imaDs1StatsYelAlarmCount": imaDs1StatsYelAlarmCount,
       "imaDs1StatsLCVErrors": imaDs1StatsLCVErrors,
       "imaDs1StatsPCVErrors": imaDs1StatsPCVErrors,
       "imaDs1StatsMOSErrors": imaDs1StatsMOSErrors,
       "imaDs1StatsSyncLossCount": imaDs1StatsSyncLossCount,
       "imaDs1StatsHECErrors": imaDs1StatsHECErrors,
       "imaDs1StatsSignalLoss": imaDs1StatsSignalLoss,
       "imaDs1StatsAISDetect": imaDs1StatsAISDetect,
       "imaDs1StatsYellowAlarm": imaDs1StatsYellowAlarm,
       "imaDs1StatsSyncLoss": imaDs1StatsSyncLoss,
       "imaDs1StatsTxClockLoss": imaDs1StatsTxClockLoss,
       "imaDs1StatsErrSec": imaDs1StatsErrSec,
       "imaDs1StatsLineErrSec": imaDs1StatsLineErrSec,
       "imaDs1StatsErrFreeSec": imaDs1StatsErrFreeSec,
       "imaDs1StatsBurstErrSec": imaDs1StatsBurstErrSec,
       "imaDs1StatsSevErrSec": imaDs1StatsSevErrSec,
       "imaDs1StatsConSevErrSec": imaDs1StatsConSevErrSec,
       "imaDs1StatsFailedSignal": imaDs1StatsFailedSignal,
       "imaDs1StatsUnavailSec": imaDs1StatsUnavailSec,
       "imaDs1StatsSevErrFramSec": imaDs1StatsSevErrFramSec,
       "imaDs1StatsClearCounters": imaDs1StatsClearCounters,
       "imaDs1DebugAddr": imaDs1DebugAddr,
       "imaDs1DebugReadValue": imaDs1DebugReadValue,
       "imaDs1DebugWriteValue": imaDs1DebugWriteValue,
       "imaDs1DebugRead": imaDs1DebugRead,
       "imaDs1PortNumber": imaDs1PortNumber,
       "atmImaE1Objects": atmImaE1Objects,
       "imaE1Table": imaE1Table,
       "imaE1Entry": imaE1Entry,
       "imaE1Index": imaE1Index,
       "imaE1GroupIndex": imaE1GroupIndex,
       "imaE1ConfLoopback": imaE1ConfLoopback,
       "imaE1ConfTxClockSelect": imaE1ConfTxClockSelect,
       "imaE1ConfLineCode": imaE1ConfLineCode,
       "imaE1ConfFrameFormat": imaE1ConfFrameFormat,
       "imaE1ConfCableLength": imaE1ConfCableLength,
       "imaE1ConfTxTimingRefLink": imaE1ConfTxTimingRefLink,
       "imaE1ConfScramble": imaE1ConfScramble,
       "imaE1StatsNoSignals": imaE1StatsNoSignals,
       "imaE1StatsRAIDetects": imaE1StatsRAIDetects,
       "imaE1StatsFASErrors": imaE1StatsFASErrors,
       "imaE1StatsCVErrors": imaE1StatsCVErrors,
       "imaE1StatsCRCErrors": imaE1StatsCRCErrors,
       "imaE1StatsEBitErrors": imaE1StatsEBitErrors,
       "imaE1StatsSyncLossCount": imaE1StatsSyncLossCount,
       "imaE1StatsHECErrors": imaE1StatsHECErrors,
       "imaE1StatsSignalLoss": imaE1StatsSignalLoss,
       "imaE1StatsRAIDetect": imaE1StatsRAIDetect,
       "imaE1StatsSyncLoss": imaE1StatsSyncLoss,
       "imaE1StatsTxClockLoss": imaE1StatsTxClockLoss,
       "imaE1StatsErrSec": imaE1StatsErrSec,
       "imaE1StatsLineErrSec": imaE1StatsLineErrSec,
       "imaE1StatsErrFreeSec": imaE1StatsErrFreeSec,
       "imaE1StatsBurstErrSec": imaE1StatsBurstErrSec,
       "imaE1StatsSevErrSec": imaE1StatsSevErrSec,
       "imaE1StatsConSevErrSec": imaE1StatsConSevErrSec,
       "imaE1StatsFailedSignal": imaE1StatsFailedSignal,
       "imaE1StatsUnavailSec": imaE1StatsUnavailSec,
       "imaE1StatsSevErrFramSec": imaE1StatsSevErrFramSec,
       "imaE1StatsClearCounters": imaE1StatsClearCounters,
       "imaE1DebugAddr": imaE1DebugAddr,
       "imaE1DebugReadValue": imaE1DebugReadValue,
       "imaE1DebugWriteValue": imaE1DebugWriteValue,
       "imaE1DebugRead": imaE1DebugRead,
       "imaE1PortNumber": imaE1PortNumber}
)
