# SNMP MIB module (NEMO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NEMO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:20 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(mip6BindingCacheEntry,
 mip6BindingHomeAddress,
 mip6BindingHomeAddressType,
 mip6MnBLCOA,
 mip6MnBLCOAType,
 mip6MnBLEntry) = mibBuilder.importSymbols(
    "MOBILEIPV6-MIB",
    "mip6BindingCacheEntry",
    "mip6BindingHomeAddress",
    "mip6BindingHomeAddressType",
    "mip6MnBLCOA",
    "mip6MnBLCOAType",
    "mip6MnBLEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

nemoMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 184)
)
nemoMIB.setRevisions(
        ("2009-03-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class NemoBURequestRejectionCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(140,
              141,
              142,
              143)
        )
    )
    namedValues = NamedValues(
        *(("forwardingSetupFailed", 143),
          ("invalidPrefix", 141),
          ("mobileRouterOperationNotPermitted", 140),
          ("notAuthorizedForPrefix", 142))
    )



# MIB Managed Objects in the order of their OIDs

_NemoNotifications_ObjectIdentity = ObjectIdentity
nemoNotifications = _NemoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 0)
)
_NemoObjects_ObjectIdentity = ObjectIdentity
nemoObjects = _NemoObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1)
)
_NemoCore_ObjectIdentity = ObjectIdentity
nemoCore = _NemoCore_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 1)
)
_NemoSystem_ObjectIdentity = ObjectIdentity
nemoSystem = _NemoSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 1)
)


class _NemoCapabilities_Type(Bits):
    """Custom type nemoCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("homeAgentSupport", 1),
          ("mobileRouter", 0))
    )

_NemoCapabilities_Type.__name__ = "Bits"
_NemoCapabilities_Object = MibScalar
nemoCapabilities = _NemoCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 1, 1),
    _NemoCapabilities_Type()
)
nemoCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoCapabilities.setStatus("current")


class _NemoStatus_Type(Integer32):
    """Custom type nemoStatus based on Integer32"""
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


_NemoStatus_Type.__name__ = "Integer32"
_NemoStatus_Object = MibScalar
nemoStatus = _NemoStatus_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 1, 2),
    _NemoStatus_Type()
)
nemoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nemoStatus.setStatus("current")
_NemoBindings_ObjectIdentity = ObjectIdentity
nemoBindings = _NemoBindings_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 2)
)
_NemoBindingCacheTable_Object = MibTable
nemoBindingCacheTable = _NemoBindingCacheTable_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    nemoBindingCacheTable.setStatus("current")
_NemoBindingCacheEntry_Object = MibTableRow
nemoBindingCacheEntry = _NemoBindingCacheEntry_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nemoBindingCacheEntry.setStatus("current")
_NemoBindingMrFlag_Type = TruthValue
_NemoBindingMrFlag_Object = MibTableColumn
nemoBindingMrFlag = _NemoBindingMrFlag_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 2, 1, 1, 1),
    _NemoBindingMrFlag_Type()
)
nemoBindingMrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoBindingMrFlag.setStatus("current")


class _NemoBindingMrMode_Type(Integer32):
    """Custom type nemoBindingMrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicitMode", 2),
          ("implicitMode", 1))
    )


_NemoBindingMrMode_Type.__name__ = "Integer32"
_NemoBindingMrMode_Object = MibTableColumn
nemoBindingMrMode = _NemoBindingMrMode_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 2, 1, 1, 2),
    _NemoBindingMrMode_Type()
)
nemoBindingMrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoBindingMrMode.setStatus("current")
_NemoConfiguration_ObjectIdentity = ObjectIdentity
nemoConfiguration = _NemoConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 3)
)
_NemoStats_ObjectIdentity = ObjectIdentity
nemoStats = _NemoStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 4)
)
_NemoCounterDiscontinuityTime_Type = TimeStamp
_NemoCounterDiscontinuityTime_Object = MibScalar
nemoCounterDiscontinuityTime = _NemoCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 1, 4, 1),
    _NemoCounterDiscontinuityTime_Type()
)
nemoCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoCounterDiscontinuityTime.setStatus("current")
_NemoMr_ObjectIdentity = ObjectIdentity
nemoMr = _NemoMr_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 2)
)
_NemoMrSystem_ObjectIdentity = ObjectIdentity
nemoMrSystem = _NemoMrSystem_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 1)
)
_NemoMrEgressIfTable_Object = MibTable
nemoMrEgressIfTable = _NemoMrEgressIfTable_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    nemoMrEgressIfTable.setStatus("current")
_NemoMrEgressIfEntry_Object = MibTableRow
nemoMrEgressIfEntry = _NemoMrEgressIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 1, 1, 1)
)
nemoMrEgressIfEntry.setIndexNames(
    (0, "NEMO-MIB", "nemoMrEgressIfIndex"),
)
if mibBuilder.loadTexts:
    nemoMrEgressIfEntry.setStatus("current")
_NemoMrEgressIfIndex_Type = InterfaceIndex
_NemoMrEgressIfIndex_Object = MibTableColumn
nemoMrEgressIfIndex = _NemoMrEgressIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 1, 1, 1, 1),
    _NemoMrEgressIfIndex_Type()
)
nemoMrEgressIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nemoMrEgressIfIndex.setStatus("current")


class _NemoMrEgressIfPriority_Type(Unsigned32):
    """Custom type nemoMrEgressIfPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NemoMrEgressIfPriority_Type.__name__ = "Unsigned32"
_NemoMrEgressIfPriority_Object = MibTableColumn
nemoMrEgressIfPriority = _NemoMrEgressIfPriority_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 1, 1, 1, 2),
    _NemoMrEgressIfPriority_Type()
)
nemoMrEgressIfPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrEgressIfPriority.setStatus("current")
_NemoMrEgressIfDescription_Type = SnmpAdminString
_NemoMrEgressIfDescription_Object = MibTableColumn
nemoMrEgressIfDescription = _NemoMrEgressIfDescription_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 1, 1, 1, 3),
    _NemoMrEgressIfDescription_Type()
)
nemoMrEgressIfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrEgressIfDescription.setStatus("current")
_NemoMrEgressIfRoamHoldDownTime_Type = Gauge32
_NemoMrEgressIfRoamHoldDownTime_Object = MibTableColumn
nemoMrEgressIfRoamHoldDownTime = _NemoMrEgressIfRoamHoldDownTime_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 1, 1, 1, 4),
    _NemoMrEgressIfRoamHoldDownTime_Type()
)
nemoMrEgressIfRoamHoldDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrEgressIfRoamHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    nemoMrEgressIfRoamHoldDownTime.setUnits("seconds")
_NemoMrConf_ObjectIdentity = ObjectIdentity
nemoMrConf = _NemoMrConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2)
)
_NemoMrDiscoveryRequests_Type = Counter32
_NemoMrDiscoveryRequests_Object = MibScalar
nemoMrDiscoveryRequests = _NemoMrDiscoveryRequests_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2, 1),
    _NemoMrDiscoveryRequests_Type()
)
nemoMrDiscoveryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrDiscoveryRequests.setStatus("current")
_NemoMrDiscoveryReplies_Type = Counter32
_NemoMrDiscoveryReplies_Object = MibScalar
nemoMrDiscoveryReplies = _NemoMrDiscoveryReplies_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2, 2),
    _NemoMrDiscoveryReplies_Type()
)
nemoMrDiscoveryReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrDiscoveryReplies.setStatus("current")
_NemoMrDiscoveryRepliesRouterFlagZero_Type = Counter32
_NemoMrDiscoveryRepliesRouterFlagZero_Object = MibScalar
nemoMrDiscoveryRepliesRouterFlagZero = _NemoMrDiscoveryRepliesRouterFlagZero_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2, 3),
    _NemoMrDiscoveryRepliesRouterFlagZero_Type()
)
nemoMrDiscoveryRepliesRouterFlagZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrDiscoveryRepliesRouterFlagZero.setStatus("current")
_NemoMrMovedHome_Type = Counter32
_NemoMrMovedHome_Object = MibScalar
nemoMrMovedHome = _NemoMrMovedHome_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2, 4),
    _NemoMrMovedHome_Type()
)
nemoMrMovedHome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrMovedHome.setStatus("current")
_NemoMrMovedOutofHome_Type = Counter32
_NemoMrMovedOutofHome_Object = MibScalar
nemoMrMovedOutofHome = _NemoMrMovedOutofHome_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2, 5),
    _NemoMrMovedOutofHome_Type()
)
nemoMrMovedOutofHome.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrMovedOutofHome.setStatus("current")
_NemoMrMovedFNtoFN_Type = Counter32
_NemoMrMovedFNtoFN_Object = MibScalar
nemoMrMovedFNtoFN = _NemoMrMovedFNtoFN_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2, 6),
    _NemoMrMovedFNtoFN_Type()
)
nemoMrMovedFNtoFN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrMovedFNtoFN.setStatus("current")
_NemoMrBetterIfDetected_Type = Counter32
_NemoMrBetterIfDetected_Object = MibScalar
nemoMrBetterIfDetected = _NemoMrBetterIfDetected_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 2, 7),
    _NemoMrBetterIfDetected_Type()
)
nemoMrBetterIfDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBetterIfDetected.setStatus("current")
_NemoMrRegistration_ObjectIdentity = ObjectIdentity
nemoMrRegistration = _NemoMrRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3)
)
_NemoMrBLTable_Object = MibTable
nemoMrBLTable = _NemoMrBLTable_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    nemoMrBLTable.setStatus("current")
_NemoMrBLEntry_Object = MibTableRow
nemoMrBLEntry = _NemoMrBLEntry_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1, 1)
)
if mibBuilder.loadTexts:
    nemoMrBLEntry.setStatus("current")


class _NemoMrBLMode_Type(Integer32):
    """Custom type nemoMrBLMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicitMode", 2),
          ("implicitMode", 1))
    )


_NemoMrBLMode_Type.__name__ = "Integer32"
_NemoMrBLMode_Object = MibTableColumn
nemoMrBLMode = _NemoMrBLMode_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1, 1, 1),
    _NemoMrBLMode_Type()
)
nemoMrBLMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBLMode.setStatus("current")
_NemoMrBLMrFlag_Type = TruthValue
_NemoMrBLMrFlag_Object = MibTableColumn
nemoMrBLMrFlag = _NemoMrBLMrFlag_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1, 1, 2),
    _NemoMrBLMrFlag_Type()
)
nemoMrBLMrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBLMrFlag.setStatus("current")
_NemoMrBLHomeAddressPrefixLength_Type = InetAddressPrefixLength
_NemoMrBLHomeAddressPrefixLength_Object = MibTableColumn
nemoMrBLHomeAddressPrefixLength = _NemoMrBLHomeAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1, 1, 3),
    _NemoMrBLHomeAddressPrefixLength_Type()
)
nemoMrBLHomeAddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBLHomeAddressPrefixLength.setStatus("current")
_NemoMrBLCareofAddressPrefixLength_Type = InetAddressPrefixLength
_NemoMrBLCareofAddressPrefixLength_Object = MibTableColumn
nemoMrBLCareofAddressPrefixLength = _NemoMrBLCareofAddressPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1, 1, 4),
    _NemoMrBLCareofAddressPrefixLength_Type()
)
nemoMrBLCareofAddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBLCareofAddressPrefixLength.setStatus("current")
_NemoMrBLActiveEgressIfIndex_Type = InterfaceIndex
_NemoMrBLActiveEgressIfIndex_Object = MibTableColumn
nemoMrBLActiveEgressIfIndex = _NemoMrBLActiveEgressIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1, 1, 5),
    _NemoMrBLActiveEgressIfIndex_Type()
)
nemoMrBLActiveEgressIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBLActiveEgressIfIndex.setStatus("current")
_NemoMrBLEstablishedHomeTunnelIfIndex_Type = InterfaceIndex
_NemoMrBLEstablishedHomeTunnelIfIndex_Object = MibTableColumn
nemoMrBLEstablishedHomeTunnelIfIndex = _NemoMrBLEstablishedHomeTunnelIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 1, 1, 6),
    _NemoMrBLEstablishedHomeTunnelIfIndex_Type()
)
nemoMrBLEstablishedHomeTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBLEstablishedHomeTunnelIfIndex.setStatus("current")
_NemoMrRegnCounters_ObjectIdentity = ObjectIdentity
nemoMrRegnCounters = _NemoMrRegnCounters_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 2)
)
_NemoMrMobilityMessagesSent_Type = Counter32
_NemoMrMobilityMessagesSent_Object = MibScalar
nemoMrMobilityMessagesSent = _NemoMrMobilityMessagesSent_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 2, 1),
    _NemoMrMobilityMessagesSent_Type()
)
nemoMrMobilityMessagesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrMobilityMessagesSent.setStatus("current")
_NemoMrMobilityMessagesRecd_Type = Counter32
_NemoMrMobilityMessagesRecd_Object = MibScalar
nemoMrMobilityMessagesRecd = _NemoMrMobilityMessagesRecd_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 2, 2),
    _NemoMrMobilityMessagesRecd_Type()
)
nemoMrMobilityMessagesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrMobilityMessagesRecd.setStatus("current")


class _NemoMrPrefixRegMode_Type(Integer32):
    """Custom type nemoMrPrefixRegMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("explicitMode", 2),
          ("implicitMode", 1))
    )


_NemoMrPrefixRegMode_Type.__name__ = "Integer32"
_NemoMrPrefixRegMode_Object = MibScalar
nemoMrPrefixRegMode = _NemoMrPrefixRegMode_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 3, 3),
    _NemoMrPrefixRegMode_Type()
)
nemoMrPrefixRegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nemoMrPrefixRegMode.setStatus("current")
_NemoMrGlobalStats_ObjectIdentity = ObjectIdentity
nemoMrGlobalStats = _NemoMrGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4)
)
_NemoMrBindingAcksWONemoSupport_Type = Counter32
_NemoMrBindingAcksWONemoSupport_Object = MibScalar
nemoMrBindingAcksWONemoSupport = _NemoMrBindingAcksWONemoSupport_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4, 1),
    _NemoMrBindingAcksWONemoSupport_Type()
)
nemoMrBindingAcksWONemoSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBindingAcksWONemoSupport.setStatus("current")
_NemoMrBindingAcksRegTypeChangeDisallowed_Type = Counter32
_NemoMrBindingAcksRegTypeChangeDisallowed_Object = MibScalar
nemoMrBindingAcksRegTypeChangeDisallowed = _NemoMrBindingAcksRegTypeChangeDisallowed_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4, 2),
    _NemoMrBindingAcksRegTypeChangeDisallowed_Type()
)
nemoMrBindingAcksRegTypeChangeDisallowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBindingAcksRegTypeChangeDisallowed.setStatus("current")
_NemoMrBindingAcksOperationNotPermitted_Type = Counter32
_NemoMrBindingAcksOperationNotPermitted_Object = MibScalar
nemoMrBindingAcksOperationNotPermitted = _NemoMrBindingAcksOperationNotPermitted_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4, 3),
    _NemoMrBindingAcksOperationNotPermitted_Type()
)
nemoMrBindingAcksOperationNotPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBindingAcksOperationNotPermitted.setStatus("current")
_NemoMrBindingAcksInvalidPrefix_Type = Counter32
_NemoMrBindingAcksInvalidPrefix_Object = MibScalar
nemoMrBindingAcksInvalidPrefix = _NemoMrBindingAcksInvalidPrefix_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4, 4),
    _NemoMrBindingAcksInvalidPrefix_Type()
)
nemoMrBindingAcksInvalidPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBindingAcksInvalidPrefix.setStatus("current")
_NemoMrBindingAcksNotAuthorizedForPrefix_Type = Counter32
_NemoMrBindingAcksNotAuthorizedForPrefix_Object = MibScalar
nemoMrBindingAcksNotAuthorizedForPrefix = _NemoMrBindingAcksNotAuthorizedForPrefix_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4, 5),
    _NemoMrBindingAcksNotAuthorizedForPrefix_Type()
)
nemoMrBindingAcksNotAuthorizedForPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBindingAcksNotAuthorizedForPrefix.setStatus("current")
_NemoMrBindingAcksForwardingSetupFailed_Type = Counter32
_NemoMrBindingAcksForwardingSetupFailed_Object = MibScalar
nemoMrBindingAcksForwardingSetupFailed = _NemoMrBindingAcksForwardingSetupFailed_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4, 6),
    _NemoMrBindingAcksForwardingSetupFailed_Type()
)
nemoMrBindingAcksForwardingSetupFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBindingAcksForwardingSetupFailed.setStatus("current")
_NemoMrBindingAcksOtherError_Type = Counter32
_NemoMrBindingAcksOtherError_Object = MibScalar
nemoMrBindingAcksOtherError = _NemoMrBindingAcksOtherError_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 2, 4, 7),
    _NemoMrBindingAcksOtherError_Type()
)
nemoMrBindingAcksOtherError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoMrBindingAcksOtherError.setStatus("current")
_NemoCn_ObjectIdentity = ObjectIdentity
nemoCn = _NemoCn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 3)
)
_NemoHa_ObjectIdentity = ObjectIdentity
nemoHa = _NemoHa_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 4)
)
_NemoHaAdvertisement_ObjectIdentity = ObjectIdentity
nemoHaAdvertisement = _NemoHaAdvertisement_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 1)
)
_NemoHaStats_ObjectIdentity = ObjectIdentity
nemoHaStats = _NemoHaStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2)
)
_NemoHaGlobalStats_ObjectIdentity = ObjectIdentity
nemoHaGlobalStats = _NemoHaGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1)
)
_NemoHaBUAcksWONemoSupport_Type = Counter32
_NemoHaBUAcksWONemoSupport_Object = MibScalar
nemoHaBUAcksWONemoSupport = _NemoHaBUAcksWONemoSupport_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1, 1),
    _NemoHaBUAcksWONemoSupport_Type()
)
nemoHaBUAcksWONemoSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcksWONemoSupport.setStatus("current")
_NemoHaBUAcksRegTypeChangeDisallowed_Type = Counter32
_NemoHaBUAcksRegTypeChangeDisallowed_Object = MibScalar
nemoHaBUAcksRegTypeChangeDisallowed = _NemoHaBUAcksRegTypeChangeDisallowed_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1, 2),
    _NemoHaBUAcksRegTypeChangeDisallowed_Type()
)
nemoHaBUAcksRegTypeChangeDisallowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcksRegTypeChangeDisallowed.setStatus("current")
_NemoHaBUAcksOperationNotPermitted_Type = Counter32
_NemoHaBUAcksOperationNotPermitted_Object = MibScalar
nemoHaBUAcksOperationNotPermitted = _NemoHaBUAcksOperationNotPermitted_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1, 3),
    _NemoHaBUAcksOperationNotPermitted_Type()
)
nemoHaBUAcksOperationNotPermitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcksOperationNotPermitted.setStatus("current")
_NemoHaBUAcksInvalidPrefix_Type = Counter32
_NemoHaBUAcksInvalidPrefix_Object = MibScalar
nemoHaBUAcksInvalidPrefix = _NemoHaBUAcksInvalidPrefix_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1, 4),
    _NemoHaBUAcksInvalidPrefix_Type()
)
nemoHaBUAcksInvalidPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcksInvalidPrefix.setStatus("current")
_NemoHaBUAcksNotAuthorizedForPrefix_Type = Counter32
_NemoHaBUAcksNotAuthorizedForPrefix_Object = MibScalar
nemoHaBUAcksNotAuthorizedForPrefix = _NemoHaBUAcksNotAuthorizedForPrefix_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1, 5),
    _NemoHaBUAcksNotAuthorizedForPrefix_Type()
)
nemoHaBUAcksNotAuthorizedForPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcksNotAuthorizedForPrefix.setStatus("current")
_NemoHaBUAcksForwardingSetupFailed_Type = Counter32
_NemoHaBUAcksForwardingSetupFailed_Object = MibScalar
nemoHaBUAcksForwardingSetupFailed = _NemoHaBUAcksForwardingSetupFailed_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1, 6),
    _NemoHaBUAcksForwardingSetupFailed_Type()
)
nemoHaBUAcksForwardingSetupFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcksForwardingSetupFailed.setStatus("current")
_NemoHaBUAcksOtherError_Type = Counter32
_NemoHaBUAcksOtherError_Object = MibScalar
nemoHaBUAcksOtherError = _NemoHaBUAcksOtherError_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 1, 7),
    _NemoHaBUAcksOtherError_Type()
)
nemoHaBUAcksOtherError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcksOtherError.setStatus("current")
_NemoHaCounterTable_Object = MibTable
nemoHaCounterTable = _NemoHaCounterTable_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    nemoHaCounterTable.setStatus("current")
_NemoHaCounterEntry_Object = MibTableRow
nemoHaCounterEntry = _NemoHaCounterEntry_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1)
)
nemoHaCounterEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddress"),
)
if mibBuilder.loadTexts:
    nemoHaCounterEntry.setStatus("current")
_NemoHaBURequestsAccepted_Type = Counter32
_NemoHaBURequestsAccepted_Object = MibTableColumn
nemoHaBURequestsAccepted = _NemoHaBURequestsAccepted_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1, 1),
    _NemoHaBURequestsAccepted_Type()
)
nemoHaBURequestsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBURequestsAccepted.setStatus("current")
_NemoHaBURequestsDenied_Type = Counter32
_NemoHaBURequestsDenied_Object = MibTableColumn
nemoHaBURequestsDenied = _NemoHaBURequestsDenied_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1, 2),
    _NemoHaBURequestsDenied_Type()
)
nemoHaBURequestsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBURequestsDenied.setStatus("current")


class _NemoHaBCEntryCreationTime_Type(DateAndTime):
    """Custom type nemoHaBCEntryCreationTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_NemoHaBCEntryCreationTime_Type.__name__ = "DateAndTime"
_NemoHaBCEntryCreationTime_Object = MibTableColumn
nemoHaBCEntryCreationTime = _NemoHaBCEntryCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1, 3),
    _NemoHaBCEntryCreationTime_Type()
)
nemoHaBCEntryCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBCEntryCreationTime.setStatus("current")


class _NemoHaBUAcceptedTime_Type(DateAndTime):
    """Custom type nemoHaBUAcceptedTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_NemoHaBUAcceptedTime_Type.__name__ = "DateAndTime"
_NemoHaBUAcceptedTime_Object = MibTableColumn
nemoHaBUAcceptedTime = _NemoHaBUAcceptedTime_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1, 4),
    _NemoHaBUAcceptedTime_Type()
)
nemoHaBUAcceptedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBUAcceptedTime.setStatus("current")


class _NemoHaBURejectionTime_Type(DateAndTime):
    """Custom type nemoHaBURejectionTime based on DateAndTime"""
    subtypeSpec = DateAndTime.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_NemoHaBURejectionTime_Type.__name__ = "DateAndTime"
_NemoHaBURejectionTime_Object = MibTableColumn
nemoHaBURejectionTime = _NemoHaBURejectionTime_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1, 5),
    _NemoHaBURejectionTime_Type()
)
nemoHaBURejectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaBURejectionTime.setStatus("current")
_NemoHaRecentBURejectionCode_Type = NemoBURequestRejectionCode
_NemoHaRecentBURejectionCode_Object = MibTableColumn
nemoHaRecentBURejectionCode = _NemoHaRecentBURejectionCode_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1, 6),
    _NemoHaRecentBURejectionCode_Type()
)
nemoHaRecentBURejectionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaRecentBURejectionCode.setStatus("current")
_NemoHaCtrDiscontinuityTime_Type = TimeStamp
_NemoHaCtrDiscontinuityTime_Object = MibTableColumn
nemoHaCtrDiscontinuityTime = _NemoHaCtrDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 2, 2, 1, 7),
    _NemoHaCtrDiscontinuityTime_Type()
)
nemoHaCtrDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaCtrDiscontinuityTime.setStatus("current")
_NemoHaRegistration_ObjectIdentity = ObjectIdentity
nemoHaRegistration = _NemoHaRegistration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3)
)
_NemoHaMobileNetworkPrefixTable_Object = MibTable
nemoHaMobileNetworkPrefixTable = _NemoHaMobileNetworkPrefixTable_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    nemoHaMobileNetworkPrefixTable.setStatus("current")
_NemoHaMobileNetworkPrefixEntry_Object = MibTableRow
nemoHaMobileNetworkPrefixEntry = _NemoHaMobileNetworkPrefixEntry_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3, 1, 1)
)
nemoHaMobileNetworkPrefixEntry.setIndexNames(
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddressType"),
    (0, "MOBILEIPV6-MIB", "mip6BindingHomeAddress"),
    (0, "NEMO-MIB", "nemoHaMobileNetworkPrefixSeqNo"),
)
if mibBuilder.loadTexts:
    nemoHaMobileNetworkPrefixEntry.setStatus("current")


class _NemoHaMobileNetworkPrefixSeqNo_Type(Unsigned32):
    """Custom type nemoHaMobileNetworkPrefixSeqNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_NemoHaMobileNetworkPrefixSeqNo_Type.__name__ = "Unsigned32"
_NemoHaMobileNetworkPrefixSeqNo_Object = MibTableColumn
nemoHaMobileNetworkPrefixSeqNo = _NemoHaMobileNetworkPrefixSeqNo_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3, 1, 1, 1),
    _NemoHaMobileNetworkPrefixSeqNo_Type()
)
nemoHaMobileNetworkPrefixSeqNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nemoHaMobileNetworkPrefixSeqNo.setStatus("current")
_NemoHaMobileNetworkPrefixType_Type = InetAddressType
_NemoHaMobileNetworkPrefixType_Object = MibTableColumn
nemoHaMobileNetworkPrefixType = _NemoHaMobileNetworkPrefixType_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3, 1, 1, 2),
    _NemoHaMobileNetworkPrefixType_Type()
)
nemoHaMobileNetworkPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaMobileNetworkPrefixType.setStatus("current")
_NemoHaMobileNetworkPrefix_Type = InetAddress
_NemoHaMobileNetworkPrefix_Object = MibTableColumn
nemoHaMobileNetworkPrefix = _NemoHaMobileNetworkPrefix_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3, 1, 1, 3),
    _NemoHaMobileNetworkPrefix_Type()
)
nemoHaMobileNetworkPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaMobileNetworkPrefix.setStatus("current")


class _NemoHaMobileNetworkPrefixLength_Type(Unsigned32):
    """Custom type nemoHaMobileNetworkPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_NemoHaMobileNetworkPrefixLength_Type.__name__ = "Unsigned32"
_NemoHaMobileNetworkPrefixLength_Object = MibTableColumn
nemoHaMobileNetworkPrefixLength = _NemoHaMobileNetworkPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3, 1, 1, 4),
    _NemoHaMobileNetworkPrefixLength_Type()
)
nemoHaMobileNetworkPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaMobileNetworkPrefixLength.setStatus("current")


class _NemoHaMobileNetworkPrefixSource_Type(Integer32):
    """Custom type nemoHaMobileNetworkPrefixSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bindingUpdate", 2),
          ("configured", 1))
    )


_NemoHaMobileNetworkPrefixSource_Type.__name__ = "Integer32"
_NemoHaMobileNetworkPrefixSource_Object = MibTableColumn
nemoHaMobileNetworkPrefixSource = _NemoHaMobileNetworkPrefixSource_Object(
    (1, 3, 6, 1, 2, 1, 184, 1, 4, 3, 1, 1, 5),
    _NemoHaMobileNetworkPrefixSource_Type()
)
nemoHaMobileNetworkPrefixSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nemoHaMobileNetworkPrefixSource.setStatus("current")
_NemoConformance_ObjectIdentity = ObjectIdentity
nemoConformance = _NemoConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 2)
)
_NemoGroups_ObjectIdentity = ObjectIdentity
nemoGroups = _NemoGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 2, 1)
)
_NemoCompliances_ObjectIdentity = ObjectIdentity
nemoCompliances = _NemoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 184, 2, 2)
)
mip6BindingCacheEntry.registerAugmentions(
    ("NEMO-MIB",
     "nemoBindingCacheEntry")
)
nemoBindingCacheEntry.setIndexNames(*mip6BindingCacheEntry.getIndexNames())
mip6MnBLEntry.registerAugmentions(
    ("NEMO-MIB",
     "nemoMrBLEntry")
)
nemoMrBLEntry.setIndexNames(*mip6MnBLEntry.getIndexNames())

# Managed Objects groups

nemoSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 1)
)
nemoSystemGroup.setObjects(
      *(("NEMO-MIB", "nemoCapabilities"),
        ("NEMO-MIB", "nemoStatus"))
)
if mibBuilder.loadTexts:
    nemoSystemGroup.setStatus("current")

nemoBindingCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 2)
)
nemoBindingCacheGroup.setObjects(
      *(("NEMO-MIB", "nemoBindingMrFlag"),
        ("NEMO-MIB", "nemoBindingMrMode"))
)
if mibBuilder.loadTexts:
    nemoBindingCacheGroup.setStatus("current")

nemoStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 3)
)
nemoStatsGroup.setObjects(
    ("NEMO-MIB", "nemoCounterDiscontinuityTime")
)
if mibBuilder.loadTexts:
    nemoStatsGroup.setStatus("current")

nemoMrConfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 4)
)
nemoMrConfGroup.setObjects(
      *(("NEMO-MIB", "nemoMrEgressIfPriority"),
        ("NEMO-MIB", "nemoMrEgressIfDescription"),
        ("NEMO-MIB", "nemoMrEgressIfRoamHoldDownTime"),
        ("NEMO-MIB", "nemoMrDiscoveryRequests"),
        ("NEMO-MIB", "nemoMrDiscoveryReplies"),
        ("NEMO-MIB", "nemoMrDiscoveryRepliesRouterFlagZero"),
        ("NEMO-MIB", "nemoMrMovedHome"),
        ("NEMO-MIB", "nemoMrMovedOutofHome"),
        ("NEMO-MIB", "nemoMrMovedFNtoFN"),
        ("NEMO-MIB", "nemoMrBetterIfDetected"))
)
if mibBuilder.loadTexts:
    nemoMrConfGroup.setStatus("current")

nemoMrRegistrationGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 5)
)
nemoMrRegistrationGroup.setObjects(
      *(("NEMO-MIB", "nemoMrBLMode"),
        ("NEMO-MIB", "nemoMrBLMrFlag"),
        ("NEMO-MIB", "nemoMrBLHomeAddressPrefixLength"),
        ("NEMO-MIB", "nemoMrBLCareofAddressPrefixLength"),
        ("NEMO-MIB", "nemoMrBLActiveEgressIfIndex"),
        ("NEMO-MIB", "nemoMrBLEstablishedHomeTunnelIfIndex"),
        ("NEMO-MIB", "nemoMrMobilityMessagesSent"),
        ("NEMO-MIB", "nemoMrMobilityMessagesRecd"),
        ("NEMO-MIB", "nemoMrPrefixRegMode"),
        ("NEMO-MIB", "nemoMrBindingAcksWONemoSupport"),
        ("NEMO-MIB", "nemoMrBindingAcksRegTypeChangeDisallowed"),
        ("NEMO-MIB", "nemoMrBindingAcksOperationNotPermitted"),
        ("NEMO-MIB", "nemoMrBindingAcksInvalidPrefix"),
        ("NEMO-MIB", "nemoMrBindingAcksNotAuthorizedForPrefix"),
        ("NEMO-MIB", "nemoMrBindingAcksForwardingSetupFailed"),
        ("NEMO-MIB", "nemoMrBindingAcksOtherError"))
)
if mibBuilder.loadTexts:
    nemoMrRegistrationGroup.setStatus("current")

nemoHaSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 6)
)
nemoHaSystemGroup.setObjects(
      *(("NEMO-MIB", "nemoHaMobileNetworkPrefixType"),
        ("NEMO-MIB", "nemoHaMobileNetworkPrefix"),
        ("NEMO-MIB", "nemoHaMobileNetworkPrefixLength"),
        ("NEMO-MIB", "nemoHaMobileNetworkPrefixSource"))
)
if mibBuilder.loadTexts:
    nemoHaSystemGroup.setStatus("current")

nemoHaStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 7)
)
nemoHaStatsGroup.setObjects(
      *(("NEMO-MIB", "nemoHaBURequestsAccepted"),
        ("NEMO-MIB", "nemoHaBURequestsDenied"),
        ("NEMO-MIB", "nemoHaBCEntryCreationTime"),
        ("NEMO-MIB", "nemoHaBUAcceptedTime"),
        ("NEMO-MIB", "nemoHaBURejectionTime"),
        ("NEMO-MIB", "nemoHaRecentBURejectionCode"),
        ("NEMO-MIB", "nemoHaCtrDiscontinuityTime"))
)
if mibBuilder.loadTexts:
    nemoHaStatsGroup.setStatus("current")

nemoHaGlobalStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 8)
)
nemoHaGlobalStatsGroup.setObjects(
      *(("NEMO-MIB", "nemoHaBUAcksWONemoSupport"),
        ("NEMO-MIB", "nemoHaBUAcksRegTypeChangeDisallowed"),
        ("NEMO-MIB", "nemoHaBUAcksOperationNotPermitted"),
        ("NEMO-MIB", "nemoHaBUAcksInvalidPrefix"),
        ("NEMO-MIB", "nemoHaBUAcksNotAuthorizedForPrefix"),
        ("NEMO-MIB", "nemoHaBUAcksForwardingSetupFailed"),
        ("NEMO-MIB", "nemoHaBUAcksOtherError"))
)
if mibBuilder.loadTexts:
    nemoHaGlobalStatsGroup.setStatus("current")


# Notification objects

nemoHomeTunnelEstablished = NotificationType(
    (1, 3, 6, 1, 2, 1, 184, 0, 1)
)
nemoHomeTunnelEstablished.setObjects(
      *(("NEMO-MIB", "nemoMrBLActiveEgressIfIndex"),
        ("NEMO-MIB", "nemoMrBLEstablishedHomeTunnelIfIndex"),
        ("MOBILEIPV6-MIB", "mip6MnBLCOAType"),
        ("MOBILEIPV6-MIB", "mip6MnBLCOA"),
        ("NEMO-MIB", "nemoMrBLHomeAddressPrefixLength"),
        ("NEMO-MIB", "nemoMrBLCareofAddressPrefixLength"))
)
if mibBuilder.loadTexts:
    nemoHomeTunnelEstablished.setStatus(
        "current"
    )

nemoHomeTunnelReleased = NotificationType(
    (1, 3, 6, 1, 2, 1, 184, 0, 2)
)
nemoHomeTunnelReleased.setObjects(
      *(("NEMO-MIB", "nemoMrBLActiveEgressIfIndex"),
        ("NEMO-MIB", "nemoMrBLEstablishedHomeTunnelIfIndex"),
        ("MOBILEIPV6-MIB", "mip6MnBLCOAType"),
        ("MOBILEIPV6-MIB", "mip6MnBLCOA"),
        ("NEMO-MIB", "nemoMrBLHomeAddressPrefixLength"),
        ("NEMO-MIB", "nemoMrBLCareofAddressPrefixLength"))
)
if mibBuilder.loadTexts:
    nemoHomeTunnelReleased.setStatus(
        "current"
    )


# Notifications groups

nemoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 184, 2, 1, 9)
)
nemoNotificationGroup.setObjects(
      *(("NEMO-MIB", "nemoHomeTunnelEstablished"),
        ("NEMO-MIB", "nemoHomeTunnelReleased"))
)
if mibBuilder.loadTexts:
    nemoNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nemoCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 1)
)
if mibBuilder.loadTexts:
    nemoCoreCompliance.setStatus(
        "current"
    )

nemoCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 2)
)
if mibBuilder.loadTexts:
    nemoCompliance2.setStatus(
        "current"
    )

nemoCoreReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 3)
)
if mibBuilder.loadTexts:
    nemoCoreReadOnlyCompliance.setStatus(
        "current"
    )

nemoReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 4)
)
if mibBuilder.loadTexts:
    nemoReadOnlyCompliance2.setStatus(
        "current"
    )

nemoMrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 5)
)
if mibBuilder.loadTexts:
    nemoMrCompliance.setStatus(
        "current"
    )

nemoMrReadOnlyCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 6)
)
if mibBuilder.loadTexts:
    nemoMrReadOnlyCompliance2.setStatus(
        "current"
    )

nemoHaCoreCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 7)
)
if mibBuilder.loadTexts:
    nemoHaCoreCompliance.setStatus(
        "current"
    )

nemoHaCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 8)
)
if mibBuilder.loadTexts:
    nemoHaCompliance2.setStatus(
        "current"
    )

nemoNotificationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 184, 2, 2, 9)
)
if mibBuilder.loadTexts:
    nemoNotificationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEMO-MIB",
    **{"NemoBURequestRejectionCode": NemoBURequestRejectionCode,
       "nemoMIB": nemoMIB,
       "nemoNotifications": nemoNotifications,
       "nemoHomeTunnelEstablished": nemoHomeTunnelEstablished,
       "nemoHomeTunnelReleased": nemoHomeTunnelReleased,
       "nemoObjects": nemoObjects,
       "nemoCore": nemoCore,
       "nemoSystem": nemoSystem,
       "nemoCapabilities": nemoCapabilities,
       "nemoStatus": nemoStatus,
       "nemoBindings": nemoBindings,
       "nemoBindingCacheTable": nemoBindingCacheTable,
       "nemoBindingCacheEntry": nemoBindingCacheEntry,
       "nemoBindingMrFlag": nemoBindingMrFlag,
       "nemoBindingMrMode": nemoBindingMrMode,
       "nemoConfiguration": nemoConfiguration,
       "nemoStats": nemoStats,
       "nemoCounterDiscontinuityTime": nemoCounterDiscontinuityTime,
       "nemoMr": nemoMr,
       "nemoMrSystem": nemoMrSystem,
       "nemoMrEgressIfTable": nemoMrEgressIfTable,
       "nemoMrEgressIfEntry": nemoMrEgressIfEntry,
       "nemoMrEgressIfIndex": nemoMrEgressIfIndex,
       "nemoMrEgressIfPriority": nemoMrEgressIfPriority,
       "nemoMrEgressIfDescription": nemoMrEgressIfDescription,
       "nemoMrEgressIfRoamHoldDownTime": nemoMrEgressIfRoamHoldDownTime,
       "nemoMrConf": nemoMrConf,
       "nemoMrDiscoveryRequests": nemoMrDiscoveryRequests,
       "nemoMrDiscoveryReplies": nemoMrDiscoveryReplies,
       "nemoMrDiscoveryRepliesRouterFlagZero": nemoMrDiscoveryRepliesRouterFlagZero,
       "nemoMrMovedHome": nemoMrMovedHome,
       "nemoMrMovedOutofHome": nemoMrMovedOutofHome,
       "nemoMrMovedFNtoFN": nemoMrMovedFNtoFN,
       "nemoMrBetterIfDetected": nemoMrBetterIfDetected,
       "nemoMrRegistration": nemoMrRegistration,
       "nemoMrBLTable": nemoMrBLTable,
       "nemoMrBLEntry": nemoMrBLEntry,
       "nemoMrBLMode": nemoMrBLMode,
       "nemoMrBLMrFlag": nemoMrBLMrFlag,
       "nemoMrBLHomeAddressPrefixLength": nemoMrBLHomeAddressPrefixLength,
       "nemoMrBLCareofAddressPrefixLength": nemoMrBLCareofAddressPrefixLength,
       "nemoMrBLActiveEgressIfIndex": nemoMrBLActiveEgressIfIndex,
       "nemoMrBLEstablishedHomeTunnelIfIndex": nemoMrBLEstablishedHomeTunnelIfIndex,
       "nemoMrRegnCounters": nemoMrRegnCounters,
       "nemoMrMobilityMessagesSent": nemoMrMobilityMessagesSent,
       "nemoMrMobilityMessagesRecd": nemoMrMobilityMessagesRecd,
       "nemoMrPrefixRegMode": nemoMrPrefixRegMode,
       "nemoMrGlobalStats": nemoMrGlobalStats,
       "nemoMrBindingAcksWONemoSupport": nemoMrBindingAcksWONemoSupport,
       "nemoMrBindingAcksRegTypeChangeDisallowed": nemoMrBindingAcksRegTypeChangeDisallowed,
       "nemoMrBindingAcksOperationNotPermitted": nemoMrBindingAcksOperationNotPermitted,
       "nemoMrBindingAcksInvalidPrefix": nemoMrBindingAcksInvalidPrefix,
       "nemoMrBindingAcksNotAuthorizedForPrefix": nemoMrBindingAcksNotAuthorizedForPrefix,
       "nemoMrBindingAcksForwardingSetupFailed": nemoMrBindingAcksForwardingSetupFailed,
       "nemoMrBindingAcksOtherError": nemoMrBindingAcksOtherError,
       "nemoCn": nemoCn,
       "nemoHa": nemoHa,
       "nemoHaAdvertisement": nemoHaAdvertisement,
       "nemoHaStats": nemoHaStats,
       "nemoHaGlobalStats": nemoHaGlobalStats,
       "nemoHaBUAcksWONemoSupport": nemoHaBUAcksWONemoSupport,
       "nemoHaBUAcksRegTypeChangeDisallowed": nemoHaBUAcksRegTypeChangeDisallowed,
       "nemoHaBUAcksOperationNotPermitted": nemoHaBUAcksOperationNotPermitted,
       "nemoHaBUAcksInvalidPrefix": nemoHaBUAcksInvalidPrefix,
       "nemoHaBUAcksNotAuthorizedForPrefix": nemoHaBUAcksNotAuthorizedForPrefix,
       "nemoHaBUAcksForwardingSetupFailed": nemoHaBUAcksForwardingSetupFailed,
       "nemoHaBUAcksOtherError": nemoHaBUAcksOtherError,
       "nemoHaCounterTable": nemoHaCounterTable,
       "nemoHaCounterEntry": nemoHaCounterEntry,
       "nemoHaBURequestsAccepted": nemoHaBURequestsAccepted,
       "nemoHaBURequestsDenied": nemoHaBURequestsDenied,
       "nemoHaBCEntryCreationTime": nemoHaBCEntryCreationTime,
       "nemoHaBUAcceptedTime": nemoHaBUAcceptedTime,
       "nemoHaBURejectionTime": nemoHaBURejectionTime,
       "nemoHaRecentBURejectionCode": nemoHaRecentBURejectionCode,
       "nemoHaCtrDiscontinuityTime": nemoHaCtrDiscontinuityTime,
       "nemoHaRegistration": nemoHaRegistration,
       "nemoHaMobileNetworkPrefixTable": nemoHaMobileNetworkPrefixTable,
       "nemoHaMobileNetworkPrefixEntry": nemoHaMobileNetworkPrefixEntry,
       "nemoHaMobileNetworkPrefixSeqNo": nemoHaMobileNetworkPrefixSeqNo,
       "nemoHaMobileNetworkPrefixType": nemoHaMobileNetworkPrefixType,
       "nemoHaMobileNetworkPrefix": nemoHaMobileNetworkPrefix,
       "nemoHaMobileNetworkPrefixLength": nemoHaMobileNetworkPrefixLength,
       "nemoHaMobileNetworkPrefixSource": nemoHaMobileNetworkPrefixSource,
       "nemoConformance": nemoConformance,
       "nemoGroups": nemoGroups,
       "nemoSystemGroup": nemoSystemGroup,
       "nemoBindingCacheGroup": nemoBindingCacheGroup,
       "nemoStatsGroup": nemoStatsGroup,
       "nemoMrConfGroup": nemoMrConfGroup,
       "nemoMrRegistrationGroup": nemoMrRegistrationGroup,
       "nemoHaSystemGroup": nemoHaSystemGroup,
       "nemoHaStatsGroup": nemoHaStatsGroup,
       "nemoHaGlobalStatsGroup": nemoHaGlobalStatsGroup,
       "nemoNotificationGroup": nemoNotificationGroup,
       "nemoCompliances": nemoCompliances,
       "nemoCoreCompliance": nemoCoreCompliance,
       "nemoCompliance2": nemoCompliance2,
       "nemoCoreReadOnlyCompliance": nemoCoreReadOnlyCompliance,
       "nemoReadOnlyCompliance2": nemoReadOnlyCompliance2,
       "nemoMrCompliance": nemoMrCompliance,
       "nemoMrReadOnlyCompliance2": nemoMrReadOnlyCompliance2,
       "nemoHaCoreCompliance": nemoHaCoreCompliance,
       "nemoHaCompliance2": nemoHaCompliance2,
       "nemoNotificationCompliance": nemoNotificationCompliance}
)
