# SNMP MIB module (HUAWEI-IMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:02 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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

hwImaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176)
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



# MIB Managed Objects in the order of their OIDs

_HwImaMibObjects_ObjectIdentity = ObjectIdentity
hwImaMibObjects = _HwImaMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1)
)
_HwImaGroupTable_Object = MibTable
hwImaGroupTable = _HwImaGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1)
)
if mibBuilder.loadTexts:
    hwImaGroupTable.setStatus("current")
_HwImaGroupEntry_Object = MibTableRow
hwImaGroupEntry = _HwImaGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1)
)
hwImaGroupEntry.setIndexNames(
    (0, "HUAWEI-IMA-MIB", "hwImaGroupIfIndex"),
)
if mibBuilder.loadTexts:
    hwImaGroupEntry.setStatus("current")
_HwImaGroupIfIndex_Type = InterfaceIndex
_HwImaGroupIfIndex_Object = MibTableColumn
hwImaGroupIfIndex = _HwImaGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 1),
    _HwImaGroupIfIndex_Type()
)
hwImaGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupIfIndex.setStatus("current")
_HwImaGroupNeState_Type = ImaGroupState
_HwImaGroupNeState_Object = MibTableColumn
hwImaGroupNeState = _HwImaGroupNeState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 2),
    _HwImaGroupNeState_Type()
)
hwImaGroupNeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupNeState.setStatus("current")
_HwImaGroupFeState_Type = ImaGroupState
_HwImaGroupFeState_Object = MibTableColumn
hwImaGroupFeState = _HwImaGroupFeState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 3),
    _HwImaGroupFeState_Type()
)
hwImaGroupFeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupFeState.setStatus("current")


class _HwImaGroupSymmetry_Type(ImaGroupSymmetry):
    """Custom type hwImaGroupSymmetry based on ImaGroupSymmetry"""


_HwImaGroupSymmetry_Object = MibTableColumn
hwImaGroupSymmetry = _HwImaGroupSymmetry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 4),
    _HwImaGroupSymmetry_Type()
)
hwImaGroupSymmetry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupSymmetry.setStatus("current")


class _HwImaGroupMinNumTxLinks_Type(Integer32):
    """Custom type hwImaGroupMinNumTxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwImaGroupMinNumTxLinks_Type.__name__ = "Integer32"
_HwImaGroupMinNumTxLinks_Object = MibTableColumn
hwImaGroupMinNumTxLinks = _HwImaGroupMinNumTxLinks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 5),
    _HwImaGroupMinNumTxLinks_Type()
)
hwImaGroupMinNumTxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwImaGroupMinNumTxLinks.setStatus("current")


class _HwImaGroupMinNumRxLinks_Type(Integer32):
    """Custom type hwImaGroupMinNumRxLinks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_HwImaGroupMinNumRxLinks_Type.__name__ = "Integer32"
_HwImaGroupMinNumRxLinks_Object = MibTableColumn
hwImaGroupMinNumRxLinks = _HwImaGroupMinNumRxLinks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 6),
    _HwImaGroupMinNumRxLinks_Type()
)
hwImaGroupMinNumRxLinks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwImaGroupMinNumRxLinks.setStatus("current")
_HwImaGroupTxTimingRefLink_Type = InterfaceIndexOrZero
_HwImaGroupTxTimingRefLink_Object = MibTableColumn
hwImaGroupTxTimingRefLink = _HwImaGroupTxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 7),
    _HwImaGroupTxTimingRefLink_Type()
)
hwImaGroupTxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupTxTimingRefLink.setStatus("current")
_HwImaGroupRxTimingRefLink_Type = InterfaceIndexOrZero
_HwImaGroupRxTimingRefLink_Object = MibTableColumn
hwImaGroupRxTimingRefLink = _HwImaGroupRxTimingRefLink_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 8),
    _HwImaGroupRxTimingRefLink_Type()
)
hwImaGroupRxTimingRefLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupRxTimingRefLink.setStatus("current")


class _HwImaGroupTxImaId_Type(Integer32):
    """Custom type hwImaGroupTxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwImaGroupTxImaId_Type.__name__ = "Integer32"
_HwImaGroupTxImaId_Object = MibTableColumn
hwImaGroupTxImaId = _HwImaGroupTxImaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 9),
    _HwImaGroupTxImaId_Type()
)
hwImaGroupTxImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupTxImaId.setStatus("current")


class _HwImaGroupRxImaId_Type(Integer32):
    """Custom type hwImaGroupRxImaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwImaGroupRxImaId_Type.__name__ = "Integer32"
_HwImaGroupRxImaId_Object = MibTableColumn
hwImaGroupRxImaId = _HwImaGroupRxImaId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 10),
    _HwImaGroupRxImaId_Type()
)
hwImaGroupRxImaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupRxImaId.setStatus("current")


class _HwImaGroupTxFrameLength_Type(ImaFrameLength):
    """Custom type hwImaGroupTxFrameLength based on ImaFrameLength"""


_HwImaGroupTxFrameLength_Object = MibTableColumn
hwImaGroupTxFrameLength = _HwImaGroupTxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 11),
    _HwImaGroupTxFrameLength_Type()
)
hwImaGroupTxFrameLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwImaGroupTxFrameLength.setStatus("current")
_HwImaGroupRxFrameLength_Type = ImaFrameLength
_HwImaGroupRxFrameLength_Object = MibTableColumn
hwImaGroupRxFrameLength = _HwImaGroupRxFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 12),
    _HwImaGroupRxFrameLength_Type()
)
hwImaGroupRxFrameLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupRxFrameLength.setStatus("current")


class _HwImaGroupDiffDelayMax_Type(MilliSeconds):
    """Custom type hwImaGroupDiffDelayMax based on MilliSeconds"""
    defaultValue = 25

    subtypeSpec = MilliSeconds.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 100),
    )


_HwImaGroupDiffDelayMax_Type.__name__ = "MilliSeconds"
_HwImaGroupDiffDelayMax_Object = MibTableColumn
hwImaGroupDiffDelayMax = _HwImaGroupDiffDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 13),
    _HwImaGroupDiffDelayMax_Type()
)
hwImaGroupDiffDelayMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwImaGroupDiffDelayMax.setStatus("current")


class _HwImaGroupAlphaValue_Type(Integer32):
    """Custom type hwImaGroupAlphaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwImaGroupAlphaValue_Type.__name__ = "Integer32"
_HwImaGroupAlphaValue_Object = MibTableColumn
hwImaGroupAlphaValue = _HwImaGroupAlphaValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 14),
    _HwImaGroupAlphaValue_Type()
)
hwImaGroupAlphaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupAlphaValue.setStatus("current")


class _HwImaGroupBetaValue_Type(Integer32):
    """Custom type hwImaGroupBetaValue based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwImaGroupBetaValue_Type.__name__ = "Integer32"
_HwImaGroupBetaValue_Object = MibTableColumn
hwImaGroupBetaValue = _HwImaGroupBetaValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 15),
    _HwImaGroupBetaValue_Type()
)
hwImaGroupBetaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupBetaValue.setStatus("current")


class _HwImaGroupGammaValue_Type(Integer32):
    """Custom type hwImaGroupGammaValue based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_HwImaGroupGammaValue_Type.__name__ = "Integer32"
_HwImaGroupGammaValue_Object = MibTableColumn
hwImaGroupGammaValue = _HwImaGroupGammaValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 16),
    _HwImaGroupGammaValue_Type()
)
hwImaGroupGammaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupGammaValue.setStatus("current")
_HwImaGroupNumTxActLinks_Type = Gauge32
_HwImaGroupNumTxActLinks_Object = MibTableColumn
hwImaGroupNumTxActLinks = _HwImaGroupNumTxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 17),
    _HwImaGroupNumTxActLinks_Type()
)
hwImaGroupNumTxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupNumTxActLinks.setStatus("current")
_HwImaGroupNumRxActLinks_Type = Gauge32
_HwImaGroupNumRxActLinks_Object = MibTableColumn
hwImaGroupNumRxActLinks = _HwImaGroupNumRxActLinks_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 18),
    _HwImaGroupNumRxActLinks_Type()
)
hwImaGroupNumRxActLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupNumRxActLinks.setStatus("current")


class _HwImaGroupTxOamLabelValue_Type(Integer32):
    """Custom type hwImaGroupTxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwImaGroupTxOamLabelValue_Type.__name__ = "Integer32"
_HwImaGroupTxOamLabelValue_Object = MibTableColumn
hwImaGroupTxOamLabelValue = _HwImaGroupTxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 19),
    _HwImaGroupTxOamLabelValue_Type()
)
hwImaGroupTxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupTxOamLabelValue.setStatus("current")


class _HwImaGroupRxOamLabelValue_Type(Integer32):
    """Custom type hwImaGroupRxOamLabelValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwImaGroupRxOamLabelValue_Type.__name__ = "Integer32"
_HwImaGroupRxOamLabelValue_Object = MibTableColumn
hwImaGroupRxOamLabelValue = _HwImaGroupRxOamLabelValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 20),
    _HwImaGroupRxOamLabelValue_Type()
)
hwImaGroupRxOamLabelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupRxOamLabelValue.setStatus("current")
_HwImaGroupFirstLinkIfIndex_Type = InterfaceIndex
_HwImaGroupFirstLinkIfIndex_Object = MibTableColumn
hwImaGroupFirstLinkIfIndex = _HwImaGroupFirstLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 1, 1, 21),
    _HwImaGroupFirstLinkIfIndex_Type()
)
hwImaGroupFirstLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaGroupFirstLinkIfIndex.setStatus("current")
_HwImaLinkTable_Object = MibTable
hwImaLinkTable = _HwImaLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2)
)
if mibBuilder.loadTexts:
    hwImaLinkTable.setStatus("current")
_HwImaLinkEntry_Object = MibTableRow
hwImaLinkEntry = _HwImaLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1)
)
hwImaLinkEntry.setIndexNames(
    (0, "HUAWEI-IMA-MIB", "hwImaLinkIfIndex"),
)
if mibBuilder.loadTexts:
    hwImaLinkEntry.setStatus("current")
_HwImaLinkIfIndex_Type = InterfaceIndex
_HwImaLinkIfIndex_Object = MibTableColumn
hwImaLinkIfIndex = _HwImaLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 1),
    _HwImaLinkIfIndex_Type()
)
hwImaLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwImaLinkIfIndex.setStatus("current")
_HwImaLinkGroupIfIndex_Type = InterfaceIndex
_HwImaLinkGroupIfIndex_Object = MibTableColumn
hwImaLinkGroupIfIndex = _HwImaLinkGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 2),
    _HwImaLinkGroupIfIndex_Type()
)
hwImaLinkGroupIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwImaLinkGroupIfIndex.setStatus("current")
_HwImaLinkNeTxState_Type = ImaLinkState
_HwImaLinkNeTxState_Object = MibTableColumn
hwImaLinkNeTxState = _HwImaLinkNeTxState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 3),
    _HwImaLinkNeTxState_Type()
)
hwImaLinkNeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaLinkNeTxState.setStatus("current")
_HwImaLinkNeRxState_Type = ImaLinkState
_HwImaLinkNeRxState_Object = MibTableColumn
hwImaLinkNeRxState = _HwImaLinkNeRxState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 4),
    _HwImaLinkNeRxState_Type()
)
hwImaLinkNeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaLinkNeRxState.setStatus("current")
_HwImaLinkFeTxState_Type = ImaLinkState
_HwImaLinkFeTxState_Object = MibTableColumn
hwImaLinkFeTxState = _HwImaLinkFeTxState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 5),
    _HwImaLinkFeTxState_Type()
)
hwImaLinkFeTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaLinkFeTxState.setStatus("current")
_HwImaLinkFeRxState_Type = ImaLinkState
_HwImaLinkFeRxState_Object = MibTableColumn
hwImaLinkFeRxState = _HwImaLinkFeRxState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 6),
    _HwImaLinkFeRxState_Type()
)
hwImaLinkFeRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwImaLinkFeRxState.setStatus("current")
_HwImaLinkRowStatus_Type = RowStatus
_HwImaLinkRowStatus_Object = MibTableColumn
hwImaLinkRowStatus = _HwImaLinkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 1, 2, 1, 51),
    _HwImaLinkRowStatus_Type()
)
hwImaLinkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwImaLinkRowStatus.setStatus("current")
_HwImaMibConformance_ObjectIdentity = ObjectIdentity
hwImaMibConformance = _HwImaMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2)
)
_HwImaMibGroups_ObjectIdentity = ObjectIdentity
hwImaMibGroups = _HwImaMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1)
)
_HwImaMibCompliances_ObjectIdentity = ObjectIdentity
hwImaMibCompliances = _HwImaMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 2)
)

# Managed Objects groups

hwImaGroupGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1, 1)
)
hwImaGroupGroup.setObjects(
      *(("HUAWEI-IMA-MIB", "hwImaGroupIfIndex"),
        ("HUAWEI-IMA-MIB", "hwImaGroupNeState"),
        ("HUAWEI-IMA-MIB", "hwImaGroupFeState"),
        ("HUAWEI-IMA-MIB", "hwImaGroupSymmetry"),
        ("HUAWEI-IMA-MIB", "hwImaGroupMinNumTxLinks"),
        ("HUAWEI-IMA-MIB", "hwImaGroupMinNumRxLinks"),
        ("HUAWEI-IMA-MIB", "hwImaGroupTxTimingRefLink"),
        ("HUAWEI-IMA-MIB", "hwImaGroupRxTimingRefLink"),
        ("HUAWEI-IMA-MIB", "hwImaGroupTxImaId"),
        ("HUAWEI-IMA-MIB", "hwImaGroupRxImaId"),
        ("HUAWEI-IMA-MIB", "hwImaGroupTxFrameLength"),
        ("HUAWEI-IMA-MIB", "hwImaGroupRxFrameLength"),
        ("HUAWEI-IMA-MIB", "hwImaGroupDiffDelayMax"),
        ("HUAWEI-IMA-MIB", "hwImaGroupAlphaValue"),
        ("HUAWEI-IMA-MIB", "hwImaGroupBetaValue"),
        ("HUAWEI-IMA-MIB", "hwImaGroupGammaValue"),
        ("HUAWEI-IMA-MIB", "hwImaGroupNumTxActLinks"),
        ("HUAWEI-IMA-MIB", "hwImaGroupNumRxActLinks"),
        ("HUAWEI-IMA-MIB", "hwImaGroupTxOamLabelValue"),
        ("HUAWEI-IMA-MIB", "hwImaGroupRxOamLabelValue"),
        ("HUAWEI-IMA-MIB", "hwImaGroupFirstLinkIfIndex"))
)
if mibBuilder.loadTexts:
    hwImaGroupGroup.setStatus("current")

hwImaLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 1, 2)
)
hwImaLinkGroup.setObjects(
      *(("HUAWEI-IMA-MIB", "hwImaLinkGroupIfIndex"),
        ("HUAWEI-IMA-MIB", "hwImaLinkNeTxState"),
        ("HUAWEI-IMA-MIB", "hwImaLinkNeRxState"),
        ("HUAWEI-IMA-MIB", "hwImaLinkFeTxState"),
        ("HUAWEI-IMA-MIB", "hwImaLinkFeRxState"),
        ("HUAWEI-IMA-MIB", "hwImaLinkRowStatus"))
)
if mibBuilder.loadTexts:
    hwImaLinkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwImaMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 176, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwImaMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IMA-MIB",
    **{"MilliSeconds": MilliSeconds,
       "ImaGroupState": ImaGroupState,
       "ImaGroupSymmetry": ImaGroupSymmetry,
       "ImaFrameLength": ImaFrameLength,
       "ImaLinkState": ImaLinkState,
       "hwImaMIB": hwImaMIB,
       "hwImaMibObjects": hwImaMibObjects,
       "hwImaGroupTable": hwImaGroupTable,
       "hwImaGroupEntry": hwImaGroupEntry,
       "hwImaGroupIfIndex": hwImaGroupIfIndex,
       "hwImaGroupNeState": hwImaGroupNeState,
       "hwImaGroupFeState": hwImaGroupFeState,
       "hwImaGroupSymmetry": hwImaGroupSymmetry,
       "hwImaGroupMinNumTxLinks": hwImaGroupMinNumTxLinks,
       "hwImaGroupMinNumRxLinks": hwImaGroupMinNumRxLinks,
       "hwImaGroupTxTimingRefLink": hwImaGroupTxTimingRefLink,
       "hwImaGroupRxTimingRefLink": hwImaGroupRxTimingRefLink,
       "hwImaGroupTxImaId": hwImaGroupTxImaId,
       "hwImaGroupRxImaId": hwImaGroupRxImaId,
       "hwImaGroupTxFrameLength": hwImaGroupTxFrameLength,
       "hwImaGroupRxFrameLength": hwImaGroupRxFrameLength,
       "hwImaGroupDiffDelayMax": hwImaGroupDiffDelayMax,
       "hwImaGroupAlphaValue": hwImaGroupAlphaValue,
       "hwImaGroupBetaValue": hwImaGroupBetaValue,
       "hwImaGroupGammaValue": hwImaGroupGammaValue,
       "hwImaGroupNumTxActLinks": hwImaGroupNumTxActLinks,
       "hwImaGroupNumRxActLinks": hwImaGroupNumRxActLinks,
       "hwImaGroupTxOamLabelValue": hwImaGroupTxOamLabelValue,
       "hwImaGroupRxOamLabelValue": hwImaGroupRxOamLabelValue,
       "hwImaGroupFirstLinkIfIndex": hwImaGroupFirstLinkIfIndex,
       "hwImaLinkTable": hwImaLinkTable,
       "hwImaLinkEntry": hwImaLinkEntry,
       "hwImaLinkIfIndex": hwImaLinkIfIndex,
       "hwImaLinkGroupIfIndex": hwImaLinkGroupIfIndex,
       "hwImaLinkNeTxState": hwImaLinkNeTxState,
       "hwImaLinkNeRxState": hwImaLinkNeRxState,
       "hwImaLinkFeTxState": hwImaLinkFeTxState,
       "hwImaLinkFeRxState": hwImaLinkFeRxState,
       "hwImaLinkRowStatus": hwImaLinkRowStatus,
       "hwImaMibConformance": hwImaMibConformance,
       "hwImaMibGroups": hwImaMibGroups,
       "hwImaGroupGroup": hwImaGroupGroup,
       "hwImaLinkGroup": hwImaLinkGroup,
       "hwImaMibCompliances": hwImaMibCompliances,
       "hwImaMibCompliance": hwImaMibCompliance}
)
