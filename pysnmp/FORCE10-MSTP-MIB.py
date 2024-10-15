# SNMP MIB module (FORCE10-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORCE10-MSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:25 2024
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
 dot1dBridge) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dBridge")

(f10Experiment,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Experiment")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

f10Mstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class PortIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class MstiInstanceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class BpduCounter(Counter32, TextualConvention):
    status = "current"
    displayHint = "d"


class MstiOrCistInstanceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class PortId(OctetString, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )



# MIB Managed Objects in the order of their OIDs

_MstpTraps_ObjectIdentity = ObjectIdentity
mstpTraps = _MstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 0)
)
_MstpGen_ObjectIdentity = ObjectIdentity
mstpGen = _MstpGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10)
)


class _MstpGenBridgeMaxAge_Type(Timeout):
    """Custom type mstpGenBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MstpGenBridgeMaxAge_Type.__name__ = "Timeout"
_MstpGenBridgeMaxAge_Object = MibScalar
mstpGenBridgeMaxAge = _MstpGenBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 2),
    _MstpGenBridgeMaxAge_Type()
)
mstpGenBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenBridgeMaxAge.setStatus("current")


class _MstpGenBridgeHelloTime_Type(Timeout):
    """Custom type mstpGenBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MstpGenBridgeHelloTime_Type.__name__ = "Timeout"
_MstpGenBridgeHelloTime_Object = MibScalar
mstpGenBridgeHelloTime = _MstpGenBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 3),
    _MstpGenBridgeHelloTime_Type()
)
mstpGenBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenBridgeHelloTime.setStatus("current")


class _MstpGenBridgeForwardDelay_Type(Timeout):
    """Custom type mstpGenBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MstpGenBridgeForwardDelay_Type.__name__ = "Timeout"
_MstpGenBridgeForwardDelay_Object = MibScalar
mstpGenBridgeForwardDelay = _MstpGenBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 4),
    _MstpGenBridgeForwardDelay_Type()
)
mstpGenBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenBridgeForwardDelay.setStatus("current")


class _MstpGenMaxAge_Type(Timeout):
    """Custom type mstpGenMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_MstpGenMaxAge_Type.__name__ = "Timeout"
_MstpGenMaxAge_Object = MibScalar
mstpGenMaxAge = _MstpGenMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 8),
    _MstpGenMaxAge_Type()
)
mstpGenMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenMaxAge.setStatus("current")


class _MstpGenHelloTime_Type(Timeout):
    """Custom type mstpGenHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MstpGenHelloTime_Type.__name__ = "Timeout"
_MstpGenHelloTime_Object = MibScalar
mstpGenHelloTime = _MstpGenHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 9),
    _MstpGenHelloTime_Type()
)
mstpGenHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenHelloTime.setStatus("current")


class _MstpGenForwardDelay_Type(Timeout):
    """Custom type mstpGenForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_MstpGenForwardDelay_Type.__name__ = "Timeout"
_MstpGenForwardDelay_Object = MibScalar
mstpGenForwardDelay = _MstpGenForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 10),
    _MstpGenForwardDelay_Type()
)
mstpGenForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenForwardDelay.setStatus("current")


class _MstpGenMaxHops_Type(Integer32):
    """Custom type mstpGenMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_MstpGenMaxHops_Type.__name__ = "Integer32"
_MstpGenMaxHops_Object = MibScalar
mstpGenMaxHops = _MstpGenMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 14),
    _MstpGenMaxHops_Type()
)
mstpGenMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMaxHops.setStatus("current")


class _MstpGenHoldTime_Type(Timeout):
    """Custom type mstpGenHoldTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MstpGenHoldTime_Type.__name__ = "Timeout"
_MstpGenHoldTime_Object = MibScalar
mstpGenHoldTime = _MstpGenHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 15),
    _MstpGenHoldTime_Type()
)
mstpGenHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenHoldTime.setStatus("current")


class _MstpGenMigrateTime_Type(Timeout):
    """Custom type mstpGenMigrateTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MstpGenMigrateTime_Type.__name__ = "Timeout"
_MstpGenMigrateTime_Object = MibScalar
mstpGenMigrateTime = _MstpGenMigrateTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 16),
    _MstpGenMigrateTime_Type()
)
mstpGenMigrateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenMigrateTime.setStatus("current")


class _MstpGenPathCostDefault_Type(Integer32):
    """Custom type mstpGenPathCostDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pathCostDefault8021d1998", 1),
          ("pathCostDefault8021t2001", 2))
    )


_MstpGenPathCostDefault_Type.__name__ = "Integer32"
_MstpGenPathCostDefault_Object = MibScalar
mstpGenPathCostDefault = _MstpGenPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 18),
    _MstpGenPathCostDefault_Type()
)
mstpGenPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenPathCostDefault.setStatus("current")


class _MstpGenCapable_Type(Integer32):
    """Custom type mstpGenCapable based on Integer32"""
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
        *(("dot1d1998", 1),
          ("dot1d2004", 3),
          ("dot1q", 5),
          ("dot1s", 4),
          ("dot1w", 2),
          ("nonStp", 0),
          ("unknown", 6))
    )


_MstpGenCapable_Type.__name__ = "Integer32"
_MstpGenCapable_Object = MibScalar
mstpGenCapable = _MstpGenCapable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 19),
    _MstpGenCapable_Type()
)
mstpGenCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCapable.setStatus("current")


class _MstpGenForceVersion_Type(Integer32):
    """Custom type mstpGenForceVersion based on Integer32"""
    defaultValue = 3

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
        *(("autoDot1s", 3),
          ("forceDot1w", 2),
          ("forceLegacyDot1d", 1),
          ("forceNonStp", 0),
          ("unknown", 4))
    )


_MstpGenForceVersion_Type.__name__ = "Integer32"
_MstpGenForceVersion_Object = MibScalar
mstpGenForceVersion = _MstpGenForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 20),
    _MstpGenForceVersion_Type()
)
mstpGenForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenForceVersion.setStatus("current")
_MstpGenCfgIdFmtSel_Type = Integer32
_MstpGenCfgIdFmtSel_Object = MibScalar
mstpGenCfgIdFmtSel = _MstpGenCfgIdFmtSel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 30),
    _MstpGenCfgIdFmtSel_Type()
)
mstpGenCfgIdFmtSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdFmtSel.setStatus("current")


class _MstpGenCfgIdName_Type(DisplayString):
    """Custom type mstpGenCfgIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_MstpGenCfgIdName_Type.__name__ = "DisplayString"
_MstpGenCfgIdName_Object = MibScalar
mstpGenCfgIdName = _MstpGenCfgIdName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 31),
    _MstpGenCfgIdName_Type()
)
mstpGenCfgIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdName.setStatus("current")
_MstpGenCfgIdRevLevel_Type = Integer32
_MstpGenCfgIdRevLevel_Object = MibScalar
mstpGenCfgIdRevLevel = _MstpGenCfgIdRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 32),
    _MstpGenCfgIdRevLevel_Type()
)
mstpGenCfgIdRevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpGenCfgIdRevLevel.setStatus("current")


class _MstpGenCfgIdDigest_Type(OctetString):
    """Custom type mstpGenCfgIdDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_MstpGenCfgIdDigest_Type.__name__ = "OctetString"
_MstpGenCfgIdDigest_Object = MibScalar
mstpGenCfgIdDigest = _MstpGenCfgIdDigest_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 33),
    _MstpGenCfgIdDigest_Type()
)
mstpGenCfgIdDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenCfgIdDigest.setStatus("current")
_MstpGenReginalRoot_Type = BridgeId
_MstpGenReginalRoot_Object = MibScalar
mstpGenReginalRoot = _MstpGenReginalRoot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 34),
    _MstpGenReginalRoot_Type()
)
mstpGenReginalRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenReginalRoot.setStatus("current")
_MstpGenExternalRootCost_Type = Integer32
_MstpGenExternalRootCost_Object = MibScalar
mstpGenExternalRootCost = _MstpGenExternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 10, 35),
    _MstpGenExternalRootCost_Type()
)
mstpGenExternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpGenExternalRootCost.setStatus("current")
_MstpPortTable_Object = MibTable
mstpPortTable = _MstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11)
)
if mibBuilder.loadTexts:
    mstpPortTable.setStatus("current")
_MstpPortEntry_Object = MibTableRow
mstpPortEntry = _MstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1)
)
mstpPortEntry.setIndexNames(
    (0, "FORCE10-MSTP-MIB", "mstpPortIndex"),
)
if mibBuilder.loadTexts:
    mstpPortEntry.setStatus("current")
_MstpPortIndex_Type = PortIndex
_MstpPortIndex_Object = MibTableColumn
mstpPortIndex = _MstpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 1),
    _MstpPortIndex_Type()
)
mstpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortIndex.setStatus("current")
_MstpPortAdminMACEnable_Type = TruthValue
_MstpPortAdminMACEnable_Object = MibTableColumn
mstpPortAdminMACEnable = _MstpPortAdminMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 2),
    _MstpPortAdminMACEnable_Type()
)
mstpPortAdminMACEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAdminMACEnable.setStatus("current")
_MstpPortOperMACEnable_Type = TruthValue
_MstpPortOperMACEnable_Object = MibTableColumn
mstpPortOperMACEnable = _MstpPortOperMACEnable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 3),
    _MstpPortOperMACEnable_Type()
)
mstpPortOperMACEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperMACEnable.setStatus("current")
_MstpPortUpTime_Type = TimeTicks
_MstpPortUpTime_Object = MibTableColumn
mstpPortUpTime = _MstpPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 4),
    _MstpPortUpTime_Type()
)
mstpPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortUpTime.setStatus("current")


class _MstpPortAdminExternalPathCost_Type(Integer32):
    """Custom type mstpPortAdminExternalPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstpPortAdminExternalPathCost_Type.__name__ = "Integer32"
_MstpPortAdminExternalPathCost_Object = MibTableColumn
mstpPortAdminExternalPathCost = _MstpPortAdminExternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 5),
    _MstpPortAdminExternalPathCost_Type()
)
mstpPortAdminExternalPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAdminExternalPathCost.setStatus("current")
_MstpPortOperExternalPathCost_Type = Integer32
_MstpPortOperExternalPathCost_Object = MibTableColumn
mstpPortOperExternalPathCost = _MstpPortOperExternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 6),
    _MstpPortOperExternalPathCost_Type()
)
mstpPortOperExternalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperExternalPathCost.setStatus("current")
_MstpPortAdminEdge_Type = TruthValue
_MstpPortAdminEdge_Object = MibTableColumn
mstpPortAdminEdge = _MstpPortAdminEdge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 7),
    _MstpPortAdminEdge_Type()
)
mstpPortAdminEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAdminEdge.setStatus("current")
_MstpPortOperEdge_Type = TruthValue
_MstpPortOperEdge_Object = MibTableColumn
mstpPortOperEdge = _MstpPortOperEdge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 8),
    _MstpPortOperEdge_Type()
)
mstpPortOperEdge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperEdge.setStatus("current")
_MstpPortAutoEdge_Type = TruthValue
_MstpPortAutoEdge_Object = MibTableColumn
mstpPortAutoEdge = _MstpPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 9),
    _MstpPortAutoEdge_Type()
)
mstpPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAutoEdge.setStatus("current")


class _MstpPortAdminPointToPoint_Type(Integer32):
    """Custom type mstpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("forceFalse", 1),
          ("forceTrue", 0))
    )


_MstpPortAdminPointToPoint_Type.__name__ = "Integer32"
_MstpPortAdminPointToPoint_Object = MibTableColumn
mstpPortAdminPointToPoint = _MstpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 10),
    _MstpPortAdminPointToPoint_Type()
)
mstpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAdminPointToPoint.setStatus("current")
_MstpPortOperPointToPoint_Type = TruthValue
_MstpPortOperPointToPoint_Object = MibTableColumn
mstpPortOperPointToPoint = _MstpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 11),
    _MstpPortOperPointToPoint_Type()
)
mstpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortOperPointToPoint.setStatus("current")


class _MstpPortHelloTime_Type(Timeout):
    """Custom type mstpPortHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_MstpPortHelloTime_Type.__name__ = "Timeout"
_MstpPortHelloTime_Object = MibTableColumn
mstpPortHelloTime = _MstpPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 12),
    _MstpPortHelloTime_Type()
)
mstpPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortHelloTime.setStatus("current")
_MstpPortAdminNonStp_Type = TruthValue
_MstpPortAdminNonStp_Object = MibTableColumn
mstpPortAdminNonStp = _MstpPortAdminNonStp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 13),
    _MstpPortAdminNonStp_Type()
)
mstpPortAdminNonStp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortAdminNonStp.setStatus("current")
_MstpPortProtocolMigration_Type = TruthValue
_MstpPortProtocolMigration_Object = MibTableColumn
mstpPortProtocolMigration = _MstpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 14),
    _MstpPortProtocolMigration_Type()
)
mstpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpPortProtocolMigration.setStatus("current")
_MstpPortRxTcnBpduCounter_Type = BpduCounter
_MstpPortRxTcnBpduCounter_Object = MibTableColumn
mstpPortRxTcnBpduCounter = _MstpPortRxTcnBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 15),
    _MstpPortRxTcnBpduCounter_Type()
)
mstpPortRxTcnBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortRxTcnBpduCounter.setStatus("current")
_MstpPortRxCfgBpduCounter_Type = BpduCounter
_MstpPortRxCfgBpduCounter_Object = MibTableColumn
mstpPortRxCfgBpduCounter = _MstpPortRxCfgBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 16),
    _MstpPortRxCfgBpduCounter_Type()
)
mstpPortRxCfgBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortRxCfgBpduCounter.setStatus("current")
_MstpPortRxRstBpduCounter_Type = BpduCounter
_MstpPortRxRstBpduCounter_Object = MibTableColumn
mstpPortRxRstBpduCounter = _MstpPortRxRstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 17),
    _MstpPortRxRstBpduCounter_Type()
)
mstpPortRxRstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortRxRstBpduCounter.setStatus("current")
_MstpPortRxMstBpduCounter_Type = BpduCounter
_MstpPortRxMstBpduCounter_Object = MibTableColumn
mstpPortRxMstBpduCounter = _MstpPortRxMstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 18),
    _MstpPortRxMstBpduCounter_Type()
)
mstpPortRxMstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortRxMstBpduCounter.setStatus("current")
_MstpPortTxTcnBpduCounter_Type = BpduCounter
_MstpPortTxTcnBpduCounter_Object = MibTableColumn
mstpPortTxTcnBpduCounter = _MstpPortTxTcnBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 19),
    _MstpPortTxTcnBpduCounter_Type()
)
mstpPortTxTcnBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortTxTcnBpduCounter.setStatus("current")
_MstpPortTxCfgBpduCounter_Type = BpduCounter
_MstpPortTxCfgBpduCounter_Object = MibTableColumn
mstpPortTxCfgBpduCounter = _MstpPortTxCfgBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 20),
    _MstpPortTxCfgBpduCounter_Type()
)
mstpPortTxCfgBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortTxCfgBpduCounter.setStatus("current")
_MstpPortTxRstBpduCounter_Type = BpduCounter
_MstpPortTxRstBpduCounter_Object = MibTableColumn
mstpPortTxRstBpduCounter = _MstpPortTxRstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 21),
    _MstpPortTxRstBpduCounter_Type()
)
mstpPortTxRstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortTxRstBpduCounter.setStatus("current")
_MstpPortTxMstBpduCounter_Type = BpduCounter
_MstpPortTxMstBpduCounter_Object = MibTableColumn
mstpPortTxMstBpduCounter = _MstpPortTxMstBpduCounter_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 11, 1, 22),
    _MstpPortTxMstBpduCounter_Type()
)
mstpPortTxMstBpduCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpPortTxMstBpduCounter.setStatus("current")
_MstpMapTable_Object = MibTable
mstpMapTable = _MstpMapTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 12)
)
if mibBuilder.loadTexts:
    mstpMapTable.setStatus("current")
_MstpMapEntry_Object = MibTableRow
mstpMapEntry = _MstpMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 12, 1)
)
mstpMapEntry.setIndexNames(
    (0, "FORCE10-MSTP-MIB", "mstpMapMSTiID"),
    (0, "FORCE10-MSTP-MIB", "mstpMapVlanRangeIndex"),
)
if mibBuilder.loadTexts:
    mstpMapEntry.setStatus("current")
_MstpMapMSTiID_Type = MstiInstanceIndex
_MstpMapMSTiID_Object = MibTableColumn
mstpMapMSTiID = _MstpMapMSTiID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 12, 1, 1),
    _MstpMapMSTiID_Type()
)
mstpMapMSTiID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpMapMSTiID.setStatus("current")


class _MstpMapVlanRangeIndex_Type(Integer32):
    """Custom type mstpMapVlanRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MstpMapVlanRangeIndex_Type.__name__ = "Integer32"
_MstpMapVlanRangeIndex_Object = MibTableColumn
mstpMapVlanRangeIndex = _MstpMapVlanRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 12, 1, 2),
    _MstpMapVlanRangeIndex_Type()
)
mstpMapVlanRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpMapVlanRangeIndex.setStatus("current")
_MstpMapVlanMin_Type = VlanId
_MstpMapVlanMin_Object = MibTableColumn
mstpMapVlanMin = _MstpMapVlanMin_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 12, 1, 3),
    _MstpMapVlanMin_Type()
)
mstpMapVlanMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstpMapVlanMin.setStatus("current")
_MstpMapVlanMax_Type = VlanId
_MstpMapVlanMax_Object = MibTableColumn
mstpMapVlanMax = _MstpMapVlanMax_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 12, 1, 4),
    _MstpMapVlanMax_Type()
)
mstpMapVlanMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstpMapVlanMax.setStatus("current")
_MstpMapRowStatus_Type = RowStatus
_MstpMapRowStatus_Object = MibTableColumn
mstpMapRowStatus = _MstpMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 12, 1, 9),
    _MstpMapRowStatus_Type()
)
mstpMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstpMapRowStatus.setStatus("current")
_MstpXstTable_Object = MibTable
mstpXstTable = _MstpXstTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13)
)
if mibBuilder.loadTexts:
    mstpXstTable.setStatus("current")
_MstpXstEntry_Object = MibTableRow
mstpXstEntry = _MstpXstEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1)
)
mstpXstEntry.setIndexNames(
    (0, "FORCE10-MSTP-MIB", "mstpXstId"),
)
if mibBuilder.loadTexts:
    mstpXstEntry.setStatus("current")
_MstpXstId_Type = MstiOrCistInstanceIndex
_MstpXstId_Object = MibTableColumn
mstpXstId = _MstpXstId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 1),
    _MstpXstId_Type()
)
mstpXstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstId.setStatus("current")


class _MstpXstBridgePriority_Type(Integer32):
    """Custom type mstpXstBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_MstpXstBridgePriority_Type.__name__ = "Integer32"
_MstpXstBridgePriority_Object = MibTableColumn
mstpXstBridgePriority = _MstpXstBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 2),
    _MstpXstBridgePriority_Type()
)
mstpXstBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstBridgePriority.setStatus("current")
_MstpXstBridgeId_Type = BridgeId
_MstpXstBridgeId_Object = MibTableColumn
mstpXstBridgeId = _MstpXstBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 3),
    _MstpXstBridgeId_Type()
)
mstpXstBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstBridgeId.setStatus("current")
_MstpXstDesignatedRoot_Type = BridgeId
_MstpXstDesignatedRoot_Object = MibTableColumn
mstpXstDesignatedRoot = _MstpXstDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 4),
    _MstpXstDesignatedRoot_Type()
)
mstpXstDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstDesignatedRoot.setStatus("current")
_MstpXstDesignatedBridge_Type = BridgeId
_MstpXstDesignatedBridge_Object = MibTableColumn
mstpXstDesignatedBridge = _MstpXstDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 5),
    _MstpXstDesignatedBridge_Type()
)
mstpXstDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstDesignatedBridge.setStatus("current")
_MstpXstInternalRootCost_Type = Integer32
_MstpXstInternalRootCost_Object = MibTableColumn
mstpXstInternalRootCost = _MstpXstInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 6),
    _MstpXstInternalRootCost_Type()
)
mstpXstInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstInternalRootCost.setStatus("current")
_MstpXstRootPort_Type = PortIndexOrZero
_MstpXstRootPort_Object = MibTableColumn
mstpXstRootPort = _MstpXstRootPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 7),
    _MstpXstRootPort_Type()
)
mstpXstRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstRootPort.setStatus("current")
_MstpXstMasterPort_Type = PortIndexOrZero
_MstpXstMasterPort_Object = MibTableColumn
mstpXstMasterPort = _MstpXstMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 8),
    _MstpXstMasterPort_Type()
)
mstpXstMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstMasterPort.setStatus("current")
_MstpXstTimeSinceTopologyChange_Type = TimeTicks
_MstpXstTimeSinceTopologyChange_Object = MibTableColumn
mstpXstTimeSinceTopologyChange = _MstpXstTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 11),
    _MstpXstTimeSinceTopologyChange_Type()
)
mstpXstTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTimeSinceTopologyChange.setStatus("current")
_MstpXstTopologyChangesCount_Type = Counter32
_MstpXstTopologyChangesCount_Object = MibTableColumn
mstpXstTopologyChangesCount = _MstpXstTopologyChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 12),
    _MstpXstTopologyChangesCount_Type()
)
mstpXstTopologyChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTopologyChangesCount.setStatus("current")
_MstpXstTopologyChangeFlag_Type = TruthValue
_MstpXstTopologyChangeFlag_Object = MibTableColumn
mstpXstTopologyChangeFlag = _MstpXstTopologyChangeFlag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 13, 1, 13),
    _MstpXstTopologyChangeFlag_Type()
)
mstpXstTopologyChangeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstTopologyChangeFlag.setStatus("current")
_MstpXstPortTable_Object = MibTable
mstpXstPortTable = _MstpXstPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14)
)
if mibBuilder.loadTexts:
    mstpXstPortTable.setStatus("current")
_MstpXstPortEntry_Object = MibTableRow
mstpXstPortEntry = _MstpXstPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1)
)
mstpXstPortEntry.setIndexNames(
    (0, "FORCE10-MSTP-MIB", "mstpXstPortXstId"),
    (0, "FORCE10-MSTP-MIB", "mstpXstPortIndex"),
)
if mibBuilder.loadTexts:
    mstpXstPortEntry.setStatus("current")
_MstpXstPortXstId_Type = MstiOrCistInstanceIndex
_MstpXstPortXstId_Object = MibTableColumn
mstpXstPortXstId = _MstpXstPortXstId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 1),
    _MstpXstPortXstId_Type()
)
mstpXstPortXstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstpXstPortXstId.setStatus("current")
_MstpXstPortIndex_Type = PortIndex
_MstpXstPortIndex_Object = MibTableColumn
mstpXstPortIndex = _MstpXstPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 2),
    _MstpXstPortIndex_Type()
)
mstpXstPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortIndex.setStatus("current")


class _MstpXstPortState_Type(Integer32):
    """Custom type mstpXstPortState based on Integer32"""
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
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 4),
          ("learning", 3),
          ("unknown", 5))
    )


_MstpXstPortState_Type.__name__ = "Integer32"
_MstpXstPortState_Object = MibTableColumn
mstpXstPortState = _MstpXstPortState_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 3),
    _MstpXstPortState_Type()
)
mstpXstPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortState.setStatus("current")


class _MstpXstPortRole_Type(Integer32):
    """Custom type mstpXstPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("master", 6),
          ("nonStp", 7),
          ("root", 4),
          ("unknown", 8))
    )


_MstpXstPortRole_Type.__name__ = "Integer32"
_MstpXstPortRole_Object = MibTableColumn
mstpXstPortRole = _MstpXstPortRole_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 4),
    _MstpXstPortRole_Type()
)
mstpXstPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortRole.setStatus("current")
_MstpXstPortDesignatedRoot_Type = BridgeId
_MstpXstPortDesignatedRoot_Object = MibTableColumn
mstpXstPortDesignatedRoot = _MstpXstPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 6),
    _MstpXstPortDesignatedRoot_Type()
)
mstpXstPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedRoot.setStatus("current")
_MstpXstPortExternalRootCost_Type = Integer32
_MstpXstPortExternalRootCost_Object = MibTableColumn
mstpXstPortExternalRootCost = _MstpXstPortExternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 7),
    _MstpXstPortExternalRootCost_Type()
)
mstpXstPortExternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortExternalRootCost.setStatus("current")
_MstpXstPortRegionalBridge_Type = BridgeId
_MstpXstPortRegionalBridge_Object = MibTableColumn
mstpXstPortRegionalBridge = _MstpXstPortRegionalBridge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 8),
    _MstpXstPortRegionalBridge_Type()
)
mstpXstPortRegionalBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortRegionalBridge.setStatus("current")
_MstpXstPortInternalRootCost_Type = Integer32
_MstpXstPortInternalRootCost_Object = MibTableColumn
mstpXstPortInternalRootCost = _MstpXstPortInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 9),
    _MstpXstPortInternalRootCost_Type()
)
mstpXstPortInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortInternalRootCost.setStatus("current")
_MstpXstPortDesignatedBridge_Type = BridgeId
_MstpXstPortDesignatedBridge_Object = MibTableColumn
mstpXstPortDesignatedBridge = _MstpXstPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 10),
    _MstpXstPortDesignatedBridge_Type()
)
mstpXstPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedBridge.setStatus("current")
_MstpXstPortDesignatedPort_Type = PortId
_MstpXstPortDesignatedPort_Object = MibTableColumn
mstpXstPortDesignatedPort = _MstpXstPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 14),
    _MstpXstPortDesignatedPort_Type()
)
mstpXstPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortDesignatedPort.setStatus("current")


class _MstpXstPortPriority_Type(Integer32):
    """Custom type mstpXstPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MstpXstPortPriority_Type.__name__ = "Integer32"
_MstpXstPortPriority_Object = MibTableColumn
mstpXstPortPriority = _MstpXstPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 15),
    _MstpXstPortPriority_Type()
)
mstpXstPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortPriority.setStatus("current")


class _MstpXstPortAdminInternalPathCost_Type(Integer32):
    """Custom type mstpXstPortAdminInternalPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_MstpXstPortAdminInternalPathCost_Type.__name__ = "Integer32"
_MstpXstPortAdminInternalPathCost_Object = MibTableColumn
mstpXstPortAdminInternalPathCost = _MstpXstPortAdminInternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 16),
    _MstpXstPortAdminInternalPathCost_Type()
)
mstpXstPortAdminInternalPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstpXstPortAdminInternalPathCost.setStatus("current")
_MstpXstPortOperInternalPathCost_Type = Integer32
_MstpXstPortOperInternalPathCost_Object = MibTableColumn
mstpXstPortOperInternalPathCost = _MstpXstPortOperInternalPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 14, 1, 17),
    _MstpXstPortOperInternalPathCost_Type()
)
mstpXstPortOperInternalPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstpXstPortOperInternalPathCost.setStatus("current")

# Managed Objects groups


# Notification objects

mstpNewRootBridge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 0, 1)
)
mstpNewRootBridge.setObjects(
    ("FORCE10-MSTP-MIB", "mstpXstId")
)
if mibBuilder.loadTexts:
    mstpNewRootBridge.setStatus(
        "current"
    )

mstpNewRootPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 0, 2)
)
mstpNewRootPort.setObjects(
      *(("FORCE10-MSTP-MIB", "mstpXstId"),
        ("FORCE10-MSTP-MIB", "mstpXstPortIndex"))
)
if mibBuilder.loadTexts:
    mstpNewRootPort.setStatus(
        "current"
    )

mstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 20, 2, 0, 3)
)
mstpTopologyChange.setObjects(
      *(("FORCE10-MSTP-MIB", "mstpXstId"),
        ("FORCE10-MSTP-MIB", "mstpXstPortIndex"),
        ("FORCE10-MSTP-MIB", "mstpXstPortState"))
)
if mibBuilder.loadTexts:
    mstpTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORCE10-MSTP-MIB",
    **{"PortIndex": PortIndex,
       "PortIndexOrZero": PortIndexOrZero,
       "MstiInstanceIndex": MstiInstanceIndex,
       "BpduCounter": BpduCounter,
       "MstiOrCistInstanceIndex": MstiOrCistInstanceIndex,
       "PortId": PortId,
       "f10Mstp": f10Mstp,
       "mstpTraps": mstpTraps,
       "mstpNewRootBridge": mstpNewRootBridge,
       "mstpNewRootPort": mstpNewRootPort,
       "mstpTopologyChange": mstpTopologyChange,
       "mstpGen": mstpGen,
       "mstpGenBridgeMaxAge": mstpGenBridgeMaxAge,
       "mstpGenBridgeHelloTime": mstpGenBridgeHelloTime,
       "mstpGenBridgeForwardDelay": mstpGenBridgeForwardDelay,
       "mstpGenMaxAge": mstpGenMaxAge,
       "mstpGenHelloTime": mstpGenHelloTime,
       "mstpGenForwardDelay": mstpGenForwardDelay,
       "mstpGenMaxHops": mstpGenMaxHops,
       "mstpGenHoldTime": mstpGenHoldTime,
       "mstpGenMigrateTime": mstpGenMigrateTime,
       "mstpGenPathCostDefault": mstpGenPathCostDefault,
       "mstpGenCapable": mstpGenCapable,
       "mstpGenForceVersion": mstpGenForceVersion,
       "mstpGenCfgIdFmtSel": mstpGenCfgIdFmtSel,
       "mstpGenCfgIdName": mstpGenCfgIdName,
       "mstpGenCfgIdRevLevel": mstpGenCfgIdRevLevel,
       "mstpGenCfgIdDigest": mstpGenCfgIdDigest,
       "mstpGenReginalRoot": mstpGenReginalRoot,
       "mstpGenExternalRootCost": mstpGenExternalRootCost,
       "mstpPortTable": mstpPortTable,
       "mstpPortEntry": mstpPortEntry,
       "mstpPortIndex": mstpPortIndex,
       "mstpPortAdminMACEnable": mstpPortAdminMACEnable,
       "mstpPortOperMACEnable": mstpPortOperMACEnable,
       "mstpPortUpTime": mstpPortUpTime,
       "mstpPortAdminExternalPathCost": mstpPortAdminExternalPathCost,
       "mstpPortOperExternalPathCost": mstpPortOperExternalPathCost,
       "mstpPortAdminEdge": mstpPortAdminEdge,
       "mstpPortOperEdge": mstpPortOperEdge,
       "mstpPortAutoEdge": mstpPortAutoEdge,
       "mstpPortAdminPointToPoint": mstpPortAdminPointToPoint,
       "mstpPortOperPointToPoint": mstpPortOperPointToPoint,
       "mstpPortHelloTime": mstpPortHelloTime,
       "mstpPortAdminNonStp": mstpPortAdminNonStp,
       "mstpPortProtocolMigration": mstpPortProtocolMigration,
       "mstpPortRxTcnBpduCounter": mstpPortRxTcnBpduCounter,
       "mstpPortRxCfgBpduCounter": mstpPortRxCfgBpduCounter,
       "mstpPortRxRstBpduCounter": mstpPortRxRstBpduCounter,
       "mstpPortRxMstBpduCounter": mstpPortRxMstBpduCounter,
       "mstpPortTxTcnBpduCounter": mstpPortTxTcnBpduCounter,
       "mstpPortTxCfgBpduCounter": mstpPortTxCfgBpduCounter,
       "mstpPortTxRstBpduCounter": mstpPortTxRstBpduCounter,
       "mstpPortTxMstBpduCounter": mstpPortTxMstBpduCounter,
       "mstpMapTable": mstpMapTable,
       "mstpMapEntry": mstpMapEntry,
       "mstpMapMSTiID": mstpMapMSTiID,
       "mstpMapVlanRangeIndex": mstpMapVlanRangeIndex,
       "mstpMapVlanMin": mstpMapVlanMin,
       "mstpMapVlanMax": mstpMapVlanMax,
       "mstpMapRowStatus": mstpMapRowStatus,
       "mstpXstTable": mstpXstTable,
       "mstpXstEntry": mstpXstEntry,
       "mstpXstId": mstpXstId,
       "mstpXstBridgePriority": mstpXstBridgePriority,
       "mstpXstBridgeId": mstpXstBridgeId,
       "mstpXstDesignatedRoot": mstpXstDesignatedRoot,
       "mstpXstDesignatedBridge": mstpXstDesignatedBridge,
       "mstpXstInternalRootCost": mstpXstInternalRootCost,
       "mstpXstRootPort": mstpXstRootPort,
       "mstpXstMasterPort": mstpXstMasterPort,
       "mstpXstTimeSinceTopologyChange": mstpXstTimeSinceTopologyChange,
       "mstpXstTopologyChangesCount": mstpXstTopologyChangesCount,
       "mstpXstTopologyChangeFlag": mstpXstTopologyChangeFlag,
       "mstpXstPortTable": mstpXstPortTable,
       "mstpXstPortEntry": mstpXstPortEntry,
       "mstpXstPortXstId": mstpXstPortXstId,
       "mstpXstPortIndex": mstpXstPortIndex,
       "mstpXstPortState": mstpXstPortState,
       "mstpXstPortRole": mstpXstPortRole,
       "mstpXstPortDesignatedRoot": mstpXstPortDesignatedRoot,
       "mstpXstPortExternalRootCost": mstpXstPortExternalRootCost,
       "mstpXstPortRegionalBridge": mstpXstPortRegionalBridge,
       "mstpXstPortInternalRootCost": mstpXstPortInternalRootCost,
       "mstpXstPortDesignatedBridge": mstpXstPortDesignatedBridge,
       "mstpXstPortDesignatedPort": mstpXstPortDesignatedPort,
       "mstpXstPortPriority": mstpXstPortPriority,
       "mstpXstPortAdminInternalPathCost": mstpXstPortAdminInternalPathCost,
       "mstpXstPortOperInternalPathCost": mstpXstPortOperInternalPathCost}
)
