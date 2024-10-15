# SNMP MIB module (CISCO-VINES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VINES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:11:40 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

(PhysAddress,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "PhysAddress",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions



class VinesNetworkNumber(Integer32):
    """Custom type VinesNetworkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class VinesHostNumber(Integer32):
    """Custom type VinesHostNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )





class VinesMetric(Integer32):
    """Custom type VinesMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 819200),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVinesMIB_ObjectIdentity = ObjectIdentity
ciscoVinesMIB = _CiscoVinesMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17)
)
_CiscoVinesMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVinesMIBObjects = _CiscoVinesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1)
)
_CvBasic_ObjectIdentity = ObjectIdentity
cvBasic = _CvBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 1)
)
_CvBasicNetwork_Type = VinesNetworkNumber
_CvBasicNetwork_Object = MibScalar
cvBasicNetwork = _CvBasicNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 1, 1),
    _CvBasicNetwork_Type()
)
cvBasicNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvBasicNetwork.setStatus("mandatory")
_CvBasicHost_Type = VinesHostNumber
_CvBasicHost_Object = MibScalar
cvBasicHost = _CvBasicHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 1, 2),
    _CvBasicHost_Type()
)
cvBasicHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvBasicHost.setStatus("mandatory")
_CvBasicNextClient_Type = VinesHostNumber
_CvBasicNextClient_Object = MibScalar
cvBasicNextClient = _CvBasicNextClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 1, 3),
    _CvBasicNextClient_Type()
)
cvBasicNextClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvBasicNextClient.setStatus("mandatory")
_CvForwarding_ObjectIdentity = ObjectIdentity
cvForwarding = _CvForwarding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2)
)
_CvForwNeighborNeighborCount_Type = Gauge32
_CvForwNeighborNeighborCount_Object = MibScalar
cvForwNeighborNeighborCount = _CvForwNeighborNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 1),
    _CvForwNeighborNeighborCount_Type()
)
cvForwNeighborNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborNeighborCount.setStatus("mandatory")
_CvForwNeighborPathCount_Type = Gauge32
_CvForwNeighborPathCount_Object = MibScalar
cvForwNeighborPathCount = _CvForwNeighborPathCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 2),
    _CvForwNeighborPathCount_Type()
)
cvForwNeighborPathCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborPathCount.setStatus("mandatory")
_CvForwNeighborVersion_Type = Integer32
_CvForwNeighborVersion_Object = MibScalar
cvForwNeighborVersion = _CvForwNeighborVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 3),
    _CvForwNeighborVersion_Type()
)
cvForwNeighborVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborVersion.setStatus("mandatory")
_CvForwNeighborTable_Object = MibTable
cvForwNeighborTable = _CvForwNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cvForwNeighborTable.setStatus("mandatory")
_CvForwNeighborEntry_Object = MibTableRow
cvForwNeighborEntry = _CvForwNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1)
)
cvForwNeighborEntry.setIndexNames(
    (0, "CISCO-VINES-MIB", "cvForwNeighborNetwork"),
    (0, "CISCO-VINES-MIB", "cvForwNeighborHost"),
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-VINES-MIB", "cvForwNeighborPhysAddress"),
)
if mibBuilder.loadTexts:
    cvForwNeighborEntry.setStatus("mandatory")
_CvForwNeighborNetwork_Type = VinesNetworkNumber
_CvForwNeighborNetwork_Object = MibTableColumn
cvForwNeighborNetwork = _CvForwNeighborNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 1),
    _CvForwNeighborNetwork_Type()
)
cvForwNeighborNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvForwNeighborNetwork.setStatus("mandatory")
_CvForwNeighborHost_Type = VinesHostNumber
_CvForwNeighborHost_Object = MibTableColumn
cvForwNeighborHost = _CvForwNeighborHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 2),
    _CvForwNeighborHost_Type()
)
cvForwNeighborHost.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvForwNeighborHost.setStatus("mandatory")
_CvForwNeighborPhysAddress_Type = PhysAddress
_CvForwNeighborPhysAddress_Object = MibTableColumn
cvForwNeighborPhysAddress = _CvForwNeighborPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 3),
    _CvForwNeighborPhysAddress_Type()
)
cvForwNeighborPhysAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvForwNeighborPhysAddress.setStatus("mandatory")


class _CvForwNeighborSource_Type(Integer32):
    """Custom type cvForwNeighborSource based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("igrp", 6),
          ("manualNeighbor", 8),
          ("manualRoute", 5),
          ("rtpRedirect", 3),
          ("rtpUpdate", 4),
          ("self", 2),
          ("test", 7),
          ("unrecognized", 1))
    )


_CvForwNeighborSource_Type.__name__ = "Integer32"
_CvForwNeighborSource_Object = MibTableColumn
cvForwNeighborSource = _CvForwNeighborSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 4),
    _CvForwNeighborSource_Type()
)
cvForwNeighborSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborSource.setStatus("mandatory")


class _CvForwNeighborRtpVersion_Type(Integer32):
    """Custom type cvForwNeighborRtpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CvForwNeighborRtpVersion_Type.__name__ = "Integer32"
_CvForwNeighborRtpVersion_Object = MibTableColumn
cvForwNeighborRtpVersion = _CvForwNeighborRtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 5),
    _CvForwNeighborRtpVersion_Type()
)
cvForwNeighborRtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborRtpVersion.setStatus("mandatory")


class _CvForwNeighborUsageType_Type(Integer32):
    """Custom type cvForwNeighborUsageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backup", 3),
          ("next", 1),
          ("roundRobin", 2))
    )


_CvForwNeighborUsageType_Type.__name__ = "Integer32"
_CvForwNeighborUsageType_Object = MibTableColumn
cvForwNeighborUsageType = _CvForwNeighborUsageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 6),
    _CvForwNeighborUsageType_Type()
)
cvForwNeighborUsageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborUsageType.setStatus("mandatory")


class _CvForwNeighborAge_Type(Integer32):
    """Custom type cvForwNeighborAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CvForwNeighborAge_Type.__name__ = "Integer32"
_CvForwNeighborAge_Object = MibTableColumn
cvForwNeighborAge = _CvForwNeighborAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 7),
    _CvForwNeighborAge_Type()
)
cvForwNeighborAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborAge.setStatus("mandatory")
_CvForwNeighborMetric_Type = VinesMetric
_CvForwNeighborMetric_Object = MibTableColumn
cvForwNeighborMetric = _CvForwNeighborMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 8),
    _CvForwNeighborMetric_Type()
)
cvForwNeighborMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborMetric.setStatus("mandatory")
_CvForwNeighborUses_Type = Counter32
_CvForwNeighborUses_Object = MibTableColumn
cvForwNeighborUses = _CvForwNeighborUses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 4, 1, 9),
    _CvForwNeighborUses_Type()
)
cvForwNeighborUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwNeighborUses.setStatus("mandatory")
_CvForwRouteRouterCount_Type = Gauge32
_CvForwRouteRouterCount_Object = MibScalar
cvForwRouteRouterCount = _CvForwRouteRouterCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 5),
    _CvForwRouteRouterCount_Type()
)
cvForwRouteRouterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteRouterCount.setStatus("mandatory")
_CvForwRouteRouteCount_Type = Gauge32
_CvForwRouteRouteCount_Object = MibScalar
cvForwRouteRouteCount = _CvForwRouteRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 6),
    _CvForwRouteRouteCount_Type()
)
cvForwRouteRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteRouteCount.setStatus("mandatory")
_CvForwRouteVersion_Type = Integer32
_CvForwRouteVersion_Object = MibScalar
cvForwRouteVersion = _CvForwRouteVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 7),
    _CvForwRouteVersion_Type()
)
cvForwRouteVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteVersion.setStatus("mandatory")
_CvForwRouteUpdateCountdown_Type = Gauge32
_CvForwRouteUpdateCountdown_Object = MibScalar
cvForwRouteUpdateCountdown = _CvForwRouteUpdateCountdown_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 8),
    _CvForwRouteUpdateCountdown_Type()
)
cvForwRouteUpdateCountdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteUpdateCountdown.setStatus("mandatory")
_CvForwRouteTable_Object = MibTable
cvForwRouteTable = _CvForwRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9)
)
if mibBuilder.loadTexts:
    cvForwRouteTable.setStatus("mandatory")
_CvForwRouteEntry_Object = MibTableRow
cvForwRouteEntry = _CvForwRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1)
)
cvForwRouteEntry.setIndexNames(
    (0, "CISCO-VINES-MIB", "cvForwRouteNetworkNumber"),
    (0, "CISCO-VINES-MIB", "cvForwRouteNeighborNetwork"),
)
if mibBuilder.loadTexts:
    cvForwRouteEntry.setStatus("mandatory")
_CvForwRouteNetworkNumber_Type = VinesNetworkNumber
_CvForwRouteNetworkNumber_Object = MibTableColumn
cvForwRouteNetworkNumber = _CvForwRouteNetworkNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 1),
    _CvForwRouteNetworkNumber_Type()
)
cvForwRouteNetworkNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvForwRouteNetworkNumber.setStatus("mandatory")
_CvForwRouteNeighborNetwork_Type = VinesNetworkNumber
_CvForwRouteNeighborNetwork_Object = MibTableColumn
cvForwRouteNeighborNetwork = _CvForwRouteNeighborNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 2),
    _CvForwRouteNeighborNetwork_Type()
)
cvForwRouteNeighborNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvForwRouteNeighborNetwork.setStatus("mandatory")


class _CvForwRouteSource_Type(Integer32):
    """Custom type cvForwRouteSource based on Integer32"""
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
        *(("igrp", 6),
          ("manualRoute", 5),
          ("rtpRedirect", 3),
          ("rtpUpdate", 4),
          ("self", 2),
          ("test", 7),
          ("unrecognized", 1))
    )


_CvForwRouteSource_Type.__name__ = "Integer32"
_CvForwRouteSource_Object = MibTableColumn
cvForwRouteSource = _CvForwRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 3),
    _CvForwRouteSource_Type()
)
cvForwRouteSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteSource.setStatus("mandatory")


class _CvForwRouteRtpVersion_Type(Integer32):
    """Custom type cvForwRouteRtpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CvForwRouteRtpVersion_Type.__name__ = "Integer32"
_CvForwRouteRtpVersion_Object = MibTableColumn
cvForwRouteRtpVersion = _CvForwRouteRtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 4),
    _CvForwRouteRtpVersion_Type()
)
cvForwRouteRtpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteRtpVersion.setStatus("mandatory")
_CvForwRouteUseNext_Type = TruthValue
_CvForwRouteUseNext_Object = MibTableColumn
cvForwRouteUseNext = _CvForwRouteUseNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 5),
    _CvForwRouteUseNext_Type()
)
cvForwRouteUseNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteUseNext.setStatus("mandatory")
_CvForwRouteForwardBroadcast_Type = TruthValue
_CvForwRouteForwardBroadcast_Object = MibTableColumn
cvForwRouteForwardBroadcast = _CvForwRouteForwardBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 6),
    _CvForwRouteForwardBroadcast_Type()
)
cvForwRouteForwardBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteForwardBroadcast.setStatus("mandatory")
_CvForwRouteSuppress_Type = TruthValue
_CvForwRouteSuppress_Object = MibTableColumn
cvForwRouteSuppress = _CvForwRouteSuppress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 7),
    _CvForwRouteSuppress_Type()
)
cvForwRouteSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteSuppress.setStatus("mandatory")
_CvForwRouteLoadShareEligible_Type = TruthValue
_CvForwRouteLoadShareEligible_Object = MibTableColumn
cvForwRouteLoadShareEligible = _CvForwRouteLoadShareEligible_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 8),
    _CvForwRouteLoadShareEligible_Type()
)
cvForwRouteLoadShareEligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteLoadShareEligible.setStatus("mandatory")


class _CvForwRouteAge_Type(Integer32):
    """Custom type cvForwRouteAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_CvForwRouteAge_Type.__name__ = "Integer32"
_CvForwRouteAge_Object = MibTableColumn
cvForwRouteAge = _CvForwRouteAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 9),
    _CvForwRouteAge_Type()
)
cvForwRouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteAge.setStatus("mandatory")
_CvForwRouteMetric_Type = VinesMetric
_CvForwRouteMetric_Object = MibTableColumn
cvForwRouteMetric = _CvForwRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 10),
    _CvForwRouteMetric_Type()
)
cvForwRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteMetric.setStatus("mandatory")
_CvForwRouteUses_Type = Counter32
_CvForwRouteUses_Object = MibTableColumn
cvForwRouteUses = _CvForwRouteUses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 2, 9, 1, 11),
    _CvForwRouteUses_Type()
)
cvForwRouteUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvForwRouteUses.setStatus("mandatory")
_CvTotal_ObjectIdentity = ObjectIdentity
cvTotal = _CvTotal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3)
)
_CvTotalInputPackets_Type = Counter32
_CvTotalInputPackets_Object = MibScalar
cvTotalInputPackets = _CvTotalInputPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 1),
    _CvTotalInputPackets_Type()
)
cvTotalInputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalInputPackets.setStatus("mandatory")
_CvTotalOutputPackets_Type = Counter32
_CvTotalOutputPackets_Object = MibScalar
cvTotalOutputPackets = _CvTotalOutputPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 2),
    _CvTotalOutputPackets_Type()
)
cvTotalOutputPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalOutputPackets.setStatus("mandatory")
_CvTotalLocalDestPackets_Type = Counter32
_CvTotalLocalDestPackets_Object = MibScalar
cvTotalLocalDestPackets = _CvTotalLocalDestPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 3),
    _CvTotalLocalDestPackets_Type()
)
cvTotalLocalDestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalLocalDestPackets.setStatus("mandatory")
_CvTotalForwardedPackets_Type = Counter32
_CvTotalForwardedPackets_Object = MibScalar
cvTotalForwardedPackets = _CvTotalForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 4),
    _CvTotalForwardedPackets_Type()
)
cvTotalForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalForwardedPackets.setStatus("mandatory")
_CvTotalBroadcastInPackets_Type = Counter32
_CvTotalBroadcastInPackets_Object = MibScalar
cvTotalBroadcastInPackets = _CvTotalBroadcastInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 5),
    _CvTotalBroadcastInPackets_Type()
)
cvTotalBroadcastInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalBroadcastInPackets.setStatus("mandatory")
_CvTotalBroadcastOutPackets_Type = Counter32
_CvTotalBroadcastOutPackets_Object = MibScalar
cvTotalBroadcastOutPackets = _CvTotalBroadcastOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 6),
    _CvTotalBroadcastOutPackets_Type()
)
cvTotalBroadcastOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalBroadcastOutPackets.setStatus("mandatory")
_CvTotalBroadcastForwardPackets_Type = Counter32
_CvTotalBroadcastForwardPackets_Object = MibScalar
cvTotalBroadcastForwardPackets = _CvTotalBroadcastForwardPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 7),
    _CvTotalBroadcastForwardPackets_Type()
)
cvTotalBroadcastForwardPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalBroadcastForwardPackets.setStatus("mandatory")
_CvTotalLanOnlyPackets_Type = Counter32
_CvTotalLanOnlyPackets_Object = MibScalar
cvTotalLanOnlyPackets = _CvTotalLanOnlyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 8),
    _CvTotalLanOnlyPackets_Type()
)
cvTotalLanOnlyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalLanOnlyPackets.setStatus("mandatory")
_CvTotalNotOver4800Packets_Type = Counter32
_CvTotalNotOver4800Packets_Object = MibScalar
cvTotalNotOver4800Packets = _CvTotalNotOver4800Packets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 9),
    _CvTotalNotOver4800Packets_Type()
)
cvTotalNotOver4800Packets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalNotOver4800Packets.setStatus("mandatory")
_CvTotalNoChargesPackets_Type = Counter32
_CvTotalNoChargesPackets_Object = MibScalar
cvTotalNoChargesPackets = _CvTotalNoChargesPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 10),
    _CvTotalNoChargesPackets_Type()
)
cvTotalNoChargesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalNoChargesPackets.setStatus("mandatory")
_CvTotalFormatErrors_Type = Counter32
_CvTotalFormatErrors_Object = MibScalar
cvTotalFormatErrors = _CvTotalFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 11),
    _CvTotalFormatErrors_Type()
)
cvTotalFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalFormatErrors.setStatus("mandatory")
_CvTotalChecksumErrors_Type = Counter32
_CvTotalChecksumErrors_Object = MibScalar
cvTotalChecksumErrors = _CvTotalChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 12),
    _CvTotalChecksumErrors_Type()
)
cvTotalChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalChecksumErrors.setStatus("mandatory")
_CvTotalHopCountsExceeded_Type = Counter32
_CvTotalHopCountsExceeded_Object = MibScalar
cvTotalHopCountsExceeded = _CvTotalHopCountsExceeded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 13),
    _CvTotalHopCountsExceeded_Type()
)
cvTotalHopCountsExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalHopCountsExceeded.setStatus("mandatory")
_CvTotalNoRouteDrops_Type = Counter32
_CvTotalNoRouteDrops_Object = MibScalar
cvTotalNoRouteDrops = _CvTotalNoRouteDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 14),
    _CvTotalNoRouteDrops_Type()
)
cvTotalNoRouteDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalNoRouteDrops.setStatus("mandatory")
_CvTotalEncapsFailedDrops_Type = Counter32
_CvTotalEncapsFailedDrops_Object = MibScalar
cvTotalEncapsFailedDrops = _CvTotalEncapsFailedDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 15),
    _CvTotalEncapsFailedDrops_Type()
)
cvTotalEncapsFailedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalEncapsFailedDrops.setStatus("mandatory")
_CvTotalUnknownPackets_Type = Counter32
_CvTotalUnknownPackets_Object = MibScalar
cvTotalUnknownPackets = _CvTotalUnknownPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 16),
    _CvTotalUnknownPackets_Type()
)
cvTotalUnknownPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalUnknownPackets.setStatus("mandatory")
_CvTotalIcpInPackets_Type = Counter32
_CvTotalIcpInPackets_Object = MibScalar
cvTotalIcpInPackets = _CvTotalIcpInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 17),
    _CvTotalIcpInPackets_Type()
)
cvTotalIcpInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalIcpInPackets.setStatus("mandatory")
_CvTotalIcpOutPackets_Type = Counter32
_CvTotalIcpOutPackets_Object = MibScalar
cvTotalIcpOutPackets = _CvTotalIcpOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 18),
    _CvTotalIcpOutPackets_Type()
)
cvTotalIcpOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalIcpOutPackets.setStatus("mandatory")
_CvTotalMetricOutPackets_Type = Counter32
_CvTotalMetricOutPackets_Object = MibScalar
cvTotalMetricOutPackets = _CvTotalMetricOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 19),
    _CvTotalMetricOutPackets_Type()
)
cvTotalMetricOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalMetricOutPackets.setStatus("mandatory")
_CvTotalMacEchoInPackets_Type = Counter32
_CvTotalMacEchoInPackets_Object = MibScalar
cvTotalMacEchoInPackets = _CvTotalMacEchoInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 20),
    _CvTotalMacEchoInPackets_Type()
)
cvTotalMacEchoInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalMacEchoInPackets.setStatus("mandatory")
_CvTotalMacEchoOutPackets_Type = Counter32
_CvTotalMacEchoOutPackets_Object = MibScalar
cvTotalMacEchoOutPackets = _CvTotalMacEchoOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 21),
    _CvTotalMacEchoOutPackets_Type()
)
cvTotalMacEchoOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalMacEchoOutPackets.setStatus("mandatory")
_CvTotalEchoInPackets_Type = Counter32
_CvTotalEchoInPackets_Object = MibScalar
cvTotalEchoInPackets = _CvTotalEchoInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 22),
    _CvTotalEchoInPackets_Type()
)
cvTotalEchoInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalEchoInPackets.setStatus("mandatory")
_CvTotalEchoOutPackets_Type = Counter32
_CvTotalEchoOutPackets_Object = MibScalar
cvTotalEchoOutPackets = _CvTotalEchoOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 23),
    _CvTotalEchoOutPackets_Type()
)
cvTotalEchoOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalEchoOutPackets.setStatus("mandatory")
_CvTotalProxyOutPackets_Type = Counter32
_CvTotalProxyOutPackets_Object = MibScalar
cvTotalProxyOutPackets = _CvTotalProxyOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 24),
    _CvTotalProxyOutPackets_Type()
)
cvTotalProxyOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalProxyOutPackets.setStatus("mandatory")
_CvTotalProxyReplyOutPackets_Type = Counter32
_CvTotalProxyReplyOutPackets_Object = MibScalar
cvTotalProxyReplyOutPackets = _CvTotalProxyReplyOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 3, 25),
    _CvTotalProxyReplyOutPackets_Type()
)
cvTotalProxyReplyOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvTotalProxyReplyOutPackets.setStatus("mandatory")
_CvInterface_ObjectIdentity = ObjectIdentity
cvInterface = _CvInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4)
)
_CvIfConfigTable_Object = MibTable
cvIfConfigTable = _CvIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cvIfConfigTable.setStatus("mandatory")
_CvIfConfigEntry_Object = MibTableRow
cvIfConfigEntry = _CvIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1)
)
cvIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvIfConfigEntry.setStatus("mandatory")
_CvIfConfigMetric_Type = VinesMetric
_CvIfConfigMetric_Object = MibTableColumn
cvIfConfigMetric = _CvIfConfigMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 1),
    _CvIfConfigMetric_Type()
)
cvIfConfigMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigMetric.setStatus("mandatory")


class _CvIfConfigEncapsulation_Type(Integer32):
    """Custom type cvIfConfigEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arpa", 1),
          ("snap", 3),
          ("tokenRing", 2))
    )


_CvIfConfigEncapsulation_Type.__name__ = "Integer32"
_CvIfConfigEncapsulation_Object = MibTableColumn
cvIfConfigEncapsulation = _CvIfConfigEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 2),
    _CvIfConfigEncapsulation_Type()
)
cvIfConfigEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigEncapsulation.setStatus("mandatory")
_CvIfConfigAccesslist_Type = Integer32
_CvIfConfigAccesslist_Object = MibTableColumn
cvIfConfigAccesslist = _CvIfConfigAccesslist_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 3),
    _CvIfConfigAccesslist_Type()
)
cvIfConfigAccesslist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigAccesslist.setStatus("mandatory")


class _CvIfConfigPropagate_Type(Integer32):
    """Custom type cvIfConfigPropagate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("dynamic", 3),
          ("never", 1))
    )


_CvIfConfigPropagate_Type.__name__ = "Integer32"
_CvIfConfigPropagate_Object = MibTableColumn
cvIfConfigPropagate = _CvIfConfigPropagate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 4),
    _CvIfConfigPropagate_Type()
)
cvIfConfigPropagate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigPropagate.setStatus("mandatory")


class _CvIfConfigArpEnabled_Type(Integer32):
    """Custom type cvIfConfigArpEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("always", 2),
          ("dynamic", 3),
          ("never", 1))
    )


_CvIfConfigArpEnabled_Type.__name__ = "Integer32"
_CvIfConfigArpEnabled_Object = MibTableColumn
cvIfConfigArpEnabled = _CvIfConfigArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 5),
    _CvIfConfigArpEnabled_Type()
)
cvIfConfigArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigArpEnabled.setStatus("mandatory")


class _CvIfConfigServerless_Type(Integer32):
    """Custom type cvIfConfigServerless based on Integer32"""
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
        *(("always", 3),
          ("alwaysBroadcast", 4),
          ("dynamic", 2),
          ("never", 1))
    )


_CvIfConfigServerless_Type.__name__ = "Integer32"
_CvIfConfigServerless_Object = MibTableColumn
cvIfConfigServerless = _CvIfConfigServerless_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 6),
    _CvIfConfigServerless_Type()
)
cvIfConfigServerless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigServerless.setStatus("mandatory")
_CvIfConfigRedirectInterval_Type = Integer32
_CvIfConfigRedirectInterval_Object = MibTableColumn
cvIfConfigRedirectInterval = _CvIfConfigRedirectInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 7),
    _CvIfConfigRedirectInterval_Type()
)
cvIfConfigRedirectInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigRedirectInterval.setStatus("mandatory")
_CvIfConfigSplitDisabled_Type = TruthValue
_CvIfConfigSplitDisabled_Object = MibTableColumn
cvIfConfigSplitDisabled = _CvIfConfigSplitDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 8),
    _CvIfConfigSplitDisabled_Type()
)
cvIfConfigSplitDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigSplitDisabled.setStatus("mandatory")
_CvIfConfigLineup_Type = TruthValue
_CvIfConfigLineup_Object = MibTableColumn
cvIfConfigLineup = _CvIfConfigLineup_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 9),
    _CvIfConfigLineup_Type()
)
cvIfConfigLineup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigLineup.setStatus("mandatory")
_CvIfConfigFastokay_Type = TruthValue
_CvIfConfigFastokay_Object = MibTableColumn
cvIfConfigFastokay = _CvIfConfigFastokay_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 10),
    _CvIfConfigFastokay_Type()
)
cvIfConfigFastokay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigFastokay.setStatus("mandatory")
_CvIfConfigRouteCache_Type = TruthValue
_CvIfConfigRouteCache_Object = MibTableColumn
cvIfConfigRouteCache = _CvIfConfigRouteCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 11),
    _CvIfConfigRouteCache_Type()
)
cvIfConfigRouteCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigRouteCache.setStatus("mandatory")
_CvIfConfigInputRouterFilter_Type = Integer32
_CvIfConfigInputRouterFilter_Object = MibTableColumn
cvIfConfigInputRouterFilter = _CvIfConfigInputRouterFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 12),
    _CvIfConfigInputRouterFilter_Type()
)
cvIfConfigInputRouterFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigInputRouterFilter.setStatus("mandatory")
_CvIfConfigInputNetworkFilter_Type = Integer32
_CvIfConfigInputNetworkFilter_Object = MibTableColumn
cvIfConfigInputNetworkFilter = _CvIfConfigInputNetworkFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 13),
    _CvIfConfigInputNetworkFilter_Type()
)
cvIfConfigInputNetworkFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigInputNetworkFilter.setStatus("mandatory")
_CvIfConfigOutputNetworkFilter_Type = Integer32
_CvIfConfigOutputNetworkFilter_Object = MibTableColumn
cvIfConfigOutputNetworkFilter = _CvIfConfigOutputNetworkFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 1, 1, 14),
    _CvIfConfigOutputNetworkFilter_Type()
)
cvIfConfigOutputNetworkFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfConfigOutputNetworkFilter.setStatus("mandatory")
_CvIfCountInTable_Object = MibTable
cvIfCountInTable = _CvIfCountInTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2)
)
if mibBuilder.loadTexts:
    cvIfCountInTable.setStatus("mandatory")
_CvIfCountInEntry_Object = MibTableRow
cvIfCountInEntry = _CvIfCountInEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1)
)
cvIfCountInEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvIfCountInEntry.setStatus("mandatory")
_CvIfCountInNotEnabledDrops_Type = Counter32
_CvIfCountInNotEnabledDrops_Object = MibTableColumn
cvIfCountInNotEnabledDrops = _CvIfCountInNotEnabledDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 1),
    _CvIfCountInNotEnabledDrops_Type()
)
cvIfCountInNotEnabledDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInNotEnabledDrops.setStatus("mandatory")
_CvIfCountInFormatErrors_Type = Counter32
_CvIfCountInFormatErrors_Object = MibTableColumn
cvIfCountInFormatErrors = _CvIfCountInFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 2),
    _CvIfCountInFormatErrors_Type()
)
cvIfCountInFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInFormatErrors.setStatus("mandatory")
_CvIfCountInLocalDestPackets_Type = Counter32
_CvIfCountInLocalDestPackets_Object = MibTableColumn
cvIfCountInLocalDestPackets = _CvIfCountInLocalDestPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 3),
    _CvIfCountInLocalDestPackets_Type()
)
cvIfCountInLocalDestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInLocalDestPackets.setStatus("mandatory")
_CvIfCountInBroadcastPackets_Type = Counter32
_CvIfCountInBroadcastPackets_Object = MibTableColumn
cvIfCountInBroadcastPackets = _CvIfCountInBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 4),
    _CvIfCountInBroadcastPackets_Type()
)
cvIfCountInBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInBroadcastPackets.setStatus("mandatory")
_CvIfCountInForwardedPackets_Type = Counter32
_CvIfCountInForwardedPackets_Object = MibTableColumn
cvIfCountInForwardedPackets = _CvIfCountInForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 5),
    _CvIfCountInForwardedPackets_Type()
)
cvIfCountInForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInForwardedPackets.setStatus("mandatory")
_CvIfCountInNoRouteDrops_Type = Counter32
_CvIfCountInNoRouteDrops_Object = MibTableColumn
cvIfCountInNoRouteDrops = _CvIfCountInNoRouteDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 6),
    _CvIfCountInNoRouteDrops_Type()
)
cvIfCountInNoRouteDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInNoRouteDrops.setStatus("mandatory")
_CvIfCountInZeroHopCountDrops_Type = Counter32
_CvIfCountInZeroHopCountDrops_Object = MibTableColumn
cvIfCountInZeroHopCountDrops = _CvIfCountInZeroHopCountDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 7),
    _CvIfCountInZeroHopCountDrops_Type()
)
cvIfCountInZeroHopCountDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInZeroHopCountDrops.setStatus("mandatory")
_CvIfCountInChecksumErrors_Type = Counter32
_CvIfCountInChecksumErrors_Object = MibTableColumn
cvIfCountInChecksumErrors = _CvIfCountInChecksumErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 8),
    _CvIfCountInChecksumErrors_Type()
)
cvIfCountInChecksumErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInChecksumErrors.setStatus("mandatory")
_CvIfCountInArpQueryRequests_Type = Counter32
_CvIfCountInArpQueryRequests_Object = MibTableColumn
cvIfCountInArpQueryRequests = _CvIfCountInArpQueryRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 9),
    _CvIfCountInArpQueryRequests_Type()
)
cvIfCountInArpQueryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInArpQueryRequests.setStatus("mandatory")
_CvIfCountInArpQueryResponses_Type = Counter32
_CvIfCountInArpQueryResponses_Object = MibTableColumn
cvIfCountInArpQueryResponses = _CvIfCountInArpQueryResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 10),
    _CvIfCountInArpQueryResponses_Type()
)
cvIfCountInArpQueryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInArpQueryResponses.setStatus("mandatory")
_CvIfCountInArpAssignmentRequests_Type = Counter32
_CvIfCountInArpAssignmentRequests_Object = MibTableColumn
cvIfCountInArpAssignmentRequests = _CvIfCountInArpAssignmentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 11),
    _CvIfCountInArpAssignmentRequests_Type()
)
cvIfCountInArpAssignmentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInArpAssignmentRequests.setStatus("mandatory")
_CvIfCountInArpAssignmentResponses_Type = Counter32
_CvIfCountInArpAssignmentResponses_Object = MibTableColumn
cvIfCountInArpAssignmentResponses = _CvIfCountInArpAssignmentResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 12),
    _CvIfCountInArpAssignmentResponses_Type()
)
cvIfCountInArpAssignmentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInArpAssignmentResponses.setStatus("mandatory")
_CvIfCountInArpIllegalMessages_Type = Counter32
_CvIfCountInArpIllegalMessages_Object = MibTableColumn
cvIfCountInArpIllegalMessages = _CvIfCountInArpIllegalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 13),
    _CvIfCountInArpIllegalMessages_Type()
)
cvIfCountInArpIllegalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInArpIllegalMessages.setStatus("mandatory")
_CvIfCountInIcpErrorMessages_Type = Counter32
_CvIfCountInIcpErrorMessages_Object = MibTableColumn
cvIfCountInIcpErrorMessages = _CvIfCountInIcpErrorMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 14),
    _CvIfCountInIcpErrorMessages_Type()
)
cvIfCountInIcpErrorMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInIcpErrorMessages.setStatus("mandatory")
_CvIfCountInIcpMetricMessages_Type = Counter32
_CvIfCountInIcpMetricMessages_Object = MibTableColumn
cvIfCountInIcpMetricMessages = _CvIfCountInIcpMetricMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 15),
    _CvIfCountInIcpMetricMessages_Type()
)
cvIfCountInIcpMetricMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInIcpMetricMessages.setStatus("mandatory")
_CvIfCountInIcpIllegalMessages_Type = Counter32
_CvIfCountInIcpIllegalMessages_Object = MibTableColumn
cvIfCountInIcpIllegalMessages = _CvIfCountInIcpIllegalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 16),
    _CvIfCountInIcpIllegalMessages_Type()
)
cvIfCountInIcpIllegalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInIcpIllegalMessages.setStatus("mandatory")
_CvIfCountInIpcMessages_Type = Counter32
_CvIfCountInIpcMessages_Object = MibTableColumn
cvIfCountInIpcMessages = _CvIfCountInIpcMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 17),
    _CvIfCountInIpcMessages_Type()
)
cvIfCountInIpcMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInIpcMessages.setStatus("mandatory")
_CvIfCountInRtp0Messages_Type = Counter32
_CvIfCountInRtp0Messages_Object = MibTableColumn
cvIfCountInRtp0Messages = _CvIfCountInRtp0Messages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 18),
    _CvIfCountInRtp0Messages_Type()
)
cvIfCountInRtp0Messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtp0Messages.setStatus("mandatory")
_CvIfCountInRtp1Messages_Type = Counter32
_CvIfCountInRtp1Messages_Object = MibTableColumn
cvIfCountInRtp1Messages = _CvIfCountInRtp1Messages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 19),
    _CvIfCountInRtp1Messages_Type()
)
cvIfCountInRtp1Messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtp1Messages.setStatus("mandatory")
_CvIfCountInRtp2Messages_Type = Counter32
_CvIfCountInRtp2Messages_Object = MibTableColumn
cvIfCountInRtp2Messages = _CvIfCountInRtp2Messages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 20),
    _CvIfCountInRtp2Messages_Type()
)
cvIfCountInRtp2Messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtp2Messages.setStatus("mandatory")
_CvIfCountInRtp3Messages_Type = Counter32
_CvIfCountInRtp3Messages_Object = MibTableColumn
cvIfCountInRtp3Messages = _CvIfCountInRtp3Messages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 21),
    _CvIfCountInRtp3Messages_Type()
)
cvIfCountInRtp3Messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtp3Messages.setStatus("mandatory")
_CvIfCountInRtpUpdateMessages_Type = Counter32
_CvIfCountInRtpUpdateMessages_Object = MibTableColumn
cvIfCountInRtpUpdateMessages = _CvIfCountInRtpUpdateMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 22),
    _CvIfCountInRtpUpdateMessages_Type()
)
cvIfCountInRtpUpdateMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtpUpdateMessages.setStatus("mandatory")
_CvIfCountInRtpResponseMessages_Type = Counter32
_CvIfCountInRtpResponseMessages_Object = MibTableColumn
cvIfCountInRtpResponseMessages = _CvIfCountInRtpResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 23),
    _CvIfCountInRtpResponseMessages_Type()
)
cvIfCountInRtpResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtpResponseMessages.setStatus("mandatory")
_CvIfCountInRtpRedirectMessages_Type = Counter32
_CvIfCountInRtpRedirectMessages_Object = MibTableColumn
cvIfCountInRtpRedirectMessages = _CvIfCountInRtpRedirectMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 24),
    _CvIfCountInRtpRedirectMessages_Type()
)
cvIfCountInRtpRedirectMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtpRedirectMessages.setStatus("mandatory")
_CvIfCountInRtpIllegalMessages_Type = Counter32
_CvIfCountInRtpIllegalMessages_Object = MibTableColumn
cvIfCountInRtpIllegalMessages = _CvIfCountInRtpIllegalMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 25),
    _CvIfCountInRtpIllegalMessages_Type()
)
cvIfCountInRtpIllegalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInRtpIllegalMessages.setStatus("mandatory")
_CvIfCountInSppMessages_Type = Counter32
_CvIfCountInSppMessages_Object = MibTableColumn
cvIfCountInSppMessages = _CvIfCountInSppMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 26),
    _CvIfCountInSppMessages_Type()
)
cvIfCountInSppMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInSppMessages.setStatus("mandatory")
_CvIfCountInIpUnknownProtocols_Type = Counter32
_CvIfCountInIpUnknownProtocols_Object = MibTableColumn
cvIfCountInIpUnknownProtocols = _CvIfCountInIpUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 27),
    _CvIfCountInIpUnknownProtocols_Type()
)
cvIfCountInIpUnknownProtocols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInIpUnknownProtocols.setStatus("mandatory")
_CvIfCountInIpcUnknownPorts_Type = Counter32
_CvIfCountInIpcUnknownPorts_Object = MibTableColumn
cvIfCountInIpcUnknownPorts = _CvIfCountInIpcUnknownPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 28),
    _CvIfCountInIpcUnknownPorts_Type()
)
cvIfCountInIpcUnknownPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInIpcUnknownPorts.setStatus("mandatory")
_CvIfCountInBroadcastsHelpered_Type = Counter32
_CvIfCountInBroadcastsHelpered_Object = MibTableColumn
cvIfCountInBroadcastsHelpered = _CvIfCountInBroadcastsHelpered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 29),
    _CvIfCountInBroadcastsHelpered_Type()
)
cvIfCountInBroadcastsHelpered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInBroadcastsHelpered.setStatus("mandatory")
_CvIfCountInBroadcastsForwarded_Type = Counter32
_CvIfCountInBroadcastsForwarded_Object = MibTableColumn
cvIfCountInBroadcastsForwarded = _CvIfCountInBroadcastsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 30),
    _CvIfCountInBroadcastsForwarded_Type()
)
cvIfCountInBroadcastsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInBroadcastsForwarded.setStatus("mandatory")
_CvIfCountInBroadcastDuplicates_Type = Counter32
_CvIfCountInBroadcastDuplicates_Object = MibTableColumn
cvIfCountInBroadcastDuplicates = _CvIfCountInBroadcastDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 31),
    _CvIfCountInBroadcastDuplicates_Type()
)
cvIfCountInBroadcastDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInBroadcastDuplicates.setStatus("mandatory")
_CvIfCountInEchoPackets_Type = Counter32
_CvIfCountInEchoPackets_Object = MibTableColumn
cvIfCountInEchoPackets = _CvIfCountInEchoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 32),
    _CvIfCountInEchoPackets_Type()
)
cvIfCountInEchoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInEchoPackets.setStatus("mandatory")
_CvIfCountInMacEchoPackets_Type = Counter32
_CvIfCountInMacEchoPackets_Object = MibTableColumn
cvIfCountInMacEchoPackets = _CvIfCountInMacEchoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 33),
    _CvIfCountInMacEchoPackets_Type()
)
cvIfCountInMacEchoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInMacEchoPackets.setStatus("mandatory")
_CvIfCountInProxyReplyPackets_Type = Counter32
_CvIfCountInProxyReplyPackets_Object = MibTableColumn
cvIfCountInProxyReplyPackets = _CvIfCountInProxyReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 2, 1, 34),
    _CvIfCountInProxyReplyPackets_Type()
)
cvIfCountInProxyReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountInProxyReplyPackets.setStatus("mandatory")
_CvIfCountOutTable_Object = MibTable
cvIfCountOutTable = _CvIfCountOutTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3)
)
if mibBuilder.loadTexts:
    cvIfCountOutTable.setStatus("mandatory")
_CvIfCountOutEntry_Object = MibTableRow
cvIfCountOutEntry = _CvIfCountOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1)
)
cvIfCountOutEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvIfCountOutEntry.setStatus("mandatory")
_CvIfCountOutUnicastPackets_Type = Counter32
_CvIfCountOutUnicastPackets_Object = MibTableColumn
cvIfCountOutUnicastPackets = _CvIfCountOutUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 1),
    _CvIfCountOutUnicastPackets_Type()
)
cvIfCountOutUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutUnicastPackets.setStatus("mandatory")
_CvIfCountOutBroadcastPackets_Type = Counter32
_CvIfCountOutBroadcastPackets_Object = MibTableColumn
cvIfCountOutBroadcastPackets = _CvIfCountOutBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 2),
    _CvIfCountOutBroadcastPackets_Type()
)
cvIfCountOutBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutBroadcastPackets.setStatus("mandatory")
_CvIfCountOutForwardedPackets_Type = Counter32
_CvIfCountOutForwardedPackets_Object = MibTableColumn
cvIfCountOutForwardedPackets = _CvIfCountOutForwardedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 3),
    _CvIfCountOutForwardedPackets_Type()
)
cvIfCountOutForwardedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutForwardedPackets.setStatus("mandatory")
_CvIfCountOutEncapsulationFailures_Type = Counter32
_CvIfCountOutEncapsulationFailures_Object = MibTableColumn
cvIfCountOutEncapsulationFailures = _CvIfCountOutEncapsulationFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 4),
    _CvIfCountOutEncapsulationFailures_Type()
)
cvIfCountOutEncapsulationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutEncapsulationFailures.setStatus("mandatory")
_CvIfCountOutAccessFailures_Type = Counter32
_CvIfCountOutAccessFailures_Object = MibTableColumn
cvIfCountOutAccessFailures = _CvIfCountOutAccessFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 5),
    _CvIfCountOutAccessFailures_Type()
)
cvIfCountOutAccessFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutAccessFailures.setStatus("mandatory")
_CvIfCountOutDownFailures_Type = Counter32
_CvIfCountOutDownFailures_Object = MibTableColumn
cvIfCountOutDownFailures = _CvIfCountOutDownFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 6),
    _CvIfCountOutDownFailures_Type()
)
cvIfCountOutDownFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutDownFailures.setStatus("mandatory")
_CvIfCountOutPacketsNotBroadcastToSource_Type = Counter32
_CvIfCountOutPacketsNotBroadcastToSource_Object = MibTableColumn
cvIfCountOutPacketsNotBroadcastToSource = _CvIfCountOutPacketsNotBroadcastToSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 7),
    _CvIfCountOutPacketsNotBroadcastToSource_Type()
)
cvIfCountOutPacketsNotBroadcastToSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutPacketsNotBroadcastToSource.setStatus("mandatory")
_CvIfCountOutPacketsNotBroadcastLanOnly_Type = Counter32
_CvIfCountOutPacketsNotBroadcastLanOnly_Object = MibTableColumn
cvIfCountOutPacketsNotBroadcastLanOnly = _CvIfCountOutPacketsNotBroadcastLanOnly_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 8),
    _CvIfCountOutPacketsNotBroadcastLanOnly_Type()
)
cvIfCountOutPacketsNotBroadcastLanOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutPacketsNotBroadcastLanOnly.setStatus("mandatory")
_CvIfCountOutPacketsNotBroadcastNotOver4800_Type = Counter32
_CvIfCountOutPacketsNotBroadcastNotOver4800_Object = MibTableColumn
cvIfCountOutPacketsNotBroadcastNotOver4800 = _CvIfCountOutPacketsNotBroadcastNotOver4800_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 9),
    _CvIfCountOutPacketsNotBroadcastNotOver4800_Type()
)
cvIfCountOutPacketsNotBroadcastNotOver4800.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutPacketsNotBroadcastNotOver4800.setStatus("mandatory")
_CvIfCountOutPacketsNotBroadcastNoCharge_Type = Counter32
_CvIfCountOutPacketsNotBroadcastNoCharge_Object = MibTableColumn
cvIfCountOutPacketsNotBroadcastNoCharge = _CvIfCountOutPacketsNotBroadcastNoCharge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 10),
    _CvIfCountOutPacketsNotBroadcastNoCharge_Type()
)
cvIfCountOutPacketsNotBroadcastNoCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutPacketsNotBroadcastNoCharge.setStatus("mandatory")
_CvIfCountOutBroadcastsForwarded_Type = Counter32
_CvIfCountOutBroadcastsForwarded_Object = MibTableColumn
cvIfCountOutBroadcastsForwarded = _CvIfCountOutBroadcastsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 11),
    _CvIfCountOutBroadcastsForwarded_Type()
)
cvIfCountOutBroadcastsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutBroadcastsForwarded.setStatus("mandatory")
_CvIfCountOutBroadcastsHelpered_Type = Counter32
_CvIfCountOutBroadcastsHelpered_Object = MibTableColumn
cvIfCountOutBroadcastsHelpered = _CvIfCountOutBroadcastsHelpered_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 12),
    _CvIfCountOutBroadcastsHelpered_Type()
)
cvIfCountOutBroadcastsHelpered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutBroadcastsHelpered.setStatus("mandatory")
_CvIfCountOutArpQueryRequests_Type = Counter32
_CvIfCountOutArpQueryRequests_Object = MibTableColumn
cvIfCountOutArpQueryRequests = _CvIfCountOutArpQueryRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 13),
    _CvIfCountOutArpQueryRequests_Type()
)
cvIfCountOutArpQueryRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutArpQueryRequests.setStatus("mandatory")
_CvIfCountOutArpQueryResponses_Type = Counter32
_CvIfCountOutArpQueryResponses_Object = MibTableColumn
cvIfCountOutArpQueryResponses = _CvIfCountOutArpQueryResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 14),
    _CvIfCountOutArpQueryResponses_Type()
)
cvIfCountOutArpQueryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutArpQueryResponses.setStatus("mandatory")
_CvIfCountOutArpAssignmentRequests_Type = Counter32
_CvIfCountOutArpAssignmentRequests_Object = MibTableColumn
cvIfCountOutArpAssignmentRequests = _CvIfCountOutArpAssignmentRequests_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 15),
    _CvIfCountOutArpAssignmentRequests_Type()
)
cvIfCountOutArpAssignmentRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutArpAssignmentRequests.setStatus("mandatory")
_CvIfCountOutArpAssignmentResponses_Type = Counter32
_CvIfCountOutArpAssignmentResponses_Object = MibTableColumn
cvIfCountOutArpAssignmentResponses = _CvIfCountOutArpAssignmentResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 16),
    _CvIfCountOutArpAssignmentResponses_Type()
)
cvIfCountOutArpAssignmentResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutArpAssignmentResponses.setStatus("mandatory")
_CvIfCountOutIcpErrorMessages_Type = Counter32
_CvIfCountOutIcpErrorMessages_Object = MibTableColumn
cvIfCountOutIcpErrorMessages = _CvIfCountOutIcpErrorMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 17),
    _CvIfCountOutIcpErrorMessages_Type()
)
cvIfCountOutIcpErrorMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutIcpErrorMessages.setStatus("mandatory")
_CvIfCountOutIcpMetricMessages_Type = Counter32
_CvIfCountOutIcpMetricMessages_Object = MibTableColumn
cvIfCountOutIcpMetricMessages = _CvIfCountOutIcpMetricMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 18),
    _CvIfCountOutIcpMetricMessages_Type()
)
cvIfCountOutIcpMetricMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutIcpMetricMessages.setStatus("mandatory")
_CvIfCountOutIpcMessages_Type = Counter32
_CvIfCountOutIpcMessages_Object = MibTableColumn
cvIfCountOutIpcMessages = _CvIfCountOutIpcMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 19),
    _CvIfCountOutIpcMessages_Type()
)
cvIfCountOutIpcMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutIpcMessages.setStatus("mandatory")
_CvIfCountOutRtp0Messages_Type = Counter32
_CvIfCountOutRtp0Messages_Object = MibTableColumn
cvIfCountOutRtp0Messages = _CvIfCountOutRtp0Messages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 20),
    _CvIfCountOutRtp0Messages_Type()
)
cvIfCountOutRtp0Messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutRtp0Messages.setStatus("mandatory")
_CvIfCountOutRtpRequestMessages_Type = Counter32
_CvIfCountOutRtpRequestMessages_Object = MibTableColumn
cvIfCountOutRtpRequestMessages = _CvIfCountOutRtpRequestMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 21),
    _CvIfCountOutRtpRequestMessages_Type()
)
cvIfCountOutRtpRequestMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutRtpRequestMessages.setStatus("mandatory")
_CvIfCountOutRtp2Messages_Type = Counter32
_CvIfCountOutRtp2Messages_Object = MibTableColumn
cvIfCountOutRtp2Messages = _CvIfCountOutRtp2Messages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 22),
    _CvIfCountOutRtp2Messages_Type()
)
cvIfCountOutRtp2Messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutRtp2Messages.setStatus("mandatory")
_CvIfCountOutRtp3Messages_Type = Counter32
_CvIfCountOutRtp3Messages_Object = MibTableColumn
cvIfCountOutRtp3Messages = _CvIfCountOutRtp3Messages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 23),
    _CvIfCountOutRtp3Messages_Type()
)
cvIfCountOutRtp3Messages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutRtp3Messages.setStatus("mandatory")
_CvIfCountOutRtpUpdateMessages_Type = Counter32
_CvIfCountOutRtpUpdateMessages_Object = MibTableColumn
cvIfCountOutRtpUpdateMessages = _CvIfCountOutRtpUpdateMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 24),
    _CvIfCountOutRtpUpdateMessages_Type()
)
cvIfCountOutRtpUpdateMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutRtpUpdateMessages.setStatus("mandatory")
_CvIfCountOutRtpResponseMessages_Type = Counter32
_CvIfCountOutRtpResponseMessages_Object = MibTableColumn
cvIfCountOutRtpResponseMessages = _CvIfCountOutRtpResponseMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 25),
    _CvIfCountOutRtpResponseMessages_Type()
)
cvIfCountOutRtpResponseMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutRtpResponseMessages.setStatus("mandatory")
_CvIfCountOutRtpRedirectMessages_Type = Counter32
_CvIfCountOutRtpRedirectMessages_Object = MibTableColumn
cvIfCountOutRtpRedirectMessages = _CvIfCountOutRtpRedirectMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 26),
    _CvIfCountOutRtpRedirectMessages_Type()
)
cvIfCountOutRtpRedirectMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutRtpRedirectMessages.setStatus("mandatory")
_CvIfCountOutSppMessages_Type = Counter32
_CvIfCountOutSppMessages_Object = MibTableColumn
cvIfCountOutSppMessages = _CvIfCountOutSppMessages_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 27),
    _CvIfCountOutSppMessages_Type()
)
cvIfCountOutSppMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutSppMessages.setStatus("mandatory")
_CvIfCountOutEchoPackets_Type = Counter32
_CvIfCountOutEchoPackets_Object = MibTableColumn
cvIfCountOutEchoPackets = _CvIfCountOutEchoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 28),
    _CvIfCountOutEchoPackets_Type()
)
cvIfCountOutEchoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutEchoPackets.setStatus("mandatory")
_CvIfCountOutMacEchoPackets_Type = Counter32
_CvIfCountOutMacEchoPackets_Object = MibTableColumn
cvIfCountOutMacEchoPackets = _CvIfCountOutMacEchoPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 29),
    _CvIfCountOutMacEchoPackets_Type()
)
cvIfCountOutMacEchoPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutMacEchoPackets.setStatus("mandatory")
_CvIfCountOutProxyPackets_Type = Counter32
_CvIfCountOutProxyPackets_Object = MibTableColumn
cvIfCountOutProxyPackets = _CvIfCountOutProxyPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 1, 4, 3, 1, 30),
    _CvIfCountOutProxyPackets_Type()
)
cvIfCountOutProxyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCountOutProxyPackets.setStatus("mandatory")
_CiscoVinesMIBConformance_ObjectIdentity = ObjectIdentity
ciscoVinesMIBConformance = _CiscoVinesMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 3)
)
_CiscoVinesMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVinesMIBCompliances = _CiscoVinesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 3, 1)
)
_CiscoVinesMIBCompliance_ObjectIdentity = ObjectIdentity
ciscoVinesMIBCompliance = _CiscoVinesMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 3, 1, 1)
)
_CiscoVinesMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVinesMIBGroups = _CiscoVinesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 3, 2)
)
_CiscoVinesMIBGroup_ObjectIdentity = ObjectIdentity
ciscoVinesMIBGroup = _CiscoVinesMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 17, 3, 2, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VINES-MIB",
    **{"VinesNetworkNumber": VinesNetworkNumber,
       "VinesHostNumber": VinesHostNumber,
       "VinesMetric": VinesMetric,
       "ciscoVinesMIB": ciscoVinesMIB,
       "ciscoVinesMIBObjects": ciscoVinesMIBObjects,
       "cvBasic": cvBasic,
       "cvBasicNetwork": cvBasicNetwork,
       "cvBasicHost": cvBasicHost,
       "cvBasicNextClient": cvBasicNextClient,
       "cvForwarding": cvForwarding,
       "cvForwNeighborNeighborCount": cvForwNeighborNeighborCount,
       "cvForwNeighborPathCount": cvForwNeighborPathCount,
       "cvForwNeighborVersion": cvForwNeighborVersion,
       "cvForwNeighborTable": cvForwNeighborTable,
       "cvForwNeighborEntry": cvForwNeighborEntry,
       "cvForwNeighborNetwork": cvForwNeighborNetwork,
       "cvForwNeighborHost": cvForwNeighborHost,
       "cvForwNeighborPhysAddress": cvForwNeighborPhysAddress,
       "cvForwNeighborSource": cvForwNeighborSource,
       "cvForwNeighborRtpVersion": cvForwNeighborRtpVersion,
       "cvForwNeighborUsageType": cvForwNeighborUsageType,
       "cvForwNeighborAge": cvForwNeighborAge,
       "cvForwNeighborMetric": cvForwNeighborMetric,
       "cvForwNeighborUses": cvForwNeighborUses,
       "cvForwRouteRouterCount": cvForwRouteRouterCount,
       "cvForwRouteRouteCount": cvForwRouteRouteCount,
       "cvForwRouteVersion": cvForwRouteVersion,
       "cvForwRouteUpdateCountdown": cvForwRouteUpdateCountdown,
       "cvForwRouteTable": cvForwRouteTable,
       "cvForwRouteEntry": cvForwRouteEntry,
       "cvForwRouteNetworkNumber": cvForwRouteNetworkNumber,
       "cvForwRouteNeighborNetwork": cvForwRouteNeighborNetwork,
       "cvForwRouteSource": cvForwRouteSource,
       "cvForwRouteRtpVersion": cvForwRouteRtpVersion,
       "cvForwRouteUseNext": cvForwRouteUseNext,
       "cvForwRouteForwardBroadcast": cvForwRouteForwardBroadcast,
       "cvForwRouteSuppress": cvForwRouteSuppress,
       "cvForwRouteLoadShareEligible": cvForwRouteLoadShareEligible,
       "cvForwRouteAge": cvForwRouteAge,
       "cvForwRouteMetric": cvForwRouteMetric,
       "cvForwRouteUses": cvForwRouteUses,
       "cvTotal": cvTotal,
       "cvTotalInputPackets": cvTotalInputPackets,
       "cvTotalOutputPackets": cvTotalOutputPackets,
       "cvTotalLocalDestPackets": cvTotalLocalDestPackets,
       "cvTotalForwardedPackets": cvTotalForwardedPackets,
       "cvTotalBroadcastInPackets": cvTotalBroadcastInPackets,
       "cvTotalBroadcastOutPackets": cvTotalBroadcastOutPackets,
       "cvTotalBroadcastForwardPackets": cvTotalBroadcastForwardPackets,
       "cvTotalLanOnlyPackets": cvTotalLanOnlyPackets,
       "cvTotalNotOver4800Packets": cvTotalNotOver4800Packets,
       "cvTotalNoChargesPackets": cvTotalNoChargesPackets,
       "cvTotalFormatErrors": cvTotalFormatErrors,
       "cvTotalChecksumErrors": cvTotalChecksumErrors,
       "cvTotalHopCountsExceeded": cvTotalHopCountsExceeded,
       "cvTotalNoRouteDrops": cvTotalNoRouteDrops,
       "cvTotalEncapsFailedDrops": cvTotalEncapsFailedDrops,
       "cvTotalUnknownPackets": cvTotalUnknownPackets,
       "cvTotalIcpInPackets": cvTotalIcpInPackets,
       "cvTotalIcpOutPackets": cvTotalIcpOutPackets,
       "cvTotalMetricOutPackets": cvTotalMetricOutPackets,
       "cvTotalMacEchoInPackets": cvTotalMacEchoInPackets,
       "cvTotalMacEchoOutPackets": cvTotalMacEchoOutPackets,
       "cvTotalEchoInPackets": cvTotalEchoInPackets,
       "cvTotalEchoOutPackets": cvTotalEchoOutPackets,
       "cvTotalProxyOutPackets": cvTotalProxyOutPackets,
       "cvTotalProxyReplyOutPackets": cvTotalProxyReplyOutPackets,
       "cvInterface": cvInterface,
       "cvIfConfigTable": cvIfConfigTable,
       "cvIfConfigEntry": cvIfConfigEntry,
       "cvIfConfigMetric": cvIfConfigMetric,
       "cvIfConfigEncapsulation": cvIfConfigEncapsulation,
       "cvIfConfigAccesslist": cvIfConfigAccesslist,
       "cvIfConfigPropagate": cvIfConfigPropagate,
       "cvIfConfigArpEnabled": cvIfConfigArpEnabled,
       "cvIfConfigServerless": cvIfConfigServerless,
       "cvIfConfigRedirectInterval": cvIfConfigRedirectInterval,
       "cvIfConfigSplitDisabled": cvIfConfigSplitDisabled,
       "cvIfConfigLineup": cvIfConfigLineup,
       "cvIfConfigFastokay": cvIfConfigFastokay,
       "cvIfConfigRouteCache": cvIfConfigRouteCache,
       "cvIfConfigInputRouterFilter": cvIfConfigInputRouterFilter,
       "cvIfConfigInputNetworkFilter": cvIfConfigInputNetworkFilter,
       "cvIfConfigOutputNetworkFilter": cvIfConfigOutputNetworkFilter,
       "cvIfCountInTable": cvIfCountInTable,
       "cvIfCountInEntry": cvIfCountInEntry,
       "cvIfCountInNotEnabledDrops": cvIfCountInNotEnabledDrops,
       "cvIfCountInFormatErrors": cvIfCountInFormatErrors,
       "cvIfCountInLocalDestPackets": cvIfCountInLocalDestPackets,
       "cvIfCountInBroadcastPackets": cvIfCountInBroadcastPackets,
       "cvIfCountInForwardedPackets": cvIfCountInForwardedPackets,
       "cvIfCountInNoRouteDrops": cvIfCountInNoRouteDrops,
       "cvIfCountInZeroHopCountDrops": cvIfCountInZeroHopCountDrops,
       "cvIfCountInChecksumErrors": cvIfCountInChecksumErrors,
       "cvIfCountInArpQueryRequests": cvIfCountInArpQueryRequests,
       "cvIfCountInArpQueryResponses": cvIfCountInArpQueryResponses,
       "cvIfCountInArpAssignmentRequests": cvIfCountInArpAssignmentRequests,
       "cvIfCountInArpAssignmentResponses": cvIfCountInArpAssignmentResponses,
       "cvIfCountInArpIllegalMessages": cvIfCountInArpIllegalMessages,
       "cvIfCountInIcpErrorMessages": cvIfCountInIcpErrorMessages,
       "cvIfCountInIcpMetricMessages": cvIfCountInIcpMetricMessages,
       "cvIfCountInIcpIllegalMessages": cvIfCountInIcpIllegalMessages,
       "cvIfCountInIpcMessages": cvIfCountInIpcMessages,
       "cvIfCountInRtp0Messages": cvIfCountInRtp0Messages,
       "cvIfCountInRtp1Messages": cvIfCountInRtp1Messages,
       "cvIfCountInRtp2Messages": cvIfCountInRtp2Messages,
       "cvIfCountInRtp3Messages": cvIfCountInRtp3Messages,
       "cvIfCountInRtpUpdateMessages": cvIfCountInRtpUpdateMessages,
       "cvIfCountInRtpResponseMessages": cvIfCountInRtpResponseMessages,
       "cvIfCountInRtpRedirectMessages": cvIfCountInRtpRedirectMessages,
       "cvIfCountInRtpIllegalMessages": cvIfCountInRtpIllegalMessages,
       "cvIfCountInSppMessages": cvIfCountInSppMessages,
       "cvIfCountInIpUnknownProtocols": cvIfCountInIpUnknownProtocols,
       "cvIfCountInIpcUnknownPorts": cvIfCountInIpcUnknownPorts,
       "cvIfCountInBroadcastsHelpered": cvIfCountInBroadcastsHelpered,
       "cvIfCountInBroadcastsForwarded": cvIfCountInBroadcastsForwarded,
       "cvIfCountInBroadcastDuplicates": cvIfCountInBroadcastDuplicates,
       "cvIfCountInEchoPackets": cvIfCountInEchoPackets,
       "cvIfCountInMacEchoPackets": cvIfCountInMacEchoPackets,
       "cvIfCountInProxyReplyPackets": cvIfCountInProxyReplyPackets,
       "cvIfCountOutTable": cvIfCountOutTable,
       "cvIfCountOutEntry": cvIfCountOutEntry,
       "cvIfCountOutUnicastPackets": cvIfCountOutUnicastPackets,
       "cvIfCountOutBroadcastPackets": cvIfCountOutBroadcastPackets,
       "cvIfCountOutForwardedPackets": cvIfCountOutForwardedPackets,
       "cvIfCountOutEncapsulationFailures": cvIfCountOutEncapsulationFailures,
       "cvIfCountOutAccessFailures": cvIfCountOutAccessFailures,
       "cvIfCountOutDownFailures": cvIfCountOutDownFailures,
       "cvIfCountOutPacketsNotBroadcastToSource": cvIfCountOutPacketsNotBroadcastToSource,
       "cvIfCountOutPacketsNotBroadcastLanOnly": cvIfCountOutPacketsNotBroadcastLanOnly,
       "cvIfCountOutPacketsNotBroadcastNotOver4800": cvIfCountOutPacketsNotBroadcastNotOver4800,
       "cvIfCountOutPacketsNotBroadcastNoCharge": cvIfCountOutPacketsNotBroadcastNoCharge,
       "cvIfCountOutBroadcastsForwarded": cvIfCountOutBroadcastsForwarded,
       "cvIfCountOutBroadcastsHelpered": cvIfCountOutBroadcastsHelpered,
       "cvIfCountOutArpQueryRequests": cvIfCountOutArpQueryRequests,
       "cvIfCountOutArpQueryResponses": cvIfCountOutArpQueryResponses,
       "cvIfCountOutArpAssignmentRequests": cvIfCountOutArpAssignmentRequests,
       "cvIfCountOutArpAssignmentResponses": cvIfCountOutArpAssignmentResponses,
       "cvIfCountOutIcpErrorMessages": cvIfCountOutIcpErrorMessages,
       "cvIfCountOutIcpMetricMessages": cvIfCountOutIcpMetricMessages,
       "cvIfCountOutIpcMessages": cvIfCountOutIpcMessages,
       "cvIfCountOutRtp0Messages": cvIfCountOutRtp0Messages,
       "cvIfCountOutRtpRequestMessages": cvIfCountOutRtpRequestMessages,
       "cvIfCountOutRtp2Messages": cvIfCountOutRtp2Messages,
       "cvIfCountOutRtp3Messages": cvIfCountOutRtp3Messages,
       "cvIfCountOutRtpUpdateMessages": cvIfCountOutRtpUpdateMessages,
       "cvIfCountOutRtpResponseMessages": cvIfCountOutRtpResponseMessages,
       "cvIfCountOutRtpRedirectMessages": cvIfCountOutRtpRedirectMessages,
       "cvIfCountOutSppMessages": cvIfCountOutSppMessages,
       "cvIfCountOutEchoPackets": cvIfCountOutEchoPackets,
       "cvIfCountOutMacEchoPackets": cvIfCountOutMacEchoPackets,
       "cvIfCountOutProxyPackets": cvIfCountOutProxyPackets,
       "ciscoVinesMIBConformance": ciscoVinesMIBConformance,
       "ciscoVinesMIBCompliances": ciscoVinesMIBCompliances,
       "ciscoVinesMIBCompliance": ciscoVinesMIBCompliance,
       "ciscoVinesMIBGroups": ciscoVinesMIBGroups,
       "ciscoVinesMIBGroup": ciscoVinesMIBGroup}
)
