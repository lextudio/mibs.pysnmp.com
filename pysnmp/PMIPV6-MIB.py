# SNMP MIB module (PMIPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PMIPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:05 2024
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

(Ipv6AddressIfIdentifierTC,) = mibBuilder.importSymbols(
    "IP-MIB",
    "Ipv6AddressIfIdentifierTC")

(mip6BindingCacheEntry,
 mip6MnBLEntry) = mibBuilder.importSymbols(
    "MOBILEIPV6-MIB",
    "mip6BindingCacheEntry",
    "mip6MnBLEntry")

(Pmip6MnIdentifier,
 Pmip6MnIndex,
 Pmip6MnInterfaceATT,
 Pmip6MnLLIdentifier,
 Pmip6MnLLIndex,
 Pmip6TimeStamp64) = mibBuilder.importSymbols(
    "PMIPV6-TC-MIB",
    "Pmip6MnIdentifier",
    "Pmip6MnIndex",
    "Pmip6MnInterfaceATT",
    "Pmip6MnLLIdentifier",
    "Pmip6MnLLIndex",
    "Pmip6TimeStamp64")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

pmip6MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 206)
)
pmip6MIB.setRevisions(
        ("2012-05-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pmip6Notifications_ObjectIdentity = ObjectIdentity
pmip6Notifications = _Pmip6Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 0)
)
_Pmip6Objects_ObjectIdentity = ObjectIdentity
pmip6Objects = _Pmip6Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1)
)
_Pmip6Core_ObjectIdentity = ObjectIdentity
pmip6Core = _Pmip6Core_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 1)
)
_Pmip6System_ObjectIdentity = ObjectIdentity
pmip6System = _Pmip6System_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 1)
)


class _Pmip6Capabilities_Type(Bits):
    """Custom type pmip6Capabilities based on Bits"""
    namedValues = NamedValues(
        *(("localMobilityAnchor", 1),
          ("mobilityAccessGateway", 0))
    )

_Pmip6Capabilities_Type.__name__ = "Bits"
_Pmip6Capabilities_Object = MibScalar
pmip6Capabilities = _Pmip6Capabilities_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 1, 1),
    _Pmip6Capabilities_Type()
)
pmip6Capabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6Capabilities.setStatus("current")
_Pmip6Bindings_ObjectIdentity = ObjectIdentity
pmip6Bindings = _Pmip6Bindings_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2)
)
_Pmip6BindingCacheTable_Object = MibTable
pmip6BindingCacheTable = _Pmip6BindingCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pmip6BindingCacheTable.setStatus("current")
_Pmip6BindingCacheEntry_Object = MibTableRow
pmip6BindingCacheEntry = _Pmip6BindingCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pmip6BindingCacheEntry.setStatus("current")
_Pmip6BindingPBUFlag_Type = TruthValue
_Pmip6BindingPBUFlag_Object = MibTableColumn
pmip6BindingPBUFlag = _Pmip6BindingPBUFlag_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 1),
    _Pmip6BindingPBUFlag_Type()
)
pmip6BindingPBUFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingPBUFlag.setStatus("current")
_Pmip6BindingMnIndex_Type = Pmip6MnIndex
_Pmip6BindingMnIndex_Object = MibTableColumn
pmip6BindingMnIndex = _Pmip6BindingMnIndex_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 2),
    _Pmip6BindingMnIndex_Type()
)
pmip6BindingMnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingMnIndex.setStatus("current")
_Pmip6BindingMnLLIndex_Type = Pmip6MnLLIndex
_Pmip6BindingMnLLIndex_Object = MibTableColumn
pmip6BindingMnLLIndex = _Pmip6BindingMnLLIndex_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 3),
    _Pmip6BindingMnLLIndex_Type()
)
pmip6BindingMnLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingMnLLIndex.setStatus("current")
_Pmip6BindingMagLinkLocalAddressType_Type = InetAddressType
_Pmip6BindingMagLinkLocalAddressType_Object = MibTableColumn
pmip6BindingMagLinkLocalAddressType = _Pmip6BindingMagLinkLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 4),
    _Pmip6BindingMagLinkLocalAddressType_Type()
)
pmip6BindingMagLinkLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingMagLinkLocalAddressType.setStatus("current")
_Pmip6BindingMagLinkLocalAddress_Type = InetAddress
_Pmip6BindingMagLinkLocalAddress_Object = MibTableColumn
pmip6BindingMagLinkLocalAddress = _Pmip6BindingMagLinkLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 5),
    _Pmip6BindingMagLinkLocalAddress_Type()
)
pmip6BindingMagLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingMagLinkLocalAddress.setStatus("current")
_Pmip6BindingTunnelIfIdentifier_Type = Ipv6AddressIfIdentifierTC
_Pmip6BindingTunnelIfIdentifier_Object = MibTableColumn
pmip6BindingTunnelIfIdentifier = _Pmip6BindingTunnelIfIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 6),
    _Pmip6BindingTunnelIfIdentifier_Type()
)
pmip6BindingTunnelIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingTunnelIfIdentifier.setStatus("current")
_Pmip6BindingMnInterfaceATT_Type = Pmip6MnInterfaceATT
_Pmip6BindingMnInterfaceATT_Object = MibTableColumn
pmip6BindingMnInterfaceATT = _Pmip6BindingMnInterfaceATT_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 7),
    _Pmip6BindingMnInterfaceATT_Type()
)
pmip6BindingMnInterfaceATT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingMnInterfaceATT.setStatus("current")
_Pmip6BindingTimeRecentlyAccepted_Type = Pmip6TimeStamp64
_Pmip6BindingTimeRecentlyAccepted_Object = MibTableColumn
pmip6BindingTimeRecentlyAccepted = _Pmip6BindingTimeRecentlyAccepted_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 2, 1, 1, 8),
    _Pmip6BindingTimeRecentlyAccepted_Type()
)
pmip6BindingTimeRecentlyAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingTimeRecentlyAccepted.setStatus("current")
_Pmip6Conf_ObjectIdentity = ObjectIdentity
pmip6Conf = _Pmip6Conf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 3)
)


class _Pmip6MobileNodeGeneratedTimestampInUse_Type(TruthValue):
    """Custom type pmip6MobileNodeGeneratedTimestampInUse based on TruthValue"""


_Pmip6MobileNodeGeneratedTimestampInUse_Object = MibScalar
pmip6MobileNodeGeneratedTimestampInUse = _Pmip6MobileNodeGeneratedTimestampInUse_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 3, 1),
    _Pmip6MobileNodeGeneratedTimestampInUse_Type()
)
pmip6MobileNodeGeneratedTimestampInUse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6MobileNodeGeneratedTimestampInUse.setStatus("current")
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Type = InetAddressType
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Object = MibScalar
pmip6FixedMagLinkLocalAddressOnAllAccessLinksType = _Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 3, 2),
    _Pmip6FixedMagLinkLocalAddressOnAllAccessLinksType_Type()
)
pmip6FixedMagLinkLocalAddressOnAllAccessLinksType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6FixedMagLinkLocalAddressOnAllAccessLinksType.setStatus("current")
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Type = InetAddress
_Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Object = MibScalar
pmip6FixedMagLinkLocalAddressOnAllAccessLinks = _Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 3, 3),
    _Pmip6FixedMagLinkLocalAddressOnAllAccessLinks_Type()
)
pmip6FixedMagLinkLocalAddressOnAllAccessLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6FixedMagLinkLocalAddressOnAllAccessLinks.setStatus("current")
_Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Type = PhysAddress
_Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Object = MibScalar
pmip6FixedMagLinkLayerAddressOnAllAccessLinks = _Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 3, 4),
    _Pmip6FixedMagLinkLayerAddressOnAllAccessLinks_Type()
)
pmip6FixedMagLinkLayerAddressOnAllAccessLinks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6FixedMagLinkLayerAddressOnAllAccessLinks.setStatus("current")
_Pmip6Stats_ObjectIdentity = ObjectIdentity
pmip6Stats = _Pmip6Stats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4)
)
_Pmip6BindingRegCounters_ObjectIdentity = ObjectIdentity
pmip6BindingRegCounters = _Pmip6BindingRegCounters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1)
)
_Pmip6MissingMnIdentifierOption_Type = Counter32
_Pmip6MissingMnIdentifierOption_Object = MibScalar
pmip6MissingMnIdentifierOption = _Pmip6MissingMnIdentifierOption_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 1),
    _Pmip6MissingMnIdentifierOption_Type()
)
pmip6MissingMnIdentifierOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MissingMnIdentifierOption.setStatus("current")
_Pmip6MagNotAuthorizedForProxyReg_Type = Counter32
_Pmip6MagNotAuthorizedForProxyReg_Object = MibScalar
pmip6MagNotAuthorizedForProxyReg = _Pmip6MagNotAuthorizedForProxyReg_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 2),
    _Pmip6MagNotAuthorizedForProxyReg_Type()
)
pmip6MagNotAuthorizedForProxyReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagNotAuthorizedForProxyReg.setStatus("current")
_Pmip6NotLMAForThisMobileNode_Type = Counter32
_Pmip6NotLMAForThisMobileNode_Object = MibScalar
pmip6NotLMAForThisMobileNode = _Pmip6NotLMAForThisMobileNode_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 3),
    _Pmip6NotLMAForThisMobileNode_Type()
)
pmip6NotLMAForThisMobileNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6NotLMAForThisMobileNode.setStatus("current")
_Pmip6ProxyRegNotEnabled_Type = Counter32
_Pmip6ProxyRegNotEnabled_Object = MibScalar
pmip6ProxyRegNotEnabled = _Pmip6ProxyRegNotEnabled_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 4),
    _Pmip6ProxyRegNotEnabled_Type()
)
pmip6ProxyRegNotEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6ProxyRegNotEnabled.setStatus("current")
_Pmip6MissingHomeNetworkPrefixOption_Type = Counter32
_Pmip6MissingHomeNetworkPrefixOption_Object = MibScalar
pmip6MissingHomeNetworkPrefixOption = _Pmip6MissingHomeNetworkPrefixOption_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 5),
    _Pmip6MissingHomeNetworkPrefixOption_Type()
)
pmip6MissingHomeNetworkPrefixOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MissingHomeNetworkPrefixOption.setStatus("current")
_Pmip6MissingHandOffIndicatorOption_Type = Counter32
_Pmip6MissingHandOffIndicatorOption_Object = MibScalar
pmip6MissingHandOffIndicatorOption = _Pmip6MissingHandOffIndicatorOption_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 6),
    _Pmip6MissingHandOffIndicatorOption_Type()
)
pmip6MissingHandOffIndicatorOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MissingHandOffIndicatorOption.setStatus("current")
_Pmip6MissingAccessTechTypeOption_Type = Counter32
_Pmip6MissingAccessTechTypeOption_Object = MibScalar
pmip6MissingAccessTechTypeOption = _Pmip6MissingAccessTechTypeOption_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 7),
    _Pmip6MissingAccessTechTypeOption_Type()
)
pmip6MissingAccessTechTypeOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MissingAccessTechTypeOption.setStatus("current")
_Pmip6NotAuthorizedForHomeNetworkPrefix_Type = Counter32
_Pmip6NotAuthorizedForHomeNetworkPrefix_Object = MibScalar
pmip6NotAuthorizedForHomeNetworkPrefix = _Pmip6NotAuthorizedForHomeNetworkPrefix_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 8),
    _Pmip6NotAuthorizedForHomeNetworkPrefix_Type()
)
pmip6NotAuthorizedForHomeNetworkPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6NotAuthorizedForHomeNetworkPrefix.setStatus("current")
_Pmip6TimestampMismatch_Type = Counter32
_Pmip6TimestampMismatch_Object = MibScalar
pmip6TimestampMismatch = _Pmip6TimestampMismatch_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 9),
    _Pmip6TimestampMismatch_Type()
)
pmip6TimestampMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6TimestampMismatch.setStatus("current")
_Pmip6TimestampLowerThanPrevAccepted_Type = Counter32
_Pmip6TimestampLowerThanPrevAccepted_Object = MibScalar
pmip6TimestampLowerThanPrevAccepted = _Pmip6TimestampLowerThanPrevAccepted_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 10),
    _Pmip6TimestampLowerThanPrevAccepted_Type()
)
pmip6TimestampLowerThanPrevAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6TimestampLowerThanPrevAccepted.setStatus("current")
_Pmip6BcePbuPrefixSetDoNotMatch_Type = Counter32
_Pmip6BcePbuPrefixSetDoNotMatch_Object = MibScalar
pmip6BcePbuPrefixSetDoNotMatch = _Pmip6BcePbuPrefixSetDoNotMatch_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 11),
    _Pmip6BcePbuPrefixSetDoNotMatch_Type()
)
pmip6BcePbuPrefixSetDoNotMatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BcePbuPrefixSetDoNotMatch.setStatus("current")
_Pmip6InitialBindingRegistrations_Type = Counter32
_Pmip6InitialBindingRegistrations_Object = MibScalar
pmip6InitialBindingRegistrations = _Pmip6InitialBindingRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 12),
    _Pmip6InitialBindingRegistrations_Type()
)
pmip6InitialBindingRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6InitialBindingRegistrations.setStatus("current")
_Pmip6BindingLifeTimeExtensionNoHandOff_Type = Counter32
_Pmip6BindingLifeTimeExtensionNoHandOff_Object = MibScalar
pmip6BindingLifeTimeExtensionNoHandOff = _Pmip6BindingLifeTimeExtensionNoHandOff_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 13),
    _Pmip6BindingLifeTimeExtensionNoHandOff_Type()
)
pmip6BindingLifeTimeExtensionNoHandOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingLifeTimeExtensionNoHandOff.setStatus("current")
_Pmip6BindingLifeTimeExtensionAfterHandOff_Type = Counter32
_Pmip6BindingLifeTimeExtensionAfterHandOff_Object = MibScalar
pmip6BindingLifeTimeExtensionAfterHandOff = _Pmip6BindingLifeTimeExtensionAfterHandOff_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 14),
    _Pmip6BindingLifeTimeExtensionAfterHandOff_Type()
)
pmip6BindingLifeTimeExtensionAfterHandOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingLifeTimeExtensionAfterHandOff.setStatus("current")
_Pmip6BindingDeRegistrations_Type = Counter32
_Pmip6BindingDeRegistrations_Object = MibScalar
pmip6BindingDeRegistrations = _Pmip6BindingDeRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 15),
    _Pmip6BindingDeRegistrations_Type()
)
pmip6BindingDeRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingDeRegistrations.setStatus("current")
_Pmip6BindingBindingAcks_Type = Counter32
_Pmip6BindingBindingAcks_Object = MibScalar
pmip6BindingBindingAcks = _Pmip6BindingBindingAcks_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 16),
    _Pmip6BindingBindingAcks_Type()
)
pmip6BindingBindingAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6BindingBindingAcks.setStatus("current")
_Pmip6CounterDiscontinuityTime_Type = TimeStamp
_Pmip6CounterDiscontinuityTime_Object = MibScalar
pmip6CounterDiscontinuityTime = _Pmip6CounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 1, 4, 1, 17),
    _Pmip6CounterDiscontinuityTime_Type()
)
pmip6CounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6CounterDiscontinuityTime.setStatus("current")
_Pmip6Mag_ObjectIdentity = ObjectIdentity
pmip6Mag = _Pmip6Mag_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 2)
)
_Pmip6MagSystem_ObjectIdentity = ObjectIdentity
pmip6MagSystem = _Pmip6MagSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 1)
)


class _Pmip6MagStatus_Type(Integer32):
    """Custom type pmip6MagStatus based on Integer32"""
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


_Pmip6MagStatus_Type.__name__ = "Integer32"
_Pmip6MagStatus_Object = MibScalar
pmip6MagStatus = _Pmip6MagStatus_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 1, 1),
    _Pmip6MagStatus_Type()
)
pmip6MagStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6MagStatus.setStatus("current")
_Pmip6MagProxyCOATable_Object = MibTable
pmip6MagProxyCOATable = _Pmip6MagProxyCOATable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pmip6MagProxyCOATable.setStatus("current")
_Pmip6MagProxyCOAEntry_Object = MibTableRow
pmip6MagProxyCOAEntry = _Pmip6MagProxyCOAEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 1, 2, 1)
)
pmip6MagProxyCOAEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6MagProxyCOAType"),
    (0, "PMIPV6-MIB", "pmip6MagProxyCOA"),
)
if mibBuilder.loadTexts:
    pmip6MagProxyCOAEntry.setStatus("current")
_Pmip6MagProxyCOAType_Type = InetAddressType
_Pmip6MagProxyCOAType_Object = MibTableColumn
pmip6MagProxyCOAType = _Pmip6MagProxyCOAType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 1, 2, 1, 1),
    _Pmip6MagProxyCOAType_Type()
)
pmip6MagProxyCOAType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6MagProxyCOAType.setStatus("current")
_Pmip6MagProxyCOA_Type = InetAddress
_Pmip6MagProxyCOA_Object = MibTableColumn
pmip6MagProxyCOA = _Pmip6MagProxyCOA_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 1, 2, 1, 2),
    _Pmip6MagProxyCOA_Type()
)
pmip6MagProxyCOA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6MagProxyCOA.setStatus("current")


class _Pmip6MagProxyCOAState_Type(Integer32):
    """Custom type pmip6MagProxyCOAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 2),
          ("tunneled", 3),
          ("unknown", 1))
    )


_Pmip6MagProxyCOAState_Type.__name__ = "Integer32"
_Pmip6MagProxyCOAState_Object = MibTableColumn
pmip6MagProxyCOAState = _Pmip6MagProxyCOAState_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 1, 2, 1, 3),
    _Pmip6MagProxyCOAState_Type()
)
pmip6MagProxyCOAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagProxyCOAState.setStatus("current")
_Pmip6MagConf_ObjectIdentity = ObjectIdentity
pmip6MagConf = _Pmip6MagConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2)
)


class _Pmip6MagEnableMagLocalRouting_Type(TruthValue):
    """Custom type pmip6MagEnableMagLocalRouting based on TruthValue"""


_Pmip6MagEnableMagLocalRouting_Object = MibScalar
pmip6MagEnableMagLocalRouting = _Pmip6MagEnableMagLocalRouting_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 1),
    _Pmip6MagEnableMagLocalRouting_Type()
)
pmip6MagEnableMagLocalRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6MagEnableMagLocalRouting.setStatus("current")
_Pmip6MagMnIdentifierTable_Object = MibTable
pmip6MagMnIdentifierTable = _Pmip6MagMnIdentifierTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pmip6MagMnIdentifierTable.setStatus("current")
_Pmip6MagMnIdentifierEntry_Object = MibTableRow
pmip6MagMnIdentifierEntry = _Pmip6MagMnIdentifierEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 2, 1)
)
pmip6MagMnIdentifierEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6MagBLMnIndex"),
)
if mibBuilder.loadTexts:
    pmip6MagMnIdentifierEntry.setStatus("current")
_Pmip6MagMnIdentifier_Type = Pmip6MnIdentifier
_Pmip6MagMnIdentifier_Object = MibTableColumn
pmip6MagMnIdentifier = _Pmip6MagMnIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 2, 1, 1),
    _Pmip6MagMnIdentifier_Type()
)
pmip6MagMnIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagMnIdentifier.setStatus("current")
_Pmip6MagMnLLIdentifierTable_Object = MibTable
pmip6MagMnLLIdentifierTable = _Pmip6MagMnLLIdentifierTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pmip6MagMnLLIdentifierTable.setStatus("current")
_Pmip6MagMnLLIdentifierEntry_Object = MibTableRow
pmip6MagMnLLIdentifierEntry = _Pmip6MagMnLLIdentifierEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 3, 1)
)
pmip6MagMnLLIdentifierEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6MagBLMnIndex"),
    (0, "PMIPV6-MIB", "pmip6MagBLMnLLIndex"),
)
if mibBuilder.loadTexts:
    pmip6MagMnLLIdentifierEntry.setStatus("current")
_Pmip6MagMnLLIdentifier_Type = Pmip6MnLLIdentifier
_Pmip6MagMnLLIdentifier_Object = MibTableColumn
pmip6MagMnLLIdentifier = _Pmip6MagMnLLIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 3, 1, 1),
    _Pmip6MagMnLLIdentifier_Type()
)
pmip6MagMnLLIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagMnLLIdentifier.setStatus("current")
_Pmip6MagHomeNetworkPrefixTable_Object = MibTable
pmip6MagHomeNetworkPrefixTable = _Pmip6MagHomeNetworkPrefixTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pmip6MagHomeNetworkPrefixTable.setStatus("current")
_Pmip6MagHomeNetworkPrefixEntry_Object = MibTableRow
pmip6MagHomeNetworkPrefixEntry = _Pmip6MagHomeNetworkPrefixEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 4, 1)
)
pmip6MagHomeNetworkPrefixEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6MagBLMnIndex"),
    (0, "PMIPV6-MIB", "pmip6MagBLMnLLIndex"),
    (0, "PMIPV6-MIB", "pmip6MagHomeNetworkPrefixType"),
    (0, "PMIPV6-MIB", "pmip6MagHomeNetworkPrefix"),
)
if mibBuilder.loadTexts:
    pmip6MagHomeNetworkPrefixEntry.setStatus("current")
_Pmip6MagHomeNetworkPrefixType_Type = InetAddressType
_Pmip6MagHomeNetworkPrefixType_Object = MibTableColumn
pmip6MagHomeNetworkPrefixType = _Pmip6MagHomeNetworkPrefixType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 4, 1, 1),
    _Pmip6MagHomeNetworkPrefixType_Type()
)
pmip6MagHomeNetworkPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6MagHomeNetworkPrefixType.setStatus("current")
_Pmip6MagHomeNetworkPrefix_Type = InetAddress
_Pmip6MagHomeNetworkPrefix_Object = MibTableColumn
pmip6MagHomeNetworkPrefix = _Pmip6MagHomeNetworkPrefix_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 4, 1, 2),
    _Pmip6MagHomeNetworkPrefix_Type()
)
pmip6MagHomeNetworkPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6MagHomeNetworkPrefix.setStatus("current")
_Pmip6MagHomeNetworkPrefixLength_Type = InetAddressPrefixLength
_Pmip6MagHomeNetworkPrefixLength_Object = MibTableColumn
pmip6MagHomeNetworkPrefixLength = _Pmip6MagHomeNetworkPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 4, 1, 3),
    _Pmip6MagHomeNetworkPrefixLength_Type()
)
pmip6MagHomeNetworkPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagHomeNetworkPrefixLength.setStatus("current")
_Pmip6MagHomeNetworkPrefixLifeTime_Type = Unsigned32
_Pmip6MagHomeNetworkPrefixLifeTime_Object = MibTableColumn
pmip6MagHomeNetworkPrefixLifeTime = _Pmip6MagHomeNetworkPrefixLifeTime_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 2, 4, 1, 4),
    _Pmip6MagHomeNetworkPrefixLifeTime_Type()
)
pmip6MagHomeNetworkPrefixLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagHomeNetworkPrefixLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    pmip6MagHomeNetworkPrefixLifeTime.setUnits("seconds")
_Pmip6MagRegistration_ObjectIdentity = ObjectIdentity
pmip6MagRegistration = _Pmip6MagRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3)
)
_Pmip6MagBLTable_Object = MibTable
pmip6MagBLTable = _Pmip6MagBLTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pmip6MagBLTable.setStatus("current")
_Pmip6MagBLEntry_Object = MibTableRow
pmip6MagBLEntry = _Pmip6MagBLEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pmip6MagBLEntry.setStatus("current")
_Pmip6MagBLFlag_Type = TruthValue
_Pmip6MagBLFlag_Object = MibTableColumn
pmip6MagBLFlag = _Pmip6MagBLFlag_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 1),
    _Pmip6MagBLFlag_Type()
)
pmip6MagBLFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLFlag.setStatus("current")
_Pmip6MagBLMnIndex_Type = Pmip6MnIndex
_Pmip6MagBLMnIndex_Object = MibTableColumn
pmip6MagBLMnIndex = _Pmip6MagBLMnIndex_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 2),
    _Pmip6MagBLMnIndex_Type()
)
pmip6MagBLMnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLMnIndex.setStatus("current")
_Pmip6MagBLMnLLIndex_Type = Pmip6MnLLIndex
_Pmip6MagBLMnLLIndex_Object = MibTableColumn
pmip6MagBLMnLLIndex = _Pmip6MagBLMnLLIndex_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 3),
    _Pmip6MagBLMnLLIndex_Type()
)
pmip6MagBLMnLLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLMnLLIndex.setStatus("current")
_Pmip6MagBLMagLinkLocalAddressType_Type = InetAddressType
_Pmip6MagBLMagLinkLocalAddressType_Object = MibTableColumn
pmip6MagBLMagLinkLocalAddressType = _Pmip6MagBLMagLinkLocalAddressType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 4),
    _Pmip6MagBLMagLinkLocalAddressType_Type()
)
pmip6MagBLMagLinkLocalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLMagLinkLocalAddressType.setStatus("current")
_Pmip6MagBLMagLinkLocalAddress_Type = InetAddress
_Pmip6MagBLMagLinkLocalAddress_Object = MibTableColumn
pmip6MagBLMagLinkLocalAddress = _Pmip6MagBLMagLinkLocalAddress_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 5),
    _Pmip6MagBLMagLinkLocalAddress_Type()
)
pmip6MagBLMagLinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLMagLinkLocalAddress.setStatus("current")
_Pmip6MagBLMagIfIdentifierToMn_Type = Ipv6AddressIfIdentifierTC
_Pmip6MagBLMagIfIdentifierToMn_Object = MibTableColumn
pmip6MagBLMagIfIdentifierToMn = _Pmip6MagBLMagIfIdentifierToMn_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 6),
    _Pmip6MagBLMagIfIdentifierToMn_Type()
)
pmip6MagBLMagIfIdentifierToMn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLMagIfIdentifierToMn.setStatus("current")
_Pmip6MagBLTunnelIfIdentifier_Type = Ipv6AddressIfIdentifierTC
_Pmip6MagBLTunnelIfIdentifier_Object = MibTableColumn
pmip6MagBLTunnelIfIdentifier = _Pmip6MagBLTunnelIfIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 7),
    _Pmip6MagBLTunnelIfIdentifier_Type()
)
pmip6MagBLTunnelIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLTunnelIfIdentifier.setStatus("current")
_Pmip6MagBLMnInterfaceATT_Type = Pmip6MnInterfaceATT
_Pmip6MagBLMnInterfaceATT_Object = MibTableColumn
pmip6MagBLMnInterfaceATT = _Pmip6MagBLMnInterfaceATT_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 8),
    _Pmip6MagBLMnInterfaceATT_Type()
)
pmip6MagBLMnInterfaceATT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLMnInterfaceATT.setStatus("current")
_Pmip6MagBLTimeRecentlyAccepted_Type = Pmip6TimeStamp64
_Pmip6MagBLTimeRecentlyAccepted_Object = MibTableColumn
pmip6MagBLTimeRecentlyAccepted = _Pmip6MagBLTimeRecentlyAccepted_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 1, 1, 9),
    _Pmip6MagBLTimeRecentlyAccepted_Type()
)
pmip6MagBLTimeRecentlyAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagBLTimeRecentlyAccepted.setStatus("current")
_Pmip6MagMnProfileTable_Object = MibTable
pmip6MagMnProfileTable = _Pmip6MagMnProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    pmip6MagMnProfileTable.setStatus("current")
_Pmip6MagMnProfileEntry_Object = MibTableRow
pmip6MagMnProfileEntry = _Pmip6MagMnProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 2, 1)
)
pmip6MagMnProfileEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6MagProfMnIndex"),
)
if mibBuilder.loadTexts:
    pmip6MagMnProfileEntry.setStatus("current")
_Pmip6MagProfMnIndex_Type = Pmip6MnIndex
_Pmip6MagProfMnIndex_Object = MibTableColumn
pmip6MagProfMnIndex = _Pmip6MagProfMnIndex_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 2, 1, 1),
    _Pmip6MagProfMnIndex_Type()
)
pmip6MagProfMnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6MagProfMnIndex.setStatus("current")
_Pmip6MagProfMnIdentifier_Type = Pmip6MnIdentifier
_Pmip6MagProfMnIdentifier_Object = MibTableColumn
pmip6MagProfMnIdentifier = _Pmip6MagProfMnIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 2, 1, 2),
    _Pmip6MagProfMnIdentifier_Type()
)
pmip6MagProfMnIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagProfMnIdentifier.setStatus("current")
_Pmip6MagProfMnLocalMobilityAnchorAddressType_Type = InetAddressType
_Pmip6MagProfMnLocalMobilityAnchorAddressType_Object = MibTableColumn
pmip6MagProfMnLocalMobilityAnchorAddressType = _Pmip6MagProfMnLocalMobilityAnchorAddressType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 2, 1, 3),
    _Pmip6MagProfMnLocalMobilityAnchorAddressType_Type()
)
pmip6MagProfMnLocalMobilityAnchorAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagProfMnLocalMobilityAnchorAddressType.setStatus("current")
_Pmip6MagProfMnLocalMobilityAnchorAddress_Type = InetAddress
_Pmip6MagProfMnLocalMobilityAnchorAddress_Object = MibTableColumn
pmip6MagProfMnLocalMobilityAnchorAddress = _Pmip6MagProfMnLocalMobilityAnchorAddress_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 2, 3, 2, 1, 4),
    _Pmip6MagProfMnLocalMobilityAnchorAddress_Type()
)
pmip6MagProfMnLocalMobilityAnchorAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6MagProfMnLocalMobilityAnchorAddress.setStatus("current")
_Pmip6Lma_ObjectIdentity = ObjectIdentity
pmip6Lma = _Pmip6Lma_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 3)
)
_Pmip6LmaSystem_ObjectIdentity = ObjectIdentity
pmip6LmaSystem = _Pmip6LmaSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 1)
)


class _Pmip6LmaStatus_Type(Integer32):
    """Custom type pmip6LmaStatus based on Integer32"""
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


_Pmip6LmaStatus_Type.__name__ = "Integer32"
_Pmip6LmaStatus_Object = MibScalar
pmip6LmaStatus = _Pmip6LmaStatus_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 1, 1),
    _Pmip6LmaStatus_Type()
)
pmip6LmaStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6LmaStatus.setStatus("current")
_Pmip6LmaLMAATable_Object = MibTable
pmip6LmaLMAATable = _Pmip6LmaLMAATable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pmip6LmaLMAATable.setStatus("current")
_Pmip6LmaLMAAEntry_Object = MibTableRow
pmip6LmaLMAAEntry = _Pmip6LmaLMAAEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 1, 2, 1)
)
pmip6LmaLMAAEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6LmaLMAAType"),
    (0, "PMIPV6-MIB", "pmip6LmaLMAA"),
)
if mibBuilder.loadTexts:
    pmip6LmaLMAAEntry.setStatus("current")
_Pmip6LmaLMAAType_Type = InetAddressType
_Pmip6LmaLMAAType_Object = MibTableColumn
pmip6LmaLMAAType = _Pmip6LmaLMAAType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 1, 2, 1, 1),
    _Pmip6LmaLMAAType_Type()
)
pmip6LmaLMAAType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6LmaLMAAType.setStatus("current")
_Pmip6LmaLMAA_Type = InetAddress
_Pmip6LmaLMAA_Object = MibTableColumn
pmip6LmaLMAA = _Pmip6LmaLMAA_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 1, 2, 1, 2),
    _Pmip6LmaLMAA_Type()
)
pmip6LmaLMAA.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6LmaLMAA.setStatus("current")


class _Pmip6LmaLMAAState_Type(Integer32):
    """Custom type pmip6LmaLMAAState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activated", 2),
          ("tunneled", 3),
          ("unknown", 1))
    )


_Pmip6LmaLMAAState_Type.__name__ = "Integer32"
_Pmip6LmaLMAAState_Object = MibTableColumn
pmip6LmaLMAAState = _Pmip6LmaLMAAState_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 1, 2, 1, 3),
    _Pmip6LmaLMAAState_Type()
)
pmip6LmaLMAAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6LmaLMAAState.setStatus("current")
_Pmip6LmaConf_ObjectIdentity = ObjectIdentity
pmip6LmaConf = _Pmip6LmaConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2)
)


class _Pmip6LmaMinDelayBeforeBCEDelete_Type(Integer32):
    """Custom type pmip6LmaMinDelayBeforeBCEDelete based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pmip6LmaMinDelayBeforeBCEDelete_Type.__name__ = "Integer32"
_Pmip6LmaMinDelayBeforeBCEDelete_Object = MibScalar
pmip6LmaMinDelayBeforeBCEDelete = _Pmip6LmaMinDelayBeforeBCEDelete_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 1),
    _Pmip6LmaMinDelayBeforeBCEDelete_Type()
)
pmip6LmaMinDelayBeforeBCEDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6LmaMinDelayBeforeBCEDelete.setStatus("current")
if mibBuilder.loadTexts:
    pmip6LmaMinDelayBeforeBCEDelete.setUnits("milliseconds")


class _Pmip6LmaMaxDelayBeforeNewBCEAssign_Type(Integer32):
    """Custom type pmip6LmaMaxDelayBeforeNewBCEAssign based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pmip6LmaMaxDelayBeforeNewBCEAssign_Type.__name__ = "Integer32"
_Pmip6LmaMaxDelayBeforeNewBCEAssign_Object = MibScalar
pmip6LmaMaxDelayBeforeNewBCEAssign = _Pmip6LmaMaxDelayBeforeNewBCEAssign_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 2),
    _Pmip6LmaMaxDelayBeforeNewBCEAssign_Type()
)
pmip6LmaMaxDelayBeforeNewBCEAssign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6LmaMaxDelayBeforeNewBCEAssign.setStatus("current")
if mibBuilder.loadTexts:
    pmip6LmaMaxDelayBeforeNewBCEAssign.setUnits("milliseconds")


class _Pmip6LmaTimestampValidityWindow_Type(Integer32):
    """Custom type pmip6LmaTimestampValidityWindow based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Pmip6LmaTimestampValidityWindow_Type.__name__ = "Integer32"
_Pmip6LmaTimestampValidityWindow_Object = MibScalar
pmip6LmaTimestampValidityWindow = _Pmip6LmaTimestampValidityWindow_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 3),
    _Pmip6LmaTimestampValidityWindow_Type()
)
pmip6LmaTimestampValidityWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6LmaTimestampValidityWindow.setStatus("current")
if mibBuilder.loadTexts:
    pmip6LmaTimestampValidityWindow.setUnits("milliseconds")
_Pmip6LmaMnIdentifierTable_Object = MibTable
pmip6LmaMnIdentifierTable = _Pmip6LmaMnIdentifierTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    pmip6LmaMnIdentifierTable.setStatus("current")
_Pmip6LmaMnIdentifierEntry_Object = MibTableRow
pmip6LmaMnIdentifierEntry = _Pmip6LmaMnIdentifierEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 4, 1)
)
pmip6LmaMnIdentifierEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6BindingMnIndex"),
)
if mibBuilder.loadTexts:
    pmip6LmaMnIdentifierEntry.setStatus("current")
_Pmip6LmaMnIdentifier_Type = Pmip6MnIdentifier
_Pmip6LmaMnIdentifier_Object = MibTableColumn
pmip6LmaMnIdentifier = _Pmip6LmaMnIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 4, 1, 1),
    _Pmip6LmaMnIdentifier_Type()
)
pmip6LmaMnIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6LmaMnIdentifier.setStatus("current")
_Pmip6LmaMnLLIdentifierTable_Object = MibTable
pmip6LmaMnLLIdentifierTable = _Pmip6LmaMnLLIdentifierTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 5)
)
if mibBuilder.loadTexts:
    pmip6LmaMnLLIdentifierTable.setStatus("current")
_Pmip6LmaMnLLIdentifierEntry_Object = MibTableRow
pmip6LmaMnLLIdentifierEntry = _Pmip6LmaMnLLIdentifierEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 5, 1)
)
pmip6LmaMnLLIdentifierEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6BindingMnIndex"),
    (0, "PMIPV6-MIB", "pmip6BindingMnLLIndex"),
)
if mibBuilder.loadTexts:
    pmip6LmaMnLLIdentifierEntry.setStatus("current")
_Pmip6LmaMnLLIdentifier_Type = Pmip6MnLLIdentifier
_Pmip6LmaMnLLIdentifier_Object = MibTableColumn
pmip6LmaMnLLIdentifier = _Pmip6LmaMnLLIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 5, 1, 1),
    _Pmip6LmaMnLLIdentifier_Type()
)
pmip6LmaMnLLIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6LmaMnLLIdentifier.setStatus("current")
_Pmip6LmaHomeNetworkPrefixTable_Object = MibTable
pmip6LmaHomeNetworkPrefixTable = _Pmip6LmaHomeNetworkPrefixTable_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 6)
)
if mibBuilder.loadTexts:
    pmip6LmaHomeNetworkPrefixTable.setStatus("current")
_Pmip6LmaHomeNetworkPrefixEntry_Object = MibTableRow
pmip6LmaHomeNetworkPrefixEntry = _Pmip6LmaHomeNetworkPrefixEntry_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 6, 1)
)
pmip6LmaHomeNetworkPrefixEntry.setIndexNames(
    (0, "PMIPV6-MIB", "pmip6BindingMnIndex"),
    (0, "PMIPV6-MIB", "pmip6BindingMnLLIndex"),
    (0, "PMIPV6-MIB", "pmip6LmaHomeNetworkPrefixType"),
    (0, "PMIPV6-MIB", "pmip6LmaHomeNetworkPrefix"),
)
if mibBuilder.loadTexts:
    pmip6LmaHomeNetworkPrefixEntry.setStatus("current")
_Pmip6LmaHomeNetworkPrefixType_Type = InetAddressType
_Pmip6LmaHomeNetworkPrefixType_Object = MibTableColumn
pmip6LmaHomeNetworkPrefixType = _Pmip6LmaHomeNetworkPrefixType_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 6, 1, 1),
    _Pmip6LmaHomeNetworkPrefixType_Type()
)
pmip6LmaHomeNetworkPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6LmaHomeNetworkPrefixType.setStatus("current")
_Pmip6LmaHomeNetworkPrefix_Type = InetAddress
_Pmip6LmaHomeNetworkPrefix_Object = MibTableColumn
pmip6LmaHomeNetworkPrefix = _Pmip6LmaHomeNetworkPrefix_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 6, 1, 2),
    _Pmip6LmaHomeNetworkPrefix_Type()
)
pmip6LmaHomeNetworkPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pmip6LmaHomeNetworkPrefix.setStatus("current")
_Pmip6LmaHomeNetworkPrefixLength_Type = InetAddressPrefixLength
_Pmip6LmaHomeNetworkPrefixLength_Object = MibTableColumn
pmip6LmaHomeNetworkPrefixLength = _Pmip6LmaHomeNetworkPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 6, 1, 3),
    _Pmip6LmaHomeNetworkPrefixLength_Type()
)
pmip6LmaHomeNetworkPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmip6LmaHomeNetworkPrefixLength.setStatus("current")
_Pmip6LmaHomeNetworkPrefixLifeTime_Type = Gauge32
_Pmip6LmaHomeNetworkPrefixLifeTime_Object = MibTableColumn
pmip6LmaHomeNetworkPrefixLifeTime = _Pmip6LmaHomeNetworkPrefixLifeTime_Object(
    (1, 3, 6, 1, 2, 1, 206, 1, 3, 2, 6, 1, 4),
    _Pmip6LmaHomeNetworkPrefixLifeTime_Type()
)
pmip6LmaHomeNetworkPrefixLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmip6LmaHomeNetworkPrefixLifeTime.setStatus("current")
if mibBuilder.loadTexts:
    pmip6LmaHomeNetworkPrefixLifeTime.setUnits("seconds")
_Pmip6Conformance_ObjectIdentity = ObjectIdentity
pmip6Conformance = _Pmip6Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 2)
)
_Pmip6Groups_ObjectIdentity = ObjectIdentity
pmip6Groups = _Pmip6Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 2, 1)
)
_Pmip6Compliances_ObjectIdentity = ObjectIdentity
pmip6Compliances = _Pmip6Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 206, 2, 2)
)
mip6BindingCacheEntry.registerAugmentions(
    ("PMIPV6-MIB",
     "pmip6BindingCacheEntry")
)
pmip6BindingCacheEntry.setIndexNames(*mip6BindingCacheEntry.getIndexNames())
mip6MnBLEntry.registerAugmentions(
    ("PMIPV6-MIB",
     "pmip6MagBLEntry")
)
pmip6MagBLEntry.setIndexNames(*mip6MnBLEntry.getIndexNames())

# Managed Objects groups

pmip6SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 1)
)
pmip6SystemGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6Capabilities"),
        ("PMIPV6-MIB", "pmip6MobileNodeGeneratedTimestampInUse"),
        ("PMIPV6-MIB", "pmip6FixedMagLinkLocalAddressOnAllAccessLinksType"),
        ("PMIPV6-MIB", "pmip6FixedMagLinkLocalAddressOnAllAccessLinks"),
        ("PMIPV6-MIB", "pmip6FixedMagLinkLayerAddressOnAllAccessLinks"))
)
if mibBuilder.loadTexts:
    pmip6SystemGroup.setStatus("current")

pmip6BindingCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 2)
)
pmip6BindingCacheGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6BindingPBUFlag"),
        ("PMIPV6-MIB", "pmip6BindingMnIndex"),
        ("PMIPV6-MIB", "pmip6BindingMnLLIndex"),
        ("PMIPV6-MIB", "pmip6BindingMagLinkLocalAddressType"),
        ("PMIPV6-MIB", "pmip6BindingMagLinkLocalAddress"),
        ("PMIPV6-MIB", "pmip6BindingTunnelIfIdentifier"),
        ("PMIPV6-MIB", "pmip6BindingMnInterfaceATT"),
        ("PMIPV6-MIB", "pmip6BindingTimeRecentlyAccepted"),
        ("PMIPV6-MIB", "pmip6LmaMnIdentifier"),
        ("PMIPV6-MIB", "pmip6LmaMnLLIdentifier"))
)
if mibBuilder.loadTexts:
    pmip6BindingCacheGroup.setStatus("current")

pmip6StatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 3)
)
pmip6StatsGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6MissingMnIdentifierOption"),
        ("PMIPV6-MIB", "pmip6MagNotAuthorizedForProxyReg"),
        ("PMIPV6-MIB", "pmip6NotLMAForThisMobileNode"),
        ("PMIPV6-MIB", "pmip6ProxyRegNotEnabled"),
        ("PMIPV6-MIB", "pmip6MissingHomeNetworkPrefixOption"),
        ("PMIPV6-MIB", "pmip6MissingHandOffIndicatorOption"),
        ("PMIPV6-MIB", "pmip6MissingAccessTechTypeOption"),
        ("PMIPV6-MIB", "pmip6NotAuthorizedForHomeNetworkPrefix"),
        ("PMIPV6-MIB", "pmip6TimestampMismatch"),
        ("PMIPV6-MIB", "pmip6TimestampLowerThanPrevAccepted"),
        ("PMIPV6-MIB", "pmip6BcePbuPrefixSetDoNotMatch"),
        ("PMIPV6-MIB", "pmip6InitialBindingRegistrations"),
        ("PMIPV6-MIB", "pmip6BindingLifeTimeExtensionNoHandOff"),
        ("PMIPV6-MIB", "pmip6BindingLifeTimeExtensionAfterHandOff"),
        ("PMIPV6-MIB", "pmip6BindingDeRegistrations"),
        ("PMIPV6-MIB", "pmip6BindingBindingAcks"),
        ("PMIPV6-MIB", "pmip6CounterDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    pmip6StatsGroup.setStatus("current")

pmip6MagSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 4)
)
pmip6MagSystemGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6MagStatus"),
        ("PMIPV6-MIB", "pmip6MagProxyCOAState"))
)
if mibBuilder.loadTexts:
    pmip6MagSystemGroup.setStatus("current")

pmip6MagConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 5)
)
pmip6MagConfigurationGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6MagHomeNetworkPrefixLength"),
        ("PMIPV6-MIB", "pmip6MagHomeNetworkPrefixLifeTime"),
        ("PMIPV6-MIB", "pmip6MagEnableMagLocalRouting"))
)
if mibBuilder.loadTexts:
    pmip6MagConfigurationGroup.setStatus("current")

pmip6MagRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 6)
)
pmip6MagRegistrationGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6MagBLFlag"),
        ("PMIPV6-MIB", "pmip6MagBLMnIndex"),
        ("PMIPV6-MIB", "pmip6MagBLMnLLIndex"),
        ("PMIPV6-MIB", "pmip6MagBLMagLinkLocalAddressType"),
        ("PMIPV6-MIB", "pmip6MagBLMagLinkLocalAddress"),
        ("PMIPV6-MIB", "pmip6MagBLMagIfIdentifierToMn"),
        ("PMIPV6-MIB", "pmip6MagBLTunnelIfIdentifier"),
        ("PMIPV6-MIB", "pmip6MagBLMnInterfaceATT"),
        ("PMIPV6-MIB", "pmip6MagBLTimeRecentlyAccepted"),
        ("PMIPV6-MIB", "pmip6MagMnIdentifier"),
        ("PMIPV6-MIB", "pmip6MagMnLLIdentifier"),
        ("PMIPV6-MIB", "pmip6MagProfMnIdentifier"),
        ("PMIPV6-MIB", "pmip6MagProfMnLocalMobilityAnchorAddressType"),
        ("PMIPV6-MIB", "pmip6MagProfMnLocalMobilityAnchorAddress"))
)
if mibBuilder.loadTexts:
    pmip6MagRegistrationGroup.setStatus("current")

pmip6LmaSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 7)
)
pmip6LmaSystemGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6LmaStatus"),
        ("PMIPV6-MIB", "pmip6LmaLMAAState"))
)
if mibBuilder.loadTexts:
    pmip6LmaSystemGroup.setStatus("current")

pmip6LmaConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 8)
)
pmip6LmaConfigurationGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6LmaMinDelayBeforeBCEDelete"),
        ("PMIPV6-MIB", "pmip6LmaMaxDelayBeforeNewBCEAssign"),
        ("PMIPV6-MIB", "pmip6LmaTimestampValidityWindow"),
        ("PMIPV6-MIB", "pmip6LmaHomeNetworkPrefixLength"),
        ("PMIPV6-MIB", "pmip6LmaHomeNetworkPrefixLifeTime"))
)
if mibBuilder.loadTexts:
    pmip6LmaConfigurationGroup.setStatus("current")


# Notification objects

pmip6MagHomeTunnelEstablished = NotificationType(
    (1, 3, 6, 1, 2, 1, 206, 0, 1)
)
pmip6MagHomeTunnelEstablished.setObjects(
      *(("PMIPV6-MIB", "pmip6MagBLTunnelIfIdentifier"),
        ("PMIPV6-MIB", "pmip6MagProxyCOAState"))
)
if mibBuilder.loadTexts:
    pmip6MagHomeTunnelEstablished.setStatus(
        "current"
    )

pmip6MagHomeTunnelReleased = NotificationType(
    (1, 3, 6, 1, 2, 1, 206, 0, 2)
)
pmip6MagHomeTunnelReleased.setObjects(
      *(("PMIPV6-MIB", "pmip6MagBLTunnelIfIdentifier"),
        ("PMIPV6-MIB", "pmip6MagProxyCOAState"))
)
if mibBuilder.loadTexts:
    pmip6MagHomeTunnelReleased.setStatus(
        "current"
    )

pmip6LmaHomeTunnelEstablished = NotificationType(
    (1, 3, 6, 1, 2, 1, 206, 0, 3)
)
pmip6LmaHomeTunnelEstablished.setObjects(
      *(("PMIPV6-MIB", "pmip6BindingTunnelIfIdentifier"),
        ("PMIPV6-MIB", "pmip6LmaLMAAState"))
)
if mibBuilder.loadTexts:
    pmip6LmaHomeTunnelEstablished.setStatus(
        "current"
    )

pmip6LmaHomeTunnelReleased = NotificationType(
    (1, 3, 6, 1, 2, 1, 206, 0, 4)
)
pmip6LmaHomeTunnelReleased.setObjects(
      *(("PMIPV6-MIB", "pmip6BindingTunnelIfIdentifier"),
        ("PMIPV6-MIB", "pmip6LmaLMAAState"))
)
if mibBuilder.loadTexts:
    pmip6LmaHomeTunnelReleased.setStatus(
        "current"
    )


# Notifications groups

pmip6MagNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 9)
)
pmip6MagNotificationGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6MagHomeTunnelEstablished"),
        ("PMIPV6-MIB", "pmip6MagHomeTunnelReleased"))
)
if mibBuilder.loadTexts:
    pmip6MagNotificationGroup.setStatus(
        "current"
    )

pmip6LmaNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 206, 2, 1, 10)
)
pmip6LmaNotificationGroup.setObjects(
      *(("PMIPV6-MIB", "pmip6LmaHomeTunnelEstablished"),
        ("PMIPV6-MIB", "pmip6LmaHomeTunnelReleased"))
)
if mibBuilder.loadTexts:
    pmip6LmaNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pmip6CoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pmip6CoreCompliance.setStatus(
        "current"
    )

pmip6Compliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 2)
)
if mibBuilder.loadTexts:
    pmip6Compliance2.setStatus(
        "current"
    )

pmip6CoreReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 3)
)
if mibBuilder.loadTexts:
    pmip6CoreReadOnlyCompliance.setStatus(
        "current"
    )

pmip6ReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 4)
)
if mibBuilder.loadTexts:
    pmip6ReadOnlyCompliance2.setStatus(
        "current"
    )

pmip6MagCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 5)
)
if mibBuilder.loadTexts:
    pmip6MagCoreCompliance.setStatus(
        "current"
    )

pmip6MagCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 6)
)
if mibBuilder.loadTexts:
    pmip6MagCompliance2.setStatus(
        "current"
    )

pmip6MagCoreReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 7)
)
if mibBuilder.loadTexts:
    pmip6MagCoreReadOnlyCompliance.setStatus(
        "current"
    )

pmip6MagReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 8)
)
if mibBuilder.loadTexts:
    pmip6MagReadOnlyCompliance2.setStatus(
        "current"
    )

pmip6LmaCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 9)
)
if mibBuilder.loadTexts:
    pmip6LmaCoreCompliance.setStatus(
        "current"
    )

pmip6LmaCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 10)
)
if mibBuilder.loadTexts:
    pmip6LmaCompliance2.setStatus(
        "current"
    )

pmip6LmaReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 11)
)
if mibBuilder.loadTexts:
    pmip6LmaReadOnlyCompliance.setStatus(
        "current"
    )

pmip6LmaReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 12)
)
if mibBuilder.loadTexts:
    pmip6LmaReadOnlyCompliance2.setStatus(
        "current"
    )

pmip6MagNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 13)
)
if mibBuilder.loadTexts:
    pmip6MagNotificationCompliance.setStatus(
        "current"
    )

pmip6LmaNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 206, 2, 2, 14)
)
if mibBuilder.loadTexts:
    pmip6LmaNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PMIPV6-MIB",
    **{"pmip6MIB": pmip6MIB,
       "pmip6Notifications": pmip6Notifications,
       "pmip6MagHomeTunnelEstablished": pmip6MagHomeTunnelEstablished,
       "pmip6MagHomeTunnelReleased": pmip6MagHomeTunnelReleased,
       "pmip6LmaHomeTunnelEstablished": pmip6LmaHomeTunnelEstablished,
       "pmip6LmaHomeTunnelReleased": pmip6LmaHomeTunnelReleased,
       "pmip6Objects": pmip6Objects,
       "pmip6Core": pmip6Core,
       "pmip6System": pmip6System,
       "pmip6Capabilities": pmip6Capabilities,
       "pmip6Bindings": pmip6Bindings,
       "pmip6BindingCacheTable": pmip6BindingCacheTable,
       "pmip6BindingCacheEntry": pmip6BindingCacheEntry,
       "pmip6BindingPBUFlag": pmip6BindingPBUFlag,
       "pmip6BindingMnIndex": pmip6BindingMnIndex,
       "pmip6BindingMnLLIndex": pmip6BindingMnLLIndex,
       "pmip6BindingMagLinkLocalAddressType": pmip6BindingMagLinkLocalAddressType,
       "pmip6BindingMagLinkLocalAddress": pmip6BindingMagLinkLocalAddress,
       "pmip6BindingTunnelIfIdentifier": pmip6BindingTunnelIfIdentifier,
       "pmip6BindingMnInterfaceATT": pmip6BindingMnInterfaceATT,
       "pmip6BindingTimeRecentlyAccepted": pmip6BindingTimeRecentlyAccepted,
       "pmip6Conf": pmip6Conf,
       "pmip6MobileNodeGeneratedTimestampInUse": pmip6MobileNodeGeneratedTimestampInUse,
       "pmip6FixedMagLinkLocalAddressOnAllAccessLinksType": pmip6FixedMagLinkLocalAddressOnAllAccessLinksType,
       "pmip6FixedMagLinkLocalAddressOnAllAccessLinks": pmip6FixedMagLinkLocalAddressOnAllAccessLinks,
       "pmip6FixedMagLinkLayerAddressOnAllAccessLinks": pmip6FixedMagLinkLayerAddressOnAllAccessLinks,
       "pmip6Stats": pmip6Stats,
       "pmip6BindingRegCounters": pmip6BindingRegCounters,
       "pmip6MissingMnIdentifierOption": pmip6MissingMnIdentifierOption,
       "pmip6MagNotAuthorizedForProxyReg": pmip6MagNotAuthorizedForProxyReg,
       "pmip6NotLMAForThisMobileNode": pmip6NotLMAForThisMobileNode,
       "pmip6ProxyRegNotEnabled": pmip6ProxyRegNotEnabled,
       "pmip6MissingHomeNetworkPrefixOption": pmip6MissingHomeNetworkPrefixOption,
       "pmip6MissingHandOffIndicatorOption": pmip6MissingHandOffIndicatorOption,
       "pmip6MissingAccessTechTypeOption": pmip6MissingAccessTechTypeOption,
       "pmip6NotAuthorizedForHomeNetworkPrefix": pmip6NotAuthorizedForHomeNetworkPrefix,
       "pmip6TimestampMismatch": pmip6TimestampMismatch,
       "pmip6TimestampLowerThanPrevAccepted": pmip6TimestampLowerThanPrevAccepted,
       "pmip6BcePbuPrefixSetDoNotMatch": pmip6BcePbuPrefixSetDoNotMatch,
       "pmip6InitialBindingRegistrations": pmip6InitialBindingRegistrations,
       "pmip6BindingLifeTimeExtensionNoHandOff": pmip6BindingLifeTimeExtensionNoHandOff,
       "pmip6BindingLifeTimeExtensionAfterHandOff": pmip6BindingLifeTimeExtensionAfterHandOff,
       "pmip6BindingDeRegistrations": pmip6BindingDeRegistrations,
       "pmip6BindingBindingAcks": pmip6BindingBindingAcks,
       "pmip6CounterDiscontinuityTime": pmip6CounterDiscontinuityTime,
       "pmip6Mag": pmip6Mag,
       "pmip6MagSystem": pmip6MagSystem,
       "pmip6MagStatus": pmip6MagStatus,
       "pmip6MagProxyCOATable": pmip6MagProxyCOATable,
       "pmip6MagProxyCOAEntry": pmip6MagProxyCOAEntry,
       "pmip6MagProxyCOAType": pmip6MagProxyCOAType,
       "pmip6MagProxyCOA": pmip6MagProxyCOA,
       "pmip6MagProxyCOAState": pmip6MagProxyCOAState,
       "pmip6MagConf": pmip6MagConf,
       "pmip6MagEnableMagLocalRouting": pmip6MagEnableMagLocalRouting,
       "pmip6MagMnIdentifierTable": pmip6MagMnIdentifierTable,
       "pmip6MagMnIdentifierEntry": pmip6MagMnIdentifierEntry,
       "pmip6MagMnIdentifier": pmip6MagMnIdentifier,
       "pmip6MagMnLLIdentifierTable": pmip6MagMnLLIdentifierTable,
       "pmip6MagMnLLIdentifierEntry": pmip6MagMnLLIdentifierEntry,
       "pmip6MagMnLLIdentifier": pmip6MagMnLLIdentifier,
       "pmip6MagHomeNetworkPrefixTable": pmip6MagHomeNetworkPrefixTable,
       "pmip6MagHomeNetworkPrefixEntry": pmip6MagHomeNetworkPrefixEntry,
       "pmip6MagHomeNetworkPrefixType": pmip6MagHomeNetworkPrefixType,
       "pmip6MagHomeNetworkPrefix": pmip6MagHomeNetworkPrefix,
       "pmip6MagHomeNetworkPrefixLength": pmip6MagHomeNetworkPrefixLength,
       "pmip6MagHomeNetworkPrefixLifeTime": pmip6MagHomeNetworkPrefixLifeTime,
       "pmip6MagRegistration": pmip6MagRegistration,
       "pmip6MagBLTable": pmip6MagBLTable,
       "pmip6MagBLEntry": pmip6MagBLEntry,
       "pmip6MagBLFlag": pmip6MagBLFlag,
       "pmip6MagBLMnIndex": pmip6MagBLMnIndex,
       "pmip6MagBLMnLLIndex": pmip6MagBLMnLLIndex,
       "pmip6MagBLMagLinkLocalAddressType": pmip6MagBLMagLinkLocalAddressType,
       "pmip6MagBLMagLinkLocalAddress": pmip6MagBLMagLinkLocalAddress,
       "pmip6MagBLMagIfIdentifierToMn": pmip6MagBLMagIfIdentifierToMn,
       "pmip6MagBLTunnelIfIdentifier": pmip6MagBLTunnelIfIdentifier,
       "pmip6MagBLMnInterfaceATT": pmip6MagBLMnInterfaceATT,
       "pmip6MagBLTimeRecentlyAccepted": pmip6MagBLTimeRecentlyAccepted,
       "pmip6MagMnProfileTable": pmip6MagMnProfileTable,
       "pmip6MagMnProfileEntry": pmip6MagMnProfileEntry,
       "pmip6MagProfMnIndex": pmip6MagProfMnIndex,
       "pmip6MagProfMnIdentifier": pmip6MagProfMnIdentifier,
       "pmip6MagProfMnLocalMobilityAnchorAddressType": pmip6MagProfMnLocalMobilityAnchorAddressType,
       "pmip6MagProfMnLocalMobilityAnchorAddress": pmip6MagProfMnLocalMobilityAnchorAddress,
       "pmip6Lma": pmip6Lma,
       "pmip6LmaSystem": pmip6LmaSystem,
       "pmip6LmaStatus": pmip6LmaStatus,
       "pmip6LmaLMAATable": pmip6LmaLMAATable,
       "pmip6LmaLMAAEntry": pmip6LmaLMAAEntry,
       "pmip6LmaLMAAType": pmip6LmaLMAAType,
       "pmip6LmaLMAA": pmip6LmaLMAA,
       "pmip6LmaLMAAState": pmip6LmaLMAAState,
       "pmip6LmaConf": pmip6LmaConf,
       "pmip6LmaMinDelayBeforeBCEDelete": pmip6LmaMinDelayBeforeBCEDelete,
       "pmip6LmaMaxDelayBeforeNewBCEAssign": pmip6LmaMaxDelayBeforeNewBCEAssign,
       "pmip6LmaTimestampValidityWindow": pmip6LmaTimestampValidityWindow,
       "pmip6LmaMnIdentifierTable": pmip6LmaMnIdentifierTable,
       "pmip6LmaMnIdentifierEntry": pmip6LmaMnIdentifierEntry,
       "pmip6LmaMnIdentifier": pmip6LmaMnIdentifier,
       "pmip6LmaMnLLIdentifierTable": pmip6LmaMnLLIdentifierTable,
       "pmip6LmaMnLLIdentifierEntry": pmip6LmaMnLLIdentifierEntry,
       "pmip6LmaMnLLIdentifier": pmip6LmaMnLLIdentifier,
       "pmip6LmaHomeNetworkPrefixTable": pmip6LmaHomeNetworkPrefixTable,
       "pmip6LmaHomeNetworkPrefixEntry": pmip6LmaHomeNetworkPrefixEntry,
       "pmip6LmaHomeNetworkPrefixType": pmip6LmaHomeNetworkPrefixType,
       "pmip6LmaHomeNetworkPrefix": pmip6LmaHomeNetworkPrefix,
       "pmip6LmaHomeNetworkPrefixLength": pmip6LmaHomeNetworkPrefixLength,
       "pmip6LmaHomeNetworkPrefixLifeTime": pmip6LmaHomeNetworkPrefixLifeTime,
       "pmip6Conformance": pmip6Conformance,
       "pmip6Groups": pmip6Groups,
       "pmip6SystemGroup": pmip6SystemGroup,
       "pmip6BindingCacheGroup": pmip6BindingCacheGroup,
       "pmip6StatsGroup": pmip6StatsGroup,
       "pmip6MagSystemGroup": pmip6MagSystemGroup,
       "pmip6MagConfigurationGroup": pmip6MagConfigurationGroup,
       "pmip6MagRegistrationGroup": pmip6MagRegistrationGroup,
       "pmip6LmaSystemGroup": pmip6LmaSystemGroup,
       "pmip6LmaConfigurationGroup": pmip6LmaConfigurationGroup,
       "pmip6MagNotificationGroup": pmip6MagNotificationGroup,
       "pmip6LmaNotificationGroup": pmip6LmaNotificationGroup,
       "pmip6Compliances": pmip6Compliances,
       "pmip6CoreCompliance": pmip6CoreCompliance,
       "pmip6Compliance2": pmip6Compliance2,
       "pmip6CoreReadOnlyCompliance": pmip6CoreReadOnlyCompliance,
       "pmip6ReadOnlyCompliance2": pmip6ReadOnlyCompliance2,
       "pmip6MagCoreCompliance": pmip6MagCoreCompliance,
       "pmip6MagCompliance2": pmip6MagCompliance2,
       "pmip6MagCoreReadOnlyCompliance": pmip6MagCoreReadOnlyCompliance,
       "pmip6MagReadOnlyCompliance2": pmip6MagReadOnlyCompliance2,
       "pmip6LmaCoreCompliance": pmip6LmaCoreCompliance,
       "pmip6LmaCompliance2": pmip6LmaCompliance2,
       "pmip6LmaReadOnlyCompliance": pmip6LmaReadOnlyCompliance,
       "pmip6LmaReadOnlyCompliance2": pmip6LmaReadOnlyCompliance2,
       "pmip6MagNotificationCompliance": pmip6MagNotificationCompliance,
       "pmip6LmaNotificationCompliance": pmip6LmaNotificationCompliance}
)
