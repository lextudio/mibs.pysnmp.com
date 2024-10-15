# SNMP MIB module (HH3C-LswINF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-LswINF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:52:44 2024
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

(hh3clswCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3clswCommon")

(ifEntry,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
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

hh3cLswL2InfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5)
)
hh3cLswL2InfMib.setRevisions(
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



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"


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

_Hh3cLswExtInterface_ObjectIdentity = ObjectIdentity
hh3cLswExtInterface = _Hh3cLswExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1)
)
_Hh3cifXXTable_Object = MibTable
hh3cifXXTable = _Hh3cifXXTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cifXXTable.setStatus("current")
_Hh3cifXXEntry_Object = MibTableRow
hh3cifXXEntry = _Hh3cifXXEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cifXXEntry.setStatus("current")
_Hh3cifUnBoundPort_Type = TruthValue
_Hh3cifUnBoundPort_Object = MibTableColumn
hh3cifUnBoundPort = _Hh3cifUnBoundPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 1),
    _Hh3cifUnBoundPort_Type()
)
hh3cifUnBoundPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifUnBoundPort.setStatus("current")
_Hh3cifISPhyPort_Type = TruthValue
_Hh3cifISPhyPort_Object = MibTableColumn
hh3cifISPhyPort = _Hh3cifISPhyPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 2),
    _Hh3cifISPhyPort_Type()
)
hh3cifISPhyPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifISPhyPort.setStatus("current")
_Hh3cifAggregatePort_Type = TruthValue
_Hh3cifAggregatePort_Object = MibTableColumn
hh3cifAggregatePort = _Hh3cifAggregatePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 3),
    _Hh3cifAggregatePort_Type()
)
hh3cifAggregatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifAggregatePort.setStatus("current")
_Hh3cifMirrorPort_Type = TruthValue
_Hh3cifMirrorPort_Object = MibTableColumn
hh3cifMirrorPort = _Hh3cifMirrorPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 4),
    _Hh3cifMirrorPort_Type()
)
hh3cifMirrorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifMirrorPort.setStatus("current")


class _Hh3cifVLANType_Type(Integer32):
    """Custom type hh3cifVLANType based on Integer32"""
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


_Hh3cifVLANType_Type.__name__ = "Integer32"
_Hh3cifVLANType_Object = MibTableColumn
hh3cifVLANType = _Hh3cifVLANType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 5),
    _Hh3cifVLANType_Type()
)
hh3cifVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifVLANType.setStatus("current")


class _Hh3cifMcastControl_Type(Integer32):
    """Custom type hh3cifMcastControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Hh3cifMcastControl_Type.__name__ = "Integer32"
_Hh3cifMcastControl_Object = MibTableColumn
hh3cifMcastControl = _Hh3cifMcastControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 6),
    _Hh3cifMcastControl_Type()
)
hh3cifMcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifMcastControl.setStatus("current")
_Hh3cifFlowControl_Type = TruthValue
_Hh3cifFlowControl_Object = MibTableColumn
hh3cifFlowControl = _Hh3cifFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 7),
    _Hh3cifFlowControl_Type()
)
hh3cifFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifFlowControl.setStatus("current")
_Hh3cifSrcMacControl_Type = TruthValue
_Hh3cifSrcMacControl_Object = MibTableColumn
hh3cifSrcMacControl = _Hh3cifSrcMacControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 8),
    _Hh3cifSrcMacControl_Type()
)
hh3cifSrcMacControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifSrcMacControl.setStatus("current")


class _Hh3cifClearStat_Type(Integer32):
    """Custom type hh3cifClearStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Hh3cifClearStat_Type.__name__ = "Integer32"
_Hh3cifClearStat_Object = MibTableColumn
hh3cifClearStat = _Hh3cifClearStat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 9),
    _Hh3cifClearStat_Type()
)
hh3cifClearStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifClearStat.setStatus("current")
_Hh3cifXXBasePortIndex_Type = Integer32
_Hh3cifXXBasePortIndex_Object = MibTableColumn
hh3cifXXBasePortIndex = _Hh3cifXXBasePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 10),
    _Hh3cifXXBasePortIndex_Type()
)
hh3cifXXBasePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifXXBasePortIndex.setStatus("current")
_Hh3cifXXDevPortIndex_Type = Integer32
_Hh3cifXXDevPortIndex_Object = MibTableColumn
hh3cifXXDevPortIndex = _Hh3cifXXDevPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 11),
    _Hh3cifXXDevPortIndex_Type()
)
hh3cifXXDevPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifXXDevPortIndex.setStatus("current")
_Hh3cifPpsMcastControl_Type = Integer32
_Hh3cifPpsMcastControl_Object = MibTableColumn
hh3cifPpsMcastControl = _Hh3cifPpsMcastControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 12),
    _Hh3cifPpsMcastControl_Type()
)
hh3cifPpsMcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifPpsMcastControl.setStatus("current")


class _Hh3cifPpsBcastDisValControl_Type(Integer32):
    """Custom type hh3cifPpsBcastDisValControl based on Integer32"""
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


_Hh3cifPpsBcastDisValControl_Type.__name__ = "Integer32"
_Hh3cifPpsBcastDisValControl_Object = MibTableColumn
hh3cifPpsBcastDisValControl = _Hh3cifPpsBcastDisValControl_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 13),
    _Hh3cifPpsBcastDisValControl_Type()
)
hh3cifPpsBcastDisValControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifPpsBcastDisValControl.setStatus("current")
_Hh3cifUniSuppressionStep_Type = Integer32
_Hh3cifUniSuppressionStep_Object = MibTableColumn
hh3cifUniSuppressionStep = _Hh3cifUniSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 14),
    _Hh3cifUniSuppressionStep_Type()
)
hh3cifUniSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifUniSuppressionStep.setStatus("current")
_Hh3cifPpsUniSuppressionMax_Type = Integer32
_Hh3cifPpsUniSuppressionMax_Object = MibTableColumn
hh3cifPpsUniSuppressionMax = _Hh3cifPpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 15),
    _Hh3cifPpsUniSuppressionMax_Type()
)
hh3cifPpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifPpsUniSuppressionMax.setStatus("current")
_Hh3cifMulSuppressionStep_Type = Integer32
_Hh3cifMulSuppressionStep_Object = MibTableColumn
hh3cifMulSuppressionStep = _Hh3cifMulSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 16),
    _Hh3cifMulSuppressionStep_Type()
)
hh3cifMulSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifMulSuppressionStep.setStatus("current")
_Hh3cifPpsMulSuppressionMax_Type = Integer32
_Hh3cifPpsMulSuppressionMax_Object = MibTableColumn
hh3cifPpsMulSuppressionMax = _Hh3cifPpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 17),
    _Hh3cifPpsMulSuppressionMax_Type()
)
hh3cifPpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifPpsMulSuppressionMax.setStatus("current")
_Hh3cifUniSuppression_Type = Integer32
_Hh3cifUniSuppression_Object = MibTableColumn
hh3cifUniSuppression = _Hh3cifUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 18),
    _Hh3cifUniSuppression_Type()
)
hh3cifUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifUniSuppression.setStatus("current")
_Hh3cifPpsUniSuppression_Type = Integer32
_Hh3cifPpsUniSuppression_Object = MibTableColumn
hh3cifPpsUniSuppression = _Hh3cifPpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 19),
    _Hh3cifPpsUniSuppression_Type()
)
hh3cifPpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifPpsUniSuppression.setStatus("current")
_Hh3cifMulSuppression_Type = Integer32
_Hh3cifMulSuppression_Object = MibTableColumn
hh3cifMulSuppression = _Hh3cifMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 20),
    _Hh3cifMulSuppression_Type()
)
hh3cifMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifMulSuppression.setStatus("current")
_Hh3cifPpsMulSuppression_Type = Integer32
_Hh3cifPpsMulSuppression_Object = MibTableColumn
hh3cifPpsMulSuppression = _Hh3cifPpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 21),
    _Hh3cifPpsMulSuppression_Type()
)
hh3cifPpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifPpsMulSuppression.setStatus("current")


class _Hh3cifComboActivePort_Type(Integer32):
    """Custom type hh3cifComboActivePort based on Integer32"""
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


_Hh3cifComboActivePort_Type.__name__ = "Integer32"
_Hh3cifComboActivePort_Object = MibTableColumn
hh3cifComboActivePort = _Hh3cifComboActivePort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 22),
    _Hh3cifComboActivePort_Type()
)
hh3cifComboActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifComboActivePort.setStatus("obsolete")
_Hh3cifBMbpsMulSuppressionMax_Type = Integer32
_Hh3cifBMbpsMulSuppressionMax_Object = MibTableColumn
hh3cifBMbpsMulSuppressionMax = _Hh3cifBMbpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 23),
    _Hh3cifBMbpsMulSuppressionMax_Type()
)
hh3cifBMbpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifBMbpsMulSuppressionMax.setStatus("current")
_Hh3cifBMbpsMulSuppression_Type = Integer32
_Hh3cifBMbpsMulSuppression_Object = MibTableColumn
hh3cifBMbpsMulSuppression = _Hh3cifBMbpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 24),
    _Hh3cifBMbpsMulSuppression_Type()
)
hh3cifBMbpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifBMbpsMulSuppression.setStatus("current")
_Hh3cifBKbpsMulSuppressionMax_Type = Integer32
_Hh3cifBKbpsMulSuppressionMax_Object = MibTableColumn
hh3cifBKbpsMulSuppressionMax = _Hh3cifBKbpsMulSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 25),
    _Hh3cifBKbpsMulSuppressionMax_Type()
)
hh3cifBKbpsMulSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifBKbpsMulSuppressionMax.setStatus("current")
_Hh3cifBKbpsMulSuppressionStep_Type = Integer32
_Hh3cifBKbpsMulSuppressionStep_Object = MibTableColumn
hh3cifBKbpsMulSuppressionStep = _Hh3cifBKbpsMulSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 26),
    _Hh3cifBKbpsMulSuppressionStep_Type()
)
hh3cifBKbpsMulSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifBKbpsMulSuppressionStep.setStatus("current")
_Hh3cifBKbpsMulSuppression_Type = Integer32
_Hh3cifBKbpsMulSuppression_Object = MibTableColumn
hh3cifBKbpsMulSuppression = _Hh3cifBKbpsMulSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 27),
    _Hh3cifBKbpsMulSuppression_Type()
)
hh3cifBKbpsMulSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifBKbpsMulSuppression.setStatus("current")


class _Hh3cifUnknownPacketDropMul_Type(DropDirection):
    """Custom type hh3cifUnknownPacketDropMul based on DropDirection"""


_Hh3cifUnknownPacketDropMul_Object = MibTableColumn
hh3cifUnknownPacketDropMul = _Hh3cifUnknownPacketDropMul_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 28),
    _Hh3cifUnknownPacketDropMul_Type()
)
hh3cifUnknownPacketDropMul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifUnknownPacketDropMul.setStatus("current")


class _Hh3cifUnknownPacketDropUni_Type(DropDirection):
    """Custom type hh3cifUnknownPacketDropUni based on DropDirection"""


_Hh3cifUnknownPacketDropUni_Object = MibTableColumn
hh3cifUnknownPacketDropUni = _Hh3cifUnknownPacketDropUni_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 29),
    _Hh3cifUnknownPacketDropUni_Type()
)
hh3cifUnknownPacketDropUni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifUnknownPacketDropUni.setStatus("current")
_Hh3cifBMbpsUniSuppressionMax_Type = Integer32
_Hh3cifBMbpsUniSuppressionMax_Object = MibTableColumn
hh3cifBMbpsUniSuppressionMax = _Hh3cifBMbpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 30),
    _Hh3cifBMbpsUniSuppressionMax_Type()
)
hh3cifBMbpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifBMbpsUniSuppressionMax.setStatus("current")
_Hh3cifBMbpsUniSuppression_Type = Integer32
_Hh3cifBMbpsUniSuppression_Object = MibTableColumn
hh3cifBMbpsUniSuppression = _Hh3cifBMbpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 31),
    _Hh3cifBMbpsUniSuppression_Type()
)
hh3cifBMbpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifBMbpsUniSuppression.setStatus("current")
_Hh3cifBKbpsUniSuppressionMax_Type = Integer32
_Hh3cifBKbpsUniSuppressionMax_Object = MibTableColumn
hh3cifBKbpsUniSuppressionMax = _Hh3cifBKbpsUniSuppressionMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 32),
    _Hh3cifBKbpsUniSuppressionMax_Type()
)
hh3cifBKbpsUniSuppressionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifBKbpsUniSuppressionMax.setStatus("current")
_Hh3cifBKbpsUniSuppressionStep_Type = Integer32
_Hh3cifBKbpsUniSuppressionStep_Object = MibTableColumn
hh3cifBKbpsUniSuppressionStep = _Hh3cifBKbpsUniSuppressionStep_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 33),
    _Hh3cifBKbpsUniSuppressionStep_Type()
)
hh3cifBKbpsUniSuppressionStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifBKbpsUniSuppressionStep.setStatus("current")
_Hh3cifBKbpsUniSuppression_Type = Integer32
_Hh3cifBKbpsUniSuppression_Object = MibTableColumn
hh3cifBKbpsUniSuppression = _Hh3cifBKbpsUniSuppression_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 34),
    _Hh3cifBKbpsUniSuppression_Type()
)
hh3cifBKbpsUniSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifBKbpsUniSuppression.setStatus("current")
_Hh3cifOutPayloadOctets_Type = Counter64
_Hh3cifOutPayloadOctets_Object = MibTableColumn
hh3cifOutPayloadOctets = _Hh3cifOutPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 35),
    _Hh3cifOutPayloadOctets_Type()
)
hh3cifOutPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifOutPayloadOctets.setStatus("current")
_Hh3cifInPayloadOctets_Type = Counter64
_Hh3cifInPayloadOctets_Object = MibTableColumn
hh3cifInPayloadOctets = _Hh3cifInPayloadOctets_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 36),
    _Hh3cifInPayloadOctets_Type()
)
hh3cifInPayloadOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifInPayloadOctets.setStatus("current")
_Hh3cifInErrorPktsRate_Type = Integer32
_Hh3cifInErrorPktsRate_Object = MibTableColumn
hh3cifInErrorPktsRate = _Hh3cifInErrorPktsRate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 37),
    _Hh3cifInErrorPktsRate_Type()
)
hh3cifInErrorPktsRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifInErrorPktsRate.setStatus("current")
_Hh3cifInPkts_Type = Counter64
_Hh3cifInPkts_Object = MibTableColumn
hh3cifInPkts = _Hh3cifInPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 38),
    _Hh3cifInPkts_Type()
)
hh3cifInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifInPkts.setStatus("current")
_Hh3cifInNormalPkts_Type = Counter64
_Hh3cifInNormalPkts_Object = MibTableColumn
hh3cifInNormalPkts = _Hh3cifInNormalPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 39),
    _Hh3cifInNormalPkts_Type()
)
hh3cifInNormalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifInNormalPkts.setStatus("current")
_Hh3cifOutPkts_Type = Counter64
_Hh3cifOutPkts_Object = MibTableColumn
hh3cifOutPkts = _Hh3cifOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 1, 1, 40),
    _Hh3cifOutPkts_Type()
)
hh3cifOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifOutPkts.setStatus("current")
_Hh3cifAggregateTable_Object = MibTable
hh3cifAggregateTable = _Hh3cifAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cifAggregateTable.setStatus("current")
_Hh3cifAggregateEntry_Object = MibTableRow
hh3cifAggregateEntry = _Hh3cifAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1)
)
hh3cifAggregateEntry.setIndexNames(
    (0, "HH3C-LswINF-MIB", "hh3cifAggregatePortIndex"),
)
if mibBuilder.loadTexts:
    hh3cifAggregateEntry.setStatus("current")
_Hh3cifAggregatePortIndex_Type = InterfaceIndex
_Hh3cifAggregatePortIndex_Object = MibTableColumn
hh3cifAggregatePortIndex = _Hh3cifAggregatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 1),
    _Hh3cifAggregatePortIndex_Type()
)
hh3cifAggregatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifAggregatePortIndex.setStatus("current")


class _Hh3cifAggregatePortName_Type(OctetString):
    """Custom type hh3cifAggregatePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Hh3cifAggregatePortName_Type.__name__ = "OctetString"
_Hh3cifAggregatePortName_Object = MibTableColumn
hh3cifAggregatePortName = _Hh3cifAggregatePortName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 2),
    _Hh3cifAggregatePortName_Type()
)
hh3cifAggregatePortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifAggregatePortName.setStatus("current")
_Hh3cifAggregatePortListPorts_Type = PortList
_Hh3cifAggregatePortListPorts_Object = MibTableColumn
hh3cifAggregatePortListPorts = _Hh3cifAggregatePortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 3),
    _Hh3cifAggregatePortListPorts_Type()
)
hh3cifAggregatePortListPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifAggregatePortListPorts.setStatus("current")


class _Hh3cifAggregateModel_Type(Integer32):
    """Custom type hh3cifAggregateModel based on Integer32"""
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


_Hh3cifAggregateModel_Type.__name__ = "Integer32"
_Hh3cifAggregateModel_Object = MibTableColumn
hh3cifAggregateModel = _Hh3cifAggregateModel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 4),
    _Hh3cifAggregateModel_Type()
)
hh3cifAggregateModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifAggregateModel.setStatus("current")
_Hh3cifAggregateOperStatus_Type = RowStatus
_Hh3cifAggregateOperStatus_Object = MibTableColumn
hh3cifAggregateOperStatus = _Hh3cifAggregateOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 2, 1, 5),
    _Hh3cifAggregateOperStatus_Type()
)
hh3cifAggregateOperStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cifAggregateOperStatus.setStatus("current")
_Hh3cifHybridPortTable_Object = MibTable
hh3cifHybridPortTable = _Hh3cifHybridPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cifHybridPortTable.setStatus("current")
_Hh3cifHybridPortEntry_Object = MibTableRow
hh3cifHybridPortEntry = _Hh3cifHybridPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1)
)
hh3cifHybridPortEntry.setIndexNames(
    (0, "HH3C-LswINF-MIB", "hh3cifHybridPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cifHybridPortEntry.setStatus("current")
_Hh3cifHybridPortIndex_Type = Integer32
_Hh3cifHybridPortIndex_Object = MibTableColumn
hh3cifHybridPortIndex = _Hh3cifHybridPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 1),
    _Hh3cifHybridPortIndex_Type()
)
hh3cifHybridPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifHybridPortIndex.setStatus("current")


class _Hh3cifHybridTaggedVlanListLow_Type(OctetString):
    """Custom type hh3cifHybridTaggedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifHybridTaggedVlanListLow_Type.__name__ = "OctetString"
_Hh3cifHybridTaggedVlanListLow_Object = MibTableColumn
hh3cifHybridTaggedVlanListLow = _Hh3cifHybridTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 2),
    _Hh3cifHybridTaggedVlanListLow_Type()
)
hh3cifHybridTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifHybridTaggedVlanListLow.setStatus("current")


class _Hh3cifHybridTaggedVlanListHigh_Type(OctetString):
    """Custom type hh3cifHybridTaggedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifHybridTaggedVlanListHigh_Type.__name__ = "OctetString"
_Hh3cifHybridTaggedVlanListHigh_Object = MibTableColumn
hh3cifHybridTaggedVlanListHigh = _Hh3cifHybridTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 3),
    _Hh3cifHybridTaggedVlanListHigh_Type()
)
hh3cifHybridTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifHybridTaggedVlanListHigh.setStatus("current")


class _Hh3cifHybridUnTaggedVlanListLow_Type(OctetString):
    """Custom type hh3cifHybridUnTaggedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifHybridUnTaggedVlanListLow_Type.__name__ = "OctetString"
_Hh3cifHybridUnTaggedVlanListLow_Object = MibTableColumn
hh3cifHybridUnTaggedVlanListLow = _Hh3cifHybridUnTaggedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 4),
    _Hh3cifHybridUnTaggedVlanListLow_Type()
)
hh3cifHybridUnTaggedVlanListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifHybridUnTaggedVlanListLow.setStatus("current")


class _Hh3cifHybridUnTaggedVlanListHigh_Type(OctetString):
    """Custom type hh3cifHybridUnTaggedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Hh3cifHybridUnTaggedVlanListHigh_Type.__name__ = "OctetString"
_Hh3cifHybridUnTaggedVlanListHigh_Object = MibTableColumn
hh3cifHybridUnTaggedVlanListHigh = _Hh3cifHybridUnTaggedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 3, 1, 5),
    _Hh3cifHybridUnTaggedVlanListHigh_Type()
)
hh3cifHybridUnTaggedVlanListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifHybridUnTaggedVlanListHigh.setStatus("current")
_Hh3cifComboPortTable_Object = MibTable
hh3cifComboPortTable = _Hh3cifComboPortTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cifComboPortTable.setStatus("current")
_Hh3cifComboPortEntry_Object = MibTableRow
hh3cifComboPortEntry = _Hh3cifComboPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4, 1)
)
hh3cifComboPortEntry.setIndexNames(
    (0, "HH3C-LswINF-MIB", "hh3cifComboPortIndex"),
)
if mibBuilder.loadTexts:
    hh3cifComboPortEntry.setStatus("current")
_Hh3cifComboPortIndex_Type = InterfaceIndex
_Hh3cifComboPortIndex_Object = MibTableColumn
hh3cifComboPortIndex = _Hh3cifComboPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4, 1, 1),
    _Hh3cifComboPortIndex_Type()
)
hh3cifComboPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifComboPortIndex.setStatus("current")


class _Hh3cifComboPortCurActive_Type(Integer32):
    """Custom type hh3cifComboPortCurActive based on Integer32"""
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


_Hh3cifComboPortCurActive_Type.__name__ = "Integer32"
_Hh3cifComboPortCurActive_Object = MibTableColumn
hh3cifComboPortCurActive = _Hh3cifComboPortCurActive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 1, 4, 1, 2),
    _Hh3cifComboPortCurActive_Type()
)
hh3cifComboPortCurActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifComboPortCurActive.setStatus("current")
_Hh3cLswL2InfMibObject_ObjectIdentity = ObjectIdentity
hh3cLswL2InfMibObject = _Hh3cLswL2InfMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1)
)
_Hh3cSlotPortMax_Type = Integer32
_Hh3cSlotPortMax_Object = MibScalar
hh3cSlotPortMax = _Hh3cSlotPortMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 1),
    _Hh3cSlotPortMax_Type()
)
hh3cSlotPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSlotPortMax.setStatus("current")
_Hh3cSwitchPortMax_Type = Integer32
_Hh3cSwitchPortMax_Object = MibScalar
hh3cSwitchPortMax = _Hh3cSwitchPortMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 2),
    _Hh3cSwitchPortMax_Type()
)
hh3cSwitchPortMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSwitchPortMax.setStatus("current")
_Hh3cifVLANTrunkStatusTable_Object = MibTable
hh3cifVLANTrunkStatusTable = _Hh3cifVLANTrunkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cifVLANTrunkStatusTable.setStatus("current")
_Hh3cifVLANTrunkStatusEntry_Object = MibTableRow
hh3cifVLANTrunkStatusEntry = _Hh3cifVLANTrunkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1)
)
hh3cifVLANTrunkStatusEntry.setIndexNames(
    (0, "HH3C-LswINF-MIB", "hh3cifVLANTrunkIndex"),
)
if mibBuilder.loadTexts:
    hh3cifVLANTrunkStatusEntry.setStatus("current")
_Hh3cifVLANTrunkIndex_Type = InterfaceIndex
_Hh3cifVLANTrunkIndex_Object = MibTableColumn
hh3cifVLANTrunkIndex = _Hh3cifVLANTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 1),
    _Hh3cifVLANTrunkIndex_Type()
)
hh3cifVLANTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifVLANTrunkIndex.setStatus("current")


class _Hh3cifVLANTrunkGvrpRegistration_Type(Integer32):
    """Custom type hh3cifVLANTrunkGvrpRegistration based on Integer32"""
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


_Hh3cifVLANTrunkGvrpRegistration_Type.__name__ = "Integer32"
_Hh3cifVLANTrunkGvrpRegistration_Object = MibTableColumn
hh3cifVLANTrunkGvrpRegistration = _Hh3cifVLANTrunkGvrpRegistration_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 2),
    _Hh3cifVLANTrunkGvrpRegistration_Type()
)
hh3cifVLANTrunkGvrpRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifVLANTrunkGvrpRegistration.setStatus("current")
_Hh3cifVLANTrunkPassListLow_Type = OctetString
_Hh3cifVLANTrunkPassListLow_Object = MibTableColumn
hh3cifVLANTrunkPassListLow = _Hh3cifVLANTrunkPassListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 4),
    _Hh3cifVLANTrunkPassListLow_Type()
)
hh3cifVLANTrunkPassListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifVLANTrunkPassListLow.setStatus("current")
_Hh3cifVLANTrunkPassListHigh_Type = OctetString
_Hh3cifVLANTrunkPassListHigh_Object = MibTableColumn
hh3cifVLANTrunkPassListHigh = _Hh3cifVLANTrunkPassListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 5),
    _Hh3cifVLANTrunkPassListHigh_Type()
)
hh3cifVLANTrunkPassListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifVLANTrunkPassListHigh.setStatus("current")
_Hh3cifVLANTrunkAllowListLow_Type = OctetString
_Hh3cifVLANTrunkAllowListLow_Object = MibTableColumn
hh3cifVLANTrunkAllowListLow = _Hh3cifVLANTrunkAllowListLow_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 6),
    _Hh3cifVLANTrunkAllowListLow_Type()
)
hh3cifVLANTrunkAllowListLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifVLANTrunkAllowListLow.setStatus("current")
_Hh3cifVLANTrunkAllowListHigh_Type = OctetString
_Hh3cifVLANTrunkAllowListHigh_Object = MibTableColumn
hh3cifVLANTrunkAllowListHigh = _Hh3cifVLANTrunkAllowListHigh_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 3, 1, 7),
    _Hh3cifVLANTrunkAllowListHigh_Type()
)
hh3cifVLANTrunkAllowListHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifVLANTrunkAllowListHigh.setStatus("current")
_Hh3cethernetTable_Object = MibTable
hh3cethernetTable = _Hh3cethernetTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cethernetTable.setStatus("current")
_Hh3cethernetEntry_Object = MibTableRow
hh3cethernetEntry = _Hh3cethernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cethernetEntry.setStatus("current")


class _Hh3cifEthernetDuplex_Type(Integer32):
    """Custom type hh3cifEthernetDuplex based on Integer32"""
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


_Hh3cifEthernetDuplex_Type.__name__ = "Integer32"
_Hh3cifEthernetDuplex_Object = MibTableColumn
hh3cifEthernetDuplex = _Hh3cifEthernetDuplex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 3),
    _Hh3cifEthernetDuplex_Type()
)
hh3cifEthernetDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetDuplex.setStatus("current")
_Hh3cifEthernetMTU_Type = Integer32
_Hh3cifEthernetMTU_Object = MibTableColumn
hh3cifEthernetMTU = _Hh3cifEthernetMTU_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 4),
    _Hh3cifEthernetMTU_Type()
)
hh3cifEthernetMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetMTU.setStatus("current")


class _Hh3cifEthernetSpeed_Type(Integer32):
    """Custom type hh3cifEthernetSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              100,
              1000,
              10000,
              24000)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("s10000M", 10000),
          ("s1000M", 1000),
          ("s100M", 100),
          ("s10M", 10),
          ("s24000M", 24000))
    )


_Hh3cifEthernetSpeed_Type.__name__ = "Integer32"
_Hh3cifEthernetSpeed_Object = MibTableColumn
hh3cifEthernetSpeed = _Hh3cifEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 5),
    _Hh3cifEthernetSpeed_Type()
)
hh3cifEthernetSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetSpeed.setStatus("current")


class _Hh3cifEthernetMdi_Type(Integer32):
    """Custom type hh3cifEthernetMdi based on Integer32"""
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


_Hh3cifEthernetMdi_Type.__name__ = "Integer32"
_Hh3cifEthernetMdi_Object = MibTableColumn
hh3cifEthernetMdi = _Hh3cifEthernetMdi_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 7),
    _Hh3cifEthernetMdi_Type()
)
hh3cifEthernetMdi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetMdi.setStatus("current")


class _Hh3cMaxMacLearn_Type(Integer32):
    """Custom type hh3cMaxMacLearn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_Hh3cMaxMacLearn_Type.__name__ = "Integer32"
_Hh3cMaxMacLearn_Object = MibTableColumn
hh3cMaxMacLearn = _Hh3cMaxMacLearn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 8),
    _Hh3cMaxMacLearn_Type()
)
hh3cMaxMacLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cMaxMacLearn.setStatus("current")


class _Hh3cifMacAddressLearn_Type(Integer32):
    """Custom type hh3cifMacAddressLearn based on Integer32"""
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


_Hh3cifMacAddressLearn_Type.__name__ = "Integer32"
_Hh3cifMacAddressLearn_Object = MibTableColumn
hh3cifMacAddressLearn = _Hh3cifMacAddressLearn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 9),
    _Hh3cifMacAddressLearn_Type()
)
hh3cifMacAddressLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifMacAddressLearn.setStatus("current")


class _Hh3cifEthernetTest_Type(Integer32):
    """Custom type hh3cifEthernetTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("test", 1)
    )


_Hh3cifEthernetTest_Type.__name__ = "Integer32"
_Hh3cifEthernetTest_Object = MibTableColumn
hh3cifEthernetTest = _Hh3cifEthernetTest_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 10),
    _Hh3cifEthernetTest_Type()
)
hh3cifEthernetTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetTest.setStatus("current")


class _Hh3cifMacAddrLearnMode_Type(Integer32):
    """Custom type hh3cifMacAddrLearnMode based on Integer32"""
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


_Hh3cifMacAddrLearnMode_Type.__name__ = "Integer32"
_Hh3cifMacAddrLearnMode_Object = MibTableColumn
hh3cifMacAddrLearnMode = _Hh3cifMacAddrLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 11),
    _Hh3cifMacAddrLearnMode_Type()
)
hh3cifMacAddrLearnMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifMacAddrLearnMode.setStatus("current")


class _Hh3cifEthernetFlowInterval_Type(Integer32):
    """Custom type hh3cifEthernetFlowInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 300),
    )


_Hh3cifEthernetFlowInterval_Type.__name__ = "Integer32"
_Hh3cifEthernetFlowInterval_Object = MibTableColumn
hh3cifEthernetFlowInterval = _Hh3cifEthernetFlowInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 12),
    _Hh3cifEthernetFlowInterval_Type()
)
hh3cifEthernetFlowInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetFlowInterval.setStatus("current")
_Hh3cifEthernetIsolate_Type = OctetString
_Hh3cifEthernetIsolate_Object = MibTableColumn
hh3cifEthernetIsolate = _Hh3cifEthernetIsolate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 13),
    _Hh3cifEthernetIsolate_Type()
)
hh3cifEthernetIsolate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetIsolate.setStatus("current")


class _Hh3cifVlanVPNStatus_Type(Integer32):
    """Custom type hh3cifVlanVPNStatus based on Integer32"""
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


_Hh3cifVlanVPNStatus_Type.__name__ = "Integer32"
_Hh3cifVlanVPNStatus_Object = MibTableColumn
hh3cifVlanVPNStatus = _Hh3cifVlanVPNStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 14),
    _Hh3cifVlanVPNStatus_Type()
)
hh3cifVlanVPNStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifVlanVPNStatus.setStatus("current")


class _Hh3cifVlanVPNUplinkStatus_Type(Integer32):
    """Custom type hh3cifVlanVPNUplinkStatus based on Integer32"""
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


_Hh3cifVlanVPNUplinkStatus_Type.__name__ = "Integer32"
_Hh3cifVlanVPNUplinkStatus_Object = MibTableColumn
hh3cifVlanVPNUplinkStatus = _Hh3cifVlanVPNUplinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 15),
    _Hh3cifVlanVPNUplinkStatus_Type()
)
hh3cifVlanVPNUplinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifVlanVPNUplinkStatus.setStatus("current")


class _Hh3cifVlanVPNTPID_Type(Integer32):
    """Custom type hh3cifVlanVPNTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cifVlanVPNTPID_Type.__name__ = "Integer32"
_Hh3cifVlanVPNTPID_Object = MibTableColumn
hh3cifVlanVPNTPID = _Hh3cifVlanVPNTPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 16),
    _Hh3cifVlanVPNTPID_Type()
)
hh3cifVlanVPNTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifVlanVPNTPID.setStatus("current")
_Hh3cifIsolateGroupID_Type = Integer32
_Hh3cifIsolateGroupID_Object = MibTableColumn
hh3cifIsolateGroupID = _Hh3cifIsolateGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 17),
    _Hh3cifIsolateGroupID_Type()
)
hh3cifIsolateGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifIsolateGroupID.setStatus("current")


class _Hh3cifisUplinkPort_Type(Integer32):
    """Custom type hh3cifisUplinkPort based on Integer32"""
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


_Hh3cifisUplinkPort_Type.__name__ = "Integer32"
_Hh3cifisUplinkPort_Object = MibTableColumn
hh3cifisUplinkPort = _Hh3cifisUplinkPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 18),
    _Hh3cifisUplinkPort_Type()
)
hh3cifisUplinkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifisUplinkPort.setStatus("current")
_Hh3cifEthernetAutoSpeedMask_Type = SpeedModeFlag
_Hh3cifEthernetAutoSpeedMask_Object = MibTableColumn
hh3cifEthernetAutoSpeedMask = _Hh3cifEthernetAutoSpeedMask_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 19),
    _Hh3cifEthernetAutoSpeedMask_Type()
)
hh3cifEthernetAutoSpeedMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cifEthernetAutoSpeedMask.setStatus("current")
_Hh3cifEthernetAutoSpeed_Type = SpeedModeFlag
_Hh3cifEthernetAutoSpeed_Object = MibTableColumn
hh3cifEthernetAutoSpeed = _Hh3cifEthernetAutoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 4, 1, 20),
    _Hh3cifEthernetAutoSpeed_Type()
)
hh3cifEthernetAutoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cifEthernetAutoSpeed.setStatus("current")
_Hh3cIsolateGroupMax_Type = Integer32
_Hh3cIsolateGroupMax_Object = MibScalar
hh3cIsolateGroupMax = _Hh3cIsolateGroupMax_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 5),
    _Hh3cIsolateGroupMax_Type()
)
hh3cIsolateGroupMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIsolateGroupMax.setStatus("current")


class _Hh3cGlobalBroadcastMaxPps_Type(Integer32):
    """Custom type hh3cGlobalBroadcastMaxPps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14881000),
    )


_Hh3cGlobalBroadcastMaxPps_Type.__name__ = "Integer32"
_Hh3cGlobalBroadcastMaxPps_Object = MibScalar
hh3cGlobalBroadcastMaxPps = _Hh3cGlobalBroadcastMaxPps_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 6),
    _Hh3cGlobalBroadcastMaxPps_Type()
)
hh3cGlobalBroadcastMaxPps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cGlobalBroadcastMaxPps.setStatus("current")


class _Hh3cGlobalBroadcastMaxRatio_Type(Integer32):
    """Custom type hh3cGlobalBroadcastMaxRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cGlobalBroadcastMaxRatio_Type.__name__ = "Integer32"
_Hh3cGlobalBroadcastMaxRatio_Object = MibScalar
hh3cGlobalBroadcastMaxRatio = _Hh3cGlobalBroadcastMaxRatio_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 7),
    _Hh3cGlobalBroadcastMaxRatio_Type()
)
hh3cGlobalBroadcastMaxRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cGlobalBroadcastMaxRatio.setStatus("current")


class _Hh3cBpduTunnelStatus_Type(Integer32):
    """Custom type hh3cBpduTunnelStatus based on Integer32"""
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


_Hh3cBpduTunnelStatus_Type.__name__ = "Integer32"
_Hh3cBpduTunnelStatus_Object = MibScalar
hh3cBpduTunnelStatus = _Hh3cBpduTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 8),
    _Hh3cBpduTunnelStatus_Type()
)
hh3cBpduTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cBpduTunnelStatus.setStatus("current")


class _Hh3cVlanVPNTPIDMode_Type(Integer32):
    """Custom type hh3cVlanVPNTPIDMode based on Integer32"""
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


_Hh3cVlanVPNTPIDMode_Type.__name__ = "Integer32"
_Hh3cVlanVPNTPIDMode_Object = MibScalar
hh3cVlanVPNTPIDMode = _Hh3cVlanVPNTPIDMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 9),
    _Hh3cVlanVPNTPIDMode_Type()
)
hh3cVlanVPNTPIDMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVlanVPNTPIDMode.setStatus("current")


class _Hh3cVlanVPNTPID_Type(Integer32):
    """Custom type hh3cVlanVPNTPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cVlanVPNTPID_Type.__name__ = "Integer32"
_Hh3cVlanVPNTPID_Object = MibScalar
hh3cVlanVPNTPID = _Hh3cVlanVPNTPID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 10),
    _Hh3cVlanVPNTPID_Type()
)
hh3cVlanVPNTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVlanVPNTPID.setStatus("current")
_Hh3cPortIsolateGroupTable_Object = MibTable
hh3cPortIsolateGroupTable = _Hh3cPortIsolateGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11)
)
if mibBuilder.loadTexts:
    hh3cPortIsolateGroupTable.setStatus("current")
_Hh3cPortIsolateGroupEntry_Object = MibTableRow
hh3cPortIsolateGroupEntry = _Hh3cPortIsolateGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1)
)
hh3cPortIsolateGroupEntry.setIndexNames(
    (0, "HH3C-LswINF-MIB", "hh3cPortIsolateGroupIndex"),
)
if mibBuilder.loadTexts:
    hh3cPortIsolateGroupEntry.setStatus("current")
_Hh3cPortIsolateGroupIndex_Type = Integer32
_Hh3cPortIsolateGroupIndex_Object = MibTableColumn
hh3cPortIsolateGroupIndex = _Hh3cPortIsolateGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 1),
    _Hh3cPortIsolateGroupIndex_Type()
)
hh3cPortIsolateGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cPortIsolateGroupIndex.setStatus("current")
_Hh3cPortIsolateUplinkIfIndex_Type = InterfaceIndex
_Hh3cPortIsolateUplinkIfIndex_Object = MibTableColumn
hh3cPortIsolateUplinkIfIndex = _Hh3cPortIsolateUplinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 2),
    _Hh3cPortIsolateUplinkIfIndex_Type()
)
hh3cPortIsolateUplinkIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortIsolateUplinkIfIndex.setStatus("current")
_Hh3cPortIsolateGroupRowStatus_Type = RowStatus
_Hh3cPortIsolateGroupRowStatus_Object = MibTableColumn
hh3cPortIsolateGroupRowStatus = _Hh3cPortIsolateGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 3),
    _Hh3cPortIsolateGroupRowStatus_Type()
)
hh3cPortIsolateGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortIsolateGroupRowStatus.setStatus("current")


class _Hh3cPortIsolateGroupDescription_Type(DisplayString):
    """Custom type hh3cPortIsolateGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_Hh3cPortIsolateGroupDescription_Type.__name__ = "DisplayString"
_Hh3cPortIsolateGroupDescription_Object = MibTableColumn
hh3cPortIsolateGroupDescription = _Hh3cPortIsolateGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 11, 1, 4),
    _Hh3cPortIsolateGroupDescription_Type()
)
hh3cPortIsolateGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cPortIsolateGroupDescription.setStatus("current")
_Hh3cMaxMacLearnRange_Type = Integer32
_Hh3cMaxMacLearnRange_Object = MibScalar
hh3cMaxMacLearnRange = _Hh3cMaxMacLearnRange_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 35, 5, 1, 12),
    _Hh3cMaxMacLearnRange_Type()
)
hh3cMaxMacLearnRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cMaxMacLearnRange.setStatus("current")
ifEntry.registerAugmentions(
    ("HH3C-LswINF-MIB",
     "hh3cifXXEntry")
)
hh3cifXXEntry.setIndexNames(*ifEntry.getIndexNames())
ifEntry.registerAugmentions(
    ("HH3C-LswINF-MIB",
     "hh3cethernetEntry")
)
hh3cethernetEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-LswINF-MIB",
    **{"PortList": PortList,
       "VlanIndex": VlanIndex,
       "InterfaceIndex": InterfaceIndex,
       "DropDirection": DropDirection,
       "SpeedModeFlag": SpeedModeFlag,
       "hh3cLswExtInterface": hh3cLswExtInterface,
       "hh3cifXXTable": hh3cifXXTable,
       "hh3cifXXEntry": hh3cifXXEntry,
       "hh3cifUnBoundPort": hh3cifUnBoundPort,
       "hh3cifISPhyPort": hh3cifISPhyPort,
       "hh3cifAggregatePort": hh3cifAggregatePort,
       "hh3cifMirrorPort": hh3cifMirrorPort,
       "hh3cifVLANType": hh3cifVLANType,
       "hh3cifMcastControl": hh3cifMcastControl,
       "hh3cifFlowControl": hh3cifFlowControl,
       "hh3cifSrcMacControl": hh3cifSrcMacControl,
       "hh3cifClearStat": hh3cifClearStat,
       "hh3cifXXBasePortIndex": hh3cifXXBasePortIndex,
       "hh3cifXXDevPortIndex": hh3cifXXDevPortIndex,
       "hh3cifPpsMcastControl": hh3cifPpsMcastControl,
       "hh3cifPpsBcastDisValControl": hh3cifPpsBcastDisValControl,
       "hh3cifUniSuppressionStep": hh3cifUniSuppressionStep,
       "hh3cifPpsUniSuppressionMax": hh3cifPpsUniSuppressionMax,
       "hh3cifMulSuppressionStep": hh3cifMulSuppressionStep,
       "hh3cifPpsMulSuppressionMax": hh3cifPpsMulSuppressionMax,
       "hh3cifUniSuppression": hh3cifUniSuppression,
       "hh3cifPpsUniSuppression": hh3cifPpsUniSuppression,
       "hh3cifMulSuppression": hh3cifMulSuppression,
       "hh3cifPpsMulSuppression": hh3cifPpsMulSuppression,
       "hh3cifComboActivePort": hh3cifComboActivePort,
       "hh3cifBMbpsMulSuppressionMax": hh3cifBMbpsMulSuppressionMax,
       "hh3cifBMbpsMulSuppression": hh3cifBMbpsMulSuppression,
       "hh3cifBKbpsMulSuppressionMax": hh3cifBKbpsMulSuppressionMax,
       "hh3cifBKbpsMulSuppressionStep": hh3cifBKbpsMulSuppressionStep,
       "hh3cifBKbpsMulSuppression": hh3cifBKbpsMulSuppression,
       "hh3cifUnknownPacketDropMul": hh3cifUnknownPacketDropMul,
       "hh3cifUnknownPacketDropUni": hh3cifUnknownPacketDropUni,
       "hh3cifBMbpsUniSuppressionMax": hh3cifBMbpsUniSuppressionMax,
       "hh3cifBMbpsUniSuppression": hh3cifBMbpsUniSuppression,
       "hh3cifBKbpsUniSuppressionMax": hh3cifBKbpsUniSuppressionMax,
       "hh3cifBKbpsUniSuppressionStep": hh3cifBKbpsUniSuppressionStep,
       "hh3cifBKbpsUniSuppression": hh3cifBKbpsUniSuppression,
       "hh3cifOutPayloadOctets": hh3cifOutPayloadOctets,
       "hh3cifInPayloadOctets": hh3cifInPayloadOctets,
       "hh3cifInErrorPktsRate": hh3cifInErrorPktsRate,
       "hh3cifInPkts": hh3cifInPkts,
       "hh3cifInNormalPkts": hh3cifInNormalPkts,
       "hh3cifOutPkts": hh3cifOutPkts,
       "hh3cifAggregateTable": hh3cifAggregateTable,
       "hh3cifAggregateEntry": hh3cifAggregateEntry,
       "hh3cifAggregatePortIndex": hh3cifAggregatePortIndex,
       "hh3cifAggregatePortName": hh3cifAggregatePortName,
       "hh3cifAggregatePortListPorts": hh3cifAggregatePortListPorts,
       "hh3cifAggregateModel": hh3cifAggregateModel,
       "hh3cifAggregateOperStatus": hh3cifAggregateOperStatus,
       "hh3cifHybridPortTable": hh3cifHybridPortTable,
       "hh3cifHybridPortEntry": hh3cifHybridPortEntry,
       "hh3cifHybridPortIndex": hh3cifHybridPortIndex,
       "hh3cifHybridTaggedVlanListLow": hh3cifHybridTaggedVlanListLow,
       "hh3cifHybridTaggedVlanListHigh": hh3cifHybridTaggedVlanListHigh,
       "hh3cifHybridUnTaggedVlanListLow": hh3cifHybridUnTaggedVlanListLow,
       "hh3cifHybridUnTaggedVlanListHigh": hh3cifHybridUnTaggedVlanListHigh,
       "hh3cifComboPortTable": hh3cifComboPortTable,
       "hh3cifComboPortEntry": hh3cifComboPortEntry,
       "hh3cifComboPortIndex": hh3cifComboPortIndex,
       "hh3cifComboPortCurActive": hh3cifComboPortCurActive,
       "hh3cLswL2InfMib": hh3cLswL2InfMib,
       "hh3cLswL2InfMibObject": hh3cLswL2InfMibObject,
       "hh3cSlotPortMax": hh3cSlotPortMax,
       "hh3cSwitchPortMax": hh3cSwitchPortMax,
       "hh3cifVLANTrunkStatusTable": hh3cifVLANTrunkStatusTable,
       "hh3cifVLANTrunkStatusEntry": hh3cifVLANTrunkStatusEntry,
       "hh3cifVLANTrunkIndex": hh3cifVLANTrunkIndex,
       "hh3cifVLANTrunkGvrpRegistration": hh3cifVLANTrunkGvrpRegistration,
       "hh3cifVLANTrunkPassListLow": hh3cifVLANTrunkPassListLow,
       "hh3cifVLANTrunkPassListHigh": hh3cifVLANTrunkPassListHigh,
       "hh3cifVLANTrunkAllowListLow": hh3cifVLANTrunkAllowListLow,
       "hh3cifVLANTrunkAllowListHigh": hh3cifVLANTrunkAllowListHigh,
       "hh3cethernetTable": hh3cethernetTable,
       "hh3cethernetEntry": hh3cethernetEntry,
       "hh3cifEthernetDuplex": hh3cifEthernetDuplex,
       "hh3cifEthernetMTU": hh3cifEthernetMTU,
       "hh3cifEthernetSpeed": hh3cifEthernetSpeed,
       "hh3cifEthernetMdi": hh3cifEthernetMdi,
       "hh3cMaxMacLearn": hh3cMaxMacLearn,
       "hh3cifMacAddressLearn": hh3cifMacAddressLearn,
       "hh3cifEthernetTest": hh3cifEthernetTest,
       "hh3cifMacAddrLearnMode": hh3cifMacAddrLearnMode,
       "hh3cifEthernetFlowInterval": hh3cifEthernetFlowInterval,
       "hh3cifEthernetIsolate": hh3cifEthernetIsolate,
       "hh3cifVlanVPNStatus": hh3cifVlanVPNStatus,
       "hh3cifVlanVPNUplinkStatus": hh3cifVlanVPNUplinkStatus,
       "hh3cifVlanVPNTPID": hh3cifVlanVPNTPID,
       "hh3cifIsolateGroupID": hh3cifIsolateGroupID,
       "hh3cifisUplinkPort": hh3cifisUplinkPort,
       "hh3cifEthernetAutoSpeedMask": hh3cifEthernetAutoSpeedMask,
       "hh3cifEthernetAutoSpeed": hh3cifEthernetAutoSpeed,
       "hh3cIsolateGroupMax": hh3cIsolateGroupMax,
       "hh3cGlobalBroadcastMaxPps": hh3cGlobalBroadcastMaxPps,
       "hh3cGlobalBroadcastMaxRatio": hh3cGlobalBroadcastMaxRatio,
       "hh3cBpduTunnelStatus": hh3cBpduTunnelStatus,
       "hh3cVlanVPNTPIDMode": hh3cVlanVPNTPIDMode,
       "hh3cVlanVPNTPID": hh3cVlanVPNTPID,
       "hh3cPortIsolateGroupTable": hh3cPortIsolateGroupTable,
       "hh3cPortIsolateGroupEntry": hh3cPortIsolateGroupEntry,
       "hh3cPortIsolateGroupIndex": hh3cPortIsolateGroupIndex,
       "hh3cPortIsolateUplinkIfIndex": hh3cPortIsolateUplinkIfIndex,
       "hh3cPortIsolateGroupRowStatus": hh3cPortIsolateGroupRowStatus,
       "hh3cPortIsolateGroupDescription": hh3cPortIsolateGroupDescription,
       "hh3cMaxMacLearnRange": hh3cMaxMacLearnRange}
)
