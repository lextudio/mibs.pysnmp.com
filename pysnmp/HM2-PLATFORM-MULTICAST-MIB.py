# SNMP MIB module (HM2-PLATFORM-MULTICAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-MULTICAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:12 2024
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

(HmEnabledStatus,
 hm2PlatformMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2PlatformMibs")

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

(mgmdHostCacheAddress,
 mgmdHostCacheAddressType,
 mgmdHostCacheIfIndex,
 mgmdHostInterfaceIfIndex,
 mgmdHostInterfaceQuerierType) = mibBuilder.importSymbols(
    "MGMD-STD-MIB",
    "mgmdHostCacheAddress",
    "mgmdHostCacheAddressType",
    "mgmdHostCacheIfIndex",
    "mgmdHostInterfaceIfIndex",
    "mgmdHostInterfaceQuerierType")

(pimBsrCandidateBSREntry,) = mibBuilder.importSymbols(
    "PIM-BSR-MIB",
    "pimBsrCandidateBSREntry")

(PimGroupMappingOriginType,) = mibBuilder.importSymbols(
    "PIM-STD-MIB",
    "PimGroupMappingOriginType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hm2PlatformMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4)
)
hm2PlatformMulticast.setRevisions(
        ("2013-07-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentMulticastIGMPConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastIGMPConfigGroup = _Hm2AgentMulticastIGMPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 1)
)


class _Hm2AgentMulticastIGMPAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentMulticastIGMPAdminMode based on HmEnabledStatus"""


_Hm2AgentMulticastIGMPAdminMode_Object = MibScalar
hm2AgentMulticastIGMPAdminMode = _Hm2AgentMulticastIGMPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 1, 1),
    _Hm2AgentMulticastIGMPAdminMode_Type()
)
hm2AgentMulticastIGMPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastIGMPAdminMode.setStatus("current")
_Hm2AgentMulticastIGMPProxyOperStatus_Type = HmEnabledStatus
_Hm2AgentMulticastIGMPProxyOperStatus_Object = MibScalar
hm2AgentMulticastIGMPProxyOperStatus = _Hm2AgentMulticastIGMPProxyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 1, 249),
    _Hm2AgentMulticastIGMPProxyOperStatus_Type()
)
hm2AgentMulticastIGMPProxyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastIGMPProxyOperStatus.setStatus("current")
_Hm2AgentMulticastPIMSMConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastPIMSMConfigGroup = _Hm2AgentMulticastPIMSMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3)
)


class _Hm2AgentMulticastPIMSMAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentMulticastPIMSMAdminMode based on HmEnabledStatus"""


_Hm2AgentMulticastPIMSMAdminMode_Object = MibScalar
hm2AgentMulticastPIMSMAdminMode = _Hm2AgentMulticastPIMSMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 1),
    _Hm2AgentMulticastPIMSMAdminMode_Type()
)
hm2AgentMulticastPIMSMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMAdminMode.setStatus("current")
_Hm2AgentPIMBsrCandidateConfTable_Object = MibTable
hm2AgentPIMBsrCandidateConfTable = _Hm2AgentPIMBsrCandidateConfTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 4)
)
if mibBuilder.loadTexts:
    hm2AgentPIMBsrCandidateConfTable.setStatus("current")
_Hm2AgentPIMBsrCandidateConfEntry_Object = MibTableRow
hm2AgentPIMBsrCandidateConfEntry = _Hm2AgentPIMBsrCandidateConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 4, 1)
)
if mibBuilder.loadTexts:
    hm2AgentPIMBsrCandidateConfEntry.setStatus("current")


class _PimBsrCandidateBSRAdvInterval_Type(Unsigned32):
    """Custom type pimBsrCandidateBSRAdvInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16383),
    )


_PimBsrCandidateBSRAdvInterval_Type.__name__ = "Unsigned32"
_PimBsrCandidateBSRAdvInterval_Object = MibTableColumn
pimBsrCandidateBSRAdvInterval = _PimBsrCandidateBSRAdvInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 4, 1, 1),
    _PimBsrCandidateBSRAdvInterval_Type()
)
pimBsrCandidateBSRAdvInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pimBsrCandidateBSRAdvInterval.setStatus("current")
_Hm2AgentMulticastPIMSMGroupMappingTable_Object = MibTable
hm2AgentMulticastPIMSMGroupMappingTable = _Hm2AgentMulticastPIMSMGroupMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingTable.setStatus("current")
_Hm2AgentMulticastPIMSMGroupMappingEntry_Object = MibTableRow
hm2AgentMulticastPIMSMGroupMappingEntry = _Hm2AgentMulticastPIMSMGroupMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1)
)
hm2AgentMulticastPIMSMGroupMappingEntry.setIndexNames(
    (0, "HM2-PLATFORM-MULTICAST-MIB", "hm2AgentMulticastPIMSMGroupMappingGrpAddrType"),
    (0, "HM2-PLATFORM-MULTICAST-MIB", "hm2AgentMulticastPIMSMGroupMappingGrpAddr"),
)
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingEntry.setStatus("current")
_Hm2AgentMulticastPIMSMGroupMappingGrpAddrType_Type = InetAddressType
_Hm2AgentMulticastPIMSMGroupMappingGrpAddrType_Object = MibTableColumn
hm2AgentMulticastPIMSMGroupMappingGrpAddrType = _Hm2AgentMulticastPIMSMGroupMappingGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1, 1),
    _Hm2AgentMulticastPIMSMGroupMappingGrpAddrType_Type()
)
hm2AgentMulticastPIMSMGroupMappingGrpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingGrpAddrType.setStatus("current")


class _Hm2AgentMulticastPIMSMGroupMappingGrpAddr_Type(InetAddress):
    """Custom type hm2AgentMulticastPIMSMGroupMappingGrpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Hm2AgentMulticastPIMSMGroupMappingGrpAddr_Type.__name__ = "InetAddress"
_Hm2AgentMulticastPIMSMGroupMappingGrpAddr_Object = MibTableColumn
hm2AgentMulticastPIMSMGroupMappingGrpAddr = _Hm2AgentMulticastPIMSMGroupMappingGrpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1, 2),
    _Hm2AgentMulticastPIMSMGroupMappingGrpAddr_Type()
)
hm2AgentMulticastPIMSMGroupMappingGrpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingGrpAddr.setStatus("current")
_Hm2AgentMulticastPIMSMGroupMappingRPAddrType_Type = InetAddressType
_Hm2AgentMulticastPIMSMGroupMappingRPAddrType_Object = MibTableColumn
hm2AgentMulticastPIMSMGroupMappingRPAddrType = _Hm2AgentMulticastPIMSMGroupMappingRPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1, 3),
    _Hm2AgentMulticastPIMSMGroupMappingRPAddrType_Type()
)
hm2AgentMulticastPIMSMGroupMappingRPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingRPAddrType.setStatus("current")


class _Hm2AgentMulticastPIMSMGroupMappingRPAddr_Type(InetAddress):
    """Custom type hm2AgentMulticastPIMSMGroupMappingRPAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(16, 16),
        ValueSizeConstraint(20, 20),
    )


_Hm2AgentMulticastPIMSMGroupMappingRPAddr_Type.__name__ = "InetAddress"
_Hm2AgentMulticastPIMSMGroupMappingRPAddr_Object = MibTableColumn
hm2AgentMulticastPIMSMGroupMappingRPAddr = _Hm2AgentMulticastPIMSMGroupMappingRPAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1, 4),
    _Hm2AgentMulticastPIMSMGroupMappingRPAddr_Type()
)
hm2AgentMulticastPIMSMGroupMappingRPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingRPAddr.setStatus("current")
_Hm2AgentMulticastPIMSMGroupMappingOrigin_Type = PimGroupMappingOriginType
_Hm2AgentMulticastPIMSMGroupMappingOrigin_Object = MibTableColumn
hm2AgentMulticastPIMSMGroupMappingOrigin = _Hm2AgentMulticastPIMSMGroupMappingOrigin_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1, 5),
    _Hm2AgentMulticastPIMSMGroupMappingOrigin_Type()
)
hm2AgentMulticastPIMSMGroupMappingOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingOrigin.setStatus("current")


class _Hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen_Type(InetAddressPrefixLength):
    """Custom type hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen based on InetAddressPrefixLength"""
    subtypeSpec = InetAddressPrefixLength.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 128),
    )


_Hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_Hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen_Object = MibTableColumn
hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen = _Hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1, 6),
    _Hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen_Type()
)
hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen.setStatus("current")
_Hm2AgentMulticastPIMSMGroupMappingExpiryTime_Type = TimeTicks
_Hm2AgentMulticastPIMSMGroupMappingExpiryTime_Object = MibTableColumn
hm2AgentMulticastPIMSMGroupMappingExpiryTime = _Hm2AgentMulticastPIMSMGroupMappingExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 3, 249, 1, 7),
    _Hm2AgentMulticastPIMSMGroupMappingExpiryTime_Type()
)
hm2AgentMulticastPIMSMGroupMappingExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMSMGroupMappingExpiryTime.setStatus("current")
_Hm2AgentMulticastPIMDMConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastPIMDMConfigGroup = _Hm2AgentMulticastPIMDMConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 4)
)


class _Hm2AgentMulticastPIMDMAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentMulticastPIMDMAdminMode based on HmEnabledStatus"""


_Hm2AgentMulticastPIMDMAdminMode_Object = MibScalar
hm2AgentMulticastPIMDMAdminMode = _Hm2AgentMulticastPIMDMAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 4, 1),
    _Hm2AgentMulticastPIMDMAdminMode_Type()
)
hm2AgentMulticastPIMDMAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMDMAdminMode.setStatus("current")


class _Hm2AgentMulticastPIMDMPruneAssertHoldtime_Type(Unsigned32):
    """Custom type hm2AgentMulticastPIMDMPruneAssertHoldtime based on Unsigned32"""
    defaultValue = 210

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 64800),
    )


_Hm2AgentMulticastPIMDMPruneAssertHoldtime_Type.__name__ = "Unsigned32"
_Hm2AgentMulticastPIMDMPruneAssertHoldtime_Object = MibScalar
hm2AgentMulticastPIMDMPruneAssertHoldtime = _Hm2AgentMulticastPIMDMPruneAssertHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 4, 248),
    _Hm2AgentMulticastPIMDMPruneAssertHoldtime_Type()
)
hm2AgentMulticastPIMDMPruneAssertHoldtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMDMPruneAssertHoldtime.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentMulticastPIMDMPruneAssertHoldtime.setUnits("seconds")
_Hm2AgentMulticastRoutingConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastRoutingConfigGroup = _Hm2AgentMulticastRoutingConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 5)
)


class _Hm2AgentMulticastRoutingAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentMulticastRoutingAdminMode based on HmEnabledStatus"""


_Hm2AgentMulticastRoutingAdminMode_Object = MibScalar
hm2AgentMulticastRoutingAdminMode = _Hm2AgentMulticastRoutingAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 5, 1),
    _Hm2AgentMulticastRoutingAdminMode_Type()
)
hm2AgentMulticastRoutingAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastRoutingAdminMode.setStatus("current")


class _Hm2AgentMulticastSoftwareDSCP_Type(Unsigned32):
    """Custom type hm2AgentMulticastSoftwareDSCP based on Unsigned32"""
    defaultValue = 48

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hm2AgentMulticastSoftwareDSCP_Type.__name__ = "Unsigned32"
_Hm2AgentMulticastSoftwareDSCP_Object = MibScalar
hm2AgentMulticastSoftwareDSCP = _Hm2AgentMulticastSoftwareDSCP_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 5, 248),
    _Hm2AgentMulticastSoftwareDSCP_Type()
)
hm2AgentMulticastSoftwareDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastSoftwareDSCP.setStatus("current")
_Hm2AgentMulticastDVMRPConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastDVMRPConfigGroup = _Hm2AgentMulticastDVMRPConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 6)
)


class _Hm2AgentMulticastDVMRPAdminMode_Type(HmEnabledStatus):
    """Custom type hm2AgentMulticastDVMRPAdminMode based on HmEnabledStatus"""


_Hm2AgentMulticastDVMRPAdminMode_Object = MibScalar
hm2AgentMulticastDVMRPAdminMode = _Hm2AgentMulticastDVMRPAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 6, 1),
    _Hm2AgentMulticastDVMRPAdminMode_Type()
)
hm2AgentMulticastDVMRPAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastDVMRPAdminMode.setStatus("current")


class _Hm2AgentMulticastDVMRPRouteExpiryTime_Type(Unsigned32):
    """Custom type hm2AgentMulticastDVMRPRouteExpiryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_Hm2AgentMulticastDVMRPRouteExpiryTime_Type.__name__ = "Unsigned32"
_Hm2AgentMulticastDVMRPRouteExpiryTime_Object = MibScalar
hm2AgentMulticastDVMRPRouteExpiryTime = _Hm2AgentMulticastDVMRPRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 6, 248),
    _Hm2AgentMulticastDVMRPRouteExpiryTime_Type()
)
hm2AgentMulticastDVMRPRouteExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastDVMRPRouteExpiryTime.setStatus("current")
if mibBuilder.loadTexts:
    hm2AgentMulticastDVMRPRouteExpiryTime.setUnits("seconds")
_Hm2AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity = ObjectIdentity
hm2AgentSnmpTrapFlagsConfigGroupMulticast = _Hm2AgentSnmpTrapFlagsConfigGroupMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 7)
)


class _Hm2AgentSnmpDVMRPTrapFlag_Type(HmEnabledStatus):
    """Custom type hm2AgentSnmpDVMRPTrapFlag based on HmEnabledStatus"""


_Hm2AgentSnmpDVMRPTrapFlag_Object = MibScalar
hm2AgentSnmpDVMRPTrapFlag = _Hm2AgentSnmpDVMRPTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 7, 1),
    _Hm2AgentSnmpDVMRPTrapFlag_Type()
)
hm2AgentSnmpDVMRPTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSnmpDVMRPTrapFlag.setStatus("current")


class _Hm2AgentSnmpPIMTrapFlag_Type(HmEnabledStatus):
    """Custom type hm2AgentSnmpPIMTrapFlag based on HmEnabledStatus"""


_Hm2AgentSnmpPIMTrapFlag_Object = MibScalar
hm2AgentSnmpPIMTrapFlag = _Hm2AgentSnmpPIMTrapFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 7, 2),
    _Hm2AgentSnmpPIMTrapFlag_Type()
)
hm2AgentSnmpPIMTrapFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSnmpPIMTrapFlag.setStatus("current")
_Hm2AgentIpStaticMRouteTable_Object = MibTable
hm2AgentIpStaticMRouteTable = _Hm2AgentIpStaticMRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8)
)
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteTable.setStatus("current")
_Hm2AgentIpStaticMRouteEntry_Object = MibTableRow
hm2AgentIpStaticMRouteEntry = _Hm2AgentIpStaticMRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1)
)
hm2AgentIpStaticMRouteEntry.setIndexNames(
    (0, "HM2-PLATFORM-MULTICAST-MIB", "hm2AgentIpStaticMRouteSrcAddressType"),
    (0, "HM2-PLATFORM-MULTICAST-MIB", "hm2AgentIpStaticMRouteSrcIpAddr"),
    (0, "HM2-PLATFORM-MULTICAST-MIB", "hm2AgentIpStaticMRouteSrcNetMask"),
)
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteEntry.setStatus("current")
_Hm2AgentIpStaticMRouteSrcAddressType_Type = InetAddressType
_Hm2AgentIpStaticMRouteSrcAddressType_Object = MibTableColumn
hm2AgentIpStaticMRouteSrcAddressType = _Hm2AgentIpStaticMRouteSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 1),
    _Hm2AgentIpStaticMRouteSrcAddressType_Type()
)
hm2AgentIpStaticMRouteSrcAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteSrcAddressType.setStatus("current")


class _Hm2AgentIpStaticMRouteSrcIpAddr_Type(InetAddress):
    """Custom type hm2AgentIpStaticMRouteSrcIpAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_Hm2AgentIpStaticMRouteSrcIpAddr_Type.__name__ = "InetAddress"
_Hm2AgentIpStaticMRouteSrcIpAddr_Object = MibTableColumn
hm2AgentIpStaticMRouteSrcIpAddr = _Hm2AgentIpStaticMRouteSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 2),
    _Hm2AgentIpStaticMRouteSrcIpAddr_Type()
)
hm2AgentIpStaticMRouteSrcIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteSrcIpAddr.setStatus("current")


class _Hm2AgentIpStaticMRouteSrcNetMask_Type(Integer32):
    """Custom type hm2AgentIpStaticMRouteSrcNetMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Hm2AgentIpStaticMRouteSrcNetMask_Type.__name__ = "Integer32"
_Hm2AgentIpStaticMRouteSrcNetMask_Object = MibTableColumn
hm2AgentIpStaticMRouteSrcNetMask = _Hm2AgentIpStaticMRouteSrcNetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 3),
    _Hm2AgentIpStaticMRouteSrcNetMask_Type()
)
hm2AgentIpStaticMRouteSrcNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteSrcNetMask.setStatus("current")
_Hm2AgentIpStaticMRouteRpfIpAddr_Type = InetAddress
_Hm2AgentIpStaticMRouteRpfIpAddr_Object = MibTableColumn
hm2AgentIpStaticMRouteRpfIpAddr = _Hm2AgentIpStaticMRouteRpfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 4),
    _Hm2AgentIpStaticMRouteRpfIpAddr_Type()
)
hm2AgentIpStaticMRouteRpfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteRpfIpAddr.setStatus("deprecated")
_Hm2AgentIpStaticMRouteIfIndex_Type = InterfaceIndex
_Hm2AgentIpStaticMRouteIfIndex_Object = MibTableColumn
hm2AgentIpStaticMRouteIfIndex = _Hm2AgentIpStaticMRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 5),
    _Hm2AgentIpStaticMRouteIfIndex_Type()
)
hm2AgentIpStaticMRouteIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteIfIndex.setStatus("current")


class _Hm2AgentIpStaticMRoutePreference_Type(Integer32):
    """Custom type hm2AgentIpStaticMRoutePreference based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hm2AgentIpStaticMRoutePreference_Type.__name__ = "Integer32"
_Hm2AgentIpStaticMRoutePreference_Object = MibTableColumn
hm2AgentIpStaticMRoutePreference = _Hm2AgentIpStaticMRoutePreference_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 6),
    _Hm2AgentIpStaticMRoutePreference_Type()
)
hm2AgentIpStaticMRoutePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRoutePreference.setStatus("current")
_Hm2AgentIpStaticMRouteStatus_Type = RowStatus
_Hm2AgentIpStaticMRouteStatus_Object = MibTableColumn
hm2AgentIpStaticMRouteStatus = _Hm2AgentIpStaticMRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 7),
    _Hm2AgentIpStaticMRouteStatus_Type()
)
hm2AgentIpStaticMRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteStatus.setStatus("current")
_Hm2AgentIpStaticMRouteExtRpfIpAddrType_Type = InetAddressType
_Hm2AgentIpStaticMRouteExtRpfIpAddrType_Object = MibTableColumn
hm2AgentIpStaticMRouteExtRpfIpAddrType = _Hm2AgentIpStaticMRouteExtRpfIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 248),
    _Hm2AgentIpStaticMRouteExtRpfIpAddrType_Type()
)
hm2AgentIpStaticMRouteExtRpfIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteExtRpfIpAddrType.setStatus("current")
_Hm2AgentIpStaticMRouteExtRpfIpAddr_Type = InetAddress
_Hm2AgentIpStaticMRouteExtRpfIpAddr_Object = MibTableColumn
hm2AgentIpStaticMRouteExtRpfIpAddr = _Hm2AgentIpStaticMRouteExtRpfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 8, 1, 249),
    _Hm2AgentIpStaticMRouteExtRpfIpAddr_Type()
)
hm2AgentIpStaticMRouteExtRpfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hm2AgentIpStaticMRouteExtRpfIpAddr.setStatus("current")
_Hm2AgentMulticastMgmdExtConfigGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastMgmdExtConfigGroup = _Hm2AgentMulticastMgmdExtConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 250)
)
_Hm2AgentMulticastMgmdExtTable_Object = MibTable
hm2AgentMulticastMgmdExtTable = _Hm2AgentMulticastMgmdExtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 250, 10)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastMgmdExtTable.setStatus("current")
_Hm2AgentMulticastMgmdExtEntry_Object = MibTableRow
hm2AgentMulticastMgmdExtEntry = _Hm2AgentMulticastMgmdExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 250, 10, 1)
)
hm2AgentMulticastMgmdExtEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdHostInterfaceIfIndex"),
    (0, "MGMD-STD-MIB", "mgmdHostInterfaceQuerierType"),
)
if mibBuilder.loadTexts:
    hm2AgentMulticastMgmdExtEntry.setStatus("current")


class _Hm2AgentMulticastMgmdUnsolicitRprtInterval_Type(Unsigned32):
    """Custom type hm2AgentMulticastMgmdUnsolicitRprtInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 260),
    )


_Hm2AgentMulticastMgmdUnsolicitRprtInterval_Type.__name__ = "Unsigned32"
_Hm2AgentMulticastMgmdUnsolicitRprtInterval_Object = MibTableColumn
hm2AgentMulticastMgmdUnsolicitRprtInterval = _Hm2AgentMulticastMgmdUnsolicitRprtInterval_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 250, 10, 1, 1),
    _Hm2AgentMulticastMgmdUnsolicitRprtInterval_Type()
)
hm2AgentMulticastMgmdUnsolicitRprtInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentMulticastMgmdUnsolicitRprtInterval.setStatus("current")
_Hm2AgentMulticastMgmdNumberOfGroups_Type = Integer32
_Hm2AgentMulticastMgmdNumberOfGroups_Object = MibTableColumn
hm2AgentMulticastMgmdNumberOfGroups = _Hm2AgentMulticastMgmdNumberOfGroups_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 250, 10, 1, 2),
    _Hm2AgentMulticastMgmdNumberOfGroups_Type()
)
hm2AgentMulticastMgmdNumberOfGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastMgmdNumberOfGroups.setStatus("current")
_Hm2AgentMulticastMgmdHostCacheExtGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastMgmdHostCacheExtGroup = _Hm2AgentMulticastMgmdHostCacheExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 251)
)
_Hm2AgentMulticastMgmdHostCacheExtTable_Object = MibTable
hm2AgentMulticastMgmdHostCacheExtTable = _Hm2AgentMulticastMgmdHostCacheExtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 251, 10)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastMgmdHostCacheExtTable.setStatus("current")
_Hm2AgentMulticastMgmdHostCacheExtEntry_Object = MibTableRow
hm2AgentMulticastMgmdHostCacheExtEntry = _Hm2AgentMulticastMgmdHostCacheExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 251, 10, 1)
)
hm2AgentMulticastMgmdHostCacheExtEntry.setIndexNames(
    (0, "MGMD-STD-MIB", "mgmdHostCacheAddressType"),
    (0, "MGMD-STD-MIB", "mgmdHostCacheAddress"),
    (0, "MGMD-STD-MIB", "mgmdHostCacheIfIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentMulticastMgmdHostCacheExtEntry.setStatus("current")


class _Hm2AgentMulticastMgmdHostStatus_Type(Integer32):
    """Custom type hm2AgentMulticastMgmdHostStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delay-member", 2),
          ("idle-member", 3),
          ("non-member", 1))
    )


_Hm2AgentMulticastMgmdHostStatus_Type.__name__ = "Integer32"
_Hm2AgentMulticastMgmdHostStatus_Object = MibTableColumn
hm2AgentMulticastMgmdHostStatus = _Hm2AgentMulticastMgmdHostStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 251, 10, 1, 1),
    _Hm2AgentMulticastMgmdHostStatus_Type()
)
hm2AgentMulticastMgmdHostStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentMulticastMgmdHostStatus.setStatus("current")
_Hm2AgentMulticastSNMPExtensionGroup_ObjectIdentity = ObjectIdentity
hm2AgentMulticastSNMPExtensionGroup = _Hm2AgentMulticastSNMPExtensionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260)
)
_Hm2AgentMulticastProtocolEnableErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastProtocolEnableErrorReturn = _Hm2AgentMulticastProtocolEnableErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 1)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastProtocolEnableErrorReturn.setStatus("current")
_Hm2AgentMulticastNullGroupErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastNullGroupErrorReturn = _Hm2AgentMulticastNullGroupErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 2)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastNullGroupErrorReturn.setStatus("current")
_Hm2AgentMulticastBoundaryRangeEntriesErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastBoundaryRangeEntriesErrorReturn = _Hm2AgentMulticastBoundaryRangeEntriesErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 3)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastBoundaryRangeEntriesErrorReturn.setStatus("current")
_Hm2AgentMulticastHostEntriesErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastHostEntriesErrorReturn = _Hm2AgentMulticastHostEntriesErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 4)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastHostEntriesErrorReturn.setStatus("current")
_Hm2AgentMgmdHostInvalidEntryErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMgmdHostInvalidEntryErrorReturn = _Hm2AgentMgmdHostInvalidEntryErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 5)
)
if mibBuilder.loadTexts:
    hm2AgentMgmdHostInvalidEntryErrorReturn.setStatus("current")
_Hm2AgentMulticastProtocolDeInitErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastProtocolDeInitErrorReturn = _Hm2AgentMulticastProtocolDeInitErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 6)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastProtocolDeInitErrorReturn.setStatus("current")
_Hm2AgentMulticastLocalAddressErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastLocalAddressErrorReturn = _Hm2AgentMulticastLocalAddressErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 7)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastLocalAddressErrorReturn.setStatus("current")
_Hm2AgentMulticastCandRPErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastCandRPErrorReturn = _Hm2AgentMulticastCandRPErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 8)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastCandRPErrorReturn.setStatus("current")
_Hm2AgentMulticastUnicastValidationErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastUnicastValidationErrorReturn = _Hm2AgentMulticastUnicastValidationErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 9)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastUnicastValidationErrorReturn.setStatus("current")
_Hm2AgentMulticastGroupValidationErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastGroupValidationErrorReturn = _Hm2AgentMulticastGroupValidationErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 10)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastGroupValidationErrorReturn.setStatus("current")
_Hm2AgentMulticastSSMValidationErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastSSMValidationErrorReturn = _Hm2AgentMulticastSSMValidationErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 11)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastSSMValidationErrorReturn.setStatus("current")
_Hm2AgentMulticastStaticSourceErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastStaticSourceErrorReturn = _Hm2AgentMulticastStaticSourceErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 12)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastStaticSourceErrorReturn.setStatus("current")
_Hm2AgentMulticastStaticRPFErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastStaticRPFErrorReturn = _Hm2AgentMulticastStaticRPFErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 13)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastStaticRPFErrorReturn.setStatus("current")
_Hm2AgentMulticastStaticHostErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastStaticHostErrorReturn = _Hm2AgentMulticastStaticHostErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 14)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastStaticHostErrorReturn.setStatus("current")
_Hm2AgentMulticastCandRPPrimaryErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastCandRPPrimaryErrorReturn = _Hm2AgentMulticastCandRPPrimaryErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 15)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastCandRPPrimaryErrorReturn.setStatus("current")
_Hm2AgentMulticastCandBSRPrimaryErrorReturn_ObjectIdentity = ObjectIdentity
hm2AgentMulticastCandBSRPrimaryErrorReturn = _Hm2AgentMulticastCandBSRPrimaryErrorReturn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 4, 260, 16)
)
if mibBuilder.loadTexts:
    hm2AgentMulticastCandBSRPrimaryErrorReturn.setStatus("current")
pimBsrCandidateBSREntry.registerAugmentions(
    ("HM2-PLATFORM-MULTICAST-MIB",
     "hm2AgentPIMBsrCandidateConfEntry")
)
hm2AgentPIMBsrCandidateConfEntry.setIndexNames(*pimBsrCandidateBSREntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-MULTICAST-MIB",
    **{"hm2PlatformMulticast": hm2PlatformMulticast,
       "hm2AgentMulticastIGMPConfigGroup": hm2AgentMulticastIGMPConfigGroup,
       "hm2AgentMulticastIGMPAdminMode": hm2AgentMulticastIGMPAdminMode,
       "hm2AgentMulticastIGMPProxyOperStatus": hm2AgentMulticastIGMPProxyOperStatus,
       "hm2AgentMulticastPIMSMConfigGroup": hm2AgentMulticastPIMSMConfigGroup,
       "hm2AgentMulticastPIMSMAdminMode": hm2AgentMulticastPIMSMAdminMode,
       "hm2AgentPIMBsrCandidateConfTable": hm2AgentPIMBsrCandidateConfTable,
       "hm2AgentPIMBsrCandidateConfEntry": hm2AgentPIMBsrCandidateConfEntry,
       "pimBsrCandidateBSRAdvInterval": pimBsrCandidateBSRAdvInterval,
       "hm2AgentMulticastPIMSMGroupMappingTable": hm2AgentMulticastPIMSMGroupMappingTable,
       "hm2AgentMulticastPIMSMGroupMappingEntry": hm2AgentMulticastPIMSMGroupMappingEntry,
       "hm2AgentMulticastPIMSMGroupMappingGrpAddrType": hm2AgentMulticastPIMSMGroupMappingGrpAddrType,
       "hm2AgentMulticastPIMSMGroupMappingGrpAddr": hm2AgentMulticastPIMSMGroupMappingGrpAddr,
       "hm2AgentMulticastPIMSMGroupMappingRPAddrType": hm2AgentMulticastPIMSMGroupMappingRPAddrType,
       "hm2AgentMulticastPIMSMGroupMappingRPAddr": hm2AgentMulticastPIMSMGroupMappingRPAddr,
       "hm2AgentMulticastPIMSMGroupMappingOrigin": hm2AgentMulticastPIMSMGroupMappingOrigin,
       "hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen": hm2AgentMulticastPIMSMGroupMappingGrpPrefixLen,
       "hm2AgentMulticastPIMSMGroupMappingExpiryTime": hm2AgentMulticastPIMSMGroupMappingExpiryTime,
       "hm2AgentMulticastPIMDMConfigGroup": hm2AgentMulticastPIMDMConfigGroup,
       "hm2AgentMulticastPIMDMAdminMode": hm2AgentMulticastPIMDMAdminMode,
       "hm2AgentMulticastPIMDMPruneAssertHoldtime": hm2AgentMulticastPIMDMPruneAssertHoldtime,
       "hm2AgentMulticastRoutingConfigGroup": hm2AgentMulticastRoutingConfigGroup,
       "hm2AgentMulticastRoutingAdminMode": hm2AgentMulticastRoutingAdminMode,
       "hm2AgentMulticastSoftwareDSCP": hm2AgentMulticastSoftwareDSCP,
       "hm2AgentMulticastDVMRPConfigGroup": hm2AgentMulticastDVMRPConfigGroup,
       "hm2AgentMulticastDVMRPAdminMode": hm2AgentMulticastDVMRPAdminMode,
       "hm2AgentMulticastDVMRPRouteExpiryTime": hm2AgentMulticastDVMRPRouteExpiryTime,
       "hm2AgentSnmpTrapFlagsConfigGroupMulticast": hm2AgentSnmpTrapFlagsConfigGroupMulticast,
       "hm2AgentSnmpDVMRPTrapFlag": hm2AgentSnmpDVMRPTrapFlag,
       "hm2AgentSnmpPIMTrapFlag": hm2AgentSnmpPIMTrapFlag,
       "hm2AgentIpStaticMRouteTable": hm2AgentIpStaticMRouteTable,
       "hm2AgentIpStaticMRouteEntry": hm2AgentIpStaticMRouteEntry,
       "hm2AgentIpStaticMRouteSrcAddressType": hm2AgentIpStaticMRouteSrcAddressType,
       "hm2AgentIpStaticMRouteSrcIpAddr": hm2AgentIpStaticMRouteSrcIpAddr,
       "hm2AgentIpStaticMRouteSrcNetMask": hm2AgentIpStaticMRouteSrcNetMask,
       "hm2AgentIpStaticMRouteRpfIpAddr": hm2AgentIpStaticMRouteRpfIpAddr,
       "hm2AgentIpStaticMRouteIfIndex": hm2AgentIpStaticMRouteIfIndex,
       "hm2AgentIpStaticMRoutePreference": hm2AgentIpStaticMRoutePreference,
       "hm2AgentIpStaticMRouteStatus": hm2AgentIpStaticMRouteStatus,
       "hm2AgentIpStaticMRouteExtRpfIpAddrType": hm2AgentIpStaticMRouteExtRpfIpAddrType,
       "hm2AgentIpStaticMRouteExtRpfIpAddr": hm2AgentIpStaticMRouteExtRpfIpAddr,
       "hm2AgentMulticastMgmdExtConfigGroup": hm2AgentMulticastMgmdExtConfigGroup,
       "hm2AgentMulticastMgmdExtTable": hm2AgentMulticastMgmdExtTable,
       "hm2AgentMulticastMgmdExtEntry": hm2AgentMulticastMgmdExtEntry,
       "hm2AgentMulticastMgmdUnsolicitRprtInterval": hm2AgentMulticastMgmdUnsolicitRprtInterval,
       "hm2AgentMulticastMgmdNumberOfGroups": hm2AgentMulticastMgmdNumberOfGroups,
       "hm2AgentMulticastMgmdHostCacheExtGroup": hm2AgentMulticastMgmdHostCacheExtGroup,
       "hm2AgentMulticastMgmdHostCacheExtTable": hm2AgentMulticastMgmdHostCacheExtTable,
       "hm2AgentMulticastMgmdHostCacheExtEntry": hm2AgentMulticastMgmdHostCacheExtEntry,
       "hm2AgentMulticastMgmdHostStatus": hm2AgentMulticastMgmdHostStatus,
       "hm2AgentMulticastSNMPExtensionGroup": hm2AgentMulticastSNMPExtensionGroup,
       "hm2AgentMulticastProtocolEnableErrorReturn": hm2AgentMulticastProtocolEnableErrorReturn,
       "hm2AgentMulticastNullGroupErrorReturn": hm2AgentMulticastNullGroupErrorReturn,
       "hm2AgentMulticastBoundaryRangeEntriesErrorReturn": hm2AgentMulticastBoundaryRangeEntriesErrorReturn,
       "hm2AgentMulticastHostEntriesErrorReturn": hm2AgentMulticastHostEntriesErrorReturn,
       "hm2AgentMgmdHostInvalidEntryErrorReturn": hm2AgentMgmdHostInvalidEntryErrorReturn,
       "hm2AgentMulticastProtocolDeInitErrorReturn": hm2AgentMulticastProtocolDeInitErrorReturn,
       "hm2AgentMulticastLocalAddressErrorReturn": hm2AgentMulticastLocalAddressErrorReturn,
       "hm2AgentMulticastCandRPErrorReturn": hm2AgentMulticastCandRPErrorReturn,
       "hm2AgentMulticastUnicastValidationErrorReturn": hm2AgentMulticastUnicastValidationErrorReturn,
       "hm2AgentMulticastGroupValidationErrorReturn": hm2AgentMulticastGroupValidationErrorReturn,
       "hm2AgentMulticastSSMValidationErrorReturn": hm2AgentMulticastSSMValidationErrorReturn,
       "hm2AgentMulticastStaticSourceErrorReturn": hm2AgentMulticastStaticSourceErrorReturn,
       "hm2AgentMulticastStaticRPFErrorReturn": hm2AgentMulticastStaticRPFErrorReturn,
       "hm2AgentMulticastStaticHostErrorReturn": hm2AgentMulticastStaticHostErrorReturn,
       "hm2AgentMulticastCandRPPrimaryErrorReturn": hm2AgentMulticastCandRPPrimaryErrorReturn,
       "hm2AgentMulticastCandBSRPrimaryErrorReturn": hm2AgentMulticastCandBSRPrimaryErrorReturn}
)
