# SNMP MIB module (ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:30 2024
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

(BridgeId,
 Timeout,
 dot1dBasePort) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBasePort")

(eltMesBridgeExtMIBObjects,) = mibBuilder.importSymbols(
    "ELTEX-MES-BRIDGE-EXT-MIB",
    "eltMesBridgeExtMIBObjects")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PortList,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesStpMultiProcessMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesDot1dStpMultiProcess_ObjectIdentity = ObjectIdentity
eltMesDot1dStpMultiProcess = _EltMesDot1dStpMultiProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1)
)
_Eltdot1dStpMultiProcessTable_Object = MibTable
eltdot1dStpMultiProcessTable = _Eltdot1dStpMultiProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessTable.setStatus("current")
_Eltdot1dStpMultiProcessEntry_Object = MibTableRow
eltdot1dStpMultiProcessEntry = _Eltdot1dStpMultiProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1)
)
eltdot1dStpMultiProcessEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB", "eltdot1dStpMultiProcessId"),
)
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessEntry.setStatus("current")


class _Eltdot1dStpMultiProcessId_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Eltdot1dStpMultiProcessId_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessId_Object = MibTableColumn
eltdot1dStpMultiProcessId = _Eltdot1dStpMultiProcessId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 1),
    _Eltdot1dStpMultiProcessId_Type()
)
eltdot1dStpMultiProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessId.setStatus("current")


class _Eltdot1dStpMultiProcessPriority_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Eltdot1dStpMultiProcessPriority_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPriority_Object = MibTableColumn
eltdot1dStpMultiProcessPriority = _Eltdot1dStpMultiProcessPriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 2),
    _Eltdot1dStpMultiProcessPriority_Type()
)
eltdot1dStpMultiProcessPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPriority.setStatus("current")


class _Eltdot1dStpMultiProcessBridgeMaxAge_Type(Timeout):
    """Custom type eltdot1dStpMultiProcessBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_Eltdot1dStpMultiProcessBridgeMaxAge_Type.__name__ = "Timeout"
_Eltdot1dStpMultiProcessBridgeMaxAge_Object = MibTableColumn
eltdot1dStpMultiProcessBridgeMaxAge = _Eltdot1dStpMultiProcessBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 3),
    _Eltdot1dStpMultiProcessBridgeMaxAge_Type()
)
eltdot1dStpMultiProcessBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessBridgeMaxAge.setStatus("current")


class _Eltdot1dStpMultiProcessBridgeHelloTime_Type(Timeout):
    """Custom type eltdot1dStpMultiProcessBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Eltdot1dStpMultiProcessBridgeHelloTime_Type.__name__ = "Timeout"
_Eltdot1dStpMultiProcessBridgeHelloTime_Object = MibTableColumn
eltdot1dStpMultiProcessBridgeHelloTime = _Eltdot1dStpMultiProcessBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 4),
    _Eltdot1dStpMultiProcessBridgeHelloTime_Type()
)
eltdot1dStpMultiProcessBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessBridgeHelloTime.setStatus("current")


class _Eltdot1dStpMultiProcessBridgeForwardDelay_Type(Timeout):
    """Custom type eltdot1dStpMultiProcessBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_Eltdot1dStpMultiProcessBridgeForwardDelay_Type.__name__ = "Timeout"
_Eltdot1dStpMultiProcessBridgeForwardDelay_Object = MibTableColumn
eltdot1dStpMultiProcessBridgeForwardDelay = _Eltdot1dStpMultiProcessBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 5),
    _Eltdot1dStpMultiProcessBridgeForwardDelay_Type()
)
eltdot1dStpMultiProcessBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessBridgeForwardDelay.setStatus("current")


class _Eltdot1dStpMultiProcessVersion_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stpCompatible", 0))
    )


_Eltdot1dStpMultiProcessVersion_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessVersion_Object = MibTableColumn
eltdot1dStpMultiProcessVersion = _Eltdot1dStpMultiProcessVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 6),
    _Eltdot1dStpMultiProcessVersion_Type()
)
eltdot1dStpMultiProcessVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessVersion.setStatus("current")
_Eltdot1dStpMultiProcessTimeSinceTopologyChange_Type = TimeTicks
_Eltdot1dStpMultiProcessTimeSinceTopologyChange_Object = MibTableColumn
eltdot1dStpMultiProcessTimeSinceTopologyChange = _Eltdot1dStpMultiProcessTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 7),
    _Eltdot1dStpMultiProcessTimeSinceTopologyChange_Type()
)
eltdot1dStpMultiProcessTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessTimeSinceTopologyChange.setStatus("current")
_Eltdot1dStpMultiProcessTopChanges_Type = Counter32
_Eltdot1dStpMultiProcessTopChanges_Object = MibTableColumn
eltdot1dStpMultiProcessTopChanges = _Eltdot1dStpMultiProcessTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 8),
    _Eltdot1dStpMultiProcessTopChanges_Type()
)
eltdot1dStpMultiProcessTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessTopChanges.setStatus("current")
_Eltdot1dStpMultiProcessDesignatedRoot_Type = BridgeId
_Eltdot1dStpMultiProcessDesignatedRoot_Object = MibTableColumn
eltdot1dStpMultiProcessDesignatedRoot = _Eltdot1dStpMultiProcessDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 9),
    _Eltdot1dStpMultiProcessDesignatedRoot_Type()
)
eltdot1dStpMultiProcessDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessDesignatedRoot.setStatus("current")
_Eltdot1dStpMultiProcessRootCost_Type = Integer32
_Eltdot1dStpMultiProcessRootCost_Object = MibTableColumn
eltdot1dStpMultiProcessRootCost = _Eltdot1dStpMultiProcessRootCost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 10),
    _Eltdot1dStpMultiProcessRootCost_Type()
)
eltdot1dStpMultiProcessRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessRootCost.setStatus("current")
_Eltdot1dStpMultiProcessRootPort_Type = Integer32
_Eltdot1dStpMultiProcessRootPort_Object = MibTableColumn
eltdot1dStpMultiProcessRootPort = _Eltdot1dStpMultiProcessRootPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 11),
    _Eltdot1dStpMultiProcessRootPort_Type()
)
eltdot1dStpMultiProcessRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessRootPort.setStatus("current")
_Eltdot1dStpMultiProcessMaxAge_Type = Timeout
_Eltdot1dStpMultiProcessMaxAge_Object = MibTableColumn
eltdot1dStpMultiProcessMaxAge = _Eltdot1dStpMultiProcessMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 12),
    _Eltdot1dStpMultiProcessMaxAge_Type()
)
eltdot1dStpMultiProcessMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessMaxAge.setStatus("current")
_Eltdot1dStpMultiProcessHelloTime_Type = Timeout
_Eltdot1dStpMultiProcessHelloTime_Object = MibTableColumn
eltdot1dStpMultiProcessHelloTime = _Eltdot1dStpMultiProcessHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 13),
    _Eltdot1dStpMultiProcessHelloTime_Type()
)
eltdot1dStpMultiProcessHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessHelloTime.setStatus("current")
_Eltdot1dStpMultiProcessHoldTime_Type = Integer32
_Eltdot1dStpMultiProcessHoldTime_Object = MibTableColumn
eltdot1dStpMultiProcessHoldTime = _Eltdot1dStpMultiProcessHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 14),
    _Eltdot1dStpMultiProcessHoldTime_Type()
)
eltdot1dStpMultiProcessHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessHoldTime.setStatus("current")
_Eltdot1dStpMultiProcessForwardDelay_Type = Timeout
_Eltdot1dStpMultiProcessForwardDelay_Object = MibTableColumn
eltdot1dStpMultiProcessForwardDelay = _Eltdot1dStpMultiProcessForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 15),
    _Eltdot1dStpMultiProcessForwardDelay_Type()
)
eltdot1dStpMultiProcessForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessForwardDelay.setStatus("current")
_Eltdot1dStpMultiProcessRowStatus_Type = RowStatus
_Eltdot1dStpMultiProcessRowStatus_Object = MibTableColumn
eltdot1dStpMultiProcessRowStatus = _Eltdot1dStpMultiProcessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 16),
    _Eltdot1dStpMultiProcessRowStatus_Type()
)
eltdot1dStpMultiProcessRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessRowStatus.setStatus("current")
_Eltdot1dStpMultiProcessLastTopologyChangePort_Type = Integer32
_Eltdot1dStpMultiProcessLastTopologyChangePort_Object = MibTableColumn
eltdot1dStpMultiProcessLastTopologyChangePort = _Eltdot1dStpMultiProcessLastTopologyChangePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 1, 1, 17),
    _Eltdot1dStpMultiProcessLastTopologyChangePort_Type()
)
eltdot1dStpMultiProcessLastTopologyChangePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessLastTopologyChangePort.setStatus("current")
_Eltdot1dStpMultiProcessPortTable_Object = MibTable
eltdot1dStpMultiProcessPortTable = _Eltdot1dStpMultiProcessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2)
)
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortTable.setStatus("current")
_Eltdot1dStpMultiProcessPortEntry_Object = MibTableRow
eltdot1dStpMultiProcessPortEntry = _Eltdot1dStpMultiProcessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1)
)
eltdot1dStpMultiProcessPortEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB", "eltdot1dStpMultiProcessPortPort"),
)
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortEntry.setStatus("current")


class _Eltdot1dStpMultiProcessPortPort_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Eltdot1dStpMultiProcessPortPort_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortPort_Object = MibTableColumn
eltdot1dStpMultiProcessPortPort = _Eltdot1dStpMultiProcessPortPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 1),
    _Eltdot1dStpMultiProcessPortPort_Type()
)
eltdot1dStpMultiProcessPortPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortPort.setStatus("current")


class _Eltdot1dStpMultiProcessPortProcessId_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortProcessId_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortProcessId_Object = MibTableColumn
eltdot1dStpMultiProcessPortProcessId = _Eltdot1dStpMultiProcessPortProcessId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 2),
    _Eltdot1dStpMultiProcessPortProcessId_Type()
)
eltdot1dStpMultiProcessPortProcessId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortProcessId.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId1_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId1_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId1_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId1 = _Eltdot1dStpMultiProcessPortSharedProcessId1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 3),
    _Eltdot1dStpMultiProcessPortSharedProcessId1_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId1.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId2_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId2_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId2_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId2 = _Eltdot1dStpMultiProcessPortSharedProcessId2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 4),
    _Eltdot1dStpMultiProcessPortSharedProcessId2_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId2.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId3_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId3_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId3_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId3 = _Eltdot1dStpMultiProcessPortSharedProcessId3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 5),
    _Eltdot1dStpMultiProcessPortSharedProcessId3_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId3.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId4_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId4_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId4_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId4 = _Eltdot1dStpMultiProcessPortSharedProcessId4_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 6),
    _Eltdot1dStpMultiProcessPortSharedProcessId4_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId4.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId5_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId5_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId5_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId5 = _Eltdot1dStpMultiProcessPortSharedProcessId5_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 7),
    _Eltdot1dStpMultiProcessPortSharedProcessId5_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId5.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId6_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId6_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId6_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId6 = _Eltdot1dStpMultiProcessPortSharedProcessId6_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 8),
    _Eltdot1dStpMultiProcessPortSharedProcessId6_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId6.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId7_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId7_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId7_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId7 = _Eltdot1dStpMultiProcessPortSharedProcessId7_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 9),
    _Eltdot1dStpMultiProcessPortSharedProcessId7_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId7.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId8_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId8_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId8_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId8 = _Eltdot1dStpMultiProcessPortSharedProcessId8_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 10),
    _Eltdot1dStpMultiProcessPortSharedProcessId8_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId8.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId9_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId9_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId9_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId9 = _Eltdot1dStpMultiProcessPortSharedProcessId9_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 11),
    _Eltdot1dStpMultiProcessPortSharedProcessId9_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId9.setStatus("current")


class _Eltdot1dStpMultiProcessPortSharedProcessId10_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortSharedProcessId10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortSharedProcessId10_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortSharedProcessId10_Object = MibTableColumn
eltdot1dStpMultiProcessPortSharedProcessId10 = _Eltdot1dStpMultiProcessPortSharedProcessId10_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 2, 1, 12),
    _Eltdot1dStpMultiProcessPortSharedProcessId10_Type()
)
eltdot1dStpMultiProcessPortSharedProcessId10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortSharedProcessId10.setStatus("current")
_Eltdot1dStpMultiProcessPortListTable_Object = MibTable
eltdot1dStpMultiProcessPortListTable = _Eltdot1dStpMultiProcessPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 3)
)
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortListTable.setStatus("current")
_Eltdot1dStpMultiProcessPortListEntry_Object = MibTableRow
eltdot1dStpMultiProcessPortListEntry = _Eltdot1dStpMultiProcessPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 3, 1)
)
eltdot1dStpMultiProcessPortListEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB", "eltdot1dStpMultiProcessPortListProcessId"),
)
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortListEntry.setStatus("current")


class _Eltdot1dStpMultiProcessPortListProcessId_Type(Integer32):
    """Custom type eltdot1dStpMultiProcessPortListProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Eltdot1dStpMultiProcessPortListProcessId_Type.__name__ = "Integer32"
_Eltdot1dStpMultiProcessPortListProcessId_Object = MibTableColumn
eltdot1dStpMultiProcessPortListProcessId = _Eltdot1dStpMultiProcessPortListProcessId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 3, 1, 1),
    _Eltdot1dStpMultiProcessPortListProcessId_Type()
)
eltdot1dStpMultiProcessPortListProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortListProcessId.setStatus("current")
_Eltdot1dStpMultiProcessPortList_Type = PortList
_Eltdot1dStpMultiProcessPortList_Object = MibTableColumn
eltdot1dStpMultiProcessPortList = _Eltdot1dStpMultiProcessPortList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 1, 3, 1, 2),
    _Eltdot1dStpMultiProcessPortList_Type()
)
eltdot1dStpMultiProcessPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1dStpMultiProcessPortList.setStatus("current")
_EltMesDot1sMstpMultiProcess_ObjectIdentity = ObjectIdentity
eltMesDot1sMstpMultiProcess = _EltMesDot1sMstpMultiProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2)
)
_Eltdot1sMstpMultiProcessInstanceTable_Object = MibTable
eltdot1sMstpMultiProcessInstanceTable = _Eltdot1sMstpMultiProcessInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1)
)
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceTable.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceEntry_Object = MibTableRow
eltdot1sMstpMultiProcessInstanceEntry = _Eltdot1sMstpMultiProcessInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1)
)
eltdot1sMstpMultiProcessInstanceEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB", "eltdot1sMstpMultiProcessInstanceProcessId"),
    (0, "ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB", "eltdot1sMstpMultiProcessInstanceId"),
)
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceEntry.setStatus("current")


class _Eltdot1sMstpMultiProcessInstanceProcessId_Type(Integer32):
    """Custom type eltdot1sMstpMultiProcessInstanceProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Eltdot1sMstpMultiProcessInstanceProcessId_Type.__name__ = "Integer32"
_Eltdot1sMstpMultiProcessInstanceProcessId_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceProcessId = _Eltdot1sMstpMultiProcessInstanceProcessId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 1),
    _Eltdot1sMstpMultiProcessInstanceProcessId_Type()
)
eltdot1sMstpMultiProcessInstanceProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceProcessId.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceId_Type = Integer32
_Eltdot1sMstpMultiProcessInstanceId_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceId = _Eltdot1sMstpMultiProcessInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 2),
    _Eltdot1sMstpMultiProcessInstanceId_Type()
)
eltdot1sMstpMultiProcessInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceId.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceEnable_Type = TruthValue
_Eltdot1sMstpMultiProcessInstanceEnable_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceEnable = _Eltdot1sMstpMultiProcessInstanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 3),
    _Eltdot1sMstpMultiProcessInstanceEnable_Type()
)
eltdot1sMstpMultiProcessInstanceEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceEnable.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange_Type = TimeTicks
_Eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange = _Eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 4),
    _Eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange_Type()
)
eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceTopChanges_Type = Counter32
_Eltdot1sMstpMultiProcessInstanceTopChanges_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceTopChanges = _Eltdot1sMstpMultiProcessInstanceTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 5),
    _Eltdot1sMstpMultiProcessInstanceTopChanges_Type()
)
eltdot1sMstpMultiProcessInstanceTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceTopChanges.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceDesignatedRoot_Type = BridgeId
_Eltdot1sMstpMultiProcessInstanceDesignatedRoot_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceDesignatedRoot = _Eltdot1sMstpMultiProcessInstanceDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 6),
    _Eltdot1sMstpMultiProcessInstanceDesignatedRoot_Type()
)
eltdot1sMstpMultiProcessInstanceDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceDesignatedRoot.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceRootCost_Type = Integer32
_Eltdot1sMstpMultiProcessInstanceRootCost_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceRootCost = _Eltdot1sMstpMultiProcessInstanceRootCost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 7),
    _Eltdot1sMstpMultiProcessInstanceRootCost_Type()
)
eltdot1sMstpMultiProcessInstanceRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceRootCost.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceRootPort_Type = Integer32
_Eltdot1sMstpMultiProcessInstanceRootPort_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceRootPort = _Eltdot1sMstpMultiProcessInstanceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 8),
    _Eltdot1sMstpMultiProcessInstanceRootPort_Type()
)
eltdot1sMstpMultiProcessInstanceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceRootPort.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceMaxAge_Type = Timeout
_Eltdot1sMstpMultiProcessInstanceMaxAge_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceMaxAge = _Eltdot1sMstpMultiProcessInstanceMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 9),
    _Eltdot1sMstpMultiProcessInstanceMaxAge_Type()
)
eltdot1sMstpMultiProcessInstanceMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceMaxAge.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceHelloTime_Type = Timeout
_Eltdot1sMstpMultiProcessInstanceHelloTime_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceHelloTime = _Eltdot1sMstpMultiProcessInstanceHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 10),
    _Eltdot1sMstpMultiProcessInstanceHelloTime_Type()
)
eltdot1sMstpMultiProcessInstanceHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceHelloTime.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceHoldTime_Type = Integer32
_Eltdot1sMstpMultiProcessInstanceHoldTime_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceHoldTime = _Eltdot1sMstpMultiProcessInstanceHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 11),
    _Eltdot1sMstpMultiProcessInstanceHoldTime_Type()
)
eltdot1sMstpMultiProcessInstanceHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceHoldTime.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceForwardDelay_Type = Timeout
_Eltdot1sMstpMultiProcessInstanceForwardDelay_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceForwardDelay = _Eltdot1sMstpMultiProcessInstanceForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 12),
    _Eltdot1sMstpMultiProcessInstanceForwardDelay_Type()
)
eltdot1sMstpMultiProcessInstanceForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceForwardDelay.setStatus("current")


class _Eltdot1sMstpMultiProcessInstancePriority_Type(Integer32):
    """Custom type eltdot1sMstpMultiProcessInstancePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_Eltdot1sMstpMultiProcessInstancePriority_Type.__name__ = "Integer32"
_Eltdot1sMstpMultiProcessInstancePriority_Object = MibTableColumn
eltdot1sMstpMultiProcessInstancePriority = _Eltdot1sMstpMultiProcessInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 13),
    _Eltdot1sMstpMultiProcessInstancePriority_Type()
)
eltdot1sMstpMultiProcessInstancePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstancePriority.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceRemainingHopes_Type = Integer32
_Eltdot1sMstpMultiProcessInstanceRemainingHopes_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceRemainingHopes = _Eltdot1sMstpMultiProcessInstanceRemainingHopes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 14),
    _Eltdot1sMstpMultiProcessInstanceRemainingHopes_Type()
)
eltdot1sMstpMultiProcessInstanceRemainingHopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceRemainingHopes.setStatus("current")
_Eltdot1sMstpMultiProcessInstanceLastTopologyChangePort_Type = Integer32
_Eltdot1sMstpMultiProcessInstanceLastTopologyChangePort_Object = MibTableColumn
eltdot1sMstpMultiProcessInstanceLastTopologyChangePort = _Eltdot1sMstpMultiProcessInstanceLastTopologyChangePort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 1, 1, 15),
    _Eltdot1sMstpMultiProcessInstanceLastTopologyChangePort_Type()
)
eltdot1sMstpMultiProcessInstanceLastTopologyChangePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessInstanceLastTopologyChangePort.setStatus("current")
_Eltdot1sMstpMultiProcessTable_Object = MibTable
eltdot1sMstpMultiProcessTable = _Eltdot1sMstpMultiProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2)
)
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessTable.setStatus("current")
_Eltdot1sMstpMultiProcessEntry_Object = MibTableRow
eltdot1sMstpMultiProcessEntry = _Eltdot1sMstpMultiProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2, 1)
)
eltdot1sMstpMultiProcessEntry.setIndexNames(
    (0, "ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB", "eltdot1sMstpMultiProcessId"),
)
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessEntry.setStatus("current")


class _Eltdot1sMstpMultiProcessId_Type(Integer32):
    """Custom type eltdot1sMstpMultiProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Eltdot1sMstpMultiProcessId_Type.__name__ = "Integer32"
_Eltdot1sMstpMultiProcessId_Object = MibTableColumn
eltdot1sMstpMultiProcessId = _Eltdot1sMstpMultiProcessId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2, 1, 1),
    _Eltdot1sMstpMultiProcessId_Type()
)
eltdot1sMstpMultiProcessId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessId.setStatus("current")


class _Eltdot1sMstpMultiProcessMaxHopes_Type(Integer32):
    """Custom type eltdot1sMstpMultiProcessMaxHopes based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Eltdot1sMstpMultiProcessMaxHopes_Type.__name__ = "Integer32"
_Eltdot1sMstpMultiProcessMaxHopes_Object = MibTableColumn
eltdot1sMstpMultiProcessMaxHopes = _Eltdot1sMstpMultiProcessMaxHopes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2, 1, 2),
    _Eltdot1sMstpMultiProcessMaxHopes_Type()
)
eltdot1sMstpMultiProcessMaxHopes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessMaxHopes.setStatus("current")


class _Eltdot1sMstpMultiProcessDesignatedMaxHopes_Type(Integer32):
    """Custom type eltdot1sMstpMultiProcessDesignatedMaxHopes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_Eltdot1sMstpMultiProcessDesignatedMaxHopes_Type.__name__ = "Integer32"
_Eltdot1sMstpMultiProcessDesignatedMaxHopes_Object = MibTableColumn
eltdot1sMstpMultiProcessDesignatedMaxHopes = _Eltdot1sMstpMultiProcessDesignatedMaxHopes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2, 1, 3),
    _Eltdot1sMstpMultiProcessDesignatedMaxHopes_Type()
)
eltdot1sMstpMultiProcessDesignatedMaxHopes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessDesignatedMaxHopes.setStatus("current")
_Eltdot1sMstpMultiProcessRegionalRoot_Type = BridgeId
_Eltdot1sMstpMultiProcessRegionalRoot_Object = MibTableColumn
eltdot1sMstpMultiProcessRegionalRoot = _Eltdot1sMstpMultiProcessRegionalRoot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2, 1, 4),
    _Eltdot1sMstpMultiProcessRegionalRoot_Type()
)
eltdot1sMstpMultiProcessRegionalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessRegionalRoot.setStatus("current")
_Eltdot1sMstpMultiProcessRegionalRootCost_Type = Integer32
_Eltdot1sMstpMultiProcessRegionalRootCost_Object = MibTableColumn
eltdot1sMstpMultiProcessRegionalRootCost = _Eltdot1sMstpMultiProcessRegionalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2, 1, 5),
    _Eltdot1sMstpMultiProcessRegionalRootCost_Type()
)
eltdot1sMstpMultiProcessRegionalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessRegionalRootCost.setStatus("current")
_Eltdot1sMstpMultiProcessRemainingHops_Type = Integer32
_Eltdot1sMstpMultiProcessRemainingHops_Object = MibTableColumn
eltdot1sMstpMultiProcessRemainingHops = _Eltdot1sMstpMultiProcessRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 401, 0, 2, 2, 2, 1, 6),
    _Eltdot1sMstpMultiProcessRemainingHops_Type()
)
eltdot1sMstpMultiProcessRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltdot1sMstpMultiProcessRemainingHops.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-BRIDGE-STP-MULTIPROCESS-MIB",
    **{"eltMesStpMultiProcessMIB": eltMesStpMultiProcessMIB,
       "eltMesDot1dStpMultiProcess": eltMesDot1dStpMultiProcess,
       "eltdot1dStpMultiProcessTable": eltdot1dStpMultiProcessTable,
       "eltdot1dStpMultiProcessEntry": eltdot1dStpMultiProcessEntry,
       "eltdot1dStpMultiProcessId": eltdot1dStpMultiProcessId,
       "eltdot1dStpMultiProcessPriority": eltdot1dStpMultiProcessPriority,
       "eltdot1dStpMultiProcessBridgeMaxAge": eltdot1dStpMultiProcessBridgeMaxAge,
       "eltdot1dStpMultiProcessBridgeHelloTime": eltdot1dStpMultiProcessBridgeHelloTime,
       "eltdot1dStpMultiProcessBridgeForwardDelay": eltdot1dStpMultiProcessBridgeForwardDelay,
       "eltdot1dStpMultiProcessVersion": eltdot1dStpMultiProcessVersion,
       "eltdot1dStpMultiProcessTimeSinceTopologyChange": eltdot1dStpMultiProcessTimeSinceTopologyChange,
       "eltdot1dStpMultiProcessTopChanges": eltdot1dStpMultiProcessTopChanges,
       "eltdot1dStpMultiProcessDesignatedRoot": eltdot1dStpMultiProcessDesignatedRoot,
       "eltdot1dStpMultiProcessRootCost": eltdot1dStpMultiProcessRootCost,
       "eltdot1dStpMultiProcessRootPort": eltdot1dStpMultiProcessRootPort,
       "eltdot1dStpMultiProcessMaxAge": eltdot1dStpMultiProcessMaxAge,
       "eltdot1dStpMultiProcessHelloTime": eltdot1dStpMultiProcessHelloTime,
       "eltdot1dStpMultiProcessHoldTime": eltdot1dStpMultiProcessHoldTime,
       "eltdot1dStpMultiProcessForwardDelay": eltdot1dStpMultiProcessForwardDelay,
       "eltdot1dStpMultiProcessRowStatus": eltdot1dStpMultiProcessRowStatus,
       "eltdot1dStpMultiProcessLastTopologyChangePort": eltdot1dStpMultiProcessLastTopologyChangePort,
       "eltdot1dStpMultiProcessPortTable": eltdot1dStpMultiProcessPortTable,
       "eltdot1dStpMultiProcessPortEntry": eltdot1dStpMultiProcessPortEntry,
       "eltdot1dStpMultiProcessPortPort": eltdot1dStpMultiProcessPortPort,
       "eltdot1dStpMultiProcessPortProcessId": eltdot1dStpMultiProcessPortProcessId,
       "eltdot1dStpMultiProcessPortSharedProcessId1": eltdot1dStpMultiProcessPortSharedProcessId1,
       "eltdot1dStpMultiProcessPortSharedProcessId2": eltdot1dStpMultiProcessPortSharedProcessId2,
       "eltdot1dStpMultiProcessPortSharedProcessId3": eltdot1dStpMultiProcessPortSharedProcessId3,
       "eltdot1dStpMultiProcessPortSharedProcessId4": eltdot1dStpMultiProcessPortSharedProcessId4,
       "eltdot1dStpMultiProcessPortSharedProcessId5": eltdot1dStpMultiProcessPortSharedProcessId5,
       "eltdot1dStpMultiProcessPortSharedProcessId6": eltdot1dStpMultiProcessPortSharedProcessId6,
       "eltdot1dStpMultiProcessPortSharedProcessId7": eltdot1dStpMultiProcessPortSharedProcessId7,
       "eltdot1dStpMultiProcessPortSharedProcessId8": eltdot1dStpMultiProcessPortSharedProcessId8,
       "eltdot1dStpMultiProcessPortSharedProcessId9": eltdot1dStpMultiProcessPortSharedProcessId9,
       "eltdot1dStpMultiProcessPortSharedProcessId10": eltdot1dStpMultiProcessPortSharedProcessId10,
       "eltdot1dStpMultiProcessPortListTable": eltdot1dStpMultiProcessPortListTable,
       "eltdot1dStpMultiProcessPortListEntry": eltdot1dStpMultiProcessPortListEntry,
       "eltdot1dStpMultiProcessPortListProcessId": eltdot1dStpMultiProcessPortListProcessId,
       "eltdot1dStpMultiProcessPortList": eltdot1dStpMultiProcessPortList,
       "eltMesDot1sMstpMultiProcess": eltMesDot1sMstpMultiProcess,
       "eltdot1sMstpMultiProcessInstanceTable": eltdot1sMstpMultiProcessInstanceTable,
       "eltdot1sMstpMultiProcessInstanceEntry": eltdot1sMstpMultiProcessInstanceEntry,
       "eltdot1sMstpMultiProcessInstanceProcessId": eltdot1sMstpMultiProcessInstanceProcessId,
       "eltdot1sMstpMultiProcessInstanceId": eltdot1sMstpMultiProcessInstanceId,
       "eltdot1sMstpMultiProcessInstanceEnable": eltdot1sMstpMultiProcessInstanceEnable,
       "eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange": eltdot1sMstpMultiProcessInstanceTimeSinceTopologyChange,
       "eltdot1sMstpMultiProcessInstanceTopChanges": eltdot1sMstpMultiProcessInstanceTopChanges,
       "eltdot1sMstpMultiProcessInstanceDesignatedRoot": eltdot1sMstpMultiProcessInstanceDesignatedRoot,
       "eltdot1sMstpMultiProcessInstanceRootCost": eltdot1sMstpMultiProcessInstanceRootCost,
       "eltdot1sMstpMultiProcessInstanceRootPort": eltdot1sMstpMultiProcessInstanceRootPort,
       "eltdot1sMstpMultiProcessInstanceMaxAge": eltdot1sMstpMultiProcessInstanceMaxAge,
       "eltdot1sMstpMultiProcessInstanceHelloTime": eltdot1sMstpMultiProcessInstanceHelloTime,
       "eltdot1sMstpMultiProcessInstanceHoldTime": eltdot1sMstpMultiProcessInstanceHoldTime,
       "eltdot1sMstpMultiProcessInstanceForwardDelay": eltdot1sMstpMultiProcessInstanceForwardDelay,
       "eltdot1sMstpMultiProcessInstancePriority": eltdot1sMstpMultiProcessInstancePriority,
       "eltdot1sMstpMultiProcessInstanceRemainingHopes": eltdot1sMstpMultiProcessInstanceRemainingHopes,
       "eltdot1sMstpMultiProcessInstanceLastTopologyChangePort": eltdot1sMstpMultiProcessInstanceLastTopologyChangePort,
       "eltdot1sMstpMultiProcessTable": eltdot1sMstpMultiProcessTable,
       "eltdot1sMstpMultiProcessEntry": eltdot1sMstpMultiProcessEntry,
       "eltdot1sMstpMultiProcessId": eltdot1sMstpMultiProcessId,
       "eltdot1sMstpMultiProcessMaxHopes": eltdot1sMstpMultiProcessMaxHopes,
       "eltdot1sMstpMultiProcessDesignatedMaxHopes": eltdot1sMstpMultiProcessDesignatedMaxHopes,
       "eltdot1sMstpMultiProcessRegionalRoot": eltdot1sMstpMultiProcessRegionalRoot,
       "eltdot1sMstpMultiProcessRegionalRootCost": eltdot1sMstpMultiProcessRegionalRootCost,
       "eltdot1sMstpMultiProcessRemainingHops": eltdot1sMstpMultiProcessRemainingHops}
)
