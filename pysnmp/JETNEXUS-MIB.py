# SNMP MIB module (JETNEXUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JETNEXUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:38 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

jetnexusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38370)
)
jetnexusMIB.setRevisions(
        ("2014-10-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JetnexusData_ObjectIdentity = ObjectIdentity
jetnexusData = _JetnexusData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38370, 1)
)
_JetnexusGlobal_ObjectIdentity = ObjectIdentity
jetnexusGlobal = _JetnexusGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1)
)
_JetnexusOverallInputBytes_Type = Counter64
_JetnexusOverallInputBytes_Object = MibScalar
jetnexusOverallInputBytes = _JetnexusOverallInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 1),
    _JetnexusOverallInputBytes_Type()
)
jetnexusOverallInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusOverallInputBytes.setStatus("current")
_JetnexusOverallOutputBytes_Type = Counter64
_JetnexusOverallOutputBytes_Object = MibScalar
jetnexusOverallOutputBytes = _JetnexusOverallOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 2),
    _JetnexusOverallOutputBytes_Type()
)
jetnexusOverallOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusOverallOutputBytes.setStatus("current")
_JetnexusCompressedInputBytes_Type = Counter64
_JetnexusCompressedInputBytes_Object = MibScalar
jetnexusCompressedInputBytes = _JetnexusCompressedInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 3),
    _JetnexusCompressedInputBytes_Type()
)
jetnexusCompressedInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusCompressedInputBytes.setStatus("current")
_JetnexusCompressedOutputBytes_Type = Counter64
_JetnexusCompressedOutputBytes_Object = MibScalar
jetnexusCompressedOutputBytes = _JetnexusCompressedOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 4),
    _JetnexusCompressedOutputBytes_Type()
)
jetnexusCompressedOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusCompressedOutputBytes.setStatus("current")
_JetnexusVersionInfo_Type = OctetString
_JetnexusVersionInfo_Object = MibScalar
jetnexusVersionInfo = _JetnexusVersionInfo_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 5),
    _JetnexusVersionInfo_Type()
)
jetnexusVersionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusVersionInfo.setStatus("current")
_JetnexusTotalClientConnections_Type = Counter64
_JetnexusTotalClientConnections_Object = MibScalar
jetnexusTotalClientConnections = _JetnexusTotalClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 6),
    _JetnexusTotalClientConnections_Type()
)
jetnexusTotalClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusTotalClientConnections.setStatus("current")
_JetnexusCpuPercent_Type = Integer32
_JetnexusCpuPercent_Object = MibScalar
jetnexusCpuPercent = _JetnexusCpuPercent_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 7),
    _JetnexusCpuPercent_Type()
)
jetnexusCpuPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusCpuPercent.setStatus("current")
_JetnexusDiskFreePercent_Type = Integer32
_JetnexusDiskFreePercent_Object = MibScalar
jetnexusDiskFreePercent = _JetnexusDiskFreePercent_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 8),
    _JetnexusDiskFreePercent_Type()
)
jetnexusDiskFreePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusDiskFreePercent.setStatus("current")
_JetnexusMemoryPercent_Type = Integer32
_JetnexusMemoryPercent_Object = MibScalar
jetnexusMemoryPercent = _JetnexusMemoryPercent_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 9),
    _JetnexusMemoryPercent_Type()
)
jetnexusMemoryPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusMemoryPercent.setStatus("current")
_JetnexusCurrentConnections_Type = Integer32
_JetnexusCurrentConnections_Object = MibScalar
jetnexusCurrentConnections = _JetnexusCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 1, 10),
    _JetnexusCurrentConnections_Type()
)
jetnexusCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jetnexusCurrentConnections.setStatus("current")
_JnvirtualserviceTable_Object = MibTable
jnvirtualserviceTable = _JnvirtualserviceTable_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2)
)
if mibBuilder.loadTexts:
    jnvirtualserviceTable.setStatus("current")
_JnvirtualserviceEntry_Object = MibTableRow
jnvirtualserviceEntry = _JnvirtualserviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1)
)
jnvirtualserviceEntry.setIndexNames(
    (0, "JETNEXUS-MIB", "jnvirtualserviceIndexVirtualService"),
)
if mibBuilder.loadTexts:
    jnvirtualserviceEntry.setStatus("current")


class _JnvirtualserviceIndexVirtualService_Type(Integer32):
    """Custom type jnvirtualserviceIndexVirtualService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnvirtualserviceIndexVirtualService_Type.__name__ = "Integer32"
_JnvirtualserviceIndexVirtualService_Object = MibTableColumn
jnvirtualserviceIndexVirtualService = _JnvirtualserviceIndexVirtualService_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 1),
    _JnvirtualserviceIndexVirtualService_Type()
)
jnvirtualserviceIndexVirtualService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnvirtualserviceIndexVirtualService.setStatus("current")
_JnvirtualserviceVSAddrPort_Type = OctetString
_JnvirtualserviceVSAddrPort_Object = MibTableColumn
jnvirtualserviceVSAddrPort = _JnvirtualserviceVSAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 2),
    _JnvirtualserviceVSAddrPort_Type()
)
jnvirtualserviceVSAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceVSAddrPort.setStatus("current")
_JnvirtualserviceOverallInputBytes_Type = Counter64
_JnvirtualserviceOverallInputBytes_Object = MibTableColumn
jnvirtualserviceOverallInputBytes = _JnvirtualserviceOverallInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 3),
    _JnvirtualserviceOverallInputBytes_Type()
)
jnvirtualserviceOverallInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceOverallInputBytes.setStatus("current")
_JnvirtualserviceOverallOutputBytes_Type = Counter64
_JnvirtualserviceOverallOutputBytes_Object = MibTableColumn
jnvirtualserviceOverallOutputBytes = _JnvirtualserviceOverallOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 4),
    _JnvirtualserviceOverallOutputBytes_Type()
)
jnvirtualserviceOverallOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceOverallOutputBytes.setStatus("current")
_JnvirtualserviceCacheBytes_Type = Counter64
_JnvirtualserviceCacheBytes_Object = MibTableColumn
jnvirtualserviceCacheBytes = _JnvirtualserviceCacheBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 5),
    _JnvirtualserviceCacheBytes_Type()
)
jnvirtualserviceCacheBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceCacheBytes.setStatus("current")
_JnvirtualserviceCompressionPercent_Type = Integer32
_JnvirtualserviceCompressionPercent_Object = MibTableColumn
jnvirtualserviceCompressionPercent = _JnvirtualserviceCompressionPercent_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 6),
    _JnvirtualserviceCompressionPercent_Type()
)
jnvirtualserviceCompressionPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceCompressionPercent.setStatus("current")
_JnvirtualservicePresentClientConnections_Type = Integer32
_JnvirtualservicePresentClientConnections_Object = MibTableColumn
jnvirtualservicePresentClientConnections = _JnvirtualservicePresentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 7),
    _JnvirtualservicePresentClientConnections_Type()
)
jnvirtualservicePresentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualservicePresentClientConnections.setStatus("current")
_JnvirtualserviceHitCount_Type = Counter64
_JnvirtualserviceHitCount_Object = MibTableColumn
jnvirtualserviceHitCount = _JnvirtualserviceHitCount_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 8),
    _JnvirtualserviceHitCount_Type()
)
jnvirtualserviceHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceHitCount.setStatus("current")
_JnvirtualserviceCacheHits_Type = Counter64
_JnvirtualserviceCacheHits_Object = MibTableColumn
jnvirtualserviceCacheHits = _JnvirtualserviceCacheHits_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 9),
    _JnvirtualserviceCacheHits_Type()
)
jnvirtualserviceCacheHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceCacheHits.setStatus("current")
_JnvirtualserviceCacheHitsPercent_Type = Integer32
_JnvirtualserviceCacheHitsPercent_Object = MibTableColumn
jnvirtualserviceCacheHitsPercent = _JnvirtualserviceCacheHitsPercent_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 10),
    _JnvirtualserviceCacheHitsPercent_Type()
)
jnvirtualserviceCacheHitsPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceCacheHitsPercent.setStatus("current")
_JnvirtualserviceVSStatus_Type = OctetString
_JnvirtualserviceVSStatus_Object = MibTableColumn
jnvirtualserviceVSStatus = _JnvirtualserviceVSStatus_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 2, 1, 11),
    _JnvirtualserviceVSStatus_Type()
)
jnvirtualserviceVSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnvirtualserviceVSStatus.setStatus("current")
_JnrealserverTable_Object = MibTable
jnrealserverTable = _JnrealserverTable_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3)
)
if mibBuilder.loadTexts:
    jnrealserverTable.setStatus("current")
_JnrealserverEntry_Object = MibTableRow
jnrealserverEntry = _JnrealserverEntry_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1)
)
jnrealserverEntry.setIndexNames(
    (0, "JETNEXUS-MIB", "jnrealserverIndexVirtualService"),
    (0, "JETNEXUS-MIB", "jnrealserverIndexRealServer"),
)
if mibBuilder.loadTexts:
    jnrealserverEntry.setStatus("current")


class _JnrealserverIndexVirtualService_Type(Integer32):
    """Custom type jnrealserverIndexVirtualService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnrealserverIndexVirtualService_Type.__name__ = "Integer32"
_JnrealserverIndexVirtualService_Object = MibTableColumn
jnrealserverIndexVirtualService = _JnrealserverIndexVirtualService_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 1),
    _JnrealserverIndexVirtualService_Type()
)
jnrealserverIndexVirtualService.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnrealserverIndexVirtualService.setStatus("current")


class _JnrealserverIndexRealServer_Type(Integer32):
    """Custom type jnrealserverIndexRealServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_JnrealserverIndexRealServer_Type.__name__ = "Integer32"
_JnrealserverIndexRealServer_Object = MibTableColumn
jnrealserverIndexRealServer = _JnrealserverIndexRealServer_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 2),
    _JnrealserverIndexRealServer_Type()
)
jnrealserverIndexRealServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnrealserverIndexRealServer.setStatus("current")
_JnrealserverVSAddrPort_Type = OctetString
_JnrealserverVSAddrPort_Object = MibTableColumn
jnrealserverVSAddrPort = _JnrealserverVSAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 3),
    _JnrealserverVSAddrPort_Type()
)
jnrealserverVSAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverVSAddrPort.setStatus("current")
_JnrealserverRSAddrPort_Type = OctetString
_JnrealserverRSAddrPort_Object = MibTableColumn
jnrealserverRSAddrPort = _JnrealserverRSAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 4),
    _JnrealserverRSAddrPort_Type()
)
jnrealserverRSAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverRSAddrPort.setStatus("current")
_JnrealserverOverallInputBytes_Type = Counter64
_JnrealserverOverallInputBytes_Object = MibTableColumn
jnrealserverOverallInputBytes = _JnrealserverOverallInputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 5),
    _JnrealserverOverallInputBytes_Type()
)
jnrealserverOverallInputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverOverallInputBytes.setStatus("current")
_JnrealserverOverallOutputBytes_Type = Counter64
_JnrealserverOverallOutputBytes_Object = MibTableColumn
jnrealserverOverallOutputBytes = _JnrealserverOverallOutputBytes_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 6),
    _JnrealserverOverallOutputBytes_Type()
)
jnrealserverOverallOutputBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverOverallOutputBytes.setStatus("current")
_JnrealserverCompressionPercent_Type = Integer32
_JnrealserverCompressionPercent_Object = MibTableColumn
jnrealserverCompressionPercent = _JnrealserverCompressionPercent_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 7),
    _JnrealserverCompressionPercent_Type()
)
jnrealserverCompressionPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverCompressionPercent.setStatus("current")
_JnrealserverPresentClientConnections_Type = Integer32
_JnrealserverPresentClientConnections_Object = MibTableColumn
jnrealserverPresentClientConnections = _JnrealserverPresentClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 8),
    _JnrealserverPresentClientConnections_Type()
)
jnrealserverPresentClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverPresentClientConnections.setStatus("current")
_JnrealserverPoolUsage_Type = Integer32
_JnrealserverPoolUsage_Object = MibTableColumn
jnrealserverPoolUsage = _JnrealserverPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 9),
    _JnrealserverPoolUsage_Type()
)
jnrealserverPoolUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverPoolUsage.setStatus("current")
_JnrealserverHitCount_Type = Counter64
_JnrealserverHitCount_Object = MibTableColumn
jnrealserverHitCount = _JnrealserverHitCount_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 10),
    _JnrealserverHitCount_Type()
)
jnrealserverHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverHitCount.setStatus("current")
_JnrealserverRSStatus_Type = OctetString
_JnrealserverRSStatus_Object = MibTableColumn
jnrealserverRSStatus = _JnrealserverRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 38370, 1, 3, 1, 11),
    _JnrealserverRSStatus_Type()
)
jnrealserverRSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnrealserverRSStatus.setStatus("current")
_JetnexusConformance_ObjectIdentity = ObjectIdentity
jetnexusConformance = _JetnexusConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38370, 2)
)
_JetnexusGroups_ObjectIdentity = ObjectIdentity
jetnexusGroups = _JetnexusGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38370, 2, 1)
)
_JetnexusCompliances_ObjectIdentity = ObjectIdentity
jetnexusCompliances = _JetnexusCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38370, 2, 2)
)

# Managed Objects groups

jetnexusCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 38370, 2, 1, 1)
)
jetnexusCurrentGroup.setObjects(
      *(("JETNEXUS-MIB", "jetnexusOverallInputBytes"),
        ("JETNEXUS-MIB", "jetnexusOverallOutputBytes"),
        ("JETNEXUS-MIB", "jetnexusCompressedInputBytes"),
        ("JETNEXUS-MIB", "jetnexusCompressedOutputBytes"),
        ("JETNEXUS-MIB", "jetnexusVersionInfo"),
        ("JETNEXUS-MIB", "jetnexusTotalClientConnections"),
        ("JETNEXUS-MIB", "jetnexusCpuPercent"),
        ("JETNEXUS-MIB", "jetnexusDiskFreePercent"),
        ("JETNEXUS-MIB", "jetnexusMemoryPercent"),
        ("JETNEXUS-MIB", "jetnexusCurrentConnections"),
        ("JETNEXUS-MIB", "jnvirtualserviceVSAddrPort"),
        ("JETNEXUS-MIB", "jnvirtualserviceOverallInputBytes"),
        ("JETNEXUS-MIB", "jnvirtualserviceOverallOutputBytes"),
        ("JETNEXUS-MIB", "jnvirtualserviceCacheBytes"),
        ("JETNEXUS-MIB", "jnvirtualserviceCompressionPercent"),
        ("JETNEXUS-MIB", "jnvirtualservicePresentClientConnections"),
        ("JETNEXUS-MIB", "jnvirtualserviceHitCount"),
        ("JETNEXUS-MIB", "jnvirtualserviceCacheHits"),
        ("JETNEXUS-MIB", "jnvirtualserviceCacheHitsPercent"),
        ("JETNEXUS-MIB", "jnvirtualserviceVSStatus"),
        ("JETNEXUS-MIB", "jnrealserverVSAddrPort"),
        ("JETNEXUS-MIB", "jnrealserverRSAddrPort"),
        ("JETNEXUS-MIB", "jnrealserverOverallInputBytes"),
        ("JETNEXUS-MIB", "jnrealserverOverallOutputBytes"),
        ("JETNEXUS-MIB", "jnrealserverCompressionPercent"),
        ("JETNEXUS-MIB", "jnrealserverPresentClientConnections"),
        ("JETNEXUS-MIB", "jnrealserverPoolUsage"),
        ("JETNEXUS-MIB", "jnrealserverHitCount"),
        ("JETNEXUS-MIB", "jnrealserverRSStatus"))
)
if mibBuilder.loadTexts:
    jetnexusCurrentGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

jetnexusBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 38370, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jetnexusBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JETNEXUS-MIB",
    **{"jetnexusMIB": jetnexusMIB,
       "jetnexusData": jetnexusData,
       "jetnexusGlobal": jetnexusGlobal,
       "jetnexusOverallInputBytes": jetnexusOverallInputBytes,
       "jetnexusOverallOutputBytes": jetnexusOverallOutputBytes,
       "jetnexusCompressedInputBytes": jetnexusCompressedInputBytes,
       "jetnexusCompressedOutputBytes": jetnexusCompressedOutputBytes,
       "jetnexusVersionInfo": jetnexusVersionInfo,
       "jetnexusTotalClientConnections": jetnexusTotalClientConnections,
       "jetnexusCpuPercent": jetnexusCpuPercent,
       "jetnexusDiskFreePercent": jetnexusDiskFreePercent,
       "jetnexusMemoryPercent": jetnexusMemoryPercent,
       "jetnexusCurrentConnections": jetnexusCurrentConnections,
       "jnvirtualserviceTable": jnvirtualserviceTable,
       "jnvirtualserviceEntry": jnvirtualserviceEntry,
       "jnvirtualserviceIndexVirtualService": jnvirtualserviceIndexVirtualService,
       "jnvirtualserviceVSAddrPort": jnvirtualserviceVSAddrPort,
       "jnvirtualserviceOverallInputBytes": jnvirtualserviceOverallInputBytes,
       "jnvirtualserviceOverallOutputBytes": jnvirtualserviceOverallOutputBytes,
       "jnvirtualserviceCacheBytes": jnvirtualserviceCacheBytes,
       "jnvirtualserviceCompressionPercent": jnvirtualserviceCompressionPercent,
       "jnvirtualservicePresentClientConnections": jnvirtualservicePresentClientConnections,
       "jnvirtualserviceHitCount": jnvirtualserviceHitCount,
       "jnvirtualserviceCacheHits": jnvirtualserviceCacheHits,
       "jnvirtualserviceCacheHitsPercent": jnvirtualserviceCacheHitsPercent,
       "jnvirtualserviceVSStatus": jnvirtualserviceVSStatus,
       "jnrealserverTable": jnrealserverTable,
       "jnrealserverEntry": jnrealserverEntry,
       "jnrealserverIndexVirtualService": jnrealserverIndexVirtualService,
       "jnrealserverIndexRealServer": jnrealserverIndexRealServer,
       "jnrealserverVSAddrPort": jnrealserverVSAddrPort,
       "jnrealserverRSAddrPort": jnrealserverRSAddrPort,
       "jnrealserverOverallInputBytes": jnrealserverOverallInputBytes,
       "jnrealserverOverallOutputBytes": jnrealserverOverallOutputBytes,
       "jnrealserverCompressionPercent": jnrealserverCompressionPercent,
       "jnrealserverPresentClientConnections": jnrealserverPresentClientConnections,
       "jnrealserverPoolUsage": jnrealserverPoolUsage,
       "jnrealserverHitCount": jnrealserverHitCount,
       "jnrealserverRSStatus": jnrealserverRSStatus,
       "jetnexusConformance": jetnexusConformance,
       "jetnexusGroups": jetnexusGroups,
       "jetnexusCurrentGroup": jetnexusCurrentGroup,
       "jetnexusCompliances": jetnexusCompliances,
       "jetnexusBasicCompliance": jetnexusBasicCompliance}
)
