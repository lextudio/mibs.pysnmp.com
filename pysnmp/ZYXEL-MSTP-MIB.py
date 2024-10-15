# SNMP MIB module (ZYXEL-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-MSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:24 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelMstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MstiOrCistInstanceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_ZyxelMstpSetup_ObjectIdentity = ObjectIdentity
zyxelMstpSetup = _ZyxelMstpSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1)
)
_ZyxelMstpGeneral_ObjectIdentity = ObjectIdentity
zyxelMstpGeneral = _ZyxelMstpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1)
)
_ZyMstpGeneralState_Type = EnabledStatus
_ZyMstpGeneralState_Object = MibScalar
zyMstpGeneralState = _ZyMstpGeneralState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 1),
    _ZyMstpGeneralState_Type()
)
zyMstpGeneralState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpGeneralState.setStatus("current")
_ZyMstpGeneralConfigIdName_Type = DisplayString
_ZyMstpGeneralConfigIdName_Object = MibScalar
zyMstpGeneralConfigIdName = _ZyMstpGeneralConfigIdName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 2),
    _ZyMstpGeneralConfigIdName_Type()
)
zyMstpGeneralConfigIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpGeneralConfigIdName.setStatus("current")
_ZyMstpGeneralConfigIdRevisionLevel_Type = Integer32
_ZyMstpGeneralConfigIdRevisionLevel_Object = MibScalar
zyMstpGeneralConfigIdRevisionLevel = _ZyMstpGeneralConfigIdRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 3),
    _ZyMstpGeneralConfigIdRevisionLevel_Type()
)
zyMstpGeneralConfigIdRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpGeneralConfigIdRevisionLevel.setStatus("current")


class _ZyMstpGeneralHelloTime_Type(Timeout):
    """Custom type zyMstpGeneralHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZyMstpGeneralHelloTime_Type.__name__ = "Timeout"
_ZyMstpGeneralHelloTime_Object = MibScalar
zyMstpGeneralHelloTime = _ZyMstpGeneralHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 4),
    _ZyMstpGeneralHelloTime_Type()
)
zyMstpGeneralHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpGeneralHelloTime.setStatus("current")


class _ZyMstpGeneralMaxAge_Type(Timeout):
    """Custom type zyMstpGeneralMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_ZyMstpGeneralMaxAge_Type.__name__ = "Timeout"
_ZyMstpGeneralMaxAge_Object = MibScalar
zyMstpGeneralMaxAge = _ZyMstpGeneralMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 5),
    _ZyMstpGeneralMaxAge_Type()
)
zyMstpGeneralMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpGeneralMaxAge.setStatus("current")


class _ZyMstpGeneralForwardDelay_Type(Timeout):
    """Custom type zyMstpGeneralForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_ZyMstpGeneralForwardDelay_Type.__name__ = "Timeout"
_ZyMstpGeneralForwardDelay_Object = MibScalar
zyMstpGeneralForwardDelay = _ZyMstpGeneralForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 6),
    _ZyMstpGeneralForwardDelay_Type()
)
zyMstpGeneralForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpGeneralForwardDelay.setStatus("current")


class _ZyMstpGeneralMaxHops_Type(Integer32):
    """Custom type zyMstpGeneralMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZyMstpGeneralMaxHops_Type.__name__ = "Integer32"
_ZyMstpGeneralMaxHops_Object = MibScalar
zyMstpGeneralMaxHops = _ZyMstpGeneralMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 1, 7),
    _ZyMstpGeneralMaxHops_Type()
)
zyMstpGeneralMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpGeneralMaxHops.setStatus("current")
_ZyMstpVlanMapMaxNumberOfInstances_Type = Integer32
_ZyMstpVlanMapMaxNumberOfInstances_Object = MibScalar
zyMstpVlanMapMaxNumberOfInstances = _ZyMstpVlanMapMaxNumberOfInstances_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 2),
    _ZyMstpVlanMapMaxNumberOfInstances_Type()
)
zyMstpVlanMapMaxNumberOfInstances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpVlanMapMaxNumberOfInstances.setStatus("current")
_ZyxelMstpVlanMapTable_Object = MibTable
zyxelMstpVlanMapTable = _ZyxelMstpVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelMstpVlanMapTable.setStatus("current")
_ZyxelMstpVlanMapEntry_Object = MibTableRow
zyxelMstpVlanMapEntry = _ZyxelMstpVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1)
)
zyxelMstpVlanMapEntry.setIndexNames(
    (0, "ZYXEL-MSTP-MIB", "zyMstpVlanMapInstance"),
)
if mibBuilder.loadTexts:
    zyxelMstpVlanMapEntry.setStatus("current")
_ZyMstpVlanMapInstance_Type = MstiOrCistInstanceIndex
_ZyMstpVlanMapInstance_Object = MibTableColumn
zyMstpVlanMapInstance = _ZyMstpVlanMapInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 1),
    _ZyMstpVlanMapInstance_Type()
)
zyMstpVlanMapInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMstpVlanMapInstance.setStatus("current")


class _ZyMstpVlanMapVlans1k_Type(OctetString):
    """Custom type zyMstpVlanMapVlans1k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMstpVlanMapVlans1k_Type.__name__ = "OctetString"
_ZyMstpVlanMapVlans1k_Object = MibTableColumn
zyMstpVlanMapVlans1k = _ZyMstpVlanMapVlans1k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 2),
    _ZyMstpVlanMapVlans1k_Type()
)
zyMstpVlanMapVlans1k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpVlanMapVlans1k.setStatus("current")


class _ZyMstpVlanMapVlans2k_Type(OctetString):
    """Custom type zyMstpVlanMapVlans2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMstpVlanMapVlans2k_Type.__name__ = "OctetString"
_ZyMstpVlanMapVlans2k_Object = MibTableColumn
zyMstpVlanMapVlans2k = _ZyMstpVlanMapVlans2k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 3),
    _ZyMstpVlanMapVlans2k_Type()
)
zyMstpVlanMapVlans2k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpVlanMapVlans2k.setStatus("current")


class _ZyMstpVlanMapVlans3k_Type(OctetString):
    """Custom type zyMstpVlanMapVlans3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMstpVlanMapVlans3k_Type.__name__ = "OctetString"
_ZyMstpVlanMapVlans3k_Object = MibTableColumn
zyMstpVlanMapVlans3k = _ZyMstpVlanMapVlans3k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 4),
    _ZyMstpVlanMapVlans3k_Type()
)
zyMstpVlanMapVlans3k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpVlanMapVlans3k.setStatus("current")


class _ZyMstpVlanMapVlans4k_Type(OctetString):
    """Custom type zyMstpVlanMapVlans4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ZyMstpVlanMapVlans4k_Type.__name__ = "OctetString"
_ZyMstpVlanMapVlans4k_Object = MibTableColumn
zyMstpVlanMapVlans4k = _ZyMstpVlanMapVlans4k_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 5),
    _ZyMstpVlanMapVlans4k_Type()
)
zyMstpVlanMapVlans4k.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpVlanMapVlans4k.setStatus("current")
_ZyMstpVlanMapRowStatus_Type = RowStatus
_ZyMstpVlanMapRowStatus_Object = MibTableColumn
zyMstpVlanMapRowStatus = _ZyMstpVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 3, 1, 6),
    _ZyMstpVlanMapRowStatus_Type()
)
zyMstpVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyMstpVlanMapRowStatus.setStatus("current")
_ZyxelMstpPortTable_Object = MibTable
zyxelMstpPortTable = _ZyxelMstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelMstpPortTable.setStatus("current")
_ZyxelMstpPortEntry_Object = MibTableRow
zyxelMstpPortEntry = _ZyxelMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 4, 1)
)
zyxelMstpPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMstpPortEntry.setStatus("current")


class _ZyMstpPortAdminEdgePort_Type(Integer32):
    """Custom type zyMstpPortAdminEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_ZyMstpPortAdminEdgePort_Type.__name__ = "Integer32"
_ZyMstpPortAdminEdgePort_Object = MibTableColumn
zyMstpPortAdminEdgePort = _ZyMstpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 4, 1, 1),
    _ZyMstpPortAdminEdgePort_Type()
)
zyMstpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpPortAdminEdgePort.setStatus("current")
_ZyxelMstpInstanceTable_Object = MibTable
zyxelMstpInstanceTable = _ZyxelMstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5)
)
if mibBuilder.loadTexts:
    zyxelMstpInstanceTable.setStatus("current")
_ZyxelMstpInstanceEntry_Object = MibTableRow
zyxelMstpInstanceEntry = _ZyxelMstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5, 1)
)
zyxelMstpInstanceEntry.setIndexNames(
    (0, "ZYXEL-MSTP-MIB", "zyMstpInstanceId"),
)
if mibBuilder.loadTexts:
    zyxelMstpInstanceEntry.setStatus("current")
_ZyMstpInstanceId_Type = MstiOrCistInstanceIndex
_ZyMstpInstanceId_Object = MibTableColumn
zyMstpInstanceId = _ZyMstpInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5, 1, 1),
    _ZyMstpInstanceId_Type()
)
zyMstpInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMstpInstanceId.setStatus("current")


class _ZyMstpInstanceBridgePriority_Type(Integer32):
    """Custom type zyMstpInstanceBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_ZyMstpInstanceBridgePriority_Type.__name__ = "Integer32"
_ZyMstpInstanceBridgePriority_Object = MibTableColumn
zyMstpInstanceBridgePriority = _ZyMstpInstanceBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 5, 1, 2),
    _ZyMstpInstanceBridgePriority_Type()
)
zyMstpInstanceBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpInstanceBridgePriority.setStatus("current")
_ZyxelMstpInstancePortTable_Object = MibTable
zyxelMstpInstancePortTable = _ZyxelMstpInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelMstpInstancePortTable.setStatus("current")
_ZyxelMstpInstancePortEntry_Object = MibTableRow
zyxelMstpInstancePortEntry = _ZyxelMstpInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1)
)
zyxelMstpInstancePortEntry.setIndexNames(
    (0, "ZYXEL-MSTP-MIB", "zyMstpInstancePortInstanceId"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMstpInstancePortEntry.setStatus("current")
_ZyMstpInstancePortInstanceId_Type = MstiOrCistInstanceIndex
_ZyMstpInstancePortInstanceId_Object = MibTableColumn
zyMstpInstancePortInstanceId = _ZyMstpInstancePortInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 1),
    _ZyMstpInstancePortInstanceId_Type()
)
zyMstpInstancePortInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMstpInstancePortInstanceId.setStatus("current")
_ZyMstpInstancePortState_Type = EnabledStatus
_ZyMstpInstancePortState_Object = MibTableColumn
zyMstpInstancePortState = _ZyMstpInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 2),
    _ZyMstpInstancePortState_Type()
)
zyMstpInstancePortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpInstancePortState.setStatus("current")


class _ZyMstpInstancePortPriority_Type(Integer32):
    """Custom type zyMstpInstancePortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZyMstpInstancePortPriority_Type.__name__ = "Integer32"
_ZyMstpInstancePortPriority_Object = MibTableColumn
zyMstpInstancePortPriority = _ZyMstpInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 3),
    _ZyMstpInstancePortPriority_Type()
)
zyMstpInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpInstancePortPriority.setStatus("current")


class _ZyMstpInstancePortPathCost_Type(Integer32):
    """Custom type zyMstpInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZyMstpInstancePortPathCost_Type.__name__ = "Integer32"
_ZyMstpInstancePortPathCost_Object = MibTableColumn
zyMstpInstancePortPathCost = _ZyMstpInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 1, 6, 1, 4),
    _ZyMstpInstancePortPathCost_Type()
)
zyMstpInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpInstancePortPathCost.setStatus("current")
_ZyxelMstpStatus_ObjectIdentity = ObjectIdentity
zyxelMstpStatus = _ZyxelMstpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2)
)
_ZyxelMstpInfoGeneral_ObjectIdentity = ObjectIdentity
zyxelMstpInfoGeneral = _ZyxelMstpInfoGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1)
)
_ZyMstpInfoGeneralConfigIdName_Type = DisplayString
_ZyMstpInfoGeneralConfigIdName_Object = MibScalar
zyMstpInfoGeneralConfigIdName = _ZyMstpInfoGeneralConfigIdName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 1),
    _ZyMstpInfoGeneralConfigIdName_Type()
)
zyMstpInfoGeneralConfigIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralConfigIdName.setStatus("current")
_ZyMstpInfoGeneralConfigIdRevisionLevel_Type = Integer32
_ZyMstpInfoGeneralConfigIdRevisionLevel_Object = MibScalar
zyMstpInfoGeneralConfigIdRevisionLevel = _ZyMstpInfoGeneralConfigIdRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 2),
    _ZyMstpInfoGeneralConfigIdRevisionLevel_Type()
)
zyMstpInfoGeneralConfigIdRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralConfigIdRevisionLevel.setStatus("current")


class _ZyMstpInfoGeneralConfigIdConfigDigest_Type(OctetString):
    """Custom type zyMstpInfoGeneralConfigIdConfigDigest based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_ZyMstpInfoGeneralConfigIdConfigDigest_Type.__name__ = "OctetString"
_ZyMstpInfoGeneralConfigIdConfigDigest_Object = MibScalar
zyMstpInfoGeneralConfigIdConfigDigest = _ZyMstpInfoGeneralConfigIdConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 3),
    _ZyMstpInfoGeneralConfigIdConfigDigest_Type()
)
zyMstpInfoGeneralConfigIdConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralConfigIdConfigDigest.setStatus("current")


class _ZyMstpInfoGeneralHelloTime_Type(Timeout):
    """Custom type zyMstpInfoGeneralHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZyMstpInfoGeneralHelloTime_Type.__name__ = "Timeout"
_ZyMstpInfoGeneralHelloTime_Object = MibScalar
zyMstpInfoGeneralHelloTime = _ZyMstpInfoGeneralHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 4),
    _ZyMstpInfoGeneralHelloTime_Type()
)
zyMstpInfoGeneralHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralHelloTime.setStatus("current")


class _ZyMstpInfoGeneralMaxAge_Type(Timeout):
    """Custom type zyMstpInfoGeneralMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_ZyMstpInfoGeneralMaxAge_Type.__name__ = "Timeout"
_ZyMstpInfoGeneralMaxAge_Object = MibScalar
zyMstpInfoGeneralMaxAge = _ZyMstpInfoGeneralMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 5),
    _ZyMstpInfoGeneralMaxAge_Type()
)
zyMstpInfoGeneralMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralMaxAge.setStatus("current")


class _ZyMstpInfoGeneralForwardDelay_Type(Timeout):
    """Custom type zyMstpInfoGeneralForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_ZyMstpInfoGeneralForwardDelay_Type.__name__ = "Timeout"
_ZyMstpInfoGeneralForwardDelay_Object = MibScalar
zyMstpInfoGeneralForwardDelay = _ZyMstpInfoGeneralForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 6),
    _ZyMstpInfoGeneralForwardDelay_Type()
)
zyMstpInfoGeneralForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralForwardDelay.setStatus("current")
_ZyMstpInfoGeneralCistRootPathCost_Type = Integer32
_ZyMstpInfoGeneralCistRootPathCost_Object = MibScalar
zyMstpInfoGeneralCistRootPathCost = _ZyMstpInfoGeneralCistRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 7),
    _ZyMstpInfoGeneralCistRootPathCost_Type()
)
zyMstpInfoGeneralCistRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralCistRootPathCost.setStatus("current")


class _ZyMstpInfoGeneralCistRootBridgeId_Type(OctetString):
    """Custom type zyMstpInfoGeneralCistRootBridgeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ZyMstpInfoGeneralCistRootBridgeId_Type.__name__ = "OctetString"
_ZyMstpInfoGeneralCistRootBridgeId_Object = MibScalar
zyMstpInfoGeneralCistRootBridgeId = _ZyMstpInfoGeneralCistRootBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 1, 8),
    _ZyMstpInfoGeneralCistRootBridgeId_Type()
)
zyMstpInfoGeneralCistRootBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoGeneralCistRootBridgeId.setStatus("current")
_ZyxelMstpInfoVlanMapTable_Object = MibTable
zyxelMstpInfoVlanMapTable = _ZyxelMstpInfoVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2)
)
if mibBuilder.loadTexts:
    zyxelMstpInfoVlanMapTable.setStatus("current")
_ZyxelMstpInfoVlanMapEntry_Object = MibTableRow
zyxelMstpInfoVlanMapEntry = _ZyxelMstpInfoVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2, 1)
)
zyxelMstpInfoVlanMapEntry.setIndexNames(
    (0, "ZYXEL-MSTP-MIB", "zyMstpInfoVlanMapVid"),
)
if mibBuilder.loadTexts:
    zyxelMstpInfoVlanMapEntry.setStatus("current")


class _ZyMstpInfoVlanMapVid_Type(Integer32):
    """Custom type zyMstpInfoVlanMapVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyMstpInfoVlanMapVid_Type.__name__ = "Integer32"
_ZyMstpInfoVlanMapVid_Object = MibTableColumn
zyMstpInfoVlanMapVid = _ZyMstpInfoVlanMapVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2, 1, 1),
    _ZyMstpInfoVlanMapVid_Type()
)
zyMstpInfoVlanMapVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMstpInfoVlanMapVid.setStatus("current")
_ZyMstpInfoVlanMapInstance_Type = MstiOrCistInstanceIndex
_ZyMstpInfoVlanMapInstance_Object = MibTableColumn
zyMstpInfoVlanMapInstance = _ZyMstpInfoVlanMapInstance_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 2, 1, 2),
    _ZyMstpInfoVlanMapInstance_Type()
)
zyMstpInfoVlanMapInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoVlanMapInstance.setStatus("current")
_ZyxelMstpInfoPortTable_Object = MibTable
zyxelMstpInfoPortTable = _ZyxelMstpInfoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3)
)
if mibBuilder.loadTexts:
    zyxelMstpInfoPortTable.setStatus("current")
_ZyxelMstpInfoPortEntry_Object = MibTableRow
zyxelMstpInfoPortEntry = _ZyxelMstpInfoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3, 1)
)
zyxelMstpInfoPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMstpInfoPortEntry.setStatus("current")
_ZyMstpInfoPortOperEdgePort_Type = TruthValue
_ZyMstpInfoPortOperEdgePort_Object = MibTableColumn
zyMstpInfoPortOperEdgePort = _ZyMstpInfoPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3, 1, 1),
    _ZyMstpInfoPortOperEdgePort_Type()
)
zyMstpInfoPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoPortOperEdgePort.setStatus("current")
_ZyMstpInfoPortOperPointToPointMAC_Type = TruthValue
_ZyMstpInfoPortOperPointToPointMAC_Object = MibTableColumn
zyMstpInfoPortOperPointToPointMAC = _ZyMstpInfoPortOperPointToPointMAC_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 3, 1, 2),
    _ZyMstpInfoPortOperPointToPointMAC_Type()
)
zyMstpInfoPortOperPointToPointMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoPortOperPointToPointMAC.setStatus("current")
_ZyxelMstpInfoInstanceTable_Object = MibTable
zyxelMstpInfoInstanceTable = _ZyxelMstpInfoInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4)
)
if mibBuilder.loadTexts:
    zyxelMstpInfoInstanceTable.setStatus("current")
_ZyxelMstpInfoInstanceEntry_Object = MibTableRow
zyxelMstpInfoInstanceEntry = _ZyxelMstpInfoInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1)
)
zyxelMstpInfoInstanceEntry.setIndexNames(
    (0, "ZYXEL-MSTP-MIB", "zyMstpInfoInstanceId"),
)
if mibBuilder.loadTexts:
    zyxelMstpInfoInstanceEntry.setStatus("current")
_ZyMstpInfoInstanceId_Type = MstiOrCistInstanceIndex
_ZyMstpInfoInstanceId_Object = MibTableColumn
zyMstpInfoInstanceId = _ZyMstpInfoInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 1),
    _ZyMstpInfoInstanceId_Type()
)
zyMstpInfoInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMstpInfoInstanceId.setStatus("current")
_ZyMstpInfoInstanceBridgeId_Type = BridgeId
_ZyMstpInfoInstanceBridgeId_Object = MibTableColumn
zyMstpInfoInstanceBridgeId = _ZyMstpInfoInstanceBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 2),
    _ZyMstpInfoInstanceBridgeId_Type()
)
zyMstpInfoInstanceBridgeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstanceBridgeId.setStatus("current")
_ZyMstpInfoInstanceInternalRootCost_Type = Integer32
_ZyMstpInfoInstanceInternalRootCost_Object = MibTableColumn
zyMstpInfoInstanceInternalRootCost = _ZyMstpInfoInstanceInternalRootCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 3),
    _ZyMstpInfoInstanceInternalRootCost_Type()
)
zyMstpInfoInstanceInternalRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstanceInternalRootCost.setStatus("current")
_ZyMstpInfoInstanceRootPort_Type = Integer32
_ZyMstpInfoInstanceRootPort_Object = MibTableColumn
zyMstpInfoInstanceRootPort = _ZyMstpInfoInstanceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 4),
    _ZyMstpInfoInstanceRootPort_Type()
)
zyMstpInfoInstanceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstanceRootPort.setStatus("current")
_ZyMstpInfoInstanceTimeSinceTopologyChange_Type = TimeTicks
_ZyMstpInfoInstanceTimeSinceTopologyChange_Object = MibTableColumn
zyMstpInfoInstanceTimeSinceTopologyChange = _ZyMstpInfoInstanceTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 5),
    _ZyMstpInfoInstanceTimeSinceTopologyChange_Type()
)
zyMstpInfoInstanceTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstanceTimeSinceTopologyChange.setStatus("current")
_ZyMstpInfoInstanceTopologyChangesCount_Type = Counter32
_ZyMstpInfoInstanceTopologyChangesCount_Object = MibTableColumn
zyMstpInfoInstanceTopologyChangesCount = _ZyMstpInfoInstanceTopologyChangesCount_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 4, 1, 6),
    _ZyMstpInfoInstanceTopologyChangesCount_Type()
)
zyMstpInfoInstanceTopologyChangesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstanceTopologyChangesCount.setStatus("current")
_ZyxelMstpInfoInstancePortTable_Object = MibTable
zyxelMstpInfoInstancePortTable = _ZyxelMstpInfoInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5)
)
if mibBuilder.loadTexts:
    zyxelMstpInfoInstancePortTable.setStatus("current")
_ZyxelMstpInfoInstancePortEntry_Object = MibTableRow
zyxelMstpInfoInstancePortEntry = _ZyxelMstpInfoInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1)
)
zyxelMstpInfoInstancePortEntry.setIndexNames(
    (0, "ZYXEL-MSTP-MIB", "zyMstpInfoInstancePortInstanceId"),
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelMstpInfoInstancePortEntry.setStatus("current")
_ZyMstpInfoInstancePortInstanceId_Type = MstiOrCistInstanceIndex
_ZyMstpInfoInstancePortInstanceId_Object = MibTableColumn
zyMstpInfoInstancePortInstanceId = _ZyMstpInfoInstancePortInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 1),
    _ZyMstpInfoInstancePortInstanceId_Type()
)
zyMstpInfoInstancePortInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyMstpInfoInstancePortInstanceId.setStatus("current")


class _ZyMstpInfoInstancePortPathCost_Type(Integer32):
    """Custom type zyMstpInfoInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZyMstpInfoInstancePortPathCost_Type.__name__ = "Integer32"
_ZyMstpInfoInstancePortPathCost_Object = MibTableColumn
zyMstpInfoInstancePortPathCost = _ZyMstpInfoInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 2),
    _ZyMstpInfoInstancePortPathCost_Type()
)
zyMstpInfoInstancePortPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstancePortPathCost.setStatus("current")


class _ZyMstpInfoInstancePortState_Type(Integer32):
    """Custom type zyMstpInfoInstancePortState based on Integer32"""
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
        *(("disabled", 0),
          ("discarding", 1),
          ("forwarding", 3),
          ("learning", 2),
          ("unknown", 4))
    )


_ZyMstpInfoInstancePortState_Type.__name__ = "Integer32"
_ZyMstpInfoInstancePortState_Object = MibTableColumn
zyMstpInfoInstancePortState = _ZyMstpInfoInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 3),
    _ZyMstpInfoInstancePortState_Type()
)
zyMstpInfoInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstancePortState.setStatus("current")
_ZyMstpInfoInstancePortDesignatedRoot_Type = BridgeId
_ZyMstpInfoInstancePortDesignatedRoot_Object = MibTableColumn
zyMstpInfoInstancePortDesignatedRoot = _ZyMstpInfoInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 4),
    _ZyMstpInfoInstancePortDesignatedRoot_Type()
)
zyMstpInfoInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstancePortDesignatedRoot.setStatus("current")
_ZyMstpInfoInstancePortDesignatedCost_Type = Integer32
_ZyMstpInfoInstancePortDesignatedCost_Object = MibTableColumn
zyMstpInfoInstancePortDesignatedCost = _ZyMstpInfoInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 5),
    _ZyMstpInfoInstancePortDesignatedCost_Type()
)
zyMstpInfoInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstancePortDesignatedCost.setStatus("current")
_ZyMstpInfoInstancePortDesignatedBridge_Type = BridgeId
_ZyMstpInfoInstancePortDesignatedBridge_Object = MibTableColumn
zyMstpInfoInstancePortDesignatedBridge = _ZyMstpInfoInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 6),
    _ZyMstpInfoInstancePortDesignatedBridge_Type()
)
zyMstpInfoInstancePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstancePortDesignatedBridge.setStatus("current")
_ZyMstpInfoInstancePortDesignatedPort_Type = Integer32
_ZyMstpInfoInstancePortDesignatedPort_Object = MibTableColumn
zyMstpInfoInstancePortDesignatedPort = _ZyMstpInfoInstancePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 2, 5, 1, 7),
    _ZyMstpInfoInstancePortDesignatedPort_Type()
)
zyMstpInfoInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyMstpInfoInstancePortDesignatedPort.setStatus("current")
_ZyxelMstpNotifications_ObjectIdentity = ObjectIdentity
zyxelMstpNotifications = _ZyxelMstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 3)
)

# Managed Objects groups


# Notification objects

zyMstpNewRoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 3, 1)
)
zyMstpNewRoot.setObjects(
    ("ZYXEL-MSTP-MIB", "zyMstpInstanceId")
)
if mibBuilder.loadTexts:
    zyMstpNewRoot.setStatus(
        "current"
    )

zyMstpTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 53, 3, 2)
)
zyMstpTopologyChange.setObjects(
    ("ZYXEL-MSTP-MIB", "zyMstpInstanceId")
)
if mibBuilder.loadTexts:
    zyMstpTopologyChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-MSTP-MIB",
    **{"MstiOrCistInstanceIndex": MstiOrCistInstanceIndex,
       "zyxelMstp": zyxelMstp,
       "zyxelMstpSetup": zyxelMstpSetup,
       "zyxelMstpGeneral": zyxelMstpGeneral,
       "zyMstpGeneralState": zyMstpGeneralState,
       "zyMstpGeneralConfigIdName": zyMstpGeneralConfigIdName,
       "zyMstpGeneralConfigIdRevisionLevel": zyMstpGeneralConfigIdRevisionLevel,
       "zyMstpGeneralHelloTime": zyMstpGeneralHelloTime,
       "zyMstpGeneralMaxAge": zyMstpGeneralMaxAge,
       "zyMstpGeneralForwardDelay": zyMstpGeneralForwardDelay,
       "zyMstpGeneralMaxHops": zyMstpGeneralMaxHops,
       "zyMstpVlanMapMaxNumberOfInstances": zyMstpVlanMapMaxNumberOfInstances,
       "zyxelMstpVlanMapTable": zyxelMstpVlanMapTable,
       "zyxelMstpVlanMapEntry": zyxelMstpVlanMapEntry,
       "zyMstpVlanMapInstance": zyMstpVlanMapInstance,
       "zyMstpVlanMapVlans1k": zyMstpVlanMapVlans1k,
       "zyMstpVlanMapVlans2k": zyMstpVlanMapVlans2k,
       "zyMstpVlanMapVlans3k": zyMstpVlanMapVlans3k,
       "zyMstpVlanMapVlans4k": zyMstpVlanMapVlans4k,
       "zyMstpVlanMapRowStatus": zyMstpVlanMapRowStatus,
       "zyxelMstpPortTable": zyxelMstpPortTable,
       "zyxelMstpPortEntry": zyxelMstpPortEntry,
       "zyMstpPortAdminEdgePort": zyMstpPortAdminEdgePort,
       "zyxelMstpInstanceTable": zyxelMstpInstanceTable,
       "zyxelMstpInstanceEntry": zyxelMstpInstanceEntry,
       "zyMstpInstanceId": zyMstpInstanceId,
       "zyMstpInstanceBridgePriority": zyMstpInstanceBridgePriority,
       "zyxelMstpInstancePortTable": zyxelMstpInstancePortTable,
       "zyxelMstpInstancePortEntry": zyxelMstpInstancePortEntry,
       "zyMstpInstancePortInstanceId": zyMstpInstancePortInstanceId,
       "zyMstpInstancePortState": zyMstpInstancePortState,
       "zyMstpInstancePortPriority": zyMstpInstancePortPriority,
       "zyMstpInstancePortPathCost": zyMstpInstancePortPathCost,
       "zyxelMstpStatus": zyxelMstpStatus,
       "zyxelMstpInfoGeneral": zyxelMstpInfoGeneral,
       "zyMstpInfoGeneralConfigIdName": zyMstpInfoGeneralConfigIdName,
       "zyMstpInfoGeneralConfigIdRevisionLevel": zyMstpInfoGeneralConfigIdRevisionLevel,
       "zyMstpInfoGeneralConfigIdConfigDigest": zyMstpInfoGeneralConfigIdConfigDigest,
       "zyMstpInfoGeneralHelloTime": zyMstpInfoGeneralHelloTime,
       "zyMstpInfoGeneralMaxAge": zyMstpInfoGeneralMaxAge,
       "zyMstpInfoGeneralForwardDelay": zyMstpInfoGeneralForwardDelay,
       "zyMstpInfoGeneralCistRootPathCost": zyMstpInfoGeneralCistRootPathCost,
       "zyMstpInfoGeneralCistRootBridgeId": zyMstpInfoGeneralCistRootBridgeId,
       "zyxelMstpInfoVlanMapTable": zyxelMstpInfoVlanMapTable,
       "zyxelMstpInfoVlanMapEntry": zyxelMstpInfoVlanMapEntry,
       "zyMstpInfoVlanMapVid": zyMstpInfoVlanMapVid,
       "zyMstpInfoVlanMapInstance": zyMstpInfoVlanMapInstance,
       "zyxelMstpInfoPortTable": zyxelMstpInfoPortTable,
       "zyxelMstpInfoPortEntry": zyxelMstpInfoPortEntry,
       "zyMstpInfoPortOperEdgePort": zyMstpInfoPortOperEdgePort,
       "zyMstpInfoPortOperPointToPointMAC": zyMstpInfoPortOperPointToPointMAC,
       "zyxelMstpInfoInstanceTable": zyxelMstpInfoInstanceTable,
       "zyxelMstpInfoInstanceEntry": zyxelMstpInfoInstanceEntry,
       "zyMstpInfoInstanceId": zyMstpInfoInstanceId,
       "zyMstpInfoInstanceBridgeId": zyMstpInfoInstanceBridgeId,
       "zyMstpInfoInstanceInternalRootCost": zyMstpInfoInstanceInternalRootCost,
       "zyMstpInfoInstanceRootPort": zyMstpInfoInstanceRootPort,
       "zyMstpInfoInstanceTimeSinceTopologyChange": zyMstpInfoInstanceTimeSinceTopologyChange,
       "zyMstpInfoInstanceTopologyChangesCount": zyMstpInfoInstanceTopologyChangesCount,
       "zyxelMstpInfoInstancePortTable": zyxelMstpInfoInstancePortTable,
       "zyxelMstpInfoInstancePortEntry": zyxelMstpInfoInstancePortEntry,
       "zyMstpInfoInstancePortInstanceId": zyMstpInfoInstancePortInstanceId,
       "zyMstpInfoInstancePortPathCost": zyMstpInfoInstancePortPathCost,
       "zyMstpInfoInstancePortState": zyMstpInfoInstancePortState,
       "zyMstpInfoInstancePortDesignatedRoot": zyMstpInfoInstancePortDesignatedRoot,
       "zyMstpInfoInstancePortDesignatedCost": zyMstpInfoInstancePortDesignatedCost,
       "zyMstpInfoInstancePortDesignatedBridge": zyMstpInfoInstancePortDesignatedBridge,
       "zyMstpInfoInstancePortDesignatedPort": zyMstpInfoInstancePortDesignatedPort,
       "zyxelMstpNotifications": zyxelMstpNotifications,
       "zyMstpNewRoot": zyMstpNewRoot,
       "zyMstpTopologyChange": zyMstpTopologyChange}
)
