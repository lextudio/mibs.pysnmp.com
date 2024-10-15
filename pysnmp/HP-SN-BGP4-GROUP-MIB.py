# SNMP MIB module (HP-SN-BGP4-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-BGP4-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:42 2024
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

(snBgp4,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snBgp4")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnBgp4Gen_ObjectIdentity = ObjectIdentity
snBgp4Gen = _SnBgp4Gen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1)
)


class _SnBgp4GenAlwaysCompareMed_Type(Integer32):
    """Custom type snBgp4GenAlwaysCompareMed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4GenAlwaysCompareMed_Type.__name__ = "Integer32"
_SnBgp4GenAlwaysCompareMed_Object = MibScalar
snBgp4GenAlwaysCompareMed = _SnBgp4GenAlwaysCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 1),
    _SnBgp4GenAlwaysCompareMed_Type()
)
snBgp4GenAlwaysCompareMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenAlwaysCompareMed.setStatus("mandatory")


class _SnBgp4GenAutoSummary_Type(Integer32):
    """Custom type snBgp4GenAutoSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4GenAutoSummary_Type.__name__ = "Integer32"
_SnBgp4GenAutoSummary_Object = MibScalar
snBgp4GenAutoSummary = _SnBgp4GenAutoSummary_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 2),
    _SnBgp4GenAutoSummary_Type()
)
snBgp4GenAutoSummary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenAutoSummary.setStatus("mandatory")
_SnBgp4GenDefaultLocalPreference_Type = Integer32
_SnBgp4GenDefaultLocalPreference_Object = MibScalar
snBgp4GenDefaultLocalPreference = _SnBgp4GenDefaultLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 3),
    _SnBgp4GenDefaultLocalPreference_Type()
)
snBgp4GenDefaultLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenDefaultLocalPreference.setStatus("mandatory")


class _SnBgp4GenDefaultInfoOriginate_Type(Integer32):
    """Custom type snBgp4GenDefaultInfoOriginate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4GenDefaultInfoOriginate_Type.__name__ = "Integer32"
_SnBgp4GenDefaultInfoOriginate_Object = MibScalar
snBgp4GenDefaultInfoOriginate = _SnBgp4GenDefaultInfoOriginate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 4),
    _SnBgp4GenDefaultInfoOriginate_Type()
)
snBgp4GenDefaultInfoOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenDefaultInfoOriginate.setStatus("mandatory")


class _SnBgp4GenFastExternalFallover_Type(Integer32):
    """Custom type snBgp4GenFastExternalFallover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4GenFastExternalFallover_Type.__name__ = "Integer32"
_SnBgp4GenFastExternalFallover_Object = MibScalar
snBgp4GenFastExternalFallover = _SnBgp4GenFastExternalFallover_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 5),
    _SnBgp4GenFastExternalFallover_Type()
)
snBgp4GenFastExternalFallover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenFastExternalFallover.setStatus("mandatory")
_SnBgp4GenNextBootNeighbors_Type = Integer32
_SnBgp4GenNextBootNeighbors_Object = MibScalar
snBgp4GenNextBootNeighbors = _SnBgp4GenNextBootNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 6),
    _SnBgp4GenNextBootNeighbors_Type()
)
snBgp4GenNextBootNeighbors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenNextBootNeighbors.setStatus("mandatory")
_SnBgp4GenNextBootRoutes_Type = Integer32
_SnBgp4GenNextBootRoutes_Object = MibScalar
snBgp4GenNextBootRoutes = _SnBgp4GenNextBootRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 7),
    _SnBgp4GenNextBootRoutes_Type()
)
snBgp4GenNextBootRoutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenNextBootRoutes.setStatus("mandatory")


class _SnBgp4GenSynchronization_Type(Integer32):
    """Custom type snBgp4GenSynchronization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4GenSynchronization_Type.__name__ = "Integer32"
_SnBgp4GenSynchronization_Object = MibScalar
snBgp4GenSynchronization = _SnBgp4GenSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 8),
    _SnBgp4GenSynchronization_Type()
)
snBgp4GenSynchronization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenSynchronization.setStatus("mandatory")


class _SnBgp4GenKeepAliveTime_Type(Integer32):
    """Custom type snBgp4GenKeepAliveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4GenKeepAliveTime_Type.__name__ = "Integer32"
_SnBgp4GenKeepAliveTime_Object = MibScalar
snBgp4GenKeepAliveTime = _SnBgp4GenKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 9),
    _SnBgp4GenKeepAliveTime_Type()
)
snBgp4GenKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenKeepAliveTime.setStatus("mandatory")


class _SnBgp4GenHoldTime_Type(Integer32):
    """Custom type snBgp4GenHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4GenHoldTime_Type.__name__ = "Integer32"
_SnBgp4GenHoldTime_Object = MibScalar
snBgp4GenHoldTime = _SnBgp4GenHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 10),
    _SnBgp4GenHoldTime_Type()
)
snBgp4GenHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenHoldTime.setStatus("mandatory")
_SnBgp4GenRouterId_Type = IpAddress
_SnBgp4GenRouterId_Object = MibScalar
snBgp4GenRouterId = _SnBgp4GenRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 11),
    _SnBgp4GenRouterId_Type()
)
snBgp4GenRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenRouterId.setStatus("mandatory")


class _SnBgp4GenTableMap_Type(OctetString):
    """Custom type snBgp4GenTableMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4GenTableMap_Type.__name__ = "OctetString"
_SnBgp4GenTableMap_Object = MibScalar
snBgp4GenTableMap = _SnBgp4GenTableMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 12),
    _SnBgp4GenTableMap_Type()
)
snBgp4GenTableMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenTableMap.setStatus("mandatory")


class _SnBgp4GenAdminStat_Type(Integer32):
    """Custom type snBgp4GenAdminStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4GenAdminStat_Type.__name__ = "Integer32"
_SnBgp4GenAdminStat_Object = MibScalar
snBgp4GenAdminStat = _SnBgp4GenAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 13),
    _SnBgp4GenAdminStat_Type()
)
snBgp4GenAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenAdminStat.setStatus("mandatory")
_SnBgp4GenDefaultMetric_Type = Integer32
_SnBgp4GenDefaultMetric_Object = MibScalar
snBgp4GenDefaultMetric = _SnBgp4GenDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 14),
    _SnBgp4GenDefaultMetric_Type()
)
snBgp4GenDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenDefaultMetric.setStatus("mandatory")
_SnBgp4GenMaxNeighbors_Type = Integer32
_SnBgp4GenMaxNeighbors_Object = MibScalar
snBgp4GenMaxNeighbors = _SnBgp4GenMaxNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 15),
    _SnBgp4GenMaxNeighbors_Type()
)
snBgp4GenMaxNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxNeighbors.setStatus("mandatory")
_SnBgp4GenMinNeighbors_Type = Integer32
_SnBgp4GenMinNeighbors_Object = MibScalar
snBgp4GenMinNeighbors = _SnBgp4GenMinNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 16),
    _SnBgp4GenMinNeighbors_Type()
)
snBgp4GenMinNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMinNeighbors.setStatus("mandatory")
_SnBgp4GenMaxRoutes_Type = Integer32
_SnBgp4GenMaxRoutes_Object = MibScalar
snBgp4GenMaxRoutes = _SnBgp4GenMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 17),
    _SnBgp4GenMaxRoutes_Type()
)
snBgp4GenMaxRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxRoutes.setStatus("mandatory")
_SnBgp4GenMinRoutes_Type = Integer32
_SnBgp4GenMinRoutes_Object = MibScalar
snBgp4GenMinRoutes = _SnBgp4GenMinRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 18),
    _SnBgp4GenMinRoutes_Type()
)
snBgp4GenMinRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMinRoutes.setStatus("mandatory")
_SnBgp4GenMaxAddrFilters_Type = Integer32
_SnBgp4GenMaxAddrFilters_Object = MibScalar
snBgp4GenMaxAddrFilters = _SnBgp4GenMaxAddrFilters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 19),
    _SnBgp4GenMaxAddrFilters_Type()
)
snBgp4GenMaxAddrFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxAddrFilters.setStatus("mandatory")
_SnBgp4GenMaxAggregateAddresses_Type = Integer32
_SnBgp4GenMaxAggregateAddresses_Object = MibScalar
snBgp4GenMaxAggregateAddresses = _SnBgp4GenMaxAggregateAddresses_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 20),
    _SnBgp4GenMaxAggregateAddresses_Type()
)
snBgp4GenMaxAggregateAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxAggregateAddresses.setStatus("mandatory")
_SnBgp4GenMaxAsPathFilters_Type = Integer32
_SnBgp4GenMaxAsPathFilters_Object = MibScalar
snBgp4GenMaxAsPathFilters = _SnBgp4GenMaxAsPathFilters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 21),
    _SnBgp4GenMaxAsPathFilters_Type()
)
snBgp4GenMaxAsPathFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxAsPathFilters.setStatus("mandatory")
_SnBgp4GenMaxCommunityFilters_Type = Integer32
_SnBgp4GenMaxCommunityFilters_Object = MibScalar
snBgp4GenMaxCommunityFilters = _SnBgp4GenMaxCommunityFilters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 22),
    _SnBgp4GenMaxCommunityFilters_Type()
)
snBgp4GenMaxCommunityFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxCommunityFilters.setStatus("mandatory")
_SnBgp4GenMaxNetworks_Type = Integer32
_SnBgp4GenMaxNetworks_Object = MibScalar
snBgp4GenMaxNetworks = _SnBgp4GenMaxNetworks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 23),
    _SnBgp4GenMaxNetworks_Type()
)
snBgp4GenMaxNetworks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxNetworks.setStatus("mandatory")
_SnBgp4GenMaxRouteMapFilters_Type = Integer32
_SnBgp4GenMaxRouteMapFilters_Object = MibScalar
snBgp4GenMaxRouteMapFilters = _SnBgp4GenMaxRouteMapFilters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 24),
    _SnBgp4GenMaxRouteMapFilters_Type()
)
snBgp4GenMaxRouteMapFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenMaxRouteMapFilters.setStatus("mandatory")
_SnBgp4GenNeighPrefixMinValue_Type = Integer32
_SnBgp4GenNeighPrefixMinValue_Object = MibScalar
snBgp4GenNeighPrefixMinValue = _SnBgp4GenNeighPrefixMinValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 25),
    _SnBgp4GenNeighPrefixMinValue_Type()
)
snBgp4GenNeighPrefixMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenNeighPrefixMinValue.setStatus("mandatory")
_SnBgp4GenOperNeighbors_Type = Integer32
_SnBgp4GenOperNeighbors_Object = MibScalar
snBgp4GenOperNeighbors = _SnBgp4GenOperNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 26),
    _SnBgp4GenOperNeighbors_Type()
)
snBgp4GenOperNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenOperNeighbors.setStatus("mandatory")
_SnBgp4GenOperRoutes_Type = Integer32
_SnBgp4GenOperRoutes_Object = MibScalar
snBgp4GenOperRoutes = _SnBgp4GenOperRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 27),
    _SnBgp4GenOperRoutes_Type()
)
snBgp4GenOperRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenOperRoutes.setStatus("mandatory")


class _SnBgp4GenLocalAs_Type(Integer32):
    """Custom type snBgp4GenLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnBgp4GenLocalAs_Type.__name__ = "Integer32"
_SnBgp4GenLocalAs_Object = MibScalar
snBgp4GenLocalAs = _SnBgp4GenLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 28),
    _SnBgp4GenLocalAs_Type()
)
snBgp4GenLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenLocalAs.setStatus("mandatory")
_SnBgp4GenRoutesInstalled_Type = Integer32
_SnBgp4GenRoutesInstalled_Object = MibScalar
snBgp4GenRoutesInstalled = _SnBgp4GenRoutesInstalled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 29),
    _SnBgp4GenRoutesInstalled_Type()
)
snBgp4GenRoutesInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenRoutesInstalled.setStatus("mandatory")
_SnBgp4GenAsPathInstalled_Type = Integer32
_SnBgp4GenAsPathInstalled_Object = MibScalar
snBgp4GenAsPathInstalled = _SnBgp4GenAsPathInstalled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 30),
    _SnBgp4GenAsPathInstalled_Type()
)
snBgp4GenAsPathInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenAsPathInstalled.setStatus("mandatory")


class _SnBgp4ExternalDistance_Type(Integer32):
    """Custom type snBgp4ExternalDistance based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnBgp4ExternalDistance_Type.__name__ = "Integer32"
_SnBgp4ExternalDistance_Object = MibScalar
snBgp4ExternalDistance = _SnBgp4ExternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 31),
    _SnBgp4ExternalDistance_Type()
)
snBgp4ExternalDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4ExternalDistance.setStatus("mandatory")


class _SnBgp4InternalDistance_Type(Integer32):
    """Custom type snBgp4InternalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnBgp4InternalDistance_Type.__name__ = "Integer32"
_SnBgp4InternalDistance_Object = MibScalar
snBgp4InternalDistance = _SnBgp4InternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 32),
    _SnBgp4InternalDistance_Type()
)
snBgp4InternalDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4InternalDistance.setStatus("mandatory")


class _SnBgp4LocalDistance_Type(Integer32):
    """Custom type snBgp4LocalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnBgp4LocalDistance_Type.__name__ = "Integer32"
_SnBgp4LocalDistance_Object = MibScalar
snBgp4LocalDistance = _SnBgp4LocalDistance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 33),
    _SnBgp4LocalDistance_Type()
)
snBgp4LocalDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4LocalDistance.setStatus("mandatory")
_SnBgp4OperNumOfAttributes_Type = Integer32
_SnBgp4OperNumOfAttributes_Object = MibScalar
snBgp4OperNumOfAttributes = _SnBgp4OperNumOfAttributes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 34),
    _SnBgp4OperNumOfAttributes_Type()
)
snBgp4OperNumOfAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4OperNumOfAttributes.setStatus("mandatory")


class _SnBgp4NextBootMaxAttributes_Type(Integer32):
    """Custom type snBgp4NextBootMaxAttributes based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 30000),
    )


_SnBgp4NextBootMaxAttributes_Type.__name__ = "Integer32"
_SnBgp4NextBootMaxAttributes_Object = MibScalar
snBgp4NextBootMaxAttributes = _SnBgp4NextBootMaxAttributes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 35),
    _SnBgp4NextBootMaxAttributes_Type()
)
snBgp4NextBootMaxAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NextBootMaxAttributes.setStatus("mandatory")
_SnBgp4ClusterId_Type = Integer32
_SnBgp4ClusterId_Object = MibScalar
snBgp4ClusterId = _SnBgp4ClusterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 36),
    _SnBgp4ClusterId_Type()
)
snBgp4ClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4ClusterId.setStatus("mandatory")


class _SnBgp4ClientToClientReflection_Type(Integer32):
    """Custom type snBgp4ClientToClientReflection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4ClientToClientReflection_Type.__name__ = "Integer32"
_SnBgp4ClientToClientReflection_Object = MibScalar
snBgp4ClientToClientReflection = _SnBgp4ClientToClientReflection_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 37),
    _SnBgp4ClientToClientReflection_Type()
)
snBgp4ClientToClientReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4ClientToClientReflection.setStatus("mandatory")
_SnBgp4GenTotalNeighbors_Type = Integer32
_SnBgp4GenTotalNeighbors_Object = MibScalar
snBgp4GenTotalNeighbors = _SnBgp4GenTotalNeighbors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 38),
    _SnBgp4GenTotalNeighbors_Type()
)
snBgp4GenTotalNeighbors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4GenTotalNeighbors.setStatus("mandatory")


class _SnBgp4GenMaxPaths_Type(Integer32):
    """Custom type snBgp4GenMaxPaths based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnBgp4GenMaxPaths_Type.__name__ = "Integer32"
_SnBgp4GenMaxPaths_Object = MibScalar
snBgp4GenMaxPaths = _SnBgp4GenMaxPaths_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 39),
    _SnBgp4GenMaxPaths_Type()
)
snBgp4GenMaxPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenMaxPaths.setStatus("mandatory")


class _SnBgp4GenConfedId_Type(Integer32):
    """Custom type snBgp4GenConfedId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnBgp4GenConfedId_Type.__name__ = "Integer32"
_SnBgp4GenConfedId_Object = MibScalar
snBgp4GenConfedId = _SnBgp4GenConfedId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 40),
    _SnBgp4GenConfedId_Type()
)
snBgp4GenConfedId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenConfedId.setStatus("mandatory")


class _SnBgp4GenConfedPeers_Type(OctetString):
    """Custom type snBgp4GenConfedPeers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SnBgp4GenConfedPeers_Type.__name__ = "OctetString"
_SnBgp4GenConfedPeers_Object = MibScalar
snBgp4GenConfedPeers = _SnBgp4GenConfedPeers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 1, 41),
    _SnBgp4GenConfedPeers_Type()
)
snBgp4GenConfedPeers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4GenConfedPeers.setStatus("mandatory")
_SnBgp4AddrFilter_ObjectIdentity = ObjectIdentity
snBgp4AddrFilter = _SnBgp4AddrFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2)
)
_SnBgp4AddrFilterTable_Object = MibTable
snBgp4AddrFilterTable = _SnBgp4AddrFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1)
)
if mibBuilder.loadTexts:
    snBgp4AddrFilterTable.setStatus("mandatory")
_SnBgp4AddrFilterEntry_Object = MibTableRow
snBgp4AddrFilterEntry = _SnBgp4AddrFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1)
)
snBgp4AddrFilterEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4AddrFilterIndex"),
)
if mibBuilder.loadTexts:
    snBgp4AddrFilterEntry.setStatus("mandatory")
_SnBgp4AddrFilterIndex_Type = Integer32
_SnBgp4AddrFilterIndex_Object = MibTableColumn
snBgp4AddrFilterIndex = _SnBgp4AddrFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1, 1),
    _SnBgp4AddrFilterIndex_Type()
)
snBgp4AddrFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AddrFilterIndex.setStatus("mandatory")


class _SnBgp4AddrFilterAction_Type(Integer32):
    """Custom type snBgp4AddrFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnBgp4AddrFilterAction_Type.__name__ = "Integer32"
_SnBgp4AddrFilterAction_Object = MibTableColumn
snBgp4AddrFilterAction = _SnBgp4AddrFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1, 2),
    _SnBgp4AddrFilterAction_Type()
)
snBgp4AddrFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AddrFilterAction.setStatus("mandatory")
_SnBgp4AddrFilterSourceIp_Type = IpAddress
_SnBgp4AddrFilterSourceIp_Object = MibTableColumn
snBgp4AddrFilterSourceIp = _SnBgp4AddrFilterSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1, 3),
    _SnBgp4AddrFilterSourceIp_Type()
)
snBgp4AddrFilterSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AddrFilterSourceIp.setStatus("mandatory")
_SnBgp4AddrFilterSourceMask_Type = IpAddress
_SnBgp4AddrFilterSourceMask_Object = MibTableColumn
snBgp4AddrFilterSourceMask = _SnBgp4AddrFilterSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1, 4),
    _SnBgp4AddrFilterSourceMask_Type()
)
snBgp4AddrFilterSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AddrFilterSourceMask.setStatus("mandatory")
_SnBgp4AddrFilterDestIp_Type = IpAddress
_SnBgp4AddrFilterDestIp_Object = MibTableColumn
snBgp4AddrFilterDestIp = _SnBgp4AddrFilterDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1, 5),
    _SnBgp4AddrFilterDestIp_Type()
)
snBgp4AddrFilterDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AddrFilterDestIp.setStatus("mandatory")
_SnBgp4AddrFilterDestMask_Type = IpAddress
_SnBgp4AddrFilterDestMask_Object = MibTableColumn
snBgp4AddrFilterDestMask = _SnBgp4AddrFilterDestMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1, 6),
    _SnBgp4AddrFilterDestMask_Type()
)
snBgp4AddrFilterDestMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AddrFilterDestMask.setStatus("mandatory")


class _SnBgp4AddrFilterRowStatus_Type(Integer32):
    """Custom type snBgp4AddrFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4AddrFilterRowStatus_Type.__name__ = "Integer32"
_SnBgp4AddrFilterRowStatus_Object = MibTableColumn
snBgp4AddrFilterRowStatus = _SnBgp4AddrFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 2, 1, 1, 7),
    _SnBgp4AddrFilterRowStatus_Type()
)
snBgp4AddrFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AddrFilterRowStatus.setStatus("mandatory")
_SnBgp4AggregateAddr_ObjectIdentity = ObjectIdentity
snBgp4AggregateAddr = _SnBgp4AggregateAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3)
)
_SnBgp4AggregateAddrTable_Object = MibTable
snBgp4AggregateAddrTable = _SnBgp4AggregateAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3, 1)
)
if mibBuilder.loadTexts:
    snBgp4AggregateAddrTable.setStatus("mandatory")
_SnBgp4AggregateAddrEntry_Object = MibTableRow
snBgp4AggregateAddrEntry = _SnBgp4AggregateAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3, 1, 1)
)
snBgp4AggregateAddrEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4AggregateAddrIp"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4AggregateAddrMask"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4AggregateAddrOption"),
)
if mibBuilder.loadTexts:
    snBgp4AggregateAddrEntry.setStatus("mandatory")
_SnBgp4AggregateAddrIp_Type = IpAddress
_SnBgp4AggregateAddrIp_Object = MibTableColumn
snBgp4AggregateAddrIp = _SnBgp4AggregateAddrIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3, 1, 1, 1),
    _SnBgp4AggregateAddrIp_Type()
)
snBgp4AggregateAddrIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AggregateAddrIp.setStatus("mandatory")
_SnBgp4AggregateAddrMask_Type = IpAddress
_SnBgp4AggregateAddrMask_Object = MibTableColumn
snBgp4AggregateAddrMask = _SnBgp4AggregateAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3, 1, 1, 2),
    _SnBgp4AggregateAddrMask_Type()
)
snBgp4AggregateAddrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AggregateAddrMask.setStatus("mandatory")


class _SnBgp4AggregateAddrOption_Type(Integer32):
    """Custom type snBgp4AggregateAddrOption based on Integer32"""
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
        *(("address", 1),
          ("advertiseMap", 5),
          ("asSet", 2),
          ("attributeMap", 6),
          ("summaryOnly", 3),
          ("suppressMap", 4))
    )


_SnBgp4AggregateAddrOption_Type.__name__ = "Integer32"
_SnBgp4AggregateAddrOption_Object = MibTableColumn
snBgp4AggregateAddrOption = _SnBgp4AggregateAddrOption_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3, 1, 1, 3),
    _SnBgp4AggregateAddrOption_Type()
)
snBgp4AggregateAddrOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AggregateAddrOption.setStatus("mandatory")


class _SnBgp4AggregateAddrMap_Type(OctetString):
    """Custom type snBgp4AggregateAddrMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4AggregateAddrMap_Type.__name__ = "OctetString"
_SnBgp4AggregateAddrMap_Object = MibTableColumn
snBgp4AggregateAddrMap = _SnBgp4AggregateAddrMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3, 1, 1, 4),
    _SnBgp4AggregateAddrMap_Type()
)
snBgp4AggregateAddrMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AggregateAddrMap.setStatus("mandatory")


class _SnBgp4AggregateAddrRowStatus_Type(Integer32):
    """Custom type snBgp4AggregateAddrRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4AggregateAddrRowStatus_Type.__name__ = "Integer32"
_SnBgp4AggregateAddrRowStatus_Object = MibTableColumn
snBgp4AggregateAddrRowStatus = _SnBgp4AggregateAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 3, 1, 1, 5),
    _SnBgp4AggregateAddrRowStatus_Type()
)
snBgp4AggregateAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AggregateAddrRowStatus.setStatus("mandatory")
_SnBgp4AsPathFilter_ObjectIdentity = ObjectIdentity
snBgp4AsPathFilter = _SnBgp4AsPathFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 4)
)
_SnBgp4AsPathFilterTable_Object = MibTable
snBgp4AsPathFilterTable = _SnBgp4AsPathFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 4, 1)
)
if mibBuilder.loadTexts:
    snBgp4AsPathFilterTable.setStatus("mandatory")
_SnBgp4AsPathFilterEntry_Object = MibTableRow
snBgp4AsPathFilterEntry = _SnBgp4AsPathFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 4, 1, 1)
)
snBgp4AsPathFilterEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4AsPathFilterIndex"),
)
if mibBuilder.loadTexts:
    snBgp4AsPathFilterEntry.setStatus("mandatory")
_SnBgp4AsPathFilterIndex_Type = Integer32
_SnBgp4AsPathFilterIndex_Object = MibTableColumn
snBgp4AsPathFilterIndex = _SnBgp4AsPathFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 4, 1, 1, 1),
    _SnBgp4AsPathFilterIndex_Type()
)
snBgp4AsPathFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AsPathFilterIndex.setStatus("mandatory")


class _SnBgp4AsPathFilterAction_Type(Integer32):
    """Custom type snBgp4AsPathFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnBgp4AsPathFilterAction_Type.__name__ = "Integer32"
_SnBgp4AsPathFilterAction_Object = MibTableColumn
snBgp4AsPathFilterAction = _SnBgp4AsPathFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 4, 1, 1, 2),
    _SnBgp4AsPathFilterAction_Type()
)
snBgp4AsPathFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AsPathFilterAction.setStatus("mandatory")


class _SnBgp4AsPathFilterRegExpression_Type(OctetString):
    """Custom type snBgp4AsPathFilterRegExpression based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SnBgp4AsPathFilterRegExpression_Type.__name__ = "OctetString"
_SnBgp4AsPathFilterRegExpression_Object = MibTableColumn
snBgp4AsPathFilterRegExpression = _SnBgp4AsPathFilterRegExpression_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 4, 1, 1, 3),
    _SnBgp4AsPathFilterRegExpression_Type()
)
snBgp4AsPathFilterRegExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AsPathFilterRegExpression.setStatus("mandatory")


class _SnBgp4AsPathFilterRowStatus_Type(Integer32):
    """Custom type snBgp4AsPathFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4AsPathFilterRowStatus_Type.__name__ = "Integer32"
_SnBgp4AsPathFilterRowStatus_Object = MibTableColumn
snBgp4AsPathFilterRowStatus = _SnBgp4AsPathFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 4, 1, 1, 4),
    _SnBgp4AsPathFilterRowStatus_Type()
)
snBgp4AsPathFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4AsPathFilterRowStatus.setStatus("mandatory")
_SnBgp4CommunityFilter_ObjectIdentity = ObjectIdentity
snBgp4CommunityFilter = _SnBgp4CommunityFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5)
)
_SnBgp4CommunityFilterTable_Object = MibTable
snBgp4CommunityFilterTable = _SnBgp4CommunityFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1)
)
if mibBuilder.loadTexts:
    snBgp4CommunityFilterTable.setStatus("mandatory")
_SnBgp4CommunityFilterEntry_Object = MibTableRow
snBgp4CommunityFilterEntry = _SnBgp4CommunityFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1)
)
snBgp4CommunityFilterEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4CommunityFilterIndex"),
)
if mibBuilder.loadTexts:
    snBgp4CommunityFilterEntry.setStatus("mandatory")
_SnBgp4CommunityFilterIndex_Type = Integer32
_SnBgp4CommunityFilterIndex_Object = MibTableColumn
snBgp4CommunityFilterIndex = _SnBgp4CommunityFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 1),
    _SnBgp4CommunityFilterIndex_Type()
)
snBgp4CommunityFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterIndex.setStatus("mandatory")


class _SnBgp4CommunityFilterAction_Type(Integer32):
    """Custom type snBgp4CommunityFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnBgp4CommunityFilterAction_Type.__name__ = "Integer32"
_SnBgp4CommunityFilterAction_Object = MibTableColumn
snBgp4CommunityFilterAction = _SnBgp4CommunityFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 2),
    _SnBgp4CommunityFilterAction_Type()
)
snBgp4CommunityFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterAction.setStatus("mandatory")


class _SnBgp4CommunityFilterCommNum_Type(OctetString):
    """Custom type snBgp4CommunityFilterCommNum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SnBgp4CommunityFilterCommNum_Type.__name__ = "OctetString"
_SnBgp4CommunityFilterCommNum_Object = MibTableColumn
snBgp4CommunityFilterCommNum = _SnBgp4CommunityFilterCommNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 3),
    _SnBgp4CommunityFilterCommNum_Type()
)
snBgp4CommunityFilterCommNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterCommNum.setStatus("mandatory")


class _SnBgp4CommunityFilterInternet_Type(Integer32):
    """Custom type snBgp4CommunityFilterInternet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4CommunityFilterInternet_Type.__name__ = "Integer32"
_SnBgp4CommunityFilterInternet_Object = MibTableColumn
snBgp4CommunityFilterInternet = _SnBgp4CommunityFilterInternet_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 4),
    _SnBgp4CommunityFilterInternet_Type()
)
snBgp4CommunityFilterInternet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterInternet.setStatus("mandatory")


class _SnBgp4CommunityFilterNoAdvertise_Type(Integer32):
    """Custom type snBgp4CommunityFilterNoAdvertise based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnBgp4CommunityFilterNoAdvertise_Type.__name__ = "Integer32"
_SnBgp4CommunityFilterNoAdvertise_Object = MibTableColumn
snBgp4CommunityFilterNoAdvertise = _SnBgp4CommunityFilterNoAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 5),
    _SnBgp4CommunityFilterNoAdvertise_Type()
)
snBgp4CommunityFilterNoAdvertise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterNoAdvertise.setStatus("mandatory")


class _SnBgp4CommunityFilterNoExport_Type(Integer32):
    """Custom type snBgp4CommunityFilterNoExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnBgp4CommunityFilterNoExport_Type.__name__ = "Integer32"
_SnBgp4CommunityFilterNoExport_Object = MibTableColumn
snBgp4CommunityFilterNoExport = _SnBgp4CommunityFilterNoExport_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 6),
    _SnBgp4CommunityFilterNoExport_Type()
)
snBgp4CommunityFilterNoExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterNoExport.setStatus("mandatory")


class _SnBgp4CommunityFilterRowStatus_Type(Integer32):
    """Custom type snBgp4CommunityFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4CommunityFilterRowStatus_Type.__name__ = "Integer32"
_SnBgp4CommunityFilterRowStatus_Object = MibTableColumn
snBgp4CommunityFilterRowStatus = _SnBgp4CommunityFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 7),
    _SnBgp4CommunityFilterRowStatus_Type()
)
snBgp4CommunityFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterRowStatus.setStatus("mandatory")


class _SnBgp4CommunityFilterLocalAs_Type(Integer32):
    """Custom type snBgp4CommunityFilterLocalAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnBgp4CommunityFilterLocalAs_Type.__name__ = "Integer32"
_SnBgp4CommunityFilterLocalAs_Object = MibTableColumn
snBgp4CommunityFilterLocalAs = _SnBgp4CommunityFilterLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 5, 1, 1, 8),
    _SnBgp4CommunityFilterLocalAs_Type()
)
snBgp4CommunityFilterLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4CommunityFilterLocalAs.setStatus("mandatory")
_SnBgp4NeighGenCfg_ObjectIdentity = ObjectIdentity
snBgp4NeighGenCfg = _SnBgp4NeighGenCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6)
)
_SnBgp4NeighGenCfgTable_Object = MibTable
snBgp4NeighGenCfgTable = _SnBgp4NeighGenCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1)
)
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgTable.setStatus("mandatory")
_SnBgp4NeighGenCfgEntry_Object = MibTableRow
snBgp4NeighGenCfgEntry = _SnBgp4NeighGenCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1)
)
snBgp4NeighGenCfgEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighGenCfgNeighIp"),
)
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgEntry.setStatus("mandatory")
_SnBgp4NeighGenCfgNeighIp_Type = IpAddress
_SnBgp4NeighGenCfgNeighIp_Object = MibTableColumn
snBgp4NeighGenCfgNeighIp = _SnBgp4NeighGenCfgNeighIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 1),
    _SnBgp4NeighGenCfgNeighIp_Type()
)
snBgp4NeighGenCfgNeighIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgNeighIp.setStatus("mandatory")


class _SnBgp4NeighGenCfgAdvertlevel_Type(Integer32):
    """Custom type snBgp4NeighGenCfgAdvertlevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_SnBgp4NeighGenCfgAdvertlevel_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgAdvertlevel_Object = MibTableColumn
snBgp4NeighGenCfgAdvertlevel = _SnBgp4NeighGenCfgAdvertlevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 2),
    _SnBgp4NeighGenCfgAdvertlevel_Type()
)
snBgp4NeighGenCfgAdvertlevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgAdvertlevel.setStatus("mandatory")


class _SnBgp4NeighGenCfgDefOriginate_Type(Integer32):
    """Custom type snBgp4NeighGenCfgDefOriginate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NeighGenCfgDefOriginate_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgDefOriginate_Object = MibTableColumn
snBgp4NeighGenCfgDefOriginate = _SnBgp4NeighGenCfgDefOriginate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 3),
    _SnBgp4NeighGenCfgDefOriginate_Type()
)
snBgp4NeighGenCfgDefOriginate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgDefOriginate.setStatus("mandatory")


class _SnBgp4NeighGenCfgEbgpMultihop_Type(Integer32):
    """Custom type snBgp4NeighGenCfgEbgpMultihop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NeighGenCfgEbgpMultihop_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgEbgpMultihop_Object = MibTableColumn
snBgp4NeighGenCfgEbgpMultihop = _SnBgp4NeighGenCfgEbgpMultihop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 4),
    _SnBgp4NeighGenCfgEbgpMultihop_Type()
)
snBgp4NeighGenCfgEbgpMultihop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgEbgpMultihop.setStatus("mandatory")
_SnBgp4NeighGenCfgMaxPrefix_Type = Integer32
_SnBgp4NeighGenCfgMaxPrefix_Object = MibTableColumn
snBgp4NeighGenCfgMaxPrefix = _SnBgp4NeighGenCfgMaxPrefix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 5),
    _SnBgp4NeighGenCfgMaxPrefix_Type()
)
snBgp4NeighGenCfgMaxPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgMaxPrefix.setStatus("mandatory")


class _SnBgp4NeighGenCfgNextHopSelf_Type(Integer32):
    """Custom type snBgp4NeighGenCfgNextHopSelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NeighGenCfgNextHopSelf_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgNextHopSelf_Object = MibTableColumn
snBgp4NeighGenCfgNextHopSelf = _SnBgp4NeighGenCfgNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 6),
    _SnBgp4NeighGenCfgNextHopSelf_Type()
)
snBgp4NeighGenCfgNextHopSelf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgNextHopSelf.setStatus("mandatory")


class _SnBgp4NeighGenCfgRemoteAs_Type(Integer32):
    """Custom type snBgp4NeighGenCfgRemoteAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnBgp4NeighGenCfgRemoteAs_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgRemoteAs_Object = MibTableColumn
snBgp4NeighGenCfgRemoteAs = _SnBgp4NeighGenCfgRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 7),
    _SnBgp4NeighGenCfgRemoteAs_Type()
)
snBgp4NeighGenCfgRemoteAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgRemoteAs.setStatus("mandatory")


class _SnBgp4NeighGenCfgSendComm_Type(Integer32):
    """Custom type snBgp4NeighGenCfgSendComm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NeighGenCfgSendComm_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgSendComm_Object = MibTableColumn
snBgp4NeighGenCfgSendComm = _SnBgp4NeighGenCfgSendComm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 8),
    _SnBgp4NeighGenCfgSendComm_Type()
)
snBgp4NeighGenCfgSendComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgSendComm.setStatus("mandatory")


class _SnBgp4NeighGenCfgWeight_Type(Integer32):
    """Custom type snBgp4NeighGenCfgWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4NeighGenCfgWeight_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgWeight_Object = MibTableColumn
snBgp4NeighGenCfgWeight = _SnBgp4NeighGenCfgWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 9),
    _SnBgp4NeighGenCfgWeight_Type()
)
snBgp4NeighGenCfgWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgWeight.setStatus("mandatory")


class _SnBgp4NeighGenCfgWeightFilterList_Type(OctetString):
    """Custom type snBgp4NeighGenCfgWeightFilterList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4NeighGenCfgWeightFilterList_Type.__name__ = "OctetString"
_SnBgp4NeighGenCfgWeightFilterList_Object = MibTableColumn
snBgp4NeighGenCfgWeightFilterList = _SnBgp4NeighGenCfgWeightFilterList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 10),
    _SnBgp4NeighGenCfgWeightFilterList_Type()
)
snBgp4NeighGenCfgWeightFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgWeightFilterList.setStatus("mandatory")


class _SnBgp4NeighGenCfgRowStatus_Type(Integer32):
    """Custom type snBgp4NeighGenCfgRowStatus based on Integer32"""
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
        *(("applyDefault", 6),
          ("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4NeighGenCfgRowStatus_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgRowStatus_Object = MibTableColumn
snBgp4NeighGenCfgRowStatus = _SnBgp4NeighGenCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 11),
    _SnBgp4NeighGenCfgRowStatus_Type()
)
snBgp4NeighGenCfgRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgRowStatus.setStatus("mandatory")


class _SnBgp4NeighGenCfgUpdateSrcLpbIntf_Type(Integer32):
    """Custom type snBgp4NeighGenCfgUpdateSrcLpbIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_SnBgp4NeighGenCfgUpdateSrcLpbIntf_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgUpdateSrcLpbIntf_Object = MibTableColumn
snBgp4NeighGenCfgUpdateSrcLpbIntf = _SnBgp4NeighGenCfgUpdateSrcLpbIntf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 12),
    _SnBgp4NeighGenCfgUpdateSrcLpbIntf_Type()
)
snBgp4NeighGenCfgUpdateSrcLpbIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgUpdateSrcLpbIntf.setStatus("mandatory")


class _SnBgp4NeighGenCfgRouteRefClient_Type(Integer32):
    """Custom type snBgp4NeighGenCfgRouteRefClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NeighGenCfgRouteRefClient_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgRouteRefClient_Object = MibTableColumn
snBgp4NeighGenCfgRouteRefClient = _SnBgp4NeighGenCfgRouteRefClient_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 13),
    _SnBgp4NeighGenCfgRouteRefClient_Type()
)
snBgp4NeighGenCfgRouteRefClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgRouteRefClient.setStatus("mandatory")


class _SnBgp4NeighGenCfgRemovePrivateAs_Type(Integer32):
    """Custom type snBgp4NeighGenCfgRemovePrivateAs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NeighGenCfgRemovePrivateAs_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgRemovePrivateAs_Object = MibTableColumn
snBgp4NeighGenCfgRemovePrivateAs = _SnBgp4NeighGenCfgRemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 14),
    _SnBgp4NeighGenCfgRemovePrivateAs_Type()
)
snBgp4NeighGenCfgRemovePrivateAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgRemovePrivateAs.setStatus("mandatory")


class _SnBgp4NeighGenCfgEbgpMultihopTtl_Type(Integer32):
    """Custom type snBgp4NeighGenCfgEbgpMultihopTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnBgp4NeighGenCfgEbgpMultihopTtl_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgEbgpMultihopTtl_Object = MibTableColumn
snBgp4NeighGenCfgEbgpMultihopTtl = _SnBgp4NeighGenCfgEbgpMultihopTtl_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 15),
    _SnBgp4NeighGenCfgEbgpMultihopTtl_Type()
)
snBgp4NeighGenCfgEbgpMultihopTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgEbgpMultihopTtl.setStatus("mandatory")


class _SnBgp4NeighGenCfgShutdown_Type(Integer32):
    """Custom type snBgp4NeighGenCfgShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NeighGenCfgShutdown_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgShutdown_Object = MibTableColumn
snBgp4NeighGenCfgShutdown = _SnBgp4NeighGenCfgShutdown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 16),
    _SnBgp4NeighGenCfgShutdown_Type()
)
snBgp4NeighGenCfgShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgShutdown.setStatus("mandatory")


class _SnBgp4NeighGenCfgKeepAliveTime_Type(Integer32):
    """Custom type snBgp4NeighGenCfgKeepAliveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4NeighGenCfgKeepAliveTime_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgKeepAliveTime_Object = MibTableColumn
snBgp4NeighGenCfgKeepAliveTime = _SnBgp4NeighGenCfgKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 17),
    _SnBgp4NeighGenCfgKeepAliveTime_Type()
)
snBgp4NeighGenCfgKeepAliveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgKeepAliveTime.setStatus("mandatory")


class _SnBgp4NeighGenCfgHoldTime_Type(Integer32):
    """Custom type snBgp4NeighGenCfgHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4NeighGenCfgHoldTime_Type.__name__ = "Integer32"
_SnBgp4NeighGenCfgHoldTime_Object = MibTableColumn
snBgp4NeighGenCfgHoldTime = _SnBgp4NeighGenCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 6, 1, 1, 18),
    _SnBgp4NeighGenCfgHoldTime_Type()
)
snBgp4NeighGenCfgHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighGenCfgHoldTime.setStatus("mandatory")
_SnBgp4NeighDistGroup_ObjectIdentity = ObjectIdentity
snBgp4NeighDistGroup = _SnBgp4NeighDistGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 7)
)
_SnBgp4NeighDistGroupTable_Object = MibTable
snBgp4NeighDistGroupTable = _SnBgp4NeighDistGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 7, 1)
)
if mibBuilder.loadTexts:
    snBgp4NeighDistGroupTable.setStatus("mandatory")
_SnBgp4NeighDistGroupEntry_Object = MibTableRow
snBgp4NeighDistGroupEntry = _SnBgp4NeighDistGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 7, 1, 1)
)
snBgp4NeighDistGroupEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighDistGroupNeighIp"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighDistGroupDir"),
)
if mibBuilder.loadTexts:
    snBgp4NeighDistGroupEntry.setStatus("mandatory")
_SnBgp4NeighDistGroupNeighIp_Type = IpAddress
_SnBgp4NeighDistGroupNeighIp_Object = MibTableColumn
snBgp4NeighDistGroupNeighIp = _SnBgp4NeighDistGroupNeighIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 7, 1, 1, 1),
    _SnBgp4NeighDistGroupNeighIp_Type()
)
snBgp4NeighDistGroupNeighIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighDistGroupNeighIp.setStatus("mandatory")


class _SnBgp4NeighDistGroupDir_Type(Integer32):
    """Custom type snBgp4NeighDistGroupDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 0))
    )


_SnBgp4NeighDistGroupDir_Type.__name__ = "Integer32"
_SnBgp4NeighDistGroupDir_Object = MibTableColumn
snBgp4NeighDistGroupDir = _SnBgp4NeighDistGroupDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 7, 1, 1, 2),
    _SnBgp4NeighDistGroupDir_Type()
)
snBgp4NeighDistGroupDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighDistGroupDir.setStatus("mandatory")


class _SnBgp4NeighDistGroupAccessList_Type(OctetString):
    """Custom type snBgp4NeighDistGroupAccessList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4NeighDistGroupAccessList_Type.__name__ = "OctetString"
_SnBgp4NeighDistGroupAccessList_Object = MibTableColumn
snBgp4NeighDistGroupAccessList = _SnBgp4NeighDistGroupAccessList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 7, 1, 1, 3),
    _SnBgp4NeighDistGroupAccessList_Type()
)
snBgp4NeighDistGroupAccessList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighDistGroupAccessList.setStatus("mandatory")


class _SnBgp4NeighDistGroupRowStatus_Type(Integer32):
    """Custom type snBgp4NeighDistGroupRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4NeighDistGroupRowStatus_Type.__name__ = "Integer32"
_SnBgp4NeighDistGroupRowStatus_Object = MibTableColumn
snBgp4NeighDistGroupRowStatus = _SnBgp4NeighDistGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 7, 1, 1, 4),
    _SnBgp4NeighDistGroupRowStatus_Type()
)
snBgp4NeighDistGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighDistGroupRowStatus.setStatus("mandatory")
_SnBgp4NeighFilterGroup_ObjectIdentity = ObjectIdentity
snBgp4NeighFilterGroup = _SnBgp4NeighFilterGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 8)
)
_SnBgp4NeighFilterGroupTable_Object = MibTable
snBgp4NeighFilterGroupTable = _SnBgp4NeighFilterGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 8, 1)
)
if mibBuilder.loadTexts:
    snBgp4NeighFilterGroupTable.setStatus("mandatory")
_SnBgp4NeighFilterGroupEntry_Object = MibTableRow
snBgp4NeighFilterGroupEntry = _SnBgp4NeighFilterGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 8, 1, 1)
)
snBgp4NeighFilterGroupEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighFilterGroupNeighIp"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighFilterGroupDir"),
)
if mibBuilder.loadTexts:
    snBgp4NeighFilterGroupEntry.setStatus("mandatory")
_SnBgp4NeighFilterGroupNeighIp_Type = IpAddress
_SnBgp4NeighFilterGroupNeighIp_Object = MibTableColumn
snBgp4NeighFilterGroupNeighIp = _SnBgp4NeighFilterGroupNeighIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 8, 1, 1, 1),
    _SnBgp4NeighFilterGroupNeighIp_Type()
)
snBgp4NeighFilterGroupNeighIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighFilterGroupNeighIp.setStatus("mandatory")


class _SnBgp4NeighFilterGroupDir_Type(Integer32):
    """Custom type snBgp4NeighFilterGroupDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 0))
    )


_SnBgp4NeighFilterGroupDir_Type.__name__ = "Integer32"
_SnBgp4NeighFilterGroupDir_Object = MibTableColumn
snBgp4NeighFilterGroupDir = _SnBgp4NeighFilterGroupDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 8, 1, 1, 2),
    _SnBgp4NeighFilterGroupDir_Type()
)
snBgp4NeighFilterGroupDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighFilterGroupDir.setStatus("mandatory")


class _SnBgp4NeighFilterGroupAccessList_Type(OctetString):
    """Custom type snBgp4NeighFilterGroupAccessList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4NeighFilterGroupAccessList_Type.__name__ = "OctetString"
_SnBgp4NeighFilterGroupAccessList_Object = MibTableColumn
snBgp4NeighFilterGroupAccessList = _SnBgp4NeighFilterGroupAccessList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 8, 1, 1, 3),
    _SnBgp4NeighFilterGroupAccessList_Type()
)
snBgp4NeighFilterGroupAccessList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighFilterGroupAccessList.setStatus("mandatory")


class _SnBgp4NeighFilterGroupRowStatus_Type(Integer32):
    """Custom type snBgp4NeighFilterGroupRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4NeighFilterGroupRowStatus_Type.__name__ = "Integer32"
_SnBgp4NeighFilterGroupRowStatus_Object = MibTableColumn
snBgp4NeighFilterGroupRowStatus = _SnBgp4NeighFilterGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 8, 1, 1, 4),
    _SnBgp4NeighFilterGroupRowStatus_Type()
)
snBgp4NeighFilterGroupRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighFilterGroupRowStatus.setStatus("mandatory")
_SnBgp4NeighRouteMap_ObjectIdentity = ObjectIdentity
snBgp4NeighRouteMap = _SnBgp4NeighRouteMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 9)
)
_SnBgp4NeighRouteMapTable_Object = MibTable
snBgp4NeighRouteMapTable = _SnBgp4NeighRouteMapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 9, 1)
)
if mibBuilder.loadTexts:
    snBgp4NeighRouteMapTable.setStatus("mandatory")
_SnBgp4NeighRouteMapEntry_Object = MibTableRow
snBgp4NeighRouteMapEntry = _SnBgp4NeighRouteMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 9, 1, 1)
)
snBgp4NeighRouteMapEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighRouteMapNeighIp"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighRouteMapDir"),
)
if mibBuilder.loadTexts:
    snBgp4NeighRouteMapEntry.setStatus("mandatory")
_SnBgp4NeighRouteMapNeighIp_Type = IpAddress
_SnBgp4NeighRouteMapNeighIp_Object = MibTableColumn
snBgp4NeighRouteMapNeighIp = _SnBgp4NeighRouteMapNeighIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 9, 1, 1, 1),
    _SnBgp4NeighRouteMapNeighIp_Type()
)
snBgp4NeighRouteMapNeighIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighRouteMapNeighIp.setStatus("mandatory")


class _SnBgp4NeighRouteMapDir_Type(Integer32):
    """Custom type snBgp4NeighRouteMapDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 0))
    )


_SnBgp4NeighRouteMapDir_Type.__name__ = "Integer32"
_SnBgp4NeighRouteMapDir_Object = MibTableColumn
snBgp4NeighRouteMapDir = _SnBgp4NeighRouteMapDir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 9, 1, 1, 2),
    _SnBgp4NeighRouteMapDir_Type()
)
snBgp4NeighRouteMapDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighRouteMapDir.setStatus("mandatory")


class _SnBgp4NeighRouteMapMapName_Type(OctetString):
    """Custom type snBgp4NeighRouteMapMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4NeighRouteMapMapName_Type.__name__ = "OctetString"
_SnBgp4NeighRouteMapMapName_Object = MibTableColumn
snBgp4NeighRouteMapMapName = _SnBgp4NeighRouteMapMapName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 9, 1, 1, 3),
    _SnBgp4NeighRouteMapMapName_Type()
)
snBgp4NeighRouteMapMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighRouteMapMapName.setStatus("mandatory")


class _SnBgp4NeighRouteMapRowStatus_Type(Integer32):
    """Custom type snBgp4NeighRouteMapRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4NeighRouteMapRowStatus_Type.__name__ = "Integer32"
_SnBgp4NeighRouteMapRowStatus_Object = MibTableColumn
snBgp4NeighRouteMapRowStatus = _SnBgp4NeighRouteMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 9, 1, 1, 4),
    _SnBgp4NeighRouteMapRowStatus_Type()
)
snBgp4NeighRouteMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NeighRouteMapRowStatus.setStatus("mandatory")
_SnBgp4Network_ObjectIdentity = ObjectIdentity
snBgp4Network = _SnBgp4Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10)
)
_SnBgp4NetworkTable_Object = MibTable
snBgp4NetworkTable = _SnBgp4NetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10, 1)
)
if mibBuilder.loadTexts:
    snBgp4NetworkTable.setStatus("mandatory")
_SnBgp4NetworkEntry_Object = MibTableRow
snBgp4NetworkEntry = _SnBgp4NetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10, 1, 1)
)
snBgp4NetworkEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NetworkIp"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NetworkSubnetMask"),
)
if mibBuilder.loadTexts:
    snBgp4NetworkEntry.setStatus("mandatory")
_SnBgp4NetworkIp_Type = IpAddress
_SnBgp4NetworkIp_Object = MibTableColumn
snBgp4NetworkIp = _SnBgp4NetworkIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10, 1, 1, 1),
    _SnBgp4NetworkIp_Type()
)
snBgp4NetworkIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NetworkIp.setStatus("mandatory")
_SnBgp4NetworkSubnetMask_Type = IpAddress
_SnBgp4NetworkSubnetMask_Object = MibTableColumn
snBgp4NetworkSubnetMask = _SnBgp4NetworkSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10, 1, 1, 2),
    _SnBgp4NetworkSubnetMask_Type()
)
snBgp4NetworkSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NetworkSubnetMask.setStatus("mandatory")


class _SnBgp4NetworkWeight_Type(Integer32):
    """Custom type snBgp4NetworkWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4NetworkWeight_Type.__name__ = "Integer32"
_SnBgp4NetworkWeight_Object = MibTableColumn
snBgp4NetworkWeight = _SnBgp4NetworkWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10, 1, 1, 3),
    _SnBgp4NetworkWeight_Type()
)
snBgp4NetworkWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NetworkWeight.setStatus("mandatory")


class _SnBgp4NetworkBackdoor_Type(Integer32):
    """Custom type snBgp4NetworkBackdoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4NetworkBackdoor_Type.__name__ = "Integer32"
_SnBgp4NetworkBackdoor_Object = MibTableColumn
snBgp4NetworkBackdoor = _SnBgp4NetworkBackdoor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10, 1, 1, 4),
    _SnBgp4NetworkBackdoor_Type()
)
snBgp4NetworkBackdoor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NetworkBackdoor.setStatus("mandatory")


class _SnBgp4NetworkRowStatus_Type(Integer32):
    """Custom type snBgp4NetworkRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4NetworkRowStatus_Type.__name__ = "Integer32"
_SnBgp4NetworkRowStatus_Object = MibTableColumn
snBgp4NetworkRowStatus = _SnBgp4NetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 10, 1, 1, 5),
    _SnBgp4NetworkRowStatus_Type()
)
snBgp4NetworkRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4NetworkRowStatus.setStatus("mandatory")
_SnBgp4Redis_ObjectIdentity = ObjectIdentity
snBgp4Redis = _SnBgp4Redis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11)
)
_SnBgp4RedisTable_Object = MibTable
snBgp4RedisTable = _SnBgp4RedisTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1)
)
if mibBuilder.loadTexts:
    snBgp4RedisTable.setStatus("mandatory")
_SnBgp4RedisEntry_Object = MibTableRow
snBgp4RedisEntry = _SnBgp4RedisEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1)
)
snBgp4RedisEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RedisProtocol"),
)
if mibBuilder.loadTexts:
    snBgp4RedisEntry.setStatus("mandatory")


class _SnBgp4RedisProtocol_Type(Integer32):
    """Custom type snBgp4RedisProtocol based on Integer32"""
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
        *(("connected", 4),
          ("ospf", 2),
          ("rip", 1),
          ("static", 3))
    )


_SnBgp4RedisProtocol_Type.__name__ = "Integer32"
_SnBgp4RedisProtocol_Object = MibTableColumn
snBgp4RedisProtocol = _SnBgp4RedisProtocol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 1),
    _SnBgp4RedisProtocol_Type()
)
snBgp4RedisProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RedisProtocol.setStatus("mandatory")
_SnBgp4RedisMetric_Type = Integer32
_SnBgp4RedisMetric_Object = MibTableColumn
snBgp4RedisMetric = _SnBgp4RedisMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 2),
    _SnBgp4RedisMetric_Type()
)
snBgp4RedisMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RedisMetric.setStatus("mandatory")


class _SnBgp4RedisRouteMap_Type(OctetString):
    """Custom type snBgp4RedisRouteMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4RedisRouteMap_Type.__name__ = "OctetString"
_SnBgp4RedisRouteMap_Object = MibTableColumn
snBgp4RedisRouteMap = _SnBgp4RedisRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 3),
    _SnBgp4RedisRouteMap_Type()
)
snBgp4RedisRouteMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RedisRouteMap.setStatus("mandatory")


class _SnBgp4RedisWeight_Type(Integer32):
    """Custom type snBgp4RedisWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4RedisWeight_Type.__name__ = "Integer32"
_SnBgp4RedisWeight_Object = MibTableColumn
snBgp4RedisWeight = _SnBgp4RedisWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 4),
    _SnBgp4RedisWeight_Type()
)
snBgp4RedisWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RedisWeight.setStatus("mandatory")


class _SnBgp4RedisMatchInternal_Type(Integer32):
    """Custom type snBgp4RedisMatchInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4RedisMatchInternal_Type.__name__ = "Integer32"
_SnBgp4RedisMatchInternal_Object = MibTableColumn
snBgp4RedisMatchInternal = _SnBgp4RedisMatchInternal_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 5),
    _SnBgp4RedisMatchInternal_Type()
)
snBgp4RedisMatchInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RedisMatchInternal.setStatus("mandatory")


class _SnBgp4RedisMatchExternal1_Type(Integer32):
    """Custom type snBgp4RedisMatchExternal1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4RedisMatchExternal1_Type.__name__ = "Integer32"
_SnBgp4RedisMatchExternal1_Object = MibTableColumn
snBgp4RedisMatchExternal1 = _SnBgp4RedisMatchExternal1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 6),
    _SnBgp4RedisMatchExternal1_Type()
)
snBgp4RedisMatchExternal1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RedisMatchExternal1.setStatus("mandatory")


class _SnBgp4RedisMatchExternal2_Type(Integer32):
    """Custom type snBgp4RedisMatchExternal2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4RedisMatchExternal2_Type.__name__ = "Integer32"
_SnBgp4RedisMatchExternal2_Object = MibTableColumn
snBgp4RedisMatchExternal2 = _SnBgp4RedisMatchExternal2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 7),
    _SnBgp4RedisMatchExternal2_Type()
)
snBgp4RedisMatchExternal2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RedisMatchExternal2.setStatus("mandatory")


class _SnBgp4RedisRowStatus_Type(Integer32):
    """Custom type snBgp4RedisRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4RedisRowStatus_Type.__name__ = "Integer32"
_SnBgp4RedisRowStatus_Object = MibTableColumn
snBgp4RedisRowStatus = _SnBgp4RedisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 11, 1, 1, 8),
    _SnBgp4RedisRowStatus_Type()
)
snBgp4RedisRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RedisRowStatus.setStatus("mandatory")
_SnBgp4RouteMapFilter_ObjectIdentity = ObjectIdentity
snBgp4RouteMapFilter = _SnBgp4RouteMapFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 12)
)
_SnBgp4RouteMapFilterTable_Object = MibTable
snBgp4RouteMapFilterTable = _SnBgp4RouteMapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 12, 1)
)
if mibBuilder.loadTexts:
    snBgp4RouteMapFilterTable.setStatus("mandatory")
_SnBgp4RouteMapFilterEntry_Object = MibTableRow
snBgp4RouteMapFilterEntry = _SnBgp4RouteMapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 12, 1, 1)
)
snBgp4RouteMapFilterEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RouteMapFilterMapName"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RouteMapFilterSequenceNum"),
)
if mibBuilder.loadTexts:
    snBgp4RouteMapFilterEntry.setStatus("mandatory")


class _SnBgp4RouteMapFilterMapName_Type(OctetString):
    """Custom type snBgp4RouteMapFilterMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4RouteMapFilterMapName_Type.__name__ = "OctetString"
_SnBgp4RouteMapFilterMapName_Object = MibTableColumn
snBgp4RouteMapFilterMapName = _SnBgp4RouteMapFilterMapName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 12, 1, 1, 1),
    _SnBgp4RouteMapFilterMapName_Type()
)
snBgp4RouteMapFilterMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteMapFilterMapName.setStatus("mandatory")
_SnBgp4RouteMapFilterSequenceNum_Type = Integer32
_SnBgp4RouteMapFilterSequenceNum_Object = MibTableColumn
snBgp4RouteMapFilterSequenceNum = _SnBgp4RouteMapFilterSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 12, 1, 1, 2),
    _SnBgp4RouteMapFilterSequenceNum_Type()
)
snBgp4RouteMapFilterSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteMapFilterSequenceNum.setStatus("mandatory")


class _SnBgp4RouteMapFilterAction_Type(Integer32):
    """Custom type snBgp4RouteMapFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1))
    )


_SnBgp4RouteMapFilterAction_Type.__name__ = "Integer32"
_SnBgp4RouteMapFilterAction_Object = MibTableColumn
snBgp4RouteMapFilterAction = _SnBgp4RouteMapFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 12, 1, 1, 3),
    _SnBgp4RouteMapFilterAction_Type()
)
snBgp4RouteMapFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapFilterAction.setStatus("mandatory")


class _SnBgp4RouteMapFilterRowStatus_Type(Integer32):
    """Custom type snBgp4RouteMapFilterRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("invalid", 1),
          ("modify", 5),
          ("valid", 2))
    )


_SnBgp4RouteMapFilterRowStatus_Type.__name__ = "Integer32"
_SnBgp4RouteMapFilterRowStatus_Object = MibTableColumn
snBgp4RouteMapFilterRowStatus = _SnBgp4RouteMapFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 12, 1, 1, 4),
    _SnBgp4RouteMapFilterRowStatus_Type()
)
snBgp4RouteMapFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapFilterRowStatus.setStatus("mandatory")
_SnBgp4RouteMapMatch_ObjectIdentity = ObjectIdentity
snBgp4RouteMapMatch = _SnBgp4RouteMapMatch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13)
)
_SnBgp4RouteMapMatchTable_Object = MibTable
snBgp4RouteMapMatchTable = _SnBgp4RouteMapMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1)
)
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchTable.setStatus("mandatory")
_SnBgp4RouteMapMatchEntry_Object = MibTableRow
snBgp4RouteMapMatchEntry = _SnBgp4RouteMapMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1)
)
snBgp4RouteMapMatchEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RouteMapMatchMapName"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RouteMapMatchSequenceNum"),
)
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchEntry.setStatus("mandatory")


class _SnBgp4RouteMapMatchMapName_Type(OctetString):
    """Custom type snBgp4RouteMapMatchMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4RouteMapMatchMapName_Type.__name__ = "OctetString"
_SnBgp4RouteMapMatchMapName_Object = MibTableColumn
snBgp4RouteMapMatchMapName = _SnBgp4RouteMapMatchMapName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 1),
    _SnBgp4RouteMapMatchMapName_Type()
)
snBgp4RouteMapMatchMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchMapName.setStatus("mandatory")
_SnBgp4RouteMapMatchSequenceNum_Type = Integer32
_SnBgp4RouteMapMatchSequenceNum_Object = MibTableColumn
snBgp4RouteMapMatchSequenceNum = _SnBgp4RouteMapMatchSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 2),
    _SnBgp4RouteMapMatchSequenceNum_Type()
)
snBgp4RouteMapMatchSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchSequenceNum.setStatus("mandatory")


class _SnBgp4RouteMapMatchAsPathFilter_Type(OctetString):
    """Custom type snBgp4RouteMapMatchAsPathFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnBgp4RouteMapMatchAsPathFilter_Type.__name__ = "OctetString"
_SnBgp4RouteMapMatchAsPathFilter_Object = MibTableColumn
snBgp4RouteMapMatchAsPathFilter = _SnBgp4RouteMapMatchAsPathFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 3),
    _SnBgp4RouteMapMatchAsPathFilter_Type()
)
snBgp4RouteMapMatchAsPathFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchAsPathFilter.setStatus("mandatory")


class _SnBgp4RouteMapMatchCommunityFilter_Type(OctetString):
    """Custom type snBgp4RouteMapMatchCommunityFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnBgp4RouteMapMatchCommunityFilter_Type.__name__ = "OctetString"
_SnBgp4RouteMapMatchCommunityFilter_Object = MibTableColumn
snBgp4RouteMapMatchCommunityFilter = _SnBgp4RouteMapMatchCommunityFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 4),
    _SnBgp4RouteMapMatchCommunityFilter_Type()
)
snBgp4RouteMapMatchCommunityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchCommunityFilter.setStatus("mandatory")


class _SnBgp4RouteMapMatchAddressFilter_Type(OctetString):
    """Custom type snBgp4RouteMapMatchAddressFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnBgp4RouteMapMatchAddressFilter_Type.__name__ = "OctetString"
_SnBgp4RouteMapMatchAddressFilter_Object = MibTableColumn
snBgp4RouteMapMatchAddressFilter = _SnBgp4RouteMapMatchAddressFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 5),
    _SnBgp4RouteMapMatchAddressFilter_Type()
)
snBgp4RouteMapMatchAddressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchAddressFilter.setStatus("mandatory")
_SnBgp4RouteMapMatchMetric_Type = Integer32
_SnBgp4RouteMapMatchMetric_Object = MibTableColumn
snBgp4RouteMapMatchMetric = _SnBgp4RouteMapMatchMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 6),
    _SnBgp4RouteMapMatchMetric_Type()
)
snBgp4RouteMapMatchMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchMetric.setStatus("mandatory")


class _SnBgp4RouteMapMatchNextHopList_Type(OctetString):
    """Custom type snBgp4RouteMapMatchNextHopList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4RouteMapMatchNextHopList_Type.__name__ = "OctetString"
_SnBgp4RouteMapMatchNextHopList_Object = MibTableColumn
snBgp4RouteMapMatchNextHopList = _SnBgp4RouteMapMatchNextHopList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 7),
    _SnBgp4RouteMapMatchNextHopList_Type()
)
snBgp4RouteMapMatchNextHopList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchNextHopList.setStatus("mandatory")


class _SnBgp4RouteMapMatchRouteType_Type(Integer32):
    """Custom type snBgp4RouteMapMatchRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("externalType1", 2),
          ("externalType2", 3),
          ("internal", 4),
          ("local", 5),
          ("none", 0))
    )


_SnBgp4RouteMapMatchRouteType_Type.__name__ = "Integer32"
_SnBgp4RouteMapMatchRouteType_Object = MibTableColumn
snBgp4RouteMapMatchRouteType = _SnBgp4RouteMapMatchRouteType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 8),
    _SnBgp4RouteMapMatchRouteType_Type()
)
snBgp4RouteMapMatchRouteType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchRouteType.setStatus("mandatory")


class _SnBgp4RouteMapMatchTagList_Type(OctetString):
    """Custom type snBgp4RouteMapMatchTagList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4RouteMapMatchTagList_Type.__name__ = "OctetString"
_SnBgp4RouteMapMatchTagList_Object = MibTableColumn
snBgp4RouteMapMatchTagList = _SnBgp4RouteMapMatchTagList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 9),
    _SnBgp4RouteMapMatchTagList_Type()
)
snBgp4RouteMapMatchTagList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchTagList.setStatus("mandatory")
_SnBgp4RouteMapMatchRowMask_Type = Integer32
_SnBgp4RouteMapMatchRowMask_Object = MibTableColumn
snBgp4RouteMapMatchRowMask = _SnBgp4RouteMapMatchRowMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 13, 1, 1, 10),
    _SnBgp4RouteMapMatchRowMask_Type()
)
snBgp4RouteMapMatchRowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapMatchRowMask.setStatus("mandatory")
_SnBgp4RouteMapSet_ObjectIdentity = ObjectIdentity
snBgp4RouteMapSet = _SnBgp4RouteMapSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14)
)
_SnBgp4RouteMapSetTable_Object = MibTable
snBgp4RouteMapSetTable = _SnBgp4RouteMapSetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1)
)
if mibBuilder.loadTexts:
    snBgp4RouteMapSetTable.setStatus("mandatory")
_SnBgp4RouteMapSetEntry_Object = MibTableRow
snBgp4RouteMapSetEntry = _SnBgp4RouteMapSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1)
)
snBgp4RouteMapSetEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RouteMapSetMapName"),
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RouteMapSetSequenceNum"),
)
if mibBuilder.loadTexts:
    snBgp4RouteMapSetEntry.setStatus("mandatory")


class _SnBgp4RouteMapSetMapName_Type(OctetString):
    """Custom type snBgp4RouteMapSetMapName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4RouteMapSetMapName_Type.__name__ = "OctetString"
_SnBgp4RouteMapSetMapName_Object = MibTableColumn
snBgp4RouteMapSetMapName = _SnBgp4RouteMapSetMapName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 1),
    _SnBgp4RouteMapSetMapName_Type()
)
snBgp4RouteMapSetMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetMapName.setStatus("mandatory")
_SnBgp4RouteMapSetSequenceNum_Type = Integer32
_SnBgp4RouteMapSetSequenceNum_Object = MibTableColumn
snBgp4RouteMapSetSequenceNum = _SnBgp4RouteMapSetSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 2),
    _SnBgp4RouteMapSetSequenceNum_Type()
)
snBgp4RouteMapSetSequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetSequenceNum.setStatus("mandatory")


class _SnBgp4RouteMapSetAsPathType_Type(Integer32):
    """Custom type snBgp4RouteMapSetAsPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("prepend", 1),
          ("tag", 0))
    )


_SnBgp4RouteMapSetAsPathType_Type.__name__ = "Integer32"
_SnBgp4RouteMapSetAsPathType_Object = MibTableColumn
snBgp4RouteMapSetAsPathType = _SnBgp4RouteMapSetAsPathType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 3),
    _SnBgp4RouteMapSetAsPathType_Type()
)
snBgp4RouteMapSetAsPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetAsPathType.setStatus("mandatory")


class _SnBgp4RouteMapSetAsPathString_Type(OctetString):
    """Custom type snBgp4RouteMapSetAsPathString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnBgp4RouteMapSetAsPathString_Type.__name__ = "OctetString"
_SnBgp4RouteMapSetAsPathString_Object = MibTableColumn
snBgp4RouteMapSetAsPathString = _SnBgp4RouteMapSetAsPathString_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 4),
    _SnBgp4RouteMapSetAsPathString_Type()
)
snBgp4RouteMapSetAsPathString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetAsPathString.setStatus("mandatory")


class _SnBgp4RouteMapSetAutoTag_Type(Integer32):
    """Custom type snBgp4RouteMapSetAutoTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4RouteMapSetAutoTag_Type.__name__ = "Integer32"
_SnBgp4RouteMapSetAutoTag_Object = MibTableColumn
snBgp4RouteMapSetAutoTag = _SnBgp4RouteMapSetAutoTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 5),
    _SnBgp4RouteMapSetAutoTag_Type()
)
snBgp4RouteMapSetAutoTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetAutoTag.setStatus("mandatory")


class _SnBgp4RouteMapSetCommunityType_Type(Integer32):
    """Custom type snBgp4RouteMapSetCommunityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 3),
          ("nums", 0))
    )


_SnBgp4RouteMapSetCommunityType_Type.__name__ = "Integer32"
_SnBgp4RouteMapSetCommunityType_Object = MibTableColumn
snBgp4RouteMapSetCommunityType = _SnBgp4RouteMapSetCommunityType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 6),
    _SnBgp4RouteMapSetCommunityType_Type()
)
snBgp4RouteMapSetCommunityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetCommunityType.setStatus("mandatory")
_SnBgp4RouteMapSetCommunityNum_Type = Integer32
_SnBgp4RouteMapSetCommunityNum_Object = MibTableColumn
snBgp4RouteMapSetCommunityNum = _SnBgp4RouteMapSetCommunityNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 7),
    _SnBgp4RouteMapSetCommunityNum_Type()
)
snBgp4RouteMapSetCommunityNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetCommunityNum.setStatus("deprecated")


class _SnBgp4RouteMapSetCommunityAdditive_Type(Integer32):
    """Custom type snBgp4RouteMapSetCommunityAdditive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnBgp4RouteMapSetCommunityAdditive_Type.__name__ = "Integer32"
_SnBgp4RouteMapSetCommunityAdditive_Object = MibTableColumn
snBgp4RouteMapSetCommunityAdditive = _SnBgp4RouteMapSetCommunityAdditive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 8),
    _SnBgp4RouteMapSetCommunityAdditive_Type()
)
snBgp4RouteMapSetCommunityAdditive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetCommunityAdditive.setStatus("mandatory")
_SnBgp4RouteMapSetLocalPreference_Type = Integer32
_SnBgp4RouteMapSetLocalPreference_Object = MibTableColumn
snBgp4RouteMapSetLocalPreference = _SnBgp4RouteMapSetLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 9),
    _SnBgp4RouteMapSetLocalPreference_Type()
)
snBgp4RouteMapSetLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetLocalPreference.setStatus("mandatory")
_SnBgp4RouteMapSetMetric_Type = Integer32
_SnBgp4RouteMapSetMetric_Object = MibTableColumn
snBgp4RouteMapSetMetric = _SnBgp4RouteMapSetMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 10),
    _SnBgp4RouteMapSetMetric_Type()
)
snBgp4RouteMapSetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetMetric.setStatus("mandatory")
_SnBgp4RouteMapSetNextHop_Type = IpAddress
_SnBgp4RouteMapSetNextHop_Object = MibTableColumn
snBgp4RouteMapSetNextHop = _SnBgp4RouteMapSetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 11),
    _SnBgp4RouteMapSetNextHop_Type()
)
snBgp4RouteMapSetNextHop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetNextHop.setStatus("mandatory")


class _SnBgp4RouteMapSetOrigin_Type(Integer32):
    """Custom type snBgp4RouteMapSetOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egp", 1),
          ("igp", 0),
          ("incomplete", 2))
    )


_SnBgp4RouteMapSetOrigin_Type.__name__ = "Integer32"
_SnBgp4RouteMapSetOrigin_Object = MibTableColumn
snBgp4RouteMapSetOrigin = _SnBgp4RouteMapSetOrigin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 12),
    _SnBgp4RouteMapSetOrigin_Type()
)
snBgp4RouteMapSetOrigin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetOrigin.setStatus("mandatory")
_SnBgp4RouteMapSetTag_Type = Integer32
_SnBgp4RouteMapSetTag_Object = MibTableColumn
snBgp4RouteMapSetTag = _SnBgp4RouteMapSetTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 13),
    _SnBgp4RouteMapSetTag_Type()
)
snBgp4RouteMapSetTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetTag.setStatus("mandatory")


class _SnBgp4RouteMapSetWeight_Type(Integer32):
    """Custom type snBgp4RouteMapSetWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnBgp4RouteMapSetWeight_Type.__name__ = "Integer32"
_SnBgp4RouteMapSetWeight_Object = MibTableColumn
snBgp4RouteMapSetWeight = _SnBgp4RouteMapSetWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 14),
    _SnBgp4RouteMapSetWeight_Type()
)
snBgp4RouteMapSetWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetWeight.setStatus("mandatory")
_SnBgp4RouteMapSetRowMask_Type = Integer32
_SnBgp4RouteMapSetRowMask_Object = MibTableColumn
snBgp4RouteMapSetRowMask = _SnBgp4RouteMapSetRowMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 15),
    _SnBgp4RouteMapSetRowMask_Type()
)
snBgp4RouteMapSetRowMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetRowMask.setStatus("mandatory")


class _SnBgp4RouteMapSetCommunityNums_Type(OctetString):
    """Custom type snBgp4RouteMapSetCommunityNums based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_SnBgp4RouteMapSetCommunityNums_Type.__name__ = "OctetString"
_SnBgp4RouteMapSetCommunityNums_Object = MibTableColumn
snBgp4RouteMapSetCommunityNums = _SnBgp4RouteMapSetCommunityNums_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 14, 1, 1, 16),
    _SnBgp4RouteMapSetCommunityNums_Type()
)
snBgp4RouteMapSetCommunityNums.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4RouteMapSetCommunityNums.setStatus("mandatory")
_SnBgp4NeighOperStatus_ObjectIdentity = ObjectIdentity
snBgp4NeighOperStatus = _SnBgp4NeighOperStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15)
)
_SnBgp4NeighOperStatusTable_Object = MibTable
snBgp4NeighOperStatusTable = _SnBgp4NeighOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1)
)
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusTable.setStatus("mandatory")
_SnBgp4NeighOperStatusEntry_Object = MibTableRow
snBgp4NeighOperStatusEntry = _SnBgp4NeighOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1)
)
snBgp4NeighOperStatusEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighOperStatusIndex"),
)
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusEntry.setStatus("mandatory")
_SnBgp4NeighOperStatusIndex_Type = Integer32
_SnBgp4NeighOperStatusIndex_Object = MibTableColumn
snBgp4NeighOperStatusIndex = _SnBgp4NeighOperStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 1),
    _SnBgp4NeighOperStatusIndex_Type()
)
snBgp4NeighOperStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusIndex.setStatus("mandatory")
_SnBgp4NeighOperStatusIp_Type = IpAddress
_SnBgp4NeighOperStatusIp_Object = MibTableColumn
snBgp4NeighOperStatusIp = _SnBgp4NeighOperStatusIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 2),
    _SnBgp4NeighOperStatusIp_Type()
)
snBgp4NeighOperStatusIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusIp.setStatus("mandatory")
_SnBgp4NeighOperStatusRemoteAs_Type = Integer32
_SnBgp4NeighOperStatusRemoteAs_Object = MibTableColumn
snBgp4NeighOperStatusRemoteAs = _SnBgp4NeighOperStatusRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 3),
    _SnBgp4NeighOperStatusRemoteAs_Type()
)
snBgp4NeighOperStatusRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusRemoteAs.setStatus("mandatory")


class _SnBgp4NeighOperStatusBgpType_Type(Integer32):
    """Custom type snBgp4NeighOperStatusBgpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ebgp", 0),
          ("ibgp", 1))
    )


_SnBgp4NeighOperStatusBgpType_Type.__name__ = "Integer32"
_SnBgp4NeighOperStatusBgpType_Object = MibTableColumn
snBgp4NeighOperStatusBgpType = _SnBgp4NeighOperStatusBgpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 4),
    _SnBgp4NeighOperStatusBgpType_Type()
)
snBgp4NeighOperStatusBgpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusBgpType.setStatus("mandatory")


class _SnBgp4NeighOperStatusState_Type(Integer32):
    """Custom type snBgp4NeighOperStatusState based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("noState", 0),
          ("openConfirm", 5),
          ("openSent", 4))
    )


_SnBgp4NeighOperStatusState_Type.__name__ = "Integer32"
_SnBgp4NeighOperStatusState_Object = MibTableColumn
snBgp4NeighOperStatusState = _SnBgp4NeighOperStatusState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 5),
    _SnBgp4NeighOperStatusState_Type()
)
snBgp4NeighOperStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusState.setStatus("mandatory")
_SnBgp4NeighOperStatusKeepAliveTime_Type = Integer32
_SnBgp4NeighOperStatusKeepAliveTime_Object = MibTableColumn
snBgp4NeighOperStatusKeepAliveTime = _SnBgp4NeighOperStatusKeepAliveTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 6),
    _SnBgp4NeighOperStatusKeepAliveTime_Type()
)
snBgp4NeighOperStatusKeepAliveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusKeepAliveTime.setStatus("mandatory")
_SnBgp4NeighOperStatusHoldTime_Type = Integer32
_SnBgp4NeighOperStatusHoldTime_Object = MibTableColumn
snBgp4NeighOperStatusHoldTime = _SnBgp4NeighOperStatusHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 7),
    _SnBgp4NeighOperStatusHoldTime_Type()
)
snBgp4NeighOperStatusHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusHoldTime.setStatus("mandatory")
_SnBgp4NeighOperStatusAdvertlevel_Type = Integer32
_SnBgp4NeighOperStatusAdvertlevel_Object = MibTableColumn
snBgp4NeighOperStatusAdvertlevel = _SnBgp4NeighOperStatusAdvertlevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 8),
    _SnBgp4NeighOperStatusAdvertlevel_Type()
)
snBgp4NeighOperStatusAdvertlevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusAdvertlevel.setStatus("mandatory")
_SnBgp4NeighOperStatusKeepAliveTxCounts_Type = Counter32
_SnBgp4NeighOperStatusKeepAliveTxCounts_Object = MibTableColumn
snBgp4NeighOperStatusKeepAliveTxCounts = _SnBgp4NeighOperStatusKeepAliveTxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 9),
    _SnBgp4NeighOperStatusKeepAliveTxCounts_Type()
)
snBgp4NeighOperStatusKeepAliveTxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusKeepAliveTxCounts.setStatus("mandatory")
_SnBgp4NeighOperStatusKeepAliveRxCounts_Type = Counter32
_SnBgp4NeighOperStatusKeepAliveRxCounts_Object = MibTableColumn
snBgp4NeighOperStatusKeepAliveRxCounts = _SnBgp4NeighOperStatusKeepAliveRxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 10),
    _SnBgp4NeighOperStatusKeepAliveRxCounts_Type()
)
snBgp4NeighOperStatusKeepAliveRxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusKeepAliveRxCounts.setStatus("mandatory")
_SnBgp4NeighOperStatusUpdateTxCounts_Type = Counter32
_SnBgp4NeighOperStatusUpdateTxCounts_Object = MibTableColumn
snBgp4NeighOperStatusUpdateTxCounts = _SnBgp4NeighOperStatusUpdateTxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 11),
    _SnBgp4NeighOperStatusUpdateTxCounts_Type()
)
snBgp4NeighOperStatusUpdateTxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusUpdateTxCounts.setStatus("mandatory")
_SnBgp4NeighOperStatusUpdateRxCounts_Type = Counter32
_SnBgp4NeighOperStatusUpdateRxCounts_Object = MibTableColumn
snBgp4NeighOperStatusUpdateRxCounts = _SnBgp4NeighOperStatusUpdateRxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 12),
    _SnBgp4NeighOperStatusUpdateRxCounts_Type()
)
snBgp4NeighOperStatusUpdateRxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusUpdateRxCounts.setStatus("mandatory")
_SnBgp4NeighOperStatusNotifTxCounts_Type = Counter32
_SnBgp4NeighOperStatusNotifTxCounts_Object = MibTableColumn
snBgp4NeighOperStatusNotifTxCounts = _SnBgp4NeighOperStatusNotifTxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 13),
    _SnBgp4NeighOperStatusNotifTxCounts_Type()
)
snBgp4NeighOperStatusNotifTxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusNotifTxCounts.setStatus("mandatory")
_SnBgp4NeighOperStatusNotifRxCounts_Type = Counter32
_SnBgp4NeighOperStatusNotifRxCounts_Object = MibTableColumn
snBgp4NeighOperStatusNotifRxCounts = _SnBgp4NeighOperStatusNotifRxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 14),
    _SnBgp4NeighOperStatusNotifRxCounts_Type()
)
snBgp4NeighOperStatusNotifRxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusNotifRxCounts.setStatus("mandatory")
_SnBgp4NeighOperStatusOpenTxCounts_Type = Counter32
_SnBgp4NeighOperStatusOpenTxCounts_Object = MibTableColumn
snBgp4NeighOperStatusOpenTxCounts = _SnBgp4NeighOperStatusOpenTxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 15),
    _SnBgp4NeighOperStatusOpenTxCounts_Type()
)
snBgp4NeighOperStatusOpenTxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusOpenTxCounts.setStatus("mandatory")
_SnBgp4NeighOperStatusOpenRxCounts_Type = Counter32
_SnBgp4NeighOperStatusOpenRxCounts_Object = MibTableColumn
snBgp4NeighOperStatusOpenRxCounts = _SnBgp4NeighOperStatusOpenRxCounts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 15, 1, 1, 16),
    _SnBgp4NeighOperStatusOpenRxCounts_Type()
)
snBgp4NeighOperStatusOpenRxCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighOperStatusOpenRxCounts.setStatus("mandatory")
_SnBgp4RouteOperStatus_ObjectIdentity = ObjectIdentity
snBgp4RouteOperStatus = _SnBgp4RouteOperStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16)
)
_SnBgp4RouteOperStatusTable_Object = MibTable
snBgp4RouteOperStatusTable = _SnBgp4RouteOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1)
)
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusTable.setStatus("mandatory")
_SnBgp4RouteOperStatusEntry_Object = MibTableRow
snBgp4RouteOperStatusEntry = _SnBgp4RouteOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1)
)
snBgp4RouteOperStatusEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4RouteOperStatusIndex"),
)
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusEntry.setStatus("mandatory")
_SnBgp4RouteOperStatusIndex_Type = Integer32
_SnBgp4RouteOperStatusIndex_Object = MibTableColumn
snBgp4RouteOperStatusIndex = _SnBgp4RouteOperStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 1),
    _SnBgp4RouteOperStatusIndex_Type()
)
snBgp4RouteOperStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusIndex.setStatus("mandatory")
_SnBgp4RouteOperStatusIp_Type = IpAddress
_SnBgp4RouteOperStatusIp_Object = MibTableColumn
snBgp4RouteOperStatusIp = _SnBgp4RouteOperStatusIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 2),
    _SnBgp4RouteOperStatusIp_Type()
)
snBgp4RouteOperStatusIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusIp.setStatus("mandatory")
_SnBgp4RouteOperStatusSubnetMask_Type = IpAddress
_SnBgp4RouteOperStatusSubnetMask_Object = MibTableColumn
snBgp4RouteOperStatusSubnetMask = _SnBgp4RouteOperStatusSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 3),
    _SnBgp4RouteOperStatusSubnetMask_Type()
)
snBgp4RouteOperStatusSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusSubnetMask.setStatus("mandatory")
_SnBgp4RouteOperStatusNextHop_Type = IpAddress
_SnBgp4RouteOperStatusNextHop_Object = MibTableColumn
snBgp4RouteOperStatusNextHop = _SnBgp4RouteOperStatusNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 4),
    _SnBgp4RouteOperStatusNextHop_Type()
)
snBgp4RouteOperStatusNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusNextHop.setStatus("mandatory")
_SnBgp4RouteOperStatusMetric_Type = Integer32
_SnBgp4RouteOperStatusMetric_Object = MibTableColumn
snBgp4RouteOperStatusMetric = _SnBgp4RouteOperStatusMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 5),
    _SnBgp4RouteOperStatusMetric_Type()
)
snBgp4RouteOperStatusMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusMetric.setStatus("mandatory")
_SnBgp4RouteOperStatusLocalPreference_Type = Integer32
_SnBgp4RouteOperStatusLocalPreference_Object = MibTableColumn
snBgp4RouteOperStatusLocalPreference = _SnBgp4RouteOperStatusLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 6),
    _SnBgp4RouteOperStatusLocalPreference_Type()
)
snBgp4RouteOperStatusLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusLocalPreference.setStatus("mandatory")
_SnBgp4RouteOperStatusWeight_Type = Integer32
_SnBgp4RouteOperStatusWeight_Object = MibTableColumn
snBgp4RouteOperStatusWeight = _SnBgp4RouteOperStatusWeight_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 7),
    _SnBgp4RouteOperStatusWeight_Type()
)
snBgp4RouteOperStatusWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusWeight.setStatus("mandatory")


class _SnBgp4RouteOperStatusOrigin_Type(Integer32):
    """Custom type snBgp4RouteOperStatusOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egp", 1),
          ("igp", 0),
          ("incomplete", 2))
    )


_SnBgp4RouteOperStatusOrigin_Type.__name__ = "Integer32"
_SnBgp4RouteOperStatusOrigin_Object = MibTableColumn
snBgp4RouteOperStatusOrigin = _SnBgp4RouteOperStatusOrigin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 8),
    _SnBgp4RouteOperStatusOrigin_Type()
)
snBgp4RouteOperStatusOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusOrigin.setStatus("mandatory")
_SnBgp4RouteOperStatusStatus_Type = Integer32
_SnBgp4RouteOperStatusStatus_Object = MibTableColumn
snBgp4RouteOperStatusStatus = _SnBgp4RouteOperStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 9),
    _SnBgp4RouteOperStatusStatus_Type()
)
snBgp4RouteOperStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusStatus.setStatus("mandatory")
_SnBgp4RouteOperStatusRouteTag_Type = Integer32
_SnBgp4RouteOperStatusRouteTag_Object = MibTableColumn
snBgp4RouteOperStatusRouteTag = _SnBgp4RouteOperStatusRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 10),
    _SnBgp4RouteOperStatusRouteTag_Type()
)
snBgp4RouteOperStatusRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusRouteTag.setStatus("mandatory")
_SnBgp4RouteOperStatusCommunityList_Type = OctetString
_SnBgp4RouteOperStatusCommunityList_Object = MibTableColumn
snBgp4RouteOperStatusCommunityList = _SnBgp4RouteOperStatusCommunityList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 11),
    _SnBgp4RouteOperStatusCommunityList_Type()
)
snBgp4RouteOperStatusCommunityList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusCommunityList.setStatus("mandatory")
_SnBgp4RouteOperStatusAsPathList_Type = OctetString
_SnBgp4RouteOperStatusAsPathList_Object = MibTableColumn
snBgp4RouteOperStatusAsPathList = _SnBgp4RouteOperStatusAsPathList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 16, 1, 1, 12),
    _SnBgp4RouteOperStatusAsPathList_Type()
)
snBgp4RouteOperStatusAsPathList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4RouteOperStatusAsPathList.setStatus("mandatory")
_SnBgp4NeighborSummary_ObjectIdentity = ObjectIdentity
snBgp4NeighborSummary = _SnBgp4NeighborSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17)
)
_SnBgp4NeighborSummaryTable_Object = MibTable
snBgp4NeighborSummaryTable = _SnBgp4NeighborSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1)
)
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryTable.setStatus("mandatory")
_SnBgp4NeighborSummaryEntry_Object = MibTableRow
snBgp4NeighborSummaryEntry = _SnBgp4NeighborSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1, 1)
)
snBgp4NeighborSummaryEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4NeighborSummaryIndex"),
)
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryEntry.setStatus("mandatory")
_SnBgp4NeighborSummaryIndex_Type = Integer32
_SnBgp4NeighborSummaryIndex_Object = MibTableColumn
snBgp4NeighborSummaryIndex = _SnBgp4NeighborSummaryIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1, 1, 1),
    _SnBgp4NeighborSummaryIndex_Type()
)
snBgp4NeighborSummaryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryIndex.setStatus("mandatory")
_SnBgp4NeighborSummaryIp_Type = IpAddress
_SnBgp4NeighborSummaryIp_Object = MibTableColumn
snBgp4NeighborSummaryIp = _SnBgp4NeighborSummaryIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1, 1, 2),
    _SnBgp4NeighborSummaryIp_Type()
)
snBgp4NeighborSummaryIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryIp.setStatus("mandatory")


class _SnBgp4NeighborSummaryState_Type(Integer32):
    """Custom type snBgp4NeighborSummaryState based on Integer32"""
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("noState", 0),
          ("openConfirm", 5),
          ("openSent", 4))
    )


_SnBgp4NeighborSummaryState_Type.__name__ = "Integer32"
_SnBgp4NeighborSummaryState_Object = MibTableColumn
snBgp4NeighborSummaryState = _SnBgp4NeighborSummaryState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1, 1, 3),
    _SnBgp4NeighborSummaryState_Type()
)
snBgp4NeighborSummaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryState.setStatus("mandatory")
_SnBgp4NeighborSummaryStateChgTime_Type = Integer32
_SnBgp4NeighborSummaryStateChgTime_Object = MibTableColumn
snBgp4NeighborSummaryStateChgTime = _SnBgp4NeighborSummaryStateChgTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1, 1, 4),
    _SnBgp4NeighborSummaryStateChgTime_Type()
)
snBgp4NeighborSummaryStateChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryStateChgTime.setStatus("mandatory")
_SnBgp4NeighborSummaryRouteReceived_Type = Integer32
_SnBgp4NeighborSummaryRouteReceived_Object = MibTableColumn
snBgp4NeighborSummaryRouteReceived = _SnBgp4NeighborSummaryRouteReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1, 1, 5),
    _SnBgp4NeighborSummaryRouteReceived_Type()
)
snBgp4NeighborSummaryRouteReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryRouteReceived.setStatus("mandatory")
_SnBgp4NeighborSummaryRouteInstalled_Type = Integer32
_SnBgp4NeighborSummaryRouteInstalled_Object = MibTableColumn
snBgp4NeighborSummaryRouteInstalled = _SnBgp4NeighborSummaryRouteInstalled_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 17, 1, 1, 6),
    _SnBgp4NeighborSummaryRouteInstalled_Type()
)
snBgp4NeighborSummaryRouteInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4NeighborSummaryRouteInstalled.setStatus("mandatory")
_SnBgp4Attribute_ObjectIdentity = ObjectIdentity
snBgp4Attribute = _SnBgp4Attribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18)
)
_SnBgp4AttributeTable_Object = MibTable
snBgp4AttributeTable = _SnBgp4AttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1)
)
if mibBuilder.loadTexts:
    snBgp4AttributeTable.setStatus("mandatory")
_SnBgp4AttributeEntry_Object = MibTableRow
snBgp4AttributeEntry = _SnBgp4AttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1)
)
snBgp4AttributeEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4AttributeIndex"),
)
if mibBuilder.loadTexts:
    snBgp4AttributeEntry.setStatus("mandatory")
_SnBgp4AttributeIndex_Type = Integer32
_SnBgp4AttributeIndex_Object = MibTableColumn
snBgp4AttributeIndex = _SnBgp4AttributeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 1),
    _SnBgp4AttributeIndex_Type()
)
snBgp4AttributeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeIndex.setStatus("mandatory")
_SnBgp4AttributeNextHop_Type = IpAddress
_SnBgp4AttributeNextHop_Object = MibTableColumn
snBgp4AttributeNextHop = _SnBgp4AttributeNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 2),
    _SnBgp4AttributeNextHop_Type()
)
snBgp4AttributeNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeNextHop.setStatus("mandatory")
_SnBgp4AttributeMetric_Type = Integer32
_SnBgp4AttributeMetric_Object = MibTableColumn
snBgp4AttributeMetric = _SnBgp4AttributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 3),
    _SnBgp4AttributeMetric_Type()
)
snBgp4AttributeMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeMetric.setStatus("mandatory")


class _SnBgp4AttributeOrigin_Type(Integer32):
    """Custom type snBgp4AttributeOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("egp", 1),
          ("igp", 0),
          ("incomplete", 2))
    )


_SnBgp4AttributeOrigin_Type.__name__ = "Integer32"
_SnBgp4AttributeOrigin_Object = MibTableColumn
snBgp4AttributeOrigin = _SnBgp4AttributeOrigin_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 4),
    _SnBgp4AttributeOrigin_Type()
)
snBgp4AttributeOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeOrigin.setStatus("mandatory")
_SnBgp4AttributeAggregatorAs_Type = Integer32
_SnBgp4AttributeAggregatorAs_Object = MibTableColumn
snBgp4AttributeAggregatorAs = _SnBgp4AttributeAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 5),
    _SnBgp4AttributeAggregatorAs_Type()
)
snBgp4AttributeAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeAggregatorAs.setStatus("mandatory")
_SnBgp4AttributeRouterId_Type = IpAddress
_SnBgp4AttributeRouterId_Object = MibTableColumn
snBgp4AttributeRouterId = _SnBgp4AttributeRouterId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 6),
    _SnBgp4AttributeRouterId_Type()
)
snBgp4AttributeRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeRouterId.setStatus("mandatory")


class _SnBgp4AttributeAtomicAggregatePresent_Type(Integer32):
    """Custom type snBgp4AttributeAtomicAggregatePresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SnBgp4AttributeAtomicAggregatePresent_Type.__name__ = "Integer32"
_SnBgp4AttributeAtomicAggregatePresent_Object = MibTableColumn
snBgp4AttributeAtomicAggregatePresent = _SnBgp4AttributeAtomicAggregatePresent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 7),
    _SnBgp4AttributeAtomicAggregatePresent_Type()
)
snBgp4AttributeAtomicAggregatePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeAtomicAggregatePresent.setStatus("mandatory")
_SnBgp4AttributeLocalPreference_Type = Integer32
_SnBgp4AttributeLocalPreference_Object = MibTableColumn
snBgp4AttributeLocalPreference = _SnBgp4AttributeLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 8),
    _SnBgp4AttributeLocalPreference_Type()
)
snBgp4AttributeLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeLocalPreference.setStatus("mandatory")
_SnBgp4AttributeCommunityList_Type = OctetString
_SnBgp4AttributeCommunityList_Object = MibTableColumn
snBgp4AttributeCommunityList = _SnBgp4AttributeCommunityList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 9),
    _SnBgp4AttributeCommunityList_Type()
)
snBgp4AttributeCommunityList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeCommunityList.setStatus("mandatory")
_SnBgp4AttributeAsPathList_Type = OctetString
_SnBgp4AttributeAsPathList_Object = MibTableColumn
snBgp4AttributeAsPathList = _SnBgp4AttributeAsPathList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 10),
    _SnBgp4AttributeAsPathList_Type()
)
snBgp4AttributeAsPathList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeAsPathList.setStatus("mandatory")
_SnBgp4AttributeOriginator_Type = IpAddress
_SnBgp4AttributeOriginator_Object = MibTableColumn
snBgp4AttributeOriginator = _SnBgp4AttributeOriginator_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 11),
    _SnBgp4AttributeOriginator_Type()
)
snBgp4AttributeOriginator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeOriginator.setStatus("mandatory")
_SnBgp4AttributeClusterList_Type = OctetString
_SnBgp4AttributeClusterList_Object = MibTableColumn
snBgp4AttributeClusterList = _SnBgp4AttributeClusterList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 18, 1, 1, 12),
    _SnBgp4AttributeClusterList_Type()
)
snBgp4AttributeClusterList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4AttributeClusterList.setStatus("mandatory")
_SnBgp4ClearNeighborCmd_ObjectIdentity = ObjectIdentity
snBgp4ClearNeighborCmd = _SnBgp4ClearNeighborCmd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 19)
)
_SnBgp4ClearNeighborCmdTable_Object = MibTable
snBgp4ClearNeighborCmdTable = _SnBgp4ClearNeighborCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 19, 1)
)
if mibBuilder.loadTexts:
    snBgp4ClearNeighborCmdTable.setStatus("mandatory")
_SnBgp4ClearNeighborCmdEntry_Object = MibTableRow
snBgp4ClearNeighborCmdEntry = _SnBgp4ClearNeighborCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 19, 1, 1)
)
snBgp4ClearNeighborCmdEntry.setIndexNames(
    (0, "HP-SN-BGP4-GROUP-MIB", "snBgp4ClearNeighborCmdIp"),
)
if mibBuilder.loadTexts:
    snBgp4ClearNeighborCmdEntry.setStatus("mandatory")
_SnBgp4ClearNeighborCmdIp_Type = IpAddress
_SnBgp4ClearNeighborCmdIp_Object = MibTableColumn
snBgp4ClearNeighborCmdIp = _SnBgp4ClearNeighborCmdIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 19, 1, 1, 1),
    _SnBgp4ClearNeighborCmdIp_Type()
)
snBgp4ClearNeighborCmdIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snBgp4ClearNeighborCmdIp.setStatus("mandatory")


class _SnBgp4ClearNeighborCmdElement_Type(Integer32):
    """Custom type snBgp4ClearNeighborCmdElement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("lastPacketWithError", 1),
          ("neighbor", 5),
          ("notificationErrors", 2),
          ("softOutbound", 3),
          ("traffic", 4),
          ("valid", 0))
    )


_SnBgp4ClearNeighborCmdElement_Type.__name__ = "Integer32"
_SnBgp4ClearNeighborCmdElement_Object = MibTableColumn
snBgp4ClearNeighborCmdElement = _SnBgp4ClearNeighborCmdElement_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 11, 19, 1, 1, 2),
    _SnBgp4ClearNeighborCmdElement_Type()
)
snBgp4ClearNeighborCmdElement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snBgp4ClearNeighborCmdElement.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-BGP4-GROUP-MIB",
    **{"snBgp4Gen": snBgp4Gen,
       "snBgp4GenAlwaysCompareMed": snBgp4GenAlwaysCompareMed,
       "snBgp4GenAutoSummary": snBgp4GenAutoSummary,
       "snBgp4GenDefaultLocalPreference": snBgp4GenDefaultLocalPreference,
       "snBgp4GenDefaultInfoOriginate": snBgp4GenDefaultInfoOriginate,
       "snBgp4GenFastExternalFallover": snBgp4GenFastExternalFallover,
       "snBgp4GenNextBootNeighbors": snBgp4GenNextBootNeighbors,
       "snBgp4GenNextBootRoutes": snBgp4GenNextBootRoutes,
       "snBgp4GenSynchronization": snBgp4GenSynchronization,
       "snBgp4GenKeepAliveTime": snBgp4GenKeepAliveTime,
       "snBgp4GenHoldTime": snBgp4GenHoldTime,
       "snBgp4GenRouterId": snBgp4GenRouterId,
       "snBgp4GenTableMap": snBgp4GenTableMap,
       "snBgp4GenAdminStat": snBgp4GenAdminStat,
       "snBgp4GenDefaultMetric": snBgp4GenDefaultMetric,
       "snBgp4GenMaxNeighbors": snBgp4GenMaxNeighbors,
       "snBgp4GenMinNeighbors": snBgp4GenMinNeighbors,
       "snBgp4GenMaxRoutes": snBgp4GenMaxRoutes,
       "snBgp4GenMinRoutes": snBgp4GenMinRoutes,
       "snBgp4GenMaxAddrFilters": snBgp4GenMaxAddrFilters,
       "snBgp4GenMaxAggregateAddresses": snBgp4GenMaxAggregateAddresses,
       "snBgp4GenMaxAsPathFilters": snBgp4GenMaxAsPathFilters,
       "snBgp4GenMaxCommunityFilters": snBgp4GenMaxCommunityFilters,
       "snBgp4GenMaxNetworks": snBgp4GenMaxNetworks,
       "snBgp4GenMaxRouteMapFilters": snBgp4GenMaxRouteMapFilters,
       "snBgp4GenNeighPrefixMinValue": snBgp4GenNeighPrefixMinValue,
       "snBgp4GenOperNeighbors": snBgp4GenOperNeighbors,
       "snBgp4GenOperRoutes": snBgp4GenOperRoutes,
       "snBgp4GenLocalAs": snBgp4GenLocalAs,
       "snBgp4GenRoutesInstalled": snBgp4GenRoutesInstalled,
       "snBgp4GenAsPathInstalled": snBgp4GenAsPathInstalled,
       "snBgp4ExternalDistance": snBgp4ExternalDistance,
       "snBgp4InternalDistance": snBgp4InternalDistance,
       "snBgp4LocalDistance": snBgp4LocalDistance,
       "snBgp4OperNumOfAttributes": snBgp4OperNumOfAttributes,
       "snBgp4NextBootMaxAttributes": snBgp4NextBootMaxAttributes,
       "snBgp4ClusterId": snBgp4ClusterId,
       "snBgp4ClientToClientReflection": snBgp4ClientToClientReflection,
       "snBgp4GenTotalNeighbors": snBgp4GenTotalNeighbors,
       "snBgp4GenMaxPaths": snBgp4GenMaxPaths,
       "snBgp4GenConfedId": snBgp4GenConfedId,
       "snBgp4GenConfedPeers": snBgp4GenConfedPeers,
       "snBgp4AddrFilter": snBgp4AddrFilter,
       "snBgp4AddrFilterTable": snBgp4AddrFilterTable,
       "snBgp4AddrFilterEntry": snBgp4AddrFilterEntry,
       "snBgp4AddrFilterIndex": snBgp4AddrFilterIndex,
       "snBgp4AddrFilterAction": snBgp4AddrFilterAction,
       "snBgp4AddrFilterSourceIp": snBgp4AddrFilterSourceIp,
       "snBgp4AddrFilterSourceMask": snBgp4AddrFilterSourceMask,
       "snBgp4AddrFilterDestIp": snBgp4AddrFilterDestIp,
       "snBgp4AddrFilterDestMask": snBgp4AddrFilterDestMask,
       "snBgp4AddrFilterRowStatus": snBgp4AddrFilterRowStatus,
       "snBgp4AggregateAddr": snBgp4AggregateAddr,
       "snBgp4AggregateAddrTable": snBgp4AggregateAddrTable,
       "snBgp4AggregateAddrEntry": snBgp4AggregateAddrEntry,
       "snBgp4AggregateAddrIp": snBgp4AggregateAddrIp,
       "snBgp4AggregateAddrMask": snBgp4AggregateAddrMask,
       "snBgp4AggregateAddrOption": snBgp4AggregateAddrOption,
       "snBgp4AggregateAddrMap": snBgp4AggregateAddrMap,
       "snBgp4AggregateAddrRowStatus": snBgp4AggregateAddrRowStatus,
       "snBgp4AsPathFilter": snBgp4AsPathFilter,
       "snBgp4AsPathFilterTable": snBgp4AsPathFilterTable,
       "snBgp4AsPathFilterEntry": snBgp4AsPathFilterEntry,
       "snBgp4AsPathFilterIndex": snBgp4AsPathFilterIndex,
       "snBgp4AsPathFilterAction": snBgp4AsPathFilterAction,
       "snBgp4AsPathFilterRegExpression": snBgp4AsPathFilterRegExpression,
       "snBgp4AsPathFilterRowStatus": snBgp4AsPathFilterRowStatus,
       "snBgp4CommunityFilter": snBgp4CommunityFilter,
       "snBgp4CommunityFilterTable": snBgp4CommunityFilterTable,
       "snBgp4CommunityFilterEntry": snBgp4CommunityFilterEntry,
       "snBgp4CommunityFilterIndex": snBgp4CommunityFilterIndex,
       "snBgp4CommunityFilterAction": snBgp4CommunityFilterAction,
       "snBgp4CommunityFilterCommNum": snBgp4CommunityFilterCommNum,
       "snBgp4CommunityFilterInternet": snBgp4CommunityFilterInternet,
       "snBgp4CommunityFilterNoAdvertise": snBgp4CommunityFilterNoAdvertise,
       "snBgp4CommunityFilterNoExport": snBgp4CommunityFilterNoExport,
       "snBgp4CommunityFilterRowStatus": snBgp4CommunityFilterRowStatus,
       "snBgp4CommunityFilterLocalAs": snBgp4CommunityFilterLocalAs,
       "snBgp4NeighGenCfg": snBgp4NeighGenCfg,
       "snBgp4NeighGenCfgTable": snBgp4NeighGenCfgTable,
       "snBgp4NeighGenCfgEntry": snBgp4NeighGenCfgEntry,
       "snBgp4NeighGenCfgNeighIp": snBgp4NeighGenCfgNeighIp,
       "snBgp4NeighGenCfgAdvertlevel": snBgp4NeighGenCfgAdvertlevel,
       "snBgp4NeighGenCfgDefOriginate": snBgp4NeighGenCfgDefOriginate,
       "snBgp4NeighGenCfgEbgpMultihop": snBgp4NeighGenCfgEbgpMultihop,
       "snBgp4NeighGenCfgMaxPrefix": snBgp4NeighGenCfgMaxPrefix,
       "snBgp4NeighGenCfgNextHopSelf": snBgp4NeighGenCfgNextHopSelf,
       "snBgp4NeighGenCfgRemoteAs": snBgp4NeighGenCfgRemoteAs,
       "snBgp4NeighGenCfgSendComm": snBgp4NeighGenCfgSendComm,
       "snBgp4NeighGenCfgWeight": snBgp4NeighGenCfgWeight,
       "snBgp4NeighGenCfgWeightFilterList": snBgp4NeighGenCfgWeightFilterList,
       "snBgp4NeighGenCfgRowStatus": snBgp4NeighGenCfgRowStatus,
       "snBgp4NeighGenCfgUpdateSrcLpbIntf": snBgp4NeighGenCfgUpdateSrcLpbIntf,
       "snBgp4NeighGenCfgRouteRefClient": snBgp4NeighGenCfgRouteRefClient,
       "snBgp4NeighGenCfgRemovePrivateAs": snBgp4NeighGenCfgRemovePrivateAs,
       "snBgp4NeighGenCfgEbgpMultihopTtl": snBgp4NeighGenCfgEbgpMultihopTtl,
       "snBgp4NeighGenCfgShutdown": snBgp4NeighGenCfgShutdown,
       "snBgp4NeighGenCfgKeepAliveTime": snBgp4NeighGenCfgKeepAliveTime,
       "snBgp4NeighGenCfgHoldTime": snBgp4NeighGenCfgHoldTime,
       "snBgp4NeighDistGroup": snBgp4NeighDistGroup,
       "snBgp4NeighDistGroupTable": snBgp4NeighDistGroupTable,
       "snBgp4NeighDistGroupEntry": snBgp4NeighDistGroupEntry,
       "snBgp4NeighDistGroupNeighIp": snBgp4NeighDistGroupNeighIp,
       "snBgp4NeighDistGroupDir": snBgp4NeighDistGroupDir,
       "snBgp4NeighDistGroupAccessList": snBgp4NeighDistGroupAccessList,
       "snBgp4NeighDistGroupRowStatus": snBgp4NeighDistGroupRowStatus,
       "snBgp4NeighFilterGroup": snBgp4NeighFilterGroup,
       "snBgp4NeighFilterGroupTable": snBgp4NeighFilterGroupTable,
       "snBgp4NeighFilterGroupEntry": snBgp4NeighFilterGroupEntry,
       "snBgp4NeighFilterGroupNeighIp": snBgp4NeighFilterGroupNeighIp,
       "snBgp4NeighFilterGroupDir": snBgp4NeighFilterGroupDir,
       "snBgp4NeighFilterGroupAccessList": snBgp4NeighFilterGroupAccessList,
       "snBgp4NeighFilterGroupRowStatus": snBgp4NeighFilterGroupRowStatus,
       "snBgp4NeighRouteMap": snBgp4NeighRouteMap,
       "snBgp4NeighRouteMapTable": snBgp4NeighRouteMapTable,
       "snBgp4NeighRouteMapEntry": snBgp4NeighRouteMapEntry,
       "snBgp4NeighRouteMapNeighIp": snBgp4NeighRouteMapNeighIp,
       "snBgp4NeighRouteMapDir": snBgp4NeighRouteMapDir,
       "snBgp4NeighRouteMapMapName": snBgp4NeighRouteMapMapName,
       "snBgp4NeighRouteMapRowStatus": snBgp4NeighRouteMapRowStatus,
       "snBgp4Network": snBgp4Network,
       "snBgp4NetworkTable": snBgp4NetworkTable,
       "snBgp4NetworkEntry": snBgp4NetworkEntry,
       "snBgp4NetworkIp": snBgp4NetworkIp,
       "snBgp4NetworkSubnetMask": snBgp4NetworkSubnetMask,
       "snBgp4NetworkWeight": snBgp4NetworkWeight,
       "snBgp4NetworkBackdoor": snBgp4NetworkBackdoor,
       "snBgp4NetworkRowStatus": snBgp4NetworkRowStatus,
       "snBgp4Redis": snBgp4Redis,
       "snBgp4RedisTable": snBgp4RedisTable,
       "snBgp4RedisEntry": snBgp4RedisEntry,
       "snBgp4RedisProtocol": snBgp4RedisProtocol,
       "snBgp4RedisMetric": snBgp4RedisMetric,
       "snBgp4RedisRouteMap": snBgp4RedisRouteMap,
       "snBgp4RedisWeight": snBgp4RedisWeight,
       "snBgp4RedisMatchInternal": snBgp4RedisMatchInternal,
       "snBgp4RedisMatchExternal1": snBgp4RedisMatchExternal1,
       "snBgp4RedisMatchExternal2": snBgp4RedisMatchExternal2,
       "snBgp4RedisRowStatus": snBgp4RedisRowStatus,
       "snBgp4RouteMapFilter": snBgp4RouteMapFilter,
       "snBgp4RouteMapFilterTable": snBgp4RouteMapFilterTable,
       "snBgp4RouteMapFilterEntry": snBgp4RouteMapFilterEntry,
       "snBgp4RouteMapFilterMapName": snBgp4RouteMapFilterMapName,
       "snBgp4RouteMapFilterSequenceNum": snBgp4RouteMapFilterSequenceNum,
       "snBgp4RouteMapFilterAction": snBgp4RouteMapFilterAction,
       "snBgp4RouteMapFilterRowStatus": snBgp4RouteMapFilterRowStatus,
       "snBgp4RouteMapMatch": snBgp4RouteMapMatch,
       "snBgp4RouteMapMatchTable": snBgp4RouteMapMatchTable,
       "snBgp4RouteMapMatchEntry": snBgp4RouteMapMatchEntry,
       "snBgp4RouteMapMatchMapName": snBgp4RouteMapMatchMapName,
       "snBgp4RouteMapMatchSequenceNum": snBgp4RouteMapMatchSequenceNum,
       "snBgp4RouteMapMatchAsPathFilter": snBgp4RouteMapMatchAsPathFilter,
       "snBgp4RouteMapMatchCommunityFilter": snBgp4RouteMapMatchCommunityFilter,
       "snBgp4RouteMapMatchAddressFilter": snBgp4RouteMapMatchAddressFilter,
       "snBgp4RouteMapMatchMetric": snBgp4RouteMapMatchMetric,
       "snBgp4RouteMapMatchNextHopList": snBgp4RouteMapMatchNextHopList,
       "snBgp4RouteMapMatchRouteType": snBgp4RouteMapMatchRouteType,
       "snBgp4RouteMapMatchTagList": snBgp4RouteMapMatchTagList,
       "snBgp4RouteMapMatchRowMask": snBgp4RouteMapMatchRowMask,
       "snBgp4RouteMapSet": snBgp4RouteMapSet,
       "snBgp4RouteMapSetTable": snBgp4RouteMapSetTable,
       "snBgp4RouteMapSetEntry": snBgp4RouteMapSetEntry,
       "snBgp4RouteMapSetMapName": snBgp4RouteMapSetMapName,
       "snBgp4RouteMapSetSequenceNum": snBgp4RouteMapSetSequenceNum,
       "snBgp4RouteMapSetAsPathType": snBgp4RouteMapSetAsPathType,
       "snBgp4RouteMapSetAsPathString": snBgp4RouteMapSetAsPathString,
       "snBgp4RouteMapSetAutoTag": snBgp4RouteMapSetAutoTag,
       "snBgp4RouteMapSetCommunityType": snBgp4RouteMapSetCommunityType,
       "snBgp4RouteMapSetCommunityNum": snBgp4RouteMapSetCommunityNum,
       "snBgp4RouteMapSetCommunityAdditive": snBgp4RouteMapSetCommunityAdditive,
       "snBgp4RouteMapSetLocalPreference": snBgp4RouteMapSetLocalPreference,
       "snBgp4RouteMapSetMetric": snBgp4RouteMapSetMetric,
       "snBgp4RouteMapSetNextHop": snBgp4RouteMapSetNextHop,
       "snBgp4RouteMapSetOrigin": snBgp4RouteMapSetOrigin,
       "snBgp4RouteMapSetTag": snBgp4RouteMapSetTag,
       "snBgp4RouteMapSetWeight": snBgp4RouteMapSetWeight,
       "snBgp4RouteMapSetRowMask": snBgp4RouteMapSetRowMask,
       "snBgp4RouteMapSetCommunityNums": snBgp4RouteMapSetCommunityNums,
       "snBgp4NeighOperStatus": snBgp4NeighOperStatus,
       "snBgp4NeighOperStatusTable": snBgp4NeighOperStatusTable,
       "snBgp4NeighOperStatusEntry": snBgp4NeighOperStatusEntry,
       "snBgp4NeighOperStatusIndex": snBgp4NeighOperStatusIndex,
       "snBgp4NeighOperStatusIp": snBgp4NeighOperStatusIp,
       "snBgp4NeighOperStatusRemoteAs": snBgp4NeighOperStatusRemoteAs,
       "snBgp4NeighOperStatusBgpType": snBgp4NeighOperStatusBgpType,
       "snBgp4NeighOperStatusState": snBgp4NeighOperStatusState,
       "snBgp4NeighOperStatusKeepAliveTime": snBgp4NeighOperStatusKeepAliveTime,
       "snBgp4NeighOperStatusHoldTime": snBgp4NeighOperStatusHoldTime,
       "snBgp4NeighOperStatusAdvertlevel": snBgp4NeighOperStatusAdvertlevel,
       "snBgp4NeighOperStatusKeepAliveTxCounts": snBgp4NeighOperStatusKeepAliveTxCounts,
       "snBgp4NeighOperStatusKeepAliveRxCounts": snBgp4NeighOperStatusKeepAliveRxCounts,
       "snBgp4NeighOperStatusUpdateTxCounts": snBgp4NeighOperStatusUpdateTxCounts,
       "snBgp4NeighOperStatusUpdateRxCounts": snBgp4NeighOperStatusUpdateRxCounts,
       "snBgp4NeighOperStatusNotifTxCounts": snBgp4NeighOperStatusNotifTxCounts,
       "snBgp4NeighOperStatusNotifRxCounts": snBgp4NeighOperStatusNotifRxCounts,
       "snBgp4NeighOperStatusOpenTxCounts": snBgp4NeighOperStatusOpenTxCounts,
       "snBgp4NeighOperStatusOpenRxCounts": snBgp4NeighOperStatusOpenRxCounts,
       "snBgp4RouteOperStatus": snBgp4RouteOperStatus,
       "snBgp4RouteOperStatusTable": snBgp4RouteOperStatusTable,
       "snBgp4RouteOperStatusEntry": snBgp4RouteOperStatusEntry,
       "snBgp4RouteOperStatusIndex": snBgp4RouteOperStatusIndex,
       "snBgp4RouteOperStatusIp": snBgp4RouteOperStatusIp,
       "snBgp4RouteOperStatusSubnetMask": snBgp4RouteOperStatusSubnetMask,
       "snBgp4RouteOperStatusNextHop": snBgp4RouteOperStatusNextHop,
       "snBgp4RouteOperStatusMetric": snBgp4RouteOperStatusMetric,
       "snBgp4RouteOperStatusLocalPreference": snBgp4RouteOperStatusLocalPreference,
       "snBgp4RouteOperStatusWeight": snBgp4RouteOperStatusWeight,
       "snBgp4RouteOperStatusOrigin": snBgp4RouteOperStatusOrigin,
       "snBgp4RouteOperStatusStatus": snBgp4RouteOperStatusStatus,
       "snBgp4RouteOperStatusRouteTag": snBgp4RouteOperStatusRouteTag,
       "snBgp4RouteOperStatusCommunityList": snBgp4RouteOperStatusCommunityList,
       "snBgp4RouteOperStatusAsPathList": snBgp4RouteOperStatusAsPathList,
       "snBgp4NeighborSummary": snBgp4NeighborSummary,
       "snBgp4NeighborSummaryTable": snBgp4NeighborSummaryTable,
       "snBgp4NeighborSummaryEntry": snBgp4NeighborSummaryEntry,
       "snBgp4NeighborSummaryIndex": snBgp4NeighborSummaryIndex,
       "snBgp4NeighborSummaryIp": snBgp4NeighborSummaryIp,
       "snBgp4NeighborSummaryState": snBgp4NeighborSummaryState,
       "snBgp4NeighborSummaryStateChgTime": snBgp4NeighborSummaryStateChgTime,
       "snBgp4NeighborSummaryRouteReceived": snBgp4NeighborSummaryRouteReceived,
       "snBgp4NeighborSummaryRouteInstalled": snBgp4NeighborSummaryRouteInstalled,
       "snBgp4Attribute": snBgp4Attribute,
       "snBgp4AttributeTable": snBgp4AttributeTable,
       "snBgp4AttributeEntry": snBgp4AttributeEntry,
       "snBgp4AttributeIndex": snBgp4AttributeIndex,
       "snBgp4AttributeNextHop": snBgp4AttributeNextHop,
       "snBgp4AttributeMetric": snBgp4AttributeMetric,
       "snBgp4AttributeOrigin": snBgp4AttributeOrigin,
       "snBgp4AttributeAggregatorAs": snBgp4AttributeAggregatorAs,
       "snBgp4AttributeRouterId": snBgp4AttributeRouterId,
       "snBgp4AttributeAtomicAggregatePresent": snBgp4AttributeAtomicAggregatePresent,
       "snBgp4AttributeLocalPreference": snBgp4AttributeLocalPreference,
       "snBgp4AttributeCommunityList": snBgp4AttributeCommunityList,
       "snBgp4AttributeAsPathList": snBgp4AttributeAsPathList,
       "snBgp4AttributeOriginator": snBgp4AttributeOriginator,
       "snBgp4AttributeClusterList": snBgp4AttributeClusterList,
       "snBgp4ClearNeighborCmd": snBgp4ClearNeighborCmd,
       "snBgp4ClearNeighborCmdTable": snBgp4ClearNeighborCmdTable,
       "snBgp4ClearNeighborCmdEntry": snBgp4ClearNeighborCmdEntry,
       "snBgp4ClearNeighborCmdIp": snBgp4ClearNeighborCmdIp,
       "snBgp4ClearNeighborCmdElement": snBgp4ClearNeighborCmdElement}
)
