# SNMP MIB module (Wellfleet-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:26 2024
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

(wfIpGroup,
 wfRipGroup,
 wfUdpGroup) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIpGroup",
    "wfRipGroup",
    "wfUdpGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfIpBase_ObjectIdentity = ObjectIdentity
wfIpBase = _WfIpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1)
)


class _WfIpBaseCreate_Type(Integer32):
    """Custom type wfIpBaseCreate based on Integer32"""
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


_WfIpBaseCreate_Type.__name__ = "Integer32"
_WfIpBaseCreate_Object = MibScalar
wfIpBaseCreate = _WfIpBaseCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 1),
    _WfIpBaseCreate_Type()
)
wfIpBaseCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseCreate.setStatus("mandatory")


class _WfIpBaseEnable_Type(Integer32):
    """Custom type wfIpBaseEnable based on Integer32"""
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


_WfIpBaseEnable_Type.__name__ = "Integer32"
_WfIpBaseEnable_Object = MibScalar
wfIpBaseEnable = _WfIpBaseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 2),
    _WfIpBaseEnable_Type()
)
wfIpBaseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseEnable.setStatus("mandatory")


class _WfIpBaseState_Type(Integer32):
    """Custom type wfIpBaseState based on Integer32"""
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


_WfIpBaseState_Type.__name__ = "Integer32"
_WfIpBaseState_Object = MibScalar
wfIpBaseState = _WfIpBaseState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 3),
    _WfIpBaseState_Type()
)
wfIpBaseState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseState.setStatus("mandatory")


class _WfIpBaseForwarding_Type(Integer32):
    """Custom type wfIpBaseForwarding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("not-forwarding", 2))
    )


_WfIpBaseForwarding_Type.__name__ = "Integer32"
_WfIpBaseForwarding_Object = MibScalar
wfIpBaseForwarding = _WfIpBaseForwarding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 4),
    _WfIpBaseForwarding_Type()
)
wfIpBaseForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseForwarding.setStatus("mandatory")


class _WfIpBaseDefaultTTL_Type(Integer32):
    """Custom type wfIpBaseDefaultTTL based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpBaseDefaultTTL_Type.__name__ = "Integer32"
_WfIpBaseDefaultTTL_Object = MibScalar
wfIpBaseDefaultTTL = _WfIpBaseDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 5),
    _WfIpBaseDefaultTTL_Type()
)
wfIpBaseDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDefaultTTL.setStatus("mandatory")


class _WfIpBaseRipDiameter_Type(Integer32):
    """Custom type wfIpBaseRipDiameter based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfIpBaseRipDiameter_Type.__name__ = "Integer32"
_WfIpBaseRipDiameter_Object = MibScalar
wfIpBaseRipDiameter = _WfIpBaseRipDiameter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 6),
    _WfIpBaseRipDiameter_Type()
)
wfIpBaseRipDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseRipDiameter.setStatus("mandatory")


class _WfIpBaseRouteCache_Type(Integer32):
    """Custom type wfIpBaseRouteCache based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            60
        )
    )
    namedValues = NamedValues(
        ("default", 60)
    )


_WfIpBaseRouteCache_Type.__name__ = "Integer32"
_WfIpBaseRouteCache_Object = MibScalar
wfIpBaseRouteCache = _WfIpBaseRouteCache_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 7),
    _WfIpBaseRouteCache_Type()
)
wfIpBaseRouteCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseRouteCache.setStatus("mandatory")


class _WfIpBaseMibTables_Type(Integer32):
    """Custom type wfIpBaseMibTables based on Integer32"""
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
        *(("both", 4),
          ("forwarding", 3),
          ("none", 1),
          ("route", 2))
    )


_WfIpBaseMibTables_Type.__name__ = "Integer32"
_WfIpBaseMibTables_Object = MibScalar
wfIpBaseMibTables = _WfIpBaseMibTables_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 8),
    _WfIpBaseMibTables_Type()
)
wfIpBaseMibTables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseMibTables.setStatus("mandatory")
_WfIpBaseNetworks_Type = Integer32
_WfIpBaseNetworks_Object = MibScalar
wfIpBaseNetworks = _WfIpBaseNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 9),
    _WfIpBaseNetworks_Type()
)
wfIpBaseNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseNetworks.setStatus("mandatory")


class _WfIpBaseZeroSubnetEnable_Type(Integer32):
    """Custom type wfIpBaseZeroSubnetEnable based on Integer32"""
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
          ("rip1onasb", 3))
    )


_WfIpBaseZeroSubnetEnable_Type.__name__ = "Integer32"
_WfIpBaseZeroSubnetEnable_Object = MibScalar
wfIpBaseZeroSubnetEnable = _WfIpBaseZeroSubnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 10),
    _WfIpBaseZeroSubnetEnable_Type()
)
wfIpBaseZeroSubnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseZeroSubnetEnable.setStatus("mandatory")
_WfIpBaseEstimatedNetworks_Type = Integer32
_WfIpBaseEstimatedNetworks_Object = MibScalar
wfIpBaseEstimatedNetworks = _WfIpBaseEstimatedNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 11),
    _WfIpBaseEstimatedNetworks_Type()
)
wfIpBaseEstimatedNetworks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseEstimatedNetworks.setStatus("mandatory")
_WfIpBaseHosts_Type = Integer32
_WfIpBaseHosts_Object = MibScalar
wfIpBaseHosts = _WfIpBaseHosts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 12),
    _WfIpBaseHosts_Type()
)
wfIpBaseHosts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseHosts.setStatus("mandatory")
_WfIpBaseEstimatedHosts_Type = Integer32
_WfIpBaseEstimatedHosts_Object = MibScalar
wfIpBaseEstimatedHosts = _WfIpBaseEstimatedHosts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 13),
    _WfIpBaseEstimatedHosts_Type()
)
wfIpBaseEstimatedHosts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseEstimatedHosts.setStatus("mandatory")


class _WfIpBaseDefaultOverSubnetEnable_Type(Integer32):
    """Custom type wfIpBaseDefaultOverSubnetEnable based on Integer32"""
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


_WfIpBaseDefaultOverSubnetEnable_Type.__name__ = "Integer32"
_WfIpBaseDefaultOverSubnetEnable_Object = MibScalar
wfIpBaseDefaultOverSubnetEnable = _WfIpBaseDefaultOverSubnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 14),
    _WfIpBaseDefaultOverSubnetEnable_Type()
)
wfIpBaseDefaultOverSubnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDefaultOverSubnetEnable.setStatus("mandatory")


class _WfIpBaseMaxPolicyRules_Type(Integer32):
    """Custom type wfIpBaseMaxPolicyRules based on Integer32"""
    defaultValue = 32


_WfIpBaseMaxPolicyRules_Object = MibScalar
wfIpBaseMaxPolicyRules = _WfIpBaseMaxPolicyRules_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 15),
    _WfIpBaseMaxPolicyRules_Type()
)
wfIpBaseMaxPolicyRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseMaxPolicyRules.setStatus("mandatory")


class _WfIpBaseRouteFilterSupport_Type(Integer32):
    """Custom type wfIpBaseRouteFilterSupport based on Integer32"""
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


_WfIpBaseRouteFilterSupport_Type.__name__ = "Integer32"
_WfIpBaseRouteFilterSupport_Object = MibScalar
wfIpBaseRouteFilterSupport = _WfIpBaseRouteFilterSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 16),
    _WfIpBaseRouteFilterSupport_Type()
)
wfIpBaseRouteFilterSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseRouteFilterSupport.setStatus("mandatory")


class _WfRipMaximumPath_Type(Integer32):
    """Custom type wfRipMaximumPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WfRipMaximumPath_Type.__name__ = "Integer32"
_WfRipMaximumPath_Object = MibScalar
wfRipMaximumPath = _WfRipMaximumPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 17),
    _WfRipMaximumPath_Type()
)
wfRipMaximumPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipMaximumPath.setStatus("mandatory")


class _WfIpMultipathMethod_Type(Integer32):
    """Custom type wfIpMultipathMethod based on Integer32"""
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
        *(("dest-hash", 4),
          ("disabled", 1),
          ("round-robin", 2),
          ("src-dest-hash", 3))
    )


_WfIpMultipathMethod_Type.__name__ = "Integer32"
_WfIpMultipathMethod_Object = MibScalar
wfIpMultipathMethod = _WfIpMultipathMethod_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 18),
    _WfIpMultipathMethod_Type()
)
wfIpMultipathMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpMultipathMethod.setStatus("mandatory")


class _WfIpBaseIspMode_Type(Integer32):
    """Custom type wfIpBaseIspMode based on Integer32"""
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


_WfIpBaseIspMode_Type.__name__ = "Integer32"
_WfIpBaseIspMode_Object = MibScalar
wfIpBaseIspMode = _WfIpBaseIspMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 19),
    _WfIpBaseIspMode_Type()
)
wfIpBaseIspMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseIspMode.setStatus("mandatory")


class _WfIpBaseExtendedTrafficFilterSupport_Type(Integer32):
    """Custom type wfIpBaseExtendedTrafficFilterSupport based on Integer32"""
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


_WfIpBaseExtendedTrafficFilterSupport_Type.__name__ = "Integer32"
_WfIpBaseExtendedTrafficFilterSupport_Object = MibScalar
wfIpBaseExtendedTrafficFilterSupport = _WfIpBaseExtendedTrafficFilterSupport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 20),
    _WfIpBaseExtendedTrafficFilterSupport_Type()
)
wfIpBaseExtendedTrafficFilterSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseExtendedTrafficFilterSupport.setStatus("mandatory")


class _WfIpOspfMaximumPath_Type(Integer32):
    """Custom type wfIpOspfMaximumPath based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_WfIpOspfMaximumPath_Type.__name__ = "Integer32"
_WfIpOspfMaximumPath_Object = MibScalar
wfIpOspfMaximumPath = _WfIpOspfMaximumPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 21),
    _WfIpOspfMaximumPath_Type()
)
wfIpOspfMaximumPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpOspfMaximumPath.setStatus("mandatory")


class _WfIpBaseIcmpErrorLimit_Type(Integer32):
    """Custom type wfIpBaseIcmpErrorLimit based on Integer32"""
    defaultValue = 0


_WfIpBaseIcmpErrorLimit_Object = MibScalar
wfIpBaseIcmpErrorLimit = _WfIpBaseIcmpErrorLimit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 22),
    _WfIpBaseIcmpErrorLimit_Type()
)
wfIpBaseIcmpErrorLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseIcmpErrorLimit.setStatus("mandatory")


class _WfIpBaseIbgpEcmp_Type(Integer32):
    """Custom type wfIpBaseIbgpEcmp based on Integer32"""
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


_WfIpBaseIbgpEcmp_Type.__name__ = "Integer32"
_WfIpBaseIbgpEcmp_Object = MibScalar
wfIpBaseIbgpEcmp = _WfIpBaseIbgpEcmp_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 23),
    _WfIpBaseIbgpEcmp_Type()
)
wfIpBaseIbgpEcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseIbgpEcmp.setStatus("obsolete")


class _WfIpBaseRtbBalanceInterval_Type(Integer32):
    """Custom type wfIpBaseRtbBalanceInterval based on Integer32"""
    defaultValue = 0


_WfIpBaseRtbBalanceInterval_Object = MibScalar
wfIpBaseRtbBalanceInterval = _WfIpBaseRtbBalanceInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 24),
    _WfIpBaseRtbBalanceInterval_Type()
)
wfIpBaseRtbBalanceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseRtbBalanceInterval.setStatus("mandatory")


class _WfIpBaseRtblP1_Type(Integer32):
    """Custom type wfIpBaseRtblP1 based on Integer32"""
    defaultValue = 0


_WfIpBaseRtblP1_Object = MibScalar
wfIpBaseRtblP1 = _WfIpBaseRtblP1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 25),
    _WfIpBaseRtblP1_Type()
)
wfIpBaseRtblP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseRtblP1.setStatus("mandatory")


class _WfIpBaseRtblP2_Type(Integer32):
    """Custom type wfIpBaseRtblP2 based on Integer32"""
    defaultValue = 0


_WfIpBaseRtblP2_Object = MibScalar
wfIpBaseRtblP2 = _WfIpBaseRtblP2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 26),
    _WfIpBaseRtblP2_Type()
)
wfIpBaseRtblP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseRtblP2.setStatus("mandatory")


class _WfIpBaseArpBufLimitPrcnt_Type(Integer32):
    """Custom type wfIpBaseArpBufLimitPrcnt based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfIpBaseArpBufLimitPrcnt_Type.__name__ = "Integer32"
_WfIpBaseArpBufLimitPrcnt_Object = MibScalar
wfIpBaseArpBufLimitPrcnt = _WfIpBaseArpBufLimitPrcnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 27),
    _WfIpBaseArpBufLimitPrcnt_Type()
)
wfIpBaseArpBufLimitPrcnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseArpBufLimitPrcnt.setStatus("mandatory")


class _WfIpBaseDirectedBcastEnable_Type(Integer32):
    """Custom type wfIpBaseDirectedBcastEnable based on Integer32"""
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


_WfIpBaseDirectedBcastEnable_Type.__name__ = "Integer32"
_WfIpBaseDirectedBcastEnable_Object = MibScalar
wfIpBaseDirectedBcastEnable = _WfIpBaseDirectedBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 28),
    _WfIpBaseDirectedBcastEnable_Type()
)
wfIpBaseDirectedBcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDirectedBcastEnable.setStatus("mandatory")


class _WfIpBaseHostOnlyRip_Type(Integer32):
    """Custom type wfIpBaseHostOnlyRip based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("listen", 1),
          ("notlisten", 2))
    )


_WfIpBaseHostOnlyRip_Type.__name__ = "Integer32"
_WfIpBaseHostOnlyRip_Object = MibScalar
wfIpBaseHostOnlyRip = _WfIpBaseHostOnlyRip_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 29),
    _WfIpBaseHostOnlyRip_Type()
)
wfIpBaseHostOnlyRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseHostOnlyRip.setStatus("mandatory")


class _WfIpBaseBlockSRR_Type(Integer32):
    """Custom type wfIpBaseBlockSRR based on Integer32"""
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


_WfIpBaseBlockSRR_Type.__name__ = "Integer32"
_WfIpBaseBlockSRR_Object = MibScalar
wfIpBaseBlockSRR = _WfIpBaseBlockSRR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 1, 30),
    _WfIpBaseBlockSRR_Type()
)
wfIpBaseBlockSRR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseBlockSRR.setStatus("mandatory")
_WfIpBaseRtEntryTable_Object = MibTable
wfIpBaseRtEntryTable = _WfIpBaseRtEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wfIpBaseRtEntryTable.setStatus("mandatory")
_WfIpBaseRtEntry_Object = MibTableRow
wfIpBaseRtEntry = _WfIpBaseRtEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1)
)
wfIpBaseRtEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpBaseRouteDest"),
)
if mibBuilder.loadTexts:
    wfIpBaseRtEntry.setStatus("mandatory")
_WfIpBaseRouteDest_Type = IpAddress
_WfIpBaseRouteDest_Object = MibTableColumn
wfIpBaseRouteDest = _WfIpBaseRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 1),
    _WfIpBaseRouteDest_Type()
)
wfIpBaseRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteDest.setStatus("mandatory")
_WfIpBaseRouteIfIndex_Type = Integer32
_WfIpBaseRouteIfIndex_Object = MibTableColumn
wfIpBaseRouteIfIndex = _WfIpBaseRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 2),
    _WfIpBaseRouteIfIndex_Type()
)
wfIpBaseRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteIfIndex.setStatus("mandatory")
_WfIpBaseRouteMetric1_Type = Integer32
_WfIpBaseRouteMetric1_Object = MibTableColumn
wfIpBaseRouteMetric1 = _WfIpBaseRouteMetric1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 3),
    _WfIpBaseRouteMetric1_Type()
)
wfIpBaseRouteMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric1.setStatus("mandatory")
_WfIpBaseRouteMetric2_Type = Integer32
_WfIpBaseRouteMetric2_Object = MibTableColumn
wfIpBaseRouteMetric2 = _WfIpBaseRouteMetric2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 4),
    _WfIpBaseRouteMetric2_Type()
)
wfIpBaseRouteMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric2.setStatus("mandatory")
_WfIpBaseRouteMetric3_Type = Integer32
_WfIpBaseRouteMetric3_Object = MibTableColumn
wfIpBaseRouteMetric3 = _WfIpBaseRouteMetric3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 5),
    _WfIpBaseRouteMetric3_Type()
)
wfIpBaseRouteMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric3.setStatus("mandatory")
_WfIpBaseRouteMetric4_Type = Integer32
_WfIpBaseRouteMetric4_Object = MibTableColumn
wfIpBaseRouteMetric4 = _WfIpBaseRouteMetric4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 6),
    _WfIpBaseRouteMetric4_Type()
)
wfIpBaseRouteMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric4.setStatus("mandatory")
_WfIpBaseRouteNextHop_Type = IpAddress
_WfIpBaseRouteNextHop_Object = MibTableColumn
wfIpBaseRouteNextHop = _WfIpBaseRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 7),
    _WfIpBaseRouteNextHop_Type()
)
wfIpBaseRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteNextHop.setStatus("mandatory")


class _WfIpBaseRouteType_Type(Integer32):
    """Custom type wfIpBaseRouteType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_WfIpBaseRouteType_Type.__name__ = "Integer32"
_WfIpBaseRouteType_Object = MibTableColumn
wfIpBaseRouteType = _WfIpBaseRouteType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 8),
    _WfIpBaseRouteType_Type()
)
wfIpBaseRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteType.setStatus("mandatory")


class _WfIpBaseRouteProto_Type(Integer32):
    """Custom type wfIpBaseRouteProto based on Integer32"""
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
              8,
              9,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ahb", 16),
          ("asr", 17),
          ("bgp", 14),
          ("egp", 5),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("is", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_WfIpBaseRouteProto_Type.__name__ = "Integer32"
_WfIpBaseRouteProto_Object = MibTableColumn
wfIpBaseRouteProto = _WfIpBaseRouteProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 9),
    _WfIpBaseRouteProto_Type()
)
wfIpBaseRouteProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteProto.setStatus("mandatory")
_WfIpBaseRouteAge_Type = Integer32
_WfIpBaseRouteAge_Object = MibTableColumn
wfIpBaseRouteAge = _WfIpBaseRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 10),
    _WfIpBaseRouteAge_Type()
)
wfIpBaseRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteAge.setStatus("mandatory")
_WfIpBaseRouteMask_Type = IpAddress
_WfIpBaseRouteMask_Object = MibTableColumn
wfIpBaseRouteMask = _WfIpBaseRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 11),
    _WfIpBaseRouteMask_Type()
)
wfIpBaseRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMask.setStatus("mandatory")
_WfIpBaseRouteMetric5_Type = Integer32
_WfIpBaseRouteMetric5_Object = MibTableColumn
wfIpBaseRouteMetric5 = _WfIpBaseRouteMetric5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 12),
    _WfIpBaseRouteMetric5_Type()
)
wfIpBaseRouteMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteMetric5.setStatus("mandatory")
_WfIpBaseRouteInfo_Type = ObjectIdentifier
_WfIpBaseRouteInfo_Object = MibTableColumn
wfIpBaseRouteInfo = _WfIpBaseRouteInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 2, 1, 13),
    _WfIpBaseRouteInfo_Type()
)
wfIpBaseRouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseRouteInfo.setStatus("mandatory")
_WfIpBaseHostEntryTable_Object = MibTable
wfIpBaseHostEntryTable = _WfIpBaseHostEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wfIpBaseHostEntryTable.setStatus("obsolete")
_WfIpBaseHostEntry_Object = MibTableRow
wfIpBaseHostEntry = _WfIpBaseHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1)
)
wfIpBaseHostEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpBaseNetToMediaIfIndex"),
    (0, "Wellfleet-IP-MIB", "wfIpBaseNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    wfIpBaseHostEntry.setStatus("obsolete")
_WfIpBaseNetToMediaIfIndex_Type = Integer32
_WfIpBaseNetToMediaIfIndex_Object = MibTableColumn
wfIpBaseNetToMediaIfIndex = _WfIpBaseNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 1),
    _WfIpBaseNetToMediaIfIndex_Type()
)
wfIpBaseNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaIfIndex.setStatus("obsolete")
_WfIpBaseNetToMediaPhysAddress_Type = OctetString
_WfIpBaseNetToMediaPhysAddress_Object = MibTableColumn
wfIpBaseNetToMediaPhysAddress = _WfIpBaseNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 2),
    _WfIpBaseNetToMediaPhysAddress_Type()
)
wfIpBaseNetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaPhysAddress.setStatus("obsolete")
_WfIpBaseNetToMediaNetAddress_Type = IpAddress
_WfIpBaseNetToMediaNetAddress_Object = MibTableColumn
wfIpBaseNetToMediaNetAddress = _WfIpBaseNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 3),
    _WfIpBaseNetToMediaNetAddress_Type()
)
wfIpBaseNetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaNetAddress.setStatus("obsolete")


class _WfIpBaseNetToMediaType_Type(Integer32):
    """Custom type wfIpBaseNetToMediaType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_WfIpBaseNetToMediaType_Type.__name__ = "Integer32"
_WfIpBaseNetToMediaType_Object = MibTableColumn
wfIpBaseNetToMediaType = _WfIpBaseNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 3, 1, 4),
    _WfIpBaseNetToMediaType_Type()
)
wfIpBaseNetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseNetToMediaType.setStatus("obsolete")
_WfIpInterfaceTable_Object = MibTable
wfIpInterfaceTable = _WfIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    wfIpInterfaceTable.setStatus("obsolete")
_WfIpInterfaceEntry_Object = MibTableRow
wfIpInterfaceEntry = _WfIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1)
)
wfIpInterfaceEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpInterfaceAddr"),
    (0, "Wellfleet-IP-MIB", "wfIpInterfaceCircuit"),
)
if mibBuilder.loadTexts:
    wfIpInterfaceEntry.setStatus("obsolete")


class _WfIpInterfaceCreate_Type(Integer32):
    """Custom type wfIpInterfaceCreate based on Integer32"""
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


_WfIpInterfaceCreate_Type.__name__ = "Integer32"
_WfIpInterfaceCreate_Object = MibTableColumn
wfIpInterfaceCreate = _WfIpInterfaceCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 1),
    _WfIpInterfaceCreate_Type()
)
wfIpInterfaceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCreate.setStatus("obsolete")


class _WfIpInterfaceEnable_Type(Integer32):
    """Custom type wfIpInterfaceEnable based on Integer32"""
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


_WfIpInterfaceEnable_Type.__name__ = "Integer32"
_WfIpInterfaceEnable_Object = MibTableColumn
wfIpInterfaceEnable = _WfIpInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 2),
    _WfIpInterfaceEnable_Type()
)
wfIpInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceEnable.setStatus("obsolete")


class _WfIpInterfaceState_Type(Integer32):
    """Custom type wfIpInterfaceState based on Integer32"""
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


_WfIpInterfaceState_Type.__name__ = "Integer32"
_WfIpInterfaceState_Object = MibTableColumn
wfIpInterfaceState = _WfIpInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 3),
    _WfIpInterfaceState_Type()
)
wfIpInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceState.setStatus("obsolete")
_WfIpInterfaceAddr_Type = IpAddress
_WfIpInterfaceAddr_Object = MibTableColumn
wfIpInterfaceAddr = _WfIpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 4),
    _WfIpInterfaceAddr_Type()
)
wfIpInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAddr.setStatus("obsolete")
_WfIpInterfaceCircuit_Type = Integer32
_WfIpInterfaceCircuit_Object = MibTableColumn
wfIpInterfaceCircuit = _WfIpInterfaceCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 5),
    _WfIpInterfaceCircuit_Type()
)
wfIpInterfaceCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceCircuit.setStatus("obsolete")
_WfIpInterfaceMask_Type = IpAddress
_WfIpInterfaceMask_Object = MibTableColumn
wfIpInterfaceMask = _WfIpInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 6),
    _WfIpInterfaceMask_Type()
)
wfIpInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMask.setStatus("obsolete")


class _WfIpInterfaceCost_Type(Integer32):
    """Custom type wfIpInterfaceCost based on Integer32"""
    defaultValue = 1


_WfIpInterfaceCost_Object = MibTableColumn
wfIpInterfaceCost = _WfIpInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 7),
    _WfIpInterfaceCost_Type()
)
wfIpInterfaceCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCost.setStatus("obsolete")
_WfIpInterfaceCfgBcastAddr_Type = IpAddress
_WfIpInterfaceCfgBcastAddr_Object = MibTableColumn
wfIpInterfaceCfgBcastAddr = _WfIpInterfaceCfgBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 8),
    _WfIpInterfaceCfgBcastAddr_Type()
)
wfIpInterfaceCfgBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCfgBcastAddr.setStatus("obsolete")
_WfIpInterfaceBcastAddr_Type = IpAddress
_WfIpInterfaceBcastAddr_Object = MibTableColumn
wfIpInterfaceBcastAddr = _WfIpInterfaceBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 9),
    _WfIpInterfaceBcastAddr_Type()
)
wfIpInterfaceBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceBcastAddr.setStatus("obsolete")


class _WfIpInterfaceMTUDiscovery_Type(Integer32):
    """Custom type wfIpInterfaceMTUDiscovery based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceMTUDiscovery_Type.__name__ = "Integer32"
_WfIpInterfaceMTUDiscovery_Object = MibTableColumn
wfIpInterfaceMTUDiscovery = _WfIpInterfaceMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 10),
    _WfIpInterfaceMTUDiscovery_Type()
)
wfIpInterfaceMTUDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMTUDiscovery.setStatus("obsolete")


class _WfIpInterfaceAMR_Type(Integer32):
    """Custom type wfIpInterfaceAMR based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceAMR_Type.__name__ = "Integer32"
_WfIpInterfaceAMR_Object = MibTableColumn
wfIpInterfaceAMR = _WfIpInterfaceAMR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 11),
    _WfIpInterfaceAMR_Type()
)
wfIpInterfaceAMR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAMR.setStatus("obsolete")


class _WfIpInterfaceASB_Type(Integer32):
    """Custom type wfIpInterfaceASB based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceASB_Type.__name__ = "Integer32"
_WfIpInterfaceASB_Object = MibTableColumn
wfIpInterfaceASB = _WfIpInterfaceASB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 12),
    _WfIpInterfaceASB_Type()
)
wfIpInterfaceASB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceASB.setStatus("obsolete")


class _WfIpInterfaceAddressResolutionType_Type(Integer32):
    """Custom type wfIpInterfaceAddressResolutionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("arp-in-arp", 6),
          ("arp-probe", 10),
          ("atm-arp", 11),
          ("bfe-ddn", 8),
          ("ddn", 3),
          ("in-arp", 5),
          ("none", 7),
          ("pdn", 4),
          ("probe", 9))
    )


_WfIpInterfaceAddressResolutionType_Type.__name__ = "Integer32"
_WfIpInterfaceAddressResolutionType_Object = MibTableColumn
wfIpInterfaceAddressResolutionType = _WfIpInterfaceAddressResolutionType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 13),
    _WfIpInterfaceAddressResolutionType_Type()
)
wfIpInterfaceAddressResolutionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAddressResolutionType.setStatus("obsolete")


class _WfIpInterfaceProxy_Type(Integer32):
    """Custom type wfIpInterfaceProxy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceProxy_Type.__name__ = "Integer32"
_WfIpInterfaceProxy_Object = MibTableColumn
wfIpInterfaceProxy = _WfIpInterfaceProxy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 14),
    _WfIpInterfaceProxy_Type()
)
wfIpInterfaceProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceProxy.setStatus("obsolete")


class _WfIpInterfaceHostCache_Type(Integer32):
    """Custom type wfIpInterfaceHostCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              120,
              180,
              240,
              300,
              600,
              900,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("cache-120", 120),
          ("cache-1200", 1200),
          ("cache-180", 180),
          ("cache-240", 240),
          ("cache-300", 300),
          ("cache-600", 600),
          ("cache-900", 900),
          ("cache-off", 1))
    )


_WfIpInterfaceHostCache_Type.__name__ = "Integer32"
_WfIpInterfaceHostCache_Object = MibTableColumn
wfIpInterfaceHostCache = _WfIpInterfaceHostCache_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 15),
    _WfIpInterfaceHostCache_Type()
)
wfIpInterfaceHostCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceHostCache.setStatus("obsolete")


class _WfIpInterfaceUdpXsumOn_Type(Integer32):
    """Custom type wfIpInterfaceUdpXsumOn based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceUdpXsumOn_Type.__name__ = "Integer32"
_WfIpInterfaceUdpXsumOn_Object = MibTableColumn
wfIpInterfaceUdpXsumOn = _WfIpInterfaceUdpXsumOn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 16),
    _WfIpInterfaceUdpXsumOn_Type()
)
wfIpInterfaceUdpXsumOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceUdpXsumOn.setStatus("obsolete")
_WfIpInterfaceCfgMacAddress_Type = OctetString
_WfIpInterfaceCfgMacAddress_Object = MibTableColumn
wfIpInterfaceCfgMacAddress = _WfIpInterfaceCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 17),
    _WfIpInterfaceCfgMacAddress_Type()
)
wfIpInterfaceCfgMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceCfgMacAddress.setStatus("obsolete")
_WfIpInterfaceMacAddress_Type = OctetString
_WfIpInterfaceMacAddress_Object = MibTableColumn
wfIpInterfaceMacAddress = _WfIpInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 18),
    _WfIpInterfaceMacAddress_Type()
)
wfIpInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceMacAddress.setStatus("obsolete")
_WfIpInterfaceReasmMaxSize_Type = Integer32
_WfIpInterfaceReasmMaxSize_Object = MibTableColumn
wfIpInterfaceReasmMaxSize = _WfIpInterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 19),
    _WfIpInterfaceReasmMaxSize_Type()
)
wfIpInterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmMaxSize.setStatus("obsolete")
_WfIpInterfaceMaxInfo_Type = Integer32
_WfIpInterfaceMaxInfo_Object = MibTableColumn
wfIpInterfaceMaxInfo = _WfIpInterfaceMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 20),
    _WfIpInterfaceMaxInfo_Type()
)
wfIpInterfaceMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceMaxInfo.setStatus("obsolete")
_WfIpInterfaceInReceives_Type = Counter32
_WfIpInterfaceInReceives_Object = MibTableColumn
wfIpInterfaceInReceives = _WfIpInterfaceInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 21),
    _WfIpInterfaceInReceives_Type()
)
wfIpInterfaceInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInReceives.setStatus("obsolete")
_WfIpInterfaceInHdrErrors_Type = Counter32
_WfIpInterfaceInHdrErrors_Object = MibTableColumn
wfIpInterfaceInHdrErrors = _WfIpInterfaceInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 22),
    _WfIpInterfaceInHdrErrors_Type()
)
wfIpInterfaceInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInHdrErrors.setStatus("obsolete")
_WfIpInterfaceInAddrErrors_Type = Counter32
_WfIpInterfaceInAddrErrors_Object = MibTableColumn
wfIpInterfaceInAddrErrors = _WfIpInterfaceInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 23),
    _WfIpInterfaceInAddrErrors_Type()
)
wfIpInterfaceInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInAddrErrors.setStatus("obsolete")
_WfIpInterfaceForwDatagrams_Type = Counter32
_WfIpInterfaceForwDatagrams_Object = MibTableColumn
wfIpInterfaceForwDatagrams = _WfIpInterfaceForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 24),
    _WfIpInterfaceForwDatagrams_Type()
)
wfIpInterfaceForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceForwDatagrams.setStatus("obsolete")
_WfIpInterfaceInUnknownProtos_Type = Counter32
_WfIpInterfaceInUnknownProtos_Object = MibTableColumn
wfIpInterfaceInUnknownProtos = _WfIpInterfaceInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 25),
    _WfIpInterfaceInUnknownProtos_Type()
)
wfIpInterfaceInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInUnknownProtos.setStatus("obsolete")
_WfIpInterfaceInDiscards_Type = Counter32
_WfIpInterfaceInDiscards_Object = MibTableColumn
wfIpInterfaceInDiscards = _WfIpInterfaceInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 26),
    _WfIpInterfaceInDiscards_Type()
)
wfIpInterfaceInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInDiscards.setStatus("obsolete")
_WfIpInterfaceInDelivers_Type = Counter32
_WfIpInterfaceInDelivers_Object = MibTableColumn
wfIpInterfaceInDelivers = _WfIpInterfaceInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 27),
    _WfIpInterfaceInDelivers_Type()
)
wfIpInterfaceInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceInDelivers.setStatus("obsolete")
_WfIpInterfaceOutRequests_Type = Counter32
_WfIpInterfaceOutRequests_Object = MibTableColumn
wfIpInterfaceOutRequests = _WfIpInterfaceOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 28),
    _WfIpInterfaceOutRequests_Type()
)
wfIpInterfaceOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceOutRequests.setStatus("obsolete")
_WfIpInterfaceOutDiscards_Type = Counter32
_WfIpInterfaceOutDiscards_Object = MibTableColumn
wfIpInterfaceOutDiscards = _WfIpInterfaceOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 29),
    _WfIpInterfaceOutDiscards_Type()
)
wfIpInterfaceOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceOutDiscards.setStatus("obsolete")
_WfIpInterfaceOutNoRoutes_Type = Counter32
_WfIpInterfaceOutNoRoutes_Object = MibTableColumn
wfIpInterfaceOutNoRoutes = _WfIpInterfaceOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 30),
    _WfIpInterfaceOutNoRoutes_Type()
)
wfIpInterfaceOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceOutNoRoutes.setStatus("obsolete")
_WfIpInterfaceReasmTimeout_Type = Integer32
_WfIpInterfaceReasmTimeout_Object = MibTableColumn
wfIpInterfaceReasmTimeout = _WfIpInterfaceReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 31),
    _WfIpInterfaceReasmTimeout_Type()
)
wfIpInterfaceReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmTimeout.setStatus("obsolete")
_WfIpInterfaceReasmReqds_Type = Counter32
_WfIpInterfaceReasmReqds_Object = MibTableColumn
wfIpInterfaceReasmReqds = _WfIpInterfaceReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 32),
    _WfIpInterfaceReasmReqds_Type()
)
wfIpInterfaceReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmReqds.setStatus("obsolete")
_WfIpInterfaceReasmOKs_Type = Counter32
_WfIpInterfaceReasmOKs_Object = MibTableColumn
wfIpInterfaceReasmOKs = _WfIpInterfaceReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 33),
    _WfIpInterfaceReasmOKs_Type()
)
wfIpInterfaceReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmOKs.setStatus("obsolete")
_WfIpInterfaceReasmFails_Type = Counter32
_WfIpInterfaceReasmFails_Object = MibTableColumn
wfIpInterfaceReasmFails = _WfIpInterfaceReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 34),
    _WfIpInterfaceReasmFails_Type()
)
wfIpInterfaceReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceReasmFails.setStatus("obsolete")
_WfIpInterfaceFragOKs_Type = Counter32
_WfIpInterfaceFragOKs_Object = MibTableColumn
wfIpInterfaceFragOKs = _WfIpInterfaceFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 35),
    _WfIpInterfaceFragOKs_Type()
)
wfIpInterfaceFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceFragOKs.setStatus("obsolete")
_WfIpInterfaceFragFails_Type = Counter32
_WfIpInterfaceFragFails_Object = MibTableColumn
wfIpInterfaceFragFails = _WfIpInterfaceFragFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 36),
    _WfIpInterfaceFragFails_Type()
)
wfIpInterfaceFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceFragFails.setStatus("obsolete")
_WfIpInterfaceFragCreates_Type = Counter32
_WfIpInterfaceFragCreates_Object = MibTableColumn
wfIpInterfaceFragCreates = _WfIpInterfaceFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 37),
    _WfIpInterfaceFragCreates_Type()
)
wfIpInterfaceFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceFragCreates.setStatus("obsolete")
_WfIpInterfaceIcmpInMsgs_Type = Counter32
_WfIpInterfaceIcmpInMsgs_Object = MibTableColumn
wfIpInterfaceIcmpInMsgs = _WfIpInterfaceIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 38),
    _WfIpInterfaceIcmpInMsgs_Type()
)
wfIpInterfaceIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInMsgs.setStatus("obsolete")
_WfIpInterfaceIcmpInErrors_Type = Counter32
_WfIpInterfaceIcmpInErrors_Object = MibTableColumn
wfIpInterfaceIcmpInErrors = _WfIpInterfaceIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 39),
    _WfIpInterfaceIcmpInErrors_Type()
)
wfIpInterfaceIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInErrors.setStatus("obsolete")
_WfIpInterfaceIcmpInDestUnreachs_Type = Counter32
_WfIpInterfaceIcmpInDestUnreachs_Object = MibTableColumn
wfIpInterfaceIcmpInDestUnreachs = _WfIpInterfaceIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 40),
    _WfIpInterfaceIcmpInDestUnreachs_Type()
)
wfIpInterfaceIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInDestUnreachs.setStatus("obsolete")
_WfIpInterfaceIcmpInTimeExcds_Type = Counter32
_WfIpInterfaceIcmpInTimeExcds_Object = MibTableColumn
wfIpInterfaceIcmpInTimeExcds = _WfIpInterfaceIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 41),
    _WfIpInterfaceIcmpInTimeExcds_Type()
)
wfIpInterfaceIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInTimeExcds.setStatus("obsolete")
_WfIpInterfaceIcmpInParmProbs_Type = Counter32
_WfIpInterfaceIcmpInParmProbs_Object = MibTableColumn
wfIpInterfaceIcmpInParmProbs = _WfIpInterfaceIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 42),
    _WfIpInterfaceIcmpInParmProbs_Type()
)
wfIpInterfaceIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInParmProbs.setStatus("obsolete")
_WfIpInterfaceIcmpInSrcQuenchs_Type = Counter32
_WfIpInterfaceIcmpInSrcQuenchs_Object = MibTableColumn
wfIpInterfaceIcmpInSrcQuenchs = _WfIpInterfaceIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 43),
    _WfIpInterfaceIcmpInSrcQuenchs_Type()
)
wfIpInterfaceIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInSrcQuenchs.setStatus("obsolete")
_WfIpInterfaceIcmpInRedirects_Type = Counter32
_WfIpInterfaceIcmpInRedirects_Object = MibTableColumn
wfIpInterfaceIcmpInRedirects = _WfIpInterfaceIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 44),
    _WfIpInterfaceIcmpInRedirects_Type()
)
wfIpInterfaceIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInRedirects.setStatus("obsolete")
_WfIpInterfaceIcmpInEchos_Type = Counter32
_WfIpInterfaceIcmpInEchos_Object = MibTableColumn
wfIpInterfaceIcmpInEchos = _WfIpInterfaceIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 45),
    _WfIpInterfaceIcmpInEchos_Type()
)
wfIpInterfaceIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInEchos.setStatus("obsolete")
_WfIpInterfaceIcmpInEchoReps_Type = Counter32
_WfIpInterfaceIcmpInEchoReps_Object = MibTableColumn
wfIpInterfaceIcmpInEchoReps = _WfIpInterfaceIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 46),
    _WfIpInterfaceIcmpInEchoReps_Type()
)
wfIpInterfaceIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInEchoReps.setStatus("obsolete")
_WfIpInterfaceIcmpInTimestamps_Type = Counter32
_WfIpInterfaceIcmpInTimestamps_Object = MibTableColumn
wfIpInterfaceIcmpInTimestamps = _WfIpInterfaceIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 47),
    _WfIpInterfaceIcmpInTimestamps_Type()
)
wfIpInterfaceIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInTimestamps.setStatus("obsolete")
_WfIpInterfaceIcmpInTimestampReps_Type = Counter32
_WfIpInterfaceIcmpInTimestampReps_Object = MibTableColumn
wfIpInterfaceIcmpInTimestampReps = _WfIpInterfaceIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 48),
    _WfIpInterfaceIcmpInTimestampReps_Type()
)
wfIpInterfaceIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInTimestampReps.setStatus("obsolete")
_WfIpInterfaceIcmpInAddrMasks_Type = Counter32
_WfIpInterfaceIcmpInAddrMasks_Object = MibTableColumn
wfIpInterfaceIcmpInAddrMasks = _WfIpInterfaceIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 49),
    _WfIpInterfaceIcmpInAddrMasks_Type()
)
wfIpInterfaceIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInAddrMasks.setStatus("obsolete")
_WfIpInterfaceIcmpInAddrMaskReps_Type = Counter32
_WfIpInterfaceIcmpInAddrMaskReps_Object = MibTableColumn
wfIpInterfaceIcmpInAddrMaskReps = _WfIpInterfaceIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 50),
    _WfIpInterfaceIcmpInAddrMaskReps_Type()
)
wfIpInterfaceIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInAddrMaskReps.setStatus("obsolete")
_WfIpInterfaceIcmpOutMsgs_Type = Counter32
_WfIpInterfaceIcmpOutMsgs_Object = MibTableColumn
wfIpInterfaceIcmpOutMsgs = _WfIpInterfaceIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 51),
    _WfIpInterfaceIcmpOutMsgs_Type()
)
wfIpInterfaceIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutMsgs.setStatus("obsolete")
_WfIpInterfaceIcmpOutErrors_Type = Counter32
_WfIpInterfaceIcmpOutErrors_Object = MibTableColumn
wfIpInterfaceIcmpOutErrors = _WfIpInterfaceIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 52),
    _WfIpInterfaceIcmpOutErrors_Type()
)
wfIpInterfaceIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutErrors.setStatus("obsolete")
_WfIpInterfaceIcmpOutDestUnreachs_Type = Counter32
_WfIpInterfaceIcmpOutDestUnreachs_Object = MibTableColumn
wfIpInterfaceIcmpOutDestUnreachs = _WfIpInterfaceIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 53),
    _WfIpInterfaceIcmpOutDestUnreachs_Type()
)
wfIpInterfaceIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutDestUnreachs.setStatus("obsolete")
_WfIpInterfaceIcmpOutTimeExcds_Type = Counter32
_WfIpInterfaceIcmpOutTimeExcds_Object = MibTableColumn
wfIpInterfaceIcmpOutTimeExcds = _WfIpInterfaceIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 54),
    _WfIpInterfaceIcmpOutTimeExcds_Type()
)
wfIpInterfaceIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutTimeExcds.setStatus("obsolete")
_WfIpInterfaceIcmpOutParmProbs_Type = Counter32
_WfIpInterfaceIcmpOutParmProbs_Object = MibTableColumn
wfIpInterfaceIcmpOutParmProbs = _WfIpInterfaceIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 55),
    _WfIpInterfaceIcmpOutParmProbs_Type()
)
wfIpInterfaceIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutParmProbs.setStatus("obsolete")
_WfIpInterfaceIcmpOutSrcQuenchs_Type = Counter32
_WfIpInterfaceIcmpOutSrcQuenchs_Object = MibTableColumn
wfIpInterfaceIcmpOutSrcQuenchs = _WfIpInterfaceIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 56),
    _WfIpInterfaceIcmpOutSrcQuenchs_Type()
)
wfIpInterfaceIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutSrcQuenchs.setStatus("obsolete")
_WfIpInterfaceIcmpOutRedirects_Type = Counter32
_WfIpInterfaceIcmpOutRedirects_Object = MibTableColumn
wfIpInterfaceIcmpOutRedirects = _WfIpInterfaceIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 57),
    _WfIpInterfaceIcmpOutRedirects_Type()
)
wfIpInterfaceIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutRedirects.setStatus("obsolete")
_WfIpInterfaceIcmpOutEchos_Type = Counter32
_WfIpInterfaceIcmpOutEchos_Object = MibTableColumn
wfIpInterfaceIcmpOutEchos = _WfIpInterfaceIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 58),
    _WfIpInterfaceIcmpOutEchos_Type()
)
wfIpInterfaceIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutEchos.setStatus("obsolete")
_WfIpInterfaceIcmpOutEchoReps_Type = Counter32
_WfIpInterfaceIcmpOutEchoReps_Object = MibTableColumn
wfIpInterfaceIcmpOutEchoReps = _WfIpInterfaceIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 59),
    _WfIpInterfaceIcmpOutEchoReps_Type()
)
wfIpInterfaceIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutEchoReps.setStatus("obsolete")
_WfIpInterfaceIcmpOutTimestamps_Type = Counter32
_WfIpInterfaceIcmpOutTimestamps_Object = MibTableColumn
wfIpInterfaceIcmpOutTimestamps = _WfIpInterfaceIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 60),
    _WfIpInterfaceIcmpOutTimestamps_Type()
)
wfIpInterfaceIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutTimestamps.setStatus("obsolete")
_WfIpInterfaceIcmpOutTimestampReps_Type = Counter32
_WfIpInterfaceIcmpOutTimestampReps_Object = MibTableColumn
wfIpInterfaceIcmpOutTimestampReps = _WfIpInterfaceIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 61),
    _WfIpInterfaceIcmpOutTimestampReps_Type()
)
wfIpInterfaceIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutTimestampReps.setStatus("obsolete")
_WfIpInterfaceIcmpOutAddrMasks_Type = Counter32
_WfIpInterfaceIcmpOutAddrMasks_Object = MibTableColumn
wfIpInterfaceIcmpOutAddrMasks = _WfIpInterfaceIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 62),
    _WfIpInterfaceIcmpOutAddrMasks_Type()
)
wfIpInterfaceIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutAddrMasks.setStatus("obsolete")
_WfIpInterfaceIcmpOutAddrMaskReps_Type = Counter32
_WfIpInterfaceIcmpOutAddrMaskReps_Object = MibTableColumn
wfIpInterfaceIcmpOutAddrMaskReps = _WfIpInterfaceIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 63),
    _WfIpInterfaceIcmpOutAddrMaskReps_Type()
)
wfIpInterfaceIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutAddrMaskReps.setStatus("obsolete")


class _WfIpInterfaceTrEndStation_Type(Integer32):
    """Custom type wfIpInterfaceTrEndStation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceTrEndStation_Type.__name__ = "Integer32"
_WfIpInterfaceTrEndStation_Object = MibTableColumn
wfIpInterfaceTrEndStation = _WfIpInterfaceTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 64),
    _WfIpInterfaceTrEndStation_Type()
)
wfIpInterfaceTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceTrEndStation.setStatus("obsolete")
_WfIpInterfaceSMDSGroupAddress_Type = OctetString
_WfIpInterfaceSMDSGroupAddress_Object = MibTableColumn
wfIpInterfaceSMDSGroupAddress = _WfIpInterfaceSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 65),
    _WfIpInterfaceSMDSGroupAddress_Type()
)
wfIpInterfaceSMDSGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceSMDSGroupAddress.setStatus("obsolete")
_WfIpInterfaceSMDSArpReqAddress_Type = OctetString
_WfIpInterfaceSMDSArpReqAddress_Object = MibTableColumn
wfIpInterfaceSMDSArpReqAddress = _WfIpInterfaceSMDSArpReqAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 66),
    _WfIpInterfaceSMDSArpReqAddress_Type()
)
wfIpInterfaceSMDSArpReqAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceSMDSArpReqAddress.setStatus("obsolete")
_WfIpInterfaceFRBcastDlci_Type = Integer32
_WfIpInterfaceFRBcastDlci_Object = MibTableColumn
wfIpInterfaceFRBcastDlci = _WfIpInterfaceFRBcastDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 67),
    _WfIpInterfaceFRBcastDlci_Type()
)
wfIpInterfaceFRBcastDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceFRBcastDlci.setStatus("obsolete")
_WfIpInterfaceFRMcast1Dlci_Type = Integer32
_WfIpInterfaceFRMcast1Dlci_Object = MibTableColumn
wfIpInterfaceFRMcast1Dlci = _WfIpInterfaceFRMcast1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 68),
    _WfIpInterfaceFRMcast1Dlci_Type()
)
wfIpInterfaceFRMcast1Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceFRMcast1Dlci.setStatus("obsolete")
_WfIpInterfaceFRMcast2Dlci_Type = Integer32
_WfIpInterfaceFRMcast2Dlci_Object = MibTableColumn
wfIpInterfaceFRMcast2Dlci = _WfIpInterfaceFRMcast2Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 69),
    _WfIpInterfaceFRMcast2Dlci_Type()
)
wfIpInterfaceFRMcast2Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceFRMcast2Dlci.setStatus("obsolete")


class _WfIpInterfaceRedirect_Type(Integer32):
    """Custom type wfIpInterfaceRedirect based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfIpInterfaceRedirect_Type.__name__ = "Integer32"
_WfIpInterfaceRedirect_Object = MibTableColumn
wfIpInterfaceRedirect = _WfIpInterfaceRedirect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 70),
    _WfIpInterfaceRedirect_Type()
)
wfIpInterfaceRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceRedirect.setStatus("obsolete")


class _WfIpInterfaceEnetArpEncaps_Type(Integer32):
    """Custom type wfIpInterfaceEnetArpEncaps based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("arpbothprobelsap", 9),
          ("arpenetprobelsap", 7),
          ("arpsnapprobelsap", 8),
          ("both", 3),
          ("enet", 1),
          ("probeboth", 6),
          ("probeenet", 5),
          ("probelsap", 4),
          ("snap", 2))
    )


_WfIpInterfaceEnetArpEncaps_Type.__name__ = "Integer32"
_WfIpInterfaceEnetArpEncaps_Object = MibTableColumn
wfIpInterfaceEnetArpEncaps = _WfIpInterfaceEnetArpEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 71),
    _WfIpInterfaceEnetArpEncaps_Type()
)
wfIpInterfaceEnetArpEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceEnetArpEncaps.setStatus("obsolete")
_WfIpInterfaceCacheMisses_Type = Counter32
_WfIpInterfaceCacheMisses_Object = MibTableColumn
wfIpInterfaceCacheMisses = _WfIpInterfaceCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 72),
    _WfIpInterfaceCacheMisses_Type()
)
wfIpInterfaceCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceCacheMisses.setStatus("obsolete")
_WfIpInterfaceCacheNetworks_Type = Gauge32
_WfIpInterfaceCacheNetworks_Object = MibTableColumn
wfIpInterfaceCacheNetworks = _WfIpInterfaceCacheNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 73),
    _WfIpInterfaceCacheNetworks_Type()
)
wfIpInterfaceCacheNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceCacheNetworks.setStatus("obsolete")
_WfIpInterfaceCacheRemoves_Type = Counter32
_WfIpInterfaceCacheRemoves_Object = MibTableColumn
wfIpInterfaceCacheRemoves = _WfIpInterfaceCacheRemoves_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 74),
    _WfIpInterfaceCacheRemoves_Type()
)
wfIpInterfaceCacheRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceCacheRemoves.setStatus("obsolete")


class _WfIpInterfaceSlotMask_Type(Gauge32):
    """Custom type wfIpInterfaceSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfIpInterfaceSlotMask_Object = MibTableColumn
wfIpInterfaceSlotMask = _WfIpInterfaceSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 75),
    _WfIpInterfaceSlotMask_Type()
)
wfIpInterfaceSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceSlotMask.setStatus("obsolete")


class _WfIpInterfaceEnableSecurity_Type(Integer32):
    """Custom type wfIpInterfaceEnableSecurity based on Integer32"""
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


_WfIpInterfaceEnableSecurity_Type.__name__ = "Integer32"
_WfIpInterfaceEnableSecurity_Object = MibTableColumn
wfIpInterfaceEnableSecurity = _WfIpInterfaceEnableSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 76),
    _WfIpInterfaceEnableSecurity_Type()
)
wfIpInterfaceEnableSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceEnableSecurity.setStatus("obsolete")


class _WfIpInterfaceStripSecurity_Type(Integer32):
    """Custom type wfIpInterfaceStripSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_WfIpInterfaceStripSecurity_Type.__name__ = "Integer32"
_WfIpInterfaceStripSecurity_Object = MibTableColumn
wfIpInterfaceStripSecurity = _WfIpInterfaceStripSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 77),
    _WfIpInterfaceStripSecurity_Type()
)
wfIpInterfaceStripSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceStripSecurity.setStatus("obsolete")


class _WfIpInterfaceRequireOutSecurity_Type(Integer32):
    """Custom type wfIpInterfaceRequireOutSecurity based on Integer32"""
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
        *(("all", 3),
          ("forwarded", 1),
          ("originated", 2))
    )


_WfIpInterfaceRequireOutSecurity_Type.__name__ = "Integer32"
_WfIpInterfaceRequireOutSecurity_Object = MibTableColumn
wfIpInterfaceRequireOutSecurity = _WfIpInterfaceRequireOutSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 78),
    _WfIpInterfaceRequireOutSecurity_Type()
)
wfIpInterfaceRequireOutSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceRequireOutSecurity.setStatus("obsolete")


class _WfIpInterfaceRequireInSecurity_Type(Integer32):
    """Custom type wfIpInterfaceRequireInSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_WfIpInterfaceRequireInSecurity_Type.__name__ = "Integer32"
_WfIpInterfaceRequireInSecurity_Object = MibTableColumn
wfIpInterfaceRequireInSecurity = _WfIpInterfaceRequireInSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 79),
    _WfIpInterfaceRequireInSecurity_Type()
)
wfIpInterfaceRequireInSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceRequireInSecurity.setStatus("obsolete")


class _WfIpInterfaceMinLevel_Type(Integer32):
    """Custom type wfIpInterfaceMinLevel based on Integer32"""
    defaultValue = 171

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpInterfaceMinLevel_Type.__name__ = "Integer32"
_WfIpInterfaceMinLevel_Object = MibTableColumn
wfIpInterfaceMinLevel = _WfIpInterfaceMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 80),
    _WfIpInterfaceMinLevel_Type()
)
wfIpInterfaceMinLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMinLevel.setStatus("obsolete")


class _WfIpInterfaceMaxLevel_Type(Integer32):
    """Custom type wfIpInterfaceMaxLevel based on Integer32"""
    defaultValue = 61

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpInterfaceMaxLevel_Type.__name__ = "Integer32"
_WfIpInterfaceMaxLevel_Object = MibTableColumn
wfIpInterfaceMaxLevel = _WfIpInterfaceMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 81),
    _WfIpInterfaceMaxLevel_Type()
)
wfIpInterfaceMaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMaxLevel.setStatus("obsolete")
_WfIpInterfaceMustOutAuthority_Type = OctetString
_WfIpInterfaceMustOutAuthority_Object = MibTableColumn
wfIpInterfaceMustOutAuthority = _WfIpInterfaceMustOutAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 82),
    _WfIpInterfaceMustOutAuthority_Type()
)
wfIpInterfaceMustOutAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMustOutAuthority.setStatus("obsolete")
_WfIpInterfaceMayOutAuthority_Type = OctetString
_WfIpInterfaceMayOutAuthority_Object = MibTableColumn
wfIpInterfaceMayOutAuthority = _WfIpInterfaceMayOutAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 83),
    _WfIpInterfaceMayOutAuthority_Type()
)
wfIpInterfaceMayOutAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMayOutAuthority.setStatus("obsolete")
_WfIpInterfaceMustInAuthority_Type = OctetString
_WfIpInterfaceMustInAuthority_Object = MibTableColumn
wfIpInterfaceMustInAuthority = _WfIpInterfaceMustInAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 84),
    _WfIpInterfaceMustInAuthority_Type()
)
wfIpInterfaceMustInAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMustInAuthority.setStatus("obsolete")
_WfIpInterfaceMayInAuthority_Type = OctetString
_WfIpInterfaceMayInAuthority_Object = MibTableColumn
wfIpInterfaceMayInAuthority = _WfIpInterfaceMayInAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 85),
    _WfIpInterfaceMayInAuthority_Type()
)
wfIpInterfaceMayInAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceMayInAuthority.setStatus("obsolete")


class _WfIpInterfaceImplicitLabelEnabled_Type(Integer32):
    """Custom type wfIpInterfaceImplicitLabelEnabled based on Integer32"""
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


_WfIpInterfaceImplicitLabelEnabled_Type.__name__ = "Integer32"
_WfIpInterfaceImplicitLabelEnabled_Object = MibTableColumn
wfIpInterfaceImplicitLabelEnabled = _WfIpInterfaceImplicitLabelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 86),
    _WfIpInterfaceImplicitLabelEnabled_Type()
)
wfIpInterfaceImplicitLabelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceImplicitLabelEnabled.setStatus("obsolete")
_WfIpInterfaceImplicitAuth_Type = OctetString
_WfIpInterfaceImplicitAuth_Object = MibTableColumn
wfIpInterfaceImplicitAuth = _WfIpInterfaceImplicitAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 87),
    _WfIpInterfaceImplicitAuth_Type()
)
wfIpInterfaceImplicitAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceImplicitAuth.setStatus("obsolete")


class _WfIpInterfaceImplicitLevel_Type(Integer32):
    """Custom type wfIpInterfaceImplicitLevel based on Integer32"""
    defaultValue = 171

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpInterfaceImplicitLevel_Type.__name__ = "Integer32"
_WfIpInterfaceImplicitLevel_Object = MibTableColumn
wfIpInterfaceImplicitLevel = _WfIpInterfaceImplicitLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 88),
    _WfIpInterfaceImplicitLevel_Type()
)
wfIpInterfaceImplicitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceImplicitLevel.setStatus("obsolete")


class _WfIpInterfaceDefaultLabelEnabled_Type(Integer32):
    """Custom type wfIpInterfaceDefaultLabelEnabled based on Integer32"""
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


_WfIpInterfaceDefaultLabelEnabled_Type.__name__ = "Integer32"
_WfIpInterfaceDefaultLabelEnabled_Object = MibTableColumn
wfIpInterfaceDefaultLabelEnabled = _WfIpInterfaceDefaultLabelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 89),
    _WfIpInterfaceDefaultLabelEnabled_Type()
)
wfIpInterfaceDefaultLabelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceDefaultLabelEnabled.setStatus("obsolete")
_WfIpInterfaceDefaultAuth_Type = OctetString
_WfIpInterfaceDefaultAuth_Object = MibTableColumn
wfIpInterfaceDefaultAuth = _WfIpInterfaceDefaultAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 90),
    _WfIpInterfaceDefaultAuth_Type()
)
wfIpInterfaceDefaultAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceDefaultAuth.setStatus("obsolete")


class _WfIpInterfaceDefaultLevel_Type(Integer32):
    """Custom type wfIpInterfaceDefaultLevel based on Integer32"""
    defaultValue = 171

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpInterfaceDefaultLevel_Type.__name__ = "Integer32"
_WfIpInterfaceDefaultLevel_Object = MibTableColumn
wfIpInterfaceDefaultLevel = _WfIpInterfaceDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 91),
    _WfIpInterfaceDefaultLevel_Type()
)
wfIpInterfaceDefaultLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceDefaultLevel.setStatus("obsolete")


class _WfIpInterfaceErrorLabelEnabled_Type(Integer32):
    """Custom type wfIpInterfaceErrorLabelEnabled based on Integer32"""
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


_WfIpInterfaceErrorLabelEnabled_Type.__name__ = "Integer32"
_WfIpInterfaceErrorLabelEnabled_Object = MibTableColumn
wfIpInterfaceErrorLabelEnabled = _WfIpInterfaceErrorLabelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 92),
    _WfIpInterfaceErrorLabelEnabled_Type()
)
wfIpInterfaceErrorLabelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceErrorLabelEnabled.setStatus("obsolete")
_WfIpInterfaceErrorAuth_Type = OctetString
_WfIpInterfaceErrorAuth_Object = MibTableColumn
wfIpInterfaceErrorAuth = _WfIpInterfaceErrorAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 93),
    _WfIpInterfaceErrorAuth_Type()
)
wfIpInterfaceErrorAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceErrorAuth.setStatus("obsolete")
_WfIpInterfaceDropRxAuths_Type = Counter32
_WfIpInterfaceDropRxAuths_Object = MibTableColumn
wfIpInterfaceDropRxAuths = _WfIpInterfaceDropRxAuths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 94),
    _WfIpInterfaceDropRxAuths_Type()
)
wfIpInterfaceDropRxAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropRxAuths.setStatus("obsolete")
_WfIpInterfaceDropRxFormats_Type = Counter32
_WfIpInterfaceDropRxFormats_Object = MibTableColumn
wfIpInterfaceDropRxFormats = _WfIpInterfaceDropRxFormats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 95),
    _WfIpInterfaceDropRxFormats_Type()
)
wfIpInterfaceDropRxFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropRxFormats.setStatus("obsolete")
_WfIpInterfaceDropRxLevels_Type = Counter32
_WfIpInterfaceDropRxLevels_Object = MibTableColumn
wfIpInterfaceDropRxLevels = _WfIpInterfaceDropRxLevels_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 96),
    _WfIpInterfaceDropRxLevels_Type()
)
wfIpInterfaceDropRxLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropRxLevels.setStatus("obsolete")
_WfIpInterfaceDropRxNoIpsos_Type = Counter32
_WfIpInterfaceDropRxNoIpsos_Object = MibTableColumn
wfIpInterfaceDropRxNoIpsos = _WfIpInterfaceDropRxNoIpsos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 97),
    _WfIpInterfaceDropRxNoIpsos_Type()
)
wfIpInterfaceDropRxNoIpsos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropRxNoIpsos.setStatus("obsolete")
_WfIpInterfaceDropTxAuths_Type = Counter32
_WfIpInterfaceDropTxAuths_Object = MibTableColumn
wfIpInterfaceDropTxAuths = _WfIpInterfaceDropTxAuths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 98),
    _WfIpInterfaceDropTxAuths_Type()
)
wfIpInterfaceDropTxAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropTxAuths.setStatus("obsolete")
_WfIpInterfaceDropTxLevels_Type = Counter32
_WfIpInterfaceDropTxLevels_Object = MibTableColumn
wfIpInterfaceDropTxLevels = _WfIpInterfaceDropTxLevels_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 99),
    _WfIpInterfaceDropTxLevels_Type()
)
wfIpInterfaceDropTxLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropTxLevels.setStatus("obsolete")
_WfIpInterfaceDropTxNoIpsos_Type = Counter32
_WfIpInterfaceDropTxNoIpsos_Object = MibTableColumn
wfIpInterfaceDropTxNoIpsos = _WfIpInterfaceDropTxNoIpsos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 100),
    _WfIpInterfaceDropTxNoIpsos_Type()
)
wfIpInterfaceDropTxNoIpsos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropTxNoIpsos.setStatus("obsolete")
_WfIpInterfaceDropTxNoIpsoRooms_Type = Counter32
_WfIpInterfaceDropTxNoIpsoRooms_Object = MibTableColumn
wfIpInterfaceDropTxNoIpsoRooms = _WfIpInterfaceDropTxNoIpsoRooms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 101),
    _WfIpInterfaceDropTxNoIpsoRooms_Type()
)
wfIpInterfaceDropTxNoIpsoRooms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceDropTxNoIpsoRooms.setStatus("obsolete")
_WfIpInterfaceICMPInAdminProhib_Type = Counter32
_WfIpInterfaceICMPInAdminProhib_Object = MibTableColumn
wfIpInterfaceICMPInAdminProhib = _WfIpInterfaceICMPInAdminProhib_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 102),
    _WfIpInterfaceICMPInAdminProhib_Type()
)
wfIpInterfaceICMPInAdminProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceICMPInAdminProhib.setStatus("obsolete")
_WfIpInterfaceICMPOutAdminProhib_Type = Counter32
_WfIpInterfaceICMPOutAdminProhib_Object = MibTableColumn
wfIpInterfaceICMPOutAdminProhib = _WfIpInterfaceICMPOutAdminProhib_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 103),
    _WfIpInterfaceICMPOutAdminProhib_Type()
)
wfIpInterfaceICMPOutAdminProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceICMPOutAdminProhib.setStatus("obsolete")


class _WfIpInterfaceFwdCacheSize_Type(Integer32):
    """Custom type wfIpInterfaceFwdCacheSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2147483647),
    )


_WfIpInterfaceFwdCacheSize_Type.__name__ = "Integer32"
_WfIpInterfaceFwdCacheSize_Object = MibTableColumn
wfIpInterfaceFwdCacheSize = _WfIpInterfaceFwdCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 104),
    _WfIpInterfaceFwdCacheSize_Type()
)
wfIpInterfaceFwdCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceFwdCacheSize.setStatus("obsolete")
_WfIpInterfaceTunnelInfo_Type = OctetString
_WfIpInterfaceTunnelInfo_Object = MibTableColumn
wfIpInterfaceTunnelInfo = _WfIpInterfaceTunnelInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 105),
    _WfIpInterfaceTunnelInfo_Type()
)
wfIpInterfaceTunnelInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceTunnelInfo.setStatus("obsolete")
_WfIpInterfaceIcmpInRdiscSolicit_Type = Counter32
_WfIpInterfaceIcmpInRdiscSolicit_Object = MibTableColumn
wfIpInterfaceIcmpInRdiscSolicit = _WfIpInterfaceIcmpInRdiscSolicit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 106),
    _WfIpInterfaceIcmpInRdiscSolicit_Type()
)
wfIpInterfaceIcmpInRdiscSolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInRdiscSolicit.setStatus("obsolete")
_WfIpInterfaceIcmpInRdiscAdvert_Type = Counter32
_WfIpInterfaceIcmpInRdiscAdvert_Object = MibTableColumn
wfIpInterfaceIcmpInRdiscAdvert = _WfIpInterfaceIcmpInRdiscAdvert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 107),
    _WfIpInterfaceIcmpInRdiscAdvert_Type()
)
wfIpInterfaceIcmpInRdiscAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpInRdiscAdvert.setStatus("obsolete")
_WfIpInterfaceIcmpOutRdiscAdvert_Type = Counter32
_WfIpInterfaceIcmpOutRdiscAdvert_Object = MibTableColumn
wfIpInterfaceIcmpOutRdiscAdvert = _WfIpInterfaceIcmpOutRdiscAdvert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 108),
    _WfIpInterfaceIcmpOutRdiscAdvert_Type()
)
wfIpInterfaceIcmpOutRdiscAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceIcmpOutRdiscAdvert.setStatus("obsolete")
_WfIpInterfaceRoutingDiscards_Type = Counter32
_WfIpInterfaceRoutingDiscards_Object = MibTableColumn
wfIpInterfaceRoutingDiscards = _WfIpInterfaceRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 109),
    _WfIpInterfaceRoutingDiscards_Type()
)
wfIpInterfaceRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceRoutingDiscards.setStatus("obsolete")
_WfIpInterfaceUnnumAssocAddr_Type = IpAddress
_WfIpInterfaceUnnumAssocAddr_Object = MibTableColumn
wfIpInterfaceUnnumAssocAddr = _WfIpInterfaceUnnumAssocAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 110),
    _WfIpInterfaceUnnumAssocAddr_Type()
)
wfIpInterfaceUnnumAssocAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceUnnumAssocAddr.setStatus("obsolete")


class _WfIpInterfaceUnnumAssocAlt_Type(Integer32):
    """Custom type wfIpInterfaceUnnumAssocAlt based on Integer32"""
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


_WfIpInterfaceUnnumAssocAlt_Type.__name__ = "Integer32"
_WfIpInterfaceUnnumAssocAlt_Object = MibTableColumn
wfIpInterfaceUnnumAssocAlt = _WfIpInterfaceUnnumAssocAlt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 111),
    _WfIpInterfaceUnnumAssocAlt_Type()
)
wfIpInterfaceUnnumAssocAlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceUnnumAssocAlt.setStatus("obsolete")


class _WfIpInterfaceAtmArpMode_Type(Integer32):
    """Custom type wfIpInterfaceAtmArpMode based on Integer32"""
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
        *(("client", 1),
          ("none", 3),
          ("server", 2))
    )


_WfIpInterfaceAtmArpMode_Type.__name__ = "Integer32"
_WfIpInterfaceAtmArpMode_Object = MibTableColumn
wfIpInterfaceAtmArpMode = _WfIpInterfaceAtmArpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 112),
    _WfIpInterfaceAtmArpMode_Type()
)
wfIpInterfaceAtmArpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpMode.setStatus("obsolete")
_WfIpInterfaceAtmArpServerAddress_Type = OctetString
_WfIpInterfaceAtmArpServerAddress_Object = MibTableColumn
wfIpInterfaceAtmArpServerAddress = _WfIpInterfaceAtmArpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 113),
    _WfIpInterfaceAtmArpServerAddress_Type()
)
wfIpInterfaceAtmArpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpServerAddress.setStatus("obsolete")


class _WfIpInterfaceAtmArpServerVcAgingEnable_Type(Integer32):
    """Custom type wfIpInterfaceAtmArpServerVcAgingEnable based on Integer32"""
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


_WfIpInterfaceAtmArpServerVcAgingEnable_Type.__name__ = "Integer32"
_WfIpInterfaceAtmArpServerVcAgingEnable_Object = MibTableColumn
wfIpInterfaceAtmArpServerVcAgingEnable = _WfIpInterfaceAtmArpServerVcAgingEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 114),
    _WfIpInterfaceAtmArpServerVcAgingEnable_Type()
)
wfIpInterfaceAtmArpServerVcAgingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpServerVcAgingEnable.setStatus("obsolete")


class _WfIpInterfaceAtmArpServerRegInterval_Type(Integer32):
    """Custom type wfIpInterfaceAtmArpServerRegInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(900,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("clientdefault", 900),
          ("serverdefault", 1200))
    )


_WfIpInterfaceAtmArpServerRegInterval_Type.__name__ = "Integer32"
_WfIpInterfaceAtmArpServerRegInterval_Object = MibTableColumn
wfIpInterfaceAtmArpServerRegInterval = _WfIpInterfaceAtmArpServerRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 115),
    _WfIpInterfaceAtmArpServerRegInterval_Type()
)
wfIpInterfaceAtmArpServerRegInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpServerRegInterval.setStatus("obsolete")


class _WfIpInterfaceAtmArpServerConnState_Type(Integer32):
    """Custom type wfIpInterfaceAtmArpServerConnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              12,
              20,
              28,
              36,
              44,
              52,
              60,
              260,
              268,
              276,
              284,
              292,
              300,
              308,
              316,
              516,
              524,
              532,
              540,
              548,
              556,
              564,
              572,
              772,
              780,
              788,
              796,
              804,
              812,
              820,
              828,
              1028)
        )
    )
    namedValues = NamedValues(
        *(("closednotreg", 4),
          ("closednotregarp", 12),
          ("closedreg", 516),
          ("closedregarp", 524),
          ("closedregfail", 772),
          ("closedregfailarp", 780),
          ("closedregingarpxxx", 268),
          ("closedregingxxx", 260),
          ("init", 1),
          ("noservercfg", 1028),
          ("openfailnotreg", 52),
          ("openfailnotregarp", 60),
          ("openfailreg", 564),
          ("openfailregarp", 572),
          ("openfailregfail", 820),
          ("openfailregfailarp", 828),
          ("openfailregingarpxxx", 316),
          ("openfailregingxxx", 308),
          ("openingnotreg", 20),
          ("openingnotregarp", 28),
          ("openingreg", 532),
          ("openingregarp", 540),
          ("openingregfail", 788),
          ("openingregfailarp", 796),
          ("openingregingarpxxx", 284),
          ("openingregingxxx", 276),
          ("opennotregarpxxx", 44),
          ("opennotregxxx", 36),
          ("openreg", 548),
          ("openregarpxxx", 556),
          ("openregfailarpxxx", 812),
          ("openregfailxxx", 804),
          ("openreging", 292),
          ("openregingarp", 300),
          ("wereserver", 2))
    )


_WfIpInterfaceAtmArpServerConnState_Type.__name__ = "Integer32"
_WfIpInterfaceAtmArpServerConnState_Object = MibTableColumn
wfIpInterfaceAtmArpServerConnState = _WfIpInterfaceAtmArpServerConnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 116),
    _WfIpInterfaceAtmArpServerConnState_Type()
)
wfIpInterfaceAtmArpServerConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpServerConnState.setStatus("obsolete")
_WfIpInterfaceAtmArpAttemptedCalls_Type = Counter32
_WfIpInterfaceAtmArpAttemptedCalls_Object = MibTableColumn
wfIpInterfaceAtmArpAttemptedCalls = _WfIpInterfaceAtmArpAttemptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 117),
    _WfIpInterfaceAtmArpAttemptedCalls_Type()
)
wfIpInterfaceAtmArpAttemptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpAttemptedCalls.setStatus("obsolete")
_WfIpInterfaceAtmArpFailRetryCalls_Type = Counter32
_WfIpInterfaceAtmArpFailRetryCalls_Object = MibTableColumn
wfIpInterfaceAtmArpFailRetryCalls = _WfIpInterfaceAtmArpFailRetryCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 118),
    _WfIpInterfaceAtmArpFailRetryCalls_Type()
)
wfIpInterfaceAtmArpFailRetryCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpFailRetryCalls.setStatus("obsolete")
_WfIpInterfaceAtmArpFailNoRetryCalls_Type = Counter32
_WfIpInterfaceAtmArpFailNoRetryCalls_Object = MibTableColumn
wfIpInterfaceAtmArpFailNoRetryCalls = _WfIpInterfaceAtmArpFailNoRetryCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 119),
    _WfIpInterfaceAtmArpFailNoRetryCalls_Type()
)
wfIpInterfaceAtmArpFailNoRetryCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpFailNoRetryCalls.setStatus("obsolete")
_WfIpInterfaceAtmArpSuccessfulCalls_Type = Counter32
_WfIpInterfaceAtmArpSuccessfulCalls_Object = MibTableColumn
wfIpInterfaceAtmArpSuccessfulCalls = _WfIpInterfaceAtmArpSuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 120),
    _WfIpInterfaceAtmArpSuccessfulCalls_Type()
)
wfIpInterfaceAtmArpSuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpSuccessfulCalls.setStatus("obsolete")
_WfIpInterfaceAtmArpAcceptedCalls_Type = Counter32
_WfIpInterfaceAtmArpAcceptedCalls_Object = MibTableColumn
wfIpInterfaceAtmArpAcceptedCalls = _WfIpInterfaceAtmArpAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 121),
    _WfIpInterfaceAtmArpAcceptedCalls_Type()
)
wfIpInterfaceAtmArpAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpAcceptedCalls.setStatus("obsolete")
_WfIpInterfaceAtmArpOpenSvcs_Type = Counter32
_WfIpInterfaceAtmArpOpenSvcs_Object = MibTableColumn
wfIpInterfaceAtmArpOpenSvcs = _WfIpInterfaceAtmArpOpenSvcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 122),
    _WfIpInterfaceAtmArpOpenSvcs_Type()
)
wfIpInterfaceAtmArpOpenSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpOpenSvcs.setStatus("obsolete")
_WfIpInterfaceAtmArpMisc_Type = Integer32
_WfIpInterfaceAtmArpMisc_Object = MibTableColumn
wfIpInterfaceAtmArpMisc = _WfIpInterfaceAtmArpMisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 123),
    _WfIpInterfaceAtmArpMisc_Type()
)
wfIpInterfaceAtmArpMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpMisc.setStatus("obsolete")
_WfIpInterfaceAtmArpMisc2_Type = Integer32
_WfIpInterfaceAtmArpMisc2_Object = MibTableColumn
wfIpInterfaceAtmArpMisc2 = _WfIpInterfaceAtmArpMisc2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 124),
    _WfIpInterfaceAtmArpMisc2_Type()
)
wfIpInterfaceAtmArpMisc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceAtmArpMisc2.setStatus("obsolete")
_WfIpInterfaceMcastInPkts_Type = Counter32
_WfIpInterfaceMcastInPkts_Object = MibTableColumn
wfIpInterfaceMcastInPkts = _WfIpInterfaceMcastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 125),
    _WfIpInterfaceMcastInPkts_Type()
)
wfIpInterfaceMcastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceMcastInPkts.setStatus("obsolete")
_WfIpInterfaceMcastOutPkts_Type = Counter32
_WfIpInterfaceMcastOutPkts_Object = MibTableColumn
wfIpInterfaceMcastOutPkts = _WfIpInterfaceMcastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 126),
    _WfIpInterfaceMcastOutPkts_Type()
)
wfIpInterfaceMcastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInterfaceMcastOutPkts.setStatus("obsolete")


class _WfIpInterfaceTrEsArpType_Type(Integer32):
    """Custom type wfIpInterfaceTrEsArpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("are", 2),
          ("ste", 1))
    )


_WfIpInterfaceTrEsArpType_Type.__name__ = "Integer32"
_WfIpInterfaceTrEsArpType_Object = MibTableColumn
wfIpInterfaceTrEsArpType = _WfIpInterfaceTrEsArpType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 4, 1, 127),
    _WfIpInterfaceTrEsArpType_Type()
)
wfIpInterfaceTrEsArpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpInterfaceTrEsArpType.setStatus("obsolete")
_WfIpStaticRouteTable_Object = MibTable
wfIpStaticRouteTable = _WfIpStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5)
)
if mibBuilder.loadTexts:
    wfIpStaticRouteTable.setStatus("mandatory")
_WfIpStaticRouteEntry_Object = MibTableRow
wfIpStaticRouteEntry = _WfIpStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1)
)
wfIpStaticRouteEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpSrIpAddress"),
    (0, "Wellfleet-IP-MIB", "wfIpSrIpNetMask"),
    (0, "Wellfleet-IP-MIB", "wfIpSrIpAddressRt"),
)
if mibBuilder.loadTexts:
    wfIpStaticRouteEntry.setStatus("mandatory")


class _WfIpSrCreate_Type(Integer32):
    """Custom type wfIpSrCreate based on Integer32"""
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


_WfIpSrCreate_Type.__name__ = "Integer32"
_WfIpSrCreate_Object = MibTableColumn
wfIpSrCreate = _WfIpSrCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 1),
    _WfIpSrCreate_Type()
)
wfIpSrCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrCreate.setStatus("mandatory")


class _WfIpSrEnable_Type(Integer32):
    """Custom type wfIpSrEnable based on Integer32"""
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


_WfIpSrEnable_Type.__name__ = "Integer32"
_WfIpSrEnable_Object = MibTableColumn
wfIpSrEnable = _WfIpSrEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 2),
    _WfIpSrEnable_Type()
)
wfIpSrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrEnable.setStatus("mandatory")
_WfIpSrIpAddress_Type = IpAddress
_WfIpSrIpAddress_Object = MibTableColumn
wfIpSrIpAddress = _WfIpSrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 3),
    _WfIpSrIpAddress_Type()
)
wfIpSrIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrIpAddress.setStatus("mandatory")
_WfIpSrIpNetMask_Type = IpAddress
_WfIpSrIpNetMask_Object = MibTableColumn
wfIpSrIpNetMask = _WfIpSrIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 4),
    _WfIpSrIpNetMask_Type()
)
wfIpSrIpNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrIpNetMask.setStatus("mandatory")


class _WfIpSrCost_Type(Integer32):
    """Custom type wfIpSrCost based on Integer32"""
    defaultValue = 1


_WfIpSrCost_Object = MibTableColumn
wfIpSrCost = _WfIpSrCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 5),
    _WfIpSrCost_Type()
)
wfIpSrCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrCost.setStatus("mandatory")
_WfIpSrNextHopAddr_Type = IpAddress
_WfIpSrNextHopAddr_Object = MibTableColumn
wfIpSrNextHopAddr = _WfIpSrNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 6),
    _WfIpSrNextHopAddr_Type()
)
wfIpSrNextHopAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrNextHopAddr.setStatus("mandatory")
_WfIpSrNextHopMask_Type = IpAddress
_WfIpSrNextHopMask_Object = MibTableColumn
wfIpSrNextHopMask = _WfIpSrNextHopMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 7),
    _WfIpSrNextHopMask_Type()
)
wfIpSrNextHopMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrNextHopMask.setStatus("obsolete")


class _WfIpSrPreference_Type(Integer32):
    """Custom type wfIpSrPreference based on Integer32"""
    defaultValue = 16


_WfIpSrPreference_Object = MibTableColumn
wfIpSrPreference = _WfIpSrPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 8),
    _WfIpSrPreference_Type()
)
wfIpSrPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrPreference.setStatus("mandatory")
_WfIpSrIpAddressRt_Type = Integer32
_WfIpSrIpAddressRt_Object = MibTableColumn
wfIpSrIpAddressRt = _WfIpSrIpAddressRt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 9),
    _WfIpSrIpAddressRt_Type()
)
wfIpSrIpAddressRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrIpAddressRt.setStatus("mandatory")


class _WfIpSrValid_Type(Integer32):
    """Custom type wfIpSrValid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpSrValid_Type.__name__ = "Integer32"
_WfIpSrValid_Object = MibTableColumn
wfIpSrValid = _WfIpSrValid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 10),
    _WfIpSrValid_Type()
)
wfIpSrValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpSrValid.setStatus("mandatory")
_WfIpSrUnnumCct_Type = Integer32
_WfIpSrUnnumCct_Object = MibTableColumn
wfIpSrUnnumCct = _WfIpSrUnnumCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 5, 1, 11),
    _WfIpSrUnnumCct_Type()
)
wfIpSrUnnumCct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpSrUnnumCct.setStatus("mandatory")
_WfIpAdjacentHostTable_Object = MibTable
wfIpAdjacentHostTable = _WfIpAdjacentHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6)
)
if mibBuilder.loadTexts:
    wfIpAdjacentHostTable.setStatus("mandatory")
_WfIpAdjacentHostEntry_Object = MibTableRow
wfIpAdjacentHostEntry = _WfIpAdjacentHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1)
)
wfIpAdjacentHostEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpAdjHostIpAddress"),
)
if mibBuilder.loadTexts:
    wfIpAdjacentHostEntry.setStatus("mandatory")


class _WfIpAdjHostCreate_Type(Integer32):
    """Custom type wfIpAdjHostCreate based on Integer32"""
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


_WfIpAdjHostCreate_Type.__name__ = "Integer32"
_WfIpAdjHostCreate_Object = MibTableColumn
wfIpAdjHostCreate = _WfIpAdjHostCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 1),
    _WfIpAdjHostCreate_Type()
)
wfIpAdjHostCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostCreate.setStatus("mandatory")


class _WfIpAdjHostEnable_Type(Integer32):
    """Custom type wfIpAdjHostEnable based on Integer32"""
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


_WfIpAdjHostEnable_Type.__name__ = "Integer32"
_WfIpAdjHostEnable_Object = MibTableColumn
wfIpAdjHostEnable = _WfIpAdjHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 2),
    _WfIpAdjHostEnable_Type()
)
wfIpAdjHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostEnable.setStatus("mandatory")
_WfIpAdjHostIpAddress_Type = IpAddress
_WfIpAdjHostIpAddress_Object = MibTableColumn
wfIpAdjHostIpAddress = _WfIpAdjHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 3),
    _WfIpAdjHostIpAddress_Type()
)
wfIpAdjHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdjHostIpAddress.setStatus("mandatory")
_WfIpAdjHostIntf_Type = IpAddress
_WfIpAdjHostIntf_Object = MibTableColumn
wfIpAdjHostIntf = _WfIpAdjHostIntf_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 4),
    _WfIpAdjHostIntf_Type()
)
wfIpAdjHostIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostIntf.setStatus("mandatory")
_WfIpAdjHostIntfMask_Type = IpAddress
_WfIpAdjHostIntfMask_Object = MibTableColumn
wfIpAdjHostIntfMask = _WfIpAdjHostIntfMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 5),
    _WfIpAdjHostIntfMask_Type()
)
wfIpAdjHostIntfMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostIntfMask.setStatus("mandatory")
_WfIpAdjHostMacAddr_Type = OctetString
_WfIpAdjHostMacAddr_Object = MibTableColumn
wfIpAdjHostMacAddr = _WfIpAdjHostMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 6),
    _WfIpAdjHostMacAddr_Type()
)
wfIpAdjHostMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostMacAddr.setStatus("mandatory")


class _WfIpAdjHostEncaps_Type(Integer32):
    """Custom type wfIpAdjHostEncaps based on Integer32"""
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
        *(("ddn", 4),
          ("enet", 1),
          ("gre", 7),
          ("null", 5),
          ("pdn", 3),
          ("snap", 2),
          ("snapip", 6))
    )


_WfIpAdjHostEncaps_Type.__name__ = "Integer32"
_WfIpAdjHostEncaps_Object = MibTableColumn
wfIpAdjHostEncaps = _WfIpAdjHostEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 7),
    _WfIpAdjHostEncaps_Type()
)
wfIpAdjHostEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostEncaps.setStatus("mandatory")


class _WfIpAdjHostValid_Type(Integer32):
    """Custom type wfIpAdjHostValid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_WfIpAdjHostValid_Type.__name__ = "Integer32"
_WfIpAdjHostValid_Object = MibTableColumn
wfIpAdjHostValid = _WfIpAdjHostValid_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 8),
    _WfIpAdjHostValid_Type()
)
wfIpAdjHostValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdjHostValid.setStatus("mandatory")
_WfIpAdjHostX121Addr_Type = DisplayString
_WfIpAdjHostX121Addr_Object = MibTableColumn
wfIpAdjHostX121Addr = _WfIpAdjHostX121Addr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 9),
    _WfIpAdjHostX121Addr_Type()
)
wfIpAdjHostX121Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostX121Addr.setStatus("mandatory")
_WfIpAdjHostSubaddr_Type = DisplayString
_WfIpAdjHostSubaddr_Object = MibTableColumn
wfIpAdjHostSubaddr = _WfIpAdjHostSubaddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 10),
    _WfIpAdjHostSubaddr_Type()
)
wfIpAdjHostSubaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostSubaddr.setStatus("mandatory")


class _WfIpAdjHostTypeOfNumber_Type(Integer32):
    """Custom type wfIpAdjHostTypeOfNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("international", 2),
          ("unknown", 1))
    )


_WfIpAdjHostTypeOfNumber_Type.__name__ = "Integer32"
_WfIpAdjHostTypeOfNumber_Object = MibTableColumn
wfIpAdjHostTypeOfNumber = _WfIpAdjHostTypeOfNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 11),
    _WfIpAdjHostTypeOfNumber_Type()
)
wfIpAdjHostTypeOfNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostTypeOfNumber.setStatus("mandatory")


class _WfIpAdjHostType_Type(Integer32):
    """Custom type wfIpAdjHostType based on Integer32"""
    defaultValue = 2

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
        *(("default", 2),
          ("frdlci", 4),
          ("fre164", 1),
          ("frx121", 3),
          ("gre", 5))
    )


_WfIpAdjHostType_Type.__name__ = "Integer32"
_WfIpAdjHostType_Object = MibTableColumn
wfIpAdjHostType = _WfIpAdjHostType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 12),
    _WfIpAdjHostType_Type()
)
wfIpAdjHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostType.setStatus("mandatory")
_WfIpAdjHostGreConnName_Type = DisplayString
_WfIpAdjHostGreConnName_Object = MibTableColumn
wfIpAdjHostGreConnName = _WfIpAdjHostGreConnName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 6, 1, 13),
    _WfIpAdjHostGreConnName_Type()
)
wfIpAdjHostGreConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAdjHostGreConnName.setStatus("mandatory")
_WfIpTrafficFilterTable_Object = MibTable
wfIpTrafficFilterTable = _WfIpTrafficFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7)
)
if mibBuilder.loadTexts:
    wfIpTrafficFilterTable.setStatus("mandatory")
_WfIpTrafficFilterEntry_Object = MibTableRow
wfIpTrafficFilterEntry = _WfIpTrafficFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1)
)
wfIpTrafficFilterEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpTrafficFilterInterface"),
    (0, "Wellfleet-IP-MIB", "wfIpTrafficFilterCircuit"),
    (0, "Wellfleet-IP-MIB", "wfIpTrafficFilterRuleNumber"),
    (0, "Wellfleet-IP-MIB", "wfIpTrafficFilterFragment"),
)
if mibBuilder.loadTexts:
    wfIpTrafficFilterEntry.setStatus("mandatory")


class _WfIpTrafficFilterCreate_Type(Integer32):
    """Custom type wfIpTrafficFilterCreate based on Integer32"""
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


_WfIpTrafficFilterCreate_Type.__name__ = "Integer32"
_WfIpTrafficFilterCreate_Object = MibTableColumn
wfIpTrafficFilterCreate = _WfIpTrafficFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 1),
    _WfIpTrafficFilterCreate_Type()
)
wfIpTrafficFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterCreate.setStatus("mandatory")


class _WfIpTrafficFilterEnable_Type(Integer32):
    """Custom type wfIpTrafficFilterEnable based on Integer32"""
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


_WfIpTrafficFilterEnable_Type.__name__ = "Integer32"
_WfIpTrafficFilterEnable_Object = MibTableColumn
wfIpTrafficFilterEnable = _WfIpTrafficFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 2),
    _WfIpTrafficFilterEnable_Type()
)
wfIpTrafficFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterEnable.setStatus("mandatory")


class _WfIpTrafficFilterStatus_Type(Integer32):
    """Custom type wfIpTrafficFilterStatus based on Integer32"""
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


_WfIpTrafficFilterStatus_Type.__name__ = "Integer32"
_WfIpTrafficFilterStatus_Object = MibTableColumn
wfIpTrafficFilterStatus = _WfIpTrafficFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 3),
    _WfIpTrafficFilterStatus_Type()
)
wfIpTrafficFilterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterStatus.setStatus("mandatory")
_WfIpTrafficFilterCounter_Type = Counter32
_WfIpTrafficFilterCounter_Object = MibTableColumn
wfIpTrafficFilterCounter = _WfIpTrafficFilterCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 4),
    _WfIpTrafficFilterCounter_Type()
)
wfIpTrafficFilterCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterCounter.setStatus("mandatory")
_WfIpTrafficFilterDefinition_Type = Opaque
_WfIpTrafficFilterDefinition_Object = MibTableColumn
wfIpTrafficFilterDefinition = _WfIpTrafficFilterDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 5),
    _WfIpTrafficFilterDefinition_Type()
)
wfIpTrafficFilterDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterDefinition.setStatus("mandatory")
_WfIpTrafficFilterReserved_Type = Integer32
_WfIpTrafficFilterReserved_Object = MibTableColumn
wfIpTrafficFilterReserved = _WfIpTrafficFilterReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 6),
    _WfIpTrafficFilterReserved_Type()
)
wfIpTrafficFilterReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterReserved.setStatus("mandatory")
_WfIpTrafficFilterInterface_Type = IpAddress
_WfIpTrafficFilterInterface_Object = MibTableColumn
wfIpTrafficFilterInterface = _WfIpTrafficFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 7),
    _WfIpTrafficFilterInterface_Type()
)
wfIpTrafficFilterInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterInterface.setStatus("mandatory")
_WfIpTrafficFilterCircuit_Type = Integer32
_WfIpTrafficFilterCircuit_Object = MibTableColumn
wfIpTrafficFilterCircuit = _WfIpTrafficFilterCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 8),
    _WfIpTrafficFilterCircuit_Type()
)
wfIpTrafficFilterCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterCircuit.setStatus("mandatory")
_WfIpTrafficFilterRuleNumber_Type = Integer32
_WfIpTrafficFilterRuleNumber_Object = MibTableColumn
wfIpTrafficFilterRuleNumber = _WfIpTrafficFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 9),
    _WfIpTrafficFilterRuleNumber_Type()
)
wfIpTrafficFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterRuleNumber.setStatus("mandatory")
_WfIpTrafficFilterFragment_Type = Integer32
_WfIpTrafficFilterFragment_Object = MibTableColumn
wfIpTrafficFilterFragment = _WfIpTrafficFilterFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 10),
    _WfIpTrafficFilterFragment_Type()
)
wfIpTrafficFilterFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterFragment.setStatus("mandatory")
_WfIpTrafficFilterName_Type = DisplayString
_WfIpTrafficFilterName_Object = MibTableColumn
wfIpTrafficFilterName = _WfIpTrafficFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 11),
    _WfIpTrafficFilterName_Type()
)
wfIpTrafficFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterName.setStatus("mandatory")
_WfIpTrafficFilterPrecedence_Type = Integer32
_WfIpTrafficFilterPrecedence_Object = MibTableColumn
wfIpTrafficFilterPrecedence = _WfIpTrafficFilterPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 12),
    _WfIpTrafficFilterPrecedence_Type()
)
wfIpTrafficFilterPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterPrecedence.setStatus("mandatory")


class _WfIpTrafficFilterType_Type(Integer32):
    """Custom type wfIpTrafficFilterType based on Integer32"""
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
        *(("copsdiffserv", 3),
          ("dynamicdiffserv", 4),
          ("ip", 1),
          ("staticdiffserv", 2))
    )


_WfIpTrafficFilterType_Type.__name__ = "Integer32"
_WfIpTrafficFilterType_Object = MibTableColumn
wfIpTrafficFilterType = _WfIpTrafficFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 13),
    _WfIpTrafficFilterType_Type()
)
wfIpTrafficFilterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterType.setStatus("mandatory")
_WfIpTrafficFilterDSOopCounter_Type = Counter32
_WfIpTrafficFilterDSOopCounter_Object = MibTableColumn
wfIpTrafficFilterDSOopCounter = _WfIpTrafficFilterDSOopCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 14),
    _WfIpTrafficFilterDSOopCounter_Type()
)
wfIpTrafficFilterDSOopCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterDSOopCounter.setStatus("mandatory")


class _WfIpTrafficFilterDSPrecedence_Type(Integer32):
    """Custom type wfIpTrafficFilterDSPrecedence based on Integer32"""
    defaultValue = 16


_WfIpTrafficFilterDSPrecedence_Object = MibTableColumn
wfIpTrafficFilterDSPrecedence = _WfIpTrafficFilterDSPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 15),
    _WfIpTrafficFilterDSPrecedence_Type()
)
wfIpTrafficFilterDSPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTrafficFilterDSPrecedence.setStatus("mandatory")
_WfIpTrafficFilterDSBytes_Type = Counter32
_WfIpTrafficFilterDSBytes_Object = MibTableColumn
wfIpTrafficFilterDSBytes = _WfIpTrafficFilterDSBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 16),
    _WfIpTrafficFilterDSBytes_Type()
)
wfIpTrafficFilterDSBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterDSBytes.setStatus("mandatory")
_WfIpTrafficFilterDSOopBytes_Type = Counter32
_WfIpTrafficFilterDSOopBytes_Object = MibTableColumn
wfIpTrafficFilterDSOopBytes = _WfIpTrafficFilterDSOopBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 7, 1, 17),
    _WfIpTrafficFilterDSOopBytes_Type()
)
wfIpTrafficFilterDSOopBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTrafficFilterDSOopBytes.setStatus("mandatory")
_WfIpForwardTable_Object = MibTable
wfIpForwardTable = _WfIpForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16)
)
if mibBuilder.loadTexts:
    wfIpForwardTable.setStatus("mandatory")
_WfIpForwardEntry_Object = MibTableRow
wfIpForwardEntry = _WfIpForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1)
)
wfIpForwardEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpForwardDest"),
    (0, "Wellfleet-IP-MIB", "wfIpForwardMask"),
    (0, "Wellfleet-IP-MIB", "wfIpForwardProto"),
    (0, "Wellfleet-IP-MIB", "wfIpForwardPolicy"),
    (0, "Wellfleet-IP-MIB", "wfIpForwardNextHop"),
)
if mibBuilder.loadTexts:
    wfIpForwardEntry.setStatus("mandatory")
_WfIpForwardDest_Type = IpAddress
_WfIpForwardDest_Object = MibTableColumn
wfIpForwardDest = _WfIpForwardDest_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 1),
    _WfIpForwardDest_Type()
)
wfIpForwardDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardDest.setStatus("mandatory")
_WfIpForwardMask_Type = IpAddress
_WfIpForwardMask_Object = MibTableColumn
wfIpForwardMask = _WfIpForwardMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 2),
    _WfIpForwardMask_Type()
)
wfIpForwardMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardMask.setStatus("mandatory")
_WfIpForwardPolicy_Type = Integer32
_WfIpForwardPolicy_Object = MibTableColumn
wfIpForwardPolicy = _WfIpForwardPolicy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 3),
    _WfIpForwardPolicy_Type()
)
wfIpForwardPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardPolicy.setStatus("mandatory")
_WfIpForwardNextHop_Type = IpAddress
_WfIpForwardNextHop_Object = MibTableColumn
wfIpForwardNextHop = _WfIpForwardNextHop_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 4),
    _WfIpForwardNextHop_Type()
)
wfIpForwardNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardNextHop.setStatus("mandatory")
_WfIpForwardIfIndex_Type = Integer32
_WfIpForwardIfIndex_Object = MibTableColumn
wfIpForwardIfIndex = _WfIpForwardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 5),
    _WfIpForwardIfIndex_Type()
)
wfIpForwardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardIfIndex.setStatus("mandatory")


class _WfIpForwardType_Type(Integer32):
    """Custom type wfIpForwardType based on Integer32"""
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
        *(("direct", 3),
          ("indirect", 4),
          ("invalid", 2),
          ("other", 1))
    )


_WfIpForwardType_Type.__name__ = "Integer32"
_WfIpForwardType_Object = MibTableColumn
wfIpForwardType = _WfIpForwardType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 6),
    _WfIpForwardType_Type()
)
wfIpForwardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardType.setStatus("mandatory")


class _WfIpForwardProto_Type(Integer32):
    """Custom type wfIpForwardProto based on Integer32"""
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
              8,
              9,
              10,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ahb", 16),
          ("asr", 17),
          ("bgp", 14),
          ("egp", 5),
          ("esis", 10),
          ("ggp", 6),
          ("hello", 7),
          ("icmp", 4),
          ("idpr", 15),
          ("isis", 9),
          ("local", 2),
          ("netmgmt", 3),
          ("ospf", 13),
          ("other", 1),
          ("rip", 8))
    )


_WfIpForwardProto_Type.__name__ = "Integer32"
_WfIpForwardProto_Object = MibTableColumn
wfIpForwardProto = _WfIpForwardProto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 7),
    _WfIpForwardProto_Type()
)
wfIpForwardProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardProto.setStatus("mandatory")
_WfIpForwardAge_Type = Integer32
_WfIpForwardAge_Object = MibTableColumn
wfIpForwardAge = _WfIpForwardAge_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 8),
    _WfIpForwardAge_Type()
)
wfIpForwardAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardAge.setStatus("mandatory")
_WfIpForwardInfo_Type = ObjectIdentifier
_WfIpForwardInfo_Object = MibTableColumn
wfIpForwardInfo = _WfIpForwardInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 9),
    _WfIpForwardInfo_Type()
)
wfIpForwardInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardInfo.setStatus("mandatory")
_WfIpForwardNextHopAS_Type = Integer32
_WfIpForwardNextHopAS_Object = MibTableColumn
wfIpForwardNextHopAS = _WfIpForwardNextHopAS_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 10),
    _WfIpForwardNextHopAS_Type()
)
wfIpForwardNextHopAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardNextHopAS.setStatus("mandatory")
_WfIpForwardMetric1_Type = Integer32
_WfIpForwardMetric1_Object = MibTableColumn
wfIpForwardMetric1 = _WfIpForwardMetric1_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 11),
    _WfIpForwardMetric1_Type()
)
wfIpForwardMetric1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardMetric1.setStatus("mandatory")
_WfIpForwardMetric2_Type = Integer32
_WfIpForwardMetric2_Object = MibTableColumn
wfIpForwardMetric2 = _WfIpForwardMetric2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 12),
    _WfIpForwardMetric2_Type()
)
wfIpForwardMetric2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardMetric2.setStatus("mandatory")
_WfIpForwardMetric3_Type = Integer32
_WfIpForwardMetric3_Object = MibTableColumn
wfIpForwardMetric3 = _WfIpForwardMetric3_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 13),
    _WfIpForwardMetric3_Type()
)
wfIpForwardMetric3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardMetric3.setStatus("mandatory")
_WfIpForwardMetric4_Type = Integer32
_WfIpForwardMetric4_Object = MibTableColumn
wfIpForwardMetric4 = _WfIpForwardMetric4_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 14),
    _WfIpForwardMetric4_Type()
)
wfIpForwardMetric4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardMetric4.setStatus("mandatory")
_WfIpForwardMetric5_Type = Integer32
_WfIpForwardMetric5_Object = MibTableColumn
wfIpForwardMetric5 = _WfIpForwardMetric5_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 16, 1, 15),
    _WfIpForwardMetric5_Type()
)
wfIpForwardMetric5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpForwardMetric5.setStatus("mandatory")
_WfRdiscIntfTable_Object = MibTable
wfRdiscIntfTable = _WfRdiscIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17)
)
if mibBuilder.loadTexts:
    wfRdiscIntfTable.setStatus("mandatory")
_WfRdiscIntfEntry_Object = MibTableRow
wfRdiscIntfEntry = _WfRdiscIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1)
)
wfRdiscIntfEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfRdiscInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfRdiscIntfEntry.setStatus("mandatory")


class _WfRdiscInterfaceCreate_Type(Integer32):
    """Custom type wfRdiscInterfaceCreate based on Integer32"""
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


_WfRdiscInterfaceCreate_Type.__name__ = "Integer32"
_WfRdiscInterfaceCreate_Object = MibTableColumn
wfRdiscInterfaceCreate = _WfRdiscInterfaceCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 1),
    _WfRdiscInterfaceCreate_Type()
)
wfRdiscInterfaceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRdiscInterfaceCreate.setStatus("mandatory")


class _WfRdiscInterfaceEnable_Type(Integer32):
    """Custom type wfRdiscInterfaceEnable based on Integer32"""
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


_WfRdiscInterfaceEnable_Type.__name__ = "Integer32"
_WfRdiscInterfaceEnable_Object = MibTableColumn
wfRdiscInterfaceEnable = _WfRdiscInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 2),
    _WfRdiscInterfaceEnable_Type()
)
wfRdiscInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRdiscInterfaceEnable.setStatus("mandatory")


class _WfRdiscInterfaceState_Type(Integer32):
    """Custom type wfRdiscInterfaceState based on Integer32"""
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


_WfRdiscInterfaceState_Type.__name__ = "Integer32"
_WfRdiscInterfaceState_Object = MibTableColumn
wfRdiscInterfaceState = _WfRdiscInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 3),
    _WfRdiscInterfaceState_Type()
)
wfRdiscInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRdiscInterfaceState.setStatus("mandatory")
_WfRdiscInterfaceIndex_Type = IpAddress
_WfRdiscInterfaceIndex_Object = MibTableColumn
wfRdiscInterfaceIndex = _WfRdiscInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 4),
    _WfRdiscInterfaceIndex_Type()
)
wfRdiscInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRdiscInterfaceIndex.setStatus("mandatory")


class _WfRdiscInterfaceBcast_Type(Integer32):
    """Custom type wfRdiscInterfaceBcast based on Integer32"""
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
        *(("direct", 3),
          ("local", 2),
          ("mcast", 1))
    )


_WfRdiscInterfaceBcast_Type.__name__ = "Integer32"
_WfRdiscInterfaceBcast_Object = MibTableColumn
wfRdiscInterfaceBcast = _WfRdiscInterfaceBcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 5),
    _WfRdiscInterfaceBcast_Type()
)
wfRdiscInterfaceBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRdiscInterfaceBcast.setStatus("mandatory")


class _WfRdiscInterfaceMinIntrvl_Type(Integer32):
    """Custom type wfRdiscInterfaceMinIntrvl based on Integer32"""
    defaultValue = 450


_WfRdiscInterfaceMinIntrvl_Object = MibTableColumn
wfRdiscInterfaceMinIntrvl = _WfRdiscInterfaceMinIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 6),
    _WfRdiscInterfaceMinIntrvl_Type()
)
wfRdiscInterfaceMinIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRdiscInterfaceMinIntrvl.setStatus("mandatory")


class _WfRdiscInterfaceMaxIntrvl_Type(Integer32):
    """Custom type wfRdiscInterfaceMaxIntrvl based on Integer32"""
    defaultValue = 600


_WfRdiscInterfaceMaxIntrvl_Object = MibTableColumn
wfRdiscInterfaceMaxIntrvl = _WfRdiscInterfaceMaxIntrvl_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 7),
    _WfRdiscInterfaceMaxIntrvl_Type()
)
wfRdiscInterfaceMaxIntrvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRdiscInterfaceMaxIntrvl.setStatus("mandatory")


class _WfRdiscInterfaceLifetime_Type(Integer32):
    """Custom type wfRdiscInterfaceLifetime based on Integer32"""
    defaultValue = 1800


_WfRdiscInterfaceLifetime_Object = MibTableColumn
wfRdiscInterfaceLifetime = _WfRdiscInterfaceLifetime_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 8),
    _WfRdiscInterfaceLifetime_Type()
)
wfRdiscInterfaceLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRdiscInterfaceLifetime.setStatus("mandatory")
_WfRdiscInterfacePref_Type = Integer32
_WfRdiscInterfacePref_Object = MibTableColumn
wfRdiscInterfacePref = _WfRdiscInterfacePref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 9),
    _WfRdiscInterfacePref_Type()
)
wfRdiscInterfacePref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRdiscInterfacePref.setStatus("mandatory")
_WfRdiscInterfaceUnicastAdvt_Type = Counter32
_WfRdiscInterfaceUnicastAdvt_Object = MibTableColumn
wfRdiscInterfaceUnicastAdvt = _WfRdiscInterfaceUnicastAdvt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 10),
    _WfRdiscInterfaceUnicastAdvt_Type()
)
wfRdiscInterfaceUnicastAdvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRdiscInterfaceUnicastAdvt.setStatus("mandatory")
_WfRdiscInterfaceMulticastAdvt_Type = Counter32
_WfRdiscInterfaceMulticastAdvt_Object = MibTableColumn
wfRdiscInterfaceMulticastAdvt = _WfRdiscInterfaceMulticastAdvt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 11),
    _WfRdiscInterfaceMulticastAdvt_Type()
)
wfRdiscInterfaceMulticastAdvt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRdiscInterfaceMulticastAdvt.setStatus("mandatory")
_WfRdiscInterfaceDynamicPref_Type = Integer32
_WfRdiscInterfaceDynamicPref_Object = MibTableColumn
wfRdiscInterfaceDynamicPref = _WfRdiscInterfaceDynamicPref_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 17, 1, 12),
    _WfRdiscInterfaceDynamicPref_Type()
)
wfRdiscInterfaceDynamicPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRdiscInterfaceDynamicPref.setStatus("obsolete")
_WfIpNetToMediaEntryTable_Object = MibTable
wfIpNetToMediaEntryTable = _WfIpNetToMediaEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 18)
)
if mibBuilder.loadTexts:
    wfIpNetToMediaEntryTable.setStatus("mandatory")
_WfIpNetToMediaEntry_Object = MibTableRow
wfIpNetToMediaEntry = _WfIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 18, 1)
)
wfIpNetToMediaEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpNetToMediaIfIndex"),
    (0, "Wellfleet-IP-MIB", "wfIpNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    wfIpNetToMediaEntry.setStatus("mandatory")
_WfIpNetToMediaIfIndex_Type = Integer32
_WfIpNetToMediaIfIndex_Object = MibTableColumn
wfIpNetToMediaIfIndex = _WfIpNetToMediaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 18, 1, 1),
    _WfIpNetToMediaIfIndex_Type()
)
wfIpNetToMediaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpNetToMediaIfIndex.setStatus("mandatory")
_WfIpNetToMediaPhysAddress_Type = OctetString
_WfIpNetToMediaPhysAddress_Object = MibTableColumn
wfIpNetToMediaPhysAddress = _WfIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 18, 1, 2),
    _WfIpNetToMediaPhysAddress_Type()
)
wfIpNetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpNetToMediaPhysAddress.setStatus("mandatory")
_WfIpNetToMediaNetAddress_Type = IpAddress
_WfIpNetToMediaNetAddress_Object = MibTableColumn
wfIpNetToMediaNetAddress = _WfIpNetToMediaNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 18, 1, 3),
    _WfIpNetToMediaNetAddress_Type()
)
wfIpNetToMediaNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpNetToMediaNetAddress.setStatus("mandatory")


class _WfIpNetToMediaType_Type(Integer32):
    """Custom type wfIpNetToMediaType based on Integer32"""
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
        *(("dynamic", 3),
          ("invalid", 2),
          ("other", 1),
          ("static", 4))
    )


_WfIpNetToMediaType_Type.__name__ = "Integer32"
_WfIpNetToMediaType_Object = MibTableColumn
wfIpNetToMediaType = _WfIpNetToMediaType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 18, 1, 4),
    _WfIpNetToMediaType_Type()
)
wfIpNetToMediaType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpNetToMediaType.setStatus("mandatory")
_WfIpAccCtrlFilterTable_Object = MibTable
wfIpAccCtrlFilterTable = _WfIpAccCtrlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19)
)
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterTable.setStatus("mandatory")
_WfIpAccCtrlFilterEntry_Object = MibTableRow
wfIpAccCtrlFilterEntry = _WfIpAccCtrlFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1)
)
wfIpAccCtrlFilterEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpAccCtrlFilterIndex"),
)
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterEntry.setStatus("mandatory")


class _WfIpAccCtrlFilterCreate_Type(Integer32):
    """Custom type wfIpAccCtrlFilterCreate based on Integer32"""
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


_WfIpAccCtrlFilterCreate_Type.__name__ = "Integer32"
_WfIpAccCtrlFilterCreate_Object = MibTableColumn
wfIpAccCtrlFilterCreate = _WfIpAccCtrlFilterCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 1),
    _WfIpAccCtrlFilterCreate_Type()
)
wfIpAccCtrlFilterCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterCreate.setStatus("mandatory")


class _WfIpAccCtrlFilterEnable_Type(Integer32):
    """Custom type wfIpAccCtrlFilterEnable based on Integer32"""
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


_WfIpAccCtrlFilterEnable_Type.__name__ = "Integer32"
_WfIpAccCtrlFilterEnable_Object = MibTableColumn
wfIpAccCtrlFilterEnable = _WfIpAccCtrlFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 2),
    _WfIpAccCtrlFilterEnable_Type()
)
wfIpAccCtrlFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterEnable.setStatus("mandatory")
_WfIpAccCtrlFilterIndex_Type = Integer32
_WfIpAccCtrlFilterIndex_Object = MibTableColumn
wfIpAccCtrlFilterIndex = _WfIpAccCtrlFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 3),
    _WfIpAccCtrlFilterIndex_Type()
)
wfIpAccCtrlFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterIndex.setStatus("mandatory")
_WfIpAccCtrlFilterName_Type = DisplayString
_WfIpAccCtrlFilterName_Object = MibTableColumn
wfIpAccCtrlFilterName = _WfIpAccCtrlFilterName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 4),
    _WfIpAccCtrlFilterName_Type()
)
wfIpAccCtrlFilterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterName.setStatus("mandatory")
_WfIpAccCtrlFilterNetwork_Type = IpAddress
_WfIpAccCtrlFilterNetwork_Object = MibTableColumn
wfIpAccCtrlFilterNetwork = _WfIpAccCtrlFilterNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 5),
    _WfIpAccCtrlFilterNetwork_Type()
)
wfIpAccCtrlFilterNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterNetwork.setStatus("mandatory")
_WfIpAccCtrlFilterNetworkMask_Type = IpAddress
_WfIpAccCtrlFilterNetworkMask_Object = MibTableColumn
wfIpAccCtrlFilterNetworkMask = _WfIpAccCtrlFilterNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 6),
    _WfIpAccCtrlFilterNetworkMask_Type()
)
wfIpAccCtrlFilterNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterNetworkMask.setStatus("mandatory")


class _WfIpAccCtrlFilterAction_Type(Integer32):
    """Custom type wfIpAccCtrlFilterAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 2))
    )


_WfIpAccCtrlFilterAction_Type.__name__ = "Integer32"
_WfIpAccCtrlFilterAction_Object = MibTableColumn
wfIpAccCtrlFilterAction = _WfIpAccCtrlFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 7),
    _WfIpAccCtrlFilterAction_Type()
)
wfIpAccCtrlFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterAction.setStatus("mandatory")
_WfIpAccCtrlFilterServiceMask_Type = Integer32
_WfIpAccCtrlFilterServiceMask_Object = MibTableColumn
wfIpAccCtrlFilterServiceMask = _WfIpAccCtrlFilterServiceMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 8),
    _WfIpAccCtrlFilterServiceMask_Type()
)
wfIpAccCtrlFilterServiceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterServiceMask.setStatus("mandatory")


class _WfIpAccCtrlFilterDenyLog_Type(Integer32):
    """Custom type wfIpAccCtrlFilterDenyLog based on Integer32"""
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


_WfIpAccCtrlFilterDenyLog_Type.__name__ = "Integer32"
_WfIpAccCtrlFilterDenyLog_Object = MibTableColumn
wfIpAccCtrlFilterDenyLog = _WfIpAccCtrlFilterDenyLog_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 9),
    _WfIpAccCtrlFilterDenyLog_Type()
)
wfIpAccCtrlFilterDenyLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterDenyLog.setStatus("mandatory")
_WfIpAccCtrlFilterPrecedence_Type = Integer32
_WfIpAccCtrlFilterPrecedence_Object = MibTableColumn
wfIpAccCtrlFilterPrecedence = _WfIpAccCtrlFilterPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 10),
    _WfIpAccCtrlFilterPrecedence_Type()
)
wfIpAccCtrlFilterPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterPrecedence.setStatus("mandatory")
_WfIpAccCtrlFilterId_Type = Integer32
_WfIpAccCtrlFilterId_Object = MibTableColumn
wfIpAccCtrlFilterId = _WfIpAccCtrlFilterId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 19, 1, 11),
    _WfIpAccCtrlFilterId_Type()
)
wfIpAccCtrlFilterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlFilterId.setStatus("mandatory")
_WfIpAccCtrlNetworkTable_Object = MibTable
wfIpAccCtrlNetworkTable = _WfIpAccCtrlNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20)
)
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkTable.setStatus("mandatory")
_WfIpAccCtrlNetworkEntry_Object = MibTableRow
wfIpAccCtrlNetworkEntry = _WfIpAccCtrlNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20, 1)
)
wfIpAccCtrlNetworkEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpAccCtrlNetworkIndex"),
)
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkEntry.setStatus("mandatory")


class _WfIpAccCtrlNetworkCreate_Type(Integer32):
    """Custom type wfIpAccCtrlNetworkCreate based on Integer32"""
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


_WfIpAccCtrlNetworkCreate_Type.__name__ = "Integer32"
_WfIpAccCtrlNetworkCreate_Object = MibTableColumn
wfIpAccCtrlNetworkCreate = _WfIpAccCtrlNetworkCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20, 1, 1),
    _WfIpAccCtrlNetworkCreate_Type()
)
wfIpAccCtrlNetworkCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkCreate.setStatus("mandatory")


class _WfIpAccCtrlNetworkEnable_Type(Integer32):
    """Custom type wfIpAccCtrlNetworkEnable based on Integer32"""
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


_WfIpAccCtrlNetworkEnable_Type.__name__ = "Integer32"
_WfIpAccCtrlNetworkEnable_Object = MibTableColumn
wfIpAccCtrlNetworkEnable = _WfIpAccCtrlNetworkEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20, 1, 2),
    _WfIpAccCtrlNetworkEnable_Type()
)
wfIpAccCtrlNetworkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkEnable.setStatus("mandatory")
_WfIpAccCtrlNetworkIndex_Type = Integer32
_WfIpAccCtrlNetworkIndex_Object = MibTableColumn
wfIpAccCtrlNetworkIndex = _WfIpAccCtrlNetworkIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20, 1, 3),
    _WfIpAccCtrlNetworkIndex_Type()
)
wfIpAccCtrlNetworkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkIndex.setStatus("mandatory")
_WfIpAccCtrlNetworkNetwork_Type = IpAddress
_WfIpAccCtrlNetworkNetwork_Object = MibTableColumn
wfIpAccCtrlNetworkNetwork = _WfIpAccCtrlNetworkNetwork_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20, 1, 4),
    _WfIpAccCtrlNetworkNetwork_Type()
)
wfIpAccCtrlNetworkNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkNetwork.setStatus("mandatory")
_WfIpAccCtrlNetworkNetworkMask_Type = IpAddress
_WfIpAccCtrlNetworkNetworkMask_Object = MibTableColumn
wfIpAccCtrlNetworkNetworkMask = _WfIpAccCtrlNetworkNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20, 1, 5),
    _WfIpAccCtrlNetworkNetworkMask_Type()
)
wfIpAccCtrlNetworkNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkNetworkMask.setStatus("mandatory")
_WfIpAccCtrlNetworkId_Type = Integer32
_WfIpAccCtrlNetworkId_Object = MibTableColumn
wfIpAccCtrlNetworkId = _WfIpAccCtrlNetworkId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 20, 1, 6),
    _WfIpAccCtrlNetworkId_Type()
)
wfIpAccCtrlNetworkId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlNetworkId.setStatus("mandatory")
_WfIpAccCtrlUserHostTable_Object = MibTable
wfIpAccCtrlUserHostTable = _WfIpAccCtrlUserHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21)
)
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostTable.setStatus("mandatory")
_WfIpAccCtrlUserHostEntry_Object = MibTableRow
wfIpAccCtrlUserHostEntry = _WfIpAccCtrlUserHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21, 1)
)
wfIpAccCtrlUserHostEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpAccCtrlUserHostIndex"),
)
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostEntry.setStatus("mandatory")


class _WfIpAccCtrlUserHostCreate_Type(Integer32):
    """Custom type wfIpAccCtrlUserHostCreate based on Integer32"""
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


_WfIpAccCtrlUserHostCreate_Type.__name__ = "Integer32"
_WfIpAccCtrlUserHostCreate_Object = MibTableColumn
wfIpAccCtrlUserHostCreate = _WfIpAccCtrlUserHostCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21, 1, 1),
    _WfIpAccCtrlUserHostCreate_Type()
)
wfIpAccCtrlUserHostCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostCreate.setStatus("mandatory")


class _WfIpAccCtrlUserHostEnable_Type(Integer32):
    """Custom type wfIpAccCtrlUserHostEnable based on Integer32"""
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


_WfIpAccCtrlUserHostEnable_Type.__name__ = "Integer32"
_WfIpAccCtrlUserHostEnable_Object = MibTableColumn
wfIpAccCtrlUserHostEnable = _WfIpAccCtrlUserHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21, 1, 2),
    _WfIpAccCtrlUserHostEnable_Type()
)
wfIpAccCtrlUserHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostEnable.setStatus("mandatory")
_WfIpAccCtrlUserHostIndex_Type = Integer32
_WfIpAccCtrlUserHostIndex_Object = MibTableColumn
wfIpAccCtrlUserHostIndex = _WfIpAccCtrlUserHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21, 1, 3),
    _WfIpAccCtrlUserHostIndex_Type()
)
wfIpAccCtrlUserHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostIndex.setStatus("mandatory")
_WfIpAccCtrlUserHostUser_Type = DisplayString
_WfIpAccCtrlUserHostUser_Object = MibTableColumn
wfIpAccCtrlUserHostUser = _WfIpAccCtrlUserHostUser_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21, 1, 4),
    _WfIpAccCtrlUserHostUser_Type()
)
wfIpAccCtrlUserHostUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostUser.setStatus("mandatory")
_WfIpAccCtrlUserHostHost_Type = DisplayString
_WfIpAccCtrlUserHostHost_Object = MibTableColumn
wfIpAccCtrlUserHostHost = _WfIpAccCtrlUserHostHost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21, 1, 5),
    _WfIpAccCtrlUserHostHost_Type()
)
wfIpAccCtrlUserHostHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostHost.setStatus("mandatory")
_WfIpAccCtrlUserHostId_Type = Integer32
_WfIpAccCtrlUserHostId_Object = MibTableColumn
wfIpAccCtrlUserHostId = _WfIpAccCtrlUserHostId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 21, 1, 6),
    _WfIpAccCtrlUserHostId_Type()
)
wfIpAccCtrlUserHostId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpAccCtrlUserHostId.setStatus("mandatory")
_WfIpAddrTable_Object = MibTable
wfIpAddrTable = _WfIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 22)
)
if mibBuilder.loadTexts:
    wfIpAddrTable.setStatus("mandatory")
_WfIpAddrEntry_Object = MibTableRow
wfIpAddrEntry = _WfIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 22, 1)
)
wfIpAddrEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpAdEntAddr"),
)
if mibBuilder.loadTexts:
    wfIpAddrEntry.setStatus("mandatory")
_WfIpAdEntAddr_Type = IpAddress
_WfIpAdEntAddr_Object = MibTableColumn
wfIpAdEntAddr = _WfIpAdEntAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 22, 1, 1),
    _WfIpAdEntAddr_Type()
)
wfIpAdEntAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdEntAddr.setStatus("mandatory")
_WfIpAdEntIfIndex_Type = Integer32
_WfIpAdEntIfIndex_Object = MibTableColumn
wfIpAdEntIfIndex = _WfIpAdEntIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 22, 1, 2),
    _WfIpAdEntIfIndex_Type()
)
wfIpAdEntIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdEntIfIndex.setStatus("mandatory")
_WfIpAdEntNetMask_Type = IpAddress
_WfIpAdEntNetMask_Object = MibTableColumn
wfIpAdEntNetMask = _WfIpAdEntNetMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 22, 1, 3),
    _WfIpAdEntNetMask_Type()
)
wfIpAdEntNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdEntNetMask.setStatus("mandatory")
_WfIpAdEntBcastAddr_Type = Integer32
_WfIpAdEntBcastAddr_Object = MibTableColumn
wfIpAdEntBcastAddr = _WfIpAdEntBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 22, 1, 4),
    _WfIpAdEntBcastAddr_Type()
)
wfIpAdEntBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdEntBcastAddr.setStatus("mandatory")


class _WfIpAdEntReasmMaxSize_Type(Integer32):
    """Custom type wfIpAdEntReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIpAdEntReasmMaxSize_Type.__name__ = "Integer32"
_WfIpAdEntReasmMaxSize_Object = MibTableColumn
wfIpAdEntReasmMaxSize = _WfIpAdEntReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 22, 1, 5),
    _WfIpAdEntReasmMaxSize_Type()
)
wfIpAdEntReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpAdEntReasmMaxSize.setStatus("mandatory")
_WfIpInternalHostTable_Object = MibTable
wfIpInternalHostTable = _WfIpInternalHostTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23)
)
if mibBuilder.loadTexts:
    wfIpInternalHostTable.setStatus("mandatory")
_WfIpInternalHostEntry_Object = MibTableRow
wfIpInternalHostEntry = _WfIpInternalHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1)
)
wfIpInternalHostEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpInternHtIpAddress"),
)
if mibBuilder.loadTexts:
    wfIpInternalHostEntry.setStatus("mandatory")
_WfIpInternHtIpAddress_Type = IpAddress
_WfIpInternHtIpAddress_Object = MibTableColumn
wfIpInternHtIpAddress = _WfIpInternHtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 1),
    _WfIpInternHtIpAddress_Type()
)
wfIpInternHtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtIpAddress.setStatus("mandatory")
_WfIpInternHtReceives_Type = Counter32
_WfIpInternHtReceives_Object = MibTableColumn
wfIpInternHtReceives = _WfIpInternHtReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 2),
    _WfIpInternHtReceives_Type()
)
wfIpInternHtReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtReceives.setStatus("mandatory")
_WfIpInternHtInDelivers_Type = Counter32
_WfIpInternHtInDelivers_Object = MibTableColumn
wfIpInternHtInDelivers = _WfIpInternHtInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 3),
    _WfIpInternHtInDelivers_Type()
)
wfIpInternHtInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtInDelivers.setStatus("mandatory")
_WfIpInternHtUnknownProtos_Type = Counter32
_WfIpInternHtUnknownProtos_Object = MibTableColumn
wfIpInternHtUnknownProtos = _WfIpInternHtUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 4),
    _WfIpInternHtUnknownProtos_Type()
)
wfIpInternHtUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtUnknownProtos.setStatus("mandatory")
_WfIpInternHtReasmReqds_Type = Counter32
_WfIpInternHtReasmReqds_Object = MibTableColumn
wfIpInternHtReasmReqds = _WfIpInternHtReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 5),
    _WfIpInternHtReasmReqds_Type()
)
wfIpInternHtReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtReasmReqds.setStatus("mandatory")
_WfIpInternHtReasmFails_Type = Counter32
_WfIpInternHtReasmFails_Object = MibTableColumn
wfIpInternHtReasmFails = _WfIpInternHtReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 6),
    _WfIpInternHtReasmFails_Type()
)
wfIpInternHtReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtReasmFails.setStatus("mandatory")
_WfIpInternHtReasmOKs_Type = Counter32
_WfIpInternHtReasmOKs_Object = MibTableColumn
wfIpInternHtReasmOKs = _WfIpInternHtReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 7),
    _WfIpInternHtReasmOKs_Type()
)
wfIpInternHtReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtReasmOKs.setStatus("mandatory")
_WfIpInternHtInHdrErrors_Type = Counter32
_WfIpInternHtInHdrErrors_Object = MibTableColumn
wfIpInternHtInHdrErrors = _WfIpInternHtInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 23, 1, 8),
    _WfIpInternHtInHdrErrors_Type()
)
wfIpInternHtInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpInternHtInHdrErrors.setStatus("mandatory")
_WfIpIntfCfgTable_Object = MibTable
wfIpIntfCfgTable = _WfIpIntfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24)
)
if mibBuilder.loadTexts:
    wfIpIntfCfgTable.setStatus("mandatory")
_WfIpIntfCfgEntry_Object = MibTableRow
wfIpIntfCfgEntry = _WfIpIntfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1)
)
wfIpIntfCfgEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpIntfCfgAddr"),
    (0, "Wellfleet-IP-MIB", "wfIpIntfCfgCircuit"),
)
if mibBuilder.loadTexts:
    wfIpIntfCfgEntry.setStatus("mandatory")


class _WfIpIntfCfgCreate_Type(Integer32):
    """Custom type wfIpIntfCfgCreate based on Integer32"""
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


_WfIpIntfCfgCreate_Type.__name__ = "Integer32"
_WfIpIntfCfgCreate_Object = MibTableColumn
wfIpIntfCfgCreate = _WfIpIntfCfgCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 1),
    _WfIpIntfCfgCreate_Type()
)
wfIpIntfCfgCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgCreate.setStatus("mandatory")


class _WfIpIntfCfgEnable_Type(Integer32):
    """Custom type wfIpIntfCfgEnable based on Integer32"""
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


_WfIpIntfCfgEnable_Type.__name__ = "Integer32"
_WfIpIntfCfgEnable_Object = MibTableColumn
wfIpIntfCfgEnable = _WfIpIntfCfgEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 2),
    _WfIpIntfCfgEnable_Type()
)
wfIpIntfCfgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgEnable.setStatus("mandatory")


class _WfIpIntfCfgState_Type(Integer32):
    """Custom type wfIpIntfCfgState based on Integer32"""
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


_WfIpIntfCfgState_Type.__name__ = "Integer32"
_WfIpIntfCfgState_Object = MibTableColumn
wfIpIntfCfgState = _WfIpIntfCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 3),
    _WfIpIntfCfgState_Type()
)
wfIpIntfCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfCfgState.setStatus("mandatory")
_WfIpIntfCfgAddr_Type = IpAddress
_WfIpIntfCfgAddr_Object = MibTableColumn
wfIpIntfCfgAddr = _WfIpIntfCfgAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 4),
    _WfIpIntfCfgAddr_Type()
)
wfIpIntfCfgAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfCfgAddr.setStatus("mandatory")
_WfIpIntfCfgCircuit_Type = Integer32
_WfIpIntfCfgCircuit_Object = MibTableColumn
wfIpIntfCfgCircuit = _WfIpIntfCfgCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 5),
    _WfIpIntfCfgCircuit_Type()
)
wfIpIntfCfgCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfCfgCircuit.setStatus("mandatory")
_WfIpIntfCfgMask_Type = IpAddress
_WfIpIntfCfgMask_Object = MibTableColumn
wfIpIntfCfgMask = _WfIpIntfCfgMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 6),
    _WfIpIntfCfgMask_Type()
)
wfIpIntfCfgMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMask.setStatus("mandatory")


class _WfIpIntfCfgCost_Type(Integer32):
    """Custom type wfIpIntfCfgCost based on Integer32"""
    defaultValue = 1


_WfIpIntfCfgCost_Object = MibTableColumn
wfIpIntfCfgCost = _WfIpIntfCfgCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 7),
    _WfIpIntfCfgCost_Type()
)
wfIpIntfCfgCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgCost.setStatus("mandatory")
_WfIpIntfCfgCfgBcastAddr_Type = IpAddress
_WfIpIntfCfgCfgBcastAddr_Object = MibTableColumn
wfIpIntfCfgCfgBcastAddr = _WfIpIntfCfgCfgBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 8),
    _WfIpIntfCfgCfgBcastAddr_Type()
)
wfIpIntfCfgCfgBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgCfgBcastAddr.setStatus("mandatory")
_WfIpIntfCfgBcastAddr_Type = IpAddress
_WfIpIntfCfgBcastAddr_Object = MibTableColumn
wfIpIntfCfgBcastAddr = _WfIpIntfCfgBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 9),
    _WfIpIntfCfgBcastAddr_Type()
)
wfIpIntfCfgBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfCfgBcastAddr.setStatus("mandatory")
_WfIpIntfCfgCfgMacAddress_Type = OctetString
_WfIpIntfCfgCfgMacAddress_Object = MibTableColumn
wfIpIntfCfgCfgMacAddress = _WfIpIntfCfgCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 10),
    _WfIpIntfCfgCfgMacAddress_Type()
)
wfIpIntfCfgCfgMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgCfgMacAddress.setStatus("mandatory")
_WfIpIntfCfgMacAddress_Type = OctetString
_WfIpIntfCfgMacAddress_Object = MibTableColumn
wfIpIntfCfgMacAddress = _WfIpIntfCfgMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 11),
    _WfIpIntfCfgMacAddress_Type()
)
wfIpIntfCfgMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfCfgMacAddress.setStatus("mandatory")


class _WfIpIntfCfgMTUDiscovery_Type(Integer32):
    """Custom type wfIpIntfCfgMTUDiscovery based on Integer32"""
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


_WfIpIntfCfgMTUDiscovery_Type.__name__ = "Integer32"
_WfIpIntfCfgMTUDiscovery_Object = MibTableColumn
wfIpIntfCfgMTUDiscovery = _WfIpIntfCfgMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 12),
    _WfIpIntfCfgMTUDiscovery_Type()
)
wfIpIntfCfgMTUDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMTUDiscovery.setStatus("mandatory")


class _WfIpIntfCfgAMR_Type(Integer32):
    """Custom type wfIpIntfCfgAMR based on Integer32"""
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


_WfIpIntfCfgAMR_Type.__name__ = "Integer32"
_WfIpIntfCfgAMR_Object = MibTableColumn
wfIpIntfCfgAMR = _WfIpIntfCfgAMR_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 13),
    _WfIpIntfCfgAMR_Type()
)
wfIpIntfCfgAMR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAMR.setStatus("mandatory")


class _WfIpIntfCfgASB_Type(Integer32):
    """Custom type wfIpIntfCfgASB based on Integer32"""
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


_WfIpIntfCfgASB_Type.__name__ = "Integer32"
_WfIpIntfCfgASB_Object = MibTableColumn
wfIpIntfCfgASB = _WfIpIntfCfgASB_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 14),
    _WfIpIntfCfgASB_Type()
)
wfIpIntfCfgASB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgASB.setStatus("mandatory")


class _WfIpIntfCfgAddressResolutionType_Type(Integer32):
    """Custom type wfIpIntfCfgAddressResolutionType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("arp-in-arp", 6),
          ("arp-probe", 10),
          ("atm-arp", 11),
          ("bfe-ddn", 8),
          ("ddn", 3),
          ("in-arp", 5),
          ("none", 7),
          ("pdn", 4),
          ("probe", 9))
    )


_WfIpIntfCfgAddressResolutionType_Type.__name__ = "Integer32"
_WfIpIntfCfgAddressResolutionType_Object = MibTableColumn
wfIpIntfCfgAddressResolutionType = _WfIpIntfCfgAddressResolutionType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 15),
    _WfIpIntfCfgAddressResolutionType_Type()
)
wfIpIntfCfgAddressResolutionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAddressResolutionType.setStatus("mandatory")


class _WfIpIntfCfgProxy_Type(Integer32):
    """Custom type wfIpIntfCfgProxy based on Integer32"""
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


_WfIpIntfCfgProxy_Type.__name__ = "Integer32"
_WfIpIntfCfgProxy_Object = MibTableColumn
wfIpIntfCfgProxy = _WfIpIntfCfgProxy_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 16),
    _WfIpIntfCfgProxy_Type()
)
wfIpIntfCfgProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgProxy.setStatus("mandatory")


class _WfIpIntfCfgHostCache_Type(Integer32):
    """Custom type wfIpIntfCfgHostCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              120,
              180,
              240,
              300,
              600,
              900,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("cache-120", 120),
          ("cache-1200", 1200),
          ("cache-180", 180),
          ("cache-240", 240),
          ("cache-300", 300),
          ("cache-600", 600),
          ("cache-900", 900),
          ("cache-off", 1))
    )


_WfIpIntfCfgHostCache_Type.__name__ = "Integer32"
_WfIpIntfCfgHostCache_Object = MibTableColumn
wfIpIntfCfgHostCache = _WfIpIntfCfgHostCache_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 17),
    _WfIpIntfCfgHostCache_Type()
)
wfIpIntfCfgHostCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgHostCache.setStatus("mandatory")


class _WfIpIntfCfgUdpXsumOn_Type(Integer32):
    """Custom type wfIpIntfCfgUdpXsumOn based on Integer32"""
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


_WfIpIntfCfgUdpXsumOn_Type.__name__ = "Integer32"
_WfIpIntfCfgUdpXsumOn_Object = MibTableColumn
wfIpIntfCfgUdpXsumOn = _WfIpIntfCfgUdpXsumOn_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 18),
    _WfIpIntfCfgUdpXsumOn_Type()
)
wfIpIntfCfgUdpXsumOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgUdpXsumOn.setStatus("mandatory")


class _WfIpIntfCfgTrEndStation_Type(Integer32):
    """Custom type wfIpIntfCfgTrEndStation based on Integer32"""
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


_WfIpIntfCfgTrEndStation_Type.__name__ = "Integer32"
_WfIpIntfCfgTrEndStation_Object = MibTableColumn
wfIpIntfCfgTrEndStation = _WfIpIntfCfgTrEndStation_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 19),
    _WfIpIntfCfgTrEndStation_Type()
)
wfIpIntfCfgTrEndStation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgTrEndStation.setStatus("mandatory")
_WfIpIntfCfgSMDSGroupAddress_Type = OctetString
_WfIpIntfCfgSMDSGroupAddress_Object = MibTableColumn
wfIpIntfCfgSMDSGroupAddress = _WfIpIntfCfgSMDSGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 20),
    _WfIpIntfCfgSMDSGroupAddress_Type()
)
wfIpIntfCfgSMDSGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgSMDSGroupAddress.setStatus("mandatory")
_WfIpIntfCfgSMDSArpReqAddress_Type = OctetString
_WfIpIntfCfgSMDSArpReqAddress_Object = MibTableColumn
wfIpIntfCfgSMDSArpReqAddress = _WfIpIntfCfgSMDSArpReqAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 21),
    _WfIpIntfCfgSMDSArpReqAddress_Type()
)
wfIpIntfCfgSMDSArpReqAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgSMDSArpReqAddress.setStatus("mandatory")
_WfIpIntfCfgFRBcastDlci_Type = Integer32
_WfIpIntfCfgFRBcastDlci_Object = MibTableColumn
wfIpIntfCfgFRBcastDlci = _WfIpIntfCfgFRBcastDlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 22),
    _WfIpIntfCfgFRBcastDlci_Type()
)
wfIpIntfCfgFRBcastDlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgFRBcastDlci.setStatus("mandatory")
_WfIpIntfCfgFRMcast1Dlci_Type = Integer32
_WfIpIntfCfgFRMcast1Dlci_Object = MibTableColumn
wfIpIntfCfgFRMcast1Dlci = _WfIpIntfCfgFRMcast1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 23),
    _WfIpIntfCfgFRMcast1Dlci_Type()
)
wfIpIntfCfgFRMcast1Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgFRMcast1Dlci.setStatus("mandatory")
_WfIpIntfCfgFRMcast2Dlci_Type = Integer32
_WfIpIntfCfgFRMcast2Dlci_Object = MibTableColumn
wfIpIntfCfgFRMcast2Dlci = _WfIpIntfCfgFRMcast2Dlci_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 24),
    _WfIpIntfCfgFRMcast2Dlci_Type()
)
wfIpIntfCfgFRMcast2Dlci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgFRMcast2Dlci.setStatus("mandatory")


class _WfIpIntfCfgRedirect_Type(Integer32):
    """Custom type wfIpIntfCfgRedirect based on Integer32"""
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


_WfIpIntfCfgRedirect_Type.__name__ = "Integer32"
_WfIpIntfCfgRedirect_Object = MibTableColumn
wfIpIntfCfgRedirect = _WfIpIntfCfgRedirect_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 25),
    _WfIpIntfCfgRedirect_Type()
)
wfIpIntfCfgRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgRedirect.setStatus("mandatory")


class _WfIpIntfCfgEnetArpEncaps_Type(Integer32):
    """Custom type wfIpIntfCfgEnetArpEncaps based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("arpbothprobelsap", 9),
          ("arpenetprobelsap", 7),
          ("arpsnapprobelsap", 8),
          ("both", 3),
          ("enet", 1),
          ("probeboth", 6),
          ("probeenet", 5),
          ("probelsap", 4),
          ("snap", 2))
    )


_WfIpIntfCfgEnetArpEncaps_Type.__name__ = "Integer32"
_WfIpIntfCfgEnetArpEncaps_Object = MibTableColumn
wfIpIntfCfgEnetArpEncaps = _WfIpIntfCfgEnetArpEncaps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 26),
    _WfIpIntfCfgEnetArpEncaps_Type()
)
wfIpIntfCfgEnetArpEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgEnetArpEncaps.setStatus("mandatory")


class _WfIpIntfCfgSlotMask_Type(Gauge32):
    """Custom type wfIpIntfCfgSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfIpIntfCfgSlotMask_Object = MibTableColumn
wfIpIntfCfgSlotMask = _WfIpIntfCfgSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 27),
    _WfIpIntfCfgSlotMask_Type()
)
wfIpIntfCfgSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgSlotMask.setStatus("mandatory")


class _WfIpIntfCfgEnableSecurity_Type(Integer32):
    """Custom type wfIpIntfCfgEnableSecurity based on Integer32"""
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


_WfIpIntfCfgEnableSecurity_Type.__name__ = "Integer32"
_WfIpIntfCfgEnableSecurity_Object = MibTableColumn
wfIpIntfCfgEnableSecurity = _WfIpIntfCfgEnableSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 28),
    _WfIpIntfCfgEnableSecurity_Type()
)
wfIpIntfCfgEnableSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgEnableSecurity.setStatus("mandatory")


class _WfIpIntfCfgStripSecurity_Type(Integer32):
    """Custom type wfIpIntfCfgStripSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("incoming", 1),
          ("outgoing", 2))
    )


_WfIpIntfCfgStripSecurity_Type.__name__ = "Integer32"
_WfIpIntfCfgStripSecurity_Object = MibTableColumn
wfIpIntfCfgStripSecurity = _WfIpIntfCfgStripSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 29),
    _WfIpIntfCfgStripSecurity_Type()
)
wfIpIntfCfgStripSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgStripSecurity.setStatus("mandatory")


class _WfIpIntfCfgRequireOutSecurity_Type(Integer32):
    """Custom type wfIpIntfCfgRequireOutSecurity based on Integer32"""
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
        *(("all", 3),
          ("forwarded", 1),
          ("originated", 2))
    )


_WfIpIntfCfgRequireOutSecurity_Type.__name__ = "Integer32"
_WfIpIntfCfgRequireOutSecurity_Object = MibTableColumn
wfIpIntfCfgRequireOutSecurity = _WfIpIntfCfgRequireOutSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 30),
    _WfIpIntfCfgRequireOutSecurity_Type()
)
wfIpIntfCfgRequireOutSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgRequireOutSecurity.setStatus("mandatory")


class _WfIpIntfCfgRequireInSecurity_Type(Integer32):
    """Custom type wfIpIntfCfgRequireInSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("yes", 1)
    )


_WfIpIntfCfgRequireInSecurity_Type.__name__ = "Integer32"
_WfIpIntfCfgRequireInSecurity_Object = MibTableColumn
wfIpIntfCfgRequireInSecurity = _WfIpIntfCfgRequireInSecurity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 31),
    _WfIpIntfCfgRequireInSecurity_Type()
)
wfIpIntfCfgRequireInSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgRequireInSecurity.setStatus("mandatory")


class _WfIpIntfCfgMinLevel_Type(Integer32):
    """Custom type wfIpIntfCfgMinLevel based on Integer32"""
    defaultValue = 171

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpIntfCfgMinLevel_Type.__name__ = "Integer32"
_WfIpIntfCfgMinLevel_Object = MibTableColumn
wfIpIntfCfgMinLevel = _WfIpIntfCfgMinLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 32),
    _WfIpIntfCfgMinLevel_Type()
)
wfIpIntfCfgMinLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMinLevel.setStatus("mandatory")


class _WfIpIntfCfgMaxLevel_Type(Integer32):
    """Custom type wfIpIntfCfgMaxLevel based on Integer32"""
    defaultValue = 61

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpIntfCfgMaxLevel_Type.__name__ = "Integer32"
_WfIpIntfCfgMaxLevel_Object = MibTableColumn
wfIpIntfCfgMaxLevel = _WfIpIntfCfgMaxLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 33),
    _WfIpIntfCfgMaxLevel_Type()
)
wfIpIntfCfgMaxLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMaxLevel.setStatus("mandatory")
_WfIpIntfCfgMustOutAuthority_Type = OctetString
_WfIpIntfCfgMustOutAuthority_Object = MibTableColumn
wfIpIntfCfgMustOutAuthority = _WfIpIntfCfgMustOutAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 34),
    _WfIpIntfCfgMustOutAuthority_Type()
)
wfIpIntfCfgMustOutAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMustOutAuthority.setStatus("mandatory")
_WfIpIntfCfgMayOutAuthority_Type = OctetString
_WfIpIntfCfgMayOutAuthority_Object = MibTableColumn
wfIpIntfCfgMayOutAuthority = _WfIpIntfCfgMayOutAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 35),
    _WfIpIntfCfgMayOutAuthority_Type()
)
wfIpIntfCfgMayOutAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMayOutAuthority.setStatus("mandatory")
_WfIpIntfCfgMustInAuthority_Type = OctetString
_WfIpIntfCfgMustInAuthority_Object = MibTableColumn
wfIpIntfCfgMustInAuthority = _WfIpIntfCfgMustInAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 36),
    _WfIpIntfCfgMustInAuthority_Type()
)
wfIpIntfCfgMustInAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMustInAuthority.setStatus("mandatory")
_WfIpIntfCfgMayInAuthority_Type = OctetString
_WfIpIntfCfgMayInAuthority_Object = MibTableColumn
wfIpIntfCfgMayInAuthority = _WfIpIntfCfgMayInAuthority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 37),
    _WfIpIntfCfgMayInAuthority_Type()
)
wfIpIntfCfgMayInAuthority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMayInAuthority.setStatus("mandatory")


class _WfIpIntfCfgImplicitLabelEnabled_Type(Integer32):
    """Custom type wfIpIntfCfgImplicitLabelEnabled based on Integer32"""
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


_WfIpIntfCfgImplicitLabelEnabled_Type.__name__ = "Integer32"
_WfIpIntfCfgImplicitLabelEnabled_Object = MibTableColumn
wfIpIntfCfgImplicitLabelEnabled = _WfIpIntfCfgImplicitLabelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 38),
    _WfIpIntfCfgImplicitLabelEnabled_Type()
)
wfIpIntfCfgImplicitLabelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgImplicitLabelEnabled.setStatus("mandatory")
_WfIpIntfCfgImplicitAuth_Type = OctetString
_WfIpIntfCfgImplicitAuth_Object = MibTableColumn
wfIpIntfCfgImplicitAuth = _WfIpIntfCfgImplicitAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 39),
    _WfIpIntfCfgImplicitAuth_Type()
)
wfIpIntfCfgImplicitAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgImplicitAuth.setStatus("mandatory")


class _WfIpIntfCfgImplicitLevel_Type(Integer32):
    """Custom type wfIpIntfCfgImplicitLevel based on Integer32"""
    defaultValue = 171

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpIntfCfgImplicitLevel_Type.__name__ = "Integer32"
_WfIpIntfCfgImplicitLevel_Object = MibTableColumn
wfIpIntfCfgImplicitLevel = _WfIpIntfCfgImplicitLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 40),
    _WfIpIntfCfgImplicitLevel_Type()
)
wfIpIntfCfgImplicitLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgImplicitLevel.setStatus("mandatory")


class _WfIpIntfCfgDefaultLabelEnabled_Type(Integer32):
    """Custom type wfIpIntfCfgDefaultLabelEnabled based on Integer32"""
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


_WfIpIntfCfgDefaultLabelEnabled_Type.__name__ = "Integer32"
_WfIpIntfCfgDefaultLabelEnabled_Object = MibTableColumn
wfIpIntfCfgDefaultLabelEnabled = _WfIpIntfCfgDefaultLabelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 41),
    _WfIpIntfCfgDefaultLabelEnabled_Type()
)
wfIpIntfCfgDefaultLabelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgDefaultLabelEnabled.setStatus("mandatory")
_WfIpIntfCfgDefaultAuth_Type = OctetString
_WfIpIntfCfgDefaultAuth_Object = MibTableColumn
wfIpIntfCfgDefaultAuth = _WfIpIntfCfgDefaultAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 42),
    _WfIpIntfCfgDefaultAuth_Type()
)
wfIpIntfCfgDefaultAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgDefaultAuth.setStatus("mandatory")


class _WfIpIntfCfgDefaultLevel_Type(Integer32):
    """Custom type wfIpIntfCfgDefaultLevel based on Integer32"""
    defaultValue = 171

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(61,
              90,
              150,
              171)
        )
    )
    namedValues = NamedValues(
        *(("confidential", 150),
          ("secret", 90),
          ("topsecret", 61),
          ("unclassified", 171))
    )


_WfIpIntfCfgDefaultLevel_Type.__name__ = "Integer32"
_WfIpIntfCfgDefaultLevel_Object = MibTableColumn
wfIpIntfCfgDefaultLevel = _WfIpIntfCfgDefaultLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 43),
    _WfIpIntfCfgDefaultLevel_Type()
)
wfIpIntfCfgDefaultLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgDefaultLevel.setStatus("mandatory")


class _WfIpIntfCfgErrorLabelEnabled_Type(Integer32):
    """Custom type wfIpIntfCfgErrorLabelEnabled based on Integer32"""
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


_WfIpIntfCfgErrorLabelEnabled_Type.__name__ = "Integer32"
_WfIpIntfCfgErrorLabelEnabled_Object = MibTableColumn
wfIpIntfCfgErrorLabelEnabled = _WfIpIntfCfgErrorLabelEnabled_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 44),
    _WfIpIntfCfgErrorLabelEnabled_Type()
)
wfIpIntfCfgErrorLabelEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgErrorLabelEnabled.setStatus("mandatory")
_WfIpIntfCfgErrorAuth_Type = OctetString
_WfIpIntfCfgErrorAuth_Object = MibTableColumn
wfIpIntfCfgErrorAuth = _WfIpIntfCfgErrorAuth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 45),
    _WfIpIntfCfgErrorAuth_Type()
)
wfIpIntfCfgErrorAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgErrorAuth.setStatus("mandatory")


class _WfIpIntfCfgFwdCacheSize_Type(Integer32):
    """Custom type wfIpIntfCfgFwdCacheSize based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 2147483647),
    )


_WfIpIntfCfgFwdCacheSize_Type.__name__ = "Integer32"
_WfIpIntfCfgFwdCacheSize_Object = MibTableColumn
wfIpIntfCfgFwdCacheSize = _WfIpIntfCfgFwdCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 46),
    _WfIpIntfCfgFwdCacheSize_Type()
)
wfIpIntfCfgFwdCacheSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgFwdCacheSize.setStatus("mandatory")
_WfIpIntfCfgUnnumAsocAddr_Type = IpAddress
_WfIpIntfCfgUnnumAsocAddr_Object = MibTableColumn
wfIpIntfCfgUnnumAsocAddr = _WfIpIntfCfgUnnumAsocAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 47),
    _WfIpIntfCfgUnnumAsocAddr_Type()
)
wfIpIntfCfgUnnumAsocAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgUnnumAsocAddr.setStatus("mandatory")


class _WfIpIntfCfgUnnumAsocAlt_Type(Integer32):
    """Custom type wfIpIntfCfgUnnumAsocAlt based on Integer32"""
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


_WfIpIntfCfgUnnumAsocAlt_Type.__name__ = "Integer32"
_WfIpIntfCfgUnnumAsocAlt_Object = MibTableColumn
wfIpIntfCfgUnnumAsocAlt = _WfIpIntfCfgUnnumAsocAlt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 48),
    _WfIpIntfCfgUnnumAsocAlt_Type()
)
wfIpIntfCfgUnnumAsocAlt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgUnnumAsocAlt.setStatus("mandatory")


class _WfIpIntfCfgAtmArpMode_Type(Integer32):
    """Custom type wfIpIntfCfgAtmArpMode based on Integer32"""
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
        *(("client", 1),
          ("none", 3),
          ("server", 2))
    )


_WfIpIntfCfgAtmArpMode_Type.__name__ = "Integer32"
_WfIpIntfCfgAtmArpMode_Object = MibTableColumn
wfIpIntfCfgAtmArpMode = _WfIpIntfCfgAtmArpMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 49),
    _WfIpIntfCfgAtmArpMode_Type()
)
wfIpIntfCfgAtmArpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAtmArpMode.setStatus("mandatory")
_WfIpIntfCfgAtmArpSrvAddress_Type = OctetString
_WfIpIntfCfgAtmArpSrvAddress_Object = MibTableColumn
wfIpIntfCfgAtmArpSrvAddress = _WfIpIntfCfgAtmArpSrvAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 50),
    _WfIpIntfCfgAtmArpSrvAddress_Type()
)
wfIpIntfCfgAtmArpSrvAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAtmArpSrvAddress.setStatus("mandatory")


class _WfIpIntfCfgAtmArpSrvVcAgingEnable_Type(Integer32):
    """Custom type wfIpIntfCfgAtmArpSrvVcAgingEnable based on Integer32"""
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


_WfIpIntfCfgAtmArpSrvVcAgingEnable_Type.__name__ = "Integer32"
_WfIpIntfCfgAtmArpSrvVcAgingEnable_Object = MibTableColumn
wfIpIntfCfgAtmArpSrvVcAgingEnable = _WfIpIntfCfgAtmArpSrvVcAgingEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 51),
    _WfIpIntfCfgAtmArpSrvVcAgingEnable_Type()
)
wfIpIntfCfgAtmArpSrvVcAgingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAtmArpSrvVcAgingEnable.setStatus("mandatory")


class _WfIpIntfCfgAtmArpSrvRegInterval_Type(Integer32):
    """Custom type wfIpIntfCfgAtmArpSrvRegInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(900,
              1200)
        )
    )
    namedValues = NamedValues(
        *(("client-default", 900),
          ("server-default", 1200))
    )


_WfIpIntfCfgAtmArpSrvRegInterval_Type.__name__ = "Integer32"
_WfIpIntfCfgAtmArpSrvRegInterval_Object = MibTableColumn
wfIpIntfCfgAtmArpSrvRegInterval = _WfIpIntfCfgAtmArpSrvRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 52),
    _WfIpIntfCfgAtmArpSrvRegInterval_Type()
)
wfIpIntfCfgAtmArpSrvRegInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAtmArpSrvRegInterval.setStatus("mandatory")
_WfIpIntfCfgAtmArpMisc_Type = Integer32
_WfIpIntfCfgAtmArpMisc_Object = MibTableColumn
wfIpIntfCfgAtmArpMisc = _WfIpIntfCfgAtmArpMisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 53),
    _WfIpIntfCfgAtmArpMisc_Type()
)
wfIpIntfCfgAtmArpMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAtmArpMisc.setStatus("mandatory")
_WfIpIntfCfgAtmArpMisc2_Type = Integer32
_WfIpIntfCfgAtmArpMisc2_Object = MibTableColumn
wfIpIntfCfgAtmArpMisc2 = _WfIpIntfCfgAtmArpMisc2_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 54),
    _WfIpIntfCfgAtmArpMisc2_Type()
)
wfIpIntfCfgAtmArpMisc2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgAtmArpMisc2.setStatus("mandatory")


class _WfIpIntfCfgAtmArpSrvConnState_Type(Integer32):
    """Custom type wfIpIntfCfgAtmArpSrvConnState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              12,
              20,
              28,
              36,
              44,
              52,
              60,
              260,
              268,
              276,
              284,
              292,
              300,
              308,
              316,
              516,
              524,
              532,
              540,
              548,
              556,
              564,
              572,
              772,
              780,
              788,
              796,
              804,
              812,
              820,
              828,
              1028)
        )
    )
    namedValues = NamedValues(
        *(("closednotreg", 4),
          ("closednotregarp", 12),
          ("closedreg", 516),
          ("closedregarp", 524),
          ("closedregfail", 772),
          ("closedregfailarp", 780),
          ("closedregingarpxxx", 268),
          ("closedregingxxx", 260),
          ("init", 1),
          ("noservercfg", 1028),
          ("openfailnotreg", 52),
          ("openfailnotregarp", 60),
          ("openfailreg", 564),
          ("openfailregarp", 572),
          ("openfailregfail", 820),
          ("openfailregfailarp", 828),
          ("openfailregingarpxxx", 316),
          ("openfailregingxxx", 308),
          ("openingnotreg", 20),
          ("openingnotregarp", 28),
          ("openingreg", 532),
          ("openingregarp", 540),
          ("openingregfail", 788),
          ("openingregfailarp", 796),
          ("openingregingarpxxx", 284),
          ("openingregingxxx", 276),
          ("opennotregarpxxx", 44),
          ("opennotregxxx", 36),
          ("openreg", 548),
          ("openregarpxxx", 556),
          ("openregfailarpxxx", 812),
          ("openregfailxxx", 804),
          ("openreging", 292),
          ("openregingarp", 300),
          ("wereserver", 2))
    )


_WfIpIntfCfgAtmArpSrvConnState_Type.__name__ = "Integer32"
_WfIpIntfCfgAtmArpSrvConnState_Object = MibTableColumn
wfIpIntfCfgAtmArpSrvConnState = _WfIpIntfCfgAtmArpSrvConnState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 55),
    _WfIpIntfCfgAtmArpSrvConnState_Type()
)
wfIpIntfCfgAtmArpSrvConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfCfgAtmArpSrvConnState.setStatus("mandatory")


class _WfIpIntfCfgTrEsArpType_Type(Integer32):
    """Custom type wfIpIntfCfgTrEsArpType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("are", 2),
          ("ste", 1))
    )


_WfIpIntfCfgTrEsArpType_Type.__name__ = "Integer32"
_WfIpIntfCfgTrEsArpType_Object = MibTableColumn
wfIpIntfCfgTrEsArpType = _WfIpIntfCfgTrEsArpType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 56),
    _WfIpIntfCfgTrEsArpType_Type()
)
wfIpIntfCfgTrEsArpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgTrEsArpType.setStatus("mandatory")


class _WfIpIntfCfgMprMode_Type(Integer32):
    """Custom type wfIpIntfCfgMprMode based on Integer32"""
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
        *(("none", 1),
          ("replicate", 3),
          ("translate", 2))
    )


_WfIpIntfCfgMprMode_Type.__name__ = "Integer32"
_WfIpIntfCfgMprMode_Object = MibTableColumn
wfIpIntfCfgMprMode = _WfIpIntfCfgMprMode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 57),
    _WfIpIntfCfgMprMode_Type()
)
wfIpIntfCfgMprMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMprMode.setStatus("mandatory")


class _WfIpIntfCfgMprState_Type(Integer32):
    """Custom type wfIpIntfCfgMprState based on Integer32"""
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


_WfIpIntfCfgMprState_Type.__name__ = "Integer32"
_WfIpIntfCfgMprState_Object = MibTableColumn
wfIpIntfCfgMprState = _WfIpIntfCfgMprState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 58),
    _WfIpIntfCfgMprState_Type()
)
wfIpIntfCfgMprState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfCfgMprState.setStatus("mandatory")


class _WfIpIntfCfgIPSecEnable_Type(Integer32):
    """Custom type wfIpIntfCfgIPSecEnable based on Integer32"""
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


_WfIpIntfCfgIPSecEnable_Type.__name__ = "Integer32"
_WfIpIntfCfgIPSecEnable_Object = MibTableColumn
wfIpIntfCfgIPSecEnable = _WfIpIntfCfgIPSecEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 59),
    _WfIpIntfCfgIPSecEnable_Type()
)
wfIpIntfCfgIPSecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgIPSecEnable.setStatus("mandatory")


class _WfIpIntfCfgIPSecLogLevel_Type(Integer32):
    """Custom type wfIpIntfCfgIPSecLogLevel based on Integer32"""
    defaultValue = 0


_WfIpIntfCfgIPSecLogLevel_Object = MibTableColumn
wfIpIntfCfgIPSecLogLevel = _WfIpIntfCfgIPSecLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 60),
    _WfIpIntfCfgIPSecLogLevel_Type()
)
wfIpIntfCfgIPSecLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgIPSecLogLevel.setStatus("mandatory")


class _WfIpIntfCfgTosTemplate_Type(Integer32):
    """Custom type wfIpIntfCfgTosTemplate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rfc791-precedence", 2))
    )


_WfIpIntfCfgTosTemplate_Type.__name__ = "Integer32"
_WfIpIntfCfgTosTemplate_Object = MibTableColumn
wfIpIntfCfgTosTemplate = _WfIpIntfCfgTosTemplate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 61),
    _WfIpIntfCfgTosTemplate_Type()
)
wfIpIntfCfgTosTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgTosTemplate.setStatus("obsolete")


class _WfIpIntfCfgMsgLevel_Type(Integer32):
    """Custom type wfIpIntfCfgMsgLevel based on Integer32"""
    defaultValue = 917504

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65536,
              131072,
              262144,
              524288,
              917504,
              1048576,
              2031616)
        )
    )
    namedValues = NamedValues(
        *(("all", 2031616),
          ("debug", 65536),
          ("fault", 524288),
          ("info", 131072),
          ("infofaultwarning", 917504),
          ("trace", 1048576),
          ("warning", 262144))
    )


_WfIpIntfCfgMsgLevel_Type.__name__ = "Integer32"
_WfIpIntfCfgMsgLevel_Object = MibTableColumn
wfIpIntfCfgMsgLevel = _WfIpIntfCfgMsgLevel_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 62),
    _WfIpIntfCfgMsgLevel_Type()
)
wfIpIntfCfgMsgLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMsgLevel.setStatus("mandatory")


class _WfIpIntfCfgMtu_Type(Integer32):
    """Custom type wfIpIntfCfgMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIpIntfCfgMtu_Type.__name__ = "Integer32"
_WfIpIntfCfgMtu_Object = MibTableColumn
wfIpIntfCfgMtu = _WfIpIntfCfgMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 63),
    _WfIpIntfCfgMtu_Type()
)
wfIpIntfCfgMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgMtu.setStatus("mandatory")


class _WfIpIntfCfgDropIpMacBroadcast_Type(Integer32):
    """Custom type wfIpIntfCfgDropIpMacBroadcast based on Integer32"""
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


_WfIpIntfCfgDropIpMacBroadcast_Type.__name__ = "Integer32"
_WfIpIntfCfgDropIpMacBroadcast_Object = MibTableColumn
wfIpIntfCfgDropIpMacBroadcast = _WfIpIntfCfgDropIpMacBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 24, 1, 64),
    _WfIpIntfCfgDropIpMacBroadcast_Type()
)
wfIpIntfCfgDropIpMacBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpIntfCfgDropIpMacBroadcast.setStatus("mandatory")
_WfIpIntfStatsTable_Object = MibTable
wfIpIntfStatsTable = _WfIpIntfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25)
)
if mibBuilder.loadTexts:
    wfIpIntfStatsTable.setStatus("mandatory")
_WfIpIntfStatsEntry_Object = MibTableRow
wfIpIntfStatsEntry = _WfIpIntfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1)
)
wfIpIntfStatsEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpIntfStatsAddr"),
    (0, "Wellfleet-IP-MIB", "wfIpIntfStatsCircuit"),
)
if mibBuilder.loadTexts:
    wfIpIntfStatsEntry.setStatus("mandatory")
_WfIpIntfStatsAddr_Type = IpAddress
_WfIpIntfStatsAddr_Object = MibTableColumn
wfIpIntfStatsAddr = _WfIpIntfStatsAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 1),
    _WfIpIntfStatsAddr_Type()
)
wfIpIntfStatsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsAddr.setStatus("mandatory")
_WfIpIntfStatsCircuit_Type = Integer32
_WfIpIntfStatsCircuit_Object = MibTableColumn
wfIpIntfStatsCircuit = _WfIpIntfStatsCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 2),
    _WfIpIntfStatsCircuit_Type()
)
wfIpIntfStatsCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsCircuit.setStatus("mandatory")
_WfIpIntfStatsReasmMaxSize_Type = Gauge32
_WfIpIntfStatsReasmMaxSize_Object = MibTableColumn
wfIpIntfStatsReasmMaxSize = _WfIpIntfStatsReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 3),
    _WfIpIntfStatsReasmMaxSize_Type()
)
wfIpIntfStatsReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsReasmMaxSize.setStatus("mandatory")
_WfIpIntfStatsMaxInfo_Type = Integer32
_WfIpIntfStatsMaxInfo_Object = MibTableColumn
wfIpIntfStatsMaxInfo = _WfIpIntfStatsMaxInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 4),
    _WfIpIntfStatsMaxInfo_Type()
)
wfIpIntfStatsMaxInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsMaxInfo.setStatus("mandatory")
_WfIpIntfStatsInReceives_Type = Counter32
_WfIpIntfStatsInReceives_Object = MibTableColumn
wfIpIntfStatsInReceives = _WfIpIntfStatsInReceives_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 5),
    _WfIpIntfStatsInReceives_Type()
)
wfIpIntfStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsInReceives.setStatus("mandatory")
_WfIpIntfStatsInHdrErrors_Type = Counter32
_WfIpIntfStatsInHdrErrors_Object = MibTableColumn
wfIpIntfStatsInHdrErrors = _WfIpIntfStatsInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 6),
    _WfIpIntfStatsInHdrErrors_Type()
)
wfIpIntfStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsInHdrErrors.setStatus("mandatory")
_WfIpIntfStatsInAddrErrors_Type = Counter32
_WfIpIntfStatsInAddrErrors_Object = MibTableColumn
wfIpIntfStatsInAddrErrors = _WfIpIntfStatsInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 7),
    _WfIpIntfStatsInAddrErrors_Type()
)
wfIpIntfStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsInAddrErrors.setStatus("mandatory")
_WfIpIntfStatsForwDatagrams_Type = Counter32
_WfIpIntfStatsForwDatagrams_Object = MibTableColumn
wfIpIntfStatsForwDatagrams = _WfIpIntfStatsForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 8),
    _WfIpIntfStatsForwDatagrams_Type()
)
wfIpIntfStatsForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsForwDatagrams.setStatus("mandatory")
_WfIpIntfStatsInUnknownProtos_Type = Counter32
_WfIpIntfStatsInUnknownProtos_Object = MibTableColumn
wfIpIntfStatsInUnknownProtos = _WfIpIntfStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 9),
    _WfIpIntfStatsInUnknownProtos_Type()
)
wfIpIntfStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsInUnknownProtos.setStatus("mandatory")
_WfIpIntfStatsInDiscards_Type = Counter32
_WfIpIntfStatsInDiscards_Object = MibTableColumn
wfIpIntfStatsInDiscards = _WfIpIntfStatsInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 10),
    _WfIpIntfStatsInDiscards_Type()
)
wfIpIntfStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsInDiscards.setStatus("mandatory")
_WfIpIntfStatsInDelivers_Type = Counter32
_WfIpIntfStatsInDelivers_Object = MibTableColumn
wfIpIntfStatsInDelivers = _WfIpIntfStatsInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 11),
    _WfIpIntfStatsInDelivers_Type()
)
wfIpIntfStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsInDelivers.setStatus("mandatory")
_WfIpIntfStatsOutRequests_Type = Counter32
_WfIpIntfStatsOutRequests_Object = MibTableColumn
wfIpIntfStatsOutRequests = _WfIpIntfStatsOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 12),
    _WfIpIntfStatsOutRequests_Type()
)
wfIpIntfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsOutRequests.setStatus("mandatory")
_WfIpIntfStatsOutDiscards_Type = Counter32
_WfIpIntfStatsOutDiscards_Object = MibTableColumn
wfIpIntfStatsOutDiscards = _WfIpIntfStatsOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 13),
    _WfIpIntfStatsOutDiscards_Type()
)
wfIpIntfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsOutDiscards.setStatus("mandatory")
_WfIpIntfStatsOutNoRoutes_Type = Counter32
_WfIpIntfStatsOutNoRoutes_Object = MibTableColumn
wfIpIntfStatsOutNoRoutes = _WfIpIntfStatsOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 14),
    _WfIpIntfStatsOutNoRoutes_Type()
)
wfIpIntfStatsOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsOutNoRoutes.setStatus("mandatory")
_WfIpIntfStatsReasmTimeout_Type = Integer32
_WfIpIntfStatsReasmTimeout_Object = MibTableColumn
wfIpIntfStatsReasmTimeout = _WfIpIntfStatsReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 15),
    _WfIpIntfStatsReasmTimeout_Type()
)
wfIpIntfStatsReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsReasmTimeout.setStatus("mandatory")
_WfIpIntfStatsReasmReqds_Type = Counter32
_WfIpIntfStatsReasmReqds_Object = MibTableColumn
wfIpIntfStatsReasmReqds = _WfIpIntfStatsReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 16),
    _WfIpIntfStatsReasmReqds_Type()
)
wfIpIntfStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsReasmReqds.setStatus("mandatory")
_WfIpIntfStatsReasmOKs_Type = Counter32
_WfIpIntfStatsReasmOKs_Object = MibTableColumn
wfIpIntfStatsReasmOKs = _WfIpIntfStatsReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 17),
    _WfIpIntfStatsReasmOKs_Type()
)
wfIpIntfStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsReasmOKs.setStatus("mandatory")
_WfIpIntfStatsReasmFails_Type = Counter32
_WfIpIntfStatsReasmFails_Object = MibTableColumn
wfIpIntfStatsReasmFails = _WfIpIntfStatsReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 18),
    _WfIpIntfStatsReasmFails_Type()
)
wfIpIntfStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsReasmFails.setStatus("mandatory")
_WfIpIntfStatsFragOKs_Type = Counter32
_WfIpIntfStatsFragOKs_Object = MibTableColumn
wfIpIntfStatsFragOKs = _WfIpIntfStatsFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 19),
    _WfIpIntfStatsFragOKs_Type()
)
wfIpIntfStatsFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsFragOKs.setStatus("mandatory")
_WfIpIntfStatsFragFails_Type = Counter32
_WfIpIntfStatsFragFails_Object = MibTableColumn
wfIpIntfStatsFragFails = _WfIpIntfStatsFragFails_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 20),
    _WfIpIntfStatsFragFails_Type()
)
wfIpIntfStatsFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsFragFails.setStatus("mandatory")
_WfIpIntfStatsFragCreates_Type = Counter32
_WfIpIntfStatsFragCreates_Object = MibTableColumn
wfIpIntfStatsFragCreates = _WfIpIntfStatsFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 21),
    _WfIpIntfStatsFragCreates_Type()
)
wfIpIntfStatsFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsFragCreates.setStatus("mandatory")
_WfIpIntfStatsCacheMisses_Type = Counter32
_WfIpIntfStatsCacheMisses_Object = MibTableColumn
wfIpIntfStatsCacheMisses = _WfIpIntfStatsCacheMisses_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 22),
    _WfIpIntfStatsCacheMisses_Type()
)
wfIpIntfStatsCacheMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsCacheMisses.setStatus("mandatory")
_WfIpIntfStatsCacheNetworks_Type = Gauge32
_WfIpIntfStatsCacheNetworks_Object = MibTableColumn
wfIpIntfStatsCacheNetworks = _WfIpIntfStatsCacheNetworks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 23),
    _WfIpIntfStatsCacheNetworks_Type()
)
wfIpIntfStatsCacheNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsCacheNetworks.setStatus("mandatory")
_WfIpIntfStatsCacheRemoves_Type = Counter32
_WfIpIntfStatsCacheRemoves_Object = MibTableColumn
wfIpIntfStatsCacheRemoves = _WfIpIntfStatsCacheRemoves_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 24),
    _WfIpIntfStatsCacheRemoves_Type()
)
wfIpIntfStatsCacheRemoves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsCacheRemoves.setStatus("mandatory")
_WfIpIntfStatsDropRxAuths_Type = Counter32
_WfIpIntfStatsDropRxAuths_Object = MibTableColumn
wfIpIntfStatsDropRxAuths = _WfIpIntfStatsDropRxAuths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 25),
    _WfIpIntfStatsDropRxAuths_Type()
)
wfIpIntfStatsDropRxAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropRxAuths.setStatus("mandatory")
_WfIpIntfStatsDropRxFormats_Type = Counter32
_WfIpIntfStatsDropRxFormats_Object = MibTableColumn
wfIpIntfStatsDropRxFormats = _WfIpIntfStatsDropRxFormats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 26),
    _WfIpIntfStatsDropRxFormats_Type()
)
wfIpIntfStatsDropRxFormats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropRxFormats.setStatus("mandatory")
_WfIpIntfStatsDropRxLevels_Type = Counter32
_WfIpIntfStatsDropRxLevels_Object = MibTableColumn
wfIpIntfStatsDropRxLevels = _WfIpIntfStatsDropRxLevels_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 27),
    _WfIpIntfStatsDropRxLevels_Type()
)
wfIpIntfStatsDropRxLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropRxLevels.setStatus("mandatory")
_WfIpIntfStatsDropRxNoIpsos_Type = Counter32
_WfIpIntfStatsDropRxNoIpsos_Object = MibTableColumn
wfIpIntfStatsDropRxNoIpsos = _WfIpIntfStatsDropRxNoIpsos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 28),
    _WfIpIntfStatsDropRxNoIpsos_Type()
)
wfIpIntfStatsDropRxNoIpsos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropRxNoIpsos.setStatus("mandatory")
_WfIpIntfStatsDropTxAuths_Type = Counter32
_WfIpIntfStatsDropTxAuths_Object = MibTableColumn
wfIpIntfStatsDropTxAuths = _WfIpIntfStatsDropTxAuths_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 29),
    _WfIpIntfStatsDropTxAuths_Type()
)
wfIpIntfStatsDropTxAuths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropTxAuths.setStatus("mandatory")
_WfIpIntfStatsDropTxLevels_Type = Counter32
_WfIpIntfStatsDropTxLevels_Object = MibTableColumn
wfIpIntfStatsDropTxLevels = _WfIpIntfStatsDropTxLevels_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 30),
    _WfIpIntfStatsDropTxLevels_Type()
)
wfIpIntfStatsDropTxLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropTxLevels.setStatus("mandatory")
_WfIpIntfStatsDropTxNoIpsos_Type = Counter32
_WfIpIntfStatsDropTxNoIpsos_Object = MibTableColumn
wfIpIntfStatsDropTxNoIpsos = _WfIpIntfStatsDropTxNoIpsos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 31),
    _WfIpIntfStatsDropTxNoIpsos_Type()
)
wfIpIntfStatsDropTxNoIpsos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropTxNoIpsos.setStatus("mandatory")
_WfIpIntfStatsDropTxNoIpsoRooms_Type = Counter32
_WfIpIntfStatsDropTxNoIpsoRooms_Object = MibTableColumn
wfIpIntfStatsDropTxNoIpsoRooms = _WfIpIntfStatsDropTxNoIpsoRooms_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 32),
    _WfIpIntfStatsDropTxNoIpsoRooms_Type()
)
wfIpIntfStatsDropTxNoIpsoRooms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsDropTxNoIpsoRooms.setStatus("mandatory")
_WfIpIntfStatsRoutingDiscards_Type = Counter32
_WfIpIntfStatsRoutingDiscards_Object = MibTableColumn
wfIpIntfStatsRoutingDiscards = _WfIpIntfStatsRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 33),
    _WfIpIntfStatsRoutingDiscards_Type()
)
wfIpIntfStatsRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsRoutingDiscards.setStatus("mandatory")
_WfIpIntfStatsAtmArpAttemptedCalls_Type = Counter32
_WfIpIntfStatsAtmArpAttemptedCalls_Object = MibTableColumn
wfIpIntfStatsAtmArpAttemptedCalls = _WfIpIntfStatsAtmArpAttemptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 34),
    _WfIpIntfStatsAtmArpAttemptedCalls_Type()
)
wfIpIntfStatsAtmArpAttemptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsAtmArpAttemptedCalls.setStatus("mandatory")
_WfIpIntfStatsAtmArpFailRetryCalls_Type = Counter32
_WfIpIntfStatsAtmArpFailRetryCalls_Object = MibTableColumn
wfIpIntfStatsAtmArpFailRetryCalls = _WfIpIntfStatsAtmArpFailRetryCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 35),
    _WfIpIntfStatsAtmArpFailRetryCalls_Type()
)
wfIpIntfStatsAtmArpFailRetryCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsAtmArpFailRetryCalls.setStatus("mandatory")
_WfIpIntfStatsAtmArpFailNoRetryCalls_Type = Counter32
_WfIpIntfStatsAtmArpFailNoRetryCalls_Object = MibTableColumn
wfIpIntfStatsAtmArpFailNoRetryCalls = _WfIpIntfStatsAtmArpFailNoRetryCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 36),
    _WfIpIntfStatsAtmArpFailNoRetryCalls_Type()
)
wfIpIntfStatsAtmArpFailNoRetryCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsAtmArpFailNoRetryCalls.setStatus("mandatory")
_WfIpIntfStatsAtmArpSuccessfulCalls_Type = Counter32
_WfIpIntfStatsAtmArpSuccessfulCalls_Object = MibTableColumn
wfIpIntfStatsAtmArpSuccessfulCalls = _WfIpIntfStatsAtmArpSuccessfulCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 37),
    _WfIpIntfStatsAtmArpSuccessfulCalls_Type()
)
wfIpIntfStatsAtmArpSuccessfulCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsAtmArpSuccessfulCalls.setStatus("mandatory")
_WfIpIntfStatsAtmArpAcceptedCalls_Type = Counter32
_WfIpIntfStatsAtmArpAcceptedCalls_Object = MibTableColumn
wfIpIntfStatsAtmArpAcceptedCalls = _WfIpIntfStatsAtmArpAcceptedCalls_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 38),
    _WfIpIntfStatsAtmArpAcceptedCalls_Type()
)
wfIpIntfStatsAtmArpAcceptedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsAtmArpAcceptedCalls.setStatus("mandatory")
_WfIpIntfStatsAtmArpOpenSvcs_Type = Counter32
_WfIpIntfStatsAtmArpOpenSvcs_Object = MibTableColumn
wfIpIntfStatsAtmArpOpenSvcs = _WfIpIntfStatsAtmArpOpenSvcs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 39),
    _WfIpIntfStatsAtmArpOpenSvcs_Type()
)
wfIpIntfStatsAtmArpOpenSvcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsAtmArpOpenSvcs.setStatus("mandatory")
_WfIpIntfStatsMcastInPkts_Type = Counter32
_WfIpIntfStatsMcastInPkts_Object = MibTableColumn
wfIpIntfStatsMcastInPkts = _WfIpIntfStatsMcastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 40),
    _WfIpIntfStatsMcastInPkts_Type()
)
wfIpIntfStatsMcastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsMcastInPkts.setStatus("mandatory")
_WfIpIntfStatsMcastOutPkts_Type = Counter32
_WfIpIntfStatsMcastOutPkts_Object = MibTableColumn
wfIpIntfStatsMcastOutPkts = _WfIpIntfStatsMcastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 41),
    _WfIpIntfStatsMcastOutPkts_Type()
)
wfIpIntfStatsMcastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsMcastOutPkts.setStatus("mandatory")
_WfIpIntfStatsMcastInDataPkts_Type = Counter32
_WfIpIntfStatsMcastInDataPkts_Object = MibTableColumn
wfIpIntfStatsMcastInDataPkts = _WfIpIntfStatsMcastInDataPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 42),
    _WfIpIntfStatsMcastInDataPkts_Type()
)
wfIpIntfStatsMcastInDataPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsMcastInDataPkts.setStatus("mandatory")
_WfIpIntfStatsControlPathInPkts_Type = Counter32
_WfIpIntfStatsControlPathInPkts_Object = MibTableColumn
wfIpIntfStatsControlPathInPkts = _WfIpIntfStatsControlPathInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 43),
    _WfIpIntfStatsControlPathInPkts_Type()
)
wfIpIntfStatsControlPathInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsControlPathInPkts.setStatus("mandatory")
_WfIpIntfStatsControlPathOutPkts_Type = Counter32
_WfIpIntfStatsControlPathOutPkts_Object = MibTableColumn
wfIpIntfStatsControlPathOutPkts = _WfIpIntfStatsControlPathOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 25, 1, 44),
    _WfIpIntfStatsControlPathOutPkts_Type()
)
wfIpIntfStatsControlPathOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsControlPathOutPkts.setStatus("mandatory")
_WfIpIntfStatsIcmpTable_Object = MibTable
wfIpIntfStatsIcmpTable = _WfIpIntfStatsIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26)
)
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpTable.setStatus("mandatory")
_WfIpIntfStatsIcmpEntry_Object = MibTableRow
wfIpIntfStatsIcmpEntry = _WfIpIntfStatsIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1)
)
wfIpIntfStatsIcmpEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpIntfStatsIcmpAddr"),
    (0, "Wellfleet-IP-MIB", "wfIpIntfStatsIcmpCircuit"),
)
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpEntry.setStatus("mandatory")
_WfIpIntfStatsIcmpAddr_Type = IpAddress
_WfIpIntfStatsIcmpAddr_Object = MibTableColumn
wfIpIntfStatsIcmpAddr = _WfIpIntfStatsIcmpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 1),
    _WfIpIntfStatsIcmpAddr_Type()
)
wfIpIntfStatsIcmpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpAddr.setStatus("mandatory")
_WfIpIntfStatsIcmpCircuit_Type = Integer32
_WfIpIntfStatsIcmpCircuit_Object = MibTableColumn
wfIpIntfStatsIcmpCircuit = _WfIpIntfStatsIcmpCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 2),
    _WfIpIntfStatsIcmpCircuit_Type()
)
wfIpIntfStatsIcmpCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpCircuit.setStatus("mandatory")
_WfIpIntfStatsIcmpInMsgs_Type = Counter32
_WfIpIntfStatsIcmpInMsgs_Object = MibTableColumn
wfIpIntfStatsIcmpInMsgs = _WfIpIntfStatsIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 3),
    _WfIpIntfStatsIcmpInMsgs_Type()
)
wfIpIntfStatsIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInMsgs.setStatus("mandatory")
_WfIpIntfStatsIcmpInErrors_Type = Counter32
_WfIpIntfStatsIcmpInErrors_Object = MibTableColumn
wfIpIntfStatsIcmpInErrors = _WfIpIntfStatsIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 4),
    _WfIpIntfStatsIcmpInErrors_Type()
)
wfIpIntfStatsIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInErrors.setStatus("mandatory")
_WfIpIntfStatsIcmpInDestUnreachs_Type = Counter32
_WfIpIntfStatsIcmpInDestUnreachs_Object = MibTableColumn
wfIpIntfStatsIcmpInDestUnreachs = _WfIpIntfStatsIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 5),
    _WfIpIntfStatsIcmpInDestUnreachs_Type()
)
wfIpIntfStatsIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInDestUnreachs.setStatus("mandatory")
_WfIpIntfStatsIcmpInTimeExcds_Type = Counter32
_WfIpIntfStatsIcmpInTimeExcds_Object = MibTableColumn
wfIpIntfStatsIcmpInTimeExcds = _WfIpIntfStatsIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 6),
    _WfIpIntfStatsIcmpInTimeExcds_Type()
)
wfIpIntfStatsIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInTimeExcds.setStatus("mandatory")
_WfIpIntfStatsIcmpInParmProbs_Type = Counter32
_WfIpIntfStatsIcmpInParmProbs_Object = MibTableColumn
wfIpIntfStatsIcmpInParmProbs = _WfIpIntfStatsIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 7),
    _WfIpIntfStatsIcmpInParmProbs_Type()
)
wfIpIntfStatsIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInParmProbs.setStatus("mandatory")
_WfIpIntfStatsIcmpInSrcQuenchs_Type = Counter32
_WfIpIntfStatsIcmpInSrcQuenchs_Object = MibTableColumn
wfIpIntfStatsIcmpInSrcQuenchs = _WfIpIntfStatsIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 8),
    _WfIpIntfStatsIcmpInSrcQuenchs_Type()
)
wfIpIntfStatsIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInSrcQuenchs.setStatus("mandatory")
_WfIpIntfStatsIcmpInRedirects_Type = Counter32
_WfIpIntfStatsIcmpInRedirects_Object = MibTableColumn
wfIpIntfStatsIcmpInRedirects = _WfIpIntfStatsIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 9),
    _WfIpIntfStatsIcmpInRedirects_Type()
)
wfIpIntfStatsIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInRedirects.setStatus("mandatory")
_WfIpIntfStatsIcmpInEchos_Type = Counter32
_WfIpIntfStatsIcmpInEchos_Object = MibTableColumn
wfIpIntfStatsIcmpInEchos = _WfIpIntfStatsIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 10),
    _WfIpIntfStatsIcmpInEchos_Type()
)
wfIpIntfStatsIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInEchos.setStatus("mandatory")
_WfIpIntfStatsIcmpInEchoReps_Type = Counter32
_WfIpIntfStatsIcmpInEchoReps_Object = MibTableColumn
wfIpIntfStatsIcmpInEchoReps = _WfIpIntfStatsIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 11),
    _WfIpIntfStatsIcmpInEchoReps_Type()
)
wfIpIntfStatsIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInEchoReps.setStatus("mandatory")
_WfIpIntfStatsIcmpInTimestamps_Type = Counter32
_WfIpIntfStatsIcmpInTimestamps_Object = MibTableColumn
wfIpIntfStatsIcmpInTimestamps = _WfIpIntfStatsIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 12),
    _WfIpIntfStatsIcmpInTimestamps_Type()
)
wfIpIntfStatsIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInTimestamps.setStatus("mandatory")
_WfIpIntfStatsIcmpInTimestampReps_Type = Counter32
_WfIpIntfStatsIcmpInTimestampReps_Object = MibTableColumn
wfIpIntfStatsIcmpInTimestampReps = _WfIpIntfStatsIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 13),
    _WfIpIntfStatsIcmpInTimestampReps_Type()
)
wfIpIntfStatsIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInTimestampReps.setStatus("mandatory")
_WfIpIntfStatsIcmpInAddrMasks_Type = Counter32
_WfIpIntfStatsIcmpInAddrMasks_Object = MibTableColumn
wfIpIntfStatsIcmpInAddrMasks = _WfIpIntfStatsIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 14),
    _WfIpIntfStatsIcmpInAddrMasks_Type()
)
wfIpIntfStatsIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInAddrMasks.setStatus("mandatory")
_WfIpIntfStatsIcmpInAddrMaskReps_Type = Counter32
_WfIpIntfStatsIcmpInAddrMaskReps_Object = MibTableColumn
wfIpIntfStatsIcmpInAddrMaskReps = _WfIpIntfStatsIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 15),
    _WfIpIntfStatsIcmpInAddrMaskReps_Type()
)
wfIpIntfStatsIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInAddrMaskReps.setStatus("mandatory")
_WfIpIntfStatsIcmpOutMsgs_Type = Counter32
_WfIpIntfStatsIcmpOutMsgs_Object = MibTableColumn
wfIpIntfStatsIcmpOutMsgs = _WfIpIntfStatsIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 16),
    _WfIpIntfStatsIcmpOutMsgs_Type()
)
wfIpIntfStatsIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutMsgs.setStatus("mandatory")
_WfIpIntfStatsIcmpOutErrors_Type = Counter32
_WfIpIntfStatsIcmpOutErrors_Object = MibTableColumn
wfIpIntfStatsIcmpOutErrors = _WfIpIntfStatsIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 17),
    _WfIpIntfStatsIcmpOutErrors_Type()
)
wfIpIntfStatsIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutErrors.setStatus("mandatory")
_WfIpIntfStatsIcmpOutDestUnreachs_Type = Counter32
_WfIpIntfStatsIcmpOutDestUnreachs_Object = MibTableColumn
wfIpIntfStatsIcmpOutDestUnreachs = _WfIpIntfStatsIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 18),
    _WfIpIntfStatsIcmpOutDestUnreachs_Type()
)
wfIpIntfStatsIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutDestUnreachs.setStatus("mandatory")
_WfIpIntfStatsIcmpOutTimeExcds_Type = Counter32
_WfIpIntfStatsIcmpOutTimeExcds_Object = MibTableColumn
wfIpIntfStatsIcmpOutTimeExcds = _WfIpIntfStatsIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 19),
    _WfIpIntfStatsIcmpOutTimeExcds_Type()
)
wfIpIntfStatsIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutTimeExcds.setStatus("mandatory")
_WfIpIntfStatsIcmpOutParmProbs_Type = Counter32
_WfIpIntfStatsIcmpOutParmProbs_Object = MibTableColumn
wfIpIntfStatsIcmpOutParmProbs = _WfIpIntfStatsIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 20),
    _WfIpIntfStatsIcmpOutParmProbs_Type()
)
wfIpIntfStatsIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutParmProbs.setStatus("mandatory")
_WfIpIntfStatsIcmpOutSrcQuenchs_Type = Counter32
_WfIpIntfStatsIcmpOutSrcQuenchs_Object = MibTableColumn
wfIpIntfStatsIcmpOutSrcQuenchs = _WfIpIntfStatsIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 21),
    _WfIpIntfStatsIcmpOutSrcQuenchs_Type()
)
wfIpIntfStatsIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutSrcQuenchs.setStatus("mandatory")
_WfIpIntfStatsIcmpOutRedirects_Type = Counter32
_WfIpIntfStatsIcmpOutRedirects_Object = MibTableColumn
wfIpIntfStatsIcmpOutRedirects = _WfIpIntfStatsIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 22),
    _WfIpIntfStatsIcmpOutRedirects_Type()
)
wfIpIntfStatsIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutRedirects.setStatus("mandatory")
_WfIpIntfStatsIcmpOutEchos_Type = Counter32
_WfIpIntfStatsIcmpOutEchos_Object = MibTableColumn
wfIpIntfStatsIcmpOutEchos = _WfIpIntfStatsIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 23),
    _WfIpIntfStatsIcmpOutEchos_Type()
)
wfIpIntfStatsIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutEchos.setStatus("mandatory")
_WfIpIntfStatsIcmpOutEchoReps_Type = Counter32
_WfIpIntfStatsIcmpOutEchoReps_Object = MibTableColumn
wfIpIntfStatsIcmpOutEchoReps = _WfIpIntfStatsIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 24),
    _WfIpIntfStatsIcmpOutEchoReps_Type()
)
wfIpIntfStatsIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutEchoReps.setStatus("mandatory")
_WfIpIntfStatsIcmpOutTimestamps_Type = Counter32
_WfIpIntfStatsIcmpOutTimestamps_Object = MibTableColumn
wfIpIntfStatsIcmpOutTimestamps = _WfIpIntfStatsIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 25),
    _WfIpIntfStatsIcmpOutTimestamps_Type()
)
wfIpIntfStatsIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutTimestamps.setStatus("mandatory")
_WfIpIntfStatsIcmpOutTimestampReps_Type = Counter32
_WfIpIntfStatsIcmpOutTimestampReps_Object = MibTableColumn
wfIpIntfStatsIcmpOutTimestampReps = _WfIpIntfStatsIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 26),
    _WfIpIntfStatsIcmpOutTimestampReps_Type()
)
wfIpIntfStatsIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutTimestampReps.setStatus("mandatory")
_WfIpIntfStatsIcmpOutAddrMasks_Type = Counter32
_WfIpIntfStatsIcmpOutAddrMasks_Object = MibTableColumn
wfIpIntfStatsIcmpOutAddrMasks = _WfIpIntfStatsIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 27),
    _WfIpIntfStatsIcmpOutAddrMasks_Type()
)
wfIpIntfStatsIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutAddrMasks.setStatus("mandatory")
_WfIpIntfStatsIcmpOutAddrMaskReps_Type = Counter32
_WfIpIntfStatsIcmpOutAddrMaskReps_Object = MibTableColumn
wfIpIntfStatsIcmpOutAddrMaskReps = _WfIpIntfStatsIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 28),
    _WfIpIntfStatsIcmpOutAddrMaskReps_Type()
)
wfIpIntfStatsIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutAddrMaskReps.setStatus("mandatory")
_WfIpIntfStatsIcmpInAdminProhib_Type = Counter32
_WfIpIntfStatsIcmpInAdminProhib_Object = MibTableColumn
wfIpIntfStatsIcmpInAdminProhib = _WfIpIntfStatsIcmpInAdminProhib_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 29),
    _WfIpIntfStatsIcmpInAdminProhib_Type()
)
wfIpIntfStatsIcmpInAdminProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInAdminProhib.setStatus("mandatory")
_WfIpIntfStatsIcmpOutAdminProhib_Type = Counter32
_WfIpIntfStatsIcmpOutAdminProhib_Object = MibTableColumn
wfIpIntfStatsIcmpOutAdminProhib = _WfIpIntfStatsIcmpOutAdminProhib_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 30),
    _WfIpIntfStatsIcmpOutAdminProhib_Type()
)
wfIpIntfStatsIcmpOutAdminProhib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutAdminProhib.setStatus("mandatory")
_WfIpIntfStatsIcmpInRdiscSolicit_Type = Counter32
_WfIpIntfStatsIcmpInRdiscSolicit_Object = MibTableColumn
wfIpIntfStatsIcmpInRdiscSolicit = _WfIpIntfStatsIcmpInRdiscSolicit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 31),
    _WfIpIntfStatsIcmpInRdiscSolicit_Type()
)
wfIpIntfStatsIcmpInRdiscSolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInRdiscSolicit.setStatus("mandatory")
_WfIpIntfStatsIcmpInRdiscAdvert_Type = Counter32
_WfIpIntfStatsIcmpInRdiscAdvert_Object = MibTableColumn
wfIpIntfStatsIcmpInRdiscAdvert = _WfIpIntfStatsIcmpInRdiscAdvert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 32),
    _WfIpIntfStatsIcmpInRdiscAdvert_Type()
)
wfIpIntfStatsIcmpInRdiscAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpInRdiscAdvert.setStatus("mandatory")
_WfIpIntfStatsIcmpOutRdiscAdvert_Type = Counter32
_WfIpIntfStatsIcmpOutRdiscAdvert_Object = MibTableColumn
wfIpIntfStatsIcmpOutRdiscAdvert = _WfIpIntfStatsIcmpOutRdiscAdvert_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 26, 1, 33),
    _WfIpIntfStatsIcmpOutRdiscAdvert_Type()
)
wfIpIntfStatsIcmpOutRdiscAdvert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpIntfStatsIcmpOutRdiscAdvert.setStatus("mandatory")
_WfIpGreTnlTable_Object = MibTable
wfIpGreTnlTable = _WfIpGreTnlTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27)
)
if mibBuilder.loadTexts:
    wfIpGreTnlTable.setStatus("mandatory")
_WfIpGreTnlEntry_Object = MibTableRow
wfIpGreTnlEntry = _WfIpGreTnlEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1)
)
wfIpGreTnlEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpGreTnlNum"),
)
if mibBuilder.loadTexts:
    wfIpGreTnlEntry.setStatus("mandatory")


class _WfIpGreTnlCreate_Type(Integer32):
    """Custom type wfIpGreTnlCreate based on Integer32"""
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


_WfIpGreTnlCreate_Type.__name__ = "Integer32"
_WfIpGreTnlCreate_Object = MibTableColumn
wfIpGreTnlCreate = _WfIpGreTnlCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 1),
    _WfIpGreTnlCreate_Type()
)
wfIpGreTnlCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreTnlCreate.setStatus("mandatory")


class _WfIpGreTnlEnable_Type(Integer32):
    """Custom type wfIpGreTnlEnable based on Integer32"""
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


_WfIpGreTnlEnable_Type.__name__ = "Integer32"
_WfIpGreTnlEnable_Object = MibTableColumn
wfIpGreTnlEnable = _WfIpGreTnlEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 2),
    _WfIpGreTnlEnable_Type()
)
wfIpGreTnlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreTnlEnable.setStatus("mandatory")


class _WfIpGreTnlState_Type(Integer32):
    """Custom type wfIpGreTnlState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfIpGreTnlState_Type.__name__ = "Integer32"
_WfIpGreTnlState_Object = MibTableColumn
wfIpGreTnlState = _WfIpGreTnlState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 3),
    _WfIpGreTnlState_Type()
)
wfIpGreTnlState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpGreTnlState.setStatus("mandatory")
_WfIpGreTnlNum_Type = Integer32
_WfIpGreTnlNum_Object = MibTableColumn
wfIpGreTnlNum = _WfIpGreTnlNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 4),
    _WfIpGreTnlNum_Type()
)
wfIpGreTnlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpGreTnlNum.setStatus("mandatory")
_WfIpGreTnlName_Type = DisplayString
_WfIpGreTnlName_Object = MibTableColumn
wfIpGreTnlName = _WfIpGreTnlName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 5),
    _WfIpGreTnlName_Type()
)
wfIpGreTnlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreTnlName.setStatus("mandatory")


class _WfIpGreTnlCctNum_Type(Integer32):
    """Custom type wfIpGreTnlCctNum based on Integer32"""
    defaultValue = -1


_WfIpGreTnlCctNum_Object = MibTableColumn
wfIpGreTnlCctNum = _WfIpGreTnlCctNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 6),
    _WfIpGreTnlCctNum_Type()
)
wfIpGreTnlCctNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreTnlCctNum.setStatus("mandatory")
_WfIpGreTnlLocIpAddr_Type = IpAddress
_WfIpGreTnlLocIpAddr_Object = MibTableColumn
wfIpGreTnlLocIpAddr = _WfIpGreTnlLocIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 7),
    _WfIpGreTnlLocIpAddr_Type()
)
wfIpGreTnlLocIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreTnlLocIpAddr.setStatus("mandatory")


class _WfIpGreTnlMinMtu_Type(Integer32):
    """Custom type wfIpGreTnlMinMtu based on Integer32"""
    defaultValue = 0


_WfIpGreTnlMinMtu_Object = MibTableColumn
wfIpGreTnlMinMtu = _WfIpGreTnlMinMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 27, 1, 8),
    _WfIpGreTnlMinMtu_Type()
)
wfIpGreTnlMinMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreTnlMinMtu.setStatus("mandatory")
_WfIpGreConnTable_Object = MibTable
wfIpGreConnTable = _WfIpGreConnTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28)
)
if mibBuilder.loadTexts:
    wfIpGreConnTable.setStatus("mandatory")
_WfIpGreConnEntry_Object = MibTableRow
wfIpGreConnEntry = _WfIpGreConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1)
)
wfIpGreConnEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpGreConnTnlNum"),
    (0, "Wellfleet-IP-MIB", "wfIpGreConnNum"),
)
if mibBuilder.loadTexts:
    wfIpGreConnEntry.setStatus("mandatory")


class _WfIpGreConnCreate_Type(Integer32):
    """Custom type wfIpGreConnCreate based on Integer32"""
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


_WfIpGreConnCreate_Type.__name__ = "Integer32"
_WfIpGreConnCreate_Object = MibTableColumn
wfIpGreConnCreate = _WfIpGreConnCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1, 1),
    _WfIpGreConnCreate_Type()
)
wfIpGreConnCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreConnCreate.setStatus("mandatory")


class _WfIpGreConnEnable_Type(Integer32):
    """Custom type wfIpGreConnEnable based on Integer32"""
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


_WfIpGreConnEnable_Type.__name__ = "Integer32"
_WfIpGreConnEnable_Object = MibTableColumn
wfIpGreConnEnable = _WfIpGreConnEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1, 2),
    _WfIpGreConnEnable_Type()
)
wfIpGreConnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreConnEnable.setStatus("mandatory")
_WfIpGreConnTnlNum_Type = Integer32
_WfIpGreConnTnlNum_Object = MibTableColumn
wfIpGreConnTnlNum = _WfIpGreConnTnlNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1, 3),
    _WfIpGreConnTnlNum_Type()
)
wfIpGreConnTnlNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpGreConnTnlNum.setStatus("mandatory")
_WfIpGreConnNum_Type = Integer32
_WfIpGreConnNum_Object = MibTableColumn
wfIpGreConnNum = _WfIpGreConnNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1, 4),
    _WfIpGreConnNum_Type()
)
wfIpGreConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpGreConnNum.setStatus("mandatory")
_WfIpGreConnName_Type = DisplayString
_WfIpGreConnName_Object = MibTableColumn
wfIpGreConnName = _WfIpGreConnName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1, 5),
    _WfIpGreConnName_Type()
)
wfIpGreConnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreConnName.setStatus("mandatory")
_WfIpGreConnRemIpAddr_Type = IpAddress
_WfIpGreConnRemIpAddr_Object = MibTableColumn
wfIpGreConnRemIpAddr = _WfIpGreConnRemIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1, 6),
    _WfIpGreConnRemIpAddr_Type()
)
wfIpGreConnRemIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreConnRemIpAddr.setStatus("mandatory")
_WfIpGreConnProtoMap_Type = Integer32
_WfIpGreConnProtoMap_Object = MibTableColumn
wfIpGreConnProtoMap = _WfIpGreConnProtoMap_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 28, 1, 7),
    _WfIpGreConnProtoMap_Type()
)
wfIpGreConnProtoMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpGreConnProtoMap.setStatus("mandatory")
_WfIpFilterRuleTable_Object = MibTable
wfIpFilterRuleTable = _WfIpFilterRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29)
)
if mibBuilder.loadTexts:
    wfIpFilterRuleTable.setStatus("mandatory")
_WfIpFilterRuleEntry_Object = MibTableRow
wfIpFilterRuleEntry = _WfIpFilterRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1)
)
wfIpFilterRuleEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpFilterRuleNumber"),
    (0, "Wellfleet-IP-MIB", "wfIpFilterRuleFragment"),
)
if mibBuilder.loadTexts:
    wfIpFilterRuleEntry.setStatus("mandatory")


class _WfIpFilterRuleCreate_Type(Integer32):
    """Custom type wfIpFilterRuleCreate based on Integer32"""
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


_WfIpFilterRuleCreate_Type.__name__ = "Integer32"
_WfIpFilterRuleCreate_Object = MibTableColumn
wfIpFilterRuleCreate = _WfIpFilterRuleCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 1),
    _WfIpFilterRuleCreate_Type()
)
wfIpFilterRuleCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleCreate.setStatus("mandatory")
_WfIpFilterRuleNumber_Type = Integer32
_WfIpFilterRuleNumber_Object = MibTableColumn
wfIpFilterRuleNumber = _WfIpFilterRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 2),
    _WfIpFilterRuleNumber_Type()
)
wfIpFilterRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterRuleNumber.setStatus("mandatory")
_WfIpFilterRuleName_Type = DisplayString
_WfIpFilterRuleName_Object = MibTableColumn
wfIpFilterRuleName = _WfIpFilterRuleName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 3),
    _WfIpFilterRuleName_Type()
)
wfIpFilterRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleName.setStatus("mandatory")
_WfIpFilterRuleDescription_Type = Opaque
_WfIpFilterRuleDescription_Object = MibTableColumn
wfIpFilterRuleDescription = _WfIpFilterRuleDescription_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 4),
    _WfIpFilterRuleDescription_Type()
)
wfIpFilterRuleDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleDescription.setStatus("mandatory")
_WfIpFilterRuleFragment_Type = Integer32
_WfIpFilterRuleFragment_Object = MibTableColumn
wfIpFilterRuleFragment = _WfIpFilterRuleFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 5),
    _WfIpFilterRuleFragment_Type()
)
wfIpFilterRuleFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterRuleFragment.setStatus("mandatory")


class _WfIpFilterRuleNewTosValue_Type(Integer32):
    """Custom type wfIpFilterRuleNewTosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIpFilterRuleNewTosValue_Type.__name__ = "Integer32"
_WfIpFilterRuleNewTosValue_Object = MibTableColumn
wfIpFilterRuleNewTosValue = _WfIpFilterRuleNewTosValue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 6),
    _WfIpFilterRuleNewTosValue_Type()
)
wfIpFilterRuleNewTosValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleNewTosValue.setStatus("mandatory")
_WfIpFilterRuleNewTosValueMask_Type = Integer32
_WfIpFilterRuleNewTosValueMask_Object = MibTableColumn
wfIpFilterRuleNewTosValueMask = _WfIpFilterRuleNewTosValueMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 7),
    _WfIpFilterRuleNewTosValueMask_Type()
)
wfIpFilterRuleNewTosValueMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleNewTosValueMask.setStatus("mandatory")


class _WfIpFilterRuleAction_Type(Integer32):
    """Custom type wfIpFilterRuleAction based on Integer32"""
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
        *(("accept", 2),
          ("drop", 1),
          ("forwardtohost", 3))
    )


_WfIpFilterRuleAction_Type.__name__ = "Integer32"
_WfIpFilterRuleAction_Object = MibTableColumn
wfIpFilterRuleAction = _WfIpFilterRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 8),
    _WfIpFilterRuleAction_Type()
)
wfIpFilterRuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleAction.setStatus("mandatory")


class _WfIpFilterRuleClassifyAction_Type(Integer32):
    """Custom type wfIpFilterRuleClassifyAction based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(99, 99),
    )


_WfIpFilterRuleClassifyAction_Type.__name__ = "Integer32"
_WfIpFilterRuleClassifyAction_Object = MibTableColumn
wfIpFilterRuleClassifyAction = _WfIpFilterRuleClassifyAction_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 9),
    _WfIpFilterRuleClassifyAction_Type()
)
wfIpFilterRuleClassifyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleClassifyAction.setStatus("mandatory")


class _WfIpFilterRuleDropPreference_Type(Integer32):
    """Custom type wfIpFilterRuleDropPreference based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
        ValueRangeConstraint(99, 99),
    )


_WfIpFilterRuleDropPreference_Type.__name__ = "Integer32"
_WfIpFilterRuleDropPreference_Object = MibTableColumn
wfIpFilterRuleDropPreference = _WfIpFilterRuleDropPreference_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 29, 1, 10),
    _WfIpFilterRuleDropPreference_Type()
)
wfIpFilterRuleDropPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterRuleDropPreference.setStatus("mandatory")
_WfIpFilterConfigTable_Object = MibTable
wfIpFilterConfigTable = _WfIpFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30)
)
if mibBuilder.loadTexts:
    wfIpFilterConfigTable.setStatus("mandatory")
_WfIpFilterConfigEntry_Object = MibTableRow
wfIpFilterConfigEntry = _WfIpFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1)
)
wfIpFilterConfigEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpFilterConfigInterface"),
    (0, "Wellfleet-IP-MIB", "wfIpFilterConfigCircuit"),
    (0, "Wellfleet-IP-MIB", "wfIpFilterConfigIndex"),
)
if mibBuilder.loadTexts:
    wfIpFilterConfigEntry.setStatus("mandatory")


class _WfIpFilterConfigCreate_Type(Integer32):
    """Custom type wfIpFilterConfigCreate based on Integer32"""
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


_WfIpFilterConfigCreate_Type.__name__ = "Integer32"
_WfIpFilterConfigCreate_Object = MibTableColumn
wfIpFilterConfigCreate = _WfIpFilterConfigCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 1),
    _WfIpFilterConfigCreate_Type()
)
wfIpFilterConfigCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterConfigCreate.setStatus("mandatory")


class _WfIpFilterConfigEnable_Type(Integer32):
    """Custom type wfIpFilterConfigEnable based on Integer32"""
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


_WfIpFilterConfigEnable_Type.__name__ = "Integer32"
_WfIpFilterConfigEnable_Object = MibTableColumn
wfIpFilterConfigEnable = _WfIpFilterConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 2),
    _WfIpFilterConfigEnable_Type()
)
wfIpFilterConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterConfigEnable.setStatus("mandatory")


class _WfIpFilterConfigStatus_Type(Integer32):
    """Custom type wfIpFilterConfigStatus based on Integer32"""
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


_WfIpFilterConfigStatus_Type.__name__ = "Integer32"
_WfIpFilterConfigStatus_Object = MibTableColumn
wfIpFilterConfigStatus = _WfIpFilterConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 3),
    _WfIpFilterConfigStatus_Type()
)
wfIpFilterConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterConfigStatus.setStatus("mandatory")
_WfIpFilterConfigRuleNumber_Type = Integer32
_WfIpFilterConfigRuleNumber_Object = MibTableColumn
wfIpFilterConfigRuleNumber = _WfIpFilterConfigRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 4),
    _WfIpFilterConfigRuleNumber_Type()
)
wfIpFilterConfigRuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterConfigRuleNumber.setStatus("mandatory")
_WfIpFilterConfigRulePrecedence_Type = Integer32
_WfIpFilterConfigRulePrecedence_Object = MibTableColumn
wfIpFilterConfigRulePrecedence = _WfIpFilterConfigRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 5),
    _WfIpFilterConfigRulePrecedence_Type()
)
wfIpFilterConfigRulePrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterConfigRulePrecedence.setStatus("mandatory")


class _WfIpFilterConfigFilterType_Type(Integer32):
    """Custom type wfIpFilterConfigFilterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_WfIpFilterConfigFilterType_Type.__name__ = "Integer32"
_WfIpFilterConfigFilterType_Object = MibTableColumn
wfIpFilterConfigFilterType = _WfIpFilterConfigFilterType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 6),
    _WfIpFilterConfigFilterType_Type()
)
wfIpFilterConfigFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterConfigFilterType.setStatus("mandatory")


class _WfIpFilterConfigLogFilterInfo_Type(Integer32):
    """Custom type wfIpFilterConfigLogFilterInfo based on Integer32"""
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


_WfIpFilterConfigLogFilterInfo_Type.__name__ = "Integer32"
_WfIpFilterConfigLogFilterInfo_Object = MibTableColumn
wfIpFilterConfigLogFilterInfo = _WfIpFilterConfigLogFilterInfo_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 7),
    _WfIpFilterConfigLogFilterInfo_Type()
)
wfIpFilterConfigLogFilterInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterConfigLogFilterInfo.setStatus("mandatory")
_WfIpFilterConfigReserved_Type = Integer32
_WfIpFilterConfigReserved_Object = MibTableColumn
wfIpFilterConfigReserved = _WfIpFilterConfigReserved_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 8),
    _WfIpFilterConfigReserved_Type()
)
wfIpFilterConfigReserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterConfigReserved.setStatus("mandatory")
_WfIpFilterConfigInterface_Type = IpAddress
_WfIpFilterConfigInterface_Object = MibTableColumn
wfIpFilterConfigInterface = _WfIpFilterConfigInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 9),
    _WfIpFilterConfigInterface_Type()
)
wfIpFilterConfigInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterConfigInterface.setStatus("mandatory")
_WfIpFilterConfigCircuit_Type = Integer32
_WfIpFilterConfigCircuit_Object = MibTableColumn
wfIpFilterConfigCircuit = _WfIpFilterConfigCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 10),
    _WfIpFilterConfigCircuit_Type()
)
wfIpFilterConfigCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterConfigCircuit.setStatus("mandatory")
_WfIpFilterConfigIndex_Type = Integer32
_WfIpFilterConfigIndex_Object = MibTableColumn
wfIpFilterConfigIndex = _WfIpFilterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 30, 1, 11),
    _WfIpFilterConfigIndex_Type()
)
wfIpFilterConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterConfigIndex.setStatus("mandatory")
_WfIpFilterStatsTable_Object = MibTable
wfIpFilterStatsTable = _WfIpFilterStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 31)
)
if mibBuilder.loadTexts:
    wfIpFilterStatsTable.setStatus("mandatory")
_WfIpFilterStatsEntry_Object = MibTableRow
wfIpFilterStatsEntry = _WfIpFilterStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 31, 1)
)
wfIpFilterStatsEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpFilterStatsInterface"),
    (0, "Wellfleet-IP-MIB", "wfIpFilterStatsCircuit"),
    (0, "Wellfleet-IP-MIB", "wfIpFilterStatsIndex"),
)
if mibBuilder.loadTexts:
    wfIpFilterStatsEntry.setStatus("mandatory")
_WfIpFilterStatsCounter_Type = Counter32
_WfIpFilterStatsCounter_Object = MibTableColumn
wfIpFilterStatsCounter = _WfIpFilterStatsCounter_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 31, 1, 1),
    _WfIpFilterStatsCounter_Type()
)
wfIpFilterStatsCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterStatsCounter.setStatus("mandatory")
_WfIpFilterStatsInterface_Type = IpAddress
_WfIpFilterStatsInterface_Object = MibTableColumn
wfIpFilterStatsInterface = _WfIpFilterStatsInterface_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 31, 1, 2),
    _WfIpFilterStatsInterface_Type()
)
wfIpFilterStatsInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterStatsInterface.setStatus("mandatory")
_WfIpFilterStatsCircuit_Type = Integer32
_WfIpFilterStatsCircuit_Object = MibTableColumn
wfIpFilterStatsCircuit = _WfIpFilterStatsCircuit_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 31, 1, 3),
    _WfIpFilterStatsCircuit_Type()
)
wfIpFilterStatsCircuit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterStatsCircuit.setStatus("mandatory")
_WfIpFilterStatsIndex_Type = Integer32
_WfIpFilterStatsIndex_Object = MibTableColumn
wfIpFilterStatsIndex = _WfIpFilterStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 31, 1, 4),
    _WfIpFilterStatsIndex_Type()
)
wfIpFilterStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterStatsIndex.setStatus("mandatory")
_WfIpTosTemplateCfgTable_Object = MibTable
wfIpTosTemplateCfgTable = _WfIpTosTemplateCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32)
)
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgTable.setStatus("obsolete")
_WfIpTosTemplateCfgEntry_Object = MibTableRow
wfIpTosTemplateCfgEntry = _WfIpTosTemplateCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1)
)
wfIpTosTemplateCfgEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpTosTemplateCfgIndex"),
)
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgEntry.setStatus("obsolete")


class _WfIpTosTemplateCfgCreate_Type(Integer32):
    """Custom type wfIpTosTemplateCfgCreate based on Integer32"""
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


_WfIpTosTemplateCfgCreate_Type.__name__ = "Integer32"
_WfIpTosTemplateCfgCreate_Object = MibTableColumn
wfIpTosTemplateCfgCreate = _WfIpTosTemplateCfgCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 1),
    _WfIpTosTemplateCfgCreate_Type()
)
wfIpTosTemplateCfgCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgCreate.setStatus("obsolete")


class _WfIpTosTemplateCfgIndex_Type(Integer32):
    """Custom type wfIpTosTemplateCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(33, 256),
    )


_WfIpTosTemplateCfgIndex_Type.__name__ = "Integer32"
_WfIpTosTemplateCfgIndex_Object = MibTableColumn
wfIpTosTemplateCfgIndex = _WfIpTosTemplateCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 2),
    _WfIpTosTemplateCfgIndex_Type()
)
wfIpTosTemplateCfgIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgIndex.setStatus("obsolete")
_WfIpTosTemplateCfgName_Type = DisplayString
_WfIpTosTemplateCfgName_Object = MibTableColumn
wfIpTosTemplateCfgName = _WfIpTosTemplateCfgName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 3),
    _WfIpTosTemplateCfgName_Type()
)
wfIpTosTemplateCfgName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgName.setStatus("obsolete")


class _WfIpTosTemplateCfgStatus_Type(Integer32):
    """Custom type wfIpTosTemplateCfgStatus based on Integer32"""
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
        *(("invalid", 2),
          ("notconfigurable", 3),
          ("valid", 1))
    )


_WfIpTosTemplateCfgStatus_Type.__name__ = "Integer32"
_WfIpTosTemplateCfgStatus_Object = MibTableColumn
wfIpTosTemplateCfgStatus = _WfIpTosTemplateCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 4),
    _WfIpTosTemplateCfgStatus_Type()
)
wfIpTosTemplateCfgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgStatus.setStatus("obsolete")


class _WfIpTosTemplateCfgRxEnable_Type(Integer32):
    """Custom type wfIpTosTemplateCfgRxEnable based on Integer32"""
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


_WfIpTosTemplateCfgRxEnable_Type.__name__ = "Integer32"
_WfIpTosTemplateCfgRxEnable_Object = MibTableColumn
wfIpTosTemplateCfgRxEnable = _WfIpTosTemplateCfgRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 5),
    _WfIpTosTemplateCfgRxEnable_Type()
)
wfIpTosTemplateCfgRxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgRxEnable.setStatus("obsolete")
_WfIpTosTemplateCfgRxMapping_Type = OctetString
_WfIpTosTemplateCfgRxMapping_Object = MibTableColumn
wfIpTosTemplateCfgRxMapping = _WfIpTosTemplateCfgRxMapping_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 6),
    _WfIpTosTemplateCfgRxMapping_Type()
)
wfIpTosTemplateCfgRxMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgRxMapping.setStatus("obsolete")


class _WfIpTosTemplateCfgTxEnable_Type(Integer32):
    """Custom type wfIpTosTemplateCfgTxEnable based on Integer32"""
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


_WfIpTosTemplateCfgTxEnable_Type.__name__ = "Integer32"
_WfIpTosTemplateCfgTxEnable_Object = MibTableColumn
wfIpTosTemplateCfgTxEnable = _WfIpTosTemplateCfgTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 7),
    _WfIpTosTemplateCfgTxEnable_Type()
)
wfIpTosTemplateCfgTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgTxEnable.setStatus("obsolete")
_WfIpTosTemplateCfgTxMapping_Type = OctetString
_WfIpTosTemplateCfgTxMapping_Object = MibTableColumn
wfIpTosTemplateCfgTxMapping = _WfIpTosTemplateCfgTxMapping_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 32, 1, 8),
    _WfIpTosTemplateCfgTxMapping_Type()
)
wfIpTosTemplateCfgTxMapping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpTosTemplateCfgTxMapping.setStatus("obsolete")
_WfIpTosTemplateTable_Object = MibTable
wfIpTosTemplateTable = _WfIpTosTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33)
)
if mibBuilder.loadTexts:
    wfIpTosTemplateTable.setStatus("obsolete")
_WfIpTosTemplateEntry_Object = MibTableRow
wfIpTosTemplateEntry = _WfIpTosTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1)
)
wfIpTosTemplateEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpTosTemplateIndex"),
)
if mibBuilder.loadTexts:
    wfIpTosTemplateEntry.setStatus("obsolete")


class _WfIpTosTemplateIndex_Type(Integer32):
    """Custom type wfIpTosTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_WfIpTosTemplateIndex_Type.__name__ = "Integer32"
_WfIpTosTemplateIndex_Object = MibTableColumn
wfIpTosTemplateIndex = _WfIpTosTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1, 1),
    _WfIpTosTemplateIndex_Type()
)
wfIpTosTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateIndex.setStatus("obsolete")
_WfIpTosTemplateName_Type = DisplayString
_WfIpTosTemplateName_Object = MibTableColumn
wfIpTosTemplateName = _WfIpTosTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1, 2),
    _WfIpTosTemplateName_Type()
)
wfIpTosTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateName.setStatus("obsolete")


class _WfIpTosTemplateStatus_Type(Integer32):
    """Custom type wfIpTosTemplateStatus based on Integer32"""
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
        *(("builtin", 3),
          ("invalid", 2),
          ("valid", 1))
    )


_WfIpTosTemplateStatus_Type.__name__ = "Integer32"
_WfIpTosTemplateStatus_Object = MibTableColumn
wfIpTosTemplateStatus = _WfIpTosTemplateStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1, 3),
    _WfIpTosTemplateStatus_Type()
)
wfIpTosTemplateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateStatus.setStatus("obsolete")


class _WfIpTosTemplateRxEnable_Type(Integer32):
    """Custom type wfIpTosTemplateRxEnable based on Integer32"""
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


_WfIpTosTemplateRxEnable_Type.__name__ = "Integer32"
_WfIpTosTemplateRxEnable_Object = MibTableColumn
wfIpTosTemplateRxEnable = _WfIpTosTemplateRxEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1, 4),
    _WfIpTosTemplateRxEnable_Type()
)
wfIpTosTemplateRxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateRxEnable.setStatus("obsolete")
_WfIpTosTemplateRxMapping_Type = OctetString
_WfIpTosTemplateRxMapping_Object = MibTableColumn
wfIpTosTemplateRxMapping = _WfIpTosTemplateRxMapping_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1, 5),
    _WfIpTosTemplateRxMapping_Type()
)
wfIpTosTemplateRxMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateRxMapping.setStatus("obsolete")


class _WfIpTosTemplateTxEnable_Type(Integer32):
    """Custom type wfIpTosTemplateTxEnable based on Integer32"""
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


_WfIpTosTemplateTxEnable_Type.__name__ = "Integer32"
_WfIpTosTemplateTxEnable_Object = MibTableColumn
wfIpTosTemplateTxEnable = _WfIpTosTemplateTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1, 6),
    _WfIpTosTemplateTxEnable_Type()
)
wfIpTosTemplateTxEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateTxEnable.setStatus("obsolete")
_WfIpTosTemplateTxMapping_Type = OctetString
_WfIpTosTemplateTxMapping_Object = MibTableColumn
wfIpTosTemplateTxMapping = _WfIpTosTemplateTxMapping_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 33, 1, 7),
    _WfIpTosTemplateTxMapping_Type()
)
wfIpTosTemplateTxMapping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpTosTemplateTxMapping.setStatus("obsolete")
_WfIpBaseDbg_ObjectIdentity = ObjectIdentity
wfIpBaseDbg = _WfIpBaseDbg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 34)
)


class _WfIpBaseDbgCreate_Type(Integer32):
    """Custom type wfIpBaseDbgCreate based on Integer32"""
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


_WfIpBaseDbgCreate_Type.__name__ = "Integer32"
_WfIpBaseDbgCreate_Object = MibScalar
wfIpBaseDbgCreate = _WfIpBaseDbgCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 34, 1),
    _WfIpBaseDbgCreate_Type()
)
wfIpBaseDbgCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDbgCreate.setStatus("mandatory")
_WfIpBaseDbgOptions_Type = Integer32
_WfIpBaseDbgOptions_Object = MibScalar
wfIpBaseDbgOptions = _WfIpBaseDbgOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 34, 2),
    _WfIpBaseDbgOptions_Type()
)
wfIpBaseDbgOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDbgOptions.setStatus("mandatory")
_WfIpBaseDbgAddress_Type = IpAddress
_WfIpBaseDbgAddress_Object = MibScalar
wfIpBaseDbgAddress = _WfIpBaseDbgAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 34, 3),
    _WfIpBaseDbgAddress_Type()
)
wfIpBaseDbgAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDbgAddress.setStatus("mandatory")
_WfIpBaseDbgAddressMask_Type = IpAddress
_WfIpBaseDbgAddressMask_Object = MibScalar
wfIpBaseDbgAddressMask = _WfIpBaseDbgAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 34, 4),
    _WfIpBaseDbgAddressMask_Type()
)
wfIpBaseDbgAddressMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDbgAddressMask.setStatus("mandatory")
_WfIpBaseDbgMisc_Type = Integer32
_WfIpBaseDbgMisc_Object = MibScalar
wfIpBaseDbgMisc = _WfIpBaseDbgMisc_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 34, 5),
    _WfIpBaseDbgMisc_Type()
)
wfIpBaseDbgMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpBaseDbgMisc.setStatus("mandatory")
_WfIpFilterTemplateTable_Object = MibTable
wfIpFilterTemplateTable = _WfIpFilterTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 35)
)
if mibBuilder.loadTexts:
    wfIpFilterTemplateTable.setStatus("mandatory")
_WfIpFilterTemplateEntry_Object = MibTableRow
wfIpFilterTemplateEntry = _WfIpFilterTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 35, 1)
)
wfIpFilterTemplateEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfIpFilterTemplateRuleNumber"),
    (0, "Wellfleet-IP-MIB", "wfIpFilterTemplateFragment"),
)
if mibBuilder.loadTexts:
    wfIpFilterTemplateEntry.setStatus("mandatory")


class _WfIpFilterTemplateCreate_Type(Integer32):
    """Custom type wfIpFilterTemplateCreate based on Integer32"""
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


_WfIpFilterTemplateCreate_Type.__name__ = "Integer32"
_WfIpFilterTemplateCreate_Object = MibTableColumn
wfIpFilterTemplateCreate = _WfIpFilterTemplateCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 35, 1, 1),
    _WfIpFilterTemplateCreate_Type()
)
wfIpFilterTemplateCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterTemplateCreate.setStatus("mandatory")
_WfIpFilterTemplateRuleNumber_Type = Integer32
_WfIpFilterTemplateRuleNumber_Object = MibTableColumn
wfIpFilterTemplateRuleNumber = _WfIpFilterTemplateRuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 35, 1, 2),
    _WfIpFilterTemplateRuleNumber_Type()
)
wfIpFilterTemplateRuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterTemplateRuleNumber.setStatus("mandatory")
_WfIpFilterTemplateFragment_Type = Integer32
_WfIpFilterTemplateFragment_Object = MibTableColumn
wfIpFilterTemplateFragment = _WfIpFilterTemplateFragment_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 35, 1, 3),
    _WfIpFilterTemplateFragment_Type()
)
wfIpFilterTemplateFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIpFilterTemplateFragment.setStatus("mandatory")
_WfIpFilterTemplateDefinition_Type = Opaque
_WfIpFilterTemplateDefinition_Object = MibTableColumn
wfIpFilterTemplateDefinition = _WfIpFilterTemplateDefinition_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 35, 1, 4),
    _WfIpFilterTemplateDefinition_Type()
)
wfIpFilterTemplateDefinition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterTemplateDefinition.setStatus("mandatory")
_WfIpFilterTemplateName_Type = DisplayString
_WfIpFilterTemplateName_Object = MibTableColumn
wfIpFilterTemplateName = _WfIpFilterTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 1, 35, 1, 5),
    _WfIpFilterTemplateName_Type()
)
wfIpFilterTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfIpFilterTemplateName.setStatus("mandatory")
_WfRipIntfTable_Object = MibTable
wfRipIntfTable = _WfRipIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    wfRipIntfTable.setStatus("obsolete")
_WfRipIntfEntry_Object = MibTableRow
wfRipIntfEntry = _WfRipIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1)
)
wfRipIntfEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfRipInterfaceIndex"),
)
if mibBuilder.loadTexts:
    wfRipIntfEntry.setStatus("obsolete")


class _WfRipInterfaceCreate_Type(Integer32):
    """Custom type wfRipInterfaceCreate based on Integer32"""
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


_WfRipInterfaceCreate_Type.__name__ = "Integer32"
_WfRipInterfaceCreate_Object = MibTableColumn
wfRipInterfaceCreate = _WfRipInterfaceCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 1),
    _WfRipInterfaceCreate_Type()
)
wfRipInterfaceCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceCreate.setStatus("obsolete")


class _WfRipInterfaceEnable_Type(Integer32):
    """Custom type wfRipInterfaceEnable based on Integer32"""
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


_WfRipInterfaceEnable_Type.__name__ = "Integer32"
_WfRipInterfaceEnable_Object = MibTableColumn
wfRipInterfaceEnable = _WfRipInterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 2),
    _WfRipInterfaceEnable_Type()
)
wfRipInterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceEnable.setStatus("obsolete")


class _WfRipInterfaceState_Type(Integer32):
    """Custom type wfRipInterfaceState based on Integer32"""
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


_WfRipInterfaceState_Type.__name__ = "Integer32"
_WfRipInterfaceState_Object = MibTableColumn
wfRipInterfaceState = _WfRipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 3),
    _WfRipInterfaceState_Type()
)
wfRipInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipInterfaceState.setStatus("obsolete")
_WfRipInterfaceIndex_Type = IpAddress
_WfRipInterfaceIndex_Object = MibTableColumn
wfRipInterfaceIndex = _WfRipInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 4),
    _WfRipInterfaceIndex_Type()
)
wfRipInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipInterfaceIndex.setStatus("obsolete")


class _WfRipInterfaceSupply_Type(Integer32):
    """Custom type wfRipInterfaceSupply based on Integer32"""
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


_WfRipInterfaceSupply_Type.__name__ = "Integer32"
_WfRipInterfaceSupply_Object = MibTableColumn
wfRipInterfaceSupply = _WfRipInterfaceSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 5),
    _WfRipInterfaceSupply_Type()
)
wfRipInterfaceSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceSupply.setStatus("obsolete")


class _WfRipInterfaceListen_Type(Integer32):
    """Custom type wfRipInterfaceListen based on Integer32"""
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


_WfRipInterfaceListen_Type.__name__ = "Integer32"
_WfRipInterfaceListen_Object = MibTableColumn
wfRipInterfaceListen = _WfRipInterfaceListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 6),
    _WfRipInterfaceListen_Type()
)
wfRipInterfaceListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceListen.setStatus("obsolete")


class _WfRipInterfaceDefaultRouteSupply_Type(Integer32):
    """Custom type wfRipInterfaceDefaultRouteSupply based on Integer32"""
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


_WfRipInterfaceDefaultRouteSupply_Type.__name__ = "Integer32"
_WfRipInterfaceDefaultRouteSupply_Object = MibTableColumn
wfRipInterfaceDefaultRouteSupply = _WfRipInterfaceDefaultRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 7),
    _WfRipInterfaceDefaultRouteSupply_Type()
)
wfRipInterfaceDefaultRouteSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceDefaultRouteSupply.setStatus("obsolete")


class _WfRipInterfaceDefaultRouteListen_Type(Integer32):
    """Custom type wfRipInterfaceDefaultRouteListen based on Integer32"""
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


_WfRipInterfaceDefaultRouteListen_Type.__name__ = "Integer32"
_WfRipInterfaceDefaultRouteListen_Object = MibTableColumn
wfRipInterfaceDefaultRouteListen = _WfRipInterfaceDefaultRouteListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 8),
    _WfRipInterfaceDefaultRouteListen_Type()
)
wfRipInterfaceDefaultRouteListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfaceDefaultRouteListen.setStatus("obsolete")


class _WfRipInterfacePoisonedReversed_Type(Integer32):
    """Custom type wfRipInterfacePoisonedReversed based on Integer32"""
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
        *(("actual", 2),
          ("poisoned", 1),
          ("split", 3))
    )


_WfRipInterfacePoisonedReversed_Type.__name__ = "Integer32"
_WfRipInterfacePoisonedReversed_Object = MibTableColumn
wfRipInterfacePoisonedReversed = _WfRipInterfacePoisonedReversed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 1, 1, 9),
    _WfRipInterfacePoisonedReversed_Type()
)
wfRipInterfacePoisonedReversed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipInterfacePoisonedReversed.setStatus("obsolete")
_WfRipInterfaceTable_Object = MibTable
wfRipInterfaceTable = _WfRipInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2)
)
if mibBuilder.loadTexts:
    wfRipInterfaceTable.setStatus("mandatory")
_WfRipInterfaceEntry_Object = MibTableRow
wfRipInterfaceEntry = _WfRipInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1)
)
wfRipInterfaceEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfRipIntfIndex"),
    (0, "Wellfleet-IP-MIB", "wfRipIntfCct"),
)
if mibBuilder.loadTexts:
    wfRipInterfaceEntry.setStatus("mandatory")


class _WfRipIntfCreate_Type(Integer32):
    """Custom type wfRipIntfCreate based on Integer32"""
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


_WfRipIntfCreate_Type.__name__ = "Integer32"
_WfRipIntfCreate_Object = MibTableColumn
wfRipIntfCreate = _WfRipIntfCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 1),
    _WfRipIntfCreate_Type()
)
wfRipIntfCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfCreate.setStatus("mandatory")


class _WfRipIntfEnable_Type(Integer32):
    """Custom type wfRipIntfEnable based on Integer32"""
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


_WfRipIntfEnable_Type.__name__ = "Integer32"
_WfRipIntfEnable_Object = MibTableColumn
wfRipIntfEnable = _WfRipIntfEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 2),
    _WfRipIntfEnable_Type()
)
wfRipIntfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfEnable.setStatus("mandatory")


class _WfRipIntfState_Type(Integer32):
    """Custom type wfRipIntfState based on Integer32"""
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


_WfRipIntfState_Type.__name__ = "Integer32"
_WfRipIntfState_Object = MibTableColumn
wfRipIntfState = _WfRipIntfState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 3),
    _WfRipIntfState_Type()
)
wfRipIntfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipIntfState.setStatus("mandatory")
_WfRipIntfIndex_Type = IpAddress
_WfRipIntfIndex_Object = MibTableColumn
wfRipIntfIndex = _WfRipIntfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 4),
    _WfRipIntfIndex_Type()
)
wfRipIntfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipIntfIndex.setStatus("mandatory")


class _WfRipIntfSupply_Type(Integer32):
    """Custom type wfRipIntfSupply based on Integer32"""
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


_WfRipIntfSupply_Type.__name__ = "Integer32"
_WfRipIntfSupply_Object = MibTableColumn
wfRipIntfSupply = _WfRipIntfSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 5),
    _WfRipIntfSupply_Type()
)
wfRipIntfSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfSupply.setStatus("mandatory")


class _WfRipIntfListen_Type(Integer32):
    """Custom type wfRipIntfListen based on Integer32"""
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


_WfRipIntfListen_Type.__name__ = "Integer32"
_WfRipIntfListen_Object = MibTableColumn
wfRipIntfListen = _WfRipIntfListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 6),
    _WfRipIntfListen_Type()
)
wfRipIntfListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfListen.setStatus("mandatory")


class _WfRipIntfDefaultRouteSupply_Type(Integer32):
    """Custom type wfRipIntfDefaultRouteSupply based on Integer32"""
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
          ("generated", 3))
    )


_WfRipIntfDefaultRouteSupply_Type.__name__ = "Integer32"
_WfRipIntfDefaultRouteSupply_Object = MibTableColumn
wfRipIntfDefaultRouteSupply = _WfRipIntfDefaultRouteSupply_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 7),
    _WfRipIntfDefaultRouteSupply_Type()
)
wfRipIntfDefaultRouteSupply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfDefaultRouteSupply.setStatus("mandatory")


class _WfRipIntfDefaultRouteListen_Type(Integer32):
    """Custom type wfRipIntfDefaultRouteListen based on Integer32"""
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


_WfRipIntfDefaultRouteListen_Type.__name__ = "Integer32"
_WfRipIntfDefaultRouteListen_Object = MibTableColumn
wfRipIntfDefaultRouteListen = _WfRipIntfDefaultRouteListen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 8),
    _WfRipIntfDefaultRouteListen_Type()
)
wfRipIntfDefaultRouteListen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfDefaultRouteListen.setStatus("mandatory")


class _WfRipIntfPoisonedReversed_Type(Integer32):
    """Custom type wfRipIntfPoisonedReversed based on Integer32"""
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
        *(("actual", 2),
          ("poisoned", 1),
          ("split", 3))
    )


_WfRipIntfPoisonedReversed_Type.__name__ = "Integer32"
_WfRipIntfPoisonedReversed_Object = MibTableColumn
wfRipIntfPoisonedReversed = _WfRipIntfPoisonedReversed_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 9),
    _WfRipIntfPoisonedReversed_Type()
)
wfRipIntfPoisonedReversed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfPoisonedReversed.setStatus("mandatory")
_WfRipIntfCct_Type = Integer32
_WfRipIntfCct_Object = MibTableColumn
wfRipIntfCct = _WfRipIntfCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 10),
    _WfRipIntfCct_Type()
)
wfRipIntfCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRipIntfCct.setStatus("mandatory")


class _WfRipIntfTTL_Type(Integer32):
    """Custom type wfRipIntfTTL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WfRipIntfTTL_Type.__name__ = "Integer32"
_WfRipIntfTTL_Object = MibTableColumn
wfRipIntfTTL = _WfRipIntfTTL_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 11),
    _WfRipIntfTTL_Type()
)
wfRipIntfTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfTTL.setStatus("mandatory")


class _WfRipIntfBroadcastTimer_Type(Integer32):
    """Custom type wfRipIntfBroadcastTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1209600),
    )


_WfRipIntfBroadcastTimer_Type.__name__ = "Integer32"
_WfRipIntfBroadcastTimer_Object = MibTableColumn
wfRipIntfBroadcastTimer = _WfRipIntfBroadcastTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 12),
    _WfRipIntfBroadcastTimer_Type()
)
wfRipIntfBroadcastTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfBroadcastTimer.setStatus("mandatory")


class _WfRipIntfTimeoutTimer_Type(Integer32):
    """Custom type wfRipIntfTimeoutTimer based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 3628800),
    )


_WfRipIntfTimeoutTimer_Type.__name__ = "Integer32"
_WfRipIntfTimeoutTimer_Object = MibTableColumn
wfRipIntfTimeoutTimer = _WfRipIntfTimeoutTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 13),
    _WfRipIntfTimeoutTimer_Type()
)
wfRipIntfTimeoutTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfTimeoutTimer.setStatus("mandatory")


class _WfRipIntfHolddownTimer_Type(Integer32):
    """Custom type wfRipIntfHolddownTimer based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 3628800),
    )


_WfRipIntfHolddownTimer_Type.__name__ = "Integer32"
_WfRipIntfHolddownTimer_Object = MibTableColumn
wfRipIntfHolddownTimer = _WfRipIntfHolddownTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 14),
    _WfRipIntfHolddownTimer_Type()
)
wfRipIntfHolddownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfHolddownTimer.setStatus("mandatory")


class _WfRipIntfCompSwitch_Type(Integer32):
    """Custom type wfRipIntfCompSwitch based on Integer32"""
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
        *(("aggr", 3),
          ("rip1", 1),
          ("rip2", 2))
    )


_WfRipIntfCompSwitch_Type.__name__ = "Integer32"
_WfRipIntfCompSwitch_Object = MibTableColumn
wfRipIntfCompSwitch = _WfRipIntfCompSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 15),
    _WfRipIntfCompSwitch_Type()
)
wfRipIntfCompSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfCompSwitch.setStatus("mandatory")


class _WfRipIntfTriggeredUpdates_Type(Integer32):
    """Custom type wfRipIntfTriggeredUpdates based on Integer32"""
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


_WfRipIntfTriggeredUpdates_Type.__name__ = "Integer32"
_WfRipIntfTriggeredUpdates_Object = MibTableColumn
wfRipIntfTriggeredUpdates = _WfRipIntfTriggeredUpdates_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 16),
    _WfRipIntfTriggeredUpdates_Type()
)
wfRipIntfTriggeredUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfTriggeredUpdates.setStatus("mandatory")


class _WfRipIntfAuthType_Type(Integer32):
    """Custom type wfRipIntfAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("simple-password", 2))
    )


_WfRipIntfAuthType_Type.__name__ = "Integer32"
_WfRipIntfAuthType_Object = MibTableColumn
wfRipIntfAuthType = _WfRipIntfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 17),
    _WfRipIntfAuthType_Type()
)
wfRipIntfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfAuthType.setStatus("mandatory")


class _WfRipIntfAuthentication_Type(DisplayString):
    """Custom type wfRipIntfAuthentication based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_WfRipIntfAuthentication_Type.__name__ = "DisplayString"
_WfRipIntfAuthentication_Object = MibTableColumn
wfRipIntfAuthentication = _WfRipIntfAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 18),
    _WfRipIntfAuthentication_Type()
)
wfRipIntfAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfAuthentication.setStatus("mandatory")


class _WfRipIntfInitStabilizationTimer_Type(Integer32):
    """Custom type wfRipIntfInitStabilizationTimer based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_WfRipIntfInitStabilizationTimer_Type.__name__ = "Integer32"
_WfRipIntfInitStabilizationTimer_Object = MibTableColumn
wfRipIntfInitStabilizationTimer = _WfRipIntfInitStabilizationTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 19),
    _WfRipIntfInitStabilizationTimer_Type()
)
wfRipIntfInitStabilizationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfInitStabilizationTimer.setStatus("mandatory")


class _WfRipIntfSVCBroadcast_Type(Integer32):
    """Custom type wfRipIntfSVCBroadcast based on Integer32"""
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


_WfRipIntfSVCBroadcast_Type.__name__ = "Integer32"
_WfRipIntfSVCBroadcast_Object = MibTableColumn
wfRipIntfSVCBroadcast = _WfRipIntfSVCBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 20),
    _WfRipIntfSVCBroadcast_Type()
)
wfRipIntfSVCBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfSVCBroadcast.setStatus("mandatory")


class _WfRipIntfDefaultRouteCost_Type(Integer32):
    """Custom type wfRipIntfDefaultRouteCost based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_WfRipIntfDefaultRouteCost_Type.__name__ = "Integer32"
_WfRipIntfDefaultRouteCost_Object = MibTableColumn
wfRipIntfDefaultRouteCost = _WfRipIntfDefaultRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 2, 2, 2, 1, 21),
    _WfRipIntfDefaultRouteCost_Type()
)
wfRipIntfDefaultRouteCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRipIntfDefaultRouteCost.setStatus("mandatory")
_WfUdp_ObjectIdentity = ObjectIdentity
wfUdp = _WfUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 1)
)
_WfUdpInDatagrams_Type = Counter32
_WfUdpInDatagrams_Object = MibScalar
wfUdpInDatagrams = _WfUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 1, 1),
    _WfUdpInDatagrams_Type()
)
wfUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpInDatagrams.setStatus("mandatory")
_WfUdpNoPorts_Type = Counter32
_WfUdpNoPorts_Object = MibScalar
wfUdpNoPorts = _WfUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 1, 2),
    _WfUdpNoPorts_Type()
)
wfUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpNoPorts.setStatus("mandatory")
_WfUdpInErrors_Type = Counter32
_WfUdpInErrors_Object = MibScalar
wfUdpInErrors = _WfUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 1, 3),
    _WfUdpInErrors_Type()
)
wfUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpInErrors.setStatus("mandatory")
_WfUdpOutDatagrams_Type = Counter32
_WfUdpOutDatagrams_Object = MibScalar
wfUdpOutDatagrams = _WfUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 1, 4),
    _WfUdpOutDatagrams_Type()
)
wfUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpOutDatagrams.setStatus("mandatory")
_WfUdpTable_Object = MibTable
wfUdpTable = _WfUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 2)
)
if mibBuilder.loadTexts:
    wfUdpTable.setStatus("mandatory")
_WfUdpEntry_Object = MibTableRow
wfUdpEntry = _WfUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 2, 1)
)
wfUdpEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfUdpLocalAddress"),
    (0, "Wellfleet-IP-MIB", "wfUdpLocalPort"),
)
if mibBuilder.loadTexts:
    wfUdpEntry.setStatus("mandatory")
_WfUdpLocalAddress_Type = IpAddress
_WfUdpLocalAddress_Object = MibTableColumn
wfUdpLocalAddress = _WfUdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 2, 1, 1),
    _WfUdpLocalAddress_Type()
)
wfUdpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpLocalAddress.setStatus("mandatory")
_WfUdpLocalPort_Type = Integer32
_WfUdpLocalPort_Object = MibTableColumn
wfUdpLocalPort = _WfUdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 2, 1, 2),
    _WfUdpLocalPort_Type()
)
wfUdpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpLocalPort.setStatus("mandatory")
_WfUdpMpr_ObjectIdentity = ObjectIdentity
wfUdpMpr = _WfUdpMpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3)
)


class _WfUdpMprCreate_Type(Integer32):
    """Custom type wfUdpMprCreate based on Integer32"""
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


_WfUdpMprCreate_Type.__name__ = "Integer32"
_WfUdpMprCreate_Object = MibScalar
wfUdpMprCreate = _WfUdpMprCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 1),
    _WfUdpMprCreate_Type()
)
wfUdpMprCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprCreate.setStatus("mandatory")


class _WfUdpMprEnable_Type(Integer32):
    """Custom type wfUdpMprEnable based on Integer32"""
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


_WfUdpMprEnable_Type.__name__ = "Integer32"
_WfUdpMprEnable_Object = MibScalar
wfUdpMprEnable = _WfUdpMprEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 2),
    _WfUdpMprEnable_Type()
)
wfUdpMprEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprEnable.setStatus("mandatory")


class _WfUdpMprStartPort_Type(Integer32):
    """Custom type wfUdpMprStartPort based on Integer32"""
    defaultValue = 50000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(10000,
              50000,
              60000)
        )
    )
    namedValues = NamedValues(
        *(("default", 50000),
          ("maximum", 60000),
          ("minumum", 10000))
    )


_WfUdpMprStartPort_Type.__name__ = "Integer32"
_WfUdpMprStartPort_Object = MibScalar
wfUdpMprStartPort = _WfUdpMprStartPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 3),
    _WfUdpMprStartPort_Type()
)
wfUdpMprStartPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprStartPort.setStatus("mandatory")


class _WfUdpMprNumberOfPorts_Type(Integer32):
    """Custom type wfUdpMprNumberOfPorts based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(64,
              256)
        )
    )
    namedValues = NamedValues(
        *(("default", 64),
          ("maximum", 256))
    )


_WfUdpMprNumberOfPorts_Type.__name__ = "Integer32"
_WfUdpMprNumberOfPorts_Object = MibScalar
wfUdpMprNumberOfPorts = _WfUdpMprNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 4),
    _WfUdpMprNumberOfPorts_Type()
)
wfUdpMprNumberOfPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprNumberOfPorts.setStatus("mandatory")


class _WfUdpMprStatisticsEnable_Type(Integer32):
    """Custom type wfUdpMprStatisticsEnable based on Integer32"""
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


_WfUdpMprStatisticsEnable_Type.__name__ = "Integer32"
_WfUdpMprStatisticsEnable_Object = MibScalar
wfUdpMprStatisticsEnable = _WfUdpMprStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 5),
    _WfUdpMprStatisticsEnable_Type()
)
wfUdpMprStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprStatisticsEnable.setStatus("mandatory")
_WfUdpMprInPkts_Type = Counter32
_WfUdpMprInPkts_Object = MibScalar
wfUdpMprInPkts = _WfUdpMprInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 6),
    _WfUdpMprInPkts_Type()
)
wfUdpMprInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprInPkts.setStatus("mandatory")
_WfUdpMprOutPkts_Type = Counter32
_WfUdpMprOutPkts_Object = MibScalar
wfUdpMprOutPkts = _WfUdpMprOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 7),
    _WfUdpMprOutPkts_Type()
)
wfUdpMprOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprOutPkts.setStatus("mandatory")
_WfUdpMprGenPkts_Type = Counter32
_WfUdpMprGenPkts_Object = MibScalar
wfUdpMprGenPkts = _WfUdpMprGenPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 8),
    _WfUdpMprGenPkts_Type()
)
wfUdpMprGenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprGenPkts.setStatus("mandatory")
_WfUdpMprLookupDrops_Type = Counter32
_WfUdpMprLookupDrops_Object = MibScalar
wfUdpMprLookupDrops = _WfUdpMprLookupDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 9),
    _WfUdpMprLookupDrops_Type()
)
wfUdpMprLookupDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprLookupDrops.setStatus("mandatory")
_WfUdpMprDisableDrops_Type = Counter32
_WfUdpMprDisableDrops_Object = MibScalar
wfUdpMprDisableDrops = _WfUdpMprDisableDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 3, 10),
    _WfUdpMprDisableDrops_Type()
)
wfUdpMprDisableDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprDisableDrops.setStatus("mandatory")
_WfUdpMprMappingTable_Object = MibTable
wfUdpMprMappingTable = _WfUdpMprMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4)
)
if mibBuilder.loadTexts:
    wfUdpMprMappingTable.setStatus("mandatory")
_WfUdpMprMappingEntry_Object = MibTableRow
wfUdpMprMappingEntry = _WfUdpMprMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1)
)
wfUdpMprMappingEntry.setIndexNames(
    (0, "Wellfleet-IP-MIB", "wfUdpMprMapPort"),
)
if mibBuilder.loadTexts:
    wfUdpMprMappingEntry.setStatus("mandatory")


class _WfUdpMprMapCreate_Type(Integer32):
    """Custom type wfUdpMprMapCreate based on Integer32"""
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


_WfUdpMprMapCreate_Type.__name__ = "Integer32"
_WfUdpMprMapCreate_Object = MibTableColumn
wfUdpMprMapCreate = _WfUdpMprMapCreate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 1),
    _WfUdpMprMapCreate_Type()
)
wfUdpMprMapCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprMapCreate.setStatus("mandatory")


class _WfUdpMprMapEnable_Type(Integer32):
    """Custom type wfUdpMprMapEnable based on Integer32"""
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


_WfUdpMprMapEnable_Type.__name__ = "Integer32"
_WfUdpMprMapEnable_Object = MibTableColumn
wfUdpMprMapEnable = _WfUdpMprMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 2),
    _WfUdpMprMapEnable_Type()
)
wfUdpMprMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprMapEnable.setStatus("mandatory")
_WfUdpMprMapPort_Type = Integer32
_WfUdpMprMapPort_Object = MibTableColumn
wfUdpMprMapPort = _WfUdpMprMapPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 3),
    _WfUdpMprMapPort_Type()
)
wfUdpMprMapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprMapPort.setStatus("mandatory")
_WfUdpMprMapMcastAddr_Type = IpAddress
_WfUdpMprMapMcastAddr_Object = MibTableColumn
wfUdpMprMapMcastAddr = _WfUdpMprMapMcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 4),
    _WfUdpMprMapMcastAddr_Type()
)
wfUdpMprMapMcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprMapMcastAddr.setStatus("mandatory")


class _WfUdpMprMapStatisticsEnable_Type(Integer32):
    """Custom type wfUdpMprMapStatisticsEnable based on Integer32"""
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


_WfUdpMprMapStatisticsEnable_Type.__name__ = "Integer32"
_WfUdpMprMapStatisticsEnable_Object = MibTableColumn
wfUdpMprMapStatisticsEnable = _WfUdpMprMapStatisticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 5),
    _WfUdpMprMapStatisticsEnable_Type()
)
wfUdpMprMapStatisticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfUdpMprMapStatisticsEnable.setStatus("mandatory")
_WfUdpMprMapInPkts_Type = Counter32
_WfUdpMprMapInPkts_Object = MibTableColumn
wfUdpMprMapInPkts = _WfUdpMprMapInPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 6),
    _WfUdpMprMapInPkts_Type()
)
wfUdpMprMapInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprMapInPkts.setStatus("mandatory")
_WfUdpMprMapOutPkts_Type = Counter32
_WfUdpMprMapOutPkts_Object = MibTableColumn
wfUdpMprMapOutPkts = _WfUdpMprMapOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 7),
    _WfUdpMprMapOutPkts_Type()
)
wfUdpMprMapOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprMapOutPkts.setStatus("mandatory")
_WfUdpMprMapGenPkts_Type = Counter32
_WfUdpMprMapGenPkts_Object = MibTableColumn
wfUdpMprMapGenPkts = _WfUdpMprMapGenPkts_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 8),
    _WfUdpMprMapGenPkts_Type()
)
wfUdpMprMapGenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprMapGenPkts.setStatus("mandatory")
_WfUdpMprMapLookupDrops_Type = Counter32
_WfUdpMprMapLookupDrops_Object = MibTableColumn
wfUdpMprMapLookupDrops = _WfUdpMprMapLookupDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 9),
    _WfUdpMprMapLookupDrops_Type()
)
wfUdpMprMapLookupDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprMapLookupDrops.setStatus("mandatory")
_WfUdpMprMapDisableDrops_Type = Counter32
_WfUdpMprMapDisableDrops_Object = MibTableColumn
wfUdpMprMapDisableDrops = _WfUdpMprMapDisableDrops_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 4, 4, 1, 10),
    _WfUdpMprMapDisableDrops_Type()
)
wfUdpMprMapDisableDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUdpMprMapDisableDrops.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-IP-MIB",
    **{"wfIpBase": wfIpBase,
       "wfIpBaseCreate": wfIpBaseCreate,
       "wfIpBaseEnable": wfIpBaseEnable,
       "wfIpBaseState": wfIpBaseState,
       "wfIpBaseForwarding": wfIpBaseForwarding,
       "wfIpBaseDefaultTTL": wfIpBaseDefaultTTL,
       "wfIpBaseRipDiameter": wfIpBaseRipDiameter,
       "wfIpBaseRouteCache": wfIpBaseRouteCache,
       "wfIpBaseMibTables": wfIpBaseMibTables,
       "wfIpBaseNetworks": wfIpBaseNetworks,
       "wfIpBaseZeroSubnetEnable": wfIpBaseZeroSubnetEnable,
       "wfIpBaseEstimatedNetworks": wfIpBaseEstimatedNetworks,
       "wfIpBaseHosts": wfIpBaseHosts,
       "wfIpBaseEstimatedHosts": wfIpBaseEstimatedHosts,
       "wfIpBaseDefaultOverSubnetEnable": wfIpBaseDefaultOverSubnetEnable,
       "wfIpBaseMaxPolicyRules": wfIpBaseMaxPolicyRules,
       "wfIpBaseRouteFilterSupport": wfIpBaseRouteFilterSupport,
       "wfRipMaximumPath": wfRipMaximumPath,
       "wfIpMultipathMethod": wfIpMultipathMethod,
       "wfIpBaseIspMode": wfIpBaseIspMode,
       "wfIpBaseExtendedTrafficFilterSupport": wfIpBaseExtendedTrafficFilterSupport,
       "wfIpOspfMaximumPath": wfIpOspfMaximumPath,
       "wfIpBaseIcmpErrorLimit": wfIpBaseIcmpErrorLimit,
       "wfIpBaseIbgpEcmp": wfIpBaseIbgpEcmp,
       "wfIpBaseRtbBalanceInterval": wfIpBaseRtbBalanceInterval,
       "wfIpBaseRtblP1": wfIpBaseRtblP1,
       "wfIpBaseRtblP2": wfIpBaseRtblP2,
       "wfIpBaseArpBufLimitPrcnt": wfIpBaseArpBufLimitPrcnt,
       "wfIpBaseDirectedBcastEnable": wfIpBaseDirectedBcastEnable,
       "wfIpBaseHostOnlyRip": wfIpBaseHostOnlyRip,
       "wfIpBaseBlockSRR": wfIpBaseBlockSRR,
       "wfIpBaseRtEntryTable": wfIpBaseRtEntryTable,
       "wfIpBaseRtEntry": wfIpBaseRtEntry,
       "wfIpBaseRouteDest": wfIpBaseRouteDest,
       "wfIpBaseRouteIfIndex": wfIpBaseRouteIfIndex,
       "wfIpBaseRouteMetric1": wfIpBaseRouteMetric1,
       "wfIpBaseRouteMetric2": wfIpBaseRouteMetric2,
       "wfIpBaseRouteMetric3": wfIpBaseRouteMetric3,
       "wfIpBaseRouteMetric4": wfIpBaseRouteMetric4,
       "wfIpBaseRouteNextHop": wfIpBaseRouteNextHop,
       "wfIpBaseRouteType": wfIpBaseRouteType,
       "wfIpBaseRouteProto": wfIpBaseRouteProto,
       "wfIpBaseRouteAge": wfIpBaseRouteAge,
       "wfIpBaseRouteMask": wfIpBaseRouteMask,
       "wfIpBaseRouteMetric5": wfIpBaseRouteMetric5,
       "wfIpBaseRouteInfo": wfIpBaseRouteInfo,
       "wfIpBaseHostEntryTable": wfIpBaseHostEntryTable,
       "wfIpBaseHostEntry": wfIpBaseHostEntry,
       "wfIpBaseNetToMediaIfIndex": wfIpBaseNetToMediaIfIndex,
       "wfIpBaseNetToMediaPhysAddress": wfIpBaseNetToMediaPhysAddress,
       "wfIpBaseNetToMediaNetAddress": wfIpBaseNetToMediaNetAddress,
       "wfIpBaseNetToMediaType": wfIpBaseNetToMediaType,
       "wfIpInterfaceTable": wfIpInterfaceTable,
       "wfIpInterfaceEntry": wfIpInterfaceEntry,
       "wfIpInterfaceCreate": wfIpInterfaceCreate,
       "wfIpInterfaceEnable": wfIpInterfaceEnable,
       "wfIpInterfaceState": wfIpInterfaceState,
       "wfIpInterfaceAddr": wfIpInterfaceAddr,
       "wfIpInterfaceCircuit": wfIpInterfaceCircuit,
       "wfIpInterfaceMask": wfIpInterfaceMask,
       "wfIpInterfaceCost": wfIpInterfaceCost,
       "wfIpInterfaceCfgBcastAddr": wfIpInterfaceCfgBcastAddr,
       "wfIpInterfaceBcastAddr": wfIpInterfaceBcastAddr,
       "wfIpInterfaceMTUDiscovery": wfIpInterfaceMTUDiscovery,
       "wfIpInterfaceAMR": wfIpInterfaceAMR,
       "wfIpInterfaceASB": wfIpInterfaceASB,
       "wfIpInterfaceAddressResolutionType": wfIpInterfaceAddressResolutionType,
       "wfIpInterfaceProxy": wfIpInterfaceProxy,
       "wfIpInterfaceHostCache": wfIpInterfaceHostCache,
       "wfIpInterfaceUdpXsumOn": wfIpInterfaceUdpXsumOn,
       "wfIpInterfaceCfgMacAddress": wfIpInterfaceCfgMacAddress,
       "wfIpInterfaceMacAddress": wfIpInterfaceMacAddress,
       "wfIpInterfaceReasmMaxSize": wfIpInterfaceReasmMaxSize,
       "wfIpInterfaceMaxInfo": wfIpInterfaceMaxInfo,
       "wfIpInterfaceInReceives": wfIpInterfaceInReceives,
       "wfIpInterfaceInHdrErrors": wfIpInterfaceInHdrErrors,
       "wfIpInterfaceInAddrErrors": wfIpInterfaceInAddrErrors,
       "wfIpInterfaceForwDatagrams": wfIpInterfaceForwDatagrams,
       "wfIpInterfaceInUnknownProtos": wfIpInterfaceInUnknownProtos,
       "wfIpInterfaceInDiscards": wfIpInterfaceInDiscards,
       "wfIpInterfaceInDelivers": wfIpInterfaceInDelivers,
       "wfIpInterfaceOutRequests": wfIpInterfaceOutRequests,
       "wfIpInterfaceOutDiscards": wfIpInterfaceOutDiscards,
       "wfIpInterfaceOutNoRoutes": wfIpInterfaceOutNoRoutes,
       "wfIpInterfaceReasmTimeout": wfIpInterfaceReasmTimeout,
       "wfIpInterfaceReasmReqds": wfIpInterfaceReasmReqds,
       "wfIpInterfaceReasmOKs": wfIpInterfaceReasmOKs,
       "wfIpInterfaceReasmFails": wfIpInterfaceReasmFails,
       "wfIpInterfaceFragOKs": wfIpInterfaceFragOKs,
       "wfIpInterfaceFragFails": wfIpInterfaceFragFails,
       "wfIpInterfaceFragCreates": wfIpInterfaceFragCreates,
       "wfIpInterfaceIcmpInMsgs": wfIpInterfaceIcmpInMsgs,
       "wfIpInterfaceIcmpInErrors": wfIpInterfaceIcmpInErrors,
       "wfIpInterfaceIcmpInDestUnreachs": wfIpInterfaceIcmpInDestUnreachs,
       "wfIpInterfaceIcmpInTimeExcds": wfIpInterfaceIcmpInTimeExcds,
       "wfIpInterfaceIcmpInParmProbs": wfIpInterfaceIcmpInParmProbs,
       "wfIpInterfaceIcmpInSrcQuenchs": wfIpInterfaceIcmpInSrcQuenchs,
       "wfIpInterfaceIcmpInRedirects": wfIpInterfaceIcmpInRedirects,
       "wfIpInterfaceIcmpInEchos": wfIpInterfaceIcmpInEchos,
       "wfIpInterfaceIcmpInEchoReps": wfIpInterfaceIcmpInEchoReps,
       "wfIpInterfaceIcmpInTimestamps": wfIpInterfaceIcmpInTimestamps,
       "wfIpInterfaceIcmpInTimestampReps": wfIpInterfaceIcmpInTimestampReps,
       "wfIpInterfaceIcmpInAddrMasks": wfIpInterfaceIcmpInAddrMasks,
       "wfIpInterfaceIcmpInAddrMaskReps": wfIpInterfaceIcmpInAddrMaskReps,
       "wfIpInterfaceIcmpOutMsgs": wfIpInterfaceIcmpOutMsgs,
       "wfIpInterfaceIcmpOutErrors": wfIpInterfaceIcmpOutErrors,
       "wfIpInterfaceIcmpOutDestUnreachs": wfIpInterfaceIcmpOutDestUnreachs,
       "wfIpInterfaceIcmpOutTimeExcds": wfIpInterfaceIcmpOutTimeExcds,
       "wfIpInterfaceIcmpOutParmProbs": wfIpInterfaceIcmpOutParmProbs,
       "wfIpInterfaceIcmpOutSrcQuenchs": wfIpInterfaceIcmpOutSrcQuenchs,
       "wfIpInterfaceIcmpOutRedirects": wfIpInterfaceIcmpOutRedirects,
       "wfIpInterfaceIcmpOutEchos": wfIpInterfaceIcmpOutEchos,
       "wfIpInterfaceIcmpOutEchoReps": wfIpInterfaceIcmpOutEchoReps,
       "wfIpInterfaceIcmpOutTimestamps": wfIpInterfaceIcmpOutTimestamps,
       "wfIpInterfaceIcmpOutTimestampReps": wfIpInterfaceIcmpOutTimestampReps,
       "wfIpInterfaceIcmpOutAddrMasks": wfIpInterfaceIcmpOutAddrMasks,
       "wfIpInterfaceIcmpOutAddrMaskReps": wfIpInterfaceIcmpOutAddrMaskReps,
       "wfIpInterfaceTrEndStation": wfIpInterfaceTrEndStation,
       "wfIpInterfaceSMDSGroupAddress": wfIpInterfaceSMDSGroupAddress,
       "wfIpInterfaceSMDSArpReqAddress": wfIpInterfaceSMDSArpReqAddress,
       "wfIpInterfaceFRBcastDlci": wfIpInterfaceFRBcastDlci,
       "wfIpInterfaceFRMcast1Dlci": wfIpInterfaceFRMcast1Dlci,
       "wfIpInterfaceFRMcast2Dlci": wfIpInterfaceFRMcast2Dlci,
       "wfIpInterfaceRedirect": wfIpInterfaceRedirect,
       "wfIpInterfaceEnetArpEncaps": wfIpInterfaceEnetArpEncaps,
       "wfIpInterfaceCacheMisses": wfIpInterfaceCacheMisses,
       "wfIpInterfaceCacheNetworks": wfIpInterfaceCacheNetworks,
       "wfIpInterfaceCacheRemoves": wfIpInterfaceCacheRemoves,
       "wfIpInterfaceSlotMask": wfIpInterfaceSlotMask,
       "wfIpInterfaceEnableSecurity": wfIpInterfaceEnableSecurity,
       "wfIpInterfaceStripSecurity": wfIpInterfaceStripSecurity,
       "wfIpInterfaceRequireOutSecurity": wfIpInterfaceRequireOutSecurity,
       "wfIpInterfaceRequireInSecurity": wfIpInterfaceRequireInSecurity,
       "wfIpInterfaceMinLevel": wfIpInterfaceMinLevel,
       "wfIpInterfaceMaxLevel": wfIpInterfaceMaxLevel,
       "wfIpInterfaceMustOutAuthority": wfIpInterfaceMustOutAuthority,
       "wfIpInterfaceMayOutAuthority": wfIpInterfaceMayOutAuthority,
       "wfIpInterfaceMustInAuthority": wfIpInterfaceMustInAuthority,
       "wfIpInterfaceMayInAuthority": wfIpInterfaceMayInAuthority,
       "wfIpInterfaceImplicitLabelEnabled": wfIpInterfaceImplicitLabelEnabled,
       "wfIpInterfaceImplicitAuth": wfIpInterfaceImplicitAuth,
       "wfIpInterfaceImplicitLevel": wfIpInterfaceImplicitLevel,
       "wfIpInterfaceDefaultLabelEnabled": wfIpInterfaceDefaultLabelEnabled,
       "wfIpInterfaceDefaultAuth": wfIpInterfaceDefaultAuth,
       "wfIpInterfaceDefaultLevel": wfIpInterfaceDefaultLevel,
       "wfIpInterfaceErrorLabelEnabled": wfIpInterfaceErrorLabelEnabled,
       "wfIpInterfaceErrorAuth": wfIpInterfaceErrorAuth,
       "wfIpInterfaceDropRxAuths": wfIpInterfaceDropRxAuths,
       "wfIpInterfaceDropRxFormats": wfIpInterfaceDropRxFormats,
       "wfIpInterfaceDropRxLevels": wfIpInterfaceDropRxLevels,
       "wfIpInterfaceDropRxNoIpsos": wfIpInterfaceDropRxNoIpsos,
       "wfIpInterfaceDropTxAuths": wfIpInterfaceDropTxAuths,
       "wfIpInterfaceDropTxLevels": wfIpInterfaceDropTxLevels,
       "wfIpInterfaceDropTxNoIpsos": wfIpInterfaceDropTxNoIpsos,
       "wfIpInterfaceDropTxNoIpsoRooms": wfIpInterfaceDropTxNoIpsoRooms,
       "wfIpInterfaceICMPInAdminProhib": wfIpInterfaceICMPInAdminProhib,
       "wfIpInterfaceICMPOutAdminProhib": wfIpInterfaceICMPOutAdminProhib,
       "wfIpInterfaceFwdCacheSize": wfIpInterfaceFwdCacheSize,
       "wfIpInterfaceTunnelInfo": wfIpInterfaceTunnelInfo,
       "wfIpInterfaceIcmpInRdiscSolicit": wfIpInterfaceIcmpInRdiscSolicit,
       "wfIpInterfaceIcmpInRdiscAdvert": wfIpInterfaceIcmpInRdiscAdvert,
       "wfIpInterfaceIcmpOutRdiscAdvert": wfIpInterfaceIcmpOutRdiscAdvert,
       "wfIpInterfaceRoutingDiscards": wfIpInterfaceRoutingDiscards,
       "wfIpInterfaceUnnumAssocAddr": wfIpInterfaceUnnumAssocAddr,
       "wfIpInterfaceUnnumAssocAlt": wfIpInterfaceUnnumAssocAlt,
       "wfIpInterfaceAtmArpMode": wfIpInterfaceAtmArpMode,
       "wfIpInterfaceAtmArpServerAddress": wfIpInterfaceAtmArpServerAddress,
       "wfIpInterfaceAtmArpServerVcAgingEnable": wfIpInterfaceAtmArpServerVcAgingEnable,
       "wfIpInterfaceAtmArpServerRegInterval": wfIpInterfaceAtmArpServerRegInterval,
       "wfIpInterfaceAtmArpServerConnState": wfIpInterfaceAtmArpServerConnState,
       "wfIpInterfaceAtmArpAttemptedCalls": wfIpInterfaceAtmArpAttemptedCalls,
       "wfIpInterfaceAtmArpFailRetryCalls": wfIpInterfaceAtmArpFailRetryCalls,
       "wfIpInterfaceAtmArpFailNoRetryCalls": wfIpInterfaceAtmArpFailNoRetryCalls,
       "wfIpInterfaceAtmArpSuccessfulCalls": wfIpInterfaceAtmArpSuccessfulCalls,
       "wfIpInterfaceAtmArpAcceptedCalls": wfIpInterfaceAtmArpAcceptedCalls,
       "wfIpInterfaceAtmArpOpenSvcs": wfIpInterfaceAtmArpOpenSvcs,
       "wfIpInterfaceAtmArpMisc": wfIpInterfaceAtmArpMisc,
       "wfIpInterfaceAtmArpMisc2": wfIpInterfaceAtmArpMisc2,
       "wfIpInterfaceMcastInPkts": wfIpInterfaceMcastInPkts,
       "wfIpInterfaceMcastOutPkts": wfIpInterfaceMcastOutPkts,
       "wfIpInterfaceTrEsArpType": wfIpInterfaceTrEsArpType,
       "wfIpStaticRouteTable": wfIpStaticRouteTable,
       "wfIpStaticRouteEntry": wfIpStaticRouteEntry,
       "wfIpSrCreate": wfIpSrCreate,
       "wfIpSrEnable": wfIpSrEnable,
       "wfIpSrIpAddress": wfIpSrIpAddress,
       "wfIpSrIpNetMask": wfIpSrIpNetMask,
       "wfIpSrCost": wfIpSrCost,
       "wfIpSrNextHopAddr": wfIpSrNextHopAddr,
       "wfIpSrNextHopMask": wfIpSrNextHopMask,
       "wfIpSrPreference": wfIpSrPreference,
       "wfIpSrIpAddressRt": wfIpSrIpAddressRt,
       "wfIpSrValid": wfIpSrValid,
       "wfIpSrUnnumCct": wfIpSrUnnumCct,
       "wfIpAdjacentHostTable": wfIpAdjacentHostTable,
       "wfIpAdjacentHostEntry": wfIpAdjacentHostEntry,
       "wfIpAdjHostCreate": wfIpAdjHostCreate,
       "wfIpAdjHostEnable": wfIpAdjHostEnable,
       "wfIpAdjHostIpAddress": wfIpAdjHostIpAddress,
       "wfIpAdjHostIntf": wfIpAdjHostIntf,
       "wfIpAdjHostIntfMask": wfIpAdjHostIntfMask,
       "wfIpAdjHostMacAddr": wfIpAdjHostMacAddr,
       "wfIpAdjHostEncaps": wfIpAdjHostEncaps,
       "wfIpAdjHostValid": wfIpAdjHostValid,
       "wfIpAdjHostX121Addr": wfIpAdjHostX121Addr,
       "wfIpAdjHostSubaddr": wfIpAdjHostSubaddr,
       "wfIpAdjHostTypeOfNumber": wfIpAdjHostTypeOfNumber,
       "wfIpAdjHostType": wfIpAdjHostType,
       "wfIpAdjHostGreConnName": wfIpAdjHostGreConnName,
       "wfIpTrafficFilterTable": wfIpTrafficFilterTable,
       "wfIpTrafficFilterEntry": wfIpTrafficFilterEntry,
       "wfIpTrafficFilterCreate": wfIpTrafficFilterCreate,
       "wfIpTrafficFilterEnable": wfIpTrafficFilterEnable,
       "wfIpTrafficFilterStatus": wfIpTrafficFilterStatus,
       "wfIpTrafficFilterCounter": wfIpTrafficFilterCounter,
       "wfIpTrafficFilterDefinition": wfIpTrafficFilterDefinition,
       "wfIpTrafficFilterReserved": wfIpTrafficFilterReserved,
       "wfIpTrafficFilterInterface": wfIpTrafficFilterInterface,
       "wfIpTrafficFilterCircuit": wfIpTrafficFilterCircuit,
       "wfIpTrafficFilterRuleNumber": wfIpTrafficFilterRuleNumber,
       "wfIpTrafficFilterFragment": wfIpTrafficFilterFragment,
       "wfIpTrafficFilterName": wfIpTrafficFilterName,
       "wfIpTrafficFilterPrecedence": wfIpTrafficFilterPrecedence,
       "wfIpTrafficFilterType": wfIpTrafficFilterType,
       "wfIpTrafficFilterDSOopCounter": wfIpTrafficFilterDSOopCounter,
       "wfIpTrafficFilterDSPrecedence": wfIpTrafficFilterDSPrecedence,
       "wfIpTrafficFilterDSBytes": wfIpTrafficFilterDSBytes,
       "wfIpTrafficFilterDSOopBytes": wfIpTrafficFilterDSOopBytes,
       "wfIpForwardTable": wfIpForwardTable,
       "wfIpForwardEntry": wfIpForwardEntry,
       "wfIpForwardDest": wfIpForwardDest,
       "wfIpForwardMask": wfIpForwardMask,
       "wfIpForwardPolicy": wfIpForwardPolicy,
       "wfIpForwardNextHop": wfIpForwardNextHop,
       "wfIpForwardIfIndex": wfIpForwardIfIndex,
       "wfIpForwardType": wfIpForwardType,
       "wfIpForwardProto": wfIpForwardProto,
       "wfIpForwardAge": wfIpForwardAge,
       "wfIpForwardInfo": wfIpForwardInfo,
       "wfIpForwardNextHopAS": wfIpForwardNextHopAS,
       "wfIpForwardMetric1": wfIpForwardMetric1,
       "wfIpForwardMetric2": wfIpForwardMetric2,
       "wfIpForwardMetric3": wfIpForwardMetric3,
       "wfIpForwardMetric4": wfIpForwardMetric4,
       "wfIpForwardMetric5": wfIpForwardMetric5,
       "wfRdiscIntfTable": wfRdiscIntfTable,
       "wfRdiscIntfEntry": wfRdiscIntfEntry,
       "wfRdiscInterfaceCreate": wfRdiscInterfaceCreate,
       "wfRdiscInterfaceEnable": wfRdiscInterfaceEnable,
       "wfRdiscInterfaceState": wfRdiscInterfaceState,
       "wfRdiscInterfaceIndex": wfRdiscInterfaceIndex,
       "wfRdiscInterfaceBcast": wfRdiscInterfaceBcast,
       "wfRdiscInterfaceMinIntrvl": wfRdiscInterfaceMinIntrvl,
       "wfRdiscInterfaceMaxIntrvl": wfRdiscInterfaceMaxIntrvl,
       "wfRdiscInterfaceLifetime": wfRdiscInterfaceLifetime,
       "wfRdiscInterfacePref": wfRdiscInterfacePref,
       "wfRdiscInterfaceUnicastAdvt": wfRdiscInterfaceUnicastAdvt,
       "wfRdiscInterfaceMulticastAdvt": wfRdiscInterfaceMulticastAdvt,
       "wfRdiscInterfaceDynamicPref": wfRdiscInterfaceDynamicPref,
       "wfIpNetToMediaEntryTable": wfIpNetToMediaEntryTable,
       "wfIpNetToMediaEntry": wfIpNetToMediaEntry,
       "wfIpNetToMediaIfIndex": wfIpNetToMediaIfIndex,
       "wfIpNetToMediaPhysAddress": wfIpNetToMediaPhysAddress,
       "wfIpNetToMediaNetAddress": wfIpNetToMediaNetAddress,
       "wfIpNetToMediaType": wfIpNetToMediaType,
       "wfIpAccCtrlFilterTable": wfIpAccCtrlFilterTable,
       "wfIpAccCtrlFilterEntry": wfIpAccCtrlFilterEntry,
       "wfIpAccCtrlFilterCreate": wfIpAccCtrlFilterCreate,
       "wfIpAccCtrlFilterEnable": wfIpAccCtrlFilterEnable,
       "wfIpAccCtrlFilterIndex": wfIpAccCtrlFilterIndex,
       "wfIpAccCtrlFilterName": wfIpAccCtrlFilterName,
       "wfIpAccCtrlFilterNetwork": wfIpAccCtrlFilterNetwork,
       "wfIpAccCtrlFilterNetworkMask": wfIpAccCtrlFilterNetworkMask,
       "wfIpAccCtrlFilterAction": wfIpAccCtrlFilterAction,
       "wfIpAccCtrlFilterServiceMask": wfIpAccCtrlFilterServiceMask,
       "wfIpAccCtrlFilterDenyLog": wfIpAccCtrlFilterDenyLog,
       "wfIpAccCtrlFilterPrecedence": wfIpAccCtrlFilterPrecedence,
       "wfIpAccCtrlFilterId": wfIpAccCtrlFilterId,
       "wfIpAccCtrlNetworkTable": wfIpAccCtrlNetworkTable,
       "wfIpAccCtrlNetworkEntry": wfIpAccCtrlNetworkEntry,
       "wfIpAccCtrlNetworkCreate": wfIpAccCtrlNetworkCreate,
       "wfIpAccCtrlNetworkEnable": wfIpAccCtrlNetworkEnable,
       "wfIpAccCtrlNetworkIndex": wfIpAccCtrlNetworkIndex,
       "wfIpAccCtrlNetworkNetwork": wfIpAccCtrlNetworkNetwork,
       "wfIpAccCtrlNetworkNetworkMask": wfIpAccCtrlNetworkNetworkMask,
       "wfIpAccCtrlNetworkId": wfIpAccCtrlNetworkId,
       "wfIpAccCtrlUserHostTable": wfIpAccCtrlUserHostTable,
       "wfIpAccCtrlUserHostEntry": wfIpAccCtrlUserHostEntry,
       "wfIpAccCtrlUserHostCreate": wfIpAccCtrlUserHostCreate,
       "wfIpAccCtrlUserHostEnable": wfIpAccCtrlUserHostEnable,
       "wfIpAccCtrlUserHostIndex": wfIpAccCtrlUserHostIndex,
       "wfIpAccCtrlUserHostUser": wfIpAccCtrlUserHostUser,
       "wfIpAccCtrlUserHostHost": wfIpAccCtrlUserHostHost,
       "wfIpAccCtrlUserHostId": wfIpAccCtrlUserHostId,
       "wfIpAddrTable": wfIpAddrTable,
       "wfIpAddrEntry": wfIpAddrEntry,
       "wfIpAdEntAddr": wfIpAdEntAddr,
       "wfIpAdEntIfIndex": wfIpAdEntIfIndex,
       "wfIpAdEntNetMask": wfIpAdEntNetMask,
       "wfIpAdEntBcastAddr": wfIpAdEntBcastAddr,
       "wfIpAdEntReasmMaxSize": wfIpAdEntReasmMaxSize,
       "wfIpInternalHostTable": wfIpInternalHostTable,
       "wfIpInternalHostEntry": wfIpInternalHostEntry,
       "wfIpInternHtIpAddress": wfIpInternHtIpAddress,
       "wfIpInternHtReceives": wfIpInternHtReceives,
       "wfIpInternHtInDelivers": wfIpInternHtInDelivers,
       "wfIpInternHtUnknownProtos": wfIpInternHtUnknownProtos,
       "wfIpInternHtReasmReqds": wfIpInternHtReasmReqds,
       "wfIpInternHtReasmFails": wfIpInternHtReasmFails,
       "wfIpInternHtReasmOKs": wfIpInternHtReasmOKs,
       "wfIpInternHtInHdrErrors": wfIpInternHtInHdrErrors,
       "wfIpIntfCfgTable": wfIpIntfCfgTable,
       "wfIpIntfCfgEntry": wfIpIntfCfgEntry,
       "wfIpIntfCfgCreate": wfIpIntfCfgCreate,
       "wfIpIntfCfgEnable": wfIpIntfCfgEnable,
       "wfIpIntfCfgState": wfIpIntfCfgState,
       "wfIpIntfCfgAddr": wfIpIntfCfgAddr,
       "wfIpIntfCfgCircuit": wfIpIntfCfgCircuit,
       "wfIpIntfCfgMask": wfIpIntfCfgMask,
       "wfIpIntfCfgCost": wfIpIntfCfgCost,
       "wfIpIntfCfgCfgBcastAddr": wfIpIntfCfgCfgBcastAddr,
       "wfIpIntfCfgBcastAddr": wfIpIntfCfgBcastAddr,
       "wfIpIntfCfgCfgMacAddress": wfIpIntfCfgCfgMacAddress,
       "wfIpIntfCfgMacAddress": wfIpIntfCfgMacAddress,
       "wfIpIntfCfgMTUDiscovery": wfIpIntfCfgMTUDiscovery,
       "wfIpIntfCfgAMR": wfIpIntfCfgAMR,
       "wfIpIntfCfgASB": wfIpIntfCfgASB,
       "wfIpIntfCfgAddressResolutionType": wfIpIntfCfgAddressResolutionType,
       "wfIpIntfCfgProxy": wfIpIntfCfgProxy,
       "wfIpIntfCfgHostCache": wfIpIntfCfgHostCache,
       "wfIpIntfCfgUdpXsumOn": wfIpIntfCfgUdpXsumOn,
       "wfIpIntfCfgTrEndStation": wfIpIntfCfgTrEndStation,
       "wfIpIntfCfgSMDSGroupAddress": wfIpIntfCfgSMDSGroupAddress,
       "wfIpIntfCfgSMDSArpReqAddress": wfIpIntfCfgSMDSArpReqAddress,
       "wfIpIntfCfgFRBcastDlci": wfIpIntfCfgFRBcastDlci,
       "wfIpIntfCfgFRMcast1Dlci": wfIpIntfCfgFRMcast1Dlci,
       "wfIpIntfCfgFRMcast2Dlci": wfIpIntfCfgFRMcast2Dlci,
       "wfIpIntfCfgRedirect": wfIpIntfCfgRedirect,
       "wfIpIntfCfgEnetArpEncaps": wfIpIntfCfgEnetArpEncaps,
       "wfIpIntfCfgSlotMask": wfIpIntfCfgSlotMask,
       "wfIpIntfCfgEnableSecurity": wfIpIntfCfgEnableSecurity,
       "wfIpIntfCfgStripSecurity": wfIpIntfCfgStripSecurity,
       "wfIpIntfCfgRequireOutSecurity": wfIpIntfCfgRequireOutSecurity,
       "wfIpIntfCfgRequireInSecurity": wfIpIntfCfgRequireInSecurity,
       "wfIpIntfCfgMinLevel": wfIpIntfCfgMinLevel,
       "wfIpIntfCfgMaxLevel": wfIpIntfCfgMaxLevel,
       "wfIpIntfCfgMustOutAuthority": wfIpIntfCfgMustOutAuthority,
       "wfIpIntfCfgMayOutAuthority": wfIpIntfCfgMayOutAuthority,
       "wfIpIntfCfgMustInAuthority": wfIpIntfCfgMustInAuthority,
       "wfIpIntfCfgMayInAuthority": wfIpIntfCfgMayInAuthority,
       "wfIpIntfCfgImplicitLabelEnabled": wfIpIntfCfgImplicitLabelEnabled,
       "wfIpIntfCfgImplicitAuth": wfIpIntfCfgImplicitAuth,
       "wfIpIntfCfgImplicitLevel": wfIpIntfCfgImplicitLevel,
       "wfIpIntfCfgDefaultLabelEnabled": wfIpIntfCfgDefaultLabelEnabled,
       "wfIpIntfCfgDefaultAuth": wfIpIntfCfgDefaultAuth,
       "wfIpIntfCfgDefaultLevel": wfIpIntfCfgDefaultLevel,
       "wfIpIntfCfgErrorLabelEnabled": wfIpIntfCfgErrorLabelEnabled,
       "wfIpIntfCfgErrorAuth": wfIpIntfCfgErrorAuth,
       "wfIpIntfCfgFwdCacheSize": wfIpIntfCfgFwdCacheSize,
       "wfIpIntfCfgUnnumAsocAddr": wfIpIntfCfgUnnumAsocAddr,
       "wfIpIntfCfgUnnumAsocAlt": wfIpIntfCfgUnnumAsocAlt,
       "wfIpIntfCfgAtmArpMode": wfIpIntfCfgAtmArpMode,
       "wfIpIntfCfgAtmArpSrvAddress": wfIpIntfCfgAtmArpSrvAddress,
       "wfIpIntfCfgAtmArpSrvVcAgingEnable": wfIpIntfCfgAtmArpSrvVcAgingEnable,
       "wfIpIntfCfgAtmArpSrvRegInterval": wfIpIntfCfgAtmArpSrvRegInterval,
       "wfIpIntfCfgAtmArpMisc": wfIpIntfCfgAtmArpMisc,
       "wfIpIntfCfgAtmArpMisc2": wfIpIntfCfgAtmArpMisc2,
       "wfIpIntfCfgAtmArpSrvConnState": wfIpIntfCfgAtmArpSrvConnState,
       "wfIpIntfCfgTrEsArpType": wfIpIntfCfgTrEsArpType,
       "wfIpIntfCfgMprMode": wfIpIntfCfgMprMode,
       "wfIpIntfCfgMprState": wfIpIntfCfgMprState,
       "wfIpIntfCfgIPSecEnable": wfIpIntfCfgIPSecEnable,
       "wfIpIntfCfgIPSecLogLevel": wfIpIntfCfgIPSecLogLevel,
       "wfIpIntfCfgTosTemplate": wfIpIntfCfgTosTemplate,
       "wfIpIntfCfgMsgLevel": wfIpIntfCfgMsgLevel,
       "wfIpIntfCfgMtu": wfIpIntfCfgMtu,
       "wfIpIntfCfgDropIpMacBroadcast": wfIpIntfCfgDropIpMacBroadcast,
       "wfIpIntfStatsTable": wfIpIntfStatsTable,
       "wfIpIntfStatsEntry": wfIpIntfStatsEntry,
       "wfIpIntfStatsAddr": wfIpIntfStatsAddr,
       "wfIpIntfStatsCircuit": wfIpIntfStatsCircuit,
       "wfIpIntfStatsReasmMaxSize": wfIpIntfStatsReasmMaxSize,
       "wfIpIntfStatsMaxInfo": wfIpIntfStatsMaxInfo,
       "wfIpIntfStatsInReceives": wfIpIntfStatsInReceives,
       "wfIpIntfStatsInHdrErrors": wfIpIntfStatsInHdrErrors,
       "wfIpIntfStatsInAddrErrors": wfIpIntfStatsInAddrErrors,
       "wfIpIntfStatsForwDatagrams": wfIpIntfStatsForwDatagrams,
       "wfIpIntfStatsInUnknownProtos": wfIpIntfStatsInUnknownProtos,
       "wfIpIntfStatsInDiscards": wfIpIntfStatsInDiscards,
       "wfIpIntfStatsInDelivers": wfIpIntfStatsInDelivers,
       "wfIpIntfStatsOutRequests": wfIpIntfStatsOutRequests,
       "wfIpIntfStatsOutDiscards": wfIpIntfStatsOutDiscards,
       "wfIpIntfStatsOutNoRoutes": wfIpIntfStatsOutNoRoutes,
       "wfIpIntfStatsReasmTimeout": wfIpIntfStatsReasmTimeout,
       "wfIpIntfStatsReasmReqds": wfIpIntfStatsReasmReqds,
       "wfIpIntfStatsReasmOKs": wfIpIntfStatsReasmOKs,
       "wfIpIntfStatsReasmFails": wfIpIntfStatsReasmFails,
       "wfIpIntfStatsFragOKs": wfIpIntfStatsFragOKs,
       "wfIpIntfStatsFragFails": wfIpIntfStatsFragFails,
       "wfIpIntfStatsFragCreates": wfIpIntfStatsFragCreates,
       "wfIpIntfStatsCacheMisses": wfIpIntfStatsCacheMisses,
       "wfIpIntfStatsCacheNetworks": wfIpIntfStatsCacheNetworks,
       "wfIpIntfStatsCacheRemoves": wfIpIntfStatsCacheRemoves,
       "wfIpIntfStatsDropRxAuths": wfIpIntfStatsDropRxAuths,
       "wfIpIntfStatsDropRxFormats": wfIpIntfStatsDropRxFormats,
       "wfIpIntfStatsDropRxLevels": wfIpIntfStatsDropRxLevels,
       "wfIpIntfStatsDropRxNoIpsos": wfIpIntfStatsDropRxNoIpsos,
       "wfIpIntfStatsDropTxAuths": wfIpIntfStatsDropTxAuths,
       "wfIpIntfStatsDropTxLevels": wfIpIntfStatsDropTxLevels,
       "wfIpIntfStatsDropTxNoIpsos": wfIpIntfStatsDropTxNoIpsos,
       "wfIpIntfStatsDropTxNoIpsoRooms": wfIpIntfStatsDropTxNoIpsoRooms,
       "wfIpIntfStatsRoutingDiscards": wfIpIntfStatsRoutingDiscards,
       "wfIpIntfStatsAtmArpAttemptedCalls": wfIpIntfStatsAtmArpAttemptedCalls,
       "wfIpIntfStatsAtmArpFailRetryCalls": wfIpIntfStatsAtmArpFailRetryCalls,
       "wfIpIntfStatsAtmArpFailNoRetryCalls": wfIpIntfStatsAtmArpFailNoRetryCalls,
       "wfIpIntfStatsAtmArpSuccessfulCalls": wfIpIntfStatsAtmArpSuccessfulCalls,
       "wfIpIntfStatsAtmArpAcceptedCalls": wfIpIntfStatsAtmArpAcceptedCalls,
       "wfIpIntfStatsAtmArpOpenSvcs": wfIpIntfStatsAtmArpOpenSvcs,
       "wfIpIntfStatsMcastInPkts": wfIpIntfStatsMcastInPkts,
       "wfIpIntfStatsMcastOutPkts": wfIpIntfStatsMcastOutPkts,
       "wfIpIntfStatsMcastInDataPkts": wfIpIntfStatsMcastInDataPkts,
       "wfIpIntfStatsControlPathInPkts": wfIpIntfStatsControlPathInPkts,
       "wfIpIntfStatsControlPathOutPkts": wfIpIntfStatsControlPathOutPkts,
       "wfIpIntfStatsIcmpTable": wfIpIntfStatsIcmpTable,
       "wfIpIntfStatsIcmpEntry": wfIpIntfStatsIcmpEntry,
       "wfIpIntfStatsIcmpAddr": wfIpIntfStatsIcmpAddr,
       "wfIpIntfStatsIcmpCircuit": wfIpIntfStatsIcmpCircuit,
       "wfIpIntfStatsIcmpInMsgs": wfIpIntfStatsIcmpInMsgs,
       "wfIpIntfStatsIcmpInErrors": wfIpIntfStatsIcmpInErrors,
       "wfIpIntfStatsIcmpInDestUnreachs": wfIpIntfStatsIcmpInDestUnreachs,
       "wfIpIntfStatsIcmpInTimeExcds": wfIpIntfStatsIcmpInTimeExcds,
       "wfIpIntfStatsIcmpInParmProbs": wfIpIntfStatsIcmpInParmProbs,
       "wfIpIntfStatsIcmpInSrcQuenchs": wfIpIntfStatsIcmpInSrcQuenchs,
       "wfIpIntfStatsIcmpInRedirects": wfIpIntfStatsIcmpInRedirects,
       "wfIpIntfStatsIcmpInEchos": wfIpIntfStatsIcmpInEchos,
       "wfIpIntfStatsIcmpInEchoReps": wfIpIntfStatsIcmpInEchoReps,
       "wfIpIntfStatsIcmpInTimestamps": wfIpIntfStatsIcmpInTimestamps,
       "wfIpIntfStatsIcmpInTimestampReps": wfIpIntfStatsIcmpInTimestampReps,
       "wfIpIntfStatsIcmpInAddrMasks": wfIpIntfStatsIcmpInAddrMasks,
       "wfIpIntfStatsIcmpInAddrMaskReps": wfIpIntfStatsIcmpInAddrMaskReps,
       "wfIpIntfStatsIcmpOutMsgs": wfIpIntfStatsIcmpOutMsgs,
       "wfIpIntfStatsIcmpOutErrors": wfIpIntfStatsIcmpOutErrors,
       "wfIpIntfStatsIcmpOutDestUnreachs": wfIpIntfStatsIcmpOutDestUnreachs,
       "wfIpIntfStatsIcmpOutTimeExcds": wfIpIntfStatsIcmpOutTimeExcds,
       "wfIpIntfStatsIcmpOutParmProbs": wfIpIntfStatsIcmpOutParmProbs,
       "wfIpIntfStatsIcmpOutSrcQuenchs": wfIpIntfStatsIcmpOutSrcQuenchs,
       "wfIpIntfStatsIcmpOutRedirects": wfIpIntfStatsIcmpOutRedirects,
       "wfIpIntfStatsIcmpOutEchos": wfIpIntfStatsIcmpOutEchos,
       "wfIpIntfStatsIcmpOutEchoReps": wfIpIntfStatsIcmpOutEchoReps,
       "wfIpIntfStatsIcmpOutTimestamps": wfIpIntfStatsIcmpOutTimestamps,
       "wfIpIntfStatsIcmpOutTimestampReps": wfIpIntfStatsIcmpOutTimestampReps,
       "wfIpIntfStatsIcmpOutAddrMasks": wfIpIntfStatsIcmpOutAddrMasks,
       "wfIpIntfStatsIcmpOutAddrMaskReps": wfIpIntfStatsIcmpOutAddrMaskReps,
       "wfIpIntfStatsIcmpInAdminProhib": wfIpIntfStatsIcmpInAdminProhib,
       "wfIpIntfStatsIcmpOutAdminProhib": wfIpIntfStatsIcmpOutAdminProhib,
       "wfIpIntfStatsIcmpInRdiscSolicit": wfIpIntfStatsIcmpInRdiscSolicit,
       "wfIpIntfStatsIcmpInRdiscAdvert": wfIpIntfStatsIcmpInRdiscAdvert,
       "wfIpIntfStatsIcmpOutRdiscAdvert": wfIpIntfStatsIcmpOutRdiscAdvert,
       "wfIpGreTnlTable": wfIpGreTnlTable,
       "wfIpGreTnlEntry": wfIpGreTnlEntry,
       "wfIpGreTnlCreate": wfIpGreTnlCreate,
       "wfIpGreTnlEnable": wfIpGreTnlEnable,
       "wfIpGreTnlState": wfIpGreTnlState,
       "wfIpGreTnlNum": wfIpGreTnlNum,
       "wfIpGreTnlName": wfIpGreTnlName,
       "wfIpGreTnlCctNum": wfIpGreTnlCctNum,
       "wfIpGreTnlLocIpAddr": wfIpGreTnlLocIpAddr,
       "wfIpGreTnlMinMtu": wfIpGreTnlMinMtu,
       "wfIpGreConnTable": wfIpGreConnTable,
       "wfIpGreConnEntry": wfIpGreConnEntry,
       "wfIpGreConnCreate": wfIpGreConnCreate,
       "wfIpGreConnEnable": wfIpGreConnEnable,
       "wfIpGreConnTnlNum": wfIpGreConnTnlNum,
       "wfIpGreConnNum": wfIpGreConnNum,
       "wfIpGreConnName": wfIpGreConnName,
       "wfIpGreConnRemIpAddr": wfIpGreConnRemIpAddr,
       "wfIpGreConnProtoMap": wfIpGreConnProtoMap,
       "wfIpFilterRuleTable": wfIpFilterRuleTable,
       "wfIpFilterRuleEntry": wfIpFilterRuleEntry,
       "wfIpFilterRuleCreate": wfIpFilterRuleCreate,
       "wfIpFilterRuleNumber": wfIpFilterRuleNumber,
       "wfIpFilterRuleName": wfIpFilterRuleName,
       "wfIpFilterRuleDescription": wfIpFilterRuleDescription,
       "wfIpFilterRuleFragment": wfIpFilterRuleFragment,
       "wfIpFilterRuleNewTosValue": wfIpFilterRuleNewTosValue,
       "wfIpFilterRuleNewTosValueMask": wfIpFilterRuleNewTosValueMask,
       "wfIpFilterRuleAction": wfIpFilterRuleAction,
       "wfIpFilterRuleClassifyAction": wfIpFilterRuleClassifyAction,
       "wfIpFilterRuleDropPreference": wfIpFilterRuleDropPreference,
       "wfIpFilterConfigTable": wfIpFilterConfigTable,
       "wfIpFilterConfigEntry": wfIpFilterConfigEntry,
       "wfIpFilterConfigCreate": wfIpFilterConfigCreate,
       "wfIpFilterConfigEnable": wfIpFilterConfigEnable,
       "wfIpFilterConfigStatus": wfIpFilterConfigStatus,
       "wfIpFilterConfigRuleNumber": wfIpFilterConfigRuleNumber,
       "wfIpFilterConfigRulePrecedence": wfIpFilterConfigRulePrecedence,
       "wfIpFilterConfigFilterType": wfIpFilterConfigFilterType,
       "wfIpFilterConfigLogFilterInfo": wfIpFilterConfigLogFilterInfo,
       "wfIpFilterConfigReserved": wfIpFilterConfigReserved,
       "wfIpFilterConfigInterface": wfIpFilterConfigInterface,
       "wfIpFilterConfigCircuit": wfIpFilterConfigCircuit,
       "wfIpFilterConfigIndex": wfIpFilterConfigIndex,
       "wfIpFilterStatsTable": wfIpFilterStatsTable,
       "wfIpFilterStatsEntry": wfIpFilterStatsEntry,
       "wfIpFilterStatsCounter": wfIpFilterStatsCounter,
       "wfIpFilterStatsInterface": wfIpFilterStatsInterface,
       "wfIpFilterStatsCircuit": wfIpFilterStatsCircuit,
       "wfIpFilterStatsIndex": wfIpFilterStatsIndex,
       "wfIpTosTemplateCfgTable": wfIpTosTemplateCfgTable,
       "wfIpTosTemplateCfgEntry": wfIpTosTemplateCfgEntry,
       "wfIpTosTemplateCfgCreate": wfIpTosTemplateCfgCreate,
       "wfIpTosTemplateCfgIndex": wfIpTosTemplateCfgIndex,
       "wfIpTosTemplateCfgName": wfIpTosTemplateCfgName,
       "wfIpTosTemplateCfgStatus": wfIpTosTemplateCfgStatus,
       "wfIpTosTemplateCfgRxEnable": wfIpTosTemplateCfgRxEnable,
       "wfIpTosTemplateCfgRxMapping": wfIpTosTemplateCfgRxMapping,
       "wfIpTosTemplateCfgTxEnable": wfIpTosTemplateCfgTxEnable,
       "wfIpTosTemplateCfgTxMapping": wfIpTosTemplateCfgTxMapping,
       "wfIpTosTemplateTable": wfIpTosTemplateTable,
       "wfIpTosTemplateEntry": wfIpTosTemplateEntry,
       "wfIpTosTemplateIndex": wfIpTosTemplateIndex,
       "wfIpTosTemplateName": wfIpTosTemplateName,
       "wfIpTosTemplateStatus": wfIpTosTemplateStatus,
       "wfIpTosTemplateRxEnable": wfIpTosTemplateRxEnable,
       "wfIpTosTemplateRxMapping": wfIpTosTemplateRxMapping,
       "wfIpTosTemplateTxEnable": wfIpTosTemplateTxEnable,
       "wfIpTosTemplateTxMapping": wfIpTosTemplateTxMapping,
       "wfIpBaseDbg": wfIpBaseDbg,
       "wfIpBaseDbgCreate": wfIpBaseDbgCreate,
       "wfIpBaseDbgOptions": wfIpBaseDbgOptions,
       "wfIpBaseDbgAddress": wfIpBaseDbgAddress,
       "wfIpBaseDbgAddressMask": wfIpBaseDbgAddressMask,
       "wfIpBaseDbgMisc": wfIpBaseDbgMisc,
       "wfIpFilterTemplateTable": wfIpFilterTemplateTable,
       "wfIpFilterTemplateEntry": wfIpFilterTemplateEntry,
       "wfIpFilterTemplateCreate": wfIpFilterTemplateCreate,
       "wfIpFilterTemplateRuleNumber": wfIpFilterTemplateRuleNumber,
       "wfIpFilterTemplateFragment": wfIpFilterTemplateFragment,
       "wfIpFilterTemplateDefinition": wfIpFilterTemplateDefinition,
       "wfIpFilterTemplateName": wfIpFilterTemplateName,
       "wfRipIntfTable": wfRipIntfTable,
       "wfRipIntfEntry": wfRipIntfEntry,
       "wfRipInterfaceCreate": wfRipInterfaceCreate,
       "wfRipInterfaceEnable": wfRipInterfaceEnable,
       "wfRipInterfaceState": wfRipInterfaceState,
       "wfRipInterfaceIndex": wfRipInterfaceIndex,
       "wfRipInterfaceSupply": wfRipInterfaceSupply,
       "wfRipInterfaceListen": wfRipInterfaceListen,
       "wfRipInterfaceDefaultRouteSupply": wfRipInterfaceDefaultRouteSupply,
       "wfRipInterfaceDefaultRouteListen": wfRipInterfaceDefaultRouteListen,
       "wfRipInterfacePoisonedReversed": wfRipInterfacePoisonedReversed,
       "wfRipInterfaceTable": wfRipInterfaceTable,
       "wfRipInterfaceEntry": wfRipInterfaceEntry,
       "wfRipIntfCreate": wfRipIntfCreate,
       "wfRipIntfEnable": wfRipIntfEnable,
       "wfRipIntfState": wfRipIntfState,
       "wfRipIntfIndex": wfRipIntfIndex,
       "wfRipIntfSupply": wfRipIntfSupply,
       "wfRipIntfListen": wfRipIntfListen,
       "wfRipIntfDefaultRouteSupply": wfRipIntfDefaultRouteSupply,
       "wfRipIntfDefaultRouteListen": wfRipIntfDefaultRouteListen,
       "wfRipIntfPoisonedReversed": wfRipIntfPoisonedReversed,
       "wfRipIntfCct": wfRipIntfCct,
       "wfRipIntfTTL": wfRipIntfTTL,
       "wfRipIntfBroadcastTimer": wfRipIntfBroadcastTimer,
       "wfRipIntfTimeoutTimer": wfRipIntfTimeoutTimer,
       "wfRipIntfHolddownTimer": wfRipIntfHolddownTimer,
       "wfRipIntfCompSwitch": wfRipIntfCompSwitch,
       "wfRipIntfTriggeredUpdates": wfRipIntfTriggeredUpdates,
       "wfRipIntfAuthType": wfRipIntfAuthType,
       "wfRipIntfAuthentication": wfRipIntfAuthentication,
       "wfRipIntfInitStabilizationTimer": wfRipIntfInitStabilizationTimer,
       "wfRipIntfSVCBroadcast": wfRipIntfSVCBroadcast,
       "wfRipIntfDefaultRouteCost": wfRipIntfDefaultRouteCost,
       "wfUdp": wfUdp,
       "wfUdpInDatagrams": wfUdpInDatagrams,
       "wfUdpNoPorts": wfUdpNoPorts,
       "wfUdpInErrors": wfUdpInErrors,
       "wfUdpOutDatagrams": wfUdpOutDatagrams,
       "wfUdpTable": wfUdpTable,
       "wfUdpEntry": wfUdpEntry,
       "wfUdpLocalAddress": wfUdpLocalAddress,
       "wfUdpLocalPort": wfUdpLocalPort,
       "wfUdpMpr": wfUdpMpr,
       "wfUdpMprCreate": wfUdpMprCreate,
       "wfUdpMprEnable": wfUdpMprEnable,
       "wfUdpMprStartPort": wfUdpMprStartPort,
       "wfUdpMprNumberOfPorts": wfUdpMprNumberOfPorts,
       "wfUdpMprStatisticsEnable": wfUdpMprStatisticsEnable,
       "wfUdpMprInPkts": wfUdpMprInPkts,
       "wfUdpMprOutPkts": wfUdpMprOutPkts,
       "wfUdpMprGenPkts": wfUdpMprGenPkts,
       "wfUdpMprLookupDrops": wfUdpMprLookupDrops,
       "wfUdpMprDisableDrops": wfUdpMprDisableDrops,
       "wfUdpMprMappingTable": wfUdpMprMappingTable,
       "wfUdpMprMappingEntry": wfUdpMprMappingEntry,
       "wfUdpMprMapCreate": wfUdpMprMapCreate,
       "wfUdpMprMapEnable": wfUdpMprMapEnable,
       "wfUdpMprMapPort": wfUdpMprMapPort,
       "wfUdpMprMapMcastAddr": wfUdpMprMapMcastAddr,
       "wfUdpMprMapStatisticsEnable": wfUdpMprMapStatisticsEnable,
       "wfUdpMprMapInPkts": wfUdpMprMapInPkts,
       "wfUdpMprMapOutPkts": wfUdpMprMapOutPkts,
       "wfUdpMprMapGenPkts": wfUdpMprMapGenPkts,
       "wfUdpMprMapLookupDrops": wfUdpMprMapLookupDrops,
       "wfUdpMprMapDisableDrops": wfUdpMprMapDisableDrops}
)
