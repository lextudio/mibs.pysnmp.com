# SNMP MIB module (BENU-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BENU-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:51 2024
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

(benuWAG,) = mibBuilder.importSymbols(
    "BENU-WAG-MIB",
    "benuWAG")

(InetAddressIPv4,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressPrefixLength")

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

bDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6)
)
bDhcpMIB.setRevisions(
        ("2015-12-18 00:00",
         "2015-11-12 00:00",
         "2015-01-29 00:00",
         "2015-01-16 00:00",
         "2014-07-30 00:00",
         "2014-04-14 00:00",
         "2013-10-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BDhcpNotifications_ObjectIdentity = ObjectIdentity
bDhcpNotifications = _BDhcpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 0)
)
if mibBuilder.loadTexts:
    bDhcpNotifications.setStatus("current")
_BDhcpv4MIBObjects_ObjectIdentity = ObjectIdentity
bDhcpv4MIBObjects = _BDhcpv4MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    bDhcpv4MIBObjects.setStatus("current")
_BDhcpSubnetTable_Object = MibTable
bDhcpSubnetTable = _BDhcpSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    bDhcpSubnetTable.setStatus("current")
_BDhcpSubnetEntry_Object = MibTableRow
bDhcpSubnetEntry = _BDhcpSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1)
)
bDhcpSubnetEntry.setIndexNames(
    (0, "BENU-DHCP-MIB", "bDhcpSubnetStatsInterval"),
    (0, "BENU-DHCP-MIB", "bDhcpSubnetIndex"),
    (0, "BENU-DHCP-MIB", "bDhcpSubnetRangeIndex"),
)
if mibBuilder.loadTexts:
    bDhcpSubnetEntry.setStatus("current")
_BDhcpSubnetStatsInterval_Type = Integer32
_BDhcpSubnetStatsInterval_Object = MibTableColumn
bDhcpSubnetStatsInterval = _BDhcpSubnetStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 1),
    _BDhcpSubnetStatsInterval_Type()
)
bDhcpSubnetStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDhcpSubnetStatsInterval.setStatus("current")


class _BDhcpSubnetIndex_Type(Integer32):
    """Custom type bDhcpSubnetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 144),
    )


_BDhcpSubnetIndex_Type.__name__ = "Integer32"
_BDhcpSubnetIndex_Object = MibTableColumn
bDhcpSubnetIndex = _BDhcpSubnetIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 2),
    _BDhcpSubnetIndex_Type()
)
bDhcpSubnetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDhcpSubnetIndex.setStatus("current")


class _BDhcpSubnetRangeIndex_Type(Integer32):
    """Custom type bDhcpSubnetRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BDhcpSubnetRangeIndex_Type.__name__ = "Integer32"
_BDhcpSubnetRangeIndex_Object = MibTableColumn
bDhcpSubnetRangeIndex = _BDhcpSubnetRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 3),
    _BDhcpSubnetRangeIndex_Type()
)
bDhcpSubnetRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDhcpSubnetRangeIndex.setStatus("current")
_BDhcpSubnetIntervalDuration_Type = Integer32
_BDhcpSubnetIntervalDuration_Object = MibTableColumn
bDhcpSubnetIntervalDuration = _BDhcpSubnetIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 4),
    _BDhcpSubnetIntervalDuration_Type()
)
bDhcpSubnetIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetIntervalDuration.setStatus("current")
_BDhcpSubnetStartAddress_Type = InetAddressIPv4
_BDhcpSubnetStartAddress_Object = MibTableColumn
bDhcpSubnetStartAddress = _BDhcpSubnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 5),
    _BDhcpSubnetStartAddress_Type()
)
bDhcpSubnetStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetStartAddress.setStatus("current")
_BDhcpSubnetEndAddress_Type = InetAddressIPv4
_BDhcpSubnetEndAddress_Object = MibTableColumn
bDhcpSubnetEndAddress = _BDhcpSubnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 6),
    _BDhcpSubnetEndAddress_Type()
)
bDhcpSubnetEndAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetEndAddress.setStatus("current")
_BDhcpSubnetTotalAddresses_Type = Unsigned32
_BDhcpSubnetTotalAddresses_Object = MibTableColumn
bDhcpSubnetTotalAddresses = _BDhcpSubnetTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 7),
    _BDhcpSubnetTotalAddresses_Type()
)
bDhcpSubnetTotalAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetTotalAddresses.setStatus("current")
_BDhcpSubnetPeakFreeAddresses_Type = Unsigned32
_BDhcpSubnetPeakFreeAddresses_Object = MibTableColumn
bDhcpSubnetPeakFreeAddresses = _BDhcpSubnetPeakFreeAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 8),
    _BDhcpSubnetPeakFreeAddresses_Type()
)
bDhcpSubnetPeakFreeAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetPeakFreeAddresses.setStatus("current")
_BDhcpSubnetPeakUsedAddresses_Type = Unsigned32
_BDhcpSubnetPeakUsedAddresses_Object = MibTableColumn
bDhcpSubnetPeakUsedAddresses = _BDhcpSubnetPeakUsedAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 9),
    _BDhcpSubnetPeakUsedAddresses_Type()
)
bDhcpSubnetPeakUsedAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetPeakUsedAddresses.setStatus("current")
_BDhcpSubnetAddress_Type = InetAddressIPv4
_BDhcpSubnetAddress_Object = MibTableColumn
bDhcpSubnetAddress = _BDhcpSubnetAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 10),
    _BDhcpSubnetAddress_Type()
)
bDhcpSubnetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetAddress.setStatus("current")
_BDhcpSubnetMask_Type = InetAddressPrefixLength
_BDhcpSubnetMask_Object = MibTableColumn
bDhcpSubnetMask = _BDhcpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 11),
    _BDhcpSubnetMask_Type()
)
bDhcpSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetMask.setStatus("current")
_BDhcpSubnetUsedAddrLowThreshold_Type = Unsigned32
_BDhcpSubnetUsedAddrLowThreshold_Object = MibTableColumn
bDhcpSubnetUsedAddrLowThreshold = _BDhcpSubnetUsedAddrLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 12),
    _BDhcpSubnetUsedAddrLowThreshold_Type()
)
bDhcpSubnetUsedAddrLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetUsedAddrLowThreshold.setStatus("current")
_BDhcpSubnetUsedAddrHighThreshold_Type = Unsigned32
_BDhcpSubnetUsedAddrHighThreshold_Object = MibTableColumn
bDhcpSubnetUsedAddrHighThreshold = _BDhcpSubnetUsedAddrHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 13),
    _BDhcpSubnetUsedAddrHighThreshold_Type()
)
bDhcpSubnetUsedAddrHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetUsedAddrHighThreshold.setStatus("current")
_BDhcpSubnetPeakHoldAddresses_Type = Unsigned32
_BDhcpSubnetPeakHoldAddresses_Object = MibTableColumn
bDhcpSubnetPeakHoldAddresses = _BDhcpSubnetPeakHoldAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 1, 1, 14),
    _BDhcpSubnetPeakHoldAddresses_Type()
)
bDhcpSubnetPeakHoldAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSubnetPeakHoldAddresses.setStatus("current")
_BDhcpGlobalTable_Object = MibTable
bDhcpGlobalTable = _BDhcpGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    bDhcpGlobalTable.setStatus("current")
_BDhcpGlobalEntry_Object = MibTableRow
bDhcpGlobalEntry = _BDhcpGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1)
)
bDhcpGlobalEntry.setIndexNames(
    (0, "BENU-DHCP-MIB", "bDhcpGlobalStatsInterval"),
)
if mibBuilder.loadTexts:
    bDhcpGlobalEntry.setStatus("current")
_BDhcpGlobalStatsInterval_Type = Integer32
_BDhcpGlobalStatsInterval_Object = MibTableColumn
bDhcpGlobalStatsInterval = _BDhcpGlobalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 1),
    _BDhcpGlobalStatsInterval_Type()
)
bDhcpGlobalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDhcpGlobalStatsInterval.setStatus("current")
_BDhcpDiscoversRcvd_Type = Unsigned32
_BDhcpDiscoversRcvd_Object = MibTableColumn
bDhcpDiscoversRcvd = _BDhcpDiscoversRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 2),
    _BDhcpDiscoversRcvd_Type()
)
bDhcpDiscoversRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpDiscoversRcvd.setStatus("current")
_BDhcpOffersSent_Type = Unsigned32
_BDhcpOffersSent_Object = MibTableColumn
bDhcpOffersSent = _BDhcpOffersSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 3),
    _BDhcpOffersSent_Type()
)
bDhcpOffersSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpOffersSent.setStatus("current")
_BDhcpRequestsRcvd_Type = Unsigned32
_BDhcpRequestsRcvd_Object = MibTableColumn
bDhcpRequestsRcvd = _BDhcpRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 4),
    _BDhcpRequestsRcvd_Type()
)
bDhcpRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpRequestsRcvd.setStatus("current")
_BDhcpDeclinesRcvd_Type = Unsigned32
_BDhcpDeclinesRcvd_Object = MibTableColumn
bDhcpDeclinesRcvd = _BDhcpDeclinesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 5),
    _BDhcpDeclinesRcvd_Type()
)
bDhcpDeclinesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpDeclinesRcvd.setStatus("current")
_BDhcpAcksSent_Type = Unsigned32
_BDhcpAcksSent_Object = MibTableColumn
bDhcpAcksSent = _BDhcpAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 6),
    _BDhcpAcksSent_Type()
)
bDhcpAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpAcksSent.setStatus("current")
_BDhcpNacksSent_Type = Unsigned32
_BDhcpNacksSent_Object = MibTableColumn
bDhcpNacksSent = _BDhcpNacksSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 7),
    _BDhcpNacksSent_Type()
)
bDhcpNacksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpNacksSent.setStatus("current")
_BDhcpReleasesRcvd_Type = Unsigned32
_BDhcpReleasesRcvd_Object = MibTableColumn
bDhcpReleasesRcvd = _BDhcpReleasesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 8),
    _BDhcpReleasesRcvd_Type()
)
bDhcpReleasesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpReleasesRcvd.setStatus("current")
_BDhcpReleasesIndRcvd_Type = Unsigned32
_BDhcpReleasesIndRcvd_Object = MibTableColumn
bDhcpReleasesIndRcvd = _BDhcpReleasesIndRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 9),
    _BDhcpReleasesIndRcvd_Type()
)
bDhcpReleasesIndRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpReleasesIndRcvd.setStatus("current")
_BDhcpReleasesSent_Type = Unsigned32
_BDhcpReleasesSent_Object = MibTableColumn
bDhcpReleasesSent = _BDhcpReleasesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 10),
    _BDhcpReleasesSent_Type()
)
bDhcpReleasesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpReleasesSent.setStatus("current")
_BDhcpInformsRcvd_Type = Unsigned32
_BDhcpInformsRcvd_Object = MibTableColumn
bDhcpInformsRcvd = _BDhcpInformsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 11),
    _BDhcpInformsRcvd_Type()
)
bDhcpInformsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpInformsRcvd.setStatus("current")
_BDhcpInformsAckSent_Type = Unsigned32
_BDhcpInformsAckSent_Object = MibTableColumn
bDhcpInformsAckSent = _BDhcpInformsAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 12),
    _BDhcpInformsAckSent_Type()
)
bDhcpInformsAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpInformsAckSent.setStatus("current")
_BDhcpDropDiscover_Type = Unsigned32
_BDhcpDropDiscover_Object = MibTableColumn
bDhcpDropDiscover = _BDhcpDropDiscover_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 13),
    _BDhcpDropDiscover_Type()
)
bDhcpDropDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpDropDiscover.setStatus("current")
_BDhcpDropRequest_Type = Unsigned32
_BDhcpDropRequest_Object = MibTableColumn
bDhcpDropRequest = _BDhcpDropRequest_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 14),
    _BDhcpDropRequest_Type()
)
bDhcpDropRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpDropRequest.setStatus("current")
_BDhcpDropRelease_Type = Unsigned32
_BDhcpDropRelease_Object = MibTableColumn
bDhcpDropRelease = _BDhcpDropRelease_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 15),
    _BDhcpDropRelease_Type()
)
bDhcpDropRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpDropRelease.setStatus("current")
_BDhcpLeasesAssigned_Type = Unsigned32
_BDhcpLeasesAssigned_Object = MibTableColumn
bDhcpLeasesAssigned = _BDhcpLeasesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 16),
    _BDhcpLeasesAssigned_Type()
)
bDhcpLeasesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesAssigned.setStatus("current")
_BDhcpLeasesReleased_Type = Unsigned32
_BDhcpLeasesReleased_Object = MibTableColumn
bDhcpLeasesReleased = _BDhcpLeasesReleased_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 17),
    _BDhcpLeasesReleased_Type()
)
bDhcpLeasesReleased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesReleased.setStatus("current")
_BDhcpLeasesRelFail_Type = Unsigned32
_BDhcpLeasesRelFail_Object = MibTableColumn
bDhcpLeasesRelFail = _BDhcpLeasesRelFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 18),
    _BDhcpLeasesRelFail_Type()
)
bDhcpLeasesRelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesRelFail.setStatus("current")
_BDhcpLeasesExpired_Type = Unsigned32
_BDhcpLeasesExpired_Object = MibTableColumn
bDhcpLeasesExpired = _BDhcpLeasesExpired_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 19),
    _BDhcpLeasesExpired_Type()
)
bDhcpLeasesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesExpired.setStatus("current")
_BDhcpLeasesRenewed_Type = Unsigned32
_BDhcpLeasesRenewed_Object = MibTableColumn
bDhcpLeasesRenewed = _BDhcpLeasesRenewed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 20),
    _BDhcpLeasesRenewed_Type()
)
bDhcpLeasesRenewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesRenewed.setStatus("current")
_BDhcpLeasesRenewFail_Type = Unsigned32
_BDhcpLeasesRenewFail_Object = MibTableColumn
bDhcpLeasesRenewFail = _BDhcpLeasesRenewFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 21),
    _BDhcpLeasesRenewFail_Type()
)
bDhcpLeasesRenewFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesRenewFail.setStatus("current")
_BDhcpLeasesNotAssignServIntNotConfig_Type = Unsigned32
_BDhcpLeasesNotAssignServIntNotConfig_Object = MibTableColumn
bDhcpLeasesNotAssignServIntNotConfig = _BDhcpLeasesNotAssignServIntNotConfig_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 22),
    _BDhcpLeasesNotAssignServIntNotConfig_Type()
)
bDhcpLeasesNotAssignServIntNotConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesNotAssignServIntNotConfig.setStatus("current")
_BDhcpLeasesNotAssignFreeBuffUnavail_Type = Unsigned32
_BDhcpLeasesNotAssignFreeBuffUnavail_Object = MibTableColumn
bDhcpLeasesNotAssignFreeBuffUnavail = _BDhcpLeasesNotAssignFreeBuffUnavail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 23),
    _BDhcpLeasesNotAssignFreeBuffUnavail_Type()
)
bDhcpLeasesNotAssignFreeBuffUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpLeasesNotAssignFreeBuffUnavail.setStatus("current")
_BDhcpIntervalDuration_Type = Integer32
_BDhcpIntervalDuration_Object = MibTableColumn
bDhcpIntervalDuration = _BDhcpIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 24),
    _BDhcpIntervalDuration_Type()
)
bDhcpIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpIntervalDuration.setStatus("current")
_BBootpRequestsRcvd_Type = Unsigned32
_BBootpRequestsRcvd_Object = MibTableColumn
bBootpRequestsRcvd = _BBootpRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 25),
    _BBootpRequestsRcvd_Type()
)
bBootpRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bBootpRequestsRcvd.setStatus("current")
_BBootpRepliesSent_Type = Unsigned32
_BBootpRepliesSent_Object = MibTableColumn
bBootpRepliesSent = _BBootpRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 26),
    _BBootpRepliesSent_Type()
)
bBootpRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bBootpRepliesSent.setStatus("current")
_BDhcpReleasesIndSent_Type = Unsigned32
_BDhcpReleasesIndSent_Object = MibTableColumn
bDhcpReleasesIndSent = _BDhcpReleasesIndSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 2, 1, 27),
    _BDhcpReleasesIndSent_Type()
)
bDhcpReleasesIndSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpReleasesIndSent.setStatus("current")
_BDhcpv4ActiveClient_Type = Unsigned32
_BDhcpv4ActiveClient_Object = MibScalar
bDhcpv4ActiveClient = _BDhcpv4ActiveClient_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 3),
    _BDhcpv4ActiveClient_Type()
)
bDhcpv4ActiveClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv4ActiveClient.setStatus("current")
_BDhcpSPWiFiGlobalTable_Object = MibTable
bDhcpSPWiFiGlobalTable = _BDhcpSPWiFiGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    bDhcpSPWiFiGlobalTable.setStatus("current")
_BDhcpSPWiFiGlobalEntry_Object = MibTableRow
bDhcpSPWiFiGlobalEntry = _BDhcpSPWiFiGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1)
)
bDhcpSPWiFiGlobalEntry.setIndexNames(
    (0, "BENU-DHCP-MIB", "bDhcpSPWiFiGlobalStatsInterval"),
)
if mibBuilder.loadTexts:
    bDhcpSPWiFiGlobalEntry.setStatus("current")
_BDhcpSPWiFiGlobalStatsInterval_Type = Integer32
_BDhcpSPWiFiGlobalStatsInterval_Object = MibTableColumn
bDhcpSPWiFiGlobalStatsInterval = _BDhcpSPWiFiGlobalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 1),
    _BDhcpSPWiFiGlobalStatsInterval_Type()
)
bDhcpSPWiFiGlobalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDhcpSPWiFiGlobalStatsInterval.setStatus("current")
_BDhcpSPWiFiDiscoversRcvd_Type = Unsigned32
_BDhcpSPWiFiDiscoversRcvd_Object = MibTableColumn
bDhcpSPWiFiDiscoversRcvd = _BDhcpSPWiFiDiscoversRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 2),
    _BDhcpSPWiFiDiscoversRcvd_Type()
)
bDhcpSPWiFiDiscoversRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiDiscoversRcvd.setStatus("current")
_BDhcpSPWiFiOffersSent_Type = Unsigned32
_BDhcpSPWiFiOffersSent_Object = MibTableColumn
bDhcpSPWiFiOffersSent = _BDhcpSPWiFiOffersSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 3),
    _BDhcpSPWiFiOffersSent_Type()
)
bDhcpSPWiFiOffersSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiOffersSent.setStatus("current")
_BDhcpSPWiFiRequestsRcvd_Type = Unsigned32
_BDhcpSPWiFiRequestsRcvd_Object = MibTableColumn
bDhcpSPWiFiRequestsRcvd = _BDhcpSPWiFiRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 4),
    _BDhcpSPWiFiRequestsRcvd_Type()
)
bDhcpSPWiFiRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiRequestsRcvd.setStatus("current")
_BDhcpSPWiFiDeclinesRcvd_Type = Unsigned32
_BDhcpSPWiFiDeclinesRcvd_Object = MibTableColumn
bDhcpSPWiFiDeclinesRcvd = _BDhcpSPWiFiDeclinesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 5),
    _BDhcpSPWiFiDeclinesRcvd_Type()
)
bDhcpSPWiFiDeclinesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiDeclinesRcvd.setStatus("current")
_BDhcpSPWiFiAcksSent_Type = Unsigned32
_BDhcpSPWiFiAcksSent_Object = MibTableColumn
bDhcpSPWiFiAcksSent = _BDhcpSPWiFiAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 6),
    _BDhcpSPWiFiAcksSent_Type()
)
bDhcpSPWiFiAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiAcksSent.setStatus("current")
_BDhcpSPWiFiNacksSent_Type = Unsigned32
_BDhcpSPWiFiNacksSent_Object = MibTableColumn
bDhcpSPWiFiNacksSent = _BDhcpSPWiFiNacksSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 7),
    _BDhcpSPWiFiNacksSent_Type()
)
bDhcpSPWiFiNacksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiNacksSent.setStatus("current")
_BDhcpSPWiFiReleasesRcvd_Type = Unsigned32
_BDhcpSPWiFiReleasesRcvd_Object = MibTableColumn
bDhcpSPWiFiReleasesRcvd = _BDhcpSPWiFiReleasesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 8),
    _BDhcpSPWiFiReleasesRcvd_Type()
)
bDhcpSPWiFiReleasesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiReleasesRcvd.setStatus("current")
_BDhcpSPWiFiReleasesIndRcvd_Type = Unsigned32
_BDhcpSPWiFiReleasesIndRcvd_Object = MibTableColumn
bDhcpSPWiFiReleasesIndRcvd = _BDhcpSPWiFiReleasesIndRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 9),
    _BDhcpSPWiFiReleasesIndRcvd_Type()
)
bDhcpSPWiFiReleasesIndRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiReleasesIndRcvd.setStatus("current")
_BDhcpSPWiFiReleasesSent_Type = Unsigned32
_BDhcpSPWiFiReleasesSent_Object = MibTableColumn
bDhcpSPWiFiReleasesSent = _BDhcpSPWiFiReleasesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 10),
    _BDhcpSPWiFiReleasesSent_Type()
)
bDhcpSPWiFiReleasesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiReleasesSent.setStatus("current")
_BDhcpSPWiFiInformsRcvd_Type = Unsigned32
_BDhcpSPWiFiInformsRcvd_Object = MibTableColumn
bDhcpSPWiFiInformsRcvd = _BDhcpSPWiFiInformsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 11),
    _BDhcpSPWiFiInformsRcvd_Type()
)
bDhcpSPWiFiInformsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiInformsRcvd.setStatus("current")
_BDhcpSPWiFiInformsAckSent_Type = Unsigned32
_BDhcpSPWiFiInformsAckSent_Object = MibTableColumn
bDhcpSPWiFiInformsAckSent = _BDhcpSPWiFiInformsAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 12),
    _BDhcpSPWiFiInformsAckSent_Type()
)
bDhcpSPWiFiInformsAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiInformsAckSent.setStatus("current")
_BDhcpSPWiFiDropDiscover_Type = Unsigned32
_BDhcpSPWiFiDropDiscover_Object = MibTableColumn
bDhcpSPWiFiDropDiscover = _BDhcpSPWiFiDropDiscover_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 13),
    _BDhcpSPWiFiDropDiscover_Type()
)
bDhcpSPWiFiDropDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiDropDiscover.setStatus("current")
_BDhcpSPWiFiDropRequest_Type = Unsigned32
_BDhcpSPWiFiDropRequest_Object = MibTableColumn
bDhcpSPWiFiDropRequest = _BDhcpSPWiFiDropRequest_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 14),
    _BDhcpSPWiFiDropRequest_Type()
)
bDhcpSPWiFiDropRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiDropRequest.setStatus("current")
_BDhcpSPWiFiDropRelease_Type = Unsigned32
_BDhcpSPWiFiDropRelease_Object = MibTableColumn
bDhcpSPWiFiDropRelease = _BDhcpSPWiFiDropRelease_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 15),
    _BDhcpSPWiFiDropRelease_Type()
)
bDhcpSPWiFiDropRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiDropRelease.setStatus("current")
_BDhcpSPWiFiLeasesAssigned_Type = Unsigned32
_BDhcpSPWiFiLeasesAssigned_Object = MibTableColumn
bDhcpSPWiFiLeasesAssigned = _BDhcpSPWiFiLeasesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 16),
    _BDhcpSPWiFiLeasesAssigned_Type()
)
bDhcpSPWiFiLeasesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesAssigned.setStatus("current")
_BDhcpSPWiFiLeasesReleased_Type = Unsigned32
_BDhcpSPWiFiLeasesReleased_Object = MibTableColumn
bDhcpSPWiFiLeasesReleased = _BDhcpSPWiFiLeasesReleased_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 17),
    _BDhcpSPWiFiLeasesReleased_Type()
)
bDhcpSPWiFiLeasesReleased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesReleased.setStatus("current")
_BDhcpSPWiFiLeasesRelFail_Type = Unsigned32
_BDhcpSPWiFiLeasesRelFail_Object = MibTableColumn
bDhcpSPWiFiLeasesRelFail = _BDhcpSPWiFiLeasesRelFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 18),
    _BDhcpSPWiFiLeasesRelFail_Type()
)
bDhcpSPWiFiLeasesRelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesRelFail.setStatus("current")
_BDhcpSPWiFiLeasesExpired_Type = Unsigned32
_BDhcpSPWiFiLeasesExpired_Object = MibTableColumn
bDhcpSPWiFiLeasesExpired = _BDhcpSPWiFiLeasesExpired_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 19),
    _BDhcpSPWiFiLeasesExpired_Type()
)
bDhcpSPWiFiLeasesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesExpired.setStatus("current")
_BDhcpSPWiFiLeasesRenewed_Type = Unsigned32
_BDhcpSPWiFiLeasesRenewed_Object = MibTableColumn
bDhcpSPWiFiLeasesRenewed = _BDhcpSPWiFiLeasesRenewed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 20),
    _BDhcpSPWiFiLeasesRenewed_Type()
)
bDhcpSPWiFiLeasesRenewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesRenewed.setStatus("current")
_BDhcpSPWiFiLeasesRenewFail_Type = Unsigned32
_BDhcpSPWiFiLeasesRenewFail_Object = MibTableColumn
bDhcpSPWiFiLeasesRenewFail = _BDhcpSPWiFiLeasesRenewFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 21),
    _BDhcpSPWiFiLeasesRenewFail_Type()
)
bDhcpSPWiFiLeasesRenewFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesRenewFail.setStatus("current")
_BDhcpSPWiFiLeasesNotAssignServIntNotConfig_Type = Unsigned32
_BDhcpSPWiFiLeasesNotAssignServIntNotConfig_Object = MibTableColumn
bDhcpSPWiFiLeasesNotAssignServIntNotConfig = _BDhcpSPWiFiLeasesNotAssignServIntNotConfig_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 22),
    _BDhcpSPWiFiLeasesNotAssignServIntNotConfig_Type()
)
bDhcpSPWiFiLeasesNotAssignServIntNotConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesNotAssignServIntNotConfig.setStatus("current")
_BDhcpSPWiFiLeasesNotAssignFreeBuffUnavail_Type = Unsigned32
_BDhcpSPWiFiLeasesNotAssignFreeBuffUnavail_Object = MibTableColumn
bDhcpSPWiFiLeasesNotAssignFreeBuffUnavail = _BDhcpSPWiFiLeasesNotAssignFreeBuffUnavail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 23),
    _BDhcpSPWiFiLeasesNotAssignFreeBuffUnavail_Type()
)
bDhcpSPWiFiLeasesNotAssignFreeBuffUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiLeasesNotAssignFreeBuffUnavail.setStatus("current")
_BDhcpSPWiFiIntervalDuration_Type = Integer32
_BDhcpSPWiFiIntervalDuration_Object = MibTableColumn
bDhcpSPWiFiIntervalDuration = _BDhcpSPWiFiIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 24),
    _BDhcpSPWiFiIntervalDuration_Type()
)
bDhcpSPWiFiIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiIntervalDuration.setStatus("current")
_BSPWiFiBootpRequestsRcvd_Type = Unsigned32
_BSPWiFiBootpRequestsRcvd_Object = MibTableColumn
bSPWiFiBootpRequestsRcvd = _BSPWiFiBootpRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 25),
    _BSPWiFiBootpRequestsRcvd_Type()
)
bSPWiFiBootpRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSPWiFiBootpRequestsRcvd.setStatus("current")
_BSPWiFiBootpRepliesSent_Type = Unsigned32
_BSPWiFiBootpRepliesSent_Object = MibTableColumn
bSPWiFiBootpRepliesSent = _BSPWiFiBootpRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 26),
    _BSPWiFiBootpRepliesSent_Type()
)
bSPWiFiBootpRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bSPWiFiBootpRepliesSent.setStatus("current")
_BDhcpSPWiFiReleasesIndSent_Type = Unsigned32
_BDhcpSPWiFiReleasesIndSent_Object = MibTableColumn
bDhcpSPWiFiReleasesIndSent = _BDhcpSPWiFiReleasesIndSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 4, 1, 27),
    _BDhcpSPWiFiReleasesIndSent_Type()
)
bDhcpSPWiFiReleasesIndSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpSPWiFiReleasesIndSent.setStatus("current")
_BDhcpHomeGlobalTable_Object = MibTable
bDhcpHomeGlobalTable = _BDhcpHomeGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5)
)
if mibBuilder.loadTexts:
    bDhcpHomeGlobalTable.setStatus("current")
_BDhcpHomeGlobalEntry_Object = MibTableRow
bDhcpHomeGlobalEntry = _BDhcpHomeGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1)
)
bDhcpHomeGlobalEntry.setIndexNames(
    (0, "BENU-DHCP-MIB", "bDhcpHomeGlobalStatsInterval"),
)
if mibBuilder.loadTexts:
    bDhcpHomeGlobalEntry.setStatus("current")
_BDhcpHomeGlobalStatsInterval_Type = Integer32
_BDhcpHomeGlobalStatsInterval_Object = MibTableColumn
bDhcpHomeGlobalStatsInterval = _BDhcpHomeGlobalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 1),
    _BDhcpHomeGlobalStatsInterval_Type()
)
bDhcpHomeGlobalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDhcpHomeGlobalStatsInterval.setStatus("current")
_BDhcpHomeDiscoversRcvd_Type = Unsigned32
_BDhcpHomeDiscoversRcvd_Object = MibTableColumn
bDhcpHomeDiscoversRcvd = _BDhcpHomeDiscoversRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 2),
    _BDhcpHomeDiscoversRcvd_Type()
)
bDhcpHomeDiscoversRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeDiscoversRcvd.setStatus("current")
_BDhcpHomeOffersSent_Type = Unsigned32
_BDhcpHomeOffersSent_Object = MibTableColumn
bDhcpHomeOffersSent = _BDhcpHomeOffersSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 3),
    _BDhcpHomeOffersSent_Type()
)
bDhcpHomeOffersSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeOffersSent.setStatus("current")
_BDhcpHomeRequestsRcvd_Type = Unsigned32
_BDhcpHomeRequestsRcvd_Object = MibTableColumn
bDhcpHomeRequestsRcvd = _BDhcpHomeRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 4),
    _BDhcpHomeRequestsRcvd_Type()
)
bDhcpHomeRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeRequestsRcvd.setStatus("current")
_BDhcpHomeDeclinesRcvd_Type = Unsigned32
_BDhcpHomeDeclinesRcvd_Object = MibTableColumn
bDhcpHomeDeclinesRcvd = _BDhcpHomeDeclinesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 5),
    _BDhcpHomeDeclinesRcvd_Type()
)
bDhcpHomeDeclinesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeDeclinesRcvd.setStatus("current")
_BDhcpHomeAcksSent_Type = Unsigned32
_BDhcpHomeAcksSent_Object = MibTableColumn
bDhcpHomeAcksSent = _BDhcpHomeAcksSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 6),
    _BDhcpHomeAcksSent_Type()
)
bDhcpHomeAcksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeAcksSent.setStatus("current")
_BDhcpHomeNacksSent_Type = Unsigned32
_BDhcpHomeNacksSent_Object = MibTableColumn
bDhcpHomeNacksSent = _BDhcpHomeNacksSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 7),
    _BDhcpHomeNacksSent_Type()
)
bDhcpHomeNacksSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeNacksSent.setStatus("current")
_BDhcpHomeReleasesRcvd_Type = Unsigned32
_BDhcpHomeReleasesRcvd_Object = MibTableColumn
bDhcpHomeReleasesRcvd = _BDhcpHomeReleasesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 8),
    _BDhcpHomeReleasesRcvd_Type()
)
bDhcpHomeReleasesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeReleasesRcvd.setStatus("current")
_BDhcpHomeReleasesIndRcvd_Type = Unsigned32
_BDhcpHomeReleasesIndRcvd_Object = MibTableColumn
bDhcpHomeReleasesIndRcvd = _BDhcpHomeReleasesIndRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 9),
    _BDhcpHomeReleasesIndRcvd_Type()
)
bDhcpHomeReleasesIndRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeReleasesIndRcvd.setStatus("current")
_BDhcpHomeReleasesSent_Type = Unsigned32
_BDhcpHomeReleasesSent_Object = MibTableColumn
bDhcpHomeReleasesSent = _BDhcpHomeReleasesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 10),
    _BDhcpHomeReleasesSent_Type()
)
bDhcpHomeReleasesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeReleasesSent.setStatus("current")
_BDhcpHomeInformsRcvd_Type = Unsigned32
_BDhcpHomeInformsRcvd_Object = MibTableColumn
bDhcpHomeInformsRcvd = _BDhcpHomeInformsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 11),
    _BDhcpHomeInformsRcvd_Type()
)
bDhcpHomeInformsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeInformsRcvd.setStatus("current")
_BDhcpHomeInformsAckSent_Type = Unsigned32
_BDhcpHomeInformsAckSent_Object = MibTableColumn
bDhcpHomeInformsAckSent = _BDhcpHomeInformsAckSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 12),
    _BDhcpHomeInformsAckSent_Type()
)
bDhcpHomeInformsAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeInformsAckSent.setStatus("current")
_BDhcpHomeDropDiscover_Type = Unsigned32
_BDhcpHomeDropDiscover_Object = MibTableColumn
bDhcpHomeDropDiscover = _BDhcpHomeDropDiscover_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 13),
    _BDhcpHomeDropDiscover_Type()
)
bDhcpHomeDropDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeDropDiscover.setStatus("current")
_BDhcpHomeDropRequest_Type = Unsigned32
_BDhcpHomeDropRequest_Object = MibTableColumn
bDhcpHomeDropRequest = _BDhcpHomeDropRequest_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 14),
    _BDhcpHomeDropRequest_Type()
)
bDhcpHomeDropRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeDropRequest.setStatus("current")
_BDhcpHomeDropRelease_Type = Unsigned32
_BDhcpHomeDropRelease_Object = MibTableColumn
bDhcpHomeDropRelease = _BDhcpHomeDropRelease_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 15),
    _BDhcpHomeDropRelease_Type()
)
bDhcpHomeDropRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeDropRelease.setStatus("current")
_BDhcpHomeLeasesAssigned_Type = Unsigned32
_BDhcpHomeLeasesAssigned_Object = MibTableColumn
bDhcpHomeLeasesAssigned = _BDhcpHomeLeasesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 16),
    _BDhcpHomeLeasesAssigned_Type()
)
bDhcpHomeLeasesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesAssigned.setStatus("current")
_BDhcpHomeLeasesReleased_Type = Unsigned32
_BDhcpHomeLeasesReleased_Object = MibTableColumn
bDhcpHomeLeasesReleased = _BDhcpHomeLeasesReleased_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 17),
    _BDhcpHomeLeasesReleased_Type()
)
bDhcpHomeLeasesReleased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesReleased.setStatus("current")
_BDhcpHomeLeasesRelFail_Type = Unsigned32
_BDhcpHomeLeasesRelFail_Object = MibTableColumn
bDhcpHomeLeasesRelFail = _BDhcpHomeLeasesRelFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 18),
    _BDhcpHomeLeasesRelFail_Type()
)
bDhcpHomeLeasesRelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesRelFail.setStatus("current")
_BDhcpHomeLeasesExpired_Type = Unsigned32
_BDhcpHomeLeasesExpired_Object = MibTableColumn
bDhcpHomeLeasesExpired = _BDhcpHomeLeasesExpired_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 19),
    _BDhcpHomeLeasesExpired_Type()
)
bDhcpHomeLeasesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesExpired.setStatus("current")
_BDhcpHomeLeasesRenewed_Type = Unsigned32
_BDhcpHomeLeasesRenewed_Object = MibTableColumn
bDhcpHomeLeasesRenewed = _BDhcpHomeLeasesRenewed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 20),
    _BDhcpHomeLeasesRenewed_Type()
)
bDhcpHomeLeasesRenewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesRenewed.setStatus("current")
_BDhcpHomeLeasesRenewFail_Type = Unsigned32
_BDhcpHomeLeasesRenewFail_Object = MibTableColumn
bDhcpHomeLeasesRenewFail = _BDhcpHomeLeasesRenewFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 21),
    _BDhcpHomeLeasesRenewFail_Type()
)
bDhcpHomeLeasesRenewFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesRenewFail.setStatus("current")
_BDhcpHomeLeasesNotAssignServIntNotConfig_Type = Unsigned32
_BDhcpHomeLeasesNotAssignServIntNotConfig_Object = MibTableColumn
bDhcpHomeLeasesNotAssignServIntNotConfig = _BDhcpHomeLeasesNotAssignServIntNotConfig_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 22),
    _BDhcpHomeLeasesNotAssignServIntNotConfig_Type()
)
bDhcpHomeLeasesNotAssignServIntNotConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesNotAssignServIntNotConfig.setStatus("current")
_BDhcpHomeLeasesNotAssignFreeBuffUnavail_Type = Unsigned32
_BDhcpHomeLeasesNotAssignFreeBuffUnavail_Object = MibTableColumn
bDhcpHomeLeasesNotAssignFreeBuffUnavail = _BDhcpHomeLeasesNotAssignFreeBuffUnavail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 23),
    _BDhcpHomeLeasesNotAssignFreeBuffUnavail_Type()
)
bDhcpHomeLeasesNotAssignFreeBuffUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeLeasesNotAssignFreeBuffUnavail.setStatus("current")
_BDhcpHomeIntervalDuration_Type = Integer32
_BDhcpHomeIntervalDuration_Object = MibTableColumn
bDhcpHomeIntervalDuration = _BDhcpHomeIntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 24),
    _BDhcpHomeIntervalDuration_Type()
)
bDhcpHomeIntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeIntervalDuration.setStatus("current")
_BHomeBootpRequestsRcvd_Type = Unsigned32
_BHomeBootpRequestsRcvd_Object = MibTableColumn
bHomeBootpRequestsRcvd = _BHomeBootpRequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 25),
    _BHomeBootpRequestsRcvd_Type()
)
bHomeBootpRequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHomeBootpRequestsRcvd.setStatus("current")
_BHomeBootpRepliesSent_Type = Unsigned32
_BHomeBootpRepliesSent_Object = MibTableColumn
bHomeBootpRepliesSent = _BHomeBootpRepliesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 26),
    _BHomeBootpRepliesSent_Type()
)
bHomeBootpRepliesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bHomeBootpRepliesSent.setStatus("current")
_BDhcpHomeReleasesIndSent_Type = Unsigned32
_BDhcpHomeReleasesIndSent_Object = MibTableColumn
bDhcpHomeReleasesIndSent = _BDhcpHomeReleasesIndSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 5, 1, 27),
    _BDhcpHomeReleasesIndSent_Type()
)
bDhcpHomeReleasesIndSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpHomeReleasesIndSent.setStatus("current")
_BDhcpv4ActiveSpWiFiClients_Type = Unsigned32
_BDhcpv4ActiveSpWiFiClients_Object = MibScalar
bDhcpv4ActiveSpWiFiClients = _BDhcpv4ActiveSpWiFiClients_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 6),
    _BDhcpv4ActiveSpWiFiClients_Type()
)
bDhcpv4ActiveSpWiFiClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv4ActiveSpWiFiClients.setStatus("current")
_BDhcpv4ActiveHomeClients_Type = Unsigned32
_BDhcpv4ActiveHomeClients_Object = MibScalar
bDhcpv4ActiveHomeClients = _BDhcpv4ActiveHomeClients_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 1, 7),
    _BDhcpv4ActiveHomeClients_Type()
)
bDhcpv4ActiveHomeClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv4ActiveHomeClients.setStatus("current")
_BDhcpv4NotifObjects_ObjectIdentity = ObjectIdentity
bDhcpv4NotifObjects = _BDhcpv4NotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 2)
)
if mibBuilder.loadTexts:
    bDhcpv4NotifObjects.setStatus("current")
_BDhcpHomeSubnetHomeId_Type = Unsigned32
_BDhcpHomeSubnetHomeId_Object = MibScalar
bDhcpHomeSubnetHomeId = _BDhcpHomeSubnetHomeId_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 2, 1),
    _BDhcpHomeSubnetHomeId_Type()
)
bDhcpHomeSubnetHomeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bDhcpHomeSubnetHomeId.setStatus("current")
_BDhcpHomeSubnetStartAddress_Type = InetAddressIPv4
_BDhcpHomeSubnetStartAddress_Object = MibScalar
bDhcpHomeSubnetStartAddress = _BDhcpHomeSubnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 2, 2),
    _BDhcpHomeSubnetStartAddress_Type()
)
bDhcpHomeSubnetStartAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bDhcpHomeSubnetStartAddress.setStatus("current")
_BDhcpHomeSubnetEndAddress_Type = InetAddressIPv4
_BDhcpHomeSubnetEndAddress_Object = MibScalar
bDhcpHomeSubnetEndAddress = _BDhcpHomeSubnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 2, 3),
    _BDhcpHomeSubnetEndAddress_Type()
)
bDhcpHomeSubnetEndAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bDhcpHomeSubnetEndAddress.setStatus("current")
_BDhcpHomeSubnetTotalAddresses_Type = Unsigned32
_BDhcpHomeSubnetTotalAddresses_Object = MibScalar
bDhcpHomeSubnetTotalAddresses = _BDhcpHomeSubnetTotalAddresses_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 2, 4),
    _BDhcpHomeSubnetTotalAddresses_Type()
)
bDhcpHomeSubnetTotalAddresses.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bDhcpHomeSubnetTotalAddresses.setStatus("current")
_BDhcpHomeSubnetUsedAddrLowThreshold_Type = Unsigned32
_BDhcpHomeSubnetUsedAddrLowThreshold_Object = MibScalar
bDhcpHomeSubnetUsedAddrLowThreshold = _BDhcpHomeSubnetUsedAddrLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 2, 5),
    _BDhcpHomeSubnetUsedAddrLowThreshold_Type()
)
bDhcpHomeSubnetUsedAddrLowThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bDhcpHomeSubnetUsedAddrLowThreshold.setStatus("current")
_BDhcpHomeSubnetUsedAddrHighThreshold_Type = Unsigned32
_BDhcpHomeSubnetUsedAddrHighThreshold_Object = MibScalar
bDhcpHomeSubnetUsedAddrHighThreshold = _BDhcpHomeSubnetUsedAddrHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 2, 6),
    _BDhcpHomeSubnetUsedAddrHighThreshold_Type()
)
bDhcpHomeSubnetUsedAddrHighThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bDhcpHomeSubnetUsedAddrHighThreshold.setStatus("current")
_BDhcpv6MIBObjects_ObjectIdentity = ObjectIdentity
bDhcpv6MIBObjects = _BDhcpv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3)
)
if mibBuilder.loadTexts:
    bDhcpv6MIBObjects.setStatus("current")
_BDhcpv6ActiveClient_Type = Unsigned32
_BDhcpv6ActiveClient_Object = MibScalar
bDhcpv6ActiveClient = _BDhcpv6ActiveClient_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 1),
    _BDhcpv6ActiveClient_Type()
)
bDhcpv6ActiveClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ActiveClient.setStatus("current")
_BDhcpv6GlobalTable_Object = MibTable
bDhcpv6GlobalTable = _BDhcpv6GlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    bDhcpv6GlobalTable.setStatus("current")
_BDhcpv6GlobalEntry_Object = MibTableRow
bDhcpv6GlobalEntry = _BDhcpv6GlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1)
)
bDhcpv6GlobalEntry.setIndexNames(
    (0, "BENU-DHCP-MIB", "bDhcpv6GlobalStatsInterval"),
)
if mibBuilder.loadTexts:
    bDhcpv6GlobalEntry.setStatus("current")
_BDhcpv6GlobalStatsInterval_Type = Integer32
_BDhcpv6GlobalStatsInterval_Object = MibTableColumn
bDhcpv6GlobalStatsInterval = _BDhcpv6GlobalStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 1),
    _BDhcpv6GlobalStatsInterval_Type()
)
bDhcpv6GlobalStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bDhcpv6GlobalStatsInterval.setStatus("current")
_BDhcpv6SolicitsRcvd_Type = Unsigned32
_BDhcpv6SolicitsRcvd_Object = MibTableColumn
bDhcpv6SolicitsRcvd = _BDhcpv6SolicitsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 2),
    _BDhcpv6SolicitsRcvd_Type()
)
bDhcpv6SolicitsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6SolicitsRcvd.setStatus("current")
_BDhcpv6OffersSent_Type = Unsigned32
_BDhcpv6OffersSent_Object = MibTableColumn
bDhcpv6OffersSent = _BDhcpv6OffersSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 3),
    _BDhcpv6OffersSent_Type()
)
bDhcpv6OffersSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6OffersSent.setStatus("current")
_BDhcpv6RequestsRcvd_Type = Unsigned32
_BDhcpv6RequestsRcvd_Object = MibTableColumn
bDhcpv6RequestsRcvd = _BDhcpv6RequestsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 4),
    _BDhcpv6RequestsRcvd_Type()
)
bDhcpv6RequestsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6RequestsRcvd.setStatus("current")
_BDhcpv6DeclinesRcvd_Type = Unsigned32
_BDhcpv6DeclinesRcvd_Object = MibTableColumn
bDhcpv6DeclinesRcvd = _BDhcpv6DeclinesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 5),
    _BDhcpv6DeclinesRcvd_Type()
)
bDhcpv6DeclinesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DeclinesRcvd.setStatus("current")
_BDhcpv6ReleasesRcvd_Type = Unsigned32
_BDhcpv6ReleasesRcvd_Object = MibTableColumn
bDhcpv6ReleasesRcvd = _BDhcpv6ReleasesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 6),
    _BDhcpv6ReleasesRcvd_Type()
)
bDhcpv6ReleasesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ReleasesRcvd.setStatus("current")
_BDhcpv6ReleaseIndRcvd_Type = Unsigned32
_BDhcpv6ReleaseIndRcvd_Object = MibTableColumn
bDhcpv6ReleaseIndRcvd = _BDhcpv6ReleaseIndRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 7),
    _BDhcpv6ReleaseIndRcvd_Type()
)
bDhcpv6ReleaseIndRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ReleaseIndRcvd.setStatus("current")
_BDhcpv6RenewRcvd_Type = Unsigned32
_BDhcpv6RenewRcvd_Object = MibTableColumn
bDhcpv6RenewRcvd = _BDhcpv6RenewRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 8),
    _BDhcpv6RenewRcvd_Type()
)
bDhcpv6RenewRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6RenewRcvd.setStatus("current")
_BDhcpv6RebindRcvd_Type = Unsigned32
_BDhcpv6RebindRcvd_Object = MibTableColumn
bDhcpv6RebindRcvd = _BDhcpv6RebindRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 9),
    _BDhcpv6RebindRcvd_Type()
)
bDhcpv6RebindRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6RebindRcvd.setStatus("current")
_BDhcpv6InformsRcvd_Type = Unsigned32
_BDhcpv6InformsRcvd_Object = MibTableColumn
bDhcpv6InformsRcvd = _BDhcpv6InformsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 10),
    _BDhcpv6InformsRcvd_Type()
)
bDhcpv6InformsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6InformsRcvd.setStatus("current")
_BDhcpv6ConfirmsRcvd_Type = Unsigned32
_BDhcpv6ConfirmsRcvd_Object = MibTableColumn
bDhcpv6ConfirmsRcvd = _BDhcpv6ConfirmsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 11),
    _BDhcpv6ConfirmsRcvd_Type()
)
bDhcpv6ConfirmsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ConfirmsRcvd.setStatus("current")
_BDhcpv6ReplysSent_Type = Unsigned32
_BDhcpv6ReplysSent_Object = MibTableColumn
bDhcpv6ReplysSent = _BDhcpv6ReplysSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 12),
    _BDhcpv6ReplysSent_Type()
)
bDhcpv6ReplysSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ReplysSent.setStatus("current")
_BDhcpv6AdvertisesSent_Type = Unsigned32
_BDhcpv6AdvertisesSent_Object = MibTableColumn
bDhcpv6AdvertisesSent = _BDhcpv6AdvertisesSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 13),
    _BDhcpv6AdvertisesSent_Type()
)
bDhcpv6AdvertisesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6AdvertisesSent.setStatus("current")
_BDhcpv6UnknownMsgsRcvd_Type = Unsigned32
_BDhcpv6UnknownMsgsRcvd_Object = MibTableColumn
bDhcpv6UnknownMsgsRcvd = _BDhcpv6UnknownMsgsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 14),
    _BDhcpv6UnknownMsgsRcvd_Type()
)
bDhcpv6UnknownMsgsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnknownMsgsRcvd.setStatus("current")
_BDhcpv6ReconfigsSent_Type = Unsigned32
_BDhcpv6ReconfigsSent_Object = MibTableColumn
bDhcpv6ReconfigsSent = _BDhcpv6ReconfigsSent_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 15),
    _BDhcpv6ReconfigsSent_Type()
)
bDhcpv6ReconfigsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ReconfigsSent.setStatus("current")
_BDhcpv6DropSolicit_Type = Unsigned32
_BDhcpv6DropSolicit_Object = MibTableColumn
bDhcpv6DropSolicit = _BDhcpv6DropSolicit_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 16),
    _BDhcpv6DropSolicit_Type()
)
bDhcpv6DropSolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropSolicit.setStatus("current")
_BDhcpv6DropAdvertise_Type = Unsigned32
_BDhcpv6DropAdvertise_Object = MibTableColumn
bDhcpv6DropAdvertise = _BDhcpv6DropAdvertise_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 17),
    _BDhcpv6DropAdvertise_Type()
)
bDhcpv6DropAdvertise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropAdvertise.setStatus("current")
_BDhcpv6DropDupSolicit_Type = Unsigned32
_BDhcpv6DropDupSolicit_Object = MibTableColumn
bDhcpv6DropDupSolicit = _BDhcpv6DropDupSolicit_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 18),
    _BDhcpv6DropDupSolicit_Type()
)
bDhcpv6DropDupSolicit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropDupSolicit.setStatus("current")
_BDhcpv6DropRequest_Type = Unsigned32
_BDhcpv6DropRequest_Object = MibTableColumn
bDhcpv6DropRequest = _BDhcpv6DropRequest_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 19),
    _BDhcpv6DropRequest_Type()
)
bDhcpv6DropRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropRequest.setStatus("current")
_BDhcpv6DropRelease_Type = Unsigned32
_BDhcpv6DropRelease_Object = MibTableColumn
bDhcpv6DropRelease = _BDhcpv6DropRelease_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 20),
    _BDhcpv6DropRelease_Type()
)
bDhcpv6DropRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropRelease.setStatus("current")
_BDhcpv6DropDecline_Type = Unsigned32
_BDhcpv6DropDecline_Object = MibTableColumn
bDhcpv6DropDecline = _BDhcpv6DropDecline_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 21),
    _BDhcpv6DropDecline_Type()
)
bDhcpv6DropDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropDecline.setStatus("current")
_BDhcpv6DropRenew_Type = Unsigned32
_BDhcpv6DropRenew_Object = MibTableColumn
bDhcpv6DropRenew = _BDhcpv6DropRenew_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 22),
    _BDhcpv6DropRenew_Type()
)
bDhcpv6DropRenew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropRenew.setStatus("current")
_BDhcpv6DropRebind_Type = Unsigned32
_BDhcpv6DropRebind_Object = MibTableColumn
bDhcpv6DropRebind = _BDhcpv6DropRebind_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 23),
    _BDhcpv6DropRebind_Type()
)
bDhcpv6DropRebind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropRebind.setStatus("current")
_BDhcpv6DropConfirm_Type = Unsigned32
_BDhcpv6DropConfirm_Object = MibTableColumn
bDhcpv6DropConfirm = _BDhcpv6DropConfirm_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 24),
    _BDhcpv6DropConfirm_Type()
)
bDhcpv6DropConfirm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropConfirm.setStatus("current")
_BDhcpv6DropInform_Type = Unsigned32
_BDhcpv6DropInform_Object = MibTableColumn
bDhcpv6DropInform = _BDhcpv6DropInform_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 25),
    _BDhcpv6DropInform_Type()
)
bDhcpv6DropInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropInform.setStatus("current")
_BDhcpv6DropRelay_Type = Unsigned32
_BDhcpv6DropRelay_Object = MibTableColumn
bDhcpv6DropRelay = _BDhcpv6DropRelay_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 26),
    _BDhcpv6DropRelay_Type()
)
bDhcpv6DropRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropRelay.setStatus("current")
_BDhcpv6DropReply_Type = Unsigned32
_BDhcpv6DropReply_Object = MibTableColumn
bDhcpv6DropReply = _BDhcpv6DropReply_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 27),
    _BDhcpv6DropReply_Type()
)
bDhcpv6DropReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropReply.setStatus("current")
_BDhcpv6DropRelayReply_Type = Unsigned32
_BDhcpv6DropRelayReply_Object = MibTableColumn
bDhcpv6DropRelayReply = _BDhcpv6DropRelayReply_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 28),
    _BDhcpv6DropRelayReply_Type()
)
bDhcpv6DropRelayReply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropRelayReply.setStatus("current")
_BDhcpv6DropReconfig_Type = Unsigned32
_BDhcpv6DropReconfig_Object = MibTableColumn
bDhcpv6DropReconfig = _BDhcpv6DropReconfig_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 29),
    _BDhcpv6DropReconfig_Type()
)
bDhcpv6DropReconfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DropReconfig.setStatus("current")
_BDhcpv6LeasesOffered_Type = Unsigned32
_BDhcpv6LeasesOffered_Object = MibTableColumn
bDhcpv6LeasesOffered = _BDhcpv6LeasesOffered_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 30),
    _BDhcpv6LeasesOffered_Type()
)
bDhcpv6LeasesOffered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesOffered.setStatus("current")
_BDhcpv6LeasesAssigned_Type = Unsigned32
_BDhcpv6LeasesAssigned_Object = MibTableColumn
bDhcpv6LeasesAssigned = _BDhcpv6LeasesAssigned_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 31),
    _BDhcpv6LeasesAssigned_Type()
)
bDhcpv6LeasesAssigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesAssigned.setStatus("current")
_BDhcpv6LeasesReleased_Type = Unsigned32
_BDhcpv6LeasesReleased_Object = MibTableColumn
bDhcpv6LeasesReleased = _BDhcpv6LeasesReleased_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 32),
    _BDhcpv6LeasesReleased_Type()
)
bDhcpv6LeasesReleased.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesReleased.setStatus("current")
_BDhcpv6LeasesRelFail_Type = Unsigned32
_BDhcpv6LeasesRelFail_Object = MibTableColumn
bDhcpv6LeasesRelFail = _BDhcpv6LeasesRelFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 33),
    _BDhcpv6LeasesRelFail_Type()
)
bDhcpv6LeasesRelFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesRelFail.setStatus("current")
_BDhcpv6LeasesExpired_Type = Unsigned32
_BDhcpv6LeasesExpired_Object = MibTableColumn
bDhcpv6LeasesExpired = _BDhcpv6LeasesExpired_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 34),
    _BDhcpv6LeasesExpired_Type()
)
bDhcpv6LeasesExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesExpired.setStatus("current")
_BDhcpv6LeasesExpiryFail_Type = Unsigned32
_BDhcpv6LeasesExpiryFail_Object = MibTableColumn
bDhcpv6LeasesExpiryFail = _BDhcpv6LeasesExpiryFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 35),
    _BDhcpv6LeasesExpiryFail_Type()
)
bDhcpv6LeasesExpiryFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesExpiryFail.setStatus("current")
_BDhcpv6LeasesRenewed_Type = Unsigned32
_BDhcpv6LeasesRenewed_Object = MibTableColumn
bDhcpv6LeasesRenewed = _BDhcpv6LeasesRenewed_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 36),
    _BDhcpv6LeasesRenewed_Type()
)
bDhcpv6LeasesRenewed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesRenewed.setStatus("current")
_BDhcpv6LeasesRenewFail_Type = Unsigned32
_BDhcpv6LeasesRenewFail_Object = MibTableColumn
bDhcpv6LeasesRenewFail = _BDhcpv6LeasesRenewFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 37),
    _BDhcpv6LeasesRenewFail_Type()
)
bDhcpv6LeasesRenewFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6LeasesRenewFail.setStatus("current")
_BDhcpv6InternalError_Type = Unsigned32
_BDhcpv6InternalError_Object = MibTableColumn
bDhcpv6InternalError = _BDhcpv6InternalError_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 38),
    _BDhcpv6InternalError_Type()
)
bDhcpv6InternalError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6InternalError.setStatus("current")
_BDhcpv6NoInterface_Type = Unsigned32
_BDhcpv6NoInterface_Object = MibTableColumn
bDhcpv6NoInterface = _BDhcpv6NoInterface_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 39),
    _BDhcpv6NoInterface_Type()
)
bDhcpv6NoInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6NoInterface.setStatus("current")
_BDhcpv6ClientIdNotPres_Type = Unsigned32
_BDhcpv6ClientIdNotPres_Object = MibTableColumn
bDhcpv6ClientIdNotPres = _BDhcpv6ClientIdNotPres_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 40),
    _BDhcpv6ClientIdNotPres_Type()
)
bDhcpv6ClientIdNotPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ClientIdNotPres.setStatus("current")
_BDhcpv6ServerIdNotPres_Type = Unsigned32
_BDhcpv6ServerIdNotPres_Object = MibTableColumn
bDhcpv6ServerIdNotPres = _BDhcpv6ServerIdNotPres_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 41),
    _BDhcpv6ServerIdNotPres_Type()
)
bDhcpv6ServerIdNotPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ServerIdNotPres.setStatus("current")
_BDhcpv6ORONotPres_Type = Unsigned32
_BDhcpv6ORONotPres_Object = MibTableColumn
bDhcpv6ORONotPres = _BDhcpv6ORONotPres_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 42),
    _BDhcpv6ORONotPres_Type()
)
bDhcpv6ORONotPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ORONotPres.setStatus("current")
_BDhcpv6ClientIdPres_Type = Unsigned32
_BDhcpv6ClientIdPres_Object = MibTableColumn
bDhcpv6ClientIdPres = _BDhcpv6ClientIdPres_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 43),
    _BDhcpv6ClientIdPres_Type()
)
bDhcpv6ClientIdPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ClientIdPres.setStatus("current")
_BDhcpv6ServerIdPres_Type = Unsigned32
_BDhcpv6ServerIdPres_Object = MibTableColumn
bDhcpv6ServerIdPres = _BDhcpv6ServerIdPres_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 44),
    _BDhcpv6ServerIdPres_Type()
)
bDhcpv6ServerIdPres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ServerIdPres.setStatus("current")
_BDhcpv6UnicastSolicitRcvd_Type = Unsigned32
_BDhcpv6UnicastSolicitRcvd_Object = MibTableColumn
bDhcpv6UnicastSolicitRcvd = _BDhcpv6UnicastSolicitRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 45),
    _BDhcpv6UnicastSolicitRcvd_Type()
)
bDhcpv6UnicastSolicitRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnicastSolicitRcvd.setStatus("current")
_BDhcpv6UnicastRequestRcvd_Type = Unsigned32
_BDhcpv6UnicastRequestRcvd_Object = MibTableColumn
bDhcpv6UnicastRequestRcvd = _BDhcpv6UnicastRequestRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 46),
    _BDhcpv6UnicastRequestRcvd_Type()
)
bDhcpv6UnicastRequestRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnicastRequestRcvd.setStatus("current")
_BDhcpv6UnicastRenewRcvd_Type = Unsigned32
_BDhcpv6UnicastRenewRcvd_Object = MibTableColumn
bDhcpv6UnicastRenewRcvd = _BDhcpv6UnicastRenewRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 47),
    _BDhcpv6UnicastRenewRcvd_Type()
)
bDhcpv6UnicastRenewRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnicastRenewRcvd.setStatus("current")
_BDhcpv6UnicastConfirmRcvd_Type = Unsigned32
_BDhcpv6UnicastConfirmRcvd_Object = MibTableColumn
bDhcpv6UnicastConfirmRcvd = _BDhcpv6UnicastConfirmRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 48),
    _BDhcpv6UnicastConfirmRcvd_Type()
)
bDhcpv6UnicastConfirmRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnicastConfirmRcvd.setStatus("current")
_BDhcpv6UnicastDeclineRcvd_Type = Unsigned32
_BDhcpv6UnicastDeclineRcvd_Object = MibTableColumn
bDhcpv6UnicastDeclineRcvd = _BDhcpv6UnicastDeclineRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 49),
    _BDhcpv6UnicastDeclineRcvd_Type()
)
bDhcpv6UnicastDeclineRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnicastDeclineRcvd.setStatus("current")
_BDhcpv6UnicastReleaseRcvd_Type = Unsigned32
_BDhcpv6UnicastReleaseRcvd_Object = MibTableColumn
bDhcpv6UnicastReleaseRcvd = _BDhcpv6UnicastReleaseRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 50),
    _BDhcpv6UnicastReleaseRcvd_Type()
)
bDhcpv6UnicastReleaseRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnicastReleaseRcvd.setStatus("current")
_BDhcpv6UnicastRebindRcvd_Type = Unsigned32
_BDhcpv6UnicastRebindRcvd_Object = MibTableColumn
bDhcpv6UnicastRebindRcvd = _BDhcpv6UnicastRebindRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 51),
    _BDhcpv6UnicastRebindRcvd_Type()
)
bDhcpv6UnicastRebindRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6UnicastRebindRcvd.setStatus("current")
_BDhcpv6RebindWithoutAddrRcvd_Type = Unsigned32
_BDhcpv6RebindWithoutAddrRcvd_Object = MibTableColumn
bDhcpv6RebindWithoutAddrRcvd = _BDhcpv6RebindWithoutAddrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 52),
    _BDhcpv6RebindWithoutAddrRcvd_Type()
)
bDhcpv6RebindWithoutAddrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6RebindWithoutAddrRcvd.setStatus("current")
_BDhcpv6ConfirmWithoutAddrRcvd_Type = Unsigned32
_BDhcpv6ConfirmWithoutAddrRcvd_Object = MibTableColumn
bDhcpv6ConfirmWithoutAddrRcvd = _BDhcpv6ConfirmWithoutAddrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 53),
    _BDhcpv6ConfirmWithoutAddrRcvd_Type()
)
bDhcpv6ConfirmWithoutAddrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ConfirmWithoutAddrRcvd.setStatus("current")
_BDhcpv6DeclineWithoutAddrRcvd_Type = Unsigned32
_BDhcpv6DeclineWithoutAddrRcvd_Object = MibTableColumn
bDhcpv6DeclineWithoutAddrRcvd = _BDhcpv6DeclineWithoutAddrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 54),
    _BDhcpv6DeclineWithoutAddrRcvd_Type()
)
bDhcpv6DeclineWithoutAddrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6DeclineWithoutAddrRcvd.setStatus("current")
_BDhcpv6RebindWithoutAddrOrMoreRcvd_Type = Unsigned32
_BDhcpv6RebindWithoutAddrOrMoreRcvd_Object = MibTableColumn
bDhcpv6RebindWithoutAddrOrMoreRcvd = _BDhcpv6RebindWithoutAddrOrMoreRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 55),
    _BDhcpv6RebindWithoutAddrOrMoreRcvd_Type()
)
bDhcpv6RebindWithoutAddrOrMoreRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6RebindWithoutAddrOrMoreRcvd.setStatus("current")
_BDhcpv6RenewWithoutAddrOrMoreRcvd_Type = Unsigned32
_BDhcpv6RenewWithoutAddrOrMoreRcvd_Object = MibTableColumn
bDhcpv6RenewWithoutAddrOrMoreRcvd = _BDhcpv6RenewWithoutAddrOrMoreRcvd_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 56),
    _BDhcpv6RenewWithoutAddrOrMoreRcvd_Type()
)
bDhcpv6RenewWithoutAddrOrMoreRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6RenewWithoutAddrOrMoreRcvd.setStatus("current")
_BDhcpv6RebindFail_Type = Unsigned32
_BDhcpv6RebindFail_Object = MibTableColumn
bDhcpv6RebindFail = _BDhcpv6RebindFail_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 57),
    _BDhcpv6RebindFail_Type()
)
bDhcpv6RebindFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6RebindFail.setStatus("current")
_BDhcpv6ReconfAcceptInSolicitMissing_Type = Unsigned32
_BDhcpv6ReconfAcceptInSolicitMissing_Object = MibTableColumn
bDhcpv6ReconfAcceptInSolicitMissing = _BDhcpv6ReconfAcceptInSolicitMissing_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 58),
    _BDhcpv6ReconfAcceptInSolicitMissing_Type()
)
bDhcpv6ReconfAcceptInSolicitMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6ReconfAcceptInSolicitMissing.setStatus("current")
_BDhcpv6IntervalDuration_Type = Integer32
_BDhcpv6IntervalDuration_Object = MibTableColumn
bDhcpv6IntervalDuration = _BDhcpv6IntervalDuration_Object(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 3, 2, 1, 59),
    _BDhcpv6IntervalDuration_Type()
)
bDhcpv6IntervalDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bDhcpv6IntervalDuration.setStatus("current")
_BDhcpv6NotifObjects_ObjectIdentity = ObjectIdentity
bDhcpv6NotifObjects = _BDhcpv6NotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 4)
)
if mibBuilder.loadTexts:
    bDhcpv6NotifObjects.setStatus("current")

# Managed Objects groups


# Notification objects

bDhcpSubnetUsedAddrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 0, 1)
)
bDhcpSubnetUsedAddrLow.setObjects(
      *(("BENU-DHCP-MIB", "bDhcpSubnetStartAddress"),
        ("BENU-DHCP-MIB", "bDhcpSubnetEndAddress"),
        ("BENU-DHCP-MIB", "bDhcpSubnetTotalAddresses"),
        ("BENU-DHCP-MIB", "bDhcpSubnetUsedAddrLowThreshold"))
)
if mibBuilder.loadTexts:
    bDhcpSubnetUsedAddrLow.setStatus(
        "current"
    )

bDhcpSubnetUsedAddrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 0, 2)
)
bDhcpSubnetUsedAddrHigh.setObjects(
      *(("BENU-DHCP-MIB", "bDhcpSubnetStartAddress"),
        ("BENU-DHCP-MIB", "bDhcpSubnetEndAddress"),
        ("BENU-DHCP-MIB", "bDhcpSubnetTotalAddresses"),
        ("BENU-DHCP-MIB", "bDhcpSubnetUsedAddrHighThreshold"))
)
if mibBuilder.loadTexts:
    bDhcpSubnetUsedAddrHigh.setStatus(
        "current"
    )

bDhcpHomeSubnetUsedAddrLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 0, 3)
)
bDhcpHomeSubnetUsedAddrLow.setObjects(
      *(("BENU-DHCP-MIB", "bDhcpHomeSubnetHomeId"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetStartAddress"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetEndAddress"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetTotalAddresses"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetUsedAddrLowThreshold"))
)
if mibBuilder.loadTexts:
    bDhcpHomeSubnetUsedAddrLow.setStatus(
        "current"
    )

bDhcpHomeSubnetUsedAddrHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 39406, 2, 1, 6, 0, 4)
)
bDhcpHomeSubnetUsedAddrHigh.setObjects(
      *(("BENU-DHCP-MIB", "bDhcpHomeSubnetHomeId"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetStartAddress"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetEndAddress"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetTotalAddresses"),
        ("BENU-DHCP-MIB", "bDhcpHomeSubnetUsedAddrHighThreshold"))
)
if mibBuilder.loadTexts:
    bDhcpHomeSubnetUsedAddrHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BENU-DHCP-MIB",
    **{"bDhcpMIB": bDhcpMIB,
       "bDhcpNotifications": bDhcpNotifications,
       "bDhcpSubnetUsedAddrLow": bDhcpSubnetUsedAddrLow,
       "bDhcpSubnetUsedAddrHigh": bDhcpSubnetUsedAddrHigh,
       "bDhcpHomeSubnetUsedAddrLow": bDhcpHomeSubnetUsedAddrLow,
       "bDhcpHomeSubnetUsedAddrHigh": bDhcpHomeSubnetUsedAddrHigh,
       "bDhcpv4MIBObjects": bDhcpv4MIBObjects,
       "bDhcpSubnetTable": bDhcpSubnetTable,
       "bDhcpSubnetEntry": bDhcpSubnetEntry,
       "bDhcpSubnetStatsInterval": bDhcpSubnetStatsInterval,
       "bDhcpSubnetIndex": bDhcpSubnetIndex,
       "bDhcpSubnetRangeIndex": bDhcpSubnetRangeIndex,
       "bDhcpSubnetIntervalDuration": bDhcpSubnetIntervalDuration,
       "bDhcpSubnetStartAddress": bDhcpSubnetStartAddress,
       "bDhcpSubnetEndAddress": bDhcpSubnetEndAddress,
       "bDhcpSubnetTotalAddresses": bDhcpSubnetTotalAddresses,
       "bDhcpSubnetPeakFreeAddresses": bDhcpSubnetPeakFreeAddresses,
       "bDhcpSubnetPeakUsedAddresses": bDhcpSubnetPeakUsedAddresses,
       "bDhcpSubnetAddress": bDhcpSubnetAddress,
       "bDhcpSubnetMask": bDhcpSubnetMask,
       "bDhcpSubnetUsedAddrLowThreshold": bDhcpSubnetUsedAddrLowThreshold,
       "bDhcpSubnetUsedAddrHighThreshold": bDhcpSubnetUsedAddrHighThreshold,
       "bDhcpSubnetPeakHoldAddresses": bDhcpSubnetPeakHoldAddresses,
       "bDhcpGlobalTable": bDhcpGlobalTable,
       "bDhcpGlobalEntry": bDhcpGlobalEntry,
       "bDhcpGlobalStatsInterval": bDhcpGlobalStatsInterval,
       "bDhcpDiscoversRcvd": bDhcpDiscoversRcvd,
       "bDhcpOffersSent": bDhcpOffersSent,
       "bDhcpRequestsRcvd": bDhcpRequestsRcvd,
       "bDhcpDeclinesRcvd": bDhcpDeclinesRcvd,
       "bDhcpAcksSent": bDhcpAcksSent,
       "bDhcpNacksSent": bDhcpNacksSent,
       "bDhcpReleasesRcvd": bDhcpReleasesRcvd,
       "bDhcpReleasesIndRcvd": bDhcpReleasesIndRcvd,
       "bDhcpReleasesSent": bDhcpReleasesSent,
       "bDhcpInformsRcvd": bDhcpInformsRcvd,
       "bDhcpInformsAckSent": bDhcpInformsAckSent,
       "bDhcpDropDiscover": bDhcpDropDiscover,
       "bDhcpDropRequest": bDhcpDropRequest,
       "bDhcpDropRelease": bDhcpDropRelease,
       "bDhcpLeasesAssigned": bDhcpLeasesAssigned,
       "bDhcpLeasesReleased": bDhcpLeasesReleased,
       "bDhcpLeasesRelFail": bDhcpLeasesRelFail,
       "bDhcpLeasesExpired": bDhcpLeasesExpired,
       "bDhcpLeasesRenewed": bDhcpLeasesRenewed,
       "bDhcpLeasesRenewFail": bDhcpLeasesRenewFail,
       "bDhcpLeasesNotAssignServIntNotConfig": bDhcpLeasesNotAssignServIntNotConfig,
       "bDhcpLeasesNotAssignFreeBuffUnavail": bDhcpLeasesNotAssignFreeBuffUnavail,
       "bDhcpIntervalDuration": bDhcpIntervalDuration,
       "bBootpRequestsRcvd": bBootpRequestsRcvd,
       "bBootpRepliesSent": bBootpRepliesSent,
       "bDhcpReleasesIndSent": bDhcpReleasesIndSent,
       "bDhcpv4ActiveClient": bDhcpv4ActiveClient,
       "bDhcpSPWiFiGlobalTable": bDhcpSPWiFiGlobalTable,
       "bDhcpSPWiFiGlobalEntry": bDhcpSPWiFiGlobalEntry,
       "bDhcpSPWiFiGlobalStatsInterval": bDhcpSPWiFiGlobalStatsInterval,
       "bDhcpSPWiFiDiscoversRcvd": bDhcpSPWiFiDiscoversRcvd,
       "bDhcpSPWiFiOffersSent": bDhcpSPWiFiOffersSent,
       "bDhcpSPWiFiRequestsRcvd": bDhcpSPWiFiRequestsRcvd,
       "bDhcpSPWiFiDeclinesRcvd": bDhcpSPWiFiDeclinesRcvd,
       "bDhcpSPWiFiAcksSent": bDhcpSPWiFiAcksSent,
       "bDhcpSPWiFiNacksSent": bDhcpSPWiFiNacksSent,
       "bDhcpSPWiFiReleasesRcvd": bDhcpSPWiFiReleasesRcvd,
       "bDhcpSPWiFiReleasesIndRcvd": bDhcpSPWiFiReleasesIndRcvd,
       "bDhcpSPWiFiReleasesSent": bDhcpSPWiFiReleasesSent,
       "bDhcpSPWiFiInformsRcvd": bDhcpSPWiFiInformsRcvd,
       "bDhcpSPWiFiInformsAckSent": bDhcpSPWiFiInformsAckSent,
       "bDhcpSPWiFiDropDiscover": bDhcpSPWiFiDropDiscover,
       "bDhcpSPWiFiDropRequest": bDhcpSPWiFiDropRequest,
       "bDhcpSPWiFiDropRelease": bDhcpSPWiFiDropRelease,
       "bDhcpSPWiFiLeasesAssigned": bDhcpSPWiFiLeasesAssigned,
       "bDhcpSPWiFiLeasesReleased": bDhcpSPWiFiLeasesReleased,
       "bDhcpSPWiFiLeasesRelFail": bDhcpSPWiFiLeasesRelFail,
       "bDhcpSPWiFiLeasesExpired": bDhcpSPWiFiLeasesExpired,
       "bDhcpSPWiFiLeasesRenewed": bDhcpSPWiFiLeasesRenewed,
       "bDhcpSPWiFiLeasesRenewFail": bDhcpSPWiFiLeasesRenewFail,
       "bDhcpSPWiFiLeasesNotAssignServIntNotConfig": bDhcpSPWiFiLeasesNotAssignServIntNotConfig,
       "bDhcpSPWiFiLeasesNotAssignFreeBuffUnavail": bDhcpSPWiFiLeasesNotAssignFreeBuffUnavail,
       "bDhcpSPWiFiIntervalDuration": bDhcpSPWiFiIntervalDuration,
       "bSPWiFiBootpRequestsRcvd": bSPWiFiBootpRequestsRcvd,
       "bSPWiFiBootpRepliesSent": bSPWiFiBootpRepliesSent,
       "bDhcpSPWiFiReleasesIndSent": bDhcpSPWiFiReleasesIndSent,
       "bDhcpHomeGlobalTable": bDhcpHomeGlobalTable,
       "bDhcpHomeGlobalEntry": bDhcpHomeGlobalEntry,
       "bDhcpHomeGlobalStatsInterval": bDhcpHomeGlobalStatsInterval,
       "bDhcpHomeDiscoversRcvd": bDhcpHomeDiscoversRcvd,
       "bDhcpHomeOffersSent": bDhcpHomeOffersSent,
       "bDhcpHomeRequestsRcvd": bDhcpHomeRequestsRcvd,
       "bDhcpHomeDeclinesRcvd": bDhcpHomeDeclinesRcvd,
       "bDhcpHomeAcksSent": bDhcpHomeAcksSent,
       "bDhcpHomeNacksSent": bDhcpHomeNacksSent,
       "bDhcpHomeReleasesRcvd": bDhcpHomeReleasesRcvd,
       "bDhcpHomeReleasesIndRcvd": bDhcpHomeReleasesIndRcvd,
       "bDhcpHomeReleasesSent": bDhcpHomeReleasesSent,
       "bDhcpHomeInformsRcvd": bDhcpHomeInformsRcvd,
       "bDhcpHomeInformsAckSent": bDhcpHomeInformsAckSent,
       "bDhcpHomeDropDiscover": bDhcpHomeDropDiscover,
       "bDhcpHomeDropRequest": bDhcpHomeDropRequest,
       "bDhcpHomeDropRelease": bDhcpHomeDropRelease,
       "bDhcpHomeLeasesAssigned": bDhcpHomeLeasesAssigned,
       "bDhcpHomeLeasesReleased": bDhcpHomeLeasesReleased,
       "bDhcpHomeLeasesRelFail": bDhcpHomeLeasesRelFail,
       "bDhcpHomeLeasesExpired": bDhcpHomeLeasesExpired,
       "bDhcpHomeLeasesRenewed": bDhcpHomeLeasesRenewed,
       "bDhcpHomeLeasesRenewFail": bDhcpHomeLeasesRenewFail,
       "bDhcpHomeLeasesNotAssignServIntNotConfig": bDhcpHomeLeasesNotAssignServIntNotConfig,
       "bDhcpHomeLeasesNotAssignFreeBuffUnavail": bDhcpHomeLeasesNotAssignFreeBuffUnavail,
       "bDhcpHomeIntervalDuration": bDhcpHomeIntervalDuration,
       "bHomeBootpRequestsRcvd": bHomeBootpRequestsRcvd,
       "bHomeBootpRepliesSent": bHomeBootpRepliesSent,
       "bDhcpHomeReleasesIndSent": bDhcpHomeReleasesIndSent,
       "bDhcpv4ActiveSpWiFiClients": bDhcpv4ActiveSpWiFiClients,
       "bDhcpv4ActiveHomeClients": bDhcpv4ActiveHomeClients,
       "bDhcpv4NotifObjects": bDhcpv4NotifObjects,
       "bDhcpHomeSubnetHomeId": bDhcpHomeSubnetHomeId,
       "bDhcpHomeSubnetStartAddress": bDhcpHomeSubnetStartAddress,
       "bDhcpHomeSubnetEndAddress": bDhcpHomeSubnetEndAddress,
       "bDhcpHomeSubnetTotalAddresses": bDhcpHomeSubnetTotalAddresses,
       "bDhcpHomeSubnetUsedAddrLowThreshold": bDhcpHomeSubnetUsedAddrLowThreshold,
       "bDhcpHomeSubnetUsedAddrHighThreshold": bDhcpHomeSubnetUsedAddrHighThreshold,
       "bDhcpv6MIBObjects": bDhcpv6MIBObjects,
       "bDhcpv6ActiveClient": bDhcpv6ActiveClient,
       "bDhcpv6GlobalTable": bDhcpv6GlobalTable,
       "bDhcpv6GlobalEntry": bDhcpv6GlobalEntry,
       "bDhcpv6GlobalStatsInterval": bDhcpv6GlobalStatsInterval,
       "bDhcpv6SolicitsRcvd": bDhcpv6SolicitsRcvd,
       "bDhcpv6OffersSent": bDhcpv6OffersSent,
       "bDhcpv6RequestsRcvd": bDhcpv6RequestsRcvd,
       "bDhcpv6DeclinesRcvd": bDhcpv6DeclinesRcvd,
       "bDhcpv6ReleasesRcvd": bDhcpv6ReleasesRcvd,
       "bDhcpv6ReleaseIndRcvd": bDhcpv6ReleaseIndRcvd,
       "bDhcpv6RenewRcvd": bDhcpv6RenewRcvd,
       "bDhcpv6RebindRcvd": bDhcpv6RebindRcvd,
       "bDhcpv6InformsRcvd": bDhcpv6InformsRcvd,
       "bDhcpv6ConfirmsRcvd": bDhcpv6ConfirmsRcvd,
       "bDhcpv6ReplysSent": bDhcpv6ReplysSent,
       "bDhcpv6AdvertisesSent": bDhcpv6AdvertisesSent,
       "bDhcpv6UnknownMsgsRcvd": bDhcpv6UnknownMsgsRcvd,
       "bDhcpv6ReconfigsSent": bDhcpv6ReconfigsSent,
       "bDhcpv6DropSolicit": bDhcpv6DropSolicit,
       "bDhcpv6DropAdvertise": bDhcpv6DropAdvertise,
       "bDhcpv6DropDupSolicit": bDhcpv6DropDupSolicit,
       "bDhcpv6DropRequest": bDhcpv6DropRequest,
       "bDhcpv6DropRelease": bDhcpv6DropRelease,
       "bDhcpv6DropDecline": bDhcpv6DropDecline,
       "bDhcpv6DropRenew": bDhcpv6DropRenew,
       "bDhcpv6DropRebind": bDhcpv6DropRebind,
       "bDhcpv6DropConfirm": bDhcpv6DropConfirm,
       "bDhcpv6DropInform": bDhcpv6DropInform,
       "bDhcpv6DropRelay": bDhcpv6DropRelay,
       "bDhcpv6DropReply": bDhcpv6DropReply,
       "bDhcpv6DropRelayReply": bDhcpv6DropRelayReply,
       "bDhcpv6DropReconfig": bDhcpv6DropReconfig,
       "bDhcpv6LeasesOffered": bDhcpv6LeasesOffered,
       "bDhcpv6LeasesAssigned": bDhcpv6LeasesAssigned,
       "bDhcpv6LeasesReleased": bDhcpv6LeasesReleased,
       "bDhcpv6LeasesRelFail": bDhcpv6LeasesRelFail,
       "bDhcpv6LeasesExpired": bDhcpv6LeasesExpired,
       "bDhcpv6LeasesExpiryFail": bDhcpv6LeasesExpiryFail,
       "bDhcpv6LeasesRenewed": bDhcpv6LeasesRenewed,
       "bDhcpv6LeasesRenewFail": bDhcpv6LeasesRenewFail,
       "bDhcpv6InternalError": bDhcpv6InternalError,
       "bDhcpv6NoInterface": bDhcpv6NoInterface,
       "bDhcpv6ClientIdNotPres": bDhcpv6ClientIdNotPres,
       "bDhcpv6ServerIdNotPres": bDhcpv6ServerIdNotPres,
       "bDhcpv6ORONotPres": bDhcpv6ORONotPres,
       "bDhcpv6ClientIdPres": bDhcpv6ClientIdPres,
       "bDhcpv6ServerIdPres": bDhcpv6ServerIdPres,
       "bDhcpv6UnicastSolicitRcvd": bDhcpv6UnicastSolicitRcvd,
       "bDhcpv6UnicastRequestRcvd": bDhcpv6UnicastRequestRcvd,
       "bDhcpv6UnicastRenewRcvd": bDhcpv6UnicastRenewRcvd,
       "bDhcpv6UnicastConfirmRcvd": bDhcpv6UnicastConfirmRcvd,
       "bDhcpv6UnicastDeclineRcvd": bDhcpv6UnicastDeclineRcvd,
       "bDhcpv6UnicastReleaseRcvd": bDhcpv6UnicastReleaseRcvd,
       "bDhcpv6UnicastRebindRcvd": bDhcpv6UnicastRebindRcvd,
       "bDhcpv6RebindWithoutAddrRcvd": bDhcpv6RebindWithoutAddrRcvd,
       "bDhcpv6ConfirmWithoutAddrRcvd": bDhcpv6ConfirmWithoutAddrRcvd,
       "bDhcpv6DeclineWithoutAddrRcvd": bDhcpv6DeclineWithoutAddrRcvd,
       "bDhcpv6RebindWithoutAddrOrMoreRcvd": bDhcpv6RebindWithoutAddrOrMoreRcvd,
       "bDhcpv6RenewWithoutAddrOrMoreRcvd": bDhcpv6RenewWithoutAddrOrMoreRcvd,
       "bDhcpv6RebindFail": bDhcpv6RebindFail,
       "bDhcpv6ReconfAcceptInSolicitMissing": bDhcpv6ReconfAcceptInSolicitMissing,
       "bDhcpv6IntervalDuration": bDhcpv6IntervalDuration,
       "bDhcpv6NotifObjects": bDhcpv6NotifObjects}
)
