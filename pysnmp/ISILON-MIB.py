# SNMP MIB module (ISILON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISILON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:46 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

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

isilon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12124)
)
isilon.setRevisions(
        ("2015-09-23 00:00",
         "2015-04-07 00:00",
         "2010-10-21 00:00",
         "2010-06-29 00:00",
         "2009-12-15 00:00",
         "2009-11-10 00:00",
         "2009-05-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cluster_ObjectIdentity = ObjectIdentity
cluster = _Cluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1)
)
_ClusterStatus_ObjectIdentity = ObjectIdentity
clusterStatus = _ClusterStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1)
)
_ClusterName_Type = DisplayString
_ClusterName_Object = MibScalar
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1, 1),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("current")


class _ClusterHealth_Type(Integer32):
    """Custom type clusterHealth based on Integer32"""
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
        *(("attn", 1),
          ("down", 2),
          ("invalid", 3),
          ("ok", 0))
    )


_ClusterHealth_Type.__name__ = "Integer32"
_ClusterHealth_Object = MibScalar
clusterHealth = _ClusterHealth_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1, 2),
    _ClusterHealth_Type()
)
clusterHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterHealth.setStatus("current")
_ClusterGUID_Type = DisplayString
_ClusterGUID_Object = MibScalar
clusterGUID = _ClusterGUID_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1, 3),
    _ClusterGUID_Type()
)
clusterGUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterGUID.setStatus("current")
_NodeCount_Type = Integer32
_NodeCount_Object = MibScalar
nodeCount = _NodeCount_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1, 4),
    _NodeCount_Type()
)
nodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCount.setStatus("current")
_ConfiguredNodes_Type = DisplayString
_ConfiguredNodes_Object = MibScalar
configuredNodes = _ConfiguredNodes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1, 5),
    _ConfiguredNodes_Type()
)
configuredNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configuredNodes.setStatus("current")
_OnlineNodes_Type = DisplayString
_OnlineNodes_Object = MibScalar
onlineNodes = _OnlineNodes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1, 6),
    _OnlineNodes_Type()
)
onlineNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    onlineNodes.setStatus("current")
_OfflineNodes_Type = DisplayString
_OfflineNodes_Object = MibScalar
offlineNodes = _OfflineNodes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 1, 7),
    _OfflineNodes_Type()
)
offlineNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offlineNodes.setStatus("current")
_ClusterPerformance_ObjectIdentity = ObjectIdentity
clusterPerformance = _ClusterPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2)
)
_ClusterIfsPerf_ObjectIdentity = ObjectIdentity
clusterIfsPerf = _ClusterIfsPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 1)
)
_ClusterIfsInBytes_Type = CounterBasedGauge64
_ClusterIfsInBytes_Object = MibScalar
clusterIfsInBytes = _ClusterIfsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 1, 1),
    _ClusterIfsInBytes_Type()
)
clusterIfsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIfsInBytes.setStatus("current")
_ClusterIfsInBitsPerSecond_Type = CounterBasedGauge64
_ClusterIfsInBitsPerSecond_Object = MibScalar
clusterIfsInBitsPerSecond = _ClusterIfsInBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 1, 2),
    _ClusterIfsInBitsPerSecond_Type()
)
clusterIfsInBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIfsInBitsPerSecond.setStatus("current")
_ClusterIfsOutBytes_Type = CounterBasedGauge64
_ClusterIfsOutBytes_Object = MibScalar
clusterIfsOutBytes = _ClusterIfsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 1, 3),
    _ClusterIfsOutBytes_Type()
)
clusterIfsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIfsOutBytes.setStatus("current")
_ClusterIfsOutBitsPerSecond_Type = CounterBasedGauge64
_ClusterIfsOutBitsPerSecond_Object = MibScalar
clusterIfsOutBitsPerSecond = _ClusterIfsOutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 1, 4),
    _ClusterIfsOutBitsPerSecond_Type()
)
clusterIfsOutBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIfsOutBitsPerSecond.setStatus("current")
_ClusterNetworkPerf_ObjectIdentity = ObjectIdentity
clusterNetworkPerf = _ClusterNetworkPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 2)
)
_ClusterNetworkInBytes_Type = CounterBasedGauge64
_ClusterNetworkInBytes_Object = MibScalar
clusterNetworkInBytes = _ClusterNetworkInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 2, 1),
    _ClusterNetworkInBytes_Type()
)
clusterNetworkInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNetworkInBytes.setStatus("obsolete")
_ClusterNetworkInBitsPerSecond_Type = CounterBasedGauge64
_ClusterNetworkInBitsPerSecond_Object = MibScalar
clusterNetworkInBitsPerSecond = _ClusterNetworkInBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 2, 2),
    _ClusterNetworkInBitsPerSecond_Type()
)
clusterNetworkInBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNetworkInBitsPerSecond.setStatus("current")
_ClusterNetworkOutBytes_Type = CounterBasedGauge64
_ClusterNetworkOutBytes_Object = MibScalar
clusterNetworkOutBytes = _ClusterNetworkOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 2, 3),
    _ClusterNetworkOutBytes_Type()
)
clusterNetworkOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNetworkOutBytes.setStatus("obsolete")
_ClusterNetworkOutBitsPerSecond_Type = CounterBasedGauge64
_ClusterNetworkOutBitsPerSecond_Object = MibScalar
clusterNetworkOutBitsPerSecond = _ClusterNetworkOutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 2, 4),
    _ClusterNetworkOutBitsPerSecond_Type()
)
clusterNetworkOutBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterNetworkOutBitsPerSecond.setStatus("current")
_ClusterCPUPerf_ObjectIdentity = ObjectIdentity
clusterCPUPerf = _ClusterCPUPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 3)
)


class _ClusterCPUUser_Type(Gauge32):
    """Custom type clusterCPUUser based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ClusterCPUUser_Type.__name__ = "Gauge32"
_ClusterCPUUser_Object = MibScalar
clusterCPUUser = _ClusterCPUUser_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 3, 1),
    _ClusterCPUUser_Type()
)
clusterCPUUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCPUUser.setStatus("current")


class _ClusterCPUNice_Type(Gauge32):
    """Custom type clusterCPUNice based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ClusterCPUNice_Type.__name__ = "Gauge32"
_ClusterCPUNice_Object = MibScalar
clusterCPUNice = _ClusterCPUNice_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 3, 2),
    _ClusterCPUNice_Type()
)
clusterCPUNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCPUNice.setStatus("current")


class _ClusterCPUSystem_Type(Gauge32):
    """Custom type clusterCPUSystem based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ClusterCPUSystem_Type.__name__ = "Gauge32"
_ClusterCPUSystem_Object = MibScalar
clusterCPUSystem = _ClusterCPUSystem_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 3, 3),
    _ClusterCPUSystem_Type()
)
clusterCPUSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCPUSystem.setStatus("current")


class _ClusterCPUInterrupt_Type(Gauge32):
    """Custom type clusterCPUInterrupt based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ClusterCPUInterrupt_Type.__name__ = "Gauge32"
_ClusterCPUInterrupt_Object = MibScalar
clusterCPUInterrupt = _ClusterCPUInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 3, 4),
    _ClusterCPUInterrupt_Type()
)
clusterCPUInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCPUInterrupt.setStatus("current")


class _ClusterCPUIdlePct_Type(Gauge32):
    """Custom type clusterCPUIdlePct based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ClusterCPUIdlePct_Type.__name__ = "Gauge32"
_ClusterCPUIdlePct_Object = MibScalar
clusterCPUIdlePct = _ClusterCPUIdlePct_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 2, 3, 5),
    _ClusterCPUIdlePct_Type()
)
clusterCPUIdlePct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCPUIdlePct.setStatus("current")
_IfsFilesystem_ObjectIdentity = ObjectIdentity
ifsFilesystem = _IfsFilesystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 3)
)
_IfsTotalBytes_Type = CounterBasedGauge64
_IfsTotalBytes_Object = MibScalar
ifsTotalBytes = _IfsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 3, 1),
    _IfsTotalBytes_Type()
)
ifsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifsTotalBytes.setStatus("current")
_IfsUsedBytes_Type = CounterBasedGauge64
_IfsUsedBytes_Object = MibScalar
ifsUsedBytes = _IfsUsedBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 3, 2),
    _IfsUsedBytes_Type()
)
ifsUsedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifsUsedBytes.setStatus("current")
_IfsAvailableBytes_Type = CounterBasedGauge64
_IfsAvailableBytes_Object = MibScalar
ifsAvailableBytes = _IfsAvailableBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 3, 3),
    _IfsAvailableBytes_Type()
)
ifsAvailableBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifsAvailableBytes.setStatus("current")
_IfsFreeBytes_Type = CounterBasedGauge64
_IfsFreeBytes_Object = MibScalar
ifsFreeBytes = _IfsFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 3, 4),
    _IfsFreeBytes_Type()
)
ifsFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifsFreeBytes.setStatus("current")


class _AccessTimeEnabled_Type(Integer32):
    """Custom type accessTimeEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AccessTimeEnabled_Type.__name__ = "Integer32"
_AccessTimeEnabled_Object = MibScalar
accessTimeEnabled = _AccessTimeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 3, 10),
    _AccessTimeEnabled_Type()
)
accessTimeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessTimeEnabled.setStatus("current")
_AccessTimeGracePeriod_Type = Gauge32
_AccessTimeGracePeriod_Object = MibScalar
accessTimeGracePeriod = _AccessTimeGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 3, 11),
    _AccessTimeGracePeriod_Type()
)
accessTimeGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    accessTimeGracePeriod.setStatus("current")
_Licenses_ObjectIdentity = ObjectIdentity
licenses = _Licenses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 5)
)
_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 5, 1)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("current")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 5, 1, 1)
)
licenseEntry.setIndexNames(
    (0, "ISILON-MIB", "licenseIndex"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("current")


class _LicenseIndex_Type(Integer32):
    """Custom type licenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_LicenseIndex_Type.__name__ = "Integer32"
_LicenseIndex_Object = MibTableColumn
licenseIndex = _LicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 5, 1, 1, 1),
    _LicenseIndex_Type()
)
licenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseIndex.setStatus("current")
_LicenseModuleName_Type = DisplayString
_LicenseModuleName_Object = MibTableColumn
licenseModuleName = _LicenseModuleName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 5, 1, 1, 2),
    _LicenseModuleName_Type()
)
licenseModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseModuleName.setStatus("current")


class _LicenseStatus_Type(Integer32):
    """Custom type licenseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 0),
          ("evaluation", 1),
          ("expired", -1),
          ("inactive", -2))
    )


_LicenseStatus_Type.__name__ = "Integer32"
_LicenseStatus_Object = MibTableColumn
licenseStatus = _LicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 5, 1, 1, 3),
    _LicenseStatus_Type()
)
licenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseStatus.setStatus("current")
_LicenseExpirationDate_Type = Gauge32
_LicenseExpirationDate_Object = MibTableColumn
licenseExpirationDate = _LicenseExpirationDate_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 5, 1, 1, 5),
    _LicenseExpirationDate_Type()
)
licenseExpirationDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licenseExpirationDate.setStatus("current")
_Quotas_ObjectIdentity = ObjectIdentity
quotas = _Quotas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12)
)
_QuotaTable_Object = MibTable
quotaTable = _QuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1)
)
if mibBuilder.loadTexts:
    quotaTable.setStatus("current")
_QuotaEntry_Object = MibTableRow
quotaEntry = _QuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1)
)
quotaEntry.setIndexNames(
    (0, "ISILON-MIB", "quotaDomainID"),
)
if mibBuilder.loadTexts:
    quotaEntry.setStatus("current")


class _QuotaDomainID_Type(DisplayString):
    """Custom type quotaDomainID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(48, 48),
    )


_QuotaDomainID_Type.__name__ = "DisplayString"
_QuotaDomainID_Object = MibTableColumn
quotaDomainID = _QuotaDomainID_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 1),
    _QuotaDomainID_Type()
)
quotaDomainID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    quotaDomainID.setStatus("current")


class _QuotaType_Type(Integer32):
    """Custom type quotaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("defaultGroup", 2),
          ("defaultUser", 0),
          ("directory", 4),
          ("group", 3),
          ("max", 6),
          ("special", 5),
          ("user", 1))
    )


_QuotaType_Type.__name__ = "Integer32"
_QuotaType_Object = MibTableColumn
quotaType = _QuotaType_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 2),
    _QuotaType_Type()
)
quotaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaType.setStatus("current")
_QuotaID_Type = Gauge32
_QuotaID_Object = MibTableColumn
quotaID = _QuotaID_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 3),
    _QuotaID_Type()
)
quotaID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaID.setStatus("current")


class _QuotaIncludesSnapshotUsage_Type(Integer32):
    """Custom type quotaIncludesSnapshotUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QuotaIncludesSnapshotUsage_Type.__name__ = "Integer32"
_QuotaIncludesSnapshotUsage_Object = MibTableColumn
quotaIncludesSnapshotUsage = _QuotaIncludesSnapshotUsage_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 4),
    _QuotaIncludesSnapshotUsage_Type()
)
quotaIncludesSnapshotUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaIncludesSnapshotUsage.setStatus("current")
_QuotaPath_Type = DisplayString
_QuotaPath_Object = MibTableColumn
quotaPath = _QuotaPath_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 5),
    _QuotaPath_Type()
)
quotaPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaPath.setStatus("current")


class _QuotaHardThresholdDefined_Type(Integer32):
    """Custom type quotaHardThresholdDefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QuotaHardThresholdDefined_Type.__name__ = "Integer32"
_QuotaHardThresholdDefined_Object = MibTableColumn
quotaHardThresholdDefined = _QuotaHardThresholdDefined_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 6),
    _QuotaHardThresholdDefined_Type()
)
quotaHardThresholdDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaHardThresholdDefined.setStatus("current")
_QuotaHardThreshold_Type = CounterBasedGauge64
_QuotaHardThreshold_Object = MibTableColumn
quotaHardThreshold = _QuotaHardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 7),
    _QuotaHardThreshold_Type()
)
quotaHardThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaHardThreshold.setStatus("current")


class _QuotaSoftThresholdDefined_Type(Integer32):
    """Custom type quotaSoftThresholdDefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QuotaSoftThresholdDefined_Type.__name__ = "Integer32"
_QuotaSoftThresholdDefined_Object = MibTableColumn
quotaSoftThresholdDefined = _QuotaSoftThresholdDefined_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 8),
    _QuotaSoftThresholdDefined_Type()
)
quotaSoftThresholdDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaSoftThresholdDefined.setStatus("current")
_QuotaSoftThreshold_Type = CounterBasedGauge64
_QuotaSoftThreshold_Object = MibTableColumn
quotaSoftThreshold = _QuotaSoftThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 9),
    _QuotaSoftThreshold_Type()
)
quotaSoftThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaSoftThreshold.setStatus("current")


class _QuotaAdvisoryThresholdDefined_Type(Integer32):
    """Custom type quotaAdvisoryThresholdDefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QuotaAdvisoryThresholdDefined_Type.__name__ = "Integer32"
_QuotaAdvisoryThresholdDefined_Object = MibTableColumn
quotaAdvisoryThresholdDefined = _QuotaAdvisoryThresholdDefined_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 10),
    _QuotaAdvisoryThresholdDefined_Type()
)
quotaAdvisoryThresholdDefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaAdvisoryThresholdDefined.setStatus("current")
_QuotaAdvisoryThreshold_Type = CounterBasedGauge64
_QuotaAdvisoryThreshold_Object = MibTableColumn
quotaAdvisoryThreshold = _QuotaAdvisoryThreshold_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 11),
    _QuotaAdvisoryThreshold_Type()
)
quotaAdvisoryThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaAdvisoryThreshold.setStatus("current")
_QuotaGracePeriod_Type = Integer32
_QuotaGracePeriod_Object = MibTableColumn
quotaGracePeriod = _QuotaGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 12),
    _QuotaGracePeriod_Type()
)
quotaGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaGracePeriod.setStatus("current")
_QuotaUsage_Type = CounterBasedGauge64
_QuotaUsage_Object = MibTableColumn
quotaUsage = _QuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 13),
    _QuotaUsage_Type()
)
quotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaUsage.setStatus("current")
_QuotaUsageWithOverhead_Type = CounterBasedGauge64
_QuotaUsageWithOverhead_Object = MibTableColumn
quotaUsageWithOverhead = _QuotaUsageWithOverhead_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 14),
    _QuotaUsageWithOverhead_Type()
)
quotaUsageWithOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaUsageWithOverhead.setStatus("current")
_QuotaInodeUsage_Type = CounterBasedGauge64
_QuotaInodeUsage_Object = MibTableColumn
quotaInodeUsage = _QuotaInodeUsage_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 15),
    _QuotaInodeUsage_Type()
)
quotaInodeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaInodeUsage.setStatus("current")


class _QuotaIncludesOverhead_Type(Integer32):
    """Custom type quotaIncludesOverhead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_QuotaIncludesOverhead_Type.__name__ = "Integer32"
_QuotaIncludesOverhead_Object = MibTableColumn
quotaIncludesOverhead = _QuotaIncludesOverhead_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 12, 1, 1, 16),
    _QuotaIncludesOverhead_Type()
)
quotaIncludesOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    quotaIncludesOverhead.setStatus("current")
_Snapshots_ObjectIdentity = ObjectIdentity
snapshots = _Snapshots_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13)
)
_SnapshotSettings_ObjectIdentity = ObjectIdentity
snapshotSettings = _SnapshotSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1)
)


class _SnapshotScheduledCreateEnabled_Type(Integer32):
    """Custom type snapshotScheduledCreateEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotScheduledCreateEnabled_Type.__name__ = "Integer32"
_SnapshotScheduledCreateEnabled_Object = MibScalar
snapshotScheduledCreateEnabled = _SnapshotScheduledCreateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 1),
    _SnapshotScheduledCreateEnabled_Type()
)
snapshotScheduledCreateEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduledCreateEnabled.setStatus("current")


class _SnapshotScheduledDeleteEnabled_Type(Integer32):
    """Custom type snapshotScheduledDeleteEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotScheduledDeleteEnabled_Type.__name__ = "Integer32"
_SnapshotScheduledDeleteEnabled_Object = MibScalar
snapshotScheduledDeleteEnabled = _SnapshotScheduledDeleteEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 2),
    _SnapshotScheduledDeleteEnabled_Type()
)
snapshotScheduledDeleteEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduledDeleteEnabled.setStatus("current")


class _SnapshotReservedPct_Type(Integer32):
    """Custom type snapshotReservedPct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SnapshotReservedPct_Type.__name__ = "Integer32"
_SnapshotReservedPct_Object = MibScalar
snapshotReservedPct = _SnapshotReservedPct_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 3),
    _SnapshotReservedPct_Type()
)
snapshotReservedPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotReservedPct.setStatus("current")


class _SnapshotRootVisibilityNFS_Type(Integer32):
    """Custom type snapshotRootVisibilityNFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotRootVisibilityNFS_Type.__name__ = "Integer32"
_SnapshotRootVisibilityNFS_Object = MibScalar
snapshotRootVisibilityNFS = _SnapshotRootVisibilityNFS_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 4),
    _SnapshotRootVisibilityNFS_Type()
)
snapshotRootVisibilityNFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRootVisibilityNFS.setStatus("current")


class _SnapshotRootAccessNFS_Type(Integer32):
    """Custom type snapshotRootAccessNFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotRootAccessNFS_Type.__name__ = "Integer32"
_SnapshotRootAccessNFS_Object = MibScalar
snapshotRootAccessNFS = _SnapshotRootAccessNFS_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 5),
    _SnapshotRootAccessNFS_Type()
)
snapshotRootAccessNFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRootAccessNFS.setStatus("current")


class _SnapshotSubdirAccessNFS_Type(Integer32):
    """Custom type snapshotSubdirAccessNFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotSubdirAccessNFS_Type.__name__ = "Integer32"
_SnapshotSubdirAccessNFS_Object = MibScalar
snapshotSubdirAccessNFS = _SnapshotSubdirAccessNFS_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 6),
    _SnapshotSubdirAccessNFS_Type()
)
snapshotSubdirAccessNFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSubdirAccessNFS.setStatus("current")


class _SnapshotRootVisibilityCIFS_Type(Integer32):
    """Custom type snapshotRootVisibilityCIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotRootVisibilityCIFS_Type.__name__ = "Integer32"
_SnapshotRootVisibilityCIFS_Object = MibScalar
snapshotRootVisibilityCIFS = _SnapshotRootVisibilityCIFS_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 7),
    _SnapshotRootVisibilityCIFS_Type()
)
snapshotRootVisibilityCIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRootVisibilityCIFS.setStatus("current")


class _SnapshotRootAccessCIFS_Type(Integer32):
    """Custom type snapshotRootAccessCIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotRootAccessCIFS_Type.__name__ = "Integer32"
_SnapshotRootAccessCIFS_Object = MibScalar
snapshotRootAccessCIFS = _SnapshotRootAccessCIFS_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 8),
    _SnapshotRootAccessCIFS_Type()
)
snapshotRootAccessCIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRootAccessCIFS.setStatus("current")


class _SnapshotSubdirAccessCIFS_Type(Integer32):
    """Custom type snapshotSubdirAccessCIFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotSubdirAccessCIFS_Type.__name__ = "Integer32"
_SnapshotSubdirAccessCIFS_Object = MibScalar
snapshotSubdirAccessCIFS = _SnapshotSubdirAccessCIFS_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 9),
    _SnapshotSubdirAccessCIFS_Type()
)
snapshotSubdirAccessCIFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSubdirAccessCIFS.setStatus("current")


class _SnapshotRootVisibilityLocal_Type(Integer32):
    """Custom type snapshotRootVisibilityLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotRootVisibilityLocal_Type.__name__ = "Integer32"
_SnapshotRootVisibilityLocal_Object = MibScalar
snapshotRootVisibilityLocal = _SnapshotRootVisibilityLocal_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 10),
    _SnapshotRootVisibilityLocal_Type()
)
snapshotRootVisibilityLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRootVisibilityLocal.setStatus("current")


class _SnapshotRootAccessLocal_Type(Integer32):
    """Custom type snapshotRootAccessLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotRootAccessLocal_Type.__name__ = "Integer32"
_SnapshotRootAccessLocal_Object = MibScalar
snapshotRootAccessLocal = _SnapshotRootAccessLocal_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 11),
    _SnapshotRootAccessLocal_Type()
)
snapshotRootAccessLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotRootAccessLocal.setStatus("current")


class _SnapshotSubdirAccessLocal_Type(Integer32):
    """Custom type snapshotSubdirAccessLocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotSubdirAccessLocal_Type.__name__ = "Integer32"
_SnapshotSubdirAccessLocal_Object = MibScalar
snapshotSubdirAccessLocal = _SnapshotSubdirAccessLocal_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 1, 12),
    _SnapshotSubdirAccessLocal_Type()
)
snapshotSubdirAccessLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSubdirAccessLocal.setStatus("current")
_SnapshotScheduleTable_Object = MibTable
snapshotScheduleTable = _SnapshotScheduleTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2)
)
if mibBuilder.loadTexts:
    snapshotScheduleTable.setStatus("current")
_SnapshotScheduleEntry_Object = MibTableRow
snapshotScheduleEntry = _SnapshotScheduleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1)
)
snapshotScheduleEntry.setIndexNames(
    (0, "ISILON-MIB", "snapshotScheduleIndex"),
)
if mibBuilder.loadTexts:
    snapshotScheduleEntry.setStatus("current")


class _SnapshotScheduleIndex_Type(Integer32):
    """Custom type snapshotScheduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SnapshotScheduleIndex_Type.__name__ = "Integer32"
_SnapshotScheduleIndex_Object = MibTableColumn
snapshotScheduleIndex = _SnapshotScheduleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1, 1),
    _SnapshotScheduleIndex_Type()
)
snapshotScheduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleIndex.setStatus("current")
_SnapshotScheduleName_Type = DisplayString
_SnapshotScheduleName_Object = MibTableColumn
snapshotScheduleName = _SnapshotScheduleName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1, 2),
    _SnapshotScheduleName_Type()
)
snapshotScheduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleName.setStatus("current")
_SnapshotScheduleAlias_Type = DisplayString
_SnapshotScheduleAlias_Object = MibTableColumn
snapshotScheduleAlias = _SnapshotScheduleAlias_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1, 3),
    _SnapshotScheduleAlias_Type()
)
snapshotScheduleAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleAlias.setStatus("current")
_SnapshotScheduleNamingPattern_Type = DisplayString
_SnapshotScheduleNamingPattern_Object = MibTableColumn
snapshotScheduleNamingPattern = _SnapshotScheduleNamingPattern_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1, 4),
    _SnapshotScheduleNamingPattern_Type()
)
snapshotScheduleNamingPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleNamingPattern.setStatus("current")
_SnapshotScheduleSchedule_Type = DisplayString
_SnapshotScheduleSchedule_Object = MibTableColumn
snapshotScheduleSchedule = _SnapshotScheduleSchedule_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1, 5),
    _SnapshotScheduleSchedule_Type()
)
snapshotScheduleSchedule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleSchedule.setStatus("current")
_SnapshotScheduleExpiration_Type = DisplayString
_SnapshotScheduleExpiration_Object = MibTableColumn
snapshotScheduleExpiration = _SnapshotScheduleExpiration_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1, 6),
    _SnapshotScheduleExpiration_Type()
)
snapshotScheduleExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotScheduleExpiration.setStatus("current")
_SnapshotSchedulePath_Type = DisplayString
_SnapshotSchedulePath_Object = MibTableColumn
snapshotSchedulePath = _SnapshotSchedulePath_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 2, 1, 7),
    _SnapshotSchedulePath_Type()
)
snapshotSchedulePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSchedulePath.setStatus("current")
_SnapshotTable_Object = MibTable
snapshotTable = _SnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3)
)
if mibBuilder.loadTexts:
    snapshotTable.setStatus("current")
_SnapshotEntry_Object = MibTableRow
snapshotEntry = _SnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1)
)
snapshotEntry.setIndexNames(
    (0, "ISILON-MIB", "snapshotIndex"),
)
if mibBuilder.loadTexts:
    snapshotEntry.setStatus("current")


class _SnapshotIndex_Type(Integer32):
    """Custom type snapshotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SnapshotIndex_Type.__name__ = "Integer32"
_SnapshotIndex_Object = MibTableColumn
snapshotIndex = _SnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 1),
    _SnapshotIndex_Type()
)
snapshotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snapshotIndex.setStatus("current")
_SnapshotName_Type = DisplayString
_SnapshotName_Object = MibTableColumn
snapshotName = _SnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 2),
    _SnapshotName_Type()
)
snapshotName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotName.setStatus("current")
_SnapshotCreated_Type = Gauge32
_SnapshotCreated_Object = MibTableColumn
snapshotCreated = _SnapshotCreated_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 3),
    _SnapshotCreated_Type()
)
snapshotCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotCreated.setStatus("current")
_SnapshotExpires_Type = Gauge32
_SnapshotExpires_Object = MibTableColumn
snapshotExpires = _SnapshotExpires_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 4),
    _SnapshotExpires_Type()
)
snapshotExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotExpires.setStatus("current")
_SnapshotSize_Type = CounterBasedGauge64
_SnapshotSize_Object = MibTableColumn
snapshotSize = _SnapshotSize_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 5),
    _SnapshotSize_Type()
)
snapshotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotSize.setStatus("current")
_SnapshotPath_Type = DisplayString
_SnapshotPath_Object = MibTableColumn
snapshotPath = _SnapshotPath_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 6),
    _SnapshotPath_Type()
)
snapshotPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotPath.setStatus("current")
_SnapshotAliasFor_Type = DisplayString
_SnapshotAliasFor_Object = MibTableColumn
snapshotAliasFor = _SnapshotAliasFor_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 7),
    _SnapshotAliasFor_Type()
)
snapshotAliasFor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotAliasFor.setStatus("current")


class _SnapshotLocked_Type(Integer32):
    """Custom type snapshotLocked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SnapshotLocked_Type.__name__ = "Integer32"
_SnapshotLocked_Object = MibTableColumn
snapshotLocked = _SnapshotLocked_Object(
    (1, 3, 6, 1, 4, 1, 12124, 1, 13, 3, 1, 8),
    _SnapshotLocked_Type()
)
snapshotLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snapshotLocked.setStatus("current")
_Node_ObjectIdentity = ObjectIdentity
node = _Node_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 2)
)
_NodeStatus_ObjectIdentity = ObjectIdentity
nodeStatus = _NodeStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 2, 1)
)
_NodeName_Type = DisplayString
_NodeName_Object = MibScalar
nodeName = _NodeName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 1, 1),
    _NodeName_Type()
)
nodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeName.setStatus("current")


class _NodeHealth_Type(Integer32):
    """Custom type nodeHealth based on Integer32"""
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
        *(("attn", 1),
          ("down", 2),
          ("invalid", 3),
          ("ok", 0))
    )


_NodeHealth_Type.__name__ = "Integer32"
_NodeHealth_Object = MibScalar
nodeHealth = _NodeHealth_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 1, 2),
    _NodeHealth_Type()
)
nodeHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeHealth.setStatus("current")


class _NodeType_Type(Integer32):
    """Custom type nodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("accelerator", 1),
          ("storage", 0))
    )


_NodeType_Type.__name__ = "Integer32"
_NodeType_Object = MibScalar
nodeType = _NodeType_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 1, 3),
    _NodeType_Type()
)
nodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeType.setStatus("current")


class _ReadOnly_Type(Integer32):
    """Custom type readOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_ReadOnly_Type.__name__ = "Integer32"
_ReadOnly_Object = MibScalar
readOnly = _ReadOnly_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 1, 4),
    _ReadOnly_Type()
)
readOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    readOnly.setStatus("current")
_NodePerformance_ObjectIdentity = ObjectIdentity
nodePerformance = _NodePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2)
)
_NodeIfsPerf_ObjectIdentity = ObjectIdentity
nodeIfsPerf = _NodeIfsPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 1)
)
_NodeIfsInBytes_Type = CounterBasedGauge64
_NodeIfsInBytes_Object = MibScalar
nodeIfsInBytes = _NodeIfsInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 1, 1),
    _NodeIfsInBytes_Type()
)
nodeIfsInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfsInBytes.setStatus("current")
_NodeIfsInBitsPerSecond_Type = CounterBasedGauge64
_NodeIfsInBitsPerSecond_Object = MibScalar
nodeIfsInBitsPerSecond = _NodeIfsInBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 1, 2),
    _NodeIfsInBitsPerSecond_Type()
)
nodeIfsInBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfsInBitsPerSecond.setStatus("current")
_NodeIfsOutBytes_Type = CounterBasedGauge64
_NodeIfsOutBytes_Object = MibScalar
nodeIfsOutBytes = _NodeIfsOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 1, 3),
    _NodeIfsOutBytes_Type()
)
nodeIfsOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfsOutBytes.setStatus("current")
_NodeIfsOutBitsPerSecond_Type = CounterBasedGauge64
_NodeIfsOutBitsPerSecond_Object = MibScalar
nodeIfsOutBitsPerSecond = _NodeIfsOutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 1, 4),
    _NodeIfsOutBitsPerSecond_Type()
)
nodeIfsOutBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeIfsOutBitsPerSecond.setStatus("current")
_NodeNetworkPerf_ObjectIdentity = ObjectIdentity
nodeNetworkPerf = _NodeNetworkPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 2)
)
_NodeNetworkInBytes_Type = CounterBasedGauge64
_NodeNetworkInBytes_Object = MibScalar
nodeNetworkInBytes = _NodeNetworkInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 2, 1),
    _NodeNetworkInBytes_Type()
)
nodeNetworkInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNetworkInBytes.setStatus("obsolete")
_NodeNetworkInBitsPerSecond_Type = CounterBasedGauge64
_NodeNetworkInBitsPerSecond_Object = MibScalar
nodeNetworkInBitsPerSecond = _NodeNetworkInBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 2, 2),
    _NodeNetworkInBitsPerSecond_Type()
)
nodeNetworkInBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNetworkInBitsPerSecond.setStatus("current")
_NodeNetworkOutBytes_Type = CounterBasedGauge64
_NodeNetworkOutBytes_Object = MibScalar
nodeNetworkOutBytes = _NodeNetworkOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 2, 3),
    _NodeNetworkOutBytes_Type()
)
nodeNetworkOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNetworkOutBytes.setStatus("obsolete")
_NodeNetworkOutBitsPerSecond_Type = CounterBasedGauge64
_NodeNetworkOutBitsPerSecond_Object = MibScalar
nodeNetworkOutBitsPerSecond = _NodeNetworkOutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 2, 4),
    _NodeNetworkOutBitsPerSecond_Type()
)
nodeNetworkOutBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeNetworkOutBitsPerSecond.setStatus("current")
_NodeCPUPerf_ObjectIdentity = ObjectIdentity
nodeCPUPerf = _NodeCPUPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3)
)


class _NodeCPUUser_Type(Gauge32):
    """Custom type nodeCPUUser based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodeCPUUser_Type.__name__ = "Gauge32"
_NodeCPUUser_Object = MibScalar
nodeCPUUser = _NodeCPUUser_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 1),
    _NodeCPUUser_Type()
)
nodeCPUUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCPUUser.setStatus("current")


class _NodeCPUNice_Type(Gauge32):
    """Custom type nodeCPUNice based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodeCPUNice_Type.__name__ = "Gauge32"
_NodeCPUNice_Object = MibScalar
nodeCPUNice = _NodeCPUNice_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 2),
    _NodeCPUNice_Type()
)
nodeCPUNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCPUNice.setStatus("current")


class _NodeCPUSystem_Type(Gauge32):
    """Custom type nodeCPUSystem based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodeCPUSystem_Type.__name__ = "Gauge32"
_NodeCPUSystem_Object = MibScalar
nodeCPUSystem = _NodeCPUSystem_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 3),
    _NodeCPUSystem_Type()
)
nodeCPUSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCPUSystem.setStatus("current")


class _NodeCPUInterrupt_Type(Gauge32):
    """Custom type nodeCPUInterrupt based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodeCPUInterrupt_Type.__name__ = "Gauge32"
_NodeCPUInterrupt_Object = MibScalar
nodeCPUInterrupt = _NodeCPUInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 4),
    _NodeCPUInterrupt_Type()
)
nodeCPUInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCPUInterrupt.setStatus("current")


class _NodeCPUIdle_Type(Gauge32):
    """Custom type nodeCPUIdle based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodeCPUIdle_Type.__name__ = "Gauge32"
_NodeCPUIdle_Object = MibScalar
nodeCPUIdle = _NodeCPUIdle_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 5),
    _NodeCPUIdle_Type()
)
nodeCPUIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeCPUIdle.setStatus("current")
_NodeCPUPerfTable_Object = MibTable
nodeCPUPerfTable = _NodeCPUPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10)
)
if mibBuilder.loadTexts:
    nodeCPUPerfTable.setStatus("current")
_NodeCPUPerfEntry_Object = MibTableRow
nodeCPUPerfEntry = _NodeCPUPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10, 1)
)
nodeCPUPerfEntry.setIndexNames(
    (0, "ISILON-MIB", "nodePerCPUID"),
)
if mibBuilder.loadTexts:
    nodeCPUPerfEntry.setStatus("current")


class _NodePerCPUUser_Type(Gauge32):
    """Custom type nodePerCPUUser based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodePerCPUUser_Type.__name__ = "Gauge32"
_NodePerCPUUser_Object = MibTableColumn
nodePerCPUUser = _NodePerCPUUser_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10, 1, 1),
    _NodePerCPUUser_Type()
)
nodePerCPUUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePerCPUUser.setStatus("current")


class _NodePerCPUNice_Type(Gauge32):
    """Custom type nodePerCPUNice based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodePerCPUNice_Type.__name__ = "Gauge32"
_NodePerCPUNice_Object = MibTableColumn
nodePerCPUNice = _NodePerCPUNice_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10, 1, 2),
    _NodePerCPUNice_Type()
)
nodePerCPUNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePerCPUNice.setStatus("current")


class _NodePerCPUSystem_Type(Gauge32):
    """Custom type nodePerCPUSystem based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodePerCPUSystem_Type.__name__ = "Gauge32"
_NodePerCPUSystem_Object = MibTableColumn
nodePerCPUSystem = _NodePerCPUSystem_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10, 1, 3),
    _NodePerCPUSystem_Type()
)
nodePerCPUSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePerCPUSystem.setStatus("current")


class _NodePerCPUInterrupt_Type(Gauge32):
    """Custom type nodePerCPUInterrupt based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodePerCPUInterrupt_Type.__name__ = "Gauge32"
_NodePerCPUInterrupt_Object = MibTableColumn
nodePerCPUInterrupt = _NodePerCPUInterrupt_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10, 1, 4),
    _NodePerCPUInterrupt_Type()
)
nodePerCPUInterrupt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePerCPUInterrupt.setStatus("current")


class _NodePerCPUIdle_Type(Gauge32):
    """Custom type nodePerCPUIdle based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NodePerCPUIdle_Type.__name__ = "Gauge32"
_NodePerCPUIdle_Object = MibTableColumn
nodePerCPUIdle = _NodePerCPUIdle_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10, 1, 5),
    _NodePerCPUIdle_Type()
)
nodePerCPUIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePerCPUIdle.setStatus("current")


class _NodePerCPUID_Type(Integer32):
    """Custom type nodePerCPUID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_NodePerCPUID_Type.__name__ = "Integer32"
_NodePerCPUID_Object = MibTableColumn
nodePerCPUID = _NodePerCPUID_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 3, 10, 1, 6),
    _NodePerCPUID_Type()
)
nodePerCPUID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nodePerCPUID.setStatus("current")
_NodeProtocolPerfTable_Object = MibTable
nodeProtocolPerfTable = _NodeProtocolPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10)
)
if mibBuilder.loadTexts:
    nodeProtocolPerfTable.setStatus("current")
_NodeProtocolPerfEntry_Object = MibTableRow
nodeProtocolPerfEntry = _NodeProtocolPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1)
)
nodeProtocolPerfEntry.setIndexNames(
    (1, "ISILON-MIB", "protocolName"),
)
if mibBuilder.loadTexts:
    nodeProtocolPerfEntry.setStatus("current")


class _ProtocolName_Type(DisplayString):
    """Custom type protocolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 4),
    )


_ProtocolName_Type.__name__ = "DisplayString"
_ProtocolName_Object = MibTableColumn
protocolName = _ProtocolName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 1),
    _ProtocolName_Type()
)
protocolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolName.setStatus("current")
_ProtocolOpCount_Type = Gauge32
_ProtocolOpCount_Object = MibTableColumn
protocolOpCount = _ProtocolOpCount_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 2),
    _ProtocolOpCount_Type()
)
protocolOpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolOpCount.setStatus("current")
_ProtocolOpsPerSecond_Type = Gauge32
_ProtocolOpsPerSecond_Object = MibTableColumn
protocolOpsPerSecond = _ProtocolOpsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 3),
    _ProtocolOpsPerSecond_Type()
)
protocolOpsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolOpsPerSecond.setStatus("current")
_InMinBytes_Type = Gauge32
_InMinBytes_Object = MibTableColumn
inMinBytes = _InMinBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 4),
    _InMinBytes_Type()
)
inMinBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inMinBytes.setStatus("current")
_InMaxBytes_Type = Gauge32
_InMaxBytes_Object = MibTableColumn
inMaxBytes = _InMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 5),
    _InMaxBytes_Type()
)
inMaxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inMaxBytes.setStatus("current")
_InAvgBytes_Type = Gauge32
_InAvgBytes_Object = MibTableColumn
inAvgBytes = _InAvgBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 6),
    _InAvgBytes_Type()
)
inAvgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inAvgBytes.setStatus("current")
_InStdDevBytes_Type = Gauge32
_InStdDevBytes_Object = MibTableColumn
inStdDevBytes = _InStdDevBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 7),
    _InStdDevBytes_Type()
)
inStdDevBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inStdDevBytes.setStatus("current")
_InBitsPerSecond_Type = CounterBasedGauge64
_InBitsPerSecond_Object = MibTableColumn
inBitsPerSecond = _InBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 8),
    _InBitsPerSecond_Type()
)
inBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBitsPerSecond.setStatus("current")
_OutMinBytes_Type = Gauge32
_OutMinBytes_Object = MibTableColumn
outMinBytes = _OutMinBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 9),
    _OutMinBytes_Type()
)
outMinBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outMinBytes.setStatus("current")
_OutMaxBytes_Type = Gauge32
_OutMaxBytes_Object = MibTableColumn
outMaxBytes = _OutMaxBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 10),
    _OutMaxBytes_Type()
)
outMaxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outMaxBytes.setStatus("current")
_OutAvgBytes_Type = Gauge32
_OutAvgBytes_Object = MibTableColumn
outAvgBytes = _OutAvgBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 11),
    _OutAvgBytes_Type()
)
outAvgBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outAvgBytes.setStatus("current")
_OutStdDevBytes_Type = Gauge32
_OutStdDevBytes_Object = MibTableColumn
outStdDevBytes = _OutStdDevBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 12),
    _OutStdDevBytes_Type()
)
outStdDevBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outStdDevBytes.setStatus("current")
_OutBitsPerSecond_Type = CounterBasedGauge64
_OutBitsPerSecond_Object = MibTableColumn
outBitsPerSecond = _OutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 13),
    _OutBitsPerSecond_Type()
)
outBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBitsPerSecond.setStatus("current")
_LatencyMin_Type = Gauge32
_LatencyMin_Object = MibTableColumn
latencyMin = _LatencyMin_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 14),
    _LatencyMin_Type()
)
latencyMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latencyMin.setStatus("current")
_LatencyMax_Type = Gauge32
_LatencyMax_Object = MibTableColumn
latencyMax = _LatencyMax_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 15),
    _LatencyMax_Type()
)
latencyMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latencyMax.setStatus("current")
_LatencyAverage_Type = Gauge32
_LatencyAverage_Object = MibTableColumn
latencyAverage = _LatencyAverage_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 16),
    _LatencyAverage_Type()
)
latencyAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latencyAverage.setStatus("current")
_LatencyStdDev_Type = Gauge32
_LatencyStdDev_Object = MibTableColumn
latencyStdDev = _LatencyStdDev_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 10, 1, 17),
    _LatencyStdDev_Type()
)
latencyStdDev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latencyStdDev.setStatus("current")
_DiskPerfTable_Object = MibTable
diskPerfTable = _DiskPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 52)
)
if mibBuilder.loadTexts:
    diskPerfTable.setStatus("current")
_DiskPerfEntry_Object = MibTableRow
diskPerfEntry = _DiskPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 52, 1)
)
diskPerfEntry.setIndexNames(
    (0, "ISILON-MIB", "diskPerfBay"),
)
if mibBuilder.loadTexts:
    diskPerfEntry.setStatus("current")


class _DiskPerfBay_Type(Integer32):
    """Custom type diskPerfBay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DiskPerfBay_Type.__name__ = "Integer32"
_DiskPerfBay_Object = MibTableColumn
diskPerfBay = _DiskPerfBay_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 52, 1, 1),
    _DiskPerfBay_Type()
)
diskPerfBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfBay.setStatus("current")
_DiskPerfDeviceName_Type = DisplayString
_DiskPerfDeviceName_Object = MibTableColumn
diskPerfDeviceName = _DiskPerfDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 52, 1, 2),
    _DiskPerfDeviceName_Type()
)
diskPerfDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfDeviceName.setStatus("current")
_DiskPerfOpsPerSecond_Type = Gauge32
_DiskPerfOpsPerSecond_Object = MibTableColumn
diskPerfOpsPerSecond = _DiskPerfOpsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 52, 1, 3),
    _DiskPerfOpsPerSecond_Type()
)
diskPerfOpsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfOpsPerSecond.setStatus("current")
_DiskPerfInBitsPerSecond_Type = Gauge32
_DiskPerfInBitsPerSecond_Object = MibTableColumn
diskPerfInBitsPerSecond = _DiskPerfInBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 52, 1, 4),
    _DiskPerfInBitsPerSecond_Type()
)
diskPerfInBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfInBitsPerSecond.setStatus("current")
_DiskPerfOutBitsPerSecond_Type = Gauge32
_DiskPerfOutBitsPerSecond_Object = MibTableColumn
diskPerfOutBitsPerSecond = _DiskPerfOutBitsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 2, 52, 1, 5),
    _DiskPerfOutBitsPerSecond_Type()
)
diskPerfOutBitsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskPerfOutBitsPerSecond.setStatus("current")
_ChassisTable_Object = MibTable
chassisTable = _ChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 51)
)
if mibBuilder.loadTexts:
    chassisTable.setStatus("current")
_ChassisEntry_Object = MibTableRow
chassisEntry = _ChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 51, 1)
)
chassisEntry.setIndexNames(
    (0, "ISILON-MIB", "chassisNumber"),
)
if mibBuilder.loadTexts:
    chassisEntry.setStatus("current")


class _ChassisNumber_Type(Integer32):
    """Custom type chassisNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ChassisNumber_Type.__name__ = "Integer32"
_ChassisNumber_Object = MibTableColumn
chassisNumber = _ChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 51, 1, 1),
    _ChassisNumber_Type()
)
chassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNumber.setStatus("current")
_ChassisConfigNumber_Type = DisplayString
_ChassisConfigNumber_Object = MibTableColumn
chassisConfigNumber = _ChassisConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 51, 1, 2),
    _ChassisConfigNumber_Type()
)
chassisConfigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisConfigNumber.setStatus("current")
_ChassisSerialNumber_Type = DisplayString
_ChassisSerialNumber_Object = MibTableColumn
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 51, 1, 3),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("current")
_ChassisModel_Type = DisplayString
_ChassisModel_Object = MibTableColumn
chassisModel = _ChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 51, 1, 4),
    _ChassisModel_Type()
)
chassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModel.setStatus("current")


class _ChassisUnitIDLEDOn_Type(Integer32):
    """Custom type chassisUnitIDLEDOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("no", 0),
          ("yes", 1))
    )


_ChassisUnitIDLEDOn_Type.__name__ = "Integer32"
_ChassisUnitIDLEDOn_Object = MibTableColumn
chassisUnitIDLEDOn = _ChassisUnitIDLEDOn_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 51, 1, 5),
    _ChassisUnitIDLEDOn_Type()
)
chassisUnitIDLEDOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisUnitIDLEDOn.setStatus("current")
_DiskTable_Object = MibTable
diskTable = _DiskTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52)
)
if mibBuilder.loadTexts:
    diskTable.setStatus("current")
_DiskEntry_Object = MibTableRow
diskEntry = _DiskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1)
)
diskEntry.setIndexNames(
    (0, "ISILON-MIB", "diskBay"),
)
if mibBuilder.loadTexts:
    diskEntry.setStatus("current")


class _DiskBay_Type(Integer32):
    """Custom type diskBay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_DiskBay_Type.__name__ = "Integer32"
_DiskBay_Object = MibTableColumn
diskBay = _DiskBay_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 1),
    _DiskBay_Type()
)
diskBay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskBay.setStatus("current")


class _DiskLogicalNumber_Type(Integer32):
    """Custom type diskLogicalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DiskLogicalNumber_Type.__name__ = "Integer32"
_DiskLogicalNumber_Object = MibTableColumn
diskLogicalNumber = _DiskLogicalNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 2),
    _DiskLogicalNumber_Type()
)
diskLogicalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskLogicalNumber.setStatus("current")
_DiskChassisNumber_Type = Integer32
_DiskChassisNumber_Object = MibTableColumn
diskChassisNumber = _DiskChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 3),
    _DiskChassisNumber_Type()
)
diskChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskChassisNumber.setStatus("current")
_DiskDeviceName_Type = DisplayString
_DiskDeviceName_Object = MibTableColumn
diskDeviceName = _DiskDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 4),
    _DiskDeviceName_Type()
)
diskDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskDeviceName.setStatus("current")
_DiskStatus_Type = DisplayString
_DiskStatus_Object = MibTableColumn
diskStatus = _DiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 5),
    _DiskStatus_Type()
)
diskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskStatus.setStatus("current")
_DiskModel_Type = DisplayString
_DiskModel_Object = MibTableColumn
diskModel = _DiskModel_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 6),
    _DiskModel_Type()
)
diskModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskModel.setStatus("current")
_DiskSerialNumber_Type = DisplayString
_DiskSerialNumber_Object = MibTableColumn
diskSerialNumber = _DiskSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 7),
    _DiskSerialNumber_Type()
)
diskSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSerialNumber.setStatus("current")
_DiskFirmwareVersion_Type = DisplayString
_DiskFirmwareVersion_Object = MibTableColumn
diskFirmwareVersion = _DiskFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 8),
    _DiskFirmwareVersion_Type()
)
diskFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskFirmwareVersion.setStatus("current")
_DiskSizeBytes_Type = CounterBasedGauge64
_DiskSizeBytes_Object = MibTableColumn
diskSizeBytes = _DiskSizeBytes_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 52, 1, 9),
    _DiskSizeBytes_Type()
)
diskSizeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskSizeBytes.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 53)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 53, 1)
)
fanEntry.setIndexNames(
    (0, "ISILON-MIB", "fanNumber"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanNumber_Type(Integer32):
    """Custom type fanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FanNumber_Type.__name__ = "Integer32"
_FanNumber_Object = MibTableColumn
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 53, 1, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("current")
_FanName_Type = DisplayString
_FanName_Object = MibTableColumn
fanName = _FanName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 53, 1, 2),
    _FanName_Type()
)
fanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanName.setStatus("current")
_FanDescription_Type = DisplayString
_FanDescription_Object = MibTableColumn
fanDescription = _FanDescription_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 53, 1, 3),
    _FanDescription_Type()
)
fanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanDescription.setStatus("current")


class _FanSpeed_Type(Integer32):
    """Custom type fanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_FanSpeed_Type.__name__ = "Integer32"
_FanSpeed_Object = MibTableColumn
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 53, 1, 4),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("current")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 54)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 54, 1)
)
tempSensorEntry.setIndexNames(
    (0, "ISILON-MIB", "tempSensorNumber"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorNumber_Type(Integer32):
    """Custom type tempSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_TempSensorNumber_Type.__name__ = "Integer32"
_TempSensorNumber_Object = MibTableColumn
tempSensorNumber = _TempSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 54, 1, 1),
    _TempSensorNumber_Type()
)
tempSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorNumber.setStatus("current")
_TempSensorName_Type = DisplayString
_TempSensorName_Object = MibTableColumn
tempSensorName = _TempSensorName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 54, 1, 2),
    _TempSensorName_Type()
)
tempSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorName.setStatus("current")
_TempSensorDescription_Type = DisplayString
_TempSensorDescription_Object = MibTableColumn
tempSensorDescription = _TempSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 54, 1, 3),
    _TempSensorDescription_Type()
)
tempSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorDescription.setStatus("current")
_TempSensorValue_Type = DisplayString
_TempSensorValue_Object = MibTableColumn
tempSensorValue = _TempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 54, 1, 4),
    _TempSensorValue_Type()
)
tempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValue.setStatus("current")
_PowerSensorTable_Object = MibTable
powerSensorTable = _PowerSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 55)
)
if mibBuilder.loadTexts:
    powerSensorTable.setStatus("current")
_PowerSensorEntry_Object = MibTableRow
powerSensorEntry = _PowerSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 55, 1)
)
powerSensorEntry.setIndexNames(
    (0, "ISILON-MIB", "powerSensorNumber"),
)
if mibBuilder.loadTexts:
    powerSensorEntry.setStatus("current")


class _PowerSensorNumber_Type(Integer32):
    """Custom type powerSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_PowerSensorNumber_Type.__name__ = "Integer32"
_PowerSensorNumber_Object = MibTableColumn
powerSensorNumber = _PowerSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 55, 1, 1),
    _PowerSensorNumber_Type()
)
powerSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSensorNumber.setStatus("current")
_PowerSensorName_Type = DisplayString
_PowerSensorName_Object = MibTableColumn
powerSensorName = _PowerSensorName_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 55, 1, 2),
    _PowerSensorName_Type()
)
powerSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSensorName.setStatus("current")
_PowerSensorDescription_Type = DisplayString
_PowerSensorDescription_Object = MibTableColumn
powerSensorDescription = _PowerSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 55, 1, 3),
    _PowerSensorDescription_Type()
)
powerSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSensorDescription.setStatus("current")
_PowerSensorValue_Type = DisplayString
_PowerSensorValue_Object = MibTableColumn
powerSensorValue = _PowerSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 12124, 2, 55, 1, 4),
    _PowerSensorValue_Type()
)
powerSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSensorValue.setStatus("current")
_Local_ObjectIdentity = ObjectIdentity
local = _Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 4)
)
_CredentialBindings_ObjectIdentity = ObjectIdentity
credentialBindings = _CredentialBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 4, 1)
)
_Conformance_ObjectIdentity = ObjectIdentity
conformance = _Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 5)
)
_ClusterGroups_ObjectIdentity = ObjectIdentity
clusterGroups = _ClusterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1)
)
_ClusterPerformanceGroups_ObjectIdentity = ObjectIdentity
clusterPerformanceGroups = _ClusterPerformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 2)
)
_SnapshotsGroup_ObjectIdentity = ObjectIdentity
snapshotsGroup = _SnapshotsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 13)
)
_NodeGroups_ObjectIdentity = ObjectIdentity
nodeGroups = _NodeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2)
)
_NodePerformanceGroup_ObjectIdentity = ObjectIdentity
nodePerformanceGroup = _NodePerformanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 2)
)

# Managed Objects groups

clusterStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 1)
)
clusterStatusGroup.setObjects(
      *(("ISILON-MIB", "clusterName"),
        ("ISILON-MIB", "clusterHealth"),
        ("ISILON-MIB", "clusterGUID"),
        ("ISILON-MIB", "nodeCount"),
        ("ISILON-MIB", "configuredNodes"),
        ("ISILON-MIB", "onlineNodes"),
        ("ISILON-MIB", "offlineNodes"))
)
if mibBuilder.loadTexts:
    clusterStatusGroup.setStatus("current")

clusterIfsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 2, 1)
)
clusterIfsPerfGroup.setObjects(
      *(("ISILON-MIB", "clusterIfsInBytes"),
        ("ISILON-MIB", "clusterIfsInBitsPerSecond"),
        ("ISILON-MIB", "clusterIfsOutBytes"),
        ("ISILON-MIB", "clusterIfsOutBitsPerSecond"))
)
if mibBuilder.loadTexts:
    clusterIfsPerfGroup.setStatus("current")

clusterNetworkPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 2, 2)
)
clusterNetworkPerfGroup.setObjects(
      *(("ISILON-MIB", "clusterNetworkInBytes"),
        ("ISILON-MIB", "clusterNetworkInBitsPerSecond"),
        ("ISILON-MIB", "clusterNetworkOutBytes"),
        ("ISILON-MIB", "clusterNetworkOutBitsPerSecond"))
)
if mibBuilder.loadTexts:
    clusterNetworkPerfGroup.setStatus("current")

clusterCPUPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 2, 3)
)
clusterCPUPerfGroup.setObjects(
      *(("ISILON-MIB", "clusterCPUUser"),
        ("ISILON-MIB", "clusterCPUNice"),
        ("ISILON-MIB", "clusterCPUSystem"),
        ("ISILON-MIB", "clusterCPUInterrupt"),
        ("ISILON-MIB", "clusterCPUIdlePct"))
)
if mibBuilder.loadTexts:
    clusterCPUPerfGroup.setStatus("current")

ifsFilesystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 3)
)
ifsFilesystemGroup.setObjects(
      *(("ISILON-MIB", "ifsTotalBytes"),
        ("ISILON-MIB", "ifsUsedBytes"),
        ("ISILON-MIB", "ifsAvailableBytes"),
        ("ISILON-MIB", "ifsFreeBytes"),
        ("ISILON-MIB", "accessTimeEnabled"),
        ("ISILON-MIB", "accessTimeGracePeriod"))
)
if mibBuilder.loadTexts:
    ifsFilesystemGroup.setStatus("current")

licensesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 5)
)
licensesGroup.setObjects(
      *(("ISILON-MIB", "licenseModuleName"),
        ("ISILON-MIB", "licenseStatus"),
        ("ISILON-MIB", "licenseExpirationDate"))
)
if mibBuilder.loadTexts:
    licensesGroup.setStatus("current")

quotasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 12)
)
quotasGroup.setObjects(
      *(("ISILON-MIB", "quotaType"),
        ("ISILON-MIB", "quotaID"),
        ("ISILON-MIB", "quotaIncludesSnapshotUsage"),
        ("ISILON-MIB", "quotaPath"),
        ("ISILON-MIB", "quotaHardThresholdDefined"),
        ("ISILON-MIB", "quotaHardThreshold"),
        ("ISILON-MIB", "quotaSoftThresholdDefined"),
        ("ISILON-MIB", "quotaSoftThreshold"),
        ("ISILON-MIB", "quotaAdvisoryThresholdDefined"),
        ("ISILON-MIB", "quotaAdvisoryThreshold"),
        ("ISILON-MIB", "quotaGracePeriod"),
        ("ISILON-MIB", "quotaUsage"),
        ("ISILON-MIB", "quotaUsageWithOverhead"),
        ("ISILON-MIB", "quotaInodeUsage"),
        ("ISILON-MIB", "quotaIncludesOverhead"))
)
if mibBuilder.loadTexts:
    quotasGroup.setStatus("current")

snapshotSettingsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 13, 1)
)
snapshotSettingsGroup.setObjects(
      *(("ISILON-MIB", "snapshotScheduledCreateEnabled"),
        ("ISILON-MIB", "snapshotScheduledDeleteEnabled"),
        ("ISILON-MIB", "snapshotReservedPct"),
        ("ISILON-MIB", "snapshotRootVisibilityNFS"),
        ("ISILON-MIB", "snapshotRootAccessNFS"),
        ("ISILON-MIB", "snapshotSubdirAccessNFS"),
        ("ISILON-MIB", "snapshotRootVisibilityCIFS"),
        ("ISILON-MIB", "snapshotRootAccessCIFS"),
        ("ISILON-MIB", "snapshotSubdirAccessCIFS"),
        ("ISILON-MIB", "snapshotRootVisibilityLocal"),
        ("ISILON-MIB", "snapshotRootAccessLocal"),
        ("ISILON-MIB", "snapshotSubdirAccessLocal"))
)
if mibBuilder.loadTexts:
    snapshotSettingsGroup.setStatus("current")

snapshotScheduleTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 13, 2)
)
snapshotScheduleTableGroup.setObjects(
      *(("ISILON-MIB", "snapshotScheduleIndex"),
        ("ISILON-MIB", "snapshotScheduleName"),
        ("ISILON-MIB", "snapshotScheduleAlias"),
        ("ISILON-MIB", "snapshotScheduleNamingPattern"),
        ("ISILON-MIB", "snapshotScheduleSchedule"),
        ("ISILON-MIB", "snapshotScheduleExpiration"),
        ("ISILON-MIB", "snapshotSchedulePath"))
)
if mibBuilder.loadTexts:
    snapshotScheduleTableGroup.setStatus("current")

snapshotTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 1, 13, 3)
)
snapshotTableGroup.setObjects(
      *(("ISILON-MIB", "snapshotName"),
        ("ISILON-MIB", "snapshotCreated"),
        ("ISILON-MIB", "snapshotExpires"),
        ("ISILON-MIB", "snapshotSize"),
        ("ISILON-MIB", "snapshotPath"),
        ("ISILON-MIB", "snapshotAliasFor"),
        ("ISILON-MIB", "snapshotLocked"))
)
if mibBuilder.loadTexts:
    snapshotTableGroup.setStatus("current")

nodeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 1)
)
nodeStatusGroup.setObjects(
      *(("ISILON-MIB", "nodeName"),
        ("ISILON-MIB", "nodeHealth"),
        ("ISILON-MIB", "nodeType"),
        ("ISILON-MIB", "readOnly"))
)
if mibBuilder.loadTexts:
    nodeStatusGroup.setStatus("current")

nodeIfsPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 2, 1)
)
nodeIfsPerfGroup.setObjects(
      *(("ISILON-MIB", "nodeIfsInBytes"),
        ("ISILON-MIB", "nodeIfsInBitsPerSecond"),
        ("ISILON-MIB", "nodeIfsOutBytes"),
        ("ISILON-MIB", "nodeIfsOutBitsPerSecond"))
)
if mibBuilder.loadTexts:
    nodeIfsPerfGroup.setStatus("current")

nodeNetworkPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 2, 2)
)
nodeNetworkPerfGroup.setObjects(
      *(("ISILON-MIB", "nodeNetworkInBytes"),
        ("ISILON-MIB", "nodeNetworkInBitsPerSecond"),
        ("ISILON-MIB", "nodeNetworkOutBytes"),
        ("ISILON-MIB", "nodeNetworkOutBitsPerSecond"))
)
if mibBuilder.loadTexts:
    nodeNetworkPerfGroup.setStatus("current")

nodeCPUPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 2, 3)
)
nodeCPUPerfGroup.setObjects(
      *(("ISILON-MIB", "nodeCPUUser"),
        ("ISILON-MIB", "nodeCPUNice"),
        ("ISILON-MIB", "nodeCPUSystem"),
        ("ISILON-MIB", "nodeCPUInterrupt"),
        ("ISILON-MIB", "nodeCPUIdle"),
        ("ISILON-MIB", "nodePerCPUUser"),
        ("ISILON-MIB", "nodePerCPUNice"),
        ("ISILON-MIB", "nodePerCPUSystem"),
        ("ISILON-MIB", "nodePerCPUInterrupt"),
        ("ISILON-MIB", "nodePerCPUIdle"))
)
if mibBuilder.loadTexts:
    nodeCPUPerfGroup.setStatus("current")

nodeProtocolPerfTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 2, 10)
)
nodeProtocolPerfTableGroup.setObjects(
      *(("ISILON-MIB", "protocolName"),
        ("ISILON-MIB", "protocolOpCount"),
        ("ISILON-MIB", "protocolOpsPerSecond"),
        ("ISILON-MIB", "inMinBytes"),
        ("ISILON-MIB", "inMaxBytes"),
        ("ISILON-MIB", "inAvgBytes"),
        ("ISILON-MIB", "inStdDevBytes"),
        ("ISILON-MIB", "inBitsPerSecond"),
        ("ISILON-MIB", "outMinBytes"),
        ("ISILON-MIB", "outMaxBytes"),
        ("ISILON-MIB", "outAvgBytes"),
        ("ISILON-MIB", "outStdDevBytes"),
        ("ISILON-MIB", "outBitsPerSecond"),
        ("ISILON-MIB", "latencyMin"),
        ("ISILON-MIB", "latencyMax"),
        ("ISILON-MIB", "latencyAverage"),
        ("ISILON-MIB", "latencyStdDev"))
)
if mibBuilder.loadTexts:
    nodeProtocolPerfTableGroup.setStatus("current")

diskPerfTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 2, 52)
)
diskPerfTableGroup.setObjects(
      *(("ISILON-MIB", "diskPerfBay"),
        ("ISILON-MIB", "diskPerfDeviceName"),
        ("ISILON-MIB", "diskPerfOpsPerSecond"),
        ("ISILON-MIB", "diskPerfInBitsPerSecond"),
        ("ISILON-MIB", "diskPerfOutBitsPerSecond"))
)
if mibBuilder.loadTexts:
    diskPerfTableGroup.setStatus("current")

chassisTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 51)
)
chassisTableGroup.setObjects(
      *(("ISILON-MIB", "chassisNumber"),
        ("ISILON-MIB", "chassisConfigNumber"),
        ("ISILON-MIB", "chassisSerialNumber"),
        ("ISILON-MIB", "chassisModel"),
        ("ISILON-MIB", "chassisUnitIDLEDOn"))
)
if mibBuilder.loadTexts:
    chassisTableGroup.setStatus("current")

diskTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 52)
)
diskTableGroup.setObjects(
      *(("ISILON-MIB", "diskBay"),
        ("ISILON-MIB", "diskLogicalNumber"),
        ("ISILON-MIB", "diskChassisNumber"),
        ("ISILON-MIB", "diskDeviceName"),
        ("ISILON-MIB", "diskStatus"),
        ("ISILON-MIB", "diskModel"),
        ("ISILON-MIB", "diskSerialNumber"),
        ("ISILON-MIB", "diskFirmwareVersion"),
        ("ISILON-MIB", "diskSizeBytes"))
)
if mibBuilder.loadTexts:
    diskTableGroup.setStatus("current")

fanTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 53)
)
fanTableGroup.setObjects(
      *(("ISILON-MIB", "fanNumber"),
        ("ISILON-MIB", "fanName"),
        ("ISILON-MIB", "fanDescription"),
        ("ISILON-MIB", "fanSpeed"))
)
if mibBuilder.loadTexts:
    fanTableGroup.setStatus("current")

tempSensorTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 54)
)
tempSensorTableGroup.setObjects(
      *(("ISILON-MIB", "tempSensorNumber"),
        ("ISILON-MIB", "tempSensorName"),
        ("ISILON-MIB", "tempSensorDescription"),
        ("ISILON-MIB", "tempSensorValue"))
)
if mibBuilder.loadTexts:
    tempSensorTableGroup.setStatus("current")

powerSensorTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 12124, 5, 2, 55)
)
powerSensorTableGroup.setObjects(
      *(("ISILON-MIB", "powerSensorNumber"),
        ("ISILON-MIB", "powerSensorName"),
        ("ISILON-MIB", "powerSensorDescription"),
        ("ISILON-MIB", "powerSensorValue"))
)
if mibBuilder.loadTexts:
    powerSensorTableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

isilonCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 12124, 5, 10)
)
if mibBuilder.loadTexts:
    isilonCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISILON-MIB",
    **{"isilon": isilon,
       "cluster": cluster,
       "clusterStatus": clusterStatus,
       "clusterName": clusterName,
       "clusterHealth": clusterHealth,
       "clusterGUID": clusterGUID,
       "nodeCount": nodeCount,
       "configuredNodes": configuredNodes,
       "onlineNodes": onlineNodes,
       "offlineNodes": offlineNodes,
       "clusterPerformance": clusterPerformance,
       "clusterIfsPerf": clusterIfsPerf,
       "clusterIfsInBytes": clusterIfsInBytes,
       "clusterIfsInBitsPerSecond": clusterIfsInBitsPerSecond,
       "clusterIfsOutBytes": clusterIfsOutBytes,
       "clusterIfsOutBitsPerSecond": clusterIfsOutBitsPerSecond,
       "clusterNetworkPerf": clusterNetworkPerf,
       "clusterNetworkInBytes": clusterNetworkInBytes,
       "clusterNetworkInBitsPerSecond": clusterNetworkInBitsPerSecond,
       "clusterNetworkOutBytes": clusterNetworkOutBytes,
       "clusterNetworkOutBitsPerSecond": clusterNetworkOutBitsPerSecond,
       "clusterCPUPerf": clusterCPUPerf,
       "clusterCPUUser": clusterCPUUser,
       "clusterCPUNice": clusterCPUNice,
       "clusterCPUSystem": clusterCPUSystem,
       "clusterCPUInterrupt": clusterCPUInterrupt,
       "clusterCPUIdlePct": clusterCPUIdlePct,
       "ifsFilesystem": ifsFilesystem,
       "ifsTotalBytes": ifsTotalBytes,
       "ifsUsedBytes": ifsUsedBytes,
       "ifsAvailableBytes": ifsAvailableBytes,
       "ifsFreeBytes": ifsFreeBytes,
       "accessTimeEnabled": accessTimeEnabled,
       "accessTimeGracePeriod": accessTimeGracePeriod,
       "licenses": licenses,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseIndex": licenseIndex,
       "licenseModuleName": licenseModuleName,
       "licenseStatus": licenseStatus,
       "licenseExpirationDate": licenseExpirationDate,
       "quotas": quotas,
       "quotaTable": quotaTable,
       "quotaEntry": quotaEntry,
       "quotaDomainID": quotaDomainID,
       "quotaType": quotaType,
       "quotaID": quotaID,
       "quotaIncludesSnapshotUsage": quotaIncludesSnapshotUsage,
       "quotaPath": quotaPath,
       "quotaHardThresholdDefined": quotaHardThresholdDefined,
       "quotaHardThreshold": quotaHardThreshold,
       "quotaSoftThresholdDefined": quotaSoftThresholdDefined,
       "quotaSoftThreshold": quotaSoftThreshold,
       "quotaAdvisoryThresholdDefined": quotaAdvisoryThresholdDefined,
       "quotaAdvisoryThreshold": quotaAdvisoryThreshold,
       "quotaGracePeriod": quotaGracePeriod,
       "quotaUsage": quotaUsage,
       "quotaUsageWithOverhead": quotaUsageWithOverhead,
       "quotaInodeUsage": quotaInodeUsage,
       "quotaIncludesOverhead": quotaIncludesOverhead,
       "snapshots": snapshots,
       "snapshotSettings": snapshotSettings,
       "snapshotScheduledCreateEnabled": snapshotScheduledCreateEnabled,
       "snapshotScheduledDeleteEnabled": snapshotScheduledDeleteEnabled,
       "snapshotReservedPct": snapshotReservedPct,
       "snapshotRootVisibilityNFS": snapshotRootVisibilityNFS,
       "snapshotRootAccessNFS": snapshotRootAccessNFS,
       "snapshotSubdirAccessNFS": snapshotSubdirAccessNFS,
       "snapshotRootVisibilityCIFS": snapshotRootVisibilityCIFS,
       "snapshotRootAccessCIFS": snapshotRootAccessCIFS,
       "snapshotSubdirAccessCIFS": snapshotSubdirAccessCIFS,
       "snapshotRootVisibilityLocal": snapshotRootVisibilityLocal,
       "snapshotRootAccessLocal": snapshotRootAccessLocal,
       "snapshotSubdirAccessLocal": snapshotSubdirAccessLocal,
       "snapshotScheduleTable": snapshotScheduleTable,
       "snapshotScheduleEntry": snapshotScheduleEntry,
       "snapshotScheduleIndex": snapshotScheduleIndex,
       "snapshotScheduleName": snapshotScheduleName,
       "snapshotScheduleAlias": snapshotScheduleAlias,
       "snapshotScheduleNamingPattern": snapshotScheduleNamingPattern,
       "snapshotScheduleSchedule": snapshotScheduleSchedule,
       "snapshotScheduleExpiration": snapshotScheduleExpiration,
       "snapshotSchedulePath": snapshotSchedulePath,
       "snapshotTable": snapshotTable,
       "snapshotEntry": snapshotEntry,
       "snapshotIndex": snapshotIndex,
       "snapshotName": snapshotName,
       "snapshotCreated": snapshotCreated,
       "snapshotExpires": snapshotExpires,
       "snapshotSize": snapshotSize,
       "snapshotPath": snapshotPath,
       "snapshotAliasFor": snapshotAliasFor,
       "snapshotLocked": snapshotLocked,
       "node": node,
       "nodeStatus": nodeStatus,
       "nodeName": nodeName,
       "nodeHealth": nodeHealth,
       "nodeType": nodeType,
       "readOnly": readOnly,
       "nodePerformance": nodePerformance,
       "nodeIfsPerf": nodeIfsPerf,
       "nodeIfsInBytes": nodeIfsInBytes,
       "nodeIfsInBitsPerSecond": nodeIfsInBitsPerSecond,
       "nodeIfsOutBytes": nodeIfsOutBytes,
       "nodeIfsOutBitsPerSecond": nodeIfsOutBitsPerSecond,
       "nodeNetworkPerf": nodeNetworkPerf,
       "nodeNetworkInBytes": nodeNetworkInBytes,
       "nodeNetworkInBitsPerSecond": nodeNetworkInBitsPerSecond,
       "nodeNetworkOutBytes": nodeNetworkOutBytes,
       "nodeNetworkOutBitsPerSecond": nodeNetworkOutBitsPerSecond,
       "nodeCPUPerf": nodeCPUPerf,
       "nodeCPUUser": nodeCPUUser,
       "nodeCPUNice": nodeCPUNice,
       "nodeCPUSystem": nodeCPUSystem,
       "nodeCPUInterrupt": nodeCPUInterrupt,
       "nodeCPUIdle": nodeCPUIdle,
       "nodeCPUPerfTable": nodeCPUPerfTable,
       "nodeCPUPerfEntry": nodeCPUPerfEntry,
       "nodePerCPUUser": nodePerCPUUser,
       "nodePerCPUNice": nodePerCPUNice,
       "nodePerCPUSystem": nodePerCPUSystem,
       "nodePerCPUInterrupt": nodePerCPUInterrupt,
       "nodePerCPUIdle": nodePerCPUIdle,
       "nodePerCPUID": nodePerCPUID,
       "nodeProtocolPerfTable": nodeProtocolPerfTable,
       "nodeProtocolPerfEntry": nodeProtocolPerfEntry,
       "protocolName": protocolName,
       "protocolOpCount": protocolOpCount,
       "protocolOpsPerSecond": protocolOpsPerSecond,
       "inMinBytes": inMinBytes,
       "inMaxBytes": inMaxBytes,
       "inAvgBytes": inAvgBytes,
       "inStdDevBytes": inStdDevBytes,
       "inBitsPerSecond": inBitsPerSecond,
       "outMinBytes": outMinBytes,
       "outMaxBytes": outMaxBytes,
       "outAvgBytes": outAvgBytes,
       "outStdDevBytes": outStdDevBytes,
       "outBitsPerSecond": outBitsPerSecond,
       "latencyMin": latencyMin,
       "latencyMax": latencyMax,
       "latencyAverage": latencyAverage,
       "latencyStdDev": latencyStdDev,
       "diskPerfTable": diskPerfTable,
       "diskPerfEntry": diskPerfEntry,
       "diskPerfBay": diskPerfBay,
       "diskPerfDeviceName": diskPerfDeviceName,
       "diskPerfOpsPerSecond": diskPerfOpsPerSecond,
       "diskPerfInBitsPerSecond": diskPerfInBitsPerSecond,
       "diskPerfOutBitsPerSecond": diskPerfOutBitsPerSecond,
       "chassisTable": chassisTable,
       "chassisEntry": chassisEntry,
       "chassisNumber": chassisNumber,
       "chassisConfigNumber": chassisConfigNumber,
       "chassisSerialNumber": chassisSerialNumber,
       "chassisModel": chassisModel,
       "chassisUnitIDLEDOn": chassisUnitIDLEDOn,
       "diskTable": diskTable,
       "diskEntry": diskEntry,
       "diskBay": diskBay,
       "diskLogicalNumber": diskLogicalNumber,
       "diskChassisNumber": diskChassisNumber,
       "diskDeviceName": diskDeviceName,
       "diskStatus": diskStatus,
       "diskModel": diskModel,
       "diskSerialNumber": diskSerialNumber,
       "diskFirmwareVersion": diskFirmwareVersion,
       "diskSizeBytes": diskSizeBytes,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanNumber": fanNumber,
       "fanName": fanName,
       "fanDescription": fanDescription,
       "fanSpeed": fanSpeed,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorNumber": tempSensorNumber,
       "tempSensorName": tempSensorName,
       "tempSensorDescription": tempSensorDescription,
       "tempSensorValue": tempSensorValue,
       "powerSensorTable": powerSensorTable,
       "powerSensorEntry": powerSensorEntry,
       "powerSensorNumber": powerSensorNumber,
       "powerSensorName": powerSensorName,
       "powerSensorDescription": powerSensorDescription,
       "powerSensorValue": powerSensorValue,
       "local": local,
       "credentialBindings": credentialBindings,
       "conformance": conformance,
       "clusterGroups": clusterGroups,
       "clusterStatusGroup": clusterStatusGroup,
       "clusterPerformanceGroups": clusterPerformanceGroups,
       "clusterIfsPerfGroup": clusterIfsPerfGroup,
       "clusterNetworkPerfGroup": clusterNetworkPerfGroup,
       "clusterCPUPerfGroup": clusterCPUPerfGroup,
       "ifsFilesystemGroup": ifsFilesystemGroup,
       "licensesGroup": licensesGroup,
       "quotasGroup": quotasGroup,
       "snapshotsGroup": snapshotsGroup,
       "snapshotSettingsGroup": snapshotSettingsGroup,
       "snapshotScheduleTableGroup": snapshotScheduleTableGroup,
       "snapshotTableGroup": snapshotTableGroup,
       "nodeGroups": nodeGroups,
       "nodeStatusGroup": nodeStatusGroup,
       "nodePerformanceGroup": nodePerformanceGroup,
       "nodeIfsPerfGroup": nodeIfsPerfGroup,
       "nodeNetworkPerfGroup": nodeNetworkPerfGroup,
       "nodeCPUPerfGroup": nodeCPUPerfGroup,
       "nodeProtocolPerfTableGroup": nodeProtocolPerfTableGroup,
       "diskPerfTableGroup": diskPerfTableGroup,
       "chassisTableGroup": chassisTableGroup,
       "diskTableGroup": diskTableGroup,
       "fanTableGroup": fanTableGroup,
       "tempSensorTableGroup": tempSensorTableGroup,
       "powerSensorTableGroup": powerSensorTableGroup,
       "isilonCompliance": isilonCompliance}
)
