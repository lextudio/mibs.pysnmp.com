# SNMP MIB module (Juniper-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:45 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniVrfName,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniVrfName")

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


# MODULE-IDENTITY

juniBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29)
)
juniBgpMIB.setRevisions(
        ("2007-05-11 05:17",
         "2006-05-15 19:24",
         "2005-12-29 21:37",
         "2005-10-05 18:46",
         "2005-10-03 18:46",
         "2004-07-06 18:46",
         "2004-05-26 19:24",
         "2004-05-26 19:24",
         "2004-05-26 19:24",
         "2004-05-26 19:24",
         "2004-05-26 19:24",
         "2002-08-31 18:22",
         "2002-03-01 16:54",
         "2002-01-23 13:16",
         "2001-12-04 15:23",
         "2001-11-30 22:20",
         "2001-06-18 18:59",
         "2000-01-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniBgpAfi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bgpIpV4", 1),
          ("bgpIpV6", 2))
    )



class JuniBgpSafi(Integer32, TextualConvention):
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



class JuniBgpStorageInteger(Unsigned32, TextualConvention):
    status = "current"


class JuniBgpResetConnectionType(Integer32, TextualConvention):
    status = "current"
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("resetTypeDynamicPeers", 9),
          ("resetTypeHard", 1),
          ("resetTypeNoop", 0),
          ("resetTypeRecreateAllIpDynInterfaces", 8),
          ("resetTypeRouteFlapHistory", 5),
          ("resetTypeSoftIn", 2),
          ("resetTypeSoftInOut", 4),
          ("resetTypeSoftInWithPrefixOrfPush", 6),
          ("resetTypeSoftOut", 3),
          ("resetTypeWaitEndOfRib", 7))
    )



class JuniBgpFourOctetAsNumber(Unsigned32, TextualConvention):
    status = "current"


class JuniBgpAdvertiseMapName(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class JuniBgpConditionalAdvStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 1),
          ("withdraw", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JuniBgpObjects_ObjectIdentity = ObjectIdentity
juniBgpObjects = _JuniBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1)
)
_JuniBgpGeneralGroup_ObjectIdentity = ObjectIdentity
juniBgpGeneralGroup = _JuniBgpGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1)
)


class _JuniBgpLocalAsNumber_Type(Integer32):
    """Custom type juniBgpLocalAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpLocalAsNumber_Type.__name__ = "Integer32"
_JuniBgpLocalAsNumber_Object = MibScalar
juniBgpLocalAsNumber = _JuniBgpLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 1),
    _JuniBgpLocalAsNumber_Type()
)
juniBgpLocalAsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpLocalAsNumber.setStatus("deprecated")


class _JuniBgpEnabled_Type(TruthValue):
    """Custom type juniBgpEnabled based on TruthValue"""


_JuniBgpEnabled_Object = MibScalar
juniBgpEnabled = _JuniBgpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 2),
    _JuniBgpEnabled_Type()
)
juniBgpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpEnabled.setStatus("current")
_JuniBgpIdentifier_Type = IpAddress
_JuniBgpIdentifier_Object = MibScalar
juniBgpIdentifier = _JuniBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 3),
    _JuniBgpIdentifier_Type()
)
juniBgpIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpIdentifier.setStatus("current")


class _JuniBgpAlwaysCompareMed_Type(TruthValue):
    """Custom type juniBgpAlwaysCompareMed based on TruthValue"""


_JuniBgpAlwaysCompareMed_Object = MibScalar
juniBgpAlwaysCompareMed = _JuniBgpAlwaysCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 4),
    _JuniBgpAlwaysCompareMed_Type()
)
juniBgpAlwaysCompareMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpAlwaysCompareMed.setStatus("current")


class _JuniBgpDefaultLocalPreference_Type(Unsigned32):
    """Custom type juniBgpDefaultLocalPreference based on Unsigned32"""
    defaultValue = 100


_JuniBgpDefaultLocalPreference_Object = MibScalar
juniBgpDefaultLocalPreference = _JuniBgpDefaultLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 5),
    _JuniBgpDefaultLocalPreference_Type()
)
juniBgpDefaultLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpDefaultLocalPreference.setStatus("current")


class _JuniBgpEqualCostLimit_Type(Integer32):
    """Custom type juniBgpEqualCostLimit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpEqualCostLimit_Type.__name__ = "Integer32"
_JuniBgpEqualCostLimit_Object = MibScalar
juniBgpEqualCostLimit = _JuniBgpEqualCostLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 6),
    _JuniBgpEqualCostLimit_Type()
)
juniBgpEqualCostLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpEqualCostLimit.setStatus("obsolete")


class _JuniBgpClientToClientReflection_Type(TruthValue):
    """Custom type juniBgpClientToClientReflection based on TruthValue"""


_JuniBgpClientToClientReflection_Object = MibScalar
juniBgpClientToClientReflection = _JuniBgpClientToClientReflection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 7),
    _JuniBgpClientToClientReflection_Type()
)
juniBgpClientToClientReflection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpClientToClientReflection.setStatus("current")


class _JuniBgpClusterId_Type(Unsigned32):
    """Custom type juniBgpClusterId based on Unsigned32"""
    defaultValue = 0


_JuniBgpClusterId_Object = MibScalar
juniBgpClusterId = _JuniBgpClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 8),
    _JuniBgpClusterId_Type()
)
juniBgpClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpClusterId.setStatus("current")


class _JuniBgpConfederationId_Type(Unsigned32):
    """Custom type juniBgpConfederationId based on Unsigned32"""
    defaultValue = 0


_JuniBgpConfederationId_Object = MibScalar
juniBgpConfederationId = _JuniBgpConfederationId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 9),
    _JuniBgpConfederationId_Type()
)
juniBgpConfederationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpConfederationId.setStatus("current")


class _JuniBgpMissingAsWorst_Type(TruthValue):
    """Custom type juniBgpMissingAsWorst based on TruthValue"""


_JuniBgpMissingAsWorst_Object = MibScalar
juniBgpMissingAsWorst = _JuniBgpMissingAsWorst_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 10),
    _JuniBgpMissingAsWorst_Type()
)
juniBgpMissingAsWorst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpMissingAsWorst.setStatus("current")


class _JuniBgpResetAllConnectionType_Type(JuniBgpResetConnectionType):
    """Custom type juniBgpResetAllConnectionType based on JuniBgpResetConnectionType"""


_JuniBgpResetAllConnectionType_Object = MibScalar
juniBgpResetAllConnectionType = _JuniBgpResetAllConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 11),
    _JuniBgpResetAllConnectionType_Type()
)
juniBgpResetAllConnectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpResetAllConnectionType.setStatus("current")


class _JuniBgpAdvertiseInactive_Type(TruthValue):
    """Custom type juniBgpAdvertiseInactive based on TruthValue"""


_JuniBgpAdvertiseInactive_Object = MibScalar
juniBgpAdvertiseInactive = _JuniBgpAdvertiseInactive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 12),
    _JuniBgpAdvertiseInactive_Type()
)
juniBgpAdvertiseInactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpAdvertiseInactive.setStatus("current")


class _JuniBgpEnforceFirstAs_Type(TruthValue):
    """Custom type juniBgpEnforceFirstAs based on TruthValue"""


_JuniBgpEnforceFirstAs_Object = MibScalar
juniBgpEnforceFirstAs = _JuniBgpEnforceFirstAs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 13),
    _JuniBgpEnforceFirstAs_Type()
)
juniBgpEnforceFirstAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpEnforceFirstAs.setStatus("current")


class _JuniBgpConfedCompareMed_Type(TruthValue):
    """Custom type juniBgpConfedCompareMed based on TruthValue"""


_JuniBgpConfedCompareMed_Object = MibScalar
juniBgpConfedCompareMed = _JuniBgpConfedCompareMed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 14),
    _JuniBgpConfedCompareMed_Type()
)
juniBgpConfedCompareMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpConfedCompareMed.setStatus("current")


class _JuniBgpGlobalRetryInterval_Type(Integer32):
    """Custom type juniBgpGlobalRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpGlobalRetryInterval_Type.__name__ = "Integer32"
_JuniBgpGlobalRetryInterval_Object = MibScalar
juniBgpGlobalRetryInterval = _JuniBgpGlobalRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 15),
    _JuniBgpGlobalRetryInterval_Type()
)
juniBgpGlobalRetryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGlobalRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpGlobalRetryInterval.setUnits("seconds")


class _JuniBgpGlobalConfigKeepAliveInterval_Type(Integer32):
    """Custom type juniBgpGlobalConfigKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpGlobalConfigKeepAliveInterval_Type.__name__ = "Integer32"
_JuniBgpGlobalConfigKeepAliveInterval_Object = MibScalar
juniBgpGlobalConfigKeepAliveInterval = _JuniBgpGlobalConfigKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 16),
    _JuniBgpGlobalConfigKeepAliveInterval_Type()
)
juniBgpGlobalConfigKeepAliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGlobalConfigKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpGlobalConfigKeepAliveInterval.setUnits("seconds")


class _JuniBgpGlobalConfigHoldTime_Type(Integer32):
    """Custom type juniBgpGlobalConfigHoldTime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JuniBgpGlobalConfigHoldTime_Type.__name__ = "Integer32"
_JuniBgpGlobalConfigHoldTime_Object = MibScalar
juniBgpGlobalConfigHoldTime = _JuniBgpGlobalConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 17),
    _JuniBgpGlobalConfigHoldTime_Type()
)
juniBgpGlobalConfigHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGlobalConfigHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpGlobalConfigHoldTime.setUnits("seconds")


class _JuniBgpGlobalAsOriginationInterval_Type(Integer32):
    """Custom type juniBgpGlobalAsOriginationInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpGlobalAsOriginationInterval_Type.__name__ = "Integer32"
_JuniBgpGlobalAsOriginationInterval_Object = MibScalar
juniBgpGlobalAsOriginationInterval = _JuniBgpGlobalAsOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 18),
    _JuniBgpGlobalAsOriginationInterval_Type()
)
juniBgpGlobalAsOriginationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGlobalAsOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpGlobalAsOriginationInterval.setUnits("seconds")


class _JuniBgpExternalAdvertisementInterval_Type(Integer32):
    """Custom type juniBgpExternalAdvertisementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpExternalAdvertisementInterval_Type.__name__ = "Integer32"
_JuniBgpExternalAdvertisementInterval_Object = MibScalar
juniBgpExternalAdvertisementInterval = _JuniBgpExternalAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 19),
    _JuniBgpExternalAdvertisementInterval_Type()
)
juniBgpExternalAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpExternalAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpExternalAdvertisementInterval.setUnits("seconds")


class _JuniBgpGlobalRibOutEnabled_Type(TruthValue):
    """Custom type juniBgpGlobalRibOutEnabled based on TruthValue"""


_JuniBgpGlobalRibOutEnabled_Object = MibScalar
juniBgpGlobalRibOutEnabled = _JuniBgpGlobalRibOutEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 20),
    _JuniBgpGlobalRibOutEnabled_Type()
)
juniBgpGlobalRibOutEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGlobalRibOutEnabled.setStatus("current")


class _JuniBgpOverloadShutdown_Type(TruthValue):
    """Custom type juniBgpOverloadShutdown based on TruthValue"""


_JuniBgpOverloadShutdown_Object = MibScalar
juniBgpOverloadShutdown = _JuniBgpOverloadShutdown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 21),
    _JuniBgpOverloadShutdown_Type()
)
juniBgpOverloadShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpOverloadShutdown.setStatus("current")


class _JuniBgpLogNeighborChanges_Type(TruthValue):
    """Custom type juniBgpLogNeighborChanges based on TruthValue"""


_JuniBgpLogNeighborChanges_Object = MibScalar
juniBgpLogNeighborChanges = _JuniBgpLogNeighborChanges_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 22),
    _JuniBgpLogNeighborChanges_Type()
)
juniBgpLogNeighborChanges.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpLogNeighborChanges.setStatus("current")


class _JuniBgpFastExternalFallover_Type(TruthValue):
    """Custom type juniBgpFastExternalFallover based on TruthValue"""


_JuniBgpFastExternalFallover_Object = MibScalar
juniBgpFastExternalFallover = _JuniBgpFastExternalFallover_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 23),
    _JuniBgpFastExternalFallover_Type()
)
juniBgpFastExternalFallover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpFastExternalFallover.setStatus("current")


class _JuniBgpInternalAdvertisementInterval_Type(Integer32):
    """Custom type juniBgpInternalAdvertisementInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpInternalAdvertisementInterval_Type.__name__ = "Integer32"
_JuniBgpInternalAdvertisementInterval_Object = MibScalar
juniBgpInternalAdvertisementInterval = _JuniBgpInternalAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 24),
    _JuniBgpInternalAdvertisementInterval_Type()
)
juniBgpInternalAdvertisementInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpInternalAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpInternalAdvertisementInterval.setUnits("seconds")


class _JuniBgpMaxAsLimit_Type(Integer32):
    """Custom type juniBgpMaxAsLimit based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpMaxAsLimit_Type.__name__ = "Integer32"
_JuniBgpMaxAsLimit_Object = MibScalar
juniBgpMaxAsLimit = _JuniBgpMaxAsLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 25),
    _JuniBgpMaxAsLimit_Type()
)
juniBgpMaxAsLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpMaxAsLimit.setStatus("current")


class _JuniBgpOperationalState_Type(Integer32):
    """Custom type juniBgpOperationalState based on Integer32"""
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


_JuniBgpOperationalState_Type.__name__ = "Integer32"
_JuniBgpOperationalState_Object = MibScalar
juniBgpOperationalState = _JuniBgpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 26),
    _JuniBgpOperationalState_Type()
)
juniBgpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpOperationalState.setStatus("current")


class _JuniBgpPreviousOperationalState_Type(Integer32):
    """Custom type juniBgpPreviousOperationalState based on Integer32"""
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


_JuniBgpPreviousOperationalState_Type.__name__ = "Integer32"
_JuniBgpPreviousOperationalState_Object = MibScalar
juniBgpPreviousOperationalState = _JuniBgpPreviousOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 27),
    _JuniBgpPreviousOperationalState_Type()
)
juniBgpPreviousOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPreviousOperationalState.setStatus("current")


class _JuniBgpAutomaticRouteTargetFilter_Type(TruthValue):
    """Custom type juniBgpAutomaticRouteTargetFilter based on TruthValue"""


_JuniBgpAutomaticRouteTargetFilter_Object = MibScalar
juniBgpAutomaticRouteTargetFilter = _JuniBgpAutomaticRouteTargetFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 28),
    _JuniBgpAutomaticRouteTargetFilter_Type()
)
juniBgpAutomaticRouteTargetFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpAutomaticRouteTargetFilter.setStatus("current")


class _JuniBgpDefaultIPv4Unicast_Type(TruthValue):
    """Custom type juniBgpDefaultIPv4Unicast based on TruthValue"""


_JuniBgpDefaultIPv4Unicast_Object = MibScalar
juniBgpDefaultIPv4Unicast = _JuniBgpDefaultIPv4Unicast_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 29),
    _JuniBgpDefaultIPv4Unicast_Type()
)
juniBgpDefaultIPv4Unicast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpDefaultIPv4Unicast.setStatus("current")


class _JuniBgpRedistributeInternal_Type(TruthValue):
    """Custom type juniBgpRedistributeInternal based on TruthValue"""


_JuniBgpRedistributeInternal_Object = MibScalar
juniBgpRedistributeInternal = _JuniBgpRedistributeInternal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 30),
    _JuniBgpRedistributeInternal_Type()
)
juniBgpRedistributeInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpRedistributeInternal.setStatus("current")


class _JuniBgpFourOctetLocalAsNumber_Type(JuniBgpFourOctetAsNumber):
    """Custom type juniBgpFourOctetLocalAsNumber based on JuniBgpFourOctetAsNumber"""
    defaultValue = 0


_JuniBgpFourOctetLocalAsNumber_Object = MibScalar
juniBgpFourOctetLocalAsNumber = _JuniBgpFourOctetLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 31),
    _JuniBgpFourOctetLocalAsNumber_Type()
)
juniBgpFourOctetLocalAsNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpFourOctetLocalAsNumber.setStatus("current")


class _JuniBgpConfederationPeersFilterList_Type(DisplayString):
    """Custom type juniBgpConfederationPeersFilterList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpConfederationPeersFilterList_Type.__name__ = "DisplayString"
_JuniBgpConfederationPeersFilterList_Object = MibScalar
juniBgpConfederationPeersFilterList = _JuniBgpConfederationPeersFilterList_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 32),
    _JuniBgpConfederationPeersFilterList_Type()
)
juniBgpConfederationPeersFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpConfederationPeersFilterList.setStatus("current")


class _JuniBgpUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpAdvertiseBestExternalToInternal", 28),
          ("juniBgpAdvertiseInactive", 9),
          ("juniBgpAlwaysCompareMed", 2),
          ("juniBgpAutomaticRouteTargetFilter", 23),
          ("juniBgpClientToClientReflection", 5),
          ("juniBgpClusterId", 6),
          ("juniBgpConfedCompareMed", 11),
          ("juniBgpConfederationId", 7),
          ("juniBgpConfederationPeersFilterList", 27),
          ("juniBgpDefaultIPv4Unicast", 24),
          ("juniBgpDefaultLocalPreference", 3),
          ("juniBgpEnabled", 0),
          ("juniBgpEnforceFirstAs", 10),
          ("juniBgpEqualCostLimit", 4),
          ("juniBgpExternalAdvertisementInterval", 16),
          ("juniBgpFastExternalFallover", 20),
          ("juniBgpFourOctetLocalAsNumber", 26),
          ("juniBgpGlobalAsOriginationInterval", 15),
          ("juniBgpGlobalConfigHoldTime", 14),
          ("juniBgpGlobalConfigKeepAliveInterval", 13),
          ("juniBgpGlobalRetryInterval", 12),
          ("juniBgpGlobalRibOutEnabled", 17),
          ("juniBgpGracefulRestartEnabled", 29),
          ("juniBgpGracefulRestartPathSelectionDeferTimeLimit", 32),
          ("juniBgpGracefulRestartRestartTime", 30),
          ("juniBgpGracefulRestartStalePathsTime", 31),
          ("juniBgpIdentifier", 1),
          ("juniBgpInternalAdvertisementInterval", 21),
          ("juniBgpLogNeighborChanges", 19),
          ("juniBgpMaxAsLimit", 22),
          ("juniBgpMissingAsWorst", 8),
          ("juniBgpOverloadShutdown", 18),
          ("juniBgpRedistributeInternal", 25))
    )

_JuniBgpUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpUnconfiguredAttributes_Object = MibScalar
juniBgpUnconfiguredAttributes = _JuniBgpUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 33),
    _JuniBgpUnconfiguredAttributes_Type()
)
juniBgpUnconfiguredAttributes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpUnconfiguredAttributes.setStatus("current")


class _JuniBgpAdvertiseBestExternalToInternal_Type(TruthValue):
    """Custom type juniBgpAdvertiseBestExternalToInternal based on TruthValue"""


_JuniBgpAdvertiseBestExternalToInternal_Object = MibScalar
juniBgpAdvertiseBestExternalToInternal = _JuniBgpAdvertiseBestExternalToInternal_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 34),
    _JuniBgpAdvertiseBestExternalToInternal_Type()
)
juniBgpAdvertiseBestExternalToInternal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpAdvertiseBestExternalToInternal.setStatus("current")


class _JuniBgpGracefulRestartEnabled_Type(TruthValue):
    """Custom type juniBgpGracefulRestartEnabled based on TruthValue"""


_JuniBgpGracefulRestartEnabled_Object = MibScalar
juniBgpGracefulRestartEnabled = _JuniBgpGracefulRestartEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 35),
    _JuniBgpGracefulRestartEnabled_Type()
)
juniBgpGracefulRestartEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGracefulRestartEnabled.setStatus("current")


class _JuniBgpGracefulRestartRestartTime_Type(Integer32):
    """Custom type juniBgpGracefulRestartRestartTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuniBgpGracefulRestartRestartTime_Type.__name__ = "Integer32"
_JuniBgpGracefulRestartRestartTime_Object = MibScalar
juniBgpGracefulRestartRestartTime = _JuniBgpGracefulRestartRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 36),
    _JuniBgpGracefulRestartRestartTime_Type()
)
juniBgpGracefulRestartRestartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGracefulRestartRestartTime.setStatus("current")


class _JuniBgpGracefulRestartStalePathsTime_Type(Integer32):
    """Custom type juniBgpGracefulRestartStalePathsTime based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuniBgpGracefulRestartStalePathsTime_Type.__name__ = "Integer32"
_JuniBgpGracefulRestartStalePathsTime_Object = MibScalar
juniBgpGracefulRestartStalePathsTime = _JuniBgpGracefulRestartStalePathsTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 37),
    _JuniBgpGracefulRestartStalePathsTime_Type()
)
juniBgpGracefulRestartStalePathsTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGracefulRestartStalePathsTime.setStatus("current")


class _JuniBgpGracefulRestartPathSelectionDeferTimeLimit_Type(Integer32):
    """Custom type juniBgpGracefulRestartPathSelectionDeferTimeLimit based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuniBgpGracefulRestartPathSelectionDeferTimeLimit_Type.__name__ = "Integer32"
_JuniBgpGracefulRestartPathSelectionDeferTimeLimit_Object = MibScalar
juniBgpGracefulRestartPathSelectionDeferTimeLimit = _JuniBgpGracefulRestartPathSelectionDeferTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 38),
    _JuniBgpGracefulRestartPathSelectionDeferTimeLimit_Type()
)
juniBgpGracefulRestartPathSelectionDeferTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpGracefulRestartPathSelectionDeferTimeLimit.setStatus("current")
_JuniBgpPlatformSupportsNonStopForwarding_Type = TruthValue
_JuniBgpPlatformSupportsNonStopForwarding_Object = MibScalar
juniBgpPlatformSupportsNonStopForwarding = _JuniBgpPlatformSupportsNonStopForwarding_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 39),
    _JuniBgpPlatformSupportsNonStopForwarding_Type()
)
juniBgpPlatformSupportsNonStopForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPlatformSupportsNonStopForwarding.setStatus("current")
_JuniBgpDeviceCanPreserveForwardingState_Type = TruthValue
_JuniBgpDeviceCanPreserveForwardingState_Object = MibScalar
juniBgpDeviceCanPreserveForwardingState = _JuniBgpDeviceCanPreserveForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 40),
    _JuniBgpDeviceCanPreserveForwardingState_Type()
)
juniBgpDeviceCanPreserveForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpDeviceCanPreserveForwardingState.setStatus("current")
_JuniBgpLastRestartWasGraceful_Type = TruthValue
_JuniBgpLastRestartWasGraceful_Object = MibScalar
juniBgpLastRestartWasGraceful = _JuniBgpLastRestartWasGraceful_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 1, 41),
    _JuniBgpLastRestartWasGraceful_Type()
)
juniBgpLastRestartWasGraceful.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpLastRestartWasGraceful.setStatus("current")
_JuniBgpRouteTableStatisticsGroup_ObjectIdentity = ObjectIdentity
juniBgpRouteTableStatisticsGroup = _JuniBgpRouteTableStatisticsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2)
)
_JuniBgpBaselineTime_Type = Unsigned32
_JuniBgpBaselineTime_Object = MibScalar
juniBgpBaselineTime = _JuniBgpBaselineTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 1),
    _JuniBgpBaselineTime_Type()
)
juniBgpBaselineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpBaselineTime.setStatus("current")
_JuniBgpDestinationCount_Type = Gauge32
_JuniBgpDestinationCount_Object = MibScalar
juniBgpDestinationCount = _JuniBgpDestinationCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 2),
    _JuniBgpDestinationCount_Type()
)
juniBgpDestinationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpDestinationCount.setStatus("current")
_JuniBgpDestinationMemoryUsed_Type = Gauge32
_JuniBgpDestinationMemoryUsed_Object = MibScalar
juniBgpDestinationMemoryUsed = _JuniBgpDestinationMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 3),
    _JuniBgpDestinationMemoryUsed_Type()
)
juniBgpDestinationMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpDestinationMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpDestinationMemoryUsed.setUnits("bytes")
_JuniBgpRouteCount_Type = Gauge32
_JuniBgpRouteCount_Object = MibScalar
juniBgpRouteCount = _JuniBgpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 4),
    _JuniBgpRouteCount_Type()
)
juniBgpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteCount.setStatus("current")
_JuniBgpRouteMemoryUsed_Type = Gauge32
_JuniBgpRouteMemoryUsed_Object = MibScalar
juniBgpRouteMemoryUsed = _JuniBgpRouteMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 5),
    _JuniBgpRouteMemoryUsed_Type()
)
juniBgpRouteMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpRouteMemoryUsed.setUnits("bytes")
_JuniBgpSelectedRouteCount_Type = Gauge32
_JuniBgpSelectedRouteCount_Object = MibScalar
juniBgpSelectedRouteCount = _JuniBgpSelectedRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 6),
    _JuniBgpSelectedRouteCount_Type()
)
juniBgpSelectedRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpSelectedRouteCount.setStatus("current")
_JuniBgpPathAttributeCount_Type = Gauge32
_JuniBgpPathAttributeCount_Object = MibScalar
juniBgpPathAttributeCount = _JuniBgpPathAttributeCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 8),
    _JuniBgpPathAttributeCount_Type()
)
juniBgpPathAttributeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPathAttributeCount.setStatus("current")
_JuniBgpPathAttributeMemoryUsed_Type = Gauge32
_JuniBgpPathAttributeMemoryUsed_Object = MibScalar
juniBgpPathAttributeMemoryUsed = _JuniBgpPathAttributeMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 9),
    _JuniBgpPathAttributeMemoryUsed_Type()
)
juniBgpPathAttributeMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPathAttributeMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPathAttributeMemoryUsed.setUnits("bytes")
_JuniBgpRouteFlapHistoryCount_Type = Gauge32
_JuniBgpRouteFlapHistoryCount_Object = MibScalar
juniBgpRouteFlapHistoryCount = _JuniBgpRouteFlapHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 10),
    _JuniBgpRouteFlapHistoryCount_Type()
)
juniBgpRouteFlapHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapHistoryCount.setStatus("current")
_JuniBgpRouteFlapHistoryMemoryUsed_Type = Gauge32
_JuniBgpRouteFlapHistoryMemoryUsed_Object = MibScalar
juniBgpRouteFlapHistoryMemoryUsed = _JuniBgpRouteFlapHistoryMemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 11),
    _JuniBgpRouteFlapHistoryMemoryUsed_Type()
)
juniBgpRouteFlapHistoryMemoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapHistoryMemoryUsed.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpRouteFlapHistoryMemoryUsed.setUnits("bytes")
_JuniBgpSuppressedRouteCount_Type = Gauge32
_JuniBgpSuppressedRouteCount_Object = MibScalar
juniBgpSuppressedRouteCount = _JuniBgpSuppressedRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 2, 12),
    _JuniBgpSuppressedRouteCount_Type()
)
juniBgpSuppressedRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpSuppressedRouteCount.setStatus("current")
_JuniBgpConfederationPeerTable_Object = MibTable
juniBgpConfederationPeerTable = _JuniBgpConfederationPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3)
)
if mibBuilder.loadTexts:
    juniBgpConfederationPeerTable.setStatus("deprecated")
_JuniBgpConfederationPeerEntry_Object = MibTableRow
juniBgpConfederationPeerEntry = _JuniBgpConfederationPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3, 1)
)
juniBgpConfederationPeerEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpConfederationPeerAsNumber"),
)
if mibBuilder.loadTexts:
    juniBgpConfederationPeerEntry.setStatus("deprecated")


class _JuniBgpConfederationPeerAsNumber_Type(Integer32):
    """Custom type juniBgpConfederationPeerAsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpConfederationPeerAsNumber_Type.__name__ = "Integer32"
_JuniBgpConfederationPeerAsNumber_Object = MibTableColumn
juniBgpConfederationPeerAsNumber = _JuniBgpConfederationPeerAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3, 1, 1),
    _JuniBgpConfederationPeerAsNumber_Type()
)
juniBgpConfederationPeerAsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpConfederationPeerAsNumber.setStatus("deprecated")
_JuniBgpConfederationPeerRowStatus_Type = RowStatus
_JuniBgpConfederationPeerRowStatus_Object = MibTableColumn
juniBgpConfederationPeerRowStatus = _JuniBgpConfederationPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 3, 1, 2),
    _JuniBgpConfederationPeerRowStatus_Type()
)
juniBgpConfederationPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpConfederationPeerRowStatus.setStatus("deprecated")
_JuniBgpPeerTable_Object = MibTable
juniBgpPeerTable = _JuniBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4)
)
if mibBuilder.loadTexts:
    juniBgpPeerTable.setStatus("current")
_JuniBgpPeerEntry_Object = MibTableRow
juniBgpPeerEntry = _JuniBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1)
)
juniBgpPeerEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerRemoteAddress"),
)
if mibBuilder.loadTexts:
    juniBgpPeerEntry.setStatus("current")
_JuniBgpPeerVrfName_Type = JuniVrfName
_JuniBgpPeerVrfName_Object = MibTableColumn
juniBgpPeerVrfName = _JuniBgpPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 1),
    _JuniBgpPeerVrfName_Type()
)
juniBgpPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerVrfName.setStatus("current")
_JuniBgpPeerRemoteAddress_Type = IpAddress
_JuniBgpPeerRemoteAddress_Object = MibTableColumn
juniBgpPeerRemoteAddress = _JuniBgpPeerRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 2),
    _JuniBgpPeerRemoteAddress_Type()
)
juniBgpPeerRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerRemoteAddress.setStatus("current")


class _JuniBgpPeerAdminStatus_Type(Integer32):
    """Custom type juniBgpPeerAdminStatus based on Integer32"""
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


_JuniBgpPeerAdminStatus_Type.__name__ = "Integer32"
_JuniBgpPeerAdminStatus_Object = MibTableColumn
juniBgpPeerAdminStatus = _JuniBgpPeerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 3),
    _JuniBgpPeerAdminStatus_Type()
)
juniBgpPeerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAdminStatus.setStatus("current")


class _JuniBgpPeerState_Type(Integer32):
    """Custom type juniBgpPeerState based on Integer32"""
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


_JuniBgpPeerState_Type.__name__ = "Integer32"
_JuniBgpPeerState_Object = MibTableColumn
juniBgpPeerState = _JuniBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 4),
    _JuniBgpPeerState_Type()
)
juniBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerState.setStatus("current")
_JuniBgpPeerNegotiatedVersion_Type = Integer32
_JuniBgpPeerNegotiatedVersion_Object = MibTableColumn
juniBgpPeerNegotiatedVersion = _JuniBgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 5),
    _JuniBgpPeerNegotiatedVersion_Type()
)
juniBgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerNegotiatedVersion.setStatus("current")
_JuniBgpPeerLocalAddress_Type = IpAddress
_JuniBgpPeerLocalAddress_Object = MibTableColumn
juniBgpPeerLocalAddress = _JuniBgpPeerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 6),
    _JuniBgpPeerLocalAddress_Type()
)
juniBgpPeerLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerLocalAddress.setStatus("current")
_JuniBgpPeerLocalAddressMask_Type = IpAddress
_JuniBgpPeerLocalAddressMask_Object = MibTableColumn
juniBgpPeerLocalAddressMask = _JuniBgpPeerLocalAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 7),
    _JuniBgpPeerLocalAddressMask_Type()
)
juniBgpPeerLocalAddressMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerLocalAddressMask.setStatus("current")


class _JuniBgpPeerLocalPort_Type(Integer32):
    """Custom type juniBgpPeerLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerLocalPort_Type.__name__ = "Integer32"
_JuniBgpPeerLocalPort_Object = MibTableColumn
juniBgpPeerLocalPort = _JuniBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 8),
    _JuniBgpPeerLocalPort_Type()
)
juniBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerLocalPort.setStatus("current")


class _JuniBgpPeerRemoteAsNumber_Type(Integer32):
    """Custom type juniBgpPeerRemoteAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerRemoteAsNumber_Type.__name__ = "Integer32"
_JuniBgpPeerRemoteAsNumber_Object = MibTableColumn
juniBgpPeerRemoteAsNumber = _JuniBgpPeerRemoteAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 9),
    _JuniBgpPeerRemoteAsNumber_Type()
)
juniBgpPeerRemoteAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerRemoteAsNumber.setStatus("deprecated")


class _JuniBgpPeerRemotePort_Type(Integer32):
    """Custom type juniBgpPeerRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerRemotePort_Type.__name__ = "Integer32"
_JuniBgpPeerRemotePort_Object = MibTableColumn
juniBgpPeerRemotePort = _JuniBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 10),
    _JuniBgpPeerRemotePort_Type()
)
juniBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerRemotePort.setStatus("current")
_JuniBgpPeerInUpdates_Type = Counter32
_JuniBgpPeerInUpdates_Object = MibTableColumn
juniBgpPeerInUpdates = _JuniBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 11),
    _JuniBgpPeerInUpdates_Type()
)
juniBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerInUpdates.setStatus("current")
_JuniBgpPeerOutUpdates_Type = Counter32
_JuniBgpPeerOutUpdates_Object = MibTableColumn
juniBgpPeerOutUpdates = _JuniBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 12),
    _JuniBgpPeerOutUpdates_Type()
)
juniBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerOutUpdates.setStatus("current")
_JuniBgpPeerInTotalMessages_Type = Counter32
_JuniBgpPeerInTotalMessages_Object = MibTableColumn
juniBgpPeerInTotalMessages = _JuniBgpPeerInTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 13),
    _JuniBgpPeerInTotalMessages_Type()
)
juniBgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerInTotalMessages.setStatus("current")
_JuniBgpPeerOutTotalMessages_Type = Counter32
_JuniBgpPeerOutTotalMessages_Object = MibTableColumn
juniBgpPeerOutTotalMessages = _JuniBgpPeerOutTotalMessages_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 14),
    _JuniBgpPeerOutTotalMessages_Type()
)
juniBgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerOutTotalMessages.setStatus("current")


class _JuniBgpPeerLastErrorCode_Type(OctetString):
    """Custom type juniBgpPeerLastErrorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_JuniBgpPeerLastErrorCode_Type.__name__ = "OctetString"
_JuniBgpPeerLastErrorCode_Object = MibTableColumn
juniBgpPeerLastErrorCode = _JuniBgpPeerLastErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 15),
    _JuniBgpPeerLastErrorCode_Type()
)
juniBgpPeerLastErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerLastErrorCode.setStatus("current")
_JuniBgpPeerLastResetReason_Type = DisplayString
_JuniBgpPeerLastResetReason_Object = MibTableColumn
juniBgpPeerLastResetReason = _JuniBgpPeerLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 16),
    _JuniBgpPeerLastResetReason_Type()
)
juniBgpPeerLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerLastResetReason.setStatus("current")
_JuniBgpPeerFsmEstablishedTransitions_Type = Counter32
_JuniBgpPeerFsmEstablishedTransitions_Object = MibTableColumn
juniBgpPeerFsmEstablishedTransitions = _JuniBgpPeerFsmEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 17),
    _JuniBgpPeerFsmEstablishedTransitions_Type()
)
juniBgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerFsmEstablishedTransitions.setStatus("current")
_JuniBgpPeerFsmEstablishedTime_Type = Gauge32
_JuniBgpPeerFsmEstablishedTime_Object = MibTableColumn
juniBgpPeerFsmEstablishedTime = _JuniBgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 18),
    _JuniBgpPeerFsmEstablishedTime_Type()
)
juniBgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerFsmEstablishedTime.setUnits("seconds")


class _JuniBgpPeerRetryInterval_Type(Integer32):
    """Custom type juniBgpPeerRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerRetryInterval_Type.__name__ = "Integer32"
_JuniBgpPeerRetryInterval_Object = MibTableColumn
juniBgpPeerRetryInterval = _JuniBgpPeerRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 19),
    _JuniBgpPeerRetryInterval_Type()
)
juniBgpPeerRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerRetryInterval.setUnits("seconds")


class _JuniBgpPeerHoldTime_Type(Integer32):
    """Custom type juniBgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JuniBgpPeerHoldTime_Type.__name__ = "Integer32"
_JuniBgpPeerHoldTime_Object = MibTableColumn
juniBgpPeerHoldTime = _JuniBgpPeerHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 20),
    _JuniBgpPeerHoldTime_Type()
)
juniBgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerHoldTime.setUnits("seconds")


class _JuniBgpPeerKeepAliveInterval_Type(Integer32):
    """Custom type juniBgpPeerKeepAliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_JuniBgpPeerKeepAliveInterval_Type.__name__ = "Integer32"
_JuniBgpPeerKeepAliveInterval_Object = MibTableColumn
juniBgpPeerKeepAliveInterval = _JuniBgpPeerKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 21),
    _JuniBgpPeerKeepAliveInterval_Type()
)
juniBgpPeerKeepAliveInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerKeepAliveInterval.setUnits("seconds")


class _JuniBgpPeerConfigHoldTime_Type(Integer32):
    """Custom type juniBgpPeerConfigHoldTime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JuniBgpPeerConfigHoldTime_Type.__name__ = "Integer32"
_JuniBgpPeerConfigHoldTime_Object = MibTableColumn
juniBgpPeerConfigHoldTime = _JuniBgpPeerConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 22),
    _JuniBgpPeerConfigHoldTime_Type()
)
juniBgpPeerConfigHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerConfigHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerConfigHoldTime.setUnits("seconds")


class _JuniBgpPeerConfigKeepAliveInterval_Type(Integer32):
    """Custom type juniBgpPeerConfigKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_JuniBgpPeerConfigKeepAliveInterval_Type.__name__ = "Integer32"
_JuniBgpPeerConfigKeepAliveInterval_Object = MibTableColumn
juniBgpPeerConfigKeepAliveInterval = _JuniBgpPeerConfigKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 23),
    _JuniBgpPeerConfigKeepAliveInterval_Type()
)
juniBgpPeerConfigKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerConfigKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerConfigKeepAliveInterval.setUnits("seconds")


class _JuniBgpPeerAsOriginationInterval_Type(Integer32):
    """Custom type juniBgpPeerAsOriginationInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerAsOriginationInterval_Type.__name__ = "Integer32"
_JuniBgpPeerAsOriginationInterval_Object = MibTableColumn
juniBgpPeerAsOriginationInterval = _JuniBgpPeerAsOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 24),
    _JuniBgpPeerAsOriginationInterval_Type()
)
juniBgpPeerAsOriginationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAsOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerAsOriginationInterval.setUnits("seconds")


class _JuniBgpPeerAdvertisementInterval_Type(Integer32):
    """Custom type juniBgpPeerAdvertisementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerAdvertisementInterval_Type.__name__ = "Integer32"
_JuniBgpPeerAdvertisementInterval_Object = MibTableColumn
juniBgpPeerAdvertisementInterval = _JuniBgpPeerAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 25),
    _JuniBgpPeerAdvertisementInterval_Type()
)
juniBgpPeerAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerAdvertisementInterval.setUnits("seconds")
_JuniBgpPeerInUpdateElapsedTime_Type = Gauge32
_JuniBgpPeerInUpdateElapsedTime_Object = MibTableColumn
juniBgpPeerInUpdateElapsedTime = _JuniBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 26),
    _JuniBgpPeerInUpdateElapsedTime_Type()
)
juniBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerInUpdateElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerInUpdateElapsedTime.setUnits("seconds")


class _JuniBgpPeerDescription_Type(DisplayString):
    """Custom type juniBgpPeerDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniBgpPeerDescription_Type.__name__ = "DisplayString"
_JuniBgpPeerDescription_Object = MibTableColumn
juniBgpPeerDescription = _JuniBgpPeerDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 27),
    _JuniBgpPeerDescription_Type()
)
juniBgpPeerDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerDescription.setStatus("current")
_JuniBgpPeerRemoteIdentifier_Type = IpAddress
_JuniBgpPeerRemoteIdentifier_Object = MibTableColumn
juniBgpPeerRemoteIdentifier = _JuniBgpPeerRemoteIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 28),
    _JuniBgpPeerRemoteIdentifier_Type()
)
juniBgpPeerRemoteIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerRemoteIdentifier.setStatus("current")


class _JuniBgpPeerWeight_Type(Unsigned32):
    """Custom type juniBgpPeerWeight based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerWeight_Object = MibTableColumn
juniBgpPeerWeight = _JuniBgpPeerWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 29),
    _JuniBgpPeerWeight_Type()
)
juniBgpPeerWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerWeight.setStatus("current")


class _JuniBgpPeerEbgpMultihop_Type(TruthValue):
    """Custom type juniBgpPeerEbgpMultihop based on TruthValue"""


_JuniBgpPeerEbgpMultihop_Object = MibTableColumn
juniBgpPeerEbgpMultihop = _JuniBgpPeerEbgpMultihop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 30),
    _JuniBgpPeerEbgpMultihop_Type()
)
juniBgpPeerEbgpMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerEbgpMultihop.setStatus("current")


class _JuniBgpPeerEbgpMultihopTtl_Type(Integer32):
    """Custom type juniBgpPeerEbgpMultihopTtl based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpPeerEbgpMultihopTtl_Type.__name__ = "Integer32"
_JuniBgpPeerEbgpMultihopTtl_Object = MibTableColumn
juniBgpPeerEbgpMultihopTtl = _JuniBgpPeerEbgpMultihopTtl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 31),
    _JuniBgpPeerEbgpMultihopTtl_Type()
)
juniBgpPeerEbgpMultihopTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerEbgpMultihopTtl.setStatus("current")


class _JuniBgpPeerUpdateSource_Type(IpAddress):
    """Custom type juniBgpPeerUpdateSource based on IpAddress"""
    defaultValue = 0


_JuniBgpPeerUpdateSource_Object = MibTableColumn
juniBgpPeerUpdateSource = _JuniBgpPeerUpdateSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 32),
    _JuniBgpPeerUpdateSource_Type()
)
juniBgpPeerUpdateSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerUpdateSource.setStatus("current")


class _JuniBgpPeerMd5Password_Type(OctetString):
    """Custom type juniBgpPeerMd5Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerMd5Password_Type.__name__ = "OctetString"
_JuniBgpPeerMd5Password_Object = MibTableColumn
juniBgpPeerMd5Password = _JuniBgpPeerMd5Password_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 33),
    _JuniBgpPeerMd5Password_Type()
)
juniBgpPeerMd5Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerMd5Password.setStatus("current")


class _JuniBgpPeerMaxUpdateSize_Type(Unsigned32):
    """Custom type juniBgpPeerMaxUpdateSize based on Unsigned32"""
    defaultValue = 4096


_JuniBgpPeerMaxUpdateSize_Object = MibTableColumn
juniBgpPeerMaxUpdateSize = _JuniBgpPeerMaxUpdateSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 34),
    _JuniBgpPeerMaxUpdateSize_Type()
)
juniBgpPeerMaxUpdateSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerMaxUpdateSize.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerMaxUpdateSize.setUnits("bytes")


class _JuniBgpPeerType_Type(Integer32):
    """Custom type juniBgpPeerType based on Integer32"""
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


_JuniBgpPeerType_Type.__name__ = "Integer32"
_JuniBgpPeerType_Object = MibTableColumn
juniBgpPeerType = _JuniBgpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 35),
    _JuniBgpPeerType_Type()
)
juniBgpPeerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerType.setStatus("current")
_JuniBgpPeerReceivedCapabilitiesOption_Type = TruthValue
_JuniBgpPeerReceivedCapabilitiesOption_Object = MibTableColumn
juniBgpPeerReceivedCapabilitiesOption = _JuniBgpPeerReceivedCapabilitiesOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 36),
    _JuniBgpPeerReceivedCapabilitiesOption_Type()
)
juniBgpPeerReceivedCapabilitiesOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilitiesOption.setStatus("current")
_JuniBgpPeerReceivedCapabilityMultiProtocol_Type = TruthValue
_JuniBgpPeerReceivedCapabilityMultiProtocol_Object = MibTableColumn
juniBgpPeerReceivedCapabilityMultiProtocol = _JuniBgpPeerReceivedCapabilityMultiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 37),
    _JuniBgpPeerReceivedCapabilityMultiProtocol_Type()
)
juniBgpPeerReceivedCapabilityMultiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilityMultiProtocol.setStatus("current")
_JuniBgpPeerReceivedCapabilityRouteRefresh_Type = TruthValue
_JuniBgpPeerReceivedCapabilityRouteRefresh_Object = MibTableColumn
juniBgpPeerReceivedCapabilityRouteRefresh = _JuniBgpPeerReceivedCapabilityRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 38),
    _JuniBgpPeerReceivedCapabilityRouteRefresh_Type()
)
juniBgpPeerReceivedCapabilityRouteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilityRouteRefresh.setStatus("current")
_JuniBgpPeerReceivedCapabilityRouteRefreshCisco_Type = TruthValue
_JuniBgpPeerReceivedCapabilityRouteRefreshCisco_Object = MibTableColumn
juniBgpPeerReceivedCapabilityRouteRefreshCisco = _JuniBgpPeerReceivedCapabilityRouteRefreshCisco_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 39),
    _JuniBgpPeerReceivedCapabilityRouteRefreshCisco_Type()
)
juniBgpPeerReceivedCapabilityRouteRefreshCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilityRouteRefreshCisco.setStatus("current")


class _JuniBgpPeerResetConnectionType_Type(JuniBgpResetConnectionType):
    """Custom type juniBgpPeerResetConnectionType based on JuniBgpResetConnectionType"""


_JuniBgpPeerResetConnectionType_Object = MibTableColumn
juniBgpPeerResetConnectionType = _JuniBgpPeerResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 40),
    _JuniBgpPeerResetConnectionType_Type()
)
juniBgpPeerResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerResetConnectionType.setStatus("current")
_JuniBgpPeerRowStatus_Type = RowStatus
_JuniBgpPeerRowStatus_Object = MibTableColumn
juniBgpPeerRowStatus = _JuniBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 41),
    _JuniBgpPeerRowStatus_Type()
)
juniBgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerRowStatus.setStatus("current")


class _JuniBgpPeerLocalAsNumber_Type(Integer32):
    """Custom type juniBgpPeerLocalAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerLocalAsNumber_Type.__name__ = "Integer32"
_JuniBgpPeerLocalAsNumber_Object = MibTableColumn
juniBgpPeerLocalAsNumber = _JuniBgpPeerLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 42),
    _JuniBgpPeerLocalAsNumber_Type()
)
juniBgpPeerLocalAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerLocalAsNumber.setStatus("deprecated")


class _JuniBgpPeerFourOctetRemoteAsNumber_Type(JuniBgpFourOctetAsNumber):
    """Custom type juniBgpPeerFourOctetRemoteAsNumber based on JuniBgpFourOctetAsNumber"""
    defaultValue = 0


_JuniBgpPeerFourOctetRemoteAsNumber_Object = MibTableColumn
juniBgpPeerFourOctetRemoteAsNumber = _JuniBgpPeerFourOctetRemoteAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 43),
    _JuniBgpPeerFourOctetRemoteAsNumber_Type()
)
juniBgpPeerFourOctetRemoteAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerFourOctetRemoteAsNumber.setStatus("current")


class _JuniBgpPeerFourOctetLocalAsNumber_Type(JuniBgpFourOctetAsNumber):
    """Custom type juniBgpPeerFourOctetLocalAsNumber based on JuniBgpFourOctetAsNumber"""
    defaultValue = 0


_JuniBgpPeerFourOctetLocalAsNumber_Object = MibTableColumn
juniBgpPeerFourOctetLocalAsNumber = _JuniBgpPeerFourOctetLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 44),
    _JuniBgpPeerFourOctetLocalAsNumber_Type()
)
juniBgpPeerFourOctetLocalAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerFourOctetLocalAsNumber.setStatus("current")
_JuniBgpPeerReceivedCapabilityFourOctetAsNumbers_Type = TruthValue
_JuniBgpPeerReceivedCapabilityFourOctetAsNumbers_Object = MibTableColumn
juniBgpPeerReceivedCapabilityFourOctetAsNumbers = _JuniBgpPeerReceivedCapabilityFourOctetAsNumbers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 45),
    _JuniBgpPeerReceivedCapabilityFourOctetAsNumbers_Type()
)
juniBgpPeerReceivedCapabilityFourOctetAsNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilityFourOctetAsNumbers.setStatus("current")
_JuniBgpPeerReceivedCapabilityDynamicCapabilityNeg_Type = TruthValue
_JuniBgpPeerReceivedCapabilityDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerReceivedCapabilityDynamicCapabilityNeg = _JuniBgpPeerReceivedCapabilityDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 46),
    _JuniBgpPeerReceivedCapabilityDynamicCapabilityNeg_Type()
)
juniBgpPeerReceivedCapabilityDynamicCapabilityNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilityDynamicCapabilityNeg.setStatus("current")


class _JuniBgpPeerShouldAdvertiseCapabilitiesOption_Type(TruthValue):
    """Custom type juniBgpPeerShouldAdvertiseCapabilitiesOption based on TruthValue"""


_JuniBgpPeerShouldAdvertiseCapabilitiesOption_Object = MibTableColumn
juniBgpPeerShouldAdvertiseCapabilitiesOption = _JuniBgpPeerShouldAdvertiseCapabilitiesOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 47),
    _JuniBgpPeerShouldAdvertiseCapabilitiesOption_Type()
)
juniBgpPeerShouldAdvertiseCapabilitiesOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerShouldAdvertiseCapabilitiesOption.setStatus("current")


class _JuniBgpPeerShouldAdvertiseCapabilityRouteRefresh_Type(TruthValue):
    """Custom type juniBgpPeerShouldAdvertiseCapabilityRouteRefresh based on TruthValue"""


_JuniBgpPeerShouldAdvertiseCapabilityRouteRefresh_Object = MibTableColumn
juniBgpPeerShouldAdvertiseCapabilityRouteRefresh = _JuniBgpPeerShouldAdvertiseCapabilityRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 48),
    _JuniBgpPeerShouldAdvertiseCapabilityRouteRefresh_Type()
)
juniBgpPeerShouldAdvertiseCapabilityRouteRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerShouldAdvertiseCapabilityRouteRefresh.setStatus("current")


class _JuniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco_Type(TruthValue):
    """Custom type juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco based on TruthValue"""


_JuniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco_Object = MibTableColumn
juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco = _JuniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 49),
    _JuniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco_Type()
)
juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco.setStatus("current")


class _JuniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers_Type(TruthValue):
    """Custom type juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers based on TruthValue"""


_JuniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers_Object = MibTableColumn
juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers = _JuniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 50),
    _JuniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers_Type()
)
juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers.setStatus("current")


class _JuniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg_Type(TruthValue):
    """Custom type juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg based on TruthValue"""


_JuniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg = _JuniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 51),
    _JuniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg_Type()
)
juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg.setStatus("current")
_JuniBgpPeerSentCapabilitiesOption_Type = TruthValue
_JuniBgpPeerSentCapabilitiesOption_Object = MibTableColumn
juniBgpPeerSentCapabilitiesOption = _JuniBgpPeerSentCapabilitiesOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 52),
    _JuniBgpPeerSentCapabilitiesOption_Type()
)
juniBgpPeerSentCapabilitiesOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilitiesOption.setStatus("current")
_JuniBgpPeerSentCapabilityMultiProtocol_Type = TruthValue
_JuniBgpPeerSentCapabilityMultiProtocol_Object = MibTableColumn
juniBgpPeerSentCapabilityMultiProtocol = _JuniBgpPeerSentCapabilityMultiProtocol_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 53),
    _JuniBgpPeerSentCapabilityMultiProtocol_Type()
)
juniBgpPeerSentCapabilityMultiProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilityMultiProtocol.setStatus("current")
_JuniBgpPeerSentCapabilityRouteRefresh_Type = TruthValue
_JuniBgpPeerSentCapabilityRouteRefresh_Object = MibTableColumn
juniBgpPeerSentCapabilityRouteRefresh = _JuniBgpPeerSentCapabilityRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 54),
    _JuniBgpPeerSentCapabilityRouteRefresh_Type()
)
juniBgpPeerSentCapabilityRouteRefresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilityRouteRefresh.setStatus("current")
_JuniBgpPeerSentCapabilityRouteRefreshCisco_Type = TruthValue
_JuniBgpPeerSentCapabilityRouteRefreshCisco_Object = MibTableColumn
juniBgpPeerSentCapabilityRouteRefreshCisco = _JuniBgpPeerSentCapabilityRouteRefreshCisco_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 55),
    _JuniBgpPeerSentCapabilityRouteRefreshCisco_Type()
)
juniBgpPeerSentCapabilityRouteRefreshCisco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilityRouteRefreshCisco.setStatus("current")
_JuniBgpPeerSentCapabilityFourOctetAsNumbers_Type = TruthValue
_JuniBgpPeerSentCapabilityFourOctetAsNumbers_Object = MibTableColumn
juniBgpPeerSentCapabilityFourOctetAsNumbers = _JuniBgpPeerSentCapabilityFourOctetAsNumbers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 56),
    _JuniBgpPeerSentCapabilityFourOctetAsNumbers_Type()
)
juniBgpPeerSentCapabilityFourOctetAsNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilityFourOctetAsNumbers.setStatus("current")
_JuniBgpPeerSentCapabilityDynamicCapabilityNeg_Type = TruthValue
_JuniBgpPeerSentCapabilityDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerSentCapabilityDynamicCapabilityNeg = _JuniBgpPeerSentCapabilityDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 57),
    _JuniBgpPeerSentCapabilityDynamicCapabilityNeg_Type()
)
juniBgpPeerSentCapabilityDynamicCapabilityNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilityDynamicCapabilityNeg.setStatus("current")
_JuniBgpPeerReceivedUnsupportedOptionalParameterNotification_Type = TruthValue
_JuniBgpPeerReceivedUnsupportedOptionalParameterNotification_Object = MibTableColumn
juniBgpPeerReceivedUnsupportedOptionalParameterNotification = _JuniBgpPeerReceivedUnsupportedOptionalParameterNotification_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 58),
    _JuniBgpPeerReceivedUnsupportedOptionalParameterNotification_Type()
)
juniBgpPeerReceivedUnsupportedOptionalParameterNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedUnsupportedOptionalParameterNotification.setStatus("current")
_JuniBgpPeerReceivedUnsupportedCapabilityNotification_Type = TruthValue
_JuniBgpPeerReceivedUnsupportedCapabilityNotification_Object = MibTableColumn
juniBgpPeerReceivedUnsupportedCapabilityNotification = _JuniBgpPeerReceivedUnsupportedCapabilityNotification_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 59),
    _JuniBgpPeerReceivedUnsupportedCapabilityNotification_Type()
)
juniBgpPeerReceivedUnsupportedCapabilityNotification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedUnsupportedCapabilityNotification.setStatus("current")


class _JuniBgpPeerUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpPeerUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpPeerAdminStatus", 0),
          ("juniBgpPeerAdvertisementInterval", 5),
          ("juniBgpPeerAsOriginationInterval", 4),
          ("juniBgpPeerBfdEnabled", 27),
          ("juniBgpPeerBfdMinReceiveInterval", 29),
          ("juniBgpPeerBfdMinTransmitInterval", 28),
          ("juniBgpPeerBfdMultiplier", 30),
          ("juniBgpPeerConfigHoldTime", 2),
          ("juniBgpPeerConfigKeepAliveInterval", 3),
          ("juniBgpPeerDescription", 6),
          ("juniBgpPeerEbgpMultihop", 8),
          ("juniBgpPeerEbgpMultihopTtl", 9),
          ("juniBgpPeerFourOctetLocalAsNumber", 14),
          ("juniBgpPeerFourOctetRemoteAsNumber", 13),
          ("juniBgpPeerGracefulRestartRestartTime", 25),
          ("juniBgpPeerGracefulRestartStalePathsTime", 26),
          ("juniBgpPeerIbgpSinglehop", 31),
          ("juniBgpPeerLenient", 21),
          ("juniBgpPeerMaxUpdateSize", 12),
          ("juniBgpPeerMd5Password", 11),
          ("juniBgpPeerPassive", 23),
          ("juniBgpPeerRetryInterval", 1),
          ("juniBgpPeerShouldAdvertiseCapabilitiesOption", 15),
          ("juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg", 19),
          ("juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers", 18),
          ("juniBgpPeerShouldAdvertiseCapabilityGracefulRestart", 24),
          ("juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg", 22),
          ("juniBgpPeerShouldAdvertiseCapabilityRouteRefresh", 16),
          ("juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco", 17),
          ("juniBgpPeerSiteOfOrigin", 20),
          ("juniBgpPeerUpdateSource", 10),
          ("juniBgpPeerWeight", 7))
    )

_JuniBgpPeerUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpPeerUnconfiguredAttributes_Object = MibTableColumn
juniBgpPeerUnconfiguredAttributes = _JuniBgpPeerUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 60),
    _JuniBgpPeerUnconfiguredAttributes_Type()
)
juniBgpPeerUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerUnconfiguredAttributes.setStatus("current")


class _JuniBgpPeerSiteOfOrigin_Type(OctetString):
    """Custom type juniBgpPeerSiteOfOrigin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniBgpPeerSiteOfOrigin_Type.__name__ = "OctetString"
_JuniBgpPeerSiteOfOrigin_Object = MibTableColumn
juniBgpPeerSiteOfOrigin = _JuniBgpPeerSiteOfOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 61),
    _JuniBgpPeerSiteOfOrigin_Type()
)
juniBgpPeerSiteOfOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerSiteOfOrigin.setStatus("current")
_JuniBgpPeerLenient_Type = TruthValue
_JuniBgpPeerLenient_Object = MibTableColumn
juniBgpPeerLenient = _JuniBgpPeerLenient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 62),
    _JuniBgpPeerLenient_Type()
)
juniBgpPeerLenient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerLenient.setStatus("current")
_JuniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg_Type = TruthValue
_JuniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg = _JuniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 63),
    _JuniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg_Type()
)
juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg.setStatus("current")


class _JuniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Type(TruthValue):
    """Custom type juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg based on TruthValue"""


_JuniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg = _JuniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 64),
    _JuniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Type()
)
juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg.setStatus("current")
_JuniBgpPeerSentCapabilityOldDynamicCapabilityNeg_Type = TruthValue
_JuniBgpPeerSentCapabilityOldDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerSentCapabilityOldDynamicCapabilityNeg = _JuniBgpPeerSentCapabilityOldDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 65),
    _JuniBgpPeerSentCapabilityOldDynamicCapabilityNeg_Type()
)
juniBgpPeerSentCapabilityOldDynamicCapabilityNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilityOldDynamicCapabilityNeg.setStatus("current")


class _JuniBgpPeerPassive_Type(TruthValue):
    """Custom type juniBgpPeerPassive based on TruthValue"""


_JuniBgpPeerPassive_Object = MibTableColumn
juniBgpPeerPassive = _JuniBgpPeerPassive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 66),
    _JuniBgpPeerPassive_Type()
)
juniBgpPeerPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerPassive.setStatus("current")
_JuniBgpPeerDynamic_Type = TruthValue
_JuniBgpPeerDynamic_Object = MibTableColumn
juniBgpPeerDynamic = _JuniBgpPeerDynamic_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 67),
    _JuniBgpPeerDynamic_Type()
)
juniBgpPeerDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerDynamic.setStatus("current")


class _JuniBgpPeerShouldAdvertiseCapabilityGracefulRestart_Type(TruthValue):
    """Custom type juniBgpPeerShouldAdvertiseCapabilityGracefulRestart based on TruthValue"""


_JuniBgpPeerShouldAdvertiseCapabilityGracefulRestart_Object = MibTableColumn
juniBgpPeerShouldAdvertiseCapabilityGracefulRestart = _JuniBgpPeerShouldAdvertiseCapabilityGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 68),
    _JuniBgpPeerShouldAdvertiseCapabilityGracefulRestart_Type()
)
juniBgpPeerShouldAdvertiseCapabilityGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerShouldAdvertiseCapabilityGracefulRestart.setStatus("current")
_JuniBgpPeerSentCapabilityGracefulRestart_Type = TruthValue
_JuniBgpPeerSentCapabilityGracefulRestart_Object = MibTableColumn
juniBgpPeerSentCapabilityGracefulRestart = _JuniBgpPeerSentCapabilityGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 69),
    _JuniBgpPeerSentCapabilityGracefulRestart_Type()
)
juniBgpPeerSentCapabilityGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentCapabilityGracefulRestart.setStatus("current")
_JuniBgpPeerReceivedCapabilityGracefulRestart_Type = TruthValue
_JuniBgpPeerReceivedCapabilityGracefulRestart_Object = MibTableColumn
juniBgpPeerReceivedCapabilityGracefulRestart = _JuniBgpPeerReceivedCapabilityGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 70),
    _JuniBgpPeerReceivedCapabilityGracefulRestart_Type()
)
juniBgpPeerReceivedCapabilityGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedCapabilityGracefulRestart.setStatus("current")


class _JuniBgpPeerGracefulRestartRestartTime_Type(Integer32):
    """Custom type juniBgpPeerGracefulRestartRestartTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuniBgpPeerGracefulRestartRestartTime_Type.__name__ = "Integer32"
_JuniBgpPeerGracefulRestartRestartTime_Object = MibTableColumn
juniBgpPeerGracefulRestartRestartTime = _JuniBgpPeerGracefulRestartRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 71),
    _JuniBgpPeerGracefulRestartRestartTime_Type()
)
juniBgpPeerGracefulRestartRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGracefulRestartRestartTime.setStatus("current")


class _JuniBgpPeerGracefulRestartStalePathsTime_Type(Integer32):
    """Custom type juniBgpPeerGracefulRestartStalePathsTime based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuniBgpPeerGracefulRestartStalePathsTime_Type.__name__ = "Integer32"
_JuniBgpPeerGracefulRestartStalePathsTime_Object = MibTableColumn
juniBgpPeerGracefulRestartStalePathsTime = _JuniBgpPeerGracefulRestartStalePathsTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 72),
    _JuniBgpPeerGracefulRestartStalePathsTime_Type()
)
juniBgpPeerGracefulRestartStalePathsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGracefulRestartStalePathsTime.setStatus("current")
_JuniBgpPeerSentGracefulRestartRestartState_Type = TruthValue
_JuniBgpPeerSentGracefulRestartRestartState_Object = MibTableColumn
juniBgpPeerSentGracefulRestartRestartState = _JuniBgpPeerSentGracefulRestartRestartState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 73),
    _JuniBgpPeerSentGracefulRestartRestartState_Type()
)
juniBgpPeerSentGracefulRestartRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentGracefulRestartRestartState.setStatus("current")
_JuniBgpPeerReceivedGracefulRestartRestartState_Type = TruthValue
_JuniBgpPeerReceivedGracefulRestartRestartState_Object = MibTableColumn
juniBgpPeerReceivedGracefulRestartRestartState = _JuniBgpPeerReceivedGracefulRestartRestartState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 74),
    _JuniBgpPeerReceivedGracefulRestartRestartState_Type()
)
juniBgpPeerReceivedGracefulRestartRestartState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedGracefulRestartRestartState.setStatus("current")


class _JuniBgpPeerSentGracefulRestartRestartTime_Type(Integer32):
    """Custom type juniBgpPeerSentGracefulRestartRestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_JuniBgpPeerSentGracefulRestartRestartTime_Type.__name__ = "Integer32"
_JuniBgpPeerSentGracefulRestartRestartTime_Object = MibTableColumn
juniBgpPeerSentGracefulRestartRestartTime = _JuniBgpPeerSentGracefulRestartRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 75),
    _JuniBgpPeerSentGracefulRestartRestartTime_Type()
)
juniBgpPeerSentGracefulRestartRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerSentGracefulRestartRestartTime.setStatus("current")


class _JuniBgpPeerReceivedGracefulRestartRestartTime_Type(Integer32):
    """Custom type juniBgpPeerReceivedGracefulRestartRestartTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerReceivedGracefulRestartRestartTime_Type.__name__ = "Integer32"
_JuniBgpPeerReceivedGracefulRestartRestartTime_Object = MibTableColumn
juniBgpPeerReceivedGracefulRestartRestartTime = _JuniBgpPeerReceivedGracefulRestartRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 76),
    _JuniBgpPeerReceivedGracefulRestartRestartTime_Type()
)
juniBgpPeerReceivedGracefulRestartRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerReceivedGracefulRestartRestartTime.setStatus("current")


class _JuniBgpPeerTimeUntilGracefulRestartRestartTimerExpires_Type(Integer32):
    """Custom type juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerTimeUntilGracefulRestartRestartTimerExpires_Type.__name__ = "Integer32"
_JuniBgpPeerTimeUntilGracefulRestartRestartTimerExpires_Object = MibTableColumn
juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires = _JuniBgpPeerTimeUntilGracefulRestartRestartTimerExpires_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 77),
    _JuniBgpPeerTimeUntilGracefulRestartRestartTimerExpires_Type()
)
juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires.setStatus("current")


class _JuniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires_Type(Integer32):
    """Custom type juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_JuniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires_Type.__name__ = "Integer32"
_JuniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires_Object = MibTableColumn
juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires = _JuniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 78),
    _JuniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires_Type()
)
juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires.setStatus("current")


class _JuniBgpPeerBfdEnabled_Type(TruthValue):
    """Custom type juniBgpPeerBfdEnabled based on TruthValue"""


_JuniBgpPeerBfdEnabled_Object = MibTableColumn
juniBgpPeerBfdEnabled = _JuniBgpPeerBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 79),
    _JuniBgpPeerBfdEnabled_Type()
)
juniBgpPeerBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerBfdEnabled.setStatus("current")


class _JuniBgpPeerBfdMinTransmitInterval_Type(Integer32):
    """Custom type juniBgpPeerBfdMinTransmitInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniBgpPeerBfdMinTransmitInterval_Type.__name__ = "Integer32"
_JuniBgpPeerBfdMinTransmitInterval_Object = MibTableColumn
juniBgpPeerBfdMinTransmitInterval = _JuniBgpPeerBfdMinTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 80),
    _JuniBgpPeerBfdMinTransmitInterval_Type()
)
juniBgpPeerBfdMinTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerBfdMinTransmitInterval.setStatus("current")


class _JuniBgpPeerBfdMinReceiveInterval_Type(Integer32):
    """Custom type juniBgpPeerBfdMinReceiveInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniBgpPeerBfdMinReceiveInterval_Type.__name__ = "Integer32"
_JuniBgpPeerBfdMinReceiveInterval_Object = MibTableColumn
juniBgpPeerBfdMinReceiveInterval = _JuniBgpPeerBfdMinReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 81),
    _JuniBgpPeerBfdMinReceiveInterval_Type()
)
juniBgpPeerBfdMinReceiveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerBfdMinReceiveInterval.setStatus("current")


class _JuniBgpPeerBfdMultiplier_Type(Integer32):
    """Custom type juniBgpPeerBfdMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpPeerBfdMultiplier_Type.__name__ = "Integer32"
_JuniBgpPeerBfdMultiplier_Object = MibTableColumn
juniBgpPeerBfdMultiplier = _JuniBgpPeerBfdMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 82),
    _JuniBgpPeerBfdMultiplier_Type()
)
juniBgpPeerBfdMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerBfdMultiplier.setStatus("current")
_JuniBgpPeerBfdSessionUp_Type = TruthValue
_JuniBgpPeerBfdSessionUp_Object = MibTableColumn
juniBgpPeerBfdSessionUp = _JuniBgpPeerBfdSessionUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 83),
    _JuniBgpPeerBfdSessionUp_Type()
)
juniBgpPeerBfdSessionUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerBfdSessionUp.setStatus("current")
_JuniBgpPeerBfdDetectionTime_Type = Integer32
_JuniBgpPeerBfdDetectionTime_Object = MibTableColumn
juniBgpPeerBfdDetectionTime = _JuniBgpPeerBfdDetectionTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 84),
    _JuniBgpPeerBfdDetectionTime_Type()
)
juniBgpPeerBfdDetectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerBfdDetectionTime.setStatus("current")


class _JuniBgpPeerIbgpSinglehop_Type(TruthValue):
    """Custom type juniBgpPeerIbgpSinglehop based on TruthValue"""


_JuniBgpPeerIbgpSinglehop_Object = MibTableColumn
juniBgpPeerIbgpSinglehop = _JuniBgpPeerIbgpSinglehop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 4, 1, 85),
    _JuniBgpPeerIbgpSinglehop_Type()
)
juniBgpPeerIbgpSinglehop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerIbgpSinglehop.setStatus("current")
_JuniBgpPeerProposedAfiSafiPeerTable_Object = MibTable
juniBgpPeerProposedAfiSafiPeerTable = _JuniBgpPeerProposedAfiSafiPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5)
)
if mibBuilder.loadTexts:
    juniBgpPeerProposedAfiSafiPeerTable.setStatus("current")
_JuniBgpPeerProposedAfiSafiPeerEntry_Object = MibTableRow
juniBgpPeerProposedAfiSafiPeerEntry = _JuniBgpPeerProposedAfiSafiPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1)
)
juniBgpPeerProposedAfiSafiPeerEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerProposedAfiSafiPeerVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerProposedAfiSafiPeerRemoteAddr"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerProposedAfiSafiPeerAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerProposedAfiSafiPeerSafi"),
)
if mibBuilder.loadTexts:
    juniBgpPeerProposedAfiSafiPeerEntry.setStatus("current")
_JuniBgpPeerProposedAfiSafiPeerVrfName_Type = JuniVrfName
_JuniBgpPeerProposedAfiSafiPeerVrfName_Object = MibTableColumn
juniBgpPeerProposedAfiSafiPeerVrfName = _JuniBgpPeerProposedAfiSafiPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 1),
    _JuniBgpPeerProposedAfiSafiPeerVrfName_Type()
)
juniBgpPeerProposedAfiSafiPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerProposedAfiSafiPeerVrfName.setStatus("current")
_JuniBgpPeerProposedAfiSafiPeerRemoteAddr_Type = IpAddress
_JuniBgpPeerProposedAfiSafiPeerRemoteAddr_Object = MibTableColumn
juniBgpPeerProposedAfiSafiPeerRemoteAddr = _JuniBgpPeerProposedAfiSafiPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 2),
    _JuniBgpPeerProposedAfiSafiPeerRemoteAddr_Type()
)
juniBgpPeerProposedAfiSafiPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerProposedAfiSafiPeerRemoteAddr.setStatus("current")
_JuniBgpPeerProposedAfiSafiPeerAfi_Type = JuniBgpAfi
_JuniBgpPeerProposedAfiSafiPeerAfi_Object = MibTableColumn
juniBgpPeerProposedAfiSafiPeerAfi = _JuniBgpPeerProposedAfiSafiPeerAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 3),
    _JuniBgpPeerProposedAfiSafiPeerAfi_Type()
)
juniBgpPeerProposedAfiSafiPeerAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerProposedAfiSafiPeerAfi.setStatus("current")
_JuniBgpPeerProposedAfiSafiPeerSafi_Type = JuniBgpSafi
_JuniBgpPeerProposedAfiSafiPeerSafi_Object = MibTableColumn
juniBgpPeerProposedAfiSafiPeerSafi = _JuniBgpPeerProposedAfiSafiPeerSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 4),
    _JuniBgpPeerProposedAfiSafiPeerSafi_Type()
)
juniBgpPeerProposedAfiSafiPeerSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerProposedAfiSafiPeerSafi.setStatus("current")
_JuniBgpPeerProposedAfiSafiPeerRowStatus_Type = RowStatus
_JuniBgpPeerProposedAfiSafiPeerRowStatus_Object = MibTableColumn
juniBgpPeerProposedAfiSafiPeerRowStatus = _JuniBgpPeerProposedAfiSafiPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 5, 1, 5),
    _JuniBgpPeerProposedAfiSafiPeerRowStatus_Type()
)
juniBgpPeerProposedAfiSafiPeerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerProposedAfiSafiPeerRowStatus.setStatus("current")
_JuniBgpLocalProposedAfiSafiPeerTable_Object = MibTable
juniBgpLocalProposedAfiSafiPeerTable = _JuniBgpLocalProposedAfiSafiPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6)
)
if mibBuilder.loadTexts:
    juniBgpLocalProposedAfiSafiPeerTable.setStatus("current")
_JuniBgpLocalProposedAfiSafiPeerEntry_Object = MibTableRow
juniBgpLocalProposedAfiSafiPeerEntry = _JuniBgpLocalProposedAfiSafiPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1)
)
juniBgpLocalProposedAfiSafiPeerEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpLocalProposedAfiSafiPeerVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpLocalProposedAfiSafiPeerRemoteAddr"),
    (0, "Juniper-BGP-MIB", "juniBgpLocalProposedAfiSafiPeerAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpLocalProposedAfiSafiPeerSafi"),
)
if mibBuilder.loadTexts:
    juniBgpLocalProposedAfiSafiPeerEntry.setStatus("current")
_JuniBgpLocalProposedAfiSafiPeerVrfName_Type = JuniVrfName
_JuniBgpLocalProposedAfiSafiPeerVrfName_Object = MibTableColumn
juniBgpLocalProposedAfiSafiPeerVrfName = _JuniBgpLocalProposedAfiSafiPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 1),
    _JuniBgpLocalProposedAfiSafiPeerVrfName_Type()
)
juniBgpLocalProposedAfiSafiPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpLocalProposedAfiSafiPeerVrfName.setStatus("current")
_JuniBgpLocalProposedAfiSafiPeerRemoteAddr_Type = IpAddress
_JuniBgpLocalProposedAfiSafiPeerRemoteAddr_Object = MibTableColumn
juniBgpLocalProposedAfiSafiPeerRemoteAddr = _JuniBgpLocalProposedAfiSafiPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 2),
    _JuniBgpLocalProposedAfiSafiPeerRemoteAddr_Type()
)
juniBgpLocalProposedAfiSafiPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpLocalProposedAfiSafiPeerRemoteAddr.setStatus("current")
_JuniBgpLocalProposedAfiSafiPeerAfi_Type = JuniBgpAfi
_JuniBgpLocalProposedAfiSafiPeerAfi_Object = MibTableColumn
juniBgpLocalProposedAfiSafiPeerAfi = _JuniBgpLocalProposedAfiSafiPeerAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 3),
    _JuniBgpLocalProposedAfiSafiPeerAfi_Type()
)
juniBgpLocalProposedAfiSafiPeerAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpLocalProposedAfiSafiPeerAfi.setStatus("current")
_JuniBgpLocalProposedAfiSafiPeerSafi_Type = JuniBgpSafi
_JuniBgpLocalProposedAfiSafiPeerSafi_Object = MibTableColumn
juniBgpLocalProposedAfiSafiPeerSafi = _JuniBgpLocalProposedAfiSafiPeerSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 4),
    _JuniBgpLocalProposedAfiSafiPeerSafi_Type()
)
juniBgpLocalProposedAfiSafiPeerSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpLocalProposedAfiSafiPeerSafi.setStatus("current")
_JuniBgpLocalProposedAfiSafiPeerRowStatus_Type = RowStatus
_JuniBgpLocalProposedAfiSafiPeerRowStatus_Object = MibTableColumn
juniBgpLocalProposedAfiSafiPeerRowStatus = _JuniBgpLocalProposedAfiSafiPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 6, 1, 5),
    _JuniBgpLocalProposedAfiSafiPeerRowStatus_Type()
)
juniBgpLocalProposedAfiSafiPeerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpLocalProposedAfiSafiPeerRowStatus.setStatus("current")
_JuniBgpExchangedAfiSafiPeerTable_Object = MibTable
juniBgpExchangedAfiSafiPeerTable = _JuniBgpExchangedAfiSafiPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7)
)
if mibBuilder.loadTexts:
    juniBgpExchangedAfiSafiPeerTable.setStatus("current")
_JuniBgpExchangedAfiSafiPeerEntry_Object = MibTableRow
juniBgpExchangedAfiSafiPeerEntry = _JuniBgpExchangedAfiSafiPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1)
)
juniBgpExchangedAfiSafiPeerEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpExchangedAfiSafiPeerVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpExchangedAfiSafiPeerRemoteAddr"),
    (0, "Juniper-BGP-MIB", "juniBgpExchangedAfiSafiPeerAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpExchangedAfiSafiPeerSafi"),
)
if mibBuilder.loadTexts:
    juniBgpExchangedAfiSafiPeerEntry.setStatus("current")
_JuniBgpExchangedAfiSafiPeerVrfName_Type = JuniVrfName
_JuniBgpExchangedAfiSafiPeerVrfName_Object = MibTableColumn
juniBgpExchangedAfiSafiPeerVrfName = _JuniBgpExchangedAfiSafiPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 1),
    _JuniBgpExchangedAfiSafiPeerVrfName_Type()
)
juniBgpExchangedAfiSafiPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpExchangedAfiSafiPeerVrfName.setStatus("current")
_JuniBgpExchangedAfiSafiPeerRemoteAddr_Type = IpAddress
_JuniBgpExchangedAfiSafiPeerRemoteAddr_Object = MibTableColumn
juniBgpExchangedAfiSafiPeerRemoteAddr = _JuniBgpExchangedAfiSafiPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 2),
    _JuniBgpExchangedAfiSafiPeerRemoteAddr_Type()
)
juniBgpExchangedAfiSafiPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpExchangedAfiSafiPeerRemoteAddr.setStatus("current")
_JuniBgpExchangedAfiSafiPeerAfi_Type = JuniBgpAfi
_JuniBgpExchangedAfiSafiPeerAfi_Object = MibTableColumn
juniBgpExchangedAfiSafiPeerAfi = _JuniBgpExchangedAfiSafiPeerAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 3),
    _JuniBgpExchangedAfiSafiPeerAfi_Type()
)
juniBgpExchangedAfiSafiPeerAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpExchangedAfiSafiPeerAfi.setStatus("current")
_JuniBgpExchangedAfiSafiPeerSafi_Type = JuniBgpSafi
_JuniBgpExchangedAfiSafiPeerSafi_Object = MibTableColumn
juniBgpExchangedAfiSafiPeerSafi = _JuniBgpExchangedAfiSafiPeerSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 4),
    _JuniBgpExchangedAfiSafiPeerSafi_Type()
)
juniBgpExchangedAfiSafiPeerSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpExchangedAfiSafiPeerSafi.setStatus("current")
_JuniBgpExchangedAfiSafiPeerRowStatus_Type = RowStatus
_JuniBgpExchangedAfiSafiPeerRowStatus_Object = MibTableColumn
juniBgpExchangedAfiSafiPeerRowStatus = _JuniBgpExchangedAfiSafiPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 7, 1, 5),
    _JuniBgpExchangedAfiSafiPeerRowStatus_Type()
)
juniBgpExchangedAfiSafiPeerRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpExchangedAfiSafiPeerRowStatus.setStatus("current")
_JuniBgpPeerAddressFamilyTable_Object = MibTable
juniBgpPeerAddressFamilyTable = _JuniBgpPeerAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8)
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyTable.setStatus("current")
_JuniBgpPeerAddressFamilyEntry_Object = MibTableRow
juniBgpPeerAddressFamilyEntry = _JuniBgpPeerAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1)
)
juniBgpPeerAddressFamilyEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilyVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilySafi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemoteAddress"),
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyEntry.setStatus("current")
_JuniBgpPeerAddressFamilyVrfName_Type = JuniVrfName
_JuniBgpPeerAddressFamilyVrfName_Object = MibTableColumn
juniBgpPeerAddressFamilyVrfName = _JuniBgpPeerAddressFamilyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 1),
    _JuniBgpPeerAddressFamilyVrfName_Type()
)
juniBgpPeerAddressFamilyVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyVrfName.setStatus("current")
_JuniBgpPeerAddressFamilyAfi_Type = JuniBgpAfi
_JuniBgpPeerAddressFamilyAfi_Object = MibTableColumn
juniBgpPeerAddressFamilyAfi = _JuniBgpPeerAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 2),
    _JuniBgpPeerAddressFamilyAfi_Type()
)
juniBgpPeerAddressFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyAfi.setStatus("current")
_JuniBgpPeerAddressFamilySafi_Type = JuniBgpSafi
_JuniBgpPeerAddressFamilySafi_Object = MibTableColumn
juniBgpPeerAddressFamilySafi = _JuniBgpPeerAddressFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 3),
    _JuniBgpPeerAddressFamilySafi_Type()
)
juniBgpPeerAddressFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilySafi.setStatus("current")
_JuniBgpPeerAddressFamilyRemoteAddress_Type = IpAddress
_JuniBgpPeerAddressFamilyRemoteAddress_Object = MibTableColumn
juniBgpPeerAddressFamilyRemoteAddress = _JuniBgpPeerAddressFamilyRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 4),
    _JuniBgpPeerAddressFamilyRemoteAddress_Type()
)
juniBgpPeerAddressFamilyRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRemoteAddress.setStatus("current")


class _JuniBgpPeerAddressFamilyPeerGroup_Type(DisplayString):
    """Custom type juniBgpPeerAddressFamilyPeerGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerAddressFamilyPeerGroup_Type.__name__ = "DisplayString"
_JuniBgpPeerAddressFamilyPeerGroup_Object = MibTableColumn
juniBgpPeerAddressFamilyPeerGroup = _JuniBgpPeerAddressFamilyPeerGroup_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 5),
    _JuniBgpPeerAddressFamilyPeerGroup_Type()
)
juniBgpPeerAddressFamilyPeerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyPeerGroup.setStatus("current")


class _JuniBgpPeerAddressFamilyDefaultOriginate_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyDefaultOriginate based on TruthValue"""


_JuniBgpPeerAddressFamilyDefaultOriginate_Object = MibTableColumn
juniBgpPeerAddressFamilyDefaultOriginate = _JuniBgpPeerAddressFamilyDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 6),
    _JuniBgpPeerAddressFamilyDefaultOriginate_Type()
)
juniBgpPeerAddressFamilyDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyDefaultOriginate.setStatus("current")


class _JuniBgpPeerAddressFamilyNextHopSelf_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyNextHopSelf based on TruthValue"""


_JuniBgpPeerAddressFamilyNextHopSelf_Object = MibTableColumn
juniBgpPeerAddressFamilyNextHopSelf = _JuniBgpPeerAddressFamilyNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 7),
    _JuniBgpPeerAddressFamilyNextHopSelf_Type()
)
juniBgpPeerAddressFamilyNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyNextHopSelf.setStatus("current")


class _JuniBgpPeerAddressFamilySendCommunity_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilySendCommunity based on TruthValue"""


_JuniBgpPeerAddressFamilySendCommunity_Object = MibTableColumn
juniBgpPeerAddressFamilySendCommunity = _JuniBgpPeerAddressFamilySendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 8),
    _JuniBgpPeerAddressFamilySendCommunity_Type()
)
juniBgpPeerAddressFamilySendCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilySendCommunity.setStatus("current")
_JuniBgpPeerAddressFamilyDistributeListIn_Type = DisplayString
_JuniBgpPeerAddressFamilyDistributeListIn_Object = MibTableColumn
juniBgpPeerAddressFamilyDistributeListIn = _JuniBgpPeerAddressFamilyDistributeListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 9),
    _JuniBgpPeerAddressFamilyDistributeListIn_Type()
)
juniBgpPeerAddressFamilyDistributeListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyDistributeListIn.setStatus("current")
_JuniBgpPeerAddressFamilyDistributeListOut_Type = DisplayString
_JuniBgpPeerAddressFamilyDistributeListOut_Object = MibTableColumn
juniBgpPeerAddressFamilyDistributeListOut = _JuniBgpPeerAddressFamilyDistributeListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 10),
    _JuniBgpPeerAddressFamilyDistributeListOut_Type()
)
juniBgpPeerAddressFamilyDistributeListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyDistributeListOut.setStatus("current")
_JuniBgpPeerAddressFamilyPrefixListIn_Type = DisplayString
_JuniBgpPeerAddressFamilyPrefixListIn_Object = MibTableColumn
juniBgpPeerAddressFamilyPrefixListIn = _JuniBgpPeerAddressFamilyPrefixListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 11),
    _JuniBgpPeerAddressFamilyPrefixListIn_Type()
)
juniBgpPeerAddressFamilyPrefixListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyPrefixListIn.setStatus("current")
_JuniBgpPeerAddressFamilyPrefixListOut_Type = DisplayString
_JuniBgpPeerAddressFamilyPrefixListOut_Object = MibTableColumn
juniBgpPeerAddressFamilyPrefixListOut = _JuniBgpPeerAddressFamilyPrefixListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 12),
    _JuniBgpPeerAddressFamilyPrefixListOut_Type()
)
juniBgpPeerAddressFamilyPrefixListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyPrefixListOut.setStatus("current")
_JuniBgpPeerAddressFamilyPrefixTreeIn_Type = DisplayString
_JuniBgpPeerAddressFamilyPrefixTreeIn_Object = MibTableColumn
juniBgpPeerAddressFamilyPrefixTreeIn = _JuniBgpPeerAddressFamilyPrefixTreeIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 13),
    _JuniBgpPeerAddressFamilyPrefixTreeIn_Type()
)
juniBgpPeerAddressFamilyPrefixTreeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyPrefixTreeIn.setStatus("current")
_JuniBgpPeerAddressFamilyPrefixTreeOut_Type = DisplayString
_JuniBgpPeerAddressFamilyPrefixTreeOut_Object = MibTableColumn
juniBgpPeerAddressFamilyPrefixTreeOut = _JuniBgpPeerAddressFamilyPrefixTreeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 14),
    _JuniBgpPeerAddressFamilyPrefixTreeOut_Type()
)
juniBgpPeerAddressFamilyPrefixTreeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyPrefixTreeOut.setStatus("current")
_JuniBgpPeerAddressFamilyFilterListIn_Type = DisplayString
_JuniBgpPeerAddressFamilyFilterListIn_Object = MibTableColumn
juniBgpPeerAddressFamilyFilterListIn = _JuniBgpPeerAddressFamilyFilterListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 15),
    _JuniBgpPeerAddressFamilyFilterListIn_Type()
)
juniBgpPeerAddressFamilyFilterListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyFilterListIn.setStatus("current")
_JuniBgpPeerAddressFamilyFilterListOut_Type = DisplayString
_JuniBgpPeerAddressFamilyFilterListOut_Object = MibTableColumn
juniBgpPeerAddressFamilyFilterListOut = _JuniBgpPeerAddressFamilyFilterListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 16),
    _JuniBgpPeerAddressFamilyFilterListOut_Type()
)
juniBgpPeerAddressFamilyFilterListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyFilterListOut.setStatus("current")
_JuniBgpPeerAddressFamilyFilterListWeight_Type = DisplayString
_JuniBgpPeerAddressFamilyFilterListWeight_Object = MibTableColumn
juniBgpPeerAddressFamilyFilterListWeight = _JuniBgpPeerAddressFamilyFilterListWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 17),
    _JuniBgpPeerAddressFamilyFilterListWeight_Type()
)
juniBgpPeerAddressFamilyFilterListWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyFilterListWeight.setStatus("current")


class _JuniBgpPeerAddressFamilyFilterListWeightValue_Type(Unsigned32):
    """Custom type juniBgpPeerAddressFamilyFilterListWeightValue based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerAddressFamilyFilterListWeightValue_Object = MibTableColumn
juniBgpPeerAddressFamilyFilterListWeightValue = _JuniBgpPeerAddressFamilyFilterListWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 18),
    _JuniBgpPeerAddressFamilyFilterListWeightValue_Type()
)
juniBgpPeerAddressFamilyFilterListWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyFilterListWeightValue.setStatus("current")


class _JuniBgpPeerAddressFamilyRouteMapIn_Type(DisplayString):
    """Custom type juniBgpPeerAddressFamilyRouteMapIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerAddressFamilyRouteMapIn_Type.__name__ = "DisplayString"
_JuniBgpPeerAddressFamilyRouteMapIn_Object = MibTableColumn
juniBgpPeerAddressFamilyRouteMapIn = _JuniBgpPeerAddressFamilyRouteMapIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 19),
    _JuniBgpPeerAddressFamilyRouteMapIn_Type()
)
juniBgpPeerAddressFamilyRouteMapIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRouteMapIn.setStatus("current")


class _JuniBgpPeerAddressFamilyRouteMapOut_Type(DisplayString):
    """Custom type juniBgpPeerAddressFamilyRouteMapOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerAddressFamilyRouteMapOut_Type.__name__ = "DisplayString"
_JuniBgpPeerAddressFamilyRouteMapOut_Object = MibTableColumn
juniBgpPeerAddressFamilyRouteMapOut = _JuniBgpPeerAddressFamilyRouteMapOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 20),
    _JuniBgpPeerAddressFamilyRouteMapOut_Type()
)
juniBgpPeerAddressFamilyRouteMapOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRouteMapOut.setStatus("current")


class _JuniBgpPeerAddressFamilyRouteReflectorClient_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyRouteReflectorClient based on TruthValue"""


_JuniBgpPeerAddressFamilyRouteReflectorClient_Object = MibTableColumn
juniBgpPeerAddressFamilyRouteReflectorClient = _JuniBgpPeerAddressFamilyRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 21),
    _JuniBgpPeerAddressFamilyRouteReflectorClient_Type()
)
juniBgpPeerAddressFamilyRouteReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRouteReflectorClient.setStatus("current")


class _JuniBgpPeerAddressFamilyRouteLimitWarn_Type(Unsigned32):
    """Custom type juniBgpPeerAddressFamilyRouteLimitWarn based on Unsigned32"""
    defaultValue = 1000000


_JuniBgpPeerAddressFamilyRouteLimitWarn_Object = MibTableColumn
juniBgpPeerAddressFamilyRouteLimitWarn = _JuniBgpPeerAddressFamilyRouteLimitWarn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 22),
    _JuniBgpPeerAddressFamilyRouteLimitWarn_Type()
)
juniBgpPeerAddressFamilyRouteLimitWarn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRouteLimitWarn.setStatus("current")


class _JuniBgpPeerAddressFamilyRouteLimitReset_Type(Unsigned32):
    """Custom type juniBgpPeerAddressFamilyRouteLimitReset based on Unsigned32"""
    defaultValue = 10000000


_JuniBgpPeerAddressFamilyRouteLimitReset_Object = MibTableColumn
juniBgpPeerAddressFamilyRouteLimitReset = _JuniBgpPeerAddressFamilyRouteLimitReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 23),
    _JuniBgpPeerAddressFamilyRouteLimitReset_Type()
)
juniBgpPeerAddressFamilyRouteLimitReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRouteLimitReset.setStatus("current")


class _JuniBgpPeerAddressFamilyRouteLimitWarnOnly_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyRouteLimitWarnOnly based on TruthValue"""


_JuniBgpPeerAddressFamilyRouteLimitWarnOnly_Object = MibTableColumn
juniBgpPeerAddressFamilyRouteLimitWarnOnly = _JuniBgpPeerAddressFamilyRouteLimitWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 24),
    _JuniBgpPeerAddressFamilyRouteLimitWarnOnly_Type()
)
juniBgpPeerAddressFamilyRouteLimitWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRouteLimitWarnOnly.setStatus("current")


class _JuniBgpPeerAddressFamilyRemovePrivateAs_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyRemovePrivateAs based on TruthValue"""


_JuniBgpPeerAddressFamilyRemovePrivateAs_Object = MibTableColumn
juniBgpPeerAddressFamilyRemovePrivateAs = _JuniBgpPeerAddressFamilyRemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 25),
    _JuniBgpPeerAddressFamilyRemovePrivateAs_Type()
)
juniBgpPeerAddressFamilyRemovePrivateAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRemovePrivateAs.setStatus("current")


class _JuniBgpPeerAddressFamilyUnsuppressMap_Type(DisplayString):
    """Custom type juniBgpPeerAddressFamilyUnsuppressMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerAddressFamilyUnsuppressMap_Type.__name__ = "DisplayString"
_JuniBgpPeerAddressFamilyUnsuppressMap_Object = MibTableColumn
juniBgpPeerAddressFamilyUnsuppressMap = _JuniBgpPeerAddressFamilyUnsuppressMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 26),
    _JuniBgpPeerAddressFamilyUnsuppressMap_Type()
)
juniBgpPeerAddressFamilyUnsuppressMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyUnsuppressMap.setStatus("current")


class _JuniBgpPeerAddressFamilyInboundSoftReconfig_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyInboundSoftReconfig based on TruthValue"""


_JuniBgpPeerAddressFamilyInboundSoftReconfig_Object = MibTableColumn
juniBgpPeerAddressFamilyInboundSoftReconfig = _JuniBgpPeerAddressFamilyInboundSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 27),
    _JuniBgpPeerAddressFamilyInboundSoftReconfig_Type()
)
juniBgpPeerAddressFamilyInboundSoftReconfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyInboundSoftReconfig.setStatus("current")


class _JuniBgpPeerAddressFamilyResetConnectionType_Type(JuniBgpResetConnectionType):
    """Custom type juniBgpPeerAddressFamilyResetConnectionType based on JuniBgpResetConnectionType"""


_JuniBgpPeerAddressFamilyResetConnectionType_Object = MibTableColumn
juniBgpPeerAddressFamilyResetConnectionType = _JuniBgpPeerAddressFamilyResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 28),
    _JuniBgpPeerAddressFamilyResetConnectionType_Type()
)
juniBgpPeerAddressFamilyResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyResetConnectionType.setStatus("current")
_JuniBgpPeerAddressFamilyRowStatus_Type = RowStatus
_JuniBgpPeerAddressFamilyRowStatus_Object = MibTableColumn
juniBgpPeerAddressFamilyRowStatus = _JuniBgpPeerAddressFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 29),
    _JuniBgpPeerAddressFamilyRowStatus_Type()
)
juniBgpPeerAddressFamilyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyRowStatus.setStatus("current")


class _JuniBgpPeerAddressFamilyAsOverride_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyAsOverride based on TruthValue"""


_JuniBgpPeerAddressFamilyAsOverride_Object = MibTableColumn
juniBgpPeerAddressFamilyAsOverride = _JuniBgpPeerAddressFamilyAsOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 30),
    _JuniBgpPeerAddressFamilyAsOverride_Type()
)
juniBgpPeerAddressFamilyAsOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyAsOverride.setStatus("current")


class _JuniBgpPeerAddressFamilyAllowAsIn_Type(Integer32):
    """Custom type juniBgpPeerAddressFamilyAllowAsIn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_JuniBgpPeerAddressFamilyAllowAsIn_Type.__name__ = "Integer32"
_JuniBgpPeerAddressFamilyAllowAsIn_Object = MibTableColumn
juniBgpPeerAddressFamilyAllowAsIn = _JuniBgpPeerAddressFamilyAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 31),
    _JuniBgpPeerAddressFamilyAllowAsIn_Type()
)
juniBgpPeerAddressFamilyAllowAsIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyAllowAsIn.setStatus("current")


class _JuniBgpPeerAddressFamilySendExtendedCommunity_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilySendExtendedCommunity based on TruthValue"""


_JuniBgpPeerAddressFamilySendExtendedCommunity_Object = MibTableColumn
juniBgpPeerAddressFamilySendExtendedCommunity = _JuniBgpPeerAddressFamilySendExtendedCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 32),
    _JuniBgpPeerAddressFamilySendExtendedCommunity_Type()
)
juniBgpPeerAddressFamilySendExtendedCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilySendExtendedCommunity.setStatus("current")


class _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend based on TruthValue"""


_JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend_Object = MibTableColumn
juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend = _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 33),
    _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend_Type()
)
juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend.setStatus("current")


class _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive based on TruthValue"""


_JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive_Object = MibTableColumn
juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive = _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 34),
    _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive_Type()
)
juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive.setStatus("current")


class _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend based on TruthValue"""


_JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Object = MibTableColumn
juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend = _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 35),
    _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Type()
)
juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend.setStatus("current")


class _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive based on TruthValue"""


_JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive_Object = MibTableColumn
juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive = _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 36),
    _JuniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive_Type()
)
juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive.setStatus("current")
_JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend_Type = TruthValue
_JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend = _JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 37),
    _JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend_Type()
)
juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend.setStatus("current")
_JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive_Type = TruthValue
_JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive = _JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 38),
    _JuniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive_Type()
)
juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive.setStatus("current")
_JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend_Type = TruthValue
_JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend = _JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 39),
    _JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend_Type()
)
juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend.setStatus("current")
_JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive_Type = TruthValue
_JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive = _JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 40),
    _JuniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive_Type()
)
juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive.setStatus("current")


class _JuniBgpPeerAddressFamilyReceivedOrfEntriesLimit_Type(Unsigned32):
    """Custom type juniBgpPeerAddressFamilyReceivedOrfEntriesLimit based on Unsigned32"""
    defaultValue = 4294967295


_JuniBgpPeerAddressFamilyReceivedOrfEntriesLimit_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedOrfEntriesLimit = _JuniBgpPeerAddressFamilyReceivedOrfEntriesLimit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 41),
    _JuniBgpPeerAddressFamilyReceivedOrfEntriesLimit_Type()
)
juniBgpPeerAddressFamilyReceivedOrfEntriesLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedOrfEntriesLimit.setStatus("current")


class _JuniBgpPeerAddressFamilyReceivedPrefixListOrfName_Type(DisplayString):
    """Custom type juniBgpPeerAddressFamilyReceivedPrefixListOrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerAddressFamilyReceivedPrefixListOrfName_Type.__name__ = "DisplayString"
_JuniBgpPeerAddressFamilyReceivedPrefixListOrfName_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedPrefixListOrfName = _JuniBgpPeerAddressFamilyReceivedPrefixListOrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 42),
    _JuniBgpPeerAddressFamilyReceivedPrefixListOrfName_Type()
)
juniBgpPeerAddressFamilyReceivedPrefixListOrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedPrefixListOrfName.setStatus("current")


class _JuniBgpPeerAddressFamilyMaximumPrefixStrict_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyMaximumPrefixStrict based on TruthValue"""


_JuniBgpPeerAddressFamilyMaximumPrefixStrict_Object = MibTableColumn
juniBgpPeerAddressFamilyMaximumPrefixStrict = _JuniBgpPeerAddressFamilyMaximumPrefixStrict_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 43),
    _JuniBgpPeerAddressFamilyMaximumPrefixStrict_Type()
)
juniBgpPeerAddressFamilyMaximumPrefixStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyMaximumPrefixStrict.setStatus("current")


class _JuniBgpPeerAddressFamilyUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpPeerAddressFamilyUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive", 29),
          ("juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend", 28),
          ("juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive", 27),
          ("juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend", 26),
          ("juniBgpPeerAddressFamilyAllowAsIn", 24),
          ("juniBgpPeerAddressFamilyAsOverride", 23),
          ("juniBgpPeerAddressFamilyDefaultOriginate", 1),
          ("juniBgpPeerAddressFamilyDefaultOriginateRouteMap", 33),
          ("juniBgpPeerAddressFamilyDistributeListIn", 4),
          ("juniBgpPeerAddressFamilyDistributeListOut", 5),
          ("juniBgpPeerAddressFamilyFilterListIn", 10),
          ("juniBgpPeerAddressFamilyFilterListOut", 11),
          ("juniBgpPeerAddressFamilyFilterListWeight", 12),
          ("juniBgpPeerAddressFamilyFilterListWeightValue", 13),
          ("juniBgpPeerAddressFamilyInboundSoftReconfig", 22),
          ("juniBgpPeerAddressFamilyMaximumPrefixStrict", 31),
          ("juniBgpPeerAddressFamilyNextHopSelf", 2),
          ("juniBgpPeerAddressFamilyNextHopUnchanged", 34),
          ("juniBgpPeerAddressFamilyPeerGroup", 0),
          ("juniBgpPeerAddressFamilyPrefixListIn", 6),
          ("juniBgpPeerAddressFamilyPrefixListOut", 7),
          ("juniBgpPeerAddressFamilyPrefixTreeIn", 8),
          ("juniBgpPeerAddressFamilyPrefixTreeOut", 9),
          ("juniBgpPeerAddressFamilyReceivedOrfEntriesLimit", 30),
          ("juniBgpPeerAddressFamilyRemovePrivateAs", 20),
          ("juniBgpPeerAddressFamilyRouteLimitReset", 18),
          ("juniBgpPeerAddressFamilyRouteLimitWarn", 17),
          ("juniBgpPeerAddressFamilyRouteLimitWarnOnly", 19),
          ("juniBgpPeerAddressFamilyRouteMapIn", 14),
          ("juniBgpPeerAddressFamilyRouteMapOut", 15),
          ("juniBgpPeerAddressFamilyRouteReflectorClient", 16),
          ("juniBgpPeerAddressFamilySendCommunity", 3),
          ("juniBgpPeerAddressFamilySendExtendedCommunity", 25),
          ("juniBgpPeerAddressFamilySendLabel", 32),
          ("juniBgpPeerAddressFamilyUnsuppressMap", 21))
    )

_JuniBgpPeerAddressFamilyUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpPeerAddressFamilyUnconfiguredAttributes_Object = MibTableColumn
juniBgpPeerAddressFamilyUnconfiguredAttributes = _JuniBgpPeerAddressFamilyUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 44),
    _JuniBgpPeerAddressFamilyUnconfiguredAttributes_Type()
)
juniBgpPeerAddressFamilyUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyUnconfiguredAttributes.setStatus("current")


class _JuniBgpPeerAddressFamilySendLabel_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilySendLabel based on TruthValue"""


_JuniBgpPeerAddressFamilySendLabel_Object = MibTableColumn
juniBgpPeerAddressFamilySendLabel = _JuniBgpPeerAddressFamilySendLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 45),
    _JuniBgpPeerAddressFamilySendLabel_Type()
)
juniBgpPeerAddressFamilySendLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilySendLabel.setStatus("current")


class _JuniBgpPeerAddressFamilyDefaultOriginateRouteMap_Type(DisplayString):
    """Custom type juniBgpPeerAddressFamilyDefaultOriginateRouteMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerAddressFamilyDefaultOriginateRouteMap_Type.__name__ = "DisplayString"
_JuniBgpPeerAddressFamilyDefaultOriginateRouteMap_Object = MibTableColumn
juniBgpPeerAddressFamilyDefaultOriginateRouteMap = _JuniBgpPeerAddressFamilyDefaultOriginateRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 46),
    _JuniBgpPeerAddressFamilyDefaultOriginateRouteMap_Type()
)
juniBgpPeerAddressFamilyDefaultOriginateRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyDefaultOriginateRouteMap.setStatus("current")
_JuniBgpPeerAddressFamilySentCapabilityGracefulRestart_Type = TruthValue
_JuniBgpPeerAddressFamilySentCapabilityGracefulRestart_Object = MibTableColumn
juniBgpPeerAddressFamilySentCapabilityGracefulRestart = _JuniBgpPeerAddressFamilySentCapabilityGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 47),
    _JuniBgpPeerAddressFamilySentCapabilityGracefulRestart_Type()
)
juniBgpPeerAddressFamilySentCapabilityGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilySentCapabilityGracefulRestart.setStatus("current")
_JuniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart_Type = TruthValue
_JuniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart = _JuniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 48),
    _JuniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart_Type()
)
juniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart.setStatus("current")
_JuniBgpPeerAddressFamilySentForwardingStatePreserved_Type = TruthValue
_JuniBgpPeerAddressFamilySentForwardingStatePreserved_Object = MibTableColumn
juniBgpPeerAddressFamilySentForwardingStatePreserved = _JuniBgpPeerAddressFamilySentForwardingStatePreserved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 49),
    _JuniBgpPeerAddressFamilySentForwardingStatePreserved_Type()
)
juniBgpPeerAddressFamilySentForwardingStatePreserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilySentForwardingStatePreserved.setStatus("current")
_JuniBgpPeerAddressFamilyReceivedForwardingStatePreserved_Type = TruthValue
_JuniBgpPeerAddressFamilyReceivedForwardingStatePreserved_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedForwardingStatePreserved = _JuniBgpPeerAddressFamilyReceivedForwardingStatePreserved_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 50),
    _JuniBgpPeerAddressFamilyReceivedForwardingStatePreserved_Type()
)
juniBgpPeerAddressFamilyReceivedForwardingStatePreserved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedForwardingStatePreserved.setStatus("current")
_JuniBgpPeerAddressFamilySentEndOfRibMarker_Type = TruthValue
_JuniBgpPeerAddressFamilySentEndOfRibMarker_Object = MibTableColumn
juniBgpPeerAddressFamilySentEndOfRibMarker = _JuniBgpPeerAddressFamilySentEndOfRibMarker_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 51),
    _JuniBgpPeerAddressFamilySentEndOfRibMarker_Type()
)
juniBgpPeerAddressFamilySentEndOfRibMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilySentEndOfRibMarker.setStatus("current")
_JuniBgpPeerAddressFamilyReceivedEndOfRibMarker_Type = TruthValue
_JuniBgpPeerAddressFamilyReceivedEndOfRibMarker_Object = MibTableColumn
juniBgpPeerAddressFamilyReceivedEndOfRibMarker = _JuniBgpPeerAddressFamilyReceivedEndOfRibMarker_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 52),
    _JuniBgpPeerAddressFamilyReceivedEndOfRibMarker_Type()
)
juniBgpPeerAddressFamilyReceivedEndOfRibMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyReceivedEndOfRibMarker.setStatus("current")
_JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes_Type = TruthValue
_JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes_Object = MibTableColumn
juniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes = _JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 53),
    _JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes_Type()
)
juniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes.setStatus("current")
_JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection_Type = TruthValue
_JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection_Object = MibTableColumn
juniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection = _JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 54),
    _JuniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection_Type()
)
juniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection.setStatus("current")


class _JuniBgpPeerAddressFamilyNextHopUnchanged_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyNextHopUnchanged based on TruthValue"""


_JuniBgpPeerAddressFamilyNextHopUnchanged_Object = MibTableColumn
juniBgpPeerAddressFamilyNextHopUnchanged = _JuniBgpPeerAddressFamilyNextHopUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 8, 1, 55),
    _JuniBgpPeerAddressFamilyNextHopUnchanged_Type()
)
juniBgpPeerAddressFamilyNextHopUnchanged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyNextHopUnchanged.setStatus("current")
_JuniBgpPeerGroupTable_Object = MibTable
juniBgpPeerGroupTable = _JuniBgpPeerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9)
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupTable.setStatus("current")
_JuniBgpPeerGroupEntry_Object = MibTableRow
juniBgpPeerGroupEntry = _JuniBgpPeerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1)
)
juniBgpPeerGroupEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupGroupName"),
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupEntry.setStatus("current")
_JuniBgpPeerGroupVrfName_Type = JuniVrfName
_JuniBgpPeerGroupVrfName_Object = MibTableColumn
juniBgpPeerGroupVrfName = _JuniBgpPeerGroupVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 1),
    _JuniBgpPeerGroupVrfName_Type()
)
juniBgpPeerGroupVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerGroupVrfName.setStatus("current")


class _JuniBgpPeerGroupGroupName_Type(DisplayString):
    """Custom type juniBgpPeerGroupGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupGroupName_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupGroupName_Object = MibTableColumn
juniBgpPeerGroupGroupName = _JuniBgpPeerGroupGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 2),
    _JuniBgpPeerGroupGroupName_Type()
)
juniBgpPeerGroupGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerGroupGroupName.setStatus("current")


class _JuniBgpPeerGroupAdminStatus_Type(Integer32):
    """Custom type juniBgpPeerGroupAdminStatus based on Integer32"""
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


_JuniBgpPeerGroupAdminStatus_Type.__name__ = "Integer32"
_JuniBgpPeerGroupAdminStatus_Object = MibTableColumn
juniBgpPeerGroupAdminStatus = _JuniBgpPeerGroupAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 3),
    _JuniBgpPeerGroupAdminStatus_Type()
)
juniBgpPeerGroupAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAdminStatus.setStatus("current")


class _JuniBgpPeerGroupRemoteAsNumber_Type(Integer32):
    """Custom type juniBgpPeerGroupRemoteAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerGroupRemoteAsNumber_Type.__name__ = "Integer32"
_JuniBgpPeerGroupRemoteAsNumber_Object = MibTableColumn
juniBgpPeerGroupRemoteAsNumber = _JuniBgpPeerGroupRemoteAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 4),
    _JuniBgpPeerGroupRemoteAsNumber_Type()
)
juniBgpPeerGroupRemoteAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupRemoteAsNumber.setStatus("deprecated")


class _JuniBgpPeerGroupRetryInterval_Type(Integer32):
    """Custom type juniBgpPeerGroupRetryInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerGroupRetryInterval_Type.__name__ = "Integer32"
_JuniBgpPeerGroupRetryInterval_Object = MibTableColumn
juniBgpPeerGroupRetryInterval = _JuniBgpPeerGroupRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 5),
    _JuniBgpPeerGroupRetryInterval_Type()
)
juniBgpPeerGroupRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerGroupRetryInterval.setUnits("seconds")


class _JuniBgpPeerGroupConfigHoldTime_Type(Integer32):
    """Custom type juniBgpPeerGroupConfigHoldTime based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_JuniBgpPeerGroupConfigHoldTime_Type.__name__ = "Integer32"
_JuniBgpPeerGroupConfigHoldTime_Object = MibTableColumn
juniBgpPeerGroupConfigHoldTime = _JuniBgpPeerGroupConfigHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 6),
    _JuniBgpPeerGroupConfigHoldTime_Type()
)
juniBgpPeerGroupConfigHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfigHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfigHoldTime.setUnits("seconds")


class _JuniBgpPeerGroupConfigKeepAliveInterval_Type(Integer32):
    """Custom type juniBgpPeerGroupConfigKeepAliveInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_JuniBgpPeerGroupConfigKeepAliveInterval_Type.__name__ = "Integer32"
_JuniBgpPeerGroupConfigKeepAliveInterval_Object = MibTableColumn
juniBgpPeerGroupConfigKeepAliveInterval = _JuniBgpPeerGroupConfigKeepAliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 7),
    _JuniBgpPeerGroupConfigKeepAliveInterval_Type()
)
juniBgpPeerGroupConfigKeepAliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfigKeepAliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfigKeepAliveInterval.setUnits("seconds")


class _JuniBgpPeerGroupAsOriginationInterval_Type(Integer32):
    """Custom type juniBgpPeerGroupAsOriginationInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerGroupAsOriginationInterval_Type.__name__ = "Integer32"
_JuniBgpPeerGroupAsOriginationInterval_Object = MibTableColumn
juniBgpPeerGroupAsOriginationInterval = _JuniBgpPeerGroupAsOriginationInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 8),
    _JuniBgpPeerGroupAsOriginationInterval_Type()
)
juniBgpPeerGroupAsOriginationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAsOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAsOriginationInterval.setUnits("seconds")


class _JuniBgpPeerGroupAdvertisementInterval_Type(Integer32):
    """Custom type juniBgpPeerGroupAdvertisementInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerGroupAdvertisementInterval_Type.__name__ = "Integer32"
_JuniBgpPeerGroupAdvertisementInterval_Object = MibTableColumn
juniBgpPeerGroupAdvertisementInterval = _JuniBgpPeerGroupAdvertisementInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 9),
    _JuniBgpPeerGroupAdvertisementInterval_Type()
)
juniBgpPeerGroupAdvertisementInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAdvertisementInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAdvertisementInterval.setUnits("seconds")


class _JuniBgpPeerGroupDescription_Type(DisplayString):
    """Custom type juniBgpPeerGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniBgpPeerGroupDescription_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupDescription_Object = MibTableColumn
juniBgpPeerGroupDescription = _JuniBgpPeerGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 10),
    _JuniBgpPeerGroupDescription_Type()
)
juniBgpPeerGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupDescription.setStatus("current")


class _JuniBgpPeerGroupWeight_Type(Unsigned32):
    """Custom type juniBgpPeerGroupWeight based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupWeight_Object = MibTableColumn
juniBgpPeerGroupWeight = _JuniBgpPeerGroupWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 11),
    _JuniBgpPeerGroupWeight_Type()
)
juniBgpPeerGroupWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupWeight.setStatus("current")


class _JuniBgpPeerGroupEbgpMultihop_Type(TruthValue):
    """Custom type juniBgpPeerGroupEbgpMultihop based on TruthValue"""


_JuniBgpPeerGroupEbgpMultihop_Object = MibTableColumn
juniBgpPeerGroupEbgpMultihop = _JuniBgpPeerGroupEbgpMultihop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 12),
    _JuniBgpPeerGroupEbgpMultihop_Type()
)
juniBgpPeerGroupEbgpMultihop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupEbgpMultihop.setStatus("current")


class _JuniBgpPeerGroupEbgpMultihopTtl_Type(Integer32):
    """Custom type juniBgpPeerGroupEbgpMultihopTtl based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpPeerGroupEbgpMultihopTtl_Type.__name__ = "Integer32"
_JuniBgpPeerGroupEbgpMultihopTtl_Object = MibTableColumn
juniBgpPeerGroupEbgpMultihopTtl = _JuniBgpPeerGroupEbgpMultihopTtl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 13),
    _JuniBgpPeerGroupEbgpMultihopTtl_Type()
)
juniBgpPeerGroupEbgpMultihopTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupEbgpMultihopTtl.setStatus("current")


class _JuniBgpPeerGroupUpdateSource_Type(IpAddress):
    """Custom type juniBgpPeerGroupUpdateSource based on IpAddress"""
    defaultValue = 0


_JuniBgpPeerGroupUpdateSource_Object = MibTableColumn
juniBgpPeerGroupUpdateSource = _JuniBgpPeerGroupUpdateSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 14),
    _JuniBgpPeerGroupUpdateSource_Type()
)
juniBgpPeerGroupUpdateSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupUpdateSource.setStatus("current")


class _JuniBgpPeerGroupMd5Password_Type(OctetString):
    """Custom type juniBgpPeerGroupMd5Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupMd5Password_Type.__name__ = "OctetString"
_JuniBgpPeerGroupMd5Password_Object = MibTableColumn
juniBgpPeerGroupMd5Password = _JuniBgpPeerGroupMd5Password_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 15),
    _JuniBgpPeerGroupMd5Password_Type()
)
juniBgpPeerGroupMd5Password.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupMd5Password.setStatus("current")


class _JuniBgpPeerGroupMaxUpdateSize_Type(Unsigned32):
    """Custom type juniBgpPeerGroupMaxUpdateSize based on Unsigned32"""
    defaultValue = 4096


_JuniBgpPeerGroupMaxUpdateSize_Object = MibTableColumn
juniBgpPeerGroupMaxUpdateSize = _JuniBgpPeerGroupMaxUpdateSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 16),
    _JuniBgpPeerGroupMaxUpdateSize_Type()
)
juniBgpPeerGroupMaxUpdateSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupMaxUpdateSize.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpPeerGroupMaxUpdateSize.setUnits("bytes")


class _JuniBgpPeerGroupResetConnectionType_Type(JuniBgpResetConnectionType):
    """Custom type juniBgpPeerGroupResetConnectionType based on JuniBgpResetConnectionType"""


_JuniBgpPeerGroupResetConnectionType_Object = MibTableColumn
juniBgpPeerGroupResetConnectionType = _JuniBgpPeerGroupResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 17),
    _JuniBgpPeerGroupResetConnectionType_Type()
)
juniBgpPeerGroupResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupResetConnectionType.setStatus("current")
_JuniBgpPeerGroupRowStatus_Type = RowStatus
_JuniBgpPeerGroupRowStatus_Object = MibTableColumn
juniBgpPeerGroupRowStatus = _JuniBgpPeerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 18),
    _JuniBgpPeerGroupRowStatus_Type()
)
juniBgpPeerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupRowStatus.setStatus("current")


class _JuniBgpPeerGroupLocalAsNumber_Type(Integer32):
    """Custom type juniBgpPeerGroupLocalAsNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpPeerGroupLocalAsNumber_Type.__name__ = "Integer32"
_JuniBgpPeerGroupLocalAsNumber_Object = MibTableColumn
juniBgpPeerGroupLocalAsNumber = _JuniBgpPeerGroupLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 19),
    _JuniBgpPeerGroupLocalAsNumber_Type()
)
juniBgpPeerGroupLocalAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupLocalAsNumber.setStatus("deprecated")


class _JuniBgpPeerGroupFourOctetRemoteAsNumber_Type(JuniBgpFourOctetAsNumber):
    """Custom type juniBgpPeerGroupFourOctetRemoteAsNumber based on JuniBgpFourOctetAsNumber"""
    defaultValue = 0


_JuniBgpPeerGroupFourOctetRemoteAsNumber_Object = MibTableColumn
juniBgpPeerGroupFourOctetRemoteAsNumber = _JuniBgpPeerGroupFourOctetRemoteAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 20),
    _JuniBgpPeerGroupFourOctetRemoteAsNumber_Type()
)
juniBgpPeerGroupFourOctetRemoteAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupFourOctetRemoteAsNumber.setStatus("current")


class _JuniBgpPeerGroupFourOctetLocalAsNumber_Type(JuniBgpFourOctetAsNumber):
    """Custom type juniBgpPeerGroupFourOctetLocalAsNumber based on JuniBgpFourOctetAsNumber"""
    defaultValue = 0


_JuniBgpPeerGroupFourOctetLocalAsNumber_Object = MibTableColumn
juniBgpPeerGroupFourOctetLocalAsNumber = _JuniBgpPeerGroupFourOctetLocalAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 21),
    _JuniBgpPeerGroupFourOctetLocalAsNumber_Type()
)
juniBgpPeerGroupFourOctetLocalAsNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupFourOctetLocalAsNumber.setStatus("current")


class _JuniBgpPeerGroupShouldAdvertiseCapabilitiesOption_Type(TruthValue):
    """Custom type juniBgpPeerGroupShouldAdvertiseCapabilitiesOption based on TruthValue"""


_JuniBgpPeerGroupShouldAdvertiseCapabilitiesOption_Object = MibTableColumn
juniBgpPeerGroupShouldAdvertiseCapabilitiesOption = _JuniBgpPeerGroupShouldAdvertiseCapabilitiesOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 22),
    _JuniBgpPeerGroupShouldAdvertiseCapabilitiesOption_Type()
)
juniBgpPeerGroupShouldAdvertiseCapabilitiesOption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupShouldAdvertiseCapabilitiesOption.setStatus("current")


class _JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh_Type(TruthValue):
    """Custom type juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh based on TruthValue"""


_JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh_Object = MibTableColumn
juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh = _JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 23),
    _JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh_Type()
)
juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh.setStatus("current")


class _JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco_Type(TruthValue):
    """Custom type juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco based on TruthValue"""


_JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco_Object = MibTableColumn
juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco = _JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 24),
    _JuniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco_Type()
)
juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco.setStatus("current")


class _JuniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers_Type(TruthValue):
    """Custom type juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers based on TruthValue"""


_JuniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers_Object = MibTableColumn
juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers = _JuniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 25),
    _JuniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers_Type()
)
juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers.setStatus("current")


class _JuniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg_Type(TruthValue):
    """Custom type juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg based on TruthValue"""


_JuniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg = _JuniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 26),
    _JuniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg_Type()
)
juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg.setStatus("current")


class _JuniBgpPeerGroupUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpPeerGroupUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpPeerGroupAdminStatus", 0),
          ("juniBgpPeerGroupAdvertisementInterval", 5),
          ("juniBgpPeerGroupAllowAccessListName", 25),
          ("juniBgpPeerGroupAllowMaxPeers", 26),
          ("juniBgpPeerGroupAsOriginationInterval", 4),
          ("juniBgpPeerGroupBfdEnabled", 30),
          ("juniBgpPeerGroupBfdMinReceiveInterval", 32),
          ("juniBgpPeerGroupBfdMinTransmitInterval", 31),
          ("juniBgpPeerGroupBfdMultiplier", 33),
          ("juniBgpPeerGroupConfigHoldTime", 2),
          ("juniBgpPeerGroupConfigKeepAliveInterval", 3),
          ("juniBgpPeerGroupConfiguredPeerType", 24),
          ("juniBgpPeerGroupDescription", 6),
          ("juniBgpPeerGroupEbgpMultihop", 8),
          ("juniBgpPeerGroupEbgpMultihopTtl", 9),
          ("juniBgpPeerGroupFourOctetLocalAsNumber", 14),
          ("juniBgpPeerGroupFourOctetRemoteAsNumber", 13),
          ("juniBgpPeerGroupGracefulRestartRestartTime", 28),
          ("juniBgpPeerGroupGracefulRestartStalePathsTime", 29),
          ("juniBgpPeerGroupIbgpSinglehop", 34),
          ("juniBgpPeerGroupLenient", 21),
          ("juniBgpPeerGroupMaxUpdateSize", 12),
          ("juniBgpPeerGroupMd5Password", 11),
          ("juniBgpPeerGroupPassive", 23),
          ("juniBgpPeerGroupRetryInterval", 1),
          ("juniBgpPeerGroupShouldAdvertiseCapabilitiesOption", 15),
          ("juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg", 19),
          ("juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers", 18),
          ("juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart", 27),
          ("juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg", 22),
          ("juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh", 16),
          ("juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco", 17),
          ("juniBgpPeerGroupSiteOfOrigin", 20),
          ("juniBgpPeerGroupUpdateSource", 10),
          ("juniBgpPeerGroupWeight", 7))
    )

_JuniBgpPeerGroupUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpPeerGroupUnconfiguredAttributes_Object = MibTableColumn
juniBgpPeerGroupUnconfiguredAttributes = _JuniBgpPeerGroupUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 27),
    _JuniBgpPeerGroupUnconfiguredAttributes_Type()
)
juniBgpPeerGroupUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupUnconfiguredAttributes.setStatus("current")


class _JuniBgpPeerGroupSiteOfOrigin_Type(OctetString):
    """Custom type juniBgpPeerGroupSiteOfOrigin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniBgpPeerGroupSiteOfOrigin_Type.__name__ = "OctetString"
_JuniBgpPeerGroupSiteOfOrigin_Object = MibTableColumn
juniBgpPeerGroupSiteOfOrigin = _JuniBgpPeerGroupSiteOfOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 28),
    _JuniBgpPeerGroupSiteOfOrigin_Type()
)
juniBgpPeerGroupSiteOfOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupSiteOfOrigin.setStatus("current")
_JuniBgpPeerGroupLenient_Type = TruthValue
_JuniBgpPeerGroupLenient_Object = MibTableColumn
juniBgpPeerGroupLenient = _JuniBgpPeerGroupLenient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 29),
    _JuniBgpPeerGroupLenient_Type()
)
juniBgpPeerGroupLenient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupLenient.setStatus("current")


class _JuniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Type(TruthValue):
    """Custom type juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg based on TruthValue"""


_JuniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Object = MibTableColumn
juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg = _JuniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 30),
    _JuniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg_Type()
)
juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg.setStatus("current")


class _JuniBgpPeerGroupPassive_Type(TruthValue):
    """Custom type juniBgpPeerGroupPassive based on TruthValue"""


_JuniBgpPeerGroupPassive_Object = MibTableColumn
juniBgpPeerGroupPassive = _JuniBgpPeerGroupPassive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 31),
    _JuniBgpPeerGroupPassive_Type()
)
juniBgpPeerGroupPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupPassive.setStatus("current")


class _JuniBgpPeerGroupConfiguredPeerType_Type(Integer32):
    """Custom type juniBgpPeerGroupConfiguredPeerType based on Integer32"""
    defaultValue = 0

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
        *(("peerTypeConfederation", 3),
          ("peerTypeExternal", 2),
          ("peerTypeInternal", 1),
          ("peerTypeNotConfigured", 0))
    )


_JuniBgpPeerGroupConfiguredPeerType_Type.__name__ = "Integer32"
_JuniBgpPeerGroupConfiguredPeerType_Object = MibTableColumn
juniBgpPeerGroupConfiguredPeerType = _JuniBgpPeerGroupConfiguredPeerType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 32),
    _JuniBgpPeerGroupConfiguredPeerType_Type()
)
juniBgpPeerGroupConfiguredPeerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfiguredPeerType.setStatus("current")


class _JuniBgpPeerGroupAllowAccessListName_Type(DisplayString):
    """Custom type juniBgpPeerGroupAllowAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAllowAccessListName_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAllowAccessListName_Object = MibTableColumn
juniBgpPeerGroupAllowAccessListName = _JuniBgpPeerGroupAllowAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 33),
    _JuniBgpPeerGroupAllowAccessListName_Type()
)
juniBgpPeerGroupAllowAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAllowAccessListName.setStatus("current")


class _JuniBgpPeerGroupAllowMaxPeers_Type(Unsigned32):
    """Custom type juniBgpPeerGroupAllowMaxPeers based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupAllowMaxPeers_Object = MibTableColumn
juniBgpPeerGroupAllowMaxPeers = _JuniBgpPeerGroupAllowMaxPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 34),
    _JuniBgpPeerGroupAllowMaxPeers_Type()
)
juniBgpPeerGroupAllowMaxPeers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAllowMaxPeers.setStatus("current")


class _JuniBgpPeerGroupCurrentDynamicPeerCount_Type(Unsigned32):
    """Custom type juniBgpPeerGroupCurrentDynamicPeerCount based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupCurrentDynamicPeerCount_Object = MibTableColumn
juniBgpPeerGroupCurrentDynamicPeerCount = _JuniBgpPeerGroupCurrentDynamicPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 35),
    _JuniBgpPeerGroupCurrentDynamicPeerCount_Type()
)
juniBgpPeerGroupCurrentDynamicPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerGroupCurrentDynamicPeerCount.setStatus("current")


class _JuniBgpPeerGroupHighWaterMarkDynamicPeerCount_Type(Unsigned32):
    """Custom type juniBgpPeerGroupHighWaterMarkDynamicPeerCount based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupHighWaterMarkDynamicPeerCount_Object = MibTableColumn
juniBgpPeerGroupHighWaterMarkDynamicPeerCount = _JuniBgpPeerGroupHighWaterMarkDynamicPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 36),
    _JuniBgpPeerGroupHighWaterMarkDynamicPeerCount_Type()
)
juniBgpPeerGroupHighWaterMarkDynamicPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerGroupHighWaterMarkDynamicPeerCount.setStatus("current")


class _JuniBgpPeerGroupRejectedDynamicPeerCount_Type(Unsigned32):
    """Custom type juniBgpPeerGroupRejectedDynamicPeerCount based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupRejectedDynamicPeerCount_Object = MibTableColumn
juniBgpPeerGroupRejectedDynamicPeerCount = _JuniBgpPeerGroupRejectedDynamicPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 37),
    _JuniBgpPeerGroupRejectedDynamicPeerCount_Type()
)
juniBgpPeerGroupRejectedDynamicPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerGroupRejectedDynamicPeerCount.setStatus("current")


class _JuniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart_Type(TruthValue):
    """Custom type juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart based on TruthValue"""


_JuniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart_Object = MibTableColumn
juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart = _JuniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 38),
    _JuniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart_Type()
)
juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart.setStatus("current")


class _JuniBgpPeerGroupGracefulRestartRestartTime_Type(Integer32):
    """Custom type juniBgpPeerGroupGracefulRestartRestartTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuniBgpPeerGroupGracefulRestartRestartTime_Type.__name__ = "Integer32"
_JuniBgpPeerGroupGracefulRestartRestartTime_Object = MibTableColumn
juniBgpPeerGroupGracefulRestartRestartTime = _JuniBgpPeerGroupGracefulRestartRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 39),
    _JuniBgpPeerGroupGracefulRestartRestartTime_Type()
)
juniBgpPeerGroupGracefulRestartRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupGracefulRestartRestartTime.setStatus("current")


class _JuniBgpPeerGroupGracefulRestartStalePathsTime_Type(Integer32):
    """Custom type juniBgpPeerGroupGracefulRestartStalePathsTime based on Integer32"""
    defaultValue = 360

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_JuniBgpPeerGroupGracefulRestartStalePathsTime_Type.__name__ = "Integer32"
_JuniBgpPeerGroupGracefulRestartStalePathsTime_Object = MibTableColumn
juniBgpPeerGroupGracefulRestartStalePathsTime = _JuniBgpPeerGroupGracefulRestartStalePathsTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 40),
    _JuniBgpPeerGroupGracefulRestartStalePathsTime_Type()
)
juniBgpPeerGroupGracefulRestartStalePathsTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupGracefulRestartStalePathsTime.setStatus("current")


class _JuniBgpPeerGroupBfdEnabled_Type(TruthValue):
    """Custom type juniBgpPeerGroupBfdEnabled based on TruthValue"""


_JuniBgpPeerGroupBfdEnabled_Object = MibTableColumn
juniBgpPeerGroupBfdEnabled = _JuniBgpPeerGroupBfdEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 41),
    _JuniBgpPeerGroupBfdEnabled_Type()
)
juniBgpPeerGroupBfdEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupBfdEnabled.setStatus("current")


class _JuniBgpPeerGroupBfdMinTransmitInterval_Type(Integer32):
    """Custom type juniBgpPeerGroupBfdMinTransmitInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniBgpPeerGroupBfdMinTransmitInterval_Type.__name__ = "Integer32"
_JuniBgpPeerGroupBfdMinTransmitInterval_Object = MibTableColumn
juniBgpPeerGroupBfdMinTransmitInterval = _JuniBgpPeerGroupBfdMinTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 42),
    _JuniBgpPeerGroupBfdMinTransmitInterval_Type()
)
juniBgpPeerGroupBfdMinTransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupBfdMinTransmitInterval.setStatus("current")


class _JuniBgpPeerGroupBfdMinReceiveInterval_Type(Integer32):
    """Custom type juniBgpPeerGroupBfdMinReceiveInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniBgpPeerGroupBfdMinReceiveInterval_Type.__name__ = "Integer32"
_JuniBgpPeerGroupBfdMinReceiveInterval_Object = MibTableColumn
juniBgpPeerGroupBfdMinReceiveInterval = _JuniBgpPeerGroupBfdMinReceiveInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 43),
    _JuniBgpPeerGroupBfdMinReceiveInterval_Type()
)
juniBgpPeerGroupBfdMinReceiveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupBfdMinReceiveInterval.setStatus("current")


class _JuniBgpPeerGroupBfdMultiplier_Type(Integer32):
    """Custom type juniBgpPeerGroupBfdMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpPeerGroupBfdMultiplier_Type.__name__ = "Integer32"
_JuniBgpPeerGroupBfdMultiplier_Object = MibTableColumn
juniBgpPeerGroupBfdMultiplier = _JuniBgpPeerGroupBfdMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 44),
    _JuniBgpPeerGroupBfdMultiplier_Type()
)
juniBgpPeerGroupBfdMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupBfdMultiplier.setStatus("current")


class _JuniBgpPeerGroupIbgpSinglehop_Type(TruthValue):
    """Custom type juniBgpPeerGroupIbgpSinglehop based on TruthValue"""


_JuniBgpPeerGroupIbgpSinglehop_Object = MibTableColumn
juniBgpPeerGroupIbgpSinglehop = _JuniBgpPeerGroupIbgpSinglehop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 9, 1, 45),
    _JuniBgpPeerGroupIbgpSinglehop_Type()
)
juniBgpPeerGroupIbgpSinglehop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupIbgpSinglehop.setStatus("current")
_JuniBgpPeerGroupAddressFamilyTable_Object = MibTable
juniBgpPeerGroupAddressFamilyTable = _JuniBgpPeerGroupAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10)
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyTable.setStatus("current")
_JuniBgpPeerGroupAddressFamilyEntry_Object = MibTableRow
juniBgpPeerGroupAddressFamilyEntry = _JuniBgpPeerGroupAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1)
)
juniBgpPeerGroupAddressFamilyEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySafi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupGroupAddressFamilyGroupName"),
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyEntry.setStatus("current")
_JuniBgpPeerGroupAddressFamilyVrfName_Type = JuniVrfName
_JuniBgpPeerGroupAddressFamilyVrfName_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyVrfName = _JuniBgpPeerGroupAddressFamilyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 1),
    _JuniBgpPeerGroupAddressFamilyVrfName_Type()
)
juniBgpPeerGroupAddressFamilyVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyVrfName.setStatus("current")
_JuniBgpPeerGroupAddressFamilyAfi_Type = JuniBgpAfi
_JuniBgpPeerGroupAddressFamilyAfi_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyAfi = _JuniBgpPeerGroupAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 2),
    _JuniBgpPeerGroupAddressFamilyAfi_Type()
)
juniBgpPeerGroupAddressFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyAfi.setStatus("current")
_JuniBgpPeerGroupAddressFamilySafi_Type = JuniBgpSafi
_JuniBgpPeerGroupAddressFamilySafi_Object = MibTableColumn
juniBgpPeerGroupAddressFamilySafi = _JuniBgpPeerGroupAddressFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 3),
    _JuniBgpPeerGroupAddressFamilySafi_Type()
)
juniBgpPeerGroupAddressFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilySafi.setStatus("current")


class _JuniBgpPeerGroupGroupAddressFamilyGroupName_Type(DisplayString):
    """Custom type juniBgpPeerGroupGroupAddressFamilyGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupGroupAddressFamilyGroupName_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupGroupAddressFamilyGroupName_Object = MibTableColumn
juniBgpPeerGroupGroupAddressFamilyGroupName = _JuniBgpPeerGroupGroupAddressFamilyGroupName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 4),
    _JuniBgpPeerGroupGroupAddressFamilyGroupName_Type()
)
juniBgpPeerGroupGroupAddressFamilyGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerGroupGroupAddressFamilyGroupName.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyDefaultOriginate_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyDefaultOriginate based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyDefaultOriginate_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyDefaultOriginate = _JuniBgpPeerGroupAddressFamilyDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 5),
    _JuniBgpPeerGroupAddressFamilyDefaultOriginate_Type()
)
juniBgpPeerGroupAddressFamilyDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyDefaultOriginate.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyNextHopSelf_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyNextHopSelf based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyNextHopSelf_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyNextHopSelf = _JuniBgpPeerGroupAddressFamilyNextHopSelf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 6),
    _JuniBgpPeerGroupAddressFamilyNextHopSelf_Type()
)
juniBgpPeerGroupAddressFamilyNextHopSelf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyNextHopSelf.setStatus("current")


class _JuniBgpPeerGroupAddressFamilySendCommunity_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilySendCommunity based on TruthValue"""


_JuniBgpPeerGroupAddressFamilySendCommunity_Object = MibTableColumn
juniBgpPeerGroupAddressFamilySendCommunity = _JuniBgpPeerGroupAddressFamilySendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 7),
    _JuniBgpPeerGroupAddressFamilySendCommunity_Type()
)
juniBgpPeerGroupAddressFamilySendCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilySendCommunity.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyDistributeListIn_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyDistributeListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyDistributeListIn_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyDistributeListIn_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyDistributeListIn = _JuniBgpPeerGroupAddressFamilyDistributeListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 8),
    _JuniBgpPeerGroupAddressFamilyDistributeListIn_Type()
)
juniBgpPeerGroupAddressFamilyDistributeListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyDistributeListIn.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyDistributeListOut_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyDistributeListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyDistributeListOut_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyDistributeListOut_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyDistributeListOut = _JuniBgpPeerGroupAddressFamilyDistributeListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 9),
    _JuniBgpPeerGroupAddressFamilyDistributeListOut_Type()
)
juniBgpPeerGroupAddressFamilyDistributeListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyDistributeListOut.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyPrefixListIn_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyPrefixListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyPrefixListIn_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyPrefixListIn_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyPrefixListIn = _JuniBgpPeerGroupAddressFamilyPrefixListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 10),
    _JuniBgpPeerGroupAddressFamilyPrefixListIn_Type()
)
juniBgpPeerGroupAddressFamilyPrefixListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyPrefixListIn.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyPrefixListOut_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyPrefixListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyPrefixListOut_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyPrefixListOut_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyPrefixListOut = _JuniBgpPeerGroupAddressFamilyPrefixListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 11),
    _JuniBgpPeerGroupAddressFamilyPrefixListOut_Type()
)
juniBgpPeerGroupAddressFamilyPrefixListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyPrefixListOut.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyPrefixTreeIn_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyPrefixTreeIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyPrefixTreeIn_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyPrefixTreeIn_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyPrefixTreeIn = _JuniBgpPeerGroupAddressFamilyPrefixTreeIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 12),
    _JuniBgpPeerGroupAddressFamilyPrefixTreeIn_Type()
)
juniBgpPeerGroupAddressFamilyPrefixTreeIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyPrefixTreeIn.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyPrefixTreeOut_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyPrefixTreeOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyPrefixTreeOut_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyPrefixTreeOut_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyPrefixTreeOut = _JuniBgpPeerGroupAddressFamilyPrefixTreeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 13),
    _JuniBgpPeerGroupAddressFamilyPrefixTreeOut_Type()
)
juniBgpPeerGroupAddressFamilyPrefixTreeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyPrefixTreeOut.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyFilterListIn_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyFilterListIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyFilterListIn_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyFilterListIn_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyFilterListIn = _JuniBgpPeerGroupAddressFamilyFilterListIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 14),
    _JuniBgpPeerGroupAddressFamilyFilterListIn_Type()
)
juniBgpPeerGroupAddressFamilyFilterListIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyFilterListIn.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyFilterListOut_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyFilterListOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyFilterListOut_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyFilterListOut_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyFilterListOut = _JuniBgpPeerGroupAddressFamilyFilterListOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 15),
    _JuniBgpPeerGroupAddressFamilyFilterListOut_Type()
)
juniBgpPeerGroupAddressFamilyFilterListOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyFilterListOut.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyFilterListWeight_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyFilterListWeight based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyFilterListWeight_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyFilterListWeight_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyFilterListWeight = _JuniBgpPeerGroupAddressFamilyFilterListWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 16),
    _JuniBgpPeerGroupAddressFamilyFilterListWeight_Type()
)
juniBgpPeerGroupAddressFamilyFilterListWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyFilterListWeight.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyFilterListWeightValue_Type(Unsigned32):
    """Custom type juniBgpPeerGroupAddressFamilyFilterListWeightValue based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupAddressFamilyFilterListWeightValue_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyFilterListWeightValue = _JuniBgpPeerGroupAddressFamilyFilterListWeightValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 17),
    _JuniBgpPeerGroupAddressFamilyFilterListWeightValue_Type()
)
juniBgpPeerGroupAddressFamilyFilterListWeightValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyFilterListWeightValue.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyRouteMapIn_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyRouteMapIn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyRouteMapIn_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyRouteMapIn_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRouteMapIn = _JuniBgpPeerGroupAddressFamilyRouteMapIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 18),
    _JuniBgpPeerGroupAddressFamilyRouteMapIn_Type()
)
juniBgpPeerGroupAddressFamilyRouteMapIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRouteMapIn.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyRouteMapOut_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyRouteMapOut based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyRouteMapOut_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyRouteMapOut_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRouteMapOut = _JuniBgpPeerGroupAddressFamilyRouteMapOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 19),
    _JuniBgpPeerGroupAddressFamilyRouteMapOut_Type()
)
juniBgpPeerGroupAddressFamilyRouteMapOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRouteMapOut.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyRouteReflectorClient_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyRouteReflectorClient based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyRouteReflectorClient_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRouteReflectorClient = _JuniBgpPeerGroupAddressFamilyRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 20),
    _JuniBgpPeerGroupAddressFamilyRouteReflectorClient_Type()
)
juniBgpPeerGroupAddressFamilyRouteReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRouteReflectorClient.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyRouteLimitWarn_Type(Unsigned32):
    """Custom type juniBgpPeerGroupAddressFamilyRouteLimitWarn based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupAddressFamilyRouteLimitWarn_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRouteLimitWarn = _JuniBgpPeerGroupAddressFamilyRouteLimitWarn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 21),
    _JuniBgpPeerGroupAddressFamilyRouteLimitWarn_Type()
)
juniBgpPeerGroupAddressFamilyRouteLimitWarn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRouteLimitWarn.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyRouteLimitReset_Type(Unsigned32):
    """Custom type juniBgpPeerGroupAddressFamilyRouteLimitReset based on Unsigned32"""
    defaultValue = 0


_JuniBgpPeerGroupAddressFamilyRouteLimitReset_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRouteLimitReset = _JuniBgpPeerGroupAddressFamilyRouteLimitReset_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 22),
    _JuniBgpPeerGroupAddressFamilyRouteLimitReset_Type()
)
juniBgpPeerGroupAddressFamilyRouteLimitReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRouteLimitReset.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly = _JuniBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 23),
    _JuniBgpPeerGroupAddressFamilyRouteLimitWarnOnly_Type()
)
juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyRemovePrivateAs_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyRemovePrivateAs based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyRemovePrivateAs_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRemovePrivateAs = _JuniBgpPeerGroupAddressFamilyRemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 24),
    _JuniBgpPeerGroupAddressFamilyRemovePrivateAs_Type()
)
juniBgpPeerGroupAddressFamilyRemovePrivateAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRemovePrivateAs.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyUnsuppressMap_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyUnsuppressMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyUnsuppressMap_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyUnsuppressMap_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyUnsuppressMap = _JuniBgpPeerGroupAddressFamilyUnsuppressMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 25),
    _JuniBgpPeerGroupAddressFamilyUnsuppressMap_Type()
)
juniBgpPeerGroupAddressFamilyUnsuppressMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyUnsuppressMap.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyInboundSoftReconfig_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyInboundSoftReconfig based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyInboundSoftReconfig_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyInboundSoftReconfig = _JuniBgpPeerGroupAddressFamilyInboundSoftReconfig_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 26),
    _JuniBgpPeerGroupAddressFamilyInboundSoftReconfig_Type()
)
juniBgpPeerGroupAddressFamilyInboundSoftReconfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyInboundSoftReconfig.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyResetConnectionType_Type(JuniBgpResetConnectionType):
    """Custom type juniBgpPeerGroupAddressFamilyResetConnectionType based on JuniBgpResetConnectionType"""


_JuniBgpPeerGroupAddressFamilyResetConnectionType_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyResetConnectionType = _JuniBgpPeerGroupAddressFamilyResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 27),
    _JuniBgpPeerGroupAddressFamilyResetConnectionType_Type()
)
juniBgpPeerGroupAddressFamilyResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyResetConnectionType.setStatus("current")
_JuniBgpPeerGroupAddressFamilyRowStatus_Type = RowStatus
_JuniBgpPeerGroupAddressFamilyRowStatus_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyRowStatus = _JuniBgpPeerGroupAddressFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 28),
    _JuniBgpPeerGroupAddressFamilyRowStatus_Type()
)
juniBgpPeerGroupAddressFamilyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyRowStatus.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyAsOverride_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyAsOverride based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyAsOverride_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyAsOverride = _JuniBgpPeerGroupAddressFamilyAsOverride_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 29),
    _JuniBgpPeerGroupAddressFamilyAsOverride_Type()
)
juniBgpPeerGroupAddressFamilyAsOverride.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyAsOverride.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyAllowAsIn_Type(Integer32):
    """Custom type juniBgpPeerGroupAddressFamilyAllowAsIn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_JuniBgpPeerGroupAddressFamilyAllowAsIn_Type.__name__ = "Integer32"
_JuniBgpPeerGroupAddressFamilyAllowAsIn_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyAllowAsIn = _JuniBgpPeerGroupAddressFamilyAllowAsIn_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 30),
    _JuniBgpPeerGroupAddressFamilyAllowAsIn_Type()
)
juniBgpPeerGroupAddressFamilyAllowAsIn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyAllowAsIn.setStatus("current")


class _JuniBgpPeerGroupAddressFamilySendExtendedCommunity_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilySendExtendedCommunity based on TruthValue"""


_JuniBgpPeerGroupAddressFamilySendExtendedCommunity_Object = MibTableColumn
juniBgpPeerGroupAddressFamilySendExtendedCommunity = _JuniBgpPeerGroupAddressFamilySendExtendedCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 31),
    _JuniBgpPeerGroupAddressFamilySendExtendedCommunity_Type()
)
juniBgpPeerGroupAddressFamilySendExtendedCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilySendExtendedCommunity.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend = _JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 32),
    _JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend_Type()
)
juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend = _JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 33),
    _JuniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend_Type()
)
juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyMaximumPrefixStrict_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyMaximumPrefixStrict based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyMaximumPrefixStrict_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyMaximumPrefixStrict = _JuniBgpPeerGroupAddressFamilyMaximumPrefixStrict_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 34),
    _JuniBgpPeerGroupAddressFamilyMaximumPrefixStrict_Type()
)
juniBgpPeerGroupAddressFamilyMaximumPrefixStrict.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyMaximumPrefixStrict.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpPeerGroupAddressFamilyUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfCiscoSend", 26),
          ("juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend", 25),
          ("juniBgpPeerGroupAddressFamilyAllowAsIn", 23),
          ("juniBgpPeerGroupAddressFamilyAsOverride", 22),
          ("juniBgpPeerGroupAddressFamilyDefaultOriginate", 0),
          ("juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap", 29),
          ("juniBgpPeerGroupAddressFamilyDistributeListIn", 3),
          ("juniBgpPeerGroupAddressFamilyDistributeListOut", 4),
          ("juniBgpPeerGroupAddressFamilyFilterListIn", 9),
          ("juniBgpPeerGroupAddressFamilyFilterListOut", 10),
          ("juniBgpPeerGroupAddressFamilyFilterListWeight", 11),
          ("juniBgpPeerGroupAddressFamilyFilterListWeightValue", 12),
          ("juniBgpPeerGroupAddressFamilyInboundSoftReconfig", 21),
          ("juniBgpPeerGroupAddressFamilyMaximumPrefixStrict", 27),
          ("juniBgpPeerGroupAddressFamilyNextHopSelf", 1),
          ("juniBgpPeerGroupAddressFamilyNextHopUnchanged", 30),
          ("juniBgpPeerGroupAddressFamilyPrefixListIn", 5),
          ("juniBgpPeerGroupAddressFamilyPrefixListOut", 6),
          ("juniBgpPeerGroupAddressFamilyPrefixTreeIn", 7),
          ("juniBgpPeerGroupAddressFamilyPrefixTreeOut", 8),
          ("juniBgpPeerGroupAddressFamilyRemovePrivateAs", 19),
          ("juniBgpPeerGroupAddressFamilyRouteLimitReset", 17),
          ("juniBgpPeerGroupAddressFamilyRouteLimitWarn", 16),
          ("juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly", 18),
          ("juniBgpPeerGroupAddressFamilyRouteMapIn", 13),
          ("juniBgpPeerGroupAddressFamilyRouteMapOut", 14),
          ("juniBgpPeerGroupAddressFamilyRouteReflectorClient", 15),
          ("juniBgpPeerGroupAddressFamilySendCommunity", 2),
          ("juniBgpPeerGroupAddressFamilySendExtendedCommunity", 24),
          ("juniBgpPeerGroupAddressFamilySendLabel", 28),
          ("juniBgpPeerGroupAddressFamilyUnsuppressMap", 20))
    )

_JuniBgpPeerGroupAddressFamilyUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpPeerGroupAddressFamilyUnconfiguredAttributes_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyUnconfiguredAttributes = _JuniBgpPeerGroupAddressFamilyUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 35),
    _JuniBgpPeerGroupAddressFamilyUnconfiguredAttributes_Type()
)
juniBgpPeerGroupAddressFamilyUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyUnconfiguredAttributes.setStatus("current")


class _JuniBgpPeerGroupAddressFamilySendLabel_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilySendLabel based on TruthValue"""


_JuniBgpPeerGroupAddressFamilySendLabel_Object = MibTableColumn
juniBgpPeerGroupAddressFamilySendLabel = _JuniBgpPeerGroupAddressFamilySendLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 36),
    _JuniBgpPeerGroupAddressFamilySendLabel_Type()
)
juniBgpPeerGroupAddressFamilySendLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilySendLabel.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap_Type(DisplayString):
    """Custom type juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap_Type.__name__ = "DisplayString"
_JuniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap = _JuniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 37),
    _JuniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap_Type()
)
juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyNextHopUnchanged_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyNextHopUnchanged based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyNextHopUnchanged_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyNextHopUnchanged = _JuniBgpPeerGroupAddressFamilyNextHopUnchanged_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 10, 1, 38),
    _JuniBgpPeerGroupAddressFamilyNextHopUnchanged_Type()
)
juniBgpPeerGroupAddressFamilyNextHopUnchanged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyNextHopUnchanged.setStatus("current")
_JuniBgpRouteFlapHistoryTable_Object = MibTable
juniBgpRouteFlapHistoryTable = _JuniBgpRouteFlapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12)
)
if mibBuilder.loadTexts:
    juniBgpRouteFlapHistoryTable.setStatus("obsolete")
_JuniBgpRouteFlapHistoryEntry_Object = MibTableRow
juniBgpRouteFlapHistoryEntry = _JuniBgpRouteFlapHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1)
)
juniBgpRouteFlapHistoryEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteRouteType"),
)
if mibBuilder.loadTexts:
    juniBgpRouteFlapHistoryEntry.setStatus("obsolete")


class _JuniBgpRouteFlapState_Type(Integer32):
    """Custom type juniBgpRouteFlapState based on Integer32"""
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


_JuniBgpRouteFlapState_Type.__name__ = "Integer32"
_JuniBgpRouteFlapState_Object = MibTableColumn
juniBgpRouteFlapState = _JuniBgpRouteFlapState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 1),
    _JuniBgpRouteFlapState_Type()
)
juniBgpRouteFlapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapState.setStatus("obsolete")
_JuniBgpRouteFlapFigureOfMerit_Type = Unsigned32
_JuniBgpRouteFlapFigureOfMerit_Object = MibTableColumn
juniBgpRouteFlapFigureOfMerit = _JuniBgpRouteFlapFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 2),
    _JuniBgpRouteFlapFigureOfMerit_Type()
)
juniBgpRouteFlapFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapFigureOfMerit.setStatus("obsolete")
_JuniBgpRouteFlapRemainingTime_Type = Unsigned32
_JuniBgpRouteFlapRemainingTime_Object = MibTableColumn
juniBgpRouteFlapRemainingTime = _JuniBgpRouteFlapRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 3),
    _JuniBgpRouteFlapRemainingTime_Type()
)
juniBgpRouteFlapRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapRemainingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniBgpRouteFlapRemainingTime.setUnits("seconds")
_JuniBgpRouteFlapSuppressThreshold_Type = Unsigned32
_JuniBgpRouteFlapSuppressThreshold_Object = MibTableColumn
juniBgpRouteFlapSuppressThreshold = _JuniBgpRouteFlapSuppressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 4),
    _JuniBgpRouteFlapSuppressThreshold_Type()
)
juniBgpRouteFlapSuppressThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapSuppressThreshold.setStatus("obsolete")
_JuniBgpRouteFlapReuseThreshold_Type = Unsigned32
_JuniBgpRouteFlapReuseThreshold_Object = MibTableColumn
juniBgpRouteFlapReuseThreshold = _JuniBgpRouteFlapReuseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 5),
    _JuniBgpRouteFlapReuseThreshold_Type()
)
juniBgpRouteFlapReuseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapReuseThreshold.setStatus("obsolete")
_JuniBgpRouteFlapMaxHoldDownTime_Type = Unsigned32
_JuniBgpRouteFlapMaxHoldDownTime_Object = MibTableColumn
juniBgpRouteFlapMaxHoldDownTime = _JuniBgpRouteFlapMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 6),
    _JuniBgpRouteFlapMaxHoldDownTime_Type()
)
juniBgpRouteFlapMaxHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapMaxHoldDownTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniBgpRouteFlapMaxHoldDownTime.setUnits("seconds")
_JuniBgpRouteFlapHalfLifeReachable_Type = Unsigned32
_JuniBgpRouteFlapHalfLifeReachable_Object = MibTableColumn
juniBgpRouteFlapHalfLifeReachable = _JuniBgpRouteFlapHalfLifeReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 7),
    _JuniBgpRouteFlapHalfLifeReachable_Type()
)
juniBgpRouteFlapHalfLifeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapHalfLifeReachable.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniBgpRouteFlapHalfLifeReachable.setUnits("seconds")
_JuniBgpRouteFlapHalfLifeUnreachable_Type = Unsigned32
_JuniBgpRouteFlapHalfLifeUnreachable_Object = MibTableColumn
juniBgpRouteFlapHalfLifeUnreachable = _JuniBgpRouteFlapHalfLifeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 12, 1, 8),
    _JuniBgpRouteFlapHalfLifeUnreachable_Type()
)
juniBgpRouteFlapHalfLifeUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteFlapHalfLifeUnreachable.setStatus("obsolete")
if mibBuilder.loadTexts:
    juniBgpRouteFlapHalfLifeUnreachable.setUnits("seconds")
_JuniBgpRouteTable_Object = MibTable
juniBgpRouteTable = _JuniBgpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13)
)
if mibBuilder.loadTexts:
    juniBgpRouteTable.setStatus("obsolete")
_JuniBgpRouteEntry_Object = MibTableRow
juniBgpRouteEntry = _JuniBgpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1)
)
juniBgpRouteEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteRouteType"),
)
if mibBuilder.loadTexts:
    juniBgpRouteEntry.setStatus("obsolete")
_JuniBgpRouteOriginatorId_Type = IpAddress
_JuniBgpRouteOriginatorId_Object = MibTableColumn
juniBgpRouteOriginatorId = _JuniBgpRouteOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 1),
    _JuniBgpRouteOriginatorId_Type()
)
juniBgpRouteOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteOriginatorId.setStatus("obsolete")
_JuniBgpRouteAtomicAggregatePresent_Type = TruthValue
_JuniBgpRouteAtomicAggregatePresent_Object = MibTableColumn
juniBgpRouteAtomicAggregatePresent = _JuniBgpRouteAtomicAggregatePresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 2),
    _JuniBgpRouteAtomicAggregatePresent_Type()
)
juniBgpRouteAtomicAggregatePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteAtomicAggregatePresent.setStatus("obsolete")
_JuniBgpRouteMedPresent_Type = TruthValue
_JuniBgpRouteMedPresent_Object = MibTableColumn
juniBgpRouteMedPresent = _JuniBgpRouteMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 3),
    _JuniBgpRouteMedPresent_Type()
)
juniBgpRouteMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteMedPresent.setStatus("obsolete")
_JuniBgpRouteLocalPrefPresent_Type = TruthValue
_JuniBgpRouteLocalPrefPresent_Object = MibTableColumn
juniBgpRouteLocalPrefPresent = _JuniBgpRouteLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 4),
    _JuniBgpRouteLocalPrefPresent_Type()
)
juniBgpRouteLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteLocalPrefPresent.setStatus("obsolete")
_JuniBgpRouteAggregatorPresent_Type = TruthValue
_JuniBgpRouteAggregatorPresent_Object = MibTableColumn
juniBgpRouteAggregatorPresent = _JuniBgpRouteAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 5),
    _JuniBgpRouteAggregatorPresent_Type()
)
juniBgpRouteAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteAggregatorPresent.setStatus("obsolete")
_JuniBgpRouteCommunitiesPresent_Type = TruthValue
_JuniBgpRouteCommunitiesPresent_Object = MibTableColumn
juniBgpRouteCommunitiesPresent = _JuniBgpRouteCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 6),
    _JuniBgpRouteCommunitiesPresent_Type()
)
juniBgpRouteCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteCommunitiesPresent.setStatus("obsolete")
_JuniBgpRouteOriginatorIdPresent_Type = TruthValue
_JuniBgpRouteOriginatorIdPresent_Object = MibTableColumn
juniBgpRouteOriginatorIdPresent = _JuniBgpRouteOriginatorIdPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 7),
    _JuniBgpRouteOriginatorIdPresent_Type()
)
juniBgpRouteOriginatorIdPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteOriginatorIdPresent.setStatus("obsolete")
_JuniBgpRouteClusterListPresent_Type = TruthValue
_JuniBgpRouteClusterListPresent_Object = MibTableColumn
juniBgpRouteClusterListPresent = _JuniBgpRouteClusterListPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 8),
    _JuniBgpRouteClusterListPresent_Type()
)
juniBgpRouteClusterListPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteClusterListPresent.setStatus("obsolete")
_JuniBgpRouteWeight_Type = Unsigned32
_JuniBgpRouteWeight_Object = MibTableColumn
juniBgpRouteWeight = _JuniBgpRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 9),
    _JuniBgpRouteWeight_Type()
)
juniBgpRouteWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteWeight.setStatus("obsolete")
_JuniBgpRouteVrfName_Type = JuniVrfName
_JuniBgpRouteVrfName_Object = MibTableColumn
juniBgpRouteVrfName = _JuniBgpRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 10),
    _JuniBgpRouteVrfName_Type()
)
juniBgpRouteVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpRouteVrfName.setStatus("obsolete")
_JuniBgpRouteAfi_Type = JuniBgpAfi
_JuniBgpRouteAfi_Object = MibTableColumn
juniBgpRouteAfi = _JuniBgpRouteAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 11),
    _JuniBgpRouteAfi_Type()
)
juniBgpRouteAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpRouteAfi.setStatus("obsolete")
_JuniBgpRouteSafi_Type = JuniBgpSafi
_JuniBgpRouteSafi_Object = MibTableColumn
juniBgpRouteSafi = _JuniBgpRouteSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 12),
    _JuniBgpRouteSafi_Type()
)
juniBgpRouteSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpRouteSafi.setStatus("obsolete")
_JuniBgpRoutePeer_Type = IpAddress
_JuniBgpRoutePeer_Object = MibTableColumn
juniBgpRoutePeer = _JuniBgpRoutePeer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 13),
    _JuniBgpRoutePeer_Type()
)
juniBgpRoutePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpRoutePeer.setStatus("obsolete")


class _JuniBgpRouteIpAddrPrefixLen_Type(Integer32):
    """Custom type juniBgpRouteIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniBgpRouteIpAddrPrefixLen_Type.__name__ = "Integer32"
_JuniBgpRouteIpAddrPrefixLen_Object = MibTableColumn
juniBgpRouteIpAddrPrefixLen = _JuniBgpRouteIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 14),
    _JuniBgpRouteIpAddrPrefixLen_Type()
)
juniBgpRouteIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpRouteIpAddrPrefixLen.setStatus("obsolete")
_JuniBgpRouteIpAddrPrefix_Type = IpAddress
_JuniBgpRouteIpAddrPrefix_Object = MibTableColumn
juniBgpRouteIpAddrPrefix = _JuniBgpRouteIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 15),
    _JuniBgpRouteIpAddrPrefix_Type()
)
juniBgpRouteIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpRouteIpAddrPrefix.setStatus("obsolete")


class _JuniBgpRouteRouteType_Type(Integer32):
    """Custom type juniBgpRouteRouteType based on Integer32"""
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


_JuniBgpRouteRouteType_Type.__name__ = "Integer32"
_JuniBgpRouteRouteType_Object = MibTableColumn
juniBgpRouteRouteType = _JuniBgpRouteRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 16),
    _JuniBgpRouteRouteType_Type()
)
juniBgpRouteRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpRouteRouteType.setStatus("obsolete")


class _JuniBgpRouteOrigin_Type(Integer32):
    """Custom type juniBgpRouteOrigin based on Integer32"""
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


_JuniBgpRouteOrigin_Type.__name__ = "Integer32"
_JuniBgpRouteOrigin_Object = MibTableColumn
juniBgpRouteOrigin = _JuniBgpRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 17),
    _JuniBgpRouteOrigin_Type()
)
juniBgpRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteOrigin.setStatus("obsolete")


class _JuniBgpRouteASPathSegment_Type(OctetString):
    """Custom type juniBgpRouteASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_JuniBgpRouteASPathSegment_Type.__name__ = "OctetString"
_JuniBgpRouteASPathSegment_Object = MibTableColumn
juniBgpRouteASPathSegment = _JuniBgpRouteASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 18),
    _JuniBgpRouteASPathSegment_Type()
)
juniBgpRouteASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteASPathSegment.setStatus("obsolete")
_JuniBgpRouteNextHop_Type = IpAddress
_JuniBgpRouteNextHop_Object = MibTableColumn
juniBgpRouteNextHop = _JuniBgpRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 19),
    _JuniBgpRouteNextHop_Type()
)
juniBgpRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteNextHop.setStatus("obsolete")
_JuniBgpRouteMultiExitDisc_Type = Unsigned32
_JuniBgpRouteMultiExitDisc_Object = MibTableColumn
juniBgpRouteMultiExitDisc = _JuniBgpRouteMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 20),
    _JuniBgpRouteMultiExitDisc_Type()
)
juniBgpRouteMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteMultiExitDisc.setStatus("obsolete")
_JuniBgpRouteLocalPref_Type = Unsigned32
_JuniBgpRouteLocalPref_Object = MibTableColumn
juniBgpRouteLocalPref = _JuniBgpRouteLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 21),
    _JuniBgpRouteLocalPref_Type()
)
juniBgpRouteLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteLocalPref.setStatus("obsolete")


class _JuniBgpRouteAtomicAggregate_Type(Integer32):
    """Custom type juniBgpRouteAtomicAggregate based on Integer32"""
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


_JuniBgpRouteAtomicAggregate_Type.__name__ = "Integer32"
_JuniBgpRouteAtomicAggregate_Object = MibTableColumn
juniBgpRouteAtomicAggregate = _JuniBgpRouteAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 22),
    _JuniBgpRouteAtomicAggregate_Type()
)
juniBgpRouteAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteAtomicAggregate.setStatus("obsolete")


class _JuniBgpRouteAggregatorAS_Type(Integer32):
    """Custom type juniBgpRouteAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpRouteAggregatorAS_Type.__name__ = "Integer32"
_JuniBgpRouteAggregatorAS_Object = MibTableColumn
juniBgpRouteAggregatorAS = _JuniBgpRouteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 23),
    _JuniBgpRouteAggregatorAS_Type()
)
juniBgpRouteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteAggregatorAS.setStatus("obsolete")
_JuniBgpRouteAggregatorAddress_Type = IpAddress
_JuniBgpRouteAggregatorAddress_Object = MibTableColumn
juniBgpRouteAggregatorAddress = _JuniBgpRouteAggregatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 24),
    _JuniBgpRouteAggregatorAddress_Type()
)
juniBgpRouteAggregatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteAggregatorAddress.setStatus("obsolete")
_JuniBgpRouteBestInIpRouteTable_Type = TruthValue
_JuniBgpRouteBestInIpRouteTable_Object = MibTableColumn
juniBgpRouteBestInIpRouteTable = _JuniBgpRouteBestInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 25),
    _JuniBgpRouteBestInIpRouteTable_Type()
)
juniBgpRouteBestInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteBestInIpRouteTable.setStatus("obsolete")


class _JuniBgpRouteUnknown_Type(OctetString):
    """Custom type juniBgpRouteUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniBgpRouteUnknown_Type.__name__ = "OctetString"
_JuniBgpRouteUnknown_Object = MibTableColumn
juniBgpRouteUnknown = _JuniBgpRouteUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 26),
    _JuniBgpRouteUnknown_Type()
)
juniBgpRouteUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteUnknown.setStatus("obsolete")
_JuniBgpRouteExtendedCommunitiesPresent_Type = TruthValue
_JuniBgpRouteExtendedCommunitiesPresent_Object = MibTableColumn
juniBgpRouteExtendedCommunitiesPresent = _JuniBgpRouteExtendedCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 27),
    _JuniBgpRouteExtendedCommunitiesPresent_Type()
)
juniBgpRouteExtendedCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteExtendedCommunitiesPresent.setStatus("obsolete")
_JuniBgpRouteValid_Type = TruthValue
_JuniBgpRouteValid_Object = MibTableColumn
juniBgpRouteValid = _JuniBgpRouteValid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 28),
    _JuniBgpRouteValid_Type()
)
juniBgpRouteValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteValid.setStatus("obsolete")


class _JuniBgpRouteSuppressedBy_Type(Integer32):
    """Custom type juniBgpRouteSuppressedBy based on Integer32"""
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


_JuniBgpRouteSuppressedBy_Type.__name__ = "Integer32"
_JuniBgpRouteSuppressedBy_Object = MibTableColumn
juniBgpRouteSuppressedBy = _JuniBgpRouteSuppressedBy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 29),
    _JuniBgpRouteSuppressedBy_Type()
)
juniBgpRouteSuppressedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteSuppressedBy.setStatus("obsolete")
_JuniBgpRouteNextHopReachable_Type = TruthValue
_JuniBgpRouteNextHopReachable_Object = MibTableColumn
juniBgpRouteNextHopReachable = _JuniBgpRouteNextHopReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 30),
    _JuniBgpRouteNextHopReachable_Type()
)
juniBgpRouteNextHopReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteNextHopReachable.setStatus("obsolete")
_JuniBgpRouteSynchronizedWithIgp_Type = TruthValue
_JuniBgpRouteSynchronizedWithIgp_Object = MibTableColumn
juniBgpRouteSynchronizedWithIgp = _JuniBgpRouteSynchronizedWithIgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 31),
    _JuniBgpRouteSynchronizedWithIgp_Type()
)
juniBgpRouteSynchronizedWithIgp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteSynchronizedWithIgp.setStatus("obsolete")
_JuniBgpRoutePlaceInIpRouteTable_Type = TruthValue
_JuniBgpRoutePlaceInIpRouteTable_Object = MibTableColumn
juniBgpRoutePlaceInIpRouteTable = _JuniBgpRoutePlaceInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 32),
    _JuniBgpRoutePlaceInIpRouteTable_Type()
)
juniBgpRoutePlaceInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRoutePlaceInIpRouteTable.setStatus("obsolete")
_JuniBgpRouteAdvertiseToExternalPeers_Type = TruthValue
_JuniBgpRouteAdvertiseToExternalPeers_Object = MibTableColumn
juniBgpRouteAdvertiseToExternalPeers = _JuniBgpRouteAdvertiseToExternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 33),
    _JuniBgpRouteAdvertiseToExternalPeers_Type()
)
juniBgpRouteAdvertiseToExternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteAdvertiseToExternalPeers.setStatus("obsolete")
_JuniBgpRouteAdvertiseToInternalPeers_Type = TruthValue
_JuniBgpRouteAdvertiseToInternalPeers_Object = MibTableColumn
juniBgpRouteAdvertiseToInternalPeers = _JuniBgpRouteAdvertiseToInternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 34),
    _JuniBgpRouteAdvertiseToInternalPeers_Type()
)
juniBgpRouteAdvertiseToInternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteAdvertiseToInternalPeers.setStatus("obsolete")


class _JuniBgpRouteDistinguisher_Type(OctetString):
    """Custom type juniBgpRouteDistinguisher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniBgpRouteDistinguisher_Type.__name__ = "OctetString"
_JuniBgpRouteDistinguisher_Object = MibTableColumn
juniBgpRouteDistinguisher = _JuniBgpRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 35),
    _JuniBgpRouteDistinguisher_Type()
)
juniBgpRouteDistinguisher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteDistinguisher.setStatus("obsolete")
_JuniBgpRouteMplsLabel_Type = Unsigned32
_JuniBgpRouteMplsLabel_Object = MibTableColumn
juniBgpRouteMplsLabel = _JuniBgpRouteMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 36),
    _JuniBgpRouteMplsLabel_Type()
)
juniBgpRouteMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteMplsLabel.setStatus("obsolete")
_JuniBgpRouteNextHopMetric_Type = Unsigned32
_JuniBgpRouteNextHopMetric_Object = MibTableColumn
juniBgpRouteNextHopMetric = _JuniBgpRouteNextHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 13, 1, 37),
    _JuniBgpRouteNextHopMetric_Type()
)
juniBgpRouteNextHopMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteNextHopMetric.setStatus("obsolete")
_JuniBgpRouteCommunityTable_Object = MibTable
juniBgpRouteCommunityTable = _JuniBgpRouteCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 14)
)
if mibBuilder.loadTexts:
    juniBgpRouteCommunityTable.setStatus("obsolete")
_JuniBgpRouteCommunityEntry_Object = MibTableRow
juniBgpRouteCommunityEntry = _JuniBgpRouteCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 14, 1)
)
juniBgpRouteCommunityEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteCommunityNumber"),
)
if mibBuilder.loadTexts:
    juniBgpRouteCommunityEntry.setStatus("obsolete")
_JuniBgpRouteCommunityNumber_Type = Unsigned32
_JuniBgpRouteCommunityNumber_Object = MibTableColumn
juniBgpRouteCommunityNumber = _JuniBgpRouteCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 14, 1, 1),
    _JuniBgpRouteCommunityNumber_Type()
)
juniBgpRouteCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteCommunityNumber.setStatus("obsolete")
_JuniBgpRouteClusterIdTable_Object = MibTable
juniBgpRouteClusterIdTable = _JuniBgpRouteClusterIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 15)
)
if mibBuilder.loadTexts:
    juniBgpRouteClusterIdTable.setStatus("obsolete")
_JuniBgpRouteClusterIdEntry_Object = MibTableRow
juniBgpRouteClusterIdEntry = _JuniBgpRouteClusterIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 15, 1)
)
juniBgpRouteClusterIdEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteClusterId"),
)
if mibBuilder.loadTexts:
    juniBgpRouteClusterIdEntry.setStatus("obsolete")
_JuniBgpRouteClusterId_Type = Unsigned32
_JuniBgpRouteClusterId_Object = MibTableColumn
juniBgpRouteClusterId = _JuniBgpRouteClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 15, 1, 1),
    _JuniBgpRouteClusterId_Type()
)
juniBgpRouteClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteClusterId.setStatus("obsolete")
_JuniBgpNetworkTable_Object = MibTable
juniBgpNetworkTable = _JuniBgpNetworkTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16)
)
if mibBuilder.loadTexts:
    juniBgpNetworkTable.setStatus("current")
_JuniBgpNetworkEntry_Object = MibTableRow
juniBgpNetworkEntry = _JuniBgpNetworkEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1)
)
juniBgpNetworkEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpNetworkVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpNetworkAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpNetworkSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpNetworkIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpNetworkIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    juniBgpNetworkEntry.setStatus("current")
_JuniBgpNetworkVrfName_Type = JuniVrfName
_JuniBgpNetworkVrfName_Object = MibTableColumn
juniBgpNetworkVrfName = _JuniBgpNetworkVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 1),
    _JuniBgpNetworkVrfName_Type()
)
juniBgpNetworkVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNetworkVrfName.setStatus("current")
_JuniBgpNetworkAfi_Type = JuniBgpAfi
_JuniBgpNetworkAfi_Object = MibTableColumn
juniBgpNetworkAfi = _JuniBgpNetworkAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 2),
    _JuniBgpNetworkAfi_Type()
)
juniBgpNetworkAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNetworkAfi.setStatus("current")
_JuniBgpNetworkSafi_Type = JuniBgpSafi
_JuniBgpNetworkSafi_Object = MibTableColumn
juniBgpNetworkSafi = _JuniBgpNetworkSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 3),
    _JuniBgpNetworkSafi_Type()
)
juniBgpNetworkSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNetworkSafi.setStatus("current")
_JuniBgpNetworkIpAddrPrefix_Type = IpAddress
_JuniBgpNetworkIpAddrPrefix_Object = MibTableColumn
juniBgpNetworkIpAddrPrefix = _JuniBgpNetworkIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 4),
    _JuniBgpNetworkIpAddrPrefix_Type()
)
juniBgpNetworkIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNetworkIpAddrPrefix.setStatus("current")


class _JuniBgpNetworkIpAddrPrefixLen_Type(Integer32):
    """Custom type juniBgpNetworkIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniBgpNetworkIpAddrPrefixLen_Type.__name__ = "Integer32"
_JuniBgpNetworkIpAddrPrefixLen_Object = MibTableColumn
juniBgpNetworkIpAddrPrefixLen = _JuniBgpNetworkIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 5),
    _JuniBgpNetworkIpAddrPrefixLen_Type()
)
juniBgpNetworkIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNetworkIpAddrPrefixLen.setStatus("current")


class _JuniBgpNetworkBackdoor_Type(TruthValue):
    """Custom type juniBgpNetworkBackdoor based on TruthValue"""


_JuniBgpNetworkBackdoor_Object = MibTableColumn
juniBgpNetworkBackdoor = _JuniBgpNetworkBackdoor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 6),
    _JuniBgpNetworkBackdoor_Type()
)
juniBgpNetworkBackdoor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpNetworkBackdoor.setStatus("current")
_JuniBgpNetworkRowStatus_Type = RowStatus
_JuniBgpNetworkRowStatus_Object = MibTableColumn
juniBgpNetworkRowStatus = _JuniBgpNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 7),
    _JuniBgpNetworkRowStatus_Type()
)
juniBgpNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpNetworkRowStatus.setStatus("current")


class _JuniBgpNetworkWeightSpecified_Type(TruthValue):
    """Custom type juniBgpNetworkWeightSpecified based on TruthValue"""


_JuniBgpNetworkWeightSpecified_Object = MibTableColumn
juniBgpNetworkWeightSpecified = _JuniBgpNetworkWeightSpecified_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 8),
    _JuniBgpNetworkWeightSpecified_Type()
)
juniBgpNetworkWeightSpecified.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpNetworkWeightSpecified.setStatus("current")


class _JuniBgpNetworkWeight_Type(Integer32):
    """Custom type juniBgpNetworkWeight based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpNetworkWeight_Type.__name__ = "Integer32"
_JuniBgpNetworkWeight_Object = MibTableColumn
juniBgpNetworkWeight = _JuniBgpNetworkWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 9),
    _JuniBgpNetworkWeight_Type()
)
juniBgpNetworkWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpNetworkWeight.setStatus("current")


class _JuniBgpNetworkRouteMap_Type(DisplayString):
    """Custom type juniBgpNetworkRouteMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpNetworkRouteMap_Type.__name__ = "DisplayString"
_JuniBgpNetworkRouteMap_Object = MibTableColumn
juniBgpNetworkRouteMap = _JuniBgpNetworkRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 10),
    _JuniBgpNetworkRouteMap_Type()
)
juniBgpNetworkRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpNetworkRouteMap.setStatus("current")


class _JuniBgpNetworkUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpNetworkUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpNetworkBackdoor", 0),
          ("juniBgpNetworkRouteMap", 2),
          ("juniBgpNetworkWeight", 1))
    )

_JuniBgpNetworkUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpNetworkUnconfiguredAttributes_Object = MibTableColumn
juniBgpNetworkUnconfiguredAttributes = _JuniBgpNetworkUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 16, 1, 11),
    _JuniBgpNetworkUnconfiguredAttributes_Type()
)
juniBgpNetworkUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpNetworkUnconfiguredAttributes.setStatus("current")
_JuniBgpAggregateTable_Object = MibTable
juniBgpAggregateTable = _JuniBgpAggregateTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17)
)
if mibBuilder.loadTexts:
    juniBgpAggregateTable.setStatus("current")
_JuniBgpAggregateEntry_Object = MibTableRow
juniBgpAggregateEntry = _JuniBgpAggregateEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1)
)
juniBgpAggregateEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpAggregateVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpAggregateAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpAggregateSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpAggregateIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpAggregateIpAddrPrefixLen"),
)
if mibBuilder.loadTexts:
    juniBgpAggregateEntry.setStatus("current")
_JuniBgpAggregateVrfName_Type = JuniVrfName
_JuniBgpAggregateVrfName_Object = MibTableColumn
juniBgpAggregateVrfName = _JuniBgpAggregateVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 1),
    _JuniBgpAggregateVrfName_Type()
)
juniBgpAggregateVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAggregateVrfName.setStatus("current")
_JuniBgpAggregateAfi_Type = JuniBgpAfi
_JuniBgpAggregateAfi_Object = MibTableColumn
juniBgpAggregateAfi = _JuniBgpAggregateAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 2),
    _JuniBgpAggregateAfi_Type()
)
juniBgpAggregateAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAggregateAfi.setStatus("current")
_JuniBgpAggregateSafi_Type = JuniBgpSafi
_JuniBgpAggregateSafi_Object = MibTableColumn
juniBgpAggregateSafi = _JuniBgpAggregateSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 3),
    _JuniBgpAggregateSafi_Type()
)
juniBgpAggregateSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAggregateSafi.setStatus("current")
_JuniBgpAggregateIpAddrPrefix_Type = IpAddress
_JuniBgpAggregateIpAddrPrefix_Object = MibTableColumn
juniBgpAggregateIpAddrPrefix = _JuniBgpAggregateIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 4),
    _JuniBgpAggregateIpAddrPrefix_Type()
)
juniBgpAggregateIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAggregateIpAddrPrefix.setStatus("current")


class _JuniBgpAggregateIpAddrPrefixLen_Type(Integer32):
    """Custom type juniBgpAggregateIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniBgpAggregateIpAddrPrefixLen_Type.__name__ = "Integer32"
_JuniBgpAggregateIpAddrPrefixLen_Object = MibTableColumn
juniBgpAggregateIpAddrPrefixLen = _JuniBgpAggregateIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 5),
    _JuniBgpAggregateIpAddrPrefixLen_Type()
)
juniBgpAggregateIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAggregateIpAddrPrefixLen.setStatus("current")


class _JuniBgpAggregateAsSet_Type(TruthValue):
    """Custom type juniBgpAggregateAsSet based on TruthValue"""


_JuniBgpAggregateAsSet_Object = MibTableColumn
juniBgpAggregateAsSet = _JuniBgpAggregateAsSet_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 6),
    _JuniBgpAggregateAsSet_Type()
)
juniBgpAggregateAsSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAggregateAsSet.setStatus("current")


class _JuniBgpAggregateSummaryOnly_Type(TruthValue):
    """Custom type juniBgpAggregateSummaryOnly based on TruthValue"""


_JuniBgpAggregateSummaryOnly_Object = MibTableColumn
juniBgpAggregateSummaryOnly = _JuniBgpAggregateSummaryOnly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 7),
    _JuniBgpAggregateSummaryOnly_Type()
)
juniBgpAggregateSummaryOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAggregateSummaryOnly.setStatus("current")


class _JuniBgpAggregateAttributeMap_Type(DisplayString):
    """Custom type juniBgpAggregateAttributeMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpAggregateAttributeMap_Type.__name__ = "DisplayString"
_JuniBgpAggregateAttributeMap_Object = MibTableColumn
juniBgpAggregateAttributeMap = _JuniBgpAggregateAttributeMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 8),
    _JuniBgpAggregateAttributeMap_Type()
)
juniBgpAggregateAttributeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAggregateAttributeMap.setStatus("current")


class _JuniBgpAggregateAdvertiseMap_Type(DisplayString):
    """Custom type juniBgpAggregateAdvertiseMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpAggregateAdvertiseMap_Type.__name__ = "DisplayString"
_JuniBgpAggregateAdvertiseMap_Object = MibTableColumn
juniBgpAggregateAdvertiseMap = _JuniBgpAggregateAdvertiseMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 9),
    _JuniBgpAggregateAdvertiseMap_Type()
)
juniBgpAggregateAdvertiseMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAggregateAdvertiseMap.setStatus("current")
_JuniBgpAggregateRowStatus_Type = RowStatus
_JuniBgpAggregateRowStatus_Object = MibTableColumn
juniBgpAggregateRowStatus = _JuniBgpAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 10),
    _JuniBgpAggregateRowStatus_Type()
)
juniBgpAggregateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAggregateRowStatus.setStatus("current")


class _JuniBgpAggregateSuppressMap_Type(DisplayString):
    """Custom type juniBgpAggregateSuppressMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpAggregateSuppressMap_Type.__name__ = "DisplayString"
_JuniBgpAggregateSuppressMap_Object = MibTableColumn
juniBgpAggregateSuppressMap = _JuniBgpAggregateSuppressMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 11),
    _JuniBgpAggregateSuppressMap_Type()
)
juniBgpAggregateSuppressMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAggregateSuppressMap.setStatus("current")


class _JuniBgpAggregateUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpAggregateUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpAggregateAdvertiseMap", 3),
          ("juniBgpAggregateAsSet", 0),
          ("juniBgpAggregateAttributeMap", 2),
          ("juniBgpAggregateSummaryOnly", 1),
          ("juniBgpAggregateSuppressMap", 4))
    )

_JuniBgpAggregateUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpAggregateUnconfiguredAttributes_Object = MibTableColumn
juniBgpAggregateUnconfiguredAttributes = _JuniBgpAggregateUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 17, 1, 12),
    _JuniBgpAggregateUnconfiguredAttributes_Type()
)
juniBgpAggregateUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAggregateUnconfiguredAttributes.setStatus("current")
_JuniBgpVrfTable_Object = MibTable
juniBgpVrfTable = _JuniBgpVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18)
)
if mibBuilder.loadTexts:
    juniBgpVrfTable.setStatus("current")
_JuniBgpVrfEntry_Object = MibTableRow
juniBgpVrfEntry = _JuniBgpVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1)
)
juniBgpVrfEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpVrfName"),
)
if mibBuilder.loadTexts:
    juniBgpVrfEntry.setStatus("current")
_JuniBgpVrfName_Type = JuniVrfName
_JuniBgpVrfName_Object = MibTableColumn
juniBgpVrfName = _JuniBgpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 1),
    _JuniBgpVrfName_Type()
)
juniBgpVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpVrfName.setStatus("current")


class _JuniBgpVrfSynchronization_Type(TruthValue):
    """Custom type juniBgpVrfSynchronization based on TruthValue"""


_JuniBgpVrfSynchronization_Object = MibTableColumn
juniBgpVrfSynchronization = _JuniBgpVrfSynchronization_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 2),
    _JuniBgpVrfSynchronization_Type()
)
juniBgpVrfSynchronization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfSynchronization.setStatus("current")


class _JuniBgpVrfAutoSummary_Type(TruthValue):
    """Custom type juniBgpVrfAutoSummary based on TruthValue"""


_JuniBgpVrfAutoSummary_Object = MibTableColumn
juniBgpVrfAutoSummary = _JuniBgpVrfAutoSummary_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 3),
    _JuniBgpVrfAutoSummary_Type()
)
juniBgpVrfAutoSummary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfAutoSummary.setStatus("current")


class _JuniBgpVrfExternalDistance_Type(Integer32):
    """Custom type juniBgpVrfExternalDistance based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpVrfExternalDistance_Type.__name__ = "Integer32"
_JuniBgpVrfExternalDistance_Object = MibTableColumn
juniBgpVrfExternalDistance = _JuniBgpVrfExternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 4),
    _JuniBgpVrfExternalDistance_Type()
)
juniBgpVrfExternalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfExternalDistance.setStatus("obsolete")


class _JuniBgpVrfInternalDistance_Type(Integer32):
    """Custom type juniBgpVrfInternalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpVrfInternalDistance_Type.__name__ = "Integer32"
_JuniBgpVrfInternalDistance_Object = MibTableColumn
juniBgpVrfInternalDistance = _JuniBgpVrfInternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 5),
    _JuniBgpVrfInternalDistance_Type()
)
juniBgpVrfInternalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfInternalDistance.setStatus("obsolete")


class _JuniBgpVrfLocalDistance_Type(Integer32):
    """Custom type juniBgpVrfLocalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpVrfLocalDistance_Type.__name__ = "Integer32"
_JuniBgpVrfLocalDistance_Object = MibTableColumn
juniBgpVrfLocalDistance = _JuniBgpVrfLocalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 6),
    _JuniBgpVrfLocalDistance_Type()
)
juniBgpVrfLocalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfLocalDistance.setStatus("obsolete")


class _JuniBgpVrfResetConnectionType_Type(JuniBgpResetConnectionType):
    """Custom type juniBgpVrfResetConnectionType based on JuniBgpResetConnectionType"""


_JuniBgpVrfResetConnectionType_Object = MibTableColumn
juniBgpVrfResetConnectionType = _JuniBgpVrfResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 7),
    _JuniBgpVrfResetConnectionType_Type()
)
juniBgpVrfResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfResetConnectionType.setStatus("current")
_JuniBgpVrfRowStatus_Type = RowStatus
_JuniBgpVrfRowStatus_Object = MibTableColumn
juniBgpVrfRowStatus = _JuniBgpVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 8),
    _JuniBgpVrfRowStatus_Type()
)
juniBgpVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfRowStatus.setStatus("current")


class _JuniBgpVrfOperationalState_Type(Integer32):
    """Custom type juniBgpVrfOperationalState based on Integer32"""
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


_JuniBgpVrfOperationalState_Type.__name__ = "Integer32"
_JuniBgpVrfOperationalState_Object = MibTableColumn
juniBgpVrfOperationalState = _JuniBgpVrfOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 9),
    _JuniBgpVrfOperationalState_Type()
)
juniBgpVrfOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpVrfOperationalState.setStatus("current")


class _JuniBgpVrfAddUnicastRoutesToMulticastView_Type(TruthValue):
    """Custom type juniBgpVrfAddUnicastRoutesToMulticastView based on TruthValue"""


_JuniBgpVrfAddUnicastRoutesToMulticastView_Object = MibTableColumn
juniBgpVrfAddUnicastRoutesToMulticastView = _JuniBgpVrfAddUnicastRoutesToMulticastView_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 10),
    _JuniBgpVrfAddUnicastRoutesToMulticastView_Type()
)
juniBgpVrfAddUnicastRoutesToMulticastView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfAddUnicastRoutesToMulticastView.setStatus("current")


class _JuniBgpVrfMaximumPathsEbgp_Type(Integer32):
    """Custom type juniBgpVrfMaximumPathsEbgp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_JuniBgpVrfMaximumPathsEbgp_Type.__name__ = "Integer32"
_JuniBgpVrfMaximumPathsEbgp_Object = MibTableColumn
juniBgpVrfMaximumPathsEbgp = _JuniBgpVrfMaximumPathsEbgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 11),
    _JuniBgpVrfMaximumPathsEbgp_Type()
)
juniBgpVrfMaximumPathsEbgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfMaximumPathsEbgp.setStatus("current")


class _JuniBgpVrfMaximumPathsIbgp_Type(Integer32):
    """Custom type juniBgpVrfMaximumPathsIbgp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_JuniBgpVrfMaximumPathsIbgp_Type.__name__ = "Integer32"
_JuniBgpVrfMaximumPathsIbgp_Object = MibTableColumn
juniBgpVrfMaximumPathsIbgp = _JuniBgpVrfMaximumPathsIbgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 12),
    _JuniBgpVrfMaximumPathsIbgp_Type()
)
juniBgpVrfMaximumPathsIbgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfMaximumPathsIbgp.setStatus("current")


class _JuniBgpVrfUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpVrfUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpVrfAddUnicastRoutesToMulticastView", 5),
          ("juniBgpVrfAutoSummary", 1),
          ("juniBgpVrfExternalDistance", 2),
          ("juniBgpVrfInternalDistance", 3),
          ("juniBgpVrfLocalDistance", 4),
          ("juniBgpVrfMaximumPathsEIbgp", 8),
          ("juniBgpVrfMaximumPathsEbgp", 6),
          ("juniBgpVrfMaximumPathsIbgp", 7),
          ("juniBgpVrfSynchronization", 0))
    )

_JuniBgpVrfUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpVrfUnconfiguredAttributes_Object = MibTableColumn
juniBgpVrfUnconfiguredAttributes = _JuniBgpVrfUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 13),
    _JuniBgpVrfUnconfiguredAttributes_Type()
)
juniBgpVrfUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfUnconfiguredAttributes.setStatus("current")


class _JuniBgpVrfMaximumPathsEIbgp_Type(Integer32):
    """Custom type juniBgpVrfMaximumPathsEIbgp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_JuniBgpVrfMaximumPathsEIbgp_Type.__name__ = "Integer32"
_JuniBgpVrfMaximumPathsEIbgp_Object = MibTableColumn
juniBgpVrfMaximumPathsEIbgp = _JuniBgpVrfMaximumPathsEIbgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 14),
    _JuniBgpVrfMaximumPathsEIbgp_Type()
)
juniBgpVrfMaximumPathsEIbgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpVrfMaximumPathsEIbgp.setStatus("current")
_JuniBgpVrfCarriersCarrierModeEnabled_Type = TruthValue
_JuniBgpVrfCarriersCarrierModeEnabled_Object = MibTableColumn
juniBgpVrfCarriersCarrierModeEnabled = _JuniBgpVrfCarriersCarrierModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 18, 1, 16),
    _JuniBgpVrfCarriersCarrierModeEnabled_Type()
)
juniBgpVrfCarriersCarrierModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpVrfCarriersCarrierModeEnabled.setStatus("obsolete")
_JuniBgpAddressFamilyTable_Object = MibTable
juniBgpAddressFamilyTable = _JuniBgpAddressFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19)
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyTable.setStatus("current")
_JuniBgpAddressFamilyEntry_Object = MibTableRow
juniBgpAddressFamilyEntry = _JuniBgpAddressFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1)
)
juniBgpAddressFamilyEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpAddressFamilyVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpAddressFamilyAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpAddressFamilySafi"),
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyEntry.setStatus("current")
_JuniBgpAddressFamilyVrfName_Type = JuniVrfName
_JuniBgpAddressFamilyVrfName_Object = MibTableColumn
juniBgpAddressFamilyVrfName = _JuniBgpAddressFamilyVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 1),
    _JuniBgpAddressFamilyVrfName_Type()
)
juniBgpAddressFamilyVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyVrfName.setStatus("current")
_JuniBgpAddressFamilyAfi_Type = JuniBgpAfi
_JuniBgpAddressFamilyAfi_Object = MibTableColumn
juniBgpAddressFamilyAfi = _JuniBgpAddressFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 2),
    _JuniBgpAddressFamilyAfi_Type()
)
juniBgpAddressFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyAfi.setStatus("current")
_JuniBgpAddressFamilySafi_Type = JuniBgpSafi
_JuniBgpAddressFamilySafi_Object = MibTableColumn
juniBgpAddressFamilySafi = _JuniBgpAddressFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 3),
    _JuniBgpAddressFamilySafi_Type()
)
juniBgpAddressFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpAddressFamilySafi.setStatus("current")


class _JuniBgpAddressFamilyDefaultOriginate_Type(TruthValue):
    """Custom type juniBgpAddressFamilyDefaultOriginate based on TruthValue"""


_JuniBgpAddressFamilyDefaultOriginate_Object = MibTableColumn
juniBgpAddressFamilyDefaultOriginate = _JuniBgpAddressFamilyDefaultOriginate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 4),
    _JuniBgpAddressFamilyDefaultOriginate_Type()
)
juniBgpAddressFamilyDefaultOriginate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDefaultOriginate.setStatus("current")


class _JuniBgpAddressFamilyRouteFlapDampening_Type(TruthValue):
    """Custom type juniBgpAddressFamilyRouteFlapDampening based on TruthValue"""


_JuniBgpAddressFamilyRouteFlapDampening_Object = MibTableColumn
juniBgpAddressFamilyRouteFlapDampening = _JuniBgpAddressFamilyRouteFlapDampening_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 5),
    _JuniBgpAddressFamilyRouteFlapDampening_Type()
)
juniBgpAddressFamilyRouteFlapDampening.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyRouteFlapDampening.setStatus("current")


class _JuniBgpAddressFamilyDampeningSuppressThreshold_Type(Unsigned32):
    """Custom type juniBgpAddressFamilyDampeningSuppressThreshold based on Unsigned32"""
    defaultValue = 1000


_JuniBgpAddressFamilyDampeningSuppressThreshold_Object = MibTableColumn
juniBgpAddressFamilyDampeningSuppressThreshold = _JuniBgpAddressFamilyDampeningSuppressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 6),
    _JuniBgpAddressFamilyDampeningSuppressThreshold_Type()
)
juniBgpAddressFamilyDampeningSuppressThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningSuppressThreshold.setStatus("current")


class _JuniBgpAddressFamilyDampeningReuseThreshold_Type(Unsigned32):
    """Custom type juniBgpAddressFamilyDampeningReuseThreshold based on Unsigned32"""
    defaultValue = 1000


_JuniBgpAddressFamilyDampeningReuseThreshold_Object = MibTableColumn
juniBgpAddressFamilyDampeningReuseThreshold = _JuniBgpAddressFamilyDampeningReuseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 7),
    _JuniBgpAddressFamilyDampeningReuseThreshold_Type()
)
juniBgpAddressFamilyDampeningReuseThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningReuseThreshold.setStatus("current")


class _JuniBgpAddressFamilyDampeningMaxHoldDownTime_Type(Unsigned32):
    """Custom type juniBgpAddressFamilyDampeningMaxHoldDownTime based on Unsigned32"""
    defaultValue = 20


_JuniBgpAddressFamilyDampeningMaxHoldDownTime_Object = MibTableColumn
juniBgpAddressFamilyDampeningMaxHoldDownTime = _JuniBgpAddressFamilyDampeningMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 8),
    _JuniBgpAddressFamilyDampeningMaxHoldDownTime_Type()
)
juniBgpAddressFamilyDampeningMaxHoldDownTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningMaxHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningMaxHoldDownTime.setUnits("seconds")


class _JuniBgpAddressFamilyDampeningHalfLifeReachable_Type(Unsigned32):
    """Custom type juniBgpAddressFamilyDampeningHalfLifeReachable based on Unsigned32"""
    defaultValue = 5


_JuniBgpAddressFamilyDampeningHalfLifeReachable_Object = MibTableColumn
juniBgpAddressFamilyDampeningHalfLifeReachable = _JuniBgpAddressFamilyDampeningHalfLifeReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 9),
    _JuniBgpAddressFamilyDampeningHalfLifeReachable_Type()
)
juniBgpAddressFamilyDampeningHalfLifeReachable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningHalfLifeReachable.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningHalfLifeReachable.setUnits("seconds")


class _JuniBgpAddressFamilyDampeningHalfLifeUnreachable_Type(Unsigned32):
    """Custom type juniBgpAddressFamilyDampeningHalfLifeUnreachable based on Unsigned32"""
    defaultValue = 5


_JuniBgpAddressFamilyDampeningHalfLifeUnreachable_Object = MibTableColumn
juniBgpAddressFamilyDampeningHalfLifeUnreachable = _JuniBgpAddressFamilyDampeningHalfLifeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 10),
    _JuniBgpAddressFamilyDampeningHalfLifeUnreachable_Type()
)
juniBgpAddressFamilyDampeningHalfLifeUnreachable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningHalfLifeUnreachable.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningHalfLifeUnreachable.setUnits("seconds")


class _JuniBgpAddressFamilyDampeningRouteMapName_Type(DisplayString):
    """Custom type juniBgpAddressFamilyDampeningRouteMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpAddressFamilyDampeningRouteMapName_Type.__name__ = "DisplayString"
_JuniBgpAddressFamilyDampeningRouteMapName_Object = MibTableColumn
juniBgpAddressFamilyDampeningRouteMapName = _JuniBgpAddressFamilyDampeningRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 11),
    _JuniBgpAddressFamilyDampeningRouteMapName_Type()
)
juniBgpAddressFamilyDampeningRouteMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDampeningRouteMapName.setStatus("current")


class _JuniBgpAddressFamilyResetConnectionType_Type(JuniBgpResetConnectionType):
    """Custom type juniBgpAddressFamilyResetConnectionType based on JuniBgpResetConnectionType"""


_JuniBgpAddressFamilyResetConnectionType_Object = MibTableColumn
juniBgpAddressFamilyResetConnectionType = _JuniBgpAddressFamilyResetConnectionType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 12),
    _JuniBgpAddressFamilyResetConnectionType_Type()
)
juniBgpAddressFamilyResetConnectionType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyResetConnectionType.setStatus("current")
_JuniBgpAddressFamilyRowStatus_Type = RowStatus
_JuniBgpAddressFamilyRowStatus_Object = MibTableColumn
juniBgpAddressFamilyRowStatus = _JuniBgpAddressFamilyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 13),
    _JuniBgpAddressFamilyRowStatus_Type()
)
juniBgpAddressFamilyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyRowStatus.setStatus("current")


class _JuniBgpAddressFamilyOperationalState_Type(Integer32):
    """Custom type juniBgpAddressFamilyOperationalState based on Integer32"""
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


_JuniBgpAddressFamilyOperationalState_Type.__name__ = "Integer32"
_JuniBgpAddressFamilyOperationalState_Object = MibTableColumn
juniBgpAddressFamilyOperationalState = _JuniBgpAddressFamilyOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 14),
    _JuniBgpAddressFamilyOperationalState_Type()
)
juniBgpAddressFamilyOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyOperationalState.setStatus("current")


class _JuniBgpAddressFamilyUnconfiguredAttributes_Type(Bits):
    """Custom type juniBgpAddressFamilyUnconfiguredAttributes based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("juniBgpAddressFamilyCheckVpnNextHops", 12),
          ("juniBgpAddressFamilyDampeningHalfLifeReachable", 5),
          ("juniBgpAddressFamilyDampeningHalfLifeUnreachable", 6),
          ("juniBgpAddressFamilyDampeningMaxHoldDownTime", 4),
          ("juniBgpAddressFamilyDampeningReuseThreshold", 3),
          ("juniBgpAddressFamilyDampeningRouteMapName", 7),
          ("juniBgpAddressFamilyDampeningSuppressThreshold", 2),
          ("juniBgpAddressFamilyDefaultOriginate", 0),
          ("juniBgpAddressFamilyDefaultOriginateRouteMap", 11),
          ("juniBgpAddressFamilyExternalDistance", 8),
          ("juniBgpAddressFamilyInternalDistance", 9),
          ("juniBgpAddressFamilyLocalDistance", 10),
          ("juniBgpAddressFamilyRouteFlapDampening", 1))
    )

_JuniBgpAddressFamilyUnconfiguredAttributes_Type.__name__ = "Bits"
_JuniBgpAddressFamilyUnconfiguredAttributes_Object = MibTableColumn
juniBgpAddressFamilyUnconfiguredAttributes = _JuniBgpAddressFamilyUnconfiguredAttributes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 15),
    _JuniBgpAddressFamilyUnconfiguredAttributes_Type()
)
juniBgpAddressFamilyUnconfiguredAttributes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyUnconfiguredAttributes.setStatus("current")


class _JuniBgpAddressFamilyExternalDistance_Type(Integer32):
    """Custom type juniBgpAddressFamilyExternalDistance based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpAddressFamilyExternalDistance_Type.__name__ = "Integer32"
_JuniBgpAddressFamilyExternalDistance_Object = MibTableColumn
juniBgpAddressFamilyExternalDistance = _JuniBgpAddressFamilyExternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 16),
    _JuniBgpAddressFamilyExternalDistance_Type()
)
juniBgpAddressFamilyExternalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyExternalDistance.setStatus("current")


class _JuniBgpAddressFamilyInternalDistance_Type(Integer32):
    """Custom type juniBgpAddressFamilyInternalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpAddressFamilyInternalDistance_Type.__name__ = "Integer32"
_JuniBgpAddressFamilyInternalDistance_Object = MibTableColumn
juniBgpAddressFamilyInternalDistance = _JuniBgpAddressFamilyInternalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 17),
    _JuniBgpAddressFamilyInternalDistance_Type()
)
juniBgpAddressFamilyInternalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyInternalDistance.setStatus("current")


class _JuniBgpAddressFamilyLocalDistance_Type(Integer32):
    """Custom type juniBgpAddressFamilyLocalDistance based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniBgpAddressFamilyLocalDistance_Type.__name__ = "Integer32"
_JuniBgpAddressFamilyLocalDistance_Object = MibTableColumn
juniBgpAddressFamilyLocalDistance = _JuniBgpAddressFamilyLocalDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 18),
    _JuniBgpAddressFamilyLocalDistance_Type()
)
juniBgpAddressFamilyLocalDistance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyLocalDistance.setStatus("current")


class _JuniBgpAddressFamilyDefaultOriginateRouteMap_Type(DisplayString):
    """Custom type juniBgpAddressFamilyDefaultOriginateRouteMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniBgpAddressFamilyDefaultOriginateRouteMap_Type.__name__ = "DisplayString"
_JuniBgpAddressFamilyDefaultOriginateRouteMap_Object = MibTableColumn
juniBgpAddressFamilyDefaultOriginateRouteMap = _JuniBgpAddressFamilyDefaultOriginateRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 19),
    _JuniBgpAddressFamilyDefaultOriginateRouteMap_Type()
)
juniBgpAddressFamilyDefaultOriginateRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyDefaultOriginateRouteMap.setStatus("current")


class _JuniBgpAddressFamilyIpIntfProfileNameForMplsHeads_Type(DisplayString):
    """Custom type juniBgpAddressFamilyIpIntfProfileNameForMplsHeads based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniBgpAddressFamilyIpIntfProfileNameForMplsHeads_Type.__name__ = "DisplayString"
_JuniBgpAddressFamilyIpIntfProfileNameForMplsHeads_Object = MibTableColumn
juniBgpAddressFamilyIpIntfProfileNameForMplsHeads = _JuniBgpAddressFamilyIpIntfProfileNameForMplsHeads_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 20),
    _JuniBgpAddressFamilyIpIntfProfileNameForMplsHeads_Type()
)
juniBgpAddressFamilyIpIntfProfileNameForMplsHeads.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyIpIntfProfileNameForMplsHeads.setStatus("obsolete")


class _JuniBgpAddressFamilyIpIntfProfileNameForMplsTails_Type(DisplayString):
    """Custom type juniBgpAddressFamilyIpIntfProfileNameForMplsTails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniBgpAddressFamilyIpIntfProfileNameForMplsTails_Type.__name__ = "DisplayString"
_JuniBgpAddressFamilyIpIntfProfileNameForMplsTails_Object = MibTableColumn
juniBgpAddressFamilyIpIntfProfileNameForMplsTails = _JuniBgpAddressFamilyIpIntfProfileNameForMplsTails_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 21),
    _JuniBgpAddressFamilyIpIntfProfileNameForMplsTails_Type()
)
juniBgpAddressFamilyIpIntfProfileNameForMplsTails.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyIpIntfProfileNameForMplsTails.setStatus("obsolete")


class _JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads_Type(DisplayString):
    """Custom type juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads_Type.__name__ = "DisplayString"
_JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads_Object = MibTableColumn
juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads = _JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 22),
    _JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads_Type()
)
juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads.setStatus("obsolete")


class _JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails_Type(DisplayString):
    """Custom type juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails_Type.__name__ = "DisplayString"
_JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails_Object = MibTableColumn
juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails = _JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 23),
    _JuniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails_Type()
)
juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails.setStatus("obsolete")


class _JuniBgpAddressFamilyCheckVpnNextHops_Type(TruthValue):
    """Custom type juniBgpAddressFamilyCheckVpnNextHops based on TruthValue"""


_JuniBgpAddressFamilyCheckVpnNextHops_Object = MibTableColumn
juniBgpAddressFamilyCheckVpnNextHops = _JuniBgpAddressFamilyCheckVpnNextHops_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 24),
    _JuniBgpAddressFamilyCheckVpnNextHops_Type()
)
juniBgpAddressFamilyCheckVpnNextHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyCheckVpnNextHops.setStatus("current")
_JuniBgpAddressFamilyPathSelectionIsDeferred_Type = TruthValue
_JuniBgpAddressFamilyPathSelectionIsDeferred_Object = MibTableColumn
juniBgpAddressFamilyPathSelectionIsDeferred = _JuniBgpAddressFamilyPathSelectionIsDeferred_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 25),
    _JuniBgpAddressFamilyPathSelectionIsDeferred_Type()
)
juniBgpAddressFamilyPathSelectionIsDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyPathSelectionIsDeferred.setStatus("current")
_JuniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards_Type = TruthValue
_JuniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards_Object = MibTableColumn
juniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards = _JuniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 26),
    _JuniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards_Type()
)
juniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards.setStatus("current")


class _JuniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires_Type(Integer32):
    """Custom type juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires_Type.__name__ = "Integer32"
_JuniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires_Object = MibTableColumn
juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires = _JuniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 19, 1, 27),
    _JuniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires_Type()
)
juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires.setStatus("current")
_JuniBgpStorageGroup_ObjectIdentity = ObjectIdentity
juniBgpStorageGroup = _JuniBgpStorageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20)
)


class _JuniBgpStorageInitialHeapSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialHeapSize based on JuniBgpStorageInteger"""
    defaultValue = 16384


_JuniBgpStorageInitialHeapSize_Object = MibScalar
juniBgpStorageInitialHeapSize = _JuniBgpStorageInitialHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 1),
    _JuniBgpStorageInitialHeapSize_Type()
)
juniBgpStorageInitialHeapSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialHeapSize.setStatus("obsolete")


class _JuniBgpStorageMaxHeapSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxHeapSize based on JuniBgpStorageInteger"""
    defaultValue = 536870912


_JuniBgpStorageMaxHeapSize_Object = MibScalar
juniBgpStorageMaxHeapSize = _JuniBgpStorageMaxHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 2),
    _JuniBgpStorageMaxHeapSize_Type()
)
juniBgpStorageMaxHeapSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxHeapSize.setStatus("obsolete")


class _JuniBgpStorageInitialVrfPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialVrfPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialVrfPoolSize_Object = MibScalar
juniBgpStorageInitialVrfPoolSize = _JuniBgpStorageInitialVrfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 4),
    _JuniBgpStorageInitialVrfPoolSize_Type()
)
juniBgpStorageInitialVrfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialVrfPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxVrfPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxVrfPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxVrfPoolSize_Object = MibScalar
juniBgpStorageMaxVrfPoolSize = _JuniBgpStorageMaxVrfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 5),
    _JuniBgpStorageMaxVrfPoolSize_Type()
)
juniBgpStorageMaxVrfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxVrfPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialAddressFamilyPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialAddressFamilyPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialAddressFamilyPoolSize_Object = MibScalar
juniBgpStorageInitialAddressFamilyPoolSize = _JuniBgpStorageInitialAddressFamilyPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 6),
    _JuniBgpStorageInitialAddressFamilyPoolSize_Type()
)
juniBgpStorageInitialAddressFamilyPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialAddressFamilyPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxAddressFamilyPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxAddressFamilyPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxAddressFamilyPoolSize_Object = MibScalar
juniBgpStorageMaxAddressFamilyPoolSize = _JuniBgpStorageMaxAddressFamilyPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 7),
    _JuniBgpStorageMaxAddressFamilyPoolSize_Type()
)
juniBgpStorageMaxAddressFamilyPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxAddressFamilyPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialPeerPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialPeerPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialPeerPoolSize_Object = MibScalar
juniBgpStorageInitialPeerPoolSize = _JuniBgpStorageInitialPeerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 8),
    _JuniBgpStorageInitialPeerPoolSize_Type()
)
juniBgpStorageInitialPeerPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialPeerPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxPeerPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxPeerPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxPeerPoolSize_Object = MibScalar
juniBgpStorageMaxPeerPoolSize = _JuniBgpStorageMaxPeerPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 9),
    _JuniBgpStorageMaxPeerPoolSize_Type()
)
juniBgpStorageMaxPeerPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxPeerPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialPeerAfPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialPeerAfPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialPeerAfPoolSize_Object = MibScalar
juniBgpStorageInitialPeerAfPoolSize = _JuniBgpStorageInitialPeerAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 10),
    _JuniBgpStorageInitialPeerAfPoolSize_Type()
)
juniBgpStorageInitialPeerAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialPeerAfPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxPeerAfPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxPeerAfPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxPeerAfPoolSize_Object = MibScalar
juniBgpStorageMaxPeerAfPoolSize = _JuniBgpStorageMaxPeerAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 11),
    _JuniBgpStorageMaxPeerAfPoolSize_Type()
)
juniBgpStorageMaxPeerAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxPeerAfPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialPeerGroupPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialPeerGroupPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialPeerGroupPoolSize_Object = MibScalar
juniBgpStorageInitialPeerGroupPoolSize = _JuniBgpStorageInitialPeerGroupPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 12),
    _JuniBgpStorageInitialPeerGroupPoolSize_Type()
)
juniBgpStorageInitialPeerGroupPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialPeerGroupPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxPeerGroupPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxPeerGroupPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxPeerGroupPoolSize_Object = MibScalar
juniBgpStorageMaxPeerGroupPoolSize = _JuniBgpStorageMaxPeerGroupPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 13),
    _JuniBgpStorageMaxPeerGroupPoolSize_Type()
)
juniBgpStorageMaxPeerGroupPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxPeerGroupPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialPeerGroupAfPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialPeerGroupAfPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialPeerGroupAfPoolSize_Object = MibScalar
juniBgpStorageInitialPeerGroupAfPoolSize = _JuniBgpStorageInitialPeerGroupAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 14),
    _JuniBgpStorageInitialPeerGroupAfPoolSize_Type()
)
juniBgpStorageInitialPeerGroupAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialPeerGroupAfPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxPeerGroupAfPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxPeerGroupAfPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxPeerGroupAfPoolSize_Object = MibScalar
juniBgpStorageMaxPeerGroupAfPoolSize = _JuniBgpStorageMaxPeerGroupAfPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 15),
    _JuniBgpStorageMaxPeerGroupAfPoolSize_Type()
)
juniBgpStorageMaxPeerGroupAfPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxPeerGroupAfPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialNetworkPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialNetworkPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialNetworkPoolSize_Object = MibScalar
juniBgpStorageInitialNetworkPoolSize = _JuniBgpStorageInitialNetworkPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 16),
    _JuniBgpStorageInitialNetworkPoolSize_Type()
)
juniBgpStorageInitialNetworkPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialNetworkPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxNetworkPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxNetworkPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxNetworkPoolSize_Object = MibScalar
juniBgpStorageMaxNetworkPoolSize = _JuniBgpStorageMaxNetworkPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 17),
    _JuniBgpStorageMaxNetworkPoolSize_Type()
)
juniBgpStorageMaxNetworkPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxNetworkPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialAggregatePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialAggregatePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialAggregatePoolSize_Object = MibScalar
juniBgpStorageInitialAggregatePoolSize = _JuniBgpStorageInitialAggregatePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 18),
    _JuniBgpStorageInitialAggregatePoolSize_Type()
)
juniBgpStorageInitialAggregatePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialAggregatePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxAggregatePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxAggregatePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxAggregatePoolSize_Object = MibScalar
juniBgpStorageMaxAggregatePoolSize = _JuniBgpStorageMaxAggregatePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 19),
    _JuniBgpStorageMaxAggregatePoolSize_Type()
)
juniBgpStorageMaxAggregatePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxAggregatePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialDestinationPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialDestinationPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialDestinationPoolSize_Object = MibScalar
juniBgpStorageInitialDestinationPoolSize = _JuniBgpStorageInitialDestinationPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 20),
    _JuniBgpStorageInitialDestinationPoolSize_Type()
)
juniBgpStorageInitialDestinationPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialDestinationPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxDestinationPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxDestinationPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxDestinationPoolSize_Object = MibScalar
juniBgpStorageMaxDestinationPoolSize = _JuniBgpStorageMaxDestinationPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 21),
    _JuniBgpStorageMaxDestinationPoolSize_Type()
)
juniBgpStorageMaxDestinationPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxDestinationPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialRoutePoolSize_Object = MibScalar
juniBgpStorageInitialRoutePoolSize = _JuniBgpStorageInitialRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 22),
    _JuniBgpStorageInitialRoutePoolSize_Type()
)
juniBgpStorageInitialRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxRoutePoolSize_Object = MibScalar
juniBgpStorageMaxRoutePoolSize = _JuniBgpStorageMaxRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 23),
    _JuniBgpStorageMaxRoutePoolSize_Type()
)
juniBgpStorageMaxRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialAttributesPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialAttributesPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialAttributesPoolSize_Object = MibScalar
juniBgpStorageInitialAttributesPoolSize = _JuniBgpStorageInitialAttributesPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 24),
    _JuniBgpStorageInitialAttributesPoolSize_Type()
)
juniBgpStorageInitialAttributesPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialAttributesPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxAttributesPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxAttributesPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxAttributesPoolSize_Object = MibScalar
juniBgpStorageMaxAttributesPoolSize = _JuniBgpStorageMaxAttributesPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 25),
    _JuniBgpStorageMaxAttributesPoolSize_Type()
)
juniBgpStorageMaxAttributesPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxAttributesPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialRouteFlapHistoryPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialRouteFlapHistoryPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialRouteFlapHistoryPoolSize_Object = MibScalar
juniBgpStorageInitialRouteFlapHistoryPoolSize = _JuniBgpStorageInitialRouteFlapHistoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 26),
    _JuniBgpStorageInitialRouteFlapHistoryPoolSize_Type()
)
juniBgpStorageInitialRouteFlapHistoryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialRouteFlapHistoryPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxRouteFlapHistoryPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxRouteFlapHistoryPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxRouteFlapHistoryPoolSize_Object = MibScalar
juniBgpStorageMaxRouteFlapHistoryPoolSize = _JuniBgpStorageMaxRouteFlapHistoryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 27),
    _JuniBgpStorageMaxRouteFlapHistoryPoolSize_Type()
)
juniBgpStorageMaxRouteFlapHistoryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxRouteFlapHistoryPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialNetworkRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialNetworkRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialNetworkRoutePoolSize_Object = MibScalar
juniBgpStorageInitialNetworkRoutePoolSize = _JuniBgpStorageInitialNetworkRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 28),
    _JuniBgpStorageInitialNetworkRoutePoolSize_Type()
)
juniBgpStorageInitialNetworkRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialNetworkRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxNetworkRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxNetworkRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxNetworkRoutePoolSize_Object = MibScalar
juniBgpStorageMaxNetworkRoutePoolSize = _JuniBgpStorageMaxNetworkRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 29),
    _JuniBgpStorageMaxNetworkRoutePoolSize_Type()
)
juniBgpStorageMaxNetworkRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxNetworkRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialRedistributedRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialRedistributedRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialRedistributedRoutePoolSize_Object = MibScalar
juniBgpStorageInitialRedistributedRoutePoolSize = _JuniBgpStorageInitialRedistributedRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 30),
    _JuniBgpStorageInitialRedistributedRoutePoolSize_Type()
)
juniBgpStorageInitialRedistributedRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialRedistributedRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxRedistributedRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxRedistributedRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxRedistributedRoutePoolSize_Object = MibScalar
juniBgpStorageMaxRedistributedRoutePoolSize = _JuniBgpStorageMaxRedistributedRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 31),
    _JuniBgpStorageMaxRedistributedRoutePoolSize_Type()
)
juniBgpStorageMaxRedistributedRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxRedistributedRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialAggregateRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialAggregateRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialAggregateRoutePoolSize_Object = MibScalar
juniBgpStorageInitialAggregateRoutePoolSize = _JuniBgpStorageInitialAggregateRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 32),
    _JuniBgpStorageInitialAggregateRoutePoolSize_Type()
)
juniBgpStorageInitialAggregateRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialAggregateRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxAggregateRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxAggregateRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxAggregateRoutePoolSize_Object = MibScalar
juniBgpStorageMaxAggregateRoutePoolSize = _JuniBgpStorageMaxAggregateRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 33),
    _JuniBgpStorageMaxAggregateRoutePoolSize_Type()
)
juniBgpStorageMaxAggregateRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxAggregateRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialAutoSummaryRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialAutoSummaryRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialAutoSummaryRoutePoolSize_Object = MibScalar
juniBgpStorageInitialAutoSummaryRoutePoolSize = _JuniBgpStorageInitialAutoSummaryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 34),
    _JuniBgpStorageInitialAutoSummaryRoutePoolSize_Type()
)
juniBgpStorageInitialAutoSummaryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialAutoSummaryRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxAutoSummaryRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxAutoSummaryRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxAutoSummaryRoutePoolSize_Object = MibScalar
juniBgpStorageMaxAutoSummaryRoutePoolSize = _JuniBgpStorageMaxAutoSummaryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 35),
    _JuniBgpStorageMaxAutoSummaryRoutePoolSize_Type()
)
juniBgpStorageMaxAutoSummaryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxAutoSummaryRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialHistoryRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialHistoryRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialHistoryRoutePoolSize_Object = MibScalar
juniBgpStorageInitialHistoryRoutePoolSize = _JuniBgpStorageInitialHistoryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 36),
    _JuniBgpStorageInitialHistoryRoutePoolSize_Type()
)
juniBgpStorageInitialHistoryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialHistoryRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxHistoryRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxHistoryRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxHistoryRoutePoolSize_Object = MibScalar
juniBgpStorageMaxHistoryRoutePoolSize = _JuniBgpStorageMaxHistoryRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 37),
    _JuniBgpStorageMaxHistoryRoutePoolSize_Type()
)
juniBgpStorageMaxHistoryRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxHistoryRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialSendQueueEntryPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialSendQueueEntryPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialSendQueueEntryPoolSize_Object = MibScalar
juniBgpStorageInitialSendQueueEntryPoolSize = _JuniBgpStorageInitialSendQueueEntryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 38),
    _JuniBgpStorageInitialSendQueueEntryPoolSize_Type()
)
juniBgpStorageInitialSendQueueEntryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialSendQueueEntryPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxSendQueueEntryPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxSendQueueEntryPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxSendQueueEntryPoolSize_Object = MibScalar
juniBgpStorageMaxSendQueueEntryPoolSize = _JuniBgpStorageMaxSendQueueEntryPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 39),
    _JuniBgpStorageMaxSendQueueEntryPoolSize_Type()
)
juniBgpStorageMaxSendQueueEntryPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxSendQueueEntryPoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialVpnRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialVpnRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialVpnRoutePoolSize_Object = MibScalar
juniBgpStorageInitialVpnRoutePoolSize = _JuniBgpStorageInitialVpnRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 40),
    _JuniBgpStorageInitialVpnRoutePoolSize_Type()
)
juniBgpStorageInitialVpnRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialVpnRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxVpnRoutePoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxVpnRoutePoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxVpnRoutePoolSize_Object = MibScalar
juniBgpStorageMaxVpnRoutePoolSize = _JuniBgpStorageMaxVpnRoutePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 41),
    _JuniBgpStorageMaxVpnRoutePoolSize_Type()
)
juniBgpStorageMaxVpnRoutePoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxVpnRoutePoolSize.setStatus("obsolete")


class _JuniBgpStorageInitialRouteTargetPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageInitialRouteTargetPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 1


_JuniBgpStorageInitialRouteTargetPoolSize_Object = MibScalar
juniBgpStorageInitialRouteTargetPoolSize = _JuniBgpStorageInitialRouteTargetPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 42),
    _JuniBgpStorageInitialRouteTargetPoolSize_Type()
)
juniBgpStorageInitialRouteTargetPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageInitialRouteTargetPoolSize.setStatus("obsolete")


class _JuniBgpStorageMaxRouteTargetPoolSize_Type(JuniBgpStorageInteger):
    """Custom type juniBgpStorageMaxRouteTargetPoolSize based on JuniBgpStorageInteger"""
    defaultValue = 500000000


_JuniBgpStorageMaxRouteTargetPoolSize_Object = MibScalar
juniBgpStorageMaxRouteTargetPoolSize = _JuniBgpStorageMaxRouteTargetPoolSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 20, 43),
    _JuniBgpStorageMaxRouteTargetPoolSize_Type()
)
juniBgpStorageMaxRouteTargetPoolSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniBgpStorageMaxRouteTargetPoolSize.setStatus("obsolete")
_JuniBgpRouteExtendedCommunityTable_Object = MibTable
juniBgpRouteExtendedCommunityTable = _JuniBgpRouteExtendedCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 22)
)
if mibBuilder.loadTexts:
    juniBgpRouteExtendedCommunityTable.setStatus("obsolete")
_JuniBgpRouteExtendedCommunityEntry_Object = MibTableRow
juniBgpRouteExtendedCommunityEntry = _JuniBgpRouteExtendedCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 22, 1)
)
juniBgpRouteExtendedCommunityEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpRouteExtendedCommunityNumber"),
)
if mibBuilder.loadTexts:
    juniBgpRouteExtendedCommunityEntry.setStatus("obsolete")


class _JuniBgpRouteExtendedCommunityNumber_Type(OctetString):
    """Custom type juniBgpRouteExtendedCommunityNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniBgpRouteExtendedCommunityNumber_Type.__name__ = "OctetString"
_JuniBgpRouteExtendedCommunityNumber_Object = MibTableColumn
juniBgpRouteExtendedCommunityNumber = _JuniBgpRouteExtendedCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 22, 1, 1),
    _JuniBgpRouteExtendedCommunityNumber_Type()
)
juniBgpRouteExtendedCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpRouteExtendedCommunityNumber.setStatus("obsolete")
_JuniBgpNewRouteTable_Object = MibTable
juniBgpNewRouteTable = _JuniBgpNewRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23)
)
if mibBuilder.loadTexts:
    juniBgpNewRouteTable.setStatus("current")
_JuniBgpNewRouteEntry_Object = MibTableRow
juniBgpNewRouteEntry = _JuniBgpNewRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1)
)
juniBgpNewRouteEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteOriginalRd"),
)
if mibBuilder.loadTexts:
    juniBgpNewRouteEntry.setStatus("current")
_JuniBgpNewRouteVrfName_Type = JuniVrfName
_JuniBgpNewRouteVrfName_Object = MibTableColumn
juniBgpNewRouteVrfName = _JuniBgpNewRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 1),
    _JuniBgpNewRouteVrfName_Type()
)
juniBgpNewRouteVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteVrfName.setStatus("current")
_JuniBgpNewRouteAfi_Type = JuniBgpAfi
_JuniBgpNewRouteAfi_Object = MibTableColumn
juniBgpNewRouteAfi = _JuniBgpNewRouteAfi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 2),
    _JuniBgpNewRouteAfi_Type()
)
juniBgpNewRouteAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteAfi.setStatus("current")
_JuniBgpNewRouteSafi_Type = JuniBgpSafi
_JuniBgpNewRouteSafi_Object = MibTableColumn
juniBgpNewRouteSafi = _JuniBgpNewRouteSafi_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 3),
    _JuniBgpNewRouteSafi_Type()
)
juniBgpNewRouteSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteSafi.setStatus("current")
_JuniBgpNewRouteIpAddrPrefix_Type = IpAddress
_JuniBgpNewRouteIpAddrPrefix_Object = MibTableColumn
juniBgpNewRouteIpAddrPrefix = _JuniBgpNewRouteIpAddrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 4),
    _JuniBgpNewRouteIpAddrPrefix_Type()
)
juniBgpNewRouteIpAddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteIpAddrPrefix.setStatus("current")


class _JuniBgpNewRouteIpAddrPrefixLen_Type(Integer32):
    """Custom type juniBgpNewRouteIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_JuniBgpNewRouteIpAddrPrefixLen_Type.__name__ = "Integer32"
_JuniBgpNewRouteIpAddrPrefixLen_Object = MibTableColumn
juniBgpNewRouteIpAddrPrefixLen = _JuniBgpNewRouteIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 5),
    _JuniBgpNewRouteIpAddrPrefixLen_Type()
)
juniBgpNewRouteIpAddrPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteIpAddrPrefixLen.setStatus("current")


class _JuniBgpNewRouteDistinguisher_Type(OctetString):
    """Custom type juniBgpNewRouteDistinguisher based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniBgpNewRouteDistinguisher_Type.__name__ = "OctetString"
_JuniBgpNewRouteDistinguisher_Object = MibTableColumn
juniBgpNewRouteDistinguisher = _JuniBgpNewRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 6),
    _JuniBgpNewRouteDistinguisher_Type()
)
juniBgpNewRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteDistinguisher.setStatus("current")
_JuniBgpNewRoutePeer_Type = IpAddress
_JuniBgpNewRoutePeer_Object = MibTableColumn
juniBgpNewRoutePeer = _JuniBgpNewRoutePeer_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 7),
    _JuniBgpNewRoutePeer_Type()
)
juniBgpNewRoutePeer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRoutePeer.setStatus("current")


class _JuniBgpNewRouteRouteType_Type(Integer32):
    """Custom type juniBgpNewRouteRouteType based on Integer32"""
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


_JuniBgpNewRouteRouteType_Type.__name__ = "Integer32"
_JuniBgpNewRouteRouteType_Object = MibTableColumn
juniBgpNewRouteRouteType = _JuniBgpNewRouteRouteType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 8),
    _JuniBgpNewRouteRouteType_Type()
)
juniBgpNewRouteRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteRouteType.setStatus("current")


class _JuniBgpNewRouteOriginalRd_Type(OctetString):
    """Custom type juniBgpNewRouteOriginalRd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniBgpNewRouteOriginalRd_Type.__name__ = "OctetString"
_JuniBgpNewRouteOriginalRd_Object = MibTableColumn
juniBgpNewRouteOriginalRd = _JuniBgpNewRouteOriginalRd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 9),
    _JuniBgpNewRouteOriginalRd_Type()
)
juniBgpNewRouteOriginalRd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpNewRouteOriginalRd.setStatus("current")
_JuniBgpNewRouteOriginatorId_Type = IpAddress
_JuniBgpNewRouteOriginatorId_Object = MibTableColumn
juniBgpNewRouteOriginatorId = _JuniBgpNewRouteOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 10),
    _JuniBgpNewRouteOriginatorId_Type()
)
juniBgpNewRouteOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteOriginatorId.setStatus("current")
_JuniBgpNewRouteAtomicAggregatePresent_Type = TruthValue
_JuniBgpNewRouteAtomicAggregatePresent_Object = MibTableColumn
juniBgpNewRouteAtomicAggregatePresent = _JuniBgpNewRouteAtomicAggregatePresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 11),
    _JuniBgpNewRouteAtomicAggregatePresent_Type()
)
juniBgpNewRouteAtomicAggregatePresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteAtomicAggregatePresent.setStatus("current")
_JuniBgpNewRouteMedPresent_Type = TruthValue
_JuniBgpNewRouteMedPresent_Object = MibTableColumn
juniBgpNewRouteMedPresent = _JuniBgpNewRouteMedPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 12),
    _JuniBgpNewRouteMedPresent_Type()
)
juniBgpNewRouteMedPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteMedPresent.setStatus("current")
_JuniBgpNewRouteLocalPrefPresent_Type = TruthValue
_JuniBgpNewRouteLocalPrefPresent_Object = MibTableColumn
juniBgpNewRouteLocalPrefPresent = _JuniBgpNewRouteLocalPrefPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 13),
    _JuniBgpNewRouteLocalPrefPresent_Type()
)
juniBgpNewRouteLocalPrefPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteLocalPrefPresent.setStatus("current")
_JuniBgpNewRouteAggregatorPresent_Type = TruthValue
_JuniBgpNewRouteAggregatorPresent_Object = MibTableColumn
juniBgpNewRouteAggregatorPresent = _JuniBgpNewRouteAggregatorPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 14),
    _JuniBgpNewRouteAggregatorPresent_Type()
)
juniBgpNewRouteAggregatorPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteAggregatorPresent.setStatus("current")
_JuniBgpNewRouteCommunitiesPresent_Type = TruthValue
_JuniBgpNewRouteCommunitiesPresent_Object = MibTableColumn
juniBgpNewRouteCommunitiesPresent = _JuniBgpNewRouteCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 15),
    _JuniBgpNewRouteCommunitiesPresent_Type()
)
juniBgpNewRouteCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteCommunitiesPresent.setStatus("current")
_JuniBgpNewRouteOriginatorIdPresent_Type = TruthValue
_JuniBgpNewRouteOriginatorIdPresent_Object = MibTableColumn
juniBgpNewRouteOriginatorIdPresent = _JuniBgpNewRouteOriginatorIdPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 16),
    _JuniBgpNewRouteOriginatorIdPresent_Type()
)
juniBgpNewRouteOriginatorIdPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteOriginatorIdPresent.setStatus("current")
_JuniBgpNewRouteClusterListPresent_Type = TruthValue
_JuniBgpNewRouteClusterListPresent_Object = MibTableColumn
juniBgpNewRouteClusterListPresent = _JuniBgpNewRouteClusterListPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 17),
    _JuniBgpNewRouteClusterListPresent_Type()
)
juniBgpNewRouteClusterListPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteClusterListPresent.setStatus("current")
_JuniBgpNewRouteWeight_Type = Unsigned32
_JuniBgpNewRouteWeight_Object = MibTableColumn
juniBgpNewRouteWeight = _JuniBgpNewRouteWeight_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 18),
    _JuniBgpNewRouteWeight_Type()
)
juniBgpNewRouteWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteWeight.setStatus("current")


class _JuniBgpNewRouteOrigin_Type(Integer32):
    """Custom type juniBgpNewRouteOrigin based on Integer32"""
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


_JuniBgpNewRouteOrigin_Type.__name__ = "Integer32"
_JuniBgpNewRouteOrigin_Object = MibTableColumn
juniBgpNewRouteOrigin = _JuniBgpNewRouteOrigin_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 19),
    _JuniBgpNewRouteOrigin_Type()
)
juniBgpNewRouteOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteOrigin.setStatus("current")


class _JuniBgpNewRouteASPathSegment_Type(OctetString):
    """Custom type juniBgpNewRouteASPathSegment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_JuniBgpNewRouteASPathSegment_Type.__name__ = "OctetString"
_JuniBgpNewRouteASPathSegment_Object = MibTableColumn
juniBgpNewRouteASPathSegment = _JuniBgpNewRouteASPathSegment_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 20),
    _JuniBgpNewRouteASPathSegment_Type()
)
juniBgpNewRouteASPathSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteASPathSegment.setStatus("current")
_JuniBgpNewRouteNextHop_Type = IpAddress
_JuniBgpNewRouteNextHop_Object = MibTableColumn
juniBgpNewRouteNextHop = _JuniBgpNewRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 21),
    _JuniBgpNewRouteNextHop_Type()
)
juniBgpNewRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteNextHop.setStatus("current")
_JuniBgpNewRouteMultiExitDisc_Type = Unsigned32
_JuniBgpNewRouteMultiExitDisc_Object = MibTableColumn
juniBgpNewRouteMultiExitDisc = _JuniBgpNewRouteMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 22),
    _JuniBgpNewRouteMultiExitDisc_Type()
)
juniBgpNewRouteMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteMultiExitDisc.setStatus("current")
_JuniBgpNewRouteLocalPref_Type = Unsigned32
_JuniBgpNewRouteLocalPref_Object = MibTableColumn
juniBgpNewRouteLocalPref = _JuniBgpNewRouteLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 23),
    _JuniBgpNewRouteLocalPref_Type()
)
juniBgpNewRouteLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteLocalPref.setStatus("current")


class _JuniBgpNewRouteAtomicAggregate_Type(Integer32):
    """Custom type juniBgpNewRouteAtomicAggregate based on Integer32"""
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


_JuniBgpNewRouteAtomicAggregate_Type.__name__ = "Integer32"
_JuniBgpNewRouteAtomicAggregate_Object = MibTableColumn
juniBgpNewRouteAtomicAggregate = _JuniBgpNewRouteAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 24),
    _JuniBgpNewRouteAtomicAggregate_Type()
)
juniBgpNewRouteAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteAtomicAggregate.setStatus("current")


class _JuniBgpNewRouteAggregatorAS_Type(Integer32):
    """Custom type juniBgpNewRouteAggregatorAS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniBgpNewRouteAggregatorAS_Type.__name__ = "Integer32"
_JuniBgpNewRouteAggregatorAS_Object = MibTableColumn
juniBgpNewRouteAggregatorAS = _JuniBgpNewRouteAggregatorAS_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 25),
    _JuniBgpNewRouteAggregatorAS_Type()
)
juniBgpNewRouteAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteAggregatorAS.setStatus("current")
_JuniBgpNewRouteAggregatorAddress_Type = IpAddress
_JuniBgpNewRouteAggregatorAddress_Object = MibTableColumn
juniBgpNewRouteAggregatorAddress = _JuniBgpNewRouteAggregatorAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 26),
    _JuniBgpNewRouteAggregatorAddress_Type()
)
juniBgpNewRouteAggregatorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteAggregatorAddress.setStatus("current")
_JuniBgpNewRouteBestInIpRouteTable_Type = TruthValue
_JuniBgpNewRouteBestInIpRouteTable_Object = MibTableColumn
juniBgpNewRouteBestInIpRouteTable = _JuniBgpNewRouteBestInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 27),
    _JuniBgpNewRouteBestInIpRouteTable_Type()
)
juniBgpNewRouteBestInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteBestInIpRouteTable.setStatus("current")


class _JuniBgpNewRouteUnknown_Type(OctetString):
    """Custom type juniBgpNewRouteUnknown based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_JuniBgpNewRouteUnknown_Type.__name__ = "OctetString"
_JuniBgpNewRouteUnknown_Object = MibTableColumn
juniBgpNewRouteUnknown = _JuniBgpNewRouteUnknown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 28),
    _JuniBgpNewRouteUnknown_Type()
)
juniBgpNewRouteUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteUnknown.setStatus("current")
_JuniBgpNewRouteExtendedCommunitiesPresent_Type = TruthValue
_JuniBgpNewRouteExtendedCommunitiesPresent_Object = MibTableColumn
juniBgpNewRouteExtendedCommunitiesPresent = _JuniBgpNewRouteExtendedCommunitiesPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 29),
    _JuniBgpNewRouteExtendedCommunitiesPresent_Type()
)
juniBgpNewRouteExtendedCommunitiesPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteExtendedCommunitiesPresent.setStatus("current")
_JuniBgpNewRouteValid_Type = TruthValue
_JuniBgpNewRouteValid_Object = MibTableColumn
juniBgpNewRouteValid = _JuniBgpNewRouteValid_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 30),
    _JuniBgpNewRouteValid_Type()
)
juniBgpNewRouteValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteValid.setStatus("current")


class _JuniBgpNewRouteSuppressedBy_Type(Integer32):
    """Custom type juniBgpNewRouteSuppressedBy based on Integer32"""
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


_JuniBgpNewRouteSuppressedBy_Type.__name__ = "Integer32"
_JuniBgpNewRouteSuppressedBy_Object = MibTableColumn
juniBgpNewRouteSuppressedBy = _JuniBgpNewRouteSuppressedBy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 31),
    _JuniBgpNewRouteSuppressedBy_Type()
)
juniBgpNewRouteSuppressedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteSuppressedBy.setStatus("current")
_JuniBgpNewRouteNextHopReachable_Type = TruthValue
_JuniBgpNewRouteNextHopReachable_Object = MibTableColumn
juniBgpNewRouteNextHopReachable = _JuniBgpNewRouteNextHopReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 32),
    _JuniBgpNewRouteNextHopReachable_Type()
)
juniBgpNewRouteNextHopReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteNextHopReachable.setStatus("current")
_JuniBgpNewRouteSynchronizedWithIgp_Type = TruthValue
_JuniBgpNewRouteSynchronizedWithIgp_Object = MibTableColumn
juniBgpNewRouteSynchronizedWithIgp = _JuniBgpNewRouteSynchronizedWithIgp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 33),
    _JuniBgpNewRouteSynchronizedWithIgp_Type()
)
juniBgpNewRouteSynchronizedWithIgp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteSynchronizedWithIgp.setStatus("current")
_JuniBgpNewRoutePlaceInIpRouteTable_Type = TruthValue
_JuniBgpNewRoutePlaceInIpRouteTable_Object = MibTableColumn
juniBgpNewRoutePlaceInIpRouteTable = _JuniBgpNewRoutePlaceInIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 34),
    _JuniBgpNewRoutePlaceInIpRouteTable_Type()
)
juniBgpNewRoutePlaceInIpRouteTable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRoutePlaceInIpRouteTable.setStatus("current")
_JuniBgpNewRouteAdvertiseToExternalPeers_Type = TruthValue
_JuniBgpNewRouteAdvertiseToExternalPeers_Object = MibTableColumn
juniBgpNewRouteAdvertiseToExternalPeers = _JuniBgpNewRouteAdvertiseToExternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 35),
    _JuniBgpNewRouteAdvertiseToExternalPeers_Type()
)
juniBgpNewRouteAdvertiseToExternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteAdvertiseToExternalPeers.setStatus("current")
_JuniBgpNewRouteAdvertiseToInternalPeers_Type = TruthValue
_JuniBgpNewRouteAdvertiseToInternalPeers_Object = MibTableColumn
juniBgpNewRouteAdvertiseToInternalPeers = _JuniBgpNewRouteAdvertiseToInternalPeers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 36),
    _JuniBgpNewRouteAdvertiseToInternalPeers_Type()
)
juniBgpNewRouteAdvertiseToInternalPeers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteAdvertiseToInternalPeers.setStatus("current")
_JuniBgpNewRouteMplsLabel_Type = Unsigned32
_JuniBgpNewRouteMplsLabel_Object = MibTableColumn
juniBgpNewRouteMplsLabel = _JuniBgpNewRouteMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 37),
    _JuniBgpNewRouteMplsLabel_Type()
)
juniBgpNewRouteMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteMplsLabel.setStatus("obsolete")
_JuniBgpNewRouteNextHopMetric_Type = Unsigned32
_JuniBgpNewRouteNextHopMetric_Object = MibTableColumn
juniBgpNewRouteNextHopMetric = _JuniBgpNewRouteNextHopMetric_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 38),
    _JuniBgpNewRouteNextHopMetric_Type()
)
juniBgpNewRouteNextHopMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteNextHopMetric.setStatus("current")
_JuniBgpNewRouteMplsInLabel_Type = Unsigned32
_JuniBgpNewRouteMplsInLabel_Object = MibTableColumn
juniBgpNewRouteMplsInLabel = _JuniBgpNewRouteMplsInLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 39),
    _JuniBgpNewRouteMplsInLabel_Type()
)
juniBgpNewRouteMplsInLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteMplsInLabel.setStatus("current")
_JuniBgpNewRouteMplsOutLabel_Type = Unsigned32
_JuniBgpNewRouteMplsOutLabel_Object = MibTableColumn
juniBgpNewRouteMplsOutLabel = _JuniBgpNewRouteMplsOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 40),
    _JuniBgpNewRouteMplsOutLabel_Type()
)
juniBgpNewRouteMplsOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteMplsOutLabel.setStatus("current")
_JuniBgpNewRouteLeaked_Type = TruthValue
_JuniBgpNewRouteLeaked_Object = MibTableColumn
juniBgpNewRouteLeaked = _JuniBgpNewRouteLeaked_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 41),
    _JuniBgpNewRouteLeaked_Type()
)
juniBgpNewRouteLeaked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteLeaked.setStatus("current")
_JuniBgpNewRouteStale_Type = TruthValue
_JuniBgpNewRouteStale_Object = MibTableColumn
juniBgpNewRouteStale = _JuniBgpNewRouteStale_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 23, 1, 42),
    _JuniBgpNewRouteStale_Type()
)
juniBgpNewRouteStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteStale.setStatus("current")
_JuniBgpNewRouteFlapHistoryTable_Object = MibTable
juniBgpNewRouteFlapHistoryTable = _JuniBgpNewRouteFlapHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24)
)
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapHistoryTable.setStatus("current")
_JuniBgpNewRouteFlapHistoryEntry_Object = MibTableRow
juniBgpNewRouteFlapHistoryEntry = _JuniBgpNewRouteFlapHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1)
)
juniBgpNewRouteFlapHistoryEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteOriginalRd"),
)
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapHistoryEntry.setStatus("current")


class _JuniBgpNewRouteFlapState_Type(Integer32):
    """Custom type juniBgpNewRouteFlapState based on Integer32"""
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


_JuniBgpNewRouteFlapState_Type.__name__ = "Integer32"
_JuniBgpNewRouteFlapState_Object = MibTableColumn
juniBgpNewRouteFlapState = _JuniBgpNewRouteFlapState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 1),
    _JuniBgpNewRouteFlapState_Type()
)
juniBgpNewRouteFlapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapState.setStatus("current")
_JuniBgpNewRouteFlapFigureOfMerit_Type = Unsigned32
_JuniBgpNewRouteFlapFigureOfMerit_Object = MibTableColumn
juniBgpNewRouteFlapFigureOfMerit = _JuniBgpNewRouteFlapFigureOfMerit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 2),
    _JuniBgpNewRouteFlapFigureOfMerit_Type()
)
juniBgpNewRouteFlapFigureOfMerit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapFigureOfMerit.setStatus("current")
_JuniBgpNewRouteFlapRemainingTime_Type = Unsigned32
_JuniBgpNewRouteFlapRemainingTime_Object = MibTableColumn
juniBgpNewRouteFlapRemainingTime = _JuniBgpNewRouteFlapRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 3),
    _JuniBgpNewRouteFlapRemainingTime_Type()
)
juniBgpNewRouteFlapRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapRemainingTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapRemainingTime.setUnits("seconds")
_JuniBgpNewRouteFlapSuppressThreshold_Type = Unsigned32
_JuniBgpNewRouteFlapSuppressThreshold_Object = MibTableColumn
juniBgpNewRouteFlapSuppressThreshold = _JuniBgpNewRouteFlapSuppressThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 4),
    _JuniBgpNewRouteFlapSuppressThreshold_Type()
)
juniBgpNewRouteFlapSuppressThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapSuppressThreshold.setStatus("current")
_JuniBgpNewRouteFlapReuseThreshold_Type = Unsigned32
_JuniBgpNewRouteFlapReuseThreshold_Object = MibTableColumn
juniBgpNewRouteFlapReuseThreshold = _JuniBgpNewRouteFlapReuseThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 5),
    _JuniBgpNewRouteFlapReuseThreshold_Type()
)
juniBgpNewRouteFlapReuseThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapReuseThreshold.setStatus("current")
_JuniBgpNewRouteFlapMaxHoldDownTime_Type = Unsigned32
_JuniBgpNewRouteFlapMaxHoldDownTime_Object = MibTableColumn
juniBgpNewRouteFlapMaxHoldDownTime = _JuniBgpNewRouteFlapMaxHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 6),
    _JuniBgpNewRouteFlapMaxHoldDownTime_Type()
)
juniBgpNewRouteFlapMaxHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapMaxHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapMaxHoldDownTime.setUnits("seconds")
_JuniBgpNewRouteFlapHalfLifeReachable_Type = Unsigned32
_JuniBgpNewRouteFlapHalfLifeReachable_Object = MibTableColumn
juniBgpNewRouteFlapHalfLifeReachable = _JuniBgpNewRouteFlapHalfLifeReachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 7),
    _JuniBgpNewRouteFlapHalfLifeReachable_Type()
)
juniBgpNewRouteFlapHalfLifeReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapHalfLifeReachable.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapHalfLifeReachable.setUnits("seconds")
_JuniBgpNewRouteFlapHalfLifeUnreachable_Type = Unsigned32
_JuniBgpNewRouteFlapHalfLifeUnreachable_Object = MibTableColumn
juniBgpNewRouteFlapHalfLifeUnreachable = _JuniBgpNewRouteFlapHalfLifeUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 24, 1, 8),
    _JuniBgpNewRouteFlapHalfLifeUnreachable_Type()
)
juniBgpNewRouteFlapHalfLifeUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapHalfLifeUnreachable.setStatus("current")
if mibBuilder.loadTexts:
    juniBgpNewRouteFlapHalfLifeUnreachable.setUnits("seconds")
_JuniBgpNewRouteCommunityTable_Object = MibTable
juniBgpNewRouteCommunityTable = _JuniBgpNewRouteCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 25)
)
if mibBuilder.loadTexts:
    juniBgpNewRouteCommunityTable.setStatus("current")
_JuniBgpNewRouteCommunityEntry_Object = MibTableRow
juniBgpNewRouteCommunityEntry = _JuniBgpNewRouteCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 25, 1)
)
juniBgpNewRouteCommunityEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteOriginalRd"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteCommunityNumber"),
)
if mibBuilder.loadTexts:
    juniBgpNewRouteCommunityEntry.setStatus("current")
_JuniBgpNewRouteCommunityNumber_Type = Unsigned32
_JuniBgpNewRouteCommunityNumber_Object = MibTableColumn
juniBgpNewRouteCommunityNumber = _JuniBgpNewRouteCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 25, 1, 1),
    _JuniBgpNewRouteCommunityNumber_Type()
)
juniBgpNewRouteCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteCommunityNumber.setStatus("current")
_JuniBgpNewRouteExtendedCommunityTable_Object = MibTable
juniBgpNewRouteExtendedCommunityTable = _JuniBgpNewRouteExtendedCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 26)
)
if mibBuilder.loadTexts:
    juniBgpNewRouteExtendedCommunityTable.setStatus("current")
_JuniBgpNewRouteExtendedCommunityEntry_Object = MibTableRow
juniBgpNewRouteExtendedCommunityEntry = _JuniBgpNewRouteExtendedCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 26, 1)
)
juniBgpNewRouteExtendedCommunityEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteOriginalRd"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunityNumber"),
)
if mibBuilder.loadTexts:
    juniBgpNewRouteExtendedCommunityEntry.setStatus("current")


class _JuniBgpNewRouteExtendedCommunityNumber_Type(OctetString):
    """Custom type juniBgpNewRouteExtendedCommunityNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_JuniBgpNewRouteExtendedCommunityNumber_Type.__name__ = "OctetString"
_JuniBgpNewRouteExtendedCommunityNumber_Object = MibTableColumn
juniBgpNewRouteExtendedCommunityNumber = _JuniBgpNewRouteExtendedCommunityNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 26, 1, 1),
    _JuniBgpNewRouteExtendedCommunityNumber_Type()
)
juniBgpNewRouteExtendedCommunityNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteExtendedCommunityNumber.setStatus("current")
_JuniBgpNewRouteClusterIdTable_Object = MibTable
juniBgpNewRouteClusterIdTable = _JuniBgpNewRouteClusterIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 27)
)
if mibBuilder.loadTexts:
    juniBgpNewRouteClusterIdTable.setStatus("current")
_JuniBgpNewRouteClusterIdEntry_Object = MibTableRow
juniBgpNewRouteClusterIdEntry = _JuniBgpNewRouteClusterIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 27, 1)
)
juniBgpNewRouteClusterIdEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteSafi"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefix"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteIpAddrPrefixLen"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteDistinguisher"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRoutePeer"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteRouteType"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteOriginalRd"),
    (0, "Juniper-BGP-MIB", "juniBgpNewRouteClusterId"),
)
if mibBuilder.loadTexts:
    juniBgpNewRouteClusterIdEntry.setStatus("current")
_JuniBgpNewRouteClusterId_Type = Unsigned32
_JuniBgpNewRouteClusterId_Object = MibTableColumn
juniBgpNewRouteClusterId = _JuniBgpNewRouteClusterId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 27, 1, 1),
    _JuniBgpNewRouteClusterId_Type()
)
juniBgpNewRouteClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpNewRouteClusterId.setStatus("current")
_JuniBgpFourOctetConfederationPeerTable_Object = MibTable
juniBgpFourOctetConfederationPeerTable = _JuniBgpFourOctetConfederationPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 28)
)
if mibBuilder.loadTexts:
    juniBgpFourOctetConfederationPeerTable.setStatus("current")
_JuniBgpFourOctetConfederationPeerEntry_Object = MibTableRow
juniBgpFourOctetConfederationPeerEntry = _JuniBgpFourOctetConfederationPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 28, 1)
)
juniBgpFourOctetConfederationPeerEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpFourOctetConfederationPeerAsNumber"),
)
if mibBuilder.loadTexts:
    juniBgpFourOctetConfederationPeerEntry.setStatus("current")
_JuniBgpFourOctetConfederationPeerAsNumber_Type = JuniBgpFourOctetAsNumber
_JuniBgpFourOctetConfederationPeerAsNumber_Object = MibTableColumn
juniBgpFourOctetConfederationPeerAsNumber = _JuniBgpFourOctetConfederationPeerAsNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 28, 1, 1),
    _JuniBgpFourOctetConfederationPeerAsNumber_Type()
)
juniBgpFourOctetConfederationPeerAsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpFourOctetConfederationPeerAsNumber.setStatus("current")
_JuniBgpFourOctetConfederationPeerRowStatus_Type = RowStatus
_JuniBgpFourOctetConfederationPeerRowStatus_Object = MibTableColumn
juniBgpFourOctetConfederationPeerRowStatus = _JuniBgpFourOctetConfederationPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 28, 1, 2),
    _JuniBgpFourOctetConfederationPeerRowStatus_Type()
)
juniBgpFourOctetConfederationPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpFourOctetConfederationPeerRowStatus.setStatus("current")
_JuniBgpPeerDynamicCapabilityTable_Object = MibTable
juniBgpPeerDynamicCapabilityTable = _JuniBgpPeerDynamicCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 29)
)
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilityTable.setStatus("current")
_JuniBgpPeerDynamicCapabilityEntry_Object = MibTableRow
juniBgpPeerDynamicCapabilityEntry = _JuniBgpPeerDynamicCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 29, 1)
)
juniBgpPeerDynamicCapabilityEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerDynamicCapabilityPeerVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerDynamicCapabilityPeerRemoteAddr"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerDynamicCapabilityCode"),
)
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilityEntry.setStatus("current")
_JuniBgpPeerDynamicCapabilityPeerVrfName_Type = JuniVrfName
_JuniBgpPeerDynamicCapabilityPeerVrfName_Object = MibTableColumn
juniBgpPeerDynamicCapabilityPeerVrfName = _JuniBgpPeerDynamicCapabilityPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 29, 1, 1),
    _JuniBgpPeerDynamicCapabilityPeerVrfName_Type()
)
juniBgpPeerDynamicCapabilityPeerVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilityPeerVrfName.setStatus("current")
_JuniBgpPeerDynamicCapabilityPeerRemoteAddr_Type = IpAddress
_JuniBgpPeerDynamicCapabilityPeerRemoteAddr_Object = MibTableColumn
juniBgpPeerDynamicCapabilityPeerRemoteAddr = _JuniBgpPeerDynamicCapabilityPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 29, 1, 2),
    _JuniBgpPeerDynamicCapabilityPeerRemoteAddr_Type()
)
juniBgpPeerDynamicCapabilityPeerRemoteAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilityPeerRemoteAddr.setStatus("current")


class _JuniBgpPeerDynamicCapabilityCode_Type(Integer32):
    """Custom type juniBgpPeerDynamicCapabilityCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniBgpPeerDynamicCapabilityCode_Type.__name__ = "Integer32"
_JuniBgpPeerDynamicCapabilityCode_Object = MibTableColumn
juniBgpPeerDynamicCapabilityCode = _JuniBgpPeerDynamicCapabilityCode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 29, 1, 3),
    _JuniBgpPeerDynamicCapabilityCode_Type()
)
juniBgpPeerDynamicCapabilityCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilityCode.setStatus("current")
_JuniBgpPeerDynamicCapabilitySent_Type = TruthValue
_JuniBgpPeerDynamicCapabilitySent_Object = MibTableColumn
juniBgpPeerDynamicCapabilitySent = _JuniBgpPeerDynamicCapabilitySent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 29, 1, 4),
    _JuniBgpPeerDynamicCapabilitySent_Type()
)
juniBgpPeerDynamicCapabilitySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilitySent.setStatus("current")
_JuniBgpPeerDynamicCapabilityReceived_Type = TruthValue
_JuniBgpPeerDynamicCapabilityReceived_Object = MibTableColumn
juniBgpPeerDynamicCapabilityReceived = _JuniBgpPeerDynamicCapabilityReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 29, 1, 5),
    _JuniBgpPeerDynamicCapabilityReceived_Type()
)
juniBgpPeerDynamicCapabilityReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilityReceived.setStatus("current")
_JuniBgpPeerAddressFamilyConditionalAdvTable_Object = MibTable
juniBgpPeerAddressFamilyConditionalAdvTable = _JuniBgpPeerAddressFamilyConditionalAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30)
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvTable.setStatus("current")
_JuniBgpPeerAddressFamilyConditionalAdvEntry_Object = MibTableRow
juniBgpPeerAddressFamilyConditionalAdvEntry = _JuniBgpPeerAddressFamilyConditionalAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30, 1)
)
juniBgpPeerAddressFamilyConditionalAdvEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilyVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilySafi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemoteAddress"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerAddressFamilyConditionalAdvAdvertiseMap"),
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvEntry.setStatus("current")
_JuniBgpPeerAddressFamilyConditionalAdvAdvertiseMap_Type = JuniBgpAdvertiseMapName
_JuniBgpPeerAddressFamilyConditionalAdvAdvertiseMap_Object = MibTableColumn
juniBgpPeerAddressFamilyConditionalAdvAdvertiseMap = _JuniBgpPeerAddressFamilyConditionalAdvAdvertiseMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30, 1, 1),
    _JuniBgpPeerAddressFamilyConditionalAdvAdvertiseMap_Type()
)
juniBgpPeerAddressFamilyConditionalAdvAdvertiseMap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvAdvertiseMap.setStatus("current")
_JuniBgpPeerAddressFamilyConditionalAdvConditionMap_Type = DisplayString
_JuniBgpPeerAddressFamilyConditionalAdvConditionMap_Object = MibTableColumn
juniBgpPeerAddressFamilyConditionalAdvConditionMap = _JuniBgpPeerAddressFamilyConditionalAdvConditionMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30, 1, 2),
    _JuniBgpPeerAddressFamilyConditionalAdvConditionMap_Type()
)
juniBgpPeerAddressFamilyConditionalAdvConditionMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvConditionMap.setStatus("current")


class _JuniBgpPeerAddressFamilyConditionalAdvIsExistMap_Type(TruthValue):
    """Custom type juniBgpPeerAddressFamilyConditionalAdvIsExistMap based on TruthValue"""


_JuniBgpPeerAddressFamilyConditionalAdvIsExistMap_Object = MibTableColumn
juniBgpPeerAddressFamilyConditionalAdvIsExistMap = _JuniBgpPeerAddressFamilyConditionalAdvIsExistMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30, 1, 3),
    _JuniBgpPeerAddressFamilyConditionalAdvIsExistMap_Type()
)
juniBgpPeerAddressFamilyConditionalAdvIsExistMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvIsExistMap.setStatus("current")


class _JuniBgpPeerAddressFamilyConditionalAdvSequenceNum_Type(Integer32):
    """Custom type juniBgpPeerAddressFamilyConditionalAdvSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerAddressFamilyConditionalAdvSequenceNum_Type.__name__ = "Integer32"
_JuniBgpPeerAddressFamilyConditionalAdvSequenceNum_Object = MibTableColumn
juniBgpPeerAddressFamilyConditionalAdvSequenceNum = _JuniBgpPeerAddressFamilyConditionalAdvSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30, 1, 4),
    _JuniBgpPeerAddressFamilyConditionalAdvSequenceNum_Type()
)
juniBgpPeerAddressFamilyConditionalAdvSequenceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvSequenceNum.setStatus("current")
_JuniBgpPeerAddressFamilyConditionalAdvStatus_Type = JuniBgpConditionalAdvStatus
_JuniBgpPeerAddressFamilyConditionalAdvStatus_Object = MibTableColumn
juniBgpPeerAddressFamilyConditionalAdvStatus = _JuniBgpPeerAddressFamilyConditionalAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30, 1, 5),
    _JuniBgpPeerAddressFamilyConditionalAdvStatus_Type()
)
juniBgpPeerAddressFamilyConditionalAdvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvStatus.setStatus("current")
_JuniBgpPeerAddressFamilyConditionalAdvRowStatus_Type = RowStatus
_JuniBgpPeerAddressFamilyConditionalAdvRowStatus_Object = MibTableColumn
juniBgpPeerAddressFamilyConditionalAdvRowStatus = _JuniBgpPeerAddressFamilyConditionalAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 30, 1, 6),
    _JuniBgpPeerAddressFamilyConditionalAdvRowStatus_Type()
)
juniBgpPeerAddressFamilyConditionalAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvRowStatus.setStatus("current")
_JuniBgpPeerGroupAddressFamilyConditionalAdvTable_Object = MibTable
juniBgpPeerGroupAddressFamilyConditionalAdvTable = _JuniBgpPeerGroupAddressFamilyConditionalAdvTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31)
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvTable.setStatus("current")
_JuniBgpPeerGroupAddressFamilyConditionalAdvEntry_Object = MibTableRow
juniBgpPeerGroupAddressFamilyConditionalAdvEntry = _JuniBgpPeerGroupAddressFamilyConditionalAdvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31, 1)
)
juniBgpPeerGroupAddressFamilyConditionalAdvEntry.setIndexNames(
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyVrfName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAfi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySafi"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupGroupAddressFamilyGroupName"),
    (0, "Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap"),
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvEntry.setStatus("current")
_JuniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap_Type = JuniBgpAdvertiseMapName
_JuniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap = _JuniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31, 1, 1),
    _JuniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap_Type()
)
juniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap.setStatus("current")
_JuniBgpPeerGroupAddressFamilyConditionalAdvConditionMap_Type = DisplayString
_JuniBgpPeerGroupAddressFamilyConditionalAdvConditionMap_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyConditionalAdvConditionMap = _JuniBgpPeerGroupAddressFamilyConditionalAdvConditionMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31, 1, 2),
    _JuniBgpPeerGroupAddressFamilyConditionalAdvConditionMap_Type()
)
juniBgpPeerGroupAddressFamilyConditionalAdvConditionMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvConditionMap.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap_Type(TruthValue):
    """Custom type juniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap based on TruthValue"""


_JuniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap = _JuniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31, 1, 3),
    _JuniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap_Type()
)
juniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap.setStatus("current")


class _JuniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum_Type(Integer32):
    """Custom type juniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum_Type.__name__ = "Integer32"
_JuniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum = _JuniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31, 1, 4),
    _JuniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum_Type()
)
juniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum.setStatus("current")
_JuniBgpPeerGroupAddressFamilyConditionalAdvStatus_Type = JuniBgpConditionalAdvStatus
_JuniBgpPeerGroupAddressFamilyConditionalAdvStatus_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyConditionalAdvStatus = _JuniBgpPeerGroupAddressFamilyConditionalAdvStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31, 1, 5),
    _JuniBgpPeerGroupAddressFamilyConditionalAdvStatus_Type()
)
juniBgpPeerGroupAddressFamilyConditionalAdvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvStatus.setStatus("current")
_JuniBgpPeerGroupAddressFamilyConditionalAdvRowStatus_Type = RowStatus
_JuniBgpPeerGroupAddressFamilyConditionalAdvRowStatus_Object = MibTableColumn
juniBgpPeerGroupAddressFamilyConditionalAdvRowStatus = _JuniBgpPeerGroupAddressFamilyConditionalAdvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 1, 31, 1, 6),
    _JuniBgpPeerGroupAddressFamilyConditionalAdvRowStatus_Type()
)
juniBgpPeerGroupAddressFamilyConditionalAdvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvRowStatus.setStatus("current")
_JuniBgpConformance_ObjectIdentity = ObjectIdentity
juniBgpConformance = _JuniBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2)
)
_JuniBgpCompliances_ObjectIdentity = ObjectIdentity
juniBgpCompliances = _JuniBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1)
)
_JuniBgpConfGroups_ObjectIdentity = ObjectIdentity
juniBgpConfGroups = _JuniBgpConfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2)
)

# Managed Objects groups

juniBgpGeneralConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 1)
)
juniBgpGeneralConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpEnabled"),
        ("Juniper-BGP-MIB", "juniBgpIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpAlwaysCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpDefaultLocalPreference"),
        ("Juniper-BGP-MIB", "juniBgpEqualCostLimit"),
        ("Juniper-BGP-MIB", "juniBgpClientToClientReflection"),
        ("Juniper-BGP-MIB", "juniBgpClusterId"),
        ("Juniper-BGP-MIB", "juniBgpConfederationId"),
        ("Juniper-BGP-MIB", "juniBgpMissingAsWorst"),
        ("Juniper-BGP-MIB", "juniBgpResetAllConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseInactive"),
        ("Juniper-BGP-MIB", "juniBgpEnforceFirstAs"),
        ("Juniper-BGP-MIB", "juniBgpConfedCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpGlobalAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpExternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRibOutEnabled"),
        ("Juniper-BGP-MIB", "juniBgpOverloadShutdown"),
        ("Juniper-BGP-MIB", "juniBgpLogNeighborChanges"),
        ("Juniper-BGP-MIB", "juniBgpFastExternalFallover"),
        ("Juniper-BGP-MIB", "juniBgpInternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpMaxAsLimit"),
        ("Juniper-BGP-MIB", "juniBgpOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpPreviousOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAutomaticRouteTargetFilter"))
)
if mibBuilder.loadTexts:
    juniBgpGeneralConfGroup.setStatus("obsolete")

juniBgpStatisticsConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 2)
)
juniBgpStatisticsConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpBaselineTime"),
        ("Juniper-BGP-MIB", "juniBgpDestinationCount"),
        ("Juniper-BGP-MIB", "juniBgpDestinationMemoryUsed"),
        ("Juniper-BGP-MIB", "juniBgpRouteCount"),
        ("Juniper-BGP-MIB", "juniBgpRouteMemoryUsed"),
        ("Juniper-BGP-MIB", "juniBgpSelectedRouteCount"),
        ("Juniper-BGP-MIB", "juniBgpPathAttributeCount"),
        ("Juniper-BGP-MIB", "juniBgpPathAttributeMemoryUsed"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapHistoryCount"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapHistoryMemoryUsed"),
        ("Juniper-BGP-MIB", "juniBgpSuppressedRouteCount"))
)
if mibBuilder.loadTexts:
    juniBgpStatisticsConfGroup.setStatus("current")

juniBgpConfederationPeerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 3)
)
juniBgpConfederationPeerConfGroup.setObjects(
    ("Juniper-BGP-MIB", "juniBgpConfederationPeerRowStatus")
)
if mibBuilder.loadTexts:
    juniBgpConfederationPeerConfGroup.setStatus("deprecated")

juniBgpPeerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 4)
)
juniBgpPeerConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup.setStatus("obsolete")

juniBgpAfiSafiPeerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 5)
)
juniBgpAfiSafiPeerConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerProposedAfiSafiPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpLocalProposedAfiSafiPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpExchangedAfiSafiPeerRowStatus"))
)
if mibBuilder.loadTexts:
    juniBgpAfiSafiPeerConfGroup.setStatus("current")

juniBgpPeerAddressFamilyConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 6)
)
juniBgpPeerAddressFamilyConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPeerGroup"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendExtendedCommunity"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConfGroup.setStatus("obsolete")

juniBgpPeerGroupConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 7)
)
juniBgpPeerGroupConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup.setStatus("obsolete")

juniBgpPeerGroupAddressFamilyConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 8)
)
juniBgpPeerGroupAddressFamilyConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendExtendedCommunity"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConfGroup.setStatus("obsolete")

juniBgpRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 9)
)
juniBgpRouteConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpRouteFlapState"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapFigureOfMerit"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapRemainingTime"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpRouteFlapHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpRouteOriginatorId"),
        ("Juniper-BGP-MIB", "juniBgpRouteAtomicAggregatePresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteMedPresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteLocalPrefPresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteAggregatorPresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteOriginatorIdPresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteClusterListPresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteWeight"),
        ("Juniper-BGP-MIB", "juniBgpRouteOrigin"),
        ("Juniper-BGP-MIB", "juniBgpRouteASPathSegment"),
        ("Juniper-BGP-MIB", "juniBgpRouteNextHop"),
        ("Juniper-BGP-MIB", "juniBgpRouteMultiExitDisc"),
        ("Juniper-BGP-MIB", "juniBgpRouteLocalPref"),
        ("Juniper-BGP-MIB", "juniBgpRouteAtomicAggregate"),
        ("Juniper-BGP-MIB", "juniBgpRouteAggregatorAS"),
        ("Juniper-BGP-MIB", "juniBgpRouteAggregatorAddress"),
        ("Juniper-BGP-MIB", "juniBgpRouteBestInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpRouteUnknown"),
        ("Juniper-BGP-MIB", "juniBgpRouteExtendedCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpRouteValid"),
        ("Juniper-BGP-MIB", "juniBgpRouteSuppressedBy"),
        ("Juniper-BGP-MIB", "juniBgpRouteNextHopReachable"),
        ("Juniper-BGP-MIB", "juniBgpRouteSynchronizedWithIgp"),
        ("Juniper-BGP-MIB", "juniBgpRoutePlaceInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpRouteAdvertiseToExternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpRouteAdvertiseToInternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpRouteDistinguisher"),
        ("Juniper-BGP-MIB", "juniBgpRouteMplsLabel"),
        ("Juniper-BGP-MIB", "juniBgpRouteNextHopMetric"),
        ("Juniper-BGP-MIB", "juniBgpRouteCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpRouteExtendedCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpRouteClusterId"))
)
if mibBuilder.loadTexts:
    juniBgpRouteConfGroup.setStatus("obsolete")

juniBgpNetworkConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 10)
)
juniBgpNetworkConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpNetworkBackdoor"),
        ("Juniper-BGP-MIB", "juniBgpNetworkRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpNetworkWeightSpecified"),
        ("Juniper-BGP-MIB", "juniBgpNetworkWeight"),
        ("Juniper-BGP-MIB", "juniBgpNetworkRouteMap"))
)
if mibBuilder.loadTexts:
    juniBgpNetworkConfGroup.setStatus("obsolete")

juniBgpAggregateConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 11)
)
juniBgpAggregateConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAggregateAsSet"),
        ("Juniper-BGP-MIB", "juniBgpAggregateSummaryOnly"),
        ("Juniper-BGP-MIB", "juniBgpAggregateAttributeMap"),
        ("Juniper-BGP-MIB", "juniBgpAggregateAdvertiseMap"),
        ("Juniper-BGP-MIB", "juniBgpAggregateRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAggregateSuppressMap"))
)
if mibBuilder.loadTexts:
    juniBgpAggregateConfGroup.setStatus("obsolete")

juniBgpVrfConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 12)
)
juniBgpVrfConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpVrfSynchronization"),
        ("Juniper-BGP-MIB", "juniBgpVrfAutoSummary"),
        ("Juniper-BGP-MIB", "juniBgpVrfExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpVrfRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpVrfOperationalState"))
)
if mibBuilder.loadTexts:
    juniBgpVrfConfGroup.setStatus("obsolete")

juniBgpAddressFamilyConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 13)
)
juniBgpAddressFamilyConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRouteFlapDampening"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningRouteMapName"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyOperationalState"))
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyConfGroup.setStatus("obsolete")

juniBgpStorageConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 14)
)
juniBgpStorageConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpStorageInitialHeapSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxHeapSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialVrfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxVrfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAddressFamilyPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAddressFamilyPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerGroupPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerGroupPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerGroupAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerGroupAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialNetworkPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxNetworkPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAggregatePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAggregatePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialDestinationPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxDestinationPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAttributesPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAttributesPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRouteFlapHistoryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRouteFlapHistoryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialNetworkRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxNetworkRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRedistributedRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRedistributedRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAggregateRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAggregateRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAutoSummaryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAutoSummaryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialHistoryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxHistoryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialSendQueueEntryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxSendQueueEntryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialVpnRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxVpnRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRouteTargetPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRouteTargetPoolSize"))
)
if mibBuilder.loadTexts:
    juniBgpStorageConfGroup.setStatus("obsolete")

juniBgpGeneralConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 15)
)
juniBgpGeneralConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpEnabled"),
        ("Juniper-BGP-MIB", "juniBgpIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpAlwaysCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpDefaultLocalPreference"),
        ("Juniper-BGP-MIB", "juniBgpEqualCostLimit"),
        ("Juniper-BGP-MIB", "juniBgpClientToClientReflection"),
        ("Juniper-BGP-MIB", "juniBgpClusterId"),
        ("Juniper-BGP-MIB", "juniBgpConfederationId"),
        ("Juniper-BGP-MIB", "juniBgpMissingAsWorst"),
        ("Juniper-BGP-MIB", "juniBgpResetAllConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseInactive"),
        ("Juniper-BGP-MIB", "juniBgpEnforceFirstAs"),
        ("Juniper-BGP-MIB", "juniBgpConfedCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpGlobalAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpExternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRibOutEnabled"),
        ("Juniper-BGP-MIB", "juniBgpOverloadShutdown"),
        ("Juniper-BGP-MIB", "juniBgpLogNeighborChanges"),
        ("Juniper-BGP-MIB", "juniBgpFastExternalFallover"),
        ("Juniper-BGP-MIB", "juniBgpInternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpMaxAsLimit"),
        ("Juniper-BGP-MIB", "juniBgpOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpPreviousOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAutomaticRouteTargetFilter"),
        ("Juniper-BGP-MIB", "juniBgpDefaultIPv4Unicast"))
)
if mibBuilder.loadTexts:
    juniBgpGeneralConfGroup2.setStatus("obsolete")

juniBgpNewRouteConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 16)
)
juniBgpNewRouteConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorId"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregatePresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMedPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPrefPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorIdPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterListPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteWeight"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOrigin"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteASPathSegment"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHop"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMultiExitDisc"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPref"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregate"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAS"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAddress"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteBestInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteUnknown"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteValid"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSuppressedBy"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSynchronizedWithIgp"),
        ("Juniper-BGP-MIB", "juniBgpNewRoutePlaceInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToExternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToInternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMplsLabel"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopMetric"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapState"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapFigureOfMerit"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapRemainingTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterId"))
)
if mibBuilder.loadTexts:
    juniBgpNewRouteConfGroup.setStatus("obsolete")

juniBgpPeerConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 17)
)
juniBgpPeerConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAsNumber"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup2.setStatus("obsolete")

juniBgpPeerGroupConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 18)
)
juniBgpPeerGroupConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLocalAsNumber"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup2.setStatus("obsolete")

juniBgpVrfConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 19)
)
juniBgpVrfConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpVrfSynchronization"),
        ("Juniper-BGP-MIB", "juniBgpVrfAutoSummary"),
        ("Juniper-BGP-MIB", "juniBgpVrfExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpVrfRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpVrfOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpVrfAddUnicastRoutesToMulticastView"))
)
if mibBuilder.loadTexts:
    juniBgpVrfConfGroup2.setStatus("obsolete")

juniBgpGeneralConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 20)
)
juniBgpGeneralConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpEnabled"),
        ("Juniper-BGP-MIB", "juniBgpIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpAlwaysCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpDefaultLocalPreference"),
        ("Juniper-BGP-MIB", "juniBgpEqualCostLimit"),
        ("Juniper-BGP-MIB", "juniBgpClientToClientReflection"),
        ("Juniper-BGP-MIB", "juniBgpClusterId"),
        ("Juniper-BGP-MIB", "juniBgpConfederationId"),
        ("Juniper-BGP-MIB", "juniBgpMissingAsWorst"),
        ("Juniper-BGP-MIB", "juniBgpResetAllConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseInactive"),
        ("Juniper-BGP-MIB", "juniBgpEnforceFirstAs"),
        ("Juniper-BGP-MIB", "juniBgpConfedCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpGlobalAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpExternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRibOutEnabled"),
        ("Juniper-BGP-MIB", "juniBgpOverloadShutdown"),
        ("Juniper-BGP-MIB", "juniBgpLogNeighborChanges"),
        ("Juniper-BGP-MIB", "juniBgpFastExternalFallover"),
        ("Juniper-BGP-MIB", "juniBgpInternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpMaxAsLimit"),
        ("Juniper-BGP-MIB", "juniBgpOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpPreviousOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAutomaticRouteTargetFilter"),
        ("Juniper-BGP-MIB", "juniBgpDefaultIPv4Unicast"),
        ("Juniper-BGP-MIB", "juniBgpRedistributeInternal"),
        ("Juniper-BGP-MIB", "juniBgpUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpGeneralConfGroup3.setStatus("obsolete")

juniBgpStorageConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 21)
)
juniBgpStorageConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpStorageInitialHeapSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxHeapSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialVrfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxVrfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAddressFamilyPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAddressFamilyPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerGroupPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerGroupPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerGroupAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerGroupAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialNetworkPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxNetworkPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAggregatePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAggregatePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialDestinationPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxDestinationPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAttributesPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAttributesPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRouteFlapHistoryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRouteFlapHistoryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialNetworkRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxNetworkRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRedistributedRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRedistributedRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAggregateRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAggregateRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAutoSummaryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAutoSummaryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialSendQueueEntryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxSendQueueEntryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialVpnRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxVpnRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRouteTargetPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRouteTargetPoolSize"))
)
if mibBuilder.loadTexts:
    juniBgpStorageConfGroup2.setStatus("obsolete")

juniBgpPeerConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 22)
)
juniBgpPeerConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup3.setStatus("obsolete")

juniBgpPeerAddressFamilyConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 23)
)
juniBgpPeerAddressFamilyConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPeerGroup"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConfGroup2.setStatus("obsolete")

juniBgpPeerGroupConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 24)
)
juniBgpPeerGroupConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup3.setStatus("obsolete")

juniBgpPeerGroupAddressFamilyConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 25)
)
juniBgpPeerGroupAddressFamilyConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConfGroup2.setStatus("obsolete")

juniBgpNetworkConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 26)
)
juniBgpNetworkConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpNetworkBackdoor"),
        ("Juniper-BGP-MIB", "juniBgpNetworkRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpNetworkWeightSpecified"),
        ("Juniper-BGP-MIB", "juniBgpNetworkWeight"),
        ("Juniper-BGP-MIB", "juniBgpNetworkRouteMap"),
        ("Juniper-BGP-MIB", "juniBgpNetworkUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpNetworkConfGroup2.setStatus("current")

juniBgpAggregateConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 27)
)
juniBgpAggregateConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAggregateAsSet"),
        ("Juniper-BGP-MIB", "juniBgpAggregateSummaryOnly"),
        ("Juniper-BGP-MIB", "juniBgpAggregateAttributeMap"),
        ("Juniper-BGP-MIB", "juniBgpAggregateAdvertiseMap"),
        ("Juniper-BGP-MIB", "juniBgpAggregateRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAggregateSuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpAggregateUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpAggregateConfGroup2.setStatus("current")

juniBgpVrfConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 28)
)
juniBgpVrfConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpVrfSynchronization"),
        ("Juniper-BGP-MIB", "juniBgpVrfAutoSummary"),
        ("Juniper-BGP-MIB", "juniBgpVrfExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpVrfRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpVrfOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpVrfAddUnicastRoutesToMulticastView"),
        ("Juniper-BGP-MIB", "juniBgpVrfUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpVrfConfGroup3.setStatus("obsolete")

juniBgpAddressFamilyConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 29)
)
juniBgpAddressFamilyConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRouteFlapDampening"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningRouteMapName"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyConfGroup2.setStatus("obsolete")

juniBgpGeneralConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 30)
)
juniBgpGeneralConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpEnabled"),
        ("Juniper-BGP-MIB", "juniBgpIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpAlwaysCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpDefaultLocalPreference"),
        ("Juniper-BGP-MIB", "juniBgpClientToClientReflection"),
        ("Juniper-BGP-MIB", "juniBgpClusterId"),
        ("Juniper-BGP-MIB", "juniBgpConfederationId"),
        ("Juniper-BGP-MIB", "juniBgpMissingAsWorst"),
        ("Juniper-BGP-MIB", "juniBgpResetAllConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseInactive"),
        ("Juniper-BGP-MIB", "juniBgpEnforceFirstAs"),
        ("Juniper-BGP-MIB", "juniBgpConfedCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpGlobalAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpExternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRibOutEnabled"),
        ("Juniper-BGP-MIB", "juniBgpOverloadShutdown"),
        ("Juniper-BGP-MIB", "juniBgpLogNeighborChanges"),
        ("Juniper-BGP-MIB", "juniBgpFastExternalFallover"),
        ("Juniper-BGP-MIB", "juniBgpInternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpMaxAsLimit"),
        ("Juniper-BGP-MIB", "juniBgpOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpPreviousOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAutomaticRouteTargetFilter"),
        ("Juniper-BGP-MIB", "juniBgpDefaultIPv4Unicast"),
        ("Juniper-BGP-MIB", "juniBgpRedistributeInternal"),
        ("Juniper-BGP-MIB", "juniBgpFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpConfederationPeersFilterList"),
        ("Juniper-BGP-MIB", "juniBgpUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpGeneralConfGroup4.setStatus("obsolete")

juniBgpFourOctetConfederationPeerConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 31)
)
juniBgpFourOctetConfederationPeerConfGroup.setObjects(
    ("Juniper-BGP-MIB", "juniBgpFourOctetConfederationPeerRowStatus")
)
if mibBuilder.loadTexts:
    juniBgpFourOctetConfederationPeerConfGroup.setStatus("current")

juniBgpPeerConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 32)
)
juniBgpPeerConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedOptionalParameterNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedCapabilityNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup4.setStatus("obsolete")

juniBgpPeerAddressFamilyConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 33)
)
juniBgpPeerAddressFamilyConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPeerGroup"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedOrfEntriesLimit"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedPrefixListOrfName"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConfGroup3.setStatus("obsolete")

juniBgpPeerGroupConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 34)
)
juniBgpPeerGroupConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup4.setStatus("obsolete")

juniBgpPeerGroupAddressFamilyConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 35)
)
juniBgpPeerGroupAddressFamilyConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConfGroup3.setStatus("obsolete")

juniBgpVrfConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 36)
)
juniBgpVrfConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpVrfSynchronization"),
        ("Juniper-BGP-MIB", "juniBgpVrfAutoSummary"),
        ("Juniper-BGP-MIB", "juniBgpVrfExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpVrfResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpVrfRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpVrfOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpVrfAddUnicastRoutesToMulticastView"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsEbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsIbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfUnconfiguredAttributes"))
)
if mibBuilder.loadTexts:
    juniBgpVrfConfGroup4.setStatus("obsolete")

juniBgpDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 37)
)
juniBgpDeprecatedGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpConfederationPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLocalAsNumber"))
)
if mibBuilder.loadTexts:
    juniBgpDeprecatedGroup.setStatus("deprecated")

juniBgpNewRouteConfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 38)
)
juniBgpNewRouteConfGroup2.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorId"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregatePresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMedPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPrefPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorIdPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterListPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteWeight"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOrigin"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteASPathSegment"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHop"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMultiExitDisc"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPref"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregate"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAS"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAddress"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteBestInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteUnknown"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteValid"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSuppressedBy"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSynchronizedWithIgp"),
        ("Juniper-BGP-MIB", "juniBgpNewRoutePlaceInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToExternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToInternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopMetric"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapState"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapFigureOfMerit"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapRemainingTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterId"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMplsInLabel"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMplsOutLabel"))
)
if mibBuilder.loadTexts:
    juniBgpNewRouteConfGroup2.setStatus("obsolete")

juniBgpGeneralConfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 39)
)
juniBgpGeneralConfGroup5.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpEnabled"),
        ("Juniper-BGP-MIB", "juniBgpIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpAlwaysCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpDefaultLocalPreference"),
        ("Juniper-BGP-MIB", "juniBgpClientToClientReflection"),
        ("Juniper-BGP-MIB", "juniBgpClusterId"),
        ("Juniper-BGP-MIB", "juniBgpConfederationId"),
        ("Juniper-BGP-MIB", "juniBgpMissingAsWorst"),
        ("Juniper-BGP-MIB", "juniBgpResetAllConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseInactive"),
        ("Juniper-BGP-MIB", "juniBgpEnforceFirstAs"),
        ("Juniper-BGP-MIB", "juniBgpConfedCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpGlobalAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpExternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRibOutEnabled"),
        ("Juniper-BGP-MIB", "juniBgpOverloadShutdown"),
        ("Juniper-BGP-MIB", "juniBgpLogNeighborChanges"),
        ("Juniper-BGP-MIB", "juniBgpFastExternalFallover"),
        ("Juniper-BGP-MIB", "juniBgpInternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpMaxAsLimit"),
        ("Juniper-BGP-MIB", "juniBgpOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpPreviousOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAutomaticRouteTargetFilter"),
        ("Juniper-BGP-MIB", "juniBgpDefaultIPv4Unicast"),
        ("Juniper-BGP-MIB", "juniBgpRedistributeInternal"),
        ("Juniper-BGP-MIB", "juniBgpFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpConfederationPeersFilterList"),
        ("Juniper-BGP-MIB", "juniBgpUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseBestExternalToInternal"))
)
if mibBuilder.loadTexts:
    juniBgpGeneralConfGroup5.setStatus("obsolete")

juniBgpPeerConfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 40)
)
juniBgpPeerConfGroup5.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedOptionalParameterNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedCapabilityNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerLenient"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup5.setStatus("obsolete")

juniBgpPeerGroupConfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 41)
)
juniBgpPeerGroupConfGroup5.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLenient"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup5.setStatus("obsolete")

juniBgpVrfConfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 42)
)
juniBgpVrfConfGroup5.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpVrfSynchronization"),
        ("Juniper-BGP-MIB", "juniBgpVrfAutoSummary"),
        ("Juniper-BGP-MIB", "juniBgpVrfResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpVrfRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpVrfOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpVrfAddUnicastRoutesToMulticastView"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsEbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsIbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsEIbgp"))
)
if mibBuilder.loadTexts:
    juniBgpVrfConfGroup5.setStatus("obsolete")

juniBgpAddressFamilyConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 43)
)
juniBgpAddressFamilyConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRouteFlapDampening"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningRouteMapName"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyLocalDistance"))
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyConfGroup3.setStatus("obsolete")

juniBgpStorageConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 44)
)
juniBgpStorageConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpStorageInitialVrfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxVrfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAddressFamilyPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAddressFamilyPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerGroupPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerGroupPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialPeerGroupAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxPeerGroupAfPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialNetworkPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxNetworkPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAggregatePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAggregatePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialDestinationPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxDestinationPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAttributesPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAttributesPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRouteFlapHistoryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRouteFlapHistoryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialNetworkRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxNetworkRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRedistributedRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRedistributedRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAggregateRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAggregateRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialAutoSummaryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxAutoSummaryRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialSendQueueEntryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxSendQueueEntryPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialVpnRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxVpnRoutePoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageInitialRouteTargetPoolSize"),
        ("Juniper-BGP-MIB", "juniBgpStorageMaxRouteTargetPoolSize"))
)
if mibBuilder.loadTexts:
    juniBgpStorageConfGroup3.setStatus("obsolete")

juniBgpNewRouteConfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 45)
)
juniBgpNewRouteConfGroup3.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorId"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregatePresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMedPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPrefPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorIdPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterListPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteWeight"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOrigin"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteASPathSegment"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHop"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMultiExitDisc"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPref"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregate"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAS"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAddress"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteBestInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteUnknown"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteValid"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSuppressedBy"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSynchronizedWithIgp"),
        ("Juniper-BGP-MIB", "juniBgpNewRoutePlaceInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToExternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToInternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopMetric"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapState"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapFigureOfMerit"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapRemainingTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterId"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMplsInLabel"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMplsOutLabel"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLeaked"))
)
if mibBuilder.loadTexts:
    juniBgpNewRouteConfGroup3.setStatus("obsolete")

juniBgpPeerAddressFamilyConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 46)
)
juniBgpPeerAddressFamilyConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPeerGroup"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedOrfEntriesLimit"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedPrefixListOrfName"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendLabel"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConfGroup4.setStatus("obsolete")

juniBgpPeerGroupAddressFamilyConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 47)
)
juniBgpPeerGroupAddressFamilyConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendLabel"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConfGroup4.setStatus("obsolete")

juniBgpVrfConfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 48)
)
juniBgpVrfConfGroup6.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpVrfSynchronization"),
        ("Juniper-BGP-MIB", "juniBgpVrfAutoSummary"),
        ("Juniper-BGP-MIB", "juniBgpVrfResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpVrfRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpVrfOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpVrfAddUnicastRoutesToMulticastView"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsEbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsIbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsEIbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfCarriersCarrierModeEnabled"))
)
if mibBuilder.loadTexts:
    juniBgpVrfConfGroup6.setStatus("obsolete")

juniBgpAddressFamilyConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 49)
)
juniBgpAddressFamilyConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRouteFlapDampening"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningRouteMapName"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyCheckVpnNextHops"))
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyConfGroup4.setStatus("obsolete")

juniBgpPeerAddressFamilyConfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 50)
)
juniBgpPeerAddressFamilyConfGroup5.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPeerGroup"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedOrfEntriesLimit"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedPrefixListOrfName"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendLabel"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginateRouteMap"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConfGroup5.setStatus("obsolete")

juniBgpPeerGroupAddressFamilyConfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 51)
)
juniBgpPeerGroupAddressFamilyConfGroup5.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendLabel"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConfGroup5.setStatus("current")

juniBgpAddressFamilyConfGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 52)
)
juniBgpAddressFamilyConfGroup5.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRouteFlapDampening"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningRouteMapName"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginateRouteMap"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfProfileNameForMplsHeads"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfProfileNameForMplsTails"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyCheckVpnNextHops"))
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyConfGroup5.setStatus("obsolete")

juniBgpPeerConfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 53)
)
juniBgpPeerConfGroup6.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedOptionalParameterNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedCapabilityNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerDynamic"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup6.setStatus("obsolete")

juniBgpPeerGroupConfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 54)
)
juniBgpPeerGroupConfGroup6.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfiguredPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowAccessListName"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowMaxPeers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupCurrentDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupHighWaterMarkDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRejectedDynamicPeerCount"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup6.setStatus("obsolete")

juniBgpPeerDynamicCapabilityConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 55)
)
juniBgpPeerDynamicCapabilityConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerDynamicCapabilitySent"),
        ("Juniper-BGP-MIB", "juniBgpPeerDynamicCapabilityReceived"))
)
if mibBuilder.loadTexts:
    juniBgpPeerDynamicCapabilityConfGroup.setStatus("current")

juniBgpGeneralConfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 56)
)
juniBgpGeneralConfGroup6.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpEnabled"),
        ("Juniper-BGP-MIB", "juniBgpIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpAlwaysCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpDefaultLocalPreference"),
        ("Juniper-BGP-MIB", "juniBgpClientToClientReflection"),
        ("Juniper-BGP-MIB", "juniBgpClusterId"),
        ("Juniper-BGP-MIB", "juniBgpConfederationId"),
        ("Juniper-BGP-MIB", "juniBgpMissingAsWorst"),
        ("Juniper-BGP-MIB", "juniBgpResetAllConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseInactive"),
        ("Juniper-BGP-MIB", "juniBgpEnforceFirstAs"),
        ("Juniper-BGP-MIB", "juniBgpConfedCompareMed"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpGlobalAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpExternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpGlobalRibOutEnabled"),
        ("Juniper-BGP-MIB", "juniBgpOverloadShutdown"),
        ("Juniper-BGP-MIB", "juniBgpLogNeighborChanges"),
        ("Juniper-BGP-MIB", "juniBgpFastExternalFallover"),
        ("Juniper-BGP-MIB", "juniBgpInternalAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpMaxAsLimit"),
        ("Juniper-BGP-MIB", "juniBgpOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpPreviousOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAutomaticRouteTargetFilter"),
        ("Juniper-BGP-MIB", "juniBgpDefaultIPv4Unicast"),
        ("Juniper-BGP-MIB", "juniBgpRedistributeInternal"),
        ("Juniper-BGP-MIB", "juniBgpFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpConfederationPeersFilterList"),
        ("Juniper-BGP-MIB", "juniBgpUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpAdvertiseBestExternalToInternal"),
        ("Juniper-BGP-MIB", "juniBgpGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpGracefulRestartStalePathsTime"),
        ("Juniper-BGP-MIB", "juniBgpGracefulRestartPathSelectionDeferTimeLimit"),
        ("Juniper-BGP-MIB", "juniBgpPlatformSupportsNonStopForwarding"),
        ("Juniper-BGP-MIB", "juniBgpDeviceCanPreserveForwardingState"),
        ("Juniper-BGP-MIB", "juniBgpLastRestartWasGraceful"))
)
if mibBuilder.loadTexts:
    juniBgpGeneralConfGroup6.setStatus("current")

juniBgpPeerConfGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 57)
)
juniBgpPeerConfGroup7.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedOptionalParameterNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedCapabilityNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerDynamic"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGracefulRestartStalePathsTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentGracefulRestartRestartState"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedGracefulRestartRestartState"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires"),
        ("Juniper-BGP-MIB", "juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup7.setStatus("obsolete")

juniBgpPeerAddressFamilyConfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 58)
)
juniBgpPeerAddressFamilyConfGroup6.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPeerGroup"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedOrfEntriesLimit"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedPrefixListOrfName"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendLabel"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginateRouteMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySentCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySentForwardingStatePreserved"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedForwardingStatePreserved"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySentEndOfRibMarker"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedEndOfRibMarker"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConfGroup6.setStatus("obsolete")

juniBgpPeerGroupConfGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 59)
)
juniBgpPeerGroupConfGroup7.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfiguredPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowAccessListName"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowMaxPeers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupCurrentDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupHighWaterMarkDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRejectedDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupGracefulRestartStalePathsTime"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup7.setStatus("obsolete")

juniBgpNewRouteConfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 60)
)
juniBgpNewRouteConfGroup4.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorId"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregatePresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMedPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPrefPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOriginatorIdPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterListPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteWeight"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteOrigin"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteASPathSegment"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHop"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMultiExitDisc"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLocalPref"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAtomicAggregate"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAS"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAggregatorAddress"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteBestInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteUnknown"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunitiesPresent"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteValid"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSuppressedBy"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteSynchronizedWithIgp"),
        ("Juniper-BGP-MIB", "juniBgpNewRoutePlaceInIpRouteTable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToExternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteAdvertiseToInternalPeers"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteNextHopMetric"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapState"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapFigureOfMerit"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapRemainingTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteFlapHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteExtendedCommunityNumber"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteClusterId"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMplsInLabel"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteMplsOutLabel"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteLeaked"),
        ("Juniper-BGP-MIB", "juniBgpNewRouteStale"))
)
if mibBuilder.loadTexts:
    juniBgpNewRouteConfGroup4.setStatus("current")

juniBgpAddressFamilyConfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 61)
)
juniBgpAddressFamilyConfGroup6.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRouteFlapDampening"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningRouteMapName"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginateRouteMap"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfProfileNameForMplsHeads"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfProfileNameForMplsTails"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyCheckVpnNextHops"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyPathSelectionIsDeferred"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires"))
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyConfGroup6.setStatus("obsolete")

juniBgpVrfConfGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 62)
)
juniBgpVrfConfGroup7.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpVrfSynchronization"),
        ("Juniper-BGP-MIB", "juniBgpVrfAutoSummary"),
        ("Juniper-BGP-MIB", "juniBgpVrfResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpVrfRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpVrfOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpVrfAddUnicastRoutesToMulticastView"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsEbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsIbgp"),
        ("Juniper-BGP-MIB", "juniBgpVrfUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpVrfMaximumPathsEIbgp"))
)
if mibBuilder.loadTexts:
    juniBgpVrfConfGroup7.setStatus("current")

juniBgpPeerAddressFamilyConfGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 63)
)
juniBgpPeerAddressFamilyConfGroup7.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPeerGroup"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyNextHopUnchanged"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedOrfEntriesLimit"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedPrefixListOrfName"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySendLabel"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyDefaultOriginateRouteMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySentCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySentForwardingStatePreserved"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedForwardingStatePreserved"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilySentEndOfRibMarker"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyReceivedEndOfRibMarker"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConfGroup7.setStatus("current")

juniBgpPeerGroupAddressFamilyConfGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 64)
)
juniBgpPeerGroupAddressFamilyConfGroup6.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyNextHopSelf"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyNextHopUnchanged"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDistributeListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyPrefixTreeOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyFilterListWeightValue"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteMapOut"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteReflectorClient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitReset"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRemovePrivateAs"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnsuppressMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyInboundSoftReconfig"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAsOverride"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAllowAsIn"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendExtendedCommunity"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyMaximumPrefixStrict"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilySendLabel"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConfGroup6.setStatus("current")

juniBgpAddressFamilyConfGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 65)
)
juniBgpAddressFamilyConfGroup7.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginate"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRouteFlapDampening"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningSuppressThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningReuseThreshold"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningMaxHoldDownTime"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeReachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningHalfLifeUnreachable"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDampeningRouteMapName"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyOperationalState"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyExternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyInternalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyLocalDistance"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyDefaultOriginateRouteMap"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyCheckVpnNextHops"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyPathSelectionIsDeferred"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards"),
        ("Juniper-BGP-MIB", "juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires"))
)
if mibBuilder.loadTexts:
    juniBgpAddressFamilyConfGroup7.setStatus("current")

juniBgpPeerConfGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 66)
)
juniBgpPeerConfGroup8.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedOptionalParameterNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedCapabilityNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerDynamic"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGracefulRestartStalePathsTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentGracefulRestartRestartState"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedGracefulRestartRestartState"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires"),
        ("Juniper-BGP-MIB", "juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdEnabled"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdMinTransmitInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdMinReceiveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdMultiplier"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdSessionUp"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdDetectionTime"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup8.setStatus("obsolete")

juniBgpPeerGroupConfGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 67)
)
juniBgpPeerGroupConfGroup8.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfiguredPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowAccessListName"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowMaxPeers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupCurrentDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupHighWaterMarkDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRejectedDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupGracefulRestartStalePathsTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdEnabled"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdMinTransmitInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdMinReceiveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdMultiplier"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup8.setStatus("current")

juniBgpPeerConfGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 68)
)
juniBgpPeerConfGroup9.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerState"),
        ("Juniper-BGP-MIB", "juniBgpPeerNegotiatedVersion"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddress"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalAddressMask"),
        ("Juniper-BGP-MIB", "juniBgpPeerLocalPort"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemotePort"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutUpdates"),
        ("Juniper-BGP-MIB", "juniBgpPeerInTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerOutTotalMessages"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastErrorCode"),
        ("Juniper-BGP-MIB", "juniBgpPeerLastResetReason"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTransitions"),
        ("Juniper-BGP-MIB", "juniBgpPeerFsmEstablishedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerInUpdateElapsedTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerRemoteIdentifier"),
        ("Juniper-BGP-MIB", "juniBgpPeerWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityMultiProtocol"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedOptionalParameterNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedUnsupportedCapabilityNotification"),
        ("Juniper-BGP-MIB", "juniBgpPeerUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerDynamic"),
        ("Juniper-BGP-MIB", "juniBgpPeerShouldAdvertiseCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGracefulRestartStalePathsTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentGracefulRestartRestartState"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedGracefulRestartRestartState"),
        ("Juniper-BGP-MIB", "juniBgpPeerSentGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerReceivedGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires"),
        ("Juniper-BGP-MIB", "juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdEnabled"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdMinTransmitInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdMinReceiveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdMultiplier"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdSessionUp"),
        ("Juniper-BGP-MIB", "juniBgpPeerBfdDetectionTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerIbgpSinglehop"))
)
if mibBuilder.loadTexts:
    juniBgpPeerConfGroup9.setStatus("current")

juniBgpPeerGroupConfGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 69)
)
juniBgpPeerGroupConfGroup9.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAdminStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRetryInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigHoldTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfigKeepAliveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAsOriginationInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAdvertisementInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupDescription"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupWeight"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihop"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupEbgpMultihopTtl"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUpdateSource"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMd5Password"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupMaxUpdateSize"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupResetConnectionType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRowStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetRemoteAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupFourOctetLocalAsNumber"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilitiesOption"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupUnconfiguredAttributes"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupSiteOfOrigin"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupLenient"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupPassive"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupConfiguredPeerType"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowAccessListName"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAllowMaxPeers"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupCurrentDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupHighWaterMarkDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupRejectedDynamicPeerCount"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupGracefulRestartRestartTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupGracefulRestartStalePathsTime"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdEnabled"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdMinTransmitInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdMinReceiveInterval"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupBfdMultiplier"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupIbgpSinglehop"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupConfGroup9.setStatus("current")

juniBgpPeerAddressFamilyConditionalAdvConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 70)
)
juniBgpPeerAddressFamilyConditionalAdvConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyConditionalAdvConditionMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyConditionalAdvIsExistMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyConditionalAdvSequenceNum"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyConditionalAdvStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerAddressFamilyConditionalAdvRowStatus"))
)
if mibBuilder.loadTexts:
    juniBgpPeerAddressFamilyConditionalAdvConfGroup.setStatus("current")

juniBgpPeerGroupAddressFamilyConditionalAdvConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 2, 71)
)
juniBgpPeerGroupAddressFamilyConditionalAdvConfGroup.setObjects(
      *(("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyConditionalAdvConditionMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyConditionalAdvStatus"),
        ("Juniper-BGP-MIB", "juniBgpPeerGroupAddressFamilyConditionalAdvRowStatus"))
)
if mibBuilder.loadTexts:
    juniBgpPeerGroupAddressFamilyConditionalAdvConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniBgpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniBgpCompliance.setStatus(
        "obsolete"
    )

juniBgpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniBgpCompliance2.setStatus(
        "obsolete"
    )

juniBgpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniBgpCompliance3.setStatus(
        "obsolete"
    )

juniBgpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniBgpCompliance4.setStatus(
        "obsolete"
    )

juniBgpCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniBgpCompliance5.setStatus(
        "obsolete"
    )

juniBgpCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniBgpCompliance6.setStatus(
        "obsolete"
    )

juniBgpCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 7)
)
if mibBuilder.loadTexts:
    juniBgpCompliance7.setStatus(
        "obsolete"
    )

juniBgpCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 8)
)
if mibBuilder.loadTexts:
    juniBgpCompliance8.setStatus(
        "obsolete"
    )

juniBgpCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 9)
)
if mibBuilder.loadTexts:
    juniBgpCompliance9.setStatus(
        "obsolete"
    )

juniBgpCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 10)
)
if mibBuilder.loadTexts:
    juniBgpCompliance10.setStatus(
        "obsolete"
    )

juniBgpCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 11)
)
if mibBuilder.loadTexts:
    juniBgpCompliance11.setStatus(
        "obsolete"
    )

juniBgpCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 12)
)
if mibBuilder.loadTexts:
    juniBgpCompliance12.setStatus(
        "obsolete"
    )

juniBgpCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 13)
)
if mibBuilder.loadTexts:
    juniBgpCompliance13.setStatus(
        "obsolete"
    )

juniBgpCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 14)
)
if mibBuilder.loadTexts:
    juniBgpCompliance14.setStatus(
        "obsolete"
    )

juniBgpCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 15)
)
if mibBuilder.loadTexts:
    juniBgpCompliance15.setStatus(
        "obsolete"
    )

juniBgpCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 29, 2, 1, 16)
)
if mibBuilder.loadTexts:
    juniBgpCompliance16.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-BGP-MIB",
    **{"JuniBgpAfi": JuniBgpAfi,
       "JuniBgpSafi": JuniBgpSafi,
       "JuniBgpStorageInteger": JuniBgpStorageInteger,
       "JuniBgpResetConnectionType": JuniBgpResetConnectionType,
       "JuniBgpFourOctetAsNumber": JuniBgpFourOctetAsNumber,
       "JuniBgpAdvertiseMapName": JuniBgpAdvertiseMapName,
       "JuniBgpConditionalAdvStatus": JuniBgpConditionalAdvStatus,
       "juniBgpMIB": juniBgpMIB,
       "juniBgpObjects": juniBgpObjects,
       "juniBgpGeneralGroup": juniBgpGeneralGroup,
       "juniBgpLocalAsNumber": juniBgpLocalAsNumber,
       "juniBgpEnabled": juniBgpEnabled,
       "juniBgpIdentifier": juniBgpIdentifier,
       "juniBgpAlwaysCompareMed": juniBgpAlwaysCompareMed,
       "juniBgpDefaultLocalPreference": juniBgpDefaultLocalPreference,
       "juniBgpEqualCostLimit": juniBgpEqualCostLimit,
       "juniBgpClientToClientReflection": juniBgpClientToClientReflection,
       "juniBgpClusterId": juniBgpClusterId,
       "juniBgpConfederationId": juniBgpConfederationId,
       "juniBgpMissingAsWorst": juniBgpMissingAsWorst,
       "juniBgpResetAllConnectionType": juniBgpResetAllConnectionType,
       "juniBgpAdvertiseInactive": juniBgpAdvertiseInactive,
       "juniBgpEnforceFirstAs": juniBgpEnforceFirstAs,
       "juniBgpConfedCompareMed": juniBgpConfedCompareMed,
       "juniBgpGlobalRetryInterval": juniBgpGlobalRetryInterval,
       "juniBgpGlobalConfigKeepAliveInterval": juniBgpGlobalConfigKeepAliveInterval,
       "juniBgpGlobalConfigHoldTime": juniBgpGlobalConfigHoldTime,
       "juniBgpGlobalAsOriginationInterval": juniBgpGlobalAsOriginationInterval,
       "juniBgpExternalAdvertisementInterval": juniBgpExternalAdvertisementInterval,
       "juniBgpGlobalRibOutEnabled": juniBgpGlobalRibOutEnabled,
       "juniBgpOverloadShutdown": juniBgpOverloadShutdown,
       "juniBgpLogNeighborChanges": juniBgpLogNeighborChanges,
       "juniBgpFastExternalFallover": juniBgpFastExternalFallover,
       "juniBgpInternalAdvertisementInterval": juniBgpInternalAdvertisementInterval,
       "juniBgpMaxAsLimit": juniBgpMaxAsLimit,
       "juniBgpOperationalState": juniBgpOperationalState,
       "juniBgpPreviousOperationalState": juniBgpPreviousOperationalState,
       "juniBgpAutomaticRouteTargetFilter": juniBgpAutomaticRouteTargetFilter,
       "juniBgpDefaultIPv4Unicast": juniBgpDefaultIPv4Unicast,
       "juniBgpRedistributeInternal": juniBgpRedistributeInternal,
       "juniBgpFourOctetLocalAsNumber": juniBgpFourOctetLocalAsNumber,
       "juniBgpConfederationPeersFilterList": juniBgpConfederationPeersFilterList,
       "juniBgpUnconfiguredAttributes": juniBgpUnconfiguredAttributes,
       "juniBgpAdvertiseBestExternalToInternal": juniBgpAdvertiseBestExternalToInternal,
       "juniBgpGracefulRestartEnabled": juniBgpGracefulRestartEnabled,
       "juniBgpGracefulRestartRestartTime": juniBgpGracefulRestartRestartTime,
       "juniBgpGracefulRestartStalePathsTime": juniBgpGracefulRestartStalePathsTime,
       "juniBgpGracefulRestartPathSelectionDeferTimeLimit": juniBgpGracefulRestartPathSelectionDeferTimeLimit,
       "juniBgpPlatformSupportsNonStopForwarding": juniBgpPlatformSupportsNonStopForwarding,
       "juniBgpDeviceCanPreserveForwardingState": juniBgpDeviceCanPreserveForwardingState,
       "juniBgpLastRestartWasGraceful": juniBgpLastRestartWasGraceful,
       "juniBgpRouteTableStatisticsGroup": juniBgpRouteTableStatisticsGroup,
       "juniBgpBaselineTime": juniBgpBaselineTime,
       "juniBgpDestinationCount": juniBgpDestinationCount,
       "juniBgpDestinationMemoryUsed": juniBgpDestinationMemoryUsed,
       "juniBgpRouteCount": juniBgpRouteCount,
       "juniBgpRouteMemoryUsed": juniBgpRouteMemoryUsed,
       "juniBgpSelectedRouteCount": juniBgpSelectedRouteCount,
       "juniBgpPathAttributeCount": juniBgpPathAttributeCount,
       "juniBgpPathAttributeMemoryUsed": juniBgpPathAttributeMemoryUsed,
       "juniBgpRouteFlapHistoryCount": juniBgpRouteFlapHistoryCount,
       "juniBgpRouteFlapHistoryMemoryUsed": juniBgpRouteFlapHistoryMemoryUsed,
       "juniBgpSuppressedRouteCount": juniBgpSuppressedRouteCount,
       "juniBgpConfederationPeerTable": juniBgpConfederationPeerTable,
       "juniBgpConfederationPeerEntry": juniBgpConfederationPeerEntry,
       "juniBgpConfederationPeerAsNumber": juniBgpConfederationPeerAsNumber,
       "juniBgpConfederationPeerRowStatus": juniBgpConfederationPeerRowStatus,
       "juniBgpPeerTable": juniBgpPeerTable,
       "juniBgpPeerEntry": juniBgpPeerEntry,
       "juniBgpPeerVrfName": juniBgpPeerVrfName,
       "juniBgpPeerRemoteAddress": juniBgpPeerRemoteAddress,
       "juniBgpPeerAdminStatus": juniBgpPeerAdminStatus,
       "juniBgpPeerState": juniBgpPeerState,
       "juniBgpPeerNegotiatedVersion": juniBgpPeerNegotiatedVersion,
       "juniBgpPeerLocalAddress": juniBgpPeerLocalAddress,
       "juniBgpPeerLocalAddressMask": juniBgpPeerLocalAddressMask,
       "juniBgpPeerLocalPort": juniBgpPeerLocalPort,
       "juniBgpPeerRemoteAsNumber": juniBgpPeerRemoteAsNumber,
       "juniBgpPeerRemotePort": juniBgpPeerRemotePort,
       "juniBgpPeerInUpdates": juniBgpPeerInUpdates,
       "juniBgpPeerOutUpdates": juniBgpPeerOutUpdates,
       "juniBgpPeerInTotalMessages": juniBgpPeerInTotalMessages,
       "juniBgpPeerOutTotalMessages": juniBgpPeerOutTotalMessages,
       "juniBgpPeerLastErrorCode": juniBgpPeerLastErrorCode,
       "juniBgpPeerLastResetReason": juniBgpPeerLastResetReason,
       "juniBgpPeerFsmEstablishedTransitions": juniBgpPeerFsmEstablishedTransitions,
       "juniBgpPeerFsmEstablishedTime": juniBgpPeerFsmEstablishedTime,
       "juniBgpPeerRetryInterval": juniBgpPeerRetryInterval,
       "juniBgpPeerHoldTime": juniBgpPeerHoldTime,
       "juniBgpPeerKeepAliveInterval": juniBgpPeerKeepAliveInterval,
       "juniBgpPeerConfigHoldTime": juniBgpPeerConfigHoldTime,
       "juniBgpPeerConfigKeepAliveInterval": juniBgpPeerConfigKeepAliveInterval,
       "juniBgpPeerAsOriginationInterval": juniBgpPeerAsOriginationInterval,
       "juniBgpPeerAdvertisementInterval": juniBgpPeerAdvertisementInterval,
       "juniBgpPeerInUpdateElapsedTime": juniBgpPeerInUpdateElapsedTime,
       "juniBgpPeerDescription": juniBgpPeerDescription,
       "juniBgpPeerRemoteIdentifier": juniBgpPeerRemoteIdentifier,
       "juniBgpPeerWeight": juniBgpPeerWeight,
       "juniBgpPeerEbgpMultihop": juniBgpPeerEbgpMultihop,
       "juniBgpPeerEbgpMultihopTtl": juniBgpPeerEbgpMultihopTtl,
       "juniBgpPeerUpdateSource": juniBgpPeerUpdateSource,
       "juniBgpPeerMd5Password": juniBgpPeerMd5Password,
       "juniBgpPeerMaxUpdateSize": juniBgpPeerMaxUpdateSize,
       "juniBgpPeerType": juniBgpPeerType,
       "juniBgpPeerReceivedCapabilitiesOption": juniBgpPeerReceivedCapabilitiesOption,
       "juniBgpPeerReceivedCapabilityMultiProtocol": juniBgpPeerReceivedCapabilityMultiProtocol,
       "juniBgpPeerReceivedCapabilityRouteRefresh": juniBgpPeerReceivedCapabilityRouteRefresh,
       "juniBgpPeerReceivedCapabilityRouteRefreshCisco": juniBgpPeerReceivedCapabilityRouteRefreshCisco,
       "juniBgpPeerResetConnectionType": juniBgpPeerResetConnectionType,
       "juniBgpPeerRowStatus": juniBgpPeerRowStatus,
       "juniBgpPeerLocalAsNumber": juniBgpPeerLocalAsNumber,
       "juniBgpPeerFourOctetRemoteAsNumber": juniBgpPeerFourOctetRemoteAsNumber,
       "juniBgpPeerFourOctetLocalAsNumber": juniBgpPeerFourOctetLocalAsNumber,
       "juniBgpPeerReceivedCapabilityFourOctetAsNumbers": juniBgpPeerReceivedCapabilityFourOctetAsNumbers,
       "juniBgpPeerReceivedCapabilityDynamicCapabilityNeg": juniBgpPeerReceivedCapabilityDynamicCapabilityNeg,
       "juniBgpPeerShouldAdvertiseCapabilitiesOption": juniBgpPeerShouldAdvertiseCapabilitiesOption,
       "juniBgpPeerShouldAdvertiseCapabilityRouteRefresh": juniBgpPeerShouldAdvertiseCapabilityRouteRefresh,
       "juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco": juniBgpPeerShouldAdvertiseCapabilityRouteRefreshCisco,
       "juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers": juniBgpPeerShouldAdvertiseCapabilityFourOctetAsNumbers,
       "juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg": juniBgpPeerShouldAdvertiseCapabilityDynamicCapabilityNeg,
       "juniBgpPeerSentCapabilitiesOption": juniBgpPeerSentCapabilitiesOption,
       "juniBgpPeerSentCapabilityMultiProtocol": juniBgpPeerSentCapabilityMultiProtocol,
       "juniBgpPeerSentCapabilityRouteRefresh": juniBgpPeerSentCapabilityRouteRefresh,
       "juniBgpPeerSentCapabilityRouteRefreshCisco": juniBgpPeerSentCapabilityRouteRefreshCisco,
       "juniBgpPeerSentCapabilityFourOctetAsNumbers": juniBgpPeerSentCapabilityFourOctetAsNumbers,
       "juniBgpPeerSentCapabilityDynamicCapabilityNeg": juniBgpPeerSentCapabilityDynamicCapabilityNeg,
       "juniBgpPeerReceivedUnsupportedOptionalParameterNotification": juniBgpPeerReceivedUnsupportedOptionalParameterNotification,
       "juniBgpPeerReceivedUnsupportedCapabilityNotification": juniBgpPeerReceivedUnsupportedCapabilityNotification,
       "juniBgpPeerUnconfiguredAttributes": juniBgpPeerUnconfiguredAttributes,
       "juniBgpPeerSiteOfOrigin": juniBgpPeerSiteOfOrigin,
       "juniBgpPeerLenient": juniBgpPeerLenient,
       "juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg": juniBgpPeerReceivedCapabilityOldDynamicCapabilityNeg,
       "juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg": juniBgpPeerShouldAdvertiseCapabilityOldDynamicCapabilityNeg,
       "juniBgpPeerSentCapabilityOldDynamicCapabilityNeg": juniBgpPeerSentCapabilityOldDynamicCapabilityNeg,
       "juniBgpPeerPassive": juniBgpPeerPassive,
       "juniBgpPeerDynamic": juniBgpPeerDynamic,
       "juniBgpPeerShouldAdvertiseCapabilityGracefulRestart": juniBgpPeerShouldAdvertiseCapabilityGracefulRestart,
       "juniBgpPeerSentCapabilityGracefulRestart": juniBgpPeerSentCapabilityGracefulRestart,
       "juniBgpPeerReceivedCapabilityGracefulRestart": juniBgpPeerReceivedCapabilityGracefulRestart,
       "juniBgpPeerGracefulRestartRestartTime": juniBgpPeerGracefulRestartRestartTime,
       "juniBgpPeerGracefulRestartStalePathsTime": juniBgpPeerGracefulRestartStalePathsTime,
       "juniBgpPeerSentGracefulRestartRestartState": juniBgpPeerSentGracefulRestartRestartState,
       "juniBgpPeerReceivedGracefulRestartRestartState": juniBgpPeerReceivedGracefulRestartRestartState,
       "juniBgpPeerSentGracefulRestartRestartTime": juniBgpPeerSentGracefulRestartRestartTime,
       "juniBgpPeerReceivedGracefulRestartRestartTime": juniBgpPeerReceivedGracefulRestartRestartTime,
       "juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires": juniBgpPeerTimeUntilGracefulRestartRestartTimerExpires,
       "juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires": juniBgpPeerTimeUntilGracefulRestartStalePathsTimerExpires,
       "juniBgpPeerBfdEnabled": juniBgpPeerBfdEnabled,
       "juniBgpPeerBfdMinTransmitInterval": juniBgpPeerBfdMinTransmitInterval,
       "juniBgpPeerBfdMinReceiveInterval": juniBgpPeerBfdMinReceiveInterval,
       "juniBgpPeerBfdMultiplier": juniBgpPeerBfdMultiplier,
       "juniBgpPeerBfdSessionUp": juniBgpPeerBfdSessionUp,
       "juniBgpPeerBfdDetectionTime": juniBgpPeerBfdDetectionTime,
       "juniBgpPeerIbgpSinglehop": juniBgpPeerIbgpSinglehop,
       "juniBgpPeerProposedAfiSafiPeerTable": juniBgpPeerProposedAfiSafiPeerTable,
       "juniBgpPeerProposedAfiSafiPeerEntry": juniBgpPeerProposedAfiSafiPeerEntry,
       "juniBgpPeerProposedAfiSafiPeerVrfName": juniBgpPeerProposedAfiSafiPeerVrfName,
       "juniBgpPeerProposedAfiSafiPeerRemoteAddr": juniBgpPeerProposedAfiSafiPeerRemoteAddr,
       "juniBgpPeerProposedAfiSafiPeerAfi": juniBgpPeerProposedAfiSafiPeerAfi,
       "juniBgpPeerProposedAfiSafiPeerSafi": juniBgpPeerProposedAfiSafiPeerSafi,
       "juniBgpPeerProposedAfiSafiPeerRowStatus": juniBgpPeerProposedAfiSafiPeerRowStatus,
       "juniBgpLocalProposedAfiSafiPeerTable": juniBgpLocalProposedAfiSafiPeerTable,
       "juniBgpLocalProposedAfiSafiPeerEntry": juniBgpLocalProposedAfiSafiPeerEntry,
       "juniBgpLocalProposedAfiSafiPeerVrfName": juniBgpLocalProposedAfiSafiPeerVrfName,
       "juniBgpLocalProposedAfiSafiPeerRemoteAddr": juniBgpLocalProposedAfiSafiPeerRemoteAddr,
       "juniBgpLocalProposedAfiSafiPeerAfi": juniBgpLocalProposedAfiSafiPeerAfi,
       "juniBgpLocalProposedAfiSafiPeerSafi": juniBgpLocalProposedAfiSafiPeerSafi,
       "juniBgpLocalProposedAfiSafiPeerRowStatus": juniBgpLocalProposedAfiSafiPeerRowStatus,
       "juniBgpExchangedAfiSafiPeerTable": juniBgpExchangedAfiSafiPeerTable,
       "juniBgpExchangedAfiSafiPeerEntry": juniBgpExchangedAfiSafiPeerEntry,
       "juniBgpExchangedAfiSafiPeerVrfName": juniBgpExchangedAfiSafiPeerVrfName,
       "juniBgpExchangedAfiSafiPeerRemoteAddr": juniBgpExchangedAfiSafiPeerRemoteAddr,
       "juniBgpExchangedAfiSafiPeerAfi": juniBgpExchangedAfiSafiPeerAfi,
       "juniBgpExchangedAfiSafiPeerSafi": juniBgpExchangedAfiSafiPeerSafi,
       "juniBgpExchangedAfiSafiPeerRowStatus": juniBgpExchangedAfiSafiPeerRowStatus,
       "juniBgpPeerAddressFamilyTable": juniBgpPeerAddressFamilyTable,
       "juniBgpPeerAddressFamilyEntry": juniBgpPeerAddressFamilyEntry,
       "juniBgpPeerAddressFamilyVrfName": juniBgpPeerAddressFamilyVrfName,
       "juniBgpPeerAddressFamilyAfi": juniBgpPeerAddressFamilyAfi,
       "juniBgpPeerAddressFamilySafi": juniBgpPeerAddressFamilySafi,
       "juniBgpPeerAddressFamilyRemoteAddress": juniBgpPeerAddressFamilyRemoteAddress,
       "juniBgpPeerAddressFamilyPeerGroup": juniBgpPeerAddressFamilyPeerGroup,
       "juniBgpPeerAddressFamilyDefaultOriginate": juniBgpPeerAddressFamilyDefaultOriginate,
       "juniBgpPeerAddressFamilyNextHopSelf": juniBgpPeerAddressFamilyNextHopSelf,
       "juniBgpPeerAddressFamilySendCommunity": juniBgpPeerAddressFamilySendCommunity,
       "juniBgpPeerAddressFamilyDistributeListIn": juniBgpPeerAddressFamilyDistributeListIn,
       "juniBgpPeerAddressFamilyDistributeListOut": juniBgpPeerAddressFamilyDistributeListOut,
       "juniBgpPeerAddressFamilyPrefixListIn": juniBgpPeerAddressFamilyPrefixListIn,
       "juniBgpPeerAddressFamilyPrefixListOut": juniBgpPeerAddressFamilyPrefixListOut,
       "juniBgpPeerAddressFamilyPrefixTreeIn": juniBgpPeerAddressFamilyPrefixTreeIn,
       "juniBgpPeerAddressFamilyPrefixTreeOut": juniBgpPeerAddressFamilyPrefixTreeOut,
       "juniBgpPeerAddressFamilyFilterListIn": juniBgpPeerAddressFamilyFilterListIn,
       "juniBgpPeerAddressFamilyFilterListOut": juniBgpPeerAddressFamilyFilterListOut,
       "juniBgpPeerAddressFamilyFilterListWeight": juniBgpPeerAddressFamilyFilterListWeight,
       "juniBgpPeerAddressFamilyFilterListWeightValue": juniBgpPeerAddressFamilyFilterListWeightValue,
       "juniBgpPeerAddressFamilyRouteMapIn": juniBgpPeerAddressFamilyRouteMapIn,
       "juniBgpPeerAddressFamilyRouteMapOut": juniBgpPeerAddressFamilyRouteMapOut,
       "juniBgpPeerAddressFamilyRouteReflectorClient": juniBgpPeerAddressFamilyRouteReflectorClient,
       "juniBgpPeerAddressFamilyRouteLimitWarn": juniBgpPeerAddressFamilyRouteLimitWarn,
       "juniBgpPeerAddressFamilyRouteLimitReset": juniBgpPeerAddressFamilyRouteLimitReset,
       "juniBgpPeerAddressFamilyRouteLimitWarnOnly": juniBgpPeerAddressFamilyRouteLimitWarnOnly,
       "juniBgpPeerAddressFamilyRemovePrivateAs": juniBgpPeerAddressFamilyRemovePrivateAs,
       "juniBgpPeerAddressFamilyUnsuppressMap": juniBgpPeerAddressFamilyUnsuppressMap,
       "juniBgpPeerAddressFamilyInboundSoftReconfig": juniBgpPeerAddressFamilyInboundSoftReconfig,
       "juniBgpPeerAddressFamilyResetConnectionType": juniBgpPeerAddressFamilyResetConnectionType,
       "juniBgpPeerAddressFamilyRowStatus": juniBgpPeerAddressFamilyRowStatus,
       "juniBgpPeerAddressFamilyAsOverride": juniBgpPeerAddressFamilyAsOverride,
       "juniBgpPeerAddressFamilyAllowAsIn": juniBgpPeerAddressFamilyAllowAsIn,
       "juniBgpPeerAddressFamilySendExtendedCommunity": juniBgpPeerAddressFamilySendExtendedCommunity,
       "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend": juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfSend,
       "juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive": juniBgpPeerAddressFamilyAdvertiseCapPrefixListOrfReceive,
       "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend": juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfSend,
       "juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive": juniBgpPeerAddressFamilyAdvertiseCapPrefixListCiscoOrfReceive,
       "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend": juniBgpPeerAddressFamilyReceivedCapPrefixListOrfSend,
       "juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive": juniBgpPeerAddressFamilyReceivedCapPrefixListOrfReceive,
       "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend": juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfSend,
       "juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive": juniBgpPeerAddressFamilyReceivedCapPrefixListCiscoOrfReceive,
       "juniBgpPeerAddressFamilyReceivedOrfEntriesLimit": juniBgpPeerAddressFamilyReceivedOrfEntriesLimit,
       "juniBgpPeerAddressFamilyReceivedPrefixListOrfName": juniBgpPeerAddressFamilyReceivedPrefixListOrfName,
       "juniBgpPeerAddressFamilyMaximumPrefixStrict": juniBgpPeerAddressFamilyMaximumPrefixStrict,
       "juniBgpPeerAddressFamilyUnconfiguredAttributes": juniBgpPeerAddressFamilyUnconfiguredAttributes,
       "juniBgpPeerAddressFamilySendLabel": juniBgpPeerAddressFamilySendLabel,
       "juniBgpPeerAddressFamilyDefaultOriginateRouteMap": juniBgpPeerAddressFamilyDefaultOriginateRouteMap,
       "juniBgpPeerAddressFamilySentCapabilityGracefulRestart": juniBgpPeerAddressFamilySentCapabilityGracefulRestart,
       "juniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart": juniBgpPeerAddressFamilyReceivedCapabilityGracefulRestart,
       "juniBgpPeerAddressFamilySentForwardingStatePreserved": juniBgpPeerAddressFamilySentForwardingStatePreserved,
       "juniBgpPeerAddressFamilyReceivedForwardingStatePreserved": juniBgpPeerAddressFamilyReceivedForwardingStatePreserved,
       "juniBgpPeerAddressFamilySentEndOfRibMarker": juniBgpPeerAddressFamilySentEndOfRibMarker,
       "juniBgpPeerAddressFamilyReceivedEndOfRibMarker": juniBgpPeerAddressFamilyReceivedEndOfRibMarker,
       "juniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes": juniBgpPeerAddressFamilyWaitingForEndOfRibBeforeFlushStaleRoutes,
       "juniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection": juniBgpPeerAddressFamilyWaitingForEndOfRibBeforePathSelection,
       "juniBgpPeerAddressFamilyNextHopUnchanged": juniBgpPeerAddressFamilyNextHopUnchanged,
       "juniBgpPeerGroupTable": juniBgpPeerGroupTable,
       "juniBgpPeerGroupEntry": juniBgpPeerGroupEntry,
       "juniBgpPeerGroupVrfName": juniBgpPeerGroupVrfName,
       "juniBgpPeerGroupGroupName": juniBgpPeerGroupGroupName,
       "juniBgpPeerGroupAdminStatus": juniBgpPeerGroupAdminStatus,
       "juniBgpPeerGroupRemoteAsNumber": juniBgpPeerGroupRemoteAsNumber,
       "juniBgpPeerGroupRetryInterval": juniBgpPeerGroupRetryInterval,
       "juniBgpPeerGroupConfigHoldTime": juniBgpPeerGroupConfigHoldTime,
       "juniBgpPeerGroupConfigKeepAliveInterval": juniBgpPeerGroupConfigKeepAliveInterval,
       "juniBgpPeerGroupAsOriginationInterval": juniBgpPeerGroupAsOriginationInterval,
       "juniBgpPeerGroupAdvertisementInterval": juniBgpPeerGroupAdvertisementInterval,
       "juniBgpPeerGroupDescription": juniBgpPeerGroupDescription,
       "juniBgpPeerGroupWeight": juniBgpPeerGroupWeight,
       "juniBgpPeerGroupEbgpMultihop": juniBgpPeerGroupEbgpMultihop,
       "juniBgpPeerGroupEbgpMultihopTtl": juniBgpPeerGroupEbgpMultihopTtl,
       "juniBgpPeerGroupUpdateSource": juniBgpPeerGroupUpdateSource,
       "juniBgpPeerGroupMd5Password": juniBgpPeerGroupMd5Password,
       "juniBgpPeerGroupMaxUpdateSize": juniBgpPeerGroupMaxUpdateSize,
       "juniBgpPeerGroupResetConnectionType": juniBgpPeerGroupResetConnectionType,
       "juniBgpPeerGroupRowStatus": juniBgpPeerGroupRowStatus,
       "juniBgpPeerGroupLocalAsNumber": juniBgpPeerGroupLocalAsNumber,
       "juniBgpPeerGroupFourOctetRemoteAsNumber": juniBgpPeerGroupFourOctetRemoteAsNumber,
       "juniBgpPeerGroupFourOctetLocalAsNumber": juniBgpPeerGroupFourOctetLocalAsNumber,
       "juniBgpPeerGroupShouldAdvertiseCapabilitiesOption": juniBgpPeerGroupShouldAdvertiseCapabilitiesOption,
       "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh": juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefresh,
       "juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco": juniBgpPeerGroupShouldAdvertiseCapabilityRouteRefreshCisco,
       "juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers": juniBgpPeerGroupShouldAdvertiseCapabilityFourOctetAsNumbers,
       "juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg": juniBgpPeerGroupShouldAdvertiseCapabilityDynamicCapabilityNeg,
       "juniBgpPeerGroupUnconfiguredAttributes": juniBgpPeerGroupUnconfiguredAttributes,
       "juniBgpPeerGroupSiteOfOrigin": juniBgpPeerGroupSiteOfOrigin,
       "juniBgpPeerGroupLenient": juniBgpPeerGroupLenient,
       "juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg": juniBgpPeerGroupShouldAdvertiseCapabilityOldDynamicCapabilityNeg,
       "juniBgpPeerGroupPassive": juniBgpPeerGroupPassive,
       "juniBgpPeerGroupConfiguredPeerType": juniBgpPeerGroupConfiguredPeerType,
       "juniBgpPeerGroupAllowAccessListName": juniBgpPeerGroupAllowAccessListName,
       "juniBgpPeerGroupAllowMaxPeers": juniBgpPeerGroupAllowMaxPeers,
       "juniBgpPeerGroupCurrentDynamicPeerCount": juniBgpPeerGroupCurrentDynamicPeerCount,
       "juniBgpPeerGroupHighWaterMarkDynamicPeerCount": juniBgpPeerGroupHighWaterMarkDynamicPeerCount,
       "juniBgpPeerGroupRejectedDynamicPeerCount": juniBgpPeerGroupRejectedDynamicPeerCount,
       "juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart": juniBgpPeerGroupShouldAdvertiseCapabilityGracefulRestart,
       "juniBgpPeerGroupGracefulRestartRestartTime": juniBgpPeerGroupGracefulRestartRestartTime,
       "juniBgpPeerGroupGracefulRestartStalePathsTime": juniBgpPeerGroupGracefulRestartStalePathsTime,
       "juniBgpPeerGroupBfdEnabled": juniBgpPeerGroupBfdEnabled,
       "juniBgpPeerGroupBfdMinTransmitInterval": juniBgpPeerGroupBfdMinTransmitInterval,
       "juniBgpPeerGroupBfdMinReceiveInterval": juniBgpPeerGroupBfdMinReceiveInterval,
       "juniBgpPeerGroupBfdMultiplier": juniBgpPeerGroupBfdMultiplier,
       "juniBgpPeerGroupIbgpSinglehop": juniBgpPeerGroupIbgpSinglehop,
       "juniBgpPeerGroupAddressFamilyTable": juniBgpPeerGroupAddressFamilyTable,
       "juniBgpPeerGroupAddressFamilyEntry": juniBgpPeerGroupAddressFamilyEntry,
       "juniBgpPeerGroupAddressFamilyVrfName": juniBgpPeerGroupAddressFamilyVrfName,
       "juniBgpPeerGroupAddressFamilyAfi": juniBgpPeerGroupAddressFamilyAfi,
       "juniBgpPeerGroupAddressFamilySafi": juniBgpPeerGroupAddressFamilySafi,
       "juniBgpPeerGroupGroupAddressFamilyGroupName": juniBgpPeerGroupGroupAddressFamilyGroupName,
       "juniBgpPeerGroupAddressFamilyDefaultOriginate": juniBgpPeerGroupAddressFamilyDefaultOriginate,
       "juniBgpPeerGroupAddressFamilyNextHopSelf": juniBgpPeerGroupAddressFamilyNextHopSelf,
       "juniBgpPeerGroupAddressFamilySendCommunity": juniBgpPeerGroupAddressFamilySendCommunity,
       "juniBgpPeerGroupAddressFamilyDistributeListIn": juniBgpPeerGroupAddressFamilyDistributeListIn,
       "juniBgpPeerGroupAddressFamilyDistributeListOut": juniBgpPeerGroupAddressFamilyDistributeListOut,
       "juniBgpPeerGroupAddressFamilyPrefixListIn": juniBgpPeerGroupAddressFamilyPrefixListIn,
       "juniBgpPeerGroupAddressFamilyPrefixListOut": juniBgpPeerGroupAddressFamilyPrefixListOut,
       "juniBgpPeerGroupAddressFamilyPrefixTreeIn": juniBgpPeerGroupAddressFamilyPrefixTreeIn,
       "juniBgpPeerGroupAddressFamilyPrefixTreeOut": juniBgpPeerGroupAddressFamilyPrefixTreeOut,
       "juniBgpPeerGroupAddressFamilyFilterListIn": juniBgpPeerGroupAddressFamilyFilterListIn,
       "juniBgpPeerGroupAddressFamilyFilterListOut": juniBgpPeerGroupAddressFamilyFilterListOut,
       "juniBgpPeerGroupAddressFamilyFilterListWeight": juniBgpPeerGroupAddressFamilyFilterListWeight,
       "juniBgpPeerGroupAddressFamilyFilterListWeightValue": juniBgpPeerGroupAddressFamilyFilterListWeightValue,
       "juniBgpPeerGroupAddressFamilyRouteMapIn": juniBgpPeerGroupAddressFamilyRouteMapIn,
       "juniBgpPeerGroupAddressFamilyRouteMapOut": juniBgpPeerGroupAddressFamilyRouteMapOut,
       "juniBgpPeerGroupAddressFamilyRouteReflectorClient": juniBgpPeerGroupAddressFamilyRouteReflectorClient,
       "juniBgpPeerGroupAddressFamilyRouteLimitWarn": juniBgpPeerGroupAddressFamilyRouteLimitWarn,
       "juniBgpPeerGroupAddressFamilyRouteLimitReset": juniBgpPeerGroupAddressFamilyRouteLimitReset,
       "juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly": juniBgpPeerGroupAddressFamilyRouteLimitWarnOnly,
       "juniBgpPeerGroupAddressFamilyRemovePrivateAs": juniBgpPeerGroupAddressFamilyRemovePrivateAs,
       "juniBgpPeerGroupAddressFamilyUnsuppressMap": juniBgpPeerGroupAddressFamilyUnsuppressMap,
       "juniBgpPeerGroupAddressFamilyInboundSoftReconfig": juniBgpPeerGroupAddressFamilyInboundSoftReconfig,
       "juniBgpPeerGroupAddressFamilyResetConnectionType": juniBgpPeerGroupAddressFamilyResetConnectionType,
       "juniBgpPeerGroupAddressFamilyRowStatus": juniBgpPeerGroupAddressFamilyRowStatus,
       "juniBgpPeerGroupAddressFamilyAsOverride": juniBgpPeerGroupAddressFamilyAsOverride,
       "juniBgpPeerGroupAddressFamilyAllowAsIn": juniBgpPeerGroupAddressFamilyAllowAsIn,
       "juniBgpPeerGroupAddressFamilySendExtendedCommunity": juniBgpPeerGroupAddressFamilySendExtendedCommunity,
       "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend": juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListOrfSend,
       "juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend": juniBgpPeerGroupAddressFamilyAdvertiseCapPrefixListCiscoOrfSend,
       "juniBgpPeerGroupAddressFamilyMaximumPrefixStrict": juniBgpPeerGroupAddressFamilyMaximumPrefixStrict,
       "juniBgpPeerGroupAddressFamilyUnconfiguredAttributes": juniBgpPeerGroupAddressFamilyUnconfiguredAttributes,
       "juniBgpPeerGroupAddressFamilySendLabel": juniBgpPeerGroupAddressFamilySendLabel,
       "juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap": juniBgpPeerGroupAddressFamilyDefaultOriginateRouteMap,
       "juniBgpPeerGroupAddressFamilyNextHopUnchanged": juniBgpPeerGroupAddressFamilyNextHopUnchanged,
       "juniBgpRouteFlapHistoryTable": juniBgpRouteFlapHistoryTable,
       "juniBgpRouteFlapHistoryEntry": juniBgpRouteFlapHistoryEntry,
       "juniBgpRouteFlapState": juniBgpRouteFlapState,
       "juniBgpRouteFlapFigureOfMerit": juniBgpRouteFlapFigureOfMerit,
       "juniBgpRouteFlapRemainingTime": juniBgpRouteFlapRemainingTime,
       "juniBgpRouteFlapSuppressThreshold": juniBgpRouteFlapSuppressThreshold,
       "juniBgpRouteFlapReuseThreshold": juniBgpRouteFlapReuseThreshold,
       "juniBgpRouteFlapMaxHoldDownTime": juniBgpRouteFlapMaxHoldDownTime,
       "juniBgpRouteFlapHalfLifeReachable": juniBgpRouteFlapHalfLifeReachable,
       "juniBgpRouteFlapHalfLifeUnreachable": juniBgpRouteFlapHalfLifeUnreachable,
       "juniBgpRouteTable": juniBgpRouteTable,
       "juniBgpRouteEntry": juniBgpRouteEntry,
       "juniBgpRouteOriginatorId": juniBgpRouteOriginatorId,
       "juniBgpRouteAtomicAggregatePresent": juniBgpRouteAtomicAggregatePresent,
       "juniBgpRouteMedPresent": juniBgpRouteMedPresent,
       "juniBgpRouteLocalPrefPresent": juniBgpRouteLocalPrefPresent,
       "juniBgpRouteAggregatorPresent": juniBgpRouteAggregatorPresent,
       "juniBgpRouteCommunitiesPresent": juniBgpRouteCommunitiesPresent,
       "juniBgpRouteOriginatorIdPresent": juniBgpRouteOriginatorIdPresent,
       "juniBgpRouteClusterListPresent": juniBgpRouteClusterListPresent,
       "juniBgpRouteWeight": juniBgpRouteWeight,
       "juniBgpRouteVrfName": juniBgpRouteVrfName,
       "juniBgpRouteAfi": juniBgpRouteAfi,
       "juniBgpRouteSafi": juniBgpRouteSafi,
       "juniBgpRoutePeer": juniBgpRoutePeer,
       "juniBgpRouteIpAddrPrefixLen": juniBgpRouteIpAddrPrefixLen,
       "juniBgpRouteIpAddrPrefix": juniBgpRouteIpAddrPrefix,
       "juniBgpRouteRouteType": juniBgpRouteRouteType,
       "juniBgpRouteOrigin": juniBgpRouteOrigin,
       "juniBgpRouteASPathSegment": juniBgpRouteASPathSegment,
       "juniBgpRouteNextHop": juniBgpRouteNextHop,
       "juniBgpRouteMultiExitDisc": juniBgpRouteMultiExitDisc,
       "juniBgpRouteLocalPref": juniBgpRouteLocalPref,
       "juniBgpRouteAtomicAggregate": juniBgpRouteAtomicAggregate,
       "juniBgpRouteAggregatorAS": juniBgpRouteAggregatorAS,
       "juniBgpRouteAggregatorAddress": juniBgpRouteAggregatorAddress,
       "juniBgpRouteBestInIpRouteTable": juniBgpRouteBestInIpRouteTable,
       "juniBgpRouteUnknown": juniBgpRouteUnknown,
       "juniBgpRouteExtendedCommunitiesPresent": juniBgpRouteExtendedCommunitiesPresent,
       "juniBgpRouteValid": juniBgpRouteValid,
       "juniBgpRouteSuppressedBy": juniBgpRouteSuppressedBy,
       "juniBgpRouteNextHopReachable": juniBgpRouteNextHopReachable,
       "juniBgpRouteSynchronizedWithIgp": juniBgpRouteSynchronizedWithIgp,
       "juniBgpRoutePlaceInIpRouteTable": juniBgpRoutePlaceInIpRouteTable,
       "juniBgpRouteAdvertiseToExternalPeers": juniBgpRouteAdvertiseToExternalPeers,
       "juniBgpRouteAdvertiseToInternalPeers": juniBgpRouteAdvertiseToInternalPeers,
       "juniBgpRouteDistinguisher": juniBgpRouteDistinguisher,
       "juniBgpRouteMplsLabel": juniBgpRouteMplsLabel,
       "juniBgpRouteNextHopMetric": juniBgpRouteNextHopMetric,
       "juniBgpRouteCommunityTable": juniBgpRouteCommunityTable,
       "juniBgpRouteCommunityEntry": juniBgpRouteCommunityEntry,
       "juniBgpRouteCommunityNumber": juniBgpRouteCommunityNumber,
       "juniBgpRouteClusterIdTable": juniBgpRouteClusterIdTable,
       "juniBgpRouteClusterIdEntry": juniBgpRouteClusterIdEntry,
       "juniBgpRouteClusterId": juniBgpRouteClusterId,
       "juniBgpNetworkTable": juniBgpNetworkTable,
       "juniBgpNetworkEntry": juniBgpNetworkEntry,
       "juniBgpNetworkVrfName": juniBgpNetworkVrfName,
       "juniBgpNetworkAfi": juniBgpNetworkAfi,
       "juniBgpNetworkSafi": juniBgpNetworkSafi,
       "juniBgpNetworkIpAddrPrefix": juniBgpNetworkIpAddrPrefix,
       "juniBgpNetworkIpAddrPrefixLen": juniBgpNetworkIpAddrPrefixLen,
       "juniBgpNetworkBackdoor": juniBgpNetworkBackdoor,
       "juniBgpNetworkRowStatus": juniBgpNetworkRowStatus,
       "juniBgpNetworkWeightSpecified": juniBgpNetworkWeightSpecified,
       "juniBgpNetworkWeight": juniBgpNetworkWeight,
       "juniBgpNetworkRouteMap": juniBgpNetworkRouteMap,
       "juniBgpNetworkUnconfiguredAttributes": juniBgpNetworkUnconfiguredAttributes,
       "juniBgpAggregateTable": juniBgpAggregateTable,
       "juniBgpAggregateEntry": juniBgpAggregateEntry,
       "juniBgpAggregateVrfName": juniBgpAggregateVrfName,
       "juniBgpAggregateAfi": juniBgpAggregateAfi,
       "juniBgpAggregateSafi": juniBgpAggregateSafi,
       "juniBgpAggregateIpAddrPrefix": juniBgpAggregateIpAddrPrefix,
       "juniBgpAggregateIpAddrPrefixLen": juniBgpAggregateIpAddrPrefixLen,
       "juniBgpAggregateAsSet": juniBgpAggregateAsSet,
       "juniBgpAggregateSummaryOnly": juniBgpAggregateSummaryOnly,
       "juniBgpAggregateAttributeMap": juniBgpAggregateAttributeMap,
       "juniBgpAggregateAdvertiseMap": juniBgpAggregateAdvertiseMap,
       "juniBgpAggregateRowStatus": juniBgpAggregateRowStatus,
       "juniBgpAggregateSuppressMap": juniBgpAggregateSuppressMap,
       "juniBgpAggregateUnconfiguredAttributes": juniBgpAggregateUnconfiguredAttributes,
       "juniBgpVrfTable": juniBgpVrfTable,
       "juniBgpVrfEntry": juniBgpVrfEntry,
       "juniBgpVrfName": juniBgpVrfName,
       "juniBgpVrfSynchronization": juniBgpVrfSynchronization,
       "juniBgpVrfAutoSummary": juniBgpVrfAutoSummary,
       "juniBgpVrfExternalDistance": juniBgpVrfExternalDistance,
       "juniBgpVrfInternalDistance": juniBgpVrfInternalDistance,
       "juniBgpVrfLocalDistance": juniBgpVrfLocalDistance,
       "juniBgpVrfResetConnectionType": juniBgpVrfResetConnectionType,
       "juniBgpVrfRowStatus": juniBgpVrfRowStatus,
       "juniBgpVrfOperationalState": juniBgpVrfOperationalState,
       "juniBgpVrfAddUnicastRoutesToMulticastView": juniBgpVrfAddUnicastRoutesToMulticastView,
       "juniBgpVrfMaximumPathsEbgp": juniBgpVrfMaximumPathsEbgp,
       "juniBgpVrfMaximumPathsIbgp": juniBgpVrfMaximumPathsIbgp,
       "juniBgpVrfUnconfiguredAttributes": juniBgpVrfUnconfiguredAttributes,
       "juniBgpVrfMaximumPathsEIbgp": juniBgpVrfMaximumPathsEIbgp,
       "juniBgpVrfCarriersCarrierModeEnabled": juniBgpVrfCarriersCarrierModeEnabled,
       "juniBgpAddressFamilyTable": juniBgpAddressFamilyTable,
       "juniBgpAddressFamilyEntry": juniBgpAddressFamilyEntry,
       "juniBgpAddressFamilyVrfName": juniBgpAddressFamilyVrfName,
       "juniBgpAddressFamilyAfi": juniBgpAddressFamilyAfi,
       "juniBgpAddressFamilySafi": juniBgpAddressFamilySafi,
       "juniBgpAddressFamilyDefaultOriginate": juniBgpAddressFamilyDefaultOriginate,
       "juniBgpAddressFamilyRouteFlapDampening": juniBgpAddressFamilyRouteFlapDampening,
       "juniBgpAddressFamilyDampeningSuppressThreshold": juniBgpAddressFamilyDampeningSuppressThreshold,
       "juniBgpAddressFamilyDampeningReuseThreshold": juniBgpAddressFamilyDampeningReuseThreshold,
       "juniBgpAddressFamilyDampeningMaxHoldDownTime": juniBgpAddressFamilyDampeningMaxHoldDownTime,
       "juniBgpAddressFamilyDampeningHalfLifeReachable": juniBgpAddressFamilyDampeningHalfLifeReachable,
       "juniBgpAddressFamilyDampeningHalfLifeUnreachable": juniBgpAddressFamilyDampeningHalfLifeUnreachable,
       "juniBgpAddressFamilyDampeningRouteMapName": juniBgpAddressFamilyDampeningRouteMapName,
       "juniBgpAddressFamilyResetConnectionType": juniBgpAddressFamilyResetConnectionType,
       "juniBgpAddressFamilyRowStatus": juniBgpAddressFamilyRowStatus,
       "juniBgpAddressFamilyOperationalState": juniBgpAddressFamilyOperationalState,
       "juniBgpAddressFamilyUnconfiguredAttributes": juniBgpAddressFamilyUnconfiguredAttributes,
       "juniBgpAddressFamilyExternalDistance": juniBgpAddressFamilyExternalDistance,
       "juniBgpAddressFamilyInternalDistance": juniBgpAddressFamilyInternalDistance,
       "juniBgpAddressFamilyLocalDistance": juniBgpAddressFamilyLocalDistance,
       "juniBgpAddressFamilyDefaultOriginateRouteMap": juniBgpAddressFamilyDefaultOriginateRouteMap,
       "juniBgpAddressFamilyIpIntfProfileNameForMplsHeads": juniBgpAddressFamilyIpIntfProfileNameForMplsHeads,
       "juniBgpAddressFamilyIpIntfProfileNameForMplsTails": juniBgpAddressFamilyIpIntfProfileNameForMplsTails,
       "juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads": juniBgpAddressFamilyIpIntfServiceProfileNameForMplsHeads,
       "juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails": juniBgpAddressFamilyIpIntfServiceProfileNameForMplsTails,
       "juniBgpAddressFamilyCheckVpnNextHops": juniBgpAddressFamilyCheckVpnNextHops,
       "juniBgpAddressFamilyPathSelectionIsDeferred": juniBgpAddressFamilyPathSelectionIsDeferred,
       "juniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards": juniBgpAddressFamilyPreventBgpRoutesFromBeingPushedToLineCards,
       "juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires": juniBgpAddressFamilyTimeUntilPathSelectionDeferTimerExpires,
       "juniBgpStorageGroup": juniBgpStorageGroup,
       "juniBgpStorageInitialHeapSize": juniBgpStorageInitialHeapSize,
       "juniBgpStorageMaxHeapSize": juniBgpStorageMaxHeapSize,
       "juniBgpStorageInitialVrfPoolSize": juniBgpStorageInitialVrfPoolSize,
       "juniBgpStorageMaxVrfPoolSize": juniBgpStorageMaxVrfPoolSize,
       "juniBgpStorageInitialAddressFamilyPoolSize": juniBgpStorageInitialAddressFamilyPoolSize,
       "juniBgpStorageMaxAddressFamilyPoolSize": juniBgpStorageMaxAddressFamilyPoolSize,
       "juniBgpStorageInitialPeerPoolSize": juniBgpStorageInitialPeerPoolSize,
       "juniBgpStorageMaxPeerPoolSize": juniBgpStorageMaxPeerPoolSize,
       "juniBgpStorageInitialPeerAfPoolSize": juniBgpStorageInitialPeerAfPoolSize,
       "juniBgpStorageMaxPeerAfPoolSize": juniBgpStorageMaxPeerAfPoolSize,
       "juniBgpStorageInitialPeerGroupPoolSize": juniBgpStorageInitialPeerGroupPoolSize,
       "juniBgpStorageMaxPeerGroupPoolSize": juniBgpStorageMaxPeerGroupPoolSize,
       "juniBgpStorageInitialPeerGroupAfPoolSize": juniBgpStorageInitialPeerGroupAfPoolSize,
       "juniBgpStorageMaxPeerGroupAfPoolSize": juniBgpStorageMaxPeerGroupAfPoolSize,
       "juniBgpStorageInitialNetworkPoolSize": juniBgpStorageInitialNetworkPoolSize,
       "juniBgpStorageMaxNetworkPoolSize": juniBgpStorageMaxNetworkPoolSize,
       "juniBgpStorageInitialAggregatePoolSize": juniBgpStorageInitialAggregatePoolSize,
       "juniBgpStorageMaxAggregatePoolSize": juniBgpStorageMaxAggregatePoolSize,
       "juniBgpStorageInitialDestinationPoolSize": juniBgpStorageInitialDestinationPoolSize,
       "juniBgpStorageMaxDestinationPoolSize": juniBgpStorageMaxDestinationPoolSize,
       "juniBgpStorageInitialRoutePoolSize": juniBgpStorageInitialRoutePoolSize,
       "juniBgpStorageMaxRoutePoolSize": juniBgpStorageMaxRoutePoolSize,
       "juniBgpStorageInitialAttributesPoolSize": juniBgpStorageInitialAttributesPoolSize,
       "juniBgpStorageMaxAttributesPoolSize": juniBgpStorageMaxAttributesPoolSize,
       "juniBgpStorageInitialRouteFlapHistoryPoolSize": juniBgpStorageInitialRouteFlapHistoryPoolSize,
       "juniBgpStorageMaxRouteFlapHistoryPoolSize": juniBgpStorageMaxRouteFlapHistoryPoolSize,
       "juniBgpStorageInitialNetworkRoutePoolSize": juniBgpStorageInitialNetworkRoutePoolSize,
       "juniBgpStorageMaxNetworkRoutePoolSize": juniBgpStorageMaxNetworkRoutePoolSize,
       "juniBgpStorageInitialRedistributedRoutePoolSize": juniBgpStorageInitialRedistributedRoutePoolSize,
       "juniBgpStorageMaxRedistributedRoutePoolSize": juniBgpStorageMaxRedistributedRoutePoolSize,
       "juniBgpStorageInitialAggregateRoutePoolSize": juniBgpStorageInitialAggregateRoutePoolSize,
       "juniBgpStorageMaxAggregateRoutePoolSize": juniBgpStorageMaxAggregateRoutePoolSize,
       "juniBgpStorageInitialAutoSummaryRoutePoolSize": juniBgpStorageInitialAutoSummaryRoutePoolSize,
       "juniBgpStorageMaxAutoSummaryRoutePoolSize": juniBgpStorageMaxAutoSummaryRoutePoolSize,
       "juniBgpStorageInitialHistoryRoutePoolSize": juniBgpStorageInitialHistoryRoutePoolSize,
       "juniBgpStorageMaxHistoryRoutePoolSize": juniBgpStorageMaxHistoryRoutePoolSize,
       "juniBgpStorageInitialSendQueueEntryPoolSize": juniBgpStorageInitialSendQueueEntryPoolSize,
       "juniBgpStorageMaxSendQueueEntryPoolSize": juniBgpStorageMaxSendQueueEntryPoolSize,
       "juniBgpStorageInitialVpnRoutePoolSize": juniBgpStorageInitialVpnRoutePoolSize,
       "juniBgpStorageMaxVpnRoutePoolSize": juniBgpStorageMaxVpnRoutePoolSize,
       "juniBgpStorageInitialRouteTargetPoolSize": juniBgpStorageInitialRouteTargetPoolSize,
       "juniBgpStorageMaxRouteTargetPoolSize": juniBgpStorageMaxRouteTargetPoolSize,
       "juniBgpRouteExtendedCommunityTable": juniBgpRouteExtendedCommunityTable,
       "juniBgpRouteExtendedCommunityEntry": juniBgpRouteExtendedCommunityEntry,
       "juniBgpRouteExtendedCommunityNumber": juniBgpRouteExtendedCommunityNumber,
       "juniBgpNewRouteTable": juniBgpNewRouteTable,
       "juniBgpNewRouteEntry": juniBgpNewRouteEntry,
       "juniBgpNewRouteVrfName": juniBgpNewRouteVrfName,
       "juniBgpNewRouteAfi": juniBgpNewRouteAfi,
       "juniBgpNewRouteSafi": juniBgpNewRouteSafi,
       "juniBgpNewRouteIpAddrPrefix": juniBgpNewRouteIpAddrPrefix,
       "juniBgpNewRouteIpAddrPrefixLen": juniBgpNewRouteIpAddrPrefixLen,
       "juniBgpNewRouteDistinguisher": juniBgpNewRouteDistinguisher,
       "juniBgpNewRoutePeer": juniBgpNewRoutePeer,
       "juniBgpNewRouteRouteType": juniBgpNewRouteRouteType,
       "juniBgpNewRouteOriginalRd": juniBgpNewRouteOriginalRd,
       "juniBgpNewRouteOriginatorId": juniBgpNewRouteOriginatorId,
       "juniBgpNewRouteAtomicAggregatePresent": juniBgpNewRouteAtomicAggregatePresent,
       "juniBgpNewRouteMedPresent": juniBgpNewRouteMedPresent,
       "juniBgpNewRouteLocalPrefPresent": juniBgpNewRouteLocalPrefPresent,
       "juniBgpNewRouteAggregatorPresent": juniBgpNewRouteAggregatorPresent,
       "juniBgpNewRouteCommunitiesPresent": juniBgpNewRouteCommunitiesPresent,
       "juniBgpNewRouteOriginatorIdPresent": juniBgpNewRouteOriginatorIdPresent,
       "juniBgpNewRouteClusterListPresent": juniBgpNewRouteClusterListPresent,
       "juniBgpNewRouteWeight": juniBgpNewRouteWeight,
       "juniBgpNewRouteOrigin": juniBgpNewRouteOrigin,
       "juniBgpNewRouteASPathSegment": juniBgpNewRouteASPathSegment,
       "juniBgpNewRouteNextHop": juniBgpNewRouteNextHop,
       "juniBgpNewRouteMultiExitDisc": juniBgpNewRouteMultiExitDisc,
       "juniBgpNewRouteLocalPref": juniBgpNewRouteLocalPref,
       "juniBgpNewRouteAtomicAggregate": juniBgpNewRouteAtomicAggregate,
       "juniBgpNewRouteAggregatorAS": juniBgpNewRouteAggregatorAS,
       "juniBgpNewRouteAggregatorAddress": juniBgpNewRouteAggregatorAddress,
       "juniBgpNewRouteBestInIpRouteTable": juniBgpNewRouteBestInIpRouteTable,
       "juniBgpNewRouteUnknown": juniBgpNewRouteUnknown,
       "juniBgpNewRouteExtendedCommunitiesPresent": juniBgpNewRouteExtendedCommunitiesPresent,
       "juniBgpNewRouteValid": juniBgpNewRouteValid,
       "juniBgpNewRouteSuppressedBy": juniBgpNewRouteSuppressedBy,
       "juniBgpNewRouteNextHopReachable": juniBgpNewRouteNextHopReachable,
       "juniBgpNewRouteSynchronizedWithIgp": juniBgpNewRouteSynchronizedWithIgp,
       "juniBgpNewRoutePlaceInIpRouteTable": juniBgpNewRoutePlaceInIpRouteTable,
       "juniBgpNewRouteAdvertiseToExternalPeers": juniBgpNewRouteAdvertiseToExternalPeers,
       "juniBgpNewRouteAdvertiseToInternalPeers": juniBgpNewRouteAdvertiseToInternalPeers,
       "juniBgpNewRouteMplsLabel": juniBgpNewRouteMplsLabel,
       "juniBgpNewRouteNextHopMetric": juniBgpNewRouteNextHopMetric,
       "juniBgpNewRouteMplsInLabel": juniBgpNewRouteMplsInLabel,
       "juniBgpNewRouteMplsOutLabel": juniBgpNewRouteMplsOutLabel,
       "juniBgpNewRouteLeaked": juniBgpNewRouteLeaked,
       "juniBgpNewRouteStale": juniBgpNewRouteStale,
       "juniBgpNewRouteFlapHistoryTable": juniBgpNewRouteFlapHistoryTable,
       "juniBgpNewRouteFlapHistoryEntry": juniBgpNewRouteFlapHistoryEntry,
       "juniBgpNewRouteFlapState": juniBgpNewRouteFlapState,
       "juniBgpNewRouteFlapFigureOfMerit": juniBgpNewRouteFlapFigureOfMerit,
       "juniBgpNewRouteFlapRemainingTime": juniBgpNewRouteFlapRemainingTime,
       "juniBgpNewRouteFlapSuppressThreshold": juniBgpNewRouteFlapSuppressThreshold,
       "juniBgpNewRouteFlapReuseThreshold": juniBgpNewRouteFlapReuseThreshold,
       "juniBgpNewRouteFlapMaxHoldDownTime": juniBgpNewRouteFlapMaxHoldDownTime,
       "juniBgpNewRouteFlapHalfLifeReachable": juniBgpNewRouteFlapHalfLifeReachable,
       "juniBgpNewRouteFlapHalfLifeUnreachable": juniBgpNewRouteFlapHalfLifeUnreachable,
       "juniBgpNewRouteCommunityTable": juniBgpNewRouteCommunityTable,
       "juniBgpNewRouteCommunityEntry": juniBgpNewRouteCommunityEntry,
       "juniBgpNewRouteCommunityNumber": juniBgpNewRouteCommunityNumber,
       "juniBgpNewRouteExtendedCommunityTable": juniBgpNewRouteExtendedCommunityTable,
       "juniBgpNewRouteExtendedCommunityEntry": juniBgpNewRouteExtendedCommunityEntry,
       "juniBgpNewRouteExtendedCommunityNumber": juniBgpNewRouteExtendedCommunityNumber,
       "juniBgpNewRouteClusterIdTable": juniBgpNewRouteClusterIdTable,
       "juniBgpNewRouteClusterIdEntry": juniBgpNewRouteClusterIdEntry,
       "juniBgpNewRouteClusterId": juniBgpNewRouteClusterId,
       "juniBgpFourOctetConfederationPeerTable": juniBgpFourOctetConfederationPeerTable,
       "juniBgpFourOctetConfederationPeerEntry": juniBgpFourOctetConfederationPeerEntry,
       "juniBgpFourOctetConfederationPeerAsNumber": juniBgpFourOctetConfederationPeerAsNumber,
       "juniBgpFourOctetConfederationPeerRowStatus": juniBgpFourOctetConfederationPeerRowStatus,
       "juniBgpPeerDynamicCapabilityTable": juniBgpPeerDynamicCapabilityTable,
       "juniBgpPeerDynamicCapabilityEntry": juniBgpPeerDynamicCapabilityEntry,
       "juniBgpPeerDynamicCapabilityPeerVrfName": juniBgpPeerDynamicCapabilityPeerVrfName,
       "juniBgpPeerDynamicCapabilityPeerRemoteAddr": juniBgpPeerDynamicCapabilityPeerRemoteAddr,
       "juniBgpPeerDynamicCapabilityCode": juniBgpPeerDynamicCapabilityCode,
       "juniBgpPeerDynamicCapabilitySent": juniBgpPeerDynamicCapabilitySent,
       "juniBgpPeerDynamicCapabilityReceived": juniBgpPeerDynamicCapabilityReceived,
       "juniBgpPeerAddressFamilyConditionalAdvTable": juniBgpPeerAddressFamilyConditionalAdvTable,
       "juniBgpPeerAddressFamilyConditionalAdvEntry": juniBgpPeerAddressFamilyConditionalAdvEntry,
       "juniBgpPeerAddressFamilyConditionalAdvAdvertiseMap": juniBgpPeerAddressFamilyConditionalAdvAdvertiseMap,
       "juniBgpPeerAddressFamilyConditionalAdvConditionMap": juniBgpPeerAddressFamilyConditionalAdvConditionMap,
       "juniBgpPeerAddressFamilyConditionalAdvIsExistMap": juniBgpPeerAddressFamilyConditionalAdvIsExistMap,
       "juniBgpPeerAddressFamilyConditionalAdvSequenceNum": juniBgpPeerAddressFamilyConditionalAdvSequenceNum,
       "juniBgpPeerAddressFamilyConditionalAdvStatus": juniBgpPeerAddressFamilyConditionalAdvStatus,
       "juniBgpPeerAddressFamilyConditionalAdvRowStatus": juniBgpPeerAddressFamilyConditionalAdvRowStatus,
       "juniBgpPeerGroupAddressFamilyConditionalAdvTable": juniBgpPeerGroupAddressFamilyConditionalAdvTable,
       "juniBgpPeerGroupAddressFamilyConditionalAdvEntry": juniBgpPeerGroupAddressFamilyConditionalAdvEntry,
       "juniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap": juniBgpPeerGroupAddressFamilyConditionalAdvAdvertiseMap,
       "juniBgpPeerGroupAddressFamilyConditionalAdvConditionMap": juniBgpPeerGroupAddressFamilyConditionalAdvConditionMap,
       "juniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap": juniBgpPeerGroupAddressFamilyConditionalAdvIsExistMap,
       "juniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum": juniBgpPeerGroupAddressFamilyConditionalAdvSequenceNum,
       "juniBgpPeerGroupAddressFamilyConditionalAdvStatus": juniBgpPeerGroupAddressFamilyConditionalAdvStatus,
       "juniBgpPeerGroupAddressFamilyConditionalAdvRowStatus": juniBgpPeerGroupAddressFamilyConditionalAdvRowStatus,
       "juniBgpConformance": juniBgpConformance,
       "juniBgpCompliances": juniBgpCompliances,
       "juniBgpCompliance": juniBgpCompliance,
       "juniBgpCompliance2": juniBgpCompliance2,
       "juniBgpCompliance3": juniBgpCompliance3,
       "juniBgpCompliance4": juniBgpCompliance4,
       "juniBgpCompliance5": juniBgpCompliance5,
       "juniBgpCompliance6": juniBgpCompliance6,
       "juniBgpCompliance7": juniBgpCompliance7,
       "juniBgpCompliance8": juniBgpCompliance8,
       "juniBgpCompliance9": juniBgpCompliance9,
       "juniBgpCompliance10": juniBgpCompliance10,
       "juniBgpCompliance11": juniBgpCompliance11,
       "juniBgpCompliance12": juniBgpCompliance12,
       "juniBgpCompliance13": juniBgpCompliance13,
       "juniBgpCompliance14": juniBgpCompliance14,
       "juniBgpCompliance15": juniBgpCompliance15,
       "juniBgpCompliance16": juniBgpCompliance16,
       "juniBgpConfGroups": juniBgpConfGroups,
       "juniBgpGeneralConfGroup": juniBgpGeneralConfGroup,
       "juniBgpStatisticsConfGroup": juniBgpStatisticsConfGroup,
       "juniBgpConfederationPeerConfGroup": juniBgpConfederationPeerConfGroup,
       "juniBgpPeerConfGroup": juniBgpPeerConfGroup,
       "juniBgpAfiSafiPeerConfGroup": juniBgpAfiSafiPeerConfGroup,
       "juniBgpPeerAddressFamilyConfGroup": juniBgpPeerAddressFamilyConfGroup,
       "juniBgpPeerGroupConfGroup": juniBgpPeerGroupConfGroup,
       "juniBgpPeerGroupAddressFamilyConfGroup": juniBgpPeerGroupAddressFamilyConfGroup,
       "juniBgpRouteConfGroup": juniBgpRouteConfGroup,
       "juniBgpNetworkConfGroup": juniBgpNetworkConfGroup,
       "juniBgpAggregateConfGroup": juniBgpAggregateConfGroup,
       "juniBgpVrfConfGroup": juniBgpVrfConfGroup,
       "juniBgpAddressFamilyConfGroup": juniBgpAddressFamilyConfGroup,
       "juniBgpStorageConfGroup": juniBgpStorageConfGroup,
       "juniBgpGeneralConfGroup2": juniBgpGeneralConfGroup2,
       "juniBgpNewRouteConfGroup": juniBgpNewRouteConfGroup,
       "juniBgpPeerConfGroup2": juniBgpPeerConfGroup2,
       "juniBgpPeerGroupConfGroup2": juniBgpPeerGroupConfGroup2,
       "juniBgpVrfConfGroup2": juniBgpVrfConfGroup2,
       "juniBgpGeneralConfGroup3": juniBgpGeneralConfGroup3,
       "juniBgpStorageConfGroup2": juniBgpStorageConfGroup2,
       "juniBgpPeerConfGroup3": juniBgpPeerConfGroup3,
       "juniBgpPeerAddressFamilyConfGroup2": juniBgpPeerAddressFamilyConfGroup2,
       "juniBgpPeerGroupConfGroup3": juniBgpPeerGroupConfGroup3,
       "juniBgpPeerGroupAddressFamilyConfGroup2": juniBgpPeerGroupAddressFamilyConfGroup2,
       "juniBgpNetworkConfGroup2": juniBgpNetworkConfGroup2,
       "juniBgpAggregateConfGroup2": juniBgpAggregateConfGroup2,
       "juniBgpVrfConfGroup3": juniBgpVrfConfGroup3,
       "juniBgpAddressFamilyConfGroup2": juniBgpAddressFamilyConfGroup2,
       "juniBgpGeneralConfGroup4": juniBgpGeneralConfGroup4,
       "juniBgpFourOctetConfederationPeerConfGroup": juniBgpFourOctetConfederationPeerConfGroup,
       "juniBgpPeerConfGroup4": juniBgpPeerConfGroup4,
       "juniBgpPeerAddressFamilyConfGroup3": juniBgpPeerAddressFamilyConfGroup3,
       "juniBgpPeerGroupConfGroup4": juniBgpPeerGroupConfGroup4,
       "juniBgpPeerGroupAddressFamilyConfGroup3": juniBgpPeerGroupAddressFamilyConfGroup3,
       "juniBgpVrfConfGroup4": juniBgpVrfConfGroup4,
       "juniBgpDeprecatedGroup": juniBgpDeprecatedGroup,
       "juniBgpNewRouteConfGroup2": juniBgpNewRouteConfGroup2,
       "juniBgpGeneralConfGroup5": juniBgpGeneralConfGroup5,
       "juniBgpPeerConfGroup5": juniBgpPeerConfGroup5,
       "juniBgpPeerGroupConfGroup5": juniBgpPeerGroupConfGroup5,
       "juniBgpVrfConfGroup5": juniBgpVrfConfGroup5,
       "juniBgpAddressFamilyConfGroup3": juniBgpAddressFamilyConfGroup3,
       "juniBgpStorageConfGroup3": juniBgpStorageConfGroup3,
       "juniBgpNewRouteConfGroup3": juniBgpNewRouteConfGroup3,
       "juniBgpPeerAddressFamilyConfGroup4": juniBgpPeerAddressFamilyConfGroup4,
       "juniBgpPeerGroupAddressFamilyConfGroup4": juniBgpPeerGroupAddressFamilyConfGroup4,
       "juniBgpVrfConfGroup6": juniBgpVrfConfGroup6,
       "juniBgpAddressFamilyConfGroup4": juniBgpAddressFamilyConfGroup4,
       "juniBgpPeerAddressFamilyConfGroup5": juniBgpPeerAddressFamilyConfGroup5,
       "juniBgpPeerGroupAddressFamilyConfGroup5": juniBgpPeerGroupAddressFamilyConfGroup5,
       "juniBgpAddressFamilyConfGroup5": juniBgpAddressFamilyConfGroup5,
       "juniBgpPeerConfGroup6": juniBgpPeerConfGroup6,
       "juniBgpPeerGroupConfGroup6": juniBgpPeerGroupConfGroup6,
       "juniBgpPeerDynamicCapabilityConfGroup": juniBgpPeerDynamicCapabilityConfGroup,
       "juniBgpGeneralConfGroup6": juniBgpGeneralConfGroup6,
       "juniBgpPeerConfGroup7": juniBgpPeerConfGroup7,
       "juniBgpPeerAddressFamilyConfGroup6": juniBgpPeerAddressFamilyConfGroup6,
       "juniBgpPeerGroupConfGroup7": juniBgpPeerGroupConfGroup7,
       "juniBgpNewRouteConfGroup4": juniBgpNewRouteConfGroup4,
       "juniBgpAddressFamilyConfGroup6": juniBgpAddressFamilyConfGroup6,
       "juniBgpVrfConfGroup7": juniBgpVrfConfGroup7,
       "juniBgpPeerAddressFamilyConfGroup7": juniBgpPeerAddressFamilyConfGroup7,
       "juniBgpPeerGroupAddressFamilyConfGroup6": juniBgpPeerGroupAddressFamilyConfGroup6,
       "juniBgpAddressFamilyConfGroup7": juniBgpAddressFamilyConfGroup7,
       "juniBgpPeerConfGroup8": juniBgpPeerConfGroup8,
       "juniBgpPeerGroupConfGroup8": juniBgpPeerGroupConfGroup8,
       "juniBgpPeerConfGroup9": juniBgpPeerConfGroup9,
       "juniBgpPeerGroupConfGroup9": juniBgpPeerGroupConfGroup9,
       "juniBgpPeerAddressFamilyConditionalAdvConfGroup": juniBgpPeerAddressFamilyConditionalAdvConfGroup,
       "juniBgpPeerGroupAddressFamilyConditionalAdvConfGroup": juniBgpPeerGroupAddressFamilyConditionalAdvConfGroup}
)
