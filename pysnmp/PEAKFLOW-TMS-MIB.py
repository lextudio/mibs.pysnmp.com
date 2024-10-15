# SNMP MIB module (PEAKFLOW-TMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PEAKFLOW-TMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:20 2024
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

(arbornetworksProducts,) = mibBuilder.importSymbols(
    "ARBOR-SMI",
    "arbornetworksProducts")

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

(Ipv6Address,
 Ipv6AddressPrefix) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressPrefix")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

peakflowTmsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5)
)
peakflowTmsMIB.setRevisions(
        ("2013-08-19 00:00",
         "2012-03-29 12:00",
         "2012-01-12 12:00",
         "2011-06-14 16:00",
         "2011-06-03 16:00",
         "2011-06-03 00:00",
         "2011-05-23 00:00",
         "2011-01-21 00:00",
         "2010-10-28 00:00",
         "2010-09-07 00:00",
         "2009-05-27 00:00",
         "2009-05-08 00:00",
         "2009-03-11 00:00",
         "2009-02-13 00:00",
         "2008-11-13 00:00",
         "2008-04-07 00:00",
         "2007-11-20 00:00",
         "2007-04-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmsTableIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class TmsTableIndexOrZero(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class TmsPercentage(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class TmsHundredths(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-2"


# MIB Managed Objects in the order of their OIDs

_PeakflowTmsMgr_ObjectIdentity = ObjectIdentity
peakflowTmsMgr = _PeakflowTmsMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2)
)
_TmsHostFault_Type = DisplayString
_TmsHostFault_Object = MibScalar
tmsHostFault = _TmsHostFault_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 1),
    _TmsHostFault_Type()
)
tmsHostFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsHostFault.setStatus("current")
_TmsHostUpTime_Type = TimeTicks
_TmsHostUpTime_Object = MibScalar
tmsHostUpTime = _TmsHostUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 2),
    _TmsHostUpTime_Type()
)
tmsHostUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsHostUpTime.setStatus("current")
_DeviceCpuLoadAvg1min_Type = TmsHundredths
_DeviceCpuLoadAvg1min_Object = MibScalar
deviceCpuLoadAvg1min = _DeviceCpuLoadAvg1min_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 3),
    _DeviceCpuLoadAvg1min_Type()
)
deviceCpuLoadAvg1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoadAvg1min.setStatus("current")
_DeviceCpuLoadAvg5min_Type = TmsHundredths
_DeviceCpuLoadAvg5min_Object = MibScalar
deviceCpuLoadAvg5min = _DeviceCpuLoadAvg5min_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 4),
    _DeviceCpuLoadAvg5min_Type()
)
deviceCpuLoadAvg5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoadAvg5min.setStatus("current")
_DeviceCpuLoadAvg15min_Type = TmsHundredths
_DeviceCpuLoadAvg15min_Object = MibScalar
deviceCpuLoadAvg15min = _DeviceCpuLoadAvg15min_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 5),
    _DeviceCpuLoadAvg15min_Type()
)
deviceCpuLoadAvg15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceCpuLoadAvg15min.setStatus("current")
_DeviceDiskUsage_Type = TmsPercentage
_DeviceDiskUsage_Object = MibScalar
deviceDiskUsage = _DeviceDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 6),
    _DeviceDiskUsage_Type()
)
deviceDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDiskUsage.setStatus("current")
_DevicePhysicalMemoryUsage_Type = TmsPercentage
_DevicePhysicalMemoryUsage_Object = MibScalar
devicePhysicalMemoryUsage = _DevicePhysicalMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 7),
    _DevicePhysicalMemoryUsage_Type()
)
devicePhysicalMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devicePhysicalMemoryUsage.setStatus("current")
_DeviceSwapSpaceUsage_Type = TmsPercentage
_DeviceSwapSpaceUsage_Object = MibScalar
deviceSwapSpaceUsage = _DeviceSwapSpaceUsage_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 8),
    _DeviceSwapSpaceUsage_Type()
)
deviceSwapSpaceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSwapSpaceUsage.setStatus("current")
_TmsTrapString_Type = DisplayString
_TmsTrapString_Object = MibScalar
tmsTrapString = _TmsTrapString_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 9),
    _TmsTrapString_Type()
)
tmsTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapString.setStatus("current")
_TmsTrapDetail_Type = DisplayString
_TmsTrapDetail_Object = MibScalar
tmsTrapDetail = _TmsTrapDetail_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 10),
    _TmsTrapDetail_Type()
)
tmsTrapDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapDetail.setStatus("current")
_TmsTrapSubhostName_Type = DisplayString
_TmsTrapSubhostName_Object = MibScalar
tmsTrapSubhostName = _TmsTrapSubhostName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 11),
    _TmsTrapSubhostName_Type()
)
tmsTrapSubhostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapSubhostName.setStatus("current")
_TmsTrapComponentName_Type = DisplayString
_TmsTrapComponentName_Object = MibScalar
tmsTrapComponentName = _TmsTrapComponentName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 12),
    _TmsTrapComponentName_Type()
)
tmsTrapComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapComponentName.setStatus("current")
_TmsTrapBgpPeer_Type = IpAddress
_TmsTrapBgpPeer_Object = MibScalar
tmsTrapBgpPeer = _TmsTrapBgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 13),
    _TmsTrapBgpPeer_Type()
)
tmsTrapBgpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapBgpPeer.setStatus("current")
_TmsTrapGreSource_Type = IpAddress
_TmsTrapGreSource_Object = MibScalar
tmsTrapGreSource = _TmsTrapGreSource_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 14),
    _TmsTrapGreSource_Type()
)
tmsTrapGreSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapGreSource.setStatus("current")
_TmsTrapGreDestination_Type = IpAddress
_TmsTrapGreDestination_Object = MibScalar
tmsTrapGreDestination = _TmsTrapGreDestination_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 15),
    _TmsTrapGreDestination_Type()
)
tmsTrapGreDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapGreDestination.setStatus("current")
_TmsTrapNexthop_Type = IpAddress
_TmsTrapNexthop_Object = MibScalar
tmsTrapNexthop = _TmsTrapNexthop_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 16),
    _TmsTrapNexthop_Type()
)
tmsTrapNexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapNexthop.setStatus("current")
_TmsTrapIpv6BgpPeer_Type = Ipv6Address
_TmsTrapIpv6BgpPeer_Object = MibScalar
tmsTrapIpv6BgpPeer = _TmsTrapIpv6BgpPeer_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 17),
    _TmsTrapIpv6BgpPeer_Type()
)
tmsTrapIpv6BgpPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapIpv6BgpPeer.setStatus("current")
_TmsTrapIpv6GreSource_Type = Ipv6Address
_TmsTrapIpv6GreSource_Object = MibScalar
tmsTrapIpv6GreSource = _TmsTrapIpv6GreSource_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 18),
    _TmsTrapIpv6GreSource_Type()
)
tmsTrapIpv6GreSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapIpv6GreSource.setStatus("current")
_TmsTrapIpv6GreDestination_Type = Ipv6Address
_TmsTrapIpv6GreDestination_Object = MibScalar
tmsTrapIpv6GreDestination = _TmsTrapIpv6GreDestination_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 19),
    _TmsTrapIpv6GreDestination_Type()
)
tmsTrapIpv6GreDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapIpv6GreDestination.setStatus("current")
_TmsTrapIpv6Nexthop_Type = Ipv6Address
_TmsTrapIpv6Nexthop_Object = MibScalar
tmsTrapIpv6Nexthop = _TmsTrapIpv6Nexthop_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 2, 20),
    _TmsTrapIpv6Nexthop_Type()
)
tmsTrapIpv6Nexthop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsTrapIpv6Nexthop.setStatus("current")
_PeakflowTmsTraps_ObjectIdentity = ObjectIdentity
peakflowTmsTraps = _PeakflowTmsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3)
)
_PeakflowTmsTrapsEnumerate_ObjectIdentity = ObjectIdentity
peakflowTmsTrapsEnumerate = _PeakflowTmsTrapsEnumerate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0)
)
_PeakflowTmsObj_ObjectIdentity = ObjectIdentity
peakflowTmsObj = _PeakflowTmsObj_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5)
)
_TmsDpiConfig_ObjectIdentity = ObjectIdentity
tmsDpiConfig = _TmsDpiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 1)
)
_TmsVersion_Type = DisplayString
_TmsVersion_Object = MibScalar
tmsVersion = _TmsVersion_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 1, 1),
    _TmsVersion_Type()
)
tmsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsVersion.setStatus("current")
_TmsLastUpdate_Type = DisplayString
_TmsLastUpdate_Object = MibScalar
tmsLastUpdate = _TmsLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 1, 2),
    _TmsLastUpdate_Type()
)
tmsLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsLastUpdate.setStatus("current")
_TmsMitigationConfig_ObjectIdentity = ObjectIdentity
tmsMitigationConfig = _TmsMitigationConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2)
)
_TmsMitigationLastUpdate_Type = DisplayString
_TmsMitigationLastUpdate_Object = MibScalar
tmsMitigationLastUpdate = _TmsMitigationLastUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 1),
    _TmsMitigationLastUpdate_Type()
)
tmsMitigationLastUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsMitigationLastUpdate.setStatus("current")
_TmsMitigationNumber_Type = TmsTableIndexOrZero
_TmsMitigationNumber_Object = MibScalar
tmsMitigationNumber = _TmsMitigationNumber_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 2),
    _TmsMitigationNumber_Type()
)
tmsMitigationNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsMitigationNumber.setStatus("current")
_TmsMitigationTable_Object = MibTable
tmsMitigationTable = _TmsMitigationTable_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3)
)
if mibBuilder.loadTexts:
    tmsMitigationTable.setStatus("current")
_TmsMitigationEntry_Object = MibTableRow
tmsMitigationEntry = _TmsMitigationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1)
)
tmsMitigationEntry.setIndexNames(
    (0, "PEAKFLOW-TMS-MIB", "tmsMitigationIndex"),
)
if mibBuilder.loadTexts:
    tmsMitigationEntry.setStatus("current")
_TmsMitigationIndex_Type = TmsTableIndex
_TmsMitigationIndex_Object = MibTableColumn
tmsMitigationIndex = _TmsMitigationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 1),
    _TmsMitigationIndex_Type()
)
tmsMitigationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsMitigationIndex.setStatus("current")
_TmsMitigationId_Type = Unsigned32
_TmsMitigationId_Object = MibTableColumn
tmsMitigationId = _TmsMitigationId_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 2),
    _TmsMitigationId_Type()
)
tmsMitigationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsMitigationId.setStatus("current")
_TmsDestinationPrefix_Type = IpAddress
_TmsDestinationPrefix_Object = MibTableColumn
tmsDestinationPrefix = _TmsDestinationPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 3),
    _TmsDestinationPrefix_Type()
)
tmsDestinationPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsDestinationPrefix.setStatus("current")


class _TmsDestinationPrefixMask_Type(Unsigned32):
    """Custom type tmsDestinationPrefixMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_TmsDestinationPrefixMask_Type.__name__ = "Unsigned32"
_TmsDestinationPrefixMask_Object = MibTableColumn
tmsDestinationPrefixMask = _TmsDestinationPrefixMask_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 4),
    _TmsDestinationPrefixMask_Type()
)
tmsDestinationPrefixMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsDestinationPrefixMask.setStatus("current")
_TmsMitigationName_Type = DisplayString
_TmsMitigationName_Object = MibTableColumn
tmsMitigationName = _TmsMitigationName_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 5),
    _TmsMitigationName_Type()
)
tmsMitigationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsMitigationName.setStatus("current")
_TmsIpv6DestinationPrefix_Type = Ipv6AddressPrefix
_TmsIpv6DestinationPrefix_Object = MibTableColumn
tmsIpv6DestinationPrefix = _TmsIpv6DestinationPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 6),
    _TmsIpv6DestinationPrefix_Type()
)
tmsIpv6DestinationPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsIpv6DestinationPrefix.setStatus("current")


class _TmsIpv6DestinationPrefixMask_Type(Unsigned32):
    """Custom type tmsIpv6DestinationPrefixMask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_TmsIpv6DestinationPrefixMask_Type.__name__ = "Unsigned32"
_TmsIpv6DestinationPrefixMask_Object = MibTableColumn
tmsIpv6DestinationPrefixMask = _TmsIpv6DestinationPrefixMask_Object(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 5, 2, 3, 1, 7),
    _TmsIpv6DestinationPrefixMask_Type()
)
tmsIpv6DestinationPrefixMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmsIpv6DestinationPrefixMask.setStatus("current")

# Managed Objects groups


# Notification objects

hostFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 1)
)
hostFault.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsHostFault"))
)
if mibBuilder.loadTexts:
    hostFault.setStatus(
        "obsolete"
    )

greTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 2)
)
greTunnelDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapGreSource"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapGreDestination"))
)
if mibBuilder.loadTexts:
    greTunnelDown.setStatus(
        "current"
    )

greTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 3)
)
greTunnelUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapGreSource"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapGreDestination"))
)
if mibBuilder.loadTexts:
    greTunnelUp.setStatus(
        "current"
    )

tmsLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 4)
)
tmsLinkUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"))
)
if mibBuilder.loadTexts:
    tmsLinkUp.setStatus(
        "obsolete"
    )

tmsLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 5)
)
tmsLinkDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"))
)
if mibBuilder.loadTexts:
    tmsLinkDown.setStatus(
        "obsolete"
    )

subHostUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 6)
)
subHostUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"))
)
if mibBuilder.loadTexts:
    subHostUp.setStatus(
        "current"
    )

subHostDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 7)
)
subHostDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"))
)
if mibBuilder.loadTexts:
    subHostDown.setStatus(
        "current"
    )

tmsBgpNeighborDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 8)
)
tmsBgpNeighborDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapBgpPeer"))
)
if mibBuilder.loadTexts:
    tmsBgpNeighborDown.setStatus(
        "current"
    )

tmsBgpNeighborUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 9)
)
tmsBgpNeighborUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapBgpPeer"))
)
if mibBuilder.loadTexts:
    tmsBgpNeighborUp.setStatus(
        "current"
    )

tmsNexthopDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 10)
)
tmsNexthopDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapNexthop"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    tmsNexthopDown.setStatus(
        "current"
    )

tmsNexthopUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 11)
)
tmsNexthopUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapNexthop"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    tmsNexthopUp.setStatus(
        "current"
    )

tmsMitigationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 12)
)
tmsMitigationError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsMitigationIndex"),
        ("PEAKFLOW-TMS-MIB", "tmsMitigationName"))
)
if mibBuilder.loadTexts:
    tmsMitigationError.setStatus(
        "current"
    )

tmsMitigationSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 13)
)
tmsMitigationSuspended.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsMitigationIndex"),
        ("PEAKFLOW-TMS-MIB", "tmsMitigationName"))
)
if mibBuilder.loadTexts:
    tmsMitigationSuspended.setStatus(
        "current"
    )

tmsMitigationRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 14)
)
tmsMitigationRunning.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsMitigationIndex"),
        ("PEAKFLOW-TMS-MIB", "tmsMitigationName"))
)
if mibBuilder.loadTexts:
    tmsMitigationRunning.setStatus(
        "current"
    )

tmsConfigMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 15)
)
tmsConfigMissing.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsConfigMissing.setStatus(
        "current"
    )

tmsConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 16)
)
tmsConfigError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsConfigError.setStatus(
        "current"
    )

tmsConfigOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 17)
)
tmsConfigOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsConfigOk.setStatus(
        "current"
    )

tmsHwDeviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 18)
)
tmsHwDeviceDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsHwDeviceDown.setStatus(
        "current"
    )

tmsHwDeviceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 19)
)
tmsHwDeviceUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsHwDeviceUp.setStatus(
        "current"
    )

tmsHwSensorCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 20)
)
tmsHwSensorCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsHwSensorCritical.setStatus(
        "current"
    )

tmsHwSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 21)
)
tmsHwSensorOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsHwSensorOk.setStatus(
        "current"
    )

tmsSwComponentDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 22)
)
tmsSwComponentDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSwComponentDown.setStatus(
        "current"
    )

tmsSwComponentUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 23)
)
tmsSwComponentUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapSubhostName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSwComponentUp.setStatus(
        "current"
    )

tmsSystemStatusCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 24)
)
tmsSystemStatusCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSystemStatusCritical.setStatus(
        "current"
    )

tmsSystemStatusDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 25)
)
tmsSystemStatusDegraded.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSystemStatusDegraded.setStatus(
        "current"
    )

tmsSystemStatusNominal = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 26)
)
tmsSystemStatusNominal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSystemStatusNominal.setStatus(
        "current"
    )

tmsFilesystemCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 27)
)
tmsFilesystemCritical.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsFilesystemCritical.setStatus(
        "current"
    )

tmsFilesystemNominal = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 28)
)
tmsFilesystemNominal.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsFilesystemNominal.setStatus(
        "current"
    )

tmsHwSensorUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 29)
)
tmsHwSensorUnknown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsHwSensorUnknown.setStatus(
        "current"
    )

tmsSpCommunicationUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 30)
)
tmsSpCommunicationUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSpCommunicationUp.setStatus(
        "current"
    )

tmsSpCommunicationDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 31)
)
tmsSpCommunicationDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSpCommunicationDown.setStatus(
        "current"
    )

tmsSystemStatusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 32)
)
tmsSystemStatusError.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSystemStatusError.setStatus(
        "current"
    )

tmsAutomitigationBgpEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 33)
)
tmsAutomitigationBgpEnabled.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsAutomitigationBgpEnabled.setStatus(
        "current"
    )

tmsAutomitigationBgpDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 34)
)
tmsAutomitigationBgpDisabled.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsAutomitigationBgpDisabled.setStatus(
        "current"
    )

tmsAutomitigationBgpSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 35)
)
tmsAutomitigationBgpSuspended.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsAutomitigationBgpSuspended.setStatus(
        "current"
    )

tmsIpv6GreTunnelDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 36)
)
tmsIpv6GreTunnelDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreSource"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreDestination"))
)
if mibBuilder.loadTexts:
    tmsIpv6GreTunnelDown.setStatus(
        "current"
    )

tmsIpv6GreTunnelUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 37)
)
tmsIpv6GreTunnelUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreSource"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6GreDestination"))
)
if mibBuilder.loadTexts:
    tmsIpv6GreTunnelUp.setStatus(
        "current"
    )

tmsIpv6BgpNeighborDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 38)
)
tmsIpv6BgpNeighborDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6BgpPeer"))
)
if mibBuilder.loadTexts:
    tmsIpv6BgpNeighborDown.setStatus(
        "current"
    )

tmsIpv6BgpNeighborUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 39)
)
tmsIpv6BgpNeighborUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6BgpPeer"))
)
if mibBuilder.loadTexts:
    tmsIpv6BgpNeighborUp.setStatus(
        "current"
    )

tmsIpv6NexthopDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 40)
)
tmsIpv6NexthopDown.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6Nexthop"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    tmsIpv6NexthopDown.setStatus(
        "current"
    )

tmsIpv6NexthopUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 41)
)
tmsIpv6NexthopUp.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapIpv6Nexthop"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    tmsIpv6NexthopUp.setStatus(
        "current"
    )

tmsPerformanceOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 42)
)
tmsPerformanceOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsPerformanceOk.setStatus(
        "current"
    )

tmsPerformanceLossy = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 43)
)
tmsPerformanceLossy.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsPerformanceLossy.setStatus(
        "current"
    )

tmsSystemPrefixesOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 44)
)
tmsSystemPrefixesOk.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSystemPrefixesOk.setStatus(
        "current"
    )

tmsSystemPrefixesMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 9694, 1, 5, 3, 0, 45)
)
tmsSystemPrefixesMissing.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapString"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapDetail"),
        ("PEAKFLOW-TMS-MIB", "tmsTrapComponentName"))
)
if mibBuilder.loadTexts:
    tmsSystemPrefixesMissing.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKFLOW-TMS-MIB",
    **{"TmsTableIndex": TmsTableIndex,
       "TmsTableIndexOrZero": TmsTableIndexOrZero,
       "TmsPercentage": TmsPercentage,
       "TmsHundredths": TmsHundredths,
       "peakflowTmsMIB": peakflowTmsMIB,
       "peakflowTmsMgr": peakflowTmsMgr,
       "tmsHostFault": tmsHostFault,
       "tmsHostUpTime": tmsHostUpTime,
       "deviceCpuLoadAvg1min": deviceCpuLoadAvg1min,
       "deviceCpuLoadAvg5min": deviceCpuLoadAvg5min,
       "deviceCpuLoadAvg15min": deviceCpuLoadAvg15min,
       "deviceDiskUsage": deviceDiskUsage,
       "devicePhysicalMemoryUsage": devicePhysicalMemoryUsage,
       "deviceSwapSpaceUsage": deviceSwapSpaceUsage,
       "tmsTrapString": tmsTrapString,
       "tmsTrapDetail": tmsTrapDetail,
       "tmsTrapSubhostName": tmsTrapSubhostName,
       "tmsTrapComponentName": tmsTrapComponentName,
       "tmsTrapBgpPeer": tmsTrapBgpPeer,
       "tmsTrapGreSource": tmsTrapGreSource,
       "tmsTrapGreDestination": tmsTrapGreDestination,
       "tmsTrapNexthop": tmsTrapNexthop,
       "tmsTrapIpv6BgpPeer": tmsTrapIpv6BgpPeer,
       "tmsTrapIpv6GreSource": tmsTrapIpv6GreSource,
       "tmsTrapIpv6GreDestination": tmsTrapIpv6GreDestination,
       "tmsTrapIpv6Nexthop": tmsTrapIpv6Nexthop,
       "peakflowTmsTraps": peakflowTmsTraps,
       "peakflowTmsTrapsEnumerate": peakflowTmsTrapsEnumerate,
       "hostFault": hostFault,
       "greTunnelDown": greTunnelDown,
       "greTunnelUp": greTunnelUp,
       "tmsLinkUp": tmsLinkUp,
       "tmsLinkDown": tmsLinkDown,
       "subHostUp": subHostUp,
       "subHostDown": subHostDown,
       "tmsBgpNeighborDown": tmsBgpNeighborDown,
       "tmsBgpNeighborUp": tmsBgpNeighborUp,
       "tmsNexthopDown": tmsNexthopDown,
       "tmsNexthopUp": tmsNexthopUp,
       "tmsMitigationError": tmsMitigationError,
       "tmsMitigationSuspended": tmsMitigationSuspended,
       "tmsMitigationRunning": tmsMitigationRunning,
       "tmsConfigMissing": tmsConfigMissing,
       "tmsConfigError": tmsConfigError,
       "tmsConfigOk": tmsConfigOk,
       "tmsHwDeviceDown": tmsHwDeviceDown,
       "tmsHwDeviceUp": tmsHwDeviceUp,
       "tmsHwSensorCritical": tmsHwSensorCritical,
       "tmsHwSensorOk": tmsHwSensorOk,
       "tmsSwComponentDown": tmsSwComponentDown,
       "tmsSwComponentUp": tmsSwComponentUp,
       "tmsSystemStatusCritical": tmsSystemStatusCritical,
       "tmsSystemStatusDegraded": tmsSystemStatusDegraded,
       "tmsSystemStatusNominal": tmsSystemStatusNominal,
       "tmsFilesystemCritical": tmsFilesystemCritical,
       "tmsFilesystemNominal": tmsFilesystemNominal,
       "tmsHwSensorUnknown": tmsHwSensorUnknown,
       "tmsSpCommunicationUp": tmsSpCommunicationUp,
       "tmsSpCommunicationDown": tmsSpCommunicationDown,
       "tmsSystemStatusError": tmsSystemStatusError,
       "tmsAutomitigationBgpEnabled": tmsAutomitigationBgpEnabled,
       "tmsAutomitigationBgpDisabled": tmsAutomitigationBgpDisabled,
       "tmsAutomitigationBgpSuspended": tmsAutomitigationBgpSuspended,
       "tmsIpv6GreTunnelDown": tmsIpv6GreTunnelDown,
       "tmsIpv6GreTunnelUp": tmsIpv6GreTunnelUp,
       "tmsIpv6BgpNeighborDown": tmsIpv6BgpNeighborDown,
       "tmsIpv6BgpNeighborUp": tmsIpv6BgpNeighborUp,
       "tmsIpv6NexthopDown": tmsIpv6NexthopDown,
       "tmsIpv6NexthopUp": tmsIpv6NexthopUp,
       "tmsPerformanceOk": tmsPerformanceOk,
       "tmsPerformanceLossy": tmsPerformanceLossy,
       "tmsSystemPrefixesOk": tmsSystemPrefixesOk,
       "tmsSystemPrefixesMissing": tmsSystemPrefixesMissing,
       "peakflowTmsObj": peakflowTmsObj,
       "tmsDpiConfig": tmsDpiConfig,
       "tmsVersion": tmsVersion,
       "tmsLastUpdate": tmsLastUpdate,
       "tmsMitigationConfig": tmsMitigationConfig,
       "tmsMitigationLastUpdate": tmsMitigationLastUpdate,
       "tmsMitigationNumber": tmsMitigationNumber,
       "tmsMitigationTable": tmsMitigationTable,
       "tmsMitigationEntry": tmsMitigationEntry,
       "tmsMitigationIndex": tmsMitigationIndex,
       "tmsMitigationId": tmsMitigationId,
       "tmsDestinationPrefix": tmsDestinationPrefix,
       "tmsDestinationPrefixMask": tmsDestinationPrefixMask,
       "tmsMitigationName": tmsMitigationName,
       "tmsIpv6DestinationPrefix": tmsIpv6DestinationPrefix,
       "tmsIpv6DestinationPrefixMask": tmsIpv6DestinationPrefixMask}
)
