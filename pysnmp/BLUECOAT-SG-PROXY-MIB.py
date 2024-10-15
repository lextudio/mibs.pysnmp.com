# SNMP MIB module (BLUECOAT-SG-PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BLUECOAT-SG-PROXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:22 2024
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

(blueCoatMgmt,) = mibBuilder.importSymbols(
    "BLUECOAT-MIB",
    "blueCoatMgmt")

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

bluecoatSGProxyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11)
)
bluecoatSGProxyMIB.setRevisions(
        ("2011-11-01 03:00",
         "2007-11-05 03:00",
         "2007-08-28 03:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SgProxyConfig_ObjectIdentity = ObjectIdentity
sgProxyConfig = _SgProxyConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 1)
)
_SgProxyAdmin_Type = DisplayString
_SgProxyAdmin_Object = MibScalar
sgProxyAdmin = _SgProxyAdmin_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 1),
    _SgProxyAdmin_Type()
)
sgProxyAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyAdmin.setStatus("current")
_SgProxySoftware_Type = DisplayString
_SgProxySoftware_Object = MibScalar
sgProxySoftware = _SgProxySoftware_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 2),
    _SgProxySoftware_Type()
)
sgProxySoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxySoftware.setStatus("current")
_SgProxyVersion_Type = DisplayString
_SgProxyVersion_Object = MibScalar
sgProxyVersion = _SgProxyVersion_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 3),
    _SgProxyVersion_Type()
)
sgProxyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyVersion.setStatus("current")
_SgProxySerialNumber_Type = DisplayString
_SgProxySerialNumber_Object = MibScalar
sgProxySerialNumber = _SgProxySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 1, 4),
    _SgProxySerialNumber_Type()
)
sgProxySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxySerialNumber.setStatus("current")
_SgProxySystem_ObjectIdentity = ObjectIdentity
sgProxySystem = _SgProxySystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2)
)
_SgProxyCpu_ObjectIdentity = ObjectIdentity
sgProxyCpu = _SgProxyCpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1)
)
_SgProxyCpuUpTime_Type = Counter64
_SgProxyCpuUpTime_Object = MibScalar
sgProxyCpuUpTime = _SgProxyCpuUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 1),
    _SgProxyCpuUpTime_Type()
)
sgProxyCpuUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuUpTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuUpTime.setUnits("Milliseconds")
_SgProxyCpuBusyTime_Type = Counter64
_SgProxyCpuBusyTime_Object = MibScalar
sgProxyCpuBusyTime = _SgProxyCpuBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 2),
    _SgProxyCpuBusyTime_Type()
)
sgProxyCpuBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuBusyTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuBusyTime.setUnits("Milliseconds")
_SgProxyCpuIdleTime_Type = Counter64
_SgProxyCpuIdleTime_Object = MibScalar
sgProxyCpuIdleTime = _SgProxyCpuIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 3),
    _SgProxyCpuIdleTime_Type()
)
sgProxyCpuIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuIdleTime.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuIdleTime.setUnits("Milliseconds")
_SgProxyCpuUpTimeSinceLastAccess_Type = Counter64
_SgProxyCpuUpTimeSinceLastAccess_Object = MibScalar
sgProxyCpuUpTimeSinceLastAccess = _SgProxyCpuUpTimeSinceLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 4),
    _SgProxyCpuUpTimeSinceLastAccess_Type()
)
sgProxyCpuUpTimeSinceLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuUpTimeSinceLastAccess.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuUpTimeSinceLastAccess.setUnits("Milliseconds")
_SgProxyCpuBusyTimeSinceLastAccess_Type = Counter64
_SgProxyCpuBusyTimeSinceLastAccess_Object = MibScalar
sgProxyCpuBusyTimeSinceLastAccess = _SgProxyCpuBusyTimeSinceLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 5),
    _SgProxyCpuBusyTimeSinceLastAccess_Type()
)
sgProxyCpuBusyTimeSinceLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuBusyTimeSinceLastAccess.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuBusyTimeSinceLastAccess.setUnits("Milliseconds")
_SgProxyCpuIdleTimeSinceLastAccess_Type = Counter64
_SgProxyCpuIdleTimeSinceLastAccess_Object = MibScalar
sgProxyCpuIdleTimeSinceLastAccess = _SgProxyCpuIdleTimeSinceLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 6),
    _SgProxyCpuIdleTimeSinceLastAccess_Type()
)
sgProxyCpuIdleTimeSinceLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuIdleTimeSinceLastAccess.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuIdleTimeSinceLastAccess.setUnits("Milliseconds")
_SgProxyCpuBusyPerCent_Type = Gauge32
_SgProxyCpuBusyPerCent_Object = MibScalar
sgProxyCpuBusyPerCent = _SgProxyCpuBusyPerCent_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 7),
    _SgProxyCpuBusyPerCent_Type()
)
sgProxyCpuBusyPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuBusyPerCent.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuBusyPerCent.setUnits("Percentage")
_SgProxyCpuIdlePerCent_Type = Gauge32
_SgProxyCpuIdlePerCent_Object = MibScalar
sgProxyCpuIdlePerCent = _SgProxyCpuIdlePerCent_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 1, 8),
    _SgProxyCpuIdlePerCent_Type()
)
sgProxyCpuIdlePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuIdlePerCent.setStatus("deprecated")
if mibBuilder.loadTexts:
    sgProxyCpuIdlePerCent.setUnits("Percentage")
_SgProxyCache_ObjectIdentity = ObjectIdentity
sgProxyCache = _SgProxyCache_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2)
)
_SgProxyStorage_Type = Counter64
_SgProxyStorage_Object = MibScalar
sgProxyStorage = _SgProxyStorage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2, 1),
    _SgProxyStorage_Type()
)
sgProxyStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyStorage.setStatus("current")
_SgProxyNumObjects_Type = Gauge32
_SgProxyNumObjects_Object = MibScalar
sgProxyNumObjects = _SgProxyNumObjects_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 2, 2),
    _SgProxyNumObjects_Type()
)
sgProxyNumObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyNumObjects.setStatus("current")
_SgProxyMemory_ObjectIdentity = ObjectIdentity
sgProxyMemory = _SgProxyMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3)
)
_SgProxyMemAvailable_Type = Counter64
_SgProxyMemAvailable_Object = MibScalar
sgProxyMemAvailable = _SgProxyMemAvailable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 1),
    _SgProxyMemAvailable_Type()
)
sgProxyMemAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyMemAvailable.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyMemAvailable.setUnits("Bytes")
_SgProxyMemCacheUsage_Type = Counter64
_SgProxyMemCacheUsage_Object = MibScalar
sgProxyMemCacheUsage = _SgProxyMemCacheUsage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 2),
    _SgProxyMemCacheUsage_Type()
)
sgProxyMemCacheUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyMemCacheUsage.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyMemCacheUsage.setUnits("Bytes")
_SgProxyMemSysUsage_Type = Counter64
_SgProxyMemSysUsage_Object = MibScalar
sgProxyMemSysUsage = _SgProxyMemSysUsage_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 3),
    _SgProxyMemSysUsage_Type()
)
sgProxyMemSysUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyMemSysUsage.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyMemSysUsage.setUnits("Bytes")
_SgProxyMemoryPressure_Type = Gauge32
_SgProxyMemoryPressure_Object = MibScalar
sgProxyMemoryPressure = _SgProxyMemoryPressure_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 3, 4),
    _SgProxyMemoryPressure_Type()
)
sgProxyMemoryPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyMemoryPressure.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyMemoryPressure.setUnits("Percentage")
_SgProxyCpuCoreTable_Object = MibTable
sgProxyCpuCoreTable = _SgProxyCpuCoreTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4)
)
if mibBuilder.loadTexts:
    sgProxyCpuCoreTable.setStatus("current")
_SgProxyCpuCoreTableEntry_Object = MibTableRow
sgProxyCpuCoreTableEntry = _SgProxyCpuCoreTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1)
)
sgProxyCpuCoreTableEntry.setIndexNames(
    (0, "BLUECOAT-SG-PROXY-MIB", "sgProxyCpuCoreIndex"),
)
if mibBuilder.loadTexts:
    sgProxyCpuCoreTableEntry.setStatus("current")


class _SgProxyCpuCoreIndex_Type(Integer32):
    """Custom type sgProxyCpuCoreIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_SgProxyCpuCoreIndex_Type.__name__ = "Integer32"
_SgProxyCpuCoreIndex_Object = MibTableColumn
sgProxyCpuCoreIndex = _SgProxyCpuCoreIndex_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 1),
    _SgProxyCpuCoreIndex_Type()
)
sgProxyCpuCoreIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sgProxyCpuCoreIndex.setStatus("current")
_SgProxyCpuCoreUpTime_Type = Counter64
_SgProxyCpuCoreUpTime_Object = MibTableColumn
sgProxyCpuCoreUpTime = _SgProxyCpuCoreUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 2),
    _SgProxyCpuCoreUpTime_Type()
)
sgProxyCpuCoreUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreUpTime.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreUpTime.setUnits("Milliseconds")
_SgProxyCpuCoreBusyTime_Type = Counter64
_SgProxyCpuCoreBusyTime_Object = MibTableColumn
sgProxyCpuCoreBusyTime = _SgProxyCpuCoreBusyTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 3),
    _SgProxyCpuCoreBusyTime_Type()
)
sgProxyCpuCoreBusyTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreBusyTime.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreBusyTime.setUnits("Milliseconds")
_SgProxyCpuCoreIdleTime_Type = Counter64
_SgProxyCpuCoreIdleTime_Object = MibTableColumn
sgProxyCpuCoreIdleTime = _SgProxyCpuCoreIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 4),
    _SgProxyCpuCoreIdleTime_Type()
)
sgProxyCpuCoreIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreIdleTime.setUnits("Milliseconds")
_SgProxyCpuCoreUpTimeSinceLastAccess_Type = Counter64
_SgProxyCpuCoreUpTimeSinceLastAccess_Object = MibTableColumn
sgProxyCpuCoreUpTimeSinceLastAccess = _SgProxyCpuCoreUpTimeSinceLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 5),
    _SgProxyCpuCoreUpTimeSinceLastAccess_Type()
)
sgProxyCpuCoreUpTimeSinceLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreUpTimeSinceLastAccess.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreUpTimeSinceLastAccess.setUnits("Milliseconds")
_SgProxyCpuCoreBusyTimeSinceLastAccess_Type = Counter64
_SgProxyCpuCoreBusyTimeSinceLastAccess_Object = MibTableColumn
sgProxyCpuCoreBusyTimeSinceLastAccess = _SgProxyCpuCoreBusyTimeSinceLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 6),
    _SgProxyCpuCoreBusyTimeSinceLastAccess_Type()
)
sgProxyCpuCoreBusyTimeSinceLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreBusyTimeSinceLastAccess.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreBusyTimeSinceLastAccess.setUnits("Milliseconds")
_SgProxyCpuCoreIdleTimeSinceLastAccess_Type = Counter64
_SgProxyCpuCoreIdleTimeSinceLastAccess_Object = MibTableColumn
sgProxyCpuCoreIdleTimeSinceLastAccess = _SgProxyCpuCoreIdleTimeSinceLastAccess_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 7),
    _SgProxyCpuCoreIdleTimeSinceLastAccess_Type()
)
sgProxyCpuCoreIdleTimeSinceLastAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreIdleTimeSinceLastAccess.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreIdleTimeSinceLastAccess.setUnits("Milliseconds")
_SgProxyCpuCoreBusyPerCent_Type = Gauge32
_SgProxyCpuCoreBusyPerCent_Object = MibTableColumn
sgProxyCpuCoreBusyPerCent = _SgProxyCpuCoreBusyPerCent_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 8),
    _SgProxyCpuCoreBusyPerCent_Type()
)
sgProxyCpuCoreBusyPerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreBusyPerCent.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreBusyPerCent.setUnits("Percentage")
_SgProxyCpuCoreIdlePerCent_Type = Gauge32
_SgProxyCpuCoreIdlePerCent_Object = MibTableColumn
sgProxyCpuCoreIdlePerCent = _SgProxyCpuCoreIdlePerCent_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 2, 4, 1, 9),
    _SgProxyCpuCoreIdlePerCent_Type()
)
sgProxyCpuCoreIdlePerCent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyCpuCoreIdlePerCent.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyCpuCoreIdlePerCent.setUnits("Percentage")
_SgProxyHttp_ObjectIdentity = ObjectIdentity
sgProxyHttp = _SgProxyHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3)
)
_SgProxyHttpPerf_ObjectIdentity = ObjectIdentity
sgProxyHttpPerf = _SgProxyHttpPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1)
)
_SgProxyHttpClient_ObjectIdentity = ObjectIdentity
sgProxyHttpClient = _SgProxyHttpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1)
)
_SgProxyHttpClientRequests_Type = Counter64
_SgProxyHttpClientRequests_Object = MibScalar
sgProxyHttpClientRequests = _SgProxyHttpClientRequests_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 1),
    _SgProxyHttpClientRequests_Type()
)
sgProxyHttpClientRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientRequests.setStatus("current")
_SgProxyHttpClientHits_Type = Counter64
_SgProxyHttpClientHits_Object = MibScalar
sgProxyHttpClientHits = _SgProxyHttpClientHits_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 2),
    _SgProxyHttpClientHits_Type()
)
sgProxyHttpClientHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientHits.setStatus("current")
_SgProxyHttpClientPartialHits_Type = Counter64
_SgProxyHttpClientPartialHits_Object = MibScalar
sgProxyHttpClientPartialHits = _SgProxyHttpClientPartialHits_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 3),
    _SgProxyHttpClientPartialHits_Type()
)
sgProxyHttpClientPartialHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientPartialHits.setStatus("current")
_SgProxyHttpClientMisses_Type = Counter64
_SgProxyHttpClientMisses_Object = MibScalar
sgProxyHttpClientMisses = _SgProxyHttpClientMisses_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 4),
    _SgProxyHttpClientMisses_Type()
)
sgProxyHttpClientMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientMisses.setStatus("current")
_SgProxyHttpClientErrors_Type = Counter64
_SgProxyHttpClientErrors_Object = MibScalar
sgProxyHttpClientErrors = _SgProxyHttpClientErrors_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 5),
    _SgProxyHttpClientErrors_Type()
)
sgProxyHttpClientErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientErrors.setStatus("current")
_SgProxyHttpClientRequestRate_Type = Gauge32
_SgProxyHttpClientRequestRate_Object = MibScalar
sgProxyHttpClientRequestRate = _SgProxyHttpClientRequestRate_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 6),
    _SgProxyHttpClientRequestRate_Type()
)
sgProxyHttpClientRequestRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientRequestRate.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpClientRequestRate.setUnits("Requests Per Second")
_SgProxyHttpClientHitRate_Type = Gauge32
_SgProxyHttpClientHitRate_Object = MibScalar
sgProxyHttpClientHitRate = _SgProxyHttpClientHitRate_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 7),
    _SgProxyHttpClientHitRate_Type()
)
sgProxyHttpClientHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientHitRate.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpClientHitRate.setUnits("Percentage")
_SgProxyHttpClientByteHitRate_Type = Gauge32
_SgProxyHttpClientByteHitRate_Object = MibScalar
sgProxyHttpClientByteHitRate = _SgProxyHttpClientByteHitRate_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 8),
    _SgProxyHttpClientByteHitRate_Type()
)
sgProxyHttpClientByteHitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientByteHitRate.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpClientByteHitRate.setUnits("Percentage")
_SgProxyHttpClientInBytes_Type = Counter64
_SgProxyHttpClientInBytes_Object = MibScalar
sgProxyHttpClientInBytes = _SgProxyHttpClientInBytes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 9),
    _SgProxyHttpClientInBytes_Type()
)
sgProxyHttpClientInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientInBytes.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpClientInBytes.setUnits("Bytes")
_SgProxyHttpClientOutBytes_Type = Counter64
_SgProxyHttpClientOutBytes_Object = MibScalar
sgProxyHttpClientOutBytes = _SgProxyHttpClientOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 1, 10),
    _SgProxyHttpClientOutBytes_Type()
)
sgProxyHttpClientOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpClientOutBytes.setUnits("Bytes")
_SgProxyHttpServer_ObjectIdentity = ObjectIdentity
sgProxyHttpServer = _SgProxyHttpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2)
)
_SgProxyHttpServerRequests_Type = Counter64
_SgProxyHttpServerRequests_Object = MibScalar
sgProxyHttpServerRequests = _SgProxyHttpServerRequests_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 1),
    _SgProxyHttpServerRequests_Type()
)
sgProxyHttpServerRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServerRequests.setStatus("current")
_SgProxyHttpServerErrors_Type = Counter64
_SgProxyHttpServerErrors_Object = MibScalar
sgProxyHttpServerErrors = _SgProxyHttpServerErrors_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 2),
    _SgProxyHttpServerErrors_Type()
)
sgProxyHttpServerErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServerErrors.setStatus("current")
_SgProxyHttpServerInBytes_Type = Counter64
_SgProxyHttpServerInBytes_Object = MibScalar
sgProxyHttpServerInBytes = _SgProxyHttpServerInBytes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 3),
    _SgProxyHttpServerInBytes_Type()
)
sgProxyHttpServerInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServerInBytes.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpServerInBytes.setUnits("Bytes")
_SgProxyHttpServerOutBytes_Type = Counter64
_SgProxyHttpServerOutBytes_Object = MibScalar
sgProxyHttpServerOutBytes = _SgProxyHttpServerOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 2, 4),
    _SgProxyHttpServerOutBytes_Type()
)
sgProxyHttpServerOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServerOutBytes.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpServerOutBytes.setUnits("Bytes")
_SgProxyHttpConnections_ObjectIdentity = ObjectIdentity
sgProxyHttpConnections = _SgProxyHttpConnections_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3)
)
_SgProxyHttpClientConnections_Type = Gauge32
_SgProxyHttpClientConnections_Object = MibScalar
sgProxyHttpClientConnections = _SgProxyHttpClientConnections_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 1),
    _SgProxyHttpClientConnections_Type()
)
sgProxyHttpClientConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientConnections.setStatus("current")
_SgProxyHttpClientConnectionsActive_Type = Gauge32
_SgProxyHttpClientConnectionsActive_Object = MibScalar
sgProxyHttpClientConnectionsActive = _SgProxyHttpClientConnectionsActive_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 2),
    _SgProxyHttpClientConnectionsActive_Type()
)
sgProxyHttpClientConnectionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientConnectionsActive.setStatus("current")
_SgProxyHttpClientConnectionsIdle_Type = Gauge32
_SgProxyHttpClientConnectionsIdle_Object = MibScalar
sgProxyHttpClientConnectionsIdle = _SgProxyHttpClientConnectionsIdle_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 3),
    _SgProxyHttpClientConnectionsIdle_Type()
)
sgProxyHttpClientConnectionsIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpClientConnectionsIdle.setStatus("current")
_SgProxyHttpServerConnections_Type = Gauge32
_SgProxyHttpServerConnections_Object = MibScalar
sgProxyHttpServerConnections = _SgProxyHttpServerConnections_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 4),
    _SgProxyHttpServerConnections_Type()
)
sgProxyHttpServerConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServerConnections.setStatus("current")
_SgProxyHttpServerConnectionsActive_Type = Gauge32
_SgProxyHttpServerConnectionsActive_Object = MibScalar
sgProxyHttpServerConnectionsActive = _SgProxyHttpServerConnectionsActive_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 5),
    _SgProxyHttpServerConnectionsActive_Type()
)
sgProxyHttpServerConnectionsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServerConnectionsActive.setStatus("current")
_SgProxyHttpServerConnectionsIdle_Type = Gauge32
_SgProxyHttpServerConnectionsIdle_Object = MibScalar
sgProxyHttpServerConnectionsIdle = _SgProxyHttpServerConnectionsIdle_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 1, 3, 6),
    _SgProxyHttpServerConnectionsIdle_Type()
)
sgProxyHttpServerConnectionsIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServerConnectionsIdle.setStatus("current")
_SgProxyHttpResponse_ObjectIdentity = ObjectIdentity
sgProxyHttpResponse = _SgProxyHttpResponse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2)
)
_SgProxyHttpResponseTime_ObjectIdentity = ObjectIdentity
sgProxyHttpResponseTime = _SgProxyHttpResponseTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1)
)
_SgProxyHttpServiceTimeAll_Type = Gauge32
_SgProxyHttpServiceTimeAll_Object = MibScalar
sgProxyHttpServiceTimeAll = _SgProxyHttpServiceTimeAll_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 1),
    _SgProxyHttpServiceTimeAll_Type()
)
sgProxyHttpServiceTimeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimeAll.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimeAll.setUnits("Milliseconds")
_SgProxyHttpServiceTimeHit_Type = Gauge32
_SgProxyHttpServiceTimeHit_Object = MibScalar
sgProxyHttpServiceTimeHit = _SgProxyHttpServiceTimeHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 2),
    _SgProxyHttpServiceTimeHit_Type()
)
sgProxyHttpServiceTimeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimeHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimeHit.setUnits("Milliseconds")
_SgProxyHttpServiceTimePartialHit_Type = Gauge32
_SgProxyHttpServiceTimePartialHit_Object = MibScalar
sgProxyHttpServiceTimePartialHit = _SgProxyHttpServiceTimePartialHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 3),
    _SgProxyHttpServiceTimePartialHit_Type()
)
sgProxyHttpServiceTimePartialHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimePartialHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimePartialHit.setUnits("Milliseconds")
_SgProxyHttpServiceTimeMiss_Type = Gauge32
_SgProxyHttpServiceTimeMiss_Object = MibScalar
sgProxyHttpServiceTimeMiss = _SgProxyHttpServiceTimeMiss_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 4),
    _SgProxyHttpServiceTimeMiss_Type()
)
sgProxyHttpServiceTimeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimeMiss.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpServiceTimeMiss.setUnits("Milliseconds")
_SgProxyHttpTotalFetchTimeAll_Type = Counter64
_SgProxyHttpTotalFetchTimeAll_Object = MibScalar
sgProxyHttpTotalFetchTimeAll = _SgProxyHttpTotalFetchTimeAll_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 5),
    _SgProxyHttpTotalFetchTimeAll_Type()
)
sgProxyHttpTotalFetchTimeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimeAll.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimeAll.setUnits("Milliseconds")
_SgProxyHttpTotalFetchTimeHit_Type = Counter64
_SgProxyHttpTotalFetchTimeHit_Object = MibScalar
sgProxyHttpTotalFetchTimeHit = _SgProxyHttpTotalFetchTimeHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 6),
    _SgProxyHttpTotalFetchTimeHit_Type()
)
sgProxyHttpTotalFetchTimeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimeHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimeHit.setUnits("Milliseconds")
_SgProxyHttpTotalFetchTimePartialHit_Type = Counter64
_SgProxyHttpTotalFetchTimePartialHit_Object = MibScalar
sgProxyHttpTotalFetchTimePartialHit = _SgProxyHttpTotalFetchTimePartialHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 7),
    _SgProxyHttpTotalFetchTimePartialHit_Type()
)
sgProxyHttpTotalFetchTimePartialHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimePartialHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimePartialHit.setUnits("Milliseconds")
_SgProxyHttpTotalFetchTimeMiss_Type = Counter64
_SgProxyHttpTotalFetchTimeMiss_Object = MibScalar
sgProxyHttpTotalFetchTimeMiss = _SgProxyHttpTotalFetchTimeMiss_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 1, 8),
    _SgProxyHttpTotalFetchTimeMiss_Type()
)
sgProxyHttpTotalFetchTimeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimeMiss.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpTotalFetchTimeMiss.setUnits("Milliseconds")
_SgProxyHttpResponseFirstByte_ObjectIdentity = ObjectIdentity
sgProxyHttpResponseFirstByte = _SgProxyHttpResponseFirstByte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2)
)
_SgProxyHttpFirstByteAll_Type = Gauge32
_SgProxyHttpFirstByteAll_Object = MibScalar
sgProxyHttpFirstByteAll = _SgProxyHttpFirstByteAll_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 1),
    _SgProxyHttpFirstByteAll_Type()
)
sgProxyHttpFirstByteAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpFirstByteAll.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpFirstByteAll.setUnits("Milliseconds")
_SgProxyHttpFirstByteHit_Type = Gauge32
_SgProxyHttpFirstByteHit_Object = MibScalar
sgProxyHttpFirstByteHit = _SgProxyHttpFirstByteHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 2),
    _SgProxyHttpFirstByteHit_Type()
)
sgProxyHttpFirstByteHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpFirstByteHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpFirstByteHit.setUnits("Milliseconds")
_SgProxyHttpFirstBytePartialHit_Type = Gauge32
_SgProxyHttpFirstBytePartialHit_Object = MibScalar
sgProxyHttpFirstBytePartialHit = _SgProxyHttpFirstBytePartialHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 3),
    _SgProxyHttpFirstBytePartialHit_Type()
)
sgProxyHttpFirstBytePartialHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpFirstBytePartialHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpFirstBytePartialHit.setUnits("Milliseconds")
_SgProxyHttpFirstByteMiss_Type = Gauge32
_SgProxyHttpFirstByteMiss_Object = MibScalar
sgProxyHttpFirstByteMiss = _SgProxyHttpFirstByteMiss_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 2, 4),
    _SgProxyHttpFirstByteMiss_Type()
)
sgProxyHttpFirstByteMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpFirstByteMiss.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpFirstByteMiss.setUnits("Milliseconds")
_SgProxyHttpResponseByteRate_ObjectIdentity = ObjectIdentity
sgProxyHttpResponseByteRate = _SgProxyHttpResponseByteRate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3)
)
_SgProxyHttpByteRateAll_Type = Gauge32
_SgProxyHttpByteRateAll_Object = MibScalar
sgProxyHttpByteRateAll = _SgProxyHttpByteRateAll_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 1),
    _SgProxyHttpByteRateAll_Type()
)
sgProxyHttpByteRateAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpByteRateAll.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpByteRateAll.setUnits("Bytes Per Second")
_SgProxyHttpByteRateHit_Type = Gauge32
_SgProxyHttpByteRateHit_Object = MibScalar
sgProxyHttpByteRateHit = _SgProxyHttpByteRateHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 2),
    _SgProxyHttpByteRateHit_Type()
)
sgProxyHttpByteRateHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpByteRateHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpByteRateHit.setUnits("Bytes Per Second")
_SgProxyHttpByteRatePartialHit_Type = Gauge32
_SgProxyHttpByteRatePartialHit_Object = MibScalar
sgProxyHttpByteRatePartialHit = _SgProxyHttpByteRatePartialHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 3),
    _SgProxyHttpByteRatePartialHit_Type()
)
sgProxyHttpByteRatePartialHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpByteRatePartialHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpByteRatePartialHit.setUnits("Bytes Per Second")
_SgProxyHttpByteRateMiss_Type = Gauge32
_SgProxyHttpByteRateMiss_Object = MibScalar
sgProxyHttpByteRateMiss = _SgProxyHttpByteRateMiss_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 3, 4),
    _SgProxyHttpByteRateMiss_Type()
)
sgProxyHttpByteRateMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpByteRateMiss.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpByteRateMiss.setUnits("Bytes Per Second")
_SgProxyHttpResponseSize_ObjectIdentity = ObjectIdentity
sgProxyHttpResponseSize = _SgProxyHttpResponseSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4)
)
_SgProxyHttpResponseSizeAll_Type = Gauge32
_SgProxyHttpResponseSizeAll_Object = MibScalar
sgProxyHttpResponseSizeAll = _SgProxyHttpResponseSizeAll_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 1),
    _SgProxyHttpResponseSizeAll_Type()
)
sgProxyHttpResponseSizeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizeAll.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizeAll.setUnits("Bytes")
_SgProxyHttpResponseSizeHit_Type = Gauge32
_SgProxyHttpResponseSizeHit_Object = MibScalar
sgProxyHttpResponseSizeHit = _SgProxyHttpResponseSizeHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 2),
    _SgProxyHttpResponseSizeHit_Type()
)
sgProxyHttpResponseSizeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizeHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizeHit.setUnits("Bytes")
_SgProxyHttpResponseSizePartialHit_Type = Gauge32
_SgProxyHttpResponseSizePartialHit_Object = MibScalar
sgProxyHttpResponseSizePartialHit = _SgProxyHttpResponseSizePartialHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 3),
    _SgProxyHttpResponseSizePartialHit_Type()
)
sgProxyHttpResponseSizePartialHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizePartialHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizePartialHit.setUnits("Bytes")
_SgProxyHttpResponseSizeMiss_Type = Gauge32
_SgProxyHttpResponseSizeMiss_Object = MibScalar
sgProxyHttpResponseSizeMiss = _SgProxyHttpResponseSizeMiss_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 2, 4, 4),
    _SgProxyHttpResponseSizeMiss_Type()
)
sgProxyHttpResponseSizeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizeMiss.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpResponseSizeMiss.setUnits("Bytes")
_SgProxyHttpMedian_ObjectIdentity = ObjectIdentity
sgProxyHttpMedian = _SgProxyHttpMedian_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3)
)
_SgProxyHttpMedianServiceTable_Object = MibTable
sgProxyHttpMedianServiceTable = _SgProxyHttpMedianServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTable.setStatus("current")
_SgProxyHttpMedianServiceEntry_Object = MibTableRow
sgProxyHttpMedianServiceEntry = _SgProxyHttpMedianServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1)
)
sgProxyHttpMedianServiceEntry.setIndexNames(
    (0, "BLUECOAT-SG-PROXY-MIB", "sgProxyHttpMedianServiceTime"),
)
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceEntry.setStatus("current")


class _SgProxyHttpMedianServiceTime_Type(Integer32):
    """Custom type sgProxyHttpMedianServiceTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              60)
        )
    )
    namedValues = NamedValues(
        *(("five", 5),
          ("one", 1),
          ("sixty", 60))
    )


_SgProxyHttpMedianServiceTime_Type.__name__ = "Integer32"
_SgProxyHttpMedianServiceTime_Object = MibTableColumn
sgProxyHttpMedianServiceTime = _SgProxyHttpMedianServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 1),
    _SgProxyHttpMedianServiceTime_Type()
)
sgProxyHttpMedianServiceTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTime.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTime.setUnits("Minutes")
_SgProxyHttpMedianServiceTimeAll_Type = Gauge32
_SgProxyHttpMedianServiceTimeAll_Object = MibTableColumn
sgProxyHttpMedianServiceTimeAll = _SgProxyHttpMedianServiceTimeAll_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 2),
    _SgProxyHttpMedianServiceTimeAll_Type()
)
sgProxyHttpMedianServiceTimeAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimeAll.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimeAll.setUnits("Milliseconds")
_SgProxyHttpMedianServiceTimeHit_Type = Gauge32
_SgProxyHttpMedianServiceTimeHit_Object = MibTableColumn
sgProxyHttpMedianServiceTimeHit = _SgProxyHttpMedianServiceTimeHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 3),
    _SgProxyHttpMedianServiceTimeHit_Type()
)
sgProxyHttpMedianServiceTimeHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimeHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimeHit.setUnits("Milliseconds")
_SgProxyHttpMedianServiceTimePartialHit_Type = Gauge32
_SgProxyHttpMedianServiceTimePartialHit_Object = MibTableColumn
sgProxyHttpMedianServiceTimePartialHit = _SgProxyHttpMedianServiceTimePartialHit_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 4),
    _SgProxyHttpMedianServiceTimePartialHit_Type()
)
sgProxyHttpMedianServiceTimePartialHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimePartialHit.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimePartialHit.setUnits("Milliseconds")
_SgProxyHttpMedianServiceTimeMiss_Type = Gauge32
_SgProxyHttpMedianServiceTimeMiss_Object = MibTableColumn
sgProxyHttpMedianServiceTimeMiss = _SgProxyHttpMedianServiceTimeMiss_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 5),
    _SgProxyHttpMedianServiceTimeMiss_Type()
)
sgProxyHttpMedianServiceTimeMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimeMiss.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyHttpMedianServiceTimeMiss.setUnits("Milliseconds")
_SgProxyDnsMedianServiceTime_Type = Gauge32
_SgProxyDnsMedianServiceTime_Object = MibTableColumn
sgProxyDnsMedianServiceTime = _SgProxyDnsMedianServiceTime_Object(
    (1, 3, 6, 1, 4, 1, 3417, 2, 11, 3, 3, 1, 1, 6),
    _SgProxyDnsMedianServiceTime_Type()
)
sgProxyDnsMedianServiceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sgProxyDnsMedianServiceTime.setStatus("current")
if mibBuilder.loadTexts:
    sgProxyDnsMedianServiceTime.setUnits("Milliseconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BLUECOAT-SG-PROXY-MIB",
    **{"bluecoatSGProxyMIB": bluecoatSGProxyMIB,
       "sgProxyConfig": sgProxyConfig,
       "sgProxyAdmin": sgProxyAdmin,
       "sgProxySoftware": sgProxySoftware,
       "sgProxyVersion": sgProxyVersion,
       "sgProxySerialNumber": sgProxySerialNumber,
       "sgProxySystem": sgProxySystem,
       "sgProxyCpu": sgProxyCpu,
       "sgProxyCpuUpTime": sgProxyCpuUpTime,
       "sgProxyCpuBusyTime": sgProxyCpuBusyTime,
       "sgProxyCpuIdleTime": sgProxyCpuIdleTime,
       "sgProxyCpuUpTimeSinceLastAccess": sgProxyCpuUpTimeSinceLastAccess,
       "sgProxyCpuBusyTimeSinceLastAccess": sgProxyCpuBusyTimeSinceLastAccess,
       "sgProxyCpuIdleTimeSinceLastAccess": sgProxyCpuIdleTimeSinceLastAccess,
       "sgProxyCpuBusyPerCent": sgProxyCpuBusyPerCent,
       "sgProxyCpuIdlePerCent": sgProxyCpuIdlePerCent,
       "sgProxyCache": sgProxyCache,
       "sgProxyStorage": sgProxyStorage,
       "sgProxyNumObjects": sgProxyNumObjects,
       "sgProxyMemory": sgProxyMemory,
       "sgProxyMemAvailable": sgProxyMemAvailable,
       "sgProxyMemCacheUsage": sgProxyMemCacheUsage,
       "sgProxyMemSysUsage": sgProxyMemSysUsage,
       "sgProxyMemoryPressure": sgProxyMemoryPressure,
       "sgProxyCpuCoreTable": sgProxyCpuCoreTable,
       "sgProxyCpuCoreTableEntry": sgProxyCpuCoreTableEntry,
       "sgProxyCpuCoreIndex": sgProxyCpuCoreIndex,
       "sgProxyCpuCoreUpTime": sgProxyCpuCoreUpTime,
       "sgProxyCpuCoreBusyTime": sgProxyCpuCoreBusyTime,
       "sgProxyCpuCoreIdleTime": sgProxyCpuCoreIdleTime,
       "sgProxyCpuCoreUpTimeSinceLastAccess": sgProxyCpuCoreUpTimeSinceLastAccess,
       "sgProxyCpuCoreBusyTimeSinceLastAccess": sgProxyCpuCoreBusyTimeSinceLastAccess,
       "sgProxyCpuCoreIdleTimeSinceLastAccess": sgProxyCpuCoreIdleTimeSinceLastAccess,
       "sgProxyCpuCoreBusyPerCent": sgProxyCpuCoreBusyPerCent,
       "sgProxyCpuCoreIdlePerCent": sgProxyCpuCoreIdlePerCent,
       "sgProxyHttp": sgProxyHttp,
       "sgProxyHttpPerf": sgProxyHttpPerf,
       "sgProxyHttpClient": sgProxyHttpClient,
       "sgProxyHttpClientRequests": sgProxyHttpClientRequests,
       "sgProxyHttpClientHits": sgProxyHttpClientHits,
       "sgProxyHttpClientPartialHits": sgProxyHttpClientPartialHits,
       "sgProxyHttpClientMisses": sgProxyHttpClientMisses,
       "sgProxyHttpClientErrors": sgProxyHttpClientErrors,
       "sgProxyHttpClientRequestRate": sgProxyHttpClientRequestRate,
       "sgProxyHttpClientHitRate": sgProxyHttpClientHitRate,
       "sgProxyHttpClientByteHitRate": sgProxyHttpClientByteHitRate,
       "sgProxyHttpClientInBytes": sgProxyHttpClientInBytes,
       "sgProxyHttpClientOutBytes": sgProxyHttpClientOutBytes,
       "sgProxyHttpServer": sgProxyHttpServer,
       "sgProxyHttpServerRequests": sgProxyHttpServerRequests,
       "sgProxyHttpServerErrors": sgProxyHttpServerErrors,
       "sgProxyHttpServerInBytes": sgProxyHttpServerInBytes,
       "sgProxyHttpServerOutBytes": sgProxyHttpServerOutBytes,
       "sgProxyHttpConnections": sgProxyHttpConnections,
       "sgProxyHttpClientConnections": sgProxyHttpClientConnections,
       "sgProxyHttpClientConnectionsActive": sgProxyHttpClientConnectionsActive,
       "sgProxyHttpClientConnectionsIdle": sgProxyHttpClientConnectionsIdle,
       "sgProxyHttpServerConnections": sgProxyHttpServerConnections,
       "sgProxyHttpServerConnectionsActive": sgProxyHttpServerConnectionsActive,
       "sgProxyHttpServerConnectionsIdle": sgProxyHttpServerConnectionsIdle,
       "sgProxyHttpResponse": sgProxyHttpResponse,
       "sgProxyHttpResponseTime": sgProxyHttpResponseTime,
       "sgProxyHttpServiceTimeAll": sgProxyHttpServiceTimeAll,
       "sgProxyHttpServiceTimeHit": sgProxyHttpServiceTimeHit,
       "sgProxyHttpServiceTimePartialHit": sgProxyHttpServiceTimePartialHit,
       "sgProxyHttpServiceTimeMiss": sgProxyHttpServiceTimeMiss,
       "sgProxyHttpTotalFetchTimeAll": sgProxyHttpTotalFetchTimeAll,
       "sgProxyHttpTotalFetchTimeHit": sgProxyHttpTotalFetchTimeHit,
       "sgProxyHttpTotalFetchTimePartialHit": sgProxyHttpTotalFetchTimePartialHit,
       "sgProxyHttpTotalFetchTimeMiss": sgProxyHttpTotalFetchTimeMiss,
       "sgProxyHttpResponseFirstByte": sgProxyHttpResponseFirstByte,
       "sgProxyHttpFirstByteAll": sgProxyHttpFirstByteAll,
       "sgProxyHttpFirstByteHit": sgProxyHttpFirstByteHit,
       "sgProxyHttpFirstBytePartialHit": sgProxyHttpFirstBytePartialHit,
       "sgProxyHttpFirstByteMiss": sgProxyHttpFirstByteMiss,
       "sgProxyHttpResponseByteRate": sgProxyHttpResponseByteRate,
       "sgProxyHttpByteRateAll": sgProxyHttpByteRateAll,
       "sgProxyHttpByteRateHit": sgProxyHttpByteRateHit,
       "sgProxyHttpByteRatePartialHit": sgProxyHttpByteRatePartialHit,
       "sgProxyHttpByteRateMiss": sgProxyHttpByteRateMiss,
       "sgProxyHttpResponseSize": sgProxyHttpResponseSize,
       "sgProxyHttpResponseSizeAll": sgProxyHttpResponseSizeAll,
       "sgProxyHttpResponseSizeHit": sgProxyHttpResponseSizeHit,
       "sgProxyHttpResponseSizePartialHit": sgProxyHttpResponseSizePartialHit,
       "sgProxyHttpResponseSizeMiss": sgProxyHttpResponseSizeMiss,
       "sgProxyHttpMedian": sgProxyHttpMedian,
       "sgProxyHttpMedianServiceTable": sgProxyHttpMedianServiceTable,
       "sgProxyHttpMedianServiceEntry": sgProxyHttpMedianServiceEntry,
       "sgProxyHttpMedianServiceTime": sgProxyHttpMedianServiceTime,
       "sgProxyHttpMedianServiceTimeAll": sgProxyHttpMedianServiceTimeAll,
       "sgProxyHttpMedianServiceTimeHit": sgProxyHttpMedianServiceTimeHit,
       "sgProxyHttpMedianServiceTimePartialHit": sgProxyHttpMedianServiceTimePartialHit,
       "sgProxyHttpMedianServiceTimeMiss": sgProxyHttpMedianServiceTimeMiss,
       "sgProxyDnsMedianServiceTime": sgProxyDnsMedianServiceTime}
)
