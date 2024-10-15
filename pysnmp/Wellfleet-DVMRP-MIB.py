# SNMP MIB module (Wellfleet-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:09 2024
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

(wfDvmrpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDvmrpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDvmrpBase_ObjectIdentity = ObjectIdentity
wfDvmrpBase = _WfDvmrpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1)
)


class _WfDvmrpBaseCreate_Type(Integer32):
    """Custom type wfDvmrpBaseCreate based on Integer32"""
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


_WfDvmrpBaseCreate_Type.__name__ = "Integer32"
_WfDvmrpBaseCreate_Object = MibScalar
wfDvmrpBaseCreate = _WfDvmrpBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 1),
    _WfDvmrpBaseCreate_Type()
)
wfDvmrpBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseCreate.setStatus("mandatory")


class _WfDvmrpBaseEnable_Type(Integer32):
    """Custom type wfDvmrpBaseEnable based on Integer32"""
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


_WfDvmrpBaseEnable_Type.__name__ = "Integer32"
_WfDvmrpBaseEnable_Object = MibScalar
wfDvmrpBaseEnable = _WfDvmrpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 2),
    _WfDvmrpBaseEnable_Type()
)
wfDvmrpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseEnable.setStatus("mandatory")


class _WfDvmrpBaseState_Type(Integer32):
    """Custom type wfDvmrpBaseState based on Integer32"""
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
          ("notpres", 4),
          ("up", 1))
    )


_WfDvmrpBaseState_Type.__name__ = "Integer32"
_WfDvmrpBaseState_Object = MibScalar
wfDvmrpBaseState = _WfDvmrpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 3),
    _WfDvmrpBaseState_Type()
)
wfDvmrpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpBaseState.setStatus("mandatory")


class _WfDvmrpBaseFullUpdateInterval_Type(Integer32):
    """Custom type wfDvmrpBaseFullUpdateInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_WfDvmrpBaseFullUpdateInterval_Type.__name__ = "Integer32"
_WfDvmrpBaseFullUpdateInterval_Object = MibScalar
wfDvmrpBaseFullUpdateInterval = _WfDvmrpBaseFullUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 4),
    _WfDvmrpBaseFullUpdateInterval_Type()
)
wfDvmrpBaseFullUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseFullUpdateInterval.setStatus("mandatory")


class _WfDvmrpBaseTriggeredUpdateInterval_Type(Integer32):
    """Custom type wfDvmrpBaseTriggeredUpdateInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1000),
    )


_WfDvmrpBaseTriggeredUpdateInterval_Type.__name__ = "Integer32"
_WfDvmrpBaseTriggeredUpdateInterval_Object = MibScalar
wfDvmrpBaseTriggeredUpdateInterval = _WfDvmrpBaseTriggeredUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 5),
    _WfDvmrpBaseTriggeredUpdateInterval_Type()
)
wfDvmrpBaseTriggeredUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseTriggeredUpdateInterval.setStatus("mandatory")


class _WfDvmrpBaseLeafTimeout_Type(Integer32):
    """Custom type wfDvmrpBaseLeafTimeout based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(25, 4000),
    )


_WfDvmrpBaseLeafTimeout_Type.__name__ = "Integer32"
_WfDvmrpBaseLeafTimeout_Object = MibScalar
wfDvmrpBaseLeafTimeout = _WfDvmrpBaseLeafTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 6),
    _WfDvmrpBaseLeafTimeout_Type()
)
wfDvmrpBaseLeafTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseLeafTimeout.setStatus("mandatory")


class _WfDvmrpBaseNeighborTimeout_Type(Integer32):
    """Custom type wfDvmrpBaseNeighborTimeout based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(35, 8000),
    )


_WfDvmrpBaseNeighborTimeout_Type.__name__ = "Integer32"
_WfDvmrpBaseNeighborTimeout_Object = MibScalar
wfDvmrpBaseNeighborTimeout = _WfDvmrpBaseNeighborTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 7),
    _WfDvmrpBaseNeighborTimeout_Type()
)
wfDvmrpBaseNeighborTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseNeighborTimeout.setStatus("mandatory")


class _WfDvmrpBaseRouteExpirationTimeout_Type(Integer32):
    """Custom type wfDvmrpBaseRouteExpirationTimeout based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4000),
    )


_WfDvmrpBaseRouteExpirationTimeout_Type.__name__ = "Integer32"
_WfDvmrpBaseRouteExpirationTimeout_Object = MibScalar
wfDvmrpBaseRouteExpirationTimeout = _WfDvmrpBaseRouteExpirationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 8),
    _WfDvmrpBaseRouteExpirationTimeout_Type()
)
wfDvmrpBaseRouteExpirationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseRouteExpirationTimeout.setStatus("mandatory")


class _WfDvmrpBaseGarbageTimeout_Type(Integer32):
    """Custom type wfDvmrpBaseGarbageTimeout based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 8000),
    )


_WfDvmrpBaseGarbageTimeout_Type.__name__ = "Integer32"
_WfDvmrpBaseGarbageTimeout_Object = MibScalar
wfDvmrpBaseGarbageTimeout = _WfDvmrpBaseGarbageTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 9),
    _WfDvmrpBaseGarbageTimeout_Type()
)
wfDvmrpBaseGarbageTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseGarbageTimeout.setStatus("mandatory")


class _WfDvmrpBaseEstimatedRoutes_Type(Integer32):
    """Custom type wfDvmrpBaseEstimatedRoutes based on Integer32"""
    defaultValue = 25

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2147483647),
    )


_WfDvmrpBaseEstimatedRoutes_Type.__name__ = "Integer32"
_WfDvmrpBaseEstimatedRoutes_Object = MibScalar
wfDvmrpBaseEstimatedRoutes = _WfDvmrpBaseEstimatedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 10),
    _WfDvmrpBaseEstimatedRoutes_Type()
)
wfDvmrpBaseEstimatedRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseEstimatedRoutes.setStatus("mandatory")


class _WfDvmrpBaseNeighborProbeInterval_Type(Integer32):
    """Custom type wfDvmrpBaseNeighborProbeInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_WfDvmrpBaseNeighborProbeInterval_Type.__name__ = "Integer32"
_WfDvmrpBaseNeighborProbeInterval_Object = MibScalar
wfDvmrpBaseNeighborProbeInterval = _WfDvmrpBaseNeighborProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 11),
    _WfDvmrpBaseNeighborProbeInterval_Type()
)
wfDvmrpBaseNeighborProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseNeighborProbeInterval.setStatus("mandatory")


class _WfDvmrpBaseRouteSwitchTimeout_Type(Integer32):
    """Custom type wfDvmrpBaseRouteSwitchTimeout based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 2000),
    )


_WfDvmrpBaseRouteSwitchTimeout_Type.__name__ = "Integer32"
_WfDvmrpBaseRouteSwitchTimeout_Object = MibScalar
wfDvmrpBaseRouteSwitchTimeout = _WfDvmrpBaseRouteSwitchTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 12),
    _WfDvmrpBaseRouteSwitchTimeout_Type()
)
wfDvmrpBaseRouteSwitchTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseRouteSwitchTimeout.setStatus("mandatory")
_WfDvmrpBaseActualRoutes_Type = Integer32
_WfDvmrpBaseActualRoutes_Object = MibScalar
wfDvmrpBaseActualRoutes = _WfDvmrpBaseActualRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 13),
    _WfDvmrpBaseActualRoutes_Type()
)
wfDvmrpBaseActualRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpBaseActualRoutes.setStatus("mandatory")


class _WfDvmrpBaseDebugLevel_Type(Gauge32):
    """Custom type wfDvmrpBaseDebugLevel based on Gauge32"""
    defaultValue = 1

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfDvmrpBaseDebugLevel_Type.__name__ = "Gauge32"
_WfDvmrpBaseDebugLevel_Object = MibScalar
wfDvmrpBaseDebugLevel = _WfDvmrpBaseDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 14),
    _WfDvmrpBaseDebugLevel_Type()
)
wfDvmrpBaseDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseDebugLevel.setStatus("mandatory")


class _WfDvmrpBasePruningEnable_Type(Integer32):
    """Custom type wfDvmrpBasePruningEnable based on Integer32"""
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


_WfDvmrpBasePruningEnable_Type.__name__ = "Integer32"
_WfDvmrpBasePruningEnable_Object = MibScalar
wfDvmrpBasePruningEnable = _WfDvmrpBasePruningEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 15),
    _WfDvmrpBasePruningEnable_Type()
)
wfDvmrpBasePruningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBasePruningEnable.setStatus("mandatory")


class _WfDvmrpBaseFragmentMtuThreshold_Type(Integer32):
    """Custom type wfDvmrpBaseFragmentMtuThreshold based on Integer32"""
    defaultValue = 1514

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(910, 2147483647),
    )


_WfDvmrpBaseFragmentMtuThreshold_Type.__name__ = "Integer32"
_WfDvmrpBaseFragmentMtuThreshold_Object = MibScalar
wfDvmrpBaseFragmentMtuThreshold = _WfDvmrpBaseFragmentMtuThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 16),
    _WfDvmrpBaseFragmentMtuThreshold_Type()
)
wfDvmrpBaseFragmentMtuThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseFragmentMtuThreshold.setStatus("obsolete")
_WfDvmrpBaseMaxRoutes_Type = Integer32
_WfDvmrpBaseMaxRoutes_Object = MibScalar
wfDvmrpBaseMaxRoutes = _WfDvmrpBaseMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 17),
    _WfDvmrpBaseMaxRoutes_Type()
)
wfDvmrpBaseMaxRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseMaxRoutes.setStatus("mandatory")


class _WfDvmrpBasePolicyEnable_Type(Integer32):
    """Custom type wfDvmrpBasePolicyEnable based on Integer32"""
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


_WfDvmrpBasePolicyEnable_Type.__name__ = "Integer32"
_WfDvmrpBasePolicyEnable_Object = MibScalar
wfDvmrpBasePolicyEnable = _WfDvmrpBasePolicyEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 18),
    _WfDvmrpBasePolicyEnable_Type()
)
wfDvmrpBasePolicyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBasePolicyEnable.setStatus("obsolete")


class _WfDvmrpBaseHolddownEnable_Type(Integer32):
    """Custom type wfDvmrpBaseHolddownEnable based on Integer32"""
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


_WfDvmrpBaseHolddownEnable_Type.__name__ = "Integer32"
_WfDvmrpBaseHolddownEnable_Object = MibScalar
wfDvmrpBaseHolddownEnable = _WfDvmrpBaseHolddownEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 1, 19),
    _WfDvmrpBaseHolddownEnable_Type()
)
wfDvmrpBaseHolddownEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpBaseHolddownEnable.setStatus("mandatory")
_WfDvmrpCircuitEntryTable_Object = MibTable
wfDvmrpCircuitEntryTable = _WfDvmrpCircuitEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2)
)
if mibBuilder.loadTexts:
    wfDvmrpCircuitEntryTable.setStatus("mandatory")
_WfDvmrpCircuitEntry_Object = MibTableRow
wfDvmrpCircuitEntry = _WfDvmrpCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1)
)
wfDvmrpCircuitEntry.setIndexNames(
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpCircuitCCT"),
)
if mibBuilder.loadTexts:
    wfDvmrpCircuitEntry.setStatus("mandatory")


class _WfDvmrpCircuitCreate_Type(Integer32):
    """Custom type wfDvmrpCircuitCreate based on Integer32"""
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


_WfDvmrpCircuitCreate_Type.__name__ = "Integer32"
_WfDvmrpCircuitCreate_Object = MibTableColumn
wfDvmrpCircuitCreate = _WfDvmrpCircuitCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 1),
    _WfDvmrpCircuitCreate_Type()
)
wfDvmrpCircuitCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitCreate.setStatus("mandatory")


class _WfDvmrpCircuitEnable_Type(Integer32):
    """Custom type wfDvmrpCircuitEnable based on Integer32"""
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


_WfDvmrpCircuitEnable_Type.__name__ = "Integer32"
_WfDvmrpCircuitEnable_Object = MibTableColumn
wfDvmrpCircuitEnable = _WfDvmrpCircuitEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 2),
    _WfDvmrpCircuitEnable_Type()
)
wfDvmrpCircuitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitEnable.setStatus("mandatory")


class _WfDvmrpCircuitState_Type(Integer32):
    """Custom type wfDvmrpCircuitState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfDvmrpCircuitState_Type.__name__ = "Integer32"
_WfDvmrpCircuitState_Object = MibTableColumn
wfDvmrpCircuitState = _WfDvmrpCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 3),
    _WfDvmrpCircuitState_Type()
)
wfDvmrpCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitState.setStatus("mandatory")
_WfDvmrpCircuitCCT_Type = Integer32
_WfDvmrpCircuitCCT_Object = MibTableColumn
wfDvmrpCircuitCCT = _WfDvmrpCircuitCCT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 4),
    _WfDvmrpCircuitCCT_Type()
)
wfDvmrpCircuitCCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitCCT.setStatus("mandatory")


class _WfDvmrpCircuitRouteEnable_Type(Integer32):
    """Custom type wfDvmrpCircuitRouteEnable based on Integer32"""
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


_WfDvmrpCircuitRouteEnable_Type.__name__ = "Integer32"
_WfDvmrpCircuitRouteEnable_Object = MibTableColumn
wfDvmrpCircuitRouteEnable = _WfDvmrpCircuitRouteEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 5),
    _WfDvmrpCircuitRouteEnable_Type()
)
wfDvmrpCircuitRouteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitRouteEnable.setStatus("mandatory")


class _WfDvmrpCircuitMetric_Type(Integer32):
    """Custom type wfDvmrpCircuitMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WfDvmrpCircuitMetric_Type.__name__ = "Integer32"
_WfDvmrpCircuitMetric_Object = MibTableColumn
wfDvmrpCircuitMetric = _WfDvmrpCircuitMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 6),
    _WfDvmrpCircuitMetric_Type()
)
wfDvmrpCircuitMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitMetric.setStatus("mandatory")


class _WfDvmrpCircuitRouteThreshold_Type(Integer32):
    """Custom type wfDvmrpCircuitRouteThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfDvmrpCircuitRouteThreshold_Type.__name__ = "Integer32"
_WfDvmrpCircuitRouteThreshold_Object = MibTableColumn
wfDvmrpCircuitRouteThreshold = _WfDvmrpCircuitRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 7),
    _WfDvmrpCircuitRouteThreshold_Type()
)
wfDvmrpCircuitRouteThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitRouteThreshold.setStatus("mandatory")
_WfDvmrpCircuitInPkts_Type = Counter32
_WfDvmrpCircuitInPkts_Object = MibTableColumn
wfDvmrpCircuitInPkts = _WfDvmrpCircuitInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 8),
    _WfDvmrpCircuitInPkts_Type()
)
wfDvmrpCircuitInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitInPkts.setStatus("mandatory")
_WfDvmrpCircuitOutPkts_Type = Counter32
_WfDvmrpCircuitOutPkts_Object = MibTableColumn
wfDvmrpCircuitOutPkts = _WfDvmrpCircuitOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 9),
    _WfDvmrpCircuitOutPkts_Type()
)
wfDvmrpCircuitOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitOutPkts.setStatus("mandatory")
_WfDvmrpCircuitInRouteUpdates_Type = Counter32
_WfDvmrpCircuitInRouteUpdates_Object = MibTableColumn
wfDvmrpCircuitInRouteUpdates = _WfDvmrpCircuitInRouteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 10),
    _WfDvmrpCircuitInRouteUpdates_Type()
)
wfDvmrpCircuitInRouteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitInRouteUpdates.setStatus("mandatory")
_WfDvmrpCircuitOutRouteUpdates_Type = Counter32
_WfDvmrpCircuitOutRouteUpdates_Object = MibTableColumn
wfDvmrpCircuitOutRouteUpdates = _WfDvmrpCircuitOutRouteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 11),
    _WfDvmrpCircuitOutRouteUpdates_Type()
)
wfDvmrpCircuitOutRouteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitOutRouteUpdates.setStatus("mandatory")
_WfDvmrpCircuitInPktDiscards_Type = Counter32
_WfDvmrpCircuitInPktDiscards_Object = MibTableColumn
wfDvmrpCircuitInPktDiscards = _WfDvmrpCircuitInPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 12),
    _WfDvmrpCircuitInPktDiscards_Type()
)
wfDvmrpCircuitInPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitInPktDiscards.setStatus("mandatory")
_WfDvmrpCircuitOutPktDiscards_Type = Counter32
_WfDvmrpCircuitOutPktDiscards_Object = MibTableColumn
wfDvmrpCircuitOutPktDiscards = _WfDvmrpCircuitOutPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 13),
    _WfDvmrpCircuitOutPktDiscards_Type()
)
wfDvmrpCircuitOutPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitOutPktDiscards.setStatus("mandatory")


class _WfDvmrpCircuitFwdCacheSize_Type(Integer32):
    """Custom type wfDvmrpCircuitFwdCacheSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 512),
    )


_WfDvmrpCircuitFwdCacheSize_Type.__name__ = "Integer32"
_WfDvmrpCircuitFwdCacheSize_Object = MibTableColumn
wfDvmrpCircuitFwdCacheSize = _WfDvmrpCircuitFwdCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 14),
    _WfDvmrpCircuitFwdCacheSize_Type()
)
wfDvmrpCircuitFwdCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitFwdCacheSize.setStatus("mandatory")


class _WfDvmrpCircuitFwdCacheTTL_Type(Integer32):
    """Custom type wfDvmrpCircuitFwdCacheTTL based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfDvmrpCircuitFwdCacheTTL_Type.__name__ = "Integer32"
_WfDvmrpCircuitFwdCacheTTL_Object = MibTableColumn
wfDvmrpCircuitFwdCacheTTL = _WfDvmrpCircuitFwdCacheTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 15),
    _WfDvmrpCircuitFwdCacheTTL_Type()
)
wfDvmrpCircuitFwdCacheTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitFwdCacheTTL.setStatus("mandatory")


class _WfDvmrpCircuitAdvertiseSelf_Type(Integer32):
    """Custom type wfDvmrpCircuitAdvertiseSelf based on Integer32"""
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


_WfDvmrpCircuitAdvertiseSelf_Type.__name__ = "Integer32"
_WfDvmrpCircuitAdvertiseSelf_Object = MibTableColumn
wfDvmrpCircuitAdvertiseSelf = _WfDvmrpCircuitAdvertiseSelf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 16),
    _WfDvmrpCircuitAdvertiseSelf_Type()
)
wfDvmrpCircuitAdvertiseSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitAdvertiseSelf.setStatus("mandatory")
_WfDvmrpCircuitFwdCacheEntries_Type = Integer32
_WfDvmrpCircuitFwdCacheEntries_Object = MibTableColumn
wfDvmrpCircuitFwdCacheEntries = _WfDvmrpCircuitFwdCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 17),
    _WfDvmrpCircuitFwdCacheEntries_Type()
)
wfDvmrpCircuitFwdCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitFwdCacheEntries.setStatus("mandatory")
_WfDvmrpCircuitInPrunePkts_Type = Counter32
_WfDvmrpCircuitInPrunePkts_Object = MibTableColumn
wfDvmrpCircuitInPrunePkts = _WfDvmrpCircuitInPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 18),
    _WfDvmrpCircuitInPrunePkts_Type()
)
wfDvmrpCircuitInPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitInPrunePkts.setStatus("mandatory")
_WfDvmrpCircuitOutPrunePkts_Type = Counter32
_WfDvmrpCircuitOutPrunePkts_Object = MibTableColumn
wfDvmrpCircuitOutPrunePkts = _WfDvmrpCircuitOutPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 19),
    _WfDvmrpCircuitOutPrunePkts_Type()
)
wfDvmrpCircuitOutPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitOutPrunePkts.setStatus("mandatory")
_WfDvmrpCircuitInGraftPkts_Type = Counter32
_WfDvmrpCircuitInGraftPkts_Object = MibTableColumn
wfDvmrpCircuitInGraftPkts = _WfDvmrpCircuitInGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 20),
    _WfDvmrpCircuitInGraftPkts_Type()
)
wfDvmrpCircuitInGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitInGraftPkts.setStatus("mandatory")
_WfDvmrpCircuitOutGraftPkts_Type = Counter32
_WfDvmrpCircuitOutGraftPkts_Object = MibTableColumn
wfDvmrpCircuitOutGraftPkts = _WfDvmrpCircuitOutGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 21),
    _WfDvmrpCircuitOutGraftPkts_Type()
)
wfDvmrpCircuitOutGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitOutGraftPkts.setStatus("mandatory")
_WfDvmrpCircuitInGraftAckPkts_Type = Counter32
_WfDvmrpCircuitInGraftAckPkts_Object = MibTableColumn
wfDvmrpCircuitInGraftAckPkts = _WfDvmrpCircuitInGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 22),
    _WfDvmrpCircuitInGraftAckPkts_Type()
)
wfDvmrpCircuitInGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitInGraftAckPkts.setStatus("mandatory")
_WfDvmrpCircuitOutGraftAckPkts_Type = Counter32
_WfDvmrpCircuitOutGraftAckPkts_Object = MibTableColumn
wfDvmrpCircuitOutGraftAckPkts = _WfDvmrpCircuitOutGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 23),
    _WfDvmrpCircuitOutGraftAckPkts_Type()
)
wfDvmrpCircuitOutGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitOutGraftAckPkts.setStatus("mandatory")


class _WfDvmrpCircuitDefaultRouteSupply_Type(Integer32):
    """Custom type wfDvmrpCircuitDefaultRouteSupply based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("generate", 3))
    )


_WfDvmrpCircuitDefaultRouteSupply_Type.__name__ = "Integer32"
_WfDvmrpCircuitDefaultRouteSupply_Object = MibTableColumn
wfDvmrpCircuitDefaultRouteSupply = _WfDvmrpCircuitDefaultRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 24),
    _WfDvmrpCircuitDefaultRouteSupply_Type()
)
wfDvmrpCircuitDefaultRouteSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitDefaultRouteSupply.setStatus("mandatory")


class _WfDvmrpCircuitDefaultRouteListen_Type(Integer32):
    """Custom type wfDvmrpCircuitDefaultRouteListen based on Integer32"""
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


_WfDvmrpCircuitDefaultRouteListen_Type.__name__ = "Integer32"
_WfDvmrpCircuitDefaultRouteListen_Object = MibTableColumn
wfDvmrpCircuitDefaultRouteListen = _WfDvmrpCircuitDefaultRouteListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 25),
    _WfDvmrpCircuitDefaultRouteListen_Type()
)
wfDvmrpCircuitDefaultRouteListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitDefaultRouteListen.setStatus("mandatory")


class _WfDvmrpCircuitReportDependProbe_Type(Integer32):
    """Custom type wfDvmrpCircuitReportDependProbe based on Integer32"""
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


_WfDvmrpCircuitReportDependProbe_Type.__name__ = "Integer32"
_WfDvmrpCircuitReportDependProbe_Object = MibTableColumn
wfDvmrpCircuitReportDependProbe = _WfDvmrpCircuitReportDependProbe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 26),
    _WfDvmrpCircuitReportDependProbe_Type()
)
wfDvmrpCircuitReportDependProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitReportDependProbe.setStatus("mandatory")


class _WfDvmrpCircuitPruneLifeTime_Type(Integer32):
    """Custom type wfDvmrpCircuitPruneLifeTime based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfDvmrpCircuitPruneLifeTime_Type.__name__ = "Integer32"
_WfDvmrpCircuitPruneLifeTime_Object = MibTableColumn
wfDvmrpCircuitPruneLifeTime = _WfDvmrpCircuitPruneLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 27),
    _WfDvmrpCircuitPruneLifeTime_Type()
)
wfDvmrpCircuitPruneLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpCircuitPruneLifeTime.setStatus("mandatory")
_WfDvmrpCircuitAcceptAggregateRoutes_Type = Integer32
_WfDvmrpCircuitAcceptAggregateRoutes_Object = MibTableColumn
wfDvmrpCircuitAcceptAggregateRoutes = _WfDvmrpCircuitAcceptAggregateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 28),
    _WfDvmrpCircuitAcceptAggregateRoutes_Type()
)
wfDvmrpCircuitAcceptAggregateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitAcceptAggregateRoutes.setStatus("mandatory")
_WfDvmrpCircuitAnnounceAggregatedRoutes_Type = Integer32
_WfDvmrpCircuitAnnounceAggregatedRoutes_Object = MibTableColumn
wfDvmrpCircuitAnnounceAggregatedRoutes = _WfDvmrpCircuitAnnounceAggregatedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 2, 1, 29),
    _WfDvmrpCircuitAnnounceAggregatedRoutes_Type()
)
wfDvmrpCircuitAnnounceAggregatedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpCircuitAnnounceAggregatedRoutes.setStatus("mandatory")
_WfDvmrpTunnelEntryTable_Object = MibTable
wfDvmrpTunnelEntryTable = _WfDvmrpTunnelEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3)
)
if mibBuilder.loadTexts:
    wfDvmrpTunnelEntryTable.setStatus("mandatory")
_WfDvmrpTunnelEntry_Object = MibTableRow
wfDvmrpTunnelEntry = _WfDvmrpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1)
)
wfDvmrpTunnelEntry.setIndexNames(
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpTunnelCCT"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpTunnelLocalRouterIpAddress"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpTunnelRemoteRouterIpAddress"),
)
if mibBuilder.loadTexts:
    wfDvmrpTunnelEntry.setStatus("mandatory")


class _WfDvmrpTunnelCreate_Type(Integer32):
    """Custom type wfDvmrpTunnelCreate based on Integer32"""
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


_WfDvmrpTunnelCreate_Type.__name__ = "Integer32"
_WfDvmrpTunnelCreate_Object = MibTableColumn
wfDvmrpTunnelCreate = _WfDvmrpTunnelCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 1),
    _WfDvmrpTunnelCreate_Type()
)
wfDvmrpTunnelCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelCreate.setStatus("mandatory")


class _WfDvmrpTunnelEnable_Type(Integer32):
    """Custom type wfDvmrpTunnelEnable based on Integer32"""
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


_WfDvmrpTunnelEnable_Type.__name__ = "Integer32"
_WfDvmrpTunnelEnable_Object = MibTableColumn
wfDvmrpTunnelEnable = _WfDvmrpTunnelEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 2),
    _WfDvmrpTunnelEnable_Type()
)
wfDvmrpTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelEnable.setStatus("mandatory")


class _WfDvmrpTunnelState_Type(Integer32):
    """Custom type wfDvmrpTunnelState based on Integer32"""
    defaultValue = 5

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
        *(("down", 2),
          ("init", 3),
          ("invalid", 4),
          ("notpres", 5),
          ("up", 1))
    )


_WfDvmrpTunnelState_Type.__name__ = "Integer32"
_WfDvmrpTunnelState_Object = MibTableColumn
wfDvmrpTunnelState = _WfDvmrpTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 3),
    _WfDvmrpTunnelState_Type()
)
wfDvmrpTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelState.setStatus("mandatory")
_WfDvmrpTunnelCCT_Type = Integer32
_WfDvmrpTunnelCCT_Object = MibTableColumn
wfDvmrpTunnelCCT = _WfDvmrpTunnelCCT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 4),
    _WfDvmrpTunnelCCT_Type()
)
wfDvmrpTunnelCCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelCCT.setStatus("mandatory")
_WfDvmrpTunnelRemoteRouterIpAddress_Type = IpAddress
_WfDvmrpTunnelRemoteRouterIpAddress_Object = MibTableColumn
wfDvmrpTunnelRemoteRouterIpAddress = _WfDvmrpTunnelRemoteRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 5),
    _WfDvmrpTunnelRemoteRouterIpAddress_Type()
)
wfDvmrpTunnelRemoteRouterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelRemoteRouterIpAddress.setStatus("mandatory")


class _WfDvmrpTunnelEncapsMode_Type(Integer32):
    """Custom type wfDvmrpTunnelEncapsMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip-in-ip", 1),
          ("lssr", 2))
    )


_WfDvmrpTunnelEncapsMode_Type.__name__ = "Integer32"
_WfDvmrpTunnelEncapsMode_Object = MibTableColumn
wfDvmrpTunnelEncapsMode = _WfDvmrpTunnelEncapsMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 6),
    _WfDvmrpTunnelEncapsMode_Type()
)
wfDvmrpTunnelEncapsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelEncapsMode.setStatus("mandatory")


class _WfDvmrpTunnelMetric_Type(Integer32):
    """Custom type wfDvmrpTunnelMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_WfDvmrpTunnelMetric_Type.__name__ = "Integer32"
_WfDvmrpTunnelMetric_Object = MibTableColumn
wfDvmrpTunnelMetric = _WfDvmrpTunnelMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 7),
    _WfDvmrpTunnelMetric_Type()
)
wfDvmrpTunnelMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelMetric.setStatus("mandatory")


class _WfDvmrpTunnelThreshold_Type(Integer32):
    """Custom type wfDvmrpTunnelThreshold based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_WfDvmrpTunnelThreshold_Type.__name__ = "Integer32"
_WfDvmrpTunnelThreshold_Object = MibTableColumn
wfDvmrpTunnelThreshold = _WfDvmrpTunnelThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 8),
    _WfDvmrpTunnelThreshold_Type()
)
wfDvmrpTunnelThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelThreshold.setStatus("mandatory")
_WfDvmrpTunnelInPkts_Type = Counter32
_WfDvmrpTunnelInPkts_Object = MibTableColumn
wfDvmrpTunnelInPkts = _WfDvmrpTunnelInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 9),
    _WfDvmrpTunnelInPkts_Type()
)
wfDvmrpTunnelInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelInPkts.setStatus("mandatory")
_WfDvmrpTunnelOutPkts_Type = Counter32
_WfDvmrpTunnelOutPkts_Object = MibTableColumn
wfDvmrpTunnelOutPkts = _WfDvmrpTunnelOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 10),
    _WfDvmrpTunnelOutPkts_Type()
)
wfDvmrpTunnelOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelOutPkts.setStatus("mandatory")
_WfDvmrpTunnelInRouteUpdates_Type = Counter32
_WfDvmrpTunnelInRouteUpdates_Object = MibTableColumn
wfDvmrpTunnelInRouteUpdates = _WfDvmrpTunnelInRouteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 11),
    _WfDvmrpTunnelInRouteUpdates_Type()
)
wfDvmrpTunnelInRouteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelInRouteUpdates.setStatus("mandatory")
_WfDvmrpTunnelOutRouteUpdates_Type = Counter32
_WfDvmrpTunnelOutRouteUpdates_Object = MibTableColumn
wfDvmrpTunnelOutRouteUpdates = _WfDvmrpTunnelOutRouteUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 12),
    _WfDvmrpTunnelOutRouteUpdates_Type()
)
wfDvmrpTunnelOutRouteUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelOutRouteUpdates.setStatus("mandatory")
_WfDvmrpTunnelInPktDiscards_Type = Counter32
_WfDvmrpTunnelInPktDiscards_Object = MibTableColumn
wfDvmrpTunnelInPktDiscards = _WfDvmrpTunnelInPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 13),
    _WfDvmrpTunnelInPktDiscards_Type()
)
wfDvmrpTunnelInPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelInPktDiscards.setStatus("mandatory")
_WfDvmrpTunnelOutPktDiscards_Type = Counter32
_WfDvmrpTunnelOutPktDiscards_Object = MibTableColumn
wfDvmrpTunnelOutPktDiscards = _WfDvmrpTunnelOutPktDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 14),
    _WfDvmrpTunnelOutPktDiscards_Type()
)
wfDvmrpTunnelOutPktDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelOutPktDiscards.setStatus("mandatory")
_WfDvmrpTunnelLocalRouterIpAddress_Type = IpAddress
_WfDvmrpTunnelLocalRouterIpAddress_Object = MibTableColumn
wfDvmrpTunnelLocalRouterIpAddress = _WfDvmrpTunnelLocalRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 15),
    _WfDvmrpTunnelLocalRouterIpAddress_Type()
)
wfDvmrpTunnelLocalRouterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelLocalRouterIpAddress.setStatus("mandatory")


class _WfDvmrpTunnelFwdCacheSize_Type(Integer32):
    """Custom type wfDvmrpTunnelFwdCacheSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 512),
    )


_WfDvmrpTunnelFwdCacheSize_Type.__name__ = "Integer32"
_WfDvmrpTunnelFwdCacheSize_Object = MibTableColumn
wfDvmrpTunnelFwdCacheSize = _WfDvmrpTunnelFwdCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 16),
    _WfDvmrpTunnelFwdCacheSize_Type()
)
wfDvmrpTunnelFwdCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelFwdCacheSize.setStatus("mandatory")


class _WfDvmrpTunnelFwdCacheTTL_Type(Integer32):
    """Custom type wfDvmrpTunnelFwdCacheTTL based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfDvmrpTunnelFwdCacheTTL_Type.__name__ = "Integer32"
_WfDvmrpTunnelFwdCacheTTL_Object = MibTableColumn
wfDvmrpTunnelFwdCacheTTL = _WfDvmrpTunnelFwdCacheTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 17),
    _WfDvmrpTunnelFwdCacheTTL_Type()
)
wfDvmrpTunnelFwdCacheTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelFwdCacheTTL.setStatus("mandatory")
_WfDvmrpTunnelFwdCacheEntries_Type = Integer32
_WfDvmrpTunnelFwdCacheEntries_Object = MibTableColumn
wfDvmrpTunnelFwdCacheEntries = _WfDvmrpTunnelFwdCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 18),
    _WfDvmrpTunnelFwdCacheEntries_Type()
)
wfDvmrpTunnelFwdCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelFwdCacheEntries.setStatus("mandatory")
_WfDvmrpTunnelInPrunePkts_Type = Counter32
_WfDvmrpTunnelInPrunePkts_Object = MibTableColumn
wfDvmrpTunnelInPrunePkts = _WfDvmrpTunnelInPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 19),
    _WfDvmrpTunnelInPrunePkts_Type()
)
wfDvmrpTunnelInPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelInPrunePkts.setStatus("mandatory")
_WfDvmrpTunnelOutPrunePkts_Type = Counter32
_WfDvmrpTunnelOutPrunePkts_Object = MibTableColumn
wfDvmrpTunnelOutPrunePkts = _WfDvmrpTunnelOutPrunePkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 20),
    _WfDvmrpTunnelOutPrunePkts_Type()
)
wfDvmrpTunnelOutPrunePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelOutPrunePkts.setStatus("mandatory")
_WfDvmrpTunnelInGraftPkts_Type = Counter32
_WfDvmrpTunnelInGraftPkts_Object = MibTableColumn
wfDvmrpTunnelInGraftPkts = _WfDvmrpTunnelInGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 21),
    _WfDvmrpTunnelInGraftPkts_Type()
)
wfDvmrpTunnelInGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelInGraftPkts.setStatus("mandatory")
_WfDvmrpTunnelOutGraftPkts_Type = Counter32
_WfDvmrpTunnelOutGraftPkts_Object = MibTableColumn
wfDvmrpTunnelOutGraftPkts = _WfDvmrpTunnelOutGraftPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 22),
    _WfDvmrpTunnelOutGraftPkts_Type()
)
wfDvmrpTunnelOutGraftPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelOutGraftPkts.setStatus("mandatory")
_WfDvmrpTunnelInGraftAckPkts_Type = Counter32
_WfDvmrpTunnelInGraftAckPkts_Object = MibTableColumn
wfDvmrpTunnelInGraftAckPkts = _WfDvmrpTunnelInGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 23),
    _WfDvmrpTunnelInGraftAckPkts_Type()
)
wfDvmrpTunnelInGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelInGraftAckPkts.setStatus("mandatory")
_WfDvmrpTunnelOutGraftAckPkts_Type = Counter32
_WfDvmrpTunnelOutGraftAckPkts_Object = MibTableColumn
wfDvmrpTunnelOutGraftAckPkts = _WfDvmrpTunnelOutGraftAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 24),
    _WfDvmrpTunnelOutGraftAckPkts_Type()
)
wfDvmrpTunnelOutGraftAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelOutGraftAckPkts.setStatus("mandatory")


class _WfDvmrpTunnelDefaultRouteSupply_Type(Integer32):
    """Custom type wfDvmrpTunnelDefaultRouteSupply based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("generate", 3))
    )


_WfDvmrpTunnelDefaultRouteSupply_Type.__name__ = "Integer32"
_WfDvmrpTunnelDefaultRouteSupply_Object = MibTableColumn
wfDvmrpTunnelDefaultRouteSupply = _WfDvmrpTunnelDefaultRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 25),
    _WfDvmrpTunnelDefaultRouteSupply_Type()
)
wfDvmrpTunnelDefaultRouteSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelDefaultRouteSupply.setStatus("mandatory")


class _WfDvmrpTunnelDefaultRouteListen_Type(Integer32):
    """Custom type wfDvmrpTunnelDefaultRouteListen based on Integer32"""
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


_WfDvmrpTunnelDefaultRouteListen_Type.__name__ = "Integer32"
_WfDvmrpTunnelDefaultRouteListen_Object = MibTableColumn
wfDvmrpTunnelDefaultRouteListen = _WfDvmrpTunnelDefaultRouteListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 26),
    _WfDvmrpTunnelDefaultRouteListen_Type()
)
wfDvmrpTunnelDefaultRouteListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelDefaultRouteListen.setStatus("mandatory")


class _WfDvmrpTunnelCtrlMsgMode_Type(Integer32):
    """Custom type wfDvmrpTunnelCtrlMsgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip-in-ip", 2),
          ("native", 1))
    )


_WfDvmrpTunnelCtrlMsgMode_Type.__name__ = "Integer32"
_WfDvmrpTunnelCtrlMsgMode_Object = MibTableColumn
wfDvmrpTunnelCtrlMsgMode = _WfDvmrpTunnelCtrlMsgMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 27),
    _WfDvmrpTunnelCtrlMsgMode_Type()
)
wfDvmrpTunnelCtrlMsgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelCtrlMsgMode.setStatus("mandatory")


class _WfDvmrpTunnelReportDependProbe_Type(Integer32):
    """Custom type wfDvmrpTunnelReportDependProbe based on Integer32"""
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


_WfDvmrpTunnelReportDependProbe_Type.__name__ = "Integer32"
_WfDvmrpTunnelReportDependProbe_Object = MibTableColumn
wfDvmrpTunnelReportDependProbe = _WfDvmrpTunnelReportDependProbe_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 28),
    _WfDvmrpTunnelReportDependProbe_Type()
)
wfDvmrpTunnelReportDependProbe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelReportDependProbe.setStatus("mandatory")


class _WfDvmrpTunnelPruneLifeTime_Type(Integer32):
    """Custom type wfDvmrpTunnelPruneLifeTime based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfDvmrpTunnelPruneLifeTime_Type.__name__ = "Integer32"
_WfDvmrpTunnelPruneLifeTime_Object = MibTableColumn
wfDvmrpTunnelPruneLifeTime = _WfDvmrpTunnelPruneLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 29),
    _WfDvmrpTunnelPruneLifeTime_Type()
)
wfDvmrpTunnelPruneLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDvmrpTunnelPruneLifeTime.setStatus("mandatory")
_WfDvmrpTunnelAcceptAggregateRoutes_Type = Integer32
_WfDvmrpTunnelAcceptAggregateRoutes_Object = MibTableColumn
wfDvmrpTunnelAcceptAggregateRoutes = _WfDvmrpTunnelAcceptAggregateRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 30),
    _WfDvmrpTunnelAcceptAggregateRoutes_Type()
)
wfDvmrpTunnelAcceptAggregateRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelAcceptAggregateRoutes.setStatus("mandatory")
_WfDvmrpTunnelAnnounceAggregatedRoutes_Type = Integer32
_WfDvmrpTunnelAnnounceAggregatedRoutes_Object = MibTableColumn
wfDvmrpTunnelAnnounceAggregatedRoutes = _WfDvmrpTunnelAnnounceAggregatedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 3, 1, 31),
    _WfDvmrpTunnelAnnounceAggregatedRoutes_Type()
)
wfDvmrpTunnelAnnounceAggregatedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpTunnelAnnounceAggregatedRoutes.setStatus("mandatory")
_WfDvmrpRouteEntryTable_Object = MibTable
wfDvmrpRouteEntryTable = _WfDvmrpRouteEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4)
)
if mibBuilder.loadTexts:
    wfDvmrpRouteEntryTable.setStatus("mandatory")
_WfDvmrpRouteEntry_Object = MibTableRow
wfDvmrpRouteEntry = _WfDvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1)
)
wfDvmrpRouteEntry.setIndexNames(
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpRouteSourceNetwork"),
)
if mibBuilder.loadTexts:
    wfDvmrpRouteEntry.setStatus("mandatory")
_WfDvmrpRouteSourceNetwork_Type = IpAddress
_WfDvmrpRouteSourceNetwork_Object = MibTableColumn
wfDvmrpRouteSourceNetwork = _WfDvmrpRouteSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 1),
    _WfDvmrpRouteSourceNetwork_Type()
)
wfDvmrpRouteSourceNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteSourceNetwork.setStatus("mandatory")
_WfDvmrpRouteSourceMask_Type = IpAddress
_WfDvmrpRouteSourceMask_Object = MibTableColumn
wfDvmrpRouteSourceMask = _WfDvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 2),
    _WfDvmrpRouteSourceMask_Type()
)
wfDvmrpRouteSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteSourceMask.setStatus("mandatory")
_WfDvmrpRouteNextHopRouter_Type = IpAddress
_WfDvmrpRouteNextHopRouter_Object = MibTableColumn
wfDvmrpRouteNextHopRouter = _WfDvmrpRouteNextHopRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 3),
    _WfDvmrpRouteNextHopRouter_Type()
)
wfDvmrpRouteNextHopRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteNextHopRouter.setStatus("mandatory")
_WfDvmrpRouteNextHopInterfaceCCT_Type = Integer32
_WfDvmrpRouteNextHopInterfaceCCT_Object = MibTableColumn
wfDvmrpRouteNextHopInterfaceCCT = _WfDvmrpRouteNextHopInterfaceCCT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 4),
    _WfDvmrpRouteNextHopInterfaceCCT_Type()
)
wfDvmrpRouteNextHopInterfaceCCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteNextHopInterfaceCCT.setStatus("mandatory")
_WfDvmrpRouteNextHopInterfaceTunnelId_Type = IpAddress
_WfDvmrpRouteNextHopInterfaceTunnelId_Object = MibTableColumn
wfDvmrpRouteNextHopInterfaceTunnelId = _WfDvmrpRouteNextHopInterfaceTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 5),
    _WfDvmrpRouteNextHopInterfaceTunnelId_Type()
)
wfDvmrpRouteNextHopInterfaceTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteNextHopInterfaceTunnelId.setStatus("mandatory")
_WfDvmrpRouteNextHopInterfaceLocalTunnelId_Type = IpAddress
_WfDvmrpRouteNextHopInterfaceLocalTunnelId_Object = MibTableColumn
wfDvmrpRouteNextHopInterfaceLocalTunnelId = _WfDvmrpRouteNextHopInterfaceLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 6),
    _WfDvmrpRouteNextHopInterfaceLocalTunnelId_Type()
)
wfDvmrpRouteNextHopInterfaceLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteNextHopInterfaceLocalTunnelId.setStatus("mandatory")
_WfDvmrpRouteTimer_Type = Integer32
_WfDvmrpRouteTimer_Object = MibTableColumn
wfDvmrpRouteTimer = _WfDvmrpRouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 7),
    _WfDvmrpRouteTimer_Type()
)
wfDvmrpRouteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteTimer.setStatus("mandatory")
_WfDvmrpRouteState_Type = Integer32
_WfDvmrpRouteState_Object = MibTableColumn
wfDvmrpRouteState = _WfDvmrpRouteState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 8),
    _WfDvmrpRouteState_Type()
)
wfDvmrpRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteState.setStatus("mandatory")
_WfDvmrpRouteMetric_Type = Integer32
_WfDvmrpRouteMetric_Object = MibTableColumn
wfDvmrpRouteMetric = _WfDvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 9),
    _WfDvmrpRouteMetric_Type()
)
wfDvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteMetric.setStatus("mandatory")
_WfDvmrpRouteProtocol_Type = Integer32
_WfDvmrpRouteProtocol_Object = MibTableColumn
wfDvmrpRouteProtocol = _WfDvmrpRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 10),
    _WfDvmrpRouteProtocol_Type()
)
wfDvmrpRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteProtocol.setStatus("mandatory")
_WfDvmrpRouteType_Type = Integer32
_WfDvmrpRouteType_Object = MibTableColumn
wfDvmrpRouteType = _WfDvmrpRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 11),
    _WfDvmrpRouteType_Type()
)
wfDvmrpRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteType.setStatus("mandatory")
_WfDvmrpRouteAggregatedType_Type = Integer32
_WfDvmrpRouteAggregatedType_Object = MibTableColumn
wfDvmrpRouteAggregatedType = _WfDvmrpRouteAggregatedType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 4, 1, 12),
    _WfDvmrpRouteAggregatedType_Type()
)
wfDvmrpRouteAggregatedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteAggregatedType.setStatus("mandatory")
_WfDvmrpRouteInterfaceEntryTable_Object = MibTable
wfDvmrpRouteInterfaceEntryTable = _WfDvmrpRouteInterfaceEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5)
)
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceEntryTable.setStatus("mandatory")
_WfDvmrpRouteInterfaceEntry_Object = MibTableRow
wfDvmrpRouteInterfaceEntry = _WfDvmrpRouteInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1)
)
wfDvmrpRouteInterfaceEntry.setIndexNames(
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpRouteInterfaceSourceNetwork"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpRouteInterfaceParentCCT"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpRouteInterfaceParentLocalTunnelId"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpRouteInterfaceParentTunnelId"),
)
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceEntry.setStatus("mandatory")
_WfDvmrpRouteInterfaceSourceNetwork_Type = IpAddress
_WfDvmrpRouteInterfaceSourceNetwork_Object = MibTableColumn
wfDvmrpRouteInterfaceSourceNetwork = _WfDvmrpRouteInterfaceSourceNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 1),
    _WfDvmrpRouteInterfaceSourceNetwork_Type()
)
wfDvmrpRouteInterfaceSourceNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceSourceNetwork.setStatus("mandatory")
_WfDvmrpRouteInterfaceSourceMask_Type = IpAddress
_WfDvmrpRouteInterfaceSourceMask_Object = MibTableColumn
wfDvmrpRouteInterfaceSourceMask = _WfDvmrpRouteInterfaceSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 2),
    _WfDvmrpRouteInterfaceSourceMask_Type()
)
wfDvmrpRouteInterfaceSourceMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceSourceMask.setStatus("mandatory")
_WfDvmrpRouteInterfaceNextHopInterfaceCCT_Type = Integer32
_WfDvmrpRouteInterfaceNextHopInterfaceCCT_Object = MibTableColumn
wfDvmrpRouteInterfaceNextHopInterfaceCCT = _WfDvmrpRouteInterfaceNextHopInterfaceCCT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 3),
    _WfDvmrpRouteInterfaceNextHopInterfaceCCT_Type()
)
wfDvmrpRouteInterfaceNextHopInterfaceCCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceNextHopInterfaceCCT.setStatus("mandatory")
_WfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId_Type = IpAddress
_WfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId_Object = MibTableColumn
wfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId = _WfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 4),
    _WfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId_Type()
)
wfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId.setStatus("mandatory")
_WfDvmrpRouteInterfaceNextHopInterfaceTunnelId_Type = IpAddress
_WfDvmrpRouteInterfaceNextHopInterfaceTunnelId_Object = MibTableColumn
wfDvmrpRouteInterfaceNextHopInterfaceTunnelId = _WfDvmrpRouteInterfaceNextHopInterfaceTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 5),
    _WfDvmrpRouteInterfaceNextHopInterfaceTunnelId_Type()
)
wfDvmrpRouteInterfaceNextHopInterfaceTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceNextHopInterfaceTunnelId.setStatus("mandatory")
_WfDvmrpRouteInterfaceState_Type = Integer32
_WfDvmrpRouteInterfaceState_Object = MibTableColumn
wfDvmrpRouteInterfaceState = _WfDvmrpRouteInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 6),
    _WfDvmrpRouteInterfaceState_Type()
)
wfDvmrpRouteInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceState.setStatus("mandatory")
_WfDvmrpRouteInterfaceDominantRouter_Type = IpAddress
_WfDvmrpRouteInterfaceDominantRouter_Object = MibTableColumn
wfDvmrpRouteInterfaceDominantRouter = _WfDvmrpRouteInterfaceDominantRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 7),
    _WfDvmrpRouteInterfaceDominantRouter_Type()
)
wfDvmrpRouteInterfaceDominantRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceDominantRouter.setStatus("mandatory")
_WfDvmrpRouteInterfaceSubordinateRouter_Type = IpAddress
_WfDvmrpRouteInterfaceSubordinateRouter_Object = MibTableColumn
wfDvmrpRouteInterfaceSubordinateRouter = _WfDvmrpRouteInterfaceSubordinateRouter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 8),
    _WfDvmrpRouteInterfaceSubordinateRouter_Type()
)
wfDvmrpRouteInterfaceSubordinateRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceSubordinateRouter.setStatus("mandatory")
_WfDvmrpRouteInterfaceHoldDownTimer_Type = Integer32
_WfDvmrpRouteInterfaceHoldDownTimer_Object = MibTableColumn
wfDvmrpRouteInterfaceHoldDownTimer = _WfDvmrpRouteInterfaceHoldDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 9),
    _WfDvmrpRouteInterfaceHoldDownTimer_Type()
)
wfDvmrpRouteInterfaceHoldDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceHoldDownTimer.setStatus("mandatory")
_WfDvmrpRouteInterfaceSPInDiscards_Type = Counter32
_WfDvmrpRouteInterfaceSPInDiscards_Object = MibTableColumn
wfDvmrpRouteInterfaceSPInDiscards = _WfDvmrpRouteInterfaceSPInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 10),
    _WfDvmrpRouteInterfaceSPInDiscards_Type()
)
wfDvmrpRouteInterfaceSPInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceSPInDiscards.setStatus("obsolete")
_WfDvmrpRouteInterfaceSPOutDiscards_Type = Counter32
_WfDvmrpRouteInterfaceSPOutDiscards_Object = MibTableColumn
wfDvmrpRouteInterfaceSPOutDiscards = _WfDvmrpRouteInterfaceSPOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 11),
    _WfDvmrpRouteInterfaceSPOutDiscards_Type()
)
wfDvmrpRouteInterfaceSPOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceSPOutDiscards.setStatus("obsolete")
_WfDvmrpRouteInterfaceThresholdOutDiscards_Type = Counter32
_WfDvmrpRouteInterfaceThresholdOutDiscards_Object = MibTableColumn
wfDvmrpRouteInterfaceThresholdOutDiscards = _WfDvmrpRouteInterfaceThresholdOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 12),
    _WfDvmrpRouteInterfaceThresholdOutDiscards_Type()
)
wfDvmrpRouteInterfaceThresholdOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceThresholdOutDiscards.setStatus("obsolete")
_WfDvmrpRouteInterfaceInSuccessfulPkts_Type = Counter32
_WfDvmrpRouteInterfaceInSuccessfulPkts_Object = MibTableColumn
wfDvmrpRouteInterfaceInSuccessfulPkts = _WfDvmrpRouteInterfaceInSuccessfulPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 13),
    _WfDvmrpRouteInterfaceInSuccessfulPkts_Type()
)
wfDvmrpRouteInterfaceInSuccessfulPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceInSuccessfulPkts.setStatus("obsolete")
_WfDvmrpRouteInterfaceOutSuccessfulPkts_Type = Counter32
_WfDvmrpRouteInterfaceOutSuccessfulPkts_Object = MibTableColumn
wfDvmrpRouteInterfaceOutSuccessfulPkts = _WfDvmrpRouteInterfaceOutSuccessfulPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 14),
    _WfDvmrpRouteInterfaceOutSuccessfulPkts_Type()
)
wfDvmrpRouteInterfaceOutSuccessfulPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceOutSuccessfulPkts.setStatus("obsolete")
_WfDvmrpRouteInterfaceParentCCT_Type = Integer32
_WfDvmrpRouteInterfaceParentCCT_Object = MibTableColumn
wfDvmrpRouteInterfaceParentCCT = _WfDvmrpRouteInterfaceParentCCT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 15),
    _WfDvmrpRouteInterfaceParentCCT_Type()
)
wfDvmrpRouteInterfaceParentCCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceParentCCT.setStatus("mandatory")
_WfDvmrpRouteInterfaceParentLocalTunnelId_Type = IpAddress
_WfDvmrpRouteInterfaceParentLocalTunnelId_Object = MibTableColumn
wfDvmrpRouteInterfaceParentLocalTunnelId = _WfDvmrpRouteInterfaceParentLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 16),
    _WfDvmrpRouteInterfaceParentLocalTunnelId_Type()
)
wfDvmrpRouteInterfaceParentLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceParentLocalTunnelId.setStatus("mandatory")
_WfDvmrpRouteInterfaceParentTunnelId_Type = IpAddress
_WfDvmrpRouteInterfaceParentTunnelId_Object = MibTableColumn
wfDvmrpRouteInterfaceParentTunnelId = _WfDvmrpRouteInterfaceParentTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 5, 1, 17),
    _WfDvmrpRouteInterfaceParentTunnelId_Type()
)
wfDvmrpRouteInterfaceParentTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpRouteInterfaceParentTunnelId.setStatus("mandatory")
_WfDvmrpNeighboringRouterEntryTable_Object = MibTable
wfDvmrpNeighboringRouterEntryTable = _WfDvmrpNeighboringRouterEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6)
)
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterEntryTable.setStatus("mandatory")
_WfDvmrpNeighboringRouterEntry_Object = MibTableRow
wfDvmrpNeighboringRouterEntry = _WfDvmrpNeighboringRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1)
)
wfDvmrpNeighboringRouterEntry.setIndexNames(
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpNeighboringRouterCCT"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpNeighboringRouterLocalTunnelId"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpNeighboringRouterTunnelId"),
    (0, "Wellfleet-DVMRP-MIB", "wfDvmrpNeighboringRouterIpAddr"),
)
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterEntry.setStatus("mandatory")
_WfDvmrpNeighboringRouterCCT_Type = Integer32
_WfDvmrpNeighboringRouterCCT_Object = MibTableColumn
wfDvmrpNeighboringRouterCCT = _WfDvmrpNeighboringRouterCCT_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 1),
    _WfDvmrpNeighboringRouterCCT_Type()
)
wfDvmrpNeighboringRouterCCT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterCCT.setStatus("mandatory")
_WfDvmrpNeighboringRouterLocalTunnelId_Type = IpAddress
_WfDvmrpNeighboringRouterLocalTunnelId_Object = MibTableColumn
wfDvmrpNeighboringRouterLocalTunnelId = _WfDvmrpNeighboringRouterLocalTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 2),
    _WfDvmrpNeighboringRouterLocalTunnelId_Type()
)
wfDvmrpNeighboringRouterLocalTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterLocalTunnelId.setStatus("mandatory")
_WfDvmrpNeighboringRouterTunnelId_Type = IpAddress
_WfDvmrpNeighboringRouterTunnelId_Object = MibTableColumn
wfDvmrpNeighboringRouterTunnelId = _WfDvmrpNeighboringRouterTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 3),
    _WfDvmrpNeighboringRouterTunnelId_Type()
)
wfDvmrpNeighboringRouterTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterTunnelId.setStatus("mandatory")
_WfDvmrpNeighboringRouterIpAddr_Type = IpAddress
_WfDvmrpNeighboringRouterIpAddr_Object = MibTableColumn
wfDvmrpNeighboringRouterIpAddr = _WfDvmrpNeighboringRouterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 4),
    _WfDvmrpNeighboringRouterIpAddr_Type()
)
wfDvmrpNeighboringRouterIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterIpAddr.setStatus("mandatory")
_WfDvmrpNeighboringRouterState_Type = Integer32
_WfDvmrpNeighboringRouterState_Object = MibTableColumn
wfDvmrpNeighboringRouterState = _WfDvmrpNeighboringRouterState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 5),
    _WfDvmrpNeighboringRouterState_Type()
)
wfDvmrpNeighboringRouterState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterState.setStatus("mandatory")
_WfDvmrpNeighboringRouterTimer_Type = Integer32
_WfDvmrpNeighboringRouterTimer_Object = MibTableColumn
wfDvmrpNeighboringRouterTimer = _WfDvmrpNeighboringRouterTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 6),
    _WfDvmrpNeighboringRouterTimer_Type()
)
wfDvmrpNeighboringRouterTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterTimer.setStatus("mandatory")
_WfDvmrpNeighboringRouterGenId_Type = Integer32
_WfDvmrpNeighboringRouterGenId_Object = MibTableColumn
wfDvmrpNeighboringRouterGenId = _WfDvmrpNeighboringRouterGenId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 7),
    _WfDvmrpNeighboringRouterGenId_Type()
)
wfDvmrpNeighboringRouterGenId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterGenId.setStatus("mandatory")


class _WfDvmrpNeighboringRouterMajorVersion_Type(Integer32):
    """Custom type wfDvmrpNeighboringRouterMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfDvmrpNeighboringRouterMajorVersion_Type.__name__ = "Integer32"
_WfDvmrpNeighboringRouterMajorVersion_Object = MibTableColumn
wfDvmrpNeighboringRouterMajorVersion = _WfDvmrpNeighboringRouterMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 8),
    _WfDvmrpNeighboringRouterMajorVersion_Type()
)
wfDvmrpNeighboringRouterMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterMajorVersion.setStatus("mandatory")


class _WfDvmrpNeighboringRouterMinorVersion_Type(Integer32):
    """Custom type wfDvmrpNeighboringRouterMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfDvmrpNeighboringRouterMinorVersion_Type.__name__ = "Integer32"
_WfDvmrpNeighboringRouterMinorVersion_Object = MibTableColumn
wfDvmrpNeighboringRouterMinorVersion = _WfDvmrpNeighboringRouterMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 9),
    _WfDvmrpNeighboringRouterMinorVersion_Type()
)
wfDvmrpNeighboringRouterMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterMinorVersion.setStatus("mandatory")
_WfDvmrpNeighboringRouterCapabilities_Type = Integer32
_WfDvmrpNeighboringRouterCapabilities_Object = MibTableColumn
wfDvmrpNeighboringRouterCapabilities = _WfDvmrpNeighboringRouterCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 12, 6, 1, 10),
    _WfDvmrpNeighboringRouterCapabilities_Type()
)
wfDvmrpNeighboringRouterCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDvmrpNeighboringRouterCapabilities.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DVMRP-MIB",
    **{"wfDvmrpBase": wfDvmrpBase,
       "wfDvmrpBaseCreate": wfDvmrpBaseCreate,
       "wfDvmrpBaseEnable": wfDvmrpBaseEnable,
       "wfDvmrpBaseState": wfDvmrpBaseState,
       "wfDvmrpBaseFullUpdateInterval": wfDvmrpBaseFullUpdateInterval,
       "wfDvmrpBaseTriggeredUpdateInterval": wfDvmrpBaseTriggeredUpdateInterval,
       "wfDvmrpBaseLeafTimeout": wfDvmrpBaseLeafTimeout,
       "wfDvmrpBaseNeighborTimeout": wfDvmrpBaseNeighborTimeout,
       "wfDvmrpBaseRouteExpirationTimeout": wfDvmrpBaseRouteExpirationTimeout,
       "wfDvmrpBaseGarbageTimeout": wfDvmrpBaseGarbageTimeout,
       "wfDvmrpBaseEstimatedRoutes": wfDvmrpBaseEstimatedRoutes,
       "wfDvmrpBaseNeighborProbeInterval": wfDvmrpBaseNeighborProbeInterval,
       "wfDvmrpBaseRouteSwitchTimeout": wfDvmrpBaseRouteSwitchTimeout,
       "wfDvmrpBaseActualRoutes": wfDvmrpBaseActualRoutes,
       "wfDvmrpBaseDebugLevel": wfDvmrpBaseDebugLevel,
       "wfDvmrpBasePruningEnable": wfDvmrpBasePruningEnable,
       "wfDvmrpBaseFragmentMtuThreshold": wfDvmrpBaseFragmentMtuThreshold,
       "wfDvmrpBaseMaxRoutes": wfDvmrpBaseMaxRoutes,
       "wfDvmrpBasePolicyEnable": wfDvmrpBasePolicyEnable,
       "wfDvmrpBaseHolddownEnable": wfDvmrpBaseHolddownEnable,
       "wfDvmrpCircuitEntryTable": wfDvmrpCircuitEntryTable,
       "wfDvmrpCircuitEntry": wfDvmrpCircuitEntry,
       "wfDvmrpCircuitCreate": wfDvmrpCircuitCreate,
       "wfDvmrpCircuitEnable": wfDvmrpCircuitEnable,
       "wfDvmrpCircuitState": wfDvmrpCircuitState,
       "wfDvmrpCircuitCCT": wfDvmrpCircuitCCT,
       "wfDvmrpCircuitRouteEnable": wfDvmrpCircuitRouteEnable,
       "wfDvmrpCircuitMetric": wfDvmrpCircuitMetric,
       "wfDvmrpCircuitRouteThreshold": wfDvmrpCircuitRouteThreshold,
       "wfDvmrpCircuitInPkts": wfDvmrpCircuitInPkts,
       "wfDvmrpCircuitOutPkts": wfDvmrpCircuitOutPkts,
       "wfDvmrpCircuitInRouteUpdates": wfDvmrpCircuitInRouteUpdates,
       "wfDvmrpCircuitOutRouteUpdates": wfDvmrpCircuitOutRouteUpdates,
       "wfDvmrpCircuitInPktDiscards": wfDvmrpCircuitInPktDiscards,
       "wfDvmrpCircuitOutPktDiscards": wfDvmrpCircuitOutPktDiscards,
       "wfDvmrpCircuitFwdCacheSize": wfDvmrpCircuitFwdCacheSize,
       "wfDvmrpCircuitFwdCacheTTL": wfDvmrpCircuitFwdCacheTTL,
       "wfDvmrpCircuitAdvertiseSelf": wfDvmrpCircuitAdvertiseSelf,
       "wfDvmrpCircuitFwdCacheEntries": wfDvmrpCircuitFwdCacheEntries,
       "wfDvmrpCircuitInPrunePkts": wfDvmrpCircuitInPrunePkts,
       "wfDvmrpCircuitOutPrunePkts": wfDvmrpCircuitOutPrunePkts,
       "wfDvmrpCircuitInGraftPkts": wfDvmrpCircuitInGraftPkts,
       "wfDvmrpCircuitOutGraftPkts": wfDvmrpCircuitOutGraftPkts,
       "wfDvmrpCircuitInGraftAckPkts": wfDvmrpCircuitInGraftAckPkts,
       "wfDvmrpCircuitOutGraftAckPkts": wfDvmrpCircuitOutGraftAckPkts,
       "wfDvmrpCircuitDefaultRouteSupply": wfDvmrpCircuitDefaultRouteSupply,
       "wfDvmrpCircuitDefaultRouteListen": wfDvmrpCircuitDefaultRouteListen,
       "wfDvmrpCircuitReportDependProbe": wfDvmrpCircuitReportDependProbe,
       "wfDvmrpCircuitPruneLifeTime": wfDvmrpCircuitPruneLifeTime,
       "wfDvmrpCircuitAcceptAggregateRoutes": wfDvmrpCircuitAcceptAggregateRoutes,
       "wfDvmrpCircuitAnnounceAggregatedRoutes": wfDvmrpCircuitAnnounceAggregatedRoutes,
       "wfDvmrpTunnelEntryTable": wfDvmrpTunnelEntryTable,
       "wfDvmrpTunnelEntry": wfDvmrpTunnelEntry,
       "wfDvmrpTunnelCreate": wfDvmrpTunnelCreate,
       "wfDvmrpTunnelEnable": wfDvmrpTunnelEnable,
       "wfDvmrpTunnelState": wfDvmrpTunnelState,
       "wfDvmrpTunnelCCT": wfDvmrpTunnelCCT,
       "wfDvmrpTunnelRemoteRouterIpAddress": wfDvmrpTunnelRemoteRouterIpAddress,
       "wfDvmrpTunnelEncapsMode": wfDvmrpTunnelEncapsMode,
       "wfDvmrpTunnelMetric": wfDvmrpTunnelMetric,
       "wfDvmrpTunnelThreshold": wfDvmrpTunnelThreshold,
       "wfDvmrpTunnelInPkts": wfDvmrpTunnelInPkts,
       "wfDvmrpTunnelOutPkts": wfDvmrpTunnelOutPkts,
       "wfDvmrpTunnelInRouteUpdates": wfDvmrpTunnelInRouteUpdates,
       "wfDvmrpTunnelOutRouteUpdates": wfDvmrpTunnelOutRouteUpdates,
       "wfDvmrpTunnelInPktDiscards": wfDvmrpTunnelInPktDiscards,
       "wfDvmrpTunnelOutPktDiscards": wfDvmrpTunnelOutPktDiscards,
       "wfDvmrpTunnelLocalRouterIpAddress": wfDvmrpTunnelLocalRouterIpAddress,
       "wfDvmrpTunnelFwdCacheSize": wfDvmrpTunnelFwdCacheSize,
       "wfDvmrpTunnelFwdCacheTTL": wfDvmrpTunnelFwdCacheTTL,
       "wfDvmrpTunnelFwdCacheEntries": wfDvmrpTunnelFwdCacheEntries,
       "wfDvmrpTunnelInPrunePkts": wfDvmrpTunnelInPrunePkts,
       "wfDvmrpTunnelOutPrunePkts": wfDvmrpTunnelOutPrunePkts,
       "wfDvmrpTunnelInGraftPkts": wfDvmrpTunnelInGraftPkts,
       "wfDvmrpTunnelOutGraftPkts": wfDvmrpTunnelOutGraftPkts,
       "wfDvmrpTunnelInGraftAckPkts": wfDvmrpTunnelInGraftAckPkts,
       "wfDvmrpTunnelOutGraftAckPkts": wfDvmrpTunnelOutGraftAckPkts,
       "wfDvmrpTunnelDefaultRouteSupply": wfDvmrpTunnelDefaultRouteSupply,
       "wfDvmrpTunnelDefaultRouteListen": wfDvmrpTunnelDefaultRouteListen,
       "wfDvmrpTunnelCtrlMsgMode": wfDvmrpTunnelCtrlMsgMode,
       "wfDvmrpTunnelReportDependProbe": wfDvmrpTunnelReportDependProbe,
       "wfDvmrpTunnelPruneLifeTime": wfDvmrpTunnelPruneLifeTime,
       "wfDvmrpTunnelAcceptAggregateRoutes": wfDvmrpTunnelAcceptAggregateRoutes,
       "wfDvmrpTunnelAnnounceAggregatedRoutes": wfDvmrpTunnelAnnounceAggregatedRoutes,
       "wfDvmrpRouteEntryTable": wfDvmrpRouteEntryTable,
       "wfDvmrpRouteEntry": wfDvmrpRouteEntry,
       "wfDvmrpRouteSourceNetwork": wfDvmrpRouteSourceNetwork,
       "wfDvmrpRouteSourceMask": wfDvmrpRouteSourceMask,
       "wfDvmrpRouteNextHopRouter": wfDvmrpRouteNextHopRouter,
       "wfDvmrpRouteNextHopInterfaceCCT": wfDvmrpRouteNextHopInterfaceCCT,
       "wfDvmrpRouteNextHopInterfaceTunnelId": wfDvmrpRouteNextHopInterfaceTunnelId,
       "wfDvmrpRouteNextHopInterfaceLocalTunnelId": wfDvmrpRouteNextHopInterfaceLocalTunnelId,
       "wfDvmrpRouteTimer": wfDvmrpRouteTimer,
       "wfDvmrpRouteState": wfDvmrpRouteState,
       "wfDvmrpRouteMetric": wfDvmrpRouteMetric,
       "wfDvmrpRouteProtocol": wfDvmrpRouteProtocol,
       "wfDvmrpRouteType": wfDvmrpRouteType,
       "wfDvmrpRouteAggregatedType": wfDvmrpRouteAggregatedType,
       "wfDvmrpRouteInterfaceEntryTable": wfDvmrpRouteInterfaceEntryTable,
       "wfDvmrpRouteInterfaceEntry": wfDvmrpRouteInterfaceEntry,
       "wfDvmrpRouteInterfaceSourceNetwork": wfDvmrpRouteInterfaceSourceNetwork,
       "wfDvmrpRouteInterfaceSourceMask": wfDvmrpRouteInterfaceSourceMask,
       "wfDvmrpRouteInterfaceNextHopInterfaceCCT": wfDvmrpRouteInterfaceNextHopInterfaceCCT,
       "wfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId": wfDvmrpRouteInterfaceNextHopInterfaceLocalTunnelId,
       "wfDvmrpRouteInterfaceNextHopInterfaceTunnelId": wfDvmrpRouteInterfaceNextHopInterfaceTunnelId,
       "wfDvmrpRouteInterfaceState": wfDvmrpRouteInterfaceState,
       "wfDvmrpRouteInterfaceDominantRouter": wfDvmrpRouteInterfaceDominantRouter,
       "wfDvmrpRouteInterfaceSubordinateRouter": wfDvmrpRouteInterfaceSubordinateRouter,
       "wfDvmrpRouteInterfaceHoldDownTimer": wfDvmrpRouteInterfaceHoldDownTimer,
       "wfDvmrpRouteInterfaceSPInDiscards": wfDvmrpRouteInterfaceSPInDiscards,
       "wfDvmrpRouteInterfaceSPOutDiscards": wfDvmrpRouteInterfaceSPOutDiscards,
       "wfDvmrpRouteInterfaceThresholdOutDiscards": wfDvmrpRouteInterfaceThresholdOutDiscards,
       "wfDvmrpRouteInterfaceInSuccessfulPkts": wfDvmrpRouteInterfaceInSuccessfulPkts,
       "wfDvmrpRouteInterfaceOutSuccessfulPkts": wfDvmrpRouteInterfaceOutSuccessfulPkts,
       "wfDvmrpRouteInterfaceParentCCT": wfDvmrpRouteInterfaceParentCCT,
       "wfDvmrpRouteInterfaceParentLocalTunnelId": wfDvmrpRouteInterfaceParentLocalTunnelId,
       "wfDvmrpRouteInterfaceParentTunnelId": wfDvmrpRouteInterfaceParentTunnelId,
       "wfDvmrpNeighboringRouterEntryTable": wfDvmrpNeighboringRouterEntryTable,
       "wfDvmrpNeighboringRouterEntry": wfDvmrpNeighboringRouterEntry,
       "wfDvmrpNeighboringRouterCCT": wfDvmrpNeighboringRouterCCT,
       "wfDvmrpNeighboringRouterLocalTunnelId": wfDvmrpNeighboringRouterLocalTunnelId,
       "wfDvmrpNeighboringRouterTunnelId": wfDvmrpNeighboringRouterTunnelId,
       "wfDvmrpNeighboringRouterIpAddr": wfDvmrpNeighboringRouterIpAddr,
       "wfDvmrpNeighboringRouterState": wfDvmrpNeighboringRouterState,
       "wfDvmrpNeighboringRouterTimer": wfDvmrpNeighboringRouterTimer,
       "wfDvmrpNeighboringRouterGenId": wfDvmrpNeighboringRouterGenId,
       "wfDvmrpNeighboringRouterMajorVersion": wfDvmrpNeighboringRouterMajorVersion,
       "wfDvmrpNeighboringRouterMinorVersion": wfDvmrpNeighboringRouterMinorVersion,
       "wfDvmrpNeighboringRouterCapabilities": wfDvmrpNeighboringRouterCapabilities}
)
