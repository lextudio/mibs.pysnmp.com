# SNMP MIB module (Wellfleet-DECNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DECNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:01 2024
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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfDecGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDecGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfivRouteGroup_ObjectIdentity = ObjectIdentity
wfivRouteGroup = _WfivRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1)
)


class _WfivRouteCreateDelete_Type(Integer32):
    """Custom type wfivRouteCreateDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfivRouteCreateDelete_Type.__name__ = "Integer32"
_WfivRouteCreateDelete_Object = MibScalar
wfivRouteCreateDelete = _WfivRouteCreateDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 1),
    _WfivRouteCreateDelete_Type()
)
wfivRouteCreateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteCreateDelete.setStatus("mandatory")


class _WfivRouteEnableDisable_Type(Integer32):
    """Custom type wfivRouteEnableDisable based on Integer32"""
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


_WfivRouteEnableDisable_Type.__name__ = "Integer32"
_WfivRouteEnableDisable_Object = MibScalar
wfivRouteEnableDisable = _WfivRouteEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 2),
    _WfivRouteEnableDisable_Type()
)
wfivRouteEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteEnableDisable.setStatus("mandatory")


class _WfivRouteState_Type(Integer32):
    """Custom type wfivRouteState based on Integer32"""
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
          ("initializing", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfivRouteState_Type.__name__ = "Integer32"
_WfivRouteState_Object = MibScalar
wfivRouteState = _WfivRouteState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 3),
    _WfivRouteState_Type()
)
wfivRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteState.setStatus("mandatory")


class _WfivRouteBroadcastRouteTimer_Type(Integer32):
    """Custom type wfivRouteBroadcastRouteTimer based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfivRouteBroadcastRouteTimer_Type.__name__ = "Integer32"
_WfivRouteBroadcastRouteTimer_Object = MibScalar
wfivRouteBroadcastRouteTimer = _WfivRouteBroadcastRouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 4),
    _WfivRouteBroadcastRouteTimer_Type()
)
wfivRouteBroadcastRouteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteBroadcastRouteTimer.setStatus("mandatory")
_WfivRouteRoutingVers_Type = DisplayString
_WfivRouteRoutingVers_Object = MibScalar
wfivRouteRoutingVers = _WfivRouteRoutingVers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 5),
    _WfivRouteRoutingVers_Type()
)
wfivRouteRoutingVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteRoutingVers.setStatus("mandatory")


class _WfivRouteMaxAddr_Type(Integer32):
    """Custom type wfivRouteMaxAddr based on Integer32"""
    defaultValue = 1023

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfivRouteMaxAddr_Type.__name__ = "Integer32"
_WfivRouteMaxAddr_Object = MibScalar
wfivRouteMaxAddr = _WfivRouteMaxAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 6),
    _WfivRouteMaxAddr_Type()
)
wfivRouteMaxAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxAddr.setStatus("mandatory")


class _WfivRouteMaxBdcastNonRouters_Type(Integer32):
    """Custom type wfivRouteMaxBdcastNonRouters based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_WfivRouteMaxBdcastNonRouters_Type.__name__ = "Integer32"
_WfivRouteMaxBdcastNonRouters_Object = MibScalar
wfivRouteMaxBdcastNonRouters = _WfivRouteMaxBdcastNonRouters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 7),
    _WfivRouteMaxBdcastNonRouters_Type()
)
wfivRouteMaxBdcastNonRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxBdcastNonRouters.setStatus("mandatory")


class _WfivRouteMaxBdcastRouters_Type(Integer32):
    """Custom type wfivRouteMaxBdcastRouters based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_WfivRouteMaxBdcastRouters_Type.__name__ = "Integer32"
_WfivRouteMaxBdcastRouters_Object = MibScalar
wfivRouteMaxBdcastRouters = _WfivRouteMaxBdcastRouters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 8),
    _WfivRouteMaxBdcastRouters_Type()
)
wfivRouteMaxBdcastRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxBdcastRouters.setStatus("mandatory")


class _WfivRouteMaxCircuits_Type(Integer32):
    """Custom type wfivRouteMaxCircuits based on Integer32"""
    defaultValue = 1024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfivRouteMaxCircuits_Type.__name__ = "Integer32"
_WfivRouteMaxCircuits_Object = MibScalar
wfivRouteMaxCircuits = _WfivRouteMaxCircuits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 9),
    _WfivRouteMaxCircuits_Type()
)
wfivRouteMaxCircuits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxCircuits.setStatus("mandatory")


class _WfivRouteMaxCost_Type(Integer32):
    """Custom type wfivRouteMaxCost based on Integer32"""
    defaultValue = 1022

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1022),
    )


_WfivRouteMaxCost_Type.__name__ = "Integer32"
_WfivRouteMaxCost_Object = MibScalar
wfivRouteMaxCost = _WfivRouteMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 10),
    _WfivRouteMaxCost_Type()
)
wfivRouteMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxCost.setStatus("mandatory")


class _WfivRouteMaxHops_Type(Integer32):
    """Custom type wfivRouteMaxHops based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_WfivRouteMaxHops_Type.__name__ = "Integer32"
_WfivRouteMaxHops_Object = MibScalar
wfivRouteMaxHops = _WfivRouteMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 11),
    _WfivRouteMaxHops_Type()
)
wfivRouteMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxHops.setStatus("mandatory")


class _WfivRouteMaxVisits_Type(Integer32):
    """Custom type wfivRouteMaxVisits based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_WfivRouteMaxVisits_Type.__name__ = "Integer32"
_WfivRouteMaxVisits_Object = MibScalar
wfivRouteMaxVisits = _WfivRouteMaxVisits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 12),
    _WfivRouteMaxVisits_Type()
)
wfivRouteMaxVisits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxVisits.setStatus("mandatory")


class _WfivRouteAreaMaxCost_Type(Integer32):
    """Custom type wfivRouteAreaMaxCost based on Integer32"""
    defaultValue = 1022

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1022),
    )


_WfivRouteAreaMaxCost_Type.__name__ = "Integer32"
_WfivRouteAreaMaxCost_Object = MibScalar
wfivRouteAreaMaxCost = _WfivRouteAreaMaxCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 13),
    _WfivRouteAreaMaxCost_Type()
)
wfivRouteAreaMaxCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteAreaMaxCost.setStatus("mandatory")


class _WfivRouteAreaMaxHops_Type(Integer32):
    """Custom type wfivRouteAreaMaxHops based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_WfivRouteAreaMaxHops_Type.__name__ = "Integer32"
_WfivRouteAreaMaxHops_Object = MibScalar
wfivRouteAreaMaxHops = _WfivRouteAreaMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 14),
    _WfivRouteAreaMaxHops_Type()
)
wfivRouteAreaMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteAreaMaxHops.setStatus("mandatory")


class _WfivRouteMaxArea_Type(Integer32):
    """Custom type wfivRouteMaxArea based on Integer32"""
    defaultValue = 63

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfivRouteMaxArea_Type.__name__ = "Integer32"
_WfivRouteMaxArea_Object = MibScalar
wfivRouteMaxArea = _WfivRouteMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 15),
    _WfivRouteMaxArea_Type()
)
wfivRouteMaxArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteMaxArea.setStatus("mandatory")


class _WfivRouteType_Type(Integer32):
    """Custom type wfivRouteType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("area", 3),
          ("nonroutingiv", 5),
          ("routingiv", 4))
    )


_WfivRouteType_Type.__name__ = "Integer32"
_WfivRouteType_Object = MibScalar
wfivRouteType = _WfivRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 16),
    _WfivRouteType_Type()
)
wfivRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteType.setStatus("mandatory")
_WfivRouteNumAdjs_Type = Counter32
_WfivRouteNumAdjs_Object = MibScalar
wfivRouteNumAdjs = _WfivRouteNumAdjs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 17),
    _WfivRouteNumAdjs_Type()
)
wfivRouteNumAdjs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteNumAdjs.setStatus("mandatory")
_WfivRouteNumLvl1Rts_Type = Counter32
_WfivRouteNumLvl1Rts_Object = MibScalar
wfivRouteNumLvl1Rts = _WfivRouteNumLvl1Rts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 18),
    _WfivRouteNumLvl1Rts_Type()
)
wfivRouteNumLvl1Rts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteNumLvl1Rts.setStatus("mandatory")
_WfivRouteNumAreas_Type = Counter32
_WfivRouteNumAreas_Object = MibScalar
wfivRouteNumAreas = _WfivRouteNumAreas_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 19),
    _WfivRouteNumAreas_Type()
)
wfivRouteNumAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivRouteNumAreas.setStatus("mandatory")


class _WfivRouteLevel1Area_Type(Integer32):
    """Custom type wfivRouteLevel1Area based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfivRouteLevel1Area_Type.__name__ = "Integer32"
_WfivRouteLevel1Area_Object = MibScalar
wfivRouteLevel1Area = _WfivRouteLevel1Area_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 20),
    _WfivRouteLevel1Area_Type()
)
wfivRouteLevel1Area.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivRouteLevel1Area.setStatus("mandatory")


class _WfivTriggeredUpdates_Type(Integer32):
    """Custom type wfivTriggeredUpdates based on Integer32"""
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


_WfivTriggeredUpdates_Type.__name__ = "Integer32"
_WfivTriggeredUpdates_Object = MibScalar
wfivTriggeredUpdates = _WfivTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 21),
    _WfivTriggeredUpdates_Type()
)
wfivTriggeredUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTriggeredUpdates.setStatus("mandatory")


class _WfivTriggeredInterval_Type(Integer32):
    """Custom type wfivTriggeredInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfivTriggeredInterval_Type.__name__ = "Integer32"
_WfivTriggeredInterval_Object = MibScalar
wfivTriggeredInterval = _WfivTriggeredInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 1, 22),
    _WfivTriggeredInterval_Type()
)
wfivTriggeredInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTriggeredInterval.setStatus("mandatory")
_WfivCircuitTable_Object = MibTable
wfivCircuitTable = _WfivCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2)
)
if mibBuilder.loadTexts:
    wfivCircuitTable.setStatus("mandatory")
_WfivCircuitEntry_Object = MibTableRow
wfivCircuitEntry = _WfivCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1)
)
wfivCircuitEntry.setIndexNames(
    (0, "Wellfleet-DECNET-MIB", "wfivCircuitID"),
)
if mibBuilder.loadTexts:
    wfivCircuitEntry.setStatus("mandatory")


class _WfivCircuitCreateDelete_Type(Integer32):
    """Custom type wfivCircuitCreateDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfivCircuitCreateDelete_Type.__name__ = "Integer32"
_WfivCircuitCreateDelete_Object = MibTableColumn
wfivCircuitCreateDelete = _WfivCircuitCreateDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 1),
    _WfivCircuitCreateDelete_Type()
)
wfivCircuitCreateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitCreateDelete.setStatus("mandatory")


class _WfivCircuitEnableDisable_Type(Integer32):
    """Custom type wfivCircuitEnableDisable based on Integer32"""
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


_WfivCircuitEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitEnableDisable_Object = MibTableColumn
wfivCircuitEnableDisable = _WfivCircuitEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 2),
    _WfivCircuitEnableDisable_Type()
)
wfivCircuitEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitEnableDisable.setStatus("mandatory")


class _WfivCircuitCommonState_Type(Integer32):
    """Custom type wfivCircuitCommonState based on Integer32"""
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
          ("initializing", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfivCircuitCommonState_Type.__name__ = "Integer32"
_WfivCircuitCommonState_Object = MibTableColumn
wfivCircuitCommonState = _WfivCircuitCommonState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 3),
    _WfivCircuitCommonState_Type()
)
wfivCircuitCommonState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCommonState.setStatus("mandatory")


class _WfivCircuitArea_Type(Integer32):
    """Custom type wfivCircuitArea based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfivCircuitArea_Type.__name__ = "Integer32"
_WfivCircuitArea_Object = MibTableColumn
wfivCircuitArea = _WfivCircuitArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 4),
    _WfivCircuitArea_Type()
)
wfivCircuitArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitArea.setStatus("mandatory")


class _WfivCircuitNodeid_Type(Integer32):
    """Custom type wfivCircuitNodeid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1023),
    )


_WfivCircuitNodeid_Type.__name__ = "Integer32"
_WfivCircuitNodeid_Object = MibTableColumn
wfivCircuitNodeid = _WfivCircuitNodeid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 5),
    _WfivCircuitNodeid_Type()
)
wfivCircuitNodeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitNodeid.setStatus("mandatory")
_WfivCircuitNodeAddr_Type = DisplayString
_WfivCircuitNodeAddr_Object = MibTableColumn
wfivCircuitNodeAddr = _WfivCircuitNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 6),
    _WfivCircuitNodeAddr_Type()
)
wfivCircuitNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitNodeAddr.setStatus("mandatory")
_WfivCircuitID_Type = Integer32
_WfivCircuitID_Object = MibTableColumn
wfivCircuitID = _WfivCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 7),
    _WfivCircuitID_Type()
)
wfivCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitID.setStatus("mandatory")


class _WfivCircuitCommonType_Type(Integer32):
    """Custom type wfivCircuitCommonType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              6,
              15,
              100,
              101,
              102,
              103,
              104)
        )
    )
    namedValues = NamedValues(
        *(("atm", 102),
          ("ethernet", 6),
          ("fddi", 15),
          ("fr", 101),
          ("ppp", 104),
          ("ring", 103),
          ("smds", 100),
          ("sync", 1),
          ("x25", 4))
    )


_WfivCircuitCommonType_Type.__name__ = "Integer32"
_WfivCircuitCommonType_Object = MibTableColumn
wfivCircuitCommonType = _WfivCircuitCommonType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 8),
    _WfivCircuitCommonType_Type()
)
wfivCircuitCommonType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCommonType.setStatus("mandatory")


class _WfivCircuitExecCost_Type(Integer32):
    """Custom type wfivCircuitExecCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfivCircuitExecCost_Type.__name__ = "Integer32"
_WfivCircuitExecCost_Object = MibTableColumn
wfivCircuitExecCost = _WfivCircuitExecCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 9),
    _WfivCircuitExecCost_Type()
)
wfivCircuitExecCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitExecCost.setStatus("mandatory")


class _WfivCircuitExecHelloTimer_Type(Integer32):
    """Custom type wfivCircuitExecHelloTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_WfivCircuitExecHelloTimer_Type.__name__ = "Integer32"
_WfivCircuitExecHelloTimer_Object = MibTableColumn
wfivCircuitExecHelloTimer = _WfivCircuitExecHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 10),
    _WfivCircuitExecHelloTimer_Type()
)
wfivCircuitExecHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitExecHelloTimer.setStatus("mandatory")
_WfivCircuitDesigRouterNodeAddr_Type = DisplayString
_WfivCircuitDesigRouterNodeAddr_Object = MibTableColumn
wfivCircuitDesigRouterNodeAddr = _WfivCircuitDesigRouterNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 11),
    _WfivCircuitDesigRouterNodeAddr_Type()
)
wfivCircuitDesigRouterNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitDesigRouterNodeAddr.setStatus("mandatory")


class _WfivCircuitMaxRouters_Type(Integer32):
    """Custom type wfivCircuitMaxRouters based on Integer32"""
    defaultValue = 33

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_WfivCircuitMaxRouters_Type.__name__ = "Integer32"
_WfivCircuitMaxRouters_Object = MibTableColumn
wfivCircuitMaxRouters = _WfivCircuitMaxRouters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 12),
    _WfivCircuitMaxRouters_Type()
)
wfivCircuitMaxRouters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitMaxRouters.setStatus("mandatory")


class _WfivCircuitRouterPri_Type(Integer32):
    """Custom type wfivCircuitRouterPri based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WfivCircuitRouterPri_Type.__name__ = "Integer32"
_WfivCircuitRouterPri_Object = MibTableColumn
wfivCircuitRouterPri = _WfivCircuitRouterPri_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 13),
    _WfivCircuitRouterPri_Type()
)
wfivCircuitRouterPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitRouterPri.setStatus("mandatory")
_WfivCircuitCountAgedPktLoss_Type = Counter32
_WfivCircuitCountAgedPktLoss_Object = MibTableColumn
wfivCircuitCountAgedPktLoss = _WfivCircuitCountAgedPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 14),
    _WfivCircuitCountAgedPktLoss_Type()
)
wfivCircuitCountAgedPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountAgedPktLoss.setStatus("mandatory")
_WfivCircuitCountNodeUnrPktLoss_Type = Counter32
_WfivCircuitCountNodeUnrPktLoss_Object = MibTableColumn
wfivCircuitCountNodeUnrPktLoss = _WfivCircuitCountNodeUnrPktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 15),
    _WfivCircuitCountNodeUnrPktLoss_Type()
)
wfivCircuitCountNodeUnrPktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountNodeUnrPktLoss.setStatus("mandatory")
_WfivCircuitCountOutRngePktLoss_Type = Counter32
_WfivCircuitCountOutRngePktLoss_Object = MibTableColumn
wfivCircuitCountOutRngePktLoss = _WfivCircuitCountOutRngePktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 16),
    _WfivCircuitCountOutRngePktLoss_Type()
)
wfivCircuitCountOutRngePktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountOutRngePktLoss.setStatus("mandatory")
_WfivCircuitCountOverSzePktLoss_Type = Counter32
_WfivCircuitCountOverSzePktLoss_Object = MibTableColumn
wfivCircuitCountOverSzePktLoss = _WfivCircuitCountOverSzePktLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 17),
    _WfivCircuitCountOverSzePktLoss_Type()
)
wfivCircuitCountOverSzePktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountOverSzePktLoss.setStatus("mandatory")
_WfivCircuitCountPacketFmtErr_Type = Counter32
_WfivCircuitCountPacketFmtErr_Object = MibTableColumn
wfivCircuitCountPacketFmtErr = _WfivCircuitCountPacketFmtErr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 18),
    _WfivCircuitCountPacketFmtErr_Type()
)
wfivCircuitCountPacketFmtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountPacketFmtErr.setStatus("mandatory")
_WfivCircuitCountPtlRteUpdtLoss_Type = Counter32
_WfivCircuitCountPtlRteUpdtLoss_Object = MibTableColumn
wfivCircuitCountPtlRteUpdtLoss = _WfivCircuitCountPtlRteUpdtLoss_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 19),
    _WfivCircuitCountPtlRteUpdtLoss_Type()
)
wfivCircuitCountPtlRteUpdtLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountPtlRteUpdtLoss.setStatus("mandatory")
_WfivCircuitCountTransitPksRecd_Type = Counter32
_WfivCircuitCountTransitPksRecd_Object = MibTableColumn
wfivCircuitCountTransitPksRecd = _WfivCircuitCountTransitPksRecd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 20),
    _WfivCircuitCountTransitPksRecd_Type()
)
wfivCircuitCountTransitPksRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountTransitPksRecd.setStatus("mandatory")
_WfivCircuitCountTransitPkSent_Type = Counter32
_WfivCircuitCountTransitPkSent_Object = MibTableColumn
wfivCircuitCountTransitPkSent = _WfivCircuitCountTransitPkSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 21),
    _WfivCircuitCountTransitPkSent_Type()
)
wfivCircuitCountTransitPkSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountTransitPkSent.setStatus("mandatory")
_WfivCircuitCountRtHelloSent_Type = Counter32
_WfivCircuitCountRtHelloSent_Object = MibTableColumn
wfivCircuitCountRtHelloSent = _WfivCircuitCountRtHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 22),
    _WfivCircuitCountRtHelloSent_Type()
)
wfivCircuitCountRtHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountRtHelloSent.setStatus("mandatory")
_WfivCircuitCountRtHelloRcvd_Type = Counter32
_WfivCircuitCountRtHelloRcvd_Object = MibTableColumn
wfivCircuitCountRtHelloRcvd = _WfivCircuitCountRtHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 23),
    _WfivCircuitCountRtHelloRcvd_Type()
)
wfivCircuitCountRtHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountRtHelloRcvd.setStatus("mandatory")
_WfivCircuitCountHelloSent_Type = Counter32
_WfivCircuitCountHelloSent_Object = MibTableColumn
wfivCircuitCountHelloSent = _WfivCircuitCountHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 24),
    _WfivCircuitCountHelloSent_Type()
)
wfivCircuitCountHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountHelloSent.setStatus("mandatory")
_WfivCircuitCountHelloRcvd_Type = Counter32
_WfivCircuitCountHelloRcvd_Object = MibTableColumn
wfivCircuitCountHelloRcvd = _WfivCircuitCountHelloRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 25),
    _WfivCircuitCountHelloRcvd_Type()
)
wfivCircuitCountHelloRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountHelloRcvd.setStatus("mandatory")
_WfivCircuitCountL1UpdSent_Type = Counter32
_WfivCircuitCountL1UpdSent_Object = MibTableColumn
wfivCircuitCountL1UpdSent = _WfivCircuitCountL1UpdSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 26),
    _WfivCircuitCountL1UpdSent_Type()
)
wfivCircuitCountL1UpdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountL1UpdSent.setStatus("mandatory")
_WfivCircuitCountL1UpdRcvd_Type = Counter32
_WfivCircuitCountL1UpdRcvd_Object = MibTableColumn
wfivCircuitCountL1UpdRcvd = _WfivCircuitCountL1UpdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 27),
    _WfivCircuitCountL1UpdRcvd_Type()
)
wfivCircuitCountL1UpdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountL1UpdRcvd.setStatus("mandatory")
_WfivCircuitCountAreaUpdSent_Type = Counter32
_WfivCircuitCountAreaUpdSent_Object = MibTableColumn
wfivCircuitCountAreaUpdSent = _WfivCircuitCountAreaUpdSent_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 28),
    _WfivCircuitCountAreaUpdSent_Type()
)
wfivCircuitCountAreaUpdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountAreaUpdSent.setStatus("mandatory")
_WfivCircuitCountAreaUpdRcvd_Type = Counter32
_WfivCircuitCountAreaUpdRcvd_Object = MibTableColumn
wfivCircuitCountAreaUpdRcvd = _WfivCircuitCountAreaUpdRcvd_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 29),
    _WfivCircuitCountAreaUpdRcvd_Type()
)
wfivCircuitCountAreaUpdRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountAreaUpdRcvd.setStatus("mandatory")
_WfivCircuitCountDropped_Type = Counter32
_WfivCircuitCountDropped_Object = MibTableColumn
wfivCircuitCountDropped = _WfivCircuitCountDropped_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 30),
    _WfivCircuitCountDropped_Type()
)
wfivCircuitCountDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitCountDropped.setStatus("mandatory")
_WfivCircuitAllEndnodesMac_Type = OctetString
_WfivCircuitAllEndnodesMac_Object = MibTableColumn
wfivCircuitAllEndnodesMac = _WfivCircuitAllEndnodesMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 31),
    _WfivCircuitAllEndnodesMac_Type()
)
wfivCircuitAllEndnodesMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitAllEndnodesMac.setStatus("mandatory")
_WfivCircuitAllRoutersMac_Type = OctetString
_WfivCircuitAllRoutersMac_Object = MibTableColumn
wfivCircuitAllRoutersMac = _WfivCircuitAllRoutersMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 32),
    _WfivCircuitAllRoutersMac_Type()
)
wfivCircuitAllRoutersMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitAllRoutersMac.setStatus("mandatory")
_WfivCircuitAllAreaRoutersMac_Type = OctetString
_WfivCircuitAllAreaRoutersMac_Object = MibTableColumn
wfivCircuitAllAreaRoutersMac = _WfivCircuitAllAreaRoutersMac_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 33),
    _WfivCircuitAllAreaRoutersMac_Type()
)
wfivCircuitAllAreaRoutersMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitAllAreaRoutersMac.setStatus("mandatory")


class _WfivCircuitHelloEnableDisable_Type(Integer32):
    """Custom type wfivCircuitHelloEnableDisable based on Integer32"""
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


_WfivCircuitHelloEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitHelloEnableDisable_Object = MibTableColumn
wfivCircuitHelloEnableDisable = _WfivCircuitHelloEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 34),
    _WfivCircuitHelloEnableDisable_Type()
)
wfivCircuitHelloEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitHelloEnableDisable.setStatus("mandatory")


class _WfivCircuitRtHelloEnableDisable_Type(Integer32):
    """Custom type wfivCircuitRtHelloEnableDisable based on Integer32"""
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


_WfivCircuitRtHelloEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitRtHelloEnableDisable_Object = MibTableColumn
wfivCircuitRtHelloEnableDisable = _WfivCircuitRtHelloEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 35),
    _WfivCircuitRtHelloEnableDisable_Type()
)
wfivCircuitRtHelloEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitRtHelloEnableDisable.setStatus("mandatory")


class _WfivCircuitL1UpdateEnableDisable_Type(Integer32):
    """Custom type wfivCircuitL1UpdateEnableDisable based on Integer32"""
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


_WfivCircuitL1UpdateEnableDisable_Type.__name__ = "Integer32"
_WfivCircuitL1UpdateEnableDisable_Object = MibTableColumn
wfivCircuitL1UpdateEnableDisable = _WfivCircuitL1UpdateEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 36),
    _WfivCircuitL1UpdateEnableDisable_Type()
)
wfivCircuitL1UpdateEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitL1UpdateEnableDisable.setStatus("mandatory")
_WfivCircuitAllEndnodesMacInUse_Type = OctetString
_WfivCircuitAllEndnodesMacInUse_Object = MibTableColumn
wfivCircuitAllEndnodesMacInUse = _WfivCircuitAllEndnodesMacInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 37),
    _WfivCircuitAllEndnodesMacInUse_Type()
)
wfivCircuitAllEndnodesMacInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitAllEndnodesMacInUse.setStatus("mandatory")
_WfivCircuitAllRoutersMacInUse_Type = OctetString
_WfivCircuitAllRoutersMacInUse_Object = MibTableColumn
wfivCircuitAllRoutersMacInUse = _WfivCircuitAllRoutersMacInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 38),
    _WfivCircuitAllRoutersMacInUse_Type()
)
wfivCircuitAllRoutersMacInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitAllRoutersMacInUse.setStatus("mandatory")
_WfivCircuitAllAreaRoutersMacInUse_Type = OctetString
_WfivCircuitAllAreaRoutersMacInUse_Object = MibTableColumn
wfivCircuitAllAreaRoutersMacInUse = _WfivCircuitAllAreaRoutersMacInUse_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 39),
    _WfivCircuitAllAreaRoutersMacInUse_Type()
)
wfivCircuitAllAreaRoutersMacInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivCircuitAllAreaRoutersMacInUse.setStatus("mandatory")


class _WfivCircuitL2UpdateDisable_Type(Integer32):
    """Custom type wfivCircuitL2UpdateDisable based on Integer32"""
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


_WfivCircuitL2UpdateDisable_Type.__name__ = "Integer32"
_WfivCircuitL2UpdateDisable_Object = MibTableColumn
wfivCircuitL2UpdateDisable = _WfivCircuitL2UpdateDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 40),
    _WfivCircuitL2UpdateDisable_Type()
)
wfivCircuitL2UpdateDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitL2UpdateDisable.setStatus("mandatory")


class _WfivCircuitLevel_Type(Integer32):
    """Custom type wfivCircuitLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level2", 1),
          ("only", 2))
    )


_WfivCircuitLevel_Type.__name__ = "Integer32"
_WfivCircuitLevel_Object = MibTableColumn
wfivCircuitLevel = _WfivCircuitLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 2, 1, 41),
    _WfivCircuitLevel_Type()
)
wfivCircuitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivCircuitLevel.setStatus("mandatory")
_WfivLevel1RouteTable_Object = MibTable
wfivLevel1RouteTable = _WfivLevel1RouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3)
)
if mibBuilder.loadTexts:
    wfivLevel1RouteTable.setStatus("mandatory")
_WfivLevel1RouteEntry_Object = MibTableRow
wfivLevel1RouteEntry = _WfivLevel1RouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1)
)
wfivLevel1RouteEntry.setIndexNames(
    (0, "Wellfleet-DECNET-MIB", "wfivLevel1AreaId"),
    (0, "Wellfleet-DECNET-MIB", "wfivLevel1NodeId"),
)
if mibBuilder.loadTexts:
    wfivLevel1RouteEntry.setStatus("mandatory")
_WfivLevel1AreaId_Type = Integer32
_WfivLevel1AreaId_Object = MibTableColumn
wfivLevel1AreaId = _WfivLevel1AreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 1),
    _WfivLevel1AreaId_Type()
)
wfivLevel1AreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1AreaId.setStatus("mandatory")
_WfivLevel1NodeId_Type = Integer32
_WfivLevel1NodeId_Object = MibTableColumn
wfivLevel1NodeId = _WfivLevel1NodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 2),
    _WfivLevel1NodeId_Type()
)
wfivLevel1NodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1NodeId.setStatus("mandatory")
_WfivLevel1RouteNodeAddr_Type = DisplayString
_WfivLevel1RouteNodeAddr_Object = MibTableColumn
wfivLevel1RouteNodeAddr = _WfivLevel1RouteNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 3),
    _WfivLevel1RouteNodeAddr_Type()
)
wfivLevel1RouteNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteNodeAddr.setStatus("mandatory")
_WfivLevel1RouteCircuitID_Type = Integer32
_WfivLevel1RouteCircuitID_Object = MibTableColumn
wfivLevel1RouteCircuitID = _WfivLevel1RouteCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 4),
    _WfivLevel1RouteCircuitID_Type()
)
wfivLevel1RouteCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteCircuitID.setStatus("mandatory")
_WfivLevel1RouteCost_Type = Integer32
_WfivLevel1RouteCost_Object = MibTableColumn
wfivLevel1RouteCost = _WfivLevel1RouteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 5),
    _WfivLevel1RouteCost_Type()
)
wfivLevel1RouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteCost.setStatus("mandatory")
_WfivLevel1RouteHops_Type = Integer32
_WfivLevel1RouteHops_Object = MibTableColumn
wfivLevel1RouteHops = _WfivLevel1RouteHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 6),
    _WfivLevel1RouteHops_Type()
)
wfivLevel1RouteHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteHops.setStatus("mandatory")
_WfivLevel1RouteNextNode_Type = DisplayString
_WfivLevel1RouteNextNode_Object = MibTableColumn
wfivLevel1RouteNextNode = _WfivLevel1RouteNextNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 7),
    _WfivLevel1RouteNextNode_Type()
)
wfivLevel1RouteNextNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivLevel1RouteNextNode.setStatus("mandatory")


class _WfivLevel1RouteDynamic_Type(Integer32):
    """Custom type wfivLevel1RouteDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_WfivLevel1RouteDynamic_Type.__name__ = "Integer32"
_WfivLevel1RouteDynamic_Object = MibTableColumn
wfivLevel1RouteDynamic = _WfivLevel1RouteDynamic_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 3, 1, 8),
    _WfivLevel1RouteDynamic_Type()
)
wfivLevel1RouteDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivLevel1RouteDynamic.setStatus("mandatory")
_WfivAreaTable_Object = MibTable
wfivAreaTable = _WfivAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4)
)
if mibBuilder.loadTexts:
    wfivAreaTable.setStatus("mandatory")
_WfivAreaEntry_Object = MibTableRow
wfivAreaEntry = _WfivAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1)
)
wfivAreaEntry.setIndexNames(
    (0, "Wellfleet-DECNET-MIB", "wfivAreaNum"),
)
if mibBuilder.loadTexts:
    wfivAreaEntry.setStatus("mandatory")
_WfivAreaNum_Type = Integer32
_WfivAreaNum_Object = MibTableColumn
wfivAreaNum = _WfivAreaNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 1),
    _WfivAreaNum_Type()
)
wfivAreaNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaNum.setStatus("mandatory")


class _WfivAreaState_Type(Integer32):
    """Custom type wfivAreaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 4),
          ("unreachable", 5))
    )


_WfivAreaState_Type.__name__ = "Integer32"
_WfivAreaState_Object = MibTableColumn
wfivAreaState = _WfivAreaState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 2),
    _WfivAreaState_Type()
)
wfivAreaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaState.setStatus("mandatory")
_WfivAreaCost_Type = Integer32
_WfivAreaCost_Object = MibTableColumn
wfivAreaCost = _WfivAreaCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 3),
    _WfivAreaCost_Type()
)
wfivAreaCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaCost.setStatus("mandatory")
_WfivAreaHops_Type = Integer32
_WfivAreaHops_Object = MibTableColumn
wfivAreaHops = _WfivAreaHops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 4),
    _WfivAreaHops_Type()
)
wfivAreaHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaHops.setStatus("mandatory")
_WfivAreaCircuitID_Type = Integer32
_WfivAreaCircuitID_Object = MibTableColumn
wfivAreaCircuitID = _WfivAreaCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 5),
    _WfivAreaCircuitID_Type()
)
wfivAreaCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaCircuitID.setStatus("mandatory")
_WfivAreaNextNode_Type = DisplayString
_WfivAreaNextNode_Object = MibTableColumn
wfivAreaNextNode = _WfivAreaNextNode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 6),
    _WfivAreaNextNode_Type()
)
wfivAreaNextNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAreaNextNode.setStatus("mandatory")


class _WfivAreaRouteDynamic_Type(Integer32):
    """Custom type wfivAreaRouteDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_WfivAreaRouteDynamic_Type.__name__ = "Integer32"
_WfivAreaRouteDynamic_Object = MibTableColumn
wfivAreaRouteDynamic = _WfivAreaRouteDynamic_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 4, 1, 7),
    _WfivAreaRouteDynamic_Type()
)
wfivAreaRouteDynamic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivAreaRouteDynamic.setStatus("mandatory")
_WfivAdjTable_Object = MibTable
wfivAdjTable = _WfivAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5)
)
if mibBuilder.loadTexts:
    wfivAdjTable.setStatus("mandatory")
_WfivAdjEntry_Object = MibTableRow
wfivAdjEntry = _WfivAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1)
)
wfivAdjEntry.setIndexNames(
    (0, "Wellfleet-DECNET-MIB", "wfivAdjIndex"),
)
if mibBuilder.loadTexts:
    wfivAdjEntry.setStatus("mandatory")
_WfivAdjIndex_Type = Integer32
_WfivAdjIndex_Object = MibTableColumn
wfivAdjIndex = _WfivAdjIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 1),
    _WfivAdjIndex_Type()
)
wfivAdjIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjIndex.setStatus("mandatory")
_WfivAdjNodeAddr_Type = DisplayString
_WfivAdjNodeAddr_Object = MibTableColumn
wfivAdjNodeAddr = _WfivAdjNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 2),
    _WfivAdjNodeAddr_Type()
)
wfivAdjNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjNodeAddr.setStatus("mandatory")
_WfivAdjBlockSize_Type = Integer32
_WfivAdjBlockSize_Object = MibTableColumn
wfivAdjBlockSize = _WfivAdjBlockSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 3),
    _WfivAdjBlockSize_Type()
)
wfivAdjBlockSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjBlockSize.setStatus("mandatory")
_WfivAdjListenTimer_Type = Integer32
_WfivAdjListenTimer_Object = MibTableColumn
wfivAdjListenTimer = _WfivAdjListenTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 4),
    _WfivAdjListenTimer_Type()
)
wfivAdjListenTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjListenTimer.setStatus("mandatory")
_WfivAdjCircuitID_Type = Integer32
_WfivAdjCircuitID_Object = MibTableColumn
wfivAdjCircuitID = _WfivAdjCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 5),
    _WfivAdjCircuitID_Type()
)
wfivAdjCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjCircuitID.setStatus("mandatory")
_WfivAdjType_Type = Integer32
_WfivAdjType_Object = MibTableColumn
wfivAdjType = _WfivAdjType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 6),
    _WfivAdjType_Type()
)
wfivAdjType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjType.setStatus("mandatory")


class _WfivAdjState_Type(Integer32):
    """Custom type wfivAdjState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("up", 2))
    )


_WfivAdjState_Type.__name__ = "Integer32"
_WfivAdjState_Object = MibTableColumn
wfivAdjState = _WfivAdjState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 7),
    _WfivAdjState_Type()
)
wfivAdjState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjState.setStatus("mandatory")
_WfivAdjPriority_Type = Integer32
_WfivAdjPriority_Object = MibTableColumn
wfivAdjPriority = _WfivAdjPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 8),
    _WfivAdjPriority_Type()
)
wfivAdjPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjPriority.setStatus("mandatory")
_WfivAdjClass_Type = Integer32
_WfivAdjClass_Object = MibTableColumn
wfivAdjClass = _WfivAdjClass_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 5, 1, 9),
    _WfivAdjClass_Type()
)
wfivAdjClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAdjClass.setStatus("mandatory")
_WfivTrafficFilterTable_Object = MibTable
wfivTrafficFilterTable = _WfivTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6)
)
if mibBuilder.loadTexts:
    wfivTrafficFilterTable.setStatus("mandatory")
_WfivTrafficFilterEntry_Object = MibTableRow
wfivTrafficFilterEntry = _WfivTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1)
)
wfivTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-DECNET-MIB", "wfivTrafficFilterCircuit"),
    (0, "Wellfleet-DECNET-MIB", "wfivTrafficFilterRuleNumber"),
    (0, "Wellfleet-DECNET-MIB", "wfivTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfivTrafficFilterEntry.setStatus("mandatory")


class _WfivTrafficFilterCreate_Type(Integer32):
    """Custom type wfivTrafficFilterCreate based on Integer32"""
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


_WfivTrafficFilterCreate_Type.__name__ = "Integer32"
_WfivTrafficFilterCreate_Object = MibTableColumn
wfivTrafficFilterCreate = _WfivTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 1),
    _WfivTrafficFilterCreate_Type()
)
wfivTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTrafficFilterCreate.setStatus("mandatory")


class _WfivTrafficFilterEnable_Type(Integer32):
    """Custom type wfivTrafficFilterEnable based on Integer32"""
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


_WfivTrafficFilterEnable_Type.__name__ = "Integer32"
_WfivTrafficFilterEnable_Object = MibTableColumn
wfivTrafficFilterEnable = _WfivTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 2),
    _WfivTrafficFilterEnable_Type()
)
wfivTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTrafficFilterEnable.setStatus("mandatory")


class _WfivTrafficFilterStatus_Type(Integer32):
    """Custom type wfivTrafficFilterStatus based on Integer32"""
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
        *(("active", 1),
          ("error", 2),
          ("inactive", 3))
    )


_WfivTrafficFilterStatus_Type.__name__ = "Integer32"
_WfivTrafficFilterStatus_Object = MibTableColumn
wfivTrafficFilterStatus = _WfivTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 3),
    _WfivTrafficFilterStatus_Type()
)
wfivTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterStatus.setStatus("mandatory")
_WfivTrafficFilterCounter_Type = Counter32
_WfivTrafficFilterCounter_Object = MibTableColumn
wfivTrafficFilterCounter = _WfivTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 4),
    _WfivTrafficFilterCounter_Type()
)
wfivTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterCounter.setStatus("mandatory")
_WfivTrafficFilterDefinition_Type = Opaque
_WfivTrafficFilterDefinition_Object = MibTableColumn
wfivTrafficFilterDefinition = _WfivTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 5),
    _WfivTrafficFilterDefinition_Type()
)
wfivTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTrafficFilterDefinition.setStatus("mandatory")
_WfivTrafficFilterReserved_Type = Integer32
_WfivTrafficFilterReserved_Object = MibTableColumn
wfivTrafficFilterReserved = _WfivTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 6),
    _WfivTrafficFilterReserved_Type()
)
wfivTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterReserved.setStatus("mandatory")
_WfivTrafficFilterCircuit_Type = Integer32
_WfivTrafficFilterCircuit_Object = MibTableColumn
wfivTrafficFilterCircuit = _WfivTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 7),
    _WfivTrafficFilterCircuit_Type()
)
wfivTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterCircuit.setStatus("mandatory")
_WfivTrafficFilterRuleNumber_Type = Integer32
_WfivTrafficFilterRuleNumber_Object = MibTableColumn
wfivTrafficFilterRuleNumber = _WfivTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 8),
    _WfivTrafficFilterRuleNumber_Type()
)
wfivTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterRuleNumber.setStatus("mandatory")
_WfivTrafficFilterFragment_Type = Integer32
_WfivTrafficFilterFragment_Object = MibTableColumn
wfivTrafficFilterFragment = _WfivTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 9),
    _WfivTrafficFilterFragment_Type()
)
wfivTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivTrafficFilterFragment.setStatus("mandatory")
_WfivTrafficFilterName_Type = DisplayString
_WfivTrafficFilterName_Object = MibTableColumn
wfivTrafficFilterName = _WfivTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 6, 1, 10),
    _WfivTrafficFilterName_Type()
)
wfivTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivTrafficFilterName.setStatus("mandatory")
_WfivStaticAdjTable_Object = MibTable
wfivStaticAdjTable = _WfivStaticAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7)
)
if mibBuilder.loadTexts:
    wfivStaticAdjTable.setStatus("mandatory")
_WfivStaticAdjEntry_Object = MibTableRow
wfivStaticAdjEntry = _WfivStaticAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1)
)
wfivStaticAdjEntry.setIndexNames(
    (0, "Wellfleet-DECNET-MIB", "wfivStaticAdjCircuitID"),
    (0, "Wellfleet-DECNET-MIB", "wfivStaticAdjArea"),
    (0, "Wellfleet-DECNET-MIB", "wfivStaticAdjNodeid"),
)
if mibBuilder.loadTexts:
    wfivStaticAdjEntry.setStatus("mandatory")


class _WfivStaticAdjCreateDelete_Type(Integer32):
    """Custom type wfivStaticAdjCreateDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("delete", 2))
    )


_WfivStaticAdjCreateDelete_Type.__name__ = "Integer32"
_WfivStaticAdjCreateDelete_Object = MibTableColumn
wfivStaticAdjCreateDelete = _WfivStaticAdjCreateDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 1),
    _WfivStaticAdjCreateDelete_Type()
)
wfivStaticAdjCreateDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjCreateDelete.setStatus("mandatory")


class _WfivStaticAdjEnableDisable_Type(Integer32):
    """Custom type wfivStaticAdjEnableDisable based on Integer32"""
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


_WfivStaticAdjEnableDisable_Type.__name__ = "Integer32"
_WfivStaticAdjEnableDisable_Object = MibTableColumn
wfivStaticAdjEnableDisable = _WfivStaticAdjEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 2),
    _WfivStaticAdjEnableDisable_Type()
)
wfivStaticAdjEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjEnableDisable.setStatus("mandatory")
_WfivStaticAdjArea_Type = Integer32
_WfivStaticAdjArea_Object = MibTableColumn
wfivStaticAdjArea = _WfivStaticAdjArea_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 3),
    _WfivStaticAdjArea_Type()
)
wfivStaticAdjArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjArea.setStatus("mandatory")
_WfivStaticAdjNodeid_Type = Integer32
_WfivStaticAdjNodeid_Object = MibTableColumn
wfivStaticAdjNodeid = _WfivStaticAdjNodeid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 4),
    _WfivStaticAdjNodeid_Type()
)
wfivStaticAdjNodeid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjNodeid.setStatus("mandatory")
_WfivStaticAdjCircuitID_Type = Integer32
_WfivStaticAdjCircuitID_Object = MibTableColumn
wfivStaticAdjCircuitID = _WfivStaticAdjCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 5),
    _WfivStaticAdjCircuitID_Type()
)
wfivStaticAdjCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjCircuitID.setStatus("mandatory")
_WfivStaticAdjNodeAddr_Type = DisplayString
_WfivStaticAdjNodeAddr_Object = MibTableColumn
wfivStaticAdjNodeAddr = _WfivStaticAdjNodeAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 6),
    _WfivStaticAdjNodeAddr_Type()
)
wfivStaticAdjNodeAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticAdjNodeAddr.setStatus("mandatory")


class _WfivStaticAdjType_Type(Integer32):
    """Custom type wfivStaticAdjType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("area", 3),
          ("nonroutingiv", 5),
          ("routingiv", 4))
    )


_WfivStaticAdjType_Type.__name__ = "Integer32"
_WfivStaticAdjType_Object = MibTableColumn
wfivStaticAdjType = _WfivStaticAdjType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 7),
    _WfivStaticAdjType_Type()
)
wfivStaticAdjType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjType.setStatus("mandatory")
_WfivStaticAdjPriority_Type = Integer32
_WfivStaticAdjPriority_Object = MibTableColumn
wfivStaticAdjPriority = _WfivStaticAdjPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 8),
    _WfivStaticAdjPriority_Type()
)
wfivStaticAdjPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjPriority.setStatus("mandatory")
_WfivStaticAdjDestMACAddr_Type = OctetString
_WfivStaticAdjDestMACAddr_Object = MibTableColumn
wfivStaticAdjDestMACAddr = _WfivStaticAdjDestMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 7, 1, 9),
    _WfivStaticAdjDestMACAddr_Type()
)
wfivStaticAdjDestMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticAdjDestMACAddr.setStatus("mandatory")
_WfivStaticRouteTable_Object = MibTable
wfivStaticRouteTable = _WfivStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8)
)
if mibBuilder.loadTexts:
    wfivStaticRouteTable.setStatus("mandatory")
_WfivStaticRouteEntry_Object = MibTableRow
wfivStaticRouteEntry = _WfivStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1)
)
wfivStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-DECNET-MIB", "wfivStaticRouteAreaId"),
    (0, "Wellfleet-DECNET-MIB", "wfivStaticRouteNodeId"),
    (0, "Wellfleet-DECNET-MIB", "wfivStaticRouteNextHopAreaId"),
    (0, "Wellfleet-DECNET-MIB", "wfivStaticRouteNextHopNodeId"),
)
if mibBuilder.loadTexts:
    wfivStaticRouteEntry.setStatus("mandatory")


class _WfivStaticRouteDelete_Type(Integer32):
    """Custom type wfivStaticRouteDelete based on Integer32"""
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


_WfivStaticRouteDelete_Type.__name__ = "Integer32"
_WfivStaticRouteDelete_Object = MibTableColumn
wfivStaticRouteDelete = _WfivStaticRouteDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 1),
    _WfivStaticRouteDelete_Type()
)
wfivStaticRouteDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticRouteDelete.setStatus("mandatory")


class _WfivStaticRouteDisable_Type(Integer32):
    """Custom type wfivStaticRouteDisable based on Integer32"""
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


_WfivStaticRouteDisable_Type.__name__ = "Integer32"
_WfivStaticRouteDisable_Object = MibTableColumn
wfivStaticRouteDisable = _WfivStaticRouteDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 2),
    _WfivStaticRouteDisable_Type()
)
wfivStaticRouteDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticRouteDisable.setStatus("mandatory")


class _WfivStaticRouteType_Type(Integer32):
    """Custom type wfivStaticRouteType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("l1", 1),
          ("l2", 2))
    )


_WfivStaticRouteType_Type.__name__ = "Integer32"
_WfivStaticRouteType_Object = MibTableColumn
wfivStaticRouteType = _WfivStaticRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 3),
    _WfivStaticRouteType_Type()
)
wfivStaticRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticRouteType.setStatus("mandatory")
_WfivStaticRouteAreaId_Type = Integer32
_WfivStaticRouteAreaId_Object = MibTableColumn
wfivStaticRouteAreaId = _WfivStaticRouteAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 4),
    _WfivStaticRouteAreaId_Type()
)
wfivStaticRouteAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticRouteAreaId.setStatus("mandatory")
_WfivStaticRouteNodeId_Type = Integer32
_WfivStaticRouteNodeId_Object = MibTableColumn
wfivStaticRouteNodeId = _WfivStaticRouteNodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 5),
    _WfivStaticRouteNodeId_Type()
)
wfivStaticRouteNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticRouteNodeId.setStatus("mandatory")


class _WfivStaticRouteCost_Type(Integer32):
    """Custom type wfivStaticRouteCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_WfivStaticRouteCost_Type.__name__ = "Integer32"
_WfivStaticRouteCost_Object = MibTableColumn
wfivStaticRouteCost = _WfivStaticRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 6),
    _WfivStaticRouteCost_Type()
)
wfivStaticRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfivStaticRouteCost.setStatus("mandatory")
_WfivStaticRouteNextHopAreaId_Type = Integer32
_WfivStaticRouteNextHopAreaId_Object = MibTableColumn
wfivStaticRouteNextHopAreaId = _WfivStaticRouteNextHopAreaId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 7),
    _WfivStaticRouteNextHopAreaId_Type()
)
wfivStaticRouteNextHopAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticRouteNextHopAreaId.setStatus("mandatory")
_WfivStaticRouteNextHopNodeId_Type = Integer32
_WfivStaticRouteNextHopNodeId_Object = MibTableColumn
wfivStaticRouteNextHopNodeId = _WfivStaticRouteNextHopNodeId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 8, 1, 8),
    _WfivStaticRouteNextHopNodeId_Type()
)
wfivStaticRouteNextHopNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivStaticRouteNextHopNodeId.setStatus("mandatory")
_WfivDecnetTrans_ObjectIdentity = ObjectIdentity
wfivDecnetTrans = _WfivDecnetTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 9)
)
_WfivDecnetTransPhase5Pkts_Type = Counter32
_WfivDecnetTransPhase5Pkts_Object = MibScalar
wfivDecnetTransPhase5Pkts = _WfivDecnetTransPhase5Pkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 9, 1),
    _WfivDecnetTransPhase5Pkts_Type()
)
wfivDecnetTransPhase5Pkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivDecnetTransPhase5Pkts.setStatus("mandatory")
_WfivDecnetTransMtuFail_Type = Counter32
_WfivDecnetTransMtuFail_Object = MibScalar
wfivDecnetTransMtuFail = _WfivDecnetTransMtuFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 9, 2),
    _WfivDecnetTransMtuFail_Type()
)
wfivDecnetTransMtuFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivDecnetTransMtuFail.setStatus("mandatory")
_WfivDecnetTransUnrFail_Type = Counter32
_WfivDecnetTransUnrFail_Object = MibScalar
wfivDecnetTransUnrFail = _WfivDecnetTransUnrFail_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 9, 3),
    _WfivDecnetTransUnrFail_Type()
)
wfivDecnetTransUnrFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivDecnetTransUnrFail.setStatus("mandatory")
_WfivDecnetTransNumPhase5Es_Type = Counter32
_WfivDecnetTransNumPhase5Es_Object = MibScalar
wfivDecnetTransNumPhase5Es = _WfivDecnetTransNumPhase5Es_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 9, 4),
    _WfivDecnetTransNumPhase5Es_Type()
)
wfivDecnetTransNumPhase5Es.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivDecnetTransNumPhase5Es.setStatus("mandatory")
_WfivAggrStats_ObjectIdentity = ObjectIdentity
wfivAggrStats = _WfivAggrStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10)
)
_WfivAggrInPkts_Type = Counter32
_WfivAggrInPkts_Object = MibScalar
wfivAggrInPkts = _WfivAggrInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 1),
    _WfivAggrInPkts_Type()
)
wfivAggrInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrInPkts.setStatus("mandatory")
_WfivAggrOutPkts_Type = Counter32
_WfivAggrOutPkts_Object = MibScalar
wfivAggrOutPkts = _WfivAggrOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 2),
    _WfivAggrOutPkts_Type()
)
wfivAggrOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrOutPkts.setStatus("mandatory")
_WfivAggrFormatErrs_Type = Counter32
_WfivAggrFormatErrs_Object = MibScalar
wfivAggrFormatErrs = _WfivAggrFormatErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 3),
    _WfivAggrFormatErrs_Type()
)
wfivAggrFormatErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrFormatErrs.setStatus("mandatory")
_WfivAggrDestUnreachables_Type = Counter32
_WfivAggrDestUnreachables_Object = MibScalar
wfivAggrDestUnreachables = _WfivAggrDestUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 4),
    _WfivAggrDestUnreachables_Type()
)
wfivAggrDestUnreachables.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrDestUnreachables.setStatus("mandatory")
_WfivAggrRangeErrs_Type = Counter32
_WfivAggrRangeErrs_Object = MibScalar
wfivAggrRangeErrs = _WfivAggrRangeErrs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 5),
    _WfivAggrRangeErrs_Type()
)
wfivAggrRangeErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrRangeErrs.setStatus("mandatory")
_WfivAggrOversizedPkts_Type = Counter32
_WfivAggrOversizedPkts_Object = MibScalar
wfivAggrOversizedPkts = _WfivAggrOversizedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 6),
    _WfivAggrOversizedPkts_Type()
)
wfivAggrOversizedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrOversizedPkts.setStatus("mandatory")
_WfivAggrAgedPkts_Type = Counter32
_WfivAggrAgedPkts_Object = MibScalar
wfivAggrAgedPkts = _WfivAggrAgedPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 7),
    _WfivAggrAgedPkts_Type()
)
wfivAggrAgedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrAgedPkts.setStatus("mandatory")
_WfivAggrFwdPkts_Type = Counter32
_WfivAggrFwdPkts_Object = MibScalar
wfivAggrFwdPkts = _WfivAggrFwdPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 2, 10, 8),
    _WfivAggrFwdPkts_Type()
)
wfivAggrFwdPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfivAggrFwdPkts.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DECNET-MIB",
    **{"wfivRouteGroup": wfivRouteGroup,
       "wfivRouteCreateDelete": wfivRouteCreateDelete,
       "wfivRouteEnableDisable": wfivRouteEnableDisable,
       "wfivRouteState": wfivRouteState,
       "wfivRouteBroadcastRouteTimer": wfivRouteBroadcastRouteTimer,
       "wfivRouteRoutingVers": wfivRouteRoutingVers,
       "wfivRouteMaxAddr": wfivRouteMaxAddr,
       "wfivRouteMaxBdcastNonRouters": wfivRouteMaxBdcastNonRouters,
       "wfivRouteMaxBdcastRouters": wfivRouteMaxBdcastRouters,
       "wfivRouteMaxCircuits": wfivRouteMaxCircuits,
       "wfivRouteMaxCost": wfivRouteMaxCost,
       "wfivRouteMaxHops": wfivRouteMaxHops,
       "wfivRouteMaxVisits": wfivRouteMaxVisits,
       "wfivRouteAreaMaxCost": wfivRouteAreaMaxCost,
       "wfivRouteAreaMaxHops": wfivRouteAreaMaxHops,
       "wfivRouteMaxArea": wfivRouteMaxArea,
       "wfivRouteType": wfivRouteType,
       "wfivRouteNumAdjs": wfivRouteNumAdjs,
       "wfivRouteNumLvl1Rts": wfivRouteNumLvl1Rts,
       "wfivRouteNumAreas": wfivRouteNumAreas,
       "wfivRouteLevel1Area": wfivRouteLevel1Area,
       "wfivTriggeredUpdates": wfivTriggeredUpdates,
       "wfivTriggeredInterval": wfivTriggeredInterval,
       "wfivCircuitTable": wfivCircuitTable,
       "wfivCircuitEntry": wfivCircuitEntry,
       "wfivCircuitCreateDelete": wfivCircuitCreateDelete,
       "wfivCircuitEnableDisable": wfivCircuitEnableDisable,
       "wfivCircuitCommonState": wfivCircuitCommonState,
       "wfivCircuitArea": wfivCircuitArea,
       "wfivCircuitNodeid": wfivCircuitNodeid,
       "wfivCircuitNodeAddr": wfivCircuitNodeAddr,
       "wfivCircuitID": wfivCircuitID,
       "wfivCircuitCommonType": wfivCircuitCommonType,
       "wfivCircuitExecCost": wfivCircuitExecCost,
       "wfivCircuitExecHelloTimer": wfivCircuitExecHelloTimer,
       "wfivCircuitDesigRouterNodeAddr": wfivCircuitDesigRouterNodeAddr,
       "wfivCircuitMaxRouters": wfivCircuitMaxRouters,
       "wfivCircuitRouterPri": wfivCircuitRouterPri,
       "wfivCircuitCountAgedPktLoss": wfivCircuitCountAgedPktLoss,
       "wfivCircuitCountNodeUnrPktLoss": wfivCircuitCountNodeUnrPktLoss,
       "wfivCircuitCountOutRngePktLoss": wfivCircuitCountOutRngePktLoss,
       "wfivCircuitCountOverSzePktLoss": wfivCircuitCountOverSzePktLoss,
       "wfivCircuitCountPacketFmtErr": wfivCircuitCountPacketFmtErr,
       "wfivCircuitCountPtlRteUpdtLoss": wfivCircuitCountPtlRteUpdtLoss,
       "wfivCircuitCountTransitPksRecd": wfivCircuitCountTransitPksRecd,
       "wfivCircuitCountTransitPkSent": wfivCircuitCountTransitPkSent,
       "wfivCircuitCountRtHelloSent": wfivCircuitCountRtHelloSent,
       "wfivCircuitCountRtHelloRcvd": wfivCircuitCountRtHelloRcvd,
       "wfivCircuitCountHelloSent": wfivCircuitCountHelloSent,
       "wfivCircuitCountHelloRcvd": wfivCircuitCountHelloRcvd,
       "wfivCircuitCountL1UpdSent": wfivCircuitCountL1UpdSent,
       "wfivCircuitCountL1UpdRcvd": wfivCircuitCountL1UpdRcvd,
       "wfivCircuitCountAreaUpdSent": wfivCircuitCountAreaUpdSent,
       "wfivCircuitCountAreaUpdRcvd": wfivCircuitCountAreaUpdRcvd,
       "wfivCircuitCountDropped": wfivCircuitCountDropped,
       "wfivCircuitAllEndnodesMac": wfivCircuitAllEndnodesMac,
       "wfivCircuitAllRoutersMac": wfivCircuitAllRoutersMac,
       "wfivCircuitAllAreaRoutersMac": wfivCircuitAllAreaRoutersMac,
       "wfivCircuitHelloEnableDisable": wfivCircuitHelloEnableDisable,
       "wfivCircuitRtHelloEnableDisable": wfivCircuitRtHelloEnableDisable,
       "wfivCircuitL1UpdateEnableDisable": wfivCircuitL1UpdateEnableDisable,
       "wfivCircuitAllEndnodesMacInUse": wfivCircuitAllEndnodesMacInUse,
       "wfivCircuitAllRoutersMacInUse": wfivCircuitAllRoutersMacInUse,
       "wfivCircuitAllAreaRoutersMacInUse": wfivCircuitAllAreaRoutersMacInUse,
       "wfivCircuitL2UpdateDisable": wfivCircuitL2UpdateDisable,
       "wfivCircuitLevel": wfivCircuitLevel,
       "wfivLevel1RouteTable": wfivLevel1RouteTable,
       "wfivLevel1RouteEntry": wfivLevel1RouteEntry,
       "wfivLevel1AreaId": wfivLevel1AreaId,
       "wfivLevel1NodeId": wfivLevel1NodeId,
       "wfivLevel1RouteNodeAddr": wfivLevel1RouteNodeAddr,
       "wfivLevel1RouteCircuitID": wfivLevel1RouteCircuitID,
       "wfivLevel1RouteCost": wfivLevel1RouteCost,
       "wfivLevel1RouteHops": wfivLevel1RouteHops,
       "wfivLevel1RouteNextNode": wfivLevel1RouteNextNode,
       "wfivLevel1RouteDynamic": wfivLevel1RouteDynamic,
       "wfivAreaTable": wfivAreaTable,
       "wfivAreaEntry": wfivAreaEntry,
       "wfivAreaNum": wfivAreaNum,
       "wfivAreaState": wfivAreaState,
       "wfivAreaCost": wfivAreaCost,
       "wfivAreaHops": wfivAreaHops,
       "wfivAreaCircuitID": wfivAreaCircuitID,
       "wfivAreaNextNode": wfivAreaNextNode,
       "wfivAreaRouteDynamic": wfivAreaRouteDynamic,
       "wfivAdjTable": wfivAdjTable,
       "wfivAdjEntry": wfivAdjEntry,
       "wfivAdjIndex": wfivAdjIndex,
       "wfivAdjNodeAddr": wfivAdjNodeAddr,
       "wfivAdjBlockSize": wfivAdjBlockSize,
       "wfivAdjListenTimer": wfivAdjListenTimer,
       "wfivAdjCircuitID": wfivAdjCircuitID,
       "wfivAdjType": wfivAdjType,
       "wfivAdjState": wfivAdjState,
       "wfivAdjPriority": wfivAdjPriority,
       "wfivAdjClass": wfivAdjClass,
       "wfivTrafficFilterTable": wfivTrafficFilterTable,
       "wfivTrafficFilterEntry": wfivTrafficFilterEntry,
       "wfivTrafficFilterCreate": wfivTrafficFilterCreate,
       "wfivTrafficFilterEnable": wfivTrafficFilterEnable,
       "wfivTrafficFilterStatus": wfivTrafficFilterStatus,
       "wfivTrafficFilterCounter": wfivTrafficFilterCounter,
       "wfivTrafficFilterDefinition": wfivTrafficFilterDefinition,
       "wfivTrafficFilterReserved": wfivTrafficFilterReserved,
       "wfivTrafficFilterCircuit": wfivTrafficFilterCircuit,
       "wfivTrafficFilterRuleNumber": wfivTrafficFilterRuleNumber,
       "wfivTrafficFilterFragment": wfivTrafficFilterFragment,
       "wfivTrafficFilterName": wfivTrafficFilterName,
       "wfivStaticAdjTable": wfivStaticAdjTable,
       "wfivStaticAdjEntry": wfivStaticAdjEntry,
       "wfivStaticAdjCreateDelete": wfivStaticAdjCreateDelete,
       "wfivStaticAdjEnableDisable": wfivStaticAdjEnableDisable,
       "wfivStaticAdjArea": wfivStaticAdjArea,
       "wfivStaticAdjNodeid": wfivStaticAdjNodeid,
       "wfivStaticAdjCircuitID": wfivStaticAdjCircuitID,
       "wfivStaticAdjNodeAddr": wfivStaticAdjNodeAddr,
       "wfivStaticAdjType": wfivStaticAdjType,
       "wfivStaticAdjPriority": wfivStaticAdjPriority,
       "wfivStaticAdjDestMACAddr": wfivStaticAdjDestMACAddr,
       "wfivStaticRouteTable": wfivStaticRouteTable,
       "wfivStaticRouteEntry": wfivStaticRouteEntry,
       "wfivStaticRouteDelete": wfivStaticRouteDelete,
       "wfivStaticRouteDisable": wfivStaticRouteDisable,
       "wfivStaticRouteType": wfivStaticRouteType,
       "wfivStaticRouteAreaId": wfivStaticRouteAreaId,
       "wfivStaticRouteNodeId": wfivStaticRouteNodeId,
       "wfivStaticRouteCost": wfivStaticRouteCost,
       "wfivStaticRouteNextHopAreaId": wfivStaticRouteNextHopAreaId,
       "wfivStaticRouteNextHopNodeId": wfivStaticRouteNextHopNodeId,
       "wfivDecnetTrans": wfivDecnetTrans,
       "wfivDecnetTransPhase5Pkts": wfivDecnetTransPhase5Pkts,
       "wfivDecnetTransMtuFail": wfivDecnetTransMtuFail,
       "wfivDecnetTransUnrFail": wfivDecnetTransUnrFail,
       "wfivDecnetTransNumPhase5Es": wfivDecnetTransNumPhase5Es,
       "wfivAggrStats": wfivAggrStats,
       "wfivAggrInPkts": wfivAggrInPkts,
       "wfivAggrOutPkts": wfivAggrOutPkts,
       "wfivAggrFormatErrs": wfivAggrFormatErrs,
       "wfivAggrDestUnreachables": wfivAggrDestUnreachables,
       "wfivAggrRangeErrs": wfivAggrRangeErrs,
       "wfivAggrOversizedPkts": wfivAggrOversizedPkts,
       "wfivAggrAgedPkts": wfivAggrAgedPkts,
       "wfivAggrFwdPkts": wfivAggrFwdPkts}
)
