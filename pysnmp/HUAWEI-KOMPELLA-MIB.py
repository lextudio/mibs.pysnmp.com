# SNMP MIB module (HUAWEI-KOMPELLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-KOMPELLA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:16 2024
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

(HWEnableValue,
 HWL2VpnStateChangeReason,
 HWL2VpnVcEncapsType) = mibBuilder.importSymbols(
    "HUAWEI-VPLS-EXT-MIB",
    "HWEnableValue",
    "HWL2VpnStateChangeReason",
    "HWL2VpnVcEncapsType")

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

hwL2VpnKompella = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwL2Vpn_ObjectIdentity = ObjectIdentity
hwL2Vpn = _HwL2Vpn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119)
)
_HwKompellaMIBObjects_ObjectIdentity = ObjectIdentity
hwKompellaMIBObjects = _HwKompellaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1)
)
_HwKompellaVpnTable_Object = MibTable
hwKompellaVpnTable = _HwKompellaVpnTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwKompellaVpnTable.setStatus("current")
_HwKompellaVpnEntry_Object = MibTableRow
hwKompellaVpnEntry = _HwKompellaVpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1, 1)
)
hwKompellaVpnEntry.setIndexNames(
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnName"),
)
if mibBuilder.loadTexts:
    hwKompellaVpnEntry.setStatus("current")


class _HwKompellaVpnName_Type(DisplayString):
    """Custom type hwKompellaVpnName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_HwKompellaVpnName_Type.__name__ = "DisplayString"
_HwKompellaVpnName_Object = MibTableColumn
hwKompellaVpnName = _HwKompellaVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1, 1, 1),
    _HwKompellaVpnName_Type()
)
hwKompellaVpnName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKompellaVpnName.setStatus("current")
_HwKompellaVpnVcType_Type = HWL2VpnVcEncapsType
_HwKompellaVpnVcType_Object = MibTableColumn
hwKompellaVpnVcType = _HwKompellaVpnVcType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1, 1, 2),
    _HwKompellaVpnVcType_Type()
)
hwKompellaVpnVcType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVpnVcType.setStatus("current")


class _HwKompellaVpnRouteDistinguisher_Type(DisplayString):
    """Custom type hwKompellaVpnRouteDistinguisher based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 21),
    )


_HwKompellaVpnRouteDistinguisher_Type.__name__ = "DisplayString"
_HwKompellaVpnRouteDistinguisher_Object = MibTableColumn
hwKompellaVpnRouteDistinguisher = _HwKompellaVpnRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1, 1, 3),
    _HwKompellaVpnRouteDistinguisher_Type()
)
hwKompellaVpnRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVpnRouteDistinguisher.setStatus("current")
_HwKompellaVpnCtrlWord_Type = HWEnableValue
_HwKompellaVpnCtrlWord_Object = MibTableColumn
hwKompellaVpnCtrlWord = _HwKompellaVpnCtrlWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1, 1, 4),
    _HwKompellaVpnCtrlWord_Type()
)
hwKompellaVpnCtrlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVpnCtrlWord.setStatus("current")


class _HwKompellaVpnMtu_Type(Unsigned32):
    """Custom type hwKompellaVpnMtu based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(46, 16352),
    )


_HwKompellaVpnMtu_Type.__name__ = "Unsigned32"
_HwKompellaVpnMtu_Object = MibTableColumn
hwKompellaVpnMtu = _HwKompellaVpnMtu_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1, 1, 5),
    _HwKompellaVpnMtu_Type()
)
hwKompellaVpnMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVpnMtu.setStatus("current")
_HwKompellaVpnRowStatus_Type = RowStatus
_HwKompellaVpnRowStatus_Object = MibTableColumn
hwKompellaVpnRowStatus = _HwKompellaVpnRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 1, 1, 51),
    _HwKompellaVpnRowStatus_Type()
)
hwKompellaVpnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVpnRowStatus.setStatus("current")
_HwKompellaVpnTargetTable_Object = MibTable
hwKompellaVpnTargetTable = _HwKompellaVpnTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwKompellaVpnTargetTable.setStatus("current")
_HwKompellaVpnTargetEntry_Object = MibTableRow
hwKompellaVpnTargetEntry = _HwKompellaVpnTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 2, 1)
)
hwKompellaVpnTargetEntry.setIndexNames(
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnName"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnTargetType"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnTarget"),
)
if mibBuilder.loadTexts:
    hwKompellaVpnTargetEntry.setStatus("current")


class _HwKompellaVpnTargetType_Type(Integer32):
    """Custom type hwKompellaVpnTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("export", 2),
          ("import", 1))
    )


_HwKompellaVpnTargetType_Type.__name__ = "Integer32"
_HwKompellaVpnTargetType_Object = MibTableColumn
hwKompellaVpnTargetType = _HwKompellaVpnTargetType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 2, 1, 2),
    _HwKompellaVpnTargetType_Type()
)
hwKompellaVpnTargetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKompellaVpnTargetType.setStatus("current")


class _HwKompellaVpnTarget_Type(DisplayString):
    """Custom type hwKompellaVpnTarget based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 21),
    )


_HwKompellaVpnTarget_Type.__name__ = "DisplayString"
_HwKompellaVpnTarget_Object = MibTableColumn
hwKompellaVpnTarget = _HwKompellaVpnTarget_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 2, 1, 3),
    _HwKompellaVpnTarget_Type()
)
hwKompellaVpnTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKompellaVpnTarget.setStatus("current")
_HwKompellaVpnTargetRowStatus_Type = RowStatus
_HwKompellaVpnTargetRowStatus_Object = MibTableColumn
hwKompellaVpnTargetRowStatus = _HwKompellaVpnTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 2, 1, 51),
    _HwKompellaVpnTargetRowStatus_Type()
)
hwKompellaVpnTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVpnTargetRowStatus.setStatus("current")
_HwKompellaCeTable_Object = MibTable
hwKompellaCeTable = _HwKompellaCeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwKompellaCeTable.setStatus("current")
_HwKompellaCeEntry_Object = MibTableRow
hwKompellaCeEntry = _HwKompellaCeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 3, 1)
)
hwKompellaCeEntry.setIndexNames(
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnName"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaCeID"),
)
if mibBuilder.loadTexts:
    hwKompellaCeEntry.setStatus("current")


class _HwKompellaCeID_Type(Unsigned32):
    """Custom type hwKompellaCeID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 249),
    )


_HwKompellaCeID_Type.__name__ = "Unsigned32"
_HwKompellaCeID_Object = MibTableColumn
hwKompellaCeID = _HwKompellaCeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 3, 1, 1),
    _HwKompellaCeID_Type()
)
hwKompellaCeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKompellaCeID.setStatus("current")


class _HwKompellaCeName_Type(DisplayString):
    """Custom type hwKompellaCeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HwKompellaCeName_Type.__name__ = "DisplayString"
_HwKompellaCeName_Object = MibTableColumn
hwKompellaCeName = _HwKompellaCeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 3, 1, 2),
    _HwKompellaCeName_Type()
)
hwKompellaCeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaCeName.setStatus("current")


class _HwKompellaCeIDRange_Type(Unsigned32):
    """Custom type hwKompellaCeIDRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 250),
    )


_HwKompellaCeIDRange_Type.__name__ = "Unsigned32"
_HwKompellaCeIDRange_Object = MibTableColumn
hwKompellaCeIDRange = _HwKompellaCeIDRange_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 3, 1, 3),
    _HwKompellaCeIDRange_Type()
)
hwKompellaCeIDRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaCeIDRange.setStatus("current")


class _HwKompellaCeIDDefaultOffset_Type(Unsigned32):
    """Custom type hwKompellaCeIDDefaultOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwKompellaCeIDDefaultOffset_Type.__name__ = "Unsigned32"
_HwKompellaCeIDDefaultOffset_Object = MibTableColumn
hwKompellaCeIDDefaultOffset = _HwKompellaCeIDDefaultOffset_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 3, 1, 4),
    _HwKompellaCeIDDefaultOffset_Type()
)
hwKompellaCeIDDefaultOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaCeIDDefaultOffset.setStatus("current")
_HwKompellaCeRowStatus_Type = RowStatus
_HwKompellaCeRowStatus_Object = MibTableColumn
hwKompellaCeRowStatus = _HwKompellaCeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 3, 1, 51),
    _HwKompellaCeRowStatus_Type()
)
hwKompellaCeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaCeRowStatus.setStatus("current")
_HwKompellaVcTable_Object = MibTable
hwKompellaVcTable = _HwKompellaVcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwKompellaVcTable.setStatus("current")
_HwKompellaVcEntry_Object = MibTableRow
hwKompellaVcEntry = _HwKompellaVcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1)
)
hwKompellaVcEntry.setIndexNames(
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnName"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaCeID"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVcIfIndex"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVcRmtCeID"),
)
if mibBuilder.loadTexts:
    hwKompellaVcEntry.setStatus("current")
_HwKompellaVcIfIndex_Type = InterfaceIndex
_HwKompellaVcIfIndex_Object = MibTableColumn
hwKompellaVcIfIndex = _HwKompellaVcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 1),
    _HwKompellaVcIfIndex_Type()
)
hwKompellaVcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKompellaVcIfIndex.setStatus("current")


class _HwKompellaVcRmtCeID_Type(Unsigned32):
    """Custom type hwKompellaVcRmtCeID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 249),
    )


_HwKompellaVcRmtCeID_Type.__name__ = "Unsigned32"
_HwKompellaVcRmtCeID_Object = MibTableColumn
hwKompellaVcRmtCeID = _HwKompellaVcRmtCeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 2),
    _HwKompellaVcRmtCeID_Type()
)
hwKompellaVcRmtCeID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKompellaVcRmtCeID.setStatus("current")
_HwKompellaVcInboundLabel_Type = Unsigned32
_HwKompellaVcInboundLabel_Object = MibTableColumn
hwKompellaVcInboundLabel = _HwKompellaVcInboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 3),
    _HwKompellaVcInboundLabel_Type()
)
hwKompellaVcInboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcInboundLabel.setStatus("current")
_HwKompellaVcOutboundLabel_Type = Unsigned32
_HwKompellaVcOutboundLabel_Object = MibTableColumn
hwKompellaVcOutboundLabel = _HwKompellaVcOutboundLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 4),
    _HwKompellaVcOutboundLabel_Type()
)
hwKompellaVcOutboundLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcOutboundLabel.setStatus("current")
_HwKompellaVcCtrlWord_Type = HWEnableValue
_HwKompellaVcCtrlWord_Object = MibTableColumn
hwKompellaVcCtrlWord = _HwKompellaVcCtrlWord_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 5),
    _HwKompellaVcCtrlWord_Type()
)
hwKompellaVcCtrlWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVcCtrlWord.setStatus("current")


class _HwKompellaVcTnlPolicyName_Type(OctetString):
    """Custom type hwKompellaVcTnlPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 39),
    )


_HwKompellaVcTnlPolicyName_Type.__name__ = "OctetString"
_HwKompellaVcTnlPolicyName_Object = MibTableColumn
hwKompellaVcTnlPolicyName = _HwKompellaVcTnlPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 6),
    _HwKompellaVcTnlPolicyName_Type()
)
hwKompellaVcTnlPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVcTnlPolicyName.setStatus("current")


class _HwKompellaVcVlanTagMode_Type(Integer32):
    """Custom type hwKompellaVcVlanTagMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("raw", 1),
          ("rawTagNotConfiged", 255),
          ("tagged", 2))
    )


_HwKompellaVcVlanTagMode_Type.__name__ = "Integer32"
_HwKompellaVcVlanTagMode_Object = MibTableColumn
hwKompellaVcVlanTagMode = _HwKompellaVcVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 7),
    _HwKompellaVcVlanTagMode_Type()
)
hwKompellaVcVlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVcVlanTagMode.setStatus("current")
_HwKompellaVcSecondary_Type = TruthValue
_HwKompellaVcSecondary_Object = MibTableColumn
hwKompellaVcSecondary = _HwKompellaVcSecondary_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 8),
    _HwKompellaVcSecondary_Type()
)
hwKompellaVcSecondary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVcSecondary.setStatus("current")
_HwKompellaOAMSync_Type = TruthValue
_HwKompellaOAMSync_Object = MibTableColumn
hwKompellaOAMSync = _HwKompellaOAMSync_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 9),
    _HwKompellaOAMSync_Type()
)
hwKompellaOAMSync.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaOAMSync.setStatus("current")
_HwKompellaVCForBFDIndex_Type = Unsigned32
_HwKompellaVCForBFDIndex_Object = MibTableColumn
hwKompellaVCForBFDIndex = _HwKompellaVCForBFDIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 10),
    _HwKompellaVCForBFDIndex_Type()
)
hwKompellaVCForBFDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVCForBFDIndex.setStatus("current")


class _HwKompellaVcOperStatus_Type(Integer32):
    """Custom type hwKompellaVcOperStatus based on Integer32"""
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


_HwKompellaVcOperStatus_Type.__name__ = "Integer32"
_HwKompellaVcOperStatus_Object = MibTableColumn
hwKompellaVcOperStatus = _HwKompellaVcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 11),
    _HwKompellaVcOperStatus_Type()
)
hwKompellaVcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcOperStatus.setStatus("current")
_HwKompellaVcRerouteDelayTime_Type = Unsigned32
_HwKompellaVcRerouteDelayTime_Object = MibTableColumn
hwKompellaVcRerouteDelayTime = _HwKompellaVcRerouteDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 12),
    _HwKompellaVcRerouteDelayTime_Type()
)
hwKompellaVcRerouteDelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVcRerouteDelayTime.setStatus("current")
_HwKompellaVcRerouteResumeTime_Type = Unsigned32
_HwKompellaVcRerouteResumeTime_Object = MibTableColumn
hwKompellaVcRerouteResumeTime = _HwKompellaVcRerouteResumeTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 13),
    _HwKompellaVcRerouteResumeTime_Type()
)
hwKompellaVcRerouteResumeTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVcRerouteResumeTime.setStatus("current")


class _HwKompellaVcReroutePolicy_Type(Integer32):
    """Custom type hwKompellaVcReroutePolicy based on Integer32"""
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
        *(("delay", 1),
          ("err", 5),
          ("immediately", 2),
          ("immediatelySwitch", 7),
          ("invalid", 6),
          ("never", 3),
          ("none", 4))
    )


_HwKompellaVcReroutePolicy_Type.__name__ = "Integer32"
_HwKompellaVcReroutePolicy_Object = MibTableColumn
hwKompellaVcReroutePolicy = _HwKompellaVcReroutePolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 14),
    _HwKompellaVcReroutePolicy_Type()
)
hwKompellaVcReroutePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcReroutePolicy.setStatus("current")
_HwKompellaVcRerouteReason_Type = HWL2VpnStateChangeReason
_HwKompellaVcRerouteReason_Object = MibTableColumn
hwKompellaVcRerouteReason = _HwKompellaVcRerouteReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 15),
    _HwKompellaVcRerouteReason_Type()
)
hwKompellaVcRerouteReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcRerouteReason.setStatus("current")
_HwKompellaVcLastRerouteTime_Type = Unsigned32
_HwKompellaVcLastRerouteTime_Object = MibTableColumn
hwKompellaVcLastRerouteTime = _HwKompellaVcLastRerouteTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 16),
    _HwKompellaVcLastRerouteTime_Type()
)
hwKompellaVcLastRerouteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcLastRerouteTime.setStatus("current")
_HwKompellaVcManualSetFault_Type = TruthValue
_HwKompellaVcManualSetFault_Object = MibTableColumn
hwKompellaVcManualSetFault = _HwKompellaVcManualSetFault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 17),
    _HwKompellaVcManualSetFault_Type()
)
hwKompellaVcManualSetFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcManualSetFault.setStatus("current")
_HwKompellaVcIsActive_Type = TruthValue
_HwKompellaVcIsActive_Object = MibTableColumn
hwKompellaVcIsActive = _HwKompellaVcIsActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 18),
    _HwKompellaVcIsActive_Type()
)
hwKompellaVcIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcIsActive.setStatus("current")


class _HwKompellaACStatus_Type(Integer32):
    """Custom type hwKompellaACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("downNotify", 6),
          ("notify", 4),
          ("notifyDown", 5),
          ("up", 1))
    )


_HwKompellaACStatus_Type.__name__ = "Integer32"
_HwKompellaACStatus_Object = MibTableColumn
hwKompellaACStatus = _HwKompellaACStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 19),
    _HwKompellaACStatus_Type()
)
hwKompellaACStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaACStatus.setStatus("current")


class _HwKompellaACOAMStatus_Type(Integer32):
    """Custom type hwKompellaACOAMStatus based on Integer32"""
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


_HwKompellaACOAMStatus_Type.__name__ = "Integer32"
_HwKompellaACOAMStatus_Object = MibTableColumn
hwKompellaACOAMStatus = _HwKompellaACOAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 20),
    _HwKompellaACOAMStatus_Type()
)
hwKompellaACOAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaACOAMStatus.setStatus("current")


class _HwKompellaVcBFDDetectMultiplier_Type(Unsigned32):
    """Custom type hwKompellaVcBFDDetectMultiplier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 50),
    )


_HwKompellaVcBFDDetectMultiplier_Type.__name__ = "Unsigned32"
_HwKompellaVcBFDDetectMultiplier_Object = MibTableColumn
hwKompellaVcBFDDetectMultiplier = _HwKompellaVcBFDDetectMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 21),
    _HwKompellaVcBFDDetectMultiplier_Type()
)
hwKompellaVcBFDDetectMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcBFDDetectMultiplier.setStatus("current")


class _HwKompellaVcBFDMinReceiveInterval_Type(Unsigned32):
    """Custom type hwKompellaVcBFDMinReceiveInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000),
    )


_HwKompellaVcBFDMinReceiveInterval_Type.__name__ = "Unsigned32"
_HwKompellaVcBFDMinReceiveInterval_Object = MibTableColumn
hwKompellaVcBFDMinReceiveInterval = _HwKompellaVcBFDMinReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 22),
    _HwKompellaVcBFDMinReceiveInterval_Type()
)
hwKompellaVcBFDMinReceiveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcBFDMinReceiveInterval.setStatus("current")


class _HwKompellaVcBFDMinTransmitInterval_Type(Unsigned32):
    """Custom type hwKompellaVcBFDMinTransmitInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1000),
    )


_HwKompellaVcBFDMinTransmitInterval_Type.__name__ = "Unsigned32"
_HwKompellaVcBFDMinTransmitInterval_Object = MibTableColumn
hwKompellaVcBFDMinTransmitInterval = _HwKompellaVcBFDMinTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 23),
    _HwKompellaVcBFDMinTransmitInterval_Type()
)
hwKompellaVcBFDMinTransmitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcBFDMinTransmitInterval.setStatus("current")
_HwKompellaVcDynamicBFDDetect_Type = TruthValue
_HwKompellaVcDynamicBFDDetect_Object = MibTableColumn
hwKompellaVcDynamicBFDDetect = _HwKompellaVcDynamicBFDDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 24),
    _HwKompellaVcDynamicBFDDetect_Type()
)
hwKompellaVcDynamicBFDDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcDynamicBFDDetect.setStatus("current")


class _HwKompellaEthOamType_Type(Integer32):
    """Custom type hwKompellaEthOamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethOam1ag", 1),
          ("ethOam3ah", 2),
          ("noEthOamCfg", 3))
    )


_HwKompellaEthOamType_Type.__name__ = "Integer32"
_HwKompellaEthOamType_Object = MibTableColumn
hwKompellaEthOamType = _HwKompellaEthOamType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 25),
    _HwKompellaEthOamType_Type()
)
hwKompellaEthOamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaEthOamType.setStatus("current")


class _HwKompellaCfmMaIndex_Type(Unsigned32):
    """Custom type hwKompellaCfmMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_HwKompellaCfmMaIndex_Type.__name__ = "Unsigned32"
_HwKompellaCfmMaIndex_Object = MibTableColumn
hwKompellaCfmMaIndex = _HwKompellaCfmMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 26),
    _HwKompellaCfmMaIndex_Type()
)
hwKompellaCfmMaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaCfmMaIndex.setStatus("current")
_HwKompellaVcPeerAddr_Type = IpAddress
_HwKompellaVcPeerAddr_Object = MibTableColumn
hwKompellaVcPeerAddr = _HwKompellaVcPeerAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 27),
    _HwKompellaVcPeerAddr_Type()
)
hwKompellaVcPeerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcPeerAddr.setStatus("current")
_HwKompellaVcRowStatus_Type = RowStatus
_HwKompellaVcRowStatus_Object = MibTableColumn
hwKompellaVcRowStatus = _HwKompellaVcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 4, 1, 51),
    _HwKompellaVcRowStatus_Type()
)
hwKompellaVcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwKompellaVcRowStatus.setStatus("current")
_HwKompellaVcTnlTable_Object = MibTable
hwKompellaVcTnlTable = _HwKompellaVcTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwKompellaVcTnlTable.setStatus("current")
_HwKompellaVcTnlEntry_Object = MibTableRow
hwKompellaVcTnlEntry = _HwKompellaVcTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 5, 1)
)
hwKompellaVcTnlEntry.setIndexNames(
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnName"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaCeID"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVcIfIndex"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVcRmtCeID"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVcTnlIndex"),
)
if mibBuilder.loadTexts:
    hwKompellaVcTnlEntry.setStatus("current")
_HwKompellaVcTnlIndex_Type = Unsigned32
_HwKompellaVcTnlIndex_Object = MibTableColumn
hwKompellaVcTnlIndex = _HwKompellaVcTnlIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 5, 1, 1),
    _HwKompellaVcTnlIndex_Type()
)
hwKompellaVcTnlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwKompellaVcTnlIndex.setStatus("current")


class _HwKompellaVcTnlType_Type(Integer32):
    """Custom type hwKompellaVcTnlType based on Integer32"""
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
        *(("crLsp", 5),
          ("gre", 2),
          ("ipsec", 4),
          ("l2tp", 3),
          ("lsp", 1))
    )


_HwKompellaVcTnlType_Type.__name__ = "Integer32"
_HwKompellaVcTnlType_Object = MibTableColumn
hwKompellaVcTnlType = _HwKompellaVcTnlType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 5, 1, 2),
    _HwKompellaVcTnlType_Type()
)
hwKompellaVcTnlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcTnlType.setStatus("current")
_HwKompellaTnlForBfdIndex_Type = Unsigned32
_HwKompellaTnlForBfdIndex_Object = MibTableColumn
hwKompellaTnlForBfdIndex = _HwKompellaTnlForBfdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 5, 1, 3),
    _HwKompellaTnlForBfdIndex_Type()
)
hwKompellaTnlForBfdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaTnlForBfdIndex.setStatus("current")
_HwKompellaVcStatisticsTable_Object = MibTable
hwKompellaVcStatisticsTable = _HwKompellaVcStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hwKompellaVcStatisticsTable.setStatus("current")
_HwKompellaVcStatisticsEntry_Object = MibTableRow
hwKompellaVcStatisticsEntry = _HwKompellaVcStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 6, 1)
)
hwKompellaVcStatisticsEntry.setIndexNames(
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVpnName"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaCeID"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVcIfIndex"),
    (0, "HUAWEI-KOMPELLA-MIB", "hwKompellaVcRmtCeID"),
)
if mibBuilder.loadTexts:
    hwKompellaVcStatisticsEntry.setStatus("current")
_HwKompellaVcStatisticsRcvPkts_Type = Counter64
_HwKompellaVcStatisticsRcvPkts_Object = MibTableColumn
hwKompellaVcStatisticsRcvPkts = _HwKompellaVcStatisticsRcvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 6, 1, 1),
    _HwKompellaVcStatisticsRcvPkts_Type()
)
hwKompellaVcStatisticsRcvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcStatisticsRcvPkts.setStatus("current")
_HwKompellaVcStatisticsRcvBytes_Type = Counter64
_HwKompellaVcStatisticsRcvBytes_Object = MibTableColumn
hwKompellaVcStatisticsRcvBytes = _HwKompellaVcStatisticsRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 6, 1, 2),
    _HwKompellaVcStatisticsRcvBytes_Type()
)
hwKompellaVcStatisticsRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcStatisticsRcvBytes.setStatus("current")
_HwKompellaVcStatisticsSndPkts_Type = Counter64
_HwKompellaVcStatisticsSndPkts_Object = MibTableColumn
hwKompellaVcStatisticsSndPkts = _HwKompellaVcStatisticsSndPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 6, 1, 3),
    _HwKompellaVcStatisticsSndPkts_Type()
)
hwKompellaVcStatisticsSndPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcStatisticsSndPkts.setStatus("current")
_HwKompellaVcStatisticsSndBytes_Type = Counter64
_HwKompellaVcStatisticsSndBytes_Object = MibTableColumn
hwKompellaVcStatisticsSndBytes = _HwKompellaVcStatisticsSndBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 6, 1, 4),
    _HwKompellaVcStatisticsSndBytes_Type()
)
hwKompellaVcStatisticsSndBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwKompellaVcStatisticsSndBytes.setStatus("current")
_HwKompellaVcUpDownNotifEnable_Type = HWEnableValue
_HwKompellaVcUpDownNotifEnable_Object = MibScalar
hwKompellaVcUpDownNotifEnable = _HwKompellaVcUpDownNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 7),
    _HwKompellaVcUpDownNotifEnable_Type()
)
hwKompellaVcUpDownNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwKompellaVcUpDownNotifEnable.setStatus("current")
_HwKompellaVcDeletedNotifEnable_Type = HWEnableValue
_HwKompellaVcDeletedNotifEnable_Object = MibScalar
hwKompellaVcDeletedNotifEnable = _HwKompellaVcDeletedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 8),
    _HwKompellaVcDeletedNotifEnable_Type()
)
hwKompellaVcDeletedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwKompellaVcDeletedNotifEnable.setStatus("current")
_HwKompellaSwitchNotifEnable_Type = HWEnableValue
_HwKompellaSwitchNotifEnable_Object = MibScalar
hwKompellaSwitchNotifEnable = _HwKompellaSwitchNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 9),
    _HwKompellaSwitchNotifEnable_Type()
)
hwKompellaSwitchNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwKompellaSwitchNotifEnable.setStatus("current")
_HwKompellaVcStateChangeReason_Type = HWL2VpnStateChangeReason
_HwKompellaVcStateChangeReason_Object = MibScalar
hwKompellaVcStateChangeReason = _HwKompellaVcStateChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 10),
    _HwKompellaVcStateChangeReason_Type()
)
hwKompellaVcStateChangeReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwKompellaVcStateChangeReason.setStatus("current")


class _HwKompellaSwitchRmtCEID_Type(Unsigned32):
    """Custom type hwKompellaSwitchRmtCEID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 249),
    )


_HwKompellaSwitchRmtCEID_Type.__name__ = "Unsigned32"
_HwKompellaSwitchRmtCEID_Object = MibScalar
hwKompellaSwitchRmtCEID = _HwKompellaSwitchRmtCEID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 1, 11),
    _HwKompellaSwitchRmtCEID_Type()
)
hwKompellaSwitchRmtCEID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwKompellaSwitchRmtCEID.setStatus("current")
_HwKompellaMIBTraps_ObjectIdentity = ObjectIdentity
hwKompellaMIBTraps = _HwKompellaMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 2)
)
_HwKompellaMIBConformance_ObjectIdentity = ObjectIdentity
hwKompellaMIBConformance = _HwKompellaMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3)
)
_HwKompellaMIBCompliances_ObjectIdentity = ObjectIdentity
hwKompellaMIBCompliances = _HwKompellaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 1)
)
_HwKompellaMIBGroups_ObjectIdentity = ObjectIdentity
hwKompellaMIBGroups = _HwKompellaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2)
)

# Managed Objects groups

hwKompellaVpnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 1)
)
hwKompellaVpnGroup.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVpnVcType"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVpnRouteDistinguisher"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVpnCtrlWord"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVpnMtu"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVpnRowStatus"))
)
if mibBuilder.loadTexts:
    hwKompellaVpnGroup.setStatus("current")

hwKompellaVpnTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 2)
)
hwKompellaVpnTargetGroup.setObjects(
    ("HUAWEI-KOMPELLA-MIB", "hwKompellaVpnTargetRowStatus")
)
if mibBuilder.loadTexts:
    hwKompellaVpnTargetGroup.setStatus("current")

hwKompellaCeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 3)
)
hwKompellaCeGroup.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaCeName"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaCeIDRange"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaCeIDDefaultOffset"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaCeRowStatus"))
)
if mibBuilder.loadTexts:
    hwKompellaCeGroup.setStatus("current")

hwKompellaVcGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 4)
)
hwKompellaVcGroup.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcInboundLabel"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcOutboundLabel"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcCtrlWord"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcTnlPolicyName"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcVlanTagMode"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcSecondary"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaOAMSync"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVCForBFDIndex"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcOperStatus"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcRerouteDelayTime"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcRerouteResumeTime"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcReroutePolicy"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcRerouteReason"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcLastRerouteTime"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcManualSetFault"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcIsActive"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaACStatus"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaACOAMStatus"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcBFDDetectMultiplier"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcBFDMinReceiveInterval"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcBFDMinTransmitInterval"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcDynamicBFDDetect"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaEthOamType"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaCfmMaIndex"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcRowStatus"))
)
if mibBuilder.loadTexts:
    hwKompellaVcGroup.setStatus("current")

hwKompellaVcTnlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 5)
)
hwKompellaVcTnlGroup.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcTnlType"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaTnlForBfdIndex"))
)
if mibBuilder.loadTexts:
    hwKompellaVcTnlGroup.setStatus("current")

hwKompellaVcStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 6)
)
hwKompellaVcStatisticsGroup.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStatisticsRcvPkts"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStatisticsRcvBytes"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStatisticsSndPkts"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStatisticsSndBytes"))
)
if mibBuilder.loadTexts:
    hwKompellaVcStatisticsGroup.setStatus("current")

hwKompellaNotificationControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 7)
)
hwKompellaNotificationControlGroup.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcUpDownNotifEnable"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcDeletedNotifEnable"))
)
if mibBuilder.loadTexts:
    hwKompellaNotificationControlGroup.setStatus("current")

hwKompellaVCSwitchControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 8)
)
hwKompellaVCSwitchControlGroup.setObjects(
    ("HUAWEI-KOMPELLA-MIB", "hwKompellaSwitchNotifEnable")
)
if mibBuilder.loadTexts:
    hwKompellaVCSwitchControlGroup.setStatus("current")

hwKompellaVcStateChangeReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 9)
)
hwKompellaVcStateChangeReasonGroup.setObjects(
    ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStateChangeReason")
)
if mibBuilder.loadTexts:
    hwKompellaVcStateChangeReasonGroup.setStatus("current")

hwKompellaSwitchRmtCEIDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 10)
)
hwKompellaSwitchRmtCEIDGroup.setObjects(
    ("HUAWEI-KOMPELLA-MIB", "hwKompellaSwitchRmtCEID")
)
if mibBuilder.loadTexts:
    hwKompellaSwitchRmtCEIDGroup.setStatus("current")


# Notification objects

hwKompellaVcDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 2, 1)
)
hwKompellaVcDown.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcSecondary"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStateChangeReason"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcPeerAddr"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcTnlPolicyName"))
)
if mibBuilder.loadTexts:
    hwKompellaVcDown.setStatus(
        "current"
    )

hwKompellaVcUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 2, 2)
)
hwKompellaVcUp.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcSecondary"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStateChangeReason"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcPeerAddr"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcTnlPolicyName"))
)
if mibBuilder.loadTexts:
    hwKompellaVcUp.setStatus(
        "current"
    )

hwKompellaSwitchWtoP = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 2, 3)
)
hwKompellaSwitchWtoP.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcCtrlWord"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaSwitchRmtCEID"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStateChangeReason"))
)
if mibBuilder.loadTexts:
    hwKompellaSwitchWtoP.setStatus(
        "current"
    )

hwKompellaSwitchPtoW = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 2, 4)
)
hwKompellaSwitchPtoW.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcCtrlWord"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaSwitchRmtCEID"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcStateChangeReason"))
)
if mibBuilder.loadTexts:
    hwKompellaSwitchPtoW.setStatus(
        "current"
    )

hwKompellaVcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 2, 5)
)
hwKompellaVcDeleted.setObjects(
    ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcSecondary")
)
if mibBuilder.loadTexts:
    hwKompellaVcDeleted.setStatus(
        "current"
    )


# Notifications groups

hwKompellaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 2, 11)
)
hwKompellaNotificationGroup.setObjects(
      *(("HUAWEI-KOMPELLA-MIB", "hwKompellaVcDown"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcUp"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaSwitchWtoP"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaSwitchPtoW"),
        ("HUAWEI-KOMPELLA-MIB", "hwKompellaVcDeleted"))
)
if mibBuilder.loadTexts:
    hwKompellaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwKompellaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 119, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwKompellaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-KOMPELLA-MIB",
    **{"hwL2Vpn": hwL2Vpn,
       "hwL2VpnKompella": hwL2VpnKompella,
       "hwKompellaMIBObjects": hwKompellaMIBObjects,
       "hwKompellaVpnTable": hwKompellaVpnTable,
       "hwKompellaVpnEntry": hwKompellaVpnEntry,
       "hwKompellaVpnName": hwKompellaVpnName,
       "hwKompellaVpnVcType": hwKompellaVpnVcType,
       "hwKompellaVpnRouteDistinguisher": hwKompellaVpnRouteDistinguisher,
       "hwKompellaVpnCtrlWord": hwKompellaVpnCtrlWord,
       "hwKompellaVpnMtu": hwKompellaVpnMtu,
       "hwKompellaVpnRowStatus": hwKompellaVpnRowStatus,
       "hwKompellaVpnTargetTable": hwKompellaVpnTargetTable,
       "hwKompellaVpnTargetEntry": hwKompellaVpnTargetEntry,
       "hwKompellaVpnTargetType": hwKompellaVpnTargetType,
       "hwKompellaVpnTarget": hwKompellaVpnTarget,
       "hwKompellaVpnTargetRowStatus": hwKompellaVpnTargetRowStatus,
       "hwKompellaCeTable": hwKompellaCeTable,
       "hwKompellaCeEntry": hwKompellaCeEntry,
       "hwKompellaCeID": hwKompellaCeID,
       "hwKompellaCeName": hwKompellaCeName,
       "hwKompellaCeIDRange": hwKompellaCeIDRange,
       "hwKompellaCeIDDefaultOffset": hwKompellaCeIDDefaultOffset,
       "hwKompellaCeRowStatus": hwKompellaCeRowStatus,
       "hwKompellaVcTable": hwKompellaVcTable,
       "hwKompellaVcEntry": hwKompellaVcEntry,
       "hwKompellaVcIfIndex": hwKompellaVcIfIndex,
       "hwKompellaVcRmtCeID": hwKompellaVcRmtCeID,
       "hwKompellaVcInboundLabel": hwKompellaVcInboundLabel,
       "hwKompellaVcOutboundLabel": hwKompellaVcOutboundLabel,
       "hwKompellaVcCtrlWord": hwKompellaVcCtrlWord,
       "hwKompellaVcTnlPolicyName": hwKompellaVcTnlPolicyName,
       "hwKompellaVcVlanTagMode": hwKompellaVcVlanTagMode,
       "hwKompellaVcSecondary": hwKompellaVcSecondary,
       "hwKompellaOAMSync": hwKompellaOAMSync,
       "hwKompellaVCForBFDIndex": hwKompellaVCForBFDIndex,
       "hwKompellaVcOperStatus": hwKompellaVcOperStatus,
       "hwKompellaVcRerouteDelayTime": hwKompellaVcRerouteDelayTime,
       "hwKompellaVcRerouteResumeTime": hwKompellaVcRerouteResumeTime,
       "hwKompellaVcReroutePolicy": hwKompellaVcReroutePolicy,
       "hwKompellaVcRerouteReason": hwKompellaVcRerouteReason,
       "hwKompellaVcLastRerouteTime": hwKompellaVcLastRerouteTime,
       "hwKompellaVcManualSetFault": hwKompellaVcManualSetFault,
       "hwKompellaVcIsActive": hwKompellaVcIsActive,
       "hwKompellaACStatus": hwKompellaACStatus,
       "hwKompellaACOAMStatus": hwKompellaACOAMStatus,
       "hwKompellaVcBFDDetectMultiplier": hwKompellaVcBFDDetectMultiplier,
       "hwKompellaVcBFDMinReceiveInterval": hwKompellaVcBFDMinReceiveInterval,
       "hwKompellaVcBFDMinTransmitInterval": hwKompellaVcBFDMinTransmitInterval,
       "hwKompellaVcDynamicBFDDetect": hwKompellaVcDynamicBFDDetect,
       "hwKompellaEthOamType": hwKompellaEthOamType,
       "hwKompellaCfmMaIndex": hwKompellaCfmMaIndex,
       "hwKompellaVcPeerAddr": hwKompellaVcPeerAddr,
       "hwKompellaVcRowStatus": hwKompellaVcRowStatus,
       "hwKompellaVcTnlTable": hwKompellaVcTnlTable,
       "hwKompellaVcTnlEntry": hwKompellaVcTnlEntry,
       "hwKompellaVcTnlIndex": hwKompellaVcTnlIndex,
       "hwKompellaVcTnlType": hwKompellaVcTnlType,
       "hwKompellaTnlForBfdIndex": hwKompellaTnlForBfdIndex,
       "hwKompellaVcStatisticsTable": hwKompellaVcStatisticsTable,
       "hwKompellaVcStatisticsEntry": hwKompellaVcStatisticsEntry,
       "hwKompellaVcStatisticsRcvPkts": hwKompellaVcStatisticsRcvPkts,
       "hwKompellaVcStatisticsRcvBytes": hwKompellaVcStatisticsRcvBytes,
       "hwKompellaVcStatisticsSndPkts": hwKompellaVcStatisticsSndPkts,
       "hwKompellaVcStatisticsSndBytes": hwKompellaVcStatisticsSndBytes,
       "hwKompellaVcUpDownNotifEnable": hwKompellaVcUpDownNotifEnable,
       "hwKompellaVcDeletedNotifEnable": hwKompellaVcDeletedNotifEnable,
       "hwKompellaSwitchNotifEnable": hwKompellaSwitchNotifEnable,
       "hwKompellaVcStateChangeReason": hwKompellaVcStateChangeReason,
       "hwKompellaSwitchRmtCEID": hwKompellaSwitchRmtCEID,
       "hwKompellaMIBTraps": hwKompellaMIBTraps,
       "hwKompellaVcDown": hwKompellaVcDown,
       "hwKompellaVcUp": hwKompellaVcUp,
       "hwKompellaSwitchWtoP": hwKompellaSwitchWtoP,
       "hwKompellaSwitchPtoW": hwKompellaSwitchPtoW,
       "hwKompellaVcDeleted": hwKompellaVcDeleted,
       "hwKompellaMIBConformance": hwKompellaMIBConformance,
       "hwKompellaMIBCompliances": hwKompellaMIBCompliances,
       "hwKompellaMIBCompliance": hwKompellaMIBCompliance,
       "hwKompellaMIBGroups": hwKompellaMIBGroups,
       "hwKompellaVpnGroup": hwKompellaVpnGroup,
       "hwKompellaVpnTargetGroup": hwKompellaVpnTargetGroup,
       "hwKompellaCeGroup": hwKompellaCeGroup,
       "hwKompellaVcGroup": hwKompellaVcGroup,
       "hwKompellaVcTnlGroup": hwKompellaVcTnlGroup,
       "hwKompellaVcStatisticsGroup": hwKompellaVcStatisticsGroup,
       "hwKompellaNotificationControlGroup": hwKompellaNotificationControlGroup,
       "hwKompellaVCSwitchControlGroup": hwKompellaVCSwitchControlGroup,
       "hwKompellaVcStateChangeReasonGroup": hwKompellaVcStateChangeReasonGroup,
       "hwKompellaSwitchRmtCEIDGroup": hwKompellaSwitchRmtCEIDGroup,
       "hwKompellaNotificationGroup": hwKompellaNotificationGroup}
)
