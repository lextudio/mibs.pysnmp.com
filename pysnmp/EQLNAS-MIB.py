# SNMP MIB module (EQLNAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EQLNAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:08 2024
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

(eqlApplianceIndex,
 eqlApplianceNetworkID,
 eqlApplianceNetworkType) = mibBuilder.importSymbols(
    "EQLAPPLIANCE-MIB",
    "eqlApplianceIndex",
    "eqlApplianceNetworkID",
    "eqlApplianceNetworkType")

(SiteIndex,
 SiteIndexOrZero,
 StatusDisabledDefault,
 eqliscsiVolumeReplSiteIndex) = mibBuilder.importSymbols(
    "EQLVOLUME-MIB",
    "SiteIndex",
    "SiteIndexOrZero",
    "StatusDisabledDefault",
    "eqliscsiVolumeReplSiteIndex")

(equalLogic,) = mibBuilder.importSymbols(
    "EQUALLOGIC-SMI",
    "equalLogic")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eqlNASModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 18)
)
eqlNASModule.setRevisions(
        ("2009-07-13 00:00",)
)


# Types definitions



class EqlNASReplicationStatus(Integer32):
    """Custom type EqlNASReplicationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("cancelled", 6),
          ("cancelling", 11),
          ("deleting", 8),
          ("demoting", 15),
          ("failed", 4),
          ("finished", 10),
          ("idle", 1),
          ("idlewaittoschedule", 14),
          ("paused", 5),
          ("pausing", 9),
          ("promoted", 12),
          ("promoting", 13),
          ("resuming", 7),
          ("unknown", 0),
          ("waitingretry", 3))
    )





class EqlNASChassisComponentStatus(Integer32):
    """Custom type EqlNASChassisComponentStatus based on Integer32"""
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
        *(("critical", 2),
          ("not-available", 3),
          ("not-optimal", 1),
          ("optimal", 0))
    )





class EqlNASChassisACPowerStatus(Integer32):
    """Custom type EqlNASChassisACPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 2),
          ("partial", 1),
          ("redundant", 0))
    )





class EqlNASChassisControllerState(Integer32):
    """Custom type EqlNASChassisControllerState based on Integer32"""
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
        *(("detached", 3),
          ("down", 4),
          ("formatted", 2),
          ("not-available", 5),
          ("standby", 0),
          ("unformatted", 1))
    )





class EqlNASChassisSanType(Integer32):
    """Custom type EqlNASChassisSanType based on Integer32"""
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
        *(("eql", 1),
          ("fc", 2),
          ("iscsi", 0),
          ("not-available", 3))
    )





class EqlNASChassisNetworkSpeed(Integer32):
    """Custom type EqlNASChassisNetworkSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("eight-gb-fibre-channel", 6),
          ("four-gb-fibre-channel", 5),
          ("not-available", 7),
          ("one-gb-ethernet", 0),
          ("one-gb-fibre-channel", 3),
          ("ten-gb-ethernet", 1),
          ("twenty-gb-ethernet", 2),
          ("two-gb-fibre-channel", 4))
    )





class EqlNASChassisControllerLocation(Integer32):
    """Custom type EqlNASChassisControllerLocation based on Integer32"""
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
        *(("irrelevant", 2),
          ("not-available", 3),
          ("one", 0),
          ("two", 1))
    )





class EqlNASReplicationError(Integer32):
    """Custom type EqlNASReplicationError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("config", 4),
          ("dest-repl-disabled", 19),
          ("disconnected", 1),
          ("fs-down", 3),
          ("fs-pri-not-available-threads", 16),
          ("fs-pri-not-optimal", 14),
          ("fs-sec-not-available-threads", 17),
          ("fs-sec-not-optimal", 15),
          ("internal", 2),
          ("jumbo-frame", 18),
          ("no-base-found", 11),
          ("no-space", 9),
          ("none", 0),
          ("not-sec", 5),
          ("pri-vol-reclaim", 12),
          ("sec-busy", 6),
          ("sec-cur-not-empty", 10),
          ("sec-fs-down", 7),
          ("sec-vol-reclaim", 13),
          ("snap-clone-base", 20),
          ("versions-dont-match", 8))
    )





class EqlNASReplicationRole(Integer32):
    """Custom type EqlNASReplicationRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("destination", 2),
          ("source", 1),
          ("unknown", 0))
    )




# TEXTUAL-CONVENTIONS



class UNIXPermissions(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "o"


class ClusterNameType(OctetString, TextualConvention):
    status = "current"
    displayHint = "t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class ClusterIdType(OctetString, TextualConvention):
    status = "current"
    displayHint = "t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )



class CertificateType(OctetString, TextualConvention):
    status = "current"
    displayHint = "t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1750),
    )



class NASContainerNameType(OctetString, TextualConvention):
    status = "current"
    displayHint = "t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )



# MIB Managed Objects in the order of their OIDs

_EqlNASObjects_ObjectIdentity = ObjectIdentity
eqlNASObjects = _EqlNASObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1)
)
_EqlNASApplianceTable_Object = MibTable
eqlNASApplianceTable = _EqlNASApplianceTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 1)
)
if mibBuilder.loadTexts:
    eqlNASApplianceTable.setStatus("current")
_EqlNASApplianceEntry_Object = MibTableRow
eqlNASApplianceEntry = _EqlNASApplianceEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 1, 1)
)
eqlNASApplianceEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlNASApplianceEntry.setStatus("current")
_EqlNASApplianceRowStatus_Type = RowStatus
_EqlNASApplianceRowStatus_Object = MibTableColumn
eqlNASApplianceRowStatus = _EqlNASApplianceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 1, 1, 1),
    _EqlNASApplianceRowStatus_Type()
)
eqlNASApplianceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceRowStatus.setStatus("current")
_EqlNASAppliancePoolSize_Type = Unsigned32
_EqlNASAppliancePoolSize_Object = MibTableColumn
eqlNASAppliancePoolSize = _EqlNASAppliancePoolSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 1, 1, 2),
    _EqlNASAppliancePoolSize_Type()
)
eqlNASAppliancePoolSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASAppliancePoolSize.setStatus("current")
_EqlNASApplianceEQLPoolIndex_Type = Unsigned32
_EqlNASApplianceEQLPoolIndex_Object = MibTableColumn
eqlNASApplianceEQLPoolIndex = _EqlNASApplianceEQLPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 1, 1, 3),
    _EqlNASApplianceEQLPoolIndex_Type()
)
eqlNASApplianceEQLPoolIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceEQLPoolIndex.setStatus("current")


class _EqlNASApplianceReplRemoteUserName_Type(OctetString):
    """Custom type eqlNASApplianceReplRemoteUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlNASApplianceReplRemoteUserName_Type.__name__ = "OctetString"
_EqlNASApplianceReplRemoteUserName_Object = MibTableColumn
eqlNASApplianceReplRemoteUserName = _EqlNASApplianceReplRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 1, 1, 4),
    _EqlNASApplianceReplRemoteUserName_Type()
)
eqlNASApplianceReplRemoteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASApplianceReplRemoteUserName.setStatus("current")


class _EqlNASApplianceNFSv4Mode_Type(Integer32):
    """Custom type eqlNASApplianceNFSv4Mode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_EqlNASApplianceNFSv4Mode_Type.__name__ = "Integer32"
_EqlNASApplianceNFSv4Mode_Object = MibTableColumn
eqlNASApplianceNFSv4Mode = _EqlNASApplianceNFSv4Mode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 1, 1, 5),
    _EqlNASApplianceNFSv4Mode_Type()
)
eqlNASApplianceNFSv4Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSv4Mode.setStatus("current")
_EqlNASContainerTable_Object = MibTable
eqlNASContainerTable = _EqlNASContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3)
)
if mibBuilder.loadTexts:
    eqlNASContainerTable.setStatus("current")
_EqlNASContainerEntry_Object = MibTableRow
eqlNASContainerEntry = _EqlNASContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1)
)
eqlNASContainerEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
)
if mibBuilder.loadTexts:
    eqlNASContainerEntry.setStatus("current")
_EqlNASContainerIndex_Type = Unsigned32
_EqlNASContainerIndex_Object = MibTableColumn
eqlNASContainerIndex = _EqlNASContainerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 1),
    _EqlNASContainerIndex_Type()
)
eqlNASContainerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASContainerIndex.setStatus("current")
_EqlNASContainerRowStatus_Type = RowStatus
_EqlNASContainerRowStatus_Object = MibTableColumn
eqlNASContainerRowStatus = _EqlNASContainerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 2),
    _EqlNASContainerRowStatus_Type()
)
eqlNASContainerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerRowStatus.setStatus("current")


class _EqlNASContainerName_Type(OctetString):
    """Custom type eqlNASContainerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASContainerName_Type.__name__ = "OctetString"
_EqlNASContainerName_Object = MibTableColumn
eqlNASContainerName = _EqlNASContainerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 3),
    _EqlNASContainerName_Type()
)
eqlNASContainerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerName.setStatus("current")
_EqlNASContainerCapacity_Type = Unsigned32
_EqlNASContainerCapacity_Object = MibTableColumn
eqlNASContainerCapacity = _EqlNASContainerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 4),
    _EqlNASContainerCapacity_Type()
)
eqlNASContainerCapacity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASContainerCapacity.setUnits("MB")
_EqlNASContainerUsedSpaceAlert_Type = Unsigned32
_EqlNASContainerUsedSpaceAlert_Object = MibTableColumn
eqlNASContainerUsedSpaceAlert = _EqlNASContainerUsedSpaceAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 5),
    _EqlNASContainerUsedSpaceAlert_Type()
)
eqlNASContainerUsedSpaceAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerUsedSpaceAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASContainerUsedSpaceAlert.setUnits("%")
_EqlNASContainerSnapshotHardQuota_Type = Unsigned32
_EqlNASContainerSnapshotHardQuota_Object = MibTableColumn
eqlNASContainerSnapshotHardQuota = _EqlNASContainerSnapshotHardQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 6),
    _EqlNASContainerSnapshotHardQuota_Type()
)
eqlNASContainerSnapshotHardQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerSnapshotHardQuota.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASContainerSnapshotHardQuota.setUnits("%")
_EqlNASContainerSnapshotUsedSpaceAlert_Type = Unsigned32
_EqlNASContainerSnapshotUsedSpaceAlert_Object = MibTableColumn
eqlNASContainerSnapshotUsedSpaceAlert = _EqlNASContainerSnapshotUsedSpaceAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 7),
    _EqlNASContainerSnapshotUsedSpaceAlert_Type()
)
eqlNASContainerSnapshotUsedSpaceAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerSnapshotUsedSpaceAlert.setStatus("current")
_EqlNASContainerUnixFilePermissions_Type = UNIXPermissions
_EqlNASContainerUnixFilePermissions_Object = MibTableColumn
eqlNASContainerUnixFilePermissions = _EqlNASContainerUnixFilePermissions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 8),
    _EqlNASContainerUnixFilePermissions_Type()
)
eqlNASContainerUnixFilePermissions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerUnixFilePermissions.setStatus("current")
_EqlNASContainerUnixDirPermissions_Type = UNIXPermissions
_EqlNASContainerUnixDirPermissions_Object = MibTableColumn
eqlNASContainerUnixDirPermissions = _EqlNASContainerUnixDirPermissions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 9),
    _EqlNASContainerUnixDirPermissions_Type()
)
eqlNASContainerUnixDirPermissions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerUnixDirPermissions.setStatus("current")
_EqlNASContainerQuotaEnabled_Type = TruthValue
_EqlNASContainerQuotaEnabled_Object = MibTableColumn
eqlNASContainerQuotaEnabled = _EqlNASContainerQuotaEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 10),
    _EqlNASContainerQuotaEnabled_Type()
)
eqlNASContainerQuotaEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerQuotaEnabled.setStatus("current")


class _EqlNASContainerFileAccessSecurity_Type(Integer32):
    """Custom type eqlNASContainerFileAccessSecurity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 1),
          ("ntfs", 2),
          ("unix", 3))
    )


_EqlNASContainerFileAccessSecurity_Type.__name__ = "Integer32"
_EqlNASContainerFileAccessSecurity_Object = MibTableColumn
eqlNASContainerFileAccessSecurity = _EqlNASContainerFileAccessSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 11),
    _EqlNASContainerFileAccessSecurity_Type()
)
eqlNASContainerFileAccessSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerFileAccessSecurity.setStatus("current")


class _EqlNASContainerAccessTimeManagementGranularity_Type(Integer32):
    """Custom type eqlNASContainerAccessTimeManagementGranularity based on Integer32"""
    defaultValue = 4

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
        *(("always", 1),
          ("daily", 4),
          ("disabled", 0),
          ("everyFiveMinutes", 2),
          ("hourly", 3),
          ("weekly", 5))
    )


_EqlNASContainerAccessTimeManagementGranularity_Type.__name__ = "Integer32"
_EqlNASContainerAccessTimeManagementGranularity_Object = MibTableColumn
eqlNASContainerAccessTimeManagementGranularity = _EqlNASContainerAccessTimeManagementGranularity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 12),
    _EqlNASContainerAccessTimeManagementGranularity_Type()
)
eqlNASContainerAccessTimeManagementGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerAccessTimeManagementGranularity.setStatus("current")


class _EqlNASContainerOptimizationEnabled_Type(TruthValue):
    """Custom type eqlNASContainerOptimizationEnabled based on TruthValue"""


_EqlNASContainerOptimizationEnabled_Object = MibTableColumn
eqlNASContainerOptimizationEnabled = _EqlNASContainerOptimizationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 13),
    _EqlNASContainerOptimizationEnabled_Type()
)
eqlNASContainerOptimizationEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerOptimizationEnabled.setStatus("current")


class _EqlNASContainerDedupMethodType_Type(Integer32):
    """Custom type eqlNASContainerDedupMethodType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("object", 2),
          ("variable-chunk", 1))
    )


_EqlNASContainerDedupMethodType_Type.__name__ = "Integer32"
_EqlNASContainerDedupMethodType_Object = MibTableColumn
eqlNASContainerDedupMethodType = _EqlNASContainerDedupMethodType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 14),
    _EqlNASContainerDedupMethodType_Type()
)
eqlNASContainerDedupMethodType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDedupMethodType.setStatus("current")


class _EqlNASContainerCompressionEnabled_Type(TruthValue):
    """Custom type eqlNASContainerCompressionEnabled based on TruthValue"""


_EqlNASContainerCompressionEnabled_Object = MibTableColumn
eqlNASContainerCompressionEnabled = _EqlNASContainerCompressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 15),
    _EqlNASContainerCompressionEnabled_Type()
)
eqlNASContainerCompressionEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerCompressionEnabled.setStatus("current")


class _EqlNASContainerModificationTimeFilter_Type(Integer32):
    """Custom type eqlNASContainerModificationTimeFilter based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 365),
    )


_EqlNASContainerModificationTimeFilter_Type.__name__ = "Integer32"
_EqlNASContainerModificationTimeFilter_Object = MibTableColumn
eqlNASContainerModificationTimeFilter = _EqlNASContainerModificationTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 16),
    _EqlNASContainerModificationTimeFilter_Type()
)
eqlNASContainerModificationTimeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerModificationTimeFilter.setStatus("current")


class _EqlNASContainerAccessTimeFilter_Type(Integer32):
    """Custom type eqlNASContainerAccessTimeFilter based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 365),
    )


_EqlNASContainerAccessTimeFilter_Type.__name__ = "Integer32"
_EqlNASContainerAccessTimeFilter_Object = MibTableColumn
eqlNASContainerAccessTimeFilter = _EqlNASContainerAccessTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 17),
    _EqlNASContainerAccessTimeFilter_Type()
)
eqlNASContainerAccessTimeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerAccessTimeFilter.setStatus("current")


class _EqlNASContainerExcludeFilesByNamePattern_Type(OctetString):
    """Custom type eqlNASContainerExcludeFilesByNamePattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlNASContainerExcludeFilesByNamePattern_Type.__name__ = "OctetString"
_EqlNASContainerExcludeFilesByNamePattern_Object = MibTableColumn
eqlNASContainerExcludeFilesByNamePattern = _EqlNASContainerExcludeFilesByNamePattern_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 18),
    _EqlNASContainerExcludeFilesByNamePattern_Type()
)
eqlNASContainerExcludeFilesByNamePattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerExcludeFilesByNamePattern.setStatus("deprecated")


class _EqlNASContainerAction_Type(Integer32):
    """Custom type eqlNASContainerAction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("delete-host-access-cfg", 1),
          ("none", 0))
    )


_EqlNASContainerAction_Type.__name__ = "Integer32"
_EqlNASContainerAction_Object = MibTableColumn
eqlNASContainerAction = _EqlNASContainerAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 19),
    _EqlNASContainerAction_Type()
)
eqlNASContainerAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerAction.setStatus("current")


class _EqlNASContainerDefaultUserQuota_Type(Unsigned32):
    """Custom type eqlNASContainerDefaultUserQuota based on Unsigned32"""
    defaultValue = 0


_EqlNASContainerDefaultUserQuota_Object = MibTableColumn
eqlNASContainerDefaultUserQuota = _EqlNASContainerDefaultUserQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 20),
    _EqlNASContainerDefaultUserQuota_Type()
)
eqlNASContainerDefaultUserQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDefaultUserQuota.setStatus("current")


class _EqlNASContainerDefaultUserQuotaAlert_Type(Unsigned32):
    """Custom type eqlNASContainerDefaultUserQuotaAlert based on Unsigned32"""
    defaultValue = 0


_EqlNASContainerDefaultUserQuotaAlert_Object = MibTableColumn
eqlNASContainerDefaultUserQuotaAlert = _EqlNASContainerDefaultUserQuotaAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 21),
    _EqlNASContainerDefaultUserQuotaAlert_Type()
)
eqlNASContainerDefaultUserQuotaAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDefaultUserQuotaAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASContainerDefaultUserQuotaAlert.setUnits("%")


class _EqlNASContainerDefaultGroupQuota_Type(Unsigned32):
    """Custom type eqlNASContainerDefaultGroupQuota based on Unsigned32"""
    defaultValue = 0


_EqlNASContainerDefaultGroupQuota_Object = MibTableColumn
eqlNASContainerDefaultGroupQuota = _EqlNASContainerDefaultGroupQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 22),
    _EqlNASContainerDefaultGroupQuota_Type()
)
eqlNASContainerDefaultGroupQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDefaultGroupQuota.setStatus("current")


class _EqlNASContainerDefaultGroupQuotaAlert_Type(Unsigned32):
    """Custom type eqlNASContainerDefaultGroupQuotaAlert based on Unsigned32"""
    defaultValue = 0


_EqlNASContainerDefaultGroupQuotaAlert_Object = MibTableColumn
eqlNASContainerDefaultGroupQuotaAlert = _EqlNASContainerDefaultGroupQuotaAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 23),
    _EqlNASContainerDefaultGroupQuotaAlert_Type()
)
eqlNASContainerDefaultGroupQuotaAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDefaultGroupQuotaAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASContainerDefaultGroupQuotaAlert.setUnits("%")


class _EqlNASContainerOptimizationFilterMode_Type(Integer32):
    """Custom type eqlNASContainerOptimizationFilterMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ignore-filters", 1),
          ("use-filters", 0))
    )


_EqlNASContainerOptimizationFilterMode_Type.__name__ = "Integer32"
_EqlNASContainerOptimizationFilterMode_Object = MibTableColumn
eqlNASContainerOptimizationFilterMode = _EqlNASContainerOptimizationFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 24),
    _EqlNASContainerOptimizationFilterMode_Type()
)
eqlNASContainerOptimizationFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerOptimizationFilterMode.setStatus("current")


class _EqlNASContainerRehydrateOnReadEnabled_Type(TruthValue):
    """Custom type eqlNASContainerRehydrateOnReadEnabled based on TruthValue"""


_EqlNASContainerRehydrateOnReadEnabled_Object = MibTableColumn
eqlNASContainerRehydrateOnReadEnabled = _EqlNASContainerRehydrateOnReadEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 1, 25),
    _EqlNASContainerRehydrateOnReadEnabled_Type()
)
eqlNASContainerRehydrateOnReadEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerRehydrateOnReadEnabled.setStatus("current")
_EqlNASContainerUniqueIDTable_Object = MibTable
eqlNASContainerUniqueIDTable = _EqlNASContainerUniqueIDTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eqlNASContainerUniqueIDTable.setStatus("current")
_EqlNASContainerUniqueIDEntry_Object = MibTableRow
eqlNASContainerUniqueIDEntry = _EqlNASContainerUniqueIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 2, 1)
)
eqlNASContainerUniqueIDEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerUniqueIDType"),
)
if mibBuilder.loadTexts:
    eqlNASContainerUniqueIDEntry.setStatus("current")


class _EqlNASContainerUniqueIDType_Type(Integer32):
    """Custom type eqlNASContainerUniqueIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("quota", 2),
          ("snapshot", 1))
    )


_EqlNASContainerUniqueIDType_Type.__name__ = "Integer32"
_EqlNASContainerUniqueIDType_Object = MibTableColumn
eqlNASContainerUniqueIDType = _EqlNASContainerUniqueIDType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 2, 1, 1),
    _EqlNASContainerUniqueIDType_Type()
)
eqlNASContainerUniqueIDType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASContainerUniqueIDType.setStatus("current")
_EqlNASContainerUniqueIDValueLen_Type = Unsigned32
_EqlNASContainerUniqueIDValueLen_Object = MibTableColumn
eqlNASContainerUniqueIDValueLen = _EqlNASContainerUniqueIDValueLen_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 2, 1, 2),
    _EqlNASContainerUniqueIDValueLen_Type()
)
eqlNASContainerUniqueIDValueLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerUniqueIDValueLen.setStatus("current")


class _EqlNASContainerUniqueIDValue_Type(OctetString):
    """Custom type eqlNASContainerUniqueIDValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_EqlNASContainerUniqueIDValue_Type.__name__ = "OctetString"
_EqlNASContainerUniqueIDValue_Object = MibTableColumn
eqlNASContainerUniqueIDValue = _EqlNASContainerUniqueIDValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 2, 1, 3),
    _EqlNASContainerUniqueIDValue_Type()
)
eqlNASContainerUniqueIDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerUniqueIDValue.setStatus("current")
_EqlNASSnapshotTable_Object = MibTable
eqlNASSnapshotTable = _EqlNASSnapshotTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eqlNASSnapshotTable.setStatus("current")
_EqlNASSnapshotEntry_Object = MibTableRow
eqlNASSnapshotEntry = _EqlNASSnapshotEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1)
)
eqlNASSnapshotEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASSnapshotIndex"),
)
if mibBuilder.loadTexts:
    eqlNASSnapshotEntry.setStatus("current")
_EqlNASSnapshotIndex_Type = Unsigned32
_EqlNASSnapshotIndex_Object = MibTableColumn
eqlNASSnapshotIndex = _EqlNASSnapshotIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1, 1),
    _EqlNASSnapshotIndex_Type()
)
eqlNASSnapshotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASSnapshotIndex.setStatus("current")
_EqlNASSnapshotRowStatus_Type = RowStatus
_EqlNASSnapshotRowStatus_Object = MibTableColumn
eqlNASSnapshotRowStatus = _EqlNASSnapshotRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1, 2),
    _EqlNASSnapshotRowStatus_Type()
)
eqlNASSnapshotRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotRowStatus.setStatus("current")


class _EqlNASSnapshotName_Type(OctetString):
    """Custom type eqlNASSnapshotName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASSnapshotName_Type.__name__ = "OctetString"
_EqlNASSnapshotName_Object = MibTableColumn
eqlNASSnapshotName = _EqlNASSnapshotName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1, 3),
    _EqlNASSnapshotName_Type()
)
eqlNASSnapshotName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotName.setStatus("current")
_EqlNASSnapshotSize_Type = Integer32
_EqlNASSnapshotSize_Object = MibTableColumn
eqlNASSnapshotSize = _EqlNASSnapshotSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1, 4),
    _EqlNASSnapshotSize_Type()
)
eqlNASSnapshotSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASSnapshotSize.setStatus("current")
_EqlNASSnapshotTimestamp_Type = Counter32
_EqlNASSnapshotTimestamp_Object = MibTableColumn
eqlNASSnapshotTimestamp = _EqlNASSnapshotTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1, 5),
    _EqlNASSnapshotTimestamp_Type()
)
eqlNASSnapshotTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASSnapshotTimestamp.setStatus("current")


class _EqlNASSnapshotRollBack_Type(TruthValue):
    """Custom type eqlNASSnapshotRollBack based on TruthValue"""


_EqlNASSnapshotRollBack_Object = MibTableColumn
eqlNASSnapshotRollBack = _EqlNASSnapshotRollBack_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1, 6),
    _EqlNASSnapshotRollBack_Type()
)
eqlNASSnapshotRollBack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotRollBack.setStatus("current")


class _EqlNASSnapshotPolicyIdx_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyIdx based on Integer32"""
    defaultValue = 0


_EqlNASSnapshotPolicyIdx_Object = MibTableColumn
eqlNASSnapshotPolicyIdx = _EqlNASSnapshotPolicyIdx_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 3, 1, 7),
    _EqlNASSnapshotPolicyIdx_Type()
)
eqlNASSnapshotPolicyIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyIdx.setStatus("current")
_EqlNASSnapshotPolicyTable_Object = MibTable
eqlNASSnapshotPolicyTable = _EqlNASSnapshotPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4)
)
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyTable.setStatus("current")
_EqlNASSnapshotPolicyEntry_Object = MibTableRow
eqlNASSnapshotPolicyEntry = _EqlNASSnapshotPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1)
)
eqlNASSnapshotPolicyEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASSnapshotPolicyIndex"),
)
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyEntry.setStatus("current")
_EqlNASSnapshotPolicyIndex_Type = Integer32
_EqlNASSnapshotPolicyIndex_Object = MibTableColumn
eqlNASSnapshotPolicyIndex = _EqlNASSnapshotPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 1),
    _EqlNASSnapshotPolicyIndex_Type()
)
eqlNASSnapshotPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyIndex.setStatus("current")
_EqlNASSnapshotPolicyRowStatus_Type = RowStatus
_EqlNASSnapshotPolicyRowStatus_Object = MibTableColumn
eqlNASSnapshotPolicyRowStatus = _EqlNASSnapshotPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 2),
    _EqlNASSnapshotPolicyRowStatus_Type()
)
eqlNASSnapshotPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyRowStatus.setStatus("current")


class _EqlNASSnapshotPolicyName_Type(OctetString):
    """Custom type eqlNASSnapshotPolicyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASSnapshotPolicyName_Type.__name__ = "OctetString"
_EqlNASSnapshotPolicyName_Object = MibTableColumn
eqlNASSnapshotPolicyName = _EqlNASSnapshotPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 3),
    _EqlNASSnapshotPolicyName_Type()
)
eqlNASSnapshotPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyName.setStatus("current")


class _EqlNASSnapshotPolicyMaxKeep_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyMaxKeep based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqlNASSnapshotPolicyMaxKeep_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyMaxKeep_Object = MibTableColumn
eqlNASSnapshotPolicyMaxKeep = _EqlNASSnapshotPolicyMaxKeep_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 6),
    _EqlNASSnapshotPolicyMaxKeep_Type()
)
eqlNASSnapshotPolicyMaxKeep.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyMaxKeep.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyMaxKeep.setUnits("snapshots")


class _EqlNASSnapshotPolicyType_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("daily", 2),
          ("hourly", 5),
          ("monthly", 4),
          ("once", 1),
          ("weekly", 3))
    )


_EqlNASSnapshotPolicyType_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyType_Object = MibTableColumn
eqlNASSnapshotPolicyType = _EqlNASSnapshotPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 7),
    _EqlNASSnapshotPolicyType_Type()
)
eqlNASSnapshotPolicyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyType.setStatus("current")


class _EqlNASSnapshotPolicyRepeatFactor_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyRepeatFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EqlNASSnapshotPolicyRepeatFactor_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyRepeatFactor_Object = MibTableColumn
eqlNASSnapshotPolicyRepeatFactor = _EqlNASSnapshotPolicyRepeatFactor_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 8),
    _EqlNASSnapshotPolicyRepeatFactor_Type()
)
eqlNASSnapshotPolicyRepeatFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyRepeatFactor.setStatus("current")


class _EqlNASSnapshotPolicyStartTime_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyStartTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqlNASSnapshotPolicyStartTime_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyStartTime_Object = MibTableColumn
eqlNASSnapshotPolicyStartTime = _EqlNASSnapshotPolicyStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 9),
    _EqlNASSnapshotPolicyStartTime_Type()
)
eqlNASSnapshotPolicyStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStartTime.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStartTime.setUnits("minutes")


class _EqlNASSnapshotPolicyEndTime_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyEndTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqlNASSnapshotPolicyEndTime_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyEndTime_Object = MibTableColumn
eqlNASSnapshotPolicyEndTime = _EqlNASSnapshotPolicyEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 10),
    _EqlNASSnapshotPolicyEndTime_Type()
)
eqlNASSnapshotPolicyEndTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyEndTime.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyEndTime.setUnits("minutes")


class _EqlNASSnapshotPolicyTimeFrequency_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyTimeFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1439),
    )


_EqlNASSnapshotPolicyTimeFrequency_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyTimeFrequency_Object = MibTableColumn
eqlNASSnapshotPolicyTimeFrequency = _EqlNASSnapshotPolicyTimeFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 11),
    _EqlNASSnapshotPolicyTimeFrequency_Type()
)
eqlNASSnapshotPolicyTimeFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyTimeFrequency.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyTimeFrequency.setUnits("minutes")


class _EqlNASSnapshotPolicyStartDate_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyStartDate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqlNASSnapshotPolicyStartDate_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyStartDate_Object = MibTableColumn
eqlNASSnapshotPolicyStartDate = _EqlNASSnapshotPolicyStartDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 12),
    _EqlNASSnapshotPolicyStartDate_Type()
)
eqlNASSnapshotPolicyStartDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStartDate.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStartDate.setUnits("days")


class _EqlNASSnapshotPolicyEndDate_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyEndDate based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EqlNASSnapshotPolicyEndDate_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyEndDate_Object = MibTableColumn
eqlNASSnapshotPolicyEndDate = _EqlNASSnapshotPolicyEndDate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 13),
    _EqlNASSnapshotPolicyEndDate_Type()
)
eqlNASSnapshotPolicyEndDate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyEndDate.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyEndDate.setUnits("days")
_EqlNASSnapshotPolicyWeekMask_Type = Integer32
_EqlNASSnapshotPolicyWeekMask_Object = MibTableColumn
eqlNASSnapshotPolicyWeekMask = _EqlNASSnapshotPolicyWeekMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 14),
    _EqlNASSnapshotPolicyWeekMask_Type()
)
eqlNASSnapshotPolicyWeekMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyWeekMask.setStatus("current")
_EqlNASSnapshotPolicyMonthMask_Type = Integer32
_EqlNASSnapshotPolicyMonthMask_Object = MibTableColumn
eqlNASSnapshotPolicyMonthMask = _EqlNASSnapshotPolicyMonthMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 15),
    _EqlNASSnapshotPolicyMonthMask_Type()
)
eqlNASSnapshotPolicyMonthMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyMonthMask.setStatus("current")


class _EqlNASSnapshotPolicyOccurence_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyOccurence based on Integer32"""
    defaultValue = 0


_EqlNASSnapshotPolicyOccurence_Object = MibTableColumn
eqlNASSnapshotPolicyOccurence = _EqlNASSnapshotPolicyOccurence_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 17),
    _EqlNASSnapshotPolicyOccurence_Type()
)
eqlNASSnapshotPolicyOccurence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyOccurence.setStatus("current")
_EqlNASSnapshotPolicyReplication_Type = SiteIndexOrZero
_EqlNASSnapshotPolicyReplication_Object = MibTableColumn
eqlNASSnapshotPolicyReplication = _EqlNASSnapshotPolicyReplication_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 18),
    _EqlNASSnapshotPolicyReplication_Type()
)
eqlNASSnapshotPolicyReplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyReplication.setStatus("current")


class _EqlNASSnapshotPolicyAdminStatus_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyAdminStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_EqlNASSnapshotPolicyAdminStatus_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyAdminStatus_Object = MibTableColumn
eqlNASSnapshotPolicyAdminStatus = _EqlNASSnapshotPolicyAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 19),
    _EqlNASSnapshotPolicyAdminStatus_Type()
)
eqlNASSnapshotPolicyAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyAdminStatus.setStatus("current")


class _EqlNASSnapshotPolicyCategory_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyCategory based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optimization-default-policy", 2),
          ("optimization-policy", 1),
          ("snapshot-replication-policy", 0))
    )


_EqlNASSnapshotPolicyCategory_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyCategory_Object = MibTableColumn
eqlNASSnapshotPolicyCategory = _EqlNASSnapshotPolicyCategory_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 4, 1, 20),
    _EqlNASSnapshotPolicyCategory_Type()
)
eqlNASSnapshotPolicyCategory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyCategory.setStatus("current")
_EqlNASSnapshotPolicyStatusTable_Object = MibTable
eqlNASSnapshotPolicyStatusTable = _EqlNASSnapshotPolicyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 5)
)
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStatusTable.setStatus("current")
_EqlNASSnapshotPolicyStatusEntry_Object = MibTableRow
eqlNASSnapshotPolicyStatusEntry = _EqlNASSnapshotPolicyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStatusEntry.setStatus("current")
_EqlNASSnapshotPolicyStatusNextCreate_Type = Counter32
_EqlNASSnapshotPolicyStatusNextCreate_Object = MibTableColumn
eqlNASSnapshotPolicyStatusNextCreate = _EqlNASSnapshotPolicyStatusNextCreate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 5, 1, 1),
    _EqlNASSnapshotPolicyStatusNextCreate_Type()
)
eqlNASSnapshotPolicyStatusNextCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStatusNextCreate.setStatus("current")


class _EqlNASSnapshotPolicyStatusOperStatus_Type(Integer32):
    """Custom type eqlNASSnapshotPolicyStatusOperStatus based on Integer32"""
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
        *(("active", 3),
          ("disabled", 1),
          ("enabled", 0),
          ("expired", 2))
    )


_EqlNASSnapshotPolicyStatusOperStatus_Type.__name__ = "Integer32"
_EqlNASSnapshotPolicyStatusOperStatus_Object = MibTableColumn
eqlNASSnapshotPolicyStatusOperStatus = _EqlNASSnapshotPolicyStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 5, 1, 2),
    _EqlNASSnapshotPolicyStatusOperStatus_Type()
)
eqlNASSnapshotPolicyStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASSnapshotPolicyStatusOperStatus.setStatus("current")
_EqlNASQuotaTable_Object = MibTable
eqlNASQuotaTable = _EqlNASQuotaTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6)
)
if mibBuilder.loadTexts:
    eqlNASQuotaTable.setStatus("current")
_EqlNASQuotaEntry_Object = MibTableRow
eqlNASQuotaEntry = _EqlNASQuotaEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6, 1)
)
eqlNASQuotaEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASQuotaTargetType"),
    (0, "EQLNAS-MIB", "eqlNASQuotaTargetName"),
)
if mibBuilder.loadTexts:
    eqlNASQuotaEntry.setStatus("current")
_EqlNASQuotaRowStatus_Type = RowStatus
_EqlNASQuotaRowStatus_Object = MibTableColumn
eqlNASQuotaRowStatus = _EqlNASQuotaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6, 1, 1),
    _EqlNASQuotaRowStatus_Type()
)
eqlNASQuotaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASQuotaRowStatus.setStatus("current")


class _EqlNASQuotaTargetType_Type(Integer32):
    """Custom type eqlNASQuotaTargetType based on Integer32"""
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
        *(("allofgroup", 1),
          ("allquotas", 6),
          ("anyuseringroup", 2),
          ("defaultgroup", 5),
          ("defaultuser", 4),
          ("unused", 0),
          ("user", 3))
    )


_EqlNASQuotaTargetType_Type.__name__ = "Integer32"
_EqlNASQuotaTargetType_Object = MibTableColumn
eqlNASQuotaTargetType = _EqlNASQuotaTargetType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6, 1, 2),
    _EqlNASQuotaTargetType_Type()
)
eqlNASQuotaTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASQuotaTargetType.setStatus("current")


class _EqlNASQuotaTargetName_Type(OctetString):
    """Custom type eqlNASQuotaTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlNASQuotaTargetName_Type.__name__ = "OctetString"
_EqlNASQuotaTargetName_Object = MibTableColumn
eqlNASQuotaTargetName = _EqlNASQuotaTargetName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6, 1, 3),
    _EqlNASQuotaTargetName_Type()
)
eqlNASQuotaTargetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASQuotaTargetName.setStatus("current")
_EqlNASQuotaWarnLimit_Type = Integer32
_EqlNASQuotaWarnLimit_Object = MibTableColumn
eqlNASQuotaWarnLimit = _EqlNASQuotaWarnLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6, 1, 4),
    _EqlNASQuotaWarnLimit_Type()
)
eqlNASQuotaWarnLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASQuotaWarnLimit.setStatus("current")
_EqlNASQuotaHardLimit_Type = Unsigned32
_EqlNASQuotaHardLimit_Object = MibTableColumn
eqlNASQuotaHardLimit = _EqlNASQuotaHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6, 1, 5),
    _EqlNASQuotaHardLimit_Type()
)
eqlNASQuotaHardLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASQuotaHardLimit.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASQuotaHardLimit.setUnits("MB")
_EqlNASQuotaUsage_Type = Integer32
_EqlNASQuotaUsage_Object = MibTableColumn
eqlNASQuotaUsage = _EqlNASQuotaUsage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 6, 1, 6),
    _EqlNASQuotaUsage_Type()
)
eqlNASQuotaUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASQuotaUsage.setStatus("current")
_EqlNASQuotaUsageTable_Object = MibTable
eqlNASQuotaUsageTable = _EqlNASQuotaUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 7)
)
if mibBuilder.loadTexts:
    eqlNASQuotaUsageTable.setStatus("current")
_EqlNASQuotaUsageEntry_Object = MibTableRow
eqlNASQuotaUsageEntry = _EqlNASQuotaUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 7, 1)
)
eqlNASQuotaUsageEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASQuotaUsageTargetType"),
    (0, "EQLNAS-MIB", "eqlNASQuotaUsageTargetName"),
)
if mibBuilder.loadTexts:
    eqlNASQuotaUsageEntry.setStatus("current")
_EqlNASQuotaUsageRowStatus_Type = RowStatus
_EqlNASQuotaUsageRowStatus_Object = MibTableColumn
eqlNASQuotaUsageRowStatus = _EqlNASQuotaUsageRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 7, 1, 1),
    _EqlNASQuotaUsageRowStatus_Type()
)
eqlNASQuotaUsageRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASQuotaUsageRowStatus.setStatus("current")


class _EqlNASQuotaUsageTargetType_Type(Integer32):
    """Custom type eqlNASQuotaUsageTargetType based on Integer32"""
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
        *(("allofgroup", 1),
          ("anyuseringroup", 2),
          ("unused", 0),
          ("user", 3))
    )


_EqlNASQuotaUsageTargetType_Type.__name__ = "Integer32"
_EqlNASQuotaUsageTargetType_Object = MibTableColumn
eqlNASQuotaUsageTargetType = _EqlNASQuotaUsageTargetType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 7, 1, 2),
    _EqlNASQuotaUsageTargetType_Type()
)
eqlNASQuotaUsageTargetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASQuotaUsageTargetType.setStatus("current")


class _EqlNASQuotaUsageTargetName_Type(OctetString):
    """Custom type eqlNASQuotaUsageTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlNASQuotaUsageTargetName_Type.__name__ = "OctetString"
_EqlNASQuotaUsageTargetName_Object = MibTableColumn
eqlNASQuotaUsageTargetName = _EqlNASQuotaUsageTargetName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 7, 1, 3),
    _EqlNASQuotaUsageTargetName_Type()
)
eqlNASQuotaUsageTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASQuotaUsageTargetName.setStatus("current")
_EqlNASQuotaUsageMB_Type = Integer32
_EqlNASQuotaUsageMB_Object = MibTableColumn
eqlNASQuotaUsageMB = _EqlNASQuotaUsageMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 7, 1, 4),
    _EqlNASQuotaUsageMB_Type()
)
eqlNASQuotaUsageMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASQuotaUsageMB.setStatus("current")
_EqlNASGroupQuotaEffectiveRuleTable_Object = MibTable
eqlNASGroupQuotaEffectiveRuleTable = _EqlNASGroupQuotaEffectiveRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8)
)
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleTable.setStatus("current")
_EqlNASGroupQuotaEffectiveRuleEntry_Object = MibTableRow
eqlNASGroupQuotaEffectiveRuleEntry = _EqlNASGroupQuotaEffectiveRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8, 1)
)
eqlNASGroupQuotaEffectiveRuleEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASGroupQuotaEffectiveRuleTargetName"),
)
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleEntry.setStatus("current")


class _EqlNASGroupQuotaEffectiveRuleTargetName_Type(OctetString):
    """Custom type eqlNASGroupQuotaEffectiveRuleTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlNASGroupQuotaEffectiveRuleTargetName_Type.__name__ = "OctetString"
_EqlNASGroupQuotaEffectiveRuleTargetName_Object = MibTableColumn
eqlNASGroupQuotaEffectiveRuleTargetName = _EqlNASGroupQuotaEffectiveRuleTargetName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8, 1, 1),
    _EqlNASGroupQuotaEffectiveRuleTargetName_Type()
)
eqlNASGroupQuotaEffectiveRuleTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleTargetName.setStatus("current")
_EqlNASGroupQuotaEffectiveRuleRowStatus_Type = RowStatus
_EqlNASGroupQuotaEffectiveRuleRowStatus_Object = MibTableColumn
eqlNASGroupQuotaEffectiveRuleRowStatus = _EqlNASGroupQuotaEffectiveRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8, 1, 2),
    _EqlNASGroupQuotaEffectiveRuleRowStatus_Type()
)
eqlNASGroupQuotaEffectiveRuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleRowStatus.setStatus("current")
_EqlNASGroupQuotaEffectiveRuleSoftLimit_Type = Integer32
_EqlNASGroupQuotaEffectiveRuleSoftLimit_Object = MibTableColumn
eqlNASGroupQuotaEffectiveRuleSoftLimit = _EqlNASGroupQuotaEffectiveRuleSoftLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8, 1, 3),
    _EqlNASGroupQuotaEffectiveRuleSoftLimit_Type()
)
eqlNASGroupQuotaEffectiveRuleSoftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleSoftLimit.setStatus("current")
_EqlNASGroupQuotaEffectiveRuleHardLimit_Type = Integer32
_EqlNASGroupQuotaEffectiveRuleHardLimit_Object = MibTableColumn
eqlNASGroupQuotaEffectiveRuleHardLimit = _EqlNASGroupQuotaEffectiveRuleHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8, 1, 4),
    _EqlNASGroupQuotaEffectiveRuleHardLimit_Type()
)
eqlNASGroupQuotaEffectiveRuleHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleHardLimit.setStatus("current")


class _EqlNASGroupQuotaEffectiveRuleSoftLimitEnabled_Type(TruthValue):
    """Custom type eqlNASGroupQuotaEffectiveRuleSoftLimitEnabled based on TruthValue"""


_EqlNASGroupQuotaEffectiveRuleSoftLimitEnabled_Object = MibTableColumn
eqlNASGroupQuotaEffectiveRuleSoftLimitEnabled = _EqlNASGroupQuotaEffectiveRuleSoftLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8, 1, 5),
    _EqlNASGroupQuotaEffectiveRuleSoftLimitEnabled_Type()
)
eqlNASGroupQuotaEffectiveRuleSoftLimitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleSoftLimitEnabled.setStatus("current")


class _EqlNASGroupQuotaEffectiveRuleHardLimitEnabled_Type(TruthValue):
    """Custom type eqlNASGroupQuotaEffectiveRuleHardLimitEnabled based on TruthValue"""


_EqlNASGroupQuotaEffectiveRuleHardLimitEnabled_Object = MibTableColumn
eqlNASGroupQuotaEffectiveRuleHardLimitEnabled = _EqlNASGroupQuotaEffectiveRuleHardLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 8, 1, 6),
    _EqlNASGroupQuotaEffectiveRuleHardLimitEnabled_Type()
)
eqlNASGroupQuotaEffectiveRuleHardLimitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASGroupQuotaEffectiveRuleHardLimitEnabled.setStatus("current")
_EqlNASUserQuotaEffectiveRuleTable_Object = MibTable
eqlNASUserQuotaEffectiveRuleTable = _EqlNASUserQuotaEffectiveRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9)
)
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleTable.setStatus("current")
_EqlNASUserQuotaEffectiveRuleEntry_Object = MibTableRow
eqlNASUserQuotaEffectiveRuleEntry = _EqlNASUserQuotaEffectiveRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1)
)
eqlNASUserQuotaEffectiveRuleEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASUserQuotaEffectiveRuleTargetName"),
)
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleEntry.setStatus("current")


class _EqlNASUserQuotaEffectiveRuleTargetName_Type(OctetString):
    """Custom type eqlNASUserQuotaEffectiveRuleTargetName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlNASUserQuotaEffectiveRuleTargetName_Type.__name__ = "OctetString"
_EqlNASUserQuotaEffectiveRuleTargetName_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleTargetName = _EqlNASUserQuotaEffectiveRuleTargetName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 1),
    _EqlNASUserQuotaEffectiveRuleTargetName_Type()
)
eqlNASUserQuotaEffectiveRuleTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleTargetName.setStatus("current")
_EqlNASUserQuotaEffectiveRuleRowStatus_Type = RowStatus
_EqlNASUserQuotaEffectiveRuleRowStatus_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleRowStatus = _EqlNASUserQuotaEffectiveRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 2),
    _EqlNASUserQuotaEffectiveRuleRowStatus_Type()
)
eqlNASUserQuotaEffectiveRuleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleRowStatus.setStatus("current")
_EqlNASUserQuotaEffectiveRuleUserSoftLimit_Type = Integer32
_EqlNASUserQuotaEffectiveRuleUserSoftLimit_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleUserSoftLimit = _EqlNASUserQuotaEffectiveRuleUserSoftLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 3),
    _EqlNASUserQuotaEffectiveRuleUserSoftLimit_Type()
)
eqlNASUserQuotaEffectiveRuleUserSoftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleUserSoftLimit.setStatus("current")
_EqlNASUserQuotaEffectiveRuleUserHardLimit_Type = Integer32
_EqlNASUserQuotaEffectiveRuleUserHardLimit_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleUserHardLimit = _EqlNASUserQuotaEffectiveRuleUserHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 4),
    _EqlNASUserQuotaEffectiveRuleUserHardLimit_Type()
)
eqlNASUserQuotaEffectiveRuleUserHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleUserHardLimit.setStatus("current")


class _EqlNASUserQuotaEffectiveRuleGroupName_Type(OctetString):
    """Custom type eqlNASUserQuotaEffectiveRuleGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 129),
    )


_EqlNASUserQuotaEffectiveRuleGroupName_Type.__name__ = "OctetString"
_EqlNASUserQuotaEffectiveRuleGroupName_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleGroupName = _EqlNASUserQuotaEffectiveRuleGroupName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 5),
    _EqlNASUserQuotaEffectiveRuleGroupName_Type()
)
eqlNASUserQuotaEffectiveRuleGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleGroupName.setStatus("current")
_EqlNASUserQuotaEffectiveRuleGroupSoftLimit_Type = Integer32
_EqlNASUserQuotaEffectiveRuleGroupSoftLimit_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleGroupSoftLimit = _EqlNASUserQuotaEffectiveRuleGroupSoftLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 6),
    _EqlNASUserQuotaEffectiveRuleGroupSoftLimit_Type()
)
eqlNASUserQuotaEffectiveRuleGroupSoftLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleGroupSoftLimit.setStatus("current")
_EqlNASUserQuotaEffectiveRuleGroupHardLimit_Type = Integer32
_EqlNASUserQuotaEffectiveRuleGroupHardLimit_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleGroupHardLimit = _EqlNASUserQuotaEffectiveRuleGroupHardLimit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 7),
    _EqlNASUserQuotaEffectiveRuleGroupHardLimit_Type()
)
eqlNASUserQuotaEffectiveRuleGroupHardLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleGroupHardLimit.setStatus("current")


class _EqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled_Type(TruthValue):
    """Custom type eqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled based on TruthValue"""


_EqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled = _EqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 8),
    _EqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled_Type()
)
eqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled.setStatus("current")


class _EqlNASUserQuotaEffectiveRuleUserHardLimitEnabled_Type(TruthValue):
    """Custom type eqlNASUserQuotaEffectiveRuleUserHardLimitEnabled based on TruthValue"""


_EqlNASUserQuotaEffectiveRuleUserHardLimitEnabled_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleUserHardLimitEnabled = _EqlNASUserQuotaEffectiveRuleUserHardLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 9),
    _EqlNASUserQuotaEffectiveRuleUserHardLimitEnabled_Type()
)
eqlNASUserQuotaEffectiveRuleUserHardLimitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleUserHardLimitEnabled.setStatus("current")


class _EqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled_Type(TruthValue):
    """Custom type eqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled based on TruthValue"""


_EqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled = _EqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 10),
    _EqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled_Type()
)
eqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled.setStatus("current")


class _EqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled_Type(TruthValue):
    """Custom type eqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled based on TruthValue"""


_EqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled_Object = MibTableColumn
eqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled = _EqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 3, 9, 1, 11),
    _EqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled_Type()
)
eqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled.setStatus("current")
_EqlNASApplianceDefaultCfgTable_Object = MibTable
eqlNASApplianceDefaultCfgTable = _EqlNASApplianceDefaultCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4)
)
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCfgTable.setStatus("current")
_EqlNASApplianceDefaultCfgEntry_Object = MibTableRow
eqlNASApplianceDefaultCfgEntry = _EqlNASApplianceDefaultCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1)
)
eqlNASApplianceDefaultCfgEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCfgEntry.setStatus("current")


class _EqlNASApplianceConfigUsedSpaceAlert_Type(Unsigned32):
    """Custom type eqlNASApplianceConfigUsedSpaceAlert based on Unsigned32"""
    defaultValue = 80


_EqlNASApplianceConfigUsedSpaceAlert_Object = MibTableColumn
eqlNASApplianceConfigUsedSpaceAlert = _EqlNASApplianceConfigUsedSpaceAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 1),
    _EqlNASApplianceConfigUsedSpaceAlert_Type()
)
eqlNASApplianceConfigUsedSpaceAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceConfigUsedSpaceAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASApplianceConfigUsedSpaceAlert.setUnits("%")


class _EqlNASApplianceConfigSnapSpaceAlert_Type(Unsigned32):
    """Custom type eqlNASApplianceConfigSnapSpaceAlert based on Unsigned32"""
    defaultValue = 80


_EqlNASApplianceConfigSnapSpaceAlert_Object = MibTableColumn
eqlNASApplianceConfigSnapSpaceAlert = _EqlNASApplianceConfigSnapSpaceAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 2),
    _EqlNASApplianceConfigSnapSpaceAlert_Type()
)
eqlNASApplianceConfigSnapSpaceAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceConfigSnapSpaceAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASApplianceConfigSnapSpaceAlert.setUnits("%")


class _EqlNASApplianceConfigSnapHardQuota_Type(Unsigned32):
    """Custom type eqlNASApplianceConfigSnapHardQuota based on Unsigned32"""
    defaultValue = 50


_EqlNASApplianceConfigSnapHardQuota_Object = MibTableColumn
eqlNASApplianceConfigSnapHardQuota = _EqlNASApplianceConfigSnapHardQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 3),
    _EqlNASApplianceConfigSnapHardQuota_Type()
)
eqlNASApplianceConfigSnapHardQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceConfigSnapHardQuota.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASApplianceConfigSnapHardQuota.setUnits("%")


class _EqlNASApplianceContainerUnixFilePerms_Type(UNIXPermissions):
    """Custom type eqlNASApplianceContainerUnixFilePerms based on UNIXPermissions"""
    defaultValue = 484


_EqlNASApplianceContainerUnixFilePerms_Object = MibTableColumn
eqlNASApplianceContainerUnixFilePerms = _EqlNASApplianceContainerUnixFilePerms_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 4),
    _EqlNASApplianceContainerUnixFilePerms_Type()
)
eqlNASApplianceContainerUnixFilePerms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceContainerUnixFilePerms.setStatus("current")


class _EqlNASApplianceContainerUnixDirPerms_Type(UNIXPermissions):
    """Custom type eqlNASApplianceContainerUnixDirPerms based on UNIXPermissions"""
    defaultValue = 493


_EqlNASApplianceContainerUnixDirPerms_Object = MibTableColumn
eqlNASApplianceContainerUnixDirPerms = _EqlNASApplianceContainerUnixDirPerms_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 5),
    _EqlNASApplianceContainerUnixDirPerms_Type()
)
eqlNASApplianceContainerUnixDirPerms.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceContainerUnixDirPerms.setStatus("current")


class _EqlNASApplianceContainerFileSecurity_Type(Integer32):
    """Custom type eqlNASApplianceContainerFileSecurity based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mixed", 1),
          ("ntfs", 2),
          ("unix", 3))
    )


_EqlNASApplianceContainerFileSecurity_Type.__name__ = "Integer32"
_EqlNASApplianceContainerFileSecurity_Object = MibTableColumn
eqlNASApplianceContainerFileSecurity = _EqlNASApplianceContainerFileSecurity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 6),
    _EqlNASApplianceContainerFileSecurity_Type()
)
eqlNASApplianceContainerFileSecurity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceContainerFileSecurity.setStatus("current")


class _EqlNASApplianceDefaultUserQuota_Type(Unsigned32):
    """Custom type eqlNASApplianceDefaultUserQuota based on Unsigned32"""
    defaultValue = 0


_EqlNASApplianceDefaultUserQuota_Object = MibTableColumn
eqlNASApplianceDefaultUserQuota = _EqlNASApplianceDefaultUserQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 7),
    _EqlNASApplianceDefaultUserQuota_Type()
)
eqlNASApplianceDefaultUserQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultUserQuota.setStatus("current")


class _EqlNASApplianceDefaultUserQuotaAlert_Type(Unsigned32):
    """Custom type eqlNASApplianceDefaultUserQuotaAlert based on Unsigned32"""
    defaultValue = 0


_EqlNASApplianceDefaultUserQuotaAlert_Object = MibTableColumn
eqlNASApplianceDefaultUserQuotaAlert = _EqlNASApplianceDefaultUserQuotaAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 8),
    _EqlNASApplianceDefaultUserQuotaAlert_Type()
)
eqlNASApplianceDefaultUserQuotaAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultUserQuotaAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultUserQuotaAlert.setUnits("%")


class _EqlNASApplianceDefaultGroupQuota_Type(Unsigned32):
    """Custom type eqlNASApplianceDefaultGroupQuota based on Unsigned32"""
    defaultValue = 0


_EqlNASApplianceDefaultGroupQuota_Object = MibTableColumn
eqlNASApplianceDefaultGroupQuota = _EqlNASApplianceDefaultGroupQuota_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 9),
    _EqlNASApplianceDefaultGroupQuota_Type()
)
eqlNASApplianceDefaultGroupQuota.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultGroupQuota.setStatus("current")


class _EqlNASApplianceDefaultGroupQuotaAlert_Type(Unsigned32):
    """Custom type eqlNASApplianceDefaultGroupQuotaAlert based on Unsigned32"""
    defaultValue = 0


_EqlNASApplianceDefaultGroupQuotaAlert_Object = MibTableColumn
eqlNASApplianceDefaultGroupQuotaAlert = _EqlNASApplianceDefaultGroupQuotaAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 10),
    _EqlNASApplianceDefaultGroupQuotaAlert_Type()
)
eqlNASApplianceDefaultGroupQuotaAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultGroupQuotaAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultGroupQuotaAlert.setUnits("%")


class _EqlNASApplianceDefaultCIFSAllowGuestAccess_Type(TruthValue):
    """Custom type eqlNASApplianceDefaultCIFSAllowGuestAccess based on TruthValue"""


_EqlNASApplianceDefaultCIFSAllowGuestAccess_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAllowGuestAccess = _EqlNASApplianceDefaultCIFSAllowGuestAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 11),
    _EqlNASApplianceDefaultCIFSAllowGuestAccess_Type()
)
eqlNASApplianceDefaultCIFSAllowGuestAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAllowGuestAccess.setStatus("current")


class _EqlNASApplianceCIFSAuthenticationMode_Type(Integer32):
    """Custom type eqlNASApplianceCIFSAuthenticationMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active-directory", 2),
          ("allow-everyone", 1),
          ("local-users", 3))
    )


_EqlNASApplianceCIFSAuthenticationMode_Type.__name__ = "Integer32"
_EqlNASApplianceCIFSAuthenticationMode_Object = MibTableColumn
eqlNASApplianceCIFSAuthenticationMode = _EqlNASApplianceCIFSAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 12),
    _EqlNASApplianceCIFSAuthenticationMode_Type()
)
eqlNASApplianceCIFSAuthenticationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAuthenticationMode.setStatus("current")


class _EqlNASApplianceDefaultCIFSLockEnforcement_Type(Integer32):
    """Custom type eqlNASApplianceDefaultCIFSLockEnforcement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-locks", 0),
          ("only-share-locks", 2),
          ("share-locks-op-locks", 1))
    )


_EqlNASApplianceDefaultCIFSLockEnforcement_Type.__name__ = "Integer32"
_EqlNASApplianceDefaultCIFSLockEnforcement_Object = MibTableColumn
eqlNASApplianceDefaultCIFSLockEnforcement = _EqlNASApplianceDefaultCIFSLockEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 13),
    _EqlNASApplianceDefaultCIFSLockEnforcement_Type()
)
eqlNASApplianceDefaultCIFSLockEnforcement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSLockEnforcement.setStatus("current")


class _EqlNASApplianceNFSExportReadWrite_Type(Integer32):
    """Custom type eqlNASApplianceNFSExportReadWrite based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_EqlNASApplianceNFSExportReadWrite_Type.__name__ = "Integer32"
_EqlNASApplianceNFSExportReadWrite_Object = MibTableColumn
eqlNASApplianceNFSExportReadWrite = _EqlNASApplianceNFSExportReadWrite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 14),
    _EqlNASApplianceNFSExportReadWrite_Type()
)
eqlNASApplianceNFSExportReadWrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportReadWrite.setStatus("current")


class _EqlNASApplianceNFSExportTrustedUsers_Type(Integer32):
    """Custom type eqlNASApplianceNFSExportTrustedUsers based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("all-except-root", 1),
          ("none", 2))
    )


_EqlNASApplianceNFSExportTrustedUsers_Type.__name__ = "Integer32"
_EqlNASApplianceNFSExportTrustedUsers_Object = MibTableColumn
eqlNASApplianceNFSExportTrustedUsers = _EqlNASApplianceNFSExportTrustedUsers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 15),
    _EqlNASApplianceNFSExportTrustedUsers_Type()
)
eqlNASApplianceNFSExportTrustedUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportTrustedUsers.setStatus("current")


class _EqlNASApplianceAccessTimeManagementGranularity_Type(Integer32):
    """Custom type eqlNASApplianceAccessTimeManagementGranularity based on Integer32"""
    defaultValue = 4

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
        *(("always", 1),
          ("daily", 4),
          ("disabled", 0),
          ("everyFiveMinutes", 2),
          ("hourly", 3),
          ("weekly", 5))
    )


_EqlNASApplianceAccessTimeManagementGranularity_Type.__name__ = "Integer32"
_EqlNASApplianceAccessTimeManagementGranularity_Object = MibTableColumn
eqlNASApplianceAccessTimeManagementGranularity = _EqlNASApplianceAccessTimeManagementGranularity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 16),
    _EqlNASApplianceAccessTimeManagementGranularity_Type()
)
eqlNASApplianceAccessTimeManagementGranularity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceAccessTimeManagementGranularity.setStatus("current")


class _EqlNASApplianceOptimizationEnabled_Type(TruthValue):
    """Custom type eqlNASApplianceOptimizationEnabled based on TruthValue"""


_EqlNASApplianceOptimizationEnabled_Object = MibTableColumn
eqlNASApplianceOptimizationEnabled = _EqlNASApplianceOptimizationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 17),
    _EqlNASApplianceOptimizationEnabled_Type()
)
eqlNASApplianceOptimizationEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceOptimizationEnabled.setStatus("current")


class _EqlNASApplianceDedupMethodType_Type(Integer32):
    """Custom type eqlNASApplianceDedupMethodType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("object", 2),
          ("variable-chunk", 1))
    )


_EqlNASApplianceDedupMethodType_Type.__name__ = "Integer32"
_EqlNASApplianceDedupMethodType_Object = MibTableColumn
eqlNASApplianceDedupMethodType = _EqlNASApplianceDedupMethodType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 18),
    _EqlNASApplianceDedupMethodType_Type()
)
eqlNASApplianceDedupMethodType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDedupMethodType.setStatus("current")


class _EqlNASApplianceCompressionEnabled_Type(TruthValue):
    """Custom type eqlNASApplianceCompressionEnabled based on TruthValue"""


_EqlNASApplianceCompressionEnabled_Object = MibTableColumn
eqlNASApplianceCompressionEnabled = _EqlNASApplianceCompressionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 19),
    _EqlNASApplianceCompressionEnabled_Type()
)
eqlNASApplianceCompressionEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCompressionEnabled.setStatus("current")


class _EqlNASApplianceModificationTimeFilter_Type(Integer32):
    """Custom type eqlNASApplianceModificationTimeFilter based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 365),
    )


_EqlNASApplianceModificationTimeFilter_Type.__name__ = "Integer32"
_EqlNASApplianceModificationTimeFilter_Object = MibTableColumn
eqlNASApplianceModificationTimeFilter = _EqlNASApplianceModificationTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 20),
    _EqlNASApplianceModificationTimeFilter_Type()
)
eqlNASApplianceModificationTimeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceModificationTimeFilter.setStatus("current")


class _EqlNASApplianceAccessTimeFilter_Type(Integer32):
    """Custom type eqlNASApplianceAccessTimeFilter based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 365),
    )


_EqlNASApplianceAccessTimeFilter_Type.__name__ = "Integer32"
_EqlNASApplianceAccessTimeFilter_Object = MibTableColumn
eqlNASApplianceAccessTimeFilter = _EqlNASApplianceAccessTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 21),
    _EqlNASApplianceAccessTimeFilter_Type()
)
eqlNASApplianceAccessTimeFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceAccessTimeFilter.setStatus("current")


class _EqlNASApplianceExcludeFilesByNamePattern_Type(OctetString):
    """Custom type eqlNASApplianceExcludeFilesByNamePattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlNASApplianceExcludeFilesByNamePattern_Type.__name__ = "OctetString"
_EqlNASApplianceExcludeFilesByNamePattern_Object = MibTableColumn
eqlNASApplianceExcludeFilesByNamePattern = _EqlNASApplianceExcludeFilesByNamePattern_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 22),
    _EqlNASApplianceExcludeFilesByNamePattern_Type()
)
eqlNASApplianceExcludeFilesByNamePattern.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceExcludeFilesByNamePattern.setStatus("deprecated")


class _EqlNASApplianceDefaultCIFSAntivirusEnabled_Type(StatusDisabledDefault):
    """Custom type eqlNASApplianceDefaultCIFSAntivirusEnabled based on StatusDisabledDefault"""


_EqlNASApplianceDefaultCIFSAntivirusEnabled_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAntivirusEnabled = _EqlNASApplianceDefaultCIFSAntivirusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 23),
    _EqlNASApplianceDefaultCIFSAntivirusEnabled_Type()
)
eqlNASApplianceDefaultCIFSAntivirusEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAntivirusEnabled.setStatus("current")


class _EqlNASApplianceDefaultCIFSAntivirusPolicy_Type(Integer32):
    """Custom type eqlNASApplianceDefaultCIFSAntivirusPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-nothing", 1),
          ("quarantine", 0),
          ("remove", 2))
    )


_EqlNASApplianceDefaultCIFSAntivirusPolicy_Type.__name__ = "Integer32"
_EqlNASApplianceDefaultCIFSAntivirusPolicy_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAntivirusPolicy = _EqlNASApplianceDefaultCIFSAntivirusPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 24),
    _EqlNASApplianceDefaultCIFSAntivirusPolicy_Type()
)
eqlNASApplianceDefaultCIFSAntivirusPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAntivirusPolicy.setStatus("current")


class _EqlNASApplianceDefaultCIFSAntivirusExtensions_Type(OctetString):
    """Custom type eqlNASApplianceDefaultCIFSAntivirusExtensions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlNASApplianceDefaultCIFSAntivirusExtensions_Type.__name__ = "OctetString"
_EqlNASApplianceDefaultCIFSAntivirusExtensions_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAntivirusExtensions = _EqlNASApplianceDefaultCIFSAntivirusExtensions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 25),
    _EqlNASApplianceDefaultCIFSAntivirusExtensions_Type()
)
eqlNASApplianceDefaultCIFSAntivirusExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAntivirusExtensions.setStatus("current")


class _EqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy_Type(Integer32):
    """Custom type eqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1))
    )


_EqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy_Type.__name__ = "Integer32"
_EqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy = _EqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 26),
    _EqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy_Type()
)
eqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy.setStatus("current")


class _EqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths_Type(OctetString):
    """Custom type eqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths_Type.__name__ = "OctetString"
_EqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths = _EqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 27),
    _EqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths_Type()
)
eqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths.setStatus("current")


class _EqlNASApplianceDefaultCIFSAntivirusLargeFileSize_Type(Unsigned32):
    """Custom type eqlNASApplianceDefaultCIFSAntivirusLargeFileSize based on Unsigned32"""
    defaultValue = 3072


_EqlNASApplianceDefaultCIFSAntivirusLargeFileSize_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAntivirusLargeFileSize = _EqlNASApplianceDefaultCIFSAntivirusLargeFileSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 28),
    _EqlNASApplianceDefaultCIFSAntivirusLargeFileSize_Type()
)
eqlNASApplianceDefaultCIFSAntivirusLargeFileSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAntivirusLargeFileSize.setStatus("current")


class _EqlNASApplianceDefaultCIFSAntivirusLargeFileOpen_Type(Integer32):
    """Custom type eqlNASApplianceDefaultCIFSAntivirusLargeFileOpen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 0))
    )


_EqlNASApplianceDefaultCIFSAntivirusLargeFileOpen_Type.__name__ = "Integer32"
_EqlNASApplianceDefaultCIFSAntivirusLargeFileOpen_Object = MibTableColumn
eqlNASApplianceDefaultCIFSAntivirusLargeFileOpen = _EqlNASApplianceDefaultCIFSAntivirusLargeFileOpen_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 29),
    _EqlNASApplianceDefaultCIFSAntivirusLargeFileOpen_Type()
)
eqlNASApplianceDefaultCIFSAntivirusLargeFileOpen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultCIFSAntivirusLargeFileOpen.setStatus("current")


class _EqlNASApplianceDefaultNFSExportsFileId32bit_Type(Integer32):
    """Custom type eqlNASApplianceDefaultNFSExportsFileId32bit based on Integer32"""
    defaultValue = 0

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


_EqlNASApplianceDefaultNFSExportsFileId32bit_Type.__name__ = "Integer32"
_EqlNASApplianceDefaultNFSExportsFileId32bit_Object = MibTableColumn
eqlNASApplianceDefaultNFSExportsFileId32bit = _EqlNASApplianceDefaultNFSExportsFileId32bit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 4, 1, 30),
    _EqlNASApplianceDefaultNFSExportsFileId32bit_Type()
)
eqlNASApplianceDefaultNFSExportsFileId32bit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceDefaultNFSExportsFileId32bit.setStatus("current")
_EqlNASContainerStatusTable_Object = MibTable
eqlNASContainerStatusTable = _EqlNASContainerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5)
)
if mibBuilder.loadTexts:
    eqlNASContainerStatusTable.setStatus("current")
_EqlNASContainerStatusEntry_Object = MibTableRow
eqlNASContainerStatusEntry = _EqlNASContainerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1)
)
eqlNASContainerStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
)
if mibBuilder.loadTexts:
    eqlNASContainerStatusEntry.setStatus("current")
_EqlNASContainerStatusConnections_Type = Unsigned32
_EqlNASContainerStatusConnections_Object = MibTableColumn
eqlNASContainerStatusConnections = _EqlNASContainerStatusConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 1),
    _EqlNASContainerStatusConnections_Type()
)
eqlNASContainerStatusConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusConnections.setStatus("current")
_EqlNASContainerStatusUsedSpace_Type = Unsigned32
_EqlNASContainerStatusUsedSpace_Object = MibTableColumn
eqlNASContainerStatusUsedSpace = _EqlNASContainerStatusUsedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 2),
    _EqlNASContainerStatusUsedSpace_Type()
)
eqlNASContainerStatusUsedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusUsedSpace.setStatus("current")
_EqlNASContainerStatusSnapshotSpace_Type = Unsigned32
_EqlNASContainerStatusSnapshotSpace_Object = MibTableColumn
eqlNASContainerStatusSnapshotSpace = _EqlNASContainerStatusSnapshotSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 3),
    _EqlNASContainerStatusSnapshotSpace_Type()
)
eqlNASContainerStatusSnapshotSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusSnapshotSpace.setStatus("current")
_EqlNASContainerStatusNumNFSExports_Type = Unsigned32
_EqlNASContainerStatusNumNFSExports_Object = MibTableColumn
eqlNASContainerStatusNumNFSExports = _EqlNASContainerStatusNumNFSExports_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 4),
    _EqlNASContainerStatusNumNFSExports_Type()
)
eqlNASContainerStatusNumNFSExports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusNumNFSExports.setStatus("current")
_EqlNASContainerStatusNumCIFSShares_Type = Unsigned32
_EqlNASContainerStatusNumCIFSShares_Object = MibTableColumn
eqlNASContainerStatusNumCIFSShares = _EqlNASContainerStatusNumCIFSShares_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 5),
    _EqlNASContainerStatusNumCIFSShares_Type()
)
eqlNASContainerStatusNumCIFSShares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusNumCIFSShares.setStatus("current")
_EqlNASContainerStatusAllocatedSpace_Type = Unsigned32
_EqlNASContainerStatusAllocatedSpace_Object = MibTableColumn
eqlNASContainerStatusAllocatedSpace = _EqlNASContainerStatusAllocatedSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 6),
    _EqlNASContainerStatusAllocatedSpace_Type()
)
eqlNASContainerStatusAllocatedSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusAllocatedSpace.setStatus("current")
_EqlNASContainerStatusFreeSpace_Type = Unsigned32
_EqlNASContainerStatusFreeSpace_Object = MibTableColumn
eqlNASContainerStatusFreeSpace = _EqlNASContainerStatusFreeSpace_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 7),
    _EqlNASContainerStatusFreeSpace_Type()
)
eqlNASContainerStatusFreeSpace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusFreeSpace.setStatus("current")
_EqlNASContainerStatusNumOfSnapshots_Type = Unsigned32
_EqlNASContainerStatusNumOfSnapshots_Object = MibTableColumn
eqlNASContainerStatusNumOfSnapshots = _EqlNASContainerStatusNumOfSnapshots_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 8),
    _EqlNASContainerStatusNumOfSnapshots_Type()
)
eqlNASContainerStatusNumOfSnapshots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusNumOfSnapshots.setStatus("current")
_EqlNASContainerStatusOptimizationSpaceSavings_Type = Unsigned32
_EqlNASContainerStatusOptimizationSpaceSavings_Object = MibTableColumn
eqlNASContainerStatusOptimizationSpaceSavings = _EqlNASContainerStatusOptimizationSpaceSavings_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 9),
    _EqlNASContainerStatusOptimizationSpaceSavings_Type()
)
eqlNASContainerStatusOptimizationSpaceSavings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusOptimizationSpaceSavings.setStatus("current")
_EqlNASContainerStatusOptimized_Type = TruthValue
_EqlNASContainerStatusOptimized_Object = MibTableColumn
eqlNASContainerStatusOptimized = _EqlNASContainerStatusOptimized_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 10),
    _EqlNASContainerStatusOptimized_Type()
)
eqlNASContainerStatusOptimized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusOptimized.setStatus("current")


class _EqlNASContainerStatusReplState_Type(Integer32):
    """Custom type eqlNASContainerStatusReplState based on Integer32"""
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
        *(("destination", 2),
          ("not-available", 4),
          ("promoted", 3),
          ("source", 1),
          ("standalone", 0))
    )


_EqlNASContainerStatusReplState_Type.__name__ = "Integer32"
_EqlNASContainerStatusReplState_Object = MibTableColumn
eqlNASContainerStatusReplState = _EqlNASContainerStatusReplState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 11),
    _EqlNASContainerStatusReplState_Type()
)
eqlNASContainerStatusReplState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusReplState.setStatus("current")
_EqlNASContainerStatusNextSnapshotID_Type = Unsigned32
_EqlNASContainerStatusNextSnapshotID_Object = MibTableColumn
eqlNASContainerStatusNextSnapshotID = _EqlNASContainerStatusNextSnapshotID_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 5, 1, 12),
    _EqlNASContainerStatusNextSnapshotID_Type()
)
eqlNASContainerStatusNextSnapshotID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerStatusNextSnapshotID.setStatus("current")
_EqlNASApplianceNFSExportsTable_Object = MibTable
eqlNASApplianceNFSExportsTable = _EqlNASApplianceNFSExportsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6)
)
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportsTable.setStatus("current")
_EqlNASApplianceNFSExportsEntry_Object = MibTableRow
eqlNASApplianceNFSExportsEntry = _EqlNASApplianceNFSExportsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1)
)
eqlNASApplianceNFSExportsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASApplianceNFSExportName"),
)
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportsEntry.setStatus("current")


class _EqlNASApplianceNFSExportName_Type(OctetString):
    """Custom type eqlNASApplianceNFSExportName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASApplianceNFSExportName_Type.__name__ = "OctetString"
_EqlNASApplianceNFSExportName_Object = MibTableColumn
eqlNASApplianceNFSExportName = _EqlNASApplianceNFSExportName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 1),
    _EqlNASApplianceNFSExportName_Type()
)
eqlNASApplianceNFSExportName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportName.setStatus("current")
_EqlNASApplianceNFSExportsRowStatus_Type = RowStatus
_EqlNASApplianceNFSExportsRowStatus_Object = MibTableColumn
eqlNASApplianceNFSExportsRowStatus = _EqlNASApplianceNFSExportsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 2),
    _EqlNASApplianceNFSExportsRowStatus_Type()
)
eqlNASApplianceNFSExportsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportsRowStatus.setStatus("current")


class _EqlNASApplianceNFSExportDirectory_Type(OctetString):
    """Custom type eqlNASApplianceNFSExportDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_EqlNASApplianceNFSExportDirectory_Type.__name__ = "OctetString"
_EqlNASApplianceNFSExportDirectory_Object = MibTableColumn
eqlNASApplianceNFSExportDirectory = _EqlNASApplianceNFSExportDirectory_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 3),
    _EqlNASApplianceNFSExportDirectory_Type()
)
eqlNASApplianceNFSExportDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportDirectory.setStatus("current")


class _EqlNASApplianceNFSAccess_Type(Integer32):
    """Custom type eqlNASApplianceNFSAccess based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("read-only", 2),
          ("read-write", 1))
    )


_EqlNASApplianceNFSAccess_Type.__name__ = "Integer32"
_EqlNASApplianceNFSAccess_Object = MibTableColumn
eqlNASApplianceNFSAccess = _EqlNASApplianceNFSAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 4),
    _EqlNASApplianceNFSAccess_Type()
)
eqlNASApplianceNFSAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSAccess.setStatus("current")


class _EqlNASApplianceNFSLimitReportedSize_Type(Unsigned32):
    """Custom type eqlNASApplianceNFSLimitReportedSize based on Unsigned32"""
    defaultValue = 0


_EqlNASApplianceNFSLimitReportedSize_Object = MibTableColumn
eqlNASApplianceNFSLimitReportedSize = _EqlNASApplianceNFSLimitReportedSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 5),
    _EqlNASApplianceNFSLimitReportedSize_Type()
)
eqlNASApplianceNFSLimitReportedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSLimitReportedSize.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSLimitReportedSize.setUnits("MB")
_EqlNASApplianceNFSAccessClientIPType_Type = InetAddressType
_EqlNASApplianceNFSAccessClientIPType_Object = MibTableColumn
eqlNASApplianceNFSAccessClientIPType = _EqlNASApplianceNFSAccessClientIPType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 6),
    _EqlNASApplianceNFSAccessClientIPType_Type()
)
eqlNASApplianceNFSAccessClientIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSAccessClientIPType.setStatus("current")
_EqlNASApplianceNFSAccessClientIP_Type = InetAddress
_EqlNASApplianceNFSAccessClientIP_Object = MibTableColumn
eqlNASApplianceNFSAccessClientIP = _EqlNASApplianceNFSAccessClientIP_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 7),
    _EqlNASApplianceNFSAccessClientIP_Type()
)
eqlNASApplianceNFSAccessClientIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSAccessClientIP.setStatus("current")
_EqlNASApplianceNFSAccessClientNetmaskType_Type = InetAddressType
_EqlNASApplianceNFSAccessClientNetmaskType_Object = MibTableColumn
eqlNASApplianceNFSAccessClientNetmaskType = _EqlNASApplianceNFSAccessClientNetmaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 8),
    _EqlNASApplianceNFSAccessClientNetmaskType_Type()
)
eqlNASApplianceNFSAccessClientNetmaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSAccessClientNetmaskType.setStatus("current")
_EqlNASApplianceNFSAccessClientNetmask_Type = InetAddress
_EqlNASApplianceNFSAccessClientNetmask_Object = MibTableColumn
eqlNASApplianceNFSAccessClientNetmask = _EqlNASApplianceNFSAccessClientNetmask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 9),
    _EqlNASApplianceNFSAccessClientNetmask_Type()
)
eqlNASApplianceNFSAccessClientNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSAccessClientNetmask.setStatus("current")


class _EqlNASApplianceNFSTrustUsers_Type(Integer32):
    """Custom type eqlNASApplianceNFSTrustUsers based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 3),
          ("all-except-root", 1),
          ("none", 2))
    )


_EqlNASApplianceNFSTrustUsers_Type.__name__ = "Integer32"
_EqlNASApplianceNFSTrustUsers_Object = MibTableColumn
eqlNASApplianceNFSTrustUsers = _EqlNASApplianceNFSTrustUsers_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 10),
    _EqlNASApplianceNFSTrustUsers_Type()
)
eqlNASApplianceNFSTrustUsers.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSTrustUsers.setStatus("current")


class _EqlNASApplianceNFSExportsFileId32bit_Type(Integer32):
    """Custom type eqlNASApplianceNFSExportsFileId32bit based on Integer32"""
    defaultValue = 0

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


_EqlNASApplianceNFSExportsFileId32bit_Type.__name__ = "Integer32"
_EqlNASApplianceNFSExportsFileId32bit_Object = MibTableColumn
eqlNASApplianceNFSExportsFileId32bit = _EqlNASApplianceNFSExportsFileId32bit_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 6, 1, 11),
    _EqlNASApplianceNFSExportsFileId32bit_Type()
)
eqlNASApplianceNFSExportsFileId32bit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceNFSExportsFileId32bit.setStatus("current")
_EqlNASApplianceCIFSTable_Object = MibTable
eqlNASApplianceCIFSTable = _EqlNASApplianceCIFSTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8)
)
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSTable.setStatus("current")
_EqlNASApplianceCIFSEntry_Object = MibTableRow
eqlNASApplianceCIFSEntry = _EqlNASApplianceCIFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1)
)
eqlNASApplianceCIFSEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASApplianceCIFSShareName"),
)
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSEntry.setStatus("current")


class _EqlNASApplianceCIFSShareName_Type(OctetString):
    """Custom type eqlNASApplianceCIFSShareName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASApplianceCIFSShareName_Type.__name__ = "OctetString"
_EqlNASApplianceCIFSShareName_Object = MibTableColumn
eqlNASApplianceCIFSShareName = _EqlNASApplianceCIFSShareName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 1),
    _EqlNASApplianceCIFSShareName_Type()
)
eqlNASApplianceCIFSShareName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSShareName.setStatus("current")
_EqlNASApplianceCIFSRowStatus_Type = RowStatus
_EqlNASApplianceCIFSRowStatus_Object = MibTableColumn
eqlNASApplianceCIFSRowStatus = _EqlNASApplianceCIFSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 2),
    _EqlNASApplianceCIFSRowStatus_Type()
)
eqlNASApplianceCIFSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSRowStatus.setStatus("current")


class _EqlNASApplianceCIFSExportedDirectory_Type(OctetString):
    """Custom type eqlNASApplianceCIFSExportedDirectory based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_EqlNASApplianceCIFSExportedDirectory_Type.__name__ = "OctetString"
_EqlNASApplianceCIFSExportedDirectory_Object = MibTableColumn
eqlNASApplianceCIFSExportedDirectory = _EqlNASApplianceCIFSExportedDirectory_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 3),
    _EqlNASApplianceCIFSExportedDirectory_Type()
)
eqlNASApplianceCIFSExportedDirectory.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSExportedDirectory.setStatus("current")


class _EqlNASApplianceCIFSAllowGuestAccess_Type(TruthValue):
    """Custom type eqlNASApplianceCIFSAllowGuestAccess based on TruthValue"""


_EqlNASApplianceCIFSAllowGuestAccess_Object = MibTableColumn
eqlNASApplianceCIFSAllowGuestAccess = _EqlNASApplianceCIFSAllowGuestAccess_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 4),
    _EqlNASApplianceCIFSAllowGuestAccess_Type()
)
eqlNASApplianceCIFSAllowGuestAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAllowGuestAccess.setStatus("current")


class _EqlNASApplianceCIFSLockEnforcement_Type(Integer32):
    """Custom type eqlNASApplianceCIFSLockEnforcement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all-locks", 0),
          ("no-byte-range-locks", 1),
          ("only-share-locks", 2))
    )


_EqlNASApplianceCIFSLockEnforcement_Type.__name__ = "Integer32"
_EqlNASApplianceCIFSLockEnforcement_Object = MibTableColumn
eqlNASApplianceCIFSLockEnforcement = _EqlNASApplianceCIFSLockEnforcement_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 5),
    _EqlNASApplianceCIFSLockEnforcement_Type()
)
eqlNASApplianceCIFSLockEnforcement.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSLockEnforcement.setStatus("current")


class _EqlNASApplianceCIFSAntivirusEnabled_Type(StatusDisabledDefault):
    """Custom type eqlNASApplianceCIFSAntivirusEnabled based on StatusDisabledDefault"""


_EqlNASApplianceCIFSAntivirusEnabled_Object = MibTableColumn
eqlNASApplianceCIFSAntivirusEnabled = _EqlNASApplianceCIFSAntivirusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 6),
    _EqlNASApplianceCIFSAntivirusEnabled_Type()
)
eqlNASApplianceCIFSAntivirusEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAntivirusEnabled.setStatus("current")


class _EqlNASApplianceCIFSAntivirusPolicy_Type(Integer32):
    """Custom type eqlNASApplianceCIFSAntivirusPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("do-nothing", 1),
          ("quarantine", 0),
          ("remove", 2))
    )


_EqlNASApplianceCIFSAntivirusPolicy_Type.__name__ = "Integer32"
_EqlNASApplianceCIFSAntivirusPolicy_Object = MibTableColumn
eqlNASApplianceCIFSAntivirusPolicy = _EqlNASApplianceCIFSAntivirusPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 7),
    _EqlNASApplianceCIFSAntivirusPolicy_Type()
)
eqlNASApplianceCIFSAntivirusPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAntivirusPolicy.setStatus("current")


class _EqlNASApplianceCIFSAntivirusExtensions_Type(OctetString):
    """Custom type eqlNASApplianceCIFSAntivirusExtensions based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlNASApplianceCIFSAntivirusExtensions_Type.__name__ = "OctetString"
_EqlNASApplianceCIFSAntivirusExtensions_Object = MibTableColumn
eqlNASApplianceCIFSAntivirusExtensions = _EqlNASApplianceCIFSAntivirusExtensions_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 8),
    _EqlNASApplianceCIFSAntivirusExtensions_Type()
)
eqlNASApplianceCIFSAntivirusExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAntivirusExtensions.setStatus("current")


class _EqlNASApplianceCIFSAntivirusExtensionsPolicy_Type(Integer32):
    """Custom type eqlNASApplianceCIFSAntivirusExtensionsPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 0),
          ("include", 1))
    )


_EqlNASApplianceCIFSAntivirusExtensionsPolicy_Type.__name__ = "Integer32"
_EqlNASApplianceCIFSAntivirusExtensionsPolicy_Object = MibTableColumn
eqlNASApplianceCIFSAntivirusExtensionsPolicy = _EqlNASApplianceCIFSAntivirusExtensionsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 9),
    _EqlNASApplianceCIFSAntivirusExtensionsPolicy_Type()
)
eqlNASApplianceCIFSAntivirusExtensionsPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAntivirusExtensionsPolicy.setStatus("current")


class _EqlNASApplianceCIFSAntivirusExcludeDirPaths_Type(OctetString):
    """Custom type eqlNASApplianceCIFSAntivirusExcludeDirPaths based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_EqlNASApplianceCIFSAntivirusExcludeDirPaths_Type.__name__ = "OctetString"
_EqlNASApplianceCIFSAntivirusExcludeDirPaths_Object = MibTableColumn
eqlNASApplianceCIFSAntivirusExcludeDirPaths = _EqlNASApplianceCIFSAntivirusExcludeDirPaths_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 10),
    _EqlNASApplianceCIFSAntivirusExcludeDirPaths_Type()
)
eqlNASApplianceCIFSAntivirusExcludeDirPaths.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAntivirusExcludeDirPaths.setStatus("current")


class _EqlNASApplianceCIFSAntivirusLargeFileSize_Type(Unsigned32):
    """Custom type eqlNASApplianceCIFSAntivirusLargeFileSize based on Unsigned32"""
    defaultValue = 3072


_EqlNASApplianceCIFSAntivirusLargeFileSize_Object = MibTableColumn
eqlNASApplianceCIFSAntivirusLargeFileSize = _EqlNASApplianceCIFSAntivirusLargeFileSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 11),
    _EqlNASApplianceCIFSAntivirusLargeFileSize_Type()
)
eqlNASApplianceCIFSAntivirusLargeFileSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAntivirusLargeFileSize.setStatus("current")


class _EqlNASApplianceCIFSAntivirusLargeFileOpen_Type(Integer32):
    """Custom type eqlNASApplianceCIFSAntivirusLargeFileOpen based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("deny", 0))
    )


_EqlNASApplianceCIFSAntivirusLargeFileOpen_Type.__name__ = "Integer32"
_EqlNASApplianceCIFSAntivirusLargeFileOpen_Object = MibTableColumn
eqlNASApplianceCIFSAntivirusLargeFileOpen = _EqlNASApplianceCIFSAntivirusLargeFileOpen_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 8, 1, 12),
    _EqlNASApplianceCIFSAntivirusLargeFileOpen_Type()
)
eqlNASApplianceCIFSAntivirusLargeFileOpen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceCIFSAntivirusLargeFileOpen.setStatus("current")
_EqlNASContainerDirectoryOpsTable_Object = MibTable
eqlNASContainerDirectoryOpsTable = _EqlNASContainerDirectoryOpsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 9)
)
if mibBuilder.loadTexts:
    eqlNASContainerDirectoryOpsTable.setStatus("current")
_EqlNASContainerDirectoryOpsEntry_Object = MibTableRow
eqlNASContainerDirectoryOpsEntry = _EqlNASContainerDirectoryOpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 9, 1)
)
eqlNASContainerDirectoryOpsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerDirectoryOpsIndex"),
)
if mibBuilder.loadTexts:
    eqlNASContainerDirectoryOpsEntry.setStatus("current")
_EqlNASContainerDirectoryOpsIndex_Type = Unsigned32
_EqlNASContainerDirectoryOpsIndex_Object = MibTableColumn
eqlNASContainerDirectoryOpsIndex = _EqlNASContainerDirectoryOpsIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 9, 1, 1),
    _EqlNASContainerDirectoryOpsIndex_Type()
)
eqlNASContainerDirectoryOpsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASContainerDirectoryOpsIndex.setStatus("current")
_EqlNASContainerDirectoryRowStatus_Type = RowStatus
_EqlNASContainerDirectoryRowStatus_Object = MibTableColumn
eqlNASContainerDirectoryRowStatus = _EqlNASContainerDirectoryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 9, 1, 2),
    _EqlNASContainerDirectoryRowStatus_Type()
)
eqlNASContainerDirectoryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDirectoryRowStatus.setStatus("current")


class _EqlNASContainerDirectoryName_Type(OctetString):
    """Custom type eqlNASContainerDirectoryName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 512),
    )


_EqlNASContainerDirectoryName_Type.__name__ = "OctetString"
_EqlNASContainerDirectoryName_Object = MibTableColumn
eqlNASContainerDirectoryName = _EqlNASContainerDirectoryName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 9, 1, 3),
    _EqlNASContainerDirectoryName_Type()
)
eqlNASContainerDirectoryName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDirectoryName.setStatus("current")


class _EqlNASContainerDirectoryCaseInsensitive_Type(Integer32):
    """Custom type eqlNASContainerDirectoryCaseInsensitive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 0))
    )


_EqlNASContainerDirectoryCaseInsensitive_Type.__name__ = "Integer32"
_EqlNASContainerDirectoryCaseInsensitive_Object = MibTableColumn
eqlNASContainerDirectoryCaseInsensitive = _EqlNASContainerDirectoryCaseInsensitive_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 9, 1, 4),
    _EqlNASContainerDirectoryCaseInsensitive_Type()
)
eqlNASContainerDirectoryCaseInsensitive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerDirectoryCaseInsensitive.setStatus("current")
_EqlNASReplSiteTable_Object = MibTable
eqlNASReplSiteTable = _EqlNASReplSiteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10)
)
if mibBuilder.loadTexts:
    eqlNASReplSiteTable.setStatus("current")
_EqlNASReplSiteEntry_Object = MibTableRow
eqlNASReplSiteEntry = _EqlNASReplSiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1)
)
eqlNASReplSiteEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplSitePartnershipId"),
)
if mibBuilder.loadTexts:
    eqlNASReplSiteEntry.setStatus("current")
_EqlNASReplSitePartnershipId_Type = Unsigned32
_EqlNASReplSitePartnershipId_Object = MibTableColumn
eqlNASReplSitePartnershipId = _EqlNASReplSitePartnershipId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 1),
    _EqlNASReplSitePartnershipId_Type()
)
eqlNASReplSitePartnershipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplSitePartnershipId.setStatus("current")
_EqlNASReplSiteRowStatus_Type = RowStatus
_EqlNASReplSiteRowStatus_Object = MibTableColumn
eqlNASReplSiteRowStatus = _EqlNASReplSiteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 2),
    _EqlNASReplSiteRowStatus_Type()
)
eqlNASReplSiteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplSiteRowStatus.setStatus("current")
_EqlNASReplSiteVolumeReplSiteIndex_Type = SiteIndex
_EqlNASReplSiteVolumeReplSiteIndex_Object = MibTableColumn
eqlNASReplSiteVolumeReplSiteIndex = _EqlNASReplSiteVolumeReplSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 3),
    _EqlNASReplSiteVolumeReplSiteIndex_Type()
)
eqlNASReplSiteVolumeReplSiteIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplSiteVolumeReplSiteIndex.setStatus("current")
_EqlNASReplSiteLocalClusterInetAddrType_Type = InetAddressType
_EqlNASReplSiteLocalClusterInetAddrType_Object = MibTableColumn
eqlNASReplSiteLocalClusterInetAddrType = _EqlNASReplSiteLocalClusterInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 4),
    _EqlNASReplSiteLocalClusterInetAddrType_Type()
)
eqlNASReplSiteLocalClusterInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplSiteLocalClusterInetAddrType.setStatus("current")
_EqlNASReplSiteLocalClusterInetAddr_Type = InetAddress
_EqlNASReplSiteLocalClusterInetAddr_Object = MibTableColumn
eqlNASReplSiteLocalClusterInetAddr = _EqlNASReplSiteLocalClusterInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 5),
    _EqlNASReplSiteLocalClusterInetAddr_Type()
)
eqlNASReplSiteLocalClusterInetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplSiteLocalClusterInetAddr.setStatus("current")
_EqlNASReplSiteRemoteClusterInetAddrType_Type = InetAddressType
_EqlNASReplSiteRemoteClusterInetAddrType_Object = MibTableColumn
eqlNASReplSiteRemoteClusterInetAddrType = _EqlNASReplSiteRemoteClusterInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 6),
    _EqlNASReplSiteRemoteClusterInetAddrType_Type()
)
eqlNASReplSiteRemoteClusterInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteClusterInetAddrType.setStatus("current")
_EqlNASReplSiteRemoteClusterInetAddr_Type = InetAddress
_EqlNASReplSiteRemoteClusterInetAddr_Object = MibTableColumn
eqlNASReplSiteRemoteClusterInetAddr = _EqlNASReplSiteRemoteClusterInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 7),
    _EqlNASReplSiteRemoteClusterInetAddr_Type()
)
eqlNASReplSiteRemoteClusterInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteClusterInetAddr.setStatus("current")


class _EqlNASReplSitePartnershipState_Type(Integer32):
    """Custom type eqlNASReplSitePartnershipState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configured", 2),
          ("enabled", 1),
          ("none", 0))
    )


_EqlNASReplSitePartnershipState_Type.__name__ = "Integer32"
_EqlNASReplSitePartnershipState_Object = MibTableColumn
eqlNASReplSitePartnershipState = _EqlNASReplSitePartnershipState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 8),
    _EqlNASReplSitePartnershipState_Type()
)
eqlNASReplSitePartnershipState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSitePartnershipState.setStatus("current")


class _EqlNASReplSiteUserName_Type(OctetString):
    """Custom type eqlNASReplSiteUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlNASReplSiteUserName_Type.__name__ = "OctetString"
_EqlNASReplSiteUserName_Object = MibTableColumn
eqlNASReplSiteUserName = _EqlNASReplSiteUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 9),
    _EqlNASReplSiteUserName_Type()
)
eqlNASReplSiteUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteUserName.setStatus("current")


class _EqlNASReplSitePassword_Type(OctetString):
    """Custom type eqlNASReplSitePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlNASReplSitePassword_Type.__name__ = "OctetString"
_EqlNASReplSitePassword_Object = MibTableColumn
eqlNASReplSitePassword = _EqlNASReplSitePassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 10),
    _EqlNASReplSitePassword_Type()
)
eqlNASReplSitePassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASReplSitePassword.setStatus("current")


class _EqlNASReplSiteRemoteClusterName_Type(OctetString):
    """Custom type eqlNASReplSiteRemoteClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASReplSiteRemoteClusterName_Type.__name__ = "OctetString"
_EqlNASReplSiteRemoteClusterName_Object = MibTableColumn
eqlNASReplSiteRemoteClusterName = _EqlNASReplSiteRemoteClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 11),
    _EqlNASReplSiteRemoteClusterName_Type()
)
eqlNASReplSiteRemoteClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteClusterName.setStatus("current")


class _EqlNASReplSiteAction_Type(Integer32):
    """Custom type eqlNASReplSiteAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configure", 1),
          ("delete", 2),
          ("none", 0))
    )


_EqlNASReplSiteAction_Type.__name__ = "Integer32"
_EqlNASReplSiteAction_Object = MibTableColumn
eqlNASReplSiteAction = _EqlNASReplSiteAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 12),
    _EqlNASReplSiteAction_Type()
)
eqlNASReplSiteAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteAction.setStatus("current")


class _EqlNASReplSiteRemoteUserName_Type(OctetString):
    """Custom type eqlNASReplSiteRemoteUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EqlNASReplSiteRemoteUserName_Type.__name__ = "OctetString"
_EqlNASReplSiteRemoteUserName_Object = MibTableColumn
eqlNASReplSiteRemoteUserName = _EqlNASReplSiteRemoteUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 13),
    _EqlNASReplSiteRemoteUserName_Type()
)
eqlNASReplSiteRemoteUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteUserName.setStatus("current")


class _EqlNASReplSiteRemotePassword_Type(OctetString):
    """Custom type eqlNASReplSiteRemotePassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EqlNASReplSiteRemotePassword_Type.__name__ = "OctetString"
_EqlNASReplSiteRemotePassword_Object = MibTableColumn
eqlNASReplSiteRemotePassword = _EqlNASReplSiteRemotePassword_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 14),
    _EqlNASReplSiteRemotePassword_Type()
)
eqlNASReplSiteRemotePassword.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemotePassword.setStatus("current")
_EqlNASReplSiteRemoteClusterId_Type = ClusterIdType
_EqlNASReplSiteRemoteClusterId_Object = MibTableColumn
eqlNASReplSiteRemoteClusterId = _EqlNASReplSiteRemoteClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 15),
    _EqlNASReplSiteRemoteClusterId_Type()
)
eqlNASReplSiteRemoteClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteClusterId.setStatus("current")
_EqlNASReplSiteRemoteClusterMPV_Type = Unsigned32
_EqlNASReplSiteRemoteClusterMPV_Object = MibTableColumn
eqlNASReplSiteRemoteClusterMPV = _EqlNASReplSiteRemoteClusterMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 16),
    _EqlNASReplSiteRemoteClusterMPV_Type()
)
eqlNASReplSiteRemoteClusterMPV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteClusterMPV.setStatus("current")
_EqlNASReplSiteRemoteNetworkAddrType_Type = InetAddressType
_EqlNASReplSiteRemoteNetworkAddrType_Object = MibTableColumn
eqlNASReplSiteRemoteNetworkAddrType = _EqlNASReplSiteRemoteNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 17),
    _EqlNASReplSiteRemoteNetworkAddrType_Type()
)
eqlNASReplSiteRemoteNetworkAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteNetworkAddrType.setStatus("current")
_EqlNASReplSiteRemoteNetworkAddr_Type = InetAddress
_EqlNASReplSiteRemoteNetworkAddr_Object = MibTableColumn
eqlNASReplSiteRemoteNetworkAddr = _EqlNASReplSiteRemoteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 18),
    _EqlNASReplSiteRemoteNetworkAddr_Type()
)
eqlNASReplSiteRemoteNetworkAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteNetworkAddr.setStatus("current")
_EqlNASReplSiteRemoteNetworkMask_Type = InetAddress
_EqlNASReplSiteRemoteNetworkMask_Object = MibTableColumn
eqlNASReplSiteRemoteNetworkMask = _EqlNASReplSiteRemoteNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 10, 1, 19),
    _EqlNASReplSiteRemoteNetworkMask_Type()
)
eqlNASReplSiteRemoteNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplSiteRemoteNetworkMask.setStatus("current")
_EqlNASReplicationTable_Object = MibTable
eqlNASReplicationTable = _EqlNASReplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11)
)
if mibBuilder.loadTexts:
    eqlNASReplicationTable.setStatus("current")
_EqlNASReplicationEntry_Object = MibTableRow
eqlNASReplicationEntry = _EqlNASReplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1)
)
eqlNASReplicationEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplSitePartnershipId"),
    (0, "EQLNAS-MIB", "eqlNASReplicationId"),
)
if mibBuilder.loadTexts:
    eqlNASReplicationEntry.setStatus("current")
_EqlNASReplicationId_Type = Unsigned32
_EqlNASReplicationId_Object = MibTableColumn
eqlNASReplicationId = _EqlNASReplicationId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 1),
    _EqlNASReplicationId_Type()
)
eqlNASReplicationId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplicationId.setStatus("current")
_EqlNASReplicationRowStatus_Type = RowStatus
_EqlNASReplicationRowStatus_Object = MibTableColumn
eqlNASReplicationRowStatus = _EqlNASReplicationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 2),
    _EqlNASReplicationRowStatus_Type()
)
eqlNASReplicationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplicationRowStatus.setStatus("current")
_EqlNASReplicationLastRecoveryTime_Type = Counter32
_EqlNASReplicationLastRecoveryTime_Object = MibTableColumn
eqlNASReplicationLastRecoveryTime = _EqlNASReplicationLastRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 3),
    _EqlNASReplicationLastRecoveryTime_Type()
)
eqlNASReplicationLastRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationLastRecoveryTime.setStatus("current")
_EqlNASReplicationNextRecoveryTime_Type = Counter32
_EqlNASReplicationNextRecoveryTime_Object = MibTableColumn
eqlNASReplicationNextRecoveryTime = _EqlNASReplicationNextRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 4),
    _EqlNASReplicationNextRecoveryTime_Type()
)
eqlNASReplicationNextRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationNextRecoveryTime.setStatus("current")


class _EqlNASReplicationSourceClusterName_Type(OctetString):
    """Custom type eqlNASReplicationSourceClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASReplicationSourceClusterName_Type.__name__ = "OctetString"
_EqlNASReplicationSourceClusterName_Object = MibTableColumn
eqlNASReplicationSourceClusterName = _EqlNASReplicationSourceClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 5),
    _EqlNASReplicationSourceClusterName_Type()
)
eqlNASReplicationSourceClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationSourceClusterName.setStatus("current")
_EqlNASReplicationSourceFSId_Type = Unsigned32
_EqlNASReplicationSourceFSId_Object = MibTableColumn
eqlNASReplicationSourceFSId = _EqlNASReplicationSourceFSId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 6),
    _EqlNASReplicationSourceFSId_Type()
)
eqlNASReplicationSourceFSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationSourceFSId.setStatus("current")


class _EqlNASReplicationSourceFSName_Type(OctetString):
    """Custom type eqlNASReplicationSourceFSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASReplicationSourceFSName_Type.__name__ = "OctetString"
_EqlNASReplicationSourceFSName_Object = MibTableColumn
eqlNASReplicationSourceFSName = _EqlNASReplicationSourceFSName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 7),
    _EqlNASReplicationSourceFSName_Type()
)
eqlNASReplicationSourceFSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplicationSourceFSName.setStatus("current")


class _EqlNASReplicationDestClusterName_Type(OctetString):
    """Custom type eqlNASReplicationDestClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASReplicationDestClusterName_Type.__name__ = "OctetString"
_EqlNASReplicationDestClusterName_Object = MibTableColumn
eqlNASReplicationDestClusterName = _EqlNASReplicationDestClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 8),
    _EqlNASReplicationDestClusterName_Type()
)
eqlNASReplicationDestClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationDestClusterName.setStatus("current")
_EqlNASReplicationDestFSId_Type = Unsigned32
_EqlNASReplicationDestFSId_Object = MibTableColumn
eqlNASReplicationDestFSId = _EqlNASReplicationDestFSId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 9),
    _EqlNASReplicationDestFSId_Type()
)
eqlNASReplicationDestFSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationDestFSId.setStatus("current")


class _EqlNASReplicationDestFSName_Type(OctetString):
    """Custom type eqlNASReplicationDestFSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASReplicationDestFSName_Type.__name__ = "OctetString"
_EqlNASReplicationDestFSName_Object = MibTableColumn
eqlNASReplicationDestFSName = _EqlNASReplicationDestFSName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 10),
    _EqlNASReplicationDestFSName_Type()
)
eqlNASReplicationDestFSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplicationDestFSName.setStatus("current")
_EqlNASReplicationStatus_Type = EqlNASReplicationStatus
_EqlNASReplicationStatus_Object = MibTableColumn
eqlNASReplicationStatus = _EqlNASReplicationStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 11),
    _EqlNASReplicationStatus_Type()
)
eqlNASReplicationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationStatus.setStatus("current")
_EqlNASReplicationMinToComplete_Type = Unsigned32
_EqlNASReplicationMinToComplete_Object = MibTableColumn
eqlNASReplicationMinToComplete = _EqlNASReplicationMinToComplete_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 12),
    _EqlNASReplicationMinToComplete_Type()
)
eqlNASReplicationMinToComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationMinToComplete.setStatus("current")
_EqlNASReplicationTransferredPer_Type = Unsigned32
_EqlNASReplicationTransferredPer_Object = MibTableColumn
eqlNASReplicationTransferredPer = _EqlNASReplicationTransferredPer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 13),
    _EqlNASReplicationTransferredPer_Type()
)
eqlNASReplicationTransferredPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationTransferredPer.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASReplicationTransferredPer.setUnits("%")


class _EqlNASReplicationAction_Type(Integer32):
    """Custom type eqlNASReplicationAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 4),
          ("delete", 8),
          ("demote", 5),
          ("force-delete", 9),
          ("force-promote", 7),
          ("inbound-delete", 102),
          ("inbound-delete-failback", 107),
          ("inbound-delete-failback-restore-cfg", 108),
          ("inbound-promote", 103),
          ("inbound-promote-keep-demote", 105),
          ("inbound-promote-keep-demote-restore-cfg", 106),
          ("inbound-promote-restore-cfg", 104),
          ("none", 0),
          ("outbound-delete", 100),
          ("outbound-force-delete", 101),
          ("pause", 2),
          ("promote", 6),
          ("replicate", 1),
          ("restore-cfg", 109),
          ("resume", 3))
    )


_EqlNASReplicationAction_Type.__name__ = "Integer32"
_EqlNASReplicationAction_Object = MibTableColumn
eqlNASReplicationAction = _EqlNASReplicationAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 11, 1, 14),
    _EqlNASReplicationAction_Type()
)
eqlNASReplicationAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplicationAction.setStatus("current")
_EqlNASReplPartnerInfoMapTable_Object = MibTable
eqlNASReplPartnerInfoMapTable = _EqlNASReplPartnerInfoMapTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12)
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapTable.setStatus("current")
_EqlNASReplPartnerInfoMapEntry_Object = MibTableRow
eqlNASReplPartnerInfoMapEntry = _EqlNASReplPartnerInfoMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1)
)
eqlNASReplPartnerInfoMapEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapEntry.setStatus("current")
_EqlNASReplPartnerInfoMapRowStatus_Type = RowStatus
_EqlNASReplPartnerInfoMapRowStatus_Object = MibTableColumn
eqlNASReplPartnerInfoMapRowStatus = _EqlNASReplPartnerInfoMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 1),
    _EqlNASReplPartnerInfoMapRowStatus_Type()
)
eqlNASReplPartnerInfoMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapRowStatus.setStatus("current")


class _EqlNASReplPartnerInfoMapClusterName_Type(OctetString):
    """Custom type eqlNASReplPartnerInfoMapClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASReplPartnerInfoMapClusterName_Type.__name__ = "OctetString"
_EqlNASReplPartnerInfoMapClusterName_Object = MibTableColumn
eqlNASReplPartnerInfoMapClusterName = _EqlNASReplPartnerInfoMapClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 2),
    _EqlNASReplPartnerInfoMapClusterName_Type()
)
eqlNASReplPartnerInfoMapClusterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapClusterName.setStatus("current")
_EqlNASReplPartnerInfoMapClusterSanVIPType_Type = InetAddressType
_EqlNASReplPartnerInfoMapClusterSanVIPType_Object = MibTableColumn
eqlNASReplPartnerInfoMapClusterSanVIPType = _EqlNASReplPartnerInfoMapClusterSanVIPType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 3),
    _EqlNASReplPartnerInfoMapClusterSanVIPType_Type()
)
eqlNASReplPartnerInfoMapClusterSanVIPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapClusterSanVIPType.setStatus("current")
_EqlNASReplPartnerInfoMapClusterSanVIP_Type = InetAddress
_EqlNASReplPartnerInfoMapClusterSanVIP_Object = MibTableColumn
eqlNASReplPartnerInfoMapClusterSanVIP = _EqlNASReplPartnerInfoMapClusterSanVIP_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 4),
    _EqlNASReplPartnerInfoMapClusterSanVIP_Type()
)
eqlNASReplPartnerInfoMapClusterSanVIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapClusterSanVIP.setStatus("current")
_EqlNASReplPartnerInfoMapClusterId_Type = ClusterIdType
_EqlNASReplPartnerInfoMapClusterId_Object = MibTableColumn
eqlNASReplPartnerInfoMapClusterId = _EqlNASReplPartnerInfoMapClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 5),
    _EqlNASReplPartnerInfoMapClusterId_Type()
)
eqlNASReplPartnerInfoMapClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapClusterId.setStatus("current")
_EqlNASReplPartnerInfoMapClusterMPV_Type = Unsigned32
_EqlNASReplPartnerInfoMapClusterMPV_Object = MibTableColumn
eqlNASReplPartnerInfoMapClusterMPV = _EqlNASReplPartnerInfoMapClusterMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 6),
    _EqlNASReplPartnerInfoMapClusterMPV_Type()
)
eqlNASReplPartnerInfoMapClusterMPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapClusterMPV.setStatus("current")
_EqlNASReplPartnerInfoMapNetworkAddrType_Type = InetAddressType
_EqlNASReplPartnerInfoMapNetworkAddrType_Object = MibTableColumn
eqlNASReplPartnerInfoMapNetworkAddrType = _EqlNASReplPartnerInfoMapNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 7),
    _EqlNASReplPartnerInfoMapNetworkAddrType_Type()
)
eqlNASReplPartnerInfoMapNetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapNetworkAddrType.setStatus("current")
_EqlNASReplPartnerInfoMapNetworkAddr_Type = InetAddress
_EqlNASReplPartnerInfoMapNetworkAddr_Object = MibTableColumn
eqlNASReplPartnerInfoMapNetworkAddr = _EqlNASReplPartnerInfoMapNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 8),
    _EqlNASReplPartnerInfoMapNetworkAddr_Type()
)
eqlNASReplPartnerInfoMapNetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapNetworkAddr.setStatus("current")
_EqlNASReplPartnerInfoMapNetworkMask_Type = InetAddress
_EqlNASReplPartnerInfoMapNetworkMask_Object = MibTableColumn
eqlNASReplPartnerInfoMapNetworkMask = _EqlNASReplPartnerInfoMapNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 12, 1, 9),
    _EqlNASReplPartnerInfoMapNetworkMask_Type()
)
eqlNASReplPartnerInfoMapNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerInfoMapNetworkMask.setStatus("current")
_EqlNASReplPartnerIdMapTable_Object = MibTable
eqlNASReplPartnerIdMapTable = _EqlNASReplPartnerIdMapTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 13)
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerIdMapTable.setStatus("current")
_EqlNASReplPartnerIdMapEntry_Object = MibTableRow
eqlNASReplPartnerIdMapEntry = _EqlNASReplPartnerIdMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 13, 1)
)
eqlNASReplPartnerIdMapEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplPartnerInfoMapClusterName"),
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerIdMapEntry.setStatus("current")
_EqlNASReplPartnerIdMapRowStatus_Type = RowStatus
_EqlNASReplPartnerIdMapRowStatus_Object = MibTableColumn
eqlNASReplPartnerIdMapRowStatus = _EqlNASReplPartnerIdMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 13, 1, 1),
    _EqlNASReplPartnerIdMapRowStatus_Type()
)
eqlNASReplPartnerIdMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerIdMapRowStatus.setStatus("current")
_EqlNASReplPartnerIdMapPartnershipId_Type = Unsigned32
_EqlNASReplPartnerIdMapPartnershipId_Object = MibTableColumn
eqlNASReplPartnerIdMapPartnershipId = _EqlNASReplPartnerIdMapPartnershipId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 13, 1, 2),
    _EqlNASReplPartnerIdMapPartnershipId_Type()
)
eqlNASReplPartnerIdMapPartnershipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplPartnerIdMapPartnershipId.setStatus("current")
_EqlNASContainerCfgTable_Object = MibTable
eqlNASContainerCfgTable = _EqlNASContainerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14)
)
if mibBuilder.loadTexts:
    eqlNASContainerCfgTable.setStatus("current")
_EqlNASContainerCfgEntry_Object = MibTableRow
eqlNASContainerCfgEntry = _EqlNASContainerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14, 1)
)
eqlNASContainerCfgEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerCfgIndex"),
)
if mibBuilder.loadTexts:
    eqlNASContainerCfgEntry.setStatus("current")
_EqlNASContainerCfgIndex_Type = Unsigned32
_EqlNASContainerCfgIndex_Object = MibTableColumn
eqlNASContainerCfgIndex = _EqlNASContainerCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14, 1, 1),
    _EqlNASContainerCfgIndex_Type()
)
eqlNASContainerCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASContainerCfgIndex.setStatus("current")
_EqlNASContainerCfgRowStatus_Type = RowStatus
_EqlNASContainerCfgRowStatus_Object = MibTableColumn
eqlNASContainerCfgRowStatus = _EqlNASContainerCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14, 1, 2),
    _EqlNASContainerCfgRowStatus_Type()
)
eqlNASContainerCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASContainerCfgRowStatus.setStatus("current")


class _EqlNASContainerCfgSourceClusterName_Type(OctetString):
    """Custom type eqlNASContainerCfgSourceClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASContainerCfgSourceClusterName_Type.__name__ = "OctetString"
_EqlNASContainerCfgSourceClusterName_Object = MibTableColumn
eqlNASContainerCfgSourceClusterName = _EqlNASContainerCfgSourceClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14, 1, 3),
    _EqlNASContainerCfgSourceClusterName_Type()
)
eqlNASContainerCfgSourceClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASContainerCfgSourceClusterName.setStatus("current")


class _EqlNASContainerCfgSourceFSName_Type(OctetString):
    """Custom type eqlNASContainerCfgSourceFSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASContainerCfgSourceFSName_Type.__name__ = "OctetString"
_EqlNASContainerCfgSourceFSName_Object = MibTableColumn
eqlNASContainerCfgSourceFSName = _EqlNASContainerCfgSourceFSName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14, 1, 4),
    _EqlNASContainerCfgSourceFSName_Type()
)
eqlNASContainerCfgSourceFSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASContainerCfgSourceFSName.setStatus("current")


class _EqlNASContainerCfgModules_Type(Bits):
    """Custom type eqlNASContainerCfgModules based on Bits"""
    namedValues = NamedValues(
        *(("cifsShare", 1),
          ("nfsExport", 0),
          ("quotaRule", 2),
          ("snapshotScheduler", 3),
          ("volumeName", 5),
          ("volumeParameters", 4),
          ("volumeSize", 6))
    )

_EqlNASContainerCfgModules_Type.__name__ = "Bits"
_EqlNASContainerCfgModules_Object = MibTableColumn
eqlNASContainerCfgModules = _EqlNASContainerCfgModules_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14, 1, 5),
    _EqlNASContainerCfgModules_Type()
)
eqlNASContainerCfgModules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASContainerCfgModules.setStatus("current")
_EqlNASContainerCfgRequestId_Type = Counter64
_EqlNASContainerCfgRequestId_Object = MibTableColumn
eqlNASContainerCfgRequestId = _EqlNASContainerCfgRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 14, 1, 6),
    _EqlNASContainerCfgRequestId_Type()
)
eqlNASContainerCfgRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASContainerCfgRequestId.setStatus("current")
_EqlNASFSScanTable_Object = MibTable
eqlNASFSScanTable = _EqlNASFSScanTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 15)
)
if mibBuilder.loadTexts:
    eqlNASFSScanTable.setStatus("current")
_EqlNASFSScanEntry_Object = MibTableRow
eqlNASFSScanEntry = _EqlNASFSScanEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 15, 1)
)
eqlNASFSScanEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlNASFSScanEntry.setStatus("current")


class _EqlNASFSScanRate_Type(Integer32):
    """Custom type eqlNASFSScanRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 1),
          ("normal", 0),
          ("off", 2))
    )


_EqlNASFSScanRate_Type.__name__ = "Integer32"
_EqlNASFSScanRate_Object = MibTableColumn
eqlNASFSScanRate = _EqlNASFSScanRate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 15, 1, 1),
    _EqlNASFSScanRate_Type()
)
eqlNASFSScanRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASFSScanRate.setStatus("current")
_EqlNASReplicationHistoryTable_Object = MibTable
eqlNASReplicationHistoryTable = _EqlNASReplicationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16)
)
if mibBuilder.loadTexts:
    eqlNASReplicationHistoryTable.setStatus("current")
_EqlNASReplicationHistoryEntry_Object = MibTableRow
eqlNASReplicationHistoryEntry = _EqlNASReplicationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1)
)
eqlNASReplicationHistoryEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplSitePartnershipId"),
    (0, "EQLNAS-MIB", "eqlNASReplicationId"),
    (0, "EQLNAS-MIB", "eqlNASReplicationHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    eqlNASReplicationHistoryEntry.setStatus("current")
_EqlNASReplicationHistorySampleIndex_Type = Unsigned32
_EqlNASReplicationHistorySampleIndex_Object = MibTableColumn
eqlNASReplicationHistorySampleIndex = _EqlNASReplicationHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1, 1),
    _EqlNASReplicationHistorySampleIndex_Type()
)
eqlNASReplicationHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationHistorySampleIndex.setStatus("current")
_EqlNASReplicationHistoryStartTime_Type = Integer32
_EqlNASReplicationHistoryStartTime_Object = MibTableColumn
eqlNASReplicationHistoryStartTime = _EqlNASReplicationHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1, 2),
    _EqlNASReplicationHistoryStartTime_Type()
)
eqlNASReplicationHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationHistoryStartTime.setStatus("current")
_EqlNASReplicationHistoryEndTime_Type = Integer32
_EqlNASReplicationHistoryEndTime_Object = MibTableColumn
eqlNASReplicationHistoryEndTime = _EqlNASReplicationHistoryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1, 3),
    _EqlNASReplicationHistoryEndTime_Type()
)
eqlNASReplicationHistoryEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationHistoryEndTime.setStatus("current")
_EqlNASReplicationHistoryTransferredMb_Type = Unsigned32
_EqlNASReplicationHistoryTransferredMb_Object = MibTableColumn
eqlNASReplicationHistoryTransferredMb = _EqlNASReplicationHistoryTransferredMb_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1, 4),
    _EqlNASReplicationHistoryTransferredMb_Type()
)
eqlNASReplicationHistoryTransferredMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationHistoryTransferredMb.setStatus("current")
_EqlNASReplicationHistoryStatus_Type = EqlNASReplicationStatus
_EqlNASReplicationHistoryStatus_Object = MibTableColumn
eqlNASReplicationHistoryStatus = _EqlNASReplicationHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1, 5),
    _EqlNASReplicationHistoryStatus_Type()
)
eqlNASReplicationHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationHistoryStatus.setStatus("current")


class _EqlNASReplicationHistorySrcContainer_Type(OctetString):
    """Custom type eqlNASReplicationHistorySrcContainer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASReplicationHistorySrcContainer_Type.__name__ = "OctetString"
_EqlNASReplicationHistorySrcContainer_Object = MibTableColumn
eqlNASReplicationHistorySrcContainer = _EqlNASReplicationHistorySrcContainer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1, 6),
    _EqlNASReplicationHistorySrcContainer_Type()
)
eqlNASReplicationHistorySrcContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationHistorySrcContainer.setStatus("current")


class _EqlNASReplicationHistoryDestContainer_Type(OctetString):
    """Custom type eqlNASReplicationHistoryDestContainer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASReplicationHistoryDestContainer_Type.__name__ = "OctetString"
_EqlNASReplicationHistoryDestContainer_Object = MibTableColumn
eqlNASReplicationHistoryDestContainer = _EqlNASReplicationHistoryDestContainer_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 16, 1, 7),
    _EqlNASReplicationHistoryDestContainer_Type()
)
eqlNASReplicationHistoryDestContainer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplicationHistoryDestContainer.setStatus("current")
_EqlNASApplianceAntivirusHostTable_Object = MibTable
eqlNASApplianceAntivirusHostTable = _EqlNASApplianceAntivirusHostTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 17)
)
if mibBuilder.loadTexts:
    eqlNASApplianceAntivirusHostTable.setStatus("current")
_EqlNASApplianceAntivirusHostEntry_Object = MibTableRow
eqlNASApplianceAntivirusHostEntry = _EqlNASApplianceAntivirusHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 17, 1)
)
eqlNASApplianceAntivirusHostEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASApplianceAntivirusHostIndex"),
)
if mibBuilder.loadTexts:
    eqlNASApplianceAntivirusHostEntry.setStatus("current")
_EqlNASApplianceAntivirusHostIndex_Type = Unsigned32
_EqlNASApplianceAntivirusHostIndex_Object = MibTableColumn
eqlNASApplianceAntivirusHostIndex = _EqlNASApplianceAntivirusHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 17, 1, 1),
    _EqlNASApplianceAntivirusHostIndex_Type()
)
eqlNASApplianceAntivirusHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASApplianceAntivirusHostIndex.setStatus("current")
_EqlNASApplianceAntivirusHostRowStatus_Type = RowStatus
_EqlNASApplianceAntivirusHostRowStatus_Object = MibTableColumn
eqlNASApplianceAntivirusHostRowStatus = _EqlNASApplianceAntivirusHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 17, 1, 2),
    _EqlNASApplianceAntivirusHostRowStatus_Type()
)
eqlNASApplianceAntivirusHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceAntivirusHostRowStatus.setStatus("current")


class _EqlNASApplianceAntivirusHostName_Type(OctetString):
    """Custom type eqlNASApplianceAntivirusHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlNASApplianceAntivirusHostName_Type.__name__ = "OctetString"
_EqlNASApplianceAntivirusHostName_Object = MibTableColumn
eqlNASApplianceAntivirusHostName = _EqlNASApplianceAntivirusHostName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 17, 1, 3),
    _EqlNASApplianceAntivirusHostName_Type()
)
eqlNASApplianceAntivirusHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceAntivirusHostName.setStatus("current")


class _EqlNASApplianceAntivirusHostPortNumber_Type(Unsigned32):
    """Custom type eqlNASApplianceAntivirusHostPortNumber based on Unsigned32"""
    defaultValue = 1344

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EqlNASApplianceAntivirusHostPortNumber_Type.__name__ = "Unsigned32"
_EqlNASApplianceAntivirusHostPortNumber_Object = MibTableColumn
eqlNASApplianceAntivirusHostPortNumber = _EqlNASApplianceAntivirusHostPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 17, 1, 4),
    _EqlNASApplianceAntivirusHostPortNumber_Type()
)
eqlNASApplianceAntivirusHostPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceAntivirusHostPortNumber.setStatus("current")


class _EqlNASApplianceAntivirusHostTransactionState_Type(Integer32):
    """Custom type eqlNASApplianceAntivirusHostTransactionState based on Integer32"""
    defaultValue = 0

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
        *(("configCommit", 2),
          ("configInProgress", 1),
          ("configStart", 0),
          ("configStartCommit", 3))
    )


_EqlNASApplianceAntivirusHostTransactionState_Type.__name__ = "Integer32"
_EqlNASApplianceAntivirusHostTransactionState_Object = MibTableColumn
eqlNASApplianceAntivirusHostTransactionState = _EqlNASApplianceAntivirusHostTransactionState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 17, 1, 5),
    _EqlNASApplianceAntivirusHostTransactionState_Type()
)
eqlNASApplianceAntivirusHostTransactionState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASApplianceAntivirusHostTransactionState.setStatus("current")
_EqlNASChassisTable_Object = MibTable
eqlNASChassisTable = _EqlNASChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18)
)
if mibBuilder.loadTexts:
    eqlNASChassisTable.setStatus("current")
_EqlNASChassisEntry_Object = MibTableRow
eqlNASChassisEntry = _EqlNASChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18, 1)
)
eqlNASChassisEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisIndex"),
)
if mibBuilder.loadTexts:
    eqlNASChassisEntry.setStatus("current")
_EqlNASChassisIndex_Type = Unsigned32
_EqlNASChassisIndex_Object = MibTableColumn
eqlNASChassisIndex = _EqlNASChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18, 1, 1),
    _EqlNASChassisIndex_Type()
)
eqlNASChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASChassisIndex.setStatus("current")
_EqlNASChassisRowStatus_Type = RowStatus
_EqlNASChassisRowStatus_Object = MibTableColumn
eqlNASChassisRowStatus = _EqlNASChassisRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18, 1, 2),
    _EqlNASChassisRowStatus_Type()
)
eqlNASChassisRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASChassisRowStatus.setStatus("current")


class _EqlNASChassisName_Type(OctetString):
    """Custom type eqlNASChassisName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlNASChassisName_Type.__name__ = "OctetString"
_EqlNASChassisName_Object = MibTableColumn
eqlNASChassisName = _EqlNASChassisName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18, 1, 3),
    _EqlNASChassisName_Type()
)
eqlNASChassisName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASChassisName.setStatus("current")
_EqlNASChassisRequestId_Type = Counter64
_EqlNASChassisRequestId_Object = MibTableColumn
eqlNASChassisRequestId = _EqlNASChassisRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18, 1, 4),
    _EqlNASChassisRequestId_Type()
)
eqlNASChassisRequestId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisRequestId.setStatus("current")
_EqlNASChassisFileSystemMember_Type = TruthValue
_EqlNASChassisFileSystemMember_Object = MibTableColumn
eqlNASChassisFileSystemMember = _EqlNASChassisFileSystemMember_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18, 1, 5),
    _EqlNASChassisFileSystemMember_Type()
)
eqlNASChassisFileSystemMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisFileSystemMember.setStatus("current")


class _EqlNASChassisModelName_Type(OctetString):
    """Custom type eqlNASChassisModelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlNASChassisModelName_Type.__name__ = "OctetString"
_EqlNASChassisModelName_Object = MibTableColumn
eqlNASChassisModelName = _EqlNASChassisModelName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 18, 1, 6),
    _EqlNASChassisModelName_Type()
)
eqlNASChassisModelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASChassisModelName.setStatus("current")
_EqlNASChassisStatusTable_Object = MibTable
eqlNASChassisStatusTable = _EqlNASChassisStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19)
)
if mibBuilder.loadTexts:
    eqlNASChassisStatusTable.setStatus("current")
_EqlNASChassisStatusEntry_Object = MibTableRow
eqlNASChassisStatusEntry = _EqlNASChassisStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1)
)
eqlNASChassisStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisIndex"),
)
if mibBuilder.loadTexts:
    eqlNASChassisStatusEntry.setStatus("current")
_EqlNASChassisOverallStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisOverallStatus_Object = MibTableColumn
eqlNASChassisOverallStatus = _EqlNASChassisOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 1),
    _EqlNASChassisOverallStatus_Type()
)
eqlNASChassisOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisOverallStatus.setStatus("current")


class _EqlNASChassisChassisTag_Type(OctetString):
    """Custom type eqlNASChassisChassisTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_EqlNASChassisChassisTag_Type.__name__ = "OctetString"
_EqlNASChassisChassisTag_Object = MibTableColumn
eqlNASChassisChassisTag = _EqlNASChassisChassisTag_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 2),
    _EqlNASChassisChassisTag_Type()
)
eqlNASChassisChassisTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisChassisTag.setStatus("current")


class _EqlNASChassisModel_Type(OctetString):
    """Custom type eqlNASChassisModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisModel_Type.__name__ = "OctetString"
_EqlNASChassisModel_Object = MibTableColumn
eqlNASChassisModel = _EqlNASChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 3),
    _EqlNASChassisModel_Type()
)
eqlNASChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisModel.setStatus("current")
_EqlNASChassisSanType_Type = EqlNASChassisSanType
_EqlNASChassisSanType_Object = MibTableColumn
eqlNASChassisSanType = _EqlNASChassisSanType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 4),
    _EqlNASChassisSanType_Type()
)
eqlNASChassisSanType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisSanType.setStatus("current")
_EqlNASChassisOverallControllerStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisOverallControllerStatus_Object = MibTableColumn
eqlNASChassisOverallControllerStatus = _EqlNASChassisOverallControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 5),
    _EqlNASChassisOverallControllerStatus_Type()
)
eqlNASChassisOverallControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisOverallControllerStatus.setStatus("current")
_EqlNASChassisClientNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisClientNetworkSpeed_Object = MibTableColumn
eqlNASChassisClientNetworkSpeed = _EqlNASChassisClientNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 6),
    _EqlNASChassisClientNetworkSpeed_Type()
)
eqlNASChassisClientNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisClientNetworkSpeed.setStatus("current")
_EqlNASChassisBackplaneNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisBackplaneNetworkSpeed_Object = MibTableColumn
eqlNASChassisBackplaneNetworkSpeed = _EqlNASChassisBackplaneNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 7),
    _EqlNASChassisBackplaneNetworkSpeed_Type()
)
eqlNASChassisBackplaneNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisBackplaneNetworkSpeed.setStatus("current")
_EqlNASChassisInternalNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisInternalNetworkSpeed_Object = MibTableColumn
eqlNASChassisInternalNetworkSpeed = _EqlNASChassisInternalNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 8),
    _EqlNASChassisInternalNetworkSpeed_Type()
)
eqlNASChassisInternalNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisInternalNetworkSpeed.setStatus("current")
_EqlNASChassisSanNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisSanNetworkSpeed_Object = MibTableColumn
eqlNASChassisSanNetworkSpeed = _EqlNASChassisSanNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 9),
    _EqlNASChassisSanNetworkSpeed_Type()
)
eqlNASChassisSanNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisSanNetworkSpeed.setStatus("current")
_EqlNASChassisClientNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisClientNetworkStatus_Object = MibTableColumn
eqlNASChassisClientNetworkStatus = _EqlNASChassisClientNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 10),
    _EqlNASChassisClientNetworkStatus_Type()
)
eqlNASChassisClientNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisClientNetworkStatus.setStatus("current")
_EqlNASChassisBackplaneNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisBackplaneNetworkStatus_Object = MibTableColumn
eqlNASChassisBackplaneNetworkStatus = _EqlNASChassisBackplaneNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 11),
    _EqlNASChassisBackplaneNetworkStatus_Type()
)
eqlNASChassisBackplaneNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisBackplaneNetworkStatus.setStatus("current")
_EqlNASChassisInternalNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisInternalNetworkStatus_Object = MibTableColumn
eqlNASChassisInternalNetworkStatus = _EqlNASChassisInternalNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 12),
    _EqlNASChassisInternalNetworkStatus_Type()
)
eqlNASChassisInternalNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisInternalNetworkStatus.setStatus("current")
_EqlNASChassisSanNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisSanNetworkStatus_Object = MibTableColumn
eqlNASChassisSanNetworkStatus = _EqlNASChassisSanNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 13),
    _EqlNASChassisSanNetworkStatus_Type()
)
eqlNASChassisSanNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisSanNetworkStatus.setStatus("current")
_EqlNASChassisOverallFanStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisOverallFanStatus_Object = MibTableColumn
eqlNASChassisOverallFanStatus = _EqlNASChassisOverallFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 14),
    _EqlNASChassisOverallFanStatus_Type()
)
eqlNASChassisOverallFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisOverallFanStatus.setStatus("current")
_EqlNASChassisOverallPowerSupplyStatus_Type = EqlNASChassisACPowerStatus
_EqlNASChassisOverallPowerSupplyStatus_Object = MibTableColumn
eqlNASChassisOverallPowerSupplyStatus = _EqlNASChassisOverallPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 1, 15),
    _EqlNASChassisOverallPowerSupplyStatus_Type()
)
eqlNASChassisOverallPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisOverallPowerSupplyStatus.setStatus("current")
_EqlNASChassisFanStatusTable_Object = MibTable
eqlNASChassisFanStatusTable = _EqlNASChassisFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 2)
)
if mibBuilder.loadTexts:
    eqlNASChassisFanStatusTable.setStatus("current")
_EqlNASChassisFanStatusEntry_Object = MibTableRow
eqlNASChassisFanStatusEntry = _EqlNASChassisFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 2, 1)
)
eqlNASChassisFanStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisFanName"),
)
if mibBuilder.loadTexts:
    eqlNASChassisFanStatusEntry.setStatus("current")


class _EqlNASChassisFanName_Type(OctetString):
    """Custom type eqlNASChassisFanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisFanName_Type.__name__ = "OctetString"
_EqlNASChassisFanName_Object = MibTableColumn
eqlNASChassisFanName = _EqlNASChassisFanName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 2, 1, 1),
    _EqlNASChassisFanName_Type()
)
eqlNASChassisFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisFanName.setStatus("current")
_EqlNASChassisFanStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisFanStatus_Object = MibTableColumn
eqlNASChassisFanStatus = _EqlNASChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 2, 1, 2),
    _EqlNASChassisFanStatus_Type()
)
eqlNASChassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisFanStatus.setStatus("current")
_EqlNASChassisFanRpm_Type = Unsigned32
_EqlNASChassisFanRpm_Object = MibTableColumn
eqlNASChassisFanRpm = _EqlNASChassisFanRpm_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 2, 1, 3),
    _EqlNASChassisFanRpm_Type()
)
eqlNASChassisFanRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisFanRpm.setStatus("current")


class _EqlNASChassisFanRpmRange_Type(OctetString):
    """Custom type eqlNASChassisFanRpmRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_EqlNASChassisFanRpmRange_Type.__name__ = "OctetString"
_EqlNASChassisFanRpmRange_Object = MibTableColumn
eqlNASChassisFanRpmRange = _EqlNASChassisFanRpmRange_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 2, 1, 4),
    _EqlNASChassisFanRpmRange_Type()
)
eqlNASChassisFanRpmRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisFanRpmRange.setStatus("current")
_EqlNASChassisPowerSupplyStatusTable_Object = MibTable
eqlNASChassisPowerSupplyStatusTable = _EqlNASChassisPowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 3)
)
if mibBuilder.loadTexts:
    eqlNASChassisPowerSupplyStatusTable.setStatus("current")
_EqlNASChassisPowerSupplyStatusEntry_Object = MibTableRow
eqlNASChassisPowerSupplyStatusEntry = _EqlNASChassisPowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 3, 1)
)
eqlNASChassisPowerSupplyStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisPowerSupplyName"),
)
if mibBuilder.loadTexts:
    eqlNASChassisPowerSupplyStatusEntry.setStatus("current")


class _EqlNASChassisPowerSupplyName_Type(OctetString):
    """Custom type eqlNASChassisPowerSupplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisPowerSupplyName_Type.__name__ = "OctetString"
_EqlNASChassisPowerSupplyName_Object = MibTableColumn
eqlNASChassisPowerSupplyName = _EqlNASChassisPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 3, 1, 1),
    _EqlNASChassisPowerSupplyName_Type()
)
eqlNASChassisPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisPowerSupplyName.setStatus("current")
_EqlNASChassisPowerSupplyStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisPowerSupplyStatus_Object = MibTableColumn
eqlNASChassisPowerSupplyStatus = _EqlNASChassisPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 19, 3, 1, 2),
    _EqlNASChassisPowerSupplyStatus_Type()
)
eqlNASChassisPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisPowerSupplyStatus.setStatus("current")
_EqlNASChassisControllerStatusTable_Object = MibTable
eqlNASChassisControllerStatusTable = _EqlNASChassisControllerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20)
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerStatusTable.setStatus("current")
_EqlNASChassisControllerStatusEntry_Object = MibTableRow
eqlNASChassisControllerStatusEntry = _EqlNASChassisControllerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1)
)
eqlNASChassisControllerStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerIndex"),
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerStatusEntry.setStatus("current")
_EqlNASChassisControllerIndex_Type = Unsigned32
_EqlNASChassisControllerIndex_Object = MibTableColumn
eqlNASChassisControllerIndex = _EqlNASChassisControllerIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 1),
    _EqlNASChassisControllerIndex_Type()
)
eqlNASChassisControllerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerIndex.setStatus("current")
_EqlNASChassisControllerStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerStatus_Object = MibTableColumn
eqlNASChassisControllerStatus = _EqlNASChassisControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 2),
    _EqlNASChassisControllerStatus_Type()
)
eqlNASChassisControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerStatus.setStatus("current")
_EqlNASChassisControllerState_Type = EqlNASChassisControllerState
_EqlNASChassisControllerState_Object = MibTableColumn
eqlNASChassisControllerState = _EqlNASChassisControllerState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 3),
    _EqlNASChassisControllerState_Type()
)
eqlNASChassisControllerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerState.setStatus("current")
_EqlNASChassisControllerLocation_Type = EqlNASChassisControllerLocation
_EqlNASChassisControllerLocation_Object = MibTableColumn
eqlNASChassisControllerLocation = _EqlNASChassisControllerLocation_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 4),
    _EqlNASChassisControllerLocation_Type()
)
eqlNASChassisControllerLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerLocation.setStatus("current")
_EqlNASChassisControllerAmbientTemperatureStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerAmbientTemperatureStatus_Object = MibTableColumn
eqlNASChassisControllerAmbientTemperatureStatus = _EqlNASChassisControllerAmbientTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 5),
    _EqlNASChassisControllerAmbientTemperatureStatus_Type()
)
eqlNASChassisControllerAmbientTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerAmbientTemperatureStatus.setStatus("current")
_EqlNASChassisControllerAmbientTemperatureValue_Type = Integer32
_EqlNASChassisControllerAmbientTemperatureValue_Object = MibTableColumn
eqlNASChassisControllerAmbientTemperatureValue = _EqlNASChassisControllerAmbientTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 6),
    _EqlNASChassisControllerAmbientTemperatureValue_Type()
)
eqlNASChassisControllerAmbientTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerAmbientTemperatureValue.setStatus("current")


class _EqlNASChassisControllerSystemControllerId_Type(OctetString):
    """Custom type eqlNASChassisControllerSystemControllerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisControllerSystemControllerId_Type.__name__ = "OctetString"
_EqlNASChassisControllerSystemControllerId_Object = MibTableColumn
eqlNASChassisControllerSystemControllerId = _EqlNASChassisControllerSystemControllerId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 7),
    _EqlNASChassisControllerSystemControllerId_Type()
)
eqlNASChassisControllerSystemControllerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerSystemControllerId.setStatus("current")
_EqlNASChassisControllerBPSStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerBPSStatus_Object = MibTableColumn
eqlNASChassisControllerBPSStatus = _EqlNASChassisControllerBPSStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 8),
    _EqlNASChassisControllerBPSStatus_Type()
)
eqlNASChassisControllerBPSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerBPSStatus.setStatus("current")
_EqlNASChassisControllerBPSIsAccessible_Type = TruthValue
_EqlNASChassisControllerBPSIsAccessible_Object = MibTableColumn
eqlNASChassisControllerBPSIsAccessible = _EqlNASChassisControllerBPSIsAccessible_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 9),
    _EqlNASChassisControllerBPSIsAccessible_Type()
)
eqlNASChassisControllerBPSIsAccessible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerBPSIsAccessible.setStatus("current")


class _EqlNASChassisControllerBPSModel_Type(OctetString):
    """Custom type eqlNASChassisControllerBPSModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisControllerBPSModel_Type.__name__ = "OctetString"
_EqlNASChassisControllerBPSModel_Object = MibTableColumn
eqlNASChassisControllerBPSModel = _EqlNASChassisControllerBPSModel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 10),
    _EqlNASChassisControllerBPSModel_Type()
)
eqlNASChassisControllerBPSModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerBPSModel.setStatus("current")
_EqlNASChassisControllerBPSCharge_Type = Unsigned32
_EqlNASChassisControllerBPSCharge_Object = MibTableColumn
eqlNASChassisControllerBPSCharge = _EqlNASChassisControllerBPSCharge_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 11),
    _EqlNASChassisControllerBPSCharge_Type()
)
eqlNASChassisControllerBPSCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerBPSCharge.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASChassisControllerBPSCharge.setUnits("%")
_EqlNASChassisControllerCPUOverallStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerCPUOverallStatus_Object = MibTableColumn
eqlNASChassisControllerCPUOverallStatus = _EqlNASChassisControllerCPUOverallStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 12),
    _EqlNASChassisControllerCPUOverallStatus_Type()
)
eqlNASChassisControllerCPUOverallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerCPUOverallStatus.setStatus("current")
_EqlNASChassisControllerCPUCurrentCoresCount_Type = Unsigned32
_EqlNASChassisControllerCPUCurrentCoresCount_Object = MibTableColumn
eqlNASChassisControllerCPUCurrentCoresCount = _EqlNASChassisControllerCPUCurrentCoresCount_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 13),
    _EqlNASChassisControllerCPUCurrentCoresCount_Type()
)
eqlNASChassisControllerCPUCurrentCoresCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerCPUCurrentCoresCount.setStatus("current")
_EqlNASChassisControllerOverallFanStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerOverallFanStatus_Object = MibTableColumn
eqlNASChassisControllerOverallFanStatus = _EqlNASChassisControllerOverallFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 14),
    _EqlNASChassisControllerOverallFanStatus_Type()
)
eqlNASChassisControllerOverallFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerOverallFanStatus.setStatus("current")
_EqlNASChassisControllerOverallLocalDiskStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerOverallLocalDiskStatus_Object = MibTableColumn
eqlNASChassisControllerOverallLocalDiskStatus = _EqlNASChassisControllerOverallLocalDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 15),
    _EqlNASChassisControllerOverallLocalDiskStatus_Type()
)
eqlNASChassisControllerOverallLocalDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerOverallLocalDiskStatus.setStatus("current")
_EqlNASChassisControllerOverallRaidControllerStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerOverallRaidControllerStatus_Object = MibTableColumn
eqlNASChassisControllerOverallRaidControllerStatus = _EqlNASChassisControllerOverallRaidControllerStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 16),
    _EqlNASChassisControllerOverallRaidControllerStatus_Type()
)
eqlNASChassisControllerOverallRaidControllerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerOverallRaidControllerStatus.setStatus("current")
_EqlNASChassisControllerOverallVirtualDiskStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerOverallVirtualDiskStatus_Object = MibTableColumn
eqlNASChassisControllerOverallVirtualDiskStatus = _EqlNASChassisControllerOverallVirtualDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 17),
    _EqlNASChassisControllerOverallVirtualDiskStatus_Type()
)
eqlNASChassisControllerOverallVirtualDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerOverallVirtualDiskStatus.setStatus("current")
_EqlNASChassisControllerMemoryStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerMemoryStatus_Object = MibTableColumn
eqlNASChassisControllerMemoryStatus = _EqlNASChassisControllerMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 18),
    _EqlNASChassisControllerMemoryStatus_Type()
)
eqlNASChassisControllerMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerMemoryStatus.setStatus("current")
_EqlNASChassisControllerMemorySize_Type = Unsigned32
_EqlNASChassisControllerMemorySize_Object = MibTableColumn
eqlNASChassisControllerMemorySize = _EqlNASChassisControllerMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 19),
    _EqlNASChassisControllerMemorySize_Type()
)
eqlNASChassisControllerMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerMemorySize.setStatus("current")
_EqlNASChassisControllerBackplaneNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerBackplaneNetworkStatus_Object = MibTableColumn
eqlNASChassisControllerBackplaneNetworkStatus = _EqlNASChassisControllerBackplaneNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 20),
    _EqlNASChassisControllerBackplaneNetworkStatus_Type()
)
eqlNASChassisControllerBackplaneNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerBackplaneNetworkStatus.setStatus("current")
_EqlNASChassisControllerBackplaneNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisControllerBackplaneNetworkSpeed_Object = MibTableColumn
eqlNASChassisControllerBackplaneNetworkSpeed = _EqlNASChassisControllerBackplaneNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 21),
    _EqlNASChassisControllerBackplaneNetworkSpeed_Type()
)
eqlNASChassisControllerBackplaneNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerBackplaneNetworkSpeed.setStatus("current")
_EqlNASChassisControllerClientNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerClientNetworkStatus_Object = MibTableColumn
eqlNASChassisControllerClientNetworkStatus = _EqlNASChassisControllerClientNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 22),
    _EqlNASChassisControllerClientNetworkStatus_Type()
)
eqlNASChassisControllerClientNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerClientNetworkStatus.setStatus("current")
_EqlNASChassisControllerClientNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisControllerClientNetworkSpeed_Object = MibTableColumn
eqlNASChassisControllerClientNetworkSpeed = _EqlNASChassisControllerClientNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 23),
    _EqlNASChassisControllerClientNetworkSpeed_Type()
)
eqlNASChassisControllerClientNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerClientNetworkSpeed.setStatus("current")
_EqlNASChassisControllerInternalNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerInternalNetworkStatus_Object = MibTableColumn
eqlNASChassisControllerInternalNetworkStatus = _EqlNASChassisControllerInternalNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 24),
    _EqlNASChassisControllerInternalNetworkStatus_Type()
)
eqlNASChassisControllerInternalNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerInternalNetworkStatus.setStatus("current")
_EqlNASChassisControllerInternalNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisControllerInternalNetworkSpeed_Object = MibTableColumn
eqlNASChassisControllerInternalNetworkSpeed = _EqlNASChassisControllerInternalNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 25),
    _EqlNASChassisControllerInternalNetworkSpeed_Type()
)
eqlNASChassisControllerInternalNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerInternalNetworkSpeed.setStatus("current")
_EqlNASChassisControllerSanNetworkStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerSanNetworkStatus_Object = MibTableColumn
eqlNASChassisControllerSanNetworkStatus = _EqlNASChassisControllerSanNetworkStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 26),
    _EqlNASChassisControllerSanNetworkStatus_Type()
)
eqlNASChassisControllerSanNetworkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerSanNetworkStatus.setStatus("current")
_EqlNASChassisControllerSanNetworkSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisControllerSanNetworkSpeed_Object = MibTableColumn
eqlNASChassisControllerSanNetworkSpeed = _EqlNASChassisControllerSanNetworkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 27),
    _EqlNASChassisControllerSanNetworkSpeed_Type()
)
eqlNASChassisControllerSanNetworkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerSanNetworkSpeed.setStatus("current")
_EqlNASChassisControllerOverallPowerSupplyStatus_Type = EqlNASChassisACPowerStatus
_EqlNASChassisControllerOverallPowerSupplyStatus_Object = MibTableColumn
eqlNASChassisControllerOverallPowerSupplyStatus = _EqlNASChassisControllerOverallPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 1, 28),
    _EqlNASChassisControllerOverallPowerSupplyStatus_Type()
)
eqlNASChassisControllerOverallPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerOverallPowerSupplyStatus.setStatus("current")
_EqlNASChassisControllerFanStatusTable_Object = MibTable
eqlNASChassisControllerFanStatusTable = _EqlNASChassisControllerFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 2)
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerFanStatusTable.setStatus("current")
_EqlNASChassisControllerFanStatusEntry_Object = MibTableRow
eqlNASChassisControllerFanStatusEntry = _EqlNASChassisControllerFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 2, 1)
)
eqlNASChassisControllerFanStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerFanName"),
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerFanStatusEntry.setStatus("current")


class _EqlNASChassisControllerFanName_Type(OctetString):
    """Custom type eqlNASChassisControllerFanName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisControllerFanName_Type.__name__ = "OctetString"
_EqlNASChassisControllerFanName_Object = MibTableColumn
eqlNASChassisControllerFanName = _EqlNASChassisControllerFanName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 2, 1, 1),
    _EqlNASChassisControllerFanName_Type()
)
eqlNASChassisControllerFanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerFanName.setStatus("current")
_EqlNASChassisControllerFanStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerFanStatus_Object = MibTableColumn
eqlNASChassisControllerFanStatus = _EqlNASChassisControllerFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 2, 1, 2),
    _EqlNASChassisControllerFanStatus_Type()
)
eqlNASChassisControllerFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerFanStatus.setStatus("current")
_EqlNASChassisControllerFanRpm_Type = Unsigned32
_EqlNASChassisControllerFanRpm_Object = MibTableColumn
eqlNASChassisControllerFanRpm = _EqlNASChassisControllerFanRpm_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 2, 1, 3),
    _EqlNASChassisControllerFanRpm_Type()
)
eqlNASChassisControllerFanRpm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerFanRpm.setStatus("current")


class _EqlNASChassisControllerFanRpmRange_Type(OctetString):
    """Custom type eqlNASChassisControllerFanRpmRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_EqlNASChassisControllerFanRpmRange_Type.__name__ = "OctetString"
_EqlNASChassisControllerFanRpmRange_Object = MibTableColumn
eqlNASChassisControllerFanRpmRange = _EqlNASChassisControllerFanRpmRange_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 2, 1, 4),
    _EqlNASChassisControllerFanRpmRange_Type()
)
eqlNASChassisControllerFanRpmRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerFanRpmRange.setStatus("current")
_EqlNASChassisControllerPowerSupplyStatusTable_Object = MibTable
eqlNASChassisControllerPowerSupplyStatusTable = _EqlNASChassisControllerPowerSupplyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 3)
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerPowerSupplyStatusTable.setStatus("current")
_EqlNASChassisControllerPowerSupplyStatusEntry_Object = MibTableRow
eqlNASChassisControllerPowerSupplyStatusEntry = _EqlNASChassisControllerPowerSupplyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 3, 1)
)
eqlNASChassisControllerPowerSupplyStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerPowerSupplyName"),
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerPowerSupplyStatusEntry.setStatus("current")


class _EqlNASChassisControllerPowerSupplyName_Type(OctetString):
    """Custom type eqlNASChassisControllerPowerSupplyName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisControllerPowerSupplyName_Type.__name__ = "OctetString"
_EqlNASChassisControllerPowerSupplyName_Object = MibTableColumn
eqlNASChassisControllerPowerSupplyName = _EqlNASChassisControllerPowerSupplyName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 3, 1, 1),
    _EqlNASChassisControllerPowerSupplyName_Type()
)
eqlNASChassisControllerPowerSupplyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerPowerSupplyName.setStatus("current")
_EqlNASChassisControllerPowerSupplyStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerPowerSupplyStatus_Object = MibTableColumn
eqlNASChassisControllerPowerSupplyStatus = _EqlNASChassisControllerPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 3, 1, 2),
    _EqlNASChassisControllerPowerSupplyStatus_Type()
)
eqlNASChassisControllerPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerPowerSupplyStatus.setStatus("current")
_EqlNASChassisControllerDiskStatusTable_Object = MibTable
eqlNASChassisControllerDiskStatusTable = _EqlNASChassisControllerDiskStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 4)
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerDiskStatusTable.setStatus("current")
_EqlNASChassisControllerDiskStatusEntry_Object = MibTableRow
eqlNASChassisControllerDiskStatusEntry = _EqlNASChassisControllerDiskStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 4, 1)
)
eqlNASChassisControllerDiskStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerDiskName"),
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerDiskStatusEntry.setStatus("current")


class _EqlNASChassisControllerDiskName_Type(OctetString):
    """Custom type eqlNASChassisControllerDiskName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisControllerDiskName_Type.__name__ = "OctetString"
_EqlNASChassisControllerDiskName_Object = MibTableColumn
eqlNASChassisControllerDiskName = _EqlNASChassisControllerDiskName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 4, 1, 1),
    _EqlNASChassisControllerDiskName_Type()
)
eqlNASChassisControllerDiskName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerDiskName.setStatus("current")
_EqlNASChassisControllerDiskStatus_Type = EqlNASChassisComponentStatus
_EqlNASChassisControllerDiskStatus_Object = MibTableColumn
eqlNASChassisControllerDiskStatus = _EqlNASChassisControllerDiskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 4, 1, 2),
    _EqlNASChassisControllerDiskStatus_Type()
)
eqlNASChassisControllerDiskStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerDiskStatus.setStatus("current")
_EqlNASChassisControllerNicStatusTable_Object = MibTable
eqlNASChassisControllerNicStatusTable = _EqlNASChassisControllerNicStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5)
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicStatusTable.setStatus("current")
_EqlNASChassisControllerNicStatusEntry_Object = MibTableRow
eqlNASChassisControllerNicStatusEntry = _EqlNASChassisControllerNicStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1)
)
eqlNASChassisControllerNicStatusEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkType"),
    (0, "EQLNAS-MIB", "eqlNASChassisControllerNicName"),
)
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicStatusEntry.setStatus("current")


class _EqlNASChassisControllerNicName_Type(OctetString):
    """Custom type eqlNASChassisControllerNicName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASChassisControllerNicName_Type.__name__ = "OctetString"
_EqlNASChassisControllerNicName_Object = MibTableColumn
eqlNASChassisControllerNicName = _EqlNASChassisControllerNicName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1, 1),
    _EqlNASChassisControllerNicName_Type()
)
eqlNASChassisControllerNicName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicName.setStatus("current")


class _EqlNASChassisControllerNicState_Type(Integer32):
    """Custom type eqlNASChassisControllerNicState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-available", 2),
          ("off", 1),
          ("on", 0))
    )


_EqlNASChassisControllerNicState_Type.__name__ = "Integer32"
_EqlNASChassisControllerNicState_Object = MibTableColumn
eqlNASChassisControllerNicState = _EqlNASChassisControllerNicState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1, 2),
    _EqlNASChassisControllerNicState_Type()
)
eqlNASChassisControllerNicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicState.setStatus("current")
_EqlNASChassisControllerNicSpeed_Type = EqlNASChassisNetworkSpeed
_EqlNASChassisControllerNicSpeed_Object = MibTableColumn
eqlNASChassisControllerNicSpeed = _EqlNASChassisControllerNicSpeed_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1, 3),
    _EqlNASChassisControllerNicSpeed_Type()
)
eqlNASChassisControllerNicSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicSpeed.setStatus("current")


class _EqlNASChassisControllerNicSlot_Type(OctetString):
    """Custom type eqlNASChassisControllerNicSlot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_EqlNASChassisControllerNicSlot_Type.__name__ = "OctetString"
_EqlNASChassisControllerNicSlot_Object = MibTableColumn
eqlNASChassisControllerNicSlot = _EqlNASChassisControllerNicSlot_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1, 4),
    _EqlNASChassisControllerNicSlot_Type()
)
eqlNASChassisControllerNicSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicSlot.setStatus("current")
_EqlNASChassisControllerNicPort_Type = Unsigned32
_EqlNASChassisControllerNicPort_Object = MibTableColumn
eqlNASChassisControllerNicPort = _EqlNASChassisControllerNicPort_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1, 5),
    _EqlNASChassisControllerNicPort_Type()
)
eqlNASChassisControllerNicPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicPort.setStatus("current")


class _EqlNASChassisControllerNicDuplex_Type(Integer32):
    """Custom type eqlNASChassisControllerNicDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 0),
          ("half", 1),
          ("unknown", 2))
    )


_EqlNASChassisControllerNicDuplex_Type.__name__ = "Integer32"
_EqlNASChassisControllerNicDuplex_Object = MibTableColumn
eqlNASChassisControllerNicDuplex = _EqlNASChassisControllerNicDuplex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1, 6),
    _EqlNASChassisControllerNicDuplex_Type()
)
eqlNASChassisControllerNicDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicDuplex.setStatus("current")


class _EqlNASChassisControllerNicFlowControl_Type(Integer32):
    """Custom type eqlNASChassisControllerNicFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 0),
          ("unknown", 2))
    )


_EqlNASChassisControllerNicFlowControl_Type.__name__ = "Integer32"
_EqlNASChassisControllerNicFlowControl_Object = MibTableColumn
eqlNASChassisControllerNicFlowControl = _EqlNASChassisControllerNicFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 20, 5, 1, 7),
    _EqlNASChassisControllerNicFlowControl_Type()
)
eqlNASChassisControllerNicFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASChassisControllerNicFlowControl.setStatus("current")
_EqlNASDiagsTable_Object = MibTable
eqlNASDiagsTable = _EqlNASDiagsTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 21)
)
if mibBuilder.loadTexts:
    eqlNASDiagsTable.setStatus("current")
_EqlNASDiagsEntry_Object = MibTableRow
eqlNASDiagsEntry = _EqlNASDiagsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 21, 1)
)
eqlNASDiagsEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlNASDiagsEntry.setStatus("current")


class _EqlNASDiagsStart_Type(Integer32):
    """Custom type eqlNASDiagsStart based on Integer32"""
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
        *(("clientconnectivity", 5),
          ("file", 2),
          ("fileaccessibility", 6),
          ("general", 1),
          ("logs", 8),
          ("network", 3),
          ("performance", 4),
          ("protocolslog", 7))
    )


_EqlNASDiagsStart_Type.__name__ = "Integer32"
_EqlNASDiagsStart_Object = MibTableColumn
eqlNASDiagsStart = _EqlNASDiagsStart_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 21, 1, 1),
    _EqlNASDiagsStart_Type()
)
eqlNASDiagsStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASDiagsStart.setStatus("current")


class _EqlNASDiagsCaseNumber_Type(OctetString):
    """Custom type eqlNASDiagsCaseNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_EqlNASDiagsCaseNumber_Type.__name__ = "OctetString"
_EqlNASDiagsCaseNumber_Object = MibTableColumn
eqlNASDiagsCaseNumber = _EqlNASDiagsCaseNumber_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 21, 1, 2),
    _EqlNASDiagsCaseNumber_Type()
)
eqlNASDiagsCaseNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASDiagsCaseNumber.setStatus("current")


class _EqlNASDiagsStatus_Type(Integer32):
    """Custom type eqlNASDiagsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("running", 2))
    )


_EqlNASDiagsStatus_Type.__name__ = "Integer32"
_EqlNASDiagsStatus_Object = MibTableColumn
eqlNASDiagsStatus = _EqlNASDiagsStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 21, 1, 3),
    _EqlNASDiagsStatus_Type()
)
eqlNASDiagsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASDiagsStatus.setStatus("current")
_EqlNASClientStaticRouteTable_Object = MibTable
eqlNASClientStaticRouteTable = _EqlNASClientStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22)
)
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteTable.setStatus("current")
_EqlNASClientStaticRouteEntry_Object = MibTableRow
eqlNASClientStaticRouteEntry = _EqlNASClientStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1)
)
eqlNASClientStaticRouteEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkID"),
    (0, "EQLNAS-MIB", "eqlNASClientStaticRouteNetworkAddrType"),
    (0, "EQLNAS-MIB", "eqlNASClientStaticRouteNetworkAddr"),
    (0, "EQLNAS-MIB", "eqlNASClientStaticRouteNetworkMaskType"),
    (0, "EQLNAS-MIB", "eqlNASClientStaticRouteNetworkMask"),
)
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteEntry.setStatus("current")
_EqlNASClientStaticRouteRowStatus_Type = RowStatus
_EqlNASClientStaticRouteRowStatus_Object = MibTableColumn
eqlNASClientStaticRouteRowStatus = _EqlNASClientStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1, 1),
    _EqlNASClientStaticRouteRowStatus_Type()
)
eqlNASClientStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteRowStatus.setStatus("current")
_EqlNASClientStaticRouteNetworkAddrType_Type = InetAddressType
_EqlNASClientStaticRouteNetworkAddrType_Object = MibTableColumn
eqlNASClientStaticRouteNetworkAddrType = _EqlNASClientStaticRouteNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1, 2),
    _EqlNASClientStaticRouteNetworkAddrType_Type()
)
eqlNASClientStaticRouteNetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteNetworkAddrType.setStatus("current")
_EqlNASClientStaticRouteNetworkAddr_Type = InetAddress
_EqlNASClientStaticRouteNetworkAddr_Object = MibTableColumn
eqlNASClientStaticRouteNetworkAddr = _EqlNASClientStaticRouteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1, 3),
    _EqlNASClientStaticRouteNetworkAddr_Type()
)
eqlNASClientStaticRouteNetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteNetworkAddr.setStatus("current")
_EqlNASClientStaticRouteNetworkMaskType_Type = InetAddressType
_EqlNASClientStaticRouteNetworkMaskType_Object = MibTableColumn
eqlNASClientStaticRouteNetworkMaskType = _EqlNASClientStaticRouteNetworkMaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1, 4),
    _EqlNASClientStaticRouteNetworkMaskType_Type()
)
eqlNASClientStaticRouteNetworkMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteNetworkMaskType.setStatus("current")
_EqlNASClientStaticRouteNetworkMask_Type = InetAddress
_EqlNASClientStaticRouteNetworkMask_Object = MibTableColumn
eqlNASClientStaticRouteNetworkMask = _EqlNASClientStaticRouteNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1, 5),
    _EqlNASClientStaticRouteNetworkMask_Type()
)
eqlNASClientStaticRouteNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteNetworkMask.setStatus("current")
_EqlNASClientStaticRouteGatewayAddrType_Type = InetAddressType
_EqlNASClientStaticRouteGatewayAddrType_Object = MibTableColumn
eqlNASClientStaticRouteGatewayAddrType = _EqlNASClientStaticRouteGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1, 6),
    _EqlNASClientStaticRouteGatewayAddrType_Type()
)
eqlNASClientStaticRouteGatewayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteGatewayAddrType.setStatus("current")
_EqlNASClientStaticRouteGatewayAddr_Type = InetAddress
_EqlNASClientStaticRouteGatewayAddr_Object = MibTableColumn
eqlNASClientStaticRouteGatewayAddr = _EqlNASClientStaticRouteGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 22, 1, 7),
    _EqlNASClientStaticRouteGatewayAddr_Type()
)
eqlNASClientStaticRouteGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClientStaticRouteGatewayAddr.setStatus("current")
_EqlNASClusterUpdateTable_Object = MibTable
eqlNASClusterUpdateTable = _EqlNASClusterUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23)
)
if mibBuilder.loadTexts:
    eqlNASClusterUpdateTable.setStatus("current")
_EqlNASClusterUpdateEntry_Object = MibTableRow
eqlNASClusterUpdateEntry = _EqlNASClusterUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23, 1)
)
eqlNASClusterUpdateEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlNASClusterUpdateEntry.setStatus("current")
_EqlNASClusterUpdateRowStatus_Type = RowStatus
_EqlNASClusterUpdateRowStatus_Object = MibTableColumn
eqlNASClusterUpdateRowStatus = _EqlNASClusterUpdateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23, 1, 1),
    _EqlNASClusterUpdateRowStatus_Type()
)
eqlNASClusterUpdateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClusterUpdateRowStatus.setStatus("current")


class _EqlNASClusterUpdateFilename_Type(OctetString):
    """Custom type eqlNASClusterUpdateFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 261),
    )


_EqlNASClusterUpdateFilename_Type.__name__ = "OctetString"
_EqlNASClusterUpdateFilename_Object = MibTableColumn
eqlNASClusterUpdateFilename = _EqlNASClusterUpdateFilename_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23, 1, 2),
    _EqlNASClusterUpdateFilename_Type()
)
eqlNASClusterUpdateFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClusterUpdateFilename.setStatus("current")


class _EqlNASClusterUpdateEQLGroupMPV_Type(Unsigned32):
    """Custom type eqlNASClusterUpdateEQLGroupMPV based on Unsigned32"""
    defaultValue = 0


_EqlNASClusterUpdateEQLGroupMPV_Object = MibTableColumn
eqlNASClusterUpdateEQLGroupMPV = _EqlNASClusterUpdateEQLGroupMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23, 1, 3),
    _EqlNASClusterUpdateEQLGroupMPV_Type()
)
eqlNASClusterUpdateEQLGroupMPV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClusterUpdateEQLGroupMPV.setStatus("current")


class _EqlNASClusterUpdateClusterMPV_Type(Unsigned32):
    """Custom type eqlNASClusterUpdateClusterMPV based on Unsigned32"""
    defaultValue = 0


_EqlNASClusterUpdateClusterMPV_Object = MibTableColumn
eqlNASClusterUpdateClusterMPV = _EqlNASClusterUpdateClusterMPV_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23, 1, 4),
    _EqlNASClusterUpdateClusterMPV_Type()
)
eqlNASClusterUpdateClusterMPV.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClusterUpdateClusterMPV.setStatus("current")


class _EqlNASClusterUpdateEQLGroupCurrentCompLevel_Type(Unsigned32):
    """Custom type eqlNASClusterUpdateEQLGroupCurrentCompLevel based on Unsigned32"""
    defaultValue = 0


_EqlNASClusterUpdateEQLGroupCurrentCompLevel_Object = MibTableColumn
eqlNASClusterUpdateEQLGroupCurrentCompLevel = _EqlNASClusterUpdateEQLGroupCurrentCompLevel_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23, 1, 5),
    _EqlNASClusterUpdateEQLGroupCurrentCompLevel_Type()
)
eqlNASClusterUpdateEQLGroupCurrentCompLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClusterUpdateEQLGroupCurrentCompLevel.setStatus("current")


class _EqlNASClusterUpdateRequestId_Type(Counter64):
    """Custom type eqlNASClusterUpdateRequestId based on Counter64"""
    defaultValue = 0


_EqlNASClusterUpdateRequestId_Object = MibTableColumn
eqlNASClusterUpdateRequestId = _EqlNASClusterUpdateRequestId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 23, 1, 6),
    _EqlNASClusterUpdateRequestId_Type()
)
eqlNASClusterUpdateRequestId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClusterUpdateRequestId.setStatus("current")
_EqlNASClusterInfoTable_Object = MibTable
eqlNASClusterInfoTable = _EqlNASClusterInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24)
)
if mibBuilder.loadTexts:
    eqlNASClusterInfoTable.setStatus("current")
_EqlNASClusterInfoEntry_Object = MibTableRow
eqlNASClusterInfoEntry = _EqlNASClusterInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1)
)
eqlNASClusterInfoEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASClusterInfoSiteType"),
    (0, "EQLVOLUME-MIB", "eqliscsiVolumeReplSiteIndex"),
    (0, "EQLNAS-MIB", "eqlNASClusterInfoSegmentId"),
)
if mibBuilder.loadTexts:
    eqlNASClusterInfoEntry.setStatus("current")
_EqlNASClusterInfoRowStatus_Type = RowStatus
_EqlNASClusterInfoRowStatus_Object = MibTableColumn
eqlNASClusterInfoRowStatus = _EqlNASClusterInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1, 1),
    _EqlNASClusterInfoRowStatus_Type()
)
eqlNASClusterInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASClusterInfoRowStatus.setStatus("current")


class _EqlNASClusterInfoSiteType_Type(Integer32):
    """Custom type eqlNASClusterInfoSiteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_EqlNASClusterInfoSiteType_Type.__name__ = "Integer32"
_EqlNASClusterInfoSiteType_Object = MibTableColumn
eqlNASClusterInfoSiteType = _EqlNASClusterInfoSiteType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1, 2),
    _EqlNASClusterInfoSiteType_Type()
)
eqlNASClusterInfoSiteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASClusterInfoSiteType.setStatus("current")
_EqlNASClusterInfoSegmentId_Type = Unsigned32
_EqlNASClusterInfoSegmentId_Object = MibTableColumn
eqlNASClusterInfoSegmentId = _EqlNASClusterInfoSegmentId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1, 3),
    _EqlNASClusterInfoSegmentId_Type()
)
eqlNASClusterInfoSegmentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASClusterInfoSegmentId.setStatus("current")
_EqlNASClusterInfoSegmentSize_Type = Unsigned32
_EqlNASClusterInfoSegmentSize_Object = MibTableColumn
eqlNASClusterInfoSegmentSize = _EqlNASClusterInfoSegmentSize_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1, 4),
    _EqlNASClusterInfoSegmentSize_Type()
)
eqlNASClusterInfoSegmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClusterInfoSegmentSize.setStatus("current")
_EqlNASClusterInfoMoreSegment_Type = TruthValue
_EqlNASClusterInfoMoreSegment_Object = MibTableColumn
eqlNASClusterInfoMoreSegment = _EqlNASClusterInfoMoreSegment_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1, 5),
    _EqlNASClusterInfoMoreSegment_Type()
)
eqlNASClusterInfoMoreSegment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClusterInfoMoreSegment.setStatus("current")
_EqlNASClusterInfoCertificate_Type = CertificateType
_EqlNASClusterInfoCertificate_Object = MibTableColumn
eqlNASClusterInfoCertificate = _EqlNASClusterInfoCertificate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1, 6),
    _EqlNASClusterInfoCertificate_Type()
)
eqlNASClusterInfoCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClusterInfoCertificate.setStatus("current")
_EqlNASClusterInfoClusterId_Type = ClusterIdType
_EqlNASClusterInfoClusterId_Object = MibTableColumn
eqlNASClusterInfoClusterId = _EqlNASClusterInfoClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 24, 1, 7),
    _EqlNASClusterInfoClusterId_Type()
)
eqlNASClusterInfoClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClusterInfoClusterId.setStatus("current")
_EqlNASReplPartnerClusterIdMapTable_Object = MibTable
eqlNASReplPartnerClusterIdMapTable = _EqlNASReplPartnerClusterIdMapTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 25)
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerClusterIdMapTable.setStatus("current")
_EqlNASReplPartnerClusterIdMapEntry_Object = MibTableRow
eqlNASReplPartnerClusterIdMapEntry = _EqlNASReplPartnerClusterIdMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 25, 1)
)
eqlNASReplPartnerClusterIdMapEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplPartnerClusterIdMapSanVIPType"),
    (0, "EQLNAS-MIB", "eqlNASReplPartnerClusterIdMapSanVIP"),
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerClusterIdMapEntry.setStatus("current")
_EqlNASReplPartnerClusterIdMapSanVIPType_Type = InetAddressType
_EqlNASReplPartnerClusterIdMapSanVIPType_Object = MibTableColumn
eqlNASReplPartnerClusterIdMapSanVIPType = _EqlNASReplPartnerClusterIdMapSanVIPType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 25, 1, 1),
    _EqlNASReplPartnerClusterIdMapSanVIPType_Type()
)
eqlNASReplPartnerClusterIdMapSanVIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASReplPartnerClusterIdMapSanVIPType.setStatus("current")
_EqlNASReplPartnerClusterIdMapSanVIP_Type = InetAddress
_EqlNASReplPartnerClusterIdMapSanVIP_Object = MibTableColumn
eqlNASReplPartnerClusterIdMapSanVIP = _EqlNASReplPartnerClusterIdMapSanVIP_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 25, 1, 2),
    _EqlNASReplPartnerClusterIdMapSanVIP_Type()
)
eqlNASReplPartnerClusterIdMapSanVIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASReplPartnerClusterIdMapSanVIP.setStatus("current")
_EqlNASReplPartnerClusterIdMapClusterId_Type = ClusterIdType
_EqlNASReplPartnerClusterIdMapClusterId_Object = MibTableColumn
eqlNASReplPartnerClusterIdMapClusterId = _EqlNASReplPartnerClusterIdMapClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 25, 1, 3),
    _EqlNASReplPartnerClusterIdMapClusterId_Type()
)
eqlNASReplPartnerClusterIdMapClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplPartnerClusterIdMapClusterId.setStatus("current")
_EqlNASReplPartnerConfigTable_Object = MibTable
eqlNASReplPartnerConfigTable = _EqlNASReplPartnerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 26)
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerConfigTable.setStatus("current")
_EqlNASReplPartnerConfigEntry_Object = MibTableRow
eqlNASReplPartnerConfigEntry = _EqlNASReplPartnerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 26, 1)
)
eqlNASReplPartnerConfigEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASClusterInfoClusterId"),
    (0, "EQLNAS-MIB", "eqlNASClusterInfoSegmentId"),
)
if mibBuilder.loadTexts:
    eqlNASReplPartnerConfigEntry.setStatus("current")
_EqlNASReplPartnerConfigRowStatus_Type = RowStatus
_EqlNASReplPartnerConfigRowStatus_Object = MibTableColumn
eqlNASReplPartnerConfigRowStatus = _EqlNASReplPartnerConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 26, 1, 1),
    _EqlNASReplPartnerConfigRowStatus_Type()
)
eqlNASReplPartnerConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplPartnerConfigRowStatus.setStatus("current")
_EqlNASReplPartnerConfigCertificate_Type = CertificateType
_EqlNASReplPartnerConfigCertificate_Object = MibTableColumn
eqlNASReplPartnerConfigCertificate = _EqlNASReplPartnerConfigCertificate_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 26, 1, 2),
    _EqlNASReplPartnerConfigCertificate_Type()
)
eqlNASReplPartnerConfigCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplPartnerConfigCertificate.setStatus("current")
_EqlNASReplPartnerConfigInetAddrType_Type = InetAddressType
_EqlNASReplPartnerConfigInetAddrType_Object = MibTableColumn
eqlNASReplPartnerConfigInetAddrType = _EqlNASReplPartnerConfigInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 26, 1, 3),
    _EqlNASReplPartnerConfigInetAddrType_Type()
)
eqlNASReplPartnerConfigInetAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplPartnerConfigInetAddrType.setStatus("current")
_EqlNASReplPartnerConfigInetAddr_Type = InetAddress
_EqlNASReplPartnerConfigInetAddr_Object = MibTableColumn
eqlNASReplPartnerConfigInetAddr = _EqlNASReplPartnerConfigInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 26, 1, 4),
    _EqlNASReplPartnerConfigInetAddr_Type()
)
eqlNASReplPartnerConfigInetAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASReplPartnerConfigInetAddr.setStatus("current")
_EqlNASReplTable_Object = MibTable
eqlNASReplTable = _EqlNASReplTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27)
)
if mibBuilder.loadTexts:
    eqlNASReplTable.setStatus("current")
_EqlNASReplEntry_Object = MibTableRow
eqlNASReplEntry = _EqlNASReplEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1)
)
eqlNASReplEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplSiteRemoteClusterId"),
    (0, "EQLNAS-MIB", "eqlNASReplRemoteFSId"),
)
if mibBuilder.loadTexts:
    eqlNASReplEntry.setStatus("current")
_EqlNASReplRowStatus_Type = RowStatus
_EqlNASReplRowStatus_Object = MibTableColumn
eqlNASReplRowStatus = _EqlNASReplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 1),
    _EqlNASReplRowStatus_Type()
)
eqlNASReplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplRowStatus.setStatus("current")
_EqlNASReplRemoteFSId_Type = Unsigned32
_EqlNASReplRemoteFSId_Object = MibTableColumn
eqlNASReplRemoteFSId = _EqlNASReplRemoteFSId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 2),
    _EqlNASReplRemoteFSId_Type()
)
eqlNASReplRemoteFSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplRemoteFSId.setStatus("current")
_EqlNASReplVolumeReplSiteIndex_Type = SiteIndex
_EqlNASReplVolumeReplSiteIndex_Object = MibTableColumn
eqlNASReplVolumeReplSiteIndex = _EqlNASReplVolumeReplSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 3),
    _EqlNASReplVolumeReplSiteIndex_Type()
)
eqlNASReplVolumeReplSiteIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplVolumeReplSiteIndex.setStatus("current")


class _EqlNASReplRemoteClusterName_Type(OctetString):
    """Custom type eqlNASReplRemoteClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASReplRemoteClusterName_Type.__name__ = "OctetString"
_EqlNASReplRemoteClusterName_Object = MibTableColumn
eqlNASReplRemoteClusterName = _EqlNASReplRemoteClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 4),
    _EqlNASReplRemoteClusterName_Type()
)
eqlNASReplRemoteClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplRemoteClusterName.setStatus("current")


class _EqlNASReplRemoteFSName_Type(OctetString):
    """Custom type eqlNASReplRemoteFSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASReplRemoteFSName_Type.__name__ = "OctetString"
_EqlNASReplRemoteFSName_Object = MibTableColumn
eqlNASReplRemoteFSName = _EqlNASReplRemoteFSName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 5),
    _EqlNASReplRemoteFSName_Type()
)
eqlNASReplRemoteFSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplRemoteFSName.setStatus("current")
_EqlNASReplAchievedRecoveryTime_Type = Counter32
_EqlNASReplAchievedRecoveryTime_Object = MibTableColumn
eqlNASReplAchievedRecoveryTime = _EqlNASReplAchievedRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 6),
    _EqlNASReplAchievedRecoveryTime_Type()
)
eqlNASReplAchievedRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplAchievedRecoveryTime.setStatus("current")
_EqlNASReplNextRecoveryTime_Type = Counter32
_EqlNASReplNextRecoveryTime_Object = MibTableColumn
eqlNASReplNextRecoveryTime = _EqlNASReplNextRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 7),
    _EqlNASReplNextRecoveryTime_Type()
)
eqlNASReplNextRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplNextRecoveryTime.setStatus("current")
_EqlNASReplTargetRecoveryTime_Type = Counter32
_EqlNASReplTargetRecoveryTime_Object = MibTableColumn
eqlNASReplTargetRecoveryTime = _EqlNASReplTargetRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 8),
    _EqlNASReplTargetRecoveryTime_Type()
)
eqlNASReplTargetRecoveryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplTargetRecoveryTime.setStatus("current")
_EqlNASReplTransferredPercent_Type = Unsigned32
_EqlNASReplTransferredPercent_Object = MibTableColumn
eqlNASReplTransferredPercent = _EqlNASReplTransferredPercent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 9),
    _EqlNASReplTransferredPercent_Type()
)
eqlNASReplTransferredPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplTransferredPercent.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASReplTransferredPercent.setUnits("%")
_EqlNASReplTransferredMB_Type = Unsigned32
_EqlNASReplTransferredMB_Object = MibTableColumn
eqlNASReplTransferredMB = _EqlNASReplTransferredMB_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 10),
    _EqlNASReplTransferredMB_Type()
)
eqlNASReplTransferredMB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplTransferredMB.setStatus("current")
_EqlNASReplStatus_Type = EqlNASReplicationStatus
_EqlNASReplStatus_Object = MibTableColumn
eqlNASReplStatus = _EqlNASReplStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 11),
    _EqlNASReplStatus_Type()
)
eqlNASReplStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplStatus.setStatus("current")


class _EqlNASReplAction_Type(Integer32):
    """Custom type eqlNASReplAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              110,
              111,
              112)
        )
    )
    namedValues = NamedValues(
        *(("cancel", 4),
          ("delete", 8),
          ("demote", 5),
          ("force-delete", 9),
          ("force-promote", 7),
          ("inbound-delete", 102),
          ("inbound-delete-failback", 107),
          ("inbound-delete-failback-restore-cfg", 108),
          ("inbound-pause", 110),
          ("inbound-promote", 103),
          ("inbound-promote-keep-demote", 105),
          ("inbound-promote-keep-demote-restore-cfg", 106),
          ("inbound-promote-restore-cfg", 104),
          ("inbound-resume", 111),
          ("internal-promote", 112),
          ("none", 0),
          ("outbound-delete", 100),
          ("outbound-force-delete", 101),
          ("pause", 2),
          ("promote", 6),
          ("replicate", 1),
          ("restore-cfg", 109),
          ("resume", 3))
    )


_EqlNASReplAction_Type.__name__ = "Integer32"
_EqlNASReplAction_Object = MibTableColumn
eqlNASReplAction = _EqlNASReplAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 12),
    _EqlNASReplAction_Type()
)
eqlNASReplAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASReplAction.setStatus("current")
_EqlNASReplSecsToComplete_Type = Unsigned32
_EqlNASReplSecsToComplete_Object = MibTableColumn
eqlNASReplSecsToComplete = _EqlNASReplSecsToComplete_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 13),
    _EqlNASReplSecsToComplete_Type()
)
eqlNASReplSecsToComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplSecsToComplete.setStatus("current")
_EqlNASReplError_Type = EqlNASReplicationError
_EqlNASReplError_Object = MibTableColumn
eqlNASReplError = _EqlNASReplError_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 14),
    _EqlNASReplError_Type()
)
eqlNASReplError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplError.setStatus("current")
_EqlNASReplRole_Type = EqlNASReplicationRole
_EqlNASReplRole_Object = MibTableColumn
eqlNASReplRole = _EqlNASReplRole_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 15),
    _EqlNASReplRole_Type()
)
eqlNASReplRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplRole.setStatus("current")
_EqlNASReplCurrentXferRateKbps_Type = Unsigned32
_EqlNASReplCurrentXferRateKbps_Object = MibTableColumn
eqlNASReplCurrentXferRateKbps = _EqlNASReplCurrentXferRateKbps_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 27, 1, 16),
    _EqlNASReplCurrentXferRateKbps_Type()
)
eqlNASReplCurrentXferRateKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplCurrentXferRateKbps.setStatus("current")
_EqlNASConfigStateTable_Object = MibTable
eqlNASConfigStateTable = _EqlNASConfigStateTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 28)
)
if mibBuilder.loadTexts:
    eqlNASConfigStateTable.setStatus("current")
_EqlNASConfigStateEntry_Object = MibTableRow
eqlNASConfigStateEntry = _EqlNASConfigStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 28, 1)
)
eqlNASConfigStateEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlNASConfigStateEntry.setStatus("current")


class _EqlNASConfigStateConfigFinished_Type(TruthValue):
    """Custom type eqlNASConfigStateConfigFinished based on TruthValue"""


_EqlNASConfigStateConfigFinished_Object = MibTableColumn
eqlNASConfigStateConfigFinished = _EqlNASConfigStateConfigFinished_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 28, 1, 1),
    _EqlNASConfigStateConfigFinished_Type()
)
eqlNASConfigStateConfigFinished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASConfigStateConfigFinished.setStatus("current")


class _EqlNASConfigStateHardwareReplaceInProgress_Type(TruthValue):
    """Custom type eqlNASConfigStateHardwareReplaceInProgress based on TruthValue"""


_EqlNASConfigStateHardwareReplaceInProgress_Object = MibTableColumn
eqlNASConfigStateHardwareReplaceInProgress = _EqlNASConfigStateHardwareReplaceInProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 28, 1, 2),
    _EqlNASConfigStateHardwareReplaceInProgress_Type()
)
eqlNASConfigStateHardwareReplaceInProgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASConfigStateHardwareReplaceInProgress.setStatus("current")
_EqlNASClientTable_Object = MibTable
eqlNASClientTable = _EqlNASClientTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29)
)
if mibBuilder.loadTexts:
    eqlNASClientTable.setStatus("current")
_EqlNASClientEntry_Object = MibTableRow
eqlNASClientEntry = _EqlNASClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1)
)
eqlNASClientEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASClientNodeIndex"),
    (0, "EQLNAS-MIB", "eqlNASClientIPAddressType"),
    (0, "EQLNAS-MIB", "eqlNASClientIPAddress"),
    (0, "EQLNAS-MIB", "eqlNASClientUserName"),
    (0, "EQLNAS-MIB", "eqlNASClientProtocol"),
)
if mibBuilder.loadTexts:
    eqlNASClientEntry.setStatus("current")
_EqlNASClientNodeIndex_Type = Unsigned32
_EqlNASClientNodeIndex_Object = MibTableColumn
eqlNASClientNodeIndex = _EqlNASClientNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 1),
    _EqlNASClientNodeIndex_Type()
)
eqlNASClientNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientNodeIndex.setStatus("current")
_EqlNASClientIPAddressType_Type = InetAddressType
_EqlNASClientIPAddressType_Object = MibTableColumn
eqlNASClientIPAddressType = _EqlNASClientIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 2),
    _EqlNASClientIPAddressType_Type()
)
eqlNASClientIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientIPAddressType.setStatus("current")
_EqlNASClientIPAddress_Type = InetAddress
_EqlNASClientIPAddress_Object = MibTableColumn
eqlNASClientIPAddress = _EqlNASClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 3),
    _EqlNASClientIPAddress_Type()
)
eqlNASClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientIPAddress.setStatus("current")


class _EqlNASClientUserName_Type(OctetString):
    """Custom type eqlNASClientUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 85),
    )


_EqlNASClientUserName_Type.__name__ = "OctetString"
_EqlNASClientUserName_Object = MibTableColumn
eqlNASClientUserName = _EqlNASClientUserName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 4),
    _EqlNASClientUserName_Type()
)
eqlNASClientUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientUserName.setStatus("current")


class _EqlNASClientProtocol_Type(Integer32):
    """Custom type eqlNASClientProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cifs", 1)
    )


_EqlNASClientProtocol_Type.__name__ = "Integer32"
_EqlNASClientProtocol_Object = MibTableColumn
eqlNASClientProtocol = _EqlNASClientProtocol_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 5),
    _EqlNASClientProtocol_Type()
)
eqlNASClientProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientProtocol.setStatus("current")
_EqlNASClientConnectedTime_Type = Counter32
_EqlNASClientConnectedTime_Object = MibTableColumn
eqlNASClientConnectedTime = _EqlNASClientConnectedTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 6),
    _EqlNASClientConnectedTime_Type()
)
eqlNASClientConnectedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientConnectedTime.setStatus("current")
_EqlNASClientIdleTime_Type = Counter32
_EqlNASClientIdleTime_Object = MibTableColumn
eqlNASClientIdleTime = _EqlNASClientIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 7),
    _EqlNASClientIdleTime_Type()
)
eqlNASClientIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientIdleTime.setStatus("current")
_EqlNASClientNumOpenFiles_Type = Unsigned32
_EqlNASClientNumOpenFiles_Object = MibTableColumn
eqlNASClientNumOpenFiles = _EqlNASClientNumOpenFiles_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 8),
    _EqlNASClientNumOpenFiles_Type()
)
eqlNASClientNumOpenFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientNumOpenFiles.setStatus("current")
_EqlNASClientIsGuest_Type = TruthValue
_EqlNASClientIsGuest_Object = MibTableColumn
eqlNASClientIsGuest = _EqlNASClientIsGuest_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 29, 1, 9),
    _EqlNASClientIsGuest_Type()
)
eqlNASClientIsGuest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASClientIsGuest.setStatus("current")
_EqlNASStatsClusterTrafficRateTable_Object = MibTable
eqlNASStatsClusterTrafficRateTable = _EqlNASStatsClusterTrafficRateTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30)
)
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateTable.setStatus("current")
_EqlNASStatsClusterTrafficRateEntry_Object = MibTableRow
eqlNASStatsClusterTrafficRateEntry = _EqlNASStatsClusterTrafficRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1)
)
eqlNASStatsClusterTrafficRateEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
)
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateEntry.setStatus("current")
_EqlNASStatsClusterTrafficRateTimestamp_Type = Counter32
_EqlNASStatsClusterTrafficRateTimestamp_Object = MibTableColumn
eqlNASStatsClusterTrafficRateTimestamp = _EqlNASStatsClusterTrafficRateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 1),
    _EqlNASStatsClusterTrafficRateTimestamp_Type()
)
eqlNASStatsClusterTrafficRateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateTimestamp.setStatus("current")
_EqlNASStatsClusterTrafficRateNfsReadMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNfsReadMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNfsReadMBsPerSec = _EqlNASStatsClusterTrafficRateNfsReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 2),
    _EqlNASStatsClusterTrafficRateNfsReadMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateNfsReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNfsReadMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateNfsWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNfsWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNfsWriteMBsPerSec = _EqlNASStatsClusterTrafficRateNfsWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 3),
    _EqlNASStatsClusterTrafficRateNfsWriteMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateNfsWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNfsWriteMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateNdmpReadMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNdmpReadMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNdmpReadMBsPerSec = _EqlNASStatsClusterTrafficRateNdmpReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 4),
    _EqlNASStatsClusterTrafficRateNdmpReadMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateNdmpReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNdmpReadMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec = _EqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 5),
    _EqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateCifsReadMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateCifsReadMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateCifsReadMBsPerSec = _EqlNASStatsClusterTrafficRateCifsReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 6),
    _EqlNASStatsClusterTrafficRateCifsReadMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateCifsReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateCifsReadMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateCifsWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateCifsWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateCifsWriteMBsPerSec = _EqlNASStatsClusterTrafficRateCifsWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 7),
    _EqlNASStatsClusterTrafficRateCifsWriteMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateCifsWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateCifsWriteMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateReplicationReadMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateReplicationReadMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateReplicationReadMBsPerSec = _EqlNASStatsClusterTrafficRateReplicationReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 8),
    _EqlNASStatsClusterTrafficRateReplicationReadMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateReplicationReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateReplicationReadMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec = _EqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 9),
    _EqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec = _EqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 10),
    _EqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec = _EqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 11),
    _EqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec = _EqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 12),
    _EqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec = _EqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 13),
    _EqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec = _EqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 14),
    _EqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec_Type()
)
eqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateNfsIOPSRead_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNfsIOPSRead_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNfsIOPSRead = _EqlNASStatsClusterTrafficRateNfsIOPSRead_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 15),
    _EqlNASStatsClusterTrafficRateNfsIOPSRead_Type()
)
eqlNASStatsClusterTrafficRateNfsIOPSRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNfsIOPSRead.setStatus("current")
_EqlNASStatsClusterTrafficRateNfsIOPSWrite_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNfsIOPSWrite_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNfsIOPSWrite = _EqlNASStatsClusterTrafficRateNfsIOPSWrite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 16),
    _EqlNASStatsClusterTrafficRateNfsIOPSWrite_Type()
)
eqlNASStatsClusterTrafficRateNfsIOPSWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNfsIOPSWrite.setStatus("current")
_EqlNASStatsClusterTrafficRateNfsIOPSOther_Type = Unsigned32
_EqlNASStatsClusterTrafficRateNfsIOPSOther_Object = MibTableColumn
eqlNASStatsClusterTrafficRateNfsIOPSOther = _EqlNASStatsClusterTrafficRateNfsIOPSOther_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 17),
    _EqlNASStatsClusterTrafficRateNfsIOPSOther_Type()
)
eqlNASStatsClusterTrafficRateNfsIOPSOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateNfsIOPSOther.setStatus("current")
_EqlNASStatsClusterTrafficRateCifsIOPSRead_Type = Unsigned32
_EqlNASStatsClusterTrafficRateCifsIOPSRead_Object = MibTableColumn
eqlNASStatsClusterTrafficRateCifsIOPSRead = _EqlNASStatsClusterTrafficRateCifsIOPSRead_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 18),
    _EqlNASStatsClusterTrafficRateCifsIOPSRead_Type()
)
eqlNASStatsClusterTrafficRateCifsIOPSRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateCifsIOPSRead.setStatus("current")
_EqlNASStatsClusterTrafficRateCifsIOPSWrite_Type = Unsigned32
_EqlNASStatsClusterTrafficRateCifsIOPSWrite_Object = MibTableColumn
eqlNASStatsClusterTrafficRateCifsIOPSWrite = _EqlNASStatsClusterTrafficRateCifsIOPSWrite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 19),
    _EqlNASStatsClusterTrafficRateCifsIOPSWrite_Type()
)
eqlNASStatsClusterTrafficRateCifsIOPSWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateCifsIOPSWrite.setStatus("current")
_EqlNASStatsClusterTrafficRateCifsIOPSOther_Type = Unsigned32
_EqlNASStatsClusterTrafficRateCifsIOPSOther_Object = MibTableColumn
eqlNASStatsClusterTrafficRateCifsIOPSOther = _EqlNASStatsClusterTrafficRateCifsIOPSOther_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 20),
    _EqlNASStatsClusterTrafficRateCifsIOPSOther_Type()
)
eqlNASStatsClusterTrafficRateCifsIOPSOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateCifsIOPSOther.setStatus("current")
_EqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec = _EqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 21),
    _EqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec.setStatus("current")
_EqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec_Type = Unsigned32
_EqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec_Object = MibTableColumn
eqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec = _EqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 30, 1, 22),
    _EqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec_Type()
)
eqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateTable_Object = MibTable
eqlNASStatsControllerTrafficRateTable = _EqlNASStatsControllerTrafficRateTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31)
)
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateTable.setStatus("current")
_EqlNASStatsControllerTrafficRateEntry_Object = MibTableRow
eqlNASStatsControllerTrafficRateEntry = _EqlNASStatsControllerTrafficRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1)
)
eqlNASStatsControllerTrafficRateEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASStatsControllerTrafficRateIndex"),
)
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateEntry.setStatus("current")
_EqlNASStatsControllerTrafficRateIndex_Type = Unsigned32
_EqlNASStatsControllerTrafficRateIndex_Object = MibTableColumn
eqlNASStatsControllerTrafficRateIndex = _EqlNASStatsControllerTrafficRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 1),
    _EqlNASStatsControllerTrafficRateIndex_Type()
)
eqlNASStatsControllerTrafficRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateIndex.setStatus("current")
_EqlNASStatsControllerTrafficRateTimestamp_Type = Counter32
_EqlNASStatsControllerTrafficRateTimestamp_Object = MibTableColumn
eqlNASStatsControllerTrafficRateTimestamp = _EqlNASStatsControllerTrafficRateTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 2),
    _EqlNASStatsControllerTrafficRateTimestamp_Type()
)
eqlNASStatsControllerTrafficRateTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateTimestamp.setStatus("current")
_EqlNASStatsControllerTrafficRateNfsReadMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNfsReadMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNfsReadMBsPerSec = _EqlNASStatsControllerTrafficRateNfsReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 3),
    _EqlNASStatsControllerTrafficRateNfsReadMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateNfsReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNfsReadMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateNfsWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNfsWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNfsWriteMBsPerSec = _EqlNASStatsControllerTrafficRateNfsWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 4),
    _EqlNASStatsControllerTrafficRateNfsWriteMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateNfsWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNfsWriteMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateNdmpReadMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNdmpReadMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNdmpReadMBsPerSec = _EqlNASStatsControllerTrafficRateNdmpReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 5),
    _EqlNASStatsControllerTrafficRateNdmpReadMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateNdmpReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNdmpReadMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec = _EqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 6),
    _EqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateCifsReadMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateCifsReadMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateCifsReadMBsPerSec = _EqlNASStatsControllerTrafficRateCifsReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 7),
    _EqlNASStatsControllerTrafficRateCifsReadMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateCifsReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateCifsReadMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateCifsWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateCifsWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateCifsWriteMBsPerSec = _EqlNASStatsControllerTrafficRateCifsWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 8),
    _EqlNASStatsControllerTrafficRateCifsWriteMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateCifsWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateCifsWriteMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateReplicationReadMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateReplicationReadMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateReplicationReadMBsPerSec = _EqlNASStatsControllerTrafficRateReplicationReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 9),
    _EqlNASStatsControllerTrafficRateReplicationReadMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateReplicationReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateReplicationReadMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec = _EqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 10),
    _EqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec = _EqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 11),
    _EqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec = _EqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 12),
    _EqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec = _EqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 13),
    _EqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec = _EqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 14),
    _EqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec = _EqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 15),
    _EqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec_Type()
)
eqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateNfsIOPSRead_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNfsIOPSRead_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNfsIOPSRead = _EqlNASStatsControllerTrafficRateNfsIOPSRead_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 16),
    _EqlNASStatsControllerTrafficRateNfsIOPSRead_Type()
)
eqlNASStatsControllerTrafficRateNfsIOPSRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNfsIOPSRead.setStatus("current")
_EqlNASStatsControllerTrafficRateNfsIOPSWrite_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNfsIOPSWrite_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNfsIOPSWrite = _EqlNASStatsControllerTrafficRateNfsIOPSWrite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 17),
    _EqlNASStatsControllerTrafficRateNfsIOPSWrite_Type()
)
eqlNASStatsControllerTrafficRateNfsIOPSWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNfsIOPSWrite.setStatus("current")
_EqlNASStatsControllerTrafficRateNfsIOPSOther_Type = Unsigned32
_EqlNASStatsControllerTrafficRateNfsIOPSOther_Object = MibTableColumn
eqlNASStatsControllerTrafficRateNfsIOPSOther = _EqlNASStatsControllerTrafficRateNfsIOPSOther_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 18),
    _EqlNASStatsControllerTrafficRateNfsIOPSOther_Type()
)
eqlNASStatsControllerTrafficRateNfsIOPSOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateNfsIOPSOther.setStatus("current")
_EqlNASStatsControllerTrafficRateCifsIOPSRead_Type = Unsigned32
_EqlNASStatsControllerTrafficRateCifsIOPSRead_Object = MibTableColumn
eqlNASStatsControllerTrafficRateCifsIOPSRead = _EqlNASStatsControllerTrafficRateCifsIOPSRead_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 19),
    _EqlNASStatsControllerTrafficRateCifsIOPSRead_Type()
)
eqlNASStatsControllerTrafficRateCifsIOPSRead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateCifsIOPSRead.setStatus("current")
_EqlNASStatsControllerTrafficRateCifsIOPSWrite_Type = Unsigned32
_EqlNASStatsControllerTrafficRateCifsIOPSWrite_Object = MibTableColumn
eqlNASStatsControllerTrafficRateCifsIOPSWrite = _EqlNASStatsControllerTrafficRateCifsIOPSWrite_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 20),
    _EqlNASStatsControllerTrafficRateCifsIOPSWrite_Type()
)
eqlNASStatsControllerTrafficRateCifsIOPSWrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateCifsIOPSWrite.setStatus("current")
_EqlNASStatsControllerTrafficRateCifsIOPSOther_Type = Unsigned32
_EqlNASStatsControllerTrafficRateCifsIOPSOther_Object = MibTableColumn
eqlNASStatsControllerTrafficRateCifsIOPSOther = _EqlNASStatsControllerTrafficRateCifsIOPSOther_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 21),
    _EqlNASStatsControllerTrafficRateCifsIOPSOther_Type()
)
eqlNASStatsControllerTrafficRateCifsIOPSOther.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateCifsIOPSOther.setStatus("current")
_EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec = _EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 22),
    _EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec.setStatus("current")
_EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage_Type = Unsigned32
_EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage_Object = MibTableColumn
eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage = _EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 23),
    _EqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage_Type()
)
eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage.setStatus("current")
_EqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec_Type = Unsigned32
_EqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec_Object = MibTableColumn
eqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec = _EqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 1, 24),
    _EqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec_Type()
)
eqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec.setStatus("current")
_EqlNASStatsControllerLoadBalancingTable_Object = MibTable
eqlNASStatsControllerLoadBalancingTable = _EqlNASStatsControllerLoadBalancingTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 2)
)
if mibBuilder.loadTexts:
    eqlNASStatsControllerLoadBalancingTable.setStatus("current")
_EqlNASStatsControllerLoadBalancingEntry_Object = MibTableRow
eqlNASStatsControllerLoadBalancingEntry = _EqlNASStatsControllerLoadBalancingEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 2, 1)
)
eqlNASStatsControllerLoadBalancingEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASStatsControllerLoadBalancingIndex"),
)
if mibBuilder.loadTexts:
    eqlNASStatsControllerLoadBalancingEntry.setStatus("current")
_EqlNASStatsControllerLoadBalancingIndex_Type = Unsigned32
_EqlNASStatsControllerLoadBalancingIndex_Object = MibTableColumn
eqlNASStatsControllerLoadBalancingIndex = _EqlNASStatsControllerLoadBalancingIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 2, 1, 1),
    _EqlNASStatsControllerLoadBalancingIndex_Type()
)
eqlNASStatsControllerLoadBalancingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerLoadBalancingIndex.setStatus("current")
_EqlNASStatsControllerLoadBalancingTimestamp_Type = Counter32
_EqlNASStatsControllerLoadBalancingTimestamp_Object = MibTableColumn
eqlNASStatsControllerLoadBalancingTimestamp = _EqlNASStatsControllerLoadBalancingTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 2, 1, 2),
    _EqlNASStatsControllerLoadBalancingTimestamp_Type()
)
eqlNASStatsControllerLoadBalancingTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerLoadBalancingTimestamp.setStatus("current")
_EqlNASStatsControllerCPULoadPercent_Type = Unsigned32
_EqlNASStatsControllerCPULoadPercent_Object = MibTableColumn
eqlNASStatsControllerCPULoadPercent = _EqlNASStatsControllerCPULoadPercent_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 2, 1, 3),
    _EqlNASStatsControllerCPULoadPercent_Type()
)
eqlNASStatsControllerCPULoadPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerCPULoadPercent.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASStatsControllerCPULoadPercent.setUnits("%")
_EqlNASStatsControllerTotalCifsConnections_Type = Unsigned32
_EqlNASStatsControllerTotalCifsConnections_Object = MibTableColumn
eqlNASStatsControllerTotalCifsConnections = _EqlNASStatsControllerTotalCifsConnections_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 31, 2, 1, 4),
    _EqlNASStatsControllerTotalCifsConnections_Type()
)
eqlNASStatsControllerTotalCifsConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASStatsControllerTotalCifsConnections.setStatus("current")
_EqlNASCacheInfoTable_Object = MibTable
eqlNASCacheInfoTable = _EqlNASCacheInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 40)
)
if mibBuilder.loadTexts:
    eqlNASCacheInfoTable.setStatus("current")
_EqlNASCacheInfoEntry_Object = MibTableRow
eqlNASCacheInfoEntry = _EqlNASCacheInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 40, 1)
)
eqlNASCacheInfoEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASCacheInfoIndex"),
)
if mibBuilder.loadTexts:
    eqlNASCacheInfoEntry.setStatus("current")
_EqlNASCacheInfoIndex_Type = Unsigned32
_EqlNASCacheInfoIndex_Object = MibTableColumn
eqlNASCacheInfoIndex = _EqlNASCacheInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 40, 1, 1),
    _EqlNASCacheInfoIndex_Type()
)
eqlNASCacheInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASCacheInfoIndex.setStatus("current")


class _EqlNASCacheInfoCacheObjectName_Type(OctetString):
    """Custom type eqlNASCacheInfoCacheObjectName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASCacheInfoCacheObjectName_Type.__name__ = "OctetString"
_EqlNASCacheInfoCacheObjectName_Object = MibTableColumn
eqlNASCacheInfoCacheObjectName = _EqlNASCacheInfoCacheObjectName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 40, 1, 2),
    _EqlNASCacheInfoCacheObjectName_Type()
)
eqlNASCacheInfoCacheObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASCacheInfoCacheObjectName.setStatus("current")
_EqlNASCacheInfoCacheObjectExpiryTime_Type = Unsigned32
_EqlNASCacheInfoCacheObjectExpiryTime_Object = MibTableColumn
eqlNASCacheInfoCacheObjectExpiryTime = _EqlNASCacheInfoCacheObjectExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 40, 1, 3),
    _EqlNASCacheInfoCacheObjectExpiryTime_Type()
)
eqlNASCacheInfoCacheObjectExpiryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASCacheInfoCacheObjectExpiryTime.setStatus("current")


class _EqlNASCacheInfoCacheObjectState_Type(OctetString):
    """Custom type eqlNASCacheInfoCacheObjectState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASCacheInfoCacheObjectState_Type.__name__ = "OctetString"
_EqlNASCacheInfoCacheObjectState_Object = MibTableColumn
eqlNASCacheInfoCacheObjectState = _EqlNASCacheInfoCacheObjectState_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 40, 1, 4),
    _EqlNASCacheInfoCacheObjectState_Type()
)
eqlNASCacheInfoCacheObjectState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASCacheInfoCacheObjectState.setStatus("current")


class _EqlNASCacheInfoAction_Type(Integer32):
    """Custom type eqlNASCacheInfoAction based on Integer32"""
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
        *(("none", 0),
          ("refresh", 2),
          ("refresh-all", 1),
          ("restart-agent", 3))
    )


_EqlNASCacheInfoAction_Type.__name__ = "Integer32"
_EqlNASCacheInfoAction_Object = MibTableColumn
eqlNASCacheInfoAction = _EqlNASCacheInfoAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 40, 1, 5),
    _EqlNASCacheInfoAction_Type()
)
eqlNASCacheInfoAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASCacheInfoAction.setStatus("current")
_EqlNASReplHistoryTable_Object = MibTable
eqlNASReplHistoryTable = _EqlNASReplHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41)
)
if mibBuilder.loadTexts:
    eqlNASReplHistoryTable.setStatus("current")
_EqlNASReplHistoryEntry_Object = MibTableRow
eqlNASReplHistoryEntry = _EqlNASReplHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1)
)
eqlNASReplHistoryEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplHistoryUniqueId"),
)
if mibBuilder.loadTexts:
    eqlNASReplHistoryEntry.setStatus("current")
_EqlNASReplHistoryUniqueId_Type = Unsigned32
_EqlNASReplHistoryUniqueId_Object = MibTableColumn
eqlNASReplHistoryUniqueId = _EqlNASReplHistoryUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 1),
    _EqlNASReplHistoryUniqueId_Type()
)
eqlNASReplHistoryUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryUniqueId.setStatus("current")
_EqlNASReplHistoryEventTime_Type = Integer32
_EqlNASReplHistoryEventTime_Object = MibTableColumn
eqlNASReplHistoryEventTime = _EqlNASReplHistoryEventTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 2),
    _EqlNASReplHistoryEventTime_Type()
)
eqlNASReplHistoryEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryEventTime.setStatus("current")
_EqlNASReplHistorySourceContainerName_Type = NASContainerNameType
_EqlNASReplHistorySourceContainerName_Object = MibTableColumn
eqlNASReplHistorySourceContainerName = _EqlNASReplHistorySourceContainerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 3),
    _EqlNASReplHistorySourceContainerName_Type()
)
eqlNASReplHistorySourceContainerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistorySourceContainerName.setStatus("current")
_EqlNASReplHistorySourceClusterName_Type = ClusterNameType
_EqlNASReplHistorySourceClusterName_Object = MibTableColumn
eqlNASReplHistorySourceClusterName = _EqlNASReplHistorySourceClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 4),
    _EqlNASReplHistorySourceClusterName_Type()
)
eqlNASReplHistorySourceClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistorySourceClusterName.setStatus("current")
_EqlNASReplHistoryDestContainerName_Type = NASContainerNameType
_EqlNASReplHistoryDestContainerName_Object = MibTableColumn
eqlNASReplHistoryDestContainerName = _EqlNASReplHistoryDestContainerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 5),
    _EqlNASReplHistoryDestContainerName_Type()
)
eqlNASReplHistoryDestContainerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryDestContainerName.setStatus("current")
_EqlNASReplHistoryDestClusterName_Type = ClusterNameType
_EqlNASReplHistoryDestClusterName_Object = MibTableColumn
eqlNASReplHistoryDestClusterName = _EqlNASReplHistoryDestClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 6),
    _EqlNASReplHistoryDestClusterName_Type()
)
eqlNASReplHistoryDestClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryDestClusterName.setStatus("current")
_EqlNASReplHistoryStartTime_Type = Integer32
_EqlNASReplHistoryStartTime_Object = MibTableColumn
eqlNASReplHistoryStartTime = _EqlNASReplHistoryStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 7),
    _EqlNASReplHistoryStartTime_Type()
)
eqlNASReplHistoryStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryStartTime.setStatus("current")
_EqlNASReplHistoryEndTime_Type = Integer32
_EqlNASReplHistoryEndTime_Object = MibTableColumn
eqlNASReplHistoryEndTime = _EqlNASReplHistoryEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 8),
    _EqlNASReplHistoryEndTime_Type()
)
eqlNASReplHistoryEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryEndTime.setStatus("current")
_EqlNASReplHistoryTransferredMb_Type = Counter32
_EqlNASReplHistoryTransferredMb_Object = MibTableColumn
eqlNASReplHistoryTransferredMb = _EqlNASReplHistoryTransferredMb_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 9),
    _EqlNASReplHistoryTransferredMb_Type()
)
eqlNASReplHistoryTransferredMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryTransferredMb.setStatus("current")
_EqlNASReplHistoryStatus_Type = EqlNASReplicationStatus
_EqlNASReplHistoryStatus_Object = MibTableColumn
eqlNASReplHistoryStatus = _EqlNASReplHistoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 41, 1, 10),
    _EqlNASReplHistoryStatus_Type()
)
eqlNASReplHistoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASReplHistoryStatus.setStatus("current")
_EqlNASTaskTable_Object = MibTable
eqlNASTaskTable = _EqlNASTaskTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42)
)
if mibBuilder.loadTexts:
    eqlNASTaskTable.setStatus("current")
_EqlNASTaskEntry_Object = MibTableRow
eqlNASTaskEntry = _EqlNASTaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1)
)
eqlNASTaskEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASTaskIndex"),
)
if mibBuilder.loadTexts:
    eqlNASTaskEntry.setStatus("current")
_EqlNASTaskIndex_Type = Unsigned32
_EqlNASTaskIndex_Object = MibTableColumn
eqlNASTaskIndex = _EqlNASTaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 1),
    _EqlNASTaskIndex_Type()
)
eqlNASTaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eqlNASTaskIndex.setStatus("current")
_EqlNASTaskRowStatus_Type = RowStatus
_EqlNASTaskRowStatus_Object = MibTableColumn
eqlNASTaskRowStatus = _EqlNASTaskRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 2),
    _EqlNASTaskRowStatus_Type()
)
eqlNASTaskRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskRowStatus.setStatus("current")


class _EqlNASTaskType_Type(Integer32):
    """Custom type eqlNASTaskType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failback", 2),
          ("resync", 1))
    )


_EqlNASTaskType_Type.__name__ = "Integer32"
_EqlNASTaskType_Object = MibTableColumn
eqlNASTaskType = _EqlNASTaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 3),
    _EqlNASTaskType_Type()
)
eqlNASTaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskType.setStatus("current")


class _EqlNASTaskContext_Type(OctetString):
    """Custom type eqlNASTaskContext based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EqlNASTaskContext_Type.__name__ = "OctetString"
_EqlNASTaskContext_Object = MibTableColumn
eqlNASTaskContext = _EqlNASTaskContext_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 4),
    _EqlNASTaskContext_Type()
)
eqlNASTaskContext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskContext.setStatus("current")
_EqlNASTaskNumSubTasks_Type = Unsigned32
_EqlNASTaskNumSubTasks_Object = MibTableColumn
eqlNASTaskNumSubTasks = _EqlNASTaskNumSubTasks_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 5),
    _EqlNASTaskNumSubTasks_Type()
)
eqlNASTaskNumSubTasks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskNumSubTasks.setStatus("current")


class _EqlNASTaskSubTaskInProgress_Type(Integer32):
    """Custom type eqlNASTaskSubTaskInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              110,
              120,
              130,
              140,
              150,
              160,
              170,
              300,
              310,
              320,
              330,
              340,
              350,
              360,
              370,
              380,
              10000)
        )
    )
    namedValues = NamedValues(
        *(("complete", 10000),
          ("failback-primaryContainerPromote", 300),
          ("failback-primaryContainerReplicationConfigure", 380),
          ("failback-primaryContainerReplicationDelete", 310),
          ("failback-recoveryContainerDisableSchedules", 330),
          ("failback-recoveryContainerFinalReplication", 350),
          ("failback-recoveryContainerPromote", 360),
          ("failback-recoveryContainerReplicate", 340),
          ("failback-recoveryContainerReplicationConfigure", 320),
          ("failback-recoveryContainerReplicationDelete", 370),
          ("none", 0),
          ("resync-primaryContainerPromote", 100),
          ("resync-primaryContainerReplicationConfigure", 160),
          ("resync-primaryContainerReplicationDelete", 110),
          ("resync-recoveryContainerPromote", 170),
          ("resync-recoveryContainerReplicate", 130),
          ("resync-recoveryContainerReplicationConfigure", 120),
          ("resync-recoveryContainerReplicationDelete", 150),
          ("resync-recoveryContainerSourcePromote", 140))
    )


_EqlNASTaskSubTaskInProgress_Type.__name__ = "Integer32"
_EqlNASTaskSubTaskInProgress_Object = MibTableColumn
eqlNASTaskSubTaskInProgress = _EqlNASTaskSubTaskInProgress_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 6),
    _EqlNASTaskSubTaskInProgress_Type()
)
eqlNASTaskSubTaskInProgress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskSubTaskInProgress.setStatus("current")
_EqlNASTaskSubtaskStatus_Type = Unsigned32
_EqlNASTaskSubtaskStatus_Object = MibTableColumn
eqlNASTaskSubtaskStatus = _EqlNASTaskSubtaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 7),
    _EqlNASTaskSubtaskStatus_Type()
)
eqlNASTaskSubtaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskSubtaskStatus.setStatus("current")


class _EqlNASTaskStatus_Type(Integer32):
    """Custom type eqlNASTaskStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("complete", 3),
          ("in-progress", 2),
          ("user-action-required", 1))
    )


_EqlNASTaskStatus_Type.__name__ = "Integer32"
_EqlNASTaskStatus_Object = MibTableColumn
eqlNASTaskStatus = _EqlNASTaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 8),
    _EqlNASTaskStatus_Type()
)
eqlNASTaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskStatus.setStatus("current")


class _EqlNASTaskUserAction_Type(Integer32):
    """Custom type eqlNASTaskUserAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("retry", 1)
    )


_EqlNASTaskUserAction_Type.__name__ = "Integer32"
_EqlNASTaskUserAction_Object = MibTableColumn
eqlNASTaskUserAction = _EqlNASTaskUserAction_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 9),
    _EqlNASTaskUserAction_Type()
)
eqlNASTaskUserAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskUserAction.setStatus("current")
_EqlNASTaskStartTime_Type = Counter32
_EqlNASTaskStartTime_Object = MibTableColumn
eqlNASTaskStartTime = _EqlNASTaskStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 42, 1, 10),
    _EqlNASTaskStartTime_Type()
)
eqlNASTaskStartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskStartTime.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASTaskStartTime.setUnits("seconds")
_EqlNASTaskContainerReplInfoTable_Object = MibTable
eqlNASTaskContainerReplInfoTable = _EqlNASTaskContainerReplInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43)
)
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoTable.setStatus("current")
_EqlNASTaskContainerReplInfoEntry_Object = MibTableRow
eqlNASTaskContainerReplInfoEntry = _EqlNASTaskContainerReplInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1)
)
eqlNASTaskContainerReplInfoEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
    (0, "EQLNAS-MIB", "eqlNASReplSiteRemoteClusterId"),
    (0, "EQLNAS-MIB", "eqlNASTaskContainerReplInfoRemoteFSId"),
)
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoEntry.setStatus("current")
_EqlNASTaskContainerReplInfoRowStatus_Type = RowStatus
_EqlNASTaskContainerReplInfoRowStatus_Object = MibTableColumn
eqlNASTaskContainerReplInfoRowStatus = _EqlNASTaskContainerReplInfoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 1),
    _EqlNASTaskContainerReplInfoRowStatus_Type()
)
eqlNASTaskContainerReplInfoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoRowStatus.setStatus("current")
_EqlNASTaskContainerReplInfoRemoteFSId_Type = Unsigned32
_EqlNASTaskContainerReplInfoRemoteFSId_Object = MibTableColumn
eqlNASTaskContainerReplInfoRemoteFSId = _EqlNASTaskContainerReplInfoRemoteFSId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 2),
    _EqlNASTaskContainerReplInfoRemoteFSId_Type()
)
eqlNASTaskContainerReplInfoRemoteFSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoRemoteFSId.setStatus("current")
_EqlNASTaskContainerReplInfoVolumeReplSiteIndex_Type = SiteIndex
_EqlNASTaskContainerReplInfoVolumeReplSiteIndex_Object = MibTableColumn
eqlNASTaskContainerReplInfoVolumeReplSiteIndex = _EqlNASTaskContainerReplInfoVolumeReplSiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 3),
    _EqlNASTaskContainerReplInfoVolumeReplSiteIndex_Type()
)
eqlNASTaskContainerReplInfoVolumeReplSiteIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoVolumeReplSiteIndex.setStatus("current")


class _EqlNASTaskContainerReplInfoRemoteClusterName_Type(OctetString):
    """Custom type eqlNASTaskContainerReplInfoRemoteClusterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EqlNASTaskContainerReplInfoRemoteClusterName_Type.__name__ = "OctetString"
_EqlNASTaskContainerReplInfoRemoteClusterName_Object = MibTableColumn
eqlNASTaskContainerReplInfoRemoteClusterName = _EqlNASTaskContainerReplInfoRemoteClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 4),
    _EqlNASTaskContainerReplInfoRemoteClusterName_Type()
)
eqlNASTaskContainerReplInfoRemoteClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoRemoteClusterName.setStatus("current")


class _EqlNASTaskContainerReplInfoLocalFSName_Type(OctetString):
    """Custom type eqlNASTaskContainerReplInfoLocalFSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASTaskContainerReplInfoLocalFSName_Type.__name__ = "OctetString"
_EqlNASTaskContainerReplInfoLocalFSName_Object = MibTableColumn
eqlNASTaskContainerReplInfoLocalFSName = _EqlNASTaskContainerReplInfoLocalFSName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 5),
    _EqlNASTaskContainerReplInfoLocalFSName_Type()
)
eqlNASTaskContainerReplInfoLocalFSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoLocalFSName.setStatus("current")


class _EqlNASTaskContainerReplInfoRemoteFSName_Type(OctetString):
    """Custom type eqlNASTaskContainerReplInfoRemoteFSName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASTaskContainerReplInfoRemoteFSName_Type.__name__ = "OctetString"
_EqlNASTaskContainerReplInfoRemoteFSName_Object = MibTableColumn
eqlNASTaskContainerReplInfoRemoteFSName = _EqlNASTaskContainerReplInfoRemoteFSName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 6),
    _EqlNASTaskContainerReplInfoRemoteFSName_Type()
)
eqlNASTaskContainerReplInfoRemoteFSName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoRemoteFSName.setStatus("current")
_EqlNASTaskContainerReplInfoLocalClusterId_Type = ClusterIdType
_EqlNASTaskContainerReplInfoLocalClusterId_Object = MibTableColumn
eqlNASTaskContainerReplInfoLocalClusterId = _EqlNASTaskContainerReplInfoLocalClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 7),
    _EqlNASTaskContainerReplInfoLocalClusterId_Type()
)
eqlNASTaskContainerReplInfoLocalClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoLocalClusterId.setStatus("current")
_EqlNASTaskContainerReplInfoTaskId_Type = Unsigned32
_EqlNASTaskContainerReplInfoTaskId_Object = MibTableColumn
eqlNASTaskContainerReplInfoTaskId = _EqlNASTaskContainerReplInfoTaskId_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 43, 1, 8),
    _EqlNASTaskContainerReplInfoTaskId_Type()
)
eqlNASTaskContainerReplInfoTaskId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASTaskContainerReplInfoTaskId.setStatus("current")
_EqlNASLostContainerTable_Object = MibTable
eqlNASLostContainerTable = _EqlNASLostContainerTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 44)
)
if mibBuilder.loadTexts:
    eqlNASLostContainerTable.setStatus("current")
_EqlNASLostContainerEntry_Object = MibTableRow
eqlNASLostContainerEntry = _EqlNASLostContainerEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 44, 1)
)
eqlNASLostContainerEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLNAS-MIB", "eqlNASContainerIndex"),
)
if mibBuilder.loadTexts:
    eqlNASLostContainerEntry.setStatus("current")
_EqlNASLostContainerRowStatus_Type = RowStatus
_EqlNASLostContainerRowStatus_Object = MibTableColumn
eqlNASLostContainerRowStatus = _EqlNASLostContainerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 44, 1, 1),
    _EqlNASLostContainerRowStatus_Type()
)
eqlNASLostContainerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASLostContainerRowStatus.setStatus("current")


class _EqlNASLostContainerName_Type(OctetString):
    """Custom type eqlNASLostContainerName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 230),
    )


_EqlNASLostContainerName_Type.__name__ = "OctetString"
_EqlNASLostContainerName_Object = MibTableColumn
eqlNASLostContainerName = _EqlNASLostContainerName_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 44, 1, 2),
    _EqlNASLostContainerName_Type()
)
eqlNASLostContainerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASLostContainerName.setStatus("current")
_EqlNASLostContainerCapacity_Type = Unsigned32
_EqlNASLostContainerCapacity_Object = MibTableColumn
eqlNASLostContainerCapacity = _EqlNASLostContainerCapacity_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 44, 1, 3),
    _EqlNASLostContainerCapacity_Type()
)
eqlNASLostContainerCapacity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASLostContainerCapacity.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASLostContainerCapacity.setUnits("MB")
_EqlNASLostContainerUsedSpaceAlert_Type = Unsigned32
_EqlNASLostContainerUsedSpaceAlert_Object = MibTableColumn
eqlNASLostContainerUsedSpaceAlert = _EqlNASLostContainerUsedSpaceAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 44, 1, 4),
    _EqlNASLostContainerUsedSpaceAlert_Type()
)
eqlNASLostContainerUsedSpaceAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASLostContainerUsedSpaceAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASLostContainerUsedSpaceAlert.setUnits("%")
_EqlNASLostContainerSnapshotUsedSpaceAlert_Type = Unsigned32
_EqlNASLostContainerSnapshotUsedSpaceAlert_Object = MibTableColumn
eqlNASLostContainerSnapshotUsedSpaceAlert = _EqlNASLostContainerSnapshotUsedSpaceAlert_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 44, 1, 5),
    _EqlNASLostContainerSnapshotUsedSpaceAlert_Type()
)
eqlNASLostContainerSnapshotUsedSpaceAlert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASLostContainerSnapshotUsedSpaceAlert.setStatus("current")
if mibBuilder.loadTexts:
    eqlNASLostContainerSnapshotUsedSpaceAlert.setUnits("%")
_EqlNASSanStaticRouteTable_Object = MibTable
eqlNASSanStaticRouteTable = _EqlNASSanStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45)
)
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteTable.setStatus("current")
_EqlNASSanStaticRouteEntry_Object = MibTableRow
eqlNASSanStaticRouteEntry = _EqlNASSanStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1)
)
eqlNASSanStaticRouteEntry.setIndexNames(
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceIndex"),
    (0, "EQLAPPLIANCE-MIB", "eqlApplianceNetworkID"),
    (0, "EQLNAS-MIB", "eqlNASSanStaticRouteNetworkAddrType"),
    (0, "EQLNAS-MIB", "eqlNASSanStaticRouteNetworkAddr"),
    (0, "EQLNAS-MIB", "eqlNASSanStaticRouteNetworkMaskType"),
    (0, "EQLNAS-MIB", "eqlNASSanStaticRouteNetworkMask"),
)
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteEntry.setStatus("current")
_EqlNASSanStaticRouteRowStatus_Type = RowStatus
_EqlNASSanStaticRouteRowStatus_Object = MibTableColumn
eqlNASSanStaticRouteRowStatus = _EqlNASSanStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1, 1),
    _EqlNASSanStaticRouteRowStatus_Type()
)
eqlNASSanStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteRowStatus.setStatus("current")
_EqlNASSanStaticRouteNetworkAddrType_Type = InetAddressType
_EqlNASSanStaticRouteNetworkAddrType_Object = MibTableColumn
eqlNASSanStaticRouteNetworkAddrType = _EqlNASSanStaticRouteNetworkAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1, 2),
    _EqlNASSanStaticRouteNetworkAddrType_Type()
)
eqlNASSanStaticRouteNetworkAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteNetworkAddrType.setStatus("current")
_EqlNASSanStaticRouteNetworkAddr_Type = InetAddress
_EqlNASSanStaticRouteNetworkAddr_Object = MibTableColumn
eqlNASSanStaticRouteNetworkAddr = _EqlNASSanStaticRouteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1, 3),
    _EqlNASSanStaticRouteNetworkAddr_Type()
)
eqlNASSanStaticRouteNetworkAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteNetworkAddr.setStatus("current")
_EqlNASSanStaticRouteNetworkMaskType_Type = InetAddressType
_EqlNASSanStaticRouteNetworkMaskType_Object = MibTableColumn
eqlNASSanStaticRouteNetworkMaskType = _EqlNASSanStaticRouteNetworkMaskType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1, 4),
    _EqlNASSanStaticRouteNetworkMaskType_Type()
)
eqlNASSanStaticRouteNetworkMaskType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteNetworkMaskType.setStatus("current")
_EqlNASSanStaticRouteNetworkMask_Type = InetAddress
_EqlNASSanStaticRouteNetworkMask_Object = MibTableColumn
eqlNASSanStaticRouteNetworkMask = _EqlNASSanStaticRouteNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1, 5),
    _EqlNASSanStaticRouteNetworkMask_Type()
)
eqlNASSanStaticRouteNetworkMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteNetworkMask.setStatus("current")
_EqlNASSanStaticRouteGatewayAddrType_Type = InetAddressType
_EqlNASSanStaticRouteGatewayAddrType_Object = MibTableColumn
eqlNASSanStaticRouteGatewayAddrType = _EqlNASSanStaticRouteGatewayAddrType_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1, 6),
    _EqlNASSanStaticRouteGatewayAddrType_Type()
)
eqlNASSanStaticRouteGatewayAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteGatewayAddrType.setStatus("current")
_EqlNASSanStaticRouteGatewayAddr_Type = InetAddress
_EqlNASSanStaticRouteGatewayAddr_Object = MibTableColumn
eqlNASSanStaticRouteGatewayAddr = _EqlNASSanStaticRouteGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 12740, 18, 1, 45, 1, 7),
    _EqlNASSanStaticRouteGatewayAddr_Type()
)
eqlNASSanStaticRouteGatewayAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eqlNASSanStaticRouteGatewayAddr.setStatus("current")
eqlNASSnapshotPolicyEntry.registerAugmentions(
    ("EQLNAS-MIB",
     "eqlNASSnapshotPolicyStatusEntry")
)
eqlNASSnapshotPolicyStatusEntry.setIndexNames(*eqlNASSnapshotPolicyEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EQLNAS-MIB",
    **{"UNIXPermissions": UNIXPermissions,
       "ClusterNameType": ClusterNameType,
       "ClusterIdType": ClusterIdType,
       "CertificateType": CertificateType,
       "NASContainerNameType": NASContainerNameType,
       "EqlNASReplicationStatus": EqlNASReplicationStatus,
       "EqlNASChassisComponentStatus": EqlNASChassisComponentStatus,
       "EqlNASChassisACPowerStatus": EqlNASChassisACPowerStatus,
       "EqlNASChassisControllerState": EqlNASChassisControllerState,
       "EqlNASChassisSanType": EqlNASChassisSanType,
       "EqlNASChassisNetworkSpeed": EqlNASChassisNetworkSpeed,
       "EqlNASChassisControllerLocation": EqlNASChassisControllerLocation,
       "EqlNASReplicationError": EqlNASReplicationError,
       "EqlNASReplicationRole": EqlNASReplicationRole,
       "eqlNASModule": eqlNASModule,
       "eqlNASObjects": eqlNASObjects,
       "eqlNASApplianceTable": eqlNASApplianceTable,
       "eqlNASApplianceEntry": eqlNASApplianceEntry,
       "eqlNASApplianceRowStatus": eqlNASApplianceRowStatus,
       "eqlNASAppliancePoolSize": eqlNASAppliancePoolSize,
       "eqlNASApplianceEQLPoolIndex": eqlNASApplianceEQLPoolIndex,
       "eqlNASApplianceReplRemoteUserName": eqlNASApplianceReplRemoteUserName,
       "eqlNASApplianceNFSv4Mode": eqlNASApplianceNFSv4Mode,
       "eqlNASContainerTable": eqlNASContainerTable,
       "eqlNASContainerEntry": eqlNASContainerEntry,
       "eqlNASContainerIndex": eqlNASContainerIndex,
       "eqlNASContainerRowStatus": eqlNASContainerRowStatus,
       "eqlNASContainerName": eqlNASContainerName,
       "eqlNASContainerCapacity": eqlNASContainerCapacity,
       "eqlNASContainerUsedSpaceAlert": eqlNASContainerUsedSpaceAlert,
       "eqlNASContainerSnapshotHardQuota": eqlNASContainerSnapshotHardQuota,
       "eqlNASContainerSnapshotUsedSpaceAlert": eqlNASContainerSnapshotUsedSpaceAlert,
       "eqlNASContainerUnixFilePermissions": eqlNASContainerUnixFilePermissions,
       "eqlNASContainerUnixDirPermissions": eqlNASContainerUnixDirPermissions,
       "eqlNASContainerQuotaEnabled": eqlNASContainerQuotaEnabled,
       "eqlNASContainerFileAccessSecurity": eqlNASContainerFileAccessSecurity,
       "eqlNASContainerAccessTimeManagementGranularity": eqlNASContainerAccessTimeManagementGranularity,
       "eqlNASContainerOptimizationEnabled": eqlNASContainerOptimizationEnabled,
       "eqlNASContainerDedupMethodType": eqlNASContainerDedupMethodType,
       "eqlNASContainerCompressionEnabled": eqlNASContainerCompressionEnabled,
       "eqlNASContainerModificationTimeFilter": eqlNASContainerModificationTimeFilter,
       "eqlNASContainerAccessTimeFilter": eqlNASContainerAccessTimeFilter,
       "eqlNASContainerExcludeFilesByNamePattern": eqlNASContainerExcludeFilesByNamePattern,
       "eqlNASContainerAction": eqlNASContainerAction,
       "eqlNASContainerDefaultUserQuota": eqlNASContainerDefaultUserQuota,
       "eqlNASContainerDefaultUserQuotaAlert": eqlNASContainerDefaultUserQuotaAlert,
       "eqlNASContainerDefaultGroupQuota": eqlNASContainerDefaultGroupQuota,
       "eqlNASContainerDefaultGroupQuotaAlert": eqlNASContainerDefaultGroupQuotaAlert,
       "eqlNASContainerOptimizationFilterMode": eqlNASContainerOptimizationFilterMode,
       "eqlNASContainerRehydrateOnReadEnabled": eqlNASContainerRehydrateOnReadEnabled,
       "eqlNASContainerUniqueIDTable": eqlNASContainerUniqueIDTable,
       "eqlNASContainerUniqueIDEntry": eqlNASContainerUniqueIDEntry,
       "eqlNASContainerUniqueIDType": eqlNASContainerUniqueIDType,
       "eqlNASContainerUniqueIDValueLen": eqlNASContainerUniqueIDValueLen,
       "eqlNASContainerUniqueIDValue": eqlNASContainerUniqueIDValue,
       "eqlNASSnapshotTable": eqlNASSnapshotTable,
       "eqlNASSnapshotEntry": eqlNASSnapshotEntry,
       "eqlNASSnapshotIndex": eqlNASSnapshotIndex,
       "eqlNASSnapshotRowStatus": eqlNASSnapshotRowStatus,
       "eqlNASSnapshotName": eqlNASSnapshotName,
       "eqlNASSnapshotSize": eqlNASSnapshotSize,
       "eqlNASSnapshotTimestamp": eqlNASSnapshotTimestamp,
       "eqlNASSnapshotRollBack": eqlNASSnapshotRollBack,
       "eqlNASSnapshotPolicyIdx": eqlNASSnapshotPolicyIdx,
       "eqlNASSnapshotPolicyTable": eqlNASSnapshotPolicyTable,
       "eqlNASSnapshotPolicyEntry": eqlNASSnapshotPolicyEntry,
       "eqlNASSnapshotPolicyIndex": eqlNASSnapshotPolicyIndex,
       "eqlNASSnapshotPolicyRowStatus": eqlNASSnapshotPolicyRowStatus,
       "eqlNASSnapshotPolicyName": eqlNASSnapshotPolicyName,
       "eqlNASSnapshotPolicyMaxKeep": eqlNASSnapshotPolicyMaxKeep,
       "eqlNASSnapshotPolicyType": eqlNASSnapshotPolicyType,
       "eqlNASSnapshotPolicyRepeatFactor": eqlNASSnapshotPolicyRepeatFactor,
       "eqlNASSnapshotPolicyStartTime": eqlNASSnapshotPolicyStartTime,
       "eqlNASSnapshotPolicyEndTime": eqlNASSnapshotPolicyEndTime,
       "eqlNASSnapshotPolicyTimeFrequency": eqlNASSnapshotPolicyTimeFrequency,
       "eqlNASSnapshotPolicyStartDate": eqlNASSnapshotPolicyStartDate,
       "eqlNASSnapshotPolicyEndDate": eqlNASSnapshotPolicyEndDate,
       "eqlNASSnapshotPolicyWeekMask": eqlNASSnapshotPolicyWeekMask,
       "eqlNASSnapshotPolicyMonthMask": eqlNASSnapshotPolicyMonthMask,
       "eqlNASSnapshotPolicyOccurence": eqlNASSnapshotPolicyOccurence,
       "eqlNASSnapshotPolicyReplication": eqlNASSnapshotPolicyReplication,
       "eqlNASSnapshotPolicyAdminStatus": eqlNASSnapshotPolicyAdminStatus,
       "eqlNASSnapshotPolicyCategory": eqlNASSnapshotPolicyCategory,
       "eqlNASSnapshotPolicyStatusTable": eqlNASSnapshotPolicyStatusTable,
       "eqlNASSnapshotPolicyStatusEntry": eqlNASSnapshotPolicyStatusEntry,
       "eqlNASSnapshotPolicyStatusNextCreate": eqlNASSnapshotPolicyStatusNextCreate,
       "eqlNASSnapshotPolicyStatusOperStatus": eqlNASSnapshotPolicyStatusOperStatus,
       "eqlNASQuotaTable": eqlNASQuotaTable,
       "eqlNASQuotaEntry": eqlNASQuotaEntry,
       "eqlNASQuotaRowStatus": eqlNASQuotaRowStatus,
       "eqlNASQuotaTargetType": eqlNASQuotaTargetType,
       "eqlNASQuotaTargetName": eqlNASQuotaTargetName,
       "eqlNASQuotaWarnLimit": eqlNASQuotaWarnLimit,
       "eqlNASQuotaHardLimit": eqlNASQuotaHardLimit,
       "eqlNASQuotaUsage": eqlNASQuotaUsage,
       "eqlNASQuotaUsageTable": eqlNASQuotaUsageTable,
       "eqlNASQuotaUsageEntry": eqlNASQuotaUsageEntry,
       "eqlNASQuotaUsageRowStatus": eqlNASQuotaUsageRowStatus,
       "eqlNASQuotaUsageTargetType": eqlNASQuotaUsageTargetType,
       "eqlNASQuotaUsageTargetName": eqlNASQuotaUsageTargetName,
       "eqlNASQuotaUsageMB": eqlNASQuotaUsageMB,
       "eqlNASGroupQuotaEffectiveRuleTable": eqlNASGroupQuotaEffectiveRuleTable,
       "eqlNASGroupQuotaEffectiveRuleEntry": eqlNASGroupQuotaEffectiveRuleEntry,
       "eqlNASGroupQuotaEffectiveRuleTargetName": eqlNASGroupQuotaEffectiveRuleTargetName,
       "eqlNASGroupQuotaEffectiveRuleRowStatus": eqlNASGroupQuotaEffectiveRuleRowStatus,
       "eqlNASGroupQuotaEffectiveRuleSoftLimit": eqlNASGroupQuotaEffectiveRuleSoftLimit,
       "eqlNASGroupQuotaEffectiveRuleHardLimit": eqlNASGroupQuotaEffectiveRuleHardLimit,
       "eqlNASGroupQuotaEffectiveRuleSoftLimitEnabled": eqlNASGroupQuotaEffectiveRuleSoftLimitEnabled,
       "eqlNASGroupQuotaEffectiveRuleHardLimitEnabled": eqlNASGroupQuotaEffectiveRuleHardLimitEnabled,
       "eqlNASUserQuotaEffectiveRuleTable": eqlNASUserQuotaEffectiveRuleTable,
       "eqlNASUserQuotaEffectiveRuleEntry": eqlNASUserQuotaEffectiveRuleEntry,
       "eqlNASUserQuotaEffectiveRuleTargetName": eqlNASUserQuotaEffectiveRuleTargetName,
       "eqlNASUserQuotaEffectiveRuleRowStatus": eqlNASUserQuotaEffectiveRuleRowStatus,
       "eqlNASUserQuotaEffectiveRuleUserSoftLimit": eqlNASUserQuotaEffectiveRuleUserSoftLimit,
       "eqlNASUserQuotaEffectiveRuleUserHardLimit": eqlNASUserQuotaEffectiveRuleUserHardLimit,
       "eqlNASUserQuotaEffectiveRuleGroupName": eqlNASUserQuotaEffectiveRuleGroupName,
       "eqlNASUserQuotaEffectiveRuleGroupSoftLimit": eqlNASUserQuotaEffectiveRuleGroupSoftLimit,
       "eqlNASUserQuotaEffectiveRuleGroupHardLimit": eqlNASUserQuotaEffectiveRuleGroupHardLimit,
       "eqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled": eqlNASUserQuotaEffectiveRuleUserSoftLimitEnabled,
       "eqlNASUserQuotaEffectiveRuleUserHardLimitEnabled": eqlNASUserQuotaEffectiveRuleUserHardLimitEnabled,
       "eqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled": eqlNASUserQuotaEffectiveRuleGroupSoftLimitEnabled,
       "eqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled": eqlNASUserQuotaEffectiveRuleGroupHardLimitEnabled,
       "eqlNASApplianceDefaultCfgTable": eqlNASApplianceDefaultCfgTable,
       "eqlNASApplianceDefaultCfgEntry": eqlNASApplianceDefaultCfgEntry,
       "eqlNASApplianceConfigUsedSpaceAlert": eqlNASApplianceConfigUsedSpaceAlert,
       "eqlNASApplianceConfigSnapSpaceAlert": eqlNASApplianceConfigSnapSpaceAlert,
       "eqlNASApplianceConfigSnapHardQuota": eqlNASApplianceConfigSnapHardQuota,
       "eqlNASApplianceContainerUnixFilePerms": eqlNASApplianceContainerUnixFilePerms,
       "eqlNASApplianceContainerUnixDirPerms": eqlNASApplianceContainerUnixDirPerms,
       "eqlNASApplianceContainerFileSecurity": eqlNASApplianceContainerFileSecurity,
       "eqlNASApplianceDefaultUserQuota": eqlNASApplianceDefaultUserQuota,
       "eqlNASApplianceDefaultUserQuotaAlert": eqlNASApplianceDefaultUserQuotaAlert,
       "eqlNASApplianceDefaultGroupQuota": eqlNASApplianceDefaultGroupQuota,
       "eqlNASApplianceDefaultGroupQuotaAlert": eqlNASApplianceDefaultGroupQuotaAlert,
       "eqlNASApplianceDefaultCIFSAllowGuestAccess": eqlNASApplianceDefaultCIFSAllowGuestAccess,
       "eqlNASApplianceCIFSAuthenticationMode": eqlNASApplianceCIFSAuthenticationMode,
       "eqlNASApplianceDefaultCIFSLockEnforcement": eqlNASApplianceDefaultCIFSLockEnforcement,
       "eqlNASApplianceNFSExportReadWrite": eqlNASApplianceNFSExportReadWrite,
       "eqlNASApplianceNFSExportTrustedUsers": eqlNASApplianceNFSExportTrustedUsers,
       "eqlNASApplianceAccessTimeManagementGranularity": eqlNASApplianceAccessTimeManagementGranularity,
       "eqlNASApplianceOptimizationEnabled": eqlNASApplianceOptimizationEnabled,
       "eqlNASApplianceDedupMethodType": eqlNASApplianceDedupMethodType,
       "eqlNASApplianceCompressionEnabled": eqlNASApplianceCompressionEnabled,
       "eqlNASApplianceModificationTimeFilter": eqlNASApplianceModificationTimeFilter,
       "eqlNASApplianceAccessTimeFilter": eqlNASApplianceAccessTimeFilter,
       "eqlNASApplianceExcludeFilesByNamePattern": eqlNASApplianceExcludeFilesByNamePattern,
       "eqlNASApplianceDefaultCIFSAntivirusEnabled": eqlNASApplianceDefaultCIFSAntivirusEnabled,
       "eqlNASApplianceDefaultCIFSAntivirusPolicy": eqlNASApplianceDefaultCIFSAntivirusPolicy,
       "eqlNASApplianceDefaultCIFSAntivirusExtensions": eqlNASApplianceDefaultCIFSAntivirusExtensions,
       "eqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy": eqlNASApplianceDefaultCIFSAntivirusExtensionsPolicy,
       "eqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths": eqlNASApplianceDefaultCIFSAntivirusExcludeDirPaths,
       "eqlNASApplianceDefaultCIFSAntivirusLargeFileSize": eqlNASApplianceDefaultCIFSAntivirusLargeFileSize,
       "eqlNASApplianceDefaultCIFSAntivirusLargeFileOpen": eqlNASApplianceDefaultCIFSAntivirusLargeFileOpen,
       "eqlNASApplianceDefaultNFSExportsFileId32bit": eqlNASApplianceDefaultNFSExportsFileId32bit,
       "eqlNASContainerStatusTable": eqlNASContainerStatusTable,
       "eqlNASContainerStatusEntry": eqlNASContainerStatusEntry,
       "eqlNASContainerStatusConnections": eqlNASContainerStatusConnections,
       "eqlNASContainerStatusUsedSpace": eqlNASContainerStatusUsedSpace,
       "eqlNASContainerStatusSnapshotSpace": eqlNASContainerStatusSnapshotSpace,
       "eqlNASContainerStatusNumNFSExports": eqlNASContainerStatusNumNFSExports,
       "eqlNASContainerStatusNumCIFSShares": eqlNASContainerStatusNumCIFSShares,
       "eqlNASContainerStatusAllocatedSpace": eqlNASContainerStatusAllocatedSpace,
       "eqlNASContainerStatusFreeSpace": eqlNASContainerStatusFreeSpace,
       "eqlNASContainerStatusNumOfSnapshots": eqlNASContainerStatusNumOfSnapshots,
       "eqlNASContainerStatusOptimizationSpaceSavings": eqlNASContainerStatusOptimizationSpaceSavings,
       "eqlNASContainerStatusOptimized": eqlNASContainerStatusOptimized,
       "eqlNASContainerStatusReplState": eqlNASContainerStatusReplState,
       "eqlNASContainerStatusNextSnapshotID": eqlNASContainerStatusNextSnapshotID,
       "eqlNASApplianceNFSExportsTable": eqlNASApplianceNFSExportsTable,
       "eqlNASApplianceNFSExportsEntry": eqlNASApplianceNFSExportsEntry,
       "eqlNASApplianceNFSExportName": eqlNASApplianceNFSExportName,
       "eqlNASApplianceNFSExportsRowStatus": eqlNASApplianceNFSExportsRowStatus,
       "eqlNASApplianceNFSExportDirectory": eqlNASApplianceNFSExportDirectory,
       "eqlNASApplianceNFSAccess": eqlNASApplianceNFSAccess,
       "eqlNASApplianceNFSLimitReportedSize": eqlNASApplianceNFSLimitReportedSize,
       "eqlNASApplianceNFSAccessClientIPType": eqlNASApplianceNFSAccessClientIPType,
       "eqlNASApplianceNFSAccessClientIP": eqlNASApplianceNFSAccessClientIP,
       "eqlNASApplianceNFSAccessClientNetmaskType": eqlNASApplianceNFSAccessClientNetmaskType,
       "eqlNASApplianceNFSAccessClientNetmask": eqlNASApplianceNFSAccessClientNetmask,
       "eqlNASApplianceNFSTrustUsers": eqlNASApplianceNFSTrustUsers,
       "eqlNASApplianceNFSExportsFileId32bit": eqlNASApplianceNFSExportsFileId32bit,
       "eqlNASApplianceCIFSTable": eqlNASApplianceCIFSTable,
       "eqlNASApplianceCIFSEntry": eqlNASApplianceCIFSEntry,
       "eqlNASApplianceCIFSShareName": eqlNASApplianceCIFSShareName,
       "eqlNASApplianceCIFSRowStatus": eqlNASApplianceCIFSRowStatus,
       "eqlNASApplianceCIFSExportedDirectory": eqlNASApplianceCIFSExportedDirectory,
       "eqlNASApplianceCIFSAllowGuestAccess": eqlNASApplianceCIFSAllowGuestAccess,
       "eqlNASApplianceCIFSLockEnforcement": eqlNASApplianceCIFSLockEnforcement,
       "eqlNASApplianceCIFSAntivirusEnabled": eqlNASApplianceCIFSAntivirusEnabled,
       "eqlNASApplianceCIFSAntivirusPolicy": eqlNASApplianceCIFSAntivirusPolicy,
       "eqlNASApplianceCIFSAntivirusExtensions": eqlNASApplianceCIFSAntivirusExtensions,
       "eqlNASApplianceCIFSAntivirusExtensionsPolicy": eqlNASApplianceCIFSAntivirusExtensionsPolicy,
       "eqlNASApplianceCIFSAntivirusExcludeDirPaths": eqlNASApplianceCIFSAntivirusExcludeDirPaths,
       "eqlNASApplianceCIFSAntivirusLargeFileSize": eqlNASApplianceCIFSAntivirusLargeFileSize,
       "eqlNASApplianceCIFSAntivirusLargeFileOpen": eqlNASApplianceCIFSAntivirusLargeFileOpen,
       "eqlNASContainerDirectoryOpsTable": eqlNASContainerDirectoryOpsTable,
       "eqlNASContainerDirectoryOpsEntry": eqlNASContainerDirectoryOpsEntry,
       "eqlNASContainerDirectoryOpsIndex": eqlNASContainerDirectoryOpsIndex,
       "eqlNASContainerDirectoryRowStatus": eqlNASContainerDirectoryRowStatus,
       "eqlNASContainerDirectoryName": eqlNASContainerDirectoryName,
       "eqlNASContainerDirectoryCaseInsensitive": eqlNASContainerDirectoryCaseInsensitive,
       "eqlNASReplSiteTable": eqlNASReplSiteTable,
       "eqlNASReplSiteEntry": eqlNASReplSiteEntry,
       "eqlNASReplSitePartnershipId": eqlNASReplSitePartnershipId,
       "eqlNASReplSiteRowStatus": eqlNASReplSiteRowStatus,
       "eqlNASReplSiteVolumeReplSiteIndex": eqlNASReplSiteVolumeReplSiteIndex,
       "eqlNASReplSiteLocalClusterInetAddrType": eqlNASReplSiteLocalClusterInetAddrType,
       "eqlNASReplSiteLocalClusterInetAddr": eqlNASReplSiteLocalClusterInetAddr,
       "eqlNASReplSiteRemoteClusterInetAddrType": eqlNASReplSiteRemoteClusterInetAddrType,
       "eqlNASReplSiteRemoteClusterInetAddr": eqlNASReplSiteRemoteClusterInetAddr,
       "eqlNASReplSitePartnershipState": eqlNASReplSitePartnershipState,
       "eqlNASReplSiteUserName": eqlNASReplSiteUserName,
       "eqlNASReplSitePassword": eqlNASReplSitePassword,
       "eqlNASReplSiteRemoteClusterName": eqlNASReplSiteRemoteClusterName,
       "eqlNASReplSiteAction": eqlNASReplSiteAction,
       "eqlNASReplSiteRemoteUserName": eqlNASReplSiteRemoteUserName,
       "eqlNASReplSiteRemotePassword": eqlNASReplSiteRemotePassword,
       "eqlNASReplSiteRemoteClusterId": eqlNASReplSiteRemoteClusterId,
       "eqlNASReplSiteRemoteClusterMPV": eqlNASReplSiteRemoteClusterMPV,
       "eqlNASReplSiteRemoteNetworkAddrType": eqlNASReplSiteRemoteNetworkAddrType,
       "eqlNASReplSiteRemoteNetworkAddr": eqlNASReplSiteRemoteNetworkAddr,
       "eqlNASReplSiteRemoteNetworkMask": eqlNASReplSiteRemoteNetworkMask,
       "eqlNASReplicationTable": eqlNASReplicationTable,
       "eqlNASReplicationEntry": eqlNASReplicationEntry,
       "eqlNASReplicationId": eqlNASReplicationId,
       "eqlNASReplicationRowStatus": eqlNASReplicationRowStatus,
       "eqlNASReplicationLastRecoveryTime": eqlNASReplicationLastRecoveryTime,
       "eqlNASReplicationNextRecoveryTime": eqlNASReplicationNextRecoveryTime,
       "eqlNASReplicationSourceClusterName": eqlNASReplicationSourceClusterName,
       "eqlNASReplicationSourceFSId": eqlNASReplicationSourceFSId,
       "eqlNASReplicationSourceFSName": eqlNASReplicationSourceFSName,
       "eqlNASReplicationDestClusterName": eqlNASReplicationDestClusterName,
       "eqlNASReplicationDestFSId": eqlNASReplicationDestFSId,
       "eqlNASReplicationDestFSName": eqlNASReplicationDestFSName,
       "eqlNASReplicationStatus": eqlNASReplicationStatus,
       "eqlNASReplicationMinToComplete": eqlNASReplicationMinToComplete,
       "eqlNASReplicationTransferredPer": eqlNASReplicationTransferredPer,
       "eqlNASReplicationAction": eqlNASReplicationAction,
       "eqlNASReplPartnerInfoMapTable": eqlNASReplPartnerInfoMapTable,
       "eqlNASReplPartnerInfoMapEntry": eqlNASReplPartnerInfoMapEntry,
       "eqlNASReplPartnerInfoMapRowStatus": eqlNASReplPartnerInfoMapRowStatus,
       "eqlNASReplPartnerInfoMapClusterName": eqlNASReplPartnerInfoMapClusterName,
       "eqlNASReplPartnerInfoMapClusterSanVIPType": eqlNASReplPartnerInfoMapClusterSanVIPType,
       "eqlNASReplPartnerInfoMapClusterSanVIP": eqlNASReplPartnerInfoMapClusterSanVIP,
       "eqlNASReplPartnerInfoMapClusterId": eqlNASReplPartnerInfoMapClusterId,
       "eqlNASReplPartnerInfoMapClusterMPV": eqlNASReplPartnerInfoMapClusterMPV,
       "eqlNASReplPartnerInfoMapNetworkAddrType": eqlNASReplPartnerInfoMapNetworkAddrType,
       "eqlNASReplPartnerInfoMapNetworkAddr": eqlNASReplPartnerInfoMapNetworkAddr,
       "eqlNASReplPartnerInfoMapNetworkMask": eqlNASReplPartnerInfoMapNetworkMask,
       "eqlNASReplPartnerIdMapTable": eqlNASReplPartnerIdMapTable,
       "eqlNASReplPartnerIdMapEntry": eqlNASReplPartnerIdMapEntry,
       "eqlNASReplPartnerIdMapRowStatus": eqlNASReplPartnerIdMapRowStatus,
       "eqlNASReplPartnerIdMapPartnershipId": eqlNASReplPartnerIdMapPartnershipId,
       "eqlNASContainerCfgTable": eqlNASContainerCfgTable,
       "eqlNASContainerCfgEntry": eqlNASContainerCfgEntry,
       "eqlNASContainerCfgIndex": eqlNASContainerCfgIndex,
       "eqlNASContainerCfgRowStatus": eqlNASContainerCfgRowStatus,
       "eqlNASContainerCfgSourceClusterName": eqlNASContainerCfgSourceClusterName,
       "eqlNASContainerCfgSourceFSName": eqlNASContainerCfgSourceFSName,
       "eqlNASContainerCfgModules": eqlNASContainerCfgModules,
       "eqlNASContainerCfgRequestId": eqlNASContainerCfgRequestId,
       "eqlNASFSScanTable": eqlNASFSScanTable,
       "eqlNASFSScanEntry": eqlNASFSScanEntry,
       "eqlNASFSScanRate": eqlNASFSScanRate,
       "eqlNASReplicationHistoryTable": eqlNASReplicationHistoryTable,
       "eqlNASReplicationHistoryEntry": eqlNASReplicationHistoryEntry,
       "eqlNASReplicationHistorySampleIndex": eqlNASReplicationHistorySampleIndex,
       "eqlNASReplicationHistoryStartTime": eqlNASReplicationHistoryStartTime,
       "eqlNASReplicationHistoryEndTime": eqlNASReplicationHistoryEndTime,
       "eqlNASReplicationHistoryTransferredMb": eqlNASReplicationHistoryTransferredMb,
       "eqlNASReplicationHistoryStatus": eqlNASReplicationHistoryStatus,
       "eqlNASReplicationHistorySrcContainer": eqlNASReplicationHistorySrcContainer,
       "eqlNASReplicationHistoryDestContainer": eqlNASReplicationHistoryDestContainer,
       "eqlNASApplianceAntivirusHostTable": eqlNASApplianceAntivirusHostTable,
       "eqlNASApplianceAntivirusHostEntry": eqlNASApplianceAntivirusHostEntry,
       "eqlNASApplianceAntivirusHostIndex": eqlNASApplianceAntivirusHostIndex,
       "eqlNASApplianceAntivirusHostRowStatus": eqlNASApplianceAntivirusHostRowStatus,
       "eqlNASApplianceAntivirusHostName": eqlNASApplianceAntivirusHostName,
       "eqlNASApplianceAntivirusHostPortNumber": eqlNASApplianceAntivirusHostPortNumber,
       "eqlNASApplianceAntivirusHostTransactionState": eqlNASApplianceAntivirusHostTransactionState,
       "eqlNASChassisTable": eqlNASChassisTable,
       "eqlNASChassisEntry": eqlNASChassisEntry,
       "eqlNASChassisIndex": eqlNASChassisIndex,
       "eqlNASChassisRowStatus": eqlNASChassisRowStatus,
       "eqlNASChassisName": eqlNASChassisName,
       "eqlNASChassisRequestId": eqlNASChassisRequestId,
       "eqlNASChassisFileSystemMember": eqlNASChassisFileSystemMember,
       "eqlNASChassisModelName": eqlNASChassisModelName,
       "eqlNASChassisStatusTable": eqlNASChassisStatusTable,
       "eqlNASChassisStatusEntry": eqlNASChassisStatusEntry,
       "eqlNASChassisOverallStatus": eqlNASChassisOverallStatus,
       "eqlNASChassisChassisTag": eqlNASChassisChassisTag,
       "eqlNASChassisModel": eqlNASChassisModel,
       "eqlNASChassisSanType": eqlNASChassisSanType,
       "eqlNASChassisOverallControllerStatus": eqlNASChassisOverallControllerStatus,
       "eqlNASChassisClientNetworkSpeed": eqlNASChassisClientNetworkSpeed,
       "eqlNASChassisBackplaneNetworkSpeed": eqlNASChassisBackplaneNetworkSpeed,
       "eqlNASChassisInternalNetworkSpeed": eqlNASChassisInternalNetworkSpeed,
       "eqlNASChassisSanNetworkSpeed": eqlNASChassisSanNetworkSpeed,
       "eqlNASChassisClientNetworkStatus": eqlNASChassisClientNetworkStatus,
       "eqlNASChassisBackplaneNetworkStatus": eqlNASChassisBackplaneNetworkStatus,
       "eqlNASChassisInternalNetworkStatus": eqlNASChassisInternalNetworkStatus,
       "eqlNASChassisSanNetworkStatus": eqlNASChassisSanNetworkStatus,
       "eqlNASChassisOverallFanStatus": eqlNASChassisOverallFanStatus,
       "eqlNASChassisOverallPowerSupplyStatus": eqlNASChassisOverallPowerSupplyStatus,
       "eqlNASChassisFanStatusTable": eqlNASChassisFanStatusTable,
       "eqlNASChassisFanStatusEntry": eqlNASChassisFanStatusEntry,
       "eqlNASChassisFanName": eqlNASChassisFanName,
       "eqlNASChassisFanStatus": eqlNASChassisFanStatus,
       "eqlNASChassisFanRpm": eqlNASChassisFanRpm,
       "eqlNASChassisFanRpmRange": eqlNASChassisFanRpmRange,
       "eqlNASChassisPowerSupplyStatusTable": eqlNASChassisPowerSupplyStatusTable,
       "eqlNASChassisPowerSupplyStatusEntry": eqlNASChassisPowerSupplyStatusEntry,
       "eqlNASChassisPowerSupplyName": eqlNASChassisPowerSupplyName,
       "eqlNASChassisPowerSupplyStatus": eqlNASChassisPowerSupplyStatus,
       "eqlNASChassisControllerStatusTable": eqlNASChassisControllerStatusTable,
       "eqlNASChassisControllerStatusEntry": eqlNASChassisControllerStatusEntry,
       "eqlNASChassisControllerIndex": eqlNASChassisControllerIndex,
       "eqlNASChassisControllerStatus": eqlNASChassisControllerStatus,
       "eqlNASChassisControllerState": eqlNASChassisControllerState,
       "eqlNASChassisControllerLocation": eqlNASChassisControllerLocation,
       "eqlNASChassisControllerAmbientTemperatureStatus": eqlNASChassisControllerAmbientTemperatureStatus,
       "eqlNASChassisControllerAmbientTemperatureValue": eqlNASChassisControllerAmbientTemperatureValue,
       "eqlNASChassisControllerSystemControllerId": eqlNASChassisControllerSystemControllerId,
       "eqlNASChassisControllerBPSStatus": eqlNASChassisControllerBPSStatus,
       "eqlNASChassisControllerBPSIsAccessible": eqlNASChassisControllerBPSIsAccessible,
       "eqlNASChassisControllerBPSModel": eqlNASChassisControllerBPSModel,
       "eqlNASChassisControllerBPSCharge": eqlNASChassisControllerBPSCharge,
       "eqlNASChassisControllerCPUOverallStatus": eqlNASChassisControllerCPUOverallStatus,
       "eqlNASChassisControllerCPUCurrentCoresCount": eqlNASChassisControllerCPUCurrentCoresCount,
       "eqlNASChassisControllerOverallFanStatus": eqlNASChassisControllerOverallFanStatus,
       "eqlNASChassisControllerOverallLocalDiskStatus": eqlNASChassisControllerOverallLocalDiskStatus,
       "eqlNASChassisControllerOverallRaidControllerStatus": eqlNASChassisControllerOverallRaidControllerStatus,
       "eqlNASChassisControllerOverallVirtualDiskStatus": eqlNASChassisControllerOverallVirtualDiskStatus,
       "eqlNASChassisControllerMemoryStatus": eqlNASChassisControllerMemoryStatus,
       "eqlNASChassisControllerMemorySize": eqlNASChassisControllerMemorySize,
       "eqlNASChassisControllerBackplaneNetworkStatus": eqlNASChassisControllerBackplaneNetworkStatus,
       "eqlNASChassisControllerBackplaneNetworkSpeed": eqlNASChassisControllerBackplaneNetworkSpeed,
       "eqlNASChassisControllerClientNetworkStatus": eqlNASChassisControllerClientNetworkStatus,
       "eqlNASChassisControllerClientNetworkSpeed": eqlNASChassisControllerClientNetworkSpeed,
       "eqlNASChassisControllerInternalNetworkStatus": eqlNASChassisControllerInternalNetworkStatus,
       "eqlNASChassisControllerInternalNetworkSpeed": eqlNASChassisControllerInternalNetworkSpeed,
       "eqlNASChassisControllerSanNetworkStatus": eqlNASChassisControllerSanNetworkStatus,
       "eqlNASChassisControllerSanNetworkSpeed": eqlNASChassisControllerSanNetworkSpeed,
       "eqlNASChassisControllerOverallPowerSupplyStatus": eqlNASChassisControllerOverallPowerSupplyStatus,
       "eqlNASChassisControllerFanStatusTable": eqlNASChassisControllerFanStatusTable,
       "eqlNASChassisControllerFanStatusEntry": eqlNASChassisControllerFanStatusEntry,
       "eqlNASChassisControllerFanName": eqlNASChassisControllerFanName,
       "eqlNASChassisControllerFanStatus": eqlNASChassisControllerFanStatus,
       "eqlNASChassisControllerFanRpm": eqlNASChassisControllerFanRpm,
       "eqlNASChassisControllerFanRpmRange": eqlNASChassisControllerFanRpmRange,
       "eqlNASChassisControllerPowerSupplyStatusTable": eqlNASChassisControllerPowerSupplyStatusTable,
       "eqlNASChassisControllerPowerSupplyStatusEntry": eqlNASChassisControllerPowerSupplyStatusEntry,
       "eqlNASChassisControllerPowerSupplyName": eqlNASChassisControllerPowerSupplyName,
       "eqlNASChassisControllerPowerSupplyStatus": eqlNASChassisControllerPowerSupplyStatus,
       "eqlNASChassisControllerDiskStatusTable": eqlNASChassisControllerDiskStatusTable,
       "eqlNASChassisControllerDiskStatusEntry": eqlNASChassisControllerDiskStatusEntry,
       "eqlNASChassisControllerDiskName": eqlNASChassisControllerDiskName,
       "eqlNASChassisControllerDiskStatus": eqlNASChassisControllerDiskStatus,
       "eqlNASChassisControllerNicStatusTable": eqlNASChassisControllerNicStatusTable,
       "eqlNASChassisControllerNicStatusEntry": eqlNASChassisControllerNicStatusEntry,
       "eqlNASChassisControllerNicName": eqlNASChassisControllerNicName,
       "eqlNASChassisControllerNicState": eqlNASChassisControllerNicState,
       "eqlNASChassisControllerNicSpeed": eqlNASChassisControllerNicSpeed,
       "eqlNASChassisControllerNicSlot": eqlNASChassisControllerNicSlot,
       "eqlNASChassisControllerNicPort": eqlNASChassisControllerNicPort,
       "eqlNASChassisControllerNicDuplex": eqlNASChassisControllerNicDuplex,
       "eqlNASChassisControllerNicFlowControl": eqlNASChassisControllerNicFlowControl,
       "eqlNASDiagsTable": eqlNASDiagsTable,
       "eqlNASDiagsEntry": eqlNASDiagsEntry,
       "eqlNASDiagsStart": eqlNASDiagsStart,
       "eqlNASDiagsCaseNumber": eqlNASDiagsCaseNumber,
       "eqlNASDiagsStatus": eqlNASDiagsStatus,
       "eqlNASClientStaticRouteTable": eqlNASClientStaticRouteTable,
       "eqlNASClientStaticRouteEntry": eqlNASClientStaticRouteEntry,
       "eqlNASClientStaticRouteRowStatus": eqlNASClientStaticRouteRowStatus,
       "eqlNASClientStaticRouteNetworkAddrType": eqlNASClientStaticRouteNetworkAddrType,
       "eqlNASClientStaticRouteNetworkAddr": eqlNASClientStaticRouteNetworkAddr,
       "eqlNASClientStaticRouteNetworkMaskType": eqlNASClientStaticRouteNetworkMaskType,
       "eqlNASClientStaticRouteNetworkMask": eqlNASClientStaticRouteNetworkMask,
       "eqlNASClientStaticRouteGatewayAddrType": eqlNASClientStaticRouteGatewayAddrType,
       "eqlNASClientStaticRouteGatewayAddr": eqlNASClientStaticRouteGatewayAddr,
       "eqlNASClusterUpdateTable": eqlNASClusterUpdateTable,
       "eqlNASClusterUpdateEntry": eqlNASClusterUpdateEntry,
       "eqlNASClusterUpdateRowStatus": eqlNASClusterUpdateRowStatus,
       "eqlNASClusterUpdateFilename": eqlNASClusterUpdateFilename,
       "eqlNASClusterUpdateEQLGroupMPV": eqlNASClusterUpdateEQLGroupMPV,
       "eqlNASClusterUpdateClusterMPV": eqlNASClusterUpdateClusterMPV,
       "eqlNASClusterUpdateEQLGroupCurrentCompLevel": eqlNASClusterUpdateEQLGroupCurrentCompLevel,
       "eqlNASClusterUpdateRequestId": eqlNASClusterUpdateRequestId,
       "eqlNASClusterInfoTable": eqlNASClusterInfoTable,
       "eqlNASClusterInfoEntry": eqlNASClusterInfoEntry,
       "eqlNASClusterInfoRowStatus": eqlNASClusterInfoRowStatus,
       "eqlNASClusterInfoSiteType": eqlNASClusterInfoSiteType,
       "eqlNASClusterInfoSegmentId": eqlNASClusterInfoSegmentId,
       "eqlNASClusterInfoSegmentSize": eqlNASClusterInfoSegmentSize,
       "eqlNASClusterInfoMoreSegment": eqlNASClusterInfoMoreSegment,
       "eqlNASClusterInfoCertificate": eqlNASClusterInfoCertificate,
       "eqlNASClusterInfoClusterId": eqlNASClusterInfoClusterId,
       "eqlNASReplPartnerClusterIdMapTable": eqlNASReplPartnerClusterIdMapTable,
       "eqlNASReplPartnerClusterIdMapEntry": eqlNASReplPartnerClusterIdMapEntry,
       "eqlNASReplPartnerClusterIdMapSanVIPType": eqlNASReplPartnerClusterIdMapSanVIPType,
       "eqlNASReplPartnerClusterIdMapSanVIP": eqlNASReplPartnerClusterIdMapSanVIP,
       "eqlNASReplPartnerClusterIdMapClusterId": eqlNASReplPartnerClusterIdMapClusterId,
       "eqlNASReplPartnerConfigTable": eqlNASReplPartnerConfigTable,
       "eqlNASReplPartnerConfigEntry": eqlNASReplPartnerConfigEntry,
       "eqlNASReplPartnerConfigRowStatus": eqlNASReplPartnerConfigRowStatus,
       "eqlNASReplPartnerConfigCertificate": eqlNASReplPartnerConfigCertificate,
       "eqlNASReplPartnerConfigInetAddrType": eqlNASReplPartnerConfigInetAddrType,
       "eqlNASReplPartnerConfigInetAddr": eqlNASReplPartnerConfigInetAddr,
       "eqlNASReplTable": eqlNASReplTable,
       "eqlNASReplEntry": eqlNASReplEntry,
       "eqlNASReplRowStatus": eqlNASReplRowStatus,
       "eqlNASReplRemoteFSId": eqlNASReplRemoteFSId,
       "eqlNASReplVolumeReplSiteIndex": eqlNASReplVolumeReplSiteIndex,
       "eqlNASReplRemoteClusterName": eqlNASReplRemoteClusterName,
       "eqlNASReplRemoteFSName": eqlNASReplRemoteFSName,
       "eqlNASReplAchievedRecoveryTime": eqlNASReplAchievedRecoveryTime,
       "eqlNASReplNextRecoveryTime": eqlNASReplNextRecoveryTime,
       "eqlNASReplTargetRecoveryTime": eqlNASReplTargetRecoveryTime,
       "eqlNASReplTransferredPercent": eqlNASReplTransferredPercent,
       "eqlNASReplTransferredMB": eqlNASReplTransferredMB,
       "eqlNASReplStatus": eqlNASReplStatus,
       "eqlNASReplAction": eqlNASReplAction,
       "eqlNASReplSecsToComplete": eqlNASReplSecsToComplete,
       "eqlNASReplError": eqlNASReplError,
       "eqlNASReplRole": eqlNASReplRole,
       "eqlNASReplCurrentXferRateKbps": eqlNASReplCurrentXferRateKbps,
       "eqlNASConfigStateTable": eqlNASConfigStateTable,
       "eqlNASConfigStateEntry": eqlNASConfigStateEntry,
       "eqlNASConfigStateConfigFinished": eqlNASConfigStateConfigFinished,
       "eqlNASConfigStateHardwareReplaceInProgress": eqlNASConfigStateHardwareReplaceInProgress,
       "eqlNASClientTable": eqlNASClientTable,
       "eqlNASClientEntry": eqlNASClientEntry,
       "eqlNASClientNodeIndex": eqlNASClientNodeIndex,
       "eqlNASClientIPAddressType": eqlNASClientIPAddressType,
       "eqlNASClientIPAddress": eqlNASClientIPAddress,
       "eqlNASClientUserName": eqlNASClientUserName,
       "eqlNASClientProtocol": eqlNASClientProtocol,
       "eqlNASClientConnectedTime": eqlNASClientConnectedTime,
       "eqlNASClientIdleTime": eqlNASClientIdleTime,
       "eqlNASClientNumOpenFiles": eqlNASClientNumOpenFiles,
       "eqlNASClientIsGuest": eqlNASClientIsGuest,
       "eqlNASStatsClusterTrafficRateTable": eqlNASStatsClusterTrafficRateTable,
       "eqlNASStatsClusterTrafficRateEntry": eqlNASStatsClusterTrafficRateEntry,
       "eqlNASStatsClusterTrafficRateTimestamp": eqlNASStatsClusterTrafficRateTimestamp,
       "eqlNASStatsClusterTrafficRateNfsReadMBsPerSec": eqlNASStatsClusterTrafficRateNfsReadMBsPerSec,
       "eqlNASStatsClusterTrafficRateNfsWriteMBsPerSec": eqlNASStatsClusterTrafficRateNfsWriteMBsPerSec,
       "eqlNASStatsClusterTrafficRateNdmpReadMBsPerSec": eqlNASStatsClusterTrafficRateNdmpReadMBsPerSec,
       "eqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec": eqlNASStatsClusterTrafficRateNdmpWriteMBsPerSec,
       "eqlNASStatsClusterTrafficRateCifsReadMBsPerSec": eqlNASStatsClusterTrafficRateCifsReadMBsPerSec,
       "eqlNASStatsClusterTrafficRateCifsWriteMBsPerSec": eqlNASStatsClusterTrafficRateCifsWriteMBsPerSec,
       "eqlNASStatsClusterTrafficRateReplicationReadMBsPerSec": eqlNASStatsClusterTrafficRateReplicationReadMBsPerSec,
       "eqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec": eqlNASStatsClusterTrafficRateReplicationWriteMBsPerSec,
       "eqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec": eqlNASStatsClusterTrafficRateStorageSubSystemReadMBsPerSec,
       "eqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec": eqlNASStatsClusterTrafficRateStorageSubSystemWriteMBsPerSec,
       "eqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec": eqlNASStatsClusterTrafficRateNetworkOverheadReadMBsPerSec,
       "eqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec": eqlNASStatsClusterTrafficRateNetworkOverheadWriteMBsPerSec,
       "eqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec": eqlNASStatsClusterTrafficRateNetworkPacketDropsPerSec,
       "eqlNASStatsClusterTrafficRateNfsIOPSRead": eqlNASStatsClusterTrafficRateNfsIOPSRead,
       "eqlNASStatsClusterTrafficRateNfsIOPSWrite": eqlNASStatsClusterTrafficRateNfsIOPSWrite,
       "eqlNASStatsClusterTrafficRateNfsIOPSOther": eqlNASStatsClusterTrafficRateNfsIOPSOther,
       "eqlNASStatsClusterTrafficRateCifsIOPSRead": eqlNASStatsClusterTrafficRateCifsIOPSRead,
       "eqlNASStatsClusterTrafficRateCifsIOPSWrite": eqlNASStatsClusterTrafficRateCifsIOPSWrite,
       "eqlNASStatsClusterTrafficRateCifsIOPSOther": eqlNASStatsClusterTrafficRateCifsIOPSOther,
       "eqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec": eqlNASStatsClusterTrafficRateTotalPrimaryMBsPerSec,
       "eqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec": eqlNASStatsClusterTrafficRateTotalSecondaryMBsPerSec,
       "eqlNASStatsControllerTrafficRateTable": eqlNASStatsControllerTrafficRateTable,
       "eqlNASStatsControllerTrafficRateEntry": eqlNASStatsControllerTrafficRateEntry,
       "eqlNASStatsControllerTrafficRateIndex": eqlNASStatsControllerTrafficRateIndex,
       "eqlNASStatsControllerTrafficRateTimestamp": eqlNASStatsControllerTrafficRateTimestamp,
       "eqlNASStatsControllerTrafficRateNfsReadMBsPerSec": eqlNASStatsControllerTrafficRateNfsReadMBsPerSec,
       "eqlNASStatsControllerTrafficRateNfsWriteMBsPerSec": eqlNASStatsControllerTrafficRateNfsWriteMBsPerSec,
       "eqlNASStatsControllerTrafficRateNdmpReadMBsPerSec": eqlNASStatsControllerTrafficRateNdmpReadMBsPerSec,
       "eqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec": eqlNASStatsControllerTrafficRateNdmpWriteMBsPerSec,
       "eqlNASStatsControllerTrafficRateCifsReadMBsPerSec": eqlNASStatsControllerTrafficRateCifsReadMBsPerSec,
       "eqlNASStatsControllerTrafficRateCifsWriteMBsPerSec": eqlNASStatsControllerTrafficRateCifsWriteMBsPerSec,
       "eqlNASStatsControllerTrafficRateReplicationReadMBsPerSec": eqlNASStatsControllerTrafficRateReplicationReadMBsPerSec,
       "eqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec": eqlNASStatsControllerTrafficRateReplicationWriteMBsPerSec,
       "eqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec": eqlNASStatsControllerTrafficRateStorageSubSystemReadMBsPerSec,
       "eqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec": eqlNASStatsControllerTrafficRateStorageSubSystemWriteMBsPerSec,
       "eqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec": eqlNASStatsControllerTrafficRateNetworkOverheadReadMBsPerSec,
       "eqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec": eqlNASStatsControllerTrafficRateNetworkOverheadWriteMBsPerSec,
       "eqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec": eqlNASStatsControllerTrafficRateNetworkPacketDropsPerSec,
       "eqlNASStatsControllerTrafficRateNfsIOPSRead": eqlNASStatsControllerTrafficRateNfsIOPSRead,
       "eqlNASStatsControllerTrafficRateNfsIOPSWrite": eqlNASStatsControllerTrafficRateNfsIOPSWrite,
       "eqlNASStatsControllerTrafficRateNfsIOPSOther": eqlNASStatsControllerTrafficRateNfsIOPSOther,
       "eqlNASStatsControllerTrafficRateCifsIOPSRead": eqlNASStatsControllerTrafficRateCifsIOPSRead,
       "eqlNASStatsControllerTrafficRateCifsIOPSWrite": eqlNASStatsControllerTrafficRateCifsIOPSWrite,
       "eqlNASStatsControllerTrafficRateCifsIOPSOther": eqlNASStatsControllerTrafficRateCifsIOPSOther,
       "eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec": eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSec,
       "eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage": eqlNASStatsControllerTrafficRateTotalPrimaryMBsPerSecToAverage,
       "eqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec": eqlNASStatsControllerTrafficRateTotalSecondaryMBsPerSec,
       "eqlNASStatsControllerLoadBalancingTable": eqlNASStatsControllerLoadBalancingTable,
       "eqlNASStatsControllerLoadBalancingEntry": eqlNASStatsControllerLoadBalancingEntry,
       "eqlNASStatsControllerLoadBalancingIndex": eqlNASStatsControllerLoadBalancingIndex,
       "eqlNASStatsControllerLoadBalancingTimestamp": eqlNASStatsControllerLoadBalancingTimestamp,
       "eqlNASStatsControllerCPULoadPercent": eqlNASStatsControllerCPULoadPercent,
       "eqlNASStatsControllerTotalCifsConnections": eqlNASStatsControllerTotalCifsConnections,
       "eqlNASCacheInfoTable": eqlNASCacheInfoTable,
       "eqlNASCacheInfoEntry": eqlNASCacheInfoEntry,
       "eqlNASCacheInfoIndex": eqlNASCacheInfoIndex,
       "eqlNASCacheInfoCacheObjectName": eqlNASCacheInfoCacheObjectName,
       "eqlNASCacheInfoCacheObjectExpiryTime": eqlNASCacheInfoCacheObjectExpiryTime,
       "eqlNASCacheInfoCacheObjectState": eqlNASCacheInfoCacheObjectState,
       "eqlNASCacheInfoAction": eqlNASCacheInfoAction,
       "eqlNASReplHistoryTable": eqlNASReplHistoryTable,
       "eqlNASReplHistoryEntry": eqlNASReplHistoryEntry,
       "eqlNASReplHistoryUniqueId": eqlNASReplHistoryUniqueId,
       "eqlNASReplHistoryEventTime": eqlNASReplHistoryEventTime,
       "eqlNASReplHistorySourceContainerName": eqlNASReplHistorySourceContainerName,
       "eqlNASReplHistorySourceClusterName": eqlNASReplHistorySourceClusterName,
       "eqlNASReplHistoryDestContainerName": eqlNASReplHistoryDestContainerName,
       "eqlNASReplHistoryDestClusterName": eqlNASReplHistoryDestClusterName,
       "eqlNASReplHistoryStartTime": eqlNASReplHistoryStartTime,
       "eqlNASReplHistoryEndTime": eqlNASReplHistoryEndTime,
       "eqlNASReplHistoryTransferredMb": eqlNASReplHistoryTransferredMb,
       "eqlNASReplHistoryStatus": eqlNASReplHistoryStatus,
       "eqlNASTaskTable": eqlNASTaskTable,
       "eqlNASTaskEntry": eqlNASTaskEntry,
       "eqlNASTaskIndex": eqlNASTaskIndex,
       "eqlNASTaskRowStatus": eqlNASTaskRowStatus,
       "eqlNASTaskType": eqlNASTaskType,
       "eqlNASTaskContext": eqlNASTaskContext,
       "eqlNASTaskNumSubTasks": eqlNASTaskNumSubTasks,
       "eqlNASTaskSubTaskInProgress": eqlNASTaskSubTaskInProgress,
       "eqlNASTaskSubtaskStatus": eqlNASTaskSubtaskStatus,
       "eqlNASTaskStatus": eqlNASTaskStatus,
       "eqlNASTaskUserAction": eqlNASTaskUserAction,
       "eqlNASTaskStartTime": eqlNASTaskStartTime,
       "eqlNASTaskContainerReplInfoTable": eqlNASTaskContainerReplInfoTable,
       "eqlNASTaskContainerReplInfoEntry": eqlNASTaskContainerReplInfoEntry,
       "eqlNASTaskContainerReplInfoRowStatus": eqlNASTaskContainerReplInfoRowStatus,
       "eqlNASTaskContainerReplInfoRemoteFSId": eqlNASTaskContainerReplInfoRemoteFSId,
       "eqlNASTaskContainerReplInfoVolumeReplSiteIndex": eqlNASTaskContainerReplInfoVolumeReplSiteIndex,
       "eqlNASTaskContainerReplInfoRemoteClusterName": eqlNASTaskContainerReplInfoRemoteClusterName,
       "eqlNASTaskContainerReplInfoLocalFSName": eqlNASTaskContainerReplInfoLocalFSName,
       "eqlNASTaskContainerReplInfoRemoteFSName": eqlNASTaskContainerReplInfoRemoteFSName,
       "eqlNASTaskContainerReplInfoLocalClusterId": eqlNASTaskContainerReplInfoLocalClusterId,
       "eqlNASTaskContainerReplInfoTaskId": eqlNASTaskContainerReplInfoTaskId,
       "eqlNASLostContainerTable": eqlNASLostContainerTable,
       "eqlNASLostContainerEntry": eqlNASLostContainerEntry,
       "eqlNASLostContainerRowStatus": eqlNASLostContainerRowStatus,
       "eqlNASLostContainerName": eqlNASLostContainerName,
       "eqlNASLostContainerCapacity": eqlNASLostContainerCapacity,
       "eqlNASLostContainerUsedSpaceAlert": eqlNASLostContainerUsedSpaceAlert,
       "eqlNASLostContainerSnapshotUsedSpaceAlert": eqlNASLostContainerSnapshotUsedSpaceAlert,
       "eqlNASSanStaticRouteTable": eqlNASSanStaticRouteTable,
       "eqlNASSanStaticRouteEntry": eqlNASSanStaticRouteEntry,
       "eqlNASSanStaticRouteRowStatus": eqlNASSanStaticRouteRowStatus,
       "eqlNASSanStaticRouteNetworkAddrType": eqlNASSanStaticRouteNetworkAddrType,
       "eqlNASSanStaticRouteNetworkAddr": eqlNASSanStaticRouteNetworkAddr,
       "eqlNASSanStaticRouteNetworkMaskType": eqlNASSanStaticRouteNetworkMaskType,
       "eqlNASSanStaticRouteNetworkMask": eqlNASSanStaticRouteNetworkMask,
       "eqlNASSanStaticRouteGatewayAddrType": eqlNASSanStaticRouteGatewayAddrType,
       "eqlNASSanStaticRouteGatewayAddr": eqlNASSanStaticRouteGatewayAddr}
)
