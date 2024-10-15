# SNMP MIB module (TPLINK-SPANNING-TREE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-SPANNING-TREE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:41 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")


# MODULE-IDENTITY

tplinkSpanningTreeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21)
)
tplinkSpanningTreeMIB.setRevisions(
        ("2012-11-21 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkSpanningTreeMIBObjects_ObjectIdentity = ObjectIdentity
tplinkSpanningTreeMIBObjects = _TplinkSpanningTreeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1)
)
_TpStpBasicCfg_ObjectIdentity = ObjectIdentity
tpStpBasicCfg = _TpStpBasicCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1)
)
_TpStpBasicGlobalConfig_ObjectIdentity = ObjectIdentity
tpStpBasicGlobalConfig = _TpStpBasicGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1)
)


class _TpStpEnable_Type(Integer32):
    """Custom type tpStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpEnable_Type.__name__ = "Integer32"
_TpStpEnable_Object = MibScalar
tpStpEnable = _TpStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 1),
    _TpStpEnable_Type()
)
tpStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpEnable.setStatus("current")


class _TpRstpEnable_Type(Integer32):
    """Custom type tpRstpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpRstpEnable_Type.__name__ = "Integer32"
_TpRstpEnable_Object = MibScalar
tpRstpEnable = _TpRstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 2),
    _TpRstpEnable_Type()
)
tpRstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpRstpEnable.setStatus("current")


class _TpMstpEnable_Type(Integer32):
    """Custom type tpMstpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpMstpEnable_Type.__name__ = "Integer32"
_TpMstpEnable_Object = MibScalar
tpMstpEnable = _TpMstpEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 1, 3),
    _TpMstpEnable_Type()
)
tpMstpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpEnable.setStatus("current")
_TpStpBasicParamConfig_ObjectIdentity = ObjectIdentity
tpStpBasicParamConfig = _TpStpBasicParamConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2)
)


class _TpStpCistPriority_Type(Integer32):
    """Custom type tpStpCistPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_TpStpCistPriority_Type.__name__ = "Integer32"
_TpStpCistPriority_Object = MibScalar
tpStpCistPriority = _TpStpCistPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 1),
    _TpStpCistPriority_Type()
)
tpStpCistPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpCistPriority.setStatus("current")


class _TpStpHelloTime_Type(Integer32):
    """Custom type tpStpHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TpStpHelloTime_Type.__name__ = "Integer32"
_TpStpHelloTime_Object = MibScalar
tpStpHelloTime = _TpStpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 2),
    _TpStpHelloTime_Type()
)
tpStpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpHelloTime.setStatus("current")


class _TpStpAgingTime_Type(Integer32):
    """Custom type tpStpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_TpStpAgingTime_Type.__name__ = "Integer32"
_TpStpAgingTime_Object = MibScalar
tpStpAgingTime = _TpStpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 3),
    _TpStpAgingTime_Type()
)
tpStpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpAgingTime.setStatus("current")


class _TpStpForwardDelay_Type(Integer32):
    """Custom type tpStpForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_TpStpForwardDelay_Type.__name__ = "Integer32"
_TpStpForwardDelay_Object = MibScalar
tpStpForwardDelay = _TpStpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 4),
    _TpStpForwardDelay_Type()
)
tpStpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpForwardDelay.setStatus("current")


class _TpStpHoldCount_Type(Integer32):
    """Custom type tpStpHoldCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TpStpHoldCount_Type.__name__ = "Integer32"
_TpStpHoldCount_Object = MibScalar
tpStpHoldCount = _TpStpHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 5),
    _TpStpHoldCount_Type()
)
tpStpHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpHoldCount.setStatus("current")


class _TpStpMaxHops_Type(Integer32):
    """Custom type tpStpMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_TpStpMaxHops_Type.__name__ = "Integer32"
_TpStpMaxHops_Object = MibScalar
tpStpMaxHops = _TpStpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 2, 6),
    _TpStpMaxHops_Type()
)
tpStpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpMaxHops.setStatus("current")
_TpStpInfo_ObjectIdentity = ObjectIdentity
tpStpInfo = _TpStpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3)
)


class _TpStpEnableStatus_Type(Integer32):
    """Custom type tpStpEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpEnableStatus_Type.__name__ = "Integer32"
_TpStpEnableStatus_Object = MibScalar
tpStpEnableStatus = _TpStpEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 1),
    _TpStpEnableStatus_Type()
)
tpStpEnableStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpEnableStatus.setStatus("current")


class _TpStpMode_Type(Integer32):
    """Custom type tpStpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 1))
    )


_TpStpMode_Type.__name__ = "Integer32"
_TpStpMode_Object = MibScalar
tpStpMode = _TpStpMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 2),
    _TpStpMode_Type()
)
tpStpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpMode.setStatus("current")


class _TpStpLocalBridge_Type(OctetString):
    """Custom type tpStpLocalBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpLocalBridge_Type.__name__ = "OctetString"
_TpStpLocalBridge_Object = MibScalar
tpStpLocalBridge = _TpStpLocalBridge_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 3),
    _TpStpLocalBridge_Type()
)
tpStpLocalBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpLocalBridge.setStatus("current")


class _TpStpCISTRoot_Type(OctetString):
    """Custom type tpStpCISTRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpCISTRoot_Type.__name__ = "OctetString"
_TpStpCISTRoot_Object = MibScalar
tpStpCISTRoot = _TpStpCISTRoot_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 4),
    _TpStpCISTRoot_Type()
)
tpStpCISTRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpCISTRoot.setStatus("current")


class _TpStpExPathCost_Type(Integer32):
    """Custom type tpStpExPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_TpStpExPathCost_Type.__name__ = "Integer32"
_TpStpExPathCost_Object = MibScalar
tpStpExPathCost = _TpStpExPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 5),
    _TpStpExPathCost_Type()
)
tpStpExPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpExPathCost.setStatus("current")


class _TpStpRegionRoot_Type(OctetString):
    """Custom type tpStpRegionRoot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpRegionRoot_Type.__name__ = "OctetString"
_TpStpRegionRoot_Object = MibScalar
tpStpRegionRoot = _TpStpRegionRoot_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 6),
    _TpStpRegionRoot_Type()
)
tpStpRegionRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpRegionRoot.setStatus("current")


class _TpStpInPathCost_Type(Integer32):
    """Custom type tpStpInPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_TpStpInPathCost_Type.__name__ = "Integer32"
_TpStpInPathCost_Object = MibScalar
tpStpInPathCost = _TpStpInPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 7),
    _TpStpInPathCost_Type()
)
tpStpInPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpInPathCost.setStatus("current")


class _TpStpDesignatedBridge_Type(OctetString):
    """Custom type tpStpDesignatedBridge based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpDesignatedBridge_Type.__name__ = "OctetString"
_TpStpDesignatedBridge_Object = MibScalar
tpStpDesignatedBridge = _TpStpDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 8),
    _TpStpDesignatedBridge_Type()
)
tpStpDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpDesignatedBridge.setStatus("current")
_TpStpRootPort_Type = Integer32
_TpStpRootPort_Object = MibScalar
tpStpRootPort = _TpStpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 9),
    _TpStpRootPort_Type()
)
tpStpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpRootPort.setStatus("current")


class _TpStpLastTopologyChangeTime_Type(OctetString):
    """Custom type tpStpLastTopologyChangeTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpLastTopologyChangeTime_Type.__name__ = "OctetString"
_TpStpLastTopologyChangeTime_Object = MibScalar
tpStpLastTopologyChangeTime = _TpStpLastTopologyChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 10),
    _TpStpLastTopologyChangeTime_Type()
)
tpStpLastTopologyChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpLastTopologyChangeTime.setStatus("current")
_TpStpTopologyChangeCounter_Type = Integer32
_TpStpTopologyChangeCounter_Object = MibScalar
tpStpTopologyChangeCounter = _TpStpTopologyChangeCounter_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 1, 3, 11),
    _TpStpTopologyChangeCounter_Type()
)
tpStpTopologyChangeCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpTopologyChangeCounter.setStatus("current")
_TpStpPortCfg_ObjectIdentity = ObjectIdentity
tpStpPortCfg = _TpStpPortCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2)
)
_TpStpPortConfigTable_Object = MibTable
tpStpPortConfigTable = _TpStpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpStpPortConfigTable.setStatus("current")
_TpStpPortConfigEntry_Object = MibTableRow
tpStpPortConfigEntry = _TpStpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1)
)
tpStpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpStpPortConfigEntry.setStatus("current")


class _TpStpPortNumber_Type(OctetString):
    """Custom type tpStpPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpPortNumber_Type.__name__ = "OctetString"
_TpStpPortNumber_Object = MibTableColumn
tpStpPortNumber = _TpStpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 1),
    _TpStpPortNumber_Type()
)
tpStpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpPortNumber.setStatus("current")


class _TpStpPortEnable_Type(Integer32):
    """Custom type tpStpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("errPort", 2))
    )


_TpStpPortEnable_Type.__name__ = "Integer32"
_TpStpPortEnable_Object = MibTableColumn
tpStpPortEnable = _TpStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 2),
    _TpStpPortEnable_Type()
)
tpStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpPortEnable.setStatus("current")


class _TpStpPortPriority_Type(Integer32):
    """Custom type tpStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_TpStpPortPriority_Type.__name__ = "Integer32"
_TpStpPortPriority_Object = MibTableColumn
tpStpPortPriority = _TpStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 3),
    _TpStpPortPriority_Type()
)
tpStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpPortPriority.setStatus("current")


class _TpStpPortExPathCost_Type(Integer32):
    """Custom type tpStpPortExPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_TpStpPortExPathCost_Type.__name__ = "Integer32"
_TpStpPortExPathCost_Object = MibTableColumn
tpStpPortExPathCost = _TpStpPortExPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 4),
    _TpStpPortExPathCost_Type()
)
tpStpPortExPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpPortExPathCost.setStatus("current")


class _TpStpPortInPathCost_Type(Integer32):
    """Custom type tpStpPortInPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_TpStpPortInPathCost_Type.__name__ = "Integer32"
_TpStpPortInPathCost_Object = MibTableColumn
tpStpPortInPathCost = _TpStpPortInPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 5),
    _TpStpPortInPathCost_Type()
)
tpStpPortInPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpPortInPathCost.setStatus("current")


class _TpStpEdgePortStatus_Type(Integer32):
    """Custom type tpStpEdgePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpEdgePortStatus_Type.__name__ = "Integer32"
_TpStpEdgePortStatus_Object = MibTableColumn
tpStpEdgePortStatus = _TpStpEdgePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 6),
    _TpStpEdgePortStatus_Type()
)
tpStpEdgePortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpEdgePortStatus.setStatus("current")


class _TpStpPointToPointStatus_Type(Integer32):
    """Custom type tpStpPointToPointStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("force-disable", 2),
          ("force-enable", 1))
    )


_TpStpPointToPointStatus_Type.__name__ = "Integer32"
_TpStpPointToPointStatus_Object = MibTableColumn
tpStpPointToPointStatus = _TpStpPointToPointStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 7),
    _TpStpPointToPointStatus_Type()
)
tpStpPointToPointStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpPointToPointStatus.setStatus("current")


class _TpStpPortMCheck_Type(Integer32):
    """Custom type tpStpPortMCheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unChange", 0))
    )


_TpStpPortMCheck_Type.__name__ = "Integer32"
_TpStpPortMCheck_Object = MibTableColumn
tpStpPortMCheck = _TpStpPortMCheck_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 8),
    _TpStpPortMCheck_Type()
)
tpStpPortMCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpPortMCheck.setStatus("current")


class _TpStpPortStpVersion_Type(Integer32):
    """Custom type tpStpPortStpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("n-a", 0),
          ("rstp", 2),
          ("stp", 1))
    )


_TpStpPortStpVersion_Type.__name__ = "Integer32"
_TpStpPortStpVersion_Object = MibTableColumn
tpStpPortStpVersion = _TpStpPortStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 9),
    _TpStpPortStpVersion_Type()
)
tpStpPortStpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpPortStpVersion.setStatus("current")


class _TpStpPortRole_Type(Integer32):
    """Custom type tpStpPortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 4),
          ("disabled", 1),
          ("master", 6),
          ("n-a", 0),
          ("root", 5))
    )


_TpStpPortRole_Type.__name__ = "Integer32"
_TpStpPortRole_Object = MibTableColumn
tpStpPortRole = _TpStpPortRole_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 10),
    _TpStpPortRole_Type()
)
tpStpPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpPortRole.setStatus("current")


class _TpStpPortStatus_Type(Integer32):
    """Custom type tpStpPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("disconnected", 1),
          ("forwarding", 4),
          ("learning", 3),
          ("n-a", 0))
    )


_TpStpPortStatus_Type.__name__ = "Integer32"
_TpStpPortStatus_Object = MibTableColumn
tpStpPortStatus = _TpStpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 11),
    _TpStpPortStatus_Type()
)
tpStpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpPortStatus.setStatus("current")


class _TpStpPortLag_Type(OctetString):
    """Custom type tpStpPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpPortLag_Type.__name__ = "OctetString"
_TpStpPortLag_Object = MibTableColumn
tpStpPortLag = _TpStpPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 2, 1, 1, 12),
    _TpStpPortLag_Type()
)
tpStpPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpPortLag.setStatus("current")
_TpStpInstanceCfg_ObjectIdentity = ObjectIdentity
tpStpInstanceCfg = _TpStpInstanceCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3)
)
_TpMstpRegionConfig_ObjectIdentity = ObjectIdentity
tpMstpRegionConfig = _TpMstpRegionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1)
)


class _TpMstpRegionName_Type(OctetString):
    """Custom type tpMstpRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TpMstpRegionName_Type.__name__ = "OctetString"
_TpMstpRegionName_Object = MibScalar
tpMstpRegionName = _TpMstpRegionName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1, 1),
    _TpMstpRegionName_Type()
)
tpMstpRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpRegionName.setStatus("current")


class _TpMstpRevision_Type(Integer32):
    """Custom type tpMstpRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TpMstpRevision_Type.__name__ = "Integer32"
_TpMstpRevision_Object = MibScalar
tpMstpRevision = _TpMstpRevision_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 1, 2),
    _TpMstpRevision_Type()
)
tpMstpRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpRevision.setStatus("current")
_TpMstpInstanceConfigTable_Object = MibTable
tpMstpInstanceConfigTable = _TpMstpInstanceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tpMstpInstanceConfigTable.setStatus("current")
_TpMstpInstanceConfigEntry_Object = MibTableRow
tpMstpInstanceConfigEntry = _TpMstpInstanceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1)
)
tpMstpInstanceConfigEntry.setIndexNames(
    (0, "TPLINK-SPANNING-TREE-MIB", "tpMstpInstanceId"),
)
if mibBuilder.loadTexts:
    tpMstpInstanceConfigEntry.setStatus("current")
_TpMstpInstanceId_Type = Integer32
_TpMstpInstanceId_Object = MibTableColumn
tpMstpInstanceId = _TpMstpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 1),
    _TpMstpInstanceId_Type()
)
tpMstpInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMstpInstanceId.setStatus("current")


class _TpMstpInstanceEnable_Type(Integer32):
    """Custom type tpMstpInstanceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpMstpInstanceEnable_Type.__name__ = "Integer32"
_TpMstpInstanceEnable_Object = MibTableColumn
tpMstpInstanceEnable = _TpMstpInstanceEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 2),
    _TpMstpInstanceEnable_Type()
)
tpMstpInstanceEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMstpInstanceEnable.setStatus("current")


class _TpMstpInstancePriority_Type(Integer32):
    """Custom type tpMstpInstancePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_TpMstpInstancePriority_Type.__name__ = "Integer32"
_TpMstpInstancePriority_Object = MibTableColumn
tpMstpInstancePriority = _TpMstpInstancePriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 3),
    _TpMstpInstancePriority_Type()
)
tpMstpInstancePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpInstancePriority.setStatus("current")


class _TpMstpInstanceVlanId_Type(OctetString):
    """Custom type tpMstpInstanceVlanId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TpMstpInstanceVlanId_Type.__name__ = "OctetString"
_TpMstpInstanceVlanId_Object = MibTableColumn
tpMstpInstanceVlanId = _TpMstpInstanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 4),
    _TpMstpInstanceVlanId_Type()
)
tpMstpInstanceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpInstanceVlanId.setStatus("current")


class _TpMstpClearInstanceVlanId_Type(Integer32):
    """Custom type tpMstpClearInstanceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_TpMstpClearInstanceVlanId_Type.__name__ = "Integer32"
_TpMstpClearInstanceVlanId_Object = MibTableColumn
tpMstpClearInstanceVlanId = _TpMstpClearInstanceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 2, 1, 5),
    _TpMstpClearInstanceVlanId_Type()
)
tpMstpClearInstanceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpClearInstanceVlanId.setStatus("current")
_TpMstpInstancePortConfigTable_Object = MibTable
tpMstpInstancePortConfigTable = _TpMstpInstancePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tpMstpInstancePortConfigTable.setStatus("current")
_TpMstpInstancePortConfigEntry_Object = MibTableRow
tpMstpInstancePortConfigEntry = _TpMstpInstancePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1)
)
tpMstpInstancePortConfigEntry.setIndexNames(
    (0, "TPLINK-SPANNING-TREE-MIB", "tpMstpInstancePortConfigId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMstpInstancePortConfigEntry.setStatus("current")
_TpMstpInstancePortConfigId_Type = Integer32
_TpMstpInstancePortConfigId_Object = MibTableColumn
tpMstpInstancePortConfigId = _TpMstpInstancePortConfigId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 1),
    _TpMstpInstancePortConfigId_Type()
)
tpMstpInstancePortConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMstpInstancePortConfigId.setStatus("current")


class _TpMstpInstancePortNumber_Type(OctetString):
    """Custom type tpMstpInstancePortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMstpInstancePortNumber_Type.__name__ = "OctetString"
_TpMstpInstancePortNumber_Object = MibTableColumn
tpMstpInstancePortNumber = _TpMstpInstancePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 2),
    _TpMstpInstancePortNumber_Type()
)
tpMstpInstancePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMstpInstancePortNumber.setStatus("current")


class _TpMstpInstancePortPriority_Type(Integer32):
    """Custom type tpMstpInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_TpMstpInstancePortPriority_Type.__name__ = "Integer32"
_TpMstpInstancePortPriority_Object = MibTableColumn
tpMstpInstancePortPriority = _TpMstpInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 3),
    _TpMstpInstancePortPriority_Type()
)
tpMstpInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpInstancePortPriority.setStatus("current")


class _TpMstpInstancePortPathCost_Type(Integer32):
    """Custom type tpMstpInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000000),
    )


_TpMstpInstancePortPathCost_Type.__name__ = "Integer32"
_TpMstpInstancePortPathCost_Object = MibTableColumn
tpMstpInstancePortPathCost = _TpMstpInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 4),
    _TpMstpInstancePortPathCost_Type()
)
tpMstpInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMstpInstancePortPathCost.setStatus("current")


class _TpMstpInstancePortRole_Type(Integer32):
    """Custom type tpMstpInstancePortRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 4),
          ("disabled", 1),
          ("master", 6),
          ("n-a", 0),
          ("root", 5))
    )


_TpMstpInstancePortRole_Type.__name__ = "Integer32"
_TpMstpInstancePortRole_Object = MibTableColumn
tpMstpInstancePortRole = _TpMstpInstancePortRole_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 5),
    _TpMstpInstancePortRole_Type()
)
tpMstpInstancePortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMstpInstancePortRole.setStatus("current")


class _TpMstpInstancePortStatus_Type(Integer32):
    """Custom type tpMstpInstancePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("disabled", 1),
          ("forwarding", 4),
          ("learning", 3),
          ("n-a", 0))
    )


_TpMstpInstancePortStatus_Type.__name__ = "Integer32"
_TpMstpInstancePortStatus_Object = MibTableColumn
tpMstpInstancePortStatus = _TpMstpInstancePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 6),
    _TpMstpInstancePortStatus_Type()
)
tpMstpInstancePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMstpInstancePortStatus.setStatus("current")


class _TpMstpInstancePortLag_Type(OctetString):
    """Custom type tpMstpInstancePortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMstpInstancePortLag_Type.__name__ = "OctetString"
_TpMstpInstancePortLag_Object = MibTableColumn
tpMstpInstancePortLag = _TpMstpInstancePortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 3, 3, 1, 7),
    _TpMstpInstancePortLag_Type()
)
tpMstpInstancePortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMstpInstancePortLag.setStatus("current")
_TpStpSecurityCfg_ObjectIdentity = ObjectIdentity
tpStpSecurityCfg = _TpStpSecurityCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4)
)
_TpStpPortDefendTable_Object = MibTable
tpStpPortDefendTable = _TpStpPortDefendTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tpStpPortDefendTable.setStatus("current")
_TpStpPortDefendEntry_Object = MibTableRow
tpStpPortDefendEntry = _TpStpPortDefendEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1)
)
tpStpPortDefendEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpStpPortDefendEntry.setStatus("current")


class _TpStpDefendPortNumber_Type(OctetString):
    """Custom type tpStpDefendPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpDefendPortNumber_Type.__name__ = "OctetString"
_TpStpDefendPortNumber_Object = MibTableColumn
tpStpDefendPortNumber = _TpStpDefendPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 1),
    _TpStpDefendPortNumber_Type()
)
tpStpDefendPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpDefendPortNumber.setStatus("current")


class _TpStpLoopDefendEnable_Type(Integer32):
    """Custom type tpStpLoopDefendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpLoopDefendEnable_Type.__name__ = "Integer32"
_TpStpLoopDefendEnable_Object = MibTableColumn
tpStpLoopDefendEnable = _TpStpLoopDefendEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 2),
    _TpStpLoopDefendEnable_Type()
)
tpStpLoopDefendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpLoopDefendEnable.setStatus("current")


class _TpStpRootBridgeDefendEnable_Type(Integer32):
    """Custom type tpStpRootBridgeDefendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpRootBridgeDefendEnable_Type.__name__ = "Integer32"
_TpStpRootBridgeDefendEnable_Object = MibTableColumn
tpStpRootBridgeDefendEnable = _TpStpRootBridgeDefendEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 3),
    _TpStpRootBridgeDefendEnable_Type()
)
tpStpRootBridgeDefendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpRootBridgeDefendEnable.setStatus("current")


class _TpStpTcDefendEnable_Type(Integer32):
    """Custom type tpStpTcDefendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpTcDefendEnable_Type.__name__ = "Integer32"
_TpStpTcDefendEnable_Object = MibTableColumn
tpStpTcDefendEnable = _TpStpTcDefendEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 4),
    _TpStpTcDefendEnable_Type()
)
tpStpTcDefendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpTcDefendEnable.setStatus("current")


class _TpStpBPDUDefendEnable_Type(Integer32):
    """Custom type tpStpBPDUDefendEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpBPDUDefendEnable_Type.__name__ = "Integer32"
_TpStpBPDUDefendEnable_Object = MibTableColumn
tpStpBPDUDefendEnable = _TpStpBPDUDefendEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 5),
    _TpStpBPDUDefendEnable_Type()
)
tpStpBPDUDefendEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpBPDUDefendEnable.setStatus("current")


class _TpStpBPDUHoldEnable_Type(Integer32):
    """Custom type tpStpBPDUHoldEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TpStpBPDUHoldEnable_Type.__name__ = "Integer32"
_TpStpBPDUHoldEnable_Object = MibTableColumn
tpStpBPDUHoldEnable = _TpStpBPDUHoldEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 6),
    _TpStpBPDUHoldEnable_Type()
)
tpStpBPDUHoldEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpBPDUHoldEnable.setStatus("current")


class _TpStpDefendPortLag_Type(OctetString):
    """Custom type tpStpDefendPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpStpDefendPortLag_Type.__name__ = "OctetString"
_TpStpDefendPortLag_Object = MibTableColumn
tpStpDefendPortLag = _TpStpDefendPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 1, 1, 7),
    _TpStpDefendPortLag_Type()
)
tpStpDefendPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpStpDefendPortLag.setStatus("current")
_TpStpTcDefendConfig_ObjectIdentity = ObjectIdentity
tpStpTcDefendConfig = _TpStpTcDefendConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2)
)


class _TpStpTcDefendThreshold_Type(Integer32):
    """Custom type tpStpTcDefendThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TpStpTcDefendThreshold_Type.__name__ = "Integer32"
_TpStpTcDefendThreshold_Object = MibScalar
tpStpTcDefendThreshold = _TpStpTcDefendThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2, 1),
    _TpStpTcDefendThreshold_Type()
)
tpStpTcDefendThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpTcDefendThreshold.setStatus("current")


class _TpStpTcDefendTimer_Type(Integer32):
    """Custom type tpStpTcDefendTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TpStpTcDefendTimer_Type.__name__ = "Integer32"
_TpStpTcDefendTimer_Object = MibScalar
tpStpTcDefendTimer = _TpStpTcDefendTimer_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 1, 4, 2, 2),
    _TpStpTcDefendTimer_Type()
)
tpStpTcDefendTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpStpTcDefendTimer.setStatus("current")
_TplinkSpanningTreeNotifications_ObjectIdentity = ObjectIdentity
tplinkSpanningTreeNotifications = _TplinkSpanningTreeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 2)
)

# Managed Objects groups


# Notification objects

tpMstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 11863, 6, 21, 2, 1)
)
if mibBuilder.loadTexts:
    tpMstpTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-SPANNING-TREE-MIB",
    **{"tplinkSpanningTreeMIB": tplinkSpanningTreeMIB,
       "tplinkSpanningTreeMIBObjects": tplinkSpanningTreeMIBObjects,
       "tpStpBasicCfg": tpStpBasicCfg,
       "tpStpBasicGlobalConfig": tpStpBasicGlobalConfig,
       "tpStpEnable": tpStpEnable,
       "tpRstpEnable": tpRstpEnable,
       "tpMstpEnable": tpMstpEnable,
       "tpStpBasicParamConfig": tpStpBasicParamConfig,
       "tpStpCistPriority": tpStpCistPriority,
       "tpStpHelloTime": tpStpHelloTime,
       "tpStpAgingTime": tpStpAgingTime,
       "tpStpForwardDelay": tpStpForwardDelay,
       "tpStpHoldCount": tpStpHoldCount,
       "tpStpMaxHops": tpStpMaxHops,
       "tpStpInfo": tpStpInfo,
       "tpStpEnableStatus": tpStpEnableStatus,
       "tpStpMode": tpStpMode,
       "tpStpLocalBridge": tpStpLocalBridge,
       "tpStpCISTRoot": tpStpCISTRoot,
       "tpStpExPathCost": tpStpExPathCost,
       "tpStpRegionRoot": tpStpRegionRoot,
       "tpStpInPathCost": tpStpInPathCost,
       "tpStpDesignatedBridge": tpStpDesignatedBridge,
       "tpStpRootPort": tpStpRootPort,
       "tpStpLastTopologyChangeTime": tpStpLastTopologyChangeTime,
       "tpStpTopologyChangeCounter": tpStpTopologyChangeCounter,
       "tpStpPortCfg": tpStpPortCfg,
       "tpStpPortConfigTable": tpStpPortConfigTable,
       "tpStpPortConfigEntry": tpStpPortConfigEntry,
       "tpStpPortNumber": tpStpPortNumber,
       "tpStpPortEnable": tpStpPortEnable,
       "tpStpPortPriority": tpStpPortPriority,
       "tpStpPortExPathCost": tpStpPortExPathCost,
       "tpStpPortInPathCost": tpStpPortInPathCost,
       "tpStpEdgePortStatus": tpStpEdgePortStatus,
       "tpStpPointToPointStatus": tpStpPointToPointStatus,
       "tpStpPortMCheck": tpStpPortMCheck,
       "tpStpPortStpVersion": tpStpPortStpVersion,
       "tpStpPortRole": tpStpPortRole,
       "tpStpPortStatus": tpStpPortStatus,
       "tpStpPortLag": tpStpPortLag,
       "tpStpInstanceCfg": tpStpInstanceCfg,
       "tpMstpRegionConfig": tpMstpRegionConfig,
       "tpMstpRegionName": tpMstpRegionName,
       "tpMstpRevision": tpMstpRevision,
       "tpMstpInstanceConfigTable": tpMstpInstanceConfigTable,
       "tpMstpInstanceConfigEntry": tpMstpInstanceConfigEntry,
       "tpMstpInstanceId": tpMstpInstanceId,
       "tpMstpInstanceEnable": tpMstpInstanceEnable,
       "tpMstpInstancePriority": tpMstpInstancePriority,
       "tpMstpInstanceVlanId": tpMstpInstanceVlanId,
       "tpMstpClearInstanceVlanId": tpMstpClearInstanceVlanId,
       "tpMstpInstancePortConfigTable": tpMstpInstancePortConfigTable,
       "tpMstpInstancePortConfigEntry": tpMstpInstancePortConfigEntry,
       "tpMstpInstancePortConfigId": tpMstpInstancePortConfigId,
       "tpMstpInstancePortNumber": tpMstpInstancePortNumber,
       "tpMstpInstancePortPriority": tpMstpInstancePortPriority,
       "tpMstpInstancePortPathCost": tpMstpInstancePortPathCost,
       "tpMstpInstancePortRole": tpMstpInstancePortRole,
       "tpMstpInstancePortStatus": tpMstpInstancePortStatus,
       "tpMstpInstancePortLag": tpMstpInstancePortLag,
       "tpStpSecurityCfg": tpStpSecurityCfg,
       "tpStpPortDefendTable": tpStpPortDefendTable,
       "tpStpPortDefendEntry": tpStpPortDefendEntry,
       "tpStpDefendPortNumber": tpStpDefendPortNumber,
       "tpStpLoopDefendEnable": tpStpLoopDefendEnable,
       "tpStpRootBridgeDefendEnable": tpStpRootBridgeDefendEnable,
       "tpStpTcDefendEnable": tpStpTcDefendEnable,
       "tpStpBPDUDefendEnable": tpStpBPDUDefendEnable,
       "tpStpBPDUHoldEnable": tpStpBPDUHoldEnable,
       "tpStpDefendPortLag": tpStpDefendPortLag,
       "tpStpTcDefendConfig": tpStpTcDefendConfig,
       "tpStpTcDefendThreshold": tpStpTcDefendThreshold,
       "tpStpTcDefendTimer": tpStpTcDefendTimer,
       "tplinkSpanningTreeNotifications": tplinkSpanningTreeNotifications,
       "tpMstpTopologyChange": tpMstpTopologyChange}
)
