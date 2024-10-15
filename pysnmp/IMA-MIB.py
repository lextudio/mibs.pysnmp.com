# SNMP MIB module (IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:22 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

atmfImaMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1)
)
atmfImaMib.setRevisions(
        ("1999-02-11 18:30",
         "1997-01-09 22:45")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MilliSeconds(Integer32, TextualConvention):
    status = "current"


class ImaGroupState(Integer32, TextualConvention):
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 8),
          ("configAbortIncompatibleSymmetry", 5),
          ("configAbortOther", 6),
          ("configAbortUnsupportedImaVersion", 10),
          ("configAbortUnsupportedM", 4),
          ("insufficientLinks", 7),
          ("notConfigured", 1),
          ("operational", 9),
          ("startUp", 2),
          ("startUpAck", 3))
    )



class ImaGroupFailureStatus(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("blockedFe", 11),
          ("blockedNe", 10),
          ("failedAssymetricFe", 7),
          ("failedAssymetricNe", 6),
          ("insufficientLinksFe", 9),
          ("insufficientLinksNe", 8),
          ("invalidImaVersionFe", 14),
          ("invalidImaVersionNe", 13),
          ("invalidMValueFe", 5),
          ("invalidMValueNe", 4),
          ("noFailure", 1),
          ("otherFailure", 12),
          ("startUpFe", 3),
          ("startUpNe", 2))
    )



class ImaAlarmStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("declared", 2))
    )



class ImaAlarmType(Integer32, TextualConvention):
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("imaAlarmGroupBlockedFe", 15),
          ("imaAlarmGroupCfgAbort", 11),
          ("imaAlarmGroupCfgAbortFe", 12),
          ("imaAlarmGroupInsuffLinks", 13),
          ("imaAlarmGroupInsuffLinksFe", 14),
          ("imaAlarmGroupStartupFe", 10),
          ("imaAlarmGroupTimingSynch", 16),
          ("imaAlarmLinkLif", 1),
          ("imaAlarmLinkLods", 2),
          ("imaAlarmLinkRfi", 3),
          ("imaAlarmLinkRxFault", 7),
          ("imaAlarmLinkRxMisConnect", 5),
          ("imaAlarmLinkRxUnusableFe", 9),
          ("imaAlarmLinkTxFault", 6),
          ("imaAlarmLinkTxMisConnect", 4),
          ("imaAlarmLinkTxUnusableFe", 8))
    )



class ImaGroupTxClkMode(Integer32, TextualConvention):
    status = "current"
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



class ImaGroupSymmetry(Integer32, TextualConvention):
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
        *(("asymmetricConfiguration", 3),
          ("asymmetricOperation", 2),
          ("symmetricOperation", 1))
    )



class ImaFrameLength(Integer32, TextualConvention):
    status = "current"
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



class ImaLinkState(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("active", 8),
          ("notInGroup", 1),
          ("unusableFailed", 6),
          ("unusableFault", 3),
          ("unusableInhibited", 5),
          ("unusableMisconnected", 4),
          ("unusableNoGivenReason", 2),
          ("usable", 7))
    )



class ImaLinkFailureStatus(Integer32, TextualConvention):
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



class ImaTestProcStatus(Integer32, TextualConvention):
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
        *(("disabled", 1),
          ("linkFail", 3),
          ("operating", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AtmForum_ObjectIdentity = ObjectIdentity
atmForum = _AtmForum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353)
)
_AtmForumNetworkManagement_ObjectIdentity = ObjectIdentity
atmForumNetworkManagement = _AtmForumNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5)
)
_AtmfIma_ObjectIdentity = ObjectIdentity
atmfIma = _AtmfIma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7)
)
_AtmfImaMibObjects_ObjectIdentity = ObjectIdentity
atmfImaMibObjects = _AtmfImaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1)
)


class _ImaGroupNumber_Type(Integer32):
    """Custom type imaGroupNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ImaGroupNumber_Type.__name__ = "Integer32"
_ImaGroupNumber_Object = MibScalar
imaGroupNumber = _ImaGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 1),
    _ImaGroupNumber_Type()
)
imaGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumber.setStatus("current")
_ImaGroupTable_Object = MibTable
imaGroupTable = _ImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    imaGroupTable.setStatus("current")
_ImaGroupEntry_Object = MibTableRow
imaGroupEntry = _ImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1)
)
imaGroupEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaGroupEntry.setStatus("current")


class _ImaGroupIndex_Type(Integer32):
    """Custom type imaGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ImaGroupIndex_Type.__name__ = "Integer32"
_ImaGroupIndex_Object = MibTableColumn
imaGroupIndex = _ImaGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 1),
    _ImaGroupIndex_Type()
)
imaGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaGroupIndex.setStatus("current")
_ImaGroupRowStatus_Type = RowStatus
_ImaGroupRowStatus_Object = MibTableColumn
imaGroupRowStatus = _ImaGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 2),
    _ImaGroupRowStatus_Type()
)
imaGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupRowStatus.setStatus("current")
_ImaGroupIfIndex_Type = InterfaceIndex
_ImaGroupIfIndex_Object = MibTableColumn
imaGroupIfIndex = _ImaGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 3),
    _ImaGroupIfIndex_Type()
)
imaGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIfIndex.setStatus("current")
_ImaGroupNeState_Type = ImaGroupState
_ImaGroupNeState_Object = MibTableColumn
imaGroupNeState = _ImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 4),
    _ImaGroupNeState_Type()
)
imaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNeState.setStatus("current")
_ImaGroupFeState_Type = ImaGroupState
_ImaGroupFeState_Object = MibTableColumn
imaGroupFeState = _ImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 5),
    _ImaGroupFeState_Type()
)
imaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeState.setStatus("current")
_ImaGroupFailureStatus_Type = ImaGroupFailureStatus
_ImaGroupFailureStatus_Object = MibTableColumn
imaGroupFailureStatus = _ImaGroupFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 6),
    _ImaGroupFailureStatus_Type()
)
imaGroupFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFailureStatus.setStatus("current")


class _ImaGroupSymmetry_Type(ImaGroupSymmetry):
    """Custom type imaGroupSymmetry based on ImaGroupSymmetry"""


_ImaGroupSymmetry_Object = MibTableColumn
imaGroupSymmetry = _ImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 7),
    _ImaGroupSymmetry_Type()
)
imaGroupSymmetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupSymmetry.setStatus("current")


class _ImaGroupMinNumTxLinks_Type(Integer32):
    """Custom type imaGroupMinNumTxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ImaGroupMinNumTxLinks_Type.__name__ = "Integer32"
_ImaGroupMinNumTxLinks_Object = MibTableColumn
imaGroupMinNumTxLinks = _ImaGroupMinNumTxLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 8),
    _ImaGroupMinNumTxLinks_Type()
)
imaGroupMinNumTxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupMinNumTxLinks.setStatus("current")


class _ImaGroupMinNumRxLinks_Type(Integer32):
    """Custom type imaGroupMinNumRxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ImaGroupMinNumRxLinks_Type.__name__ = "Integer32"
_ImaGroupMinNumRxLinks_Object = MibTableColumn
imaGroupMinNumRxLinks = _ImaGroupMinNumRxLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 9),
    _ImaGroupMinNumRxLinks_Type()
)
imaGroupMinNumRxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupMinNumRxLinks.setStatus("current")


class _ImaGroupNeTxClkMode_Type(ImaGroupTxClkMode):
    """Custom type imaGroupNeTxClkMode based on ImaGroupTxClkMode"""


_ImaGroupNeTxClkMode_Object = MibTableColumn
imaGroupNeTxClkMode = _ImaGroupNeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 10),
    _ImaGroupNeTxClkMode_Type()
)
imaGroupNeTxClkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupNeTxClkMode.setStatus("current")
_ImaGroupFeTxClkMode_Type = ImaGroupTxClkMode
_ImaGroupFeTxClkMode_Object = MibTableColumn
imaGroupFeTxClkMode = _ImaGroupFeTxClkMode_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 11),
    _ImaGroupFeTxClkMode_Type()
)
imaGroupFeTxClkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeTxClkMode.setStatus("current")
_ImaGroupTxTimingRefLink_Type = InterfaceIndexOrZero
_ImaGroupTxTimingRefLink_Object = MibTableColumn
imaGroupTxTimingRefLink = _ImaGroupTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 12),
    _ImaGroupTxTimingRefLink_Type()
)
imaGroupTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTxTimingRefLink.setStatus("current")
_ImaGroupRxTimingRefLink_Type = InterfaceIndexOrZero
_ImaGroupRxTimingRefLink_Object = MibTableColumn
imaGroupRxTimingRefLink = _ImaGroupRxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 13),
    _ImaGroupRxTimingRefLink_Type()
)
imaGroupRxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxTimingRefLink.setStatus("current")
_ImaGroupLastChange_Type = DateAndTime
_ImaGroupLastChange_Object = MibTableColumn
imaGroupLastChange = _ImaGroupLastChange_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 14),
    _ImaGroupLastChange_Type()
)
imaGroupLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupLastChange.setStatus("current")


class _ImaGroupTxImaId_Type(Integer32):
    """Custom type imaGroupTxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupTxImaId_Type.__name__ = "Integer32"
_ImaGroupTxImaId_Object = MibTableColumn
imaGroupTxImaId = _ImaGroupTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 15),
    _ImaGroupTxImaId_Type()
)
imaGroupTxImaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTxImaId.setStatus("current")


class _ImaGroupRxImaId_Type(Integer32):
    """Custom type imaGroupRxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupRxImaId_Type.__name__ = "Integer32"
_ImaGroupRxImaId_Object = MibTableColumn
imaGroupRxImaId = _ImaGroupRxImaId_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 16),
    _ImaGroupRxImaId_Type()
)
imaGroupRxImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxImaId.setStatus("current")


class _ImaGroupTxFrameLength_Type(ImaFrameLength):
    """Custom type imaGroupTxFrameLength based on ImaFrameLength"""


_ImaGroupTxFrameLength_Object = MibTableColumn
imaGroupTxFrameLength = _ImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 17),
    _ImaGroupTxFrameLength_Type()
)
imaGroupTxFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTxFrameLength.setStatus("current")
_ImaGroupRxFrameLength_Type = ImaFrameLength
_ImaGroupRxFrameLength_Object = MibTableColumn
imaGroupRxFrameLength = _ImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 18),
    _ImaGroupRxFrameLength_Type()
)
imaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxFrameLength.setStatus("current")


class _ImaGroupDiffDelayMax_Type(MilliSeconds):
    """Custom type imaGroupDiffDelayMax based on MilliSeconds"""
    defaultValue = 25


_ImaGroupDiffDelayMax_Object = MibTableColumn
imaGroupDiffDelayMax = _ImaGroupDiffDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 19),
    _ImaGroupDiffDelayMax_Type()
)
imaGroupDiffDelayMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupDiffDelayMax.setStatus("current")
_ImaGroupLeastDelayLink_Type = InterfaceIndexOrZero
_ImaGroupLeastDelayLink_Object = MibTableColumn
imaGroupLeastDelayLink = _ImaGroupLeastDelayLink_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 20),
    _ImaGroupLeastDelayLink_Type()
)
imaGroupLeastDelayLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupLeastDelayLink.setStatus("current")
_ImaGroupDiffDelayMaxObs_Type = MilliSeconds
_ImaGroupDiffDelayMaxObs_Object = MibTableColumn
imaGroupDiffDelayMaxObs = _ImaGroupDiffDelayMaxObs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 21),
    _ImaGroupDiffDelayMaxObs_Type()
)
imaGroupDiffDelayMaxObs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupDiffDelayMaxObs.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 22),
    _ImaGroupAlphaValue_Type()
)
imaGroupAlphaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupAlphaValue.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 23),
    _ImaGroupBetaValue_Type()
)
imaGroupBetaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupBetaValue.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 24),
    _ImaGroupGammaValue_Type()
)
imaGroupGammaValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupGammaValue.setStatus("current")
_ImaGroupRunningSecs_Type = Gauge32
_ImaGroupRunningSecs_Object = MibTableColumn
imaGroupRunningSecs = _ImaGroupRunningSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 25),
    _ImaGroupRunningSecs_Type()
)
imaGroupRunningSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRunningSecs.setStatus("current")
_ImaGroupUnavailSecs_Type = Counter32
_ImaGroupUnavailSecs_Object = MibTableColumn
imaGroupUnavailSecs = _ImaGroupUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 26),
    _ImaGroupUnavailSecs_Type()
)
imaGroupUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupUnavailSecs.setStatus("current")
_ImaGroupNeNumFailures_Type = Counter32
_ImaGroupNeNumFailures_Object = MibTableColumn
imaGroupNeNumFailures = _ImaGroupNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 27),
    _ImaGroupNeNumFailures_Type()
)
imaGroupNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNeNumFailures.setStatus("current")
_ImaGroupFeNumFailures_Type = Counter32
_ImaGroupFeNumFailures_Object = MibTableColumn
imaGroupFeNumFailures = _ImaGroupFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 28),
    _ImaGroupFeNumFailures_Type()
)
imaGroupFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupFeNumFailures.setStatus("current")
_ImaGroupTxAvailCellRate_Type = Gauge32
_ImaGroupTxAvailCellRate_Object = MibTableColumn
imaGroupTxAvailCellRate = _ImaGroupTxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 29),
    _ImaGroupTxAvailCellRate_Type()
)
imaGroupTxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTxAvailCellRate.setStatus("current")
_ImaGroupRxAvailCellRate_Type = Gauge32
_ImaGroupRxAvailCellRate_Object = MibTableColumn
imaGroupRxAvailCellRate = _ImaGroupRxAvailCellRate_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 30),
    _ImaGroupRxAvailCellRate_Type()
)
imaGroupRxAvailCellRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxAvailCellRate.setStatus("current")
_ImaGroupNumTxCfgLinks_Type = Gauge32
_ImaGroupNumTxCfgLinks_Object = MibTableColumn
imaGroupNumTxCfgLinks = _ImaGroupNumTxCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 31),
    _ImaGroupNumTxCfgLinks_Type()
)
imaGroupNumTxCfgLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumTxCfgLinks.setStatus("current")
_ImaGroupNumRxCfgLinks_Type = Gauge32
_ImaGroupNumRxCfgLinks_Object = MibTableColumn
imaGroupNumRxCfgLinks = _ImaGroupNumRxCfgLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 32),
    _ImaGroupNumRxCfgLinks_Type()
)
imaGroupNumRxCfgLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumRxCfgLinks.setStatus("current")
_ImaGroupNumTxActLinks_Type = Gauge32
_ImaGroupNumTxActLinks_Object = MibTableColumn
imaGroupNumTxActLinks = _ImaGroupNumTxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 33),
    _ImaGroupNumTxActLinks_Type()
)
imaGroupNumTxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumTxActLinks.setStatus("current")
_ImaGroupNumRxActLinks_Type = Gauge32
_ImaGroupNumRxActLinks_Object = MibTableColumn
imaGroupNumRxActLinks = _ImaGroupNumRxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 34),
    _ImaGroupNumRxActLinks_Type()
)
imaGroupNumRxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupNumRxActLinks.setStatus("current")


class _ImaGroupTestLinkIfIndex_Type(InterfaceIndexOrZero):
    """Custom type imaGroupTestLinkIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_ImaGroupTestLinkIfIndex_Object = MibTableColumn
imaGroupTestLinkIfIndex = _ImaGroupTestLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 35),
    _ImaGroupTestLinkIfIndex_Type()
)
imaGroupTestLinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTestLinkIfIndex.setStatus("current")


class _ImaGroupTestPattern_Type(Integer32):
    """Custom type imaGroupTestPattern based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_ImaGroupTestPattern_Type.__name__ = "Integer32"
_ImaGroupTestPattern_Object = MibTableColumn
imaGroupTestPattern = _ImaGroupTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 36),
    _ImaGroupTestPattern_Type()
)
imaGroupTestPattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTestPattern.setStatus("current")


class _ImaGroupTestProcStatus_Type(ImaTestProcStatus):
    """Custom type imaGroupTestProcStatus based on ImaTestProcStatus"""


_ImaGroupTestProcStatus_Object = MibTableColumn
imaGroupTestProcStatus = _ImaGroupTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 37),
    _ImaGroupTestProcStatus_Type()
)
imaGroupTestProcStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaGroupTestProcStatus.setStatus("current")


class _ImaGroupValidIntervals_Type(Integer32):
    """Custom type imaGroupValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ImaGroupValidIntervals_Type.__name__ = "Integer32"
_ImaGroupValidIntervals_Object = MibTableColumn
imaGroupValidIntervals = _ImaGroupValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 38),
    _ImaGroupValidIntervals_Type()
)
imaGroupValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupValidIntervals.setStatus("current")


class _ImaGroupInvalidIntervals_Type(Integer32):
    """Custom type imaGroupInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ImaGroupInvalidIntervals_Type.__name__ = "Integer32"
_ImaGroupInvalidIntervals_Object = MibTableColumn
imaGroupInvalidIntervals = _ImaGroupInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 39),
    _ImaGroupInvalidIntervals_Type()
)
imaGroupInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupInvalidIntervals.setStatus("current")


class _ImaGroupTimeElapsed_Type(Integer32):
    """Custom type imaGroupTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_ImaGroupTimeElapsed_Type.__name__ = "Integer32"
_ImaGroupTimeElapsed_Object = MibTableColumn
imaGroupTimeElapsed = _ImaGroupTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 40),
    _ImaGroupTimeElapsed_Type()
)
imaGroupTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTimeElapsed.setStatus("current")


class _ImaGroupTxOamLabelValue_Type(Integer32):
    """Custom type imaGroupTxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ImaGroupTxOamLabelValue_Type.__name__ = "Integer32"
_ImaGroupTxOamLabelValue_Object = MibTableColumn
imaGroupTxOamLabelValue = _ImaGroupTxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 41),
    _ImaGroupTxOamLabelValue_Type()
)
imaGroupTxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTxOamLabelValue.setStatus("current")


class _ImaGroupRxOamLabelValue_Type(Integer32):
    """Custom type imaGroupRxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaGroupRxOamLabelValue_Type.__name__ = "Integer32"
_ImaGroupRxOamLabelValue_Object = MibTableColumn
imaGroupRxOamLabelValue = _ImaGroupRxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 2, 1, 42),
    _ImaGroupRxOamLabelValue_Type()
)
imaGroupRxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupRxOamLabelValue.setStatus("current")
_ImaGroupMappingTable_Object = MibTable
imaGroupMappingTable = _ImaGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    imaGroupMappingTable.setStatus("current")
_ImaGroupMappingEntry_Object = MibTableRow
imaGroupMappingEntry = _ImaGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 3, 1)
)
imaGroupMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    imaGroupMappingEntry.setStatus("current")
_ImaGroupMappingIndex_Type = Integer32
_ImaGroupMappingIndex_Object = MibTableColumn
imaGroupMappingIndex = _ImaGroupMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 3, 1, 1),
    _ImaGroupMappingIndex_Type()
)
imaGroupMappingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupMappingIndex.setStatus("current")
_ImaLinkTable_Object = MibTable
imaLinkTable = _ImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    imaLinkTable.setStatus("current")
_ImaLinkEntry_Object = MibTableRow
imaLinkEntry = _ImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1)
)
imaLinkEntry.setIndexNames(
    (0, "IMA-MIB", "imaLinkIfIndex"),
)
if mibBuilder.loadTexts:
    imaLinkEntry.setStatus("current")
_ImaLinkIfIndex_Type = InterfaceIndex
_ImaLinkIfIndex_Object = MibTableColumn
imaLinkIfIndex = _ImaLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 1),
    _ImaLinkIfIndex_Type()
)
imaLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaLinkIfIndex.setStatus("current")
_ImaLinkRowStatus_Type = RowStatus
_ImaLinkRowStatus_Object = MibTableColumn
imaLinkRowStatus = _ImaLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 2),
    _ImaLinkRowStatus_Type()
)
imaLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkRowStatus.setStatus("current")
_ImaLinkGroupIndex_Type = Integer32
_ImaLinkGroupIndex_Object = MibTableColumn
imaLinkGroupIndex = _ImaLinkGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 3),
    _ImaLinkGroupIndex_Type()
)
imaLinkGroupIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    imaLinkGroupIndex.setStatus("current")
_ImaLinkNeTxState_Type = ImaLinkState
_ImaLinkNeTxState_Object = MibTableColumn
imaLinkNeTxState = _ImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 4),
    _ImaLinkNeTxState_Type()
)
imaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxState.setStatus("current")
_ImaLinkNeRxState_Type = ImaLinkState
_ImaLinkNeRxState_Object = MibTableColumn
imaLinkNeRxState = _ImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 5),
    _ImaLinkNeRxState_Type()
)
imaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxState.setStatus("current")
_ImaLinkFeTxState_Type = ImaLinkState
_ImaLinkFeTxState_Object = MibTableColumn
imaLinkFeTxState = _ImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 6),
    _ImaLinkFeTxState_Type()
)
imaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxState.setStatus("current")
_ImaLinkFeRxState_Type = ImaLinkState
_ImaLinkFeRxState_Object = MibTableColumn
imaLinkFeRxState = _ImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 7),
    _ImaLinkFeRxState_Type()
)
imaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxState.setStatus("current")
_ImaLinkNeRxFailureStatus_Type = ImaLinkFailureStatus
_ImaLinkNeRxFailureStatus_Object = MibTableColumn
imaLinkNeRxFailureStatus = _ImaLinkNeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 8),
    _ImaLinkNeRxFailureStatus_Type()
)
imaLinkNeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxFailureStatus.setStatus("current")
_ImaLinkFeRxFailureStatus_Type = ImaLinkFailureStatus
_ImaLinkFeRxFailureStatus_Object = MibTableColumn
imaLinkFeRxFailureStatus = _ImaLinkFeRxFailureStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 9),
    _ImaLinkFeRxFailureStatus_Type()
)
imaLinkFeRxFailureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxFailureStatus.setStatus("current")


class _ImaLinkTxLid_Type(Integer32):
    """Custom type imaLinkTxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ImaLinkTxLid_Type.__name__ = "Integer32"
_ImaLinkTxLid_Object = MibTableColumn
imaLinkTxLid = _ImaLinkTxLid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 10),
    _ImaLinkTxLid_Type()
)
imaLinkTxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTxLid.setStatus("current")


class _ImaLinkRxLid_Type(Integer32):
    """Custom type imaLinkRxLid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ImaLinkRxLid_Type.__name__ = "Integer32"
_ImaLinkRxLid_Object = MibTableColumn
imaLinkRxLid = _ImaLinkRxLid_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 11),
    _ImaLinkRxLid_Type()
)
imaLinkRxLid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxLid.setStatus("current")
_ImaLinkRelDelay_Type = MilliSeconds
_ImaLinkRelDelay_Object = MibTableColumn
imaLinkRelDelay = _ImaLinkRelDelay_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 12),
    _ImaLinkRelDelay_Type()
)
imaLinkRelDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRelDelay.setStatus("current")
_ImaLinkImaViolations_Type = Counter32
_ImaLinkImaViolations_Object = MibTableColumn
imaLinkImaViolations = _ImaLinkImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 13),
    _ImaLinkImaViolations_Type()
)
imaLinkImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkImaViolations.setStatus("current")
_ImaLinkOifAnomalies_Type = Counter32
_ImaLinkOifAnomalies_Object = MibTableColumn
imaLinkOifAnomalies = _ImaLinkOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 14),
    _ImaLinkOifAnomalies_Type()
)
imaLinkOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkOifAnomalies.setStatus("current")
_ImaLinkNeSevErroredSecs_Type = Counter32
_ImaLinkNeSevErroredSecs_Object = MibTableColumn
imaLinkNeSevErroredSecs = _ImaLinkNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 15),
    _ImaLinkNeSevErroredSecs_Type()
)
imaLinkNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeSevErroredSecs.setStatus("current")
_ImaLinkFeSevErroredSecs_Type = Counter32
_ImaLinkFeSevErroredSecs_Object = MibTableColumn
imaLinkFeSevErroredSecs = _ImaLinkFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 16),
    _ImaLinkFeSevErroredSecs_Type()
)
imaLinkFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeSevErroredSecs.setStatus("current")
_ImaLinkNeUnavailSecs_Type = Counter32
_ImaLinkNeUnavailSecs_Object = MibTableColumn
imaLinkNeUnavailSecs = _ImaLinkNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 17),
    _ImaLinkNeUnavailSecs_Type()
)
imaLinkNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeUnavailSecs.setStatus("current")
_ImaLinkFeUnavailSecs_Type = Counter32
_ImaLinkFeUnavailSecs_Object = MibTableColumn
imaLinkFeUnavailSecs = _ImaLinkFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 18),
    _ImaLinkFeUnavailSecs_Type()
)
imaLinkFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeUnavailSecs.setStatus("current")
_ImaLinkNeTxUnusableSecs_Type = Counter32
_ImaLinkNeTxUnusableSecs_Object = MibTableColumn
imaLinkNeTxUnusableSecs = _ImaLinkNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 19),
    _ImaLinkNeTxUnusableSecs_Type()
)
imaLinkNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxUnusableSecs.setStatus("current")
_ImaLinkNeRxUnusableSecs_Type = Counter32
_ImaLinkNeRxUnusableSecs_Object = MibTableColumn
imaLinkNeRxUnusableSecs = _ImaLinkNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 20),
    _ImaLinkNeRxUnusableSecs_Type()
)
imaLinkNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxUnusableSecs.setStatus("current")
_ImaLinkFeTxUnusableSecs_Type = Counter32
_ImaLinkFeTxUnusableSecs_Object = MibTableColumn
imaLinkFeTxUnusableSecs = _ImaLinkFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 21),
    _ImaLinkFeTxUnusableSecs_Type()
)
imaLinkFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxUnusableSecs.setStatus("current")
_ImaLinkFeRxUnusableSecs_Type = Counter32
_ImaLinkFeRxUnusableSecs_Object = MibTableColumn
imaLinkFeRxUnusableSecs = _ImaLinkFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 22),
    _ImaLinkFeRxUnusableSecs_Type()
)
imaLinkFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxUnusableSecs.setStatus("current")
_ImaLinkNeTxNumFailures_Type = Counter32
_ImaLinkNeTxNumFailures_Object = MibTableColumn
imaLinkNeTxNumFailures = _ImaLinkNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 23),
    _ImaLinkNeTxNumFailures_Type()
)
imaLinkNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeTxNumFailures.setStatus("current")
_ImaLinkNeRxNumFailures_Type = Counter32
_ImaLinkNeRxNumFailures_Object = MibTableColumn
imaLinkNeRxNumFailures = _ImaLinkNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 24),
    _ImaLinkNeRxNumFailures_Type()
)
imaLinkNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkNeRxNumFailures.setStatus("current")
_ImaLinkFeTxNumFailures_Type = Counter32
_ImaLinkFeTxNumFailures_Object = MibTableColumn
imaLinkFeTxNumFailures = _ImaLinkFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 25),
    _ImaLinkFeTxNumFailures_Type()
)
imaLinkFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeTxNumFailures.setStatus("current")
_ImaLinkFeRxNumFailures_Type = Counter32
_ImaLinkFeRxNumFailures_Object = MibTableColumn
imaLinkFeRxNumFailures = _ImaLinkFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 26),
    _ImaLinkFeRxNumFailures_Type()
)
imaLinkFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkFeRxNumFailures.setStatus("current")
_ImaLinkTxStuffs_Type = Counter32
_ImaLinkTxStuffs_Object = MibTableColumn
imaLinkTxStuffs = _ImaLinkTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 27),
    _ImaLinkTxStuffs_Type()
)
imaLinkTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTxStuffs.setStatus("current")
_ImaLinkRxStuffs_Type = Counter32
_ImaLinkRxStuffs_Object = MibTableColumn
imaLinkRxStuffs = _ImaLinkRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 28),
    _ImaLinkRxStuffs_Type()
)
imaLinkRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxStuffs.setStatus("current")


class _ImaLinkRxTestPattern_Type(Integer32):
    """Custom type imaLinkRxTestPattern based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ImaLinkRxTestPattern_Type.__name__ = "Integer32"
_ImaLinkRxTestPattern_Object = MibTableColumn
imaLinkRxTestPattern = _ImaLinkRxTestPattern_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 29),
    _ImaLinkRxTestPattern_Type()
)
imaLinkRxTestPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkRxTestPattern.setStatus("current")
_ImaLinkTestProcStatus_Type = ImaTestProcStatus
_ImaLinkTestProcStatus_Object = MibTableColumn
imaLinkTestProcStatus = _ImaLinkTestProcStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 30),
    _ImaLinkTestProcStatus_Type()
)
imaLinkTestProcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTestProcStatus.setStatus("current")


class _ImaLinkValidIntervals_Type(Integer32):
    """Custom type imaLinkValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ImaLinkValidIntervals_Type.__name__ = "Integer32"
_ImaLinkValidIntervals_Object = MibTableColumn
imaLinkValidIntervals = _ImaLinkValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 31),
    _ImaLinkValidIntervals_Type()
)
imaLinkValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkValidIntervals.setStatus("current")


class _ImaLinkInvalidIntervals_Type(Integer32):
    """Custom type imaLinkInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_ImaLinkInvalidIntervals_Type.__name__ = "Integer32"
_ImaLinkInvalidIntervals_Object = MibTableColumn
imaLinkInvalidIntervals = _ImaLinkInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 32),
    _ImaLinkInvalidIntervals_Type()
)
imaLinkInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkInvalidIntervals.setStatus("current")


class _ImaLinkTimeElapsed_Type(Integer32):
    """Custom type imaLinkTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_ImaLinkTimeElapsed_Type.__name__ = "Integer32"
_ImaLinkTimeElapsed_Object = MibTableColumn
imaLinkTimeElapsed = _ImaLinkTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 4, 1, 33),
    _ImaLinkTimeElapsed_Type()
)
imaLinkTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTimeElapsed.setStatus("current")
_ImaAlarmStatus_Type = ImaAlarmStatus
_ImaAlarmStatus_Object = MibScalar
imaAlarmStatus = _ImaAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 5),
    _ImaAlarmStatus_Type()
)
imaAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaAlarmStatus.setStatus("current")
_ImaAlarmType_Type = ImaAlarmType
_ImaAlarmType_Object = MibScalar
imaAlarmType = _ImaAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 6),
    _ImaAlarmType_Type()
)
imaAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaAlarmType.setStatus("current")
_ImaGroupCurrentTable_Object = MibTable
imaGroupCurrentTable = _ImaGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7)
)
if mibBuilder.loadTexts:
    imaGroupCurrentTable.setStatus("current")
_ImaGroupCurrentEntry_Object = MibTableRow
imaGroupCurrentEntry = _ImaGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1)
)
imaGroupCurrentEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaGroupCurrentEntry.setStatus("current")
_ImaGroupCurrentUnavailSecs_Type = Gauge32
_ImaGroupCurrentUnavailSecs_Object = MibTableColumn
imaGroupCurrentUnavailSecs = _ImaGroupCurrentUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1, 1),
    _ImaGroupCurrentUnavailSecs_Type()
)
imaGroupCurrentUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrentUnavailSecs.setStatus("current")
_ImaGroupCurrentNeNumFailures_Type = Gauge32
_ImaGroupCurrentNeNumFailures_Object = MibTableColumn
imaGroupCurrentNeNumFailures = _ImaGroupCurrentNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1, 2),
    _ImaGroupCurrentNeNumFailures_Type()
)
imaGroupCurrentNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrentNeNumFailures.setStatus("current")
_ImaGroupCurrentFeNumFailures_Type = Gauge32
_ImaGroupCurrentFeNumFailures_Object = MibTableColumn
imaGroupCurrentFeNumFailures = _ImaGroupCurrentFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 7, 1, 3),
    _ImaGroupCurrentFeNumFailures_Type()
)
imaGroupCurrentFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupCurrentFeNumFailures.setStatus("current")
_ImaGroupIntervalTable_Object = MibTable
imaGroupIntervalTable = _ImaGroupIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8)
)
if mibBuilder.loadTexts:
    imaGroupIntervalTable.setStatus("current")
_ImaGroupIntervalEntry_Object = MibTableRow
imaGroupIntervalEntry = _ImaGroupIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1)
)
imaGroupIntervalEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
    (0, "IMA-MIB", "imaGroupIntervalNumber"),
)
if mibBuilder.loadTexts:
    imaGroupIntervalEntry.setStatus("current")


class _ImaGroupIntervalNumber_Type(Integer32):
    """Custom type imaGroupIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ImaGroupIntervalNumber_Type.__name__ = "Integer32"
_ImaGroupIntervalNumber_Object = MibTableColumn
imaGroupIntervalNumber = _ImaGroupIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 1),
    _ImaGroupIntervalNumber_Type()
)
imaGroupIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaGroupIntervalNumber.setStatus("current")
_ImaGroupIntervalUnavailSecs_Type = Gauge32
_ImaGroupIntervalUnavailSecs_Object = MibTableColumn
imaGroupIntervalUnavailSecs = _ImaGroupIntervalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 2),
    _ImaGroupIntervalUnavailSecs_Type()
)
imaGroupIntervalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIntervalUnavailSecs.setStatus("current")
_ImaGroupIntervalNeNumFailures_Type = Gauge32
_ImaGroupIntervalNeNumFailures_Object = MibTableColumn
imaGroupIntervalNeNumFailures = _ImaGroupIntervalNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 3),
    _ImaGroupIntervalNeNumFailures_Type()
)
imaGroupIntervalNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIntervalNeNumFailures.setStatus("current")
_ImaGroupIntervalFeNumFailures_Type = Gauge32
_ImaGroupIntervalFeNumFailures_Object = MibTableColumn
imaGroupIntervalFeNumFailures = _ImaGroupIntervalFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 8, 1, 4),
    _ImaGroupIntervalFeNumFailures_Type()
)
imaGroupIntervalFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupIntervalFeNumFailures.setStatus("current")
_ImaGroupTotalTable_Object = MibTable
imaGroupTotalTable = _ImaGroupTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9)
)
if mibBuilder.loadTexts:
    imaGroupTotalTable.setStatus("current")
_ImaGroupTotalEntry_Object = MibTableRow
imaGroupTotalEntry = _ImaGroupTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1)
)
imaGroupTotalEntry.setIndexNames(
    (0, "IMA-MIB", "imaGroupIndex"),
)
if mibBuilder.loadTexts:
    imaGroupTotalEntry.setStatus("current")
_ImaGroupTotalUnavailSecs_Type = Gauge32
_ImaGroupTotalUnavailSecs_Object = MibTableColumn
imaGroupTotalUnavailSecs = _ImaGroupTotalUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1, 1),
    _ImaGroupTotalUnavailSecs_Type()
)
imaGroupTotalUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTotalUnavailSecs.setStatus("current")
_ImaGroupTotalNeNumFailures_Type = Gauge32
_ImaGroupTotalNeNumFailures_Object = MibTableColumn
imaGroupTotalNeNumFailures = _ImaGroupTotalNeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1, 2),
    _ImaGroupTotalNeNumFailures_Type()
)
imaGroupTotalNeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTotalNeNumFailures.setStatus("current")
_ImaGroupTotalFeNumFailures_Type = Gauge32
_ImaGroupTotalFeNumFailures_Object = MibTableColumn
imaGroupTotalFeNumFailures = _ImaGroupTotalFeNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 9, 1, 3),
    _ImaGroupTotalFeNumFailures_Type()
)
imaGroupTotalFeNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaGroupTotalFeNumFailures.setStatus("current")
_ImaLinkCurrentTable_Object = MibTable
imaLinkCurrentTable = _ImaLinkCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10)
)
if mibBuilder.loadTexts:
    imaLinkCurrentTable.setStatus("current")
_ImaLinkCurrentEntry_Object = MibTableRow
imaLinkCurrentEntry = _ImaLinkCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1)
)
imaLinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    imaLinkCurrentEntry.setStatus("current")
_ImaLinkCurrentImaViolations_Type = Gauge32
_ImaLinkCurrentImaViolations_Object = MibTableColumn
imaLinkCurrentImaViolations = _ImaLinkCurrentImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 1),
    _ImaLinkCurrentImaViolations_Type()
)
imaLinkCurrentImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentImaViolations.setStatus("current")
_ImaLinkCurrentOifAnomalies_Type = Gauge32
_ImaLinkCurrentOifAnomalies_Object = MibTableColumn
imaLinkCurrentOifAnomalies = _ImaLinkCurrentOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 2),
    _ImaLinkCurrentOifAnomalies_Type()
)
imaLinkCurrentOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentOifAnomalies.setStatus("current")
_ImaLinkCurrentNeSevErroredSecs_Type = Gauge32
_ImaLinkCurrentNeSevErroredSecs_Object = MibTableColumn
imaLinkCurrentNeSevErroredSecs = _ImaLinkCurrentNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 3),
    _ImaLinkCurrentNeSevErroredSecs_Type()
)
imaLinkCurrentNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeSevErroredSecs.setStatus("current")
_ImaLinkCurrentFeSevErroredSecs_Type = Gauge32
_ImaLinkCurrentFeSevErroredSecs_Object = MibTableColumn
imaLinkCurrentFeSevErroredSecs = _ImaLinkCurrentFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 4),
    _ImaLinkCurrentFeSevErroredSecs_Type()
)
imaLinkCurrentFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeSevErroredSecs.setStatus("current")
_ImaLinkCurrentNeUnavailSecs_Type = Gauge32
_ImaLinkCurrentNeUnavailSecs_Object = MibTableColumn
imaLinkCurrentNeUnavailSecs = _ImaLinkCurrentNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 5),
    _ImaLinkCurrentNeUnavailSecs_Type()
)
imaLinkCurrentNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeUnavailSecs.setStatus("current")
_ImaLinkCurrentFeUnavailSecs_Type = Gauge32
_ImaLinkCurrentFeUnavailSecs_Object = MibTableColumn
imaLinkCurrentFeUnavailSecs = _ImaLinkCurrentFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 6),
    _ImaLinkCurrentFeUnavailSecs_Type()
)
imaLinkCurrentFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeUnavailSecs.setStatus("current")
_ImaLinkCurrentNeTxUnusableSecs_Type = Gauge32
_ImaLinkCurrentNeTxUnusableSecs_Object = MibTableColumn
imaLinkCurrentNeTxUnusableSecs = _ImaLinkCurrentNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 7),
    _ImaLinkCurrentNeTxUnusableSecs_Type()
)
imaLinkCurrentNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeTxUnusableSecs.setStatus("current")
_ImaLinkCurrentNeRxUnusableSecs_Type = Gauge32
_ImaLinkCurrentNeRxUnusableSecs_Object = MibTableColumn
imaLinkCurrentNeRxUnusableSecs = _ImaLinkCurrentNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 8),
    _ImaLinkCurrentNeRxUnusableSecs_Type()
)
imaLinkCurrentNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeRxUnusableSecs.setStatus("current")
_ImaLinkCurrentFeTxUnusableSecs_Type = Gauge32
_ImaLinkCurrentFeTxUnusableSecs_Object = MibTableColumn
imaLinkCurrentFeTxUnusableSecs = _ImaLinkCurrentFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 9),
    _ImaLinkCurrentFeTxUnusableSecs_Type()
)
imaLinkCurrentFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeTxUnusableSecs.setStatus("current")
_ImaLinkCurrentFeRxUnusableSecs_Type = Gauge32
_ImaLinkCurrentFeRxUnusableSecs_Object = MibTableColumn
imaLinkCurrentFeRxUnusableSecs = _ImaLinkCurrentFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 10),
    _ImaLinkCurrentFeRxUnusableSecs_Type()
)
imaLinkCurrentFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeRxUnusableSecs.setStatus("current")
_ImaLinkCurrentNeTxNumFailures_Type = Gauge32
_ImaLinkCurrentNeTxNumFailures_Object = MibTableColumn
imaLinkCurrentNeTxNumFailures = _ImaLinkCurrentNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 11),
    _ImaLinkCurrentNeTxNumFailures_Type()
)
imaLinkCurrentNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeTxNumFailures.setStatus("current")
_ImaLinkCurrentNeRxNumFailures_Type = Gauge32
_ImaLinkCurrentNeRxNumFailures_Object = MibTableColumn
imaLinkCurrentNeRxNumFailures = _ImaLinkCurrentNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 12),
    _ImaLinkCurrentNeRxNumFailures_Type()
)
imaLinkCurrentNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentNeRxNumFailures.setStatus("current")
_ImaLinkCurrentFeTxNumFailures_Type = Gauge32
_ImaLinkCurrentFeTxNumFailures_Object = MibTableColumn
imaLinkCurrentFeTxNumFailures = _ImaLinkCurrentFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 13),
    _ImaLinkCurrentFeTxNumFailures_Type()
)
imaLinkCurrentFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeTxNumFailures.setStatus("current")
_ImaLinkCurrentFeRxNumFailures_Type = Gauge32
_ImaLinkCurrentFeRxNumFailures_Object = MibTableColumn
imaLinkCurrentFeRxNumFailures = _ImaLinkCurrentFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 14),
    _ImaLinkCurrentFeRxNumFailures_Type()
)
imaLinkCurrentFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentFeRxNumFailures.setStatus("current")
_ImaLinkCurrentTxStuffs_Type = Gauge32
_ImaLinkCurrentTxStuffs_Object = MibTableColumn
imaLinkCurrentTxStuffs = _ImaLinkCurrentTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 15),
    _ImaLinkCurrentTxStuffs_Type()
)
imaLinkCurrentTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentTxStuffs.setStatus("current")
_ImaLinkCurrentRxStuffs_Type = Gauge32
_ImaLinkCurrentRxStuffs_Object = MibTableColumn
imaLinkCurrentRxStuffs = _ImaLinkCurrentRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 10, 1, 16),
    _ImaLinkCurrentRxStuffs_Type()
)
imaLinkCurrentRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkCurrentRxStuffs.setStatus("current")
_ImaLinkIntervalTable_Object = MibTable
imaLinkIntervalTable = _ImaLinkIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11)
)
if mibBuilder.loadTexts:
    imaLinkIntervalTable.setStatus("current")
_ImaLinkIntervalEntry_Object = MibTableRow
imaLinkIntervalEntry = _ImaLinkIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1)
)
imaLinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "IMA-MIB", "imaLinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    imaLinkIntervalEntry.setStatus("current")


class _ImaLinkIntervalNumber_Type(Integer32):
    """Custom type imaLinkIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ImaLinkIntervalNumber_Type.__name__ = "Integer32"
_ImaLinkIntervalNumber_Object = MibTableColumn
imaLinkIntervalNumber = _ImaLinkIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 1),
    _ImaLinkIntervalNumber_Type()
)
imaLinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    imaLinkIntervalNumber.setStatus("current")
_ImaLinkIntervalImaViolations_Type = Gauge32
_ImaLinkIntervalImaViolations_Object = MibTableColumn
imaLinkIntervalImaViolations = _ImaLinkIntervalImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 2),
    _ImaLinkIntervalImaViolations_Type()
)
imaLinkIntervalImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalImaViolations.setStatus("current")
_ImaLinkIntervalOifAnomalies_Type = Gauge32
_ImaLinkIntervalOifAnomalies_Object = MibTableColumn
imaLinkIntervalOifAnomalies = _ImaLinkIntervalOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 3),
    _ImaLinkIntervalOifAnomalies_Type()
)
imaLinkIntervalOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalOifAnomalies.setStatus("current")
_ImaLinkIntervalNeSevErroredSecs_Type = Gauge32
_ImaLinkIntervalNeSevErroredSecs_Object = MibTableColumn
imaLinkIntervalNeSevErroredSecs = _ImaLinkIntervalNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 4),
    _ImaLinkIntervalNeSevErroredSecs_Type()
)
imaLinkIntervalNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeSevErroredSecs.setStatus("current")
_ImaLinkIntervalFeSevErroredSecs_Type = Gauge32
_ImaLinkIntervalFeSevErroredSecs_Object = MibTableColumn
imaLinkIntervalFeSevErroredSecs = _ImaLinkIntervalFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 5),
    _ImaLinkIntervalFeSevErroredSecs_Type()
)
imaLinkIntervalFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeSevErroredSecs.setStatus("current")
_ImaLinkIntervalNeUnavailSecs_Type = Gauge32
_ImaLinkIntervalNeUnavailSecs_Object = MibTableColumn
imaLinkIntervalNeUnavailSecs = _ImaLinkIntervalNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 6),
    _ImaLinkIntervalNeUnavailSecs_Type()
)
imaLinkIntervalNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeUnavailSecs.setStatus("current")
_ImaLinkIntervalFeUnavailSecs_Type = Gauge32
_ImaLinkIntervalFeUnavailSecs_Object = MibTableColumn
imaLinkIntervalFeUnavailSecs = _ImaLinkIntervalFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 7),
    _ImaLinkIntervalFeUnavailSecs_Type()
)
imaLinkIntervalFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeUnavailSecs.setStatus("current")
_ImaLinkIntervalNeTxUnusableSecs_Type = Gauge32
_ImaLinkIntervalNeTxUnusableSecs_Object = MibTableColumn
imaLinkIntervalNeTxUnusableSecs = _ImaLinkIntervalNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 8),
    _ImaLinkIntervalNeTxUnusableSecs_Type()
)
imaLinkIntervalNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeTxUnusableSecs.setStatus("current")
_ImaLinkIntervalNeRxUnusableSecs_Type = Gauge32
_ImaLinkIntervalNeRxUnusableSecs_Object = MibTableColumn
imaLinkIntervalNeRxUnusableSecs = _ImaLinkIntervalNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 9),
    _ImaLinkIntervalNeRxUnusableSecs_Type()
)
imaLinkIntervalNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeRxUnusableSecs.setStatus("current")
_ImaLinkIntervalFeTxUnusableSecs_Type = Gauge32
_ImaLinkIntervalFeTxUnusableSecs_Object = MibTableColumn
imaLinkIntervalFeTxUnusableSecs = _ImaLinkIntervalFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 10),
    _ImaLinkIntervalFeTxUnusableSecs_Type()
)
imaLinkIntervalFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeTxUnusableSecs.setStatus("current")
_ImaLinkIntervalFeRxUnusableSecs_Type = Gauge32
_ImaLinkIntervalFeRxUnusableSecs_Object = MibTableColumn
imaLinkIntervalFeRxUnusableSecs = _ImaLinkIntervalFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 11),
    _ImaLinkIntervalFeRxUnusableSecs_Type()
)
imaLinkIntervalFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeRxUnusableSecs.setStatus("current")
_ImaLinkIntervalNeTxNumFailures_Type = Gauge32
_ImaLinkIntervalNeTxNumFailures_Object = MibTableColumn
imaLinkIntervalNeTxNumFailures = _ImaLinkIntervalNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 12),
    _ImaLinkIntervalNeTxNumFailures_Type()
)
imaLinkIntervalNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeTxNumFailures.setStatus("current")
_ImaLinkIntervalNeRxNumFailures_Type = Gauge32
_ImaLinkIntervalNeRxNumFailures_Object = MibTableColumn
imaLinkIntervalNeRxNumFailures = _ImaLinkIntervalNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 13),
    _ImaLinkIntervalNeRxNumFailures_Type()
)
imaLinkIntervalNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalNeRxNumFailures.setStatus("current")
_ImaLinkIntervalFeTxNumFailures_Type = Gauge32
_ImaLinkIntervalFeTxNumFailures_Object = MibTableColumn
imaLinkIntervalFeTxNumFailures = _ImaLinkIntervalFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 14),
    _ImaLinkIntervalFeTxNumFailures_Type()
)
imaLinkIntervalFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeTxNumFailures.setStatus("current")
_ImaLinkIntervalFeRxNumFailures_Type = Gauge32
_ImaLinkIntervalFeRxNumFailures_Object = MibTableColumn
imaLinkIntervalFeRxNumFailures = _ImaLinkIntervalFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 15),
    _ImaLinkIntervalFeRxNumFailures_Type()
)
imaLinkIntervalFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalFeRxNumFailures.setStatus("current")
_ImaLinkIntervalTxStuffs_Type = Gauge32
_ImaLinkIntervalTxStuffs_Object = MibTableColumn
imaLinkIntervalTxStuffs = _ImaLinkIntervalTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 16),
    _ImaLinkIntervalTxStuffs_Type()
)
imaLinkIntervalTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalTxStuffs.setStatus("current")
_ImaLinkIntervalRxStuffs_Type = Gauge32
_ImaLinkIntervalRxStuffs_Object = MibTableColumn
imaLinkIntervalRxStuffs = _ImaLinkIntervalRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 11, 1, 17),
    _ImaLinkIntervalRxStuffs_Type()
)
imaLinkIntervalRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkIntervalRxStuffs.setStatus("current")
_ImaLinkTotalTable_Object = MibTable
imaLinkTotalTable = _ImaLinkTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12)
)
if mibBuilder.loadTexts:
    imaLinkTotalTable.setStatus("current")
_ImaLinkTotalEntry_Object = MibTableRow
imaLinkTotalEntry = _ImaLinkTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1)
)
imaLinkTotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    imaLinkTotalEntry.setStatus("current")
_ImaLinkTotalImaViolations_Type = Gauge32
_ImaLinkTotalImaViolations_Object = MibTableColumn
imaLinkTotalImaViolations = _ImaLinkTotalImaViolations_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 1),
    _ImaLinkTotalImaViolations_Type()
)
imaLinkTotalImaViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalImaViolations.setStatus("current")
_ImaLinkTotalOifAnomalies_Type = Gauge32
_ImaLinkTotalOifAnomalies_Object = MibTableColumn
imaLinkTotalOifAnomalies = _ImaLinkTotalOifAnomalies_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 2),
    _ImaLinkTotalOifAnomalies_Type()
)
imaLinkTotalOifAnomalies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalOifAnomalies.setStatus("current")
_ImaLinkTotalNeSevErroredSecs_Type = Gauge32
_ImaLinkTotalNeSevErroredSecs_Object = MibTableColumn
imaLinkTotalNeSevErroredSecs = _ImaLinkTotalNeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 3),
    _ImaLinkTotalNeSevErroredSecs_Type()
)
imaLinkTotalNeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalNeSevErroredSecs.setStatus("current")
_ImaLinkTotalFeSevErroredSecs_Type = Gauge32
_ImaLinkTotalFeSevErroredSecs_Object = MibTableColumn
imaLinkTotalFeSevErroredSecs = _ImaLinkTotalFeSevErroredSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 4),
    _ImaLinkTotalFeSevErroredSecs_Type()
)
imaLinkTotalFeSevErroredSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalFeSevErroredSecs.setStatus("current")
_ImaLinkTotalNeUnavailSecs_Type = Gauge32
_ImaLinkTotalNeUnavailSecs_Object = MibTableColumn
imaLinkTotalNeUnavailSecs = _ImaLinkTotalNeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 5),
    _ImaLinkTotalNeUnavailSecs_Type()
)
imaLinkTotalNeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalNeUnavailSecs.setStatus("current")
_ImaLinkTotalFeUnavailSecs_Type = Gauge32
_ImaLinkTotalFeUnavailSecs_Object = MibTableColumn
imaLinkTotalFeUnavailSecs = _ImaLinkTotalFeUnavailSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 6),
    _ImaLinkTotalFeUnavailSecs_Type()
)
imaLinkTotalFeUnavailSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalFeUnavailSecs.setStatus("current")
_ImaLinkTotalNeTxUnusableSecs_Type = Gauge32
_ImaLinkTotalNeTxUnusableSecs_Object = MibTableColumn
imaLinkTotalNeTxUnusableSecs = _ImaLinkTotalNeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 7),
    _ImaLinkTotalNeTxUnusableSecs_Type()
)
imaLinkTotalNeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalNeTxUnusableSecs.setStatus("current")
_ImaLinkTotalNeRxUnusableSecs_Type = Gauge32
_ImaLinkTotalNeRxUnusableSecs_Object = MibTableColumn
imaLinkTotalNeRxUnusableSecs = _ImaLinkTotalNeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 8),
    _ImaLinkTotalNeRxUnusableSecs_Type()
)
imaLinkTotalNeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalNeRxUnusableSecs.setStatus("current")
_ImaLinkTotalFeTxUnusableSecs_Type = Gauge32
_ImaLinkTotalFeTxUnusableSecs_Object = MibTableColumn
imaLinkTotalFeTxUnusableSecs = _ImaLinkTotalFeTxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 9),
    _ImaLinkTotalFeTxUnusableSecs_Type()
)
imaLinkTotalFeTxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalFeTxUnusableSecs.setStatus("current")
_ImaLinkTotalFeRxUnusableSecs_Type = Gauge32
_ImaLinkTotalFeRxUnusableSecs_Object = MibTableColumn
imaLinkTotalFeRxUnusableSecs = _ImaLinkTotalFeRxUnusableSecs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 10),
    _ImaLinkTotalFeRxUnusableSecs_Type()
)
imaLinkTotalFeRxUnusableSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalFeRxUnusableSecs.setStatus("current")
_ImaLinkTotalNeTxNumFailures_Type = Gauge32
_ImaLinkTotalNeTxNumFailures_Object = MibTableColumn
imaLinkTotalNeTxNumFailures = _ImaLinkTotalNeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 11),
    _ImaLinkTotalNeTxNumFailures_Type()
)
imaLinkTotalNeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalNeTxNumFailures.setStatus("current")
_ImaLinkTotalNeRxNumFailures_Type = Gauge32
_ImaLinkTotalNeRxNumFailures_Object = MibTableColumn
imaLinkTotalNeRxNumFailures = _ImaLinkTotalNeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 12),
    _ImaLinkTotalNeRxNumFailures_Type()
)
imaLinkTotalNeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalNeRxNumFailures.setStatus("current")
_ImaLinkTotalFeTxNumFailures_Type = Gauge32
_ImaLinkTotalFeTxNumFailures_Object = MibTableColumn
imaLinkTotalFeTxNumFailures = _ImaLinkTotalFeTxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 13),
    _ImaLinkTotalFeTxNumFailures_Type()
)
imaLinkTotalFeTxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalFeTxNumFailures.setStatus("current")
_ImaLinkTotalFeRxNumFailures_Type = Gauge32
_ImaLinkTotalFeRxNumFailures_Object = MibTableColumn
imaLinkTotalFeRxNumFailures = _ImaLinkTotalFeRxNumFailures_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 14),
    _ImaLinkTotalFeRxNumFailures_Type()
)
imaLinkTotalFeRxNumFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalFeRxNumFailures.setStatus("current")
_ImaLinkTotalTxStuffs_Type = Gauge32
_ImaLinkTotalTxStuffs_Object = MibTableColumn
imaLinkTotalTxStuffs = _ImaLinkTotalTxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 15),
    _ImaLinkTotalTxStuffs_Type()
)
imaLinkTotalTxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalTxStuffs.setStatus("current")
_ImaLinkTotalRxStuffs_Type = Gauge32
_ImaLinkTotalRxStuffs_Object = MibTableColumn
imaLinkTotalRxStuffs = _ImaLinkTotalRxStuffs_Object(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 1, 12, 1, 16),
    _ImaLinkTotalRxStuffs_Type()
)
imaLinkTotalRxStuffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    imaLinkTotalRxStuffs.setStatus("current")
_AtmfImaMibTraps_ObjectIdentity = ObjectIdentity
atmfImaMibTraps = _AtmfImaMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2)
)
_AtmfImaMibTrapPrefix_ObjectIdentity = ObjectIdentity
atmfImaMibTrapPrefix = _AtmfImaMibTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0)
)
_AtmfImaMibConformance_ObjectIdentity = ObjectIdentity
atmfImaMibConformance = _AtmfImaMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3)
)
_AtmfImaMibGroups_ObjectIdentity = ObjectIdentity
atmfImaMibGroups = _AtmfImaMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1)
)
_AtmfImaMibCompliances_ObjectIdentity = ObjectIdentity
atmfImaMibCompliances = _AtmfImaMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 2)
)

# Managed Objects groups

imaGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 1)
)
imaGroupGroup.setObjects(
      *(("IMA-MIB", "imaGroupNumber"),
        ("IMA-MIB", "imaGroupRowStatus"),
        ("IMA-MIB", "imaGroupIfIndex"),
        ("IMA-MIB", "imaGroupNeState"),
        ("IMA-MIB", "imaGroupFeState"),
        ("IMA-MIB", "imaGroupFailureStatus"),
        ("IMA-MIB", "imaGroupSymmetry"),
        ("IMA-MIB", "imaGroupMinNumTxLinks"),
        ("IMA-MIB", "imaGroupMinNumRxLinks"),
        ("IMA-MIB", "imaGroupNeTxClkMode"),
        ("IMA-MIB", "imaGroupFeTxClkMode"),
        ("IMA-MIB", "imaGroupTxTimingRefLink"),
        ("IMA-MIB", "imaGroupRxTimingRefLink"),
        ("IMA-MIB", "imaGroupLastChange"),
        ("IMA-MIB", "imaGroupTxImaId"),
        ("IMA-MIB", "imaGroupRxImaId"),
        ("IMA-MIB", "imaGroupTxFrameLength"),
        ("IMA-MIB", "imaGroupRxFrameLength"),
        ("IMA-MIB", "imaGroupDiffDelayMax"),
        ("IMA-MIB", "imaGroupLeastDelayLink"),
        ("IMA-MIB", "imaGroupDiffDelayMaxObs"),
        ("IMA-MIB", "imaGroupAlphaValue"),
        ("IMA-MIB", "imaGroupBetaValue"),
        ("IMA-MIB", "imaGroupGammaValue"),
        ("IMA-MIB", "imaGroupRunningSecs"),
        ("IMA-MIB", "imaGroupUnavailSecs"),
        ("IMA-MIB", "imaGroupNeNumFailures"),
        ("IMA-MIB", "imaGroupFeNumFailures"),
        ("IMA-MIB", "imaGroupTxAvailCellRate"),
        ("IMA-MIB", "imaGroupRxAvailCellRate"),
        ("IMA-MIB", "imaGroupNumTxCfgLinks"),
        ("IMA-MIB", "imaGroupNumRxCfgLinks"),
        ("IMA-MIB", "imaGroupNumTxActLinks"),
        ("IMA-MIB", "imaGroupNumRxActLinks"),
        ("IMA-MIB", "imaGroupTxOamLabelValue"),
        ("IMA-MIB", "imaGroupRxOamLabelValue"))
)
if mibBuilder.loadTexts:
    imaGroupGroup.setStatus("current")

imaLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 2)
)
imaLinkGroup.setObjects(
      *(("IMA-MIB", "imaLinkRowStatus"),
        ("IMA-MIB", "imaLinkGroupIndex"),
        ("IMA-MIB", "imaLinkNeTxState"),
        ("IMA-MIB", "imaLinkNeRxState"),
        ("IMA-MIB", "imaLinkFeTxState"),
        ("IMA-MIB", "imaLinkFeRxState"),
        ("IMA-MIB", "imaLinkNeRxFailureStatus"),
        ("IMA-MIB", "imaLinkFeRxFailureStatus"),
        ("IMA-MIB", "imaLinkTxLid"),
        ("IMA-MIB", "imaLinkRxLid"),
        ("IMA-MIB", "imaLinkRelDelay"),
        ("IMA-MIB", "imaLinkImaViolations"),
        ("IMA-MIB", "imaLinkOifAnomalies"),
        ("IMA-MIB", "imaLinkNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkNeUnavailSecs"),
        ("IMA-MIB", "imaLinkFeUnavailSecs"),
        ("IMA-MIB", "imaLinkNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkNeTxNumFailures"),
        ("IMA-MIB", "imaLinkNeRxNumFailures"),
        ("IMA-MIB", "imaLinkFeTxNumFailures"),
        ("IMA-MIB", "imaLinkFeRxNumFailures"),
        ("IMA-MIB", "imaLinkTxStuffs"),
        ("IMA-MIB", "imaLinkRxStuffs"))
)
if mibBuilder.loadTexts:
    imaLinkGroup.setStatus("current")

imaGroupMappingTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 3)
)
imaGroupMappingTableGroup.setObjects(
    ("IMA-MIB", "imaGroupMappingIndex")
)
if mibBuilder.loadTexts:
    imaGroupMappingTableGroup.setStatus("current")

imaTestPatternGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 4)
)
imaTestPatternGroup.setObjects(
      *(("IMA-MIB", "imaGroupTestLinkIfIndex"),
        ("IMA-MIB", "imaGroupTestPattern"),
        ("IMA-MIB", "imaGroupTestProcStatus"),
        ("IMA-MIB", "imaLinkRxTestPattern"),
        ("IMA-MIB", "imaLinkTestProcStatus"))
)
if mibBuilder.loadTexts:
    imaTestPatternGroup.setStatus("current")

imaAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 5)
)
imaAlarmGroup.setObjects(
      *(("IMA-MIB", "imaAlarmStatus"),
        ("IMA-MIB", "imaAlarmType"))
)
if mibBuilder.loadTexts:
    imaAlarmGroup.setStatus("current")

imaGroupIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 6)
)
imaGroupIntervalGroup.setObjects(
      *(("IMA-MIB", "imaGroupValidIntervals"),
        ("IMA-MIB", "imaGroupInvalidIntervals"),
        ("IMA-MIB", "imaGroupTimeElapsed"),
        ("IMA-MIB", "imaGroupCurrentUnavailSecs"),
        ("IMA-MIB", "imaGroupCurrentNeNumFailures"),
        ("IMA-MIB", "imaGroupCurrentFeNumFailures"),
        ("IMA-MIB", "imaGroupIntervalUnavailSecs"),
        ("IMA-MIB", "imaGroupIntervalNeNumFailures"),
        ("IMA-MIB", "imaGroupIntervalFeNumFailures"),
        ("IMA-MIB", "imaGroupTotalUnavailSecs"),
        ("IMA-MIB", "imaGroupTotalNeNumFailures"),
        ("IMA-MIB", "imaGroupTotalFeNumFailures"))
)
if mibBuilder.loadTexts:
    imaGroupIntervalGroup.setStatus("current")

imaLinkIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 7)
)
imaLinkIntervalGroup.setObjects(
      *(("IMA-MIB", "imaLinkValidIntervals"),
        ("IMA-MIB", "imaLinkInvalidIntervals"),
        ("IMA-MIB", "imaLinkTimeElapsed"),
        ("IMA-MIB", "imaLinkCurrentImaViolations"),
        ("IMA-MIB", "imaLinkCurrentOifAnomalies"),
        ("IMA-MIB", "imaLinkCurrentNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrentFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkCurrentNeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrentFeUnavailSecs"),
        ("IMA-MIB", "imaLinkCurrentNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkCurrentNeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentNeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentFeTxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentFeRxNumFailures"),
        ("IMA-MIB", "imaLinkCurrentTxStuffs"),
        ("IMA-MIB", "imaLinkCurrentRxStuffs"),
        ("IMA-MIB", "imaLinkIntervalImaViolations"),
        ("IMA-MIB", "imaLinkIntervalOifAnomalies"),
        ("IMA-MIB", "imaLinkIntervalNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkIntervalFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkIntervalNeUnavailSecs"),
        ("IMA-MIB", "imaLinkIntervalFeUnavailSecs"),
        ("IMA-MIB", "imaLinkIntervalNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkIntervalNeTxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalNeRxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalFeTxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalFeRxNumFailures"),
        ("IMA-MIB", "imaLinkIntervalTxStuffs"),
        ("IMA-MIB", "imaLinkIntervalRxStuffs"),
        ("IMA-MIB", "imaLinkTotalImaViolations"),
        ("IMA-MIB", "imaLinkTotalOifAnomalies"),
        ("IMA-MIB", "imaLinkTotalNeSevErroredSecs"),
        ("IMA-MIB", "imaLinkTotalFeSevErroredSecs"),
        ("IMA-MIB", "imaLinkTotalNeUnavailSecs"),
        ("IMA-MIB", "imaLinkTotalFeUnavailSecs"),
        ("IMA-MIB", "imaLinkTotalNeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkTotalNeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkTotalFeTxUnusableSecs"),
        ("IMA-MIB", "imaLinkTotalFeRxUnusableSecs"),
        ("IMA-MIB", "imaLinkTotalNeTxNumFailures"),
        ("IMA-MIB", "imaLinkTotalNeRxNumFailures"),
        ("IMA-MIB", "imaLinkTotalFeTxNumFailures"),
        ("IMA-MIB", "imaLinkTotalFeRxNumFailures"),
        ("IMA-MIB", "imaLinkTotalTxStuffs"),
        ("IMA-MIB", "imaLinkTotalRxStuffs"))
)
if mibBuilder.loadTexts:
    imaLinkIntervalGroup.setStatus("current")


# Notification objects

imaFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 2, 0, 1)
)
imaFailureAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IMA-MIB", "imaAlarmStatus"),
        ("IMA-MIB", "imaAlarmType"))
)
if mibBuilder.loadTexts:
    imaFailureAlarm.setStatus(
        "current"
    )


# Notifications groups

imaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 1, 8)
)
imaNotificationsGroup.setObjects(
    ("IMA-MIB", "imaFailureAlarm")
)
if mibBuilder.loadTexts:
    imaNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

atmfImaMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 353, 5, 7, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    atmfImaMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IMA-MIB",
    **{"MilliSeconds": MilliSeconds,
       "ImaGroupState": ImaGroupState,
       "ImaGroupFailureStatus": ImaGroupFailureStatus,
       "ImaAlarmStatus": ImaAlarmStatus,
       "ImaAlarmType": ImaAlarmType,
       "ImaGroupTxClkMode": ImaGroupTxClkMode,
       "ImaGroupSymmetry": ImaGroupSymmetry,
       "ImaFrameLength": ImaFrameLength,
       "ImaLinkState": ImaLinkState,
       "ImaLinkFailureStatus": ImaLinkFailureStatus,
       "ImaTestProcStatus": ImaTestProcStatus,
       "atmForum": atmForum,
       "atmForumNetworkManagement": atmForumNetworkManagement,
       "atmfIma": atmfIma,
       "atmfImaMib": atmfImaMib,
       "atmfImaMibObjects": atmfImaMibObjects,
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
       "imaGroupNumTxCfgLinks": imaGroupNumTxCfgLinks,
       "imaGroupNumRxCfgLinks": imaGroupNumRxCfgLinks,
       "imaGroupNumTxActLinks": imaGroupNumTxActLinks,
       "imaGroupNumRxActLinks": imaGroupNumRxActLinks,
       "imaGroupTestLinkIfIndex": imaGroupTestLinkIfIndex,
       "imaGroupTestPattern": imaGroupTestPattern,
       "imaGroupTestProcStatus": imaGroupTestProcStatus,
       "imaGroupValidIntervals": imaGroupValidIntervals,
       "imaGroupInvalidIntervals": imaGroupInvalidIntervals,
       "imaGroupTimeElapsed": imaGroupTimeElapsed,
       "imaGroupTxOamLabelValue": imaGroupTxOamLabelValue,
       "imaGroupRxOamLabelValue": imaGroupRxOamLabelValue,
       "imaGroupMappingTable": imaGroupMappingTable,
       "imaGroupMappingEntry": imaGroupMappingEntry,
       "imaGroupMappingIndex": imaGroupMappingIndex,
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
       "imaLinkNeSevErroredSecs": imaLinkNeSevErroredSecs,
       "imaLinkFeSevErroredSecs": imaLinkFeSevErroredSecs,
       "imaLinkNeUnavailSecs": imaLinkNeUnavailSecs,
       "imaLinkFeUnavailSecs": imaLinkFeUnavailSecs,
       "imaLinkNeTxUnusableSecs": imaLinkNeTxUnusableSecs,
       "imaLinkNeRxUnusableSecs": imaLinkNeRxUnusableSecs,
       "imaLinkFeTxUnusableSecs": imaLinkFeTxUnusableSecs,
       "imaLinkFeRxUnusableSecs": imaLinkFeRxUnusableSecs,
       "imaLinkNeTxNumFailures": imaLinkNeTxNumFailures,
       "imaLinkNeRxNumFailures": imaLinkNeRxNumFailures,
       "imaLinkFeTxNumFailures": imaLinkFeTxNumFailures,
       "imaLinkFeRxNumFailures": imaLinkFeRxNumFailures,
       "imaLinkTxStuffs": imaLinkTxStuffs,
       "imaLinkRxStuffs": imaLinkRxStuffs,
       "imaLinkRxTestPattern": imaLinkRxTestPattern,
       "imaLinkTestProcStatus": imaLinkTestProcStatus,
       "imaLinkValidIntervals": imaLinkValidIntervals,
       "imaLinkInvalidIntervals": imaLinkInvalidIntervals,
       "imaLinkTimeElapsed": imaLinkTimeElapsed,
       "imaAlarmStatus": imaAlarmStatus,
       "imaAlarmType": imaAlarmType,
       "imaGroupCurrentTable": imaGroupCurrentTable,
       "imaGroupCurrentEntry": imaGroupCurrentEntry,
       "imaGroupCurrentUnavailSecs": imaGroupCurrentUnavailSecs,
       "imaGroupCurrentNeNumFailures": imaGroupCurrentNeNumFailures,
       "imaGroupCurrentFeNumFailures": imaGroupCurrentFeNumFailures,
       "imaGroupIntervalTable": imaGroupIntervalTable,
       "imaGroupIntervalEntry": imaGroupIntervalEntry,
       "imaGroupIntervalNumber": imaGroupIntervalNumber,
       "imaGroupIntervalUnavailSecs": imaGroupIntervalUnavailSecs,
       "imaGroupIntervalNeNumFailures": imaGroupIntervalNeNumFailures,
       "imaGroupIntervalFeNumFailures": imaGroupIntervalFeNumFailures,
       "imaGroupTotalTable": imaGroupTotalTable,
       "imaGroupTotalEntry": imaGroupTotalEntry,
       "imaGroupTotalUnavailSecs": imaGroupTotalUnavailSecs,
       "imaGroupTotalNeNumFailures": imaGroupTotalNeNumFailures,
       "imaGroupTotalFeNumFailures": imaGroupTotalFeNumFailures,
       "imaLinkCurrentTable": imaLinkCurrentTable,
       "imaLinkCurrentEntry": imaLinkCurrentEntry,
       "imaLinkCurrentImaViolations": imaLinkCurrentImaViolations,
       "imaLinkCurrentOifAnomalies": imaLinkCurrentOifAnomalies,
       "imaLinkCurrentNeSevErroredSecs": imaLinkCurrentNeSevErroredSecs,
       "imaLinkCurrentFeSevErroredSecs": imaLinkCurrentFeSevErroredSecs,
       "imaLinkCurrentNeUnavailSecs": imaLinkCurrentNeUnavailSecs,
       "imaLinkCurrentFeUnavailSecs": imaLinkCurrentFeUnavailSecs,
       "imaLinkCurrentNeTxUnusableSecs": imaLinkCurrentNeTxUnusableSecs,
       "imaLinkCurrentNeRxUnusableSecs": imaLinkCurrentNeRxUnusableSecs,
       "imaLinkCurrentFeTxUnusableSecs": imaLinkCurrentFeTxUnusableSecs,
       "imaLinkCurrentFeRxUnusableSecs": imaLinkCurrentFeRxUnusableSecs,
       "imaLinkCurrentNeTxNumFailures": imaLinkCurrentNeTxNumFailures,
       "imaLinkCurrentNeRxNumFailures": imaLinkCurrentNeRxNumFailures,
       "imaLinkCurrentFeTxNumFailures": imaLinkCurrentFeTxNumFailures,
       "imaLinkCurrentFeRxNumFailures": imaLinkCurrentFeRxNumFailures,
       "imaLinkCurrentTxStuffs": imaLinkCurrentTxStuffs,
       "imaLinkCurrentRxStuffs": imaLinkCurrentRxStuffs,
       "imaLinkIntervalTable": imaLinkIntervalTable,
       "imaLinkIntervalEntry": imaLinkIntervalEntry,
       "imaLinkIntervalNumber": imaLinkIntervalNumber,
       "imaLinkIntervalImaViolations": imaLinkIntervalImaViolations,
       "imaLinkIntervalOifAnomalies": imaLinkIntervalOifAnomalies,
       "imaLinkIntervalNeSevErroredSecs": imaLinkIntervalNeSevErroredSecs,
       "imaLinkIntervalFeSevErroredSecs": imaLinkIntervalFeSevErroredSecs,
       "imaLinkIntervalNeUnavailSecs": imaLinkIntervalNeUnavailSecs,
       "imaLinkIntervalFeUnavailSecs": imaLinkIntervalFeUnavailSecs,
       "imaLinkIntervalNeTxUnusableSecs": imaLinkIntervalNeTxUnusableSecs,
       "imaLinkIntervalNeRxUnusableSecs": imaLinkIntervalNeRxUnusableSecs,
       "imaLinkIntervalFeTxUnusableSecs": imaLinkIntervalFeTxUnusableSecs,
       "imaLinkIntervalFeRxUnusableSecs": imaLinkIntervalFeRxUnusableSecs,
       "imaLinkIntervalNeTxNumFailures": imaLinkIntervalNeTxNumFailures,
       "imaLinkIntervalNeRxNumFailures": imaLinkIntervalNeRxNumFailures,
       "imaLinkIntervalFeTxNumFailures": imaLinkIntervalFeTxNumFailures,
       "imaLinkIntervalFeRxNumFailures": imaLinkIntervalFeRxNumFailures,
       "imaLinkIntervalTxStuffs": imaLinkIntervalTxStuffs,
       "imaLinkIntervalRxStuffs": imaLinkIntervalRxStuffs,
       "imaLinkTotalTable": imaLinkTotalTable,
       "imaLinkTotalEntry": imaLinkTotalEntry,
       "imaLinkTotalImaViolations": imaLinkTotalImaViolations,
       "imaLinkTotalOifAnomalies": imaLinkTotalOifAnomalies,
       "imaLinkTotalNeSevErroredSecs": imaLinkTotalNeSevErroredSecs,
       "imaLinkTotalFeSevErroredSecs": imaLinkTotalFeSevErroredSecs,
       "imaLinkTotalNeUnavailSecs": imaLinkTotalNeUnavailSecs,
       "imaLinkTotalFeUnavailSecs": imaLinkTotalFeUnavailSecs,
       "imaLinkTotalNeTxUnusableSecs": imaLinkTotalNeTxUnusableSecs,
       "imaLinkTotalNeRxUnusableSecs": imaLinkTotalNeRxUnusableSecs,
       "imaLinkTotalFeTxUnusableSecs": imaLinkTotalFeTxUnusableSecs,
       "imaLinkTotalFeRxUnusableSecs": imaLinkTotalFeRxUnusableSecs,
       "imaLinkTotalNeTxNumFailures": imaLinkTotalNeTxNumFailures,
       "imaLinkTotalNeRxNumFailures": imaLinkTotalNeRxNumFailures,
       "imaLinkTotalFeTxNumFailures": imaLinkTotalFeTxNumFailures,
       "imaLinkTotalFeRxNumFailures": imaLinkTotalFeRxNumFailures,
       "imaLinkTotalTxStuffs": imaLinkTotalTxStuffs,
       "imaLinkTotalRxStuffs": imaLinkTotalRxStuffs,
       "atmfImaMibTraps": atmfImaMibTraps,
       "atmfImaMibTrapPrefix": atmfImaMibTrapPrefix,
       "imaFailureAlarm": imaFailureAlarm,
       "atmfImaMibConformance": atmfImaMibConformance,
       "atmfImaMibGroups": atmfImaMibGroups,
       "imaGroupGroup": imaGroupGroup,
       "imaLinkGroup": imaLinkGroup,
       "imaGroupMappingTableGroup": imaGroupMappingTableGroup,
       "imaTestPatternGroup": imaTestPatternGroup,
       "imaAlarmGroup": imaAlarmGroup,
       "imaGroupIntervalGroup": imaGroupIntervalGroup,
       "imaLinkIntervalGroup": imaLinkIntervalGroup,
       "imaNotificationsGroup": imaNotificationsGroup,
       "atmfImaMibCompliances": atmfImaMibCompliances,
       "atmfImaMibCompliance": atmfImaMibCompliance}
)
