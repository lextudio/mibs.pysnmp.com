# SNMP MIB module (HUAWEI-MPLSOAM-PS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MPLSOAM-PS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:13 2024
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

(hwMplsTunnelSignalProto,) = mibBuilder.importSymbols(
    "HUAWEI-MPLS-EXTEND-MIB",
    "hwMplsTunnelSignalProto")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
_HwMplsPsObjects_ObjectIdentity = ObjectIdentity
hwMplsPsObjects = _HwMplsPsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3)
)
_HwMplsPsTable_Object = MibTable
hwMplsPsTable = _HwMplsPsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwMplsPsTable.setStatus("current")
_HwMplsPsEntry_Object = MibTableRow
hwMplsPsEntry = _HwMplsPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1)
)
hwMplsPsEntry.setIndexNames(
    (0, "HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsIndex"),
)
if mibBuilder.loadTexts:
    hwMplsPsEntry.setStatus("current")
_HwMplsPsIndex_Type = Unsigned32
_HwMplsPsIndex_Object = MibTableColumn
hwMplsPsIndex = _HwMplsPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 1),
    _HwMplsPsIndex_Type()
)
hwMplsPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsIndex.setStatus("current")


class _HwMplsPsType_Type(Integer32):
    """Custom type hwMplsPsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_HwMplsPsType_Type.__name__ = "Integer32"
_HwMplsPsType_Object = MibTableColumn
hwMplsPsType = _HwMplsPsType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 2),
    _HwMplsPsType_Type()
)
hwMplsPsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsType.setStatus("current")
_HwMplsPsWorkTunnName_Type = OctetString
_HwMplsPsWorkTunnName_Object = MibTableColumn
hwMplsPsWorkTunnName = _HwMplsPsWorkTunnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 3),
    _HwMplsPsWorkTunnName_Type()
)
hwMplsPsWorkTunnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsWorkTunnName.setStatus("current")


class _HwMplsPsWorkTunnId_Type(Integer32):
    """Custom type hwMplsPsWorkTunnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsPsWorkTunnId_Type.__name__ = "Integer32"
_HwMplsPsWorkTunnId_Object = MibTableColumn
hwMplsPsWorkTunnId = _HwMplsPsWorkTunnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 4),
    _HwMplsPsWorkTunnId_Type()
)
hwMplsPsWorkTunnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsWorkTunnId.setStatus("current")
_HwMplsPsProtectTunnName_Type = OctetString
_HwMplsPsProtectTunnName_Object = MibTableColumn
hwMplsPsProtectTunnName = _HwMplsPsProtectTunnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 5),
    _HwMplsPsProtectTunnName_Type()
)
hwMplsPsProtectTunnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsProtectTunnName.setStatus("current")


class _HwMplsPsProtectTunnId_Type(Integer32):
    """Custom type hwMplsPsProtectTunnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsPsProtectTunnId_Type.__name__ = "Integer32"
_HwMplsPsProtectTunnId_Object = MibTableColumn
hwMplsPsProtectTunnId = _HwMplsPsProtectTunnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 6),
    _HwMplsPsProtectTunnId_Type()
)
hwMplsPsProtectTunnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsProtectTunnId.setStatus("current")


class _HwMplsPsRevertiveMode_Type(Integer32):
    """Custom type hwMplsPsRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwMplsPsRevertiveMode_Type.__name__ = "Integer32"
_HwMplsPsRevertiveMode_Object = MibTableColumn
hwMplsPsRevertiveMode = _HwMplsPsRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 7),
    _HwMplsPsRevertiveMode_Type()
)
hwMplsPsRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsRevertiveMode.setStatus("current")


class _HwMplsPsWTR_Type(Integer32):
    """Custom type hwMplsPsWTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwMplsPsWTR_Type.__name__ = "Integer32"
_HwMplsPsWTR_Object = MibTableColumn
hwMplsPsWTR = _HwMplsPsWTR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 8),
    _HwMplsPsWTR_Type()
)
hwMplsPsWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsWTR.setStatus("current")


class _HwMplsPsHoldOff_Type(Integer32):
    """Custom type hwMplsPsHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwMplsPsHoldOff_Type.__name__ = "Integer32"
_HwMplsPsHoldOff_Object = MibTableColumn
hwMplsPsHoldOff = _HwMplsPsHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 9),
    _HwMplsPsHoldOff_Type()
)
hwMplsPsHoldOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsHoldOff.setStatus("current")


class _HwMplsPsSwitchCondition_Type(Integer32):
    """Custom type hwMplsPsSwitchCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_HwMplsPsSwitchCondition_Type.__name__ = "Integer32"
_HwMplsPsSwitchCondition_Object = MibTableColumn
hwMplsPsSwitchCondition = _HwMplsPsSwitchCondition_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 10),
    _HwMplsPsSwitchCondition_Type()
)
hwMplsPsSwitchCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsSwitchCondition.setStatus("current")


class _HwMplsPsWorkTunnelState_Type(Integer32):
    """Custom type hwMplsPsWorkTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwMplsPsWorkTunnelState_Type.__name__ = "Integer32"
_HwMplsPsWorkTunnelState_Object = MibTableColumn
hwMplsPsWorkTunnelState = _HwMplsPsWorkTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 11),
    _HwMplsPsWorkTunnelState_Type()
)
hwMplsPsWorkTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsWorkTunnelState.setStatus("current")


class _HwMplsPsProtTunnelState_Type(Integer32):
    """Custom type hwMplsPsProtTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwMplsPsProtTunnelState_Type.__name__ = "Integer32"
_HwMplsPsProtTunnelState_Object = MibTableColumn
hwMplsPsProtTunnelState = _HwMplsPsProtTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 12),
    _HwMplsPsProtTunnelState_Type()
)
hwMplsPsProtTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsProtTunnelState.setStatus("current")


class _HwMplsPsSwitchResult_Type(Integer32):
    """Custom type hwMplsPsSwitchResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwMplsPsSwitchResult_Type.__name__ = "Integer32"
_HwMplsPsSwitchResult_Object = MibTableColumn
hwMplsPsSwitchResult = _HwMplsPsSwitchResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 13),
    _HwMplsPsSwitchResult_Type()
)
hwMplsPsSwitchResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsSwitchResult.setStatus("current")


class _HwMplsPsCfgType_Type(Integer32):
    """Custom type hwMplsPsCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwMplsPsCfgType_Type.__name__ = "Integer32"
_HwMplsPsCfgType_Object = MibTableColumn
hwMplsPsCfgType = _HwMplsPsCfgType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 14),
    _HwMplsPsCfgType_Type()
)
hwMplsPsCfgType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsCfgType.setStatus("current")


class _HwMplsPsCfgProtectTunnId_Type(Integer32):
    """Custom type hwMplsPsCfgProtectTunnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsPsCfgProtectTunnId_Type.__name__ = "Integer32"
_HwMplsPsCfgProtectTunnId_Object = MibTableColumn
hwMplsPsCfgProtectTunnId = _HwMplsPsCfgProtectTunnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 15),
    _HwMplsPsCfgProtectTunnId_Type()
)
hwMplsPsCfgProtectTunnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsCfgProtectTunnId.setStatus("current")


class _HwMplsPsCfgRevertiveMode_Type(Integer32):
    """Custom type hwMplsPsCfgRevertiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwMplsPsCfgRevertiveMode_Type.__name__ = "Integer32"
_HwMplsPsCfgRevertiveMode_Object = MibTableColumn
hwMplsPsCfgRevertiveMode = _HwMplsPsCfgRevertiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 16),
    _HwMplsPsCfgRevertiveMode_Type()
)
hwMplsPsCfgRevertiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsCfgRevertiveMode.setStatus("current")


class _HwMplsPsCfgWTR_Type(Integer32):
    """Custom type hwMplsPsCfgWTR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_HwMplsPsCfgWTR_Type.__name__ = "Integer32"
_HwMplsPsCfgWTR_Object = MibTableColumn
hwMplsPsCfgWTR = _HwMplsPsCfgWTR_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 17),
    _HwMplsPsCfgWTR_Type()
)
hwMplsPsCfgWTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsCfgWTR.setStatus("current")


class _HwMplsPsCfgHoldOff_Type(Integer32):
    """Custom type hwMplsPsCfgHoldOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwMplsPsCfgHoldOff_Type.__name__ = "Integer32"
_HwMplsPsCfgHoldOff_Object = MibTableColumn
hwMplsPsCfgHoldOff = _HwMplsPsCfgHoldOff_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 18),
    _HwMplsPsCfgHoldOff_Type()
)
hwMplsPsCfgHoldOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsCfgHoldOff.setStatus("current")
_HwMplsPsRowStatus_Type = RowStatus
_HwMplsPsRowStatus_Object = MibTableColumn
hwMplsPsRowStatus = _HwMplsPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 1, 1, 19),
    _HwMplsPsRowStatus_Type()
)
hwMplsPsRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsPsRowStatus.setStatus("current")


class _HwTunnPsTrapOpen_Type(Unsigned32):
    """Custom type hwTunnPsTrapOpen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HwTunnPsTrapOpen_Type.__name__ = "Unsigned32"
_HwTunnPsTrapOpen_Object = MibScalar
hwTunnPsTrapOpen = _HwTunnPsTrapOpen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 2),
    _HwTunnPsTrapOpen_Type()
)
hwTunnPsTrapOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwTunnPsTrapOpen.setStatus("current")
_HwMplsVCPsTable_Object = MibTable
hwMplsVCPsTable = _HwMplsVCPsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwMplsVCPsTable.setStatus("current")
_HwMplsVCPsEntry_Object = MibTableRow
hwMplsVCPsEntry = _HwMplsVCPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1)
)
hwMplsVCPsEntry.setIndexNames(
    (0, "HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsIfIndex"),
)
if mibBuilder.loadTexts:
    hwMplsVCPsEntry.setStatus("current")
_HwMplsVCPsIfIndex_Type = InterfaceIndex
_HwMplsVCPsIfIndex_Object = MibTableColumn
hwMplsVCPsIfIndex = _HwMplsVCPsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 1),
    _HwMplsVCPsIfIndex_Type()
)
hwMplsVCPsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMplsVCPsIfIndex.setStatus("current")
_HwMplsVCPsTNLBinding_Type = TruthValue
_HwMplsVCPsTNLBinding_Object = MibTableColumn
hwMplsVCPsTNLBinding = _HwMplsVCPsTNLBinding_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 2),
    _HwMplsVCPsTNLBinding_Type()
)
hwMplsVCPsTNLBinding.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsVCPsTNLBinding.setStatus("current")
_HwMplsTeReverseLspName_Type = OctetString
_HwMplsTeReverseLspName_Object = MibTableColumn
hwMplsTeReverseLspName = _HwMplsTeReverseLspName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 3),
    _HwMplsTeReverseLspName_Type()
)
hwMplsTeReverseLspName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsTeReverseLspName.setStatus("current")
_HwMplsVcPsRowStatus_Type = RowStatus
_HwMplsVcPsRowStatus_Object = MibTableColumn
hwMplsVcPsRowStatus = _HwMplsVcPsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 4),
    _HwMplsVcPsRowStatus_Type()
)
hwMplsVcPsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsVcPsRowStatus.setStatus("current")
_HwMplsTeReverseLspLsrId_Type = IpAddress
_HwMplsTeReverseLspLsrId_Object = MibTableColumn
hwMplsTeReverseLspLsrId = _HwMplsTeReverseLspLsrId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 5),
    _HwMplsTeReverseLspLsrId_Type()
)
hwMplsTeReverseLspLsrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsTeReverseLspLsrId.setStatus("current")


class _HwMplsTeReverseLspTunnId_Type(Integer32):
    """Custom type hwMplsTeReverseLspTunnId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMplsTeReverseLspTunnId_Type.__name__ = "Integer32"
_HwMplsTeReverseLspTunnId_Object = MibTableColumn
hwMplsTeReverseLspTunnId = _HwMplsTeReverseLspTunnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 3, 1, 6),
    _HwMplsTeReverseLspTunnId_Type()
)
hwMplsTeReverseLspTunnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMplsTeReverseLspTunnId.setStatus("current")


class _HwMplsApsMismatchReason_Type(Integer32):
    """Custom type hwMplsApsMismatchReason based on Integer32"""
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
        *(("bridge", 1),
          ("channel", 2),
          ("operation", 4),
          ("switching", 3),
          ("traffic", 5))
    )


_HwMplsApsMismatchReason_Type.__name__ = "Integer32"
_HwMplsApsMismatchReason_Object = MibScalar
hwMplsApsMismatchReason = _HwMplsApsMismatchReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 3, 4),
    _HwMplsApsMismatchReason_Type()
)
hwMplsApsMismatchReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMplsApsMismatchReason.setStatus("current")
_HwMplsPsNotifications_ObjectIdentity = ObjectIdentity
hwMplsPsNotifications = _HwMplsPsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4)
)
_HwMplsOamPsConformance_ObjectIdentity = ObjectIdentity
hwMplsOamPsConformance = _HwMplsOamPsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100)
)
_HwMplsOamPsCompliances_ObjectIdentity = ObjectIdentity
hwMplsOamPsCompliances = _HwMplsOamPsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 1)
)
_HwMplsOamPsGroups_ObjectIdentity = ObjectIdentity
hwMplsOamPsGroups = _HwMplsOamPsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2)
)

# Managed Objects groups

hwMplsPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 1)
)
hwMplsPsGroup.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsType"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsRevertiveMode"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWTR"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsHoldOff"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchCondition"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnelState"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtTunnelState"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgType"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgProtectTunnId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgRevertiveMode"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgWTR"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsCfgHoldOff"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsRowStatus"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwTunnPsTrapOpen"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsIfIndex"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsIndex"))
)
if mibBuilder.loadTexts:
    hwMplsPsGroup.setStatus("current")

hwMplsVcPsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 2)
)
hwMplsVcPsGroup.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVCPsTNLBinding"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsVcPsRowStatus"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspLsrId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsTeReverseLspTunnId"))
)
if mibBuilder.loadTexts:
    hwMplsVcPsGroup.setStatus("current")


# Notification objects

hwMplsPsSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 1)
)
hwMplsPsSwitchPtoW.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hwMplsPsSwitchPtoW.setStatus(
        "current"
    )

hwMplsPsSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 2)
)
hwMplsPsSwitchWtoP.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsProtectTunnId"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchResult"))
)
if mibBuilder.loadTexts:
    hwMplsPsSwitchWtoP.setStatus(
        "current"
    )

hwMplsApsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 3)
)
hwMplsApsMismatch.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchReason"))
)
if mibBuilder.loadTexts:
    hwMplsApsMismatch.setStatus(
        "current"
    )

hwMplsApsMismatchRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 4)
)
hwMplsApsMismatchRecovery.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchReason"))
)
if mibBuilder.loadTexts:
    hwMplsApsMismatchRecovery.setStatus(
        "current"
    )

hwMplsApsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 5)
)
hwMplsApsLost.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsApsLost.setStatus(
        "current"
    )

hwMplsApsLostRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 4, 6)
)
hwMplsApsLostRecovery.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsWorkTunnName"),
        ("HUAWEI-MPLS-EXTEND-MIB", "hwMplsTunnelSignalProto"))
)
if mibBuilder.loadTexts:
    hwMplsApsLostRecovery.setStatus(
        "current"
    )


# Notifications groups

hwMplsPsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 2, 3)
)
hwMplsPsNotificationGroup.setObjects(
      *(("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchPtoW"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsPsSwitchWtoP"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatch"),
        ("HUAWEI-MPLSOAM-PS-MIB", "hwMplsApsMismatchRecovery"))
)
if mibBuilder.loadTexts:
    hwMplsPsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMplsOamPsGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 12, 7, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hwMplsOamPsGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MPLSOAM-PS-MIB",
    **{"hwMplsOam": hwMplsOam,
       "hwMplsOamPs": hwMplsOamPs,
       "hwMplsPsObjects": hwMplsPsObjects,
       "hwMplsPsTable": hwMplsPsTable,
       "hwMplsPsEntry": hwMplsPsEntry,
       "hwMplsPsIndex": hwMplsPsIndex,
       "hwMplsPsType": hwMplsPsType,
       "hwMplsPsWorkTunnName": hwMplsPsWorkTunnName,
       "hwMplsPsWorkTunnId": hwMplsPsWorkTunnId,
       "hwMplsPsProtectTunnName": hwMplsPsProtectTunnName,
       "hwMplsPsProtectTunnId": hwMplsPsProtectTunnId,
       "hwMplsPsRevertiveMode": hwMplsPsRevertiveMode,
       "hwMplsPsWTR": hwMplsPsWTR,
       "hwMplsPsHoldOff": hwMplsPsHoldOff,
       "hwMplsPsSwitchCondition": hwMplsPsSwitchCondition,
       "hwMplsPsWorkTunnelState": hwMplsPsWorkTunnelState,
       "hwMplsPsProtTunnelState": hwMplsPsProtTunnelState,
       "hwMplsPsSwitchResult": hwMplsPsSwitchResult,
       "hwMplsPsCfgType": hwMplsPsCfgType,
       "hwMplsPsCfgProtectTunnId": hwMplsPsCfgProtectTunnId,
       "hwMplsPsCfgRevertiveMode": hwMplsPsCfgRevertiveMode,
       "hwMplsPsCfgWTR": hwMplsPsCfgWTR,
       "hwMplsPsCfgHoldOff": hwMplsPsCfgHoldOff,
       "hwMplsPsRowStatus": hwMplsPsRowStatus,
       "hwTunnPsTrapOpen": hwTunnPsTrapOpen,
       "hwMplsVCPsTable": hwMplsVCPsTable,
       "hwMplsVCPsEntry": hwMplsVCPsEntry,
       "hwMplsVCPsIfIndex": hwMplsVCPsIfIndex,
       "hwMplsVCPsTNLBinding": hwMplsVCPsTNLBinding,
       "hwMplsTeReverseLspName": hwMplsTeReverseLspName,
       "hwMplsVcPsRowStatus": hwMplsVcPsRowStatus,
       "hwMplsTeReverseLspLsrId": hwMplsTeReverseLspLsrId,
       "hwMplsTeReverseLspTunnId": hwMplsTeReverseLspTunnId,
       "hwMplsApsMismatchReason": hwMplsApsMismatchReason,
       "hwMplsPsNotifications": hwMplsPsNotifications,
       "hwMplsPsSwitchPtoW": hwMplsPsSwitchPtoW,
       "hwMplsPsSwitchWtoP": hwMplsPsSwitchWtoP,
       "hwMplsApsMismatch": hwMplsApsMismatch,
       "hwMplsApsMismatchRecovery": hwMplsApsMismatchRecovery,
       "hwMplsApsLost": hwMplsApsLost,
       "hwMplsApsLostRecovery": hwMplsApsLostRecovery,
       "hwMplsOamPsConformance": hwMplsOamPsConformance,
       "hwMplsOamPsCompliances": hwMplsOamPsCompliances,
       "hwMplsOamPsGroupCompliance": hwMplsOamPsGroupCompliance,
       "hwMplsOamPsGroups": hwMplsOamPsGroups,
       "hwMplsPsGroup": hwMplsPsGroup,
       "hwMplsVcPsGroup": hwMplsVcPsGroup,
       "hwMplsPsNotificationGroup": hwMplsPsNotificationGroup}
)
