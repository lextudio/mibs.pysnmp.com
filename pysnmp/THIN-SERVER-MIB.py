# SNMP MIB module (THIN-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/THIN-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:31 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IbmThinServer_ObjectIdentity = ObjectIdentity
ibmThinServer = _IbmThinServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3)
)
_GenInfo_ObjectIdentity = ObjectIdentity
genInfo = _GenInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1)
)


class _ThinserverEnable_Type(Integer32):
    """Custom type thinserverEnable based on Integer32"""
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
        *(("disabled", 0),
          ("disabledpending", 3),
          ("enabled", 1),
          ("passthru", 2))
    )


_ThinserverEnable_Type.__name__ = "Integer32"
_ThinserverEnable_Object = MibScalar
thinserverEnable = _ThinserverEnable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 1),
    _ThinserverEnable_Type()
)
thinserverEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverEnable.setStatus("mandatory")
_ThinserverRefreshInterval_Type = Integer32
_ThinserverRefreshInterval_Object = MibScalar
thinserverRefreshInterval = _ThinserverRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 2),
    _ThinserverRefreshInterval_Type()
)
thinserverRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverRefreshInterval.setStatus("mandatory")
_ThinserverRefreshTime_Type = DisplayString
_ThinserverRefreshTime_Object = MibScalar
thinserverRefreshTime = _ThinserverRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 3),
    _ThinserverRefreshTime_Type()
)
thinserverRefreshTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverRefreshTime.setStatus("mandatory")


class _ThinserverRefreshNow_Type(Integer32):
    """Custom type thinserverRefreshNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("refreshnow", 2))
    )


_ThinserverRefreshNow_Type.__name__ = "Integer32"
_ThinserverRefreshNow_Object = MibScalar
thinserverRefreshNow = _ThinserverRefreshNow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 4),
    _ThinserverRefreshNow_Type()
)
thinserverRefreshNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverRefreshNow.setStatus("mandatory")
_ThinserverMemory_Type = Integer32
_ThinserverMemory_Object = MibScalar
thinserverMemory = _ThinserverMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 5),
    _ThinserverMemory_Type()
)
thinserverMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverMemory.setStatus("mandatory")
_ThinserverHardFileSpace_Type = Integer32
_ThinserverHardFileSpace_Object = MibScalar
thinserverHardFileSpace = _ThinserverHardFileSpace_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 6),
    _ThinserverHardFileSpace_Type()
)
thinserverHardFileSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverHardFileSpace.setStatus("mandatory")
_ThinserverHardFileUsed_Type = Gauge32
_ThinserverHardFileUsed_Object = MibScalar
thinserverHardFileUsed = _ThinserverHardFileUsed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 7),
    _ThinserverHardFileUsed_Type()
)
thinserverHardFileUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverHardFileUsed.setStatus("mandatory")
_ThinserverNumFilesCached_Type = Gauge32
_ThinserverNumFilesCached_Object = MibScalar
thinserverNumFilesCached = _ThinserverNumFilesCached_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 8),
    _ThinserverNumFilesCached_Type()
)
thinserverNumFilesCached.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNumFilesCached.setStatus("mandatory")
_ThinserverMasterServerIPAddress_Type = IpAddress
_ThinserverMasterServerIPAddress_Object = MibScalar
thinserverMasterServerIPAddress = _ThinserverMasterServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 9),
    _ThinserverMasterServerIPAddress_Type()
)
thinserverMasterServerIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverMasterServerIPAddress.setStatus("mandatory")


class _ThinserverSyncProtocol_Type(Integer32):
    """Custom type thinserverSyncProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nfs", 2),
          ("rfs400", 1))
    )


_ThinserverSyncProtocol_Type.__name__ = "Integer32"
_ThinserverSyncProtocol_Object = MibScalar
thinserverSyncProtocol = _ThinserverSyncProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 10),
    _ThinserverSyncProtocol_Type()
)
thinserverSyncProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverSyncProtocol.setStatus("mandatory")


class _ThinserverPreloadListName_Type(DisplayString):
    """Custom type thinserverPreloadListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ThinserverPreloadListName_Type.__name__ = "DisplayString"
_ThinserverPreloadListName_Object = MibScalar
thinserverPreloadListName = _ThinserverPreloadListName_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 11),
    _ThinserverPreloadListName_Type()
)
thinserverPreloadListName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverPreloadListName.setStatus("mandatory")
_ThinserverMountPointsTable_Object = MibTable
thinserverMountPointsTable = _ThinserverMountPointsTable_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12)
)
if mibBuilder.loadTexts:
    thinserverMountPointsTable.setStatus("mandatory")
_ThinserverMountPointsEntry_Object = MibTableRow
thinserverMountPointsEntry = _ThinserverMountPointsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1)
)
thinserverMountPointsEntry.setIndexNames(
    (0, "THIN-SERVER-MIB", "thinserverMountPointsIndex"),
)
if mibBuilder.loadTexts:
    thinserverMountPointsEntry.setStatus("mandatory")
_ThinserverMountPointsIndex_Type = Integer32
_ThinserverMountPointsIndex_Object = MibTableColumn
thinserverMountPointsIndex = _ThinserverMountPointsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1, 1),
    _ThinserverMountPointsIndex_Type()
)
thinserverMountPointsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    thinserverMountPointsIndex.setStatus("mandatory")


class _ThinserverMountPointsDescr_Type(DisplayString):
    """Custom type thinserverMountPointsDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ThinserverMountPointsDescr_Type.__name__ = "DisplayString"
_ThinserverMountPointsDescr_Object = MibTableColumn
thinserverMountPointsDescr = _ThinserverMountPointsDescr_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1, 2),
    _ThinserverMountPointsDescr_Type()
)
thinserverMountPointsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverMountPointsDescr.setStatus("mandatory")


class _ThinserverMountPointsScope_Type(Integer32):
    """Custom type thinserverMountPointsScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("include", 1))
    )


_ThinserverMountPointsScope_Type.__name__ = "Integer32"
_ThinserverMountPointsScope_Object = MibTableColumn
thinserverMountPointsScope = _ThinserverMountPointsScope_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 12, 1, 3),
    _ThinserverMountPointsScope_Type()
)
thinserverMountPointsScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverMountPointsScope.setStatus("mandatory")
_ThinserverPacketTimeout_Type = Integer32
_ThinserverPacketTimeout_Object = MibScalar
thinserverPacketTimeout = _ThinserverPacketTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 13),
    _ThinserverPacketTimeout_Type()
)
thinserverPacketTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverPacketTimeout.setStatus("mandatory")
_ThinserverMaxRetries_Type = Integer32
_ThinserverMaxRetries_Object = MibScalar
thinserverMaxRetries = _ThinserverMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 14),
    _ThinserverMaxRetries_Type()
)
thinserverMaxRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverMaxRetries.setStatus("mandatory")
_ThinserverMaxSegSize_Type = Integer32
_ThinserverMaxSegSize_Object = MibScalar
thinserverMaxSegSize = _ThinserverMaxSegSize_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 15),
    _ThinserverMaxSegSize_Type()
)
thinserverMaxSegSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverMaxSegSize.setStatus("mandatory")
_ThinserverUseHardFile_Type = TruthValue
_ThinserverUseHardFile_Object = MibScalar
thinserverUseHardFile = _ThinserverUseHardFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 16),
    _ThinserverUseHardFile_Type()
)
thinserverUseHardFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverUseHardFile.setStatus("mandatory")


class _ThinserverRestartNow_Type(Integer32):
    """Custom type thinserverRestartNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("restartnow", 2))
    )


_ThinserverRestartNow_Type.__name__ = "Integer32"
_ThinserverRestartNow_Object = MibScalar
thinserverRestartNow = _ThinserverRestartNow_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 17),
    _ThinserverRestartNow_Type()
)
thinserverRestartNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverRestartNow.setStatus("mandatory")
_ThinserverConfiguredMemory_Type = Integer32
_ThinserverConfiguredMemory_Object = MibScalar
thinserverConfiguredMemory = _ThinserverConfiguredMemory_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 1, 18),
    _ThinserverConfiguredMemory_Type()
)
thinserverConfiguredMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverConfiguredMemory.setStatus("mandatory")
_GenStat_ObjectIdentity = ObjectIdentity
genStat = _GenStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2)
)
_ThinserverFilesOpenCurrently_Type = Gauge32
_ThinserverFilesOpenCurrently_Object = MibScalar
thinserverFilesOpenCurrently = _ThinserverFilesOpenCurrently_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 1),
    _ThinserverFilesOpenCurrently_Type()
)
thinserverFilesOpenCurrently.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverFilesOpenCurrently.setStatus("mandatory")
_ThinserverTotalFileOpens_Type = Counter32
_ThinserverTotalFileOpens_Object = MibScalar
thinserverTotalFileOpens = _ThinserverTotalFileOpens_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 2),
    _ThinserverTotalFileOpens_Type()
)
thinserverTotalFileOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverTotalFileOpens.setStatus("mandatory")
_ThinserverReadMissesDirty_Type = Counter32
_ThinserverReadMissesDirty_Object = MibScalar
thinserverReadMissesDirty = _ThinserverReadMissesDirty_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 3),
    _ThinserverReadMissesDirty_Type()
)
thinserverReadMissesDirty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverReadMissesDirty.setStatus("mandatory")
_ThinserverReadMissesNotPresent_Type = Counter32
_ThinserverReadMissesNotPresent_Object = MibScalar
thinserverReadMissesNotPresent = _ThinserverReadMissesNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 4),
    _ThinserverReadMissesNotPresent_Type()
)
thinserverReadMissesNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverReadMissesNotPresent.setStatus("mandatory")
_ThinserverOpenFailsFileLocked_Type = Counter32
_ThinserverOpenFailsFileLocked_Object = MibScalar
thinserverOpenFailsFileLocked = _ThinserverOpenFailsFileLocked_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 5),
    _ThinserverOpenFailsFileLocked_Type()
)
thinserverOpenFailsFileLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverOpenFailsFileLocked.setStatus("mandatory")
_ThinserverNoRoomOnHardFile_Type = Counter32
_ThinserverNoRoomOnHardFile_Object = MibScalar
thinserverNoRoomOnHardFile = _ThinserverNoRoomOnHardFile_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 6),
    _ThinserverNoRoomOnHardFile_Type()
)
thinserverNoRoomOnHardFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNoRoomOnHardFile.setStatus("mandatory")


class _ThinserverResetGenCounters_Type(Integer32):
    """Custom type thinserverResetGenCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("resetnow", 2))
    )


_ThinserverResetGenCounters_Type.__name__ = "Integer32"
_ThinserverResetGenCounters_Object = MibScalar
thinserverResetGenCounters = _ThinserverResetGenCounters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 2, 7),
    _ThinserverResetGenCounters_Type()
)
thinserverResetGenCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverResetGenCounters.setStatus("mandatory")
_MsConnStats_ObjectIdentity = ObjectIdentity
msConnStats = _MsConnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3)
)
_ThinserverNumRefreshes_Type = Counter32
_ThinserverNumRefreshes_Object = MibScalar
thinserverNumRefreshes = _ThinserverNumRefreshes_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 1),
    _ThinserverNumRefreshes_Type()
)
thinserverNumRefreshes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNumRefreshes.setStatus("mandatory")
_ThinserverNumRefreshFail_Type = Counter32
_ThinserverNumRefreshFail_Object = MibScalar
thinserverNumRefreshFail = _ThinserverNumRefreshFail_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 2),
    _ThinserverNumRefreshFail_Type()
)
thinserverNumRefreshFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNumRefreshFail.setStatus("mandatory")
_ThinserverNumFilesRefreshed_Type = Counter32
_ThinserverNumFilesRefreshed_Object = MibScalar
thinserverNumFilesRefreshed = _ThinserverNumFilesRefreshed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 3),
    _ThinserverNumFilesRefreshed_Type()
)
thinserverNumFilesRefreshed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNumFilesRefreshed.setStatus("mandatory")
_ThinserverLastFileUpdate_Type = DisplayString
_ThinserverLastFileUpdate_Object = MibScalar
thinserverLastFileUpdate = _ThinserverLastFileUpdate_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 4),
    _ThinserverLastFileUpdate_Type()
)
thinserverLastFileUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverLastFileUpdate.setStatus("mandatory")


class _ThinserverResetMSConnStats_Type(Integer32):
    """Custom type thinserverResetMSConnStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("resetnow", 2))
    )


_ThinserverResetMSConnStats_Type.__name__ = "Integer32"
_ThinserverResetMSConnStats_Object = MibScalar
thinserverResetMSConnStats = _ThinserverResetMSConnStats_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 3, 5),
    _ThinserverResetMSConnStats_Type()
)
thinserverResetMSConnStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverResetMSConnStats.setStatus("mandatory")
_RfsStat_ObjectIdentity = ObjectIdentity
rfsStat = _RfsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4)
)
_ThinserverRFSTotalClients_Type = Counter32
_ThinserverRFSTotalClients_Object = MibScalar
thinserverRFSTotalClients = _ThinserverRFSTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 1),
    _ThinserverRFSTotalClients_Type()
)
thinserverRFSTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverRFSTotalClients.setStatus("mandatory")
_ThinserverRFSCurrentClients_Type = Gauge32
_ThinserverRFSCurrentClients_Object = MibScalar
thinserverRFSCurrentClients = _ThinserverRFSCurrentClients_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 2),
    _ThinserverRFSCurrentClients_Type()
)
thinserverRFSCurrentClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverRFSCurrentClients.setStatus("mandatory")
_ThinserverRFSFilesServed_Type = Counter32
_ThinserverRFSFilesServed_Object = MibScalar
thinserverRFSFilesServed = _ThinserverRFSFilesServed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 3),
    _ThinserverRFSFilesServed_Type()
)
thinserverRFSFilesServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverRFSFilesServed.setStatus("mandatory")
_ThinserverRFSFilesServedByMS_Type = Counter32
_ThinserverRFSFilesServedByMS_Object = MibScalar
thinserverRFSFilesServedByMS = _ThinserverRFSFilesServedByMS_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 4),
    _ThinserverRFSFilesServedByMS_Type()
)
thinserverRFSFilesServedByMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverRFSFilesServedByMS.setStatus("mandatory")
_ThinserverNum449Accepts_Type = Counter32
_ThinserverNum449Accepts_Object = MibScalar
thinserverNum449Accepts = _ThinserverNum449Accepts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 5),
    _ThinserverNum449Accepts_Type()
)
thinserverNum449Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNum449Accepts.setStatus("mandatory")
_ThinserverNum449ConnsActive_Type = Gauge32
_ThinserverNum449ConnsActive_Object = MibScalar
thinserverNum449ConnsActive = _ThinserverNum449ConnsActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 6),
    _ThinserverNum449ConnsActive_Type()
)
thinserverNum449ConnsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNum449ConnsActive.setStatus("mandatory")
_ThinserverNum8473Accepts_Type = Counter32
_ThinserverNum8473Accepts_Object = MibScalar
thinserverNum8473Accepts = _ThinserverNum8473Accepts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 7),
    _ThinserverNum8473Accepts_Type()
)
thinserverNum8473Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNum8473Accepts.setStatus("mandatory")
_ThinserverNum8473ConnsActive_Type = Gauge32
_ThinserverNum8473ConnsActive_Object = MibScalar
thinserverNum8473ConnsActive = _ThinserverNum8473ConnsActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 8),
    _ThinserverNum8473ConnsActive_Type()
)
thinserverNum8473ConnsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNum8473ConnsActive.setStatus("mandatory")
_ThinserverNum8476Accepts_Type = Counter32
_ThinserverNum8476Accepts_Object = MibScalar
thinserverNum8476Accepts = _ThinserverNum8476Accepts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 9),
    _ThinserverNum8476Accepts_Type()
)
thinserverNum8476Accepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNum8476Accepts.setStatus("mandatory")
_ThinserverNum8476ConnsActive_Type = Gauge32
_ThinserverNum8476ConnsActive_Object = MibScalar
thinserverNum8476ConnsActive = _ThinserverNum8476ConnsActive_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 10),
    _ThinserverNum8476ConnsActive_Type()
)
thinserverNum8476ConnsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNum8476ConnsActive.setStatus("mandatory")
_ThinserverNumRFSWrites_Type = Counter32
_ThinserverNumRFSWrites_Object = MibScalar
thinserverNumRFSWrites = _ThinserverNumRFSWrites_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 11),
    _ThinserverNumRFSWrites_Type()
)
thinserverNumRFSWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNumRFSWrites.setStatus("mandatory")


class _ThinserverResetRFSCounters_Type(Integer32):
    """Custom type thinserverResetRFSCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("resetnow", 2))
    )


_ThinserverResetRFSCounters_Type.__name__ = "Integer32"
_ThinserverResetRFSCounters_Object = MibScalar
thinserverResetRFSCounters = _ThinserverResetRFSCounters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 4, 12),
    _ThinserverResetRFSCounters_Type()
)
thinserverResetRFSCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverResetRFSCounters.setStatus("mandatory")
_TftpStat_ObjectIdentity = ObjectIdentity
tftpStat = _TftpStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5)
)
_ThinserverTFTPTotalClients_Type = Counter32
_ThinserverTFTPTotalClients_Object = MibScalar
thinserverTFTPTotalClients = _ThinserverTFTPTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 1),
    _ThinserverTFTPTotalClients_Type()
)
thinserverTFTPTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverTFTPTotalClients.setStatus("mandatory")
_ThinserverTFTPCurrentClients_Type = Gauge32
_ThinserverTFTPCurrentClients_Object = MibScalar
thinserverTFTPCurrentClients = _ThinserverTFTPCurrentClients_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 2),
    _ThinserverTFTPCurrentClients_Type()
)
thinserverTFTPCurrentClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverTFTPCurrentClients.setStatus("mandatory")
_ThinserverTFTPFileisServed_Type = Counter32
_ThinserverTFTPFileisServed_Object = MibScalar
thinserverTFTPFileisServed = _ThinserverTFTPFileisServed_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 3),
    _ThinserverTFTPFileisServed_Type()
)
thinserverTFTPFileisServed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverTFTPFileisServed.setStatus("mandatory")
_ThinserverTFTPFilesServedByMS_Type = Counter32
_ThinserverTFTPFilesServedByMS_Object = MibScalar
thinserverTFTPFilesServedByMS = _ThinserverTFTPFilesServedByMS_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 4),
    _ThinserverTFTPFilesServedByMS_Type()
)
thinserverTFTPFilesServedByMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverTFTPFilesServedByMS.setStatus("mandatory")


class _ThinserverResetTFTPCounters_Type(Integer32):
    """Custom type thinserverResetTFTPCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("resetnow", 2))
    )


_ThinserverResetTFTPCounters_Type.__name__ = "Integer32"
_ThinserverResetTFTPCounters_Object = MibScalar
thinserverResetTFTPCounters = _ThinserverResetTFTPCounters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 5, 5),
    _ThinserverResetTFTPCounters_Type()
)
thinserverResetTFTPCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverResetTFTPCounters.setStatus("mandatory")
_NfsStat_ObjectIdentity = ObjectIdentity
nfsStat = _NfsStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6)
)
_ThinserverNFSDReadRequests_Type = Counter32
_ThinserverNFSDReadRequests_Object = MibScalar
thinserverNFSDReadRequests = _ThinserverNFSDReadRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 1),
    _ThinserverNFSDReadRequests_Type()
)
thinserverNFSDReadRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNFSDReadRequests.setStatus("mandatory")
_ThinserverNFSDReadDirRequests_Type = Counter32
_ThinserverNFSDReadDirRequests_Object = MibScalar
thinserverNFSDReadDirRequests = _ThinserverNFSDReadDirRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 2),
    _ThinserverNFSDReadDirRequests_Type()
)
thinserverNFSDReadDirRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNFSDReadDirRequests.setStatus("mandatory")
_ThinserverNFSDUnsupportedRequests_Type = Counter32
_ThinserverNFSDUnsupportedRequests_Object = MibScalar
thinserverNFSDUnsupportedRequests = _ThinserverNFSDUnsupportedRequests_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 3),
    _ThinserverNFSDUnsupportedRequests_Type()
)
thinserverNFSDUnsupportedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNFSDUnsupportedRequests.setStatus("mandatory")
_ThinserverNFSDTotalMounts_Type = Counter32
_ThinserverNFSDTotalMounts_Object = MibScalar
thinserverNFSDTotalMounts = _ThinserverNFSDTotalMounts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 4),
    _ThinserverNFSDTotalMounts_Type()
)
thinserverNFSDTotalMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNFSDTotalMounts.setStatus("mandatory")
_ThinserverNFSDCurrentMounts_Type = Gauge32
_ThinserverNFSDCurrentMounts_Object = MibScalar
thinserverNFSDCurrentMounts = _ThinserverNFSDCurrentMounts_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 5),
    _ThinserverNFSDCurrentMounts_Type()
)
thinserverNFSDCurrentMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNFSDCurrentMounts.setStatus("mandatory")
_ThinserverNFSDTotalClients_Type = Counter32
_ThinserverNFSDTotalClients_Object = MibScalar
thinserverNFSDTotalClients = _ThinserverNFSDTotalClients_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 6),
    _ThinserverNFSDTotalClients_Type()
)
thinserverNFSDTotalClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNFSDTotalClients.setStatus("mandatory")
_ThinserverNFSDCurrentClients_Type = Gauge32
_ThinserverNFSDCurrentClients_Object = MibScalar
thinserverNFSDCurrentClients = _ThinserverNFSDCurrentClients_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 7),
    _ThinserverNFSDCurrentClients_Type()
)
thinserverNFSDCurrentClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thinserverNFSDCurrentClients.setStatus("mandatory")


class _ThinserverNFSDResetCounters_Type(Integer32):
    """Custom type thinserverNFSDResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noaction", 1),
          ("resetnow", 2))
    )


_ThinserverNFSDResetCounters_Type.__name__ = "Integer32"
_ThinserverNFSDResetCounters_Object = MibScalar
thinserverNFSDResetCounters = _ThinserverNFSDResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 119, 2, 3, 6, 8),
    _ThinserverNFSDResetCounters_Type()
)
thinserverNFSDResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thinserverNFSDResetCounters.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "THIN-SERVER-MIB",
    **{"ibmThinServer": ibmThinServer,
       "genInfo": genInfo,
       "thinserverEnable": thinserverEnable,
       "thinserverRefreshInterval": thinserverRefreshInterval,
       "thinserverRefreshTime": thinserverRefreshTime,
       "thinserverRefreshNow": thinserverRefreshNow,
       "thinserverMemory": thinserverMemory,
       "thinserverHardFileSpace": thinserverHardFileSpace,
       "thinserverHardFileUsed": thinserverHardFileUsed,
       "thinserverNumFilesCached": thinserverNumFilesCached,
       "thinserverMasterServerIPAddress": thinserverMasterServerIPAddress,
       "thinserverSyncProtocol": thinserverSyncProtocol,
       "thinserverPreloadListName": thinserverPreloadListName,
       "thinserverMountPointsTable": thinserverMountPointsTable,
       "thinserverMountPointsEntry": thinserverMountPointsEntry,
       "thinserverMountPointsIndex": thinserverMountPointsIndex,
       "thinserverMountPointsDescr": thinserverMountPointsDescr,
       "thinserverMountPointsScope": thinserverMountPointsScope,
       "thinserverPacketTimeout": thinserverPacketTimeout,
       "thinserverMaxRetries": thinserverMaxRetries,
       "thinserverMaxSegSize": thinserverMaxSegSize,
       "thinserverUseHardFile": thinserverUseHardFile,
       "thinserverRestartNow": thinserverRestartNow,
       "thinserverConfiguredMemory": thinserverConfiguredMemory,
       "genStat": genStat,
       "thinserverFilesOpenCurrently": thinserverFilesOpenCurrently,
       "thinserverTotalFileOpens": thinserverTotalFileOpens,
       "thinserverReadMissesDirty": thinserverReadMissesDirty,
       "thinserverReadMissesNotPresent": thinserverReadMissesNotPresent,
       "thinserverOpenFailsFileLocked": thinserverOpenFailsFileLocked,
       "thinserverNoRoomOnHardFile": thinserverNoRoomOnHardFile,
       "thinserverResetGenCounters": thinserverResetGenCounters,
       "msConnStats": msConnStats,
       "thinserverNumRefreshes": thinserverNumRefreshes,
       "thinserverNumRefreshFail": thinserverNumRefreshFail,
       "thinserverNumFilesRefreshed": thinserverNumFilesRefreshed,
       "thinserverLastFileUpdate": thinserverLastFileUpdate,
       "thinserverResetMSConnStats": thinserverResetMSConnStats,
       "rfsStat": rfsStat,
       "thinserverRFSTotalClients": thinserverRFSTotalClients,
       "thinserverRFSCurrentClients": thinserverRFSCurrentClients,
       "thinserverRFSFilesServed": thinserverRFSFilesServed,
       "thinserverRFSFilesServedByMS": thinserverRFSFilesServedByMS,
       "thinserverNum449Accepts": thinserverNum449Accepts,
       "thinserverNum449ConnsActive": thinserverNum449ConnsActive,
       "thinserverNum8473Accepts": thinserverNum8473Accepts,
       "thinserverNum8473ConnsActive": thinserverNum8473ConnsActive,
       "thinserverNum8476Accepts": thinserverNum8476Accepts,
       "thinserverNum8476ConnsActive": thinserverNum8476ConnsActive,
       "thinserverNumRFSWrites": thinserverNumRFSWrites,
       "thinserverResetRFSCounters": thinserverResetRFSCounters,
       "tftpStat": tftpStat,
       "thinserverTFTPTotalClients": thinserverTFTPTotalClients,
       "thinserverTFTPCurrentClients": thinserverTFTPCurrentClients,
       "thinserverTFTPFileisServed": thinserverTFTPFileisServed,
       "thinserverTFTPFilesServedByMS": thinserverTFTPFilesServedByMS,
       "thinserverResetTFTPCounters": thinserverResetTFTPCounters,
       "nfsStat": nfsStat,
       "thinserverNFSDReadRequests": thinserverNFSDReadRequests,
       "thinserverNFSDReadDirRequests": thinserverNFSDReadDirRequests,
       "thinserverNFSDUnsupportedRequests": thinserverNFSDUnsupportedRequests,
       "thinserverNFSDTotalMounts": thinserverNFSDTotalMounts,
       "thinserverNFSDCurrentMounts": thinserverNFSDCurrentMounts,
       "thinserverNFSDTotalClients": thinserverNFSDTotalClients,
       "thinserverNFSDCurrentClients": thinserverNFSDCurrentClients,
       "thinserverNFSDResetCounters": thinserverNFSDResetCounters}
)
