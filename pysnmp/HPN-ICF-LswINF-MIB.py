# SNMP MIB module (HPN-ICF-LswINF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-LswINF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:44 2024
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

(hpnicflswCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicflswCommon")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

hpnicfLswL2InfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5)
)
hpnicfLswL2InfMib.setRevisions(
        ("2001-06-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


class VlanIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class DropDirection(Integer32, TextualConvention):
    status = "current"
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
        *(("disable", 1),
          ("enableBoth", 4),
          ("enableInbound", 2),
          ("enableOutbound", 3))
    )



class SpeedModeFlag(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_HpnicfLswExtInterface_ObjectIdentity = ObjectIdentity
hpnicfLswExtInterface = _HpnicfLswExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1)
)
_HpnicfifXXTable_Object = MibTable
hpnicfifXXTable = _HpnicfifXXTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfifXXTable.setStatus("current")
_HpnicfifXXEntry_Object = MibTableRow
hpnicfifXXEntry = _HpnicfifXXEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1)
)
hpnicfifXXEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfifXXEntry.setStatus("current")
_HpnicfifUnBoundPort_Type = TruthValue
_HpnicfifUnBoundPort_Object = MibTableColumn
hpnicfifUnBoundPort = _HpnicfifUnBoundPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 1),
    _HpnicfifUnBoundPort_Type()
)
hpnicfifUnBoundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifUnBoundPort.setStatus("current")
_HpnicfifISPhyPort_Type = TruthValue
_HpnicfifISPhyPort_Object = MibTableColumn
hpnicfifISPhyPort = _HpnicfifISPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 2),
    _HpnicfifISPhyPort_Type()
)
hpnicfifISPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifISPhyPort.setStatus("current")
_HpnicfifAggregatePort_Type = TruthValue
_HpnicfifAggregatePort_Object = MibTableColumn
hpnicfifAggregatePort = _HpnicfifAggregatePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 3),
    _HpnicfifAggregatePort_Type()
)
hpnicfifAggregatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifAggregatePort.setStatus("current")
_HpnicfifMirrorPort_Type = TruthValue
_HpnicfifMirrorPort_Object = MibTableColumn
hpnicfifMirrorPort = _HpnicfifMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 4),
    _HpnicfifMirrorPort_Type()
)
hpnicfifMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifMirrorPort.setStatus("current")


class _HpnicfifVLANType_Type(Integer32):
    """Custom type hpnicfifVLANType based on Integer32"""
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
        *(("access", 2),
          ("fabric", 4),
          ("hybrid", 3),
          ("vLANTrunk", 1))
    )


_HpnicfifVLANType_Type.__name__ = "Integer32"
_HpnicfifVLANType_Object = MibTableColumn
hpnicfifVLANType = _HpnicfifVLANType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 5),
    _HpnicfifVLANType_Type()
)
hpnicfifVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifVLANType.setStatus("current")


class _HpnicfifMcastControl_Type(Integer32):
    """Custom type hpnicfifMcastControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfifMcastControl_Type.__name__ = "Integer32"
_HpnicfifMcastControl_Object = MibTableColumn
hpnicfifMcastControl = _HpnicfifMcastControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 6),
    _HpnicfifMcastControl_Type()
)
hpnicfifMcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifMcastControl.setStatus("current")
_HpnicfifFlowControl_Type = TruthValue
_HpnicfifFlowControl_Object = MibTableColumn
hpnicfifFlowControl = _HpnicfifFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 7),
    _HpnicfifFlowControl_Type()
)
hpnicfifFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifFlowControl.setStatus("current")
_HpnicfifSrcMacControl_Type = TruthValue
_HpnicfifSrcMacControl_Object = MibTableColumn
hpnicfifSrcMacControl = _HpnicfifSrcMacControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 8),
    _HpnicfifSrcMacControl_Type()
)
hpnicfifSrcMacControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifSrcMacControl.setStatus("current")


class _HpnicfifClearStat_Type(Integer32):
    """Custom type hpnicfifClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_HpnicfifClearStat_Type.__name__ = "Integer32"
_HpnicfifClearStat_Object = MibTableColumn
hpnicfifClearStat = _HpnicfifClearStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 9),
    _HpnicfifClearStat_Type()
)
hpnicfifClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifClearStat.setStatus("current")
_HpnicfifXXBasePortIndex_Type = Integer32
_HpnicfifXXBasePortIndex_Object = MibTableColumn
hpnicfifXXBasePortIndex = _HpnicfifXXBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 10),
    _HpnicfifXXBasePortIndex_Type()
)
hpnicfifXXBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifXXBasePortIndex.setStatus("current")
_HpnicfifXXDevPortIndex_Type = Integer32
_HpnicfifXXDevPortIndex_Object = MibTableColumn
hpnicfifXXDevPortIndex = _HpnicfifXXDevPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 11),
    _HpnicfifXXDevPortIndex_Type()
)
hpnicfifXXDevPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifXXDevPortIndex.setStatus("current")
_HpnicfifPpsMcastControl_Type = Integer32
_HpnicfifPpsMcastControl_Object = MibTableColumn
hpnicfifPpsMcastControl = _HpnicfifPpsMcastControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 12),
    _HpnicfifPpsMcastControl_Type()
)
hpnicfifPpsMcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifPpsMcastControl.setStatus("current")


class _HpnicfifPpsBcastDisValControl_Type(Integer32):
    """Custom type hpnicfifPpsBcastDisValControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpnicfifPpsBcastDisValControl_Type.__name__ = "Integer32"
_HpnicfifPpsBcastDisValControl_Object = MibTableColumn
hpnicfifPpsBcastDisValControl = _HpnicfifPpsBcastDisValControl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 13),
    _HpnicfifPpsBcastDisValControl_Type()
)
hpnicfifPpsBcastDisValControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifPpsBcastDisValControl.setStatus("current")
_HpnicfifUniSuppressionStep_Type = Integer32
_HpnicfifUniSuppressionStep_Object = MibTableColumn
hpnicfifUniSuppressionStep = _HpnicfifUniSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 14),
    _HpnicfifUniSuppressionStep_Type()
)
hpnicfifUniSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifUniSuppressionStep.setStatus("current")
_HpnicfifPpsUniSuppressionMax_Type = Integer32
_HpnicfifPpsUniSuppressionMax_Object = MibTableColumn
hpnicfifPpsUniSuppressionMax = _HpnicfifPpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 15),
    _HpnicfifPpsUniSuppressionMax_Type()
)
hpnicfifPpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifPpsUniSuppressionMax.setStatus("current")
_HpnicfifMulSuppressionStep_Type = Integer32
_HpnicfifMulSuppressionStep_Object = MibTableColumn
hpnicfifMulSuppressionStep = _HpnicfifMulSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 16),
    _HpnicfifMulSuppressionStep_Type()
)
hpnicfifMulSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifMulSuppressionStep.setStatus("current")
_HpnicfifPpsMulSuppressionMax_Type = Integer32
_HpnicfifPpsMulSuppressionMax_Object = MibTableColumn
hpnicfifPpsMulSuppressionMax = _HpnicfifPpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 17),
    _HpnicfifPpsMulSuppressionMax_Type()
)
hpnicfifPpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifPpsMulSuppressionMax.setStatus("current")
_HpnicfifUniSuppression_Type = Integer32
_HpnicfifUniSuppression_Object = MibTableColumn
hpnicfifUniSuppression = _HpnicfifUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 18),
    _HpnicfifUniSuppression_Type()
)
hpnicfifUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifUniSuppression.setStatus("current")
_HpnicfifPpsUniSuppression_Type = Integer32
_HpnicfifPpsUniSuppression_Object = MibTableColumn
hpnicfifPpsUniSuppression = _HpnicfifPpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 19),
    _HpnicfifPpsUniSuppression_Type()
)
hpnicfifPpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifPpsUniSuppression.setStatus("current")
_HpnicfifMulSuppression_Type = Integer32
_HpnicfifMulSuppression_Object = MibTableColumn
hpnicfifMulSuppression = _HpnicfifMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 20),
    _HpnicfifMulSuppression_Type()
)
hpnicfifMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifMulSuppression.setStatus("current")
_HpnicfifPpsMulSuppression_Type = Integer32
_HpnicfifPpsMulSuppression_Object = MibTableColumn
hpnicfifPpsMulSuppression = _HpnicfifPpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 21),
    _HpnicfifPpsMulSuppression_Type()
)
hpnicfifPpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifPpsMulSuppression.setStatus("current")


class _HpnicfifComboActivePort_Type(Integer32):
    """Custom type hpnicfifComboActivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1),
          ("na", 3))
    )


_HpnicfifComboActivePort_Type.__name__ = "Integer32"
_HpnicfifComboActivePort_Object = MibTableColumn
hpnicfifComboActivePort = _HpnicfifComboActivePort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 22),
    _HpnicfifComboActivePort_Type()
)
hpnicfifComboActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifComboActivePort.setStatus("obsolete")
_HpnicfifBMbpsMulSuppressionMax_Type = Integer32
_HpnicfifBMbpsMulSuppressionMax_Object = MibTableColumn
hpnicfifBMbpsMulSuppressionMax = _HpnicfifBMbpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 23),
    _HpnicfifBMbpsMulSuppressionMax_Type()
)
hpnicfifBMbpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifBMbpsMulSuppressionMax.setStatus("current")
_HpnicfifBMbpsMulSuppression_Type = Integer32
_HpnicfifBMbpsMulSuppression_Object = MibTableColumn
hpnicfifBMbpsMulSuppression = _HpnicfifBMbpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 24),
    _HpnicfifBMbpsMulSuppression_Type()
)
hpnicfifBMbpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifBMbpsMulSuppression.setStatus("current")
_HpnicfifBKbpsMulSuppressionMax_Type = Integer32
_HpnicfifBKbpsMulSuppressionMax_Object = MibTableColumn
hpnicfifBKbpsMulSuppressionMax = _HpnicfifBKbpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 25),
    _HpnicfifBKbpsMulSuppressionMax_Type()
)
hpnicfifBKbpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifBKbpsMulSuppressionMax.setStatus("current")
_HpnicfifBKbpsMulSuppressionStep_Type = Integer32
_HpnicfifBKbpsMulSuppressionStep_Object = MibTableColumn
hpnicfifBKbpsMulSuppressionStep = _HpnicfifBKbpsMulSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 26),
    _HpnicfifBKbpsMulSuppressionStep_Type()
)
hpnicfifBKbpsMulSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifBKbpsMulSuppressionStep.setStatus("current")
_HpnicfifBKbpsMulSuppression_Type = Integer32
_HpnicfifBKbpsMulSuppression_Object = MibTableColumn
hpnicfifBKbpsMulSuppression = _HpnicfifBKbpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 27),
    _HpnicfifBKbpsMulSuppression_Type()
)
hpnicfifBKbpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifBKbpsMulSuppression.setStatus("current")


class _HpnicfifUnknownPacketDropMul_Type(DropDirection):
    """Custom type hpnicfifUnknownPacketDropMul based on DropDirection"""


_HpnicfifUnknownPacketDropMul_Object = MibTableColumn
hpnicfifUnknownPacketDropMul = _HpnicfifUnknownPacketDropMul_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 28),
    _HpnicfifUnknownPacketDropMul_Type()
)
hpnicfifUnknownPacketDropMul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifUnknownPacketDropMul.setStatus("current")


class _HpnicfifUnknownPacketDropUni_Type(DropDirection):
    """Custom type hpnicfifUnknownPacketDropUni based on DropDirection"""


_HpnicfifUnknownPacketDropUni_Object = MibTableColumn
hpnicfifUnknownPacketDropUni = _HpnicfifUnknownPacketDropUni_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 29),
    _HpnicfifUnknownPacketDropUni_Type()
)
hpnicfifUnknownPacketDropUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifUnknownPacketDropUni.setStatus("current")
_HpnicfifBMbpsUniSuppressionMax_Type = Integer32
_HpnicfifBMbpsUniSuppressionMax_Object = MibTableColumn
hpnicfifBMbpsUniSuppressionMax = _HpnicfifBMbpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 30),
    _HpnicfifBMbpsUniSuppressionMax_Type()
)
hpnicfifBMbpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifBMbpsUniSuppressionMax.setStatus("current")
_HpnicfifBMbpsUniSuppression_Type = Integer32
_HpnicfifBMbpsUniSuppression_Object = MibTableColumn
hpnicfifBMbpsUniSuppression = _HpnicfifBMbpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 31),
    _HpnicfifBMbpsUniSuppression_Type()
)
hpnicfifBMbpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifBMbpsUniSuppression.setStatus("current")
_HpnicfifBKbpsUniSuppressionMax_Type = Integer32
_HpnicfifBKbpsUniSuppressionMax_Object = MibTableColumn
hpnicfifBKbpsUniSuppressionMax = _HpnicfifBKbpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 32),
    _HpnicfifBKbpsUniSuppressionMax_Type()
)
hpnicfifBKbpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifBKbpsUniSuppressionMax.setStatus("current")
_HpnicfifBKbpsUniSuppressionStep_Type = Integer32
_HpnicfifBKbpsUniSuppressionStep_Object = MibTableColumn
hpnicfifBKbpsUniSuppressionStep = _HpnicfifBKbpsUniSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 33),
    _HpnicfifBKbpsUniSuppressionStep_Type()
)
hpnicfifBKbpsUniSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifBKbpsUniSuppressionStep.setStatus("current")
_HpnicfifBKbpsUniSuppression_Type = Integer32
_HpnicfifBKbpsUniSuppression_Object = MibTableColumn
hpnicfifBKbpsUniSuppression = _HpnicfifBKbpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 34),
    _HpnicfifBKbpsUniSuppression_Type()
)
hpnicfifBKbpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifBKbpsUniSuppression.setStatus("current")
_HpnicfifOutPayloadOctets_Type = Counter64
_HpnicfifOutPayloadOctets_Object = MibTableColumn
hpnicfifOutPayloadOctets = _HpnicfifOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 35),
    _HpnicfifOutPayloadOctets_Type()
)
hpnicfifOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifOutPayloadOctets.setStatus("current")
_HpnicfifInPayloadOctets_Type = Counter64
_HpnicfifInPayloadOctets_Object = MibTableColumn
hpnicfifInPayloadOctets = _HpnicfifInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 36),
    _HpnicfifInPayloadOctets_Type()
)
hpnicfifInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifInPayloadOctets.setStatus("current")
_HpnicfifInErrorPktsRate_Type = Integer32
_HpnicfifInErrorPktsRate_Object = MibTableColumn
hpnicfifInErrorPktsRate = _HpnicfifInErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 37),
    _HpnicfifInErrorPktsRate_Type()
)
hpnicfifInErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifInErrorPktsRate.setStatus("current")
_HpnicfifInPkts_Type = Counter64
_HpnicfifInPkts_Object = MibTableColumn
hpnicfifInPkts = _HpnicfifInPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 38),
    _HpnicfifInPkts_Type()
)
hpnicfifInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifInPkts.setStatus("current")
_HpnicfifInNormalPkts_Type = Counter64
_HpnicfifInNormalPkts_Object = MibTableColumn
hpnicfifInNormalPkts = _HpnicfifInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 39),
    _HpnicfifInNormalPkts_Type()
)
hpnicfifInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifInNormalPkts.setStatus("current")
_HpnicfifOutPkts_Type = Counter64
_HpnicfifOutPkts_Object = MibTableColumn
hpnicfifOutPkts = _HpnicfifOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 1, 1, 40),
    _HpnicfifOutPkts_Type()
)
hpnicfifOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifOutPkts.setStatus("current")
_HpnicfifAggregateTable_Object = MibTable
hpnicfifAggregateTable = _HpnicfifAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfifAggregateTable.setStatus("current")
_HpnicfifAggregateEntry_Object = MibTableRow
hpnicfifAggregateEntry = _HpnicfifAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 2, 1)
)
hpnicfifAggregateEntry.setIndexNames(
    (0, "HPN-ICF-LswINF-MIB", "hpnicfifAggregatePortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfifAggregateEntry.setStatus("current")
_HpnicfifAggregatePortIndex_Type = InterfaceIndex
_HpnicfifAggregatePortIndex_Object = MibTableColumn
hpnicfifAggregatePortIndex = _HpnicfifAggregatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 2, 1, 1),
    _HpnicfifAggregatePortIndex_Type()
)
hpnicfifAggregatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifAggregatePortIndex.setStatus("current")


class _HpnicfifAggregatePortName_Type(OctetString):
    """Custom type hpnicfifAggregatePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_HpnicfifAggregatePortName_Type.__name__ = "OctetString"
_HpnicfifAggregatePortName_Object = MibTableColumn
hpnicfifAggregatePortName = _HpnicfifAggregatePortName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 2, 1, 2),
    _HpnicfifAggregatePortName_Type()
)
hpnicfifAggregatePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifAggregatePortName.setStatus("current")
_HpnicfifAggregatePortListPorts_Type = PortList
_HpnicfifAggregatePortListPorts_Object = MibTableColumn
hpnicfifAggregatePortListPorts = _HpnicfifAggregatePortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 2, 1, 3),
    _HpnicfifAggregatePortListPorts_Type()
)
hpnicfifAggregatePortListPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifAggregatePortListPorts.setStatus("current")


class _HpnicfifAggregateModel_Type(Integer32):
    """Custom type hpnicfifAggregateModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 2),
          ("ingress", 1),
          ("round-robin", 3))
    )


_HpnicfifAggregateModel_Type.__name__ = "Integer32"
_HpnicfifAggregateModel_Object = MibTableColumn
hpnicfifAggregateModel = _HpnicfifAggregateModel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 2, 1, 4),
    _HpnicfifAggregateModel_Type()
)
hpnicfifAggregateModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifAggregateModel.setStatus("current")
_HpnicfifAggregateOperStatus_Type = RowStatus
_HpnicfifAggregateOperStatus_Object = MibTableColumn
hpnicfifAggregateOperStatus = _HpnicfifAggregateOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 2, 1, 5),
    _HpnicfifAggregateOperStatus_Type()
)
hpnicfifAggregateOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfifAggregateOperStatus.setStatus("current")
_HpnicfifHybridPortTable_Object = MibTable
hpnicfifHybridPortTable = _HpnicfifHybridPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfifHybridPortTable.setStatus("current")
_HpnicfifHybridPortEntry_Object = MibTableRow
hpnicfifHybridPortEntry = _HpnicfifHybridPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 3, 1)
)
hpnicfifHybridPortEntry.setIndexNames(
    (0, "HPN-ICF-LswINF-MIB", "hpnicfifHybridPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfifHybridPortEntry.setStatus("current")
_HpnicfifHybridPortIndex_Type = Integer32
_HpnicfifHybridPortIndex_Object = MibTableColumn
hpnicfifHybridPortIndex = _HpnicfifHybridPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 3, 1, 1),
    _HpnicfifHybridPortIndex_Type()
)
hpnicfifHybridPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifHybridPortIndex.setStatus("current")


class _HpnicfifHybridTaggedVlanListLow_Type(OctetString):
    """Custom type hpnicfifHybridTaggedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifHybridTaggedVlanListLow_Type.__name__ = "OctetString"
_HpnicfifHybridTaggedVlanListLow_Object = MibTableColumn
hpnicfifHybridTaggedVlanListLow = _HpnicfifHybridTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 3, 1, 2),
    _HpnicfifHybridTaggedVlanListLow_Type()
)
hpnicfifHybridTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifHybridTaggedVlanListLow.setStatus("current")


class _HpnicfifHybridTaggedVlanListHigh_Type(OctetString):
    """Custom type hpnicfifHybridTaggedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifHybridTaggedVlanListHigh_Type.__name__ = "OctetString"
_HpnicfifHybridTaggedVlanListHigh_Object = MibTableColumn
hpnicfifHybridTaggedVlanListHigh = _HpnicfifHybridTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 3, 1, 3),
    _HpnicfifHybridTaggedVlanListHigh_Type()
)
hpnicfifHybridTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifHybridTaggedVlanListHigh.setStatus("current")


class _HpnicfifHybridUnTaggedVlanListLow_Type(OctetString):
    """Custom type hpnicfifHybridUnTaggedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifHybridUnTaggedVlanListLow_Type.__name__ = "OctetString"
_HpnicfifHybridUnTaggedVlanListLow_Object = MibTableColumn
hpnicfifHybridUnTaggedVlanListLow = _HpnicfifHybridUnTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 3, 1, 4),
    _HpnicfifHybridUnTaggedVlanListLow_Type()
)
hpnicfifHybridUnTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifHybridUnTaggedVlanListLow.setStatus("current")


class _HpnicfifHybridUnTaggedVlanListHigh_Type(OctetString):
    """Custom type hpnicfifHybridUnTaggedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpnicfifHybridUnTaggedVlanListHigh_Type.__name__ = "OctetString"
_HpnicfifHybridUnTaggedVlanListHigh_Object = MibTableColumn
hpnicfifHybridUnTaggedVlanListHigh = _HpnicfifHybridUnTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 3, 1, 5),
    _HpnicfifHybridUnTaggedVlanListHigh_Type()
)
hpnicfifHybridUnTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifHybridUnTaggedVlanListHigh.setStatus("current")
_HpnicfifComboPortTable_Object = MibTable
hpnicfifComboPortTable = _HpnicfifComboPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfifComboPortTable.setStatus("current")
_HpnicfifComboPortEntry_Object = MibTableRow
hpnicfifComboPortEntry = _HpnicfifComboPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 4, 1)
)
hpnicfifComboPortEntry.setIndexNames(
    (0, "HPN-ICF-LswINF-MIB", "hpnicfifComboPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfifComboPortEntry.setStatus("current")
_HpnicfifComboPortIndex_Type = InterfaceIndex
_HpnicfifComboPortIndex_Object = MibTableColumn
hpnicfifComboPortIndex = _HpnicfifComboPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 4, 1, 1),
    _HpnicfifComboPortIndex_Type()
)
hpnicfifComboPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifComboPortIndex.setStatus("current")


class _HpnicfifComboPortCurActive_Type(Integer32):
    """Custom type hpnicfifComboPortCurActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copper", 2),
          ("fiber", 1),
          ("na", 3))
    )


_HpnicfifComboPortCurActive_Type.__name__ = "Integer32"
_HpnicfifComboPortCurActive_Object = MibTableColumn
hpnicfifComboPortCurActive = _HpnicfifComboPortCurActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 4, 1, 2),
    _HpnicfifComboPortCurActive_Type()
)
hpnicfifComboPortCurActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifComboPortCurActive.setStatus("current")
_HpnicfifPktBufTable_Object = MibTable
hpnicfifPktBufTable = _HpnicfifPktBufTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 5)
)
if mibBuilder.loadTexts:
    hpnicfifPktBufTable.setStatus("current")
_HpnicfifPktBufEntry_Object = MibTableRow
hpnicfifPktBufEntry = _HpnicfifPktBufEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 5, 1)
)
hpnicfifPktBufEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfifPktBufEntry.setStatus("current")
_HpnicfifPktBufFree_Type = Integer32
_HpnicfifPktBufFree_Object = MibTableColumn
hpnicfifPktBufFree = _HpnicfifPktBufFree_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 5, 1, 1),
    _HpnicfifPktBufFree_Type()
)
hpnicfifPktBufFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifPktBufFree.setStatus("current")
_HpnicfifPktBufInit_Type = Integer32
_HpnicfifPktBufInit_Object = MibTableColumn
hpnicfifPktBufInit = _HpnicfifPktBufInit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 5, 1, 2),
    _HpnicfifPktBufInit_Type()
)
hpnicfifPktBufInit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifPktBufInit.setStatus("current")
_HpnicfifPktBufMin_Type = Integer32
_HpnicfifPktBufMin_Object = MibTableColumn
hpnicfifPktBufMin = _HpnicfifPktBufMin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 5, 1, 3),
    _HpnicfifPktBufMin_Type()
)
hpnicfifPktBufMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifPktBufMin.setStatus("current")
_HpnicfifPktBufMiss_Type = Counter64
_HpnicfifPktBufMiss_Object = MibTableColumn
hpnicfifPktBufMiss = _HpnicfifPktBufMiss_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 1, 5, 1, 4),
    _HpnicfifPktBufMiss_Type()
)
hpnicfifPktBufMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifPktBufMiss.setStatus("current")
_HpnicfLswL2InfMibObject_ObjectIdentity = ObjectIdentity
hpnicfLswL2InfMibObject = _HpnicfLswL2InfMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1)
)
_HpnicfSlotPortMax_Type = Integer32
_HpnicfSlotPortMax_Object = MibScalar
hpnicfSlotPortMax = _HpnicfSlotPortMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 1),
    _HpnicfSlotPortMax_Type()
)
hpnicfSlotPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSlotPortMax.setStatus("current")
_HpnicfSwitchPortMax_Type = Integer32
_HpnicfSwitchPortMax_Object = MibScalar
hpnicfSwitchPortMax = _HpnicfSwitchPortMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 2),
    _HpnicfSwitchPortMax_Type()
)
hpnicfSwitchPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSwitchPortMax.setStatus("current")
_HpnicfifVLANTrunkStatusTable_Object = MibTable
hpnicfifVLANTrunkStatusTable = _HpnicfifVLANTrunkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkStatusTable.setStatus("current")
_HpnicfifVLANTrunkStatusEntry_Object = MibTableRow
hpnicfifVLANTrunkStatusEntry = _HpnicfifVLANTrunkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3, 1)
)
hpnicfifVLANTrunkStatusEntry.setIndexNames(
    (0, "HPN-ICF-LswINF-MIB", "hpnicfifVLANTrunkIndex"),
)
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkStatusEntry.setStatus("current")
_HpnicfifVLANTrunkIndex_Type = InterfaceIndex
_HpnicfifVLANTrunkIndex_Object = MibTableColumn
hpnicfifVLANTrunkIndex = _HpnicfifVLANTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3, 1, 1),
    _HpnicfifVLANTrunkIndex_Type()
)
hpnicfifVLANTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkIndex.setStatus("current")


class _HpnicfifVLANTrunkGvrpRegistration_Type(Integer32):
    """Custom type hpnicfifVLANTrunkGvrpRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 2),
          ("forbidden", 3),
          ("normal", 1))
    )


_HpnicfifVLANTrunkGvrpRegistration_Type.__name__ = "Integer32"
_HpnicfifVLANTrunkGvrpRegistration_Object = MibTableColumn
hpnicfifVLANTrunkGvrpRegistration = _HpnicfifVLANTrunkGvrpRegistration_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3, 1, 2),
    _HpnicfifVLANTrunkGvrpRegistration_Type()
)
hpnicfifVLANTrunkGvrpRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkGvrpRegistration.setStatus("current")
_HpnicfifVLANTrunkPassListLow_Type = OctetString
_HpnicfifVLANTrunkPassListLow_Object = MibTableColumn
hpnicfifVLANTrunkPassListLow = _HpnicfifVLANTrunkPassListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3, 1, 4),
    _HpnicfifVLANTrunkPassListLow_Type()
)
hpnicfifVLANTrunkPassListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkPassListLow.setStatus("current")
_HpnicfifVLANTrunkPassListHigh_Type = OctetString
_HpnicfifVLANTrunkPassListHigh_Object = MibTableColumn
hpnicfifVLANTrunkPassListHigh = _HpnicfifVLANTrunkPassListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3, 1, 5),
    _HpnicfifVLANTrunkPassListHigh_Type()
)
hpnicfifVLANTrunkPassListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkPassListHigh.setStatus("current")
_HpnicfifVLANTrunkAllowListLow_Type = OctetString
_HpnicfifVLANTrunkAllowListLow_Object = MibTableColumn
hpnicfifVLANTrunkAllowListLow = _HpnicfifVLANTrunkAllowListLow_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3, 1, 6),
    _HpnicfifVLANTrunkAllowListLow_Type()
)
hpnicfifVLANTrunkAllowListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkAllowListLow.setStatus("current")
_HpnicfifVLANTrunkAllowListHigh_Type = OctetString
_HpnicfifVLANTrunkAllowListHigh_Object = MibTableColumn
hpnicfifVLANTrunkAllowListHigh = _HpnicfifVLANTrunkAllowListHigh_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 3, 1, 7),
    _HpnicfifVLANTrunkAllowListHigh_Type()
)
hpnicfifVLANTrunkAllowListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifVLANTrunkAllowListHigh.setStatus("current")
_HpnicfethernetTable_Object = MibTable
hpnicfethernetTable = _HpnicfethernetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfethernetTable.setStatus("current")
_HpnicfethernetEntry_Object = MibTableRow
hpnicfethernetEntry = _HpnicfethernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1)
)
hpnicfethernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfethernetEntry.setStatus("current")


class _HpnicfifEthernetDuplex_Type(Integer32):
    """Custom type hpnicfifEthernetDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 1),
          ("half", 2))
    )


_HpnicfifEthernetDuplex_Type.__name__ = "Integer32"
_HpnicfifEthernetDuplex_Object = MibTableColumn
hpnicfifEthernetDuplex = _HpnicfifEthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 3),
    _HpnicfifEthernetDuplex_Type()
)
hpnicfifEthernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetDuplex.setStatus("current")
_HpnicfifEthernetMTU_Type = Integer32
_HpnicfifEthernetMTU_Object = MibTableColumn
hpnicfifEthernetMTU = _HpnicfifEthernetMTU_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 4),
    _HpnicfifEthernetMTU_Type()
)
hpnicfifEthernetMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetMTU.setStatus("current")


class _HpnicfifEthernetSpeed_Type(Integer32):
    """Custom type hpnicfifEthernetSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              100,
              1000,
              10000,
              24000,
              40000,
              100000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("s100000M", 100000),
          ("s10000M", 10000),
          ("s1000M", 1000),
          ("s100M", 100),
          ("s10M", 10),
          ("s24000M", 24000),
          ("s40000M", 40000))
    )


_HpnicfifEthernetSpeed_Type.__name__ = "Integer32"
_HpnicfifEthernetSpeed_Object = MibTableColumn
hpnicfifEthernetSpeed = _HpnicfifEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 5),
    _HpnicfifEthernetSpeed_Type()
)
hpnicfifEthernetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetSpeed.setStatus("current")


class _HpnicfifEthernetMdi_Type(Integer32):
    """Custom type hpnicfifEthernetMdi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi-auto", 3),
          ("mdi-ii", 1),
          ("mdi-x", 2))
    )


_HpnicfifEthernetMdi_Type.__name__ = "Integer32"
_HpnicfifEthernetMdi_Object = MibTableColumn
hpnicfifEthernetMdi = _HpnicfifEthernetMdi_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 7),
    _HpnicfifEthernetMdi_Type()
)
hpnicfifEthernetMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetMdi.setStatus("current")


class _HpnicfMaxMacLearn_Type(Integer32):
    """Custom type hpnicfMaxMacLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_HpnicfMaxMacLearn_Type.__name__ = "Integer32"
_HpnicfMaxMacLearn_Object = MibTableColumn
hpnicfMaxMacLearn = _HpnicfMaxMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 8),
    _HpnicfMaxMacLearn_Type()
)
hpnicfMaxMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfMaxMacLearn.setStatus("current")


class _HpnicfifMacAddressLearn_Type(Integer32):
    """Custom type hpnicfifMacAddressLearn based on Integer32"""
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


_HpnicfifMacAddressLearn_Type.__name__ = "Integer32"
_HpnicfifMacAddressLearn_Object = MibTableColumn
hpnicfifMacAddressLearn = _HpnicfifMacAddressLearn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 9),
    _HpnicfifMacAddressLearn_Type()
)
hpnicfifMacAddressLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifMacAddressLearn.setStatus("current")


class _HpnicfifEthernetTest_Type(Integer32):
    """Custom type hpnicfifEthernetTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("test", 1)
    )


_HpnicfifEthernetTest_Type.__name__ = "Integer32"
_HpnicfifEthernetTest_Object = MibTableColumn
hpnicfifEthernetTest = _HpnicfifEthernetTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 10),
    _HpnicfifEthernetTest_Type()
)
hpnicfifEthernetTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetTest.setStatus("current")


class _HpnicfifMacAddrLearnMode_Type(Integer32):
    """Custom type hpnicfifMacAddrLearnMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("iVL", 1),
          ("sVL", 2))
    )


_HpnicfifMacAddrLearnMode_Type.__name__ = "Integer32"
_HpnicfifMacAddrLearnMode_Object = MibTableColumn
hpnicfifMacAddrLearnMode = _HpnicfifMacAddrLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 11),
    _HpnicfifMacAddrLearnMode_Type()
)
hpnicfifMacAddrLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifMacAddrLearnMode.setStatus("current")


class _HpnicfifEthernetFlowInterval_Type(Integer32):
    """Custom type hpnicfifEthernetFlowInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_HpnicfifEthernetFlowInterval_Type.__name__ = "Integer32"
_HpnicfifEthernetFlowInterval_Object = MibTableColumn
hpnicfifEthernetFlowInterval = _HpnicfifEthernetFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 12),
    _HpnicfifEthernetFlowInterval_Type()
)
hpnicfifEthernetFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetFlowInterval.setStatus("current")
_HpnicfifEthernetIsolate_Type = OctetString
_HpnicfifEthernetIsolate_Object = MibTableColumn
hpnicfifEthernetIsolate = _HpnicfifEthernetIsolate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 13),
    _HpnicfifEthernetIsolate_Type()
)
hpnicfifEthernetIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetIsolate.setStatus("current")


class _HpnicfifVlanVPNStatus_Type(Integer32):
    """Custom type hpnicfifVlanVPNStatus based on Integer32"""
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


_HpnicfifVlanVPNStatus_Type.__name__ = "Integer32"
_HpnicfifVlanVPNStatus_Object = MibTableColumn
hpnicfifVlanVPNStatus = _HpnicfifVlanVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 14),
    _HpnicfifVlanVPNStatus_Type()
)
hpnicfifVlanVPNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifVlanVPNStatus.setStatus("current")


class _HpnicfifVlanVPNUplinkStatus_Type(Integer32):
    """Custom type hpnicfifVlanVPNUplinkStatus based on Integer32"""
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


_HpnicfifVlanVPNUplinkStatus_Type.__name__ = "Integer32"
_HpnicfifVlanVPNUplinkStatus_Object = MibTableColumn
hpnicfifVlanVPNUplinkStatus = _HpnicfifVlanVPNUplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 15),
    _HpnicfifVlanVPNUplinkStatus_Type()
)
hpnicfifVlanVPNUplinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifVlanVPNUplinkStatus.setStatus("current")


class _HpnicfifVlanVPNTPID_Type(Integer32):
    """Custom type hpnicfifVlanVPNTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfifVlanVPNTPID_Type.__name__ = "Integer32"
_HpnicfifVlanVPNTPID_Object = MibTableColumn
hpnicfifVlanVPNTPID = _HpnicfifVlanVPNTPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 16),
    _HpnicfifVlanVPNTPID_Type()
)
hpnicfifVlanVPNTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifVlanVPNTPID.setStatus("current")
_HpnicfifIsolateGroupID_Type = Integer32
_HpnicfifIsolateGroupID_Object = MibTableColumn
hpnicfifIsolateGroupID = _HpnicfifIsolateGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 17),
    _HpnicfifIsolateGroupID_Type()
)
hpnicfifIsolateGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifIsolateGroupID.setStatus("current")


class _HpnicfifisUplinkPort_Type(Integer32):
    """Custom type hpnicfifisUplinkPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_HpnicfifisUplinkPort_Type.__name__ = "Integer32"
_HpnicfifisUplinkPort_Object = MibTableColumn
hpnicfifisUplinkPort = _HpnicfifisUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 18),
    _HpnicfifisUplinkPort_Type()
)
hpnicfifisUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifisUplinkPort.setStatus("current")
_HpnicfifEthernetAutoSpeedMask_Type = SpeedModeFlag
_HpnicfifEthernetAutoSpeedMask_Object = MibTableColumn
hpnicfifEthernetAutoSpeedMask = _HpnicfifEthernetAutoSpeedMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 19),
    _HpnicfifEthernetAutoSpeedMask_Type()
)
hpnicfifEthernetAutoSpeedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifEthernetAutoSpeedMask.setStatus("current")
_HpnicfifEthernetAutoSpeed_Type = SpeedModeFlag
_HpnicfifEthernetAutoSpeed_Object = MibTableColumn
hpnicfifEthernetAutoSpeed = _HpnicfifEthernetAutoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 4, 1, 20),
    _HpnicfifEthernetAutoSpeed_Type()
)
hpnicfifEthernetAutoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfifEthernetAutoSpeed.setStatus("current")
_HpnicfIsolateGroupMax_Type = Integer32
_HpnicfIsolateGroupMax_Object = MibScalar
hpnicfIsolateGroupMax = _HpnicfIsolateGroupMax_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 5),
    _HpnicfIsolateGroupMax_Type()
)
hpnicfIsolateGroupMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIsolateGroupMax.setStatus("current")


class _HpnicfGlobalBroadcastMaxPps_Type(Integer32):
    """Custom type hpnicfGlobalBroadcastMaxPps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_HpnicfGlobalBroadcastMaxPps_Type.__name__ = "Integer32"
_HpnicfGlobalBroadcastMaxPps_Object = MibScalar
hpnicfGlobalBroadcastMaxPps = _HpnicfGlobalBroadcastMaxPps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 6),
    _HpnicfGlobalBroadcastMaxPps_Type()
)
hpnicfGlobalBroadcastMaxPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfGlobalBroadcastMaxPps.setStatus("current")


class _HpnicfGlobalBroadcastMaxRatio_Type(Integer32):
    """Custom type hpnicfGlobalBroadcastMaxRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HpnicfGlobalBroadcastMaxRatio_Type.__name__ = "Integer32"
_HpnicfGlobalBroadcastMaxRatio_Object = MibScalar
hpnicfGlobalBroadcastMaxRatio = _HpnicfGlobalBroadcastMaxRatio_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 7),
    _HpnicfGlobalBroadcastMaxRatio_Type()
)
hpnicfGlobalBroadcastMaxRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfGlobalBroadcastMaxRatio.setStatus("current")


class _HpnicfBpduTunnelStatus_Type(Integer32):
    """Custom type hpnicfBpduTunnelStatus based on Integer32"""
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


_HpnicfBpduTunnelStatus_Type.__name__ = "Integer32"
_HpnicfBpduTunnelStatus_Object = MibScalar
hpnicfBpduTunnelStatus = _HpnicfBpduTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 8),
    _HpnicfBpduTunnelStatus_Type()
)
hpnicfBpduTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfBpduTunnelStatus.setStatus("current")


class _HpnicfVlanVPNTPIDMode_Type(Integer32):
    """Custom type hpnicfVlanVPNTPIDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("global", 2),
          ("port-based", 1))
    )


_HpnicfVlanVPNTPIDMode_Type.__name__ = "Integer32"
_HpnicfVlanVPNTPIDMode_Object = MibScalar
hpnicfVlanVPNTPIDMode = _HpnicfVlanVPNTPIDMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 9),
    _HpnicfVlanVPNTPIDMode_Type()
)
hpnicfVlanVPNTPIDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfVlanVPNTPIDMode.setStatus("current")


class _HpnicfVlanVPNTPID_Type(Integer32):
    """Custom type hpnicfVlanVPNTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfVlanVPNTPID_Type.__name__ = "Integer32"
_HpnicfVlanVPNTPID_Object = MibScalar
hpnicfVlanVPNTPID = _HpnicfVlanVPNTPID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 10),
    _HpnicfVlanVPNTPID_Type()
)
hpnicfVlanVPNTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVlanVPNTPID.setStatus("current")
_HpnicfPortIsolateGroupTable_Object = MibTable
hpnicfPortIsolateGroupTable = _HpnicfPortIsolateGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hpnicfPortIsolateGroupTable.setStatus("current")
_HpnicfPortIsolateGroupEntry_Object = MibTableRow
hpnicfPortIsolateGroupEntry = _HpnicfPortIsolateGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 11, 1)
)
hpnicfPortIsolateGroupEntry.setIndexNames(
    (0, "HPN-ICF-LswINF-MIB", "hpnicfPortIsolateGroupIndex"),
)
if mibBuilder.loadTexts:
    hpnicfPortIsolateGroupEntry.setStatus("current")
_HpnicfPortIsolateGroupIndex_Type = Integer32
_HpnicfPortIsolateGroupIndex_Object = MibTableColumn
hpnicfPortIsolateGroupIndex = _HpnicfPortIsolateGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 11, 1, 1),
    _HpnicfPortIsolateGroupIndex_Type()
)
hpnicfPortIsolateGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfPortIsolateGroupIndex.setStatus("current")
_HpnicfPortIsolateUplinkIfIndex_Type = InterfaceIndex
_HpnicfPortIsolateUplinkIfIndex_Object = MibTableColumn
hpnicfPortIsolateUplinkIfIndex = _HpnicfPortIsolateUplinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 11, 1, 2),
    _HpnicfPortIsolateUplinkIfIndex_Type()
)
hpnicfPortIsolateUplinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortIsolateUplinkIfIndex.setStatus("current")
_HpnicfPortIsolateGroupRowStatus_Type = RowStatus
_HpnicfPortIsolateGroupRowStatus_Object = MibTableColumn
hpnicfPortIsolateGroupRowStatus = _HpnicfPortIsolateGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 11, 1, 3),
    _HpnicfPortIsolateGroupRowStatus_Type()
)
hpnicfPortIsolateGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortIsolateGroupRowStatus.setStatus("current")


class _HpnicfPortIsolateGroupDescription_Type(DisplayString):
    """Custom type hpnicfPortIsolateGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpnicfPortIsolateGroupDescription_Type.__name__ = "DisplayString"
_HpnicfPortIsolateGroupDescription_Object = MibTableColumn
hpnicfPortIsolateGroupDescription = _HpnicfPortIsolateGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 11, 1, 4),
    _HpnicfPortIsolateGroupDescription_Type()
)
hpnicfPortIsolateGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfPortIsolateGroupDescription.setStatus("current")
_HpnicfMaxMacLearnRange_Type = Integer32
_HpnicfMaxMacLearnRange_Object = MibScalar
hpnicfMaxMacLearnRange = _HpnicfMaxMacLearnRange_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 12),
    _HpnicfMaxMacLearnRange_Type()
)
hpnicfMaxMacLearnRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfMaxMacLearnRange.setStatus("current")
_HpnicfifPortProtocolStatTable_Object = MibTable
hpnicfifPortProtocolStatTable = _HpnicfifPortProtocolStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13)
)
if mibBuilder.loadTexts:
    hpnicfifPortProtocolStatTable.setStatus("current")
_HpnicfifPortProtocolStatEntry_Object = MibTableRow
hpnicfifPortProtocolStatEntry = _HpnicfifPortProtocolStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1)
)
hpnicfifPortProtocolStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfifPortProtocolStatEntry.setStatus("current")
_HpnicfifIPv4InOctets_Type = Counter64
_HpnicfifIPv4InOctets_Object = MibTableColumn
hpnicfifIPv4InOctets = _HpnicfifIPv4InOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 1),
    _HpnicfifIPv4InOctets_Type()
)
hpnicfifIPv4InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4InOctets.setStatus("current")
_HpnicfifIPv4InUcastPkts_Type = Counter64
_HpnicfifIPv4InUcastPkts_Object = MibTableColumn
hpnicfifIPv4InUcastPkts = _HpnicfifIPv4InUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 2),
    _HpnicfifIPv4InUcastPkts_Type()
)
hpnicfifIPv4InUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4InUcastPkts.setStatus("current")
_HpnicfifIPv4InMultiPkts_Type = Counter64
_HpnicfifIPv4InMultiPkts_Object = MibTableColumn
hpnicfifIPv4InMultiPkts = _HpnicfifIPv4InMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 3),
    _HpnicfifIPv4InMultiPkts_Type()
)
hpnicfifIPv4InMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4InMultiPkts.setStatus("current")
_HpnicfifIPv4InBroadcastPkts_Type = Counter64
_HpnicfifIPv4InBroadcastPkts_Object = MibTableColumn
hpnicfifIPv4InBroadcastPkts = _HpnicfifIPv4InBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 4),
    _HpnicfifIPv4InBroadcastPkts_Type()
)
hpnicfifIPv4InBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4InBroadcastPkts.setStatus("current")
_HpnicfifIPv4InDiscards_Type = Counter64
_HpnicfifIPv4InDiscards_Object = MibTableColumn
hpnicfifIPv4InDiscards = _HpnicfifIPv4InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 5),
    _HpnicfifIPv4InDiscards_Type()
)
hpnicfifIPv4InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4InDiscards.setStatus("current")
_HpnicfifIPv4InErrors_Type = Counter64
_HpnicfifIPv4InErrors_Object = MibTableColumn
hpnicfifIPv4InErrors = _HpnicfifIPv4InErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 6),
    _HpnicfifIPv4InErrors_Type()
)
hpnicfifIPv4InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4InErrors.setStatus("current")
_HpnicfifIPv4OutOctets_Type = Counter64
_HpnicfifIPv4OutOctets_Object = MibTableColumn
hpnicfifIPv4OutOctets = _HpnicfifIPv4OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 7),
    _HpnicfifIPv4OutOctets_Type()
)
hpnicfifIPv4OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4OutOctets.setStatus("current")
_HpnicfifIPv4OutUcastPkts_Type = Counter64
_HpnicfifIPv4OutUcastPkts_Object = MibTableColumn
hpnicfifIPv4OutUcastPkts = _HpnicfifIPv4OutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 8),
    _HpnicfifIPv4OutUcastPkts_Type()
)
hpnicfifIPv4OutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4OutUcastPkts.setStatus("current")
_HpnicfifIPv4OutMultiPkts_Type = Counter64
_HpnicfifIPv4OutMultiPkts_Object = MibTableColumn
hpnicfifIPv4OutMultiPkts = _HpnicfifIPv4OutMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 9),
    _HpnicfifIPv4OutMultiPkts_Type()
)
hpnicfifIPv4OutMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4OutMultiPkts.setStatus("current")
_HpnicfifIPv4OutBroadcastPkts_Type = Counter64
_HpnicfifIPv4OutBroadcastPkts_Object = MibTableColumn
hpnicfifIPv4OutBroadcastPkts = _HpnicfifIPv4OutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 10),
    _HpnicfifIPv4OutBroadcastPkts_Type()
)
hpnicfifIPv4OutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4OutBroadcastPkts.setStatus("current")
_HpnicfifIPv4OutDiscards_Type = Counter64
_HpnicfifIPv4OutDiscards_Object = MibTableColumn
hpnicfifIPv4OutDiscards = _HpnicfifIPv4OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 11),
    _HpnicfifIPv4OutDiscards_Type()
)
hpnicfifIPv4OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4OutDiscards.setStatus("current")
_HpnicfifIPv4OutErrors_Type = Counter64
_HpnicfifIPv4OutErrors_Object = MibTableColumn
hpnicfifIPv4OutErrors = _HpnicfifIPv4OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 12),
    _HpnicfifIPv4OutErrors_Type()
)
hpnicfifIPv4OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv4OutErrors.setStatus("current")
_HpnicfifIPv6InOctets_Type = Counter64
_HpnicfifIPv6InOctets_Object = MibTableColumn
hpnicfifIPv6InOctets = _HpnicfifIPv6InOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 13),
    _HpnicfifIPv6InOctets_Type()
)
hpnicfifIPv6InOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6InOctets.setStatus("current")
_HpnicfifIPv6InUcastPkts_Type = Counter64
_HpnicfifIPv6InUcastPkts_Object = MibTableColumn
hpnicfifIPv6InUcastPkts = _HpnicfifIPv6InUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 14),
    _HpnicfifIPv6InUcastPkts_Type()
)
hpnicfifIPv6InUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6InUcastPkts.setStatus("current")
_HpnicfifIPv6InMultiPkts_Type = Counter64
_HpnicfifIPv6InMultiPkts_Object = MibTableColumn
hpnicfifIPv6InMultiPkts = _HpnicfifIPv6InMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 15),
    _HpnicfifIPv6InMultiPkts_Type()
)
hpnicfifIPv6InMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6InMultiPkts.setStatus("current")
_HpnicfifIPv6InAnycastPkts_Type = Counter64
_HpnicfifIPv6InAnycastPkts_Object = MibTableColumn
hpnicfifIPv6InAnycastPkts = _HpnicfifIPv6InAnycastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 16),
    _HpnicfifIPv6InAnycastPkts_Type()
)
hpnicfifIPv6InAnycastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6InAnycastPkts.setStatus("current")
_HpnicfifIPv6InDiscards_Type = Counter64
_HpnicfifIPv6InDiscards_Object = MibTableColumn
hpnicfifIPv6InDiscards = _HpnicfifIPv6InDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 17),
    _HpnicfifIPv6InDiscards_Type()
)
hpnicfifIPv6InDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6InDiscards.setStatus("current")
_HpnicfifIPv6InErrors_Type = Counter64
_HpnicfifIPv6InErrors_Object = MibTableColumn
hpnicfifIPv6InErrors = _HpnicfifIPv6InErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 18),
    _HpnicfifIPv6InErrors_Type()
)
hpnicfifIPv6InErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6InErrors.setStatus("current")
_HpnicfifIPv6OutOctets_Type = Counter64
_HpnicfifIPv6OutOctets_Object = MibTableColumn
hpnicfifIPv6OutOctets = _HpnicfifIPv6OutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 19),
    _HpnicfifIPv6OutOctets_Type()
)
hpnicfifIPv6OutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6OutOctets.setStatus("current")
_HpnicfifIPv6OutUcastPkts_Type = Counter64
_HpnicfifIPv6OutUcastPkts_Object = MibTableColumn
hpnicfifIPv6OutUcastPkts = _HpnicfifIPv6OutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 20),
    _HpnicfifIPv6OutUcastPkts_Type()
)
hpnicfifIPv6OutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6OutUcastPkts.setStatus("current")
_HpnicfifIPv6OutMultiPkts_Type = Counter64
_HpnicfifIPv6OutMultiPkts_Object = MibTableColumn
hpnicfifIPv6OutMultiPkts = _HpnicfifIPv6OutMultiPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 21),
    _HpnicfifIPv6OutMultiPkts_Type()
)
hpnicfifIPv6OutMultiPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6OutMultiPkts.setStatus("current")
_HpnicfifIPv6OutAnycastPkts_Type = Counter64
_HpnicfifIPv6OutAnycastPkts_Object = MibTableColumn
hpnicfifIPv6OutAnycastPkts = _HpnicfifIPv6OutAnycastPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 22),
    _HpnicfifIPv6OutAnycastPkts_Type()
)
hpnicfifIPv6OutAnycastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6OutAnycastPkts.setStatus("current")
_HpnicfifIPv6OutDiscards_Type = Counter64
_HpnicfifIPv6OutDiscards_Object = MibTableColumn
hpnicfifIPv6OutDiscards = _HpnicfifIPv6OutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 23),
    _HpnicfifIPv6OutDiscards_Type()
)
hpnicfifIPv6OutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6OutDiscards.setStatus("current")
_HpnicfifIPv6OutErrors_Type = Counter64
_HpnicfifIPv6OutErrors_Object = MibTableColumn
hpnicfifIPv6OutErrors = _HpnicfifIPv6OutErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 35, 5, 1, 13, 1, 24),
    _HpnicfifIPv6OutErrors_Type()
)
hpnicfifIPv6OutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfifIPv6OutErrors.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-LswINF-MIB",
    **{"PortList": PortList,
       "VlanIndex": VlanIndex,
       "DropDirection": DropDirection,
       "SpeedModeFlag": SpeedModeFlag,
       "hpnicfLswExtInterface": hpnicfLswExtInterface,
       "hpnicfifXXTable": hpnicfifXXTable,
       "hpnicfifXXEntry": hpnicfifXXEntry,
       "hpnicfifUnBoundPort": hpnicfifUnBoundPort,
       "hpnicfifISPhyPort": hpnicfifISPhyPort,
       "hpnicfifAggregatePort": hpnicfifAggregatePort,
       "hpnicfifMirrorPort": hpnicfifMirrorPort,
       "hpnicfifVLANType": hpnicfifVLANType,
       "hpnicfifMcastControl": hpnicfifMcastControl,
       "hpnicfifFlowControl": hpnicfifFlowControl,
       "hpnicfifSrcMacControl": hpnicfifSrcMacControl,
       "hpnicfifClearStat": hpnicfifClearStat,
       "hpnicfifXXBasePortIndex": hpnicfifXXBasePortIndex,
       "hpnicfifXXDevPortIndex": hpnicfifXXDevPortIndex,
       "hpnicfifPpsMcastControl": hpnicfifPpsMcastControl,
       "hpnicfifPpsBcastDisValControl": hpnicfifPpsBcastDisValControl,
       "hpnicfifUniSuppressionStep": hpnicfifUniSuppressionStep,
       "hpnicfifPpsUniSuppressionMax": hpnicfifPpsUniSuppressionMax,
       "hpnicfifMulSuppressionStep": hpnicfifMulSuppressionStep,
       "hpnicfifPpsMulSuppressionMax": hpnicfifPpsMulSuppressionMax,
       "hpnicfifUniSuppression": hpnicfifUniSuppression,
       "hpnicfifPpsUniSuppression": hpnicfifPpsUniSuppression,
       "hpnicfifMulSuppression": hpnicfifMulSuppression,
       "hpnicfifPpsMulSuppression": hpnicfifPpsMulSuppression,
       "hpnicfifComboActivePort": hpnicfifComboActivePort,
       "hpnicfifBMbpsMulSuppressionMax": hpnicfifBMbpsMulSuppressionMax,
       "hpnicfifBMbpsMulSuppression": hpnicfifBMbpsMulSuppression,
       "hpnicfifBKbpsMulSuppressionMax": hpnicfifBKbpsMulSuppressionMax,
       "hpnicfifBKbpsMulSuppressionStep": hpnicfifBKbpsMulSuppressionStep,
       "hpnicfifBKbpsMulSuppression": hpnicfifBKbpsMulSuppression,
       "hpnicfifUnknownPacketDropMul": hpnicfifUnknownPacketDropMul,
       "hpnicfifUnknownPacketDropUni": hpnicfifUnknownPacketDropUni,
       "hpnicfifBMbpsUniSuppressionMax": hpnicfifBMbpsUniSuppressionMax,
       "hpnicfifBMbpsUniSuppression": hpnicfifBMbpsUniSuppression,
       "hpnicfifBKbpsUniSuppressionMax": hpnicfifBKbpsUniSuppressionMax,
       "hpnicfifBKbpsUniSuppressionStep": hpnicfifBKbpsUniSuppressionStep,
       "hpnicfifBKbpsUniSuppression": hpnicfifBKbpsUniSuppression,
       "hpnicfifOutPayloadOctets": hpnicfifOutPayloadOctets,
       "hpnicfifInPayloadOctets": hpnicfifInPayloadOctets,
       "hpnicfifInErrorPktsRate": hpnicfifInErrorPktsRate,
       "hpnicfifInPkts": hpnicfifInPkts,
       "hpnicfifInNormalPkts": hpnicfifInNormalPkts,
       "hpnicfifOutPkts": hpnicfifOutPkts,
       "hpnicfifAggregateTable": hpnicfifAggregateTable,
       "hpnicfifAggregateEntry": hpnicfifAggregateEntry,
       "hpnicfifAggregatePortIndex": hpnicfifAggregatePortIndex,
       "hpnicfifAggregatePortName": hpnicfifAggregatePortName,
       "hpnicfifAggregatePortListPorts": hpnicfifAggregatePortListPorts,
       "hpnicfifAggregateModel": hpnicfifAggregateModel,
       "hpnicfifAggregateOperStatus": hpnicfifAggregateOperStatus,
       "hpnicfifHybridPortTable": hpnicfifHybridPortTable,
       "hpnicfifHybridPortEntry": hpnicfifHybridPortEntry,
       "hpnicfifHybridPortIndex": hpnicfifHybridPortIndex,
       "hpnicfifHybridTaggedVlanListLow": hpnicfifHybridTaggedVlanListLow,
       "hpnicfifHybridTaggedVlanListHigh": hpnicfifHybridTaggedVlanListHigh,
       "hpnicfifHybridUnTaggedVlanListLow": hpnicfifHybridUnTaggedVlanListLow,
       "hpnicfifHybridUnTaggedVlanListHigh": hpnicfifHybridUnTaggedVlanListHigh,
       "hpnicfifComboPortTable": hpnicfifComboPortTable,
       "hpnicfifComboPortEntry": hpnicfifComboPortEntry,
       "hpnicfifComboPortIndex": hpnicfifComboPortIndex,
       "hpnicfifComboPortCurActive": hpnicfifComboPortCurActive,
       "hpnicfifPktBufTable": hpnicfifPktBufTable,
       "hpnicfifPktBufEntry": hpnicfifPktBufEntry,
       "hpnicfifPktBufFree": hpnicfifPktBufFree,
       "hpnicfifPktBufInit": hpnicfifPktBufInit,
       "hpnicfifPktBufMin": hpnicfifPktBufMin,
       "hpnicfifPktBufMiss": hpnicfifPktBufMiss,
       "hpnicfLswL2InfMib": hpnicfLswL2InfMib,
       "hpnicfLswL2InfMibObject": hpnicfLswL2InfMibObject,
       "hpnicfSlotPortMax": hpnicfSlotPortMax,
       "hpnicfSwitchPortMax": hpnicfSwitchPortMax,
       "hpnicfifVLANTrunkStatusTable": hpnicfifVLANTrunkStatusTable,
       "hpnicfifVLANTrunkStatusEntry": hpnicfifVLANTrunkStatusEntry,
       "hpnicfifVLANTrunkIndex": hpnicfifVLANTrunkIndex,
       "hpnicfifVLANTrunkGvrpRegistration": hpnicfifVLANTrunkGvrpRegistration,
       "hpnicfifVLANTrunkPassListLow": hpnicfifVLANTrunkPassListLow,
       "hpnicfifVLANTrunkPassListHigh": hpnicfifVLANTrunkPassListHigh,
       "hpnicfifVLANTrunkAllowListLow": hpnicfifVLANTrunkAllowListLow,
       "hpnicfifVLANTrunkAllowListHigh": hpnicfifVLANTrunkAllowListHigh,
       "hpnicfethernetTable": hpnicfethernetTable,
       "hpnicfethernetEntry": hpnicfethernetEntry,
       "hpnicfifEthernetDuplex": hpnicfifEthernetDuplex,
       "hpnicfifEthernetMTU": hpnicfifEthernetMTU,
       "hpnicfifEthernetSpeed": hpnicfifEthernetSpeed,
       "hpnicfifEthernetMdi": hpnicfifEthernetMdi,
       "hpnicfMaxMacLearn": hpnicfMaxMacLearn,
       "hpnicfifMacAddressLearn": hpnicfifMacAddressLearn,
       "hpnicfifEthernetTest": hpnicfifEthernetTest,
       "hpnicfifMacAddrLearnMode": hpnicfifMacAddrLearnMode,
       "hpnicfifEthernetFlowInterval": hpnicfifEthernetFlowInterval,
       "hpnicfifEthernetIsolate": hpnicfifEthernetIsolate,
       "hpnicfifVlanVPNStatus": hpnicfifVlanVPNStatus,
       "hpnicfifVlanVPNUplinkStatus": hpnicfifVlanVPNUplinkStatus,
       "hpnicfifVlanVPNTPID": hpnicfifVlanVPNTPID,
       "hpnicfifIsolateGroupID": hpnicfifIsolateGroupID,
       "hpnicfifisUplinkPort": hpnicfifisUplinkPort,
       "hpnicfifEthernetAutoSpeedMask": hpnicfifEthernetAutoSpeedMask,
       "hpnicfifEthernetAutoSpeed": hpnicfifEthernetAutoSpeed,
       "hpnicfIsolateGroupMax": hpnicfIsolateGroupMax,
       "hpnicfGlobalBroadcastMaxPps": hpnicfGlobalBroadcastMaxPps,
       "hpnicfGlobalBroadcastMaxRatio": hpnicfGlobalBroadcastMaxRatio,
       "hpnicfBpduTunnelStatus": hpnicfBpduTunnelStatus,
       "hpnicfVlanVPNTPIDMode": hpnicfVlanVPNTPIDMode,
       "hpnicfVlanVPNTPID": hpnicfVlanVPNTPID,
       "hpnicfPortIsolateGroupTable": hpnicfPortIsolateGroupTable,
       "hpnicfPortIsolateGroupEntry": hpnicfPortIsolateGroupEntry,
       "hpnicfPortIsolateGroupIndex": hpnicfPortIsolateGroupIndex,
       "hpnicfPortIsolateUplinkIfIndex": hpnicfPortIsolateUplinkIfIndex,
       "hpnicfPortIsolateGroupRowStatus": hpnicfPortIsolateGroupRowStatus,
       "hpnicfPortIsolateGroupDescription": hpnicfPortIsolateGroupDescription,
       "hpnicfMaxMacLearnRange": hpnicfMaxMacLearnRange,
       "hpnicfifPortProtocolStatTable": hpnicfifPortProtocolStatTable,
       "hpnicfifPortProtocolStatEntry": hpnicfifPortProtocolStatEntry,
       "hpnicfifIPv4InOctets": hpnicfifIPv4InOctets,
       "hpnicfifIPv4InUcastPkts": hpnicfifIPv4InUcastPkts,
       "hpnicfifIPv4InMultiPkts": hpnicfifIPv4InMultiPkts,
       "hpnicfifIPv4InBroadcastPkts": hpnicfifIPv4InBroadcastPkts,
       "hpnicfifIPv4InDiscards": hpnicfifIPv4InDiscards,
       "hpnicfifIPv4InErrors": hpnicfifIPv4InErrors,
       "hpnicfifIPv4OutOctets": hpnicfifIPv4OutOctets,
       "hpnicfifIPv4OutUcastPkts": hpnicfifIPv4OutUcastPkts,
       "hpnicfifIPv4OutMultiPkts": hpnicfifIPv4OutMultiPkts,
       "hpnicfifIPv4OutBroadcastPkts": hpnicfifIPv4OutBroadcastPkts,
       "hpnicfifIPv4OutDiscards": hpnicfifIPv4OutDiscards,
       "hpnicfifIPv4OutErrors": hpnicfifIPv4OutErrors,
       "hpnicfifIPv6InOctets": hpnicfifIPv6InOctets,
       "hpnicfifIPv6InUcastPkts": hpnicfifIPv6InUcastPkts,
       "hpnicfifIPv6InMultiPkts": hpnicfifIPv6InMultiPkts,
       "hpnicfifIPv6InAnycastPkts": hpnicfifIPv6InAnycastPkts,
       "hpnicfifIPv6InDiscards": hpnicfifIPv6InDiscards,
       "hpnicfifIPv6InErrors": hpnicfifIPv6InErrors,
       "hpnicfifIPv6OutOctets": hpnicfifIPv6OutOctets,
       "hpnicfifIPv6OutUcastPkts": hpnicfifIPv6OutUcastPkts,
       "hpnicfifIPv6OutMultiPkts": hpnicfifIPv6OutMultiPkts,
       "hpnicfifIPv6OutAnycastPkts": hpnicfifIPv6OutAnycastPkts,
       "hpnicfifIPv6OutDiscards": hpnicfifIPv6OutDiscards,
       "hpnicfifIPv6OutErrors": hpnicfifIPv6OutErrors}
)
