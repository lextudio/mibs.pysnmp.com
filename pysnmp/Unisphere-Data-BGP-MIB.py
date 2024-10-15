# SNMP MIB module (Unisphere-Data-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:22 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdVrfName,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdVrfName")


# MODULE-IDENTITY

usdBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29)
)
usdBgpMIB.setRevisions(
        ("2002-09-04 13:23",
         "2002-03-01 16:54",
         "2002-01-23 13:16",
         "2001-12-04 15:23",
         "2001-11-30 22:20",
         "2001-06-18 18:59",
         "2000-01-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdBgpAfi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bgpIpV4", 1)
    )



class UsdBgpSafi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              128)
        )
    )
    namedValues = NamedValues(
        *(("bgpMulticast", 2),
          ("bgpUnicast", 1),
          ("bgpUnicastMulticast", 3),
          ("bgpVPNUnicast", 128))
    )



class UsdBgpStorageInteger(Unsigned32, TextualConvention):
    status = "current"


class UsdBgpResetConnectionType(Integer32, TextualConvention):
    status = "current"
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
        *(("resetTypeHard", 1),
          ("resetTypeNoop", 0),
          ("resetTypeRouteFlapHistory", 5),
          ("resetTypeSoftIn", 2),
          ("resetTypeSoftInOut", 4),
          ("resetTypeSoftOut", 3))
    )



# MIB Managed Objects in the order of their OIDs

_UsdBgpObjects_ObjectIdentity = ObjectIdentity
usdBgpObjects = _UsdBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1)
)
_UsdBgpGeneralGroup_ObjectIdentity = ObjectIdentity
usdBgpGeneralGroup = _UsdBgpGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1)
)


class _UsdBgpLocalAsNumber_Type(Integer32):
    """Custom type usdBgpLocalAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpLocalAsNumber_Type.__name__ = "Integer32"
_UsdBgpLocalAsNumber_Object = MibScalar
usdBgpLocalAsNumber = _UsdBgpLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 1),
    _UsdBgpLocalAsNumber_Type()
)
usdBgpLocalAsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpLocalAsNumber.setStatus("current")


class _UsdBgpEnabled_Type(TruthValue):
    """Custom type usdBgpEnabled based on TruthValue"""


_UsdBgpEnabled_Object = MibScalar
usdBgpEnabled = _UsdBgpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 2),
    _UsdBgpEnabled_Type()
)
usdBgpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpEnabled.setStatus("current")
_UsdBgpIdentifier_Type = IpAddress
_UsdBgpIdentifier_Object = MibScalar
usdBgpIdentifier = _UsdBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 3),
    _UsdBgpIdentifier_Type()
)
usdBgpIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpIdentifier.setStatus("current")


class _UsdBgpAlwaysCompareMed_Type(TruthValue):
    """Custom type usdBgpAlwaysCompareMed based on TruthValue"""


_UsdBgpAlwaysCompareMed_Object = MibScalar
usdBgpAlwaysCompareMed = _UsdBgpAlwaysCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 4),
    _UsdBgpAlwaysCompareMed_Type()
)
usdBgpAlwaysCompareMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpAlwaysCompareMed.setStatus("current")


class _UsdBgpDefaultLocalPreference_Type(Unsigned32):
    """Custom type usdBgpDefaultLocalPreference based on Unsigned32"""
    defaultValue = 100


_UsdBgpDefaultLocalPreference_Object = MibScalar
usdBgpDefaultLocalPreference = _UsdBgpDefaultLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 5),
    _UsdBgpDefaultLocalPreference_Type()
)
usdBgpDefaultLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpDefaultLocalPreference.setStatus("current")


class _UsdBgpEqualCostLimit_Type(Integer32):
    """Custom type usdBgpEqualCostLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpEqualCostLimit_Type.__name__ = "Integer32"
_UsdBgpEqualCostLimit_Object = MibScalar
usdBgpEqualCostLimit = _UsdBgpEqualCostLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 6),
    _UsdBgpEqualCostLimit_Type()
)
usdBgpEqualCostLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpEqualCostLimit.setStatus("current")


class _UsdBgpClientToClientReflection_Type(TruthValue):
    """Custom type usdBgpClientToClientReflection based on TruthValue"""


_UsdBgpClientToClientReflection_Object = MibScalar
usdBgpClientToClientReflection = _UsdBgpClientToClientReflection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 7),
    _UsdBgpClientToClientReflection_Type()
)
usdBgpClientToClientReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpClientToClientReflection.setStatus("current")


class _UsdBgpClusterId_Type(Unsigned32):
    """Custom type usdBgpClusterId based on Unsigned32"""
    defaultValue = 0


_UsdBgpClusterId_Object = MibScalar
usdBgpClusterId = _UsdBgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 8),
    _UsdBgpClusterId_Type()
)
usdBgpClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpClusterId.setStatus("current")


class _UsdBgpConfederationId_Type(Unsigned32):
    """Custom type usdBgpConfederationId based on Unsigned32"""
    defaultValue = 0


_UsdBgpConfederationId_Object = MibScalar
usdBgpConfederationId = _UsdBgpConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 9),
    _UsdBgpConfederationId_Type()
)
usdBgpConfederationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpConfederationId.setStatus("current")


class _UsdBgpMissingAsWorst_Type(TruthValue):
    """Custom type usdBgpMissingAsWorst based on TruthValue"""


_UsdBgpMissingAsWorst_Object = MibScalar
usdBgpMissingAsWorst = _UsdBgpMissingAsWorst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 10),
    _UsdBgpMissingAsWorst_Type()
)
usdBgpMissingAsWorst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpMissingAsWorst.setStatus("current")


class _UsdBgpResetAllConnectionType_Type(UsdBgpResetConnectionType):
    """Custom type usdBgpResetAllConnectionType based on UsdBgpResetConnectionType"""


_UsdBgpResetAllConnectionType_Object = MibScalar
usdBgpResetAllConnectionType = _UsdBgpResetAllConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 11),
    _UsdBgpResetAllConnectionType_Type()
)
usdBgpResetAllConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpResetAllConnectionType.setStatus("current")


class _UsdBgpAdvertiseInactive_Type(TruthValue):
    """Custom type usdBgpAdvertiseInactive based on TruthValue"""


_UsdBgpAdvertiseInactive_Object = MibScalar
usdBgpAdvertiseInactive = _UsdBgpAdvertiseInactive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 12),
    _UsdBgpAdvertiseInactive_Type()
)
usdBgpAdvertiseInactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpAdvertiseInactive.setStatus("current")


class _UsdBgpEnforceFirstAs_Type(TruthValue):
    """Custom type usdBgpEnforceFirstAs based on TruthValue"""


_UsdBgpEnforceFirstAs_Object = MibScalar
usdBgpEnforceFirstAs = _UsdBgpEnforceFirstAs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 13),
    _UsdBgpEnforceFirstAs_Type()
)
usdBgpEnforceFirstAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpEnforceFirstAs.setStatus("current")


class _UsdBgpConfedCompareMed_Type(TruthValue):
    """Custom type usdBgpConfedCompareMed based on TruthValue"""


_UsdBgpConfedCompareMed_Object = MibScalar
usdBgpConfedCompareMed = _UsdBgpConfedCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 14),
    _UsdBgpConfedCompareMed_Type()
)
usdBgpConfedCompareMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpConfedCompareMed.setStatus("current")


class _UsdBgpGlobalRetryInterval_Type(Integer32):
    """Custom type usdBgpGlobalRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpGlobalRetryInterval_Type.__name__ = "Integer32"
_UsdBgpGlobalRetryInterval_Object = MibScalar
usdBgpGlobalRetryInterval = _UsdBgpGlobalRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 15),
    _UsdBgpGlobalRetryInterval_Type()
)
usdBgpGlobalRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpGlobalRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpGlobalRetryInterval.setUnits("seconds")


class _UsdBgpGlobalConfigKeepAliveInterval_Type(Integer32):
    """Custom type usdBgpGlobalConfigKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_UsdBgpGlobalConfigKeepAliveInterval_Type.__name__ = "Integer32"
_UsdBgpGlobalConfigKeepAliveInterval_Object = MibScalar
usdBgpGlobalConfigKeepAliveInterval = _UsdBgpGlobalConfigKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 16),
    _UsdBgpGlobalConfigKeepAliveInterval_Type()
)
usdBgpGlobalConfigKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpGlobalConfigKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpGlobalConfigKeepAliveInterval.setUnits("seconds")


class _UsdBgpGlobalConfigHoldTime_Type(Integer32):
    """Custom type usdBgpGlobalConfigHoldTime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_UsdBgpGlobalConfigHoldTime_Type.__name__ = "Integer32"
_UsdBgpGlobalConfigHoldTime_Object = MibScalar
usdBgpGlobalConfigHoldTime = _UsdBgpGlobalConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 17),
    _UsdBgpGlobalConfigHoldTime_Type()
)
usdBgpGlobalConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpGlobalConfigHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpGlobalConfigHoldTime.setUnits("seconds")


class _UsdBgpGlobalAsOriginationInterval_Type(Integer32):
    """Custom type usdBgpGlobalAsOriginationInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpGlobalAsOriginationInterval_Type.__name__ = "Integer32"
_UsdBgpGlobalAsOriginationInterval_Object = MibScalar
usdBgpGlobalAsOriginationInterval = _UsdBgpGlobalAsOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 18),
    _UsdBgpGlobalAsOriginationInterval_Type()
)
usdBgpGlobalAsOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpGlobalAsOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpGlobalAsOriginationInterval.setUnits("seconds")


class _UsdBgpExternalAdvertisementInterval_Type(Integer32):
    """Custom type usdBgpExternalAdvertisementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpExternalAdvertisementInterval_Type.__name__ = "Integer32"
_UsdBgpExternalAdvertisementInterval_Object = MibScalar
usdBgpExternalAdvertisementInterval = _UsdBgpExternalAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 19),
    _UsdBgpExternalAdvertisementInterval_Type()
)
usdBgpExternalAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpExternalAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpExternalAdvertisementInterval.setUnits("seconds")


class _UsdBgpGlobalRibOutEnabled_Type(TruthValue):
    """Custom type usdBgpGlobalRibOutEnabled based on TruthValue"""


_UsdBgpGlobalRibOutEnabled_Object = MibScalar
usdBgpGlobalRibOutEnabled = _UsdBgpGlobalRibOutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 20),
    _UsdBgpGlobalRibOutEnabled_Type()
)
usdBgpGlobalRibOutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpGlobalRibOutEnabled.setStatus("current")


class _UsdBgpOverloadShutdown_Type(TruthValue):
    """Custom type usdBgpOverloadShutdown based on TruthValue"""


_UsdBgpOverloadShutdown_Object = MibScalar
usdBgpOverloadShutdown = _UsdBgpOverloadShutdown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 21),
    _UsdBgpOverloadShutdown_Type()
)
usdBgpOverloadShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpOverloadShutdown.setStatus("current")


class _UsdBgpLogNeighborChanges_Type(TruthValue):
    """Custom type usdBgpLogNeighborChanges based on TruthValue"""


_UsdBgpLogNeighborChanges_Object = MibScalar
usdBgpLogNeighborChanges = _UsdBgpLogNeighborChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 22),
    _UsdBgpLogNeighborChanges_Type()
)
usdBgpLogNeighborChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpLogNeighborChanges.setStatus("current")


class _UsdBgpFastExternalFallover_Type(TruthValue):
    """Custom type usdBgpFastExternalFallover based on TruthValue"""


_UsdBgpFastExternalFallover_Object = MibScalar
usdBgpFastExternalFallover = _UsdBgpFastExternalFallover_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 23),
    _UsdBgpFastExternalFallover_Type()
)
usdBgpFastExternalFallover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpFastExternalFallover.setStatus("current")


class _UsdBgpInternalAdvertisementInterval_Type(Integer32):
    """Custom type usdBgpInternalAdvertisementInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpInternalAdvertisementInterval_Type.__name__ = "Integer32"
_UsdBgpInternalAdvertisementInterval_Object = MibScalar
usdBgpInternalAdvertisementInterval = _UsdBgpInternalAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 24),
    _UsdBgpInternalAdvertisementInterval_Type()
)
usdBgpInternalAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpInternalAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpInternalAdvertisementInterval.setUnits("seconds")


class _UsdBgpMaxAsLimit_Type(Integer32):
    """Custom type usdBgpMaxAsLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpMaxAsLimit_Type.__name__ = "Integer32"
_UsdBgpMaxAsLimit_Object = MibScalar
usdBgpMaxAsLimit = _UsdBgpMaxAsLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 25),
    _UsdBgpMaxAsLimit_Type()
)
usdBgpMaxAsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpMaxAsLimit.setStatus("current")


class _UsdBgpOperationalState_Type(Integer32):
    """Custom type usdBgpOperationalState based on Integer32"""
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
        *(("down", 2),
          ("none", 0),
          ("overload", 3),
          ("up", 1))
    )


_UsdBgpOperationalState_Type.__name__ = "Integer32"
_UsdBgpOperationalState_Object = MibScalar
usdBgpOperationalState = _UsdBgpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 26),
    _UsdBgpOperationalState_Type()
)
usdBgpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpOperationalState.setStatus("current")


class _UsdBgpPreviousOperationalState_Type(Integer32):
    """Custom type usdBgpPreviousOperationalState based on Integer32"""
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
        *(("down", 2),
          ("none", 0),
          ("overload", 3),
          ("up", 1))
    )


_UsdBgpPreviousOperationalState_Type.__name__ = "Integer32"
_UsdBgpPreviousOperationalState_Object = MibScalar
usdBgpPreviousOperationalState = _UsdBgpPreviousOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 27),
    _UsdBgpPreviousOperationalState_Type()
)
usdBgpPreviousOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPreviousOperationalState.setStatus("current")


class _UsdBgpAutomaticRouteTargetFilter_Type(TruthValue):
    """Custom type usdBgpAutomaticRouteTargetFilter based on TruthValue"""


_UsdBgpAutomaticRouteTargetFilter_Object = MibScalar
usdBgpAutomaticRouteTargetFilter = _UsdBgpAutomaticRouteTargetFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 28),
    _UsdBgpAutomaticRouteTargetFilter_Type()
)
usdBgpAutomaticRouteTargetFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpAutomaticRouteTargetFilter.setStatus("current")


class _UsdBgpDefaultIPv4Unicast_Type(TruthValue):
    """Custom type usdBgpDefaultIPv4Unicast based on TruthValue"""


_UsdBgpDefaultIPv4Unicast_Object = MibScalar
usdBgpDefaultIPv4Unicast = _UsdBgpDefaultIPv4Unicast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 29),
    _UsdBgpDefaultIPv4Unicast_Type()
)
usdBgpDefaultIPv4Unicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpDefaultIPv4Unicast.setStatus("current")


class _UsdBgpRedistributeInternal_Type(TruthValue):
    """Custom type usdBgpRedistributeInternal based on TruthValue"""


_UsdBgpRedistributeInternal_Object = MibScalar
usdBgpRedistributeInternal = _UsdBgpRedistributeInternal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 30),
    _UsdBgpRedistributeInternal_Type()
)
usdBgpRedistributeInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpRedistributeInternal.setStatus("current")


class _UsdBgpUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpAdvertiseInactive", 10),
          ("usdBgpAlwaysCompareMed", 3),
          ("usdBgpAutomaticRouteTargetFilter", 24),
          ("usdBgpClientToClientReflection", 6),
          ("usdBgpClusterId", 7),
          ("usdBgpConfedCompareMed", 12),
          ("usdBgpConfederationId", 8),
          ("usdBgpDefaultIPv4Unicast", 25),
          ("usdBgpDefaultLocalPreference", 4),
          ("usdBgpEnabled", 1),
          ("usdBgpEnforceFirstAs", 11),
          ("usdBgpEqualCostLimit", 5),
          ("usdBgpExternalAdvertisementInterval", 17),
          ("usdBgpFastExternalFallover", 21),
          ("usdBgpGlobalAsOriginationInterval", 16),
          ("usdBgpGlobalConfigHoldTime", 15),
          ("usdBgpGlobalConfigKeepAliveInterval", 14),
          ("usdBgpGlobalRetryInterval", 13),
          ("usdBgpGlobalRibOutEnabled", 18),
          ("usdBgpIdentifier", 2),
          ("usdBgpInternalAdvertisementInterval", 22),
          ("usdBgpLocalAsNumber", 0),
          ("usdBgpLogNeighborChanges", 20),
          ("usdBgpMaxAsLimit", 23),
          ("usdBgpMissingAsWorst", 9),
          ("usdBgpOverloadShutdown", 19),
          ("usdBgpRedistributeInternal", 26))
    )

_UsdBgpUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpUnconfiguredAttributes_Object = MibScalar
usdBgpUnconfiguredAttributes = _UsdBgpUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 33),
    _UsdBgpUnconfiguredAttributes_Type()
)
usdBgpUnconfiguredAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpUnconfiguredAttributes.setStatus("current")
_UsdBgpRouteTableStatisticsGroup_ObjectIdentity = ObjectIdentity
usdBgpRouteTableStatisticsGroup = _UsdBgpRouteTableStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2)
)
_UsdBgpBaselineTime_Type = Unsigned32
_UsdBgpBaselineTime_Object = MibScalar
usdBgpBaselineTime = _UsdBgpBaselineTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 1),
    _UsdBgpBaselineTime_Type()
)
usdBgpBaselineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpBaselineTime.setStatus("current")
_UsdBgpDestinationCount_Type = Gauge32
_UsdBgpDestinationCount_Object = MibScalar
usdBgpDestinationCount = _UsdBgpDestinationCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 2),
    _UsdBgpDestinationCount_Type()
)
usdBgpDestinationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpDestinationCount.setStatus("current")
_UsdBgpDestinationMemoryUsed_Type = Gauge32
_UsdBgpDestinationMemoryUsed_Object = MibScalar
usdBgpDestinationMemoryUsed = _UsdBgpDestinationMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 3),
    _UsdBgpDestinationMemoryUsed_Type()
)
usdBgpDestinationMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpDestinationMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpDestinationMemoryUsed.setUnits("bytes")
_UsdBgpRouteCount_Type = Gauge32
_UsdBgpRouteCount_Object = MibScalar
usdBgpRouteCount = _UsdBgpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 4),
    _UsdBgpRouteCount_Type()
)
usdBgpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteCount.setStatus("current")
_UsdBgpRouteMemoryUsed_Type = Gauge32
_UsdBgpRouteMemoryUsed_Object = MibScalar
usdBgpRouteMemoryUsed = _UsdBgpRouteMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 5),
    _UsdBgpRouteMemoryUsed_Type()
)
usdBgpRouteMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpRouteMemoryUsed.setUnits("bytes")
_UsdBgpSelectedRouteCount_Type = Gauge32
_UsdBgpSelectedRouteCount_Object = MibScalar
usdBgpSelectedRouteCount = _UsdBgpSelectedRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 6),
    _UsdBgpSelectedRouteCount_Type()
)
usdBgpSelectedRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpSelectedRouteCount.setStatus("current")
_UsdBgpPathAttributeCount_Type = Gauge32
_UsdBgpPathAttributeCount_Object = MibScalar
usdBgpPathAttributeCount = _UsdBgpPathAttributeCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 8),
    _UsdBgpPathAttributeCount_Type()
)
usdBgpPathAttributeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPathAttributeCount.setStatus("current")
_UsdBgpPathAttributeMemoryUsed_Type = Gauge32
_UsdBgpPathAttributeMemoryUsed_Object = MibScalar
usdBgpPathAttributeMemoryUsed = _UsdBgpPathAttributeMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 9),
    _UsdBgpPathAttributeMemoryUsed_Type()
)
usdBgpPathAttributeMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPathAttributeMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPathAttributeMemoryUsed.setUnits("bytes")
_UsdBgpRouteFlapHistoryCount_Type = Gauge32
_UsdBgpRouteFlapHistoryCount_Object = MibScalar
usdBgpRouteFlapHistoryCount = _UsdBgpRouteFlapHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 10),
    _UsdBgpRouteFlapHistoryCount_Type()
)
usdBgpRouteFlapHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapHistoryCount.setStatus("current")
_UsdBgpRouteFlapHistoryMemoryUsed_Type = Gauge32
_UsdBgpRouteFlapHistoryMemoryUsed_Object = MibScalar
usdBgpRouteFlapHistoryMemoryUsed = _UsdBgpRouteFlapHistoryMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 11),
    _UsdBgpRouteFlapHistoryMemoryUsed_Type()
)
usdBgpRouteFlapHistoryMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapHistoryMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpRouteFlapHistoryMemoryUsed.setUnits("bytes")
_UsdBgpSuppressedRouteCount_Type = Gauge32
_UsdBgpSuppressedRouteCount_Object = MibScalar
usdBgpSuppressedRouteCount = _UsdBgpSuppressedRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 12),
    _UsdBgpSuppressedRouteCount_Type()
)
usdBgpSuppressedRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpSuppressedRouteCount.setStatus("current")
_UsdBgpConfederationPeerTable_Object = MibTable
usdBgpConfederationPeerTable = _UsdBgpConfederationPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    usdBgpConfederationPeerTable.setStatus("current")
_UsdBgpConfederationPeerEntry_Object = MibTableRow
usdBgpConfederationPeerEntry = _UsdBgpConfederationPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3, 1)
)
usdBgpConfederationPeerEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpConfederationPeerAsNumber"),
)
if mibBuilder.loadTexts:
    usdBgpConfederationPeerEntry.setStatus("current")


class _UsdBgpConfederationPeerAsNumber_Type(Integer32):
    """Custom type usdBgpConfederationPeerAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpConfederationPeerAsNumber_Type.__name__ = "Integer32"
_UsdBgpConfederationPeerAsNumber_Object = MibTableColumn
usdBgpConfederationPeerAsNumber = _UsdBgpConfederationPeerAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3, 1, 1),
    _UsdBgpConfederationPeerAsNumber_Type()
)
usdBgpConfederationPeerAsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpConfederationPeerAsNumber.setStatus("current")
_UsdBgpConfederationPeerRowStatus_Type = RowStatus
_UsdBgpConfederationPeerRowStatus_Object = MibTableColumn
usdBgpConfederationPeerRowStatus = _UsdBgpConfederationPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3, 1, 2),
    _UsdBgpConfederationPeerRowStatus_Type()
)
usdBgpConfederationPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpConfederationPeerRowStatus.setStatus("current")
_UsdBgpPeerTable_Object = MibTable
usdBgpPeerTable = _UsdBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    usdBgpPeerTable.setStatus("current")
_UsdBgpPeerEntry_Object = MibTableRow
usdBgpPeerEntry = _UsdBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1)
)
usdBgpPeerEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerRemoteAddress"),
)
if mibBuilder.loadTexts:
    usdBgpPeerEntry.setStatus("current")
_UsdBgpPeerVrfName_Type = UsdVrfName
_UsdBgpPeerVrfName_Object = MibTableColumn
usdBgpPeerVrfName = _UsdBgpPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 1),
    _UsdBgpPeerVrfName_Type()
)
usdBgpPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerVrfName.setStatus("current")
_UsdBgpPeerRemoteAddress_Type = IpAddress
_UsdBgpPeerRemoteAddress_Object = MibTableColumn
usdBgpPeerRemoteAddress = _UsdBgpPeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 2),
    _UsdBgpPeerRemoteAddress_Type()
)
usdBgpPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerRemoteAddress.setStatus("current")


class _UsdBgpPeerAdminStatus_Type(Integer32):
    """Custom type usdBgpPeerAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )


_UsdBgpPeerAdminStatus_Type.__name__ = "Integer32"
_UsdBgpPeerAdminStatus_Object = MibTableColumn
usdBgpPeerAdminStatus = _UsdBgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 3),
    _UsdBgpPeerAdminStatus_Type()
)
usdBgpPeerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAdminStatus.setStatus("current")


class _UsdBgpPeerState_Type(Integer32):
    """Custom type usdBgpPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4),
          ("removing", 7),
          ("stop", 0))
    )


_UsdBgpPeerState_Type.__name__ = "Integer32"
_UsdBgpPeerState_Object = MibTableColumn
usdBgpPeerState = _UsdBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 4),
    _UsdBgpPeerState_Type()
)
usdBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerState.setStatus("current")
_UsdBgpPeerNegotiatedVersion_Type = Integer32
_UsdBgpPeerNegotiatedVersion_Object = MibTableColumn
usdBgpPeerNegotiatedVersion = _UsdBgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 5),
    _UsdBgpPeerNegotiatedVersion_Type()
)
usdBgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerNegotiatedVersion.setStatus("current")
_UsdBgpPeerLocalAddress_Type = IpAddress
_UsdBgpPeerLocalAddress_Object = MibTableColumn
usdBgpPeerLocalAddress = _UsdBgpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 6),
    _UsdBgpPeerLocalAddress_Type()
)
usdBgpPeerLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerLocalAddress.setStatus("current")
_UsdBgpPeerLocalAddressMask_Type = IpAddress
_UsdBgpPeerLocalAddressMask_Object = MibTableColumn
usdBgpPeerLocalAddressMask = _UsdBgpPeerLocalAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 7),
    _UsdBgpPeerLocalAddressMask_Type()
)
usdBgpPeerLocalAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerLocalAddressMask.setStatus("current")


class _UsdBgpPeerLocalPort_Type(Integer32):
    """Custom type usdBgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpPeerLocalPort_Type.__name__ = "Integer32"
_UsdBgpPeerLocalPort_Object = MibTableColumn
usdBgpPeerLocalPort = _UsdBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 8),
    _UsdBgpPeerLocalPort_Type()
)
usdBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerLocalPort.setStatus("current")


class _UsdBgpPeerRemoteAsNumber_Type(Integer32):
    """Custom type usdBgpPeerRemoteAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpPeerRemoteAsNumber_Type.__name__ = "Integer32"
_UsdBgpPeerRemoteAsNumber_Object = MibTableColumn
usdBgpPeerRemoteAsNumber = _UsdBgpPeerRemoteAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 9),
    _UsdBgpPeerRemoteAsNumber_Type()
)
usdBgpPeerRemoteAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerRemoteAsNumber.setStatus("current")


class _UsdBgpPeerRemotePort_Type(Integer32):
    """Custom type usdBgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpPeerRemotePort_Type.__name__ = "Integer32"
_UsdBgpPeerRemotePort_Object = MibTableColumn
usdBgpPeerRemotePort = _UsdBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 10),
    _UsdBgpPeerRemotePort_Type()
)
usdBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerRemotePort.setStatus("current")
_UsdBgpPeerInUpdates_Type = Counter32
_UsdBgpPeerInUpdates_Object = MibTableColumn
usdBgpPeerInUpdates = _UsdBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 11),
    _UsdBgpPeerInUpdates_Type()
)
usdBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerInUpdates.setStatus("current")
_UsdBgpPeerOutUpdates_Type = Counter32
_UsdBgpPeerOutUpdates_Object = MibTableColumn
usdBgpPeerOutUpdates = _UsdBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 12),
    _UsdBgpPeerOutUpdates_Type()
)
usdBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerOutUpdates.setStatus("current")
_UsdBgpPeerInTotalMessages_Type = Counter32
_UsdBgpPeerInTotalMessages_Object = MibTableColumn
usdBgpPeerInTotalMessages = _UsdBgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 13),
    _UsdBgpPeerInTotalMessages_Type()
)
usdBgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerInTotalMessages.setStatus("current")
_UsdBgpPeerOutTotalMessages_Type = Counter32
_UsdBgpPeerOutTotalMessages_Object = MibTableColumn
usdBgpPeerOutTotalMessages = _UsdBgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 14),
    _UsdBgpPeerOutTotalMessages_Type()
)
usdBgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerOutTotalMessages.setStatus("current")


class _UsdBgpPeerLastErrorCode_Type(OctetString):
    """Custom type usdBgpPeerLastErrorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_UsdBgpPeerLastErrorCode_Type.__name__ = "OctetString"
_UsdBgpPeerLastErrorCode_Object = MibTableColumn
usdBgpPeerLastErrorCode = _UsdBgpPeerLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 15),
    _UsdBgpPeerLastErrorCode_Type()
)
usdBgpPeerLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerLastErrorCode.setStatus("current")
_UsdBgpPeerLastResetReason_Type = DisplayString
_UsdBgpPeerLastResetReason_Object = MibTableColumn
usdBgpPeerLastResetReason = _UsdBgpPeerLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 16),
    _UsdBgpPeerLastResetReason_Type()
)
usdBgpPeerLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerLastResetReason.setStatus("current")
_UsdBgpPeerFsmEstablishedTransitions_Type = Counter32
_UsdBgpPeerFsmEstablishedTransitions_Object = MibTableColumn
usdBgpPeerFsmEstablishedTransitions = _UsdBgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 17),
    _UsdBgpPeerFsmEstablishedTransitions_Type()
)
usdBgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerFsmEstablishedTransitions.setStatus("current")
_UsdBgpPeerFsmEstablishedTime_Type = Gauge32
_UsdBgpPeerFsmEstablishedTime_Object = MibTableColumn
usdBgpPeerFsmEstablishedTime = _UsdBgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 18),
    _UsdBgpPeerFsmEstablishedTime_Type()
)
usdBgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerFsmEstablishedTime.setUnits("seconds")


class _UsdBgpPeerRetryInterval_Type(Integer32):
    """Custom type usdBgpPeerRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpPeerRetryInterval_Type.__name__ = "Integer32"
_UsdBgpPeerRetryInterval_Object = MibTableColumn
usdBgpPeerRetryInterval = _UsdBgpPeerRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 19),
    _UsdBgpPeerRetryInterval_Type()
)
usdBgpPeerRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerRetryInterval.setUnits("seconds")


class _UsdBgpPeerHoldTime_Type(Integer32):
    """Custom type usdBgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_UsdBgpPeerHoldTime_Type.__name__ = "Integer32"
_UsdBgpPeerHoldTime_Object = MibTableColumn
usdBgpPeerHoldTime = _UsdBgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 20),
    _UsdBgpPeerHoldTime_Type()
)
usdBgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerHoldTime.setUnits("seconds")


class _UsdBgpPeerKeepAliveInterval_Type(Integer32):
    """Custom type usdBgpPeerKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_UsdBgpPeerKeepAliveInterval_Type.__name__ = "Integer32"
_UsdBgpPeerKeepAliveInterval_Object = MibTableColumn
usdBgpPeerKeepAliveInterval = _UsdBgpPeerKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 21),
    _UsdBgpPeerKeepAliveInterval_Type()
)
usdBgpPeerKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerKeepAliveInterval.setUnits("seconds")


class _UsdBgpPeerConfigHoldTime_Type(Integer32):
    """Custom type usdBgpPeerConfigHoldTime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_UsdBgpPeerConfigHoldTime_Type.__name__ = "Integer32"
_UsdBgpPeerConfigHoldTime_Object = MibTableColumn
usdBgpPeerConfigHoldTime = _UsdBgpPeerConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 22),
    _UsdBgpPeerConfigHoldTime_Type()
)
usdBgpPeerConfigHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerConfigHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerConfigHoldTime.setUnits("seconds")


class _UsdBgpPeerConfigKeepAliveInterval_Type(Integer32):
    """Custom type usdBgpPeerConfigKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_UsdBgpPeerConfigKeepAliveInterval_Type.__name__ = "Integer32"
_UsdBgpPeerConfigKeepAliveInterval_Object = MibTableColumn
usdBgpPeerConfigKeepAliveInterval = _UsdBgpPeerConfigKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 23),
    _UsdBgpPeerConfigKeepAliveInterval_Type()
)
usdBgpPeerConfigKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerConfigKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerConfigKeepAliveInterval.setUnits("seconds")


class _UsdBgpPeerAsOriginationInterval_Type(Integer32):
    """Custom type usdBgpPeerAsOriginationInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpPeerAsOriginationInterval_Type.__name__ = "Integer32"
_UsdBgpPeerAsOriginationInterval_Object = MibTableColumn
usdBgpPeerAsOriginationInterval = _UsdBgpPeerAsOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 24),
    _UsdBgpPeerAsOriginationInterval_Type()
)
usdBgpPeerAsOriginationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAsOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerAsOriginationInterval.setUnits("seconds")


class _UsdBgpPeerAdvertisementInterval_Type(Integer32):
    """Custom type usdBgpPeerAdvertisementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpPeerAdvertisementInterval_Type.__name__ = "Integer32"
_UsdBgpPeerAdvertisementInterval_Object = MibTableColumn
usdBgpPeerAdvertisementInterval = _UsdBgpPeerAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 25),
    _UsdBgpPeerAdvertisementInterval_Type()
)
usdBgpPeerAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerAdvertisementInterval.setUnits("seconds")
_UsdBgpPeerInUpdateElapsedTime_Type = Gauge32
_UsdBgpPeerInUpdateElapsedTime_Object = MibTableColumn
usdBgpPeerInUpdateElapsedTime = _UsdBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 26),
    _UsdBgpPeerInUpdateElapsedTime_Type()
)
usdBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerInUpdateElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerInUpdateElapsedTime.setUnits("seconds")


class _UsdBgpPeerDescription_Type(DisplayString):
    """Custom type usdBgpPeerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UsdBgpPeerDescription_Type.__name__ = "DisplayString"
_UsdBgpPeerDescription_Object = MibTableColumn
usdBgpPeerDescription = _UsdBgpPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 27),
    _UsdBgpPeerDescription_Type()
)
usdBgpPeerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerDescription.setStatus("current")
_UsdBgpPeerRemoteIdentifier_Type = IpAddress
_UsdBgpPeerRemoteIdentifier_Object = MibTableColumn
usdBgpPeerRemoteIdentifier = _UsdBgpPeerRemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 28),
    _UsdBgpPeerRemoteIdentifier_Type()
)
usdBgpPeerRemoteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerRemoteIdentifier.setStatus("current")


class _UsdBgpPeerWeight_Type(Unsigned32):
    """Custom type usdBgpPeerWeight based on Unsigned32"""
    defaultValue = 0


_UsdBgpPeerWeight_Object = MibTableColumn
usdBgpPeerWeight = _UsdBgpPeerWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 29),
    _UsdBgpPeerWeight_Type()
)
usdBgpPeerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerWeight.setStatus("current")


class _UsdBgpPeerEbgpMultihop_Type(TruthValue):
    """Custom type usdBgpPeerEbgpMultihop based on TruthValue"""


_UsdBgpPeerEbgpMultihop_Object = MibTableColumn
usdBgpPeerEbgpMultihop = _UsdBgpPeerEbgpMultihop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 30),
    _UsdBgpPeerEbgpMultihop_Type()
)
usdBgpPeerEbgpMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerEbgpMultihop.setStatus("current")


class _UsdBgpPeerEbgpMultihopTtl_Type(Integer32):
    """Custom type usdBgpPeerEbgpMultihopTtl based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdBgpPeerEbgpMultihopTtl_Type.__name__ = "Integer32"
_UsdBgpPeerEbgpMultihopTtl_Object = MibTableColumn
usdBgpPeerEbgpMultihopTtl = _UsdBgpPeerEbgpMultihopTtl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 31),
    _UsdBgpPeerEbgpMultihopTtl_Type()
)
usdBgpPeerEbgpMultihopTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerEbgpMultihopTtl.setStatus("current")


class _UsdBgpPeerUpdateSource_Type(IpAddress):
    """Custom type usdBgpPeerUpdateSource based on IpAddress"""
    defaultValue = 0


_UsdBgpPeerUpdateSource_Object = MibTableColumn
usdBgpPeerUpdateSource = _UsdBgpPeerUpdateSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 32),
    _UsdBgpPeerUpdateSource_Type()
)
usdBgpPeerUpdateSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerUpdateSource.setStatus("current")


class _UsdBgpPeerMd5Password_Type(OctetString):
    """Custom type usdBgpPeerMd5Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerMd5Password_Type.__name__ = "OctetString"
_UsdBgpPeerMd5Password_Object = MibTableColumn
usdBgpPeerMd5Password = _UsdBgpPeerMd5Password_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 33),
    _UsdBgpPeerMd5Password_Type()
)
usdBgpPeerMd5Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerMd5Password.setStatus("current")


class _UsdBgpPeerMaxUpdateSize_Type(Unsigned32):
    """Custom type usdBgpPeerMaxUpdateSize based on Unsigned32"""
    defaultValue = 4096


_UsdBgpPeerMaxUpdateSize_Object = MibTableColumn
usdBgpPeerMaxUpdateSize = _UsdBgpPeerMaxUpdateSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 34),
    _UsdBgpPeerMaxUpdateSize_Type()
)
usdBgpPeerMaxUpdateSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerMaxUpdateSize.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerMaxUpdateSize.setUnits("bytes")


class _UsdBgpPeerType_Type(Integer32):
    """Custom type usdBgpPeerType based on Integer32"""
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
        *(("peerTypeConfederation", 3),
          ("peerTypeExternal", 2),
          ("peerTypeInternal", 1),
          ("peerTypeUnknown", 4))
    )


_UsdBgpPeerType_Type.__name__ = "Integer32"
_UsdBgpPeerType_Object = MibTableColumn
usdBgpPeerType = _UsdBgpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 35),
    _UsdBgpPeerType_Type()
)
usdBgpPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerType.setStatus("current")
_UsdBgpPeerSupportsCapabilityNegotiation_Type = TruthValue
_UsdBgpPeerSupportsCapabilityNegotiation_Object = MibTableColumn
usdBgpPeerSupportsCapabilityNegotiation = _UsdBgpPeerSupportsCapabilityNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 36),
    _UsdBgpPeerSupportsCapabilityNegotiation_Type()
)
usdBgpPeerSupportsCapabilityNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerSupportsCapabilityNegotiation.setStatus("current")
_UsdBgpPeerCapabilityMultiProtocol_Type = TruthValue
_UsdBgpPeerCapabilityMultiProtocol_Object = MibTableColumn
usdBgpPeerCapabilityMultiProtocol = _UsdBgpPeerCapabilityMultiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 37),
    _UsdBgpPeerCapabilityMultiProtocol_Type()
)
usdBgpPeerCapabilityMultiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerCapabilityMultiProtocol.setStatus("current")
_UsdBgpPeerCapabilityRouteRefresh_Type = TruthValue
_UsdBgpPeerCapabilityRouteRefresh_Object = MibTableColumn
usdBgpPeerCapabilityRouteRefresh = _UsdBgpPeerCapabilityRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 38),
    _UsdBgpPeerCapabilityRouteRefresh_Type()
)
usdBgpPeerCapabilityRouteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerCapabilityRouteRefresh.setStatus("current")
_UsdBgpPeerCapabilityRouteRefreshCiscoProprietary_Type = TruthValue
_UsdBgpPeerCapabilityRouteRefreshCiscoProprietary_Object = MibTableColumn
usdBgpPeerCapabilityRouteRefreshCiscoProprietary = _UsdBgpPeerCapabilityRouteRefreshCiscoProprietary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 39),
    _UsdBgpPeerCapabilityRouteRefreshCiscoProprietary_Type()
)
usdBgpPeerCapabilityRouteRefreshCiscoProprietary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerCapabilityRouteRefreshCiscoProprietary.setStatus("current")


class _UsdBgpPeerResetConnectionType_Type(UsdBgpResetConnectionType):
    """Custom type usdBgpPeerResetConnectionType based on UsdBgpResetConnectionType"""


_UsdBgpPeerResetConnectionType_Object = MibTableColumn
usdBgpPeerResetConnectionType = _UsdBgpPeerResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 40),
    _UsdBgpPeerResetConnectionType_Type()
)
usdBgpPeerResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerResetConnectionType.setStatus("current")
_UsdBgpPeerRowStatus_Type = RowStatus
_UsdBgpPeerRowStatus_Object = MibTableColumn
usdBgpPeerRowStatus = _UsdBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 41),
    _UsdBgpPeerRowStatus_Type()
)
usdBgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerRowStatus.setStatus("current")


class _UsdBgpPeerLocalAsNumber_Type(Integer32):
    """Custom type usdBgpPeerLocalAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpPeerLocalAsNumber_Type.__name__ = "Integer32"
_UsdBgpPeerLocalAsNumber_Object = MibTableColumn
usdBgpPeerLocalAsNumber = _UsdBgpPeerLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 42),
    _UsdBgpPeerLocalAsNumber_Type()
)
usdBgpPeerLocalAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerLocalAsNumber.setStatus("current")


class _UsdBgpPeerUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpPeerUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpPeerAdminStatus", 0),
          ("usdBgpPeerAdvertisementInterval", 6),
          ("usdBgpPeerAsOriginationInterval", 5),
          ("usdBgpPeerConfigHoldTime", 3),
          ("usdBgpPeerConfigKeepAliveInterval", 4),
          ("usdBgpPeerDescription", 7),
          ("usdBgpPeerEbgpMultihop", 9),
          ("usdBgpPeerEbgpMultihopTtl", 10),
          ("usdBgpPeerLocalAsNumber", 14),
          ("usdBgpPeerMaxUpdateSize", 13),
          ("usdBgpPeerMd5Password", 12),
          ("usdBgpPeerRemoteAsNumber", 1),
          ("usdBgpPeerRetryInterval", 2),
          ("usdBgpPeerUpdateSource", 11),
          ("usdBgpPeerWeight", 8))
    )

_UsdBgpPeerUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpPeerUnconfiguredAttributes_Object = MibTableColumn
usdBgpPeerUnconfiguredAttributes = _UsdBgpPeerUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 60),
    _UsdBgpPeerUnconfiguredAttributes_Type()
)
usdBgpPeerUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerUnconfiguredAttributes.setStatus("current")
_UsdBgpPeerProposedAfiSafiPeerTable_Object = MibTable
usdBgpPeerProposedAfiSafiPeerTable = _UsdBgpPeerProposedAfiSafiPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5)
)
if mibBuilder.loadTexts:
    usdBgpPeerProposedAfiSafiPeerTable.setStatus("current")
_UsdBgpPeerProposedAfiSafiPeerEntry_Object = MibTableRow
usdBgpPeerProposedAfiSafiPeerEntry = _UsdBgpPeerProposedAfiSafiPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1)
)
usdBgpPeerProposedAfiSafiPeerEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerProposedAfiSafiPeerVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerProposedAfiSafiPeerRemoteAddr"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerProposedAfiSafiPeerAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerProposedAfiSafiPeerSafi"),
)
if mibBuilder.loadTexts:
    usdBgpPeerProposedAfiSafiPeerEntry.setStatus("current")
_UsdBgpPeerProposedAfiSafiPeerVrfName_Type = UsdVrfName
_UsdBgpPeerProposedAfiSafiPeerVrfName_Object = MibTableColumn
usdBgpPeerProposedAfiSafiPeerVrfName = _UsdBgpPeerProposedAfiSafiPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 1),
    _UsdBgpPeerProposedAfiSafiPeerVrfName_Type()
)
usdBgpPeerProposedAfiSafiPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerProposedAfiSafiPeerVrfName.setStatus("current")
_UsdBgpPeerProposedAfiSafiPeerRemoteAddr_Type = IpAddress
_UsdBgpPeerProposedAfiSafiPeerRemoteAddr_Object = MibTableColumn
usdBgpPeerProposedAfiSafiPeerRemoteAddr = _UsdBgpPeerProposedAfiSafiPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 2),
    _UsdBgpPeerProposedAfiSafiPeerRemoteAddr_Type()
)
usdBgpPeerProposedAfiSafiPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerProposedAfiSafiPeerRemoteAddr.setStatus("current")
_UsdBgpPeerProposedAfiSafiPeerAfi_Type = UsdBgpAfi
_UsdBgpPeerProposedAfiSafiPeerAfi_Object = MibTableColumn
usdBgpPeerProposedAfiSafiPeerAfi = _UsdBgpPeerProposedAfiSafiPeerAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 3),
    _UsdBgpPeerProposedAfiSafiPeerAfi_Type()
)
usdBgpPeerProposedAfiSafiPeerAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerProposedAfiSafiPeerAfi.setStatus("current")
_UsdBgpPeerProposedAfiSafiPeerSafi_Type = UsdBgpSafi
_UsdBgpPeerProposedAfiSafiPeerSafi_Object = MibTableColumn
usdBgpPeerProposedAfiSafiPeerSafi = _UsdBgpPeerProposedAfiSafiPeerSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 4),
    _UsdBgpPeerProposedAfiSafiPeerSafi_Type()
)
usdBgpPeerProposedAfiSafiPeerSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerProposedAfiSafiPeerSafi.setStatus("current")
_UsdBgpPeerProposedAfiSafiPeerRowStatus_Type = RowStatus
_UsdBgpPeerProposedAfiSafiPeerRowStatus_Object = MibTableColumn
usdBgpPeerProposedAfiSafiPeerRowStatus = _UsdBgpPeerProposedAfiSafiPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 5),
    _UsdBgpPeerProposedAfiSafiPeerRowStatus_Type()
)
usdBgpPeerProposedAfiSafiPeerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpPeerProposedAfiSafiPeerRowStatus.setStatus("current")
_UsdBgpLocalProposedAfiSafiPeerTable_Object = MibTable
usdBgpLocalProposedAfiSafiPeerTable = _UsdBgpLocalProposedAfiSafiPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6)
)
if mibBuilder.loadTexts:
    usdBgpLocalProposedAfiSafiPeerTable.setStatus("current")
_UsdBgpLocalProposedAfiSafiPeerEntry_Object = MibTableRow
usdBgpLocalProposedAfiSafiPeerEntry = _UsdBgpLocalProposedAfiSafiPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1)
)
usdBgpLocalProposedAfiSafiPeerEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpLocalProposedAfiSafiPeerVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpLocalProposedAfiSafiPeerRemoteAddr"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpLocalProposedAfiSafiPeerAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpLocalProposedAfiSafiPeerSafi"),
)
if mibBuilder.loadTexts:
    usdBgpLocalProposedAfiSafiPeerEntry.setStatus("current")
_UsdBgpLocalProposedAfiSafiPeerVrfName_Type = UsdVrfName
_UsdBgpLocalProposedAfiSafiPeerVrfName_Object = MibTableColumn
usdBgpLocalProposedAfiSafiPeerVrfName = _UsdBgpLocalProposedAfiSafiPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 1),
    _UsdBgpLocalProposedAfiSafiPeerVrfName_Type()
)
usdBgpLocalProposedAfiSafiPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpLocalProposedAfiSafiPeerVrfName.setStatus("current")
_UsdBgpLocalProposedAfiSafiPeerRemoteAddr_Type = IpAddress
_UsdBgpLocalProposedAfiSafiPeerRemoteAddr_Object = MibTableColumn
usdBgpLocalProposedAfiSafiPeerRemoteAddr = _UsdBgpLocalProposedAfiSafiPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 2),
    _UsdBgpLocalProposedAfiSafiPeerRemoteAddr_Type()
)
usdBgpLocalProposedAfiSafiPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpLocalProposedAfiSafiPeerRemoteAddr.setStatus("current")
_UsdBgpLocalProposedAfiSafiPeerAfi_Type = UsdBgpAfi
_UsdBgpLocalProposedAfiSafiPeerAfi_Object = MibTableColumn
usdBgpLocalProposedAfiSafiPeerAfi = _UsdBgpLocalProposedAfiSafiPeerAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 3),
    _UsdBgpLocalProposedAfiSafiPeerAfi_Type()
)
usdBgpLocalProposedAfiSafiPeerAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpLocalProposedAfiSafiPeerAfi.setStatus("current")
_UsdBgpLocalProposedAfiSafiPeerSafi_Type = UsdBgpSafi
_UsdBgpLocalProposedAfiSafiPeerSafi_Object = MibTableColumn
usdBgpLocalProposedAfiSafiPeerSafi = _UsdBgpLocalProposedAfiSafiPeerSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 4),
    _UsdBgpLocalProposedAfiSafiPeerSafi_Type()
)
usdBgpLocalProposedAfiSafiPeerSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpLocalProposedAfiSafiPeerSafi.setStatus("current")
_UsdBgpLocalProposedAfiSafiPeerRowStatus_Type = RowStatus
_UsdBgpLocalProposedAfiSafiPeerRowStatus_Object = MibTableColumn
usdBgpLocalProposedAfiSafiPeerRowStatus = _UsdBgpLocalProposedAfiSafiPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 5),
    _UsdBgpLocalProposedAfiSafiPeerRowStatus_Type()
)
usdBgpLocalProposedAfiSafiPeerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpLocalProposedAfiSafiPeerRowStatus.setStatus("current")
_UsdBgpExchangedAfiSafiPeerTable_Object = MibTable
usdBgpExchangedAfiSafiPeerTable = _UsdBgpExchangedAfiSafiPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7)
)
if mibBuilder.loadTexts:
    usdBgpExchangedAfiSafiPeerTable.setStatus("current")
_UsdBgpExchangedAfiSafiPeerEntry_Object = MibTableRow
usdBgpExchangedAfiSafiPeerEntry = _UsdBgpExchangedAfiSafiPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1)
)
usdBgpExchangedAfiSafiPeerEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpExchangedAfiSafiPeerVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpExchangedAfiSafiPeerRemoteAddr"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpExchangedAfiSafiPeerAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpExchangedAfiSafiPeerSafi"),
)
if mibBuilder.loadTexts:
    usdBgpExchangedAfiSafiPeerEntry.setStatus("current")
_UsdBgpExchangedAfiSafiPeerVrfName_Type = UsdVrfName
_UsdBgpExchangedAfiSafiPeerVrfName_Object = MibTableColumn
usdBgpExchangedAfiSafiPeerVrfName = _UsdBgpExchangedAfiSafiPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 1),
    _UsdBgpExchangedAfiSafiPeerVrfName_Type()
)
usdBgpExchangedAfiSafiPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpExchangedAfiSafiPeerVrfName.setStatus("current")
_UsdBgpExchangedAfiSafiPeerRemoteAddr_Type = IpAddress
_UsdBgpExchangedAfiSafiPeerRemoteAddr_Object = MibTableColumn
usdBgpExchangedAfiSafiPeerRemoteAddr = _UsdBgpExchangedAfiSafiPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 2),
    _UsdBgpExchangedAfiSafiPeerRemoteAddr_Type()
)
usdBgpExchangedAfiSafiPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpExchangedAfiSafiPeerRemoteAddr.setStatus("current")
_UsdBgpExchangedAfiSafiPeerAfi_Type = UsdBgpAfi
_UsdBgpExchangedAfiSafiPeerAfi_Object = MibTableColumn
usdBgpExchangedAfiSafiPeerAfi = _UsdBgpExchangedAfiSafiPeerAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 3),
    _UsdBgpExchangedAfiSafiPeerAfi_Type()
)
usdBgpExchangedAfiSafiPeerAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpExchangedAfiSafiPeerAfi.setStatus("current")
_UsdBgpExchangedAfiSafiPeerSafi_Type = UsdBgpSafi
_UsdBgpExchangedAfiSafiPeerSafi_Object = MibTableColumn
usdBgpExchangedAfiSafiPeerSafi = _UsdBgpExchangedAfiSafiPeerSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 4),
    _UsdBgpExchangedAfiSafiPeerSafi_Type()
)
usdBgpExchangedAfiSafiPeerSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpExchangedAfiSafiPeerSafi.setStatus("current")
_UsdBgpExchangedAfiSafiPeerRowStatus_Type = RowStatus
_UsdBgpExchangedAfiSafiPeerRowStatus_Object = MibTableColumn
usdBgpExchangedAfiSafiPeerRowStatus = _UsdBgpExchangedAfiSafiPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 5),
    _UsdBgpExchangedAfiSafiPeerRowStatus_Type()
)
usdBgpExchangedAfiSafiPeerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpExchangedAfiSafiPeerRowStatus.setStatus("current")
_UsdBgpPeerAddressFamilyTable_Object = MibTable
usdBgpPeerAddressFamilyTable = _UsdBgpPeerAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8)
)
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyTable.setStatus("current")
_UsdBgpPeerAddressFamilyEntry_Object = MibTableRow
usdBgpPeerAddressFamilyEntry = _UsdBgpPeerAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1)
)
usdBgpPeerAddressFamilyEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilySafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRemoteAddress"),
)
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyEntry.setStatus("current")
_UsdBgpPeerAddressFamilyVrfName_Type = UsdVrfName
_UsdBgpPeerAddressFamilyVrfName_Object = MibTableColumn
usdBgpPeerAddressFamilyVrfName = _UsdBgpPeerAddressFamilyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 1),
    _UsdBgpPeerAddressFamilyVrfName_Type()
)
usdBgpPeerAddressFamilyVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyVrfName.setStatus("current")
_UsdBgpPeerAddressFamilyAfi_Type = UsdBgpAfi
_UsdBgpPeerAddressFamilyAfi_Object = MibTableColumn
usdBgpPeerAddressFamilyAfi = _UsdBgpPeerAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 2),
    _UsdBgpPeerAddressFamilyAfi_Type()
)
usdBgpPeerAddressFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyAfi.setStatus("current")
_UsdBgpPeerAddressFamilySafi_Type = UsdBgpSafi
_UsdBgpPeerAddressFamilySafi_Object = MibTableColumn
usdBgpPeerAddressFamilySafi = _UsdBgpPeerAddressFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 3),
    _UsdBgpPeerAddressFamilySafi_Type()
)
usdBgpPeerAddressFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilySafi.setStatus("current")
_UsdBgpPeerAddressFamilyRemoteAddress_Type = IpAddress
_UsdBgpPeerAddressFamilyRemoteAddress_Object = MibTableColumn
usdBgpPeerAddressFamilyRemoteAddress = _UsdBgpPeerAddressFamilyRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 4),
    _UsdBgpPeerAddressFamilyRemoteAddress_Type()
)
usdBgpPeerAddressFamilyRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRemoteAddress.setStatus("current")


class _UsdBgpPeerAddressFamilyPeerGroup_Type(DisplayString):
    """Custom type usdBgpPeerAddressFamilyPeerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerAddressFamilyPeerGroup_Type.__name__ = "DisplayString"
_UsdBgpPeerAddressFamilyPeerGroup_Object = MibTableColumn
usdBgpPeerAddressFamilyPeerGroup = _UsdBgpPeerAddressFamilyPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 5),
    _UsdBgpPeerAddressFamilyPeerGroup_Type()
)
usdBgpPeerAddressFamilyPeerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyPeerGroup.setStatus("current")


class _UsdBgpPeerAddressFamilyDefaultOriginate_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilyDefaultOriginate based on TruthValue"""


_UsdBgpPeerAddressFamilyDefaultOriginate_Object = MibTableColumn
usdBgpPeerAddressFamilyDefaultOriginate = _UsdBgpPeerAddressFamilyDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 6),
    _UsdBgpPeerAddressFamilyDefaultOriginate_Type()
)
usdBgpPeerAddressFamilyDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyDefaultOriginate.setStatus("current")


class _UsdBgpPeerAddressFamilyNextHopSelf_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilyNextHopSelf based on TruthValue"""


_UsdBgpPeerAddressFamilyNextHopSelf_Object = MibTableColumn
usdBgpPeerAddressFamilyNextHopSelf = _UsdBgpPeerAddressFamilyNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 7),
    _UsdBgpPeerAddressFamilyNextHopSelf_Type()
)
usdBgpPeerAddressFamilyNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyNextHopSelf.setStatus("current")


class _UsdBgpPeerAddressFamilySendCommunity_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilySendCommunity based on TruthValue"""


_UsdBgpPeerAddressFamilySendCommunity_Object = MibTableColumn
usdBgpPeerAddressFamilySendCommunity = _UsdBgpPeerAddressFamilySendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 8),
    _UsdBgpPeerAddressFamilySendCommunity_Type()
)
usdBgpPeerAddressFamilySendCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilySendCommunity.setStatus("current")
_UsdBgpPeerAddressFamilyDistributeListIn_Type = DisplayString
_UsdBgpPeerAddressFamilyDistributeListIn_Object = MibTableColumn
usdBgpPeerAddressFamilyDistributeListIn = _UsdBgpPeerAddressFamilyDistributeListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 9),
    _UsdBgpPeerAddressFamilyDistributeListIn_Type()
)
usdBgpPeerAddressFamilyDistributeListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyDistributeListIn.setStatus("current")
_UsdBgpPeerAddressFamilyDistributeListOut_Type = DisplayString
_UsdBgpPeerAddressFamilyDistributeListOut_Object = MibTableColumn
usdBgpPeerAddressFamilyDistributeListOut = _UsdBgpPeerAddressFamilyDistributeListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 10),
    _UsdBgpPeerAddressFamilyDistributeListOut_Type()
)
usdBgpPeerAddressFamilyDistributeListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyDistributeListOut.setStatus("current")
_UsdBgpPeerAddressFamilyPrefixListIn_Type = DisplayString
_UsdBgpPeerAddressFamilyPrefixListIn_Object = MibTableColumn
usdBgpPeerAddressFamilyPrefixListIn = _UsdBgpPeerAddressFamilyPrefixListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 11),
    _UsdBgpPeerAddressFamilyPrefixListIn_Type()
)
usdBgpPeerAddressFamilyPrefixListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyPrefixListIn.setStatus("current")
_UsdBgpPeerAddressFamilyPrefixListOut_Type = DisplayString
_UsdBgpPeerAddressFamilyPrefixListOut_Object = MibTableColumn
usdBgpPeerAddressFamilyPrefixListOut = _UsdBgpPeerAddressFamilyPrefixListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 12),
    _UsdBgpPeerAddressFamilyPrefixListOut_Type()
)
usdBgpPeerAddressFamilyPrefixListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyPrefixListOut.setStatus("current")
_UsdBgpPeerAddressFamilyPrefixTreeIn_Type = DisplayString
_UsdBgpPeerAddressFamilyPrefixTreeIn_Object = MibTableColumn
usdBgpPeerAddressFamilyPrefixTreeIn = _UsdBgpPeerAddressFamilyPrefixTreeIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 13),
    _UsdBgpPeerAddressFamilyPrefixTreeIn_Type()
)
usdBgpPeerAddressFamilyPrefixTreeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyPrefixTreeIn.setStatus("current")
_UsdBgpPeerAddressFamilyPrefixTreeOut_Type = DisplayString
_UsdBgpPeerAddressFamilyPrefixTreeOut_Object = MibTableColumn
usdBgpPeerAddressFamilyPrefixTreeOut = _UsdBgpPeerAddressFamilyPrefixTreeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 14),
    _UsdBgpPeerAddressFamilyPrefixTreeOut_Type()
)
usdBgpPeerAddressFamilyPrefixTreeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyPrefixTreeOut.setStatus("current")
_UsdBgpPeerAddressFamilyFilterListIn_Type = DisplayString
_UsdBgpPeerAddressFamilyFilterListIn_Object = MibTableColumn
usdBgpPeerAddressFamilyFilterListIn = _UsdBgpPeerAddressFamilyFilterListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 15),
    _UsdBgpPeerAddressFamilyFilterListIn_Type()
)
usdBgpPeerAddressFamilyFilterListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyFilterListIn.setStatus("current")
_UsdBgpPeerAddressFamilyFilterListOut_Type = DisplayString
_UsdBgpPeerAddressFamilyFilterListOut_Object = MibTableColumn
usdBgpPeerAddressFamilyFilterListOut = _UsdBgpPeerAddressFamilyFilterListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 16),
    _UsdBgpPeerAddressFamilyFilterListOut_Type()
)
usdBgpPeerAddressFamilyFilterListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyFilterListOut.setStatus("current")
_UsdBgpPeerAddressFamilyFilterListWeight_Type = DisplayString
_UsdBgpPeerAddressFamilyFilterListWeight_Object = MibTableColumn
usdBgpPeerAddressFamilyFilterListWeight = _UsdBgpPeerAddressFamilyFilterListWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 17),
    _UsdBgpPeerAddressFamilyFilterListWeight_Type()
)
usdBgpPeerAddressFamilyFilterListWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyFilterListWeight.setStatus("current")


class _UsdBgpPeerAddressFamilyFilterListWeightValue_Type(Unsigned32):
    """Custom type usdBgpPeerAddressFamilyFilterListWeightValue based on Unsigned32"""
    defaultValue = 0


_UsdBgpPeerAddressFamilyFilterListWeightValue_Object = MibTableColumn
usdBgpPeerAddressFamilyFilterListWeightValue = _UsdBgpPeerAddressFamilyFilterListWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 18),
    _UsdBgpPeerAddressFamilyFilterListWeightValue_Type()
)
usdBgpPeerAddressFamilyFilterListWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyFilterListWeightValue.setStatus("current")


class _UsdBgpPeerAddressFamilyRouteMapIn_Type(DisplayString):
    """Custom type usdBgpPeerAddressFamilyRouteMapIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerAddressFamilyRouteMapIn_Type.__name__ = "DisplayString"
_UsdBgpPeerAddressFamilyRouteMapIn_Object = MibTableColumn
usdBgpPeerAddressFamilyRouteMapIn = _UsdBgpPeerAddressFamilyRouteMapIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 19),
    _UsdBgpPeerAddressFamilyRouteMapIn_Type()
)
usdBgpPeerAddressFamilyRouteMapIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRouteMapIn.setStatus("current")


class _UsdBgpPeerAddressFamilyRouteMapOut_Type(DisplayString):
    """Custom type usdBgpPeerAddressFamilyRouteMapOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerAddressFamilyRouteMapOut_Type.__name__ = "DisplayString"
_UsdBgpPeerAddressFamilyRouteMapOut_Object = MibTableColumn
usdBgpPeerAddressFamilyRouteMapOut = _UsdBgpPeerAddressFamilyRouteMapOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 20),
    _UsdBgpPeerAddressFamilyRouteMapOut_Type()
)
usdBgpPeerAddressFamilyRouteMapOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRouteMapOut.setStatus("current")


class _UsdBgpPeerAddressFamilyRouteReflectorClient_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilyRouteReflectorClient based on TruthValue"""


_UsdBgpPeerAddressFamilyRouteReflectorClient_Object = MibTableColumn
usdBgpPeerAddressFamilyRouteReflectorClient = _UsdBgpPeerAddressFamilyRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 21),
    _UsdBgpPeerAddressFamilyRouteReflectorClient_Type()
)
usdBgpPeerAddressFamilyRouteReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRouteReflectorClient.setStatus("current")


class _UsdBgpPeerAddressFamilyRouteLimitWarn_Type(Unsigned32):
    """Custom type usdBgpPeerAddressFamilyRouteLimitWarn based on Unsigned32"""
    defaultValue = 1000000


_UsdBgpPeerAddressFamilyRouteLimitWarn_Object = MibTableColumn
usdBgpPeerAddressFamilyRouteLimitWarn = _UsdBgpPeerAddressFamilyRouteLimitWarn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 22),
    _UsdBgpPeerAddressFamilyRouteLimitWarn_Type()
)
usdBgpPeerAddressFamilyRouteLimitWarn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRouteLimitWarn.setStatus("current")


class _UsdBgpPeerAddressFamilyRouteLimitReset_Type(Unsigned32):
    """Custom type usdBgpPeerAddressFamilyRouteLimitReset based on Unsigned32"""
    defaultValue = 10000000


_UsdBgpPeerAddressFamilyRouteLimitReset_Object = MibTableColumn
usdBgpPeerAddressFamilyRouteLimitReset = _UsdBgpPeerAddressFamilyRouteLimitReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 23),
    _UsdBgpPeerAddressFamilyRouteLimitReset_Type()
)
usdBgpPeerAddressFamilyRouteLimitReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRouteLimitReset.setStatus("current")


class _UsdBgpPeerAddressFamilyRouteLimitWarnOnly_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilyRouteLimitWarnOnly based on TruthValue"""


_UsdBgpPeerAddressFamilyRouteLimitWarnOnly_Object = MibTableColumn
usdBgpPeerAddressFamilyRouteLimitWarnOnly = _UsdBgpPeerAddressFamilyRouteLimitWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 24),
    _UsdBgpPeerAddressFamilyRouteLimitWarnOnly_Type()
)
usdBgpPeerAddressFamilyRouteLimitWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRouteLimitWarnOnly.setStatus("current")


class _UsdBgpPeerAddressFamilyRemovePrivateAs_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilyRemovePrivateAs based on TruthValue"""


_UsdBgpPeerAddressFamilyRemovePrivateAs_Object = MibTableColumn
usdBgpPeerAddressFamilyRemovePrivateAs = _UsdBgpPeerAddressFamilyRemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 25),
    _UsdBgpPeerAddressFamilyRemovePrivateAs_Type()
)
usdBgpPeerAddressFamilyRemovePrivateAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRemovePrivateAs.setStatus("current")


class _UsdBgpPeerAddressFamilyUnsuppressMap_Type(DisplayString):
    """Custom type usdBgpPeerAddressFamilyUnsuppressMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerAddressFamilyUnsuppressMap_Type.__name__ = "DisplayString"
_UsdBgpPeerAddressFamilyUnsuppressMap_Object = MibTableColumn
usdBgpPeerAddressFamilyUnsuppressMap = _UsdBgpPeerAddressFamilyUnsuppressMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 26),
    _UsdBgpPeerAddressFamilyUnsuppressMap_Type()
)
usdBgpPeerAddressFamilyUnsuppressMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyUnsuppressMap.setStatus("current")


class _UsdBgpPeerAddressFamilyInboundSoftReconfig_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilyInboundSoftReconfig based on TruthValue"""


_UsdBgpPeerAddressFamilyInboundSoftReconfig_Object = MibTableColumn
usdBgpPeerAddressFamilyInboundSoftReconfig = _UsdBgpPeerAddressFamilyInboundSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 27),
    _UsdBgpPeerAddressFamilyInboundSoftReconfig_Type()
)
usdBgpPeerAddressFamilyInboundSoftReconfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyInboundSoftReconfig.setStatus("current")


class _UsdBgpPeerAddressFamilyResetConnectionType_Type(UsdBgpResetConnectionType):
    """Custom type usdBgpPeerAddressFamilyResetConnectionType based on UsdBgpResetConnectionType"""


_UsdBgpPeerAddressFamilyResetConnectionType_Object = MibTableColumn
usdBgpPeerAddressFamilyResetConnectionType = _UsdBgpPeerAddressFamilyResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 28),
    _UsdBgpPeerAddressFamilyResetConnectionType_Type()
)
usdBgpPeerAddressFamilyResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyResetConnectionType.setStatus("current")
_UsdBgpPeerAddressFamilyRowStatus_Type = RowStatus
_UsdBgpPeerAddressFamilyRowStatus_Object = MibTableColumn
usdBgpPeerAddressFamilyRowStatus = _UsdBgpPeerAddressFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 29),
    _UsdBgpPeerAddressFamilyRowStatus_Type()
)
usdBgpPeerAddressFamilyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyRowStatus.setStatus("current")


class _UsdBgpPeerAddressFamilyAsOverride_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilyAsOverride based on TruthValue"""


_UsdBgpPeerAddressFamilyAsOverride_Object = MibTableColumn
usdBgpPeerAddressFamilyAsOverride = _UsdBgpPeerAddressFamilyAsOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 30),
    _UsdBgpPeerAddressFamilyAsOverride_Type()
)
usdBgpPeerAddressFamilyAsOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyAsOverride.setStatus("current")


class _UsdBgpPeerAddressFamilyAllowAsIn_Type(Integer32):
    """Custom type usdBgpPeerAddressFamilyAllowAsIn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_UsdBgpPeerAddressFamilyAllowAsIn_Type.__name__ = "Integer32"
_UsdBgpPeerAddressFamilyAllowAsIn_Object = MibTableColumn
usdBgpPeerAddressFamilyAllowAsIn = _UsdBgpPeerAddressFamilyAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 31),
    _UsdBgpPeerAddressFamilyAllowAsIn_Type()
)
usdBgpPeerAddressFamilyAllowAsIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyAllowAsIn.setStatus("current")


class _UsdBgpPeerAddressFamilySendExtendedCommunity_Type(TruthValue):
    """Custom type usdBgpPeerAddressFamilySendExtendedCommunity based on TruthValue"""


_UsdBgpPeerAddressFamilySendExtendedCommunity_Object = MibTableColumn
usdBgpPeerAddressFamilySendExtendedCommunity = _UsdBgpPeerAddressFamilySendExtendedCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 32),
    _UsdBgpPeerAddressFamilySendExtendedCommunity_Type()
)
usdBgpPeerAddressFamilySendExtendedCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilySendExtendedCommunity.setStatus("current")


class _UsdBgpPeerAddressFamilyUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpPeerAddressFamilyUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpPeerAddressFamilyAllowAsIn", 24),
          ("usdBgpPeerAddressFamilyAsOverride", 23),
          ("usdBgpPeerAddressFamilyDefaultOriginate", 1),
          ("usdBgpPeerAddressFamilyDistributeListIn", 4),
          ("usdBgpPeerAddressFamilyDistributeListOut", 5),
          ("usdBgpPeerAddressFamilyFilterListIn", 10),
          ("usdBgpPeerAddressFamilyFilterListOut", 11),
          ("usdBgpPeerAddressFamilyFilterListWeight", 12),
          ("usdBgpPeerAddressFamilyFilterListWeightValue", 13),
          ("usdBgpPeerAddressFamilyInboundSoftReconfig", 22),
          ("usdBgpPeerAddressFamilyNextHopSelf", 2),
          ("usdBgpPeerAddressFamilyPeerGroup", 0),
          ("usdBgpPeerAddressFamilyPrefixListIn", 6),
          ("usdBgpPeerAddressFamilyPrefixListOut", 7),
          ("usdBgpPeerAddressFamilyPrefixTreeIn", 8),
          ("usdBgpPeerAddressFamilyPrefixTreeOut", 9),
          ("usdBgpPeerAddressFamilyRemovePrivateAs", 20),
          ("usdBgpPeerAddressFamilyRouteLimitReset", 18),
          ("usdBgpPeerAddressFamilyRouteLimitWarn", 17),
          ("usdBgpPeerAddressFamilyRouteLimitWarnOnly", 19),
          ("usdBgpPeerAddressFamilyRouteMapIn", 14),
          ("usdBgpPeerAddressFamilyRouteMapOut", 15),
          ("usdBgpPeerAddressFamilyRouteReflectorClient", 16),
          ("usdBgpPeerAddressFamilySendCommunity", 3),
          ("usdBgpPeerAddressFamilySendExtendedCommunity", 25),
          ("usdBgpPeerAddressFamilyUnsuppressMap", 21))
    )

_UsdBgpPeerAddressFamilyUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpPeerAddressFamilyUnconfiguredAttributes_Object = MibTableColumn
usdBgpPeerAddressFamilyUnconfiguredAttributes = _UsdBgpPeerAddressFamilyUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 44),
    _UsdBgpPeerAddressFamilyUnconfiguredAttributes_Type()
)
usdBgpPeerAddressFamilyUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyUnconfiguredAttributes.setStatus("current")
_UsdBgpPeerGroupTable_Object = MibTable
usdBgpPeerGroupTable = _UsdBgpPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9)
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupTable.setStatus("current")
_UsdBgpPeerGroupEntry_Object = MibTableRow
usdBgpPeerGroupEntry = _UsdBgpPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1)
)
usdBgpPeerGroupEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerGroupVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerGroupGroupName"),
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupEntry.setStatus("current")
_UsdBgpPeerGroupVrfName_Type = UsdVrfName
_UsdBgpPeerGroupVrfName_Object = MibTableColumn
usdBgpPeerGroupVrfName = _UsdBgpPeerGroupVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 1),
    _UsdBgpPeerGroupVrfName_Type()
)
usdBgpPeerGroupVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerGroupVrfName.setStatus("current")


class _UsdBgpPeerGroupGroupName_Type(DisplayString):
    """Custom type usdBgpPeerGroupGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupGroupName_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupGroupName_Object = MibTableColumn
usdBgpPeerGroupGroupName = _UsdBgpPeerGroupGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 2),
    _UsdBgpPeerGroupGroupName_Type()
)
usdBgpPeerGroupGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerGroupGroupName.setStatus("current")


class _UsdBgpPeerGroupAdminStatus_Type(Integer32):
    """Custom type usdBgpPeerGroupAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 2),
          ("stop", 1))
    )


_UsdBgpPeerGroupAdminStatus_Type.__name__ = "Integer32"
_UsdBgpPeerGroupAdminStatus_Object = MibTableColumn
usdBgpPeerGroupAdminStatus = _UsdBgpPeerGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 3),
    _UsdBgpPeerGroupAdminStatus_Type()
)
usdBgpPeerGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAdminStatus.setStatus("current")


class _UsdBgpPeerGroupRemoteAsNumber_Type(Integer32):
    """Custom type usdBgpPeerGroupRemoteAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpPeerGroupRemoteAsNumber_Type.__name__ = "Integer32"
_UsdBgpPeerGroupRemoteAsNumber_Object = MibTableColumn
usdBgpPeerGroupRemoteAsNumber = _UsdBgpPeerGroupRemoteAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 4),
    _UsdBgpPeerGroupRemoteAsNumber_Type()
)
usdBgpPeerGroupRemoteAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupRemoteAsNumber.setStatus("current")


class _UsdBgpPeerGroupRetryInterval_Type(Integer32):
    """Custom type usdBgpPeerGroupRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpPeerGroupRetryInterval_Type.__name__ = "Integer32"
_UsdBgpPeerGroupRetryInterval_Object = MibTableColumn
usdBgpPeerGroupRetryInterval = _UsdBgpPeerGroupRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 5),
    _UsdBgpPeerGroupRetryInterval_Type()
)
usdBgpPeerGroupRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerGroupRetryInterval.setUnits("seconds")


class _UsdBgpPeerGroupConfigHoldTime_Type(Integer32):
    """Custom type usdBgpPeerGroupConfigHoldTime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_UsdBgpPeerGroupConfigHoldTime_Type.__name__ = "Integer32"
_UsdBgpPeerGroupConfigHoldTime_Object = MibTableColumn
usdBgpPeerGroupConfigHoldTime = _UsdBgpPeerGroupConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 6),
    _UsdBgpPeerGroupConfigHoldTime_Type()
)
usdBgpPeerGroupConfigHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupConfigHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerGroupConfigHoldTime.setUnits("seconds")


class _UsdBgpPeerGroupConfigKeepAliveInterval_Type(Integer32):
    """Custom type usdBgpPeerGroupConfigKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_UsdBgpPeerGroupConfigKeepAliveInterval_Type.__name__ = "Integer32"
_UsdBgpPeerGroupConfigKeepAliveInterval_Object = MibTableColumn
usdBgpPeerGroupConfigKeepAliveInterval = _UsdBgpPeerGroupConfigKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 7),
    _UsdBgpPeerGroupConfigKeepAliveInterval_Type()
)
usdBgpPeerGroupConfigKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupConfigKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerGroupConfigKeepAliveInterval.setUnits("seconds")


class _UsdBgpPeerGroupAsOriginationInterval_Type(Integer32):
    """Custom type usdBgpPeerGroupAsOriginationInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpPeerGroupAsOriginationInterval_Type.__name__ = "Integer32"
_UsdBgpPeerGroupAsOriginationInterval_Object = MibTableColumn
usdBgpPeerGroupAsOriginationInterval = _UsdBgpPeerGroupAsOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 8),
    _UsdBgpPeerGroupAsOriginationInterval_Type()
)
usdBgpPeerGroupAsOriginationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAsOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAsOriginationInterval.setUnits("seconds")


class _UsdBgpPeerGroupAdvertisementInterval_Type(Integer32):
    """Custom type usdBgpPeerGroupAdvertisementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdBgpPeerGroupAdvertisementInterval_Type.__name__ = "Integer32"
_UsdBgpPeerGroupAdvertisementInterval_Object = MibTableColumn
usdBgpPeerGroupAdvertisementInterval = _UsdBgpPeerGroupAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 9),
    _UsdBgpPeerGroupAdvertisementInterval_Type()
)
usdBgpPeerGroupAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAdvertisementInterval.setUnits("seconds")


class _UsdBgpPeerGroupDescription_Type(DisplayString):
    """Custom type usdBgpPeerGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UsdBgpPeerGroupDescription_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupDescription_Object = MibTableColumn
usdBgpPeerGroupDescription = _UsdBgpPeerGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 10),
    _UsdBgpPeerGroupDescription_Type()
)
usdBgpPeerGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupDescription.setStatus("current")


class _UsdBgpPeerGroupWeight_Type(Unsigned32):
    """Custom type usdBgpPeerGroupWeight based on Unsigned32"""
    defaultValue = 0


_UsdBgpPeerGroupWeight_Object = MibTableColumn
usdBgpPeerGroupWeight = _UsdBgpPeerGroupWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 11),
    _UsdBgpPeerGroupWeight_Type()
)
usdBgpPeerGroupWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupWeight.setStatus("current")


class _UsdBgpPeerGroupEbgpMultihop_Type(TruthValue):
    """Custom type usdBgpPeerGroupEbgpMultihop based on TruthValue"""


_UsdBgpPeerGroupEbgpMultihop_Object = MibTableColumn
usdBgpPeerGroupEbgpMultihop = _UsdBgpPeerGroupEbgpMultihop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 12),
    _UsdBgpPeerGroupEbgpMultihop_Type()
)
usdBgpPeerGroupEbgpMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupEbgpMultihop.setStatus("current")


class _UsdBgpPeerGroupEbgpMultihopTtl_Type(Integer32):
    """Custom type usdBgpPeerGroupEbgpMultihopTtl based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdBgpPeerGroupEbgpMultihopTtl_Type.__name__ = "Integer32"
_UsdBgpPeerGroupEbgpMultihopTtl_Object = MibTableColumn
usdBgpPeerGroupEbgpMultihopTtl = _UsdBgpPeerGroupEbgpMultihopTtl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 13),
    _UsdBgpPeerGroupEbgpMultihopTtl_Type()
)
usdBgpPeerGroupEbgpMultihopTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupEbgpMultihopTtl.setStatus("current")


class _UsdBgpPeerGroupUpdateSource_Type(IpAddress):
    """Custom type usdBgpPeerGroupUpdateSource based on IpAddress"""
    defaultValue = 0


_UsdBgpPeerGroupUpdateSource_Object = MibTableColumn
usdBgpPeerGroupUpdateSource = _UsdBgpPeerGroupUpdateSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 14),
    _UsdBgpPeerGroupUpdateSource_Type()
)
usdBgpPeerGroupUpdateSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupUpdateSource.setStatus("current")


class _UsdBgpPeerGroupMd5Password_Type(OctetString):
    """Custom type usdBgpPeerGroupMd5Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupMd5Password_Type.__name__ = "OctetString"
_UsdBgpPeerGroupMd5Password_Object = MibTableColumn
usdBgpPeerGroupMd5Password = _UsdBgpPeerGroupMd5Password_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 15),
    _UsdBgpPeerGroupMd5Password_Type()
)
usdBgpPeerGroupMd5Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupMd5Password.setStatus("current")


class _UsdBgpPeerGroupMaxUpdateSize_Type(Unsigned32):
    """Custom type usdBgpPeerGroupMaxUpdateSize based on Unsigned32"""
    defaultValue = 4096


_UsdBgpPeerGroupMaxUpdateSize_Object = MibTableColumn
usdBgpPeerGroupMaxUpdateSize = _UsdBgpPeerGroupMaxUpdateSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 16),
    _UsdBgpPeerGroupMaxUpdateSize_Type()
)
usdBgpPeerGroupMaxUpdateSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupMaxUpdateSize.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpPeerGroupMaxUpdateSize.setUnits("bytes")


class _UsdBgpPeerGroupResetConnectionType_Type(UsdBgpResetConnectionType):
    """Custom type usdBgpPeerGroupResetConnectionType based on UsdBgpResetConnectionType"""


_UsdBgpPeerGroupResetConnectionType_Object = MibTableColumn
usdBgpPeerGroupResetConnectionType = _UsdBgpPeerGroupResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 17),
    _UsdBgpPeerGroupResetConnectionType_Type()
)
usdBgpPeerGroupResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupResetConnectionType.setStatus("current")
_UsdBgpPeerGroupRowStatus_Type = RowStatus
_UsdBgpPeerGroupRowStatus_Object = MibTableColumn
usdBgpPeerGroupRowStatus = _UsdBgpPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 18),
    _UsdBgpPeerGroupRowStatus_Type()
)
usdBgpPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupRowStatus.setStatus("current")


class _UsdBgpPeerGroupLocalAsNumber_Type(Integer32):
    """Custom type usdBgpPeerGroupLocalAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpPeerGroupLocalAsNumber_Type.__name__ = "Integer32"
_UsdBgpPeerGroupLocalAsNumber_Object = MibTableColumn
usdBgpPeerGroupLocalAsNumber = _UsdBgpPeerGroupLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 19),
    _UsdBgpPeerGroupLocalAsNumber_Type()
)
usdBgpPeerGroupLocalAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupLocalAsNumber.setStatus("current")


class _UsdBgpPeerGroupUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpPeerGroupUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpPeerGroupAdminStatus", 0),
          ("usdBgpPeerGroupAdvertisementInterval", 6),
          ("usdBgpPeerGroupAsOriginationInterval", 5),
          ("usdBgpPeerGroupConfigHoldTime", 3),
          ("usdBgpPeerGroupConfigKeepAliveInterval", 4),
          ("usdBgpPeerGroupDescription", 7),
          ("usdBgpPeerGroupEbgpMultihop", 9),
          ("usdBgpPeerGroupEbgpMultihopTtl", 10),
          ("usdBgpPeerGroupLocalAsNumber", 14),
          ("usdBgpPeerGroupMaxUpdateSize", 13),
          ("usdBgpPeerGroupMd5Password", 12),
          ("usdBgpPeerGroupRemoteAsNumber", 1),
          ("usdBgpPeerGroupRetryInterval", 2),
          ("usdBgpPeerGroupUpdateSource", 11),
          ("usdBgpPeerGroupWeight", 8))
    )

_UsdBgpPeerGroupUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpPeerGroupUnconfiguredAttributes_Object = MibTableColumn
usdBgpPeerGroupUnconfiguredAttributes = _UsdBgpPeerGroupUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 27),
    _UsdBgpPeerGroupUnconfiguredAttributes_Type()
)
usdBgpPeerGroupUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupUnconfiguredAttributes.setStatus("current")
_UsdBgpPeerGroupAddressFamilyTable_Object = MibTable
usdBgpPeerGroupAddressFamilyTable = _UsdBgpPeerGroupAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10)
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyTable.setStatus("current")
_UsdBgpPeerGroupAddressFamilyEntry_Object = MibTableRow
usdBgpPeerGroupAddressFamilyEntry = _UsdBgpPeerGroupAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1)
)
usdBgpPeerGroupAddressFamilyEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilySafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpPeerGroupGroupAddressFamilyGroupName"),
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyEntry.setStatus("current")
_UsdBgpPeerGroupAddressFamilyVrfName_Type = UsdVrfName
_UsdBgpPeerGroupAddressFamilyVrfName_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyVrfName = _UsdBgpPeerGroupAddressFamilyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 1),
    _UsdBgpPeerGroupAddressFamilyVrfName_Type()
)
usdBgpPeerGroupAddressFamilyVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyVrfName.setStatus("current")
_UsdBgpPeerGroupAddressFamilyAfi_Type = UsdBgpAfi
_UsdBgpPeerGroupAddressFamilyAfi_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyAfi = _UsdBgpPeerGroupAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 2),
    _UsdBgpPeerGroupAddressFamilyAfi_Type()
)
usdBgpPeerGroupAddressFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyAfi.setStatus("current")
_UsdBgpPeerGroupAddressFamilySafi_Type = UsdBgpSafi
_UsdBgpPeerGroupAddressFamilySafi_Object = MibTableColumn
usdBgpPeerGroupAddressFamilySafi = _UsdBgpPeerGroupAddressFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 3),
    _UsdBgpPeerGroupAddressFamilySafi_Type()
)
usdBgpPeerGroupAddressFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilySafi.setStatus("current")


class _UsdBgpPeerGroupGroupAddressFamilyGroupName_Type(DisplayString):
    """Custom type usdBgpPeerGroupGroupAddressFamilyGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupGroupAddressFamilyGroupName_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupGroupAddressFamilyGroupName_Object = MibTableColumn
usdBgpPeerGroupGroupAddressFamilyGroupName = _UsdBgpPeerGroupGroupAddressFamilyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 4),
    _UsdBgpPeerGroupGroupAddressFamilyGroupName_Type()
)
usdBgpPeerGroupGroupAddressFamilyGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpPeerGroupGroupAddressFamilyGroupName.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyDefaultOriginate_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilyDefaultOriginate based on TruthValue"""


_UsdBgpPeerGroupAddressFamilyDefaultOriginate_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyDefaultOriginate = _UsdBgpPeerGroupAddressFamilyDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 5),
    _UsdBgpPeerGroupAddressFamilyDefaultOriginate_Type()
)
usdBgpPeerGroupAddressFamilyDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyDefaultOriginate.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyNextHopSelf_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilyNextHopSelf based on TruthValue"""


_UsdBgpPeerGroupAddressFamilyNextHopSelf_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyNextHopSelf = _UsdBgpPeerGroupAddressFamilyNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 6),
    _UsdBgpPeerGroupAddressFamilyNextHopSelf_Type()
)
usdBgpPeerGroupAddressFamilyNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyNextHopSelf.setStatus("current")


class _UsdBgpPeerGroupAddressFamilySendCommunity_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilySendCommunity based on TruthValue"""


_UsdBgpPeerGroupAddressFamilySendCommunity_Object = MibTableColumn
usdBgpPeerGroupAddressFamilySendCommunity = _UsdBgpPeerGroupAddressFamilySendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 7),
    _UsdBgpPeerGroupAddressFamilySendCommunity_Type()
)
usdBgpPeerGroupAddressFamilySendCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilySendCommunity.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyDistributeListIn_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyDistributeListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyDistributeListIn_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyDistributeListIn_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyDistributeListIn = _UsdBgpPeerGroupAddressFamilyDistributeListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 8),
    _UsdBgpPeerGroupAddressFamilyDistributeListIn_Type()
)
usdBgpPeerGroupAddressFamilyDistributeListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyDistributeListIn.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyDistributeListOut_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyDistributeListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyDistributeListOut_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyDistributeListOut_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyDistributeListOut = _UsdBgpPeerGroupAddressFamilyDistributeListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 9),
    _UsdBgpPeerGroupAddressFamilyDistributeListOut_Type()
)
usdBgpPeerGroupAddressFamilyDistributeListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyDistributeListOut.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyPrefixListIn_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyPrefixListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyPrefixListIn_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyPrefixListIn_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyPrefixListIn = _UsdBgpPeerGroupAddressFamilyPrefixListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 10),
    _UsdBgpPeerGroupAddressFamilyPrefixListIn_Type()
)
usdBgpPeerGroupAddressFamilyPrefixListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyPrefixListIn.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyPrefixListOut_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyPrefixListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyPrefixListOut_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyPrefixListOut_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyPrefixListOut = _UsdBgpPeerGroupAddressFamilyPrefixListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 11),
    _UsdBgpPeerGroupAddressFamilyPrefixListOut_Type()
)
usdBgpPeerGroupAddressFamilyPrefixListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyPrefixListOut.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyPrefixTreeIn_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyPrefixTreeIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyPrefixTreeIn_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyPrefixTreeIn_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyPrefixTreeIn = _UsdBgpPeerGroupAddressFamilyPrefixTreeIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 12),
    _UsdBgpPeerGroupAddressFamilyPrefixTreeIn_Type()
)
usdBgpPeerGroupAddressFamilyPrefixTreeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyPrefixTreeIn.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyPrefixTreeOut_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyPrefixTreeOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyPrefixTreeOut_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyPrefixTreeOut_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyPrefixTreeOut = _UsdBgpPeerGroupAddressFamilyPrefixTreeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 13),
    _UsdBgpPeerGroupAddressFamilyPrefixTreeOut_Type()
)
usdBgpPeerGroupAddressFamilyPrefixTreeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyPrefixTreeOut.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyFilterListIn_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyFilterListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyFilterListIn_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyFilterListIn_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyFilterListIn = _UsdBgpPeerGroupAddressFamilyFilterListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 14),
    _UsdBgpPeerGroupAddressFamilyFilterListIn_Type()
)
usdBgpPeerGroupAddressFamilyFilterListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyFilterListIn.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyFilterListOut_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyFilterListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyFilterListOut_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyFilterListOut_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyFilterListOut = _UsdBgpPeerGroupAddressFamilyFilterListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 15),
    _UsdBgpPeerGroupAddressFamilyFilterListOut_Type()
)
usdBgpPeerGroupAddressFamilyFilterListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyFilterListOut.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyFilterListWeight_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyFilterListWeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyFilterListWeight_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyFilterListWeight_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyFilterListWeight = _UsdBgpPeerGroupAddressFamilyFilterListWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 16),
    _UsdBgpPeerGroupAddressFamilyFilterListWeight_Type()
)
usdBgpPeerGroupAddressFamilyFilterListWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyFilterListWeight.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyFilterListWeightValue_Type(Unsigned32):
    """Custom type usdBgpPeerGroupAddressFamilyFilterListWeightValue based on Unsigned32"""
    defaultValue = 0


_UsdBgpPeerGroupAddressFamilyFilterListWeightValue_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyFilterListWeightValue = _UsdBgpPeerGroupAddressFamilyFilterListWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 17),
    _UsdBgpPeerGroupAddressFamilyFilterListWeightValue_Type()
)
usdBgpPeerGroupAddressFamilyFilterListWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyFilterListWeightValue.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyRouteMapIn_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyRouteMapIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyRouteMapIn_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyRouteMapIn_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRouteMapIn = _UsdBgpPeerGroupAddressFamilyRouteMapIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 18),
    _UsdBgpPeerGroupAddressFamilyRouteMapIn_Type()
)
usdBgpPeerGroupAddressFamilyRouteMapIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRouteMapIn.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyRouteMapOut_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyRouteMapOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyRouteMapOut_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyRouteMapOut_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRouteMapOut = _UsdBgpPeerGroupAddressFamilyRouteMapOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 19),
    _UsdBgpPeerGroupAddressFamilyRouteMapOut_Type()
)
usdBgpPeerGroupAddressFamilyRouteMapOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRouteMapOut.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyRouteReflectorClient_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilyRouteReflectorClient based on TruthValue"""


_UsdBgpPeerGroupAddressFamilyRouteReflectorClient_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRouteReflectorClient = _UsdBgpPeerGroupAddressFamilyRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 20),
    _UsdBgpPeerGroupAddressFamilyRouteReflectorClient_Type()
)
usdBgpPeerGroupAddressFamilyRouteReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRouteReflectorClient.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyRouteLimitWarn_Type(Unsigned32):
    """Custom type usdBgpPeerGroupAddressFamilyRouteLimitWarn based on Unsigned32"""
    defaultValue = 0


_UsdBgpPeerGroupAddressFamilyRouteLimitWarn_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRouteLimitWarn = _UsdBgpPeerGroupAddressFamilyRouteLimitWarn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 21),
    _UsdBgpPeerGroupAddressFamilyRouteLimitWarn_Type()
)
usdBgpPeerGroupAddressFamilyRouteLimitWarn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRouteLimitWarn.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyRouteLimitReset_Type(Unsigned32):
    """Custom type usdBgpPeerGroupAddressFamilyRouteLimitReset based on Unsigned32"""
    defaultValue = 0


_UsdBgpPeerGroupAddressFamilyRouteLimitReset_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRouteLimitReset = _UsdBgpPeerGroupAddressFamilyRouteLimitReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 22),
    _UsdBgpPeerGroupAddressFamilyRouteLimitReset_Type()
)
usdBgpPeerGroupAddressFamilyRouteLimitReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRouteLimitReset.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly based on TruthValue"""


_UsdBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly = _UsdBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 23),
    _UsdBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Type()
)
usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyRemovePrivateAs_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilyRemovePrivateAs based on TruthValue"""


_UsdBgpPeerGroupAddressFamilyRemovePrivateAs_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRemovePrivateAs = _UsdBgpPeerGroupAddressFamilyRemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 24),
    _UsdBgpPeerGroupAddressFamilyRemovePrivateAs_Type()
)
usdBgpPeerGroupAddressFamilyRemovePrivateAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRemovePrivateAs.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyUnsuppressMap_Type(DisplayString):
    """Custom type usdBgpPeerGroupAddressFamilyUnsuppressMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpPeerGroupAddressFamilyUnsuppressMap_Type.__name__ = "DisplayString"
_UsdBgpPeerGroupAddressFamilyUnsuppressMap_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyUnsuppressMap = _UsdBgpPeerGroupAddressFamilyUnsuppressMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 25),
    _UsdBgpPeerGroupAddressFamilyUnsuppressMap_Type()
)
usdBgpPeerGroupAddressFamilyUnsuppressMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyUnsuppressMap.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyInboundSoftReconfig_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilyInboundSoftReconfig based on TruthValue"""


_UsdBgpPeerGroupAddressFamilyInboundSoftReconfig_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyInboundSoftReconfig = _UsdBgpPeerGroupAddressFamilyInboundSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 26),
    _UsdBgpPeerGroupAddressFamilyInboundSoftReconfig_Type()
)
usdBgpPeerGroupAddressFamilyInboundSoftReconfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyInboundSoftReconfig.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyResetConnectionType_Type(UsdBgpResetConnectionType):
    """Custom type usdBgpPeerGroupAddressFamilyResetConnectionType based on UsdBgpResetConnectionType"""


_UsdBgpPeerGroupAddressFamilyResetConnectionType_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyResetConnectionType = _UsdBgpPeerGroupAddressFamilyResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 27),
    _UsdBgpPeerGroupAddressFamilyResetConnectionType_Type()
)
usdBgpPeerGroupAddressFamilyResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyResetConnectionType.setStatus("current")
_UsdBgpPeerGroupAddressFamilyRowStatus_Type = RowStatus
_UsdBgpPeerGroupAddressFamilyRowStatus_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyRowStatus = _UsdBgpPeerGroupAddressFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 28),
    _UsdBgpPeerGroupAddressFamilyRowStatus_Type()
)
usdBgpPeerGroupAddressFamilyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyRowStatus.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyAsOverride_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilyAsOverride based on TruthValue"""


_UsdBgpPeerGroupAddressFamilyAsOverride_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyAsOverride = _UsdBgpPeerGroupAddressFamilyAsOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 29),
    _UsdBgpPeerGroupAddressFamilyAsOverride_Type()
)
usdBgpPeerGroupAddressFamilyAsOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyAsOverride.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyAllowAsIn_Type(Integer32):
    """Custom type usdBgpPeerGroupAddressFamilyAllowAsIn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_UsdBgpPeerGroupAddressFamilyAllowAsIn_Type.__name__ = "Integer32"
_UsdBgpPeerGroupAddressFamilyAllowAsIn_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyAllowAsIn = _UsdBgpPeerGroupAddressFamilyAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 30),
    _UsdBgpPeerGroupAddressFamilyAllowAsIn_Type()
)
usdBgpPeerGroupAddressFamilyAllowAsIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyAllowAsIn.setStatus("current")


class _UsdBgpPeerGroupAddressFamilySendExtendedCommunity_Type(TruthValue):
    """Custom type usdBgpPeerGroupAddressFamilySendExtendedCommunity based on TruthValue"""


_UsdBgpPeerGroupAddressFamilySendExtendedCommunity_Object = MibTableColumn
usdBgpPeerGroupAddressFamilySendExtendedCommunity = _UsdBgpPeerGroupAddressFamilySendExtendedCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 31),
    _UsdBgpPeerGroupAddressFamilySendExtendedCommunity_Type()
)
usdBgpPeerGroupAddressFamilySendExtendedCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilySendExtendedCommunity.setStatus("current")


class _UsdBgpPeerGroupAddressFamilyUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpPeerGroupAddressFamilyUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpPeerGroupAddressFamilyAllowAsIn", 23),
          ("usdBgpPeerGroupAddressFamilyAsOverride", 22),
          ("usdBgpPeerGroupAddressFamilyDefaultOriginate", 0),
          ("usdBgpPeerGroupAddressFamilyDistributeListIn", 3),
          ("usdBgpPeerGroupAddressFamilyDistributeListOut", 4),
          ("usdBgpPeerGroupAddressFamilyFilterListIn", 9),
          ("usdBgpPeerGroupAddressFamilyFilterListOut", 10),
          ("usdBgpPeerGroupAddressFamilyFilterListWeight", 11),
          ("usdBgpPeerGroupAddressFamilyFilterListWeightValue", 12),
          ("usdBgpPeerGroupAddressFamilyInboundSoftReconfig", 21),
          ("usdBgpPeerGroupAddressFamilyNextHopSelf", 1),
          ("usdBgpPeerGroupAddressFamilyPrefixListIn", 5),
          ("usdBgpPeerGroupAddressFamilyPrefixListOut", 6),
          ("usdBgpPeerGroupAddressFamilyPrefixTreeIn", 7),
          ("usdBgpPeerGroupAddressFamilyPrefixTreeOut", 8),
          ("usdBgpPeerGroupAddressFamilyRemovePrivateAs", 19),
          ("usdBgpPeerGroupAddressFamilyRouteLimitReset", 17),
          ("usdBgpPeerGroupAddressFamilyRouteLimitWarn", 16),
          ("usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly", 18),
          ("usdBgpPeerGroupAddressFamilyRouteMapIn", 13),
          ("usdBgpPeerGroupAddressFamilyRouteMapOut", 14),
          ("usdBgpPeerGroupAddressFamilyRouteReflectorClient", 15),
          ("usdBgpPeerGroupAddressFamilySendCommunity", 2),
          ("usdBgpPeerGroupAddressFamilySendExtendedCommunity", 24),
          ("usdBgpPeerGroupAddressFamilyUnsuppressMap", 20))
    )

_UsdBgpPeerGroupAddressFamilyUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpPeerGroupAddressFamilyUnconfiguredAttributes_Object = MibTableColumn
usdBgpPeerGroupAddressFamilyUnconfiguredAttributes = _UsdBgpPeerGroupAddressFamilyUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 35),
    _UsdBgpPeerGroupAddressFamilyUnconfiguredAttributes_Type()
)
usdBgpPeerGroupAddressFamilyUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyUnconfiguredAttributes.setStatus("current")
_UsdBgpRouteFlapHistoryTable_Object = MibTable
usdBgpRouteFlapHistoryTable = _UsdBgpRouteFlapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12)
)
if mibBuilder.loadTexts:
    usdBgpRouteFlapHistoryTable.setStatus("obsolete")
_UsdBgpRouteFlapHistoryEntry_Object = MibTableRow
usdBgpRouteFlapHistoryEntry = _UsdBgpRouteFlapHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1)
)
usdBgpRouteFlapHistoryEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteRouteType"),
)
if mibBuilder.loadTexts:
    usdBgpRouteFlapHistoryEntry.setStatus("obsolete")


class _UsdBgpRouteFlapState_Type(Integer32):
    """Custom type usdBgpRouteFlapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateAvailable", 1),
          ("stateSuppressedReachable", 2),
          ("stateSuppressedUnreachable", 3))
    )


_UsdBgpRouteFlapState_Type.__name__ = "Integer32"
_UsdBgpRouteFlapState_Object = MibTableColumn
usdBgpRouteFlapState = _UsdBgpRouteFlapState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 1),
    _UsdBgpRouteFlapState_Type()
)
usdBgpRouteFlapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapState.setStatus("obsolete")
_UsdBgpRouteFlapFigureOfMerit_Type = Unsigned32
_UsdBgpRouteFlapFigureOfMerit_Object = MibTableColumn
usdBgpRouteFlapFigureOfMerit = _UsdBgpRouteFlapFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 2),
    _UsdBgpRouteFlapFigureOfMerit_Type()
)
usdBgpRouteFlapFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapFigureOfMerit.setStatus("obsolete")
_UsdBgpRouteFlapRemainingTime_Type = Unsigned32
_UsdBgpRouteFlapRemainingTime_Object = MibTableColumn
usdBgpRouteFlapRemainingTime = _UsdBgpRouteFlapRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 3),
    _UsdBgpRouteFlapRemainingTime_Type()
)
usdBgpRouteFlapRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapRemainingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    usdBgpRouteFlapRemainingTime.setUnits("seconds")
_UsdBgpRouteFlapSuppressThreshold_Type = Unsigned32
_UsdBgpRouteFlapSuppressThreshold_Object = MibTableColumn
usdBgpRouteFlapSuppressThreshold = _UsdBgpRouteFlapSuppressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 4),
    _UsdBgpRouteFlapSuppressThreshold_Type()
)
usdBgpRouteFlapSuppressThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapSuppressThreshold.setStatus("obsolete")
_UsdBgpRouteFlapReuseThreshold_Type = Unsigned32
_UsdBgpRouteFlapReuseThreshold_Object = MibTableColumn
usdBgpRouteFlapReuseThreshold = _UsdBgpRouteFlapReuseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 5),
    _UsdBgpRouteFlapReuseThreshold_Type()
)
usdBgpRouteFlapReuseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapReuseThreshold.setStatus("obsolete")
_UsdBgpRouteFlapMaxHoldDownTime_Type = Unsigned32
_UsdBgpRouteFlapMaxHoldDownTime_Object = MibTableColumn
usdBgpRouteFlapMaxHoldDownTime = _UsdBgpRouteFlapMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 6),
    _UsdBgpRouteFlapMaxHoldDownTime_Type()
)
usdBgpRouteFlapMaxHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapMaxHoldDownTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    usdBgpRouteFlapMaxHoldDownTime.setUnits("seconds")
_UsdBgpRouteFlapHalfLifeReachable_Type = Unsigned32
_UsdBgpRouteFlapHalfLifeReachable_Object = MibTableColumn
usdBgpRouteFlapHalfLifeReachable = _UsdBgpRouteFlapHalfLifeReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 7),
    _UsdBgpRouteFlapHalfLifeReachable_Type()
)
usdBgpRouteFlapHalfLifeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapHalfLifeReachable.setStatus("obsolete")
if mibBuilder.loadTexts:
    usdBgpRouteFlapHalfLifeReachable.setUnits("seconds")
_UsdBgpRouteFlapHalfLifeUnreachable_Type = Unsigned32
_UsdBgpRouteFlapHalfLifeUnreachable_Object = MibTableColumn
usdBgpRouteFlapHalfLifeUnreachable = _UsdBgpRouteFlapHalfLifeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 8),
    _UsdBgpRouteFlapHalfLifeUnreachable_Type()
)
usdBgpRouteFlapHalfLifeUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteFlapHalfLifeUnreachable.setStatus("obsolete")
if mibBuilder.loadTexts:
    usdBgpRouteFlapHalfLifeUnreachable.setUnits("seconds")
_UsdBgpRouteTable_Object = MibTable
usdBgpRouteTable = _UsdBgpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13)
)
if mibBuilder.loadTexts:
    usdBgpRouteTable.setStatus("obsolete")
_UsdBgpRouteEntry_Object = MibTableRow
usdBgpRouteEntry = _UsdBgpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1)
)
usdBgpRouteEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteRouteType"),
)
if mibBuilder.loadTexts:
    usdBgpRouteEntry.setStatus("obsolete")
_UsdBgpRouteOriginatorId_Type = IpAddress
_UsdBgpRouteOriginatorId_Object = MibTableColumn
usdBgpRouteOriginatorId = _UsdBgpRouteOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 1),
    _UsdBgpRouteOriginatorId_Type()
)
usdBgpRouteOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteOriginatorId.setStatus("obsolete")
_UsdBgpRouteAtomicAggregatePresent_Type = TruthValue
_UsdBgpRouteAtomicAggregatePresent_Object = MibTableColumn
usdBgpRouteAtomicAggregatePresent = _UsdBgpRouteAtomicAggregatePresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 2),
    _UsdBgpRouteAtomicAggregatePresent_Type()
)
usdBgpRouteAtomicAggregatePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteAtomicAggregatePresent.setStatus("obsolete")
_UsdBgpRouteMedPresent_Type = TruthValue
_UsdBgpRouteMedPresent_Object = MibTableColumn
usdBgpRouteMedPresent = _UsdBgpRouteMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 3),
    _UsdBgpRouteMedPresent_Type()
)
usdBgpRouteMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteMedPresent.setStatus("obsolete")
_UsdBgpRouteLocalPrefPresent_Type = TruthValue
_UsdBgpRouteLocalPrefPresent_Object = MibTableColumn
usdBgpRouteLocalPrefPresent = _UsdBgpRouteLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 4),
    _UsdBgpRouteLocalPrefPresent_Type()
)
usdBgpRouteLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteLocalPrefPresent.setStatus("obsolete")
_UsdBgpRouteAggregatorPresent_Type = TruthValue
_UsdBgpRouteAggregatorPresent_Object = MibTableColumn
usdBgpRouteAggregatorPresent = _UsdBgpRouteAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 5),
    _UsdBgpRouteAggregatorPresent_Type()
)
usdBgpRouteAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteAggregatorPresent.setStatus("obsolete")
_UsdBgpRouteCommunitiesPresent_Type = TruthValue
_UsdBgpRouteCommunitiesPresent_Object = MibTableColumn
usdBgpRouteCommunitiesPresent = _UsdBgpRouteCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 6),
    _UsdBgpRouteCommunitiesPresent_Type()
)
usdBgpRouteCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteCommunitiesPresent.setStatus("obsolete")
_UsdBgpRouteOriginatorIdPresent_Type = TruthValue
_UsdBgpRouteOriginatorIdPresent_Object = MibTableColumn
usdBgpRouteOriginatorIdPresent = _UsdBgpRouteOriginatorIdPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 7),
    _UsdBgpRouteOriginatorIdPresent_Type()
)
usdBgpRouteOriginatorIdPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteOriginatorIdPresent.setStatus("obsolete")
_UsdBgpRouteClusterListPresent_Type = TruthValue
_UsdBgpRouteClusterListPresent_Object = MibTableColumn
usdBgpRouteClusterListPresent = _UsdBgpRouteClusterListPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 8),
    _UsdBgpRouteClusterListPresent_Type()
)
usdBgpRouteClusterListPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteClusterListPresent.setStatus("obsolete")
_UsdBgpRouteWeight_Type = Unsigned32
_UsdBgpRouteWeight_Object = MibTableColumn
usdBgpRouteWeight = _UsdBgpRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 9),
    _UsdBgpRouteWeight_Type()
)
usdBgpRouteWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteWeight.setStatus("obsolete")
_UsdBgpRouteVrfName_Type = UsdVrfName
_UsdBgpRouteVrfName_Object = MibTableColumn
usdBgpRouteVrfName = _UsdBgpRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 10),
    _UsdBgpRouteVrfName_Type()
)
usdBgpRouteVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpRouteVrfName.setStatus("obsolete")
_UsdBgpRouteAfi_Type = UsdBgpAfi
_UsdBgpRouteAfi_Object = MibTableColumn
usdBgpRouteAfi = _UsdBgpRouteAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 11),
    _UsdBgpRouteAfi_Type()
)
usdBgpRouteAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpRouteAfi.setStatus("obsolete")
_UsdBgpRouteSafi_Type = UsdBgpSafi
_UsdBgpRouteSafi_Object = MibTableColumn
usdBgpRouteSafi = _UsdBgpRouteSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 12),
    _UsdBgpRouteSafi_Type()
)
usdBgpRouteSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpRouteSafi.setStatus("obsolete")
_UsdBgpRoutePeer_Type = IpAddress
_UsdBgpRoutePeer_Object = MibTableColumn
usdBgpRoutePeer = _UsdBgpRoutePeer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 13),
    _UsdBgpRoutePeer_Type()
)
usdBgpRoutePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpRoutePeer.setStatus("obsolete")


class _UsdBgpRouteIpAddrPrefixLen_Type(Integer32):
    """Custom type usdBgpRouteIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdBgpRouteIpAddrPrefixLen_Type.__name__ = "Integer32"
_UsdBgpRouteIpAddrPrefixLen_Object = MibTableColumn
usdBgpRouteIpAddrPrefixLen = _UsdBgpRouteIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 14),
    _UsdBgpRouteIpAddrPrefixLen_Type()
)
usdBgpRouteIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpRouteIpAddrPrefixLen.setStatus("obsolete")
_UsdBgpRouteIpAddrPrefix_Type = IpAddress
_UsdBgpRouteIpAddrPrefix_Object = MibTableColumn
usdBgpRouteIpAddrPrefix = _UsdBgpRouteIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 15),
    _UsdBgpRouteIpAddrPrefix_Type()
)
usdBgpRouteIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpRouteIpAddrPrefix.setStatus("obsolete")


class _UsdBgpRouteRouteType_Type(Integer32):
    """Custom type usdBgpRouteRouteType based on Integer32"""
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
        *(("routeTypeAggregate", 4),
          ("routeTypeAutoSummary", 5),
          ("routeTypeNetwork", 2),
          ("routeTypeReceived", 1),
          ("routeTypeRedistributed", 3))
    )


_UsdBgpRouteRouteType_Type.__name__ = "Integer32"
_UsdBgpRouteRouteType_Object = MibTableColumn
usdBgpRouteRouteType = _UsdBgpRouteRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 16),
    _UsdBgpRouteRouteType_Type()
)
usdBgpRouteRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpRouteRouteType.setStatus("obsolete")


class _UsdBgpRouteOrigin_Type(Integer32):
    """Custom type usdBgpRouteOrigin based on Integer32"""
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


_UsdBgpRouteOrigin_Type.__name__ = "Integer32"
_UsdBgpRouteOrigin_Object = MibTableColumn
usdBgpRouteOrigin = _UsdBgpRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 17),
    _UsdBgpRouteOrigin_Type()
)
usdBgpRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteOrigin.setStatus("obsolete")


class _UsdBgpRouteASPathSegment_Type(OctetString):
    """Custom type usdBgpRouteASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_UsdBgpRouteASPathSegment_Type.__name__ = "OctetString"
_UsdBgpRouteASPathSegment_Object = MibTableColumn
usdBgpRouteASPathSegment = _UsdBgpRouteASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 18),
    _UsdBgpRouteASPathSegment_Type()
)
usdBgpRouteASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteASPathSegment.setStatus("obsolete")
_UsdBgpRouteNextHop_Type = IpAddress
_UsdBgpRouteNextHop_Object = MibTableColumn
usdBgpRouteNextHop = _UsdBgpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 19),
    _UsdBgpRouteNextHop_Type()
)
usdBgpRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteNextHop.setStatus("obsolete")
_UsdBgpRouteMultiExitDisc_Type = Unsigned32
_UsdBgpRouteMultiExitDisc_Object = MibTableColumn
usdBgpRouteMultiExitDisc = _UsdBgpRouteMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 20),
    _UsdBgpRouteMultiExitDisc_Type()
)
usdBgpRouteMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteMultiExitDisc.setStatus("obsolete")
_UsdBgpRouteLocalPref_Type = Unsigned32
_UsdBgpRouteLocalPref_Object = MibTableColumn
usdBgpRouteLocalPref = _UsdBgpRouteLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 21),
    _UsdBgpRouteLocalPref_Type()
)
usdBgpRouteLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteLocalPref.setStatus("obsolete")


class _UsdBgpRouteAtomicAggregate_Type(Integer32):
    """Custom type usdBgpRouteAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_UsdBgpRouteAtomicAggregate_Type.__name__ = "Integer32"
_UsdBgpRouteAtomicAggregate_Object = MibTableColumn
usdBgpRouteAtomicAggregate = _UsdBgpRouteAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 22),
    _UsdBgpRouteAtomicAggregate_Type()
)
usdBgpRouteAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteAtomicAggregate.setStatus("obsolete")


class _UsdBgpRouteAggregatorAS_Type(Integer32):
    """Custom type usdBgpRouteAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpRouteAggregatorAS_Type.__name__ = "Integer32"
_UsdBgpRouteAggregatorAS_Object = MibTableColumn
usdBgpRouteAggregatorAS = _UsdBgpRouteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 23),
    _UsdBgpRouteAggregatorAS_Type()
)
usdBgpRouteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteAggregatorAS.setStatus("obsolete")
_UsdBgpRouteAggregatorAddress_Type = IpAddress
_UsdBgpRouteAggregatorAddress_Object = MibTableColumn
usdBgpRouteAggregatorAddress = _UsdBgpRouteAggregatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 24),
    _UsdBgpRouteAggregatorAddress_Type()
)
usdBgpRouteAggregatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteAggregatorAddress.setStatus("obsolete")
_UsdBgpRouteBestInIpRouteTable_Type = TruthValue
_UsdBgpRouteBestInIpRouteTable_Object = MibTableColumn
usdBgpRouteBestInIpRouteTable = _UsdBgpRouteBestInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 25),
    _UsdBgpRouteBestInIpRouteTable_Type()
)
usdBgpRouteBestInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteBestInIpRouteTable.setStatus("obsolete")


class _UsdBgpRouteUnknown_Type(OctetString):
    """Custom type usdBgpRouteUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsdBgpRouteUnknown_Type.__name__ = "OctetString"
_UsdBgpRouteUnknown_Object = MibTableColumn
usdBgpRouteUnknown = _UsdBgpRouteUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 26),
    _UsdBgpRouteUnknown_Type()
)
usdBgpRouteUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteUnknown.setStatus("obsolete")
_UsdBgpRouteExtendedCommunitiesPresent_Type = TruthValue
_UsdBgpRouteExtendedCommunitiesPresent_Object = MibTableColumn
usdBgpRouteExtendedCommunitiesPresent = _UsdBgpRouteExtendedCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 27),
    _UsdBgpRouteExtendedCommunitiesPresent_Type()
)
usdBgpRouteExtendedCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteExtendedCommunitiesPresent.setStatus("obsolete")
_UsdBgpRouteValid_Type = TruthValue
_UsdBgpRouteValid_Object = MibTableColumn
usdBgpRouteValid = _UsdBgpRouteValid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 28),
    _UsdBgpRouteValid_Type()
)
usdBgpRouteValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteValid.setStatus("obsolete")


class _UsdBgpRouteSuppressedBy_Type(Integer32):
    """Custom type usdBgpRouteSuppressedBy based on Integer32"""
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
        *(("suppressedByAggregate", 2),
          ("suppressedByAutoSummary", 3),
          ("suppressedByDampening", 4),
          ("suppressedByNothing", 1))
    )


_UsdBgpRouteSuppressedBy_Type.__name__ = "Integer32"
_UsdBgpRouteSuppressedBy_Object = MibTableColumn
usdBgpRouteSuppressedBy = _UsdBgpRouteSuppressedBy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 29),
    _UsdBgpRouteSuppressedBy_Type()
)
usdBgpRouteSuppressedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteSuppressedBy.setStatus("obsolete")
_UsdBgpRouteNextHopReachable_Type = TruthValue
_UsdBgpRouteNextHopReachable_Object = MibTableColumn
usdBgpRouteNextHopReachable = _UsdBgpRouteNextHopReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 30),
    _UsdBgpRouteNextHopReachable_Type()
)
usdBgpRouteNextHopReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteNextHopReachable.setStatus("obsolete")
_UsdBgpRouteSynchronizedWithIgp_Type = TruthValue
_UsdBgpRouteSynchronizedWithIgp_Object = MibTableColumn
usdBgpRouteSynchronizedWithIgp = _UsdBgpRouteSynchronizedWithIgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 31),
    _UsdBgpRouteSynchronizedWithIgp_Type()
)
usdBgpRouteSynchronizedWithIgp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteSynchronizedWithIgp.setStatus("obsolete")
_UsdBgpRoutePlaceInIpRouteTable_Type = TruthValue
_UsdBgpRoutePlaceInIpRouteTable_Object = MibTableColumn
usdBgpRoutePlaceInIpRouteTable = _UsdBgpRoutePlaceInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 32),
    _UsdBgpRoutePlaceInIpRouteTable_Type()
)
usdBgpRoutePlaceInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRoutePlaceInIpRouteTable.setStatus("obsolete")
_UsdBgpRouteAdvertiseToExternalPeers_Type = TruthValue
_UsdBgpRouteAdvertiseToExternalPeers_Object = MibTableColumn
usdBgpRouteAdvertiseToExternalPeers = _UsdBgpRouteAdvertiseToExternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 33),
    _UsdBgpRouteAdvertiseToExternalPeers_Type()
)
usdBgpRouteAdvertiseToExternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteAdvertiseToExternalPeers.setStatus("obsolete")
_UsdBgpRouteAdvertiseToInternalPeers_Type = TruthValue
_UsdBgpRouteAdvertiseToInternalPeers_Object = MibTableColumn
usdBgpRouteAdvertiseToInternalPeers = _UsdBgpRouteAdvertiseToInternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 34),
    _UsdBgpRouteAdvertiseToInternalPeers_Type()
)
usdBgpRouteAdvertiseToInternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteAdvertiseToInternalPeers.setStatus("obsolete")


class _UsdBgpRouteDistinguisher_Type(OctetString):
    """Custom type usdBgpRouteDistinguisher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdBgpRouteDistinguisher_Type.__name__ = "OctetString"
_UsdBgpRouteDistinguisher_Object = MibTableColumn
usdBgpRouteDistinguisher = _UsdBgpRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 35),
    _UsdBgpRouteDistinguisher_Type()
)
usdBgpRouteDistinguisher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteDistinguisher.setStatus("obsolete")
_UsdBgpRouteMplsLabel_Type = Unsigned32
_UsdBgpRouteMplsLabel_Object = MibTableColumn
usdBgpRouteMplsLabel = _UsdBgpRouteMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 36),
    _UsdBgpRouteMplsLabel_Type()
)
usdBgpRouteMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteMplsLabel.setStatus("obsolete")
_UsdBgpRouteNextHopMetric_Type = Unsigned32
_UsdBgpRouteNextHopMetric_Object = MibTableColumn
usdBgpRouteNextHopMetric = _UsdBgpRouteNextHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 37),
    _UsdBgpRouteNextHopMetric_Type()
)
usdBgpRouteNextHopMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteNextHopMetric.setStatus("obsolete")
_UsdBgpRouteCommunityTable_Object = MibTable
usdBgpRouteCommunityTable = _UsdBgpRouteCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 14)
)
if mibBuilder.loadTexts:
    usdBgpRouteCommunityTable.setStatus("obsolete")
_UsdBgpRouteCommunityEntry_Object = MibTableRow
usdBgpRouteCommunityEntry = _UsdBgpRouteCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 14, 1)
)
usdBgpRouteCommunityEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteCommunityNumber"),
)
if mibBuilder.loadTexts:
    usdBgpRouteCommunityEntry.setStatus("obsolete")
_UsdBgpRouteCommunityNumber_Type = Unsigned32
_UsdBgpRouteCommunityNumber_Object = MibTableColumn
usdBgpRouteCommunityNumber = _UsdBgpRouteCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 14, 1, 1),
    _UsdBgpRouteCommunityNumber_Type()
)
usdBgpRouteCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteCommunityNumber.setStatus("obsolete")
_UsdBgpRouteClusterIdTable_Object = MibTable
usdBgpRouteClusterIdTable = _UsdBgpRouteClusterIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 15)
)
if mibBuilder.loadTexts:
    usdBgpRouteClusterIdTable.setStatus("obsolete")
_UsdBgpRouteClusterIdEntry_Object = MibTableRow
usdBgpRouteClusterIdEntry = _UsdBgpRouteClusterIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 15, 1)
)
usdBgpRouteClusterIdEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteClusterId"),
)
if mibBuilder.loadTexts:
    usdBgpRouteClusterIdEntry.setStatus("obsolete")
_UsdBgpRouteClusterId_Type = Unsigned32
_UsdBgpRouteClusterId_Object = MibTableColumn
usdBgpRouteClusterId = _UsdBgpRouteClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 15, 1, 1),
    _UsdBgpRouteClusterId_Type()
)
usdBgpRouteClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteClusterId.setStatus("obsolete")
_UsdBgpNetworkTable_Object = MibTable
usdBgpNetworkTable = _UsdBgpNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16)
)
if mibBuilder.loadTexts:
    usdBgpNetworkTable.setStatus("current")
_UsdBgpNetworkEntry_Object = MibTableRow
usdBgpNetworkEntry = _UsdBgpNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1)
)
usdBgpNetworkEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNetworkVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNetworkAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNetworkSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNetworkIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNetworkIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    usdBgpNetworkEntry.setStatus("current")
_UsdBgpNetworkVrfName_Type = UsdVrfName
_UsdBgpNetworkVrfName_Object = MibTableColumn
usdBgpNetworkVrfName = _UsdBgpNetworkVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 1),
    _UsdBgpNetworkVrfName_Type()
)
usdBgpNetworkVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNetworkVrfName.setStatus("current")
_UsdBgpNetworkAfi_Type = UsdBgpAfi
_UsdBgpNetworkAfi_Object = MibTableColumn
usdBgpNetworkAfi = _UsdBgpNetworkAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 2),
    _UsdBgpNetworkAfi_Type()
)
usdBgpNetworkAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNetworkAfi.setStatus("current")
_UsdBgpNetworkSafi_Type = UsdBgpSafi
_UsdBgpNetworkSafi_Object = MibTableColumn
usdBgpNetworkSafi = _UsdBgpNetworkSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 3),
    _UsdBgpNetworkSafi_Type()
)
usdBgpNetworkSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNetworkSafi.setStatus("current")
_UsdBgpNetworkIpAddrPrefix_Type = IpAddress
_UsdBgpNetworkIpAddrPrefix_Object = MibTableColumn
usdBgpNetworkIpAddrPrefix = _UsdBgpNetworkIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 4),
    _UsdBgpNetworkIpAddrPrefix_Type()
)
usdBgpNetworkIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNetworkIpAddrPrefix.setStatus("current")


class _UsdBgpNetworkIpAddrPrefixLen_Type(Integer32):
    """Custom type usdBgpNetworkIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdBgpNetworkIpAddrPrefixLen_Type.__name__ = "Integer32"
_UsdBgpNetworkIpAddrPrefixLen_Object = MibTableColumn
usdBgpNetworkIpAddrPrefixLen = _UsdBgpNetworkIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 5),
    _UsdBgpNetworkIpAddrPrefixLen_Type()
)
usdBgpNetworkIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNetworkIpAddrPrefixLen.setStatus("current")


class _UsdBgpNetworkBackdoor_Type(TruthValue):
    """Custom type usdBgpNetworkBackdoor based on TruthValue"""


_UsdBgpNetworkBackdoor_Object = MibTableColumn
usdBgpNetworkBackdoor = _UsdBgpNetworkBackdoor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 6),
    _UsdBgpNetworkBackdoor_Type()
)
usdBgpNetworkBackdoor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpNetworkBackdoor.setStatus("current")
_UsdBgpNetworkRowStatus_Type = RowStatus
_UsdBgpNetworkRowStatus_Object = MibTableColumn
usdBgpNetworkRowStatus = _UsdBgpNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 7),
    _UsdBgpNetworkRowStatus_Type()
)
usdBgpNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpNetworkRowStatus.setStatus("current")


class _UsdBgpNetworkWeightSpecified_Type(TruthValue):
    """Custom type usdBgpNetworkWeightSpecified based on TruthValue"""


_UsdBgpNetworkWeightSpecified_Object = MibTableColumn
usdBgpNetworkWeightSpecified = _UsdBgpNetworkWeightSpecified_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 8),
    _UsdBgpNetworkWeightSpecified_Type()
)
usdBgpNetworkWeightSpecified.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpNetworkWeightSpecified.setStatus("current")


class _UsdBgpNetworkWeight_Type(Integer32):
    """Custom type usdBgpNetworkWeight based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpNetworkWeight_Type.__name__ = "Integer32"
_UsdBgpNetworkWeight_Object = MibTableColumn
usdBgpNetworkWeight = _UsdBgpNetworkWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 9),
    _UsdBgpNetworkWeight_Type()
)
usdBgpNetworkWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpNetworkWeight.setStatus("current")


class _UsdBgpNetworkRouteMap_Type(DisplayString):
    """Custom type usdBgpNetworkRouteMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpNetworkRouteMap_Type.__name__ = "DisplayString"
_UsdBgpNetworkRouteMap_Object = MibTableColumn
usdBgpNetworkRouteMap = _UsdBgpNetworkRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 10),
    _UsdBgpNetworkRouteMap_Type()
)
usdBgpNetworkRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpNetworkRouteMap.setStatus("current")


class _UsdBgpNetworkUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpNetworkUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpNetworkBackdoor", 0),
          ("usdBgpNetworkRouteMap", 2),
          ("usdBgpNetworkWeight", 1))
    )

_UsdBgpNetworkUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpNetworkUnconfiguredAttributes_Object = MibTableColumn
usdBgpNetworkUnconfiguredAttributes = _UsdBgpNetworkUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 11),
    _UsdBgpNetworkUnconfiguredAttributes_Type()
)
usdBgpNetworkUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpNetworkUnconfiguredAttributes.setStatus("current")
_UsdBgpAggregateTable_Object = MibTable
usdBgpAggregateTable = _UsdBgpAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17)
)
if mibBuilder.loadTexts:
    usdBgpAggregateTable.setStatus("current")
_UsdBgpAggregateEntry_Object = MibTableRow
usdBgpAggregateEntry = _UsdBgpAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1)
)
usdBgpAggregateEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAggregateVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAggregateAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAggregateSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAggregateIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAggregateIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    usdBgpAggregateEntry.setStatus("current")
_UsdBgpAggregateVrfName_Type = UsdVrfName
_UsdBgpAggregateVrfName_Object = MibTableColumn
usdBgpAggregateVrfName = _UsdBgpAggregateVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 1),
    _UsdBgpAggregateVrfName_Type()
)
usdBgpAggregateVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAggregateVrfName.setStatus("current")
_UsdBgpAggregateAfi_Type = UsdBgpAfi
_UsdBgpAggregateAfi_Object = MibTableColumn
usdBgpAggregateAfi = _UsdBgpAggregateAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 2),
    _UsdBgpAggregateAfi_Type()
)
usdBgpAggregateAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAggregateAfi.setStatus("current")
_UsdBgpAggregateSafi_Type = UsdBgpSafi
_UsdBgpAggregateSafi_Object = MibTableColumn
usdBgpAggregateSafi = _UsdBgpAggregateSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 3),
    _UsdBgpAggregateSafi_Type()
)
usdBgpAggregateSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAggregateSafi.setStatus("current")
_UsdBgpAggregateIpAddrPrefix_Type = IpAddress
_UsdBgpAggregateIpAddrPrefix_Object = MibTableColumn
usdBgpAggregateIpAddrPrefix = _UsdBgpAggregateIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 4),
    _UsdBgpAggregateIpAddrPrefix_Type()
)
usdBgpAggregateIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAggregateIpAddrPrefix.setStatus("current")


class _UsdBgpAggregateIpAddrPrefixLen_Type(Integer32):
    """Custom type usdBgpAggregateIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdBgpAggregateIpAddrPrefixLen_Type.__name__ = "Integer32"
_UsdBgpAggregateIpAddrPrefixLen_Object = MibTableColumn
usdBgpAggregateIpAddrPrefixLen = _UsdBgpAggregateIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 5),
    _UsdBgpAggregateIpAddrPrefixLen_Type()
)
usdBgpAggregateIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAggregateIpAddrPrefixLen.setStatus("current")


class _UsdBgpAggregateAsSet_Type(TruthValue):
    """Custom type usdBgpAggregateAsSet based on TruthValue"""


_UsdBgpAggregateAsSet_Object = MibTableColumn
usdBgpAggregateAsSet = _UsdBgpAggregateAsSet_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 6),
    _UsdBgpAggregateAsSet_Type()
)
usdBgpAggregateAsSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAggregateAsSet.setStatus("current")


class _UsdBgpAggregateSummaryOnly_Type(TruthValue):
    """Custom type usdBgpAggregateSummaryOnly based on TruthValue"""


_UsdBgpAggregateSummaryOnly_Object = MibTableColumn
usdBgpAggregateSummaryOnly = _UsdBgpAggregateSummaryOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 7),
    _UsdBgpAggregateSummaryOnly_Type()
)
usdBgpAggregateSummaryOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAggregateSummaryOnly.setStatus("current")


class _UsdBgpAggregateAttributeMap_Type(DisplayString):
    """Custom type usdBgpAggregateAttributeMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpAggregateAttributeMap_Type.__name__ = "DisplayString"
_UsdBgpAggregateAttributeMap_Object = MibTableColumn
usdBgpAggregateAttributeMap = _UsdBgpAggregateAttributeMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 8),
    _UsdBgpAggregateAttributeMap_Type()
)
usdBgpAggregateAttributeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAggregateAttributeMap.setStatus("current")


class _UsdBgpAggregateAdvertiseMap_Type(DisplayString):
    """Custom type usdBgpAggregateAdvertiseMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpAggregateAdvertiseMap_Type.__name__ = "DisplayString"
_UsdBgpAggregateAdvertiseMap_Object = MibTableColumn
usdBgpAggregateAdvertiseMap = _UsdBgpAggregateAdvertiseMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 9),
    _UsdBgpAggregateAdvertiseMap_Type()
)
usdBgpAggregateAdvertiseMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAggregateAdvertiseMap.setStatus("current")
_UsdBgpAggregateRowStatus_Type = RowStatus
_UsdBgpAggregateRowStatus_Object = MibTableColumn
usdBgpAggregateRowStatus = _UsdBgpAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 10),
    _UsdBgpAggregateRowStatus_Type()
)
usdBgpAggregateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAggregateRowStatus.setStatus("current")


class _UsdBgpAggregateSuppressMap_Type(DisplayString):
    """Custom type usdBgpAggregateSuppressMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpAggregateSuppressMap_Type.__name__ = "DisplayString"
_UsdBgpAggregateSuppressMap_Object = MibTableColumn
usdBgpAggregateSuppressMap = _UsdBgpAggregateSuppressMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 11),
    _UsdBgpAggregateSuppressMap_Type()
)
usdBgpAggregateSuppressMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAggregateSuppressMap.setStatus("current")


class _UsdBgpAggregateUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpAggregateUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpAggregateAdvertiseMap", 3),
          ("usdBgpAggregateAsSet", 0),
          ("usdBgpAggregateAttributeMap", 2),
          ("usdBgpAggregateSummaryOnly", 1),
          ("usdBgpAggregateSuppressMap", 4))
    )

_UsdBgpAggregateUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpAggregateUnconfiguredAttributes_Object = MibTableColumn
usdBgpAggregateUnconfiguredAttributes = _UsdBgpAggregateUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 12),
    _UsdBgpAggregateUnconfiguredAttributes_Type()
)
usdBgpAggregateUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAggregateUnconfiguredAttributes.setStatus("current")
_UsdBgpVrfTable_Object = MibTable
usdBgpVrfTable = _UsdBgpVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18)
)
if mibBuilder.loadTexts:
    usdBgpVrfTable.setStatus("current")
_UsdBgpVrfEntry_Object = MibTableRow
usdBgpVrfEntry = _UsdBgpVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1)
)
usdBgpVrfEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpVrfName"),
)
if mibBuilder.loadTexts:
    usdBgpVrfEntry.setStatus("current")
_UsdBgpVrfName_Type = UsdVrfName
_UsdBgpVrfName_Object = MibTableColumn
usdBgpVrfName = _UsdBgpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 1),
    _UsdBgpVrfName_Type()
)
usdBgpVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpVrfName.setStatus("current")


class _UsdBgpVrfSynchronization_Type(TruthValue):
    """Custom type usdBgpVrfSynchronization based on TruthValue"""


_UsdBgpVrfSynchronization_Object = MibTableColumn
usdBgpVrfSynchronization = _UsdBgpVrfSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 2),
    _UsdBgpVrfSynchronization_Type()
)
usdBgpVrfSynchronization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfSynchronization.setStatus("current")


class _UsdBgpVrfAutoSummary_Type(TruthValue):
    """Custom type usdBgpVrfAutoSummary based on TruthValue"""


_UsdBgpVrfAutoSummary_Object = MibTableColumn
usdBgpVrfAutoSummary = _UsdBgpVrfAutoSummary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 3),
    _UsdBgpVrfAutoSummary_Type()
)
usdBgpVrfAutoSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfAutoSummary.setStatus("current")


class _UsdBgpVrfExternalDistance_Type(Integer32):
    """Custom type usdBgpVrfExternalDistance based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdBgpVrfExternalDistance_Type.__name__ = "Integer32"
_UsdBgpVrfExternalDistance_Object = MibTableColumn
usdBgpVrfExternalDistance = _UsdBgpVrfExternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 4),
    _UsdBgpVrfExternalDistance_Type()
)
usdBgpVrfExternalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfExternalDistance.setStatus("current")


class _UsdBgpVrfInternalDistance_Type(Integer32):
    """Custom type usdBgpVrfInternalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdBgpVrfInternalDistance_Type.__name__ = "Integer32"
_UsdBgpVrfInternalDistance_Object = MibTableColumn
usdBgpVrfInternalDistance = _UsdBgpVrfInternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 5),
    _UsdBgpVrfInternalDistance_Type()
)
usdBgpVrfInternalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfInternalDistance.setStatus("current")


class _UsdBgpVrfLocalDistance_Type(Integer32):
    """Custom type usdBgpVrfLocalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdBgpVrfLocalDistance_Type.__name__ = "Integer32"
_UsdBgpVrfLocalDistance_Object = MibTableColumn
usdBgpVrfLocalDistance = _UsdBgpVrfLocalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 6),
    _UsdBgpVrfLocalDistance_Type()
)
usdBgpVrfLocalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfLocalDistance.setStatus("current")


class _UsdBgpVrfResetConnectionType_Type(UsdBgpResetConnectionType):
    """Custom type usdBgpVrfResetConnectionType based on UsdBgpResetConnectionType"""


_UsdBgpVrfResetConnectionType_Object = MibTableColumn
usdBgpVrfResetConnectionType = _UsdBgpVrfResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 7),
    _UsdBgpVrfResetConnectionType_Type()
)
usdBgpVrfResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfResetConnectionType.setStatus("current")
_UsdBgpVrfRowStatus_Type = RowStatus
_UsdBgpVrfRowStatus_Object = MibTableColumn
usdBgpVrfRowStatus = _UsdBgpVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 8),
    _UsdBgpVrfRowStatus_Type()
)
usdBgpVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfRowStatus.setStatus("current")


class _UsdBgpVrfOperationalState_Type(Integer32):
    """Custom type usdBgpVrfOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipVrfNotPresent", 0),
          ("ipVrfPresent", 1))
    )


_UsdBgpVrfOperationalState_Type.__name__ = "Integer32"
_UsdBgpVrfOperationalState_Object = MibTableColumn
usdBgpVrfOperationalState = _UsdBgpVrfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 9),
    _UsdBgpVrfOperationalState_Type()
)
usdBgpVrfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpVrfOperationalState.setStatus("current")


class _UsdBgpVrfAddUnicastRoutesToMulticastView_Type(TruthValue):
    """Custom type usdBgpVrfAddUnicastRoutesToMulticastView based on TruthValue"""


_UsdBgpVrfAddUnicastRoutesToMulticastView_Object = MibTableColumn
usdBgpVrfAddUnicastRoutesToMulticastView = _UsdBgpVrfAddUnicastRoutesToMulticastView_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 10),
    _UsdBgpVrfAddUnicastRoutesToMulticastView_Type()
)
usdBgpVrfAddUnicastRoutesToMulticastView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfAddUnicastRoutesToMulticastView.setStatus("current")


class _UsdBgpVrfUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpVrfUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpVrfAddUnicastRoutesToMulticastView", 5),
          ("usdBgpVrfAutoSummary", 1),
          ("usdBgpVrfExternalDistance", 2),
          ("usdBgpVrfInternalDistance", 3),
          ("usdBgpVrfLocalDistance", 4),
          ("usdBgpVrfSynchronization", 0))
    )

_UsdBgpVrfUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpVrfUnconfiguredAttributes_Object = MibTableColumn
usdBgpVrfUnconfiguredAttributes = _UsdBgpVrfUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 13),
    _UsdBgpVrfUnconfiguredAttributes_Type()
)
usdBgpVrfUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpVrfUnconfiguredAttributes.setStatus("current")
_UsdBgpAddressFamilyTable_Object = MibTable
usdBgpAddressFamilyTable = _UsdBgpAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19)
)
if mibBuilder.loadTexts:
    usdBgpAddressFamilyTable.setStatus("current")
_UsdBgpAddressFamilyEntry_Object = MibTableRow
usdBgpAddressFamilyEntry = _UsdBgpAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1)
)
usdBgpAddressFamilyEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpAddressFamilySafi"),
)
if mibBuilder.loadTexts:
    usdBgpAddressFamilyEntry.setStatus("current")
_UsdBgpAddressFamilyVrfName_Type = UsdVrfName
_UsdBgpAddressFamilyVrfName_Object = MibTableColumn
usdBgpAddressFamilyVrfName = _UsdBgpAddressFamilyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 1),
    _UsdBgpAddressFamilyVrfName_Type()
)
usdBgpAddressFamilyVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyVrfName.setStatus("current")
_UsdBgpAddressFamilyAfi_Type = UsdBgpAfi
_UsdBgpAddressFamilyAfi_Object = MibTableColumn
usdBgpAddressFamilyAfi = _UsdBgpAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 2),
    _UsdBgpAddressFamilyAfi_Type()
)
usdBgpAddressFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyAfi.setStatus("current")
_UsdBgpAddressFamilySafi_Type = UsdBgpSafi
_UsdBgpAddressFamilySafi_Object = MibTableColumn
usdBgpAddressFamilySafi = _UsdBgpAddressFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 3),
    _UsdBgpAddressFamilySafi_Type()
)
usdBgpAddressFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpAddressFamilySafi.setStatus("current")


class _UsdBgpAddressFamilyDefaultOriginate_Type(TruthValue):
    """Custom type usdBgpAddressFamilyDefaultOriginate based on TruthValue"""


_UsdBgpAddressFamilyDefaultOriginate_Object = MibTableColumn
usdBgpAddressFamilyDefaultOriginate = _UsdBgpAddressFamilyDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 4),
    _UsdBgpAddressFamilyDefaultOriginate_Type()
)
usdBgpAddressFamilyDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDefaultOriginate.setStatus("current")


class _UsdBgpAddressFamilyRouteFlapDampening_Type(TruthValue):
    """Custom type usdBgpAddressFamilyRouteFlapDampening based on TruthValue"""


_UsdBgpAddressFamilyRouteFlapDampening_Object = MibTableColumn
usdBgpAddressFamilyRouteFlapDampening = _UsdBgpAddressFamilyRouteFlapDampening_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 5),
    _UsdBgpAddressFamilyRouteFlapDampening_Type()
)
usdBgpAddressFamilyRouteFlapDampening.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyRouteFlapDampening.setStatus("current")


class _UsdBgpAddressFamilyDampeningSuppressThreshold_Type(Unsigned32):
    """Custom type usdBgpAddressFamilyDampeningSuppressThreshold based on Unsigned32"""
    defaultValue = 1000


_UsdBgpAddressFamilyDampeningSuppressThreshold_Object = MibTableColumn
usdBgpAddressFamilyDampeningSuppressThreshold = _UsdBgpAddressFamilyDampeningSuppressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 6),
    _UsdBgpAddressFamilyDampeningSuppressThreshold_Type()
)
usdBgpAddressFamilyDampeningSuppressThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningSuppressThreshold.setStatus("current")


class _UsdBgpAddressFamilyDampeningReuseThreshold_Type(Unsigned32):
    """Custom type usdBgpAddressFamilyDampeningReuseThreshold based on Unsigned32"""
    defaultValue = 1000


_UsdBgpAddressFamilyDampeningReuseThreshold_Object = MibTableColumn
usdBgpAddressFamilyDampeningReuseThreshold = _UsdBgpAddressFamilyDampeningReuseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 7),
    _UsdBgpAddressFamilyDampeningReuseThreshold_Type()
)
usdBgpAddressFamilyDampeningReuseThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningReuseThreshold.setStatus("current")


class _UsdBgpAddressFamilyDampeningMaxHoldDownTime_Type(Unsigned32):
    """Custom type usdBgpAddressFamilyDampeningMaxHoldDownTime based on Unsigned32"""
    defaultValue = 20


_UsdBgpAddressFamilyDampeningMaxHoldDownTime_Object = MibTableColumn
usdBgpAddressFamilyDampeningMaxHoldDownTime = _UsdBgpAddressFamilyDampeningMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 8),
    _UsdBgpAddressFamilyDampeningMaxHoldDownTime_Type()
)
usdBgpAddressFamilyDampeningMaxHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningMaxHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningMaxHoldDownTime.setUnits("seconds")


class _UsdBgpAddressFamilyDampeningHalfLifeReachable_Type(Unsigned32):
    """Custom type usdBgpAddressFamilyDampeningHalfLifeReachable based on Unsigned32"""
    defaultValue = 5


_UsdBgpAddressFamilyDampeningHalfLifeReachable_Object = MibTableColumn
usdBgpAddressFamilyDampeningHalfLifeReachable = _UsdBgpAddressFamilyDampeningHalfLifeReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 9),
    _UsdBgpAddressFamilyDampeningHalfLifeReachable_Type()
)
usdBgpAddressFamilyDampeningHalfLifeReachable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningHalfLifeReachable.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningHalfLifeReachable.setUnits("seconds")


class _UsdBgpAddressFamilyDampeningHalfLifeUnreachable_Type(Unsigned32):
    """Custom type usdBgpAddressFamilyDampeningHalfLifeUnreachable based on Unsigned32"""
    defaultValue = 5


_UsdBgpAddressFamilyDampeningHalfLifeUnreachable_Object = MibTableColumn
usdBgpAddressFamilyDampeningHalfLifeUnreachable = _UsdBgpAddressFamilyDampeningHalfLifeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 10),
    _UsdBgpAddressFamilyDampeningHalfLifeUnreachable_Type()
)
usdBgpAddressFamilyDampeningHalfLifeUnreachable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningHalfLifeUnreachable.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningHalfLifeUnreachable.setUnits("seconds")


class _UsdBgpAddressFamilyDampeningRouteMapName_Type(DisplayString):
    """Custom type usdBgpAddressFamilyDampeningRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UsdBgpAddressFamilyDampeningRouteMapName_Type.__name__ = "DisplayString"
_UsdBgpAddressFamilyDampeningRouteMapName_Object = MibTableColumn
usdBgpAddressFamilyDampeningRouteMapName = _UsdBgpAddressFamilyDampeningRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 11),
    _UsdBgpAddressFamilyDampeningRouteMapName_Type()
)
usdBgpAddressFamilyDampeningRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyDampeningRouteMapName.setStatus("current")


class _UsdBgpAddressFamilyResetConnectionType_Type(UsdBgpResetConnectionType):
    """Custom type usdBgpAddressFamilyResetConnectionType based on UsdBgpResetConnectionType"""


_UsdBgpAddressFamilyResetConnectionType_Object = MibTableColumn
usdBgpAddressFamilyResetConnectionType = _UsdBgpAddressFamilyResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 12),
    _UsdBgpAddressFamilyResetConnectionType_Type()
)
usdBgpAddressFamilyResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyResetConnectionType.setStatus("current")
_UsdBgpAddressFamilyRowStatus_Type = RowStatus
_UsdBgpAddressFamilyRowStatus_Object = MibTableColumn
usdBgpAddressFamilyRowStatus = _UsdBgpAddressFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 13),
    _UsdBgpAddressFamilyRowStatus_Type()
)
usdBgpAddressFamilyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyRowStatus.setStatus("current")


class _UsdBgpAddressFamilyOperationalState_Type(Integer32):
    """Custom type usdBgpAddressFamilyOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ipVrfNotPresent", 0),
          ("ipVrfPresent", 1))
    )


_UsdBgpAddressFamilyOperationalState_Type.__name__ = "Integer32"
_UsdBgpAddressFamilyOperationalState_Object = MibTableColumn
usdBgpAddressFamilyOperationalState = _UsdBgpAddressFamilyOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 14),
    _UsdBgpAddressFamilyOperationalState_Type()
)
usdBgpAddressFamilyOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyOperationalState.setStatus("current")


class _UsdBgpAddressFamilyUnconfiguredAttributes_Type(Bits):
    """Custom type usdBgpAddressFamilyUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("usdBgpAddressFamilyDampeningHalfLifeReachable", 5),
          ("usdBgpAddressFamilyDampeningHalfLifeUnreachable", 6),
          ("usdBgpAddressFamilyDampeningMaxHoldDownTime", 4),
          ("usdBgpAddressFamilyDampeningReuseThreshold", 3),
          ("usdBgpAddressFamilyDampeningRouteMapName", 7),
          ("usdBgpAddressFamilyDampeningSuppressThreshold", 2),
          ("usdBgpAddressFamilyDefaultOriginate", 0),
          ("usdBgpAddressFamilyRouteFlapDampening", 1))
    )

_UsdBgpAddressFamilyUnconfiguredAttributes_Type.__name__ = "Bits"
_UsdBgpAddressFamilyUnconfiguredAttributes_Object = MibTableColumn
usdBgpAddressFamilyUnconfiguredAttributes = _UsdBgpAddressFamilyUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 15),
    _UsdBgpAddressFamilyUnconfiguredAttributes_Type()
)
usdBgpAddressFamilyUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdBgpAddressFamilyUnconfiguredAttributes.setStatus("current")
_UsdBgpStorageGroup_ObjectIdentity = ObjectIdentity
usdBgpStorageGroup = _UsdBgpStorageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20)
)


class _UsdBgpStorageInitialHeapSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialHeapSize based on UsdBgpStorageInteger"""
    defaultValue = 33554432


_UsdBgpStorageInitialHeapSize_Object = MibScalar
usdBgpStorageInitialHeapSize = _UsdBgpStorageInitialHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 1),
    _UsdBgpStorageInitialHeapSize_Type()
)
usdBgpStorageInitialHeapSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialHeapSize.setStatus("current")


class _UsdBgpStorageMaxHeapSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxHeapSize based on UsdBgpStorageInteger"""
    defaultValue = 536870912


_UsdBgpStorageMaxHeapSize_Object = MibScalar
usdBgpStorageMaxHeapSize = _UsdBgpStorageMaxHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 2),
    _UsdBgpStorageMaxHeapSize_Type()
)
usdBgpStorageMaxHeapSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxHeapSize.setStatus("current")


class _UsdBgpStorageInitialVrfPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialVrfPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialVrfPoolSize_Object = MibScalar
usdBgpStorageInitialVrfPoolSize = _UsdBgpStorageInitialVrfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 4),
    _UsdBgpStorageInitialVrfPoolSize_Type()
)
usdBgpStorageInitialVrfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialVrfPoolSize.setStatus("current")


class _UsdBgpStorageMaxVrfPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxVrfPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxVrfPoolSize_Object = MibScalar
usdBgpStorageMaxVrfPoolSize = _UsdBgpStorageMaxVrfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 5),
    _UsdBgpStorageMaxVrfPoolSize_Type()
)
usdBgpStorageMaxVrfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxVrfPoolSize.setStatus("current")


class _UsdBgpStorageInitialAddressFamilyPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialAddressFamilyPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialAddressFamilyPoolSize_Object = MibScalar
usdBgpStorageInitialAddressFamilyPoolSize = _UsdBgpStorageInitialAddressFamilyPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 6),
    _UsdBgpStorageInitialAddressFamilyPoolSize_Type()
)
usdBgpStorageInitialAddressFamilyPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialAddressFamilyPoolSize.setStatus("current")


class _UsdBgpStorageMaxAddressFamilyPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxAddressFamilyPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxAddressFamilyPoolSize_Object = MibScalar
usdBgpStorageMaxAddressFamilyPoolSize = _UsdBgpStorageMaxAddressFamilyPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 7),
    _UsdBgpStorageMaxAddressFamilyPoolSize_Type()
)
usdBgpStorageMaxAddressFamilyPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxAddressFamilyPoolSize.setStatus("current")


class _UsdBgpStorageInitialPeerPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialPeerPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialPeerPoolSize_Object = MibScalar
usdBgpStorageInitialPeerPoolSize = _UsdBgpStorageInitialPeerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 8),
    _UsdBgpStorageInitialPeerPoolSize_Type()
)
usdBgpStorageInitialPeerPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialPeerPoolSize.setStatus("current")


class _UsdBgpStorageMaxPeerPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxPeerPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxPeerPoolSize_Object = MibScalar
usdBgpStorageMaxPeerPoolSize = _UsdBgpStorageMaxPeerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 9),
    _UsdBgpStorageMaxPeerPoolSize_Type()
)
usdBgpStorageMaxPeerPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxPeerPoolSize.setStatus("current")


class _UsdBgpStorageInitialPeerAfPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialPeerAfPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialPeerAfPoolSize_Object = MibScalar
usdBgpStorageInitialPeerAfPoolSize = _UsdBgpStorageInitialPeerAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 10),
    _UsdBgpStorageInitialPeerAfPoolSize_Type()
)
usdBgpStorageInitialPeerAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialPeerAfPoolSize.setStatus("current")


class _UsdBgpStorageMaxPeerAfPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxPeerAfPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxPeerAfPoolSize_Object = MibScalar
usdBgpStorageMaxPeerAfPoolSize = _UsdBgpStorageMaxPeerAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 11),
    _UsdBgpStorageMaxPeerAfPoolSize_Type()
)
usdBgpStorageMaxPeerAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxPeerAfPoolSize.setStatus("current")


class _UsdBgpStorageInitialPeerGroupPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialPeerGroupPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialPeerGroupPoolSize_Object = MibScalar
usdBgpStorageInitialPeerGroupPoolSize = _UsdBgpStorageInitialPeerGroupPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 12),
    _UsdBgpStorageInitialPeerGroupPoolSize_Type()
)
usdBgpStorageInitialPeerGroupPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialPeerGroupPoolSize.setStatus("current")


class _UsdBgpStorageMaxPeerGroupPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxPeerGroupPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxPeerGroupPoolSize_Object = MibScalar
usdBgpStorageMaxPeerGroupPoolSize = _UsdBgpStorageMaxPeerGroupPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 13),
    _UsdBgpStorageMaxPeerGroupPoolSize_Type()
)
usdBgpStorageMaxPeerGroupPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxPeerGroupPoolSize.setStatus("current")


class _UsdBgpStorageInitialPeerGroupAfPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialPeerGroupAfPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialPeerGroupAfPoolSize_Object = MibScalar
usdBgpStorageInitialPeerGroupAfPoolSize = _UsdBgpStorageInitialPeerGroupAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 14),
    _UsdBgpStorageInitialPeerGroupAfPoolSize_Type()
)
usdBgpStorageInitialPeerGroupAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialPeerGroupAfPoolSize.setStatus("current")


class _UsdBgpStorageMaxPeerGroupAfPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxPeerGroupAfPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxPeerGroupAfPoolSize_Object = MibScalar
usdBgpStorageMaxPeerGroupAfPoolSize = _UsdBgpStorageMaxPeerGroupAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 15),
    _UsdBgpStorageMaxPeerGroupAfPoolSize_Type()
)
usdBgpStorageMaxPeerGroupAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxPeerGroupAfPoolSize.setStatus("current")


class _UsdBgpStorageInitialNetworkPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialNetworkPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialNetworkPoolSize_Object = MibScalar
usdBgpStorageInitialNetworkPoolSize = _UsdBgpStorageInitialNetworkPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 16),
    _UsdBgpStorageInitialNetworkPoolSize_Type()
)
usdBgpStorageInitialNetworkPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialNetworkPoolSize.setStatus("current")


class _UsdBgpStorageMaxNetworkPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxNetworkPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxNetworkPoolSize_Object = MibScalar
usdBgpStorageMaxNetworkPoolSize = _UsdBgpStorageMaxNetworkPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 17),
    _UsdBgpStorageMaxNetworkPoolSize_Type()
)
usdBgpStorageMaxNetworkPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxNetworkPoolSize.setStatus("current")


class _UsdBgpStorageInitialAggregatePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialAggregatePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialAggregatePoolSize_Object = MibScalar
usdBgpStorageInitialAggregatePoolSize = _UsdBgpStorageInitialAggregatePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 18),
    _UsdBgpStorageInitialAggregatePoolSize_Type()
)
usdBgpStorageInitialAggregatePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialAggregatePoolSize.setStatus("current")


class _UsdBgpStorageMaxAggregatePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxAggregatePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxAggregatePoolSize_Object = MibScalar
usdBgpStorageMaxAggregatePoolSize = _UsdBgpStorageMaxAggregatePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 19),
    _UsdBgpStorageMaxAggregatePoolSize_Type()
)
usdBgpStorageMaxAggregatePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxAggregatePoolSize.setStatus("current")


class _UsdBgpStorageInitialDestinationPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialDestinationPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialDestinationPoolSize_Object = MibScalar
usdBgpStorageInitialDestinationPoolSize = _UsdBgpStorageInitialDestinationPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 20),
    _UsdBgpStorageInitialDestinationPoolSize_Type()
)
usdBgpStorageInitialDestinationPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialDestinationPoolSize.setStatus("current")


class _UsdBgpStorageMaxDestinationPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxDestinationPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxDestinationPoolSize_Object = MibScalar
usdBgpStorageMaxDestinationPoolSize = _UsdBgpStorageMaxDestinationPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 21),
    _UsdBgpStorageMaxDestinationPoolSize_Type()
)
usdBgpStorageMaxDestinationPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxDestinationPoolSize.setStatus("current")


class _UsdBgpStorageInitialRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialRoutePoolSize_Object = MibScalar
usdBgpStorageInitialRoutePoolSize = _UsdBgpStorageInitialRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 22),
    _UsdBgpStorageInitialRoutePoolSize_Type()
)
usdBgpStorageInitialRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialRoutePoolSize.setStatus("current")


class _UsdBgpStorageMaxRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxRoutePoolSize_Object = MibScalar
usdBgpStorageMaxRoutePoolSize = _UsdBgpStorageMaxRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 23),
    _UsdBgpStorageMaxRoutePoolSize_Type()
)
usdBgpStorageMaxRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxRoutePoolSize.setStatus("current")


class _UsdBgpStorageInitialAttributesPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialAttributesPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialAttributesPoolSize_Object = MibScalar
usdBgpStorageInitialAttributesPoolSize = _UsdBgpStorageInitialAttributesPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 24),
    _UsdBgpStorageInitialAttributesPoolSize_Type()
)
usdBgpStorageInitialAttributesPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialAttributesPoolSize.setStatus("current")


class _UsdBgpStorageMaxAttributesPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxAttributesPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxAttributesPoolSize_Object = MibScalar
usdBgpStorageMaxAttributesPoolSize = _UsdBgpStorageMaxAttributesPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 25),
    _UsdBgpStorageMaxAttributesPoolSize_Type()
)
usdBgpStorageMaxAttributesPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxAttributesPoolSize.setStatus("current")


class _UsdBgpStorageInitialRouteFlapHistoryPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialRouteFlapHistoryPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialRouteFlapHistoryPoolSize_Object = MibScalar
usdBgpStorageInitialRouteFlapHistoryPoolSize = _UsdBgpStorageInitialRouteFlapHistoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 26),
    _UsdBgpStorageInitialRouteFlapHistoryPoolSize_Type()
)
usdBgpStorageInitialRouteFlapHistoryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialRouteFlapHistoryPoolSize.setStatus("current")


class _UsdBgpStorageMaxRouteFlapHistoryPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxRouteFlapHistoryPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxRouteFlapHistoryPoolSize_Object = MibScalar
usdBgpStorageMaxRouteFlapHistoryPoolSize = _UsdBgpStorageMaxRouteFlapHistoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 27),
    _UsdBgpStorageMaxRouteFlapHistoryPoolSize_Type()
)
usdBgpStorageMaxRouteFlapHistoryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxRouteFlapHistoryPoolSize.setStatus("current")


class _UsdBgpStorageInitialNetworkRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialNetworkRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialNetworkRoutePoolSize_Object = MibScalar
usdBgpStorageInitialNetworkRoutePoolSize = _UsdBgpStorageInitialNetworkRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 28),
    _UsdBgpStorageInitialNetworkRoutePoolSize_Type()
)
usdBgpStorageInitialNetworkRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialNetworkRoutePoolSize.setStatus("current")


class _UsdBgpStorageMaxNetworkRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxNetworkRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxNetworkRoutePoolSize_Object = MibScalar
usdBgpStorageMaxNetworkRoutePoolSize = _UsdBgpStorageMaxNetworkRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 29),
    _UsdBgpStorageMaxNetworkRoutePoolSize_Type()
)
usdBgpStorageMaxNetworkRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxNetworkRoutePoolSize.setStatus("current")


class _UsdBgpStorageInitialRedistributedRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialRedistributedRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialRedistributedRoutePoolSize_Object = MibScalar
usdBgpStorageInitialRedistributedRoutePoolSize = _UsdBgpStorageInitialRedistributedRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 30),
    _UsdBgpStorageInitialRedistributedRoutePoolSize_Type()
)
usdBgpStorageInitialRedistributedRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialRedistributedRoutePoolSize.setStatus("current")


class _UsdBgpStorageMaxRedistributedRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxRedistributedRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxRedistributedRoutePoolSize_Object = MibScalar
usdBgpStorageMaxRedistributedRoutePoolSize = _UsdBgpStorageMaxRedistributedRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 31),
    _UsdBgpStorageMaxRedistributedRoutePoolSize_Type()
)
usdBgpStorageMaxRedistributedRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxRedistributedRoutePoolSize.setStatus("current")


class _UsdBgpStorageInitialAggregateRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialAggregateRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialAggregateRoutePoolSize_Object = MibScalar
usdBgpStorageInitialAggregateRoutePoolSize = _UsdBgpStorageInitialAggregateRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 32),
    _UsdBgpStorageInitialAggregateRoutePoolSize_Type()
)
usdBgpStorageInitialAggregateRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialAggregateRoutePoolSize.setStatus("current")


class _UsdBgpStorageMaxAggregateRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxAggregateRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxAggregateRoutePoolSize_Object = MibScalar
usdBgpStorageMaxAggregateRoutePoolSize = _UsdBgpStorageMaxAggregateRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 33),
    _UsdBgpStorageMaxAggregateRoutePoolSize_Type()
)
usdBgpStorageMaxAggregateRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxAggregateRoutePoolSize.setStatus("current")


class _UsdBgpStorageInitialAutoSummaryRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialAutoSummaryRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialAutoSummaryRoutePoolSize_Object = MibScalar
usdBgpStorageInitialAutoSummaryRoutePoolSize = _UsdBgpStorageInitialAutoSummaryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 34),
    _UsdBgpStorageInitialAutoSummaryRoutePoolSize_Type()
)
usdBgpStorageInitialAutoSummaryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialAutoSummaryRoutePoolSize.setStatus("current")


class _UsdBgpStorageMaxAutoSummaryRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxAutoSummaryRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxAutoSummaryRoutePoolSize_Object = MibScalar
usdBgpStorageMaxAutoSummaryRoutePoolSize = _UsdBgpStorageMaxAutoSummaryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 35),
    _UsdBgpStorageMaxAutoSummaryRoutePoolSize_Type()
)
usdBgpStorageMaxAutoSummaryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxAutoSummaryRoutePoolSize.setStatus("current")


class _UsdBgpStorageInitialHistoryRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialHistoryRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialHistoryRoutePoolSize_Object = MibScalar
usdBgpStorageInitialHistoryRoutePoolSize = _UsdBgpStorageInitialHistoryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 36),
    _UsdBgpStorageInitialHistoryRoutePoolSize_Type()
)
usdBgpStorageInitialHistoryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialHistoryRoutePoolSize.setStatus("obsolete")


class _UsdBgpStorageMaxHistoryRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxHistoryRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxHistoryRoutePoolSize_Object = MibScalar
usdBgpStorageMaxHistoryRoutePoolSize = _UsdBgpStorageMaxHistoryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 37),
    _UsdBgpStorageMaxHistoryRoutePoolSize_Type()
)
usdBgpStorageMaxHistoryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxHistoryRoutePoolSize.setStatus("obsolete")


class _UsdBgpStorageInitialSendQueueEntryPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialSendQueueEntryPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialSendQueueEntryPoolSize_Object = MibScalar
usdBgpStorageInitialSendQueueEntryPoolSize = _UsdBgpStorageInitialSendQueueEntryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 38),
    _UsdBgpStorageInitialSendQueueEntryPoolSize_Type()
)
usdBgpStorageInitialSendQueueEntryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialSendQueueEntryPoolSize.setStatus("current")


class _UsdBgpStorageMaxSendQueueEntryPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxSendQueueEntryPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxSendQueueEntryPoolSize_Object = MibScalar
usdBgpStorageMaxSendQueueEntryPoolSize = _UsdBgpStorageMaxSendQueueEntryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 39),
    _UsdBgpStorageMaxSendQueueEntryPoolSize_Type()
)
usdBgpStorageMaxSendQueueEntryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxSendQueueEntryPoolSize.setStatus("current")


class _UsdBgpStorageInitialVpnRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialVpnRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialVpnRoutePoolSize_Object = MibScalar
usdBgpStorageInitialVpnRoutePoolSize = _UsdBgpStorageInitialVpnRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 40),
    _UsdBgpStorageInitialVpnRoutePoolSize_Type()
)
usdBgpStorageInitialVpnRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialVpnRoutePoolSize.setStatus("current")


class _UsdBgpStorageMaxVpnRoutePoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxVpnRoutePoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxVpnRoutePoolSize_Object = MibScalar
usdBgpStorageMaxVpnRoutePoolSize = _UsdBgpStorageMaxVpnRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 41),
    _UsdBgpStorageMaxVpnRoutePoolSize_Type()
)
usdBgpStorageMaxVpnRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxVpnRoutePoolSize.setStatus("current")


class _UsdBgpStorageInitialRouteTargetPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageInitialRouteTargetPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 1


_UsdBgpStorageInitialRouteTargetPoolSize_Object = MibScalar
usdBgpStorageInitialRouteTargetPoolSize = _UsdBgpStorageInitialRouteTargetPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 42),
    _UsdBgpStorageInitialRouteTargetPoolSize_Type()
)
usdBgpStorageInitialRouteTargetPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageInitialRouteTargetPoolSize.setStatus("current")


class _UsdBgpStorageMaxRouteTargetPoolSize_Type(UsdBgpStorageInteger):
    """Custom type usdBgpStorageMaxRouteTargetPoolSize based on UsdBgpStorageInteger"""
    defaultValue = 500000000


_UsdBgpStorageMaxRouteTargetPoolSize_Object = MibScalar
usdBgpStorageMaxRouteTargetPoolSize = _UsdBgpStorageMaxRouteTargetPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 43),
    _UsdBgpStorageMaxRouteTargetPoolSize_Type()
)
usdBgpStorageMaxRouteTargetPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdBgpStorageMaxRouteTargetPoolSize.setStatus("current")
_UsdBgpRouteExtendedCommunityTable_Object = MibTable
usdBgpRouteExtendedCommunityTable = _UsdBgpRouteExtendedCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 22)
)
if mibBuilder.loadTexts:
    usdBgpRouteExtendedCommunityTable.setStatus("obsolete")
_UsdBgpRouteExtendedCommunityEntry_Object = MibTableRow
usdBgpRouteExtendedCommunityEntry = _UsdBgpRouteExtendedCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 22, 1)
)
usdBgpRouteExtendedCommunityEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpRouteExtendedCommunityNumber"),
)
if mibBuilder.loadTexts:
    usdBgpRouteExtendedCommunityEntry.setStatus("obsolete")


class _UsdBgpRouteExtendedCommunityNumber_Type(OctetString):
    """Custom type usdBgpRouteExtendedCommunityNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdBgpRouteExtendedCommunityNumber_Type.__name__ = "OctetString"
_UsdBgpRouteExtendedCommunityNumber_Object = MibTableColumn
usdBgpRouteExtendedCommunityNumber = _UsdBgpRouteExtendedCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 22, 1, 1),
    _UsdBgpRouteExtendedCommunityNumber_Type()
)
usdBgpRouteExtendedCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpRouteExtendedCommunityNumber.setStatus("obsolete")
_UsdBgpNewRouteTable_Object = MibTable
usdBgpNewRouteTable = _UsdBgpNewRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23)
)
if mibBuilder.loadTexts:
    usdBgpNewRouteTable.setStatus("current")
_UsdBgpNewRouteEntry_Object = MibTableRow
usdBgpNewRouteEntry = _UsdBgpNewRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1)
)
usdBgpNewRouteEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteOriginalRd"),
)
if mibBuilder.loadTexts:
    usdBgpNewRouteEntry.setStatus("current")
_UsdBgpNewRouteVrfName_Type = UsdVrfName
_UsdBgpNewRouteVrfName_Object = MibTableColumn
usdBgpNewRouteVrfName = _UsdBgpNewRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 1),
    _UsdBgpNewRouteVrfName_Type()
)
usdBgpNewRouteVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteVrfName.setStatus("current")
_UsdBgpNewRouteAfi_Type = UsdBgpAfi
_UsdBgpNewRouteAfi_Object = MibTableColumn
usdBgpNewRouteAfi = _UsdBgpNewRouteAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 2),
    _UsdBgpNewRouteAfi_Type()
)
usdBgpNewRouteAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteAfi.setStatus("current")
_UsdBgpNewRouteSafi_Type = UsdBgpSafi
_UsdBgpNewRouteSafi_Object = MibTableColumn
usdBgpNewRouteSafi = _UsdBgpNewRouteSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 3),
    _UsdBgpNewRouteSafi_Type()
)
usdBgpNewRouteSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteSafi.setStatus("current")
_UsdBgpNewRouteIpAddrPrefix_Type = IpAddress
_UsdBgpNewRouteIpAddrPrefix_Object = MibTableColumn
usdBgpNewRouteIpAddrPrefix = _UsdBgpNewRouteIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 4),
    _UsdBgpNewRouteIpAddrPrefix_Type()
)
usdBgpNewRouteIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteIpAddrPrefix.setStatus("current")


class _UsdBgpNewRouteIpAddrPrefixLen_Type(Integer32):
    """Custom type usdBgpNewRouteIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_UsdBgpNewRouteIpAddrPrefixLen_Type.__name__ = "Integer32"
_UsdBgpNewRouteIpAddrPrefixLen_Object = MibTableColumn
usdBgpNewRouteIpAddrPrefixLen = _UsdBgpNewRouteIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 5),
    _UsdBgpNewRouteIpAddrPrefixLen_Type()
)
usdBgpNewRouteIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteIpAddrPrefixLen.setStatus("current")


class _UsdBgpNewRouteDistinguisher_Type(OctetString):
    """Custom type usdBgpNewRouteDistinguisher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdBgpNewRouteDistinguisher_Type.__name__ = "OctetString"
_UsdBgpNewRouteDistinguisher_Object = MibTableColumn
usdBgpNewRouteDistinguisher = _UsdBgpNewRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 6),
    _UsdBgpNewRouteDistinguisher_Type()
)
usdBgpNewRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteDistinguisher.setStatus("current")
_UsdBgpNewRoutePeer_Type = IpAddress
_UsdBgpNewRoutePeer_Object = MibTableColumn
usdBgpNewRoutePeer = _UsdBgpNewRoutePeer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 7),
    _UsdBgpNewRoutePeer_Type()
)
usdBgpNewRoutePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRoutePeer.setStatus("current")


class _UsdBgpNewRouteRouteType_Type(Integer32):
    """Custom type usdBgpNewRouteRouteType based on Integer32"""
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
        *(("routeTypeAggregate", 4),
          ("routeTypeAutoSummary", 5),
          ("routeTypeNetwork", 2),
          ("routeTypeReceived", 1),
          ("routeTypeRedistributed", 3))
    )


_UsdBgpNewRouteRouteType_Type.__name__ = "Integer32"
_UsdBgpNewRouteRouteType_Object = MibTableColumn
usdBgpNewRouteRouteType = _UsdBgpNewRouteRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 8),
    _UsdBgpNewRouteRouteType_Type()
)
usdBgpNewRouteRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteRouteType.setStatus("current")


class _UsdBgpNewRouteOriginalRd_Type(OctetString):
    """Custom type usdBgpNewRouteOriginalRd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdBgpNewRouteOriginalRd_Type.__name__ = "OctetString"
_UsdBgpNewRouteOriginalRd_Object = MibTableColumn
usdBgpNewRouteOriginalRd = _UsdBgpNewRouteOriginalRd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 9),
    _UsdBgpNewRouteOriginalRd_Type()
)
usdBgpNewRouteOriginalRd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdBgpNewRouteOriginalRd.setStatus("current")
_UsdBgpNewRouteOriginatorId_Type = IpAddress
_UsdBgpNewRouteOriginatorId_Object = MibTableColumn
usdBgpNewRouteOriginatorId = _UsdBgpNewRouteOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 10),
    _UsdBgpNewRouteOriginatorId_Type()
)
usdBgpNewRouteOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteOriginatorId.setStatus("current")
_UsdBgpNewRouteAtomicAggregatePresent_Type = TruthValue
_UsdBgpNewRouteAtomicAggregatePresent_Object = MibTableColumn
usdBgpNewRouteAtomicAggregatePresent = _UsdBgpNewRouteAtomicAggregatePresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 11),
    _UsdBgpNewRouteAtomicAggregatePresent_Type()
)
usdBgpNewRouteAtomicAggregatePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteAtomicAggregatePresent.setStatus("current")
_UsdBgpNewRouteMedPresent_Type = TruthValue
_UsdBgpNewRouteMedPresent_Object = MibTableColumn
usdBgpNewRouteMedPresent = _UsdBgpNewRouteMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 12),
    _UsdBgpNewRouteMedPresent_Type()
)
usdBgpNewRouteMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteMedPresent.setStatus("current")
_UsdBgpNewRouteLocalPrefPresent_Type = TruthValue
_UsdBgpNewRouteLocalPrefPresent_Object = MibTableColumn
usdBgpNewRouteLocalPrefPresent = _UsdBgpNewRouteLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 13),
    _UsdBgpNewRouteLocalPrefPresent_Type()
)
usdBgpNewRouteLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteLocalPrefPresent.setStatus("current")
_UsdBgpNewRouteAggregatorPresent_Type = TruthValue
_UsdBgpNewRouteAggregatorPresent_Object = MibTableColumn
usdBgpNewRouteAggregatorPresent = _UsdBgpNewRouteAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 14),
    _UsdBgpNewRouteAggregatorPresent_Type()
)
usdBgpNewRouteAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteAggregatorPresent.setStatus("current")
_UsdBgpNewRouteCommunitiesPresent_Type = TruthValue
_UsdBgpNewRouteCommunitiesPresent_Object = MibTableColumn
usdBgpNewRouteCommunitiesPresent = _UsdBgpNewRouteCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 15),
    _UsdBgpNewRouteCommunitiesPresent_Type()
)
usdBgpNewRouteCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteCommunitiesPresent.setStatus("current")
_UsdBgpNewRouteOriginatorIdPresent_Type = TruthValue
_UsdBgpNewRouteOriginatorIdPresent_Object = MibTableColumn
usdBgpNewRouteOriginatorIdPresent = _UsdBgpNewRouteOriginatorIdPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 16),
    _UsdBgpNewRouteOriginatorIdPresent_Type()
)
usdBgpNewRouteOriginatorIdPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteOriginatorIdPresent.setStatus("current")
_UsdBgpNewRouteClusterListPresent_Type = TruthValue
_UsdBgpNewRouteClusterListPresent_Object = MibTableColumn
usdBgpNewRouteClusterListPresent = _UsdBgpNewRouteClusterListPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 17),
    _UsdBgpNewRouteClusterListPresent_Type()
)
usdBgpNewRouteClusterListPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteClusterListPresent.setStatus("current")
_UsdBgpNewRouteWeight_Type = Unsigned32
_UsdBgpNewRouteWeight_Object = MibTableColumn
usdBgpNewRouteWeight = _UsdBgpNewRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 18),
    _UsdBgpNewRouteWeight_Type()
)
usdBgpNewRouteWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteWeight.setStatus("current")


class _UsdBgpNewRouteOrigin_Type(Integer32):
    """Custom type usdBgpNewRouteOrigin based on Integer32"""
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


_UsdBgpNewRouteOrigin_Type.__name__ = "Integer32"
_UsdBgpNewRouteOrigin_Object = MibTableColumn
usdBgpNewRouteOrigin = _UsdBgpNewRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 19),
    _UsdBgpNewRouteOrigin_Type()
)
usdBgpNewRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteOrigin.setStatus("current")


class _UsdBgpNewRouteASPathSegment_Type(OctetString):
    """Custom type usdBgpNewRouteASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_UsdBgpNewRouteASPathSegment_Type.__name__ = "OctetString"
_UsdBgpNewRouteASPathSegment_Object = MibTableColumn
usdBgpNewRouteASPathSegment = _UsdBgpNewRouteASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 20),
    _UsdBgpNewRouteASPathSegment_Type()
)
usdBgpNewRouteASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteASPathSegment.setStatus("current")
_UsdBgpNewRouteNextHop_Type = IpAddress
_UsdBgpNewRouteNextHop_Object = MibTableColumn
usdBgpNewRouteNextHop = _UsdBgpNewRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 21),
    _UsdBgpNewRouteNextHop_Type()
)
usdBgpNewRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteNextHop.setStatus("current")
_UsdBgpNewRouteMultiExitDisc_Type = Unsigned32
_UsdBgpNewRouteMultiExitDisc_Object = MibTableColumn
usdBgpNewRouteMultiExitDisc = _UsdBgpNewRouteMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 22),
    _UsdBgpNewRouteMultiExitDisc_Type()
)
usdBgpNewRouteMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteMultiExitDisc.setStatus("current")
_UsdBgpNewRouteLocalPref_Type = Unsigned32
_UsdBgpNewRouteLocalPref_Object = MibTableColumn
usdBgpNewRouteLocalPref = _UsdBgpNewRouteLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 23),
    _UsdBgpNewRouteLocalPref_Type()
)
usdBgpNewRouteLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteLocalPref.setStatus("current")


class _UsdBgpNewRouteAtomicAggregate_Type(Integer32):
    """Custom type usdBgpNewRouteAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_UsdBgpNewRouteAtomicAggregate_Type.__name__ = "Integer32"
_UsdBgpNewRouteAtomicAggregate_Object = MibTableColumn
usdBgpNewRouteAtomicAggregate = _UsdBgpNewRouteAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 24),
    _UsdBgpNewRouteAtomicAggregate_Type()
)
usdBgpNewRouteAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteAtomicAggregate.setStatus("current")


class _UsdBgpNewRouteAggregatorAS_Type(Integer32):
    """Custom type usdBgpNewRouteAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdBgpNewRouteAggregatorAS_Type.__name__ = "Integer32"
_UsdBgpNewRouteAggregatorAS_Object = MibTableColumn
usdBgpNewRouteAggregatorAS = _UsdBgpNewRouteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 25),
    _UsdBgpNewRouteAggregatorAS_Type()
)
usdBgpNewRouteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteAggregatorAS.setStatus("current")
_UsdBgpNewRouteAggregatorAddress_Type = IpAddress
_UsdBgpNewRouteAggregatorAddress_Object = MibTableColumn
usdBgpNewRouteAggregatorAddress = _UsdBgpNewRouteAggregatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 26),
    _UsdBgpNewRouteAggregatorAddress_Type()
)
usdBgpNewRouteAggregatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteAggregatorAddress.setStatus("current")
_UsdBgpNewRouteBestInIpRouteTable_Type = TruthValue
_UsdBgpNewRouteBestInIpRouteTable_Object = MibTableColumn
usdBgpNewRouteBestInIpRouteTable = _UsdBgpNewRouteBestInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 27),
    _UsdBgpNewRouteBestInIpRouteTable_Type()
)
usdBgpNewRouteBestInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteBestInIpRouteTable.setStatus("current")


class _UsdBgpNewRouteUnknown_Type(OctetString):
    """Custom type usdBgpNewRouteUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UsdBgpNewRouteUnknown_Type.__name__ = "OctetString"
_UsdBgpNewRouteUnknown_Object = MibTableColumn
usdBgpNewRouteUnknown = _UsdBgpNewRouteUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 28),
    _UsdBgpNewRouteUnknown_Type()
)
usdBgpNewRouteUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteUnknown.setStatus("current")
_UsdBgpNewRouteExtendedCommunitiesPresent_Type = TruthValue
_UsdBgpNewRouteExtendedCommunitiesPresent_Object = MibTableColumn
usdBgpNewRouteExtendedCommunitiesPresent = _UsdBgpNewRouteExtendedCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 29),
    _UsdBgpNewRouteExtendedCommunitiesPresent_Type()
)
usdBgpNewRouteExtendedCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteExtendedCommunitiesPresent.setStatus("current")
_UsdBgpNewRouteValid_Type = TruthValue
_UsdBgpNewRouteValid_Object = MibTableColumn
usdBgpNewRouteValid = _UsdBgpNewRouteValid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 30),
    _UsdBgpNewRouteValid_Type()
)
usdBgpNewRouteValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteValid.setStatus("current")


class _UsdBgpNewRouteSuppressedBy_Type(Integer32):
    """Custom type usdBgpNewRouteSuppressedBy based on Integer32"""
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
        *(("suppressedByAggregate", 2),
          ("suppressedByAutoSummary", 3),
          ("suppressedByDampening", 4),
          ("suppressedByNothing", 1))
    )


_UsdBgpNewRouteSuppressedBy_Type.__name__ = "Integer32"
_UsdBgpNewRouteSuppressedBy_Object = MibTableColumn
usdBgpNewRouteSuppressedBy = _UsdBgpNewRouteSuppressedBy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 31),
    _UsdBgpNewRouteSuppressedBy_Type()
)
usdBgpNewRouteSuppressedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteSuppressedBy.setStatus("current")
_UsdBgpNewRouteNextHopReachable_Type = TruthValue
_UsdBgpNewRouteNextHopReachable_Object = MibTableColumn
usdBgpNewRouteNextHopReachable = _UsdBgpNewRouteNextHopReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 32),
    _UsdBgpNewRouteNextHopReachable_Type()
)
usdBgpNewRouteNextHopReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteNextHopReachable.setStatus("current")
_UsdBgpNewRouteSynchronizedWithIgp_Type = TruthValue
_UsdBgpNewRouteSynchronizedWithIgp_Object = MibTableColumn
usdBgpNewRouteSynchronizedWithIgp = _UsdBgpNewRouteSynchronizedWithIgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 33),
    _UsdBgpNewRouteSynchronizedWithIgp_Type()
)
usdBgpNewRouteSynchronizedWithIgp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteSynchronizedWithIgp.setStatus("current")
_UsdBgpNewRoutePlaceInIpRouteTable_Type = TruthValue
_UsdBgpNewRoutePlaceInIpRouteTable_Object = MibTableColumn
usdBgpNewRoutePlaceInIpRouteTable = _UsdBgpNewRoutePlaceInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 34),
    _UsdBgpNewRoutePlaceInIpRouteTable_Type()
)
usdBgpNewRoutePlaceInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRoutePlaceInIpRouteTable.setStatus("current")
_UsdBgpNewRouteAdvertiseToExternalPeers_Type = TruthValue
_UsdBgpNewRouteAdvertiseToExternalPeers_Object = MibTableColumn
usdBgpNewRouteAdvertiseToExternalPeers = _UsdBgpNewRouteAdvertiseToExternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 35),
    _UsdBgpNewRouteAdvertiseToExternalPeers_Type()
)
usdBgpNewRouteAdvertiseToExternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteAdvertiseToExternalPeers.setStatus("current")
_UsdBgpNewRouteAdvertiseToInternalPeers_Type = TruthValue
_UsdBgpNewRouteAdvertiseToInternalPeers_Object = MibTableColumn
usdBgpNewRouteAdvertiseToInternalPeers = _UsdBgpNewRouteAdvertiseToInternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 36),
    _UsdBgpNewRouteAdvertiseToInternalPeers_Type()
)
usdBgpNewRouteAdvertiseToInternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteAdvertiseToInternalPeers.setStatus("current")
_UsdBgpNewRouteMplsLabel_Type = Unsigned32
_UsdBgpNewRouteMplsLabel_Object = MibTableColumn
usdBgpNewRouteMplsLabel = _UsdBgpNewRouteMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 37),
    _UsdBgpNewRouteMplsLabel_Type()
)
usdBgpNewRouteMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteMplsLabel.setStatus("current")
_UsdBgpNewRouteNextHopMetric_Type = Unsigned32
_UsdBgpNewRouteNextHopMetric_Object = MibTableColumn
usdBgpNewRouteNextHopMetric = _UsdBgpNewRouteNextHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 38),
    _UsdBgpNewRouteNextHopMetric_Type()
)
usdBgpNewRouteNextHopMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteNextHopMetric.setStatus("current")
_UsdBgpNewRouteFlapHistoryTable_Object = MibTable
usdBgpNewRouteFlapHistoryTable = _UsdBgpNewRouteFlapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24)
)
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapHistoryTable.setStatus("current")
_UsdBgpNewRouteFlapHistoryEntry_Object = MibTableRow
usdBgpNewRouteFlapHistoryEntry = _UsdBgpNewRouteFlapHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1)
)
usdBgpNewRouteFlapHistoryEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteOriginalRd"),
)
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapHistoryEntry.setStatus("current")


class _UsdBgpNewRouteFlapState_Type(Integer32):
    """Custom type usdBgpNewRouteFlapState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateAvailable", 1),
          ("stateSuppressedReachable", 2),
          ("stateSuppressedUnreachable", 3))
    )


_UsdBgpNewRouteFlapState_Type.__name__ = "Integer32"
_UsdBgpNewRouteFlapState_Object = MibTableColumn
usdBgpNewRouteFlapState = _UsdBgpNewRouteFlapState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 1),
    _UsdBgpNewRouteFlapState_Type()
)
usdBgpNewRouteFlapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapState.setStatus("current")
_UsdBgpNewRouteFlapFigureOfMerit_Type = Unsigned32
_UsdBgpNewRouteFlapFigureOfMerit_Object = MibTableColumn
usdBgpNewRouteFlapFigureOfMerit = _UsdBgpNewRouteFlapFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 2),
    _UsdBgpNewRouteFlapFigureOfMerit_Type()
)
usdBgpNewRouteFlapFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapFigureOfMerit.setStatus("current")
_UsdBgpNewRouteFlapRemainingTime_Type = Unsigned32
_UsdBgpNewRouteFlapRemainingTime_Object = MibTableColumn
usdBgpNewRouteFlapRemainingTime = _UsdBgpNewRouteFlapRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 3),
    _UsdBgpNewRouteFlapRemainingTime_Type()
)
usdBgpNewRouteFlapRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapRemainingTime.setUnits("seconds")
_UsdBgpNewRouteFlapSuppressThreshold_Type = Unsigned32
_UsdBgpNewRouteFlapSuppressThreshold_Object = MibTableColumn
usdBgpNewRouteFlapSuppressThreshold = _UsdBgpNewRouteFlapSuppressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 4),
    _UsdBgpNewRouteFlapSuppressThreshold_Type()
)
usdBgpNewRouteFlapSuppressThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapSuppressThreshold.setStatus("current")
_UsdBgpNewRouteFlapReuseThreshold_Type = Unsigned32
_UsdBgpNewRouteFlapReuseThreshold_Object = MibTableColumn
usdBgpNewRouteFlapReuseThreshold = _UsdBgpNewRouteFlapReuseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 5),
    _UsdBgpNewRouteFlapReuseThreshold_Type()
)
usdBgpNewRouteFlapReuseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapReuseThreshold.setStatus("current")
_UsdBgpNewRouteFlapMaxHoldDownTime_Type = Unsigned32
_UsdBgpNewRouteFlapMaxHoldDownTime_Object = MibTableColumn
usdBgpNewRouteFlapMaxHoldDownTime = _UsdBgpNewRouteFlapMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 6),
    _UsdBgpNewRouteFlapMaxHoldDownTime_Type()
)
usdBgpNewRouteFlapMaxHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapMaxHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapMaxHoldDownTime.setUnits("seconds")
_UsdBgpNewRouteFlapHalfLifeReachable_Type = Unsigned32
_UsdBgpNewRouteFlapHalfLifeReachable_Object = MibTableColumn
usdBgpNewRouteFlapHalfLifeReachable = _UsdBgpNewRouteFlapHalfLifeReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 7),
    _UsdBgpNewRouteFlapHalfLifeReachable_Type()
)
usdBgpNewRouteFlapHalfLifeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapHalfLifeReachable.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapHalfLifeReachable.setUnits("seconds")
_UsdBgpNewRouteFlapHalfLifeUnreachable_Type = Unsigned32
_UsdBgpNewRouteFlapHalfLifeUnreachable_Object = MibTableColumn
usdBgpNewRouteFlapHalfLifeUnreachable = _UsdBgpNewRouteFlapHalfLifeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 8),
    _UsdBgpNewRouteFlapHalfLifeUnreachable_Type()
)
usdBgpNewRouteFlapHalfLifeUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapHalfLifeUnreachable.setStatus("current")
if mibBuilder.loadTexts:
    usdBgpNewRouteFlapHalfLifeUnreachable.setUnits("seconds")
_UsdBgpNewRouteCommunityTable_Object = MibTable
usdBgpNewRouteCommunityTable = _UsdBgpNewRouteCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 25)
)
if mibBuilder.loadTexts:
    usdBgpNewRouteCommunityTable.setStatus("current")
_UsdBgpNewRouteCommunityEntry_Object = MibTableRow
usdBgpNewRouteCommunityEntry = _UsdBgpNewRouteCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 25, 1)
)
usdBgpNewRouteCommunityEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteOriginalRd"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteCommunityNumber"),
)
if mibBuilder.loadTexts:
    usdBgpNewRouteCommunityEntry.setStatus("current")
_UsdBgpNewRouteCommunityNumber_Type = Unsigned32
_UsdBgpNewRouteCommunityNumber_Object = MibTableColumn
usdBgpNewRouteCommunityNumber = _UsdBgpNewRouteCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 25, 1, 1),
    _UsdBgpNewRouteCommunityNumber_Type()
)
usdBgpNewRouteCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteCommunityNumber.setStatus("current")
_UsdBgpNewRouteExtendedCommunityTable_Object = MibTable
usdBgpNewRouteExtendedCommunityTable = _UsdBgpNewRouteExtendedCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 26)
)
if mibBuilder.loadTexts:
    usdBgpNewRouteExtendedCommunityTable.setStatus("current")
_UsdBgpNewRouteExtendedCommunityEntry_Object = MibTableRow
usdBgpNewRouteExtendedCommunityEntry = _UsdBgpNewRouteExtendedCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 26, 1)
)
usdBgpNewRouteExtendedCommunityEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteOriginalRd"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteExtendedCommunityNumber"),
)
if mibBuilder.loadTexts:
    usdBgpNewRouteExtendedCommunityEntry.setStatus("current")


class _UsdBgpNewRouteExtendedCommunityNumber_Type(OctetString):
    """Custom type usdBgpNewRouteExtendedCommunityNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_UsdBgpNewRouteExtendedCommunityNumber_Type.__name__ = "OctetString"
_UsdBgpNewRouteExtendedCommunityNumber_Object = MibTableColumn
usdBgpNewRouteExtendedCommunityNumber = _UsdBgpNewRouteExtendedCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 26, 1, 1),
    _UsdBgpNewRouteExtendedCommunityNumber_Type()
)
usdBgpNewRouteExtendedCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteExtendedCommunityNumber.setStatus("current")
_UsdBgpNewRouteClusterIdTable_Object = MibTable
usdBgpNewRouteClusterIdTable = _UsdBgpNewRouteClusterIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 27)
)
if mibBuilder.loadTexts:
    usdBgpNewRouteClusterIdTable.setStatus("current")
_UsdBgpNewRouteClusterIdEntry_Object = MibTableRow
usdBgpNewRouteClusterIdEntry = _UsdBgpNewRouteClusterIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 27, 1)
)
usdBgpNewRouteClusterIdEntry.setIndexNames(
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteVrfName"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteAfi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteSafi"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefix"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteIpAddrPrefixLen"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteDistinguisher"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRoutePeer"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteRouteType"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteOriginalRd"),
    (0, "Unisphere-Data-BGP-MIB", "usdBgpNewRouteClusterId"),
)
if mibBuilder.loadTexts:
    usdBgpNewRouteClusterIdEntry.setStatus("current")
_UsdBgpNewRouteClusterId_Type = Unsigned32
_UsdBgpNewRouteClusterId_Object = MibTableColumn
usdBgpNewRouteClusterId = _UsdBgpNewRouteClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 27, 1, 1),
    _UsdBgpNewRouteClusterId_Type()
)
usdBgpNewRouteClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdBgpNewRouteClusterId.setStatus("current")
_UsdBgpConformance_ObjectIdentity = ObjectIdentity
usdBgpConformance = _UsdBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2)
)
_UsdBgpCompliances_ObjectIdentity = ObjectIdentity
usdBgpCompliances = _UsdBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1)
)
_UsdBgpConfGroups_ObjectIdentity = ObjectIdentity
usdBgpConfGroups = _UsdBgpConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2)
)

# Managed Objects groups

usdBgpGeneralConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 1)
)
usdBgpGeneralConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpLocalAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEnabled"),
        ("Unisphere-Data-BGP-MIB", "usdBgpIdentifier"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAlwaysCompareMed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpDefaultLocalPreference"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEqualCostLimit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpClientToClientReflection"),
        ("Unisphere-Data-BGP-MIB", "usdBgpClusterId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpConfederationId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpMissingAsWorst"),
        ("Unisphere-Data-BGP-MIB", "usdBgpResetAllConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAdvertiseInactive"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEnforceFirstAs"),
        ("Unisphere-Data-BGP-MIB", "usdBgpConfedCompareMed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpExternalAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalRibOutEnabled"),
        ("Unisphere-Data-BGP-MIB", "usdBgpOverloadShutdown"),
        ("Unisphere-Data-BGP-MIB", "usdBgpLogNeighborChanges"),
        ("Unisphere-Data-BGP-MIB", "usdBgpFastExternalFallover"),
        ("Unisphere-Data-BGP-MIB", "usdBgpInternalAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpMaxAsLimit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPreviousOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAutomaticRouteTargetFilter"))
)
if mibBuilder.loadTexts:
    usdBgpGeneralConfGroup.setStatus("obsolete")

usdBgpStatisticsConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 2)
)
usdBgpStatisticsConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpBaselineTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpDestinationCount"),
        ("Unisphere-Data-BGP-MIB", "usdBgpDestinationMemoryUsed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteCount"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteMemoryUsed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpSelectedRouteCount"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPathAttributeCount"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPathAttributeMemoryUsed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapHistoryCount"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapHistoryMemoryUsed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpSuppressedRouteCount"))
)
if mibBuilder.loadTexts:
    usdBgpStatisticsConfGroup.setStatus("current")

usdBgpConfederationPeerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 3)
)
usdBgpConfederationPeerConfGroup.setObjects(
    ("Unisphere-Data-BGP-MIB", "usdBgpConfederationPeerRowStatus")
)
if mibBuilder.loadTexts:
    usdBgpConfederationPeerConfGroup.setStatus("current")

usdBgpPeerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 4)
)
usdBgpPeerConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerAdminStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerNegotiatedVersion"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAddress"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAddressMask"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalPort"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemoteAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemotePort"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInUpdates"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerOutUpdates"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInTotalMessages"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerOutTotalMessages"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLastErrorCode"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLastResetReason"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerFsmEstablishedTransitions"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerFsmEstablishedTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInUpdateElapsedTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerDescription"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemoteIdentifier"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerEbgpMultihop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerEbgpMultihopTtl"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerUpdateSource"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerMd5Password"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerMaxUpdateSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerSupportsCapabilityNegotiation"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityMultiProtocol"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityRouteRefresh"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityRouteRefreshCiscoProprietary"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRowStatus"))
)
if mibBuilder.loadTexts:
    usdBgpPeerConfGroup.setStatus("obsolete")

usdBgpAfiSafiPeerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 5)
)
usdBgpAfiSafiPeerConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerProposedAfiSafiPeerRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpLocalProposedAfiSafiPeerRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpExchangedAfiSafiPeerRowStatus"))
)
if mibBuilder.loadTexts:
    usdBgpAfiSafiPeerConfGroup.setStatus("current")

usdBgpPeerAddressFamilyConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 6)
)
usdBgpPeerAddressFamilyConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPeerGroup"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyDefaultOriginate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyNextHopSelf"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilySendCommunity"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyDistributeListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyDistributeListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixTreeIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixTreeOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListWeightValue"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteMapIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteMapOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteReflectorClient"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteLimitWarn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteLimitReset"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRemovePrivateAs"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyUnsuppressMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyAsOverride"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyAllowAsIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilySendExtendedCommunity"))
)
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyConfGroup.setStatus("obsolete")

usdBgpPeerGroupConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 7)
)
usdBgpPeerGroupConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAdminStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRemoteAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupDescription"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupEbgpMultihop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupEbgpMultihopTtl"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupUpdateSource"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupMd5Password"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupMaxUpdateSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRowStatus"))
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupConfGroup.setStatus("obsolete")

usdBgpPeerGroupAddressFamilyConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 8)
)
usdBgpPeerGroupAddressFamilyConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilySendCommunity"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyAsOverride"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilySendExtendedCommunity"))
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyConfGroup.setStatus("obsolete")

usdBgpRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 9)
)
usdBgpRouteConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapFigureOfMerit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapRemainingTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapSuppressThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapReuseThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapMaxHoldDownTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapHalfLifeReachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteFlapHalfLifeUnreachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteOriginatorId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteAtomicAggregatePresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteMedPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteLocalPrefPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteAggregatorPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteCommunitiesPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteOriginatorIdPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteClusterListPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteOrigin"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteASPathSegment"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteNextHop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteMultiExitDisc"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteLocalPref"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteAtomicAggregate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteAggregatorAS"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteAggregatorAddress"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteBestInIpRouteTable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteUnknown"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteExtendedCommunitiesPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteValid"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteSuppressedBy"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteNextHopReachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteSynchronizedWithIgp"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRoutePlaceInIpRouteTable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteAdvertiseToExternalPeers"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteAdvertiseToInternalPeers"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteDistinguisher"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteMplsLabel"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteNextHopMetric"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteCommunityNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteExtendedCommunityNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRouteClusterId"))
)
if mibBuilder.loadTexts:
    usdBgpRouteConfGroup.setStatus("obsolete")

usdBgpNetworkConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 10)
)
usdBgpNetworkConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpNetworkBackdoor"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkWeightSpecified"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkRouteMap"))
)
if mibBuilder.loadTexts:
    usdBgpNetworkConfGroup.setStatus("obsolete")

usdBgpAggregateConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 11)
)
usdBgpAggregateConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpAggregateAsSet"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateSummaryOnly"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateAttributeMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateAdvertiseMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateSuppressMap"))
)
if mibBuilder.loadTexts:
    usdBgpAggregateConfGroup.setStatus("obsolete")

usdBgpVrfConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 12)
)
usdBgpVrfConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpVrfSynchronization"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfAutoSummary"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfExternalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfInternalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfLocalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfOperationalState"))
)
if mibBuilder.loadTexts:
    usdBgpVrfConfGroup.setStatus("obsolete")

usdBgpAddressFamilyConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 13)
)
usdBgpAddressFamilyConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDefaultOriginate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyRouteFlapDampening"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningSuppressThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningReuseThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningRouteMapName"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyOperationalState"))
)
if mibBuilder.loadTexts:
    usdBgpAddressFamilyConfGroup.setStatus("obsolete")

usdBgpStorageConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 14)
)
usdBgpStorageConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialHeapSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxHeapSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialVrfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxVrfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAddressFamilyPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAddressFamilyPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerGroupPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerGroupPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerGroupAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerGroupAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialNetworkPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxNetworkPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAggregatePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAggregatePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialDestinationPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxDestinationPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAttributesPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAttributesPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRouteFlapHistoryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRouteFlapHistoryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialNetworkRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxNetworkRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRedistributedRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRedistributedRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAggregateRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAggregateRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAutoSummaryRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAutoSummaryRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialHistoryRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxHistoryRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialSendQueueEntryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxSendQueueEntryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialVpnRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxVpnRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRouteTargetPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRouteTargetPoolSize"))
)
if mibBuilder.loadTexts:
    usdBgpStorageConfGroup.setStatus("obsolete")

usdBgpGeneralConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 15)
)
usdBgpGeneralConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpLocalAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEnabled"),
        ("Unisphere-Data-BGP-MIB", "usdBgpIdentifier"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAlwaysCompareMed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpDefaultLocalPreference"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEqualCostLimit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpClientToClientReflection"),
        ("Unisphere-Data-BGP-MIB", "usdBgpClusterId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpConfederationId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpMissingAsWorst"),
        ("Unisphere-Data-BGP-MIB", "usdBgpResetAllConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAdvertiseInactive"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEnforceFirstAs"),
        ("Unisphere-Data-BGP-MIB", "usdBgpConfedCompareMed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpExternalAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalRibOutEnabled"),
        ("Unisphere-Data-BGP-MIB", "usdBgpOverloadShutdown"),
        ("Unisphere-Data-BGP-MIB", "usdBgpLogNeighborChanges"),
        ("Unisphere-Data-BGP-MIB", "usdBgpFastExternalFallover"),
        ("Unisphere-Data-BGP-MIB", "usdBgpInternalAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpMaxAsLimit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPreviousOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAutomaticRouteTargetFilter"),
        ("Unisphere-Data-BGP-MIB", "usdBgpDefaultIPv4Unicast"))
)
if mibBuilder.loadTexts:
    usdBgpGeneralConfGroup2.setStatus("obsolete")

usdBgpNewRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 16)
)
usdBgpNewRouteConfGroup.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpNewRouteOriginatorId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteAtomicAggregatePresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteMedPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteLocalPrefPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteAggregatorPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteCommunitiesPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteOriginatorIdPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteClusterListPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteOrigin"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteASPathSegment"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteNextHop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteMultiExitDisc"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteLocalPref"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteAtomicAggregate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteAggregatorAS"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteAggregatorAddress"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteBestInIpRouteTable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteUnknown"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteExtendedCommunitiesPresent"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteValid"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteSuppressedBy"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteNextHopReachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteSynchronizedWithIgp"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRoutePlaceInIpRouteTable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteAdvertiseToExternalPeers"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteAdvertiseToInternalPeers"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteMplsLabel"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteNextHopMetric"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapFigureOfMerit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapRemainingTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapSuppressThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapReuseThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapMaxHoldDownTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapHalfLifeReachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteFlapHalfLifeUnreachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteCommunityNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteExtendedCommunityNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNewRouteClusterId"))
)
if mibBuilder.loadTexts:
    usdBgpNewRouteConfGroup.setStatus("current")

usdBgpPeerConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 17)
)
usdBgpPeerConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerAdminStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerNegotiatedVersion"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAddress"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAddressMask"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalPort"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemoteAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemotePort"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInUpdates"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerOutUpdates"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInTotalMessages"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerOutTotalMessages"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLastErrorCode"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLastResetReason"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerFsmEstablishedTransitions"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerFsmEstablishedTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInUpdateElapsedTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerDescription"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemoteIdentifier"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerEbgpMultihop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerEbgpMultihopTtl"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerUpdateSource"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerMd5Password"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerMaxUpdateSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerSupportsCapabilityNegotiation"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityMultiProtocol"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityRouteRefresh"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityRouteRefreshCiscoProprietary"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAsNumber"))
)
if mibBuilder.loadTexts:
    usdBgpPeerConfGroup2.setStatus("obsolete")

usdBgpPeerGroupConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 18)
)
usdBgpPeerGroupConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAdminStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRemoteAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupDescription"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupEbgpMultihop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupEbgpMultihopTtl"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupUpdateSource"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupMd5Password"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupMaxUpdateSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupLocalAsNumber"))
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupConfGroup2.setStatus("obsolete")

usdBgpVrfConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 19)
)
usdBgpVrfConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpVrfSynchronization"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfAutoSummary"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfExternalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfInternalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfLocalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfAddUnicastRoutesToMulticastView"))
)
if mibBuilder.loadTexts:
    usdBgpVrfConfGroup2.setStatus("obsolete")

usdBgpGeneralConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 20)
)
usdBgpGeneralConfGroup3.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpLocalAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEnabled"),
        ("Unisphere-Data-BGP-MIB", "usdBgpIdentifier"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAlwaysCompareMed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpDefaultLocalPreference"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEqualCostLimit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpClientToClientReflection"),
        ("Unisphere-Data-BGP-MIB", "usdBgpClusterId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpConfederationId"),
        ("Unisphere-Data-BGP-MIB", "usdBgpMissingAsWorst"),
        ("Unisphere-Data-BGP-MIB", "usdBgpResetAllConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAdvertiseInactive"),
        ("Unisphere-Data-BGP-MIB", "usdBgpEnforceFirstAs"),
        ("Unisphere-Data-BGP-MIB", "usdBgpConfedCompareMed"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpExternalAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpGlobalRibOutEnabled"),
        ("Unisphere-Data-BGP-MIB", "usdBgpOverloadShutdown"),
        ("Unisphere-Data-BGP-MIB", "usdBgpLogNeighborChanges"),
        ("Unisphere-Data-BGP-MIB", "usdBgpFastExternalFallover"),
        ("Unisphere-Data-BGP-MIB", "usdBgpInternalAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpMaxAsLimit"),
        ("Unisphere-Data-BGP-MIB", "usdBgpOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPreviousOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAutomaticRouteTargetFilter"),
        ("Unisphere-Data-BGP-MIB", "usdBgpDefaultIPv4Unicast"),
        ("Unisphere-Data-BGP-MIB", "usdBgpRedistributeInternal"),
        ("Unisphere-Data-BGP-MIB", "usdBgpUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpGeneralConfGroup3.setStatus("current")

usdBgpStorageConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 21)
)
usdBgpStorageConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialHeapSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxHeapSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialVrfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxVrfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAddressFamilyPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAddressFamilyPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerGroupPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerGroupPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialPeerGroupAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxPeerGroupAfPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialNetworkPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxNetworkPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAggregatePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAggregatePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialDestinationPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxDestinationPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAttributesPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAttributesPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRouteFlapHistoryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRouteFlapHistoryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialNetworkRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxNetworkRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRedistributedRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRedistributedRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAggregateRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAggregateRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialAutoSummaryRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxAutoSummaryRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialSendQueueEntryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxSendQueueEntryPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialVpnRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxVpnRoutePoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageInitialRouteTargetPoolSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpStorageMaxRouteTargetPoolSize"))
)
if mibBuilder.loadTexts:
    usdBgpStorageConfGroup2.setStatus("current")

usdBgpPeerConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 22)
)
usdBgpPeerConfGroup3.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerAdminStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerNegotiatedVersion"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAddress"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAddressMask"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalPort"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemoteAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemotePort"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInUpdates"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerOutUpdates"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInTotalMessages"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerOutTotalMessages"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLastErrorCode"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLastResetReason"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerFsmEstablishedTransitions"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerFsmEstablishedTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerInUpdateElapsedTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerDescription"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRemoteIdentifier"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerEbgpMultihop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerEbgpMultihopTtl"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerUpdateSource"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerMd5Password"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerMaxUpdateSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerSupportsCapabilityNegotiation"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityMultiProtocol"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityRouteRefresh"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerCapabilityRouteRefreshCiscoProprietary"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerLocalAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpPeerConfGroup3.setStatus("current")

usdBgpPeerAddressFamilyConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 23)
)
usdBgpPeerAddressFamilyConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPeerGroup"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyDefaultOriginate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyNextHopSelf"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilySendCommunity"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyDistributeListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyDistributeListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixTreeIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyPrefixTreeOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyFilterListWeightValue"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteMapIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteMapOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteReflectorClient"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteLimitWarn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteLimitReset"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRemovePrivateAs"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyUnsuppressMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyAsOverride"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyAllowAsIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilySendExtendedCommunity"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpPeerAddressFamilyConfGroup2.setStatus("current")

usdBgpPeerGroupConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 24)
)
usdBgpPeerGroupConfGroup3.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAdminStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRemoteAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRetryInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupConfigHoldTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupConfigKeepAliveInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAsOriginationInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAdvertisementInterval"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupDescription"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupEbgpMultihop"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupEbgpMultihopTtl"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupUpdateSource"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupMd5Password"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupMaxUpdateSize"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupLocalAsNumber"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupConfGroup3.setStatus("current")

usdBgpPeerGroupAddressFamilyConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 25)
)
usdBgpPeerGroupAddressFamilyConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilySendCommunity"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyAsOverride"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilySendExtendedCommunity"),
        ("Unisphere-Data-BGP-MIB", "usdBgpPeerGroupAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpPeerGroupAddressFamilyConfGroup2.setStatus("current")

usdBgpNetworkConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 26)
)
usdBgpNetworkConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpNetworkBackdoor"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkWeightSpecified"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkWeight"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkRouteMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpNetworkUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpNetworkConfGroup2.setStatus("current")

usdBgpAggregateConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 27)
)
usdBgpAggregateConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpAggregateAsSet"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateSummaryOnly"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateAttributeMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateAdvertiseMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateSuppressMap"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAggregateUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpAggregateConfGroup2.setStatus("current")

usdBgpVrfConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 28)
)
usdBgpVrfConfGroup3.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpVrfSynchronization"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfAutoSummary"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfExternalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfInternalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfLocalDistance"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfAddUnicastRoutesToMulticastView"),
        ("Unisphere-Data-BGP-MIB", "usdBgpVrfUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpVrfConfGroup3.setStatus("current")

usdBgpAddressFamilyConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 29)
)
usdBgpAddressFamilyConfGroup2.setObjects(
      *(("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDefaultOriginate"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyRouteFlapDampening"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningSuppressThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningReuseThreshold"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyDampeningRouteMapName"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyResetConnectionType"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyRowStatus"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyOperationalState"),
        ("Unisphere-Data-BGP-MIB", "usdBgpAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    usdBgpAddressFamilyConfGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdBgpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdBgpCompliance.setStatus(
        "obsolete"
    )

usdBgpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdBgpCompliance2.setStatus(
        "obsolete"
    )

usdBgpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 3)
)
if mibBuilder.loadTexts:
    usdBgpCompliance3.setStatus(
        "obsolete"
    )

usdBgpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 4)
)
if mibBuilder.loadTexts:
    usdBgpCompliance4.setStatus(
        "obsolete"
    )

usdBgpCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 5)
)
if mibBuilder.loadTexts:
    usdBgpCompliance5.setStatus(
        "obsolete"
    )

usdBgpCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 6)
)
if mibBuilder.loadTexts:
    usdBgpCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-BGP-MIB",
    **{"UsdBgpAfi": UsdBgpAfi,
       "UsdBgpSafi": UsdBgpSafi,
       "UsdBgpStorageInteger": UsdBgpStorageInteger,
       "UsdBgpResetConnectionType": UsdBgpResetConnectionType,
       "usdBgpMIB": usdBgpMIB,
       "usdBgpObjects": usdBgpObjects,
       "usdBgpGeneralGroup": usdBgpGeneralGroup,
       "usdBgpLocalAsNumber": usdBgpLocalAsNumber,
       "usdBgpEnabled": usdBgpEnabled,
       "usdBgpIdentifier": usdBgpIdentifier,
       "usdBgpAlwaysCompareMed": usdBgpAlwaysCompareMed,
       "usdBgpDefaultLocalPreference": usdBgpDefaultLocalPreference,
       "usdBgpEqualCostLimit": usdBgpEqualCostLimit,
       "usdBgpClientToClientReflection": usdBgpClientToClientReflection,
       "usdBgpClusterId": usdBgpClusterId,
       "usdBgpConfederationId": usdBgpConfederationId,
       "usdBgpMissingAsWorst": usdBgpMissingAsWorst,
       "usdBgpResetAllConnectionType": usdBgpResetAllConnectionType,
       "usdBgpAdvertiseInactive": usdBgpAdvertiseInactive,
       "usdBgpEnforceFirstAs": usdBgpEnforceFirstAs,
       "usdBgpConfedCompareMed": usdBgpConfedCompareMed,
       "usdBgpGlobalRetryInterval": usdBgpGlobalRetryInterval,
       "usdBgpGlobalConfigKeepAliveInterval": usdBgpGlobalConfigKeepAliveInterval,
       "usdBgpGlobalConfigHoldTime": usdBgpGlobalConfigHoldTime,
       "usdBgpGlobalAsOriginationInterval": usdBgpGlobalAsOriginationInterval,
       "usdBgpExternalAdvertisementInterval": usdBgpExternalAdvertisementInterval,
       "usdBgpGlobalRibOutEnabled": usdBgpGlobalRibOutEnabled,
       "usdBgpOverloadShutdown": usdBgpOverloadShutdown,
       "usdBgpLogNeighborChanges": usdBgpLogNeighborChanges,
       "usdBgpFastExternalFallover": usdBgpFastExternalFallover,
       "usdBgpInternalAdvertisementInterval": usdBgpInternalAdvertisementInterval,
       "usdBgpMaxAsLimit": usdBgpMaxAsLimit,
       "usdBgpOperationalState": usdBgpOperationalState,
       "usdBgpPreviousOperationalState": usdBgpPreviousOperationalState,
       "usdBgpAutomaticRouteTargetFilter": usdBgpAutomaticRouteTargetFilter,
       "usdBgpDefaultIPv4Unicast": usdBgpDefaultIPv4Unicast,
       "usdBgpRedistributeInternal": usdBgpRedistributeInternal,
       "usdBgpUnconfiguredAttributes": usdBgpUnconfiguredAttributes,
       "usdBgpRouteTableStatisticsGroup": usdBgpRouteTableStatisticsGroup,
       "usdBgpBaselineTime": usdBgpBaselineTime,
       "usdBgpDestinationCount": usdBgpDestinationCount,
       "usdBgpDestinationMemoryUsed": usdBgpDestinationMemoryUsed,
       "usdBgpRouteCount": usdBgpRouteCount,
       "usdBgpRouteMemoryUsed": usdBgpRouteMemoryUsed,
       "usdBgpSelectedRouteCount": usdBgpSelectedRouteCount,
       "usdBgpPathAttributeCount": usdBgpPathAttributeCount,
       "usdBgpPathAttributeMemoryUsed": usdBgpPathAttributeMemoryUsed,
       "usdBgpRouteFlapHistoryCount": usdBgpRouteFlapHistoryCount,
       "usdBgpRouteFlapHistoryMemoryUsed": usdBgpRouteFlapHistoryMemoryUsed,
       "usdBgpSuppressedRouteCount": usdBgpSuppressedRouteCount,
       "usdBgpConfederationPeerTable": usdBgpConfederationPeerTable,
       "usdBgpConfederationPeerEntry": usdBgpConfederationPeerEntry,
       "usdBgpConfederationPeerAsNumber": usdBgpConfederationPeerAsNumber,
       "usdBgpConfederationPeerRowStatus": usdBgpConfederationPeerRowStatus,
       "usdBgpPeerTable": usdBgpPeerTable,
       "usdBgpPeerEntry": usdBgpPeerEntry,
       "usdBgpPeerVrfName": usdBgpPeerVrfName,
       "usdBgpPeerRemoteAddress": usdBgpPeerRemoteAddress,
       "usdBgpPeerAdminStatus": usdBgpPeerAdminStatus,
       "usdBgpPeerState": usdBgpPeerState,
       "usdBgpPeerNegotiatedVersion": usdBgpPeerNegotiatedVersion,
       "usdBgpPeerLocalAddress": usdBgpPeerLocalAddress,
       "usdBgpPeerLocalAddressMask": usdBgpPeerLocalAddressMask,
       "usdBgpPeerLocalPort": usdBgpPeerLocalPort,
       "usdBgpPeerRemoteAsNumber": usdBgpPeerRemoteAsNumber,
       "usdBgpPeerRemotePort": usdBgpPeerRemotePort,
       "usdBgpPeerInUpdates": usdBgpPeerInUpdates,
       "usdBgpPeerOutUpdates": usdBgpPeerOutUpdates,
       "usdBgpPeerInTotalMessages": usdBgpPeerInTotalMessages,
       "usdBgpPeerOutTotalMessages": usdBgpPeerOutTotalMessages,
       "usdBgpPeerLastErrorCode": usdBgpPeerLastErrorCode,
       "usdBgpPeerLastResetReason": usdBgpPeerLastResetReason,
       "usdBgpPeerFsmEstablishedTransitions": usdBgpPeerFsmEstablishedTransitions,
       "usdBgpPeerFsmEstablishedTime": usdBgpPeerFsmEstablishedTime,
       "usdBgpPeerRetryInterval": usdBgpPeerRetryInterval,
       "usdBgpPeerHoldTime": usdBgpPeerHoldTime,
       "usdBgpPeerKeepAliveInterval": usdBgpPeerKeepAliveInterval,
       "usdBgpPeerConfigHoldTime": usdBgpPeerConfigHoldTime,
       "usdBgpPeerConfigKeepAliveInterval": usdBgpPeerConfigKeepAliveInterval,
       "usdBgpPeerAsOriginationInterval": usdBgpPeerAsOriginationInterval,
       "usdBgpPeerAdvertisementInterval": usdBgpPeerAdvertisementInterval,
       "usdBgpPeerInUpdateElapsedTime": usdBgpPeerInUpdateElapsedTime,
       "usdBgpPeerDescription": usdBgpPeerDescription,
       "usdBgpPeerRemoteIdentifier": usdBgpPeerRemoteIdentifier,
       "usdBgpPeerWeight": usdBgpPeerWeight,
       "usdBgpPeerEbgpMultihop": usdBgpPeerEbgpMultihop,
       "usdBgpPeerEbgpMultihopTtl": usdBgpPeerEbgpMultihopTtl,
       "usdBgpPeerUpdateSource": usdBgpPeerUpdateSource,
       "usdBgpPeerMd5Password": usdBgpPeerMd5Password,
       "usdBgpPeerMaxUpdateSize": usdBgpPeerMaxUpdateSize,
       "usdBgpPeerType": usdBgpPeerType,
       "usdBgpPeerSupportsCapabilityNegotiation": usdBgpPeerSupportsCapabilityNegotiation,
       "usdBgpPeerCapabilityMultiProtocol": usdBgpPeerCapabilityMultiProtocol,
       "usdBgpPeerCapabilityRouteRefresh": usdBgpPeerCapabilityRouteRefresh,
       "usdBgpPeerCapabilityRouteRefreshCiscoProprietary": usdBgpPeerCapabilityRouteRefreshCiscoProprietary,
       "usdBgpPeerResetConnectionType": usdBgpPeerResetConnectionType,
       "usdBgpPeerRowStatus": usdBgpPeerRowStatus,
       "usdBgpPeerLocalAsNumber": usdBgpPeerLocalAsNumber,
       "usdBgpPeerUnconfiguredAttributes": usdBgpPeerUnconfiguredAttributes,
       "usdBgpPeerProposedAfiSafiPeerTable": usdBgpPeerProposedAfiSafiPeerTable,
       "usdBgpPeerProposedAfiSafiPeerEntry": usdBgpPeerProposedAfiSafiPeerEntry,
       "usdBgpPeerProposedAfiSafiPeerVrfName": usdBgpPeerProposedAfiSafiPeerVrfName,
       "usdBgpPeerProposedAfiSafiPeerRemoteAddr": usdBgpPeerProposedAfiSafiPeerRemoteAddr,
       "usdBgpPeerProposedAfiSafiPeerAfi": usdBgpPeerProposedAfiSafiPeerAfi,
       "usdBgpPeerProposedAfiSafiPeerSafi": usdBgpPeerProposedAfiSafiPeerSafi,
       "usdBgpPeerProposedAfiSafiPeerRowStatus": usdBgpPeerProposedAfiSafiPeerRowStatus,
       "usdBgpLocalProposedAfiSafiPeerTable": usdBgpLocalProposedAfiSafiPeerTable,
       "usdBgpLocalProposedAfiSafiPeerEntry": usdBgpLocalProposedAfiSafiPeerEntry,
       "usdBgpLocalProposedAfiSafiPeerVrfName": usdBgpLocalProposedAfiSafiPeerVrfName,
       "usdBgpLocalProposedAfiSafiPeerRemoteAddr": usdBgpLocalProposedAfiSafiPeerRemoteAddr,
       "usdBgpLocalProposedAfiSafiPeerAfi": usdBgpLocalProposedAfiSafiPeerAfi,
       "usdBgpLocalProposedAfiSafiPeerSafi": usdBgpLocalProposedAfiSafiPeerSafi,
       "usdBgpLocalProposedAfiSafiPeerRowStatus": usdBgpLocalProposedAfiSafiPeerRowStatus,
       "usdBgpExchangedAfiSafiPeerTable": usdBgpExchangedAfiSafiPeerTable,
       "usdBgpExchangedAfiSafiPeerEntry": usdBgpExchangedAfiSafiPeerEntry,
       "usdBgpExchangedAfiSafiPeerVrfName": usdBgpExchangedAfiSafiPeerVrfName,
       "usdBgpExchangedAfiSafiPeerRemoteAddr": usdBgpExchangedAfiSafiPeerRemoteAddr,
       "usdBgpExchangedAfiSafiPeerAfi": usdBgpExchangedAfiSafiPeerAfi,
       "usdBgpExchangedAfiSafiPeerSafi": usdBgpExchangedAfiSafiPeerSafi,
       "usdBgpExchangedAfiSafiPeerRowStatus": usdBgpExchangedAfiSafiPeerRowStatus,
       "usdBgpPeerAddressFamilyTable": usdBgpPeerAddressFamilyTable,
       "usdBgpPeerAddressFamilyEntry": usdBgpPeerAddressFamilyEntry,
       "usdBgpPeerAddressFamilyVrfName": usdBgpPeerAddressFamilyVrfName,
       "usdBgpPeerAddressFamilyAfi": usdBgpPeerAddressFamilyAfi,
       "usdBgpPeerAddressFamilySafi": usdBgpPeerAddressFamilySafi,
       "usdBgpPeerAddressFamilyRemoteAddress": usdBgpPeerAddressFamilyRemoteAddress,
       "usdBgpPeerAddressFamilyPeerGroup": usdBgpPeerAddressFamilyPeerGroup,
       "usdBgpPeerAddressFamilyDefaultOriginate": usdBgpPeerAddressFamilyDefaultOriginate,
       "usdBgpPeerAddressFamilyNextHopSelf": usdBgpPeerAddressFamilyNextHopSelf,
       "usdBgpPeerAddressFamilySendCommunity": usdBgpPeerAddressFamilySendCommunity,
       "usdBgpPeerAddressFamilyDistributeListIn": usdBgpPeerAddressFamilyDistributeListIn,
       "usdBgpPeerAddressFamilyDistributeListOut": usdBgpPeerAddressFamilyDistributeListOut,
       "usdBgpPeerAddressFamilyPrefixListIn": usdBgpPeerAddressFamilyPrefixListIn,
       "usdBgpPeerAddressFamilyPrefixListOut": usdBgpPeerAddressFamilyPrefixListOut,
       "usdBgpPeerAddressFamilyPrefixTreeIn": usdBgpPeerAddressFamilyPrefixTreeIn,
       "usdBgpPeerAddressFamilyPrefixTreeOut": usdBgpPeerAddressFamilyPrefixTreeOut,
       "usdBgpPeerAddressFamilyFilterListIn": usdBgpPeerAddressFamilyFilterListIn,
       "usdBgpPeerAddressFamilyFilterListOut": usdBgpPeerAddressFamilyFilterListOut,
       "usdBgpPeerAddressFamilyFilterListWeight": usdBgpPeerAddressFamilyFilterListWeight,
       "usdBgpPeerAddressFamilyFilterListWeightValue": usdBgpPeerAddressFamilyFilterListWeightValue,
       "usdBgpPeerAddressFamilyRouteMapIn": usdBgpPeerAddressFamilyRouteMapIn,
       "usdBgpPeerAddressFamilyRouteMapOut": usdBgpPeerAddressFamilyRouteMapOut,
       "usdBgpPeerAddressFamilyRouteReflectorClient": usdBgpPeerAddressFamilyRouteReflectorClient,
       "usdBgpPeerAddressFamilyRouteLimitWarn": usdBgpPeerAddressFamilyRouteLimitWarn,
       "usdBgpPeerAddressFamilyRouteLimitReset": usdBgpPeerAddressFamilyRouteLimitReset,
       "usdBgpPeerAddressFamilyRouteLimitWarnOnly": usdBgpPeerAddressFamilyRouteLimitWarnOnly,
       "usdBgpPeerAddressFamilyRemovePrivateAs": usdBgpPeerAddressFamilyRemovePrivateAs,
       "usdBgpPeerAddressFamilyUnsuppressMap": usdBgpPeerAddressFamilyUnsuppressMap,
       "usdBgpPeerAddressFamilyInboundSoftReconfig": usdBgpPeerAddressFamilyInboundSoftReconfig,
       "usdBgpPeerAddressFamilyResetConnectionType": usdBgpPeerAddressFamilyResetConnectionType,
       "usdBgpPeerAddressFamilyRowStatus": usdBgpPeerAddressFamilyRowStatus,
       "usdBgpPeerAddressFamilyAsOverride": usdBgpPeerAddressFamilyAsOverride,
       "usdBgpPeerAddressFamilyAllowAsIn": usdBgpPeerAddressFamilyAllowAsIn,
       "usdBgpPeerAddressFamilySendExtendedCommunity": usdBgpPeerAddressFamilySendExtendedCommunity,
       "usdBgpPeerAddressFamilyUnconfiguredAttributes": usdBgpPeerAddressFamilyUnconfiguredAttributes,
       "usdBgpPeerGroupTable": usdBgpPeerGroupTable,
       "usdBgpPeerGroupEntry": usdBgpPeerGroupEntry,
       "usdBgpPeerGroupVrfName": usdBgpPeerGroupVrfName,
       "usdBgpPeerGroupGroupName": usdBgpPeerGroupGroupName,
       "usdBgpPeerGroupAdminStatus": usdBgpPeerGroupAdminStatus,
       "usdBgpPeerGroupRemoteAsNumber": usdBgpPeerGroupRemoteAsNumber,
       "usdBgpPeerGroupRetryInterval": usdBgpPeerGroupRetryInterval,
       "usdBgpPeerGroupConfigHoldTime": usdBgpPeerGroupConfigHoldTime,
       "usdBgpPeerGroupConfigKeepAliveInterval": usdBgpPeerGroupConfigKeepAliveInterval,
       "usdBgpPeerGroupAsOriginationInterval": usdBgpPeerGroupAsOriginationInterval,
       "usdBgpPeerGroupAdvertisementInterval": usdBgpPeerGroupAdvertisementInterval,
       "usdBgpPeerGroupDescription": usdBgpPeerGroupDescription,
       "usdBgpPeerGroupWeight": usdBgpPeerGroupWeight,
       "usdBgpPeerGroupEbgpMultihop": usdBgpPeerGroupEbgpMultihop,
       "usdBgpPeerGroupEbgpMultihopTtl": usdBgpPeerGroupEbgpMultihopTtl,
       "usdBgpPeerGroupUpdateSource": usdBgpPeerGroupUpdateSource,
       "usdBgpPeerGroupMd5Password": usdBgpPeerGroupMd5Password,
       "usdBgpPeerGroupMaxUpdateSize": usdBgpPeerGroupMaxUpdateSize,
       "usdBgpPeerGroupResetConnectionType": usdBgpPeerGroupResetConnectionType,
       "usdBgpPeerGroupRowStatus": usdBgpPeerGroupRowStatus,
       "usdBgpPeerGroupLocalAsNumber": usdBgpPeerGroupLocalAsNumber,
       "usdBgpPeerGroupUnconfiguredAttributes": usdBgpPeerGroupUnconfiguredAttributes,
       "usdBgpPeerGroupAddressFamilyTable": usdBgpPeerGroupAddressFamilyTable,
       "usdBgpPeerGroupAddressFamilyEntry": usdBgpPeerGroupAddressFamilyEntry,
       "usdBgpPeerGroupAddressFamilyVrfName": usdBgpPeerGroupAddressFamilyVrfName,
       "usdBgpPeerGroupAddressFamilyAfi": usdBgpPeerGroupAddressFamilyAfi,
       "usdBgpPeerGroupAddressFamilySafi": usdBgpPeerGroupAddressFamilySafi,
       "usdBgpPeerGroupGroupAddressFamilyGroupName": usdBgpPeerGroupGroupAddressFamilyGroupName,
       "usdBgpPeerGroupAddressFamilyDefaultOriginate": usdBgpPeerGroupAddressFamilyDefaultOriginate,
       "usdBgpPeerGroupAddressFamilyNextHopSelf": usdBgpPeerGroupAddressFamilyNextHopSelf,
       "usdBgpPeerGroupAddressFamilySendCommunity": usdBgpPeerGroupAddressFamilySendCommunity,
       "usdBgpPeerGroupAddressFamilyDistributeListIn": usdBgpPeerGroupAddressFamilyDistributeListIn,
       "usdBgpPeerGroupAddressFamilyDistributeListOut": usdBgpPeerGroupAddressFamilyDistributeListOut,
       "usdBgpPeerGroupAddressFamilyPrefixListIn": usdBgpPeerGroupAddressFamilyPrefixListIn,
       "usdBgpPeerGroupAddressFamilyPrefixListOut": usdBgpPeerGroupAddressFamilyPrefixListOut,
       "usdBgpPeerGroupAddressFamilyPrefixTreeIn": usdBgpPeerGroupAddressFamilyPrefixTreeIn,
       "usdBgpPeerGroupAddressFamilyPrefixTreeOut": usdBgpPeerGroupAddressFamilyPrefixTreeOut,
       "usdBgpPeerGroupAddressFamilyFilterListIn": usdBgpPeerGroupAddressFamilyFilterListIn,
       "usdBgpPeerGroupAddressFamilyFilterListOut": usdBgpPeerGroupAddressFamilyFilterListOut,
       "usdBgpPeerGroupAddressFamilyFilterListWeight": usdBgpPeerGroupAddressFamilyFilterListWeight,
       "usdBgpPeerGroupAddressFamilyFilterListWeightValue": usdBgpPeerGroupAddressFamilyFilterListWeightValue,
       "usdBgpPeerGroupAddressFamilyRouteMapIn": usdBgpPeerGroupAddressFamilyRouteMapIn,
       "usdBgpPeerGroupAddressFamilyRouteMapOut": usdBgpPeerGroupAddressFamilyRouteMapOut,
       "usdBgpPeerGroupAddressFamilyRouteReflectorClient": usdBgpPeerGroupAddressFamilyRouteReflectorClient,
       "usdBgpPeerGroupAddressFamilyRouteLimitWarn": usdBgpPeerGroupAddressFamilyRouteLimitWarn,
       "usdBgpPeerGroupAddressFamilyRouteLimitReset": usdBgpPeerGroupAddressFamilyRouteLimitReset,
       "usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly": usdBgpPeerGroupAddressFamilyRouteLimitWarnOnly,
       "usdBgpPeerGroupAddressFamilyRemovePrivateAs": usdBgpPeerGroupAddressFamilyRemovePrivateAs,
       "usdBgpPeerGroupAddressFamilyUnsuppressMap": usdBgpPeerGroupAddressFamilyUnsuppressMap,
       "usdBgpPeerGroupAddressFamilyInboundSoftReconfig": usdBgpPeerGroupAddressFamilyInboundSoftReconfig,
       "usdBgpPeerGroupAddressFamilyResetConnectionType": usdBgpPeerGroupAddressFamilyResetConnectionType,
       "usdBgpPeerGroupAddressFamilyRowStatus": usdBgpPeerGroupAddressFamilyRowStatus,
       "usdBgpPeerGroupAddressFamilyAsOverride": usdBgpPeerGroupAddressFamilyAsOverride,
       "usdBgpPeerGroupAddressFamilyAllowAsIn": usdBgpPeerGroupAddressFamilyAllowAsIn,
       "usdBgpPeerGroupAddressFamilySendExtendedCommunity": usdBgpPeerGroupAddressFamilySendExtendedCommunity,
       "usdBgpPeerGroupAddressFamilyUnconfiguredAttributes": usdBgpPeerGroupAddressFamilyUnconfiguredAttributes,
       "usdBgpRouteFlapHistoryTable": usdBgpRouteFlapHistoryTable,
       "usdBgpRouteFlapHistoryEntry": usdBgpRouteFlapHistoryEntry,
       "usdBgpRouteFlapState": usdBgpRouteFlapState,
       "usdBgpRouteFlapFigureOfMerit": usdBgpRouteFlapFigureOfMerit,
       "usdBgpRouteFlapRemainingTime": usdBgpRouteFlapRemainingTime,
       "usdBgpRouteFlapSuppressThreshold": usdBgpRouteFlapSuppressThreshold,
       "usdBgpRouteFlapReuseThreshold": usdBgpRouteFlapReuseThreshold,
       "usdBgpRouteFlapMaxHoldDownTime": usdBgpRouteFlapMaxHoldDownTime,
       "usdBgpRouteFlapHalfLifeReachable": usdBgpRouteFlapHalfLifeReachable,
       "usdBgpRouteFlapHalfLifeUnreachable": usdBgpRouteFlapHalfLifeUnreachable,
       "usdBgpRouteTable": usdBgpRouteTable,
       "usdBgpRouteEntry": usdBgpRouteEntry,
       "usdBgpRouteOriginatorId": usdBgpRouteOriginatorId,
       "usdBgpRouteAtomicAggregatePresent": usdBgpRouteAtomicAggregatePresent,
       "usdBgpRouteMedPresent": usdBgpRouteMedPresent,
       "usdBgpRouteLocalPrefPresent": usdBgpRouteLocalPrefPresent,
       "usdBgpRouteAggregatorPresent": usdBgpRouteAggregatorPresent,
       "usdBgpRouteCommunitiesPresent": usdBgpRouteCommunitiesPresent,
       "usdBgpRouteOriginatorIdPresent": usdBgpRouteOriginatorIdPresent,
       "usdBgpRouteClusterListPresent": usdBgpRouteClusterListPresent,
       "usdBgpRouteWeight": usdBgpRouteWeight,
       "usdBgpRouteVrfName": usdBgpRouteVrfName,
       "usdBgpRouteAfi": usdBgpRouteAfi,
       "usdBgpRouteSafi": usdBgpRouteSafi,
       "usdBgpRoutePeer": usdBgpRoutePeer,
       "usdBgpRouteIpAddrPrefixLen": usdBgpRouteIpAddrPrefixLen,
       "usdBgpRouteIpAddrPrefix": usdBgpRouteIpAddrPrefix,
       "usdBgpRouteRouteType": usdBgpRouteRouteType,
       "usdBgpRouteOrigin": usdBgpRouteOrigin,
       "usdBgpRouteASPathSegment": usdBgpRouteASPathSegment,
       "usdBgpRouteNextHop": usdBgpRouteNextHop,
       "usdBgpRouteMultiExitDisc": usdBgpRouteMultiExitDisc,
       "usdBgpRouteLocalPref": usdBgpRouteLocalPref,
       "usdBgpRouteAtomicAggregate": usdBgpRouteAtomicAggregate,
       "usdBgpRouteAggregatorAS": usdBgpRouteAggregatorAS,
       "usdBgpRouteAggregatorAddress": usdBgpRouteAggregatorAddress,
       "usdBgpRouteBestInIpRouteTable": usdBgpRouteBestInIpRouteTable,
       "usdBgpRouteUnknown": usdBgpRouteUnknown,
       "usdBgpRouteExtendedCommunitiesPresent": usdBgpRouteExtendedCommunitiesPresent,
       "usdBgpRouteValid": usdBgpRouteValid,
       "usdBgpRouteSuppressedBy": usdBgpRouteSuppressedBy,
       "usdBgpRouteNextHopReachable": usdBgpRouteNextHopReachable,
       "usdBgpRouteSynchronizedWithIgp": usdBgpRouteSynchronizedWithIgp,
       "usdBgpRoutePlaceInIpRouteTable": usdBgpRoutePlaceInIpRouteTable,
       "usdBgpRouteAdvertiseToExternalPeers": usdBgpRouteAdvertiseToExternalPeers,
       "usdBgpRouteAdvertiseToInternalPeers": usdBgpRouteAdvertiseToInternalPeers,
       "usdBgpRouteDistinguisher": usdBgpRouteDistinguisher,
       "usdBgpRouteMplsLabel": usdBgpRouteMplsLabel,
       "usdBgpRouteNextHopMetric": usdBgpRouteNextHopMetric,
       "usdBgpRouteCommunityTable": usdBgpRouteCommunityTable,
       "usdBgpRouteCommunityEntry": usdBgpRouteCommunityEntry,
       "usdBgpRouteCommunityNumber": usdBgpRouteCommunityNumber,
       "usdBgpRouteClusterIdTable": usdBgpRouteClusterIdTable,
       "usdBgpRouteClusterIdEntry": usdBgpRouteClusterIdEntry,
       "usdBgpRouteClusterId": usdBgpRouteClusterId,
       "usdBgpNetworkTable": usdBgpNetworkTable,
       "usdBgpNetworkEntry": usdBgpNetworkEntry,
       "usdBgpNetworkVrfName": usdBgpNetworkVrfName,
       "usdBgpNetworkAfi": usdBgpNetworkAfi,
       "usdBgpNetworkSafi": usdBgpNetworkSafi,
       "usdBgpNetworkIpAddrPrefix": usdBgpNetworkIpAddrPrefix,
       "usdBgpNetworkIpAddrPrefixLen": usdBgpNetworkIpAddrPrefixLen,
       "usdBgpNetworkBackdoor": usdBgpNetworkBackdoor,
       "usdBgpNetworkRowStatus": usdBgpNetworkRowStatus,
       "usdBgpNetworkWeightSpecified": usdBgpNetworkWeightSpecified,
       "usdBgpNetworkWeight": usdBgpNetworkWeight,
       "usdBgpNetworkRouteMap": usdBgpNetworkRouteMap,
       "usdBgpNetworkUnconfiguredAttributes": usdBgpNetworkUnconfiguredAttributes,
       "usdBgpAggregateTable": usdBgpAggregateTable,
       "usdBgpAggregateEntry": usdBgpAggregateEntry,
       "usdBgpAggregateVrfName": usdBgpAggregateVrfName,
       "usdBgpAggregateAfi": usdBgpAggregateAfi,
       "usdBgpAggregateSafi": usdBgpAggregateSafi,
       "usdBgpAggregateIpAddrPrefix": usdBgpAggregateIpAddrPrefix,
       "usdBgpAggregateIpAddrPrefixLen": usdBgpAggregateIpAddrPrefixLen,
       "usdBgpAggregateAsSet": usdBgpAggregateAsSet,
       "usdBgpAggregateSummaryOnly": usdBgpAggregateSummaryOnly,
       "usdBgpAggregateAttributeMap": usdBgpAggregateAttributeMap,
       "usdBgpAggregateAdvertiseMap": usdBgpAggregateAdvertiseMap,
       "usdBgpAggregateRowStatus": usdBgpAggregateRowStatus,
       "usdBgpAggregateSuppressMap": usdBgpAggregateSuppressMap,
       "usdBgpAggregateUnconfiguredAttributes": usdBgpAggregateUnconfiguredAttributes,
       "usdBgpVrfTable": usdBgpVrfTable,
       "usdBgpVrfEntry": usdBgpVrfEntry,
       "usdBgpVrfName": usdBgpVrfName,
       "usdBgpVrfSynchronization": usdBgpVrfSynchronization,
       "usdBgpVrfAutoSummary": usdBgpVrfAutoSummary,
       "usdBgpVrfExternalDistance": usdBgpVrfExternalDistance,
       "usdBgpVrfInternalDistance": usdBgpVrfInternalDistance,
       "usdBgpVrfLocalDistance": usdBgpVrfLocalDistance,
       "usdBgpVrfResetConnectionType": usdBgpVrfResetConnectionType,
       "usdBgpVrfRowStatus": usdBgpVrfRowStatus,
       "usdBgpVrfOperationalState": usdBgpVrfOperationalState,
       "usdBgpVrfAddUnicastRoutesToMulticastView": usdBgpVrfAddUnicastRoutesToMulticastView,
       "usdBgpVrfUnconfiguredAttributes": usdBgpVrfUnconfiguredAttributes,
       "usdBgpAddressFamilyTable": usdBgpAddressFamilyTable,
       "usdBgpAddressFamilyEntry": usdBgpAddressFamilyEntry,
       "usdBgpAddressFamilyVrfName": usdBgpAddressFamilyVrfName,
       "usdBgpAddressFamilyAfi": usdBgpAddressFamilyAfi,
       "usdBgpAddressFamilySafi": usdBgpAddressFamilySafi,
       "usdBgpAddressFamilyDefaultOriginate": usdBgpAddressFamilyDefaultOriginate,
       "usdBgpAddressFamilyRouteFlapDampening": usdBgpAddressFamilyRouteFlapDampening,
       "usdBgpAddressFamilyDampeningSuppressThreshold": usdBgpAddressFamilyDampeningSuppressThreshold,
       "usdBgpAddressFamilyDampeningReuseThreshold": usdBgpAddressFamilyDampeningReuseThreshold,
       "usdBgpAddressFamilyDampeningMaxHoldDownTime": usdBgpAddressFamilyDampeningMaxHoldDownTime,
       "usdBgpAddressFamilyDampeningHalfLifeReachable": usdBgpAddressFamilyDampeningHalfLifeReachable,
       "usdBgpAddressFamilyDampeningHalfLifeUnreachable": usdBgpAddressFamilyDampeningHalfLifeUnreachable,
       "usdBgpAddressFamilyDampeningRouteMapName": usdBgpAddressFamilyDampeningRouteMapName,
       "usdBgpAddressFamilyResetConnectionType": usdBgpAddressFamilyResetConnectionType,
       "usdBgpAddressFamilyRowStatus": usdBgpAddressFamilyRowStatus,
       "usdBgpAddressFamilyOperationalState": usdBgpAddressFamilyOperationalState,
       "usdBgpAddressFamilyUnconfiguredAttributes": usdBgpAddressFamilyUnconfiguredAttributes,
       "usdBgpStorageGroup": usdBgpStorageGroup,
       "usdBgpStorageInitialHeapSize": usdBgpStorageInitialHeapSize,
       "usdBgpStorageMaxHeapSize": usdBgpStorageMaxHeapSize,
       "usdBgpStorageInitialVrfPoolSize": usdBgpStorageInitialVrfPoolSize,
       "usdBgpStorageMaxVrfPoolSize": usdBgpStorageMaxVrfPoolSize,
       "usdBgpStorageInitialAddressFamilyPoolSize": usdBgpStorageInitialAddressFamilyPoolSize,
       "usdBgpStorageMaxAddressFamilyPoolSize": usdBgpStorageMaxAddressFamilyPoolSize,
       "usdBgpStorageInitialPeerPoolSize": usdBgpStorageInitialPeerPoolSize,
       "usdBgpStorageMaxPeerPoolSize": usdBgpStorageMaxPeerPoolSize,
       "usdBgpStorageInitialPeerAfPoolSize": usdBgpStorageInitialPeerAfPoolSize,
       "usdBgpStorageMaxPeerAfPoolSize": usdBgpStorageMaxPeerAfPoolSize,
       "usdBgpStorageInitialPeerGroupPoolSize": usdBgpStorageInitialPeerGroupPoolSize,
       "usdBgpStorageMaxPeerGroupPoolSize": usdBgpStorageMaxPeerGroupPoolSize,
       "usdBgpStorageInitialPeerGroupAfPoolSize": usdBgpStorageInitialPeerGroupAfPoolSize,
       "usdBgpStorageMaxPeerGroupAfPoolSize": usdBgpStorageMaxPeerGroupAfPoolSize,
       "usdBgpStorageInitialNetworkPoolSize": usdBgpStorageInitialNetworkPoolSize,
       "usdBgpStorageMaxNetworkPoolSize": usdBgpStorageMaxNetworkPoolSize,
       "usdBgpStorageInitialAggregatePoolSize": usdBgpStorageInitialAggregatePoolSize,
       "usdBgpStorageMaxAggregatePoolSize": usdBgpStorageMaxAggregatePoolSize,
       "usdBgpStorageInitialDestinationPoolSize": usdBgpStorageInitialDestinationPoolSize,
       "usdBgpStorageMaxDestinationPoolSize": usdBgpStorageMaxDestinationPoolSize,
       "usdBgpStorageInitialRoutePoolSize": usdBgpStorageInitialRoutePoolSize,
       "usdBgpStorageMaxRoutePoolSize": usdBgpStorageMaxRoutePoolSize,
       "usdBgpStorageInitialAttributesPoolSize": usdBgpStorageInitialAttributesPoolSize,
       "usdBgpStorageMaxAttributesPoolSize": usdBgpStorageMaxAttributesPoolSize,
       "usdBgpStorageInitialRouteFlapHistoryPoolSize": usdBgpStorageInitialRouteFlapHistoryPoolSize,
       "usdBgpStorageMaxRouteFlapHistoryPoolSize": usdBgpStorageMaxRouteFlapHistoryPoolSize,
       "usdBgpStorageInitialNetworkRoutePoolSize": usdBgpStorageInitialNetworkRoutePoolSize,
       "usdBgpStorageMaxNetworkRoutePoolSize": usdBgpStorageMaxNetworkRoutePoolSize,
       "usdBgpStorageInitialRedistributedRoutePoolSize": usdBgpStorageInitialRedistributedRoutePoolSize,
       "usdBgpStorageMaxRedistributedRoutePoolSize": usdBgpStorageMaxRedistributedRoutePoolSize,
       "usdBgpStorageInitialAggregateRoutePoolSize": usdBgpStorageInitialAggregateRoutePoolSize,
       "usdBgpStorageMaxAggregateRoutePoolSize": usdBgpStorageMaxAggregateRoutePoolSize,
       "usdBgpStorageInitialAutoSummaryRoutePoolSize": usdBgpStorageInitialAutoSummaryRoutePoolSize,
       "usdBgpStorageMaxAutoSummaryRoutePoolSize": usdBgpStorageMaxAutoSummaryRoutePoolSize,
       "usdBgpStorageInitialHistoryRoutePoolSize": usdBgpStorageInitialHistoryRoutePoolSize,
       "usdBgpStorageMaxHistoryRoutePoolSize": usdBgpStorageMaxHistoryRoutePoolSize,
       "usdBgpStorageInitialSendQueueEntryPoolSize": usdBgpStorageInitialSendQueueEntryPoolSize,
       "usdBgpStorageMaxSendQueueEntryPoolSize": usdBgpStorageMaxSendQueueEntryPoolSize,
       "usdBgpStorageInitialVpnRoutePoolSize": usdBgpStorageInitialVpnRoutePoolSize,
       "usdBgpStorageMaxVpnRoutePoolSize": usdBgpStorageMaxVpnRoutePoolSize,
       "usdBgpStorageInitialRouteTargetPoolSize": usdBgpStorageInitialRouteTargetPoolSize,
       "usdBgpStorageMaxRouteTargetPoolSize": usdBgpStorageMaxRouteTargetPoolSize,
       "usdBgpRouteExtendedCommunityTable": usdBgpRouteExtendedCommunityTable,
       "usdBgpRouteExtendedCommunityEntry": usdBgpRouteExtendedCommunityEntry,
       "usdBgpRouteExtendedCommunityNumber": usdBgpRouteExtendedCommunityNumber,
       "usdBgpNewRouteTable": usdBgpNewRouteTable,
       "usdBgpNewRouteEntry": usdBgpNewRouteEntry,
       "usdBgpNewRouteVrfName": usdBgpNewRouteVrfName,
       "usdBgpNewRouteAfi": usdBgpNewRouteAfi,
       "usdBgpNewRouteSafi": usdBgpNewRouteSafi,
       "usdBgpNewRouteIpAddrPrefix": usdBgpNewRouteIpAddrPrefix,
       "usdBgpNewRouteIpAddrPrefixLen": usdBgpNewRouteIpAddrPrefixLen,
       "usdBgpNewRouteDistinguisher": usdBgpNewRouteDistinguisher,
       "usdBgpNewRoutePeer": usdBgpNewRoutePeer,
       "usdBgpNewRouteRouteType": usdBgpNewRouteRouteType,
       "usdBgpNewRouteOriginalRd": usdBgpNewRouteOriginalRd,
       "usdBgpNewRouteOriginatorId": usdBgpNewRouteOriginatorId,
       "usdBgpNewRouteAtomicAggregatePresent": usdBgpNewRouteAtomicAggregatePresent,
       "usdBgpNewRouteMedPresent": usdBgpNewRouteMedPresent,
       "usdBgpNewRouteLocalPrefPresent": usdBgpNewRouteLocalPrefPresent,
       "usdBgpNewRouteAggregatorPresent": usdBgpNewRouteAggregatorPresent,
       "usdBgpNewRouteCommunitiesPresent": usdBgpNewRouteCommunitiesPresent,
       "usdBgpNewRouteOriginatorIdPresent": usdBgpNewRouteOriginatorIdPresent,
       "usdBgpNewRouteClusterListPresent": usdBgpNewRouteClusterListPresent,
       "usdBgpNewRouteWeight": usdBgpNewRouteWeight,
       "usdBgpNewRouteOrigin": usdBgpNewRouteOrigin,
       "usdBgpNewRouteASPathSegment": usdBgpNewRouteASPathSegment,
       "usdBgpNewRouteNextHop": usdBgpNewRouteNextHop,
       "usdBgpNewRouteMultiExitDisc": usdBgpNewRouteMultiExitDisc,
       "usdBgpNewRouteLocalPref": usdBgpNewRouteLocalPref,
       "usdBgpNewRouteAtomicAggregate": usdBgpNewRouteAtomicAggregate,
       "usdBgpNewRouteAggregatorAS": usdBgpNewRouteAggregatorAS,
       "usdBgpNewRouteAggregatorAddress": usdBgpNewRouteAggregatorAddress,
       "usdBgpNewRouteBestInIpRouteTable": usdBgpNewRouteBestInIpRouteTable,
       "usdBgpNewRouteUnknown": usdBgpNewRouteUnknown,
       "usdBgpNewRouteExtendedCommunitiesPresent": usdBgpNewRouteExtendedCommunitiesPresent,
       "usdBgpNewRouteValid": usdBgpNewRouteValid,
       "usdBgpNewRouteSuppressedBy": usdBgpNewRouteSuppressedBy,
       "usdBgpNewRouteNextHopReachable": usdBgpNewRouteNextHopReachable,
       "usdBgpNewRouteSynchronizedWithIgp": usdBgpNewRouteSynchronizedWithIgp,
       "usdBgpNewRoutePlaceInIpRouteTable": usdBgpNewRoutePlaceInIpRouteTable,
       "usdBgpNewRouteAdvertiseToExternalPeers": usdBgpNewRouteAdvertiseToExternalPeers,
       "usdBgpNewRouteAdvertiseToInternalPeers": usdBgpNewRouteAdvertiseToInternalPeers,
       "usdBgpNewRouteMplsLabel": usdBgpNewRouteMplsLabel,
       "usdBgpNewRouteNextHopMetric": usdBgpNewRouteNextHopMetric,
       "usdBgpNewRouteFlapHistoryTable": usdBgpNewRouteFlapHistoryTable,
       "usdBgpNewRouteFlapHistoryEntry": usdBgpNewRouteFlapHistoryEntry,
       "usdBgpNewRouteFlapState": usdBgpNewRouteFlapState,
       "usdBgpNewRouteFlapFigureOfMerit": usdBgpNewRouteFlapFigureOfMerit,
       "usdBgpNewRouteFlapRemainingTime": usdBgpNewRouteFlapRemainingTime,
       "usdBgpNewRouteFlapSuppressThreshold": usdBgpNewRouteFlapSuppressThreshold,
       "usdBgpNewRouteFlapReuseThreshold": usdBgpNewRouteFlapReuseThreshold,
       "usdBgpNewRouteFlapMaxHoldDownTime": usdBgpNewRouteFlapMaxHoldDownTime,
       "usdBgpNewRouteFlapHalfLifeReachable": usdBgpNewRouteFlapHalfLifeReachable,
       "usdBgpNewRouteFlapHalfLifeUnreachable": usdBgpNewRouteFlapHalfLifeUnreachable,
       "usdBgpNewRouteCommunityTable": usdBgpNewRouteCommunityTable,
       "usdBgpNewRouteCommunityEntry": usdBgpNewRouteCommunityEntry,
       "usdBgpNewRouteCommunityNumber": usdBgpNewRouteCommunityNumber,
       "usdBgpNewRouteExtendedCommunityTable": usdBgpNewRouteExtendedCommunityTable,
       "usdBgpNewRouteExtendedCommunityEntry": usdBgpNewRouteExtendedCommunityEntry,
       "usdBgpNewRouteExtendedCommunityNumber": usdBgpNewRouteExtendedCommunityNumber,
       "usdBgpNewRouteClusterIdTable": usdBgpNewRouteClusterIdTable,
       "usdBgpNewRouteClusterIdEntry": usdBgpNewRouteClusterIdEntry,
       "usdBgpNewRouteClusterId": usdBgpNewRouteClusterId,
       "usdBgpConformance": usdBgpConformance,
       "usdBgpCompliances": usdBgpCompliances,
       "usdBgpCompliance": usdBgpCompliance,
       "usdBgpCompliance2": usdBgpCompliance2,
       "usdBgpCompliance3": usdBgpCompliance3,
       "usdBgpCompliance4": usdBgpCompliance4,
       "usdBgpCompliance5": usdBgpCompliance5,
       "usdBgpCompliance6": usdBgpCompliance6,
       "usdBgpConfGroups": usdBgpConfGroups,
       "usdBgpGeneralConfGroup": usdBgpGeneralConfGroup,
       "usdBgpStatisticsConfGroup": usdBgpStatisticsConfGroup,
       "usdBgpConfederationPeerConfGroup": usdBgpConfederationPeerConfGroup,
       "usdBgpPeerConfGroup": usdBgpPeerConfGroup,
       "usdBgpAfiSafiPeerConfGroup": usdBgpAfiSafiPeerConfGroup,
       "usdBgpPeerAddressFamilyConfGroup": usdBgpPeerAddressFamilyConfGroup,
       "usdBgpPeerGroupConfGroup": usdBgpPeerGroupConfGroup,
       "usdBgpPeerGroupAddressFamilyConfGroup": usdBgpPeerGroupAddressFamilyConfGroup,
       "usdBgpRouteConfGroup": usdBgpRouteConfGroup,
       "usdBgpNetworkConfGroup": usdBgpNetworkConfGroup,
       "usdBgpAggregateConfGroup": usdBgpAggregateConfGroup,
       "usdBgpVrfConfGroup": usdBgpVrfConfGroup,
       "usdBgpAddressFamilyConfGroup": usdBgpAddressFamilyConfGroup,
       "usdBgpStorageConfGroup": usdBgpStorageConfGroup,
       "usdBgpGeneralConfGroup2": usdBgpGeneralConfGroup2,
       "usdBgpNewRouteConfGroup": usdBgpNewRouteConfGroup,
       "usdBgpPeerConfGroup2": usdBgpPeerConfGroup2,
       "usdBgpPeerGroupConfGroup2": usdBgpPeerGroupConfGroup2,
       "usdBgpVrfConfGroup2": usdBgpVrfConfGroup2,
       "usdBgpGeneralConfGroup3": usdBgpGeneralConfGroup3,
       "usdBgpStorageConfGroup2": usdBgpStorageConfGroup2,
       "usdBgpPeerConfGroup3": usdBgpPeerConfGroup3,
       "usdBgpPeerAddressFamilyConfGroup2": usdBgpPeerAddressFamilyConfGroup2,
       "usdBgpPeerGroupConfGroup3": usdBgpPeerGroupConfGroup3,
       "usdBgpPeerGroupAddressFamilyConfGroup2": usdBgpPeerGroupAddressFamilyConfGroup2,
       "usdBgpNetworkConfGroup2": usdBgpNetworkConfGroup2,
       "usdBgpAggregateConfGroup2": usdBgpAggregateConfGroup2,
       "usdBgpVrfConfGroup3": usdBgpVrfConfGroup3,
       "usdBgpAddressFamilyConfGroup2": usdBgpAddressFamilyConfGroup2}
)
