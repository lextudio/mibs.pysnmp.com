# SNMP MIB module (Wellfleet-APPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-APPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:45 2024
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

(wfAppnGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfAppnGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfAppnNode_ObjectIdentity = ObjectIdentity
wfAppnNode = _WfAppnNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1)
)
_WfAppnNodeInfoAndCaps_ObjectIdentity = ObjectIdentity
wfAppnNodeInfoAndCaps = _WfAppnNodeInfoAndCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1)
)


class _WfAppnNodeDelete_Type(Integer32):
    """Custom type wfAppnNodeDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnNodeDelete_Type.__name__ = "Integer32"
_WfAppnNodeDelete_Object = MibScalar
wfAppnNodeDelete = _WfAppnNodeDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 1),
    _WfAppnNodeDelete_Type()
)
wfAppnNodeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDelete.setStatus("mandatory")


class _WfAppnNodeDisable_Type(Integer32):
    """Custom type wfAppnNodeDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeDisable_Type.__name__ = "Integer32"
_WfAppnNodeDisable_Object = MibScalar
wfAppnNodeDisable = _WfAppnNodeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 2),
    _WfAppnNodeDisable_Type()
)
wfAppnNodeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDisable.setStatus("mandatory")


class _WfAppnNodeState_Type(Integer32):
    """Custom type wfAppnNodeState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAppnNodeState_Type.__name__ = "Integer32"
_WfAppnNodeState_Object = MibScalar
wfAppnNodeState = _WfAppnNodeState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 3),
    _WfAppnNodeState_Type()
)
wfAppnNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeState.setStatus("mandatory")
_WfAppnNodeCpName_Type = DisplayString
_WfAppnNodeCpName_Object = MibScalar
wfAppnNodeCpName = _WfAppnNodeCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 4),
    _WfAppnNodeCpName_Type()
)
wfAppnNodeCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCpName.setStatus("mandatory")
_WfAppnNodeNetid_Type = DisplayString
_WfAppnNodeNetid_Object = MibScalar
wfAppnNodeNetid = _WfAppnNodeNetid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 5),
    _WfAppnNodeNetid_Type()
)
wfAppnNodeNetid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNetid.setStatus("mandatory")
_WfAppnNodeBlockNum_Type = DisplayString
_WfAppnNodeBlockNum_Object = MibScalar
wfAppnNodeBlockNum = _WfAppnNodeBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 6),
    _WfAppnNodeBlockNum_Type()
)
wfAppnNodeBlockNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeBlockNum.setStatus("mandatory")
_WfAppnNodeIdNum_Type = DisplayString
_WfAppnNodeIdNum_Object = MibScalar
wfAppnNodeIdNum = _WfAppnNodeIdNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 7),
    _WfAppnNodeIdNum_Type()
)
wfAppnNodeIdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeIdNum.setStatus("mandatory")


class _WfAppnNodeType_Type(Integer32):
    """Custom type wfAppnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("en", 2),
          ("len", 4),
          ("nn", 1))
    )


_WfAppnNodeType_Type.__name__ = "Integer32"
_WfAppnNodeType_Object = MibScalar
wfAppnNodeType = _WfAppnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 8),
    _WfAppnNodeType_Type()
)
wfAppnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeType.setStatus("mandatory")
_WfAppnNodeUpTime_Type = Integer32
_WfAppnNodeUpTime_Object = MibScalar
wfAppnNodeUpTime = _WfAppnNodeUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 9),
    _WfAppnNodeUpTime_Type()
)
wfAppnNodeUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeUpTime.setStatus("mandatory")


class _WfAppnNodeNegotLs_Type(Integer32):
    """Custom type wfAppnNodeNegotLs based on Integer32"""
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


_WfAppnNodeNegotLs_Type.__name__ = "Integer32"
_WfAppnNodeNegotLs_Object = MibScalar
wfAppnNodeNegotLs = _WfAppnNodeNegotLs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 10),
    _WfAppnNodeNegotLs_Type()
)
wfAppnNodeNegotLs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNegotLs.setStatus("mandatory")


class _WfAppnNodeSegReasm_Type(Integer32):
    """Custom type wfAppnNodeSegReasm based on Integer32"""
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


_WfAppnNodeSegReasm_Type.__name__ = "Integer32"
_WfAppnNodeSegReasm_Object = MibScalar
wfAppnNodeSegReasm = _WfAppnNodeSegReasm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 11),
    _WfAppnNodeSegReasm_Type()
)
wfAppnNodeSegReasm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeSegReasm.setStatus("mandatory")


class _WfAppnNodeBindReasm_Type(Integer32):
    """Custom type wfAppnNodeBindReasm based on Integer32"""
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


_WfAppnNodeBindReasm_Type.__name__ = "Integer32"
_WfAppnNodeBindReasm_Object = MibScalar
wfAppnNodeBindReasm = _WfAppnNodeBindReasm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 12),
    _WfAppnNodeBindReasm_Type()
)
wfAppnNodeBindReasm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeBindReasm.setStatus("mandatory")


class _WfAppnNodeParallelTg_Type(Integer32):
    """Custom type wfAppnNodeParallelTg based on Integer32"""
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


_WfAppnNodeParallelTg_Type.__name__ = "Integer32"
_WfAppnNodeParallelTg_Object = MibScalar
wfAppnNodeParallelTg = _WfAppnNodeParallelTg_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 13),
    _WfAppnNodeParallelTg_Type()
)
wfAppnNodeParallelTg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeParallelTg.setStatus("mandatory")


class _WfAppnNodeService_Type(Integer32):
    """Custom type wfAppnNodeService based on Integer32"""
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


_WfAppnNodeService_Type.__name__ = "Integer32"
_WfAppnNodeService_Object = MibScalar
wfAppnNodeService = _WfAppnNodeService_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 14),
    _WfAppnNodeService_Type()
)
wfAppnNodeService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeService.setStatus("mandatory")


class _WfAppnNodeAdaptiveBindPacing_Type(Integer32):
    """Custom type wfAppnNodeAdaptiveBindPacing based on Integer32"""
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


_WfAppnNodeAdaptiveBindPacing_Type.__name__ = "Integer32"
_WfAppnNodeAdaptiveBindPacing_Object = MibScalar
wfAppnNodeAdaptiveBindPacing = _WfAppnNodeAdaptiveBindPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 15),
    _WfAppnNodeAdaptiveBindPacing_Type()
)
wfAppnNodeAdaptiveBindPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeAdaptiveBindPacing.setStatus("mandatory")


class _WfAppnNodeNnRcvRegChar_Type(Integer32):
    """Custom type wfAppnNodeNnRcvRegChar based on Integer32"""
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


_WfAppnNodeNnRcvRegChar_Type.__name__ = "Integer32"
_WfAppnNodeNnRcvRegChar_Object = MibScalar
wfAppnNodeNnRcvRegChar = _WfAppnNodeNnRcvRegChar_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 16),
    _WfAppnNodeNnRcvRegChar_Type()
)
wfAppnNodeNnRcvRegChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNnRcvRegChar.setStatus("mandatory")


class _WfAppnNodeNnGateway_Type(Integer32):
    """Custom type wfAppnNodeNnGateway based on Integer32"""
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


_WfAppnNodeNnGateway_Type.__name__ = "Integer32"
_WfAppnNodeNnGateway_Object = MibScalar
wfAppnNodeNnGateway = _WfAppnNodeNnGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 17),
    _WfAppnNodeNnGateway_Type()
)
wfAppnNodeNnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNnGateway.setStatus("mandatory")


class _WfAppnNodeNnCentralDirectory_Type(Integer32):
    """Custom type wfAppnNodeNnCentralDirectory based on Integer32"""
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


_WfAppnNodeNnCentralDirectory_Type.__name__ = "Integer32"
_WfAppnNodeNnCentralDirectory_Object = MibScalar
wfAppnNodeNnCentralDirectory = _WfAppnNodeNnCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 18),
    _WfAppnNodeNnCentralDirectory_Type()
)
wfAppnNodeNnCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNnCentralDirectory.setStatus("mandatory")


class _WfAppnNodeNnTreeCache_Type(Integer32):
    """Custom type wfAppnNodeNnTreeCache based on Integer32"""
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


_WfAppnNodeNnTreeCache_Type.__name__ = "Integer32"
_WfAppnNodeNnTreeCache_Object = MibScalar
wfAppnNodeNnTreeCache = _WfAppnNodeNnTreeCache_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 19),
    _WfAppnNodeNnTreeCache_Type()
)
wfAppnNodeNnTreeCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNnTreeCache.setStatus("mandatory")


class _WfAppnNodeNnTreeUpdate_Type(Integer32):
    """Custom type wfAppnNodeNnTreeUpdate based on Integer32"""
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


_WfAppnNodeNnTreeUpdate_Type.__name__ = "Integer32"
_WfAppnNodeNnTreeUpdate_Object = MibScalar
wfAppnNodeNnTreeUpdate = _WfAppnNodeNnTreeUpdate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 20),
    _WfAppnNodeNnTreeUpdate_Type()
)
wfAppnNodeNnTreeUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNnTreeUpdate.setStatus("mandatory")


class _WfAppnNodeNnRouteAddResist_Type(Integer32):
    """Custom type wfAppnNodeNnRouteAddResist based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeNnRouteAddResist_Type.__name__ = "Integer32"
_WfAppnNodeNnRouteAddResist_Object = MibScalar
wfAppnNodeNnRouteAddResist = _WfAppnNodeNnRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 21),
    _WfAppnNodeNnRouteAddResist_Type()
)
wfAppnNodeNnRouteAddResist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnRouteAddResist.setStatus("mandatory")


class _WfAppnNodeNnIsr_Type(Integer32):
    """Custom type wfAppnNodeNnIsr based on Integer32"""
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


_WfAppnNodeNnIsr_Type.__name__ = "Integer32"
_WfAppnNodeNnIsr_Object = MibScalar
wfAppnNodeNnIsr = _WfAppnNodeNnIsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 22),
    _WfAppnNodeNnIsr_Type()
)
wfAppnNodeNnIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNnIsr.setStatus("mandatory")
_WfAppnNodeNnFrsn_Type = Integer32
_WfAppnNodeNnFrsn_Object = MibScalar
wfAppnNodeNnFrsn = _WfAppnNodeNnFrsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 23),
    _WfAppnNodeNnFrsn_Type()
)
wfAppnNodeNnFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeNnFrsn.setStatus("mandatory")


class _WfAppnNodeModeToCosDisable_Type(Integer32):
    """Custom type wfAppnNodeModeToCosDisable based on Integer32"""
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


_WfAppnNodeModeToCosDisable_Type.__name__ = "Integer32"
_WfAppnNodeModeToCosDisable_Object = MibScalar
wfAppnNodeModeToCosDisable = _WfAppnNodeModeToCosDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 24),
    _WfAppnNodeModeToCosDisable_Type()
)
wfAppnNodeModeToCosDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeModeToCosDisable.setStatus("mandatory")


class _WfAppnNodeMdsDisable_Type(Integer32):
    """Custom type wfAppnNodeMdsDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeMdsDisable_Type.__name__ = "Integer32"
_WfAppnNodeMdsDisable_Object = MibScalar
wfAppnNodeMdsDisable = _WfAppnNodeMdsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 25),
    _WfAppnNodeMdsDisable_Type()
)
wfAppnNodeMdsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeMdsDisable.setStatus("mandatory")


class _WfAppnNodeRegWithCdsDisable_Type(Integer32):
    """Custom type wfAppnNodeRegWithCdsDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeRegWithCdsDisable_Type.__name__ = "Integer32"
_WfAppnNodeRegWithCdsDisable_Object = MibScalar
wfAppnNodeRegWithCdsDisable = _WfAppnNodeRegWithCdsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 26),
    _WfAppnNodeRegWithCdsDisable_Type()
)
wfAppnNodeRegWithCdsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeRegWithCdsDisable.setStatus("mandatory")


class _WfAppnNodeAlertQSize_Type(Integer32):
    """Custom type wfAppnNodeAlertQSize based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 2147483647),
    )


_WfAppnNodeAlertQSize_Type.__name__ = "Integer32"
_WfAppnNodeAlertQSize_Object = MibScalar
wfAppnNodeAlertQSize = _WfAppnNodeAlertQSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 27),
    _WfAppnNodeAlertQSize_Type()
)
wfAppnNodeAlertQSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeAlertQSize.setStatus("mandatory")


class _WfAppnNodeCosCacheSize_Type(Integer32):
    """Custom type wfAppnNodeCosCacheSize based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2147483647),
    )


_WfAppnNodeCosCacheSize_Type.__name__ = "Integer32"
_WfAppnNodeCosCacheSize_Object = MibScalar
wfAppnNodeCosCacheSize = _WfAppnNodeCosCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 28),
    _WfAppnNodeCosCacheSize_Type()
)
wfAppnNodeCosCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCosCacheSize.setStatus("mandatory")


class _WfAppnNodeStoreEndpointRscvsDisable_Type(Integer32):
    """Custom type wfAppnNodeStoreEndpointRscvsDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeStoreEndpointRscvsDisable_Type.__name__ = "Integer32"
_WfAppnNodeStoreEndpointRscvsDisable_Object = MibScalar
wfAppnNodeStoreEndpointRscvsDisable = _WfAppnNodeStoreEndpointRscvsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 29),
    _WfAppnNodeStoreEndpointRscvsDisable_Type()
)
wfAppnNodeStoreEndpointRscvsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeStoreEndpointRscvsDisable.setStatus("mandatory")


class _WfAppnNodeNnMaxLocates_Type(Integer32):
    """Custom type wfAppnNodeNnMaxLocates based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2147483647),
    )


_WfAppnNodeNnMaxLocates_Type.__name__ = "Integer32"
_WfAppnNodeNnMaxLocates_Object = MibScalar
wfAppnNodeNnMaxLocates = _WfAppnNodeNnMaxLocates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 30),
    _WfAppnNodeNnMaxLocates_Type()
)
wfAppnNodeNnMaxLocates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnMaxLocates.setStatus("mandatory")


class _WfAppnNodeNnDirCacheSize_Type(Integer32):
    """Custom type wfAppnNodeNnDirCacheSize based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("def", 100)
    )


_WfAppnNodeNnDirCacheSize_Type.__name__ = "Integer32"
_WfAppnNodeNnDirCacheSize_Object = MibScalar
wfAppnNodeNnDirCacheSize = _WfAppnNodeNnDirCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 31),
    _WfAppnNodeNnDirCacheSize_Type()
)
wfAppnNodeNnDirCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnDirCacheSize.setStatus("mandatory")
_WfAppnNodeNnMaxDirEntries_Type = Integer32
_WfAppnNodeNnMaxDirEntries_Object = MibScalar
wfAppnNodeNnMaxDirEntries = _WfAppnNodeNnMaxDirEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 32),
    _WfAppnNodeNnMaxDirEntries_Type()
)
wfAppnNodeNnMaxDirEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnMaxDirEntries.setStatus("mandatory")


class _WfAppnNodeNnLocateTimeout_Type(Integer32):
    """Custom type wfAppnNodeNnLocateTimeout based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            60
        )
    )
    namedValues = NamedValues(
        ("def", 60)
    )


_WfAppnNodeNnLocateTimeout_Type.__name__ = "Integer32"
_WfAppnNodeNnLocateTimeout_Object = MibScalar
wfAppnNodeNnLocateTimeout = _WfAppnNodeNnLocateTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 33),
    _WfAppnNodeNnLocateTimeout_Type()
)
wfAppnNodeNnLocateTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnLocateTimeout.setStatus("mandatory")


class _WfAppnNodeNnTreeCacheSize_Type(Integer32):
    """Custom type wfAppnNodeNnTreeCacheSize based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 2147483647),
    )


_WfAppnNodeNnTreeCacheSize_Type.__name__ = "Integer32"
_WfAppnNodeNnTreeCacheSize_Object = MibScalar
wfAppnNodeNnTreeCacheSize = _WfAppnNodeNnTreeCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 34),
    _WfAppnNodeNnTreeCacheSize_Type()
)
wfAppnNodeNnTreeCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnTreeCacheSize.setStatus("mandatory")


class _WfAppnNodeNnTreeCacheUseLimit_Type(Integer32):
    """Custom type wfAppnNodeNnTreeCacheUseLimit based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfAppnNodeNnTreeCacheUseLimit_Type.__name__ = "Integer32"
_WfAppnNodeNnTreeCacheUseLimit_Object = MibScalar
wfAppnNodeNnTreeCacheUseLimit = _WfAppnNodeNnTreeCacheUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 35),
    _WfAppnNodeNnTreeCacheUseLimit_Type()
)
wfAppnNodeNnTreeCacheUseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnTreeCacheUseLimit.setStatus("mandatory")
_WfAppnNodeNnMaxTdmNodes_Type = Integer32
_WfAppnNodeNnMaxTdmNodes_Object = MibScalar
wfAppnNodeNnMaxTdmNodes = _WfAppnNodeNnMaxTdmNodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 36),
    _WfAppnNodeNnMaxTdmNodes_Type()
)
wfAppnNodeNnMaxTdmNodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnMaxTdmNodes.setStatus("mandatory")
_WfAppnNodeNnMaxTdmTgs_Type = Integer32
_WfAppnNodeNnMaxTdmTgs_Object = MibScalar
wfAppnNodeNnMaxTdmTgs = _WfAppnNodeNnMaxTdmTgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 37),
    _WfAppnNodeNnMaxTdmTgs_Type()
)
wfAppnNodeNnMaxTdmTgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnMaxTdmTgs.setStatus("mandatory")


class _WfAppnNodeNnMaxIsrSessions_Type(Integer32):
    """Custom type wfAppnNodeNnMaxIsrSessions based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 2147483647),
    )


_WfAppnNodeNnMaxIsrSessions_Type.__name__ = "Integer32"
_WfAppnNodeNnMaxIsrSessions_Object = MibScalar
wfAppnNodeNnMaxIsrSessions = _WfAppnNodeNnMaxIsrSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 38),
    _WfAppnNodeNnMaxIsrSessions_Type()
)
wfAppnNodeNnMaxIsrSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnMaxIsrSessions.setStatus("mandatory")


class _WfAppnNodeNnIsrSessionUpperThresh_Type(Integer32):
    """Custom type wfAppnNodeNnIsrSessionUpperThresh based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            900
        )
    )
    namedValues = NamedValues(
        ("def", 900)
    )


_WfAppnNodeNnIsrSessionUpperThresh_Type.__name__ = "Integer32"
_WfAppnNodeNnIsrSessionUpperThresh_Object = MibScalar
wfAppnNodeNnIsrSessionUpperThresh = _WfAppnNodeNnIsrSessionUpperThresh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 39),
    _WfAppnNodeNnIsrSessionUpperThresh_Type()
)
wfAppnNodeNnIsrSessionUpperThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnIsrSessionUpperThresh.setStatus("mandatory")


class _WfAppnNodeNnIsrSessionLowerThresh_Type(Integer32):
    """Custom type wfAppnNodeNnIsrSessionLowerThresh based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            800
        )
    )
    namedValues = NamedValues(
        ("def", 800)
    )


_WfAppnNodeNnIsrSessionLowerThresh_Type.__name__ = "Integer32"
_WfAppnNodeNnIsrSessionLowerThresh_Object = MibScalar
wfAppnNodeNnIsrSessionLowerThresh = _WfAppnNodeNnIsrSessionLowerThresh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 40),
    _WfAppnNodeNnIsrSessionLowerThresh_Type()
)
wfAppnNodeNnIsrSessionLowerThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnIsrSessionLowerThresh.setStatus("mandatory")


class _WfAppnNodeNnIsrMaxRuSize_Type(Integer32):
    """Custom type wfAppnNodeNnIsrMaxRuSize based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4096),
    )


_WfAppnNodeNnIsrMaxRuSize_Type.__name__ = "Integer32"
_WfAppnNodeNnIsrMaxRuSize_Object = MibScalar
wfAppnNodeNnIsrMaxRuSize = _WfAppnNodeNnIsrMaxRuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 41),
    _WfAppnNodeNnIsrMaxRuSize_Type()
)
wfAppnNodeNnIsrMaxRuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnIsrMaxRuSize.setStatus("mandatory")


class _WfAppnNodeNnIsrRcvPacingWindow_Type(Integer32):
    """Custom type wfAppnNodeNnIsrRcvPacingWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfAppnNodeNnIsrRcvPacingWindow_Type.__name__ = "Integer32"
_WfAppnNodeNnIsrRcvPacingWindow_Object = MibScalar
wfAppnNodeNnIsrRcvPacingWindow = _WfAppnNodeNnIsrRcvPacingWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 42),
    _WfAppnNodeNnIsrRcvPacingWindow_Type()
)
wfAppnNodeNnIsrRcvPacingWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnIsrRcvPacingWindow.setStatus("mandatory")


class _WfAppnNodeNnStoreIsrRscvsDisable_Type(Integer32):
    """Custom type wfAppnNodeNnStoreIsrRscvsDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeNnStoreIsrRscvsDisable_Type.__name__ = "Integer32"
_WfAppnNodeNnStoreIsrRscvsDisable_Object = MibScalar
wfAppnNodeNnStoreIsrRscvsDisable = _WfAppnNodeNnStoreIsrRscvsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 43),
    _WfAppnNodeNnStoreIsrRscvsDisable_Type()
)
wfAppnNodeNnStoreIsrRscvsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnStoreIsrRscvsDisable.setStatus("mandatory")


class _WfAppnNodeNnStoreDlurRscvsDisable_Type(Integer32):
    """Custom type wfAppnNodeNnStoreDlurRscvsDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeNnStoreDlurRscvsDisable_Type.__name__ = "Integer32"
_WfAppnNodeNnStoreDlurRscvsDisable_Object = MibScalar
wfAppnNodeNnStoreDlurRscvsDisable = _WfAppnNodeNnStoreDlurRscvsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 44),
    _WfAppnNodeNnStoreDlurRscvsDisable_Type()
)
wfAppnNodeNnStoreDlurRscvsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnStoreDlurRscvsDisable.setStatus("mandatory")


class _WfAppnNodeNnDlurDisable_Type(Integer32):
    """Custom type wfAppnNodeNnDlurDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeNnDlurDisable_Type.__name__ = "Integer32"
_WfAppnNodeNnDlurDisable_Object = MibScalar
wfAppnNodeNnDlurDisable = _WfAppnNodeNnDlurDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 45),
    _WfAppnNodeNnDlurDisable_Type()
)
wfAppnNodeNnDlurDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeNnDlurDisable.setStatus("mandatory")
_WfAppnNodeTotalAvailableMemory_Type = Integer32
_WfAppnNodeTotalAvailableMemory_Object = MibScalar
wfAppnNodeTotalAvailableMemory = _WfAppnNodeTotalAvailableMemory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 46),
    _WfAppnNodeTotalAvailableMemory_Type()
)
wfAppnNodeTotalAvailableMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeTotalAvailableMemory.setStatus("mandatory")
_WfAppnNodeInUseMemory_Type = Integer32
_WfAppnNodeInUseMemory_Object = MibScalar
wfAppnNodeInUseMemory = _WfAppnNodeInUseMemory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 47),
    _WfAppnNodeInUseMemory_Type()
)
wfAppnNodeInUseMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeInUseMemory.setStatus("mandatory")
_WfAppnNodeMemoryWarningThreshold_Type = Integer32
_WfAppnNodeMemoryWarningThreshold_Object = MibScalar
wfAppnNodeMemoryWarningThreshold = _WfAppnNodeMemoryWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 48),
    _WfAppnNodeMemoryWarningThreshold_Type()
)
wfAppnNodeMemoryWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeMemoryWarningThreshold.setStatus("mandatory")
_WfAppnNodeMemoryCriticalThreshold_Type = Integer32
_WfAppnNodeMemoryCriticalThreshold_Object = MibScalar
wfAppnNodeMemoryCriticalThreshold = _WfAppnNodeMemoryCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 49),
    _WfAppnNodeMemoryCriticalThreshold_Type()
)
wfAppnNodeMemoryCriticalThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeMemoryCriticalThreshold.setStatus("mandatory")


class _WfAppnNodeHprDisable_Type(Integer32):
    """Custom type wfAppnNodeHprDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeHprDisable_Type.__name__ = "Integer32"
_WfAppnNodeHprDisable_Object = MibScalar
wfAppnNodeHprDisable = _WfAppnNodeHprDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 50),
    _WfAppnNodeHprDisable_Type()
)
wfAppnNodeHprDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeHprDisable.setStatus("mandatory")


class _WfAppnNodeHprPathSwitchCtrlrDisable_Type(Integer32):
    """Custom type wfAppnNodeHprPathSwitchCtrlrDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeHprPathSwitchCtrlrDisable_Type.__name__ = "Integer32"
_WfAppnNodeHprPathSwitchCtrlrDisable_Object = MibScalar
wfAppnNodeHprPathSwitchCtrlrDisable = _WfAppnNodeHprPathSwitchCtrlrDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 51),
    _WfAppnNodeHprPathSwitchCtrlrDisable_Type()
)
wfAppnNodeHprPathSwitchCtrlrDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeHprPathSwitchCtrlrDisable.setStatus("mandatory")


class _WfAppnNodeDebugIpsTraceDisable_Type(Integer32):
    """Custom type wfAppnNodeDebugIpsTraceDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeDebugIpsTraceDisable_Type.__name__ = "Integer32"
_WfAppnNodeDebugIpsTraceDisable_Object = MibScalar
wfAppnNodeDebugIpsTraceDisable = _WfAppnNodeDebugIpsTraceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 52),
    _WfAppnNodeDebugIpsTraceDisable_Type()
)
wfAppnNodeDebugIpsTraceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDebugIpsTraceDisable.setStatus("mandatory")


class _WfAppnNodeDebugIpsTraceSize_Type(Integer32):
    """Custom type wfAppnNodeDebugIpsTraceSize based on Integer32"""
    defaultValue = 50000


_WfAppnNodeDebugIpsTraceSize_Object = MibScalar
wfAppnNodeDebugIpsTraceSize = _WfAppnNodeDebugIpsTraceSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 53),
    _WfAppnNodeDebugIpsTraceSize_Type()
)
wfAppnNodeDebugIpsTraceSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDebugIpsTraceSize.setStatus("mandatory")
_WfAppnNodeDefaultDlusName_Type = DisplayString
_WfAppnNodeDefaultDlusName_Object = MibScalar
wfAppnNodeDefaultDlusName = _WfAppnNodeDefaultDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 54),
    _WfAppnNodeDefaultDlusName_Type()
)
wfAppnNodeDefaultDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDefaultDlusName.setStatus("mandatory")
_WfAppnNodeDefaultBackupDlusName_Type = DisplayString
_WfAppnNodeDefaultBackupDlusName_Object = MibScalar
wfAppnNodeDefaultBackupDlusName = _WfAppnNodeDefaultBackupDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 55),
    _WfAppnNodeDefaultBackupDlusName_Type()
)
wfAppnNodeDefaultBackupDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDefaultBackupDlusName.setStatus("mandatory")


class _WfAppnNodePdLogDisable_Type(Integer32):
    """Custom type wfAppnNodePdLogDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodePdLogDisable_Type.__name__ = "Integer32"
_WfAppnNodePdLogDisable_Object = MibScalar
wfAppnNodePdLogDisable = _WfAppnNodePdLogDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 56),
    _WfAppnNodePdLogDisable_Type()
)
wfAppnNodePdLogDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePdLogDisable.setStatus("mandatory")


class _WfAppnNodeDlusRetryTimeout_Type(Integer32):
    """Custom type wfAppnNodeDlusRetryTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 90),
    )


_WfAppnNodeDlusRetryTimeout_Type.__name__ = "Integer32"
_WfAppnNodeDlusRetryTimeout_Object = MibScalar
wfAppnNodeDlusRetryTimeout = _WfAppnNodeDlusRetryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 57),
    _WfAppnNodeDlusRetryTimeout_Type()
)
wfAppnNodeDlusRetryTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlusRetryTimeout.setStatus("mandatory")


class _WfAppnNodeDlusRetryLimit_Type(Integer32):
    """Custom type wfAppnNodeDlusRetryLimit based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_WfAppnNodeDlusRetryLimit_Type.__name__ = "Integer32"
_WfAppnNodeDlusRetryLimit_Object = MibScalar
wfAppnNodeDlusRetryLimit = _WfAppnNodeDlusRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 58),
    _WfAppnNodeDlusRetryLimit_Type()
)
wfAppnNodeDlusRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlusRetryLimit.setStatus("mandatory")


class _WfAppnNodeSoloistSlotNum_Type(Integer32):
    """Custom type wfAppnNodeSoloistSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfAppnNodeSoloistSlotNum_Type.__name__ = "Integer32"
_WfAppnNodeSoloistSlotNum_Object = MibScalar
wfAppnNodeSoloistSlotNum = _WfAppnNodeSoloistSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 59),
    _WfAppnNodeSoloistSlotNum_Type()
)
wfAppnNodeSoloistSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeSoloistSlotNum.setStatus("mandatory")


class _WfAppnNodeBrNNSupport_Type(Integer32):
    """Custom type wfAppnNodeBrNNSupport based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeBrNNSupport_Type.__name__ = "Integer32"
_WfAppnNodeBrNNSupport_Object = MibScalar
wfAppnNodeBrNNSupport = _WfAppnNodeBrNNSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 60),
    _WfAppnNodeBrNNSupport_Type()
)
wfAppnNodeBrNNSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeBrNNSupport.setStatus("mandatory")


class _WfAppnNodeRegisterWithNN_Type(Integer32):
    """Custom type wfAppnNodeRegisterWithNN based on Integer32"""
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
        *(("all", 2),
          ("local", 3),
          ("none", 1))
    )


_WfAppnNodeRegisterWithNN_Type.__name__ = "Integer32"
_WfAppnNodeRegisterWithNN_Object = MibScalar
wfAppnNodeRegisterWithNN = _WfAppnNodeRegisterWithNN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 61),
    _WfAppnNodeRegisterWithNN_Type()
)
wfAppnNodeRegisterWithNN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeRegisterWithNN.setStatus("mandatory")


class _WfAppnNodeBranchAwarenessEnable_Type(Integer32):
    """Custom type wfAppnNodeBranchAwarenessEnable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeBranchAwarenessEnable_Type.__name__ = "Integer32"
_WfAppnNodeBranchAwarenessEnable_Object = MibScalar
wfAppnNodeBranchAwarenessEnable = _WfAppnNodeBranchAwarenessEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 1, 62),
    _WfAppnNodeBranchAwarenessEnable_Type()
)
wfAppnNodeBranchAwarenessEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeBranchAwarenessEnable.setStatus("mandatory")
_WfAppnNodeDlcTable_Object = MibTable
wfAppnNodeDlcTable = _WfAppnNodeDlcTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2)
)
if mibBuilder.loadTexts:
    wfAppnNodeDlcTable.setStatus("mandatory")
_WfAppnNodeDlcEntry_Object = MibTableRow
wfAppnNodeDlcEntry = _WfAppnNodeDlcEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1)
)
wfAppnNodeDlcEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeDlcName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeDlcEntry.setStatus("mandatory")


class _WfAppnNodeDlcDelete_Type(Integer32):
    """Custom type wfAppnNodeDlcDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnNodeDlcDelete_Type.__name__ = "Integer32"
_WfAppnNodeDlcDelete_Object = MibTableColumn
wfAppnNodeDlcDelete = _WfAppnNodeDlcDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 1),
    _WfAppnNodeDlcDelete_Type()
)
wfAppnNodeDlcDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlcDelete.setStatus("mandatory")


class _WfAppnNodeDlcDisable_Type(Integer32):
    """Custom type wfAppnNodeDlcDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeDlcDisable_Type.__name__ = "Integer32"
_WfAppnNodeDlcDisable_Object = MibTableColumn
wfAppnNodeDlcDisable = _WfAppnNodeDlcDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 2),
    _WfAppnNodeDlcDisable_Type()
)
wfAppnNodeDlcDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlcDisable.setStatus("mandatory")
_WfAppnNodeDlcName_Type = DisplayString
_WfAppnNodeDlcName_Object = MibTableColumn
wfAppnNodeDlcName = _WfAppnNodeDlcName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 3),
    _WfAppnNodeDlcName_Type()
)
wfAppnNodeDlcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeDlcName.setStatus("mandatory")


class _WfAppnNodeDlcState_Type(Integer32):
    """Custom type wfAppnNodeDlcState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_WfAppnNodeDlcState_Type.__name__ = "Integer32"
_WfAppnNodeDlcState_Object = MibTableColumn
wfAppnNodeDlcState = _WfAppnNodeDlcState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 4),
    _WfAppnNodeDlcState_Type()
)
wfAppnNodeDlcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeDlcState.setStatus("mandatory")


class _WfAppnNodeDlcType_Type(Integer32):
    """Custom type wfAppnNodeDlcType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dls", 5),
          ("fr", 4),
          ("qllc", 6),
          ("sdlc", 1),
          ("srb", 2),
          ("tb", 3))
    )


_WfAppnNodeDlcType_Type.__name__ = "Integer32"
_WfAppnNodeDlcType_Object = MibTableColumn
wfAppnNodeDlcType = _WfAppnNodeDlcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 5),
    _WfAppnNodeDlcType_Type()
)
wfAppnNodeDlcType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlcType.setStatus("mandatory")


class _WfAppnNodeDlcNegLsSupportDisable_Type(Integer32):
    """Custom type wfAppnNodeDlcNegLsSupportDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeDlcNegLsSupportDisable_Type.__name__ = "Integer32"
_WfAppnNodeDlcNegLsSupportDisable_Object = MibTableColumn
wfAppnNodeDlcNegLsSupportDisable = _WfAppnNodeDlcNegLsSupportDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 6),
    _WfAppnNodeDlcNegLsSupportDisable_Type()
)
wfAppnNodeDlcNegLsSupportDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlcNegLsSupportDisable.setStatus("mandatory")
_WfAppnNodeDlcCct_Type = Integer32
_WfAppnNodeDlcCct_Object = MibTableColumn
wfAppnNodeDlcCct = _WfAppnNodeDlcCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 7),
    _WfAppnNodeDlcCct_Type()
)
wfAppnNodeDlcCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlcCct.setStatus("mandatory")
_WfAppnNodeDlcData_Type = OctetString
_WfAppnNodeDlcData_Object = MibTableColumn
wfAppnNodeDlcData = _WfAppnNodeDlcData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 2, 1, 8),
    _WfAppnNodeDlcData_Type()
)
wfAppnNodeDlcData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeDlcData.setStatus("mandatory")
_WfAppnNodePortTable_Object = MibTable
wfAppnNodePortTable = _WfAppnNodePortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3)
)
if mibBuilder.loadTexts:
    wfAppnNodePortTable.setStatus("mandatory")
_WfAppnNodePortEntry_Object = MibTableRow
wfAppnNodePortEntry = _WfAppnNodePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1)
)
wfAppnNodePortEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodePortName"),
)
if mibBuilder.loadTexts:
    wfAppnNodePortEntry.setStatus("mandatory")


class _WfAppnNodePortDelete_Type(Integer32):
    """Custom type wfAppnNodePortDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnNodePortDelete_Type.__name__ = "Integer32"
_WfAppnNodePortDelete_Object = MibTableColumn
wfAppnNodePortDelete = _WfAppnNodePortDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 1),
    _WfAppnNodePortDelete_Type()
)
wfAppnNodePortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortDelete.setStatus("mandatory")


class _WfAppnNodePortDisable_Type(Integer32):
    """Custom type wfAppnNodePortDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodePortDisable_Type.__name__ = "Integer32"
_WfAppnNodePortDisable_Object = MibTableColumn
wfAppnNodePortDisable = _WfAppnNodePortDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 2),
    _WfAppnNodePortDisable_Type()
)
wfAppnNodePortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortDisable.setStatus("mandatory")
_WfAppnNodePortName_Type = DisplayString
_WfAppnNodePortName_Object = MibTableColumn
wfAppnNodePortName = _WfAppnNodePortName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 3),
    _WfAppnNodePortName_Type()
)
wfAppnNodePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortName.setStatus("mandatory")


class _WfAppnNodePortState_Type(Integer32):
    """Custom type wfAppnNodePortState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_WfAppnNodePortState_Type.__name__ = "Integer32"
_WfAppnNodePortState_Object = MibTableColumn
wfAppnNodePortState = _WfAppnNodePortState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 4),
    _WfAppnNodePortState_Type()
)
wfAppnNodePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortState.setStatus("mandatory")


class _WfAppnNodePortDlcType_Type(Integer32):
    """Custom type wfAppnNodePortDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenring", 6))
    )


_WfAppnNodePortDlcType_Type.__name__ = "Integer32"
_WfAppnNodePortDlcType_Object = MibTableColumn
wfAppnNodePortDlcType = _WfAppnNodePortDlcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 5),
    _WfAppnNodePortDlcType_Type()
)
wfAppnNodePortDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortDlcType.setStatus("mandatory")


class _WfAppnNodePortPortType_Type(Integer32):
    """Custom type wfAppnNodePortPortType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fac", 3),
          ("leased", 1),
          ("switched", 2))
    )


_WfAppnNodePortPortType_Type.__name__ = "Integer32"
_WfAppnNodePortPortType_Object = MibTableColumn
wfAppnNodePortPortType = _WfAppnNodePortPortType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 6),
    _WfAppnNodePortPortType_Type()
)
wfAppnNodePortPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortPortType.setStatus("mandatory")


class _WfAppnNodePortSIMRIM_Type(Integer32):
    """Custom type wfAppnNodePortSIMRIM based on Integer32"""
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


_WfAppnNodePortSIMRIM_Type.__name__ = "Integer32"
_WfAppnNodePortSIMRIM_Object = MibTableColumn
wfAppnNodePortSIMRIM = _WfAppnNodePortSIMRIM_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 7),
    _WfAppnNodePortSIMRIM_Type()
)
wfAppnNodePortSIMRIM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortSIMRIM.setStatus("mandatory")


class _WfAppnNodePortLsRole_Type(Integer32):
    """Custom type wfAppnNodePortLsRole based on Integer32"""
    defaultValue = 3

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
        *(("abm", 4),
          ("negot", 3),
          ("primary", 1),
          ("secondary", 2))
    )


_WfAppnNodePortLsRole_Type.__name__ = "Integer32"
_WfAppnNodePortLsRole_Object = MibTableColumn
wfAppnNodePortLsRole = _WfAppnNodePortLsRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 8),
    _WfAppnNodePortLsRole_Type()
)
wfAppnNodePortLsRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortLsRole.setStatus("mandatory")


class _WfAppnNodePortMaxRcvBtuSize_Type(Integer32):
    """Custom type wfAppnNodePortMaxRcvBtuSize based on Integer32"""
    defaultValue = 1470

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4105),
    )


_WfAppnNodePortMaxRcvBtuSize_Type.__name__ = "Integer32"
_WfAppnNodePortMaxRcvBtuSize_Object = MibTableColumn
wfAppnNodePortMaxRcvBtuSize = _WfAppnNodePortMaxRcvBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 9),
    _WfAppnNodePortMaxRcvBtuSize_Type()
)
wfAppnNodePortMaxRcvBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortMaxRcvBtuSize.setStatus("mandatory")


class _WfAppnNodePortMaxIframeWindow_Type(Integer32):
    """Custom type wfAppnNodePortMaxIframeWindow based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfAppnNodePortMaxIframeWindow_Type.__name__ = "Integer32"
_WfAppnNodePortMaxIframeWindow_Object = MibTableColumn
wfAppnNodePortMaxIframeWindow = _WfAppnNodePortMaxIframeWindow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 10),
    _WfAppnNodePortMaxIframeWindow_Type()
)
wfAppnNodePortMaxIframeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortMaxIframeWindow.setStatus("mandatory")
_WfAppnNodePortDefLsGoodXids_Type = Counter32
_WfAppnNodePortDefLsGoodXids_Object = MibTableColumn
wfAppnNodePortDefLsGoodXids = _WfAppnNodePortDefLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 11),
    _WfAppnNodePortDefLsGoodXids_Type()
)
wfAppnNodePortDefLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortDefLsGoodXids.setStatus("mandatory")
_WfAppnNodePortDefLsBadXids_Type = Counter32
_WfAppnNodePortDefLsBadXids_Object = MibTableColumn
wfAppnNodePortDefLsBadXids = _WfAppnNodePortDefLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 12),
    _WfAppnNodePortDefLsBadXids_Type()
)
wfAppnNodePortDefLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortDefLsBadXids.setStatus("mandatory")
_WfAppnNodePortDynLsGoodXids_Type = Counter32
_WfAppnNodePortDynLsGoodXids_Object = MibTableColumn
wfAppnNodePortDynLsGoodXids = _WfAppnNodePortDynLsGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 13),
    _WfAppnNodePortDynLsGoodXids_Type()
)
wfAppnNodePortDynLsGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortDynLsGoodXids.setStatus("mandatory")
_WfAppnNodePortDynLsBadXids_Type = Counter32
_WfAppnNodePortDynLsBadXids_Object = MibTableColumn
wfAppnNodePortDynLsBadXids = _WfAppnNodePortDynLsBadXids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 14),
    _WfAppnNodePortDynLsBadXids_Type()
)
wfAppnNodePortDynLsBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodePortDynLsBadXids.setStatus("mandatory")
_WfAppnNodePortDlcName_Type = DisplayString
_WfAppnNodePortDlcName_Object = MibTableColumn
wfAppnNodePortDlcName = _WfAppnNodePortDlcName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 15),
    _WfAppnNodePortDlcName_Type()
)
wfAppnNodePortDlcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortDlcName.setStatus("mandatory")
_WfAppnNodePortNumber_Type = Integer32
_WfAppnNodePortNumber_Object = MibTableColumn
wfAppnNodePortNumber = _WfAppnNodePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 16),
    _WfAppnNodePortNumber_Type()
)
wfAppnNodePortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortNumber.setStatus("mandatory")


class _WfAppnNodePortTotLinkActLim_Type(Integer32):
    """Custom type wfAppnNodePortTotLinkActLim based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              256)
        )
    )
    namedValues = NamedValues(
        *(("neg", 1),
          ("pri", 256))
    )


_WfAppnNodePortTotLinkActLim_Type.__name__ = "Integer32"
_WfAppnNodePortTotLinkActLim_Object = MibTableColumn
wfAppnNodePortTotLinkActLim = _WfAppnNodePortTotLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 17),
    _WfAppnNodePortTotLinkActLim_Type()
)
wfAppnNodePortTotLinkActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortTotLinkActLim.setStatus("mandatory")


class _WfAppnNodePortInbLinkActLim_Type(Integer32):
    """Custom type wfAppnNodePortInbLinkActLim based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              128)
        )
    )
    namedValues = NamedValues(
        *(("satf", 128),
          ("sec", 1))
    )


_WfAppnNodePortInbLinkActLim_Type.__name__ = "Integer32"
_WfAppnNodePortInbLinkActLim_Object = MibTableColumn
wfAppnNodePortInbLinkActLim = _WfAppnNodePortInbLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 18),
    _WfAppnNodePortInbLinkActLim_Type()
)
wfAppnNodePortInbLinkActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortInbLinkActLim.setStatus("mandatory")


class _WfAppnNodePortOutLinkActLim_Type(Integer32):
    """Custom type wfAppnNodePortOutLinkActLim based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              128,
              256)
        )
    )
    namedValues = NamedValues(
        *(("pri", 256),
          ("satf", 128),
          ("switched", 1))
    )


_WfAppnNodePortOutLinkActLim_Type.__name__ = "Integer32"
_WfAppnNodePortOutLinkActLim_Object = MibTableColumn
wfAppnNodePortOutLinkActLim = _WfAppnNodePortOutLinkActLim_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 19),
    _WfAppnNodePortOutLinkActLim_Type()
)
wfAppnNodePortOutLinkActLim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortOutLinkActLim.setStatus("mandatory")


class _WfAppnNodePortActXidExchangeLimit_Type(Integer32):
    """Custom type wfAppnNodePortActXidExchangeLimit based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            12
        )
    )
    namedValues = NamedValues(
        ("def", 12)
    )


_WfAppnNodePortActXidExchangeLimit_Type.__name__ = "Integer32"
_WfAppnNodePortActXidExchangeLimit_Object = MibTableColumn
wfAppnNodePortActXidExchangeLimit = _WfAppnNodePortActXidExchangeLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 20),
    _WfAppnNodePortActXidExchangeLimit_Type()
)
wfAppnNodePortActXidExchangeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortActXidExchangeLimit.setStatus("mandatory")


class _WfAppnNodePortNonActXidExchangeLimit_Type(Integer32):
    """Custom type wfAppnNodePortNonActXidExchangeLimit based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("def", 5)
    )


_WfAppnNodePortNonActXidExchangeLimit_Type.__name__ = "Integer32"
_WfAppnNodePortNonActXidExchangeLimit_Object = MibTableColumn
wfAppnNodePortNonActXidExchangeLimit = _WfAppnNodePortNonActXidExchangeLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 21),
    _WfAppnNodePortNonActXidExchangeLimit_Type()
)
wfAppnNodePortNonActXidExchangeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortNonActXidExchangeLimit.setStatus("mandatory")


class _WfAppnNodePortLsXmitRcvCap_Type(Integer32):
    """Custom type wfAppnNodePortLsXmitRcvCap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("twa", 2),
          ("tws", 1))
    )


_WfAppnNodePortLsXmitRcvCap_Type.__name__ = "Integer32"
_WfAppnNodePortLsXmitRcvCap_Object = MibTableColumn
wfAppnNodePortLsXmitRcvCap = _WfAppnNodePortLsXmitRcvCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 22),
    _WfAppnNodePortLsXmitRcvCap_Type()
)
wfAppnNodePortLsXmitRcvCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortLsXmitRcvCap.setStatus("mandatory")


class _WfAppnNodePortTargetPacingCount_Type(Integer32):
    """Custom type wfAppnNodePortTargetPacingCount based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_WfAppnNodePortTargetPacingCount_Type.__name__ = "Integer32"
_WfAppnNodePortTargetPacingCount_Object = MibTableColumn
wfAppnNodePortTargetPacingCount = _WfAppnNodePortTargetPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 23),
    _WfAppnNodePortTargetPacingCount_Type()
)
wfAppnNodePortTargetPacingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortTargetPacingCount.setStatus("mandatory")


class _WfAppnNodePortMaxSendBtuSize_Type(Integer32):
    """Custom type wfAppnNodePortMaxSendBtuSize based on Integer32"""
    defaultValue = 1470

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 4105),
    )


_WfAppnNodePortMaxSendBtuSize_Type.__name__ = "Integer32"
_WfAppnNodePortMaxSendBtuSize_Object = MibTableColumn
wfAppnNodePortMaxSendBtuSize = _WfAppnNodePortMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 24),
    _WfAppnNodePortMaxSendBtuSize_Type()
)
wfAppnNodePortMaxSendBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortMaxSendBtuSize.setStatus("mandatory")


class _WfAppnNodePortImplicitCpSessions_Type(Integer32):
    """Custom type wfAppnNodePortImplicitCpSessions based on Integer32"""
    defaultValue = 1

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


_WfAppnNodePortImplicitCpSessions_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitCpSessions_Object = MibTableColumn
wfAppnNodePortImplicitCpSessions = _WfAppnNodePortImplicitCpSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 25),
    _WfAppnNodePortImplicitCpSessions_Type()
)
wfAppnNodePortImplicitCpSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitCpSessions.setStatus("mandatory")


class _WfAppnNodePortImplicitLimResource_Type(Integer32):
    """Custom type wfAppnNodePortImplicitLimResource based on Integer32"""
    defaultValue = 2

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


_WfAppnNodePortImplicitLimResource_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitLimResource_Object = MibTableColumn
wfAppnNodePortImplicitLimResource = _WfAppnNodePortImplicitLimResource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 26),
    _WfAppnNodePortImplicitLimResource_Type()
)
wfAppnNodePortImplicitLimResource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitLimResource.setStatus("mandatory")


class _WfAppnNodePortImplicitEffCap_Type(Integer32):
    """Custom type wfAppnNodePortImplicitEffCap based on Integer32"""
    defaultValue = 133

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodePortImplicitEffCap_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitEffCap_Object = MibTableColumn
wfAppnNodePortImplicitEffCap = _WfAppnNodePortImplicitEffCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 27),
    _WfAppnNodePortImplicitEffCap_Type()
)
wfAppnNodePortImplicitEffCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitEffCap.setStatus("mandatory")


class _WfAppnNodePortImplicitConnCost_Type(Integer32):
    """Custom type wfAppnNodePortImplicitConnCost based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodePortImplicitConnCost_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitConnCost_Object = MibTableColumn
wfAppnNodePortImplicitConnCost = _WfAppnNodePortImplicitConnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 28),
    _WfAppnNodePortImplicitConnCost_Type()
)
wfAppnNodePortImplicitConnCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitConnCost.setStatus("mandatory")


class _WfAppnNodePortImplicitByteCost_Type(Integer32):
    """Custom type wfAppnNodePortImplicitByteCost based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodePortImplicitByteCost_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitByteCost_Object = MibTableColumn
wfAppnNodePortImplicitByteCost = _WfAppnNodePortImplicitByteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 29),
    _WfAppnNodePortImplicitByteCost_Type()
)
wfAppnNodePortImplicitByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitByteCost.setStatus("mandatory")


class _WfAppnNodePortImplicitSecurity_Type(Integer32):
    """Custom type wfAppnNodePortImplicitSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodePortImplicitSecurity_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitSecurity_Object = MibTableColumn
wfAppnNodePortImplicitSecurity = _WfAppnNodePortImplicitSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 30),
    _WfAppnNodePortImplicitSecurity_Type()
)
wfAppnNodePortImplicitSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitSecurity.setStatus("mandatory")


class _WfAppnNodePortImplicitDelay_Type(Integer32):
    """Custom type wfAppnNodePortImplicitDelay based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnNodePortImplicitDelay_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitDelay_Object = MibTableColumn
wfAppnNodePortImplicitDelay = _WfAppnNodePortImplicitDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 31),
    _WfAppnNodePortImplicitDelay_Type()
)
wfAppnNodePortImplicitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitDelay.setStatus("mandatory")


class _WfAppnNodePortImplicitUsr1_Type(Integer32):
    """Custom type wfAppnNodePortImplicitUsr1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodePortImplicitUsr1_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitUsr1_Object = MibTableColumn
wfAppnNodePortImplicitUsr1 = _WfAppnNodePortImplicitUsr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 32),
    _WfAppnNodePortImplicitUsr1_Type()
)
wfAppnNodePortImplicitUsr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitUsr1.setStatus("mandatory")


class _WfAppnNodePortImplicitUsr2_Type(Integer32):
    """Custom type wfAppnNodePortImplicitUsr2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodePortImplicitUsr2_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitUsr2_Object = MibTableColumn
wfAppnNodePortImplicitUsr2 = _WfAppnNodePortImplicitUsr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 33),
    _WfAppnNodePortImplicitUsr2_Type()
)
wfAppnNodePortImplicitUsr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitUsr2.setStatus("mandatory")


class _WfAppnNodePortImplicitUsr3_Type(Integer32):
    """Custom type wfAppnNodePortImplicitUsr3 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodePortImplicitUsr3_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitUsr3_Object = MibTableColumn
wfAppnNodePortImplicitUsr3 = _WfAppnNodePortImplicitUsr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 34),
    _WfAppnNodePortImplicitUsr3_Type()
)
wfAppnNodePortImplicitUsr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitUsr3.setStatus("mandatory")


class _WfAppnNodePortImplicitHprDisable_Type(Integer32):
    """Custom type wfAppnNodePortImplicitHprDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodePortImplicitHprDisable_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitHprDisable_Object = MibTableColumn
wfAppnNodePortImplicitHprDisable = _WfAppnNodePortImplicitHprDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 35),
    _WfAppnNodePortImplicitHprDisable_Type()
)
wfAppnNodePortImplicitHprDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitHprDisable.setStatus("mandatory")


class _WfAppnNodePortImplicitHprLlErrorDisable_Type(Integer32):
    """Custom type wfAppnNodePortImplicitHprLlErrorDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodePortImplicitHprLlErrorDisable_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitHprLlErrorDisable_Object = MibTableColumn
wfAppnNodePortImplicitHprLlErrorDisable = _WfAppnNodePortImplicitHprLlErrorDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 36),
    _WfAppnNodePortImplicitHprLlErrorDisable_Type()
)
wfAppnNodePortImplicitHprLlErrorDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitHprLlErrorDisable.setStatus("mandatory")


class _WfAppnNodePortImplicitLinkDeactTime_Type(Integer32):
    """Custom type wfAppnNodePortImplicitLinkDeactTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_WfAppnNodePortImplicitLinkDeactTime_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitLinkDeactTime_Object = MibTableColumn
wfAppnNodePortImplicitLinkDeactTime = _WfAppnNodePortImplicitLinkDeactTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 37),
    _WfAppnNodePortImplicitLinkDeactTime_Type()
)
wfAppnNodePortImplicitLinkDeactTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitLinkDeactTime.setStatus("mandatory")
_WfAppnNodePortDlcData_Type = OctetString
_WfAppnNodePortDlcData_Object = MibTableColumn
wfAppnNodePortDlcData = _WfAppnNodePortDlcData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 38),
    _WfAppnNodePortDlcData_Type()
)
wfAppnNodePortDlcData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortDlcData.setStatus("mandatory")


class _WfAppnNodePortHprDlcData_Type(OctetString):
    """Custom type wfAppnNodePortHprDlcData based on OctetString"""
    defaultHexValue = "c8"


_WfAppnNodePortHprDlcData_Object = MibTableColumn
wfAppnNodePortHprDlcData = _WfAppnNodePortHprDlcData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 39),
    _WfAppnNodePortHprDlcData_Type()
)
wfAppnNodePortHprDlcData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortHprDlcData.setStatus("mandatory")


class _WfAppnNodePortImplicitDlurDisable_Type(Integer32):
    """Custom type wfAppnNodePortImplicitDlurDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodePortImplicitDlurDisable_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitDlurDisable_Object = MibTableColumn
wfAppnNodePortImplicitDlurDisable = _WfAppnNodePortImplicitDlurDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 40),
    _WfAppnNodePortImplicitDlurDisable_Type()
)
wfAppnNodePortImplicitDlurDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitDlurDisable.setStatus("mandatory")


class _WfAppnNodePortImplicitUplinkToEN_Type(Integer32):
    """Custom type wfAppnNodePortImplicitUplinkToEN based on Integer32"""
    defaultValue = 2

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


_WfAppnNodePortImplicitUplinkToEN_Type.__name__ = "Integer32"
_WfAppnNodePortImplicitUplinkToEN_Object = MibTableColumn
wfAppnNodePortImplicitUplinkToEN = _WfAppnNodePortImplicitUplinkToEN_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 3, 1, 41),
    _WfAppnNodePortImplicitUplinkToEN_Type()
)
wfAppnNodePortImplicitUplinkToEN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodePortImplicitUplinkToEN.setStatus("mandatory")
_WfAppnNodeLsTable_Object = MibTable
wfAppnNodeLsTable = _WfAppnNodeLsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4)
)
if mibBuilder.loadTexts:
    wfAppnNodeLsTable.setStatus("mandatory")
_WfAppnNodeLsEntry_Object = MibTableRow
wfAppnNodeLsEntry = _WfAppnNodeLsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1)
)
wfAppnNodeLsEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeLsName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeLsEntry.setStatus("mandatory")


class _WfAppnNodeLsDelete_Type(Integer32):
    """Custom type wfAppnNodeLsDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnNodeLsDelete_Type.__name__ = "Integer32"
_WfAppnNodeLsDelete_Object = MibTableColumn
wfAppnNodeLsDelete = _WfAppnNodeLsDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 1),
    _WfAppnNodeLsDelete_Type()
)
wfAppnNodeLsDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsDelete.setStatus("mandatory")


class _WfAppnNodeLsDisable_Type(Integer32):
    """Custom type wfAppnNodeLsDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeLsDisable_Type.__name__ = "Integer32"
_WfAppnNodeLsDisable_Object = MibTableColumn
wfAppnNodeLsDisable = _WfAppnNodeLsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 2),
    _WfAppnNodeLsDisable_Type()
)
wfAppnNodeLsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsDisable.setStatus("mandatory")
_WfAppnNodeLsName_Type = DisplayString
_WfAppnNodeLsName_Object = MibTableColumn
wfAppnNodeLsName = _WfAppnNodeLsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 3),
    _WfAppnNodeLsName_Type()
)
wfAppnNodeLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsName.setStatus("mandatory")
_WfAppnNodeLsPortName_Type = DisplayString
_WfAppnNodeLsPortName_Object = MibTableColumn
wfAppnNodeLsPortName = _WfAppnNodeLsPortName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 4),
    _WfAppnNodeLsPortName_Type()
)
wfAppnNodeLsPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsPortName.setStatus("mandatory")


class _WfAppnNodeLsState_Type(Integer32):
    """Custom type wfAppnNodeLsState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_WfAppnNodeLsState_Type.__name__ = "Integer32"
_WfAppnNodeLsState_Object = MibTableColumn
wfAppnNodeLsState = _WfAppnNodeLsState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 5),
    _WfAppnNodeLsState_Type()
)
wfAppnNodeLsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsState.setStatus("mandatory")
_WfAppnNodeLsCpName_Type = DisplayString
_WfAppnNodeLsCpName_Object = MibTableColumn
wfAppnNodeLsCpName = _WfAppnNodeLsCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 6),
    _WfAppnNodeLsCpName_Type()
)
wfAppnNodeLsCpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsCpName.setStatus("mandatory")


class _WfAppnNodeLsTgNum_Type(Integer32):
    """Custom type wfAppnNodeLsTgNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_WfAppnNodeLsTgNum_Type.__name__ = "Integer32"
_WfAppnNodeLsTgNum_Object = MibTableColumn
wfAppnNodeLsTgNum = _WfAppnNodeLsTgNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 7),
    _WfAppnNodeLsTgNum_Type()
)
wfAppnNodeLsTgNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsTgNum.setStatus("mandatory")


class _WfAppnNodeLsLimResource_Type(Integer32):
    """Custom type wfAppnNodeLsLimResource based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeLsLimResource_Type.__name__ = "Integer32"
_WfAppnNodeLsLimResource_Object = MibTableColumn
wfAppnNodeLsLimResource = _WfAppnNodeLsLimResource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 8),
    _WfAppnNodeLsLimResource_Type()
)
wfAppnNodeLsLimResource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsLimResource.setStatus("mandatory")


class _WfAppnNodeLsMigration_Type(Integer32):
    """Custom type wfAppnNodeLsMigration based on Integer32"""
    defaultValue = 2

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
        *(("noxid", 4),
          ("uplevel", 2),
          ("xid0", 1),
          ("xid3", 3))
    )


_WfAppnNodeLsMigration_Type.__name__ = "Integer32"
_WfAppnNodeLsMigration_Object = MibTableColumn
wfAppnNodeLsMigration = _WfAppnNodeLsMigration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 9),
    _WfAppnNodeLsMigration_Type()
)
wfAppnNodeLsMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsMigration.setStatus("mandatory")
_WfAppnNodeLsBlockNum_Type = DisplayString
_WfAppnNodeLsBlockNum_Object = MibTableColumn
wfAppnNodeLsBlockNum = _WfAppnNodeLsBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 10),
    _WfAppnNodeLsBlockNum_Type()
)
wfAppnNodeLsBlockNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsBlockNum.setStatus("mandatory")
_WfAppnNodeLsIdNum_Type = DisplayString
_WfAppnNodeLsIdNum_Object = MibTableColumn
wfAppnNodeLsIdNum = _WfAppnNodeLsIdNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 11),
    _WfAppnNodeLsIdNum_Type()
)
wfAppnNodeLsIdNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsIdNum.setStatus("mandatory")


class _WfAppnNodeLsCpCpSession_Type(Integer32):
    """Custom type wfAppnNodeLsCpCpSession based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeLsCpCpSession_Type.__name__ = "Integer32"
_WfAppnNodeLsCpCpSession_Object = MibTableColumn
wfAppnNodeLsCpCpSession = _WfAppnNodeLsCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 12),
    _WfAppnNodeLsCpCpSession_Type()
)
wfAppnNodeLsCpCpSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsCpCpSession.setStatus("mandatory")


class _WfAppnNodeLsTargetPacingCount_Type(Integer32):
    """Custom type wfAppnNodeLsTargetPacingCount based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WfAppnNodeLsTargetPacingCount_Type.__name__ = "Integer32"
_WfAppnNodeLsTargetPacingCount_Object = MibTableColumn
wfAppnNodeLsTargetPacingCount = _WfAppnNodeLsTargetPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 13),
    _WfAppnNodeLsTargetPacingCount_Type()
)
wfAppnNodeLsTargetPacingCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsTargetPacingCount.setStatus("mandatory")


class _WfAppnNodeLsMaxSendBtuSize_Type(Integer32):
    """Custom type wfAppnNodeLsMaxSendBtuSize based on Integer32"""
    defaultValue = 1470

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4105),
    )


_WfAppnNodeLsMaxSendBtuSize_Type.__name__ = "Integer32"
_WfAppnNodeLsMaxSendBtuSize_Object = MibTableColumn
wfAppnNodeLsMaxSendBtuSize = _WfAppnNodeLsMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 14),
    _WfAppnNodeLsMaxSendBtuSize_Type()
)
wfAppnNodeLsMaxSendBtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsMaxSendBtuSize.setStatus("mandatory")


class _WfAppnNodeLsEffCap_Type(Integer32):
    """Custom type wfAppnNodeLsEffCap based on Integer32"""
    defaultValue = 133

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsEffCap_Type.__name__ = "Integer32"
_WfAppnNodeLsEffCap_Object = MibTableColumn
wfAppnNodeLsEffCap = _WfAppnNodeLsEffCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 15),
    _WfAppnNodeLsEffCap_Type()
)
wfAppnNodeLsEffCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsEffCap.setStatus("mandatory")


class _WfAppnNodeLsConnCost_Type(Integer32):
    """Custom type wfAppnNodeLsConnCost based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsConnCost_Type.__name__ = "Integer32"
_WfAppnNodeLsConnCost_Object = MibTableColumn
wfAppnNodeLsConnCost = _WfAppnNodeLsConnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 16),
    _WfAppnNodeLsConnCost_Type()
)
wfAppnNodeLsConnCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsConnCost.setStatus("mandatory")


class _WfAppnNodeLsByteCost_Type(Integer32):
    """Custom type wfAppnNodeLsByteCost based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsByteCost_Type.__name__ = "Integer32"
_WfAppnNodeLsByteCost_Object = MibTableColumn
wfAppnNodeLsByteCost = _WfAppnNodeLsByteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 17),
    _WfAppnNodeLsByteCost_Type()
)
wfAppnNodeLsByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsByteCost.setStatus("mandatory")


class _WfAppnNodeLsSecurity_Type(Integer32):
    """Custom type wfAppnNodeLsSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsSecurity_Type.__name__ = "Integer32"
_WfAppnNodeLsSecurity_Object = MibTableColumn
wfAppnNodeLsSecurity = _WfAppnNodeLsSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 18),
    _WfAppnNodeLsSecurity_Type()
)
wfAppnNodeLsSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsSecurity.setStatus("mandatory")


class _WfAppnNodeLsDelay_Type(Integer32):
    """Custom type wfAppnNodeLsDelay based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnNodeLsDelay_Type.__name__ = "Integer32"
_WfAppnNodeLsDelay_Object = MibTableColumn
wfAppnNodeLsDelay = _WfAppnNodeLsDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 19),
    _WfAppnNodeLsDelay_Type()
)
wfAppnNodeLsDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsDelay.setStatus("mandatory")


class _WfAppnNodeLsUsr1_Type(Integer32):
    """Custom type wfAppnNodeLsUsr1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsUsr1_Type.__name__ = "Integer32"
_WfAppnNodeLsUsr1_Object = MibTableColumn
wfAppnNodeLsUsr1 = _WfAppnNodeLsUsr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 20),
    _WfAppnNodeLsUsr1_Type()
)
wfAppnNodeLsUsr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsUsr1.setStatus("mandatory")


class _WfAppnNodeLsUsr2_Type(Integer32):
    """Custom type wfAppnNodeLsUsr2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsUsr2_Type.__name__ = "Integer32"
_WfAppnNodeLsUsr2_Object = MibTableColumn
wfAppnNodeLsUsr2 = _WfAppnNodeLsUsr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 21),
    _WfAppnNodeLsUsr2_Type()
)
wfAppnNodeLsUsr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsUsr2.setStatus("mandatory")


class _WfAppnNodeLsUsr3_Type(Integer32):
    """Custom type wfAppnNodeLsUsr3 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsUsr3_Type.__name__ = "Integer32"
_WfAppnNodeLsUsr3_Object = MibTableColumn
wfAppnNodeLsUsr3 = _WfAppnNodeLsUsr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 22),
    _WfAppnNodeLsUsr3_Type()
)
wfAppnNodeLsUsr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsUsr3.setStatus("mandatory")


class _WfAppnNodeLsCpType_Type(Integer32):
    """Custom type wfAppnNodeLsCpType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("bllen", 4),
          ("dspunoxid", 8),
          ("dspuxid", 7),
          ("en", 3),
          ("hostxid0", 6),
          ("hostxid3", 5),
          ("learn", 1),
          ("nn", 2))
    )


_WfAppnNodeLsCpType_Type.__name__ = "Integer32"
_WfAppnNodeLsCpType_Object = MibTableColumn
wfAppnNodeLsCpType = _WfAppnNodeLsCpType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 23),
    _WfAppnNodeLsCpType_Type()
)
wfAppnNodeLsCpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsCpType.setStatus("mandatory")


class _WfAppnNodeLsAutoActivateDisable_Type(Integer32):
    """Custom type wfAppnNodeLsAutoActivateDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeLsAutoActivateDisable_Type.__name__ = "Integer32"
_WfAppnNodeLsAutoActivateDisable_Object = MibTableColumn
wfAppnNodeLsAutoActivateDisable = _WfAppnNodeLsAutoActivateDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 24),
    _WfAppnNodeLsAutoActivateDisable_Type()
)
wfAppnNodeLsAutoActivateDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsAutoActivateDisable.setStatus("mandatory")


class _WfAppnNodeLsSolicitSscpSessionsDisable_Type(Integer32):
    """Custom type wfAppnNodeLsSolicitSscpSessionsDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeLsSolicitSscpSessionsDisable_Type.__name__ = "Integer32"
_WfAppnNodeLsSolicitSscpSessionsDisable_Object = MibTableColumn
wfAppnNodeLsSolicitSscpSessionsDisable = _WfAppnNodeLsSolicitSscpSessionsDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 25),
    _WfAppnNodeLsSolicitSscpSessionsDisable_Type()
)
wfAppnNodeLsSolicitSscpSessionsDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsSolicitSscpSessionsDisable.setStatus("mandatory")


class _WfAppnNodeLsUseDefaultTgChars_Type(Integer32):
    """Custom type wfAppnNodeLsUseDefaultTgChars based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeLsUseDefaultTgChars_Type.__name__ = "Integer32"
_WfAppnNodeLsUseDefaultTgChars_Object = MibTableColumn
wfAppnNodeLsUseDefaultTgChars = _WfAppnNodeLsUseDefaultTgChars_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 26),
    _WfAppnNodeLsUseDefaultTgChars_Type()
)
wfAppnNodeLsUseDefaultTgChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsUseDefaultTgChars.setStatus("mandatory")
_WfAppnNodeLsLinkData_Type = OctetString
_WfAppnNodeLsLinkData_Object = MibTableColumn
wfAppnNodeLsLinkData = _WfAppnNodeLsLinkData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 27),
    _WfAppnNodeLsLinkData_Type()
)
wfAppnNodeLsLinkData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsLinkData.setStatus("mandatory")


class _WfAppnNodeLsDlurDisable_Type(Integer32):
    """Custom type wfAppnNodeLsDlurDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeLsDlurDisable_Type.__name__ = "Integer32"
_WfAppnNodeLsDlurDisable_Object = MibTableColumn
wfAppnNodeLsDlurDisable = _WfAppnNodeLsDlurDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 28),
    _WfAppnNodeLsDlurDisable_Type()
)
wfAppnNodeLsDlurDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsDlurDisable.setStatus("mandatory")
_WfAppnNodeLsDspuName_Type = DisplayString
_WfAppnNodeLsDspuName_Object = MibTableColumn
wfAppnNodeLsDspuName = _WfAppnNodeLsDspuName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 29),
    _WfAppnNodeLsDspuName_Type()
)
wfAppnNodeLsDspuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsDspuName.setStatus("mandatory")
_WfAppnNodeLsDlusName_Type = DisplayString
_WfAppnNodeLsDlusName_Object = MibTableColumn
wfAppnNodeLsDlusName = _WfAppnNodeLsDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 30),
    _WfAppnNodeLsDlusName_Type()
)
wfAppnNodeLsDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsDlusName.setStatus("mandatory")
_WfAppnNodeLsBackupDlusName_Type = DisplayString
_WfAppnNodeLsBackupDlusName_Object = MibTableColumn
wfAppnNodeLsBackupDlusName = _WfAppnNodeLsBackupDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 31),
    _WfAppnNodeLsBackupDlusName_Type()
)
wfAppnNodeLsBackupDlusName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsBackupDlusName.setStatus("mandatory")


class _WfAppnNodeLsHprDisable_Type(Integer32):
    """Custom type wfAppnNodeLsHprDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeLsHprDisable_Type.__name__ = "Integer32"
_WfAppnNodeLsHprDisable_Object = MibTableColumn
wfAppnNodeLsHprDisable = _WfAppnNodeLsHprDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 32),
    _WfAppnNodeLsHprDisable_Type()
)
wfAppnNodeLsHprDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsHprDisable.setStatus("mandatory")


class _WfAppnNodeLsHprLlErrorDisable_Type(Integer32):
    """Custom type wfAppnNodeLsHprLlErrorDisable based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeLsHprLlErrorDisable_Type.__name__ = "Integer32"
_WfAppnNodeLsHprLlErrorDisable_Object = MibTableColumn
wfAppnNodeLsHprLlErrorDisable = _WfAppnNodeLsHprLlErrorDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 33),
    _WfAppnNodeLsHprLlErrorDisable_Type()
)
wfAppnNodeLsHprLlErrorDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsHprLlErrorDisable.setStatus("mandatory")


class _WfAppnNodeLsLinkDeactTime_Type(Integer32):
    """Custom type wfAppnNodeLsLinkDeactTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 2147483647),
    )


_WfAppnNodeLsLinkDeactTime_Type.__name__ = "Integer32"
_WfAppnNodeLsLinkDeactTime_Object = MibTableColumn
wfAppnNodeLsLinkDeactTime = _WfAppnNodeLsLinkDeactTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 34),
    _WfAppnNodeLsLinkDeactTime_Type()
)
wfAppnNodeLsLinkDeactTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsLinkDeactTime.setStatus("mandatory")


class _WfAppnNodeLsLinkRetryCount_Type(Integer32):
    """Custom type wfAppnNodeLsLinkRetryCount based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfAppnNodeLsLinkRetryCount_Type.__name__ = "Integer32"
_WfAppnNodeLsLinkRetryCount_Object = MibTableColumn
wfAppnNodeLsLinkRetryCount = _WfAppnNodeLsLinkRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 35),
    _WfAppnNodeLsLinkRetryCount_Type()
)
wfAppnNodeLsLinkRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsLinkRetryCount.setStatus("mandatory")


class _WfAppnNodeLsBranchLinkType_Type(Integer32):
    """Custom type wfAppnNodeLsBranchLinkType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downlink", 2),
          ("uplink", 1))
    )


_WfAppnNodeLsBranchLinkType_Type.__name__ = "Integer32"
_WfAppnNodeLsBranchLinkType_Object = MibTableColumn
wfAppnNodeLsBranchLinkType = _WfAppnNodeLsBranchLinkType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 36),
    _WfAppnNodeLsBranchLinkType_Type()
)
wfAppnNodeLsBranchLinkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsBranchLinkType.setStatus("mandatory")


class _WfAppnNodeLsAdjBrNNLinkSupp_Type(Integer32):
    """Custom type wfAppnNodeLsAdjBrNNLinkSupp based on Integer32"""
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
        *(("allowed", 1),
          ("prohibited", 3),
          ("required", 2))
    )


_WfAppnNodeLsAdjBrNNLinkSupp_Type.__name__ = "Integer32"
_WfAppnNodeLsAdjBrNNLinkSupp_Object = MibTableColumn
wfAppnNodeLsAdjBrNNLinkSupp = _WfAppnNodeLsAdjBrNNLinkSupp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 37),
    _WfAppnNodeLsAdjBrNNLinkSupp_Type()
)
wfAppnNodeLsAdjBrNNLinkSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsAdjBrNNLinkSupp.setStatus("mandatory")


class _WfAppnNodeLsDefaultNNS_Type(Integer32):
    """Custom type wfAppnNodeLsDefaultNNS based on Integer32"""
    defaultValue = 2

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


_WfAppnNodeLsDefaultNNS_Type.__name__ = "Integer32"
_WfAppnNodeLsDefaultNNS_Object = MibTableColumn
wfAppnNodeLsDefaultNNS = _WfAppnNodeLsDefaultNNS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 4, 1, 38),
    _WfAppnNodeLsDefaultNNS_Type()
)
wfAppnNodeLsDefaultNNS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeLsDefaultNNS.setStatus("mandatory")
_WfAppnNodeLsStatusTable_Object = MibTable
wfAppnNodeLsStatusTable = _WfAppnNodeLsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5)
)
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusTable.setStatus("mandatory")
_WfAppnNodeLsStatusEntry_Object = MibTableRow
wfAppnNodeLsStatusEntry = _WfAppnNodeLsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1)
)
wfAppnNodeLsStatusEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeLsStatusName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusEntry.setStatus("mandatory")
_WfAppnNodeLsStatusName_Type = DisplayString
_WfAppnNodeLsStatusName_Object = MibTableColumn
wfAppnNodeLsStatusName = _WfAppnNodeLsStatusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 1),
    _WfAppnNodeLsStatusName_Type()
)
wfAppnNodeLsStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusName.setStatus("mandatory")
_WfAppnNodeLsStatusPortName_Type = DisplayString
_WfAppnNodeLsStatusPortName_Object = MibTableColumn
wfAppnNodeLsStatusPortName = _WfAppnNodeLsStatusPortName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 2),
    _WfAppnNodeLsStatusPortName_Type()
)
wfAppnNodeLsStatusPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusPortName.setStatus("mandatory")


class _WfAppnNodeLsStatusDlcType_Type(Integer32):
    """Custom type wfAppnNodeLsStatusDlcType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("dls", 3),
          ("ethernet", 5),
          ("other", 1),
          ("sdlc", 2),
          ("socket", 4),
          ("tokenring", 6))
    )


_WfAppnNodeLsStatusDlcType_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusDlcType_Object = MibTableColumn
wfAppnNodeLsStatusDlcType = _WfAppnNodeLsStatusDlcType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 3),
    _WfAppnNodeLsStatusDlcType_Type()
)
wfAppnNodeLsStatusDlcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusDlcType.setStatus("mandatory")


class _WfAppnNodeLsStatusDynamic_Type(Integer32):
    """Custom type wfAppnNodeLsStatusDynamic based on Integer32"""
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


_WfAppnNodeLsStatusDynamic_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusDynamic_Object = MibTableColumn
wfAppnNodeLsStatusDynamic = _WfAppnNodeLsStatusDynamic_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 4),
    _WfAppnNodeLsStatusDynamic_Type()
)
wfAppnNodeLsStatusDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusDynamic.setStatus("mandatory")


class _WfAppnNodeLsStatusState_Type(Integer32):
    """Custom type wfAppnNodeLsStatusState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_WfAppnNodeLsStatusState_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusState_Object = MibTableColumn
wfAppnNodeLsStatusState = _WfAppnNodeLsStatusState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 5),
    _WfAppnNodeLsStatusState_Type()
)
wfAppnNodeLsStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusState.setStatus("mandatory")
_WfAppnNodeLsStatusCpName_Type = DisplayString
_WfAppnNodeLsStatusCpName_Object = MibTableColumn
wfAppnNodeLsStatusCpName = _WfAppnNodeLsStatusCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 6),
    _WfAppnNodeLsStatusCpName_Type()
)
wfAppnNodeLsStatusCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusCpName.setStatus("mandatory")
_WfAppnNodeLsStatusTgNum_Type = Integer32
_WfAppnNodeLsStatusTgNum_Object = MibTableColumn
wfAppnNodeLsStatusTgNum = _WfAppnNodeLsStatusTgNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 7),
    _WfAppnNodeLsStatusTgNum_Type()
)
wfAppnNodeLsStatusTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusTgNum.setStatus("mandatory")


class _WfAppnNodeLsStatusLimResource_Type(Integer32):
    """Custom type wfAppnNodeLsStatusLimResource based on Integer32"""
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


_WfAppnNodeLsStatusLimResource_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusLimResource_Object = MibTableColumn
wfAppnNodeLsStatusLimResource = _WfAppnNodeLsStatusLimResource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 8),
    _WfAppnNodeLsStatusLimResource_Type()
)
wfAppnNodeLsStatusLimResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusLimResource.setStatus("mandatory")


class _WfAppnNodeLsStatusMigration_Type(Integer32):
    """Custom type wfAppnNodeLsStatusMigration based on Integer32"""
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
        *(("noxid", 4),
          ("uplevel", 2),
          ("xid0", 1),
          ("xid3", 3))
    )


_WfAppnNodeLsStatusMigration_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusMigration_Object = MibTableColumn
wfAppnNodeLsStatusMigration = _WfAppnNodeLsStatusMigration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 9),
    _WfAppnNodeLsStatusMigration_Type()
)
wfAppnNodeLsStatusMigration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusMigration.setStatus("mandatory")
_WfAppnNodeLsStatusBlockNum_Type = DisplayString
_WfAppnNodeLsStatusBlockNum_Object = MibTableColumn
wfAppnNodeLsStatusBlockNum = _WfAppnNodeLsStatusBlockNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 10),
    _WfAppnNodeLsStatusBlockNum_Type()
)
wfAppnNodeLsStatusBlockNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusBlockNum.setStatus("mandatory")
_WfAppnNodeLsStatusIdNum_Type = DisplayString
_WfAppnNodeLsStatusIdNum_Object = MibTableColumn
wfAppnNodeLsStatusIdNum = _WfAppnNodeLsStatusIdNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 11),
    _WfAppnNodeLsStatusIdNum_Type()
)
wfAppnNodeLsStatusIdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusIdNum.setStatus("mandatory")


class _WfAppnNodeLsStatusCpCpSession_Type(Integer32):
    """Custom type wfAppnNodeLsStatusCpCpSession based on Integer32"""
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


_WfAppnNodeLsStatusCpCpSession_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusCpCpSession_Object = MibTableColumn
wfAppnNodeLsStatusCpCpSession = _WfAppnNodeLsStatusCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 12),
    _WfAppnNodeLsStatusCpCpSession_Type()
)
wfAppnNodeLsStatusCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusCpCpSession.setStatus("mandatory")
_WfAppnNodeLsStatusTargetPacingCount_Type = Integer32
_WfAppnNodeLsStatusTargetPacingCount_Object = MibTableColumn
wfAppnNodeLsStatusTargetPacingCount = _WfAppnNodeLsStatusTargetPacingCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 13),
    _WfAppnNodeLsStatusTargetPacingCount_Type()
)
wfAppnNodeLsStatusTargetPacingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusTargetPacingCount.setStatus("mandatory")
_WfAppnNodeLsStatusMaxSendBtuSize_Type = Integer32
_WfAppnNodeLsStatusMaxSendBtuSize_Object = MibTableColumn
wfAppnNodeLsStatusMaxSendBtuSize = _WfAppnNodeLsStatusMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 14),
    _WfAppnNodeLsStatusMaxSendBtuSize_Type()
)
wfAppnNodeLsStatusMaxSendBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusMaxSendBtuSize.setStatus("mandatory")


class _WfAppnNodeLsStatusEffCap_Type(Integer32):
    """Custom type wfAppnNodeLsStatusEffCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsStatusEffCap_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusEffCap_Object = MibTableColumn
wfAppnNodeLsStatusEffCap = _WfAppnNodeLsStatusEffCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 15),
    _WfAppnNodeLsStatusEffCap_Type()
)
wfAppnNodeLsStatusEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusEffCap.setStatus("mandatory")


class _WfAppnNodeLsStatusConnCost_Type(Integer32):
    """Custom type wfAppnNodeLsStatusConnCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsStatusConnCost_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusConnCost_Object = MibTableColumn
wfAppnNodeLsStatusConnCost = _WfAppnNodeLsStatusConnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 16),
    _WfAppnNodeLsStatusConnCost_Type()
)
wfAppnNodeLsStatusConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusConnCost.setStatus("mandatory")


class _WfAppnNodeLsStatusByteCost_Type(Integer32):
    """Custom type wfAppnNodeLsStatusByteCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsStatusByteCost_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusByteCost_Object = MibTableColumn
wfAppnNodeLsStatusByteCost = _WfAppnNodeLsStatusByteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 17),
    _WfAppnNodeLsStatusByteCost_Type()
)
wfAppnNodeLsStatusByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusByteCost.setStatus("mandatory")


class _WfAppnNodeLsStatusSecurity_Type(Integer32):
    """Custom type wfAppnNodeLsStatusSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsStatusSecurity_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusSecurity_Object = MibTableColumn
wfAppnNodeLsStatusSecurity = _WfAppnNodeLsStatusSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 18),
    _WfAppnNodeLsStatusSecurity_Type()
)
wfAppnNodeLsStatusSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusSecurity.setStatus("mandatory")


class _WfAppnNodeLsStatusDelay_Type(Integer32):
    """Custom type wfAppnNodeLsStatusDelay based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnNodeLsStatusDelay_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusDelay_Object = MibTableColumn
wfAppnNodeLsStatusDelay = _WfAppnNodeLsStatusDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 19),
    _WfAppnNodeLsStatusDelay_Type()
)
wfAppnNodeLsStatusDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusDelay.setStatus("mandatory")


class _WfAppnNodeLsStatusUsr1_Type(Integer32):
    """Custom type wfAppnNodeLsStatusUsr1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsStatusUsr1_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusUsr1_Object = MibTableColumn
wfAppnNodeLsStatusUsr1 = _WfAppnNodeLsStatusUsr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 20),
    _WfAppnNodeLsStatusUsr1_Type()
)
wfAppnNodeLsStatusUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusUsr1.setStatus("mandatory")


class _WfAppnNodeLsStatusUsr2_Type(Integer32):
    """Custom type wfAppnNodeLsStatusUsr2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsStatusUsr2_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusUsr2_Object = MibTableColumn
wfAppnNodeLsStatusUsr2 = _WfAppnNodeLsStatusUsr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 21),
    _WfAppnNodeLsStatusUsr2_Type()
)
wfAppnNodeLsStatusUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusUsr2.setStatus("mandatory")


class _WfAppnNodeLsStatusUsr3_Type(Integer32):
    """Custom type wfAppnNodeLsStatusUsr3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeLsStatusUsr3_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusUsr3_Object = MibTableColumn
wfAppnNodeLsStatusUsr3 = _WfAppnNodeLsStatusUsr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 22),
    _WfAppnNodeLsStatusUsr3_Type()
)
wfAppnNodeLsStatusUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusUsr3.setStatus("mandatory")
_WfAppnNodeLsStatusInXidBytes_Type = Counter32
_WfAppnNodeLsStatusInXidBytes_Object = MibTableColumn
wfAppnNodeLsStatusInXidBytes = _WfAppnNodeLsStatusInXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 23),
    _WfAppnNodeLsStatusInXidBytes_Type()
)
wfAppnNodeLsStatusInXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusInXidBytes.setStatus("mandatory")
_WfAppnNodeLsStatusInMsgBytes_Type = Counter32
_WfAppnNodeLsStatusInMsgBytes_Object = MibTableColumn
wfAppnNodeLsStatusInMsgBytes = _WfAppnNodeLsStatusInMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 24),
    _WfAppnNodeLsStatusInMsgBytes_Type()
)
wfAppnNodeLsStatusInMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusInMsgBytes.setStatus("mandatory")
_WfAppnNodeLsStatusInXidFrames_Type = Counter32
_WfAppnNodeLsStatusInXidFrames_Object = MibTableColumn
wfAppnNodeLsStatusInXidFrames = _WfAppnNodeLsStatusInXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 25),
    _WfAppnNodeLsStatusInXidFrames_Type()
)
wfAppnNodeLsStatusInXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusInXidFrames.setStatus("mandatory")
_WfAppnNodeLsStatusInMsgFrames_Type = Counter32
_WfAppnNodeLsStatusInMsgFrames_Object = MibTableColumn
wfAppnNodeLsStatusInMsgFrames = _WfAppnNodeLsStatusInMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 26),
    _WfAppnNodeLsStatusInMsgFrames_Type()
)
wfAppnNodeLsStatusInMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusInMsgFrames.setStatus("mandatory")
_WfAppnNodeLsStatusOutXidBytes_Type = Counter32
_WfAppnNodeLsStatusOutXidBytes_Object = MibTableColumn
wfAppnNodeLsStatusOutXidBytes = _WfAppnNodeLsStatusOutXidBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 27),
    _WfAppnNodeLsStatusOutXidBytes_Type()
)
wfAppnNodeLsStatusOutXidBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusOutXidBytes.setStatus("mandatory")
_WfAppnNodeLsStatusOutMsgBytes_Type = Counter32
_WfAppnNodeLsStatusOutMsgBytes_Object = MibTableColumn
wfAppnNodeLsStatusOutMsgBytes = _WfAppnNodeLsStatusOutMsgBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 28),
    _WfAppnNodeLsStatusOutMsgBytes_Type()
)
wfAppnNodeLsStatusOutMsgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusOutMsgBytes.setStatus("mandatory")
_WfAppnNodeLsStatusOutXidFrames_Type = Counter32
_WfAppnNodeLsStatusOutXidFrames_Object = MibTableColumn
wfAppnNodeLsStatusOutXidFrames = _WfAppnNodeLsStatusOutXidFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 29),
    _WfAppnNodeLsStatusOutXidFrames_Type()
)
wfAppnNodeLsStatusOutXidFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusOutXidFrames.setStatus("mandatory")
_WfAppnNodeLsStatusOutMsgFrames_Type = Counter32
_WfAppnNodeLsStatusOutMsgFrames_Object = MibTableColumn
wfAppnNodeLsStatusOutMsgFrames = _WfAppnNodeLsStatusOutMsgFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 30),
    _WfAppnNodeLsStatusOutMsgFrames_Type()
)
wfAppnNodeLsStatusOutMsgFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusOutMsgFrames.setStatus("mandatory")
_WfAppnNodeLsStatusEchoRsps_Type = Counter32
_WfAppnNodeLsStatusEchoRsps_Object = MibTableColumn
wfAppnNodeLsStatusEchoRsps = _WfAppnNodeLsStatusEchoRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 31),
    _WfAppnNodeLsStatusEchoRsps_Type()
)
wfAppnNodeLsStatusEchoRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusEchoRsps.setStatus("mandatory")
_WfAppnNodeLsStatusCurrentDelay_Type = Integer32
_WfAppnNodeLsStatusCurrentDelay_Object = MibTableColumn
wfAppnNodeLsStatusCurrentDelay = _WfAppnNodeLsStatusCurrentDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 32),
    _WfAppnNodeLsStatusCurrentDelay_Type()
)
wfAppnNodeLsStatusCurrentDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusCurrentDelay.setStatus("mandatory")
_WfAppnNodeLsStatusMaxDelay_Type = Integer32
_WfAppnNodeLsStatusMaxDelay_Object = MibTableColumn
wfAppnNodeLsStatusMaxDelay = _WfAppnNodeLsStatusMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 33),
    _WfAppnNodeLsStatusMaxDelay_Type()
)
wfAppnNodeLsStatusMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusMaxDelay.setStatus("mandatory")
_WfAppnNodeLsStatusMinDelay_Type = Integer32
_WfAppnNodeLsStatusMinDelay_Object = MibTableColumn
wfAppnNodeLsStatusMinDelay = _WfAppnNodeLsStatusMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 34),
    _WfAppnNodeLsStatusMinDelay_Type()
)
wfAppnNodeLsStatusMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusMinDelay.setStatus("mandatory")
_WfAppnNodeLsStatusMaxDelayTime_Type = Integer32
_WfAppnNodeLsStatusMaxDelayTime_Object = MibTableColumn
wfAppnNodeLsStatusMaxDelayTime = _WfAppnNodeLsStatusMaxDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 35),
    _WfAppnNodeLsStatusMaxDelayTime_Type()
)
wfAppnNodeLsStatusMaxDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusMaxDelayTime.setStatus("mandatory")
_WfAppnNodeLsStatusGoodXids_Type = Counter32
_WfAppnNodeLsStatusGoodXids_Object = MibTableColumn
wfAppnNodeLsStatusGoodXids = _WfAppnNodeLsStatusGoodXids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 36),
    _WfAppnNodeLsStatusGoodXids_Type()
)
wfAppnNodeLsStatusGoodXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusGoodXids.setStatus("mandatory")
_WfAppnNodeLsStatusBadXids_Type = Counter32
_WfAppnNodeLsStatusBadXids_Object = MibTableColumn
wfAppnNodeLsStatusBadXids = _WfAppnNodeLsStatusBadXids_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 37),
    _WfAppnNodeLsStatusBadXids_Type()
)
wfAppnNodeLsStatusBadXids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusBadXids.setStatus("mandatory")
_WfAppnNodeLsStatusActiveSessions_Type = Integer32
_WfAppnNodeLsStatusActiveSessions_Object = MibTableColumn
wfAppnNodeLsStatusActiveSessions = _WfAppnNodeLsStatusActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 38),
    _WfAppnNodeLsStatusActiveSessions_Type()
)
wfAppnNodeLsStatusActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusActiveSessions.setStatus("mandatory")
_WfAppnNodeLsStatusInvalidSnaFrames_Type = Counter32
_WfAppnNodeLsStatusInvalidSnaFrames_Object = MibTableColumn
wfAppnNodeLsStatusInvalidSnaFrames = _WfAppnNodeLsStatusInvalidSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 39),
    _WfAppnNodeLsStatusInvalidSnaFrames_Type()
)
wfAppnNodeLsStatusInvalidSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusInvalidSnaFrames.setStatus("mandatory")
_WfAppnNodeLsStatusInScFrames_Type = Counter32
_WfAppnNodeLsStatusInScFrames_Object = MibTableColumn
wfAppnNodeLsStatusInScFrames = _WfAppnNodeLsStatusInScFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 40),
    _WfAppnNodeLsStatusInScFrames_Type()
)
wfAppnNodeLsStatusInScFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusInScFrames.setStatus("mandatory")
_WfAppnNodeLsStatusOutScFrames_Type = Counter32
_WfAppnNodeLsStatusOutScFrames_Object = MibTableColumn
wfAppnNodeLsStatusOutScFrames = _WfAppnNodeLsStatusOutScFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 41),
    _WfAppnNodeLsStatusOutScFrames_Type()
)
wfAppnNodeLsStatusOutScFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusOutScFrames.setStatus("mandatory")


class _WfAppnNodeLsStatusCpType_Type(Integer32):
    """Custom type wfAppnNodeLsStatusCpType based on Integer32"""
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
        *(("bllen", 4),
          ("dspunoxid", 8),
          ("dspuxid", 7),
          ("en", 3),
          ("hostxid0", 6),
          ("hostxid3", 5),
          ("learn", 1),
          ("nn", 2))
    )


_WfAppnNodeLsStatusCpType_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusCpType_Object = MibTableColumn
wfAppnNodeLsStatusCpType = _WfAppnNodeLsStatusCpType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 42),
    _WfAppnNodeLsStatusCpType_Type()
)
wfAppnNodeLsStatusCpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusCpType.setStatus("mandatory")
_WfAppnNodeLsStatusStartTime_Type = Integer32
_WfAppnNodeLsStatusStartTime_Object = MibTableColumn
wfAppnNodeLsStatusStartTime = _WfAppnNodeLsStatusStartTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 43),
    _WfAppnNodeLsStatusStartTime_Type()
)
wfAppnNodeLsStatusStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusStartTime.setStatus("mandatory")
_WfAppnNodeLsStatusStopTime_Type = Integer32
_WfAppnNodeLsStatusStopTime_Object = MibTableColumn
wfAppnNodeLsStatusStopTime = _WfAppnNodeLsStatusStopTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 44),
    _WfAppnNodeLsStatusStopTime_Type()
)
wfAppnNodeLsStatusStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusStopTime.setStatus("mandatory")
_WfAppnNodeLsStatusUpTime_Type = Integer32
_WfAppnNodeLsStatusUpTime_Object = MibTableColumn
wfAppnNodeLsStatusUpTime = _WfAppnNodeLsStatusUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 45),
    _WfAppnNodeLsStatusUpTime_Type()
)
wfAppnNodeLsStatusUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusUpTime.setStatus("mandatory")
_WfAppnNodeLsStatusDeactCause_Type = Integer32
_WfAppnNodeLsStatusDeactCause_Object = MibTableColumn
wfAppnNodeLsStatusDeactCause = _WfAppnNodeLsStatusDeactCause_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 46),
    _WfAppnNodeLsStatusDeactCause_Type()
)
wfAppnNodeLsStatusDeactCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusDeactCause.setStatus("mandatory")


class _WfAppnNodeLsStatusHprSupport_Type(Integer32):
    """Custom type wfAppnNodeLsStatusHprSupport based on Integer32"""
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


_WfAppnNodeLsStatusHprSupport_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusHprSupport_Object = MibTableColumn
wfAppnNodeLsStatusHprSupport = _WfAppnNodeLsStatusHprSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 47),
    _WfAppnNodeLsStatusHprSupport_Type()
)
wfAppnNodeLsStatusHprSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusHprSupport.setStatus("mandatory")


class _WfAppnNodeLsStatusHprLlErrSupport_Type(Integer32):
    """Custom type wfAppnNodeLsStatusHprLlErrSupport based on Integer32"""
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


_WfAppnNodeLsStatusHprLlErrSupport_Type.__name__ = "Integer32"
_WfAppnNodeLsStatusHprLlErrSupport_Object = MibTableColumn
wfAppnNodeLsStatusHprLlErrSupport = _WfAppnNodeLsStatusHprLlErrSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 48),
    _WfAppnNodeLsStatusHprLlErrSupport_Type()
)
wfAppnNodeLsStatusHprLlErrSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusHprLlErrSupport.setStatus("mandatory")
_WfAppnNodeLsStatusAnrLabel_Type = Integer32
_WfAppnNodeLsStatusAnrLabel_Object = MibTableColumn
wfAppnNodeLsStatusAnrLabel = _WfAppnNodeLsStatusAnrLabel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 49),
    _WfAppnNodeLsStatusAnrLabel_Type()
)
wfAppnNodeLsStatusAnrLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusAnrLabel.setStatus("mandatory")
_WfAppnNodeLsStatusLinkData_Type = OctetString
_WfAppnNodeLsStatusLinkData_Object = MibTableColumn
wfAppnNodeLsStatusLinkData = _WfAppnNodeLsStatusLinkData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 5, 1, 50),
    _WfAppnNodeLsStatusLinkData_Type()
)
wfAppnNodeLsStatusLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeLsStatusLinkData.setStatus("mandatory")
_WfAppnNodeCnTable_Object = MibTable
wfAppnNodeCnTable = _WfAppnNodeCnTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6)
)
if mibBuilder.loadTexts:
    wfAppnNodeCnTable.setStatus("mandatory")
_WfAppnNodeCnEntry_Object = MibTableRow
wfAppnNodeCnEntry = _WfAppnNodeCnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1)
)
wfAppnNodeCnEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeCnFqName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeCnEntry.setStatus("mandatory")


class _WfAppnNodeCnDelete_Type(Integer32):
    """Custom type wfAppnNodeCnDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnNodeCnDelete_Type.__name__ = "Integer32"
_WfAppnNodeCnDelete_Object = MibTableColumn
wfAppnNodeCnDelete = _WfAppnNodeCnDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 1),
    _WfAppnNodeCnDelete_Type()
)
wfAppnNodeCnDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnDelete.setStatus("mandatory")


class _WfAppnNodeCnDisable_Type(Integer32):
    """Custom type wfAppnNodeCnDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeCnDisable_Type.__name__ = "Integer32"
_WfAppnNodeCnDisable_Object = MibTableColumn
wfAppnNodeCnDisable = _WfAppnNodeCnDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 2),
    _WfAppnNodeCnDisable_Type()
)
wfAppnNodeCnDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnDisable.setStatus("mandatory")
_WfAppnNodeCnFqName_Type = DisplayString
_WfAppnNodeCnFqName_Object = MibTableColumn
wfAppnNodeCnFqName = _WfAppnNodeCnFqName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 3),
    _WfAppnNodeCnFqName_Type()
)
wfAppnNodeCnFqName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeCnFqName.setStatus("mandatory")


class _WfAppnNodeCnState_Type(Integer32):
    """Custom type wfAppnNodeCnState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_WfAppnNodeCnState_Type.__name__ = "Integer32"
_WfAppnNodeCnState_Object = MibTableColumn
wfAppnNodeCnState = _WfAppnNodeCnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 4),
    _WfAppnNodeCnState_Type()
)
wfAppnNodeCnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeCnState.setStatus("mandatory")


class _WfAppnNodeCnEffCap_Type(Integer32):
    """Custom type wfAppnNodeCnEffCap based on Integer32"""
    defaultValue = 133

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeCnEffCap_Type.__name__ = "Integer32"
_WfAppnNodeCnEffCap_Object = MibTableColumn
wfAppnNodeCnEffCap = _WfAppnNodeCnEffCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 5),
    _WfAppnNodeCnEffCap_Type()
)
wfAppnNodeCnEffCap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnEffCap.setStatus("mandatory")


class _WfAppnNodeCnConnCost_Type(Integer32):
    """Custom type wfAppnNodeCnConnCost based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeCnConnCost_Type.__name__ = "Integer32"
_WfAppnNodeCnConnCost_Object = MibTableColumn
wfAppnNodeCnConnCost = _WfAppnNodeCnConnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 6),
    _WfAppnNodeCnConnCost_Type()
)
wfAppnNodeCnConnCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnConnCost.setStatus("mandatory")


class _WfAppnNodeCnByteCost_Type(Integer32):
    """Custom type wfAppnNodeCnByteCost based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeCnByteCost_Type.__name__ = "Integer32"
_WfAppnNodeCnByteCost_Object = MibTableColumn
wfAppnNodeCnByteCost = _WfAppnNodeCnByteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 7),
    _WfAppnNodeCnByteCost_Type()
)
wfAppnNodeCnByteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnByteCost.setStatus("mandatory")


class _WfAppnNodeCnSecurity_Type(Integer32):
    """Custom type wfAppnNodeCnSecurity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeCnSecurity_Type.__name__ = "Integer32"
_WfAppnNodeCnSecurity_Object = MibTableColumn
wfAppnNodeCnSecurity = _WfAppnNodeCnSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 8),
    _WfAppnNodeCnSecurity_Type()
)
wfAppnNodeCnSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnSecurity.setStatus("mandatory")


class _WfAppnNodeCnDelay_Type(Integer32):
    """Custom type wfAppnNodeCnDelay based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnNodeCnDelay_Type.__name__ = "Integer32"
_WfAppnNodeCnDelay_Object = MibTableColumn
wfAppnNodeCnDelay = _WfAppnNodeCnDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 9),
    _WfAppnNodeCnDelay_Type()
)
wfAppnNodeCnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnDelay.setStatus("mandatory")


class _WfAppnNodeCnUsr1_Type(Integer32):
    """Custom type wfAppnNodeCnUsr1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeCnUsr1_Type.__name__ = "Integer32"
_WfAppnNodeCnUsr1_Object = MibTableColumn
wfAppnNodeCnUsr1 = _WfAppnNodeCnUsr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 10),
    _WfAppnNodeCnUsr1_Type()
)
wfAppnNodeCnUsr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnUsr1.setStatus("mandatory")


class _WfAppnNodeCnUsr2_Type(Integer32):
    """Custom type wfAppnNodeCnUsr2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeCnUsr2_Type.__name__ = "Integer32"
_WfAppnNodeCnUsr2_Object = MibTableColumn
wfAppnNodeCnUsr2 = _WfAppnNodeCnUsr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 11),
    _WfAppnNodeCnUsr2_Type()
)
wfAppnNodeCnUsr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnUsr2.setStatus("mandatory")


class _WfAppnNodeCnUsr3_Type(Integer32):
    """Custom type wfAppnNodeCnUsr3 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNodeCnUsr3_Type.__name__ = "Integer32"
_WfAppnNodeCnUsr3_Object = MibTableColumn
wfAppnNodeCnUsr3 = _WfAppnNodeCnUsr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 6, 1, 12),
    _WfAppnNodeCnUsr3_Type()
)
wfAppnNodeCnUsr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnUsr3.setStatus("mandatory")
_WfAppnNodeCnPortTable_Object = MibTable
wfAppnNodeCnPortTable = _WfAppnNodeCnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 7)
)
if mibBuilder.loadTexts:
    wfAppnNodeCnPortTable.setStatus("mandatory")
_WfAppnNodeCnPortEntry_Object = MibTableRow
wfAppnNodeCnPortEntry = _WfAppnNodeCnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 7, 1)
)
wfAppnNodeCnPortEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeCnPortCnName"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeCnPortPortName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeCnPortEntry.setStatus("mandatory")


class _WfAppnNodeCnPortDelete_Type(Integer32):
    """Custom type wfAppnNodeCnPortDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnNodeCnPortDelete_Type.__name__ = "Integer32"
_WfAppnNodeCnPortDelete_Object = MibTableColumn
wfAppnNodeCnPortDelete = _WfAppnNodeCnPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 7, 1, 1),
    _WfAppnNodeCnPortDelete_Type()
)
wfAppnNodeCnPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnPortDelete.setStatus("mandatory")


class _WfAppnNodeCnPortDisable_Type(Integer32):
    """Custom type wfAppnNodeCnPortDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeCnPortDisable_Type.__name__ = "Integer32"
_WfAppnNodeCnPortDisable_Object = MibTableColumn
wfAppnNodeCnPortDisable = _WfAppnNodeCnPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 7, 1, 2),
    _WfAppnNodeCnPortDisable_Type()
)
wfAppnNodeCnPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnPortDisable.setStatus("mandatory")
_WfAppnNodeCnPortCnName_Type = DisplayString
_WfAppnNodeCnPortCnName_Object = MibTableColumn
wfAppnNodeCnPortCnName = _WfAppnNodeCnPortCnName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 7, 1, 3),
    _WfAppnNodeCnPortCnName_Type()
)
wfAppnNodeCnPortCnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeCnPortCnName.setStatus("mandatory")
_WfAppnNodeCnPortPortName_Type = DisplayString
_WfAppnNodeCnPortPortName_Object = MibTableColumn
wfAppnNodeCnPortPortName = _WfAppnNodeCnPortPortName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 7, 1, 4),
    _WfAppnNodeCnPortPortName_Type()
)
wfAppnNodeCnPortPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeCnPortPortName.setStatus("mandatory")


class _WfAppnNodeCnPortState_Type(Integer32):
    """Custom type wfAppnNodeCnPortState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_WfAppnNodeCnPortState_Type.__name__ = "Integer32"
_WfAppnNodeCnPortState_Object = MibTableColumn
wfAppnNodeCnPortState = _WfAppnNodeCnPortState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 7, 1, 5),
    _WfAppnNodeCnPortState_Type()
)
wfAppnNodeCnPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeCnPortState.setStatus("mandatory")
_WfAppnNodeIsrSessionTable_Object = MibTable
wfAppnNodeIsrSessionTable = _WfAppnNodeIsrSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8)
)
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionTable.setStatus("mandatory")
_WfAppnNodeIsrSessionEntry_Object = MibTableRow
wfAppnNodeIsrSessionEntry = _WfAppnNodeIsrSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1)
)
wfAppnNodeIsrSessionEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeIsrSessionPcid"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeIsrSessionFqCpName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionEntry.setStatus("mandatory")
_WfAppnNodeIsrSessionPcid_Type = OctetString
_WfAppnNodeIsrSessionPcid_Object = MibTableColumn
wfAppnNodeIsrSessionPcid = _WfAppnNodeIsrSessionPcid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 1),
    _WfAppnNodeIsrSessionPcid_Type()
)
wfAppnNodeIsrSessionPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPcid.setStatus("mandatory")
_WfAppnNodeIsrSessionFqCpName_Type = DisplayString
_WfAppnNodeIsrSessionFqCpName_Object = MibTableColumn
wfAppnNodeIsrSessionFqCpName = _WfAppnNodeIsrSessionFqCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 2),
    _WfAppnNodeIsrSessionFqCpName_Type()
)
wfAppnNodeIsrSessionFqCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionFqCpName.setStatus("mandatory")


class _WfAppnNodeIsrSessionTransPriority_Type(Integer32):
    """Custom type wfAppnNodeIsrSessionTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_WfAppnNodeIsrSessionTransPriority_Type.__name__ = "Integer32"
_WfAppnNodeIsrSessionTransPriority_Object = MibTableColumn
wfAppnNodeIsrSessionTransPriority = _WfAppnNodeIsrSessionTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 3),
    _WfAppnNodeIsrSessionTransPriority_Type()
)
wfAppnNodeIsrSessionTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionTransPriority.setStatus("mandatory")
_WfAppnNodeIsrSessionCos_Type = DisplayString
_WfAppnNodeIsrSessionCos_Object = MibTableColumn
wfAppnNodeIsrSessionCos = _WfAppnNodeIsrSessionCos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 4),
    _WfAppnNodeIsrSessionCos_Type()
)
wfAppnNodeIsrSessionCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionCos.setStatus("mandatory")


class _WfAppnNodeIsrSessionLimResource_Type(Integer32):
    """Custom type wfAppnNodeIsrSessionLimResource based on Integer32"""
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


_WfAppnNodeIsrSessionLimResource_Type.__name__ = "Integer32"
_WfAppnNodeIsrSessionLimResource_Object = MibTableColumn
wfAppnNodeIsrSessionLimResource = _WfAppnNodeIsrSessionLimResource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 5),
    _WfAppnNodeIsrSessionLimResource_Type()
)
wfAppnNodeIsrSessionLimResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionLimResource.setStatus("mandatory")
_WfAppnNodeIsrSessionRscv_Type = OctetString
_WfAppnNodeIsrSessionRscv_Object = MibTableColumn
wfAppnNodeIsrSessionRscv = _WfAppnNodeIsrSessionRscv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 6),
    _WfAppnNodeIsrSessionRscv_Type()
)
wfAppnNodeIsrSessionRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionRscv.setStatus("mandatory")
_WfAppnNodeIsrSessionPriSendRuSize_Type = Integer32
_WfAppnNodeIsrSessionPriSendRuSize_Object = MibTableColumn
wfAppnNodeIsrSessionPriSendRuSize = _WfAppnNodeIsrSessionPriSendRuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 7),
    _WfAppnNodeIsrSessionPriSendRuSize_Type()
)
wfAppnNodeIsrSessionPriSendRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriSendRuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionPriRcvRuSize_Type = Integer32
_WfAppnNodeIsrSessionPriRcvRuSize_Object = MibTableColumn
wfAppnNodeIsrSessionPriRcvRuSize = _WfAppnNodeIsrSessionPriRcvRuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 8),
    _WfAppnNodeIsrSessionPriRcvRuSize_Type()
)
wfAppnNodeIsrSessionPriRcvRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriRcvRuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionPriMaxSendBtuSize_Type = Integer32
_WfAppnNodeIsrSessionPriMaxSendBtuSize_Object = MibTableColumn
wfAppnNodeIsrSessionPriMaxSendBtuSize = _WfAppnNodeIsrSessionPriMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 9),
    _WfAppnNodeIsrSessionPriMaxSendBtuSize_Type()
)
wfAppnNodeIsrSessionPriMaxSendBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriMaxSendBtuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionPriMaxRcvBtuSize_Type = Integer32
_WfAppnNodeIsrSessionPriMaxRcvBtuSize_Object = MibTableColumn
wfAppnNodeIsrSessionPriMaxRcvBtuSize = _WfAppnNodeIsrSessionPriMaxRcvBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 10),
    _WfAppnNodeIsrSessionPriMaxRcvBtuSize_Type()
)
wfAppnNodeIsrSessionPriMaxRcvBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriMaxRcvBtuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionPriMaxSendPacing_Type = Integer32
_WfAppnNodeIsrSessionPriMaxSendPacing_Object = MibTableColumn
wfAppnNodeIsrSessionPriMaxSendPacing = _WfAppnNodeIsrSessionPriMaxSendPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 11),
    _WfAppnNodeIsrSessionPriMaxSendPacing_Type()
)
wfAppnNodeIsrSessionPriMaxSendPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriMaxSendPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionPriCurSendPacing_Type = Integer32
_WfAppnNodeIsrSessionPriCurSendPacing_Object = MibTableColumn
wfAppnNodeIsrSessionPriCurSendPacing = _WfAppnNodeIsrSessionPriCurSendPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 12),
    _WfAppnNodeIsrSessionPriCurSendPacing_Type()
)
wfAppnNodeIsrSessionPriCurSendPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriCurSendPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionPriMaxRcvPacing_Type = Integer32
_WfAppnNodeIsrSessionPriMaxRcvPacing_Object = MibTableColumn
wfAppnNodeIsrSessionPriMaxRcvPacing = _WfAppnNodeIsrSessionPriMaxRcvPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 13),
    _WfAppnNodeIsrSessionPriMaxRcvPacing_Type()
)
wfAppnNodeIsrSessionPriMaxRcvPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriMaxRcvPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionPriCurRcvPacing_Type = Integer32
_WfAppnNodeIsrSessionPriCurRcvPacing_Object = MibTableColumn
wfAppnNodeIsrSessionPriCurRcvPacing = _WfAppnNodeIsrSessionPriCurRcvPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 14),
    _WfAppnNodeIsrSessionPriCurRcvPacing_Type()
)
wfAppnNodeIsrSessionPriCurRcvPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriCurRcvPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionPriSendFrames_Type = Counter32
_WfAppnNodeIsrSessionPriSendFrames_Object = MibTableColumn
wfAppnNodeIsrSessionPriSendFrames = _WfAppnNodeIsrSessionPriSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 15),
    _WfAppnNodeIsrSessionPriSendFrames_Type()
)
wfAppnNodeIsrSessionPriSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriSendFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionPriSendBytes_Type = Counter32
_WfAppnNodeIsrSessionPriSendBytes_Object = MibTableColumn
wfAppnNodeIsrSessionPriSendBytes = _WfAppnNodeIsrSessionPriSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 16),
    _WfAppnNodeIsrSessionPriSendBytes_Type()
)
wfAppnNodeIsrSessionPriSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriSendBytes.setStatus("mandatory")
_WfAppnNodeIsrSessionPriSendFmdFrames_Type = Counter32
_WfAppnNodeIsrSessionPriSendFmdFrames_Object = MibTableColumn
wfAppnNodeIsrSessionPriSendFmdFrames = _WfAppnNodeIsrSessionPriSendFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 17),
    _WfAppnNodeIsrSessionPriSendFmdFrames_Type()
)
wfAppnNodeIsrSessionPriSendFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriSendFmdFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionPriRcvFrames_Type = Counter32
_WfAppnNodeIsrSessionPriRcvFrames_Object = MibTableColumn
wfAppnNodeIsrSessionPriRcvFrames = _WfAppnNodeIsrSessionPriRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 18),
    _WfAppnNodeIsrSessionPriRcvFrames_Type()
)
wfAppnNodeIsrSessionPriRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriRcvFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionPriRcvBytes_Type = Counter32
_WfAppnNodeIsrSessionPriRcvBytes_Object = MibTableColumn
wfAppnNodeIsrSessionPriRcvBytes = _WfAppnNodeIsrSessionPriRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 19),
    _WfAppnNodeIsrSessionPriRcvBytes_Type()
)
wfAppnNodeIsrSessionPriRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriRcvBytes.setStatus("mandatory")
_WfAppnNodeIsrSessionPriRcvFmdFrames_Type = Counter32
_WfAppnNodeIsrSessionPriRcvFmdFrames_Object = MibTableColumn
wfAppnNodeIsrSessionPriRcvFmdFrames = _WfAppnNodeIsrSessionPriRcvFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 20),
    _WfAppnNodeIsrSessionPriRcvFmdFrames_Type()
)
wfAppnNodeIsrSessionPriRcvFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriRcvFmdFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionPriSidh_Type = Integer32
_WfAppnNodeIsrSessionPriSidh_Object = MibTableColumn
wfAppnNodeIsrSessionPriSidh = _WfAppnNodeIsrSessionPriSidh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 21),
    _WfAppnNodeIsrSessionPriSidh_Type()
)
wfAppnNodeIsrSessionPriSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriSidh.setStatus("mandatory")
_WfAppnNodeIsrSessionPriSidl_Type = Integer32
_WfAppnNodeIsrSessionPriSidl_Object = MibTableColumn
wfAppnNodeIsrSessionPriSidl = _WfAppnNodeIsrSessionPriSidl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 22),
    _WfAppnNodeIsrSessionPriSidl_Type()
)
wfAppnNodeIsrSessionPriSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriSidl.setStatus("mandatory")
_WfAppnNodeIsrSessionPriOdai_Type = Integer32
_WfAppnNodeIsrSessionPriOdai_Object = MibTableColumn
wfAppnNodeIsrSessionPriOdai = _WfAppnNodeIsrSessionPriOdai_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 23),
    _WfAppnNodeIsrSessionPriOdai_Type()
)
wfAppnNodeIsrSessionPriOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriOdai.setStatus("mandatory")
_WfAppnNodeIsrSessionPriLsName_Type = DisplayString
_WfAppnNodeIsrSessionPriLsName_Object = MibTableColumn
wfAppnNodeIsrSessionPriLsName = _WfAppnNodeIsrSessionPriLsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 24),
    _WfAppnNodeIsrSessionPriLsName_Type()
)
wfAppnNodeIsrSessionPriLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionPriLsName.setStatus("mandatory")
_WfAppnNodeIsrSessionSecSendRuSize_Type = Integer32
_WfAppnNodeIsrSessionSecSendRuSize_Object = MibTableColumn
wfAppnNodeIsrSessionSecSendRuSize = _WfAppnNodeIsrSessionSecSendRuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 25),
    _WfAppnNodeIsrSessionSecSendRuSize_Type()
)
wfAppnNodeIsrSessionSecSendRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecSendRuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionSecRcvRuSize_Type = Integer32
_WfAppnNodeIsrSessionSecRcvRuSize_Object = MibTableColumn
wfAppnNodeIsrSessionSecRcvRuSize = _WfAppnNodeIsrSessionSecRcvRuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 26),
    _WfAppnNodeIsrSessionSecRcvRuSize_Type()
)
wfAppnNodeIsrSessionSecRcvRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecRcvRuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionSecMaxSendBtuSize_Type = Integer32
_WfAppnNodeIsrSessionSecMaxSendBtuSize_Object = MibTableColumn
wfAppnNodeIsrSessionSecMaxSendBtuSize = _WfAppnNodeIsrSessionSecMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 27),
    _WfAppnNodeIsrSessionSecMaxSendBtuSize_Type()
)
wfAppnNodeIsrSessionSecMaxSendBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecMaxSendBtuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionSecMaxRcvBtuSize_Type = Integer32
_WfAppnNodeIsrSessionSecMaxRcvBtuSize_Object = MibTableColumn
wfAppnNodeIsrSessionSecMaxRcvBtuSize = _WfAppnNodeIsrSessionSecMaxRcvBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 28),
    _WfAppnNodeIsrSessionSecMaxRcvBtuSize_Type()
)
wfAppnNodeIsrSessionSecMaxRcvBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecMaxRcvBtuSize.setStatus("mandatory")
_WfAppnNodeIsrSessionSecMaxSendPacing_Type = Integer32
_WfAppnNodeIsrSessionSecMaxSendPacing_Object = MibTableColumn
wfAppnNodeIsrSessionSecMaxSendPacing = _WfAppnNodeIsrSessionSecMaxSendPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 29),
    _WfAppnNodeIsrSessionSecMaxSendPacing_Type()
)
wfAppnNodeIsrSessionSecMaxSendPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecMaxSendPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionSecCurSendPacing_Type = Integer32
_WfAppnNodeIsrSessionSecCurSendPacing_Object = MibTableColumn
wfAppnNodeIsrSessionSecCurSendPacing = _WfAppnNodeIsrSessionSecCurSendPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 30),
    _WfAppnNodeIsrSessionSecCurSendPacing_Type()
)
wfAppnNodeIsrSessionSecCurSendPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecCurSendPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionSecMaxRcvPacing_Type = Integer32
_WfAppnNodeIsrSessionSecMaxRcvPacing_Object = MibTableColumn
wfAppnNodeIsrSessionSecMaxRcvPacing = _WfAppnNodeIsrSessionSecMaxRcvPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 31),
    _WfAppnNodeIsrSessionSecMaxRcvPacing_Type()
)
wfAppnNodeIsrSessionSecMaxRcvPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecMaxRcvPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionSecCurRcvPacing_Type = Integer32
_WfAppnNodeIsrSessionSecCurRcvPacing_Object = MibTableColumn
wfAppnNodeIsrSessionSecCurRcvPacing = _WfAppnNodeIsrSessionSecCurRcvPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 32),
    _WfAppnNodeIsrSessionSecCurRcvPacing_Type()
)
wfAppnNodeIsrSessionSecCurRcvPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecCurRcvPacing.setStatus("mandatory")
_WfAppnNodeIsrSessionSecSendFrames_Type = Counter32
_WfAppnNodeIsrSessionSecSendFrames_Object = MibTableColumn
wfAppnNodeIsrSessionSecSendFrames = _WfAppnNodeIsrSessionSecSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 33),
    _WfAppnNodeIsrSessionSecSendFrames_Type()
)
wfAppnNodeIsrSessionSecSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecSendFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionSecSendBytes_Type = Counter32
_WfAppnNodeIsrSessionSecSendBytes_Object = MibTableColumn
wfAppnNodeIsrSessionSecSendBytes = _WfAppnNodeIsrSessionSecSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 34),
    _WfAppnNodeIsrSessionSecSendBytes_Type()
)
wfAppnNodeIsrSessionSecSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecSendBytes.setStatus("mandatory")
_WfAppnNodeIsrSessionSecSendFmdFrames_Type = Counter32
_WfAppnNodeIsrSessionSecSendFmdFrames_Object = MibTableColumn
wfAppnNodeIsrSessionSecSendFmdFrames = _WfAppnNodeIsrSessionSecSendFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 35),
    _WfAppnNodeIsrSessionSecSendFmdFrames_Type()
)
wfAppnNodeIsrSessionSecSendFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecSendFmdFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionSecRcvFrames_Type = Counter32
_WfAppnNodeIsrSessionSecRcvFrames_Object = MibTableColumn
wfAppnNodeIsrSessionSecRcvFrames = _WfAppnNodeIsrSessionSecRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 36),
    _WfAppnNodeIsrSessionSecRcvFrames_Type()
)
wfAppnNodeIsrSessionSecRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecRcvFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionSecRcvBytes_Type = Counter32
_WfAppnNodeIsrSessionSecRcvBytes_Object = MibTableColumn
wfAppnNodeIsrSessionSecRcvBytes = _WfAppnNodeIsrSessionSecRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 37),
    _WfAppnNodeIsrSessionSecRcvBytes_Type()
)
wfAppnNodeIsrSessionSecRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecRcvBytes.setStatus("mandatory")
_WfAppnNodeIsrSessionSecRcvFmdFrames_Type = Counter32
_WfAppnNodeIsrSessionSecRcvFmdFrames_Object = MibTableColumn
wfAppnNodeIsrSessionSecRcvFmdFrames = _WfAppnNodeIsrSessionSecRcvFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 38),
    _WfAppnNodeIsrSessionSecRcvFmdFrames_Type()
)
wfAppnNodeIsrSessionSecRcvFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecRcvFmdFrames.setStatus("mandatory")
_WfAppnNodeIsrSessionSecSidh_Type = Integer32
_WfAppnNodeIsrSessionSecSidh_Object = MibTableColumn
wfAppnNodeIsrSessionSecSidh = _WfAppnNodeIsrSessionSecSidh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 39),
    _WfAppnNodeIsrSessionSecSidh_Type()
)
wfAppnNodeIsrSessionSecSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecSidh.setStatus("mandatory")
_WfAppnNodeIsrSessionSecSidl_Type = Integer32
_WfAppnNodeIsrSessionSecSidl_Object = MibTableColumn
wfAppnNodeIsrSessionSecSidl = _WfAppnNodeIsrSessionSecSidl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 40),
    _WfAppnNodeIsrSessionSecSidl_Type()
)
wfAppnNodeIsrSessionSecSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecSidl.setStatus("mandatory")
_WfAppnNodeIsrSessionSecOdai_Type = Integer32
_WfAppnNodeIsrSessionSecOdai_Object = MibTableColumn
wfAppnNodeIsrSessionSecOdai = _WfAppnNodeIsrSessionSecOdai_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 41),
    _WfAppnNodeIsrSessionSecOdai_Type()
)
wfAppnNodeIsrSessionSecOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecOdai.setStatus("mandatory")
_WfAppnNodeIsrSessionSecLsName_Type = DisplayString
_WfAppnNodeIsrSessionSecLsName_Object = MibTableColumn
wfAppnNodeIsrSessionSecLsName = _WfAppnNodeIsrSessionSecLsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 42),
    _WfAppnNodeIsrSessionSecLsName_Type()
)
wfAppnNodeIsrSessionSecLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionSecLsName.setStatus("mandatory")
_WfAppnNodeIsrSessionRscvText_Type = DisplayString
_WfAppnNodeIsrSessionRscvText_Object = MibTableColumn
wfAppnNodeIsrSessionRscvText = _WfAppnNodeIsrSessionRscvText_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 8, 1, 43),
    _WfAppnNodeIsrSessionRscvText_Type()
)
wfAppnNodeIsrSessionRscvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeIsrSessionRscvText.setStatus("mandatory")
_WfAppnNodeEndptSessionTable_Object = MibTable
wfAppnNodeEndptSessionTable = _WfAppnNodeEndptSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9)
)
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionTable.setStatus("mandatory")
_WfAppnNodeEndptSessionEntry_Object = MibTableRow
wfAppnNodeEndptSessionEntry = _WfAppnNodeEndptSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1)
)
wfAppnNodeEndptSessionEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeEndptSessionId"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeEndptSessionFqPluName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionEntry.setStatus("mandatory")
_WfAppnNodeEndptSessionId_Type = OctetString
_WfAppnNodeEndptSessionId_Object = MibTableColumn
wfAppnNodeEndptSessionId = _WfAppnNodeEndptSessionId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 1),
    _WfAppnNodeEndptSessionId_Type()
)
wfAppnNodeEndptSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionId.setStatus("mandatory")
_WfAppnNodeEndptSessionPcid_Type = OctetString
_WfAppnNodeEndptSessionPcid_Object = MibTableColumn
wfAppnNodeEndptSessionPcid = _WfAppnNodeEndptSessionPcid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 2),
    _WfAppnNodeEndptSessionPcid_Type()
)
wfAppnNodeEndptSessionPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionPcid.setStatus("mandatory")
_WfAppnNodeEndptSessionFqCpName_Type = DisplayString
_WfAppnNodeEndptSessionFqCpName_Object = MibTableColumn
wfAppnNodeEndptSessionFqCpName = _WfAppnNodeEndptSessionFqCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 3),
    _WfAppnNodeEndptSessionFqCpName_Type()
)
wfAppnNodeEndptSessionFqCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionFqCpName.setStatus("mandatory")
_WfAppnNodeEndptSessionFqPluName_Type = DisplayString
_WfAppnNodeEndptSessionFqPluName_Object = MibTableColumn
wfAppnNodeEndptSessionFqPluName = _WfAppnNodeEndptSessionFqPluName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 4),
    _WfAppnNodeEndptSessionFqPluName_Type()
)
wfAppnNodeEndptSessionFqPluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionFqPluName.setStatus("mandatory")


class _WfAppnNodeEndptSessionTransPriority_Type(Integer32):
    """Custom type wfAppnNodeEndptSessionTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_WfAppnNodeEndptSessionTransPriority_Type.__name__ = "Integer32"
_WfAppnNodeEndptSessionTransPriority_Object = MibTableColumn
wfAppnNodeEndptSessionTransPriority = _WfAppnNodeEndptSessionTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 5),
    _WfAppnNodeEndptSessionTransPriority_Type()
)
wfAppnNodeEndptSessionTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionTransPriority.setStatus("mandatory")
_WfAppnNodeEndptSessionMode_Type = DisplayString
_WfAppnNodeEndptSessionMode_Object = MibTableColumn
wfAppnNodeEndptSessionMode = _WfAppnNodeEndptSessionMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 6),
    _WfAppnNodeEndptSessionMode_Type()
)
wfAppnNodeEndptSessionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionMode.setStatus("mandatory")
_WfAppnNodeEndptSessionCos_Type = DisplayString
_WfAppnNodeEndptSessionCos_Object = MibTableColumn
wfAppnNodeEndptSessionCos = _WfAppnNodeEndptSessionCos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 7),
    _WfAppnNodeEndptSessionCos_Type()
)
wfAppnNodeEndptSessionCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionCos.setStatus("mandatory")


class _WfAppnNodeEndptSessionLimResource_Type(Integer32):
    """Custom type wfAppnNodeEndptSessionLimResource based on Integer32"""
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


_WfAppnNodeEndptSessionLimResource_Type.__name__ = "Integer32"
_WfAppnNodeEndptSessionLimResource_Object = MibTableColumn
wfAppnNodeEndptSessionLimResource = _WfAppnNodeEndptSessionLimResource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 8),
    _WfAppnNodeEndptSessionLimResource_Type()
)
wfAppnNodeEndptSessionLimResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionLimResource.setStatus("mandatory")


class _WfAppnNodeEndptSessionPolarity_Type(Integer32):
    """Custom type wfAppnNodeEndptSessionPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_WfAppnNodeEndptSessionPolarity_Type.__name__ = "Integer32"
_WfAppnNodeEndptSessionPolarity_Object = MibTableColumn
wfAppnNodeEndptSessionPolarity = _WfAppnNodeEndptSessionPolarity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 9),
    _WfAppnNodeEndptSessionPolarity_Type()
)
wfAppnNodeEndptSessionPolarity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionPolarity.setStatus("mandatory")


class _WfAppnNodeEndptSessionContention_Type(Integer32):
    """Custom type wfAppnNodeEndptSessionContention based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("conloser", 2),
          ("conwinner", 1))
    )


_WfAppnNodeEndptSessionContention_Type.__name__ = "Integer32"
_WfAppnNodeEndptSessionContention_Object = MibTableColumn
wfAppnNodeEndptSessionContention = _WfAppnNodeEndptSessionContention_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 10),
    _WfAppnNodeEndptSessionContention_Type()
)
wfAppnNodeEndptSessionContention.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionContention.setStatus("mandatory")
_WfAppnNodeEndptSessionRscv_Type = OctetString
_WfAppnNodeEndptSessionRscv_Object = MibTableColumn
wfAppnNodeEndptSessionRscv = _WfAppnNodeEndptSessionRscv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 11),
    _WfAppnNodeEndptSessionRscv_Type()
)
wfAppnNodeEndptSessionRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionRscv.setStatus("mandatory")
_WfAppnNodeEndptSessionSendRuSize_Type = Integer32
_WfAppnNodeEndptSessionSendRuSize_Object = MibTableColumn
wfAppnNodeEndptSessionSendRuSize = _WfAppnNodeEndptSessionSendRuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 12),
    _WfAppnNodeEndptSessionSendRuSize_Type()
)
wfAppnNodeEndptSessionSendRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionSendRuSize.setStatus("mandatory")
_WfAppnNodeEndptSessionRcvRuSize_Type = Integer32
_WfAppnNodeEndptSessionRcvRuSize_Object = MibTableColumn
wfAppnNodeEndptSessionRcvRuSize = _WfAppnNodeEndptSessionRcvRuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 13),
    _WfAppnNodeEndptSessionRcvRuSize_Type()
)
wfAppnNodeEndptSessionRcvRuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionRcvRuSize.setStatus("mandatory")
_WfAppnNodeEndptSessionMaxSendBtuSize_Type = Integer32
_WfAppnNodeEndptSessionMaxSendBtuSize_Object = MibTableColumn
wfAppnNodeEndptSessionMaxSendBtuSize = _WfAppnNodeEndptSessionMaxSendBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 14),
    _WfAppnNodeEndptSessionMaxSendBtuSize_Type()
)
wfAppnNodeEndptSessionMaxSendBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionMaxSendBtuSize.setStatus("mandatory")
_WfAppnNodeEndptSessionMaxRcvBtuSize_Type = Integer32
_WfAppnNodeEndptSessionMaxRcvBtuSize_Object = MibTableColumn
wfAppnNodeEndptSessionMaxRcvBtuSize = _WfAppnNodeEndptSessionMaxRcvBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 15),
    _WfAppnNodeEndptSessionMaxRcvBtuSize_Type()
)
wfAppnNodeEndptSessionMaxRcvBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionMaxRcvBtuSize.setStatus("mandatory")
_WfAppnNodeEndptSessionMaxSendPacing_Type = Integer32
_WfAppnNodeEndptSessionMaxSendPacing_Object = MibTableColumn
wfAppnNodeEndptSessionMaxSendPacing = _WfAppnNodeEndptSessionMaxSendPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 16),
    _WfAppnNodeEndptSessionMaxSendPacing_Type()
)
wfAppnNodeEndptSessionMaxSendPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionMaxSendPacing.setStatus("mandatory")
_WfAppnNodeEndptSessionCurSendPacing_Type = Integer32
_WfAppnNodeEndptSessionCurSendPacing_Object = MibTableColumn
wfAppnNodeEndptSessionCurSendPacing = _WfAppnNodeEndptSessionCurSendPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 17),
    _WfAppnNodeEndptSessionCurSendPacing_Type()
)
wfAppnNodeEndptSessionCurSendPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionCurSendPacing.setStatus("mandatory")
_WfAppnNodeEndptSessionMaxRcvPacing_Type = Integer32
_WfAppnNodeEndptSessionMaxRcvPacing_Object = MibTableColumn
wfAppnNodeEndptSessionMaxRcvPacing = _WfAppnNodeEndptSessionMaxRcvPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 18),
    _WfAppnNodeEndptSessionMaxRcvPacing_Type()
)
wfAppnNodeEndptSessionMaxRcvPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionMaxRcvPacing.setStatus("mandatory")
_WfAppnNodeEndptSessionCurRcvPacing_Type = Integer32
_WfAppnNodeEndptSessionCurRcvPacing_Object = MibTableColumn
wfAppnNodeEndptSessionCurRcvPacing = _WfAppnNodeEndptSessionCurRcvPacing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 19),
    _WfAppnNodeEndptSessionCurRcvPacing_Type()
)
wfAppnNodeEndptSessionCurRcvPacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionCurRcvPacing.setStatus("mandatory")
_WfAppnNodeEndptSessionSendFrames_Type = Counter32
_WfAppnNodeEndptSessionSendFrames_Object = MibTableColumn
wfAppnNodeEndptSessionSendFrames = _WfAppnNodeEndptSessionSendFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 20),
    _WfAppnNodeEndptSessionSendFrames_Type()
)
wfAppnNodeEndptSessionSendFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionSendFrames.setStatus("mandatory")
_WfAppnNodeEndptSessionSendBytes_Type = Counter32
_WfAppnNodeEndptSessionSendBytes_Object = MibTableColumn
wfAppnNodeEndptSessionSendBytes = _WfAppnNodeEndptSessionSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 21),
    _WfAppnNodeEndptSessionSendBytes_Type()
)
wfAppnNodeEndptSessionSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionSendBytes.setStatus("mandatory")
_WfAppnNodeEndptSessionSendFmdFrames_Type = Counter32
_WfAppnNodeEndptSessionSendFmdFrames_Object = MibTableColumn
wfAppnNodeEndptSessionSendFmdFrames = _WfAppnNodeEndptSessionSendFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 22),
    _WfAppnNodeEndptSessionSendFmdFrames_Type()
)
wfAppnNodeEndptSessionSendFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionSendFmdFrames.setStatus("mandatory")
_WfAppnNodeEndptSessionRcvFrames_Type = Counter32
_WfAppnNodeEndptSessionRcvFrames_Object = MibTableColumn
wfAppnNodeEndptSessionRcvFrames = _WfAppnNodeEndptSessionRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 23),
    _WfAppnNodeEndptSessionRcvFrames_Type()
)
wfAppnNodeEndptSessionRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionRcvFrames.setStatus("mandatory")
_WfAppnNodeEndptSessionRcvBytes_Type = Counter32
_WfAppnNodeEndptSessionRcvBytes_Object = MibTableColumn
wfAppnNodeEndptSessionRcvBytes = _WfAppnNodeEndptSessionRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 24),
    _WfAppnNodeEndptSessionRcvBytes_Type()
)
wfAppnNodeEndptSessionRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionRcvBytes.setStatus("mandatory")
_WfAppnNodeEndptSessionRcvFmdFrames_Type = Counter32
_WfAppnNodeEndptSessionRcvFmdFrames_Object = MibTableColumn
wfAppnNodeEndptSessionRcvFmdFrames = _WfAppnNodeEndptSessionRcvFmdFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 25),
    _WfAppnNodeEndptSessionRcvFmdFrames_Type()
)
wfAppnNodeEndptSessionRcvFmdFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionRcvFmdFrames.setStatus("mandatory")
_WfAppnNodeEndptSessionSidh_Type = Integer32
_WfAppnNodeEndptSessionSidh_Object = MibTableColumn
wfAppnNodeEndptSessionSidh = _WfAppnNodeEndptSessionSidh_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 26),
    _WfAppnNodeEndptSessionSidh_Type()
)
wfAppnNodeEndptSessionSidh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionSidh.setStatus("mandatory")
_WfAppnNodeEndptSessionSidl_Type = Integer32
_WfAppnNodeEndptSessionSidl_Object = MibTableColumn
wfAppnNodeEndptSessionSidl = _WfAppnNodeEndptSessionSidl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 27),
    _WfAppnNodeEndptSessionSidl_Type()
)
wfAppnNodeEndptSessionSidl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionSidl.setStatus("mandatory")
_WfAppnNodeEndptSessionOdai_Type = Integer32
_WfAppnNodeEndptSessionOdai_Object = MibTableColumn
wfAppnNodeEndptSessionOdai = _WfAppnNodeEndptSessionOdai_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 28),
    _WfAppnNodeEndptSessionOdai_Type()
)
wfAppnNodeEndptSessionOdai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionOdai.setStatus("mandatory")
_WfAppnNodeEndptSessionLsName_Type = DisplayString
_WfAppnNodeEndptSessionLsName_Object = MibTableColumn
wfAppnNodeEndptSessionLsName = _WfAppnNodeEndptSessionLsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 29),
    _WfAppnNodeEndptSessionLsName_Type()
)
wfAppnNodeEndptSessionLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionLsName.setStatus("mandatory")
_WfAppnNodeEndptSessionRscvText_Type = DisplayString
_WfAppnNodeEndptSessionRscvText_Object = MibTableColumn
wfAppnNodeEndptSessionRscvText = _WfAppnNodeEndptSessionRscvText_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 9, 1, 30),
    _WfAppnNodeEndptSessionRscvText_Type()
)
wfAppnNodeEndptSessionRscvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeEndptSessionRscvText.setStatus("mandatory")
_WfAppnNodeTraceGroup_ObjectIdentity = ObjectIdentity
wfAppnNodeTraceGroup = _WfAppnNodeTraceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 10)
)


class _WfAppnNodeTraceDelete_Type(Integer32):
    """Custom type wfAppnNodeTraceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnNodeTraceDelete_Type.__name__ = "Integer32"
_WfAppnNodeTraceDelete_Object = MibScalar
wfAppnNodeTraceDelete = _WfAppnNodeTraceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 10, 1),
    _WfAppnNodeTraceDelete_Type()
)
wfAppnNodeTraceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeTraceDelete.setStatus("mandatory")


class _WfAppnNodeTraceDisable_Type(Integer32):
    """Custom type wfAppnNodeTraceDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnNodeTraceDisable_Type.__name__ = "Integer32"
_WfAppnNodeTraceDisable_Object = MibScalar
wfAppnNodeTraceDisable = _WfAppnNodeTraceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 10, 2),
    _WfAppnNodeTraceDisable_Type()
)
wfAppnNodeTraceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeTraceDisable.setStatus("mandatory")
_WfAppnNodeTraceFile_Type = DisplayString
_WfAppnNodeTraceFile_Object = MibScalar
wfAppnNodeTraceFile = _WfAppnNodeTraceFile_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 10, 3),
    _WfAppnNodeTraceFile_Type()
)
wfAppnNodeTraceFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNodeTraceFile.setStatus("mandatory")
_WfAppnNodeRtpConnectionTable_Object = MibTable
wfAppnNodeRtpConnectionTable = _WfAppnNodeRtpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11)
)
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionTable.setStatus("mandatory")
_WfAppnNodeRtpConnectionEntry_Object = MibTableRow
wfAppnNodeRtpConnectionEntry = _WfAppnNodeRtpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1)
)
wfAppnNodeRtpConnectionEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNodeRtpConnectionName"),
)
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionEntry.setStatus("mandatory")
_WfAppnNodeRtpConnectionName_Type = DisplayString
_WfAppnNodeRtpConnectionName_Object = MibTableColumn
wfAppnNodeRtpConnectionName = _WfAppnNodeRtpConnectionName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 1),
    _WfAppnNodeRtpConnectionName_Type()
)
wfAppnNodeRtpConnectionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionName.setStatus("mandatory")
_WfAppnNodeRtpConnectionDestName_Type = DisplayString
_WfAppnNodeRtpConnectionDestName_Object = MibTableColumn
wfAppnNodeRtpConnectionDestName = _WfAppnNodeRtpConnectionDestName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 2),
    _WfAppnNodeRtpConnectionDestName_Type()
)
wfAppnNodeRtpConnectionDestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionDestName.setStatus("mandatory")
_WfAppnNodeRtpConnectionFirstHopLsName_Type = DisplayString
_WfAppnNodeRtpConnectionFirstHopLsName_Object = MibTableColumn
wfAppnNodeRtpConnectionFirstHopLsName = _WfAppnNodeRtpConnectionFirstHopLsName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 3),
    _WfAppnNodeRtpConnectionFirstHopLsName_Type()
)
wfAppnNodeRtpConnectionFirstHopLsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionFirstHopLsName.setStatus("mandatory")
_WfAppnNodeRtpConnectionCosName_Type = DisplayString
_WfAppnNodeRtpConnectionCosName_Object = MibTableColumn
wfAppnNodeRtpConnectionCosName = _WfAppnNodeRtpConnectionCosName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 4),
    _WfAppnNodeRtpConnectionCosName_Type()
)
wfAppnNodeRtpConnectionCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionCosName.setStatus("mandatory")
_WfAppnNodeRtpConnectionMaxBtuSize_Type = Integer32
_WfAppnNodeRtpConnectionMaxBtuSize_Object = MibTableColumn
wfAppnNodeRtpConnectionMaxBtuSize = _WfAppnNodeRtpConnectionMaxBtuSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 5),
    _WfAppnNodeRtpConnectionMaxBtuSize_Type()
)
wfAppnNodeRtpConnectionMaxBtuSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionMaxBtuSize.setStatus("mandatory")
_WfAppnNodeRtpConnectionLivenessTimer_Type = Integer32
_WfAppnNodeRtpConnectionLivenessTimer_Object = MibTableColumn
wfAppnNodeRtpConnectionLivenessTimer = _WfAppnNodeRtpConnectionLivenessTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 6),
    _WfAppnNodeRtpConnectionLivenessTimer_Type()
)
wfAppnNodeRtpConnectionLivenessTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionLivenessTimer.setStatus("mandatory")
_WfAppnNodeRtpConnectionLivenessTimeouts_Type = Counter32
_WfAppnNodeRtpConnectionLivenessTimeouts_Object = MibTableColumn
wfAppnNodeRtpConnectionLivenessTimeouts = _WfAppnNodeRtpConnectionLivenessTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 7),
    _WfAppnNodeRtpConnectionLivenessTimeouts_Type()
)
wfAppnNodeRtpConnectionLivenessTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionLivenessTimeouts.setStatus("mandatory")
_WfAppnNodeRtpConnectionLocalTcid_Type = OctetString
_WfAppnNodeRtpConnectionLocalTcid_Object = MibTableColumn
wfAppnNodeRtpConnectionLocalTcid = _WfAppnNodeRtpConnectionLocalTcid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 8),
    _WfAppnNodeRtpConnectionLocalTcid_Type()
)
wfAppnNodeRtpConnectionLocalTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionLocalTcid.setStatus("mandatory")
_WfAppnNodeRtpConnectionRemoteTcid_Type = OctetString
_WfAppnNodeRtpConnectionRemoteTcid_Object = MibTableColumn
wfAppnNodeRtpConnectionRemoteTcid = _WfAppnNodeRtpConnectionRemoteTcid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 9),
    _WfAppnNodeRtpConnectionRemoteTcid_Type()
)
wfAppnNodeRtpConnectionRemoteTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRemoteTcid.setStatus("mandatory")
_WfAppnNodeRtpConnectionActiveSessions_Type = Integer32
_WfAppnNodeRtpConnectionActiveSessions_Object = MibTableColumn
wfAppnNodeRtpConnectionActiveSessions = _WfAppnNodeRtpConnectionActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 10),
    _WfAppnNodeRtpConnectionActiveSessions_Type()
)
wfAppnNodeRtpConnectionActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionActiveSessions.setStatus("mandatory")
_WfAppnNodeRtpConnectionSendBytes_Type = Counter32
_WfAppnNodeRtpConnectionSendBytes_Object = MibTableColumn
wfAppnNodeRtpConnectionSendBytes = _WfAppnNodeRtpConnectionSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 11),
    _WfAppnNodeRtpConnectionSendBytes_Type()
)
wfAppnNodeRtpConnectionSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionSendBytes.setStatus("mandatory")
_WfAppnNodeRtpConnectionSendPackets_Type = Counter32
_WfAppnNodeRtpConnectionSendPackets_Object = MibTableColumn
wfAppnNodeRtpConnectionSendPackets = _WfAppnNodeRtpConnectionSendPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 12),
    _WfAppnNodeRtpConnectionSendPackets_Type()
)
wfAppnNodeRtpConnectionSendPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionSendPackets.setStatus("mandatory")
_WfAppnNodeRtpConnectionSendSessionControlFrames_Type = Counter32
_WfAppnNodeRtpConnectionSendSessionControlFrames_Object = MibTableColumn
wfAppnNodeRtpConnectionSendSessionControlFrames = _WfAppnNodeRtpConnectionSendSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 13),
    _WfAppnNodeRtpConnectionSendSessionControlFrames_Type()
)
wfAppnNodeRtpConnectionSendSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionSendSessionControlFrames.setStatus("mandatory")
_WfAppnNodeRtpConnectionSendRate_Type = Gauge32
_WfAppnNodeRtpConnectionSendRate_Object = MibTableColumn
wfAppnNodeRtpConnectionSendRate = _WfAppnNodeRtpConnectionSendRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 14),
    _WfAppnNodeRtpConnectionSendRate_Type()
)
wfAppnNodeRtpConnectionSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionSendRate.setStatus("mandatory")
_WfAppnNodeRtpConnectionMaxSendRate_Type = Integer32
_WfAppnNodeRtpConnectionMaxSendRate_Object = MibTableColumn
wfAppnNodeRtpConnectionMaxSendRate = _WfAppnNodeRtpConnectionMaxSendRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 15),
    _WfAppnNodeRtpConnectionMaxSendRate_Type()
)
wfAppnNodeRtpConnectionMaxSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionMaxSendRate.setStatus("mandatory")
_WfAppnNodeRtpConnectionMinSendRate_Type = Integer32
_WfAppnNodeRtpConnectionMinSendRate_Object = MibTableColumn
wfAppnNodeRtpConnectionMinSendRate = _WfAppnNodeRtpConnectionMinSendRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 16),
    _WfAppnNodeRtpConnectionMinSendRate_Type()
)
wfAppnNodeRtpConnectionMinSendRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionMinSendRate.setStatus("mandatory")
_WfAppnNodeRtpConnectionRcvBytes_Type = Counter32
_WfAppnNodeRtpConnectionRcvBytes_Object = MibTableColumn
wfAppnNodeRtpConnectionRcvBytes = _WfAppnNodeRtpConnectionRcvBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 17),
    _WfAppnNodeRtpConnectionRcvBytes_Type()
)
wfAppnNodeRtpConnectionRcvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRcvBytes.setStatus("mandatory")
_WfAppnNodeRtpConnectionRcvPackets_Type = Counter32
_WfAppnNodeRtpConnectionRcvPackets_Object = MibTableColumn
wfAppnNodeRtpConnectionRcvPackets = _WfAppnNodeRtpConnectionRcvPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 18),
    _WfAppnNodeRtpConnectionRcvPackets_Type()
)
wfAppnNodeRtpConnectionRcvPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRcvPackets.setStatus("mandatory")
_WfAppnNodeRtpConnectionRcvSessionControlFrames_Type = Counter32
_WfAppnNodeRtpConnectionRcvSessionControlFrames_Object = MibTableColumn
wfAppnNodeRtpConnectionRcvSessionControlFrames = _WfAppnNodeRtpConnectionRcvSessionControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 19),
    _WfAppnNodeRtpConnectionRcvSessionControlFrames_Type()
)
wfAppnNodeRtpConnectionRcvSessionControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRcvSessionControlFrames.setStatus("mandatory")
_WfAppnNodeRtpConnectionRcvInvalidSnaFrames_Type = Counter32
_WfAppnNodeRtpConnectionRcvInvalidSnaFrames_Object = MibTableColumn
wfAppnNodeRtpConnectionRcvInvalidSnaFrames = _WfAppnNodeRtpConnectionRcvInvalidSnaFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 20),
    _WfAppnNodeRtpConnectionRcvInvalidSnaFrames_Type()
)
wfAppnNodeRtpConnectionRcvInvalidSnaFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRcvInvalidSnaFrames.setStatus("mandatory")
_WfAppnNodeRtpConnectionRcvRate_Type = Gauge32
_WfAppnNodeRtpConnectionRcvRate_Object = MibTableColumn
wfAppnNodeRtpConnectionRcvRate = _WfAppnNodeRtpConnectionRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 21),
    _WfAppnNodeRtpConnectionRcvRate_Type()
)
wfAppnNodeRtpConnectionRcvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRcvRate.setStatus("mandatory")
_WfAppnNodeRtpConnectionMaxRcvRate_Type = Integer32
_WfAppnNodeRtpConnectionMaxRcvRate_Object = MibTableColumn
wfAppnNodeRtpConnectionMaxRcvRate = _WfAppnNodeRtpConnectionMaxRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 22),
    _WfAppnNodeRtpConnectionMaxRcvRate_Type()
)
wfAppnNodeRtpConnectionMaxRcvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionMaxRcvRate.setStatus("mandatory")
_WfAppnNodeRtpConnectionMinRcvRate_Type = Integer32
_WfAppnNodeRtpConnectionMinRcvRate_Object = MibTableColumn
wfAppnNodeRtpConnectionMinRcvRate = _WfAppnNodeRtpConnectionMinRcvRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 23),
    _WfAppnNodeRtpConnectionMinRcvRate_Type()
)
wfAppnNodeRtpConnectionMinRcvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionMinRcvRate.setStatus("mandatory")
_WfAppnNodeRtpConnectionDiscardedBytes_Type = Counter32
_WfAppnNodeRtpConnectionDiscardedBytes_Object = MibTableColumn
wfAppnNodeRtpConnectionDiscardedBytes = _WfAppnNodeRtpConnectionDiscardedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 24),
    _WfAppnNodeRtpConnectionDiscardedBytes_Type()
)
wfAppnNodeRtpConnectionDiscardedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionDiscardedBytes.setStatus("mandatory")
_WfAppnNodeRtpConnectionDiscardedPackets_Type = Counter32
_WfAppnNodeRtpConnectionDiscardedPackets_Object = MibTableColumn
wfAppnNodeRtpConnectionDiscardedPackets = _WfAppnNodeRtpConnectionDiscardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 25),
    _WfAppnNodeRtpConnectionDiscardedPackets_Type()
)
wfAppnNodeRtpConnectionDiscardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionDiscardedPackets.setStatus("mandatory")
_WfAppnNodeRtpConnectionResentBytes_Type = Counter32
_WfAppnNodeRtpConnectionResentBytes_Object = MibTableColumn
wfAppnNodeRtpConnectionResentBytes = _WfAppnNodeRtpConnectionResentBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 26),
    _WfAppnNodeRtpConnectionResentBytes_Type()
)
wfAppnNodeRtpConnectionResentBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionResentBytes.setStatus("mandatory")
_WfAppnNodeRtpConnectionResentPackets_Type = Counter32
_WfAppnNodeRtpConnectionResentPackets_Object = MibTableColumn
wfAppnNodeRtpConnectionResentPackets = _WfAppnNodeRtpConnectionResentPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 27),
    _WfAppnNodeRtpConnectionResentPackets_Type()
)
wfAppnNodeRtpConnectionResentPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionResentPackets.setStatus("mandatory")
_WfAppnNodeRtpConnectionUpTime_Type = Integer32
_WfAppnNodeRtpConnectionUpTime_Object = MibTableColumn
wfAppnNodeRtpConnectionUpTime = _WfAppnNodeRtpConnectionUpTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 28),
    _WfAppnNodeRtpConnectionUpTime_Type()
)
wfAppnNodeRtpConnectionUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionUpTime.setStatus("mandatory")
_WfAppnNodeRtpConnectionRoundTripTime_Type = Integer32
_WfAppnNodeRtpConnectionRoundTripTime_Object = MibTableColumn
wfAppnNodeRtpConnectionRoundTripTime = _WfAppnNodeRtpConnectionRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 29),
    _WfAppnNodeRtpConnectionRoundTripTime_Type()
)
wfAppnNodeRtpConnectionRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRoundTripTime.setStatus("mandatory")
_WfAppnNodeRtpConnectionSmoothRoundTripTime_Type = Integer32
_WfAppnNodeRtpConnectionSmoothRoundTripTime_Object = MibTableColumn
wfAppnNodeRtpConnectionSmoothRoundTripTime = _WfAppnNodeRtpConnectionSmoothRoundTripTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 30),
    _WfAppnNodeRtpConnectionSmoothRoundTripTime_Type()
)
wfAppnNodeRtpConnectionSmoothRoundTripTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionSmoothRoundTripTime.setStatus("mandatory")
_WfAppnNodeRtpConnectionBurstSize_Type = Integer32
_WfAppnNodeRtpConnectionBurstSize_Object = MibTableColumn
wfAppnNodeRtpConnectionBurstSize = _WfAppnNodeRtpConnectionBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 31),
    _WfAppnNodeRtpConnectionBurstSize_Type()
)
wfAppnNodeRtpConnectionBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionBurstSize.setStatus("mandatory")
_WfAppnNodeRtpConnectionSrtExpiries_Type = Counter32
_WfAppnNodeRtpConnectionSrtExpiries_Object = MibTableColumn
wfAppnNodeRtpConnectionSrtExpiries = _WfAppnNodeRtpConnectionSrtExpiries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 32),
    _WfAppnNodeRtpConnectionSrtExpiries_Type()
)
wfAppnNodeRtpConnectionSrtExpiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionSrtExpiries.setStatus("mandatory")
_WfAppnNodeRtpConnectionShortReqTimer_Type = Integer32
_WfAppnNodeRtpConnectionShortReqTimer_Object = MibTableColumn
wfAppnNodeRtpConnectionShortReqTimer = _WfAppnNodeRtpConnectionShortReqTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 33),
    _WfAppnNodeRtpConnectionShortReqTimer_Type()
)
wfAppnNodeRtpConnectionShortReqTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionShortReqTimer.setStatus("mandatory")
_WfAppnNodeRtpConnectionGapsDetected_Type = Counter32
_WfAppnNodeRtpConnectionGapsDetected_Object = MibTableColumn
wfAppnNodeRtpConnectionGapsDetected = _WfAppnNodeRtpConnectionGapsDetected_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 34),
    _WfAppnNodeRtpConnectionGapsDetected_Type()
)
wfAppnNodeRtpConnectionGapsDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionGapsDetected.setStatus("mandatory")
_WfAppnNodeRtpConnectionRscv_Type = OctetString
_WfAppnNodeRtpConnectionRscv_Object = MibTableColumn
wfAppnNodeRtpConnectionRscv = _WfAppnNodeRtpConnectionRscv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 35),
    _WfAppnNodeRtpConnectionRscv_Type()
)
wfAppnNodeRtpConnectionRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRscv.setStatus("mandatory")
_WfAppnNodeRtpConnectionRscvText_Type = DisplayString
_WfAppnNodeRtpConnectionRscvText_Object = MibTableColumn
wfAppnNodeRtpConnectionRscvText = _WfAppnNodeRtpConnectionRscvText_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 1, 11, 1, 36),
    _WfAppnNodeRtpConnectionRscvText_Type()
)
wfAppnNodeRtpConnectionRscvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNodeRtpConnectionRscvText.setStatus("mandatory")
_WfAppnNn_ObjectIdentity = ObjectIdentity
wfAppnNn = _WfAppnNn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2)
)
_WfAppnNnTopo_ObjectIdentity = ObjectIdentity
wfAppnNnTopo = _WfAppnNnTopo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1)
)
_WfAppnNnTopoMaxNodes_Type = Integer32
_WfAppnNnTopoMaxNodes_Object = MibScalar
wfAppnNnTopoMaxNodes = _WfAppnNnTopoMaxNodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 1),
    _WfAppnNnTopoMaxNodes_Type()
)
wfAppnNnTopoMaxNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoMaxNodes.setStatus("mandatory")
_WfAppnNnTopoCurNumNodes_Type = Integer32
_WfAppnNnTopoCurNumNodes_Object = MibScalar
wfAppnNnTopoCurNumNodes = _WfAppnNnTopoCurNumNodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 2),
    _WfAppnNnTopoCurNumNodes_Type()
)
wfAppnNnTopoCurNumNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoCurNumNodes.setStatus("mandatory")
_WfAppnNnTopoInTdus_Type = Counter32
_WfAppnNnTopoInTdus_Object = MibScalar
wfAppnNnTopoInTdus = _WfAppnNnTopoInTdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 3),
    _WfAppnNnTopoInTdus_Type()
)
wfAppnNnTopoInTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoInTdus.setStatus("mandatory")
_WfAppnNnTopoOutTdus_Type = Counter32
_WfAppnNnTopoOutTdus_Object = MibScalar
wfAppnNnTopoOutTdus = _WfAppnNnTopoOutTdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 4),
    _WfAppnNnTopoOutTdus_Type()
)
wfAppnNnTopoOutTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoOutTdus.setStatus("mandatory")
_WfAppnNnTopoNodeLowRsns_Type = Counter32
_WfAppnNnTopoNodeLowRsns_Object = MibScalar
wfAppnNnTopoNodeLowRsns = _WfAppnNnTopoNodeLowRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 5),
    _WfAppnNnTopoNodeLowRsns_Type()
)
wfAppnNnTopoNodeLowRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodeLowRsns.setStatus("mandatory")
_WfAppnNnTopoNodeEqualRsns_Type = Counter32
_WfAppnNnTopoNodeEqualRsns_Object = MibScalar
wfAppnNnTopoNodeEqualRsns = _WfAppnNnTopoNodeEqualRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 6),
    _WfAppnNnTopoNodeEqualRsns_Type()
)
wfAppnNnTopoNodeEqualRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodeEqualRsns.setStatus("mandatory")
_WfAppnNnTopoNodeGoodHighRsns_Type = Counter32
_WfAppnNnTopoNodeGoodHighRsns_Object = MibScalar
wfAppnNnTopoNodeGoodHighRsns = _WfAppnNnTopoNodeGoodHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 7),
    _WfAppnNnTopoNodeGoodHighRsns_Type()
)
wfAppnNnTopoNodeGoodHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodeGoodHighRsns.setStatus("mandatory")
_WfAppnNnTopoNodeBadHighRsns_Type = Counter32
_WfAppnNnTopoNodeBadHighRsns_Object = MibScalar
wfAppnNnTopoNodeBadHighRsns = _WfAppnNnTopoNodeBadHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 8),
    _WfAppnNnTopoNodeBadHighRsns_Type()
)
wfAppnNnTopoNodeBadHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodeBadHighRsns.setStatus("mandatory")
_WfAppnNnTopoNodeStateUpdates_Type = Counter32
_WfAppnNnTopoNodeStateUpdates_Object = MibScalar
wfAppnNnTopoNodeStateUpdates = _WfAppnNnTopoNodeStateUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 9),
    _WfAppnNnTopoNodeStateUpdates_Type()
)
wfAppnNnTopoNodeStateUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodeStateUpdates.setStatus("mandatory")
_WfAppnNnTopoNodeErrors_Type = Counter32
_WfAppnNnTopoNodeErrors_Object = MibScalar
wfAppnNnTopoNodeErrors = _WfAppnNnTopoNodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 10),
    _WfAppnNnTopoNodeErrors_Type()
)
wfAppnNnTopoNodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodeErrors.setStatus("mandatory")
_WfAppnNnTopoNodeTimerUpdates_Type = Counter32
_WfAppnNnTopoNodeTimerUpdates_Object = MibScalar
wfAppnNnTopoNodeTimerUpdates = _WfAppnNnTopoNodeTimerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 11),
    _WfAppnNnTopoNodeTimerUpdates_Type()
)
wfAppnNnTopoNodeTimerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodeTimerUpdates.setStatus("mandatory")
_WfAppnNnTopoNodePurges_Type = Counter32
_WfAppnNnTopoNodePurges_Object = MibScalar
wfAppnNnTopoNodePurges = _WfAppnNnTopoNodePurges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 12),
    _WfAppnNnTopoNodePurges_Type()
)
wfAppnNnTopoNodePurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoNodePurges.setStatus("mandatory")
_WfAppnNnTopoTgLowRsns_Type = Counter32
_WfAppnNnTopoTgLowRsns_Object = MibScalar
wfAppnNnTopoTgLowRsns = _WfAppnNnTopoTgLowRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 13),
    _WfAppnNnTopoTgLowRsns_Type()
)
wfAppnNnTopoTgLowRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgLowRsns.setStatus("mandatory")
_WfAppnNnTopoTgEqualRsns_Type = Counter32
_WfAppnNnTopoTgEqualRsns_Object = MibScalar
wfAppnNnTopoTgEqualRsns = _WfAppnNnTopoTgEqualRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 14),
    _WfAppnNnTopoTgEqualRsns_Type()
)
wfAppnNnTopoTgEqualRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgEqualRsns.setStatus("mandatory")
_WfAppnNnTopoTgGoodHighRsns_Type = Counter32
_WfAppnNnTopoTgGoodHighRsns_Object = MibScalar
wfAppnNnTopoTgGoodHighRsns = _WfAppnNnTopoTgGoodHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 15),
    _WfAppnNnTopoTgGoodHighRsns_Type()
)
wfAppnNnTopoTgGoodHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgGoodHighRsns.setStatus("mandatory")
_WfAppnNnTopoTgBadHighRsns_Type = Counter32
_WfAppnNnTopoTgBadHighRsns_Object = MibScalar
wfAppnNnTopoTgBadHighRsns = _WfAppnNnTopoTgBadHighRsns_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 16),
    _WfAppnNnTopoTgBadHighRsns_Type()
)
wfAppnNnTopoTgBadHighRsns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgBadHighRsns.setStatus("mandatory")
_WfAppnNnTopoTgStateUpdates_Type = Counter32
_WfAppnNnTopoTgStateUpdates_Object = MibScalar
wfAppnNnTopoTgStateUpdates = _WfAppnNnTopoTgStateUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 17),
    _WfAppnNnTopoTgStateUpdates_Type()
)
wfAppnNnTopoTgStateUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgStateUpdates.setStatus("mandatory")
_WfAppnNnTopoTgErrors_Type = Counter32
_WfAppnNnTopoTgErrors_Object = MibScalar
wfAppnNnTopoTgErrors = _WfAppnNnTopoTgErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 18),
    _WfAppnNnTopoTgErrors_Type()
)
wfAppnNnTopoTgErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgErrors.setStatus("mandatory")
_WfAppnNnTopoTgTimerUpdates_Type = Counter32
_WfAppnNnTopoTgTimerUpdates_Object = MibScalar
wfAppnNnTopoTgTimerUpdates = _WfAppnNnTopoTgTimerUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 19),
    _WfAppnNnTopoTgTimerUpdates_Type()
)
wfAppnNnTopoTgTimerUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgTimerUpdates.setStatus("mandatory")
_WfAppnNnTopoTgPurges_Type = Counter32
_WfAppnNnTopoTgPurges_Object = MibScalar
wfAppnNnTopoTgPurges = _WfAppnNnTopoTgPurges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 20),
    _WfAppnNnTopoTgPurges_Type()
)
wfAppnNnTopoTgPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTgPurges.setStatus("mandatory")
_WfAppnNnTopoTotalRouteCalcs_Type = Counter32
_WfAppnNnTopoTotalRouteCalcs_Object = MibScalar
wfAppnNnTopoTotalRouteCalcs = _WfAppnNnTopoTotalRouteCalcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 21),
    _WfAppnNnTopoTotalRouteCalcs_Type()
)
wfAppnNnTopoTotalRouteCalcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTotalRouteCalcs.setStatus("mandatory")
_WfAppnNnTopoTotalRouteRejs_Type = Counter32
_WfAppnNnTopoTotalRouteRejs_Object = MibScalar
wfAppnNnTopoTotalRouteRejs = _WfAppnNnTopoTotalRouteRejs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 1, 22),
    _WfAppnNnTopoTotalRouteRejs_Type()
)
wfAppnNnTopoTotalRouteRejs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTopoTotalRouteRejs.setStatus("mandatory")
_WfAppnNnAdjNodeTable_Object = MibTable
wfAppnNnAdjNodeTable = _WfAppnNnAdjNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 2)
)
if mibBuilder.loadTexts:
    wfAppnNnAdjNodeTable.setStatus("mandatory")
_WfAppnNnAdjNodeEntry_Object = MibTableRow
wfAppnNnAdjNodeEntry = _WfAppnNnAdjNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 2, 1)
)
wfAppnNnAdjNodeEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNnAdjNodeAdjName"),
)
if mibBuilder.loadTexts:
    wfAppnNnAdjNodeEntry.setStatus("mandatory")
_WfAppnNnAdjNodeAdjName_Type = DisplayString
_WfAppnNnAdjNodeAdjName_Object = MibTableColumn
wfAppnNnAdjNodeAdjName = _WfAppnNnAdjNodeAdjName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 2, 1, 1),
    _WfAppnNnAdjNodeAdjName_Type()
)
wfAppnNnAdjNodeAdjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnAdjNodeAdjName.setStatus("mandatory")


class _WfAppnNnAdjNodeCpCpSessStatus_Type(Integer32):
    """Custom type wfAppnNnAdjNodeCpCpSessStatus based on Integer32"""
    defaultValue = 4

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
        *(("active", 1),
          ("inactive", 4),
          ("loser", 2),
          ("winner", 3))
    )


_WfAppnNnAdjNodeCpCpSessStatus_Type.__name__ = "Integer32"
_WfAppnNnAdjNodeCpCpSessStatus_Object = MibTableColumn
wfAppnNnAdjNodeCpCpSessStatus = _WfAppnNnAdjNodeCpCpSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 2, 1, 2),
    _WfAppnNnAdjNodeCpCpSessStatus_Type()
)
wfAppnNnAdjNodeCpCpSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnAdjNodeCpCpSessStatus.setStatus("mandatory")
_WfAppnNnAdjNodeOutOfSeqTdus_Type = Gauge32
_WfAppnNnAdjNodeOutOfSeqTdus_Object = MibTableColumn
wfAppnNnAdjNodeOutOfSeqTdus = _WfAppnNnAdjNodeOutOfSeqTdus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 2, 1, 3),
    _WfAppnNnAdjNodeOutOfSeqTdus_Type()
)
wfAppnNnAdjNodeOutOfSeqTdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnAdjNodeOutOfSeqTdus.setStatus("mandatory")
_WfAppnNnAdjNodeLastFrsnSent_Type = Integer32
_WfAppnNnAdjNodeLastFrsnSent_Object = MibTableColumn
wfAppnNnAdjNodeLastFrsnSent = _WfAppnNnAdjNodeLastFrsnSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 2, 1, 4),
    _WfAppnNnAdjNodeLastFrsnSent_Type()
)
wfAppnNnAdjNodeLastFrsnSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnAdjNodeLastFrsnSent.setStatus("mandatory")
_WfAppnNnAdjNodeLastFrsnRcvd_Type = Integer32
_WfAppnNnAdjNodeLastFrsnRcvd_Object = MibTableColumn
wfAppnNnAdjNodeLastFrsnRcvd = _WfAppnNnAdjNodeLastFrsnRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 2, 1, 5),
    _WfAppnNnAdjNodeLastFrsnRcvd_Type()
)
wfAppnNnAdjNodeLastFrsnRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnAdjNodeLastFrsnRcvd.setStatus("mandatory")
_WfAppnNnTopology_ObjectIdentity = ObjectIdentity
wfAppnNnTopology = _WfAppnNnTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3)
)
_WfAppnNnTopologyTable_Object = MibTable
wfAppnNnTopologyTable = _WfAppnNnTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1)
)
if mibBuilder.loadTexts:
    wfAppnNnTopologyTable.setStatus("mandatory")
_WfAppnNnTopologyEntry_Object = MibTableRow
wfAppnNnTopologyEntry = _WfAppnNnTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1)
)
wfAppnNnTopologyEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNnNodeName"),
)
if mibBuilder.loadTexts:
    wfAppnNnTopologyEntry.setStatus("mandatory")
_WfAppnNnNodeName_Type = DisplayString
_WfAppnNnNodeName_Object = MibTableColumn
wfAppnNnNodeName = _WfAppnNnNodeName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 1),
    _WfAppnNnNodeName_Type()
)
wfAppnNnNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeName.setStatus("mandatory")
_WfAppnNnNodeFrsn_Type = Integer32
_WfAppnNnNodeFrsn_Object = MibTableColumn
wfAppnNnNodeFrsn = _WfAppnNnNodeFrsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 2),
    _WfAppnNnNodeFrsn_Type()
)
wfAppnNnNodeFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFrsn.setStatus("mandatory")
_WfAppnNnNodeEntryTimeLeft_Type = Integer32
_WfAppnNnNodeEntryTimeLeft_Object = MibTableColumn
wfAppnNnNodeEntryTimeLeft = _WfAppnNnNodeEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 3),
    _WfAppnNnNodeEntryTimeLeft_Type()
)
wfAppnNnNodeEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeEntryTimeLeft.setStatus("mandatory")


class _WfAppnNnNodeType_Type(Integer32):
    """Custom type wfAppnNnNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nn", 1),
          ("vn", 3))
    )


_WfAppnNnNodeType_Type.__name__ = "Integer32"
_WfAppnNnNodeType_Object = MibTableColumn
wfAppnNnNodeType = _WfAppnNnNodeType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 4),
    _WfAppnNnNodeType_Type()
)
wfAppnNnNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeType.setStatus("mandatory")
_WfAppnNnNodeRsn_Type = Integer32
_WfAppnNnNodeRsn_Object = MibTableColumn
wfAppnNnNodeRsn = _WfAppnNnNodeRsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 5),
    _WfAppnNnNodeRsn_Type()
)
wfAppnNnNodeRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeRsn.setStatus("mandatory")
_WfAppnNnNodeRouteAddResist_Type = Integer32
_WfAppnNnNodeRouteAddResist_Object = MibTableColumn
wfAppnNnNodeRouteAddResist = _WfAppnNnNodeRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 6),
    _WfAppnNnNodeRouteAddResist_Type()
)
wfAppnNnNodeRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeRouteAddResist.setStatus("mandatory")


class _WfAppnNnNodeCongested_Type(Integer32):
    """Custom type wfAppnNnNodeCongested based on Integer32"""
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


_WfAppnNnNodeCongested_Type.__name__ = "Integer32"
_WfAppnNnNodeCongested_Object = MibTableColumn
wfAppnNnNodeCongested = _WfAppnNnNodeCongested_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 7),
    _WfAppnNnNodeCongested_Type()
)
wfAppnNnNodeCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeCongested.setStatus("mandatory")


class _WfAppnNnNodeIsrDepleted_Type(Integer32):
    """Custom type wfAppnNnNodeIsrDepleted based on Integer32"""
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


_WfAppnNnNodeIsrDepleted_Type.__name__ = "Integer32"
_WfAppnNnNodeIsrDepleted_Object = MibTableColumn
wfAppnNnNodeIsrDepleted = _WfAppnNnNodeIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 8),
    _WfAppnNnNodeIsrDepleted_Type()
)
wfAppnNnNodeIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeIsrDepleted.setStatus("mandatory")


class _WfAppnNnNodeEndptDepleted_Type(Integer32):
    """Custom type wfAppnNnNodeEndptDepleted based on Integer32"""
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


_WfAppnNnNodeEndptDepleted_Type.__name__ = "Integer32"
_WfAppnNnNodeEndptDepleted_Object = MibTableColumn
wfAppnNnNodeEndptDepleted = _WfAppnNnNodeEndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 9),
    _WfAppnNnNodeEndptDepleted_Type()
)
wfAppnNnNodeEndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeEndptDepleted.setStatus("mandatory")


class _WfAppnNnNodeQuiescing_Type(Integer32):
    """Custom type wfAppnNnNodeQuiescing based on Integer32"""
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


_WfAppnNnNodeQuiescing_Type.__name__ = "Integer32"
_WfAppnNnNodeQuiescing_Object = MibTableColumn
wfAppnNnNodeQuiescing = _WfAppnNnNodeQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 10),
    _WfAppnNnNodeQuiescing_Type()
)
wfAppnNnNodeQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeQuiescing.setStatus("mandatory")


class _WfAppnNnNodeGateway_Type(Integer32):
    """Custom type wfAppnNnNodeGateway based on Integer32"""
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


_WfAppnNnNodeGateway_Type.__name__ = "Integer32"
_WfAppnNnNodeGateway_Object = MibTableColumn
wfAppnNnNodeGateway = _WfAppnNnNodeGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 11),
    _WfAppnNnNodeGateway_Type()
)
wfAppnNnNodeGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeGateway.setStatus("mandatory")


class _WfAppnNnNodeCentralDirectory_Type(Integer32):
    """Custom type wfAppnNnNodeCentralDirectory based on Integer32"""
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


_WfAppnNnNodeCentralDirectory_Type.__name__ = "Integer32"
_WfAppnNnNodeCentralDirectory_Object = MibTableColumn
wfAppnNnNodeCentralDirectory = _WfAppnNnNodeCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 12),
    _WfAppnNnNodeCentralDirectory_Type()
)
wfAppnNnNodeCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeCentralDirectory.setStatus("mandatory")


class _WfAppnNnNodeIsr_Type(Integer32):
    """Custom type wfAppnNnNodeIsr based on Integer32"""
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


_WfAppnNnNodeIsr_Type.__name__ = "Integer32"
_WfAppnNnNodeIsr_Object = MibTableColumn
wfAppnNnNodeIsr = _WfAppnNnNodeIsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 13),
    _WfAppnNnNodeIsr_Type()
)
wfAppnNnNodeIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeIsr.setStatus("mandatory")


class _WfAppnNnNodeChainSupport_Type(Integer32):
    """Custom type wfAppnNnNodeChainSupport based on Integer32"""
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


_WfAppnNnNodeChainSupport_Type.__name__ = "Integer32"
_WfAppnNnNodeChainSupport_Object = MibTableColumn
wfAppnNnNodeChainSupport = _WfAppnNnNodeChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 14),
    _WfAppnNnNodeChainSupport_Type()
)
wfAppnNnNodeChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeChainSupport.setStatus("mandatory")


class _WfAppnNnNodeHprBase_Type(Integer32):
    """Custom type wfAppnNnNodeHprBase based on Integer32"""
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


_WfAppnNnNodeHprBase_Type.__name__ = "Integer32"
_WfAppnNnNodeHprBase_Object = MibTableColumn
wfAppnNnNodeHprBase = _WfAppnNnNodeHprBase_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 15),
    _WfAppnNnNodeHprBase_Type()
)
wfAppnNnNodeHprBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeHprBase.setStatus("mandatory")


class _WfAppnNnNodeRtpTower_Type(Integer32):
    """Custom type wfAppnNnNodeRtpTower based on Integer32"""
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


_WfAppnNnNodeRtpTower_Type.__name__ = "Integer32"
_WfAppnNnNodeRtpTower_Object = MibTableColumn
wfAppnNnNodeRtpTower = _WfAppnNnNodeRtpTower_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 1, 1, 16),
    _WfAppnNnNodeRtpTower_Type()
)
wfAppnNnNodeRtpTower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeRtpTower.setStatus("mandatory")
_WfAppnNnTgTopologyTable_Object = MibTable
wfAppnNnTgTopologyTable = _WfAppnNnTgTopologyTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2)
)
if mibBuilder.loadTexts:
    wfAppnNnTgTopologyTable.setStatus("mandatory")
_WfAppnNnTgTopologyEntry_Object = MibTableRow
wfAppnNnTgTopologyEntry = _WfAppnNnTgTopologyEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1)
)
wfAppnNnTgTopologyEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNnTgOwner"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNnTgDest"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNnTgNum"),
)
if mibBuilder.loadTexts:
    wfAppnNnTgTopologyEntry.setStatus("mandatory")
_WfAppnNnTgOwner_Type = DisplayString
_WfAppnNnTgOwner_Object = MibTableColumn
wfAppnNnTgOwner = _WfAppnNnTgOwner_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 1),
    _WfAppnNnTgOwner_Type()
)
wfAppnNnTgOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgOwner.setStatus("mandatory")
_WfAppnNnTgDest_Type = DisplayString
_WfAppnNnTgDest_Object = MibTableColumn
wfAppnNnTgDest = _WfAppnNnTgDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 2),
    _WfAppnNnTgDest_Type()
)
wfAppnNnTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgDest.setStatus("mandatory")
_WfAppnNnTgNum_Type = Integer32
_WfAppnNnTgNum_Object = MibTableColumn
wfAppnNnTgNum = _WfAppnNnTgNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 3),
    _WfAppnNnTgNum_Type()
)
wfAppnNnTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgNum.setStatus("mandatory")
_WfAppnNnTgFrsn_Type = Integer32
_WfAppnNnTgFrsn_Object = MibTableColumn
wfAppnNnTgFrsn = _WfAppnNnTgFrsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 4),
    _WfAppnNnTgFrsn_Type()
)
wfAppnNnTgFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFrsn.setStatus("mandatory")
_WfAppnNnTgEntryTimeLeft_Type = Integer32
_WfAppnNnTgEntryTimeLeft_Object = MibTableColumn
wfAppnNnTgEntryTimeLeft = _WfAppnNnTgEntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 5),
    _WfAppnNnTgEntryTimeLeft_Type()
)
wfAppnNnTgEntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgEntryTimeLeft.setStatus("mandatory")
_WfAppnNnTgDestVirtual_Type = Integer32
_WfAppnNnTgDestVirtual_Object = MibTableColumn
wfAppnNnTgDestVirtual = _WfAppnNnTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 6),
    _WfAppnNnTgDestVirtual_Type()
)
wfAppnNnTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgDestVirtual.setStatus("mandatory")
_WfAppnNnTgDlcData_Type = OctetString
_WfAppnNnTgDlcData_Object = MibTableColumn
wfAppnNnTgDlcData = _WfAppnNnTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 7),
    _WfAppnNnTgDlcData_Type()
)
wfAppnNnTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgDlcData.setStatus("mandatory")
_WfAppnNnTgRsn_Type = Integer32
_WfAppnNnTgRsn_Object = MibTableColumn
wfAppnNnTgRsn = _WfAppnNnTgRsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 8),
    _WfAppnNnTgRsn_Type()
)
wfAppnNnTgRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgRsn.setStatus("mandatory")
_WfAppnNnTgOperational_Type = Integer32
_WfAppnNnTgOperational_Object = MibTableColumn
wfAppnNnTgOperational = _WfAppnNnTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 9),
    _WfAppnNnTgOperational_Type()
)
wfAppnNnTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgOperational.setStatus("mandatory")
_WfAppnNnTgQuiescing_Type = Integer32
_WfAppnNnTgQuiescing_Object = MibTableColumn
wfAppnNnTgQuiescing = _WfAppnNnTgQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 10),
    _WfAppnNnTgQuiescing_Type()
)
wfAppnNnTgQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgQuiescing.setStatus("mandatory")
_WfAppnNnTgCpCpSession_Type = Integer32
_WfAppnNnTgCpCpSession_Object = MibTableColumn
wfAppnNnTgCpCpSession = _WfAppnNnTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 11),
    _WfAppnNnTgCpCpSession_Type()
)
wfAppnNnTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgCpCpSession.setStatus("mandatory")


class _WfAppnNnTgEffCap_Type(Integer32):
    """Custom type wfAppnNnTgEffCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNnTgEffCap_Type.__name__ = "Integer32"
_WfAppnNnTgEffCap_Object = MibTableColumn
wfAppnNnTgEffCap = _WfAppnNnTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 12),
    _WfAppnNnTgEffCap_Type()
)
wfAppnNnTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgEffCap.setStatus("mandatory")
_WfAppnNnTgConnCost_Type = Integer32
_WfAppnNnTgConnCost_Object = MibTableColumn
wfAppnNnTgConnCost = _WfAppnNnTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 13),
    _WfAppnNnTgConnCost_Type()
)
wfAppnNnTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgConnCost.setStatus("mandatory")
_WfAppnNnTgByteCost_Type = Integer32
_WfAppnNnTgByteCost_Object = MibTableColumn
wfAppnNnTgByteCost = _WfAppnNnTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 14),
    _WfAppnNnTgByteCost_Type()
)
wfAppnNnTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgByteCost.setStatus("mandatory")


class _WfAppnNnTgSecurity_Type(Integer32):
    """Custom type wfAppnNnTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNnTgSecurity_Type.__name__ = "Integer32"
_WfAppnNnTgSecurity_Object = MibTableColumn
wfAppnNnTgSecurity = _WfAppnNnTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 15),
    _WfAppnNnTgSecurity_Type()
)
wfAppnNnTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgSecurity.setStatus("mandatory")


class _WfAppnNnTgDelay_Type(Integer32):
    """Custom type wfAppnNnTgDelay based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnNnTgDelay_Type.__name__ = "Integer32"
_WfAppnNnTgDelay_Object = MibTableColumn
wfAppnNnTgDelay = _WfAppnNnTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 16),
    _WfAppnNnTgDelay_Type()
)
wfAppnNnTgDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNnTgDelay.setStatus("mandatory")
_WfAppnNnTgModemClass_Type = Integer32
_WfAppnNnTgModemClass_Object = MibTableColumn
wfAppnNnTgModemClass = _WfAppnNnTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 17),
    _WfAppnNnTgModemClass_Type()
)
wfAppnNnTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgModemClass.setStatus("mandatory")
_WfAppnNnTgUsr1_Type = Integer32
_WfAppnNnTgUsr1_Object = MibTableColumn
wfAppnNnTgUsr1 = _WfAppnNnTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 18),
    _WfAppnNnTgUsr1_Type()
)
wfAppnNnTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgUsr1.setStatus("mandatory")
_WfAppnNnTgUsr2_Type = Integer32
_WfAppnNnTgUsr2_Object = MibTableColumn
wfAppnNnTgUsr2 = _WfAppnNnTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 19),
    _WfAppnNnTgUsr2_Type()
)
wfAppnNnTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgUsr2.setStatus("mandatory")
_WfAppnNnTgUsr3_Type = Integer32
_WfAppnNnTgUsr3_Object = MibTableColumn
wfAppnNnTgUsr3 = _WfAppnNnTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 20),
    _WfAppnNnTgUsr3_Type()
)
wfAppnNnTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgUsr3.setStatus("mandatory")
_WfAppnNnTgHprBase_Type = Integer32
_WfAppnNnTgHprBase_Object = MibTableColumn
wfAppnNnTgHprBase = _WfAppnNnTgHprBase_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 21),
    _WfAppnNnTgHprBase_Type()
)
wfAppnNnTgHprBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgHprBase.setStatus("mandatory")
_WfAppnNnTgRtpTower_Type = Integer32
_WfAppnNnTgRtpTower_Object = MibTableColumn
wfAppnNnTgRtpTower = _WfAppnNnTgRtpTower_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 2, 1, 22),
    _WfAppnNnTgRtpTower_Type()
)
wfAppnNnTgRtpTower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgRtpTower.setStatus("mandatory")
_WfAppnNnTopologyFRTable_Object = MibTable
wfAppnNnTopologyFRTable = _WfAppnNnTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3)
)
if mibBuilder.loadTexts:
    wfAppnNnTopologyFRTable.setStatus("mandatory")
_WfAppnNnTopologyFREntry_Object = MibTableRow
wfAppnNnTopologyFREntry = _WfAppnNnTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1)
)
wfAppnNnTopologyFREntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNnNodeFRFrsn"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNnNodeFRName"),
)
if mibBuilder.loadTexts:
    wfAppnNnTopologyFREntry.setStatus("mandatory")
_WfAppnNnNodeFRName_Type = DisplayString
_WfAppnNnNodeFRName_Object = MibTableColumn
wfAppnNnNodeFRName = _WfAppnNnNodeFRName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 1),
    _WfAppnNnNodeFRName_Type()
)
wfAppnNnNodeFRName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRName.setStatus("mandatory")
_WfAppnNnNodeFRFrsn_Type = Integer32
_WfAppnNnNodeFRFrsn_Object = MibTableColumn
wfAppnNnNodeFRFrsn = _WfAppnNnNodeFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 2),
    _WfAppnNnNodeFRFrsn_Type()
)
wfAppnNnNodeFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRFrsn.setStatus("mandatory")
_WfAppnNnNodeFREntryTimeLeft_Type = Integer32
_WfAppnNnNodeFREntryTimeLeft_Object = MibTableColumn
wfAppnNnNodeFREntryTimeLeft = _WfAppnNnNodeFREntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 3),
    _WfAppnNnNodeFREntryTimeLeft_Type()
)
wfAppnNnNodeFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFREntryTimeLeft.setStatus("mandatory")


class _WfAppnNnNodeFRType_Type(Integer32):
    """Custom type wfAppnNnNodeFRType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nn", 1),
          ("vn", 3))
    )


_WfAppnNnNodeFRType_Type.__name__ = "Integer32"
_WfAppnNnNodeFRType_Object = MibTableColumn
wfAppnNnNodeFRType = _WfAppnNnNodeFRType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 4),
    _WfAppnNnNodeFRType_Type()
)
wfAppnNnNodeFRType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRType.setStatus("mandatory")
_WfAppnNnNodeFRRsn_Type = Integer32
_WfAppnNnNodeFRRsn_Object = MibTableColumn
wfAppnNnNodeFRRsn = _WfAppnNnNodeFRRsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 5),
    _WfAppnNnNodeFRRsn_Type()
)
wfAppnNnNodeFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRRsn.setStatus("mandatory")
_WfAppnNnNodeFRRouteAddResist_Type = Integer32
_WfAppnNnNodeFRRouteAddResist_Object = MibTableColumn
wfAppnNnNodeFRRouteAddResist = _WfAppnNnNodeFRRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 6),
    _WfAppnNnNodeFRRouteAddResist_Type()
)
wfAppnNnNodeFRRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRRouteAddResist.setStatus("mandatory")


class _WfAppnNnNodeFRCongested_Type(Integer32):
    """Custom type wfAppnNnNodeFRCongested based on Integer32"""
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


_WfAppnNnNodeFRCongested_Type.__name__ = "Integer32"
_WfAppnNnNodeFRCongested_Object = MibTableColumn
wfAppnNnNodeFRCongested = _WfAppnNnNodeFRCongested_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 7),
    _WfAppnNnNodeFRCongested_Type()
)
wfAppnNnNodeFRCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRCongested.setStatus("mandatory")


class _WfAppnNnNodeFRIsrDepleted_Type(Integer32):
    """Custom type wfAppnNnNodeFRIsrDepleted based on Integer32"""
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


_WfAppnNnNodeFRIsrDepleted_Type.__name__ = "Integer32"
_WfAppnNnNodeFRIsrDepleted_Object = MibTableColumn
wfAppnNnNodeFRIsrDepleted = _WfAppnNnNodeFRIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 8),
    _WfAppnNnNodeFRIsrDepleted_Type()
)
wfAppnNnNodeFRIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRIsrDepleted.setStatus("mandatory")


class _WfAppnNnNodeFREndptDepleted_Type(Integer32):
    """Custom type wfAppnNnNodeFREndptDepleted based on Integer32"""
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


_WfAppnNnNodeFREndptDepleted_Type.__name__ = "Integer32"
_WfAppnNnNodeFREndptDepleted_Object = MibTableColumn
wfAppnNnNodeFREndptDepleted = _WfAppnNnNodeFREndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 9),
    _WfAppnNnNodeFREndptDepleted_Type()
)
wfAppnNnNodeFREndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFREndptDepleted.setStatus("mandatory")


class _WfAppnNnNodeFRQuiescing_Type(Integer32):
    """Custom type wfAppnNnNodeFRQuiescing based on Integer32"""
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


_WfAppnNnNodeFRQuiescing_Type.__name__ = "Integer32"
_WfAppnNnNodeFRQuiescing_Object = MibTableColumn
wfAppnNnNodeFRQuiescing = _WfAppnNnNodeFRQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 10),
    _WfAppnNnNodeFRQuiescing_Type()
)
wfAppnNnNodeFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRQuiescing.setStatus("mandatory")


class _WfAppnNnNodeFRGateway_Type(Integer32):
    """Custom type wfAppnNnNodeFRGateway based on Integer32"""
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


_WfAppnNnNodeFRGateway_Type.__name__ = "Integer32"
_WfAppnNnNodeFRGateway_Object = MibTableColumn
wfAppnNnNodeFRGateway = _WfAppnNnNodeFRGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 11),
    _WfAppnNnNodeFRGateway_Type()
)
wfAppnNnNodeFRGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRGateway.setStatus("mandatory")


class _WfAppnNnNodeFRCentralDirectory_Type(Integer32):
    """Custom type wfAppnNnNodeFRCentralDirectory based on Integer32"""
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


_WfAppnNnNodeFRCentralDirectory_Type.__name__ = "Integer32"
_WfAppnNnNodeFRCentralDirectory_Object = MibTableColumn
wfAppnNnNodeFRCentralDirectory = _WfAppnNnNodeFRCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 12),
    _WfAppnNnNodeFRCentralDirectory_Type()
)
wfAppnNnNodeFRCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRCentralDirectory.setStatus("mandatory")


class _WfAppnNnNodeFRIsr_Type(Integer32):
    """Custom type wfAppnNnNodeFRIsr based on Integer32"""
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


_WfAppnNnNodeFRIsr_Type.__name__ = "Integer32"
_WfAppnNnNodeFRIsr_Object = MibTableColumn
wfAppnNnNodeFRIsr = _WfAppnNnNodeFRIsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 13),
    _WfAppnNnNodeFRIsr_Type()
)
wfAppnNnNodeFRIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRIsr.setStatus("mandatory")


class _WfAppnNnNodeFRChainSupport_Type(Integer32):
    """Custom type wfAppnNnNodeFRChainSupport based on Integer32"""
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


_WfAppnNnNodeFRChainSupport_Type.__name__ = "Integer32"
_WfAppnNnNodeFRChainSupport_Object = MibTableColumn
wfAppnNnNodeFRChainSupport = _WfAppnNnNodeFRChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 14),
    _WfAppnNnNodeFRChainSupport_Type()
)
wfAppnNnNodeFRChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRChainSupport.setStatus("mandatory")


class _WfAppnNnNodeFRHprBase_Type(Integer32):
    """Custom type wfAppnNnNodeFRHprBase based on Integer32"""
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


_WfAppnNnNodeFRHprBase_Type.__name__ = "Integer32"
_WfAppnNnNodeFRHprBase_Object = MibTableColumn
wfAppnNnNodeFRHprBase = _WfAppnNnNodeFRHprBase_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 15),
    _WfAppnNnNodeFRHprBase_Type()
)
wfAppnNnNodeFRHprBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRHprBase.setStatus("mandatory")


class _WfAppnNnNodeFRRtpTower_Type(Integer32):
    """Custom type wfAppnNnNodeFRRtpTower based on Integer32"""
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


_WfAppnNnNodeFRRtpTower_Type.__name__ = "Integer32"
_WfAppnNnNodeFRRtpTower_Object = MibTableColumn
wfAppnNnNodeFRRtpTower = _WfAppnNnNodeFRRtpTower_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 3, 1, 16),
    _WfAppnNnNodeFRRtpTower_Type()
)
wfAppnNnNodeFRRtpTower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnNodeFRRtpTower.setStatus("mandatory")
_WfAppnNnTgTopologyFRTable_Object = MibTable
wfAppnNnTgTopologyFRTable = _WfAppnNnTgTopologyFRTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4)
)
if mibBuilder.loadTexts:
    wfAppnNnTgTopologyFRTable.setStatus("mandatory")
_WfAppnNnTgTopologyFREntry_Object = MibTableRow
wfAppnNnTgTopologyFREntry = _WfAppnNnTgTopologyFREntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1)
)
wfAppnNnTgTopologyFREntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnNnTgFRFrsn"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNnTgFROwner"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNnTgFRDest"),
    (0, "Wellfleet-APPN-MIB", "wfAppnNnTgFRNum"),
)
if mibBuilder.loadTexts:
    wfAppnNnTgTopologyFREntry.setStatus("mandatory")
_WfAppnNnTgFROwner_Type = DisplayString
_WfAppnNnTgFROwner_Object = MibTableColumn
wfAppnNnTgFROwner = _WfAppnNnTgFROwner_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 1),
    _WfAppnNnTgFROwner_Type()
)
wfAppnNnTgFROwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFROwner.setStatus("mandatory")
_WfAppnNnTgFRDest_Type = DisplayString
_WfAppnNnTgFRDest_Object = MibTableColumn
wfAppnNnTgFRDest = _WfAppnNnTgFRDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 2),
    _WfAppnNnTgFRDest_Type()
)
wfAppnNnTgFRDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRDest.setStatus("mandatory")
_WfAppnNnTgFRNum_Type = Integer32
_WfAppnNnTgFRNum_Object = MibTableColumn
wfAppnNnTgFRNum = _WfAppnNnTgFRNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 3),
    _WfAppnNnTgFRNum_Type()
)
wfAppnNnTgFRNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRNum.setStatus("mandatory")
_WfAppnNnTgFRFrsn_Type = Integer32
_WfAppnNnTgFRFrsn_Object = MibTableColumn
wfAppnNnTgFRFrsn = _WfAppnNnTgFRFrsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 4),
    _WfAppnNnTgFRFrsn_Type()
)
wfAppnNnTgFRFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRFrsn.setStatus("mandatory")
_WfAppnNnTgFREntryTimeLeft_Type = Integer32
_WfAppnNnTgFREntryTimeLeft_Object = MibTableColumn
wfAppnNnTgFREntryTimeLeft = _WfAppnNnTgFREntryTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 5),
    _WfAppnNnTgFREntryTimeLeft_Type()
)
wfAppnNnTgFREntryTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFREntryTimeLeft.setStatus("mandatory")
_WfAppnNnTgFRDestVirtual_Type = Integer32
_WfAppnNnTgFRDestVirtual_Object = MibTableColumn
wfAppnNnTgFRDestVirtual = _WfAppnNnTgFRDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 6),
    _WfAppnNnTgFRDestVirtual_Type()
)
wfAppnNnTgFRDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRDestVirtual.setStatus("mandatory")
_WfAppnNnTgFRDlcData_Type = OctetString
_WfAppnNnTgFRDlcData_Object = MibTableColumn
wfAppnNnTgFRDlcData = _WfAppnNnTgFRDlcData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 7),
    _WfAppnNnTgFRDlcData_Type()
)
wfAppnNnTgFRDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRDlcData.setStatus("mandatory")
_WfAppnNnTgFRRsn_Type = Integer32
_WfAppnNnTgFRRsn_Object = MibTableColumn
wfAppnNnTgFRRsn = _WfAppnNnTgFRRsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 8),
    _WfAppnNnTgFRRsn_Type()
)
wfAppnNnTgFRRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRRsn.setStatus("mandatory")
_WfAppnNnTgFROperational_Type = Integer32
_WfAppnNnTgFROperational_Object = MibTableColumn
wfAppnNnTgFROperational = _WfAppnNnTgFROperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 9),
    _WfAppnNnTgFROperational_Type()
)
wfAppnNnTgFROperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFROperational.setStatus("mandatory")
_WfAppnNnTgFRQuiescing_Type = Integer32
_WfAppnNnTgFRQuiescing_Object = MibTableColumn
wfAppnNnTgFRQuiescing = _WfAppnNnTgFRQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 10),
    _WfAppnNnTgFRQuiescing_Type()
)
wfAppnNnTgFRQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRQuiescing.setStatus("mandatory")
_WfAppnNnTgFRCpCpSession_Type = Integer32
_WfAppnNnTgFRCpCpSession_Object = MibTableColumn
wfAppnNnTgFRCpCpSession = _WfAppnNnTgFRCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 11),
    _WfAppnNnTgFRCpCpSession_Type()
)
wfAppnNnTgFRCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRCpCpSession.setStatus("mandatory")


class _WfAppnNnTgFREffCap_Type(Integer32):
    """Custom type wfAppnNnTgFREffCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNnTgFREffCap_Type.__name__ = "Integer32"
_WfAppnNnTgFREffCap_Object = MibTableColumn
wfAppnNnTgFREffCap = _WfAppnNnTgFREffCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 12),
    _WfAppnNnTgFREffCap_Type()
)
wfAppnNnTgFREffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFREffCap.setStatus("mandatory")
_WfAppnNnTgFRConnCost_Type = Integer32
_WfAppnNnTgFRConnCost_Object = MibTableColumn
wfAppnNnTgFRConnCost = _WfAppnNnTgFRConnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 13),
    _WfAppnNnTgFRConnCost_Type()
)
wfAppnNnTgFRConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRConnCost.setStatus("mandatory")
_WfAppnNnTgFRByteCost_Type = Integer32
_WfAppnNnTgFRByteCost_Object = MibTableColumn
wfAppnNnTgFRByteCost = _WfAppnNnTgFRByteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 14),
    _WfAppnNnTgFRByteCost_Type()
)
wfAppnNnTgFRByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRByteCost.setStatus("mandatory")


class _WfAppnNnTgFRSecurity_Type(Integer32):
    """Custom type wfAppnNnTgFRSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnNnTgFRSecurity_Type.__name__ = "Integer32"
_WfAppnNnTgFRSecurity_Object = MibTableColumn
wfAppnNnTgFRSecurity = _WfAppnNnTgFRSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 15),
    _WfAppnNnTgFRSecurity_Type()
)
wfAppnNnTgFRSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRSecurity.setStatus("mandatory")


class _WfAppnNnTgFRDelay_Type(Integer32):
    """Custom type wfAppnNnTgFRDelay based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnNnTgFRDelay_Type.__name__ = "Integer32"
_WfAppnNnTgFRDelay_Object = MibTableColumn
wfAppnNnTgFRDelay = _WfAppnNnTgFRDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 16),
    _WfAppnNnTgFRDelay_Type()
)
wfAppnNnTgFRDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnNnTgFRDelay.setStatus("mandatory")
_WfAppnNnTgFRModemClass_Type = Integer32
_WfAppnNnTgFRModemClass_Object = MibTableColumn
wfAppnNnTgFRModemClass = _WfAppnNnTgFRModemClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 17),
    _WfAppnNnTgFRModemClass_Type()
)
wfAppnNnTgFRModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRModemClass.setStatus("mandatory")
_WfAppnNnTgFRUsr1_Type = Integer32
_WfAppnNnTgFRUsr1_Object = MibTableColumn
wfAppnNnTgFRUsr1 = _WfAppnNnTgFRUsr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 18),
    _WfAppnNnTgFRUsr1_Type()
)
wfAppnNnTgFRUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRUsr1.setStatus("mandatory")
_WfAppnNnTgFRUsr2_Type = Integer32
_WfAppnNnTgFRUsr2_Object = MibTableColumn
wfAppnNnTgFRUsr2 = _WfAppnNnTgFRUsr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 19),
    _WfAppnNnTgFRUsr2_Type()
)
wfAppnNnTgFRUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRUsr2.setStatus("mandatory")
_WfAppnNnTgFRUsr3_Type = Integer32
_WfAppnNnTgFRUsr3_Object = MibTableColumn
wfAppnNnTgFRUsr3 = _WfAppnNnTgFRUsr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 20),
    _WfAppnNnTgFRUsr3_Type()
)
wfAppnNnTgFRUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRUsr3.setStatus("mandatory")
_WfAppnNnTgFRHprBase_Type = Integer32
_WfAppnNnTgFRHprBase_Object = MibTableColumn
wfAppnNnTgFRHprBase = _WfAppnNnTgFRHprBase_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 21),
    _WfAppnNnTgFRHprBase_Type()
)
wfAppnNnTgFRHprBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRHprBase.setStatus("mandatory")
_WfAppnNnTgFRRtpTower_Type = Integer32
_WfAppnNnTgFRRtpTower_Object = MibTableColumn
wfAppnNnTgFRRtpTower = _WfAppnNnTgFRRtpTower_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 2, 3, 4, 1, 22),
    _WfAppnNnTgFRRtpTower_Type()
)
wfAppnNnTgFRRtpTower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnNnTgFRRtpTower.setStatus("mandatory")
_WfAppnLocalTopology_ObjectIdentity = ObjectIdentity
wfAppnLocalTopology = _WfAppnLocalTopology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3)
)
_WfAppnLocalThisNode_ObjectIdentity = ObjectIdentity
wfAppnLocalThisNode = _WfAppnLocalThisNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1)
)
_WfAppnLocalInfo_ObjectIdentity = ObjectIdentity
wfAppnLocalInfo = _WfAppnLocalInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1)
)
_WfAppnLocalNodeName_Type = DisplayString
_WfAppnLocalNodeName_Object = MibScalar
wfAppnLocalNodeName = _WfAppnLocalNodeName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 1),
    _WfAppnLocalNodeName_Type()
)
wfAppnLocalNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNodeName.setStatus("mandatory")


class _WfAppnLocalNodeType_Type(Integer32):
    """Custom type wfAppnLocalNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("en", 2),
          ("len", 4),
          ("nn", 1))
    )


_WfAppnLocalNodeType_Type.__name__ = "Integer32"
_WfAppnLocalNodeType_Object = MibScalar
wfAppnLocalNodeType = _WfAppnLocalNodeType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 2),
    _WfAppnLocalNodeType_Type()
)
wfAppnLocalNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNodeType.setStatus("mandatory")
_WfAppnLocalNnRsn_Type = Integer32
_WfAppnLocalNnRsn_Object = MibScalar
wfAppnLocalNnRsn = _WfAppnLocalNnRsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 3),
    _WfAppnLocalNnRsn_Type()
)
wfAppnLocalNnRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnRsn.setStatus("mandatory")
_WfAppnLocalNnRouteAddResist_Type = Integer32
_WfAppnLocalNnRouteAddResist_Object = MibScalar
wfAppnLocalNnRouteAddResist = _WfAppnLocalNnRouteAddResist_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 4),
    _WfAppnLocalNnRouteAddResist_Type()
)
wfAppnLocalNnRouteAddResist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnRouteAddResist.setStatus("mandatory")


class _WfAppnLocalNnCongested_Type(Integer32):
    """Custom type wfAppnLocalNnCongested based on Integer32"""
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


_WfAppnLocalNnCongested_Type.__name__ = "Integer32"
_WfAppnLocalNnCongested_Object = MibScalar
wfAppnLocalNnCongested = _WfAppnLocalNnCongested_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 5),
    _WfAppnLocalNnCongested_Type()
)
wfAppnLocalNnCongested.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnCongested.setStatus("mandatory")


class _WfAppnLocalNnIsrDepleted_Type(Integer32):
    """Custom type wfAppnLocalNnIsrDepleted based on Integer32"""
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


_WfAppnLocalNnIsrDepleted_Type.__name__ = "Integer32"
_WfAppnLocalNnIsrDepleted_Object = MibScalar
wfAppnLocalNnIsrDepleted = _WfAppnLocalNnIsrDepleted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 6),
    _WfAppnLocalNnIsrDepleted_Type()
)
wfAppnLocalNnIsrDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnIsrDepleted.setStatus("mandatory")


class _WfAppnLocalNnEndptDepleted_Type(Integer32):
    """Custom type wfAppnLocalNnEndptDepleted based on Integer32"""
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


_WfAppnLocalNnEndptDepleted_Type.__name__ = "Integer32"
_WfAppnLocalNnEndptDepleted_Object = MibScalar
wfAppnLocalNnEndptDepleted = _WfAppnLocalNnEndptDepleted_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 7),
    _WfAppnLocalNnEndptDepleted_Type()
)
wfAppnLocalNnEndptDepleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnEndptDepleted.setStatus("mandatory")


class _WfAppnLocalNnQuiescing_Type(Integer32):
    """Custom type wfAppnLocalNnQuiescing based on Integer32"""
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


_WfAppnLocalNnQuiescing_Type.__name__ = "Integer32"
_WfAppnLocalNnQuiescing_Object = MibScalar
wfAppnLocalNnQuiescing = _WfAppnLocalNnQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 8),
    _WfAppnLocalNnQuiescing_Type()
)
wfAppnLocalNnQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnQuiescing.setStatus("mandatory")


class _WfAppnLocalNnGateway_Type(Integer32):
    """Custom type wfAppnLocalNnGateway based on Integer32"""
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


_WfAppnLocalNnGateway_Type.__name__ = "Integer32"
_WfAppnLocalNnGateway_Object = MibScalar
wfAppnLocalNnGateway = _WfAppnLocalNnGateway_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 9),
    _WfAppnLocalNnGateway_Type()
)
wfAppnLocalNnGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnGateway.setStatus("mandatory")


class _WfAppnLocalNnCentralDirectory_Type(Integer32):
    """Custom type wfAppnLocalNnCentralDirectory based on Integer32"""
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


_WfAppnLocalNnCentralDirectory_Type.__name__ = "Integer32"
_WfAppnLocalNnCentralDirectory_Object = MibScalar
wfAppnLocalNnCentralDirectory = _WfAppnLocalNnCentralDirectory_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 10),
    _WfAppnLocalNnCentralDirectory_Type()
)
wfAppnLocalNnCentralDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnCentralDirectory.setStatus("mandatory")


class _WfAppnLocalNnIsr_Type(Integer32):
    """Custom type wfAppnLocalNnIsr based on Integer32"""
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


_WfAppnLocalNnIsr_Type.__name__ = "Integer32"
_WfAppnLocalNnIsr_Object = MibScalar
wfAppnLocalNnIsr = _WfAppnLocalNnIsr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 11),
    _WfAppnLocalNnIsr_Type()
)
wfAppnLocalNnIsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnIsr.setStatus("mandatory")


class _WfAppnLocalNnChainSupport_Type(Integer32):
    """Custom type wfAppnLocalNnChainSupport based on Integer32"""
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


_WfAppnLocalNnChainSupport_Type.__name__ = "Integer32"
_WfAppnLocalNnChainSupport_Object = MibScalar
wfAppnLocalNnChainSupport = _WfAppnLocalNnChainSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 12),
    _WfAppnLocalNnChainSupport_Type()
)
wfAppnLocalNnChainSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnChainSupport.setStatus("mandatory")
_WfAppnLocalNnFrsn_Type = Integer32
_WfAppnLocalNnFrsn_Object = MibScalar
wfAppnLocalNnFrsn = _WfAppnLocalNnFrsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 1, 13),
    _WfAppnLocalNnFrsn_Type()
)
wfAppnLocalNnFrsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalNnFrsn.setStatus("mandatory")
_WfAppnLocalTgTable_Object = MibTable
wfAppnLocalTgTable = _WfAppnLocalTgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3)
)
if mibBuilder.loadTexts:
    wfAppnLocalTgTable.setStatus("mandatory")
_WfAppnLocalTgEntry_Object = MibTableRow
wfAppnLocalTgEntry = _WfAppnLocalTgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1)
)
wfAppnLocalTgEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnLocalTgDest"),
    (0, "Wellfleet-APPN-MIB", "wfAppnLocalTgNum"),
)
if mibBuilder.loadTexts:
    wfAppnLocalTgEntry.setStatus("mandatory")
_WfAppnLocalTgDest_Type = DisplayString
_WfAppnLocalTgDest_Object = MibTableColumn
wfAppnLocalTgDest = _WfAppnLocalTgDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 1),
    _WfAppnLocalTgDest_Type()
)
wfAppnLocalTgDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgDest.setStatus("mandatory")
_WfAppnLocalTgNum_Type = Integer32
_WfAppnLocalTgNum_Object = MibTableColumn
wfAppnLocalTgNum = _WfAppnLocalTgNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 2),
    _WfAppnLocalTgNum_Type()
)
wfAppnLocalTgNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgNum.setStatus("mandatory")
_WfAppnLocalTgDestVirtual_Type = Integer32
_WfAppnLocalTgDestVirtual_Object = MibTableColumn
wfAppnLocalTgDestVirtual = _WfAppnLocalTgDestVirtual_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 3),
    _WfAppnLocalTgDestVirtual_Type()
)
wfAppnLocalTgDestVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgDestVirtual.setStatus("mandatory")
_WfAppnLocalTgDlcData_Type = OctetString
_WfAppnLocalTgDlcData_Object = MibTableColumn
wfAppnLocalTgDlcData = _WfAppnLocalTgDlcData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 4),
    _WfAppnLocalTgDlcData_Type()
)
wfAppnLocalTgDlcData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgDlcData.setStatus("mandatory")
_WfAppnLocalTgRsn_Type = Integer32
_WfAppnLocalTgRsn_Object = MibTableColumn
wfAppnLocalTgRsn = _WfAppnLocalTgRsn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 5),
    _WfAppnLocalTgRsn_Type()
)
wfAppnLocalTgRsn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgRsn.setStatus("mandatory")
_WfAppnLocalTgOperational_Type = Integer32
_WfAppnLocalTgOperational_Object = MibTableColumn
wfAppnLocalTgOperational = _WfAppnLocalTgOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 6),
    _WfAppnLocalTgOperational_Type()
)
wfAppnLocalTgOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgOperational.setStatus("mandatory")
_WfAppnLocalTgQuiescing_Type = Integer32
_WfAppnLocalTgQuiescing_Object = MibTableColumn
wfAppnLocalTgQuiescing = _WfAppnLocalTgQuiescing_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 7),
    _WfAppnLocalTgQuiescing_Type()
)
wfAppnLocalTgQuiescing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgQuiescing.setStatus("mandatory")
_WfAppnLocalTgCpCpSession_Type = Integer32
_WfAppnLocalTgCpCpSession_Object = MibTableColumn
wfAppnLocalTgCpCpSession = _WfAppnLocalTgCpCpSession_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 8),
    _WfAppnLocalTgCpCpSession_Type()
)
wfAppnLocalTgCpCpSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgCpCpSession.setStatus("mandatory")


class _WfAppnLocalTgEffCap_Type(Integer32):
    """Custom type wfAppnLocalTgEffCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnLocalTgEffCap_Type.__name__ = "Integer32"
_WfAppnLocalTgEffCap_Object = MibTableColumn
wfAppnLocalTgEffCap = _WfAppnLocalTgEffCap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 9),
    _WfAppnLocalTgEffCap_Type()
)
wfAppnLocalTgEffCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgEffCap.setStatus("mandatory")
_WfAppnLocalTgConnCost_Type = Integer32
_WfAppnLocalTgConnCost_Object = MibTableColumn
wfAppnLocalTgConnCost = _WfAppnLocalTgConnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 10),
    _WfAppnLocalTgConnCost_Type()
)
wfAppnLocalTgConnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgConnCost.setStatus("mandatory")
_WfAppnLocalTgByteCost_Type = Integer32
_WfAppnLocalTgByteCost_Object = MibTableColumn
wfAppnLocalTgByteCost = _WfAppnLocalTgByteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 11),
    _WfAppnLocalTgByteCost_Type()
)
wfAppnLocalTgByteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgByteCost.setStatus("mandatory")


class _WfAppnLocalTgSecurity_Type(Integer32):
    """Custom type wfAppnLocalTgSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnLocalTgSecurity_Type.__name__ = "Integer32"
_WfAppnLocalTgSecurity_Object = MibTableColumn
wfAppnLocalTgSecurity = _WfAppnLocalTgSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 12),
    _WfAppnLocalTgSecurity_Type()
)
wfAppnLocalTgSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgSecurity.setStatus("mandatory")


class _WfAppnLocalTgDelay_Type(Integer32):
    """Custom type wfAppnLocalTgDelay based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnLocalTgDelay_Type.__name__ = "Integer32"
_WfAppnLocalTgDelay_Object = MibTableColumn
wfAppnLocalTgDelay = _WfAppnLocalTgDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 13),
    _WfAppnLocalTgDelay_Type()
)
wfAppnLocalTgDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnLocalTgDelay.setStatus("mandatory")
_WfAppnLocalTgModemClass_Type = Integer32
_WfAppnLocalTgModemClass_Object = MibTableColumn
wfAppnLocalTgModemClass = _WfAppnLocalTgModemClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 14),
    _WfAppnLocalTgModemClass_Type()
)
wfAppnLocalTgModemClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgModemClass.setStatus("mandatory")
_WfAppnLocalTgUsr1_Type = Integer32
_WfAppnLocalTgUsr1_Object = MibTableColumn
wfAppnLocalTgUsr1 = _WfAppnLocalTgUsr1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 15),
    _WfAppnLocalTgUsr1_Type()
)
wfAppnLocalTgUsr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgUsr1.setStatus("mandatory")
_WfAppnLocalTgUsr2_Type = Integer32
_WfAppnLocalTgUsr2_Object = MibTableColumn
wfAppnLocalTgUsr2 = _WfAppnLocalTgUsr2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 16),
    _WfAppnLocalTgUsr2_Type()
)
wfAppnLocalTgUsr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgUsr2.setStatus("mandatory")
_WfAppnLocalTgUsr3_Type = Integer32
_WfAppnLocalTgUsr3_Object = MibTableColumn
wfAppnLocalTgUsr3 = _WfAppnLocalTgUsr3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 3, 1, 3, 1, 17),
    _WfAppnLocalTgUsr3_Type()
)
wfAppnLocalTgUsr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnLocalTgUsr3.setStatus("mandatory")
_WfAppnDirectory_ObjectIdentity = ObjectIdentity
wfAppnDirectory = _WfAppnDirectory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4)
)
_WfAppnDirectoryPerformance_ObjectIdentity = ObjectIdentity
wfAppnDirectoryPerformance = _WfAppnDirectoryPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1)
)
_WfAppnDirMaxCaches_Type = Integer32
_WfAppnDirMaxCaches_Object = MibScalar
wfAppnDirMaxCaches = _WfAppnDirMaxCaches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 1),
    _WfAppnDirMaxCaches_Type()
)
wfAppnDirMaxCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirMaxCaches.setStatus("mandatory")
_WfAppnDirCurCaches_Type = Gauge32
_WfAppnDirCurCaches_Object = MibScalar
wfAppnDirCurCaches = _WfAppnDirCurCaches_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 2),
    _WfAppnDirCurCaches_Type()
)
wfAppnDirCurCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirCurCaches.setStatus("mandatory")
_WfAppnDirCurHomeEntries_Type = Gauge32
_WfAppnDirCurHomeEntries_Object = MibScalar
wfAppnDirCurHomeEntries = _WfAppnDirCurHomeEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 3),
    _WfAppnDirCurHomeEntries_Type()
)
wfAppnDirCurHomeEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirCurHomeEntries.setStatus("mandatory")
_WfAppnDirRegEntries_Type = Gauge32
_WfAppnDirRegEntries_Object = MibScalar
wfAppnDirRegEntries = _WfAppnDirRegEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 4),
    _WfAppnDirRegEntries_Type()
)
wfAppnDirRegEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirRegEntries.setStatus("mandatory")
_WfAppnDirInLocates_Type = Counter32
_WfAppnDirInLocates_Object = MibScalar
wfAppnDirInLocates = _WfAppnDirInLocates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 5),
    _WfAppnDirInLocates_Type()
)
wfAppnDirInLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirInLocates.setStatus("mandatory")
_WfAppnDirInBcastLocates_Type = Counter32
_WfAppnDirInBcastLocates_Object = MibScalar
wfAppnDirInBcastLocates = _WfAppnDirInBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 6),
    _WfAppnDirInBcastLocates_Type()
)
wfAppnDirInBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirInBcastLocates.setStatus("mandatory")
_WfAppnDirOutLocates_Type = Counter32
_WfAppnDirOutLocates_Object = MibScalar
wfAppnDirOutLocates = _WfAppnDirOutLocates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 7),
    _WfAppnDirOutLocates_Type()
)
wfAppnDirOutLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirOutLocates.setStatus("mandatory")
_WfAppnDirOutBcastLocates_Type = Counter32
_WfAppnDirOutBcastLocates_Object = MibScalar
wfAppnDirOutBcastLocates = _WfAppnDirOutBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 8),
    _WfAppnDirOutBcastLocates_Type()
)
wfAppnDirOutBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirOutBcastLocates.setStatus("mandatory")
_WfAppnDirNotFoundLocates_Type = Counter32
_WfAppnDirNotFoundLocates_Object = MibScalar
wfAppnDirNotFoundLocates = _WfAppnDirNotFoundLocates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 9),
    _WfAppnDirNotFoundLocates_Type()
)
wfAppnDirNotFoundLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirNotFoundLocates.setStatus("mandatory")
_WfAppnDirNotFoundBcastLocates_Type = Counter32
_WfAppnDirNotFoundBcastLocates_Object = MibScalar
wfAppnDirNotFoundBcastLocates = _WfAppnDirNotFoundBcastLocates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 10),
    _WfAppnDirNotFoundBcastLocates_Type()
)
wfAppnDirNotFoundBcastLocates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirNotFoundBcastLocates.setStatus("mandatory")
_WfAppnDirLocateOutstands_Type = Gauge32
_WfAppnDirLocateOutstands_Object = MibScalar
wfAppnDirLocateOutstands = _WfAppnDirLocateOutstands_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 1, 11),
    _WfAppnDirLocateOutstands_Type()
)
wfAppnDirLocateOutstands.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirLocateOutstands.setStatus("mandatory")
_WfAppnDirTable_Object = MibTable
wfAppnDirTable = _WfAppnDirTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2)
)
if mibBuilder.loadTexts:
    wfAppnDirTable.setStatus("mandatory")
_WfAppnDirEntry_Object = MibTableRow
wfAppnDirEntry = _WfAppnDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2, 1)
)
wfAppnDirEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnDirLuName"),
)
if mibBuilder.loadTexts:
    wfAppnDirEntry.setStatus("mandatory")
_WfAppnDirLuName_Type = DisplayString
_WfAppnDirLuName_Object = MibTableColumn
wfAppnDirLuName = _WfAppnDirLuName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2, 1, 1),
    _WfAppnDirLuName_Type()
)
wfAppnDirLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirLuName.setStatus("mandatory")
_WfAppnDirServerName_Type = DisplayString
_WfAppnDirServerName_Object = MibTableColumn
wfAppnDirServerName = _WfAppnDirServerName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2, 1, 2),
    _WfAppnDirServerName_Type()
)
wfAppnDirServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirServerName.setStatus("mandatory")
_WfAppnDirLuOwnerName_Type = DisplayString
_WfAppnDirLuOwnerName_Object = MibTableColumn
wfAppnDirLuOwnerName = _WfAppnDirLuOwnerName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2, 1, 3),
    _WfAppnDirLuOwnerName_Type()
)
wfAppnDirLuOwnerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirLuOwnerName.setStatus("mandatory")


class _WfAppnDirLocation_Type(Integer32):
    """Custom type wfAppnDirLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("domain", 2),
          ("local", 1),
          ("xdomain", 3))
    )


_WfAppnDirLocation_Type.__name__ = "Integer32"
_WfAppnDirLocation_Object = MibTableColumn
wfAppnDirLocation = _WfAppnDirLocation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2, 1, 4),
    _WfAppnDirLocation_Type()
)
wfAppnDirLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirLocation.setStatus("mandatory")


class _WfAppnDirType_Type(Integer32):
    """Custom type wfAppnDirType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cache", 2),
          ("home", 1),
          ("registered", 3))
    )


_WfAppnDirType_Type.__name__ = "Integer32"
_WfAppnDirType_Object = MibTableColumn
wfAppnDirType = _WfAppnDirType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2, 1, 5),
    _WfAppnDirType_Type()
)
wfAppnDirType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirType.setStatus("mandatory")


class _WfAppnDirWildCard_Type(Integer32):
    """Custom type wfAppnDirWildCard based on Integer32"""
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
        *(("entry", 2),
          ("full", 4),
          ("other", 1),
          ("partial", 3))
    )


_WfAppnDirWildCard_Type.__name__ = "Integer32"
_WfAppnDirWildCard_Object = MibTableColumn
wfAppnDirWildCard = _WfAppnDirWildCard_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 2, 1, 6),
    _WfAppnDirWildCard_Type()
)
wfAppnDirWildCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirWildCard.setStatus("mandatory")
_WfAppnDirDefineTable_Object = MibTable
wfAppnDirDefineTable = _WfAppnDirDefineTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3)
)
if mibBuilder.loadTexts:
    wfAppnDirDefineTable.setStatus("mandatory")
_WfAppnDirDefineEntry_Object = MibTableRow
wfAppnDirDefineEntry = _WfAppnDirDefineEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3, 1)
)
wfAppnDirDefineEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnDirDefineResourceName"),
)
if mibBuilder.loadTexts:
    wfAppnDirDefineEntry.setStatus("mandatory")


class _WfAppnDirDefineDelete_Type(Integer32):
    """Custom type wfAppnDirDefineDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnDirDefineDelete_Type.__name__ = "Integer32"
_WfAppnDirDefineDelete_Object = MibTableColumn
wfAppnDirDefineDelete = _WfAppnDirDefineDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3, 1, 1),
    _WfAppnDirDefineDelete_Type()
)
wfAppnDirDefineDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnDirDefineDelete.setStatus("mandatory")


class _WfAppnDirDefineDisable_Type(Integer32):
    """Custom type wfAppnDirDefineDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnDirDefineDisable_Type.__name__ = "Integer32"
_WfAppnDirDefineDisable_Object = MibTableColumn
wfAppnDirDefineDisable = _WfAppnDirDefineDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3, 1, 2),
    _WfAppnDirDefineDisable_Type()
)
wfAppnDirDefineDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnDirDefineDisable.setStatus("mandatory")
_WfAppnDirDefineResourceName_Type = DisplayString
_WfAppnDirDefineResourceName_Object = MibTableColumn
wfAppnDirDefineResourceName = _WfAppnDirDefineResourceName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3, 1, 3),
    _WfAppnDirDefineResourceName_Type()
)
wfAppnDirDefineResourceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDirDefineResourceName.setStatus("mandatory")


class _WfAppnDirDefineResourceType_Type(Integer32):
    """Custom type wfAppnDirDefineResourceType based on Integer32"""
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
        *(("encp", 2),
          ("lu", 1),
          ("nncp", 3),
          ("wildcard", 4))
    )


_WfAppnDirDefineResourceType_Type.__name__ = "Integer32"
_WfAppnDirDefineResourceType_Object = MibTableColumn
wfAppnDirDefineResourceType = _WfAppnDirDefineResourceType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3, 1, 4),
    _WfAppnDirDefineResourceType_Type()
)
wfAppnDirDefineResourceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnDirDefineResourceType.setStatus("mandatory")
_WfAppnDirDefineParentName_Type = DisplayString
_WfAppnDirDefineParentName_Object = MibTableColumn
wfAppnDirDefineParentName = _WfAppnDirDefineParentName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3, 1, 5),
    _WfAppnDirDefineParentName_Type()
)
wfAppnDirDefineParentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnDirDefineParentName.setStatus("mandatory")


class _WfAppnDirDefineParentType_Type(Integer32):
    """Custom type wfAppnDirDefineParentType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("encp", 2),
          ("nncp", 3))
    )


_WfAppnDirDefineParentType_Type.__name__ = "Integer32"
_WfAppnDirDefineParentType_Object = MibTableColumn
wfAppnDirDefineParentType = _WfAppnDirDefineParentType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 4, 3, 1, 6),
    _WfAppnDirDefineParentType_Type()
)
wfAppnDirDefineParentType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnDirDefineParentType.setStatus("mandatory")
_WfAppnCos_ObjectIdentity = ObjectIdentity
wfAppnCos = _WfAppnCos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5)
)
_WfAppnCosModeTable_Object = MibTable
wfAppnCosModeTable = _WfAppnCosModeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 1)
)
if mibBuilder.loadTexts:
    wfAppnCosModeTable.setStatus("mandatory")
_WfAppnCosModeEntry_Object = MibTableRow
wfAppnCosModeEntry = _WfAppnCosModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 1, 1)
)
wfAppnCosModeEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnCosModeName"),
)
if mibBuilder.loadTexts:
    wfAppnCosModeEntry.setStatus("mandatory")
_WfAppnCosModeName_Type = DisplayString
_WfAppnCosModeName_Object = MibTableColumn
wfAppnCosModeName = _WfAppnCosModeName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 1, 1, 1),
    _WfAppnCosModeName_Type()
)
wfAppnCosModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosModeName.setStatus("mandatory")
_WfAppnCosModeCosName_Type = DisplayString
_WfAppnCosModeCosName_Object = MibTableColumn
wfAppnCosModeCosName = _WfAppnCosModeCosName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 1, 1, 2),
    _WfAppnCosModeCosName_Type()
)
wfAppnCosModeCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosModeCosName.setStatus("mandatory")
_WfAppnCosNameTable_Object = MibTable
wfAppnCosNameTable = _WfAppnCosNameTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 2)
)
if mibBuilder.loadTexts:
    wfAppnCosNameTable.setStatus("mandatory")
_WfAppnCosNameEntry_Object = MibTableRow
wfAppnCosNameEntry = _WfAppnCosNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 2, 1)
)
wfAppnCosNameEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnCosName"),
)
if mibBuilder.loadTexts:
    wfAppnCosNameEntry.setStatus("mandatory")
_WfAppnCosName_Type = DisplayString
_WfAppnCosName_Object = MibTableColumn
wfAppnCosName = _WfAppnCosName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 2, 1, 1),
    _WfAppnCosName_Type()
)
wfAppnCosName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosName.setStatus("mandatory")


class _WfAppnCosTransPriority_Type(Integer32):
    """Custom type wfAppnCosTransPriority based on Integer32"""
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
        *(("high", 3),
          ("low", 1),
          ("medium", 2),
          ("network", 4))
    )


_WfAppnCosTransPriority_Type.__name__ = "Integer32"
_WfAppnCosTransPriority_Object = MibTableColumn
wfAppnCosTransPriority = _WfAppnCosTransPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 2, 1, 2),
    _WfAppnCosTransPriority_Type()
)
wfAppnCosTransPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTransPriority.setStatus("mandatory")
_WfAppnCosNodeRowTable_Object = MibTable
wfAppnCosNodeRowTable = _WfAppnCosNodeRowTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3)
)
if mibBuilder.loadTexts:
    wfAppnCosNodeRowTable.setStatus("mandatory")
_WfAppnCosNodeRowEntry_Object = MibTableRow
wfAppnCosNodeRowEntry = _WfAppnCosNodeRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1)
)
wfAppnCosNodeRowEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnCosNodeRowName"),
    (0, "Wellfleet-APPN-MIB", "wfAppnCosNodeRowIndex"),
)
if mibBuilder.loadTexts:
    wfAppnCosNodeRowEntry.setStatus("mandatory")
_WfAppnCosNodeRowName_Type = DisplayString
_WfAppnCosNodeRowName_Object = MibTableColumn
wfAppnCosNodeRowName = _WfAppnCosNodeRowName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1, 1),
    _WfAppnCosNodeRowName_Type()
)
wfAppnCosNodeRowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosNodeRowName.setStatus("mandatory")
_WfAppnCosNodeRowIndex_Type = Integer32
_WfAppnCosNodeRowIndex_Object = MibTableColumn
wfAppnCosNodeRowIndex = _WfAppnCosNodeRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1, 2),
    _WfAppnCosNodeRowIndex_Type()
)
wfAppnCosNodeRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosNodeRowIndex.setStatus("mandatory")
_WfAppnCosNodeRowWgt_Type = Integer32
_WfAppnCosNodeRowWgt_Object = MibTableColumn
wfAppnCosNodeRowWgt = _WfAppnCosNodeRowWgt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1, 3),
    _WfAppnCosNodeRowWgt_Type()
)
wfAppnCosNodeRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosNodeRowWgt.setStatus("mandatory")
_WfAppnCosNodeRowResistMin_Type = Integer32
_WfAppnCosNodeRowResistMin_Object = MibTableColumn
wfAppnCosNodeRowResistMin = _WfAppnCosNodeRowResistMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1, 4),
    _WfAppnCosNodeRowResistMin_Type()
)
wfAppnCosNodeRowResistMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosNodeRowResistMin.setStatus("mandatory")
_WfAppnCosNodeRowResistMax_Type = Integer32
_WfAppnCosNodeRowResistMax_Object = MibTableColumn
wfAppnCosNodeRowResistMax = _WfAppnCosNodeRowResistMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1, 5),
    _WfAppnCosNodeRowResistMax_Type()
)
wfAppnCosNodeRowResistMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosNodeRowResistMax.setStatus("mandatory")


class _WfAppnCosNodeRowMinCongestAllow_Type(Integer32):
    """Custom type wfAppnCosNodeRowMinCongestAllow based on Integer32"""
    defaultValue = 1

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


_WfAppnCosNodeRowMinCongestAllow_Type.__name__ = "Integer32"
_WfAppnCosNodeRowMinCongestAllow_Object = MibTableColumn
wfAppnCosNodeRowMinCongestAllow = _WfAppnCosNodeRowMinCongestAllow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1, 6),
    _WfAppnCosNodeRowMinCongestAllow_Type()
)
wfAppnCosNodeRowMinCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosNodeRowMinCongestAllow.setStatus("mandatory")


class _WfAppnCosNodeRowMaxCongestAllow_Type(Integer32):
    """Custom type wfAppnCosNodeRowMaxCongestAllow based on Integer32"""
    defaultValue = 1

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


_WfAppnCosNodeRowMaxCongestAllow_Type.__name__ = "Integer32"
_WfAppnCosNodeRowMaxCongestAllow_Object = MibTableColumn
wfAppnCosNodeRowMaxCongestAllow = _WfAppnCosNodeRowMaxCongestAllow_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 3, 1, 7),
    _WfAppnCosNodeRowMaxCongestAllow_Type()
)
wfAppnCosNodeRowMaxCongestAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosNodeRowMaxCongestAllow.setStatus("mandatory")
_WfAppnCosTgRowTable_Object = MibTable
wfAppnCosTgRowTable = _WfAppnCosTgRowTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4)
)
if mibBuilder.loadTexts:
    wfAppnCosTgRowTable.setStatus("mandatory")
_WfAppnCosTgRowEntry_Object = MibTableRow
wfAppnCosTgRowEntry = _WfAppnCosTgRowEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1)
)
wfAppnCosTgRowEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnCosTgRowName"),
    (0, "Wellfleet-APPN-MIB", "wfAppnCosTgRowIndex"),
)
if mibBuilder.loadTexts:
    wfAppnCosTgRowEntry.setStatus("mandatory")
_WfAppnCosTgRowName_Type = DisplayString
_WfAppnCosTgRowName_Object = MibTableColumn
wfAppnCosTgRowName = _WfAppnCosTgRowName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 1),
    _WfAppnCosTgRowName_Type()
)
wfAppnCosTgRowName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowName.setStatus("mandatory")
_WfAppnCosTgRowIndex_Type = Integer32
_WfAppnCosTgRowIndex_Object = MibTableColumn
wfAppnCosTgRowIndex = _WfAppnCosTgRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 2),
    _WfAppnCosTgRowIndex_Type()
)
wfAppnCosTgRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowIndex.setStatus("mandatory")
_WfAppnCosTgRowWgt_Type = Integer32
_WfAppnCosTgRowWgt_Object = MibTableColumn
wfAppnCosTgRowWgt = _WfAppnCosTgRowWgt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 3),
    _WfAppnCosTgRowWgt_Type()
)
wfAppnCosTgRowWgt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowWgt.setStatus("mandatory")


class _WfAppnCosTgRowEffCapMin_Type(Integer32):
    """Custom type wfAppnCosTgRowEffCapMin based on Integer32"""
    defaultValue = 133

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnCosTgRowEffCapMin_Type.__name__ = "Integer32"
_WfAppnCosTgRowEffCapMin_Object = MibTableColumn
wfAppnCosTgRowEffCapMin = _WfAppnCosTgRowEffCapMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 4),
    _WfAppnCosTgRowEffCapMin_Type()
)
wfAppnCosTgRowEffCapMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowEffCapMin.setStatus("mandatory")


class _WfAppnCosTgRowEffCapMax_Type(Integer32):
    """Custom type wfAppnCosTgRowEffCapMax based on Integer32"""
    defaultValue = 133

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnCosTgRowEffCapMax_Type.__name__ = "Integer32"
_WfAppnCosTgRowEffCapMax_Object = MibTableColumn
wfAppnCosTgRowEffCapMax = _WfAppnCosTgRowEffCapMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 5),
    _WfAppnCosTgRowEffCapMax_Type()
)
wfAppnCosTgRowEffCapMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowEffCapMax.setStatus("mandatory")
_WfAppnCosTgRowConnCostMin_Type = Integer32
_WfAppnCosTgRowConnCostMin_Object = MibTableColumn
wfAppnCosTgRowConnCostMin = _WfAppnCosTgRowConnCostMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 6),
    _WfAppnCosTgRowConnCostMin_Type()
)
wfAppnCosTgRowConnCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowConnCostMin.setStatus("mandatory")
_WfAppnCosTgRowConnCostMax_Type = Integer32
_WfAppnCosTgRowConnCostMax_Object = MibTableColumn
wfAppnCosTgRowConnCostMax = _WfAppnCosTgRowConnCostMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 7),
    _WfAppnCosTgRowConnCostMax_Type()
)
wfAppnCosTgRowConnCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowConnCostMax.setStatus("mandatory")
_WfAppnCosTgRowByteCostMin_Type = Integer32
_WfAppnCosTgRowByteCostMin_Object = MibTableColumn
wfAppnCosTgRowByteCostMin = _WfAppnCosTgRowByteCostMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 8),
    _WfAppnCosTgRowByteCostMin_Type()
)
wfAppnCosTgRowByteCostMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowByteCostMin.setStatus("mandatory")
_WfAppnCosTgRowByteCostMax_Type = Integer32
_WfAppnCosTgRowByteCostMax_Object = MibTableColumn
wfAppnCosTgRowByteCostMax = _WfAppnCosTgRowByteCostMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 9),
    _WfAppnCosTgRowByteCostMax_Type()
)
wfAppnCosTgRowByteCostMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowByteCostMax.setStatus("mandatory")


class _WfAppnCosTgRowSecurityMin_Type(Integer32):
    """Custom type wfAppnCosTgRowSecurityMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnCosTgRowSecurityMin_Type.__name__ = "Integer32"
_WfAppnCosTgRowSecurityMin_Object = MibTableColumn
wfAppnCosTgRowSecurityMin = _WfAppnCosTgRowSecurityMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 10),
    _WfAppnCosTgRowSecurityMin_Type()
)
wfAppnCosTgRowSecurityMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowSecurityMin.setStatus("mandatory")


class _WfAppnCosTgRowSecurityMax_Type(Integer32):
    """Custom type wfAppnCosTgRowSecurityMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfAppnCosTgRowSecurityMax_Type.__name__ = "Integer32"
_WfAppnCosTgRowSecurityMax_Object = MibTableColumn
wfAppnCosTgRowSecurityMax = _WfAppnCosTgRowSecurityMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 11),
    _WfAppnCosTgRowSecurityMax_Type()
)
wfAppnCosTgRowSecurityMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowSecurityMax.setStatus("mandatory")


class _WfAppnCosTgRowDelayMin_Type(Integer32):
    """Custom type wfAppnCosTgRowDelayMin based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnCosTgRowDelayMin_Type.__name__ = "Integer32"
_WfAppnCosTgRowDelayMin_Object = MibTableColumn
wfAppnCosTgRowDelayMin = _WfAppnCosTgRowDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 12),
    _WfAppnCosTgRowDelayMin_Type()
)
wfAppnCosTgRowDelayMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnCosTgRowDelayMin.setStatus("mandatory")


class _WfAppnCosTgRowDelayMax_Type(Integer32):
    """Custom type wfAppnCosTgRowDelayMax based on Integer32"""
    defaultValue = 1

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
        *(("long", 4),
          ("maximum", 5),
          ("negligible", 1),
          ("packet", 3),
          ("terrestrial", 2))
    )


_WfAppnCosTgRowDelayMax_Type.__name__ = "Integer32"
_WfAppnCosTgRowDelayMax_Object = MibTableColumn
wfAppnCosTgRowDelayMax = _WfAppnCosTgRowDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 13),
    _WfAppnCosTgRowDelayMax_Type()
)
wfAppnCosTgRowDelayMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnCosTgRowDelayMax.setStatus("mandatory")
_WfAppnCosTgRowUsr1Min_Type = Integer32
_WfAppnCosTgRowUsr1Min_Object = MibTableColumn
wfAppnCosTgRowUsr1Min = _WfAppnCosTgRowUsr1Min_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 14),
    _WfAppnCosTgRowUsr1Min_Type()
)
wfAppnCosTgRowUsr1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowUsr1Min.setStatus("mandatory")
_WfAppnCosTgRowUsr1Max_Type = Integer32
_WfAppnCosTgRowUsr1Max_Object = MibTableColumn
wfAppnCosTgRowUsr1Max = _WfAppnCosTgRowUsr1Max_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 15),
    _WfAppnCosTgRowUsr1Max_Type()
)
wfAppnCosTgRowUsr1Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowUsr1Max.setStatus("mandatory")
_WfAppnCosTgRowUsr2Min_Type = Integer32
_WfAppnCosTgRowUsr2Min_Object = MibTableColumn
wfAppnCosTgRowUsr2Min = _WfAppnCosTgRowUsr2Min_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 16),
    _WfAppnCosTgRowUsr2Min_Type()
)
wfAppnCosTgRowUsr2Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowUsr2Min.setStatus("mandatory")
_WfAppnCosTgRowUsr2Max_Type = Integer32
_WfAppnCosTgRowUsr2Max_Object = MibTableColumn
wfAppnCosTgRowUsr2Max = _WfAppnCosTgRowUsr2Max_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 17),
    _WfAppnCosTgRowUsr2Max_Type()
)
wfAppnCosTgRowUsr2Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowUsr2Max.setStatus("mandatory")
_WfAppnCosTgRowUsr3Min_Type = Integer32
_WfAppnCosTgRowUsr3Min_Object = MibTableColumn
wfAppnCosTgRowUsr3Min = _WfAppnCosTgRowUsr3Min_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 18),
    _WfAppnCosTgRowUsr3Min_Type()
)
wfAppnCosTgRowUsr3Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowUsr3Min.setStatus("mandatory")
_WfAppnCosTgRowUsr3Max_Type = Integer32
_WfAppnCosTgRowUsr3Max_Object = MibTableColumn
wfAppnCosTgRowUsr3Max = _WfAppnCosTgRowUsr3Max_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 5, 4, 1, 19),
    _WfAppnCosTgRowUsr3Max_Type()
)
wfAppnCosTgRowUsr3Max.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnCosTgRowUsr3Max.setStatus("mandatory")
_WfAppnTps_ObjectIdentity = ObjectIdentity
wfAppnTps = _WfAppnTps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6)
)
_WfAppnTpPingTable_Object = MibTable
wfAppnTpPingTable = _WfAppnTpPingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1)
)
if mibBuilder.loadTexts:
    wfAppnTpPingTable.setStatus("mandatory")
_WfAppnTpPingEntry_Object = MibTableRow
wfAppnTpPingEntry = _WfAppnTpPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1)
)
wfAppnTpPingEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnTpPingIndex"),
)
if mibBuilder.loadTexts:
    wfAppnTpPingEntry.setStatus("mandatory")


class _WfAppnTpPingDelete_Type(Integer32):
    """Custom type wfAppnTpPingDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnTpPingDelete_Type.__name__ = "Integer32"
_WfAppnTpPingDelete_Object = MibTableColumn
wfAppnTpPingDelete = _WfAppnTpPingDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 1),
    _WfAppnTpPingDelete_Type()
)
wfAppnTpPingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingDelete.setStatus("mandatory")


class _WfAppnTpPingDisable_Type(Integer32):
    """Custom type wfAppnTpPingDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnTpPingDisable_Type.__name__ = "Integer32"
_WfAppnTpPingDisable_Object = MibTableColumn
wfAppnTpPingDisable = _WfAppnTpPingDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 2),
    _WfAppnTpPingDisable_Type()
)
wfAppnTpPingDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingDisable.setStatus("mandatory")
_WfAppnTpPingIndex_Type = Integer32
_WfAppnTpPingIndex_Object = MibTableColumn
wfAppnTpPingIndex = _WfAppnTpPingIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 3),
    _WfAppnTpPingIndex_Type()
)
wfAppnTpPingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpPingIndex.setStatus("mandatory")
_WfAppnTpPingFqPluName_Type = DisplayString
_WfAppnTpPingFqPluName_Object = MibTableColumn
wfAppnTpPingFqPluName = _WfAppnTpPingFqPluName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 4),
    _WfAppnTpPingFqPluName_Type()
)
wfAppnTpPingFqPluName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingFqPluName.setStatus("mandatory")


class _WfAppnTpPingDataLength_Type(Integer32):
    """Custom type wfAppnTpPingDataLength based on Integer32"""
    defaultValue = 100


_WfAppnTpPingDataLength_Object = MibTableColumn
wfAppnTpPingDataLength = _WfAppnTpPingDataLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 5),
    _WfAppnTpPingDataLength_Type()
)
wfAppnTpPingDataLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingDataLength.setStatus("mandatory")


class _WfAppnTpPingConsecutiveSends_Type(Integer32):
    """Custom type wfAppnTpPingConsecutiveSends based on Integer32"""
    defaultValue = 1


_WfAppnTpPingConsecutiveSends_Object = MibTableColumn
wfAppnTpPingConsecutiveSends = _WfAppnTpPingConsecutiveSends_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 6),
    _WfAppnTpPingConsecutiveSends_Type()
)
wfAppnTpPingConsecutiveSends.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingConsecutiveSends.setStatus("mandatory")


class _WfAppnTpPingEchoDisable_Type(Integer32):
    """Custom type wfAppnTpPingEchoDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnTpPingEchoDisable_Type.__name__ = "Integer32"
_WfAppnTpPingEchoDisable_Object = MibTableColumn
wfAppnTpPingEchoDisable = _WfAppnTpPingEchoDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 7),
    _WfAppnTpPingEchoDisable_Type()
)
wfAppnTpPingEchoDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingEchoDisable.setStatus("mandatory")


class _WfAppnTpPingIterations_Type(Integer32):
    """Custom type wfAppnTpPingIterations based on Integer32"""
    defaultValue = 2


_WfAppnTpPingIterations_Object = MibTableColumn
wfAppnTpPingIterations = _WfAppnTpPingIterations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 8),
    _WfAppnTpPingIterations_Type()
)
wfAppnTpPingIterations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingIterations.setStatus("mandatory")
_WfAppnTpPingPartnerTpName_Type = DisplayString
_WfAppnTpPingPartnerTpName_Object = MibTableColumn
wfAppnTpPingPartnerTpName = _WfAppnTpPingPartnerTpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 9),
    _WfAppnTpPingPartnerTpName_Type()
)
wfAppnTpPingPartnerTpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingPartnerTpName.setStatus("mandatory")
_WfAppnTpPingMode_Type = DisplayString
_WfAppnTpPingMode_Object = MibTableColumn
wfAppnTpPingMode = _WfAppnTpPingMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 10),
    _WfAppnTpPingMode_Type()
)
wfAppnTpPingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpPingMode.setStatus("mandatory")


class _WfAppnTpPingState_Type(Integer32):
    """Custom type wfAppnTpPingState based on Integer32"""
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
        *(("failed", 4),
          ("init", 1),
          ("ok", 3),
          ("started", 2))
    )


_WfAppnTpPingState_Type.__name__ = "Integer32"
_WfAppnTpPingState_Object = MibTableColumn
wfAppnTpPingState = _WfAppnTpPingState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 11),
    _WfAppnTpPingState_Type()
)
wfAppnTpPingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpPingState.setStatus("mandatory")
_WfAppnTpPingAllocTime_Type = Integer32
_WfAppnTpPingAllocTime_Object = MibTableColumn
wfAppnTpPingAllocTime = _WfAppnTpPingAllocTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 12),
    _WfAppnTpPingAllocTime_Type()
)
wfAppnTpPingAllocTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpPingAllocTime.setStatus("mandatory")
_WfAppnTpPingMinTime_Type = Integer32
_WfAppnTpPingMinTime_Object = MibTableColumn
wfAppnTpPingMinTime = _WfAppnTpPingMinTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 13),
    _WfAppnTpPingMinTime_Type()
)
wfAppnTpPingMinTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpPingMinTime.setStatus("mandatory")
_WfAppnTpPingMaxTime_Type = Integer32
_WfAppnTpPingMaxTime_Object = MibTableColumn
wfAppnTpPingMaxTime = _WfAppnTpPingMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 14),
    _WfAppnTpPingMaxTime_Type()
)
wfAppnTpPingMaxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpPingMaxTime.setStatus("mandatory")
_WfAppnTpPingAvgTime_Type = Integer32
_WfAppnTpPingAvgTime_Object = MibTableColumn
wfAppnTpPingAvgTime = _WfAppnTpPingAvgTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 15),
    _WfAppnTpPingAvgTime_Type()
)
wfAppnTpPingAvgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpPingAvgTime.setStatus("mandatory")
_WfAppnTpPingPartnerVersion_Type = DisplayString
_WfAppnTpPingPartnerVersion_Object = MibTableColumn
wfAppnTpPingPartnerVersion = _WfAppnTpPingPartnerVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 1, 1, 16),
    _WfAppnTpPingPartnerVersion_Type()
)
wfAppnTpPingPartnerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpPingPartnerVersion.setStatus("mandatory")
_WfAppnTpTunnelTable_Object = MibTable
wfAppnTpTunnelTable = _WfAppnTpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3)
)
if mibBuilder.loadTexts:
    wfAppnTpTunnelTable.setStatus("mandatory")
_WfAppnTpTunnelEntry_Object = MibTableRow
wfAppnTpTunnelEntry = _WfAppnTpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1)
)
wfAppnTpTunnelEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnTpTunnelCct"),
)
if mibBuilder.loadTexts:
    wfAppnTpTunnelEntry.setStatus("mandatory")


class _WfAppnTpTunnelDelete_Type(Integer32):
    """Custom type wfAppnTpTunnelDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnTpTunnelDelete_Type.__name__ = "Integer32"
_WfAppnTpTunnelDelete_Object = MibTableColumn
wfAppnTpTunnelDelete = _WfAppnTpTunnelDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 1),
    _WfAppnTpTunnelDelete_Type()
)
wfAppnTpTunnelDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpTunnelDelete.setStatus("mandatory")


class _WfAppnTpTunnelDisable_Type(Integer32):
    """Custom type wfAppnTpTunnelDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnTpTunnelDisable_Type.__name__ = "Integer32"
_WfAppnTpTunnelDisable_Object = MibTableColumn
wfAppnTpTunnelDisable = _WfAppnTpTunnelDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 2),
    _WfAppnTpTunnelDisable_Type()
)
wfAppnTpTunnelDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpTunnelDisable.setStatus("mandatory")


class _WfAppnTpTunnelState_Type(Integer32):
    """Custom type wfAppnTpTunnelState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfAppnTpTunnelState_Type.__name__ = "Integer32"
_WfAppnTpTunnelState_Object = MibTableColumn
wfAppnTpTunnelState = _WfAppnTpTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 3),
    _WfAppnTpTunnelState_Type()
)
wfAppnTpTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpTunnelState.setStatus("mandatory")
_WfAppnTpTunnelCct_Type = Integer32
_WfAppnTpTunnelCct_Object = MibTableColumn
wfAppnTpTunnelCct = _WfAppnTpTunnelCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 4),
    _WfAppnTpTunnelCct_Type()
)
wfAppnTpTunnelCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpTunnelCct.setStatus("mandatory")
_WfAppnTpTunnelFqPluName_Type = DisplayString
_WfAppnTpTunnelFqPluName_Object = MibTableColumn
wfAppnTpTunnelFqPluName = _WfAppnTpTunnelFqPluName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 5),
    _WfAppnTpTunnelFqPluName_Type()
)
wfAppnTpTunnelFqPluName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpTunnelFqPluName.setStatus("mandatory")
_WfAppnTpTunnelModeName_Type = DisplayString
_WfAppnTpTunnelModeName_Object = MibTableColumn
wfAppnTpTunnelModeName = _WfAppnTpTunnelModeName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 6),
    _WfAppnTpTunnelModeName_Type()
)
wfAppnTpTunnelModeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpTunnelModeName.setStatus("mandatory")


class _WfAppnTpTunnelMedia_Type(Integer32):
    """Custom type wfAppnTpTunnelMedia based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            5
        )
    )
    namedValues = NamedValues(
        ("ring", 5)
    )


_WfAppnTpTunnelMedia_Type.__name__ = "Integer32"
_WfAppnTpTunnelMedia_Object = MibTableColumn
wfAppnTpTunnelMedia = _WfAppnTpTunnelMedia_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 7),
    _WfAppnTpTunnelMedia_Type()
)
wfAppnTpTunnelMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpTunnelMedia.setStatus("mandatory")
_WfAppnTpTunnelMacAddress_Type = OctetString
_WfAppnTpTunnelMacAddress_Object = MibTableColumn
wfAppnTpTunnelMacAddress = _WfAppnTpTunnelMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 8),
    _WfAppnTpTunnelMacAddress_Type()
)
wfAppnTpTunnelMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnTpTunnelMacAddress.setStatus("mandatory")
_WfAppnTpTunnelTxFrames_Type = Counter32
_WfAppnTpTunnelTxFrames_Object = MibTableColumn
wfAppnTpTunnelTxFrames = _WfAppnTpTunnelTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 9),
    _WfAppnTpTunnelTxFrames_Type()
)
wfAppnTpTunnelTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpTunnelTxFrames.setStatus("mandatory")
_WfAppnTpTunnelRxFrames_Type = Counter32
_WfAppnTpTunnelRxFrames_Object = MibTableColumn
wfAppnTpTunnelRxFrames = _WfAppnTpTunnelRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 10),
    _WfAppnTpTunnelRxFrames_Type()
)
wfAppnTpTunnelRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpTunnelRxFrames.setStatus("mandatory")
_WfAppnTpTunnelDropFrames_Type = Counter32
_WfAppnTpTunnelDropFrames_Object = MibTableColumn
wfAppnTpTunnelDropFrames = _WfAppnTpTunnelDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 6, 3, 1, 11),
    _WfAppnTpTunnelDropFrames_Type()
)
wfAppnTpTunnelDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnTpTunnelDropFrames.setStatus("mandatory")
_WfAppnDlu_ObjectIdentity = ObjectIdentity
wfAppnDlu = _WfAppnDlu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7)
)
_WfAppnDlurLuTable_Object = MibTable
wfAppnDlurLuTable = _WfAppnDlurLuTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1)
)
if mibBuilder.loadTexts:
    wfAppnDlurLuTable.setStatus("mandatory")
_WfAppnDlurLuEntry_Object = MibTableRow
wfAppnDlurLuEntry = _WfAppnDlurLuEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1)
)
wfAppnDlurLuEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnDlurLuName"),
)
if mibBuilder.loadTexts:
    wfAppnDlurLuEntry.setStatus("mandatory")
_WfAppnDlurLuName_Type = DisplayString
_WfAppnDlurLuName_Object = MibTableColumn
wfAppnDlurLuName = _WfAppnDlurLuName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1, 1),
    _WfAppnDlurLuName_Type()
)
wfAppnDlurLuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurLuName.setStatus("mandatory")
_WfAppnDlurLuPuName_Type = DisplayString
_WfAppnDlurLuPuName_Object = MibTableColumn
wfAppnDlurLuPuName = _WfAppnDlurLuPuName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1, 2),
    _WfAppnDlurLuPuName_Type()
)
wfAppnDlurLuPuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurLuPuName.setStatus("mandatory")
_WfAppnDlurLuDlusName_Type = DisplayString
_WfAppnDlurLuDlusName_Object = MibTableColumn
wfAppnDlurLuDlusName = _WfAppnDlurLuDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1, 3),
    _WfAppnDlurLuDlusName_Type()
)
wfAppnDlurLuDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurLuDlusName.setStatus("mandatory")
_WfAppnDlurLuNauAddress_Type = Integer32
_WfAppnDlurLuNauAddress_Object = MibTableColumn
wfAppnDlurLuNauAddress = _WfAppnDlurLuNauAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1, 4),
    _WfAppnDlurLuNauAddress_Type()
)
wfAppnDlurLuNauAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurLuNauAddress.setStatus("mandatory")
_WfAppnDlurLuPluName_Type = DisplayString
_WfAppnDlurLuPluName_Object = MibTableColumn
wfAppnDlurLuPluName = _WfAppnDlurLuPluName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1, 5),
    _WfAppnDlurLuPluName_Type()
)
wfAppnDlurLuPluName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurLuPluName.setStatus("mandatory")
_WfAppnDlurLuRscv_Type = OctetString
_WfAppnDlurLuRscv_Object = MibTableColumn
wfAppnDlurLuRscv = _WfAppnDlurLuRscv_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1, 6),
    _WfAppnDlurLuRscv_Type()
)
wfAppnDlurLuRscv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurLuRscv.setStatus("mandatory")
_WfAppnDlurLuRscvText_Type = DisplayString
_WfAppnDlurLuRscvText_Object = MibTableColumn
wfAppnDlurLuRscvText = _WfAppnDlurLuRscvText_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 1, 1, 7),
    _WfAppnDlurLuRscvText_Type()
)
wfAppnDlurLuRscvText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurLuRscvText.setStatus("mandatory")
_WfAppnDlurPuTable_Object = MibTable
wfAppnDlurPuTable = _WfAppnDlurPuTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2)
)
if mibBuilder.loadTexts:
    wfAppnDlurPuTable.setStatus("mandatory")
_WfAppnDlurPuEntry_Object = MibTableRow
wfAppnDlurPuEntry = _WfAppnDlurPuEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1)
)
wfAppnDlurPuEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnDlurPuName"),
)
if mibBuilder.loadTexts:
    wfAppnDlurPuEntry.setStatus("mandatory")
_WfAppnDlurPuName_Type = DisplayString
_WfAppnDlurPuName_Object = MibTableColumn
wfAppnDlurPuName = _WfAppnDlurPuName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1, 1),
    _WfAppnDlurPuName_Type()
)
wfAppnDlurPuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurPuName.setStatus("mandatory")
_WfAppnDlurPuId_Type = OctetString
_WfAppnDlurPuId_Object = MibTableColumn
wfAppnDlurPuId = _WfAppnDlurPuId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1, 2),
    _WfAppnDlurPuId_Type()
)
wfAppnDlurPuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurPuId.setStatus("mandatory")
_WfAppnDlurPuDefinedDlusName_Type = DisplayString
_WfAppnDlurPuDefinedDlusName_Object = MibTableColumn
wfAppnDlurPuDefinedDlusName = _WfAppnDlurPuDefinedDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1, 3),
    _WfAppnDlurPuDefinedDlusName_Type()
)
wfAppnDlurPuDefinedDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurPuDefinedDlusName.setStatus("mandatory")
_WfAppnDlurPuBackupDlusName_Type = DisplayString
_WfAppnDlurPuBackupDlusName_Object = MibTableColumn
wfAppnDlurPuBackupDlusName = _WfAppnDlurPuBackupDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1, 4),
    _WfAppnDlurPuBackupDlusName_Type()
)
wfAppnDlurPuBackupDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurPuBackupDlusName.setStatus("mandatory")
_WfAppnDlurPuActiveDlusName_Type = DisplayString
_WfAppnDlurPuActiveDlusName_Object = MibTableColumn
wfAppnDlurPuActiveDlusName = _WfAppnDlurPuActiveDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1, 5),
    _WfAppnDlurPuActiveDlusName_Type()
)
wfAppnDlurPuActiveDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurPuActiveDlusName.setStatus("mandatory")
_WfAppnDlurPuPcid_Type = OctetString
_WfAppnDlurPuPcid_Object = MibTableColumn
wfAppnDlurPuPcid = _WfAppnDlurPuPcid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1, 6),
    _WfAppnDlurPuPcid_Type()
)
wfAppnDlurPuPcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurPuPcid.setStatus("mandatory")
_WfAppnDlurPuFqCpName_Type = DisplayString
_WfAppnDlurPuFqCpName_Object = MibTableColumn
wfAppnDlurPuFqCpName = _WfAppnDlurPuFqCpName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 2, 1, 7),
    _WfAppnDlurPuFqCpName_Type()
)
wfAppnDlurPuFqCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurPuFqCpName.setStatus("mandatory")
_WfAppnDlurDlusTable_Object = MibTable
wfAppnDlurDlusTable = _WfAppnDlurDlusTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3)
)
if mibBuilder.loadTexts:
    wfAppnDlurDlusTable.setStatus("mandatory")
_WfAppnDlurDlusEntry_Object = MibTableRow
wfAppnDlurDlusEntry = _WfAppnDlurDlusEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1)
)
wfAppnDlurDlusEntry.setIndexNames(
    (0, "Wellfleet-APPN-MIB", "wfAppnDlurDlusName"),
)
if mibBuilder.loadTexts:
    wfAppnDlurDlusEntry.setStatus("mandatory")
_WfAppnDlurDlusName_Type = DisplayString
_WfAppnDlurDlusName_Object = MibTableColumn
wfAppnDlurDlusName = _WfAppnDlurDlusName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 1),
    _WfAppnDlurDlusName_Type()
)
wfAppnDlurDlusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusName.setStatus("mandatory")


class _WfAppnDlurDlusIsDefault_Type(Integer32):
    """Custom type wfAppnDlurDlusIsDefault based on Integer32"""
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


_WfAppnDlurDlusIsDefault_Type.__name__ = "Integer32"
_WfAppnDlurDlusIsDefault_Object = MibTableColumn
wfAppnDlurDlusIsDefault = _WfAppnDlurDlusIsDefault_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 2),
    _WfAppnDlurDlusIsDefault_Type()
)
wfAppnDlurDlusIsDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusIsDefault.setStatus("mandatory")


class _WfAppnDlurDlusIsBackupDefault_Type(Integer32):
    """Custom type wfAppnDlurDlusIsBackupDefault based on Integer32"""
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


_WfAppnDlurDlusIsBackupDefault_Type.__name__ = "Integer32"
_WfAppnDlurDlusIsBackupDefault_Object = MibTableColumn
wfAppnDlurDlusIsBackupDefault = _WfAppnDlurDlusIsBackupDefault_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 3),
    _WfAppnDlurDlusIsBackupDefault_Type()
)
wfAppnDlurDlusIsBackupDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusIsBackupDefault.setStatus("mandatory")


class _WfAppnDlurDlusPipeState_Type(Integer32):
    """Custom type wfAppnDlurDlusPipeState based on Integer32"""
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
        *(("active", 3),
          ("inactive", 1),
          ("pendactive", 2),
          ("pendinact", 4))
    )


_WfAppnDlurDlusPipeState_Type.__name__ = "Integer32"
_WfAppnDlurDlusPipeState_Object = MibTableColumn
wfAppnDlurDlusPipeState = _WfAppnDlurDlusPipeState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 4),
    _WfAppnDlurDlusPipeState_Type()
)
wfAppnDlurDlusPipeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusPipeState.setStatus("mandatory")
_WfAppnDlurDlusActivePus_Type = Integer32
_WfAppnDlurDlusActivePus_Object = MibTableColumn
wfAppnDlurDlusActivePus = _WfAppnDlurDlusActivePus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 5),
    _WfAppnDlurDlusActivePus_Type()
)
wfAppnDlurDlusActivePus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusActivePus.setStatus("mandatory")
_WfAppnDlurDlusSentReqactpus_Type = Counter32
_WfAppnDlurDlusSentReqactpus_Object = MibTableColumn
wfAppnDlurDlusSentReqactpus = _WfAppnDlurDlusSentReqactpus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 6),
    _WfAppnDlurDlusSentReqactpus_Type()
)
wfAppnDlurDlusSentReqactpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentReqactpus.setStatus("mandatory")
_WfAppnDlurDlusRcvReqactpuRsps_Type = Counter32
_WfAppnDlurDlusRcvReqactpuRsps_Object = MibTableColumn
wfAppnDlurDlusRcvReqactpuRsps = _WfAppnDlurDlusRcvReqactpuRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 7),
    _WfAppnDlurDlusRcvReqactpuRsps_Type()
)
wfAppnDlurDlusRcvReqactpuRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvReqactpuRsps.setStatus("mandatory")
_WfAppnDlurDlusRcvActpus_Type = Counter32
_WfAppnDlurDlusRcvActpus_Object = MibTableColumn
wfAppnDlurDlusRcvActpus = _WfAppnDlurDlusRcvActpus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 8),
    _WfAppnDlurDlusRcvActpus_Type()
)
wfAppnDlurDlusRcvActpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvActpus.setStatus("mandatory")
_WfAppnDlurDlusSentActpuRsps_Type = Counter32
_WfAppnDlurDlusSentActpuRsps_Object = MibTableColumn
wfAppnDlurDlusSentActpuRsps = _WfAppnDlurDlusSentActpuRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 9),
    _WfAppnDlurDlusSentActpuRsps_Type()
)
wfAppnDlurDlusSentActpuRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentActpuRsps.setStatus("mandatory")
_WfAppnDlurDlusSentReqdactpus_Type = Counter32
_WfAppnDlurDlusSentReqdactpus_Object = MibTableColumn
wfAppnDlurDlusSentReqdactpus = _WfAppnDlurDlusSentReqdactpus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 10),
    _WfAppnDlurDlusSentReqdactpus_Type()
)
wfAppnDlurDlusSentReqdactpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentReqdactpus.setStatus("mandatory")
_WfAppnDlurDlusRcvReqdactpuRsps_Type = Counter32
_WfAppnDlurDlusRcvReqdactpuRsps_Object = MibTableColumn
wfAppnDlurDlusRcvReqdactpuRsps = _WfAppnDlurDlusRcvReqdactpuRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 11),
    _WfAppnDlurDlusRcvReqdactpuRsps_Type()
)
wfAppnDlurDlusRcvReqdactpuRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvReqdactpuRsps.setStatus("mandatory")
_WfAppnDlurDlusRcvDactpus_Type = Counter32
_WfAppnDlurDlusRcvDactpus_Object = MibTableColumn
wfAppnDlurDlusRcvDactpus = _WfAppnDlurDlusRcvDactpus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 12),
    _WfAppnDlurDlusRcvDactpus_Type()
)
wfAppnDlurDlusRcvDactpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvDactpus.setStatus("mandatory")
_WfAppnDlurDlusSentDactpuRsps_Type = Counter32
_WfAppnDlurDlusSentDactpuRsps_Object = MibTableColumn
wfAppnDlurDlusSentDactpuRsps = _WfAppnDlurDlusSentDactpuRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 13),
    _WfAppnDlurDlusSentDactpuRsps_Type()
)
wfAppnDlurDlusSentDactpuRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentDactpuRsps.setStatus("mandatory")
_WfAppnDlurDlusRcvActlus_Type = Counter32
_WfAppnDlurDlusRcvActlus_Object = MibTableColumn
wfAppnDlurDlusRcvActlus = _WfAppnDlurDlusRcvActlus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 14),
    _WfAppnDlurDlusRcvActlus_Type()
)
wfAppnDlurDlusRcvActlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvActlus.setStatus("mandatory")
_WfAppnDlurDlusSentActluRsps_Type = Counter32
_WfAppnDlurDlusSentActluRsps_Object = MibTableColumn
wfAppnDlurDlusSentActluRsps = _WfAppnDlurDlusSentActluRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 15),
    _WfAppnDlurDlusSentActluRsps_Type()
)
wfAppnDlurDlusSentActluRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentActluRsps.setStatus("mandatory")
_WfAppnDlurDlusRcvDactlus_Type = Counter32
_WfAppnDlurDlusRcvDactlus_Object = MibTableColumn
wfAppnDlurDlusRcvDactlus = _WfAppnDlurDlusRcvDactlus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 16),
    _WfAppnDlurDlusRcvDactlus_Type()
)
wfAppnDlurDlusRcvDactlus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvDactlus.setStatus("mandatory")
_WfAppnDlurDlusSentDactluRsps_Type = Counter32
_WfAppnDlurDlusSentDactluRsps_Object = MibTableColumn
wfAppnDlurDlusSentDactluRsps = _WfAppnDlurDlusSentDactluRsps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 17),
    _WfAppnDlurDlusSentDactluRsps_Type()
)
wfAppnDlurDlusSentDactluRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentDactluRsps.setStatus("mandatory")
_WfAppnDlurDlusRcvSscpPuMus_Type = Counter32
_WfAppnDlurDlusRcvSscpPuMus_Object = MibTableColumn
wfAppnDlurDlusRcvSscpPuMus = _WfAppnDlurDlusRcvSscpPuMus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 18),
    _WfAppnDlurDlusRcvSscpPuMus_Type()
)
wfAppnDlurDlusRcvSscpPuMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvSscpPuMus.setStatus("mandatory")
_WfAppnDlurDlusSentSscpPuMus_Type = Counter32
_WfAppnDlurDlusSentSscpPuMus_Object = MibTableColumn
wfAppnDlurDlusSentSscpPuMus = _WfAppnDlurDlusSentSscpPuMus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 19),
    _WfAppnDlurDlusSentSscpPuMus_Type()
)
wfAppnDlurDlusSentSscpPuMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentSscpPuMus.setStatus("mandatory")
_WfAppnDlurDlusRcvSscpLuMus_Type = Counter32
_WfAppnDlurDlusRcvSscpLuMus_Object = MibTableColumn
wfAppnDlurDlusRcvSscpLuMus = _WfAppnDlurDlusRcvSscpLuMus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 20),
    _WfAppnDlurDlusRcvSscpLuMus_Type()
)
wfAppnDlurDlusRcvSscpLuMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusRcvSscpLuMus.setStatus("mandatory")
_WfAppnDlurDlusSentSscpLuMus_Type = Counter32
_WfAppnDlurDlusSentSscpLuMus_Object = MibTableColumn
wfAppnDlurDlusSentSscpLuMus = _WfAppnDlurDlusSentSscpLuMus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 7, 3, 1, 21),
    _WfAppnDlurDlusSentSscpLuMus_Type()
)
wfAppnDlurDlusSentSscpLuMus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfAppnDlurDlusSentSscpLuMus.setStatus("mandatory")
_WfAppnPathSwitch_ObjectIdentity = ObjectIdentity
wfAppnPathSwitch = _WfAppnPathSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 8)
)


class _WfAppnPathSwitchDelete_Type(Integer32):
    """Custom type wfAppnPathSwitchDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfAppnPathSwitchDelete_Type.__name__ = "Integer32"
_WfAppnPathSwitchDelete_Object = MibScalar
wfAppnPathSwitchDelete = _WfAppnPathSwitchDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 8, 1),
    _WfAppnPathSwitchDelete_Type()
)
wfAppnPathSwitchDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnPathSwitchDelete.setStatus("mandatory")


class _WfAppnPathSwitchDisable_Type(Integer32):
    """Custom type wfAppnPathSwitchDisable based on Integer32"""
    defaultValue = 1

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


_WfAppnPathSwitchDisable_Type.__name__ = "Integer32"
_WfAppnPathSwitchDisable_Object = MibScalar
wfAppnPathSwitchDisable = _WfAppnPathSwitchDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 8, 2),
    _WfAppnPathSwitchDisable_Type()
)
wfAppnPathSwitchDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnPathSwitchDisable.setStatus("mandatory")
_WfAppnPathSwitchRtpConnName_Type = DisplayString
_WfAppnPathSwitchRtpConnName_Object = MibScalar
wfAppnPathSwitchRtpConnName = _WfAppnPathSwitchRtpConnName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 14, 8, 3),
    _WfAppnPathSwitchRtpConnName_Type()
)
wfAppnPathSwitchRtpConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfAppnPathSwitchRtpConnName.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-APPN-MIB",
    **{"wfAppnNode": wfAppnNode,
       "wfAppnNodeInfoAndCaps": wfAppnNodeInfoAndCaps,
       "wfAppnNodeDelete": wfAppnNodeDelete,
       "wfAppnNodeDisable": wfAppnNodeDisable,
       "wfAppnNodeState": wfAppnNodeState,
       "wfAppnNodeCpName": wfAppnNodeCpName,
       "wfAppnNodeNetid": wfAppnNodeNetid,
       "wfAppnNodeBlockNum": wfAppnNodeBlockNum,
       "wfAppnNodeIdNum": wfAppnNodeIdNum,
       "wfAppnNodeType": wfAppnNodeType,
       "wfAppnNodeUpTime": wfAppnNodeUpTime,
       "wfAppnNodeNegotLs": wfAppnNodeNegotLs,
       "wfAppnNodeSegReasm": wfAppnNodeSegReasm,
       "wfAppnNodeBindReasm": wfAppnNodeBindReasm,
       "wfAppnNodeParallelTg": wfAppnNodeParallelTg,
       "wfAppnNodeService": wfAppnNodeService,
       "wfAppnNodeAdaptiveBindPacing": wfAppnNodeAdaptiveBindPacing,
       "wfAppnNodeNnRcvRegChar": wfAppnNodeNnRcvRegChar,
       "wfAppnNodeNnGateway": wfAppnNodeNnGateway,
       "wfAppnNodeNnCentralDirectory": wfAppnNodeNnCentralDirectory,
       "wfAppnNodeNnTreeCache": wfAppnNodeNnTreeCache,
       "wfAppnNodeNnTreeUpdate": wfAppnNodeNnTreeUpdate,
       "wfAppnNodeNnRouteAddResist": wfAppnNodeNnRouteAddResist,
       "wfAppnNodeNnIsr": wfAppnNodeNnIsr,
       "wfAppnNodeNnFrsn": wfAppnNodeNnFrsn,
       "wfAppnNodeModeToCosDisable": wfAppnNodeModeToCosDisable,
       "wfAppnNodeMdsDisable": wfAppnNodeMdsDisable,
       "wfAppnNodeRegWithCdsDisable": wfAppnNodeRegWithCdsDisable,
       "wfAppnNodeAlertQSize": wfAppnNodeAlertQSize,
       "wfAppnNodeCosCacheSize": wfAppnNodeCosCacheSize,
       "wfAppnNodeStoreEndpointRscvsDisable": wfAppnNodeStoreEndpointRscvsDisable,
       "wfAppnNodeNnMaxLocates": wfAppnNodeNnMaxLocates,
       "wfAppnNodeNnDirCacheSize": wfAppnNodeNnDirCacheSize,
       "wfAppnNodeNnMaxDirEntries": wfAppnNodeNnMaxDirEntries,
       "wfAppnNodeNnLocateTimeout": wfAppnNodeNnLocateTimeout,
       "wfAppnNodeNnTreeCacheSize": wfAppnNodeNnTreeCacheSize,
       "wfAppnNodeNnTreeCacheUseLimit": wfAppnNodeNnTreeCacheUseLimit,
       "wfAppnNodeNnMaxTdmNodes": wfAppnNodeNnMaxTdmNodes,
       "wfAppnNodeNnMaxTdmTgs": wfAppnNodeNnMaxTdmTgs,
       "wfAppnNodeNnMaxIsrSessions": wfAppnNodeNnMaxIsrSessions,
       "wfAppnNodeNnIsrSessionUpperThresh": wfAppnNodeNnIsrSessionUpperThresh,
       "wfAppnNodeNnIsrSessionLowerThresh": wfAppnNodeNnIsrSessionLowerThresh,
       "wfAppnNodeNnIsrMaxRuSize": wfAppnNodeNnIsrMaxRuSize,
       "wfAppnNodeNnIsrRcvPacingWindow": wfAppnNodeNnIsrRcvPacingWindow,
       "wfAppnNodeNnStoreIsrRscvsDisable": wfAppnNodeNnStoreIsrRscvsDisable,
       "wfAppnNodeNnStoreDlurRscvsDisable": wfAppnNodeNnStoreDlurRscvsDisable,
       "wfAppnNodeNnDlurDisable": wfAppnNodeNnDlurDisable,
       "wfAppnNodeTotalAvailableMemory": wfAppnNodeTotalAvailableMemory,
       "wfAppnNodeInUseMemory": wfAppnNodeInUseMemory,
       "wfAppnNodeMemoryWarningThreshold": wfAppnNodeMemoryWarningThreshold,
       "wfAppnNodeMemoryCriticalThreshold": wfAppnNodeMemoryCriticalThreshold,
       "wfAppnNodeHprDisable": wfAppnNodeHprDisable,
       "wfAppnNodeHprPathSwitchCtrlrDisable": wfAppnNodeHprPathSwitchCtrlrDisable,
       "wfAppnNodeDebugIpsTraceDisable": wfAppnNodeDebugIpsTraceDisable,
       "wfAppnNodeDebugIpsTraceSize": wfAppnNodeDebugIpsTraceSize,
       "wfAppnNodeDefaultDlusName": wfAppnNodeDefaultDlusName,
       "wfAppnNodeDefaultBackupDlusName": wfAppnNodeDefaultBackupDlusName,
       "wfAppnNodePdLogDisable": wfAppnNodePdLogDisable,
       "wfAppnNodeDlusRetryTimeout": wfAppnNodeDlusRetryTimeout,
       "wfAppnNodeDlusRetryLimit": wfAppnNodeDlusRetryLimit,
       "wfAppnNodeSoloistSlotNum": wfAppnNodeSoloistSlotNum,
       "wfAppnNodeBrNNSupport": wfAppnNodeBrNNSupport,
       "wfAppnNodeRegisterWithNN": wfAppnNodeRegisterWithNN,
       "wfAppnNodeBranchAwarenessEnable": wfAppnNodeBranchAwarenessEnable,
       "wfAppnNodeDlcTable": wfAppnNodeDlcTable,
       "wfAppnNodeDlcEntry": wfAppnNodeDlcEntry,
       "wfAppnNodeDlcDelete": wfAppnNodeDlcDelete,
       "wfAppnNodeDlcDisable": wfAppnNodeDlcDisable,
       "wfAppnNodeDlcName": wfAppnNodeDlcName,
       "wfAppnNodeDlcState": wfAppnNodeDlcState,
       "wfAppnNodeDlcType": wfAppnNodeDlcType,
       "wfAppnNodeDlcNegLsSupportDisable": wfAppnNodeDlcNegLsSupportDisable,
       "wfAppnNodeDlcCct": wfAppnNodeDlcCct,
       "wfAppnNodeDlcData": wfAppnNodeDlcData,
       "wfAppnNodePortTable": wfAppnNodePortTable,
       "wfAppnNodePortEntry": wfAppnNodePortEntry,
       "wfAppnNodePortDelete": wfAppnNodePortDelete,
       "wfAppnNodePortDisable": wfAppnNodePortDisable,
       "wfAppnNodePortName": wfAppnNodePortName,
       "wfAppnNodePortState": wfAppnNodePortState,
       "wfAppnNodePortDlcType": wfAppnNodePortDlcType,
       "wfAppnNodePortPortType": wfAppnNodePortPortType,
       "wfAppnNodePortSIMRIM": wfAppnNodePortSIMRIM,
       "wfAppnNodePortLsRole": wfAppnNodePortLsRole,
       "wfAppnNodePortMaxRcvBtuSize": wfAppnNodePortMaxRcvBtuSize,
       "wfAppnNodePortMaxIframeWindow": wfAppnNodePortMaxIframeWindow,
       "wfAppnNodePortDefLsGoodXids": wfAppnNodePortDefLsGoodXids,
       "wfAppnNodePortDefLsBadXids": wfAppnNodePortDefLsBadXids,
       "wfAppnNodePortDynLsGoodXids": wfAppnNodePortDynLsGoodXids,
       "wfAppnNodePortDynLsBadXids": wfAppnNodePortDynLsBadXids,
       "wfAppnNodePortDlcName": wfAppnNodePortDlcName,
       "wfAppnNodePortNumber": wfAppnNodePortNumber,
       "wfAppnNodePortTotLinkActLim": wfAppnNodePortTotLinkActLim,
       "wfAppnNodePortInbLinkActLim": wfAppnNodePortInbLinkActLim,
       "wfAppnNodePortOutLinkActLim": wfAppnNodePortOutLinkActLim,
       "wfAppnNodePortActXidExchangeLimit": wfAppnNodePortActXidExchangeLimit,
       "wfAppnNodePortNonActXidExchangeLimit": wfAppnNodePortNonActXidExchangeLimit,
       "wfAppnNodePortLsXmitRcvCap": wfAppnNodePortLsXmitRcvCap,
       "wfAppnNodePortTargetPacingCount": wfAppnNodePortTargetPacingCount,
       "wfAppnNodePortMaxSendBtuSize": wfAppnNodePortMaxSendBtuSize,
       "wfAppnNodePortImplicitCpSessions": wfAppnNodePortImplicitCpSessions,
       "wfAppnNodePortImplicitLimResource": wfAppnNodePortImplicitLimResource,
       "wfAppnNodePortImplicitEffCap": wfAppnNodePortImplicitEffCap,
       "wfAppnNodePortImplicitConnCost": wfAppnNodePortImplicitConnCost,
       "wfAppnNodePortImplicitByteCost": wfAppnNodePortImplicitByteCost,
       "wfAppnNodePortImplicitSecurity": wfAppnNodePortImplicitSecurity,
       "wfAppnNodePortImplicitDelay": wfAppnNodePortImplicitDelay,
       "wfAppnNodePortImplicitUsr1": wfAppnNodePortImplicitUsr1,
       "wfAppnNodePortImplicitUsr2": wfAppnNodePortImplicitUsr2,
       "wfAppnNodePortImplicitUsr3": wfAppnNodePortImplicitUsr3,
       "wfAppnNodePortImplicitHprDisable": wfAppnNodePortImplicitHprDisable,
       "wfAppnNodePortImplicitHprLlErrorDisable": wfAppnNodePortImplicitHprLlErrorDisable,
       "wfAppnNodePortImplicitLinkDeactTime": wfAppnNodePortImplicitLinkDeactTime,
       "wfAppnNodePortDlcData": wfAppnNodePortDlcData,
       "wfAppnNodePortHprDlcData": wfAppnNodePortHprDlcData,
       "wfAppnNodePortImplicitDlurDisable": wfAppnNodePortImplicitDlurDisable,
       "wfAppnNodePortImplicitUplinkToEN": wfAppnNodePortImplicitUplinkToEN,
       "wfAppnNodeLsTable": wfAppnNodeLsTable,
       "wfAppnNodeLsEntry": wfAppnNodeLsEntry,
       "wfAppnNodeLsDelete": wfAppnNodeLsDelete,
       "wfAppnNodeLsDisable": wfAppnNodeLsDisable,
       "wfAppnNodeLsName": wfAppnNodeLsName,
       "wfAppnNodeLsPortName": wfAppnNodeLsPortName,
       "wfAppnNodeLsState": wfAppnNodeLsState,
       "wfAppnNodeLsCpName": wfAppnNodeLsCpName,
       "wfAppnNodeLsTgNum": wfAppnNodeLsTgNum,
       "wfAppnNodeLsLimResource": wfAppnNodeLsLimResource,
       "wfAppnNodeLsMigration": wfAppnNodeLsMigration,
       "wfAppnNodeLsBlockNum": wfAppnNodeLsBlockNum,
       "wfAppnNodeLsIdNum": wfAppnNodeLsIdNum,
       "wfAppnNodeLsCpCpSession": wfAppnNodeLsCpCpSession,
       "wfAppnNodeLsTargetPacingCount": wfAppnNodeLsTargetPacingCount,
       "wfAppnNodeLsMaxSendBtuSize": wfAppnNodeLsMaxSendBtuSize,
       "wfAppnNodeLsEffCap": wfAppnNodeLsEffCap,
       "wfAppnNodeLsConnCost": wfAppnNodeLsConnCost,
       "wfAppnNodeLsByteCost": wfAppnNodeLsByteCost,
       "wfAppnNodeLsSecurity": wfAppnNodeLsSecurity,
       "wfAppnNodeLsDelay": wfAppnNodeLsDelay,
       "wfAppnNodeLsUsr1": wfAppnNodeLsUsr1,
       "wfAppnNodeLsUsr2": wfAppnNodeLsUsr2,
       "wfAppnNodeLsUsr3": wfAppnNodeLsUsr3,
       "wfAppnNodeLsCpType": wfAppnNodeLsCpType,
       "wfAppnNodeLsAutoActivateDisable": wfAppnNodeLsAutoActivateDisable,
       "wfAppnNodeLsSolicitSscpSessionsDisable": wfAppnNodeLsSolicitSscpSessionsDisable,
       "wfAppnNodeLsUseDefaultTgChars": wfAppnNodeLsUseDefaultTgChars,
       "wfAppnNodeLsLinkData": wfAppnNodeLsLinkData,
       "wfAppnNodeLsDlurDisable": wfAppnNodeLsDlurDisable,
       "wfAppnNodeLsDspuName": wfAppnNodeLsDspuName,
       "wfAppnNodeLsDlusName": wfAppnNodeLsDlusName,
       "wfAppnNodeLsBackupDlusName": wfAppnNodeLsBackupDlusName,
       "wfAppnNodeLsHprDisable": wfAppnNodeLsHprDisable,
       "wfAppnNodeLsHprLlErrorDisable": wfAppnNodeLsHprLlErrorDisable,
       "wfAppnNodeLsLinkDeactTime": wfAppnNodeLsLinkDeactTime,
       "wfAppnNodeLsLinkRetryCount": wfAppnNodeLsLinkRetryCount,
       "wfAppnNodeLsBranchLinkType": wfAppnNodeLsBranchLinkType,
       "wfAppnNodeLsAdjBrNNLinkSupp": wfAppnNodeLsAdjBrNNLinkSupp,
       "wfAppnNodeLsDefaultNNS": wfAppnNodeLsDefaultNNS,
       "wfAppnNodeLsStatusTable": wfAppnNodeLsStatusTable,
       "wfAppnNodeLsStatusEntry": wfAppnNodeLsStatusEntry,
       "wfAppnNodeLsStatusName": wfAppnNodeLsStatusName,
       "wfAppnNodeLsStatusPortName": wfAppnNodeLsStatusPortName,
       "wfAppnNodeLsStatusDlcType": wfAppnNodeLsStatusDlcType,
       "wfAppnNodeLsStatusDynamic": wfAppnNodeLsStatusDynamic,
       "wfAppnNodeLsStatusState": wfAppnNodeLsStatusState,
       "wfAppnNodeLsStatusCpName": wfAppnNodeLsStatusCpName,
       "wfAppnNodeLsStatusTgNum": wfAppnNodeLsStatusTgNum,
       "wfAppnNodeLsStatusLimResource": wfAppnNodeLsStatusLimResource,
       "wfAppnNodeLsStatusMigration": wfAppnNodeLsStatusMigration,
       "wfAppnNodeLsStatusBlockNum": wfAppnNodeLsStatusBlockNum,
       "wfAppnNodeLsStatusIdNum": wfAppnNodeLsStatusIdNum,
       "wfAppnNodeLsStatusCpCpSession": wfAppnNodeLsStatusCpCpSession,
       "wfAppnNodeLsStatusTargetPacingCount": wfAppnNodeLsStatusTargetPacingCount,
       "wfAppnNodeLsStatusMaxSendBtuSize": wfAppnNodeLsStatusMaxSendBtuSize,
       "wfAppnNodeLsStatusEffCap": wfAppnNodeLsStatusEffCap,
       "wfAppnNodeLsStatusConnCost": wfAppnNodeLsStatusConnCost,
       "wfAppnNodeLsStatusByteCost": wfAppnNodeLsStatusByteCost,
       "wfAppnNodeLsStatusSecurity": wfAppnNodeLsStatusSecurity,
       "wfAppnNodeLsStatusDelay": wfAppnNodeLsStatusDelay,
       "wfAppnNodeLsStatusUsr1": wfAppnNodeLsStatusUsr1,
       "wfAppnNodeLsStatusUsr2": wfAppnNodeLsStatusUsr2,
       "wfAppnNodeLsStatusUsr3": wfAppnNodeLsStatusUsr3,
       "wfAppnNodeLsStatusInXidBytes": wfAppnNodeLsStatusInXidBytes,
       "wfAppnNodeLsStatusInMsgBytes": wfAppnNodeLsStatusInMsgBytes,
       "wfAppnNodeLsStatusInXidFrames": wfAppnNodeLsStatusInXidFrames,
       "wfAppnNodeLsStatusInMsgFrames": wfAppnNodeLsStatusInMsgFrames,
       "wfAppnNodeLsStatusOutXidBytes": wfAppnNodeLsStatusOutXidBytes,
       "wfAppnNodeLsStatusOutMsgBytes": wfAppnNodeLsStatusOutMsgBytes,
       "wfAppnNodeLsStatusOutXidFrames": wfAppnNodeLsStatusOutXidFrames,
       "wfAppnNodeLsStatusOutMsgFrames": wfAppnNodeLsStatusOutMsgFrames,
       "wfAppnNodeLsStatusEchoRsps": wfAppnNodeLsStatusEchoRsps,
       "wfAppnNodeLsStatusCurrentDelay": wfAppnNodeLsStatusCurrentDelay,
       "wfAppnNodeLsStatusMaxDelay": wfAppnNodeLsStatusMaxDelay,
       "wfAppnNodeLsStatusMinDelay": wfAppnNodeLsStatusMinDelay,
       "wfAppnNodeLsStatusMaxDelayTime": wfAppnNodeLsStatusMaxDelayTime,
       "wfAppnNodeLsStatusGoodXids": wfAppnNodeLsStatusGoodXids,
       "wfAppnNodeLsStatusBadXids": wfAppnNodeLsStatusBadXids,
       "wfAppnNodeLsStatusActiveSessions": wfAppnNodeLsStatusActiveSessions,
       "wfAppnNodeLsStatusInvalidSnaFrames": wfAppnNodeLsStatusInvalidSnaFrames,
       "wfAppnNodeLsStatusInScFrames": wfAppnNodeLsStatusInScFrames,
       "wfAppnNodeLsStatusOutScFrames": wfAppnNodeLsStatusOutScFrames,
       "wfAppnNodeLsStatusCpType": wfAppnNodeLsStatusCpType,
       "wfAppnNodeLsStatusStartTime": wfAppnNodeLsStatusStartTime,
       "wfAppnNodeLsStatusStopTime": wfAppnNodeLsStatusStopTime,
       "wfAppnNodeLsStatusUpTime": wfAppnNodeLsStatusUpTime,
       "wfAppnNodeLsStatusDeactCause": wfAppnNodeLsStatusDeactCause,
       "wfAppnNodeLsStatusHprSupport": wfAppnNodeLsStatusHprSupport,
       "wfAppnNodeLsStatusHprLlErrSupport": wfAppnNodeLsStatusHprLlErrSupport,
       "wfAppnNodeLsStatusAnrLabel": wfAppnNodeLsStatusAnrLabel,
       "wfAppnNodeLsStatusLinkData": wfAppnNodeLsStatusLinkData,
       "wfAppnNodeCnTable": wfAppnNodeCnTable,
       "wfAppnNodeCnEntry": wfAppnNodeCnEntry,
       "wfAppnNodeCnDelete": wfAppnNodeCnDelete,
       "wfAppnNodeCnDisable": wfAppnNodeCnDisable,
       "wfAppnNodeCnFqName": wfAppnNodeCnFqName,
       "wfAppnNodeCnState": wfAppnNodeCnState,
       "wfAppnNodeCnEffCap": wfAppnNodeCnEffCap,
       "wfAppnNodeCnConnCost": wfAppnNodeCnConnCost,
       "wfAppnNodeCnByteCost": wfAppnNodeCnByteCost,
       "wfAppnNodeCnSecurity": wfAppnNodeCnSecurity,
       "wfAppnNodeCnDelay": wfAppnNodeCnDelay,
       "wfAppnNodeCnUsr1": wfAppnNodeCnUsr1,
       "wfAppnNodeCnUsr2": wfAppnNodeCnUsr2,
       "wfAppnNodeCnUsr3": wfAppnNodeCnUsr3,
       "wfAppnNodeCnPortTable": wfAppnNodeCnPortTable,
       "wfAppnNodeCnPortEntry": wfAppnNodeCnPortEntry,
       "wfAppnNodeCnPortDelete": wfAppnNodeCnPortDelete,
       "wfAppnNodeCnPortDisable": wfAppnNodeCnPortDisable,
       "wfAppnNodeCnPortCnName": wfAppnNodeCnPortCnName,
       "wfAppnNodeCnPortPortName": wfAppnNodeCnPortPortName,
       "wfAppnNodeCnPortState": wfAppnNodeCnPortState,
       "wfAppnNodeIsrSessionTable": wfAppnNodeIsrSessionTable,
       "wfAppnNodeIsrSessionEntry": wfAppnNodeIsrSessionEntry,
       "wfAppnNodeIsrSessionPcid": wfAppnNodeIsrSessionPcid,
       "wfAppnNodeIsrSessionFqCpName": wfAppnNodeIsrSessionFqCpName,
       "wfAppnNodeIsrSessionTransPriority": wfAppnNodeIsrSessionTransPriority,
       "wfAppnNodeIsrSessionCos": wfAppnNodeIsrSessionCos,
       "wfAppnNodeIsrSessionLimResource": wfAppnNodeIsrSessionLimResource,
       "wfAppnNodeIsrSessionRscv": wfAppnNodeIsrSessionRscv,
       "wfAppnNodeIsrSessionPriSendRuSize": wfAppnNodeIsrSessionPriSendRuSize,
       "wfAppnNodeIsrSessionPriRcvRuSize": wfAppnNodeIsrSessionPriRcvRuSize,
       "wfAppnNodeIsrSessionPriMaxSendBtuSize": wfAppnNodeIsrSessionPriMaxSendBtuSize,
       "wfAppnNodeIsrSessionPriMaxRcvBtuSize": wfAppnNodeIsrSessionPriMaxRcvBtuSize,
       "wfAppnNodeIsrSessionPriMaxSendPacing": wfAppnNodeIsrSessionPriMaxSendPacing,
       "wfAppnNodeIsrSessionPriCurSendPacing": wfAppnNodeIsrSessionPriCurSendPacing,
       "wfAppnNodeIsrSessionPriMaxRcvPacing": wfAppnNodeIsrSessionPriMaxRcvPacing,
       "wfAppnNodeIsrSessionPriCurRcvPacing": wfAppnNodeIsrSessionPriCurRcvPacing,
       "wfAppnNodeIsrSessionPriSendFrames": wfAppnNodeIsrSessionPriSendFrames,
       "wfAppnNodeIsrSessionPriSendBytes": wfAppnNodeIsrSessionPriSendBytes,
       "wfAppnNodeIsrSessionPriSendFmdFrames": wfAppnNodeIsrSessionPriSendFmdFrames,
       "wfAppnNodeIsrSessionPriRcvFrames": wfAppnNodeIsrSessionPriRcvFrames,
       "wfAppnNodeIsrSessionPriRcvBytes": wfAppnNodeIsrSessionPriRcvBytes,
       "wfAppnNodeIsrSessionPriRcvFmdFrames": wfAppnNodeIsrSessionPriRcvFmdFrames,
       "wfAppnNodeIsrSessionPriSidh": wfAppnNodeIsrSessionPriSidh,
       "wfAppnNodeIsrSessionPriSidl": wfAppnNodeIsrSessionPriSidl,
       "wfAppnNodeIsrSessionPriOdai": wfAppnNodeIsrSessionPriOdai,
       "wfAppnNodeIsrSessionPriLsName": wfAppnNodeIsrSessionPriLsName,
       "wfAppnNodeIsrSessionSecSendRuSize": wfAppnNodeIsrSessionSecSendRuSize,
       "wfAppnNodeIsrSessionSecRcvRuSize": wfAppnNodeIsrSessionSecRcvRuSize,
       "wfAppnNodeIsrSessionSecMaxSendBtuSize": wfAppnNodeIsrSessionSecMaxSendBtuSize,
       "wfAppnNodeIsrSessionSecMaxRcvBtuSize": wfAppnNodeIsrSessionSecMaxRcvBtuSize,
       "wfAppnNodeIsrSessionSecMaxSendPacing": wfAppnNodeIsrSessionSecMaxSendPacing,
       "wfAppnNodeIsrSessionSecCurSendPacing": wfAppnNodeIsrSessionSecCurSendPacing,
       "wfAppnNodeIsrSessionSecMaxRcvPacing": wfAppnNodeIsrSessionSecMaxRcvPacing,
       "wfAppnNodeIsrSessionSecCurRcvPacing": wfAppnNodeIsrSessionSecCurRcvPacing,
       "wfAppnNodeIsrSessionSecSendFrames": wfAppnNodeIsrSessionSecSendFrames,
       "wfAppnNodeIsrSessionSecSendBytes": wfAppnNodeIsrSessionSecSendBytes,
       "wfAppnNodeIsrSessionSecSendFmdFrames": wfAppnNodeIsrSessionSecSendFmdFrames,
       "wfAppnNodeIsrSessionSecRcvFrames": wfAppnNodeIsrSessionSecRcvFrames,
       "wfAppnNodeIsrSessionSecRcvBytes": wfAppnNodeIsrSessionSecRcvBytes,
       "wfAppnNodeIsrSessionSecRcvFmdFrames": wfAppnNodeIsrSessionSecRcvFmdFrames,
       "wfAppnNodeIsrSessionSecSidh": wfAppnNodeIsrSessionSecSidh,
       "wfAppnNodeIsrSessionSecSidl": wfAppnNodeIsrSessionSecSidl,
       "wfAppnNodeIsrSessionSecOdai": wfAppnNodeIsrSessionSecOdai,
       "wfAppnNodeIsrSessionSecLsName": wfAppnNodeIsrSessionSecLsName,
       "wfAppnNodeIsrSessionRscvText": wfAppnNodeIsrSessionRscvText,
       "wfAppnNodeEndptSessionTable": wfAppnNodeEndptSessionTable,
       "wfAppnNodeEndptSessionEntry": wfAppnNodeEndptSessionEntry,
       "wfAppnNodeEndptSessionId": wfAppnNodeEndptSessionId,
       "wfAppnNodeEndptSessionPcid": wfAppnNodeEndptSessionPcid,
       "wfAppnNodeEndptSessionFqCpName": wfAppnNodeEndptSessionFqCpName,
       "wfAppnNodeEndptSessionFqPluName": wfAppnNodeEndptSessionFqPluName,
       "wfAppnNodeEndptSessionTransPriority": wfAppnNodeEndptSessionTransPriority,
       "wfAppnNodeEndptSessionMode": wfAppnNodeEndptSessionMode,
       "wfAppnNodeEndptSessionCos": wfAppnNodeEndptSessionCos,
       "wfAppnNodeEndptSessionLimResource": wfAppnNodeEndptSessionLimResource,
       "wfAppnNodeEndptSessionPolarity": wfAppnNodeEndptSessionPolarity,
       "wfAppnNodeEndptSessionContention": wfAppnNodeEndptSessionContention,
       "wfAppnNodeEndptSessionRscv": wfAppnNodeEndptSessionRscv,
       "wfAppnNodeEndptSessionSendRuSize": wfAppnNodeEndptSessionSendRuSize,
       "wfAppnNodeEndptSessionRcvRuSize": wfAppnNodeEndptSessionRcvRuSize,
       "wfAppnNodeEndptSessionMaxSendBtuSize": wfAppnNodeEndptSessionMaxSendBtuSize,
       "wfAppnNodeEndptSessionMaxRcvBtuSize": wfAppnNodeEndptSessionMaxRcvBtuSize,
       "wfAppnNodeEndptSessionMaxSendPacing": wfAppnNodeEndptSessionMaxSendPacing,
       "wfAppnNodeEndptSessionCurSendPacing": wfAppnNodeEndptSessionCurSendPacing,
       "wfAppnNodeEndptSessionMaxRcvPacing": wfAppnNodeEndptSessionMaxRcvPacing,
       "wfAppnNodeEndptSessionCurRcvPacing": wfAppnNodeEndptSessionCurRcvPacing,
       "wfAppnNodeEndptSessionSendFrames": wfAppnNodeEndptSessionSendFrames,
       "wfAppnNodeEndptSessionSendBytes": wfAppnNodeEndptSessionSendBytes,
       "wfAppnNodeEndptSessionSendFmdFrames": wfAppnNodeEndptSessionSendFmdFrames,
       "wfAppnNodeEndptSessionRcvFrames": wfAppnNodeEndptSessionRcvFrames,
       "wfAppnNodeEndptSessionRcvBytes": wfAppnNodeEndptSessionRcvBytes,
       "wfAppnNodeEndptSessionRcvFmdFrames": wfAppnNodeEndptSessionRcvFmdFrames,
       "wfAppnNodeEndptSessionSidh": wfAppnNodeEndptSessionSidh,
       "wfAppnNodeEndptSessionSidl": wfAppnNodeEndptSessionSidl,
       "wfAppnNodeEndptSessionOdai": wfAppnNodeEndptSessionOdai,
       "wfAppnNodeEndptSessionLsName": wfAppnNodeEndptSessionLsName,
       "wfAppnNodeEndptSessionRscvText": wfAppnNodeEndptSessionRscvText,
       "wfAppnNodeTraceGroup": wfAppnNodeTraceGroup,
       "wfAppnNodeTraceDelete": wfAppnNodeTraceDelete,
       "wfAppnNodeTraceDisable": wfAppnNodeTraceDisable,
       "wfAppnNodeTraceFile": wfAppnNodeTraceFile,
       "wfAppnNodeRtpConnectionTable": wfAppnNodeRtpConnectionTable,
       "wfAppnNodeRtpConnectionEntry": wfAppnNodeRtpConnectionEntry,
       "wfAppnNodeRtpConnectionName": wfAppnNodeRtpConnectionName,
       "wfAppnNodeRtpConnectionDestName": wfAppnNodeRtpConnectionDestName,
       "wfAppnNodeRtpConnectionFirstHopLsName": wfAppnNodeRtpConnectionFirstHopLsName,
       "wfAppnNodeRtpConnectionCosName": wfAppnNodeRtpConnectionCosName,
       "wfAppnNodeRtpConnectionMaxBtuSize": wfAppnNodeRtpConnectionMaxBtuSize,
       "wfAppnNodeRtpConnectionLivenessTimer": wfAppnNodeRtpConnectionLivenessTimer,
       "wfAppnNodeRtpConnectionLivenessTimeouts": wfAppnNodeRtpConnectionLivenessTimeouts,
       "wfAppnNodeRtpConnectionLocalTcid": wfAppnNodeRtpConnectionLocalTcid,
       "wfAppnNodeRtpConnectionRemoteTcid": wfAppnNodeRtpConnectionRemoteTcid,
       "wfAppnNodeRtpConnectionActiveSessions": wfAppnNodeRtpConnectionActiveSessions,
       "wfAppnNodeRtpConnectionSendBytes": wfAppnNodeRtpConnectionSendBytes,
       "wfAppnNodeRtpConnectionSendPackets": wfAppnNodeRtpConnectionSendPackets,
       "wfAppnNodeRtpConnectionSendSessionControlFrames": wfAppnNodeRtpConnectionSendSessionControlFrames,
       "wfAppnNodeRtpConnectionSendRate": wfAppnNodeRtpConnectionSendRate,
       "wfAppnNodeRtpConnectionMaxSendRate": wfAppnNodeRtpConnectionMaxSendRate,
       "wfAppnNodeRtpConnectionMinSendRate": wfAppnNodeRtpConnectionMinSendRate,
       "wfAppnNodeRtpConnectionRcvBytes": wfAppnNodeRtpConnectionRcvBytes,
       "wfAppnNodeRtpConnectionRcvPackets": wfAppnNodeRtpConnectionRcvPackets,
       "wfAppnNodeRtpConnectionRcvSessionControlFrames": wfAppnNodeRtpConnectionRcvSessionControlFrames,
       "wfAppnNodeRtpConnectionRcvInvalidSnaFrames": wfAppnNodeRtpConnectionRcvInvalidSnaFrames,
       "wfAppnNodeRtpConnectionRcvRate": wfAppnNodeRtpConnectionRcvRate,
       "wfAppnNodeRtpConnectionMaxRcvRate": wfAppnNodeRtpConnectionMaxRcvRate,
       "wfAppnNodeRtpConnectionMinRcvRate": wfAppnNodeRtpConnectionMinRcvRate,
       "wfAppnNodeRtpConnectionDiscardedBytes": wfAppnNodeRtpConnectionDiscardedBytes,
       "wfAppnNodeRtpConnectionDiscardedPackets": wfAppnNodeRtpConnectionDiscardedPackets,
       "wfAppnNodeRtpConnectionResentBytes": wfAppnNodeRtpConnectionResentBytes,
       "wfAppnNodeRtpConnectionResentPackets": wfAppnNodeRtpConnectionResentPackets,
       "wfAppnNodeRtpConnectionUpTime": wfAppnNodeRtpConnectionUpTime,
       "wfAppnNodeRtpConnectionRoundTripTime": wfAppnNodeRtpConnectionRoundTripTime,
       "wfAppnNodeRtpConnectionSmoothRoundTripTime": wfAppnNodeRtpConnectionSmoothRoundTripTime,
       "wfAppnNodeRtpConnectionBurstSize": wfAppnNodeRtpConnectionBurstSize,
       "wfAppnNodeRtpConnectionSrtExpiries": wfAppnNodeRtpConnectionSrtExpiries,
       "wfAppnNodeRtpConnectionShortReqTimer": wfAppnNodeRtpConnectionShortReqTimer,
       "wfAppnNodeRtpConnectionGapsDetected": wfAppnNodeRtpConnectionGapsDetected,
       "wfAppnNodeRtpConnectionRscv": wfAppnNodeRtpConnectionRscv,
       "wfAppnNodeRtpConnectionRscvText": wfAppnNodeRtpConnectionRscvText,
       "wfAppnNn": wfAppnNn,
       "wfAppnNnTopo": wfAppnNnTopo,
       "wfAppnNnTopoMaxNodes": wfAppnNnTopoMaxNodes,
       "wfAppnNnTopoCurNumNodes": wfAppnNnTopoCurNumNodes,
       "wfAppnNnTopoInTdus": wfAppnNnTopoInTdus,
       "wfAppnNnTopoOutTdus": wfAppnNnTopoOutTdus,
       "wfAppnNnTopoNodeLowRsns": wfAppnNnTopoNodeLowRsns,
       "wfAppnNnTopoNodeEqualRsns": wfAppnNnTopoNodeEqualRsns,
       "wfAppnNnTopoNodeGoodHighRsns": wfAppnNnTopoNodeGoodHighRsns,
       "wfAppnNnTopoNodeBadHighRsns": wfAppnNnTopoNodeBadHighRsns,
       "wfAppnNnTopoNodeStateUpdates": wfAppnNnTopoNodeStateUpdates,
       "wfAppnNnTopoNodeErrors": wfAppnNnTopoNodeErrors,
       "wfAppnNnTopoNodeTimerUpdates": wfAppnNnTopoNodeTimerUpdates,
       "wfAppnNnTopoNodePurges": wfAppnNnTopoNodePurges,
       "wfAppnNnTopoTgLowRsns": wfAppnNnTopoTgLowRsns,
       "wfAppnNnTopoTgEqualRsns": wfAppnNnTopoTgEqualRsns,
       "wfAppnNnTopoTgGoodHighRsns": wfAppnNnTopoTgGoodHighRsns,
       "wfAppnNnTopoTgBadHighRsns": wfAppnNnTopoTgBadHighRsns,
       "wfAppnNnTopoTgStateUpdates": wfAppnNnTopoTgStateUpdates,
       "wfAppnNnTopoTgErrors": wfAppnNnTopoTgErrors,
       "wfAppnNnTopoTgTimerUpdates": wfAppnNnTopoTgTimerUpdates,
       "wfAppnNnTopoTgPurges": wfAppnNnTopoTgPurges,
       "wfAppnNnTopoTotalRouteCalcs": wfAppnNnTopoTotalRouteCalcs,
       "wfAppnNnTopoTotalRouteRejs": wfAppnNnTopoTotalRouteRejs,
       "wfAppnNnAdjNodeTable": wfAppnNnAdjNodeTable,
       "wfAppnNnAdjNodeEntry": wfAppnNnAdjNodeEntry,
       "wfAppnNnAdjNodeAdjName": wfAppnNnAdjNodeAdjName,
       "wfAppnNnAdjNodeCpCpSessStatus": wfAppnNnAdjNodeCpCpSessStatus,
       "wfAppnNnAdjNodeOutOfSeqTdus": wfAppnNnAdjNodeOutOfSeqTdus,
       "wfAppnNnAdjNodeLastFrsnSent": wfAppnNnAdjNodeLastFrsnSent,
       "wfAppnNnAdjNodeLastFrsnRcvd": wfAppnNnAdjNodeLastFrsnRcvd,
       "wfAppnNnTopology": wfAppnNnTopology,
       "wfAppnNnTopologyTable": wfAppnNnTopologyTable,
       "wfAppnNnTopologyEntry": wfAppnNnTopologyEntry,
       "wfAppnNnNodeName": wfAppnNnNodeName,
       "wfAppnNnNodeFrsn": wfAppnNnNodeFrsn,
       "wfAppnNnNodeEntryTimeLeft": wfAppnNnNodeEntryTimeLeft,
       "wfAppnNnNodeType": wfAppnNnNodeType,
       "wfAppnNnNodeRsn": wfAppnNnNodeRsn,
       "wfAppnNnNodeRouteAddResist": wfAppnNnNodeRouteAddResist,
       "wfAppnNnNodeCongested": wfAppnNnNodeCongested,
       "wfAppnNnNodeIsrDepleted": wfAppnNnNodeIsrDepleted,
       "wfAppnNnNodeEndptDepleted": wfAppnNnNodeEndptDepleted,
       "wfAppnNnNodeQuiescing": wfAppnNnNodeQuiescing,
       "wfAppnNnNodeGateway": wfAppnNnNodeGateway,
       "wfAppnNnNodeCentralDirectory": wfAppnNnNodeCentralDirectory,
       "wfAppnNnNodeIsr": wfAppnNnNodeIsr,
       "wfAppnNnNodeChainSupport": wfAppnNnNodeChainSupport,
       "wfAppnNnNodeHprBase": wfAppnNnNodeHprBase,
       "wfAppnNnNodeRtpTower": wfAppnNnNodeRtpTower,
       "wfAppnNnTgTopologyTable": wfAppnNnTgTopologyTable,
       "wfAppnNnTgTopologyEntry": wfAppnNnTgTopologyEntry,
       "wfAppnNnTgOwner": wfAppnNnTgOwner,
       "wfAppnNnTgDest": wfAppnNnTgDest,
       "wfAppnNnTgNum": wfAppnNnTgNum,
       "wfAppnNnTgFrsn": wfAppnNnTgFrsn,
       "wfAppnNnTgEntryTimeLeft": wfAppnNnTgEntryTimeLeft,
       "wfAppnNnTgDestVirtual": wfAppnNnTgDestVirtual,
       "wfAppnNnTgDlcData": wfAppnNnTgDlcData,
       "wfAppnNnTgRsn": wfAppnNnTgRsn,
       "wfAppnNnTgOperational": wfAppnNnTgOperational,
       "wfAppnNnTgQuiescing": wfAppnNnTgQuiescing,
       "wfAppnNnTgCpCpSession": wfAppnNnTgCpCpSession,
       "wfAppnNnTgEffCap": wfAppnNnTgEffCap,
       "wfAppnNnTgConnCost": wfAppnNnTgConnCost,
       "wfAppnNnTgByteCost": wfAppnNnTgByteCost,
       "wfAppnNnTgSecurity": wfAppnNnTgSecurity,
       "wfAppnNnTgDelay": wfAppnNnTgDelay,
       "wfAppnNnTgModemClass": wfAppnNnTgModemClass,
       "wfAppnNnTgUsr1": wfAppnNnTgUsr1,
       "wfAppnNnTgUsr2": wfAppnNnTgUsr2,
       "wfAppnNnTgUsr3": wfAppnNnTgUsr3,
       "wfAppnNnTgHprBase": wfAppnNnTgHprBase,
       "wfAppnNnTgRtpTower": wfAppnNnTgRtpTower,
       "wfAppnNnTopologyFRTable": wfAppnNnTopologyFRTable,
       "wfAppnNnTopologyFREntry": wfAppnNnTopologyFREntry,
       "wfAppnNnNodeFRName": wfAppnNnNodeFRName,
       "wfAppnNnNodeFRFrsn": wfAppnNnNodeFRFrsn,
       "wfAppnNnNodeFREntryTimeLeft": wfAppnNnNodeFREntryTimeLeft,
       "wfAppnNnNodeFRType": wfAppnNnNodeFRType,
       "wfAppnNnNodeFRRsn": wfAppnNnNodeFRRsn,
       "wfAppnNnNodeFRRouteAddResist": wfAppnNnNodeFRRouteAddResist,
       "wfAppnNnNodeFRCongested": wfAppnNnNodeFRCongested,
       "wfAppnNnNodeFRIsrDepleted": wfAppnNnNodeFRIsrDepleted,
       "wfAppnNnNodeFREndptDepleted": wfAppnNnNodeFREndptDepleted,
       "wfAppnNnNodeFRQuiescing": wfAppnNnNodeFRQuiescing,
       "wfAppnNnNodeFRGateway": wfAppnNnNodeFRGateway,
       "wfAppnNnNodeFRCentralDirectory": wfAppnNnNodeFRCentralDirectory,
       "wfAppnNnNodeFRIsr": wfAppnNnNodeFRIsr,
       "wfAppnNnNodeFRChainSupport": wfAppnNnNodeFRChainSupport,
       "wfAppnNnNodeFRHprBase": wfAppnNnNodeFRHprBase,
       "wfAppnNnNodeFRRtpTower": wfAppnNnNodeFRRtpTower,
       "wfAppnNnTgTopologyFRTable": wfAppnNnTgTopologyFRTable,
       "wfAppnNnTgTopologyFREntry": wfAppnNnTgTopologyFREntry,
       "wfAppnNnTgFROwner": wfAppnNnTgFROwner,
       "wfAppnNnTgFRDest": wfAppnNnTgFRDest,
       "wfAppnNnTgFRNum": wfAppnNnTgFRNum,
       "wfAppnNnTgFRFrsn": wfAppnNnTgFRFrsn,
       "wfAppnNnTgFREntryTimeLeft": wfAppnNnTgFREntryTimeLeft,
       "wfAppnNnTgFRDestVirtual": wfAppnNnTgFRDestVirtual,
       "wfAppnNnTgFRDlcData": wfAppnNnTgFRDlcData,
       "wfAppnNnTgFRRsn": wfAppnNnTgFRRsn,
       "wfAppnNnTgFROperational": wfAppnNnTgFROperational,
       "wfAppnNnTgFRQuiescing": wfAppnNnTgFRQuiescing,
       "wfAppnNnTgFRCpCpSession": wfAppnNnTgFRCpCpSession,
       "wfAppnNnTgFREffCap": wfAppnNnTgFREffCap,
       "wfAppnNnTgFRConnCost": wfAppnNnTgFRConnCost,
       "wfAppnNnTgFRByteCost": wfAppnNnTgFRByteCost,
       "wfAppnNnTgFRSecurity": wfAppnNnTgFRSecurity,
       "wfAppnNnTgFRDelay": wfAppnNnTgFRDelay,
       "wfAppnNnTgFRModemClass": wfAppnNnTgFRModemClass,
       "wfAppnNnTgFRUsr1": wfAppnNnTgFRUsr1,
       "wfAppnNnTgFRUsr2": wfAppnNnTgFRUsr2,
       "wfAppnNnTgFRUsr3": wfAppnNnTgFRUsr3,
       "wfAppnNnTgFRHprBase": wfAppnNnTgFRHprBase,
       "wfAppnNnTgFRRtpTower": wfAppnNnTgFRRtpTower,
       "wfAppnLocalTopology": wfAppnLocalTopology,
       "wfAppnLocalThisNode": wfAppnLocalThisNode,
       "wfAppnLocalInfo": wfAppnLocalInfo,
       "wfAppnLocalNodeName": wfAppnLocalNodeName,
       "wfAppnLocalNodeType": wfAppnLocalNodeType,
       "wfAppnLocalNnRsn": wfAppnLocalNnRsn,
       "wfAppnLocalNnRouteAddResist": wfAppnLocalNnRouteAddResist,
       "wfAppnLocalNnCongested": wfAppnLocalNnCongested,
       "wfAppnLocalNnIsrDepleted": wfAppnLocalNnIsrDepleted,
       "wfAppnLocalNnEndptDepleted": wfAppnLocalNnEndptDepleted,
       "wfAppnLocalNnQuiescing": wfAppnLocalNnQuiescing,
       "wfAppnLocalNnGateway": wfAppnLocalNnGateway,
       "wfAppnLocalNnCentralDirectory": wfAppnLocalNnCentralDirectory,
       "wfAppnLocalNnIsr": wfAppnLocalNnIsr,
       "wfAppnLocalNnChainSupport": wfAppnLocalNnChainSupport,
       "wfAppnLocalNnFrsn": wfAppnLocalNnFrsn,
       "wfAppnLocalTgTable": wfAppnLocalTgTable,
       "wfAppnLocalTgEntry": wfAppnLocalTgEntry,
       "wfAppnLocalTgDest": wfAppnLocalTgDest,
       "wfAppnLocalTgNum": wfAppnLocalTgNum,
       "wfAppnLocalTgDestVirtual": wfAppnLocalTgDestVirtual,
       "wfAppnLocalTgDlcData": wfAppnLocalTgDlcData,
       "wfAppnLocalTgRsn": wfAppnLocalTgRsn,
       "wfAppnLocalTgOperational": wfAppnLocalTgOperational,
       "wfAppnLocalTgQuiescing": wfAppnLocalTgQuiescing,
       "wfAppnLocalTgCpCpSession": wfAppnLocalTgCpCpSession,
       "wfAppnLocalTgEffCap": wfAppnLocalTgEffCap,
       "wfAppnLocalTgConnCost": wfAppnLocalTgConnCost,
       "wfAppnLocalTgByteCost": wfAppnLocalTgByteCost,
       "wfAppnLocalTgSecurity": wfAppnLocalTgSecurity,
       "wfAppnLocalTgDelay": wfAppnLocalTgDelay,
       "wfAppnLocalTgModemClass": wfAppnLocalTgModemClass,
       "wfAppnLocalTgUsr1": wfAppnLocalTgUsr1,
       "wfAppnLocalTgUsr2": wfAppnLocalTgUsr2,
       "wfAppnLocalTgUsr3": wfAppnLocalTgUsr3,
       "wfAppnDirectory": wfAppnDirectory,
       "wfAppnDirectoryPerformance": wfAppnDirectoryPerformance,
       "wfAppnDirMaxCaches": wfAppnDirMaxCaches,
       "wfAppnDirCurCaches": wfAppnDirCurCaches,
       "wfAppnDirCurHomeEntries": wfAppnDirCurHomeEntries,
       "wfAppnDirRegEntries": wfAppnDirRegEntries,
       "wfAppnDirInLocates": wfAppnDirInLocates,
       "wfAppnDirInBcastLocates": wfAppnDirInBcastLocates,
       "wfAppnDirOutLocates": wfAppnDirOutLocates,
       "wfAppnDirOutBcastLocates": wfAppnDirOutBcastLocates,
       "wfAppnDirNotFoundLocates": wfAppnDirNotFoundLocates,
       "wfAppnDirNotFoundBcastLocates": wfAppnDirNotFoundBcastLocates,
       "wfAppnDirLocateOutstands": wfAppnDirLocateOutstands,
       "wfAppnDirTable": wfAppnDirTable,
       "wfAppnDirEntry": wfAppnDirEntry,
       "wfAppnDirLuName": wfAppnDirLuName,
       "wfAppnDirServerName": wfAppnDirServerName,
       "wfAppnDirLuOwnerName": wfAppnDirLuOwnerName,
       "wfAppnDirLocation": wfAppnDirLocation,
       "wfAppnDirType": wfAppnDirType,
       "wfAppnDirWildCard": wfAppnDirWildCard,
       "wfAppnDirDefineTable": wfAppnDirDefineTable,
       "wfAppnDirDefineEntry": wfAppnDirDefineEntry,
       "wfAppnDirDefineDelete": wfAppnDirDefineDelete,
       "wfAppnDirDefineDisable": wfAppnDirDefineDisable,
       "wfAppnDirDefineResourceName": wfAppnDirDefineResourceName,
       "wfAppnDirDefineResourceType": wfAppnDirDefineResourceType,
       "wfAppnDirDefineParentName": wfAppnDirDefineParentName,
       "wfAppnDirDefineParentType": wfAppnDirDefineParentType,
       "wfAppnCos": wfAppnCos,
       "wfAppnCosModeTable": wfAppnCosModeTable,
       "wfAppnCosModeEntry": wfAppnCosModeEntry,
       "wfAppnCosModeName": wfAppnCosModeName,
       "wfAppnCosModeCosName": wfAppnCosModeCosName,
       "wfAppnCosNameTable": wfAppnCosNameTable,
       "wfAppnCosNameEntry": wfAppnCosNameEntry,
       "wfAppnCosName": wfAppnCosName,
       "wfAppnCosTransPriority": wfAppnCosTransPriority,
       "wfAppnCosNodeRowTable": wfAppnCosNodeRowTable,
       "wfAppnCosNodeRowEntry": wfAppnCosNodeRowEntry,
       "wfAppnCosNodeRowName": wfAppnCosNodeRowName,
       "wfAppnCosNodeRowIndex": wfAppnCosNodeRowIndex,
       "wfAppnCosNodeRowWgt": wfAppnCosNodeRowWgt,
       "wfAppnCosNodeRowResistMin": wfAppnCosNodeRowResistMin,
       "wfAppnCosNodeRowResistMax": wfAppnCosNodeRowResistMax,
       "wfAppnCosNodeRowMinCongestAllow": wfAppnCosNodeRowMinCongestAllow,
       "wfAppnCosNodeRowMaxCongestAllow": wfAppnCosNodeRowMaxCongestAllow,
       "wfAppnCosTgRowTable": wfAppnCosTgRowTable,
       "wfAppnCosTgRowEntry": wfAppnCosTgRowEntry,
       "wfAppnCosTgRowName": wfAppnCosTgRowName,
       "wfAppnCosTgRowIndex": wfAppnCosTgRowIndex,
       "wfAppnCosTgRowWgt": wfAppnCosTgRowWgt,
       "wfAppnCosTgRowEffCapMin": wfAppnCosTgRowEffCapMin,
       "wfAppnCosTgRowEffCapMax": wfAppnCosTgRowEffCapMax,
       "wfAppnCosTgRowConnCostMin": wfAppnCosTgRowConnCostMin,
       "wfAppnCosTgRowConnCostMax": wfAppnCosTgRowConnCostMax,
       "wfAppnCosTgRowByteCostMin": wfAppnCosTgRowByteCostMin,
       "wfAppnCosTgRowByteCostMax": wfAppnCosTgRowByteCostMax,
       "wfAppnCosTgRowSecurityMin": wfAppnCosTgRowSecurityMin,
       "wfAppnCosTgRowSecurityMax": wfAppnCosTgRowSecurityMax,
       "wfAppnCosTgRowDelayMin": wfAppnCosTgRowDelayMin,
       "wfAppnCosTgRowDelayMax": wfAppnCosTgRowDelayMax,
       "wfAppnCosTgRowUsr1Min": wfAppnCosTgRowUsr1Min,
       "wfAppnCosTgRowUsr1Max": wfAppnCosTgRowUsr1Max,
       "wfAppnCosTgRowUsr2Min": wfAppnCosTgRowUsr2Min,
       "wfAppnCosTgRowUsr2Max": wfAppnCosTgRowUsr2Max,
       "wfAppnCosTgRowUsr3Min": wfAppnCosTgRowUsr3Min,
       "wfAppnCosTgRowUsr3Max": wfAppnCosTgRowUsr3Max,
       "wfAppnTps": wfAppnTps,
       "wfAppnTpPingTable": wfAppnTpPingTable,
       "wfAppnTpPingEntry": wfAppnTpPingEntry,
       "wfAppnTpPingDelete": wfAppnTpPingDelete,
       "wfAppnTpPingDisable": wfAppnTpPingDisable,
       "wfAppnTpPingIndex": wfAppnTpPingIndex,
       "wfAppnTpPingFqPluName": wfAppnTpPingFqPluName,
       "wfAppnTpPingDataLength": wfAppnTpPingDataLength,
       "wfAppnTpPingConsecutiveSends": wfAppnTpPingConsecutiveSends,
       "wfAppnTpPingEchoDisable": wfAppnTpPingEchoDisable,
       "wfAppnTpPingIterations": wfAppnTpPingIterations,
       "wfAppnTpPingPartnerTpName": wfAppnTpPingPartnerTpName,
       "wfAppnTpPingMode": wfAppnTpPingMode,
       "wfAppnTpPingState": wfAppnTpPingState,
       "wfAppnTpPingAllocTime": wfAppnTpPingAllocTime,
       "wfAppnTpPingMinTime": wfAppnTpPingMinTime,
       "wfAppnTpPingMaxTime": wfAppnTpPingMaxTime,
       "wfAppnTpPingAvgTime": wfAppnTpPingAvgTime,
       "wfAppnTpPingPartnerVersion": wfAppnTpPingPartnerVersion,
       "wfAppnTpTunnelTable": wfAppnTpTunnelTable,
       "wfAppnTpTunnelEntry": wfAppnTpTunnelEntry,
       "wfAppnTpTunnelDelete": wfAppnTpTunnelDelete,
       "wfAppnTpTunnelDisable": wfAppnTpTunnelDisable,
       "wfAppnTpTunnelState": wfAppnTpTunnelState,
       "wfAppnTpTunnelCct": wfAppnTpTunnelCct,
       "wfAppnTpTunnelFqPluName": wfAppnTpTunnelFqPluName,
       "wfAppnTpTunnelModeName": wfAppnTpTunnelModeName,
       "wfAppnTpTunnelMedia": wfAppnTpTunnelMedia,
       "wfAppnTpTunnelMacAddress": wfAppnTpTunnelMacAddress,
       "wfAppnTpTunnelTxFrames": wfAppnTpTunnelTxFrames,
       "wfAppnTpTunnelRxFrames": wfAppnTpTunnelRxFrames,
       "wfAppnTpTunnelDropFrames": wfAppnTpTunnelDropFrames,
       "wfAppnDlu": wfAppnDlu,
       "wfAppnDlurLuTable": wfAppnDlurLuTable,
       "wfAppnDlurLuEntry": wfAppnDlurLuEntry,
       "wfAppnDlurLuName": wfAppnDlurLuName,
       "wfAppnDlurLuPuName": wfAppnDlurLuPuName,
       "wfAppnDlurLuDlusName": wfAppnDlurLuDlusName,
       "wfAppnDlurLuNauAddress": wfAppnDlurLuNauAddress,
       "wfAppnDlurLuPluName": wfAppnDlurLuPluName,
       "wfAppnDlurLuRscv": wfAppnDlurLuRscv,
       "wfAppnDlurLuRscvText": wfAppnDlurLuRscvText,
       "wfAppnDlurPuTable": wfAppnDlurPuTable,
       "wfAppnDlurPuEntry": wfAppnDlurPuEntry,
       "wfAppnDlurPuName": wfAppnDlurPuName,
       "wfAppnDlurPuId": wfAppnDlurPuId,
       "wfAppnDlurPuDefinedDlusName": wfAppnDlurPuDefinedDlusName,
       "wfAppnDlurPuBackupDlusName": wfAppnDlurPuBackupDlusName,
       "wfAppnDlurPuActiveDlusName": wfAppnDlurPuActiveDlusName,
       "wfAppnDlurPuPcid": wfAppnDlurPuPcid,
       "wfAppnDlurPuFqCpName": wfAppnDlurPuFqCpName,
       "wfAppnDlurDlusTable": wfAppnDlurDlusTable,
       "wfAppnDlurDlusEntry": wfAppnDlurDlusEntry,
       "wfAppnDlurDlusName": wfAppnDlurDlusName,
       "wfAppnDlurDlusIsDefault": wfAppnDlurDlusIsDefault,
       "wfAppnDlurDlusIsBackupDefault": wfAppnDlurDlusIsBackupDefault,
       "wfAppnDlurDlusPipeState": wfAppnDlurDlusPipeState,
       "wfAppnDlurDlusActivePus": wfAppnDlurDlusActivePus,
       "wfAppnDlurDlusSentReqactpus": wfAppnDlurDlusSentReqactpus,
       "wfAppnDlurDlusRcvReqactpuRsps": wfAppnDlurDlusRcvReqactpuRsps,
       "wfAppnDlurDlusRcvActpus": wfAppnDlurDlusRcvActpus,
       "wfAppnDlurDlusSentActpuRsps": wfAppnDlurDlusSentActpuRsps,
       "wfAppnDlurDlusSentReqdactpus": wfAppnDlurDlusSentReqdactpus,
       "wfAppnDlurDlusRcvReqdactpuRsps": wfAppnDlurDlusRcvReqdactpuRsps,
       "wfAppnDlurDlusRcvDactpus": wfAppnDlurDlusRcvDactpus,
       "wfAppnDlurDlusSentDactpuRsps": wfAppnDlurDlusSentDactpuRsps,
       "wfAppnDlurDlusRcvActlus": wfAppnDlurDlusRcvActlus,
       "wfAppnDlurDlusSentActluRsps": wfAppnDlurDlusSentActluRsps,
       "wfAppnDlurDlusRcvDactlus": wfAppnDlurDlusRcvDactlus,
       "wfAppnDlurDlusSentDactluRsps": wfAppnDlurDlusSentDactluRsps,
       "wfAppnDlurDlusRcvSscpPuMus": wfAppnDlurDlusRcvSscpPuMus,
       "wfAppnDlurDlusSentSscpPuMus": wfAppnDlurDlusSentSscpPuMus,
       "wfAppnDlurDlusRcvSscpLuMus": wfAppnDlurDlusRcvSscpLuMus,
       "wfAppnDlurDlusSentSscpLuMus": wfAppnDlurDlusSentSscpLuMus,
       "wfAppnPathSwitch": wfAppnPathSwitch,
       "wfAppnPathSwitchDelete": wfAppnPathSwitchDelete,
       "wfAppnPathSwitchDisable": wfAppnPathSwitchDisable,
       "wfAppnPathSwitchRtpConnName": wfAppnPathSwitchRtpConnName}
)
