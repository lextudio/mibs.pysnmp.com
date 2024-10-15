# SNMP MIB module (BroadworksMaintenance) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BroadworksMaintenance
# Produced by pysmi-1.5.4 at Mon Oct 14 20:50:27 2024
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

broadsoft = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6431)
)
broadsoft.setRevisions(
        ("2006-06-09 09:30",
         "2006-03-23 19:35",
         "2005-08-16 10:00",
         "2000-09-19 14:31")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Broadworks_ObjectIdentity = ObjectIdentity
broadworks = _Broadworks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1)
)
_Common_ObjectIdentity = ObjectIdentity
common = _Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1)
)
_ManagedObjects_ObjectIdentity = ObjectIdentity
managedObjects = _ManagedObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2)
)
_MoServerModule_ObjectIdentity = ObjectIdentity
moServerModule = _MoServerModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1)
)
_BwServerType_Type = DisplayString
_BwServerType_Object = MibScalar
bwServerType = _BwServerType_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 1),
    _BwServerType_Type()
)
bwServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwServerType.setStatus("current")


class _BwRedundancyType_Type(Integer32):
    """Custom type bwRedundancyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRedundant", 0),
          ("primary", 1),
          ("seconday", 2))
    )


_BwRedundancyType_Type.__name__ = "Integer32"
_BwRedundancyType_Object = MibScalar
bwRedundancyType = _BwRedundancyType_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 2),
    _BwRedundancyType_Type()
)
bwRedundancyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwRedundancyType.setStatus("current")
_BwActiveSoftwareVersion_Type = DisplayString
_BwActiveSoftwareVersion_Object = MibScalar
bwActiveSoftwareVersion = _BwActiveSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 3),
    _BwActiveSoftwareVersion_Type()
)
bwActiveSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwActiveSoftwareVersion.setStatus("current")


class _BwAdminState_Type(Integer32):
    """Custom type bwAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("forceLock", 5),
          ("lock", 0),
          ("locking", 1),
          ("shuttingDown", 3),
          ("stopped", 4),
          ("unlock", 2))
    )


_BwAdminState_Type.__name__ = "Integer32"
_BwAdminState_Object = MibScalar
bwAdminState = _BwAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 4),
    _BwAdminState_Type()
)
bwAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAdminState.setStatus("current")


class _BwOperationalState_Type(Integer32):
    """Custom type bwOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_BwOperationalState_Type.__name__ = "Integer32"
_BwOperationalState_Object = MibScalar
bwOperationalState = _BwOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 5),
    _BwOperationalState_Type()
)
bwOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwOperationalState.setStatus("current")


class _BwResetServer_Type(Integer32):
    """Custom type bwResetServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hardReset", 2),
          ("hardRevertReset", 4),
          ("reset", 1),
          ("revertReset", 3),
          ("set", 0))
    )


_BwResetServer_Type.__name__ = "Integer32"
_BwResetServer_Object = MibScalar
bwResetServer = _BwResetServer_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 6),
    _BwResetServer_Type()
)
bwResetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwResetServer.setStatus("current")
_BwSubComponentTable_Object = MibTable
bwSubComponentTable = _BwSubComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7)
)
if mibBuilder.loadTexts:
    bwSubComponentTable.setStatus("current")
_BwSubComponentEntry_Object = MibTableRow
bwSubComponentEntry = _BwSubComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1)
)
bwSubComponentEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwSubComponentIndex"),
)
if mibBuilder.loadTexts:
    bwSubComponentEntry.setStatus("current")
_BwSubComponentIndex_Type = Unsigned32
_BwSubComponentIndex_Object = MibTableColumn
bwSubComponentIndex = _BwSubComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1, 1),
    _BwSubComponentIndex_Type()
)
bwSubComponentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSubComponentIndex.setStatus("current")
_BwSubComponentName_Type = DisplayString
_BwSubComponentName_Object = MibTableColumn
bwSubComponentName = _BwSubComponentName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1, 2),
    _BwSubComponentName_Type()
)
bwSubComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSubComponentName.setStatus("current")
_BwSubComponentInfo_Type = DisplayString
_BwSubComponentInfo_Object = MibTableColumn
bwSubComponentInfo = _BwSubComponentInfo_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 7, 1, 3),
    _BwSubComponentInfo_Type()
)
bwSubComponentInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSubComponentInfo.setStatus("current")
_BwTargetSoftwareVersion_Type = DisplayString
_BwTargetSoftwareVersion_Object = MibScalar
bwTargetSoftwareVersion = _BwTargetSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 8),
    _BwTargetSoftwareVersion_Type()
)
bwTargetSoftwareVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwTargetSoftwareVersion.setStatus("current")
_BwRevertBackupLocation_Type = DisplayString
_BwRevertBackupLocation_Object = MibScalar
bwRevertBackupLocation = _BwRevertBackupLocation_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 1, 9),
    _BwRevertBackupLocation_Type()
)
bwRevertBackupLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwRevertBackupLocation.setStatus("current")
_MoSoftwareVersionModule_ObjectIdentity = ObjectIdentity
moSoftwareVersionModule = _MoSoftwareVersionModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2)
)


class _BwUpdateSoftwareVersionTable_Type(Integer32):
    """Custom type bwUpdateSoftwareVersionTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reload", 1))
    )


_BwUpdateSoftwareVersionTable_Type.__name__ = "Integer32"
_BwUpdateSoftwareVersionTable_Object = MibScalar
bwUpdateSoftwareVersionTable = _BwUpdateSoftwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 1),
    _BwUpdateSoftwareVersionTable_Type()
)
bwUpdateSoftwareVersionTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwUpdateSoftwareVersionTable.setStatus("current")
_BwSoftwareVersionTable_Object = MibTable
bwSoftwareVersionTable = _BwSoftwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    bwSoftwareVersionTable.setStatus("current")
_BwSoftwareVersionEntry_Object = MibTableRow
bwSoftwareVersionEntry = _BwSoftwareVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1)
)
bwSoftwareVersionEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwSoftwareVersionIndex"),
)
if mibBuilder.loadTexts:
    bwSoftwareVersionEntry.setStatus("current")
_BwSoftwareVersionIndex_Type = Unsigned32
_BwSoftwareVersionIndex_Object = MibTableColumn
bwSoftwareVersionIndex = _BwSoftwareVersionIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 1),
    _BwSoftwareVersionIndex_Type()
)
bwSoftwareVersionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareVersionIndex.setStatus("current")
_BwSoftwareVersionName_Type = DisplayString
_BwSoftwareVersionName_Object = MibTableColumn
bwSoftwareVersionName = _BwSoftwareVersionName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 2),
    _BwSoftwareVersionName_Type()
)
bwSoftwareVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareVersionName.setStatus("current")
_BwSoftwareVersionInstallDate_Type = DisplayString
_BwSoftwareVersionInstallDate_Object = MibTableColumn
bwSoftwareVersionInstallDate = _BwSoftwareVersionInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 3),
    _BwSoftwareVersionInstallDate_Type()
)
bwSoftwareVersionInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareVersionInstallDate.setStatus("current")


class _BwSoftwareVersionStatus_Type(Integer32):
    """Custom type bwSoftwareVersionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("installed", 0))
    )


_BwSoftwareVersionStatus_Type.__name__ = "Integer32"
_BwSoftwareVersionStatus_Object = MibTableColumn
bwSoftwareVersionStatus = _BwSoftwareVersionStatus_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 2, 1, 4),
    _BwSoftwareVersionStatus_Type()
)
bwSoftwareVersionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareVersionStatus.setStatus("current")
_BwSoftwarePatchTable_Object = MibTable
bwSoftwarePatchTable = _BwSoftwarePatchTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    bwSoftwarePatchTable.setStatus("current")
_BwSoftwarePatchEntry_Object = MibTableRow
bwSoftwarePatchEntry = _BwSoftwarePatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1)
)
bwSoftwarePatchEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwSoftwarePatchIndex"),
)
if mibBuilder.loadTexts:
    bwSoftwarePatchEntry.setStatus("current")
_BwSoftwarePatchIndex_Type = Unsigned32
_BwSoftwarePatchIndex_Object = MibTableColumn
bwSoftwarePatchIndex = _BwSoftwarePatchIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 1),
    _BwSoftwarePatchIndex_Type()
)
bwSoftwarePatchIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchIndex.setStatus("current")
_BwSoftwarePatchVersionName_Type = DisplayString
_BwSoftwarePatchVersionName_Object = MibScalar
bwSoftwarePatchVersionName = _BwSoftwarePatchVersionName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 2),
    _BwSoftwarePatchVersionName_Type()
)
bwSoftwarePatchVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchVersionName.setStatus("obsolete")
_BwSoftwarePatchName_Type = DisplayString
_BwSoftwarePatchName_Object = MibTableColumn
bwSoftwarePatchName = _BwSoftwarePatchName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 3),
    _BwSoftwarePatchName_Type()
)
bwSoftwarePatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchName.setStatus("current")
_BwSoftwarePatchType_Type = DisplayString
_BwSoftwarePatchType_Object = MibScalar
bwSoftwarePatchType = _BwSoftwarePatchType_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 4),
    _BwSoftwarePatchType_Type()
)
bwSoftwarePatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchType.setStatus("obsolete")
_BwSoftwarePatchInstallDate_Type = DisplayString
_BwSoftwarePatchInstallDate_Object = MibTableColumn
bwSoftwarePatchInstallDate = _BwSoftwarePatchInstallDate_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 5),
    _BwSoftwarePatchInstallDate_Type()
)
bwSoftwarePatchInstallDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchInstallDate.setStatus("obsolete")


class _BwSoftwarePatchState_Type(Integer32):
    """Custom type bwSoftwarePatchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("activePendingInstalled", 3),
          ("deleted", 4),
          ("installed", 0),
          ("installedMissingDependencies", 5),
          ("installedPendingActive", 2))
    )


_BwSoftwarePatchState_Type.__name__ = "Integer32"
_BwSoftwarePatchState_Object = MibTableColumn
bwSoftwarePatchState = _BwSoftwarePatchState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 6),
    _BwSoftwarePatchState_Type()
)
bwSoftwarePatchState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchState.setStatus("current")


class _BwSoftwarePatchOperation_Type(Integer32):
    """Custom type bwSoftwarePatchOperation based on Integer32"""
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
        *(("apply", 1),
          ("delete", 3),
          ("none", 0),
          ("remove", 2))
    )


_BwSoftwarePatchOperation_Type.__name__ = "Integer32"
_BwSoftwarePatchOperation_Object = MibScalar
bwSoftwarePatchOperation = _BwSoftwarePatchOperation_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 7),
    _BwSoftwarePatchOperation_Type()
)
bwSoftwarePatchOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwSoftwarePatchOperation.setStatus("obsolete")
_BwSoftwarePatchBundle_Type = DisplayString
_BwSoftwarePatchBundle_Object = MibTableColumn
bwSoftwarePatchBundle = _BwSoftwarePatchBundle_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 3, 1, 8),
    _BwSoftwarePatchBundle_Type()
)
bwSoftwarePatchBundle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchBundle.setStatus("current")
_BwSoftwareThirdPartyTable_Object = MibTable
bwSoftwareThirdPartyTable = _BwSoftwareThirdPartyTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4)
)
if mibBuilder.loadTexts:
    bwSoftwareThirdPartyTable.setStatus("current")
_BwSoftwareThirdPartyEntry_Object = MibTableRow
bwSoftwareThirdPartyEntry = _BwSoftwareThirdPartyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1)
)
bwSoftwareThirdPartyEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwSoftwareThirdPartyIndex"),
)
if mibBuilder.loadTexts:
    bwSoftwareThirdPartyEntry.setStatus("current")
_BwSoftwareThirdPartyIndex_Type = Unsigned32
_BwSoftwareThirdPartyIndex_Object = MibTableColumn
bwSoftwareThirdPartyIndex = _BwSoftwareThirdPartyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 1),
    _BwSoftwareThirdPartyIndex_Type()
)
bwSoftwareThirdPartyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareThirdPartyIndex.setStatus("current")
_BwSoftwareThirdPartyName_Type = DisplayString
_BwSoftwareThirdPartyName_Object = MibTableColumn
bwSoftwareThirdPartyName = _BwSoftwareThirdPartyName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 2),
    _BwSoftwareThirdPartyName_Type()
)
bwSoftwareThirdPartyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareThirdPartyName.setStatus("current")
_BwSoftwareThirdPartyVersion_Type = DisplayString
_BwSoftwareThirdPartyVersion_Object = MibTableColumn
bwSoftwareThirdPartyVersion = _BwSoftwareThirdPartyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 3),
    _BwSoftwareThirdPartyVersion_Type()
)
bwSoftwareThirdPartyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareThirdPartyVersion.setStatus("current")


class _BwSoftwareThirdPartyStatus_Type(Integer32):
    """Custom type bwSoftwareThirdPartyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("installed", 0))
    )


_BwSoftwareThirdPartyStatus_Type.__name__ = "Integer32"
_BwSoftwareThirdPartyStatus_Object = MibTableColumn
bwSoftwareThirdPartyStatus = _BwSoftwareThirdPartyStatus_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 4, 1, 4),
    _BwSoftwareThirdPartyStatus_Type()
)
bwSoftwareThirdPartyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwareThirdPartyStatus.setStatus("current")
_BwSoftwarePatchHistoryTable_Object = MibTable
bwSoftwarePatchHistoryTable = _BwSoftwarePatchHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5)
)
if mibBuilder.loadTexts:
    bwSoftwarePatchHistoryTable.setStatus("current")
_BwSoftwarePatchHistoryEntry_Object = MibTableRow
bwSoftwarePatchHistoryEntry = _BwSoftwarePatchHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1)
)
bwSoftwarePatchHistoryEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwSoftwarePatchIndex"),
)
if mibBuilder.loadTexts:
    bwSoftwarePatchHistoryEntry.setStatus("current")
_BwSoftwarePatchHistoryIndex_Type = Unsigned32
_BwSoftwarePatchHistoryIndex_Object = MibTableColumn
bwSoftwarePatchHistoryIndex = _BwSoftwarePatchHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 1),
    _BwSoftwarePatchHistoryIndex_Type()
)
bwSoftwarePatchHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchHistoryIndex.setStatus("current")
_BwSoftwarePatchHistPatchName_Type = DisplayString
_BwSoftwarePatchHistPatchName_Object = MibTableColumn
bwSoftwarePatchHistPatchName = _BwSoftwarePatchHistPatchName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 2),
    _BwSoftwarePatchHistPatchName_Type()
)
bwSoftwarePatchHistPatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchHistPatchName.setStatus("current")
_BwSoftwarePatchHistTimeStamp_Type = DisplayString
_BwSoftwarePatchHistTimeStamp_Object = MibTableColumn
bwSoftwarePatchHistTimeStamp = _BwSoftwarePatchHistTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 3),
    _BwSoftwarePatchHistTimeStamp_Type()
)
bwSoftwarePatchHistTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchHistTimeStamp.setStatus("current")


class _BwSoftwarePatchHistNewState_Type(Integer32):
    """Custom type bwSoftwarePatchHistNewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("activePendingInstalled", 3),
          ("deleted", 4),
          ("installed", 0),
          ("installedMissingDependencies", 5),
          ("installedPendingActive", 2))
    )


_BwSoftwarePatchHistNewState_Type.__name__ = "Integer32"
_BwSoftwarePatchHistNewState_Object = MibTableColumn
bwSoftwarePatchHistNewState = _BwSoftwarePatchHistNewState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 5, 1, 4),
    _BwSoftwarePatchHistNewState_Type()
)
bwSoftwarePatchHistNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchHistNewState.setStatus("current")
_BwSoftwarePatchImpactedFileTable_Object = MibTable
bwSoftwarePatchImpactedFileTable = _BwSoftwarePatchImpactedFileTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6)
)
if mibBuilder.loadTexts:
    bwSoftwarePatchImpactedFileTable.setStatus("current")
_BwSoftwarePatchImpactedFileEntry_Object = MibTableRow
bwSoftwarePatchImpactedFileEntry = _BwSoftwarePatchImpactedFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1)
)
bwSoftwarePatchImpactedFileEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwSoftwarePatchIndex"),
)
if mibBuilder.loadTexts:
    bwSoftwarePatchImpactedFileEntry.setStatus("current")
_BwSoftwarePatchImpactedFileIndex_Type = Unsigned32
_BwSoftwarePatchImpactedFileIndex_Object = MibTableColumn
bwSoftwarePatchImpactedFileIndex = _BwSoftwarePatchImpactedFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1, 1),
    _BwSoftwarePatchImpactedFileIndex_Type()
)
bwSoftwarePatchImpactedFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchImpactedFileIndex.setStatus("current")
_BwSoftwarePatchImpactedFilePatchName_Type = DisplayString
_BwSoftwarePatchImpactedFilePatchName_Object = MibTableColumn
bwSoftwarePatchImpactedFilePatchName = _BwSoftwarePatchImpactedFilePatchName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1, 2),
    _BwSoftwarePatchImpactedFilePatchName_Type()
)
bwSoftwarePatchImpactedFilePatchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchImpactedFilePatchName.setStatus("current")
_BwSoftwarePatchImpactedFileFileName_Type = DisplayString
_BwSoftwarePatchImpactedFileFileName_Object = MibTableColumn
bwSoftwarePatchImpactedFileFileName = _BwSoftwarePatchImpactedFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 2, 6, 1, 3),
    _BwSoftwarePatchImpactedFileFileName_Type()
)
bwSoftwarePatchImpactedFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwSoftwarePatchImpactedFileFileName.setStatus("current")
_MoDeviceModule_ObjectIdentity = ObjectIdentity
moDeviceModule = _MoDeviceModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3)
)
_BwManagedObjectsTable_Object = MibTable
bwManagedObjectsTable = _BwManagedObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    bwManagedObjectsTable.setStatus("current")
_BwManagedObjectsEntry_Object = MibTableRow
bwManagedObjectsEntry = _BwManagedObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1)
)
bwManagedObjectsEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwManagedObjectsIndex"),
)
if mibBuilder.loadTexts:
    bwManagedObjectsEntry.setStatus("current")
_BwManagedObjectsIndex_Type = Unsigned32
_BwManagedObjectsIndex_Object = MibTableColumn
bwManagedObjectsIndex = _BwManagedObjectsIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 1),
    _BwManagedObjectsIndex_Type()
)
bwManagedObjectsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwManagedObjectsIndex.setStatus("current")
_BwManagedObjectsName_Type = DisplayString
_BwManagedObjectsName_Object = MibTableColumn
bwManagedObjectsName = _BwManagedObjectsName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 2),
    _BwManagedObjectsName_Type()
)
bwManagedObjectsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwManagedObjectsName.setStatus("current")
_BwManagedObjectsProtocol_Type = DisplayString
_BwManagedObjectsProtocol_Object = MibTableColumn
bwManagedObjectsProtocol = _BwManagedObjectsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 3),
    _BwManagedObjectsProtocol_Type()
)
bwManagedObjectsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwManagedObjectsProtocol.setStatus("current")
_BwManagedObjectsType_Type = DisplayString
_BwManagedObjectsType_Object = MibTableColumn
bwManagedObjectsType = _BwManagedObjectsType_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 4),
    _BwManagedObjectsType_Type()
)
bwManagedObjectsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwManagedObjectsType.setStatus("current")


class _BwManagedObjectsAdminState_Type(Integer32):
    """Custom type bwManagedObjectsAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 0),
          ("locking", 1),
          ("unlock", 2))
    )


_BwManagedObjectsAdminState_Type.__name__ = "Integer32"
_BwManagedObjectsAdminState_Object = MibTableColumn
bwManagedObjectsAdminState = _BwManagedObjectsAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 5),
    _BwManagedObjectsAdminState_Type()
)
bwManagedObjectsAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwManagedObjectsAdminState.setStatus("current")


class _BwManagedObjectsOperationalState_Type(Integer32):
    """Custom type bwManagedObjectsOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 0))
    )


_BwManagedObjectsOperationalState_Type.__name__ = "Integer32"
_BwManagedObjectsOperationalState_Object = MibTableColumn
bwManagedObjectsOperationalState = _BwManagedObjectsOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 2, 3, 1, 1, 6),
    _BwManagedObjectsOperationalState_Type()
)
bwManagedObjectsOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwManagedObjectsOperationalState.setStatus("current")
_Thresholds_ObjectIdentity = ObjectIdentity
thresholds = _Thresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3)
)
_ThCounterModule_ObjectIdentity = ObjectIdentity
thCounterModule = _ThCounterModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1)
)
_BwCounterThresholdTable_Object = MibTable
bwCounterThresholdTable = _BwCounterThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bwCounterThresholdTable.setStatus("current")
_BwCounterThresholdEntry_Object = MibTableRow
bwCounterThresholdEntry = _BwCounterThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1)
)
bwCounterThresholdEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwCounterThresholdIndex"),
)
if mibBuilder.loadTexts:
    bwCounterThresholdEntry.setStatus("current")
_BwCounterThresholdIndex_Type = Unsigned32
_BwCounterThresholdIndex_Object = MibTableColumn
bwCounterThresholdIndex = _BwCounterThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 1),
    _BwCounterThresholdIndex_Type()
)
bwCounterThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCounterThresholdIndex.setStatus("current")
_BwCounterThresholdDescription_Type = DisplayString
_BwCounterThresholdDescription_Object = MibTableColumn
bwCounterThresholdDescription = _BwCounterThresholdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 2),
    _BwCounterThresholdDescription_Type()
)
bwCounterThresholdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCounterThresholdDescription.setStatus("current")
_BwCounterThresholdName_Type = DisplayString
_BwCounterThresholdName_Object = MibTableColumn
bwCounterThresholdName = _BwCounterThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 3),
    _BwCounterThresholdName_Type()
)
bwCounterThresholdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCounterThresholdName.setStatus("current")
_BwCounterThresholdInitialValue_Type = Integer32
_BwCounterThresholdInitialValue_Object = MibTableColumn
bwCounterThresholdInitialValue = _BwCounterThresholdInitialValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 4),
    _BwCounterThresholdInitialValue_Type()
)
bwCounterThresholdInitialValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCounterThresholdInitialValue.setStatus("current")
_BwCounterThresholdOffsetValue_Type = Integer32
_BwCounterThresholdOffsetValue_Object = MibTableColumn
bwCounterThresholdOffsetValue = _BwCounterThresholdOffsetValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 5),
    _BwCounterThresholdOffsetValue_Type()
)
bwCounterThresholdOffsetValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCounterThresholdOffsetValue.setStatus("current")
_BwCounterThresholdCurrentValue_Type = Gauge32
_BwCounterThresholdCurrentValue_Object = MibTableColumn
bwCounterThresholdCurrentValue = _BwCounterThresholdCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 6),
    _BwCounterThresholdCurrentValue_Type()
)
bwCounterThresholdCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwCounterThresholdCurrentValue.setStatus("current")


class _BwCounterThresholdSeverity_Type(Integer32):
    """Custom type bwCounterThresholdSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("high", 3),
          ("informational", 0),
          ("low", 1),
          ("medium", 2))
    )


_BwCounterThresholdSeverity_Type.__name__ = "Integer32"
_BwCounterThresholdSeverity_Object = MibTableColumn
bwCounterThresholdSeverity = _BwCounterThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 7),
    _BwCounterThresholdSeverity_Type()
)
bwCounterThresholdSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCounterThresholdSeverity.setStatus("current")


class _BwCounterThresholdControl_Type(Integer32):
    """Custom type bwCounterThresholdControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 3),
          ("delete", 2),
          ("inactive", 0),
          ("invalid", 4))
    )


_BwCounterThresholdControl_Type.__name__ = "Integer32"
_BwCounterThresholdControl_Object = MibTableColumn
bwCounterThresholdControl = _BwCounterThresholdControl_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 1, 1, 1, 8),
    _BwCounterThresholdControl_Type()
)
bwCounterThresholdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwCounterThresholdControl.setStatus("current")
_ThGaugeModule_ObjectIdentity = ObjectIdentity
thGaugeModule = _ThGaugeModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2)
)
_BwGaugeThresholdTable_Object = MibTable
bwGaugeThresholdTable = _BwGaugeThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bwGaugeThresholdTable.setStatus("current")
_BwGaugeThresholdEntry_Object = MibTableRow
bwGaugeThresholdEntry = _BwGaugeThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1)
)
bwGaugeThresholdEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwGaugeThresholdIndex"),
)
if mibBuilder.loadTexts:
    bwGaugeThresholdEntry.setStatus("current")
_BwGaugeThresholdIndex_Type = Unsigned32
_BwGaugeThresholdIndex_Object = MibTableColumn
bwGaugeThresholdIndex = _BwGaugeThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 1),
    _BwGaugeThresholdIndex_Type()
)
bwGaugeThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwGaugeThresholdIndex.setStatus("current")
_BwGaugeThresholdDescription_Type = DisplayString
_BwGaugeThresholdDescription_Object = MibTableColumn
bwGaugeThresholdDescription = _BwGaugeThresholdDescription_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 2),
    _BwGaugeThresholdDescription_Type()
)
bwGaugeThresholdDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGaugeThresholdDescription.setStatus("current")
_BwGaugeThresholdName_Type = DisplayString
_BwGaugeThresholdName_Object = MibTableColumn
bwGaugeThresholdName = _BwGaugeThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 3),
    _BwGaugeThresholdName_Type()
)
bwGaugeThresholdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGaugeThresholdName.setStatus("current")
_BwGaugeThresholdNotifyLow_Type = Integer32
_BwGaugeThresholdNotifyLow_Object = MibTableColumn
bwGaugeThresholdNotifyLow = _BwGaugeThresholdNotifyLow_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 4),
    _BwGaugeThresholdNotifyLow_Type()
)
bwGaugeThresholdNotifyLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGaugeThresholdNotifyLow.setStatus("current")
_BwGaugeThresholdNotifyHigh_Type = Integer32
_BwGaugeThresholdNotifyHigh_Object = MibTableColumn
bwGaugeThresholdNotifyHigh = _BwGaugeThresholdNotifyHigh_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 5),
    _BwGaugeThresholdNotifyHigh_Type()
)
bwGaugeThresholdNotifyHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGaugeThresholdNotifyHigh.setStatus("current")


class _BwGaugeThresholdSeverity_Type(Integer32):
    """Custom type bwGaugeThresholdSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("high", 3),
          ("informational", 0),
          ("low", 1),
          ("medium", 2))
    )


_BwGaugeThresholdSeverity_Type.__name__ = "Integer32"
_BwGaugeThresholdSeverity_Object = MibTableColumn
bwGaugeThresholdSeverity = _BwGaugeThresholdSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 6),
    _BwGaugeThresholdSeverity_Type()
)
bwGaugeThresholdSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGaugeThresholdSeverity.setStatus("current")


class _BwGaugeThresholdControl_Type(Integer32):
    """Custom type bwGaugeThresholdControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 3),
          ("delete", 2),
          ("inactive", 0),
          ("invalid", 4))
    )


_BwGaugeThresholdControl_Type.__name__ = "Integer32"
_BwGaugeThresholdControl_Object = MibTableColumn
bwGaugeThresholdControl = _BwGaugeThresholdControl_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 2, 1, 1, 7),
    _BwGaugeThresholdControl_Type()
)
bwGaugeThresholdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwGaugeThresholdControl.setStatus("current")
_ThAlarmModule_ObjectIdentity = ObjectIdentity
thAlarmModule = _ThAlarmModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3)
)
_BwAlarmThresholdTable_Object = MibTable
bwAlarmThresholdTable = _BwAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    bwAlarmThresholdTable.setStatus("current")
_BwAlarmThresholdEntry_Object = MibTableRow
bwAlarmThresholdEntry = _BwAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1)
)
bwAlarmThresholdEntry.setIndexNames(
    (0, "BroadworksMaintenance", "bwAlarmThresholdIndex"),
)
if mibBuilder.loadTexts:
    bwAlarmThresholdEntry.setStatus("current")
_BwAlarmThresholdIndex_Type = Unsigned32
_BwAlarmThresholdIndex_Object = MibTableColumn
bwAlarmThresholdIndex = _BwAlarmThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 1),
    _BwAlarmThresholdIndex_Type()
)
bwAlarmThresholdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwAlarmThresholdIndex.setStatus("current")
_BwAlarmThresholdName_Type = DisplayString
_BwAlarmThresholdName_Object = MibTableColumn
bwAlarmThresholdName = _BwAlarmThresholdName_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 2),
    _BwAlarmThresholdName_Type()
)
bwAlarmThresholdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdName.setStatus("current")
_BwAlarmThresholdMaxNumTrapsPerTimePeriod_Type = Integer32
_BwAlarmThresholdMaxNumTrapsPerTimePeriod_Object = MibTableColumn
bwAlarmThresholdMaxNumTrapsPerTimePeriod = _BwAlarmThresholdMaxNumTrapsPerTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 3),
    _BwAlarmThresholdMaxNumTrapsPerTimePeriod_Type()
)
bwAlarmThresholdMaxNumTrapsPerTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdMaxNumTrapsPerTimePeriod.setStatus("current")
_BwAlarmThresholdTimePeriodInSeconds_Type = Integer32
_BwAlarmThresholdTimePeriodInSeconds_Object = MibTableColumn
bwAlarmThresholdTimePeriodInSeconds = _BwAlarmThresholdTimePeriodInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 4),
    _BwAlarmThresholdTimePeriodInSeconds_Type()
)
bwAlarmThresholdTimePeriodInSeconds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdTimePeriodInSeconds.setStatus("current")
_BwAlarmThresholdProblemTextVarNum1_Type = Integer32
_BwAlarmThresholdProblemTextVarNum1_Object = MibTableColumn
bwAlarmThresholdProblemTextVarNum1 = _BwAlarmThresholdProblemTextVarNum1_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 5),
    _BwAlarmThresholdProblemTextVarNum1_Type()
)
bwAlarmThresholdProblemTextVarNum1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdProblemTextVarNum1.setStatus("current")
_BwAlarmThresholdProblemTextVarNum2_Type = Integer32
_BwAlarmThresholdProblemTextVarNum2_Object = MibTableColumn
bwAlarmThresholdProblemTextVarNum2 = _BwAlarmThresholdProblemTextVarNum2_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 6),
    _BwAlarmThresholdProblemTextVarNum2_Type()
)
bwAlarmThresholdProblemTextVarNum2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdProblemTextVarNum2.setStatus("current")
_BwAlarmThresholdProblemTextVarNum3_Type = Integer32
_BwAlarmThresholdProblemTextVarNum3_Object = MibTableColumn
bwAlarmThresholdProblemTextVarNum3 = _BwAlarmThresholdProblemTextVarNum3_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 7),
    _BwAlarmThresholdProblemTextVarNum3_Type()
)
bwAlarmThresholdProblemTextVarNum3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdProblemTextVarNum3.setStatus("current")
_BwAlarmThresholdProblemTextVarNum4_Type = Integer32
_BwAlarmThresholdProblemTextVarNum4_Object = MibTableColumn
bwAlarmThresholdProblemTextVarNum4 = _BwAlarmThresholdProblemTextVarNum4_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 8),
    _BwAlarmThresholdProblemTextVarNum4_Type()
)
bwAlarmThresholdProblemTextVarNum4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdProblemTextVarNum4.setStatus("current")
_BwAlarmThresholdProblemTextVarNum5_Type = Integer32
_BwAlarmThresholdProblemTextVarNum5_Object = MibTableColumn
bwAlarmThresholdProblemTextVarNum5 = _BwAlarmThresholdProblemTextVarNum5_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 9),
    _BwAlarmThresholdProblemTextVarNum5_Type()
)
bwAlarmThresholdProblemTextVarNum5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdProblemTextVarNum5.setStatus("current")


class _BwAlarmThresholdMinimumSeverity_Type(Integer32):
    """Custom type bwAlarmThresholdMinimumSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 4),
          ("high", 3),
          ("informational", 0),
          ("low", 1),
          ("medium", 2))
    )


_BwAlarmThresholdMinimumSeverity_Type.__name__ = "Integer32"
_BwAlarmThresholdMinimumSeverity_Object = MibTableColumn
bwAlarmThresholdMinimumSeverity = _BwAlarmThresholdMinimumSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 10),
    _BwAlarmThresholdMinimumSeverity_Type()
)
bwAlarmThresholdMinimumSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdMinimumSeverity.setStatus("current")


class _BwAlarmThresholdControl_Type(Integer32):
    """Custom type bwAlarmThresholdControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("create", 3),
          ("delete", 2),
          ("inactive", 0),
          ("invalid", 4))
    )


_BwAlarmThresholdControl_Type.__name__ = "Integer32"
_BwAlarmThresholdControl_Object = MibTableColumn
bwAlarmThresholdControl = _BwAlarmThresholdControl_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 3, 3, 1, 1, 11),
    _BwAlarmThresholdControl_Type()
)
bwAlarmThresholdControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bwAlarmThresholdControl.setStatus("current")
_ReservedModule_ObjectIdentity = ObjectIdentity
reservedModule = _ReservedModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 10)
)


class _BwReservedScalar_Type(Integer32):
    """Custom type bwReservedScalar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("notUsed", 0)
    )


_BwReservedScalar_Type.__name__ = "Integer32"
_BwReservedScalar_Object = MibScalar
bwReservedScalar = _BwReservedScalar_Object(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 10, 1),
    _BwReservedScalar_Type()
)
bwReservedScalar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bwReservedScalar.setStatus("current")
_BwMtcMibConformance_ObjectIdentity = ObjectIdentity
bwMtcMibConformance = _BwMtcMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20)
)
_BwMtcMibGroups_ObjectIdentity = ObjectIdentity
bwMtcMibGroups = _BwMtcMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1)
)
_BwMtcMibCompliancy_ObjectIdentity = ObjectIdentity
bwMtcMibCompliancy = _BwMtcMibCompliancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 2)
)

# Managed Objects groups

bwMoServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 1)
)
bwMoServerGroup.setObjects(
      *(("BroadworksMaintenance", "bwServerType"),
        ("BroadworksMaintenance", "bwRedundancyType"),
        ("BroadworksMaintenance", "bwActiveSoftwareVersion"),
        ("BroadworksMaintenance", "bwAdminState"),
        ("BroadworksMaintenance", "bwOperationalState"),
        ("BroadworksMaintenance", "bwResetServer"),
        ("BroadworksMaintenance", "bwSubComponentTable"),
        ("BroadworksMaintenance", "bwTargetSoftwareVersion"),
        ("BroadworksMaintenance", "bwSubComponentIndex"),
        ("BroadworksMaintenance", "bwSubComponentName"),
        ("BroadworksMaintenance", "bwSubComponentInfo"))
)
if mibBuilder.loadTexts:
    bwMoServerGroup.setStatus("current")

bwMoSoftwareVersionsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 2)
)
bwMoSoftwareVersionsGroup.setObjects(
      *(("BroadworksMaintenance", "bwUpdateSoftwareVersionTable"),
        ("BroadworksMaintenance", "bwSoftwareVersionTable"),
        ("BroadworksMaintenance", "bwSoftwarePatchTable"),
        ("BroadworksMaintenance", "bwSoftwareThirdPartyTable"),
        ("BroadworksMaintenance", "bwSoftwareVersionIndex"),
        ("BroadworksMaintenance", "bwSoftwareVersionName"),
        ("BroadworksMaintenance", "bwSoftwareVersionInstallDate"),
        ("BroadworksMaintenance", "bwSoftwareVersionStatus"),
        ("BroadworksMaintenance", "bwSoftwarePatchIndex"),
        ("BroadworksMaintenance", "bwSoftwarePatchName"),
        ("BroadworksMaintenance", "bwSoftwarePatchInstallDate"),
        ("BroadworksMaintenance", "bwSoftwarePatchState"),
        ("BroadworksMaintenance", "bwSoftwarePatchBundle"),
        ("BroadworksMaintenance", "bwSoftwareThirdPartyIndex"),
        ("BroadworksMaintenance", "bwSoftwareThirdPartyName"),
        ("BroadworksMaintenance", "bwSoftwareThirdPartyVersion"),
        ("BroadworksMaintenance", "bwSoftwareThirdPartyStatus"),
        ("BroadworksMaintenance", "bwSoftwarePatchHistoryTable"),
        ("BroadworksMaintenance", "bwSoftwarePatchHistoryIndex"),
        ("BroadworksMaintenance", "bwSoftwarePatchHistPatchName"),
        ("BroadworksMaintenance", "bwSoftwarePatchHistTimeStamp"),
        ("BroadworksMaintenance", "bwSoftwarePatchHistNewState"),
        ("BroadworksMaintenance", "bwSoftwarePatchImpactedFileTable"),
        ("BroadworksMaintenance", "bwSoftwarePatchImpactedFileIndex"),
        ("BroadworksMaintenance", "bwSoftwarePatchImpactedFilePatchName"),
        ("BroadworksMaintenance", "bwSoftwarePatchImpactedFileFileName"))
)
if mibBuilder.loadTexts:
    bwMoSoftwareVersionsGroup.setStatus("current")

bwMoDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 3)
)
bwMoDeviceGroup.setObjects(
      *(("BroadworksMaintenance", "bwManagedObjectsTable"),
        ("BroadworksMaintenance", "bwManagedObjectsIndex"),
        ("BroadworksMaintenance", "bwManagedObjectsName"),
        ("BroadworksMaintenance", "bwManagedObjectsProtocol"),
        ("BroadworksMaintenance", "bwManagedObjectsType"),
        ("BroadworksMaintenance", "bwManagedObjectsAdminState"),
        ("BroadworksMaintenance", "bwManagedObjectsOperationalState"))
)
if mibBuilder.loadTexts:
    bwMoDeviceGroup.setStatus("current")

bwMoThresholdsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 4)
)
bwMoThresholdsGroup.setObjects(
      *(("BroadworksMaintenance", "bwCounterThresholdTable"),
        ("BroadworksMaintenance", "bwCounterThresholdIndex"),
        ("BroadworksMaintenance", "bwCounterThresholdDescription"),
        ("BroadworksMaintenance", "bwCounterThresholdName"),
        ("BroadworksMaintenance", "bwCounterThresholdInitialValue"),
        ("BroadworksMaintenance", "bwCounterThresholdOffsetValue"),
        ("BroadworksMaintenance", "bwCounterThresholdCurrentValue"),
        ("BroadworksMaintenance", "bwCounterThresholdSeverity"),
        ("BroadworksMaintenance", "bwCounterThresholdControl"),
        ("BroadworksMaintenance", "bwGaugeThresholdTable"),
        ("BroadworksMaintenance", "bwGaugeThresholdIndex"),
        ("BroadworksMaintenance", "bwGaugeThresholdDescription"),
        ("BroadworksMaintenance", "bwGaugeThresholdName"),
        ("BroadworksMaintenance", "bwGaugeThresholdNotifyLow"),
        ("BroadworksMaintenance", "bwGaugeThresholdNotifyHigh"),
        ("BroadworksMaintenance", "bwGaugeThresholdSeverity"),
        ("BroadworksMaintenance", "bwGaugeThresholdControl"),
        ("BroadworksMaintenance", "bwAlarmThresholdTable"),
        ("BroadworksMaintenance", "bwAlarmThresholdIndex"),
        ("BroadworksMaintenance", "bwAlarmThresholdName"),
        ("BroadworksMaintenance", "bwAlarmThresholdMaxNumTrapsPerTimePeriod"),
        ("BroadworksMaintenance", "bwAlarmThresholdTimePeriodInSeconds"),
        ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum1"),
        ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum2"),
        ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum3"),
        ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum4"),
        ("BroadworksMaintenance", "bwAlarmThresholdProblemTextVarNum5"),
        ("BroadworksMaintenance", "bwAlarmThresholdMinimumSeverity"),
        ("BroadworksMaintenance", "bwAlarmThresholdControl"))
)
if mibBuilder.loadTexts:
    bwMoThresholdsGroup.setStatus("current")

bwMoReserveGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 1, 10)
)
bwMoReserveGroup.setObjects(
    ("BroadworksMaintenance", "bwReservedScalar")
)
if mibBuilder.loadTexts:
    bwMoReserveGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bwMoBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6431, 1, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    bwMoBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BroadworksMaintenance",
    **{"broadsoft": broadsoft,
       "broadworks": broadworks,
       "common": common,
       "managedObjects": managedObjects,
       "moServerModule": moServerModule,
       "bwServerType": bwServerType,
       "bwRedundancyType": bwRedundancyType,
       "bwActiveSoftwareVersion": bwActiveSoftwareVersion,
       "bwAdminState": bwAdminState,
       "bwOperationalState": bwOperationalState,
       "bwResetServer": bwResetServer,
       "bwSubComponentTable": bwSubComponentTable,
       "bwSubComponentEntry": bwSubComponentEntry,
       "bwSubComponentIndex": bwSubComponentIndex,
       "bwSubComponentName": bwSubComponentName,
       "bwSubComponentInfo": bwSubComponentInfo,
       "bwTargetSoftwareVersion": bwTargetSoftwareVersion,
       "bwRevertBackupLocation": bwRevertBackupLocation,
       "moSoftwareVersionModule": moSoftwareVersionModule,
       "bwUpdateSoftwareVersionTable": bwUpdateSoftwareVersionTable,
       "bwSoftwareVersionTable": bwSoftwareVersionTable,
       "bwSoftwareVersionEntry": bwSoftwareVersionEntry,
       "bwSoftwareVersionIndex": bwSoftwareVersionIndex,
       "bwSoftwareVersionName": bwSoftwareVersionName,
       "bwSoftwareVersionInstallDate": bwSoftwareVersionInstallDate,
       "bwSoftwareVersionStatus": bwSoftwareVersionStatus,
       "bwSoftwarePatchTable": bwSoftwarePatchTable,
       "bwSoftwarePatchEntry": bwSoftwarePatchEntry,
       "bwSoftwarePatchIndex": bwSoftwarePatchIndex,
       "bwSoftwarePatchVersionName": bwSoftwarePatchVersionName,
       "bwSoftwarePatchName": bwSoftwarePatchName,
       "bwSoftwarePatchType": bwSoftwarePatchType,
       "bwSoftwarePatchInstallDate": bwSoftwarePatchInstallDate,
       "bwSoftwarePatchState": bwSoftwarePatchState,
       "bwSoftwarePatchOperation": bwSoftwarePatchOperation,
       "bwSoftwarePatchBundle": bwSoftwarePatchBundle,
       "bwSoftwareThirdPartyTable": bwSoftwareThirdPartyTable,
       "bwSoftwareThirdPartyEntry": bwSoftwareThirdPartyEntry,
       "bwSoftwareThirdPartyIndex": bwSoftwareThirdPartyIndex,
       "bwSoftwareThirdPartyName": bwSoftwareThirdPartyName,
       "bwSoftwareThirdPartyVersion": bwSoftwareThirdPartyVersion,
       "bwSoftwareThirdPartyStatus": bwSoftwareThirdPartyStatus,
       "bwSoftwarePatchHistoryTable": bwSoftwarePatchHistoryTable,
       "bwSoftwarePatchHistoryEntry": bwSoftwarePatchHistoryEntry,
       "bwSoftwarePatchHistoryIndex": bwSoftwarePatchHistoryIndex,
       "bwSoftwarePatchHistPatchName": bwSoftwarePatchHistPatchName,
       "bwSoftwarePatchHistTimeStamp": bwSoftwarePatchHistTimeStamp,
       "bwSoftwarePatchHistNewState": bwSoftwarePatchHistNewState,
       "bwSoftwarePatchImpactedFileTable": bwSoftwarePatchImpactedFileTable,
       "bwSoftwarePatchImpactedFileEntry": bwSoftwarePatchImpactedFileEntry,
       "bwSoftwarePatchImpactedFileIndex": bwSoftwarePatchImpactedFileIndex,
       "bwSoftwarePatchImpactedFilePatchName": bwSoftwarePatchImpactedFilePatchName,
       "bwSoftwarePatchImpactedFileFileName": bwSoftwarePatchImpactedFileFileName,
       "moDeviceModule": moDeviceModule,
       "bwManagedObjectsTable": bwManagedObjectsTable,
       "bwManagedObjectsEntry": bwManagedObjectsEntry,
       "bwManagedObjectsIndex": bwManagedObjectsIndex,
       "bwManagedObjectsName": bwManagedObjectsName,
       "bwManagedObjectsProtocol": bwManagedObjectsProtocol,
       "bwManagedObjectsType": bwManagedObjectsType,
       "bwManagedObjectsAdminState": bwManagedObjectsAdminState,
       "bwManagedObjectsOperationalState": bwManagedObjectsOperationalState,
       "thresholds": thresholds,
       "thCounterModule": thCounterModule,
       "bwCounterThresholdTable": bwCounterThresholdTable,
       "bwCounterThresholdEntry": bwCounterThresholdEntry,
       "bwCounterThresholdIndex": bwCounterThresholdIndex,
       "bwCounterThresholdDescription": bwCounterThresholdDescription,
       "bwCounterThresholdName": bwCounterThresholdName,
       "bwCounterThresholdInitialValue": bwCounterThresholdInitialValue,
       "bwCounterThresholdOffsetValue": bwCounterThresholdOffsetValue,
       "bwCounterThresholdCurrentValue": bwCounterThresholdCurrentValue,
       "bwCounterThresholdSeverity": bwCounterThresholdSeverity,
       "bwCounterThresholdControl": bwCounterThresholdControl,
       "thGaugeModule": thGaugeModule,
       "bwGaugeThresholdTable": bwGaugeThresholdTable,
       "bwGaugeThresholdEntry": bwGaugeThresholdEntry,
       "bwGaugeThresholdIndex": bwGaugeThresholdIndex,
       "bwGaugeThresholdDescription": bwGaugeThresholdDescription,
       "bwGaugeThresholdName": bwGaugeThresholdName,
       "bwGaugeThresholdNotifyLow": bwGaugeThresholdNotifyLow,
       "bwGaugeThresholdNotifyHigh": bwGaugeThresholdNotifyHigh,
       "bwGaugeThresholdSeverity": bwGaugeThresholdSeverity,
       "bwGaugeThresholdControl": bwGaugeThresholdControl,
       "thAlarmModule": thAlarmModule,
       "bwAlarmThresholdTable": bwAlarmThresholdTable,
       "bwAlarmThresholdEntry": bwAlarmThresholdEntry,
       "bwAlarmThresholdIndex": bwAlarmThresholdIndex,
       "bwAlarmThresholdName": bwAlarmThresholdName,
       "bwAlarmThresholdMaxNumTrapsPerTimePeriod": bwAlarmThresholdMaxNumTrapsPerTimePeriod,
       "bwAlarmThresholdTimePeriodInSeconds": bwAlarmThresholdTimePeriodInSeconds,
       "bwAlarmThresholdProblemTextVarNum1": bwAlarmThresholdProblemTextVarNum1,
       "bwAlarmThresholdProblemTextVarNum2": bwAlarmThresholdProblemTextVarNum2,
       "bwAlarmThresholdProblemTextVarNum3": bwAlarmThresholdProblemTextVarNum3,
       "bwAlarmThresholdProblemTextVarNum4": bwAlarmThresholdProblemTextVarNum4,
       "bwAlarmThresholdProblemTextVarNum5": bwAlarmThresholdProblemTextVarNum5,
       "bwAlarmThresholdMinimumSeverity": bwAlarmThresholdMinimumSeverity,
       "bwAlarmThresholdControl": bwAlarmThresholdControl,
       "reservedModule": reservedModule,
       "bwReservedScalar": bwReservedScalar,
       "bwMtcMibConformance": bwMtcMibConformance,
       "bwMtcMibGroups": bwMtcMibGroups,
       "bwMoServerGroup": bwMoServerGroup,
       "bwMoSoftwareVersionsGroup": bwMoSoftwareVersionsGroup,
       "bwMoDeviceGroup": bwMoDeviceGroup,
       "bwMoThresholdsGroup": bwMoThresholdsGroup,
       "bwMoReserveGroup": bwMoReserveGroup,
       "bwMtcMibCompliancy": bwMtcMibCompliancy,
       "bwMoBasicCompliance": bwMoBasicCompliance}
)
