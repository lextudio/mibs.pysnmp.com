# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:51 2024
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

(jnxMobileGatewayMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMobileGatewayMibRoot")

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

jnxMobileGatewayPgwSMIPPoolMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5)
)
jnxMobileGatewayPgwSMIPPoolMib.setRevisions(
        ("2011-01-13 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgSMIPPoolNotifications_ObjectIdentity = ObjectIdentity
jnxMbgSMIPPoolNotifications = _JnxMbgSMIPPoolNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0)
)
_JnxMbgSMIPPoolObjects_ObjectIdentity = ObjectIdentity
jnxMbgSMIPPoolObjects = _JnxMbgSMIPPoolObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1)
)
_JnxMbgSMIPPoolTable_Object = MibTable
jnxMbgSMIPPoolTable = _JnxMbgSMIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1)
)
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolTable.setStatus("deprecated")
_JnxMbgSMIPPoolEntry_Object = MibTableRow
jnxMbgSMIPPoolEntry = _JnxMbgSMIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1)
)
jnxMbgSMIPPoolEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolLogicalSystem"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolRoutingInstance"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolName"),
)
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolEntry.setStatus("deprecated")


class _JnxMbgSMIPPoolName_Type(DisplayString):
    """Custom type jnxMbgSMIPPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxMbgSMIPPoolName_Type.__name__ = "DisplayString"
_JnxMbgSMIPPoolName_Object = MibTableColumn
jnxMbgSMIPPoolName = _JnxMbgSMIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1, 1),
    _JnxMbgSMIPPoolName_Type()
)
jnxMbgSMIPPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolName.setStatus("deprecated")


class _JnxMbgSMIPPoolLogicalSystem_Type(DisplayString):
    """Custom type jnxMbgSMIPPoolLogicalSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxMbgSMIPPoolLogicalSystem_Type.__name__ = "DisplayString"
_JnxMbgSMIPPoolLogicalSystem_Object = MibTableColumn
jnxMbgSMIPPoolLogicalSystem = _JnxMbgSMIPPoolLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1, 2),
    _JnxMbgSMIPPoolLogicalSystem_Type()
)
jnxMbgSMIPPoolLogicalSystem.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolLogicalSystem.setStatus("deprecated")


class _JnxMbgSMIPPoolRoutingInstance_Type(DisplayString):
    """Custom type jnxMbgSMIPPoolRoutingInstance based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_JnxMbgSMIPPoolRoutingInstance_Type.__name__ = "DisplayString"
_JnxMbgSMIPPoolRoutingInstance_Object = MibTableColumn
jnxMbgSMIPPoolRoutingInstance = _JnxMbgSMIPPoolRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1, 3),
    _JnxMbgSMIPPoolRoutingInstance_Type()
)
jnxMbgSMIPPoolRoutingInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolRoutingInstance.setStatus("deprecated")
_JnxMbgSMIPPoolType_Type = InetAddressType
_JnxMbgSMIPPoolType_Object = MibTableColumn
jnxMbgSMIPPoolType = _JnxMbgSMIPPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1, 4),
    _JnxMbgSMIPPoolType_Type()
)
jnxMbgSMIPPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolType.setStatus("deprecated")
_JnxMbgSMIPPoolFree_Type = Unsigned32
_JnxMbgSMIPPoolFree_Object = MibTableColumn
jnxMbgSMIPPoolFree = _JnxMbgSMIPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1, 5),
    _JnxMbgSMIPPoolFree_Type()
)
jnxMbgSMIPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolFree.setStatus("deprecated")
_JnxMbgSMIPPoolInUse_Type = Unsigned32
_JnxMbgSMIPPoolInUse_Object = MibTableColumn
jnxMbgSMIPPoolInUse = _JnxMbgSMIPPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1, 6),
    _JnxMbgSMIPPoolInUse_Type()
)
jnxMbgSMIPPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolInUse.setStatus("deprecated")
_JnxMbgSMIPPoolUtil_Type = Unsigned32
_JnxMbgSMIPPoolUtil_Object = MibTableColumn
jnxMbgSMIPPoolUtil = _JnxMbgSMIPPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 1, 1, 7),
    _JnxMbgSMIPPoolUtil_Type()
)
jnxMbgSMIPPoolUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolUtil.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolUtil.setUnits("percent")
_JnxMbgSMIPPoolNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgSMIPPoolNotificationVars = _JnxMbgSMIPPoolNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2)
)
_JnxMbgSMIPPoolThresholdPoolName_Type = DisplayString
_JnxMbgSMIPPoolThresholdPoolName_Object = MibScalar
jnxMbgSMIPPoolThresholdPoolName = _JnxMbgSMIPPoolThresholdPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 1),
    _JnxMbgSMIPPoolThresholdPoolName_Type()
)
jnxMbgSMIPPoolThresholdPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolThresholdPoolName.setStatus("current")
_JnxMbgSMIPPoolThresholdLSName_Type = DisplayString
_JnxMbgSMIPPoolThresholdLSName_Object = MibScalar
jnxMbgSMIPPoolThresholdLSName = _JnxMbgSMIPPoolThresholdLSName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 2),
    _JnxMbgSMIPPoolThresholdLSName_Type()
)
jnxMbgSMIPPoolThresholdLSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolThresholdLSName.setStatus("current")
_JnxMbgSMIPPoolThresholdRIName_Type = DisplayString
_JnxMbgSMIPPoolThresholdRIName_Object = MibScalar
jnxMbgSMIPPoolThresholdRIName = _JnxMbgSMIPPoolThresholdRIName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 3),
    _JnxMbgSMIPPoolThresholdRIName_Type()
)
jnxMbgSMIPPoolThresholdRIName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolThresholdRIName.setStatus("current")
_JnxMbgSMIPPoolConfiguredThreshold_Type = Unsigned32
_JnxMbgSMIPPoolConfiguredThreshold_Object = MibScalar
jnxMbgSMIPPoolConfiguredThreshold = _JnxMbgSMIPPoolConfiguredThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 4),
    _JnxMbgSMIPPoolConfiguredThreshold_Type()
)
jnxMbgSMIPPoolConfiguredThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolConfiguredThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolConfiguredThreshold.setUnits("percent")
_JnxMbgSMIPPoolCurrentThreshold_Type = Unsigned32
_JnxMbgSMIPPoolCurrentThreshold_Object = MibScalar
jnxMbgSMIPPoolCurrentThreshold = _JnxMbgSMIPPoolCurrentThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 5),
    _JnxMbgSMIPPoolCurrentThreshold_Type()
)
jnxMbgSMIPPoolCurrentThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolCurrentThreshold.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolCurrentThreshold.setUnits("percent")
_JnxMbgSMIPPoolMMPoolName_Type = DisplayString
_JnxMbgSMIPPoolMMPoolName_Object = MibScalar
jnxMbgSMIPPoolMMPoolName = _JnxMbgSMIPPoolMMPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 6),
    _JnxMbgSMIPPoolMMPoolName_Type()
)
jnxMbgSMIPPoolMMPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolMMPoolName.setStatus("current")
_JnxMbgSMIPPoolMMLSName_Type = DisplayString
_JnxMbgSMIPPoolMMLSName_Object = MibScalar
jnxMbgSMIPPoolMMLSName = _JnxMbgSMIPPoolMMLSName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 7),
    _JnxMbgSMIPPoolMMLSName_Type()
)
jnxMbgSMIPPoolMMLSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolMMLSName.setStatus("current")
_JnxMbgSMIPPoolMMRIName_Type = DisplayString
_JnxMbgSMIPPoolMMRIName_Object = MibScalar
jnxMbgSMIPPoolMMRIName = _JnxMbgSMIPPoolMMRIName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 8),
    _JnxMbgSMIPPoolMMRIName_Type()
)
jnxMbgSMIPPoolMMRIName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolMMRIName.setStatus("current")
_JnxMbgSMIPPoolPrevMMState_Type = DisplayString
_JnxMbgSMIPPoolPrevMMState_Object = MibScalar
jnxMbgSMIPPoolPrevMMState = _JnxMbgSMIPPoolPrevMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 9),
    _JnxMbgSMIPPoolPrevMMState_Type()
)
jnxMbgSMIPPoolPrevMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolPrevMMState.setStatus("current")
_JnxMbgSMIPPoolNewMMState_Type = DisplayString
_JnxMbgSMIPPoolNewMMState_Object = MibScalar
jnxMbgSMIPPoolNewMMState = _JnxMbgSMIPPoolNewMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 10),
    _JnxMbgSMIPPoolNewMMState_Type()
)
jnxMbgSMIPPoolNewMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolNewMMState.setStatus("current")
_JnxMbgSMIPRangeHiThresRangeName_Type = DisplayString
_JnxMbgSMIPRangeHiThresRangeName_Object = MibScalar
jnxMbgSMIPRangeHiThresRangeName = _JnxMbgSMIPRangeHiThresRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 11),
    _JnxMbgSMIPRangeHiThresRangeName_Type()
)
jnxMbgSMIPRangeHiThresRangeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiThresRangeName.setStatus("current")
_JnxMbgSMIPRangeHiThresPoolName_Type = DisplayString
_JnxMbgSMIPRangeHiThresPoolName_Object = MibScalar
jnxMbgSMIPRangeHiThresPoolName = _JnxMbgSMIPRangeHiThresPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 12),
    _JnxMbgSMIPRangeHiThresPoolName_Type()
)
jnxMbgSMIPRangeHiThresPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiThresPoolName.setStatus("current")
_JnxMbgSMIPRangeHiLSName_Type = DisplayString
_JnxMbgSMIPRangeHiLSName_Object = MibScalar
jnxMbgSMIPRangeHiLSName = _JnxMbgSMIPRangeHiLSName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 13),
    _JnxMbgSMIPRangeHiLSName_Type()
)
jnxMbgSMIPRangeHiLSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiLSName.setStatus("current")
_JnxMbgSMIPRangeHiRIName_Type = DisplayString
_JnxMbgSMIPRangeHiRIName_Object = MibScalar
jnxMbgSMIPRangeHiRIName = _JnxMbgSMIPRangeHiRIName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 14),
    _JnxMbgSMIPRangeHiRIName_Type()
)
jnxMbgSMIPRangeHiRIName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiRIName.setStatus("current")
_JnxMbgSMIPRangeHiCfgThres_Type = Unsigned32
_JnxMbgSMIPRangeHiCfgThres_Object = MibScalar
jnxMbgSMIPRangeHiCfgThres = _JnxMbgSMIPRangeHiCfgThres_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 15),
    _JnxMbgSMIPRangeHiCfgThres_Type()
)
jnxMbgSMIPRangeHiCfgThres.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiCfgThres.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiCfgThres.setUnits("percent")
_JnxMbgSMIPRangeHiCurrUtil_Type = Unsigned32
_JnxMbgSMIPRangeHiCurrUtil_Object = MibScalar
jnxMbgSMIPRangeHiCurrUtil = _JnxMbgSMIPRangeHiCurrUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 16),
    _JnxMbgSMIPRangeHiCurrUtil_Type()
)
jnxMbgSMIPRangeHiCurrUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiCurrUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHiCurrUtil.setUnits("percent")
_JnxMbgSMIPRangeLowThresRangeName_Type = DisplayString
_JnxMbgSMIPRangeLowThresRangeName_Object = MibScalar
jnxMbgSMIPRangeLowThresRangeName = _JnxMbgSMIPRangeLowThresRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 17),
    _JnxMbgSMIPRangeLowThresRangeName_Type()
)
jnxMbgSMIPRangeLowThresRangeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowThresRangeName.setStatus("current")
_JnxMbgSMIPRangeLowThresPoolName_Type = DisplayString
_JnxMbgSMIPRangeLowThresPoolName_Object = MibScalar
jnxMbgSMIPRangeLowThresPoolName = _JnxMbgSMIPRangeLowThresPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 18),
    _JnxMbgSMIPRangeLowThresPoolName_Type()
)
jnxMbgSMIPRangeLowThresPoolName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowThresPoolName.setStatus("current")
_JnxMbgSMIPRangeLowLSName_Type = DisplayString
_JnxMbgSMIPRangeLowLSName_Object = MibScalar
jnxMbgSMIPRangeLowLSName = _JnxMbgSMIPRangeLowLSName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 19),
    _JnxMbgSMIPRangeLowLSName_Type()
)
jnxMbgSMIPRangeLowLSName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowLSName.setStatus("current")
_JnxMbgSMIPRangeLowRIName_Type = DisplayString
_JnxMbgSMIPRangeLowRIName_Object = MibScalar
jnxMbgSMIPRangeLowRIName = _JnxMbgSMIPRangeLowRIName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 20),
    _JnxMbgSMIPRangeLowRIName_Type()
)
jnxMbgSMIPRangeLowRIName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowRIName.setStatus("current")
_JnxMbgSMIPRangeLowCfgThres_Type = Unsigned32
_JnxMbgSMIPRangeLowCfgThres_Object = MibScalar
jnxMbgSMIPRangeLowCfgThres = _JnxMbgSMIPRangeLowCfgThres_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 21),
    _JnxMbgSMIPRangeLowCfgThres_Type()
)
jnxMbgSMIPRangeLowCfgThres.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowCfgThres.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowCfgThres.setUnits("percent")
_JnxMbgSMIPRangeLowCurrUtil_Type = Unsigned32
_JnxMbgSMIPRangeLowCurrUtil_Object = MibScalar
jnxMbgSMIPRangeLowCurrUtil = _JnxMbgSMIPRangeLowCurrUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 22),
    _JnxMbgSMIPRangeLowCurrUtil_Type()
)
jnxMbgSMIPRangeLowCurrUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowCurrUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowCurrUtil.setUnits("percent")
_JnxMbgSMIPPoolHTCfgThres_Type = Unsigned32
_JnxMbgSMIPPoolHTCfgThres_Object = MibScalar
jnxMbgSMIPPoolHTCfgThres = _JnxMbgSMIPPoolHTCfgThres_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 23),
    _JnxMbgSMIPPoolHTCfgThres_Type()
)
jnxMbgSMIPPoolHTCfgThres.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolHTCfgThres.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolHTCfgThres.setUnits("percent")
_JnxMbgSMIPPoolCurrUtil_Type = Unsigned32
_JnxMbgSMIPPoolCurrUtil_Object = MibScalar
jnxMbgSMIPPoolCurrUtil = _JnxMbgSMIPPoolCurrUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 24),
    _JnxMbgSMIPPoolCurrUtil_Type()
)
jnxMbgSMIPPoolCurrUtil.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolCurrUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolCurrUtil.setUnits("percent")
_JnxMbgSMIPPoolLTCfgThres_Type = Unsigned32
_JnxMbgSMIPPoolLTCfgThres_Object = MibScalar
jnxMbgSMIPPoolLTCfgThres = _JnxMbgSMIPPoolLTCfgThres_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 2, 25),
    _JnxMbgSMIPPoolLTCfgThres_Type()
)
jnxMbgSMIPPoolLTCfgThres.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolLTCfgThres.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolLTCfgThres.setUnits("percent")
_JnxMbgIPPoolTable_Object = MibTable
jnxMbgIPPoolTable = _JnxMbgIPPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3)
)
if mibBuilder.loadTexts:
    jnxMbgIPPoolTable.setStatus("current")
_JnxMbgIPPoolEntry_Object = MibTableRow
jnxMbgIPPoolEntry = _JnxMbgIPPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1)
)
jnxMbgIPPoolEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgIPPoolId"),
)
if mibBuilder.loadTexts:
    jnxMbgIPPoolEntry.setStatus("current")
_JnxMbgIPPoolId_Type = Unsigned32
_JnxMbgIPPoolId_Object = MibTableColumn
jnxMbgIPPoolId = _JnxMbgIPPoolId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 1),
    _JnxMbgIPPoolId_Type()
)
jnxMbgIPPoolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgIPPoolId.setStatus("current")
_JnxMbgIPPoolLogicalSystem_Type = DisplayString
_JnxMbgIPPoolLogicalSystem_Object = MibTableColumn
jnxMbgIPPoolLogicalSystem = _JnxMbgIPPoolLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 2),
    _JnxMbgIPPoolLogicalSystem_Type()
)
jnxMbgIPPoolLogicalSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolLogicalSystem.setStatus("current")
_JnxMbgIPPoolRoutingInstance_Type = DisplayString
_JnxMbgIPPoolRoutingInstance_Object = MibTableColumn
jnxMbgIPPoolRoutingInstance = _JnxMbgIPPoolRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 3),
    _JnxMbgIPPoolRoutingInstance_Type()
)
jnxMbgIPPoolRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolRoutingInstance.setStatus("current")
_JnxMbgIPPoolName_Type = DisplayString
_JnxMbgIPPoolName_Object = MibTableColumn
jnxMbgIPPoolName = _JnxMbgIPPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 4),
    _JnxMbgIPPoolName_Type()
)
jnxMbgIPPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolName.setStatus("current")
_JnxMbgIPPoolType_Type = InetAddressType
_JnxMbgIPPoolType_Object = MibTableColumn
jnxMbgIPPoolType = _JnxMbgIPPoolType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 5),
    _JnxMbgIPPoolType_Type()
)
jnxMbgIPPoolType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolType.setStatus("current")
_JnxMbgIPPoolFree_Type = Gauge32
_JnxMbgIPPoolFree_Object = MibTableColumn
jnxMbgIPPoolFree = _JnxMbgIPPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 6),
    _JnxMbgIPPoolFree_Type()
)
jnxMbgIPPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolFree.setStatus("current")
_JnxMbgIPPoolInUse_Type = Gauge32
_JnxMbgIPPoolInUse_Object = MibTableColumn
jnxMbgIPPoolInUse = _JnxMbgIPPoolInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 7),
    _JnxMbgIPPoolInUse_Type()
)
jnxMbgIPPoolInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolInUse.setStatus("current")
_JnxMbgIPPoolUtil_Type = Gauge32
_JnxMbgIPPoolUtil_Object = MibTableColumn
jnxMbgIPPoolUtil = _JnxMbgIPPoolUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 3, 1, 8),
    _JnxMbgIPPoolUtil_Type()
)
jnxMbgIPPoolUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgIPPoolUtil.setUnits("percent")
_JnxMbgIPPoolRangeTable_Object = MibTable
jnxMbgIPPoolRangeTable = _JnxMbgIPPoolRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeTable.setStatus("current")
_JnxMbgIPPoolRangeEntry_Object = MibTableRow
jnxMbgIPPoolRangeEntry = _JnxMbgIPPoolRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 4, 1)
)
jnxMbgIPPoolRangeEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgIPPoolId"),
    (0, "JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgIPPoolRangeName"),
)
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeEntry.setStatus("current")


class _JnxMbgIPPoolRangeName_Type(DisplayString):
    """Custom type jnxMbgIPPoolRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_JnxMbgIPPoolRangeName_Type.__name__ = "DisplayString"
_JnxMbgIPPoolRangeName_Object = MibTableColumn
jnxMbgIPPoolRangeName = _JnxMbgIPPoolRangeName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 4, 1, 1),
    _JnxMbgIPPoolRangeName_Type()
)
jnxMbgIPPoolRangeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeName.setStatus("current")
_JnxMbgIPPoolRangeType_Type = InetAddressType
_JnxMbgIPPoolRangeType_Object = MibTableColumn
jnxMbgIPPoolRangeType = _JnxMbgIPPoolRangeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 4, 1, 2),
    _JnxMbgIPPoolRangeType_Type()
)
jnxMbgIPPoolRangeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeType.setStatus("current")
_JnxMbgIPPoolRangeFree_Type = Gauge32
_JnxMbgIPPoolRangeFree_Object = MibTableColumn
jnxMbgIPPoolRangeFree = _JnxMbgIPPoolRangeFree_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 4, 1, 3),
    _JnxMbgIPPoolRangeFree_Type()
)
jnxMbgIPPoolRangeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeFree.setStatus("current")
_JnxMbgIPPoolRangeInUse_Type = Gauge32
_JnxMbgIPPoolRangeInUse_Object = MibTableColumn
jnxMbgIPPoolRangeInUse = _JnxMbgIPPoolRangeInUse_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 4, 1, 4),
    _JnxMbgIPPoolRangeInUse_Type()
)
jnxMbgIPPoolRangeInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeInUse.setStatus("current")
_JnxMbgIPPoolRangeUtil_Type = Gauge32
_JnxMbgIPPoolRangeUtil_Object = MibTableColumn
jnxMbgIPPoolRangeUtil = _JnxMbgIPPoolRangeUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 1, 4, 1, 5),
    _JnxMbgIPPoolRangeUtil_Type()
)
jnxMbgIPPoolRangeUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeUtil.setStatus("current")
if mibBuilder.loadTexts:
    jnxMbgIPPoolRangeUtil.setUnits("percent")

# Managed Objects groups


# Notification objects

jnxMbgSMIPPoolThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0, 1)
)
jnxMbgSMIPPoolThresholdExceeded.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdPoolName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdLSName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdRIName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolConfiguredThreshold"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolCurrentThreshold"))
)
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolThresholdExceeded.setStatus(
        "deprecated"
    )

jnxMbgSMIPPoolMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0, 2)
)
jnxMbgSMIPPoolMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolMMPoolName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolMMLSName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolMMRIName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolPrevMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolMMStateChange.setStatus(
        "current"
    )

jnxMbgSMIPRangeHighThresExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0, 3)
)
jnxMbgSMIPRangeHighThresExcd.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeHiThresRangeName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeHiThresPoolName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeHiLSName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeHiRIName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeHiCfgThres"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeHiCurrUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeHighThresExcd.setStatus(
        "current"
    )

jnxMbgSMIPRangeLowThresRchd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0, 4)
)
jnxMbgSMIPRangeLowThresRchd.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeLowThresRangeName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeLowThresPoolName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeLowLSName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeLowRIName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeLowCfgThres"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPRangeLowCurrUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgSMIPRangeLowThresRchd.setStatus(
        "current"
    )

jnxMbgSMIPPoolHighThresExcd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0, 5)
)
jnxMbgSMIPPoolHighThresExcd.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdPoolName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdLSName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdRIName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolHTCfgThres"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolCurrUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolHighThresExcd.setStatus(
        "current"
    )

jnxMbgSMIPPoolLowThresRchd = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0, 6)
)
jnxMbgSMIPPoolLowThresRchd.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdPoolName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdLSName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolThresholdRIName"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolLTCfgThres"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgSMIPPoolCurrUtil"))
)
if mibBuilder.loadTexts:
    jnxMbgSMIPPoolLowThresRchd.setStatus(
        "current"
    )

jnxMbgIPPoolExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 5, 0, 7)
)
jnxMbgIPPoolExhausted.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgIPPoolLogicalSystem"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgIPPoolRoutingInstance"),
        ("JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB", "jnxMbgIPPoolName"))
)
if mibBuilder.loadTexts:
    jnxMbgIPPoolExhausted.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-SM-IP-POOL-MIB",
    **{"jnxMobileGatewayPgwSMIPPoolMib": jnxMobileGatewayPgwSMIPPoolMib,
       "jnxMbgSMIPPoolNotifications": jnxMbgSMIPPoolNotifications,
       "jnxMbgSMIPPoolThresholdExceeded": jnxMbgSMIPPoolThresholdExceeded,
       "jnxMbgSMIPPoolMMStateChange": jnxMbgSMIPPoolMMStateChange,
       "jnxMbgSMIPRangeHighThresExcd": jnxMbgSMIPRangeHighThresExcd,
       "jnxMbgSMIPRangeLowThresRchd": jnxMbgSMIPRangeLowThresRchd,
       "jnxMbgSMIPPoolHighThresExcd": jnxMbgSMIPPoolHighThresExcd,
       "jnxMbgSMIPPoolLowThresRchd": jnxMbgSMIPPoolLowThresRchd,
       "jnxMbgIPPoolExhausted": jnxMbgIPPoolExhausted,
       "jnxMbgSMIPPoolObjects": jnxMbgSMIPPoolObjects,
       "jnxMbgSMIPPoolTable": jnxMbgSMIPPoolTable,
       "jnxMbgSMIPPoolEntry": jnxMbgSMIPPoolEntry,
       "jnxMbgSMIPPoolName": jnxMbgSMIPPoolName,
       "jnxMbgSMIPPoolLogicalSystem": jnxMbgSMIPPoolLogicalSystem,
       "jnxMbgSMIPPoolRoutingInstance": jnxMbgSMIPPoolRoutingInstance,
       "jnxMbgSMIPPoolType": jnxMbgSMIPPoolType,
       "jnxMbgSMIPPoolFree": jnxMbgSMIPPoolFree,
       "jnxMbgSMIPPoolInUse": jnxMbgSMIPPoolInUse,
       "jnxMbgSMIPPoolUtil": jnxMbgSMIPPoolUtil,
       "jnxMbgSMIPPoolNotificationVars": jnxMbgSMIPPoolNotificationVars,
       "jnxMbgSMIPPoolThresholdPoolName": jnxMbgSMIPPoolThresholdPoolName,
       "jnxMbgSMIPPoolThresholdLSName": jnxMbgSMIPPoolThresholdLSName,
       "jnxMbgSMIPPoolThresholdRIName": jnxMbgSMIPPoolThresholdRIName,
       "jnxMbgSMIPPoolConfiguredThreshold": jnxMbgSMIPPoolConfiguredThreshold,
       "jnxMbgSMIPPoolCurrentThreshold": jnxMbgSMIPPoolCurrentThreshold,
       "jnxMbgSMIPPoolMMPoolName": jnxMbgSMIPPoolMMPoolName,
       "jnxMbgSMIPPoolMMLSName": jnxMbgSMIPPoolMMLSName,
       "jnxMbgSMIPPoolMMRIName": jnxMbgSMIPPoolMMRIName,
       "jnxMbgSMIPPoolPrevMMState": jnxMbgSMIPPoolPrevMMState,
       "jnxMbgSMIPPoolNewMMState": jnxMbgSMIPPoolNewMMState,
       "jnxMbgSMIPRangeHiThresRangeName": jnxMbgSMIPRangeHiThresRangeName,
       "jnxMbgSMIPRangeHiThresPoolName": jnxMbgSMIPRangeHiThresPoolName,
       "jnxMbgSMIPRangeHiLSName": jnxMbgSMIPRangeHiLSName,
       "jnxMbgSMIPRangeHiRIName": jnxMbgSMIPRangeHiRIName,
       "jnxMbgSMIPRangeHiCfgThres": jnxMbgSMIPRangeHiCfgThres,
       "jnxMbgSMIPRangeHiCurrUtil": jnxMbgSMIPRangeHiCurrUtil,
       "jnxMbgSMIPRangeLowThresRangeName": jnxMbgSMIPRangeLowThresRangeName,
       "jnxMbgSMIPRangeLowThresPoolName": jnxMbgSMIPRangeLowThresPoolName,
       "jnxMbgSMIPRangeLowLSName": jnxMbgSMIPRangeLowLSName,
       "jnxMbgSMIPRangeLowRIName": jnxMbgSMIPRangeLowRIName,
       "jnxMbgSMIPRangeLowCfgThres": jnxMbgSMIPRangeLowCfgThres,
       "jnxMbgSMIPRangeLowCurrUtil": jnxMbgSMIPRangeLowCurrUtil,
       "jnxMbgSMIPPoolHTCfgThres": jnxMbgSMIPPoolHTCfgThres,
       "jnxMbgSMIPPoolCurrUtil": jnxMbgSMIPPoolCurrUtil,
       "jnxMbgSMIPPoolLTCfgThres": jnxMbgSMIPPoolLTCfgThres,
       "jnxMbgIPPoolTable": jnxMbgIPPoolTable,
       "jnxMbgIPPoolEntry": jnxMbgIPPoolEntry,
       "jnxMbgIPPoolId": jnxMbgIPPoolId,
       "jnxMbgIPPoolLogicalSystem": jnxMbgIPPoolLogicalSystem,
       "jnxMbgIPPoolRoutingInstance": jnxMbgIPPoolRoutingInstance,
       "jnxMbgIPPoolName": jnxMbgIPPoolName,
       "jnxMbgIPPoolType": jnxMbgIPPoolType,
       "jnxMbgIPPoolFree": jnxMbgIPPoolFree,
       "jnxMbgIPPoolInUse": jnxMbgIPPoolInUse,
       "jnxMbgIPPoolUtil": jnxMbgIPPoolUtil,
       "jnxMbgIPPoolRangeTable": jnxMbgIPPoolRangeTable,
       "jnxMbgIPPoolRangeEntry": jnxMbgIPPoolRangeEntry,
       "jnxMbgIPPoolRangeName": jnxMbgIPPoolRangeName,
       "jnxMbgIPPoolRangeType": jnxMbgIPPoolRangeType,
       "jnxMbgIPPoolRangeFree": jnxMbgIPPoolRangeFree,
       "jnxMbgIPPoolRangeInUse": jnxMbgIPPoolRangeInUse,
       "jnxMbgIPPoolRangeUtil": jnxMbgIPPoolRangeUtil}
)
