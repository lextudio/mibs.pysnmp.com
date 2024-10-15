# SNMP MIB module (WWP-LEOS-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-MSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:57 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosMstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37)
)
wwpLeosMstp.setRevisions(
        ("2011-08-02 00:00",
         "2006-09-29 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MstiInstanceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class MstiOrCistInstanceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



class BpduCounter(Counter32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_WwpLeosMstpNotifications_ObjectIdentity = ObjectIdentity
wwpLeosMstpNotifications = _WwpLeosMstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0)
)
_WwpLeosMstpObjects_ObjectIdentity = ObjectIdentity
wwpLeosMstpObjects = _WwpLeosMstpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1)
)
_WwpLeosMstpCfg_ObjectIdentity = ObjectIdentity
wwpLeosMstpCfg = _WwpLeosMstpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1)
)


class _WwpLeosMstpBridgeEnable_Type(TruthValue):
    """Custom type wwpLeosMstpBridgeEnable based on TruthValue"""


_WwpLeosMstpBridgeEnable_Object = MibScalar
wwpLeosMstpBridgeEnable = _WwpLeosMstpBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 1),
    _WwpLeosMstpBridgeEnable_Type()
)
wwpLeosMstpBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpBridgeEnable.setStatus("current")


class _WwpLeosMstpForceVersion_Type(Integer32):
    """Custom type wwpLeosMstpForceVersion based on Integer32"""
    defaultValue = 3

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
          ("stp", 0))
    )


_WwpLeosMstpForceVersion_Type.__name__ = "Integer32"
_WwpLeosMstpForceVersion_Object = MibScalar
wwpLeosMstpForceVersion = _WwpLeosMstpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 2),
    _WwpLeosMstpForceVersion_Type()
)
wwpLeosMstpForceVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpForceVersion.setStatus("current")


class _WwpLeosMstpForwardDelay_Type(Integer32):
    """Custom type wwpLeosMstpForwardDelay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_WwpLeosMstpForwardDelay_Type.__name__ = "Integer32"
_WwpLeosMstpForwardDelay_Object = MibScalar
wwpLeosMstpForwardDelay = _WwpLeosMstpForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 3),
    _WwpLeosMstpForwardDelay_Type()
)
wwpLeosMstpForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpForwardDelay.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMstpForwardDelay.setUnits("seconds")


class _WwpLeosMstpTxHoldCount_Type(Integer32):
    """Custom type wwpLeosMstpTxHoldCount based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosMstpTxHoldCount_Type.__name__ = "Integer32"
_WwpLeosMstpTxHoldCount_Object = MibScalar
wwpLeosMstpTxHoldCount = _WwpLeosMstpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 4),
    _WwpLeosMstpTxHoldCount_Type()
)
wwpLeosMstpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpTxHoldCount.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMstpTxHoldCount.setUnits("seconds")


class _WwpLeosMstpHelloTime_Type(Integer32):
    """Custom type wwpLeosMstpHelloTime based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WwpLeosMstpHelloTime_Type.__name__ = "Integer32"
_WwpLeosMstpHelloTime_Object = MibScalar
wwpLeosMstpHelloTime = _WwpLeosMstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 5),
    _WwpLeosMstpHelloTime_Type()
)
wwpLeosMstpHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMstpHelloTime.setUnits("seconds")


class _WwpLeosMstpMaxAge_Type(Integer32):
    """Custom type wwpLeosMstpMaxAge based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_WwpLeosMstpMaxAge_Type.__name__ = "Integer32"
_WwpLeosMstpMaxAge_Object = MibScalar
wwpLeosMstpMaxAge = _WwpLeosMstpMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 6),
    _WwpLeosMstpMaxAge_Type()
)
wwpLeosMstpMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosMstpMaxAge.setUnits("seconds")


class _WwpLeosMstpMaxHops_Type(Integer32):
    """Custom type wwpLeosMstpMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_WwpLeosMstpMaxHops_Type.__name__ = "Integer32"
_WwpLeosMstpMaxHops_Object = MibScalar
wwpLeosMstpMaxHops = _WwpLeosMstpMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 7),
    _WwpLeosMstpMaxHops_Type()
)
wwpLeosMstpMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpMaxHops.setStatus("current")


class _WwpLeosMstpLoopbackBlock_Type(TruthValue):
    """Custom type wwpLeosMstpLoopbackBlock based on TruthValue"""


_WwpLeosMstpLoopbackBlock_Object = MibScalar
wwpLeosMstpLoopbackBlock = _WwpLeosMstpLoopbackBlock_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 8),
    _WwpLeosMstpLoopbackBlock_Type()
)
wwpLeosMstpLoopbackBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpLoopbackBlock.setStatus("current")


class _WwpLeosMstpPathCostDefault_Type(Integer32):
    """Custom type wwpLeosMstpPathCostDefault based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_WwpLeosMstpPathCostDefault_Type.__name__ = "Integer32"
_WwpLeosMstpPathCostDefault_Object = MibScalar
wwpLeosMstpPathCostDefault = _WwpLeosMstpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 9),
    _WwpLeosMstpPathCostDefault_Type()
)
wwpLeosMstpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPathCostDefault.setStatus("current")


class _WwpLeosMstpGlobalStpMode_Type(Integer32):
    """Custom type wwpLeosMstpGlobalStpMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 2),
          ("rstp", 1))
    )


_WwpLeosMstpGlobalStpMode_Type.__name__ = "Integer32"
_WwpLeosMstpGlobalStpMode_Object = MibScalar
wwpLeosMstpGlobalStpMode = _WwpLeosMstpGlobalStpMode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 10),
    _WwpLeosMstpGlobalStpMode_Type()
)
wwpLeosMstpGlobalStpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpGlobalStpMode.setStatus("current")
_WwpLeosMstpPortCfgTable_Object = MibTable
wwpLeosMstpPortCfgTable = _WwpLeosMstpPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11)
)
if mibBuilder.loadTexts:
    wwpLeosMstpPortCfgTable.setStatus("current")
_WwpLeosMstpPortCfgEntry_Object = MibTableRow
wwpLeosMstpPortCfgEntry = _WwpLeosMstpPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1)
)
wwpLeosMstpPortCfgEntry.setIndexNames(
    (0, "WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMstpPortCfgEntry.setStatus("current")


class _WwpLeosMstpPortInfoIndex_Type(Integer32):
    """Custom type wwpLeosMstpPortInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosMstpPortInfoIndex_Type.__name__ = "Integer32"
_WwpLeosMstpPortInfoIndex_Object = MibTableColumn
wwpLeosMstpPortInfoIndex = _WwpLeosMstpPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 1),
    _WwpLeosMstpPortInfoIndex_Type()
)
wwpLeosMstpPortInfoIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosMstpPortInfoIndex.setStatus("current")


class _WwpLeosMstpPortEnable_Type(TruthValue):
    """Custom type wwpLeosMstpPortEnable based on TruthValue"""


_WwpLeosMstpPortEnable_Object = MibTableColumn
wwpLeosMstpPortEnable = _WwpLeosMstpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 2),
    _WwpLeosMstpPortEnable_Type()
)
wwpLeosMstpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortEnable.setStatus("current")


class _WwpLeosMstpPortAdminExtPathCost_Type(Integer32):
    """Custom type wwpLeosMstpPortAdminExtPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_WwpLeosMstpPortAdminExtPathCost_Type.__name__ = "Integer32"
_WwpLeosMstpPortAdminExtPathCost_Object = MibTableColumn
wwpLeosMstpPortAdminExtPathCost = _WwpLeosMstpPortAdminExtPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 3),
    _WwpLeosMstpPortAdminExtPathCost_Type()
)
wwpLeosMstpPortAdminExtPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortAdminExtPathCost.setStatus("current")
_WwpLeosMstpPortOperExtPathCost_Type = Integer32
_WwpLeosMstpPortOperExtPathCost_Object = MibTableColumn
wwpLeosMstpPortOperExtPathCost = _WwpLeosMstpPortOperExtPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 4),
    _WwpLeosMstpPortOperExtPathCost_Type()
)
wwpLeosMstpPortOperExtPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortOperExtPathCost.setStatus("current")


class _WwpLeosMstpPortDynamicExtPathCost_Type(TruthValue):
    """Custom type wwpLeosMstpPortDynamicExtPathCost based on TruthValue"""


_WwpLeosMstpPortDynamicExtPathCost_Object = MibTableColumn
wwpLeosMstpPortDynamicExtPathCost = _WwpLeosMstpPortDynamicExtPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 5),
    _WwpLeosMstpPortDynamicExtPathCost_Type()
)
wwpLeosMstpPortDynamicExtPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortDynamicExtPathCost.setStatus("current")
_WwpLeosMstpPortAdminEdgePort_Type = TruthValue
_WwpLeosMstpPortAdminEdgePort_Object = MibTableColumn
wwpLeosMstpPortAdminEdgePort = _WwpLeosMstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 6),
    _WwpLeosMstpPortAdminEdgePort_Type()
)
wwpLeosMstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortAdminEdgePort.setStatus("current")
_WwpLeosMstpPortOperEdgePort_Type = TruthValue
_WwpLeosMstpPortOperEdgePort_Object = MibTableColumn
wwpLeosMstpPortOperEdgePort = _WwpLeosMstpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 7),
    _WwpLeosMstpPortOperEdgePort_Type()
)
wwpLeosMstpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortOperEdgePort.setStatus("current")
_WwpLeosMstpPortProtocolMigration_Type = TruthValue
_WwpLeosMstpPortProtocolMigration_Object = MibTableColumn
wwpLeosMstpPortProtocolMigration = _WwpLeosMstpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 8),
    _WwpLeosMstpPortProtocolMigration_Type()
)
wwpLeosMstpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortProtocolMigration.setStatus("current")


class _WwpLeosMstpPortAdminPointToPoint_Type(Integer32):
    """Custom type wwpLeosMstpPortAdminPointToPoint based on Integer32"""
    defaultValue = 2

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


_WwpLeosMstpPortAdminPointToPoint_Type.__name__ = "Integer32"
_WwpLeosMstpPortAdminPointToPoint_Object = MibTableColumn
wwpLeosMstpPortAdminPointToPoint = _WwpLeosMstpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 9),
    _WwpLeosMstpPortAdminPointToPoint_Type()
)
wwpLeosMstpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortAdminPointToPoint.setStatus("current")
_WwpLeosMstpPortOperPointToPoint_Type = TruthValue
_WwpLeosMstpPortOperPointToPoint_Object = MibTableColumn
wwpLeosMstpPortOperPointToPoint = _WwpLeosMstpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 10),
    _WwpLeosMstpPortOperPointToPoint_Type()
)
wwpLeosMstpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortOperPointToPoint.setStatus("current")


class _WwpLeosMstpPortAutoEdge_Type(TruthValue):
    """Custom type wwpLeosMstpPortAutoEdge based on TruthValue"""


_WwpLeosMstpPortAutoEdge_Object = MibTableColumn
wwpLeosMstpPortAutoEdge = _WwpLeosMstpPortAutoEdge_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 11),
    _WwpLeosMstpPortAutoEdge_Type()
)
wwpLeosMstpPortAutoEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortAutoEdge.setStatus("current")


class _WwpLeosMstpPortRestrictedRole_Type(TruthValue):
    """Custom type wwpLeosMstpPortRestrictedRole based on TruthValue"""


_WwpLeosMstpPortRestrictedRole_Object = MibTableColumn
wwpLeosMstpPortRestrictedRole = _WwpLeosMstpPortRestrictedRole_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 12),
    _WwpLeosMstpPortRestrictedRole_Type()
)
wwpLeosMstpPortRestrictedRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortRestrictedRole.setStatus("current")


class _WwpLeosMstpPortRestrictedTcn_Type(TruthValue):
    """Custom type wwpLeosMstpPortRestrictedTcn based on TruthValue"""


_WwpLeosMstpPortRestrictedTcn_Object = MibTableColumn
wwpLeosMstpPortRestrictedTcn = _WwpLeosMstpPortRestrictedTcn_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 1, 11, 1, 13),
    _WwpLeosMstpPortRestrictedTcn_Type()
)
wwpLeosMstpPortRestrictedTcn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortRestrictedTcn.setStatus("current")
_WwpLeosMstpMstCfg_ObjectIdentity = ObjectIdentity
wwpLeosMstpMstCfg = _WwpLeosMstpMstCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2)
)


class _WwpLeosMstpMstCfgName_Type(DisplayString):
    """Custom type wwpLeosMstpMstCfgName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_WwpLeosMstpMstCfgName_Type.__name__ = "DisplayString"
_WwpLeosMstpMstCfgName_Object = MibScalar
wwpLeosMstpMstCfgName = _WwpLeosMstpMstCfgName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 1),
    _WwpLeosMstpMstCfgName_Type()
)
wwpLeosMstpMstCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgName.setStatus("current")


class _WwpLeosMstpMstCfgRevLevel_Type(Integer32):
    """Custom type wwpLeosMstpMstCfgRevLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosMstpMstCfgRevLevel_Type.__name__ = "Integer32"
_WwpLeosMstpMstCfgRevLevel_Object = MibScalar
wwpLeosMstpMstCfgRevLevel = _WwpLeosMstpMstCfgRevLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 2),
    _WwpLeosMstpMstCfgRevLevel_Type()
)
wwpLeosMstpMstCfgRevLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgRevLevel.setStatus("current")
_WwpLeosMstpMstCfgVlanTable_Object = MibTable
wwpLeosMstpMstCfgVlanTable = _WwpLeosMstpMstCfgVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 3)
)
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgVlanTable.setStatus("current")
_WwpLeosMstpMstCfgVlanEntry_Object = MibTableRow
wwpLeosMstpMstCfgVlanEntry = _WwpLeosMstpMstCfgVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 3, 1)
)
wwpLeosMstpMstCfgVlanEntry.setIndexNames(
    (0, "WWP-LEOS-MSTP-MIB", "wwpLeosMstpMstCfgVlanIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgVlanEntry.setStatus("current")


class _WwpLeosMstpMstCfgVlanIndex_Type(Integer32):
    """Custom type wwpLeosMstpMstCfgVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosMstpMstCfgVlanIndex_Type.__name__ = "Integer32"
_WwpLeosMstpMstCfgVlanIndex_Object = MibTableColumn
wwpLeosMstpMstCfgVlanIndex = _WwpLeosMstpMstCfgVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 3, 1, 1),
    _WwpLeosMstpMstCfgVlanIndex_Type()
)
wwpLeosMstpMstCfgVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgVlanIndex.setStatus("current")


class _WwpLeosMstpMstCfgMstiIndex_Type(MstiOrCistInstanceIndex):
    """Custom type wwpLeosMstpMstCfgMstiIndex based on MstiOrCistInstanceIndex"""
    defaultValue = 0


_WwpLeosMstpMstCfgMstiIndex_Object = MibTableColumn
wwpLeosMstpMstCfgMstiIndex = _WwpLeosMstpMstCfgMstiIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 3, 1, 2),
    _WwpLeosMstpMstCfgMstiIndex_Type()
)
wwpLeosMstpMstCfgMstiIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgMstiIndex.setStatus("current")
_WwpLeosMstpMstCfgXstMappingTable_Object = MibTable
wwpLeosMstpMstCfgXstMappingTable = _WwpLeosMstpMstCfgXstMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 4)
)
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgXstMappingTable.setStatus("current")
_WwpLeosMstpMstCfgXstMappingEntry_Object = MibTableRow
wwpLeosMstpMstCfgXstMappingEntry = _WwpLeosMstpMstCfgXstMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 4, 1)
)
wwpLeosMstpMstCfgXstMappingEntry.setIndexNames(
    (0, "WWP-LEOS-MSTP-MIB", "wwpLeosMstpMstCfgXstMappingIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgXstMappingEntry.setStatus("current")
_WwpLeosMstpMstCfgXstMappingIndex_Type = MstiOrCistInstanceIndex
_WwpLeosMstpMstCfgXstMappingIndex_Object = MibTableColumn
wwpLeosMstpMstCfgXstMappingIndex = _WwpLeosMstpMstCfgXstMappingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 4, 1, 1),
    _WwpLeosMstpMstCfgXstMappingIndex_Type()
)
wwpLeosMstpMstCfgXstMappingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgXstMappingIndex.setStatus("current")


class _WwpLeosMstpMstCfgXstMapping1k_Type(OctetString):
    """Custom type wwpLeosMstpMstCfgXstMapping1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_WwpLeosMstpMstCfgXstMapping1k_Type.__name__ = "OctetString"
_WwpLeosMstpMstCfgXstMapping1k_Object = MibTableColumn
wwpLeosMstpMstCfgXstMapping1k = _WwpLeosMstpMstCfgXstMapping1k_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 4, 1, 2),
    _WwpLeosMstpMstCfgXstMapping1k_Type()
)
wwpLeosMstpMstCfgXstMapping1k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgXstMapping1k.setStatus("current")


class _WwpLeosMstpMstCfgXstMapping2k_Type(OctetString):
    """Custom type wwpLeosMstpMstCfgXstMapping2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_WwpLeosMstpMstCfgXstMapping2k_Type.__name__ = "OctetString"
_WwpLeosMstpMstCfgXstMapping2k_Object = MibTableColumn
wwpLeosMstpMstCfgXstMapping2k = _WwpLeosMstpMstCfgXstMapping2k_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 4, 1, 3),
    _WwpLeosMstpMstCfgXstMapping2k_Type()
)
wwpLeosMstpMstCfgXstMapping2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgXstMapping2k.setStatus("current")


class _WwpLeosMstpMstCfgXstMapping3k_Type(OctetString):
    """Custom type wwpLeosMstpMstCfgXstMapping3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_WwpLeosMstpMstCfgXstMapping3k_Type.__name__ = "OctetString"
_WwpLeosMstpMstCfgXstMapping3k_Object = MibTableColumn
wwpLeosMstpMstCfgXstMapping3k = _WwpLeosMstpMstCfgXstMapping3k_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 4, 1, 4),
    _WwpLeosMstpMstCfgXstMapping3k_Type()
)
wwpLeosMstpMstCfgXstMapping3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgXstMapping3k.setStatus("current")


class _WwpLeosMstpMstCfgXstMapping4k_Type(OctetString):
    """Custom type wwpLeosMstpMstCfgXstMapping4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_WwpLeosMstpMstCfgXstMapping4k_Type.__name__ = "OctetString"
_WwpLeosMstpMstCfgXstMapping4k_Object = MibTableColumn
wwpLeosMstpMstCfgXstMapping4k = _WwpLeosMstpMstCfgXstMapping4k_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 4, 1, 5),
    _WwpLeosMstpMstCfgXstMapping4k_Type()
)
wwpLeosMstpMstCfgXstMapping4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgXstMapping4k.setStatus("current")


class _WwpLeosMstpMstCfgIdDigest_Type(OctetString):
    """Custom type wwpLeosMstpMstCfgIdDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WwpLeosMstpMstCfgIdDigest_Type.__name__ = "OctetString"
_WwpLeosMstpMstCfgIdDigest_Object = MibScalar
wwpLeosMstpMstCfgIdDigest = _WwpLeosMstpMstCfgIdDigest_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 2, 5),
    _WwpLeosMstpMstCfgIdDigest_Type()
)
wwpLeosMstpMstCfgIdDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpMstCfgIdDigest.setStatus("current")
_WwpLeosMstpXstCfg_ObjectIdentity = ObjectIdentity
wwpLeosMstpXstCfg = _WwpLeosMstpXstCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3)
)
_WwpLeosMstpXstCfgTable_Object = MibTable
wwpLeosMstpXstCfgTable = _WwpLeosMstpXstCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosMstpXstCfgTable.setStatus("current")
_WwpLeosMstpXstCfgEntry_Object = MibTableRow
wwpLeosMstpXstCfgEntry = _WwpLeosMstpXstCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 1, 1)
)
wwpLeosMstpXstCfgEntry.setIndexNames(
    (0, "WWP-LEOS-MSTP-MIB", "wwpLeosMstpXstCfgIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMstpXstCfgEntry.setStatus("current")
_WwpLeosMstpXstCfgIndex_Type = MstiOrCistInstanceIndex
_WwpLeosMstpXstCfgIndex_Object = MibTableColumn
wwpLeosMstpXstCfgIndex = _WwpLeosMstpXstCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 1, 1, 1),
    _WwpLeosMstpXstCfgIndex_Type()
)
wwpLeosMstpXstCfgIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosMstpXstCfgIndex.setStatus("current")


class _WwpLeosMstpXstCfgBridgePriority_Type(Integer32):
    """Custom type wwpLeosMstpXstCfgBridgePriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WwpLeosMstpXstCfgBridgePriority_Type.__name__ = "Integer32"
_WwpLeosMstpXstCfgBridgePriority_Object = MibTableColumn
wwpLeosMstpXstCfgBridgePriority = _WwpLeosMstpXstCfgBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 1, 1, 2),
    _WwpLeosMstpXstCfgBridgePriority_Type()
)
wwpLeosMstpXstCfgBridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMstpXstCfgBridgePriority.setStatus("current")
_WwpLeosMstpXstCfgStatus_Type = RowStatus
_WwpLeosMstpXstCfgStatus_Object = MibTableColumn
wwpLeosMstpXstCfgStatus = _WwpLeosMstpXstCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 1, 1, 3),
    _WwpLeosMstpXstCfgStatus_Type()
)
wwpLeosMstpXstCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wwpLeosMstpXstCfgStatus.setStatus("current")
_WwpLeosMstpXstPortCfgTable_Object = MibTable
wwpLeosMstpXstPortCfgTable = _WwpLeosMstpXstPortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2)
)
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgTable.setStatus("current")
_WwpLeosMstpXstPortCfgEntry_Object = MibTableRow
wwpLeosMstpXstPortCfgEntry = _WwpLeosMstpXstPortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2, 1)
)
wwpLeosMstpXstPortCfgEntry.setIndexNames(
    (0, "WWP-LEOS-MSTP-MIB", "wwpLeosMstpXstPortCfgPortIndex"),
    (0, "WWP-LEOS-MSTP-MIB", "wwpLeosMstpXstPortCfgXstIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgEntry.setStatus("current")


class _WwpLeosMstpXstPortCfgPortIndex_Type(Integer32):
    """Custom type wwpLeosMstpXstPortCfgPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosMstpXstPortCfgPortIndex_Type.__name__ = "Integer32"
_WwpLeosMstpXstPortCfgPortIndex_Object = MibTableColumn
wwpLeosMstpXstPortCfgPortIndex = _WwpLeosMstpXstPortCfgPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2, 1, 1),
    _WwpLeosMstpXstPortCfgPortIndex_Type()
)
wwpLeosMstpXstPortCfgPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgPortIndex.setStatus("current")
_WwpLeosMstpXstPortCfgXstIndex_Type = MstiOrCistInstanceIndex
_WwpLeosMstpXstPortCfgXstIndex_Object = MibTableColumn
wwpLeosMstpXstPortCfgXstIndex = _WwpLeosMstpXstPortCfgXstIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2, 1, 2),
    _WwpLeosMstpXstPortCfgXstIndex_Type()
)
wwpLeosMstpXstPortCfgXstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgXstIndex.setStatus("current")


class _WwpLeosMstpXstPortCfgPortPriority_Type(Integer32):
    """Custom type wwpLeosMstpXstPortCfgPortPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WwpLeosMstpXstPortCfgPortPriority_Type.__name__ = "Integer32"
_WwpLeosMstpXstPortCfgPortPriority_Object = MibTableColumn
wwpLeosMstpXstPortCfgPortPriority = _WwpLeosMstpXstPortCfgPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2, 1, 3),
    _WwpLeosMstpXstPortCfgPortPriority_Type()
)
wwpLeosMstpXstPortCfgPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgPortPriority.setStatus("current")


class _WwpLeosMstpXstPortCfgAdminIntPathCost_Type(Integer32):
    """Custom type wwpLeosMstpXstPortCfgAdminIntPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_WwpLeosMstpXstPortCfgAdminIntPathCost_Type.__name__ = "Integer32"
_WwpLeosMstpXstPortCfgAdminIntPathCost_Object = MibTableColumn
wwpLeosMstpXstPortCfgAdminIntPathCost = _WwpLeosMstpXstPortCfgAdminIntPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2, 1, 4),
    _WwpLeosMstpXstPortCfgAdminIntPathCost_Type()
)
wwpLeosMstpXstPortCfgAdminIntPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgAdminIntPathCost.setStatus("current")
_WwpLeosMstpXstPortCfgOperIntPathCost_Type = Integer32
_WwpLeosMstpXstPortCfgOperIntPathCost_Object = MibTableColumn
wwpLeosMstpXstPortCfgOperIntPathCost = _WwpLeosMstpXstPortCfgOperIntPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2, 1, 5),
    _WwpLeosMstpXstPortCfgOperIntPathCost_Type()
)
wwpLeosMstpXstPortCfgOperIntPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgOperIntPathCost.setStatus("current")


class _WwpLeosMstpXstPortCfgDynamicIntPathCost_Type(TruthValue):
    """Custom type wwpLeosMstpXstPortCfgDynamicIntPathCost based on TruthValue"""


_WwpLeosMstpXstPortCfgDynamicIntPathCost_Object = MibTableColumn
wwpLeosMstpXstPortCfgDynamicIntPathCost = _WwpLeosMstpXstPortCfgDynamicIntPathCost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 3, 2, 1, 6),
    _WwpLeosMstpXstPortCfgDynamicIntPathCost_Type()
)
wwpLeosMstpXstPortCfgDynamicIntPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpXstPortCfgDynamicIntPathCost.setStatus("current")
_WwpLeosMstpStats_ObjectIdentity = ObjectIdentity
wwpLeosMstpStats = _WwpLeosMstpStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4)
)
_WwpLeosMstpBridgeStatsClear_Type = TruthValue
_WwpLeosMstpBridgeStatsClear_Object = MibScalar
wwpLeosMstpBridgeStatsClear = _WwpLeosMstpBridgeStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 1),
    _WwpLeosMstpBridgeStatsClear_Type()
)
wwpLeosMstpBridgeStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpBridgeStatsClear.setStatus("current")
_WwpLeosMstpPortStatsTable_Object = MibTable
wwpLeosMstpPortStatsTable = _WwpLeosMstpPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsTable.setStatus("current")
_WwpLeosMstpPortStatsEntry_Object = MibTableRow
wwpLeosMstpPortStatsEntry = _WwpLeosMstpPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1)
)
wwpLeosMstpPortStatsEntry.setIndexNames(
    (0, "WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortStatsIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsEntry.setStatus("current")


class _WwpLeosMstpPortStatsIndex_Type(Integer32):
    """Custom type wwpLeosMstpPortStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosMstpPortStatsIndex_Type.__name__ = "Integer32"
_WwpLeosMstpPortStatsIndex_Object = MibTableColumn
wwpLeosMstpPortStatsIndex = _WwpLeosMstpPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 1),
    _WwpLeosMstpPortStatsIndex_Type()
)
wwpLeosMstpPortStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsIndex.setStatus("current")
_WwpLeosMstpPortStatsClear_Type = TruthValue
_WwpLeosMstpPortStatsClear_Object = MibTableColumn
wwpLeosMstpPortStatsClear = _WwpLeosMstpPortStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 2),
    _WwpLeosMstpPortStatsClear_Type()
)
wwpLeosMstpPortStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsClear.setStatus("current")
_WwpLeosMstpPortStatsRxTcnBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsRxTcnBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsRxTcnBpdu = _WwpLeosMstpPortStatsRxTcnBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 3),
    _WwpLeosMstpPortStatsRxTcnBpdu_Type()
)
wwpLeosMstpPortStatsRxTcnBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsRxTcnBpdu.setStatus("current")
_WwpLeosMstpPortStatsRxCfgBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsRxCfgBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsRxCfgBpdu = _WwpLeosMstpPortStatsRxCfgBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 4),
    _WwpLeosMstpPortStatsRxCfgBpdu_Type()
)
wwpLeosMstpPortStatsRxCfgBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsRxCfgBpdu.setStatus("current")
_WwpLeosMstpPortStatsRxRstBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsRxRstBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsRxRstBpdu = _WwpLeosMstpPortStatsRxRstBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 5),
    _WwpLeosMstpPortStatsRxRstBpdu_Type()
)
wwpLeosMstpPortStatsRxRstBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsRxRstBpdu.setStatus("current")
_WwpLeosMstpPortStatsRxMstBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsRxMstBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsRxMstBpdu = _WwpLeosMstpPortStatsRxMstBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 6),
    _WwpLeosMstpPortStatsRxMstBpdu_Type()
)
wwpLeosMstpPortStatsRxMstBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsRxMstBpdu.setStatus("current")
_WwpLeosMstpPortStatsTxTcnBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsTxTcnBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsTxTcnBpdu = _WwpLeosMstpPortStatsTxTcnBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 7),
    _WwpLeosMstpPortStatsTxTcnBpdu_Type()
)
wwpLeosMstpPortStatsTxTcnBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsTxTcnBpdu.setStatus("current")
_WwpLeosMstpPortStatsTxCfgBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsTxCfgBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsTxCfgBpdu = _WwpLeosMstpPortStatsTxCfgBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 8),
    _WwpLeosMstpPortStatsTxCfgBpdu_Type()
)
wwpLeosMstpPortStatsTxCfgBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsTxCfgBpdu.setStatus("current")
_WwpLeosMstpPortStatsTxRstBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsTxRstBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsTxRstBpdu = _WwpLeosMstpPortStatsTxRstBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 9),
    _WwpLeosMstpPortStatsTxRstBpdu_Type()
)
wwpLeosMstpPortStatsTxRstBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsTxRstBpdu.setStatus("current")
_WwpLeosMstpPortStatsTxMstBpdu_Type = BpduCounter
_WwpLeosMstpPortStatsTxMstBpdu_Object = MibTableColumn
wwpLeosMstpPortStatsTxMstBpdu = _WwpLeosMstpPortStatsTxMstBpdu_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 1, 4, 2, 1, 10),
    _WwpLeosMstpPortStatsTxMstBpdu_Type()
)
wwpLeosMstpPortStatsTxMstBpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosMstpPortStatsTxMstBpdu.setStatus("current")
_WwpLeosMstpConformance_ObjectIdentity = ObjectIdentity
wwpLeosMstpConformance = _WwpLeosMstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosMstpNewRootNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 1)
)
wwpLeosMstpNewRootNotification.setObjects(
    ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpXstCfgIndex")
)
if mibBuilder.loadTexts:
    wwpLeosMstpNewRootNotification.setStatus(
        "current"
    )

wwpLeosMstpTopologyChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 2)
)
wwpLeosMstpTopologyChangeNotification.setObjects(
      *(("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex"),
        ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpXstCfgIndex"))
)
if mibBuilder.loadTexts:
    wwpLeosMstpTopologyChangeNotification.setStatus(
        "current"
    )

wwpLeosMstpPortBackupNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 3)
)
wwpLeosMstpPortBackupNotification.setObjects(
    ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex")
)
if mibBuilder.loadTexts:
    wwpLeosMstpPortBackupNotification.setStatus(
        "current"
    )

wwpLeosMstpPvstBpduReceivedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 4)
)
wwpLeosMstpPvstBpduReceivedNotification.setObjects(
    ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex")
)
if mibBuilder.loadTexts:
    wwpLeosMstpPvstBpduReceivedNotification.setStatus(
        "deprecated"
    )

wwpLeosMstpSelfLoopNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 5)
)
wwpLeosMstpSelfLoopNotification.setObjects(
    ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex")
)
if mibBuilder.loadTexts:
    wwpLeosMstpSelfLoopNotification.setStatus(
        "current"
    )

wwpLeosMstpPortOperEdgeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 6)
)
wwpLeosMstpPortOperEdgeNotification.setObjects(
      *(("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex"),
        ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortOperEdgePort"))
)
if mibBuilder.loadTexts:
    wwpLeosMstpPortOperEdgeNotification.setStatus(
        "current"
    )

wwpLeosMstpPortFlapNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 7)
)
wwpLeosMstpPortFlapNotification.setObjects(
    ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex")
)
if mibBuilder.loadTexts:
    wwpLeosMstpPortFlapNotification.setStatus(
        "current"
    )

wwpLeosMstpBridgeRootPortLostNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 37, 0, 8)
)
wwpLeosMstpBridgeRootPortLostNotification.setObjects(
      *(("WWP-LEOS-MSTP-MIB", "wwpLeosMstpPortInfoIndex"),
        ("WWP-LEOS-MSTP-MIB", "wwpLeosMstpXstCfgIndex"))
)
if mibBuilder.loadTexts:
    wwpLeosMstpBridgeRootPortLostNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-MSTP-MIB",
    **{"MstiInstanceIndex": MstiInstanceIndex,
       "MstiOrCistInstanceIndex": MstiOrCistInstanceIndex,
       "BpduCounter": BpduCounter,
       "wwpLeosMstp": wwpLeosMstp,
       "wwpLeosMstpNotifications": wwpLeosMstpNotifications,
       "wwpLeosMstpNewRootNotification": wwpLeosMstpNewRootNotification,
       "wwpLeosMstpTopologyChangeNotification": wwpLeosMstpTopologyChangeNotification,
       "wwpLeosMstpPortBackupNotification": wwpLeosMstpPortBackupNotification,
       "wwpLeosMstpPvstBpduReceivedNotification": wwpLeosMstpPvstBpduReceivedNotification,
       "wwpLeosMstpSelfLoopNotification": wwpLeosMstpSelfLoopNotification,
       "wwpLeosMstpPortOperEdgeNotification": wwpLeosMstpPortOperEdgeNotification,
       "wwpLeosMstpPortFlapNotification": wwpLeosMstpPortFlapNotification,
       "wwpLeosMstpBridgeRootPortLostNotification": wwpLeosMstpBridgeRootPortLostNotification,
       "wwpLeosMstpObjects": wwpLeosMstpObjects,
       "wwpLeosMstpCfg": wwpLeosMstpCfg,
       "wwpLeosMstpBridgeEnable": wwpLeosMstpBridgeEnable,
       "wwpLeosMstpForceVersion": wwpLeosMstpForceVersion,
       "wwpLeosMstpForwardDelay": wwpLeosMstpForwardDelay,
       "wwpLeosMstpTxHoldCount": wwpLeosMstpTxHoldCount,
       "wwpLeosMstpHelloTime": wwpLeosMstpHelloTime,
       "wwpLeosMstpMaxAge": wwpLeosMstpMaxAge,
       "wwpLeosMstpMaxHops": wwpLeosMstpMaxHops,
       "wwpLeosMstpLoopbackBlock": wwpLeosMstpLoopbackBlock,
       "wwpLeosMstpPathCostDefault": wwpLeosMstpPathCostDefault,
       "wwpLeosMstpGlobalStpMode": wwpLeosMstpGlobalStpMode,
       "wwpLeosMstpPortCfgTable": wwpLeosMstpPortCfgTable,
       "wwpLeosMstpPortCfgEntry": wwpLeosMstpPortCfgEntry,
       "wwpLeosMstpPortInfoIndex": wwpLeosMstpPortInfoIndex,
       "wwpLeosMstpPortEnable": wwpLeosMstpPortEnable,
       "wwpLeosMstpPortAdminExtPathCost": wwpLeosMstpPortAdminExtPathCost,
       "wwpLeosMstpPortOperExtPathCost": wwpLeosMstpPortOperExtPathCost,
       "wwpLeosMstpPortDynamicExtPathCost": wwpLeosMstpPortDynamicExtPathCost,
       "wwpLeosMstpPortAdminEdgePort": wwpLeosMstpPortAdminEdgePort,
       "wwpLeosMstpPortOperEdgePort": wwpLeosMstpPortOperEdgePort,
       "wwpLeosMstpPortProtocolMigration": wwpLeosMstpPortProtocolMigration,
       "wwpLeosMstpPortAdminPointToPoint": wwpLeosMstpPortAdminPointToPoint,
       "wwpLeosMstpPortOperPointToPoint": wwpLeosMstpPortOperPointToPoint,
       "wwpLeosMstpPortAutoEdge": wwpLeosMstpPortAutoEdge,
       "wwpLeosMstpPortRestrictedRole": wwpLeosMstpPortRestrictedRole,
       "wwpLeosMstpPortRestrictedTcn": wwpLeosMstpPortRestrictedTcn,
       "wwpLeosMstpMstCfg": wwpLeosMstpMstCfg,
       "wwpLeosMstpMstCfgName": wwpLeosMstpMstCfgName,
       "wwpLeosMstpMstCfgRevLevel": wwpLeosMstpMstCfgRevLevel,
       "wwpLeosMstpMstCfgVlanTable": wwpLeosMstpMstCfgVlanTable,
       "wwpLeosMstpMstCfgVlanEntry": wwpLeosMstpMstCfgVlanEntry,
       "wwpLeosMstpMstCfgVlanIndex": wwpLeosMstpMstCfgVlanIndex,
       "wwpLeosMstpMstCfgMstiIndex": wwpLeosMstpMstCfgMstiIndex,
       "wwpLeosMstpMstCfgXstMappingTable": wwpLeosMstpMstCfgXstMappingTable,
       "wwpLeosMstpMstCfgXstMappingEntry": wwpLeosMstpMstCfgXstMappingEntry,
       "wwpLeosMstpMstCfgXstMappingIndex": wwpLeosMstpMstCfgXstMappingIndex,
       "wwpLeosMstpMstCfgXstMapping1k": wwpLeosMstpMstCfgXstMapping1k,
       "wwpLeosMstpMstCfgXstMapping2k": wwpLeosMstpMstCfgXstMapping2k,
       "wwpLeosMstpMstCfgXstMapping3k": wwpLeosMstpMstCfgXstMapping3k,
       "wwpLeosMstpMstCfgXstMapping4k": wwpLeosMstpMstCfgXstMapping4k,
       "wwpLeosMstpMstCfgIdDigest": wwpLeosMstpMstCfgIdDigest,
       "wwpLeosMstpXstCfg": wwpLeosMstpXstCfg,
       "wwpLeosMstpXstCfgTable": wwpLeosMstpXstCfgTable,
       "wwpLeosMstpXstCfgEntry": wwpLeosMstpXstCfgEntry,
       "wwpLeosMstpXstCfgIndex": wwpLeosMstpXstCfgIndex,
       "wwpLeosMstpXstCfgBridgePriority": wwpLeosMstpXstCfgBridgePriority,
       "wwpLeosMstpXstCfgStatus": wwpLeosMstpXstCfgStatus,
       "wwpLeosMstpXstPortCfgTable": wwpLeosMstpXstPortCfgTable,
       "wwpLeosMstpXstPortCfgEntry": wwpLeosMstpXstPortCfgEntry,
       "wwpLeosMstpXstPortCfgPortIndex": wwpLeosMstpXstPortCfgPortIndex,
       "wwpLeosMstpXstPortCfgXstIndex": wwpLeosMstpXstPortCfgXstIndex,
       "wwpLeosMstpXstPortCfgPortPriority": wwpLeosMstpXstPortCfgPortPriority,
       "wwpLeosMstpXstPortCfgAdminIntPathCost": wwpLeosMstpXstPortCfgAdminIntPathCost,
       "wwpLeosMstpXstPortCfgOperIntPathCost": wwpLeosMstpXstPortCfgOperIntPathCost,
       "wwpLeosMstpXstPortCfgDynamicIntPathCost": wwpLeosMstpXstPortCfgDynamicIntPathCost,
       "wwpLeosMstpStats": wwpLeosMstpStats,
       "wwpLeosMstpBridgeStatsClear": wwpLeosMstpBridgeStatsClear,
       "wwpLeosMstpPortStatsTable": wwpLeosMstpPortStatsTable,
       "wwpLeosMstpPortStatsEntry": wwpLeosMstpPortStatsEntry,
       "wwpLeosMstpPortStatsIndex": wwpLeosMstpPortStatsIndex,
       "wwpLeosMstpPortStatsClear": wwpLeosMstpPortStatsClear,
       "wwpLeosMstpPortStatsRxTcnBpdu": wwpLeosMstpPortStatsRxTcnBpdu,
       "wwpLeosMstpPortStatsRxCfgBpdu": wwpLeosMstpPortStatsRxCfgBpdu,
       "wwpLeosMstpPortStatsRxRstBpdu": wwpLeosMstpPortStatsRxRstBpdu,
       "wwpLeosMstpPortStatsRxMstBpdu": wwpLeosMstpPortStatsRxMstBpdu,
       "wwpLeosMstpPortStatsTxTcnBpdu": wwpLeosMstpPortStatsTxTcnBpdu,
       "wwpLeosMstpPortStatsTxCfgBpdu": wwpLeosMstpPortStatsTxCfgBpdu,
       "wwpLeosMstpPortStatsTxRstBpdu": wwpLeosMstpPortStatsTxRstBpdu,
       "wwpLeosMstpPortStatsTxMstBpdu": wwpLeosMstpPortStatsTxMstBpdu,
       "wwpLeosMstpConformance": wwpLeosMstpConformance}
)
