# SNMP MIB module (Wellfleet-SPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-SPAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:07 2024
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

(wfSpanningTree,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSpanningTree")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBrStp_ObjectIdentity = ObjectIdentity
wfBrStp = _WfBrStp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1)
)


class _WfBrStpBaseDelete_Type(Integer32):
    """Custom type wfBrStpBaseDelete based on Integer32"""
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


_WfBrStpBaseDelete_Type.__name__ = "Integer32"
_WfBrStpBaseDelete_Object = MibScalar
wfBrStpBaseDelete = _WfBrStpBaseDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 1),
    _WfBrStpBaseDelete_Type()
)
wfBrStpBaseDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBaseDelete.setStatus("mandatory")


class _WfBrStpBaseEnable_Type(Integer32):
    """Custom type wfBrStpBaseEnable based on Integer32"""
    defaultValue = 1

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


_WfBrStpBaseEnable_Type.__name__ = "Integer32"
_WfBrStpBaseEnable_Object = MibScalar
wfBrStpBaseEnable = _WfBrStpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 2),
    _WfBrStpBaseEnable_Type()
)
wfBrStpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBaseEnable.setStatus("mandatory")


class _WfBrStpBaseState_Type(Integer32):
    """Custom type wfBrStpBaseState based on Integer32"""
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
        *(("down", 2),
          ("init", 3),
          ("pres", 4),
          ("up", 1))
    )


_WfBrStpBaseState_Type.__name__ = "Integer32"
_WfBrStpBaseState_Object = MibScalar
wfBrStpBaseState = _WfBrStpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 3),
    _WfBrStpBaseState_Type()
)
wfBrStpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpBaseState.setStatus("mandatory")


class _WfBrStpProtocolSpecification_Type(Integer32):
    """Custom type wfBrStpProtocolSpecification based on Integer32"""
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
        *(("declb100", 2),
          ("ieee8021d", 3),
          ("unknown", 1))
    )


_WfBrStpProtocolSpecification_Type.__name__ = "Integer32"
_WfBrStpProtocolSpecification_Object = MibScalar
wfBrStpProtocolSpecification = _WfBrStpProtocolSpecification_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 4),
    _WfBrStpProtocolSpecification_Type()
)
wfBrStpProtocolSpecification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpProtocolSpecification.setStatus("mandatory")
_WfBrStpBridgeID_Type = OctetString
_WfBrStpBridgeID_Object = MibScalar
wfBrStpBridgeID = _WfBrStpBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 5),
    _WfBrStpBridgeID_Type()
)
wfBrStpBridgeID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeID.setStatus("mandatory")
_WfBrStpTimeSinceTopologyChange_Type = Counter32
_WfBrStpTimeSinceTopologyChange_Object = MibScalar
wfBrStpTimeSinceTopologyChange = _WfBrStpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 6),
    _WfBrStpTimeSinceTopologyChange_Type()
)
wfBrStpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpTimeSinceTopologyChange.setStatus("mandatory")
_WfBrStpTopChanges_Type = Counter32
_WfBrStpTopChanges_Object = MibScalar
wfBrStpTopChanges = _WfBrStpTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 7),
    _WfBrStpTopChanges_Type()
)
wfBrStpTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpTopChanges.setStatus("mandatory")
_WfBrStpDesignatedRoot_Type = OctetString
_WfBrStpDesignatedRoot_Object = MibScalar
wfBrStpDesignatedRoot = _WfBrStpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 8),
    _WfBrStpDesignatedRoot_Type()
)
wfBrStpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpDesignatedRoot.setStatus("mandatory")
_WfBrStpRootCost_Type = Integer32
_WfBrStpRootCost_Object = MibScalar
wfBrStpRootCost = _WfBrStpRootCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 9),
    _WfBrStpRootCost_Type()
)
wfBrStpRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpRootCost.setStatus("mandatory")
_WfBrStpRootPort_Type = Integer32
_WfBrStpRootPort_Object = MibScalar
wfBrStpRootPort = _WfBrStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 10),
    _WfBrStpRootPort_Type()
)
wfBrStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpRootPort.setStatus("mandatory")
_WfBrStpMaxAge_Type = Integer32
_WfBrStpMaxAge_Object = MibScalar
wfBrStpMaxAge = _WfBrStpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 11),
    _WfBrStpMaxAge_Type()
)
wfBrStpMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpMaxAge.setStatus("mandatory")
_WfBrStpHelloTime_Type = Integer32
_WfBrStpHelloTime_Object = MibScalar
wfBrStpHelloTime = _WfBrStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 12),
    _WfBrStpHelloTime_Type()
)
wfBrStpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpHelloTime.setStatus("mandatory")


class _WfBrStpHoldTime_Type(Integer32):
    """Custom type wfBrStpHoldTime based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            100
        )
    )
    namedValues = NamedValues(
        ("time", 100)
    )


_WfBrStpHoldTime_Type.__name__ = "Integer32"
_WfBrStpHoldTime_Object = MibScalar
wfBrStpHoldTime = _WfBrStpHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 13),
    _WfBrStpHoldTime_Type()
)
wfBrStpHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpHoldTime.setStatus("mandatory")
_WfBrStpForwardDelay_Type = Integer32
_WfBrStpForwardDelay_Object = MibScalar
wfBrStpForwardDelay = _WfBrStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 14),
    _WfBrStpForwardDelay_Type()
)
wfBrStpForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpForwardDelay.setStatus("mandatory")


class _WfBrStpBridgeMaxAge_Type(Integer32):
    """Custom type wfBrStpBridgeMaxAge based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_WfBrStpBridgeMaxAge_Type.__name__ = "Integer32"
_WfBrStpBridgeMaxAge_Object = MibScalar
wfBrStpBridgeMaxAge = _WfBrStpBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 15),
    _WfBrStpBridgeMaxAge_Type()
)
wfBrStpBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeMaxAge.setStatus("mandatory")


class _WfBrStpBridgeHelloTime_Type(Integer32):
    """Custom type wfBrStpBridgeHelloTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_WfBrStpBridgeHelloTime_Type.__name__ = "Integer32"
_WfBrStpBridgeHelloTime_Object = MibScalar
wfBrStpBridgeHelloTime = _WfBrStpBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 16),
    _WfBrStpBridgeHelloTime_Type()
)
wfBrStpBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeHelloTime.setStatus("mandatory")


class _WfBrStpBridgeForwardDelay_Type(Integer32):
    """Custom type wfBrStpBridgeForwardDelay based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_WfBrStpBridgeForwardDelay_Type.__name__ = "Integer32"
_WfBrStpBridgeForwardDelay_Object = MibScalar
wfBrStpBridgeForwardDelay = _WfBrStpBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 17),
    _WfBrStpBridgeForwardDelay_Type()
)
wfBrStpBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBridgeForwardDelay.setStatus("mandatory")


class _WfBrStpBaseTrueConverge_Type(Integer32):
    """Custom type wfBrStpBaseTrueConverge based on Integer32"""
    defaultValue = 2

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


_WfBrStpBaseTrueConverge_Type.__name__ = "Integer32"
_WfBrStpBaseTrueConverge_Object = MibScalar
wfBrStpBaseTrueConverge = _WfBrStpBaseTrueConverge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 1, 18),
    _WfBrStpBaseTrueConverge_Type()
)
wfBrStpBaseTrueConverge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpBaseTrueConverge.setStatus("mandatory")
_WfBrStpInterfaceTable_Object = MibTable
wfBrStpInterfaceTable = _WfBrStpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wfBrStpInterfaceTable.setStatus("mandatory")
_WfBrStpInterfaceEntry_Object = MibTableRow
wfBrStpInterfaceEntry = _WfBrStpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1)
)
wfBrStpInterfaceEntry.setIndexNames(
    (0, "Wellfleet-SPAN-MIB", "wfBrStpInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfBrStpInterfaceEntry.setStatus("mandatory")


class _WfBrStpInterfaceDelete_Type(Integer32):
    """Custom type wfBrStpInterfaceDelete based on Integer32"""
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


_WfBrStpInterfaceDelete_Type.__name__ = "Integer32"
_WfBrStpInterfaceDelete_Object = MibTableColumn
wfBrStpInterfaceDelete = _WfBrStpInterfaceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 1),
    _WfBrStpInterfaceDelete_Type()
)
wfBrStpInterfaceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDelete.setStatus("mandatory")


class _WfBrStpInterfaceEnable_Type(Integer32):
    """Custom type wfBrStpInterfaceEnable based on Integer32"""
    defaultValue = 1

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


_WfBrStpInterfaceEnable_Type.__name__ = "Integer32"
_WfBrStpInterfaceEnable_Object = MibTableColumn
wfBrStpInterfaceEnable = _WfBrStpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 2),
    _WfBrStpInterfaceEnable_Type()
)
wfBrStpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfaceEnable.setStatus("mandatory")
_WfBrStpInterfaceCircuit_Type = Integer32
_WfBrStpInterfaceCircuit_Object = MibTableColumn
wfBrStpInterfaceCircuit = _WfBrStpInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 3),
    _WfBrStpInterfaceCircuit_Type()
)
wfBrStpInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceCircuit.setStatus("mandatory")


class _WfBrStpInterfacePriority_Type(Integer32):
    """Custom type wfBrStpInterfacePriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfBrStpInterfacePriority_Type.__name__ = "Integer32"
_WfBrStpInterfacePriority_Object = MibTableColumn
wfBrStpInterfacePriority = _WfBrStpInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 4),
    _WfBrStpInterfacePriority_Type()
)
wfBrStpInterfacePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfacePriority.setStatus("mandatory")


class _WfBrStpInterfaceState_Type(Integer32):
    """Custom type wfBrStpInterfaceState based on Integer32"""
    defaultValue = 1

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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_WfBrStpInterfaceState_Type.__name__ = "Integer32"
_WfBrStpInterfaceState_Object = MibTableColumn
wfBrStpInterfaceState = _WfBrStpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 5),
    _WfBrStpInterfaceState_Type()
)
wfBrStpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceState.setStatus("mandatory")
_WfBrStpInterfaceMultiCastAddr_Type = OctetString
_WfBrStpInterfaceMultiCastAddr_Object = MibTableColumn
wfBrStpInterfaceMultiCastAddr = _WfBrStpInterfaceMultiCastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 6),
    _WfBrStpInterfaceMultiCastAddr_Type()
)
wfBrStpInterfaceMultiCastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceMultiCastAddr.setStatus("mandatory")


class _WfBrStpInterfacePathCost_Type(Integer32):
    """Custom type wfBrStpInterfacePathCost based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfBrStpInterfacePathCost_Type.__name__ = "Integer32"
_WfBrStpInterfacePathCost_Object = MibTableColumn
wfBrStpInterfacePathCost = _WfBrStpInterfacePathCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 7),
    _WfBrStpInterfacePathCost_Type()
)
wfBrStpInterfacePathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfacePathCost.setStatus("mandatory")
_WfBrStpInterfaceDesignatedRoot_Type = OctetString
_WfBrStpInterfaceDesignatedRoot_Object = MibTableColumn
wfBrStpInterfaceDesignatedRoot = _WfBrStpInterfaceDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 8),
    _WfBrStpInterfaceDesignatedRoot_Type()
)
wfBrStpInterfaceDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedRoot.setStatus("mandatory")
_WfBrStpInterfaceDesignatedCost_Type = Integer32
_WfBrStpInterfaceDesignatedCost_Object = MibTableColumn
wfBrStpInterfaceDesignatedCost = _WfBrStpInterfaceDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 9),
    _WfBrStpInterfaceDesignatedCost_Type()
)
wfBrStpInterfaceDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedCost.setStatus("mandatory")
_WfBrStpInterfaceDesignatedBridge_Type = OctetString
_WfBrStpInterfaceDesignatedBridge_Object = MibTableColumn
wfBrStpInterfaceDesignatedBridge = _WfBrStpInterfaceDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 10),
    _WfBrStpInterfaceDesignatedBridge_Type()
)
wfBrStpInterfaceDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedBridge.setStatus("mandatory")
_WfBrStpInterfaceDesignatedPort_Type = Integer32
_WfBrStpInterfaceDesignatedPort_Object = MibTableColumn
wfBrStpInterfaceDesignatedPort = _WfBrStpInterfaceDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 11),
    _WfBrStpInterfaceDesignatedPort_Type()
)
wfBrStpInterfaceDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceDesignatedPort.setStatus("mandatory")
_WfBrStpInterfaceForwardTransitions_Type = Counter32
_WfBrStpInterfaceForwardTransitions_Object = MibTableColumn
wfBrStpInterfaceForwardTransitions = _WfBrStpInterfaceForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 12),
    _WfBrStpInterfaceForwardTransitions_Type()
)
wfBrStpInterfaceForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfaceForwardTransitions.setStatus("mandatory")
_WfBrStpInterfacePktsXmitd_Type = Counter32
_WfBrStpInterfacePktsXmitd_Object = MibTableColumn
wfBrStpInterfacePktsXmitd = _WfBrStpInterfacePktsXmitd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 13),
    _WfBrStpInterfacePktsXmitd_Type()
)
wfBrStpInterfacePktsXmitd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfacePktsXmitd.setStatus("mandatory")
_WfBrStpInterfacePktsRcvd_Type = Counter32
_WfBrStpInterfacePktsRcvd_Object = MibTableColumn
wfBrStpInterfacePktsRcvd = _WfBrStpInterfacePktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 14),
    _WfBrStpInterfacePktsRcvd_Type()
)
wfBrStpInterfacePktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBrStpInterfacePktsRcvd.setStatus("mandatory")


class _WfBrStpInterfaceTranslationDisable_Type(Integer32):
    """Custom type wfBrStpInterfaceTranslationDisable based on Integer32"""
    defaultValue = 2

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


_WfBrStpInterfaceTranslationDisable_Type.__name__ = "Integer32"
_WfBrStpInterfaceTranslationDisable_Object = MibTableColumn
wfBrStpInterfaceTranslationDisable = _WfBrStpInterfaceTranslationDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 1, 2, 2, 1, 15),
    _WfBrStpInterfaceTranslationDisable_Type()
)
wfBrStpInterfaceTranslationDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBrStpInterfaceTranslationDisable.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-SPAN-MIB",
    **{"wfBrStp": wfBrStp,
       "wfBrStpBaseDelete": wfBrStpBaseDelete,
       "wfBrStpBaseEnable": wfBrStpBaseEnable,
       "wfBrStpBaseState": wfBrStpBaseState,
       "wfBrStpProtocolSpecification": wfBrStpProtocolSpecification,
       "wfBrStpBridgeID": wfBrStpBridgeID,
       "wfBrStpTimeSinceTopologyChange": wfBrStpTimeSinceTopologyChange,
       "wfBrStpTopChanges": wfBrStpTopChanges,
       "wfBrStpDesignatedRoot": wfBrStpDesignatedRoot,
       "wfBrStpRootCost": wfBrStpRootCost,
       "wfBrStpRootPort": wfBrStpRootPort,
       "wfBrStpMaxAge": wfBrStpMaxAge,
       "wfBrStpHelloTime": wfBrStpHelloTime,
       "wfBrStpHoldTime": wfBrStpHoldTime,
       "wfBrStpForwardDelay": wfBrStpForwardDelay,
       "wfBrStpBridgeMaxAge": wfBrStpBridgeMaxAge,
       "wfBrStpBridgeHelloTime": wfBrStpBridgeHelloTime,
       "wfBrStpBridgeForwardDelay": wfBrStpBridgeForwardDelay,
       "wfBrStpBaseTrueConverge": wfBrStpBaseTrueConverge,
       "wfBrStpInterfaceTable": wfBrStpInterfaceTable,
       "wfBrStpInterfaceEntry": wfBrStpInterfaceEntry,
       "wfBrStpInterfaceDelete": wfBrStpInterfaceDelete,
       "wfBrStpInterfaceEnable": wfBrStpInterfaceEnable,
       "wfBrStpInterfaceCircuit": wfBrStpInterfaceCircuit,
       "wfBrStpInterfacePriority": wfBrStpInterfacePriority,
       "wfBrStpInterfaceState": wfBrStpInterfaceState,
       "wfBrStpInterfaceMultiCastAddr": wfBrStpInterfaceMultiCastAddr,
       "wfBrStpInterfacePathCost": wfBrStpInterfacePathCost,
       "wfBrStpInterfaceDesignatedRoot": wfBrStpInterfaceDesignatedRoot,
       "wfBrStpInterfaceDesignatedCost": wfBrStpInterfaceDesignatedCost,
       "wfBrStpInterfaceDesignatedBridge": wfBrStpInterfaceDesignatedBridge,
       "wfBrStpInterfaceDesignatedPort": wfBrStpInterfaceDesignatedPort,
       "wfBrStpInterfaceForwardTransitions": wfBrStpInterfaceForwardTransitions,
       "wfBrStpInterfacePktsXmitd": wfBrStpInterfacePktsXmitd,
       "wfBrStpInterfacePktsRcvd": wfBrStpInterfacePktsRcvd,
       "wfBrStpInterfaceTranslationDisable": wfBrStpInterfaceTranslationDisable}
)
