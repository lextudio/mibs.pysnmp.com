# SNMP MIB module (Wellfleet-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:51 2024
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

(wfBgpGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfBgpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfBgpGeneralGroup_ObjectIdentity = ObjectIdentity
wfBgpGeneralGroup = _WfBgpGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1)
)
_WfBgp_ObjectIdentity = ObjectIdentity
wfBgp = _WfBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1)
)


class _WfBgpDelete_Type(Integer32):
    """Custom type wfBgpDelete based on Integer32"""
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


_WfBgpDelete_Type.__name__ = "Integer32"
_WfBgpDelete_Object = MibScalar
wfBgpDelete = _WfBgpDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 1),
    _WfBgpDelete_Type()
)
wfBgpDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDelete.setStatus("mandatory")


class _WfBgpDisable_Type(Integer32):
    """Custom type wfBgpDisable based on Integer32"""
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


_WfBgpDisable_Type.__name__ = "Integer32"
_WfBgpDisable_Object = MibScalar
wfBgpDisable = _WfBgpDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 2),
    _WfBgpDisable_Type()
)
wfBgpDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDisable.setStatus("mandatory")


class _WfBgpState_Type(Integer32):
    """Custom type wfBgpState based on Integer32"""
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
          ("notpresent", 5),
          ("up", 1))
    )


_WfBgpState_Type.__name__ = "Integer32"
_WfBgpState_Object = MibScalar
wfBgpState = _WfBgpState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 3),
    _WfBgpState_Type()
)
wfBgpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpState.setStatus("mandatory")
_WfBgpIdentifier_Type = IpAddress
_WfBgpIdentifier_Object = MibScalar
wfBgpIdentifier = _WfBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 4),
    _WfBgpIdentifier_Type()
)
wfBgpIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpIdentifier.setStatus("mandatory")


class _WfBgpLocalAs_Type(Integer32):
    """Custom type wfBgpLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfBgpLocalAs_Type.__name__ = "Integer32"
_WfBgpLocalAs_Object = MibScalar
wfBgpLocalAs = _WfBgpLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 5),
    _WfBgpLocalAs_Type()
)
wfBgpLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpLocalAs.setStatus("mandatory")


class _WfBgpEbgpDebugSwitch_Type(Integer32):
    """Custom type wfBgpEbgpDebugSwitch based on Integer32"""
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


_WfBgpEbgpDebugSwitch_Type.__name__ = "Integer32"
_WfBgpEbgpDebugSwitch_Object = MibScalar
wfBgpEbgpDebugSwitch = _WfBgpEbgpDebugSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 6),
    _WfBgpEbgpDebugSwitch_Type()
)
wfBgpEbgpDebugSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpEbgpDebugSwitch.setStatus("mandatory")
_WfBgpVersion_Type = OctetString
_WfBgpVersion_Object = MibScalar
wfBgpVersion = _WfBgpVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 7),
    _WfBgpVersion_Type()
)
wfBgpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpVersion.setStatus("mandatory")


class _WfBgpIntraAsIbgpRouting_Type(Integer32):
    """Custom type wfBgpIntraAsIbgpRouting based on Integer32"""
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


_WfBgpIntraAsIbgpRouting_Type.__name__ = "Integer32"
_WfBgpIntraAsIbgpRouting_Object = MibScalar
wfBgpIntraAsIbgpRouting = _WfBgpIntraAsIbgpRouting_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 8),
    _WfBgpIntraAsIbgpRouting_Type()
)
wfBgpIntraAsIbgpRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpIntraAsIbgpRouting.setStatus("mandatory")


class _WfIbgpFromProtocols_Type(Integer32):
    """Custom type wfIbgpFromProtocols based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 2),
          ("bgp", 1))
    )


_WfIbgpFromProtocols_Type.__name__ = "Integer32"
_WfIbgpFromProtocols_Object = MibScalar
wfIbgpFromProtocols = _WfIbgpFromProtocols_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 9),
    _WfIbgpFromProtocols_Type()
)
wfIbgpFromProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIbgpFromProtocols.setStatus("mandatory")


class _WfBgpIntAdvTimer_Type(Integer32):
    """Custom type wfBgpIntAdvTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgpIntAdvTimer_Type.__name__ = "Integer32"
_WfBgpIntAdvTimer_Object = MibScalar
wfBgpIntAdvTimer = _WfBgpIntAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 10),
    _WfBgpIntAdvTimer_Type()
)
wfBgpIntAdvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpIntAdvTimer.setStatus("mandatory")
_WfBgpUsedRoutes_Type = Counter32
_WfBgpUsedRoutes_Object = MibScalar
wfBgpUsedRoutes = _WfBgpUsedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 11),
    _WfBgpUsedRoutes_Type()
)
wfBgpUsedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpUsedRoutes.setStatus("mandatory")
_WfBgpTotalRoutes_Type = Counter32
_WfBgpTotalRoutes_Object = MibScalar
wfBgpTotalRoutes = _WfBgpTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 12),
    _WfBgpTotalRoutes_Type()
)
wfBgpTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpTotalRoutes.setStatus("mandatory")
_WfBgpTotalPaths_Type = Counter32
_WfBgpTotalPaths_Object = MibScalar
wfBgpTotalPaths = _WfBgpTotalPaths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 13),
    _WfBgpTotalPaths_Type()
)
wfBgpTotalPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpTotalPaths.setStatus("mandatory")


class _WfBgpMaxRedundantIbgpRoutes_Type(Integer32):
    """Custom type wfBgpMaxRedundantIbgpRoutes based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfBgpMaxRedundantIbgpRoutes_Type.__name__ = "Integer32"
_WfBgpMaxRedundantIbgpRoutes_Object = MibScalar
wfBgpMaxRedundantIbgpRoutes = _WfBgpMaxRedundantIbgpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 14),
    _WfBgpMaxRedundantIbgpRoutes_Type()
)
wfBgpMaxRedundantIbgpRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpMaxRedundantIbgpRoutes.setStatus("mandatory")


class _WfBgpRouteRequestSwitch_Type(Integer32):
    """Custom type wfBgpRouteRequestSwitch based on Integer32"""
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


_WfBgpRouteRequestSwitch_Type.__name__ = "Integer32"
_WfBgpRouteRequestSwitch_Object = MibScalar
wfBgpRouteRequestSwitch = _WfBgpRouteRequestSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 15),
    _WfBgpRouteRequestSwitch_Type()
)
wfBgpRouteRequestSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteRequestSwitch.setStatus("mandatory")


class _WfBgpConnCollisionDetect_Type(Integer32):
    """Custom type wfBgpConnCollisionDetect based on Integer32"""
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


_WfBgpConnCollisionDetect_Type.__name__ = "Integer32"
_WfBgpConnCollisionDetect_Object = MibScalar
wfBgpConnCollisionDetect = _WfBgpConnCollisionDetect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 16),
    _WfBgpConnCollisionDetect_Type()
)
wfBgpConnCollisionDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpConnCollisionDetect.setStatus("mandatory")


class _WfBgpRsTopology_Type(Integer32):
    """Custom type wfBgpRsTopology based on Integer32"""
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
        *(("client", 2),
          ("mesh", 3),
          ("none", 1),
          ("tree", 4))
    )


_WfBgpRsTopology_Type.__name__ = "Integer32"
_WfBgpRsTopology_Object = MibScalar
wfBgpRsTopology = _WfBgpRsTopology_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 17),
    _WfBgpRsTopology_Type()
)
wfBgpRsTopology.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRsTopology.setStatus("mandatory")


class _WfBgpClusterIdentifier_Type(Gauge32):
    """Custom type wfBgpClusterIdentifier based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_WfBgpClusterIdentifier_Type.__name__ = "Gauge32"
_WfBgpClusterIdentifier_Object = MibScalar
wfBgpClusterIdentifier = _WfBgpClusterIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 18),
    _WfBgpClusterIdentifier_Type()
)
wfBgpClusterIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpClusterIdentifier.setStatus("mandatory")


class _WfBgpDynamicPolChangeSupport_Type(Integer32):
    """Custom type wfBgpDynamicPolChangeSupport based on Integer32"""
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


_WfBgpDynamicPolChangeSupport_Type.__name__ = "Integer32"
_WfBgpDynamicPolChangeSupport_Object = MibScalar
wfBgpDynamicPolChangeSupport = _WfBgpDynamicPolChangeSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 19),
    _WfBgpDynamicPolChangeSupport_Type()
)
wfBgpDynamicPolChangeSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDynamicPolChangeSupport.setStatus("mandatory")


class _WfBgpSoloistSlots_Type(Gauge32):
    """Custom type wfBgpSoloistSlots based on Gauge32"""
    defaultValue = 4294705152


_WfBgpSoloistSlots_Object = MibScalar
wfBgpSoloistSlots = _WfBgpSoloistSlots_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 20),
    _WfBgpSoloistSlots_Type()
)
wfBgpSoloistSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpSoloistSlots.setStatus("mandatory")


class _WfBgpSoloistSlot_Type(Integer32):
    """Custom type wfBgpSoloistSlot based on Integer32"""
    defaultValue = 0


_WfBgpSoloistSlot_Object = MibScalar
wfBgpSoloistSlot = _WfBgpSoloistSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 21),
    _WfBgpSoloistSlot_Type()
)
wfBgpSoloistSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpSoloistSlot.setStatus("mandatory")


class _WfBgpSubnetAggregation_Type(Integer32):
    """Custom type wfBgpSubnetAggregation based on Integer32"""
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


_WfBgpSubnetAggregation_Type.__name__ = "Integer32"
_WfBgpSubnetAggregation_Object = MibScalar
wfBgpSubnetAggregation = _WfBgpSubnetAggregation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 22),
    _WfBgpSubnetAggregation_Type()
)
wfBgpSubnetAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpSubnetAggregation.setStatus("mandatory")


class _WfBgpBlackHoleSupport_Type(Integer32):
    """Custom type wfBgpBlackHoleSupport based on Integer32"""
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
        *(("disabled", 1),
          ("drop", 2),
          ("reject", 3))
    )


_WfBgpBlackHoleSupport_Type.__name__ = "Integer32"
_WfBgpBlackHoleSupport_Object = MibScalar
wfBgpBlackHoleSupport = _WfBgpBlackHoleSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 23),
    _WfBgpBlackHoleSupport_Type()
)
wfBgpBlackHoleSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpBlackHoleSupport.setStatus("mandatory")


class _WfBgpMedComparison_Type(Integer32):
    """Custom type wfBgpMedComparison based on Integer32"""
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


_WfBgpMedComparison_Type.__name__ = "Integer32"
_WfBgpMedComparison_Object = MibScalar
wfBgpMedComparison = _WfBgpMedComparison_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 24),
    _WfBgpMedComparison_Type()
)
wfBgpMedComparison.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpMedComparison.setStatus("mandatory")


class _WfBgpIbgpReflection_Type(Integer32):
    """Custom type wfBgpIbgpReflection based on Integer32"""
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


_WfBgpIbgpReflection_Type.__name__ = "Integer32"
_WfBgpIbgpReflection_Object = MibScalar
wfBgpIbgpReflection = _WfBgpIbgpReflection_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 25),
    _WfBgpIbgpReflection_Type()
)
wfBgpIbgpReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpIbgpReflection.setStatus("mandatory")


class _WfBgpIbgpEcmpMethod_Type(Integer32):
    """Custom type wfBgpIbgpEcmpMethod based on Integer32"""
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
        *(("disabled", 1),
          ("route-balance", 2),
          ("traffic-balance", 3))
    )


_WfBgpIbgpEcmpMethod_Type.__name__ = "Integer32"
_WfBgpIbgpEcmpMethod_Object = MibScalar
wfBgpIbgpEcmpMethod = _WfBgpIbgpEcmpMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 26),
    _WfBgpIbgpEcmpMethod_Type()
)
wfBgpIbgpEcmpMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpIbgpEcmpMethod.setStatus("mandatory")


class _WfBgpLocalPrefCalc_Type(Integer32):
    """Custom type wfBgpLocalPrefCalc based on Integer32"""
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


_WfBgpLocalPrefCalc_Type.__name__ = "Integer32"
_WfBgpLocalPrefCalc_Object = MibScalar
wfBgpLocalPrefCalc = _WfBgpLocalPrefCalc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 27),
    _WfBgpLocalPrefCalc_Type()
)
wfBgpLocalPrefCalc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpLocalPrefCalc.setStatus("mandatory")


class _WfBgpConfedIdentifier_Type(Integer32):
    """Custom type wfBgpConfedIdentifier based on Integer32"""
    defaultValue = 0


_WfBgpConfedIdentifier_Object = MibScalar
wfBgpConfedIdentifier = _WfBgpConfedIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 28),
    _WfBgpConfedIdentifier_Type()
)
wfBgpConfedIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpConfedIdentifier.setStatus("mandatory")
_WfBgpConfedPeers_Type = OctetString
_WfBgpConfedPeers_Object = MibScalar
wfBgpConfedPeers = _WfBgpConfedPeers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 29),
    _WfBgpConfedPeers_Type()
)
wfBgpConfedPeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpConfedPeers.setStatus("mandatory")


class _WfBgpIgpInterAction_Type(Integer32):
    """Custom type wfBgpIgpInterAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_WfBgpIgpInterAction_Type.__name__ = "Integer32"
_WfBgpIgpInterAction_Object = MibScalar
wfBgpIgpInterAction = _WfBgpIgpInterAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 1, 30),
    _WfBgpIgpInterAction_Type()
)
wfBgpIgpInterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpIgpInterAction.setStatus("mandatory")
_WfBgpPeerTable_Object = MibTable
wfBgpPeerTable = _WfBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    wfBgpPeerTable.setStatus("mandatory")
_WfBgpPeerEntry_Object = MibTableRow
wfBgpPeerEntry = _WfBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1)
)
wfBgpPeerEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgpPeerLocalAddr"),
    (0, "Wellfleet-BGP-MIB", "wfBgpPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    wfBgpPeerEntry.setStatus("mandatory")


class _WfBgpPeerDelete_Type(Integer32):
    """Custom type wfBgpPeerDelete based on Integer32"""
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


_WfBgpPeerDelete_Type.__name__ = "Integer32"
_WfBgpPeerDelete_Object = MibTableColumn
wfBgpPeerDelete = _WfBgpPeerDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 1),
    _WfBgpPeerDelete_Type()
)
wfBgpPeerDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerDelete.setStatus("mandatory")


class _WfBgpPeerDisable_Type(Integer32):
    """Custom type wfBgpPeerDisable based on Integer32"""
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


_WfBgpPeerDisable_Type.__name__ = "Integer32"
_WfBgpPeerDisable_Object = MibTableColumn
wfBgpPeerDisable = _WfBgpPeerDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 2),
    _WfBgpPeerDisable_Type()
)
wfBgpPeerDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerDisable.setStatus("mandatory")


class _WfBgpPeerState_Type(Integer32):
    """Custom type wfBgpPeerState based on Integer32"""
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
          ("notpresent", 5),
          ("up", 1))
    )


_WfBgpPeerState_Type.__name__ = "Integer32"
_WfBgpPeerState_Object = MibTableColumn
wfBgpPeerState = _WfBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 3),
    _WfBgpPeerState_Type()
)
wfBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerState.setStatus("mandatory")
_WfBgpPeerLocalAddr_Type = IpAddress
_WfBgpPeerLocalAddr_Object = MibTableColumn
wfBgpPeerLocalAddr = _WfBgpPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 4),
    _WfBgpPeerLocalAddr_Type()
)
wfBgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerLocalAddr.setStatus("mandatory")
_WfBgpPeerLocalPort_Type = Integer32
_WfBgpPeerLocalPort_Object = MibTableColumn
wfBgpPeerLocalPort = _WfBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 5),
    _WfBgpPeerLocalPort_Type()
)
wfBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerLocalPort.setStatus("mandatory")
_WfBgpPeerRemoteAddr_Type = IpAddress
_WfBgpPeerRemoteAddr_Object = MibTableColumn
wfBgpPeerRemoteAddr = _WfBgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 6),
    _WfBgpPeerRemoteAddr_Type()
)
wfBgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerRemoteAddr.setStatus("mandatory")
_WfBgpPeerRemotePort_Type = Integer32
_WfBgpPeerRemotePort_Object = MibTableColumn
wfBgpPeerRemotePort = _WfBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 7),
    _WfBgpPeerRemotePort_Type()
)
wfBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerRemotePort.setStatus("mandatory")


class _WfBgpPeerMinVersion_Type(Integer32):
    """Custom type wfBgpPeerMinVersion based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bgp3", 3),
          ("bgp4", 4))
    )


_WfBgpPeerMinVersion_Type.__name__ = "Integer32"
_WfBgpPeerMinVersion_Object = MibTableColumn
wfBgpPeerMinVersion = _WfBgpPeerMinVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 8),
    _WfBgpPeerMinVersion_Type()
)
wfBgpPeerMinVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerMinVersion.setStatus("mandatory")


class _WfBgpPeerMaxVersion_Type(Integer32):
    """Custom type wfBgpPeerMaxVersion based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bgp3", 3),
          ("bgp4", 4))
    )


_WfBgpPeerMaxVersion_Type.__name__ = "Integer32"
_WfBgpPeerMaxVersion_Object = MibTableColumn
wfBgpPeerMaxVersion = _WfBgpPeerMaxVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 9),
    _WfBgpPeerMaxVersion_Type()
)
wfBgpPeerMaxVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerMaxVersion.setStatus("mandatory")
_WfBgpPeerRemoteAs_Type = Integer32
_WfBgpPeerRemoteAs_Object = MibTableColumn
wfBgpPeerRemoteAs = _WfBgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 10),
    _WfBgpPeerRemoteAs_Type()
)
wfBgpPeerRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerRemoteAs.setStatus("mandatory")


class _WfBgpPeerExtAdvTimer_Type(Integer32):
    """Custom type wfBgpPeerExtAdvTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgpPeerExtAdvTimer_Type.__name__ = "Integer32"
_WfBgpPeerExtAdvTimer_Object = MibTableColumn
wfBgpPeerExtAdvTimer = _WfBgpPeerExtAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 11),
    _WfBgpPeerExtAdvTimer_Type()
)
wfBgpPeerExtAdvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerExtAdvTimer.setStatus("mandatory")


class _WfBgpPeerConnectRetry_Type(Integer32):
    """Custom type wfBgpPeerConnectRetry based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgpPeerConnectRetry_Type.__name__ = "Integer32"
_WfBgpPeerConnectRetry_Object = MibTableColumn
wfBgpPeerConnectRetry = _WfBgpPeerConnectRetry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 12),
    _WfBgpPeerConnectRetry_Type()
)
wfBgpPeerConnectRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerConnectRetry.setStatus("mandatory")


class _WfBgpPeerCfgHoldtime_Type(Integer32):
    """Custom type wfBgpPeerCfgHoldtime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 2147483647),
    )


_WfBgpPeerCfgHoldtime_Type.__name__ = "Integer32"
_WfBgpPeerCfgHoldtime_Object = MibTableColumn
wfBgpPeerCfgHoldtime = _WfBgpPeerCfgHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 13),
    _WfBgpPeerCfgHoldtime_Type()
)
wfBgpPeerCfgHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerCfgHoldtime.setStatus("mandatory")
_WfBgpPeerHoldtime_Type = Integer32
_WfBgpPeerHoldtime_Object = MibTableColumn
wfBgpPeerHoldtime = _WfBgpPeerHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 14),
    _WfBgpPeerHoldtime_Type()
)
wfBgpPeerHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerHoldtime.setStatus("mandatory")


class _WfBgpPeerCfgKeepAlive_Type(Integer32):
    """Custom type wfBgpPeerCfgKeepAlive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgpPeerCfgKeepAlive_Type.__name__ = "Integer32"
_WfBgpPeerCfgKeepAlive_Object = MibTableColumn
wfBgpPeerCfgKeepAlive = _WfBgpPeerCfgKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 15),
    _WfBgpPeerCfgKeepAlive_Type()
)
wfBgpPeerCfgKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerCfgKeepAlive.setStatus("mandatory")
_WfBgpPeerKeepAlive_Type = Integer32
_WfBgpPeerKeepAlive_Object = MibTableColumn
wfBgpPeerKeepAlive = _WfBgpPeerKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 16),
    _WfBgpPeerKeepAlive_Type()
)
wfBgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerKeepAlive.setStatus("mandatory")


class _WfBgpPeerPathAttrSwitch_Type(Integer32):
    """Custom type wfBgpPeerPathAttrSwitch based on Integer32"""
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


_WfBgpPeerPathAttrSwitch_Type.__name__ = "Integer32"
_WfBgpPeerPathAttrSwitch_Object = MibTableColumn
wfBgpPeerPathAttrSwitch = _WfBgpPeerPathAttrSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 17),
    _WfBgpPeerPathAttrSwitch_Type()
)
wfBgpPeerPathAttrSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerPathAttrSwitch.setStatus("obsolete")
_WfBgpPeerIdentifier_Type = IpAddress
_WfBgpPeerIdentifier_Object = MibTableColumn
wfBgpPeerIdentifier = _WfBgpPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 18),
    _WfBgpPeerIdentifier_Type()
)
wfBgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerIdentifier.setStatus("mandatory")


class _WfBgpPeerConnState_Type(Integer32):
    """Custom type wfBgpPeerConnState based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_WfBgpPeerConnState_Type.__name__ = "Integer32"
_WfBgpPeerConnState_Object = MibTableColumn
wfBgpPeerConnState = _WfBgpPeerConnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 19),
    _WfBgpPeerConnState_Type()
)
wfBgpPeerConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerConnState.setStatus("mandatory")
_WfBgpPeerNegotiatedVersion_Type = Integer32
_WfBgpPeerNegotiatedVersion_Object = MibTableColumn
wfBgpPeerNegotiatedVersion = _WfBgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 20),
    _WfBgpPeerNegotiatedVersion_Type()
)
wfBgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerNegotiatedVersion.setStatus("mandatory")
_WfBgpPeerInUpdates_Type = Counter32
_WfBgpPeerInUpdates_Object = MibTableColumn
wfBgpPeerInUpdates = _WfBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 21),
    _WfBgpPeerInUpdates_Type()
)
wfBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerInUpdates.setStatus("mandatory")
_WfBgpPeerOutUpdates_Type = Counter32
_WfBgpPeerOutUpdates_Object = MibTableColumn
wfBgpPeerOutUpdates = _WfBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 22),
    _WfBgpPeerOutUpdates_Type()
)
wfBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerOutUpdates.setStatus("mandatory")
_WfBgpPeerInTotalMessages_Type = Counter32
_WfBgpPeerInTotalMessages_Object = MibTableColumn
wfBgpPeerInTotalMessages = _WfBgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 23),
    _WfBgpPeerInTotalMessages_Type()
)
wfBgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerInTotalMessages.setStatus("mandatory")
_WfBgpPeerOutTotalMessages_Type = Counter32
_WfBgpPeerOutTotalMessages_Object = MibTableColumn
wfBgpPeerOutTotalMessages = _WfBgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 24),
    _WfBgpPeerOutTotalMessages_Type()
)
wfBgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerOutTotalMessages.setStatus("mandatory")
_WfBgpPeerLastError_Type = OctetString
_WfBgpPeerLastError_Object = MibTableColumn
wfBgpPeerLastError = _WfBgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 25),
    _WfBgpPeerLastError_Type()
)
wfBgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerLastError.setStatus("mandatory")
_WfBgpPeerTotalRoutes_Type = Counter32
_WfBgpPeerTotalRoutes_Object = MibTableColumn
wfBgpPeerTotalRoutes = _WfBgpPeerTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 26),
    _WfBgpPeerTotalRoutes_Type()
)
wfBgpPeerTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerTotalRoutes.setStatus("mandatory")
_WfBgpPeerFsmEstablishedTransitions_Type = Counter32
_WfBgpPeerFsmEstablishedTransitions_Object = MibTableColumn
wfBgpPeerFsmEstablishedTransitions = _WfBgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 27),
    _WfBgpPeerFsmEstablishedTransitions_Type()
)
wfBgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerFsmEstablishedTransitions.setStatus("mandatory")
_WfBgpPeerFsmEstablishedTime_Type = Gauge32
_WfBgpPeerFsmEstablishedTime_Object = MibTableColumn
wfBgpPeerFsmEstablishedTime = _WfBgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 28),
    _WfBgpPeerFsmEstablishedTime_Type()
)
wfBgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerFsmEstablishedTime.setStatus("mandatory")
_WfBgpPeerInUpdateElapsedTime_Type = Gauge32
_WfBgpPeerInUpdateElapsedTime_Object = MibTableColumn
wfBgpPeerInUpdateElapsedTime = _WfBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 29),
    _WfBgpPeerInUpdateElapsedTime_Type()
)
wfBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerInUpdateElapsedTime.setStatus("mandatory")


class _WfBgpPeerMinASOriginationInterval_Type(Integer32):
    """Custom type wfBgpPeerMinASOriginationInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgpPeerMinASOriginationInterval_Type.__name__ = "Integer32"
_WfBgpPeerMinASOriginationInterval_Object = MibTableColumn
wfBgpPeerMinASOriginationInterval = _WfBgpPeerMinASOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 30),
    _WfBgpPeerMinASOriginationInterval_Type()
)
wfBgpPeerMinASOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerMinASOriginationInterval.setStatus("mandatory")


class _WfBgpPeerLocalAS_Type(Integer32):
    """Custom type wfBgpPeerLocalAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfBgpPeerLocalAS_Type.__name__ = "Integer32"
_WfBgpPeerLocalAS_Object = MibTableColumn
wfBgpPeerLocalAS = _WfBgpPeerLocalAS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 31),
    _WfBgpPeerLocalAS_Type()
)
wfBgpPeerLocalAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerLocalAS.setStatus("mandatory")


class _WfBgpPeerMaxUpdateSize_Type(Integer32):
    """Custom type wfBgpPeerMaxUpdateSize based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 4096),
    )


_WfBgpPeerMaxUpdateSize_Type.__name__ = "Integer32"
_WfBgpPeerMaxUpdateSize_Object = MibTableColumn
wfBgpPeerMaxUpdateSize = _WfBgpPeerMaxUpdateSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 32),
    _WfBgpPeerMaxUpdateSize_Type()
)
wfBgpPeerMaxUpdateSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerMaxUpdateSize.setStatus("mandatory")


class _WfBgpPeerRouteEchoSwitch_Type(Integer32):
    """Custom type wfBgpPeerRouteEchoSwitch based on Integer32"""
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


_WfBgpPeerRouteEchoSwitch_Type.__name__ = "Integer32"
_WfBgpPeerRouteEchoSwitch_Object = MibTableColumn
wfBgpPeerRouteEchoSwitch = _WfBgpPeerRouteEchoSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 33),
    _WfBgpPeerRouteEchoSwitch_Type()
)
wfBgpPeerRouteEchoSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerRouteEchoSwitch.setStatus("mandatory")


class _WfBgpPeerDiscardDuplicateRouteSwitch_Type(Integer32):
    """Custom type wfBgpPeerDiscardDuplicateRouteSwitch based on Integer32"""
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


_WfBgpPeerDiscardDuplicateRouteSwitch_Type.__name__ = "Integer32"
_WfBgpPeerDiscardDuplicateRouteSwitch_Object = MibTableColumn
wfBgpPeerDiscardDuplicateRouteSwitch = _WfBgpPeerDiscardDuplicateRouteSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 34),
    _WfBgpPeerDiscardDuplicateRouteSwitch_Type()
)
wfBgpPeerDiscardDuplicateRouteSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerDiscardDuplicateRouteSwitch.setStatus("mandatory")


class _WfBgpPeerRSMode_Type(Integer32):
    """Custom type wfBgpPeerRSMode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reflector-client", 5),
          ("reflector-external", 7),
          ("reflector-internal", 6),
          ("server-client", 2),
          ("server-external", 4),
          ("server-internal", 3))
    )


_WfBgpPeerRSMode_Type.__name__ = "Integer32"
_WfBgpPeerRSMode_Object = MibTableColumn
wfBgpPeerRSMode = _WfBgpPeerRSMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 35),
    _WfBgpPeerRSMode_Type()
)
wfBgpPeerRSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerRSMode.setStatus("mandatory")


class _WfBgpPeerRSIdentifier_Type(Integer32):
    """Custom type wfBgpPeerRSIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfBgpPeerRSIdentifier_Type.__name__ = "Integer32"
_WfBgpPeerRSIdentifier_Object = MibTableColumn
wfBgpPeerRSIdentifier = _WfBgpPeerRSIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 36),
    _WfBgpPeerRSIdentifier_Type()
)
wfBgpPeerRSIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerRSIdentifier.setStatus("obsolete")


class _WfBgpPeerCfgDelayGranularity_Type(Integer32):
    """Custom type wfBgpPeerCfgDelayGranularity based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgpPeerCfgDelayGranularity_Type.__name__ = "Integer32"
_WfBgpPeerCfgDelayGranularity_Object = MibTableColumn
wfBgpPeerCfgDelayGranularity = _WfBgpPeerCfgDelayGranularity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 37),
    _WfBgpPeerCfgDelayGranularity_Type()
)
wfBgpPeerCfgDelayGranularity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerCfgDelayGranularity.setStatus("mandatory")
_WfBgpPeerDelayGranularity_Type = Integer32
_WfBgpPeerDelayGranularity_Object = MibTableColumn
wfBgpPeerDelayGranularity = _WfBgpPeerDelayGranularity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 38),
    _WfBgpPeerDelayGranularity_Type()
)
wfBgpPeerDelayGranularity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerDelayGranularity.setStatus("mandatory")


class _WfBgpPeerLastErrorSrc_Type(Integer32):
    """Custom type wfBgpPeerLastErrorSrc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_WfBgpPeerLastErrorSrc_Type.__name__ = "Integer32"
_WfBgpPeerLastErrorSrc_Object = MibTableColumn
wfBgpPeerLastErrorSrc = _WfBgpPeerLastErrorSrc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 39),
    _WfBgpPeerLastErrorSrc_Type()
)
wfBgpPeerLastErrorSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerLastErrorSrc.setStatus("mandatory")


class _WfBgpPeerNexthopSelf_Type(Integer32):
    """Custom type wfBgpPeerNexthopSelf based on Integer32"""
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


_WfBgpPeerNexthopSelf_Type.__name__ = "Integer32"
_WfBgpPeerNexthopSelf_Object = MibTableColumn
wfBgpPeerNexthopSelf = _WfBgpPeerNexthopSelf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 40),
    _WfBgpPeerNexthopSelf_Type()
)
wfBgpPeerNexthopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerNexthopSelf.setStatus("mandatory")


class _WfBgpPeerASLoopDetect_Type(Integer32):
    """Custom type wfBgpPeerASLoopDetect based on Integer32"""
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


_WfBgpPeerASLoopDetect_Type.__name__ = "Integer32"
_WfBgpPeerASLoopDetect_Object = MibTableColumn
wfBgpPeerASLoopDetect = _WfBgpPeerASLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 41),
    _WfBgpPeerASLoopDetect_Type()
)
wfBgpPeerASLoopDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerASLoopDetect.setStatus("mandatory")


class _WfBgpPeerBgpEcmpMethod_Type(Integer32):
    """Custom type wfBgpPeerBgpEcmpMethod based on Integer32"""
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
        *(("disabled", 1),
          ("route-balance", 2),
          ("traffic-balance", 3))
    )


_WfBgpPeerBgpEcmpMethod_Type.__name__ = "Integer32"
_WfBgpPeerBgpEcmpMethod_Object = MibTableColumn
wfBgpPeerBgpEcmpMethod = _WfBgpPeerBgpEcmpMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 42),
    _WfBgpPeerBgpEcmpMethod_Type()
)
wfBgpPeerBgpEcmpMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerBgpEcmpMethod.setStatus("mandatory")


class _WfBgpPeerDampenedRoutes_Type(Integer32):
    """Custom type wfBgpPeerDampenedRoutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgpPeerDampenedRoutes_Type.__name__ = "Integer32"
_WfBgpPeerDampenedRoutes_Object = MibTableColumn
wfBgpPeerDampenedRoutes = _WfBgpPeerDampenedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 43),
    _WfBgpPeerDampenedRoutes_Type()
)
wfBgpPeerDampenedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPeerDampenedRoutes.setStatus("mandatory")


class _WfBgpPeerTTL_Type(Integer32):
    """Custom type wfBgpPeerTTL based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfBgpPeerTTL_Type.__name__ = "Integer32"
_WfBgpPeerTTL_Object = MibTableColumn
wfBgpPeerTTL = _WfBgpPeerTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 44),
    _WfBgpPeerTTL_Type()
)
wfBgpPeerTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerTTL.setStatus("mandatory")


class _WfBgpPeerTcpAuthentication_Type(Integer32):
    """Custom type wfBgpPeerTcpAuthentication based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("md5", 2),
          ("none", 1))
    )


_WfBgpPeerTcpAuthentication_Type.__name__ = "Integer32"
_WfBgpPeerTcpAuthentication_Object = MibTableColumn
wfBgpPeerTcpAuthentication = _WfBgpPeerTcpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 45),
    _WfBgpPeerTcpAuthentication_Type()
)
wfBgpPeerTcpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerTcpAuthentication.setStatus("mandatory")


class _WfBgpPeerTcpMd5KeyStorage_Type(Integer32):
    """Custom type wfBgpPeerTcpMd5KeyStorage based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear-text", 1),
          ("encrypted", 2))
    )


_WfBgpPeerTcpMd5KeyStorage_Type.__name__ = "Integer32"
_WfBgpPeerTcpMd5KeyStorage_Object = MibTableColumn
wfBgpPeerTcpMd5KeyStorage = _WfBgpPeerTcpMd5KeyStorage_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 46),
    _WfBgpPeerTcpMd5KeyStorage_Type()
)
wfBgpPeerTcpMd5KeyStorage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerTcpMd5KeyStorage.setStatus("mandatory")
_WfBgpPeerTcpMd5Key_Type = OctetString
_WfBgpPeerTcpMd5Key_Object = MibTableColumn
wfBgpPeerTcpMd5Key = _WfBgpPeerTcpMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 2, 1, 47),
    _WfBgpPeerTcpMd5Key_Type()
)
wfBgpPeerTcpMd5Key.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpPeerTcpMd5Key.setStatus("mandatory")
_WfBgpAsWeightTable_Object = MibTable
wfBgpAsWeightTable = _WfBgpAsWeightTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3)
)
if mibBuilder.loadTexts:
    wfBgpAsWeightTable.setStatus("mandatory")
_WfBgpAsWeightEntry_Object = MibTableRow
wfBgpAsWeightEntry = _WfBgpAsWeightEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1)
)
wfBgpAsWeightEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgpAsWeightNumber"),
)
if mibBuilder.loadTexts:
    wfBgpAsWeightEntry.setStatus("mandatory")


class _WfBgpAsWeightDelete_Type(Integer32):
    """Custom type wfBgpAsWeightDelete based on Integer32"""
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


_WfBgpAsWeightDelete_Type.__name__ = "Integer32"
_WfBgpAsWeightDelete_Object = MibTableColumn
wfBgpAsWeightDelete = _WfBgpAsWeightDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 1),
    _WfBgpAsWeightDelete_Type()
)
wfBgpAsWeightDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightDelete.setStatus("mandatory")


class _WfBgpAsWeightDisable_Type(Integer32):
    """Custom type wfBgpAsWeightDisable based on Integer32"""
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


_WfBgpAsWeightDisable_Type.__name__ = "Integer32"
_WfBgpAsWeightDisable_Object = MibTableColumn
wfBgpAsWeightDisable = _WfBgpAsWeightDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 2),
    _WfBgpAsWeightDisable_Type()
)
wfBgpAsWeightDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightDisable.setStatus("mandatory")


class _WfBgpAsWeightState_Type(Integer32):
    """Custom type wfBgpAsWeightState based on Integer32"""
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
          ("notpresent", 5),
          ("up", 1))
    )


_WfBgpAsWeightState_Type.__name__ = "Integer32"
_WfBgpAsWeightState_Object = MibTableColumn
wfBgpAsWeightState = _WfBgpAsWeightState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 3),
    _WfBgpAsWeightState_Type()
)
wfBgpAsWeightState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpAsWeightState.setStatus("mandatory")


class _WfBgpAsWeightNumber_Type(Integer32):
    """Custom type wfBgpAsWeightNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfBgpAsWeightNumber_Type.__name__ = "Integer32"
_WfBgpAsWeightNumber_Object = MibTableColumn
wfBgpAsWeightNumber = _WfBgpAsWeightNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 4),
    _WfBgpAsWeightNumber_Type()
)
wfBgpAsWeightNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpAsWeightNumber.setStatus("mandatory")


class _WfBgpAsWeightValue_Type(Integer32):
    """Custom type wfBgpAsWeightValue based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_WfBgpAsWeightValue_Type.__name__ = "Integer32"
_WfBgpAsWeightValue_Object = MibTableColumn
wfBgpAsWeightValue = _WfBgpAsWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 5),
    _WfBgpAsWeightValue_Type()
)
wfBgpAsWeightValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue.setStatus("mandatory")


class _WfBgpAsWeightValue2_Type(Integer32):
    """Custom type wfBgpAsWeightValue2 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("default2", 8)
    )


_WfBgpAsWeightValue2_Type.__name__ = "Integer32"
_WfBgpAsWeightValue2_Object = MibTableColumn
wfBgpAsWeightValue2 = _WfBgpAsWeightValue2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 6),
    _WfBgpAsWeightValue2_Type()
)
wfBgpAsWeightValue2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue2.setStatus("mandatory")


class _WfBgpAsWeightValue3_Type(Integer32):
    """Custom type wfBgpAsWeightValue3 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("default3", 8)
    )


_WfBgpAsWeightValue3_Type.__name__ = "Integer32"
_WfBgpAsWeightValue3_Object = MibTableColumn
wfBgpAsWeightValue3 = _WfBgpAsWeightValue3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 7),
    _WfBgpAsWeightValue3_Type()
)
wfBgpAsWeightValue3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue3.setStatus("mandatory")


class _WfBgpAsWeightValue4_Type(Integer32):
    """Custom type wfBgpAsWeightValue4 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("default4", 8)
    )


_WfBgpAsWeightValue4_Type.__name__ = "Integer32"
_WfBgpAsWeightValue4_Object = MibTableColumn
wfBgpAsWeightValue4 = _WfBgpAsWeightValue4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 8),
    _WfBgpAsWeightValue4_Type()
)
wfBgpAsWeightValue4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue4.setStatus("mandatory")


class _WfBgpAsWeightValue5_Type(Integer32):
    """Custom type wfBgpAsWeightValue5 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("default5", 8)
    )


_WfBgpAsWeightValue5_Type.__name__ = "Integer32"
_WfBgpAsWeightValue5_Object = MibTableColumn
wfBgpAsWeightValue5 = _WfBgpAsWeightValue5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 9),
    _WfBgpAsWeightValue5_Type()
)
wfBgpAsWeightValue5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue5.setStatus("mandatory")


class _WfBgpAsWeightValue6_Type(Integer32):
    """Custom type wfBgpAsWeightValue6 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("default6", 8)
    )


_WfBgpAsWeightValue6_Type.__name__ = "Integer32"
_WfBgpAsWeightValue6_Object = MibTableColumn
wfBgpAsWeightValue6 = _WfBgpAsWeightValue6_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 10),
    _WfBgpAsWeightValue6_Type()
)
wfBgpAsWeightValue6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue6.setStatus("mandatory")


class _WfBgpAsWeightValue7_Type(Integer32):
    """Custom type wfBgpAsWeightValue7 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("default7", 8)
    )


_WfBgpAsWeightValue7_Type.__name__ = "Integer32"
_WfBgpAsWeightValue7_Object = MibTableColumn
wfBgpAsWeightValue7 = _WfBgpAsWeightValue7_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 11),
    _WfBgpAsWeightValue7_Type()
)
wfBgpAsWeightValue7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue7.setStatus("mandatory")


class _WfBgpAsWeightValue8_Type(Integer32):
    """Custom type wfBgpAsWeightValue8 based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            8
        )
    )
    namedValues = NamedValues(
        ("default8", 8)
    )


_WfBgpAsWeightValue8_Type.__name__ = "Integer32"
_WfBgpAsWeightValue8_Object = MibTableColumn
wfBgpAsWeightValue8 = _WfBgpAsWeightValue8_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 3, 1, 12),
    _WfBgpAsWeightValue8_Type()
)
wfBgpAsWeightValue8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpAsWeightValue8.setStatus("mandatory")
_WfBgpPathAttrTable_Object = MibTable
wfBgpPathAttrTable = _WfBgpPathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4)
)
if mibBuilder.loadTexts:
    wfBgpPathAttrTable.setStatus("obsolete")
_WfBgpPathAttrEntry_Object = MibTableRow
wfBgpPathAttrEntry = _WfBgpPathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1)
)
wfBgpPathAttrEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgpPathAttrIpAddrPrefix"),
    (0, "Wellfleet-BGP-MIB", "wfBgpPathAttrIpAddrPrefixLen"),
    (0, "Wellfleet-BGP-MIB", "wfBgpPathAttrPeer"),
)
if mibBuilder.loadTexts:
    wfBgpPathAttrEntry.setStatus("obsolete")
_WfBgpPathAttrIpAddrPrefix_Type = IpAddress
_WfBgpPathAttrIpAddrPrefix_Object = MibTableColumn
wfBgpPathAttrIpAddrPrefix = _WfBgpPathAttrIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 1),
    _WfBgpPathAttrIpAddrPrefix_Type()
)
wfBgpPathAttrIpAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrIpAddrPrefix.setStatus("obsolete")
_WfBgpPathAttrIpAddrPrefixLen_Type = Integer32
_WfBgpPathAttrIpAddrPrefixLen_Object = MibTableColumn
wfBgpPathAttrIpAddrPrefixLen = _WfBgpPathAttrIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 2),
    _WfBgpPathAttrIpAddrPrefixLen_Type()
)
wfBgpPathAttrIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrIpAddrPrefixLen.setStatus("obsolete")
_WfBgpPathAttrPeer_Type = IpAddress
_WfBgpPathAttrPeer_Object = MibTableColumn
wfBgpPathAttrPeer = _WfBgpPathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 3),
    _WfBgpPathAttrPeer_Type()
)
wfBgpPathAttrPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrPeer.setStatus("obsolete")


class _WfBgpPathAttrOrigin_Type(Integer32):
    """Custom type wfBgpPathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_WfBgpPathAttrOrigin_Type.__name__ = "Integer32"
_WfBgpPathAttrOrigin_Object = MibTableColumn
wfBgpPathAttrOrigin = _WfBgpPathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 4),
    _WfBgpPathAttrOrigin_Type()
)
wfBgpPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrOrigin.setStatus("obsolete")
_WfBgpPathAttrASPathSegment_Type = OctetString
_WfBgpPathAttrASPathSegment_Object = MibTableColumn
wfBgpPathAttrASPathSegment = _WfBgpPathAttrASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 5),
    _WfBgpPathAttrASPathSegment_Type()
)
wfBgpPathAttrASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrASPathSegment.setStatus("obsolete")
_WfBgpPathAttrNextHop_Type = IpAddress
_WfBgpPathAttrNextHop_Object = MibTableColumn
wfBgpPathAttrNextHop = _WfBgpPathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 6),
    _WfBgpPathAttrNextHop_Type()
)
wfBgpPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrNextHop.setStatus("obsolete")
_WfBgpPathAttrMultiExitDisc_Type = Integer32
_WfBgpPathAttrMultiExitDisc_Object = MibTableColumn
wfBgpPathAttrMultiExitDisc = _WfBgpPathAttrMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 7),
    _WfBgpPathAttrMultiExitDisc_Type()
)
wfBgpPathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrMultiExitDisc.setStatus("obsolete")
_WfBgpPathAttrLocalPref_Type = Integer32
_WfBgpPathAttrLocalPref_Object = MibTableColumn
wfBgpPathAttrLocalPref = _WfBgpPathAttrLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 8),
    _WfBgpPathAttrLocalPref_Type()
)
wfBgpPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrLocalPref.setStatus("obsolete")


class _WfBgpPathAttrAtomicAggregate_Type(Integer32):
    """Custom type wfBgpPathAttrAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfBgpPathAttrAtomicAggregate_Type.__name__ = "Integer32"
_WfBgpPathAttrAtomicAggregate_Object = MibTableColumn
wfBgpPathAttrAtomicAggregate = _WfBgpPathAttrAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 9),
    _WfBgpPathAttrAtomicAggregate_Type()
)
wfBgpPathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrAtomicAggregate.setStatus("obsolete")
_WfBgpPathAttrAggregatorAS_Type = Integer32
_WfBgpPathAttrAggregatorAS_Object = MibTableColumn
wfBgpPathAttrAggregatorAS = _WfBgpPathAttrAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 10),
    _WfBgpPathAttrAggregatorAS_Type()
)
wfBgpPathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrAggregatorAS.setStatus("obsolete")
_WfBgpPathAttrAggregatorAddr_Type = IpAddress
_WfBgpPathAttrAggregatorAddr_Object = MibTableColumn
wfBgpPathAttrAggregatorAddr = _WfBgpPathAttrAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 11),
    _WfBgpPathAttrAggregatorAddr_Type()
)
wfBgpPathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrAggregatorAddr.setStatus("obsolete")
_WfBgpPathAttrCalcLocalPref_Type = Integer32
_WfBgpPathAttrCalcLocalPref_Object = MibTableColumn
wfBgpPathAttrCalcLocalPref = _WfBgpPathAttrCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 12),
    _WfBgpPathAttrCalcLocalPref_Type()
)
wfBgpPathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrCalcLocalPref.setStatus("obsolete")


class _WfBgpPathAttrBest_Type(Integer32):
    """Custom type wfBgpPathAttrBest based on Integer32"""
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
        *(("bestused", 3),
          ("false", 1),
          ("true", 2),
          ("used", 4))
    )


_WfBgpPathAttrBest_Type.__name__ = "Integer32"
_WfBgpPathAttrBest_Object = MibTableColumn
wfBgpPathAttrBest = _WfBgpPathAttrBest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 13),
    _WfBgpPathAttrBest_Type()
)
wfBgpPathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrBest.setStatus("obsolete")
_WfBgpPathAttrUnknown_Type = OctetString
_WfBgpPathAttrUnknown_Object = MibTableColumn
wfBgpPathAttrUnknown = _WfBgpPathAttrUnknown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 14),
    _WfBgpPathAttrUnknown_Type()
)
wfBgpPathAttrUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrUnknown.setStatus("obsolete")
_WfBgpPathAttrImporterID_Type = IpAddress
_WfBgpPathAttrImporterID_Object = MibTableColumn
wfBgpPathAttrImporterID = _WfBgpPathAttrImporterID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 15),
    _WfBgpPathAttrImporterID_Type()
)
wfBgpPathAttrImporterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrImporterID.setStatus("obsolete")
_WfBgpPathAttrClusterID_Type = OctetString
_WfBgpPathAttrClusterID_Object = MibTableColumn
wfBgpPathAttrClusterID = _WfBgpPathAttrClusterID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 16),
    _WfBgpPathAttrClusterID_Type()
)
wfBgpPathAttrClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrClusterID.setStatus("obsolete")
_WfBgpPathAttrCommunity_Type = OctetString
_WfBgpPathAttrCommunity_Object = MibTableColumn
wfBgpPathAttrCommunity = _WfBgpPathAttrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 17),
    _WfBgpPathAttrCommunity_Type()
)
wfBgpPathAttrCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrCommunity.setStatus("obsolete")
_WfBgpPathAttrCalcMED_Type = Integer32
_WfBgpPathAttrCalcMED_Object = MibTableColumn
wfBgpPathAttrCalcMED = _WfBgpPathAttrCalcMED_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 4, 1, 18),
    _WfBgpPathAttrCalcMED_Type()
)
wfBgpPathAttrCalcMED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttrCalcMED.setStatus("obsolete")
_WfBgpDbgTable_Object = MibTable
wfBgpDbgTable = _WfBgpDbgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5)
)
if mibBuilder.loadTexts:
    wfBgpDbgTable.setStatus("mandatory")
_WfBgpDbgEntry_Object = MibTableRow
wfBgpDbgEntry = _WfBgpDbgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1)
)
wfBgpDbgEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgpDbgLocAddr"),
    (0, "Wellfleet-BGP-MIB", "wfBgpDbgRemoteAddr"),
)
if mibBuilder.loadTexts:
    wfBgpDbgEntry.setStatus("mandatory")


class _WfBgpDbgCreate_Type(Integer32):
    """Custom type wfBgpDbgCreate based on Integer32"""
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


_WfBgpDbgCreate_Type.__name__ = "Integer32"
_WfBgpDbgCreate_Object = MibTableColumn
wfBgpDbgCreate = _WfBgpDbgCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 1),
    _WfBgpDbgCreate_Type()
)
wfBgpDbgCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDbgCreate.setStatus("mandatory")
_WfBgpDbgLocAddr_Type = IpAddress
_WfBgpDbgLocAddr_Object = MibTableColumn
wfBgpDbgLocAddr = _WfBgpDbgLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 2),
    _WfBgpDbgLocAddr_Type()
)
wfBgpDbgLocAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpDbgLocAddr.setStatus("mandatory")
_WfBgpDbgRemoteAddr_Type = IpAddress
_WfBgpDbgRemoteAddr_Object = MibTableColumn
wfBgpDbgRemoteAddr = _WfBgpDbgRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 3),
    _WfBgpDbgRemoteAddr_Type()
)
wfBgpDbgRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDbgRemoteAddr.setStatus("mandatory")


class _WfBgpDbgMsgLevel_Type(Integer32):
    """Custom type wfBgpDbgMsgLevel based on Integer32"""
    defaultValue = 2031616

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65536,
              131072,
              262144,
              524288,
              1048576,
              2031616)
        )
    )
    namedValues = NamedValues(
        *(("all", 2031616),
          ("debug", 65536),
          ("fault", 524288),
          ("info", 131072),
          ("trace", 1048576),
          ("warning", 262144))
    )


_WfBgpDbgMsgLevel_Type.__name__ = "Integer32"
_WfBgpDbgMsgLevel_Object = MibTableColumn
wfBgpDbgMsgLevel = _WfBgpDbgMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 4),
    _WfBgpDbgMsgLevel_Type()
)
wfBgpDbgMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDbgMsgLevel.setStatus("mandatory")


class _WfBgpDbgMsgTraceSwitch_Type(Integer32):
    """Custom type wfBgpDbgMsgTraceSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              16,
              32,
              64,
              128)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("keepalive", 128),
          ("notification", 64),
          ("open", 16),
          ("update", 32))
    )


_WfBgpDbgMsgTraceSwitch_Type.__name__ = "Integer32"
_WfBgpDbgMsgTraceSwitch_Object = MibTableColumn
wfBgpDbgMsgTraceSwitch = _WfBgpDbgMsgTraceSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 5),
    _WfBgpDbgMsgTraceSwitch_Type()
)
wfBgpDbgMsgTraceSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDbgMsgTraceSwitch.setStatus("mandatory")
_WfBgpDbgLogCode_Type = Integer32
_WfBgpDbgLogCode_Object = MibTableColumn
wfBgpDbgLogCode = _WfBgpDbgLogCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 6),
    _WfBgpDbgLogCode_Type()
)
wfBgpDbgLogCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDbgLogCode.setStatus("mandatory")


class _WfBgpDbgLogCodeDisable_Type(Integer32):
    """Custom type wfBgpDbgLogCodeDisable based on Integer32"""
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


_WfBgpDbgLogCodeDisable_Type.__name__ = "Integer32"
_WfBgpDbgLogCodeDisable_Object = MibTableColumn
wfBgpDbgLogCodeDisable = _WfBgpDbgLogCodeDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 7),
    _WfBgpDbgLogCodeDisable_Type()
)
wfBgpDbgLogCodeDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDbgLogCodeDisable.setStatus("mandatory")
_WfBgpDbgCodes_Type = OctetString
_WfBgpDbgCodes_Object = MibTableColumn
wfBgpDbgCodes = _WfBgpDbgCodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 8),
    _WfBgpDbgCodes_Type()
)
wfBgpDbgCodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpDbgCodes.setStatus("mandatory")
_WfBgpDbgBootCodes_Type = OctetString
_WfBgpDbgBootCodes_Object = MibTableColumn
wfBgpDbgBootCodes = _WfBgpDbgBootCodes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 5, 1, 9),
    _WfBgpDbgBootCodes_Type()
)
wfBgpDbgBootCodes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpDbgBootCodes.setStatus("mandatory")
_WfBgpVirtualPeerTable_Object = MibTable
wfBgpVirtualPeerTable = _WfBgpVirtualPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6)
)
if mibBuilder.loadTexts:
    wfBgpVirtualPeerTable.setStatus("mandatory")
_WfBgpVirtualPeerEntry_Object = MibTableRow
wfBgpVirtualPeerEntry = _WfBgpVirtualPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6, 1)
)
wfBgpVirtualPeerEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgpVirtualPeerIdentifier"),
    (0, "Wellfleet-BGP-MIB", "wfBgpVirtualPeerLocalAddr"),
    (0, "Wellfleet-BGP-MIB", "wfBgpVirtualPeerRemoteAddr"),
)
if mibBuilder.loadTexts:
    wfBgpVirtualPeerEntry.setStatus("mandatory")
_WfBgpVirtualPeerLocalAddr_Type = IpAddress
_WfBgpVirtualPeerLocalAddr_Object = MibTableColumn
wfBgpVirtualPeerLocalAddr = _WfBgpVirtualPeerLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6, 1, 1),
    _WfBgpVirtualPeerLocalAddr_Type()
)
wfBgpVirtualPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpVirtualPeerLocalAddr.setStatus("mandatory")
_WfBgpVirtualPeerRemoteAddr_Type = IpAddress
_WfBgpVirtualPeerRemoteAddr_Object = MibTableColumn
wfBgpVirtualPeerRemoteAddr = _WfBgpVirtualPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6, 1, 2),
    _WfBgpVirtualPeerRemoteAddr_Type()
)
wfBgpVirtualPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpVirtualPeerRemoteAddr.setStatus("mandatory")
_WfBgpVirtualPeerIdentifier_Type = IpAddress
_WfBgpVirtualPeerIdentifier_Object = MibTableColumn
wfBgpVirtualPeerIdentifier = _WfBgpVirtualPeerIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6, 1, 3),
    _WfBgpVirtualPeerIdentifier_Type()
)
wfBgpVirtualPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpVirtualPeerIdentifier.setStatus("mandatory")
_WfBgpVirtualPeerInUpdates_Type = Counter32
_WfBgpVirtualPeerInUpdates_Object = MibTableColumn
wfBgpVirtualPeerInUpdates = _WfBgpVirtualPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6, 1, 4),
    _WfBgpVirtualPeerInUpdates_Type()
)
wfBgpVirtualPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpVirtualPeerInUpdates.setStatus("mandatory")
_WfBgpVirtualPeerTotalRoutes_Type = Counter32
_WfBgpVirtualPeerTotalRoutes_Object = MibTableColumn
wfBgpVirtualPeerTotalRoutes = _WfBgpVirtualPeerTotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6, 1, 5),
    _WfBgpVirtualPeerTotalRoutes_Type()
)
wfBgpVirtualPeerTotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpVirtualPeerTotalRoutes.setStatus("mandatory")
_WfBgpVirtualPeerInUpdateElapsedTime_Type = Gauge32
_WfBgpVirtualPeerInUpdateElapsedTime_Object = MibTableColumn
wfBgpVirtualPeerInUpdateElapsedTime = _WfBgpVirtualPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 6, 1, 6),
    _WfBgpVirtualPeerInUpdateElapsedTime_Type()
)
wfBgpVirtualPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpVirtualPeerInUpdateElapsedTime.setStatus("mandatory")
_WfBgpPathAttributeTable_Object = MibTable
wfBgpPathAttributeTable = _WfBgpPathAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7)
)
if mibBuilder.loadTexts:
    wfBgpPathAttributeTable.setStatus("mandatory")
_WfBgpPathAttributeEntry_Object = MibTableRow
wfBgpPathAttributeEntry = _WfBgpPathAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1)
)
wfBgpPathAttributeEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgpPathAttributeIpAddrPrefix"),
    (0, "Wellfleet-BGP-MIB", "wfBgpPathAttributeIpAddrPrefixLen"),
    (0, "Wellfleet-BGP-MIB", "wfBgpPathAttributeImporterID"),
    (0, "Wellfleet-BGP-MIB", "wfBgpPathAttributePeer"),
)
if mibBuilder.loadTexts:
    wfBgpPathAttributeEntry.setStatus("mandatory")
_WfBgpPathAttributeIpAddrPrefix_Type = IpAddress
_WfBgpPathAttributeIpAddrPrefix_Object = MibTableColumn
wfBgpPathAttributeIpAddrPrefix = _WfBgpPathAttributeIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 1),
    _WfBgpPathAttributeIpAddrPrefix_Type()
)
wfBgpPathAttributeIpAddrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeIpAddrPrefix.setStatus("mandatory")
_WfBgpPathAttributeIpAddrPrefixLen_Type = Integer32
_WfBgpPathAttributeIpAddrPrefixLen_Object = MibTableColumn
wfBgpPathAttributeIpAddrPrefixLen = _WfBgpPathAttributeIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 2),
    _WfBgpPathAttributeIpAddrPrefixLen_Type()
)
wfBgpPathAttributeIpAddrPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeIpAddrPrefixLen.setStatus("mandatory")
_WfBgpPathAttributeImporterID_Type = IpAddress
_WfBgpPathAttributeImporterID_Object = MibTableColumn
wfBgpPathAttributeImporterID = _WfBgpPathAttributeImporterID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 3),
    _WfBgpPathAttributeImporterID_Type()
)
wfBgpPathAttributeImporterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeImporterID.setStatus("mandatory")
_WfBgpPathAttributePeer_Type = IpAddress
_WfBgpPathAttributePeer_Object = MibTableColumn
wfBgpPathAttributePeer = _WfBgpPathAttributePeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 4),
    _WfBgpPathAttributePeer_Type()
)
wfBgpPathAttributePeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributePeer.setStatus("mandatory")


class _WfBgpPathAttributeOrigin_Type(Integer32):
    """Custom type wfBgpPathAttributeOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_WfBgpPathAttributeOrigin_Type.__name__ = "Integer32"
_WfBgpPathAttributeOrigin_Object = MibTableColumn
wfBgpPathAttributeOrigin = _WfBgpPathAttributeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 5),
    _WfBgpPathAttributeOrigin_Type()
)
wfBgpPathAttributeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeOrigin.setStatus("mandatory")
_WfBgpPathAttributeASPathSegment_Type = OctetString
_WfBgpPathAttributeASPathSegment_Object = MibTableColumn
wfBgpPathAttributeASPathSegment = _WfBgpPathAttributeASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 6),
    _WfBgpPathAttributeASPathSegment_Type()
)
wfBgpPathAttributeASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeASPathSegment.setStatus("mandatory")
_WfBgpPathAttributeNextHop_Type = IpAddress
_WfBgpPathAttributeNextHop_Object = MibTableColumn
wfBgpPathAttributeNextHop = _WfBgpPathAttributeNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 7),
    _WfBgpPathAttributeNextHop_Type()
)
wfBgpPathAttributeNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeNextHop.setStatus("mandatory")
_WfBgpPathAttributeMultiExitDisc_Type = Integer32
_WfBgpPathAttributeMultiExitDisc_Object = MibTableColumn
wfBgpPathAttributeMultiExitDisc = _WfBgpPathAttributeMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 8),
    _WfBgpPathAttributeMultiExitDisc_Type()
)
wfBgpPathAttributeMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeMultiExitDisc.setStatus("mandatory")
_WfBgpPathAttributeLocalPref_Type = Integer32
_WfBgpPathAttributeLocalPref_Object = MibTableColumn
wfBgpPathAttributeLocalPref = _WfBgpPathAttributeLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 9),
    _WfBgpPathAttributeLocalPref_Type()
)
wfBgpPathAttributeLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeLocalPref.setStatus("mandatory")


class _WfBgpPathAttributeAtomicAggregate_Type(Integer32):
    """Custom type wfBgpPathAttributeAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfBgpPathAttributeAtomicAggregate_Type.__name__ = "Integer32"
_WfBgpPathAttributeAtomicAggregate_Object = MibTableColumn
wfBgpPathAttributeAtomicAggregate = _WfBgpPathAttributeAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 10),
    _WfBgpPathAttributeAtomicAggregate_Type()
)
wfBgpPathAttributeAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeAtomicAggregate.setStatus("mandatory")
_WfBgpPathAttributeAggregatorAS_Type = Integer32
_WfBgpPathAttributeAggregatorAS_Object = MibTableColumn
wfBgpPathAttributeAggregatorAS = _WfBgpPathAttributeAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 11),
    _WfBgpPathAttributeAggregatorAS_Type()
)
wfBgpPathAttributeAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeAggregatorAS.setStatus("mandatory")
_WfBgpPathAttributeAggregatorAddr_Type = IpAddress
_WfBgpPathAttributeAggregatorAddr_Object = MibTableColumn
wfBgpPathAttributeAggregatorAddr = _WfBgpPathAttributeAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 12),
    _WfBgpPathAttributeAggregatorAddr_Type()
)
wfBgpPathAttributeAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeAggregatorAddr.setStatus("mandatory")
_WfBgpPathAttributeCalcLocalPref_Type = Integer32
_WfBgpPathAttributeCalcLocalPref_Object = MibTableColumn
wfBgpPathAttributeCalcLocalPref = _WfBgpPathAttributeCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 13),
    _WfBgpPathAttributeCalcLocalPref_Type()
)
wfBgpPathAttributeCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeCalcLocalPref.setStatus("mandatory")


class _WfBgpPathAttributeBest_Type(Integer32):
    """Custom type wfBgpPathAttributeBest based on Integer32"""
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
        *(("bestused", 3),
          ("false", 1),
          ("true", 2),
          ("used", 4))
    )


_WfBgpPathAttributeBest_Type.__name__ = "Integer32"
_WfBgpPathAttributeBest_Object = MibTableColumn
wfBgpPathAttributeBest = _WfBgpPathAttributeBest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 14),
    _WfBgpPathAttributeBest_Type()
)
wfBgpPathAttributeBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeBest.setStatus("mandatory")
_WfBgpPathAttributeUnknown_Type = OctetString
_WfBgpPathAttributeUnknown_Object = MibTableColumn
wfBgpPathAttributeUnknown = _WfBgpPathAttributeUnknown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 15),
    _WfBgpPathAttributeUnknown_Type()
)
wfBgpPathAttributeUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeUnknown.setStatus("mandatory")
_WfBgpPathAttributeClusterID_Type = OctetString
_WfBgpPathAttributeClusterID_Object = MibTableColumn
wfBgpPathAttributeClusterID = _WfBgpPathAttributeClusterID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 16),
    _WfBgpPathAttributeClusterID_Type()
)
wfBgpPathAttributeClusterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeClusterID.setStatus("mandatory")
_WfBgpPathAttributeCommunity_Type = OctetString
_WfBgpPathAttributeCommunity_Object = MibTableColumn
wfBgpPathAttributeCommunity = _WfBgpPathAttributeCommunity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 17),
    _WfBgpPathAttributeCommunity_Type()
)
wfBgpPathAttributeCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeCommunity.setStatus("mandatory")
_WfBgpPathAttributeCalcMED_Type = Integer32
_WfBgpPathAttributeCalcMED_Object = MibTableColumn
wfBgpPathAttributeCalcMED = _WfBgpPathAttributeCalcMED_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 18),
    _WfBgpPathAttributeCalcMED_Type()
)
wfBgpPathAttributeCalcMED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeCalcMED.setStatus("mandatory")
_WfBgpPathAttributeFlapPenalty_Type = Integer32
_WfBgpPathAttributeFlapPenalty_Object = MibTableColumn
wfBgpPathAttributeFlapPenalty = _WfBgpPathAttributeFlapPenalty_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 19),
    _WfBgpPathAttributeFlapPenalty_Type()
)
wfBgpPathAttributeFlapPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeFlapPenalty.setStatus("mandatory")
_WfBgpPathAttributeFlapCount_Type = Integer32
_WfBgpPathAttributeFlapCount_Object = MibTableColumn
wfBgpPathAttributeFlapCount = _WfBgpPathAttributeFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 20),
    _WfBgpPathAttributeFlapCount_Type()
)
wfBgpPathAttributeFlapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeFlapCount.setStatus("mandatory")


class _WfBgpPathAttributeRouteDampened_Type(Integer32):
    """Custom type wfBgpPathAttributeRouteDampened based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("announced", 1),
          ("suppressed", 2))
    )


_WfBgpPathAttributeRouteDampened_Type.__name__ = "Integer32"
_WfBgpPathAttributeRouteDampened_Object = MibTableColumn
wfBgpPathAttributeRouteDampened = _WfBgpPathAttributeRouteDampened_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 7, 1, 21),
    _WfBgpPathAttributeRouteDampened_Type()
)
wfBgpPathAttributeRouteDampened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpPathAttributeRouteDampened.setStatus("mandatory")
_WfBgpRouteFlapDampeningTable_Object = MibTable
wfBgpRouteFlapDampeningTable = _WfBgpRouteFlapDampeningTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8)
)
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningTable.setStatus("mandatory")
_WfBgpRouteFlapDampeningEntry_Object = MibTableRow
wfBgpRouteFlapDampeningEntry = _WfBgpRouteFlapDampeningEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1)
)
wfBgpRouteFlapDampeningEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgpRouteFlapDampeningIndex"),
)
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningEntry.setStatus("mandatory")


class _WfBgpRouteFlapDampeningDelete_Type(Integer32):
    """Custom type wfBgpRouteFlapDampeningDelete based on Integer32"""
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


_WfBgpRouteFlapDampeningDelete_Type.__name__ = "Integer32"
_WfBgpRouteFlapDampeningDelete_Object = MibTableColumn
wfBgpRouteFlapDampeningDelete = _WfBgpRouteFlapDampeningDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 1),
    _WfBgpRouteFlapDampeningDelete_Type()
)
wfBgpRouteFlapDampeningDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningDelete.setStatus("mandatory")
_WfBgpRouteFlapDampeningIndex_Type = Integer32
_WfBgpRouteFlapDampeningIndex_Object = MibTableColumn
wfBgpRouteFlapDampeningIndex = _WfBgpRouteFlapDampeningIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 2),
    _WfBgpRouteFlapDampeningIndex_Type()
)
wfBgpRouteFlapDampeningIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningIndex.setStatus("mandatory")
_WfBgpRouteFlapDampeningName_Type = DisplayString
_WfBgpRouteFlapDampeningName_Object = MibTableColumn
wfBgpRouteFlapDampeningName = _WfBgpRouteFlapDampeningName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 3),
    _WfBgpRouteFlapDampeningName_Type()
)
wfBgpRouteFlapDampeningName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningName.setStatus("mandatory")


class _WfBgpRouteFlapDampeningCutoffThreshold_Type(Integer32):
    """Custom type wfBgpRouteFlapDampeningCutoffThreshold based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_WfBgpRouteFlapDampeningCutoffThreshold_Type.__name__ = "Integer32"
_WfBgpRouteFlapDampeningCutoffThreshold_Object = MibTableColumn
wfBgpRouteFlapDampeningCutoffThreshold = _WfBgpRouteFlapDampeningCutoffThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 4),
    _WfBgpRouteFlapDampeningCutoffThreshold_Type()
)
wfBgpRouteFlapDampeningCutoffThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningCutoffThreshold.setStatus("mandatory")


class _WfBgpRouteFlapDampeningReuseThreshold_Type(Integer32):
    """Custom type wfBgpRouteFlapDampeningReuseThreshold based on Integer32"""
    defaultValue = 750

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_WfBgpRouteFlapDampeningReuseThreshold_Type.__name__ = "Integer32"
_WfBgpRouteFlapDampeningReuseThreshold_Object = MibTableColumn
wfBgpRouteFlapDampeningReuseThreshold = _WfBgpRouteFlapDampeningReuseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 5),
    _WfBgpRouteFlapDampeningReuseThreshold_Type()
)
wfBgpRouteFlapDampeningReuseThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningReuseThreshold.setStatus("mandatory")


class _WfBgpRouteFlapDampeningReachableDecay_Type(Integer32):
    """Custom type wfBgpRouteFlapDampeningReachableDecay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45),
    )


_WfBgpRouteFlapDampeningReachableDecay_Type.__name__ = "Integer32"
_WfBgpRouteFlapDampeningReachableDecay_Object = MibTableColumn
wfBgpRouteFlapDampeningReachableDecay = _WfBgpRouteFlapDampeningReachableDecay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 6),
    _WfBgpRouteFlapDampeningReachableDecay_Type()
)
wfBgpRouteFlapDampeningReachableDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningReachableDecay.setStatus("mandatory")


class _WfBgpRouteFlapDampeningUnreachableDecay_Type(Integer32):
    """Custom type wfBgpRouteFlapDampeningUnreachableDecay based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45),
    )


_WfBgpRouteFlapDampeningUnreachableDecay_Type.__name__ = "Integer32"
_WfBgpRouteFlapDampeningUnreachableDecay_Object = MibTableColumn
wfBgpRouteFlapDampeningUnreachableDecay = _WfBgpRouteFlapDampeningUnreachableDecay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 7),
    _WfBgpRouteFlapDampeningUnreachableDecay_Type()
)
wfBgpRouteFlapDampeningUnreachableDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningUnreachableDecay.setStatus("mandatory")


class _WfBgpRouteFlapDampeningMaxHoldDown_Type(Integer32):
    """Custom type wfBgpRouteFlapDampeningMaxHoldDown based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfBgpRouteFlapDampeningMaxHoldDown_Type.__name__ = "Integer32"
_WfBgpRouteFlapDampeningMaxHoldDown_Object = MibTableColumn
wfBgpRouteFlapDampeningMaxHoldDown = _WfBgpRouteFlapDampeningMaxHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 8),
    _WfBgpRouteFlapDampeningMaxHoldDown_Type()
)
wfBgpRouteFlapDampeningMaxHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningMaxHoldDown.setStatus("mandatory")


class _WfBgpRouteFlapDampeningMemoryLimit_Type(Integer32):
    """Custom type wfBgpRouteFlapDampeningMemoryLimit based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WfBgpRouteFlapDampeningMemoryLimit_Type.__name__ = "Integer32"
_WfBgpRouteFlapDampeningMemoryLimit_Object = MibTableColumn
wfBgpRouteFlapDampeningMemoryLimit = _WfBgpRouteFlapDampeningMemoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 1, 8, 1, 9),
    _WfBgpRouteFlapDampeningMemoryLimit_Type()
)
wfBgpRouteFlapDampeningMemoryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgpRouteFlapDampeningMemoryLimit.setStatus("mandatory")
_WfBgp3Group_ObjectIdentity = ObjectIdentity
wfBgp3Group = _WfBgp3Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2)
)
_WfBgp3_ObjectIdentity = ObjectIdentity
wfBgp3 = _WfBgp3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1)
)


class _WfBgp3Delete_Type(Integer32):
    """Custom type wfBgp3Delete based on Integer32"""
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


_WfBgp3Delete_Type.__name__ = "Integer32"
_WfBgp3Delete_Object = MibScalar
wfBgp3Delete = _WfBgp3Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 1),
    _WfBgp3Delete_Type()
)
wfBgp3Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgp3Delete.setStatus("mandatory")


class _WfBgp3Disable_Type(Integer32):
    """Custom type wfBgp3Disable based on Integer32"""
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


_WfBgp3Disable_Type.__name__ = "Integer32"
_WfBgp3Disable_Object = MibScalar
wfBgp3Disable = _WfBgp3Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 2),
    _WfBgp3Disable_Type()
)
wfBgp3Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgp3Disable.setStatus("mandatory")


class _WfBgp3State_Type(Integer32):
    """Custom type wfBgp3State based on Integer32"""
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
          ("notpresent", 5),
          ("up", 1))
    )


_WfBgp3State_Type.__name__ = "Integer32"
_WfBgp3State_Object = MibScalar
wfBgp3State = _WfBgp3State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 3),
    _WfBgp3State_Type()
)
wfBgp3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3State.setStatus("mandatory")


class _WfBgp3IntraAsIbgpRouting_Type(Integer32):
    """Custom type wfBgp3IntraAsIbgpRouting based on Integer32"""
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


_WfBgp3IntraAsIbgpRouting_Type.__name__ = "Integer32"
_WfBgp3IntraAsIbgpRouting_Object = MibScalar
wfBgp3IntraAsIbgpRouting = _WfBgp3IntraAsIbgpRouting_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 4),
    _WfBgp3IntraAsIbgpRouting_Type()
)
wfBgp3IntraAsIbgpRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgp3IntraAsIbgpRouting.setStatus("obsolete")


class _WfBgp3IntAdvTimer_Type(Integer32):
    """Custom type wfBgp3IntAdvTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfBgp3IntAdvTimer_Type.__name__ = "Integer32"
_WfBgp3IntAdvTimer_Object = MibScalar
wfBgp3IntAdvTimer = _WfBgp3IntAdvTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 5),
    _WfBgp3IntAdvTimer_Type()
)
wfBgp3IntAdvTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgp3IntAdvTimer.setStatus("obsolete")


class _WfBgp3RipRules_Type(Integer32):
    """Custom type wfBgp3RipRules based on Integer32"""
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


_WfBgp3RipRules_Type.__name__ = "Integer32"
_WfBgp3RipRules_Object = MibScalar
wfBgp3RipRules = _WfBgp3RipRules_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 6),
    _WfBgp3RipRules_Type()
)
wfBgp3RipRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgp3RipRules.setStatus("obsolete")
_WfBgp3UsedRoutes_Type = Counter32
_WfBgp3UsedRoutes_Object = MibScalar
wfBgp3UsedRoutes = _WfBgp3UsedRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 7),
    _WfBgp3UsedRoutes_Type()
)
wfBgp3UsedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3UsedRoutes.setStatus("obsolete")
_WfBgp3TotalRoutes_Type = Counter32
_WfBgp3TotalRoutes_Object = MibScalar
wfBgp3TotalRoutes = _WfBgp3TotalRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 1, 8),
    _WfBgp3TotalRoutes_Type()
)
wfBgp3TotalRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3TotalRoutes.setStatus("obsolete")
_WfBgp3PathAttrTable_Object = MibTable
wfBgp3PathAttrTable = _WfBgp3PathAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2)
)
if mibBuilder.loadTexts:
    wfBgp3PathAttrTable.setStatus("obsolete")
_WfBgp3PathAttrEntry_Object = MibTableRow
wfBgp3PathAttrEntry = _WfBgp3PathAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1)
)
wfBgp3PathAttrEntry.setIndexNames(
    (0, "Wellfleet-BGP-MIB", "wfBgp3PathAttrDestNetwork"),
    (0, "Wellfleet-BGP-MIB", "wfBgp3PathAttrPeer"),
)
if mibBuilder.loadTexts:
    wfBgp3PathAttrEntry.setStatus("obsolete")
_WfBgp3PathAttrPeer_Type = IpAddress
_WfBgp3PathAttrPeer_Object = MibTableColumn
wfBgp3PathAttrPeer = _WfBgp3PathAttrPeer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 1),
    _WfBgp3PathAttrPeer_Type()
)
wfBgp3PathAttrPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrPeer.setStatus("obsolete")
_WfBgp3PathAttrDestNetwork_Type = IpAddress
_WfBgp3PathAttrDestNetwork_Object = MibTableColumn
wfBgp3PathAttrDestNetwork = _WfBgp3PathAttrDestNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 2),
    _WfBgp3PathAttrDestNetwork_Type()
)
wfBgp3PathAttrDestNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrDestNetwork.setStatus("obsolete")


class _WfBgp3PathAttrOrigin_Type(Integer32):
    """Custom type wfBgp3PathAttrOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_WfBgp3PathAttrOrigin_Type.__name__ = "Integer32"
_WfBgp3PathAttrOrigin_Object = MibTableColumn
wfBgp3PathAttrOrigin = _WfBgp3PathAttrOrigin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 3),
    _WfBgp3PathAttrOrigin_Type()
)
wfBgp3PathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrOrigin.setStatus("obsolete")
_WfBgp3PathAttrASPath_Type = OctetString
_WfBgp3PathAttrASPath_Object = MibTableColumn
wfBgp3PathAttrASPath = _WfBgp3PathAttrASPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 4),
    _WfBgp3PathAttrASPath_Type()
)
wfBgp3PathAttrASPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrASPath.setStatus("obsolete")
_WfBgp3PathAttrNextHop_Type = IpAddress
_WfBgp3PathAttrNextHop_Object = MibTableColumn
wfBgp3PathAttrNextHop = _WfBgp3PathAttrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 5),
    _WfBgp3PathAttrNextHop_Type()
)
wfBgp3PathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrNextHop.setStatus("obsolete")
_WfBgp3PathAttrInterASMetric_Type = Integer32
_WfBgp3PathAttrInterASMetric_Object = MibTableColumn
wfBgp3PathAttrInterASMetric = _WfBgp3PathAttrInterASMetric_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 6),
    _WfBgp3PathAttrInterASMetric_Type()
)
wfBgp3PathAttrInterASMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrInterASMetric.setStatus("obsolete")
_WfBgp3PathAttrASPathWeight_Type = Integer32
_WfBgp3PathAttrASPathWeight_Object = MibTableColumn
wfBgp3PathAttrASPathWeight = _WfBgp3PathAttrASPathWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 7),
    _WfBgp3PathAttrASPathWeight_Type()
)
wfBgp3PathAttrASPathWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrASPathWeight.setStatus("obsolete")
_WfBgp3PathAttrBgpPreference_Type = Integer32
_WfBgp3PathAttrBgpPreference_Object = MibTableColumn
wfBgp3PathAttrBgpPreference = _WfBgp3PathAttrBgpPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 8),
    _WfBgp3PathAttrBgpPreference_Type()
)
wfBgp3PathAttrBgpPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrBgpPreference.setStatus("obsolete")


class _WfBgp3PathAttrBest_Type(Integer32):
    """Custom type wfBgp3PathAttrBest based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_WfBgp3PathAttrBest_Type.__name__ = "Integer32"
_WfBgp3PathAttrBest_Object = MibTableColumn
wfBgp3PathAttrBest = _WfBgp3PathAttrBest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 2, 2, 1, 9),
    _WfBgp3PathAttrBest_Type()
)
wfBgp3PathAttrBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp3PathAttrBest.setStatus("obsolete")
_WfBgp4Group_ObjectIdentity = ObjectIdentity
wfBgp4Group = _WfBgp4Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 3)
)
_WfBgp4_ObjectIdentity = ObjectIdentity
wfBgp4 = _WfBgp4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 3, 1)
)


class _WfBgp4Delete_Type(Integer32):
    """Custom type wfBgp4Delete based on Integer32"""
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


_WfBgp4Delete_Type.__name__ = "Integer32"
_WfBgp4Delete_Object = MibScalar
wfBgp4Delete = _WfBgp4Delete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 3, 1, 1),
    _WfBgp4Delete_Type()
)
wfBgp4Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgp4Delete.setStatus("mandatory")


class _WfBgp4Disable_Type(Integer32):
    """Custom type wfBgp4Disable based on Integer32"""
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


_WfBgp4Disable_Type.__name__ = "Integer32"
_WfBgp4Disable_Object = MibScalar
wfBgp4Disable = _WfBgp4Disable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 3, 1, 2),
    _WfBgp4Disable_Type()
)
wfBgp4Disable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBgp4Disable.setStatus("mandatory")


class _WfBgp4State_Type(Integer32):
    """Custom type wfBgp4State based on Integer32"""
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
          ("notpresent", 5),
          ("up", 1))
    )


_WfBgp4State_Type.__name__ = "Integer32"
_WfBgp4State_Object = MibScalar
wfBgp4State = _WfBgp4State_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 5, 3, 1, 3),
    _WfBgp4State_Type()
)
wfBgp4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfBgp4State.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-BGP-MIB",
    **{"wfBgpGeneralGroup": wfBgpGeneralGroup,
       "wfBgp": wfBgp,
       "wfBgpDelete": wfBgpDelete,
       "wfBgpDisable": wfBgpDisable,
       "wfBgpState": wfBgpState,
       "wfBgpIdentifier": wfBgpIdentifier,
       "wfBgpLocalAs": wfBgpLocalAs,
       "wfBgpEbgpDebugSwitch": wfBgpEbgpDebugSwitch,
       "wfBgpVersion": wfBgpVersion,
       "wfBgpIntraAsIbgpRouting": wfBgpIntraAsIbgpRouting,
       "wfIbgpFromProtocols": wfIbgpFromProtocols,
       "wfBgpIntAdvTimer": wfBgpIntAdvTimer,
       "wfBgpUsedRoutes": wfBgpUsedRoutes,
       "wfBgpTotalRoutes": wfBgpTotalRoutes,
       "wfBgpTotalPaths": wfBgpTotalPaths,
       "wfBgpMaxRedundantIbgpRoutes": wfBgpMaxRedundantIbgpRoutes,
       "wfBgpRouteRequestSwitch": wfBgpRouteRequestSwitch,
       "wfBgpConnCollisionDetect": wfBgpConnCollisionDetect,
       "wfBgpRsTopology": wfBgpRsTopology,
       "wfBgpClusterIdentifier": wfBgpClusterIdentifier,
       "wfBgpDynamicPolChangeSupport": wfBgpDynamicPolChangeSupport,
       "wfBgpSoloistSlots": wfBgpSoloistSlots,
       "wfBgpSoloistSlot": wfBgpSoloistSlot,
       "wfBgpSubnetAggregation": wfBgpSubnetAggregation,
       "wfBgpBlackHoleSupport": wfBgpBlackHoleSupport,
       "wfBgpMedComparison": wfBgpMedComparison,
       "wfBgpIbgpReflection": wfBgpIbgpReflection,
       "wfBgpIbgpEcmpMethod": wfBgpIbgpEcmpMethod,
       "wfBgpLocalPrefCalc": wfBgpLocalPrefCalc,
       "wfBgpConfedIdentifier": wfBgpConfedIdentifier,
       "wfBgpConfedPeers": wfBgpConfedPeers,
       "wfBgpIgpInterAction": wfBgpIgpInterAction,
       "wfBgpPeerTable": wfBgpPeerTable,
       "wfBgpPeerEntry": wfBgpPeerEntry,
       "wfBgpPeerDelete": wfBgpPeerDelete,
       "wfBgpPeerDisable": wfBgpPeerDisable,
       "wfBgpPeerState": wfBgpPeerState,
       "wfBgpPeerLocalAddr": wfBgpPeerLocalAddr,
       "wfBgpPeerLocalPort": wfBgpPeerLocalPort,
       "wfBgpPeerRemoteAddr": wfBgpPeerRemoteAddr,
       "wfBgpPeerRemotePort": wfBgpPeerRemotePort,
       "wfBgpPeerMinVersion": wfBgpPeerMinVersion,
       "wfBgpPeerMaxVersion": wfBgpPeerMaxVersion,
       "wfBgpPeerRemoteAs": wfBgpPeerRemoteAs,
       "wfBgpPeerExtAdvTimer": wfBgpPeerExtAdvTimer,
       "wfBgpPeerConnectRetry": wfBgpPeerConnectRetry,
       "wfBgpPeerCfgHoldtime": wfBgpPeerCfgHoldtime,
       "wfBgpPeerHoldtime": wfBgpPeerHoldtime,
       "wfBgpPeerCfgKeepAlive": wfBgpPeerCfgKeepAlive,
       "wfBgpPeerKeepAlive": wfBgpPeerKeepAlive,
       "wfBgpPeerPathAttrSwitch": wfBgpPeerPathAttrSwitch,
       "wfBgpPeerIdentifier": wfBgpPeerIdentifier,
       "wfBgpPeerConnState": wfBgpPeerConnState,
       "wfBgpPeerNegotiatedVersion": wfBgpPeerNegotiatedVersion,
       "wfBgpPeerInUpdates": wfBgpPeerInUpdates,
       "wfBgpPeerOutUpdates": wfBgpPeerOutUpdates,
       "wfBgpPeerInTotalMessages": wfBgpPeerInTotalMessages,
       "wfBgpPeerOutTotalMessages": wfBgpPeerOutTotalMessages,
       "wfBgpPeerLastError": wfBgpPeerLastError,
       "wfBgpPeerTotalRoutes": wfBgpPeerTotalRoutes,
       "wfBgpPeerFsmEstablishedTransitions": wfBgpPeerFsmEstablishedTransitions,
       "wfBgpPeerFsmEstablishedTime": wfBgpPeerFsmEstablishedTime,
       "wfBgpPeerInUpdateElapsedTime": wfBgpPeerInUpdateElapsedTime,
       "wfBgpPeerMinASOriginationInterval": wfBgpPeerMinASOriginationInterval,
       "wfBgpPeerLocalAS": wfBgpPeerLocalAS,
       "wfBgpPeerMaxUpdateSize": wfBgpPeerMaxUpdateSize,
       "wfBgpPeerRouteEchoSwitch": wfBgpPeerRouteEchoSwitch,
       "wfBgpPeerDiscardDuplicateRouteSwitch": wfBgpPeerDiscardDuplicateRouteSwitch,
       "wfBgpPeerRSMode": wfBgpPeerRSMode,
       "wfBgpPeerRSIdentifier": wfBgpPeerRSIdentifier,
       "wfBgpPeerCfgDelayGranularity": wfBgpPeerCfgDelayGranularity,
       "wfBgpPeerDelayGranularity": wfBgpPeerDelayGranularity,
       "wfBgpPeerLastErrorSrc": wfBgpPeerLastErrorSrc,
       "wfBgpPeerNexthopSelf": wfBgpPeerNexthopSelf,
       "wfBgpPeerASLoopDetect": wfBgpPeerASLoopDetect,
       "wfBgpPeerBgpEcmpMethod": wfBgpPeerBgpEcmpMethod,
       "wfBgpPeerDampenedRoutes": wfBgpPeerDampenedRoutes,
       "wfBgpPeerTTL": wfBgpPeerTTL,
       "wfBgpPeerTcpAuthentication": wfBgpPeerTcpAuthentication,
       "wfBgpPeerTcpMd5KeyStorage": wfBgpPeerTcpMd5KeyStorage,
       "wfBgpPeerTcpMd5Key": wfBgpPeerTcpMd5Key,
       "wfBgpAsWeightTable": wfBgpAsWeightTable,
       "wfBgpAsWeightEntry": wfBgpAsWeightEntry,
       "wfBgpAsWeightDelete": wfBgpAsWeightDelete,
       "wfBgpAsWeightDisable": wfBgpAsWeightDisable,
       "wfBgpAsWeightState": wfBgpAsWeightState,
       "wfBgpAsWeightNumber": wfBgpAsWeightNumber,
       "wfBgpAsWeightValue": wfBgpAsWeightValue,
       "wfBgpAsWeightValue2": wfBgpAsWeightValue2,
       "wfBgpAsWeightValue3": wfBgpAsWeightValue3,
       "wfBgpAsWeightValue4": wfBgpAsWeightValue4,
       "wfBgpAsWeightValue5": wfBgpAsWeightValue5,
       "wfBgpAsWeightValue6": wfBgpAsWeightValue6,
       "wfBgpAsWeightValue7": wfBgpAsWeightValue7,
       "wfBgpAsWeightValue8": wfBgpAsWeightValue8,
       "wfBgpPathAttrTable": wfBgpPathAttrTable,
       "wfBgpPathAttrEntry": wfBgpPathAttrEntry,
       "wfBgpPathAttrIpAddrPrefix": wfBgpPathAttrIpAddrPrefix,
       "wfBgpPathAttrIpAddrPrefixLen": wfBgpPathAttrIpAddrPrefixLen,
       "wfBgpPathAttrPeer": wfBgpPathAttrPeer,
       "wfBgpPathAttrOrigin": wfBgpPathAttrOrigin,
       "wfBgpPathAttrASPathSegment": wfBgpPathAttrASPathSegment,
       "wfBgpPathAttrNextHop": wfBgpPathAttrNextHop,
       "wfBgpPathAttrMultiExitDisc": wfBgpPathAttrMultiExitDisc,
       "wfBgpPathAttrLocalPref": wfBgpPathAttrLocalPref,
       "wfBgpPathAttrAtomicAggregate": wfBgpPathAttrAtomicAggregate,
       "wfBgpPathAttrAggregatorAS": wfBgpPathAttrAggregatorAS,
       "wfBgpPathAttrAggregatorAddr": wfBgpPathAttrAggregatorAddr,
       "wfBgpPathAttrCalcLocalPref": wfBgpPathAttrCalcLocalPref,
       "wfBgpPathAttrBest": wfBgpPathAttrBest,
       "wfBgpPathAttrUnknown": wfBgpPathAttrUnknown,
       "wfBgpPathAttrImporterID": wfBgpPathAttrImporterID,
       "wfBgpPathAttrClusterID": wfBgpPathAttrClusterID,
       "wfBgpPathAttrCommunity": wfBgpPathAttrCommunity,
       "wfBgpPathAttrCalcMED": wfBgpPathAttrCalcMED,
       "wfBgpDbgTable": wfBgpDbgTable,
       "wfBgpDbgEntry": wfBgpDbgEntry,
       "wfBgpDbgCreate": wfBgpDbgCreate,
       "wfBgpDbgLocAddr": wfBgpDbgLocAddr,
       "wfBgpDbgRemoteAddr": wfBgpDbgRemoteAddr,
       "wfBgpDbgMsgLevel": wfBgpDbgMsgLevel,
       "wfBgpDbgMsgTraceSwitch": wfBgpDbgMsgTraceSwitch,
       "wfBgpDbgLogCode": wfBgpDbgLogCode,
       "wfBgpDbgLogCodeDisable": wfBgpDbgLogCodeDisable,
       "wfBgpDbgCodes": wfBgpDbgCodes,
       "wfBgpDbgBootCodes": wfBgpDbgBootCodes,
       "wfBgpVirtualPeerTable": wfBgpVirtualPeerTable,
       "wfBgpVirtualPeerEntry": wfBgpVirtualPeerEntry,
       "wfBgpVirtualPeerLocalAddr": wfBgpVirtualPeerLocalAddr,
       "wfBgpVirtualPeerRemoteAddr": wfBgpVirtualPeerRemoteAddr,
       "wfBgpVirtualPeerIdentifier": wfBgpVirtualPeerIdentifier,
       "wfBgpVirtualPeerInUpdates": wfBgpVirtualPeerInUpdates,
       "wfBgpVirtualPeerTotalRoutes": wfBgpVirtualPeerTotalRoutes,
       "wfBgpVirtualPeerInUpdateElapsedTime": wfBgpVirtualPeerInUpdateElapsedTime,
       "wfBgpPathAttributeTable": wfBgpPathAttributeTable,
       "wfBgpPathAttributeEntry": wfBgpPathAttributeEntry,
       "wfBgpPathAttributeIpAddrPrefix": wfBgpPathAttributeIpAddrPrefix,
       "wfBgpPathAttributeIpAddrPrefixLen": wfBgpPathAttributeIpAddrPrefixLen,
       "wfBgpPathAttributeImporterID": wfBgpPathAttributeImporterID,
       "wfBgpPathAttributePeer": wfBgpPathAttributePeer,
       "wfBgpPathAttributeOrigin": wfBgpPathAttributeOrigin,
       "wfBgpPathAttributeASPathSegment": wfBgpPathAttributeASPathSegment,
       "wfBgpPathAttributeNextHop": wfBgpPathAttributeNextHop,
       "wfBgpPathAttributeMultiExitDisc": wfBgpPathAttributeMultiExitDisc,
       "wfBgpPathAttributeLocalPref": wfBgpPathAttributeLocalPref,
       "wfBgpPathAttributeAtomicAggregate": wfBgpPathAttributeAtomicAggregate,
       "wfBgpPathAttributeAggregatorAS": wfBgpPathAttributeAggregatorAS,
       "wfBgpPathAttributeAggregatorAddr": wfBgpPathAttributeAggregatorAddr,
       "wfBgpPathAttributeCalcLocalPref": wfBgpPathAttributeCalcLocalPref,
       "wfBgpPathAttributeBest": wfBgpPathAttributeBest,
       "wfBgpPathAttributeUnknown": wfBgpPathAttributeUnknown,
       "wfBgpPathAttributeClusterID": wfBgpPathAttributeClusterID,
       "wfBgpPathAttributeCommunity": wfBgpPathAttributeCommunity,
       "wfBgpPathAttributeCalcMED": wfBgpPathAttributeCalcMED,
       "wfBgpPathAttributeFlapPenalty": wfBgpPathAttributeFlapPenalty,
       "wfBgpPathAttributeFlapCount": wfBgpPathAttributeFlapCount,
       "wfBgpPathAttributeRouteDampened": wfBgpPathAttributeRouteDampened,
       "wfBgpRouteFlapDampeningTable": wfBgpRouteFlapDampeningTable,
       "wfBgpRouteFlapDampeningEntry": wfBgpRouteFlapDampeningEntry,
       "wfBgpRouteFlapDampeningDelete": wfBgpRouteFlapDampeningDelete,
       "wfBgpRouteFlapDampeningIndex": wfBgpRouteFlapDampeningIndex,
       "wfBgpRouteFlapDampeningName": wfBgpRouteFlapDampeningName,
       "wfBgpRouteFlapDampeningCutoffThreshold": wfBgpRouteFlapDampeningCutoffThreshold,
       "wfBgpRouteFlapDampeningReuseThreshold": wfBgpRouteFlapDampeningReuseThreshold,
       "wfBgpRouteFlapDampeningReachableDecay": wfBgpRouteFlapDampeningReachableDecay,
       "wfBgpRouteFlapDampeningUnreachableDecay": wfBgpRouteFlapDampeningUnreachableDecay,
       "wfBgpRouteFlapDampeningMaxHoldDown": wfBgpRouteFlapDampeningMaxHoldDown,
       "wfBgpRouteFlapDampeningMemoryLimit": wfBgpRouteFlapDampeningMemoryLimit,
       "wfBgp3Group": wfBgp3Group,
       "wfBgp3": wfBgp3,
       "wfBgp3Delete": wfBgp3Delete,
       "wfBgp3Disable": wfBgp3Disable,
       "wfBgp3State": wfBgp3State,
       "wfBgp3IntraAsIbgpRouting": wfBgp3IntraAsIbgpRouting,
       "wfBgp3IntAdvTimer": wfBgp3IntAdvTimer,
       "wfBgp3RipRules": wfBgp3RipRules,
       "wfBgp3UsedRoutes": wfBgp3UsedRoutes,
       "wfBgp3TotalRoutes": wfBgp3TotalRoutes,
       "wfBgp3PathAttrTable": wfBgp3PathAttrTable,
       "wfBgp3PathAttrEntry": wfBgp3PathAttrEntry,
       "wfBgp3PathAttrPeer": wfBgp3PathAttrPeer,
       "wfBgp3PathAttrDestNetwork": wfBgp3PathAttrDestNetwork,
       "wfBgp3PathAttrOrigin": wfBgp3PathAttrOrigin,
       "wfBgp3PathAttrASPath": wfBgp3PathAttrASPath,
       "wfBgp3PathAttrNextHop": wfBgp3PathAttrNextHop,
       "wfBgp3PathAttrInterASMetric": wfBgp3PathAttrInterASMetric,
       "wfBgp3PathAttrASPathWeight": wfBgp3PathAttrASPathWeight,
       "wfBgp3PathAttrBgpPreference": wfBgp3PathAttrBgpPreference,
       "wfBgp3PathAttrBest": wfBgp3PathAttrBest,
       "wfBgp4Group": wfBgp4Group,
       "wfBgp4": wfBgp4,
       "wfBgp4Delete": wfBgp4Delete,
       "wfBgp4Disable": wfBgp4Disable,
       "wfBgp4State": wfBgp4State}
)
