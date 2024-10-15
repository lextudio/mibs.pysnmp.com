# SNMP MIB module (ALCATEL-IND1-DVMRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-DVMRP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:57 2024
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

(routingIND1Dvmrp,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1Dvmrp")

(dvmrpInterfaceEntry,) = mibBuilder.importSymbols(
    "DVMRP-STD-MIB",
    "dvmrpInterfaceEntry")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

alcatelIND1DVMRPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1)
)
alcatelIND1DVMRPMIB.setRevisions(
        ("2007-04-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1DVMRPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1DVMRPMIBObjects = _AlcatelIND1DVMRPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1)
)
_AlaDvmrpGlobalConfig_ObjectIdentity = ObjectIdentity
alaDvmrpGlobalConfig = _AlaDvmrpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1)
)


class _AlaDvmrpAdminStatus_Type(Integer32):
    """Custom type alaDvmrpAdminStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("unrestrictedEnable", 3))
    )


_AlaDvmrpAdminStatus_Type.__name__ = "Integer32"
_AlaDvmrpAdminStatus_Object = MibScalar
alaDvmrpAdminStatus = _AlaDvmrpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 1),
    _AlaDvmrpAdminStatus_Type()
)
alaDvmrpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpAdminStatus.setStatus("current")


class _AlaDvmrpRouteReportInterval_Type(Integer32):
    """Custom type alaDvmrpRouteReportInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_AlaDvmrpRouteReportInterval_Type.__name__ = "Integer32"
_AlaDvmrpRouteReportInterval_Object = MibScalar
alaDvmrpRouteReportInterval = _AlaDvmrpRouteReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 2),
    _AlaDvmrpRouteReportInterval_Type()
)
alaDvmrpRouteReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpRouteReportInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpRouteReportInterval.setUnits("seconds")


class _AlaDvmrpFlashUpdateInterval_Type(Integer32):
    """Custom type alaDvmrpFlashUpdateInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_AlaDvmrpFlashUpdateInterval_Type.__name__ = "Integer32"
_AlaDvmrpFlashUpdateInterval_Object = MibScalar
alaDvmrpFlashUpdateInterval = _AlaDvmrpFlashUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 3),
    _AlaDvmrpFlashUpdateInterval_Type()
)
alaDvmrpFlashUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpFlashUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpFlashUpdateInterval.setUnits("seconds")


class _AlaDvmrpNeighborTimeout_Type(Integer32):
    """Custom type alaDvmrpNeighborTimeout based on Integer32"""
    defaultValue = 35

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_AlaDvmrpNeighborTimeout_Type.__name__ = "Integer32"
_AlaDvmrpNeighborTimeout_Object = MibScalar
alaDvmrpNeighborTimeout = _AlaDvmrpNeighborTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 4),
    _AlaDvmrpNeighborTimeout_Type()
)
alaDvmrpNeighborTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpNeighborTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpNeighborTimeout.setUnits("seconds")


class _AlaDvmrpRouteExpirationTimeout_Type(Integer32):
    """Custom type alaDvmrpRouteExpirationTimeout based on Integer32"""
    defaultValue = 140

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 4000),
    )


_AlaDvmrpRouteExpirationTimeout_Type.__name__ = "Integer32"
_AlaDvmrpRouteExpirationTimeout_Object = MibScalar
alaDvmrpRouteExpirationTimeout = _AlaDvmrpRouteExpirationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 5),
    _AlaDvmrpRouteExpirationTimeout_Type()
)
alaDvmrpRouteExpirationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpRouteExpirationTimeout.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpRouteExpirationTimeout.setUnits("seconds")


class _AlaDvmrpRouteHoldDown_Type(Integer32):
    """Custom type alaDvmrpRouteHoldDown based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_AlaDvmrpRouteHoldDown_Type.__name__ = "Integer32"
_AlaDvmrpRouteHoldDown_Object = MibScalar
alaDvmrpRouteHoldDown = _AlaDvmrpRouteHoldDown_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 6),
    _AlaDvmrpRouteHoldDown_Type()
)
alaDvmrpRouteHoldDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpRouteHoldDown.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpRouteHoldDown.setUnits("seconds")


class _AlaDvmrpNeighborProbeInterval_Type(Integer32):
    """Custom type alaDvmrpNeighborProbeInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_AlaDvmrpNeighborProbeInterval_Type.__name__ = "Integer32"
_AlaDvmrpNeighborProbeInterval_Object = MibScalar
alaDvmrpNeighborProbeInterval = _AlaDvmrpNeighborProbeInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 7),
    _AlaDvmrpNeighborProbeInterval_Type()
)
alaDvmrpNeighborProbeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpNeighborProbeInterval.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpNeighborProbeInterval.setUnits("seconds")


class _AlaDvmrpPruneLifetime_Type(Integer32):
    """Custom type alaDvmrpPruneLifetime based on Integer32"""
    defaultValue = 7200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 86400),
    )


_AlaDvmrpPruneLifetime_Type.__name__ = "Integer32"
_AlaDvmrpPruneLifetime_Object = MibScalar
alaDvmrpPruneLifetime = _AlaDvmrpPruneLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 8),
    _AlaDvmrpPruneLifetime_Type()
)
alaDvmrpPruneLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpPruneLifetime.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpPruneLifetime.setUnits("seconds")


class _AlaDvmrpPruneRetransmission_Type(Integer32):
    """Custom type alaDvmrpPruneRetransmission based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_AlaDvmrpPruneRetransmission_Type.__name__ = "Integer32"
_AlaDvmrpPruneRetransmission_Object = MibScalar
alaDvmrpPruneRetransmission = _AlaDvmrpPruneRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 9),
    _AlaDvmrpPruneRetransmission_Type()
)
alaDvmrpPruneRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpPruneRetransmission.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpPruneRetransmission.setUnits("seconds")


class _AlaDvmrpGraftRetransmission_Type(Integer32):
    """Custom type alaDvmrpGraftRetransmission based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_AlaDvmrpGraftRetransmission_Type.__name__ = "Integer32"
_AlaDvmrpGraftRetransmission_Object = MibScalar
alaDvmrpGraftRetransmission = _AlaDvmrpGraftRetransmission_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 10),
    _AlaDvmrpGraftRetransmission_Type()
)
alaDvmrpGraftRetransmission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpGraftRetransmission.setStatus("current")
if mibBuilder.loadTexts:
    alaDvmrpGraftRetransmission.setUnits("seconds")


class _AlaDvmrpInitNbrAsSubord_Type(TruthValue):
    """Custom type alaDvmrpInitNbrAsSubord based on TruthValue"""


_AlaDvmrpInitNbrAsSubord_Object = MibScalar
alaDvmrpInitNbrAsSubord = _AlaDvmrpInitNbrAsSubord_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 11),
    _AlaDvmrpInitNbrAsSubord_Type()
)
alaDvmrpInitNbrAsSubord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpInitNbrAsSubord.setStatus("current")


class _AlaDvmrpBfdStatus_Type(Integer32):
    """Custom type alaDvmrpBfdStatus based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpBfdStatus_Type.__name__ = "Integer32"
_AlaDvmrpBfdStatus_Object = MibScalar
alaDvmrpBfdStatus = _AlaDvmrpBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 12),
    _AlaDvmrpBfdStatus_Type()
)
alaDvmrpBfdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpBfdStatus.setStatus("current")


class _AlaDvmrpBfdAllInterfaceStatus_Type(Integer32):
    """Custom type alaDvmrpBfdAllInterfaceStatus based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpBfdAllInterfaceStatus_Type.__name__ = "Integer32"
_AlaDvmrpBfdAllInterfaceStatus_Object = MibScalar
alaDvmrpBfdAllInterfaceStatus = _AlaDvmrpBfdAllInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 1, 13),
    _AlaDvmrpBfdAllInterfaceStatus_Type()
)
alaDvmrpBfdAllInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpBfdAllInterfaceStatus.setStatus("current")
_AlaDvmrpDebugConfig_ObjectIdentity = ObjectIdentity
alaDvmrpDebugConfig = _AlaDvmrpDebugConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2)
)


class _AlaDvmrpDebugLevel_Type(Integer32):
    """Custom type alaDvmrpDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AlaDvmrpDebugLevel_Type.__name__ = "Integer32"
_AlaDvmrpDebugLevel_Object = MibScalar
alaDvmrpDebugLevel = _AlaDvmrpDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 1),
    _AlaDvmrpDebugLevel_Type()
)
alaDvmrpDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugLevel.setStatus("deprecated")


class _AlaDvmrpDebugError_Type(Integer32):
    """Custom type alaDvmrpDebugError based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugError_Type.__name__ = "Integer32"
_AlaDvmrpDebugError_Object = MibScalar
alaDvmrpDebugError = _AlaDvmrpDebugError_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 2),
    _AlaDvmrpDebugError_Type()
)
alaDvmrpDebugError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugError.setStatus("deprecated")


class _AlaDvmrpDebugNbr_Type(Integer32):
    """Custom type alaDvmrpDebugNbr based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugNbr_Type.__name__ = "Integer32"
_AlaDvmrpDebugNbr_Object = MibScalar
alaDvmrpDebugNbr = _AlaDvmrpDebugNbr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 3),
    _AlaDvmrpDebugNbr_Type()
)
alaDvmrpDebugNbr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugNbr.setStatus("deprecated")


class _AlaDvmrpDebugRoutes_Type(Integer32):
    """Custom type alaDvmrpDebugRoutes based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugRoutes_Type.__name__ = "Integer32"
_AlaDvmrpDebugRoutes_Object = MibScalar
alaDvmrpDebugRoutes = _AlaDvmrpDebugRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 4),
    _AlaDvmrpDebugRoutes_Type()
)
alaDvmrpDebugRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugRoutes.setStatus("deprecated")


class _AlaDvmrpDebugProbes_Type(Integer32):
    """Custom type alaDvmrpDebugProbes based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugProbes_Type.__name__ = "Integer32"
_AlaDvmrpDebugProbes_Object = MibScalar
alaDvmrpDebugProbes = _AlaDvmrpDebugProbes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 5),
    _AlaDvmrpDebugProbes_Type()
)
alaDvmrpDebugProbes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugProbes.setStatus("deprecated")


class _AlaDvmrpDebugPrunes_Type(Integer32):
    """Custom type alaDvmrpDebugPrunes based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugPrunes_Type.__name__ = "Integer32"
_AlaDvmrpDebugPrunes_Object = MibScalar
alaDvmrpDebugPrunes = _AlaDvmrpDebugPrunes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 6),
    _AlaDvmrpDebugPrunes_Type()
)
alaDvmrpDebugPrunes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugPrunes.setStatus("deprecated")


class _AlaDvmrpDebugGrafts_Type(Integer32):
    """Custom type alaDvmrpDebugGrafts based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugGrafts_Type.__name__ = "Integer32"
_AlaDvmrpDebugGrafts_Object = MibScalar
alaDvmrpDebugGrafts = _AlaDvmrpDebugGrafts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 7),
    _AlaDvmrpDebugGrafts_Type()
)
alaDvmrpDebugGrafts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugGrafts.setStatus("deprecated")


class _AlaDvmrpDebugTime_Type(Integer32):
    """Custom type alaDvmrpDebugTime based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugTime_Type.__name__ = "Integer32"
_AlaDvmrpDebugTime_Object = MibScalar
alaDvmrpDebugTime = _AlaDvmrpDebugTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 8),
    _AlaDvmrpDebugTime_Type()
)
alaDvmrpDebugTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugTime.setStatus("deprecated")


class _AlaDvmrpDebugIgmp_Type(Integer32):
    """Custom type alaDvmrpDebugIgmp based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugIgmp_Type.__name__ = "Integer32"
_AlaDvmrpDebugIgmp_Object = MibScalar
alaDvmrpDebugIgmp = _AlaDvmrpDebugIgmp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 9),
    _AlaDvmrpDebugIgmp_Type()
)
alaDvmrpDebugIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugIgmp.setStatus("deprecated")


class _AlaDvmrpDebugFlash_Type(Integer32):
    """Custom type alaDvmrpDebugFlash based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugFlash_Type.__name__ = "Integer32"
_AlaDvmrpDebugFlash_Object = MibScalar
alaDvmrpDebugFlash = _AlaDvmrpDebugFlash_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 10),
    _AlaDvmrpDebugFlash_Type()
)
alaDvmrpDebugFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugFlash.setStatus("deprecated")


class _AlaDvmrpDebugMip_Type(Integer32):
    """Custom type alaDvmrpDebugMip based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugMip_Type.__name__ = "Integer32"
_AlaDvmrpDebugMip_Object = MibScalar
alaDvmrpDebugMip = _AlaDvmrpDebugMip_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 11),
    _AlaDvmrpDebugMip_Type()
)
alaDvmrpDebugMip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugMip.setStatus("deprecated")


class _AlaDvmrpDebugInit_Type(Integer32):
    """Custom type alaDvmrpDebugInit based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugInit_Type.__name__ = "Integer32"
_AlaDvmrpDebugInit_Object = MibScalar
alaDvmrpDebugInit = _AlaDvmrpDebugInit_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 12),
    _AlaDvmrpDebugInit_Type()
)
alaDvmrpDebugInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugInit.setStatus("deprecated")


class _AlaDvmrpDebugTm_Type(Integer32):
    """Custom type alaDvmrpDebugTm based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugTm_Type.__name__ = "Integer32"
_AlaDvmrpDebugTm_Object = MibScalar
alaDvmrpDebugTm = _AlaDvmrpDebugTm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 13),
    _AlaDvmrpDebugTm_Type()
)
alaDvmrpDebugTm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugTm.setStatus("deprecated")


class _AlaDvmrpDebugIpmrm_Type(Integer32):
    """Custom type alaDvmrpDebugIpmrm based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugIpmrm_Type.__name__ = "Integer32"
_AlaDvmrpDebugIpmrm_Object = MibScalar
alaDvmrpDebugIpmrm = _AlaDvmrpDebugIpmrm_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 14),
    _AlaDvmrpDebugIpmrm_Type()
)
alaDvmrpDebugIpmrm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugIpmrm.setStatus("deprecated")


class _AlaDvmrpDebugMisc_Type(Integer32):
    """Custom type alaDvmrpDebugMisc based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugMisc_Type.__name__ = "Integer32"
_AlaDvmrpDebugMisc_Object = MibScalar
alaDvmrpDebugMisc = _AlaDvmrpDebugMisc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 15),
    _AlaDvmrpDebugMisc_Type()
)
alaDvmrpDebugMisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugMisc.setStatus("deprecated")


class _AlaDvmrpDebugAll_Type(Integer32):
    """Custom type alaDvmrpDebugAll based on Integer32"""
    defaultValue = 2

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


_AlaDvmrpDebugAll_Type.__name__ = "Integer32"
_AlaDvmrpDebugAll_Object = MibScalar
alaDvmrpDebugAll = _AlaDvmrpDebugAll_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 2, 16),
    _AlaDvmrpDebugAll_Type()
)
alaDvmrpDebugAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDvmrpDebugAll.setStatus("deprecated")
_AlaDvmrpTunnelXIfTable_Object = MibTable
alaDvmrpTunnelXIfTable = _AlaDvmrpTunnelXIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaDvmrpTunnelXIfTable.setStatus("current")
_AlaDvmrpTunnelXIfEntry_Object = MibTableRow
alaDvmrpTunnelXIfEntry = _AlaDvmrpTunnelXIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1)
)
alaDvmrpTunnelXIfEntry.setIndexNames(
    (0, "ALCATEL-IND1-DVMRP-MIB", "alaDvmrpTunnelIndex"),
)
if mibBuilder.loadTexts:
    alaDvmrpTunnelXIfEntry.setStatus("current")
_AlaDvmrpTunnelIndex_Type = Unsigned32
_AlaDvmrpTunnelIndex_Object = MibTableColumn
alaDvmrpTunnelIndex = _AlaDvmrpTunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1, 1),
    _AlaDvmrpTunnelIndex_Type()
)
alaDvmrpTunnelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDvmrpTunnelIndex.setStatus("current")
_AlaDvmrpLocalIfIndex_Type = Unsigned32
_AlaDvmrpLocalIfIndex_Object = MibTableColumn
alaDvmrpLocalIfIndex = _AlaDvmrpLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 3, 1, 2),
    _AlaDvmrpLocalIfIndex_Type()
)
alaDvmrpLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDvmrpLocalIfIndex.setStatus("current")
_AlaDvmrpIfAugTable_Object = MibTable
alaDvmrpIfAugTable = _AlaDvmrpIfAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaDvmrpIfAugTable.setStatus("current")
_AlaDvmrpIfAugEntry_Object = MibTableRow
alaDvmrpIfAugEntry = _AlaDvmrpIfAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    alaDvmrpIfAugEntry.setStatus("current")


class _AlaDvmrpIfBfdStatus_Type(Integer32):
    """Custom type alaDvmrpIfBfdStatus based on Integer32"""
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


_AlaDvmrpIfBfdStatus_Type.__name__ = "Integer32"
_AlaDvmrpIfBfdStatus_Object = MibTableColumn
alaDvmrpIfBfdStatus = _AlaDvmrpIfBfdStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 1, 4, 1, 1),
    _AlaDvmrpIfBfdStatus_Type()
)
alaDvmrpIfBfdStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDvmrpIfBfdStatus.setStatus("current")
_AlcatelIND1DVMRPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1DVMRPMIBConformance = _AlcatelIND1DVMRPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2)
)
_AlcatelIND1DVMRPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1DVMRPMIBCompliances = _AlcatelIND1DVMRPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 1)
)
_AlcatelIND1DVMRPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1DVMRPMIBGroups = _AlcatelIND1DVMRPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2)
)
dvmrpInterfaceEntry.registerAugmentions(
    ("ALCATEL-IND1-DVMRP-MIB",
     "alaDvmrpIfAugEntry")
)
alaDvmrpIfAugEntry.setIndexNames(*dvmrpInterfaceEntry.getIndexNames())

# Managed Objects groups

alaDvmrpConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 1)
)
alaDvmrpConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpAdminStatus"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteReportInterval"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpFlashUpdateInterval"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpNeighborTimeout"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteExpirationTimeout"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpRouteHoldDown"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpNeighborProbeInterval"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpPruneLifetime"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpPruneRetransmission"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpGraftRetransmission"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpInitNbrAsSubord"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpBfdStatus"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpBfdAllInterfaceStatus"))
)
if mibBuilder.loadTexts:
    alaDvmrpConfigMIBGroup.setStatus("current")

alaDvmrpDebugMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 2)
)
alaDvmrpDebugMIBGroup.setObjects(
      *(("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugLevel"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugError"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugNbr"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugRoutes"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugProbes"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugPrunes"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugGrafts"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugTime"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugIgmp"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugFlash"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMip"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugInit"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugTm"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugIpmrm"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugMisc"),
        ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpDebugAll"))
)
if mibBuilder.loadTexts:
    alaDvmrpDebugMIBGroup.setStatus("current")

alaDvmrpTunnelXIfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 3)
)
alaDvmrpTunnelXIfMIBGroup.setObjects(
    ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpLocalIfIndex")
)
if mibBuilder.loadTexts:
    alaDvmrpTunnelXIfMIBGroup.setStatus("current")

alaDvmrpIfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 2, 4)
)
alaDvmrpIfConfigGroup.setObjects(
    ("ALCATEL-IND1-DVMRP-MIB", "alaDvmrpIfBfdStatus")
)
if mibBuilder.loadTexts:
    alaDvmrpIfConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaDvmrpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 7, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaDvmrpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-DVMRP-MIB",
    **{"alcatelIND1DVMRPMIB": alcatelIND1DVMRPMIB,
       "alcatelIND1DVMRPMIBObjects": alcatelIND1DVMRPMIBObjects,
       "alaDvmrpGlobalConfig": alaDvmrpGlobalConfig,
       "alaDvmrpAdminStatus": alaDvmrpAdminStatus,
       "alaDvmrpRouteReportInterval": alaDvmrpRouteReportInterval,
       "alaDvmrpFlashUpdateInterval": alaDvmrpFlashUpdateInterval,
       "alaDvmrpNeighborTimeout": alaDvmrpNeighborTimeout,
       "alaDvmrpRouteExpirationTimeout": alaDvmrpRouteExpirationTimeout,
       "alaDvmrpRouteHoldDown": alaDvmrpRouteHoldDown,
       "alaDvmrpNeighborProbeInterval": alaDvmrpNeighborProbeInterval,
       "alaDvmrpPruneLifetime": alaDvmrpPruneLifetime,
       "alaDvmrpPruneRetransmission": alaDvmrpPruneRetransmission,
       "alaDvmrpGraftRetransmission": alaDvmrpGraftRetransmission,
       "alaDvmrpInitNbrAsSubord": alaDvmrpInitNbrAsSubord,
       "alaDvmrpBfdStatus": alaDvmrpBfdStatus,
       "alaDvmrpBfdAllInterfaceStatus": alaDvmrpBfdAllInterfaceStatus,
       "alaDvmrpDebugConfig": alaDvmrpDebugConfig,
       "alaDvmrpDebugLevel": alaDvmrpDebugLevel,
       "alaDvmrpDebugError": alaDvmrpDebugError,
       "alaDvmrpDebugNbr": alaDvmrpDebugNbr,
       "alaDvmrpDebugRoutes": alaDvmrpDebugRoutes,
       "alaDvmrpDebugProbes": alaDvmrpDebugProbes,
       "alaDvmrpDebugPrunes": alaDvmrpDebugPrunes,
       "alaDvmrpDebugGrafts": alaDvmrpDebugGrafts,
       "alaDvmrpDebugTime": alaDvmrpDebugTime,
       "alaDvmrpDebugIgmp": alaDvmrpDebugIgmp,
       "alaDvmrpDebugFlash": alaDvmrpDebugFlash,
       "alaDvmrpDebugMip": alaDvmrpDebugMip,
       "alaDvmrpDebugInit": alaDvmrpDebugInit,
       "alaDvmrpDebugTm": alaDvmrpDebugTm,
       "alaDvmrpDebugIpmrm": alaDvmrpDebugIpmrm,
       "alaDvmrpDebugMisc": alaDvmrpDebugMisc,
       "alaDvmrpDebugAll": alaDvmrpDebugAll,
       "alaDvmrpTunnelXIfTable": alaDvmrpTunnelXIfTable,
       "alaDvmrpTunnelXIfEntry": alaDvmrpTunnelXIfEntry,
       "alaDvmrpTunnelIndex": alaDvmrpTunnelIndex,
       "alaDvmrpLocalIfIndex": alaDvmrpLocalIfIndex,
       "alaDvmrpIfAugTable": alaDvmrpIfAugTable,
       "alaDvmrpIfAugEntry": alaDvmrpIfAugEntry,
       "alaDvmrpIfBfdStatus": alaDvmrpIfBfdStatus,
       "alcatelIND1DVMRPMIBConformance": alcatelIND1DVMRPMIBConformance,
       "alcatelIND1DVMRPMIBCompliances": alcatelIND1DVMRPMIBCompliances,
       "alaDvmrpCompliance": alaDvmrpCompliance,
       "alcatelIND1DVMRPMIBGroups": alcatelIND1DVMRPMIBGroups,
       "alaDvmrpConfigMIBGroup": alaDvmrpConfigMIBGroup,
       "alaDvmrpDebugMIBGroup": alaDvmrpDebugMIBGroup,
       "alaDvmrpTunnelXIfMIBGroup": alaDvmrpTunnelXIfMIBGroup,
       "alaDvmrpIfConfigGroup": alaDvmrpIfConfigGroup}
)
