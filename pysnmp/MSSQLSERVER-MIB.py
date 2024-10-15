# SNMP MIB module (MSSQLSERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSSQLSERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:01 2024
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Microsoft_ObjectIdentity = ObjectIdentity
microsoft = _Microsoft_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1)
)
_Apps_ObjectIdentity = ObjectIdentity
apps = _Apps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 4)
)
_MssqlServer_ObjectIdentity = ObjectIdentity
mssqlServer = _MssqlServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1)
)
_MssqlServerObjects_ObjectIdentity = ObjectIdentity
mssqlServerObjects = _MssqlServerObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1)
)
_MssqlSrvTable_Object = MibTable
mssqlSrvTable = _MssqlSrvTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mssqlSrvTable.setStatus("mandatory")
_MssqlSrvEntry_Object = MibTableRow
mssqlSrvEntry = _MssqlSrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 1, 1)
)
mssqlSrvEntry.setIndexNames(
    (0, "MSSQLSERVER-MIB", "mssqlSrvVendorName"),
)
if mibBuilder.loadTexts:
    mssqlSrvEntry.setStatus("mandatory")
_MssqlSrvVendorName_Type = DisplayString
_MssqlSrvVendorName_Object = MibTableColumn
mssqlSrvVendorName = _MssqlSrvVendorName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 1, 1, 1),
    _MssqlSrvVendorName_Type()
)
mssqlSrvVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvVendorName.setStatus("mandatory")
_MssqlSrvProductName_Type = DisplayString
_MssqlSrvProductName_Object = MibTableColumn
mssqlSrvProductName = _MssqlSrvProductName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 1, 1, 2),
    _MssqlSrvProductName_Type()
)
mssqlSrvProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvProductName.setStatus("mandatory")
_MssqlSrvVersion_Type = DisplayString
_MssqlSrvVersion_Object = MibTableColumn
mssqlSrvVersion = _MssqlSrvVersion_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 1, 1, 3),
    _MssqlSrvVersion_Type()
)
mssqlSrvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvVersion.setStatus("mandatory")
_MssqlSrvContact_Type = DisplayString
_MssqlSrvContact_Object = MibTableColumn
mssqlSrvContact = _MssqlSrvContact_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 1, 1, 4),
    _MssqlSrvContact_Type()
)
mssqlSrvContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvContact.setStatus("mandatory")


class _MssqlSrvState_Type(Integer32):
    """Custom type mssqlSrvState based on Integer32"""
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
        *(("continuing", 6),
          ("paused", 2),
          ("pausing", 7),
          ("running", 1),
          ("starting", 4),
          ("stopped", 3),
          ("stopping", 5))
    )


_MssqlSrvState_Type.__name__ = "Integer32"
_MssqlSrvState_Object = MibTableColumn
mssqlSrvState = _MssqlSrvState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 1, 1, 5),
    _MssqlSrvState_Type()
)
mssqlSrvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvState.setStatus("mandatory")
_MssqlSrvInfoTable_Object = MibTable
mssqlSrvInfoTable = _MssqlSrvInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    mssqlSrvInfoTable.setStatus("mandatory")
_MssqlSrvInfoEntry_Object = MibTableRow
mssqlSrvInfoEntry = _MssqlSrvInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1)
)
mssqlSrvInfoEntry.setIndexNames(
    (0, "MSSQLSERVER-MIB", "mssqlSrvInfoServerName"),
)
if mibBuilder.loadTexts:
    mssqlSrvInfoEntry.setStatus("mandatory")
_MssqlSrvInfoServerName_Type = DisplayString
_MssqlSrvInfoServerName_Object = MibTableColumn
mssqlSrvInfoServerName = _MssqlSrvInfoServerName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 1),
    _MssqlSrvInfoServerName_Type()
)
mssqlSrvInfoServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoServerName.setStatus("mandatory")
_MssqlSrvInfoStartupTime_Type = DisplayString
_MssqlSrvInfoStartupTime_Object = MibTableColumn
mssqlSrvInfoStartupTime = _MssqlSrvInfoStartupTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 2),
    _MssqlSrvInfoStartupTime_Type()
)
mssqlSrvInfoStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoStartupTime.setStatus("mandatory")
_MssqlSrvInfoTrans_Type = Gauge32
_MssqlSrvInfoTrans_Object = MibTableColumn
mssqlSrvInfoTrans = _MssqlSrvInfoTrans_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 3),
    _MssqlSrvInfoTrans_Type()
)
mssqlSrvInfoTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoTrans.setStatus("mandatory")
_MssqlSrvInfoPageReads_Type = Counter32
_MssqlSrvInfoPageReads_Object = MibTableColumn
mssqlSrvInfoPageReads = _MssqlSrvInfoPageReads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 4),
    _MssqlSrvInfoPageReads_Type()
)
mssqlSrvInfoPageReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoPageReads.setStatus("mandatory")
_MssqlSrvInfoSinglePageWrites_Type = Counter32
_MssqlSrvInfoSinglePageWrites_Object = MibTableColumn
mssqlSrvInfoSinglePageWrites = _MssqlSrvInfoSinglePageWrites_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 5),
    _MssqlSrvInfoSinglePageWrites_Type()
)
mssqlSrvInfoSinglePageWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoSinglePageWrites.setStatus("mandatory")
_MssqlSrvInfoBatchWrites_Type = Counter32
_MssqlSrvInfoBatchWrites_Object = MibTableColumn
mssqlSrvInfoBatchWrites = _MssqlSrvInfoBatchWrites_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 6),
    _MssqlSrvInfoBatchWrites_Type()
)
mssqlSrvInfoBatchWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoBatchWrites.setStatus("mandatory")
_MssqlSrvInfoLazyWrites_Type = Counter32
_MssqlSrvInfoLazyWrites_Object = MibTableColumn
mssqlSrvInfoLazyWrites = _MssqlSrvInfoLazyWrites_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 7),
    _MssqlSrvInfoLazyWrites_Type()
)
mssqlSrvInfoLazyWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoLazyWrites.setStatus("mandatory")
_MssqlSrvInfoLogWrites_Type = Counter32
_MssqlSrvInfoLogWrites_Object = MibTableColumn
mssqlSrvInfoLogWrites = _MssqlSrvInfoLogWrites_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 8),
    _MssqlSrvInfoLogWrites_Type()
)
mssqlSrvInfoLogWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoLogWrites.setStatus("mandatory")
_MssqlSrvInfoOutstandingReads_Type = Counter32
_MssqlSrvInfoOutstandingReads_Object = MibTableColumn
mssqlSrvInfoOutstandingReads = _MssqlSrvInfoOutstandingReads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 9),
    _MssqlSrvInfoOutstandingReads_Type()
)
mssqlSrvInfoOutstandingReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoOutstandingReads.setStatus("mandatory")
_MssqlSrvInfoOutstandingWrites_Type = Counter32
_MssqlSrvInfoOutstandingWrites_Object = MibTableColumn
mssqlSrvInfoOutstandingWrites = _MssqlSrvInfoOutstandingWrites_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 10),
    _MssqlSrvInfoOutstandingWrites_Type()
)
mssqlSrvInfoOutstandingWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoOutstandingWrites.setStatus("mandatory")
_MssqlSrvInfoCacheHitRatio_Type = Gauge32
_MssqlSrvInfoCacheHitRatio_Object = MibTableColumn
mssqlSrvInfoCacheHitRatio = _MssqlSrvInfoCacheHitRatio_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 11),
    _MssqlSrvInfoCacheHitRatio_Type()
)
mssqlSrvInfoCacheHitRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoCacheHitRatio.setStatus("mandatory")
_MssqlSrvInfoFreeBuffers_Type = Gauge32
_MssqlSrvInfoFreeBuffers_Object = MibTableColumn
mssqlSrvInfoFreeBuffers = _MssqlSrvInfoFreeBuffers_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 12),
    _MssqlSrvInfoFreeBuffers_Type()
)
mssqlSrvInfoFreeBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoFreeBuffers.setStatus("mandatory")
_MssqlSrvInfoNetworkReads_Type = Counter32
_MssqlSrvInfoNetworkReads_Object = MibTableColumn
mssqlSrvInfoNetworkReads = _MssqlSrvInfoNetworkReads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 13),
    _MssqlSrvInfoNetworkReads_Type()
)
mssqlSrvInfoNetworkReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoNetworkReads.setStatus("mandatory")
_MssqlSrvInfoNetworkWrites_Type = Counter32
_MssqlSrvInfoNetworkWrites_Object = MibTableColumn
mssqlSrvInfoNetworkWrites = _MssqlSrvInfoNetworkWrites_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 14),
    _MssqlSrvInfoNetworkWrites_Type()
)
mssqlSrvInfoNetworkWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoNetworkWrites.setStatus("mandatory")
_MssqlSrvInfoRAPhysicalReads_Type = Counter32
_MssqlSrvInfoRAPhysicalReads_Object = MibTableColumn
mssqlSrvInfoRAPhysicalReads = _MssqlSrvInfoRAPhysicalReads_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 15),
    _MssqlSrvInfoRAPhysicalReads_Type()
)
mssqlSrvInfoRAPhysicalReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoRAPhysicalReads.setStatus("mandatory")
_MssqlSrvInfoUserConnections_Type = Gauge32
_MssqlSrvInfoUserConnections_Object = MibTableColumn
mssqlSrvInfoUserConnections = _MssqlSrvInfoUserConnections_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 16),
    _MssqlSrvInfoUserConnections_Type()
)
mssqlSrvInfoUserConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoUserConnections.setStatus("mandatory")
_MssqlSrvInfoTotalLocks_Type = Gauge32
_MssqlSrvInfoTotalLocks_Object = MibTableColumn
mssqlSrvInfoTotalLocks = _MssqlSrvInfoTotalLocks_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 17),
    _MssqlSrvInfoTotalLocks_Type()
)
mssqlSrvInfoTotalLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoTotalLocks.setStatus("mandatory")
_MssqlSrvInfoTotalBlockingLocks_Type = Gauge32
_MssqlSrvInfoTotalBlockingLocks_Object = MibTableColumn
mssqlSrvInfoTotalBlockingLocks = _MssqlSrvInfoTotalBlockingLocks_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 18),
    _MssqlSrvInfoTotalBlockingLocks_Type()
)
mssqlSrvInfoTotalBlockingLocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoTotalBlockingLocks.setStatus("mandatory")
_MssqlSrvInfoUsersBlocked_Type = Gauge32
_MssqlSrvInfoUsersBlocked_Object = MibTableColumn
mssqlSrvInfoUsersBlocked = _MssqlSrvInfoUsersBlocked_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 2, 1, 19),
    _MssqlSrvInfoUsersBlocked_Type()
)
mssqlSrvInfoUsersBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvInfoUsersBlocked.setStatus("mandatory")
_MssqlSrvConfigParamTable_Object = MibTable
mssqlSrvConfigParamTable = _MssqlSrvConfigParamTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 3)
)
if mibBuilder.loadTexts:
    mssqlSrvConfigParamTable.setStatus("mandatory")
_MssqlSrvConfigParamEntry_Object = MibTableRow
mssqlSrvConfigParamEntry = _MssqlSrvConfigParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    mssqlSrvConfigParamEntry.setStatus("mandatory")
_MssqlSrvConfigParamName_Type = DisplayString
_MssqlSrvConfigParamName_Object = MibTableColumn
mssqlSrvConfigParamName = _MssqlSrvConfigParamName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 3, 1, 1),
    _MssqlSrvConfigParamName_Type()
)
mssqlSrvConfigParamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvConfigParamName.setStatus("mandatory")
_MssqlSrvConfigParamMax_Type = Integer32
_MssqlSrvConfigParamMax_Object = MibTableColumn
mssqlSrvConfigParamMax = _MssqlSrvConfigParamMax_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 3, 1, 2),
    _MssqlSrvConfigParamMax_Type()
)
mssqlSrvConfigParamMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvConfigParamMax.setStatus("mandatory")
_MssqlSrvConfigParamMin_Type = Integer32
_MssqlSrvConfigParamMin_Object = MibTableColumn
mssqlSrvConfigParamMin = _MssqlSrvConfigParamMin_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 3, 1, 3),
    _MssqlSrvConfigParamMin_Type()
)
mssqlSrvConfigParamMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvConfigParamMin.setStatus("mandatory")
_MssqlSrvConfigParamConfigValue_Type = Integer32
_MssqlSrvConfigParamConfigValue_Object = MibTableColumn
mssqlSrvConfigParamConfigValue = _MssqlSrvConfigParamConfigValue_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 3, 1, 4),
    _MssqlSrvConfigParamConfigValue_Type()
)
mssqlSrvConfigParamConfigValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvConfigParamConfigValue.setStatus("mandatory")
_MssqlSrvConfigParamRunValue_Type = Integer32
_MssqlSrvConfigParamRunValue_Object = MibTableColumn
mssqlSrvConfigParamRunValue = _MssqlSrvConfigParamRunValue_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 3, 1, 5),
    _MssqlSrvConfigParamRunValue_Type()
)
mssqlSrvConfigParamRunValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvConfigParamRunValue.setStatus("mandatory")
_MssqlSrvDeviceTable_Object = MibTable
mssqlSrvDeviceTable = _MssqlSrvDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    mssqlSrvDeviceTable.setStatus("mandatory")
_MssqlSrvDeviceEntry_Object = MibTableRow
mssqlSrvDeviceEntry = _MssqlSrvDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 4, 1)
)
mssqlSrvDeviceEntry.setIndexNames(
    (0, "MSSQLSERVER-MIB", "mssqlSrvDeviceLogicalName"),
)
if mibBuilder.loadTexts:
    mssqlSrvDeviceEntry.setStatus("mandatory")
_MssqlSrvDeviceLogicalName_Type = DisplayString
_MssqlSrvDeviceLogicalName_Object = MibTableColumn
mssqlSrvDeviceLogicalName = _MssqlSrvDeviceLogicalName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 4, 1, 1),
    _MssqlSrvDeviceLogicalName_Type()
)
mssqlSrvDeviceLogicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvDeviceLogicalName.setStatus("mandatory")
_MssqlSrvDevicePhysicalName_Type = DisplayString
_MssqlSrvDevicePhysicalName_Object = MibTableColumn
mssqlSrvDevicePhysicalName = _MssqlSrvDevicePhysicalName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 4, 1, 2),
    _MssqlSrvDevicePhysicalName_Type()
)
mssqlSrvDevicePhysicalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvDevicePhysicalName.setStatus("mandatory")
_MssqlSrvDeviceDescription_Type = DisplayString
_MssqlSrvDeviceDescription_Object = MibTableColumn
mssqlSrvDeviceDescription = _MssqlSrvDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 4, 1, 3),
    _MssqlSrvDeviceDescription_Type()
)
mssqlSrvDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlSrvDeviceDescription.setStatus("mandatory")
_MssqlDbTable_Object = MibTable
mssqlDbTable = _MssqlDbTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    mssqlDbTable.setStatus("mandatory")
_MssqlDbEntry_Object = MibTableRow
mssqlDbEntry = _MssqlDbEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 5, 1)
)
mssqlDbEntry.setIndexNames(
    (0, "MSSQLSERVER-MIB", "mssqlDbId"),
    (0, "MSSQLSERVER-MIB", "mssqlDbState"),
)
if mibBuilder.loadTexts:
    mssqlDbEntry.setStatus("mandatory")


class _MssqlDbId_Type(Integer32):
    """Custom type mssqlDbId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbId_Type.__name__ = "Integer32"
_MssqlDbId_Object = MibTableColumn
mssqlDbId = _MssqlDbId_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 5, 1, 1),
    _MssqlDbId_Type()
)
mssqlDbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbId.setStatus("mandatory")
_MssqlDbName_Type = DisplayString
_MssqlDbName_Object = MibTableColumn
mssqlDbName = _MssqlDbName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 5, 1, 2),
    _MssqlDbName_Type()
)
mssqlDbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbName.setStatus("mandatory")


class _MssqlDbState_Type(Integer32):
    """Custom type mssqlDbState based on Integer32"""
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
        *(("active", 1),
          ("dboonly", 3),
          ("loading", 7),
          ("offline", 5),
          ("publishing", 8),
          ("readOnly", 4),
          ("singleUser", 2),
          ("suspect", 6))
    )


_MssqlDbState_Type.__name__ = "Integer32"
_MssqlDbState_Object = MibTableColumn
mssqlDbState = _MssqlDbState_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 5, 1, 3),
    _MssqlDbState_Type()
)
mssqlDbState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbState.setStatus("mandatory")
_MssqlDbInfoTable_Object = MibTable
mssqlDbInfoTable = _MssqlDbInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    mssqlDbInfoTable.setStatus("mandatory")
_MssqlDbInfoEntry_Object = MibTableRow
mssqlDbInfoEntry = _MssqlDbInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1)
)
mssqlDbInfoEntry.setIndexNames(
    (0, "MSSQLSERVER-MIB", "mssqlDbInfoDbId"),
)
if mibBuilder.loadTexts:
    mssqlDbInfoEntry.setStatus("mandatory")
_MssqlDbInfoDbId_Type = Integer32
_MssqlDbInfoDbId_Object = MibTableColumn
mssqlDbInfoDbId = _MssqlDbInfoDbId_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 1),
    _MssqlDbInfoDbId_Type()
)
mssqlDbInfoDbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoDbId.setStatus("mandatory")
_MssqlDbInfoDbName_Type = DisplayString
_MssqlDbInfoDbName_Object = MibTableColumn
mssqlDbInfoDbName = _MssqlDbInfoDbName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 2),
    _MssqlDbInfoDbName_Type()
)
mssqlDbInfoDbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoDbName.setStatus("mandatory")
_MssqlDbInfoCreationDateTime_Type = DisplayString
_MssqlDbInfoCreationDateTime_Object = MibTableColumn
mssqlDbInfoCreationDateTime = _MssqlDbInfoCreationDateTime_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 3),
    _MssqlDbInfoCreationDateTime_Type()
)
mssqlDbInfoCreationDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoCreationDateTime.setStatus("mandatory")
_MssqlDbInfoOwner_Type = DisplayString
_MssqlDbInfoOwner_Object = MibTableColumn
mssqlDbInfoOwner = _MssqlDbInfoOwner_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 4),
    _MssqlDbInfoOwner_Type()
)
mssqlDbInfoOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoOwner.setStatus("mandatory")


class _MssqlDbInfoSize_Type(Integer32):
    """Custom type mssqlDbInfoSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoSize_Type.__name__ = "Integer32"
_MssqlDbInfoSize_Object = MibTableColumn
mssqlDbInfoSize = _MssqlDbInfoSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 5),
    _MssqlDbInfoSize_Type()
)
mssqlDbInfoSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoSize.setStatus("mandatory")


class _MssqlDbInfoUnallocatedSpace_Type(Integer32):
    """Custom type mssqlDbInfoUnallocatedSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoUnallocatedSpace_Type.__name__ = "Integer32"
_MssqlDbInfoUnallocatedSpace_Object = MibTableColumn
mssqlDbInfoUnallocatedSpace = _MssqlDbInfoUnallocatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 6),
    _MssqlDbInfoUnallocatedSpace_Type()
)
mssqlDbInfoUnallocatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoUnallocatedSpace.setStatus("mandatory")


class _MssqlDbInfoReservedSpace_Type(Integer32):
    """Custom type mssqlDbInfoReservedSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoReservedSpace_Type.__name__ = "Integer32"
_MssqlDbInfoReservedSpace_Object = MibTableColumn
mssqlDbInfoReservedSpace = _MssqlDbInfoReservedSpace_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 7),
    _MssqlDbInfoReservedSpace_Type()
)
mssqlDbInfoReservedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoReservedSpace.setStatus("mandatory")


class _MssqlDbInfoDataSpace_Type(Integer32):
    """Custom type mssqlDbInfoDataSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoDataSpace_Type.__name__ = "Integer32"
_MssqlDbInfoDataSpace_Object = MibTableColumn
mssqlDbInfoDataSpace = _MssqlDbInfoDataSpace_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 8),
    _MssqlDbInfoDataSpace_Type()
)
mssqlDbInfoDataSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoDataSpace.setStatus("mandatory")


class _MssqlDbInfoIndexSpace_Type(Integer32):
    """Custom type mssqlDbInfoIndexSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoIndexSpace_Type.__name__ = "Integer32"
_MssqlDbInfoIndexSpace_Object = MibTableColumn
mssqlDbInfoIndexSpace = _MssqlDbInfoIndexSpace_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 9),
    _MssqlDbInfoIndexSpace_Type()
)
mssqlDbInfoIndexSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoIndexSpace.setStatus("mandatory")


class _MssqlDbInfoUnusedSpace_Type(Integer32):
    """Custom type mssqlDbInfoUnusedSpace based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoUnusedSpace_Type.__name__ = "Integer32"
_MssqlDbInfoUnusedSpace_Object = MibTableColumn
mssqlDbInfoUnusedSpace = _MssqlDbInfoUnusedSpace_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 10),
    _MssqlDbInfoUnusedSpace_Type()
)
mssqlDbInfoUnusedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoUnusedSpace.setStatus("mandatory")
_MssqlDbInfoLastTrLogDump_Type = DisplayString
_MssqlDbInfoLastTrLogDump_Object = MibTableColumn
mssqlDbInfoLastTrLogDump = _MssqlDbInfoLastTrLogDump_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 11),
    _MssqlDbInfoLastTrLogDump_Type()
)
mssqlDbInfoLastTrLogDump.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoLastTrLogDump.setStatus("mandatory")


class _MssqlDbInfoLogSize_Type(Integer32):
    """Custom type mssqlDbInfoLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoLogSize_Type.__name__ = "Integer32"
_MssqlDbInfoLogSize_Object = MibTableColumn
mssqlDbInfoLogSize = _MssqlDbInfoLogSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 12),
    _MssqlDbInfoLogSize_Type()
)
mssqlDbInfoLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoLogSize.setStatus("mandatory")


class _MssqlDbInfoLogSpaceUsed_Type(Integer32):
    """Custom type mssqlDbInfoLogSpaceUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbInfoLogSpaceUsed_Type.__name__ = "Integer32"
_MssqlDbInfoLogSpaceUsed_Object = MibTableColumn
mssqlDbInfoLogSpaceUsed = _MssqlDbInfoLogSpaceUsed_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 6, 1, 13),
    _MssqlDbInfoLogSpaceUsed_Type()
)
mssqlDbInfoLogSpaceUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbInfoLogSpaceUsed.setStatus("mandatory")
_MssqlDbOptionTable_Object = MibTable
mssqlDbOptionTable = _MssqlDbOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    mssqlDbOptionTable.setStatus("mandatory")
_MssqlDbOptionEntry_Object = MibTableRow
mssqlDbOptionEntry = _MssqlDbOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 7, 1)
)
mssqlDbOptionEntry.setIndexNames(
    (0, "MSSQLSERVER-MIB", "mssqlDbOptionDbId"),
    (0, "MSSQLSERVER-MIB", "pysmiFakeCol1"),
)
if mibBuilder.loadTexts:
    mssqlDbOptionEntry.setStatus("mandatory")


class _MssqlDbOptionDbId_Type(Integer32):
    """Custom type mssqlDbOptionDbId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbOptionDbId_Type.__name__ = "Integer32"
_MssqlDbOptionDbId_Object = MibTableColumn
mssqlDbOptionDbId = _MssqlDbOptionDbId_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 7, 1, 1),
    _MssqlDbOptionDbId_Type()
)
mssqlDbOptionDbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbOptionDbId.setStatus("mandatory")
_MssqlDbOptionDbName_Type = DisplayString
_MssqlDbOptionDbName_Object = MibTableColumn
mssqlDbOptionDbName = _MssqlDbOptionDbName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 7, 1, 2),
    _MssqlDbOptionDbName_Type()
)
mssqlDbOptionDbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbOptionDbName.setStatus("mandatory")
_MssqlDbOptionSetName_Type = DisplayString
_MssqlDbOptionSetName_Object = MibTableColumn
mssqlDbOptionSetName = _MssqlDbOptionSetName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 7, 1, 3),
    _MssqlDbOptionSetName_Type()
)
mssqlDbOptionSetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbOptionSetName.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 7, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_MssqlDbDeviceTable_Object = MibTable
mssqlDbDeviceTable = _MssqlDbDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    mssqlDbDeviceTable.setStatus("mandatory")
_MssqlDbDeviceEntry_Object = MibTableRow
mssqlDbDeviceEntry = _MssqlDbDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8, 1)
)
mssqlDbDeviceEntry.setIndexNames(
    (0, "MSSQLSERVER-MIB", "mssqlDbDeviceDbId"),
    (0, "MSSQLSERVER-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    mssqlDbDeviceEntry.setStatus("mandatory")
_MssqlDbDeviceDbId_Type = Integer32
_MssqlDbDeviceDbId_Object = MibTableColumn
mssqlDbDeviceDbId = _MssqlDbDeviceDbId_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8, 1, 1),
    _MssqlDbDeviceDbId_Type()
)
mssqlDbDeviceDbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbDeviceDbId.setStatus("mandatory")
_MssqlDbDeviceDbName_Type = DisplayString
_MssqlDbDeviceDbName_Object = MibTableColumn
mssqlDbDeviceDbName = _MssqlDbDeviceDbName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8, 1, 2),
    _MssqlDbDeviceDbName_Type()
)
mssqlDbDeviceDbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbDeviceDbName.setStatus("mandatory")
_MssqlDbDeviceFragmentName_Type = DisplayString
_MssqlDbDeviceFragmentName_Object = MibTableColumn
mssqlDbDeviceFragmentName = _MssqlDbDeviceFragmentName_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8, 1, 3),
    _MssqlDbDeviceFragmentName_Type()
)
mssqlDbDeviceFragmentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbDeviceFragmentName.setStatus("mandatory")


class _MssqlDbDeviceFragmentSize_Type(Integer32):
    """Custom type mssqlDbDeviceFragmentSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MssqlDbDeviceFragmentSize_Type.__name__ = "Integer32"
_MssqlDbDeviceFragmentSize_Object = MibTableColumn
mssqlDbDeviceFragmentSize = _MssqlDbDeviceFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8, 1, 4),
    _MssqlDbDeviceFragmentSize_Type()
)
mssqlDbDeviceFragmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbDeviceFragmentSize.setStatus("mandatory")
_MssqlDbDeviceFragmentUsage_Type = DisplayString
_MssqlDbDeviceFragmentUsage_Object = MibTableColumn
mssqlDbDeviceFragmentUsage = _MssqlDbDeviceFragmentUsage_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8, 1, 5),
    _MssqlDbDeviceFragmentUsage_Type()
)
mssqlDbDeviceFragmentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mssqlDbDeviceFragmentUsage.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 311, 1, 4, 1, 1, 8, 1, 4294967295),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSSQLSERVER-MIB",
    **{"microsoft": microsoft,
       "software": software,
       "apps": apps,
       "mssqlServer": mssqlServer,
       "mssqlServerObjects": mssqlServerObjects,
       "mssqlSrvTable": mssqlSrvTable,
       "mssqlSrvEntry": mssqlSrvEntry,
       "mssqlSrvVendorName": mssqlSrvVendorName,
       "mssqlSrvProductName": mssqlSrvProductName,
       "mssqlSrvVersion": mssqlSrvVersion,
       "mssqlSrvContact": mssqlSrvContact,
       "mssqlSrvState": mssqlSrvState,
       "mssqlSrvInfoTable": mssqlSrvInfoTable,
       "mssqlSrvInfoEntry": mssqlSrvInfoEntry,
       "mssqlSrvInfoServerName": mssqlSrvInfoServerName,
       "mssqlSrvInfoStartupTime": mssqlSrvInfoStartupTime,
       "mssqlSrvInfoTrans": mssqlSrvInfoTrans,
       "mssqlSrvInfoPageReads": mssqlSrvInfoPageReads,
       "mssqlSrvInfoSinglePageWrites": mssqlSrvInfoSinglePageWrites,
       "mssqlSrvInfoBatchWrites": mssqlSrvInfoBatchWrites,
       "mssqlSrvInfoLazyWrites": mssqlSrvInfoLazyWrites,
       "mssqlSrvInfoLogWrites": mssqlSrvInfoLogWrites,
       "mssqlSrvInfoOutstandingReads": mssqlSrvInfoOutstandingReads,
       "mssqlSrvInfoOutstandingWrites": mssqlSrvInfoOutstandingWrites,
       "mssqlSrvInfoCacheHitRatio": mssqlSrvInfoCacheHitRatio,
       "mssqlSrvInfoFreeBuffers": mssqlSrvInfoFreeBuffers,
       "mssqlSrvInfoNetworkReads": mssqlSrvInfoNetworkReads,
       "mssqlSrvInfoNetworkWrites": mssqlSrvInfoNetworkWrites,
       "mssqlSrvInfoRAPhysicalReads": mssqlSrvInfoRAPhysicalReads,
       "mssqlSrvInfoUserConnections": mssqlSrvInfoUserConnections,
       "mssqlSrvInfoTotalLocks": mssqlSrvInfoTotalLocks,
       "mssqlSrvInfoTotalBlockingLocks": mssqlSrvInfoTotalBlockingLocks,
       "mssqlSrvInfoUsersBlocked": mssqlSrvInfoUsersBlocked,
       "mssqlSrvConfigParamTable": mssqlSrvConfigParamTable,
       "mssqlSrvConfigParamEntry": mssqlSrvConfigParamEntry,
       "mssqlSrvConfigParamName": mssqlSrvConfigParamName,
       "mssqlSrvConfigParamMax": mssqlSrvConfigParamMax,
       "mssqlSrvConfigParamMin": mssqlSrvConfigParamMin,
       "mssqlSrvConfigParamConfigValue": mssqlSrvConfigParamConfigValue,
       "mssqlSrvConfigParamRunValue": mssqlSrvConfigParamRunValue,
       "mssqlSrvDeviceTable": mssqlSrvDeviceTable,
       "mssqlSrvDeviceEntry": mssqlSrvDeviceEntry,
       "mssqlSrvDeviceLogicalName": mssqlSrvDeviceLogicalName,
       "mssqlSrvDevicePhysicalName": mssqlSrvDevicePhysicalName,
       "mssqlSrvDeviceDescription": mssqlSrvDeviceDescription,
       "mssqlDbTable": mssqlDbTable,
       "mssqlDbEntry": mssqlDbEntry,
       "mssqlDbId": mssqlDbId,
       "mssqlDbName": mssqlDbName,
       "mssqlDbState": mssqlDbState,
       "mssqlDbInfoTable": mssqlDbInfoTable,
       "mssqlDbInfoEntry": mssqlDbInfoEntry,
       "mssqlDbInfoDbId": mssqlDbInfoDbId,
       "mssqlDbInfoDbName": mssqlDbInfoDbName,
       "mssqlDbInfoCreationDateTime": mssqlDbInfoCreationDateTime,
       "mssqlDbInfoOwner": mssqlDbInfoOwner,
       "mssqlDbInfoSize": mssqlDbInfoSize,
       "mssqlDbInfoUnallocatedSpace": mssqlDbInfoUnallocatedSpace,
       "mssqlDbInfoReservedSpace": mssqlDbInfoReservedSpace,
       "mssqlDbInfoDataSpace": mssqlDbInfoDataSpace,
       "mssqlDbInfoIndexSpace": mssqlDbInfoIndexSpace,
       "mssqlDbInfoUnusedSpace": mssqlDbInfoUnusedSpace,
       "mssqlDbInfoLastTrLogDump": mssqlDbInfoLastTrLogDump,
       "mssqlDbInfoLogSize": mssqlDbInfoLogSize,
       "mssqlDbInfoLogSpaceUsed": mssqlDbInfoLogSpaceUsed,
       "mssqlDbOptionTable": mssqlDbOptionTable,
       "mssqlDbOptionEntry": mssqlDbOptionEntry,
       "mssqlDbOptionDbId": mssqlDbOptionDbId,
       "mssqlDbOptionDbName": mssqlDbOptionDbName,
       "mssqlDbOptionSetName": mssqlDbOptionSetName,
       "pysmiFakeCol1": pysmiFakeCol1,
       "mssqlDbDeviceTable": mssqlDbDeviceTable,
       "mssqlDbDeviceEntry": mssqlDbDeviceEntry,
       "mssqlDbDeviceDbId": mssqlDbDeviceDbId,
       "mssqlDbDeviceDbName": mssqlDbDeviceDbName,
       "mssqlDbDeviceFragmentName": mssqlDbDeviceFragmentName,
       "mssqlDbDeviceFragmentSize": mssqlDbDeviceFragmentSize,
       "mssqlDbDeviceFragmentUsage": mssqlDbDeviceFragmentUsage,
       "pysmiFakeCol2": pysmiFakeCol2}
)
